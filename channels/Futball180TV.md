<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/Ti1O9aqglQnYjMQoZM_BoWTSryUcqq8TSN88pvfwLLu2wLv3XBC4qBZEsHSbVMbR_t6X-oJx9wg2t7hsPg87y4iHgmcqoNi0gKeJQRLDAdGzHL_1WrVTlrMTWsrnnXmz6XtNjm6eSNYjO0UQ8U2CW1wvzMy0cJtHYpidDiLuvq3oL197Zb-Uc2FBW53nU2Tc3zb3NFslsdKz65ThtoJpwxS0Uk7oKKGktdBXard5v8DOdsxk6Dn8kZOR3bM_ewciWjcwTWimJWjgnUgeFyCsUP7WMproGMjfWX_LffX7MLdOR6vnBxyJ7XCKWLoPbp6FPLS2bxWoCMYDsDdYoyYOVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 574K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 21:13:29</div>
<hr>

<div class="tg-post" id="msg-100301">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRV6YNt6u_onayD43WTfz65LCug3NSg_EkAgzlvSlq-gnlCssWkf4QPfvxHCX00xclHxcBTkebLlEm8csFxUWiUg9T92g9ZKp6YaHvp35TGKCs43TxCFRdxLxZ1DlqtoHDcpXjMqbPW-jV7BXfKAyB397qjUZ2qf8MN5rZ-O1PA5lZnQm6JaAt9EEFFSNR1taybbSo5ci9bP_7EYe7Wpit0qniQTiUGLKUA1OOVW-kVauQFTR2LgFmQgJvN9G7YGqDkTo-_tf1PcQ4j0TiSIAHkloFJ8a5tA92o2sUsBkMbfHSZK2TmWJKjVuGMBBIfL50OcIX5OzmqaPpJvHTr--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🚨
قهرمانان وارد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/100301" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100300">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDVT9Ww2VKUUcGr-zPFIFs7UJy_I56OD8hQ1xs6zQPy77NE9Pd64JdmkQjVNIfTLX3WIKef_wfyKi-6Mo5x6ZJOeqMKOwsfAT3Ga_9qyZcloZ1Fyz7FfT1UGGrqyy9FtkuxP5DP72pXUZKPf_8Uie_-FHhYPp1ntn-LlaWHB5OpZ1K2eK0gt42PvbYOW6BBp-IQnShq4hWEJOivQatWhKifa5SHnlcU673Xs7kuPJCJYY7Lx7_LLU2A-JC2Vc06J_sHWWeiPtV3bnIiFxdniu_CG2rADhmEQHtBfXpKvz9vMQvHvXmCU1RZ57j0eIEvyY_75wZVaoO0p4aum71FwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
ورود آخرین سنگر رئالی‌ها به استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/100300" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100299">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG3A1AQ0EnRe8JXtosygNwhC-wTthyL1-mIHhuehTdW_o_c-2oSaZHgmkmHeIZS6D5vnxboSaIerG4ccCA3WtxbNuFmhYrL236EmWLK-oMn1kBTpakarkE_IfpvzBKngLJt92nhayQgzYPbXtbfe74VlTqxsg0rEg86-LjTaveIE1nXE6swe0gxhtEof2kFryF2TmLmpq7PpqB7GK3_i8DXepZrmaW1n8QLx9IWDJL5ZeUzcztat7jboMPDU_d-gTpcA6CuyfEvuVT3x27kx7ScgKcxPlPF8U_MTzBvge_lm0Q3r9niUL446mOGTHhVR37XlyVy9N8-8PXCHG56Yqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیییببببببببب آرژانتین مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/100299" target="_blank">📅 20:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100298">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHW3N_n_lo2Gtd5qULMzcZ4Q9u2AjMSMiclhX0Zjq-Zo_vH8uDhLrriM7dmWj0w0TualbvGNZF4LR549smggC83pKDZttCEYKIG97aNqcGnWN9TGLlHCfgeiJ7Kusfkdkxq_K9pPPnyMAgnjLpN3uX9l4i7kq23bEdSfTwZMY_gsDYVaAd_Y-uWpOyIsLww_Tp5BEmPYJUH5M-gEbq6N8qu9XIB920dAKgUSvMgH7VCUBkxaCAv9JwFAwenYnr1TySICF4dofhxFDP2JtJoyhZ2H_GvPfxxZXqSJjPTxzP2Rhqt8tdrB7sWOq4h28lotwnf1gIHZDKw1kAFyGPoEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیییببببببببب آرژانتین مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/100298" target="_blank">📅 20:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100297">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i65ivrBB21oeUlqKze-fxTVUkmKbOn5Q3Xado_SBnDcq-o5qv-UfWqfIMBhj2-fKgvHCdoOcHBSkADvsevSKmzL1v0Ccw5WZdjVY8xBKFCBpi1hGBqr0zdk6JNpAmYF1342LsaYV1W1jgdztTS-4ZCOd9QXsamQsXbfE6xb8ly5L5qwftyDxOhdPsGNaTGsYF8MlS9o4EhUSpcatd2YgOf19omGlD6zMbTv8CHB2fdJOYTY3UbnSxlY_DQP9XzK2ZC1WMyi9oYvSp_bLola0REzEaUD7gBPnGPogIqdn4y3WT0RB3k19FMrelXulkJqXLYARLsEoStta7690VnY7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رختکن آرژانتینو ببین پسر
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/100297" target="_blank">📅 20:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9271b4e2.mp4?token=bjXjtcKsAWhy_1c7eDZw8FlLj4F0HcKbK0P9XIZaUNYVEFaMOot6qIecJNS8-62lPhZAF7FXGH0VRjBr5M-eFhYZgvFYL36OOW1N6UQ9dyMJ_pxyL7BBZg1_SEHQ_DnGKEfEhDHSH8j4_K9p7Rl1bR7NY9n1frPF09XnXoPJhR_xt_-1gCVjpQaH6EWA1K4E8eZUHfPWoPxRwqcJ4bdHRcd-xEHqjf-BsUVkzE3IN4u4_PFKZxt-_S16temiGyrsr-ChmRgCFVvzrGy2yrVaCJt3YKtYOuUQkFxownYVPVMDlQQ0KziC6yHwRvhLrTtSbZH87e7i1u_gkCh0GtCB8YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9271b4e2.mp4?token=bjXjtcKsAWhy_1c7eDZw8FlLj4F0HcKbK0P9XIZaUNYVEFaMOot6qIecJNS8-62lPhZAF7FXGH0VRjBr5M-eFhYZgvFYL36OOW1N6UQ9dyMJ_pxyL7BBZg1_SEHQ_DnGKEfEhDHSH8j4_K9p7Rl1bR7NY9n1frPF09XnXoPJhR_xt_-1gCVjpQaH6EWA1K4E8eZUHfPWoPxRwqcJ4bdHRcd-xEHqjf-BsUVkzE3IN4u4_PFKZxt-_S16temiGyrsr-ChmRgCFVvzrGy2yrVaCJt3YKtYOuUQkFxownYVPVMDlQQ0KziC6yHwRvhLrTtSbZH87e7i1u_gkCh0GtCB8YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آرژانتین و انگلیس؛ مسابقه‌ای فراتر از فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/100296" target="_blank">📅 20:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cfzdlpv_DCD5T62DYwEob7pwj03CoKjwbJS9Y4CSEs8UgKMCNO9W3KZn9qYkQT7rmsXTdzihLl-sFuL9RZif5Fk7Viiyr9f0NCINWFMIGxc2QKARpAF5oDtFL8Qb4EiKiauk2GzMeNaMdAstg7p7Qh3db4HuNSPRVyJS9E_lFHP8Buyr3johz0iy9rZKp53zn2vAu8SZrZkddXKK7ZMn-VmouffwNMiRNLo8v37VR3oaIr-kFB0rEGtp0Z6ryW7ooY5CatT2nPtxfpW3UEktNSRYtrUCtiGVPrLy6gvxve2Yiwo_2IYNYvU5A0PP3jK4q1SnW9GW08jzLzyj4NcZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
رومانو: پیر امریک اوبامیانگ با عقد قراردادی به تیم دپورتیوولاکرونیا در لالیگا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/100295" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100294">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPA9mQP9jQu5AOBbxGHDHGISzPklYx3kmSBK_ovhG8fJBIG0YSlZ1Q-yx5mBOwZ5zXfFNxt_YiQYqt12oBQxIff3DM7KqY3XzRm4-OIuGPGs_VXFCJy61jxJFUxRPXVj2nX7CcF45SKWo3C5_SWwyugldyAuOYgTVr2BwugzJialTJhfUSndrmTwIOTC1U42gPl_yc5IE0dcQ5V5t2hJAZdO4fEGvEFOpAGQp38iWwaqBvGYBXcKzC6GlkbEdj4n1UOLpBnOPCCYqVhMqXsr01FYktMw1oxlbW2RuFHKayoqDnPTOeCqjAC2M52knXDJkhcpMMyu0Vh-_j6101L-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
😈
والیبال ایران تو نخستین بازی هفته سوم لیگ‌ملت‌ها مقابل اوکراین هم شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/100294" target="_blank">📅 20:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100293">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5NNAkTgbxUiOYn1jGTcMcAQtlYY7SGB1DzUvNJSVbNiTvJrVhPUi2bXtbStFeU07DUqVctHGuKvvSABt4Xc16OhvCJiYeLiai3kUwApxQLB_wD6dBLTUbbsD0SKQUpAL-XrvMbEqFSWHWGf0ksefRbzBbAkAGREbuw1xiNxjS-trDlF44GVXsFgk2e4Rggnd0wJlihbnM6jUWdtkDt1vyh_Yx5vB4LArXaYu7830tcIJyqYbl7h5HMNc0YXR2CF-vOfmACg1rbtdzFJpSdQwvtAkI-HDwP5TPtMflDUxXPnecN8jFv6ahl438TrbsW6QFxzZeNGTNqz8j5Yh9S85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
📊
پیش‌بینی‌های Opta برای مسابقه امروز:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
احتمال صعود انگلیس: 50.9%.
🇦🇷
احتمال صعود آرژانتین: 49.1%.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/100293" target="_blank">📅 20:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6vSMjGUAolPeIkUqvfNcd1m6ZWv731GerAjUdD5pb3eBK75-nDt-HxOI3gKb8YgGZ8nhguDR4Skza0Epeev9eztyy4Gpq2NYWzJk4mVtHl5CZFfhfqw4yjVewg553OJYlQEncoVJePXfSFtKbDV0mwx9q6eoUFJfEiaEip9Hp-M7uhttYbo2w6zQFM9oNVnxrsbbxZrxQJi6vFk4Y72il4ryszGdUOlAW_k3AzHSSSEGCQRG20IpENt6_-0udZGt9MONi9T7m2sfXgYkYG2-lljCTJyLxTKJDFHJAIHfPnS0rm9UTDfgC1YdWxpwOiWoAHsp-jWHWmG7Q6fBKkP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
اوه اوه قابو ببینید امشببببببب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/100292" target="_blank">📅 20:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100291">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBON5mBHLgfeyviGB6Bnnmau6JDp6EQ4EKB8t38afjSdnhbinW7I9N0nHIEYYJxXXc58QYwO2BeXSOvShbEkfl9a7cIyEJuNAZe-htraDfNfLZJaUYzax7fP-2IUEEtqwSrg_1FJdDH3HmB_0NEgUo7Zc3tl38A0EJvBKlR6BHmZtkjsO9KhZ7ZXF4Tp0mTnNJdcl73LpHsZ2qtnyjDZ6ey1X_5h7_0WR6nsj4pf6-crtKYkwXKSPW6-RHTjX3FD0HDVUHCiBxwKYsgSDSfzmg8WYDaeD8WylwVK8S2zody90G5TZyiJSl-jg5JbsZW-7Amed4K2n4pw7GszoJ4rGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد تیم انگلیس در مرحله حذفی مسابقات در برابر تیم‌های آمریکای جنوبی:
تعداد بازی‌ها (9)
🏟
تعداد پیروزی‌ها (4)
✅
تعداد شکست‌ها (5)
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/100291" target="_blank">📅 20:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77629477f.mp4?token=Oagpd2toYyewTSBLVvkMPJsmLUc7N1vEm7HCDG6KlppvwzZSP5dS2xlBMEiqyRNgoXtaEHqhCUW7c0F7kbeyXKDCOMNw8O3VdNXKAOId4uEb5aFrgK5G8dFgkfnTnF7xzmxe5jwyCSCP3SBdPovC3bAaFpXS2sdZjGlYLOiwpMSB2jiqTspa9OSGZPa3de1bKSyimu09Rl-SyPSKVL3kny0uO4UA-gCX7OYVY3oRC9LNEI9xVeNW-Hz2XJiWQPjSyMibjXoV6QLU2_5GH42advAdGTTrZvv3LK-E9Q4VUl-wqPlkyNd1B9-JDE2yDJXlXJGZMzga8xoV2D1doWA3Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77629477f.mp4?token=Oagpd2toYyewTSBLVvkMPJsmLUc7N1vEm7HCDG6KlppvwzZSP5dS2xlBMEiqyRNgoXtaEHqhCUW7c0F7kbeyXKDCOMNw8O3VdNXKAOId4uEb5aFrgK5G8dFgkfnTnF7xzmxe5jwyCSCP3SBdPovC3bAaFpXS2sdZjGlYLOiwpMSB2jiqTspa9OSGZPa3de1bKSyimu09Rl-SyPSKVL3kny0uO4UA-gCX7OYVY3oRC9LNEI9xVeNW-Hz2XJiWQPjSyMibjXoV6QLU2_5GH42advAdGTTrZvv3LK-E9Q4VUl-wqPlkyNd1B9-JDE2yDJXlXJGZMzga8xoV2D1doWA3Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🏆
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/Futball180TV/100290" target="_blank">📅 20:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=M_BjITrIk6fTWIBEFAZGDYoFAgXPoXJpG8EsjnkWnX4ztRwDoi2LARhaEFVIbKWvuVJmC7yn7GMLKyFBAHKyXfhMTqJ8vpu_JA4Mek1BMsdQtGbdxSeb4gBHGdyjP1h271jJh3dldeImRwynm88atL1WM_OcSKWEjbdKf0UvP3TVoS3a08MEMxlimJtOj4LnCWQ8HuziIU-oKVbWtkR5Q7RAaT6Rn_IfHHuzS0G0wlsTj8eTb-JLPYwxSuHpyIDP8XF5PGfqVVDSj1qb13gBv6dFAY00gIspaFP83zAsqVKgM7t2R2EFb37p7jl9p9bZZoWOiBKye2jQ1gpF-Vv-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=M_BjITrIk6fTWIBEFAZGDYoFAgXPoXJpG8EsjnkWnX4ztRwDoi2LARhaEFVIbKWvuVJmC7yn7GMLKyFBAHKyXfhMTqJ8vpu_JA4Mek1BMsdQtGbdxSeb4gBHGdyjP1h271jJh3dldeImRwynm88atL1WM_OcSKWEjbdKf0UvP3TVoS3a08MEMxlimJtOj4LnCWQ8HuziIU-oKVbWtkR5Q7RAaT6Rn_IfHHuzS0G0wlsTj8eTb-JLPYwxSuHpyIDP8XF5PGfqVVDSj1qb13gBv6dFAY00gIspaFP83zAsqVKgM7t2R2EFb37p7jl9p9bZZoWOiBKye2jQ1gpF-Vv-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوري در باران بانک کشاورزی، از برندگان
۹۳میلیون‌تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
🎁
اسامی برندگان تا این لحظه
https://www.bki.ir/fifa2026lottery
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/Futball180TV/100289" target="_blank">📅 20:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5wqLS4cZ5n32PnIxVL5ma223f04pMLrbhZtIwJnfNsidPTAwDPjNfpg3ikZUupXIYUxOCGeYLDPp7Xt18kOQKah0w89b4cHHjRXE56FLIxjRbntTkMvhWu1b5e-r-YWqDh8xxEzUg4hEUAI1jc2wDNHG9SvRbi_D9l5w-wxvCX2Hueh4Wm8sW4QcSoQS0l_KwDM7Rr-3mx-NCK5mbV3SvqyyXB6TpcMRuomEG7yIQD2fGR_pLYmiiMS16vTE5luUMTo9GeaMR2hVJv0L_vvtdAvgNCevY3OlMFkW6BfuQhqn91yB18P868eTAsYHvSto6aJBMhy1yYnlJiDtIFMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رابرت لواندوفسکی:
دوران من در بارسلونا به پایان رسید، و تصور نمی‌کردم خودم را در هیچ باشگاه اروپایی دیگری ببینم. علاقه من به بارسلونا بسیار زیاد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/100286" target="_blank">📅 19:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f352f457be.mp4?token=tk0xwW3B-5I26UhK5c_zu4HXke8bwEuJf3aCLG6sCUmnqmBArxhIdR0xxhZXH8YWAv9qNACJ9hBzamjO-O-i6wuz8DC5XGCUVYNqrZ9EOQDG9v_uYLLDZ7nAT1k6TC1SThlp4EDJxLR3VaLjQ0U7m4xx3wyYq8I3lGtZ6CkA-FeEBJgiKuxZMRJidji1jvDVk2CriVBS991e6tncKB3_UJYi0yJyRzYWrK5OcdjDb7aAJZBYLUPigSKhyFP7roEp_22H7pxTq_B5-V9NTWsbouOG6QV5rs20_L_8TvqYJyC4hvn4e1dWAq7YAWrZ2dRr33dX-ZnDtL-yVwLLkgHptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f352f457be.mp4?token=tk0xwW3B-5I26UhK5c_zu4HXke8bwEuJf3aCLG6sCUmnqmBArxhIdR0xxhZXH8YWAv9qNACJ9hBzamjO-O-i6wuz8DC5XGCUVYNqrZ9EOQDG9v_uYLLDZ7nAT1k6TC1SThlp4EDJxLR3VaLjQ0U7m4xx3wyYq8I3lGtZ6CkA-FeEBJgiKuxZMRJidji1jvDVk2CriVBS991e6tncKB3_UJYi0yJyRzYWrK5OcdjDb7aAJZBYLUPigSKhyFP7roEp_22H7pxTq_B5-V9NTWsbouOG6QV5rs20_L_8TvqYJyC4hvn4e1dWAq7YAWrZ2dRr33dX-ZnDtL-yVwLLkgHptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
اندر احوالات امشب هری‌کین:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/100285" target="_blank">📅 19:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtIfOg3YF8L961vf3HeUkQJEKYSHocv1uwmzTpsVjDTWKf3s7JjJ4h3mRp8i1wGn6Rh8I0nyw88kVnbCWaqTwxtmPlWZndxJyGegCU7-19k5GVEhBePCvgU12XAIR7WXlOxHT8hjJEwVwtqQVysIVBxKkPmfoQ2i2AhHzLmALU7VUGSipznJgW1dJ_ifqVukD4ZEf0GjZD31VzKWescMqKF8jFiOadgoSRXuKB19y2QeMHJH7E7gcR9VkVKtUAduXUEHDVQngV5JKwzL53Jv0e2A5kAzACa74sW_YDCV1a3c-u8Paxuu6bE884LDWkfScDKZSlDfPVVIO0qbRHDDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/Futball180TV/100284" target="_blank">📅 19:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100282">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdbb004ed.mp4?token=kshs2IzSsOdFNXhT0TFJC2XtpuExIcALnq85tBoM1V0_phuZSSh5r1T16fVqgNpUcJ2I28uOuS_856byP7gkSMOFmamo90IPUDIKVlGEOo1zGBwhqjo0gNzWikrEeUkwzkvsdS8oPN9jPMR0HFw0hCzf4nJoMElW0sBHVyjtTQz12HjeHIgndB7LAXPr0W5w_IG1xz2EGSDtyFmM_hNjxMKZGC_hrHKSxxm95e-Bqh0K_CkUZWSymW9-qgYmMjHcF-pic98vt7r7UL5cWLfYEQ54x6OgvXGssJ4wEy0907iRZLGFkOz0d61RbSjZTsNBpwp4iNoyLJbqSKyl5gcI7K5fbeD1GIcXEfkb5MIC67kb8I4CSo2IHZ9LNQPBbOE0HLuGO5s--OrwJEClHbRcSPyfOCZifVnc4R5JK74FrOC5-xk48L63SFJ2LIp_GqwTllpp0LP16Fpv4rnSkPVcl1m-G88j9qlkZxO8LgvrPcgCjyK2J8AZm6uRIbUOjKVnNY8XoH1YfCkyn_7oMm8_syu3jOmIPTciZFxq2G0HNM0UUt190V3CqYeH2VSouHYgjCGxtmsP_RUI9EfxS3af3UZ_MbDMRVZSfOq6kqu-2VBL4LHN070BkU_nnFUMZxlzr_mnJX7yxQ1bKld49o67hslmcCeUXPqjITW7_iZhbWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdbb004ed.mp4?token=kshs2IzSsOdFNXhT0TFJC2XtpuExIcALnq85tBoM1V0_phuZSSh5r1T16fVqgNpUcJ2I28uOuS_856byP7gkSMOFmamo90IPUDIKVlGEOo1zGBwhqjo0gNzWikrEeUkwzkvsdS8oPN9jPMR0HFw0hCzf4nJoMElW0sBHVyjtTQz12HjeHIgndB7LAXPr0W5w_IG1xz2EGSDtyFmM_hNjxMKZGC_hrHKSxxm95e-Bqh0K_CkUZWSymW9-qgYmMjHcF-pic98vt7r7UL5cWLfYEQ54x6OgvXGssJ4wEy0907iRZLGFkOz0d61RbSjZTsNBpwp4iNoyLJbqSKyl5gcI7K5fbeD1GIcXEfkb5MIC67kb8I4CSo2IHZ9LNQPBbOE0HLuGO5s--OrwJEClHbRcSPyfOCZifVnc4R5JK74FrOC5-xk48L63SFJ2LIp_GqwTllpp0LP16Fpv4rnSkPVcl1m-G88j9qlkZxO8LgvrPcgCjyK2J8AZm6uRIbUOjKVnNY8XoH1YfCkyn_7oMm8_syu3jOmIPTciZFxq2G0HNM0UUt190V3CqYeH2VSouHYgjCGxtmsP_RUI9EfxS3af3UZ_MbDMRVZSfOq6kqu-2VBL4LHN070BkU_nnFUMZxlzr_mnJX7yxQ1bKld49o67hslmcCeUXPqjITW7_iZhbWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
وضعیت پشم‌ریزون آرژانتینی‌ها قبل از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/100282" target="_blank">📅 19:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100281">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbnW1ufWkkUr3WuIT0PAwOHom0PQYj1XSwn1nBHUdCQ7-C9t4ukOnPCTWA0w8RxQCMYVKRODkVOj6urqCSPWqyCN67sLuMZ0q6XOzHxPTz8Atsi0CX3LheBCL-wJtbFFDFBqGKFLnBev8_fCLWBYhGkHSH8gshAyDYevhvRUv3qDY8GthUG4_lbNe5GEDunubCZXoSjq0YVzAVJSr5e-vZtE2-GCRVPqrcbrNAXHt_es4Cpe2WuimbJtA1quXesM5cK01dYhqQA-0NqwLT88rNdSqtNjZmrvGZnRnMxCwMVQB0kUH7pArf3NsvPjC8w-1VcXzUC8QfKuWbOBP4N0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
منتخب بازیکنان انگلیس و‌ آرژانتین در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/100281" target="_blank">📅 19:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100280">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86153be47.mp4?token=cM-jQNimo5Vd7ls96UYUWkmkPvd3hta8xAKuHs-SnpOZbjkfKY2-lrCKBJLLyBIsAdeoaZS4GfeAyJZ-Ktg2f46ZPHmvtMIbqiNLloSu9KlKp7J7Y_hrZo7TFP4_5751-GSPsgulcDm2uV2Kim08X6jUmWPI3OpWCgEcdWU0giz5BKiZssFF6gJ3fs7jM_f33jcov8s1QDT-QhbiNNdxHKHtYdiPMmKnf8qNuJPyOl83jz_lzvPrllDtym8t6UTcPwS3HzZSTEquFK2v8N5l_lOKc_jbZMLn8FaOIqOLNtvrV2W903jId3I9S2HEtE_lILEkdNbXlslgbRgBbvXnAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86153be47.mp4?token=cM-jQNimo5Vd7ls96UYUWkmkPvd3hta8xAKuHs-SnpOZbjkfKY2-lrCKBJLLyBIsAdeoaZS4GfeAyJZ-Ktg2f46ZPHmvtMIbqiNLloSu9KlKp7J7Y_hrZo7TFP4_5751-GSPsgulcDm2uV2Kim08X6jUmWPI3OpWCgEcdWU0giz5BKiZssFF6gJ3fs7jM_f33jcov8s1QDT-QhbiNNdxHKHtYdiPMmKnf8qNuJPyOl83jz_lzvPrllDtym8t6UTcPwS3HzZSTEquFK2v8N5l_lOKc_jbZMLn8FaOIqOLNtvrV2W903jId3I9S2HEtE_lILEkdNbXlslgbRgBbvXnAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
از هواداران ایرانی تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/100280" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100279">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f9899ffa.mp4?token=Oc6iP4ClgtL7jWOOARiYE12FMwmP2OtyPGHwol14ArbaVbt879DHe2dG0ruGrHX7qmie2lzllZh75nkRXk0bL6z_4_xqgQFVafCTaRxkWlTsNPWwbQ_qP2O5Vzti6Uli1h-TfV5FG0m9t0JYgYa25szrYAkViN4YLsapVZy1XG3fX2Seprofd91EJbpvegU1QU9sXzINgAKLBpjwGZcelAq5SiI0_W6mYCo9rRw1uE0GkGl9UDgoj5O-juIjJxGQ5Nm5f013Ak0qkUvFzFw1CGImSRvQ8VdKgWBd7bRQ6t7HVMTNwqaFTZpawx9Kc_WVXasdUKfYKP-dIbWo4XV-UHX1MnsarhE571MVvVplr4HoTvnXoEUE4HruwcFNPC3ARWV8_QvGW8O55aIROahheKamJ9qVTzaqjBkb9B8PcGLuElsEVrazicIi2oWiSIlA1adrHL9RCeBWrmdN4sl13UjD0necqFIsCYldX9Vknsxmz7xL2azTuwqmuGBUEJyNm7XX4EOpoyXnD0XfvKzvG4snoI18UC5ZACPfUHghS4OK065MDLUie0-P-HW8SRPPPHTvhXrLEif3txDHVLAH3WOeOjOiz-L3_SnpoUtbOin6oXx4iR_mJEvptzJ8X5DIypeXofmJh7MCmqwROJCUnflHsJAxgeuI8T-rA3vgXt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f9899ffa.mp4?token=Oc6iP4ClgtL7jWOOARiYE12FMwmP2OtyPGHwol14ArbaVbt879DHe2dG0ruGrHX7qmie2lzllZh75nkRXk0bL6z_4_xqgQFVafCTaRxkWlTsNPWwbQ_qP2O5Vzti6Uli1h-TfV5FG0m9t0JYgYa25szrYAkViN4YLsapVZy1XG3fX2Seprofd91EJbpvegU1QU9sXzINgAKLBpjwGZcelAq5SiI0_W6mYCo9rRw1uE0GkGl9UDgoj5O-juIjJxGQ5Nm5f013Ak0qkUvFzFw1CGImSRvQ8VdKgWBd7bRQ6t7HVMTNwqaFTZpawx9Kc_WVXasdUKfYKP-dIbWo4XV-UHX1MnsarhE571MVvVplr4HoTvnXoEUE4HruwcFNPC3ARWV8_QvGW8O55aIROahheKamJ9qVTzaqjBkb9B8PcGLuElsEVrazicIi2oWiSIlA1adrHL9RCeBWrmdN4sl13UjD0necqFIsCYldX9Vknsxmz7xL2azTuwqmuGBUEJyNm7XX4EOpoyXnD0XfvKzvG4snoI18UC5ZACPfUHghS4OK065MDLUie0-P-HW8SRPPPHTvhXrLEif3txDHVLAH3WOeOjOiz-L3_SnpoUtbOin6oXx4iR_mJEvptzJ8X5DIypeXofmJh7MCmqwROJCUnflHsJAxgeuI8T-rA3vgXt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درگیری هوادارای انگلیس و آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/100279" target="_blank">📅 18:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100278">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7054e61476.mp4?token=YATMcYE6iCvz4g5CU6RmVMM65JIJ8B9RQi8ERRpKmLP8MtDH1o_-AMsmGLghYYtc4ivIgulffZti35ZDzdF97bt1lYq4GX06-ti_0jlyXlrGXbanE_JG0FrUzZVae_XWL7p_jg5GMLGC41n8i33_i8IFF7sTPQw9-dXB4GQ6zvY9y0xJIAN_Agrr8WV9mlIhnp9F9Bl9U2MMrx4Vh1JJ_8TrSQwdFQaWl-pIxRsQ7WSkMYhG2jIgjerfS72cjqDWAqJf93C1ax7Rw6cfRyrtgObQM2mWc-1rmb5HMiZyU6vktXoaz_nY3S-YlXwTimtJEEWKIFGtiAeQZKq1dOPsKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7054e61476.mp4?token=YATMcYE6iCvz4g5CU6RmVMM65JIJ8B9RQi8ERRpKmLP8MtDH1o_-AMsmGLghYYtc4ivIgulffZti35ZDzdF97bt1lYq4GX06-ti_0jlyXlrGXbanE_JG0FrUzZVae_XWL7p_jg5GMLGC41n8i33_i8IFF7sTPQw9-dXB4GQ6zvY9y0xJIAN_Agrr8WV9mlIhnp9F9Bl9U2MMrx4Vh1JJ_8TrSQwdFQaWl-pIxRsQ7WSkMYhG2jIgjerfS72cjqDWAqJf93C1ax7Rw6cfRyrtgObQM2mWc-1rmb5HMiZyU6vktXoaz_nY3S-YlXwTimtJEEWKIFGtiAeQZKq1dOPsKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عصبانیت شدید دیکتاتور بعد گل دوم اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/100278" target="_blank">📅 18:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyL1W3P6tYxucJ3hUsuA0QptRDKaPLF-sIQ1MiAvZgQHevMZb19B51HWUDL6y7ABn6yCSoxJZalGFJTBhl_70fcf3tz94o31rgSBsGhIfXWobhbtWWEnXnLwPMbhemho1WqSe4vtf72_QZGnBQ7OqnVe1rPdp41_chzY68sow0MOhdUj6KAcHzT58i3D_7IG4f-PLK-DgB6IZ7eJyxWe6EJIaPcvQm-abcQE9c7PZjKCSTnHgng0R1CElRBGOaNG-W3b2uh3Uw1mgKBo_xgp-ng0ycJXA11QcHNoIobV0Rs6DRgY-W_f98uCRsFiyxzm47zNdmhF_yFFl2QRd0QtOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z07dhS3vVmQJue4gzVA9BVzAtaOKoQG41kANpas79JqZKd8zMpytvgRXvb4ihH-SX34iKOdpyY3v74oHe_cX8B2kuVBundGBdH4RA4VovS78iGSdU40-R2sijaV6yim-Lc6_gcK1FwONtdE1QOCG252o2jc2jHDzTkM_e6OKizffcjSecKK_dxZUnG2jhLxJhMzBLC-H7FkueAbd_-OhLMph9Sd59ln1uYHpgCRSfcBU2riXBq_F2_2RHiVorSw5QKbC6kgDQWiLn6zPoggiX3H7ToQ5ia3nfbbrxjdc4RR7W0T7U02wb70paXVskADO06gajOxAsp-NRSMj84GxbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمایی از استادیوم مرسدس بنز در فاصله کمتر از ۴ ساعت تا تقابل دیدنی آرژانتین و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/100276" target="_blank">📅 18:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a6548826.mp4?token=Z7e2jZcISN-urdN9mUm8NGln6m0-gQ4Oh5xRmdN0OO4k2ldnbpq20B-2j0-tYAG3YmNcgWnpfJY-3BNbydwbpG-UWfBF1bSEljJI7O9VG8sC-YC_-NVzGGPj_7jDrDjU5eFLTi3bXK7YJtE_vjrr6Hlzo5Y6PsDhJSUw1pUXha0UnTmGEcpWVt2HmDcCL6CNiv1F10cnJAAY8hfW_3f0hBfmS9Z-KIK6GgqFMJlhLp8l33vwf3faLOI7H-VXkbvcZPd7UZWuw3DsSrVRUFi70NfaIMn7_YuhEkLEIJ-K2ZDPgksn-pX-HIu0KUhfPo5nsY8lhdriYxwxOKmVsJwfQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a6548826.mp4?token=Z7e2jZcISN-urdN9mUm8NGln6m0-gQ4Oh5xRmdN0OO4k2ldnbpq20B-2j0-tYAG3YmNcgWnpfJY-3BNbydwbpG-UWfBF1bSEljJI7O9VG8sC-YC_-NVzGGPj_7jDrDjU5eFLTi3bXK7YJtE_vjrr6Hlzo5Y6PsDhJSUw1pUXha0UnTmGEcpWVt2HmDcCL6CNiv1F10cnJAAY8hfW_3f0hBfmS9Z-KIK6GgqFMJlhLp8l33vwf3faLOI7H-VXkbvcZPd7UZWuw3DsSrVRUFi70NfaIMn7_YuhEkLEIJ-K2ZDPgksn-pX-HIu0KUhfPo5nsY8lhdriYxwxOKmVsJwfQIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خسرو‌حیدری: قرار بود من بجای پژمان‌جمشیدی بازیگر بشم که با مخالفت همسرم روبه‌رو شدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100275" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB7TG1c2KCk6ZT-DVUuXCF8O4BAYCstYVr4RFfYTiv1b63iOe7LQrdZZsRTqNGSF-B1K0fGXWS-3iKUCXv92V_oHBJ-n_MQSJYM0-j90k9431uD0j3Lq6C0RhByHNaxrCI1LVyBjKXl4ng6CBvMkq8qjx1y3QtN5b-MgLF77er5sUU_kRES3JLWB-ZmUKVU5tt0mndgACJiEzkGTeCq0XWye6Yu7ybBShpcu8aJ2VanfF5Z3v5TD_1_rDFQZ4lH7yK5eMib9CkRkWgB4CDgeYbzOrV6P62t_xDL5fqB-4rL1BQDhdLxZmTxESxmwiZ4FByECEMzNAhjcdQTLHsVSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇩🇪
#فوووووری
از سانتی‌اونا: مایکل اولیسه به سران بایرن‌مونیخ اطلاع داده که قصد داره در تابستون به رئال‌مادرید ملحق بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100274" target="_blank">📅 18:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88663297fd.mp4?token=Kby126vv3NMIz8Z3VuJtzkTmqg7GLKOEc2vO0dnbGbqj_k7JZav6enG5LvWuCwTF-1myP9DTNx3Xw-j0DnNQNxd0LiWxTRZv4_HT2W_qoJv6rEazxlunM9N0hsxE_2bjXz6F_EqK5e5Sx1KRMcxBWuMKs5YwYEb3BcZKknVlnA3kXxttp5A1FcA0Tt-2lOr5yAgqM141XoIRC6uBK_thVa5vjs_J2nZxDQVkF-UaPrXa9xKchggFX1mg35l2V_3tjRsFGIR4AjVUJI-4eAa-8XX-zKydITcRVW0wnfNcoRLoZqbO8CIS0FsgxoW8z-z_bmyPhWOBPXhWc90rb7H0ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88663297fd.mp4?token=Kby126vv3NMIz8Z3VuJtzkTmqg7GLKOEc2vO0dnbGbqj_k7JZav6enG5LvWuCwTF-1myP9DTNx3Xw-j0DnNQNxd0LiWxTRZv4_HT2W_qoJv6rEazxlunM9N0hsxE_2bjXz6F_EqK5e5Sx1KRMcxBWuMKs5YwYEb3BcZKknVlnA3kXxttp5A1FcA0Tt-2lOr5yAgqM141XoIRC6uBK_thVa5vjs_J2nZxDQVkF-UaPrXa9xKchggFX1mg35l2V_3tjRsFGIR4AjVUJI-4eAa-8XX-zKydITcRVW0wnfNcoRLoZqbO8CIS0FsgxoW8z-z_bmyPhWOBPXhWc90rb7H0ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بنده‌خدا بعد گل یامال چرا غش کرد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100273" target="_blank">📅 18:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100271">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRnB0PV2qAvlt7o-BfpHNnyrGhdtIXu6AEBCUtfuK7YqVFYXfNuuycMpIoXexYpmMf8vjJ2UkNvnT8bBLfEq2omRkeUWqHkhRm9xA1eSH5xiOdPfHX3AnugvD-Ed5WUCwegOGzs9-111AQHGeSkyh6-DoTl3l8XkBhkBw3lYJYWUC0-796eDC9zfynHKeVkMjCi-Vxue5hz_C9njf80IntJjhcyDwAjynstMZoJfgoyK3UrRh9ZpqPTczyAz4TU-HqIBVLwg_sbQqBV6qPzMeqR3FB7IJ8o3q2hfCHxoMQipxtFlYLeHqXM59xmILRyfaZWJ1NBLe6H443XqQ0F7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADq8xaLew7pHTV5e_a8aF-3J0uT4LISWpUVVhIhc-NLdGaRTW2NEzQESQX2oHsYffdQsII9gNVA0ya3uM98hNZBc94WSAVyhMB0pOEV4AiLHVg59onMi_fjDQuwooCX1XEEGJA9m9CMBjGYxlvqEDgFRSYtcOQ1UIK7etWdIoZPBGCWQr1xFl4AvYj_Zz23FYnMeDm3d8V9dF8DHAK3Jj_YNLItky3fGVYuCwX7XYG108u4jyivCjMpIAjGe_DFJF_DXfCSj6X_w_0Ck9iWf9q3tCkA3Ci1YtpHVDCwtZ3HhF1-kx_WTPWXex0W8nc8TAxjrCSVMi74H-M0GPnIuHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
👀
رامین‌رضاییان و آقازاده بدنام ساشا سبحانی ملاقات داشتن در اروپا و احتمالا کارهای جالبی انجام دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100271" target="_blank">📅 17:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73bc182d48.mp4?token=OPJN_kFuh9YSj8MNy_SwHzjJJ-X7KtpQtZB83O1OQO98_bGM0PfbOq8OWvwmqnulFOrt2xpi88AW5dtFdp5PagRYYeTOmRLesbP3--3_969YD75GZzu3CiAI6xTQMtpUl1Xai-7oM0QbwqlW_W7xwqPWt8z56rLIRRjfvnOhI-7o6VtEeUUTx7zxqeHJlh2k-vWTunBst01cTEhU3Y98-UlIakZnjuT4Kvn3KOHVrDSvbYCUkc64RSHa8-EJrs0jnwkEHw5HpP0xiumrnUsKarGUk1BNsXb7cvK9W34O1Br3L6mzPTTKQE1OvF2lv6EN6LgLhCcFOSUlJDBI-8hCkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73bc182d48.mp4?token=OPJN_kFuh9YSj8MNy_SwHzjJJ-X7KtpQtZB83O1OQO98_bGM0PfbOq8OWvwmqnulFOrt2xpi88AW5dtFdp5PagRYYeTOmRLesbP3--3_969YD75GZzu3CiAI6xTQMtpUl1Xai-7oM0QbwqlW_W7xwqPWt8z56rLIRRjfvnOhI-7o6VtEeUUTx7zxqeHJlh2k-vWTunBst01cTEhU3Y98-UlIakZnjuT4Kvn3KOHVrDSvbYCUkc64RSHa8-EJrs0jnwkEHw5HpP0xiumrnUsKarGUk1BNsXb7cvK9W34O1Br3L6mzPTTKQE1OvF2lv6EN6LgLhCcFOSUlJDBI-8hCkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
😁
و اینگونه بود که دیکتاتور با قهرمانی در جام جهانی 2026 خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100270" target="_blank">📅 17:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100269">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47647cae7c.mp4?token=drbJ_-utuniPgarT2UKSMtOzPRzcZkSmt_m_YDYywxbDFgLH_97POWymkH4toCKjbstD4FVyLL0njfakxE41dsnGT7smTziM-Mx0B-EV09tfZD4AGZw_hXH6eY_cTUaPrO29XFRSmTzNsDpRwdo758mHoufXxPn0j9pr2ySe1jAGoFmBn591v9xY_Fl-zxYf8-l6cwqTH-aa4khDHRugI1wb6gFbf1nPeWcgcFQshEFNhcvr5YO2VQ5fMv802ztjfkiJtX0zZOwFqhXAAQ5n6uH4U_5Tseb8nPrsaRuUAim0zEUyQj03CCwHIiw5leY9IuzU5QyiOuMfjbeKW4jQtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47647cae7c.mp4?token=drbJ_-utuniPgarT2UKSMtOzPRzcZkSmt_m_YDYywxbDFgLH_97POWymkH4toCKjbstD4FVyLL0njfakxE41dsnGT7smTziM-Mx0B-EV09tfZD4AGZw_hXH6eY_cTUaPrO29XFRSmTzNsDpRwdo758mHoufXxPn0j9pr2ySe1jAGoFmBn591v9xY_Fl-zxYf8-l6cwqTH-aa4khDHRugI1wb6gFbf1nPeWcgcFQshEFNhcvr5YO2VQ5fMv802ztjfkiJtX0zZOwFqhXAAQ5n6uH4U_5Tseb8nPrsaRuUAim0zEUyQj03CCwHIiw5leY9IuzU5QyiOuMfjbeKW4jQtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
👀
لامین‌یامال بعد از بازی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100269" target="_blank">📅 17:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osvymxy85DrBJwlvfbQP5DsZzBsUDBT0IGmRCBaFTL_UIwGx8MG0tVr9FplM2HgNNLG-iIuAC5Vy3AskFdp2hHzwV4m5txUEKhZnKph6ovUcnpOKNTqVJgpsydp6dARw00whaWxPiH3eyFm0N_Upol6UPJTmPULIfrBS8KpNvoHmNVGodLQzPr9o1mICtkpdYe379pH-5u1T_17ThwvSLXhVlHLRoO2YzQov6bAR8kVpefN6cFrAN4_h2VpmtIC-S1x6e_n3f4dYxhKyTGwYHBZ7G1AUf4pTYksLeVrybLA0B-PX8Q33U_LRSW77YgBp3MmXZdamni1-Tos2YdpAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
براساس گزارش اوپتا، رودری در جام‌جهانی ۷۰۵ پاس ثبت‌کرده که ۹۳ درصد موفقت‌آمیز بوده و از سال ۱۹۶۶ تا امروز هیچ‌بازیکنی چنین آمار درخشانی نداشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100268" target="_blank">📅 17:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbRNt9REepHf-lsZD1ice8sxQ16LPSBu39g_Vz_DrlP1ZTwEE26om-6copXNbqh8XIoNE7JbsaLE40IE7IFusi_r2SgddECDAH1IYzYh8BGHyU6NdjJfh6Yh0TOCEWHXssvl2BQffCahnYoxgO1_QASX5MpOns9NdjjLyLNvCbbTq3Kys_rFfJjCsuR3eYnx24I_pL15PfY1GdKC4fPQApF6mnTbZT7WuOkHDDqHPEd2GU6DKujHHBltE71p-nXlvxEvikjL1Sy-JmixvMdW2wk7IZbJTfe1EWtXv0bt-GKdDm3aWHEy_oW66DeHdtdRn58g1O7EUxFKSCdGwrAdzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🤯
🤯
🇪🇸
هیچ بازیکنی در مراحل حذفی جام جهانی موفق نشده یک بار هم مارک کوکورلا را دریبل بزند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100267" target="_blank">📅 17:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3d1b8rYHxKZ7K1yuUlzoRTRrdvSMmdPAzp116REoTNRBpwtQu9RaqLcFxNMJsvOLdD2-y67ITEKMkCRSHUIv27UizmJCwmbd_IM1sFm9CCw_0zXiRAU5fNRwn9IKf8HaKvKbBFPhDNqMBWSZWXkKpWw2bQCqCb8vjnfO-kqLdSrPUErZCqEn_FJ3oML12LNWNoveM7CzXmVOHsyEeOhASgiODO5RAvoGb04yWUGoeGJ9_V8FTlquzI1i5XzsiMf8iwc2lJvKpOxvM64tfa49pFo-0vppTsUUo0BlIWAnv58h5GWc2hGq3cr_d1itigqYqTZN2odm9Cjzl6W63Nn2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
هیجان فوتبال با سود کریپتو میچسبه بهت
🎁
کد تخفیف روزانه مخصوص اعضای کانال
🫵
💸
سیگنال و تحلیل دقیق از برترین تحلیلگران بازار
🔥
مهمترین اخبار مالی
تخفیف روزانه در
👇
📢
کانال ایران‌اکسچنج
⚽
📢
کانال ایران‌اکسچنج
⚽
💵
🥇
خرید و فروش بیش از ۲۰۰۰ رمزارز با تضمین بهترین نرخ بازار در ایران اکسچنج
🌐
صرافی ایران‌اکسچنج
⚽
🌐
صرافی ایران‌اکسچنج
⚽</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100266" target="_blank">📅 17:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSDt-rgg6DdKnKsdXuBbiU7SKhlRbJmS8DwrN6mV36giBaX7CIGCY8qGTnloxK9NlBT6pGEqVeLT44FCTmqaxKioY0usXFzrRYDpCWYdFAKLpy5cYW_-pgpCCtgtvh9w8CUcT-l-Kp50HKvnL0s3-EAVY03W4FA5GBDwsIK5iQV8vs97Ax8qnahvzpNuSlH8JzSfJGyMXJaCdstXFPuYe_GfG-t6LFEwdQ6QEvTbIGm7YrxD_aCEDXd0NNH14fdjReiKiE3EnH00I_CKCpZVWDkR0NLKXyG80dSGkjQBHrNxyHbu4jil6WyEQxtIEALGjUDGxr_d-kFqXDJGMWMKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزان‌ترین بلیط برای فینال: 4,451 یورو
📈
گران‌ترین بلیط برای فینال، 188,803 یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100265" target="_blank">📅 17:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Doz-I4-wpneOEwdJMRRpZYzm26HRb9NigQTudRsdauoHpTY7kLm09MOd3m-vRda_3KVL53EHweasdxbWGAvJyblSmSDvza2j5OtLJRtRSqoJiCWEl9rL1GQX2bQiwUGxLw6Lqa_xGVGxHN-MTs6CdHgpwQQwHGzFUTgWvNfxNeFLbJENr0txe4fNjJvU1Jfmn3qq5fARLUlhS_mgbQGkXJu3U8k77-E7noNKCxatwvWqha9AXovkgzkRGLBAdhMjQQOCwctzVvXD6DPKU1_-SQEu8txq84GsVYMI4DPDDe6qZktme43nc_szf32VtqDwayHZv1iUtHduno0ra_h4Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
توماس توخل درباره مسی:
"مسی می‌تواند در هر لحظه‌ای درخشش فوق‌العاده‌ای داشته باشد. او یک قاتل خاموش است، می‌تواند شما را نابود کند در حالی که به آرامی حرکت می‌کند."
💀
💀
💀
💀
💀
💀
💀
💀
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/100264" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/100263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/100263" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCHncXugJLCVvM5f2CICTqbTwoGNZ70_qK-v4rtrzLMvwnOfsZJlqW0k6HORLi6D3dIcV-PXVyJyFP3CLL-PtCjjciOd0OeCUn4nEIxghOY76JQXZO1ecH_1tWSsCLYix9MZ0-V34zVpjRmlNDkrL-KTBpGUQmdzOeSRdNxPY9RDWsi8MCLKkvNnbUoZZBSX49W5q5sU2LPKXoKP7GDVuk4tBSuJSt59go_h1XWfc8tnExwPYrSyfUqOehFauAsCyXYxvHozTzBVd93-5miFxXix7_DvJakXS9Ld9QVm9-evT0NkYswuEET-IC4j_Cvqq-eLsyRSzxg75loHH2rnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
Stand for Victory |
مجموع کل جایزه  250,000€
🎁
جوایز برتر:
🥈
جای دوم — 33,000€
🥉
جای سوم — 20,000€
4️⃣
جای چهارم — 10,500€
5️⃣
جای پنجم — 8,000€
🏅
جایگاه 6 تا 10 — 4,000€ هر نفر
🎖
تا جایگاه 450 جایزه دریافت می‌کنند
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100262" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f95d4ebb0.mp4?token=ZVkcHrnpi44I2N0fUNES7CvKGROubADc8gfj-komC3WJx8LJWdjr3Ng9Gxsj9wjM7QzdEe-i04WdayxvLtJT0BMR0PlST31aJKU1UZMH92dXdF1p_hxLsD9e39x3VW-eiX4_rRL4tmpOWXW5ECW5HIHZ-x25iO6ku4qSdZr-nzuoJioodgdC3ns9vv2f79x5ABAuWdhnyUUWnMfb_w5h8OMYKhPS9rSB-pAsdSQOrQDugUnQoF9bggRRBOzOjGLVZm-6dohpe-wJXeH2IZIk1p8d6iUSUvLK3uv-vCo7YsStgxDbRz3tqgfxoERHIWSz1WTVtaaDzj6nVqvlt0PL2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f95d4ebb0.mp4?token=ZVkcHrnpi44I2N0fUNES7CvKGROubADc8gfj-komC3WJx8LJWdjr3Ng9Gxsj9wjM7QzdEe-i04WdayxvLtJT0BMR0PlST31aJKU1UZMH92dXdF1p_hxLsD9e39x3VW-eiX4_rRL4tmpOWXW5ECW5HIHZ-x25iO6ku4qSdZr-nzuoJioodgdC3ns9vv2f79x5ABAuWdhnyUUWnMfb_w5h8OMYKhPS9rSB-pAsdSQOrQDugUnQoF9bggRRBOzOjGLVZm-6dohpe-wJXeH2IZIk1p8d6iUSUvLK3uv-vCo7YsStgxDbRz3tqgfxoERHIWSz1WTVtaaDzj6nVqvlt0PL2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
🇦🇷
جو پشم‌ریزون هواداران آرژانتین در آمریکا پیش از بازی امشب مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/100261" target="_blank">📅 17:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa988482.mp4?token=uDZHJwIbktDFDS70v4GeRIdBPsocgpOd3d3lir0FT8KRCC5khWBAJpwprY_e-wb1vczC4tJBeR2j2mIAf9duD9As4STnfIWYIJxoKtOmuzRDiov-MfB3ERTcSF1rMETm-SvfLB7tkRJkpg3hzph-KlnM0vvUhwAq3a7sbwXHVbPC3XKZa2pZeaA5R9iODmSuVeOPGHpmv4FZuX6VFAOf2Zy6VITQa5sh6M-3fFCOCglqiT8mU-FaMBiWVKQ_d-r9N8A87huU-Uo9Jr-rgGqKq6uDRzPr9QQiX3jMO9uvXbR3B19-tr7_rH93oHZSrQJ-aW0Mem5NnOIDx6T_u_N1Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa988482.mp4?token=uDZHJwIbktDFDS70v4GeRIdBPsocgpOd3d3lir0FT8KRCC5khWBAJpwprY_e-wb1vczC4tJBeR2j2mIAf9duD9As4STnfIWYIJxoKtOmuzRDiov-MfB3ERTcSF1rMETm-SvfLB7tkRJkpg3hzph-KlnM0vvUhwAq3a7sbwXHVbPC3XKZa2pZeaA5R9iODmSuVeOPGHpmv4FZuX6VFAOf2Zy6VITQa5sh6M-3fFCOCglqiT8mU-FaMBiWVKQ_d-r9N8A87huU-Uo9Jr-rgGqKq6uDRzPr9QQiX3jMO9uvXbR3B19-tr7_rH93oHZSrQJ-aW0Mem5NnOIDx6T_u_N1Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
شادی اسپانیایی‌ها از صعود به فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100260" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFTkhTrl_N0GiKGhKaK6zwiXz15AYoAciy8vgkJSpW5zwYEXZ4CWCaPTfGbSZV200y4SfF2jJZg6REcqIe33uU-ML9ullkCnQ0UBC1ketL7HMCPpDsXOPVssHHzw0KYYQiKGrF6N_4-fVVy0QNh6EK2bq3j0Uy2Kna7ijOisZj2KjXwj2kD0fON4stI9U9JC5MwvdqOIn3Kd_-dIg_R2wMkqQKNdcCuK-MmXPhy4MjJxdR_v2IX7hnqqpd1KrOC40UMix97MVNIi_zBk8BI67mg0tK-PSp0kXmW-jJKQVlGI39-Fy4czbyEp5sDUoBYCMVBel1c6DMSwdTh1MkQBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد تیم انگلیس در مرحله حذفی مسابقات در برابر تیم‌های آمریکای جنوبی:
تعداد بازی‌ها (9)
🏟
تعداد پیروزی‌ها (4)
✔️
تعداد شکست‌ها (5)
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100259" target="_blank">📅 16:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6602b08c.mp4?token=WTQ2vRJ5q8Bzy-CxlmqG73J_37A7HoiTCiBmSgdAXlZmJxJZYvXvrfsme7WG2kFC_6-9QA7ulruajwKNA3T9F2pzd0ExYPaqRF1H_w8Nnx1fRh5fp-PUQLrySp-0N_KWaJm6FJUrdTL1_AVKoHWwQDnzbbv9jsN7Sg3vqagl1HUurELdjRs5Fou0n8Gyw0QEOZqShbncNqV80bbBXGZ0XuwagjUoiWLDcH4yJxgfJy7kS3A55v37zZQtOw2sYxEwG1y3nV4ELePcgoPM2Ubmc6sK_m7Yh8iAZELUSOPrNFlx2EX4Qkrk_b6XivFEXFYanTmh33Fwt842CN8UlmN1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6602b08c.mp4?token=WTQ2vRJ5q8Bzy-CxlmqG73J_37A7HoiTCiBmSgdAXlZmJxJZYvXvrfsme7WG2kFC_6-9QA7ulruajwKNA3T9F2pzd0ExYPaqRF1H_w8Nnx1fRh5fp-PUQLrySp-0N_KWaJm6FJUrdTL1_AVKoHWwQDnzbbv9jsN7Sg3vqagl1HUurELdjRs5Fou0n8Gyw0QEOZqShbncNqV80bbBXGZ0XuwagjUoiWLDcH4yJxgfJy7kS3A55v37zZQtOw2sYxEwG1y3nV4ELePcgoPM2Ubmc6sK_m7Yh8iAZELUSOPrNFlx2EX4Qkrk_b6XivFEXFYanTmh33Fwt842CN8UlmN1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال چرا پای خوان گارسیا رو ول نمیده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100258" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOZUcFbxkTje1Jnu5ScBGX0RU3asS6FqfnfbRPVpLVrxJ9VNzdk6c0nJqD9h9GlXnimCYr81qROhiOqK0TuBxVBv9GnkUUSWqqbX543RBtBQU2r8Bcisf82BwGALHWuCKYs3wFy342yAz_HuEcpx28xcxF3jIBf0VFs0govBzF5JlTX1dKKNiBewurRQLqjuav_oREvjPC14RwoS2P5WajhJZbRkBJGOglhcX0-_6pjhTJNiK49YzKQjevQ1UKluegKsc3z-FFW7GpXW1rOuM5Tq6Aah4RvvFKXEVyDnVNnrTv7s66ImdujhoVnFZ2XHxOh4ims0lDnLhdi7nRM_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
👀
دوس‌دختر پدری در بازی دیشب فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100257" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ac68188c.mp4?token=MZUotni5CWtQLn-t2WTxUpig3jOVXvmybskbYtonPOmsTsWPcLhvsTDsPyD91OTP4Ggc5WCHEkGRRbWHdn50Ftvu_gPxErCo33pcCts9bYNEuYS_5SHOyUygvY5zvtDCm2AUHVg3eyqQt5tlBSl1ngXLf8tcb03vAkzwz2xsduZOE_sack0O_u2seFfFTpb5YfBh3vkIwl3lfqlnjhM_0lsktuw4Yxc4bNgPDI3CmIWCWCmYR2pI1tHbF8jpJnvvg4XV8YO6SWkG4buFgdO290N8wLcUcT0cPi-7WkV4IGfxHAolMNlLHC47vxn4wrAHhJfs3Vup3UBNcbEPgYdqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ac68188c.mp4?token=MZUotni5CWtQLn-t2WTxUpig3jOVXvmybskbYtonPOmsTsWPcLhvsTDsPyD91OTP4Ggc5WCHEkGRRbWHdn50Ftvu_gPxErCo33pcCts9bYNEuYS_5SHOyUygvY5zvtDCm2AUHVg3eyqQt5tlBSl1ngXLf8tcb03vAkzwz2xsduZOE_sack0O_u2seFfFTpb5YfBh3vkIwl3lfqlnjhM_0lsktuw4Yxc4bNgPDI3CmIWCWCmYR2pI1tHbF8jpJnvvg4XV8YO6SWkG4buFgdO290N8wLcUcT0cPi-7WkV4IGfxHAolMNlLHC47vxn4wrAHhJfs3Vup3UBNcbEPgYdqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
درس دیشب: کری میخونی بخون ولی بلد باش مثل یامال تو زمین هم پیاده‌ش کنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100256" target="_blank">📅 16:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100255">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYAgiISj7wykm1gH_MzuVFi7-1ZXDSgDhZGMvb4r5WcofXKHtQX0d1a9xZJA4WMKGqpPHCgCluFNBrTk9EdtpYgz1oYVlLCEkZ34bOpOFX0wsQQZx5FifMraBAWqeiZG7bdUCEEyzBa1RyvCRsU4Bhzp0RcrlK2DkWsZ0j-TdyRwqr6d1MmhTc0NRAlbo-OQNxDRQMinkwZdsl7OT5u4bzGehcfb2wpvESOAIJyJl-mwCO6IYsTWPsieiwC-RhSqPpBdFYAkQ40ET7Zf5Npt9sB4scMMMiOeI0npK8rC7wlbXJoa6LhWGDKrhBhu5WN4z8bf8ksjb2xq0y04LBUgWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
نتایج تقابل‌های تاریخ انگلیس و آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100255" target="_blank">📅 15:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100254">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a487162a.mp4?token=QgULFqt8JGynXzJIwe3QQY74rH7kcx5QUp0ZS8zMsi1zNYpPG3R-Eccq7851Jdz_FYNgfC2NNdGyG-qibVyTqcpt8c4X3gKedxBaTG4XbU74fa3BZjeZopllOhktWk5hgY8gmbricMzi4GzbSFRXE3elXyef2ShG-exhlwvXfGkmrOjBb0DSlDNbkMxTlsYfSEGpEhSlYZm8ZbhPm347A3fW-EKUzGQI41F94OMHyG6xp9bLmZnu1kTAfoYzBY8DZb0vKSFKZtJOrlaox6akhWdQvTbuwbxp9SBcZC_almvXY9vLyBwF_ItzQEJgMx74-2pj4GUM6-vXBs67LcRiEB_tFYPxfjXkBivNEwoXiXXR49QsVTch4h86U2RElz3SGnr9YfGTzW6Y1X7v7uUdCwD9YhwtYu3AE-2yicsjaMzb05Awn-792cxRv8s38f41mClKQlGlQ71-74zatCDYhi7Ppbf2SobVWcTodvRV_2qllK-96EIqa7tEWZJhQAt2yUVQ-1CvSOWGWSVzpqlXgCOCecjMEYKG3EmjCTmzlE36tEjAyw7Vp60Swmlzmvtj5LhHmNzt-8lyQnAgbeVP4qYt0WPs_0AueJZtiTqBt9KeNnrZ8AQOfLhpbXivD-OMzDRxRrEhH_3c3_V8GqEO2beI6tQEAKeUYjwsXCO84N0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a487162a.mp4?token=QgULFqt8JGynXzJIwe3QQY74rH7kcx5QUp0ZS8zMsi1zNYpPG3R-Eccq7851Jdz_FYNgfC2NNdGyG-qibVyTqcpt8c4X3gKedxBaTG4XbU74fa3BZjeZopllOhktWk5hgY8gmbricMzi4GzbSFRXE3elXyef2ShG-exhlwvXfGkmrOjBb0DSlDNbkMxTlsYfSEGpEhSlYZm8ZbhPm347A3fW-EKUzGQI41F94OMHyG6xp9bLmZnu1kTAfoYzBY8DZb0vKSFKZtJOrlaox6akhWdQvTbuwbxp9SBcZC_almvXY9vLyBwF_ItzQEJgMx74-2pj4GUM6-vXBs67LcRiEB_tFYPxfjXkBivNEwoXiXXR49QsVTch4h86U2RElz3SGnr9YfGTzW6Y1X7v7uUdCwD9YhwtYu3AE-2yicsjaMzb05Awn-792cxRv8s38f41mClKQlGlQ71-74zatCDYhi7Ppbf2SobVWcTodvRV_2qllK-96EIqa7tEWZJhQAt2yUVQ-1CvSOWGWSVzpqlXgCOCecjMEYKG3EmjCTmzlE36tEjAyw7Vp60Swmlzmvtj5LhHmNzt-8lyQnAgbeVP4qYt0WPs_0AueJZtiTqBt9KeNnrZ8AQOfLhpbXivD-OMzDRxRrEhH_3c3_V8GqEO2beI6tQEAKeUYjwsXCO84N0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
دیشب دلافوئنته بعد بازی جلو فرانسه یه حال اساسی به بازیکنان اسپانیا داد و اجازه داد که با خانواده‌هاشون پیتزا بخورن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100254" target="_blank">📅 15:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100253">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01e8f0d16.mp4?token=vD25r4rdLS65Sy6B36diV8U8Cnkx9ZdCkbc4qn3I16f_HzlKyPR16phthlQwoEXN9QInbxvSxma-HdDzPQZIpr7f5CQ3qlBMSoQ92WP_xemcWGfSWCQpg3s6iPoe9c6VqpS1SDS8JmS3l0RWh7xpJrdf5oyjdmwjS2hFPOCxpRMuszZBdfDSAb7keqX26vycSBPy3vyiv-MO4BvKJIFIhazDwoHVbeMYeWkOdiIfUBbwQ0CsR6sDYoF8JLDmxCilMjW8u-UN9OcwlAwP6OGa5LS47ByKVQdU8_vsmQUsqaSuWBTsbwHYRH2rKxEgRH13GY9U-lX0YjIr_ChszQj1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01e8f0d16.mp4?token=vD25r4rdLS65Sy6B36diV8U8Cnkx9ZdCkbc4qn3I16f_HzlKyPR16phthlQwoEXN9QInbxvSxma-HdDzPQZIpr7f5CQ3qlBMSoQ92WP_xemcWGfSWCQpg3s6iPoe9c6VqpS1SDS8JmS3l0RWh7xpJrdf5oyjdmwjS2hFPOCxpRMuszZBdfDSAb7keqX26vycSBPy3vyiv-MO4BvKJIFIhazDwoHVbeMYeWkOdiIfUBbwQ0CsR6sDYoF8JLDmxCilMjW8u-UN9OcwlAwP6OGa5LS47ByKVQdU8_vsmQUsqaSuWBTsbwHYRH2rKxEgRH13GY9U-lX0YjIr_ChszQj1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
💥
آندرس اینیستا: مسی برای من بهترین بازیکن دنیاست و فراتر از کلماته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100253" target="_blank">📅 15:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/062e367521.mp4?token=baNAh7LRO2YqX5f097qO7GzbPSRn9-6TEHoQKWbSlNv8QcrbutLSqIzndrQ15yfZc8gxZ45gwzisVIgH_78dJi_AoqNy1mmeo1IDtsGoVx7HorJB35s18LSU0-oiDW4kJgLLj9Icu4UJ-HvXhi-pJuASRVZZXKYAdZfNTsfe3PRggj-r4i8wHMcuxbXz70CAClHzhtePPYZImltJwPqlkkdIgVtJwCVBnKHDaDdy9jF9pl82xzERmqopg_q4htng0akzH091nZxsF0FggU-6lFye2t4D-N9FgG1JDcmpZVgC4iwGXqMY48Upvhag4Iq9nRHummnQrJLxM9X2snSvdHm4Ev4OVEth9RLmagUfJLzhplgPHIO4QFZeIW-o1yC62ka_LvR5Sp5oBe3xP5zzDg6ZWCxKoOPW9KrfjwB12-H5II_AG7L9FxM6J9Msty6b2Ggcq92NqD9Tkeqxp9qmNUZv7uzONuyu43ahhgpUCIANmaDfZMx1fA3lKV9CMmlpeaS1bqYRZS1v3ACfv6o2g3auQNBwYf-MycKCNgvTEO7grqGFDYmnV9nLZecA8nssL_1dbym3gJEN1CUAIVOrGOYED20cIKeePY2o3viVDBeS8iJo2mItrobvgFVWcW_AFGQcaTmblbdOZINw0jSO-QkLuS2VxnhnAav8KBllzB8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/062e367521.mp4?token=baNAh7LRO2YqX5f097qO7GzbPSRn9-6TEHoQKWbSlNv8QcrbutLSqIzndrQ15yfZc8gxZ45gwzisVIgH_78dJi_AoqNy1mmeo1IDtsGoVx7HorJB35s18LSU0-oiDW4kJgLLj9Icu4UJ-HvXhi-pJuASRVZZXKYAdZfNTsfe3PRggj-r4i8wHMcuxbXz70CAClHzhtePPYZImltJwPqlkkdIgVtJwCVBnKHDaDdy9jF9pl82xzERmqopg_q4htng0akzH091nZxsF0FggU-6lFye2t4D-N9FgG1JDcmpZVgC4iwGXqMY48Upvhag4Iq9nRHummnQrJLxM9X2snSvdHm4Ev4OVEth9RLmagUfJLzhplgPHIO4QFZeIW-o1yC62ka_LvR5Sp5oBe3xP5zzDg6ZWCxKoOPW9KrfjwB12-H5II_AG7L9FxM6J9Msty6b2Ggcq92NqD9Tkeqxp9qmNUZv7uzONuyu43ahhgpUCIANmaDfZMx1fA3lKV9CMmlpeaS1bqYRZS1v3ACfv6o2g3auQNBwYf-MycKCNgvTEO7grqGFDYmnV9nLZecA8nssL_1dbym3gJEN1CUAIVOrGOYED20cIKeePY2o3viVDBeS8iJo2mItrobvgFVWcW_AFGQcaTmblbdOZINw0jSO-QkLuS2VxnhnAav8KBllzB8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح داور السالوادوری بازی دیشب ببینید
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100252" target="_blank">📅 14:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7124f6be27.mp4?token=SE78JC_IZ1t23UAApnjHegOjIJiMM8kbVVN51TOdlpKj3EIHR_dFgMs7SMIQNKE2yixCDqZBaAkpukj5UdqljoW5kGbmBLUaSrTEoYWNZe6cLRol-n-YU8bMQSKt7RD0mAVptiPcPkKw0P17SCi1EsUzHImPuFHSKewAJfnxGme2pb5qUXSG0QezFhkM0tpAxg7VFORw37qDatToHNvHAsV1F3NSum7x732kCCcA6Zm2HKESNLogwJorvxDjh_XCxFu8qEvJTrCkkjGtcz5Gl4qItc5kq3cy1WN8esbi9iGUWmiC_LYpaanlMfT7IreHsJkztCvrhu9jbPzzxDdqjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7124f6be27.mp4?token=SE78JC_IZ1t23UAApnjHegOjIJiMM8kbVVN51TOdlpKj3EIHR_dFgMs7SMIQNKE2yixCDqZBaAkpukj5UdqljoW5kGbmBLUaSrTEoYWNZe6cLRol-n-YU8bMQSKt7RD0mAVptiPcPkKw0P17SCi1EsUzHImPuFHSKewAJfnxGme2pb5qUXSG0QezFhkM0tpAxg7VFORw37qDatToHNvHAsV1F3NSum7x732kCCcA6Zm2HKESNLogwJorvxDjh_XCxFu8qEvJTrCkkjGtcz5Gl4qItc5kq3cy1WN8esbi9iGUWmiC_LYpaanlMfT7IreHsJkztCvrhu9jbPzzxDdqjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇫🇷
ویدیو لو رفته از رختکن تیم‌ملی فرانسه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100251" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlYFBxLoyZQh4He_pSvO_vx3vQeoCgF50FNzJzGr7pTnJEp09zHB1biAoD3XEuTLUz-Xv5bTfHlKAdvWd9dlQds42YBmoKFnvGtWoYKPBoaYHunyyEh-Fl8WJsc5MX8pxka2j4W_eIwZQJttNLCH2HsyWl4rYGfrUoA47LognM9i1VJ801VzzUmhPxYbVLpWxvVktWUFmfMG_fbpE0bpm1svrmEa9eUXTuznWewgyvcqEaFZcWtrVWyu0KjLQ7GTeAJnHZZHJw45o-NXyoNGXuLxf4icvp6oyvoDb0PNIaDmgJanM_pZdGrtKgFnEIw9-pKUIkQ9f63KGDdZwKZDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدین شکل
☠
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100250" target="_blank">📅 14:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea564e6cb.mp4?token=ZbJwMQThJrEWG5kelL_9lsVkT_kc4RmvjZsOC3kcxME_Rx_npm4H946d1X66b9WH-lhTABvnyOwjfoBbWN8bGEZtaEu7-JZYPxj_wMEyqzwUYQOR-yMnrNT_6JV5eXAO-Of7qGuIN20A1h-mwoLjJsDxbvex17z8Epp5qEdzXY9TkZxuX_TrFodMxSKQVY8jPqDpgE_Y_mydQYrTMRgBFHeS7JLyKd_f0Apgo2HDSg8iXkbAFaJqVsAjx5qbPYGXbajAy1cVlqqRGX7jLDVtdz7r8ljzw02TOWaVlDFvAsHLGt7IlfofIYp_C_DlVsivLFD8qhDyRPYe2up6I77rkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea564e6cb.mp4?token=ZbJwMQThJrEWG5kelL_9lsVkT_kc4RmvjZsOC3kcxME_Rx_npm4H946d1X66b9WH-lhTABvnyOwjfoBbWN8bGEZtaEu7-JZYPxj_wMEyqzwUYQOR-yMnrNT_6JV5eXAO-Of7qGuIN20A1h-mwoLjJsDxbvex17z8Epp5qEdzXY9TkZxuX_TrFodMxSKQVY8jPqDpgE_Y_mydQYrTMRgBFHeS7JLyKd_f0Apgo2HDSg8iXkbAFaJqVsAjx5qbPYGXbajAy1cVlqqRGX7jLDVtdz7r8ljzw02TOWaVlDFvAsHLGt7IlfofIYp_C_DlVsivLFD8qhDyRPYe2up6I77rkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تیکی‌تاکا ناب اسپانیا مقابل ستارگان فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100249" target="_blank">📅 14:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdavPxt7205WQGyZyaQu1v8aoJKlr8yoRlQy4lM_CkxYoTK9eZaS3EEiEztMxSKN_dkywpoT6mDo-Q9yktc_7OX-ewgkbhF9d4aoswLKcOLkfOBsFcuiax1EMGiTQvmyxS0xDiH0na8Ei6peM11HIpau-o9NF5CGg5Dyo77TLpL9QmXSezoHez-Veuo9W0nHwS5k-940gI_lrzciVEwYZvDQG-BIKGfyfB5Ag32lwRmCi2bIaPoyVOfpLOKajqcGio3cTs--6BvmbApESdaTzrVPxdMzaYwMhz6EP_dV0L_I8hXBN1irLcfVknzZ31TJGe-IltrFGExNV2CEiNr3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
با صعود به فینال جام‌جهانی، اسپانیا با عبور از فرانسه صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100248" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LON6AAr71d9ZD7QZMMbmhhfEzjjYReQwDVcXi7LgEwXRzZDdPz_Mhmy8qzcNeiLDuLQpVwORTCqrfmDTN6PsyiPNGTW_O5LKc0kkvCKKQ0JGzzfBjgU9Uu9SS-K94SowxgcE8PHvZBWReZ6wRQ_Qjav7R3Lj_fatkoa32bTh72_VsnRjcMsXV21i3PXDFjHpDSvByurF69206OTDi7kIc8SB7rGypex7MMDaPxNgi6dkwyQNfHGN49b5evIxby6CXqQoo_vi4BBm_N8Buy87MNqErHEyQXh64AEUDgEp1VPwhk9uS9PXMRb9eySOQobFsPfGcsIDrArZR48umRc2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میانگین تعداد گل‌های مورد انتظار برای تیم‌هایی که در جام جهانی 2026 با اسپانیا دیدار کردند:
🇨🇻
•
کیپ ورد (0.20)
🇸🇦
• عربستان سعودی (0.14)
🇺🇾
• اروگوئه (0.20)
🇦🇹
• اتریش (0.32)
🇵🇹
• پرتغال (0.63)
🇧🇪
• بلژیک (0.34)
🇫🇷
• فرانسه (0.31)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100247" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7bbd3518d.mp4?token=q5YZUlMTcy7QhXWfgIi7vWEZa9J5m26DhXYkFlGEq4IK7eGnb_Mvexo_ygbMqGtJzu3fyuPjJveA0iIhxmhpmbCv4WvyL9X1fZKE0-7xYkKPg8aD4hyvWjd9Nfslr7NflsxaNb8YGsscl3d2E8BZxD5-pIv5GfaubE51R0jmLicVxXThQ3PIix1i46LKNKvuGjJYEn85s2xb95fBtB1ApOuvnCYn2KDu3MdySqv_BJVwZbEU2S0_1vlxaE7beXl4r-ESvD4XsXpia-y7Nz3notd0PLlQ6PX2NkgOSYTmXuovZETBT3blnpi_XD7JODCfllqY-QTBLDBWUN6Gh61pdUV7VMiUu2K1DfTyEP8kMDhRFIJQwzor9xda_21A152n9gvnY9JO0uOpDiZF9mJZPk5cwMXygu7HqgOhi3RlW-4APopLFEUrHfNRCjrgIoFYZxEKGzP5Z8VSFpq07m2glqVpUDgpF75_XVdr5wb_cYU4vQREtnvFnKpIHQxd8wGF5X75NE1dq-D8XIwgUudSdq5kx7NCovPqNJT1pbFJMkuJjAQazoT01dCwRKCO6IEfruWAwiOmePap1TEvEY2U6ZQi_V90Jxos22lTfxjdAhgXrP_ek--CBZo3h3vAn3oo26KWbpY6Pp_gMvwwnKaGJexLyKVL81Le-n5NsAGO9Qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7bbd3518d.mp4?token=q5YZUlMTcy7QhXWfgIi7vWEZa9J5m26DhXYkFlGEq4IK7eGnb_Mvexo_ygbMqGtJzu3fyuPjJveA0iIhxmhpmbCv4WvyL9X1fZKE0-7xYkKPg8aD4hyvWjd9Nfslr7NflsxaNb8YGsscl3d2E8BZxD5-pIv5GfaubE51R0jmLicVxXThQ3PIix1i46LKNKvuGjJYEn85s2xb95fBtB1ApOuvnCYn2KDu3MdySqv_BJVwZbEU2S0_1vlxaE7beXl4r-ESvD4XsXpia-y7Nz3notd0PLlQ6PX2NkgOSYTmXuovZETBT3blnpi_XD7JODCfllqY-QTBLDBWUN6Gh61pdUV7VMiUu2K1DfTyEP8kMDhRFIJQwzor9xda_21A152n9gvnY9JO0uOpDiZF9mJZPk5cwMXygu7HqgOhi3RlW-4APopLFEUrHfNRCjrgIoFYZxEKGzP5Z8VSFpq07m2glqVpUDgpF75_XVdr5wb_cYU4vQREtnvFnKpIHQxd8wGF5X75NE1dq-D8XIwgUudSdq5kx7NCovPqNJT1pbFJMkuJjAQazoT01dCwRKCO6IEfruWAwiOmePap1TEvEY2U6ZQi_V90Jxos22lTfxjdAhgXrP_ek--CBZo3h3vAn3oo26KWbpY6Pp_gMvwwnKaGJexLyKVL81Le-n5NsAGO9Qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
کسخل‌بازیای اسپید تو بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100246" target="_blank">📅 13:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b90102af4.mp4?token=qKAg9yXAwUTO6jFEf911--yBKcSLiIOoFFblKMAfY1ZjSJcXuMoV4K-jByFecIaiHx-mmrnR8q15wnICYuM1XcTG5YP4QDJmhAkmB_N3uRPtykvwHK6EVPNGWbEc7DVSB0WjlumBM286v5EDqS1ARMbxyfvZbwyJiG-GGiPZwwgMuNG_RNFlS4CROfTPwO-nbJtZjGpJ3BK_EkD4A5ohcsuoDIdX_bbMwetWU9kGzXmY0K6gDREaYEPE_trU_omaR64lPCfacYcfKs6vP1TGGqCEXD4Y-VVSVx4gwD3gTVNWeWs1yFnFaxsCwDntrEcPlJw87cOCP2NVVL2y_dcLkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b90102af4.mp4?token=qKAg9yXAwUTO6jFEf911--yBKcSLiIOoFFblKMAfY1ZjSJcXuMoV4K-jByFecIaiHx-mmrnR8q15wnICYuM1XcTG5YP4QDJmhAkmB_N3uRPtykvwHK6EVPNGWbEc7DVSB0WjlumBM286v5EDqS1ARMbxyfvZbwyJiG-GGiPZwwgMuNG_RNFlS4CROfTPwO-nbJtZjGpJ3BK_EkD4A5ohcsuoDIdX_bbMwetWU9kGzXmY0K6gDREaYEPE_trU_omaR64lPCfacYcfKs6vP1TGGqCEXD4Y-VVSVx4gwD3gTVNWeWs1yFnFaxsCwDntrEcPlJw87cOCP2NVVL2y_dcLkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
کیلیان امباپه که دیشب جهت پنالتی اویارزابال رو‌ به درستی نشون گلرشون داد هرچند اینقدر شوت خوبی زد که در نهایت توپ گل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100245" target="_blank">📅 13:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBZPO2SE4N3Pv3EWqh0RfoEkGh3Zj_QRFUSoXcZyObydcat95WV5P5ppWTwg3mpGL4IgyPix9eNsyI3Rgr4793UPj91hpDlIzDGglyuiBX0gih6EyRo566jSOVkkOMbZ46EfNgKCZsJMpQt-FfWKQG5rdOVIvGdJzOJ9BOkrLX7fXs3rs9REtApLM4yIEOymzsNacJc2gUt22T2fgxE6o-radTRbhUqPCFvK-06--ZoRy4HVWbKuqOWyxKloSE09912NmkFr59uqhtGLHaj-ZFX6EC0SSX7c6WHjqV2YFOfbvlfLR4aPOaNyvY1hvgU4gsYhtXR8pZEmnlVkb_Xr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌟
امروز، اولین بازی لیونل مسی در مقابل تیم ملی انگلیس خواهد بود.
📊
در لیگ قهرمانان اروپا، مسی 36 بار با تیم‌های انگلیسی بازی کرده است و در 33 گل نقش داشته (27 گل و 6 پاس گل)، که این رکورد، بالاترین تعداد گل‌های زده شده توسط یک بازیکن در برابر تیم‌های یک کشور خاص است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100244" target="_blank">📅 13:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJIyBKTRJCyR8pvMNLpU09yH26qOtRW69r2yNDjTo9TY_BWfdJzsbpalM5B36mmA6zFrtMES2-ffZGrq1rEmBQMAQDRjhh9zWBU1JliCBkwEQDwQ1Dor1o1F4mNRA9SZMmoCre-S0nfKzw7JyG6rf3JvWLb_A3oNUqXDyp4yZsswzYCaZvjdsbOJ3cs5yv-mmxX9MtI8AOTTHRVx-JZTBlhR7_tH0EhepDcBdLnw_28bUVi4IMQEwQgKSs7Eqaf9PrInlD0oqdmQQvFphrw2yC07yzaAf2pgHcs5lsoiZaMmjaSnaQqlqueyn_Js5TVrYN_vCxGvVN-wnEuFa_Fpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
وضعیت جسمانی شزنی تریاکی در شروع تمرینات پیش‌فصل بارسلونا
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100243" target="_blank">📅 13:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e7076d2.mp4?token=q0yVHsSmOmMv9Vrcvi4P-3gQgW0M4wixY7W9zn4tiXet06zwna7KT5BFH0gzVIS0uq_LHFNdbznv4-Qa6Oy_jDux4sS2aM1zQPw-uCal50ZOjzneY3p-RGcX4CB2XkoqR6IZkT7R3XxSLtAzJ18FdS0r93gXCL5uxgpogHT_6HQpKyy143f1I4YIvipK0kz397hbdcvlEWvGAHJ_l7AlIq490QaM8gNEs6xXMY8Xw9WGEWS9rLUN_KIuUJOIFTcQSmo_8ZMzeJSJWXxw43iswRpanCE1q44NPfWKxwbrf67sdZxn0YBKaKhGvMC9LIa-H6KPDZitopWvpyHwz7z4GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e7076d2.mp4?token=q0yVHsSmOmMv9Vrcvi4P-3gQgW0M4wixY7W9zn4tiXet06zwna7KT5BFH0gzVIS0uq_LHFNdbznv4-Qa6Oy_jDux4sS2aM1zQPw-uCal50ZOjzneY3p-RGcX4CB2XkoqR6IZkT7R3XxSLtAzJ18FdS0r93gXCL5uxgpogHT_6HQpKyy143f1I4YIvipK0kz397hbdcvlEWvGAHJ_l7AlIq490QaM8gNEs6xXMY8Xw9WGEWS9rLUN_KIuUJOIFTcQSmo_8ZMzeJSJWXxw43iswRpanCE1q44NPfWKxwbrf67sdZxn0YBKaKhGvMC9LIa-H6KPDZitopWvpyHwz7z4GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇦🇷
تصاویری از لیونل‌مسی در آخرین تمرین آرژانتین که حسابی خلوت کرده و فکر میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100242" target="_blank">📅 13:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
⭕️
🔴
#شایعات
؛ باشگاه تراکتور با یاسر‌آسانی به توافق اولیه دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100241" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqHKHjxEhSo_PdgdXauL8zDH7kE7IzNf3zdbhqGLIa8Mpvn2aJ3FPd_xAiSSIkqhWf1t6d_S1pHLzRJKAjdV-0JAHRn94tpbrnqQ6H-QPxiGoG5VPUNrTZSjRnRGeSTz8mB1xmL-I5y37TjZ2MHO5WDroCiiWJdENrnqeW0x5gtd8VOORBeGf9G7EiczgmLX38pfFNZnEbx5ITAadHb9i4g7sNPMLYH7HYwXCeRQwxNPKU1BITs_XPZezp-ygZn0DwY_qFfDJfXaJk1IaP7VMyhAukWuseMVGoGWg_EiTdirZLRNe4v7CoWyi5rVSe4NKAssNsLXKuJfWOAq8Y3FsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flqFFFytp8RgYGp8PcK11xNL68nULIbh_VUQ4ZoIBhZPAPj012m9Y8TkyVUGq7QcA7GrlOc3CZF2De5YnN8o4jilLnoN-0bDxEb7vFqb7s2eqowYizYADsKhqSelRB00PoOmVJLhQ5RsfWx0QVw7h_zOldo4r-DVjxJhGNyOBen-V_Iz5FPdJV1llMpz1-4oECSHtqXpJVlcGBKTFitszDb_8wibqS24vnKOchNx7gzYFUgscKGN1oZKQ8lkuAAs-7Fag1Jn5BCc5L8LAGb7CmAULX4BE7o11QAz1ZxSb2tIN6sBnD1I0bYNQWMBBzhgNsktqvlAgFxTnpEQIxR88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Imp5Y6_NlUHcUsoM73Fj45qeMVtZTsDcGdUzgEjsBf7CuUiuonRtHd1VHoxEYRCPh0RS9HECMJ8jn389hTZzFPHuqzgh1EpLCCj7jolVawlNW8_FKVSMjIc2y6gbj53n82yVt8dtaIe8tX6VPgnYZQE41Pz6nl9tXwIMpxtgqMJ2k5AuAyrnPZfAVFF8fgO4fUX7zelXfMKv0bJKBFb23UEEWkgs7kKT6LioiBt408KmR1Nx9R-Ws__Q4PtGWfXS_19TZr6eDb0iE-e1gSYvmts69-seb7xmVi_ba_yHyEFNdVV1WTic9SOP4YLEmMjhB47XUX_1hutesZnQsmwqtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
لامین‌یامال و زیدش بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100238" target="_blank">📅 12:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhrhake-fzdGrrdPykxfUh2Eotclq0IOV_q9XaiCmejQKtqOX5jIYucu5P_PN88zlH90-gzyQJ6wgJg_XRLoQXiz9P0j9ooojiZjtto7AD75UYgK9v5GZgQLCHgTA0wrUgDU88woQ2YqLkkH6M6XSoucGGIkrfEOnUoX09sn7fjfhBliXQSaDiIWPXlRsyQ8rAuv4NTwgOPYG91Gx7aznDnPQGtKo34DAqW2Jq-MPcc80ESXsaw0lyRxbvEsIjrNus9u1_LKzpT8hrcOHU76FQoUZrfAxKR9ormc45FcUUf4cH6TfE2acxXN0aWpq78tgUF7RDvKOKq_V6EQN_-FhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
هواداران بارسلونا حاضرن چند سال کمتر عمر کنن ولی این قاب رو فینال جام‌جهانی ببینن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100237" target="_blank">📅 12:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100236">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab89c95bfc.mp4?token=n5VVGuaONjbm2WulrINKrbK7WxinJsw50SBrK6W5xJDkJ5yJK2LZ5YECyNxy2LyQRfnyB2ZFwWKb798GUnV5t-heD3UPcIxg0jCXzRuLt7twP0n9EyT23RAVNLqyv31dZl-2I1h17DY7sdCbqyj69azgpI52wxVHeBDKbS1rslXbVgEYqRhy4drHMzVNekPHZe-JhKHlasL2R4_Oym3lQtkrZDSVDAY4Eh1gNywjvkDJPbSRz5smrEpDmpxzC7yZi2wdzsV-QND0xsBAoEW8cZkJt-JRocIYIci6IH1ybZ_bWxHvCFtTSYIEmAZbJ6aEwjPFl-f3KOVxmsZmPAVxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab89c95bfc.mp4?token=n5VVGuaONjbm2WulrINKrbK7WxinJsw50SBrK6W5xJDkJ5yJK2LZ5YECyNxy2LyQRfnyB2ZFwWKb798GUnV5t-heD3UPcIxg0jCXzRuLt7twP0n9EyT23RAVNLqyv31dZl-2I1h17DY7sdCbqyj69azgpI52wxVHeBDKbS1rslXbVgEYqRhy4drHMzVNekPHZe-JhKHlasL2R4_Oym3lQtkrZDSVDAY4Eh1gNywjvkDJPbSRz5smrEpDmpxzC7yZi2wdzsV-QND0xsBAoEW8cZkJt-JRocIYIci6IH1ybZ_bWxHvCFtTSYIEmAZbJ6aEwjPFl-f3KOVxmsZmPAVxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
در تاریخ بنویسید؛ جنوب فقط یک جغرافیا نیست، جنوب، نام صبوری این سرزمین است که بی هیاهو، سالهاست ایستاده است …
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100236" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a0b012ed0.mp4?token=jGAyTD9axPrCQzGUWTHXQj-oDEUb-2lsy7y5nxrcFz8qeY2LsuM9lvtXgnHiW4CS66NYHBOlzLXHQO50tiFu-TGuGSkD3nWQ3JwKIpAvENTk6OA2SIfTCFI6sNybxOv8QwUQbCL3HYW6jfbjCt5zHMJGSzDAKW16NF01fAuTa_Mwh_mCVB13wl7RF57DhfzfScQ8oRvu6xdlADb_R-bnMBBaxt7JiWuyoeSJyGiF4Wz9ktYeV1I1hRwoOD_4kofXu2HOsMen9hiQAji6pC1TaaSfUqW_LxZUAPHKAd1p5IhpM80sWMpBmWaxGwDRv_pIk9G6ITe_ozyCMv1yFiPDiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a0b012ed0.mp4?token=jGAyTD9axPrCQzGUWTHXQj-oDEUb-2lsy7y5nxrcFz8qeY2LsuM9lvtXgnHiW4CS66NYHBOlzLXHQO50tiFu-TGuGSkD3nWQ3JwKIpAvENTk6OA2SIfTCFI6sNybxOv8QwUQbCL3HYW6jfbjCt5zHMJGSzDAKW16NF01fAuTa_Mwh_mCVB13wl7RF57DhfzfScQ8oRvu6xdlADb_R-bnMBBaxt7JiWuyoeSJyGiF4Wz9ktYeV1I1hRwoOD_4kofXu2HOsMen9hiQAji6pC1TaaSfUqW_LxZUAPHKAd1p5IhpM80sWMpBmWaxGwDRv_pIk9G6ITe_ozyCMv1yFiPDiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
رختکن تیم‌ملی اسپانیا بعد برد دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100235" target="_blank">📅 12:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100234">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG7MEHThpbuCsSayw_BGiR4gsf90o5WtKPG3REJHI2QR3kjAghM8QvjwVulF30QvO-DZz9GjNozXujcFL99HdUkXYxMiwM7IofY6DyapwnePJ7s8WFa1xqLJV78Lim2_2YF89VW0WrVZDorX78k7tRtIpj9EwppM2ojKWujeDzwjjLtp8QipAsv8puMJyuzjfQczdnZVwKDr7sskPz51ygyamjKjs12mgXuc6Pzn9gdgEtfECwk0mph6NjNSecPOLUnT0DweJnmKq9AITjBINK_-k-A93OMwD42wG8v9l9cjPlyARZ3aipzsdkWKBdwtHsKO4xkZi37mKi28Qbuqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فوووووری
: دیشب حین بازی منزل لامین‌یامال مورد سرقت گرفته که با تلاش نیروهای امنیتی اسپانیا فرد سارق دستگیر شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100234" target="_blank">📅 12:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100233">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2632f7587b.mp4?token=TgSkSB82Q3sjQsuKl5uF_AB_NWrsUKP84hKufncvQWNj1iIIohLqYZpmkCAI4qegjgoSfJ82gBuKptzWNmBcXo3c5ClURg3mDC3hvm1Q4TCXaUID40VSIA-mJRE82w3nfBEdM_rW_Su9_SW3oIWPrTflXELXgN7nzAu9bUqx2GGn_gpMH2nPE8ET7CIdFg3bkWMoPu6jBgfSgP6I2Hyp3-FrIrj3wciHpGbelqgkS7q6ENhRuZ_TgJdp0Z0Fe_nlYN7igK2_xDTpj64FUFCiU6e0WSrbZky3_CSCOFbbDa7rZ8X9KRS-wwVkC59VLxHOGZ551quNa5DtZxA3nAeTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2632f7587b.mp4?token=TgSkSB82Q3sjQsuKl5uF_AB_NWrsUKP84hKufncvQWNj1iIIohLqYZpmkCAI4qegjgoSfJ82gBuKptzWNmBcXo3c5ClURg3mDC3hvm1Q4TCXaUID40VSIA-mJRE82w3nfBEdM_rW_Su9_SW3oIWPrTflXELXgN7nzAu9bUqx2GGn_gpMH2nPE8ET7CIdFg3bkWMoPu6jBgfSgP6I2Hyp3-FrIrj3wciHpGbelqgkS7q6ENhRuZ_TgJdp0Z0Fe_nlYN7igK2_xDTpj64FUFCiU6e0WSrbZky3_CSCOFbbDa7rZ8X9KRS-wwVkC59VLxHOGZ551quNa5DtZxA3nAeTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
شغل جدیدی که یامال در جام‌جهانی پیدا کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100233" target="_blank">📅 12:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94662b4748.mp4?token=jz3XETgzJpkAcUtMD6aC8iZ7b8MVHBwKrFhUuQW334FWLmBazAUDJqh4-xbhSN3qGnrZX77HARt0vXnirD-sM9f2GMvzPxKZn2PxfbTpV0o3lVXgFiFjTjxStbqp-aw1SFSgwZ-UlQ1jhWO6r8KglCy56rAp94vSE5cBqZ43S1DL0QOspnv4L9xzftZYq_kTBalCYBhBLaC-g4yOf6gDLe19Hp_g3DNRQ4hhKw0RXQopuW0OiuJKuW3QH6KCTxZEER7yKN_8V1wTgc9Cjna6Yp8ne1i5iHtr0oFRHoFUAo2f9lyNB3giIEF-TivfU2I7-kCUBC29-_4zVc7SipN88w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94662b4748.mp4?token=jz3XETgzJpkAcUtMD6aC8iZ7b8MVHBwKrFhUuQW334FWLmBazAUDJqh4-xbhSN3qGnrZX77HARt0vXnirD-sM9f2GMvzPxKZn2PxfbTpV0o3lVXgFiFjTjxStbqp-aw1SFSgwZ-UlQ1jhWO6r8KglCy56rAp94vSE5cBqZ43S1DL0QOspnv4L9xzftZYq_kTBalCYBhBLaC-g4yOf6gDLe19Hp_g3DNRQ4hhKw0RXQopuW0OiuJKuW3QH6KCTxZEER7yKN_8V1wTgc9Cjna6Yp8ne1i5iHtr0oFRHoFUAo2f9lyNB3giIEF-TivfU2I7-kCUBC29-_4zVc7SipN88w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اووووعههه رو برا عمو ها بخونین
💔
😃
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100232" target="_blank">📅 11:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9efva1-oXbSxBAYJuO_aNZSXEN5D1F7osJd-FWOMcLfiHiLvVturWve140VmCVWZxYXEFtSKIb66s2ESdeu0N992bPwnD6rgNbL6mlpKwqPeJUOOxY28Sa9Y0hOXKdqDrjpWFTFyiHIQB0PTv85u2T5j_UY4nhIe72nrx7-ZurefDJYaQIr5vk7AmAHx6CH93f61PulS6Yhg6htLVQkDIhycXggozgmVBw4A9jCN5sg_t8qAoIJcps0vYHTYYrpqJcmQ9lUK3xy7IsKa12qMfv7ssLERkuJJlKYbU9q1z_HaGaQRuA7ZpcBkHXHIfOFvhSCRlAgnSx15Cbp9KIrjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تنها سه‌مدافع در جام‌جهانی بیشتر از دو گل به ثمر رسانده‌اند:
🇮🇷
•
رامين رضاییان
🇨🇴
•
دنيل مونيوز
🇪🇸
•
پدرو بورو
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100231" target="_blank">📅 11:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100230">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb46db2d6.mp4?token=D8_QrFHB7v5xf_hNrOVvsvTK6SGIQNDKsZPNHedqrxIXZZKnMq_f5LFLIRDqJNTNW-db_Oq-3WHnPThJ10Nt4aGlLTGva9dAbbMB-DyPQ95wK2aMxzT2plgKuYKfJA9aqokqNLslviChb9mDqs7hrjG6zZ4XC7TeaJW3HLwwZC47BpqD3Qysndqf4jQ6lPjoyOmfqry0AlyG7p-Js7lHdtU-54PVdqi7fhdisvtxLM1SyUt1m-PMnMIUOboL9OYV_LUPEd1Gb6tl1JhYKuDdsDgWNJtEv5CTcH6NdkK9qVkU-4LYkogASVVlBqiJ1EZFvFfHTKVNNNWjo3WxzLnc_rk1RDibx0-aIti7uZfirEfHOhi6XeYKXb0v1LhFPPaxBQ10pf3oUNUDdZ0SdybZDqZHqTEPO9cvGfakiQHW4OJcFmbhRNvZduHDsyhDQU1x0mej3i5CrUrv_98iweXvbM3jzeGWKRfDlh6bzIcc2IdcZ0-Vv0IaZxN3mlJiasOSOzsiuh4iwIHIS1Hmngds6hAJq6Vb7JIykxijfi3LnfBtupuW7Z8-sYkby0pVlZHiEWXKlWfotEjceOQ1zyyDFa3yzahQ2zvAkKGM4yQz7S9kx9_fEjli3wkoh1Khumjm0H-qb00eic_gaCu83p5P0AWluN1xrbMoma_WS4wtR6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb46db2d6.mp4?token=D8_QrFHB7v5xf_hNrOVvsvTK6SGIQNDKsZPNHedqrxIXZZKnMq_f5LFLIRDqJNTNW-db_Oq-3WHnPThJ10Nt4aGlLTGva9dAbbMB-DyPQ95wK2aMxzT2plgKuYKfJA9aqokqNLslviChb9mDqs7hrjG6zZ4XC7TeaJW3HLwwZC47BpqD3Qysndqf4jQ6lPjoyOmfqry0AlyG7p-Js7lHdtU-54PVdqi7fhdisvtxLM1SyUt1m-PMnMIUOboL9OYV_LUPEd1Gb6tl1JhYKuDdsDgWNJtEv5CTcH6NdkK9qVkU-4LYkogASVVlBqiJ1EZFvFfHTKVNNNWjo3WxzLnc_rk1RDibx0-aIti7uZfirEfHOhi6XeYKXb0v1LhFPPaxBQ10pf3oUNUDdZ0SdybZDqZHqTEPO9cvGfakiQHW4OJcFmbhRNvZduHDsyhDQU1x0mej3i5CrUrv_98iweXvbM3jzeGWKRfDlh6bzIcc2IdcZ0-Vv0IaZxN3mlJiasOSOzsiuh4iwIHIS1Hmngds6hAJq6Vb7JIykxijfi3LnfBtupuW7Z8-sYkby0pVlZHiEWXKlWfotEjceOQ1zyyDFa3yzahQ2zvAkKGM4yQz7S9kx9_fEjli3wkoh1Khumjm0H-qb00eic_gaCu83p5P0AWluN1xrbMoma_WS4wtR6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تنها چند‌ساعت تا نبرد خونین آرژانتین و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100230" target="_blank">📅 11:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100229">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nitR7Lef4EmGLJfrOcpAA3EJSQAQ96MNjusYZz0QJuszqBHKy0NhIE51wT0y6B9-wsKr53ZQGff6flMqresbGKVuwxqPI6bk_dA7TxHkbQmI9dvyg99fdUpD3PCbiikZ9dWO0wR0bwt2MD7ygCTQ007FJ1XBRWdJrfaLgnvos0prde70o-S366rS5H2Pu_YPtTzp79DS4LEwtdpUkop0SvOjTSwOqqZouolaZpnJIisln3v0ubaoTzOPgucLO5yyxaCQWFznMXMBXxepUXzsDNApbA8Rl70PZ5BZPRi5R-6J3M23fc_b05BLUppJYVGZolLFOjL-XcGRiLV0y6kIZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملاقات مارک کوکوریا با کارلوس پویول در پایان بازی با فرانسه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100229" target="_blank">📅 11:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e3ee053f.mp4?token=MRr3DzwLGMMrRN7aVNhhuwMbFx4rtr_nAfR0mVHJ0Xb3Sdodsko2tROGnbK4lH742AgA7elbIzk3CNtV-YjNgzGsFZyO16WgMcIRFb5xY_9fldzkj5P2TJygLRPB0qnFQWa4nZFBB34I00pWWA0-bz8Wz8U-8qmzyRiiV2b6i_SSMh7q6cScGnHT7v5sc__odtNur326PZ0rfjk2W3Lv1Ma7PAPmimQfF3vns7zQ_-Gg4Hh5Td0KKvM2Gg_9iC7SIKoOpkQLF1eBpB0qWhRGbvCgmtiWKE7a0YugymbRJGQw-Iq98DqZsPu0mU3XyuKbBZA8YyjGexGMFYUFR_rh7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e3ee053f.mp4?token=MRr3DzwLGMMrRN7aVNhhuwMbFx4rtr_nAfR0mVHJ0Xb3Sdodsko2tROGnbK4lH742AgA7elbIzk3CNtV-YjNgzGsFZyO16WgMcIRFb5xY_9fldzkj5P2TJygLRPB0qnFQWa4nZFBB34I00pWWA0-bz8Wz8U-8qmzyRiiV2b6i_SSMh7q6cScGnHT7v5sc__odtNur326PZ0rfjk2W3Lv1Ma7PAPmimQfF3vns7zQ_-Gg4Hh5Td0KKvM2Gg_9iC7SIKoOpkQLF1eBpB0qWhRGbvCgmtiWKE7a0YugymbRJGQw-Iq98DqZsPu0mU3XyuKbBZA8YyjGexGMFYUFR_rh7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری سمی امی‌مارتینز از آشپز‌های آرژانتین که درحال پخت‌غذا در اردوی این کشور هستن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100228" target="_blank">📅 11:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmvUMjv12uQJdMs_G0I6eJSEBNV3StcbRyWnvltpjuVmHdnvveqwh0O-p1KiKfmARV_V1azppzmr8RNHT9-Nv7QszmxHtM4ukBz3HFkDdRQyjloSXvpnWtr5aDl7GhrM4ozG4DcN4OoMjK-ORe6V9bA7d_KO_a-xB-4TR4gz80exGpirUVQIINJjjLcT7kZFmiztH_ZIs-LbFhbSjdiFyABd7WwSje2HDecu8M1Lznk-ekHf-Qz1MF_H2-llN4NLoapXPsxBeN6ceE2dj66eqvrUJyA9u-0jNeCZy7e7hHu7Hbgby3d2VTPtUok0okELmEiF3O7vFDPmGFgOtNMunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متوقف کردن مسی ؟
توماس توخل : حالا یه راهی براش پیدا میکنیم، امیدوارم سرما بخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100227" target="_blank">📅 10:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100226">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHaIPyuXqmwwXRSEscNaUZeu6vMoZAwdRIVgYzIGELfoudWnGRJnNxDthKFBjzLPD2a8klLXwZM20-kGnbWOozzqtTdZN9BYXohaf9Xy2bwKdVzhacB_REL37lqxVfJie-nQVO_jVHwowXh3q69TC0d-tEhOlejTyzrndTNmAh349A2Ydo-aUjFs76z8ur22KP_B-mQ7vDAt2Exh1Q43864lBYXjL38WJFXHsR0tHM-vBeUTrAMMLA4VKSoauStfeRbN4cerydb7A1CwzOHASjla59sYVvAiiLahgPzZG9RiTerm70Clo1DR36QoO14rDdr875u0bObShiaxINcuqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
انتقال مارک آندره تراشتگن از بارسلونا به آژاکس نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100226" target="_blank">📅 10:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d59df3b59.mp4?token=V23FcE4W5lB-X7OTxDbbhexYIE5h-5_BX6r_PHsu9oiEimSSlThcuKBE_HbWWHFUJzDhfo7DGpeKsjLOZKi3KPW5sAnK5DxcZXmzOa4ih38_Uxr7Ze2l_JA7By6PPV_WcShLJ45rQmmZY_0063uvSgy_GGH8L197QZO2d5pD7ACP-3QBqpnASzA_hdnCWAyCw8EU-5OFSG2xaGUBNJ8NuMlt-s_AzCv3lpzH8Vzhe_NW2q8gi_7OVQIyp7NbkvRGDSinv0EbbhE-Tu6oR1gRxoCD8jBM2LbWPZAyj_4XZjlcyKMw0qluyW1gvgyMxr03idCi4E0sonEsWVERG2d6Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d59df3b59.mp4?token=V23FcE4W5lB-X7OTxDbbhexYIE5h-5_BX6r_PHsu9oiEimSSlThcuKBE_HbWWHFUJzDhfo7DGpeKsjLOZKi3KPW5sAnK5DxcZXmzOa4ih38_Uxr7Ze2l_JA7By6PPV_WcShLJ45rQmmZY_0063uvSgy_GGH8L197QZO2d5pD7ACP-3QBqpnASzA_hdnCWAyCw8EU-5OFSG2xaGUBNJ8NuMlt-s_AzCv3lpzH8Vzhe_NW2q8gi_7OVQIyp7NbkvRGDSinv0EbbhE-Tu6oR1gRxoCD8jBM2LbWPZAyj_4XZjlcyKMw0qluyW1gvgyMxr03idCi4E0sonEsWVERG2d6Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ملینا بلیک نشون داد هیچ استعدادی تو گزارشگری فوتبال نداره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100225" target="_blank">📅 10:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67f731ecd.mp4?token=nE3GsaI2k34QD0m2HvKUk1Od8l5_DuL06ZUfrrzt0-g6RTmWHqx70nhJ_LcTf5pmshypkqmCcC8byd8zN1-CUW53EMF-n0sRQKlAudhxqv5pPtwbq08NtrAeElX6s0lVfu1RcLUNYq5UC358UM4IPtWZU3SOi9JJmomPvr0MoBnVT2U4eGxI3YsIrfikI6wRzlKS4l6upY_lO0rStlj7srHCLJY798FOoLeAsNvqF_PUfq10ZQJ3KRGWG0vkIaIuqaXqRpGKS3xfYPgXN9ov6Xknt4_1-vC-aRfkauccFbUSprHaR4mUNQhPYDZ3Tdm3eQyOXm2Jm5KBKBczR18sTxjlzNXh2VC180BeummjqIuZvXW1kTrXtD9nnABDlvUWKIbcV-ODF8oerfI9LdU5btJ7PHzc5BXX3AykMjFGW07fkfJwzxoVj5la1MVrmz-85wW1wOBp-oGXK6ZbnQub_5QUsiqELC8GVsQbBLsfPrxwGfsH-05PpqvLn61aTp-QgH6_26dpz893IKM7GJNJMslSc4Ol4ICoCS3Swab4OS17eCg2ku1d9OSjQjopV51gpEe0Q09QzJ2zg6NHJNN9j5j1B7KX8lCBik8W1BrH_v3BM7bxpYFO9VrDx2MAScer1HUrrbfyYeR7CXBaw03S1o2lEvIIfCzebKkSjae5CQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67f731ecd.mp4?token=nE3GsaI2k34QD0m2HvKUk1Od8l5_DuL06ZUfrrzt0-g6RTmWHqx70nhJ_LcTf5pmshypkqmCcC8byd8zN1-CUW53EMF-n0sRQKlAudhxqv5pPtwbq08NtrAeElX6s0lVfu1RcLUNYq5UC358UM4IPtWZU3SOi9JJmomPvr0MoBnVT2U4eGxI3YsIrfikI6wRzlKS4l6upY_lO0rStlj7srHCLJY798FOoLeAsNvqF_PUfq10ZQJ3KRGWG0vkIaIuqaXqRpGKS3xfYPgXN9ov6Xknt4_1-vC-aRfkauccFbUSprHaR4mUNQhPYDZ3Tdm3eQyOXm2Jm5KBKBczR18sTxjlzNXh2VC180BeummjqIuZvXW1kTrXtD9nnABDlvUWKIbcV-ODF8oerfI9LdU5btJ7PHzc5BXX3AykMjFGW07fkfJwzxoVj5la1MVrmz-85wW1wOBp-oGXK6ZbnQub_5QUsiqELC8GVsQbBLsfPrxwGfsH-05PpqvLn61aTp-QgH6_26dpz893IKM7GJNJMslSc4Ol4ICoCS3Swab4OS17eCg2ku1d9OSjQjopV51gpEe0Q09QzJ2zg6NHJNN9j5j1B7KX8lCBik8W1BrH_v3BM7bxpYFO9VrDx2MAScer1HUrrbfyYeR7CXBaw03S1o2lEvIIfCzebKkSjae5CQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
گرشا رضایی: بهترین صدا برای گزارشگری، جواد خیابانی بوده ، هست و خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100224" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100223">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏆
گوشه‌ای از بهترین سیوهای جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100223" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100222">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f24ohMNDBKLJGXQjWvBTDCW9cwCJoeftSxnraprO6tsOKYJVvTa2AWQXaq3asRDpIYpd5Xe-q1bo78OFC9BFFLNB1FWt5O6MFzBuHC_FcwNiKFcopCiCHxMQmermwPHCXf95FMvF0qa43xfoZbwatxfBQPW86LbctbSph6OrqlmV5QPNjwxvuEJXLO6uSUiGa7THyj4YXaigA_HrmKtwP3Ok3WlRzzgLZdbYtduN8shFYSU03igKmG25wzGV6XLN1H17BdByOR4JOLPvTQEhMS5dXr0etD1yKAdMrgK3HcX374MWyD0w5lTmyt9SSd5K2WJhX9ZEnLunk7Rg5cvsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین رشد فالوور بازیکنان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100222" target="_blank">📅 09:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100221">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👀
🇦🇷
آرژانتینی‌ها از سنین کودکی به فرزندانشون میفهمونن که لیونل‌مسی کی بوده و چیکار کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100221" target="_blank">📅 09:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100220">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">در حمله شب گذشته آمریکا بیش از ۱۰ موشک به تیپ ۳۸۸ ارتش در ایرانشهر - سیستان بلوچستان برخورد کرد که گزارش‌های اولیه به ده‌ها کشته در محل انفجار که عمدتاً سربازان وظیفه بودن و دست‌کم دو کشته‌ی دیگر پس از انتقال به بیمارستان حکایت دارند؛ تعداد بسیار زیادی هم مجروح شدن.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/100220" target="_blank">📅 09:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100219">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pELxHSWEWLAruGWjGG0YEKaHtoSRNkngNp4WF6OEDKBIKv8X3YxdQLEqsJw0w1hWCEHKQsXbDts7p5s3HonbapP7ocARTdBWaekl5i93o-2P-YUehvOiOi6zn_IT9f-ccg-4nP1TRg6Tn8Y5AtrUhVcdjHYdmOnyIc2xue6c1zNziSByu5ux_INYO6xoZ1KlvvAV5Ag58l2h3lRB6tL00HgntJLXWfVypARs7JIqMJAdR0ZxxEU2cJtGI_XFivB74XKoOaF7x0WB3Lf7pSscaPwkPwzRctJ0NAMRbcEoWC-Qq0Do-I5KgIbDGt_OnBsIesF6MfI1tsN2kWug78RTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
با اعلام فدراسیون فوتبال فرانسه، زیدان رسما سرمربی خروس‌ها شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/100219" target="_blank">📅 08:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100218">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxRZ4u1fLbmcNFY7YxUc0f8ZpeTj_5lQQbndzJWUNE4IDTAN9Do5cwYOsQNNNbTkXAysamdKZUqdB282n--HD3eo66huqad0V9jC79bFvXs1N--2opHkVmI5kHlv5EhkqEt7kfIggJc6HlhYcvLI9hDqkiC81oPoH1_pkLcBfZQHFzFKuoGya64YPTHq0xCMem3wp2DWDHWF791Qxu3tNYZHiTnZQgzBGz1BJybMA8koRKFR0a3ClofanWg2kxLOeO0Sm9Z8rRA-udlBSisTOB2fFuJWJzQWbTrFB7raUp6-9VlwW64Tuh0T9bcHbEirxnOQrnVB4sOJecBpxH__2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🧠
رودری با 11 بار پیروزی در دوئل‌های خودش در بازی با فرانسه به تنهایی از کل خط هافبک فرانسه (9) بیشتر دوئل موفق داشت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/100218" target="_blank">📅 06:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100217">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d888d31120.mp4?token=VeHjRATgd_tXZ7E2SjGdB0hnx5DxBoGIGPOgWV1pgLLqdsA7bp5zdwvWXsT-cQtLCVs10TdHRth7WjWgu5lnLGHnCSH0Q45LMafYTo9yl2UhNe1Nsc_rf6VrCeEPijmhqnhWrz7zAydfC1c6hmX9ikVqaif8D6ppGc86tu4xqZZh1i5-xFbF1kSy0V7qTpmPeUgdailoBNOGjCnxJw7mBhMKFczjhKpxfZZpFTAWO89DzQkmRzgx0t_RnQ3dsNEHqSV6NcUe0pBkMnQOR7RhJlFlSpbrIm4UO9HVMLbrdL3LpXpkrWgXtYTM9BY4Z8ecoWScBrTEuaY8sLvbJn-amA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d888d31120.mp4?token=VeHjRATgd_tXZ7E2SjGdB0hnx5DxBoGIGPOgWV1pgLLqdsA7bp5zdwvWXsT-cQtLCVs10TdHRth7WjWgu5lnLGHnCSH0Q45LMafYTo9yl2UhNe1Nsc_rf6VrCeEPijmhqnhWrz7zAydfC1c6hmX9ikVqaif8D6ppGc86tu4xqZZh1i5-xFbF1kSy0V7qTpmPeUgdailoBNOGjCnxJw7mBhMKFczjhKpxfZZpFTAWO89DzQkmRzgx0t_RnQ3dsNEHqSV6NcUe0pBkMnQOR7RhJlFlSpbrIm4UO9HVMLbrdL3LpXpkrWgXtYTM9BY4Z8ecoWScBrTEuaY8sLvbJn-amA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇪🇸
شعار هواداران اسپانیا: امباپه کجاست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/100217" target="_blank">📅 04:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100216">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8960eb8b.mp4?token=IVEZjN_uGdP_WE-m957bBxOEvNoNQuYDH_-C0uFeIgH2A_FcCR8LStYj9PvEoa10xjpb0Xp6kIF8Cuw5c0Hyei0fMqFxYxMqAHimtZDBPw_QHg97jy1bwx5fnhSpjmN4RG4FRgIQgzyalNzF807RFJ0dRe8gwJPZZZ5MkLPE_VCRKhzbH2G5jtwKkutS22kd63nXBihnpU8kcw786e6rIu2-juHlZqkidjajLYOp2yP3qIbVamE-9iinDKyMM5tV24rzHd9fZN08vn0fV86sJZoI_WDzZukqh3tGLiAZnI1SOzO_NJUL43a4Lvkn_zHB_Qj7YS9oc8AeMyv2I6jN8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8960eb8b.mp4?token=IVEZjN_uGdP_WE-m957bBxOEvNoNQuYDH_-C0uFeIgH2A_FcCR8LStYj9PvEoa10xjpb0Xp6kIF8Cuw5c0Hyei0fMqFxYxMqAHimtZDBPw_QHg97jy1bwx5fnhSpjmN4RG4FRgIQgzyalNzF807RFJ0dRe8gwJPZZZ5MkLPE_VCRKhzbH2G5jtwKkutS22kd63nXBihnpU8kcw786e6rIu2-juHlZqkidjajLYOp2yP3qIbVamE-9iinDKyMM5tV24rzHd9fZN08vn0fV86sJZoI_WDzZukqh3tGLiAZnI1SOzO_NJUL43a4Lvkn_zHB_Qj7YS9oc8AeMyv2I6jN8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود اسپانیا به فینال جام جهانی 2026!
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/100216" target="_blank">📅 03:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100215">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bb44d472.mp4?token=E1GNxRZRWh6Y_z6Xyi8Tler8RVstZ5__y0oOD_Keo71Kz2MXihLF7fHFwIm21IDwPwD5RVvdXF9HGRnccGB5ArkSvjdZ04aEWkX9eq4C8fuuuGtJv2x7k-P71IkTB7_arQwJ-3Qv0Eim-FNWlLo00soteOtGEzv2v2MBxGAk7WHyNpPmHVJy9bJZXmJ6zhOPqC5X3SMmGdCs-Lf7NCTotrQQ6PN3yRWcXwmZPbpWGDEN1o2i5JrgRzhIH03UdctlT1ZS9meylx3J_JOQfCoaft4jgyTOTOXjh3ICbnpwPiFpOLib2r7SiJdXPkgWxGRLnhV4Qn19oj7M_-PHqKN9Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bb44d472.mp4?token=E1GNxRZRWh6Y_z6Xyi8Tler8RVstZ5__y0oOD_Keo71Kz2MXihLF7fHFwIm21IDwPwD5RVvdXF9HGRnccGB5ArkSvjdZ04aEWkX9eq4C8fuuuGtJv2x7k-P71IkTB7_arQwJ-3Qv0Eim-FNWlLo00soteOtGEzv2v2MBxGAk7WHyNpPmHVJy9bJZXmJ6zhOPqC5X3SMmGdCs-Lf7NCTotrQQ6PN3yRWcXwmZPbpWGDEN1o2i5JrgRzhIH03UdctlT1ZS9meylx3J_JOQfCoaft4jgyTOTOXjh3ICbnpwPiFpOLib2r7SiJdXPkgWxGRLnhV4Qn19oj7M_-PHqKN9Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/100215" target="_blank">📅 03:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100214">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f573ba753.mp4?token=JSbAt46jWuBRVjYpaIR79voYSEU4N9ptbPzTH4ypywFaQnjsnzLZ6GwGwAoUcqfPkDmscX-IbDBbYQevNzPY0Y62B72QPSLkgIcEZclfKs5cQi1qLinrm99_nruqg5cZIfcbqAxsW75Vj9YRtyvti5_LzV60A9HEwZJFITXTyyy8vkHKIHImVHklLAN4VeFDtH-nlWJE26phB4LuZhETX63s1SimYomRQy470KsdDk2KR5uHDw0xbVx4KgvQpQBUOzyF6b_cJaMkp8OOaETt1ByOTD9aCYQ-C8g2KVKJ4odrPVngjSgGmos6CM2yDNPnXgKQtMU3ChKEcfSGvK1FNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f573ba753.mp4?token=JSbAt46jWuBRVjYpaIR79voYSEU4N9ptbPzTH4ypywFaQnjsnzLZ6GwGwAoUcqfPkDmscX-IbDBbYQevNzPY0Y62B72QPSLkgIcEZclfKs5cQi1qLinrm99_nruqg5cZIfcbqAxsW75Vj9YRtyvti5_LzV60A9HEwZJFITXTyyy8vkHKIHImVHklLAN4VeFDtH-nlWJE26phB4LuZhETX63s1SimYomRQy470KsdDk2KR5uHDw0xbVx4KgvQpQBUOzyF6b_cJaMkp8OOaETt1ByOTD9aCYQ-C8g2KVKJ4odrPVngjSgGmos6CM2yDNPnXgKQtMU3ChKEcfSGvK1FNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تشویق تماشاگران فرانسوی توسط امباپه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/100214" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100213">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQoxFFRbaZLVelJfBa2lnNsu817laP5K6YLIISp4ODN_aDYxGFiYYe28l2VJfggU-m6YiKM_pI9U_NWO4jVvq7zGzfLbnUnAFtDG-Q4gZbWPGCmJrIeUZQuhXF30o_MbLBruFbiSxFsjYmT3aEpmfieqcuf-FK-GIZAQ0RoGBoJ94G1P-s40EYAOynKkZaeSNvFqs4qzgL96ZEpZ0rU2DLuy2iK5eD0ZVnBDhHWtFx5HDLNVAJngdUkumNS1leSHV5aj_DTW5mTG4hr8vygOgAjFJwioGckU7QlxSQnIBFm31yGMpBPHZxmuFJXILmMJ-ghFcxoZ4iAkjln-7RYpQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
🏆
‼️
از میزان هوش داور بگیم که بنده‌خدا یادش رفته بود اسپری محو‌شونده خودشو بیاره و وسط بازی داور چهارم رسوند دستش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/100213" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100212">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری ترامپ: اگر ایرانی‌ها به مذاکرات وین نروند، هفته‌آینده تمامی پل‌ها و نیروگاه‌های برق ایران نابود می‌شود
❌
روز دوشنبه‌آتی دقیقا اولین روز هفته پس از پایان جام‌جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/100212" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100211">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری: ترامپ در مورد یک حمله زمینی به جزیره خارک: " کافیه کمی صبور باشید. من این کار را مطمئنآ خواهم کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/100211" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60a4ce9f7.mp4?token=WX3RshaVFQsnsWg-bYl6RZnt1fiOo1pVAllYBLvBHbjXN4qOjKmHGFYIiigrjJJl5lDRHb0gddRh3z2hghamD7FuatTkM7PRxGjG3vXK8xJEd38s-demZSVDBYNcFvVMhIZKStgT8STVIGIpis_hP4KVaTmhBxsaYDOeSjKmU0ZQsirLEZ7sckOGrbaxk0x6MBC55XcF7gIdvzrUZ6TNHyAiu5XVB0eEwQL3z0ymNYGN-g3RgsUrCELz7eugulC6MwInW5dXpmucEzqqt344y-j-S58f31lXcI9A8QISehy0YwjO3Qj0b-qxmGYFWNPSKfYtIzniWyVUQmbTH-eO9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60a4ce9f7.mp4?token=WX3RshaVFQsnsWg-bYl6RZnt1fiOo1pVAllYBLvBHbjXN4qOjKmHGFYIiigrjJJl5lDRHb0gddRh3z2hghamD7FuatTkM7PRxGjG3vXK8xJEd38s-demZSVDBYNcFvVMhIZKStgT8STVIGIpis_hP4KVaTmhBxsaYDOeSjKmU0ZQsirLEZ7sckOGrbaxk0x6MBC55XcF7gIdvzrUZ6TNHyAiu5XVB0eEwQL3z0ymNYGN-g3RgsUrCELz7eugulC6MwInW5dXpmucEzqqt344y-j-S58f31lXcI9A8QISehy0YwjO3Qj0b-qxmGYFWNPSKfYtIzniWyVUQmbTH-eO9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/100210" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100209">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
: ترامپ در مورد یک حمله زمینی به جزیره خارک: " کافیه کمی صبور باشید. من این کار را مطمئنآ خواهم کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/100209" target="_blank">📅 01:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100208">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a1bfb1af.mp4?token=YdCFGuZnpieNTZ5pItcbRXQeDpc4EbW13DGrASuPob5oGh0RQEIo0NubGqV7eASv19R-PRXu-JLoes2GjhxTcmJ9mJuC8BDYdn68jq4X-cwSI54Qex_QJwjwneISTmc7E0sXplQ-Oa0NXC4-tduZcbYV8gE0xpiWx9TAjKgsHUhbUi7U4QXxSOLDU_7UZkjMXicyoHZnONa3rPqyD7NUzwpKNRF86H-7D53IL1ZcDPg5CrGapvS2W_9XMwtlD0rmD_y_bYGmwqqkGiYuvdv_K5bPwiFLZujTlsb8VpmXemk6eAQFFRxxETMrN1Qo7TshO5lDbCGUQShMXDNyd1AS3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a1bfb1af.mp4?token=YdCFGuZnpieNTZ5pItcbRXQeDpc4EbW13DGrASuPob5oGh0RQEIo0NubGqV7eASv19R-PRXu-JLoes2GjhxTcmJ9mJuC8BDYdn68jq4X-cwSI54Qex_QJwjwneISTmc7E0sXplQ-Oa0NXC4-tduZcbYV8gE0xpiWx9TAjKgsHUhbUi7U4QXxSOLDU_7UZkjMXicyoHZnONa3rPqyD7NUzwpKNRF86H-7D53IL1ZcDPg5CrGapvS2W_9XMwtlD0rmD_y_bYGmwqqkGiYuvdv_K5bPwiFLZujTlsb8VpmXemk6eAQFFRxxETMrN1Qo7TshO5lDbCGUQShMXDNyd1AS3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
داداش‌یامال بعد گلی که لامین زد و مردود شد حسابی زد زیر گریه و اشکاش بند نمیومد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/100208" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100207">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSlQl-ydhpLkYGzvZE0a0OvyASJ4c-ZOmNdq3lGZwIohLupePvrMWVUCSyQ1bhgLnqFZdrjq61hxi8pT6S_ryqt7Y1V0_nN2v736oFh3IKsr8SajfC9ncoITazWYOGs_s7sJXlpaHmq14YhXrNfmNCEIYQoWlCHU6hwxev7zeVV_pKRAQAU1jCYxR3XXAkBGXTrn-R8j11iIQeQ9JqMJZd97BfBJpcyp-fB8K8b9ySJIfujDNv9r2msEgzZKwats-_0bCVyz7TRl5tfMNxaSD8uv8S-F9FnMc7fNAq5a2EExLDrOognH6cuKx5vBhX4AKl4UxHhHM2MckSx-c1rWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
پدری، یک سال پیش، پستی با عنوان "19/7/2026" منتشر کرد، که به تاریخ فینال اشاره داشت.
و امروز، پدری به فینال صعود کرد.
🫡
🫡
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/100207" target="_blank">📅 01:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100206">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e25e4d415.mp4?token=MExDEeskPyNBYVMSNcS2QlrpN64vD2_P842hPA-a1FnQgO6H7OqsWpP5vxzRKhNVMGjAre4i8uE66XI0Qhw01WMklhiOYcaS-kV6Wg126Qfd0ziks586y0yTNCxIjqe7kYJZ5SQkVe-EdY1da5qWkn5l65kLIrl67IVr3I8X2SrbW_4M9Gz-_yaquTEZ_6YOYPhXQFb-7a6ndvXsgupye4Q-uLNGIY3obvPvvD7PLVfC22AUjHjUzsjyYKoGXPetBGJVvCWlcb-2Qxe6nThczAXpGQimd33ArfGwKT_XYlwCAByVceT2Ua0u0tur47E0xVOdcBmkJmPrkcdV08-qjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e25e4d415.mp4?token=MExDEeskPyNBYVMSNcS2QlrpN64vD2_P842hPA-a1FnQgO6H7OqsWpP5vxzRKhNVMGjAre4i8uE66XI0Qhw01WMklhiOYcaS-kV6Wg126Qfd0ziks586y0yTNCxIjqe7kYJZ5SQkVe-EdY1da5qWkn5l65kLIrl67IVr3I8X2SrbW_4M9Gz-_yaquTEZ_6YOYPhXQFb-7a6ndvXsgupye4Q-uLNGIY3obvPvvD7PLVfC22AUjHjUzsjyYKoGXPetBGJVvCWlcb-2Qxe6nThczAXpGQimd33ArfGwKT_XYlwCAByVceT2Ua0u0tur47E0xVOdcBmkJmPrkcdV08-qjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا خوشحال از صعود کشورشون به فینال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/100206" target="_blank">📅 01:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100205">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=P-yiHVwk5su5EYqZxqDf0of4COP_aIA2UfKI5w2hQsgVmDtVmz3VmZv6pgE7A-HZUZfYCf5M5KBhzkMVQLZEkkYgj1FUF9DZ5h3jAJBsHnqYaK87ycWQ6wexotPDoHKupu6ziZJqqgSmY2ZQV6ZPo838P-DcqIqGMxv2_Yu-gvTnzpf3v4zsyjDMi3X-IgqrKQ0JWuxMaanTho8qThKKtUF01IC4gqEirDSepeJT0jk3aMpyXGYOM6ueUCKnD7Hcwwln3OSTOih35Gt4p4-Q-HI6Pj9EO_FQVnRXcSTxxJ_rKgY0anTZL7djqLXEXimv_-Ppu1kZGbGF2-klW2Wc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=P-yiHVwk5su5EYqZxqDf0of4COP_aIA2UfKI5w2hQsgVmDtVmz3VmZv6pgE7A-HZUZfYCf5M5KBhzkMVQLZEkkYgj1FUF9DZ5h3jAJBsHnqYaK87ycWQ6wexotPDoHKupu6ziZJqqgSmY2ZQV6ZPo838P-DcqIqGMxv2_Yu-gvTnzpf3v4zsyjDMi3X-IgqrKQ0JWuxMaanTho8qThKKtUF01IC4gqEirDSepeJT0jk3aMpyXGYOM6ueUCKnD7Hcwwln3OSTOih35Gt4p4-Q-HI6Pj9EO_FQVnRXcSTxxJ_rKgY0anTZL7djqLXEXimv_-Ppu1kZGbGF2-klW2Wc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یکی جواد خیابانی رو بگیره. بعد بازی رد داده سرود خداحافظی میخونه برا امباپه
😂
😂
😂
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/100205" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNKGFepptS4gahv4BiAlN8gRRSxv99bNkfqjm04ErjxHKCfIq8fEl0W969yihSH6FXLBCZpLwhkxxK4PXDEnsU-_kXTK0AwUoqxp7VxjSmO-Ly-IPfMPRRE3EUR18HSh2gxEpPMNrfk7EJkyOKGY2AqxLlHNfDKemdrZy1nACyjuusfLCbPcg9wZOrw621MMHINYXDAf03TrMytR0qdTAfzGb8sMxfJtxVS9lgYpTUVxB2CxEFjSpARrm_osQGOKRr7grQv9pKc7hC_hsFngw2aYRYUe7vVZKMMw5xH6cGTwUYCFXBVX4V-WUbna4X-SBgzM191WgdV0vfaJyc9-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">25 درصد از شکست‌های دشان به عنوان سرمربی فرانسه در بازی‌های رسمی مقابل اسپانیا بوده است
16 شکست
4 شکست مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100204" target="_blank">📅 01:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4ERJ5tS0EWVv6IMftkZ8Pt8E2aQ54-Y_vIIViRkLYEM-KgAtaDv42yU8jLpBP19luGyaXFk70EVLJAvJNXuLSq-6kKY5wVq_HaJXU-X2OrjU4YZ2I2PhPrcgqMiEYBq1Zt0tqMXcjew2-jJ4vJL1tneGBYYptVMwwjvPeHx9RYZws-DiAS-QXQnmciuvjlZyaTzqJQPSqL8BuuUcxNVO-yejFT4669OmJ-68abJrZYQJtGcd8h_Mhe8lg2GTRbXjeZX2KUJNIMvH-lqyX55d7-yeGDQ9W5_R-Up_E6KxC5CM7R6po3gM35mGieplcv157L7keqWutWO95HrExYMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رایان‌چرکی علیه دشان: مشکل داوری؟ قبول ندارم چون اون باعث این نبود که ما گل نزنیم. ما به تاکتیک‌های خودمون و قدرت حریف باختیم نه داور مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100203" target="_blank">📅 01:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100202">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUWGetN-t7wXPW2XOl_9JrrjnlEYtbVyXIN8PKHmoH1i2eZtq4QkguWfYti3SoyhPRId5Pxb9LcBnLZhTiH0Mrbpm5rETpKXgOGOdcudDU3QmJRIcpX9xu8SGAI7M_av9wIeE8WrEKUgNVGy3nlcBMYV4dyH-5PDropqYGjJa2nnk1DdzYm5wCOkHbSQcLs5UwVhgC6GJ4IroDTGiUw9lKgfvbaWUvmt47c2a97qrzklzzz5WfEeIMosuYdSwimuvHdZsfpLvoDZuqTw6DkMiOkVyT85Tx9eOhS8fh4vrfPcA8PIDwHhnHywUdXKUAOPJ1BiJfeSWUiNT31b7LKd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👤
لامین یامال در 12 بازی، به عنوان بازیکن اصلی در مسابقات یورو و جام جهانی شرکت کرد و 12 پیروزی با نرخ 100% کسب کرد.
😮‍💨
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/100202" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100201">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltBzxR0nxNRotDhWCtslETMfQko0UjBooMvPtQ05n0quwtT37XiWf1tPJnGPpbJ61eOFwWOUXH7CjpjGQPwxIiD4D2RENiVGe8TWRkdqNj0V00ccjQWxoQygBn32X9cO2FSt5p477XBOvqtggn5NFiec5SJ-wXpU1KRtjd0O_L-a4sY-oDQLXT8ambntlljLEF5t5hP85M2Q5YLIdzgNX9rEamiS8Uo69IfRtPxxHFRj9SPq6-5uY_FfEx_Atixr9Sil_OERkTKFFCPj0U5RlZJyYGQ5CrXjH2eDiMG6Ey-haOXHzvXRoxTlSZ4VWHSagTMQHpbgJ-1Tepmc0OBQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
امباپه در تماس با اکسپوزیتو: امشب انتقام سختی در راه است. خواهیم دید چه خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100201" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100200">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeAbLtlBgV0-_C-KD5tPOYhH62nWUg87cdy_YqmHn7VsvVzem7qylmW4Y33JDjyn7nCTIplzLWhyWI-1h5szU1rmGNKg9aRZ5PsLFgvSPXd9YxYCpyG3BqPcBeTZ0aGFlUcTzqOfZwxp2XylT_QwO9Sgo6B89wM8bbV7IPh7Ecu-05Vp6LA1HfHHKmrRw9RbuVbU_MqhLVKk0AY8g0NQ1mZr20Dk4qUobYPTkc9HdVGFTh02iZKVinvidJAsA9ldjkD5bJqzGeYwN0xydUEfZHcT2oFKkVR3-GFlu7p5hSDfwBqcZ3RRO5m_KQ6wjVapMnu8CXZ1wFueK55JAzs6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/100200" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100199">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=VlfJzHIJ-RBrE3AD09zAoFEV4gKAfNHf9KeoWwXfvhOvGtr5OjeS1ebO0UWnUtX3odNZ_Oyq0mLMzhsbs3wXfXChUlaiIhG2rc2jGrdWedJfX-tArnuc4-P_6Zp9o5NdmgUbMmhhnulYlS8hUZvywGISH6kpF128eQUYi44-voa3l2qW9R2ih6U9tMIRB44BSghmc1U78BX5d9V5xT7V3-aYFDmLanxFMSSiUP7_OLsHSALnPmJb7E7dhIhHFYHRw6HFsKQ3w8EoeCHybZni0x7sDOHjoPgcNbExNCZTEtXgU3seicfaGBYkze3Iz6nfF8H0GzSAX7xHD4lC399Gjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=VlfJzHIJ-RBrE3AD09zAoFEV4gKAfNHf9KeoWwXfvhOvGtr5OjeS1ebO0UWnUtX3odNZ_Oyq0mLMzhsbs3wXfXChUlaiIhG2rc2jGrdWedJfX-tArnuc4-P_6Zp9o5NdmgUbMmhhnulYlS8hUZvywGISH6kpF128eQUYi44-voa3l2qW9R2ih6U9tMIRB44BSghmc1U78BX5d9V5xT7V3-aYFDmLanxFMSSiUP7_OLsHSALnPmJb7E7dhIhHFYHRw6HFsKQ3w8EoeCHybZni0x7sDOHjoPgcNbExNCZTEtXgU3seicfaGBYkze3Iz6nfF8H0GzSAX7xHD4lC399Gjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
ولی این صحنه خیلی حیف شد که اسپانیا گل نزد. یکی از بهترین کارای ترکیبی جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100199" target="_blank">📅 00:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100198">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf3e_IVwvRrLueViKqyXJko_3ii_tP0aEf6K5WETYBUmwMuYgKLjJnK-e-2ZB3K565YbkMlRgJu3GKn72npX7tzGMX1NXQvm-zN_oyhZiU-Rbsm7zpvGuK8VjIXq_GcXl8Qsc-21WXFt-pHlQZjQcHLBFrkTB9gQDkyZ37L7mpUFYG2_nKvVJSLmYYUiV8odg3iFD4NOTjg39iPhWwGIqyvy9dikNYL1MUCpa40TqRI-ldhssNY4YjD3PDy4oTTjutnfil7XC9ELo3KMy_sXsuzm5QQg5seUld-FibzrGdR1aF_l2chJ6xKnIeK92EP1F_MOVSk9eI6VCAqGPtinFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
رختکن اسپانیا بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/100198" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100197">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
❌
🇫🇷
دیدیه‌دشان: یک سوال جدی از اینفانتینو دارم. آیا داور امشب عقل سالم و صلاحیت کامل برای قضاوت در این دیدار مهم داشت؟؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100197" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100196">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=EIVowVQPs6NHWL0rOKg5zL3RRmFi9IRNmpqDF7BE-0R_ltf4TSbxCyzKz0Cc2w_zxsPEWjpSNFADCOFmf0HvCVr3TTDh49DNUTUtn7wGfVRJr-bF3Mj3R3k3UZPCQ_lMAI8EOE7xukngSlo8y-vM31EIaq8e14f6LOO70q4gnP1_kOHu_6EmgXZVXcVlgtVX1OQIDyKWKZfl2stm4GRrjHvl4eupZP3-r3LQZtnG7YNqjrf9rpnETKveVRU0b_Z0Ln8B_Txq4xQyqO6_7rU_E3iBIHC3Pv3V8ytur6Ak5NOH4g_6_NwWSai2TrJq4RTGqgRUzY-biXuUL7zC8FqYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=EIVowVQPs6NHWL0rOKg5zL3RRmFi9IRNmpqDF7BE-0R_ltf4TSbxCyzKz0Cc2w_zxsPEWjpSNFADCOFmf0HvCVr3TTDh49DNUTUtn7wGfVRJr-bF3Mj3R3k3UZPCQ_lMAI8EOE7xukngSlo8y-vM31EIaq8e14f6LOO70q4gnP1_kOHu_6EmgXZVXcVlgtVX1OQIDyKWKZfl2stm4GRrjHvl4eupZP3-r3LQZtnG7YNqjrf9rpnETKveVRU0b_Z0Ln8B_Txq4xQyqO6_7rU_E3iBIHC3Pv3V8ytur6Ak5NOH4g_6_NwWSai2TrJq4RTGqgRUzY-biXuUL7zC8FqYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکراری ترین صحنه دو سال اخیر تقابل یامال و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/100196" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100195">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇪🇸
کری‌خوانی دلافوئنته سرمربی اسپانیا: امروز مقابل یکی از بهترین تیم‌های جهان بازی کردیم هرچند حریف مقابل بهترین تیم جهان شکست خورد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100195" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
