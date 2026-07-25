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
<img src="https://cdn4.telesco.pe/file/BC-mhdXhf2ejNninwu1tvFgBvD0nsx_gHeooRZ-GCUq-b51D7xteGBusRQoY7NZ-GAm1uVS_tvZlD19jremcmI5C_cmgv8BjGMaglf2e9jGWS3Uo8MR-x0sGxXmShgmBqrpj5feCFKiYYwnKWUwHLCt27MoEOJbnlkgPm_0rlEO9uQUsY6fu_XmRzXtSlurxkgjE1YpqprBtgXcjO3M_XiFh0gHuwV3QnIwZuwcB7QMP-AToBqPLAug2GetDhNEgelrT3r6PAAw9c6f3FfWhB0kx-x2IgeZgKRMeuTjAu75S25oFFXsxnRbLOwZ4XexJZrA5-QK6kuGEgumxy_ktuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 150K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 16:44:49</div>
<hr>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=A4i_UImjuSp181oxlxaqRUVpZdAQogr9s9ko9fPAg2WWkr_PWtsbkD1uOqAYFCUplvEJ8VtgO62_dOad4SMiFHotMrz-gRsJgwGY0nMAIS6Ijkjyet_gTqiHOPvVbwAqgWQSg2Gs3CuPXnNFqYQmG-wbdDioaaW6-cBe0s3mDZnjKJ7MfOdfssXgwdQRwXh4UEGrdtnm1TudjW2GLgDE3EnoEBWlm3wLhKnOPg2TkiHz4JhCWJCK_yNczuf_3xtWBfdkw19A5V1fod_V0aRRXiYQlW0imKTiTYAa903M0DrQKIRbuEJfMvMUeCBLxD9Z3PvCKzYVRsgeZMzx0nQsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fJbFRZFCCgYNwIRWjjhlHCr4kSu9UH7fEXbZE5G0wK5cmW3ukOZej7PkdStqlDdZdUKK6m4QkdWTwr3GcyHP5mg90iQWq10SWQ0FevDtcPR21ARorOjtPV9ob8HJt3xE7S3IjXN-GMk3bzwHamBPbb3ZCdsaza5Nh6GNnoKXCN7I5-mC1gaXv8-4RrwmB33mdSL13i4lhJ6XF2M0sBh6RvqG_tKRcCY0UYGjROrgpD1VtozQf3x97qf2kGrzCdZZzEJ2LXFhF63JBGGYPrGwhDrEc8uAfEAVGgirw_88-3aI1y8uePMdX7hXbCqGnH74LUs6UM--ETYZ-GaLziXSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=MHnevhGAXkWupFc21c9wSAQtHC8R_eqLaK45ptVQ5PwV1nu0cICrIAWD0U_92ALZr8k8VBvgdLv23a27lal0C4h2WHsMsOPQwDM1OkvBwza63aJmgNnAb_RU9sYh4rtD9m48JlMVkRDswjufV6v8KL_ELow-dtJ4YXOxpILwzq_zTSCxJAmtZi0EafgU2YwGJlcGqwg3efdTRM9ZSVEnDon_4GFU60TC4VR4Ylu_jr1cc4xCCCk4suYbmmcdBs8k6sWhwaaQKZdDBOzLgibQJq_dKDAunKVXUTRpVsQZIVzxvQKYjI5O1_m-lRaq3Wzd-u2VC4JJx1feqaovx0stjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlaHPhx4-xCMeKVcpbu59G1NJ3OklrZv48iCBFj9Mf_i6BznpNgJX_hQyyUR-wq4rrx6qq1ebRPLm0IeXHeeXYvrAw6UMjF0zsfgls2MHhFtABSQZ-tyXHvKpj4AVU44rOnv8W-kzOaKBELt4LcbHciMWgJKEqGk6Ifb7us2ukizxFfDqDSWlnKnMGOqI9iuUALs1h-q7g8OpyiqC_G1XCzTtJMavgYnI0dbehOERq3veXJ5eTmTe8zIyhNh7sj5a9I2RCaEBC5ri3pLDo_ojF0zSL83ZmM_e456Udpc3kCWdeRGRM_7d-9c3Xh-vPeE9SCSuTzd8egwMv3gZjw5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=phHuMXE_dxpNg2ViGJ1xbpbRGeqdbdgEKFBxI9tYbZqQAKG7Bt9RN37QHn-ZxEv2WikYVBEalUITjaf8h3--Br6hU8J1ezmfG5fNAB8PuPkuCKLWn7Ja_Wauk9e_Y8vNIXUqbCmMGB-_nqXp4XFnQ2iiVwIKD0Vk3NhqvhMdDqSkXRHqqkymVe6BbMp5dTq5hBR51sxRxPf5JhZlfQUUCcUVKnGPYKror8h4ho3IQvDDmDvnbBNgYn5t67IIBVVZYBEdd9sbLTUc5yhwnlwGrZf9W25QXhY0E9FS8zWF2n5bmb-Zg3FBs59LzDHXrq6029_4zSSYPADI9aOaLHSVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGz0K7XpgvaQxFRyCyWXWQ3UDmF4h2gMS8A1As14glMxi16DFJt6PIRBq07ue1q3VjRslbu2mlMxi7ekco8ErKa36ZqnY_TN9OXJkfPs-3sYr6dttFrR4GgD-EJDpWnXvoSVQAP1RCEyoFH3Uml-QaipD0ZxUXvLaTBXKpG_jyWQlMuceOvFrdxYVzYdJaWKg4Lt5AHxCXLx1YqC4cf3Xr8BGrgll2QIWAckzpbGZ66V6MRJeAYCU3NshkCzFB0Hi0saPb_TtZ884Gd2il1a9vKkIMNB9QqBAp8-J4MYj-Mcz-3V0lM1ctisfPr3fcS4NDlwpY1pnId4X-CVltUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=bmC2q_r9iy6MgP0ZnQOUUwtZwrn-TMIV-TOiUovlLoSqu6w25SbqEl9VusRpqMLRCgyoqvsFTMMascGkKXyrz3aTWB0WAfZkpRZQA_1IS-JGZDkI2k6C0-MGNl2JNkZhEVAXoosnjBq9aH9pkfZWLP_R6M6fqBHBmJt0CzrMOZ4W5aWzG9kaz6SVSk3r2AShSO2VOzckQLtqRi0were9ZBeVgQBds9eRE_8dbyqu3XIhb2R_dTWL1HF9qlwnrrz8VGXaeTEuyGj-K7EE3PLTHaz4kLQ0FyD8WB6YhKo2Bi4gFsgkjJ1LYQXhiXR0KJYYukwQmq9Q53iT-MlYE_AA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dIQj7mIsfpe9rn5KFKFpYcc51iViqR-AlrO8eNyAuFNmCx-iT7AsaNY-jm-rSS4xdXKiLW5Zns3MctgIeOjdbmhlic9Z6hNHvJldvLRpQmYbUeJlXwg8_AnnhdwzY7HNrAQGbu-mKM5f3DJbuZCWnp6NPMBKsWsnPM4UZpPXBgDFW8ntYXQeRDE9dnnGwSF8TZr_NjeL2n5H2caMrd7UiJv6dyHIJGfuwH55TiOwxobr85Ehf35saKjQzjgvEvRdsCPf7S8F-E2lnV4IZd03PCruAscpQmPZz_7tg19V015v5BLrMhbr-5VSmt0BLlQti2XV96x2gT1iT3i8q39bKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=dIQj7mIsfpe9rn5KFKFpYcc51iViqR-AlrO8eNyAuFNmCx-iT7AsaNY-jm-rSS4xdXKiLW5Zns3MctgIeOjdbmhlic9Z6hNHvJldvLRpQmYbUeJlXwg8_AnnhdwzY7HNrAQGbu-mKM5f3DJbuZCWnp6NPMBKsWsnPM4UZpPXBgDFW8ntYXQeRDE9dnnGwSF8TZr_NjeL2n5H2caMrd7UiJv6dyHIJGfuwH55TiOwxobr85Ehf35saKjQzjgvEvRdsCPf7S8F-E2lnV4IZd03PCruAscpQmPZz_7tg19V015v5BLrMhbr-5VSmt0BLlQti2XV96x2gT1iT3i8q39bKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=TZmpOkGjsKh-mvm2cFH34z8tpTwNssfLVJ7T5U7CVeHTY_sJ2A0h92p_SAsVcXeaOoOwwbo-V33UiPiI3JPoVD0ixsLR5MpL2HlmR2-xN-TjuHwuzE_DIPFP_Swj4uns6uYL5jYwOXolwYtdGCM5R5zUqIPsHbYK_5Jt_pZifmEJu7wrmd3iV9lhmCjZX5PjC-N8hJTE2nTWFT50b2Ou2tJ0HGfYc-QM6Cmg2PhPKy-pwv400Tisl-iG4v6HR3jL6oGMB4ArEXkdc8GJr6jGN7Y3R2-T1lusvycIr0IuCL8HlviiF0VqvHg6z2evP71sK5qGJ1_5n1dwNKEveFilHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=TZmpOkGjsKh-mvm2cFH34z8tpTwNssfLVJ7T5U7CVeHTY_sJ2A0h92p_SAsVcXeaOoOwwbo-V33UiPiI3JPoVD0ixsLR5MpL2HlmR2-xN-TjuHwuzE_DIPFP_Swj4uns6uYL5jYwOXolwYtdGCM5R5zUqIPsHbYK_5Jt_pZifmEJu7wrmd3iV9lhmCjZX5PjC-N8hJTE2nTWFT50b2Ou2tJ0HGfYc-QM6Cmg2PhPKy-pwv400Tisl-iG4v6HR3jL6oGMB4ArEXkdc8GJr6jGN7Y3R2-T1lusvycIr0IuCL8HlviiF0VqvHg6z2evP71sK5qGJ1_5n1dwNKEveFilHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=GFr1gtf-1OD5Dv07qRAZrmyfDu5yyCOHFSwzKUZPww3rCqriy3ZZmsJGhuLTSUcyxTIwbvG7qbTJZIE7sCtWFeIHx2edEHdbL7I_pmd3fW8HXH4JXU-AZk7KvCJ9tBOn581XTY-FkRAb4ainiR2uLGbWwYvvleONZsNtOEGb5hAHjdSOtfDPuYot-MpIzEfOWdsnb0gS8i1X5icOoEQGpMI6gFS155XA8mSGN9Jhf9dtQGfR59jTkviQhAAp7FVu17r8txpoNFh4RwD0hNPyCcvbYuUEXssyMdR6CMvspL-by4tKcIIIHDn8uJM2aeuBwKdrxwqJuzVEL4i12bv_cKmHsmBPwelJEM2WyKJ84SupmZ2afN_RiBUrmJs6vt7WUjbccigXf3MCRuo_uVP6HfollzU3zqERAvCkkdyr3L-OrS0igFoAlBW49WfmlRLnkS887qpqCTXPbkUhFpYxucSsM3TH6Jhn4Uawfyqroeqz72JOE--v5H6QVXSBxfjkroCcqyaedF4cnn3ErxxJ3kMmYYuhCx9r3EETb9W_RLP-9k39dEmjs23JyeB54IGG-ag6F13v6t8t8G5nk8otRGz2QTNNz3tJudsbCVV1gWiW35Nbr5IltasS64xfV4BfzB65ZNnU9koCX7YxIYGu730vAXqOWHPQq7AH555GUos" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=GFr1gtf-1OD5Dv07qRAZrmyfDu5yyCOHFSwzKUZPww3rCqriy3ZZmsJGhuLTSUcyxTIwbvG7qbTJZIE7sCtWFeIHx2edEHdbL7I_pmd3fW8HXH4JXU-AZk7KvCJ9tBOn581XTY-FkRAb4ainiR2uLGbWwYvvleONZsNtOEGb5hAHjdSOtfDPuYot-MpIzEfOWdsnb0gS8i1X5icOoEQGpMI6gFS155XA8mSGN9Jhf9dtQGfR59jTkviQhAAp7FVu17r8txpoNFh4RwD0hNPyCcvbYuUEXssyMdR6CMvspL-by4tKcIIIHDn8uJM2aeuBwKdrxwqJuzVEL4i12bv_cKmHsmBPwelJEM2WyKJ84SupmZ2afN_RiBUrmJs6vt7WUjbccigXf3MCRuo_uVP6HfollzU3zqERAvCkkdyr3L-OrS0igFoAlBW49WfmlRLnkS887qpqCTXPbkUhFpYxucSsM3TH6Jhn4Uawfyqroeqz72JOE--v5H6QVXSBxfjkroCcqyaedF4cnn3ErxxJ3kMmYYuhCx9r3EETb9W_RLP-9k39dEmjs23JyeB54IGG-ag6F13v6t8t8G5nk8otRGz2QTNNz3tJudsbCVV1gWiW35Nbr5IltasS64xfV4BfzB65ZNnU9koCX7YxIYGu730vAXqOWHPQq7AH555GUos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9CZvSGD712qutDCEn-IWPe6A-_8f8LEDaqR-dMbb6NLy0hjLIcqjCwL-3Szo-4qBQRgMO7-dSqXtQNDq2fGI5nyYdpprxxIYMxKmxvzoSlKaJ656Vr1X3La4b76yktqXsrV7M5MhxpBA3NQheTWBFDADpRjsxNFtcVGDio09RAyUWRNEUes7hWeUFiRS0j_haXqFnLh8Xz4cMh7Tyz1F2pCh3fM4ZYB7WDMvgC9ZcuvvgqVRBAaggYce4QskGv5nJvMPEoHsMREYB-6xkas1v_UarhB2Y9VgZMHuJ8UKWV8AFfVEhe8Eyr5p8fDXfVhadrCQRtnW6_hOcdnt5qFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=Y637e86oqfy4Zqj_JBkteg6XCvO3Lomls-nOgyrqu2TbGUCYcvhFGkLHEC37Fuxblwu6sq9t8zqWRqY4Vp6TjNdrqaTBKf4yCH_vPJe1c4XwJeu4kIYQjyt1HqeYPvpt7UPPnTbnxwasLZ5I4RnIPLToxWvRQNYTdFSLplStWT9AdGQ1JDyBKWvxBUJgfIKm8dumYw_FggCdviECV0JNRuSY70Lw07J9A-nyTijSw1_BWAKTpoAxIvzS18x9bvIcQfwajSF9_v5yooLpOQEDzYxmlcBO26okmmXVAWJSoudWlo9L1wgsPrL7lMyT05ECCIlE5s3ynH19JpD2jRc4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g57WqUUzg8LwHxQH3VGR2fBvYfyJv_R1xsqeLQG1ucOJp-mJPk0CdZhqTxy-4Ek5-A3l5UdLGB-LLedcnfWtCcf-nY-S0QtLypTtZhIG9ip7qMLoe3u6MhtJuG9zuiYGGjGdPQO1FiNmMu9v6S5D0ftMf-1NR18dB_0YtByfeQH3ulvHx-gD3QEzGMGI4wP7199i-aIREfdUGec0DggmSpE9Jhauvmeij8awIQ_1IbPvFU5_tZTK63BxOfLYJu7pMcbbxYWXinIGkwxPrWv9RXfKV9FnbRmSu0EUVFqQYHpfqR2g2ax7LOnFKuzaLBETqsgyuW9kYm7gm_l4Zw7Z4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGpCGD5xQCsEQ4kUQ_77MIELxttBZ7uijsFU5HJ1mBe9aXNJ-Ib-RJo5zXyOAmWCMmjXsjDeEDJCNaxT9LfYriJ3GPRWROTMJk2iRUOhTFpLb75fJrIN70q2cAkzZ0YYC24AGXVTCgpRPr9YOjxmXLxiOpqhXwR7vztxXQrEzod8XA02g1GcDa80mhTqLxIwv596C8Wz1I2sZXDkZ7583uSue8xahXWaGZDZoNgvgkuFzy9zpC0rT9XL91b6uzvYqkKewcMtKLNia2RXk5O5nh6oo0vTLLiU3jqY1-LoQzfHLuI3ELB8vmKjFdHOr2SjelobZSlytsREppL7VHoR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY2iY2032c8-Blgxzx_NC-nPqp6ZXmHRHKnRXryQ6MHMz5fBhEcKXkwx-M8WrtxsS-88dDh7_gzmmLVclC4vbf_J3cFlVH785bMsl7v4J_4l3CDFtBpN3ptvlYZPLmBjllZJYk-kjjYC_9wqk9JL8HFdO-XqbPmRcGp3huTa9H0wWb3Q7HrSCAf1bgDZ1WdZAVKmV2Gv4IE-meXpG0vtGF0V7Hc2pFTToNY_IJULnecsr2DYrv0xcuenYSu1XyVFGsS0B7ye7kUzGSrAMkcQByWOQBCcr6QuUX0DXQsWv3I_gEM1XGVUqoFmKa2xpg5yxUFy5NslM3cccsoC4Xvcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiTIvqjpeDRmUBybUp-t3ol7m0Xnx9_UTFjFt1H7_vU1LECwMRgN_cks5RgnfTWd2Rg4Fcp3-GHDe2OZn2yzfjqiUbK9wAty2iD8T1njvuchOEOpwPYsYkmrrPXcuqXscZZX2eXcv5TI3dm3J6a2l_hQPTZuinkFSzhVZcVKcoAPODrHmEwmCRKQxatVBG0RBlLB4REwYZCUjOUTwNHVGXZ4feDR2eXPXz2xUKiBniodM_dFVawFmvVqH40_J7yfOI0YKFaZrniVJHaurUaKd6PzWBLJ41y-TRKkpj9Jzu4318DDfCcAu9uN4pWKPjzlh41G3GxE-RbuBquFokD1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgkYvPAQh-DjN_QUclGZRnexFEBDOJPHdNhAUwzxFD0j8WH5ZfK30_nJA7a0Cp1SvwsAOcSaAdJ5BH7UD4HPuD6P7qRcy5TJYHVEq6yRmGt3G8Ih8KRbG_inBaptd4xerYnYCijnPuPtwc4kHhfgVbIG05RDHYxIScaouuV1jwzWoK7VWaNYJtiVH8PvqdMQSyAT020UuMH0nuPzx3Ecl2MsXqaWuKW6kbSKyH5ysb8UQaWCq31pP81egOEQK02SeUczNyW0J6GgQoiu-Lrc9nsd7muPgXmE2MB7ha21WXhxgSkymDqvM5sN-9HFK0whitmpKAOdjVonNrvwDmDEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZF7SicmL8dk6H75WJYkR8thwOE9yXuGHskyy500aTKw9egmgfO_OO3zTOPATvyHcjvMItp-ymD0NcAg89ncUr0QmN6NBLSvXca2DO48gecv3UoL5Yf3tJFshIHphjzMCVP04G_HkHZnRoIwzNK3oGCuSRsfzNcqpOg2Glk_8tcth776W8bJOao3yZgP4-n4cw3vpEfEFBHAii8bGPaWzZ3N_iwYFXgJ7oq9aiO_ZOOl7Urs6IgeyTWtvP1YtX3I0k7vqImYIK19vES37KSptjs3BzSdWbeH86T5Zu7gOyCgE4RvfKyKNzPTjYHkwji8nw1MiaXExhshXvOeQzxZqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=R6K2PkcaFFEsZwWN9y9TtwYu1DSGIpmXPm_-VowpQbhZrcPLFY-Rm0EXB_JqcPZitbneZcf8zBlgAsJUCSXJ3gNUEqEtz1L_sCLwdK3N8oxPvUEm2JTYNeMXS2XbDCkOsUgtA3uyqJNIl8nXUyllt_XYh_b_CEKf6g4LnaIWnMMtFhBF5OMPsQg1U0MxjsZ2LYvkJ3bh_MV6WUajlF8myddnuszYzKNeH0GG9XX0uZkp8ayTqC6SAgkwn2wBC6tdpjQNeDJZ669ebg0XnFkr8zsVXpFYvJAJ9k8A35gNPNp0xZBhg2wopW2e9caz2LHXD7DcqaMQinz9oFlwp-x8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=R6K2PkcaFFEsZwWN9y9TtwYu1DSGIpmXPm_-VowpQbhZrcPLFY-Rm0EXB_JqcPZitbneZcf8zBlgAsJUCSXJ3gNUEqEtz1L_sCLwdK3N8oxPvUEm2JTYNeMXS2XbDCkOsUgtA3uyqJNIl8nXUyllt_XYh_b_CEKf6g4LnaIWnMMtFhBF5OMPsQg1U0MxjsZ2LYvkJ3bh_MV6WUajlF8myddnuszYzKNeH0GG9XX0uZkp8ayTqC6SAgkwn2wBC6tdpjQNeDJZ669ebg0XnFkr8zsVXpFYvJAJ9k8A35gNPNp0xZBhg2wopW2e9caz2LHXD7DcqaMQinz9oFlwp-x8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=Fd06riwZDh9kTivlGyIiH79zoXQ3LyzZccPxPq-EUDeeKmHkzRFJdYNIOdhm6I7v9fuXvsfj3GgU5uEiOBCnMhvQuNMfPWV85hmrwtF-6r6gkBXZ09b1Yor7KVcqNkCKcy5b4E9vgjOw517LyCKteq6jnct46oip7-X253SQUs2JGc9Udp17QZCb20rYoRSjEeD9y3z-hDBTEG95zym5a8lRxvzR6ooHN6XskAZ4TvzAtJFCFTk0OHSMLnWbzeO1_alP2aP6AEiGdLa9H_qqeOfkCTmFQaN1pD5UVmZUzVYPAfkX3EFH84ZhZ2e19n2llxmS3U77S6ZTSfODA9cbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=Fd06riwZDh9kTivlGyIiH79zoXQ3LyzZccPxPq-EUDeeKmHkzRFJdYNIOdhm6I7v9fuXvsfj3GgU5uEiOBCnMhvQuNMfPWV85hmrwtF-6r6gkBXZ09b1Yor7KVcqNkCKcy5b4E9vgjOw517LyCKteq6jnct46oip7-X253SQUs2JGc9Udp17QZCb20rYoRSjEeD9y3z-hDBTEG95zym5a8lRxvzR6ooHN6XskAZ4TvzAtJFCFTk0OHSMLnWbzeO1_alP2aP6AEiGdLa9H_qqeOfkCTmFQaN1pD5UVmZUzVYPAfkX3EFH84ZhZ2e19n2llxmS3U77S6ZTSfODA9cbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=o7BpE4RDNI1Bh3HK-GDpQ_FEvEDxV9U7gQtwiloH0uiO0rpUgu1w9ExCSkhRpivQXLO8j90xFOAgjJSvVshhMPnwY1hHjqwPcbBrpsuRGQHEUITagND02jXBL2PQdOe0TMeYeW5u7-q8B5UTjjnuNAbCwPJPkkjxuBDsLgwLkTUyOeolv42lMC9zvHnfYJPXxEdwVyLGaRh-6ZDzSwX6Yof3GLY54m6qMODsH0Rocg4n-NmJut1ETj48eVuoX_5lnrVqkDxFDkwlZiNvdhaYyjAlzQzBdXvHGgOL6lnOzkH79u0T66MBZ-gwWvMo1V5aLm7R-XYhfrFEZeBVCM5lIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=o7BpE4RDNI1Bh3HK-GDpQ_FEvEDxV9U7gQtwiloH0uiO0rpUgu1w9ExCSkhRpivQXLO8j90xFOAgjJSvVshhMPnwY1hHjqwPcbBrpsuRGQHEUITagND02jXBL2PQdOe0TMeYeW5u7-q8B5UTjjnuNAbCwPJPkkjxuBDsLgwLkTUyOeolv42lMC9zvHnfYJPXxEdwVyLGaRh-6ZDzSwX6Yof3GLY54m6qMODsH0Rocg4n-NmJut1ETj48eVuoX_5lnrVqkDxFDkwlZiNvdhaYyjAlzQzBdXvHGgOL6lnOzkH79u0T66MBZ-gwWvMo1V5aLm7R-XYhfrFEZeBVCM5lIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=V_6ucBfx-Z4ThVIzyAggVh9qApzVFwmQi4ypAlUqUS6i-QluBsTBXeMWtH167OHEbRyhU7mlWFsm_Yt87Cy_wBMZkDO90TAU0wrqRGTrI7VdIcHIppGIchmZ1YR1uxMpDoXeGuvesr1hKlmvbyhQAGJ6tIvKaGzvmTE2RDShOCv4CZCSZ5KrQ94EkuJUf_B_y_pMgr6qSxpoV47Bmny4xNrHFqygRg19k9amf_nEt-MNRCgtEXBsr-rLFR0duUXczcHqUhEZPh5HjNjkE7b60ajU1Q-5CZ1kGwsH7lQ5n92sZ0FTqdJREHI3lTYBsPWIMX9rFoXWh-L300HP2H0eDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=V_6ucBfx-Z4ThVIzyAggVh9qApzVFwmQi4ypAlUqUS6i-QluBsTBXeMWtH167OHEbRyhU7mlWFsm_Yt87Cy_wBMZkDO90TAU0wrqRGTrI7VdIcHIppGIchmZ1YR1uxMpDoXeGuvesr1hKlmvbyhQAGJ6tIvKaGzvmTE2RDShOCv4CZCSZ5KrQ94EkuJUf_B_y_pMgr6qSxpoV47Bmny4xNrHFqygRg19k9amf_nEt-MNRCgtEXBsr-rLFR0duUXczcHqUhEZPh5HjNjkE7b60ajU1Q-5CZ1kGwsH7lQ5n92sZ0FTqdJREHI3lTYBsPWIMX9rFoXWh-L300HP2H0eDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=TfcDNyhOqAdPvzF496gF_eMYyhw1cpFIe8ZVt7XjcDgQw3YKXFV-ErXebRHGTqvtbCfSig2oXNQs11_U7h070CT7Gfyg7QYwcylS2law0SjlD3HHqlQSI6Na6U7-Fzl0YvcC8OCYepYzyg79gOC5IyWUw87Xg-Sx62bQYclU7JaEwzBQG5mVtXj1_CzZ6M_e1M_3mIVc5IKoK1Xkva7NWnxcOdK5Zmzn8ozO8M_menL0VY63hTp78UG2IyeZq19iZio-VV5M_A57XU7LCbQlfVAFi73i_CxG-Z-fQ6Nu6XkU_SskBVC2z7DOUheWMi1INruBygsBx-fdnKzZ4Bg0aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=TfcDNyhOqAdPvzF496gF_eMYyhw1cpFIe8ZVt7XjcDgQw3YKXFV-ErXebRHGTqvtbCfSig2oXNQs11_U7h070CT7Gfyg7QYwcylS2law0SjlD3HHqlQSI6Na6U7-Fzl0YvcC8OCYepYzyg79gOC5IyWUw87Xg-Sx62bQYclU7JaEwzBQG5mVtXj1_CzZ6M_e1M_3mIVc5IKoK1Xkva7NWnxcOdK5Zmzn8ozO8M_menL0VY63hTp78UG2IyeZq19iZio-VV5M_A57XU7LCbQlfVAFi73i_CxG-Z-fQ6Nu6XkU_SskBVC2z7DOUheWMi1INruBygsBx-fdnKzZ4Bg0aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=npuHGqhXtMSNtKR19oFVHAqvqS5QqUViFqoolFrUQG9G9rgiii8-wUZfdkICb9aMEwCmtQBUypPBwhAizXWAX542jc82apptitmpVSgKQfvhAVjLADbaw4p3cOFSOvcCoPM8VSkIMg1nQesqWYabsbIK1LRJ4t-Dc1KqGqSviXQsxEjpu80cxqejKNmI9tD5WqvST4ahQ3k3kZmC8O-LKc7VQdPHiwnB3w8ju3gLXbq9H3GXb9fzUAAbGXP5Ev67FMfr3OEFE8GkrVGFxdlNyORl8-kpJ45Y2boC0_7VwbrRGsUg9m85O1J5yEo1tM7hzDkbpyXvuMq-joKTHXrFjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=npuHGqhXtMSNtKR19oFVHAqvqS5QqUViFqoolFrUQG9G9rgiii8-wUZfdkICb9aMEwCmtQBUypPBwhAizXWAX542jc82apptitmpVSgKQfvhAVjLADbaw4p3cOFSOvcCoPM8VSkIMg1nQesqWYabsbIK1LRJ4t-Dc1KqGqSviXQsxEjpu80cxqejKNmI9tD5WqvST4ahQ3k3kZmC8O-LKc7VQdPHiwnB3w8ju3gLXbq9H3GXb9fzUAAbGXP5Ev67FMfr3OEFE8GkrVGFxdlNyORl8-kpJ45Y2boC0_7VwbrRGsUg9m85O1J5yEo1tM7hzDkbpyXvuMq-joKTHXrFjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvU4hKJ54_8A66WjyTGsknpczwQvqc-hexRpX3B2z3w5TAQ5hzDAEMFDZ_0Fqj4fUQcjE-FsgFUeaaWCN916lBRQ7yBlb6bkY3T3MBlZuxK_dknHPEQ-hyGVghdPq6lBwJ5oyZvYb94pt3ScVdLsKH7A6EcHq_Jl2zHlA_OpZzgOo7_6bmRn0SdcTa-JepZ26EbsY_wRkVcLzD26ykimIbZT6jLWOymAQ2peZxrkNzv6wwrrRAFFE5xUDpVO2kI62iO-zYXPe2gN7MscIobfU5frxn5hOyZfLiY4XUkxFFz-qs2lHn4bktWunwdqRadfeRuZ91uuZbPJC8YxB3pzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_E8kpUaiXD10b51JYOG0OmpeMe6mmAcz51jcEruSajWcErMFWXJZVLieFuVrNil0XBRDAa5oXXbDWPazVdi8zt9gz9HAXOSxu45o1T6afuNvXyjp0bxDzp_DE-BFAY05Re31mi_FcWMRB9UOKfivG2Up3GoAJtq-xowxK6s6Zp5obBnJW-5CGL9bbYGz1mDaEriqpbhG_oP1W_r6nXsx7CCYRIj-Ydx_ldOWjF4fK7PhzxuFoPf3q7Tx-QgCFSGPl4JCHBWD66tsD4LUbzR5wJbY1nCaDWAXvam_IhBne2RLt8jEkLxH3oivqflhKTa4wZhNJRUCh7RR6Qff7Ta4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIB4v26pGjwO3YEVigZAlIjR1cIxbFCTLXHH5_5_x5Ua55Yk3MxRznMrJzx0B3g5XfMw_jm0-WsULm8zNnF-D1rReq971HjL7Uz204h30ROLYYqmOmjg1lWrwtHblni54ow6-fxWpC6b7BYuzr7gaE3816QiUlAHxL2cbi8eBvd6_AhvKX4bUY31Aa1CMGSYWEXdz6RjjcfGdPp-Cyglr_hqNCkwz-0Nc9RamKizQAYu8YArPT9-p785D1ov5IHIQEYhaLDa3G_N7Qhf9S9Bnu3tTlib5mNLO8FqoUg8abQJJ4-OfIgO8KBrKdJQHCwnOnsIuWzYdl3KahOdSRljwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=j3M83j7aH_ldKHsgK_0nuNOKlTcg1GnopmA8CllHCDEYIRKDrWEkwADrf9dC1RnB3cxBpbMyVq-L7lD16SHPkxUOjYcTkJZ5tUBMKZopjLU1BgaHK_uyO7z5fXEHVFLlisNxKVJVLzgKyE-eqNvj5MpEyRpIcx6orSAwVVszG5dMdW2kGmQJRb__W0KdCA43f-5dAv-3EMCdIHF1ygojTxxda3YuyKbOjZ8zCqv8DeCciMxR37KjxnRlWRsBSaTSHnO0DJvbJf79nhybWWSROy6p1a1kpf0ZDv_p0ZXpHP72lFFjIlmot2CHPmJ7FowIN2GJiEOxXAOGpTesEm8IOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=j3M83j7aH_ldKHsgK_0nuNOKlTcg1GnopmA8CllHCDEYIRKDrWEkwADrf9dC1RnB3cxBpbMyVq-L7lD16SHPkxUOjYcTkJZ5tUBMKZopjLU1BgaHK_uyO7z5fXEHVFLlisNxKVJVLzgKyE-eqNvj5MpEyRpIcx6orSAwVVszG5dMdW2kGmQJRb__W0KdCA43f-5dAv-3EMCdIHF1ygojTxxda3YuyKbOjZ8zCqv8DeCciMxR37KjxnRlWRsBSaTSHnO0DJvbJf79nhybWWSROy6p1a1kpf0ZDv_p0ZXpHP72lFFjIlmot2CHPmJ7FowIN2GJiEOxXAOGpTesEm8IOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1yWGpmEZ1y1aSrbNQolP2VHqesAp6BxR_S3eRgrNVJl79K8UmHGLGUXZSjxAcufVATTAHwWUC4IwvG43qXBBNH-iB7A5dXCNRib4y4vbJFhQlAFnwgsXohyCp1fwbwF_FfZ965I51Xw2LUQ9Bnr7eW29K40_COMkdFTdU8hKwEUxJwbVBs5daV4oSR1aAoHGn50mx9p_IWYGWyTiu-AtVfBcO3HG9Qs6QeGCtantExtDrogxPZgErWhvyfILxQ25MQnYQLi04ScYaDhxNUzLqU5JKgIGtCbMLxrUo_JyA8WLYZoytJbzFkXon1v688Lypp0wQsH2Td67XN4rAD9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3sc2FnwdXH2CUpD2EX9qoajkiTE8kLfsg8B7vCFiMQqjdjmq2Seb7dBOLNU-45EXyNmPlEIMhHVaekcZdJluRwVQSvPd3iRubc1EWvyQkaILqFjK-GyRtal3sZPpsagjj42AnO1ji8KGyvM5SjQgdM6cMxqDqm-AmeiCOD41bOT_WU6qPPcyym-dtqYC_1t6c8p1fQj6Z9kuXqJ7ohkk-RiXOAPO1KrWOKFryu7jLR1iYtB4JhcIyfdNrzzZdnJ06mN-I4TD33EaKNmLLoX2HwDZbRUQ0Z5Q_XaDqYY3_JBic5ddHi3btn0W6Wku54nzxtTdzX9dDkoM3rxHSeB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=r7T_FzUSZwUI799xr3wI0yeRvDZhC_18e-9vl8zPn-leP2lApH4C4kcdX91M1Mksw3BbCiSeehWMJ3Bpk-IPyQRnuFwSNBfcSI6a44SvlOjyM9SF429gm4O9AP09pvbC4NQ-OJu8p2mrApby5GgoPPb3-R1dEa_FJeu64UNULT7r93UMLFqsf4OYNsXa4xLaQZX__LqqhiEI2qsHpLVdfRYzcpR17WRcYDQhZ_EbVmJindXytQq_t5STkqWcSJfz61ZyV1lE_YPHYfDashGQ9gplUnyKSUxcX31DOIgmjImJ4aI85h6o2htLGvJ8p9Mx0NnPRmY0xuCHG0DLdwKfFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=r7T_FzUSZwUI799xr3wI0yeRvDZhC_18e-9vl8zPn-leP2lApH4C4kcdX91M1Mksw3BbCiSeehWMJ3Bpk-IPyQRnuFwSNBfcSI6a44SvlOjyM9SF429gm4O9AP09pvbC4NQ-OJu8p2mrApby5GgoPPb3-R1dEa_FJeu64UNULT7r93UMLFqsf4OYNsXa4xLaQZX__LqqhiEI2qsHpLVdfRYzcpR17WRcYDQhZ_EbVmJindXytQq_t5STkqWcSJfz61ZyV1lE_YPHYfDashGQ9gplUnyKSUxcX31DOIgmjImJ4aI85h6o2htLGvJ8p9Mx0NnPRmY0xuCHG0DLdwKfFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzHSxRrE8kuZzwX1IGIicmb33CHY3Y25-udy6TOZtrzDOw_pS5R8l06S7rWvQjPwRM8AXAFhs5o503ohcjjC6xY2hI_9tdb25Xm5DtC-03y0vpnlXxFpS99pVKpaGk8yYTpGHp0BDU0GapWEDsZesxg7KdB1mxR3m2e4SHyQJrH76Yan5Xsbai14Np_DMgtca9ykn5M-5KBoDZ_ew2AnXstArQpFexHCBEV-Bs5l2FTCj6e2onHuV6tAubfok-q3l02ymiTtZc_29_qtrJmoLNpM1sZvKV93NAImHD8CeFGqBVzK8ssKngnpwFJoYqrgShEDpBojG63F9V8-7L7xiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QvLM6xtW4xKI6_cki9WsVO0cljkAsscX2JTgDgUlkhFx8bJw1F5YFF4ba_5l6-h1tUxvQkJ4ho9El538J1GT0tUlsB71XgFKtSYHVpRb-TX70siMH854h8JgFvaNVouGuJWJ0kYi0EJartMED_qlUgc4OUgut5GIW2RNPJloBsbAmis-eEYCfYv37a6el2WcGlFlBXWHNkEkuyt6PuQS7h6VT_bFrMJCtBIcLIFXbJVucS3PKOAkAHQYlANjvK6sm_Ks45Fu79F7sFFK6G-AZVBjGcXXIvhxqFcOuRyDw2HnSkryx2xTKC4C176gEOgE5CCmDXvxVkkazYrjaiP0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VczRUdcEufN642_nvFKmr33GOEIsOdvhfU2tbLG4sGg45BvSNF0B_IZsEGXyImn5E1n_fm9RttvzWPHc98Ci4NJXELXsF-N-5oKUUE_bitX06HcAxMtIVDVfq01NnvgVf2FevMluc-bWeF16ad0Se8MuBAINC5CR3_1DHCjojmGKFHb5kvpKqS8EFNYJEzw3e4lsQf1EblqPC-SqlxKva4QdcvVSLgVhPIJ5tTGk4ic7RJAA1hizyP9DAJ_ZJwSvMOhcIfJydBzsX0mOLROeh2vWRALyWqzndtgnYwtChxGeV-mtTkKzvX8V74e9Xvf32IxKoXuk5anqTrLLV8fzog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tRbHCJSt286NwCeGQAC_FJfKa30eVExrQKZsMBfVve66pzg3IkS62W6DvN6a9xUzr0tFq6fkiTyLqZ1mEpX5j1FQ0n-6zMKu3sxV-fk6RdY3kJkv2qMSXXWRloLmV_qJnws7dr33rUTitAk5wwtzwJ620EAVkwDLLqOsVCO5fe0yD0yiAuu1f-pDfp6BltHg_IzabtJKE42NcOG_Jl6vAXUaVveA-WO_smZblFoOAaWQk36wxI71MUuE6QgkZZuSXovFAZ1kHehlQRl9Jnj5m28_2wA-qxTS-qjkeuwctnFzRo-Gh_usCs7blsTiCFqpoAGqeLJvj-tkV822Bya6Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=L5s5CspqlTObB9m1hLhB2XIMjxzj1POj_uAVl2EOpOGxVrCSlqbNfX3IHYJfvZZYvDFiQR25Mm0TBIaaDow4hw4XGnIhTHdWtSffPxUzOnojPCpRb85rnK0JM7ea7n5hvhMOmVVx2MDNs7xn3F9veSNXIpN-N4FnUAHgF1iAWD_t3kmUT4Ksgh61-_SklgX6VIBvbiqyAS7HBV2qydfwt-FEmMloZScgN8Sd1aQAaZkWInB-qq6fL3vQJCw6NGxLU4xPBnbjSdq363hmhV3u9KnXaNYWR5OOmHaMPts3D-jRliAKtSbCuMEjJwgDG9riVa4h6WLakcI8jeIkxIWGog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=L5s5CspqlTObB9m1hLhB2XIMjxzj1POj_uAVl2EOpOGxVrCSlqbNfX3IHYJfvZZYvDFiQR25Mm0TBIaaDow4hw4XGnIhTHdWtSffPxUzOnojPCpRb85rnK0JM7ea7n5hvhMOmVVx2MDNs7xn3F9veSNXIpN-N4FnUAHgF1iAWD_t3kmUT4Ksgh61-_SklgX6VIBvbiqyAS7HBV2qydfwt-FEmMloZScgN8Sd1aQAaZkWInB-qq6fL3vQJCw6NGxLU4xPBnbjSdq363hmhV3u9KnXaNYWR5OOmHaMPts3D-jRliAKtSbCuMEjJwgDG9riVa4h6WLakcI8jeIkxIWGog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=XNu78zfIz29sVCST2-klJ3PK1FacVxNJqiGhEgtdNWtbipR_T8Gd8WAt4sJuonV2nms-Hn-_kQKa3_zTe4AZQKnPG6IaLesKS_2GlLFgUxyyn7RbTya7QiQPeCdQLq2Qi9NJmLkLR66sU2MPhImDLSPt9VT3hLIr22p40VuV_qdUC8Iqb_ALgn_aXLokv7tp90qK9vCj5ihkx_jaHcZVbDJ0ydDck-C5f-R4r3h5BAS3TcTiVH_weKqO7F5T2Bwl2jslxGI-RtTjGVIEueLDJYIjYbSfBmTFTvp1Ivl6-J6neBzeQ-3FV4h-3oY8wrDALBi7QVQv8Cee1NVUUTb1MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=XNu78zfIz29sVCST2-klJ3PK1FacVxNJqiGhEgtdNWtbipR_T8Gd8WAt4sJuonV2nms-Hn-_kQKa3_zTe4AZQKnPG6IaLesKS_2GlLFgUxyyn7RbTya7QiQPeCdQLq2Qi9NJmLkLR66sU2MPhImDLSPt9VT3hLIr22p40VuV_qdUC8Iqb_ALgn_aXLokv7tp90qK9vCj5ihkx_jaHcZVbDJ0ydDck-C5f-R4r3h5BAS3TcTiVH_weKqO7F5T2Bwl2jslxGI-RtTjGVIEueLDJYIjYbSfBmTFTvp1Ivl6-J6neBzeQ-3FV4h-3oY8wrDALBi7QVQv8Cee1NVUUTb1MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHJoEk5NtWfGucoijDZpsM8uSWMDCgGeeEjvHQ1EP8rgxz09oTuh1Nbctd716ZE20yUsEhK8fgDJGi4ABq6yiBp_SA6zlhh9Z058Sn1I7W3N2TU2SC2wkJQM39iteZIqNBgzUFsU_mivGIMuNWqyXeBRPMzo3J826A_p-tHwyMlMggiKGM_O3z1H_Mcz_WkWFYKZMBKDBAAGRxiWfevSxE7mMaSrADA9dExBiR59UH2gmZa5DxeCYyXW8xxVWLx9_FSGvpNltsm2kanpP-4gTZbXzQSnJ_O3VJWTh-J2Cjf9NgXEzjWZNd3R1ou_mG8ppUqvVEcBWlZWcbCB-WSY9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=ehogicuVO-snWV3HiuYt8sLZJkcSjPf0-fsdLZ2a2fZJyVVQo3y_0WZRCbVVQe2IREatAsTNEucKNtlN8DutJaHXm5h9J88wihCTOr_ul3xV3Z1UPoJjDLiFJhas0K45p5OzURYSZWgmmtAbStYEvqloFnpshh1zaxQrdNqlTeNqJBiJ_E0VDCygc_KUC_RrlQt1eiUgpPy772bmAkYNa188VVq7BRgWsNGnZCwXodj4rePxvrbTeJz-FixWP0zKkkBXWJLbyb7q06lMoeBPb4ldqNnbOCMpG3Rvltw0Y5QXO1lWoTW1uCoctIhbD7sj6oHSUP-69zFJ2MWWhfUx0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=ehogicuVO-snWV3HiuYt8sLZJkcSjPf0-fsdLZ2a2fZJyVVQo3y_0WZRCbVVQe2IREatAsTNEucKNtlN8DutJaHXm5h9J88wihCTOr_ul3xV3Z1UPoJjDLiFJhas0K45p5OzURYSZWgmmtAbStYEvqloFnpshh1zaxQrdNqlTeNqJBiJ_E0VDCygc_KUC_RrlQt1eiUgpPy772bmAkYNa188VVq7BRgWsNGnZCwXodj4rePxvrbTeJz-FixWP0zKkkBXWJLbyb7q06lMoeBPb4ldqNnbOCMpG3Rvltw0Y5QXO1lWoTW1uCoctIhbD7sj6oHSUP-69zFJ2MWWhfUx0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=V_rKep9nEX4VHPpP3-ZQJiDO49Om8yVPXdeKKuAErpAu1WWMcul_OWILLFkkqKBDPFNnF4h-Y_9q_8qX1LsSvTMbSzwhaBenTaFO2DPBPtiff-9VloRklxfM9nxXH56POocXivFPJtyYv2G_Bm5krlRCOHkD92iIMr9dbyhobX47aP1e38Z_OkGJpkiMxKe76ViYQNA7A7M5hOK2O_cvyy6mHFI7fwllc2r5XzJQcYL2czFgZ1d-HZbtdxU1I-VaNh4NnKkE8QVrZRDhFfRE2g0bpt7QD5l8T2Cgzw5wghLSgY_eQnQRQ9ZlsPqSeo_OT8oav7R5dwrVdXRyev9OTURy-vIGVLWVcFhKrKtY9rz_k6kn01w18lj-41cQskDrmwoLYV4WG0SaeqobGadn4PUHQz8yet13S9w8e9DXmCx5eWz4N7T2a_muy0969gRHExDUwRgU2P1Ot3_c9coy4Igr2jfr-tbrJJrMqBNcy7zFBFN4aH4QTw5K91-05FBZ1Mse2DqKbsaL89N4jUbBHHt6Fk9uV1SXu_-ijWY9zI77rCE9XqMxYwEfk4N6FqHmgTtd8wzDgP1bQl4IR0cmubUXAqgDZ2gfTrOTRzvj0w3EghvITkzgmUSr1COj4lLyNm2KPlNDueu7nUQb_C-_KbnfMldoWoF7bj5-nCA8hZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=V_rKep9nEX4VHPpP3-ZQJiDO49Om8yVPXdeKKuAErpAu1WWMcul_OWILLFkkqKBDPFNnF4h-Y_9q_8qX1LsSvTMbSzwhaBenTaFO2DPBPtiff-9VloRklxfM9nxXH56POocXivFPJtyYv2G_Bm5krlRCOHkD92iIMr9dbyhobX47aP1e38Z_OkGJpkiMxKe76ViYQNA7A7M5hOK2O_cvyy6mHFI7fwllc2r5XzJQcYL2czFgZ1d-HZbtdxU1I-VaNh4NnKkE8QVrZRDhFfRE2g0bpt7QD5l8T2Cgzw5wghLSgY_eQnQRQ9ZlsPqSeo_OT8oav7R5dwrVdXRyev9OTURy-vIGVLWVcFhKrKtY9rz_k6kn01w18lj-41cQskDrmwoLYV4WG0SaeqobGadn4PUHQz8yet13S9w8e9DXmCx5eWz4N7T2a_muy0969gRHExDUwRgU2P1Ot3_c9coy4Igr2jfr-tbrJJrMqBNcy7zFBFN4aH4QTw5K91-05FBZ1Mse2DqKbsaL89N4jUbBHHt6Fk9uV1SXu_-ijWY9zI77rCE9XqMxYwEfk4N6FqHmgTtd8wzDgP1bQl4IR0cmubUXAqgDZ2gfTrOTRzvj0w3EghvITkzgmUSr1COj4lLyNm2KPlNDueu7nUQb_C-_KbnfMldoWoF7bj5-nCA8hZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrTeGAAsCquZ928A7CRkT-atMVQ5tHR43eOsq0_tRdowCknIHBum7Mzuj8uNlKp1Q4Y-lRABk-Awyz2VLioLv6juZv3oxgTsMvWF3Gts-ZWdgIrwrwhTJLV9MpnUiTBWuDwSmm9hg9QcPXvActW2aXNVRdxkzAHdEu8UhqmS29ZMxy48If-OeHyF5RHd20KYSryUPKm_NTltipBysBBLhKF54YuuhXlJuoFvXjg00c0JwZTcegYOOXskn4AdHzO2uZMq6Jxl5XSDxgNIZqCAWw-jFXk-kuSPBASdxvL037hmEQ13GOkniQRBY07os949CzGPpmfafGFuCQhwZBe53g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxzWSeu0k3lG5o4_uygT0vzhtLubhsiNXNHvVAM0SZo3wSF-ksTvmk-u0OlIt2rxnnNtbk3xfIYCiLQU5-GTX6GBWjPJk7J76CCZ-jrOF58yOAT-p73tb1NOJvCRi8Uk1Mzwy3y43gUCVW-0uGXnYjildLuhIK_FpI8qgBsLCl-NKrWDR01gw8-QHNPsccgWOOP2vcJzpDN4G1mphPUiLVdnbxD6Y7bLmemRjIpQRqoIVXFeKjim1JoJCB6uDwB7toy5AZqcoQSS_otac8y5imkDUP9P2c9D-Ru_YbiJGaGPQnP1c4qxFYEGXem5M1GtlESEgB5YL8HA4lfJxrnL7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIET25OUQeY5iBFpVeLBfs9PcgpTwMF3LLMzUg0b_ZK1TAJ2UMfddQl_HfLzeAZKTqKwSTyMc_MW2KW2wjaTqO3IIy8VFOT_jOhlhh2SZhgLlehmMwePm557SLHoR9dtQQ__YkbeO70RO8TtWbzzHsLjSRbndfj2oGvY9oV2BQ4fZiZWuhyy_CBmZbAgdnjiCqyqeNitOYIfhBmldFxYvepm1dtRtppMxMl1PCKDuT2rNgr-i2KztnAeol8wUoZdZkiGT_wOETUHZbfeVsonH_VI7ghckMLurD7w1f2v_L04QJz0oS223Tm3kHDH23nXOJzCfod7sItlBRJt-j0CMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7l7CQnUOFDXNgFlRes4OJ_CT8rhu6-UMSn0n4fcYd0yahBwReHM4zPwxlfFeMKP-rEAH4G_uUoLMb_IpgVxOByQjrpHRwICjpglYD_vY1B4kRCnp1ANNGzlK3VWVk3k4wgYuT5CLq71HV-Ns-xeTG13KTfRhUEpdZgp8RnOnNkZujFiJ7n3DUrnMQPulFVY9cv8ja9xxC4cY1-iFgvaE0xqU3cA5Ygs9vPwyc-5o7E7S_3CHIgiRrXJWNo-jOdj3RqIOSU6MaG3lM0_Kz3u9Q2AWYTP1XdlqQKoeKMIxkIQjSDdSsjL-fhWce6cBAL9tr0IhJLZAMLB2LSvnjuoyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=lwiMRGOIoWWF8hOeKAQtqzn7OgjqUBVUVbgmsrS4VuMJGmSQoSzzDc8ywcMr0tswyb50T712uDReeOcawpqCM4omR6P8peCCQA2wdTZSqqJZ3sdmxDDu-BNMpWTaGU-R9kZ7OzxZ3ny-SHHlfnhfRQ53HXeM1oUtILRuPResO0Iip6ljb37QmvT8i9hjd1Ct3SJjKSrMcgvChq-XZ-vFkvjRa1okqlBeadcbqTx_KZIz7GH7CaJIZSRBDv7lNwJwLIiTp9jFI_KoyqHRO_5y-dgJ-N0Buh1DRyeTReef69jD0UvjD1LWU82l8cCZvSJFW6NI_pl4eRqMstdEKhSZgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=lwiMRGOIoWWF8hOeKAQtqzn7OgjqUBVUVbgmsrS4VuMJGmSQoSzzDc8ywcMr0tswyb50T712uDReeOcawpqCM4omR6P8peCCQA2wdTZSqqJZ3sdmxDDu-BNMpWTaGU-R9kZ7OzxZ3ny-SHHlfnhfRQ53HXeM1oUtILRuPResO0Iip6ljb37QmvT8i9hjd1Ct3SJjKSrMcgvChq-XZ-vFkvjRa1okqlBeadcbqTx_KZIz7GH7CaJIZSRBDv7lNwJwLIiTp9jFI_KoyqHRO_5y-dgJ-N0Buh1DRyeTReef69jD0UvjD1LWU82l8cCZvSJFW6NI_pl4eRqMstdEKhSZgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZcqHxOrBZL31TJl5LsAY4Jr5NQLB3tDpKV8EWgXibITrggpOV7Kf0WtpSlYKTNJzgzURdXRr-uMGqnwAazbXhWngf1hSzE_v-Q9sRx0xkMEtrBQV3Ccto_JlvBAr4Y5uuMrGkkn7imNA8kn8D21P3pFGz8lmLEAy6dYxavzgVGnnunIcx89FW6ptvhjtr_Rnx1eT_s6iibHByop0pptt6S64wox1NZd_mf6X4bROucFW6NUUebNXPWDkjDwSjhZ__BunlU5P-VW4Mg4po1UXAQT-5GSi8a-h8YM2akPRSwl0-VxkDYgPSZmhJjqCUZQctdtWfeNZaHAw73MpJIJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqVNxJ8df8fYcMpo6wapE6ZZRxsNcsPfkhlaVjoYt0ZUMa0Goug0CnowWOsF206QlEE1qgmy0dyO6m-MPWwe7h1hujTX8_HgIcz6ij_A_sD_dALJjmxDKhEGQb-hsRj4gWBBhBAfNGDiaQOZKeCt59TJEmv_RDgz7vfp9xaO5jR7sFZijDED2qjKVNrPa96ZOH4ZRzeNZEuQ7KItIkQfPoLuR_DV6ocj-vSTpjt3ZAHMyBgUbADv_7UUHqNzPE9aeK9sWTc8xvhB3iUtZ_uf9j_F-bWqeqHRVhVJv4Lb12Llo_0qvGw1iA1Nv6LMDyKVqtLpXUzMrN9WKjvQoP5emQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=CBVv1K3jyefHP0-LA5G66Kk6P6NjBQ6LR-xuu6c20E0c9nrbcm_atWWvRpVEykw5isdp1VEvRsl5mI0uRmprULdvnbGHNI1DtG2YPkW_qiRQPByC2O_zFtZCIujAp3mAPakdlgLA-G1FdP8VaEcWU1qS4Ax3L7WiqKYvGRE_vOGNprRarEcGDr3SX-vXkmPc0Tb6FEDDZ9vzvp7U2xT6VQEKrY8S4ql535lxwAdL5aXLfq_RTbnWSn2oEj15-4KDHqMcy9mCF85SNbDT2zF5JXVI6tRPbcZA19rS60lz0iKP_GLWodXPyF95eUJpLRKdT26265WnsanHfTe-kkAsnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=CBVv1K3jyefHP0-LA5G66Kk6P6NjBQ6LR-xuu6c20E0c9nrbcm_atWWvRpVEykw5isdp1VEvRsl5mI0uRmprULdvnbGHNI1DtG2YPkW_qiRQPByC2O_zFtZCIujAp3mAPakdlgLA-G1FdP8VaEcWU1qS4Ax3L7WiqKYvGRE_vOGNprRarEcGDr3SX-vXkmPc0Tb6FEDDZ9vzvp7U2xT6VQEKrY8S4ql535lxwAdL5aXLfq_RTbnWSn2oEj15-4KDHqMcy9mCF85SNbDT2zF5JXVI6tRPbcZA19rS60lz0iKP_GLWodXPyF95eUJpLRKdT26265WnsanHfTe-kkAsnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=BTHxDG23juNgzUOkXgfNaufOd-WStgb2rKI6C94UXdeYrjpw-KZXQMBJmOcduLr2B-4q_FtxMeZ0r35dxyv6wE4l9ftiLwhnQBC7bLm8Q2JyB-_dm2Rd3s5F7TIb5R5s3DqEgUjkJQJBv3KM6b0OkbWjAmRFZsrX4829fnj4OFM-N0iAaFJNHymlWm6G-lmBzLOwpdVfdxG05OQibW5BAKSnUSa_Tgg-3FMuYGxoBjP3OxMydssjdoM4dfS8fwbJ8LHFIbD-RFdI2JQYHAall6aOtFC5xVIlhqWJ8acGYncA_XdMgRx7NU8Ic87mjIlT_VBE0ta1mEtBcra0K33oZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=BTHxDG23juNgzUOkXgfNaufOd-WStgb2rKI6C94UXdeYrjpw-KZXQMBJmOcduLr2B-4q_FtxMeZ0r35dxyv6wE4l9ftiLwhnQBC7bLm8Q2JyB-_dm2Rd3s5F7TIb5R5s3DqEgUjkJQJBv3KM6b0OkbWjAmRFZsrX4829fnj4OFM-N0iAaFJNHymlWm6G-lmBzLOwpdVfdxG05OQibW5BAKSnUSa_Tgg-3FMuYGxoBjP3OxMydssjdoM4dfS8fwbJ8LHFIbD-RFdI2JQYHAall6aOtFC5xVIlhqWJ8acGYncA_XdMgRx7NU8Ic87mjIlT_VBE0ta1mEtBcra0K33oZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=NCOZmitt65gpQWZvNH1RA-6Dwlld7FcVQ2K6wEYYYlh66JRc81l447e3ssgh9prMpraVjqL9QXHh35MPCfv7b0qYkdKl6E0LWm0RxLUEiqWOoY4I5vIjSL5VVEAm0v41TlwmlPC5CxR1BJ9IR3YNWppJtCO2Gx8fE18J__h-8nbumGhMZmuI4fJTPhJmqOiYw-wmRRSE12H51JRnRWI8GcTSBD0QHwSi4Ycq6vQwMBPq_57o0cKOUrKY31FZa-fa8XgXNB36RJQGij3okLjAT0K8pUo_dAeQRRZITMo82MErMlX9B7ZW3wNMTcDbWRXz0707B-N5rDAHWHlXyW4mfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=NCOZmitt65gpQWZvNH1RA-6Dwlld7FcVQ2K6wEYYYlh66JRc81l447e3ssgh9prMpraVjqL9QXHh35MPCfv7b0qYkdKl6E0LWm0RxLUEiqWOoY4I5vIjSL5VVEAm0v41TlwmlPC5CxR1BJ9IR3YNWppJtCO2Gx8fE18J__h-8nbumGhMZmuI4fJTPhJmqOiYw-wmRRSE12H51JRnRWI8GcTSBD0QHwSi4Ycq6vQwMBPq_57o0cKOUrKY31FZa-fa8XgXNB36RJQGij3okLjAT0K8pUo_dAeQRRZITMo82MErMlX9B7ZW3wNMTcDbWRXz0707B-N5rDAHWHlXyW4mfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=b6ZSxvRyzVGuJWhpnKmumjryOQVRhwQu12EultfArGZiABL2Wd1y-7MoenyFuh4-GkfCU19DvPnpRhhCs-ZFpOcDOGQXYZDg794gcIgPc1X9ZBmVcYNN5IHCghVvgpXs2BNeceIm2SY9DYTg8PP9vR1H2S3R5lUc1u3HJTP4owpCkrG2P8_7tF5pkNZ_zskJZLw1igoXo21KZzPCThIymyC5LIbm4cRiTVOph2As9sS9OwmY-XNW_zRShi8mle798bzNtL4OAeDcMQivF20m_46Q5lImKFz85QZdiUyeK9qwS6bRp0ewIBaUhBPHJP9lIXx_HjzcJTUibyGRP4VZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=b6ZSxvRyzVGuJWhpnKmumjryOQVRhwQu12EultfArGZiABL2Wd1y-7MoenyFuh4-GkfCU19DvPnpRhhCs-ZFpOcDOGQXYZDg794gcIgPc1X9ZBmVcYNN5IHCghVvgpXs2BNeceIm2SY9DYTg8PP9vR1H2S3R5lUc1u3HJTP4owpCkrG2P8_7tF5pkNZ_zskJZLw1igoXo21KZzPCThIymyC5LIbm4cRiTVOph2As9sS9OwmY-XNW_zRShi8mle798bzNtL4OAeDcMQivF20m_46Q5lImKFz85QZdiUyeK9qwS6bRp0ewIBaUhBPHJP9lIXx_HjzcJTUibyGRP4VZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=WNhvSUND2MkWQK6eqWYFlcH_n-7E0_y89AKspHZgDAzz7Z20t76aCSVom1TZNbEV3R8-UZ9IrmEx9-OADpBQeYVvDFrjK4vXxZ1DBsrnxz-Ypjx6DbIMDIv00RNEpjCF5MK1YXMBsd7Gwfu-eQCRnBy_-XaSNAFFzbOqnqvr6zsuiIQIJMIkzjk7QwWLdcTqLdc-JqOjpwiL1VDGZzmMaiRRF2hVoe3hN2G943vz7Ro1B2wjImJ6oGWHnzF-804tYa8K5yBGfy3PNj_O_WKxZCmO0UI7IfmOR4KmGdPgVldRvNxOWkE-HMFrxtRXqwik7EMp1zpBu_xVBe5-ZlN0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=WNhvSUND2MkWQK6eqWYFlcH_n-7E0_y89AKspHZgDAzz7Z20t76aCSVom1TZNbEV3R8-UZ9IrmEx9-OADpBQeYVvDFrjK4vXxZ1DBsrnxz-Ypjx6DbIMDIv00RNEpjCF5MK1YXMBsd7Gwfu-eQCRnBy_-XaSNAFFzbOqnqvr6zsuiIQIJMIkzjk7QwWLdcTqLdc-JqOjpwiL1VDGZzmMaiRRF2hVoe3hN2G943vz7Ro1B2wjImJ6oGWHnzF-804tYa8K5yBGfy3PNj_O_WKxZCmO0UI7IfmOR4KmGdPgVldRvNxOWkE-HMFrxtRXqwik7EMp1zpBu_xVBe5-ZlN0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=uNsq8S73bMH1hm1W-2RMzb133L-fwVFOxg9AOGX3NJdbgj4W1Jcvw07OwTVUI3YLnyMIT0xz_TqCIoL5vq3dK5tm2rvm_Z-sEkaKLlcqMyupLdZW-0Ev1HsFUfBpO54xL2YFxUwp2QfeLhysRd0Mo4QrC_iHxocU5T_Q3_RibtwLZ2ZUvp7ONHPYdOawqzOEnuTozpdn3KNSJiPmuV0d2HOtCYP4tMA0DiEm2GISCTwBQp6QwE95zYWDturreenZ2N1n1Vuxki43ubcJo4NTMCx1ATASfIS7xzFXGhJhoTbQQ2kUlIBPb9v5LpVaOcmzvD_YZLF8OtGFrMiRTrpOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=uNsq8S73bMH1hm1W-2RMzb133L-fwVFOxg9AOGX3NJdbgj4W1Jcvw07OwTVUI3YLnyMIT0xz_TqCIoL5vq3dK5tm2rvm_Z-sEkaKLlcqMyupLdZW-0Ev1HsFUfBpO54xL2YFxUwp2QfeLhysRd0Mo4QrC_iHxocU5T_Q3_RibtwLZ2ZUvp7ONHPYdOawqzOEnuTozpdn3KNSJiPmuV0d2HOtCYP4tMA0DiEm2GISCTwBQp6QwE95zYWDturreenZ2N1n1Vuxki43ubcJo4NTMCx1ATASfIS7xzFXGhJhoTbQQ2kUlIBPb9v5LpVaOcmzvD_YZLF8OtGFrMiRTrpOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHDN-3wU6OEzAgjfx-WhGZe1cG3uKvYspyZF-Ish6gcqQ6QI0i_RDox-1nqAKknRJYl7oKC7Nd5d5OXyjmu1WDRYNHLg-e_ZItzL6ZENDld3i8_cd_kBR9UgfsUrlW4wmuTBfvPSA6_Xs5rl4vDjeBJ2VayKgxiCbv0jeLnat3lPtmBPn1BTipIlW4qvHHmJHmT07jn6ov9hw2EgFuJe4d-yWOeW1AytV4tH8wqVtBDPF_kNZa3IiK2KZq7_kpGtUfzBLPJKtg_ePETrJDyHmrF0mGU58POrY_yRHFlZkpVPBX1vl3SpJv9_u8geeKHJvB5BSpcdWwp_Vqc51AfsaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etMfHr5riNR6mDAXZZWCdYL_d-smF8_IXbnWL0tmi0J8cikjCBJ9vy6oGI8vRautqcg7HSMqWbe7QhOQIrrlcHLntJ8FdTlGrog91JNbRMWg3o0xSgy__hIq1dgYalIbRcSKgAAHvzJmS8-zhV3D2wBSsA8ndKAuz-kslsE5Bvry2DXliqmtpFBh-Ni8vjkJs29-6VA9neR-0zSHwtARG38ts78xrqGxhptIzSzdtkXp9YZuNqauClvSqIA7qF6peE-erFrPuMO0sAjwWI3Ta2T4vKWoOhLP7PHTcRrjkiT26qAX44bCZUVOElFigjs3my2asmXF3vTWhtj4nTKlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiqRyRNQcny6cn7Y1Ue-u2iHKhtpKNBJe4yP_I5li1QaQXpnlaKbhXwWGgQKCdnP9zcbL_4r5ARVeImqtwmMqM-bOB4AnXAanf35f-Mc9EO8iFhOg7PH0Rv24R2eJE3WVH5Z-9HlyYLCK8Vo9a14F8cg8QLgnd2P_SonfSStLKXfKMNuz8o5laHI3Ro1wRba3nRJreXz5tS9klbKplnaWtiKJCHV88pLaDtlUddfpYbJRJJHucaTSqCngp8YqE_LdENgPeuZvky38mNHIh5ESjsskzF_MeqVfnoiD1DD3Eh7kMY-EpDCO_Cb1KfNmLRlaMmSTegdx47g4NHYrcU-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=PRTRVdRx0lJlo21sQYEev624WyxaZlql35Qht4eotsPS2y4ITP192AlqZ0g2ZQY9uZ1jBgYGoaOYODfwKNNblo0befXbqamiesTSIRgS71FEqIrIYEICAphQJNB-TC8NBeoMTWkPZErxoz9z9gNXLUa8e6DqqucFV2KIR37D8rJ9B7ocZAqJWcQ0PaYpDn6ui_vSYJ3z4tvO67G3ye2sk1DcDiEG5njBr8_flFSAdE-CUvzndXNeP1j4BggGUwbD6iS7zu78yLJhO3_OPvPzJpmaoSkjnJRLkJ3cbn4aBmw1ax5sMXxE2w4uqk7InrUweCDGBQtIYpmagPIsDjCijA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=PRTRVdRx0lJlo21sQYEev624WyxaZlql35Qht4eotsPS2y4ITP192AlqZ0g2ZQY9uZ1jBgYGoaOYODfwKNNblo0befXbqamiesTSIRgS71FEqIrIYEICAphQJNB-TC8NBeoMTWkPZErxoz9z9gNXLUa8e6DqqucFV2KIR37D8rJ9B7ocZAqJWcQ0PaYpDn6ui_vSYJ3z4tvO67G3ye2sk1DcDiEG5njBr8_flFSAdE-CUvzndXNeP1j4BggGUwbD6iS7zu78yLJhO3_OPvPzJpmaoSkjnJRLkJ3cbn4aBmw1ax5sMXxE2w4uqk7InrUweCDGBQtIYpmagPIsDjCijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=ZL5niG05lBaRxDHi3zmgRtSSywXJ9oVSA1HhDyL2qi3iAUDLh9qvHE7uPZms58dO2MZwQXSN3j4Zl6u3CUUtDKoa7d6cdy8NvRRv9bYUV9Y6kZmzR9b2ZQeeXTTw7AgcAiY4vdkJnODgPPwVf1UyJlIJ6kv3Y5v07e6WQfKVtKplCo9SkeLJGPRlZFYvTXuZ8xmvaHoElGOSeVJQjyIk39CcLjDGbrAKWIueak-qb0qI_umsjzuTq0c0tybmJXtTaGjpOYiSOBNlxXjx-wFls9dzyHop_a8t9MaJjDM-JtvsjRMeGvVpngtnqF2KG3TtV-tXunHkt-SBEqgEIVcg6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=ZL5niG05lBaRxDHi3zmgRtSSywXJ9oVSA1HhDyL2qi3iAUDLh9qvHE7uPZms58dO2MZwQXSN3j4Zl6u3CUUtDKoa7d6cdy8NvRRv9bYUV9Y6kZmzR9b2ZQeeXTTw7AgcAiY4vdkJnODgPPwVf1UyJlIJ6kv3Y5v07e6WQfKVtKplCo9SkeLJGPRlZFYvTXuZ8xmvaHoElGOSeVJQjyIk39CcLjDGbrAKWIueak-qb0qI_umsjzuTq0c0tybmJXtTaGjpOYiSOBNlxXjx-wFls9dzyHop_a8t9MaJjDM-JtvsjRMeGvVpngtnqF2KG3TtV-tXunHkt-SBEqgEIVcg6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=D-vGzHNma1T_kzvwl0KxLtDx8FxLCIJ8umXrBtcy3egq43GMRDkEOjTNYBkVAyQ3m4f_ooFeT7jvbRcQGbszl8S-GhcdfqO5gosMrqL8wUVWNTn_7BB7ISotvPYvj-s-vecfO2lNU0b34rLg1mqVB8PX_SGuda2m0RVwyVBKj3PjnzAF91XUb-VqCSVk2v73JDkAIxdEF4CSd9Q-TQDZ5_zEvF_UyvDVcx4Qb0w-3p5-s9iNdsmu5wp3tzaRCt6n2kMsXRrq-7SNBZ2_C-M5-ZKQudKYe8xuk87Y3qgmUMq_v-86a8l2HuPF9SrCtsjbkLrw3HzLGTuMfj12h-B7bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=D-vGzHNma1T_kzvwl0KxLtDx8FxLCIJ8umXrBtcy3egq43GMRDkEOjTNYBkVAyQ3m4f_ooFeT7jvbRcQGbszl8S-GhcdfqO5gosMrqL8wUVWNTn_7BB7ISotvPYvj-s-vecfO2lNU0b34rLg1mqVB8PX_SGuda2m0RVwyVBKj3PjnzAF91XUb-VqCSVk2v73JDkAIxdEF4CSd9Q-TQDZ5_zEvF_UyvDVcx4Qb0w-3p5-s9iNdsmu5wp3tzaRCt6n2kMsXRrq-7SNBZ2_C-M5-ZKQudKYe8xuk87Y3qgmUMq_v-86a8l2HuPF9SrCtsjbkLrw3HzLGTuMfj12h-B7bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOpCRNfTLcyp-FhVlClL-KZM-0NLKU2_w3oOUzb2IrO1PV0XJyB3BIZOUBFqDWFi2gH0xbXJs-_KZ-fuo5LrZ3UyW5Th3uP0RtfNFE-QbZPzuvAWkmOxOavktBl7A-wkqpm0_9gfTD382y210rwM2Ctc-Ymcnslt51iapw2oGMvUfVF9YL-wADCQhNFCX9UIiy80Rw7Y2Xriqr3n7EOXtl85K3ia1nnI4dxKLaJWNES2XvKnnZftYURNQupdFgrKkqzHWlncGOCz7ArlU8h3NVqjTgUV_HttK4-ZrmRBgyX-1CVN4eJP7Z5sqQrQKKV9DrVnl3DEt3vw689WfHZ6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Fpp-1RJfi5EhkhIGWJ1Mql25kY634KJIbWV7FMkgt6QplwTVlN_nlbaV8n1-4QN6MlOpEeJBZdaf1jeNyP-A56US15H5FLkdT4l1c8Gjh9XAUqSrIhBsC_k9UIbWq9HbTZtEchN6oiqUo1HvCSYs8qbtMP7fapz2ZnROHeUSkmZh5FnHpPGfOmnVmySXQKdFaqN69DjFEMt0dKY2CFFgMAtmPt0SFQWoxfMWLbCfBnAcGtTcxFt-llEz2Iw6P3mMPGBfGpgI6HELA8byFzky54i03zXVHG9Hrb3xAJZHuboVgPR1AkLDLnVNT14PpmzZEZV0wsbXogElsCC7LBgdIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Fpp-1RJfi5EhkhIGWJ1Mql25kY634KJIbWV7FMkgt6QplwTVlN_nlbaV8n1-4QN6MlOpEeJBZdaf1jeNyP-A56US15H5FLkdT4l1c8Gjh9XAUqSrIhBsC_k9UIbWq9HbTZtEchN6oiqUo1HvCSYs8qbtMP7fapz2ZnROHeUSkmZh5FnHpPGfOmnVmySXQKdFaqN69DjFEMt0dKY2CFFgMAtmPt0SFQWoxfMWLbCfBnAcGtTcxFt-llEz2Iw6P3mMPGBfGpgI6HELA8byFzky54i03zXVHG9Hrb3xAJZHuboVgPR1AkLDLnVNT14PpmzZEZV0wsbXogElsCC7LBgdIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=v_aoIlyUNd9jNGdLNcOfPeXSymZeVvJBt7QOQMp6gZ_p-c6EAIOeC92oAR7hmEQMZlF7liH2HjUGcrnyjRhbGXTEpvUy-IBe41XE7L8RPaQ2xVmRFdKOqklksjEryYbxzxNzxiNrBZOzGpuKGzINFg3im-I0L56oXAVA1wknojz5j1iPZoZwW9GAhYm1JOm1e8o5ewmtmkQrqdyevfklDi2HhPAZZG-dFrJ77y3r3BdnssAD0Qbdzn-2eBe93cP2JNoNhr20PY3kcgP3QIk0Zm0bNludamktLrbdNoeSPp73uqHoRvW7vmY85BjAOnKfXb5rw2y8BLcpODixmYlpjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=v_aoIlyUNd9jNGdLNcOfPeXSymZeVvJBt7QOQMp6gZ_p-c6EAIOeC92oAR7hmEQMZlF7liH2HjUGcrnyjRhbGXTEpvUy-IBe41XE7L8RPaQ2xVmRFdKOqklksjEryYbxzxNzxiNrBZOzGpuKGzINFg3im-I0L56oXAVA1wknojz5j1iPZoZwW9GAhYm1JOm1e8o5ewmtmkQrqdyevfklDi2HhPAZZG-dFrJ77y3r3BdnssAD0Qbdzn-2eBe93cP2JNoNhr20PY3kcgP3QIk0Zm0bNludamktLrbdNoeSPp73uqHoRvW7vmY85BjAOnKfXb5rw2y8BLcpODixmYlpjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJhYx_Jp_S8whTZK3I9UTV908xXd-0JpdZ8Nq5M6fb1X_-GIWTaegvVsXfxcF__I1QNfbgAhdkBvwhjDE92yNfX2sjIC_pYIf_GCekSQxNM8OLtsZPY35erwFGefo045Ql1SHzShGiVQsltCG3zq0Xu-iiryc1M3oQ4j2CXd0s_X93vgR6Ubi6S6Ys6htbApjhXDYJUu6xSF_lO38WZ8CSiSeT4vvkcqyBjboE8YuPSHqjnoqJvt2cz9GWqYoFtvqnWD0vt8aTFsTHw20pfIicyjfN3L13iEtE0sjDi8svPIwJf5kw5Q8MoLFFAqtX6fvsere-r0IX_Me7fNo7fAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=ZgDKYjdef7GV0Uxk5HRNfys3CUZVKhV-NjHvCa4uYnC2V7e24a74lvCTplCrA26Td34_pX-BURKczpn9UdmLFeYeH-zVcBNC8sHZQJjcZIrBc2Tg-l3yFBPwSfc04IQaP5dR8HNcuk1bGgyJ1tg7Mo4wHJcDulW_eQcYiAPPcrGhpzcCI8GY0mWl1haOkEwabcH6W2Xgri5FcnwVCdWLGXoFvdl16D5HNjkU5--ficxh_59fEAnMUhC2-T4RpxoFXJgZJoxhO33detvcLHv30doFNSder_h9usrsZIuQqV-gSsWr37BrWS0Ko-SB7ExIZzQkEl5clIuEhBCEru5Fpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=ZgDKYjdef7GV0Uxk5HRNfys3CUZVKhV-NjHvCa4uYnC2V7e24a74lvCTplCrA26Td34_pX-BURKczpn9UdmLFeYeH-zVcBNC8sHZQJjcZIrBc2Tg-l3yFBPwSfc04IQaP5dR8HNcuk1bGgyJ1tg7Mo4wHJcDulW_eQcYiAPPcrGhpzcCI8GY0mWl1haOkEwabcH6W2Xgri5FcnwVCdWLGXoFvdl16D5HNjkU5--ficxh_59fEAnMUhC2-T4RpxoFXJgZJoxhO33detvcLHv30doFNSder_h9usrsZIuQqV-gSsWr37BrWS0Ko-SB7ExIZzQkEl5clIuEhBCEru5Fpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=Gnqd96XZ43tsvksKFuB5eSNUBq1ldLkRfPBaHqV-BnSEuHTXJ1rCkkec1djNlIrlN31-rV1YlVsuz1zzXsK_n2vYFQVxNwuOTGh3rJRuDSp1xkSlgt05UEnDGDJgPNWy_INyZqUKZdcHD9IYIJHWoE5AE4PnbmwZ1bVUQLlloOkJ9IYtDfJsRWaVrQ3b3xoxtcElavMUeDZM59BozgkqCEKHxcag54UfF_sQMODewNkBrdY92mhtM9TVAD7I48_ixArK54-z7BtQx4wX8UrFDUVgMBCvsLjYvZ1TvsVmo90gmIGUzmuyNFF1ApAtcqa8h69P_pQCF-V3p_Q_9c4oDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=Gnqd96XZ43tsvksKFuB5eSNUBq1ldLkRfPBaHqV-BnSEuHTXJ1rCkkec1djNlIrlN31-rV1YlVsuz1zzXsK_n2vYFQVxNwuOTGh3rJRuDSp1xkSlgt05UEnDGDJgPNWy_INyZqUKZdcHD9IYIJHWoE5AE4PnbmwZ1bVUQLlloOkJ9IYtDfJsRWaVrQ3b3xoxtcElavMUeDZM59BozgkqCEKHxcag54UfF_sQMODewNkBrdY92mhtM9TVAD7I48_ixArK54-z7BtQx4wX8UrFDUVgMBCvsLjYvZ1TvsVmo90gmIGUzmuyNFF1ApAtcqa8h69P_pQCF-V3p_Q_9c4oDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=tXhNH-EX4NixzVuIgSB5A0kq8HhTYb4u86jOpDGHy5ZwJ6rdp3A7D2b-PNq9uVkAXD16t-jUcVkriY0NRyAeTlyIHyZumxpvtwVJbKRIlSYBrTq_SJJFhFoby6XlG1dlBxnu7q_bIISPJKuP8JMTK3hE06h5rbj5JA0eLObxo1KASZojjdLkrMiDKM2AqNF49vi0xDx7pqYj0O0BDz5eGbcUcrVfcfYkRXKHhu88tfvDPV-F3Jni_qel1vliPcJVhKMSo6ZRsytDKZMYCAtFZBkGcLBo0o0VfYBCnbd10KuhPv4nM1zs6RcKAaCMc073vVrbJTxoXvMX6HcTnnCgaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=tXhNH-EX4NixzVuIgSB5A0kq8HhTYb4u86jOpDGHy5ZwJ6rdp3A7D2b-PNq9uVkAXD16t-jUcVkriY0NRyAeTlyIHyZumxpvtwVJbKRIlSYBrTq_SJJFhFoby6XlG1dlBxnu7q_bIISPJKuP8JMTK3hE06h5rbj5JA0eLObxo1KASZojjdLkrMiDKM2AqNF49vi0xDx7pqYj0O0BDz5eGbcUcrVfcfYkRXKHhu88tfvDPV-F3Jni_qel1vliPcJVhKMSo6ZRsytDKZMYCAtFZBkGcLBo0o0VfYBCnbd10KuhPv4nM1zs6RcKAaCMc073vVrbJTxoXvMX6HcTnnCgaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtkNCwodnsCU_T4IC4_6UWpqvGAjOwYT-L5lgN0bUlvanX995JzNWbrgNG0qR60VgyPrPVwqxTTNFD-Z7NpumwfqwfuVw4LGt3Q0LYA-VszY1UZWORtB65FofPYiI_AhvwriWMLoUoUsnmmZ7IRF5u5KekgvjsGfUAu3K8DDJ1ughue4AEU50lNBnxGyE5EnqH0RZUBns4brkBRCtmLa4ReWuPvfaCBy86QUoh2ag3JX7bmsgW4gxaJCjtgTZtxl0IVb9bOVYII-8dQFegrx003lnu6b1zIeZxAoP1NoU1M5hXfIVl52l534JYwZ8OMDpc6D-M7U84NbweRvNZIHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=pFIu0Q6pAM5-MlZ5h_zQlzQG_OgpFInUo3lVHoUhHMlXJ1bmUwujc8WEZzZ7KPmgRL7bh0Z_AaFyNeH5h6dCgv3Bzdhf0xWmbWkUY5jSw0IVoomB2TCZDoQKZlnC4v_6Ke7cO0JN7mQq_OEjfDgBmOasyTI1tpuoX3nip66zhF-bE2alcO9m7g9179By9uXQnbTsSBUv91XYQtug6iai_6kgRENhAkohTW-JROHuDeW_kjCyiWIrZj1MhtE0seMoYtdPpREbZT-nEp_WfpPQ6lJDDzlgx9iPAc1kcntb3Cz3hkD6ij-5iWDR_TfGU5YuhrUv6ZR_U6sNa4R4n2hygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=pFIu0Q6pAM5-MlZ5h_zQlzQG_OgpFInUo3lVHoUhHMlXJ1bmUwujc8WEZzZ7KPmgRL7bh0Z_AaFyNeH5h6dCgv3Bzdhf0xWmbWkUY5jSw0IVoomB2TCZDoQKZlnC4v_6Ke7cO0JN7mQq_OEjfDgBmOasyTI1tpuoX3nip66zhF-bE2alcO9m7g9179By9uXQnbTsSBUv91XYQtug6iai_6kgRENhAkohTW-JROHuDeW_kjCyiWIrZj1MhtE0seMoYtdPpREbZT-nEp_WfpPQ6lJDDzlgx9iPAc1kcntb3Cz3hkD6ij-5iWDR_TfGU5YuhrUv6ZR_U6sNa4R4n2hygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=MoUEuuCDAMLR9xcXpc9uxMn3M4kFqR3AGXoRAxhLzGNUIkzVkqUysC3rua2t7TH_11t-XQbKqxSrKWmIjTa1WeoGX6NtqOZFdqU0s2zKuwPc1nlp25pN4WFRsKtmNXGx1-NTrQM8HzwDzEoY0sDo0cnKkB9EvrHVfg6CEDvyF2JWZd6FSc7fzxMYaAS4bVtKbEg-LwVHwFwQ3MUKnPyviLQ_L7LK5XTOQRlRCT2l81W1OUJjz1v0pvG9udGtWllO61_xL7jLByslLgM0CeWzeEvpUN-pcXwDV61WTPiwvrQgQql4vxxwxy1IDjBCKh10orDFQ7DlA2r7nnQoaI7U9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=MoUEuuCDAMLR9xcXpc9uxMn3M4kFqR3AGXoRAxhLzGNUIkzVkqUysC3rua2t7TH_11t-XQbKqxSrKWmIjTa1WeoGX6NtqOZFdqU0s2zKuwPc1nlp25pN4WFRsKtmNXGx1-NTrQM8HzwDzEoY0sDo0cnKkB9EvrHVfg6CEDvyF2JWZd6FSc7fzxMYaAS4bVtKbEg-LwVHwFwQ3MUKnPyviLQ_L7LK5XTOQRlRCT2l81W1OUJjz1v0pvG9udGtWllO61_xL7jLByslLgM0CeWzeEvpUN-pcXwDV61WTPiwvrQgQql4vxxwxy1IDjBCKh10orDFQ7DlA2r7nnQoaI7U9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KI5NImdDUYXHpAzGapOAiNFOGs4sY-0VPiAywVil6un-Bhl_Rt8HLO076tvT-edIW9Nx1PVvvN6S7ZBvGNO7H5TdX3C-A857Z1oEFwtNM_ZyHa_pNeiFEsg_zgJwFn84vBLFq_vl5xbl-p_ymep5l8ZrW0EyHs_QJ4LEVAl0fBA-JwlokKZ2RDTy9gIHmK-j-teKbXh1AfdKt9pVrcdpsVvM4Ry9ZM-QjDwuzwoWngvU6cnHTnNNY9lHb3GWXjPl99MjV4gEJ_QrL79Xa3-OfwodJvkAkQADURnuaNnbZYAZH4WaM4LEWURDJRPlmHcqj6AiBSxgY58puIjzf-E_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0dgIG8dsDvzFWgWSPV7MDgkGGwfM4Jc1Oyj3Jnh_13uKCXABbpE2mwbac_OLa_AOuzPnOPmb4C5Uv6k2VoW0ZCkMIBKHaldkHyxQl8W5ZRyeUujIKZMtzCn784uG1nfRbQqSj2FHyoZsypKw_hciO43WhHDs0AlivK8G7kIy3ErG5dHxqSHTHOgHfP6JuYayawxzOX1Lbgeet2S28mNp6Dcs5DJptx00Gtn68RctLLuOydmzcezDL6JkiEmDJsEACnYstc3I-aIzrn44phRYuFBh3N67JSv5KtHn2w6qe76Sqw-FhZJCnF2XKuRaKf2bvKGE06MaA-r8nCyFlhFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXgn4rMJbdnFG2S36PS0M9rrT8xLbUbVvYH3j3X_4ZLApSaBzbz8iSwXJOo92U_hGLCR2U7scIeTTKR8kfxUmesGkbIIVwnbtDaHRV8H-CIgpSnX7dlAlB3ln5IJt2Q-r_C_DknZXvjwuptJQPwAnxCYFn6RSAwU55Dnhy_OjKWr9kq6puK2qBveDuxfpGw6N-ZOGv5H_7ZfXFthqqu4UUIFXdz8VwifsUMPJ83cjlmGHcxtOpD9L7GLqIX6q-BpmdGuUldzI-ufxhdm-JBIjD5BE_osRCZC3Nc5FyUzraMkccmLW9VTZgxdIbg5gJqpvbuIEfxrQIhrdp7fkbCBog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=MLS_bMDx78OA_JmfFgp_8tieZ_jW-lgz64ecmTzCmbGLv9gAe2PS1v43N9zb05o6BjJ4gp6lGA1MV_k9F1ay0na5v1NhFFjT5R6M0h0OM74v7le7W_lwRzEr2w-v-wnzMIrPohbXTRoB2p_wFLg2PlJeWljy5FKdUhMJ4pwhDzd-LWzKAoK3kHiosyA4ysIidXB5cA7BxuTMPXA18v7hbZyxUHHeUXcJNtQNF-J39KkO5E7mC8_O_M6zK0FeBz5rT608rROoDQt-UgBhL5jMTbzIn_Be9g0M3gZ9l8aKKqlif2TTAOz86m1L8VpOzMgXFPjmGCSfptSueKPVxZtXzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=MLS_bMDx78OA_JmfFgp_8tieZ_jW-lgz64ecmTzCmbGLv9gAe2PS1v43N9zb05o6BjJ4gp6lGA1MV_k9F1ay0na5v1NhFFjT5R6M0h0OM74v7le7W_lwRzEr2w-v-wnzMIrPohbXTRoB2p_wFLg2PlJeWljy5FKdUhMJ4pwhDzd-LWzKAoK3kHiosyA4ysIidXB5cA7BxuTMPXA18v7hbZyxUHHeUXcJNtQNF-J39KkO5E7mC8_O_M6zK0FeBz5rT608rROoDQt-UgBhL5jMTbzIn_Be9g0M3gZ9l8aKKqlif2TTAOz86m1L8VpOzMgXFPjmGCSfptSueKPVxZtXzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=bbe1rzBENZEGAYMmsZCV-YShGHuR9UG8EGva4T8ASVdhuvZeHmmkoK3_U_5Jz8NEU2knRRO2a08-itbtl1_J8A0tJQGR5E9kCNMZdKtg-PB_JGx4RtsbY82NnfXLH2Qquu47oQQOQ29RyYAEBisli26GmW3ixyXX3Wkhny_FVkQZAv1wE3ZwM2nh1jvx6_8A0XKIQB32O8222gnFTRw0xgrE2zkUgGHLXytq2QaY9hLDXOCf6s-jD7XJbYdlaDzqE8ZbaR9989dj2m-KqhdcfotBcKH-Jhrmol4LAUG8MHo6yyPopbp9EGKt13ryLGguoIzTKM04-jmn_LUWJB60ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=bbe1rzBENZEGAYMmsZCV-YShGHuR9UG8EGva4T8ASVdhuvZeHmmkoK3_U_5Jz8NEU2knRRO2a08-itbtl1_J8A0tJQGR5E9kCNMZdKtg-PB_JGx4RtsbY82NnfXLH2Qquu47oQQOQ29RyYAEBisli26GmW3ixyXX3Wkhny_FVkQZAv1wE3ZwM2nh1jvx6_8A0XKIQB32O8222gnFTRw0xgrE2zkUgGHLXytq2QaY9hLDXOCf6s-jD7XJbYdlaDzqE8ZbaR9989dj2m-KqhdcfotBcKH-Jhrmol4LAUG8MHo6yyPopbp9EGKt13ryLGguoIzTKM04-jmn_LUWJB60ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6zUTy7qcX9ERYV_tSST63L5UQzDp0RiEXxvhFM-THNeZRD_FKHa2a07Vex1ObyF4HrG0JhNMwi4Ng31bAz-kCWj3N94aNdN08PDoLdr9OyZHMooElFVeEDElLApuxnBu2RWiRI35tky9DlVtDzSaOuQSgspZC6vNuqir4wEZmoZW2SU9hLxeF4HxKR_9CJr_L1ldoCxP0uFjTF1DQxFkJzVTn6BxE8Xeinvh-ph9dqOv97c8-y1-zL7R6_2SROu5Hj0Sm0hpYpyxCBD102Swk7GoRifDp_zbOa9mbGgIT86iCrwagtLNv_TjdKkuu6o5NoBOLAqlb9znwvcn5YOAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=RKTObNGzYd9A0Ei2iPowu0-TvLYGCbOks8oE9f3DrhWDP2udH8j4mcctnHQB2Cs5Sy6L08Ou7jqthSlJ7f3aBCe3pTU2SSEMde7guiyINHxTDqPEdMaOpQLMrU5KQ6mXg3CaYN1lajweCU6gSHlVrdg7GQJFIRAVsMbRlR_Cm-vx55jCWxNrHj7m5MJuJSgqURWYpZJVZWfxYjHWwit1gQCCWc-Av_SP1wjM9JnSkru1UfRmHCt0IcxO8M8tBoe0CE33DubCH-6ErkgIYBHOFk8qY7pn74k7DUKkt4cuLetj6oEJ2a-umb5N3j_-1gTX-bJyf01-44jyc7LCLHnFsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=RKTObNGzYd9A0Ei2iPowu0-TvLYGCbOks8oE9f3DrhWDP2udH8j4mcctnHQB2Cs5Sy6L08Ou7jqthSlJ7f3aBCe3pTU2SSEMde7guiyINHxTDqPEdMaOpQLMrU5KQ6mXg3CaYN1lajweCU6gSHlVrdg7GQJFIRAVsMbRlR_Cm-vx55jCWxNrHj7m5MJuJSgqURWYpZJVZWfxYjHWwit1gQCCWc-Av_SP1wjM9JnSkru1UfRmHCt0IcxO8M8tBoe0CE33DubCH-6ErkgIYBHOFk8qY7pn74k7DUKkt4cuLetj6oEJ2a-umb5N3j_-1gTX-bJyf01-44jyc7LCLHnFsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=g7I5SkC5S_T9K4xpHQKKRBM-LkwvNzrYP3wLleFJzjqCe7FTSMzw036EtOxg1ozps4akKVfMTvxHa3T-zbD17lU6X4yfVFCvj58IqIoo-8wXqaTaNvHQOu1qvSSZNn5_9W826KgLmUbTgaKTBUwnfMDNA-L0xe9lV6YXVihWkhQmSjLFaixYG8mB-CobhuRigxrdiwDoJ-RknpzsC8d-DeGJwm9eVylt8eJk6NendRubTGVbcebLEZ4omvxQdmHdgUkobiZt7y4NcOaH2C5aIotEzDXL6k1PHF2lnTfQbh0WtZJkEc4to_QU2oRVVV2B4Qo2T8cingggWOpUyLowNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=g7I5SkC5S_T9K4xpHQKKRBM-LkwvNzrYP3wLleFJzjqCe7FTSMzw036EtOxg1ozps4akKVfMTvxHa3T-zbD17lU6X4yfVFCvj58IqIoo-8wXqaTaNvHQOu1qvSSZNn5_9W826KgLmUbTgaKTBUwnfMDNA-L0xe9lV6YXVihWkhQmSjLFaixYG8mB-CobhuRigxrdiwDoJ-RknpzsC8d-DeGJwm9eVylt8eJk6NendRubTGVbcebLEZ4omvxQdmHdgUkobiZt7y4NcOaH2C5aIotEzDXL6k1PHF2lnTfQbh0WtZJkEc4to_QU2oRVVV2B4Qo2T8cingggWOpUyLowNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
