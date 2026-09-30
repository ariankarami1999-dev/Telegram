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
<img src="https://cdn4.telesco.pe/file/o-kUhHuTEpuTxLvpth1ULdBpnNNrGgjX2HF9LBgg3Q7Fq9P02RxBhLIIgUkeJXJzkpGl1r9INUNsDlCveLyoiVlak2VPubzpkbRcukHUEFHR-j1uMh_VTElygDuaWMAOKdhTpjC2uDtT0QwfHyB4Y7ipG3MzYi3Y614W8_oGrqDxu8qvlYxFz9UlslDriDu7c9F3oeVR1clEv20x8ykABGtxcYAi1oDuakRB36vQvnm5mpKDWkMYEk4ZS1xVldaRBN-4QI7Xo3MksmqTcJ-8bsCLtzhN7bD1DWUFhFfFSnhlk-O10S-P3MFsrQ7_RoimBaUqQveXzKYLFXFGt1JxeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 477K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc2d60a6a.mp4?token=gFQ5B3T9S6inPMz7PZgWG3-fD50CxSWluLN28afEwJzievaDdfFRKZkbv3_Mlci9oVsqNKTI-DvYun-uJiVSL7nDeEKWpJvjdeQpMOusw383zyplkJk3D_BikSVA_ouTFSF3z4uQUfpqE4uX5aQ02o4B6_ntArJYyFBhoppw5EA9EU9hc0JO1tLHZlvzRXaBeZc0Npn00yJNXEhrFjixZFwO77-AyyMkUSYySR5ZGLskMAi791tW5-ZJzT0pGoJfAlbyc-AkWbdk5WpES0M8QAXE0bwmlJWps_bWUyz8kOhzm-Z199Kcds4F9XV_7IW6gwOjIIHaxE3BBp4sbt5wQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc2d60a6a.mp4?token=gFQ5B3T9S6inPMz7PZgWG3-fD50CxSWluLN28afEwJzievaDdfFRKZkbv3_Mlci9oVsqNKTI-DvYun-uJiVSL7nDeEKWpJvjdeQpMOusw383zyplkJk3D_BikSVA_ouTFSF3z4uQUfpqE4uX5aQ02o4B6_ntArJYyFBhoppw5EA9EU9hc0JO1tLHZlvzRXaBeZc0Npn00yJNXEhrFjixZFwO77-AyyMkUSYySR5ZGLskMAi791tW5-ZJzT0pGoJfAlbyc-AkWbdk5WpES0M8QAXE0bwmlJWps_bWUyz8kOhzm-Z199Kcds4F9XV_7IW6gwOjIIHaxE3BBp4sbt5wQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ششصد نیروی نظامی ایالات متحده به پیت هگست، وزیر جنگ، برای «تمرینات بدنی در پنتاگون» پیوستند؛ این برنامه پیش از سخنرانی «وضعیت نیروها» توسط او در کوانتیکو در اواخر امروز برگزار شد. انتظار می‌رود این سخنرانی شامل یک تغییر عمده در ساختار پنتاگون باشد و هگست قصد دارد ۲۰ درصد از سمت‌های اختصاص‌یافته به ژنرال‌ها و دریاسالارها را کاهش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/24595" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0894765b2.mp4?token=mmmmxTsW0WE_JYW7TlmbZkg7JA7hFR2OYr2FiAoXs9w9WjXYHSAEB7Ev9xZYVEUOQ-19hIMoTR3kUDvdY09Wkbsn_mxZBU_zyo-U2C9Ob9fupOKtzSnDENUKWSqOGhwSn9Wr-8ii9vLhmaQ9qTbz-XPxmDRKNUaojuldY2O0N8-6I3NbMfIPbLeGtGEkYh7ewsWdlYBvTIR9XMn8VKY6_eQDpThb6vuKHJI2Drr4spa5plvNXOaOHVP4L1qjzrFZMQ071WPauXhlcGB729NTyjZbeP7JcYnosu4SjzE8rvObEb24tpyW8wJW2Rax1KT_b2FYWUI-Z5EV3yyDSkueMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0894765b2.mp4?token=mmmmxTsW0WE_JYW7TlmbZkg7JA7hFR2OYr2FiAoXs9w9WjXYHSAEB7Ev9xZYVEUOQ-19hIMoTR3kUDvdY09Wkbsn_mxZBU_zyo-U2C9Ob9fupOKtzSnDENUKWSqOGhwSn9Wr-8ii9vLhmaQ9qTbz-XPxmDRKNUaojuldY2O0N8-6I3NbMfIPbLeGtGEkYh7ewsWdlYBvTIR9XMn8VKY6_eQDpThb6vuKHJI2Drr4spa5plvNXOaOHVP4L1qjzrFZMQ071WPauXhlcGB729NTyjZbeP7JcYnosu4SjzE8rvObEb24tpyW8wJW2Rax1KT_b2FYWUI-Z5EV3yyDSkueMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اسکورت هواپیما فلای دوبی در حریم هوایی اسرائیل با دو جنگنده @WarRoom</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/withyashar/24594" target="_blank">📅 19:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwNIN-c3OA7FXfB5egC-Ml1CIYjLTLgLNHAtw7wcaDePt_6hTZ-tFjhvPJLzuL92bAjjL64ZDBqJLZz50YWfcYQfJLnarj-YzZubcIArosvkW7evqotE5EQ96TktzRrxI_-GG4YR23TahTR7wkcY5lMyAcDPncFvs7R_G7P7uG2eLeWKXeJnRyA4Rbj9hLT4ujc0gqVcZWy0OzjL9OB4AsDVLx97ZUBEbjjCt4xzkWb7HtAamQONJN90HjoqerI3TQAl5fFxsGwAp11-oiSMLTX5GmuzmHlFnwPlKmZZztz-4Wq52QojbT93YnXydutTI6cACnVZO_AnzIMKxLHBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز دوم «فلای دوبی» مسافرها رو از عربستان به اسرائیل باز گرداند @WarRoom</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/24593" target="_blank">📅 19:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آسوشیتدپرس:
پاکستان اعلام کرده در صورت حمله حوثی‌ها به عربستان، برای دفاع از عربستان از
«هر وسیله‌ای که در اختیار دارد»
استفاده خواهد کرد. وزیر دفاع پاکستان این موضع را در چارچوب توافق دفاعی مشترک جدید میان
پاکستان، عربستان و ترکیه
اعلام کرده است. او در عین حال گفت پاکستان همچنان کانال‌های دیپلماتیک خود با ایران را حفظ می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/24592" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i630CZACBP1tmQzFnSQXsqzb2ouRNdtm2A7jG6hfzwevIPYPH9hhbWkGD5PGAZZHLVgzCBp4yYaeLNkwrb-27D5qVe8n1lvoNWWCozgrd7oULAC5X8XUxS9xtJlimp79lGTcFZMPZpEQWngNoc94xc5hk58DtJWH5O0QICmmt92B8Vlue19_PRfeioDFsLfz09Jcs58PsYlHc4vyvMuefugFR-pa1GvptZk_7c7pU_Zeir2evQt-qTF-dQghAkDitj1gfpPGpxhssKyxzTOvF1U8dD8FLLLc8lFf5Wh9vwd7GvxZ8Ut-0PrYFcrt341US5WhqfKsII4Ox4snLsNyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXDh6clU05wwA3WvdVss_ZC30uVuYbyr_wyLwGs4g3u7WY6mEAAHYZPJHGTtR14LgnG6kKtSCJ8_lb-8S_bHKcCYWCrR7PllVI74Qsiw6pj68kEyZmrSD2hRb5wKXhSPgW57tizqxZb7xEHZReGcTJvcpViWseuqe4C8aDfexWsGA_8THMqmAyDsnk9hIMBfBR-UgWQyQdE0aUNS31iipST6Cb71nM9tGq83LtXNVy3KG0lsVb4oHeTEZtwJ67T0TULJEfU683Qp3qLxhXPmxkutqWJzJZtOp2J1Dpu9tCt_l6sz0Ok57BgUUMfsxpmA2OShLnNI-bKw9XgK9_3Iag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : با دقت بیشتر مشخصه این خط جت است
و موشک نیست
@WarRoom</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/24590" target="_blank">📅 18:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT5Ul8dObSBUYcj3h4eNf8zWBTDD52SCR_Pq6LgrYhx93pCAiZuIbZV0eME0HOjHYfLTm4FpM6Kzz5lei2LCv_h2iG_zXgdEyESbYrkYZKZcqejjN5MpNv2PK9GU70qtPiOUtmC5t3JdvTxx3frPsrfIhlPLICD4wJJNx9l09cjUnM7V1JjM-H8TKAgtvqOylR-gnJG6u7c8wXuZc2TphhOEXmuBnKX5Kvdedg2Yl_LQ6a6ocOgLdAHfAEoznzn8d-Md0VYeNGDOGHg6ABHStJceNbruyM6UoTJEyZo9tnpM53J7JHy2jsIqx_uV3oltqASejlOI44BxzmpF5gagxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز دوم «فلای دوبی» مسافرها رو از عربستان به اسرائیل باز گرداند
@WarRoom</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/24589" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82776f51d.mp4?token=ib--sE83XD12L803ySCWebEDGbLjjDhVLFjRMrAfaPuZT16PuH33UoJ-yp91pM6UWfonSwcVyikgCdZU-KNuiOWycet6F7nSE3kP53r6JmtkgS01m3zl5UX7uOkcAJPfg_8eE4remxwiKEwO90sE6vYb-xfELu_3AX8WqfwS2QKWfI2V9a_q8h9TY_LFyszqeI1RDt1FozCjm2awyB34V8XmpIjOzGsDqwSDnJ9EdZGESqJntDjtu3MFUq7suZuxbKl7PYESHEVMIw1qyoZPcTB5TgcxOzwbyfxUi4dmLhdQ6dyRdX40B7srxeh_Z-wIkN_4XQ8lLmZlWWzrw7O7G4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82776f51d.mp4?token=ib--sE83XD12L803ySCWebEDGbLjjDhVLFjRMrAfaPuZT16PuH33UoJ-yp91pM6UWfonSwcVyikgCdZU-KNuiOWycet6F7nSE3kP53r6JmtkgS01m3zl5UX7uOkcAJPfg_8eE4remxwiKEwO90sE6vYb-xfELu_3AX8WqfwS2QKWfI2V9a_q8h9TY_LFyszqeI1RDt1FozCjm2awyB34V8XmpIjOzGsDqwSDnJ9EdZGESqJntDjtu3MFUq7suZuxbKl7PYESHEVMIw1qyoZPcTB5TgcxOzwbyfxUi4dmLhdQ6dyRdX40B7srxeh_Z-wIkN_4XQ8lLmZlWWzrw7O7G4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در تروث
@WarRoom</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/24586" target="_blank">📅 18:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اتاق جنگ با یاشار : توصیف دقیق و خط به خط درگیری در‌تنگه هرمز و نحوه پایان یافتن
@WarRoom</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/24585" target="_blank">📅 18:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمحمدرضا تنها</strong></div>
<div class="tg-text">داداش .
جای چرت پرت های این الاغچیان
یک قسمت از تام جری بزار شاد بشیم</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/24584" target="_blank">📅 18:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عراقچی: ایران در شرایط جدید، به موقعیت ممتازی دست یافته
کشورهای اروپایی، عربی و آسیایی اشتیاق شدیدی برای دیدار و ملاقات در نیویورک نشان دادند
@WarRoom</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/24583" target="_blank">📅 18:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24582">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKQygJFDYhLwXuTk5yzvG02u8xAefJENyP4nZdPIuKYVU7P2hDrU_QxBkAGJdBS2JsD4xzPj-xyO7gms8LC9y73kHybghxBFQspavtXtMA620nKqsLCzUIv1Hmwnv1LvEG_kVcUJwKNWHv67-U8_AaqqvFXNlkU7kDLb4m7HgvBk9SyeR8jWUBgOuqxHqgX9oPp4HOX3okjSgbpPjDSp5Lp8bJH1p-kvGALFk3ZZYSm2_rKFecorOa4-VHoBRbhAew6FxcmTFf6MxltzM2ayS9s-pUk_-iwlNUqzLgUTgtEB2JrOCM7iVDIZm4ifIc86s3iJHy3mNPSJX3ANRKeeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابک زنجانی عکسی از
«
محمود زیبایی
»
گذاشته که طی دستگیریش به عنوان کارشناس بانک مرکزی حضور داشته و ازش بازجویی میکرده، اکنون
زنجانی ادعا میکنه که این فرد عامل موساد بوده و روش‌هایی دور زدن تحریم رو یادگرفته
با خودش برده.
@WarRoom</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/24582" target="_blank">📅 17:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24581">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو:
«این یک
رویداد امنیتی بسیار جدی
بود. در پرواز فلای‌دبی از دبی به تل‌آویو، یکی از خلبانان با چاقو به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با تمام سرنشینان سرنگون کند. هواپیما وارد حالت چرخش شد و شروع به شیرجه رفتن کرد، اما یک مسافر اسرائیلی و یکی از اعضای خدمه وارد کابین خلبان شدند و مهاجم را هنگام تلاش برای دستکاری سامانه‌های هواپیما مهار کردند. اعضای دیگر خدمه نیز وارد کابین شدند و به تثبیت هواپیما کمک کردند. آنها قهرمان هستند؛ با ابتکار عمل و شجاعتی فوق‌العاده، جان بسیاری را نجات دادند و از وقوع یک فاجعه بزرگ جلوگیری کردند.»
@WarRoom</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/24581" target="_blank">📅 17:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مردی اتاق جنگ همه جا هست ! @WarRoom</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/24580" target="_blank">📅 16:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">استاد بزرگ شطرنج ، نتانیاهو : توان هک هر تلفنی رو داریم
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24578" target="_blank">📅 16:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لغو سفر نتانیاهو و کاتس به غزه در پی فرود اضطراری پرواز «فلای‌دبی»
بنا بر گزارش‌ها، سفر برنامه‌ ریزی‌ شده نخست‌وزیر، وزیر جنگ و رئیس ستاد ارتش اسرائیل به نوار غزه، در پی فرود اضطراری هواپیمای فلای‌دبی و احتمال امنیتی بودن آن لغو شده است
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24577" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24576">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61a612b92.mp4?token=ADsejSipsrzRns13zySBbh0DSTTrucYkE6L0dgUkj-3VrvnHb-uhEC22HYTlle3h8RrDOB1jXI-QfoGfO5rRtgnMENlyN0hX_jFKwy0gLlVBPHUlpE0XdhLAMwUwO2o5MPzJ-_dzL9F-5CUyob3qJnVFi1jkrJL9oFEoWka7WNcpnnqqcpOyEkptuB5igrMfyJGYZN7M07RJM7ao3yszwE5zc0WzCcNWtPJ_oC2YLdzQrtaF6FUSP4LPCpX5BClR75Vw-kKsmrby9LmhRjCwobJhrphTrFZv1gKv_N59lOKNKB3VbvsdG0MWWJsochMn_Yg6APURhj7-63_ftbPnpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61a612b92.mp4?token=ADsejSipsrzRns13zySBbh0DSTTrucYkE6L0dgUkj-3VrvnHb-uhEC22HYTlle3h8RrDOB1jXI-QfoGfO5rRtgnMENlyN0hX_jFKwy0gLlVBPHUlpE0XdhLAMwUwO2o5MPzJ-_dzL9F-5CUyob3qJnVFi1jkrJL9oFEoWka7WNcpnnqqcpOyEkptuB5igrMfyJGYZN7M07RJM7ao3yszwE5zc0WzCcNWtPJ_oC2YLdzQrtaF6FUSP4LPCpX5BClR75Vw-kKsmrby9LmhRjCwobJhrphTrFZv1gKv_N59lOKNKB3VbvsdG0MWWJsochMn_Yg6APURhj7-63_ftbPnpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل:
جمهوری اسلامی نزدیک به
۴۷ سال و نیم
است که حرف‌هایی می‌زند که هرگز قصد عملی کردن آن‌ها را ندارد. اما تنها چیزی که واقعاً قصد انجامش را دارد،
نابودی آمریکا و به ارمغان آوردن مرگ برای آمریکایی‌هاست.
یکی از دلایلی که بسیار سپاسگزارم این است که ترامپ سرانجام شجاعت به خرج داد و گفت: «کافی است؛ آن‌ها به سلاح هسته‌ای دست پیدا نخواهند کرد.» اگر بعد از نزدیک به ۵۰ سال که به شما می‌گویند قصد کشتنتان را دارند، هنوز حرفشان را باور نکردید،
شرم بر شما باد.
@WarRoom</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/24576" target="_blank">📅 16:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کودن هم بسیار هست..</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/24575" target="_blank">📅 16:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH H</strong></div>
<div class="tg-text">مصاحبه زن این یارو رو دیدی که باهاش عکس گذاشتی؟</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/24574" target="_blank">📅 16:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/24573" target="_blank">📅 16:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24570">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ML379klI3xKZMNGj9KclFQqCE1Lb1NsKTauqBiOOh7DrCj9tg_CPoORJiYtQ6oboCI-UpF7NcaP1J4iULJ0fooBNyDrmr-cUADawSDL_WZw_uAq1fGLE5fCMat3is7lfyMUcdln8trGUg85v2ImsMDGusLwr2y08XJNJZ9dCNBnLoMxeUk159fsgvJMAFVVKdAV2ksxWBuMHOQnEXkvn-qJyiJoOjzeSJ8GSHfKO2UtgpVV788dwNcxeReGOpC9tnsX_zH5rMyjxUB0zaYwkuWLmW_a6Gbce0-qDvja7JhKkfSgGeH9S24hliCuTlWs85OIh9buw3l1L85BbsNhClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af7c379d02.mp4?token=Aiole9vevMWhMA2L-R5yo5Amm7erz-K2TZMgN_LEI7d6RtzZ_wguhu3G_TQoYTjZZX0uJ-Bpam_ysTmkYyZftKton9o6ivUS1QrYHgWecKEPWe92x0jY9lINczDielcUyyXHN0YeLuHcn9eyMvr9tZ44irmvZF-bdameseGyDqTRonuXvWZCLv_j_vzV7YW5s9zNc3MR2CYu9l1L2xRK14aqcSGS63z5kBXyKh0qS6s2pMbWghk3V7TEgZsx16TaqnMU8HXK_-WCv8hajeAbfBcHwiuwce8zl2P1er8E4jDJ3HQ0hEqOBcFY6oHlVUQqyLD6fDeyi7zp9J2K-VsIqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af7c379d02.mp4?token=Aiole9vevMWhMA2L-R5yo5Amm7erz-K2TZMgN_LEI7d6RtzZ_wguhu3G_TQoYTjZZX0uJ-Bpam_ysTmkYyZftKton9o6ivUS1QrYHgWecKEPWe92x0jY9lINczDielcUyyXHN0YeLuHcn9eyMvr9tZ44irmvZF-bdameseGyDqTRonuXvWZCLv_j_vzV7YW5s9zNc3MR2CYu9l1L2xRK14aqcSGS63z5kBXyKh0qS6s2pMbWghk3V7TEgZsx16TaqnMU8HXK_-WCv8hajeAbfBcHwiuwce8zl2P1er8E4jDJ3HQ0hEqOBcFY6oHlVUQqyLD6fDeyi7zp9J2K-VsIqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردی اتاق جنگ همه جا هست !
@WarRoom</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/24570" target="_blank">📅 16:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">واکنش نیم میلیون اتاق جنگی به هر‌ خبر بازگشت :
🥚
🥚
ما هدف داریم و فرمول دادم ، فقط بایکت کنید و اصلا انتشار ندید @WarRoom</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/24569" target="_blank">📅 16:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">واکنش نیم میلیون اتاق جنگی به هر‌ خبر بازگشت :
🥚
🥚
ما هدف داریم و فرمول دادم ، فقط بایکت کنید و اصلا انتشار ندید
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/24568" target="_blank">📅 16:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبرگزاری رژیم فارس:
مدیریت بازار دلار تهران عملاً به وزیر خزانه‌داری آمریکا سپرده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/24567" target="_blank">📅 16:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مرد خردمند ، مارک لوین : آیا این کار آن‌قدر تحریک‌آمیز هست که آن حرام‌زاده‌ها را نابود کنیم؟ متن تفاهم‌نامه‌ی ما باید این باشد : «ما شما را از بین خواهیم برد؛ فهمیدید؟»
@WarRoom</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/24566" target="_blank">📅 15:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانال ۱۴ اسرائیل : ایران همچنان مظنون اصلی است.
روسای امنیتی اسرائیل از ارتش اسرائیل، شین بت و موساد به طور فزاینده‌ای وضعیت اضطراری در پرواز FZ1073 فلای‌دوبی را به عنوان یک حمله تروریستی ارزیابی می‌کنند.
کارشناسان امنیتی معتقدند اگر این یک حمله تروریستی تحت حمایت دولتی باشد، ایران تنها بازیگر منطقه‌ای است که توانایی عملیاتی برنامه‌ریزی و اجرای چنین عملیاتی را دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/24565" target="_blank">📅 15:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فرمانداری زاهدان:
صدای انفجار شنیده‌شده از حوالی کلانتری ۱۹ زاهدان، در محدودهٔ خیابان جمهوری گزارش شده است.بررسی‌های اولیه حاکی است صدای انفجار شنیده‌شده مربوط به انفجار یک شیء صوتی بوده است؛ این اتفاق خسارتی درپی نداشته و موضوع در دست بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/24564" target="_blank">📅 15:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گارد ساحلی هند: یک لنج ایرانی در ۳ مهر ۱۴۰۵ در دریای عرب توقیف شد.
این شناور در
غرب جزایر لاکشادویپ و داخل منطقه انحصاری اقتصادی هند
متوقف و در بازرسی آن
۵۲۶ کیلوگرم هروئین و مت‌آمفتامین (شیشه)
کشف شد؛ ارزش محموله
حدود ۳۳۸ میلیون دلار
برآورد شده است.
پنج تبعه پاکستان
نیز که سرنشین لنج بودند، بازداشت شدند. شناور، خدمه و محموله برای تحقیقات به بمبئی منتقل شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/24563" target="_blank">📅 15:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24562">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرنگار کانال ۱۲ : گزارشها حاکی از این است که کمک‌خلبان، شهروند عمان، با یک تبر سوار هواپیما شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/24562" target="_blank">📅 15:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرگزاری‌رژیم فارس : مقامات امنیتی ایران معتقدند اسرائیل در حال برنامه‌ریزی برای یک حمله تروریستی منطقه‌ای است که ممکن است هواپیماها یا فرودگاه‌ها را هدف قرار دهد و در این راستا، ایران را مقصر جلوه دهد تا با این کار، موج جدیدی از فشار بین‌المللی و "اتفاق نظر" علیه تهران ایجاد کند.سازمان‌های اطلاعاتی ایران در حال حاضر بر جلوگیری از وقوع چنین سناریویی تمرکز دارند
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24561" target="_blank">📅 14:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فرودگاه تبوک : خلبان فداکار اماراتی و کمک‌خلبان تروریست هواپیما هر دو مجروح شدند و به بیمارستان منتقل شدند. ما مراقبت‌های لازم را برای مسافران در سالن مسافران ارائه میدهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24560" target="_blank">📅 14:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کانال ۱۲ :
وزیر حمل و نقل اسرائیل خواستار توقف پروازهای شرکت هواپیمایی "فلاای-دبی" به اسرائیل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24559" target="_blank">📅 14:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اتاق جنگ با یاشار : این اقدام تروریستی جمهوری اسلامی مانند ترور ترامپ برای پیروزی بنیامین نتانیاهو در انتخابات تأثیر خواهد گذاشت
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24558" target="_blank">📅 14:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اتاق جنگ با یاشار : به کمربندی قاهره رسیدیم
🐫
🐫
🐫
🐫
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24557" target="_blank">📅 14:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک مقام امنیتی اسرائیلی به i24NEWS گفت تل‌آویو در حال بررسی این موضوع است که آیا ایران ارتباطی با تلاش برای ربودن هواپیمای فلای‌دبی داشته است یا خیر. به گفته این مقام، کمک‌خلبان که تلاش کرده کنترل هواپیما را به دست بگیرد و آن را سرنگون کند، اصالتاً عمانی است…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24556" target="_blank">📅 14:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پس‌از وقوع حادثه تروریستی و فرود اضطراری پرواز دبی به تل‌آویو در عربستان، منابع اسرائیلی گزارش کردند که یک پرواز دیگر از هواپیمایی فلای‌دبی در میانهٔ مسیر دبی به تل‌آویو در حال بازگشت به دبی است. @WarRoom  همچنین جمهوری اسلامی پیشتر تهدید کرده بود که ما راههای…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24555" target="_blank">📅 14:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدای دو انفجار در تنگه از قشم شنیده شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24553" target="_blank">📅 14:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی: تهران ادعای پاسخ نظامی به محدودیت‌های هوایی اخیر را رد کرد و از مذاکرات جدی با کشورهای ذی‌نفع برای رفع محدودیت‌ها خبر داد؛ در عین حال، هشدار داد در صورت لزوم، گزینه‌های متقابل غیرنظامی علیه برخی فرودگاه‌ها را اجرا خواهد کرد، هرچند…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24552" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKJeKiBZLOVAtjUIrOEqBWcljQILVWRg-mJhHPy8hCyF4-bojaXlRfa0Bp_0vRq3yj6HttCC-koSae276WvPwarQOcR12Py4Og6czcJ1VHXpQim7fhkt3LMsAQvS3QF1y9I7L157ubmJX9j10Ps67oI3JwJrm_wBT-PMvBXJOuaIPasR6ncbODEI4wSM0tREnbZciUxI0C7fRo5cScgzs2G-DI-ZPkxOnH4NEzUN3cpFfATKXBvkc4g8c-fencJ1P1VVrGxlTdUzQ9CpeYkGFAbb8EPvAiUpg0m5BTREaE0ZVGgrKnZ6l7EnfUc4HVHAFs5OX9K9-6isLevMmBzrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiuwJwlPszMzqqwP4mv_-9xGsndESqyuPdbnZZMQ59LNumWA1wLejJ7BtcFqQpGbHi0PitaCZLMU3GKeC8JEsF0Y54ytEDtikZlOGDb4eNrMTQ2kd8xDEFDzxsSbNoeRnEFmZHFh0ph3qWWM379C8yHXoiGB3ceys7o4cpX5GPzWRhiFuORVPRarheVrVBQl5AIKVmc40eGQThIgjckgM4gxQ3BFHVBzukbk6HNd-ZiFzSs30dQt9rdiSh1tcrWogFGcTM0J9OQ122DGFFxRQ8xWD7TlrI5UsTTPjtzB4OwCsEvNuqK_yCiL9HvI26-GHvt9BcjOOCY084SHxf9NRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s613rdOMAG80jhycn0r3yAa4n9-DBhYlw4ZxgiWQENzn8rl6hLnkMZHFoCmSKAQWsZJjtGzAivvLdIXM-pBAkn88vaDXf7MPXn-1g9GdqHBbNEin1uxRvFMkSRntrdgievKtaFkhMw2JCwBmNyTDpp6u96cvNw9QX_FXDmHuGj3SQ0HI3wKQX9YsMjbQBx2zl6STdd_bkzx3pa6QH-jjNjWikPHC0KOW3mMVwEEXWjIdqSAnTsf2QrPW_Lh0aFZ2ur7zzGE4zy7TckimZRv6SpVkfRqMh2MG3FqbkKSwJVJo3SfWIGaVNTVL7st9GJxiYk5ukF6oL1nJWm888rFlyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4d3219449.mp4?token=AFn4rqT1L8d6IJd6WM_ZLMJSNfKvwntt4ZFJM-61PH0QgMRzL49tsAKp5yYFmqkb_mYDunMPuNBJaVhSqNYp1nGWN8ZWmH2JOtNIxuwgZ1chKV12nl0P0ftw7Xd5_FDT_AiFbAFU_W2jVlk2x-0MPOwuFBPmGQF5BOP7q3cDtvgNoeht2pF9-K8jnMMgJ4wKYi_95Z8eGcbqkECp52zDSU0Isss9h04cQA778TrHI3ihwwCfJc_KHoV6UsSxoqImlcQcMWbnx484RpX0U8sEKePEDa0meRhD7_RwtrheRCt6aFuY2jduRk6W8P3cIedF7jl1aJK7_2seScIsZ7uLDqi18dxEkzXM-Wy6SPbL75eHnnGNKOv0J65o4SruKzXkZUmOWrFGNmQ_ejPcHICA8A1zHOfjZMFR3E7AFiTXke05hKtWI1khGgO4RM5BTUi3Y7mS7IC6AdZ_ruQHReZTuyZsnxoYZ0RfRSUzd5OFNiLewZQo6usQPAAO8n6ZveoaLoF4-cZpYysmjTw-GFFPtsCmRYuZAUVexy1nxc3SSYDTUmNSYIT7-ZldR3FrWArIHjTLChc5LpzFklzpQY7AIT2o8FIAYl_oW-aDtrBmhN-p3FsIOSFagnPr7vh8JcgZkK1IsZeo3DBZdeg0sjVfyuAEcu8_rJIscPGjz1QrDu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4d3219449.mp4?token=AFn4rqT1L8d6IJd6WM_ZLMJSNfKvwntt4ZFJM-61PH0QgMRzL49tsAKp5yYFmqkb_mYDunMPuNBJaVhSqNYp1nGWN8ZWmH2JOtNIxuwgZ1chKV12nl0P0ftw7Xd5_FDT_AiFbAFU_W2jVlk2x-0MPOwuFBPmGQF5BOP7q3cDtvgNoeht2pF9-K8jnMMgJ4wKYi_95Z8eGcbqkECp52zDSU0Isss9h04cQA778TrHI3ihwwCfJc_KHoV6UsSxoqImlcQcMWbnx484RpX0U8sEKePEDa0meRhD7_RwtrheRCt6aFuY2jduRk6W8P3cIedF7jl1aJK7_2seScIsZ7uLDqi18dxEkzXM-Wy6SPbL75eHnnGNKOv0J65o4SruKzXkZUmOWrFGNmQ_ejPcHICA8A1zHOfjZMFR3E7AFiTXke05hKtWI1khGgO4RM5BTUi3Y7mS7IC6AdZ_ruQHReZTuyZsnxoYZ0RfRSUzd5OFNiLewZQo6usQPAAO8n6ZveoaLoF4-cZpYysmjTw-GFFPtsCmRYuZAUVexy1nxc3SSYDTUmNSYIT7-ZldR3FrWArIHjTLChc5LpzFklzpQY7AIT2o8FIAYl_oW-aDtrBmhN-p3FsIOSFagnPr7vh8JcgZkK1IsZeo3DBZdeg0sjVfyuAEcu8_rJIscPGjz1QrDu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تمامی تصاویر و اطلاعات پرواز «فلای‌دبی» که همچنین آسیبی در دم هواپیما  را نشان می‌دهد.
‏همچنین در ویدیویی مسافران در حال خواندن دعای عبری «آوینو مالکینو» («ای پدر ما، ای پادشاه ما») هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24543" target="_blank">📅 13:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e6e28941.mp4?token=TwC8uCwqOQmhhY3f61shFMiBLVowHdAUCbyFjJxJVgsGEbRGUOJ2rmP5obFDGwZfUZXUMqXRWuGSeIxkIOZbbHkNhutUJ1GUxYmklVWoYGStQ2vAzMMOYleASzUGylzOYcreb3olGMwyT8Fcd_sexWUgD2pUN1xHMBkc00Eqf4hT7-M1oYZ-SkWlr1o9y14hr8hvpf37SFdci8X0rRSKyUo27fvp1LcSGkVrXpG0-GOvr0j8HRq1HJgDVOvUNECPcNkcGYczy-YhIhwZgM1DSYtnFJjHQTO4uaKdYuiUyR0qUqjOLIaWMssB8KAXl7ZtUbiDBWHt-sUDZTpH_omg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e6e28941.mp4?token=TwC8uCwqOQmhhY3f61shFMiBLVowHdAUCbyFjJxJVgsGEbRGUOJ2rmP5obFDGwZfUZXUMqXRWuGSeIxkIOZbbHkNhutUJ1GUxYmklVWoYGStQ2vAzMMOYleASzUGylzOYcreb3olGMwyT8Fcd_sexWUgD2pUN1xHMBkc00Eqf4hT7-M1oYZ-SkWlr1o9y14hr8hvpf37SFdci8X0rRSKyUo27fvp1LcSGkVrXpG0-GOvr0j8HRq1HJgDVOvUNECPcNkcGYczy-YhIhwZgM1DSYtnFJjHQTO4uaKdYuiUyR0qUqjOLIaWMssB8KAXl7ZtUbiDBWHt-sUDZTpH_omg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش زنده رویترز : مسافران به سلامت در عربستان پیاده شدند ، پرواز جایگزین در راه. است
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/24542" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvYqMZva0zMMgnwfETMWDSeXZh55VUc_AqtFonf0SYNGGEOk2eQoSlSujiZefvv-nMhFFKQW_FTq4BREGdRuKV00iFnpTAzXrC6Uph4ea9PLlSmkmePWHd0WQooACeGZeDdJmfYPHae9OOUJnjmPFKB4dIKXZzGWug4RR_7AkziYcPKPauVldBaDwE-AB1M8mxq888jAfNZN6J6Z9uV0BQAUXw7ae2ejsORB8PITjQ4uWluwNELlgmtQo_BaVAiwGR9m31cx1L-KKUtSj0lItNqAQl-kCdOrmtaYTx8SsWCWwClAybilIZWRP_sShyqtU8USDjDZteYkGGEhVSKz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dn4pB4CJ4Yf0mMs7Bw6D5kK5VTJLzEUjtGxEjmCXfqpRNBfd69y1fW3gCBpKTLVp3umobYjuSRbhJmDofs1dYOh0Xv_e8KTUI5AMdmTE-XDSAvlMSm1b-ql6CZRFTkUsQyB1DsFjk-dAtnBatwUA110qOkZFke2rJ9GP840wwLGMFrdZPWjGu79lBFC1gCKbgmw1KnZTriuhERuYG9FFXr1iNXLLUbHMJmz1MUl092K64kDXzq1LSEK7PAtXHQ6Q5iypViDdDxzU2zbjnIT9f6u6oorouITlbwtgIf2SAoH1NA2vEsWM9VpeYotwNxVlMxMnDZOjveo1RH4IXln8Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان تجرات دریای بریتانیا با تاخیر گزارش میدهد دیروز یک نفتکش در تنگه هرمز مورد اصابت پرتابه قرار گرفت  @WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/24540" target="_blank">📅 13:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">«دو خلبان دیگر کنترل هواپیما را به دست گرفتند»؛ مادر یکی از مسافران از لحظات هولناک پرواز فلای‌دبی در میانه پرواز می‌گوید. مادر یکی از مسافران گفت: «او چاقو برداشت و تلاش کرد خلبان را بکشد.» او افزود دخترش صدای فریاد و درخواست کمک را شنیده و پس از آن هواپیما…</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/24539" target="_blank">📅 13:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">«دو خلبان دیگر کنترل هواپیما را به دست گرفتند»؛ مادر یکی از مسافران از لحظات هولناک پرواز فلای‌دبی در میانه پرواز می‌گوید.
مادر یکی از مسافران گفت: «او چاقو برداشت و تلاش کرد خلبان را بکشد.» او افزود دخترش صدای فریاد و درخواست کمک را شنیده و پس از آن هواپیما شروع به از دست دادن کنترل و کاهش ارتفاع کرده است.
رسانه‌های اسرائیلی تأیید کردند که پس از ارزیابی‌های اولیه، این حادثه به‌عنوان
اقدامی تروریستی
در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/24538" target="_blank">📅 13:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksIAKh4oow24u7PJ8pnEV_VaC1DiusHyrcWS_7Q6j57KfzLq57l1gAn5QbQS2vE0aiF0p37AZsNBH2wVMj8MmHrnfVI2767rRLD7k0MI2fb_lAtZVYm9nLRQYh0yyBTaWHQsu3d-IKgIdqTW8NP3WWznGykdExUhhYY63PBLJXyCz1LkNEwNhJoV13ZoRQ1RGXteJ1nIBzB_Q5hbQq25N32I6a6mpEsb1JF1AkJHNeRaWYRedSkXV-QRnFouRcY9shpcSF7Wq06hKvffKHtDGn8CM2VUbXd0bT3ADzM1rkjx-CYktQ9KPUk05z_ueoouEKJH8H9jEcsfhCwR1ROwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجرات دریای بریتانیا با تاخیر گزارش میدهد دیروز یک نفتکش در تنگه هرمز مورد اصابت پرتابه قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/24537" target="_blank">📅 13:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سنتکام: مأموریت عملیات عزم راسخ در عراق پایان یافت.
فرماندهی مرکزی آمریکا اعلام کرد با خروج کامل نیروها و تجهیزات آمریکایی از
پایگاه هوایی اربیل در ۳۰ سپتامبر
، مأموریت «عملیات عزم راسخ» در عراق رسماً پایان یافت. حدود
۱٬۵۰۰ نیروی آمریکایی و ائتلاف
که عمدتاً در اربیل مستقر بودند، از عراق خارج شده‌اند و
ستاد نیروهای ائتلاف اکنون در اردن قرار دارد
. مأموریت مقابله با داعش در سوریه همچنان ادامه خواهد داشت و روابط دفاعی آمریکا و عراق از این پس در قالب
همکاری دوجانبه
دنبال می‌شود. سنتکام اعلام کرد نیروهای امنیتی عراق و اقلیم کردستان اکنون توانایی مدیریت مستقل تهدیدهای داعش را دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/24536" target="_blank">📅 13:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کانال ۱۲ : ارزیابی امنیتی اسرائیل درباره حادثه پرواز فلای‌دبی تغییر کرده است.
به گفته یک مقام ارشد اسرائیلی،
خدمه پروازی اضافی که برای آموزش در هواپیما حضور داشتند، توانستند کنترل اوضاع را به دست بگیرند
؛ این مقام گفت «خوش‌شانسی پرواز همین بود، وگرنه ممکن بود با یک ۱۱ سپتامبر دیگر روبه‌رو شویم.» N12 همچنین گزارش داده پس از ارزیابی وضعیت توسط رؤسای
ارتش اسرائیل، شین‌بت و موساد، ارزیابی فزاینده‌ای شکل گرفته که حادثه ممکن است یک اقدام تروریستی بوده باشد و گزارشی هم ادعا کرده خلبان متخاصم عمانی بوده
با این حال، این ارزیابی هنوز قطعی اعلام نشده و تحقیقات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24535" target="_blank">📅 12:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYPjJbVrYJnO5DitTtt4jVipfuccC2hWFyao9DdWV2bF0TsmmUeqZZ5V016OVpjbzklak4wymLLe2Sl6Df1PJ3NjLqEGh4k9A-eXEloqrBpI8plEFSRnZB4zeLCQlecbvAcOB9SfBpkvUGeSaQXG6RDG83RseGutJyC7K62ABFXNT38xh1QbSEvTwbSazSQtkoBI7-i9jm-3kcNIom9ifCha8dq05KV8S9nztOzvuKXvjUcpphddmHhIlLoxUzQe3Na5W7sqeQLtjv5MlV1ZxBkIgv1LKQtYQawbbhm9N0RTUo2XDv8-zUzvAs44U2R2jFWLEYN1j55JwXao1U9mkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه اعلام کرد حکم ، علی همتی و مجید نیک‌اندیش، دو تن از ‏بازداشت‌شدگان اعتراضات دی ۱۴۰۴ در مشهد، بامداد چهارشنبه هشتم مهر اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24534" target="_blank">📅 12:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گاردین:کاخ سفید به طور مخفیانه از امارات متحده عربی و عربستان سعودی خواسته است تا اختلافات خود را کنار بگذارند و اجازه دهند یک فرماندهی نظامی واحد برای مقابله با حوثی‌ها تشکیل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24533" target="_blank">📅 11:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24532">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84bc09bb3a.mp4?token=esDb4QVPjUp2YsfqyiD2VfIgBhrRzv0GTshv4YiXgB8PRuFqgjdTi4mXj5PyiIBzCnpt9618WZTXx-eoFsmSBxgBBXcACVt2tmmkMAVzsW0xJdZj2g7JH5AZECiXtnpRckIDNw6fnxxOsPqWHZ-nXTAWxxEupuT71rRX28oIIhMdfcH9DlJMPsbfuO4uu0NpPb6qw2-TazBgKK9y_JIb2vZQi2qOLpRPIylfoEvS3VT1-bfxbPpsk512E4fZOQBoH8rjh3y49_t77iaAjcYzcDEoNR4X0V3llChcQVkxtoSsKq-0qGRkwJO8WkEmj4QoONWO9VGh1ffKDEj-zKSmRlGk40Tn3QuETP6F6wtgBAb5L15Oj5U62Vew1pwo87CSw5iMwNl65qNr_Sd5KeQ9BmwpStpAhFoKy6W1v-K_H51LQWZdtDidbzZz1zLGLk6OpUQ1WvUcYfWcIF6FkSs-Ckgs4E73R7r0fq3iM-ICvcMjlvABIs9AGScu5XIUFi8OafG0PHFJtMV6heURntBp1p_tDuBedM8gyUGbnb2916XAgy1aGTs2X6zGKPOORCTDfhMk3ZXY1hq7xY8WbMREjq2qjXZjncGcgnb8-sWD07TOH_tNf5QNpcQkW8OOQPZaFR9bHWoyjtId11b7yCPWR1T1OFoXxsBXL24b7fwLJP0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84bc09bb3a.mp4?token=esDb4QVPjUp2YsfqyiD2VfIgBhrRzv0GTshv4YiXgB8PRuFqgjdTi4mXj5PyiIBzCnpt9618WZTXx-eoFsmSBxgBBXcACVt2tmmkMAVzsW0xJdZj2g7JH5AZECiXtnpRckIDNw6fnxxOsPqWHZ-nXTAWxxEupuT71rRX28oIIhMdfcH9DlJMPsbfuO4uu0NpPb6qw2-TazBgKK9y_JIb2vZQi2qOLpRPIylfoEvS3VT1-bfxbPpsk512E4fZOQBoH8rjh3y49_t77iaAjcYzcDEoNR4X0V3llChcQVkxtoSsKq-0qGRkwJO8WkEmj4QoONWO9VGh1ffKDEj-zKSmRlGk40Tn3QuETP6F6wtgBAb5L15Oj5U62Vew1pwo87CSw5iMwNl65qNr_Sd5KeQ9BmwpStpAhFoKy6W1v-K_H51LQWZdtDidbzZz1zLGLk6OpUQ1WvUcYfWcIF6FkSs-Ckgs4E73R7r0fq3iM-ICvcMjlvABIs9AGScu5XIUFi8OafG0PHFJtMV6heURntBp1p_tDuBedM8gyUGbnb2916XAgy1aGTs2X6zGKPOORCTDfhMk3ZXY1hq7xY8WbMREjq2qjXZjncGcgnb8-sWD07TOH_tNf5QNpcQkW8OOQPZaFR9bHWoyjtId11b7yCPWR1T1OFoXxsBXL24b7fwLJP0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحرکات نظامی امریکا در عمان @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24532" target="_blank">📅 11:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فلای‌دبی: پرواز FZ1073 از دبی به تل‌آویو در مسیر دچار حادثه شد.
فلای‌دبی اعلام کرد این هواپیما پس از وقوع حادثه، در
فرودگاه تبوک عربستان به سلامت فرود آمده و تمام مسافران و خدمه سالم و در امنیت هستند.
این شرکت اعلام کرد تیم‌هایش در حال همکاری با مقام‌های مربوطه هستند و جزئیات بیشتر پس از تأیید اطلاعات منتشر خواهد شد. فلای‌دبی در این بیانیه
علت حادثه یا گزارش‌های مربوط به درگیری خلبانان و فعال‌شدن کد ۷۵۰۰ را تأیید نکرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24531" target="_blank">📅 11:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خبرنگار کانال ۱۲ عبری: مقام‌های مسئول در حال بررسی این موضوع هستند که آیا یکی از خلبانان، خلبان دیگر را با چاقو زده است یا خیر.
قرار است یک هواپیمای دیگر از دبی به عربستان سعودی اعزام شود تا مسافران را سوار کرده و سپس پرواز خود را به مقصد اسرائیل ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24530" target="_blank">📅 11:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
اوضاع تحت کنترل است.
ما در حال تلاش برای
بازگرداندن مسافران به اسرائیل
هستیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24529" target="_blank">📅 11:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کانال 14 عبری:یک گزارش تکان‌دهنده: به نظر می‌رسد یکی از خلبان‌ها قصد خودکشی داشته است، اما خلبان دیگر از این کار جلوگیری کرده است، در حالی که آن‌ها با یکدیگر درگیر بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24528" target="_blank">📅 11:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRahat</strong></div>
<div class="tg-text">کانال ۱۲ اسرائیل : خدمه پرواز شامل یک خلبان روس و یک کمک‌خلبان اوکراینی بوده‌اند. @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24527" target="_blank">📅 11:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24526">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آکسیوس: مذاکرات ایران و آمریکا با میانجی‌گری قطر به بن‌بست رسیده است.
سه منبع مطلع گفتند تلاش میانجی‌های قطری برای ایجاد توافق میان تهران و واشنگتن پیشرفت قابل‌توجهی نداشته و
هیچ‌یک از دو طرف حاضر به عقب‌نشینی از مواضع خود نیستند
. اختلاف اصلی بر سر رفع محاصره دریایی آمریکا و بازگشایی تنگه هرمز در برابر امتیازات هسته‌ای ایران است. میانجی‌ها قصد دارند تلاش‌ها را ادامه دهند، اما بن‌بست موجود
نگرانی‌ها درباره ازسرگیری درگیری‌های نظامی
را افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24526" target="_blank">📅 11:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مورگان اورتگاس، مقام ارشد پیشین دولت آمریکا:
اگر جمهوری اسلامی منتظر انتخابات میان‌دوره‌ای آمریکا است تا قدرت تصمیم‌گیری ترامپ درباره ایران محدود شود، دچار محاسبه‌ای کاملاً اشتباه شده است.
اورتگاس گفت در دوره اول ترامپ نیز پس از آنکه دموکرات‌ها در انتخابات ۲۰۱۸ کنترل مجلس نمایندگان را به دست گرفتند،
کارزار فشار حداکثری علیه ایران ادامه یافت و ترامپ در سال ۲۰۲۰ دستور کشتن قاسم سلیمانی را صادر کرد.
او تأکید کرد تغییر ترکیب کنگره لزوماً مانع اقدام رئیس‌جمهور آمریکا علیه ایران نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24525" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کانال ۱۳ اسرائیل: دو خلبان پرواز فلای‌دبی از دبی به تل‌آویو داخل کابین با یکدیگر درگیر شدند و پس از درگیری، کد ۷۵۰۰، یعنی هشدار هواپیماربایی، فعال شد. هواپیما هنگام عبور از عربستان تغییر مسیر داد و پس از برخاستن جنگنده‌های اسرائیلی، در فرودگاه تبوک عربستان…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24524" target="_blank">📅 10:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال ۱۳ اسرائیل: دو خلبان پرواز فلای‌دبی از دبی به تل‌آویو داخل کابین با یکدیگر درگیر شدند و پس از درگیری، کد ۷۵۰۰، یعنی هشدار هواپیماربایی، فعال شد.
هواپیما هنگام عبور از عربستان تغییر مسیر داد و پس از برخاستن جنگنده‌های اسرائیلی، در فرودگاه تبوک عربستان به سلامت فرود آمد. منابع اسرائیلی می‌گویند
هواپیماربایی واقعی رخ نداده و کد ۷۵۰۰ احتمالاً در جریان درگیری خلبانان فعال شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24523" target="_blank">📅 10:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سی ان ان :
به گفته یک مقام اسرائیلی آگاه از این دیدار، نتانیاهو در سفر اخیر خود به ابوظبی، اطلاعات جدیدی از فعالیت‌های هسته‌ای ایران ارائه کرده و از
ساخت‌وسازهای جدید در سایت «کوه کلنگ» در حدود ۲۲۵ کیلومتری جنوب تهران
خبر داده است؛ سایتی که اسرائیل آن را یکی از مکان‌های احتمالی برای بازسازی برنامه هسته‌ای ایران می‌داند. این مقام همچنین گفت
ایران در کانون گفت‌وگوها قرار داشته است.
به گفته این منبع،
اسرائیل احتمال حمله ایران در چند هفته آینده را نیز مطرح کرده است.
در نشست گسترده‌تر، موضوعاتی از جمله
ایران، حوثی‌ها، تنگه هرمز و باب‌المندب
مورد بررسی قرار گرفته است. این شبکه به نقل از دو منبع از حضور یک
مقام ارشد امنیتی سعودی
در این نشست خبر داد، اما
عربستان سعودی بعداً حضور نماینده خود را تکذیب کرد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24522" target="_blank">📅 10:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر، گفت
کاخ سفید تنها ۳۰ دقیقه پیش از آغاز جنگ با جمهوری اسلامی، دوحه را از قریب‌الوقوع بودن عملیات نظامی مطلع کرده بود.
آل ثانی در گفت‌وگو با برنامه «پیرس مورگان بدون سانسور» گفت هنگام دریافت تماس کاخ سفید، در دوحه خواب بوده و مقام‌های آمریکایی به او اطلاع داده‌اند که
عملیات نظامی به‌زودی آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24521" target="_blank">📅 04:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaeY1uakojVXvAzbXbJEk6NU28fLAYiOkSd9mqhKyQVd2Kx7Lr0W9K72Ov21cO6jiO_x21WEemDDDmZAMtWDhL9GTMcMWYsinoJFP6mJ6B5R71OTSghgolaBlyO-tj2OnmBP5J_MNCYt9GXYb-xILxPU28RUKQ4BdDlv4E5stZjBeO5MeJkUvpqaYWKzCEPfsg4sisQaWSVxEYBeBbhQK0ISX1-O2ntGgA2g1m8akNq9uKIe7oD6dv5-WZiBShXxcU-IxDyi5eqikX8zyT_8ZVWq1M-HL4-z2CwQPFugn3XZkhku6zZy_F9nv3KcvQCUpWDStR552xbW2B_ocCi38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث تحلیلی را بازنشر کرد : ایران عملاً کنترل تنگه هرمز را از دست داده
الکساندر اشتال از مؤسسه «بورگ‌گرابن آنالیز» مدعی است که
ایران عملاً کنترل تنگه هرمز را از دست داده
و صادرات نفت خاورمیانه به حدود
۹۴ درصد سطح عادی
بازگشته است. به گفته او، امارات از ماه مه با ایجاد سازوکاری موسوم به «شاتل هرمز»، نفتکش‌ها را از مسیر نزدیک سواحل عمان عبور داده، نفت را در دریای عمان به کشتی‌های دیگر منتقل کرده و سپس نفتکش‌ها را برای بارگیری دوباره به خلیج فارس بازگردانده است. این روش بعداً توسط
عربستان و کویت
نیز به کار گرفته شده و اکنون حدود
۱۱۶ نفتکش
در این چرخه فعال هستند. به گفته اشتال، ناوگان بحری عربستان نیز با ۲۳ نفتکش در منطقه فعال شده و سنتکام با تعیین مسیر و زمان عبور نفتکش‌ها و تمرکز پوشش هوایی و دریایی، از این جریان پشتیبانی می‌کند. در مقابل، او می‌گوید صادرات نفت ایران به‌دلیل کمبود نفتکش‌های حاضر به ورود به خلیج فارس و فشار محاصره آمریکا به‌شدت مختل شده و
بارگیری نفت در پایانه خارک از ماه اوت عملاً متوقف بوده است.
اشتال در نهایت می‌گوید ایران نتوانسته تنگه هرمز را ببندد، انتقال نفت از مسیر عمان در حال گسترش است و گلوگاه اصلی اکنون
تجهیزات انتقال نفت از کشتی به کشتی در دریای عمان
است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24520" target="_blank">📅 03:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiA9MFpdUaIYoSvVz1pmJlUCFOh9Mi073tioXqKtXDZ93kAK3P0WRuFkJ2zle6FTIfLaJ5zrUm55j6lDoBsiHZFvKt5qwMblSYPRc-uMvb0edVAo9kHOk20eXOlu_tftxiZvOELOM_OhDY0cQUbMjggNoARQb9Jq-Fwdvgnnvus153VGx8yORR8od8Ro01SZHb6lGmQiGL9Ao_PhoNCI9OYyIZwl77vsok0lsSbuT-anFiqqJCDT53-2C2dTcMKYxiGCt06p4R22YR0Vsu8mfuYUt5loBTYgwFB-205sF7iUn3PC2HQt2RzXP6sdf7kl822TZ_YBi0mIQ8voh86FsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی و هیئت اعزامی بالاخره از نیویورک دل کندن و بعد از توقفی در دوحه قطر به تهران بازگشتند. همچنین شش سوخترسان در منطقه تنگه هرمز و خلیج فارس فعال هستند و یک پی-۸ پوسایدن در دریای مکران فعالیت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24519" target="_blank">📅 03:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آکسیوس: احتمال شروع جنگ بسیار بالاست
آکسیوس به نقل از مقامات آمریکایی: ممکن است ترامپ پس از انتخابات دستور بازگشت به عملیات رزمی گسترده علیه ایران را بدهد.‌‌
ایرانی ها اعلام کردند تا زمانی که واشنگتن با بازگشت به یادداشت تفاهم موافقت نکند، امتیازی نخواهند داد.‌‌
هیچ پیشرفت محسوسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها چیزهایی را طلب می‌کنند که واشنگتن نمی‌تواند آنها را بپذیرد.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24518" target="_blank">📅 03:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRPMp2IKhyE7cSpCDbsxcPHkwHj_1mXwdv_NHqaGfX_lGj7lGe-kJHkqAY6hb4lacOc1o7G57uUMaZJIroas1Mtjsev-Xt21G9XWeZARDGGA90w9-95x7MfIj6TY5RooED9XALetrw21tnlhukphclWW83v6USYN-WmDdYxRaHdIUn6wm69s2wbZUP4FRsHxfUUxrInT2zRQPwjHUgvwPf-sHXT5ta5g7vzzztLBrUkIjtKWcYMexDAmg1ZHffvOMNK2sflY7k5Ko41h7hjfNN9o1LZNXR_0RIVQC5MHZgy-L9FIqwtaMsqpxYz9dDXyjr_ZrG3357EVGdLebXgIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا در چارچوب برنامه «پاداش برای عدالت»، برای دریافت اطلاعات درباره
احمد فرهادی، عبدالله محرابی و علی‌اصغر نوروزی
، از مقام‌های نیروی هوافضای سپاه پاسداران،
تا ۱۵ میلیون دلار پاداش
تعیین کرد. این افراد در توسعه موشک‌ها و پهپادهای ایرانی و تأمین مالی و تجهیزات سپاه نقش دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24517" target="_blank">📅 02:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5adfdf90.mp4?token=ZxBKohlEU-np9izIps8T-25-y8nuv7mw93p6AWY9B6oz90hCoUtBhcq3pgBlA-iBc4e6-xPGp0AxjQ-B7OQkFYs53mtsoi8zRgwcQQb5ZitKwSaoBXeP_Ga7bA9BB00sOWcE6cz7kby8ZjG40CoYc0sCIPmB3oGjiY27ovemHs_FwhnAPSrUR_OH8wjiUzhBTWrrqTqvEpexpVZZDSSRd22Cd4dCcp208ry1o2D5cL4g2AxQMuR64mnMXEHeEQGKDkYIS3yf6te49iPVWUF7dBO74DL0ShTa0Dw7CVueCetVEHOOHYo3q1WWpOj1YEtIvVf8Dvc8-58ISacqCtRy9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5adfdf90.mp4?token=ZxBKohlEU-np9izIps8T-25-y8nuv7mw93p6AWY9B6oz90hCoUtBhcq3pgBlA-iBc4e6-xPGp0AxjQ-B7OQkFYs53mtsoi8zRgwcQQb5ZitKwSaoBXeP_Ga7bA9BB00sOWcE6cz7kby8ZjG40CoYc0sCIPmB3oGjiY27ovemHs_FwhnAPSrUR_OH8wjiUzhBTWrrqTqvEpexpVZZDSSRd22Cd4dCcp208ry1o2D5cL4g2AxQMuR64mnMXEHeEQGKDkYIS3yf6te49iPVWUF7dBO74DL0ShTa0Dw7CVueCetVEHOOHYo3q1WWpOj1YEtIvVf8Dvc8-58ISacqCtRy9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی مجلس نمایندگان آمریکا، مایک جانسون:
سناریوی وحشتناک این است که، خدا ناخواسته، دموکرات‌ها کنترل مجلس را به دست بگیرند. آن‌ها هر کمیته‌ای از کنگره را به یک نهاد بازرسی تبدیل خواهند کرد.
آن‌ها در تمام طول روز، هر روز و هر ساعت، به جای انجام کار، فقط به دنبال حمله به رئیس‌جمهور، خانواده‌اش، اعضای کابینه، حامیان مالی حزب، چهره‌های برجسته در بخش‌های تجارت و صنعت خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24516" target="_blank">📅 01:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مارک لوین : آماده باشید، سوپرایز در راهه
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24515" target="_blank">📅 00:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/042e52e439.mp4?token=MedopXZWwJFZ6NqES3vM6eUDGkOJ5jMGW2HDhVCikh_S33dNEVhYvLQwAYt8O_Y9kroA-kIC1_VjiNIW89qef43OEQGrwEllcSIJIvQ0k_VySiM8zLID1mTIpK6x5M1DFCVLdXsI-nK8o2-KeGvmiqyxscjlfxCqf8M0bv6qO_mAQcV5hBmp-a8cwuLNYwNYhIG1PtKuehMzXMmvtFj--oHaieSPUSFdya26i0c0vYPwMLCVyZY1CfN5pQl5dC7geHdpW9yQ6KIn02aoXEZcH74DbH3U0yEnz6JGwoo_iJGhEvrbJ4s12X_PSEtN_5OTklFDukoVamXbYfLgVdnQHS1BN_XRQ4G7yafTVNvt6wb5QI_Truwp4JAmKFbC2hqtBa_IH5geWW5zaITqfO0QWWrq-8Zal4ZG1bc0uVccIkJ8lq4yZT6Kd2TyxVnTDhJitlQJns5mpNde5Fz17vIj1VhI0-6mvuN25NXTjSgUjE_yVTmO8_0i56XBrUqBE1VNeYC0Qr6hyKpn4meIKkYLaXDXW20S0k6qw8N9bp948STqbpbv_6O3TFpOMUf5tx8Emla62m7OZfWRek_26p8p3KWoT01TkMjnh4g1JbqIYKGjbATBB-8w4JmSn5K0E9mQ5-FsTebvpXTj4-tHnLWbqhhLUemY2vo-x9sqgnJL_JU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/042e52e439.mp4?token=MedopXZWwJFZ6NqES3vM6eUDGkOJ5jMGW2HDhVCikh_S33dNEVhYvLQwAYt8O_Y9kroA-kIC1_VjiNIW89qef43OEQGrwEllcSIJIvQ0k_VySiM8zLID1mTIpK6x5M1DFCVLdXsI-nK8o2-KeGvmiqyxscjlfxCqf8M0bv6qO_mAQcV5hBmp-a8cwuLNYwNYhIG1PtKuehMzXMmvtFj--oHaieSPUSFdya26i0c0vYPwMLCVyZY1CfN5pQl5dC7geHdpW9yQ6KIn02aoXEZcH74DbH3U0yEnz6JGwoo_iJGhEvrbJ4s12X_PSEtN_5OTklFDukoVamXbYfLgVdnQHS1BN_XRQ4G7yafTVNvt6wb5QI_Truwp4JAmKFbC2hqtBa_IH5geWW5zaITqfO0QWWrq-8Zal4ZG1bc0uVccIkJ8lq4yZT6Kd2TyxVnTDhJitlQJns5mpNde5Fz17vIj1VhI0-6mvuN25NXTjSgUjE_yVTmO8_0i56XBrUqBE1VNeYC0Qr6hyKpn4meIKkYLaXDXW20S0k6qw8N9bp948STqbpbv_6O3TFpOMUf5tx8Emla62m7OZfWRek_26p8p3KWoT01TkMjnh4g1JbqIYKGjbATBB-8w4JmSn5K0E9mQ5-FsTebvpXTj4-tHnLWbqhhLUemY2vo-x9sqgnJL_JU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید ایران نمی‌تواند سلاح هسته‌ای داشته باشد. چرا؟ کره شمالی می‌تواند سلاح هسته‌ای داشته باشد؟
ترامپ: «آه، چون شما رئیس‌جمهور متفاوتی داشتید!!!
کیم جونگ اون
. او دوست من است. ترامپ را دوست دارد و من هم او را دوست دارم. تا زمانی که من اینجا هستم، او در امان خواهد بود. می‌دانید چرا؟
چون برای من احترام قائل است.
»
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24514" target="_blank">📅 00:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24513">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a35cfdae.mp4?token=n9ubQD1pZu9IMyS57BeGGShL0sc9Tk3XwYR0KGrsX67N3isBQmzLCmhnlDIo9BmfVVCOeAf1SPwGaGpHSEGSHZDEn_xLLJoGgOvDGyDbwQcll-ET21hSSPYnXy5OnkkqQezU4G1VlfzJXRk6cQzuNCTnAJH1z3CNqzXpSHynHM80MmTdlmsVdeq1nDVFg-ifV3vCcACuc5ZRjdzc88tn6_fCIo3duLNuYE6h66QsYCAV8lbg0ON0ji--OuyPsbWttUkJvB0BjpMFu4hhXl002TKgjChW7RBtpnX1Cf8L7YF2lfHNozHNyYEuGuItlWgLMCpJ7t9xjB_nMx-QgT7izg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a35cfdae.mp4?token=n9ubQD1pZu9IMyS57BeGGShL0sc9Tk3XwYR0KGrsX67N3isBQmzLCmhnlDIo9BmfVVCOeAf1SPwGaGpHSEGSHZDEn_xLLJoGgOvDGyDbwQcll-ET21hSSPYnXy5OnkkqQezU4G1VlfzJXRk6cQzuNCTnAJH1z3CNqzXpSHynHM80MmTdlmsVdeq1nDVFg-ifV3vCcACuc5ZRjdzc88tn6_fCIo3duLNuYE6h66QsYCAV8lbg0ON0ji--OuyPsbWttUkJvB0BjpMFu4hhXl002TKgjChW7RBtpnX1Cf8L7YF2lfHNozHNyYEuGuItlWgLMCpJ7t9xjB_nMx-QgT7izg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران و تنگه هرمز: «ما طی دو روز گذشته
بیش از هر زمان دیگری در تاریخ، نفت را از تنگه هرمز خارج کرده‌ایم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24513" target="_blank">📅 23:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431a4ea541.mp4?token=rDpzdimZSJrVW4kg9bQca_hqus1qHuzjvuzCJgdeWFf2GcxBusX3y3qJZzNlLjTTIWTJvVPz0EXtsatP-Mz60mPVnmxt2-I-INGtTHqDxZuNsV3nLLsi2RpUrWeW4Xc61kyE5BElcEjYjitS4O6lppMR-Y6SpMsjURJkgFU9aLJ6m6szysFQ3uO3ZNIAqhRYA0mmRZ4jZjw6TcbP7JmRCskScJh2lHtfztqGM84ZbLdAD5qpIpMfMfSoNS6bCyueyTf8wQ6Tex1XG-A0JaTdCLZp_1zgEKQe1KZiTsLTzt9JRcl3YuC9c_yx41drsryu3G3CoxserV4utSueq8LRPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431a4ea541.mp4?token=rDpzdimZSJrVW4kg9bQca_hqus1qHuzjvuzCJgdeWFf2GcxBusX3y3qJZzNlLjTTIWTJvVPz0EXtsatP-Mz60mPVnmxt2-I-INGtTHqDxZuNsV3nLLsi2RpUrWeW4Xc61kyE5BElcEjYjitS4O6lppMR-Y6SpMsjURJkgFU9aLJ6m6szysFQ3uO3ZNIAqhRYA0mmRZ4jZjw6TcbP7JmRCskScJh2lHtfztqGM84ZbLdAD5qpIpMfMfSoNS6bCyueyTf8wQ6Tex1XG-A0JaTdCLZp_1zgEKQe1KZiTsLTzt9JRcl3YuC9c_yx41drsryu3G3CoxserV4utSueq8LRPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره ایران: «نمی‌دانم هنوز قرار است تسلیم شوند یا نه، اما
تسلیم خواهند شد. آنها وضعیت بسیار بدی دارند.
»
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24512" target="_blank">📅 23:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENFz3-RrHKWtkNsCtsi2DN8JG_4a09tRFcbecyGZJgF-7k4PKEGXxEG-ETqlkrFGUCq_Jss35tMKor-WhpHe7Bqltf19VY4y7kqZ07cRQO7X92c2-HgFebbmZhRxPSIESRMOydJ4tpvGT2N3qP0SPF7xg6KMjakHnsT9DbRLAj9JOYLv0zMK66tzyRLqAldppk5JK1UJaz3EvJsk3KarfqtQSBB50lNy5fPFnx3ssnaalCz10ze5TVC30pigng9KDyoIwZIK1bYauYaKJHU-FLL225cRHQD9haFL03flDxRLyNj9jPHSjU79XGblnWnnrp7CnuN7loZn27xrloRpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ سوخترسان و یک پی۸ پوسایدون در حال انجام مأموریت در تنگه هرمز و خلیج فارس
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24511" target="_blank">📅 23:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24510">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skXbScJVuBuiVl2DL---2tECBvqpX3ke01X7tzOV6wBnBUFKY4xGJVl4C-u352TCTKzo1eM1CGjfnMaM6pHFUNtkVzzf9iQke-hN4mbxW20-ul8koXho8dU9A4L5IomLcHJz9-bYtAtXcNRgnQ2vl6agK3dE3CIwP1Yy3mZj1qsqe7nrFpcXHL4K5v0JfgP4aWe588swmx2hqXKz1NDvexKFD-W8vM1PPA9LOII0qfcD0__It2zU_qrp67YGLC72oYXbwNBwrGsQBw5UhiKA-U4NPQ8n82PYe40_FbOWaeWzBQ19AfUUfUom3MrDg22sQpMW10-6UG6sneH9YbbKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ اسرائیل
: اسرائیل برای جنگ بزرگ تر از ۴۰ روزه بمب سنگرشکن خریده است
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24510" target="_blank">📅 23:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دلار ۲۵۶،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/24509" target="_blank">📅 22:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55c30c663.mp4?token=WZbvxWmCjMon7HUd0nnOUEXyzfuq-gGjWWkLmLV3l96mt1LlrCFkRTM4i7An_1UfBptpXnOsMq6gUmTJAlTc48VRYEbaPX1N1XPoIzH1Bt_HrdWpl5P8JZPdaSNKltpO9BqDpfU0Z2wh2x6V2HfTvVLHGOS7gKXopmZyCnozVo27RPfEn5Jo8gqtfk_4auREmW0nSJo_1tayJGDhDYy0ykUFxR_-QvyFPEtq0vSX38XGx0e7yJDQ5CLTOOKpQTqJf_3SyHlABLjhDRWnBE6FgnJ2GdnPYvrtwCCrlEnvNcQfiZ3FQnT-0SMbbUqfA5-a3CYJ4UnN7NiMRfj7Z-VXEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55c30c663.mp4?token=WZbvxWmCjMon7HUd0nnOUEXyzfuq-gGjWWkLmLV3l96mt1LlrCFkRTM4i7An_1UfBptpXnOsMq6gUmTJAlTc48VRYEbaPX1N1XPoIzH1Bt_HrdWpl5P8JZPdaSNKltpO9BqDpfU0Z2wh2x6V2HfTvVLHGOS7gKXopmZyCnozVo27RPfEn5Jo8gqtfk_4auREmW0nSJo_1tayJGDhDYy0ykUFxR_-QvyFPEtq0vSX38XGx0e7yJDQ5CLTOOKpQTqJf_3SyHlABLjhDRWnBE6FgnJ2GdnPYvrtwCCrlEnvNcQfiZ3FQnT-0SMbbUqfA5-a3CYJ4UnN7NiMRfj7Z-VXEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار: دونالد ترامپ، رئیس‌جمهور آمریکا با انتشار این عکس از ، میزبانی نشست ناهار با مدیران ارشد فناوری و هوش مصنوعی در کاخ سفید و محل نشستن آنها خبر داد.در این نشست چهره‌هایی مانند ایلان ماسک (تسلا و اسپیس‌ایکس)، مارک زاکربرگ (متا)، جف بزوس (آمازون)،…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24508" target="_blank">📅 22:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اتاق جنگ با یاشار : انتخابات پارلمانی اسرائیل
۵ آبان
برگزار می‌شود. بر اساس آخرین نظرسنجی کان منتشرشده در امروز ،
حزب «یاشار»
به رهبری گادی آیزنکوت با
۲۳ کرسی
بزرگ‌ترین حزب است، پس از آن لیکود به رهبری بنیامین نتانیاهو با
۲۱ کرسی
و حزب نفتالی بنت با
۱۱ کرسی
قرار دارند. در مجموع، دو اردوگاه اصلی هرکدام حدود
۵۲ کرسی
دارند و هیچ‌کدام به حدنصاب
۶۱ کرسی
برای تشکیل دولت نمی‌رسند. در سنجش انتخاب نخست‌وزیر نیز نتانیاهو با
۳۹ درصد
تنها یک درصد از آیزنکوت جلوتر است.
جمع‌بندی: یاشار فعلاً بزرگ‌ترین حزب است، اما در رقابت برای تشکیل دولت، نتانیاهو و مخالفانش تقریباً برابرند و هنوز برنده مشخصی وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24507" target="_blank">📅 22:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با یاشار : انتخابات میان‌دوره‌ای کنگره آمریکا
۱۲ آبان ۱۴۰۵
برگزار می‌شود. آخرین نظرسنجی‌ها تا امروز نشان می‌دهد فعلاً
دموکرات‌ها دست بالا را دارند
؛ در نظرسنجی‌های ملی، دموکرات‌ها حدود
۷ تا ۱۴ درصد
از جمهوری‌خواهان جلوتر هستند. این برتری می‌تواند برای پس گرفتن مجلس نمایندگان کافی باشد. در مجلس سنا اما رقابت نزدیک‌تر است؛ جمهوری‌خواهان اکنون
۵۳ کرسی
و دموکرات‌ها
۴۷ کرسی
دارند و دموکرات‌ها برای رسیدن به اکثریت به کسب چهار کرسی بیشتر نیاز دارند. ایالت‌هایی مانند
تگزاس، اوهایو، آیووا، آلاسکا، مین و کارولینای شمالی
از مهم‌ترین میدان‌های تعیین‌کننده هستند. جمع‌بندی فعلی:
دموکرات‌ها در رقابت مجلس نمایندگان موقعیت بهتری دارند، اما کنترل سنا همچنان کاملاً رقابتی است و نتیجه نهایی مشخص نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24506" target="_blank">📅 22:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانال ۱۵ اسرائیل : صدای اعتراضات در ایران بلندتر شده و حاکمان خواستار اقدام تهاجمی پیشدستانه به دلیل وضعیت وخیم کشور هستند؛ مقامات افراطی در ایران گفتند : "انجام حمله پیشدستانه علیه آمریکا و متحدانش ، بهتر از تحمل وضعیت فعلی است."
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24505" target="_blank">📅 21:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda61c2c14.mp4?token=aB4z8ZWzmvrMGL0FhXXUWKIGxNDQtizhSsSMPAO4VXoq0ZjUI-2s42Kyk9x3nhb8dxLj5JQw4jwZFBpSvENyBFY-HfU45MTwhY0CCOQg6hlcCnOgJuemGLF-iarHe4JgFhcMNA9aSYw360fVHzV60FffTnw51inuSfZxAAW6hPiZksLa2u17Y4PBIIpL2iV_RSgH6fQSZR6qMDZWVIsz2QhLUrZJGKHRMDlUQYFxnOzDmcZiKfSoUTIDiuZPUrnFrmCMRb9RFlbXPnC-vCJV7hgP0R77Su3aNx8rb4QdT_YWVQh10oX_PMqdiRosVYRo7Bd4IzERCFySgMi4OPshEBMXgJVsm_OgDou58oyer5ZQ-VeTTHVKDckRf1atYr0BPztCEbkFn3yocorhu2oY59Nhd87X_4V-a3c_wlji1GT89tP2UEs37uUKLX2Wiz64-gvtyqkiZMA-__RURFNknrFLZ-byS3LX5d6V4dC-ji0_5pBWWysXALA-Ut1CyaTFTTUCbRYYN0GXN9Onouylv4lslrxviOvTfP_WDfxv-JKLx2gB3gLob2trCI15xijSzwS4hpeL_U7ZMUh_x0iurIHvohbF_qOSVQJ614hTayki8LNGBG4gTRZo22kKlro0FcH37qITvOxBzLDqgA3bFm8AzFn1qf8qaa-8AmJSspM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda61c2c14.mp4?token=aB4z8ZWzmvrMGL0FhXXUWKIGxNDQtizhSsSMPAO4VXoq0ZjUI-2s42Kyk9x3nhb8dxLj5JQw4jwZFBpSvENyBFY-HfU45MTwhY0CCOQg6hlcCnOgJuemGLF-iarHe4JgFhcMNA9aSYw360fVHzV60FffTnw51inuSfZxAAW6hPiZksLa2u17Y4PBIIpL2iV_RSgH6fQSZR6qMDZWVIsz2QhLUrZJGKHRMDlUQYFxnOzDmcZiKfSoUTIDiuZPUrnFrmCMRb9RFlbXPnC-vCJV7hgP0R77Su3aNx8rb4QdT_YWVQh10oX_PMqdiRosVYRo7Bd4IzERCFySgMi4OPshEBMXgJVsm_OgDou58oyer5ZQ-VeTTHVKDckRf1atYr0BPztCEbkFn3yocorhu2oY59Nhd87X_4V-a3c_wlji1GT89tP2UEs37uUKLX2Wiz64-gvtyqkiZMA-__RURFNknrFLZ-byS3LX5d6V4dC-ji0_5pBWWysXALA-Ut1CyaTFTTUCbRYYN0GXN9Onouylv4lslrxviOvTfP_WDfxv-JKLx2gB3gLob2trCI15xijSzwS4hpeL_U7ZMUh_x0iurIHvohbF_qOSVQJ614hTayki8LNGBG4gTRZo22kKlro0FcH37qITvOxBzLDqgA3bFm8AzFn1qf8qaa-8AmJSspM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر نخست‌وزیر قطر درباره جمهوري اسلامي:
ایران همسایه ما بوده و برای همیشه همسایه ما خواهد ماند. ما جایی نمی‌رویم. آن‌ها هم جایی نمی‌روند.
ما دهه‌ها رابطه بر پایه احترام متقابل با آن‌ها داشته‌ایم. همکاری‌ها به دلیل تحریم‌ها محدود بوده است، اما ما تمام تلاش خود را برای حفظ این رابطه همسایگی خوب به کار بستیم، هرچند در طول این دهه‌ها و در بسیاری از سیاست‌ها اختلافات زیادی داشتیم.
@WarRoom
اتاق جنگ با باشار : اگه موندین به خاطر همین رژیمه ! هم این رژیم میره هم شما میرید ! بماند به یادگار… به دل پاک بی بی قسم</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24504" target="_blank">📅 21:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزارت خارجه دانمارک:
دانمارک در تازه‌ترین توصیه سفر خود،
همچنان از تمام شهروندانش می‌خواهد به ایران سفر نکنند
و از دانمارکی‌های حاضر در ایران نیز می‌خواهد
کشور را ترک کنند
. وزارت خارجه دانمارک وضعیت امنیتی ایران را «بسیار پرخطر، ناپایدار و غیرقابل پیش‌بینی» توصیف کرده و هشدار داده که
راه‌های خروج از ایران ممکن است با اطلاع کوتاه‌مدت محدود یا کاملاً متوقف شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24503" target="_blank">📅 21:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24502">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا:
۱۰ فرد و نهاد مرتبط با شبکه تأمین تسلیحاتی
وزارت دفاع ایران
را تحریم کرد. اسامی افراد:
سید اصغر علیرضا‌زاده طباطبایی، علی فتوت احمدی، پریسا لالی، لی فِن و وسیم پاشا تاجمل
. نهادهای تحریم‌شده نیز
کاوشکام آسیا R&D، EC Mojo Technology، Cavalier Dynamics پاکستان، Cavalier Dynamics عربستان و Cavalier Dynamics ترکیه
هستند. به گفته آمریکا، این شبکه در تأمین
قطعات الکترونیکی، تجهیزات دوکاربردی، موشکی و پهپادی
برای ایران نقش داشته است. تحریم‌ها دارایی‌های این افراد و شرکت‌ها در حوزه صلاحیت آمریکا را مسدود می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24502" target="_blank">📅 21:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24501">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سخنگوی فرمانده کل نیروهای مسلح عراق : نیروهای آمریکایی به کشور خود و پایگاه‌های کشورهای همسایه بازگشتند، پس از دستیابی به توافقات. مأموریت ائتلاف فردا به طور رسمی به پایان می‌رسد, ائتلاف فردا خروج خود از کردستان عراق را نیز به پایان خواهد رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24501" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانال i24 عبری با استناد به منابع اطلاعاتی آمریکایی گزارش داد:
«ایالات متحده، نتانیاهو را در ارزیابی خود در مورد احتمال وقوع حمله به اسرائیل، سهیم می‌داند.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24500" target="_blank">📅 20:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8Cj6r-He7CUwhMsBSpqHxRC12ZGCG11c5z0FQnpuTEoknsio-7g1moI2RrwrN10F_gfLov31ZtTsAxF-Cm1uwEbcuRPTv8LEcDJJqtoXfiK-JFLVPh-MB0zAP-jFNVepYEimwmK_KLKtH3pDPbCDTwCLVjQjHWdGm53wb3rcXlNjUDkYxjdpeCK-G9AiaLQNCWZvFi49Zm3ZQPcJD_EkdW0vaJIs0Y8KHhAvZkzcBFFXU-8b5nihbkLkvDB8Cnph2rNvYRa2hLbFr1evpNYU_kxpfvVRHvs0hn7IfsBgi9rh-byOXBk5l--btC2HjoAparpvbNDIzCd2DMNbtxJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بمب‌افکن B-1B لنسر از فرودگاه پر حاشیه فیرفورد که مورد حملات احتمالی تروریستی جمهوری اسلامی قرار گرفت،  بلند شده و مشغول پرواز تمرینی و تمرین سوخگیری هوایی است. شکی نیست که این از آخرین پروازهای تمرینی قبل از حملهٔ اصلی به ایران است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24499" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24498">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از قشم پهپاد پرتاب شد به سمت تنگه و موشک کروز نیست اینبار
@WarRokm
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24498" target="_blank">📅 20:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24497">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0amVoLwdSGFbEyURp-Eyxz4Uxc_5AUG6cLJnmVMo0SV1AhGQIZ2Zi3tM5ScVFdKGYEgSODxnSjAdNcTz9qHVA6LfbjjhqjJsRc-UeBPHXPBp3jJj_ek4C6cvG6bxrKq02B9go_JMYMoDtFm8v0dZjTkK3SrFMFJN2Ffkbsv5hgdRd_sqaKbMbO5EvT1Ufdr_vm3B2bC00ub9M1HOkePbSbHAXOLgTcKc2pXpcwbCYXDr53PZzen4yQNJin6psGYqi75KgoIfPgtC1es3Gk-3CO0PbhYlw02JDkMcK21fehOe2fSMzT3JokpUM0W8kDlzK_JSenn3s3PtXQ6UdwdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار: دونالد ترامپ، رئیس‌جمهور آمریکا با انتشار این عکس از ، میزبانی نشست ناهار با مدیران ارشد فناوری و هوش مصنوعی در کاخ سفید و محل نشستن آنها خبر داد.در این نشست چهره‌هایی مانند ایلان ماسک (تسلا و اسپیس‌ایکس)، مارک زاکربرگ (متا)، جف بزوس (آمازون)، جنسن هوانگ (انویدیا)، سم آلتمن (OpenAI) و داریو آمودی (آنتروپیک) حضور دارند.موضوع نشست، آینده هوش مصنوعی، رقابت فناوری آمریکا و چین و امنیت و مقررات این فناوری است. حضور هم‌زمان مدیران بزرگ‌ترین شرکت‌های فناوری آمریکا، این جلسه را به یکی از گردهمایی‌های مهم اقتصادی و فناوری دولت ترامپ تبدیل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24497" target="_blank">📅 19:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07f7a9d90f.mp4?token=GqLJLYf7lNqG0iuIZkdku6aEqfXv-z7UjYyCVItErgJK9PmWl7UzEYeml52HHjHxgJlX-2sjhILMwfPrtNUI7rX9Hp4SsfqiE5HjBj-IldXBxtiQIVDOIvbqrLPVj7tmIMv58IqBIi1XJtQNml4_oSvnBhVTYlcGkYXzQR8Ezj1a2fQzV0RbrQ7aFjLZYh3f_8RNFLPl_QMpRZ0yRnQg99ED6kV7MQH1YZmRsfmZg2bSSt21sHYooS7rR7-XtIQ1IaJvtdBvYEqd_ub8eX8P0GoryKXJPSIy6qKrJWThaLI_fim5oGEuEaG6tNQa1-wwHBhY0kdnLXbvsrRDrQ2eww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07f7a9d90f.mp4?token=GqLJLYf7lNqG0iuIZkdku6aEqfXv-z7UjYyCVItErgJK9PmWl7UzEYeml52HHjHxgJlX-2sjhILMwfPrtNUI7rX9Hp4SsfqiE5HjBj-IldXBxtiQIVDOIvbqrLPVj7tmIMv58IqBIi1XJtQNml4_oSvnBhVTYlcGkYXzQR8Ezj1a2fQzV0RbrQ7aFjLZYh3f_8RNFLPl_QMpRZ0yRnQg99ED6kV7MQH1YZmRsfmZg2bSSt21sHYooS7rR7-XtIQ1IaJvtdBvYEqd_ub8eX8P0GoryKXJPSIy6qKrJWThaLI_fim5oGEuEaG6tNQa1-wwHBhY0kdnLXbvsrRDrQ2eww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی وا
l
نس، معاون ترامپ، درباره جمهوري اسلامي:
فکر می‌کنم [مقامات] ایرانی‌ها درک کرده‌اند که اشتباه کرده‌اند و با ما توافق امضا کرده‌اند. آتش‌بس داشتیم. قیمت‌های انرژی کاهش یافته بود. و امکان وجود داشت که اگر ایرانی‌ها رفتار مناسبی داشته باشند، از یک رابطه بهتر با ایالات متحده بهره‌مندی زیادی کسب کنند.خب، چه اتفاقی افتاد؟ آن‌ها رفتار مناسبی نداشتند. شروع به شلیک به کشتی‌های تجاری کردند. اکنون، ما می‌دانیم، زیرا اطلاعات بسیار خوبی داریم، که بسیاری از مقامات درون سیستم ایرانی نمی‌خواستند این اتفاق بیفتد.آن‌ها فکر می‌کردند احمقانه است که تندروها دوباره شروع به شلیک به کشتی‌ها کنند. اما این کار را کردند. و نتوانستند آن تندروها را کنترل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24496" target="_blank">📅 19:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597407c8b0.mp4?token=pX19_0fyP8EsCoQHGqNUZdoD1G449cdmJTNO-uMlvH2ZUcjwaCARmtHBBMbBi4joC2lAn2JFSfY697yWGGHRKugJLRsVGZ00qx0y2GOuk9tl4Tw5kbbdYDFDcGz2QdHoTJwmS0RgyL3qYrRZyRUd4BZGhavllmTbB5CcA_NM8q0hchoPry6YqJKCVTa-MEHrETJlVr6uhYpTs4c7_Mu9pS_K52-eB3zJoMB8EGQXqInd4yGV0iX39xez-NbZvrni_-5jJmcN6YNMV9T89Wy2NA68h5y7VRduLbi-0zDoFSzRjHwOWBLLMXNkzAu12w9ta0q4f8_pjs5uVJTfnnI94w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597407c8b0.mp4?token=pX19_0fyP8EsCoQHGqNUZdoD1G449cdmJTNO-uMlvH2ZUcjwaCARmtHBBMbBi4joC2lAn2JFSfY697yWGGHRKugJLRsVGZ00qx0y2GOuk9tl4Tw5kbbdYDFDcGz2QdHoTJwmS0RgyL3qYrRZyRUd4BZGhavllmTbB5CcA_NM8q0hchoPry6YqJKCVTa-MEHrETJlVr6uhYpTs4c7_Mu9pS_K52-eB3zJoMB8EGQXqInd4yGV0iX39xez-NbZvrni_-5jJmcN6YNMV9T89Wy2NA68h5y7VRduLbi-0zDoFSzRjHwOWBLLMXNkzAu12w9ta0q4f8_pjs5uVJTfnnI94w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ، درباره جمهوري اسلامي ایران:
جهانی وجود دارد که در آن می‌توانیم با تهران توافق کنیم. اما این امر نیازمند آن است که مقامات ایران رفتار مناسبی داشته باشند. این امر نیازمند آن است که مقامات ایران به تعهدات خود در قبال ایالات متحده پایبند باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24495" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b80bc12f2.mp4?token=eKtFbb6fi9oK68wXJvaHk8hIXyzwG7VfV0znrnLeD3XWmGYTSoNrSuuw6jUqEOngagfI08Wqn-6N6K4A5EbCPpJBp9vqcn8z1Hu9ImerVvywvO3JYpHmd2rZwevJUp_d35RoRGkfqxdVoriC5IvR9RE8d2OVQFVlWWryiwyMq5rceZhwEAR70EgmYJBU7p6qe2LPjgHFLIuhv1mtEV1UNFwn9egt54NlToiQ365f-EL1HGqQmTt5U_USzrh9jKPLKO62H-1NEB3HXWXELU2hc82JUGotAGFmmVbAG146p3UBa9xRpSssWElJVSpsOUPFEzx99fHM5XL7w0sJocHzSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b80bc12f2.mp4?token=eKtFbb6fi9oK68wXJvaHk8hIXyzwG7VfV0znrnLeD3XWmGYTSoNrSuuw6jUqEOngagfI08Wqn-6N6K4A5EbCPpJBp9vqcn8z1Hu9ImerVvywvO3JYpHmd2rZwevJUp_d35RoRGkfqxdVoriC5IvR9RE8d2OVQFVlWWryiwyMq5rceZhwEAR70EgmYJBU7p6qe2LPjgHFLIuhv1mtEV1UNFwn9egt54NlToiQ365f-EL1HGqQmTt5U_USzrh9jKPLKO62H-1NEB3HXWXELU2hc82JUGotAGFmmVbAG146p3UBa9xRpSssWElJVSpsOUPFEzx99fHM5XL7w0sJocHzSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا: ما معتقدیم رهبر جمهوری اسلامی ایران زنده است. برای اینکه هرگونه توافقی میان آمریکا و ایران امکان‌پذیر باشد، ایران باید رفتارش را تغییر دهد و به تعهدات موردنظر آمریکا عمل کند. @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24494" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8091040c3.mp4?token=qF-uqKXgc8s68glZwYzAigPWDisfEKbdYZwdACi3UQEAQYmaBZdaAkNY2VyNl5AM22z_mp5k8R3kxsQio0iZrmh_bknjrsnu-_wC0xsA4a5iwbGLyD45BKnCelFOfGs4oNc5m8MPuLBBvcAK5f1_1cZu5lxUj_tHSqSoCTI9ghx4YFk6LIc1C9uM1FdEbWs4WjwqvYbiEdG6CqTfJTqDUjH6fSCYyAhgrTk-CWiIb-7ymSlweAZB5hZhD0rbaqyKtpNHY0Fogomcqxtku-VsOSQoUj4yTczFTMjnVI0Cg0d_vhqBXEykUqHgvz-ap3d3Y1yrNljI1QoTHu2T0SOJrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8091040c3.mp4?token=qF-uqKXgc8s68glZwYzAigPWDisfEKbdYZwdACi3UQEAQYmaBZdaAkNY2VyNl5AM22z_mp5k8R3kxsQio0iZrmh_bknjrsnu-_wC0xsA4a5iwbGLyD45BKnCelFOfGs4oNc5m8MPuLBBvcAK5f1_1cZu5lxUj_tHSqSoCTI9ghx4YFk6LIc1C9uM1FdEbWs4WjwqvYbiEdG6CqTfJTqDUjH6fSCYyAhgrTk-CWiIb-7ymSlweAZB5hZhD0rbaqyKtpNHY0Fogomcqxtku-VsOSQoUj4yTczFTMjnVI0Cg0d_vhqBXEykUqHgvz-ap3d3Y1yrNljI1QoTHu2T0SOJrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
در سال‌های پیش رو، آن‌ها تاریخ کشور ما را خواهند نوشت و خواهند گفت که جنگ ایران یکی از مهم‌ترین کارهایی است که ما انجام دادیم.این در واقع یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24493" target="_blank">📅 19:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fe3fdc3bf.mp4?token=lc9Ftwa_VgFiNCYqpoM2FU4KdGQ4adK5wQK66hT2fLBDHhY_Vyn33ldTHZ_kRNihGeLd19Zk75OX8soAtLIabfF52zbhDjusnidsbtmgeiG4xVBwF_nUccOdRorP_sryLulRPBDLx4sWxvCM2GIRKkQ4yNclz2AWrUlyp_-Kyo93WNMmVK8hzHS516vIAzoo6A1gs5x6gDac-9USEWgpNaZhXMmisIBU9fiBji8fZd4hGVvFINNrOY8UXnDe9xamSU4_2zGqrzVxhYBZYT5XkqcrmtCsGBekTRFC-9pw8WBgl83VBQuo1yjFeVo-9DDN0f57vpQk_7p2Dxdn9FBZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fe3fdc3bf.mp4?token=lc9Ftwa_VgFiNCYqpoM2FU4KdGQ4adK5wQK66hT2fLBDHhY_Vyn33ldTHZ_kRNihGeLd19Zk75OX8soAtLIabfF52zbhDjusnidsbtmgeiG4xVBwF_nUccOdRorP_sryLulRPBDLx4sWxvCM2GIRKkQ4yNclz2AWrUlyp_-Kyo93WNMmVK8hzHS516vIAzoo6A1gs5x6gDac-9USEWgpNaZhXMmisIBU9fiBji8fZd4hGVvFINNrOY8UXnDe9xamSU4_2zGqrzVxhYBZYT5XkqcrmtCsGBekTRFC-9pw8WBgl83VBQuo1yjFeVo-9DDN0f57vpQk_7p2Dxdn9FBZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران سلاح هسته‌ای نخواهد داشت، و آن‌ها خیلی بد، خیلی بد در حال شکست خوردن هستند. این ماجرا خیلی زود تمام می‌شود.خیلی، خیلی زود تمام می‌شود. آن‌ها سلاح هسته‌ای نخواهند داشت.قیمت نفت به‌شدت سقوط خواهد کرد، درست همان‌طور که قبلاً بود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24492" target="_blank">📅 19:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262002a591.mp4?token=oMShyR9sFxwxgxWOAbj7lAkg0tiPnOcI4AdhiUjxNCDxEVlfDIua6S-9oD_5GhkXzvbvYsvU-Jmj2tTJPaSWhqsVFz8wjf4wr48aFXbwZI7geN-gdz_k4ArUC3UDlf37U94MyzVYcAyU_5t8rYGMFSoVQjM1bgIQRqgYLeAAjoHTpH4DnGChzknlWtR_EzXQf-3skPnAv4riqFdaSBdYx3199oQep9heiRtDH5ej6pSQ8MXJDdZIVaHOSU1E3HyjhWL1CWAM6Rrm-7NhdcVT8kLKuwauST_Gq5k-wvkQql_kE0HoijH8WjLkdCPKbNnrEQ57R4dIGHTaeFajaFWV5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262002a591.mp4?token=oMShyR9sFxwxgxWOAbj7lAkg0tiPnOcI4AdhiUjxNCDxEVlfDIua6S-9oD_5GhkXzvbvYsvU-Jmj2tTJPaSWhqsVFz8wjf4wr48aFXbwZI7geN-gdz_k4ArUC3UDlf37U94MyzVYcAyU_5t8rYGMFSoVQjM1bgIQRqgYLeAAjoHTpH4DnGChzknlWtR_EzXQf-3skPnAv4riqFdaSBdYx3199oQep9heiRtDH5ej6pSQ8MXJDdZIVaHOSU1E3HyjhWL1CWAM6Rrm-7NhdcVT8kLKuwauST_Gq5k-wvkQql_kE0HoijH8WjLkdCPKbNnrEQ57R4dIGHTaeFajaFWV5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار ۲۵۵،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24491" target="_blank">📅 16:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14e804573.mp4?token=YxXUyqaxlO0QiYR2XqbV6jkmkhM1nU8IcS9Ctiol56zAapupuHnn-Mn6Bx_11Nh517zWoiMGOM3Bwuz5YaTPRMwRpHF045vo8nqY-otlEhyaN-cICrLOmxsA0QDkftN7dCGAbMmyXHKhpWa1KNkshmShTKBlTKEvRAy_8wL0dm_vxNtXtp4nn_w97moPSLXfKcgnhS9Zam3PAnBLMzRUio8wZtbT-4Rm2KPUCOshtaEYqrO8mRoXgQaZyA2uxlFHTSfxJebZ2GvjkGGCl5zafaWSVB_FYg5lh6fAao_6uc7dAfnrKFp7UIXgL4dv73nGc-39J29YX4MPNWNxqK5ozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14e804573.mp4?token=YxXUyqaxlO0QiYR2XqbV6jkmkhM1nU8IcS9Ctiol56zAapupuHnn-Mn6Bx_11Nh517zWoiMGOM3Bwuz5YaTPRMwRpHF045vo8nqY-otlEhyaN-cICrLOmxsA0QDkftN7dCGAbMmyXHKhpWa1KNkshmShTKBlTKEvRAy_8wL0dm_vxNtXtp4nn_w97moPSLXfKcgnhS9Zam3PAnBLMzRUio8wZtbT-4Rm2KPUCOshtaEYqrO8mRoXgQaZyA2uxlFHTSfxJebZ2GvjkGGCl5zafaWSVB_FYg5lh6fAao_6uc7dAfnrKFp7UIXgL4dv73nGc-39J29YX4MPNWNxqK5ozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آشنا نیست ؟ خودمم ندیده بودم !
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24490" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرگزاری آناتولی:
یک فروند هواپیمای
کاسپین ایرلاینز ایران
به شماره ثبت
EP-KPB
در فرودگاه استانبول به دلیل بدهی حدود
۳ میلیون یورویی
به یک شرکت خدمات هوانوردی ترکیه، توقیف و از پرواز به ایران بازماند. شرکت
ACM Temsil Gözetim
به دلیل طلب خود علیه کاسپین ایرلاینز اقدام قانونی کرده بود و پس از صدور حکم، وکلا و مأموران اجرای حکم در فرودگاه حاضر شدند. هواپیما که مسافران خود را سوار کرده و آماده پرواز به ایران بود، با دستور مأموران متوقف و
مسافران و خدمه از هواپیما پیاده و به ترمینال منتقل شدند
و سپس عملیات توقیف هواپیما انجام شد. روند حقوقی میان کاسپین ایرلاینز و شرکت طلبکار همچنان ادامه دارد. این هواپیما یک
بوئینگ ۷۳۷-۵۰۰
است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24489" target="_blank">📅 16:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
ما معتقدیم
رهبر جمهوری اسلامی ایران زنده است.
برای اینکه هرگونه توافقی میان آمریکا و ایران امکان‌پذیر باشد،
ایران باید رفتارش را تغییر دهد و به تعهدات موردنظر آمریکا عمل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24488" target="_blank">📅 15:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBp5pI3VduE5YlAu3EI9sexsIU-fHUdLEyGsQYNgAW1H5BffoglKIakC6afzGHCOFeXF6AIL6UV85Bz3EiFyC0kJDg2nXqjfKVzcJUw9lywdmO8wfwdJUnz8M-t_nPjnrlKk0ksVq1aAxANwuaVnYHELuR28KbRbcygu6ObOyOxIcoHhP47kz_GqkrIMesCmZRLzdQjKU8kw-ITVC7dIJoWnHb2MrATo8rE3WLjpyMBK3kSZ6eZ-WdoLICrA2g7taUo8IHOHZI6ZrahbjylH8vRw0cLOemzQDCY8DcfPhGOmsO4lYNUZ53QqQN-MsTAEhImS8erM-kMIbvCSn-C0Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان ۴۷ هاموی و ۵ کامیون از آمریکا دریافت کرد
ارتش لبنان در چارچوب برنامه‌های کمک نظامی آمریکا، ۴۷ خودروی هاموی و ۵ کامیون دریافت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24487" target="_blank">📅 15:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8fb30205.mp4?token=MOlxFYdl2M0v_9aM3DU_8haE1TjczhMFQOY34JB6ci-caC3QvBXLxV8ndzFy_g_yc4jhmz2yskTk5PAGgF7_t2Tub2WMje8Zh5xvYaCIKeQRTF3Hkn7qPj3YoxT3o7fXEB2Ehox1auiR0d1_jt1PAJT4kbKayFrg_42PYSGq0YsvC0yxx-hN5PuHZKrwj0KUrMEuCFjrUmaNaA3TuzAId2XcVxG9WTkx2rxkzN_SwAruY1E2YD8gVRRG6yBXAC9CZqqQbwnzH4z7JkZjeLkKE59HZgtWEwq0YW84_4ShQ9ybwTLIFNV-yMbp9uxsFBvPKRKq7qzqiMWVvrrL-67y4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8fb30205.mp4?token=MOlxFYdl2M0v_9aM3DU_8haE1TjczhMFQOY34JB6ci-caC3QvBXLxV8ndzFy_g_yc4jhmz2yskTk5PAGgF7_t2Tub2WMje8Zh5xvYaCIKeQRTF3Hkn7qPj3YoxT3o7fXEB2Ehox1auiR0d1_jt1PAJT4kbKayFrg_42PYSGq0YsvC0yxx-hN5PuHZKrwj0KUrMEuCFjrUmaNaA3TuzAId2XcVxG9WTkx2rxkzN_SwAruY1E2YD8gVRRG6yBXAC9CZqqQbwnzH4z7JkZjeLkKE59HZgtWEwq0YW84_4ShQ9ybwTLIFNV-yMbp9uxsFBvPKRKq7qzqiMWVvrrL-67y4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
دشمنان ما ممکن است پیش از انتخابات به اسرائیل حمله کنند.
در هفته‌های اخیر بیش از ۱۰۰ تروریست را فقط در غزه از بین برده‌ایم و در لبنان نیز به عملیات ادامه می‌دهیم. اجازه عقب‌نشینی از دستاوردهای نظامی را نمی‌دهم و به دشمنان هشدار می‌دهم که بازوی بلند اسرائیل هر جا و هر زمان به آن‌ها خواهد رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24486" target="_blank">📅 15:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا به دولت عراق اجازه می‌دهد پروازها بین عراق و ایران را تحت شرایط آمریکا انجام دهد:
. پروازها فقط از فرودگاه بین‌المللی نجف
. پروازها فقط به مدت یک ماه
. پروازها فقط از طریق هواپیمایی عراق
. باید اطلاعات تعداد مسافرانی که جابه‌جا می‌شوند، نام‌ها و شماره گذرنامه‌های آنها، و مبالغی که هواپیمایی عراق در ایران برای سوخت، تعمیر و نگهداری و سایر خدمات هزینه کرده است، در اختیار آمریکا قرار گیرد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24485" target="_blank">📅 15:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCOXhPWNC2cT96E0wQ6U9LEZkZv5WUtTwVQOCyM8nPrrjPU9CwfrH9BRjliYLtbIm4027wvUatRSi8okScq_OS0bVfFKWeo3kp0147QYxD5nHKJJTEqoauXxcofMASi4mBF23lwOsvBZh5UUhagFfC71XGkyZELH24STd2cHgta6rbN76ApVWPAfe2TyAL96VJFOUJERmgNRPY3_YBDtYMvawFpELSXaqMR9R_Mj0HsIiPqUzE2tUGH6Y7naymzfCw113MapKFPtFaF-0To0tWlBTCFPglGWS8fcz1HWsi2bjZJMC-3etgkaJlgEFkniZNnF0XrDYqzA6fGIX_AbeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دریایی UKMTO: طبق گزارش دریافتی، در ۲۸ سپتامبر یک کشتی در تنگه هرمز هدف پرتابه‌ای ناشناس قرار گرفته و دچار آتش‌سوزی شده است. آتش مهار شده و کشتی در حال حاضر در وضعیت اضطراری نیست. خدمه سالم هستند و گزارشی از خسارت زیست‌محیطی یا میزان خسارت وارده منتشر نشده است. از کشتی‌ها خواسته شده با احتیاط تردد کرده و هرگونه فعالیت مشکوک را به مقامات دریایی گزارش دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24484" target="_blank">📅 14:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فیلم جدید The Fix با بازی لیام نیسون (Liam Neeson)
، داستان عملیات مخفی برای خارج کردن «مریم رجوی»، دختر فریبا رجوی، از ایران را روایت می‌کند؛ که در ازای نجات دخترش، اطلاعاتی درباره شبکه مخفی آمریکا و وقایع سال ۱۹۷۹ ارائه می‌دهد. فیلم با نمایش اسناد محرمانه درباره
خمینی، دولت آمریکا و سیا
، روایتی جنجالی از ارتباطات پنهانی آمریکا در تحولات منتهی به انقلاب ۱۳۵۷ و سقوط شاه ارائه می‌کند و همچنین به
مجاهدین خلق (MEK)، باج‌گیری، خرابکاری و ارتباط با قدرت‌های خارجی
می‌پردازد
منابع معرفی فیلم نیز تأکید کرده‌اند که بر اساس یک داستان واقعی ساخته نشده است.  مجاهدین خلق  پول خرج کردن باز بیان تو هالیوود ؟!! باید فیلم را کامل دید…
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24483" target="_blank">📅 14:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دلار تتر ۲۵۲،۳۰۰ @Waratoom
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24482" target="_blank">📅 13:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دلار تتر ۲۵۲،۳۰۰
@Waratoom
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24481" target="_blank">📅 12:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وال‌استریت ژورنال:
یک گزارش مهم از کمیته تحقیقات سنای آمریکا می‌گوید
۸۴ درصد از ۸۴۶ کیف پول رمزارزی تحریم‌شده مرتبط با ایران، عمدتاً از USDT تتر استفاده کرده‌اند
. گزارش مدعی است این شبکه‌ها برای دور زدن تحریم‌ها، معاملات نفتی و تأمین مالی شبکه‌های وابسته به ایران استفاده شده‌اند. موضوع برای بررسی بیشتر به وزارت خزانه‌داری و دادگستری آمریکا ارجاع شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/24480" target="_blank">📅 12:24 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
