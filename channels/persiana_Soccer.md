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
<img src="https://cdn4.telesco.pe/file/Lsv8vrJmWs7dCo4aRLyxfGyVD5RW8iMEp4i_borQ2Ow2SZBPiVGjf1v7ohb_dH81uHeMt0nH5ED9BoHADVlz68eo6Zdn5-sTrmRgUZ5qwQSn8iN5Qo0rxCaVYWC2Ass1mlWo1wAV_on2AE9gpmdl0KhtnjZQZBQUeKOSSTfAk_cTenZLT-Lu7BwfLxYO_heU9D0s6xt_EGcVSTuZIdWJyxhpSuLZrMFB1_bSpQBf5sMeODEfQCoKW7OphKUkzuy4kyCL58NJAonai93wkfIp1RAayTmb-3re09CV3uprefRQHlI2ZP-yJONn1KZdkmJXSXM0NK6EXKWhuXBFJajCqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 11:58:49</div>
<hr>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM8fKmQVyit-M49HFdlYRRdpqnfvrcM43-GEf-LrC8T-f1B8514NYQN0eVOeZKgXOfZILMJn2HMV9feLaLjt3bKccuKkp3Ro6leBq-9j41aASuix8L8AdfL6esTcNLVPkOAQGQ-geDgoYupHEKSilxLVweZpGrNVInOzifBLnqSa88hLfb9f-YxifNup1-L2fT47WF-KRWKHGGSOjLx0M6CCDZXN7Z7icpJ5BJnaYaHQPDndZJ3dIEiQlQn9NWjN7YHNglrFKBIuGLMM8aWnhOoMtCY-TEZgBQ3rUDBUlf8MWTuNkFG57hBFMULkAT8kWR08mYDB1dhn8jQfaRr-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtK_YfCM9GsXk3BV42kPd-2YWk-TbUiz8GoQmjcs2jk7z3zVdA5XQK1szXPMWqkJinh9eZwDvx-BvWSfK0M-F1ZFgI6xV19c_CI11BEuYQN7dzUkQlN1EF7NRokr2uqZ0qiOZhH9I4WdMhXhWIHB2iOBDnMaCaiL0RrJQ7AjCK4tPZkgLiu98NFkiZhTF58eT5MR7hqvAFN1EfNvsQbuiSe4EATvx6nfHVEaS2XoleNlMrzHJznwEE51RGveu8kb-Hw8OFZmWWrpph70vjHSmdh4TW1k54ItYPIMqfPQvigEeA1nm7Gvv7-zDdgz1dXdlk3kTH4nAQd4dhjp8NtgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRMy5A_GqT_9cC8wQEWbp1UObmCC0Ige5bi0ndUJQFs3Hfy5C5vi3SNa2BdZK-F459oVuIKVhbGzrYuQYZh1YudhUMvsaaajE2hmAQJzepgiLnlHNbs6zzzlo89Q_gq6WfxtBb4OpjgliZlom2M-EaRvjS2jWUJcsEAsG3yC9gF2bTMu9AXcGApxpnhfzFtIvuNbREeR9MdlJXn_laz_4NG9dubIyyEtkLlOM2-l-gMi8qG3yTs0n58gmI4A2OFxBciewtOVYAuyqoanN_mgPwQCLXfPaBpn_m7tEL5U7iGpMDGiFC8JBqbdp48U5hsBCfrxG-IcmFqrvNXVI0bjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22811">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚠️
خیلیانمیدونن‌که‌اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس‌خوش‌آمدگویی‌تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/22811" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcmL1slTDAoSIQcOEA_BeN889ocNz4frm-twDHD0IlBc3Mkc52ozW3wsRFTLDuScPewjK_qAdfjRRrsymBTrjVAbGadXVzdRW7SxiIxlPxJnKadZE19jTxuUJQXKMnPawCcoAR4uu99t4qrlKlMhBXGZTA-GOKvB9bZYdJZLlgGv09m2PMHGH4kZX6B_9Bgud6tb9Pd37RW8AiazQU281tgTQOM6eBGEJPmABk4oFd6l4ucOudX1w0A_txC_us1721spEojV7-pXqu9rMiQChwyuftYFRON7fUJCXK3_l_PzASqeS2FUEDlx8cP8_0i14vR3AVjhSeGLzjAxSokaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcmpzYsLJUBYrcGvfACiXG6ZL6xGcKGdmYNA5PBjcb4pqRKfuKFNnBAmg_Y7CB8HLyGzJE3ULFO0gOIIBUF_6aFYIrofwHViuK2Wk_htCFmHs_DgyjoCMS1ZDvGPvcAauEaJk5uGSSFRH0wf-FBzw7b_Bt8Mg9ayg62SH_-0-YwdMelKEAyu9hpqyPOphYdtm_XNBN6C2LqSH2nHDS85XyRVixtFnqsJ2trIqF3FnBPQp0l9g3DMnrlKe47b9J5jb9ofn53WnGIw_xWQjU9R4uYtnKD52gVSUDtLKDxwTV1GN_TJDvcwXMUmheP8T0XLJYk4zhMf9hbDSk4h0Cq5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHw6CB8TEP17boMyUP2JuWXauXs8UaQtvRF6ktfTsQ9cQSB8s0QFqfhfifOqoiWkH-8gpup_VBjHRXGkMdzBlqy8MrHhXnS5m2Pfm0aInbeqgBEd50j6Q7LujDAwdf_0l8VngiOHiR3Qvl9KYz__p4CcpbokqHG0wpib-qpwMlOWD8NaUudpW90YaDir2x6Vk2bT865EYyB9MHmpU07qQbgdoOpgwB1PjmaNiyz9GnUfm56scI1thRUh4EyPpr7Ks2Tf3qjxorxhYXaAMdzWTyL9PejmpiyV1DFK4dGuoEF1iJBhlvFUvHPd-F0qTvhhtG4jVYFbxtM0POAjapVDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1n-XJRAuopI_ppvWLDhKXCjYXG228IvBK0gsv-KiT0Tz9AgKQRNqgEevCT0mEaD4GWMQQFwFE4uJXl-IxzPdrnoZzBmoo8aYgmicw22rf3UTq98aslbcUesXgOMzsY67oVK6SMMBBn25zI6ZpPrPUqSo1wtVhIaRHwXllb_nq3eMYKk2Ghv-631H_e36OvmMjETwBhw2tgalizmqgZYveFgdCxr5nwzwuMjOGfBYA3EGhSOLN0alFeNOBQieLh-wPUPlvveyOMr9wxloW6vM6XCNdpLECU3qy-zeM6YuWEUn89HZYkHpoAbO2-HE1_Awru3iAubdKd0isMFOVFS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMbFNnOY13US0MfjIzLB7zS-y7MHt8TYpTeRzA2HaGS00IG1Dn6bd4T3-rpH3oL3HA5xQk1OVK__0lyPFf8HtaD85Df1RrboB2vVd_dlrgOfN_y8zheNo5kXCMgmABz722B-YFGq5l0tgPtAG_CAgiZXhGvk3LDfReQpAOlU2TN_UIIPLRE7wAQMOpe0e6aTE_KsXI6y4xX0cgIZ2EjzsjkfZAGf1OuLlKP4hp2O7IqGOlk6YTtqpJb3acYueAI91JZr1NsU1HLpNqhB-WlHOypOjp7iIt8P3QHZkh3qTHoOPk5ClUZ23_XcdcykYPPVeG21afyrOgPkLel5KiiSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo6tGIHDxDZQiOXSYa615zf-EcBUpgOUXisVB6aTyGIRUZ12XDDyh00ddMmGYov6iNP9qAf9nRuAjNgJwzwHFSlE-tFfnq_yHfhQ-wJ3syn15H1ap8J2Ezb1laMuSOJCkmXQhiNYR3ST6hAG2zNDViyj2rj2e0X6her6ucN2jJBjt8lBCHPxbh4iwt1TjykoPGzqcgNqvJq7nH3kKqNUDTt9Mn6b5CVqvTVcL89gqvbR1_IYiyHwPb-B0ThkP23bgSnOjapSeD_2uI2MvpFO8QCQrYNjJ-5KZvz5cw8RQ_rbv3-Ry6-yfDt7BXlnCdNl22vDTF2g-_vnWwBaSRki8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTfYhERNlQo_48JnGMB38Ym4LHr9uIRfnv2_GgTXVUsNL5WXgpojte5LPg-TcbXcz8Yu6bnddbBdU3YWAI6Oid1w7i8p-XRZiLv6oOTxlPUEVZXHRoDfFOPDARkOhTxKN71kXcX4XtgsdE3OLtJyAQkV0OlRuKilnTjH3Pgfm8RCsUzhK2V_D_sJmefa07HA5ffR2jFOLj5E3mNqpIaIoCX00-hPwBGlxlN0aqPzeWh4vg1XdEAV6Rn0K7Fux3y7ChtV9wmO-iA6pK5YMLQ1cjYckjsJHPq5KbyJwpJ0XX5gjSL3IpsIYXs3rChlSCuFttHSCJCr6kOZ8j2-fEpU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgpAVBh-87OYR1chUbEVnFbpPZcRQFgEcE6CSWIaCIOUSPLRtefAUR-SvCVrt2wZ4_VtRSoyVQQJ1COeMi_DpfZloMeKEC0hWwMD3jUbEHnvIEO5Lmf3mmFWdvw1jnZeprgzPshO7eGGXsLDanrJey5Dl-hNs28GzSFyCQfJX-Ec6FXEmWZXoCtIHkaQYWWRGXNr12r0F0IhjBT73uMMLEGM1vepmk6jJg-JL4XaFzQOHo6vIZmVX4OSZnk-t87cIjseAvD4LiaGKhc9J8WrJdK3H5X5DphVXZhAbsgjarmsAAEcM6i_9D00u3ttWEtBF_EnL2-IKmSNSr2Wu5JSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGl8ew9Rk4J5Lx_WTE1-mu6oUbto7fYiyLkrhaVNmSLUeeVVNFG_b9z3R62PNw_DPlicmpW5srvAnxjP3rhEQE_EEV0RbBAp6Deo9P1mHzTpzGDoaMAuNWUFBcCWe5Oq8kqiuA2vJeYPkpZsFlkhgFa5dKBlXzQPY9Wra_ZdzbBfj5SJaVrNBtF_IEEUuCILUoz3TO393ASw8VngQ6LwjQBQVPvA6GXmexw4JJRTVJgFQpq-W3pQ8XT2WsvOaGwBEByjsAoYjvHiDmc5Bh-WrT04hXnYWGr_Rd5-Ii0g404e56awWO5SskJ6T-Uu11gQde4L1-QkvPuPVcvvlgY8MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=LuNLHSrlGAzNL2qQLjkN4e8UzpyP092VXYSKLXOD8a9npJe6hqL8tYE6oLE0lDD5BSuYnE9t1fP0fng3fQv7LUU8HTlv-nA4al0reHA9ZviCqoIsSnLb0FycRbAx8FrtAas3zN5UKG8G0UhxBO20sh9M7PZNb9V7J6mhz-32gBi_aHp1JF4vf1X_lSnbQPFG6_eZz9M9Kkyd_x8Jlstcbrf4lNKejtVJgR4YlmE5UAfkQkQvLFNN71Na-4p_ygpt-iVtLJnaTRR9a9p-H1hN4G36XbEdGMsD50lwRpKkFyctKiuisA39c2VJtisymok78eyLieqJSg8gW1C9itdEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=LuNLHSrlGAzNL2qQLjkN4e8UzpyP092VXYSKLXOD8a9npJe6hqL8tYE6oLE0lDD5BSuYnE9t1fP0fng3fQv7LUU8HTlv-nA4al0reHA9ZviCqoIsSnLb0FycRbAx8FrtAas3zN5UKG8G0UhxBO20sh9M7PZNb9V7J6mhz-32gBi_aHp1JF4vf1X_lSnbQPFG6_eZz9M9Kkyd_x8Jlstcbrf4lNKejtVJgR4YlmE5UAfkQkQvLFNN71Na-4p_ygpt-iVtLJnaTRR9a9p-H1hN4G36XbEdGMsD50lwRpKkFyctKiuisA39c2VJtisymok78eyLieqJSg8gW1C9itdEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHS4rvmJfRl7jof41BZFKruyPpaqsTLB3m_Y16fLRfMNjBSs5PoZmJXdu577RHyaJyU9LqR-jyWCuYeczOoSALF5zti3LFO4GlWAmXn-8PvJPR2SotJwd1XQrRr9NCku_gIf2OpfJ1j8jjf3okw50rJ2iTL5i2wHokVHKUUcTZMqt8Clw8DiX15zXz2j8J7HG-tMmwt_fwMIxpvuUpgRwNyjVRs97rxhHb0BKF4MWfEET3WyroUN3spqkGNIZU40GP7jxmKOfJSmR3h_bASkjb2CQSut_QHlfGxs_AWjXBIDb32KNsV3ZpeifUvSezzoD-GueUumsAMLTPEzvr_5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=G-FH7JjGQzz1z1I97Lfl1TEOdXN782WVrx8GbKWrVmkxF0X_3xk7zFdscrngU720qWydlUkT8gDkE5xdCjhMxqB-lwmxXfXN303TrRph8qxbP7EscJ67MlYODUgHw7L5WdhT6YQI5CRNaXiCiPv8diFNBr4ckjlYC3mEYce8ijGxRp3yAo4j9k1F5P1ZT9ufLSl6yrIHjpwP_e3LCNt8ElvwSQ9uJQFegWcjYq_iR_NCHDURTlI19apSxUPWFJe6cqsPHXRUtuYSfxTYrx65LeqLZq_q40nAu_XNr-LytOtBhwpmSwWP_SFTqB-QdyOuMCAGkuADAVGS7r2JRs875Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=G-FH7JjGQzz1z1I97Lfl1TEOdXN782WVrx8GbKWrVmkxF0X_3xk7zFdscrngU720qWydlUkT8gDkE5xdCjhMxqB-lwmxXfXN303TrRph8qxbP7EscJ67MlYODUgHw7L5WdhT6YQI5CRNaXiCiPv8diFNBr4ckjlYC3mEYce8ijGxRp3yAo4j9k1F5P1ZT9ufLSl6yrIHjpwP_e3LCNt8ElvwSQ9uJQFegWcjYq_iR_NCHDURTlI19apSxUPWFJe6cqsPHXRUtuYSfxTYrx65LeqLZq_q40nAu_XNr-LytOtBhwpmSwWP_SFTqB-QdyOuMCAGkuADAVGS7r2JRs875Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22797">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=HsKRXswtuaJC77B6MNYnDC8EDUNuQsX_7nw-7CGK1qkOwMN075XHqP7OTZVSXTN3xihpk7s4AipaeV8hLiK4uRV8i4ylpdfw7jKm1psAhEGPbyNxLZCMi7gmK1EAp7CA0dOVpHtIMQIQX-ixmHY5t648cJ7UKtkptKx8w9-D4VbFe1nz_TDUbJZMXwBWUlbr8-HeWgP9BjmZPYvOiwGlv2pt53TV4XfJg8cv6VbAEaW5A7ViChSfx2M9EersdxKyWoJrDmYmDB7BrNsXx7NlEh2JDemEeFk1I1ok3I_s36bs-fQUob13TYZuy5JwdkNNQWhaprJ__QrqTYddTOcYxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=HsKRXswtuaJC77B6MNYnDC8EDUNuQsX_7nw-7CGK1qkOwMN075XHqP7OTZVSXTN3xihpk7s4AipaeV8hLiK4uRV8i4ylpdfw7jKm1psAhEGPbyNxLZCMi7gmK1EAp7CA0dOVpHtIMQIQX-ixmHY5t648cJ7UKtkptKx8w9-D4VbFe1nz_TDUbJZMXwBWUlbr8-HeWgP9BjmZPYvOiwGlv2pt53TV4XfJg8cv6VbAEaW5A7ViChSfx2M9EersdxKyWoJrDmYmDB7BrNsXx7NlEh2JDemEeFk1I1ok3I_s36bs-fQUob13TYZuy5JwdkNNQWhaprJ__QrqTYddTOcYxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ‌توم‌دوس‌داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال‌کازینوشبانه‌راهی‌برای چند برابر کردن سرمایت
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e14
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22797" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqOKxXa9wVQV4jUaplZZcwONtW9a7Ur6MNCPFdrxdhyfpMYy7a6jQ-CT10f71aM1-5__OA-F5asQvS75EJHHTbLuIDjvVm3GC55zslo76iEueqZywbznTpsU2xEWbl1gHbkShPrcDzXAPzKeYdatq60Bc1UUPxiTc33yaqmNHXiOUUkKzFLIi_Y9IQ7riahW1ylpj8GXe031mmZkbxYZ4n-zaHXhj3JyAd-V1iR5on0dyPSszqzl534GAUFBvdsNfmSb-Z1UtDYddp-PEgZU6fiNWIv-HQuOIHFA0o2Q9Xz_YQBEUetJ48L2inUqOfFvQ3yXL82UAFDE_h7PMnq2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PosK5uF_ZQgheceuU1eNpupBbz-rN2axQMTgkCFPch0yNjCXTdwwfn38cRBXDER2cUp6VuY-gzBghl-F7IbesyCl-tHMa5WY5vELpAAXqy4j08RYoAWZ4Hq_5XK9nad_R0t7XZ4_s4YJu8pFDHvutuibOm06DLFfMDJPNsxzZvYZ6pOqVdT7Uv-kLfG5Tu1BQqyA6oKX2DivxxJDjx5sfbQ2NUqZFgJgNjdXNs6F1KYtNA-7PklcMKP5cRNcjhhfTLv_f7FjzG2TkGfeYGX_et5hKDd5dhb6DR5Iea-IiHNsyPU-_3SDKVqUfLcI_QFbY8oHMHCZTHd_-nygN0cswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRwKK7UQD571U1lMhehBKOQiGQtOaLMioaLHVRd2iC2IbwtdPShBIUQQfxMuqCF5hxwK2c9-9QjWcDBItzSj_0WK_yxxO-eLwAyvNDbF6ATRchsjSGluA63g4lfmX21B43323H69AELVH1_UJ6kOPPnQx3HJtOOaFvvqjfvJKD7aMJVJ4FjkX-i0UY2IGNadiJqEIY8Q3J_DC0CUZ4hB6dxXaQuU3EJhBfoox5xbaAXmarqbxMt_XmUJOHWfBIsB-Q0fUFPmTBdFynqbyquQ2UHU_2lRmwIzTP1H5HWe_-boGC2ApXl_RKB3uN7d2e92sy1eQP81WSxdSkbst9bo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAalfEhbCeZ6i9ow-fkBBew_WLd_f5iZuAzAOkbsXESrDqUua7QJaYIUfavLyCmT858iaL55ZXG7ceeG5jIhoCUDuqFAYGwA913isF0OY4PQMuoGmapX0niz8V81PsPOPY8sJIPn0883VZB7pwm87LdI4QukPDRDhP_sQRApA7IdP9aQVxL0BRABVQIbYqy3L1m8jUF9q5Xeh1uNr0hmJrdnzQpFRY7w1ukGW737G8OBJCFmu-9OorVhRVBZwDEnaU33-AULKjdnjn0Lky1YdAPOfCfX5Mr5KkPA-ot4o2gh3ano4yIlwXudMn93zsv5wBIn2fk-0rfZVPhWOo_94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hV_xgvh28yPofX3yn8KECmBMd0R7i5_FUEhBKual_6jzpIxBDBBRts5OQ_uOsGZz4KMse4YtNbUS7r7vhxS_nz1-m6zEsKzP36p3nxrLcj1aYppp4Kgevi6f1j-AvtRqR4i2QkCZ8OdkKXWKLK4fw71Ypy27L15_wmF8YJiX4Mh8anKpKm7uKCI_fMetXLapd3lkXZI2FVl7CK1x6nU5vhnqyszIknI2zk-u_5ibUsjg4wJrTag9LcvZlQVLmvaUwdAWU1YZKN2z37Q_yQHmlbn47CJsAPZFt__zdw1BPUT3GhFg0P1ZaZAqOIUQM_8hOvjj3hDj28UbWXSCJY9ofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psAJW9UY_zIOVe75PNnVDHD0dM8yBterz2emVX3awoO94GlrYW65dRpZ1C9NnS__FX6HYuZir52UZLGvsgtFvNiZtyS7-74aMfZoRUQmRi4JhC7El-wG7nNYM-FWjVN4c4s9J5ipC7bWQn-hiXEYpZjXpRVm-0ZdRhbV6Ekat0sGsW9UfAo8h4rf3QmLoc1wa31T7lcrbN8Fq1RoMt0mfSgOfg54-W6KFTkWZAIwKEswdeR-yqqWiGAaFxwZtGnTCE_-RMm8fI0Y8Aq9rI9GSu0Ta2z3pwONpfHCYp0lq3-qiEy4YA5DBm7twE6ShfOjuRvbKde4Ry0MY7yoxIw0cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcK6M_DLWexg4rakRLAiTqoNu1KKGuaKitGc-THj3lEkNAhgPv5Z6sveTNF_vOu9q5WQb6txuK5-1qlMy16pWCIFtFyaxk0Ep7X7x19qLpFyYQU-AmbW-FSbfimW7pEkJ9EQ42vPdZeegQCeLyDoonDIAsZoEDzgLPIYr7izJ645hYDHLEdq9J5z8TCt65Qtb_PzWcFbcIxadm1Cz2vkR1V3tZ8XEGyzty2Svh4qGx6UtY2PcnYfF-n16WLM7pWMJe1ZddOgw8SQtoC2NCzwjDk842G9-Kz6mRXcIUjmkaJj7VOktkJuaP-ALtXTHd5sSPYNlM-0JuuTzyov5EW103bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcK6M_DLWexg4rakRLAiTqoNu1KKGuaKitGc-THj3lEkNAhgPv5Z6sveTNF_vOu9q5WQb6txuK5-1qlMy16pWCIFtFyaxk0Ep7X7x19qLpFyYQU-AmbW-FSbfimW7pEkJ9EQ42vPdZeegQCeLyDoonDIAsZoEDzgLPIYr7izJ645hYDHLEdq9J5z8TCt65Qtb_PzWcFbcIxadm1Cz2vkR1V3tZ8XEGyzty2Svh4qGx6UtY2PcnYfF-n16WLM7pWMJe1ZddOgw8SQtoC2NCzwjDk842G9-Kz6mRXcIUjmkaJj7VOktkJuaP-ALtXTHd5sSPYNlM-0JuuTzyov5EW103bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=uUpkaqHsKnEz6ybvuMpuMK4DgUesJX2TMa6pRzxjYYsvpE72LwzL58_yxuKzTswZD96nziCoxeYPW8PvIDjm-MSQIki64rtzu7muVRBoTeU7Z_dSaa1MEjIddmRgX36yJ9TRH9dyWCTshF6v5nd-m65obrlwvxofrHtvI6IB0IqqrTlcPt7o6iUXjyrNlXmloTLu3uzI0Yy2TrVYOkR6REXN_AFYZUJPVH6EkvFB8fXne5aGE9rBjx7F-tIL47onVdStRG41vVw_urCEgiZBp9MCdYVCeSriNrtJcm1awlN5dsX2iI6FmxGq2ORoRN-rRa-U4WcEqX6lBUPZonVc_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=uUpkaqHsKnEz6ybvuMpuMK4DgUesJX2TMa6pRzxjYYsvpE72LwzL58_yxuKzTswZD96nziCoxeYPW8PvIDjm-MSQIki64rtzu7muVRBoTeU7Z_dSaa1MEjIddmRgX36yJ9TRH9dyWCTshF6v5nd-m65obrlwvxofrHtvI6IB0IqqrTlcPt7o6iUXjyrNlXmloTLu3uzI0Yy2TrVYOkR6REXN_AFYZUJPVH6EkvFB8fXne5aGE9rBjx7F-tIL47onVdStRG41vVw_urCEgiZBp9MCdYVCeSriNrtJcm1awlN5dsX2iI6FmxGq2ORoRN-rRa-U4WcEqX6lBUPZonVc_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twFbsX-Y5X7TwrYtV1qyNLJ3ve9cn7fBh_kRb7bvjy-AtUqrke_XG0y4SuelruO40CVzeVA80naXUO9HQWFUVB8vn5oPqQTpZA9j9XNfTDlE3p0Af7kxRgKX8iFlBqIzf9irqeYECYSh2VipctJZkUpASMoUg50gjdPDMwxOKpX19Hz22e0IhvUpLE3LfNKmexob2jaRoXPg81duAs_ypCgcPiYSfXRmrtVFlhHpSSQlaDll3JPrdqIETW_6T2OE5eCuJ9xsl1pZiNn4GS3GNtThoy70HxknQIhhIYy5iDQ2oYyfw94bQRWD36QMr2ROp6y6g7jNR2UQiEXvVWPGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdQRm3WVc4YdJ14I6t-KfvFfX0w_vYhUi2SDLGJHHd5He0pgq4obzhNcJQaPkbRaNc2Hn2v8o63KDdEduOkH4XRlOgrHcRm_-fRGe_5vlpJ9dg5XvS3dGknJk8aS2w_uhzZAS4slFIwVfkwZhnXvK47WDMIWH7LYBrb5EG_YeXQa6qwwhSWP0DSdF7W6lFHa4qYYGZKHSfDmPwnwlxUW-b3tIa9CXrV8ZiR5DbllB9Mk8Tt76QyS7no2jESbq6yuCHWlaYnGUuXyZrJCa5OVuWvUw3fDdRNYcsRwPrbbuualtS0SgDz06EB7ZWAgHNp23iaKCjflDi8Ou_XhGHGgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0agdOBIACggOh1nwVXtjoljW7TckiXApYzHLEZ_RFKHckYgklWt7upiHKmaGgyIRvK89C94B8OT9D1zxeTg2lhXKYsb-77c_B1QAUKaqZqESwe6xnGg5x4qTE5ZXqpJtvcfha1sD5NREwwEuk1WLPgqJ8PG4CCZLkFl-pBYh_gUaMOv7fe2I-xRheZJaJhaK3_W9Xtou9HCf5Lk5eF-GtBk5sR63Sg32VtsIRGCP6PaW9z_4f_MEcaSeCfsrUjYUwBzJflnrIIN2YXZCuWlx4w6hEITs7WyhC-wmwbTYs_n6JBUiZAAt3nePVrE3QVdNpBat_4eoHvWbibX6ooUZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZyIzlqugKbMCXbNZE4v8VAXPZHzAmhHMw1KCeD0CY1I1YZ8lxDoZXrpYfELSQt6r-ddhDZto8Dt3XAgF3XUjMNdKJPPFUm8-8vsDIBA_1aHg6i2j--It96P6TR9soHTe4kR8JFJ9qsNIT5S07SUcwxauxH1Qv7xk8-ndnp_iRMK-bGZNjspOorOCYkTKHRBGVXDUXY0syIjjZgeE9BCZRU20vHiQR-69VgF0qu19ZCMS5m2AD6t9pwccNKYPZnZnVnSmSDuRoLp6RGh8a6x5UV7B5CLU36z8WE0vhfCvHzy4epkrCmhk_Pq1JGF2owk0kbGgev5aDeMnEAZUJwkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5xIOES4Dl6x47GMbgJsXpJ-7tlnBXNjoaOambanPARKfYWd-5k6WmsoRSe6GN7Bp8KfR2PWbkuSxt9z99xa81hihujBliV1Bt0OTYUnDi59bWnlfN6INyNHy0ITrpJMsN87UryIKBVJGke70cKtKvg1u24ObsSMXNDNhYaTjiKhyamKUWTEOS6EBP9wkzH8z-2bPENOiXq585kb7ts2s1Kie8Y33h9Xr9GnfpNyUhrR_g-dmoaWP5ApmmjjBb_td5F1tGdxwCAekyJ3bxXkpg7L6g3GxuPdRceZuY7WNhvn-gjEyy1I2O02ERuhygwQavsn0X4Kk0fZWp9_-eKC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdQhK1aFOrI1_aZYpaiur8-hN3icgTP8G99c7SufynRcegIkmWRg8askP1Muhp8GAGnB8LTZIWbxiDpb26bnVsHzgpw_m5GIQnA9S5g_UamlUgaJtXU8pH0THTdMtgm4KhHW2PUSe-EG4oI4oEatB8fFlHek8bW7-PV_WOj7ipT-DQyW5CnncTaSxA-D6dmv3FXKzImlAAXCb_KS7PI9tDLI4lzB7zm4lbJhdK1WzSijBQwX6cCSp0F8jcVjGrKSUQQCpy1E3SFJFtD5dHyWPV4Vr1uPlA22cNjniVCrte8TS2_o-RUOxaEYbdDY47sHYLwz5gqevnO0fqU4_u_f-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPmbuE9xgkmQ9SmhDPYzctmTO86Tn-DGvWLlXm2qFuVroATyWk2MjTMOM9h0FVuMm5ASfrZm7VYRavso0MQrUo3Uq9mPlqA8tUnUltuss3KxEgD6p6hcc4P02mTEJBL0mhvWrTGGV8vy6HOMMRLZp8qN7GRjUnVDvb4q2KYbGaPLToYJnN9bqDRcJy7I9mheMF8tEkzHPK48NZdnl4mfyy1CNRDCreMgERDj5c1f8n_xyrozOaJqNbTxJbbCh8_yJdj-nlhbx-DO_o3xc2aVy3I8rlLWmWufqaF23QNFVS3QIUEUn8pN0QtKYNaurefy6EnXDOPZM9uXhw9OxLImkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXWta7Eb7QPokg6GKVPHy0jFojaaEViiDpG3mNZuRHa-nKmA35rFAjOaq4nUIpR141db5DHDEbrqi_gqet0jaPlPesWUHDNv31TdPESYSJ828a98-0Eb4P4OTn0NhrcqUYkssGfcaLjFSOs17UweE1YxAksTKkZ9rnBlBlSRdHBqRrWYpnvE39t4_z3HjqWuXwBO_slNFYCxobPwvvcL8rpARoWYPqtuX7i-V9I0FIDsVjfUdn8tNGntufK1QjlLRzd4OEJhCZ3by7KizDm0BJe3QRZz0DlU5TMJiaN6_NMT-scdVzZYBWGmJk_1vZxepHFdTMKrWb4RYJBuIsvEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrvMj5UeRheQaXP1yU03qA5Yy4_T8NY1H8Q046UuwFjG-wyaoIRKBLh9ZgSV5lWRc6WWzAQjAApS__FSEaE7fn1danME-IaQSgo0ssA_adY-9DPVUCYczVuloJHx63LNFKI9T4g1GiWUOI7cUBp0S6qy3bTHT_VY7eRONPaNF0vC4bpl8i77I83V8Zkrw37FhqNJ2qzjX5bsd-7zUEyIlTFauIfYOs7GHKMWAIbl1qsZGbl07haHP_JMapNku-p7lIl48cAUptj2x-a2efVWCHfxIsPEWX8qr073wmlubPawfZFAxAFxE150bTnEFavto6WWBM4omZp3Jo4Ia8AMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeSDG43X-1oEVeI5ajmgTnI64dWyaPALUGemWB7Hkl7SD-SAXh4uAIhAoMDTIjpk2_k9ZXaY8YE9vJ509oGZo_maAexXSnOMdmGwkuaXXh6xlRvqFl9rfoizb4MaUX089Kuq6pae58YHlVdjnFty_LqKIqgGsudb7jltgyGic0XnfpS1Pd-0uLf-YW2w1b_V1WEpkrAC8Vd0xSDsCIva5wUU2ScH8SrtszCt6LgoRfx_pb9oO1ii1WeF-kYuqVobLXYMrnrwkByXJnrZsqxbfNb4CVgB5SG3IWD6J4D6tfwk0bdtUnOYVSJVfw0B3ZQhMjZQA4UEc1K143X78WEhSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwGUspRx7xEsO2AjvO_frLWkiKG0m0tul-Au72gagZ0Md-uY1rcahjISIbhQ4i_8r9kR_CK6oBHAMr0SYd_vDMjNJYadOUF3wNgOiJ3uk3zH1ZtUGvA5ra8YfLbK67_pCGbrxXebPsl9Lh27gOYDfxtFPCdEdQmTT47Xl_Avwnp11PTJHkZXsbMuaLOPv-c3swkyNMotaL6i5HJz5WgEi8OeugaAZzwQiPHcgrsH4vzrxtoZMwHLnHlvUmfmxy7ZMo3Cee4YGpG8OjpfEP8WKt0lvES8fD8xilGdxv6jRCpZRrwY30Fh1Pj0GYUB37Z5_HM_pMwCw-bAAoENDmc3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQmt-KCO99QsYt_WmYdsrBwjF0-j-bD7h1X9xav2-dWOnVkTmIN-91HW0Jet9k5DH-4gV7tOKKFLCOUQjRqxKtIZA3t01hSmZehjl_nV8fIOlcGni8kQqFh2Gl4PJtEpnjon2WHlhj9wNqE-Nf7R4-ckYn6rTuhaJHWhDi8U5sQCmNqX_AfLbIEPS6OS4Pc47KX4timMLCxczETCZgo2zkqxacVgiS7vodBMHPbNlE1c5HS3u7F_RxOpp1TdUFAZF11LXYD9rsPS0BBa4BEf4RF-MEhXZ3SQcgOP19DtFq-K5xedweyQDm46L_Q3eHzCl8xKKJU9tKovM-EZ8xGXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brajad58XsQu_voyhH4E0enBj8jp34PbnLK_fB1qV6U5aHOeHZ5x9sL7tHVPxNk5JYdTn6aIF9JEAb6KBWruy2RErIyEQSrvMK9pYH28UqHjwh2ezo0Tg5qNlQ_p1uZgpVeK9r-tHKtZUS7Yff5fRq3O32mTsoqyLX7vT81G20A7X0EIvh02bboOgHcTVTqZKJKf9XWnth4ZLUd8HQlggUMwRlEcdeMA9mRe_ccVeXIAIay8Ryxb8obVHHxU5pUHxOPQU4nfxc-ue5cdewj-zioP9QWp1DrlRnrj_Lzj6RUSxij9-ChNRjB-mWNEgcsdsjq6xmilKBlJ3QuRSHs-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3QuBfFAldHVQbNf-cNoQEqhmeD1PyhX4cBMUgmqzF5vM4cUpgK4vQtr0XqsH5FBwefbEPWWM7dUpjkFb5fGZ3vOihQ-8RHKdvBmJJ6zoYTgtb-dwGgjeWNUhOMLwcG9BN1fSd5WHVzmMV7uxYGmEXNNX2xMxTZFu0RthBtt6QpgKr-0x-_L7sRFvDQMo2YwyCx3G1cnRwBXRmnhJ32pDx8ykFseFxgsO38at67VueOfLY8Er71ZJba_eq47EMg-6t-vxDQhxIIGZarPqo_OFVykMH7dvtAYU8aWygHFaXSsM9qfbqGapxAUwmZDxyHcsrzXzTX7fq2jTwgPDhn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCcO3RAWfbm7nd2K6_1nzAyJiT__4qQWedLxb3MUXkVoqP8RFnoRCip8kpXpxk62B12uQwm8p5qZO_FdTu-ARPnY88UeMgr7UW-IN6flcXoMHH85RYN84o4aYMroXBpqt8NgSPNsnHEYkrKOn71zDOhaZd4QwAH7Q7BlmK4MwGWm_Smmsi0z9BTkHuHTENFQuChbcIMVWcX5VncTat_QRl72isBjejxBr3vMRTpFA2zCQcUyLNpATNBf7NiJCwMMt_h8jqF3cO04N0Rhk7OjAYFeROft54mAzzoWVftyZ-KbxjBQlqBKTuQ0b6uGmttsCJGAv0GSTyyuKPnwRwfqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qshhBdHY3mFxrS-O2739Y_OhYUiuLZY3FRpCqklgSXIybw5xz8K_e7FhUZ0_i3ucA16bpyKcrjZg4oGLCDp_YIcAB4F57dtBV2PBsv2umuoyo6YYOZinQ-mjMMhENhKeDfmBh0fQNmXXTKlHvGEyEWRLfmDF1uHjCeczpacvStLfpccUQmRLfAxpZ_l_mf_QFMW_DPBh4BCGILLlxeLBw7AUNVLOPbqTor0PgGNRqdcbg3jrK4MZFSVmIzHYLFLZl4Cu4_3bTEcW-B07h7HnF5JmHw0_R2r_0wC1MEIgnku8LP3NHDAfeFVAvk3mep6Z8OSyLMhw6fUDr3bNNANkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epRZmMFn9KQ2sieyMijVfqDFDAgNFx3CiHSvsmVuyFmk07mTt9PaPDaSd6wIZXXgmHtBzzNG4uVdNSMiz8L2nklnGH-4dYVYGuc_H7YHW5bV5AcVxx51UTOvD-mpNiUFAZUbNuuNzWiDIaDcB7hXxdsTPqXMjfXrui_7Pkie4B0G2uadJgWtJfPf9QXaoFTWKaP6DK1rulzjYUmjO0E2DfR-2m1D4Tvs-DHKxb7_CiLCPrpvKracksd7flQcP0Q32mg7jEwUiGBu-3lQUivfFIrM-9-G43hr1mN-8PY0pP7mgsiin6f1gzSOP5OQ0LSSpd7Av9LbAv9J2PZHEUUG9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXftYPCPnHQ4mpTUemrYm-z81Vdl3h7qoHvrX2Y8Hv5HAxnz0qcelLb71Mgb80xdlQwugV_5UVUiQ4cGER2UnNIP75LwxxKMhF5YQn0wX2cK7LJ4gErVkMM3rk1JzOsrnqVB_7_J6MbSvHv1NSz6hW0oW_mfC4CvMRi5ur-trPrZefOE-SLlN-K1VHwUHNNAeEq1lN61szJ9PpVatwW3SRRDvKUbsvubgPLyo1B6efB6pB89M5sgaIyOv9vHXUVKZPECwDlKbyJlNOWMt7TGRy2dO2WDKRWwAAQAgth9iyKgW5JFPPQAboqm3yJyslfD8mqRDlrZ_8i-CIYrQxACuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOu8OMdz0qxfI2BzwErKVqeIkdOJrx8aHzWK5oYtHTjLtWZgDGjqtTaWhkX8Ww6-ZIcFhtou7XOONyRu2YYay4kOcn4DtqaoVUKBqsrvudNRsuLmZi6-S8jTQtk9np3EZfc6-dIYht8t1XUKtfIWGXTScnPQIU_3kj_crtjb2WPIJrw9g9Hp4mNxceoRb53zIAaFFdAzmB_8cr0W6bJ00ANyq_atSEnD9JEHnza6ubfR51YWiAlPR0sXc6S1eaIU4dtEY5wuPn0ti7EtEAEd6RAcCm9mUoMTTpVgS8kZo770-Ypp35ea55nH0yV1ueo-bMLHgF4LQFNfe1jB5pSurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paQefPXpLi_DJ_VShruhok2SiixZn5SB6c_A3hLVGzKUuo0FZ5vf_U7Wf2JxdK73PYqy-GzMLTvoa7N3PLPwmjyDPo_980OUvs6DCnK6LmkKUmjr6yrk9aR8b1cDWdvr1A44p8L8saxS0Yb1ajD_UGD-zKadiEGNGDX3wML6db7vU8iqBir1DTJ23tom5317IO1Ov2-j4znzyocNaiKf4_rL5akctJFhh-id8cJDZHFiYHC-GMzNxvlY3GcOM47JbYqxscGub34Vu6ePOh39B1LPnH-H9Pl7RyGr8_4yYoAowS1BUX_hS6So3nUJJPeQv4UV8yr8hurkf9ECgNZ46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq7LYMQocxOc70i3sJUxL9pADSFV6n3af3UHKqpjF_jlQhPrzC7GcXReuhPEGRGfgUqCW9uREaeYre3vlGWD9LNys_RFSW0hJpTXuSBhgU0_nYRHejmUKCKV9rGvHk3F7kr08w2-B2a9QcoAmApLLSDtQlOyvYZHlkMCIoAEPq_H8ib0_hN8wuDzk5TyP7YVQz0r4FQ2Jws_52lhmhRJ4E83DlokbkYgZh2xVXXwjlVmfK11JHzJOo0ILDPoNKOZhpePWJNLsLtk4ekPMJj4aufA4zf7p6qT2d9QWNepaI1EJh5jTliAeBRUCur6YrO6Hi-6Ppjr905cmSIaHaTh1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=SSRDPrSKMTJMNG9UKv8qKP86sNO7pr3Wi_OlGZtbDd5M0itvm0RT-SPP3X36eWxRqtoVdBF_82YO7LXLXTuxnbwKyxVuLrayy_pIQNsgTP87l8kLv1sH8AZHoxL-FUwHk1sz2SL3Z7xPCsBAv6zp5rDO6gzGa_PQBQClP3EVyIY9-lEkY3S__d3lnKZWlwc_UWeQNjTj2cdEeQYuRhP_51DhZGF5i1h9uOT1wumXKZC7xQmwJuXMvPmfyBL-0uRLbshMFEexRiWR1RzFzVP3GtOVhnPPNocGfGCOJo3dcDOD0Yrb6ciymFNEiGD7NM2tpBBXqIGkkzGgQZApoPyBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=SSRDPrSKMTJMNG9UKv8qKP86sNO7pr3Wi_OlGZtbDd5M0itvm0RT-SPP3X36eWxRqtoVdBF_82YO7LXLXTuxnbwKyxVuLrayy_pIQNsgTP87l8kLv1sH8AZHoxL-FUwHk1sz2SL3Z7xPCsBAv6zp5rDO6gzGa_PQBQClP3EVyIY9-lEkY3S__d3lnKZWlwc_UWeQNjTj2cdEeQYuRhP_51DhZGF5i1h9uOT1wumXKZC7xQmwJuXMvPmfyBL-0uRLbshMFEexRiWR1RzFzVP3GtOVhnPPNocGfGCOJo3dcDOD0Yrb6ciymFNEiGD7NM2tpBBXqIGkkzGgQZApoPyBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndiVQgSx2QvFzhSdcdhFsmnmA6qm4BQ_e45X-SHnGMDwag4LXOc0HUUevnqgoOkCfPkvHo3lLNXWvLujG27v2Bl8G0yoDk4qAGt2tmwDG8Yuu-n1tRz7pW89MdZvAFFmllTcTP2XpDfn42h1yTQT3bcFyBE61hEnp1V7KHEofo4M8javvaaM9jEsKM1-3w-3kXEUnzoicQs_NBHo9TtY_Ou8tg8LtFRsqsJZZl5rfyVp_XQ9x2YM7c3W6BnHwMSgCeUvjhEWpBNprfHTxtM0LWTCdgp_C804r47VOibIan2syDqF1QsgzuwafwgHEEYEXrP54DP6pb_JTCEro4MNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ju0oreMqoSWODf6Zqz2tRoIUfDl9BkKuI7U2S5i9Mm0LGYdfkKddgKLnULVeMsRLJ7YrvswY7ao8GFzCUSzbILwweMcKuAud9Xp0DUXHpskSk8PoPRRdStGP93ki-eoTJsdeIZjPV3_3nvh66vjHsDT68VskC76BY4o3rKBYnWe_fO565m2ioNz8kZOxZpMfOm0KwsJ3I23YTjN3cOsRnkFfctkWh_pWmxEaNWI52RcWeAx9Rh5e2KW-ZiRHdxkw_sEZoIG6PiTNzpzeITZ1Li02LdI8YYmQZV_HynWUk6o81iSquSBN0uHgqq2QceEaGj8PDfvdq9iJFMxiPxIqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNItFvHPdE6JSCvqL_P06kCpIlCRluIjKDGIX9guaP0_wTztSljJpvFEJ2Zud4Luh_-IDY2QrFB-EL84jHPbm0A4Ug_JvC2llIlqekbknGQmfakViYWq8-Uc84B6Z2h7dwGgzx8yOzXMJttjvcErqNwVTnADukrbaGYWAxyqb_SS3mR2acnMxn-y2vVivnTpaPMDVtgF3FBPAwhtIKdk71MMryxu4hizWAhVqOze4DeG0XL1lk9aZESdhWqFyOMfq-hyDngvZFLkMH8to-PN6Ewwg58xFh88SHqVPgBvyTGGod5xRFypJsKVZEqXkLsE5u46I01CQ9OzfpyhgRwnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=JJAviu3upgsWCkL646UCiUaKDcg5PYBgFClcwpxi6cpVdMGGXt0-IVD4f3YW3oW8gwJGKt7AJTQLHM7OAgonF8Gi0brYK4F8-DYXrn_tYP5t36wQb2b4FOAjbpsJ37W2YMT3drRT4jNQ325dLlcWJLOU8a5VobsO-5BLvjz_O2xeA8ZI5qzK1hxmgd5fPNaK0ZX8SAC4p_pGjlIMOludY_htIhs-97Bxs_5sQ-aXhZahlyyVcp4eionicaSPm-q7awABLTgmNFXumtKER260GFrtN_Q6zNTB3qFU8y7aw8AGF5wS-5Jn3NM60Znll6P4zP4ztEzylek4T7pYzHbZvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=JJAviu3upgsWCkL646UCiUaKDcg5PYBgFClcwpxi6cpVdMGGXt0-IVD4f3YW3oW8gwJGKt7AJTQLHM7OAgonF8Gi0brYK4F8-DYXrn_tYP5t36wQb2b4FOAjbpsJ37W2YMT3drRT4jNQ325dLlcWJLOU8a5VobsO-5BLvjz_O2xeA8ZI5qzK1hxmgd5fPNaK0ZX8SAC4p_pGjlIMOludY_htIhs-97Bxs_5sQ-aXhZahlyyVcp4eionicaSPm-q7awABLTgmNFXumtKER260GFrtN_Q6zNTB3qFU8y7aw8AGF5wS-5Jn3NM60Znll6P4zP4ztEzylek4T7pYzHbZvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl97d0YQ_PIPfn_fyEmHkYhAPKtCYx0vWrAEiqEx2Y6Yrp50_xV5oXJDSHd-qx2CJn7TMkotM8SKbHfzXbCU37NkZOK-i7kzn7vVszffc_MWtSIkHg-TKyQ9tMBfQDNQ8tLHd_80zXuZRg8o0fzDLuy6bDrPmmuJ4DOOakr6iOILXX2wSHgM3o_udpEaHBb8O--_imgNFp8u0Hk8ViWe0AzcgN__-kgjyyDeyEsgxwNI_RPcgFYpfd4zoUleNdTJaF5hXlGICKukT-84Y2ozB0csWKXFIHAkvAmfIG0Zg_5_l16HBXUeMY1TX3ex1ZyK4F3TvX1Lst8xQgMj4n_ZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fukq5-n2X4BbKz2EJ_Lgr0dK0UKWdzlXGnpOVfYXNctpC9DqBnwT43nEiPnTaOMLuc4vNjvfLztF3LAQ7p1SETfzNaQ8Eh2TjEU8Ar51y9sq9u_AFy9mmI2m9nk2nhZjkY32wBec8gweE7gyeUCCFdhvHNgdFZco4-h6FQYJsUZYAXzIj1vR8jphtD2idHzkNr8RugRwE5sim8qy7gaPhL3gzxmz6K1K1Js7l9zSEAW_FM3NsKZq8NxqX2WD1r0uk7RZnuHjW8cCcSPbOWzBJoK5bem9Ow-q4rSKI13FGyzxPAMpzyKHdETpTfzscpRxC2LsxPhV6NdH5aGa3FZ_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXMTB9J9MYuCGNHmSHefL56kf190g6CM_xFuX4rWDL_2EntlL5bvKvhscshetgxlTwkYEv3YBko7LmPrFk-jXgGu91hJmVIppXBigu-eQWYIrnWUU3eqtvA95xUuHabaXyNVEPL3IvvMEiICidLLS_-O5wuo4tMeQvVecZsy6rqeAA3KIA1HiypcDamEZf0pDAvVa0hg00fGoNqjftBrv4BXjoD6cOLjGgtGN_7IOcco279RdKRqBTMsK5smz9nTHFUWICbADgMil-pH1B6VSadK8eVfw_SYuFIj6l6az-VS7aBwrXtc2ArrvVAdYs13NKbQuUT1k37wgsF2dqBXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7eBRx-XDRjENFLa3uLtzY_Q16QvGOeHFolKooYbZzTntSOvKFLOuXheIjMezjlEk88CPyQR60mqreW6-uY3r7sabMeGrnU3D3peRWVbSTJFmxVyJ14LSvRSqURlKehfjZeBLE4vnEBerSESq3QZlIpipVThEXSnthIzVKxjS6_xTrAoMOhZJ-F7_68JjdyYaDxw_nrUkE2y-gz9ZxQy4wYlU9qh-6XXc3sggJNUdykiGaEMaVk9WaeV0T2hwZ-aVUz6BogkwtvHJ0qRHm9-flrlCijHUCdd9UsxX4e1B0MdtVvmU7qRXhvcUY_b5WwTvx-o-bBd7i9Isryn7tjf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEunpowaXmFZhOO_g7V8iN1hYFeaaD42GpUolSSKST32WMwmTjHP_CnyqjFk9_Ate88HbmX2b0mUcnsfrgFGeAKswyRw05hQQHaZq2pNICBzzLrHqGsdL5_mZngqZEPvq6ynSG0oeQOkq6MmntzTA1p491PoiS3kuB4xUE_MeiyTKWAyUhfbEfnkOAMSShEap--I5jTZZQgDqlut66CvCCCgSfRxlFZz94qa0sBon53rHkPtBZYbGa54TVWagpdt-nuJZqwLLOu_iC7kCavl4XFG7yGpYSBw13KEOF8ny2kkpy6ubADHllj9duJM4TP3UOIhTCWbyhQcBZwoxrUUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkUFCAJ8OFkReQz2ekZUmx13_cHrblricH7gskIq2yZ0wqMRGRhFIoPgmxwQt4IEPaTzvzbEByC28zkRl1gLMEdAGxF8fzUNIkfjnKnKVDbBsh17BWxyGAse98XZhNGoQpH_Er-mJEFJU0b1ykTOW_nwEbkvEiU3Mn4zrRjz6DhYoiY4H4GMG6ew8pdRjNUnwVYYwC1RTCqkYvgKs5xrUeXgI6zCN1ZEukKy3WUcSB9tRkDdq_TW-iTRntDBYtmS5MOsM0ButYVuVu8FvbtZWWZIbHNIYL9YyoaxZ5KXFWbprEErsoubesjBo98KIFx4HO-udfXaT2kNxHx9c7_k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWmin5H0ARKGSMKzWnw2HrV384tZYy87aQzXxt-iKVuvhTyfudCKhg7KS3VxsVL_-rTBbmXf2V8U2wXezqebiXzckIW0hXUFCJ4KOqkL79TRrIaWVVROQiGv_t6XFkYUYJ0DVA566duV2UMfghGCgUbto7OV-naSS_hNJWtkgeNKMlz1DBkZN67kYbL-nm3-IyRGEH070i1-ozftFBsmja-hWzZ0xOi8KzqWg7elDtxFxlIIOYbDcwLz8PLjRvFAjcIjiqOi-ARn0ASsRfBoqm4OSqr8IG_hYsVa__j-iUtmx-6yZw1HIggPXKbbwhk57gXM6cNOy39rjiWs6D6oQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=UbpbMiWgP1LRlHR0td8UCkv7NRmh-OS7I8FYxNdctq2--1bbegIKtbWxjneMTx1uaD9N77gsEpofQJRlGzaVT_4UmzwYzPnN27DgbcJ3tdVGrBuYtvzFFfEME4QRlO8DAWK9OFvc5YjDNeEmnts12hDmjTJyXEL6-0O_xgsrsUEw_WVPpmxdfYwbKFtrEIAUbBQNqcRw8j0zWaJjF4f9C0XEOQUoYMDPEg2sN-9IH6yjfiWpWBP4M93EHHSwEUzCVR0jLUnGf_hr1Q3kcYSdWSryYpeBA4awPpNg44UM2WWtxqPtkEAFgyCIWhw-J1Fe90hgrP1yY79xFywe3mzNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=UbpbMiWgP1LRlHR0td8UCkv7NRmh-OS7I8FYxNdctq2--1bbegIKtbWxjneMTx1uaD9N77gsEpofQJRlGzaVT_4UmzwYzPnN27DgbcJ3tdVGrBuYtvzFFfEME4QRlO8DAWK9OFvc5YjDNeEmnts12hDmjTJyXEL6-0O_xgsrsUEw_WVPpmxdfYwbKFtrEIAUbBQNqcRw8j0zWaJjF4f9C0XEOQUoYMDPEg2sN-9IH6yjfiWpWBP4M93EHHSwEUzCVR0jLUnGf_hr1Q3kcYSdWSryYpeBA4awPpNg44UM2WWtxqPtkEAFgyCIWhw-J1Fe90hgrP1yY79xFywe3mzNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHhY-yV7QGMla9LABYIaT4EcymmfK_wfqxZKOC-ItvIm4IinL3oMHLTV0rn8AM4zz2ESDY6-mnBEcfZTH4EiL5X0nXP75jp2pddAYImerdpEjS0RsVTurYRjNy9--3WLJmh-PSI0Kzml-9Uq1GTD35p86-C0t2fQWS0u7ttZcYbg9P_-5xfuQkVzS-Z3PgvoMKiFXSXiq1FZm239TvsZ-DYm0E-f4Eur4XL54nLzM2CzEeQqxiqPok4dPVi9kGPp-lcaFFRm_S28-yJqJswhIw0jkHLmVWiISrkddEoPW6QAYpWh9iROEPDCObPdymCMZ7ArgtDzRL9yEM1jdjmjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvjk1VBkCM0ZpT2E2zBvvx0t46UMWExCbMI-Jtr3YhL5mI9h5UoQgutWfAqusglRIiehBbIKLgqztampw2ZeKB6wMllftvOnTxDxEAmfyNDg_wOpCr18ZpFnOUa1cYdC8j4Gfjuz_z76LAJs8rzdgdfvASpCyqiCWIfxWrBXPnQ_omj3AsOpSlxftRXFapMz9e3b7mh6e936xfXZITg8zax4XD1YIZ8LQRE4tqIm6lyNI8gVxToZAz1Es_EuNlkDuMVEaceNoblYBB1bajFiZ3Rp9HY5_NoL1xKS6kNZvJTsAeTcgBG58IdTbZiQCLZkoZ6_QKXM9110G5pLyRCroQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVmkeAfssHyy7iwyf6PZP1YJIHlqyU73DUV83YyhGqecHPEZMoy4uKqCNyz9bDIAfnkNdMgnwOUZT4XiAeFKdSJT6iKiarUl_uIrbHOjdUV3Fc62hOphJ9texGSA2SP-okDiosHtmL_jzzl8i3NVYP7xcZrgjmH0SM0P-LObywEv8TywEHE7q21gFIcVs4xsiyUeQ2EipqIjBWCRQxvwzeHNyTwl7l8AUDy--k-OD2ZeUIW1mFy9WkfSD65NJTJwiFt4TLpLTJ7eqq9ar8cmiOENVP8rCiLhjjNG4BjN6UMHg0Ldx8tDefhz1N07qG1RQ1O7xUF6nQUwZCFyKkROkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZITzPDCmDFN1tZbqaklLGLX_mdEF7lCwkV1TI1ceA-wHuPlBd1tGZEks0pMZ2LeXTWFnVYMhxHutHhTIO3dvXxcTs-jZQgjzjmdqLOcrS11TTL2J-JxcLI4gv3wLujO8URkCzIs-pGmOidsWYp9yjPpRCH1uQC_Cx74i_nMyq3q2ip_bTkUF9zTsMDIN2yE9VJjatl6BTQ-1NDgJ0XgbScdUu2scewSABj_QWTFAb-ZHhkYxxl1BJ0OCw9VtUdXio9OypbksNfSizd58OO4Mb2tlVmB7XjnRpJomJ9dQUfmBn4s2OKsfiNuMnU80YZGZbdntxp4TvCFl6Quq1wFc2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqh8aOIZyOh-w_t1zdEWkwy9A3fl1a6TYg_uQYyMiOYBBg3CqVYgXbYqNDVgW8uaL3WZst5QtlcNs1GuI-azKXnMdjQ5VFnvU-hIuOppQvjyWkGCqQkta8y4-0gqKRFlg9AgsWZvqK33DxxkdyMx_PNIXjKld83fRaaQ07GRIndksq-C1ZTjkOwDLBJjpzIIK2O6NqfRCFFsrfWqBvz8BCXb8slVvZrA-on2m9nFAC1zIAZMEZOv4NGo38WNYGVqDebHP7ueBvrNHXijrdUM55yeUgn8_jPjkipaSpGu5-f765JPkTNI-pk8vXaFUyiQ-nFjq2dMQoBPLKOla1_RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBm01HkIaoQC04MPq4fRX-5EYBYH78wbXYkSppOOUniWQmgUZOi3gm5LTlQJB6h9oPXboeItgmYlg_zy6BgsLRG1vb8dTUA6ht9UQST63QJgHGtX2agkZdfvuzznizUEadMvFzU3xnaoRFerRacYKmECPo9vKIgnkRwK5X2j6s6Gxv42JgDozEsqkkTH8SSNHJubyh7g-KCq1JOvptyw-5Hhmg21dr7M9R4xcuZRUXXLKE1KStyY7NqrTFlhs2Q7sBvK0aL_MlujzNWrSJWbI4IlrBfY0epVu3L8q5x8G0AV-I-I5ghyre3216TEgVhUrJDmJyl_9xAo6IlpkGKNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=i4YAfVDcUtcthiTB_11vYGGOK-RLs5ByONWtCOl16HuoejBqNT3Qqruabc2hQoioKwhW9xYH2lZVuKqHlod7HCXKXAPyUaNT9S9pJeNlJy7trbTu3TGtO9GpHcQmtvXcfrXNghUPM20N_ylnyqzpktNzKbLYgGEXo92Yq4BUQ8ChcPCOiGzDXsb6Zx8aWr1MkW-UV4IJ9oVp3vEKN388f6yPLlZjXgxhqTXiDWjsOGmIC59zYb1MAQwPuTxaadjeljpNFv6nILBjjPwGMWTZe53YWko03KQSVpyR4Ij4Z8DPBahsHfg4UBd76xkzhl5H2DXJ78SEsuEtLtRbhlCwAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=i4YAfVDcUtcthiTB_11vYGGOK-RLs5ByONWtCOl16HuoejBqNT3Qqruabc2hQoioKwhW9xYH2lZVuKqHlod7HCXKXAPyUaNT9S9pJeNlJy7trbTu3TGtO9GpHcQmtvXcfrXNghUPM20N_ylnyqzpktNzKbLYgGEXo92Yq4BUQ8ChcPCOiGzDXsb6Zx8aWr1MkW-UV4IJ9oVp3vEKN388f6yPLlZjXgxhqTXiDWjsOGmIC59zYb1MAQwPuTxaadjeljpNFv6nILBjjPwGMWTZe53YWko03KQSVpyR4Ij4Z8DPBahsHfg4UBd76xkzhl5H2DXJ78SEsuEtLtRbhlCwAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=PSqOPmRKZswtaCiuq5RhcWcnUcOVJeHjCZlXTIYxQG40fQxM8GglCm51rSf8kgEHtvlJUZIsl2VLpm838APr8a-j2HBj9aqowZODbVd3mIJQcMsv8nTCGkNLllta3nAn5OtbLZ33nOAtbLJkYWA0aJQmyd6WBWYPpQ7A53pLeaMw9UMJVgvS5jinv5V99kVfJOODgoBNWOsvC34DjPFYoSmi_j_GhxN4k1u7ChUa1cOoBckkGydSZMw_Jyz5kdEKjBbQo4MP09DskNb5Ut0K9ApGxg1kLeNOEbvcguZcWhOz7fjPtJaKSQ10emJh8DtCT_IlU4rH2QIZlv1xR5PKT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=PSqOPmRKZswtaCiuq5RhcWcnUcOVJeHjCZlXTIYxQG40fQxM8GglCm51rSf8kgEHtvlJUZIsl2VLpm838APr8a-j2HBj9aqowZODbVd3mIJQcMsv8nTCGkNLllta3nAn5OtbLZ33nOAtbLJkYWA0aJQmyd6WBWYPpQ7A53pLeaMw9UMJVgvS5jinv5V99kVfJOODgoBNWOsvC34DjPFYoSmi_j_GhxN4k1u7ChUa1cOoBckkGydSZMw_Jyz5kdEKjBbQo4MP09DskNb5Ut0K9ApGxg1kLeNOEbvcguZcWhOz7fjPtJaKSQ10emJh8DtCT_IlU4rH2QIZlv1xR5PKT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA0dgg-r2lyKd525AX6QWpRDvhPDpfP_8WOwyKwsS2cOm98qyNTEij--yvm9WatFI9vXLSBACoiKBb_pSpxG8E--lpJsDJw3QMuczNK7ORXpB-U0mwqZgaR_avoB-ddwKYDEclcYOl2-xqlWd78mlb9z7XkNakq-nHryiv0JqkkWJGUH2pk3IfVc-cu7graBFSucMlCcaKL048cKyqQgUI68bBIITyEw6Vj5tbg_0poztI2OF9uWZ9UJn-UZYeI_91_-SiBbSXnitS8vBzk58m8Ae-fwVWuNZNAuKMZ2tuHre39MJVOJvJAtMisoO0ZQUBMpCdkeQbYrze70sdPVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfHY3LBNP--KOE4LVe6SLZ1nCqaOPuhmxlFYYUjZfGyTMilAe0XF6WCdbapbkCpF0ar2-VIMgBBdIEeBR2dkIcRnqjsod5gAg1rnqWGeMEaZ80b0LU6r0NTQDbO8CzIysZSQhw5Ve-QWFsG-usydGaXEZsFJur5aTzU3bQcvqSnkgIs-37gpwPIUvZdaGbTlYEnEigo-3SdhOEexR7kaCb22beajn0LIDBm7LXBiQmBIWDQNEc03MqUh2iKHc_QUDFXGwDmWNAmGwtufPzdZU3-wS0_-ttDN-aTbhx7SO7x10J7ZCcY5HjP1PuRf7fC791EDQ4xT0lGEY0HRij_tyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5OnAjsJRwtwWvIQMyj2CZJRfkHglDBRFDx-kbZUE8SRG7yQUl5ZdltAK39P03sK5O15Ro72nHvOhY155Hoql38acUS5DgGecTif34akJ_d5fQMJAKZBrXhdiAEt7njusJ0LT4c2TZ_SmnUi7-eDli4JNuXpro_qBhaI17mBiyQsNR59ZohrdgZOek4UHecD2yqI3audEc0hWBm4318dfSw2Pm6IYAKHm0AuWYwS2qMpSHjajjYD3_gAtzd8WpZGMKIY59sGBjOrfG-rLCnQoxRvPbF_ee7-qW6P1JBUjxwDjbYm3Ll-Kx1cuYOp-RMAJVnNjJ8T3NqvQRbDe6ojag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=M1tz6J6ZdvSETuiZuTub4nS65qk55jIx0Ibn3XZoTLPBSufa16srn1s4d0ZBaly46sqEE0aNdB5Rr6rr06MQ_FIwuV9m5t3ymq1XdKMVHloVCcCJS0MmrtgQ_8lNQThZdgpzvLrQM443-PpA7f05CjM6JFnMC17gmBKMyulBU-KbKOKd-sB6lLl0msrtd3zanDssJU6nUn_PCDzkg_7bxbL_OSS1-RYGTd4I5d2bFwY268G93Wjmpq7af1GfiJAOwrLxFeW-36K6Ae7NjKo058Hdoks0o3LdjyhavALah_V-cZmdb9_GmaBabCPX2nhnWRqGnCmmWBfU-Bb26RReow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=M1tz6J6ZdvSETuiZuTub4nS65qk55jIx0Ibn3XZoTLPBSufa16srn1s4d0ZBaly46sqEE0aNdB5Rr6rr06MQ_FIwuV9m5t3ymq1XdKMVHloVCcCJS0MmrtgQ_8lNQThZdgpzvLrQM443-PpA7f05CjM6JFnMC17gmBKMyulBU-KbKOKd-sB6lLl0msrtd3zanDssJU6nUn_PCDzkg_7bxbL_OSS1-RYGTd4I5d2bFwY268G93Wjmpq7af1GfiJAOwrLxFeW-36K6Ae7NjKo058Hdoks0o3LdjyhavALah_V-cZmdb9_GmaBabCPX2nhnWRqGnCmmWBfU-Bb26RReow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqAVLWZ0welenCONgR1FIb8nsAvs7bfdrj3G9DnFi20L5Ye3xrpav_8eJX7VCt4vFNO-ICMyL-nyCJpiy9lX7M14p2_TznArvgardoIb7uVbnJU-BvRdGKR_nuC0d2W7VIrcZlCJYckLGFR6Wq-yWeKNIYRvQNm786Bzp66IXiMgptI5YMxyTZ2UlPBfHpJQtq-bTCP4_VCMPIGhUHf-86OdJvMitmNE77FOKcck4vbI-zPTV6DgnwtCkwN3PoeChLqxjp3OBfAsuQm1IaUjXSCZqsglwJhntjtc9B5w3URrCAdw4-B0RaX1W2MGLUtQ6yIKwpDMmuSAaxAFcwikDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daNXI9hwrgFVaMsl_l2sKVrjMy0BfVCqxtvNas19C7-H0_oiNWrNFoYunMCAuoNa3z-J6H3Mh_uOtKAnlKnF7-j1TBlisAxP360vHsmYHYT5Whns90kogXqd9-NEerNV1A5m6xyX8FcjmIBeCY6zYKUFjBLmfGir7l4M9CPVKLVhhmC_UZ3kwLWN1T1-0C34hXRASMmD6BaYjoTdCtMtqczhlcDto3_Zxa69cnREN-OrbrKkAfsEOzuHbnoiTSkXSmupuJwXBurLEF0Bc0-GnFsbYCzn4b5SrUVba186vDmnUYuYdsdA1Rtz6-C9oqmIDcex3RjBWTYQXoEJmcslrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJiJgp1J04daz5wsIe7H1h-_fDW0BH7gxYq9eZBs1A0ebUIYLfOaaG_VIJosk4ow4-l5Uh9R1VLn9QTfrU_lpJRdFyjbDANPw7PVQq-7317rsiGC0mWdgw4lHizUP1MbQUrylZkVScylRuqb4al-A3IrbgWkCqUSdXKV3S-hvqFj1YeshbUaNqBNdxfnl5UraLiNkY0atecDaTsl47N73ON04B-5JR5o6Sj2wHlrCbpRB7fxuYn5XrYGmH48QhPCh2CcTBL97OxtcEP16P_tX21RUwBu1jq0lawfjmXINtzoOR-zbtUfHnis2G867y3sT7mDn-CZwSXgAoaA92JWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTpzS4DbJS_m0GO9fN6ZRU0UJ-DC-Z0bznQcW45YQgVAsq5Ap8mWU73l0tOzczZWOxrY-AovQ3WkjBNQfuxfbChSHUhDvSyIdjrauGyUmkLXcz7J303aX6fTuQG-BBui1K8OBJ75nJjxcHGhOJ4gemZs6remO4SUzlSH3UH_WhAqij5RI9S9gR7QcqtEd79YIyR3pQl0yXB5j8_RHBjwSY_OnCTVhA8ilX5tWjAb0ckvizgBUaK0-pl6bgPKncjTQ6pgQ-yjN-5RW5FLu8S6Eu31lQ8MKFP03j_zjHWcLCtpQTD5dGJb7aTN9xbpq-pD6DOJXX0vIvfZNQtNgPxEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h58IWXIQ8-H8079PsHIFjFvCbZW7Vksw9UeRUzvutwJfXqmLfOEhlF-Cx_B8BDrx9OpK4q_vzxofENOESe-fDQSihmznR-jN11FKgkmffYm9LEjFoBtbL-ugtqY2JkSjr0Heps__QTJ5ZjNu5e4yVo6DAdcGju9nE4giDp8UkIg6OWwq8AX5qsORESghvTP82BUu51abLNs_nzSPZaHfjkYmYkQ1B-6GeFEzAus2vVWRBsMCTxVb3pDPyQbfT8qnWTUiOEWVS9hUHBHHlzPY4VWUXHBzQzMtKWqt45Tu7NTMxnKwkqxMaUCmV07pcEC18JoJwXGj08tDOpmisj6mYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBbgfJtJDispvOLgxNsWkanQ7oKiv-hKVHdElB3gqm2IT9KTPxCCInLln1gf33B6pd01F7Deg2XWEKD8DliEkdUdd-pV6zKNpZGpJWKcXe-ghOEdABCRKDdwh5--x9trA-5htZ2ehvy-F5D2BLbNCgFc-85JzyBfIizFk3_UspTDUTBA1syESEPKha2t6Oy4AVIWScm7KMX9wfWw83resZbiZ5B2Ba1hfd9XuwJr14Y3xyL2VR8SEwnMoY9nWVOgaCS6GK17QC_X8laNWwmhRBjNGLXWMrll3j2qVfUpxM61RNSUc3eMF1Rlj-8xG36zlH9mOnIFkyqOztUMhY2nHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNh7J8GV7Ml3gtu8Ygirq-tRYZE0jQren_9a6ppfv9FlDqpFTN9IeWfsJ_EHQhh11UdqtJ8QPBWjOjo5ed7O53a_m5Mq7MJbB4QgnLl2SQU10sSkVTSGdaWRWYDiW6D-8X51OhwFw5-6qoOFzYzcRQhxZPs3fKH8GgeAGI3nwdsaxulnsZB42JpN73gwuY0bdvYLPsLEkdzJ1oyBwfzAsEE1a8rrQyqBKz0vK5s-tNWTG7S8eqY5BMYYWuoZHzAXc8pgr6ILVhuL1M-V1VEVevYdJTubzBzFz6qSPcLpgWlnmznp_x0JSVIxHxq_Hk9m00L_aEe1uYDUrcdMMpUIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN18XwsqeE9gAZSK9rqvAshlGV7il0RDwrzf-C_gN0AnkkVCiEirC7hbCORzIui0-EBCqgWZVPipZY0X6H2OfQlKpS69u5hO46NZahxp5oY0OOQe5-8cwGN3Nni75o7CDGxr-NUx1rpcqan_B8uU2e_PSLr2aUxRH9f6NXeOgn2PDt1F5AKJPsiDSg25BTrFPnXWjbA2-rXp1kMxp_ZKCFUD_2Y5YRUN2vLcn5LMTP0-Tw94MLYCn1gtYL3J7-woF9pBHEKfgcFiSDxEDT4lcBb_fQLg2uZiihbPjjuWySPgH1EDgfeVZLU-z0Pj-B1KA-5Rj2AazdJQDOGpk1uXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkNgQEVey9IDL727XPxQesXVncOWKXbcKszLTAwqog3G2wVJXlUhtYwpqca4k21ReG_EHtrAobbgoN_eQe6s9Z7YXO98SyVZdSi1YUcI0nqvt6IDobvvqTbHo171C1pAUEePfJJPbt7bnjMgzztMIkH3Z1RwldiZvYTAnr0CoyDl3GzxkcOrNxlz-aVRzBVQ0QBISGoFJi51-7-vZMKW-G5OgQoepI6iXYHFV_05dEenLiqUDTtScgHyROcu_NepFsUXK-a8XbkOkTdnCk_F8Wnnb1M13X87hbJUm4PTZ7zqJn8KAVoFIjVnCtZOLN12kcTHRJp1Quv5-x3CKXGJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUDPe_NAwkK_wCOuqaQituwGcEyrjpiL-8HdP-lyg2-lQuF5ei-zd-REXPhiDRgTSEJKXj6gTPMc1VHEK-k8kRmgdHuFhn0Gy3c7PJ81EBA6L1EYxojH6sZ92-xz_XnAJa4aiEmK6awI_08vyN4X2ypt9PzUu4ZbgoC-l_1Wd1kfL09mOowbl5kbxczpN5yfO9dkM9kSjGWp1-qaERehNSG2avIgF2w2LXfbioxHUJQVQip9ftH0aTT5dMR1f4qUcPaecds_S6y7jxV39ZmqxflTisbHxf4Tv6n5irOdzgGfparqlUWDsMxmTsSFA1I03oIMaYfpIxJuDTLxidWvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQwP6mRG3ssbSLnF8nMVdFTGzwbumhCcMKJSxDpQmUp1eyMFbf9ah3Ee6Xo6KQy6Tp05GFheHMdQFKFZ0KCIT9LN2NDgjiyXuAAAcALIeH7paMNe6Nld3YkCJfG_SZ9T5SDKS6eXHqj23G59pNcd5_IrOzAzi7u7PLDvpiNlYxdjsCgFzaiOzIieUrAMjo8OGextY-X8-t2dGHRjXsLAsaZENiXEFt8lxWZXnN9DaOpa_GxzSJvvv2npphsWu4yHTcv9-4bRqqXrZWGomNTcMewzRAyhqHV7KK0icBMxC-RYnr0QfMJ-NMbiX3vs4fW7f-PHFG3Lp6L3DTqBtYy3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tfb4BMimAhZrcnnHk-fz6QrEzQGoPCMPiOXvHMi8UKp1Rdw4CX-ueasT0ng3rHNN3hrDMufxOlwyh5f8G0_Ik0_5VDobwu8E4CphzwrlAYxkBPzHPRal-bhUnP4WZC1HHjqYXNg8B4Gwt7u3fc1-K9XE3Ka5SCGhxZhzBhSsBcxQlwOUzAnfFFpE2TMmF8G5bUzq8wT8xxEa8sp-YMR6rkjZezAvaeuIGdQB9uHJqQ02FUpxxIhsxx9mhNgF_MWzPMkB-CYY1qcBEbJnXjEmvL45AWubsSIfeM0uc1pMJT8PjunjsuN85YVV-QDlUP5fCW8Tk2nOjJAZ1zHnbSG8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSHHReIXm-bcjQJbdBaUboThaVkFNu9NJGY5XNKP0aLdJuYK3FAuKCrbCA80mJSkjDWDPulOdl_GG8ScSnd1gq1QIMZxdAs-Tp_gM1sSU9QWzeuKM_G59PkRLjzwuzTLdk3_BVaKDZqcHgQBV4G1vfF89PJAPx7af2p1XFdTlY6_Cr3LtktYvx_lR8XrVcus-Bm-811Ad0IhvFcwqmyZPq-MPMpDKbSTsOlmI1wMEefcc85IltAyHoi-MrxbxD8HguKr--w0ULNyFNcXn7wkUFcvGL08HJEUILuwAW74c6WIh1y70JQj_Rl_ZvtPocsUewErK1kYRzufhrg6y10YIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=d6wrH2PifF4FFKRnz3uCDIFN-H7Rdmm55GnKwtJijsO-vUJdi4nqTM00Ap2MypzJBoPSTqF3HZjKyKdPxmu2k7QuNqXMyjJ5lqoWU7DvPQ1YBn3BLu9WMWFz01cvhe3ob1CC3KMEWbY5eSDXY3zZyqY_DNOkihnStraBODIFeBOD-fcE9NYRi-OiYGWZipLJLKJ1Ag_51Zc9ml35pxIU600fzKdRK7yd0EnXH-LftJvnUkBXBmHxALjR5E9lq5Mjowlb1obMETYc_nxW0I8GfM-X1gxvDeU04h0ZS28G5JUfV33srAv1pXNVd2695Zw439hesDXwDllJOE7l1NMFRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=d6wrH2PifF4FFKRnz3uCDIFN-H7Rdmm55GnKwtJijsO-vUJdi4nqTM00Ap2MypzJBoPSTqF3HZjKyKdPxmu2k7QuNqXMyjJ5lqoWU7DvPQ1YBn3BLu9WMWFz01cvhe3ob1CC3KMEWbY5eSDXY3zZyqY_DNOkihnStraBODIFeBOD-fcE9NYRi-OiYGWZipLJLKJ1Ag_51Zc9ml35pxIU600fzKdRK7yd0EnXH-LftJvnUkBXBmHxALjR5E9lq5Mjowlb1obMETYc_nxW0I8GfM-X1gxvDeU04h0ZS28G5JUfV33srAv1pXNVd2695Zw439hesDXwDllJOE7l1NMFRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UadSL3fe3NxLamypY44zodOlGctVsio4zEnWUwBCTjl4Yaq13eZGeVXE59ypcsIOp-aMv00XILlpQgkPJnzZ6_O1gcyTNaBXh8OyIGikme_wezoLoHzEnkVIknyj9SDNd3Rw8_qviozsJvxSL9CWkex7J6Vi0CVOr6WiWpwuwB0Z5sRLd5t1VAcIImfsf-CYinW7mAWRmiN9uTtyYOsje6zwGl1yQ6ZKdKfTYf0IZzk359mVk4506HlqRZm0s95kuHSV3hkYPbBXZoKtldjuD5gaMEf99T8s-XmRfOSo-dPYN12b6FGVTGIHybYhB7rNf6F7HOOREdLB085_gaXMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLizgHkQwpEBZ7VxDdDUdTGJR72ZAK5u1H6eZOC7gBxF8s6K0vn9VOCXmLZ1Yv9DBva9iP0La7lbbcHCCBEWWKvej_Uv9MvgO5bUeuvuBn0Sdkn7u38INuoO1m9a_YyPt4OZAuDEaGxSJf3rUwJRyVPu3FLo7XzaC9IHB8g4G67QJSLbCvzVKWp56MgcmRHJuzUnNyb4Ehx4_yQCYQ4DRSzGTaTEOLJch0hV2UYJbVuBwfr-btDR-waZx-fFXi1dsVW_i5LtWnmLevPPW36nb9UzdeKV5HkdGpgh1YZr2a4xGza_AeOBJnB434KZicAeZQ8x8syM93MA3cCwaXKlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=LFuCvCT4nT2UNhO-3QBKzJ_CLfNH11kq6J5nWNSNPJZBYlwUosyszKyEI1IpJyJsPnd03t4OWiVogbb9pfnc25vrviTwtdd7Y_5hlVAqwz6WMLSK-AHyLGQkPkKOSM4E0XwP_rZAYqRL_ZRCqJDMYZn8skiXQ6iPuPLvH-IrxHjNFRLV0TG6bRxHdyRGBwv1zMkD1NjhZ7G1vAUa3HjXlpBoVMmjG7c5VwwWJ7wKTtsUPgAqffPWvzCvfqxO2XunzXmO9OpdsAoEFn_yraqWsBy4FDTyNOw0RnobpAg2CW0I6xLlnwhBzly4JE6QRfH5wjpiYtlPSgAu55NapkI1xQHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=LFuCvCT4nT2UNhO-3QBKzJ_CLfNH11kq6J5nWNSNPJZBYlwUosyszKyEI1IpJyJsPnd03t4OWiVogbb9pfnc25vrviTwtdd7Y_5hlVAqwz6WMLSK-AHyLGQkPkKOSM4E0XwP_rZAYqRL_ZRCqJDMYZn8skiXQ6iPuPLvH-IrxHjNFRLV0TG6bRxHdyRGBwv1zMkD1NjhZ7G1vAUa3HjXlpBoVMmjG7c5VwwWJ7wKTtsUPgAqffPWvzCvfqxO2XunzXmO9OpdsAoEFn_yraqWsBy4FDTyNOw0RnobpAg2CW0I6xLlnwhBzly4JE6QRfH5wjpiYtlPSgAu55NapkI1xQHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxoqIo-7p_KvTp84X8anX7hm6OFNWyf44Iolwn-3-0TudTO6Jg2otIuHxb7FtzUM_LTKrTBoMpFnbfJFFCN0B3FgKzCFaiJnHMnRV_HTinSyDRuj9mhrTIjBHX098xj6Gp2ziFaFKd_L-W0uY-ny0EnJZYIQeUHZdh3BDpEGNOhYe6E8NdzPh8g8UsfpcSoyZ9oQOzRGab1Qid6ACr4ulI5DKNjy2XC9AQj9J9f-LQ4MTgLME-AwwUyfTR-fW2nepsp7_Q2UrNCq3He_eK4gbDqqwwGQBHKUuHwiT_ZhMFg6dHdx3sPC7Ha5D0U9UiUsXQd_cPdzdHee8dRVKp6-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krLl19KGCLTnkY1erpDrDfm0AINhrMlVq2mJH-jjmZn9ZqGJ9p7bETz7tyJrfgXWV5WjvXn7WUbpibvW5mkPYqHBBrYtHAFafYrp5FqZrVowuHWGc3IjRG-v_tAqyXq1oa1ixy2teLh6sMtHRoOprSi9QmK_XKhs3OQ_TXh9xiriitQnoJ1hfh5ntdPFMGUoe9gEVZscoflpJLKuOZuyheBYW5k5kE9nWUavmVlwygGSg2MAHAlA0V-G_Yl9Lb-OknzwYylxKljgrK-88-_oBTxRd-ne1nv3EZu1YLT99JUx4tTq87kc--S83gKO41r1Gwlgd805DUIr71XXUAFGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M862rRz7j-rdt8rKEGlCQCk5Vc-ZQCN3kg9SCHW1aTyN2O0eBYire1wMRDrCfUIAA6bevL26GiXXncq-m1l3jqmkaDVUy9tl71jHvD9zjhI-SsXpsH_4RqG2QwIomLutlZfuNohbEgNr1G0qOW9IEuXzyk61xFRWZy7p2Et_8jHyLtCBE_1aKADlQlZ-wH_8bRNxSnm2-BX-ekqgXPW37UrPSiBKKqSbT7Y1QRzh-RwgwLpfdjeTc3EfHDbmAZu5q9B2p4J12m1XFrM1sDJpSZb6a2IlITh204Bef7I6TAQt8r7jzOiWNps9rDu2El-ThygaahCr9N_yu9TQ_U0dUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8XIOtpD4T46ETtIOCmauk1S5ueU6Y83Qz_YIf6hz2obLLiaAUYL0A4pyd1JFsdOAspPN5oB0Jx15DhiQW4b4Iy7NQnM-os7sh3Yk__zDVG_e5SjTkYgFAwY_CbeIHxQp6BtWOrA8vdqTjU4kPvDREY4ikEvQ1dk6vMbU9FiX6iZPXQu-ekM9xdFoNIQuv-NtHQbkIOO3saMsTG3KXU4cYHL3VrnLi9xdZDxnk7ekOZUNwy5ocMyWTWUStywClJGMqyG8WA_7tuUWDFlJCVrwrvgvEqWTHu1CWfaZzU8AJ1mpuRbp2koW28OC5IrlGMUuty7hvcrfVjFYmcismNAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCybpVyuV9jB36vlKUJyISipsyIcbv9zxRh5LwiOd3sa2i6XhH-aU5B0ZKHGKPPHRAwq3Frw5zIWAcWGQAHZPejv5iv82XR_uSa0uQY6niPOlHx8wVd8mIfF0EhkivnHJPrLrlSfabq7Viy5pw6m0uRcRR8IGF1bRikixqsd_zuVe8vV27WttZMKcLldp2iK2nh9C_ymazpFTg5Q56tshoX73G5B-jhkuDTbxqbJXLZzZwki1stw41omtiOUBotGnODIFTbAyI0NcneB_8fsYSDK2a9uTYM3uE14dEiKWl77DKr8wGY_TF7Ck5Si4v91oTWxVGr213wDNG0XepC0yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=cSDYssIV-_DyEiOehHG1Nhs8kqXaXJpiFMESQIyXLu-D3FrREYkrohKUMTWAS3CHVhnrcniCHNVFoqvCNBtH3jcmdfiCpopzPSIPe15da5xc9Y-mUUV4rvKj3AeNLYBYN66CaG4XWyPcFcFGr-sUz3hU7K6jFa8j20STHi8dN6h0Da7VmKsi3cx28DXkHDxeKy47kcwjoWcn65nVoriGGFl3GnahyZol8zZiYtKzzjwNgMge97ektO6Oqpe73HwBTvG74qE3bw_L7SJMdGeW0gCtq2ROdBcxlHtx0obQ11dHINYBf7qG33-e9sCWyWri9GBN-Cf2LpHyr-lCMKXzlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=cSDYssIV-_DyEiOehHG1Nhs8kqXaXJpiFMESQIyXLu-D3FrREYkrohKUMTWAS3CHVhnrcniCHNVFoqvCNBtH3jcmdfiCpopzPSIPe15da5xc9Y-mUUV4rvKj3AeNLYBYN66CaG4XWyPcFcFGr-sUz3hU7K6jFa8j20STHi8dN6h0Da7VmKsi3cx28DXkHDxeKy47kcwjoWcn65nVoriGGFl3GnahyZol8zZiYtKzzjwNgMge97ektO6Oqpe73HwBTvG74qE3bw_L7SJMdGeW0gCtq2ROdBcxlHtx0obQ11dHINYBf7qG33-e9sCWyWri9GBN-Cf2LpHyr-lCMKXzlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PikNnz7eCc4kJPOQo5xB1xYWQHqFbLJxmuV3iLrgcP4W83F68MhEIuvLlTPxn3ExQRf406HkwIWa8pIQuTTe3_FkiGCbqZPkXUP2c7Q2VDktqFxUtwiF8qSflrNjzW8PJ2rBJH44QPHAR2KF7cIt5qItVJOv0-tS2YZaR1CUhIB0lHRa2BiOB-l7rfcbod81JmD5reCd0Fp-dOOI2HfGzUk3goN-Af4lAu7ZArcKl3EX3iZaAKxbYnJ66ER6ZzfnGj1TmXm4WgP3OJ9_Hna0rq9Ns7qzsMGAlLamm3pYCse9T7pvHcWnMhFRg9vUL8mXB9K_mSXpf4oJ07M4zVkbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV-EezuiPRBnm4C7HJYqoJTSVfJL-l6oYXijmgaBqKHj-VNwrCn9f3Ioxualb7Ymh4S21AACATRujUFJNZVw0hC5ktT9uanB9sDDI7vEsANJwBVMBhq9ZA9EfsL9Lyue5FFK5WkCzsnH94gNZhn2MgO4lEItfeQM2BQBlxU7RCcAjMvq16rgpyFV2mKLKz2w8YOYHiBtESxgQ9SB_2jWkrqiWjiwFFtiiJbhAc_ATN2mu4vKVAiknh0RSzMu8SEntQc7hVgM3vOzEP6DbUXSeBChGFxWg5LveqSb6eLwxtLUtDjCkLrkVy6YveAa6APX3knhnvmSQCZ_h8uIKfHZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC5r1pk5uWlqChUJR7gd8hFnZxtEJICwPirxVZ6D_BEtvyRHQWvkhSvK_yInhtzwSu3UguBJ659FTuI5Vsn4pr1mz9XBUWtEaLPvVw93JMYQ3UipuE8GtXyuylwCMHDTZG5S815HaCViB85w37ASm6aohHwYFirDA1hkh4jYfWiOxumzI_EfJdV06ftSok65BHCpaNBgK3BztVQgT6Yc1ON_vaU2qvgTv1tWNnl2InvtlLysNg9fBPpCytwrADaEdk9g7FA-DsX78I87D6P1P0Ige0EE9LqZYBDl-PUHbid-8de9d3uf1ALVA2Iyq8nyvaxQ5BKqw_vUvJtjUKn20g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrw6aQh5wn6Q9ikm1eLJ45A4X5Q47F7-YGgm9Svsxgu6-P6csOjvvAxtMFXhHTL7Os_NHIyZT1nz59SR4ky7FBbFfVvY1Tb5PDfrpPaf8d3fB4XvdSPfr_eDcLH6R911D4MQZERmr_2wzkJ5mgM4MlSxswybVMMuW7SICvUPEdPS1rxuF3JCqN3CIIudzKzxOlPe5BobQ_RIAXIgF8cidUyq5SqBzip-UAuftrRpUfWjouy8sq1NUVK5OLhfb8fEQiAjS-GRPs9KflyWbaeZ8Yf_v1SBx_RH-cXKVvIsJEukQa_agirpyPOYSlRDTxekm6tUftbt8pALJhWedkxmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
