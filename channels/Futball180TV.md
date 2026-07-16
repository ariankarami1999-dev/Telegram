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
<p>@Futball180TV • 👥 572K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 04:26:11</div>
<hr>

<div class="tg-post" id="msg-100451">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=Gh1Z28KTCUByzDomyMOmtfY_aSzRX3h7_8xBnTDReFRT1CeouyZ_Va5mr_8srHeoS9gLrD1Mag445O4DGV0ipF1rX0757PgKvoXS2VkBiXQ2_EA9_Q3JLBvYR-l4ZExRMOLNIxaHUxA3e8LoUocFyx4LScbXshKn8Kc6xZO1nPr3tyNW0c3onc8URXtPdg-EfWXtlNE69pmaWE0uiEr8v4KW53uKz6H4hIqkSzq-hUy1yaAmSyUDOSZCb2eMPmx0AQROCnknXYonPfCMOOs1nGhuoZXAcHk7RVt8w_Hz-HYrFC5QdKfsM2t6umAdS9H3rkhB6yhy_g4zp2Y7ntCHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=Gh1Z28KTCUByzDomyMOmtfY_aSzRX3h7_8xBnTDReFRT1CeouyZ_Va5mr_8srHeoS9gLrD1Mag445O4DGV0ipF1rX0757PgKvoXS2VkBiXQ2_EA9_Q3JLBvYR-l4ZExRMOLNIxaHUxA3e8LoUocFyx4LScbXshKn8Kc6xZO1nPr3tyNW0c3onc8URXtPdg-EfWXtlNE69pmaWE0uiEr8v4KW53uKz6H4hIqkSzq-hUy1yaAmSyUDOSZCb2eMPmx0AQROCnknXYonPfCMOOs1nGhuoZXAcHk7RVt8w_Hz-HYrFC5QdKfsM2t6umAdS9H3rkhB6yhy_g4zp2Y7ntCHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فینال جام جهانی 2026: اسپانیا-آرژانتین.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/100451" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100450">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVca1GuB-D1bUfWDFnseCTfRxEVH3T_0R9XhXiWVew2Xt3Z-5prR__2LhFp0ppDjGFTCL6If_QfJREPgvsCdNTbzphTGc0OgDweo9_UYc2_qnM62i7mNkX6yNkOtY4PwgPzyOqTsZPoBLTblQSFgYs-YGvlEQkOup_6r38QT8C0zWA7V0yCcmH5tQPRA3hozYQpupeY21Chx-lXIVu7wzyQCPgbUxslXKFFjUxRWlwE7aK7VywQJ0GL4yuDt5kuP6eVoT_NqdxJn1WX4ommO5h11kqHZGlgji8Xv74b4rayCeAtg3ENWGxLMTrUB6M9lKhnkLMxvXM2jIaoH9D6HlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
عملکرد لیونل‌مسی در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/100450" target="_blank">📅 03:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100448">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llCwU2g7TMoUdUmdhy-5HDGzZtuQ4LtoXswgW9bLMiiQTQ_ZzJbb2NVC20KAqL_b_5lD3RBiG0pfVr3UwxPGRwgp2TdKqsZzIsnT7P_XE8C5QyiSKdgskhb3r7s5I5VHRnuBU-uun1ioFL2sFGd49kVt2OKixxRcDHneZUhzAUdGxgNECqS-l6u7aWmrLDUQoW2vjn2uWq5E9y076yw-t_WtnhgLuzFdSZ-lgeXbJgd3sqSSkUKq_vhVWp0pFuULkpoLhWIJm0EgpD6Fzg27qUFCMw5hQVovMyDLIh09300o5QxBsC6dFXh5wIi2nr30WS2KkJBTRap788JkK15-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا ممکن است تیم ملی آرژانتین را پس از برافراشتن بنری با عنوان جزایر مالویناس (فالکلند) متعلق به آرژانتین است جریمه کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/100448" target="_blank">📅 02:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100447">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=gandeb1C6JhM_U9z54mSm9AOMBBbXN6nnVw4FPXQ6UMD5SEV1Vkt872GQrjdrmLOqfQCyQdSH4CfG1Hi8dkx68tlOe4Gb-rcpszstOn5a3-JgPv4qJ5DYo9ZUohfiWYW0pT6jPWGgwB1ekths7oqTOVHXhpMt-MwAOAfQWQxaRYfpobMIwXuEZlQNmPN7wGbC6ZdL7l9CzMnFRoqZ8Qr1DIRs14ETkhEyMqJIrhP0g3yGAAtkg5p3Xcdz9maxQaMYuHvwgdB3p7oC4tgXoyXK91WXrK3rD4yhWs9xXD0FhafK1nO9rsU7XPw3ktVCBHXWhZlcPA5ddWOLNOtj_8WNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=gandeb1C6JhM_U9z54mSm9AOMBBbXN6nnVw4FPXQ6UMD5SEV1Vkt872GQrjdrmLOqfQCyQdSH4CfG1Hi8dkx68tlOe4Gb-rcpszstOn5a3-JgPv4qJ5DYo9ZUohfiWYW0pT6jPWGgwB1ekths7oqTOVHXhpMt-MwAOAfQWQxaRYfpobMIwXuEZlQNmPN7wGbC6ZdL7l9CzMnFRoqZ8Qr1DIRs14ETkhEyMqJIrhP0g3yGAAtkg5p3Xcdz9maxQaMYuHvwgdB3p7oC4tgXoyXK91WXrK3rD4yhWs9xXD0FhafK1nO9rsU7XPw3ktVCBHXWhZlcPA5ddWOLNOtj_8WNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری اکت توخل و اسکالونی بعد از گل دوم آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/100447" target="_blank">📅 02:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100446">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=cknfvziZZBTlRGl_4oAovrLTxureS6cPnj2RVcZhE9_1zSBBZY3otgkm_KS9LJtoV-sm25npLfiLyYtWDHlNrVKpYf89JiShRz2hbNpxCJqcHd9iC3FiutXjLcNBygyhbvOUV6q-xQHTT0r_rhWkdRJRewh6Pss-313FMtDvXk6jbCgeZccJgLvecZb0pFVVdED2KIV8APC_2i6wKBMV7Gtr0ldpnnHaNYXr2-s2Jf-tOkF8eVVJY3-8cqwmeqMVRmrh6JMK9TIn2imb91Jge63vNYckb3qOmhKpI2NMO92j4sCpEle58K7JNuZKIQqNX81k_RrvKxShlX5uuVAA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=cknfvziZZBTlRGl_4oAovrLTxureS6cPnj2RVcZhE9_1zSBBZY3otgkm_KS9LJtoV-sm25npLfiLyYtWDHlNrVKpYf89JiShRz2hbNpxCJqcHd9iC3FiutXjLcNBygyhbvOUV6q-xQHTT0r_rhWkdRJRewh6Pss-313FMtDvXk6jbCgeZccJgLvecZb0pFVVdED2KIV8APC_2i6wKBMV7Gtr0ldpnnHaNYXr2-s2Jf-tOkF8eVVJY3-8cqwmeqMVRmrh6JMK9TIn2imb91Jge63vNYckb3qOmhKpI2NMO92j4sCpEle58K7JNuZKIQqNX81k_RrvKxShlX5uuVAA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل کل مسی و بلینگهام
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/100446" target="_blank">📅 02:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100445">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYfg2bQTPd0603UWT1jLMdIliv8GmF2ky58c476nuU34IC9al9ut6X5AoSR6ffDIFVxYx5EgT2FQ2yQzMdro54_qzaWArrcNyk7vOAJcbmBi4SGrYzgvmhoM3GsO2WcGmZLNEIt9WQnPVG0hHCnkCarHw_E7d3cph6Wm283wpEad4Dp2FVrnAUWT_tM80X7mm3SRfIY96cc4mTTzfWwzpFDBc1jA3cxPB65gXBJHpOAgtF_EjNM11Hv9U8Qx8WoPO5ZZrJCH9sLlqOfn_ikLC5vxpQ-dbbCjzDF-syWSjtNVvxH6BsHs_ZmQ_u1JeGQjpDRJkFZLqgXWmv5Wul90QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لائوتارو پس از به ثمر رساندن گل، نام مسی را که روی پیراهن او نوشته شده بود، بوسید.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/Futball180TV/100445" target="_blank">📅 02:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100444">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDtmvp_2gj-AUnn0Gj8AG9Qb6PoQjXz0-D7RJIdH_byb9LBHYBBK82JyXD9oFIBj1F65ysn6sYlCjs4Fl-8fKc94eQ0H6YGPh4YTiu0VrQJk-i_6jSWzQT3A1ttmlLK7l8NQNJlYkXW1KGyKYNHH8dgVl1BKBIEJtaVU1A1M1ZqIvFnvgG691fa0lksKKBrLkf7ml3AVKlqZehOE-HHPP1Wu1vwJbRRlGujujq4yn492956hv3xJ847l8QMRAbLfNHM3TJqMAoEXkyGLAbCnR_afR_2cyBENV_phEwESEcBIv5vDs9rnByFSedw56LOqmo7afDZXrroxhNlViacJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی:
این جام جهانی دیوانه کننده است و رسیدن دوباره به فینال باورنکردنی است. من به آرژانتینی ها در قطر گفتم: خوش بگذرانید، این تیم هرگز ناامید نمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/Futball180TV/100444" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100441">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBW0EMK8o30YPk1LaFp9I46jgnBR9qO1w8t1-pWrBRg1BKUeD-ULRY9GkLh2-kmyAahApCfNoaC07lzacE6tIzpO3YjQFENLsZXF4ycasbCEfU0IqH0DjLtlrllBmBWJ64rTytsb77vNBgNaIxcUQXtZ1MFuliQpTFSq0AlNMj7JsY-O55qRcNIDdxSOOAuoIb5pbVQEJ5WTN1QVmn12m9_lq1s-zFG_GaAOZZbT2ZKlqgJWh1h0h-exQEGLYg2fl8ZmMigLtC0cj_tx621hU95uy5ZP4ZTV7TwlZ3GT4lna9Tee7nf8wbmEpQIH7coG27mX0mPf3649NWSnGi4HNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mo2TBExmq9YWLHkLQvW7jBM5HCjJvf5PoXOUcUD3vlTm5v01MBQzAPMFWrlb2HKOc1uqBFFQOKsd0mv3lMjirZSaewnmoV8vK_3nzn9Bcz4RvIS-IInbyu2bbFY_mH7L1TY4mXo25JRdwzWzamOgKrM2aWph9kZOMSAdqBmPDi_x9AxnG5DBRVVPtfl5RDAxYhwIAOK_doVoPL6xLnHQKFOJHLQ100HvWKkTO0OJmsePw07mq4Rd_K_8W3SWt0CLcAdKJIfpex-MDGyAS_0uKQRiV3-j_bz6CbRQs3p9WGdoSYQ4YcvEOJ_QiBbem5XrmkOCj57VIkeApKPn_M97Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbDyv5f9UHQHGMMbHlf8N-3L2-Kya4XBPGGxL_z39jMsq987Ipzl92g48IEDmdpOlPBiKzswwBh2_F9K5BGEaVeuf5JGJWGVzW7KbE5gkOJ227tNRSpYPJy0qU8jPNEMlUKPeJXJrlzhpyesN1_a9t9HEkvHdlpASWmEdg8SPRJlnkFUXyVTuRZt8BXz9HZE14r3eFKSGPkEhbqCJHnVJz-095rhOS_PCnFfel7hC1CKjAVlcgetlYTee9V8Euc9MKHB-099xQyV1ru_HG2zbaNKvPfe1YLGT5yDWa1CcYwVzrYaS_871UKV-d3sbcftXEYSfZwpezv5bYXZjy8aDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🐐
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/100441" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100440">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqstjDIUolHjl3kuzszg_7QxNI6BbwhhE6g-x1suRaLRhaV1AB_ueuGpCFtVmdM9cpiC4wKJ_0RIZoPjlmdeCSdPaaM1oqb-qKl1_1zjY9aGMyjtG7Td9R58tAjZg6BDJ7IHnRPr9BP2vuzE2l22XK15r7g1IF1rWyUATV6UAPo1ccwsu6r53AlPJU0qz9xXQMdBLd2AuWpErvzeQvwfh53SmuxZU8SR3Jz6hRlile-iLpKNhqfwF1a1Nxwj0-fL8xm3wlD4uhGL7gEPfrHdxdBfPxb9F_JQ1Jn24peqtqAjhy7eq2WVfCM5yi3j7AvPW-r5YJo6ojR8vSELbs-o4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اسطوره لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/100440" target="_blank">📅 02:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100439">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135c24c050.mp4?token=adSu5oopaAthiuM9_3DsfY8AI8arKBZtqFPN5j1f-8p3KxuZmp_ZEAm-4Nee3NUqYrQEVVDH5E4UEOgTXBGVsIvEe97uJ4BxprDk4jsBPGDOomaKp3M4RZoXsXdHEbIt3GjscCPDdd2ortyrP9fC0Cp31cPZ1oaEOihGeZhMHEtXlvwPIFbgjqixjhTEQIR7IrS3FfAWUxz-Hvi2X3frRlCBG94uV32Xj7lombWjftKTR9a7wPOdjOGiLSCog3Hqr98e3OKmY97XwZXfBv9RVyzqKbtUjKXiwGfcNvX7vBwUla0jyVLjRrGCEDe4B4R6domQVTiL0wwAcY3kuHRAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135c24c050.mp4?token=adSu5oopaAthiuM9_3DsfY8AI8arKBZtqFPN5j1f-8p3KxuZmp_ZEAm-4Nee3NUqYrQEVVDH5E4UEOgTXBGVsIvEe97uJ4BxprDk4jsBPGDOomaKp3M4RZoXsXdHEbIt3GjscCPDdd2ortyrP9fC0Cp31cPZ1oaEOihGeZhMHEtXlvwPIFbgjqixjhTEQIR7IrS3FfAWUxz-Hvi2X3frRlCBG94uV32Xj7lombWjftKTR9a7wPOdjOGiLSCog3Hqr98e3OKmY97XwZXfBv9RVyzqKbtUjKXiwGfcNvX7vBwUla0jyVLjRrGCEDe4B4R6domQVTiL0wwAcY3kuHRAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
شادی آرژانتینی‌ها با رهبری لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/Futball180TV/100439" target="_blank">📅 02:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100438">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubFQzRH5ZAcNpjX03beelrUexG5q7CzVbDgyae9mGH7X47SHIhpnHvYqy2Eyl6T4aC9GMRGB6GrDDKuljCXAUZenzZE97JauKWfNpi77ve2popP77vBAwsThSmkNGFmJ7d0J2XOb85Voshn5ZWadDWqMEdAZtTnqIbk-ouFZjRIvV31RTsxjEZ5n02ytFSzFZIvtcjy3ROjgE4JJkxZ0MmXi-hhECS9b5PB61FI6PPlUDYToCx0ZxUrT2_WgzdEgVOf8l77FfAyCgDb53bu_RnVqg46PxU_CwgUOUWE4y0hkAa4Gk-MYh3HDT1-ogC96hlHcMnEhz823nCXuxNo1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی و کافو تنها بازیکنانی هستند که در سه فینال جام جهانی شرکت کرده اند.
کافو: 1994، 1998 و 2002
مسی: 2014 ، 2022 و 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/100438" target="_blank">📅 02:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100437">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e27d580c5.mp4?token=pL_nfPI34CkTujFrFKegEukZk63tWPyohNXfq-VXs9pZGjXaWYFQXG6d-cBRa42KZjcxUAqA6R8GlrstuvCQEd0SGUMweL_8ANxOHil3f2aoDyyCE2VZBVAyY6V-J80RmpreXSJqD8Bh2fNOK-d5MIrI-DIreb1t3rKAmtCCsvzmox51So_7yBiOMgRMlucXeHHQXDMdL-5275KeY1GSapZZVyz3PsJsw0GsmOG31HlSebNNC4ilzeLdqjTtmvoKI9XiDFGJMLWqFwIP5ih6PBgQJhZlJHk-Ns7X40lRVtToWZONYXljyRP3sqK4c_gY2cUdnHA-URVR4-js0zA6XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e27d580c5.mp4?token=pL_nfPI34CkTujFrFKegEukZk63tWPyohNXfq-VXs9pZGjXaWYFQXG6d-cBRa42KZjcxUAqA6R8GlrstuvCQEd0SGUMweL_8ANxOHil3f2aoDyyCE2VZBVAyY6V-J80RmpreXSJqD8Bh2fNOK-d5MIrI-DIreb1t3rKAmtCCsvzmox51So_7yBiOMgRMlucXeHHQXDMdL-5275KeY1GSapZZVyz3PsJsw0GsmOG31HlSebNNC4ilzeLdqjTtmvoKI9XiDFGJMLWqFwIP5ih6PBgQJhZlJHk-Ns7X40lRVtToWZONYXljyRP3sqK4c_gY2cUdnHA-URVR4-js0zA6XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
حرکت زشت و عجیب بلینگهام بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100437" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100436">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎙
اسکالونی:
ما برای پیروزی به فینال می رویم و برای قهرمانی در جام جهانی تلاش خواهیم کرد.
هیچ کلمه ای برای توصیف بازیکنانم پیدا نمیکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/100436" target="_blank">📅 01:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100435">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9481ccab4.mp4?token=KKGDN6mzMngirVYk0nVwfWjkVKdUMcI3LWcpTzNNrb9ehtpcYeFXsvlFZRyCtRZRmmhdvFcsGBCkS2m66ZcsEmXWEkt3sxSmcLnyWJOv_TuZovDdVhbwm-Nr59TCavWkyevYlgKMvwlJRoSfGJx96JQYWo41VUrf69JmGth75ddvfUQ3XlweC1k717yn26Lk_HVSvPn6nIKG1s1fIaPJIcEAONjtGy3ioS2luEUOucPrCKbDehh0AGaxCnyiys2imd8ZrwXjYgO7QvLtxvu2KdjlaV9LptxGKuAXzknBS2oXOMkhR1Y-WR4aLehfNwO59HNdqNZfghPX2YxcMC6AIEVuKkaDMb4snUzk8zDuIc1lR_dyGTjjuSv5NtOM0eqCG_LwSoQZ3yoTXvViOk-bde0B-66wFBIj3nh_uhROqWS1Q3U0YzBN2RYA8uC_WP3-Rw3WngGqK-yvhJtBF95aOM5n3n5-7tuH67MgcF90N1_-oRmeX0VhhY9NHCZ7KXZkKJxZ-hFa5m9b3ju0Fq2r9blLpRrIrQwJAmHyc86xlpRNpOdJXSIrFfVv0CxOOVT-3Mngph3qZzbkQOuyoQkFBjVWa6lOWGqIL8Ud7SX5bds4pzwW0-tOJ0SuZvzN2waqbn7_4ViXPgxozr7i8qMGJAeSW0lGcnK6iuKIra37XeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9481ccab4.mp4?token=KKGDN6mzMngirVYk0nVwfWjkVKdUMcI3LWcpTzNNrb9ehtpcYeFXsvlFZRyCtRZRmmhdvFcsGBCkS2m66ZcsEmXWEkt3sxSmcLnyWJOv_TuZovDdVhbwm-Nr59TCavWkyevYlgKMvwlJRoSfGJx96JQYWo41VUrf69JmGth75ddvfUQ3XlweC1k717yn26Lk_HVSvPn6nIKG1s1fIaPJIcEAONjtGy3ioS2luEUOucPrCKbDehh0AGaxCnyiys2imd8ZrwXjYgO7QvLtxvu2KdjlaV9LptxGKuAXzknBS2oXOMkhR1Y-WR4aLehfNwO59HNdqNZfghPX2YxcMC6AIEVuKkaDMb4snUzk8zDuIc1lR_dyGTjjuSv5NtOM0eqCG_LwSoQZ3yoTXvViOk-bde0B-66wFBIj3nh_uhROqWS1Q3U0YzBN2RYA8uC_WP3-Rw3WngGqK-yvhJtBF95aOM5n3n5-7tuH67MgcF90N1_-oRmeX0VhhY9NHCZ7KXZkKJxZ-hFa5m9b3ju0Fq2r9blLpRrIrQwJAmHyc86xlpRNpOdJXSIrFfVv0CxOOVT-3Mngph3qZzbkQOuyoQkFBjVWa6lOWGqIL8Ud7SX5bds4pzwW0-tOJ0SuZvzN2waqbn7_4ViXPgxozr7i8qMGJAeSW0lGcnK6iuKIra37XeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇦🇷
🤯
کسخل شدن گزارشگر آرژانتینی پس از گل لائوتارو مارتینز به انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100435" target="_blank">📅 01:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100434">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEPRntvfaBjUTkO53xbjhe7X_FsxnmWakF7iiSUV2tQhbI7MWLiu3rJcf7fpuOZ4log-P21_CPNg3144RzZQizsVFniq1S15gOcYroEw_RhyI1jHcw-Unoqhv26AHzad67PuQdI4qaNLPar3WnaNwOQbd8DXnXhJACKZI8QqmDRfICTbR5sG7CO-3GUzNlk9nhHPPNgPmrYAdRqqBlh4dRrRS9rVKGTkDSRWgB9NTqED9EJaQwsxsSqDj8V2wbdA1hhuV6O4c0AvBwzTCk7mbQU__CP4e7uVs1MeIcqFWcV9uM2CpXtNkuhlDKjU2WpOQosSt45msaF_i_6tsQQdZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ‌هالند بعد برد آرژانتین
😂
😂
🔥
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100434" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4tCtIgF3acV78bYt9wGmLL4DZ-5UhWCuck1x8ILUBruIHOHr2XNHIzSkJxKB8jpoSRGsLVmiV9YUgE_-OiVasKUxXTqmU7zqp1eQ208EzTJ3781w0-QrkRp_4LT_3i6QJDvSat-1K5a-kIa1t2C7wFCUd8bZAazf5gxWj4ATkrXiF_D5feMSZBk-RgfYXPMOwGCBPuXWeIg9cC3PAKYPU-1gRe4i_8itRmSPJJyo6W-zZSPnpaAhV2o8IHHS3h412iTMVSABkBoszjMy6aanXiWbqgvpONRyYNn9v52gIIHxBL5yA-FUfQrX63pXMwGQMcMRdba3CXMR8nIjLaMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
خایه‌مالی سنگین گوردون برای بارساییا
:
سال‌هاست که شاهد تأثیرگذاری لئو مسی برای بارسلونا هستم و امروز متوجه شدم که او حتی از آنچه فکر می‌کردم هم بهتر است. از حذف ناامید هستم، اما می‌دانم که حداقل جام جهانی را کسی خواهد برد که دیوانه‌وار بارسلونا را دوست دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100433" target="_blank">📅 01:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100432">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=CluqlbZ10dkIp0sjhch4CFLnN1rdIhGmqG2yLu4cZVaADnLmL7FRzaZiM01HLCVnVvlC4g2a9Ty_NvwJ7Lfx09tEwWPxEYP1Ewr-xPGo-6m3WXbnIimoiQlrgbl_jYksFR42OsTEpjOOOhp_EsOsoNIhP5uYPIRrSTQcENv9npGRa2AoX1lFtifanvwi2-OJzjRZdl7aaSkcGo0yDODrWcpqEH1bRPtUyMWIVVZGWFgSqNT54yQ-DlezLNdhrZNVTHpphoagWpRkOwN-EfJzhnUPvcBIl-is0t7C9IA7oJDhPhHAAMpL00TzzTtALq7wxklnSMMsNeTF-JL8BimRCVME8Ys-RJnvQajjr4P25m60WFFgaavyZOYbozGy-Y1P6zaYq4IcpgDw7Pdye3XuTB32N1b318QI5sD6s917M5gpHwwbhZFoyjHGzDQ761L7mHkR2EKN6Hax9P14Mxa6TCjNLh0-u1-NXD2JIlPAI0KJiNIaZWxRK8NWpSiv8M4nr3KA0TVnMpEwUySTIaAUrOylEX5ZVnfwDPnqWqWLWmOqBQfda-m5BjmqloqzcyBmte8Wv2BQk2zIEItFWsul1Lx7nxpoeBTaj9rZQS1KADRsqe4gl6svqJmz10FeINivlCMFv2wjNAlxC_isRAlRpv8_Tdgor4iaKDC0pv46qbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=CluqlbZ10dkIp0sjhch4CFLnN1rdIhGmqG2yLu4cZVaADnLmL7FRzaZiM01HLCVnVvlC4g2a9Ty_NvwJ7Lfx09tEwWPxEYP1Ewr-xPGo-6m3WXbnIimoiQlrgbl_jYksFR42OsTEpjOOOhp_EsOsoNIhP5uYPIRrSTQcENv9npGRa2AoX1lFtifanvwi2-OJzjRZdl7aaSkcGo0yDODrWcpqEH1bRPtUyMWIVVZGWFgSqNT54yQ-DlezLNdhrZNVTHpphoagWpRkOwN-EfJzhnUPvcBIl-is0t7C9IA7oJDhPhHAAMpL00TzzTtALq7wxklnSMMsNeTF-JL8BimRCVME8Ys-RJnvQajjr4P25m60WFFgaavyZOYbozGy-Y1P6zaYq4IcpgDw7Pdye3XuTB32N1b318QI5sD6s917M5gpHwwbhZFoyjHGzDQ761L7mHkR2EKN6Hax9P14Mxa6TCjNLh0-u1-NXD2JIlPAI0KJiNIaZWxRK8NWpSiv8M4nr3KA0TVnMpEwUySTIaAUrOylEX5ZVnfwDPnqWqWLWmOqBQfda-m5BjmqloqzcyBmte8Wv2BQk2zIEItFWsul1Lx7nxpoeBTaj9rZQS1KADRsqe4gl6svqJmz10FeINivlCMFv2wjNAlxC_isRAlRpv8_Tdgor4iaKDC0pv46qbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جو فوق‌العاده رختکن آرژانتین
🔥
🔥
🔥
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100432" target="_blank">📅 01:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100431">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شب خوش رئالی
😐</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/100431" target="_blank">📅 01:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100430">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6D5lDKmxzBUzZeBHhI7w3n_8Xqi4uLJs_ubYuRrCOt7bB9uV8lyWTB6TJgR5qr9YI_9DwdDLwJb_eRsp1bXvbecTNX-WH5TttE3q7g1qae0aEDbYNZmGWYqOwPdpxR1dgci9q8WZToJu2Y7U5FT2InXF_jCwJmuMQiTlh26m57oMK3EPCD8_QfPaJorH2Md0s4YnXxv9CqazUpBKDrfpYRrM9Qa3j2tnWRLHy1gTAnzDWu1a8WPvJQVVE6wFp_D38FUVw1VedR94JaM5d_MRqdFfRqtzPwPgJquRSenbFQ5RJlvMBoUVgHuKOVbFV2pJ6UFEd9dDgAwlxE_SI4h7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
هری کین: مسی یکی از بهترین بازیکنان جهان است. ما سعی کردیم تا حد ممکن جلوی او را بگیریم، اما وقتی توپ به او می‌رسد، حس می‌کنید که انگار دوباره به زندگی برمی‌گردد.
😮‍💨
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100430" target="_blank">📅 01:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100429">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbN5kaa-jhSBRMWiC6hfIxpE1doSSsWYPcrOGSWstuzo8XfzJaN2AITzpeTj_LA8a9P1JTWfJaJuPJVL0zFknqvcHVHW5fJ2qBZ18CjzZQOaChoBaOiyWm5uJUXJw5mSxVsoDOSSqMduEXGf_mneIOYqyNYK1xaWV0ym-i2CgQzpqULgF1VIWv2BPNQc1EblvuQAxlar6g0UbSZKBST9LBFQ1slY2SqRpH3zU6AlcvKpQWuJQ-3_cLX0PZl0EqPC3GU-3yDOQcewzvxEdxXkTtP6rgsq_tIHR0BNhb4otxvWkvmC_4ABRVPwFt1v0f_guNq5TVP2mR62Lwfp943A2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇦🇷
طبق آمار اپتا، احتمال پیروزی آرژانتین قبل از گل انزو فرناندز، 1.3 درصد بود.
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100429" target="_blank">📅 01:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100428">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqbFiU0jETubyqx2EhM6b0SkxJsDEews3gyCJ2FzPyccnJL1tD5OskY3udPFgkon-OS2MksNc_W7MRHwg-bpbsqgBRuxv8V0RmU93vPye79Bm5S_huR52kRTM09IirOp1wdx9qpjwPLGlufueFsHAH-6oJkUQgQFwwq3Ju8lneuJElPBBrS3jhLhQVw2FBft00CQvcR7S4Z_lz1n-_WdjSzJJTz_Pblkw3T254mmRlj8fot8hkaAEC5brZKbX4i7vV6wV48BxQCUBRBmIy_jf_5qHFrEmODIEo75jQwgMm0Z_wLCSmf-l3npSHBsRXvhcQOW9kcqu25fQMjVvytpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
😐
🤯
کاربری ۵ سال پیش پیش‌بینی کرده فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا سه بر دو به سود آلبی‌سلسته تمام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100428" target="_blank">📅 01:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100427">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7oVgZvWSwawPe4USKH5IGkfLkuyJJEgFpIskl3NQtiUyFyn6i-4g0CN4EArR3s2r5Wb8kcpAg4aUduwoQKEcm54Z40aphTAiJF2Hp2PdRVDIva-kSVeYVJEMgiz_dVTk0_3O8HUw7egrnsvC3TuxB4qi6KCiDBas1YRiN-nBs-TXCsTTYwVdzszL6zMl0bNKEP22E9XzZ3FpK3Pc0y3aqsqvejbyJgLGxZmQa-z9NYaZeaiwJUioMtxLgAUuCRJoY-FQxZrjWIEnb3_oPht2j3WP8uk8WxTGKzU7ZMgNnAiVOCA7epA8b5MwGmIar3ccEctwkIXAwJbyaIY7eiRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
MOTM
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100427" target="_blank">📅 01:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100426">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvDWsCvi0GeFa81-zvGauvh2CFuH8DqDa3EuTHtgkmAE7ASPD3Kt9OTKOZSbMhVFDcmCUh5_zN7MAt5VNFeBPNq6SsR5iD0Cxcbxmun-PsxHXpLddbEmGa9-HNI4FxDUp9Upfrrr7Ies88bWQJl_x5b6c1-SvueOQbQLUORMafZGKFsnB92X5A_pYY56Cn-YhEjq0dJleiUH_H3AtZ7ypkRcBFHZNIutsBU7fgfMYzvprAH1CsCCbCyJcIaZxySkx8dTt5JXJ8UPjMmkKmXVWJE2_DBpSUvQ28ri477sQLfTF9NpHWnAyzwdDiwa4hkayNM83SLsVhceVYWJAo0lLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری کین:
قلبم خیلی شکسته. تیم بعد از اینکه جلو افتاد، خیلی عقب‌نشینی کرد. نباید اینکارو میکردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100426" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100425">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTomG6MnLF9E8N_wVrfdiM7CpwdVRfjk39iTjmtIueFH8P4xZRu9YVZJ2GpZEvM2GTQj7rHqBRIrZoC0j7F8q73b5YkOBJvSiXLzaWYj0Tah3Cx2mhyUM87e-zwFAuYSlEjV61Oj4JOS0QqHC3_n3-w0kaoRtgCkF1e9a1H30Kn-BCIxxrbbPj_H3NmfDUdgW5PcCQuyowMSFbFoIv4ra5fDdpd7zkxkzKuUXnaFWF-fyapmPiiTZjemIv__-n0qJZADidYx5BXr-99Ht_qFptK8HmAHMmNOP2MxFZ_GzKRz9kwMT_Qzc4JIvedstEXPI-od8USk-MYQT6MKk5M3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: قبل از بازی به صراحت گفتم که لیونل‌مسی یک قاتل بی‌نظیر در زمین است و از او باید بترسیم. او در این سن توانایی خود را به نحو احسن ارائه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100425" target="_blank">📅 01:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100424">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKnpb9BpInNWJBR47pH4E_c5SnQzh8tqAOlL43-ZWjmGzahVxkHdPkbN0kWSlawJ2npvx_uvxYXjsUP7mrJCdsFBVv3r1cpIXX7vtfkTznhmv2TuRGaabftlhXQcM55Q_DwfVXgMC6CPe7vV0ump_4ZwihjZv2MMCbu1ZS9VJ6yEr7Qwxg6i0emXRyi9toK01nra2FKSmmcqgY7UshR_ipoxILkGTbZVXVFR10Ps_g24dQxxg1JXEgsHYNSHSUGXZXAXjcC6DExc-mpijr_W6wSEHJ-8Nzj3lFZT1miM-GK59Fsx0CuZ7u8rQP7R6NHTvNQnNs0tGi2jLeHgt_dtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
اسطوره، مسی، تا به امروز، بیشترین تعداد دریبل موفق را در جام جهانی داشته است: 24 دریبل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100424" target="_blank">📅 01:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100423">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY2rqQQyKQY6m6YuhBHiS1DajfASQz3iqFyC-324GfkemordZvocZA7IXJnHU6s9x3m2BKveJRDghKnshIQS8-3Iq0o3mmb4_QhkeZMe8lKtnj0YAcbNf8_8cHi0q5fHNretVfJxaZbwHwkLC6iWEIxkkuNb7QrWo269zuFOSR44NaVELBUeukcv5VQOG1c0nfIiZRKHxb2M0DXcfyDqkzr2p9dds1A_-mKKU4JEaGIgm_ka2tX4LO031UUGVTdGKGgCz2oaJu9GQviTIfqeDl4W7WpE2dZPPSAuDgeO2KGEvkvMK0IKc37cWsY6haSdhN_WfM98AKgM5tBevoQ40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: شدیدا ناراحتم. نمیدونم چی بگم. بازی ضعیفی بعد گل اول ارائه دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100423" target="_blank">📅 01:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100422">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgKfdl6K7PLl1dqjq5wEsMR5HEbKIM11ebblQ5ntfmU9GnTOZHPE9uJ3TNIPGhjR19luWW0s8Ks3polMT1IB6-hq0BW2Q-Tz7I6ZQfEsyZmq951fH1NsXkRUUmpz6XIcKxwRlqFlIHi4Jrj4Ng3xoq2688LdkyWiqi8QKYgz2XPloAOyhbj-DEKC1SBPwVg6avMR0St-ty6YwOCu69yusZ6GEVC2gHBCUiKcFy7ItRq25v1_0UDZiOPpHnLe6CCuAFVfI5cwrlSOTEnbPAR2NNpDTVD4tJnYPGEMX2pth1jhHQqiwzVqxutN-foWTJ7lh5LEff0MMJ3N8avruMDMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100422" target="_blank">📅 01:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100421">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC6JV48_V9nx3ngVXp6w5v75Jl3IuvUkDm_-Pvk46fBvRuQwyzFfaTc-bxammeb20Zbw0KY3NdwL-9j4bWy-z3_7cW9IjojQ3pdO-So-C4arSqX3cNLfFdc_15OEYyAJJMlkWKUOPuYUn3dBM7OsLxSHGAQqOB8M0iYBHxJcHqRWEjs61imfzonxEI7crsNmpK7lj90gbuK83VY73LoS3-I18ICKyqaQU56OtgHxgTs92XDlo2kGcFB7UesWdF68dTYcmP82MpPpIydHXl9FqYzZeBEErAgKmjXuL38F-NN_6M3Qb7i-LGr7XsONTz3V0OBh_48fGxoQ_e-BSEiw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
⚽️
پست جالب DAZN: ‏بعضی داستان‌ها تغییر نمی‌کنند، فقط قهرمان داستان عوض می‌شود.
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100421" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100420">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDtW3lOiYAiUTqsIW0CL9gKptn3AsrZCgSb11nfIxc9QRsbdRk2eGSsOJ9XFZIA9qBWzXJm5KaBQrtDC5MHU8JQjv9xnmpJH0ge2961gsefG2q2JMQ996I-ggznLWMR8Vr0i0RT4s7WVkouECpLJEmtJGUWE4Yt2euzrwIxM3h75LdB4RAIwJtt3o4KS6B9TyeXSCTuDA7i-Ag5govPrZ31QlvaMdgZsSRRccwtUnKJ5zd7wdJJa5rFmgpyDMsm9xLi7CeHD3eSqPkrpb6EAtjUilJzCAF8h7uMTzN5CJNLi5ocU50lYh_oeZZv1hr0mEv_BsiDwsJEF0PBcXO-OIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
کلاس‌آموزشی احترام به اسطوره توسط آرژانتینی‌ها؛ کاری که پرتغالی‌های بی‌لیاقت برای CR7 انجام ندادن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100420" target="_blank">📅 01:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100419">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d365933365.mp4?token=IZiwgR-fCbEomCP_sjgw_zCRW4Uhvfkv-P9IyDYuexUINH1p5mL9Ej3TWDcrmOg8n6KUzd20a24L9iRZKRz8Zi51m9DW-nY_FvfKLCakB4fV10sG9kk6mmg0Zvm-MgfxPwN_G2_4D3H_Apl7nI-u-lsSLbyCQUf05a9m-9s3B6Q5aXHjKnSt-pirOBBKHauSJRnGicuFt118gJkHyCGKR8gKnDxJ3rOJCygxtziBgPmwyABo5y3nDovCtUFeRft6SjWylv69c0JDzTAXlX2NTzmknKoOWoSz7nvYZcFmwjmVls4SpR-6ErVJd0gTeilfflS7YZlJGYNQkpGJZ77WDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d365933365.mp4?token=IZiwgR-fCbEomCP_sjgw_zCRW4Uhvfkv-P9IyDYuexUINH1p5mL9Ej3TWDcrmOg8n6KUzd20a24L9iRZKRz8Zi51m9DW-nY_FvfKLCakB4fV10sG9kk6mmg0Zvm-MgfxPwN_G2_4D3H_Apl7nI-u-lsSLbyCQUf05a9m-9s3B6Q5aXHjKnSt-pirOBBKHauSJRnGicuFt118gJkHyCGKR8gKnDxJ3rOJCygxtziBgPmwyABo5y3nDovCtUFeRft6SjWylv69c0JDzTAXlX2NTzmknKoOWoSz7nvYZcFmwjmVls4SpR-6ErVJd0gTeilfflS7YZlJGYNQkpGJZ77WDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم این چه سمیه
😂
😂
😂
😳
😳
😳</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100419" target="_blank">📅 01:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100418">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnBHD8GjGnaxX1VP_8TZiiEeMFqiMFkETB6Tvw4bR15X17OB8JrhuLtIvN7KDnnYgJhDzWIIZxWQU_ftTAaAYgMlcL1AneCet7QeJ9hFnCiUxqYbgweat2IKMZJ2aClgQZNopYy9SibpOzewLXHgQxQtR-jNMGoBGUaTLJOZJHZh4up_vRLNZCiMRD_UQPVWsNAygqmOvIQCO8jw6vit83n7r11Z_Va9bCnbJdG6BFz-oNJHim3J0t6KPOekZKdgUxMVHdK7_7hz5Kt4SYWHhKPu9NSbVhrq821v6RqHwyriAshHKbBQ1wlRfEaPZ58QwR8WjAMtJIvR6k5CoGOnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
لیساندرو مارتینز بعد از بازی
😂
😂
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100418" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100417">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQbgjTMcRZzEVk_O81CQ83EdspRNxr1knvIaAcq0Sf95Ntu6LT4fnsmm8k-JtdNc2vMiyEh95Df7wBAB9BfVET6ND4AO9E7EiG6QT3VZ7uTXAJmqQWhqGSlcMxEQMF_T6_NdRwpAwObMyNeEaUGxko_-Xt4iOGhqhlP_fUsXzfaXeHbIEyRopezaJvxBScRPx8xjtZH13hzWUqyxtP-ED0rLKqcNkIVWSP3eBXrgJ9O4Mjm6XMBwdqOIG7OeFMHZaXSBkWOemGhR2ERdbG_4o5gAVr4xVWQ2PrDee57O-RqxyN56c9Y3p6WNP7jbIHn4c0B7uFaEawkudE1YCa8yZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو جام جهانی و 2 فینال
کسی بهش نمیپردازه ولی ایشون واقعا مفهوم آندرریتد رو برامون معنا کرده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100417" target="_blank">📅 01:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100416">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EINzOVSz3-1SR2-edH5bzND_t2KMAhcIkk8fWzxXoPAEDGXiYGWzQxiOGbVIlimsyJC0n_kn_Vq-mPBGTZdVjU4TH1sZzdh5PjHOhR85UhhblcGRlYsBOqi4EOpO5E5ONQ4pu6NoeCbB7FzxhJAXbbZBOJP4DVWCfH0HhrxFRYCumDUbC6-uA4OWcvlT5zF_I6k3d4dfAbYbh91fFLnUC-iHO6zNRYE6SPTIsCh-DyDRYTIpkSR-BiM0YwfmV2nJ_I0KGmn-3SsqIbbq1FytjhdNtha8hlQHEbaEabv3PITQP-M4pVBMDVe4_GFplKnam7JIVZOopcrr91MfpaLMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
لیونل با کسب 87.1 درصد آرا، در صدر رقابت برای توپ طلایی جام‌جهانی قرار دارد، طبق گزارش پولی مارکت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100416" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100415">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKlJDYYhNDQZL6ZlXgAd_hFw8zqQGM_fDsjldww_TX8DHRUzd8zQLik8JH1Iz3QgZLVRtZjIav8jmPk5kJaqFkS9WUvTBlWblrMEeIwUzETsHQoVkoTWdJ4VXkq-BpDVuLK6yHBRj9tqvD7rKKvQ_NonqeO0NT6aw4T3OCye-NbgQir8niXUt07qqkdQkTb-R4SbWbu1x3sxdQKfVHAtESfCRtv2TdzWUGRMkXpSCJL7Xsnh-4GZ2uSYIB4DN4DmGiT4lWUD324N09x1C4Nln6GyRFMLax9MbO3uwgUqyisRFpw7ig5L2ysTtnc3lxj1GkJxrArwf-mImHzRll7hXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک توخل بعد از اینکه انگلیس گل اولو زد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100415" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100414">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msif32d1FL4z4MmE072ZLKfJAYLzMu6Iax0q_dQ4opkGsJUkVKWevyCMsrmLz8RSfz-J8qkX-8xK6YesUH5ZKfhST7BktMEcxdf9xiqEn3sawiHZGmqKDH0W4rvWxckCQNfc5LGoAF6rlV8Br_YtrqulUyOkokUiVsdlUVWPKwzP8K_gD9ZKI1zY1CQPj7P6RkOWCU9vUfUpJJUfHrQG4R-lvRENk6ne7S1l4RD82EdkwG8xAB-pBx7NO_UfaavWlvA7Ym4l3hJGXw-14917Au4WUGQ6gIeD6xyVtxlbqVujGv-GzQHhNAVFRd8Hu-N6ZDMESR3Tj4voz4edc0XMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
ویلیام سالیبا مدافع تیم‌ملی فرانسه بدلیل مصدومیت از ناحیه کمر ۴ ماه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100414" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100413">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100413" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100412">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uuGSsuqfNqsGg6B-lRp4mRYHXU6G7bKPRVdUdPDcgfdZ-O_G5O7SCcnmqtSN1e_W-QgGTmfQ4DQxHjkNJpuhoC8QyFfZGXxyImnOe5Ua2TiizL-cYqwQl8uRLm0YryEStRVn06JaM3Wc3dChG4vhHCfoUkEJ4dlH1vJGdZhBMS8R-etoPkin3uCenNa1oiXLWLea1XmrkobeodBNWQmPT60e3bGUgkhflt8l6beFkufC8f8Y6nLWzVGP8P818c9fMXZGv4VIv5wvWJo4rKJpEBCoKrxMZbOd_Y-4Stlds6ekoO8XJ-EA1XTmMjePslhu4vY_7vZZ5WSMXZM3QaRcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100412" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100411">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
از الان بگم دوستان رئالی - بایرنی - منچستری - آرسنالی - پاریسی - بازم رئالی - وغیرررره
بازی فینال هیچ ربطی به شما نداره بهتره نبینین و‌خوابتونو حروم نکنین
مرسی از توجه تون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100411" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100410">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thivMXX_PytjF0JdFwsO-gKdcFUSwCe90qXP7V3V5kvIhWiLEqv0MCHHSnfZuo5mfn_Am0Fj64Mf0rTfjlj4Z0Zi1f6waug0WN2UiHYTI-MnFGZ1PCiOg_LxoUPclcmRW_rMNr_9VKLFrmGBmp560aS8LxH90G9vgbOqfVdPdFIgYtKquqz02Afufm2pBmNi1tPiNUq9JNjE_wCxIYmC0uY42h9757LK6RSSrurO1KbNNOEJcKZlpDWIYFmA8Snma7TOLuHPDtfEnO9N_rxwh1g_XgdLnpJI7ZFEZpK6Eb5PkJchJUJfpQqmPPKsnc8D-tMfZXAU-s0lPJLnLy2ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روباه مکار گریه کن پدرسگگگگگ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100410" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100409">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
هری‌کین: من بسیار ناراحت هستم بری بازیکنان. من بسیار ناراحت هستم برای هواداران. من بسیار ناراحت هستم برای کادر فنی.
🇬🇧
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100409" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100407">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iu-iWZie00IlCH_auiNB6qqUgK0IX7Lnt2PaqWjscNCSjq9T-U_ghG-4l9x3AZ7EFRhqbYLiNEeUde6gL_Lrbc2RpQQA8m4KatXRik_8g21RwsjGb4tygsx6PATXMTerjfyK0zcpx67jG0AGUyhNmOoaHKIWAmKbl_K7AfCSjBsl4R89mAxC6l9dPctsHs8nzJPcIPYdISZpRcvcOxFLz9j2oth8WP6jyfs-xw7gJBc__-lau23MBxOgcdYscAiX_Gwc-QVU7eGWQHn5gRAyyzYON19nZEvXTQt3i0MTOs5Ca7lFbQNT0wWQZb1PmkqaH8K5fGgDkm1JQp14ev4Knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNhrnxxL1eSHQu0W2YXzvxhjVS3n_tVc7GyKPikdGqRBiUMBnB17Yg4cbaPb2OLla2XDLRzziTn4qpMuVoAKWizDLNsBxP1qjzk2fJRsVifI9RzEhkyeoQowJAP0CJ8qjX5JsD91ajQIjFQ0RatQN5aJVSh7mr6kDlmogHGVXrBEM05JRXwexNvp4sMmdXTtQqhmsfOyg02KJPL4MPTh7F6a-fbre_bN4rl8UQNaPh3X8eYrFHc3erFikLjBR_qRMHGDH0McRGlfoyAjTq9t-AOWPkdHUJFkTPNnXnlUo9mzy4XcqAhowqFoD11iz6S7tPgDNCg5uIpvDnAvfUtu_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا بقیه هیچی، چطوری دلت اومد یه کاری کنی دوا لیپا ناراحت بشه توخل احمق؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100407" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100406">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z81Zglbdx8MonZIpk9VJ8sLp1nkyJKoPEW4QLJRjW6CdVycjUbf21KlHZusA9hJcrc3qHd3RWQrCeZWSapyAHlp5uziZDnynOZiiINX_ia6yWOt0rVV-DiS8Ld__EXT_FfVY-Zsl-nN1Hj5W1lkLBzPsb-uExmWFdEAFDDdbT1gPuGMTmEP918z2CiiTmJTMdcdw_qcA05C39WVqVnEgu_babyRsX9LUxz5jHLjswKxpPy-z9bjwIt-M4i356_nQTH2Kta2i_zBBRk67dUtZejy4TB3mUZo9mS0fQJu3Ysu0zQWdP0aq9CmxZnb_D3thuJKtou2-PCxSToTR8rbkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
🏆
🇪🇸
#
فوووووری
؛ علیرضا فغانی شانس اول قضاوت فینال جام‌جهانی شد. با توجه به اینکه فغانی حداقل یک بازی برای فرانسه و انگلیس در این تورنمنت سوت زده، فیفا قصد داره رقابت حساس فینال رو به این داور بسپاره. جمع‌بندی نهایی تا حداکثر روز شنبه صورت میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100406" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100405">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVvPzovC8vw7WuHJ6FN8UU3QahcFlAg5A2t0NpiDcHi-VRtbY3WSE5LSvdARAcc6pcYHwtmuA_JxLPcan8nonpzSeLwbltSDesdIap_8SmPx8OtnlBsQWN6hDBZZgLWj67JrjU6-ZSAsqOv3ymqMu5vaZ3i2rub9iJwta29a677e4Z7RHmHpnINg3sxVAFJ4c8uhvDk7RfEcDK6hNQ6aPNmCsGfHicbRHdq4DLlvkeqlZPLZPqPxu60RAXifUNwrCHe2bJx82_LmB143Tz2hASagXfikapzaHN5mJCH5r6PBAKQrI7jY62-8reBopKL76vn6-I7csnBwX4jfJyATGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعویضای توخل بعد از گل اول انگلیس رو باید تدریس کنن تو کلاس‌های مربیگری تحت عنوان «چگونه تیم خود را از هم بپاشیم»
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100405" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100404">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇵🇹
➡️
🇫🇷
➡️
🇬🇧
➡️
🖕
چیزی نیست دوستان مهاجرت ۳۰ روزه دوستانمونو بهتون نشون دادم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100404" target="_blank">📅 00:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100403">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmlXBzp1pY0VHTgtBwoGscXwmKpwKGvI1PGItj_HXgmbJ8BBUmTfWxucGssvf72mwRmAkr6-OxoJW1Bnda2vDIq0OR01FJ4g1cahHYpulDwihHA4jlbSqkTHcu6PSooo_7WipoiFcmeiVG8Renq4xmkzTD841f2-y5Lyf3KvO4EF9fsPSl8ERzvxSqdylo0GFHYGUyybWKBq4i8VTNxPDo1RCLoviRNhxryD-CgsKA2ALSXcXBXgwFJ25r2Gecmnuc3REYCLL86qLbffslhc2x6XATf9jILkjlxGt5s4_txWKFCJu_k014jxGofhKzovGcOyN1dzn2V4x1cdvgNxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
|| بیشترین حضور در فینال در تاریخ جام‌جهانی:
🇩🇪
• آلمان — ۸ بار
🇦🇷
• آرژانتین — ۷ بار
🆕
🇧🇷
• برزیل — ۶ بار
🇮🇹
• ایتالیا — ۶ بار
🇫🇷
• فرانسه — ۴ بار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100403" target="_blank">📅 00:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100402">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6480a164be.mp4?token=l5tG3ET8oMeUJY0H-D_eDQal9Dl2lQDLWiW11vp_BWPLMnJYtPboLbxR7e5lENNSZmqG9LELMoHPtyuQjt5GICzn565lasFqNhcZsGFxt2HYBPCm8v1PyaCxl605mEoZx8tg6Iq2pSC2EcdyNHZxpaKmV28Ht__fSvDQP6k7F55HaQb97AJr8-xFL1zXTvBVXq6OcdvlxMKg35jKPjaVLy9zoohyARvxhyR4XuaQNMWbzPji5SoyRgeST-c6r3em0o1M1VKL6AoAayR9Mra2TYWYbGajZwbverrC2YEJJNvU-UFotAdYLegefAQHhh22hi4beqec25qRY3xyaG-qew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6480a164be.mp4?token=l5tG3ET8oMeUJY0H-D_eDQal9Dl2lQDLWiW11vp_BWPLMnJYtPboLbxR7e5lENNSZmqG9LELMoHPtyuQjt5GICzn565lasFqNhcZsGFxt2HYBPCm8v1PyaCxl605mEoZx8tg6Iq2pSC2EcdyNHZxpaKmV28Ht__fSvDQP6k7F55HaQb97AJr8-xFL1zXTvBVXq6OcdvlxMKg35jKPjaVLy9zoohyARvxhyR4XuaQNMWbzPji5SoyRgeST-c6r3em0o1M1VKL6AoAayR9Mra2TYWYbGajZwbverrC2YEJJNvU-UFotAdYLegefAQHhh22hi4beqec25qRY3xyaG-qew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
اسطوره لیونل‌مسی بعد صعود به فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100402" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100401">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbeJKrozH3nez2pP9zWquQKjlagJ37WxNwHARH6e5goigz8UJBKT8jgrTrsbOZZyynOUy2nXxTBhK5oL2t75dmRX7Q3TYouC9478HSXKft3nyVqHrHwgtev4sVIcoi-2evTw4UIZApLRZImLAk7I75n0Vu1AZ_qtL4STu5_fbUhhmWSBgpVlU3bQcObw2rRqwqpc6XDgAArZs-LOTRqcDdUMxhK1SY01ZgtF3MMJas0it7U_CNty66PwQlgKUc3iqaJL9e0tDPg2KhQ7_xXJ4KLYmFSEXD0L3uigEnB7JDcMqJwXfoFdWTCTd6XSmvKRp_ZCQOJkaxzbelA8YDhiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100401" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100400">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8A-hyhejfmuof125hA7QcXjxP7TrTJRNXUE_lxn21UZ_VlwiYT09NEmJRNtvxk-yXaVQMYW9wVFTLjwqOIMTibltPEvx1_v9ChqQno5lhUQ9_TxM-cGSp4hxKYVlKJ1vqj1v-zvlEfgLrA6NSKTQpton-NzyrrNxIk9VfB6sg4-ij3hTTLkHcKFKtvxY2AGKcq1J3kdP91FyilDHX-DPe-E-33uhLC_i4rxz3dmiBs_ue3jB6xYHdF3KDlCcdZpLjo27ue5iMUOMA8j6LtyWiSOZJdlW0qHQDM9ifh0Xf0TFf-tungpYU93SoOa_eOLA98u29Zo2mUuTfKx1O5YRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100400" target="_blank">📅 00:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCh1NBKqTCzeAwn6nxz25UbuD2fWIjNeSsVvfLXmZrOzTMEZwcU6JrmNtBrNUBsB69GpANK-AGgHTiF0oO3Wp0o3Py0ZsbOj-OMW7pPmBGR0Jsj4lnCdJ9va1bK4Y2l1awjGIMeUE7VztF4dXMOYIhe8dUelJTLYrbhZ2hls8L5az4YxOBcW2RnQnTuTnDSXICWLJMHCEKfHN_Pb7LFbK79TlaeNRsAZnmgIXd3Y6Qewp5iglXjJg7l3qCzoadsid9rxPpiDLTEj3Dvp7L8_G9Nn9p2ccmU2RESseZ2cRdvqqd7SwcLGRgSUMG0ys6qt2ABY8P5Ahn8Plo-1KNRAyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی، اسطوره فوتبال، با ۱۱ پاس گل، رکورددار بیشترین پاس گل در تاریخ جام جهانی شد.
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100399" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسطوره
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100398" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100397">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWiwCABTmsQUmto6ISG23NLuyp9P9DLxCFdV65zLyY60zRpqA1xDPX1IdRbpA2wCo9ZDAhz3tjOlGURoWryGD3vovj3ZZOtMgeyFetupr2whP7_uinSdga6SixgDJamaDPrf2BFLjPXw5JZGbPWS5uDojzc3AlQTKRpzFPjDO7bZNz2sLdKkAqAA5keyTxKATjSx5tpzgbrJ-hDsft2I28WA15QK8oAoR6eyZZa_k5b6IVOb1HizshNgnCIZiW2IvWWbI8xax-QUXcQKxH7E9gDRI_m1Nj6CqC9vt5EKIWWnJZ7ThK8sCHF4H1aDNURVZXwHfaqhASScYtysWlqDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🏆
#فوووووری
از ESPN: توپ‌طلا جام‌جهانی فوتبال به یامال یا لیونل‌مسی اهدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100397" target="_blank">📅 00:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3tgygK7MCq4ON2zZgiB1CMlkxjaZVewkdfSZpzoyv_R6B_8wEoYG3VXF6PkmI_XCM2hx1YxkqtosMMcP89mCJiBioVbjkN114QyySEPLQP4xB2i5a2HMe5HIB61al3c9pO7_f3hVjDcbsU8OEohnGOGTRBLlfoB4Cy28xs1wLLboKA9Gppij2y2u--FYv3xrq__NfLRvyKSvZMD2zJBJqg3rlXTD-HPLpFItC7rPrkVppZSzpL0nkw4sf6Ca1s8xZ97nVjgSJExQA755mJ0nu5qvK6LEOfRNX05GG8v3JIN1aE3tU0KQkx6UTo1w1F0Ws-2uRppyLuslrdogZdo0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
آغوش هری‌کین و لیونل‌مسی بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100396" target="_blank">📅 00:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d66FAB11EFP50DmMHcHXx1tLs7fqxRXRLNZT9qUKGQ0wx4XoSSMbFJ13l55XK20P9cbbUhKIRLUcGHZi1wgUnmK_UFwg9rShB9IrvYHiWoB2Ms8gME_eftuZoXNI6CaZmcAiQmpbg20awGmpVjtDR_nJO7kPaFk8raUgH4YvJ7-3DXCaqQX2KeTpEQmdOWmjeQ9B2zk2PX4pEF-crbVZvGGUN5598OyKk6uxQ3Sm6h-KrANMZZCJiEmK7jDoLGKRa39aOCqe8WZ9IXFxjLPj5S97xLULGK6qT090jP3C09fiucsAvoJS5XacvYmHlvYo6uuLFvsL5H3cZz177pAMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100395" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nbephOCelUgaCmKRMX3KPiSWo2oTXOLtKklNJeyX2hWRk_3L10CZ1UTZinxTkf1FJqOiIt4iQh15IxQVkNKUb3m2miRCDfKGf16i2VxNa0OCDFf1zY2SoSsyTZKn4xy7v3FVA7KhqvVLlMjsDdh9WH0iQrKrHfcLiyDOpbwtgKkeRmCmBd2kmTbnJ73ktEqSUWoeFNATwafFT1S7U6x2y4nETEwxE_JM5sGu-WQD00enadhtEjTlWBJlh9YdI4lwswkhdKJH1iQVf33iIgT2S_rz8z2iIHvJw6JUBQvmGEf7id5jdzKGuDN5wSvdnPlNLwvh_eQfH93sdbVwTwAz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه سر عالی فیفا به انگلیس
😍
😍
تیم ملی فیفا ۲ -- تموم دنیا ۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100394" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVVpWIYyzIW1qNUHUkQPyU7IxE-TzTbTzSNe9Ohx_KI0PUI1hxO2-1wlZ1nqa965TQHiJfrakyvE61QJxE8G9n3b9Fbp5WMi3GxBHWuW5W2VL8tQMCutVSwbJoIGexgVOIy7A_zY62kZHM18J6eYpvJu241yP6IZ9kiRWd5THekT5kXmhY9KkW1lyOYT4VKnXRaWQi2vz31ZoVXuXDJ7RIC553CadmXJNIW_IgulgKJpmpvFBc1i8zwED8Yyg35HUSvVuKGVGY5LhN3SKxR-e-vd5mlTJJiFK9KI8XF7uVcShXmmx27KPGGIoa1O3QV2Df8aQkW1rW4z_VLimke3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اسطوره لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100393" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
خلیل البلوشی:
- فینال بین آرژانتین و اسپانیا، چه کابوسی برای برخی از افراد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100391" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmtZnb1et2WRT60N7CiKw_QsTFzrtY0TzFRZeLkHrAelrg9k1sBMWUowhTHsdDIdtwMsTMuhQCGr_itC-P9ZkYw5VX3Rq06811FGqC4h-OAYscoalaNbGngZpefZNORF_GSd4lI0NhP9qd4D_rPkc2FpF9qX5IwIZERrUSLBabVrzYHbI-mxVagVbGNd9uT736hoJdXeYnKpfBJKW0sjL_ADiWk9pc_nMs3HRUlchlRI5gsnlregm97cmnb0SKQO84UQ4Nlz4GdeX_oLcMiMwJNEv0LdI2sXNT7HOePpmEJj7_wzVs-gvXHr_azuznj9lvon4JUUaMGlUeR93H4lnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی|ادای احترام جهان به اسطوره مسی و آرژانتین؛ نمایش درخشان مقابل تیم انگلیس؛ اسکالونی و تیمش برای دومین بار پیاپی راهی فینال جام‌جهانی شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/100390" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زندگییییییییی به کامممممه اقایووووون</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100389" target="_blank">📅 00:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DSCwsBME4SnMZLbDxaPfVmSZmn07NMrneCUjjZBdyTQAs551OqlfOzfw1ngFO2Ew98Csf6oK-iqqJNoK3QehFlEhMKqqYiCml87M9XmMVGdOfXLeM2Fu4n7z_eD11-jAVzBoar66jDcgGZSVpE-eJPfVO2tVotxQIqKBs1O8O8_l3ljXTGQI__71J5vcQyJ06WVBjE405F0TZZh0wtLuGzmVQEdebpa1Jqms726agZQpFEmp8gOSAhkRocagesX2chWymj_i91r7X4LvvJtTyO5LN-EihUWsdsFQJUOp8tNDeM9Vk4AAxliIOM32DPZKUk9lk7_HqbOXIL7DFNZbQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی|ادای احترام جهان به اسطوره مسی و آرژانتین؛ نمایش درخشان مقابل تیم انگلیس؛ اسکالونی و تیمش برای دومین بار پیاپی راهی فینال جام‌جهانی شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100388" target="_blank">📅 00:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBx_uj4QJWquAeU8VYIjew2JkNSaVR8Xi6uvfkEP-APcccaWDwLYf63Ygr5pVuR7XznuhqeUKhGUlbRh0ZgA9A_H4K3vo_E0ge3JebdpF0szgmaDjmMiRi5Qrm67hIYtbXfD711gHj27J_jBrOH2FFNrbCdmfTc7aeuNpatmC58_v7VRv3jfOdanVpjxHJDA1sydgJqfb77SGDklGQPo3MLPDQ21xUar-22LiLbLi7RDjG1OjlqObmhK7q7GxK352QBqmjzclLuBYyzG3oYKG-4qqsy8HLw2dkeqyxUsHqWCmodC92MpAVM_jM1Vbfqotba4S2LxdNxG2o0pNjK-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت مسی از دقیقه 80:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100387" target="_blank">📅 00:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100385">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">توخل حالا میتونه پرویز مظلومی استایل ده دوازده تا دفاع دیگه بیاره داخل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100385" target="_blank">📅 00:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100384">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کسخار انگلیسی جماعت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100384" target="_blank">📅 00:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حاله وقتشه امیرعلی ۹ ساله از کرج بیاد هشتگ پسرفیفا بزنه
🤡
🤡
🤡</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100383" target="_blank">📅 00:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">میگما ؟
تا الان که ناداوری چیزی نبوده ؟</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100382" target="_blank">📅 00:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100381">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🔥
گل‌دوم آرژانتین توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100381" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100380">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسپید کیت انگلیس پوشیده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100380" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100379">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مسی: من به اینا نمیبازم.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100379" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/591054bccf.mp4?token=Y9YLbaNODwWqw_Oe-gA_IISmzJz9nzfQ3lfap-d6UjtUll2vBbq8cdFgsJkoSd2j-ukusUtln_9CdfVTeUaYOk_5Gvu-Gr7L8gj-nUMLCtNhOnrPULmnfWk9HU3mkFPYFm3pZZ7h32D4wn25am3E3HJj_DbgDB5bYaM0aKU2LwreiTUZg5bAiPU5aSwQZRX0x-FVZyHCx08jagHyImJuEFqBoe5ZtvggH8Yoj8IiZchmSctQz3A_wsz4AVjuC0V-_Zj3NW0qPWt3hWGok78WmU2y-oy1eHkSN6b4sk9QfDAoLRpmo6nZITUrH7L3TERVuLLVgV9u_uzSzhXDv-4vY0jxaQafF2q3W7K0KAHXV29YC0jya_LqyOLYK13OpYlPAhML7KzWac74gx-MPTXNHKcwX3DIt7CpOmRBf9LZyTiaBysKAraZ_trFY406TY1dzsdXOElofzBWQkSx0C9gXKcj7AQNZ05X3hguNjxZqstfGqqAXNNjJ5KuRaVpzssWONw6PuJghhLcF4v0Ishsfhei62CpPwBwpvUzRGYxOJvpDntvlFATGgdTSdagxIlZ2y-vAwwhvvEEfjP2gy-2h2yoRjNJkzVFF-QlIKpmULtk8GFRZIP1PYCw7vPputAOF6VcpL0DNzgV2uKRR4kGE8IZjpvzDh8UqY8XgjL16rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/591054bccf.mp4?token=Y9YLbaNODwWqw_Oe-gA_IISmzJz9nzfQ3lfap-d6UjtUll2vBbq8cdFgsJkoSd2j-ukusUtln_9CdfVTeUaYOk_5Gvu-Gr7L8gj-nUMLCtNhOnrPULmnfWk9HU3mkFPYFm3pZZ7h32D4wn25am3E3HJj_DbgDB5bYaM0aKU2LwreiTUZg5bAiPU5aSwQZRX0x-FVZyHCx08jagHyImJuEFqBoe5ZtvggH8Yoj8IiZchmSctQz3A_wsz4AVjuC0V-_Zj3NW0qPWt3hWGok78WmU2y-oy1eHkSN6b4sk9QfDAoLRpmo6nZITUrH7L3TERVuLLVgV9u_uzSzhXDv-4vY0jxaQafF2q3W7K0KAHXV29YC0jya_LqyOLYK13OpYlPAhML7KzWac74gx-MPTXNHKcwX3DIt7CpOmRBf9LZyTiaBysKAraZ_trFY406TY1dzsdXOElofzBWQkSx0C9gXKcj7AQNZ05X3hguNjxZqstfGqqAXNNjJ5KuRaVpzssWONw6PuJghhLcF4v0Ishsfhei62CpPwBwpvUzRGYxOJvpDntvlFATGgdTSdagxIlZ2y-vAwwhvvEEfjP2gy-2h2yoRjNJkzVFF-QlIKpmULtk8GFRZIP1PYCw7vPputAOF6VcpL0DNzgV2uKRR4kGE8IZjpvzDh8UqY8XgjL16rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
گل‌دوم آرژانتین توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100377" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100376">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">لایوتارووووووووون</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100376" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100375">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100375" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100374">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چه فوتبالییییییی</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100374" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100373">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یاااااااااا خدااااا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100373" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100372">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ایننننن مسییییییییه اییییننننته مسیییییییی</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100372" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100371">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یاااا خداااااا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100371" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100370">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یا پیغمبرررررر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100370" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خدایاااااا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100369" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چه کامبکییییی</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100368" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آرژانتینینیننینینینینین</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100367" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلللللللللللل دومممم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100366" target="_blank">📅 00:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUlvV9Tmwdn2Fgl4HHMoAv_8-RFlEaXKETykmTy7OdZHBnJfj2MvzKl_G3I2OtEmWY6EhW6DWvkkgoLuyEY1phGldXXZGDE-Ml3ob_nG-ve8R5mX7hL7iv2O5vcl5Pe1fGY5BU3LKT0qvxpJIF5ndQ1eFc6Gu7uP1-xJzFd7F0btb1QWTS3vRGZkokrmgUnvqlBKxRvgfh-SxCXtZeXqjch3gJ6nKDt3tKyIXzuBFhfoKarnScU2BUB0OkoK5yixEYXn3UqBOptzga4njqX4nExHet1TUjSznqM3gEiLPKPB_JcO3z9QY2OMWb1bqc5PZky0m2n-LTBFyk8OEA0vYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم همینطور بانو
منم همینطور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100365" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">۹ دقیقه وقت اضافه گرفت</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100364" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100363">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d3c31b26.mp4?token=oc_XYv3HgupClDEo4pkBkRXBBkH9AjmBW_uyfwpm7q1PO9hCwn5ANTUC--Ld569R28bSLiR2IBg7j2u2Y7VT69cEWHnpaU5gW0XQWpFDD34nIqS-K7DdFW4qlO_1aJs8LSX3lH_m-PGYCUrltcw-eo_k4Cuxy0yFE8sl-kNgS6fjFZp64ZRXP38SEcvQymJZlenc5V1edry-WyI4xMza24CsPsWpDQHJvH62EcDh1qO_VWB1P_ce5kuEl5c4I2F8WHnQ974kyNGhsDLcwavmT2VXKnPgGeXWrmgLbFZcJxeN_MebphlCbunVRtSZka8WHS2xuGuj1DVRFtuDieAiiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d3c31b26.mp4?token=oc_XYv3HgupClDEo4pkBkRXBBkH9AjmBW_uyfwpm7q1PO9hCwn5ANTUC--Ld569R28bSLiR2IBg7j2u2Y7VT69cEWHnpaU5gW0XQWpFDD34nIqS-K7DdFW4qlO_1aJs8LSX3lH_m-PGYCUrltcw-eo_k4Cuxy0yFE8sl-kNgS6fjFZp64ZRXP38SEcvQymJZlenc5V1edry-WyI4xMza24CsPsWpDQHJvH62EcDh1qO_VWB1P_ce5kuEl5c4I2F8WHnQ974kyNGhsDLcwavmT2VXKnPgGeXWrmgLbFZcJxeN_MebphlCbunVRtSZka8WHS2xuGuj1DVRFtuDieAiiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌زیبای انزو با گزارش عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100363" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100362">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">داور خارکسده ضد آرژانتینه</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100362" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100361">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇦🇷
گل مساوی آرژانتین به انگلیس توسط انزو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100361" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100360">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گل تایییده</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100360" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100359">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کمترین حق آرژانتین گل زدن بوددد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100359" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100358">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پاس گل مسیییییی</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100358" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100357">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این ارژانتییییییییننننننننه حروم زاده هاااااااا</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100357" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چه گلیییییییی زد انزووووو</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100356" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100355">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ارژانتیننننن</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100355" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/100354" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">چه شوووووتی گرفت پیکفورد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100353" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چه پاسییی داد مسی ولی افساید بود</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100352" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100351">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انگلیس شدیدا تحت فشاره</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100351" target="_blank">📅 00:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100350">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیکفورد لاشییی گل بخور دیگه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100350" target="_blank">📅 00:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100349">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیکفورد چییییی گرفت</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100349" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100348" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100347">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">چه تکلیییییی زد اسپنس</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100347" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100346">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100346" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100345">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گوردووووون</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100345" target="_blank">📅 23:46 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
