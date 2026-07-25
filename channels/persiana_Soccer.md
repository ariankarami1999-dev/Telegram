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
<img src="https://cdn4.telesco.pe/file/OcA9oU9QPTndMhxsxWOTHCWJ3bZrVdUZ5TrO6Hw4XQysfrmOCnhntcXrMhTkC6Fl8wbodEgL7Y3hExvjtJQ7lbIqUG6pFNOmGNHc6XsEIAB4pwJ5O3BCBAt63X5crSFWwIYWVrRFSaqf4PpuTSsRWEoGEx_-a8P2_8Wds8A3i-NK-5PBaDrUfV_KgBRohoSK3jbOnushSuB2yj-7chp7JqIX5m1UtKsS27Xg7igjtHL3GTk3x8NdAkj3N63LukTd0Uiinz3lSpWvSq1BtPe_2RVkXQhkSs9DeIsSIHX_H76QA9UShyZEQgC3qSLJ2c4_TWAVajQQpAnGxH-QRHMDUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 584K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 00:45:30</div>
<hr>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aidk2iBT0I0yxrZeTc4IfHGIPV_cUMRVrewmJlYM07zj0iczcRISIFowSTK1d15pACP9i0MRyIRQc383fShyZoPfhLTTNrRsTnAHZxtMGh9pqzrjdGkKPYdN9a-OARCt95NWwWLJL6EXMWNcX-5WDQ5AOnuoOuZLHSYuYOyptusYKeC6MBG2XjpDCwO5bhi81gZUi5F8V2QAD8OXnFot1Xjya5Ktozusd1NKk3YOEGzcVRmoj9wRPowi3NvdMRRU42XJ_vnp6yxCu83iPYcGCqtXAgRqeFG_NswpEfzxL5_uIulk1d9BbOHgINGdLjI2oWizFYOhDmgb2xpRIeie_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuW2fPiJ33hgQFWZzkSRbl0DHaQdIyxjMVCvsKkGArrq9n15FecW4i_7AG9WsV6iSR-Say0vEbaoMLEoJ3TrKVkaYZWQctC93VnJmmvzeqpnJXggDel_nKbLx5TqZ4hfdl9WOjjHhC0KFoNQwTIdWxMckq5qrcG2wdg6MiM_iN8iE8YMLYpshrNce7hmCH1Pz44TamzDYJY3RSakElU-ySz7vtWzBkcZK4wqiMcClcyvymC6-mu4d2061gzxqSczgLXtBxzFQF1q2kR8Q45gKDnuT25F4OBO56lpiw1onNUndihjnt63efG9mpWMAWP_dHi0TYqP3dnEFtffBlwmjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDBAcHEqAo91YxDi238AxWj_twwFPZjsQ8lQlbO0MGuUQ5WB6S4IA_c1lJDyxKQoLPNrPM8FD6QcG9Gl23xvtlgoPzmDXO3kWqBGJefXHI1sblCjukph675nZNlcxPZH34dtQv4sAxgHUjnOpIDmCnCA5eR4FgWzfQKaiL5VerT8dSJYUiMGtHSVP5kZ1W-IikB6GsSdYpj0JL7zvV6tSUnmRdYO6F52gdXf6jEogJApu2M422LqTEu5pqP_LrMoHYxb0PkxpUkH_bIO-QQ31Ql9Ve0Nudt0TZIK6xksxlXRzkKgQLWRh98_aZNJPKsfWH5IID3dVf4dQ2X15CxCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAMgDTbw4OJ_rFYZiZeDAZSsS3xfc5HWGNV3GvC3Qo-mZrT3BMPOUFkkxIjsn7jBPWdJha2bahi7qC8SRB1s4hut5daQ03IjF3jl33fx4FMEZ-v-R93eslrHFMRMkE-RJm6m4SJoWkQwOZWaO87IPmUui9k1tNTpX5BPh71V_opTa7TAua27LhFOLa_ghDXlEXOog_Jl7VSV8fQneNB23c_DIFf6sgnzUFdM-zbGoxeYZh7slgBNOPa4fjjKU4Vv7hDYNEE-CGTcSve6vCGmgiqwB69gJpU9ggHrRI6kP1K7Cfexqf7PRUoJZ-507-xd0xXtZVGbck8xwSlAfa3GPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUQ1qCL8jNAG744ZxELh92aMe4P9L97d6vrzk2SHkvtLb_bIfYU10jheDbZkOglF1oryquX4NcFVXsgn_eu2A-rOi82lwOFvBl6y8u2Y7wktsVD1SEZvMD-64C64_X8A60KtB1HRYYblgAFfVHFRH48lGpeDitfnrI5ZDhsPhH2Y9wjv7TukNd_S8Z_SB7DDtmLzIFdbROZLij3HNzEHJVjhSZWqYBD8GzggNml1SWYOomKCFYTHx8WQxVL32D34ULL_IoefNxw1LJT0BsJCEBV4kexXjnt9hLUVX1TBvzgZyESBGnx9QySAUjKdurUxh3LRnvAo0wOxBPVVtcVOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5E7eNKT2qIVvi5dNfSDtnp1NXaWvAZNlGr2wWg8HXRpNAIWgf8tyvr4irtG0B-EgeVillD1R44ic8r-I6EfeIQ4pRzT4Ph7bma--ea6z3UP2BTjTcVT1dACLZhb2ZQCrjs-lGm4_IAq9tM5tabNVkJe-Mf367vwLtgeh2sgD-cd66YN7cY-PCREsB49IPA6YavucuPvidsM9Xn16vsgwpuYELpIbebq_5bsZybs_4V6JxvSwz5AjkKsiFjlXnPDrlgcfYjRpBLYXe6JRBCFbo3YX19H8oIOy_KWKaAmuyHJ1GWOoO359Sdrfeu6tukJ4iv36RnFS5dSc-KSfpR3pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By9ATaF82wq-bqytN7YlJJ_9Dq81MopwtIz2tUDz3xY2B9Gee_WhxNi2taDbJRj-u4cvAbzTXmAzCvxk8qjjQO5arpSjXGGewvARGzegqzE3-XKEbRLLEOtQdi0KriQ_HpnhVNMXA-U5udXbsf5Ip5nGFdXet1Y9nH3VukvrGE6TxvGC33nnce1cT0So52XXB7o3mKHnLoR6hbtmJXYsAR-58cN-5AvDF1HFVik-XZsHYlG__2d1tAsmZf6sH7tpHAhvaIZRl4retrOR1DALLLWQi0Z5ka2qQYKQcB18yhbCE07JR_BofJGH8Ylmqd2NggquNff2xVqDyU5bopL70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t38KPbavUbvzIRjEkIhTFQkYwzTU622JmZWR2iBu3KKxp3en7DQbbEiuWFzF0cPV6PmKRTICF6ARmK5Hk8aLNVpOs1ayxVFh-p8ZPpOAB3Egi9belCIfvlLhwNEg6_pCWkYoLVcpcr6nPbFCZTVhiDJcSXl4NEihL4Z5G0S1kjTLDKEKGFxNasvGToxuauq--L8kr4OMdjKEsCfdPdjjbvjlWDg41UViG2-RH-seDL6ttBi2UhJJxVMhYil17qZLWXM_8c70AtENTqcwlW7em7JGv6qWxDjnF4mU5rV18gC6c5Rj_4jc7An0v1Hy8gltGmzsug5dhpPZV_f7B1W8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmOaMaI_EGthyf3RM6rUWLPtBAjlt9_F-XHgiQTpJyAlB1Vg84iASYe1PCM9Ed3PGlUmhdbT3igYKInPvlH7HB5nt74lri1oLA12AkLFzB46eZgBQMqy_l0-4TnL0mGuUYbndmeg5_J1o9L9bZkwWpcxfIY8zWrsFNzC5zK3XtUNqKqrw-Fk0HbseHLpD3yvfGp7nBfUhP_iEFHDpJ32kIL5pvRpk6mDOKiX5r7EbeCuh66az43xcceG35fX3jlmqP1O3Hx2EqSIC7fjMvb_mzZKXdBD_4sUBLyBW8O8ul72ec1Z3CBiqa_DARD6a2MxqhCcx_-l4nTAzaoD_ZzOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzcQ81wEUv7e7gRyrlQI7TlrVG9AnOsCNg9pXDNMhiMiB0bjO3Co5Y_kQcHRamaBBBNtwuRJaOTRuTA2esyfkC9XHA4lY_p2VqOqtJycnpe04MCNFkz2_fF2GrP23Y6T1Vd6e-re93OSI4-8KlB3LPa7bjTeM3at3RaznP4CzpfxDlfKgj2jX36_SYFosDnjE5Qb3OqHjwWAo3vuvRG0wefWznRXOW2002W3Kha_n1uoNiLMFWTiSzxOhK_2LZQnClLnFT6LBeG2FBg2gfReknKOsPrG3ybV5Fk_tKbu0c01kR_Ip-BU4RjYXboBm5fBNIgZjJCVlkcU0s6pEQyJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxlcz4Z8xIwXJ2DDb0swBEdKhiOTahe6Scnhrav3LhKSZlt4YxRSWxG-WXexfY7xC-94aCGTotTcIugLf_-Lj8XFOsp0JoPI47Z7u6WUosvlq5ROWl0nwAd0CRgBRglWAWspYhzycuSKK49l2HYo9nCH_iutEJ14paMu4lf9jWGqhucBrz-co4kO1Hf4NKWKSIRxFkuKZjXdiBP-gMyLLLFMtEG30p0x11-RjLpSE2q2EPOsZqFS6-FpJULYdcem1IaaDO4hiQvMo9nfYKcP_ic12M0a0BuYjohlcpi6r6WyG9jCzuXoOHG4UMkP-chm6SNtqoxEMa1ZpOYoCW5poQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EukDkGr7tbfK1-VCL6vxYOGJOoeJBEGHsJVRiDkLW5bklVblWkH8owbtXQ6cp0_ccxmbBET78bxJhYi40JJysi_r4cJWSwsis86xNS7T2S8BwbQktAKf3d-deZav-FA6WARjAWSLNuex99RXHNnpuCfMPdyxZrkrFP9ExT-WjXmQL5N-YjEzayDJQcghDfUo5xEF4hg5jNgp5moNUkzzGtRP3GGxDHWgFEDogjYhk_8Ybb4KXWSQOK7kBj3DPUhF7lfrA25bho0pyk0SI3w6PsKu0OZO2TDrgD9ebkRxu35zphQfQjt3e_zmCfxlVnh0hQ3HwLJ5kdnbZmgrwTj9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFwcKwFGTQCp2LSjhQt0D3JWW5pWEvyCUjhKSIuOltZ3mIiSH1Ftx-o8rdrXX2Y4DMQo92JHpEwsWsDEdUiAuIS3nPwHXGw5hpx6VugBJ7ERMZnEnJI84uqXH5aLaOOgaEfTZ0e0YNTfWxcr9s4ZZ9TbbhTkWVj0LGgfd9Hdp_NDrkGnUBF2A4QDpyT8b3r2hs3bqoMoPPAfglSNx3z8ijiz1eMT3GXGiGplRURPfRMe-dQTDhlw0NoHxoV8SGDpPYwfUW6HWwyCHC1EiN96O_q5UhNqKMzYRxNIFEyAvksNfCFniYSO3PukojGf9OKpwhoNJMru168dg8OhWprP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-T_0vNK86TO3_2rLIVELHIeYzvtK-EY4ZLSOrKAehD6nxbgsZIXR8SoLMNZnpLS1PIKei1H1whbYje61PTCZr47jQANcsBhhrqV49OpeEUiQE42wH9hZ3T6yKi3m_p4J44exeIImRw5FiThr34Inq45E996bToZOYGfo6r2q6hyZ-CLc_O0QSmFUrO1DAyx6MPSwD_CL8zUAJ2__TosS0y6xWEo94WMV3LCtK3EjdUtmVyUHG9zAosM6vunzNPMD92zzTdGPaiq621SgTScK6GACJJFoeEV0QfD6kxPv93Y29phXx87dbzaj_nhvBEFnb4nkACtziJC5d5zyFcc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc_QEPZ_nx1o7Hf008jIpkPjscTlixOqrCFWVVVtNXhDdE27RtRucj7NX89Wtjx0s7iGj37o18hpWTCffSqpyHyrro0-jlTJO90ow85sHQxvlQM7Lm-h7gx_TvG4Sc8NDIkDqqaM5yuTpXj5D-b0HYxkL4T0fiyRvW4rmAo-cb3WwrsLnnTQr-35E1ofzyRFJ5oSRAB_CZ_PO0An2_8PnGIeO3e5pJHh-4PvnhXonVJnSwQf_9XS-Ao1cJnEwN6mMNHUFJQGnElnMVv3f9ewZ0J4DaRHOEYm9Do2r0gkfc0cEbOQINYyfEJdQ73eqZADXqbBwwqO2VsA37LcyczabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0zQaFziDrxD_YNg6l8Hg4cb7-vXMvH2OW0CRhm6k9zHmjm3VHbRQKeF6GSrWBT6PpcLydfMDEOz17A7ynF8juo80DHb7RUTE65oyaBDJbuYqmbFNK1ctSqORDTXUnwfeoqcEGIgrOK8a3r0dFWJztdE4Tt705P25nCfDPSs9bP3yufAnAfsKOgS5vuTAJhQhGvT7G0KmjTSU1Zn48-fzHmoxovETbPCuv1u4XZGVQexJPNzCBrbw0a9U-qXW3OlmEL7hRETdgWFnPj8LdOWnjqzgQlF6VTdBJ3VHE9lv6YtPHhLiCg_XZ2-1VnciWZlszPZ8rDdw8XrI2SI5tLbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAeVOC9i_zHrjFowWhnMy4CtJWOI_HEahnqzACMoRJOlobryrWpQY1UPdiEWUMYT4RnuD8HJZ5Wm_5ibt9EhXTZJ7gRZgU3H-sP5T_NIrloky5LB-N_qgBWjm78vOwJWd8KPqiGDAzqHfzZzOyTIyVe_bIpacX-ezI-6SbfhfYF0gRRCr3h73eYYMQxuS7KdIbn_64p-Qlgwm8A-kqcGwNKJXbkWKqjowmMsoJRDq7VE2LgdIsY008Jzy-QM75NE8Ya4vTBja1VvUZhluIIYMiPdANw050eD6Q05X-Z5lE6k2nGuF2AdP4fOXjKiXb2mCO1CzAO3Kjy1ob0ZTRRnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=o-Re4m_9W39m_LncqgU9TdQwVXy5sILYvpYb90dlWZZbsUkgWAxplhb0WD-D0HnRwqUm3EDAt1GSN2A_TNEq5dZkCGRz16HXeOR2rwLlIpYVk_aLUzwUDDbZGcNhj8UhP6G_b4yuK1i-0GYNWA9PjjsZUVb-rd_-fLE0QuNMGrwAug2Lh-5VTbByeKe0WU5y39tcMpE55TYICQUVFCyv6SjxStRSlzzIgM-2HBHFmx8ij5nWrlx0dXMtJmMiERAeSWHGlHSEcRFuOYMD2buoHrTkQrob4_UcSifUYd24ud1lrJ0FxhcEaiNwM_j42oABz_7UVUpu7EKDi_Ugp0qWaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=o-Re4m_9W39m_LncqgU9TdQwVXy5sILYvpYb90dlWZZbsUkgWAxplhb0WD-D0HnRwqUm3EDAt1GSN2A_TNEq5dZkCGRz16HXeOR2rwLlIpYVk_aLUzwUDDbZGcNhj8UhP6G_b4yuK1i-0GYNWA9PjjsZUVb-rd_-fLE0QuNMGrwAug2Lh-5VTbByeKe0WU5y39tcMpE55TYICQUVFCyv6SjxStRSlzzIgM-2HBHFmx8ij5nWrlx0dXMtJmMiERAeSWHGlHSEcRFuOYMD2buoHrTkQrob4_UcSifUYd24ud1lrJ0FxhcEaiNwM_j42oABz_7UVUpu7EKDi_Ugp0qWaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SulGdjBtJZGT-dbk2TpKEfARxiY5n_5edD5baP_0KdXpPpkrPy0C7xTyGlbSCB1OfqUjZbedeNXHS6w1LwZe9kWzzII5skV4q4gYukPGjCn6YjsYMP1qC_-n3Zmo6J2Ow6LEVIbNv2BFi__jANBU2LPzNWBD6_SSl1dkpUOLe2PWueXoRwT33Kv2Asgdf8e80e3dpE29MEZJ5b5WecjXECjLiKj3k7VVpvEKdaXMPhbwdxjoQOkWpzAtzgjUHN3cLzfdr15cOF9cKblysws-KJF_oXHL4P_q0gb3NXukt0_M2isyhROdCoQ8CVTEja_QVAg56ApsTNcBBgOqdwpuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO9Zxj2k3c-u9A3MD5o8CW1a_I89bVFDRe0LO3kmO_T2UHbcYCJ14dculspSOtdEpvZuuyrIaiTKpqzNvF9MF5MpXTWyzw0aPpwcBNRrp49uA3HTUwOwiuRFJLdkeBxSAWNNv92QBLZD15hBQFkFyDg7zfPKhtA2mBuLNcT6N1D8W9VZoRxm1V0G7LcbxMSQXzsP26EqVKbthvKW1c8y8bkUzQJGXmYnyifbEwrJ1vIn5QNv7jbDNUZkB8tLoDsimYMTPcfZ5hgbG0KdPz61zXs50u9MFNlAwhTaa0ivrJKEGNyKOixj6jM2QfBtzBBtN6AAUJ8jwhDBKeGRsIXP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1erqe78W6G_ORauvCB4ZcA05hxQCB-MxGvTlXu7ddHa1FnjdoWHkv6MrI0AZMrYJQPqjxRO7kRbwX_7Zr3g6YivNDyoG1mUnUS_Gj2tBvG2V1p48kJ4IWqqj8NjCZSuIrS-8dfHtIPvGjS4WMVT_MeY0snwlcORTXYYGdzA0bDwWSBSoPH6UBLT68fCjkJc6PxTFCfM5rxQI11mMK9GHgfMbiNQrSSLm3oLKjwPulVNuqVZKjVtTaYqEcUiqYCfL8FivSullOegaQDKzSAvQc0ExvT8IIi21vNllo3UfQ8UD0_SE4EppzCa9hfTg3OKV9nJUjUQKNRWho87m39gIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=GiG1vjp0X-eVttawzZ06LMbhWVcjKc8lUtfGkcPlAx-GC2mxXK0Fk0GNK5x73AWdsxZpQXE3JWCBx3zF87C1Nrqx2AQF0-wvbC_E4Bo0Z7GSumOCcM4LRy1_ga2a2PBoKcFKyyuHvxxx-F9BlMy4vUI0IThg6pfyufs2kooYoFSfD7C4Ynd8iTp1drFTJnGplvpicHWV88LeEmS8blq6qA3PuZk7gHbZ2cay0V_V9IVbbq_g5UbouZRUV8tUF9XW6agmRKPZLg6KUf4ysG8tuQ7uRLb9BtCsXUZxKTj8xoG-j3IbzA0dqRkT1IYD5HoIsBGej6l6J5eCvw4n0pz0XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=GiG1vjp0X-eVttawzZ06LMbhWVcjKc8lUtfGkcPlAx-GC2mxXK0Fk0GNK5x73AWdsxZpQXE3JWCBx3zF87C1Nrqx2AQF0-wvbC_E4Bo0Z7GSumOCcM4LRy1_ga2a2PBoKcFKyyuHvxxx-F9BlMy4vUI0IThg6pfyufs2kooYoFSfD7C4Ynd8iTp1drFTJnGplvpicHWV88LeEmS8blq6qA3PuZk7gHbZ2cay0V_V9IVbbq_g5UbouZRUV8tUF9XW6agmRKPZLg6KUf4ysG8tuQ7uRLb9BtCsXUZxKTj8xoG-j3IbzA0dqRkT1IYD5HoIsBGej6l6J5eCvw4n0pz0XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Od7TfafBQCPLRPITJaJVJ7u9S1iTRXUYJFnVP4FNd7HvCC9bGksI-kXEsEdZpqafwe4hrSt22OTwdvFaPoP46xdIGlqanrGmgIYa9wU1f73G4JtTW3o4VNyTvdWj8YI6g3RjzBKpxT_-DQ0I_dffb21PJf0oD0cTwwMzmrgI4iwgpNJoOnqjbCA5bsYoh77j_vzQdzs8tWq2a-nsFLmJJOZKwe5eGNndrRNzFtEms0MxHonZZ177CvWK_RcBV01Ti11HmaZn3O6-QG8J-qaMh6-bc1TPJBjg56oQqInuk8tPmeeL2oo06GzLkcfHP3DOzTf1whswEYeGuxAIBGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=lvafbe6AtVXiyT44tiQpCo1HnFwfdF1nnTKSEgV3oX-NdcPxmnnaPMCzmKmbvCbmM5aEF9CtpMZU1-PFJNELIdoPD0bEQMJUCvROM8_cJBKvIX6EbTpb2_S1KIKhUkkk5TPeWrEqTGK6cMKaG7jeeF7tXBfUnK3lnM_DlDLSJxLA-AGjvGoij3-fxpFotNkmNPolkTnA_aMBaFrn3hP6s_x56kHacDq2sUdGL6vQTCBiFVq8OLQejhmt7Qjs3EIVxIPRip2yY5qd-mX3nfzHkJYcFN5z1on6vdGQf4fLGT5SRALXNZuw3kSaSOxZdadyfUxiYhAoOEZuKyTrqpmbug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=lvafbe6AtVXiyT44tiQpCo1HnFwfdF1nnTKSEgV3oX-NdcPxmnnaPMCzmKmbvCbmM5aEF9CtpMZU1-PFJNELIdoPD0bEQMJUCvROM8_cJBKvIX6EbTpb2_S1KIKhUkkk5TPeWrEqTGK6cMKaG7jeeF7tXBfUnK3lnM_DlDLSJxLA-AGjvGoij3-fxpFotNkmNPolkTnA_aMBaFrn3hP6s_x56kHacDq2sUdGL6vQTCBiFVq8OLQejhmt7Qjs3EIVxIPRip2yY5qd-mX3nfzHkJYcFN5z1on6vdGQf4fLGT5SRALXNZuw3kSaSOxZdadyfUxiYhAoOEZuKyTrqpmbug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFVeChk_tbt1rW1DMKy8DA8-ROGHsfLvfLd1UoKpEoFIuyo8pCJgT5Alg1TPjmp0x48AYMoiRkoMMuWiQ1AUQKchk9p06P1U-jF56FJn63t5j9xug5733vxEF1aAHHttVWcMMPVfKd3fdBmn4_cJzddKW-muzHooCHAVFh5utHhnZmob5A9vP-iBTJz9TtwzmNjp09OyhzMhglXjvsEoqp14i5YFC-Jq1EsbCQ3yEpXcgKLnzimLm2au-qCQ0Eucy_IEICmlb0_RbzrTEwVB693dpTHRVUYevk6pJ-6XTTpjswtZkIohFATHuS8yVCnET_4pkKSyWLVs6QRutAvjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AO8nD0iHaZya1JQC9yCAJik90In8GKv9VdtqQVEZhAPVroH6lB4DOJM4wUY-pCSwZswmUsUuiQzr_F9-oAoGnCmtLJqrJher9pYMirZubwWfZDfjcljK_XynBvH7GyKeOxbl82HqYMQg-wsDvdKQ71RHI_vV9yRhCcJ-lv7CZfvqwENPdtCtJVkBT32OOaHzNQ_NQUJUjvfqGNRDBLCREl6Lf4nLXRx3vm9X2zuv2UPzl9eWvioKsXFKw37lcf65pL7aNlMfgjIwlUYcBVq4dx4JQYeqrLxP9v-GbnjR-EXK_Px3rwEcIMO5yQYhlaLtV9W3JMK8pW3d7vnyXMyCFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ0mAM34qD0JIZjC9tOfeS20LwlV0qCRHiSmFbPNXIAs5AzZdrlNHoJADHEPKBZkeufEM3-bVPNokQLoUPu64R7jUFAdJmkqSd6b-jSKGOxqAQ8yIEQfEGcD6PsRwOsqIZZ2LjfmLmz_gowrx4ZooEl6tftSgQZVd9l2rZQZAiDFCfPtA0Py5yHDqsBcNAmuuXKc5NAyrAuz2hwzyFoHlj2K_3ZBA91mbvmBZVQtIq9pob81DpJPIFx0M2OFFz_TIJIouUkAPnKvaWRf1u9CKKPD35h6marc_Vx50GL8YOmCm1FV2ZliMxmXdt6r7eN0m8RNRypla4akPDStYcBr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8wuhPvGdo95lwIlMv-rrN8_sTKd14NARxJg1xXXEY5Ek0NmcKvCLjXuLn6rkJ8CErUTNOf5wPEU1bPAc2mv9r03fmJUkWMaGox8F6AKRo-46gnuiU9xRgo9dr4-FemxnMUAMMwEBdOPa1l_ersLGt04XKSbDiILTkTIwcOU11AAAPNBoC27tfpmtuLO0-7riYX24b7zq02djFc723RCE15vcwDLPLsAkI0U2RCZTjcuXeckXe0DRbMCAX17u_K9aYQQe7nV9czdM0lQk77ITtiLFOIo3jzFCaiP7hjspgsjHbAupRma9xKr2yHwkdeqb4n-kCLAD_W_HPJt_aCIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA4Dz2WYjHoBERV5CuXytOUIev0s_OsE-s57CdpWLI7D6N3Q5lSELGdMI5LCs2zmfYNp9p8AbpOOeUVYzoBzxfAiRSD4NBo30SzTJbKcEqQ8TrBhRt1qDP-sigp0rF87uP12OAvKq2mG9qJpjrmCY9G35cEw2mTNHbkFwgyB9Kkak4mifQFA-zLC9ulwIvcrVxxKPNVbOby4omEkRLIibitLd5zPFM4EOCzrmJT_6gVaK55_c7srEjFFxt-lBWMP0ePsTRpzp6Pl_5xht5nnbxWHy8Rs0PfBAwQZx-nI5ii-rh8CBfvuzA2PTz3zha0z8G3rFsXQXfRgkGif_p7LuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRTi7fpTfOGlinshfRUcHpSa3Te61NS7Z-D8sa6aAV7xIil38AYnoFZA65l-8WcbdkQi6Barj1gDCIAMTJAwF1Tkpt8yH36g6ZawMoyo0ZgD2mPNKz_MFwF8oDG5lg4REsipYimf-h4HZy262aluWxTThk71NkjuJAfClO7h9-rSWP_47b5rwG4LbrWBrZX9r0x7kXR2OgJgzYgLKU219wZUxbKPdEXqvTYVW-29J0T32NB2t_76AJk7Cf4yHrWenXlMW9ckpA9xigVo-QX8lQA7a4MHUp6PKUSkDUono1vOxbUBoXv4ewSwTlatIs_AhonTw-BjLrIzhPgtp7BkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIKM96zc-nEhdDUrhk2euzIPmZn1C6-FHt1tYKv0hr2fxUanNKm1-9vapmaxprvjGxcnSEM5f1fbEK-T95eM4C6gmg2TWVb2npuxf717k5_BHQ6uigymp1SEQLAbqYBanMKsF-IiujrIP_4mm0W2HSQz1hpWJcJ74PeyDpFlBTGpDz56ycgAHXdItqbXQu058jlSz37tJ1hYKEi01doELJbZYohHuY1KD6V-BPdIq7U5KtHKAEcrn8QP52syBTy2AOy70uBQBclwAMkxKzaCbsNwtSxvlAsutQxx-Qk0tM0tYWnWkpc9hCkym4D9QMp2gKeS8Wj4BV3Q9_21rvfHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_3ftUumJ1SMLh1yHn_vNdGnqTNPKjKk_6JD5uV-uWA9aXUrtBPzt-ZIHY8U5vI1yADYaMDaSWcIGXniFTBmOucRPt2vGiTC6rw78gMJ_11WfTBgYiba-THBHde2WAFqqgswU2g1G0JuYzV8ZAuOw9rOy3eyTz0pWiHEVQOK5-lpH7A9HYIx878mgOZgSYZXrQEbnvdpvzDe1LI8oMmlsuqr1USfRJlrK-m5I3BAYkOnHccNe_WpK3ji1SewGT0f9klD2A-kOOiFDGFOozGw9jnE3ZeMzHpalJx1os_vTSeeH6-5sN18G8Vg93XdE2rTrkZ1aBvZmnzLaCu_Rf35sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=fLUIgXovr4vGKBQliDORHRFKD-bARUh5aUkR4T8HsCGJm7EGylDO2pMu4upmliqkr3w8GKKA-NR9PRtRLJs9P1gZvVOwSMEMci2n_Hc0v86Rjx03JaIpJIFtOYPYIvcEwlWA-VBQ13SYEmdm-F5QGNeG01LStNK7IADTLqWvqntwDiB4LMw-haGfa7yYo3Ppg7XoJ2y-351FSQ8GEeOkM5Tzmg_AclAu0kWtmxgQcBOm_pmwdcl_AWgvemTK_E6g5GhAvt2v1XaGA-J97lB0jwc87qy3BPQTWmZ2MwIU_OfE-wj0AfcAwym9pqHa3XEjM5J76Bz7Zi3qMXt7U1LHNmTXwLh8AkEE2KiZelRfLN1VHK9Fn-D4p_65hE_mKejp8Po5Ttu9yL6cfIO-yiINuyuU-e4qm5G2I0WcAkjswkmcna3rk6vOsKkyhdzV93iyCJizVAu5JPTxg-1OVunFqgH6FjgeBhxBB5tqbVcr3laKuKp6OAM1GkhOiC8ycTHzFn4sDTOJ_v6gxAo26nCbc1f6pX4TM1sIA9SyfVriauIFm_OtRAncjF_LS7KyVMv28pMEVeI1isXm9i5AQD25b6CnFvBvktTKH7TuUuYfIL5tG5T9ZfjH1ks9vw6uUKVZvtxjdzjWS3TKO_yS7lg_MTNnNJg9_5V2-55LKXOgK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=fLUIgXovr4vGKBQliDORHRFKD-bARUh5aUkR4T8HsCGJm7EGylDO2pMu4upmliqkr3w8GKKA-NR9PRtRLJs9P1gZvVOwSMEMci2n_Hc0v86Rjx03JaIpJIFtOYPYIvcEwlWA-VBQ13SYEmdm-F5QGNeG01LStNK7IADTLqWvqntwDiB4LMw-haGfa7yYo3Ppg7XoJ2y-351FSQ8GEeOkM5Tzmg_AclAu0kWtmxgQcBOm_pmwdcl_AWgvemTK_E6g5GhAvt2v1XaGA-J97lB0jwc87qy3BPQTWmZ2MwIU_OfE-wj0AfcAwym9pqHa3XEjM5J76Bz7Zi3qMXt7U1LHNmTXwLh8AkEE2KiZelRfLN1VHK9Fn-D4p_65hE_mKejp8Po5Ttu9yL6cfIO-yiINuyuU-e4qm5G2I0WcAkjswkmcna3rk6vOsKkyhdzV93iyCJizVAu5JPTxg-1OVunFqgH6FjgeBhxBB5tqbVcr3laKuKp6OAM1GkhOiC8ycTHzFn4sDTOJ_v6gxAo26nCbc1f6pX4TM1sIA9SyfVriauIFm_OtRAncjF_LS7KyVMv28pMEVeI1isXm9i5AQD25b6CnFvBvktTKH7TuUuYfIL5tG5T9ZfjH1ks9vw6uUKVZvtxjdzjWS3TKO_yS7lg_MTNnNJg9_5V2-55LKXOgK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahyulO6QHURTidKFW45Mwih5qg1r2ZBZuLBlAA-1YIl9Vsn3e2l2RgJnVcmsfsOLMXB1n6kSfp8PBfo2r-PNfY9ISusRraae_HbrpOFX-bICE8PRafalWGVtrzPTtiFwMOyNAAOlddBf1x949Fd1HvytAVL-mf-lC1-SYmhrTnUy_VzBN8IdUv9iOKYCmpPHU9X7VB-x-mRU_cSIgr7tX6E-HfDDZBtrhfdrI86Y8YZVvO7jkz8pgujJVlRMWpsGCgbe_qAxfZKxFBm1cvmqWxT9Ahc35sH35_H1PK6ZGxdGH6FF2ahGdxVZrL4GiDdYzTtx0A5MQJwr24EjZtHtyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPqLHeWbCYLRuQF7vkK1-_DZtRw8OH0nI_7dksS9RS0oM6g_WB9x-4HEikgZIx2ndfiID0LiRlw8GLgBJptrm_Kws2vGy_ljAgn46znCmKxvu2uqX0guwoGGuxghV3JrUebQDL9ao_IYIVnWWS6YhXWcgDoeUDLeahw8h11snu9IHxte05sxOYMEvVBmVFKqXEmXbhrbmABCaPp9YN_QR6NSFJ2gV065-4Pe7-13zvzXlNPsxpPf_KSjHHArBQGkGBxzQpCf3w8oWPO6HxZ17x_ls91uhO1s8i-kVPmUtoSCa9JV_wiDB8RDge17Pn-KbJOjyUlqsyVkCD328suozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEejIt_S2HU-6l30CRlKEW7_Tgz3z5hwufQ8wWZeuXTydOc_F1OYGKEM5ckwCfdq-nRtQJP98xl_DqKLUvgmWdoUsmwCSPnbWBaJCev6oyvPUynq21QUjjjQJzJuBGTvADwBdDxX7cCq0P7SkEjKiFfxTIW0rvl1QHBafUmTzpNZIb1W5rgj2kS4vBLzkIsDv4oKYlOjVakjAAn7Pn-G_9Dmnyi9NtCDgcWjR5WypocaqCLmj7T0eRMDBxs_uavC050z8JEUovQdJ2z-RbSd50_yR0niHiZRbFqQrSY74lDU6ROTrGBmJaMNS2FBRbSr0dAbxTbg3411uYgzlSI8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-HVS_qrjotzj1r3XV97AioEjtT1zHNYJ5yxgUGDVDGl5gdvguUrM6T5UIAW7r59rKvfNyuK-wiVNu5az0-oGkCoMZA2Z6T1PN-ceN-lKoQnts6g3NkWDtM8jG1o1UTA8fMflQppN_5atfkJY8dlR-6NemV5POs-3nf6kCBn3fC1euvLPI_5NKWhn0xxTuXZRvCUKqKDazZFMhIl_t2HYKxst87-pkyMdoZ48IwXDkGMtncELX5-JdBxodSZ8VkmT3Gm4IOyFl7GExqgXnXjEoU2OzRRUJmEgN8f-xC_2Ms_ZmCi_V-TIoiHF53UZcvZxtmD_Bzqp2bhnabrlkGxWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKXZCWWCI8F9SIKxxRT2DpcXvhBnN-1c9DQClugfHZ5cJ73NCObeN4encSQes6FtYOEmLvfZHqEX0uFSXoWgCj-rr0hDBO0W4K1W7Z561DmaPuAJytMGxvlpJi1SnPzz_8g7ujGQiFQvbnBa-w09Ma-duuDNJ_ZBgSvBrPzyx_6iQ3Wh10NRVe2G8FTQ6gCek55EAvM9bQkiEMdNk2aquYeeuLDr0iWyjxmxZa-XOCaAHIOmdD_FTZcQ_t2Cs0H4Cby_ImMofzEfR-UxIm8hGrrRHrZgUwzZ5b_hEuFcvY8I6vksfq5soeUKmjXsI4zEWD3mLYPA-Kqq7vjo8o3d-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsn44oXElA4DDXC17p7PuQl0alsw44yaqNPu7VpOjSwSeNwdeUl2Bf59kT2dzKQDwapfitcsIiQUm1BfxoER8WvlITT9n8ZrqRgK6iy6aFSuVrKVW-vmNo4S8LENYldztl7sK_DLjWAtACEqs03fOiNFhI1DJ6PqCP1zkXWU6Fa6ruJTnJEx-nZhxfXiBcjL-u7_sEIDRkA9EqGKffWJ0NcpFayb4Fn6-AaAGDMSnnVrKGn7cUE_45Pna8kmZPulzxtoUczXdMwShyOqucIcuAY3wxR481Y4f0xwxHB_Q99SPqqBNHCPmK90WyyOFRNQeqpxBp_bA3UYNooPDsZCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=SbCxfJa3__ul4BGP53KwBNeSaQXOo_hfnb5Li54N9fS2s0uQKgeug8XAztOROLOm8Hku8iuIcsOLRnPtO6dSMvxUWvIkDp3g71mbz4aA9HZKgatoC_k1a4CgcgGgMSKOpbiIdWckmxuXSwJSopo0IH_jZwLw9xdh_ev9B9N1u3qaGqs_4os2YktbO9ebAzBh4nPmHyXtpsVxbjPfqvTMm0EsbkQNlWO7n0-2d79lpuA2ZCEUBvWIsSlV7fDtw3tA7KKtfIaqzIlPh5kRKyRKbtLbk_B1DTdJ-tkox_1sJrvpeYnOYeWdlJDeVh_yHdeetr-lgXezoQj4FiXHnx1E0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=SbCxfJa3__ul4BGP53KwBNeSaQXOo_hfnb5Li54N9fS2s0uQKgeug8XAztOROLOm8Hku8iuIcsOLRnPtO6dSMvxUWvIkDp3g71mbz4aA9HZKgatoC_k1a4CgcgGgMSKOpbiIdWckmxuXSwJSopo0IH_jZwLw9xdh_ev9B9N1u3qaGqs_4os2YktbO9ebAzBh4nPmHyXtpsVxbjPfqvTMm0EsbkQNlWO7n0-2d79lpuA2ZCEUBvWIsSlV7fDtw3tA7KKtfIaqzIlPh5kRKyRKbtLbk_B1DTdJ-tkox_1sJrvpeYnOYeWdlJDeVh_yHdeetr-lgXezoQj4FiXHnx1E0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBSBkuz37cRM3wIxqYA5fYrVDMxRQ620yXrY33leUjF2mAOF3mJYPYM-flWcyC9brgU_2RiQKg63EHUnKNv16kU6PImHVtS921ouaT4f05XYvGJL315PCjdTPfE8050jjPkTUqaAPu98NzX7Dr2-9aFoJEXGrZA_E0Ljm13bP8rdhXFfdEQ1CHENGg-OTgL-ViM_5jJfq7ukIhoggNnn6ApQvGK68OYzHZGimRKt77WniomxaZ0q8woSjagTZlOu7lQFJmkGh_vAfJ55BcFcjYG-PS3gnktAdOFtLiq15pOhU7KhqrN66Yi5uXf1zmiICvDk4oAIanZM78gRpoIutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAd4Yzui5sTRf1eeulsroxWgM3fxlnoU7iv9kQMcVPBzU6RQMSBrvO1oDMF3erKV9KHWv6_kdAA_QMCmuV-WjljFp37KO9m5m1f5FSo6FOXJKXKNTI75992LPZXimNsdNIC5pF_XIoE4fWHNHTV8z3_RFBiLgdpljjhVq7DHFYLXRPV5SPFW15hAZg9udG1aRi5yfzQB15T1hRDJHDGAKCGU8SsxD9tgl8DSNX6uNLDnUiQEs4ufg4I-fjjPH33a0UYUkp93hjNsgNxqRp9W6xxBetDIk-oFczO2mTFm3PkPQ7E2UMNUDmflZ_0mQ6K2qXoBq69LTaf-jfFxx77Yxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7qWKUcSwIifXvlkfIR-TCEwsyLIKx3pkIFcZlDyVO5jYqY0ShE23qudrf0HMog1p5Sh8-asbqxIcy3valDkx-505Ivy3RrC69b21FOcYZIAPaRe9yl2TN0Toc3u4-Bj6YAqBGYwmDSY7cZ74BQPLgC5oHkWFSxWkfBNTm5JtV8yXAjkNcTFtdJGCWlX5hAWL_3nZ-21h5NQuqze81vTNhKgeZjs8jVGLYQ-lNlcLuEC-KVfb0pWJlOjKQvfernov-92ctd0Fy6rsWbF0BsuSMGY2aAqX3Uj7qP35qDXXCTYvfoHgHLRC4Qx1iFJZ-b0sWIaDs7BpxWkFojnppM0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjLTQp-BPkOPIfOl5vsWVCiMFWPSswJ-EZoK0YiAQT4FtF54QjgMUk9IWu9FJgPCZlXlz6OqHdbPl2T8JyQ8ayng5TwM8W3es0KOHXXrchuRlR7fBk0qkrIQMtDg5m36_nSD0EBkVnU4AWH5vnv9_c7OvRvZ_rt_pqw1XIh7_XSYdW_308WJrQUPrVz8KLncPY0S7yS9mri0drbU8Bf4I5888S16nxwtqW9usqKH80yOFu_fxxB_U5nBWnZMNk0VuwJLyvXhg1af4xwcmDN1ONQvn6YCHUdMXXSWO4KLrjv5eR--m7cTEIY25J588i7Sx5dw3uS9pKFzdzUAxU9Wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPeuFF9DGa3OT7388Gdvcg3M7MIDutyXjKHBHbQ54zUJ2OExS8VrEuSonJLAW0-fRsfJwNwrC2BvzcEFpXxeT0j3hgyWLimKdn4-RyX4xL-xk3xXjAjqT7rQ4A37DbrGyup9QqPl274ILgTcSSfqMEVb4min4PUZBQSASgbEbvOOTojU8RvTF-neMOoCdM_Oon9LCmBaHqEVk00U3RQr_L60UbWDJ4M2oX-KOJBbHESVC5I-9JjgumEaZmXfaRGqENr6yBSbLN6OiqzJIHBMGRn1SigAgWUdvoTsN1mwpOe7wbMF4URYq2rpkV4Jj7RPrVtyQONTs9tS2YrS9Dnh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaN-pvc9J_l510JyPHJJgPVbqF30AxDsxDpop1wrnMHZMuj3-iweWLqislB_WAq0gxKdlBs3zH465e416q3itB51LYchtrPgFyIsxwWUh7XxO-HSxl6h1O6FPtdtWRrcrH-wSlwpNIdXJxydrVYLn87euPwD4i2SEHxDjLA0DY0iu8OEb03ufHPCmpq96oJdheh9q9HH3JH3pvKThbWujcTocg7gQaaS4LLWG8Pi_01Wvhii0FW8jO49mvLB2QNO0rw9YYTpzJx-yALF-mLX5Ajxg7VrSy7ehrkgrsviKshzUTqL_3gRO0QWU6SkRmiSFmF6qh_yibYU52Glgiq_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvNiEsu7UHVXm692020RpMCNQGyljKJDvk-J7qHUa0HQpBU3tfONC5crLqlR3LCUZ8VPKCeRuJmH-PKcwK3HQNa5acP28wVa7wr2ON0SQUGoOc742_aj7qCO_Wbiq0YDpPbuY-MUDouNIK1c8A5U3MJNYzxCZUeJ1m89aJe0VsA8AVs_OJ4EbL7pNOBLNbfw9-fVyY9t_vRx2xnbsi9AVSgnii8IIb5HKkyvC0RJ9hlkZG5k3qhXh-RtR30WxARObme6M2GwkePvpdJnqLQzTcnbscXvjuuJfMKsDMh9ZesYjmtN4HQ-GbVD4e1BYoeEsfLwm9XwHA6n-LS18k6Y9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeKMZMPeYWgm2Pdc2B0Q2NMiEjCQqOnN-fCPKyVU9W8JPpMTxHQik4_w7fFASADiy4wJxCXOzh07Z3VZOeJbmihLsDUVgB-7q931wyvrQhGvjHpLYPhI_mpRfjbuqWkSNKIJvDn6o2oQy78gY14zrX9zKIKYqqypu4dIy3KelTwjOY2RfjKHyND8Fy7ndK3Qk3hS1vWpIV1VgE0BkeQoiwdk7V0_dxxD9GhxzIa9u9QIbMFr_EtqqPRhKSx7iNlMsCa5Rfj7EhR7mT_gSnAl_ws1FBSJLAR2hS_0tDYlCyT_h8sY3dv98ozTFzS4F5pkIpV3ibKe20TG3oFscILjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-U45iyvMgyUeSP71Rw43gDxpi7Jt0vNrjifDHEO4sgwHpNrA-hXbbuWWdGHCJDrclK0G4_928Zk90P0x0HfLwjG1BOmundq9BgU3HIFWtclxyVfZ_O8bFCeUhSKvlK2lWUkdL8aG5qoJn4_hpRyT3NcZG0aPm8pdEhOOOlY4_DsJEi9yY55FlsZFdFlfDHBJPhQAttuE6pm1vukJXpWelXlRsv8yLm0AGkIt_uCcNdDh-7OzePdz02dShoG9S7CXLGP4V5tUwbbx3W6XRQeToKFyWdqCDKCsMCYYNAdmGMudrkR9t4rleAKzv1E4aEidsvA2Qbf8H33TRDKf8n_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPfrXJTZzkPYeqUJb23WpIF8wykuDzuXqQ8k34WhY7MqyGIGL0qzJooZ433VJTykZ_EIN-AzFQlQf4pvDQQW2JQDynh_k04QhmBF2TUzn3fOauSj9pMTzGGjKlx401z_LFwmWvUQFv5Xc1qN3RIq_0SYxGXlsiofcTm4leq_ghjCARlffqZAOIPHviq77QqjJBq99Di-J7Cr-CtneQybCnEc3XW4ZKym37t0ofBcKZSAZR-7wnhoBPznWRqYL4PtoesnoRPSXZlypQYayMPys0t1_OyVHDukpYM5t4HLwvlZBSnclIpgoaNQGI0sxwcwa99eXSKNhjPBrqVgPjMWvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=n22fcFIPNXb86jCIymIGWi8pvc38Lhl8gHGECilEqJpsMW5d7f6DZFRKcgfj6G-_gNOLOv2yjFDqGLbgdj56vjUUML3huQpBaDOiXSns-S3y_flchXIkpaAKsNWGzeOuk_9eTedZLwUa-fQoYcDXygi-3tjSMWX7HdkC0euNdCdjNjcfrVqacFoZBzqG4HVQwIMosWyVJOUFuKbsi2NFTIqvW4z6ZTRgJGR9bPEI9pKkxQzcKb7Nj0LRHDkuaBefNw3yBoS97JOlbCUWYkvg0cIl1xitR4xH-nH8aAxcLAkeeWbnd5HCicmPJk4HpzWnuUhZCHnY-dhYKq2Hu767RxHJsI8dcrufnOkvkmO_thLQgzkOqI7I7KUEHuoFDyJF56qxCiLXImuTWCnw7G6tiLbTRgJ2B1pxcg6G7OCyyFi2B6lb7E9sE3mQ_MjwFicdA_Z8YP24FSz7Z8IFinRPR1CU-9nxK4bpXb190y25RDfOLvUCcTcPxUu2P3itSVl4keYFf6aVqqwZDv9MSilg4pA_VRIKOIyWU5L6evBSsP6ZluVKvv-nAS8OYzHrz0Ggkv1FFJVA-Hyonfe7rmdxa4mmXvhvrFGPjOKqISqsgBdmbWE7G_YFmN8RgPx-NYJTq7FFrHh1u-4wbOnx_mZvu8opR5inw7i0NZfaTex3V40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=n22fcFIPNXb86jCIymIGWi8pvc38Lhl8gHGECilEqJpsMW5d7f6DZFRKcgfj6G-_gNOLOv2yjFDqGLbgdj56vjUUML3huQpBaDOiXSns-S3y_flchXIkpaAKsNWGzeOuk_9eTedZLwUa-fQoYcDXygi-3tjSMWX7HdkC0euNdCdjNjcfrVqacFoZBzqG4HVQwIMosWyVJOUFuKbsi2NFTIqvW4z6ZTRgJGR9bPEI9pKkxQzcKb7Nj0LRHDkuaBefNw3yBoS97JOlbCUWYkvg0cIl1xitR4xH-nH8aAxcLAkeeWbnd5HCicmPJk4HpzWnuUhZCHnY-dhYKq2Hu767RxHJsI8dcrufnOkvkmO_thLQgzkOqI7I7KUEHuoFDyJF56qxCiLXImuTWCnw7G6tiLbTRgJ2B1pxcg6G7OCyyFi2B6lb7E9sE3mQ_MjwFicdA_Z8YP24FSz7Z8IFinRPR1CU-9nxK4bpXb190y25RDfOLvUCcTcPxUu2P3itSVl4keYFf6aVqqwZDv9MSilg4pA_VRIKOIyWU5L6evBSsP6ZluVKvv-nAS8OYzHrz0Ggkv1FFJVA-Hyonfe7rmdxa4mmXvhvrFGPjOKqISqsgBdmbWE7G_YFmN8RgPx-NYJTq7FFrHh1u-4wbOnx_mZvu8opR5inw7i0NZfaTex3V40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBdpJ9NMSfj-sUDhcRpnm00kfF00f24LtCCUPLFBSvI5Z3T9h6N72HrrhCUkrYCDEzUq2Q5kZYqRnZ_rbUuccYTy_H7lenSdplbLZMOKlUbp4l63BasKwxeJNmEVf_u2MrJ3xC6ZJ4oXv45VcZ5QWcB2cVw-n3RzhSAj-JIREJoXsm9fzmpCpHTVEsAtqdsV33zKI9WuU5YHS7S25aLtLzdAdiTCmoJHnoUlALHBETGDa_JczwRHRt49a7QMgpDO9YPGSURuBOBPrQdwM7fm6gH5Y1Owsj_2XFYO_JGTaZWVcE3FiTyhCgMiKc36o9Jrfwat6OAloq18kL3Lz79ugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptvQAKjzkl8Kts5GqU7ZodHt34UePRKt1RAjq0_PyyDyvqgamtXX6M8W7U4BdPQMET3UxCH9YG1zoZ8tf5KfZH2KTz9Gu2iTygwGWvpQX1LpFGTDrCx5DEuSNDb9-lZ3O4RlkDBQDIeL5cRoELzFlvyZnlXAnzwbrBjI7VwkRb2rbEuNG8cyjilTYOQZsmrLg3AyBb786ubBG4A2cHRTHOdXW1ix_T09d3YZZ9SO8NAdIWv_qPj_l-FeFeiml8NG9Hk7xxjAKwctPxfbb6lOYtWssOrTzFXd4HgDBbBHpnsOha_X_mj_NkH4J-5y1XAfJ7QSSUF-4aUsUFnzSdwSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHNuHt8SKixIkeX3b6YVOaX6ngVMIwPNbf_lIcjHfEes37g91teTgSKlyEHdd3fGPtshCkim-8x7VKA05GXmRX60MeG-dWkoYW5UXFT8z15cNRLYmNFmXF5HyhrSUiG4ZQd5UjOHTRhbVT9RcbzrYQ9qGOY5ZTgr-CHSGEqjLhjQzRhUGCwTOAjwWIBZgiIXOGP8YMcxR-nl5kUExRcL26zwmGiD-LTWwzAavHQ5BiURi_32sZP-Hp6XFISTQcy0igmns2ydUlr2h47unXW7KcE693U0rX9KSTOlQKdSWpUo0jFVGnyswXlZvKUPP85GIJjavBhih33onngY_nYfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgAxWHXqpRmKjV0CWEq_8HZGdXONAuOi0NjEUPr1gECgLUPE2gCoYBWDRiLS-IN79MdvzAmg6Gj4bgHxG-_9-Fm4Bc5NKRAp0XzwVLDQFTHhuYY2K6V1Fcy0LNTb2AXqL8OLy5o0AOWhJgmJe8W763Tt8w4L1QBnnAifEnSifID757v8xZc2NEI0X5q1FEXCsP52kWwYYhElw79k8scGdQEbol-IIzGz9mVlxYA9BeBUjHVb3dt4ZCm7Y4tpA1wdX0s6DpvbczWzF7uViOqzgSdcWdXsYSRci5OMUoXb5uoUI6JsZEGhTWxHyGdk-w05Ikd88j6kyzUd_ysLe0z_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctD-W_D9MKhAW0MJi4x5YGqU7tCJp3QUwAISY9vHmSxBUlJD0Tt8EFXTPOhGDpMTg1zRC4jHeNdXpPYN7OUKE4NHDnXBSemsDuhjKik7cvgbX4fK7twOxsSGsLD0eat8wPlH4h8zTuR22wikXYDpHSlFZkdjtRWQBLWPGNPBRJyn0a3YuaY7DjuSBS-RKZ1MizR4RZMB-1SrFj6iHYD-NeITlYMcUNG4Tx3MN-5hOE9V_RDUm8KTTtNQKeux0jMNU6ZrMtUAYiJVu-5J8fliOYGFd1VrsCCloYB2JfFMh34i9WlB2BJLVkR62M1DTQJTqrO89wG0FjpO-c4spdmvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm3X9Ko-27MJRtjm6gOTu-JbxnzjkqLcIkmfTXv1UIFw3SBWcz_vmbks2xVIN91ftP_9w5uJbcx-tGVKIJjKZESUVctUF4bSQOisUk5HhQipVTgiYyUXMz-K1d8o55A7ciL8PthZa0FuKBCxrM4XOw9rR__9O0YRdqZaXCcr-zkjqWdohZLvl-jMaAu2o96xZcZgFKZI5QnDRk_uqpFhXIFx_ZJ4I5FJGIXL2Vu8bWvEUQpj2Q1UQLIzE5S91jfKTE8l83cj7IitFZnmHcRecVFwpuWLT_jb3TxRq7wp5cD330RgnlDiC9KStSLip8mcfHB3bpF55JhuNISp_1F_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJELN2a8CDx7HqoLci9Oxp3xcUEHfQUqqqvsy6nGXsPlN_xge6nNSaGa0yRyy1uXo2ivoTIo2yKj3kDwD9ZECCp01EZ3cRt4kZXeprYMhWsF4cfetU88cdAcsFOSNMGFbnKH-wqjiKxDu7o--790kJiM-ftcweviuQvXn-lEUe2bGXjuO0eGFE9YrWZXe6su6ZowJ1kMctgf3jrDMVbDcotd36XnJqZzkNQsIhR4i3AJu1mai9RdrOaYUEGM50nBes4f6ritiLUl4CK9H9JCFpQLk1Th-lUXEtXPcFzSs7_lUfW5H9sNtEAoliEQyeKtGC50j_Si8JKpB_XWp5oPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=o011y-M2HUTcy_o8kUuoDX42R4DG5hWu90krAzNrET7ASb89gPm44Crax5dFORdbkRTMBZj5H2xNLOfPtwBuHxH83B6ZxXFBQZMmV1fBxQhWYGjBDuEF1hh130vD5_ihGU_Sy1jDmoYmYziIGtT8KOqiR36TF6LXku6avZxdSjHXMZ3UT2eowEw0oso-cApGWa4zbBBhCA3dhqS1QBfQoekmqqsMaxbWnMN7TMelUMtV6e6n6ZiEdweS38xxtKb1bZOWVtnkC0ob7gcV9wNCbuQ9LJJfeljrFEtcTH6jCErH84ywWUUJifOMIPYV1vHirVAtswoyGLnAPqlATxMzrQVB0MS5ZgyyKfWIZPPKJ_QZQCVRRePSibwqs7WUc_z8DS6k4ndW-yhlNm3IrqduG-dEkpUv8UApS9bxfveS-w_B88wZ-BXZTceG066pNW58nBViMk7AAYysF0_AvQJbCX6E2c4IiTE4j62i2-hb_PXHmi0DwzLHTYnlwcQaVTfzU4TcWSQpCifd2q29dbhxIoWc0j-RM183EHhyZuEMUqQHvpPWZx8SojKNd5Vzcs6XxmeMlRylLE5WDHYnZOmwg7o1pSFX9QM-JMncd6QZcW7LlfUOD8DkIAZogVm6PaKiWHEpk7rmRDfbrxKY1WctHBIRabeFhgV0FTkzuqWCIsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxE0fkT5PHrakg40wVCyP_qauHMCHb_HpltjXteg7CnbdUksJKaa7OQVmZ-k7v46G577Gc7CTPrt7gbTHoCUMltMe3ZkSPxuFRib9aesEQ-Cwi-Zu1JkWuKY_yLADifTJbJlgFlGO9aS03Sg7Ut85MRj9hMQqWfO1mZIXLkjW4zbZBbpE6spBGk5yltdifxNxRHulqMJhPpseNMSSLXmxOyl7A4bjFT_vlLYAyVQVAd5jwWasPxB1EJeMXDVHw1EA2Up67eeT0ZZcsSysltlppcek-gL1I8k_oUw4Qo6sTSAelxhd1ciEYEXwNykshv-_q98850_grf8E3gDTi4dLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26453">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJ8L8YCowZcH7WxY2oitFW5ce4Ws2-gJ4AQU1CKthiOf7d-ZGCY_nV6rZC1gx9m8qvnvkxWCOcJLHwFDDphDYNFP7OWyJu67Yivbbv2NE1TzvRtWiXlmtnxuPR_Z-9v86mzbIn_f60CAGnvqFOdJreq8HXyRgLl_7FmcJk2mY6W552dXcNsWNUgX9r0ZPVDqg8tgviiVb0AAaTxAl3h27ScP6XmF2hnN5lL7pLkkzoAWnG7LhXewfvKmcq_ZlDAibVd-tlvE8ZcmPiCUHyawuLTyMHx9baSxc2OTvrR4P6bnpDkldv7MnKEYNs5fW2heRrLyYjerNsSE6GFI458iow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو: باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26453" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26452">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdDT9STtD4eMwMAAUvrXOoraGrvWGgrGkLPk6d-V-5ZmiL5s_KSZw-yhCgVtX-9uGWvvqUUr5SXw0IGJYx3kkfbmu0aHCeX1Qe5KNf_yNyIKY6cl4zyu3MY5cjkdwe-dAvHtM-vuX2C8H0Bdm50peDgekrzfdXBwougSTAsubB51YZ_z8BVpaXCgZsOPqh58xawWstWG3GGxNsQLUDAFpKLXPduxZoSOctQNMvkYsS-aBjy8Suct7wM4F2hhr_5uZPfaTJCnoljUvRx8EIn5FJ-eekOHf2eah-qs3NfIUZfCLY7qlb0usTw_kwFEZVkf1_mmf9WMG_8ULazx6R3Y6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فابریزیو رومانو:
باشگاه رئال مادرید بعد از توافق‌شخصی با یان دیومانده وینگر راست 19 ساله تیم ملی ساحل‌عاج؛ پیشنهادی 100 میلیون یورویی به‌باشگاه لایپزیگ داده‌است که این آفر رد شده. حالا باشگاه آلمانی گفته برای فروش دیومانده ما رقمی بسیار بیشتر از 100 میلیون یورو میخواهیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26452" target="_blank">📅 00:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26451">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajfh7a0LjA2AYZVwGIUCHUBG-2NlfxaaMOCeCC59FHD3nYK9vqEBh2TZPX483AOnCCzlSvie4fUhgEj9MMGz3xHlZ9sPneTT8mmTSsQp7WGUlEf3ElBHo3-7zzdkGLjv25PIrq3tgVWmz-Vt1bFX_oILbkQQ8-9wCP9RxnIQeWMuyX6ZBHf8ZA2o7OoIb6Psnfa1JWagBXVS5NUw5cA4XUDzAom8TsBn-xVXj80awqm-vDFsBQ93mf1wVdg7Z-C7FCCXEzzwO37FK60Va6wjexZFVPc07oLbI107-LpuHO706mfurSyiDthXIzDVawSdeHn2S-Mjuf8ICWrynDkyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26451" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26450">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHUEDzAftjXeReDE1cjlteSHSQtO0RCakko1GNy3QGL1yZdpoDVhBGSNOYHaICgJjPNo9wpFmg-fLOfLKeMxtIOI1uybVhuEAd_6PmgWHir_F2a-p7-d6iPRfAOct26lyGRWuLlHtKl1XYJ9Y5XQgWMaKGxGp12xrcqc9khZD4rYhwjWODLv40vsXaWY0elV71XYToYqEr9tMuN773AT-hv_bkV6iG9h8jkqzlzMhO4AwgR7wE1UPSHWJlMzcjy6hz73luAsEwpwXd0awkMqR-4rGbG78mViJsEK8Zo2ai4s5-qdZBGc9tB8eEpV1KGWLoK-OYUbB_GBWtxxKlNItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26450" target="_blank">📅 00:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26448">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1MDMgPNcK8ve0GhN9Es36wiugKkCtf3q-zSi_sQoaJn1ThYLh4ifVP9Ww06y2Wi0OW-3ElwPbsMcNrS6vYKAxVK-_bMaxVlhAO1MtorYNbigWRj2pTdA56RBJu3ZMmL0l2xiZFJg80EkWAIIqzailjdwirY-1v3pzoSwQ_kRCyLHCf2c0p_IRWh0C0KqKgkWOJoDdC0mnrQFXDC3hj1rAqcFM2ooBeJG1DMLHleke4tXLoH4aminjXq8ezzhbz-F7h7ZL9lxMA_l_Uj5kNG86iZgO4dcR_dk4Pas_8_ds_JpnKBDROlVYEQ_7qWvMDnulq_zOkpT6D1CxlfA72b3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26448" target="_blank">📅 00:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26447">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sppU2PGm94XunUz2BoNLGbxL6dIJlUndknPbHu7N4OnKoqzkpsdyTXnjCn1f9zOHft1O-VJ3IuLwdR2Ld8MBgLNVN77veN91WBJXIbAJS2qxQNy_cfxcQ98QQjU1Lfl5rTlglpHaYanAZHkMvRgRwNv9kUz41gGlCXtX4yppJB_tYOEYDKM6klaq1y5Msg4uUdt6H8D3RK-8nTCGK_suU6SAj21OWv1nxxB0tZwWNTRvTLmE7UNZa3-f4pWwWU___-BSYSPXii5DHqrhfPNmdNt9cnTabDLVdC0xCw80SFOiksfnM5lY4EYNhmqyoTZ8BwvCYZFTaAUPRLCnkQENmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26447" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26446">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqLF_NOr5Y_YlQaxJQHDXO-RR-8UJRotWw7KV6IegcFb4NpwQ2Cy5wpiLKbtcq-vIduYT75V-zSRC2K_0A5zhzRXZQyuYBHIs5EEswDp0ybbKh3rYBiqK26X1Mk2bW2zaUkvcyU_TLbmxlx8RysqrXFRw6rW4TWAIRsC7tnUEx2PMPHonUvWCcsQEmRv7CNdYceNEh9YoqlDBsvF17RDtyzpgoOpo8xkana2IN0B-tC6OjscfGB9bAY5BMnvQ9mATThXrv4UyCJupv9IYHD1jNDXZXNYMbqjE1CB2wUdB_TKigs-_mBGdUzcYe65PCbGtdla9OrF2xsCw4mJSQd1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26446" target="_blank">📅 00:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26445">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zglf_DhIxh9G4PoctVWoz1eJOP-GRazFrOANph47SwYasnuPxPpUw1y1kRi5gDP9dZ6t4jwIuLhMpin-oeSNp8Ei6irA_qictIr6uj4CxGVGwqItr5bRN9_P7V-FyADe6B49iQW_i8UbvUFD-WFywMDXgRvpNwkCELwZbCFRrfGM3d0MWjjb74Tb9rfpY44RkW9JfeQUydo9gWddo2dTdT7kZyrHcA-HDuPrXO_wcqLYnJu-9Pdefk6RIIspcICna1wSA3o73zJU0Si_uSRIvwkO_3ZUhLSs0A2amZSbU4-fJ18nrOw5qooW0Ykoq54B4Y2n3Lra0NJoxQyLpjZMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیریت‌‌باشگاه‌پرسپولیس برای محمد رضا اخباری،کسری‌طاهری،دانیال‌ایری و پوریا لطیفی فر 4 خرید جدیدخود بلیط‌گرفته و بزودی این چهار بازیکن جدیدنیز به‌اردوی سرخ‌ها‌اضافه‌خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26445" target="_blank">📅 23:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26444">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtCULiPyy4B8YhNNn19Lgl8BDoxu7_A6MCySwCXilr-rvClNyvKhAjGDRCHA-cxMEqIMMDEwGeBIN0VTSBU-prt8tLStIPwaCsTq7YzRnMskwXhASLgFdglzl4aZL6bhQMqsXrvWW9WLQMzwQk80lNG29rwaUsrA7K03pEj7qHHJYB9OOeXnrYMDr9vZvZxnipjQsL8kajHKlzPN8LhRo0az11XKe4G-ms4LAlW-7E0CYw_3FD6VtSvY12gg-Mjy6fOZlabf8Gwiyth_XJT0Q8dX-WidkgOmY-aNxCYJC-TSIN8dapE5Pu7jVdhifaSH2HDYQksodRGkqmbbT64izw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🇮🇷
بااعلام ایجنت درترانسفرمارکت؛ رامین رضاییان ستاره 36 ساله‌استقلال رسما ازجمع آبی‌ها جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26444" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26443">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8P6EMF-2k3lurxAdfQ9APqeVhXTD306i4NI6Z7mwmIiH127HZT4si28_iR4gGi_leebLYBa9ImoZQkXoTfarUi1B-yIryHseYIzTxw6MxsxS0R1RjLKLAp8Y4p3JazGS7AVY-4GkUp0H67rKFxuFCqFzCDWbVdrwtS8Vtfzo3yqENBSRIHcExyb68qh9YcLbLFLm7KdKRzhZXbp7GpTkMJmBro3tjd01oQOM7YSzYk285BJWpvMtYOyuN3WO9EHM8bsbGMu4nekxoUN1fPFixQ-u06bflusc53ERKtsusl-129leuA2p2XA9F-xbXJyKrx-PpmdpWp5zxj1KhKEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26443" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26442">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z42P6HyziikmauQYdCLv56lDP4jscCwoaaJCPBF_wMPgs_R0UVe5PenVNEbTW229BXQ4MJaydwqRRkmupTrmYYQkZQYN9OhOOFnlExiC0VFdC7YGRI-ENnsn-fvLREi0Qa8IHmpGorND6HQqI9Ms3AmHL3eF5kr7bi5KLOQqIttrCsmIhCELWjsNSZkj1trW94lvhTaaWEGCMnsjPXf_J7RlzAAab9A6u3t0JIglinDaX3L0nW13aQBKEcNnPgyS1K4s8bl0P4PouudftJoakPeeO27e-86IuNLedgb-qrpQ_djN5U0U3p3pnatu3CXjQ1-bkk_NcF38MWmRSyWbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق اخبار دریافتی پرشیانا از مدیریت‌باشگاه‌پرسپولیس؛ فردا رضایت‌نامه دانیال ایری و کسری‌طاهری‌توسط‌‌نساجی برای سرخپوشان پایتخت صادرخواهدکرد. محمدرضا اخباری و پوریا لطیفی فر نیز دراین‌هفته رونمایی میشوند. اما برای پست دفاع چپ‌هنوزتوافق‌نهایی حاصل…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26442" target="_blank">📅 23:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26441">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7M-HBElAOatAwJlWtzGi6MedaWFLEacSOwc4fptUyJWqlLYAyzdkNoOwNkDZeR6sgNQHht0U6yGKd6hrDo1Rf9XMy3ONvxeUs5oc5NVdvEl10_rG8Xr0UxY2Wzsq02AGnkyEYHw5tW5icGbt9qWcghChf04oYzre6KDp-VMQ5HealQ7Cm8CN4LwXjgm2Bnq9gcKkqVm1h_dM1heVrkXqvn_jRS2dwv7CVOMBpdkTRCwvZ94ZrLDInMlaOMDOuNH1HfScWtku8xnlkSwSJKl-WkvTs90tvqqAcw0WBY6_zD34cuvG52952ybNEHj2HXik45bH_vpzjsL4rpLWuPZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
افشاگری جالب زلاتان ابراهیموویچ:
وقتی میخواستیم‌بریم‌استادیوم برای‌دیدن بازی فینال سوار هلیکوپتر شدیم و باید اعتراف کنم که از ترس خودم روخراب‌کرده‌بودم که یهو یادم اومد اگه سقوط کنیم هانری هم میمیره و این از استرسم کم کرد. با خودم میگفتم زلاتا‌ن نگران نباش تو بمیری‌ هانریم میمره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26441" target="_blank">📅 22:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26440">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=GvPSEDXk9tBmwiyqmutq9zga9LYVO9S_6-xynrd2if-kfNmeMOHbkgjrlmOYu3j0fusBZp832pTkhlktUpvqzhD23FrGYU41w3GDIjJv83RC9GLneedHJW888Y8PDtyjNIJnXCNqnEgJWV1Z3YmIMBkLjO3D7mVDiVD14WMSBEuiqNJZ5NoNZfonmlSG1-1b_gZVlGsTq6g37Sq82SwUUzNo6336Tl0X-6uO7xSLthuKqbK76nXNz-_nkxGzFt0pfQecajoPxx9mlFsDI_4CWv7Jsf96JC-l33sxgh7NL-Wh7pZXJ7Jk2ID56DH_CvM8CvCEBiWoZk7rvSZ92yojsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3dee6971.mp4?token=GvPSEDXk9tBmwiyqmutq9zga9LYVO9S_6-xynrd2if-kfNmeMOHbkgjrlmOYu3j0fusBZp832pTkhlktUpvqzhD23FrGYU41w3GDIjJv83RC9GLneedHJW888Y8PDtyjNIJnXCNqnEgJWV1Z3YmIMBkLjO3D7mVDiVD14WMSBEuiqNJZ5NoNZfonmlSG1-1b_gZVlGsTq6g37Sq82SwUUzNo6336Tl0X-6uO7xSLthuKqbK76nXNz-_nkxGzFt0pfQecajoPxx9mlFsDI_4CWv7Jsf96JC-l33sxgh7NL-Wh7pZXJ7Jk2ID56DH_CvM8CvCEBiWoZk7rvSZ92yojsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26440" target="_blank">📅 22:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26439">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRsaBUCeKoD04uTdYKPsbWKdNWG52PJoU12ciPkVB_xc-YvxUpXqIaJirIikbRkLsX-g2MP1OGQWwQASXjwmDNfxMKzM8dsOCgC0MjOKHj0Koi1IL98R4TeZxTfOrgD-qozEvmwwrniSMnRrlO2G0_CS6-2o8uDDL4Y2o4_9JAZrM0qf6vJIoOzqkXZTiC8J1jXR_OXYAHkscLSlpCVeu6_d9H7cTWd1NDZ8VKUKsDSkYzqhAG01tspw-E9uGpZVCJnP75KfxJoNVbABt3PcixLZZdF3tsPAAsLRv9b8pJ9_HOvbI-abng50lEmNa-DTju4AJuHA81O5AYrAbHOnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
دیوید اورنشتاین: رئال مذاکرات‌رسمی خود را برای جذب رودری ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی آغاز کرده‌است. سران باشگاه رئال مادرید از جذب رودی اطمینان کامل دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26439" target="_blank">📅 22:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26438">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWDq0etU-1GTWfVhPGbgPN_rqOAI-qt9Z2XBjzCGh6NBh8NzAfvEHs3O4NC5evyN7-f9qvhAyQcUvmWi8mmxZS-mQjbv71vo6BXTO56k0TYitmrfRFdDAzW4noDGpLPX0pe_4CzoAS6AUZ86HstwQxeQDWgy8HGl6rYomhLnrfnthSQHZmpP_ez8KUVb_aY3uJ391AVEEpWKyCvd9DxySdkscScvM6zlrItn5CYuP_93Sf9SXfWi8y2XubnxQKfOBCyU8MWjCNJrH0MDOMz4GF8dHtvxP8YrsYk9OS5msOp9qSK0WcwfEU-feRpNhT_vur2jZrW5MLGsdBowBolndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باشگاه رئال مادرید با رودری ستاره تیم ملی اسپانیا به توافق کامل رسیده است و حالا فقط توافق به منچسترسیتی برای‌این انتقال باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26438" target="_blank">📅 21:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26437">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCk1KA2VkjcCnttIP67pMWq1OA3ibWOOC7TTzEZiGIi9hrBeIgxKNVrY81s7qVOwBS5Gn8A1f4HzsWCHJ1W4uOLojRQT6fPVNDLobWnS1ekgJ-48EWhUTtdV2JQunSLh-4H3YC9IqGnpYjuaMYYywF1VmBWAfJ7XDVeZlgJQp68d7bz5vblx7lwG2wfvSTq56KkR3FsdELE7jymiDG4dEs53BfDU6BUgQhRIBaUKDG2V3LyHGKBQ1N_CBS9GB9QEMuHGkosUIoBNGwRKpCVc3bEbb8F_uxgmXonvX6hyNdmvfhiIOnPE8UjpClPAPrTIObekub-VpZALhNKhZHSbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26437" target="_blank">📅 21:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26436">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxklqkcAZHP40recPnW_j60wbZJ5xp4wExjYES6p9vbj1UUfSf9UPdWHzRul7RxigTbC7VbHJ1QMseZgPueIj4rXSNrnMnjzwGZuxfzPaawbYLdEE_WmL-cOTWUF91Sk-dpamQD6PHbWBXNt2jmcaESa0Rux38lSzhbdMkWG9Qxo4YNgJNWQW92FXcv7O4lC-iX_ygmFu2tXeQd7-fmc0HzikbYXGC544jjgX27WSaHnNnr6SAFIoRHJbLwLEe22X5Re45mOR6BjooIf4xsEp91ea78_5hxAhe-HCSh-kg2kNDTjkxyfzV9OIgkopYUf33Hhln6_Lf8Zl1L5Cheg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26436" target="_blank">📅 21:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26435">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=Dsmf7dqOKAQkW3nlNnr4TJvkm2zgAdxW_re7KHrfRSvf7h_jWBz8_kFyQAPVcmWR36qM2ONoD822iWNBr7pBaz9JqfrXkTrp0EA1DC2SuqOFAR2v59a3mbBb6Pg44ax44nh3wO1NSaysmPNMAH6kPnkITkSSHsFDyUBAx7_hQ74QqGLvDSZr3p76aiZ6mBTEkVl8CdITSkaYGTL3rdHA3hyNNCLmHB0ouPOHk7uMJYbaU-T5uJqlYumW2iYOz7iXqxjr7pv1R-LPdvvmMpaopNGFl1FgiXp5If-n-2WV2IvLgeRj3iZ67P3IBgvZXJwqaFVLZG01iLbZSOXXGSNtzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b4ce1c09.mp4?token=Dsmf7dqOKAQkW3nlNnr4TJvkm2zgAdxW_re7KHrfRSvf7h_jWBz8_kFyQAPVcmWR36qM2ONoD822iWNBr7pBaz9JqfrXkTrp0EA1DC2SuqOFAR2v59a3mbBb6Pg44ax44nh3wO1NSaysmPNMAH6kPnkITkSSHsFDyUBAx7_hQ74QqGLvDSZr3p76aiZ6mBTEkVl8CdITSkaYGTL3rdHA3hyNNCLmHB0ouPOHk7uMJYbaU-T5uJqlYumW2iYOz7iXqxjr7pv1R-LPdvvmMpaopNGFl1FgiXp5If-n-2WV2IvLgeRj3iZ67P3IBgvZXJwqaFVLZG01iLbZSOXXGSNtzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26435" target="_blank">📅 21:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26434">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beyHWAD8G6t7XkSNLbh4Djim4KndlIk_Ykx4Whhpqljpauj_Z_qCEwLBa-CwbUWKFPrZaTzl39ZAr6Ci7-Bd0lloIhhlK6--dk5VhpDjDhEvq8fvUV06aSag1Y3fJ-RIDV5loKBvm-XhdHJ8yX_AXXUyfGy4mlfFjc4gc6yYU7xumqZWAGEp3Lo2v7UBgmVmFWiafkY23oXyzDbmOlCKypVM-6l8WFgtvVuhrXmUtYyYU49sX290nxE7XqubcpIqe3PSQxlMjytOPIYlkazbB1C3whEf5xtdIHwwC9APmZq9DmGQsHDl8E6sUM4D4DfkYRBMQ79QITBgT0cQWuGJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
#فوری
؛متاسفانه‌خبررسید اکبرعبدی بازیگر سینما و تلویزیون دقایقی قبل در سن 66 سالگی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26434" target="_blank">📅 21:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26433">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9WvKJ7eKfUNTDgzxbYw-oJpLgogUZtYiljHMOFeOt-UikqO_FLAG_k1x8iktQ6P9oCZ1GCm-2fw5AO12CerIEA2tfjpqh5JVcHCUrWNb26U4OW6o72bauE74TH3s_j-T3ahp8Ls-0EPvsnXeF5j5H2s4adeIn2Ss7EQkw6wcSz2FRSgeXpLuji7OGk_H3Rg0VHjTa6j4Gt4lRKbvNlwWqOGesw3j-stNHRO3SYjx6PrQd4f3uY5Eb49rtHmmIRcyTGpvC88boiE1CaR0cf7W8l4Y3KLfl_W-NtZSZprttZ1SCk6QYFrYC2yQnziX9WztNPh1HlabJj8GONs6JERjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه سپاهان با احسان محروقی مهاجم 27 ساله و گلزن تیم فولاد خوزستان واردمذاکره‌شده تادرصورت توافق نهایی با این‌بازیکن‌قرارداد امضا کند. محروقی پیش تر مدنظر تارتار نیز بود که با موندن سرگیف در پرسپولیس قید جذب ستاره فولادی هارو زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26433" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26432">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvcZsXsKIReek7mND61CzdIfWUaDMc1ZhxqdG9rqkWED4zqd3pSp_9u6kfK7M5mzEOtGCG7DlgeIHf4xyngL_HiOl6wJibRBxU6fSBAOeycRDCyVbKaVUjV5LPvgleI3gPC-dliog92dJZZD_ultK7aL4gsd5ezWbWUQ8RriOzToH36g2zMv3PkF587L0La6LxHrxeIiW_zMroXNsQ8YZYI0p7Y24yCdgQ-i4dBJu0d4xxZ-VTJI6PtC2WIfKkjuU7GPFC2cREII1P5oQ4Bo7LNMnj56ivKYRIwwzefTmmupIQIabhHxdpMq4uzv7GNth_Wbo700ake76bOHo4yzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چلسی‌ که۳۸بازیکن‌تواسکواد خودش داره "بزرگ ترین اسکواد لیگ‌جزیره" و فقط میتونه ۲۵ بازیکنش روتو لیگ‌برتر ثبت کنه مکسنس لاکروا رو هم خرید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26432" target="_blank">📅 20:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26431">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGRg8ZPlGn0RWUvkUipv4T42whwvDsBUmThk8YqfpqSl3cFdKe__FE4q5QyzY_E0fndRaa248Kj3J86ZXE1D5d77F_OUL8FYHCwDhrEoD3t1-M2oSMAI8IWfE68jb10lgEh5wLgvfhQF9jb46tQ9HrjVXd5wtqdKIAyal1lPoFRW9VIyPBBvzcXkZI2F7lwaVLb5XZeETPxMo5Gl7F717XetHaGg3Rbwo6ijLh5sTw1e--SQ-BmQrIhmOf8yOHOGN8R9QG1bd83wPTitJ_ZmePVAY3mYM1ahgo1pb1JX-feF69PuKGBornNWUfeXdfJQG6brd5dtX5w8yKfKPPkW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهایی‌که از نگاه رسانه پرشیانا باشگاه پرسپولیس به زودی آن‌هارو رسمی و نهایی خواهد کرد: محمدرضااخباری، دانیال ایری، پوریا لطیفی فر، امیر جعفری، کسری طاهری، آلن هلیلوویچ کروات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26431" target="_blank">📅 19:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26430">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkkbZ10TQchNjRwkh5rFZ7JB5EnQfBO4e4-j6FMyHKZVbb5x5R44Hk-KUq-Lf_rHwtL8IF0JNhN2WLbOPjLqLerlUdUbClveLrcNHGf-VeuGVJC3HHxdFNPl6y0UpZ-9I9hV_Xu0TGGrO-EtQp3OsTVdnHTLEFNNqGXf7Q7caNzBnEPGIUBxeuXH_0JCvFAvBeY4JavJ0tv-ywUq48GcZ93VHxD69inE8bc-Tdm_kpTZtj9AMtuNs3CqvxLjRodWTmR_tFkieOzfjAaiJBP_hOtnyQOXNg62tsi1hY94pO4OIushsXnLoxZRSS5GQvtZaSXuVgjh_aO2e9A0OeypEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26430" target="_blank">📅 19:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26429">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T02vNDyLs9KxE4VV9OoMpocKpzPdsrVRtyP4-qKosB7N0uxK0vEC6Vl-riP_pdR-mwFSdFkXw7x6lU7y8fbEoKQv8Ka1_scZpI0PJEgo0aVvpnB1NEe-0WqWvPPgFvvFkmo8nIXGYkXFW0yd4tFHNY9WhaYGLMdIu1BVrzMO2JOACgm7S9mMZ2sI-lxUL4SFX2yvgamm73kfxtStFtAQ6oRGL8M6RbvRoUwLg4-LMcyXpZudSwFCgxnb3uko4YPB_ZHLZetUfMIhygiqZ6tUTED3yhPhcG1qqnksXvkEv91dSJZvKRSbbcddkdy-eFKNp8GhIR2zVeSF5HJ_WRAFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ادعای‌رسانه‌های‌ایتالیایی؛ آندره‌آ پیرلو اسطوره باشگاه آث میلان بزودی با عقد قراردادی تا پایان جام جهانی 2030 سکان هدایت‌تیم‌ملی‌ایتالیا رو بر عهده خواهد گرفت. استراماچونی هم دستیارش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26429" target="_blank">📅 19:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26428">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwnENYpGwg9hflTiibyGxIkjU-a2yH2yV4RqkZB9JlM_H_4TXFZIz80u4UoWsHmhHtskvScBEaV0HbOoVTaD4PwJPtLbtSpTVMXgWbRTdGa62jU4tvvBGvU1Ns9y7EPSkl0uDCCZK3UjQjlyJAKAWzQsepWa3zTjQkVqqM30n3pAJ8O0D5jSS0pLhBCoPwS4hcbSa1SajFZ2YI-pCZd5RNtHDI9HQnfPJ6yYmcFGNiQnBu6m0coehBdrP2wDf1wezmp0OdN8UGPI8GRVd0pcBG3yDwvJQdtn2mfCLNZw4vTheSZ4RduDRvGyEXO706bZPQDQiWlNxOdOzfVNZBzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
#تکمیلی؛ بااعلام‌ایجنت محمد محبی در ترانسفر مارکت؛ ستاره تیم‌ملی با اتمام قراردادش با روستوف روسیه رسمابازیکن‌آزاد شد. محمد محبی پیش‌از جام جهانی به باشگاه استقلال قول داده بود درصورتی که آفر اروپایی دریافت‌نکنه به استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26428" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26427">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cil8MWon2g5sMRKbP4WA8xKfj30JybaJkDOVp8RyQlZul4AYrrmkxIhmkg9aJVhHqf-Csfb__ZamdpMurD-Zge0Rq4bNa-Tmf32a6yetr0lfc8q9kMWzC-ZxBD_cDekhNewFFwyqxEyInhENLbOnEYNX4BEeGR1NWsWDhC8IUj3DpwXZDaCnT6GjCsmQ4KLpYYqBiTaA6RFCeGVfp_YIxafi4hel3_kvAJPKUe_8IpVe-hfyqTBo9RS90vWyd3IUqDGqSz744ASc7swfmLS4AGo5V10yEB9cB6ZA0IfGwPk-RJpz2Y2Xh9XBByXCkZeQkEJrxgkdsJxLcoaqkp5msA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی از کیت دوم تیم بارسلونا برای فصل جدید رقابت‌ ها؛ بارسایی‌ ها دوست داشتید؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26427" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26426">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4uabSLRN9Qtm7JWjxfh94YLwu51omrsVlgG5XKy_hKuJn0S20m6oQtB4QiX4rXBqPxwCG2YukfbECvZxjaOd8gwgJxkDJZRmI7OLPudRyWo-kSPg09jNYmkMcOAa_W-7CbLQ3Tok7jnYq1lNtKAgxWTiseI_cl4ojbAwT8j4RazT_VtMETTBuVoKXJJztW_rUfjs4csMJb2GI_oIAax2Ulq52Ah1gMJAJr_6Wxi91v55BzO2mIBCcIr2JFHpRmfcOr297IAbVPBc0gNhEn6KTd5H79YjEOT8dA8eVnz-IOMJj4mm3_39B3o7TvL3N3bMHpLln6R-HVolUg3mk1r1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خب سهراب یه نفس راحت کشید؛ با اعلام باشگاه منچستر سیتی قرارداد فیل فودن ستاره 26 ساله سیتیزن‌ها تا سال 2030 تمدید شد. الهلال اگه میخوادش باید 75M€ فقط هزینه بند فسخ کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26426" target="_blank">📅 18:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26425">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKlLbDzfrT4ym79WJ0Iz6NacKbsmIk61cSi7RE20R_f3NxYZoOm4xbEosXYT7MJrqRDG_B6gUVWEpouoQHfHvbJ4B-h25Pbg6b_t2Jn5BGlAQCY2Tx-PMfBZAbCYvg96BgCM2CZX8lv1oyQ3SlfrAcdxCs808qxkGA7I8TPmODdrkcEHVM4KpYRwgcLb8JE2Ug2kyOQMiIli4wdWOcoZcBRaOJsBl-qYfy4Qt5m5ZNbJckySB0Kk5eUIqvZgkqpHT0Pdbp10eVXF6LLFadb-MXPesXiBaYLcOouOtbcqtUod6rAqXMvqwlh3V6E4TtVxWFuaO5zeVhfSoB6eTcFv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
ارلینگ هالند و وزینیا دوفوق ستاره نروژ و کیپ ورد بیشترین تعداد فالور رو در جام جهانی گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26425" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=PL68ZeBURfkXi8CMIqXhYGFlIoo3RC1-bwtGmOnhujyAiYNMJl9sKiswwDqzX5Nfo9lV4kjBuUk5cNg1xrImyL2hClqg14gTBLkUEOuzLohX3aNToMuSX9SrzhOY2pohZL24X48DK72gBW_R6oNMjRRFJq2Cy3vqvai7bgDSbXo5FXASwmMs0byUu1h_W-7UEtxN3GksfmZ9DbeVnchUuH0PybG8vLGfamEskZo3s6crZqW10OTrzzStqV86jyUWd0xMEAlwBXcQ9wZL3zHuaDdZJWP5x7SFdvcuHIjVloiuIVLJIKYEEcESdWLB0XC0V3VJWR0JG9cE90PtzAyn6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5feffe70.mp4?token=PL68ZeBURfkXi8CMIqXhYGFlIoo3RC1-bwtGmOnhujyAiYNMJl9sKiswwDqzX5Nfo9lV4kjBuUk5cNg1xrImyL2hClqg14gTBLkUEOuzLohX3aNToMuSX9SrzhOY2pohZL24X48DK72gBW_R6oNMjRRFJq2Cy3vqvai7bgDSbXo5FXASwmMs0byUu1h_W-7UEtxN3GksfmZ9DbeVnchUuH0PybG8vLGfamEskZo3s6crZqW10OTrzzStqV86jyUWd0xMEAlwBXcQ9wZL3zHuaDdZJWP5x7SFdvcuHIjVloiuIVLJIKYEEcESdWLB0XC0V3VJWR0JG9cE90PtzAyn6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26424" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26423">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj_Mh3NNp6eJLYZKcMbcHqRW21rWW35lN_EStiiPN-Jye6XSZLTQu_Wh2mCdChWbqLkcRj-2FqcJkKKKAxL8DZonOu6-Vgs5qt79tidOqecrQ9bBrMvGpsoUPDXsNDXCO78o1T8OY-mUTR_Z6KoCnKqoB0tceEuWQLx06Bu8rzwRvfYD5sktJGPGgEs06GBM5a8iVh3LCa1E191wtMQ2cKVtWKip6q_1dL7TxGgbf-5tk8mvRylw1UgZce-nBCtktVsRB2-52SYoauaa3hrYf2NzGa5rm9h4sIzq-zE4C6YfFO5a2ERE-a89S7NZhTCdg4Ylbs2K2dIiQgP7WCG09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های‌برزیلی: وینیسیوس‌جونیور ستاره رئال مادرید از تغییراتی‌ که به‌درخواست دوس دخترش رو صورتش انجام‌شده راضیه و قراره بزودی کل ایرادات صورتش رو برطرف کنه و دماغش رو نیز عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26423" target="_blank">📅 18:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26421">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzKiR2YcBQsPuFC-Mhw0furV5RDg2ML_QaptpkNvBSqDOGUgEYwu6Dz_Gp-GgHHg940fp77MsPk-D-hUHEnJU2HpLwWilsc9uFme5JMyqOHrXkcCKIUIa8qMWQFm8Jied9t1Qu6SAYVB1CXWNbLx80XcQ6iTRhKGApfEMLjM8l2OjYm4kHPm4E8Fxoalscp8qkWTgQhLxhfUqX4iREUZW8Vxgts8YV9fxzeFlz8nL0Gsf6gbc7vGW1neX8lbs6qbiZd5txuzKtipG_SAODII2DHk72nmXdI2VPyNnIh1hwtAFVJJMKLKMtFF9nwyBHFWQ4GKtP-7U9XvSQ4Whpcd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26421" target="_blank">📅 18:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26420">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuBNWh_lu5n-ayzzxYjpEQq4OrBesDwMXZyL9Jx_vhO06Q2BvSs420kqofPHrJxeXZFbJfUy6QjivLWqJigJidkg8LkltWbg0V4z0__EWd3SXE6jGYUEfazB3fciD0HdgVDgmXr0TEYN6e5kvZzmrLjSQDy0vZoMTFjOz2ifR65Y2iFW5dBMqMnXLAXOhzZdaqR9iwK1dOSWdHXvB_aWLGBTZZ3pnQ-84QyKiBuysryVy8okWsRiXOekCxO7C6-P0vwwKEQlP5AdZ_KnzQ5KDed0yUz2Ov8CsTNRM-boMCmyNAYEexC9fTv6KP4D4n7-kLS7SU2-5rNLImzHPoidyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26420" target="_blank">📅 17:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26419">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qm3JThKKtomzItEU0bAcVDKQxoBaeXFYVfLj1SaNvHTb9L-lQ6Ixt2nP988xzjUkE7v_bdvNuOtpjeKrdVrcm7SOTk339fCqS18w_nBJC5zUe4RG7_HdtNB6epKcXZXmLyIm-1OVcu0T2hrFJ9wwCyY9XXhchDYM4Yt7UVukfoTgg3D4eDBOqxUtDgq5LMuWPLb3C-cQDwrxkM_9NZ2mCUGvtc2P63xHDkqEq_xJu6qaMTsAITWFCD3DS7qH-4PGe1lUGWf-6x5pbqjiKzB69EIguAIo8ZlqXCCaUB-ApCJx-HhKBjfpacsFo2vRTcWEQIk5a1R6JVcNxnEkA-Nlng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال‌پیشنهادی که به محمد محبی داده به‌این‌صورته: فصل اول 85 میلیارد تومان، فصل دوم 120 میلیارد تومان و فصل سوم 165 میلیارد تومان. این رقم‌ پایه بدون آپشنه. محبی به تاجرنیا گفته اگه راهی اروپا نشه صدرصد به‌این‌آفر پاسخ مثبت میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26419" target="_blank">📅 17:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26418">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdG4JunQopBjTEvhSV9v2-TXQiN6txQtS8k2wV6nYhHq_BJLKGelYZSxJFA5AcVi82WNgySeZZhlZvgcL0dJEeuxFEOrMq_eeja6LoXhV8CmhZ7Gex4YSQCjGnOp_PA161DQZ5GxQ1dAYwf4jjENiIgQMOAcrkIbeT_hpCn-P1eaxFFoH5K-XUs8iwuHjcllViwqIjTV7NvZt2E_D7e6n3jou-Y003vqCSWIqW0nczF0Fz4zRzjsd073E12iO0BVAoBSKYM3Ye0KXCIyv8REZ3KseaL87J5cEQ3rLJUjks672grgBtnc6dhToExtbUFqx9ONSkMq0ZYauj3w1dKxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26418" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26417">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqgUaF-8Jol2S9ulKw7q5sUt7-dmFi1Jyx2MhlMQwcVuI0C-tUvWuwB-r_NtL3TXTbf85QU8aMyhBBWSsIiqH1fV2YUqsKWtpYeAUymZHZaY0Lmszk_LRHWF6e4fC0BX2cjS25GsfOdaMzzW_2DCMRePITPpcoVc6BReKSwUcnufm9x7PPHkKYcsKSahdu9gjmWBrb04D3_CY6MwiPLZQNOEbAMwd0DEcY2t1mh8wyGpNSG55fIvPKtL_fizsCvdOtGVuycVlZzUNq90lDU_QiU5yWG_vT4kBfvc59smC6TXyuo2CCM-sPml9F4Qr0WCkwuszt7OVVXTz6GKOG6abQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوخبر مهم از تیم‌های ملی ایتالیا و آلمان؛ طبق انتظار پپ‌گواردیولا بافدراسیون‌ایتالیا به توافق مالی نرسید و رسما به پیشنهاد آتزوری پاسخ منفی داد. فدراسیون آلمان هم از یورگن کلوپ رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26417" target="_blank">📅 16:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26416">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOkfxKIEgDdu85uIrA4zlGbjjk891CsHhkI_ajsGpR-7GW1KPsdrNkMwiwqdTiEJXUuN67trdJcGRmvp9R6yZZxBegnoXzAou_bN0YwQ-a9N-2a5WmntXBLeSEr82ma69V6Hw6_OuH75is8Qtueo0FIQv4W8ab2oxUDgkfhquzeGo6alj6o4Kq1eN2UaqTiJQ9ieQZX2J5e2dg2C0lZOavg_N8VgiHZC1Hzr3XL45u0YY90hHrKKQUBDhwSjGZOXWc-hczdu5RPEz2AUPjm5AA65D1aihdFlmsv040rDzoupbcaI9I1_4XoaZGBXCwKQbryDFy2FoLF5mBDRTItzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26416" target="_blank">📅 16:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26415">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArbqgYudnPZaRQElx27cnuIxi_vElv3bZqZVT5CNTc-7QP5EFgnuUdaRBYUIdBwxkuUS4AoM13slSgMttK0tqmjr_tf60fL0DDfmNPeOjmti6yhUNkCVwZ1OvO5_hQ8YqzemuI1XdpCknxCC69mQ7eUfAU_Ni2T-nayqmi2YHUahhM0flGiHXUyrWj2XZRhJsTRqDeBSELJrWLslw5Fl24BCrTVPVGznUqjo3UsOAzbu1us611fm3ur45wZOOum3e4EDjRTat0Ymn5tXijp1T2sTKOWKk-zgyiTC_IQ4jaJ84A6R2I5R7Fkya1R5nqmqxpMEdFX3-7upg_1qtI_Sbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت امین حزباوی به مدیریت استقلال اعلام کرده رضایت نامه رو از سپاهان بگیرید من حزباوی رو به ساختمان باشگاه‌تون میاریم‌ سه ساله ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26415" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26414">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇪🇸
یه‌ویدیو دو دیقه‌ای از این فرفره ببینید؛
ستاره جدید و کشف‌شده‌از لاماسیا؛ همین‌چند سال دیگه از یامال هم‌خفن‌ترمیشه. ارزش دیدن داره حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26414" target="_blank">📅 15:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI-ZNZIJJ_4vXhx62GBR_1wUw0VdkhpIKbVG_cojmE1LLd0odEbspqcqNJVxwEC6A2cFWz0YVEdvJVh6WDvHyp5sPQqBMUOH2MSqU9o0v20hgkAvbGGc1tgkch_s0IaGcbKhln4dXLYCbOTEN2cF78pXBU5GYxCBloZrx59mOQdDfzLVPAjES-fMPKJX31WzdoeQn6ugPP54mN0YD-neFGIkIxelPQ8-BEjuKPGX76AvrDCgxgGmlUdLmGb49rCfgpFnjTVdf8IGEqFHIjZ7gddsiJLHbF40akZOWy3nh0oixx1ucIL3Yd7Cwd6YLl8rZGg8LVj5zmL4x9cOw9gmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26413" target="_blank">📅 15:30 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
