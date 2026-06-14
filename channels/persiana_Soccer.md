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
<img src="https://cdn4.telesco.pe/file/ByJo-9dl89Khdp4gk2KH5hMFuiT452PcrZi90zHfIs75IwHbZB6rYJgkT6DzNhuVUQoDv832gkclwpTzaX_cysIlIBR8AIPACTNcGXlJybR-IsGuR3Xe3ti0whTYux6uUjSzM_lIfb5wacgCk1lC7CbfBBSBG1aIXU4iPCbFZg9mwI3QifZAYkNM20cAViU1OOjuFS_VXvdHPPtJ0leyyzOWpPPBNcDr3DCxXfqRpYqcgJPFWZBhRBgnVBgF3RyNVTuOt9jCPuheSRZJeM3isMkzZeklhwwGCjVg5NVQfu2iuTiS-3XFjc08PfKdr-V7Cpv8labVVcMU1yaJz1p-Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 245K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 00:14:42</div>
<hr>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDn5avfzB5kdz36xohNC6dkU352tRybQCxVxsSCFFxN3VWUz-tYQJtiMQOu3t4fXxtMpDpcn-IW2S9UFeLUn6QYgnN74-KrXSLplCzoq4MV0kDudqvc5XzS55TOmqfW3xp0e2C8ApZ1I9j3y8ryE8uMWLZ9f-K1xpyaLW9x8sUpvnrwpGpz-rwItHFLgeckgwcnxJvcktjDo9TCxEwG1KU06OnwEAW1-tc1fVxHMRGycQkSDVFRvleg9JMWkhR_i-YSy9UEgpUkKbJNxPNwOPc2u0ABdBHIpRbkqXt2chip43J9ylUlkbs4ulsGP6-ZEOO-Wfa9Dci63-eGCQY7OBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/23469" target="_blank">📅 23:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8H_gPz-66xG75eo3HHD6nnx6goSs8tIRDmT1HMjxM--06BTEx3Fu0rWYfi_LoZ4kzOJw3wWSHAdP_ZFMubq0i6__jLSUbcyhVRnnEbrAjb9f_r6itAFNqfmp0_dnEveeBKnwttgxoETCC6LrtYCEwOP0xswLm9k4gTHuc-N0jH-0lizHpWiYPW8l16UfCFv7bajxEBlxy9G1hxHxQQroGTA5ruFdgDCVdyHDd7l-RG70GFlWVYiOVac8KMPe0DI6ELzm-Hc2oAlK3igTinG1TBUSupaM121NhQr-lbAnQ2YGfdhQBQ4gSEUVAybU-IKTISBscJeodlc00-E9Sd8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاریخ‌فراموش‌نمیکنه بچه جون؛ یه زمانی برای یه صندلی اینجوری داشتی خواهش و التماس میکردی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/23468" target="_blank">📅 23:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmNLS0NQ7OP495AZdi-DFq5nTswnzJ4PJAGOPTUWtz02VBcAB5cTe1N5qegENye8vKTRg3VNUwi8jpifIuGq8JS-BzBmxkvAsgM2haZca9iV_JULP4BtczVuL6Q7E8Z8Ww7PbYPbOtoB8kMwIWRu4rm3c5eP6E0GYlAU8M4xB0f8-rFl3d2Yf-MHGuOP4mC30WZCyWOciisG9kRKUQ-rY3z8OGeCy_Lj4XkFa4llwyNCaBcGzgYeHMWMzt9Z-AmCfyYLT4g8C5eKtHG_QOo-isfHkL1RzBeB3vIwJroP4DlX9QBQ4xEUzjAzWJj4UidkRqKh_CWRPngKOK4refvkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/23467" target="_blank">📅 23:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=jGBqK1Fvvq3cAkXD7OPWm6o4y7JzaOGCP26fABGwsr9PXi3ZX6VFkDS4Cwp4Z60PI4KS6_uPTVmHDDLqLeBR1Kp4WawMHEh9fvJmjL2fVqGHBC6vCcL93H6y0ATDLVOTWqzXwwG50zJl1O0zpPQL4SHwC9y9NkC_NV9ZkYOALYxNz0mczmnSdUQLwqTus7WLEkVKxZBXV87w7g27sh_plY5xAkY1efzxJKKFmZEWZ_VEHshQyTVawp04uEFVpn87UOGLuAaury04hqGHjPZaNZ_aKHQ39U28TTNHJVA00OYSda5sCfApp4Uh1xokO9A0SeUrlqJdMZWPhE4RdmmryTOtptd74jmnRdIq1ljZagwtcUJDTczFpSv7EIrwLV5npW1iKGQ-WUzKPKlPI6BCwzeQ1r9v-7dZt3Bj_UHL2rlmgQlDhjw6JRlnCp0rtPl_aVw0KmWtgwtKdFEsJ5DzL7Pa9s2ja1ijtoBvXuCgSZAjvaXfU-PkfMOW_WRfQ0ux0DWdA88JuRA--9Yk8I8Ebd_-3H7MZB9EkBTtxYPQ_UIWjwJq9Ws9Agcdm9zT_Mt2Pzm6FM7vf24b3K8Lfb_0_Q6f_zr-xc73K5sTKWLRiPqbBPHfdDKYoA0VfMHYDeWTAjDwIrnYwiFBORcizE17EU0vf4-gl90Yj4u7gY65y_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=jGBqK1Fvvq3cAkXD7OPWm6o4y7JzaOGCP26fABGwsr9PXi3ZX6VFkDS4Cwp4Z60PI4KS6_uPTVmHDDLqLeBR1Kp4WawMHEh9fvJmjL2fVqGHBC6vCcL93H6y0ATDLVOTWqzXwwG50zJl1O0zpPQL4SHwC9y9NkC_NV9ZkYOALYxNz0mczmnSdUQLwqTus7WLEkVKxZBXV87w7g27sh_plY5xAkY1efzxJKKFmZEWZ_VEHshQyTVawp04uEFVpn87UOGLuAaury04hqGHjPZaNZ_aKHQ39U28TTNHJVA00OYSda5sCfApp4Uh1xokO9A0SeUrlqJdMZWPhE4RdmmryTOtptd74jmnRdIq1ljZagwtcUJDTczFpSv7EIrwLV5npW1iKGQ-WUzKPKlPI6BCwzeQ1r9v-7dZt3Bj_UHL2rlmgQlDhjw6JRlnCp0rtPl_aVw0KmWtgwtKdFEsJ5DzL7Pa9s2ja1ijtoBvXuCgSZAjvaXfU-PkfMOW_WRfQ0ux0DWdA88JuRA--9Yk8I8Ebd_-3H7MZB9EkBTtxYPQ_UIWjwJq9Ws9Agcdm9zT_Mt2Pzm6FM7vf24b3K8Lfb_0_Q6f_zr-xc73K5sTKWLRiPqbBPHfdDKYoA0VfMHYDeWTAjDwIrnYwiFBORcizE17EU0vf4-gl90Yj4u7gY65y_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی وسط‌پخش‌زنده سرودملی آلمان رو خوند خداداد از خنده کم مونده که پخش رو زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/23466" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی2026|جشنواره‌گل ژرمن‌ ها مقابل تیم کم نام و نشان کوراسائو؛ شاگردان ناگلزمن در ایستگاه نخست رقابتا حریفش رو هفتایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/23465" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO_-L-YpaDK-QWcwmXTQFcejECtsmMAPAvTk1CbBUXdCTxIqJP7ZNfkSUWL_GUI9JHx71UxKDPrHt8_tE_9Lc7ZjSfwQrhw2tbAFb9zSEBe-BUf-b7q_t0o9M6IlmNV1mjOu80Wlor8PGeEAeBGaSKeHDXjojTV1coFA4-Bfvae2uRjyoZKyPaW1OmmlT9_4mx9MU6YSY_SjqO_b-S5FdrQUEwIW80x3KfjJPFykoCcnxYePiplSBpoZXy3peqhv_pvGvDXbNZ7dPnk-347OgRqODz0orczIyuVFzEaVFlx2dx7p6sNjw61KneVZ9u9RUCT9qalyKfSWXSUGpSdSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/23464" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_bVHfdUM2rypNlgEMX-NEvfVFZf00WuhDA7kELoFzxA8H4BTbFnGUKss71Lf_AAMw0IlSE1ilcFqrTDCGR2mesHFiiBx6xBjRaIy4H7vGuBk9mMY8MRlHrzzfdlHYHtxAnivvXnThXC6_g4p8NS2NUMqaFo3gLRCDVqqXkgvkoEZMZYRFlIx-FKCa-oW5vAA0XUO0LVqHseZjwexgCzLd882ON8V2c2A6yEuntncQb-K8e41ajSSJ0ck5zOuWpix2Ci4cCNM8kJZJ1Stz3Rx2RUZ6Fpd2-YnAv7f94NbYU5usFpuGtxyKRI3vJewBzADOEoo4fLqDbvoyUVmoEjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nw41JFDT7y69H6K7NI9MFzbjnkBgMV4J3vVdy-1DimgmXGNzzlr5G8csF3n5YtGIXpI2rtrdbzfzC2FZooX1wUb8UBdS2LPohb-seJTiOR991XhKIAhonar_tLydWCOfDozXWb77HD9bs0jY8-xbrhAWsa5CYRlnT48OOYxJbQOFzKdz-SN5_cGYqdZ5fMdeRz7JWlOQy52oXDDo8vwht63PoC3UReBJvPJQWZYMkkKgm3EW9nsccfBIVBZmCtIcYeGz2EKrDYylJCBtD6_30XeOHde0nXcKoA0jPKWj6AoN2AsYZRlvGolLCIdekB4-AuCwjV1VyE4NWA4lgsPnmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی
؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23462" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4oaCp0L7ezMBTrKgdVDvcnf5PG2O3e9-EbuLGioRT5ZgzdbBq4uf2bNkhOYovqhhn5U13RJIgQyYKAvxXRxe_OKpEx7Y_TJt-ImhsNc1Fq1YxmjRS05mBLsqhED5A43gYub0R5fABI2tU0gxsNfV4y4vjV9SUKwyhjrBZeUf6rw3DXpDxfCB2BwbeE4wM66mJJkAwx78_SManRh5wA91D9ouFJ6fO8LO7UHbk4X-9XNa2buVyrxyGqkoMWNmDFikH-VYVTv3uY2LJrmZo60_oQleJn11xtuu1z_Eg6F8Xu0RTcSz-iDGXu9S802AoBT1CkkjR4gE73sn69gE1xcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/23461" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=iESBe4mTYHNyjKbAAwUUOLS2x5t1X33GsGAiZr0KL41A0OmASQcpeuR0vcOfhWjmMbnB97PzLR9H3BcHkaB0cfwvU9BIe1ZyA2aLDmPTCS1avV0PKEOPNlZuQyym-txXFJ36QEpL2yEMkZnEKBeD9F9rh-QqkrfBfGA7sQCElBGCt1FGbrP0wd635wEZO5IVk4IyVJ4f1R3PwhmI0K1nLE3r1mNBVdsuqHTdf0dhDhUoOfCIcbE2pC2HSNSI2iaU2QtBdqK2H_AGKla6U68-pyXKw6cHppmF-rA3VmZOnNiAHuePreca07BA8vGOHww7cppzuKYxETS0Cw3Cbq7aEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=iESBe4mTYHNyjKbAAwUUOLS2x5t1X33GsGAiZr0KL41A0OmASQcpeuR0vcOfhWjmMbnB97PzLR9H3BcHkaB0cfwvU9BIe1ZyA2aLDmPTCS1avV0PKEOPNlZuQyym-txXFJ36QEpL2yEMkZnEKBeD9F9rh-QqkrfBfGA7sQCElBGCt1FGbrP0wd635wEZO5IVk4IyVJ4f1R3PwhmI0K1nLE3r1mNBVdsuqHTdf0dhDhUoOfCIcbE2pC2HSNSI2iaU2QtBdqK2H_AGKla6U68-pyXKw6cHppmF-rA3VmZOnNiAHuePreca07BA8vGOHww7cppzuKYxETS0Cw3Cbq7aEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های ابوطالب‌حسینی به بعضی از مجری‌های بیهوده،دلقک و بی‌خاصیت صداوسیما فعلی مملکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23460" target="_blank">📅 21:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8GDHVyMSwB0WaxHyAe3A98BVZl8XsuMYSno4R8oWUJZrNAPTG-aZSU1hs_GnZKUArQ45HinPGz9meyUjVx9RDsZ2e1QSdA-Wnc-rGhtGtwFRW6-eeGQpP65AzdEFzgcTYc8W6f5LMywJtGL6-QSD7aGJk9XPqK6Jr38Z6VLdsdiI31MPXEYuMstCjKwZr0sCCVx_cVAhSdAhAMojV2DVhPjmbVsousvAN1knxc6sYJNEvU68banakZugdmebx1wFdp3XDrCfP2ATsjG_d0FRGwfioZZa7WVGPmAf2pomRrUJcqeU015f6X85Nuvm5LKcU6sf71JKqNIiIla9dcg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اصلی‌ اینکه اکثر بازیکنان ایرانی خارج از کشور علاقه دارند به لیگ برتر برگردن اینه که چون شرایط کشور خاصه و ممکنه در هر مقطع از فصل جنگ بشه و بازیکنان‌ خارجی تیم‌هاشون‌رو ولکنن برند لژیونرها قصد دارند با رقمی بسیار نجومی تر از دستمزد فعلیشون در باشگاه‌هاشون…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23459" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeXlkJvKbMl_KSpxzqHjbinfsmTO2LWnh8elmyd6a60twbbvOExWK8dmnD67Xo59gbqnq3uH5lhBZZLAgD2eJX1upDMgdvzkeClJxA2Gb-hZ3r9WXG_QtzRW7pdvNHcxSl04y8Uod3JjtdfVxJkj3ZHijJUW6zI9PPJkZdD1Gg58ujMFFHMuLlLyK778EmDu1m_PEwDA56-igZoYdk_jSBlJ_LwZQ-Ng0VU3N9rgEQM9vMlx8tFarpnvajsDNzhrGDV27kFFiedYVne_1CtDgDubXW0kget4PGTSN2mEau__sYJuF04KrUkBco5pUTTipHxohzsj5TEaqZmJUo4YPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ اولویت اول رضا غندی پور مهاجم 19 ساله الوحده امارات دراین‌تابستان پیوستن به باشگاه پرسپولیس است و درصورتیکه کادر فنی سرخپوشان روی این بازیکن نظر مثبت داشته باشد جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23458" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-9mrTb4rS8JGwe1eYAkWQYsJHodWhqqyQDb_TMn3crB9_qaNX7h-N3pSy7L97zfE5P5s07suH1_NxCi2JwxGEFBKGOilNMV9PgGjmni4PmWfmZLCHYrIrZV0kOOd4r0IKkR9jW4MUXvvil6bTcdJWytKvnTDq4IlOTTN6XzB8MwmntHGE2umgwZi2EASpf6ePmeYlMAC38phZbqdXKu1zdA8dfCmIwv4WXxNNTxH16vLtarA3A9ltf4NPtN0EjS3FqET8QEfNi6c9DFZs9Rrq-iQhG1P7OnSCiy4AdLWaUQGl-MA1B7y3coBgAxizMzfj4XwfOT99dHaLAaqHC-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23457" target="_blank">📅 20:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvX9BJ7OjLLASqYWuqI4uYPEDyf5qHOM7IscyyL6QzqElCEzBAt-TRSxA0mNYR-QwhVVw2ZRhYyOTKIU3cHckrZYQ_R1cnbLGjJ-GNWwoX8RsFCn9LGKpI1Wobuk2Q2lscuc9V2Cv1a_E2WILnkKOmwkaN2uAgMhMGibIN_V9YNs_BMyr1bVQaxoTO_8nucZ2DST0yENj6rQPKPkBqOeVEtelI6TNymlntjwI-Kug5DkMpQKcI_MC9EvqdyA6IZwQt7xsUFjP3K0PovEF8cG9TbAee-_IhSSwxJzB52OCs5MkjLwQwjn93hb2d4mnUvHRZQT5Wxzy5dhbtAGeB5VOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چهار خرید باشگاه رئال مادرید در این پنجره تا اینجای کار؛پرزبرای جذب‌کوکوریا 50 میلیون یورو به تیم چلسی‌پرداخت‌کرد.درحالی کوکوریا جذب شد که اکثر رسانه ها خبر از اومدن کالافیوری میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23456" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=kV6i-q5JqATGC0EGqHNCunlZF9NtThqVHazTGADyuExm0f8yEFosO_iFqdECUyV44mmAlesD5B6icky9Xj5zyCy1SlhvR3uvSo-ZqIPnp-1zkPaA9pF3qqPbg29e0kixZ_u7Gsz7H5CZQ0UoaWulJFKQjszDPBExYXXSsU__XJKLfe9kmkDuisJr2pg80NZCixGR8bDfMcOLHbeQxGy_ft5WaYLCIf3_mJEfMbBvZjxsOamfcPXOaR1Ve1OJE5kS6V23LRSpP7N8eV-iiH8hObXt57klTTsLwgW-IrsZaVJu-XaJ4UBTBLXDJJ8uYC8ao7FWv1qQc8qfQZn1T5t8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=kV6i-q5JqATGC0EGqHNCunlZF9NtThqVHazTGADyuExm0f8yEFosO_iFqdECUyV44mmAlesD5B6icky9Xj5zyCy1SlhvR3uvSo-ZqIPnp-1zkPaA9pF3qqPbg29e0kixZ_u7Gsz7H5CZQ0UoaWulJFKQjszDPBExYXXSsU__XJKLfe9kmkDuisJr2pg80NZCixGR8bDfMcOLHbeQxGy_ft5WaYLCIf3_mJEfMbBvZjxsOamfcPXOaR1Ve1OJE5kS6V23LRSpP7N8eV-iiH8hObXt57klTTsLwgW-IrsZaVJu-XaJ4UBTBLXDJJ8uYC8ao7FWv1qQc8qfQZn1T5t8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شهاب زاهدی درباره عینک خاص‌ش در برنامه عادل و عزیزم گفتن‌های عادل به شهاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/23455" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMsenNJOXQi16lOUTOH0rIG7tApGWIZ-N7kiPRZKfQUAI06clP8xiWKJz4qPVzxmEGjeRsB-vCoQtUsSYMyXfMNqm7sl0Agb5GXOuhmsKSFPg3NiVw0mBlgzQLQqmlwAYkE-geDj6hjZ6xolH1-h_lQKopn_LZHkSIVUsa0fBHNs9PVLY--8TXneana2P1fpe5qtD7WtVnpoPw2KXD6KZEXH-7zXPmRuAv4jiA3dBI_sgdmIiX9oGcD3ZIJBjLImNEBP-vUvOrDD2RWGPK06GSNsmiWqOhTN_glp9e8UJJ6w28Keyk6bXVgaRJlQZPJpOaV0DjqjZs7_VlVCb73wrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های
#جام_جهانی
رو بدون استرس و کمترین ریسک ممکن پیش بینی کن.
⭕️
⚽
آلمان
🟢
کوراسائو
⭕️
⚽
هلند
🟢
ژاپن
💳
حسابتوبرای‌این‌بازی در
#رومابت
با ارز دیجیتال شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
24
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23454" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqUmJSjyb7lPvxyYQ1h5ooQmSBGr_2s8nP354ThiP65nNQiBpJgHxJ-shlzMHavSHSUM1GgkA_9YkpHJ60JAAsCY0PEujEQOyXBFvHeShaJ1frW863L52Rs0TTyI-aHGAO4D8aEeT62Htx2CcS6pXVQK-HM79uGR08LEjoanlnRbq5eOskE-FD8W5VxknHA2i2ZS_nElVRNs3z6FrSj-bWebdAlfRZivMrPqIa_ANnCZIYKM_9frH7Bf77DWozVmIWDflNaq83iGGSboEmf3Fbx78tgvVntsqsONB8SO7dNfm2dSKgDQLITWviwsFNl3sKaWp-YtNG0qLr_F8XdiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
میانگین سنی تیم‌های حاضر درلیگ ملت‌های والیبال؛ ایرانِ مدل پیاتزا دومین تیم جوان این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/23453" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23452">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyg-ANUpF4uk8wiV-UCKktRsRftZLjExTni_sYL2ww-bT1zpQAdanhQeaG8bpqtvC5dAqdBO-V4wqOc-UJZlkr_ygK1lCKnjkusMOUe6kXl1X3PMHX8mcO4FC_BeFYm9X9wduHeoLVbob8KZjS2hQI8OTvhcno_rwWXI08Ugppz1IyziMTii5aUVg1crdAqsb5hX4AnKlf71QgVjFg15QqIYjAadWD6LBMAZPCPgdwOxHO8Eh9QVkJeRKDZ4_WVb7hQRsFurcDL59NSDhtj0wBqSJN-gi-7IWl0nd1KYHFfHvJM94qvlC6MhEeK25pLkZ8iiILyyHRXvA6BtreAPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23452" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u77ejBKK-aFHkMc4a2NzaUyJZzfyypEbmLt5AbdlcXUR3emeICktC50KZiepqkukf2A8k9EoRxNGpgigZOMG3C2fgQgymSizCgGrzH8rc3bPRNJeFv_aQivQPONoCThfsfy_9oT5TAPwwnH7Q60oF2N31SgaZRXnHsaH4_OqOYQrC-3YAxESNOO1eJIQ9mqx01d2zrmO-QWiMMPsXQFWZ7ddt4zoMXmS80RKfYqthDOV0KcGkjU-x17V6WzYaa9qge6895k4whRi3zCDNADdW8MsfMxGrpWEv1Hz2G-oLNlHW21vhirijuF-aWOlSQSVkpay4Ol-Hnhmlb-kvFSrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23451" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlXIDj9e2ls1zwsFITN_AJ0JF4ywLtEDemxFakQ3V7pJle6R0D7ZvhU1nJWIl94TBiI9GOFOtY2VbOXTdhWN12_clzlsgc91o87NcSyI4b3BwJ7TkAkigQHWkHcd-veLXTc7Wn-muTM5XDV98ZX2WAlYBu_OF4oyHQFatLDzudtwiZFeNDXfPO-7btCYPRUVZo_XkjdaNcxdxRohACwoQhKK8v-0ta0GIcV1nAdDMiKi_ymSnUlFTGuu0zpCTqaKQlfwaQoSj5fCFAJv7U3MvKo_TWFNNkX_vwlGOmZI0Z4OLcFkxmU1iH97vOCTLcajRVZCxlzzA3o-XRHLaBbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23450" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23448" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcELFcoRh49nZSUSLgjWXQlQonRplflk6zN56jUJDn44qRQ0eOmRHGGhKx1MqDHiPPX7EBixcSHpLeaea6CMf6_Sf1aaL3Ae4ykdmjAY8_wE0AgJ7cz9ss8VByJEUvHJWzcar5y1lyMJEt_woSKtfnYESNFjAajkwJucSIC0_XaI_dX418rr_MTZpx9q4ZXGs8NcsG7N6gbfIgkYwc_6cqf6KAJvOMGfVgTIbE3A9LNcCIEeAFKHlF8mzaeZ7S2YxxS9HQ7vwYNG4HQA7fXwZJQRF0pn08PXq_jeE_KBirv7XsGGX2WsRCpQfr_1qnuODG0CWcs4IP5V6htbKHs9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23447" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23446">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔵
👤
هایلایتی‌کامل‌از عملکرد درخشان محمد جواد حسین نژاد درفصل‌گذشته‌رقابت‌های‌لیگ برتر روسیه؛ قطعا‌بازگشت محمدجواد حسین نژاد به لیگ‌برتر یکی از بزرگ‌‌ترین بمب‌های تاریخ فوتبال ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23446" target="_blank">📅 18:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi6fiw-NMUSzJ697FiGtKgmC3rgluRaxtzKnJ4ek_NNcsRCn4rZb3EI_3WjetPo0hnvXQhYTfbX-Y_0goHzJ7LOYDj7lLoMxyHUPp5AJ1Q1Q7c4o8xhwX7FEuUvuE33OTx1towBQxUHXKSnZZm4P1xmvghLSrDsvLe2QHmspnL0jMsxuiXwz9dIiwsZ1zbOaBbZHLbcHRFwsfUj3TXr0RJkwezMCe3bP_es1JVoQjU2Vx03iZ62wZZLI6n5zZ22PO287Ko8a57NnxGmYLTmi8HyhV0WUMHcyJGMdURtKMyU95ygxIOMQURekonWNoNMhdY_wro1yH4mClNz_WNMEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdZZoChf1Ca-He2BFs2z73MhOfFaM-50CzFgBJHR9QLiSlCF_44Aj5rnxNj-awLj6eqkQSmtn7INEOdH_l85ea61Ea9qA2NJWGWdLBxmiYGrfXrh8kllMiz27gfTvNmrvg0p0TxdsolInyf8t5YW6AHllncrMzZFMarXe_8-T_zJD1I-oM1J94Q7ceN4qWBzu3BqT6aMXaZpEojG-d8U1dcaybI_4733g1Hf9a7H85o7yqLUcvwjcKp5YniXmIoVy-9f1c1IoNYX_Siwk7vvHCuHI45D85o7jlcSCZrikV31IgS-WWIr_hkFMR8frhvmMVpel_IWW6QFVW4dykrH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=drx-KvI7Tbbm-Yxhl4fLjrKMw-bPm7gY1GxwcSIX4_0Toc8N6SthlphoZEsqW0gPvZpazNoMhntYwFQO8O33g_ZqNB-avbUMWo9AKAgjI6MY-Sr5YesYGUt5U61Ro4bsqXV9bdxWJo5mQ3OOtm-a528HL76lWSNpuSvfINKGQr4FgGv1-6WfGj08QADV-kYSvuSzsjXspoCHm1X4EfdvFjkCb421nEoNC56GYOgO1f1K5V77lNlRk09xEYUaxe7dtMtDbfRfDi7o5dWwVY-do0zVqnscxtT5Lu03OXXxeuuQMAVbilfrVnAuCb5MKuwKQJY28-SdmSUFss0BhAQEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=drx-KvI7Tbbm-Yxhl4fLjrKMw-bPm7gY1GxwcSIX4_0Toc8N6SthlphoZEsqW0gPvZpazNoMhntYwFQO8O33g_ZqNB-avbUMWo9AKAgjI6MY-Sr5YesYGUt5U61Ro4bsqXV9bdxWJo5mQ3OOtm-a528HL76lWSNpuSvfINKGQr4FgGv1-6WfGj08QADV-kYSvuSzsjXspoCHm1X4EfdvFjkCb421nEoNC56GYOgO1f1K5V77lNlRk09xEYUaxe7dtMtDbfRfDi7o5dWwVY-do0zVqnscxtT5Lu03OXXxeuuQMAVbilfrVnAuCb5MKuwKQJY28-SdmSUFss0BhAQEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzRgOx3yTfZ7pKJrUodTfwdK-1X-8tC54o8XvR9G3psfkRKz1VET4SgbiqqN75rLpijA74_GFwQX1LJv2cKBfb23FRKnGhCnl1_vCnO_cjLgO61fBIarfQKrmV6Pq9bCPfQN5Hkva70KAAqF6WSrpBlsnYTITCMC2tLYn_KhNALg80VDjYwVck150K5CDjN0C9sIypE3Z-dxb1IhKeAqon6-DKFPHO0KGUferL2ZRC8LkyEt0NQ0oq73qCXAf96VUubEiWCa9x-AtMwsOxIJ_vP2uXEsTZVGXCxwVlYrX2lT_MXnPfeHu9ohFs0rIolxMeUI7J8OkLGXJ_ULImdrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SduDmkcg0ETonGIE3gJ6n_r3v7rVizqekA2eksh_FpZI2VHO7pT5tkfN_OVx_uJuAFV4XAuHgPQ58JNiv5eaounzAh79D-o7Q16NCWI2DyWoIjTkJEvhy9x7yeGAQyjniWJFsvPBxAb3UYfXkpwoT18FyzMDDxe6Q2Xmg0PCeQwnO50CLcmnx6Yo17SfKQiyShioiIRDwqcncsrsbMpthjoi-jMLqyA-nkUuneDL06tDeeK4JD8H1o_kRsulL8uDYysPT-vUsxKxp-b4lgnML8TH06XGf62cBvPuzFIgwOdFrYe856PZ35FK27wuh3HOJ1jfAZzU8xlMtC0gYQyqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG5Zt57rO3Dp0cezsb6xn-Tabg2H-y0gZxQQOMfIRCKOw9HJeAYKQHrlN62ORD-A1--DEQfXsoSXRtZyv8EVU8Pt9AzfeqY1-T_3vbYrI0c7GNsVE2_ykk-TIHULKUKtXlxHHp3YzJjGE275rafs971kHJ952qyOdcgzq7LBkyNRxTWrNhTUgvR91FmbuaCUa5zxmi77oVjTvAD7wGZH9tkrvV8C5NxzDMJkEvdAs5zZZgXbjGnk71fUownpATsHD2OgPBVa8HPOI18jED8bwRs_tnXDMXJlmyg-lP1AyeC9uoO0UR8dLwX4oHjrCKJq4tOB19X95LwU1ycOGG1N_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7jbQC3gr5qMIpjrLigEcgj2wI7XWNMKVDV3oOeS5Kx071aNaobWBIBUc4_9tUrOk3FSwkA6S-G4j2BM07teUIrFQEtYh2acgnYiTO5G9OLOfBtiLF1Do5icFII0kqGK2OdOKo3yawyNLrtqH6PE5PYTEb7PkcIx-hIayYRafVS1S85gLG3SSqKSn44a_Vvl36lQpNj9DjGmcDpCymQZdE2ggxa1jyoVSiH3dQHNVrwhkzuBJwL-fVQQYD_FUxVloLCAitRkevfZV24VAPaAKgyIF3q0qFjMcmHsDEWCpSEQRRdGvR4g4BOo0aKHDLK9h_I0trY-M7KRVBT3kW9ukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZELBJBh_sES5pLDlAnYIEoZmIuhyqDMPAD6RQLLUWq5cys_AE8FfwucbYDzYXq9PzfqFjGTcW-0jGSA0WrGFH68ceCExJPRbH7szI4gJmA4NOMN1n_NNnYAJmgrzSVCOqXoY1I3NFUcsTClSM_ZiDwgf4501Y_vEtmktD9208PXIu05uRLLGkvZKmdKsAde2OA61EKyUvimYaPCvdg8adksw9Zq1GDYWbRcjgRLNaoTU84AOpl0gN_vWLAN5EEX7qY7FgOwMl0mBWaAj4FSoXz2epir6bPXPRnlcx4jwlGbKG1NITPxhMHWIBg5VWGIxB6jF0QrHp7rq5QHuPz4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=Rc0nnvTo9dtgqzsbzbm50FwsAuoLnvv7XpV7Fkvya4MUYUtU4PXWR8fGu20JKefM65ayR9pWyxUYjaW1_DJTC2TiLNXPu08_mz1g-6uQ3GOX0A3BpjA_MeLPkaBaaCH57CzNMp229bvWbgvxIk-9TlcPsdbY0YNCU6TNc_rgdBJK9DdgimFNr6_5E88aQFuOk_VSgFhkstKUoP4JFxdM-Ho4x5uZ-Mkn1fc0AkUJ5w2_SMLloan_KVe5-fWck9Gy9qhQ9yjSGZ3MYfGTeE8AxyfhE-Z98dPzZNIgFldZYVCUOp3xVfFztwKN8SZKcXWBaiucCi7BMta8VjThcDOQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=Rc0nnvTo9dtgqzsbzbm50FwsAuoLnvv7XpV7Fkvya4MUYUtU4PXWR8fGu20JKefM65ayR9pWyxUYjaW1_DJTC2TiLNXPu08_mz1g-6uQ3GOX0A3BpjA_MeLPkaBaaCH57CzNMp229bvWbgvxIk-9TlcPsdbY0YNCU6TNc_rgdBJK9DdgimFNr6_5E88aQFuOk_VSgFhkstKUoP4JFxdM-Ho4x5uZ-Mkn1fc0AkUJ5w2_SMLloan_KVe5-fWck9Gy9qhQ9yjSGZ3MYfGTeE8AxyfhE-Z98dPzZNIgFldZYVCUOp3xVfFztwKN8SZKcXWBaiucCi7BMta8VjThcDOQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وکیل تتلو گفته‌تتلو واسه‌ماه‌محرم درخواست مرخصی کرده که بیاد داخل هیئت‌ها نوحه بخونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=vruYEvu4tDysh_iZPeX8-6Jd7jTZKJW6GFne-N-9gvbzRdx9MkSrLbxObLyX2dCgDAJ23ey8r9wiPvqs9dWtnEYMBsCHhSndS93XOuqv35RCOourB59bF5LNlf9H1ugPM9WfJtnR1wPtz27oVpFYn6QQH9m4jet03YDsR9EVScZWktGnDQHfsT7QoTbLoo2logWXb37GALw1RkK5EDccE_yATC8hYjwLUuXaM6PfGyapIJCUYP7HnqzlRJw32JbaSGhXTJ7JVaPEarF9B21HlwfVpzLhXH21iSV90zwdsi73iW3-omVBTEWWnpJfq-nDL6V9ZOS4QE3FI3nW6wmhkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=vruYEvu4tDysh_iZPeX8-6Jd7jTZKJW6GFne-N-9gvbzRdx9MkSrLbxObLyX2dCgDAJ23ey8r9wiPvqs9dWtnEYMBsCHhSndS93XOuqv35RCOourB59bF5LNlf9H1ugPM9WfJtnR1wPtz27oVpFYn6QQH9m4jet03YDsR9EVScZWktGnDQHfsT7QoTbLoo2logWXb37GALw1RkK5EDccE_yATC8hYjwLUuXaM6PfGyapIJCUYP7HnqzlRJw32JbaSGhXTJ7JVaPEarF9B21HlwfVpzLhXH21iSV90zwdsi73iW3-omVBTEWWnpJfq-nDL6V9ZOS4QE3FI3nW6wmhkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s50BuxGp4rfeC3Fn8LDPMguN2ORdM0jnFWXxmbDhHuOIOMq86_Oek7Xlbr_zv5QBOseiW8DxNj24Onn9Q6o3qfHA7RbM7bXoXTWg-fMAw7DV-wAKzPSZHac3EcgQXaqoG-oF9u6QLL-CStKsiwFDSvh8KMMKZw6qscFhuMbDCt0EzsEPquISBMQof2nB0HlXInjkvl7GElJ4hmqLRMGNz-JGD3ZKwl6p6nX0XdSRgSm_HOWUjpgYRXcEmS2UpkRjL8UIiAusHh6RRltggndBU2KxvsAIOdJO8yGfMwIl_rxalYJ3JpBXmreJ9YCL7CHkBxI-BpYUGK8ZH9NlZaMElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=V5jrBShSYe0JNJLAxmx4P9sn_GV2J-FrHwaqbBKQayi6t9OfP61m5lnuEfFXnik0xIHRMttV0DfYOuf-jqPkI6Jfhd5e3xShwXJCteeT940Dhm8EOw6hnRpOxuOfriiaRzFaQtlGSc49wD_x2UnGSL8SZr9MMxEgbGYWGAAkP8erzxRVPm5nPJrW3yF_HwDr9ByIuga7Sles1i5bPuqey1FFL1Mx1TXVWZoxgxgJl6ghEpRvpbpZE3AQTbfA-72aQwEetf-01AOXeta-Wsn0nnC3vgpFdz7p_KLIdalE2XtQ2shAqYq5WfxlEhPRMTWXcEU-ZxLr72Z_wzCv7nEF0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=V5jrBShSYe0JNJLAxmx4P9sn_GV2J-FrHwaqbBKQayi6t9OfP61m5lnuEfFXnik0xIHRMttV0DfYOuf-jqPkI6Jfhd5e3xShwXJCteeT940Dhm8EOw6hnRpOxuOfriiaRzFaQtlGSc49wD_x2UnGSL8SZr9MMxEgbGYWGAAkP8erzxRVPm5nPJrW3yF_HwDr9ByIuga7Sles1i5bPuqey1FFL1Mx1TXVWZoxgxgJl6ghEpRvpbpZE3AQTbfA-72aQwEetf-01AOXeta-Wsn0nnC3vgpFdz7p_KLIdalE2XtQ2shAqYq5WfxlEhPRMTWXcEU-ZxLr72Z_wzCv7nEF0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=uT5O-975BTC_yEi6vkEozPo5aGJHTBdQuWwSFPEUlNTgVg8AKiqOB543UKpoFx2MEnI9E5MEYCuD5P4gxigZ9YDyH_DCVl40Z-T8FRBlzyvejlpGqnjZmSpR1tkIc67Z_w_rrmbSMuQTIYjK3a0rISo9f1zHMsDIyTbZ3Cx-BFE3n7xTcCwDsN9nUS7h7HjDM6ourJzMORGZuy3foJ3iHpado_CFG-NU4eVqL8FpWa-PSm7084XuL_vWtvAsFhHZRj0odbCrDTlLeBhgYAtEWymhwH65G9cc_YnOa12NoQlD4vT7n2y7WaXfbAcfwyrTrAFS4kar6E5ajwVgWpswtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=uT5O-975BTC_yEi6vkEozPo5aGJHTBdQuWwSFPEUlNTgVg8AKiqOB543UKpoFx2MEnI9E5MEYCuD5P4gxigZ9YDyH_DCVl40Z-T8FRBlzyvejlpGqnjZmSpR1tkIc67Z_w_rrmbSMuQTIYjK3a0rISo9f1zHMsDIyTbZ3Cx-BFE3n7xTcCwDsN9nUS7h7HjDM6ourJzMORGZuy3foJ3iHpado_CFG-NU4eVqL8FpWa-PSm7084XuL_vWtvAsFhHZRj0odbCrDTlLeBhgYAtEWymhwH65G9cc_YnOa12NoQlD4vT7n2y7WaXfbAcfwyrTrAFS4kar6E5ajwVgWpswtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-KOmlorYf8NEoBUgJmEnD_fhH8540VPAshjq2PyT92yuxQ4_HoMMY9pRqxRCLNZuhLRIXCBWNeMaFOCa13b2Me-Is5KMaKDppm5FswMyshpqhJxPoayEDwPhx_ySRLaiZhtWTsyvaxT6_Ai59tNwONS0AJQRgQyzaHB_BzQj_kPW6PSOyoWikohgsEwPFyG_bHs2JpWmuO-Z6CJlCrlaZtvHF9GCzm0Dq-CgstTKOMkOMXr8D2987mvEo_Pyh1hiVH-jfvIe2DcNk1iANcbQ6Sw_gDHUKSApw6_axFRfpBHYTGlBNhqATSjiI-Ia5k-eMLJ1cvt-SfA4JvKZnfZEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9uoVUQY-qRtEfMHCOMJ4AwcHTdRqIs0-VYjq9GKxxg94mGrR1lKUnnTNLvuSQRZmjejEb0eqWbCDYWn19TTL-mIveQsBn4zh99TlXCz05iUpHXkeaAbJikMuTCxTwVnDr_wARivgYQcqBeawWpCNL4V8HPv28WjVJMl7ry7WUHZgvL3QOIEplYT8Se7a0j9SDGRJAgjS41409-zdqUDa1Rz-o3jGsSWAzOtbDG2rX9PrXJGp2yx3Sx9m-7MAsKjUQWwEhXAQvd8HZO4QJgOjzXSYf5eYtTwFdUcVvsaMCsgK2IVHvniG-yozxBYDti2jsuODzvHZunzM3ZExROFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=LV3pTDTnbC6TDebOl2MKvKEmXzaNbhkCshSrgK8eTFtGbejmNyerQRt5qVHMWwpGR9EaCIUlxKza79Vebx3sD_kgo2wYpo3TqxgRAAMwu5SmjtVxYfoU81UQOCDZfYDDX6KKKP6M6QVUGfMIAxr00XTmxKIXWazSKn2CV5KMdm_Dnn4w0T68YQHv2sRcc1H-a2ahUdRQoxbPfNNjZudULcSR6MtxkNTFpVLHGCwjYOC3wbr-md40Eh_J-jF1X6jzm-v7KzPfJhLEHIXr2LT2zpaAio_eQebRv6_zPyrqugCYDNQ_p8Jc-tvzwKvQ03Ea4Pi_MwcYXwFi1iAV7nUL-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=LV3pTDTnbC6TDebOl2MKvKEmXzaNbhkCshSrgK8eTFtGbejmNyerQRt5qVHMWwpGR9EaCIUlxKza79Vebx3sD_kgo2wYpo3TqxgRAAMwu5SmjtVxYfoU81UQOCDZfYDDX6KKKP6M6QVUGfMIAxr00XTmxKIXWazSKn2CV5KMdm_Dnn4w0T68YQHv2sRcc1H-a2ahUdRQoxbPfNNjZudULcSR6MtxkNTFpVLHGCwjYOC3wbr-md40Eh_J-jF1X6jzm-v7KzPfJhLEHIXr2LT2zpaAio_eQebRv6_zPyrqugCYDNQ_p8Jc-tvzwKvQ03Ea4Pi_MwcYXwFi1iAV7nUL-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNks1oqHRsakdlsupcAorXBOAd5sLfy95uQGfv0UZN2dyygmJwG1M5q2rSm_Di6TbKViQ_qQX94N2oNBMihTHICEkbOwGfyP9Pm-OwH8V8A3vBKRB9rx6mTokAzf6d4TKyKoGCE7GmiP81yvlFqCNXbsGsjYsd9IASXyRpSoyy4bKMip0p0iDcM-TMx8ZQ4rq8QaaVsJEwL20rQ0pp3Gdt2rQWF_j7HbGFoDKHocwl9IVxVmz7aNXoPsbbGXUCDm3K6sBt9XWa6kXLKJFXhL65Z1pmd8u6pde2eaJUo2KMHWuM5QNl3d9m-IemEzGkW7foWMi748R-qTGUqLJmac6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkOE2weGcna29Za4v5KbO-zLL4Abw63dLAwvfwRN7c2G2AxEALKZMIE06MGrgsTRrE102OMYVJRLod690tfuLLsDil3D6nNFH3jmcSygVvSWOb0HiN24LsKMk1g4BlCOtVMCDHDpC9sl89bZK9cu5PAMlGGaXrSn_HWUsfKNl5JbkdBWBT36bGIjRQzY5gAGr5qxVpG7rs5zQ6Toif4dz8vDD43QFJv45ecby8M6gqjwRRUWVyV4mU-JksKKVCB6yB7CylFhOhX3rd8xpNfQ6yjGL_Wt-Jnd1rb48Wv1I3PIALyxghZ3w6_LiX13ituPKj_Wl65lzwANs5MIoRLUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIrhyCEcum3_w0jzoBS2pICOThXoJ_2DESTUpvcIeZLyjx39zR-Av8VXBqcgtpXBejJPb9GQ_Hs0WCGo9YpcS1b79M89_PduClAaAs4odN26Mb1FGCGvJQdM2yw30zFNavYIEMglyumMhejOS7un4469tzEbrQfhjagCm4pXh9-mb3xFBq_SaBTqhdx0lb0ziG_H0jL027QTuC8GRZ7927aJANwCMD__aBWJvMQ-sNyp3oFvNM1c8F7SQBEoFEpBbbrfykaAGYHD1mz5lzkitxZHmsvkExSoRxfKN5dlc9LJvcS7ZEMLHHiYxhWn5Tkc8CjGvyhaNIz9NJD4qQPUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgJ_H10h6rjvjQryeASue7idIdieaWIRcEz7GgaF9BN35xgW0nIRwQd3zHAQNBeT2kGmgF5XqyJ3QXndckKdc-yEqQ1AYXyJi_wIKIdfsrMyQgDFl1GW4UsnpNR85_Zsfgpi1r1ZyXFeM0QprvIaYTgAjyLsXjKiAcWWEK0df_tjsmc1yajJibWzuKqjZUopeoV8HwUOlY7yqM7xgxbNMa6RZIGwzWBcwSUTSxmQxYjb1FCvaYRxLIaqQAcR8QrbrcOxZ8jMJSa-fcGEWu8vHMonduu9DiOybqTeqde_Ckz7CoVc6AoQzAA7AVpqOukVRCIxFJDq4PF5_fIBZdpUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMIHiW5T1xRZCr1b8Pk316A7FlPuyy_Ex9KpNKtZ3_5YKHg5JZSs3295kM6SJStpgTjuNICLs0rHnHPPC48nmU39Sbae6KXU0Bmc-sr0ZTnYyD8T7QcbZohxGM--z3NHXTS18IHvFPzCwp2Au6dRm5n0eqc58I5oO39hrauygXNxMiJWj7bVmJVn7j_en-j9SuGWpNVNhYqQqvxGlFYBIVr958RJcPHrCr8ujwN5aiGzYFrDVXy3agEbAUANHiLQNsJd781xhtrwBsUEvMX0eSo5HbaR0ewW4k0MhPI8FAm05M1tUchvtjjioackhZyCD2lWTHNmGZr773LldXrNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaFHNuK0XF7P9FsI7KY7xwh1Z16F061gzPmPMuhqVQx0DVNEzYo7CaneQPpSBxxUN4OrD7Q2lpFFVrzR5F5kG4rVZayGTTPvBPl7A7ZhO_XTm5uw4_YRU0Wbnlr7y65VjaP_LYIyOUG_KKYmsZDlNnvOzseIFVo64LBkqx_86_kYHt1I98YbostzOG0XKOlx7-gYYkQpumecoSMkAXxmgaopQQigh6-mccgELbNxhU343I7F9fAUG610o2eH-fvjvqDU2qb0HwNPLs2Z70fz39XvLMemvV3ymWxsP7rlUX6azmkQyXLxlTB6w0rbdJ9lNFtw5FgGHGeKAxx0MR_jMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MelBet | جایی برای پیش‌بینی‌های هوشمندانه
درجام‌جهانی 2026 هوشمندانه قدم بردارید و روی پلتفرمی با اعتبار جهانی پیش‌بینی کنید!
🔥
امکان شارژ کارت به کارت و هات ووچر
اسپانسر رسمی جام جهانی
پشتیبانی از زبان فارسی و کامل‌ترین برنامه موبایل
قرعه‌کشی و آفرهای ویژه جام جهانی
✅
حرفه‌ای،مطمئن و درکلاس جهانی پیشبینی کنید!
📌
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌ Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23423" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEe8TEnazLwx9rIKSMslSjan9ijqkaiF_ICUKh3aV0TI1OvFe-BALjBJjs5YahgRcYWQxU3hPG3IN5gih_Cu4afr2DvureQtyVfQsb17ImTwJ5u40slP1Ij5jh9Kd1rTtqNm9_uK4bF8N8snTgtNLeRV_OPQ3Q61Tg_IzGJyZXUwR6t4YzBJYotgQsKQqpx8d7gWzQ_RRIojRPiYLKsc37nXC44HGgyLARXuKyql0SMILChcUfrUw1aqwmP_LfxLtFbPY1aZtkIteBI58sBxk0nxb2N_FDdYuGUaUwf5q2TXvH-QrbvJKs3LuHGRb5IlNO3RE6LTkwhHgkNQ9TgKfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVOAPm0PcXdeNND1UhAYRKLx8_6fBBAAMT9HwhpihvLaTZW2ulbg8cTMTZF0sY1ZRWXl9HDuRLMSu-bxP1fy_erMZQp7Bg-F2vGJytyIGSS0s71a9LV9rNW4iYgSl2kY-V4ne8G9hHWeHruPbLCyMo8KlMXCOqLodcUWDks21XUHdrptXtFFBqmHFgWmfl_4z2tkYlevQWOvIg1ZEoOG1epLbguWHDln7DpSAhlqHtQUpRSVilVpJ2tzzIZph60rts1_nXBJfQEN8idpyl5kX2hgpt_1zl0gCL6xhoEyaAV0ri37QZNAyfdrV7686duFf_8MBGFvjDE2OXNWTJMKEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhzxzLzUStdhuIU2zopZIUoul-Emw18vZIZ-3tuoBKyMxXlZrPI-vBdwE6YrqkvWHjRcNfU9k9f7GQtHbYxIoz6wGVJdCctSNuvWNRPy7iu5gxFH8_e5pOvSHdCbB_zpwWtSciwAAH8EJxidnGapyvs7wjA9TRHrBsJ4-hvLyAuY6Y8WbQVtg7GBkKTA9FFaMsmKIP1quCTHPfj76RDspOVGxl6SDPFF3MS6p1h0iMMItHFeCrdLxL7rh-Lf0hulFKV-hDpKfAJQDJN9aMNW5BT2BWTmgBTRVYPz38C1LSbHYB5v8gcF5fsYVC6S88OvJdoNNvReOKV2rtXBtYMYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXOGNos2UGJ5_6KQ3hh-kwCae03yQevOkyHmz2ZJ0qCECjNSNBhtDoLk7h4ebzEimTBM3okheUfSy_-afecvoruTp-l8ajYVXxh7LC0z1VTSqxpiZECsOb3cn8ZctT6t807PYCT0Dte_HegwsGxxdAzay-8PwS7NxgUP1tDZjw_edMxTEk4gNCvo458ADU5lWXT8gqB1qtUy8hprlN7u-Id2Kfea3hV_f8Mt1K7NU4WG_HooHIHaD1Q9CLxm5Xq3X2-Xzebpiy-5GhD93H0m6bYcSZx8DDIuQBFvNafaCG63P9aSLhdMD9cHgYdl_aClA8Cgs66S_izmKssD1TAmOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTbtfOorqdYX3CAc6ROhRpVzEFHN8t3ytU35ilMpgw2MDBqJHLOJClVw4yMFabSqKcH5VvZm6dZI_G1z-LJQtza_2_8DGBUNWChhKj9LHXJrOK71UPE8YYQeum8SzF6kabL3pWGqxDx7aGtguYhc5mrlr7v_7OPLHP-Y9CufSZ30OWBoxdsHOQYH_l2yt_eux9mSSrdwPVL_eATifS268Qs4Yx_TF9LieomBTrwK-HEuTbIl3mgHTvIjyd9pBwS5CUq8VWVPRKpo8R9T4xlDhfVjWZW7sTL3wNBZyyLqnVU3ehmLcUHgqbMNGkpmOx2g2Kxx5bctO7_HqASGUoAHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=j2U-lsSUNhU_0g3Jjn1ihwftmE2Yy9LeNypxk4Eq9wcfUbHuboYCh03dscG2gJvK9MMz0I-u3Gr_1SC3fKJre1qsZLrsNTIvS51c4zplWSyRzNHot9_9cvaC9jFy-ZkSE9YuvledVrCnwWq0U-11Kn7DyaEA7MeEarehV8Uyp2UFVG1979OvZC9jHJnN1ytbwOPg6Alfd5WszuM-9ocBWlivNzXeQswjM7nE5AbuNrr25pIUlcvjghM9f14Z1qiVE6Txg1JkMBo6fodZ9JYfxTjZUOZPEi5dukDdoXaV0UEa4aziUMFt9fBg-J1U7bStd9PHQVw9TclMD8me63GTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=j2U-lsSUNhU_0g3Jjn1ihwftmE2Yy9LeNypxk4Eq9wcfUbHuboYCh03dscG2gJvK9MMz0I-u3Gr_1SC3fKJre1qsZLrsNTIvS51c4zplWSyRzNHot9_9cvaC9jFy-ZkSE9YuvledVrCnwWq0U-11Kn7DyaEA7MeEarehV8Uyp2UFVG1979OvZC9jHJnN1ytbwOPg6Alfd5WszuM-9ocBWlivNzXeQswjM7nE5AbuNrr25pIUlcvjghM9f14Z1qiVE6Txg1JkMBo6fodZ9JYfxTjZUOZPEi5dukDdoXaV0UEa4aziUMFt9fBg-J1U7bStd9PHQVw9TclMD8me63GTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6gBD_TJLokByOxvvN-6qV4CNGcp-zGkK-dRIA8bjAgU689czR-wsupzUXqKHJonCJQ_rrd1kyHR_x4VtCW5caE4OBDtu9j3ISFm_MG46ZzgtE9miQkUWLIwNQvCBVm04WXgly59Mg0KQL-9VrueYvvLC48Z8eColJJ3fe-KalaOB3MbZnjDW6_R-aXVRz0pDoZQxejShQQtqeunGH8Epa1d1_EH2XM6QAaqbaIMTPaj95iIE5a6L-tzylRgCFeE-SAJj_XvdnbdRTT_SDjU5kRU-TCS8W2J--KhGJHlocKNeIxrhstJ3Nd7tgKKJxZpleQLQKAG8oK1q-KB5NTuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=YBZ9i73BMxI-ctCf0OvWin9xboXPLHAqgqoS_fqJyeToEQFaHbB_xhKWypQPnr7-Y71lEQDVrklUxdVWitFbGTGmddhu3meRBvi5Pz2On3WnmdSXpzLx6aGfaDVC8qPGwG0tmtWKZxE_ISyUVGJS29NYRXohjV-pENLFpPWHt26XP1pmjkmj_byXcMTnI7NqZUeylhmY1TluRQBe6rS72j4YphJEAhJZsTgBgqSTK6D3X_oTrlG11RHKxJleULXlc6R0kBRqLpw6vu02D-e-fQNyqf3Rx3QjEjG7AKnVPPE7MRb6DRFZFTNLwLH_mzh3Ir1LwjUDq6uJGuL9XdWhmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=YBZ9i73BMxI-ctCf0OvWin9xboXPLHAqgqoS_fqJyeToEQFaHbB_xhKWypQPnr7-Y71lEQDVrklUxdVWitFbGTGmddhu3meRBvi5Pz2On3WnmdSXpzLx6aGfaDVC8qPGwG0tmtWKZxE_ISyUVGJS29NYRXohjV-pENLFpPWHt26XP1pmjkmj_byXcMTnI7NqZUeylhmY1TluRQBe6rS72j4YphJEAhJZsTgBgqSTK6D3X_oTrlG11RHKxJleULXlc6R0kBRqLpw6vu02D-e-fQNyqf3Rx3QjEjG7AKnVPPE7MRb6DRFZFTNLwLH_mzh3Ir1LwjUDq6uJGuL9XdWhmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMojGuM05UrcbHq5nZtvrMxkV4RsdmxO-hrZ524rmz8QXiN2pPuao4KygcQC233q5UMvMi86RBaxhe4NRYxiper9YkeYUDgicHSQShBqU1-MUrmhr9z3jzMNfn9-_1sP0pfbIL5RIwsCokj8JVvMwTjrSjfgKg_0CdlvYLZZ3Jf_3pAEeU5KgV00lky-ycNiN0qtZbXq7dvN7rUrNIDYtWANKOpyvnVBhZL2gWzG6XucrcZgfi4oo3LQIODxFd7kdM7fzNkN__KcK8mAph_okNTwcr-K9Kpwz-G_tfD0EXqLVw-dnAjY8SI_hG9R3fdUcBMyNwYnA2htrfTXBKqa0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=JM3ReDLGr3Setfy_WyzeLAm586L9J7FRu7uYSov9X_uCTcjI5Ih-_TUvupIZiitaC7koH0XtRKNY9ojQpCM9In6-s00RD7Wd0BMyHWz8S-NiyanZS6-FUcD9Yvp0LvW4eSu6rdhWgQ1x8L1_txW_URppNcjr1m8nSjQ1qNo0zTGxlSCYStIC9bbxNqc0aURcgKLydxCOmdigTzSdMj4_qTg0J757ijERpjNNEXC5-XvH5Fwx2hljE0S5t3EFuJXaYM4nQmzLczpHa2yCAFb2Xk5N-kk388RcBxooJhOxdCp1otXCDr2_gv5D2D3qsjkTS1XLeZ5q2TbA4bhOejUAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=JM3ReDLGr3Setfy_WyzeLAm586L9J7FRu7uYSov9X_uCTcjI5Ih-_TUvupIZiitaC7koH0XtRKNY9ojQpCM9In6-s00RD7Wd0BMyHWz8S-NiyanZS6-FUcD9Yvp0LvW4eSu6rdhWgQ1x8L1_txW_URppNcjr1m8nSjQ1qNo0zTGxlSCYStIC9bbxNqc0aURcgKLydxCOmdigTzSdMj4_qTg0J757ijERpjNNEXC5-XvH5Fwx2hljE0S5t3EFuJXaYM4nQmzLczpHa2yCAFb2Xk5N-kk388RcBxooJhOxdCp1otXCDr2_gv5D2D3qsjkTS1XLeZ5q2TbA4bhOejUAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw3Cl0psx6l8GeDnk3b9PQhh2ypAnrXNHICW82uy_AApIadSUQOb8AWwoFF9uL7aBEDfy7KE4Xh_YHLBJsbFzZMRPp6o30sgh40zRaM9m7K15vk5v9MsRodED_PY0TVkcjSroAIOd4K4Mt59WwAkZOthNkJgdMr1unr_x38msXXaTlf2TvfnyKYWScBG0yt_egoqvJ2nfzGaKqdTq5blxQ-pYjgUnP_D7WjvoCxbmGLJP8NWo6rC1g5R21GxMYIXR18NFkwBpXi0Jp2QbZyMmcTUf1S3gwBZotzQnCEdAtuC3myngzRwuf4v-WBEeqF5QEo0OWEUADD02d9DjYlo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFyBx3zW3QKgn-fdIlU1gDd-Il_HSK4HW8FJF96Cs9w5Uf8mmbs8J42mQpbCXeNqw7LU6cyj6ASymD0hC3NTyfnGxw97TWAedkZuCgytPi870Kz81BopcpRL7uHLmb5lCfUvoVWkfKPq-RQCQbvZt-uruM4jS8FBdnHeWS5It4VzH40UTDJi1q5BbOKHLb32-xTQOccSG8OrWnAvLxNZzfCZvbuO5O8N52rC5myQBTjSVJqwrmBP0toTeWsSwBhWusuAIRWO0FJ407RzlCCLZAkZ_m1YsCZAvVRNLJDYumuRNxNSl6n-AO-5EPUhzpSNG1eFwYRpDcB-t-lUTx8Tig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=Oxuch5GtekRtIp4w9vtWOtGzihjHj1aiPpPxROA4m2zP7_UlFdeYzkEchrd_s013UbNPPZ1sojk3fpgrUH1UxSeRVy2lAdS8eaAsuBf1VVYA8oZRMvnBjlQZmK2zmY9jAJ6dKIrupTLBbSzkM2yEsveeU0rG0thYbwIVvufyasBatOphfWsYEk5YV_0bYDqdtMU8yxb59U3Q5Ci7ENlpNnzUZV0cwgSwRHkP2jpmrLh2keNNCEycZCtxMNUb2biJeF0bOha8LDJQInFubOjYQVJ99xk8kugHeW_Yqf0GLmi8KN9s_jniE2amCXjN-PJt6IcA_lfR3p_TigF4thRIjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=Oxuch5GtekRtIp4w9vtWOtGzihjHj1aiPpPxROA4m2zP7_UlFdeYzkEchrd_s013UbNPPZ1sojk3fpgrUH1UxSeRVy2lAdS8eaAsuBf1VVYA8oZRMvnBjlQZmK2zmY9jAJ6dKIrupTLBbSzkM2yEsveeU0rG0thYbwIVvufyasBatOphfWsYEk5YV_0bYDqdtMU8yxb59U3Q5Ci7ENlpNnzUZV0cwgSwRHkP2jpmrLh2keNNCEycZCtxMNUb2biJeF0bOha8LDJQInFubOjYQVJ99xk8kugHeW_Yqf0GLmi8KN9s_jniE2amCXjN-PJt6IcA_lfR3p_TigF4thRIjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO8h5_bH-Kqnb39VSQZv2nP0fax3y6kF1hTGzzukJQ9FstUiwMAj3XQMPCxK1qUHB2biRSwTfi1lOEGbMFDIHZ80roq3W3JGMwvOvS-1S4O8A_v2L1KiDguJ01y-m3z4PNJcdUfKDbKeNJ8_4wV0fCBSrHmmdf2MQdtvm5gl7UMF4T7Up86PHlk5Wlk0geJQO1240VVQd-SbIhuGnB-BCAZNzNUWMRv0SL3mr19KsEwfscUEe-T6HJDH6pKhfj5QoSGYFsGTSi3_Cu68xIxPsz9eUpDveRsh9YUKUIrlWGIrG4hFHJmsRWsldseoPvwRRQ_Hu6See_8oAp7omm38yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLS5FwTK4SymqVLUnFcoNSV4XMVZ9WGhaT1NJ_uwux93tbcC1cY-vHccfikQ-wIeL3oD3fp6ffJ_w5uaZcCg390WEHeOFaVe6vZanZwyV422Jcf1fBE26BDND7WX0Pllzj3uGXRVzfpYf8lbsxD0PDhLmwTIrgpLVLU3bWWzFMZXBwbCht_doDOXlvfcr8Qn7wd2agD7rX3DbAAZulZmXyUvTHP9TVsTJB1-F8C6145dlF3s2nN4nHhSQxrknKzp4ZMULk348m5qSkTyOzUmfBnTMJymMtYqLZzg5KCuDFahmtqeakrTT-cvTvk8IMD7p6L9O6YvgS-Q4HZpy1PIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7HTicd8x0UCHBYxauvJxv_Gnh3ZjM8d7uzyOXcmlDAX5IsusCKDSQHoANFWTLkG69DJgKUYT37-ZKIhgEGuLylsj8wHfLsEOS9NUjeMijzpsZ5z0hqW1KbFitlp93i0H5A-eQBVphniBhAN6YSEUu2loVRSf_OZi_uhLjnaOnWapj5LAAxtlGvXQ4PHThEhrOayHoYNp_BoBixSLsvjaYSo4QJ--XaOjmJkBG9jleUIxzn_eNX3ZxqCEqTMAmbeZsskJ8KxAEwe356SJLIp8ljlzTANVc1IC-HOhmkhiAmfu4okhhfrqOdSQtunpe6kZK1D_iTdVVPP_NjMaOnnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=G1K1KIwalMgXrrjS7Qwmg656DHxUaT1AX3hY6z8ZgGjOMh4IRIhnA-Q3swFjBPpEVAhAsCYJAlNRA8knA3LEdS6jPKnFg_NT9UXD8z95-v0D0fppkezhBm6EybzDLEacDpktATAOKbCwxjzCtcjbF-_0jN5-3szmZF0QxzfYActZ6gRYPjInuJ119xQXq8cH4mfkySf9Ea_tXTKI1odii-VSLZ-g0s0LW-sTbDNRMT3qUK6knHP2dx9hTUVc6kwAjbCdg5ID2ac5-7a3kQxoWDSMxAq6PpcWXED0ChQ5SPZVb8pSaFyGKctfZKrJ8QpOS49g_4RqizQp0GqFIu6KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=G1K1KIwalMgXrrjS7Qwmg656DHxUaT1AX3hY6z8ZgGjOMh4IRIhnA-Q3swFjBPpEVAhAsCYJAlNRA8knA3LEdS6jPKnFg_NT9UXD8z95-v0D0fppkezhBm6EybzDLEacDpktATAOKbCwxjzCtcjbF-_0jN5-3szmZF0QxzfYActZ6gRYPjInuJ119xQXq8cH4mfkySf9Ea_tXTKI1odii-VSLZ-g0s0LW-sTbDNRMT3qUK6knHP2dx9hTUVc6kwAjbCdg5ID2ac5-7a3kQxoWDSMxAq6PpcWXED0ChQ5SPZVb8pSaFyGKctfZKrJ8QpOS49g_4RqizQp0GqFIu6KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXlu5I0FNEdFOte7T0cEAHvKXTwFfW7_3JyKwR_L2TlI0RVTYxcJCeUU3r3qFW64rrCfla2Llbxq78MoG_wrmSkyehumChWPC2Spa5klMg82_y9CprVUJV0CVele_7obnIHm3KA5mPn-BzGxMWJ6HRvnkphxHgklxXz3BIfWWizh53j5z7XbrwIIotZrwSGORhmJF4yO2koY0DcxMBp8J0TiY5epteUyKJxFd09SX20TuKjnX1PwKXcknxehOwIHvSD5CBc-ImwXw2D7ZCr70UpXfCmU5v61FnGk3tOxURC_0gWVj8yniC51aY0f8HzFsR53ZrjTiOUq6dFo9WZA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=lN0RWHS5KEsL2ZfH3OWzjiPkhlp6qnoqPENrvQE2AQxcEtkBuTrZ8KcMp4HFHthpU86-32J8bp35Vnq8rQ7jLBvgltBCeLeKWO20nsl37PwI-tiIc0Le2OrfwpT1KfOId4TomaTgIdLqmQ7UMREzfnD5YjTAnl33ZESIvU-X64Kf55xMYEgyzo0uGLXP7nzQr2AJTdgbqEUVB6na1J21P8k8h0RhJFE8S6ypFa6viM5yadhDfKAN1VgJKI0yXbNq4PTuPM37boL4mitA6kd8PlmL-acKoWU6hv1pjDMLCrmfIVtGWu7fYJflfscqAy7LeihX9cnGQI2Jso3zFfSxCHtrEDJ_e0pjnkdJ3qoEUZu-ioHt5Vt3soWlivcowQ4mwZAito31By-aQ_abTuwC5ptE3fd_dDQRGdGha1xyPzkAb7g9YNKAguVLs1HKr6OWPN8Pl20fR5pd-uc5lx5uX1grRXkqWfuSzmFazI6Z3DF8V2H1Ca08jB3qW72ICWplSYq9H2koJjXm2q9Tl7_SF-j-9ZjG_2rZPAkQX0DcrMrdpqsiURjmMuN1PGCGFGl5HuipKWBd5uqjWSQSaGyg0AzOItSc8J0v3jtKEcTdGNHKhW6qjoQzhNtQczf9pHtrx55ixN1s4M6eh6ttaXIWdqqj0nEW-SdR9sX-RzMn46g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=lN0RWHS5KEsL2ZfH3OWzjiPkhlp6qnoqPENrvQE2AQxcEtkBuTrZ8KcMp4HFHthpU86-32J8bp35Vnq8rQ7jLBvgltBCeLeKWO20nsl37PwI-tiIc0Le2OrfwpT1KfOId4TomaTgIdLqmQ7UMREzfnD5YjTAnl33ZESIvU-X64Kf55xMYEgyzo0uGLXP7nzQr2AJTdgbqEUVB6na1J21P8k8h0RhJFE8S6ypFa6viM5yadhDfKAN1VgJKI0yXbNq4PTuPM37boL4mitA6kd8PlmL-acKoWU6hv1pjDMLCrmfIVtGWu7fYJflfscqAy7LeihX9cnGQI2Jso3zFfSxCHtrEDJ_e0pjnkdJ3qoEUZu-ioHt5Vt3soWlivcowQ4mwZAito31By-aQ_abTuwC5ptE3fd_dDQRGdGha1xyPzkAb7g9YNKAguVLs1HKr6OWPN8Pl20fR5pd-uc5lx5uX1grRXkqWfuSzmFazI6Z3DF8V2H1Ca08jB3qW72ICWplSYq9H2koJjXm2q9Tl7_SF-j-9ZjG_2rZPAkQX0DcrMrdpqsiURjmMuN1PGCGFGl5HuipKWBd5uqjWSQSaGyg0AzOItSc8J0v3jtKEcTdGNHKhW6qjoQzhNtQczf9pHtrx55ixN1s4M6eh6ttaXIWdqqj0nEW-SdR9sX-RzMn46g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=Hdy45SOo6S7-Vb1XjV-nPbgUm4Sx_kcUUBCT_oAcmnQfmeTuBd2zQ1Izawv34oEay8ysvll8rIt_xldWoIwOmEMIgTLgQL7Q0VGTX6KxLfDfS0wPfW7F9pKw8w5TyttD-TDS8pLnR1XOWQ6tlG4TGS3avHvLb_b7rBrzoNK1Z-wPWm-z4v7IccUzIKgYat9mtt5ZnkZ6QDLHIUAcjFYa-lqZrONryKUsoHnRX1BidZHOmZsrP9x6pjYz60UUUBUCP6ugH9sbwhB7ONFQazQYkl1yiVSpYqUmSVmwgrLQ4YgE-kNJEc75MtN2eJV5UEmZek128hOano2vWcE0qpvgiayQko-uh2Qos2NnTBKFRLeesQ9cR2q5H2MysAsaTfHPud7tItZn9Iyx_8ruvBPPjg6xf91AHsKQmYPAR2CkbgWHZushUQf9Mql1TNDaRryO0YM1AsJezLQWq5OaJLLNQQeJMRqScB4mPlTp6xwBIIKf9UFXHmVcbzc0lFNilMm5OssFXnVFlFGh0PQQBMoBIeqTDOXctTjVeph_Ip8RJ4bPx1JiUksBTGJdlO0UCxQkxIu9O6HJ2gO8vnkW1UugKJlf9RhjHK3AeJEru9C6l_48GmV_s9GU8ar4krg3i0KFPVK9rxhICFpU2af2KwpVwF-ufJbC_DFkjKZckPMoKlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=Hdy45SOo6S7-Vb1XjV-nPbgUm4Sx_kcUUBCT_oAcmnQfmeTuBd2zQ1Izawv34oEay8ysvll8rIt_xldWoIwOmEMIgTLgQL7Q0VGTX6KxLfDfS0wPfW7F9pKw8w5TyttD-TDS8pLnR1XOWQ6tlG4TGS3avHvLb_b7rBrzoNK1Z-wPWm-z4v7IccUzIKgYat9mtt5ZnkZ6QDLHIUAcjFYa-lqZrONryKUsoHnRX1BidZHOmZsrP9x6pjYz60UUUBUCP6ugH9sbwhB7ONFQazQYkl1yiVSpYqUmSVmwgrLQ4YgE-kNJEc75MtN2eJV5UEmZek128hOano2vWcE0qpvgiayQko-uh2Qos2NnTBKFRLeesQ9cR2q5H2MysAsaTfHPud7tItZn9Iyx_8ruvBPPjg6xf91AHsKQmYPAR2CkbgWHZushUQf9Mql1TNDaRryO0YM1AsJezLQWq5OaJLLNQQeJMRqScB4mPlTp6xwBIIKf9UFXHmVcbzc0lFNilMm5OssFXnVFlFGh0PQQBMoBIeqTDOXctTjVeph_Ip8RJ4bPx1JiUksBTGJdlO0UCxQkxIu9O6HJ2gO8vnkW1UugKJlf9RhjHK3AeJEru9C6l_48GmV_s9GU8ar4krg3i0KFPVK9rxhICFpU2af2KwpVwF-ufJbC_DFkjKZckPMoKlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlTO7hv6Be7ZxsCHqYS0sPUbXLzRGiPe9ANjwE5mqzyVNTQANsypyMdPuZ1El-Zco0bc9MKRpLOErkUpnH_hf1gq3d_amACdto8NzIiC6zt6hWawcoBDuqMNNVTMo7DTv_HLcrkJuazj_tvMc8q65UYM7m-XDz6PpcRWaaD8MdOWV1iWTlIlYXjUzmzB2visEK_8DfhvhwYonM6DcakisPx3PDkNI4tKr4d3yMcWXXlTwDHT5LToJZxg2gI0LXUrnjVMO0uW55hHFTwZm0JaBEQ1aBG1yWqVzbj4HVj2FudHAtF1tKcN0IVaeS6LubnxzuD1YhJBBmYGxcT-jTp3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_o9po3av-bQpielU9-X5QqGtb0XYk3-LKHqzH1k5SobqxySkbd86FTmOaGJ8J7s8DrqpSrezlA4Bbkq0I2jqAwP4o2yteYSRsO4EyIZFXzlmhrh4nDMUVZRVrUspAQZtufbn8tufxrYVlewN0HemEi5aFybTcyJHfNiAs2jlNulNjiLmjqOWpd51xKmVbBVTci53Va_BQiptI7amH5CMVot66R1bxUH_ZhOonCbrCxerkoHJDOb_ozJgwXJio_yUyGX31fRwsM4LTOb0BN2QrxSSvsRC65gKSMScxWjWqVYUbYYZ5m_Tz4Qe9I6DSYQ6foEJkKje-qR2brG00lAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDLKZ11BJWD8t4CkBrYs91flZjNiSJhJsafR-fDgHIIHggMqnMKq7XysHTWVMzuM0OQjDWGNFn4nL1FVhYR4G3W13MTo1NHChdYVyTG-ACkGqKG0Y2CIt2JO0Emy4Tp63D3dVSPdx1_yInCCwPBlNHGaBpwD_SuYbRsH3SbyMA2WmTUcy9u82Tc9Eg6biHNmDjf_gP2QQm9mqvMEt3CxWA0wqEnUAyMpR_kNcRav1h3d1bfNXGDQzEMXcJRFy0JS_51sj_pr_Ub1YiFZwcopeyK-17K0tZKyBKlJnh2lwxV3a3pl5rwL3vKmt6kk7T1pRscqBDW4rQmaHogP6CqJ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePZiU8l2-YAC7xL5wBOCFYfh7azDTsb8XrIzIj201PW_2y6hDb3hCxH3pXIkIJnA6CQfxXxqaXJewFAc5VnMlmmgBccm5swdJ24Q19XQxK65-EO4lJCkeAivT5MJmbDuRKyZkv5qpzC0-qzj-SXY-ZL_ZG4uDuhQDEQnqs8t-zi_GG5ViaSnZFO52OJlTx3oW3K36MJ2s7R3RW4BUVFUmqS8Em-ja3UTwYNU3O-lZ32tPr2BMPyeVvQrGF9duS1D35SIye_r6kFfM8ELxFML7Cyv_z6CFauBQqb7YHxxmhkX2KfvWqxf00vmoGziMw-P5ZJEnFBp80Js_M_Cu1bQBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=B2eDkOrwC9xB1NpAlHXO0VYnU2a-qdSUXCBzcclpxYDCyS8GnEnSiK9dOAQqhmoX2BgHvqvZ6NwWN-HM9vASDhThd406iAfxE9o5z7KScw6z-k08yoDHmjnfC5uTAFC21VNyE04NOjGGHG__Hw_Ew_hIPII9ukzkYHl9p9gUx9oWwNRiQboy_i_ssu9ad8zdpYTCVn3LEq_kDGBXQNqMXGc4VknEPu1A4gOV9wzo6vpVmxoUIbkaI9PDbMUujewGcELc5OasDLBX7PGQ7_6nk5lR6DKLY1wT2XAUEZn3r0oE0a5en-CyNWNJOkzc1qcnzBqIDIhfViYAs3UfdUj51w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=B2eDkOrwC9xB1NpAlHXO0VYnU2a-qdSUXCBzcclpxYDCyS8GnEnSiK9dOAQqhmoX2BgHvqvZ6NwWN-HM9vASDhThd406iAfxE9o5z7KScw6z-k08yoDHmjnfC5uTAFC21VNyE04NOjGGHG__Hw_Ew_hIPII9ukzkYHl9p9gUx9oWwNRiQboy_i_ssu9ad8zdpYTCVn3LEq_kDGBXQNqMXGc4VknEPu1A4gOV9wzo6vpVmxoUIbkaI9PDbMUujewGcELc5OasDLBX7PGQ7_6nk5lR6DKLY1wT2XAUEZn3r0oE0a5en-CyNWNJOkzc1qcnzBqIDIhfViYAs3UfdUj51w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFpQ1WFfyeYByAuFWhOfy3yGqxsFneWpNGEx7nCALWIJ4MeFeEZ8xDa-ndjWC9jZqdtrFa6iA2zV2Z6DNj5lSWueLfzH95O8exD83Had6NhDuJutikxFnxeSmS2h1Q9d5tg3eR4ZQiHnDVQLIEgOpeV9EPoCOEz_aeDdeU-fiQukUk87sn47zG2aDo7HZaMmYHNDC7uBPYCSV7dWaBBnKuucmtCl3a2z-iUlA23UC8wckrykADOkaoDfdt8GNhDxRH7SAQBhsrt7HGQdrmb2iUNBRvJJdMjDMg34hJgv42l_Qq4VuEFUCqW1rs0vThpDJY8wc_lRX8PHAQYCwlpu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB1ZyqA6B0xI6KqpPxWQl01gPS0ZxpLAziwZujsJGaA91hD-4UuoMEw35BkZc7RbL9nw367NFMw4B5LpHbLSG3Sp0JkT08idwIdgweHuRH5IbD2Bc12VokRikfatiViNO7i8PLWTIrgXRe5So0EP1TwbOGe337iDDoc6C3wiakJEIrTULS4-o8ZzjEP0Mvj7oIz13QuY3BxwCK_wcEMkRPYbdPvYeKzzVZsu2EsYGYdpxUiXW_8K3SeW44m0LndoCSyGsWpkp46quP1R44oAp7ifYSdryFcCqp58HUiF4yFCRui1Ppe5bOoFuf2qvPBrGEwZ0dExOfgH8KmchiT8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxiMk64gdp6HILFdWRUWjUTQAfNm_FCJKeIUBw7m9FM7yU--7Xdv3prn5TGcM2jcOyRS1dEjsSKl7CBlcJ5fNtkywvlzYiFpblOn8WwkxZO0GtrF40hZRAwlReXwTS2tyZvVjA23yKXV8UOqcCwXrO4w1boo1WO_l_Rsp48r6KfVZ5KR0eU3XfNbq-utN6Jc8nJRoyYXle3RtJh2uhPk-FYencPPMJDldeEdCYSY7ChaRINanX5EGCuitN5UK2F65gzB7keNZ9pyqJIbSOvz2R3axvgYJohaVGcKzHU1udmiJ1YlCqEFTCFxmIWldHnfTpYCKgwQPfh58VYgtS8Q7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=Al9UxZjpsQ9J10Xd7kIIXIqVNYahhS1AwsbsL0b7jLN2xbWagX73oR6G0-ySoLy8Sd6WnoIdIChcYyVlJTu8FvACaJDLVD6_alX2ORIwoAWeMMKkwKVewr32VkCsuyDSz6QdC-aPoasbK7U2jFvZTOzknSjcLzZIQLZlDN2GUppdZz1_vKujIdVM4y1xSmGeg11OJIo6vaFETLCSMHo9uXJ6XMCRoepBQYGKotGk611lZF1q1hOS8zdN-e6mMm9QrOOy1-x6pqcuSgEe4HzA8yg1Q26ijhxeYB_SYWVw0sTrOlHSkDDPoyri6-zh6jn7XzHfT12HERH-dYGlITvXvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=Al9UxZjpsQ9J10Xd7kIIXIqVNYahhS1AwsbsL0b7jLN2xbWagX73oR6G0-ySoLy8Sd6WnoIdIChcYyVlJTu8FvACaJDLVD6_alX2ORIwoAWeMMKkwKVewr32VkCsuyDSz6QdC-aPoasbK7U2jFvZTOzknSjcLzZIQLZlDN2GUppdZz1_vKujIdVM4y1xSmGeg11OJIo6vaFETLCSMHo9uXJ6XMCRoepBQYGKotGk611lZF1q1hOS8zdN-e6mMm9QrOOy1-x6pqcuSgEe4HzA8yg1Q26ijhxeYB_SYWVw0sTrOlHSkDDPoyri6-zh6jn7XzHfT12HERH-dYGlITvXvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td9c50DH8d6zKoQU0k5tCpoWfh32W9en4mplpq9XuEhMUknqi45Ui5vy1uONZB8mOhOn3lRMoSWS8Zk5YhnmeLwPFiDpehWBR66WgGBpuVNgSd4XlPDSsKlL2uzfpgXcPEwsgd2BAYL-ivsV6OhZMiIfF5QDIHZxWn4A0JNmBHq4fPikB6R-t3tFOo1uSXav1fJFLw0aW1uPg5DHv6H9j_SaaZYAsQdRkdUfN4NKkUJ35FUWFicaFvY6s-NegohkSXCLGoTtAqX7dxdyxrdgnrljrq5sj9bjaDMuKfNknFfX5dSgSKuGNq1kQaTrQ92l-Y9dAo8fBJ2q92K97dOFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=jovLHgUQnQQWFlC6uIBqHtwCO8EqSwg--YWiIiYTsBAgKDyhG_ettsvA2BLXzXAlsAG-tUEU1c1tPrBwVzpPMGv7ZbTWTuamTdxF4tid7wxdUOqaSyynF-Wdw05j878ba90sfEFknsrkpKo_48VAzj6J2DIr-fYrQP_MVb4hkpgdv7CkiH-bKWRRGn4u9Y_NJErjCZIE2xROXhulg46UV4OAQ57ts6-KnQ0HBHXU35JuhGnTM5Md-UH_RAyEwJyw4fOHeBbXOtTeV-EAtYg1n_aSLZqOaJ3XPipXX-uiNT2LtKKPdaFM6vixTzUxRVWztcknECzgmc3OJhmIKzqMmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=jovLHgUQnQQWFlC6uIBqHtwCO8EqSwg--YWiIiYTsBAgKDyhG_ettsvA2BLXzXAlsAG-tUEU1c1tPrBwVzpPMGv7ZbTWTuamTdxF4tid7wxdUOqaSyynF-Wdw05j878ba90sfEFknsrkpKo_48VAzj6J2DIr-fYrQP_MVb4hkpgdv7CkiH-bKWRRGn4u9Y_NJErjCZIE2xROXhulg46UV4OAQ57ts6-KnQ0HBHXU35JuhGnTM5Md-UH_RAyEwJyw4fOHeBbXOtTeV-EAtYg1n_aSLZqOaJ3XPipXX-uiNT2LtKKPdaFM6vixTzUxRVWztcknECzgmc3OJhmIKzqMmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwsAGjnK3qiF598-739nTRWSVTD5rZj8Jd1Lyub4cRbDaqoe6Av-Z4O5B57Z7hsNDRN-919W8dRcbJzEdSdJHpaNOpqMdt0uguiLUyOdED4LJi6LSix8kRV4czRGKR7caXrC8GwAMVMvRY0pmPIejIXePkLUf9GIj0vmCQfGyLuCmwleE7O3-npxuyn8tH6bcGY8_qxIKE0usXTJtKg1KOfSNq9VWe1WyZeqTFCxKLQncBKA_S3KbMhVQC4eHNLOkj5gZPdTO1MlyaeYfq6j5q163fra4tbBbf7AG_fOF_logO5Bj5MzR2NnqdursVDWbVlYwhmMBkKUTOt3nYnCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDNIN61Z6dM8hD5i-y6ZPRWllm-eHqmNymFvpQZWE5xPq9x8HXckoeprpxY_hYIgyZ7ubL8z4SlaemOb7FVzjHgdCiywQPedOQ1H_h64FgiI3-KQOwy3v0SFgYLCH4npOI7ZEEcYT4TSTJUkivEuE7CWFL2UvVFT9Z-qGZY3oedImbgbSzcpuEYyq6scjFGd6S-0N_6fXQ7aZ7PeFixjlrvqHwJ-dHS5xDu3fzLTfiNIaD1bGPmAnsrV2yoPWsLLSbDdpsPHRLflbHwi7ko7qVpcO4vVCvW9WxBrQvjopGa_G3kDkXJQgJ412Vt-DoLDxanJLnDuBl1WJRNiMyNazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBF2BxthVexjJ1nYrtEolF9yaA1Kdj_4O5xQK6RuBI4anYHkq1jn8zELHXeU9yjJ3eWT9xhb-T4ilyU9dxonafMktAfvJqH8AKmVGXYT7y8uY3id2a4o4jLtjwLszyiVPeRbyoKLzvZTd38Sm3SNH48ZSSpTYG13EZK5ZVVJcuT94tvfPN6vzDvEJA49vVvaczwJpBfjaKVLUWvihF08vbJiJOpeqPVeu3ejugIkcO-aC7zcY63yXFfGQUQEH2eVel2O65QCQZx0rOT7rUQHljWyeaSgxBHHP8FdukqFCvzFpQn_6hrX2b2pEa-3H2MU8a2N0UbOmqR6-SaiNjJxDB4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBF2BxthVexjJ1nYrtEolF9yaA1Kdj_4O5xQK6RuBI4anYHkq1jn8zELHXeU9yjJ3eWT9xhb-T4ilyU9dxonafMktAfvJqH8AKmVGXYT7y8uY3id2a4o4jLtjwLszyiVPeRbyoKLzvZTd38Sm3SNH48ZSSpTYG13EZK5ZVVJcuT94tvfPN6vzDvEJA49vVvaczwJpBfjaKVLUWvihF08vbJiJOpeqPVeu3ejugIkcO-aC7zcY63yXFfGQUQEH2eVel2O65QCQZx0rOT7rUQHljWyeaSgxBHHP8FdukqFCvzFpQn_6hrX2b2pEa-3H2MU8a2N0UbOmqR6-SaiNjJxDB4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHFKAb5c8Le1mNGYFpByUd_SCUOxo0ip1BrtRAfI3c8JOC_6HGG906-IenRDlc5MzRU-rmNikITPCgA5JTDEgauCErY7_DQf6RidbS8vj2WklKR8-Bu7sATHOf56fh8cnYO5_sPpbvQ0TFuABFgPoLO9MVgZB-T2Ga2VEsaTlNr-z1NUa4qIWuBDc78QI2Rap0SqfNWglnyIQZ7ECKYj0qpKVAALwGk7kv6E8Nns2ihw08WpJZKApaCcC-amLKfr8E0WA3jL5lhV-yLC0b30KkdGCvDnXPKHX3ZxPUDsBGYxFa-0G-8AAdMXwoTFnA8UbrgVXB1cz9F7otszuQlcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9jtepvBhXgpQDACdjIm4QwUxD1ZZaw20VFyTVXhyftxstglgKt2t8dYi_VazdRxcfWmy2IPrjGRDZjwG6Y5wVNok3EGdfK3F8Q4wJumcf8a9FOjPghgeU18n88yITwAzXMc6-NMkSfzXjD97Jybx7mM9Rp1WF8Mo8RVi2zQSbY8oIhVWdLpNLJEeESkCY55mhKqNcG4HWb4Fdo_gV4ReW_-GVEVcVDOYd9YBHkJ4P-qgAF-GgGH9IXUsjQoZb40tlUVP6Mqj6dd3BhtrAdRPilm0TQRghliuDW7tZloQ10KfvHRaKL55WQsy7kXbdhVDZMKp305n_JNHvK1v3kQxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=R9zuTaur_DLS01PvovfiEjHH_FYC2E1ZRMlFCMa9BfkekSITSevQw0TLEiPgN_80BepfQqwPGcCeHcqYVYn_CQyA6KRbPjetf5jz_9FVkg7msnvbYw1QJPWL4Nko389hdVTgNpJa7biD7DPOmtAtu_o2hWTUJ09hs7QjrYr4MF8PzmdLFaSqIOyns51sLdeOXvvTHpRIjAndHv_abVnMtDKg4El_aXbVwZybx5E1IVMie8wGonXAIYX4Tj4NFReBpGSBipudaMVSuPLx96y31gBY3fDC8d-Tc1puLQftD0TKuUzps5jiDCWv930iObTehBXZWbeD0yMZzGTearZDTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=R9zuTaur_DLS01PvovfiEjHH_FYC2E1ZRMlFCMa9BfkekSITSevQw0TLEiPgN_80BepfQqwPGcCeHcqYVYn_CQyA6KRbPjetf5jz_9FVkg7msnvbYw1QJPWL4Nko389hdVTgNpJa7biD7DPOmtAtu_o2hWTUJ09hs7QjrYr4MF8PzmdLFaSqIOyns51sLdeOXvvTHpRIjAndHv_abVnMtDKg4El_aXbVwZybx5E1IVMie8wGonXAIYX4Tj4NFReBpGSBipudaMVSuPLx96y31gBY3fDC8d-Tc1puLQftD0TKuUzps5jiDCWv930iObTehBXZWbeD0yMZzGTearZDTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=KyC0oUF8DcbIyycgsVZLY3bt0IuALcc2bJOUfudTU76mT1XSNq5Tj-y0sJTw00L4U7VIooF5MDcp55Z4pHCCC9oK5AwlzwgM3EgJCDOW2c48VYYNjPGs3qLrkoT0xYi0Fbz5yyj-emFv1ZMmL0kahGOk9eD7qqSsM14eA2m8y00upFA3PjAGQCE1TtvyZum_UEXstYoz0dcc9PWewXvxnAMuRm-5ZHopzyQG2nlzYefmfvpiv1u7EdFGW3nO8k6oHLQpLxvS4x77QEIMxXDM_HJZpuP4cSm5dXVZRjq2VJGFjFM9gTqGqB_EgKQsRYdZbp69UdGO4BWNwylxufSglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=KyC0oUF8DcbIyycgsVZLY3bt0IuALcc2bJOUfudTU76mT1XSNq5Tj-y0sJTw00L4U7VIooF5MDcp55Z4pHCCC9oK5AwlzwgM3EgJCDOW2c48VYYNjPGs3qLrkoT0xYi0Fbz5yyj-emFv1ZMmL0kahGOk9eD7qqSsM14eA2m8y00upFA3PjAGQCE1TtvyZum_UEXstYoz0dcc9PWewXvxnAMuRm-5ZHopzyQG2nlzYefmfvpiv1u7EdFGW3nO8k6oHLQpLxvS4x77QEIMxXDM_HJZpuP4cSm5dXVZRjq2VJGFjFM9gTqGqB_EgKQsRYdZbp69UdGO4BWNwylxufSglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=s2-CnjEKwlz9tFzeC8u-wkHXtn79jLz126cfzaY8890J1mkyFXsv5KbG3NoNtbyHxApChZQAd3rYxTeZ9QgX0_KNG-mFlRwAMm_Jqd3vcgB-2dgNgDka30EQdk0mb_d8eBPfRUzw_93Wo4zOqahgL_DjunYNv6bFsPqNZMi5dDjclA7QGu8kuZXlqX3KdVAi1TdJIQ9PEkpP6kbHpi3lg8sCuWnE-4tV_hGyKYo1BBYgsq38SZYGvuKTEdBFZ27EzCjEXfOQ-ZTKnXvI56Kvy4Re78wX45hIl-XX2U9cyHM5RxeFmChtFOi_d3OxA9_O9CJ3WYbyFHFxCuEGdhB9Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=s2-CnjEKwlz9tFzeC8u-wkHXtn79jLz126cfzaY8890J1mkyFXsv5KbG3NoNtbyHxApChZQAd3rYxTeZ9QgX0_KNG-mFlRwAMm_Jqd3vcgB-2dgNgDka30EQdk0mb_d8eBPfRUzw_93Wo4zOqahgL_DjunYNv6bFsPqNZMi5dDjclA7QGu8kuZXlqX3KdVAi1TdJIQ9PEkpP6kbHpi3lg8sCuWnE-4tV_hGyKYo1BBYgsq38SZYGvuKTEdBFZ27EzCjEXfOQ-ZTKnXvI56Kvy4Re78wX45hIl-XX2U9cyHM5RxeFmChtFOi_d3OxA9_O9CJ3WYbyFHFxCuEGdhB9Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=t_GVDP-i32Zd3MLJgaQbPif8vvGh27V44hqi0Z2zlFMPkxjDe353CaL-8P6PmJ805eNq4O6uEu-0qX9dg2OXayKuRJ3Rri0dl2Syz13nlRJjlwxWT2CprjHYklBxEfnoILHd1PLi7eo_0Ak_gCvY8oYP-C7Qp1cJ0NqRWCOsXziny3dlioEYXBrZk4P_2omgU6de4kkLNoJmCNyPfpTiQZcqK1BpSwEa6QMpeLAsRJNinmYTP3JftYTru8zf7X94UUd2UzqHotS0XJqnt7jQ_w6dpwlUQaLVPWeJZXUmGgmT-Txl7qb5X85y5N1RjyG73O3eAHC0kdUVwAIqlr3gJjVbbUH211-7Y8m4bCWLr4aQMg6A4OHoN6_YGiMwxQZyYcJdE3dy194a2SmEAjLUChfiAHg-TKVRaVG-W3QHoAtu6pZrhfzbP0MejIcX6_HgF2oX5dkPdm6nCWeBuo_qF2h7ckWMqvAKIwHpvXt8Ry_nKjFazcZdQ6sgzRF6OQEN77fCs9MxUVq5m3kE0rbwJyKGb6_DAbPHHCbuAbuidi8aNgN9h3PsRJmTkU_vTCG6et-w-fWec9IUOBIAMMMpnMv5jgRmArxjkJ4fgY2Eb8-7K-dauYmi6ylns8uzPx7KlU4heuCq4B5BfBJVCV5kMS-V7O_PkPeWU1QdkwA-8EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=t_GVDP-i32Zd3MLJgaQbPif8vvGh27V44hqi0Z2zlFMPkxjDe353CaL-8P6PmJ805eNq4O6uEu-0qX9dg2OXayKuRJ3Rri0dl2Syz13nlRJjlwxWT2CprjHYklBxEfnoILHd1PLi7eo_0Ak_gCvY8oYP-C7Qp1cJ0NqRWCOsXziny3dlioEYXBrZk4P_2omgU6de4kkLNoJmCNyPfpTiQZcqK1BpSwEa6QMpeLAsRJNinmYTP3JftYTru8zf7X94UUd2UzqHotS0XJqnt7jQ_w6dpwlUQaLVPWeJZXUmGgmT-Txl7qb5X85y5N1RjyG73O3eAHC0kdUVwAIqlr3gJjVbbUH211-7Y8m4bCWLr4aQMg6A4OHoN6_YGiMwxQZyYcJdE3dy194a2SmEAjLUChfiAHg-TKVRaVG-W3QHoAtu6pZrhfzbP0MejIcX6_HgF2oX5dkPdm6nCWeBuo_qF2h7ckWMqvAKIwHpvXt8Ry_nKjFazcZdQ6sgzRF6OQEN77fCs9MxUVq5m3kE0rbwJyKGb6_DAbPHHCbuAbuidi8aNgN9h3PsRJmTkU_vTCG6et-w-fWec9IUOBIAMMMpnMv5jgRmArxjkJ4fgY2Eb8-7K-dauYmi6ylns8uzPx7KlU4heuCq4B5BfBJVCV5kMS-V7O_PkPeWU1QdkwA-8EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8v2VhaAPhE093de1wm4n_yMa2oRRBBiy87eJJeRGuzCE7W-R-EbjPqqS1ftDXTMm5wwQ9gaUPSID1abXQiIt2-epluR9OwB9ZmtjAQKz2kx9zVAK_3Jm3VVFUJJLYtt4bqzbHTjEVQVphPe2IHn-Rn1FaPEG6Zu8zUNzrRhXII0Hl2Bgv01gJ5LX0sE14oXQRGxyTj87Qshv9cnd0OG0ZEVmaSIjhq44l13KPWnkfillp8X6caehysZK5ktxzsGHdWRuuQMia49Q6JPGLGB5pK8cnYYGwj8gtEajbrGnPtcvsSpjKP2DpKrwFmvp01f_gEdDixiy_17lxZW9acvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkwlUnZhL3CPV8luQqg03XWwgGYX5KZn442wzL91TRo2vjqPLs88Ly4MaWQRgHjc-a0RNnW627e6MCFgq7jk7SGSCRLuMJHctc1YweflHTAHymppVpNz72lUd8-wiTxIS_gQg2jetzCn-E_oe0s-piJrup4rg9brSfcmSv1RRNhG7NKhPJWf4Jw3eIDeJpL-QPej-SOaUe4cyXNCVQG1N_esJMWoyK4fgw2_2cb_YhAJYuH4Rp1_D15VFpyLKdd2kMRD_8ye5_xyrY1BKUe4a9Rxdy48N2-iCfVgNauelZS9LJA3yPS6usNF0EncS40kcSIFkNXbk1ERh7Lj-6aaPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRRug0pP9wV4upOMhfY6k0V-_pxGfKBSSINU93dshm2rjjGHxFoluJHtYy3R_ViHb4ugfVTbfFLzgsQ8LMICI7soFNC3nWloia-uM9HfvxBMzHdFzwY23Z6Z3HkHSBkdgbtF6qkS19CcmIB2hYC1i9wpGuYSrRVB6kJRDV9TXn8bb0daHbQDa30ahrU8f9kdH1SuPKyV5nh3xnxgHWQ5AUx3j8gvMjWTaO-G-1HI_lAy65yPGA3qFRZ2VU3qB-Lph_trzVRjlhm1TUo91G-E_-1XQFqwvlaxgBPEnjhbIgES-KDG8qhfs2jX-F4GNO-7ggEX7W2Q2rDjPMJXwlqviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGuLf2SFAIZsqL7KesGdTQFcg_7z4RXTxRwNoEdG9eT82kdFuc0hC_PCimWnwsErtltRHggh-e6sehdpynM_33p6CiPr7e6cayxEaMnlEzeQgJ5FWELZogsKiQa4yl-CPnWWXK4SSABetacm4zvjaN7YtJS0wWlEhZQpRLGm3LlZ72LqxsBeaExf1KN4iSCNJvW6QNMiSgbU0vcF8eo5vK_1kyaSLwnnim5yq6l9omEVjwon-qctAhI3v2prMyDZPR60xbyZB361QpeMDIhTsKbanbagyzj1rFru87-CuLXTtm7fdo26p40fEuOkqFmmBN09mtDtIP3IpurtA_KTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFit_38-6GT_EtNg_LsvtVPezmNAIcteE8OJNFOheHRouxyRGKOl1PP6aBrDrPlgU0REYQIgsCYMIc1LmzJqbYHM3gKlDC0yronIV_CVH83nJT4Es6CFRFJslwe5nRIapp51-cakqf0_zJxkdLxFkfQE0r62r9FGl97haHICvAMNqoSDRCcpiKw2hiDyGyN1mCQUH34Lq_sl2yZEaBxoqY85EeQRhj8DCreoz2ZfFlcjwfM0MRhF7gzuS4GzvV49hGzN2_NUdZOFbvEvCZuYLNNuNvQPcCg1cuory50Cem8XFRwAj0R--h_8X76wEJ1aHC3DG7_dXMTE_qpr8zy8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXHP1l8Cc1SJ_efKVm9AV_JsaMCo7O1sEfA84odzXr06o_Zy3QZhBl8diPsTi9Nm1weNAQXQJ8ZlcS5R5jC8p7tyOFpoSP9lGPNpsX-9ZhiPt5i0BNAtUdFrE2j2fPB5fq46IWz4iCc7zmR5LYLDsdk7n7PcvFSPAbmSjbKezp6lAtvXAgyn605stY1W5mbXZN8Pe3SeONXQqTi4BFicAFODbcALcvXHpx88Y7ZSRvx-4-S_uhLgoBvSWx7AtnbaFNX4mbGv1YtyC2W9jMcpkqgtce3yL3TNlGIjWuZI14lapy4D2wiysouUjpaxOm46R9MPlK_Wl2dSvwZZgFtssA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpooKfN9T0smlLXWi_l79ngjKoJYNWGN7jnfotNHOEDu3vHuVRJfGu-EZkkmeWXR1PPu-I1i-flyBfB_bFtTTLeE-Qh4y7SJ4nN_Jukx25HRGvYz-hc5mAR6GJj5_pQynxMuH9jLUHunpuVXfOLozAla-Fdo_ahc6sXQ3LsZ2OH3rUaRxl7Ewgatl6YeCn8QfYKZX0t6U1_ZEpm_tobiYb9FvUAswFYrtKSTKVrlU2bOtFW7XXiOghhMxYb-j3X5Kh5DnDXlAuCDundVp0ZcnUL_j9z8t2EVPJCnvuUE5rAt8e2uwuKcOrVn1XByLt60icz4d1it0II6bWCVZcsBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=S1d6kD-bApAyPUrCKLNLMUMk3TtPvsd3Tk9BzlB3TQI1xT9o6_17FrngsB9D7tpGMfP5VqrB0VsslJ2RewSmvNWZPPcGzBDzHCXbzdnT5-VLTAuwqf3NXHjtuVAeq4xoD6UzjlaW4HonmXe6yso4Of7BGs4lMC0uNQpBWWVVTgNjB5faxdQLL8W9BT3nAQdHlzwTkeWaNmvavoYTIEg5TF1vp0RgS8DdvQWXcu9kHQpVN2qWstF4UbZ-xWP7inPrOs9cNcqowAFSUkxeURGkqKkSX0lEId55uBjaHVhxQmi0sAHY5RemDUpg13235rY2ZWYXWO9G8f19e325GW-_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=S1d6kD-bApAyPUrCKLNLMUMk3TtPvsd3Tk9BzlB3TQI1xT9o6_17FrngsB9D7tpGMfP5VqrB0VsslJ2RewSmvNWZPPcGzBDzHCXbzdnT5-VLTAuwqf3NXHjtuVAeq4xoD6UzjlaW4HonmXe6yso4Of7BGs4lMC0uNQpBWWVVTgNjB5faxdQLL8W9BT3nAQdHlzwTkeWaNmvavoYTIEg5TF1vp0RgS8DdvQWXcu9kHQpVN2qWstF4UbZ-xWP7inPrOs9cNcqowAFSUkxeURGkqKkSX0lEId55uBjaHVhxQmi0sAHY5RemDUpg13235rY2ZWYXWO9G8f19e325GW-_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm8zth6eN54i183Bay9-Rv6qRdw5-hJTvKcSQfQeSmnqFa_QhiBwaxcqPr4jQni7TwDJ0hoZepZ_jueP4Eyb7Yz8hPS29Sv2v8kT1Dfz26zw6AKGbCLYL33nmjT1R-W7wfkI9gXXmbaIwtAyFLLAqga12s_PYils0jOWFNfsE0GH2bMZD1TM1L1W-PYU7NCcjrJUxr5nEorOqDfN8Y-0m1t7AievxBrMTH_x-Qu6Q5NAa9r0NT6MRXVu1LTP6RwGCQvvJtzhw7FqfBuIoXMdr1sfDCanqUJvax7C-Eg7vA0IJ8flOY7ZoHONlGSdFqg3iPWstKIh9--HxLWffiyIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUyo_dQi5l5d7qaXi_8_DlcvJWDUUldkDTBnCggCU38lbqLdmBQRmwH1a2z5Y-XktVLmIiR_lJLmYk-OnqGUjD4O8un-nHhBTpRL-NxF02tT2M0QXQ203hd8LSaeR_VeL_hHorBrT5Tm5TgJuR-s51lr5RkjIpD3kg8xXUZPcbVifKYpAlc2cW9f34j99bbXhegt3mFa53D7dXpikm4lQb4Guxn8iPR3_Wu5cVvuo6CkD-7GcfY2FMbdBDV6V6rWH4vtQUk2mWvfj3-55ecE134pyB5v9PV0s_SW-z-hXbUvGpfA3YU0LtT6mB8-BHoaErPglqfG3RKbS0Nlw8zJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQLsG6Dg8pgz4rLfT6fF0BKpjUSKybwfzDkfKU1zryeFVUpyXU4GUNzMOwB_-ICShMC9gPCjE0rK5MKqUTpzFprDKDG0NM0tT3mWZIb_MalkxvkYK4xjyrlZVXMyTo5PWEJLNpPuZkqW5t_UtgzJ4vvt9GdAGEUSv9zAf_9ZzRDv5w9yxuEv3-d4RUX5VUYwgksDgJEn6n3hybdGrZ3Ez8pIj0WXXfoieFPW_oEEUwmIwPq5z2lGDu8iuKKaIkFaGdk8eO5kQ7R3TdQNG39TjEiYNPk_zS7znvW9k3FGT87ULS8lKNg-B5Dm2uP-Y3igX-ykaaLid7DasAyEx3G1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2mnIytuMSoZnniT0ltLkmKwmSAmajxsA-sBPk2K6rjM2c3y1qXCIpRAUQCZ7aNUlqQLMppgnL9VXBW4sgLrNavKXxMdKnwyXptX5lQfDhxg1Pt9y3Yor9FShN4ZaM2wvmYn_dJY3X_lL_x3jUVS33cET_MG_NhF_3nHySTOgAnSnonroJ7TSAddAFtF5Cr6HM4qEPOEAC0vmnYQHZ6xAt5NO42dqOqSI1xU9SwyPAkf5lQExlur0ExbNR5Hp_zme_OPJJ8pltfBNyKpcMgCVxrqohmsN_KtTCjXxan0ETDfP1yuSkTjCyZURhtWvzZCbypVGJgmBNTknxwj4CaZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWigYe7QyCmuvtf8TzjbAyfeFQkGoxl0g9HSKRNzDo7N7UW1sf1qnmbEQ-nE4MwUtceb_iZG_Z8wr9x-7PtzqCx8LjbjEP9EBdHXPrVECfBmGMYC5XmfPaoGdU7iLoKlUcip7-h1vsghe3B2svSrgm3XM2Fgvmw8pielHOgjjfU0QJH-KBvxjHePKH6JffDUrZGhFSex0Nke1lMaRyMcP4-nyuqsQzsYLHcpYEbiqLqDNcJERco6cpnFeQF6sJ_QJChY0E2idFUw-uSPGZsBtAxjDwC-mS60cyHuFUhfZ4sYUNEEqHL7w522imqGJj63GFgv2lH604Au8dmiD6Qn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXSvIeDFOItRRHXjWP6jd2gGPjd9YnZQTzk-5M-T6BANEj90y0c3LODNTW46zw4fdr-ssx_X9geDXQHOrcbAnkyAPnqkdB3tUTUzBcAljpPJ6LQb9vj4qFQOK3aJm4i9aOeWDMnG8pfWXiO9ydx6bKGJpCS4TkV2Sb8TE8n7eVx-lt0B5CJDOCwWGD3PgVNGEavJKWwSvToKteCC1RNyRlzYz2yGAAxmmcdZwuJ21GA9F20-EOf2vfq0DyqnfRFbdk605XPdZbpqut5bh7Ff7ltpDjgVMT82IzDQ8NLx9f3yRp4D5c9zVLSqsQY22gIfFa_-i5J-ZYbrdQ8tgaKCGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF0pp1FzzXQu97a24LKVIDJjMrFlSLlL4t1WKiEDFx3UKthu5feBogoSGz_puDE4RdALNdu2IHTpVaZc4f9RtuGKwVzFfbiVjBI-X9C4e7mS2w_lQ4k86oVVTBpcqfi7ib_3CSW228ctEuT4X_KwGVfEA60Y9VBl2cKmWLsuaMflOR4267g5Wk6u6bjICIuNjD4lmCm2D7pTH19n6OOYqFze0OqeyxTuR6HSpCbYVIDPWrgQjZO_O6e1cF2JxzdbQSG7tNo-3yQvrQ3dE39tqWTT0LijDzzVixrr6Rqg1SaRcaa0ctmpbB2U6ss6RhJLojhNSkaf6dSfffPwKLTKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS3RLStgL-KEVWRZuZuwIcuGRVQ9ZqjtwbD7DbftMiakoEJZqg4v_c9P6o_dAEZLB9Nmfxf_a6i8H1zb01DgirwlkY75iNG6VsuD69184HtZYgQRqSc6JoYbxT-TnvRo7rG4NfAojv_Ny0Ll5QH2tTJoU5omZl4X_gZLfxPLN9TZdiAWwZmIqJUOupUcDQpYT1pt15F9hQO_UcRiu-C5s0dsfw4Tt53RQ6pWAnx6dzegpujhKT4UWJYnnjb_pxygeXCAxjY7x-omWNfI9Jsg6gpIRlKIYmfSNLtrzvxb0VUmLTSPq_coNcNQaXUwS7e6w5VkVWkgiMKeznYqgNw7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6LMi_m1xco_Yr7Avkn5SztRW02jXKQRXp8YgrakycUl041CB4DRK_tjcviVKrUgVfloMYub2Gptv3htNlUOKoYJv32FDWxsAAw3RaJ91DOdWTq4nBLz2yjgWtUaQsaIXnN-idreVg9DqQHwWddTloWvmvWOFfF7JE8snBXWCuJ3qOZR-rey0WXunLWJvzZ4PRI4pA1DAVVVmwdhLSJCEtdguJEw0xFKLc-j0HTOj81tPUB-30YRLXtYaTeOERE4zGphWrgwgC9341Zunyib8Jq0b8Ckn2PkGGav2dc71xdZ5oowBRJOA8Uj3PYIdd3Csi7ywLdfZ6Gua6W6f2oHQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYlBiZzel-AsiE8_agIgnSrz6lot2jzR9rIQ9ybs62yL_NGICA4KDTf8ZlmR6RyitbiYpADFlU_s7WxHyF5Iw3_4MsG0y9xAWK7xVGe8UDK0zdXsF9O3Khw9Od7NJ9fNoXNSR2aym3bNLTTsQEKaYeaEWpusSFH-TUrqItCpP6cJ5i-BtYw-TSVX6ZNuUWDjqpedBz73A7tYzwJnol3f1NQnNKiPselkAR_K7Pu8qFXbZh2N_8TAX026uiOPMIqUWpfr9wGA6Sq5WpphCF5843_THqtx1RqO4H28Qpt1OI1LA9D0ZIv43y_Z5oSOJ2o6fxHi13tpS_t-O8Zz_30rQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIuKzQM-UXwst17a9Ol-yvHyb3gdFD-K8KMMfGDbFridREbR3PPiONx7FItkUCEFRUrIGaKTLjLE-SlfDZ1k_KASEvc5rAGP6vK_z49QmBSzQatOsCB-UG5CCqwNrwdReHoFiw0p8Lqikqq7VB3jDDGUZTPYc0KQCwDp9YyzuSHBiuExP6xTqWor3yHPaw4rQEcPyD1PC4G7fNZtQl2xfFStSd1smtKXoEg-iNuT0e93XXmSjv7u6EfMKGoS64C0aB7x3coQqh2pcFNvFVOgzQHXE4_GfnnO8Pu9BgKLiHc52DHC1cdCn6_Cmi8x1ceZv2Q2osA21esAQCOQShnKrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPxNWDMGgJdvkyqneQ3w4Y-zVQnm_ht9DSud1mU_xA5AfTBmS7tWDXE5X4flvZw3hI9Y5SO56JsqR2hxESHAmWOO8lvRPXaDVSItzjyaYKd1bVfyjGgVGC0C8LU1eci8NEPOU6hma8TuJ-rVgsfytjNSSvdKxHRRx9aT9U0UtYndkmTfM2bqRVPX_TB0FYOOge-NhDih2yjG6cGZG4fzKNBWD3XSdN2pgN-sFqut61FKvCgvnhKwbHMMMpowLXisEEcu1ED_4a6qFBmRJEypbnCeP8bjtmm90Mange4s4PCLMJNJB9Rw1sj3pkY26pdE5WW9YpB3BQ2DhA5T-MD4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
