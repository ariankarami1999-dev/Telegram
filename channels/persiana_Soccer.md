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
<img src="https://cdn4.telesco.pe/file/GE3yq8bkQ16p5KfNgI1Kp4BiaWvo7k82pOjoAtIfgr7CN_3e-D_u626RTinhoyhxxvIOD37Xu5BTiOoHmluS7jeCeiZScrC_OIWsiB2LHY6f3UKXcLef9kLtd-TJiE3VbtxzSmat7FKUqHvjkh_SS706tejLDHlzq6WVutfTtiLr1_5g-5V2_PeDSER3hsoW5zVw1CGif_BMggM3R24N5QGKJoNHJvFiJDmQzjS2RFOcBTlIAaHrUbpIW7YBmEtddo1HbPqGmqv6om9zPC1otoRkCS_IKZtBgLmxg1Xl8kybYdnXEaPoCOMMZC2sVA585RyybcvPRUf0hPI9dG2gZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 551K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-29369">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMyhKNpUvQvlV7kFdiN9wYhmx2NC0zQMP8dwKIYlT_2WxOngRvZMQVcScJ2gW7N-zfJ6vkd_tYFp0rEanrZ9vQjxWgqh1rdmgiRY35fP4-_Zg8VIdSD1a-SBu1Di1p--beGsmBnHOrRTj2X3o_y_tJCqu6YWa0KUvQgMKRwnRHqnNA8BAunmZX3vBq36OBiJ_Y1pelPLOSbh8_xNlQV1VGJRJJtCSmJR1D_lV4pI6PNr_gACeGZ11V3a19lWc21kwMXSOvxxZFT8RqlJDVldm5atEXmr9K7FHhM9_qFn_yqjyeOsqxxJQ_33t4L7_AYtLN1yJeFslBBB-RV1O3310A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/persiana_Soccer/29369" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29368">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpTHxnBnfOoqDJ1wHgg43uwSpbjUUYF2EBdfbqVuMh4hfkV5bsekDuu1Ec_r_1LN_9qrAvm2X50oX8bLwq8b9Go6GIzQ1PG05u0pYpVEq8AOCJpX0obx2tW-YEN8KFWaDA4qkUuX5_zLuP-OUgRLrpWgXzOMU6odsqxiBilc897jYM55qhKY_BwxTVatiMO2gPwK8CVoBcZhTyTGI5n7bmDw5f3nPI006vtcFmS2WwZ9Nuxod-yjS4PyrAjbAsjVVeCRpEvYHqSrgf9M_TltB-yyE4j5mIczER2XxCHn7AwX-bOuCMSn5zOVwVnnzO1s9nHAVY4l9bKCsxuLPNfXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
لیونل مسی آرژانتینی ساعاتی قبل با خرید 100% سهام‌باشگاه‌الدنسه‌مالک این باشگاه اسپانیایی تو دسته‌دوم لالیگا شد. چقد لوگوشون‌شبیه بارسائه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/29368" target="_blank">📅 14:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29367">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBLWHRP1dxenIIdX4L9fQVpI9ch25KdTXa5M4ZkXK25TMP1tT1NBm1egZB2rVxkq_M2JBjYOyNJ8a6rvlT96nzVM3Gjj37hmHS2W8OO74rij1DwDk5fEceqMFoHO4swLLV0YNmP-grJ_De3QduTicPVjZ1FjFaRJtpKxW_Q01FXNdEoeuh7l500aW5Ql8OtB6kMgdzrzgHPDAah1luuZzdPIfuvjU7BWnf4Pcls9_vBclqmrdkqn_6fj7ClHPASe0GWhbAqbT4xilvf10DaU8hU6N911iJQM_2nth-jdcsEhbm1rTsVcYVEWYYvWg1LxvrZncz4ZqzVHHFxSPH8D8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/29367" target="_blank">📅 14:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29366">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0TnUsdWqDsnhUtRa60Vo1mqedV06iZ3JSue6lX1O0wkUmqapoB2HvtwNn7WcHIuG5UHJmDzbQiAiYWnFgsn4QdDwCM3Et4OERulCZmPJY1N-ckosEEWioSsjb9C6EQhJf_fHwTVh-Z7kRdr49AE_HLjUCsJ7ijc_Ij_Ici2i9jP5jMPIBpRi497GMeNrHxdvmGa-oDEeWuNNiFIftVG85Kk8fxqvot3j83rawMP4DCWdPpBSCUZK6_EN2aMYVuhtXb-b73nTXysNgEGdlH4n7rgUMZWDlky3eJPTLFEeS3otKBj2mniixPjbnvSMZCUg25Bl-AMUdBvIYX53aFuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌‌ملت‌‌های‌والیبال‌آسیا؛
تیم ملی والیبال ایران درسومین‌مسابقه خود درقهرمانی مردان آسیا 2026 بانتیجه‌سه‌بریک موفق به شکست چین شد. شاگردان پیاتزا بااین‌ پیروزی درجدول کلی‌مسابقات در جایگاه دوم قرار گرفتند و در مرحله یک چهارم نهایی رقابت ها به مصاف تیم ملی چین تایپه خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/29366" target="_blank">📅 13:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29365">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=Fvjxa76m1RhC2paxc6CVA9Ms4i5TgdOMmXhE8vEHJuuaxN9P4BEGUufvfEP9WFLSd4hZPKntq-u55thHIjiuok5IaI7tYhlREhAXMZ3BHKh6Hd-AjfMYR_Anz5qvuNFY071GsI1HzJbDqpwHGzM0Gp__RY39nJcyB4yekkERVg1CuMtiEYVPVUjZ-TUdVXDvedQU9KP9XmcHgAgswZT_n7DPm9okTa9sCUFhBAQg8nIxMtWjD8bIsmxuoMiri_vZp5QLxk2bgTgQ_QBWximlvZv9-P4wSzTxMipr90JhWz5I4nb3Vmlx12ik7u_ToPMDnwlSgSq23TlCPRa0Hv_yFwI7YgImeSv_I9mXez78C03c9PYjnrnkaaytYC8h-Lk9-QYEn_wuTr3Emg7BjL8AdbXgPfQoPB0t6XX-BGiO5-5ISAv1ILVkyEZRjUt_n_xvPYuBcBSn9ImcLNZvWlMSpgh0zmz2n8Se6FjHU0_hCUHo4ixaUsps-0eLJ6OFvo7DbvxN2rvO52fnPly1Z8Smbs7KkRUnO5RmNZ5x_QrUPUnyCXg2WliZPAQmhmlQL6fOj8fx2K8ZXHpwkQ3fRxHeDFLcUoV5UrMFpOZ2HeMffnYvv77-Fl-EfQ58DwVOi11fKz_BIcG8YgvxQNOvjFy8SyYA1TheLAFwbSAu_tnMo9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=Fvjxa76m1RhC2paxc6CVA9Ms4i5TgdOMmXhE8vEHJuuaxN9P4BEGUufvfEP9WFLSd4hZPKntq-u55thHIjiuok5IaI7tYhlREhAXMZ3BHKh6Hd-AjfMYR_Anz5qvuNFY071GsI1HzJbDqpwHGzM0Gp__RY39nJcyB4yekkERVg1CuMtiEYVPVUjZ-TUdVXDvedQU9KP9XmcHgAgswZT_n7DPm9okTa9sCUFhBAQg8nIxMtWjD8bIsmxuoMiri_vZp5QLxk2bgTgQ_QBWximlvZv9-P4wSzTxMipr90JhWz5I4nb3Vmlx12ik7u_ToPMDnwlSgSq23TlCPRa0Hv_yFwI7YgImeSv_I9mXez78C03c9PYjnrnkaaytYC8h-Lk9-QYEn_wuTr3Emg7BjL8AdbXgPfQoPB0t6XX-BGiO5-5ISAv1ILVkyEZRjUt_n_xvPYuBcBSn9ImcLNZvWlMSpgh0zmz2n8Se6FjHU0_hCUHo4ixaUsps-0eLJ6OFvo7DbvxN2rvO52fnPly1Z8Smbs7KkRUnO5RmNZ5x_QrUPUnyCXg2WliZPAQmhmlQL6fOj8fx2K8ZXHpwkQ3fRxHeDFLcUoV5UrMFpOZ2HeMffnYvv77-Fl-EfQ58DwVOi11fKz_BIcG8YgvxQNOvjFy8SyYA1TheLAFwbSAu_tnMo9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز جذاب و دیدنی دیدار هفته اخیر آرسنال و چلسی؛ میکل آرتتا به‌این شکل تونست ژابی رو ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/29365" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29364">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=QMs5pO3rS1XCaU1aQKaSwkZ_Ib0op1XlUeJ2yohQkkL-3L_OkW12mFMeAT1AS7wQvmMDYEIxCsB4ciCUv-fE5OoOHBvLZdcY0UXjCwZHjHE0-lkaUQM93wza0wdBHQnE3kD9Xu4RlvtPsTqox4e3Uh80BeZILfswA4ewoMdk_50Qiq3e5kTuKMng6FUTmrXve3vpYoHp6EKXG608ZXsqrqemMsoUieH084ulD1DfkLIrajJZhqg2A-NeWXcNGQkI49LpWvroqLP_5jgi6yrBbPqiJYtFhsg2NBG3ar_RSEWWX-L7XKUs3LFfJoq6f7m8OaPVQHDmfvbzh1SiIqt7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=QMs5pO3rS1XCaU1aQKaSwkZ_Ib0op1XlUeJ2yohQkkL-3L_OkW12mFMeAT1AS7wQvmMDYEIxCsB4ciCUv-fE5OoOHBvLZdcY0UXjCwZHjHE0-lkaUQM93wza0wdBHQnE3kD9Xu4RlvtPsTqox4e3Uh80BeZILfswA4ewoMdk_50Qiq3e5kTuKMng6FUTmrXve3vpYoHp6EKXG608ZXsqrqemMsoUieH084ulD1DfkLIrajJZhqg2A-NeWXcNGQkI49LpWvroqLP_5jgi6yrBbPqiJYtFhsg2NBG3ar_RSEWWX-L7XKUs3LFfJoq6f7m8OaPVQHDmfvbzh1SiIqt7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
فاصله‌امتیازات دوتیم استقلال و پرسپولیس در تمام ادوار لیگ‌برتر به‌کمترین حالت خود در تاریخ 25 ساله برگزاری این مسابقات رسیده است؛ تا پایان هفته‌ششم لیگ بیست‌‌ششم استقلال تنهابایک امتیاز پیشه. نکته مهم این که در محاسبه امتیازات، کسر امتیازهای انضباطی اعمال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/29364" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29363">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1hBmY0jk2Pjge70LqQEW7METLk-9SBZ6zdQDEpFBlXrc3vPrOMsCoZu6JBGphqd7uTr361Lx4nOr8BbgeVYoaVD4BKppeYjJrANNNGMsM1hqlkVWMKbyI5PCpak70pZnQYQyyQBFpgdw1I46tNrVXgxPzmtfUw69YuzZ1f6fUB24ku6R5b2d_kymZ_SEbBPEBO4tK7ODS1kOaiVWUuXX_Aj7MbD4pQVrdP_JVCdytHPI1cJs3NAvYf4we79fV8kBwGDARFogXDUeY-_RzTTKdVuUlR5Ro43QHC0PvQ1tYnDoTmQOxpkdDWCN7BNf2DG-aQVEvvZfY0p9n7lGTNr2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇪🇸
بارسلونا
🆚
فاینورد
🇳🇱
⏰
ساعت ۲۰:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/29363" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29362">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=r0TZlDKuTJkTz6-9tqifLQT7fVHXpP4ODJfVVL2cq4oZC__kWuqYV2g2rditdd2O6KumtHZC0QYkTd2WQxWsduckm4sPqKq4vQzf7EMZtxtmn-Nat-w_joHiDvy40ouHIxuFdkH2Y2FxKd3ZRcEf6l9MSijUOKoHV5ip-1DOXawoC4xZ5Tq4hiFSS-xbUPAxaab2InJByk8rrib0FECgxN2noTx7-3HmiDupLRvm8E6NE46Ng0Mx2yR96Vor7ciFkS6w7bRSnby6EzNL7Ay1blhn0PkzN4uTufgzL3FrPWTXQ-Xc76DSbwDHGsX4Wz45JySIGp1FjcDmktm0GIkqsUdzGgrQnpi1mQ976WGgVaiMWrXaV2JvnZDZuiYdNASAFWnEg09RLPZveVnolFJdsL2vyiLOUhbeQ6g8lQR07FZlF8Z8UOjM6PelNU8NbtPTgQ3y6uzx4G079uKKfb30z4YqKr1rfEUhMe_MmrOQDTN774_opohZxWthI7xJEUtHGCsPNGBziONylmwVRa4ios-aJfN_pEZ8PbL6hhPtNYusV-aqtmgjlVrdOVzdVKDYUhZq_q9vEcxJ43XOrAyEw_vX7FxksnE5nae207IB8N754D-jhklUqpCgWx_8W_zZg7UO8bbqOrDiGN6Ub_KpNfshfpOb_-zCl8UvPcfdeqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=r0TZlDKuTJkTz6-9tqifLQT7fVHXpP4ODJfVVL2cq4oZC__kWuqYV2g2rditdd2O6KumtHZC0QYkTd2WQxWsduckm4sPqKq4vQzf7EMZtxtmn-Nat-w_joHiDvy40ouHIxuFdkH2Y2FxKd3ZRcEf6l9MSijUOKoHV5ip-1DOXawoC4xZ5Tq4hiFSS-xbUPAxaab2InJByk8rrib0FECgxN2noTx7-3HmiDupLRvm8E6NE46Ng0Mx2yR96Vor7ciFkS6w7bRSnby6EzNL7Ay1blhn0PkzN4uTufgzL3FrPWTXQ-Xc76DSbwDHGsX4Wz45JySIGp1FjcDmktm0GIkqsUdzGgrQnpi1mQ976WGgVaiMWrXaV2JvnZDZuiYdNASAFWnEg09RLPZveVnolFJdsL2vyiLOUhbeQ6g8lQR07FZlF8Z8UOjM6PelNU8NbtPTgQ3y6uzx4G079uKKfb30z4YqKr1rfEUhMe_MmrOQDTN774_opohZxWthI7xJEUtHGCsPNGBziONylmwVRa4ios-aJfN_pEZ8PbL6hhPtNYusV-aqtmgjlVrdOVzdVKDYUhZq_q9vEcxJ43XOrAyEw_vX7FxksnE5nae207IB8N754D-jhklUqpCgWx_8W_zZg7UO8bbqOrDiGN6Ub_KpNfshfpOb_-zCl8UvPcfdeqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
عملکرد 9 فوق ستاره‌ درفصل‌گذشته رقابت‌ها که در لیست 30 نفره کاندیدای توپ طلا قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/29362" target="_blank">📅 13:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29361">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732028b756.mp4?token=PDNrRf11q2ZBXaWZYfy-8XRGW5pbphpymsHMIk1Pw1yoRaD87E2ACy7S0spePj1dHAr3wNKNnRlrEsVqYXwe0ufUoTb6sfplgV2tvfHqkt0YwexPkyeW7r4mCMLfpyor64lKGfWBvuDp8IjLB6jg2smg1ufh095A5m6qlHiMftldMM9un-5uJCG434kNvcur9qVzgwlucZ0jKd36pvxlKYDV871KqiRu4HyNzq5Jun8TtSFBKFMw1HFrvfrc1F4Qcr7cMDSYnGXHgQMHVfxO-DaaLdYoVqR67JRpHyegZwKZTgkXMJoNMd9veMtuWd7V2xt1o9hVk15H-MxHyAarog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732028b756.mp4?token=PDNrRf11q2ZBXaWZYfy-8XRGW5pbphpymsHMIk1Pw1yoRaD87E2ACy7S0spePj1dHAr3wNKNnRlrEsVqYXwe0ufUoTb6sfplgV2tvfHqkt0YwexPkyeW7r4mCMLfpyor64lKGfWBvuDp8IjLB6jg2smg1ufh095A5m6qlHiMftldMM9un-5uJCG434kNvcur9qVzgwlucZ0jKd36pvxlKYDV871KqiRu4HyNzq5Jun8TtSFBKFMw1HFrvfrc1F4Qcr7cMDSYnGXHgQMHVfxO-DaaLdYoVqR67JRpHyegZwKZTgkXMJoNMd9veMtuWd7V2xt1o9hVk15H-MxHyAarog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29361" target="_blank">📅 12:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29360">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbJB32RuWFjkBqfaAillMrChO2QFEuPpxZ6cLliFASON2WaH_4FM7kIsxUFm6TaR215fdrJ7lveytKkKd9fsIMwSLB-xj8bJ8koBsr4eVTSlRY70xRSjdB3q09uLh35t-N-vTJ5np6iORlaxq2F50OdDrc4bk3kfqe_9c7AcB1c4gQMKJO_IoiXAF89-uXdMJUJTMDhvhwNs_gV_a3wBt48145sepmDbKCrlQw59SykvlZDTH8jF6tmC6H4lpbmrOmZ_bWn_mSAzmjp_UNsKpzmfiPEdnA9WVYi4ZDmE7vsyCPGb0urPCTamHJZCXa4BSiui_E-cBL-RVe1MOb_y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برسی عملکرد خیره کننده رافینیا دیاز ستاره برزیلی بارسا درفصل‌گذشته‌رقابت‌ها که یکی از بزرگ ترین غایبان لیست نهایی 30 نفره کاندید های جایزه توپ طلا در سال 2026 به شمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/29360" target="_blank">📅 12:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29359">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVU117DTbP8f3puMKuaLHssGOkNXvGaEoni964X1RqGPgxjD3b__KxacX8ur3IQUrNAePqed3STnMXIODlNK-pfWSgAsqCDEztEg1KojNXji33jb4wHu4uXeuhfQK-UnM7e4g--TrDIawmoMmIjvGyheVAiMcdfpOxMzTHHVU-AnKKtdPUYexbzsEPXGCA-wI-kGsDMby4TPpGX1IrRNBiayls9u7xLUNX-lJnAyiZu7m5wih24O1noamt2hWDPYns_UdrEsfr7mx3UW5E5bM6Gu0YYVnKT5XjfyaKn1vbycQxMAByKirTHc0zgcfL9clzNhVgTWOQpVuMI9F9_wZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/29359" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29358">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXcAmMisysnLgSDmzRndW0if9iG65AhZ7nEwSrQSO-LsUaDu5ojI1MpT6-u09B-_n49NCo9CU9P27-2D8qEC-jbWR2MHMzGISK0w8JKLbFrgpHG69gMfxbxxoZE60x2KIFuMiBRi_e5sv5W2N0PO_SyRj0G5MRN8CNBBebFO5Q0tIskDCQ6rve0KggmEF6VvAgzL0znr0UhBoelQVsa19s5OqTjO6IRlOIZdDhDmUlwv85G24hTeUCBPEUMKItxNxJcU5evIw0A5AMNB1SPviPNjXd09s81Hr9MRSfqZSbHG9hibYeJtRhzDmsj_G2uQicT2-7wryW138qu_Q_j0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29358" target="_blank">📅 11:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29357">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwb8Zu4cv4bfnl-vGjRQdk5Wlp_iH91r6t1v3ea-cLUemXQgWSTNXumJqIBrstAmTeb2KdR3joplBNll4mC95kqmsUosuGg20Wp0XWU8sn-BOz-a9N3NLrjNVYRndRpSx27INmZaoO0Sp4EsNAy1yQv0qXeSUwcU_2BDAjseRoP6vM6DFRQ_aVTbFzibOkNhGnQOBZ7-z1us9_w7aSgqEXpTk99sV3bAfbXyvE-O_M9VzQtmCqZlYs69xrIF9i_6ebPd7-XPwbc1wQ6OFIIAaLEY0RIr-datd27eR-1F13aLXZGolr8datmgpVtbw97A40f4wV-hpDVf7tqPBiR57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/29357" target="_blank">📅 11:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29356">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKO9mOEOyOpco4o7022whIKhJawkCxIC3TfvlzvUVu4kiYfvogZenF-KosAAlo--y4NHhGKEZo5MGkNujN2wLk1QnS2mhe914QWv5EibQCHMAxA0D6V2MRC-YC594oB6G9o_sWt0zSmPKTzg4pRmKupFtP4Wp5QmisVcFudgjKZgcNvyzUB5zLf-0E8CewmwBj9NzVlxoomIzR4oaBXSHjyN3rdpsrtoWXe40-YSB8-IktREH24LUVMk0ow8fcuzZI_UijnAflN7EUUHWgFT05jf-UqBxOCpx-7zFLdMTtJe-FmrvBLhjywKI7R57KCEs4iWgZkDVtz7f2-X4sYV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛
خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/29356" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29355">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jokmiuiDdNFdE4qcMuqL67dm0duNbQ5aXkbbl-iYcJyxRBMfbZdJIAPFvtdrKBHSc9CWriCvDa4V3hOizhpCfl6xXzcnhIgt1WZoEluvF5u56ZoytMQUSJt7WthpuAGJXiPU2PXM-G72uUQzHBhw2ufYNzRHJjQED446L8VIEjf5s_JQzcSd3Haq_F9smezTr4Gp65snz4QuOJjfMGGFdTD2XKBimw6YY55ahSSgRFOCWLjmfz8meB8OcuKUp_SYO1o1gvmP2NBfMa7JFjlOys3bnRRzESlnpNU-Zxsu3UAcLQ1DRFtxMzjmHlDHPEwHrex1EsWhOKwZkn4eN3Xw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوریا شهرآبادی مهاجم ۲۰ ساله پرسپولیس با دو گلی که این فصل به ثمر رساند به دومین گلزن جوان تاریخ این باشگاه با حداقل دو گل تبدیل شد. مهرداد اولادی با ۱۹ سال و ۶ ماه و یک روز، تنها بازیکنیه که پیش از ۲۰ سالگی به ۲ گل برای پرسپولیس رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/29355" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=OOwYtWjrGT6_9lnFmrB4kLOzO6IdJbvp-ainwDKd99fTEDKbebYcr_o-wRVjHUXP7IGsG1hAdmbPkG9uU1xEsk8YOZkyHpw_K-aijykEVbN8QqFIcIGvGuk28Mwf6KqHNhMsnowaxXgotaC4UfpKFPNwsfFCp1y4BbiGIw-jwQ7nrJBqw0Ot0fc2s1NJRmzntCymsTJvJT7Wtn6W-TWrCTvJ5_a9--M0gHklDquoBPEp7gMamy0mruWmptnRaepYfV2SXd0NLSABAfKMBk74sXtituGEYYw8oOHNcJeKx-IqqqS7hXdpbp-vCGTgiaY-ndkjjSnN8qdueeZcs2v9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=OOwYtWjrGT6_9lnFmrB4kLOzO6IdJbvp-ainwDKd99fTEDKbebYcr_o-wRVjHUXP7IGsG1hAdmbPkG9uU1xEsk8YOZkyHpw_K-aijykEVbN8QqFIcIGvGuk28Mwf6KqHNhMsnowaxXgotaC4UfpKFPNwsfFCp1y4BbiGIw-jwQ7nrJBqw0Ot0fc2s1NJRmzntCymsTJvJT7Wtn6W-TWrCTvJ5_a9--M0gHklDquoBPEp7gMamy0mruWmptnRaepYfV2SXd0NLSABAfKMBk74sXtituGEYYw8oOHNcJeKx-IqqqS7hXdpbp-vCGTgiaY-ndkjjSnN8qdueeZcs2v9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت تمام قد خوزه مورینیو از فده والورده؛
جایزه‌بهترین‌بازیکن زمین باید به‌کورتوا میرسید فک کنم اهداکننده‌جایزه گل والورده رو دید و بقیه بازی رو خوابید با این حال فده هم خوب بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/29354" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5zA04yFAgVi3zeAZ4YpXIJyS4XEPrKEuDPLnbprrbqbka-jjt8MnSjOCU8FvBuGIJrSXnUY2KmDUdRc72AjXS-Bj7ptMuFJEZzO4eP57mIm0_-rGznMMZXQzLb7ynmn73RCyP4KmGVNIiuYf-CjZT5GKnj8fIawam1_Uh5PMwua5vao3ZsU68Dqnp8-WoaeY5XXrIoQ5HC7Z5Fbo9XrDqq-CehKxmnOffH9fc5P_Og3XWeyBJyYr9mz6SG0_puriRI9e5O4TBF9WuAHKwNNQEmtDAG-aX4o5wLLfzAyXJ1Jn0RzZR2FUtWNvIw6Ye8wQB2ZriRJfyZ0_2aqCruQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛بعداز درخشش ادامه‌دار نادر محمدی در لیگ‌یک‌روسیه و لینک‌کردن او به آرسنال توسط رسانه 433؛ این‌بار نشریه سان گفته میکل آرتتا اگه قهرمانی UCL رو میخواد باید نادر محمدی رو در ژانویه جذب کنه! قطعا درهر بازی 3 4 پاس گل ثبت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/29353" target="_blank">📅 09:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29352">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kib3UUM0B5J7VQ8-RX0UCxtX_4AfQN9NoPcoziLwsbBlTQe8A_wDNCM-byy3YAHzDnfzey3QSZIxKkXlAGJd-0ucBSwxFEDnhuiXZdHvJ59OV225AZVrRJ5COxfuM0G6BRP2gvnZrgOGwTukCkUT9ujjyFGdAq61Han78oxYcvXXwh0uv0JGP83smKyhGsbapr-AlBDFFnfJi9YcOdaxQhHOq4qhqXsJ_Yd6ckwC5sHu_RxAZccR6KhE5DnLb2Ye2OglqEvfvOfe7diRLiIccrfcSQDF9d6eW3OxQEhaxqTSm6eGFP1jRm5cjN33nSL3fmP7Ok_lQVbaulSXXDV-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29352" target="_blank">📅 09:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29351">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h783phW4ZZZ5QLbAew2wB1vjinSN0tOGDOAEsJzBWuQ0G-n9jPBOiaWijrs5W9LkVfy8e1MALW_4AovuJpc_wYz6MhMD7SzW8VyUkv17pWAkzg3uUVYUgaCv_itrRaCIzQ2YWCahaFBF87b1NT5FRnviY7r6yX_F3HW22ViOIrEt23Ph7rd4ZFlsGtEfQhNBtRwueHyzn4PtrggpZUuuaCzgi6lI9E_A3Q9cqSZafGh5QkBiBndwU-_ArqZHwy6f919TLetRSKA61vKzeZaQJWM0qdzOII-gshxPWntckzEbyqXPJ9yyzKxxPnAbYLpsbVuFqxWC8RTsv8F8LJK0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاکتیک‌ این‌روزهای کادر فنی اسپارتاک کوستروما درلیگ‌یک روسیه: نادر اوت پرتاب میکنه یکیتون بزنه توگل؛ نادر محمدی چهارمین پاس‌گل خود را با پرتاب اوت به ثبت رساند. چقدرم خوب میزنن تو گل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29351" target="_blank">📅 02:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJCim-h1z4QmxU9PRNgLXeMBlKuHLYhdvl_uvtBjTXP7YejcyFzdyfdVRQKHcXban33TtZrYVj5OV8IlnjcMYw0VNKNYlpR3LYvVYlqrYr-2hyVMMUSbqlfaV_gHoZvMMkDXNrQST4Kptj1IPllZuam3Jo3ag_Qx1-oRITbAgfYSn3PsAnXJx105EvB8B2vgdCnQ4__KcoqpDfqUyJt0C9ziuGfndq5VpmazgKK4EYgl_0-Gg2gkiXyrurk9AyVz0td2p4c231cWNCHek9Kl5mcV4xIHTRPAkjPWPeMs-Y5IJ_UU3uesdZA7bsqdPwV1Y4z57kLpFwySr0j6-9iPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ ازجدال شاگردان فلیک با فاینورد تا تقابل لیورپول و اتلتیکو در چمپیونزلیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29349" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2c4L9-9btVa_WAvUpowDUzOqshdTRWYlSsD_fAoAthcX2_nCVSQ5MZ72lM0dB8d1wseCiQRi2jVKNbPXRR2PdbtXi8aIsuogfxUBTUtzE9JfIwr2CauWAZTJhmIeHS01FJJzg27edvqfSy7Y5AhOet8PgqGNG63V3uwu6V1ohfRvAu4L4quYcG6rJpCISIoBr0Z5rmbQHrY_gHloScIpkjWrUMdWWmDFnOMp2GEv40QuPY6cN8IQ8zaP1W9u86IDiXp-I6iYEQUpI_aPFHUFy0a-Y13N2vfI9mS-gLuFOMHikmz5FNVf998mx-Kw2jvomxhc-qf1w2XbBj1jkpQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شروع سه امتیازی رئالی‌ها در UCL و برد آبی‌های منچستر در شب دبل هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29348" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29347">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRPj_xMmmr0j3jK3PoDqPYK-EgRGkBga9kP4gWkfR5hBclZ7CErTTYtzM_SRem_DW1YmY0pYbLcVxFu6YTEpE8lKrKKZR7DhoZS9WZzCebLxOg2SMyakiiQaDkemz7a1Gu5IWXc6bZVUpzxm7uRrXs1_Q-_tKo8LvVIJGv0gcM6PBtn5xCm0DTGCqW2u_aHLwTJsIcbj94U9vbOUJzFa_Tlnli9Kb74Ttx8byBnI71EP-7-XbglLNanTcX162VZGSHrYsBepin5o5WcWRy1Xk3ggu35uEVwG3JBRE347Y3D6rF8fW5RP_6mramcfrG2BYKEk6WJoUdEgmZXNFdqUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29347" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIPi3Ot3WcnJPe3R6qwthnqFZesSgQhWqDuq1XVLzBaUk2ZDmCHcLkOgqouSE_znt9LDAK_GsMnyf4yhOkXm81j8WKYnPkoKkOxg53fqL6SGf0Qr0A7wEdhNZG9eNbdBwRj7LHQM4jtin5xace42X7tEDur-6Zg8iPF-OihIp3lvcYF0F2Vwx1rPMzyoMbIozHdhVG9VlcnbfSxVGboxKgQFOWKZKRydnHUbWQeTZYkR6CM6C7THqVAHJX27zm9af4us-vYFx3iLEXuT3Hi0qiHvvytE54tam8GZxaSmrtbExo8ByjmEyYs9qdTk-BVaS5RLl5rBrKQsQbnwAtBINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6ILYtxTDyveZ_ivrJEo4hJC5M-NSsrR9Qgea3D5BFPwXviFl7pBoSSMUyUZRJWO5PuAtyliAJ6YV7BMplDxCFMdaI_Bf1acf0sG-98pdeRHYojXbUDrQ1pgMx9Oqt_yV0Mt0sV_KJCHDYQoAkK4vLPkI2fjtm0mI0KYLnWopNscLq9tCBA7nKMlgvopKE1ryh_MBGFj1-yZMeHzHYc9c9NX3LtiYkCyYee9-C_ko8sp39ox1IEbS0ux53ja4XIvV8jFSZdVtTKXG1fM4Dj9a2xrHZiowZ-oBL1pOVywm47Upnpe2umVx6Ih4n8Ij6a3fKYblXdJ0yqgfCpR0SSsnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جک‌‌گریلیش‌ ستاره‌ سابق منچسترسیتی و فعلی اورتون در کنار پارتنرش؛ اون اوایلی که تازه اومده بود سیتی بیس چاری مست میکرد فوتبالش رو به چوخ داد الان باز بهتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29345" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29344">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odYA-oqOu3VSZ98wVP31XHnxfQK3YWYG5XJ2LQwDY4yO-vfSQDjiGmzH6Ie3zsMJ7kvxXyNWnI-b_k2lzNItq4z8dLSr-EMx3qDniWbNb2ng6PDD8qKE4vwXYP-ogVRiaCPBPEjdegz7a5z2qouL8E50K7Q43A9H_iEWB7IxWP-05j8p1mowvY5BnhF22Yi8xBg11XSqyvZQrqnw2IADE-MJVsLsFbZxatFarx7ify0j5H6gDPFhr_KpHgezmh971NcRacdz8iAlIvV52-2UUCOzikjDK3O-UlScApTMX-AK3qwr1zZNmMogCTvhYEOHU1u4GlFXzVPQsNnOQONpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29344" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuFe7n1tNbAvmNBxFHRaK2_PXvTLgQUqn5lf4f_zFVYYY4Q9pvg3eFas16SND3PaQNe2qwO4X6GQ4ku_ZfKpH5XG42PPbROQ91k_ZqshChZuQff4LTow3l2oHD03Bvr4SWR8K0LZTMAmMDz7aTVyI-tnrM0eKG8dBg9MMbQcHKWHBsTrtVtn1wvd6LnMHS2108Rv5iG7UhCfTJ5oi8kE3oRfDOPB92XU6ES-9TQJjArj0EW8YOfuQlUe4gukPv9UdJwZd-EWdI3vFiZUK8VDRtf7vxf0wKytaeHZ631X4dBcg8QBf451kMXG_U67BvSACXyMviIBV6W2NYQgwMPjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29343" target="_blank">📅 00:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2_9-UBEb4pOar93vmvHfM7U5LtJUzRiQGK-gEVO9kSDEu0kPcMUa04Dl4xuAolrInUaVWS4CBm0eALjmKAJ94UcqdYz_QbRJaYyLcBdBKRHR37dwcPv0MDsy8cVz08VxV-pZdrK3DSM0WIi8TS2mhwOtD0zxLGnnYijxsoDzaJ63ci3uNm0BMlsr8kMwgen7zHlqLoN__eWE9xV_qM5l4FQ4R5GTyyb8BZTA9Dpq5-DPtpiI7v-Ak4Aa3HV0dJrJLmVVyy4qHO2tjLnenJzFAvVJ_Kh6dPKfteY3hYpLvwYPEEFK2xktWLjT2Tko-8qjXWkMpbu0VPgeUrIzj7xEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29342" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b900e940.mp4?token=kRHHbLprySyHDRP-CvT-FpXGPuoA_2uP_MLCEvVZ6iypxdIoq-2ZDV5Grc--Q7CAAzpQIgwrTRGazcZ7XcRSNtEd4sYzIb_Btmp2lRKQ8WtD6ElfjM29RdZTbr2MJW2ngjlBnIizoyQ1aJBKQpBMo3FR-Co-GY5c91_84m-D4r6nMgyFlaBywL77d_srJ36JKIc0JjSiyjJ1m-dRVCHOJzPEwuGgH7qGtqaJ7qjoEGTtum2ibK-ZiEz4wjomEJc0DhM01tTkwf9Xyk1H6124icm-t48_XTyH8NZs01fNRAhdhv8TZEtfgNpq-hATEvgc4KDAewH2P18k_JEG9rXEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b900e940.mp4?token=kRHHbLprySyHDRP-CvT-FpXGPuoA_2uP_MLCEvVZ6iypxdIoq-2ZDV5Grc--Q7CAAzpQIgwrTRGazcZ7XcRSNtEd4sYzIb_Btmp2lRKQ8WtD6ElfjM29RdZTbr2MJW2ngjlBnIizoyQ1aJBKQpBMo3FR-Co-GY5c91_84m-D4r6nMgyFlaBywL77d_srJ36JKIc0JjSiyjJ1m-dRVCHOJzPEwuGgH7qGtqaJ7qjoEGTtum2ibK-ZiEz4wjomEJc0DhM01tTkwf9Xyk1H6124icm-t48_XTyH8NZs01fNRAhdhv8TZEtfgNpq-hATEvgc4KDAewH2P18k_JEG9rXEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29341" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtIVccgzJO7TFRneekJOQDZjjUmu0WdD90ToktTs-KDwbfj9EDco4QWSJ9a7BdeUiB1TaHzfLm0T8BcLO0fxzt-hP3wOzWp266pq3wmpSJvFn4qy-QwXq_KgJMIg8qSgnYWf0YCW8rcefKgrSZtdpE7Wv-kpwj8YCap8LwKKWzADXZM4hjSu4c5GhZDPYNQUQnyb_IIuA9ZuxPX486y-BOKfu2aPnKJ0zAvW_W1s6o71Q95VKtLZoFMFYAeWXYo8aUq7ejDp1y2lGMCHgFdISCtYb7vSxRYvrs0ffl3PmNzuwA18DczU25bNNXetBTBfcxxeDHRcFxTfbE5i6SDpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29340" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29338">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29338" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29337">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29337" target="_blank">📅 22:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29335">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFibL4_wOkF9V30_VjIxA97niEN2Muj7T5yA06AGK6dNtfugfS30e8FFRmG-BfYHbHTQLFu24jE5IkxQmZyCJTxPd5OoztgSlycB1oSEk7bwmy9Pjg8D4GEx_GcWI59Xdjv02KrDsdBqL0HRlDqiiVCSMA9VnPLjRvd9u2wlMPSAs7QqlLOykgCpWKvsnumdf0PqJT8gQwnRxw8x2rfnQg-QfDlM_bddA4hzgUS_K_VbaWh_0ehyU4tlLpbSxUnT1dZEqPmCIAMZBVEiRtt09_77NUTLOaKBinTc-GIc1f2GUqr_5SFycTJMNNzUK_fXSi-OzM0kN6k_KAPYOOr2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWFqWcAPAvf5QU2D-MfIeZk1mt3fd4VRobLHFxeu9p5vcs6q2XDBD68438kjAZrk5BwRHwvIZLHHdso3VgVbQFI9R17nLM152f8R6DTEAMOqWRKWgBvB1F9NTH8gWPWY0QRePV9Ne0auSW6qsKvhCNDN5ADFVOFwdWYX5fltWwQeXKwfzgpkVI55Pr5BrhJtlPGIPJCo8fFT-A3u40AqAAPqZ49hk7cGxRMDpZ5MQKLBIf1xSK2eseVJTrQPdR9z9jb2nPvbR8qDwsdxE66biYO_x7_DS0-6NW5zw38IUEy3B5347YwwnEQj2tpbsDsRslJwq03w658MpoaG8uXLuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29335" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29334">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=ifBAVHnHyRVAs6jf1CEZT82Cqe8d4LdG-Dkdq6A2RRMKKa9EaHf-R5vj4iYr-d6qkBsANdLmGzLZrA9cUMtRF4pZ8ctUmAmRZmTnF5GyO02p0WC22qRjh_L7gJUalgtXUi0m66fLzwj3PtgAMiDE53bSOkBDAYPmPTXCZrROtaE9_V8k0X8VyExwqThQJmnIzIHTelO2UsYxfylaydint6aRrVJ-NJCeq52tvH-lSn4OM-78YVFXnMVOjy6YAi57z1ADPZ131Gnc1IQnjrTDBxRvm5iWS3K40UxlO7cVcMd5LB0pZz44h0A03us2a7afnyDzdMSC-8whRZPKAzbnPoH0ImREHW2Mo0IyIljUfM15vVukp0kFG9AwPKZKq99mIruRNJfZYW0xhEWQievZJVhV_WI6xSquV5ptnj12bhxfgcERKotwlggoAXvvfPLn57WYVwlJ9QOypQiQVcwjpG_veL5vMiu8ggbKQf7F-8LGeWxpznxej-OXQHb3FwcDP6n5maIoSeBWMm2G8CSLuFD-XhYVwK0Zp2whW96d7jzkx6pC_u4Z9BHs6Pe7615uA0vU-_1wjTN2U4BQGuCvyA-BWX0PDAWVUBInnnhYt9rl-yk4QLoM4ogPclZVNvn2NqSlqPSZt10wjioeI_Icf-XG-EqPH8OIc5Z4JvzjJyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=ifBAVHnHyRVAs6jf1CEZT82Cqe8d4LdG-Dkdq6A2RRMKKa9EaHf-R5vj4iYr-d6qkBsANdLmGzLZrA9cUMtRF4pZ8ctUmAmRZmTnF5GyO02p0WC22qRjh_L7gJUalgtXUi0m66fLzwj3PtgAMiDE53bSOkBDAYPmPTXCZrROtaE9_V8k0X8VyExwqThQJmnIzIHTelO2UsYxfylaydint6aRrVJ-NJCeq52tvH-lSn4OM-78YVFXnMVOjy6YAi57z1ADPZ131Gnc1IQnjrTDBxRvm5iWS3K40UxlO7cVcMd5LB0pZz44h0A03us2a7afnyDzdMSC-8whRZPKAzbnPoH0ImREHW2Mo0IyIljUfM15vVukp0kFG9AwPKZKq99mIruRNJfZYW0xhEWQievZJVhV_WI6xSquV5ptnj12bhxfgcERKotwlggoAXvvfPLn57WYVwlJ9QOypQiQVcwjpG_veL5vMiu8ggbKQf7F-8LGeWxpznxej-OXQHb3FwcDP6n5maIoSeBWMm2G8CSLuFD-XhYVwK0Zp2whW96d7jzkx6pC_u4Z9BHs6Pe7615uA0vU-_1wjTN2U4BQGuCvyA-BWX0PDAWVUBInnnhYt9rl-yk4QLoM4ogPclZVNvn2NqSlqPSZt10wjioeI_Icf-XG-EqPH8OIc5Z4JvzjJyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29334" target="_blank">📅 22:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29333">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJETy_o_58av2T9icVchyurzheYnf3lBEB4c8ocDMm5Y21CvD2_Pb3A5qDnBt8JbQw2g1WkVoNd-RSoIvN30s-ftnU5Q2UxyusPMhfnK6o2tSm7qW_LaEwHK9Wom2NYkj_kQFW0UdA0IcMIN8PYLfunvCgn33Ys77Pr3F2XRs1LiRta7R88cLpeJ_Kys3lX8nqOw2R_-yxRZZiZHke4CCsNFxjeaigxeQXtzi4Q0s005a-VIj2FTyPRMa4gaTMP4roA0TCKbYZrXQknigMlJq0M9tc2f9GdMpZf-t2OYfCovoujdEF_50M8U_PZ7usqDvHhGYt9E1KLcGVWgmUkoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایننرمیلان هم امشب بااین ترکیب تهاجمی 352 به مصاف‌رئال‌مادریدمیره. مورینیو هم برای چندمین هفته پیاپی یان‌دیومانده خرید 140 میلیون یورویی کهکشانی هارو نیمکت نشین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29333" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29332">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwhlf_oLRbTkG_r2kBjMvVcekxRmfWCnoKuN9Rb189GiCc5Ff_jRnTvFha0BZLPfAWl9iUTDezs0xOrpRw446jvxOAV3WRx9FXDvyXwCbZY16NjYC7wsdMa6M307jci2EVs4rA-nD7d2gG8b_P_YWwAo8TDKSwH8Ug1IBJ-1plD_K7Z6kV9DNvzS8gMhXym-HaljCB9u5NSZoOi9HSQcEgLjsVPNGqxV_9NDOlmpvf8EJaky9faElwNRkgU74x8EVFFB-komeOQhzfnF3nW_OSbGcAvA8xUPsMYO-eGNAuYGwETzmXiv2mVb__dv-BO34W0OMUcu6ykXHmb_T-vyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29332" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29331">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7v1jh3Hay26EiFHGKzwghUeDGWna4EzO8q0uF9R42nLn3C_iTgRrh3U3bsLKCWGztGcBqF6uO4GaKySV9z8vrK2HgSeys9pQQjvGAF_ycTXx0uJLVpw8zea7M4YDhJkECBGVQ5o-0pIuTsAgWVCTnT64n_s9s29mrV0X1k1LJE1ihCPlMLvOvnWSIHfFF9aUje6Wbt5iNrJmh_JXZeiIYrpOgYLbUZ2WpHgZmxTB6GDPtWef43LaMwKKqsJEddM1gSFmMVztsqIpPOyEu5rmpEg9jqLWKsdVHZ4QBrggeJq8W5k__-zw5Y6VAEuQm6liHBNHW-tjGWUE-nttSqAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
عملکرد تیم دهوک عراق تحت هدایت یحیی گلمحمدی درفصل‌جدید لیگ برتر عراق: 6 مسابقه، 5 تساوی، 1 پیروزی، قرار گرفتن در رتبه هشتم جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29331" target="_blank">📅 21:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29330">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRZnwmb_2X1XeQ6B_wL1htcguFt6R4-C45x4nt0Mfi_cc_4lQtENWRXAIuA6a7dXbQuQN1Ww3TvNw870IOIJJqd3YULk2Jgt5QxbmKzGfMB2EdXwCmTm0fNH5A-K-iDUInFoaVZJRFw9BesaBaIdL3t3N4c82r8Wm_rkueFV8rihrXVHD4bpPW5ZxV3qharnWkD9ue7jktbe5b_HKaHXPpOWr_K7jHkx30dAWrE4ZMbmgtGA7BpACTzvAH7zFcdeLWX0hoROX5NJCrQz5Rim8pX61Yzk4kEJ1oj0kn-CtWN87q5N_YboSjY80P3CaPMdIldg1dpVmCQFFnQn2d2acA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29330" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29329">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la9LsLflzugHgFC29ZaAfSnduy9nK27Cev5WANOybd6N80s3-5lva8c8eJNNsttDIZhMh08XVPj6DcvH1M3HoZu1TcCAJEax-JBTfTpmSYliEtJOKInQgDNUScSNi52rtqD0LYX22xEEn9DBZCnf0z9c79nEp8dXaVe53TIoPbtQB6zHurF0_r-AWXOEaErhERqk7u7YqKYP48hl7VNS5tQYRuvTOLtpQj3caoUEooYyC1i7gkR-obqR-d0SOlz-qKOKxThIEw2RZ9OJ7aPfPD0orHe6nUvNkgjgaxJa2qLTHok145i-8aSjhYek0t1x6eGztzHgjAUY91eQgXBJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ
؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29329" target="_blank">📅 21:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29328">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29328" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29327">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
ویدیویی فوق العاده از دوران درخشان نیمار جونیور فوق‌ستاره سابق تیم ملی برزیل در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29327" target="_blank">📅 20:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29326">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeaK_i7z7gXwpP9Y4R1Qj_LdUepA6984-46Os1nOdzlcxx8PD6gFes23LRoVo4vz3R0BssYu6cCO5LD53w-edi8OQdGvKL5Arkyxc_aTqZa7dKmt9AGcnGMrUFTHUbjtHCc-PWawRT1sKBS1i6_xKVpyrftB6fgN6V2bJ2uhoc4Bz93PXlQsus2OrfqVwnLQGfRCPHeXdCTUpWtENnnMeuD1U3cnq95FbCW8_ymtBnBepi9y_yCzsJdapVpDPQN7Pb57d5xp2h05UnaWAQivGvN7PEyS1XTVAeOg3atdy67g6UWdGNlZ-J75Y0dq4q9ucDO__AZ5USZTpw7wwNP7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
سامان تورانیان مدافع راست استقلال که در اواخر بازی با آلومینیوم مصدوم و تعویض شد امروز درتمرینات گروهی آبی‌ها شرکت کرد و مشکلی برای دیدار پس فردا مقابل پیکان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29326" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29325">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvySAd_lJ4sFNCscU1jXg9Z1iYj7D27i9CiN73utwbcsOxk2fLyW6HyQJ1F4HymZ2hqg9mznP4Ombg4QnpGa4bJb-ko-E0d3WQ-PCSix54CISHlCr2EX8StNL3TL8uhHHX2zjvrXdaqWN0Fcjhn_MeTvf__2t1HzTMe-U4GQ-oN1pVP8Y5_LsoGGZg4h9Kck0m1nEX5jA2qkRtG2UpyHfmhutFTPyXeYl7k8ULhAgAwl__xgPkjpKNlwRW6TlKhiYHhHpw9Q_m6pmQIEFjpHMh8brVNhSCMlOAEAZ3LQoaUinCVXbDk6XldeqPQt3b7GV4-Tf8coSJMhOjz1jx_mZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
در فاصله چهار روز تا دیدار با خیبر؛ محمد مهدی زارع مدافع‌میانی‌جوان‌تیم پرسپولیس در پایان تمرین امروز سرخ‌ها هنگام دوش گرفتن پاش به طرز عجیبی دچار بریدگی شد و حدود هشت بخیه خورد. احتمالا خواسته که موهاش رو بزنه پاش رو بریده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29325" target="_blank">📅 20:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29324">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3bqobfMntnHE_MjHPmUDU2lzW-lsGdNaknSBIA3zRz3dEmDxBUm3ZLm4Cjofb93ebpFuXTENpKbdF-A024-B2UhM9Pga5tL2zrTMYE1d5kD6SXueUEwAeEBz8s0fm7H7paQfa808hnOAmQaEfMM6_h8YmCEw9JwxLPMrR-z-hP9RGbwjA_aIDYzOLxKovjuV5W6jEK4fcXi74HCGvQZNqu5DK9B-pKuH2v_H8ilIUHmNb7ANanvR5xz3HHzimdzSwI2Uk0-8nxgnwBJAlAi77Exn_Y01EdDjiNI2KuSnrqCgZsO0kmPNt4hf4DLVJ0bY2TCyZZq7atG-5MnAcESQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاپایان‌هفته‌ششم‌لیگ‌برتر؛
جواد نکونام، پیروز قربانی و سهراب بختیاری زاده سه سرمربی هستند که تیم‌ هاشون هنوز متحمل شکست نشده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29324" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29323">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgDRXzImh-lDfH6OSHViznzeDwHwBoAarv0AbQRv_0RQ_tYIvJX_VmxdsLUvougAkarcGEiqheq_BcTuv2XrMqipH2Pmfrl9EXzQ5Lsi-IgFkKuvUhAdepQer35EwxAvlp10P5mE0JFt0KPFGd26uO7pbhGJ8agXkeqbx87tRuHFMt4U3W0vYM6mBc_-EQEBKfL18I4lsVuvx06vfDvQlRJDRSTDkQLzBTdkIyxdd6cZpkjgEvGbUrZCOB12EwPxpKT_Gj0BLO7AKbtGd6e8Vy32wuf3vkxn_icwp6GifhQfqpxKNR4ZlwNBys9yQonD3Y9KxFy0Z-0yFcYtRbnJbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29323" target="_blank">📅 19:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29322">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=EK1A2bG8MXmSSL9fGKkqfhdUSmnoUp9VCrk0y6wkgxqip12Xp-WHf2G98wWzV0cDbB7Tv-HYoSsfPo2UWE8vqiGzA4SN_HEZvIYIzmkRT2GVTugJ0dC9rwjQHJM-Nor2VGDJ73mFTe-hy9n_GiwDHbfQBqNJZ-NSktZLBXU-ez8e_EGUI0te3xUrZL2TKjooUGvPCIRaENy16327NJ7EH-sw2OOhaxwbNip6IvJnq_H0p0pXfIpOVUJPSnc5IyuLFaXI2yYYYGuhBIPhHkanG5zdR6emerVVfhYif9G3lpGbxl9EmIrxefLBfdzDBz0j9JkTwUjvPLlVwQup0DnOhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=EK1A2bG8MXmSSL9fGKkqfhdUSmnoUp9VCrk0y6wkgxqip12Xp-WHf2G98wWzV0cDbB7Tv-HYoSsfPo2UWE8vqiGzA4SN_HEZvIYIzmkRT2GVTugJ0dC9rwjQHJM-Nor2VGDJ73mFTe-hy9n_GiwDHbfQBqNJZ-NSktZLBXU-ez8e_EGUI0te3xUrZL2TKjooUGvPCIRaENy16327NJ7EH-sw2OOhaxwbNip6IvJnq_H0p0pXfIpOVUJPSnc5IyuLFaXI2yYYYGuhBIPhHkanG5zdR6emerVVfhYif9G3lpGbxl9EmIrxefLBfdzDBz0j9JkTwUjvPLlVwQup0DnOhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به سه پاس گلی که نادر محمدی روی پرتاب‌های اوت خودثبت‌کرده‌حالارسانه‌های خارجی معتبر جدی جدی‌ دارند او روبه‌آرسنال و میکل‌آرتتاپیشنهاد میدند که‌در ژانویه این بازیکن رو برای توپچی‌ها جذب کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29322" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29321">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIal_3JajKN3obbTIg9afDwqmP7QYr6bemF0kgmSnFU7oqnqzjVZiYXf3jhXoSjHFJMjf9UbAYH03gZdfU8w_buAdlORw2Vd6FwQsl48wYVsuHem9mDRJV7rb8il4n2ejmd5oYgEMgvqpF-iZJsO4PzHj2Fp_rHS0oAE6Dodp8_mQtvXgpKioRQRwcE15cL2V35jzCFREjzXv31iwuCdbAdX8l1bhP4J6BpoUwCNnjurWebssfSlk3zFo2tkjWksEbblFtk3aR9HZphSchKLXkfbCNswowzCzlOA7IX7eduNVBQLoJntdFnDCYxon05pOPrdFxtg_6Z7WOoxGQ20sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29321" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29320">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBnN_tLMyqRr1_JfDqa6yz4J1wFk0QpGB1epwZx3tLTrJj2r8_wOzj0MIedEOim1WrUiTX23opluA0WcXofQP3joFDN0mu-HzKC3gxUBF4GBBo92g30Tpp0eRwfcJOeHuW2iG6l00HVZ6E2QLV6XPjZx49J_8FnkVyNq5cBEEGrYW7wvnwksn9neo9xaF84TOuRX0EIQzJYrMLA-JKe3LUOpKLas9FctvkM8WTS02sL7eSXmy8D56Pkvk4WBJlOua8Enhi5u6Obl0Jq-Y2bWy7dVHhXTIkUir9Uex-rAnfeMPPLt1rKJcabQ6ShIhWZsVSRmO4rboHCI6YEPPHLBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇪🇸
رئال مادرید
🆚
اینتر
🇮🇹
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29320" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29319">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197500367e.mp4?token=GA63JsFfhZXRMRm89ILGQqNRyG2HTYjh4YxH54985oLAYsRZbiaFXmooUqn5GTb2mc-TsBknAJK0jNFndteLd3wbvfaUxPcmVag9eLVEsKVG_HsUGRCybc8mfKMXu7Ztc56WHxsVIsZlLqYkJ1UvGTkv5gVnoVHBgdLPA7mBNsl0hd4_vog38IgFYwzStSqR_ZdNcrIbP9X8S3v3P5SV6-vt4paFq4yB6B0cUd2QCdtZFrsXb9DhdH41H-gBpFwYEAZ-xBaUVjoqsG53P0tRVY_B1JEpfOM8i_sH_KoIQdJBz_K-CRDax9SPKy0yVZzpJbWNgXutMgIJmHOyllfzdgAbW2lfW8d4MlheXl7aQSPCNgdaoFzWVOI-vJwxVKy6HgCHb7h3PdwLG0mxM4TKkwsi-EV-82PhFsfGJiCH1xNXEp77EqQA6JCn0DY5cff12BwxFjiGooITqusnqXcS5qipf0yfeeE2FMyJx-ZxCzFq3zhIhK7i59c0Cuejv-EzaxZukMTbCLxhTxG5vQ1WhT5q20gEt0E6I7nIZvCjq6BK0xzSQNum8Mlc5GLad2dZlrGw-tdBRlRFpJFhAxUBiyU74Vs4At-nwFb3bIFMr-TASrCDfJx5OZT10qZDJEJ27YLtMkRnbAdFTj0glx9NMQTzAwUPWSYiifX_tvP-xUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197500367e.mp4?token=GA63JsFfhZXRMRm89ILGQqNRyG2HTYjh4YxH54985oLAYsRZbiaFXmooUqn5GTb2mc-TsBknAJK0jNFndteLd3wbvfaUxPcmVag9eLVEsKVG_HsUGRCybc8mfKMXu7Ztc56WHxsVIsZlLqYkJ1UvGTkv5gVnoVHBgdLPA7mBNsl0hd4_vog38IgFYwzStSqR_ZdNcrIbP9X8S3v3P5SV6-vt4paFq4yB6B0cUd2QCdtZFrsXb9DhdH41H-gBpFwYEAZ-xBaUVjoqsG53P0tRVY_B1JEpfOM8i_sH_KoIQdJBz_K-CRDax9SPKy0yVZzpJbWNgXutMgIJmHOyllfzdgAbW2lfW8d4MlheXl7aQSPCNgdaoFzWVOI-vJwxVKy6HgCHb7h3PdwLG0mxM4TKkwsi-EV-82PhFsfGJiCH1xNXEp77EqQA6JCn0DY5cff12BwxFjiGooITqusnqXcS5qipf0yfeeE2FMyJx-ZxCzFq3zhIhK7i59c0Cuejv-EzaxZukMTbCLxhTxG5vQ1WhT5q20gEt0E6I7nIZvCjq6BK0xzSQNum8Mlc5GLad2dZlrGw-tdBRlRFpJFhAxUBiyU74Vs4At-nwFb3bIFMr-TASrCDfJx5OZT10qZDJEJ27YLtMkRnbAdFTj0glx9NMQTzAwUPWSYiifX_tvP-xUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29319" target="_blank">📅 19:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29318">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkG13JCGnkzT36Lvjv5wVhEfIbRB5sIkpVwZRikLmPSeCpn8WnZ8tsjZPlHWZk5qSKUUmR5Hhz-gdBzJ72VfMC8kWtUOXMZPLHtNDdgmk9PsnhP4PHeAhOji4T0kh43MepsNIj5ZpeWfXJyiJ9HfD68jfLOk_4e3aM6FfvJ-1pmNjDW0_swwoTATWqZpuDbomcoqzdUHeO4c_cK6uiBy6TvNyowlvwHoBW5KsWa17plh1qpoVohIBgqVBS2gL6BMR9fH96LABCAyTm6tHp5yrzXHlyQu8i-VeEWT8xdACUN6e6fIsKeRvzi0hSE-A7N5-vyZcI2qg_o882Bs0TW9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29318" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29317">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQuRrNCMLXhiz3geWlCuqAcn424IaSg-K-JDcUahTwmtuoty6MD3O6tW3xtUjZclwZysuc0QC7a7DlHhH1HEUAo-kD3EYZumBfGjWo0BK0MYRGeuQIUItIzq5dBSgm-4Pp5c90oTRQ5ELLje4LyAr_XZxnh7fEhqwSNOQrw3Mg-Vt9K1hQ9GGInjHQqoLUjALPKh27p0mok97BY06vgtr8QsQ5A2JVNbzK3npoJBarQ5bkNsywb2iwCEzWiInjG3_dY_EcnsqLTeMeZ1bE1_XuPsGHL0y7EfDZ7xQqf3EsY4MyuzEM8ifSzajvan5oylVICMy2u2vS8U-WVX6Z38GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران بیشترین نامزد کسب جایزه توپ طلا در تاریخ؛ کریس رونالدو در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29317" target="_blank">📅 18:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29316">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=AWZfcWnxnfmlXzShcnO2bby9K0cPAILCfS8krHkS7JwGkMlzspvkK0sHzCFCmpSwC6D0i7S145elu179pzTFh77M521yczNcR-JjzY0pqSg-yrFV-DF8g6_hfD94iHdHdojvl8wEl8iR1HRixNB0JQyBCCPWvE122Hmml_9IdCwzIxg48UdXe7kLCmXKpSGUWrntXupnPUMqwGteMPe_lbounZS-eK_S4LnbbgKTyFasqz9NgahOcH82fycibWJqkj8mSFl6EeEBgY4mB4iu5EC5HRK8dhz_ewhrOXsB2BAW9SPpcxHFoDN5BA7-RjahA7-c97ydGo8HsxN8Q15vEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=AWZfcWnxnfmlXzShcnO2bby9K0cPAILCfS8krHkS7JwGkMlzspvkK0sHzCFCmpSwC6D0i7S145elu179pzTFh77M521yczNcR-JjzY0pqSg-yrFV-DF8g6_hfD94iHdHdojvl8wEl8iR1HRixNB0JQyBCCPWvE122Hmml_9IdCwzIxg48UdXe7kLCmXKpSGUWrntXupnPUMqwGteMPe_lbounZS-eK_S4LnbbgKTyFasqz9NgahOcH82fycibWJqkj8mSFl6EeEBgY4mB4iu5EC5HRK8dhz_ewhrOXsB2BAW9SPpcxHFoDN5BA7-RjahA7-c97ydGo8HsxN8Q15vEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت‌ها پارتنرت رو راضی میکنی که باهات یه مسابقه فوتبال ببینه؛ هیجانش عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29316" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29314">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=ttEV92aTVqEOry7YTP3vzeu4rTYwLKbW3nZPVy0zqC_9A8oWOppkmhKj3jMXgbMVcisq7mf7FY_DPXWUbAJasCWY_FiotywiB7olXa1S4PpiMUr_ZxTLSHVMuE78GGb_04y6_a8wZ5bAx7_hgv8HIzASrVrYj_IG0tpXyeQN8b6QSgo9yWY1SkYONglmZjULuIKhrCGpcuJY49gMfkAi22oJ0MvYxwKkaw4OK7OrjwoOLZU0mi_X1rztMpg8RjthZPPOjmCZhv2v5nJz7k0F4RjUqLdO84qYL6ZJK9yeFeDP-qXh6JrkLn-9BRcD9gnvAhgyq0Tar7ltuJfcLi_hQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=ttEV92aTVqEOry7YTP3vzeu4rTYwLKbW3nZPVy0zqC_9A8oWOppkmhKj3jMXgbMVcisq7mf7FY_DPXWUbAJasCWY_FiotywiB7olXa1S4PpiMUr_ZxTLSHVMuE78GGb_04y6_a8wZ5bAx7_hgv8HIzASrVrYj_IG0tpXyeQN8b6QSgo9yWY1SkYONglmZjULuIKhrCGpcuJY49gMfkAi22oJ0MvYxwKkaw4OK7OrjwoOLZU0mi_X1rztMpg8RjthZPPOjmCZhv2v5nJz7k0F4RjUqLdO84qYL6ZJK9yeFeDP-qXh6JrkLn-9BRcD9gnvAhgyq0Tar7ltuJfcLi_hQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره بارسا:
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29314" target="_blank">📅 17:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29313">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ-fUJOltFRE1ZzCH6v_sG0fZJK9R-oTSkjsYdxbJp2Ea3n9mAF-PwxxO9AklwaN30V5OIKQ_2nPxhnj_MJRxOfScNGC2Sy1Sx_psTBBZujyxZqQaxrTtEIZRsCxYDHZa1U7g-SnhIumY9_RlZiuMkb7bHDjjbkgZb0Pb5FcGzmA2I0d8P58Ns3ZkeeQQFAdWwcmJ5zTHu260hS90zM4f0g7Q2wOXqsAiMeWVkqPZJfnpqaeZ7Zlnq61ysVo0maSqrvk93fAobvAxbmV8kUj6uMHnkZT5GyT38Ha5RPjg7-smUUMl-pLgZfHgO66SKrrJK1nn2jkCCW60Z05Kgwlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29313" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyMM6fq_YQttxFVlvM3fU_a8G1N-QCuaWxcthm6DyjAxvp1TKUTiBYdLVbKR6ubYi7zEbnPtrR0ILSRc5Q-8h39npe9-gl0UgeUqpiLqAfAjoaJdlgca-SFXgE89ArbLZkVY13dXhc-QC0I2j6DzJwWpE-AtCVR44x_7I9R0ebTJ77bK9TQq3z2BIZKTOYJADbLVPGeC57eZvrqGvWyBNRpiMMgHHphL-F83Q_quRaJS3N4fEuYv4mHe0X0OIOQwTCq9ys4D2KaO2BaCJ5fxXLBaKCYsOcK1diOxpzPZG_S0QWOJrlAgLVciawEmLwiy-9KXrgguBw_Uhqgf0Of09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29312" target="_blank">📅 17:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6VLdFhfDGc1i958VuJ6Q7mn_RuEl-TD725_GNSYmNxSkW2c3kAuephZzSCwMg--jhVrjR9bDliRGNU3MI2livdj4tkBwVNBCSZUwHuFB7L27yTcUpAmI0E3oCJZZKyF8Ip2MbSQh7iKYI5jTtkE70tc7j8arnV4CzQX46MKZPlNdbWJu0q4dD2FUju9L4OEjZMgt2ht1TtXtL7Q5WmWPM12gVugFjRtkpy7WRzGA4TJr_luAcv2xTa6I7qcU4j6jm4DqYv8e9zbtoIUnZDrtZUT8l1Bt2hzJamUWedFThH8EIUMsoQP7qzbPqYzQHrQNSf0NMsoXYqr9j-ri4Mqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ اولویت بندی هلدینگ خلیج فارس برای مدیرعاملی تیم‌استقلال مشخص شد: ابتدا علی تاجرنیا، دوم شهاب الدین عزیزی خادم و سوم محمد رجائیان. از بین این 3 تا یکی قطعا بعنوان مدیرعامل جدید آبی پوشان انتخاب و معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29311" target="_blank">📅 16:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29309">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaHbj3VIzKUcu061I5lmCnQtMc2wAhff6yS3LmFIjw_ts5GH1Z-Smxdkcf2koJbBLPXmuPSx0L8JUTVBNRFZ8RX-e_2VaiJLr7LETJ14tQfpko22wD40Eyi6F2PzIJ_AUEHQ79cPCNEFZu9fFrn5bt-NOIQR6EkTi6bCwGjwuLt_ShvefWJGnLgnp_xQf_14G2gmn3XtvT8wV_H56L8pJ-ReLq5YnkgjBcz8a9p9HLlgK2kJE831twjI1JTRvNxzisQJwOojkUABugEKBNWO5qBc6VGd92fU14a4ZYNGGSc38mEKRLTOPY5m7oHjxq4zLO1Vf_luNzcrJesRh-mNUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مادر کوبارسی‌مدافع‌بارسلونا:
اینو حتی خودشم نمیدونه ولی اون هرشب تو خواب حرف میزنه. یه بار رفتم تا ببینم چی‌میگه دیدم داره تو خواب به مارتین میگه خط آفسایدو نگه دار بازیکن تو افساید باسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29309" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29308">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29308" target="_blank">📅 16:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29307">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwfwBRx-eBQYErYtzcjxBLjRfLX5wkk9auzWEJ9KgZZ5w5l-eQNIAJu4G3FH31AuGoIYS78pnWYhlcRwu_uQdeu6fBT056JL8HXLoq15vTTOaGXEVC_roJ4L8YMj-Nzg0q02qV9xM2_LtffURP2pJDVPufpZqk-ArUTS7DEWSvRf8YoP1NpZPwOcQb3mQMDUJ5VvZVZE1B3ykuIW3xNj_RKIAUWFXxCBDeKYu6vBjppRZVoAkr38tr9_5Q2jXKuSHLlAuuXvK44Rnts_EBGxMFF2ACwG4hQt9OZx36Hu5yy9zn4UvsKGMlH-ohaIvKVoqlVbh7S69d5d8H22D_x0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌رقابت‌های لیگ قهرمانان اروپا به‌مناسبت‌شروع‌فصل جدید این مسابقات از امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29307" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29306">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4ue9hE8R9c_Z4KWE3L-wx9uustMx5tpLO7MQrzE3VKg-znAiHyX4L_XZ3yjUGNTO6V7d2gK1UkQDHe9cy4UkNqLgxvPQiTeu7WDeysTdlIjYSJfPw46FaSn3AFW5JC8GNyfzl0UbDP2v0FH4gejgnv-3fygNpuV7LEJHgRxVzwV3bnWw6LCaqULBBfDwU0Ox7w_Lk8CK3VdzeuHlGM-kODZ33rcD3mdRX2hhYKtlYsDkaLVZZ_PDmfn4EWTaLiL-3YfTLnqiGZcCuX-RfD8dyR8cNQk3flnFOt5ldHTqydw-AFcl-KVouXaS8lv0ep-cAu82Ja452zUe5ctEDyLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
👤
به مناسبت شروع فصل جدید چمپیونزلیگ؛ نگاهی بندازیم به‌عملکرد کریس رونالدو بهترین گلزن تاریخ این‌رقابت‌ها با وجود دوری چند ساله از UCL.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29306" target="_blank">📅 15:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29305">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=Qe_bwMUp53M4dvx-gBclKTJH2wT9V0pQVjq-6MoNAgeK1fDQF1XhCc0lCPdNgnnWm3yXh0N49x4PmhPB69A0hiPwDl0mI2uC88YXyjO4zV5kLK3E6qKwwb4OFlDiRY0qF6gQwEBNWFm4JkLZ1t_VZeWv2DfRgHdyFVRkVBXWSbR5bzmF61VYItPlrP7ZsvD200QTxq7JLok1SgRQb1eyXmpkhVSfF4upMyfReQa6ZNPIuS2vqiczBojgqUUdX1Sl07CGVDtZA7Qm5NBbFM7fmRWx7-EVfN1K4iaaMMCymWj1svQRyPR3PGFNpwbt860JkC3ywsn7WHzxBHSonPVTQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=Qe_bwMUp53M4dvx-gBclKTJH2wT9V0pQVjq-6MoNAgeK1fDQF1XhCc0lCPdNgnnWm3yXh0N49x4PmhPB69A0hiPwDl0mI2uC88YXyjO4zV5kLK3E6qKwwb4OFlDiRY0qF6gQwEBNWFm4JkLZ1t_VZeWv2DfRgHdyFVRkVBXWSbR5bzmF61VYItPlrP7ZsvD200QTxq7JLok1SgRQb1eyXmpkhVSfF4upMyfReQa6ZNPIuS2vqiczBojgqUUdX1Sl07CGVDtZA7Qm5NBbFM7fmRWx7-EVfN1K4iaaMMCymWj1svQRyPR3PGFNpwbt860JkC3ywsn7WHzxBHSonPVTQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی‌از لیگ جزیره به لالیگا میای؛ برگای رودری ستاره تازه وارد بارسلونا از سطح بازیکنان والنسیا ریخته؛ پنجاه بار گفت داداش اینا خیلی ضعیفن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29305" target="_blank">📅 15:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29304">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE2FmzMiZ85eE3mTmCmPq-J3FdHBo_XJsaBER0FQFqprNiL5qPl6grE__wVFHhVlz-C3pKAW48b36E9EtYWlPxXf9SC2WJVGD6a-YsQlIzOliegGUZZ6TkaTv1bcxWzpjVU7Ba1YhV-Qcgq8Rf1crCmnfTXWB6OliH7h_z-B2IHmaLrif1HVTJ1r4NWmFmSmfKc5Q5QhUR1M_4N1e9FknCPKxMrP_RRFpq42A3LNbu7sRJdGjifFQbgKlfW5CRftVns6XrNcHMLRNQnubOzRfXnRT87Z35ho0TkWfQPU7uA6mSo-wTW_ZPs5e4IIW4O-vaXbNJmyfd6yepsvV_ttPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمدرضا شایع به این شکل جواب میثاقی رو داد؛ تو خودت مفت‌بری. دیگه‌از مفت بری حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29304" target="_blank">📅 15:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5I1JWOcyjwY8ynsY98F6kMSz-C4y2MDJ4p3RQROJ0Dm1UbvMrD8tkkL0dcDWr_ypWOcH-neRksyMEN7EswTE5KJkA5Jd8htAWFizo6kxA73Vk6o_df00WaGI8NLgl6hLl0dPve7V4n0wgV153URxj_E_T_FcGeINrUrwCxnaVqDJ02jnEaEiod3z5TmpH5-7FSFSyBt-8RzpawQhPrhX3c5S6YnlsMm4gOHBAry0OboeNfHfAstJZOX-QEy4PtgM56bOWUvKVofA6ApPS60mCIgATPuFGl4fxGwkUixnNdc0fOZeTCUv6j10xm8FW_U0XP6318gFN2QOr9P4zEuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29303" target="_blank">📅 14:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29302">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4rQVljD7GHbpgOf3CLpScrOjU3ChhX7WnqQ_Q6G_1l0YaepGfUK4P0BL44hcOuBJkEEU5WyQI10LKXybmCTbAWk3TzpRzYvrBHvW_5Qqp-cQoMy5Iuf87YbQYj7wMBbm_qERw8vBIdbovvr8ObkPly7ckE0iqDT1hspx-N1LKw-IwMF5BDveOWhDZm4O5dW60rTpHCl9BaagScGIPCzgLEbBvcmls9oJyPinvjjCLSlsmPyrdqiXzKhul2MWHp5Tfp2e3GPsug6JJBaZVmDGgIYKddZ_YYQM99Z2WzLZ2bSYMUAWNvMaBBxNnZpM288kQgDsLi2fFWhtR8KnE0KBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29302" target="_blank">📅 14:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29301">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=XajTC4Up48wN9VW9QakFVBfCQTmnbv-NGbrb__APxEcmePWl4BAakOq6xKcOp_0OKvzuZj4dKFYc7jd2hA7u39-WOKfttEUxOPIhDHrU7S9IHH_FEyyTUjuqXUJEz5s4Go5898qnZb3iwxUZUj0thSQ33Hb06DcNHWtzNPG7EjudVXHdgzZXi50MPQJR56UOPVXQrmWFV1kS0nw4sSlQijNA_iAn5oJO7lPYIEZFXZhUSowrh_7CtYzUAsXwzvnuwoPEVwFGGBHXO7Q1gCEQsXWVW8uLh16uHSS0SZno-4KxeA4d21yFPPx1DwuFDx2hC8YRS8wxvDclkxurWdWCfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=XajTC4Up48wN9VW9QakFVBfCQTmnbv-NGbrb__APxEcmePWl4BAakOq6xKcOp_0OKvzuZj4dKFYc7jd2hA7u39-WOKfttEUxOPIhDHrU7S9IHH_FEyyTUjuqXUJEz5s4Go5898qnZb3iwxUZUj0thSQ33Hb06DcNHWtzNPG7EjudVXHdgzZXi50MPQJR56UOPVXQrmWFV1kS0nw4sSlQijNA_iAn5oJO7lPYIEZFXZhUSowrh_7CtYzUAsXwzvnuwoPEVwFGGBHXO7Q1gCEQsXWVW8uLh16uHSS0SZno-4KxeA4d21yFPPx1DwuFDx2hC8YRS8wxvDclkxurWdWCfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
خولیان‌آلوارز
🆚
بارسا؛انتقالی‌که‌بالاخره‌اتفاق خواهد افتاد؛ رسانه‌های اسپانیایی خبر از تلاش آلوارز برای راضی‌کردن مدیران‌تیم‌‌اتلتیکو برای پیوستن او به بارسا در پنجره نقل و انتقالات نیم فصل خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29301" target="_blank">📅 13:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29300">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXSKq7IHbMkAV4DY8EF9ILO8R7TYtJL6X_8I0jpG1665y3ucLwlLaALwCFGssp2pl_pLRX6QCxdnAHdcbjolrmo9L5eA11DGZSocqajKIpOc1HBAhPmScm9p7iVRf8nhXTbG42L977ae-AIm7vdl1aOJqYhGuf9T7IWJLByhWvD-V-7Ewy4vWpEFzabtHhziLB1tCsUoFrwPZo3Ij5ZZMUozVecKsjowgjVeMZTawcFwmU8X0AAu13wcbbLdTjxW13SuVv0llC2-TrOJfH8mpRNwpHAjxXi1qyVJFFrDolCCkY2YErqWTN49de_DJwruDdVa9tByW2I1y6_w4gagvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29300" target="_blank">📅 13:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29298">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYEnj_f4lZbvznNGHgjAwltpKOSsGFK2AbrB3tHiC1pZ0yTM3fM4uEcRPlz_6EY4P9oA1RX4iIivH6UrZKMW7W5gpatL2Hhhxu2svuJLXsfLlJeDQIdnidGSm10SZ9ADKmE7GI3PUfjAORi24j_8YKoaWj5vJyqF7CBN3-33AbTLY96JlFokKBQGSG6zRQnfIbvNn6lrsMANA7zfRRGiCCGCMa4B5zCGtGYADxO3UxJH-xuRBEOU92bpx7-LItGJVYL0i3OMsgioAi2rjwA5y5M4FeoUaAG63EX_ztyfiFeGLjDt2m57cz6Zf2T5ohEM2uUcRZPvql2Ly9pPKD9V7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llccf-MLHiY6bntPPAQRGFhbACk2_F8GS_qq6yYK-FCZcKhFHNZeLtjD2m7yZ7jwoFgpISG3pgiXAWt3Ydx6WG1Rdz4k9KhoUlraedZ8ID-kAh1QcXdQ9SO8dPPV7r74qt2KV1WlGlr8pKrVY0_XC8eZsL9ancgUr3Nur0FKUlNOwPrtZrxH5mT0MgLLzCCE9haJ0hlycZ8Cd7Qybbk6FAeQBClEwT_6WnaYs48X35jWo__eYJj-54vRsjI5DLiAGMqtc3f6E9L2k4shGBr5yDdhXxe6deeDNfaow_ZHoGPbev2U1LdeSoyTRuZJ6C860n1eeQS_4ubZLkdDb6bPcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اسماعیل کارتال امشب در دیداری حیثیتی و با ستاره‌هاش دو بر یک به بشیکتاس باخت. ولاهوویچ که درجریان‌بازی بااشکرینیار مدافع فنر باغچه بارها درگیری داشت دقیقه 73 گل برتری تیمش رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29298" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29297">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNGlNZwXsJCeb25wCxZUhdCaM5L1A1DFeAQEXKfBXmGMCkehRTKW4yu-5OsxrmJ2bQKGru1IQuBckfLGOhj-GF2DGN4olTmj1b0ve-rZ4daybkVJO1ayzWZV2BTsq-b1A-VHoD8v8BqctWnbL4rA6CkF0LtK2ZYtdRvUHfhHQgsDcpy5XCwpDJ8sR6BMqfzZQU3AqrwJHq5-yEnySVoegPlhFZkNooSrc-j7viuEtWJyGf8k-_WV2o9uehXZQ7wgscpUNK_p3xn32S-A3SXAJIYy1rdtzLeQNkFpYRO3fv14IVJetzbxfCZSUpYiVQDHNTIy5O_7zrXE7g9FqmykUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29297" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCBeciohR70Cv-VlnpD356i0V3WVs9uQkTyuAU5-6yB5UUYSZR-Eym602OUQRjmFheglNt0yxDkjJv86utFARNuwgwFKV6RQ1quImiH8TAhM9cedfHSzO0WFMa8FcDAYH8XC715cqn7TEuxLiIjTHVub9s4zeGbNgvZwLabT-9TBfcCbOnbniEaM9XBxdFhRQDxy6wvYoHr6lumCYKppYEMK9lAJQ6erb52LIh5nygmX2cStJhDDxJUbw6WOcWMxt6MuwORu6Hk0lwo_X-tq14eAMyrNnZHWqAXkpW-CnMQ6-kwzPPbS7PDwIMzNxInqbUAFS3oHt-M_oq8JOdjsqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇵🇹
پورتو
🆚
منچستر‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ ‌‌سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29296" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi7r8-L8GnLRAlrSrcOaNglqu5gaXFjjbsvIoa3ohtzf8TO5g45ueJPelMHUHsLrE_zfog4Jn24QNXU1OYRIqmim_N77t-2iIjSZHfMAb4ijogsQ_8dH-5drx_7XilFNbC_6bIe3ZGaXJxWFBRJA50Sc554_oKQ7qHibW7UOKv00AinXXAIJOzmS_oFSflDT__NY8Cl0EpqoSh1sb5eSQ3TOvq38XkTnhQqcQeiF6XbKy7JPvHc_f-W_z0xShpB765VZ7uEhoguY35vH23coCrTHP8GNr_0wLjRIWfyCsSDhhypKmWKrsCPcJGeusukTUbpbTZar_--M62In0BeKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیکو ویلیامز، کول پالمر، لامین یامال دزیره دوئه در کل دوران حرفه‌ایشون؛ یامال هر همشون کوچیک‌‌تره از لحاظ سنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29295" target="_blank">📅 11:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQFSuAVSRihLGojYZ5svDyTIG_yVmJ4VtBSFS261Ep3IpKFcApmy4XdTdrtLNPAka2Nx24MX8EnD6ZSbg-n4tEi0tKFiWqxRQqgXy0LpWx67FTB5cIRpymnyc3cDJ_HWEAiqP-fTXP8nxp6TvLblxWKX2nfJ6Zg1ieKI9jLNzFCfpYM7EEWWyD-Lvjs0lWIAjUh6DtTtEW-ylTiAjem8qv8G3GM_mR2SnP-KQXVK4_0Q1vSnRJMHY0VQ17-WYuTgikVAfvWOGikbZBl30aL2SCYNbej26VweSjr7AfglPsFtQBhqNWSFesF8ksbFgDdkO77NGZRcUnOqIK0k6lkl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29294" target="_blank">📅 10:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6hBgFK8GOWiGNBm5t93gcdb91p8AVos_dN7YzeDwf_QjJdWtlg6wa4_ZrzsvlLkXDbctsgkGdGug0G9Jno_5YFmJ79_7qtPa_vxBsYc96VLLJxrydtloSe46IoSH_EoYqh9l86bvbKusYkONpEXVTIzeZMyHFRVGL5TzvfALN-D2lkfnLo9TKPH5pEY4zmwBzjpQ6HLvmYd-3o4r91Ge6PX_Pe2E-YQxAVafcL9wKS7QtSF4XZc8NuDc92Jd9UMbz9cxA0D7uYHX56DmW6GviuxGxxx8oADGd0pOCnOxmz3DrJfDQenAUbusDMzEe8eemO7YbmCxUDXzK8BhmFKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منظورعادل‌ازاینیکه‌گفت خداداد یه کارایی کرده که فکر میکنه هرکاری کنه کاریش ندارند یعنی این.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29293" target="_blank">📅 10:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9lOY5Sx6u8-4n0PewXId3jZEL7xxPEuX6Mj-1uie7g7yKC30O9X-F823azeIQztPRl_PFZquaitJrzzCBeSqsdLT4AqvWtnw8SCsKGNh8i1AXymXxSBGMRkLgGeyscZapBdgbka7sSOlV395FmryjWafQdHspIKuHIIkVQsYDp_T4P9k6ahVfZs5uG5SDK-Yotq1A5Ykz-EkGvK38yczjhhYPcvMl3ujpoNJuW6Fn0EYc64aWFz0Y7KMDSccB43_d0LgPUk17d_LL8KDkj7t-BWVhxAsDFC1_2_2WYGrbC9_EPmUycAA6JLaHFFPo_3_ruJ8hw2qENs89tOXI-Qvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29292" target="_blank">📅 10:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SguervjsALM5GkIxbm8fzU0K4A8zSe10kFOG0v4m6lE46by6umBCmCfDUyT1LpUfujg9TudZg8pfVdrze3EjgNKrscZDy7Tqz24oDvPFFyK8n3gK_N9A4MA4Nnb1qzOnIE3QX7OXGczgNHykoHg_sFp-u8ZJMlAM02M9k1Eb1o9Y7g_9eFGvBxYhPd8cmVMEaPzxjfpTxuhQ92ET6bwEmh5UQFN3StufwCjSWiwqY3VrySQ5B0h0ULwx5VpIJ9Mfv-3rCa8cKqBhe8BlJRTLdscO2YFRytuSKFRt8EEINpUX4R0xMdLj1ZF7M5oeTV4udsPNtz5mhOUE0_QkM199Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29291" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29290">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQEFRwDtf1p84UZ1xjEM3wNSwYzgB7O47gzyGq5Pn9OS65tq-dCTbS5FtJeDkMRZneVl9YzWgOA3sn5rGP43tW6rNycl_upQSlXMuzG0GU7uvTkk8Lajp7Yc_C90SX9Sk8LUk8PQ7GA-nQrIVzvuMUxaC6568Zo501CJloKJEgRJQxbwETF-tP21DyDyBCb398XVvWUyZ7ql3p3U1KfSo2ml-WSn7YaE0ygSZdQJh9zcSezlIVeiOpTzh0vksz7iQ0nCsxRCQne0zdkseyOXII-6ezZ215oIUqU4QoHiog1COVgVHgng42JTdWZqHdnVH1eul_DqLkv1wxxU_keaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29290" target="_blank">📅 09:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29289">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره جوان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29289" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29287">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve8LAjJnP6oIBrs7AoByL4lNMhQ_0OFLkxsVhhdYUS8dGTHJi3UzxtvLuJQI_5jP5z8r-rbI8KjTCqPm4q6AVUnr6R3JZEvn62ZPgfEmiw7dgnaiuUI7DZRjUOJdEwrHrqjmvTNF3N5yqIlkr17oJS8Jt_BFEG5SjjtE2xozHmp9RmYYZWm0vf0JjVynIJyB4dYGe71PDvE0324zCPl8lz2XB9WfaWZixMwOf0d_3enx4DUrUmAGxUjieK30OHEzVcCdGoScW-ZHPOLU9p85OlRY74cJXvvKmtqWUw38GnRzP_avK7Y8GPm83iyJJKIdd0gYjAVAKVDSnNKX4uI4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ آغاز فصل جدید UCL با میزبانی کهکشانی‌های‌مادرید از تیم سابق آقای خاص!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29287" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29286">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhBKcanJv5feUnDVc1uMTvofy-uTRBiCEfr0eDjn9wwqezteH5-wBCxn0T4PZNBN0FEhBYGYPeXNlQcnfL_deMfriHZt_0T3dlHSEYCIX3WxwWzUYS4IMjLFEUkjJL1wdwLuyrejKSRBUf7rR3v_hZtfNp8Gaa_6RSlPzsaPDYWKCOw8bUF-L2ls7hZEHp1Gyq_AzPPVThz7qJDprHMtgAxECPeqUJ2zpmtHc6-1-B3VkHkyrJsaMcO0pnBm3H7XA3ig0CVig8o4Uze3FViDXskXLckbiMT6V4SE4ImlWUOVZs088cRXsCdHElQBK3dBJUW6P0TLwzlgPx4zegSvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌ارزشمند پرسپولیسی‌ ها مقابل ذوب‌آهن در پایان هفته ششم لیگ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29286" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29285">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2eCtTFJbET-38puurlExo3UeIqyCfXz7-2FYp_5w7PQ3KNoVx4ZTjdtRI1YxcG4O79CLt6RJRczZzIpiZZPuFM8T9n19JzOYFK5ieXLvIrBxaae0LFXKLrox0oc2hF3zV-Y1fnhwmFDkHZYMzfRdHZjwsknKdqolnz1YgvOcbaH-kfO0KWKpI-WXWdrQ2E0796MnFjbOB_yiTwr0EBHYo4h-Xh-fLKeK4L3GOAgxCAB3BGPmf8YWNsRJCkUH3DmZS9A4Z4EqzzT7YbjifOx-F9Rt_2zLOIvkatlJAUop_oaDWMjB7x3s4Z7befclfWzZsW2vDt7XbhN3Dc8z9mFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه پرسپولیس بزودی‌جلسه‌ای رو بانماینده دنیل گرا برای فسخ توافقی قرارداد این بازیکن برگزار خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29285" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ1N6hqhmU9f4zjgFTY3187yv_Jg57OetvA4T9kklI94PzKtabUd6DAhFXJgp0gj0c_Yr7S6XuwHWuQ1Dr0X3_JriPXit5E0XS_0ra49_ZAOPl5nN4TO4MTXrrLt3BJqWHGSm4U0NsLmj2sjQV7K6wzanXrOrLOwrxaYGRCKgTH4kg2T4D2hQBSe6TTgh64LjQ4gF0LLU7oyTUJHugODK0f8n6AcfXvT8IwBKaz-sgZnRNqCWpCZNEqhv2pIRnYguw6BcJrAAfME2fKW7ThxJBMBLLwm1UboRauOowyePIjl5sH3pZ2hkn0WCZn7XQZOPw4IT_3_wSiF0GTCRctQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29284" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29283">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=TyQGyhp8zqkLRPhczdyuGdB5fXm6et0qlrZ7ZHf50_bUxWRBi2djEE3oaDZwXsywWnJ2QpVW0p8tz_qeza6NR936N_k7wbik8yJn_tLYQsFiKeN5yUKdnzn_p9NSLvhm378ADJulfxCtouuENImEIaTaHpj_xdu_vV5fMroiXRZdQmaS0jOr31wjZJwEmB-cB8TxnTHxt3Z3jaXBjuFYaxnjrzAv-ozQ9c7MuMOthE3O7mf2snohfD0nYKRoLsiqnLyVH6BWrsVWR2y8QAx9bB-gsVa_cpqCzs94bcMvTB_0uc0Znh3iyWKsqhTwXDIJmxEuPIYEzQsbhevERSX31Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=TyQGyhp8zqkLRPhczdyuGdB5fXm6et0qlrZ7ZHf50_bUxWRBi2djEE3oaDZwXsywWnJ2QpVW0p8tz_qeza6NR936N_k7wbik8yJn_tLYQsFiKeN5yUKdnzn_p9NSLvhm378ADJulfxCtouuENImEIaTaHpj_xdu_vV5fMroiXRZdQmaS0jOr31wjZJwEmB-cB8TxnTHxt3Z3jaXBjuFYaxnjrzAv-ozQ9c7MuMOthE3O7mf2snohfD0nYKRoLsiqnLyVH6BWrsVWR2y8QAx9bB-gsVa_cpqCzs94bcMvTB_0uc0Znh3iyWKsqhTwXDIJmxEuPIYEzQsbhevERSX31Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو رواصلا ازدست ندید؛ خنده‌های عادل وقتی عضو هیات‌مدیره‌تراکتور کلمه "بی ناموس" رو به زبان میاره عالیه. تلاش کرد سانسورش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29283" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29281">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=VsoHxF4oc1ZGJzmPqYkLmG52Wyy7-OS2yj1a_ikY3uVaSXjhK7Vkd4jg-WG6SHjFylIOo-KzXmrINFqzacq5MMmbzUdzEuIMncXq5SNYQ5uoQjDH_H6M-pTJTW-S5QpmQ9_AqU-MiRtNF_uQDbnKQwJDeA-rBSjsLXWOuX6HybU-6wqPDKwZckbPhV-R0lw8UmX7jjZGEOlaoHWRcOkS7o5KYq4ithhGOZ2HkhblRccZB_PaIM37KlTS6-BznqIXzjDH14DKpoKsOH7-ySjR0HR0zgJsOLhZMFbee89grcn-F9YVHB1VG3bBRUmMADX0OuradhZ2Gan6J1OSZCQT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=VsoHxF4oc1ZGJzmPqYkLmG52Wyy7-OS2yj1a_ikY3uVaSXjhK7Vkd4jg-WG6SHjFylIOo-KzXmrINFqzacq5MMmbzUdzEuIMncXq5SNYQ5uoQjDH_H6M-pTJTW-S5QpmQ9_AqU-MiRtNF_uQDbnKQwJDeA-rBSjsLXWOuX6HybU-6wqPDKwZckbPhV-R0lw8UmX7jjZGEOlaoHWRcOkS7o5KYq4ithhGOZ2HkhblRccZB_PaIM37KlTS6-BznqIXzjDH14DKpoKsOH7-ySjR0HR0zgJsOLhZMFbee89grcn-F9YVHB1VG3bBRUmMADX0OuradhZ2Gan6J1OSZCQT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
کیلیان‌امباپه ستاره رئال‌مادرید:
من بهترین بازیکن دنیام؛ و با اتفاقاتی که این تابستون رقم زدم، حس میکنم امسال سال خوبیه برای بردن توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29281" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29280">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932bc654da.mp4?token=S9lRbxZrGAhClRcc0UJekKgo7HGKlgYwKGh9f5fTX_B80I1axNQhCR-puH8623i3hbsUs4jBs36KSUR_6iQRNVNLxEnBckznr26FmRzdFqYftPC6YHDq6YtdvvHDCXvrUeXosn5zCOFALVppfS1i8NsHnSEwMhBgsMdowezYVIpnCZmf2-5zm2rQIq7rqyDi9FdlPNF9kEH6lPblJGMMd06NKQJyXcoIc4mzQPD0k2cu8I40bB6I1z0Iz-YJ3A9PPuM7E-nW8-ZHO6eUyg9dH9hTCwMkIV73Ivu_QVaH8zKJ5qluAvaIBKOy4xgUVCGrtGAH1UeK6dhBtTzycMWYgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932bc654da.mp4?token=S9lRbxZrGAhClRcc0UJekKgo7HGKlgYwKGh9f5fTX_B80I1axNQhCR-puH8623i3hbsUs4jBs36KSUR_6iQRNVNLxEnBckznr26FmRzdFqYftPC6YHDq6YtdvvHDCXvrUeXosn5zCOFALVppfS1i8NsHnSEwMhBgsMdowezYVIpnCZmf2-5zm2rQIq7rqyDi9FdlPNF9kEH6lPblJGMMd06NKQJyXcoIc4mzQPD0k2cu8I40bB6I1z0Iz-YJ3A9PPuM7E-nW8-ZHO6eUyg9dH9hTCwMkIV73Ivu_QVaH8zKJ5qluAvaIBKOy4xgUVCGrtGAH1UeK6dhBtTzycMWYgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌دردهایی‌که‌ بافوتبال‌فراموش‌کردیم؛ ویدیویی زیبا ببینیم از یکی از زمین‌های خاکی فوتبال ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29280" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29279">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO3_2J2Ru4ZuuVszhlisczZSFN-RqRgsJ4VSDbYleutj5d1SMYUboPjoXkOnS1Kj5hWquL1TYs5LGZAR9JV5uLELUgzGNhau0a6WE8C7VmHHV8vm1dRrtA9OdurA91oOJw9Kiz4bXwgBpoMQejllm23tQ9sMCEyA0HVkN9F9xlWkaj-YpCri0UizNh1ePrmOKAAfk-wd7GtB416EKYmfOf8Zi4Z3QqwOQFWMN9nGdA-zT5mqx2IJHirRuETqCwhbdb_VQerurtmuWySh5mMl94MOqTPejTD4i0cpTTFbvnnLnUghphNIFnA_VEyCe5xt3L5wwvR7q7lNflPN5HSHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه نرخ بنزین در جایگاه سوخت به این شکله که در تصویر مشاهده میکنید؛ نرخ سوم که بنزین لیتری 10 هزار تومانه از 12 امشب اعمال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29279" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29278">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFmyWwB8lLfJ3LHJWhRCIgG4TF0Qigug8K8uD3uIbfDhHckTJxC9C7KSLRjP-I7mlqSVZy57jzl3qqNWm4OHVkCyY90-eeEvpgf2leqAPxnlxheWU4q0Km51DBM79JdxDxaTicIuj0YNaX7DOkBgBWU5AqhgDzg7jxVwEl-MK5XjSsFI865gs6YZ3tYBAOz_tbJQ8B2d0ep4JAv-qoFcK_Q3FTvHZxFhWnJZKaJ7qZd9VjUVIM5CrCCSiuegW28aNBZsFP2aE6f56UUevreZ_5pjfBJ5RyugXK6CL1gtkf94U4_Rkh_Vu-BuUVlko9yPuOPsGpQHJFR4uhBvQVkK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29278" target="_blank">📅 23:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29277">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqtGrS129DAr_POuO8DEHo0DB9jaRW3Ukyic1oMfKJ8Xv6YB8IxIEflYCwjvNNQoo8RL8UxPwD00LkwAJXIuj_Y76_KvvxfRNfBBkjACHPPF42ZNjRNUk-3TiZIXuWPjra2peYzPwSrBkn74558FwIvWhk9LMvxfd_mx3zvBTsKUIqprGt_wJ9tQuC-xE-PRz-l826zJzxZX-aTpqQbYgK3Gz2AdD8XoeuILj34qtQCbX1oMfpQJedRszF1KfdDLKyCKVUsqb0lX6u0x8wW_q2W2DfIU805xgMGlw564D18jJvEr_DMH_lox2gkvJ-Qt3dV6aBt-qEHKdfYmH0w6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛
الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود اما امشب کلین شیت شیرین کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29277" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=Eh4yULq1Vdanf-8wyroEpZbGfjXGmekvBirHp-y6Vgr6h8q5gcIV-N3By_5fnXfkwSDZnKPeQwYivIrnb2FI_qdMcMRNbRR_yJU-IccNTdyM3fRztouVdkmzwKAg6AxZCPr-zJFy7s3gzX4XJr0V4LsNdn3MpeNZK37SANUL0HDrVaVRySEresp-4RhkAYnnGS2A1WFhb_RQoI43BrxLu8WiEMkGfkn8hRlbZQWMVl-pz0COTdtri0hfKOv30u6RvO08-a2_N_Qc7dk6RQxzTdMNEChxLhYIt4eULXxTVeo91tOprDJQIPyD-7LpT7r_PhP3yANM4TXTkBMbptJITA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=Eh4yULq1Vdanf-8wyroEpZbGfjXGmekvBirHp-y6Vgr6h8q5gcIV-N3By_5fnXfkwSDZnKPeQwYivIrnb2FI_qdMcMRNbRR_yJU-IccNTdyM3fRztouVdkmzwKAg6AxZCPr-zJFy7s3gzX4XJr0V4LsNdn3MpeNZK37SANUL0HDrVaVRySEresp-4RhkAYnnGS2A1WFhb_RQoI43BrxLu8WiEMkGfkn8hRlbZQWMVl-pz0COTdtri0hfKOv30u6RvO08-a2_N_Qc7dk6RQxzTdMNEChxLhYIt4eULXxTVeo91tOprDJQIPyD-7LpT7r_PhP3yANM4TXTkBMbptJITA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی هیات‌مدیره‌باشگاه‌تراکتور در گفتگو با عادل: عالیشاه به خداداد‌نگاه‌کرده و گفته خفه شو بی ناموس. فحاشی رو بازیکن گل گهر شروع کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29276" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=KpFsnvU_8yd0HmB_r6VAB6JZPAiA-JszS6_-T8r-akuGQnflHFoHfrV6ktPxx-vt-9qNGEu8HOZwqtS2Wkli93R-o1ao4BBvJmhvmGsHUnFWH1o7Qm20D6VXdNhO28KmLoOMzPVRy1LZm8qYKgOdeZv03kT3AzyPiaf46ah7QDjmDFee8odc5HuEgQt7Wmch7Ka2VJLo_rhaNXg8kGMsOCYcXEbLqIfrh8n4NwPYg4INZrJ9W0ynL0NYuIKQjqaltFfhBewonHZNpSU-jqnT0qBWq7ghnHqdljeMeGyGzTxerc8gCbBxzdwIeMnz-Bny43N0sSbJe8v-xXpySLJdcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=KpFsnvU_8yd0HmB_r6VAB6JZPAiA-JszS6_-T8r-akuGQnflHFoHfrV6ktPxx-vt-9qNGEu8HOZwqtS2Wkli93R-o1ao4BBvJmhvmGsHUnFWH1o7Qm20D6VXdNhO28KmLoOMzPVRy1LZm8qYKgOdeZv03kT3AzyPiaf46ah7QDjmDFee8odc5HuEgQt7Wmch7Ka2VJLo_rhaNXg8kGMsOCYcXEbLqIfrh8n4NwPYg4INZrJ9W0ynL0NYuIKQjqaltFfhBewonHZNpSU-jqnT0qBWq7ghnHqdljeMeGyGzTxerc8gCbBxzdwIeMnz-Bny43N0sSbJe8v-xXpySLJdcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29275" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29274">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvN50hu7IYb-HM2moPM0rPBHpB_b70IDkIRWjacq0TSQdE_EwkzOV9ZF5LZmjEBZVPNTW-lqRjNZGZNVE2kwzoX9NkFg-G8MJC71sm-9oEqZKIzIip8F1Z-F5dOln_WpRc-7y6USSwgoifk8DromxZYdaVlgmp06sZB_1DC2KvVcdf5Per0XgbzMzStD0aawF-wxNA7PoiJC4rHhFPF1LI_gdJBzY-RuKuUtriPP5WVWr_8O2-O3KCAUCu_sEsh6U2UhMrZWLl-iZoDwk6CkvlHvqCPVpHILIhM-PYRTktWlOoMYVW9EpJdzNH1AtN5PKJrOHYAf0dqfuAnYvnDFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارشبکه DAZN ایتالیا که روی برد اینتر در بازی با ناپولی شرط بسته بود و 650 هزار دلار برده بود. پست‌برگ‌ریزون ریپلای شده هم حتما بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29274" target="_blank">📅 22:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29273">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEzaRcaY6fzp06fVPKgT9htes91dS3PfGvGEc7ynQAvzCWzOvxI-RdiWE-tMysT1gItSUaOZBcx0gonFVSP3uPPK9f5kPMBpzAXI-xkr0tEGR-M8LujN0CmX1i9ASn9XrC1e0sP-hiOAKfLQ1L6wYws8EmlbqFBv22gVwNE0hL1vDz7iXX74mksi3ulwWwgoAakWt49uEnYnzzm0tD4L5ASt6bzy5w__lMy9IbJDKxp3rFAu3WFaI1llr77Xc2DKIhI0NssUaE8Vj_xxT-nvca6-bPT-W3snhid0Lab6lIlA_p-jTGUNZee4eQXm5maltl6UJJOvPLstQQZ-x8qmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29273" target="_blank">📅 22:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29272">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📹
خلاصه دیدار امشب دو تیم پرسپولیس
🆚
ذوب آهن در هفته ششم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29272" target="_blank">📅 22:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvl1iq6rumzCOZ-IP3ZKAH4zIP9-ekgTzDl0qEE74f_hL4P0jr749ijv5Kd4K-Ao237NQmAISa-2NTOOx7d3JnFyGlXPOMDtpboyRmh0SdODiAHnIKLzjUxDmz6BcTGOgDblbFdrPPxjkOtCGSbwI64l7hLh_r4OWEaJ1J1bw7bNqWPPhxU1OM2Cddj40LcpmPlGdp0XoUcXXLX7AyH5orbQ_1Oq8yC66QWsVx6vjDH3qRkAX0EYlL0Fehn9886EcELTZJnJmN1EZiuBuq8moAWtG92CvlKp2GW_bVEoZdfDeOBFlEBhexqmkWJw3sUQC6QdfwbpqMjs_D10nlxYeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VohslEX9TwSoLmh3JA0St4SxIlqTz6E_pm3rgINaaFSuUj9nkRe4ofpGkg9EVoiTziMAkExJ6quAAY-PP0rgLwP-aQ64ubmZkNuF690pFXcvYtwN8M0MyfapXLQkX2IGbDbzPZCUuFgbW0QsSiwGSDsrRWOUddAnGl-FtxIA28UQY-4i3kr6dWZk1ZdmHVaDacbagZvWTLAaT6YLY26_fAxhyt8eN9fXvLvrS1X2llSZkR0Q4XoFnlIIYS6RwatMs9b-lZxU-OdzMSVIIFhIVBtG06ynmHkFdAE0iF5uTH5WL29ZiQz8tHydUQNaT7z22pA9BAgiOw011sUdd8Js0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29270" target="_blank">📅 22:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7XvaN7AtJUa7p3uBTLqv_25ofNuLH0L9s-e8qmdvejKNxEdYl0ZKoFg59X3SH1PujK0XQvxZjaX5HBVeme0Pewj5ooAHPobsLh0Ka_Z-Ey8p9S3s0iyiBtTqLcI7FvDKLkkVVADPJ_CmKJ1LqTrriQYuok__ATmwjnxJ76STq9eATgyvGlZSO3d0-wSJ4ntENtP35e02K66reGpNr2CNMKJ8emjrCdmA5AGluK3p_3PObj9rbPJp9SfcHo9m18Tf54e8SHwTlU8HGnqku6IJUx--_QCsZ-4Oog4BSdibd1Fuxch3xSQMQy6LM4VQwvNgia4Vw5fuOBj8rYuIrJQwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHdynK5RzYZ6BzjFbskUM8FMSgE14WR3ZHUynaCsroa50m4bjs8mpGWDz3IS6Jj51dhzVxYAPok9CXg6XuKFfm0Fz7hO0EUAZeIirU28_nVWm1RsWnLcl-XZKTCQGfXr4QJkTDzMFG67Obyw0apnQjCP4An1wFmvnjDJBiQ8_02Ok61SNIdt9yGFaw8aLZtLrcHegggs2IuXa1hjP_KgC2pXU9elP9XL8VdmAIqOi9YxN8iec0q4oUM4aGzzS4p52a9JA38jyxkkYmv5PWWmDKdMU-wjChEVWvp3ad1jBITNsvNzXx7NiQeJa-yGrj01FPpDEOeYM_3UBrZaXYA7Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
🔴
بانوان هوادار تیم فوتبال پرسپولیس در جریان بازی امشب سرخ‌ها مقابل ذوب آهن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29268" target="_blank">📅 22:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=u9h7c5Vr8xWL76sRzlFe_nUK7LRmU6mHbbAfjgcvCGcF8CpeW2-THw5Im5lzwDd4Hm8gD3y-jVy0Re2pIS8QG8_ySeEDmyJuFiVd8rjV-ukmm__RYX9VpYOxEtAYyxdcXC98RD7POv5REWQKOdue9x9BDdrKGKX5MQ1RJ_2G5no0aCRfGyw3ZkJf5FsKe6lEZxUEwljpZe8pFQ-PClunN3MuEMicZGaGlPUTlQ0jvrYRDoqIn6QXv1xWjjy-k61QnIop6DXSYa_4jE1nHZUYxWYma2eVIVTShrWfeyhqZFu_K3eZcDThaSh7MEhsaryWQc1rxqNDNwhlZGIRW9fmb18erJVnGftqX8XOLCPGPnlq8h7gB2HFajxVpbqsO_MpVQ7HhI1IMjjG9lYQw_zlB5fjZ22KzgtgIcTco-R5f8b9NiUS-7LpjzjfwYJAtvLdJTQ6Hl4ENwnxk_XmIFAog9AMiioaqClx2DrAa1Fej3sCJPkphYzaM34xgeN5nqei49Iqx10YNQK3EmvVv7320-lSTrmUkR_qg1n5QSUjCzUqAB16teYaAkm70AlHSlQQB6Bm3WsWAxP-nSz6s-y_ojZGalfSjQMvTnpqzHSKFt2RU7-aWq71IIway7oK3URPEU4ZnhE4xayY2aUuhVWcGOaroYfl8VBC56EE2KY424A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=u9h7c5Vr8xWL76sRzlFe_nUK7LRmU6mHbbAfjgcvCGcF8CpeW2-THw5Im5lzwDd4Hm8gD3y-jVy0Re2pIS8QG8_ySeEDmyJuFiVd8rjV-ukmm__RYX9VpYOxEtAYyxdcXC98RD7POv5REWQKOdue9x9BDdrKGKX5MQ1RJ_2G5no0aCRfGyw3ZkJf5FsKe6lEZxUEwljpZe8pFQ-PClunN3MuEMicZGaGlPUTlQ0jvrYRDoqIn6QXv1xWjjy-k61QnIop6DXSYa_4jE1nHZUYxWYma2eVIVTShrWfeyhqZFu_K3eZcDThaSh7MEhsaryWQc1rxqNDNwhlZGIRW9fmb18erJVnGftqX8XOLCPGPnlq8h7gB2HFajxVpbqsO_MpVQ7HhI1IMjjG9lYQw_zlB5fjZ22KzgtgIcTco-R5f8b9NiUS-7LpjzjfwYJAtvLdJTQ6Hl4ENwnxk_XmIFAog9AMiioaqClx2DrAa1Fej3sCJPkphYzaM34xgeN5nqei49Iqx10YNQK3EmvVv7320-lSTrmUkR_qg1n5QSUjCzUqAB16teYaAkm70AlHSlQQB6Bm3WsWAxP-nSz6s-y_ojZGalfSjQMvTnpqzHSKFt2RU7-aWq71IIway7oK3URPEU4ZnhE4xayY2aUuhVWcGOaroYfl8VBC56EE2KY424A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اتفاق‌عجیب‌پس‌از پایان بازی امشب دو تیم ذوب آهن و پرسپولیس؛ اعضای تیم ذوب آهن به خطا روی بازیکن خود درمحوطه‌جریمه‌تیم پرسپولیس معترض شدند و VARهم‌صحنه را چک کرد اما داور در نهایت این اعتراض را نپذیرفت و به رختکن رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29267" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS3EAb-seO7ERRZ6nNTmpmGk1hS38ljbloW-Ck5SAQRsh-9r8rWqNqX6J1b3Po_NHDML90_IpBZ4cHxiaQHCBQ4WNcEOU6y8EWZCyZn6VQMfkGRu18h_rBpfWdYDmPvxXUQIHAJQpB8BeEf7WJ-a3Y9NtYudom3drPWQmmsO-gFwAxss5zzYDJmV8XkIdlnwwg1K1OJAbnrgu5FEjMj2MTTPuQMPozHDoAWnoM2QOrqZDuiiIWISI48Wtzm1HKMlXoEp7yI5lQj6m9smI_o14nWkofUPnNhCuz-4X6PSDhOMB4g093PCE-XTubHQSkGVhD-6oc9Y2udA1jdc3ZhAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌پسر ۱۷ ساله اهل مکزیک بوده و بعدِ اینکه دوست‌دخترش گردنش را مکید، جان باخته. شدت مکش به حدی بوده که باعث تشکیل لخته خون دریکی از رگ‌های گردنش‌شده‌ست. این لخته به سمت مغز حرکت‌کرده و باعث‌سکته‌مغزی‌شدید شده و پسر تنها چند ساعت بعد جان خود…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29266" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH1Fccq8sYL46KCPq_FlRFs431-8CG22mbh-ZY8cOcxHMN1_u5yKVX-qVNX0dSXwEnDSoAKaG0fXghuJm3bO7h7qzDPgf4cWBkmuBoB_Fie8bKsNS7Zj1Zowu9vTDsVfifVR42fG3MpnZIHM8ePtVmZwuWVrP5divaNPbPtVt0ldQ266dyBvwQDYiRZ2fu9w2XyxWorC1qIQXdREWuBAd7jJbErXpLTV2LLveGJd74sNAMBPfBl28FqTwXM5WZjkbC-aoypkCg6An3J5Tcjl-1nSws_Tf8ZOAr-ZHuTjJcFaMNzaXyZzLAmJTM_yLgM91zMb02bu_DiT0FLt1w6jpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک کونده هافبک‌شانزده ساله لیورپول با عقد قراردادی تا سال 2033 به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29265" target="_blank">📅 21:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=ebbNc9faGZLKKloZBes1wkGNhGnt-dj04hD9GU0sTA9P_UzXc_7XntBxHE7lsOWyS3Bm2v03dz72ew-tPJNNl_dKK3JMlnmYgZWg6jI1A_TBqRlEWtKdVooJ4Lo036l9twPK3wG37N7iboPG-dXRpXa-F1WlC38GsyW6pT-S0TBzKxhaJsZMTNlawuC8OAAgg6MZbnuItsOLZicrnoT9EP5GWn-3ogR-OtP0LXmjej35_WbosXjsbtYPBlT3MySN8exqpA0kuCqax8MfKBTNQ7uidAXdERABGEHPOy5ymtOUKWnu_o8GbHybRZUK_qv1Ce-QoUN1myF1MxdEIhOYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=ebbNc9faGZLKKloZBes1wkGNhGnt-dj04hD9GU0sTA9P_UzXc_7XntBxHE7lsOWyS3Bm2v03dz72ew-tPJNNl_dKK3JMlnmYgZWg6jI1A_TBqRlEWtKdVooJ4Lo036l9twPK3wG37N7iboPG-dXRpXa-F1WlC38GsyW6pT-S0TBzKxhaJsZMTNlawuC8OAAgg6MZbnuItsOLZicrnoT9EP5GWn-3ogR-OtP0LXmjej35_WbosXjsbtYPBlT3MySN8exqpA0kuCqax8MfKBTNQ7uidAXdERABGEHPOy5ymtOUKWnu_o8GbHybRZUK_qv1Ce-QoUN1myF1MxdEIhOYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29264" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m68tilN-LDWTRwqENekhjrLZTMIK5Lf88yQKYtR0AAHwTWKVJ_Feh7isFww0O1iXitfvQQtyTah1lIguokrxazbAN8K62f4XwMMnLD7EUX1n7GY_G1LutUnqonjkOWz6lCOIXs-8p_RrFXMOt2fqSMziydaD_AtbWoIHnPfhD4GJc-Qo24kJdSpozaclh-XHiVYNd9zR9vx8RSmFxsnRndxKZ79Q6pjQWPNJYgTv5Su0A2hNXW2Db12hAapal8av_5uWB7Pd2FD1PN0SnO6Dit-EINU7UBH6Ppl5Dm5F96P6i9iWwwwIeBo5AXS-TpiIDdQB0tkH3Fv9BJXjpZXm9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29263" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg2Zq6vz6KQBWBTzaDlLXUzQSVtWx_GimPAaAmfwzYBEIdN5MMPKgTtSjI45EoURz5buSOmVwYJhsk9rBp-QsMHD8jX3C_0Rqoccbwd9ZjHUvXblx5iARIuopr428YDQNKcJzZmQGes7HkkFvTcMbePgVB_Pr4XpW0Adl3gtkQyrP5SmQJJtb71Y4NCAlpetWCpx_lm7D84xgiDZhf4iyapfWII23msHGaaDzygxSaMbGUCJOAM-zW_Vov03xIylWXLWxtzfbqexRr1vtchMh0CwmdAM6caxG-Buowbw4jSRK80BYgwAGJgevmbkUzupIzKWZiDlPwpDct5SJIWKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29262" target="_blank">📅 20:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29261">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=TwiWftWX6kh0tolPm_bZBbQBA7qKIjHU9KgLTN2ZfP3UfTOvxQ8w_77DzJSrYx6ym8P51xeJE61ecshaPi4AnnwSF6RCsY4pcI8IAV6lRcp15c46Mi9S993Qmokj9FllM_vDkJVv8AwnNa1eTIuuGwJpZOews09-pnXM4Lb9wCVI60hhK9Vw7rbSDgQRt4CF4kc8OdR9MSBskKKv78_FDpPnMrcsZACcX2I5D5nNdul2-oVXe4clPEkI-HA94pyNev7JVcng0EOWWGWbpq8g8vneMw52kiNQ5Kox-lXQzX1nvEqaocHR8w-qRtGK9wYvvYpaoQ5GleRJgUU6iyaKaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=TwiWftWX6kh0tolPm_bZBbQBA7qKIjHU9KgLTN2ZfP3UfTOvxQ8w_77DzJSrYx6ym8P51xeJE61ecshaPi4AnnwSF6RCsY4pcI8IAV6lRcp15c46Mi9S993Qmokj9FllM_vDkJVv8AwnNa1eTIuuGwJpZOews09-pnXM4Lb9wCVI60hhK9Vw7rbSDgQRt4CF4kc8OdR9MSBskKKv78_FDpPnMrcsZACcX2I5D5nNdul2-oVXe4clPEkI-HA94pyNev7JVcng0EOWWGWbpq8g8vneMw52kiNQ5Kox-lXQzX1nvEqaocHR8w-qRtGK9wYvvYpaoQ5GleRJgUU6iyaKaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
روی پاس هوشمندانه مجید عیدی؛ گل اول پرسپولیس به ذوب آهن توسط علی علیپور در دقیقه 41؛ این 96مین‌گل‌علیپور باپیراهن پرسپولیس بود و باعبور از پروین به دومین گلزن تاریخ تیم تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29261" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITXI86fxYf9vnBxZSKm6u0MZu93ZHNfux7Uf-lZKKRTEiO5H1mFKZnpPRLtSQa8KfQQbkt1-yUPdnwrIzlqf8SwXu2732E1idVnpvowkjijUbUBO60JujniZUHE0J787htRNMIlJa2x6Wj2wi_O74LGPoeSh9-Llq6TWLvlcnTj1qvsux9sLFFd7lWfIgeDvX9L0g7qxSgXZHEZ7gkJsJNagf3qxMacppIz9fsnNaCzh3pqBeVRRdmRlF8uIe1E1LndPhY6ZNqCjn19Fb2DzLacCsrX_JdK7s0ic2L1mzo1z1Oqm-5qzvZbL42c9wjmyDz9u3dwTrDpy8RXiwbCb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29260" target="_blank">📅 20:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29259">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02306a280.mp4?token=IDHcYM59995MsW7gLevb_uSuvtS3HzHrJJ6Mw0G7JH9UnQM3sH3YpmggsN9q8r1RJ5AvgNII2RaVRqj9x5IWT-rLhNju0DtZ_RMVSqTkDC14PsvYqNK5jwUlkRWcN3a6em7qv65zQTMbuCOj_YnM0tzjQd_RRNXlizC8o6foYxR2b_yWhMngl8rmK9a7_1CDia_BHt4KhbSFmYxYh9I9i53g4qYKLDscFOoH8yOrmzKn72yEsu5kSKjlL4-jXnl1maJwpxpucowfFfoLOdmswqIbdYz0HAPXGGistCBIDI7dlyb4Y2DMFbyNyRlXD-d09o33xDBnsaszbjpi1YnnMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02306a280.mp4?token=IDHcYM59995MsW7gLevb_uSuvtS3HzHrJJ6Mw0G7JH9UnQM3sH3YpmggsN9q8r1RJ5AvgNII2RaVRqj9x5IWT-rLhNju0DtZ_RMVSqTkDC14PsvYqNK5jwUlkRWcN3a6em7qv65zQTMbuCOj_YnM0tzjQd_RRNXlizC8o6foYxR2b_yWhMngl8rmK9a7_1CDia_BHt4KhbSFmYxYh9I9i53g4qYKLDscFOoH8yOrmzKn72yEsu5kSKjlL4-jXnl1maJwpxpucowfFfoLOdmswqIbdYz0HAPXGGistCBIDI7dlyb4Y2DMFbyNyRlXD-d09o33xDBnsaszbjpi1YnnMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
حرکت جالب کیلیان امباپه درنشست خبری قبلِ‌بازی بااینتر بابرداشتن نوشابه روی میز کنفرانس خبری و جایگزین کردن آن با آب به سبک رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29259" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
