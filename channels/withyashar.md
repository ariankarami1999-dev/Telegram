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
<img src="https://cdn4.telesco.pe/file/LsrkeohT1HZyMY4KIbpPif9vZ5sidyn60SJXIoNDzWa4cW1e6poaFwPnImsW8g-_E2IvwhDnPRUSKrry1hp-9gZg5__Rtg118-gylyBOfcTaNcTJsO2RyRXHWdn8ercm0A1Vn9Mm0e8T5Ayh9AeL48ZcoTOe1H2yhBgQq_ihvKBtSQREUSDBb6hl_JAUmHSajktA-7mwptc5e_6l-iK8XYvD96I1Vs6x2fQY_kacCSyCcU_U2fr3L6WTcILuEk5nH-MEsqfwKLsu_aPKssh_0HtBRcA9ilENIJ7TydJTHR881Dr_Hk4o5j0DjJNurnXU9NeBV4tbB2RCN6ElNYMtJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 388K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 00:04:59</div>
<hr>

<div class="tg-post" id="msg-18102">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3QK4jqkYfIRqDEQc4pcXkzT6mJO0rfbf5y8Mbv-fbkSUH7kUULKI27NDKuPp-Zgpp9uRfnu62ifySld91_wPlD3ayefFEeLqHyRtzzwZEJVpayJLlLV5n4NTyy49YCGBd552Xc12S_oxQTcgBujMk2-fMoftC3XODXqQVzAuVZu9odpwuM9hgoxwR_fdknwOhhQwzMeu3uwPzg7UDJu00E9nR2Eq4xekCoK96iXNrMehO9KihjzWJbSjNPMuBcyDLAaIBMSrM8c21bxWqwtuctHKputfSeTTQaowBEaGurN4yWx2uTY4EhBViULOoQcEljyX5ZPSzZDZW6HoFZIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه داری:
رژیم ایران با فریب زنده می ماند و شبکه شمخانی یکی از سودآورترین موتورهای آن است.
وزارت خزانه داری زیرساخت های مالی را که به رژیم اجازه می دهد تهدیدات خود را به امنیت ملی ایالات متحده و حمل و نقل جهانی ادامه دهد ، تعطیل می کند.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/18102" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18101">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حملات امشب در شب سوم تا کنون به این شهرها انجام شده است
💥
بهبهان
💥
بوشهر
💥
سیریک
💥
بندرعباس
💥
اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/withyashar/18101" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18100">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">محمد مرندی: ترامپ برای هفته‌ها مخفیانه در حال برنامه‌ریزی حملات هوایی گسترده و تهاجم زمینی با حمایت دولت‌های عربی بود
@WarRoom</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/withyashar/18100" target="_blank">📅 23:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18099">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUBoqamSmz6v3XXco5-53oKQU7OSkN-70ud8_26oP-V7cSKb-wWAnYjN1H-bREHFKrPpyrgYuUiOsAOmPejc-LuCnuOtgPnGd-sgz7-9zbzAx_kPSpXuf9OCrq-Wt3le3z2E_KWmeJfapfxuIHslrw17r2n9bVc3zPtHTfRAweMuKv1LS6HvVeV6yZPdIQdhHB8WFxjtolFYaq0OM3Fbxc0qivLzgmsItENvy2H23MUoDgGqHE18wRDsIDtMbhDMRvmSFGHEewT4n4ovaehVHTVd2m-TPJTSvT0HTi7l2O0MQ0sOso7ywFcx055MlNFj7IZF2DdIcAl2qqfdSvKniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق اعلام سنتکام، محاصره از همین لحظه باید شروع شده باشد.
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/18099" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18098">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش انفجار قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/18098" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18097">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">در ساعت ۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET) امروز (۲۲:۳۰ به وقت تهران)، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) دور تازه‌ای از حملات علیه ایران را آغاز کردند تا به تضعیف بیشتر توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز مورد استفاده…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/18097" target="_blank">📅 23:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18096">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یاشار بهبهان بازم صدای انفجار اومد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/18096" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18095">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اهواز همینجور میزنه
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/18095" target="_blank">📅 23:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18094">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بندر عباس جدیددددد
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18094" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18093">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سه انفجار سریع و رعد آسا به نوع پله ای سمت صنایع بسیار دهشتناک
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/18093" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18092">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آی‌۲۴نیوز: مقامات اسرائیلی معتقدند که ایالات متحده در حال افزایش آمادگی‌ها برای یک درگیری تمام‌عیار احتمالی با ایران است، با منابعی که با واشنگتن در تماس هستند و برنامه‌ریزی گسترده‌ای برای بازگشت به درگیری‌های با شدت بالا را توصیف می‌کنند که ممکن است در عرض چند هفته رخ دهد.
یک منبع اسرائیلی گفت: «یک جنگ وجود خواهد داشت. تنها سوال این است که چه زمانی.»
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/18092" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18091">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اهواز رگباری میزنهههههه
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/18091" target="_blank">📅 23:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18090">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پدافند بوشهر درگیر شد
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/18090" target="_blank">📅 23:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18089">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDd0G1fXJ5t-8Jmmzogd2hdseSaHyu3d_-U41Qu6XEmKx8tdd5rDcp65MWAE84tlTqvFDKSB6uOyMUfGgOQGDcfQO9tTlNYHq4vRC4-_XUQl2BsFOf0NU_FhnhlKhZshgUH7TmXuX5_h7G9T4cfahryVgtozk3yhJiuEAp52rzeEVGOBI6dAjQw6H8pwhf8EQTydndRhupw4iFgNfBtgCdKfuGOmZsLR46E69lDztPVh3umCPTsaHyqgrb2_NPV0hFMEhQp1Wd4aPaCkIi8XMEW7EpxvYBHRhh3ejcGz9snhyfko2ZcOzFU2p56GIiS6Y_oOc_WGbGlFxoyc4e8BHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین عکس ارسالی شب سوم حمله : سمت شهرک پیامبراعظم بندرعباس
از لحظه ای که علام کردی تا الان
۱۰ تا انفجارو رد کرده
لعنتی معلوم نیست چیه پشت اون تپه
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/18089" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18088">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سیریک رگباری‌ میزنه با صدا فوتبال میکس شده
🥲
قوی باشید</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/18088" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18087">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فیلم و عکس هم بدیدددد</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/18087" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18086">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجاررر سیریک
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/18086" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18085">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">۳-۵ انفجار جدید بندر عباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/18085" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18084">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اهواز چند انفجار جدید
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/18084" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18083">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSsNV3NJc_pjeUxideiN1h7SnsyYVKCXPaZfF-gRBvowYO7F68fiHqpi_CZev8jK1X7qhxpHtGZCx1WxRKydNY0WPWGBrF-167JkuTnb3L9rhg3icXjswO5Q85qwIpWN9pmOS7mMVdeMUgUBBHy22esjot2AXHcSNj4sJ_HWj4dkH4ceCfaJr64ru2LofQzdN4RxVCXBywdUDX5sLvbxO63XYSMCDY62kEkkpT8xJqp0y83N1WhQw8rSweY3KW4X9pPVYHhQb-DMXIICeHRL_JjlPoB1IMdM4Ix0Gyp3LgLKl8t3t9cXO0_GEDJ4DxvHXJsjb8CT3F-4LESSkNuAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ساعت
۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
امروز
(۲۲:۳۰ به وقت تهران)
، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) دور تازه‌ای از حملات علیه ایران را آغاز کردند تا به تضعیف بیشتر توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز مورد استفاده قرار می‌گیرد، ادامه دهند.
این حملات در حالی انجام می‌شود که نیروهای آمریکایی خود را برای ازسرگیری
محاصره دریایی
بنادر و مناطق ساحلی ایران آماده می‌کنند.
قرار است این محاصره دریایی از ساعت
۴:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
(۲۳:۳۰ به وقت تهران)
به اجرا گذاشته شود
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/18083" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18082">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سنتکام:
دور جدیدی از حملات هوایی علیه ایران را آغاز کرده‌ایم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/18082" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18081">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ارتش کویت: یک شناور متعلق به نیروی دریایی کویت امشب مورد هدف ایران قرار گرفت که در نتیجه، چهار نفر از نیروهای مسلح مجروح شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/18081" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18080">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شمارش معکوس و لحظه‌شماری رسانه‌ها برای آغاز محاصره دریایی امریکا علیه جمهوری اسلامی ایران:
55 دقیقه تا از سرگیری محاصره دریایی آمریکا بر تنگه هرمز
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/18080" target="_blank">📅 22:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18079">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۴ انفجار بندرررر ر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/18079" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18078">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">لشکر 192 اهوازو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/18078" target="_blank">📅 22:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18077">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/18077" target="_blank">📅 22:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18076">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">۵ انفجار اهواز
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/18076" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18075">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/18075" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18074">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار در کیانشهر اهواز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/18074" target="_blank">📅 22:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18073">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وای نت : فرودگاه‌ بن‌گوریون به حدی از سوخت‌رسان پر شده که ممکن است باعث لغو یا اختلال هزاران بلیت هواپیمای غیرنظامی شود! @WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18073" target="_blank">📅 22:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18072">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">۲ انفجار دمشق
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18072" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش های بسیار از‌ درگیری پدافند شهر اسلام آباد غرب در استان کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18070" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رسانه های رژیم : دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18069" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFP3HwDOZWWNUTUq0NkJBEfOdaLGeDjxKnYhjh4KnTcrOKmhdjVX03dthtgL7MlI2jhuuB0NjmBy9gnPx_sXB5NSGeu4A756O_rdPZJpBNU9n_uQhyl-cYLeTuI4PoHJ1DmECNfyXZdYwEO95OHw9ax8D9xG_wVOo3QPsn3XW_4IVuf4ACOlV8URSBF0R-cmzLo_7XaWe668s7fy6NCHVFaA2nUeL3plnP89diktGzH5wyEpZBMCjsJ7ejFnzH8oO7krgkG61Q0pCSV00YseiFxIUoNpp8lYpYsmhRmYI651roek77L82_Vyot7MHg7k-3nYiXM23QkYbQfhYE-JMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اولین بار در‌
تاریخ
!!!
یه کبوتر جای درستی میرینه
@WarRoom
🚨
🚨
🚨
🚨
😂</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18068" target="_blank">📅 21:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آموزش‌وپرورش : دانش آموزا به هیچ وجه نگران نباشند ،حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدن ، با خیال آسوده امتحانتونو بدید.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18067" target="_blank">📅 21:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کابینه امنیتی-سیاسی فردا ساعت ۲۰:۰۰ تشکیل جلسه خواهد داد. @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18066" target="_blank">📅 21:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سی‌ان‌ان : حداقل ۲۲ کشتی تجاری در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18065" target="_blank">📅 21:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437c5a5907.mp4?token=KYIzVZWVyG2eDXIJKvuLZMw5oC6tcx8JbSclJAhLEsIjHyAkLdi0V8BX9rsXS1Ymy_H_rcaOrGEAvEC0eEAIDgSWMEwOYcIXRssRuGevs7OzTFh33wWTC8yl7Hgl9mLnhGD0Km6WHQfXq4yOMeaBwQYt9iA-gp7Hpy_4SmQ5K7hyXSFqAckUOMX3ihi_l07ZjNRz7TpbFI-ezlGIZjTVUjPg27PSwqhHqJ440gyVhVQJCY2wQ7L1bkwos6vA-4BopnVEpMxAnngdnFnc2B-sbtSV43pF0d14OX9CASaION2L2F-cCMgAoumhuBNPC5zOBfMPFs9SCYs19lkCXhtaXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437c5a5907.mp4?token=KYIzVZWVyG2eDXIJKvuLZMw5oC6tcx8JbSclJAhLEsIjHyAkLdi0V8BX9rsXS1Ymy_H_rcaOrGEAvEC0eEAIDgSWMEwOYcIXRssRuGevs7OzTFh33wWTC8yl7Hgl9mLnhGD0Km6WHQfXq4yOMeaBwQYt9iA-gp7Hpy_4SmQ5K7hyXSFqAckUOMX3ihi_l07ZjNRz7TpbFI-ezlGIZjTVUjPg27PSwqhHqJ440gyVhVQJCY2wQ7L1bkwos6vA-4BopnVEpMxAnngdnFnc2B-sbtSV43pF0d14OX9CASaION2L2F-cCMgAoumhuBNPC5zOBfMPFs9SCYs19lkCXhtaXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لانچر مشهد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18064" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فوری | شبکه ABC به نقل از یک مسئول آمریکایی: نیروهای آمریکایی در حال حاضر هم حملات هوایی را در ايران انجام می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18063" target="_blank">📅 21:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فوری | شبکه خبری ABC به نقل از یک مسئول آمریکایی: حملات آمریکا به ايران همچنان از چند ساعت پیش ادامه دارد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
یاشار : بابا من میگم میزنند! بعضی نمیفهمند !</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18062" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18061">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">توانیر: از فردا قطعی برق برنامه‌ریزی شده در شهر تهران آغاز خواهد شد.
@WarRoom
🥲</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18061" target="_blank">📅 21:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18060">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">موج جدید حملات موشکی ، از لارک موشک بلند شد
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18060" target="_blank">📅 21:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18059">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پایگاه هوایی شیخ عیسی و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین، هدف حملات موشکی و پهپادی قرار گرفته است.
@WarRoom
یاشار : هدف با اصابت فرق ‌داره</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18059" target="_blank">📅 21:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18058">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حملات موشکی و پهپادی خصمانه جمهوری اسلامی علیه بحرین و اردن از سر گرفته شد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18058" target="_blank">📅 21:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18057">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxFUMo6Ed7E4LOJuRN50Ll6_O3NHAK7xBXOeowQZpZCPmqUk7EfRlSFasg-UTHgzbEWAJfYS1MhcmC6ArXxri3csy4iRNm5Ibx83iSAL5xysHmRD2Xpp0t-DYFFyu8_Q6imvUwNYLE-ViFFPasEYQyNkO69V-8lkh4p-uza6nX9ZXfPPiLWD2rGlmPUqyTgzE9D6ggCkniP9qESb8fe-t8ExeDPYoHuTCL5pRuN2yP0YXoHSh8jEjMDnbsFHTiivD4w2elPdeWqbeWqRActBbBLBfoGxQTjsy6Rkepa_jl9VV6vdVx9AeJ7en8KxGptx-TWexM4gO147YtfeOlT3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون آسمان بحرین ، جمهوری اسلامی از موشک های خوشه‌ای استفاده کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18057" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18056">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شلیک موشک بسمت بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18056" target="_blank">📅 20:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18055">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50324115f7.mp4?token=XNG4hwf7hP1NWDsOlFUioVUE_ib56lhqAVS_yAVuUaZhNDDQLjc-eGp9aK7Tvlv1mjUmxzePPGebDIwbulT7JAuCfhJBa8mpn5xYSeDuegjpSO48y3xeguq5GP-xBT1qNpOtmf5jrZaVHR3CShPeC5g5PA5_uRt4l2lFK011pk7o2iWeTe4-SkK054kY33Gpo3SRoBfOlJbVQuW-zYASd-eAFKVfzP2c9k3wuZvZftu9DEWxa87KcktOCC-b4k6YrImEnQxCdtM-BkljXDhbm8BJaq3CLF3xI_Ch2HUTaxqDhZ8zTWTOrp5kZc8R_rJIjODkHv6SU454P3UHKuljVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50324115f7.mp4?token=XNG4hwf7hP1NWDsOlFUioVUE_ib56lhqAVS_yAVuUaZhNDDQLjc-eGp9aK7Tvlv1mjUmxzePPGebDIwbulT7JAuCfhJBa8mpn5xYSeDuegjpSO48y3xeguq5GP-xBT1qNpOtmf5jrZaVHR3CShPeC5g5PA5_uRt4l2lFK011pk7o2iWeTe4-SkK054kY33Gpo3SRoBfOlJbVQuW-zYASd-eAFKVfzP2c9k3wuZvZftu9DEWxa87KcktOCC-b4k6YrImEnQxCdtM-BkljXDhbm8BJaq3CLF3xI_Ch2HUTaxqDhZ8zTWTOrp5kZc8R_rJIjODkHv6SU454P3UHKuljVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای نت : فرودگاه‌ بن‌گوریون به حدی از سوخت‌رسان پر شده که ممکن است باعث لغو یا اختلال هزاران بلیت هواپیمای غیرنظامی شود!
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18055" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18054">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارشهای متعدد از مشاهده ستون دود(احتمالا آتش‌سوزی) خ دماوند.میدان امام حسین تهران @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18054" target="_blank">📅 20:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8fc831a4f.mp4?token=dIPYRAVdTrP1PzOHjMxu07hRHYRlGaGJgSOpSnPput9GxFoP0wAjZG01CySRvbxAuCvCgg0r1LsSkFtA-UQgoi0bqHTviECrrnbGvWaJGB8keDBFDBDvO56JrgfGbOZzbo3TTiR6rBMLPTxLNCEduocG4r21eSQaNWtLGrIlNShyzv28iabEQGa3vfRh2GM5CvLfxpIsxoHdn86ZO_TWNBOSFPqHaPn7pHcP8bbnJ8pSSExwQ822IRxvobgvmjATgIrjwmxsLzCPNf0_FhaBs0gbyS_5J96HeG1WZWYqFdQ-wkPOMndRBsUzRChN4HmTOTKNcvZ-8m03_a6j-G6xsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8fc831a4f.mp4?token=dIPYRAVdTrP1PzOHjMxu07hRHYRlGaGJgSOpSnPput9GxFoP0wAjZG01CySRvbxAuCvCgg0r1LsSkFtA-UQgoi0bqHTviECrrnbGvWaJGB8keDBFDBDvO56JrgfGbOZzbo3TTiR6rBMLPTxLNCEduocG4r21eSQaNWtLGrIlNShyzv28iabEQGa3vfRh2GM5CvLfxpIsxoHdn86ZO_TWNBOSFPqHaPn7pHcP8bbnJ8pSSExwQ822IRxvobgvmjATgIrjwmxsLzCPNf0_FhaBs0gbyS_5J96HeG1WZWYqFdQ-wkPOMndRBsUzRChN4HmTOTKNcvZ-8m03_a6j-G6xsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ایران ما فراوان سپهدار است
⚔️
@WarRoom
🇮🇷</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18053" target="_blank">📅 20:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش شلیک موشک/صدای انفجار از  تبریز و شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18052" target="_blank">📅 20:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ارتش اسرائیل: ۴ تروریست حماس در شمال نوار غزه به هلاکت رسیدند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18051" target="_blank">📅 20:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18050">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_LYdNIi0E-9f-0BS9Ewc37tU7iE2mJRQfYD96_w6tiPOGZ3EfCMas7T3rS1nzfxlFMNTAM-ka7GBiMS2r9aD1v4t_1qNWwuCdONiYQHXqgwnALqmY3-GW3dJkrtBcu7jCtyd6mI6aBpPiR23CNMn4vWJ8PZp1A_YGwvi7SL4yiik68Q0zc_isgq-BVxxVtah8EKBR_vKgBf5qYTGcaV8wWkUnTqm4QelP2BCtfNJXGHuIiL92K0kurXhDtC8wyxxOi3Sg0tZa2h4l6CfPFusD4ioour9WkYIh0-EySUcTom5WaB1XPv-XDQRcMjRCGyRdkTca8LOBEl5iP9boK-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانری مک‌مستر، فرماندار کارولینای جنوبی، اعلام کرد با قبول درخواست ترامپ ، دارلین گراهام نوردون، خواهر لیندسی گراهام، تا پایان دوره تصدی او در ماه ژانویه، جایگزین او خواهد بود.  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18050" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18049">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حزب الله عراق: در صورت جنگ علیه ایران، مشارکت نیروهای مقاومت فوری خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18049" target="_blank">📅 20:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18048">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammadreza</strong></div>
<div class="tg-text">سلام آقا یاشار.
خداوکیلی تا آخر هفته تهران رو نزنه من یکی خونم رو میبرم بندرعباس ...
داره حسودیم میشه به بندری ها.
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18048" target="_blank">📅 20:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صدای انفجار سنگین بوشهر
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18047" target="_blank">📅 20:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ماهشهر صدای ۲ انفجار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18046" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18045">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرنگار: آیا لایحه تحریم‌های روسیه را امضا می‌کنید؟
ترامپ: لیندزی آن را بسیار شدیداً می‌خواست. آن‌ها دوست دارند ایران و حزب‌الله را به آن اضافه کنند. این به افتخار لیندزی است.
شانس خوبی وجود دارد که انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18045" target="_blank">📅 20:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صدای انفجار/شلیک در قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/18044" target="_blank">📅 19:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تنگه دعوا شدددد
🚨
🚨
🚨
وقوع جنگ تمام عیار در تنگه هرمز،
سپاه هم از حمله موشکی به دو نفتکش دیگر در تنگه هرمز خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18043" target="_blank">📅 19:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb5168e57.mp4?token=h9mkSkPAmQ7JS2sdsctZhw2E7H3EKSuThKClFjW6IFypvE7dxCDojlv3OqfUODnFVyyoIhKL6Q4WF16N4yeCc4ZbOM25i5gOAtDHiWVJlnBWUe0lxr8fIRcHqddiURu6P9Ot_UVZpJmhw7blpcLuJQvCmbPOlTEUwG4DGo0wuEq3ffyPBmtt5qo84-uQ16ByQln6A2KcCON8AUMmU-MAbGxhOvu8D6XZmR1KRsFQVGbf9Yabtj6bo-vfufh-L1ZW9zCEnOqXOXNqNtBTfvrRySv0BABU7KLwdYgg8lpu98JJt2-5W1AC9sYmTzBxtA7LNQc6caCv5NsKO-gRDffCCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb5168e57.mp4?token=h9mkSkPAmQ7JS2sdsctZhw2E7H3EKSuThKClFjW6IFypvE7dxCDojlv3OqfUODnFVyyoIhKL6Q4WF16N4yeCc4ZbOM25i5gOAtDHiWVJlnBWUe0lxr8fIRcHqddiURu6P9Ot_UVZpJmhw7blpcLuJQvCmbPOlTEUwG4DGo0wuEq3ffyPBmtt5qo84-uQ16ByQln6A2KcCON8AUMmU-MAbGxhOvu8D6XZmR1KRsFQVGbf9Yabtj6bo-vfufh-L1ZW9zCEnOqXOXNqNtBTfvrRySv0BABU7KLwdYgg8lpu98JJt2-5W1AC9sYmTzBxtA7LNQc6caCv5NsKO-gRDffCCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونا اول شلیک کردن و این اشتباه بزرگی بود، چون از همون موقع ما حسابی داریم بهشون ضربه می‌زنیم.»
«سلیمانی کنترل کامل ایران رو در دست داشت.»
«رهبران ایران از سلیمانی می‌ترسیدن.»
«من اون رو کشتم.»
«کشورهای عربی به من گفتن: "ترجیح می‌دیم توی آمریکا سرمایه‌گذاری کنیم تا اینکه بابت عبور از تنگه عوارض پرداخت کنیم." و من هم از این موضوع خوشم اومد، چون نباید هیچ کشوری بتونه برای تنگه عوارض بگیره.»
«در مقابل این سرمایه‌گذاری، کشورهای حاشیه خلیج فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری می‌کنن و به نظرم این معامله خیلی بهتره
@WarRoom
یاشار : بازم سیگنال سلیمانی داد حمله امشب حتمی است
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18042" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ: از لغو محاصره دریایی یا اعطای معافیت‌های تحریمی به ایران پشیمان نیستم؛ من به آنها فرصت دادم تا به توافق برسند
@warroom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/18041" target="_blank">📅 19:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">موج جدید حملات موشکی ایران به کویت
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/18040" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb6044c25.mp4?token=jlJAg6VwE_a7YZzloLqAfQGPHhDxAhgIw63U8MFc2ywrC9-OqTSSBltdeqyfpODYq_8dmf_ODtchmp5Wt-obTExiu0Y20PodSKmYSxCj4_iXt3-HJRazm3xMt2qJtsuVPuYd_3QhF4r8oee5gPVILq4JUVW2j4udNqU-alAJ4_9SnCK2piwjA7s55gJwu8HhknWTiyPu4k5Kah0s5xACu_EtMOtQBunvueaY6MsjDhNYc7k9BHnUuTIW3blMRmgScEnSJapKHZaputkjwJTf5K9xmox3pK5QDD_uW3XvFZ8wx45LcdfWDH9UYZyeG2AeYcKm7rkKaK5RyDuIwwUU4zHSeiShnYhckYcuQt1kGzqTHDMh7c0qKZr_0O2_1BmEunCw8luNdXBO9cz-p2_IDwW-NNiPlql7r061j9JBVP0wFFk-QRpMQX8VqPur0fZfkLNyJhoI9pFBcCby-GjhsFggOuOTyElxBZ13ZOdo2MFA1MwuT66_USZNlAFopwMElmMuVcl6xkl887VavUc-nghuZJa5noQcfRD8Bf8BL8nD3JWeVDTy_XWz8B9hdvYt8VkUXbO4Ti86BrZLsLt74pZvz934M1vp-VvX304BWMQaawgd0fzhQrKu438qyrPEj91gFCmP-MyoisO4xCxow7rz4oqEvnaVwE-hi0cMSX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb6044c25.mp4?token=jlJAg6VwE_a7YZzloLqAfQGPHhDxAhgIw63U8MFc2ywrC9-OqTSSBltdeqyfpODYq_8dmf_ODtchmp5Wt-obTExiu0Y20PodSKmYSxCj4_iXt3-HJRazm3xMt2qJtsuVPuYd_3QhF4r8oee5gPVILq4JUVW2j4udNqU-alAJ4_9SnCK2piwjA7s55gJwu8HhknWTiyPu4k5Kah0s5xACu_EtMOtQBunvueaY6MsjDhNYc7k9BHnUuTIW3blMRmgScEnSJapKHZaputkjwJTf5K9xmox3pK5QDD_uW3XvFZ8wx45LcdfWDH9UYZyeG2AeYcKm7rkKaK5RyDuIwwUU4zHSeiShnYhckYcuQt1kGzqTHDMh7c0qKZr_0O2_1BmEunCw8luNdXBO9cz-p2_IDwW-NNiPlql7r061j9JBVP0wFFk-QRpMQX8VqPur0fZfkLNyJhoI9pFBcCby-GjhsFggOuOTyElxBZ13ZOdo2MFA1MwuT66_USZNlAFopwMElmMuVcl6xkl887VavUc-nghuZJa5noQcfRD8Bf8BL8nD3JWeVDTy_XWz8B9hdvYt8VkUXbO4Ti86BrZLsLt74pZvz934M1vp-VvX304BWMQaawgd0fzhQrKu438qyrPEj91gFCmP-MyoisO4xCxow7rz4oqEvnaVwE-hi0cMSX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره فوت سناتور لیندسی گراهام: امیدوار بودم که او بیشتر به سلامتی خود اهمیت می‌داد.
اما آنچه اتفاق افتاده، در واقع چیزی است که تشخیص آن بسیار دشوار است
من فکر نمی‌کنم در این ماجرا چیز شیطانی وجود داشته باشد. می‌دانم که نظریه‌های توطئه زیادی وجود دارد.
به نظر من، اگر اف‌بی‌آی در حال بررسی علت فوت او باشد، وقت خود را تلف می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18039" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اندیمشک و دزفول رو ززززززدن @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/18038" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ: فکر نمی‌کنم به حضور نظامی در عراق نیاز داشته باشیم
ایران باری بر دوش عراق است زیرا قلدر کشورهای خاورمیانه است.
شرکت‌های نفتی در سطوح بی‌سابقه‌ای وارد عراق خواهند شد
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/18037" target="_blank">📅 19:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18036">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ : قدرت نظامی ایران فقط یه بخش خیلی کوچیک از چیزی شده که چهار ماه پیش بود پس عراق دیگه مشکل ایران رو نخواهد داشت @WarRoom</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/18036" target="_blank">📅 19:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18035">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ba06220b.mp4?token=ZYpnY-I9u3wfqOT_s0-xd4HQUD4b-d3z4yV2Xcs4YBS57U2Yc0kLBraQpG11m3I3DeV3b3yrbNbd8M6Q3bvEsJjLOxjyglUkV6c_6AKgQ7Bp5pZJoVmUSTTVYepUsv_PlE911iMfY6caW4QYyBLpSyziC3goaBWkHWa7BQLucdaGaguen2VpG0vbuNLJvhiyJI2GdLC5UBZbqnJP1ynigP2LQuGXUG3Bk7QFcBSDVVY5vO1ahoPvpH1MNi68Pu0TEkf-2T9Y90hbxDSDkIRDd9EH4m44WtwIyGbup5bQibYNbzdDhjDGt-VMdf1p0grElWaKUmMtr-n_wdA6VM32oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ba06220b.mp4?token=ZYpnY-I9u3wfqOT_s0-xd4HQUD4b-d3z4yV2Xcs4YBS57U2Yc0kLBraQpG11m3I3DeV3b3yrbNbd8M6Q3bvEsJjLOxjyglUkV6c_6AKgQ7Bp5pZJoVmUSTTVYepUsv_PlE911iMfY6caW4QYyBLpSyziC3goaBWkHWa7BQLucdaGaguen2VpG0vbuNLJvhiyJI2GdLC5UBZbqnJP1ynigP2LQuGXUG3Bk7QFcBSDVVY5vO1ahoPvpH1MNi68Pu0TEkf-2T9Y90hbxDSDkIRDd9EH4m44WtwIyGbup5bQibYNbzdDhjDGt-VMdf1p0grElWaKUmMtr-n_wdA6VM32oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : قدرت نظامی ایران فقط یه بخش خیلی کوچیک از چیزی شده که چهار ماه پیش بود
پس عراق دیگه مشکل ایران رو نخواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/18035" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18034">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دونالد ترامپ، در دفتر بیضی شکل با علی الزیدی، نخست وزیر جدید عراق، دیدار کرد. در طول این دیدار، ترامپ به الزیدی گفت: «
او جوان و خوش تیپ است، که این من را خوشحال نمی‌کند
.»
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/18034" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18033">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ایران اعلام کرد که زیرساخت‌های شرکت اسپیس‌اکس (SpaceX) متعلق به ایلان ماسک، هدف نظامی مشروعی محسوب می‌شوند
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/18033" target="_blank">📅 19:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18032">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d88026e9.mp4?token=OWAVMhKuRIXq9PQ0bHWHHbg6pCC66OiuXpb_KTkBgIqhHDuWgW4NRoY_H01ibwkTs9VPaDVsc1qQ0I3q9UpN0bg3Bj6QYoar1Zfh2GrClzBghcPC6fRj7UZUphc-2XA0o1t8wASOZmcNSBmdZmOx99BbTa3UdmNlhrvcchDp_BGnD3GwRB-PT5ySV4WFClroK14eUwaQfzRLFB9TpzIVxIGmpI-iUkeEH5AnR8cbgBUAFMPo9yWCQUP8MYlMPfKUb0GdVgLIf4CHq9UeXeE4zHtVgzxT1gcyxu12f1xffr4woTgsSapEMfc1z6e5tx7iMmkOlrMM1etlaaM_vfjjvy3AkjU0XoGAjhnGRjth09BTdHkA8V4nourVTng0h6kIJC14QmGhuGEXh93GIDcoVGuPpgKLUbAfwK4b4D_q3NOh6zUfnIAt1w_YNtL4aQ_G2mL7pcuqceVV35RUzoUBpxEnDdJQeKR1rFxftS1F4zpxbfVGZ5UaFh5EB4141wCLD_DD_cQr2jeaX8jLSB_EAgnuX9uGB83_cpciEGfv8N9FJRM2bwm1e0vX-2tssZOWyfba_M-RCCE_2unWGdQfe6xVDLLLfhkNJMXCyckdSIniiIL2j9-7QFq-1yAKA_gDShSZ6tEEDNGnGg12gJW84ANe_HwuRldm_EoZKZWyvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d88026e9.mp4?token=OWAVMhKuRIXq9PQ0bHWHHbg6pCC66OiuXpb_KTkBgIqhHDuWgW4NRoY_H01ibwkTs9VPaDVsc1qQ0I3q9UpN0bg3Bj6QYoar1Zfh2GrClzBghcPC6fRj7UZUphc-2XA0o1t8wASOZmcNSBmdZmOx99BbTa3UdmNlhrvcchDp_BGnD3GwRB-PT5ySV4WFClroK14eUwaQfzRLFB9TpzIVxIGmpI-iUkeEH5AnR8cbgBUAFMPo9yWCQUP8MYlMPfKUb0GdVgLIf4CHq9UeXeE4zHtVgzxT1gcyxu12f1xffr4woTgsSapEMfc1z6e5tx7iMmkOlrMM1etlaaM_vfjjvy3AkjU0XoGAjhnGRjth09BTdHkA8V4nourVTng0h6kIJC14QmGhuGEXh93GIDcoVGuPpgKLUbAfwK4b4D_q3NOh6zUfnIAt1w_YNtL4aQ_G2mL7pcuqceVV35RUzoUBpxEnDdJQeKR1rFxftS1F4zpxbfVGZ5UaFh5EB4141wCLD_DD_cQr2jeaX8jLSB_EAgnuX9uGB83_cpciEGfv8N9FJRM2bwm1e0vX-2tssZOWyfba_M-RCCE_2unWGdQfe6xVDLLLfhkNJMXCyckdSIniiIL2j9-7QFq-1yAKA_gDShSZ6tEEDNGnGg12gJW84ANe_HwuRldm_EoZKZWyvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان اردن
@WarRoom</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/18032" target="_blank">📅 19:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18031">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجار های شدیدی در کویت گزارش شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/18031" target="_blank">📅 19:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18030">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آسیب به تأسیسات برق کیش در پی انفجار پرتابه‌ها؛ احتمال خاموشی موقت شرکت آب و برق کیش: در پی انفجار پرتابه‌ها در نزدیکی نیروگاه برق جزیره، برخی تجهیزات فنی آسیب دیده و در حال بررسی است.  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/18030" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18029">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آسیب به تأسیسات برق کیش در پی انفجار پرتابه‌ها؛ احتمال خاموشی موقت
شرکت آب و برق کیش:
در پی انفجار پرتابه‌ها در نزدیکی نیروگاه برق جزیره، برخی تجهیزات فنی آسیب دیده و در حال بررسی است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/18029" target="_blank">📅 19:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18028">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کاخ سفید:  «به ترامپ اعتماد کنید؛ وحشت‌زده نشوید» @WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/18028" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18027">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارسالی : پایگاه چهارم شکاری دزفول شیشه هامون لرزید یه انفجار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18027" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18026">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کاخ سفید:
«به ترامپ اعتماد کنید؛ وحشت‌زده نشوید»
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18026" target="_blank">📅 19:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18025">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اندیمشک و دزفول رو ززززززدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18025" target="_blank">📅 19:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18024">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قشم رو ززززززدن @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18024" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18023">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تحلیل مانوک خدابخشیان در پاسخ به روح‌الله زم(در حضور وی)که باید شنید.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18023" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18022">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کویت : ما در حال حاضر مورد حمله موشکی/پهپادی ایران قرار گرفته‌ایم. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/18022" target="_blank">📅 19:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18021">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کویت : ما در حال حاضر مورد حمله موشکی/پهپادی ایران قرار گرفته‌ایم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/18021" target="_blank">📅 19:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18020">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ در کاخ سفید از نخست‌وزیر عراق استقبال کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18020" target="_blank">📅 18:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18019">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجار پایگاه دریایی بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18019" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18018">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGgZhdOexTyxUEkWQoKP7ATtR_RDxi50wx5XcLdhEnpsaCi5OevZ5W2YR9hadSU9TCR9J3LvSS_EQjG-2xCG6lthLsHTZw_Wu2zWXwly5EkJMmd_XAiC7MoLXhM4EukjDwYZaP6AFd9Q6r-m_bDlbHtiOKvmdhIqm0uYUmSuTsyjdX6NuMAfQuVSJJaVP4teEjxpOpZ3qHvSxMKwZVu0_R2CIEHAaQzBdobKNxvEhaQ_B0EvrZwaoj2Jed0FJfZ_607cLrjqjn4O4hBrFMUkj3kQ-k90F674p4sYm27R22kA8MH864fJstpnAbqHhSvW8e2oAaQnwwFyuQh6TnIF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما یک محاصره کامل خواهیم داشت، اما فقط بر روی کشتی‌هایی که به بنادر ایران می‌آیند و می‌روند، یا هر چیزی که مربوط به محمولهٔ ایرانی است را حمل می‌کنند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18018" target="_blank">📅 18:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18017">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قشم رو ززززززدن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/18017" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18016">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ad064452.mp4?token=bejWCl5HlpTAuHMidSKxUa2qlYF1SJkTzJkkdaD46xXTOq2I_klIHlTIbMSaiiqmwUEpwXqtKXyPk9aAPWvRH0BhpoetSLm1kU8p6FtnnI0ZL_nd6B3CnuQlFyuMiA70wDiN-2PDQaCPYNYogn_r5DHiXX-_-1WhXzGv5xp5mA2WpjKKRx0T5cXAJiBgiPf0JXx7TU9SsLhEEihOd9xTicWgaGrKB04EPoZ3jxGwfpWBos2qaknhGjkXkLRDGDUpqBMvTb0zGCek9cLNJZt5GtJfRl0-Yiurxbv7ZsC3uojqHmAuXOCiKPV_LPrLMp_-dpYQCiaFTDQ6pkhX5NKOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ad064452.mp4?token=bejWCl5HlpTAuHMidSKxUa2qlYF1SJkTzJkkdaD46xXTOq2I_klIHlTIbMSaiiqmwUEpwXqtKXyPk9aAPWvRH0BhpoetSLm1kU8p6FtnnI0ZL_nd6B3CnuQlFyuMiA70wDiN-2PDQaCPYNYogn_r5DHiXX-_-1WhXzGv5xp5mA2WpjKKRx0T5cXAJiBgiPf0JXx7TU9SsLhEEihOd9xTicWgaGrKB04EPoZ3jxGwfpWBos2qaknhGjkXkLRDGDUpqBMvTb0zGCek9cLNJZt5GtJfRl0-Yiurxbv7ZsC3uojqHmAuXOCiKPV_LPrLMp_-dpYQCiaFTDQ6pkhX5NKOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه حکم بازداشت نتانیاهو را صادر کرد به نوشته «ترکیه تودی»، این حکم موقت از سوی دادگاه عالی کیفری یازدهم استانبول و در چارچوب رسیدگی به پرونده مربوط به توقیف ناوگان صمود - که عازم غزه بود - صادر شد. فهرست اتهامات علیه نخست‌وزیر اسرائیل شامل «جنایت علیه بشریت»،…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18016" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18015">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترکیه حکم بازداشت نتانیاهو را صادر کرد
به نوشته «ترکیه تودی»، این حکم موقت از سوی دادگاه عالی کیفری یازدهم استانبول و در چارچوب رسیدگی به پرونده مربوط به توقیف ناوگان صمود - که عازم غزه بود - صادر شد.
فهرست اتهامات علیه نخست‌وزیر اسرائیل شامل «جنایت علیه بشریت»، «نسل‌کشی»، «صدمه عمدی» و «شکنجه» است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18015" target="_blank">📅 18:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18014">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32f130ceb.mp4?token=lIOWo4uadJPslI3GP-QSEYNPkj_8DrGDcjxvxznYxOUq3TeOvKEyBavq3mtw8bzgmmwkVESRsZB40iocLLNjh_4XuhX06ze28Kt4Rol5lfEqb6-Rw8Uj4_KZRFZzVU-VPldpvnO1vNjV7iEsT3mYQJYLh7qhcmv0wMEsybEL9q7hKn4-dwSyFOfD_jWI5lAxl9nQ17DmVdPNjPM43N7WKQMcVNnlyge3azU8SMWBmq3AnBtOt2V81B7uXoO1ApvSYb6liMASG5XzMQGZMFX43C80C0LvhE7foxL5qTdVdIHtXmqc5rLMSbTpdA-0fZBa2bMxoc_Ht8tz0fatNan_c3J5w2vUkqInlyTDAXbRrWIU8PQrSG_6-35sGObKyTrPCZCBmcPEBgn2YNnfcPoLE2imYOPvkMNzKXlSkSStmyJmkAYKk5IlktkyE9P-3sHq3o_YA6EGGB7oACALyog6oZcHM3epap8EUNs4NDskEM8qUJznwnVvd3YoNrL63XLzY0ByoBhvUY3MXQTvHfbpRI7u3xoXTlMcJQ1ySwGoN2XppNXPD3JvNppEhPvAUq29905WYTud4s6bcrLVRISLgPSeqYXwmImxZk0O2djrs3EI6-8gHO6GtO1s1XNt4lgG-RQCVg8qIzLDBKnzRQUgG4QRMulI9D-wv4jkmiTmrzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32f130ceb.mp4?token=lIOWo4uadJPslI3GP-QSEYNPkj_8DrGDcjxvxznYxOUq3TeOvKEyBavq3mtw8bzgmmwkVESRsZB40iocLLNjh_4XuhX06ze28Kt4Rol5lfEqb6-Rw8Uj4_KZRFZzVU-VPldpvnO1vNjV7iEsT3mYQJYLh7qhcmv0wMEsybEL9q7hKn4-dwSyFOfD_jWI5lAxl9nQ17DmVdPNjPM43N7WKQMcVNnlyge3azU8SMWBmq3AnBtOt2V81B7uXoO1ApvSYb6liMASG5XzMQGZMFX43C80C0LvhE7foxL5qTdVdIHtXmqc5rLMSbTpdA-0fZBa2bMxoc_Ht8tz0fatNan_c3J5w2vUkqInlyTDAXbRrWIU8PQrSG_6-35sGObKyTrPCZCBmcPEBgn2YNnfcPoLE2imYOPvkMNzKXlSkSStmyJmkAYKk5IlktkyE9P-3sHq3o_YA6EGGB7oACALyog6oZcHM3epap8EUNs4NDskEM8qUJznwnVvd3YoNrL63XLzY0ByoBhvUY3MXQTvHfbpRI7u3xoXTlMcJQ1ySwGoN2XppNXPD3JvNppEhPvAUq29905WYTud4s6bcrLVRISLgPSeqYXwmImxZk0O2djrs3EI6-8gHO6GtO1s1XNt4lgG-RQCVg8qIzLDBKnzRQUgG4QRMulI9D-wv4jkmiTmrzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ اصل مصاحبه دهه هشتادش رو هم منتشر کرد که براتون با زیر نویس فارسی قرار دادم لذت ببرید
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18014" target="_blank">📅 18:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18013">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/18013" target="_blank">📅 18:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18012">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWQbktwc73kRZrdmnHy1OwSfQq1FgJCEDCtrc2Au1j8SrT1U8lyNtnaB9_p6KWY-LuS_Z4GP6j-KieR-o2lmxasx0ih48ixKAELtRYn5WwnqtnsqdcT-M0c2_lUKTijReIiWL2fXQHqNlvU5W2Amy4MtG4R5N8kpRoZvm7Me9U4As-lo_Q70ftQHiNNcgvt1zUzJ5dwR-ZD4d3WtzQvehR0qI3AAJCU5JfE8YnMTftFj8wWqr6V0oTLhMroiOIoKzHICd8g65J34FVaN_8kA7nnDh__ylW5vbe4cUPrA7qGcr1ulao1ZRnn8l06eHVFMkKL7KYP7-_IT0Q1RJmLoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پستی از کاربری که متنی از مصاحبه او با روزنامه گاردین است را بازنشر کرد.
کاربر : «وای خدای من!
اصلاً نمی‌دانستم ترامپ این را گفته است.
آن هم در سال ۱۹۸۸!
جزیره خارک را تصرف کنید!
»
متن مصاحبه ترامپ با گاردین ۱۹۸۸:
«اگه من بودم در قبال ایران بسیار سخت‌گیر می‌بودم. آن‌ها از نظر روانی ما را شکست داده‌اند و باعث شده‌اند مثل یک مشت احمق به نظر برسیم. اگر حتی یک گلوله به سمت یکی از نیروها یا کشتی‌های ما شلیک می‌شد، یه بلایی  بر سر جزیره خارک می‌آوردم و وارد عمل می‌شدم و آن را تصرف می‌کردم. ایران حتی از پس عراق هم برنمی‌آید، اما ایالات متحده را به بازی گرفته است. حمله به آن‌ها به نفع جهان خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18012" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18011">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اکسیوس: تلاش‌ها برای دور زدن تنگه هرمز ادامه دارد.
@warroom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18011" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18010">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/18010" target="_blank">📅 17:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18009">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adzeDKPPv_OU9p_GOovY_cwcV0ic59p2vL_DdjVQbjlny0WaElhUZLmLkcg74zmIe6t-28px8CB6_zxBNHAiCexyhlO5Ptu_8W8p_YgNnXq_sICsIARRZweqGHreKAr8MrA_WlfDo4otGpPbkShrII7935sRThNjvXJNaM9ePuc0SAa8qAv2Pn6pAGdIBVI8mmf7Oyl-mS74tu4DSj7Ic297gL3zbJSV9HcInxVWkgb4noFic24Vua8DzwbcCbheIsMBXDJbQEu0cnzIEVGYN4bfKdb8hCUiionYk1NfNMCMiGxYcI0vd5wDeLVDuBrccw0xdgBLRNzcab0o8vrF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشهای متعدد از مشاهده ستون دود(احتمالا آتش‌سوزی) خ دماوند.میدان امام حسین تهران
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18009" target="_blank">📅 17:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18008">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اعلام الحربی یمن:
به تمامی شرکت‌های هواپیمایی هشدار می‌دهیم که از پرواز در حریم هوایی عربستان خودداری کنند و هشدارهای ما را جدی بگیرند تا زمانی که تحریم‌ها از فرودگاه بین‌المللی صنعا برداشته شود.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18008" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18007">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2ca3903c.mp4?token=Hso9FR6-1MyOpghWBA_IS_eQkoP-IGfzmF1W_HOfSETsprLWG47VrLTruwitaho9ALcgWxIZc-0_xQBRvI-zuycQV8_AKVUsoP0pz7CWJZVIHL5Uq07t_ntvyY22Q1Ek2OPdpfZYsF3K4XXvW2PX9IiGmXgtP1-ZbkrwGltLTC2Ph9EitPJt8IEtdpoYpeu451VpmjlxkN8PJGlL-RS8HGohK_X4r03JAXhip-qKfkt6W9E-bRUdyQAFpJDVeKk6_wuBD2vmdtvnTPIjPbSL9zt75khlMddCijc2YfoL5ne5kSlhha9hEiI_eeOZMtoH4CUoaboNKqOU7-2HUydn-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2ca3903c.mp4?token=Hso9FR6-1MyOpghWBA_IS_eQkoP-IGfzmF1W_HOfSETsprLWG47VrLTruwitaho9ALcgWxIZc-0_xQBRvI-zuycQV8_AKVUsoP0pz7CWJZVIHL5Uq07t_ntvyY22Q1Ek2OPdpfZYsF3K4XXvW2PX9IiGmXgtP1-ZbkrwGltLTC2Ph9EitPJt8IEtdpoYpeu451VpmjlxkN8PJGlL-RS8HGohK_X4r03JAXhip-qKfkt6W9E-bRUdyQAFpJDVeKk6_wuBD2vmdtvnTPIjPbSL9zt75khlMddCijc2YfoL5ne5kSlhha9hEiI_eeOZMtoH4CUoaboNKqOU7-2HUydn-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : همکنون ملوانان آمریکایی عملیات پرواز را بر روی ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش (سی‌وی‌ان ۷۷) انجام می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18007" target="_blank">📅 17:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18006">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef98fc005e.mp4?token=A0ZhsFhKnC7GOQqFL18P08N9zesnEuQt0lZu6nx2oh8jerrQ0OgmbqzfnlZDlAU1_2y7hnZ9jGKaolzt6IZzWrAj8d1sufeXzKSTs2o7pLTYMx0wfFnO2YQEA1-r6tK3N69heJFA2sNhjIvBIpV0hZ1Mtx4kD7gM-oEtfaFNYukLW7QpXftojXKfBP05dGBDXsDXHRf8CHqk96rSnyl45PB7RJzqFI_kHuCW8FCKY6zRDYq6LbEah9t4kLYxMWzmr4vkoGcOunuiES1PNqwJ8jkluzUgEw8HWGm4OHrPYANeRRvM9SxWqaCxLaLFUBrAOTzRmx5dzGHbfK2tRCWP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef98fc005e.mp4?token=A0ZhsFhKnC7GOQqFL18P08N9zesnEuQt0lZu6nx2oh8jerrQ0OgmbqzfnlZDlAU1_2y7hnZ9jGKaolzt6IZzWrAj8d1sufeXzKSTs2o7pLTYMx0wfFnO2YQEA1-r6tK3N69heJFA2sNhjIvBIpV0hZ1Mtx4kD7gM-oEtfaFNYukLW7QpXftojXKfBP05dGBDXsDXHRf8CHqk96rSnyl45PB7RJzqFI_kHuCW8FCKY6zRDYq6LbEah9t4kLYxMWzmr4vkoGcOunuiES1PNqwJ8jkluzUgEw8HWGm4OHrPYANeRRvM9SxWqaCxLaLFUBrAOTzRmx5dzGHbfK2tRCWP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : فقط یک چیز می‌توانم به شما بگویم. نه، آن را به رهبران ایران می‌گویم: اگر به ما حمله کنید، روی آرامش حساب نکنید. روی تکرار این حمله حساب نکنید. چون تکرار نخواهد شد.
حمله قبلی به اندازه کافی قدرتمند بود. این حمله متفاوت خواهد بود - قدرتمند.
روزهایی که کسی می‌توانست به ما حمله کند و ما دو برابر محکم‌تر حمله نمی‌کردیم، گذشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18006" target="_blank">📅 17:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18005">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2rsdoSZpIU5R7s2kAW0t7lW2FzvWKBqegbS0emlby0tIy1BEoBjyt_IJ4iVpWZSuNcfmdrDzkS4MDw7DjhcPE8OnZWqKB0_YExo_U12k5XTB-eccIAouSh8EUWPfhEgqFHbGpJtKTyCpUZK4WWEMSa8g9DOhHU4XY43QwAzzT3bd21uTWyQpOOKipEbg28dlM1PAsr4cRjA5IrpNsu--PqVc5fweV2Z-qkgSyBU5Pr0J_cJ5GqhhQWw2JItQCcAQY9RReQgc2eqMc-qkEFJ5jvhEDrdGOmeJmzvCXF6PEkJD6NyKpwbB-Pcr3ZmTPrItZTCm1ku5QehwiJhDD5fzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: وقوع آتش‌سوزی در یک کشتی حامل مواد شیمیایی در پی حمله‌ دیشب در نزدیکی سواحل عمان
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18005" target="_blank">📅 16:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18004">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سنای آمریکا امروز (۱۴ ژوئیه ۲۰۲۶ / ۲۳ تیر ۱۴۰۵) قرار است درباره لایحه اختیارات دفاع ملی سال مالی ۲۰۲۷ (NDAA 2027) با بودجه پیشنهادی ۱.۱۵ تریلیون دلار رأی‌گیری کند.  این لایحه بودجه سالانه وزارت دفاع آمریکا است و فقط یک بسته اضطراری «مربوط به جنگ با ایران» نیست، اما شامل ماده‌ای به نام «ماده ۲۲۴» است که همکاری‌های نظامی، فناوری و صنعتی میان دو کشور آمریکا و اسرائیل را در حوزه‌هایی مانند هوش مصنوعی، جنگ سایبری، سامانه‌های خودمختار، تولید مشترک تسلیحات و تبادل داده‌های نظامی گسترش می‌دهد و عملا شریک میکند ، همچنین یک نماینده اجرایی ویژه در پنتاگون برای نظارت بر این همکاری‌ها تعیین میشود.  منتقدان این ماده را گامی به سوی «ادغام بی‌سابقه نظامی» آمریکا و اسرائیل می‌دانند که حتی از همکاری‌های ناتو فراتر است و به سطح دیگری میبرد، در حالی که حامیان آن را تقویت ضروری همکاری دفاعی با اسرائیل در برابر تهدیدات منطقه‌ای توصیف می‌کنند که واجب است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18004" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18003">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نتانیاهو: به رهبران ایران می‌گویم که به فکر حمله به ما نباشید، زیرا پاسخ ما بسیار قوی‌تر از قبل خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18003" target="_blank">📅 16:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18002">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzSujBwnH9vANk16He0V2HGUyWOfZP4USvrBd996vZ_o_XQYQid05hABKggGWorcQGNCCEUoesBfrjdmXhABmyCRxcZUJDWhvv12jd5hql1D5FOGOkwbr7vp0Srmzn2_B9k8hcOSNugw_6k4Wj6LygNUgiIqDLBoQcsTRiOE-rEAWMbLZKS799UIWVYe4DkmdjIXctaVFU0-sAA6yO2avmzdFMlpp_rX7bmzo7RYlGOuEzSc8QyyFkz3_WYMdq2uDICaRLKT_BM87nArjOoYHnLeRpP_n4gLZP4xeiywzvsOiK_dAZLVM62jvCZzG2R8UTNLuRTQRjVSkR8YXJPuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار امروز رادار سمت اسکله باهنر به سمت شهید رجایی بندرعباس زدن کله هاش‌ پریده @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18002" target="_blank">📅 15:56 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
