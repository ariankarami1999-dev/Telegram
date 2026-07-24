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
<img src="https://cdn4.telesco.pe/file/COUeBOHS89lnRK1xf9cHnOL__ll_W_sm3n1t06vwbpUDJr3Mylx_AhC9GzRdIKHozcyjGWUOZShI_wL7wFUNr4wzB1dIjZTmuwLa1Fs1A6hah6wBTLbjkm3gB5WzbNOs52utfIyV1veXQdzvWV8DGuu9ArkPDFqNjxR4k_GOnGaNqiHfN9PA2Bd3xW7BlRhNRHGaNRPQvI0E5mT0z7zmGTOsdCh4bF_LvQ4Ui7l1689Gzyz7Wvjo_BHzG3jL8IT8Mm5tloC5Ts9Rn2Sw_4aeQfHP581eBDsatVFPLiKwR0enivG_IYzYYlz-I0VcRvD_-bqwTdrJAyh7hW0OGIpnLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 933K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 05:23:21</div>
<hr>

<div class="tg-post" id="msg-137120">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
مسئولان آمریکایی:
ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/alonews/137120" target="_blank">📅 03:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خنداب اراک رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/137119" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137118">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کوهدشت لرستان رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/137118" target="_blank">📅 03:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137117">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4I5iUGaJuDg8fTJYZ_afQ7yBOyF4z2wsMn-uhlEDuHeoJXMffRP6weTiMbU37fTv7VPd_VV5Y9JWqktiP9cvfH0SWVKl9hi233lv-xtPZv8EVKYeC5gkI2n80RoiTCaanWgdvYmceOdtffq4Z53qCRBZ1eWqR_yrhwH5jlpa5RIyMfl_lrjniU4FJ0bmCKyGd48PbEOOw7a1FbfenA-Eaddi-Tm0emgJt_ldbo_m-HzFZJTZ3J-asy14Lr2mOlA_gVg-4oe5g1CY-dMpXTdXqzAkyG7htOlG-wctQrS2ce9saAHEuWN8CF9MUwKOj9wdNBPB30edMaRumVtR0KE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از بمباران امشب اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/137117" target="_blank">📅 03:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137116">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دزفول رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/137116" target="_blank">📅 03:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137115">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خرم آباد رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/137115" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137114">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نیویورک تایمز:
ایران امروز پیشنهاد آتش بسی که نخست وزیر عراق به تهران اورده بود رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/alonews/137114" target="_blank">📅 03:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
چابهار رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/alonews/137112" target="_blank">📅 03:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
قشم رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/137111" target="_blank">📅 02:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c10375a07a.mp4?token=vtd3vU4DZlix0o0SZe0Kjmb4BTYuhzRn1aZwFannZXLlz1XvODr2oUKmPrAa57h2e91OLmjpobo99gZgoYIg8IixRXfbjTXcMK8r6grhS-ZDWebA3qoR1SYeAz_Zc_xDQzxZ8Kc5AsqeQNAyNm4irbY2p7iNyN9Tx0h-mjd59oWkSoH5F_3ALdGqp1-Nn9kjMDHcMgvAn9DQYzXMiUeymOt4uwqZOADa22XHF_9QoN9kggFuUkA6L-dlpF9tamBv4li_KhDe5eK6Gnzj8D5VyQxoB8TnlXCPX3ttZUoCBE8hSsIf7lTizXrvcpEiTVyRms5hs9OeVHZ4D_iICMr2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c10375a07a.mp4?token=vtd3vU4DZlix0o0SZe0Kjmb4BTYuhzRn1aZwFannZXLlz1XvODr2oUKmPrAa57h2e91OLmjpobo99gZgoYIg8IixRXfbjTXcMK8r6grhS-ZDWebA3qoR1SYeAz_Zc_xDQzxZ8Kc5AsqeQNAyNm4irbY2p7iNyN9Tx0h-mjd59oWkSoH5F_3ALdGqp1-Nn9kjMDHcMgvAn9DQYzXMiUeymOt4uwqZOADa22XHF_9QoN9kggFuUkA6L-dlpF9tamBv4li_KhDe5eK6Gnzj8D5VyQxoB8TnlXCPX3ttZUoCBE8hSsIf7lTizXrvcpEiTVyRms5hs9OeVHZ4D_iICMr2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اهواز رو امشب بد زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/137110" target="_blank">📅 02:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBI_gbPEoSW0oD5P0Eg3hu0lxMdZLgFkY66Ji9Uu9gM5RIlK52XvdvfXr0N3XaY_kOoSe5yPsbN6nq4VUsdExthPGr3NJyEH-aqczf-bPt9gf5av2NsALO6cgk76f3vcyp83G2Wz_zYQDBHObXxKFf6pEBWAbZINM3EhwvUdwAgUBGTzXg9Pa3cdRpIZNv7BiFqXKmd6faFqAjxZb8fb_tNu4thxYHqOrbxqMR60Nr9_nu4-aJ-kj29J2LP84uVf5b819U0Oe_luLy2zacpi5EMJxpP6kQ22fKzs7y-HvYS1ORWD_E8cxP0GzPu4-Q_e4rv9TBXhODgMoV7yIHtsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: دور جدید حملات شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/137109" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137108">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g44Iduizal35rbzyoErik4WcTBTIJqOmCtbP3mDACeYd2cpZOHGANTx_0GWi_TUn7RZfUKjGbJCG4oIcRb-JRjhZCnsmL_uUuH6My09eZHJHiRz095Tnj5ACFFua-jIG9KmZxU6Tn4PA0kDLhZ2AZMLlQfbVzBHY8x_SEfPyfFMSpF47DRfwn3e_CYdygxs7GXMiyssLnhFAMHHA_QONkR-jo-cDkClXQhbnFJofpucLZNqWrkBSe2qXMjbKWbamzCraDpn_5jDA-aCCj7fSY2cVFI7evZ2bsKuhkfmK_F5hLXIcrmETMPZYhgZ-ktnv8uT7m94g7BDRG7I9EJZemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات امشب به اهواز با b1 انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/137108" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137107">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بندرعباسم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/137107" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137106">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62de7a19f2.mp4?token=aBLJtHEA-B_HlBKVX-Pd6s_i65ElFuPiEMCPAD2ICH57ReWZ9Ox0BnSmKS6Ru5l2vWIhFcZtX3tSMneJiIcNi_Mp0FxC0Ke9hvr2vhhQBqQSiF8PyoQQ9aXdvZ5PlVPObxCf1Zf5Et8MWAn-TqdtsX_4cqM7qPTp9wIKx1WZpKqUnIuiw5xOHxpwKefVDIxe5Wf5LWM7b6AoMiMVbFsm0HO2P4-W5jgB9VcbVFtGbJ2ScAh8KMRzrD72SbVePrFQTLXHLX9g2Wd1_HYZTWL94sWezFdLKqt87VZJ2el1sUeY5Y8eLirh9shzYpucPLrq_feEtZIethojj-8RLrBCiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62de7a19f2.mp4?token=aBLJtHEA-B_HlBKVX-Pd6s_i65ElFuPiEMCPAD2ICH57ReWZ9Ox0BnSmKS6Ru5l2vWIhFcZtX3tSMneJiIcNi_Mp0FxC0Ke9hvr2vhhQBqQSiF8PyoQQ9aXdvZ5PlVPObxCf1Zf5Et8MWAn-TqdtsX_4cqM7qPTp9wIKx1WZpKqUnIuiw5xOHxpwKefVDIxe5Wf5LWM7b6AoMiMVbFsm0HO2P4-W5jgB9VcbVFtGbJ2ScAh8KMRzrD72SbVePrFQTLXHLX9g2Wd1_HYZTWL94sWezFdLKqt87VZJ2el1sUeY5Y8eLirh9shzYpucPLrq_feEtZIethojj-8RLrBCiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/137106" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137105">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
اهواز زیر آتیش سنگینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/137105" target="_blank">📅 02:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137104">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
اهواز رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/137104" target="_blank">📅 02:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137103">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036ea5904f.mp4?token=Un1h5JlOGr87ENav313pF-DQIJKzSfOEFjG_zWShNi0QupeavNlsI5O6dLNjhSc6gfwwqpyxhiVeAbMGvOuqXwbVt9SnqUQ0QOOOQn6lsy7bHK6-OwVitWCx-8vAnQKFOzdBRf6cnhHCa1-LvZ8fhhASLyvmQphgyZAwU5n9tS_ZZZwBE0lAbq5U45SXy_jJw5MzoUWjaH1VkeT50J3tV-E8cS5EwAVMb_tIy3UMvscMZLOTNOltWjRyVFqFqveyGPEtFkcAnLDuMUp1Ew-35OiyVOzArGInKnNpwA6LT2iZIoKCqVmkYvxmB4JMxzAz2l5xdsyugHRjG_H3SXjcjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036ea5904f.mp4?token=Un1h5JlOGr87ENav313pF-DQIJKzSfOEFjG_zWShNi0QupeavNlsI5O6dLNjhSc6gfwwqpyxhiVeAbMGvOuqXwbVt9SnqUQ0QOOOQn6lsy7bHK6-OwVitWCx-8vAnQKFOzdBRf6cnhHCa1-LvZ8fhhASLyvmQphgyZAwU5n9tS_ZZZwBE0lAbq5U45SXy_jJw5MzoUWjaH1VkeT50J3tV-E8cS5EwAVMb_tIy3UMvscMZLOTNOltWjRyVFqFqveyGPEtFkcAnLDuMUp1Ew-35OiyVOzArGInKnNpwA6LT2iZIoKCqVmkYvxmB4JMxzAz2l5xdsyugHRjG_H3SXjcjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس: الله اکبر جنگنده تو قشم زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/137103" target="_blank">📅 02:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137102">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=eTMRno7VhsSHrTyP9bXbHDT_OnWkkCJq1WUW9RzWTdo4LNA5Dp4YH0EsLikeoUXFCzFhdJq1dsBpL1HvFxZGsBeLLG3KyyNeK1-QMdWrFxI04gNb-WPw26ZmD386n3NmfZLy49CHx29NI31VjE2VXBBGjeOmgKuN6R-DRB81Oj3FpMt5imMCUDhBKLCfGBPWI8xg2gQhhqptvyMb8DOGE2FFT7uroHePzO64kGtpAimiOCfyLxEk7VElOcRxQ32YiNPSwISscQITjtiQ5NnHbYGHVhlsZ4H8nhHjk2bT6gvGzPH0beNGD2E0qK3OidiRaGBxWvBbrjUnSBZzegwB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=eTMRno7VhsSHrTyP9bXbHDT_OnWkkCJq1WUW9RzWTdo4LNA5Dp4YH0EsLikeoUXFCzFhdJq1dsBpL1HvFxZGsBeLLG3KyyNeK1-QMdWrFxI04gNb-WPw26ZmD386n3NmfZLy49CHx29NI31VjE2VXBBGjeOmgKuN6R-DRB81Oj3FpMt5imMCUDhBKLCfGBPWI8xg2gQhhqptvyMb8DOGE2FFT7uroHePzO64kGtpAimiOCfyLxEk7VElOcRxQ32YiNPSwISscQITjtiQ5NnHbYGHVhlsZ4H8nhHjk2bT6gvGzPH0beNGD2E0qK3OidiRaGBxWvBbrjUnSBZzegwB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد اوجی وزیر نفت دولت سابق رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
🔴
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
🔴
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/137102" target="_blank">📅 02:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137101">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ به اکسیوس:
جنگ جدید با ایران می‌تواند از عملیات خشم حماسی که 40 روز طول کشید نیز بزرگ تر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/137101" target="_blank">📅 01:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137100">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgV6Wl9BqTQM3BlkCQSwAYl1rUK3t31GphFMfVsJnfObVT0-hsxTeyZJxREe7jtorsCOnb7E5hU2S93-QpKn-Zp8uYgJPCoz9PTPwGST-NKRK-vdA0qgBqwifDL2Dy3TP1mUVsISxyWipspTR14DgDmJW0Yap3o4EkLucNEhCkCYbNk3sCAv8P5TZj8MSVuKvkrVZPkUej6ZTDXZqRW3CmDX-9kLrf5foZkhYpQDPCBdFV4d8G3YLdk1yJMLxn6VRkneZiK4NgwMoAo_tlTCAzoBPbEeG4swUpJGBaEu74F7j8wVYL_ZCDXwftcjunD1hbvZaEYy08z4xlxa-l9eLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ
:
از این لحظه به بعد، هرگونه خسارتی که به کشتی‌ها، کالاها یا هر چیزی مرتبط با آن‌ها وارد شود، از طریق وجوه متعلق به ایران که در حال حاضر در اختیار ایالات متحده قرار دارد جبران خواهد شد.
ممکن است این خسارت‌ها قابل‌توجه باشند، اما با وجود این، این اقدام عادلانه و درست است و باید انجام شود.
از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/137100" target="_blank">📅 01:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/137099" target="_blank">📅 01:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkZC-0pJsSLdcOIsWcUkp67C-rVxe7-NREddP52CYjeZ8OMdHxM7CfSwq6EcLl__0TUB-sLqfCpSMMeuiYS1Hz2P6Ujqefamzt3tNGVovO_97qjVCGYX3884WFnZibkI3uJsxCnxGurcb2AN2cJ5l5CIo2xC5kO1LSZ-OQTV3zgfaituka8RXRHOUD5mF4oQ5miZHoPnW2iBqDzjquRU9tG5uRAdGPL3LXyUoDAXQkmuk1fg98E8zcHTSgf8VPp_D5SsFtHDDzzyI2urtjnJgrG45woXdbC-Lf_BHtMJ9qilbAytY6ah-RGRWXM6aJIdCeHgg2tFk9q3AoLbP2b6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
بمب‌افکن‌های B_1 در مسیر خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/137098" target="_blank">📅 01:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137097">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
حال حاضر ۸ سوخت‌رسان بر فراز خلیج فارس در حال پرواز هستند. به نظر می‌رسد سبک عملیاتی بزرگتر و متفاوتی در حال انجام است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/137097" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137096">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وال‌استریت ژورنال: تصاویر ماهواره‌ای نشون می‌ده جمهوری اسلامی روند بازسازی تاسیسات آسیب‌دیده در حملات هوایی آمریکا و اسرائیل رو با سرعت آغاز کرده.
🔴
سرعت بازسازی این تاسیسات نگرانی‌هایی رو درباره میزان اثربخشی کارزار هوایی آمریکا و اسرائیل علیه جمهوری اسلامی ایجاد کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/137096" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137095">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خبری منتشر شده در کانالای تلگرامی تحت عنوان تخلیه برخی مناطق در اصفهان کذب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/137095" target="_blank">📅 01:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137094">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🙂
وای خدااای من برید تاریخ سه روز قبل جنگ رو تو این کانال ببینید دقیق درست گفته بود آمریکا میزنه با ساعت! هم قیمت دلار و طلا دقیق پیشبینی کرده بود  چند روز زودتر همیشه پیشبینی میکنه! الانم تاریخ حمله جدید اسرائیلو گفته
‼️
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
💵
@Tahlilgar_Jang
🪙
@Tahlilgar_Jang</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/137094" target="_blank">📅 01:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137093">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یه موشک رفت تو تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/137093" target="_blank">📅 01:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137092">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=oV1jVraStwuogNmN4zJxA701W3Jikv95dgR89Xc5Y7bGbZujJ0l1NpyTY5tHFDly4uplORkpj0qC-EQB1Yv83x50hdcBhuFRnMnXGBBU80PWjGJjLe2vXYpOjMSFuDJvsOShawX8UNdAIKKd55KkbZnBhJggdFK8x42Ri8qIhn6VKFGLRATd501kE4SOOV9elPb59kxFhH6R_uFR3F_uQJpUP1vdbScijPpSC0I-Hq0j3sETbLi2mGXC5EcEkSUb2E9W5W4qgyJYLm35CnSlkvbrDaVRSkpEF_oQ8QPWij8wKjnqcj1hn68GDJRA2YV9B9-JB7wBDcAtZ4A0UEpYmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9df895be3.mp4?token=oV1jVraStwuogNmN4zJxA701W3Jikv95dgR89Xc5Y7bGbZujJ0l1NpyTY5tHFDly4uplORkpj0qC-EQB1Yv83x50hdcBhuFRnMnXGBBU80PWjGJjLe2vXYpOjMSFuDJvsOShawX8UNdAIKKd55KkbZnBhJggdFK8x42Ri8qIhn6VKFGLRATd501kE4SOOV9elPb59kxFhH6R_uFR3F_uQJpUP1vdbScijPpSC0I-Hq0j3sETbLi2mGXC5EcEkSUb2E9W5W4qgyJYLm35CnSlkvbrDaVRSkpEF_oQ8QPWij8wKjnqcj1hn68GDJRA2YV9B9-JB7wBDcAtZ4A0UEpYmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یبار دیگه ببینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/137092" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137091">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137091" target="_blank">📅 01:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137090">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گزارش‌ها از پرواز جنگنده‌های ارتش در برخی نقاط کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137090" target="_blank">📅 01:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137089">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
از اهواز موشک شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/137089" target="_blank">📅 00:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137088">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
قشم رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/137088" target="_blank">📅 00:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137087">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کانال ۱۳ عبری:
نهادهای اطلاعاتی غرب بر این باورند که ممکن است ایران آغازگر اقدام علیه اسرائیل باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/137087" target="_blank">📅 00:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137086">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
تسنیم: دقایل قبل، اصابت ۲ موشک آمریکایی به محدوده روستای مسن قشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/137086" target="_blank">📅 00:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137085">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
نیویورک پست : روز چهارشنبه، یک حمله دیگر از سوی ایران توانست سامانه‌های پدافند هوایی آمریکا را نفوذ کرده و به یک انبار سلاح در نزدیکی همان پایگاهی اصابت کند که سه سرباز آمریکایی در آن در اردن کشته شدند. این حمله منجر به انفجار شد و در نتیجه، یک "ابر قارچ" شکل گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/137085" target="_blank">📅 00:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137084">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ارتش کویت: پدافند هوایی ما در حال مقابله با حملات موشکی و پهپادی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/137084" target="_blank">📅 00:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137083">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3U8vkPfWK1hSUQeI4P11L0NMzB5Zz69ZW_8WB0pe_Yjnfsmr4DUSAquOiO4DuiD2X816smqd9ikaYxGV2YiTd9ga7xBI-rv1nRNUmg0-EjzQfu2FYdLXE-SJI_ilVlF9vdjhFvSSVOCB7khKiTPj300LOW4v9Avn8pofYih7r4GH-B_ZanhDmiJrb9zZIs1m0_RgDjevtVldPF9oYyp_3nrAu1glEI9uIrIZFgbZ-QOGFTiOD3TZhpGxcRJlWjC7F7CheJX98PFkgmF6EPKMe2h7nwbyruYpnkm2Zs1hJa7qnzrhddLfMoRDYmG19l4gJakCpx9vyIFn49Rzh6r1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی به قلعه‌نویی:
به عنوان یه مربی ایرانی کاری کردید که واسه اولین بار تو جام‌جهانی، از هیچ تیمی شکست نخوردیم و این ارزشمند بود؛
🔴
امثال فردوسی پور طبیعیه که شما رو تخریب کنن چون ذاتا خودتحقیر هستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/137083" target="_blank">📅 00:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137082">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxVsQiBRZwY_ojXudvWtmua-jN2eULQtsWnidbnYJbqYhf4Uiovgn0O8Ch709f89C0SsAIY8KBywJPxJPvJyHlsjgTZjtc2g09bcEqPMoVOu578sVNsdXKYYp5qJ8IKR3hseSArjzPxiLKTZCQIOfKZjdm-ryBSADB4MVJN332rweCtzsXzwGJ5i1JoyJiae1NmxN-izHcSkImf6g_W5pIertqIY68zkIcc5jJBXwWhxj6HIFlzXUYhNVMTuAeC4J39p8sN7Ea5pmx7RCdq5yZjxLvdxo9rM2rR-PMj-mOD9MqnglR_OQHSEEejSqMwojp47-9dWxqqlopFRPQSXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تهدید انگلیس توسط ابراهیم عزیزی برای تصرف جزیره دیگو گارسیا
🔴
دوران سایکس–پیکو مدت‌هاست به پایان رسیده است.روزی که دیه‌گو گارسیا را نیز مانند دیگر مستعمرات خود از دست بدهید، چندان دور نیست.
🔴
بریتانیا بهتر است درباره شکنندگی مرزهای خودش تأمل کند و دریابد که توانمندی‌های ایران بسیار فراتر از گزینه‌های نظامی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/137082" target="_blank">📅 23:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137081">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxIxZ7PFzr2FJns9fyJXPfvp6Bhw1A06zihKbFjlNGSCifrxZgWhceHDQEtEuV7WHdpZTJLoK0M0-roRPdaK8aTSCQkE4adV-9XjiyRYlgWm_L3pothoyM7RiCjICkyf5JtTMG_Udx9i01QkULIg2EeFHNFaEWc-wMXy-QtnHw2pdmtTOFyd2TnabFHzIJY6mQCjz4IXcASzGl_ZaLb2XekrsHOVr3NRgb3PdRNKpCrF0thU77H2BKKw0TZTD2npZTe3QapHdWrwyrSO2L24d0GTzkSE0pPqk5PXYzuaSpm5r8rxFd2-wkVKL4D2rWVRJQXWEEPpnLUOKW3HNXsuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعداد زیادی پهپاد رو به سمت روسیه فرستاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/137081" target="_blank">📅 23:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137080">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtvVxgXpivjCnVm_uamuKh2VXLKBG5e0r44DDI1cxs1hqSW4MZJOmgJQWhZ8sPFx1dAy1SR6pCJVkn2ji2wDvx94kxOwl4BH6-xVFzXz_WILelSGvYtM5ICCWDEy8YpyIQcAMlkh8We89nwqQwKd-cjL9gn386SE3n_m3PQYKhBzO4NtHTf8cO3KuLcYKQt6GfZ4HGH_J5ikkqBq-oY7ofF3Z3Z8Q4_TU8VXf4IUmwBLoTBi_gn6Xug5BVNgoJXu_kJr5GugaNZj_qpr0qNuK4vLQWYyyhS2YXPBRR4PHVb9DEFqSY-PPl7LX5udlCjibmHkbFkvyiYf4khpoFHoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا انقدر هواپیمای ترابری داره میفرسته که تو آسمون ترافیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137080" target="_blank">📅 23:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137079">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwrkoSnyiu1FXElh8MBoGxFtVhvX2PKrQmHKm5iDAJzysp5Y-wSyN5L9t1pSqHamBCjb-hQMzLZPXhJI1yFR16jYvxaoEHzB6HpLKt04nOtMKCsf4xem1Vcul6gf1RODBTvclSq0rGeNDFeDfwELaoZLv4sRdnVUV93yKt6zwo-NRQ6rE4cVpgJMyD3EkElW231lwfHzWMmaGfZtGZzx61-krXRxkqXUD7lFHxZH3KSBWTd0LoJYmlgHFq_vG0JGnV1is1VgyH_i4KxyjHRoqirD-tpZ0vNHH1n1AouiCA1jJjnTJWuWwOedeYORRdk3twYcF7yeD85yOz_CEFJEXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت مالک شریعتی نماینده مجلس بر علیه پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/137079" target="_blank">📅 23:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137078">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd81f5131.mp4?token=oO0ZEHWR1zrYW3F-GU7_4gHKcRHOJObzOj7VQDTCUqm6ZOWVtFRwzDIENErkStiaNhXJkBheiS2V6Lu0wxu06EA0VMEPURrIJDiqYZzInSzC7cu16Z84QABctMTOBKz1iJtpJrLZwvEHvo3sswX49yHquW0lWOJdCPU8XPcY4m-jXjsC3EBraG2mk8QxjxGzJXj_ywzmxxZLaW1TpHOzMAl58UX9EXqVraebGY_-tWWW3k4gG5TpbxSCZ6E3HQ6_oUwG7hIsuS_rZUUN2NC8T-E4FmctJUF1jvExwP34z6YRbc_Y5Oo9-USyoJi9Y_Hjb9eq8KX-hBck8ZH8tgS-8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd81f5131.mp4?token=oO0ZEHWR1zrYW3F-GU7_4gHKcRHOJObzOj7VQDTCUqm6ZOWVtFRwzDIENErkStiaNhXJkBheiS2V6Lu0wxu06EA0VMEPURrIJDiqYZzInSzC7cu16Z84QABctMTOBKz1iJtpJrLZwvEHvo3sswX49yHquW0lWOJdCPU8XPcY4m-jXjsC3EBraG2mk8QxjxGzJXj_ywzmxxZLaW1TpHOzMAl58UX9EXqVraebGY_-tWWW3k4gG5TpbxSCZ6E3HQ6_oUwG7hIsuS_rZUUN2NC8T-E4FmctJUF1jvExwP34z6YRbc_Y5Oo9-USyoJi9Y_Hjb9eq8KX-hBck8ZH8tgS-8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قسمتی از ویس دادگاه نوید افکاری: بهش میگن در یه فیلمی دیده شدی! نوید میپرسه خب اون فیلم چیو نشون میده؟ اون فیلم رو به من و شکات هم نشون بدین. میگن LCD خرابه. بودجش تامین نشده!
#نوید_افکاری
🤔
لعنت به جمهوری اسلامی، لعنت به حرام زاده های طرفدار این حکومت قاتل که جوانان زیادی رو با اذان صبح اعدام کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/137078" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137077">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72219f7361.mp4?token=BdiFn4ngCgFjmKWLmk6tO3wAObaR4nemH27DwcthNdbGN6_EHozY2kx0J9u2MhV5Agh65mz77FPydZFDiNaMt_nGc_Tnjxd0tKGs-aWG6LZ4ij0H8qxa9036H6rrsP3u8bsBTciVWJCY8wD0jo5RQcxjkkbaSI7nvF5TBmARCcAe4Hhdb6U43Gsfft9oldzPSgn8uOJ8TjcdSZ90gR5-wuUUNJ62KjhbF1IPUbR-ndxuFn4Nu_9CFeBeBYzhhTpVY-2pNkT7Lb4xHpJx7u09L9KzAZds-Zi0J10ZAJkc3XPkoUgN4Imf7Xw2xU0yFb1A0rgl0NZiPaZi_9OmyzNfXkJsuvD7CjHc328Z3sV2iEGhr4HEfBX3V2KUatujxZ46N9nzvsT4TElkxTKNhmVqlN-YK5hT0v8yAvmeEZQ4gkNcZeAXIaI4wgeupmebCGakbIT4EED2FQ7Oa3Ao4GfuSv08UUB2ObLOkW9g7Nrp1m3VD1qomDx_WjwfeeY_oD-r2RimEuybYe7mMSkx3WbunmwyMYg4Zb3nyrYKfUparO0iyf5BZJKjc52A5GpzoUQ-jCDwJ10xt589GvubLwGDE-lv_DK_R234V0bb1UCb3T7UYELGYShoHcHq8PeUMsxtzEHzGdnjws5FHDkFap2bruXqSsLTeBdc4QvZ_jTCH5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72219f7361.mp4?token=BdiFn4ngCgFjmKWLmk6tO3wAObaR4nemH27DwcthNdbGN6_EHozY2kx0J9u2MhV5Agh65mz77FPydZFDiNaMt_nGc_Tnjxd0tKGs-aWG6LZ4ij0H8qxa9036H6rrsP3u8bsBTciVWJCY8wD0jo5RQcxjkkbaSI7nvF5TBmARCcAe4Hhdb6U43Gsfft9oldzPSgn8uOJ8TjcdSZ90gR5-wuUUNJ62KjhbF1IPUbR-ndxuFn4Nu_9CFeBeBYzhhTpVY-2pNkT7Lb4xHpJx7u09L9KzAZds-Zi0J10ZAJkc3XPkoUgN4Imf7Xw2xU0yFb1A0rgl0NZiPaZi_9OmyzNfXkJsuvD7CjHc328Z3sV2iEGhr4HEfBX3V2KUatujxZ46N9nzvsT4TElkxTKNhmVqlN-YK5hT0v8yAvmeEZQ4gkNcZeAXIaI4wgeupmebCGakbIT4EED2FQ7Oa3Ao4GfuSv08UUB2ObLOkW9g7Nrp1m3VD1qomDx_WjwfeeY_oD-r2RimEuybYe7mMSkx3WbunmwyMYg4Zb3nyrYKfUparO0iyf5BZJKjc52A5GpzoUQ-jCDwJ10xt589GvubLwGDE-lv_DK_R234V0bb1UCb3T7UYELGYShoHcHq8PeUMsxtzEHzGdnjws5FHDkFap2bruXqSsLTeBdc4QvZ_jTCH5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل، مایک هاوکابی: وقتی شما، یا آقای مامدانی، می‌گویید که بنیامین نتانیاهو مرتکب نسل‌کشی شده است، یا اینکه اسرائیل مرتکب نسل‌کشی شده است، این یک اظهار نظر احمقانه است.
🔴
چرا؟ زیرا وقتی کسی مرتکب نسل‌کشی می‌شود، تلاش می‌کند یک ملت کامل را نابود کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137077" target="_blank">📅 23:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137076">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: آمریکا بداند اگر جنگ را آغاز کند، گستره جنگ فرامنطقه‌ای خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/137076" target="_blank">📅 23:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137073">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed11b92b0.mp4?token=VdXGar6lTq08jMmHeMHauj_Ew3N_86WmdsnuNfeLIn_hymgVRJGQilUzZSRm0m35KkAyKV1PnmfaFWSZrArtGaFdW6GgcxXZ5ji_vauI3-MSOHYCg_bY3I8vosmqns2Pm_24EXeNbbLuigMuTPAsf-T7IuFII9BNodf-ebCSTZqKbKhmu061DLPRxqk3fM8OjHXA_C2dkGTxH9CZ-qyuwWzh7XEJEPVL9sthzd8nf_let9zYOXC4QQpMfyQnaZ6NAlEyow-OB4CGSzbquEWZpWvr6HagH6DJCqNhu1ICGPaCMToGgpwXlYVoZhO7V77YOs1CHwRlwwtlWThRHJO5c30-mDhFLFdYXeDbRdwspgKUteTCf4JaBr8H0_eTHaZPAvaTuq61GdbVXtDMThOxEuFP99WL7vApg0xwGLA0WDMZTei1eQVx5Ghtx1t2gKFp6hmVRulMN8FEIWCpbSDmZjyShCpE7ZdPlaBmFkZ-DL4D3zA1j4OkizyY7CnEoa7Yl4d29rDpeIBBsEtzKLolyZQZclG4GHbLN8P-bMkA08E4kQKh8eE3bbijVoc7rWTOKECV8eD3Wy1tEcCowN22wECpwmcxRCvPdc0HH3zjnLo_PtRYCrRdteY2DLlIvlzlADrT074CacTVt3wlYxqkziUOyVqYSGEaW96DXvco_XU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed11b92b0.mp4?token=VdXGar6lTq08jMmHeMHauj_Ew3N_86WmdsnuNfeLIn_hymgVRJGQilUzZSRm0m35KkAyKV1PnmfaFWSZrArtGaFdW6GgcxXZ5ji_vauI3-MSOHYCg_bY3I8vosmqns2Pm_24EXeNbbLuigMuTPAsf-T7IuFII9BNodf-ebCSTZqKbKhmu061DLPRxqk3fM8OjHXA_C2dkGTxH9CZ-qyuwWzh7XEJEPVL9sthzd8nf_let9zYOXC4QQpMfyQnaZ6NAlEyow-OB4CGSzbquEWZpWvr6HagH6DJCqNhu1ICGPaCMToGgpwXlYVoZhO7V77YOs1CHwRlwwtlWThRHJO5c30-mDhFLFdYXeDbRdwspgKUteTCf4JaBr8H0_eTHaZPAvaTuq61GdbVXtDMThOxEuFP99WL7vApg0xwGLA0WDMZTei1eQVx5Ghtx1t2gKFp6hmVRulMN8FEIWCpbSDmZjyShCpE7ZdPlaBmFkZ-DL4D3zA1j4OkizyY7CnEoa7Yl4d29rDpeIBBsEtzKLolyZQZclG4GHbLN8P-bMkA08E4kQKh8eE3bbijVoc7rWTOKECV8eD3Wy1tEcCowN22wECpwmcxRCvPdc0HH3zjnLo_PtRYCrRdteY2DLlIvlzlADrT074CacTVt3wlYxqkziUOyVqYSGEaW96DXvco_XU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون بمباران غزه توسط جنگنده های ارتش اسرائیل
🔴
ارتش قبل از این حملات، اطلاعیه‌های تخلیه را برای مناطق مورد نظر صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/137073" target="_blank">📅 23:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137072">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f877915d27.mp4?token=UJ_kB1Gk2ap6RxH3v18a8Z4QpEN07Y9MkUcW9vDyakkmQLN_VOVDNBiZiiu65zKFmd9gEB6MFc5qmuP7Sdg0XdKiFFFlIMBmdRAoURbCnWyCh3SMPCNSQeBrG8MPCmz7-lW8azWI3wmmgRGLewkjjLxrWOxFaM_lY2e122_5uR1diMHqDFAJrZKAmU7OlQnF2Kx3uCGU2YOO-kgdoaUCnaHQoX2572ZNy-TQPt77hWfJnvNQBQbeTiGOB5OiJZz-pGxwftY0fpbhDuh7cNCdnl9LjXuEG1CPlceftjvWKhSkWIhbzelPNbvRYmn9BLxSltspbcZJ2sVg0ZIgy4pqkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f877915d27.mp4?token=UJ_kB1Gk2ap6RxH3v18a8Z4QpEN07Y9MkUcW9vDyakkmQLN_VOVDNBiZiiu65zKFmd9gEB6MFc5qmuP7Sdg0XdKiFFFlIMBmdRAoURbCnWyCh3SMPCNSQeBrG8MPCmz7-lW8azWI3wmmgRGLewkjjLxrWOxFaM_lY2e122_5uR1diMHqDFAJrZKAmU7OlQnF2Kx3uCGU2YOO-kgdoaUCnaHQoX2572ZNy-TQPt77hWfJnvNQBQbeTiGOB5OiJZz-pGxwftY0fpbhDuh7cNCdnl9LjXuEG1CPlceftjvWKhSkWIhbzelPNbvRYmn9BLxSltspbcZJ2sVg0ZIgy4pqkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی: نامه‌های احضاریه ترامپ و نتانیاهو به کاخ سفید رفته است
🔴
آنجا امضا گرفته و از طریق کانال بین‌المللی به قوه قضاییه برگشته است.
🔴
اگر در دادگاه حاضر نشوند؛ حکم غیابی قصاص برای ترامپ صادر خواهد شد؛ صدور حکم، تنظیمات آنها را به هم خواهد زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/137072" target="_blank">📅 23:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137071">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: ما در قبال ایران خوب عمل کرده‌ایم و اجازه نخواهیم داد که به سلاح هسته‌ای دست یابد.
🔴
ایرانی‌ها مایل به اقدام دیپلماتیک هستند، اما من می‌گویم که هنوز آماده نیستند.
🔴
اگر ایالات متحده علیه ایران اقدامی نکند، هیچ‌کس دیگری دست به اقدامی نخواهد زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/137071" target="_blank">📅 23:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137070">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG7kCFgZF1H6hocQ1nZP8IXn46pPsIng9__miiIQ_7LgFXSiEwB6y2TZ6txRNmYww-qiop_BL05yMnWq460iXqXGkkMUmGKNBn0bA_w-HsPfQ_TRvyyz-XK7nYM6g9ujze8Has-ifzINiujfOsVM4AWfPvZeh-0p3mZGtbTd2W55triiU3hHGnYKIxMYUaTw_UZc2DArItulxro5WA0JTete_avlYvGmjNqwpk5YQAxg2tOB3PWcmNm-z3bM6vGWxXx_bvJ4MMxQ34za_wwOThPscjU7GEFtFu8vqjw5RdCrLsGnOGLfHdPsWJqyyEFMK7g-lfXdgz13IS-WA7IC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت شدید سوخت رسان ها در خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/137070" target="_blank">📅 23:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137069">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELJ1zZIzKns-7sCi0ev0b-nM6F3B0Z39P2yy3O-aev4EISZ6S9VGee0KoXhsCgNgfZZ5l4emNUDmsS6E8sHW4a4Vij-V1GDGoy8-LtgNuedd43__XS8dnDVc_S3R1dXs1KwCqYcBR1KWod8sulqtvcGDtpcW4XJU9tJew916O16-A7tMzjg3Vhk3GX1OOpRT2MmbOzPDwCAwDaAwid3XGLQpWq01voj5X3bvabbgodPCkaEgP_47N_dKTlfdeTubsSl11FaN9mxtk5KaZ3vE_3oA3B3_mJ9IRRSKFSB9Ed4Cq7Lw1AD9VPXtQMloa6sl8FfkzKmimuxY05zyxrRXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنایه عراقچی به مارک روبیو که مدعی شده بود سیاست آمریکا «سر در برابر چشم» است!
🔴
عناصر وابسته به اسرائیل در دولت آمریکا سر خود را در خاک دفن می‌کنند (اشاره به یک ضرب المثل انگلیسی)
🔴
آنها چشم بر واقعیت‌های میدانی بسته‌اند و گویا تنها دغدغه‌شان انتخابات ۲۰۲۸ است.
🔴
تجاوز بی‌خردانه‌ای که این افراد تبلیغ و تشویق می‌کنند، تنها یک نتیجه خواهد داشت: رئیس‌جمهور آمریکا اگر دنبال معامله است، باید بهای سنگین‌تری بپردازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137069" target="_blank">📅 23:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137068">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ارتش کویت اعلام کرده است که سامانه‌های پدافند هوایی در حال حاضر با "حملات موشکی و پهپادی خصمانه" درگیر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/137068" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137067">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی:
آمریکا بداند اگر جنگ را آغاز کند، گستره جنگ فرامنطقه‌ای خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/137067" target="_blank">📅 23:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137066">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9175f919.mp4?token=d6FP062NWW-5v7yql4B3mxkzNucm6sKqtNavCl-014nM4hOJIFf-XUfHXYNFrEXCmG-iJiwUi13GOMkunTBUn6Js_Ygs_DLJ-PzghiW-pKooEUwqOGOXfbQ8R37IqgYFCv3F4u4XNsoer1zV5bbeKJpIwMQAUJWVewg91UGQWtPfjwn_huUYMmGGCL12RZe36jLyz5GjF8PEdr6G-GljC801zedrKEijHV6ceU6DV3f4iWaZO0bRNHjx9i3V8AR0674Q_1d6Io3GarLzACbQB3nWT6jsi0ZM3u4-mVQaWg-4zGjhpYVhsKtmRYrt5_8gwRrtC50wxKLYWwOnRldbijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9175f919.mp4?token=d6FP062NWW-5v7yql4B3mxkzNucm6sKqtNavCl-014nM4hOJIFf-XUfHXYNFrEXCmG-iJiwUi13GOMkunTBUn6Js_Ygs_DLJ-PzghiW-pKooEUwqOGOXfbQ8R37IqgYFCv3F4u4XNsoer1zV5bbeKJpIwMQAUJWVewg91UGQWtPfjwn_huUYMmGGCL12RZe36jLyz5GjF8PEdr6G-GljC801zedrKEijHV6ceU6DV3f4iWaZO0bRNHjx9i3V8AR0674Q_1d6Io3GarLzACbQB3nWT6jsi0ZM3u4-mVQaWg-4zGjhpYVhsKtmRYrt5_8gwRrtC50wxKLYWwOnRldbijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: عراقچی می‌گوید سیاست آن‌ها «چشم در برابر چشم» است.
🔴
سیاست ترامپ «سر در برابر چشم» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/137066" target="_blank">📅 22:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137065">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
کانال 13 عبری: «نهادهای اطلاعاتی غرب بر این باورند که ممکن است ایران آغازگر اقدام علیه اسرائیل باشد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/137065" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137064">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اکونومیست: چین از جنگ اوکراین برای تقویت توان نظامی خود در آستانه درگیری احتمالی بر سر تایوان بهره می‌برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/137064" target="_blank">📅 22:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137063">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بیانیه مشترک عراق و ایران: حل بحران‌های منطقه‌ای تنها از طریق گفتگو، دیپلماسی و مشارکت کشورهای منطقه میسر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/137063" target="_blank">📅 22:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137062">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6183d48d9b.mp4?token=LSAQHpViRlZZdi-pcdklclTRpCyf7V7wAMI0zv7UDChoy5ZyHmNnMcCOBscxlFHMpnVL5GbIg8gI3ywK0JWvOPuSmeWi-qRREUsnP6MTmYbdNq0NZxekq_M7Eo6FWFvJu1MiDtB7d4hPLNsVsizSKWIS0qSNJ8lJTgAFy7dodvZhvsrh6xFjZNp8J7K2N8HmeXFhm6kEx7SoBRjBceyfBbIx3BFdP93QbmIf3v6UlKK2ur2GvQt5-cetbJOQiqbdDvIUoF9N-98sbj5-2WcCRCDI4RpTmfWoXz_jo8lbRRp7ykyBdE4sWEOHn6OXwYcJ1fsLGRESX1bM5OEgeiciOz2luaVLcoome0IobBKyDzh4B-I5jsI5V4Mpj6qNFweOqACM-bgxDs2VRqYCONUSF7Jf2HnF5juHHZWUOJ7pVaUDGRVl6XGx90Oog-Kh9ax_IvP9xAZvAibjvtESzpFQId56CCx6UaSjD-yPubeTvUnFp9xUSGVtxOzzuTaBgiSfIHXbr1PrqmrBBE1wsU7B9DJZnXFNHm693OvloEmVaanFD5XiDFJgnuqD5Uk9fYM1J3kV110-S3DpWKkD8y_X2CItHC5uR8tk9uO9azYiB2Hx3mfbQy3-_fEHy873_EUVjbE8AICbt7yMNLu6jNypyvBI-AelwM5mfr_TpPt_gJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6183d48d9b.mp4?token=LSAQHpViRlZZdi-pcdklclTRpCyf7V7wAMI0zv7UDChoy5ZyHmNnMcCOBscxlFHMpnVL5GbIg8gI3ywK0JWvOPuSmeWi-qRREUsnP6MTmYbdNq0NZxekq_M7Eo6FWFvJu1MiDtB7d4hPLNsVsizSKWIS0qSNJ8lJTgAFy7dodvZhvsrh6xFjZNp8J7K2N8HmeXFhm6kEx7SoBRjBceyfBbIx3BFdP93QbmIf3v6UlKK2ur2GvQt5-cetbJOQiqbdDvIUoF9N-98sbj5-2WcCRCDI4RpTmfWoXz_jo8lbRRp7ykyBdE4sWEOHn6OXwYcJ1fsLGRESX1bM5OEgeiciOz2luaVLcoome0IobBKyDzh4B-I5jsI5V4Mpj6qNFweOqACM-bgxDs2VRqYCONUSF7Jf2HnF5juHHZWUOJ7pVaUDGRVl6XGx90Oog-Kh9ax_IvP9xAZvAibjvtESzpFQId56CCx6UaSjD-yPubeTvUnFp9xUSGVtxOzzuTaBgiSfIHXbr1PrqmrBBE1wsU7B9DJZnXFNHm693OvloEmVaanFD5XiDFJgnuqD5Uk9fYM1J3kV110-S3DpWKkD8y_X2CItHC5uR8tk9uO9azYiB2Hx3mfbQy3-_fEHy873_EUVjbE8AICbt7yMNLu6jNypyvBI-AelwM5mfr_TpPt_gJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ایران ارتشی ندارد
🔴
آن‌ها چیزی جز اینکه بدجنس و باهوش هستند ندارند و هنوز هم مقداری توانایی دارند.
🔴
چهار ماه پیش، به من اعتماد کنید، آن‌ها بسیار، بسیار قوی‌تر بودند. می‌خواهم اخبار غیرجعلی را به شما بدهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/137062" target="_blank">📅 22:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137061">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59931d1cb8.mp4?token=D1KBMLgClJmREdGeAyUm_3k0EM1xTXxkkn1cCAXB_MXjeVvHIUyNJQzaN4EJpqDj91jBCUTaqgxMyo_gBJODPl1tKMw61w0Hm3WArrqbiFdQo52_HseHlFOAAtDg47MUOzaNyFayrOax6JV7Hswg0AG8zQcyarUx9dZyv3AqI9NPDCNlx_DN4_Cge8ZiHoIFi-YI1mY2ji3dGNvlNd7mzkLVf9ivSUQmfcjtb0C_0PKEVO29l89IwAiAa4DTvs-snXmtcUkUBBzFPQ92UnqTwAIP5biAbUBJN_SgkCVRJkavTai1VYUmRV0ZZHOYZxGLi97IyuLeuYiLrE-2swmwhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59931d1cb8.mp4?token=D1KBMLgClJmREdGeAyUm_3k0EM1xTXxkkn1cCAXB_MXjeVvHIUyNJQzaN4EJpqDj91jBCUTaqgxMyo_gBJODPl1tKMw61w0Hm3WArrqbiFdQo52_HseHlFOAAtDg47MUOzaNyFayrOax6JV7Hswg0AG8zQcyarUx9dZyv3AqI9NPDCNlx_DN4_Cge8ZiHoIFi-YI1mY2ji3dGNvlNd7mzkLVf9ivSUQmfcjtb0C_0PKEVO29l89IwAiAa4DTvs-snXmtcUkUBBzFPQ92UnqTwAIP5biAbUBJN_SgkCVRJkavTai1VYUmRV0ZZHOYZxGLi97IyuLeuYiLrE-2swmwhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
جنگِ ایران بهتر از چیزی که کسی انتظار داشت پیش می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/137061" target="_blank">📅 22:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137060">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: ما به لطف ونزوئلا پول زیادی درآوردیم. ما به این پول حق داریم.
🔴
ترامپ درباره تلفات آمریکا:
این ۱۸ نفر در دو جنگ است.
🔴
وزیر انرژی کریس وایت ونزوئلا را اداره می‌کند.
🔴
او بیشتر از هر کس دیگری که تا به حال اداره کرده است، اداره می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/137060" target="_blank">📅 22:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137059">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26191c2b9.mp4?token=hWYQOD3EWxlOxdaGU6ZnW87EYgK02dZS0G8LlvdE4bzgUlISqfS72_eS-H-SOD8fn5Jzpy4NsKSY30ewRlgnvdTz9FfFXirqtYlHIlsbAH3aQGu9xLqZC3EZt9OrrLPby6NJCE94pVOD5F4ChE_8oWpWtv54K8RO9Aw5W3xzZNbO85pWB-prUXamxyq6ibkSob-q1ZznlAwMjE3LUDLfVswi5vJHv5iMizDmFOIO0rxVMCftOWyRHhL-pBdb7UqyFjvIeOtbuXhJbGpcWQDnE4P7vhPC0i8M6JvMwwJq2uS2h-UhPoYXpulBiGD3pTgcu4_WJvlIK0r_-u0E6y19Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26191c2b9.mp4?token=hWYQOD3EWxlOxdaGU6ZnW87EYgK02dZS0G8LlvdE4bzgUlISqfS72_eS-H-SOD8fn5Jzpy4NsKSY30ewRlgnvdTz9FfFXirqtYlHIlsbAH3aQGu9xLqZC3EZt9OrrLPby6NJCE94pVOD5F4ChE_8oWpWtv54K8RO9Aw5W3xzZNbO85pWB-prUXamxyq6ibkSob-q1ZznlAwMjE3LUDLfVswi5vJHv5iMizDmFOIO0rxVMCftOWyRHhL-pBdb7UqyFjvIeOtbuXhJbGpcWQDnE4P7vhPC0i8M6JvMwwJq2uS2h-UhPoYXpulBiGD3pTgcu4_WJvlIK0r_-u0E6y19Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در مقابل جمهوری اسلامی ایران عملکرد بسیار خوبی داریم. عملکرد ما فوق‌العاده است.
🔴
آنها دوست دارند کاری انجام دهند، اما من می‌گویم که آنها هنوز آماده نیستند.
🔴
آنها به همان چیزهایی که الان دارند، نیاز دارند. آنها هنوز آماده نیستند. آنها اهداف شومی دارند.
🔴
ما نمی‌توانیم اجازه دهیم که آنها سلاح هسته‌ای داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/137059" target="_blank">📅 22:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137058">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/058bc5f933.mp4?token=KAqTh1jaS-4egYPT6vWFGOfPaYvudDDnINx_7RB9fc5fXv4ytkCLRx4zO91KqF6J9hywe_yfXcEn4EUMBpAHVXqay-wqLdAEFmeJwWSo4RfN6jE8UaJ2J3NqdGsWof74DPYOd44XxbsxmHrhbgMehkJ984y-3Xvfci5o2kA4Dlk-DUIZJoEJi62HK3o1QIWDOEFAoWzCqQEIzwa6YiUzCxTn5liQU9Hc2FMozJR8SUFKsWm8-puSR6WtjeZ-6-mb92tyy08EKjAZy1F7F9fA_dN8OF1EErVyVPizXIoNGQeeXaw-AdPCdtRMROUOMmjOjYWelqSLY6QEiHHA5om9FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/058bc5f933.mp4?token=KAqTh1jaS-4egYPT6vWFGOfPaYvudDDnINx_7RB9fc5fXv4ytkCLRx4zO91KqF6J9hywe_yfXcEn4EUMBpAHVXqay-wqLdAEFmeJwWSo4RfN6jE8UaJ2J3NqdGsWof74DPYOd44XxbsxmHrhbgMehkJ984y-3Xvfci5o2kA4Dlk-DUIZJoEJi62HK3o1QIWDOEFAoWzCqQEIzwa6YiUzCxTn5liQU9Hc2FMozJR8SUFKsWm8-puSR6WtjeZ-6-mb92tyy08EKjAZy1F7F9fA_dN8OF1EErVyVPizXIoNGQeeXaw-AdPCdtRMROUOMmjOjYWelqSLY6QEiHHA5om9FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر از یک کشور دیگر خوشتان نمی‌آید، بگذارید آن‌ها به ساختن توربین‌های بادی ادامه دهند. این صنعت در حال فروپاشی است.
🔴
ما از چیزهایی استفاده خواهیم کرد که کارآمد هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/137058" target="_blank">📅 22:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137057">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba15abfb56.mp4?token=CpCyRXZCobUrzYsGWNv6QRCh8BGnUQTc63g6hNdsJJJpCy5INOVGQTqG9dvZQcedhgNvwtqXYMZr3-4Ul6pTIejxv55nCsjM8XJFGYguGOpe8FR2TxmgYNvpxLlTiRkuJ08J7KqXSm_qxpcL8BazrT0XvNUeTjRQhkdyag2YkjgZctQSdnpNJIULZsFYWLC02dGt21_5UQKuQD7y-PNNjsTgffIM-3yu0Kq62_7zxSlQVyss6NrmwbfRZjSb0YseaozVTESXZt1GnLlL2IORCXLyXLP9OJDhLYD_M8pR4Yp5hsh0WeY6m2ueDc0zoo-1Kx4YQbeZwgDj_95zrCAHnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba15abfb56.mp4?token=CpCyRXZCobUrzYsGWNv6QRCh8BGnUQTc63g6hNdsJJJpCy5INOVGQTqG9dvZQcedhgNvwtqXYMZr3-4Ul6pTIejxv55nCsjM8XJFGYguGOpe8FR2TxmgYNvpxLlTiRkuJ08J7KqXSm_qxpcL8BazrT0XvNUeTjRQhkdyag2YkjgZctQSdnpNJIULZsFYWLC02dGt21_5UQKuQD7y-PNNjsTgffIM-3yu0Kq62_7zxSlQVyss6NrmwbfRZjSb0YseaozVTESXZt1GnLlL2IORCXLyXLP9OJDhLYD_M8pR4Yp5hsh0WeY6m2ueDc0zoo-1Kx4YQbeZwgDj_95zrCAHnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «هیچ‌کس نمی‌توانست مناظره بین دونالد ترامپ و جو بایدنِ خواب‌آلود را تماشا کند، چون باد نمی‌وزید.» (کنایه و شوخی ترامپ با ظاهر و لقب تمسخرآمیز بایدن.)
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/137057" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137056">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-WSlteIm9P0hCyANpliIAV7SoNJZE-ULMMrkx2n66hZJHTsN1UlLvSgl1gxVxRJoAwbRqe3fjHomSZR6WKOt4DZ34LHSWCSQbQVSsEV3sab-EkPdEzomzSBGI5KNtQDYf5Qq1RcDWsn_wWSj2wmSkJDCmJCaeJZwizSRYPenfYPoDCAEN5ot8kp5PgReWTeCqPalWtwezWIFdk_1npXODRBhRk2GbaA8sADxpo8OdVYt6gunEvPDP9rjuevH1e-boykPOATxCRWQ43onh1un848GadbTn6zIhHPL1BxOn1oom6ndHXQznm4xABJSwSxAit9GxjLiWJBouKoYjTzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به ۱۰۲ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/137056" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
گزارش فعالیت جنگنده های نیرو هوایی ارتش بر فراز اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/137055" target="_blank">📅 22:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b623ee9c.mp4?token=ZnQnJNsPFpvf9rs6d8F5RBA1sImBnlQbI9Zgu3Gmwa1aA9pHy7dMedvOQ_7bTR7oSu3aLLeI_zIv3iCf5Lpci32TgnfMksa7W9YgtVtAVddSnb04-u0hnpKT9hEJFPfqRF2UggL7PQQGoJM-kDaVfxQSIfmqw1tAdgqu8K3ziMxtNXvzqFYEEqr-7JlnTyW0L76Y8ePKLUgVkLdnxZXo0xjOqCL1l8P1p3ubKScnGaDDWJC8UO0pNe5__Csy9VS5HuE1zf_FOEdvxPfZOx3bpNrdkUXSKxQrCuk-9rIZ93UbLa1bx3km7A6RPuZUJ3_C2Qglwf5h-pxfsSYOsTEDcmK5zRHEIIlrLhZGoNbUAzHP23NiVzSfI_efWaOzr15ZZx4r2dmP_bGhCQSleWvs1o_IBtXVG0J64ZSABwtgc_JfnN69CeuSYMGo2PTcoiEa_-cdu1mcs8chUn9W1FYAwaB8iOTzgddtiL6bm8m6bab8_KPcIvxlSE808jjk4KzRZ1sT5qdFzBIEuo54v4-Qb-H68emFU97lfDEJfWHQ1WWiK3xcnvcaR5uwK6trSd17LHWW-QP7Sglf6SPDORrM9ujie9UlCAUKcnml3Mp5TCPuyq4plCbC5tvvRIFNOsehuqiBQ7lIThGkti5IeNQ3l741NArA-eF2uO3VFxa9Kj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b623ee9c.mp4?token=ZnQnJNsPFpvf9rs6d8F5RBA1sImBnlQbI9Zgu3Gmwa1aA9pHy7dMedvOQ_7bTR7oSu3aLLeI_zIv3iCf5Lpci32TgnfMksa7W9YgtVtAVddSnb04-u0hnpKT9hEJFPfqRF2UggL7PQQGoJM-kDaVfxQSIfmqw1tAdgqu8K3ziMxtNXvzqFYEEqr-7JlnTyW0L76Y8ePKLUgVkLdnxZXo0xjOqCL1l8P1p3ubKScnGaDDWJC8UO0pNe5__Csy9VS5HuE1zf_FOEdvxPfZOx3bpNrdkUXSKxQrCuk-9rIZ93UbLa1bx3km7A6RPuZUJ3_C2Qglwf5h-pxfsSYOsTEDcmK5zRHEIIlrLhZGoNbUAzHP23NiVzSfI_efWaOzr15ZZx4r2dmP_bGhCQSleWvs1o_IBtXVG0J64ZSABwtgc_JfnN69CeuSYMGo2PTcoiEa_-cdu1mcs8chUn9W1FYAwaB8iOTzgddtiL6bm8m6bab8_KPcIvxlSE808jjk4KzRZ1sT5qdFzBIEuo54v4-Qb-H68emFU97lfDEJfWHQ1WWiK3xcnvcaR5uwK6trSd17LHWW-QP7Sglf6SPDORrM9ujie9UlCAUKcnml3Mp5TCPuyq4plCbC5tvvRIFNOsehuqiBQ7lIThGkti5IeNQ3l741NArA-eF2uO3VFxa9Kj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من می‌خواهم رئیس‌جمهور بعدی باشم.
🔴
من می‌خواهم کاری کنم که کسی بسیار خوب به نظر برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/137054" target="_blank">📅 22:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfdd7c5329.mp4?token=atB3eOc1DU3Ee4XnrqKzikeYqDwjScyH3T5tVcyJqGgYc6W4YlQNEqFbBqRK-3E7IbzxiSWbsBkX3BFe53XNgRblWYZS985jJI0QyBDM6OkVNCOIqkxb6cELb-pDoIIwtpkNSvrXGFOps5__aHArddMC4y5AOzpcqW8PN1IsLVwilguo_aLkVMNW2hdRXawmO_JKEHP6SqkKCqkSiOrV_Punom5NBzUxXs5BBBW-onD2rFcePsUF13L5jg_GBZYyAx4EHOWfPb2XfKZBxswAKKE9HFB68fow36xbme4RSIvslFxHaiojF4l0_WPuaXgPJfDO0R9yi1V5Kd2O9sk0QlD2XnWgom3AfBiZaUvUiTW57VIVUlyuJJQYrPrCF_SqnS9qM6RUh-49xRbtEkRlesop62dEPl2NbRqu42N8y0RggrRd0dHo7ht3bWEylFkUA3hsKq61q0GeZmNNBxdLgQ_7rfM6q7t6NZ9AULWLW8ISFvkTmgdF4tke2RWt96u_9lYKGmIABHdwKyIbrkSV-DuOH126YDD-pzcYJC5YPUUjjokrQim8Lxj09WV7q1xGUjK7R9bp7XMS8-eVHjaYy8accEAv62fGCOMjVXoUkJlN-AemouVN5tQkCoE7rt7a9keoKR19E-89aQMtRCfauJxdjAR4p32k5uuR8CSbTm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfdd7c5329.mp4?token=atB3eOc1DU3Ee4XnrqKzikeYqDwjScyH3T5tVcyJqGgYc6W4YlQNEqFbBqRK-3E7IbzxiSWbsBkX3BFe53XNgRblWYZS985jJI0QyBDM6OkVNCOIqkxb6cELb-pDoIIwtpkNSvrXGFOps5__aHArddMC4y5AOzpcqW8PN1IsLVwilguo_aLkVMNW2hdRXawmO_JKEHP6SqkKCqkSiOrV_Punom5NBzUxXs5BBBW-onD2rFcePsUF13L5jg_GBZYyAx4EHOWfPb2XfKZBxswAKKE9HFB68fow36xbme4RSIvslFxHaiojF4l0_WPuaXgPJfDO0R9yi1V5Kd2O9sk0QlD2XnWgom3AfBiZaUvUiTW57VIVUlyuJJQYrPrCF_SqnS9qM6RUh-49xRbtEkRlesop62dEPl2NbRqu42N8y0RggrRd0dHo7ht3bWEylFkUA3hsKq61q0GeZmNNBxdLgQ_7rfM6q7t6NZ9AULWLW8ISFvkTmgdF4tke2RWt96u_9lYKGmIABHdwKyIbrkSV-DuOH126YDD-pzcYJC5YPUUjjokrQim8Lxj09WV7q1xGUjK7R9bp7XMS8-eVHjaYy8accEAv62fGCOMjVXoUkJlN-AemouVN5tQkCoE7rt7a9keoKR19E-89aQMtRCfauJxdjAR4p32k5uuR8CSbTm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی رئیس جمهور اوکراین:
افرادی در اطراف پوتین هستند که می خواهند جنگ را پایان دهند، شاهد فروپاشی اقتصادی، فروپاشی لجستیکی و غیره هستند، اما به قول خودشان افراد نظامی هستند که خواهان گسترش جنگ، افزایش بسیج هستند.
🔴
آنها می خواهند ما را شکست دهند و آنها خواهان ادامه این جنگ هستند.
🔴
به همین دلیل باید برای گذراندن برنامه زمستان آماده شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/137053" target="_blank">📅 22:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cfd01a28.mp4?token=UPL8srRe0HiBbgFvx_NEg04QQVyuubZ0W7pum8zhfAJJgPvB3sPsEjH8SyRqvle-iyxjKc7ZOQ9mrwSPqpaug9U7GhC1WCiwJ0LdIaCETLqCkenRo0Qy6rMVdHZQrkNpJHg4kVFIwfmoRBs78W1guyqFA0JktejTSuL36cpCGtNUZMNHNaP_dfPuYQAxvDJl7sUnOQIGWxYXUXlxAIAk5XIeDmIYlb-lGGMyjCjNNVHmGWfTPvFoV0-PEwl2v95srVIbvTRYvMTAcjUZaWrh-3MfCS188AHF1vmh6UaQ4TEwEUYr7EWNECc_pOPR3JFf5voT3GSvt2jhqo8R0VUNWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cfd01a28.mp4?token=UPL8srRe0HiBbgFvx_NEg04QQVyuubZ0W7pum8zhfAJJgPvB3sPsEjH8SyRqvle-iyxjKc7ZOQ9mrwSPqpaug9U7GhC1WCiwJ0LdIaCETLqCkenRo0Qy6rMVdHZQrkNpJHg4kVFIwfmoRBs78W1guyqFA0JktejTSuL36cpCGtNUZMNHNaP_dfPuYQAxvDJl7sUnOQIGWxYXUXlxAIAk5XIeDmIYlb-lGGMyjCjNNVHmGWfTPvFoV0-PEwl2v95srVIbvTRYvMTAcjUZaWrh-3MfCS188AHF1vmh6UaQ4TEwEUYr7EWNECc_pOPR3JFf5voT3GSvt2jhqo8R0VUNWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما ۱۰ درصد از اینتل را خریدیم. آن را با قیمت مناسب به دست آوردیم.
ما در آن معامله حدود ۷۲ میلیارد دلار کسب کردیم.
🔴
آیا برای آن معامله اعتباری دریافت می‌کنم؟ خیر، من هیچ اعتباری دریافت نمی‌کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/137052" target="_blank">📅 22:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
عراقچی وارد قرقیزستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/137051" target="_blank">📅 22:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bdeb069b8.mp4?token=VIDx7s0J9euAV1eAbCnhdnlvBZ1AYQOZr9TVg3mMDMBVnpvwlgXIXIpvI1F9MGJkyGhYT3niRYD-JirV33_R3R0fQyR2bPCZIy9RnZOlcK7NS10evpNHnlIzaJt6Y7gItKka4BbpecOuU7lL9wqHECsFdWdvutoLrNX3n6SHNOZPxvJY_NRod92MuOXMwkHxyM7bvYHLWN813FPy4T8vSvQWscGBrxrJrN5NRqk5qm1DBRcmSzDZR1rJHUZm9C92ulRWJnv7J-ECLXVOvy1PS_dKTlfjMae04i7zToPSf3P4H0gMVbcs-CPcACi5DxRsMtVZK-7jWo-vaR5eiqlqEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bdeb069b8.mp4?token=VIDx7s0J9euAV1eAbCnhdnlvBZ1AYQOZr9TVg3mMDMBVnpvwlgXIXIpvI1F9MGJkyGhYT3niRYD-JirV33_R3R0fQyR2bPCZIy9RnZOlcK7NS10evpNHnlIzaJt6Y7gItKka4BbpecOuU7lL9wqHECsFdWdvutoLrNX3n6SHNOZPxvJY_NRod92MuOXMwkHxyM7bvYHLWN813FPy4T8vSvQWscGBrxrJrN5NRqk5qm1DBRcmSzDZR1rJHUZm9C92ulRWJnv7J-ECLXVOvy1PS_dKTlfjMae04i7zToPSf3P4H0gMVbcs-CPcACi5DxRsMtVZK-7jWo-vaR5eiqlqEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هوش مصنوعی بزرگتر از اینترنت است.
🔴
هوش مصنوعی بزرگتر از هر چیزی است که تاکنون کسی دیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/137050" target="_blank">📅 22:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: از زمان ازسرگیری محاصره دریایی ایران در هفته گذشته، مسیر ۱۲ کشتی تجاری را تغییر دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/137049" target="_blank">📅 22:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
العربیه: قیمت نفت همچنان در حال افزایش است و قیمت هر بشکه نفت برنت ۸ درصد افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/137048" target="_blank">📅 22:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137047">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر امور خارجه کوبا به الجزیره:
سناریوی تصرف کوبا ممکن است در ذهن واشنگتن باشد، اما این کار نه آسان است و نه قابل قبول
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/137047" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137045">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpUocJTB7vbsJHXXwlEcz9LW-KGZ2b4PHXVHffIbmnY0o7OXlHRo5x4sv-nj0Axv8L8V27YbKNifZHqP_bIqwPOx2PdWoTRTnvq6PLSw5vC0IdVK5fxwpeTqwQouNkG1LXgeLlKktfIB2QsPvSQbiQWpsrbfmRj19I5IgW-hQ4DDUbKTW_EcNgzcUeYEfI4SAOfUxgRL0iozDMUCtmaCSZfbBj1wKJ6DFmtSnNW_dFwPlES2kwLAvfc_myjq7TIZuy1tySdrq6X-MDSEDRpsFmxvq04HF1iIlfjnDk3UJ7CDTyPouHWyTQ_mu0KuHjnQ2IWVERuY2OxLO6XnQUHdvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toeIRropaMVj-NA9QUVlHxOaxLHnL-d27qrc9YaSxJtx-cdy9dkn0kaqSj7-QNSulyt6vbQ8gy_t0-_cGXBpXkFImdI-nCZKnAeLJns85xXTNAqxlp8OMSbcW9vjlhTL2Eslotj3biH21xpUWd2t9e6uz5Aoz6-tW6cbiJBpwqP9OE82dyPpnk5Oy6NcD6VFEuRwY4veizf-5hPGTJ3WGhvAqGmSlpdmJHz1viIbCLkoZnWBtpSlIXn3XAJpNjc82lpuxq3UoO68TjVRFS90ezrJ_6tpGSL4ZzwYG4O8Ofi-pjxoHWgQyatmTpEW4txissaoIM5pL4v4EslcoY96MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار نخست وزیر عراق با قالیباف
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/137045" target="_blank">📅 22:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137044">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
گزارشات از شنیده شدن صدای انفجار در شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/137044" target="_blank">📅 21:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137042">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqjvXNPw38WQ9tdEY2uvkNB1eORNqqHIczwAGChUCkhI_WH5H7G-cTzAPIe82ltG37c2queNa_0f-NKquvdsFksafseGXkplFG6kAJhn93iYBMnycnsaRkoNz-jVTulD77R2T6SRIMxNhtfb1OdowCdAEpWIQd8C_UygTKInxJj1RQE4zYHo1xCGLsNu_pFCByEoF8XjkmYFa_wCBly6VJtCKZs9Fei5v285z26s7FQWDWr5u2KHADqA0ecBQ60hi0Eg9PcUq1gphj8bS8pmXwdY6BtoB3tVFu4i3QPOBG_Cem_Zhf7wlsNpU2BpnhI1-_Jxl7eR3V2dX_jMD5lJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐲
فیلترشکن تانل شده مولتی لوکیشن
▪️
5 گیگ 35 هزار تومان
▪️
10 گیگ 70 هزار تومان
▪️
15 گیگ 100 هزار تومان
▪️
20 گیگ 140 هزار تومان
▪️
50 گیگ 320 هزار تومان
▪️
100 گیگ 600 هزار تومن
👥
- بدون محدودیت کاربر (999 نفر)
🎮
- پینگ پایین مناسب گیم
🛰
- تمامی سرور ها تانل شده ایمن و پرسرعت
🖥
- مناسب برای تمامی سرویس های تحریم شده (
📱
📱
📱
📱
📱
📱
📱
📱
)
🇹🇷
🇫🇮
🇩🇪
🇸🇪
🇳🇱
✨
خرید و تست با دریافت بونس اولین خرید
🛍</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/137042" target="_blank">📅 21:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137041">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddd8bf81be.mp4?token=ZTzEaLl_xt2fSylFICcNO1RIJkMa3xmovuz6BeYZSPhi0WACnLO9N6LfWxEH-SaFEr0DNPmExVV3WWJAc1H_VR8eCISgnt0HqkZ9h5XVKRgty12BS4VjEmieiHI1cs9Wbh_VSZ9bYzQ-Nv3gISM2wLCCXXl3OpZHfPg1s-EwNTfGyjuEM4FgxyGplrTzk_nRemBMlT-Gz6dCevCUhs7viL9sk8qtiCRGwMlMQQa7lPLaJknGkCJ8bsbiud0WoR0qpbCh_tpiKcrBmMpuJkQACU9jiiPm2lcIGk_HVcd-k_D-wMxFGIJRA04cPcFTO-2qTbBidMpm3-jaYSJZhn2vfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddd8bf81be.mp4?token=ZTzEaLl_xt2fSylFICcNO1RIJkMa3xmovuz6BeYZSPhi0WACnLO9N6LfWxEH-SaFEr0DNPmExVV3WWJAc1H_VR8eCISgnt0HqkZ9h5XVKRgty12BS4VjEmieiHI1cs9Wbh_VSZ9bYzQ-Nv3gISM2wLCCXXl3OpZHfPg1s-EwNTfGyjuEM4FgxyGplrTzk_nRemBMlT-Gz6dCevCUhs7viL9sk8qtiCRGwMlMQQa7lPLaJknGkCJ8bsbiud0WoR0qpbCh_tpiKcrBmMpuJkQACU9jiiPm2lcIGk_HVcd-k_D-wMxFGIJRA04cPcFTO-2qTbBidMpm3-jaYSJZhn2vfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین زلنسکی:
پوتین در حال آماده‌سازی حملات جدید علیه اوکراین است، از دیدگاه ما، در حال آماده‌سازی بسیج اضافی در روسیه است، و در حال آماده‌سازی گسترش جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/137041" target="_blank">📅 21:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137040">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde7f010c8.mp4?token=EmbXgkHZ0Q4y73ar-gx-MdL05XqfEdzU6fVQ9ZGZgrWD_CCEKNng61JbSk4TLd6sqFvAxaswHR1T249XoQqWnp2T6loCVn4zZpZ69mMeDL39ceu_HhPpIX-DbmkoD66YPdEV9_uInJm8Jk4IvlqWSwF6TBdNm1AjAgoJRdljGghmTI9x_GaZGAbjVPBoBQpsLij9XKy8zN0FmgkU-8cyYmralUG8UTmzBgiNoV1VKvLl2eM4fOHDtMcTMY7h4qh6v4y9SqdmSbS7MtfhLii6sMTHXH72SEjMiymFyycs4C7Hi5VJxTicgRDquQSszbSr8PyqGsXis52Y9ll8KpjTdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde7f010c8.mp4?token=EmbXgkHZ0Q4y73ar-gx-MdL05XqfEdzU6fVQ9ZGZgrWD_CCEKNng61JbSk4TLd6sqFvAxaswHR1T249XoQqWnp2T6loCVn4zZpZ69mMeDL39ceu_HhPpIX-DbmkoD66YPdEV9_uInJm8Jk4IvlqWSwF6TBdNm1AjAgoJRdljGghmTI9x_GaZGAbjVPBoBQpsLij9XKy8zN0FmgkU-8cyYmralUG8UTmzBgiNoV1VKvLl2eM4fOHDtMcTMY7h4qh6v4y9SqdmSbS7MtfhLii6sMTHXH72SEjMiymFyycs4C7Hi5VJxTicgRDquQSszbSr8PyqGsXis52Y9ll8KpjTdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقرار یک زیردریایی و یک سامانه موشکی «ذوالفقار» متعلق به بسیج در میدان آزادی برای نمایش به مردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/137040" target="_blank">📅 21:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137039">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GckRoa96tNq7DBCacY9n55GHLWYeWcdcbEzd0l5rT_1TjfMeeA-32k8t8BDEs750G_6xsWx9VLhTncM5HdqerW7aztgUKcShyiE_uCHnP7EGThIxiOIlJqq71idd8MYoN91uGirrVpFnwnnzIL8BI5u2ZIlJ_Vp7q6EKrqGTMwjZUQUd8rV91lG6ZUdwuDOn1-CtpB24rr28c_zeO1gqfufslsPdfUhkHXUNOX_-XpeDR-FrJRODt3qd6bDX-1EhQRV5z0k__eUFqU3r9OBSRkMJ_QsThqZCVi1rRouYwxutLdeMdnZrxgf7n-aMfIsmBIF2soVWXNM_FRFCAqVEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت ۱۰۱ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/137039" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137038">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ایلان ماسک: هوش مصنوعی تا پنج سال دیگر از مجموع هوش انسان فراتر می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/137038" target="_blank">📅 21:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137037">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فرانسه تخلیه سفارت خود در تهران را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/137037" target="_blank">📅 21:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137036">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67665193ec.mp4?token=Z3HCPuOb0lVBqL68HVVrWZob_EurezgizVmJkpB4WciUbRMD8BEghSTy4_Kc94BybFB9MoRlF9JvLY_ogqWHpjzFZswfD1io8Ny6QxfFUZtZerSdk7fzkrDJ_zrWfAjokdGBa1lFK-PmdOzujX98G89J1uij8IKQ65ZXX_e065axJ5IiMAtvr2j7iKKLdAhRXBPbbxNYxa7DOBZaHNoe6C2DvGpkDDqvARSYyh-_tUi2slHcWcsCRO9PIi94bHAdFgZqgl-0UsfYPRJU0DJPI2z_bHxMTLzTxYrrMI9Tkgv--ctRNSEkteAkhAzP5mQ-jpZwJsqdB7vGT4bne0MBooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67665193ec.mp4?token=Z3HCPuOb0lVBqL68HVVrWZob_EurezgizVmJkpB4WciUbRMD8BEghSTy4_Kc94BybFB9MoRlF9JvLY_ogqWHpjzFZswfD1io8Ny6QxfFUZtZerSdk7fzkrDJ_zrWfAjokdGBa1lFK-PmdOzujX98G89J1uij8IKQ65ZXX_e065axJ5IiMAtvr2j7iKKLdAhRXBPbbxNYxa7DOBZaHNoe6C2DvGpkDDqvARSYyh-_tUi2slHcWcsCRO9PIi94bHAdFgZqgl-0UsfYPRJU0DJPI2z_bHxMTLzTxYrrMI9Tkgv--ctRNSEkteAkhAzP5mQ-jpZwJsqdB7vGT4bne0MBooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چرا عربستان سعودی به توافق هسته‌ای غیرنظامی دست پیدا می‌کند، اما ایران این توافق را به دست نمی‌آورد؟
🔴
سخنگوی کاخ سفید: توافق ما با عربستان سعودی، منافع آمریکا را در اولویت قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/137036" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137035">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a0l6cQ3WzUJfY4Hzv2Uk1j1SuYWmxYY-kJOp7w0xgvJQc3ivi8W0AwdgYp2MIvC1PctitwxkxYnsoeEs63E3BZOzh6G-_m5Gpl75y2KVgyVXwcHoNHN58y3qsfa0_u0bTWQpaJw_4xOm9sED1b58CutPDzIQiQlOAxag-EjzEiJ1K43Ru2RAsVh8cjND4dAd7hLsvlDqLffAvAw3tITKWmZ6GCFMtwsJvq0VwgrYf_tMxPK3xg9RCvKiPfnWrFzSaD4Ca4QAID8491d4L__APeFujVg9EN9MFJX2QWOG4IsraH09HHFKjd5wQk2skyPBiis6tmjAM_0XgFwuHXdaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای نظارتی E-3G Sentry متعلق به نیروی هوایی ایالات متحده در آسمان، که نشانه‌ای از دور دیگری از حملات علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/137035" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137034">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
شرکت پالایش و پخش فرآورده‌های نفتی: عرضه سی‌ان‌جی با مشارکت داوطلبانه بیش از هزار جایگاه، از اول مرداد رایگان شد
🔴
این طرح با هدف کاهش مصرف بنزین عملیاتی شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/137034" target="_blank">📅 21:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137033">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی:  تل‌آویو در صورت مشارکت ایران در جنگ، قصد دارد اهدافی را در ایران مورد حمله قرار دهد که تاکنون هدف قرار نگرفته‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/137033" target="_blank">📅 21:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137032">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سی‌ان‌ان: مامور سرویس مخفی که از جی دی ونس محافظت می‌کرد، به افشای اطلاعات مربوط به سفرها و خانواده معاون رئیس جمهور متهم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137032" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137031">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
به گفته برخی منابع  کاردار سفارت آلمان ایران را ترک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137031" target="_blank">📅 21:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137027">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729b02b020.mp4?token=YvWyk9Uxiv2tTyfEcDVmd7jxKyqtFXqkNSc83Ff4Z2-a4qPiU1m2VWlf9FllHjNPNBvHnyuD6cJRE6j9B6es08qZdMgxIEGeOoiF1CT1AiyBGOz9QiQFISbF38Z5dNv0T3-6ljD6xl_-kHsB_itw5PsldDUuBOLsFARVgiWojEGnjjowdk_Vw88c1R4uN56UoBpBACK30fzfJHCvAfp6qSkRz-aP2bR5gMw_46VZtj0FEu7qxaPdhRW9g4nV_9inJJHuYm5OeRDBUYsB8L-Fa_CBe1thfh-1olG5hFji1I_Qpm8GoE3_EAhyA-_IiUwBgAd9w4UzjPS0EKKbg8Du5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729b02b020.mp4?token=YvWyk9Uxiv2tTyfEcDVmd7jxKyqtFXqkNSc83Ff4Z2-a4qPiU1m2VWlf9FllHjNPNBvHnyuD6cJRE6j9B6es08qZdMgxIEGeOoiF1CT1AiyBGOz9QiQFISbF38Z5dNv0T3-6ljD6xl_-kHsB_itw5PsldDUuBOLsFARVgiWojEGnjjowdk_Vw88c1R4uN56UoBpBACK30fzfJHCvAfp6qSkRz-aP2bR5gMw_46VZtj0FEu7qxaPdhRW9g4nV_9inJJHuYm5OeRDBUYsB8L-Fa_CBe1thfh-1olG5hFji1I_Qpm8GoE3_EAhyA-_IiUwBgAd9w4UzjPS0EKKbg8Du5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قبایل عرب سوریه در شمال این کشور، بسیج خود را علیه ائتلاف نیروهای دموکراتیک سوریه (SDF) که تحت رهبری کردها فعالیت می‌کند، اعلام کرده‌اند و در حال استقرار نیروهای خود در نزدیکی شهر حسکه هستند که تحت کنترل SDF قرار دارد.
🔴
این قبایل عرب ادعا می‌کنند که هدفشان رهایی شمال سوریه از سازمان "تروریستی" است و خواستار آن هستند که دولت سوریه کنترل کامل این منطقه را به دست بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/137027" target="_blank">📅 20:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137026">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU2lG87s-IhsC3HtCy7fg-BRa764MjQzwLF3X5dIqJEdfPM9fwldO3nZO4SK053ihU30Wre0SAohdTxSgAQcOQLjVY_TRdB0ruPRJWJ8HqV1neAfe-ekFfSnc3s1m8fHgTx2BsubIHAXk7BeW_GNdi66AVHzHO8oe-JbHA4PX1uPegrSMFrLZU20vzhLerq58MCugFL6lo4fFbG9S6_VrMDwV2EQBkFCnlf3ig4kmU4SD31QUG3SOJ2fOeb0_uEvldZclVCcttybxAWAp4OefGCsc399GR0hIolA31NvbesFrbMKU5ZA3xryNUpDcPrNLGlFrYFKhDypRZLaeAmqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک‌ نفتکش منتسب به ناوگان ایران دقایقی پیش از محاصره آمریکا از آب‌های آزاد وارد دریای عمان شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/137026" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e488927e.mp4?token=nrHs0JFSwtaNBxrbPKMP0waJ__-K3qs_OyzMZOSDELpEntFSeMETviUmujehO5lCTzPhArH5C2psI-FV9yIeHUa4BFD79k1dD5Z7voeau2DuLQ2mMeqNz8mTIzF2f7to_9TIEQ1d8KzC_UK6CBxC2WQ7cUy5qicWA7PSihUaP-wzeZQywsx-UDvB5z-2AfD4Dlh67r_67b3bJW2thOr5RgS_F2rdLSsW6_Wmfh8UlVuw-QYevf_IQ4ewQtqJjAZKEyOo3SyIDvw7M2gEglXZPu4xjU9NQKfahUjVHd-Cw2GWSo0-NmPfD6Hluy8KookZTqyEXIAdhT7uQ1XDGmuwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e488927e.mp4?token=nrHs0JFSwtaNBxrbPKMP0waJ__-K3qs_OyzMZOSDELpEntFSeMETviUmujehO5lCTzPhArH5C2psI-FV9yIeHUa4BFD79k1dD5Z7voeau2DuLQ2mMeqNz8mTIzF2f7to_9TIEQ1d8KzC_UK6CBxC2WQ7cUy5qicWA7PSihUaP-wzeZQywsx-UDvB5z-2AfD4Dlh67r_67b3bJW2thOr5RgS_F2rdLSsW6_Wmfh8UlVuw-QYevf_IQ4ewQtqJjAZKEyOo3SyIDvw7M2gEglXZPu4xjU9NQKfahUjVHd-Cw2GWSo0-NmPfD6Hluy8KookZTqyEXIAdhT7uQ1XDGmuwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرار گسترده زندانیان از زندانی در کلمبیا
🔴
در پی وقوع شورش در زندان «لاورا والنسیا» واقع در شهر «پوپایان» کلمبیا، بیش از ۳۰ زندانی موفق به فرار شدند.
🔴
عملیات گسترده نیروهای امنیتی برای شناسایی و بازداشت زندانیان فراری در شهر پوپایان آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/137025" target="_blank">📅 20:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
به گفته برخی منابع عبری ، اسرائیل هشداری از جانب سرویس های امنیتی غربی مبنی بر حمله قریب الوقوع ایران دریافت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/137024" target="_blank">📅 20:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137023">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
به گفته برخی منابع عبری ، اسرائیل هشداری از جانب سرویس های امنیتی غربی مبنی بر حمله قریب الوقوع ایران دریافت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/137023" target="_blank">📅 20:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری / بریتانیا: نیروهای ما آماده‌اند تا هرگونه حمله‌ای را در پی تهدیدات ایران دفع کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/137022" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQFtPMcIrLkJKhW0-iV5KC4U9R4PQTr5buUv3R-RWnLGRa9TcfTkqb2q_1zUD8g5HxYIcXf-hLMr_n2LWmPrM8M-q5GqRlrsW7RORO0cN6HXusx4cHr9HpMXUwmipsUTLeQKPevZ1hDDVQjW7b9t8mTQLicJwh0Ic7-LyQ0321Esi37BsAkDwmnB8XuszBOt2JF5B-gW6yDKTwTFKvOQIuYKlG9fYg7kDXpaKtVEZ-24L2zPZjPaUelBcgXSVYutsvcl1aNHxSPXIHPbSKh6muhl62vw48Ij6xAmr-cbDk9vmOC2vENr5fw81MMrj_GIJ3XGvSPtqrqnLAA6y2039A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتسب به اصابت در بزرگترین نیروگاه برق کویت در حملات ساعتی پیش ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/137021" target="_blank">📅 20:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137020">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
به گفته برخی منابع  کاردار سفارت آلمان ایران را ترک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/137020" target="_blank">📅 20:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137019">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/ سنای آمریکا پیش‌نویس قطعنامه محدود کردن اختیارات ترامپ در مورد جنگ با ایران را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/137019" target="_blank">📅 20:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137018">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
زلنسکی: آمریکایی‌ها روی ایران متمرکز شده‌اند؛ این موضوع برای ما مشکل محسوب می‌شود
🔴
اوضاع در تهران به آن خوبی که واشنگتن می‌خواهد، نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/137018" target="_blank">📅 20:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137017">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
خبرگزاری فارس: صدای انفجاری از دریا در جزیره لارک در جنوب کشور شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/137017" target="_blank">📅 20:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137016">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزارت دفاع کویت اعلام کرد که گذرگاه مرزی العبدالی، واقع در مرز شرقی کویت و عراق، امروز مورد حملات مکرر پهپادهای ایرانی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/137016" target="_blank">📅 20:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137015">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxFj2i1hj9bN1DKgcd-72BnXNfuAIyCb9uGrjU2d0qtUsJ3ifBS1lfXJu68LC6jGJVAP1fBjGEok8d9TqA-MPOkHSo8ME3qPd-31xQd2Fle3gfb6gw_lOnc3ueLpKnomRKhAymtDwFqxILXqh7eNhpEk4EV8cKP8A_jTfzT8U0-lkLpGSCWkcZw4553-nH_rAr4m42svcmoJ2VxFUZHSXIWLZv2CdzrAHFajEj1oBpBOSdCW2UYp9l2D8jM9aIn9KYfl_IfuJu0dtpgqy8iYgAhozaWVsNngT2iwPhymaqN-BUZYhjhpsd_Cf4HJDs2-kts_4hOH-ZQndhk0x8O_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی : رئیس جمهور آمریکا، با اشتباهات مرگبار خود، از "بازی دیوانگی" به "بازی ناامیدی" روی آورده است.
🔴
حمله‌ای به زائران در شلمچه و تهدید به حمله به زیرساخت‌ها، چیزی جز ناامیدی و ناتوانی نیست.
🔴
پاسخ ایران به حملات زیرساختی، تشدید شده و قاطع خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/137015" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137014">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دبیرکل سازمان ملل پس از سه رقمی شدن قیمت نفت: درگیری‌ها باید متوقف شود، دیپلماسی تنها راه پیش‌رو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/137014" target="_blank">📅 20:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137013">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffeaff223.mp4?token=QGegCbC93EtRO8PRCgIfkUQlex5ZhbhyG4rS1jdsTOlUStuoN5XbMzG0QDGs3GkYqJMrKbuP4MGyBNdmOb9Gzp567YhuU9b4WQFkkpgvEsofFzJPIAPi8gcSzgZ4ru0MFOxz293_eFutuAW8gzIjGtaZxvR8bbpFS_TfB2pbrOEGx2QtahgB3GKZCqjlmjFptVp1ukzgbNORiVKz9ebifTxvQfvZvfBk1XTnSUdoJAqpcINm_cFIIdRYR5oIrT1aY_vfLaXFXH9Iw76XP_Z9udFp1eBx0KpwyQZ3w5kyheQTN9LOCYczUEIixqrHkHD65RAlNm7upln-SJfc9ksNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffeaff223.mp4?token=QGegCbC93EtRO8PRCgIfkUQlex5ZhbhyG4rS1jdsTOlUStuoN5XbMzG0QDGs3GkYqJMrKbuP4MGyBNdmOb9Gzp567YhuU9b4WQFkkpgvEsofFzJPIAPi8gcSzgZ4ru0MFOxz293_eFutuAW8gzIjGtaZxvR8bbpFS_TfB2pbrOEGx2QtahgB3GKZCqjlmjFptVp1ukzgbNORiVKz9ebifTxvQfvZvfBk1XTnSUdoJAqpcINm_cFIIdRYR5oIrT1aY_vfLaXFXH9Iw76XP_Z9udFp1eBx0KpwyQZ3w5kyheQTN9LOCYczUEIixqrHkHD65RAlNm7upln-SJfc9ksNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهبر دموکرات‌های مجلس نمایندگان درباره ترامپ: او بعد از فینال جام جهانی خودش را رسوا کرد.
🔴
او شبیه پیرمردی در باشگاهی بود که هیچ‌کس نمی‌خواست با او باشند و او تنها کسی بود که نمی‌توانست این را بفهمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/137013" target="_blank">📅 20:10 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
