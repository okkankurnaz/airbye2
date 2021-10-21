import React from "react";
import styled from "styled-components";
import { FormattedMessage } from "react-intl";

import Modal from "components/Modal";
import { Button } from "components/base/Button";

type ConfirmationModalProps = {
  onClose: () => void;
  title: React.ReactNode;
  text: React.ReactNode;
  submitButtonText: React.ReactNode;
  onSubmit: () => void;
};

const Content = styled.div`
  width: 585px;
  font-size: 14px;
  line-height: 28px;
  padding: 10px 40px 15px 37px;
  white-space: pre-line;
`;

const ButtonContent = styled.div`
  padding-top: 28px;
  display: flex;
  justify-content: flex-end;
`;

const ButtonWithMargin = styled(Button)`
  margin-right: 12px;
`;

const ConfirmationModal: React.FC<ConfirmationModalProps> = ({
  onClose,
  title,
  text,
  onSubmit,
  submitButtonText,
}) => (
  <Modal onClose={onClose} title={title}>
    <Content>
      {text}
      <ButtonContent>
        <ButtonWithMargin onClick={onClose} type="button" secondary>
          <FormattedMessage id="form.cancel" />
        </ButtonWithMargin>
        <Button type="button" danger onClick={onSubmit} data-id="delete">
          {submitButtonText}
        </Button>
      </ButtonContent>
    </Content>
  </Modal>
);

export default ConfirmationModal;
