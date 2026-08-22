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
<img src="https://cdn4.telesco.pe/file/FOd6Ks00NBy4K-RoR05pw_-KjXS_qHoaW6tCPfyZZgj79BTPDXI1-92q0mjO3S8fS4D1I2EZNOuCVtKRmvzIihhJ4QfozNN5uD6DfP0myxSE49Tt1TbL7JTs2t7m0hNnLnkrhRSWQ0oi42s_RH6FqZVGKEgTeD1MRC9pR8_GevxBq7T-AlAwtJNIMpDUznSi4AIsPjUTvgQV5-fS469_OW-twZHUwhA-dvAjZYON9alTD3OvdIOeOa83C2k1K3RSoTdttz_pdpfFby5R84z655fOmPIXR_X_TBL7okCsceFBZ4_2PLRNX5dz4xtOc__I6z3c6Mu1_Po2-TSIPpiloA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 06:42:39</div>
<hr>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5JGef6Z48XdeANFbKQMsFecOBGzh6j7ZG9l8a5opHGuoxdamAIhdozJ46Bqx33gueobO8IT1rgZ8IZdQNDfwuiz0ySNibW1PaellmLCubp1DJ12jdpOlt6yNZsDHwi1qcINM9g_hCFx-_yWVGdLLxXNY6majTXXmsy7q28hBgjZgxG3UBn34f-5Nq4kIXq4ZytAhGyAQYdIs2JRi5FS_gUtKK0vHUBBlmM9K3Votiw46Lkf_6qG4EC4L8hbQ3FEuymu5WdhAyGxpLxqt76fX743cjdE_X3fpDrl1zqf8wg3VGAQ4GwwNy2_g75D6rqvP7t-NhetExcVm3gJuxK3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnM_36Rx2khF_f0H3uaQ7UpQbpNYq8UA8AhMviy5zoL1dvxacl8OL4jcwTLrKIt6Lw8BCYtWXNehFFuskM-jwt8zx55xTKVbNzLmnMKPue3a5C17rZmCqxRRtovJhFkFeY3PcHGNN_4sQS2Zl_AFbw1N1dIRbsT3pJEMKoOfKgfQ1rY-ZwXRco7OY7ozQN1cPZrW34je-nekzv-nwxQ9ho2KK_g3Sg4TCzcUSCsLm47Y8ii6i3xVGqqbyNVmpIaX5O8nQNKqhcgWzxa0Ec-EWaEeD86npBSaSYty2lWgJiguHmUAaPFGi28PDfRezWp87xPgqggJ16dypfUcTiZPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGqjGEaKqvdTFhoUceIolmvyLfRbwSGWioPVwEnhMJdcEZXLD7BotRWHuPGUxozSpoZVthqj4276WcGPB_4MWQnbtTV0nPkCFOWvLsly_JkjoSLManwlIphuy6wVudxFry5iOF6B_8-oFA494myhtYnpl7fy9DGbVbpXPZiYj_oaOHbZbJ-EVFGwp6ZJL3aPz8LoDVNwbVD2xZUhDAjyaT24zx1gHtjE9DMrMhf8d4VuX2JIwUIi2Jd3llV7S44iVkr72hQ0ASO9QEOOZNeM4SLEGfueFyBeu1iW45_j44uFPlcHhsVhCM85Yh0eNE3Erb7J-4hNuPKyWwo1ysrEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0ohILSPW2O_SOe1NkBErJEIPThX09VhvtcXHmXbCIBFRzoYpIjdImQ1uTAjvO9VGOg88kDcNbPLnbBPqh-SQ7riC_M4ARMNoK0fuv5gJQx5aQvZV_l1XkN2PdLiO4zpHitRdGMAfGr8LREZK3DwBWODCcSQyyQ2a89QYJ4eubPDvX0XbAyxgGM0A8DNWB135UGxS006tUwSCkH_OtWNiaNxWS4W1tDykwgZPVd-FteeFIE3KfNfo0eXn3hhU5wRq7iVxl6PdsJf3X4C_bJoH4bQr9DAtMB0hGtSZq4nGZq4f2E4TTkVQOwGS7KQiLm-8rIoM2LkEx5D9asQsI8YXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJHtpWwHZyVHW2lU_mwtMNMYpcAet42p9zbh5LNkNfcjgWxC4vuS_54RU8irkW9Oa5Gk9FZ4h5VG3F25VZlzKjD3sp_l1rWoXJ9ky3blOz4bCoA7L8NM6Y-nM5NKU-2Fbo3eRWedEPylIlLj_lgLFewsArzbHKA0vO24smst1YYsFpB5mCjBXS9ClE4lKV3hw_mi79NMAkATsZBPs0UsPYOveq2P7s1d8iM97tuA2anMEW-cuLT63IMWZEBNWes76gnL1xGhlaPzTlsjGHIJYPX0CzZD5tfCqkfXZlT_x8lE00bvHJrwJRMK_14CGx3xmMAAfB2YTpAj-ealFvQoEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVwOmj27ZXolV-KHP8L2D4Pahm8zRA8AB_-G7fikzdtlJ7jhbtBuL0WDe8xxF9RswR2T8tnFWJtpwq4V9gw0yGV5nVDoZyXWDE20mX8jiFYr__iFZTTmctUqMzSajNX6q-Is9lJBXHyUz2Ias9_0N8TAFw4pevRzXDELdoz8xuFJJrS77hH-zV8fz5P_UHwOMBGHMAbrFj3qIiUKL4ZSPQ64mLEVPhA0s5dlfjp5bsSH-_3dmo0OK2faekZvbmUsmxy2vmGRUfY6HJG4rP3CbgnCCVj_47CYxM69BBGiUqCJcr4OvzlWcxy2VYmq-PUiTVV2DjqYUk05tcQLaP-t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXgeorvbzMcJVImjKjaXB4uyk8ECq1GLm0ESAwB7LuzMk3LJXY05dPU-OXiby5kfCsh7j9COMIN8FqpVelK7qo_WOPggrSXcXzxW-UMYJfPPVBKXscU6dnPRf63EyiHT3wu3ifboNGs1k1l21EISablwR3E0E2ZTr6Tm8E8UESl_kxPEL6aMmxkIeNhnGogBP7SRiIfSo22hkQrhW4EYis-3VOmnxnFccAI-4UHbhAqQR4_kSOo9wCIEZuo0R2Phfe1OLhtMqah4Ka1BGe5w156bhwyvAeOdlRorQPjsnh0Sfy1tFMIIMu2KSAPljQSuXLyrxBooJUs6ZtOVbFWf5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUV8tqbpjf6Ou4EqcITPPxoKhXfyNVkUmYpYakIc84YZ71_PiayVL0U5cjsfXsxo_T6oyC6q_1eu08QjJIT61m7MSZ3sDfsK41efZt_UCRonz24JbnixXDOpTP08GxP72_YHxnLeswNfJs9vh-s5IuP0LCsG4O8NdYuUpjfk45zk_2A_AZuGrKcbTRmiHT_AjmUpi8tJpvo7_ia1fRhFRMF4rDcgLK45tHfjW3lZXHpqY2NDlDGe0tPiy4qqr4Lh6G0poiPK7rgOetRCkdR5iRmpm0nCJuvCpLB-OJ-M1yzbOX9SpIdTVA3znQ8aldrrNFyBnXCtzO-PgvaSHW6-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEDCjD4Kupo-S6dTI9EDlV6idagOB1B8cq0VulXNIIe86ZVKLFJYjMz2FXtFpO9D6fG7nZVN2YBpdXDgExWYqaq8WXyBtRjH4LdovqDH9lYVKp-CKuJX-7_9NzrGdWgUx5skiLD5Fftv0RKCiGor7MOuONEHbbcUe5BBk72TyEEpnoIcq07i9kdwEAr0o6TntSFrc3AwXirQQgO7WMu5MHuewvNqyybkPhUdPhzcQQQ_usyX-Vu8wjtovHXQjgkZLktQpBBkZaALI8VZJTaGHrMlyaGE3k-TXVQ0Efd_7YiBd_Mnif_a--UrRCLp-ZPH5obkh0HOFCz6X-KW2tbwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcdF61RsgxMpZ3GbUYWqGRdS3ba-YOuvEI3siEBOjzpUBPWBTbovoJ8H8OAlqXeuye7hL2JRqdWVINqpLzhG7MhE8YflOf-8OB1rpHwlullwPs3hnW3VT-D7VCH7EGZXpAV8rRU68r8p6VTRSKteoC2-0HP6Ya7gvyt5G3zZqSF3mmmBySKLgIT5cXlZWFtb08l3qoy8u8QHEv1jTLASDsGFQdcn06zRNgthoSNYEReEkEIWYhiJI7833YyUnGE8OfH_kAvrOlyK9xhdRPmU7CLOFEvu2cclqKlgtUXMQwuAHDat5ywruqwBilmPouRXKh3QvHOeIGKiDcJlq7pMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljGh5mN-R3-vTA0KuuW_BT7tWAQRwNPi3EaAdffQqOkKvwAzYLwMsThJwZLZp4-GyqzNqKQfftsZT-wnXefjcEvvp4HbOeBH04EF85V7qYNLKtXNgacDPx3XlpWOGmTmDaE9m-kpALEL4IFxcobrHv3gnOi4DGYSZqClWfaP1jrBMtcHw-FO-6FkdwWXrUlJ8_bFT6igsCN6eoogZucOo0e778lxEuPAR5qeMQEbOd9_uZg4tvvy30L2I4PZ_qLEcju5xSeEFsO979MKMkUSiNk4_mxi7a-JEkW48FD4Nxgph93JT4C3jyl7bi7EwaMSfRyfpx9PVDNeKM2ELpH-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAlXwum122IIjgsVqKb9bPea1uSnkODhVOKxtFT5xk0AlnGf-Zy8D6P7Yu75TFAwnvIuwgzoyo2X7uJRc-wlzMWPLYvXMDyz99XzpRQKl7TVnQAXJ47rL6KqwzXp8BfUsYdMYPp_MiBM94WOUzDwI2UtmtmxQ8JRGDcwaplPn4foIU9INBoQ0jHQW2h91k_NazmckaMoP3R6IkY8_m_wqJRqwf9HQooY96T-7IVgMwcj_HpiiXu6rxvlWX7lOabnnmE_t9gKHvpYqZLf1z7HsF8cwibx7TdRDs4YOtWbdMd6x9Qj5hN4gt7ZtfsSfDXcDPDuJXjx0IF7M75VZhPLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5SwFPkD62G1BqX80w0yxGr4Xn6Igf3xU85zMSC-psBCmFCw0e4Nls0zeGRyn6WFEUNl8NBnio75MkQH_4ZYzC85sYTFr5gmtSudASJYk508qk12eD0TQkVhavn79E5t8jK4-x4xOupoF6JS9EqCOUd04cuKPkXkdh3dnDab-7SwR1su2HdoDo-zixP6tmQJ0KH64DKbX_Gkws8VeXdG9COQIca2TV_hh9n7S8bF9xARH7K71dPjXtdua5KGAO3ZuxB_7Dx4x7O-rEMM9kRgUUMo8NTINqD7DqzNC1AcZ0Dgbkp3d4HKnE-EGNSWtxHiFPJj1iS1SLZ0PCPjw8Hn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3sVcriqOuZfabeG_IQiXFMW4mrXXTOCpI3XlWbvclzPJ6zfPgmD286WDijhldMKGsygzfYz09QhfW7BJuvASUOoA_PNcWRjaM9TeZeZtBegxxCRXjMpwhu7_SYYv9An43lXumNiognDZQmYpw5I0oI1I2rwrSPBPzkQxLZheKRUZPGnlxr7UtBW4T3FHq3Lg2DqZ8VHK4qUSNC-wwRV9d-L8HSlEZFI0ISnrUlh5Pq0Gfh0DQZjPsUWIVCuAtl2ti3yRYx7Pu24YUN5Mm6obS_tRyXvwXyFjGpO3YaY5GDE2M5M0hk8dKrFzdHbVZAGn7xGfVwJ9EbZ1hRnZa8qWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pe3nAzlAbKtp4hOwA7vTubgFOpUM1EgjNfrEhlFcCdKKthTxa75kCoCmw_--BX4_jwTAoasT-DOm26Y6PCbdVhOW8-5iFrJcivVAltrxNeqFTSIJ9HaJdTTLjA5jTQNcvt-XreU7uYOFJHQ6NeRMR-6lfOsWRk61H2ufyUtp7-bSpmsVCR1iDyzX8YYbJv0tsBqzCga79OcWUS5AoawKpZZ3bZ27tMfgh4Hic8AV9lE7GEdkHa4UiSIZL_ZajxjNzD-CFcnqJcEukvUTBmtz80KM0WwtIV8bgBgaFypxksUnfLNMj1irp4fhcoyM9qjgUk9QUwQejmKVu0w8voFxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUpty3cyirP5_eudOiGZY2VrN95acIAnT0OJZePaUrWNiLyJxYGf98TmOrezvPj937lZbH5yJl8kRep1V0AOgw7yDa8dMpV5bh8klktcnIh-rMtgnNq2ZvLxZsrm3bzS3Mh2M-Ev1PcmO7shuf0PO8iIu_C7X-lwGASlCgIIyVXxflw6c-cVW9K3vaMK7KyyJh-Gg3tt-EN08cgk2QhSGKwrZaJo5YkPzPU80VfJQw0-tzCfwXKfmi5DM1T3X9zyV84FIh0i5xcUxJweav44Igc2iWQbutAioS3bKs2i9fLUEKWPD18xY_K3ku8sN8pd3yfaOuQiePT4hEfOyoCuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M01HcTEG1jkCQfb2rXS1OD-qluAFAPSJuPHT8v-d5Svv8noLpgTd2VxFidEjta5VXmaFLJSM4QH4mb9wjtQvi6mrsJQraWAmXPvbsXC_e4CzZH-DEkgKp3omJCUnZum1qoyNgI06ePen5jHahSThLz5VFDR9qUzQ0pzz7wIqE73YKQnPduXmUmTHAT8MeJm0EBFbxuF5rbGHlOCupnaHNvTDM7nyXfBIYxEGbsu7x1XuY_d9o6Ykm3hjFP8F1LGIfUl3GMgpzyWUNsLKZDC6Xpn-aGBGxLD2hY8huimAFs178nQMcvyShpIFog9R6-f4ulmy0kRIeHNuEfDyUVl7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHYcV95KAFTuzFXuQcTqwnbuAwWCLplXQP40qg0qhL1c0B3KUC8YvPi_3VHp4Ox0A5u1jE-HCFILKtCvSTZWYVBHVSQI9UgxekmaGgdycfbEN2lzoxkXH48zr0FrSwhp2Qx-JIFq65FNonrFNwsPvR-5sSroIfSVriuMhZAHr7GdUxhDoCCJDUBywACY7ncDqlfh1VNG0uoEF17U-AFdDu1UMe-EoZJYtmiOHP8rUUAjcIWoqWvPmrvF1Azr2oplicsFm6XrVettPj6AgTFgpUAPDOhyh_kheAWC7-CZ5K7Jud1s1_1yWXfqXxBRAxBJ_kgxZ7mm1vGzual5JsBF_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-OUtvntB4-pwiY9XhyG-0otwWfYHl17hkEWewT0Kdh8XdkYKB-F_rDKvs_5IJ5aqnIi5gaQQjJ2OTUNiAa1_vb47IEjAejNnRcpCuOEogtXP8cnNkqP2iHisQfW1_hebgoYIrFzjwMxnRYxbdJMvnucvGsy1EW02cHSpXTs5_o_XAfUo3eEVBJDYaOxhboHhOqSIgo4yQqXM4jLh7lYBKxXpjf6o42JWNylAzRj_CU50K3yATj9cGUBXQPzMHhROMAiz7PWFr1oebusQ1bkVkeK4eO3uxQoSCsif4YT2do_i6kHM6fftfRzTGRBAstAXEkOFtzI__aa0VZutm6H8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrqDPlXy6w6PFO4ekEhnrhMYUcHS2OfWfb5iHHIEaD7XWt4TnTAwrGZ2mPo1piN8-ucQiQ0ljLXeYkUAH4N83P2VNKA5rKe4aHKH9Xg7J3LSmwwV3uyy35Gbc7bbmZoPqVe75bLaSlymD02QOhQ48HBGanR4G78cV7fGyt8-l6XK5GBkT-J6OEMp3bBJqSzjSnel3ZVtUPp63Cm8yloUU7qC1VgnD6R_JXGpnjunBZCmCnjYqJ-Jp_iBuajomoM5uHC_elq6yx2DaHJTYtixbGt2h4Rq_rah3euIUW5c9PTwV0VMtHJRqnirKkt63Frg64IttLvo8sIFsU01yT7ydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsAKNKaqfYRlZASz7EMbeQqqS7ZWrv1Au007Tr8t6Um49d3PTxYwCAr4Jzka90Wbp1XWq2Z5sxhH-WeItjjDU-TeWsV4ySaST8axlzfWGLhfu2dPaSo1WJ0xT6Gvj8EMrCCXwhtTOlJJDDNZJVNcGtZntcyZlmEzb9EWw8c2GZqfbI7LUoXnItZ_k1RyDAC0FBuWuRmbEAjG3bhfY_IdrYX5wBugH8cAY4q6axDpddofFDWmz8gTpER9wGmgaTvih-epZajYOcuN9R1jjiBtj17yL1VFc8CTwS6Fx-LDmpQJ3u34ljY8BoW5irB06zFraKSIeHDKab4M-CVeeJ4SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZbWpmPsYYTlexay2oT77uU6K6fPUz6SG4qYZEzcCPKcB7tQXslI_sBmoMb74-ObSVf-WuwhI3yxpia2reLuiBp0YWxUPvHCu-8RQfVnSYp6Minebd-4brsfx0786VxxGLzMZQYDW1IObqk_nv03kUsgg3JCUg4fEnYOcMeaaOvtl53cXidCJKUwTPRYtSI2vCAMXfoYcgQwxxgoH5FEgnx5aSRxV80L5ESHCuvxnZh6n77ObbmcVRDnoS_rUTiHac_JAJYtCcAVMP1mojMvvFyH62z-Bft-1IKedFPtkTX9Oup524OeTeGJOCy68ODUzIKxQZkj4-kRqJULgmidUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvpyYjrkkv3BIiLsrj8fW7U-9F22POsdyarDX8VbOAv6H_y9xoLD3E1ulyUFkMDUOnB_ndR11Q7BxD4VDERjGWKH_6l2Dm2X5At7_xkeWPasnqB7ZL9CSkepPhyTT-t3PBuAhwwqp-yY8BDz8mb8_qO1UJlktJIVOLtiHhKZDThSJ64T2Vm3QXZURkqiir6R-bpWGbouCmUq2bu-SnzzYpEyE1yqZsUh3dAZ93YRSGwoUCmNJypCVsQQvHYA7HjS6XJCiLVCuHU2ftavOcx8ZKMww9mGFNN-oW7yRV6nL-3MyYE6KF7ewuW5nRKkGojnLahNSOrMjcNMA939I5HSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdmTqe7elVzWUiOHPaglE8GT74txryjmIZ9r-VvPsQmfgyW0EX2SwNz8u5jkh7eZPE2Qj0GZlAZrnsaJ8GElT-n3z-fH_K__nDrF-ojtLBwvHzX0i_vPtEgKWO20nifYbhcDMt5IX1Iyc8gPOBjyW42AuI-tTxuhTp3gFmgFdl41ZqROPWWmS0Pjm04POaSJZkfuQ2ObKNsBQ7exQ2aBFZqOrpJ5cPfl-AljCPi1bmhsGaagX_Z_9MyAmpSDCs4J79NeEdimJQpE49Ybu16-W7Otz4WswpTYPPxpn3J3adCZJkKq_vRWBJXnXlosYdgqUmYZpUVBRT1cdNOMDly6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfkTyFsWxmiRpsnfAzh631Y6M6SE4eeKSaPsErkvg7sMO_2EaC-904PvCRCiFOcHTmzAniYVdBYBFBYFA_pNNwjfZvUGflJNhdC1W9zyTctYBV7168NttXIs3cUyPAlwboYP7EhUjxTf-MlBzfbgsx1mhChbR-CPXwdIdTTCywGEQiGT7Sr8q1P5ctwAgdaH1yvVQ7eKKvDGLKP5Q3O50SbhDWc8cTxlE3F6hauT-Awn19jDWuY7usjZpiLrMPe8E0sP2aEPmUYLSykgXmEm26c92TqmRJ5E1qxta0ac8ZxDxAtqewuogOjXU7a0egKVB8WzrKo_mlu4yVd4JttmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YawKpj0cu2UDDV29Ijk-KGZAUYi7cU7HnjuZOt2LiI2v5Yo0htKYuAPvwI1hNYClnsgD4eWpb0FFHRxKVS5ZGttubZzH-qoBG4PTrwBDhAUZ1jzuIapTTv_78YnzBMF4_RxQK_KcQ4Bigw5zsDA8vLanAz1fi3dZ6zu1VwWBnokVlKFA7dVr7mY7gMh9byvlcQ8d_X3NxqSgpTLzrqfdSEj_iiXhiyKOzIzdsLFsSe605XmqAy0qIJidpfm8fqAOl2h-yEr-G3iO80n5k88cA9H7H5yoS3qW7rtdu1dWJT5vVFYvNfpiqLwe9vNdZY85wHfCYH6jIhj7CFnAajD12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BACgeb0wXi5sshQZGommFS_R2x63rTibEnlzf--MBJNFxnwdWQA7Yij65DInfSFgKnv4WzsCM2PGQK_lUItRSLzeRZXTnHuxx0nH9eND4O2SQWNZ0OiqkoDlr8bkaqrOSBg9gq6tk3XoUpsj9iJnWzfubnod3T9XGcZrpRDjpDAZj6wiWdRFv-EqyJ7jApo_Eo4BrVLMynU7VmXmYhknTxIzglA6l5KgqVjMbMZl8mFgRf4z_K3pCt_NxclGK5DtUpGlGwpqjf4d15I6dK3grG8kh6skZ7eESpwknyIDPQ9EGQMLlG5sV9c9IP9YP6VmPluELxKkYY4XzuxL8KkTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpFbsgb2eD5Aq_6uVaqTCD11URJtHlI_986ZbnPo2iNhttyfLkKppiitgItsJT_PmRXUVAwFVOZ1y6_qsgMs4FmXX9mg_uA-Wr-U4ZH55nGmUUE9xaMZuxKknkhamfdYpUTXk6kPIPEQ0e9GqiElaIchmsiv1LY-55fmhxPYka67yFRbXmMO0WOAFseMmybw1KR1e62Y8e3M-LboJU239PXz8q4OHSvgnuR5Ym8CgI7yHBAOb4Q3PTuEqeXDRUSE2TlkaV9jcGmOO-BJp5oyKHxQYctp4kafU12SaPPlysMCWFo5yHJ7aBuW1i4UXVSimVLu5neYhhjwb2hdwaaG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUQj7n89eaFEt-rSQYkEFb03_3ALZFKAzc87vA4Bw1THZZ0vYbeFC3MhhXJ9ShupJecraUVDTFj6R3nBHU7tyskH4GrolpEUfWoWwUTuFxxDHMRZ7WzdDbKutz_LFKF_ktciqCwXQZuAuXSe8bPBRAdzzLRJvTwq_rB6pjMkJkqUQRPOS_2iDLauxO1kubdXop9bo-3KD6YMmG0iCtJ7bBIvBIkYD2wt0ATaTTsJGM7N40goxQbPv2gt2ATyphvL53IK2TCefkpa6UIWdPlGwzzX5yYfGWHJg9KZnZfWO2dcG52l6LTDFlCdT79af6lnMTsnUhD3jXGNggXna3ip0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnkgUQcqQosqUDQnRxtagSXEUGRLVmJ2zfTAiJW9cp0eySaUx9O14Xb15LaT_sqC8qeGEirFcTyUkZnstlHGuCVfxcaTrlVhXj5ZjIrKasuyDmmDzNRrXk47EqwcjAmLbcytYmySbKb0Q7V_PDUyPpVVWzmujm6pzYett7yNQigNmwwT30xGBCJZlMZJzZHkE1U2NAerFM2YBASJ7QV5EQ7dNptPXvpAKOQhOAR7YZBf7vZeGlLTVl70Wxpzyf64QRSrQe7tZ-6QVS-kg1nnr4jpv4dWDmlHKs4nVOwT3M_s2CrOaEWiIpzageHAtHKQXi-GcxkYX-kVJmsONphdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0-QwXFMEQJriBWyIfP7xe3PZ897KP5AXdvNewTkqn6P4BF5brXyTDVxL_sT34sKUEauTKwXsex77RXLXXE4LclzK79_OeN1du0a5BhSZNeQY1-_NwNoAALPeI8XjPIeHDJ3joYuwDg3MpeL7hnsEXU6OVptdko09binjYOnJgKZfIEw3njDd9b-u5LoP0X8XsT3qobVp2Yu9gAgHa9u2tB4D8bb6HBPY76ACN3CY9EGepLrm0WG9BtLMg14BoPSm67LtodcmTZ3Xr_KG8kSJWrcFfef-mMyibe9bB4FZEz_QQsj0wmzChE-7rNH7B-AXVQLeJaxCYxzCBs2-koiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ0blVJYVxUOLzjVXGYH0s1OAf1V0PpM5ZGNwNxsPPkBkTNtcYUUWCXgv39I3MD5MibPhgTxQqlBCMGFi4jsZ8hNIhGjRKa7pRDQ-CM_TWbLMKYCDlB2yd4g70UhPvk4kxX8FKM8O5yhsB5M0kI6QMu03_4vj2ILbnqRiM-wLL_gUGHMCKRZARnMKgGVbQNkmoIptT6CHBp1kmVwIO4lWkkrvhJdNxmsOjRdb-xslqo8Z-6h4ES18pN1GUW5IeeGhr61HJGFb2Y3VZU6p_oSE5Pmk3LUnsbVgV-6kttCrWatqeINYSmWKne-GstE74ll-xVL94S-1ZdBRzdl6zG-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2UdgjuYHrU0sDWO2MbFaiyIYttNIwJDLfj_aMTTzXkGJ5MfKoez6Oe07Sf-GmTlwTpu0tXtqZDAIKE8lW6C9NHI3PuRcJmGSISC6GiAGhObnguJVVZcaX34xTQCzQGVUxK4WJRMSdnzvd9sF68Hii2Fj4TsgCg6iO8C2tRRTyKvY7t9HMScjeysZ8-RPVjM9hcoTWFf93coNCwlvssP3GZhhh1QTEDLgPgENztYIW_AT5VJ2j6iwGYQ6WEeYLojRBgavKEeg3Kh3JZFapq8MCnQXFHOclH1XXi_0dvxPlSJfHyacU95UoHgnBXFi6oAW4ua9bqLgoY-pPI8ij5rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4C2kwGEZln03SkINdjZOuANm1ZzT5ICF49n4YjVPlXWq5YqgRBD1is-kv_36aPeCjk1uVziZsNYzUsDLHCdN1XYByl5pu1T_kXzmrHeRXM1zeiqjBILCSpsTwXCocK-9TmqBVeXGaSBEZgtF650HLgmUDMACmIMi43trVifNSnp0j68WN-ogWIPG7JA708S6IbsaqeCOKES35bJB9pIUXjb4KDefK4jqUn3Q_VDhBqgwScLXRdWBJRp25TvPUsNNul0c_UbGNxpr1tKlbWglU_t98czI_squYtuhi3pjYuzcQFQa1RjxUlq5cXuhmWY8ByKegRckjyj3h4z-IAvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=Jtwwnds0Q7rNTra7Nl7bwZ4N8sP968dy90Oqw__XBjSMZNjwPpU9iFx604AQDFDW1dk8QSQxUGODBmyS89iaBNCyQnaeAZ2RWlU2bgMKbASxIYZZTVbIfOm-uWbLCJJ07b3VxvKQ0LTCC1c5j-XsTAq2isp337iYdH5-aMCeQtEDaW4LM_V72ndSU2y-aAcS8tgmyvkOhTZ9zuNJxmWHX08KPPlhr74PNCpta_x2AkL7QrLooMpqlAmGjkxYtgvB55G84F_SVEOyVShsyzwwqKjYcRh_M0IOhNidU0B-1bENn9h0OCv7z9JHoeuWDdAaZMaByuxIWQswJHzJEHIEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=Jtwwnds0Q7rNTra7Nl7bwZ4N8sP968dy90Oqw__XBjSMZNjwPpU9iFx604AQDFDW1dk8QSQxUGODBmyS89iaBNCyQnaeAZ2RWlU2bgMKbASxIYZZTVbIfOm-uWbLCJJ07b3VxvKQ0LTCC1c5j-XsTAq2isp337iYdH5-aMCeQtEDaW4LM_V72ndSU2y-aAcS8tgmyvkOhTZ9zuNJxmWHX08KPPlhr74PNCpta_x2AkL7QrLooMpqlAmGjkxYtgvB55G84F_SVEOyVShsyzwwqKjYcRh_M0IOhNidU0B-1bENn9h0OCv7z9JHoeuWDdAaZMaByuxIWQswJHzJEHIEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvnlbVQBxxSY0YeDVaKxy-B5uTAybKcjRS-HDzd3trPFt_Pt_mqrN9_dnRqohLf-MuOwi8vNWAO6BA6e_3P-4nUyL0IV6T4syrhdtB9SvHw3LwHtRm9q3MTObSTyrLHI5DV7Vt6ifuiPIR1ywr7vLPFlN-Vs9LQcHrqk1BG9TWVzceY4-taIc3lj1R0QiTkP0ekbfbjcnyMYlMOqP9XQLeCtKjWF004RiPEJnqpSo7jItaoAIy7gki1B9cVL4voV-DMhfPFXS9lNzygZ5kiVB034X8oQmzHSN5ogO3QS96qLfS2K_N52nmRpwkATFuXA_rVkYMm1Kr_c3ItsbeQNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=cp3U6eSy5tzmjwigzAERODIDfAE9Gnqy6p3BcwA2hhX5DKGsg7dBtNzB5RE1jW-7OTzKQggPGaZkLObmbOJa_Ly-GR2KuK3z6YkmHeo5clSI7DzpdobV3C7ibJyrD07Mh9VJL6sYVnyJAej95vyBvjKOmo8SMwDKD40sZs54jBymL1EFm_eup9UUX4_4XkiTLUmMfjUWw4oLmWhftfmpTy5GQo7ig-aXIxmi5dAeczeHhjCm0w-YKosYJqQRS5G5zKoMqLk1BUs6du1c8N53O9mqI6hPf8ksXVWuWXUwTJffVekV41OGVAbc9ruOcDPZc3JXJTM94DKPEicduPfJGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=cp3U6eSy5tzmjwigzAERODIDfAE9Gnqy6p3BcwA2hhX5DKGsg7dBtNzB5RE1jW-7OTzKQggPGaZkLObmbOJa_Ly-GR2KuK3z6YkmHeo5clSI7DzpdobV3C7ibJyrD07Mh9VJL6sYVnyJAej95vyBvjKOmo8SMwDKD40sZs54jBymL1EFm_eup9UUX4_4XkiTLUmMfjUWw4oLmWhftfmpTy5GQo7ig-aXIxmi5dAeczeHhjCm0w-YKosYJqQRS5G5zKoMqLk1BUs6du1c8N53O9mqI6hPf8ksXVWuWXUwTJffVekV41OGVAbc9ruOcDPZc3JXJTM94DKPEicduPfJGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPF_6KocN-QnbnwUPMmH-UAAZLDEmOY79xBlIkkDMZh1l-OryAdW_43RKdReZd1c1DtTdW25bNra0psTmlHDxX9_chSfACYvzXdO90YVTAye6Lka-kzRGmphV5yNZr7bLkeAWR387EENpCNmW1SlCuc_WojEzhf5p92dqe95qykF6zzqKfGfLQg98F6bEi_Cqn3opBTL2dTE51D7ysyJA7NOhgp0XZqZynBf8OlSKzINWeOW62Oj3faBF4wBbgPYzAp3EgVSCyvT7oLy-p_8knPEfhjyVLMeNCaf9mtwyBhFQrtIvqjcwkpE0W6HBFjZuAi4H2g8oEKvFj-9A6QEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmKhO06ip8h5eNsBhqCBvf9dI4FudMWMq526_gOw4BBy7Ej5at87wzc9vA0x2zCzIWHXON6yVNZcnc862wvuX8kW7lNTC_FtirQ_bcLN6LIkoqSO-iOKMUuDd5L0UCg2awO7N1lAWdkiVOti9yRXWPA-wTgRlyoFVsZ0Md0AVPszqYzf23qSQRaCqCBzXgFYBHdk0qhUAaAMr0elBJxyEiOHH-0OeBFJv7Dg37xBhaO_B7AMvGdu7CbEH5MDCYyVq4jCvP7C18YH32RjhkLge6bq-lfuCSfTJP9-OuL0ZbVw4C-wrKH_qaWQUaUVlqJa6GYyaNrPPsAOK6tmJLfAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=XANDlhyC7rsXdToTU6cGfdMKJ2fGjfmctZR_eWICVFHDz-jONTUphfz5ouQAkDAdyiJLCb4EjrMxwzKZ1eIv9vufd2Tr2ZlJMGY1YjypiKvtHyrn737Q3-pu5qAvQ_vaQxWGAUcSOQ2WuneOQuszu58E0yPV171asnDzcUVZIenw_i59F59yfqN6kU9vDNhmJxb-36OTuOEil-Zsa2QdxYM0Htuecrl3JXh6blqOQIgCtY-3TZTM00HkQ7mrI2Km7Y6KqDxy9CYVPZcKhtGu-MnePRZwXaICbo92Yr8AqRoBFmCXpr-1VOPzlMh6msEIhAt2dgVCBC6msc9YE_hy_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=XANDlhyC7rsXdToTU6cGfdMKJ2fGjfmctZR_eWICVFHDz-jONTUphfz5ouQAkDAdyiJLCb4EjrMxwzKZ1eIv9vufd2Tr2ZlJMGY1YjypiKvtHyrn737Q3-pu5qAvQ_vaQxWGAUcSOQ2WuneOQuszu58E0yPV171asnDzcUVZIenw_i59F59yfqN6kU9vDNhmJxb-36OTuOEil-Zsa2QdxYM0Htuecrl3JXh6blqOQIgCtY-3TZTM00HkQ7mrI2Km7Y6KqDxy9CYVPZcKhtGu-MnePRZwXaICbo92Yr8AqRoBFmCXpr-1VOPzlMh6msEIhAt2dgVCBC6msc9YE_hy_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMKP5LRBktnqSntNKQS489foLyqDb5DeWzqLJ9AQuJ-p7Qhs0p45XWgsk1aHTBiBwgqe5M8np2BnSmUQNiuLuCQOmibmCc4NJT6KSoB_rg_URxfH1fsPz9zg_eT_YPN4Ejx_d9FcpiG4QLXYcMXuTRvU2W3muKPDUgXMochFDQd-sKYmhEszL0_77TCOZKUUD9GhYmlUfwzORbbpQpwPJ_HQ9rxbpkhz93Z5QCcCKhzCRLfnJMajSLN_88z2iwlpIkozk7PaIsQr9mxiIVpdu0wmpxTCiabzCRBhG2PqCSyJ7lo0COsROtfhaR5IHV6BsOWpogWTWJj4r4js0TVCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkghfB3cQPrS_PK46QqAugBKPeI61j0xAXnzcpAC5hNEU7g1bDfu4FlhxoczlTn6aMIqE5KysOtdz8JmruQopI9poNUqUL406mUSkGwMmIlyXbFYydZD4sAzmj2QVejmUvOe2NDmis6mn0rARTSLvinFGZsaOu1_83XEQXB3CY7oAyv6RcxNooMa0FU68XPPbt7mYucopFZeEJUuhoF-mq3ji8_jNVQv8E6vOcL9bqRWsjhqIQrOvvil23o3DEvmWnUsoUsy9xdDrFLSAS_b4T0yCXuUL26GD6WB6MzYGi_PJ6rQAIK-2xwssId89vagF-eYk1mQOQygyRUEknz35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVUwHRbr7x1BLHqdUD1L3BJ6eDSPm5TaeXSpEuNhZRCC4G6w6-2hMxh6U7nBeW3JbhsAB_nz7x08OGcE9PMlmzFlooYsyHO0MW8gWgjuyRML57Jx70mJtsJ2v0N2hK_auiJX9PbFjIY9_tS-gLFiUfJsbXMUgDiLMVsxzUyIXrrjvF5baXnycxDQEXoVGCUjPN412kksCjK92hSq9fUZKZMvrG80CBKBDF62QMjdnUDMLhn8nk0p73uRBwVmjnYCTstCXFVPHma477KXdewrvBzERMjfxvCBaYG57fBbea4UAc9H64gr6OvNgdMH0iePAnv1_eJQ_tYhDvzqa8uYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=OTlIxYk4HoaPhKdjZTybo97FMZYiZDc0k-yUQoFQjy3nfcmIAsqp9QIBU6WQWh2BRnZcMRk4ujp5ADqLuNO-A6u9aaSB4ZeNgoeLaZRGyZ-8ub04JE7acTgZFHSfKVlSSAo8CQLlx26XEnPRF5wgInh2Jdlbbi5N4u124jDFjGMHeObIQKBk9Q_lnast19I4QfN2g4KzO9XsxBc3rAPTfbGDQI78BmY38d-CWrSmtAH1xotGe5egKuNr1cv1gRbY6au4SSBCFgz6Syk5Wn07t8KQh13tBXHi3ssTNjACegVirwqm7fWilvqu8xciPEW0ZdPuVd7L-MmTVKxi6_bcYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=OTlIxYk4HoaPhKdjZTybo97FMZYiZDc0k-yUQoFQjy3nfcmIAsqp9QIBU6WQWh2BRnZcMRk4ujp5ADqLuNO-A6u9aaSB4ZeNgoeLaZRGyZ-8ub04JE7acTgZFHSfKVlSSAo8CQLlx26XEnPRF5wgInh2Jdlbbi5N4u124jDFjGMHeObIQKBk9Q_lnast19I4QfN2g4KzO9XsxBc3rAPTfbGDQI78BmY38d-CWrSmtAH1xotGe5egKuNr1cv1gRbY6au4SSBCFgz6Syk5Wn07t8KQh13tBXHi3ssTNjACegVirwqm7fWilvqu8xciPEW0ZdPuVd7L-MmTVKxi6_bcYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=VgpXveDe82MTdNyfrY_NOmDITxf4grgPIpiBGnjj4Km6k_-F5AJ8BlPP8hAI-YlaFL0mR04V0ndn-EZVF39gTulKBPKl1vbkh8k_dGS3EPLHQUzlxHw0WEYBjoHdrWvokIJxFw9t4UcNDb_jMPy3Jw2FSH-B7ITgQIsIxMGJtU_mqUHKZxMxe6pStT4sEl--9-kNZBCDHiNO1y8_43JQoU8O1Xt6_tBLnIniKPOyWHYDEWMZCQZkTtvOWN5kGD8iHc6wwGKgOCy0Aqdo1OZby6blYFmk8dbHzYv_vF_wNFoDdBkp5wpBBwfdZy8R0M4pNENLNwq5tJsTHZ2XE2TTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=VgpXveDe82MTdNyfrY_NOmDITxf4grgPIpiBGnjj4Km6k_-F5AJ8BlPP8hAI-YlaFL0mR04V0ndn-EZVF39gTulKBPKl1vbkh8k_dGS3EPLHQUzlxHw0WEYBjoHdrWvokIJxFw9t4UcNDb_jMPy3Jw2FSH-B7ITgQIsIxMGJtU_mqUHKZxMxe6pStT4sEl--9-kNZBCDHiNO1y8_43JQoU8O1Xt6_tBLnIniKPOyWHYDEWMZCQZkTtvOWN5kGD8iHc6wwGKgOCy0Aqdo1OZby6blYFmk8dbHzYv_vF_wNFoDdBkp5wpBBwfdZy8R0M4pNENLNwq5tJsTHZ2XE2TTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLyuMPrbNU2Om9RCwRePIxvBgZ_nBgO0vY6vCVEi1jt_1DYAqifWXwxkgUi8Q3XVXv6T_gy1639E4ayXVjnauvp1XD6Z0MCKS9-FcZRqyfrDBDtLuO6UBxQfwpBgTWv-t7qwW_j5KiDwuNUMGybG3wDxCIZ6e3zGIAN1SYzHFBEDigufW6HNkCqaBPxjtxE19hl1zcsH2eF9BBBu9Sx--pkiSCeH3WRv06RvtDePKB_3g4sMdPAnmUXKMSDs3Uglu-U4w0GyVNGPXVsLYmGhw4ODPtlJUQZj-ecEd2jFy6UqPntw27BogtULCDNh9jA7UuRP7HMyxYIOhdkaC8xZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqKMihdepCOLf9fgbyf-aRb08p_kcrbFn4AUgaXz5BbydBL6Opn5Ll7tpamo6_QgyCx-bFgNOolFElex1nRHcPew_fH5oQiruuwIZBlc7Eew16OiY26GnFw9ib3T2zlFzpBtClAfZ-46dcwfoqVpPMYpTUyKkorQ2hX-8rtuuZOIokekgeG8SV9vJoaWukB-Q_5NCz-k7D7J6NIJnP0ju8pNtXOgitvlWwFl7DASqB_quUOqYfJA3R6F2NRwNQrkikRBWMzIyetqNTSK77BJQr1jc2kGqaTpa8JypkQBGOdlDHZ7a5ylB1UWXPigPftec7dNIC8b4_Qru0t7GLwEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQMXQjE6f7DO9bWg8PqnXvEYZLGmTHix500G3J0pfd45CZOy85ToInUCihqBf8RK317Rzaqa5wRwe7M8yOgfSFVEupvAZ335LF62f3XDEDY1YpqZJ4X4WhNo3rTj9FkAwPg_89LPBvabDCk0iTov1motLv8VphZfqp3owSgy3-z4q5KXYf5ySXlrPtAsNnBJeKyrA_D6s3Bk4gi70e_dIkux9ZvnChgKrmo-mDh8yodJ97KqueKA8e_WaMU7hgDz_mfiWnSGP1x-rj0AoSV_dloxntzko6iKlb1tmdSwGNZoLJgfqrJaIGux4UB6MEMF4IHnfRgcKu69cGeQbu7B6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwriN4Z7beQf0BeOSMoWBvKJWiFqspb0kC9YvNAHjrplwfO7aYwxzt3CqcxIGxhOezEPT40IFzL-weDEAN28tTn-A9-sAPFL8xGyUcGu-T9JGZvjeHyFKdumOLza0EdNesedmPNHD3vVqUZpP1oRyogt5gO5d89xxnu7sTFszex4X2D37yEGUbBSGEDokhhpUmcja-9s-Bo0wuwzrb7pWFqrabyINPvIhIOeZmPxLz9i4qfjOg4MIRLArrEiIhBJt4FlPSxMVkDIJrf1TZHjgtPZmHBuIpqIUCfvSKiA0H9BA-juAQBzBvTw-f1Env0f-tQ2PzBet6lTPo4EqBFqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1k3jNV4Q20HYU3jnKNskaYek7_f8jv6DaPc3hZ-Igx8Kxw1l8sIcdtSm-EcyOK8IViOlYu_JE6v59DVZs6e5do1c4kWrkP1PtyPK9vUN4dEH7aNCcCU0K3iyc_Oi9NPOYtL9XbNESYNDhSM2u6FNiO9FdxUV32bAkvkiES7NxiUsDzotxwpyQH4cb91BsD0QR5b5pg6iQ3sla82ZPFLa-Z10qLeZ3UsGr5ihe7rQEyjRDl0XQ9DgRmGKgPttUCMIECr8m4aA8cQyYZKwF-EkE38bb8kckzZU0QSR2VrMdcvNptNnZWTBpi-rf2-lXJXevjRQT2Nk6EZQy9Pb38zvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7znj0xHdijINe5WxR4n91CWy5MLLQs_CanFR8Swveztmr7vljbsYLSlSO7c1h_WvTYRBtOOEruuYFVN9Bb3ClnjkNbaA1XeryvJ-5omyg9dQrgCn-arRCUG5sfLkHv-ErFU3Q6gpazyHOoKxCsGIk10xyHJ41BPgyEa2Nq4L9GW0pKT1TkVjr1lyjnCXkXb9tDAX3Kw91lswTpkNZintukt6yUNZ47rZsR_s-O_tdoEMIUAQmQFG8pe2LXEUHfh-w5wbQLCZcQcaPJgdIXbsN85-a891bhJGB3DqTsoAvP_Q5Nlnysga9r6124X2EmPzGLVCbdzQ5wselBnUSDOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIQqHOpvlyxcO6t-1CYPeAmMja7e7IzyZLF-oaDA17gsLhI40o9IPH_ahX6LUdLkSJO-lFAj2I4HSziWMbVhWQpHMuVvD8RUXMZKwGrds_YoB3ovbw8ofFHUisKvAArz7DuBIuQQ8vHA_mLy-XqabOoZ-G3_xiMcnXzydz124BttOuV_qY-TNeKipzMlDR5EA5zjSJ3kv8QEFv2Z9wBFMeadkGzVboYpkSkZuAq_udtdPYwoigNiST6zw9Sj8IYfACE7qwqWN3VZukp50SCN56Utf-oFBnbGK3xkpbTSfF-v5E1cBChK2Rwbqow-BUIQvhFZGWFdkKIVp_9KSrBP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=NDpITd-eIxRdbAQbo1MmzV916rmnWP_o9sQs6o2iblpfS8pdYcNBbZ3QefXhdEc8PmbGa5wvnuXpNUsXUkFQbCEzoUNlOFvKtv8qPJGKmubZKPDi1zmJmiyIsaWOHLPSHIeWw3alcqSrPn-OyKZYz71DCvfK5X-Ze8nvKBjVc0RiRNvnlQHwnepn1BEcvZ_OlprcMhxtBzAI3LwLAMA5hDTc5Q3XloqRYGEuIxQZiQOCjMIYXEAaRhXJ64WFb7zev935KNy8CUie2zUaC62ATP1wEBZvvtlVrxQ9tXPOM8gtJjUut9m6SV6dvjb_gZjUhrCb5B5OK79ZL9I4n44B4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=NDpITd-eIxRdbAQbo1MmzV916rmnWP_o9sQs6o2iblpfS8pdYcNBbZ3QefXhdEc8PmbGa5wvnuXpNUsXUkFQbCEzoUNlOFvKtv8qPJGKmubZKPDi1zmJmiyIsaWOHLPSHIeWw3alcqSrPn-OyKZYz71DCvfK5X-Ze8nvKBjVc0RiRNvnlQHwnepn1BEcvZ_OlprcMhxtBzAI3LwLAMA5hDTc5Q3XloqRYGEuIxQZiQOCjMIYXEAaRhXJ64WFb7zev935KNy8CUie2zUaC62ATP1wEBZvvtlVrxQ9tXPOM8gtJjUut9m6SV6dvjb_gZjUhrCb5B5OK79ZL9I4n44B4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=UsafrRVYJRimnw0CdBlwh3sAhBl8HJNUW2_sgDjgh_YBqI_cbpE_Y-Rc0Sf5zTg9MacMUyM-wh-B1UddHSCZQroNCkbZUXSy7FP2dvfAgQ9LTVCob1FvVaOHulR00NhkmMBRSAFR_srlSGQoyvqKBiovSLeT-BOxUOr1YW-a35qcqDrwW9CIeoqzYjAY64_WTXML_UZANElS6KvBQTSGgKrwWdb85nxGEXwn3TNfP5RNACbB-mH3Y7ZnRgc6mFnu--98-5gM9KPjtduG7pKz9REZDdDrk1-KQ_t_1bmDQkFThQQuv9vdARpLAiPiWbQlZutrTZJ-VrPyZPCfIUl25A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=UsafrRVYJRimnw0CdBlwh3sAhBl8HJNUW2_sgDjgh_YBqI_cbpE_Y-Rc0Sf5zTg9MacMUyM-wh-B1UddHSCZQroNCkbZUXSy7FP2dvfAgQ9LTVCob1FvVaOHulR00NhkmMBRSAFR_srlSGQoyvqKBiovSLeT-BOxUOr1YW-a35qcqDrwW9CIeoqzYjAY64_WTXML_UZANElS6KvBQTSGgKrwWdb85nxGEXwn3TNfP5RNACbB-mH3Y7ZnRgc6mFnu--98-5gM9KPjtduG7pKz9REZDdDrk1-KQ_t_1bmDQkFThQQuv9vdARpLAiPiWbQlZutrTZJ-VrPyZPCfIUl25A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ov_nNOUpJDpNbBRX-Uoh3BMJ0GavyB852puTzBn0AwKMcFkNRiyvCs-h-fR1cIl-o5FCQwUUR8wHBn141X19NkMrUHDa_SH4d9YoWmQ_rZJbYovE2f6dlx_PE6Qyo0wMtIn0djvHghx30AZP0cveox-qCsQYSisew5WzfWIKVnMsIm0MDisdyV1iXAFdNIT2GrKQknXGDVJpJcKnaRVaE7T6gJf7TciZmsebAMbCsFovJBcLi_yi26WBJ06mse2OYB6CoKB-z8rAbC6uiMEo9eEj7N_hAc-KWt7AdEG0tGWYWQhkmioFdwlGGDoKOa09ZRCDTSXcA7Twz-WeDAjEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ov_nNOUpJDpNbBRX-Uoh3BMJ0GavyB852puTzBn0AwKMcFkNRiyvCs-h-fR1cIl-o5FCQwUUR8wHBn141X19NkMrUHDa_SH4d9YoWmQ_rZJbYovE2f6dlx_PE6Qyo0wMtIn0djvHghx30AZP0cveox-qCsQYSisew5WzfWIKVnMsIm0MDisdyV1iXAFdNIT2GrKQknXGDVJpJcKnaRVaE7T6gJf7TciZmsebAMbCsFovJBcLi_yi26WBJ06mse2OYB6CoKB-z8rAbC6uiMEo9eEj7N_hAc-KWt7AdEG0tGWYWQhkmioFdwlGGDoKOa09ZRCDTSXcA7Twz-WeDAjEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=FR5CUyy18wygiMW-PYcgSaN_2LhPseOCDf6dBXUQbQUvaWT7TOtOtkRDZtcEq40BagUGrdEAXn_r1pv5DZMyTNzLmsaIKD960aaGbT2iKupW_mJsMmPS2oF66xqJEXqOenSsr5BI37qC4_s1DhDt9DlefZRLCcCBUpNZSS3r4NQczePKnrSOxnOY4v02xp3zpANarYIUjZi7jWc-SMtSQ2tyYp7_6ih8oIbYXtgm6j4fgLvcL76FB5RwOmB-RavyCqxX2Jyf5FJdtt45Nu0AMX8pBd4Jf8PvaxE0Eay3fA93nCzrk37utHM8CpXKn09zPqBE1UcWp2UbNQHaNgNuAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=FR5CUyy18wygiMW-PYcgSaN_2LhPseOCDf6dBXUQbQUvaWT7TOtOtkRDZtcEq40BagUGrdEAXn_r1pv5DZMyTNzLmsaIKD960aaGbT2iKupW_mJsMmPS2oF66xqJEXqOenSsr5BI37qC4_s1DhDt9DlefZRLCcCBUpNZSS3r4NQczePKnrSOxnOY4v02xp3zpANarYIUjZi7jWc-SMtSQ2tyYp7_6ih8oIbYXtgm6j4fgLvcL76FB5RwOmB-RavyCqxX2Jyf5FJdtt45Nu0AMX8pBd4Jf8PvaxE0Eay3fA93nCzrk37utHM8CpXKn09zPqBE1UcWp2UbNQHaNgNuAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=lHbfrtiHPF2QIe2B99T7urWjjfZzBJeVjXjbmsLUktnf8sTXS4hVAUbI6VL-Muu4QGIoJxyD8cAS1B-Q17QjULJtBgZ9ilQjaR7yLnCNjJhIKRo99Kj-CS79qhT4S4qzNSRavvjhzXx76Y4tGQDJFz3tUJ7VpDyRO-0_NsnQ5Yrs8HHJNQYiNXHN4mOQD8vjfsOoRaj5faRILQcCBuDzx3cu6MuA1RHnMHDjKtx4xJtQDbFAyns5BBmOcWVJR5TFLTBCW5JASqsGYm2rUJVIx3VL58MFeOmZXHEDgRCYrT-uuCqEZAvw0JN7JpDHY_ntZe2eHVtWNJ1VCKUZ84bqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=lHbfrtiHPF2QIe2B99T7urWjjfZzBJeVjXjbmsLUktnf8sTXS4hVAUbI6VL-Muu4QGIoJxyD8cAS1B-Q17QjULJtBgZ9ilQjaR7yLnCNjJhIKRo99Kj-CS79qhT4S4qzNSRavvjhzXx76Y4tGQDJFz3tUJ7VpDyRO-0_NsnQ5Yrs8HHJNQYiNXHN4mOQD8vjfsOoRaj5faRILQcCBuDzx3cu6MuA1RHnMHDjKtx4xJtQDbFAyns5BBmOcWVJR5TFLTBCW5JASqsGYm2rUJVIx3VL58MFeOmZXHEDgRCYrT-uuCqEZAvw0JN7JpDHY_ntZe2eHVtWNJ1VCKUZ84bqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=kGWalSHnqqmxQcsNU5mmH_vzj9hDbqWQ5Y8JoM0pnEmbgEkTkeWXid3436QS4IOySJZRULWhWqB-q5A7ZQu-R0G57hombhoDMOjCg-LMKKz-6Id-kllzC3UdtzSUUs2xG5vaRH3OWQFsWDPWFWQvbzqFzcH-9zIITSMqvXjf1LY-nWVlAb_ebO-_RT8vWgsC8aMRU7hAPJ8NPm5YvTd8JLzIPVZuP0LJN54PkQJw7wuQuzD65yn-YEuVhWBSI84WPtypVJaropAol2i5aoFiz24atbInX5HSN-JhsjUyjGPHy9p3s1oZEpPVMGRmeEL8e4T5T7h1khYG5tQXMiXxpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=kGWalSHnqqmxQcsNU5mmH_vzj9hDbqWQ5Y8JoM0pnEmbgEkTkeWXid3436QS4IOySJZRULWhWqB-q5A7ZQu-R0G57hombhoDMOjCg-LMKKz-6Id-kllzC3UdtzSUUs2xG5vaRH3OWQFsWDPWFWQvbzqFzcH-9zIITSMqvXjf1LY-nWVlAb_ebO-_RT8vWgsC8aMRU7hAPJ8NPm5YvTd8JLzIPVZuP0LJN54PkQJw7wuQuzD65yn-YEuVhWBSI84WPtypVJaropAol2i5aoFiz24atbInX5HSN-JhsjUyjGPHy9p3s1oZEpPVMGRmeEL8e4T5T7h1khYG5tQXMiXxpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=qqFjkiw3hukW1cx-SK7_apR1Mol4iKlCovH21OovpRqZuS1tKT686DTQcAAMcYBxD_jC9qRxtznNrIOMdrUAIkPVsqBQPfFhPF_-Suofs0J-NsrKzWVToFEiPmPP6OhuDs3lY_PUG-5hjOFP4mvk5At1W0-JrUALjumcQSaAyr7eMm1auLrOGSDvvnlAPHmnzT6SEbVdUBX3nZmS0gGlwMo8yBwvfrBISYqODwfonRgA1QHnqSGqa3IRuwfPIdZOGra1spXG5ptpdpaoAoG2r6vIZXiOYhcAAyUaB8evaNy_c4JIQoL8dcMUiLcUIkhrKYcSgB2_qGo_5SWhQU6qFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=qqFjkiw3hukW1cx-SK7_apR1Mol4iKlCovH21OovpRqZuS1tKT686DTQcAAMcYBxD_jC9qRxtznNrIOMdrUAIkPVsqBQPfFhPF_-Suofs0J-NsrKzWVToFEiPmPP6OhuDs3lY_PUG-5hjOFP4mvk5At1W0-JrUALjumcQSaAyr7eMm1auLrOGSDvvnlAPHmnzT6SEbVdUBX3nZmS0gGlwMo8yBwvfrBISYqODwfonRgA1QHnqSGqa3IRuwfPIdZOGra1spXG5ptpdpaoAoG2r6vIZXiOYhcAAyUaB8evaNy_c4JIQoL8dcMUiLcUIkhrKYcSgB2_qGo_5SWhQU6qFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2DoVTiGabp7sn9sw1YtJwdzfUGrrK9Gjot3buqcbGUXb3XlM3U4vFwldbDmV3zUSQ1nn32JTXe2zROIDvN4ZPeNivOJo9a7Svd_0ZFGFcoKUxs08cTvCJBGUEH0ajUpla0w7gNI0oTnSwLcvPbvtHMuZwWrOSTIQrTcK07zwprGfUrGVIssAOxNHvoJFSOmmptWHPsT3YquMjVLorHBxonoHl2BsTHMlZjssfiYkp2EviJ8nFt6rUtEqtOvLqbbkm9ZkooRQ4SPao7Xvc_ap0YKOQ5mZ8jaigjcMH_KjCcL1IirCEjekDZN7tKSAreYeEI5x8XDaTn7FQuMQO_0Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=sEx0IZyHD8BwHgBXCYURQ_vNSCafjo2ewXk_3xyaW2nx65mThrV6QodDQx9tTqkTG6FDVEGKB9CmqlUuaVQ38f3bTRmIJ7AKpbao5xFtBR4km7dIfUN-ZjEj8Yc9fC-1lGv_7V7fqGwJwIgtbyOrgmkX5uks8GuEreyHh1HwGy03MGjdyJNaTWsfoSqbV3gJIaATaIMdbaZZ-V7JAC_3f9iP3ZrlBvtOsen48HzFOVdur12YvV6nwlkhpk2vacECDWJkIifB6qD1nHLdp3DmUETHbmYR_1I2ikDjj_t0WZa4pe8pe0cnUWd0YdmSQBwPzA0ps2_fsbo1KDUfLWByiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=sEx0IZyHD8BwHgBXCYURQ_vNSCafjo2ewXk_3xyaW2nx65mThrV6QodDQx9tTqkTG6FDVEGKB9CmqlUuaVQ38f3bTRmIJ7AKpbao5xFtBR4km7dIfUN-ZjEj8Yc9fC-1lGv_7V7fqGwJwIgtbyOrgmkX5uks8GuEreyHh1HwGy03MGjdyJNaTWsfoSqbV3gJIaATaIMdbaZZ-V7JAC_3f9iP3ZrlBvtOsen48HzFOVdur12YvV6nwlkhpk2vacECDWJkIifB6qD1nHLdp3DmUETHbmYR_1I2ikDjj_t0WZa4pe8pe0cnUWd0YdmSQBwPzA0ps2_fsbo1KDUfLWByiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZLhsv9EBbh9Ss8GjWdYZDPKF3GsorQFb8qjSegV9Nd5bRmuAacr3zxAmLFnj5JsB1evgaWQBWVQJJffOdS7Po13Ww9vxH3cTYNr3nKkMhCQaD8SICAwpufXdDbnwNXycnXzo9wm_UgApiF7VsH8Af2qDHv2-CRGFbrmt58ILj3lCFONcS7Cw7crCP8MBsrEvjnQhUGxrg9NhCw3-LEjLU8oaq6DGJajp1K_WRrj8mF4USWckMHtgE8avBQ3U7bix1nNDwQ4hXmzmrpsMAv2NizhKBYgQxgcjy2q5LB47K76Mb93DVF-sgFqJdofWCg04sZRc16u9GB09A_o6Iw0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZDwepRvjiUGyfSIIXWLaLTh_oHbvgy6Dq0XMgJFRUt37srxr5RijLjkEZEw339sWmREZjXnekrDSRmVTJIcqBDhEPmZPo1xsqJV1nGrmxg0O1UQNYSIXgUPmKGLVAKNqEKpexb1E8JMbTavSWvq8MsGw6zn_vsEexf-uw_1u8e9aC1D8p9SLXefzjzpco-xtruYPC_Q8cEh_jWXxe9Q6Ets_sxh3gnYY5hXy98-YLPFQrgt0BZ6DU09XMcQsJu4O4SxHGnNTd2UP_DJ6j3b9M4QBfIGhfQrqzyMiVW5Fj1eJyyOKf-3-vEyeWQffPlucLwSPJedyuI_UTSL02V-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiL7NlsD2X166f401okz-gbHXXinNSYA1bZ3fZTDgYmc6MM5puo81-Bt7-bnlCHVR6DQH11OrUzNwl3rE3o0Ls4MSWCILuQtwIwzLf1DdqSF7ob2404ZO_bxwzD3vMvoCVGeWP2gSnx9YFbTKv-ksRofyb2MByrZE0cIJ5t1Y_JbFRVmXc2Ks8pTncBGdLIKmvdRNv9v5TDJDApGr4eWqXufQ7VIiCTzKBrTpmDKXaEBw0dE5vX57lDExgyjFo1lePiLA6enb0HL02lMntfI9FTEBnWUxwvYjpdOin3d5wHWxbLmd7CuQ5DymdLI06EqPCnPqzB5eQZSKw7DUw4JrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGbHAMYw293MMDuAp98F7Bai32mrF6Iww7ry0RQVUbkSCuTCY7sUnupfN5NkKqNrw74iGiiL65wnc57X3sLfKA4odLtqZ28zuwcwO83R8hQSAh_kYxc-TniCboeleiGXoWI1cH0o5TlsS4o3_KQcjmaYwaTiKxz05i2D8TQaew_mfziz-a6cO5zFCq4CtO58EHR2hhiM9WiGVmh3mrcXq4y_BYL6y7H5N0g5HPAfy3La2vtLq3LFaOYP81E2ZAjlEL4vZnFvEhfNBW9KjPpGchtZoSZTt8zRq9zQpg0ICVjSjoUjQ5wY6XpSJ0esOBSarNsKj6EJQqtwqCP0sMAZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=oZRJdhPWDE9hjy1945QBBYN_PwMz6XJeKF-Q8lp2MVZIvr0sUURGFxaKC8fIyPBErtx4pfE29KiQob1OcQCspYGS092MttygsS6vKbJd9aH03VyvEXkjy9irIYP2SAKISc8-qX6c22_JwAAI2KGguPLNB8aReeg4MluVkSgK3ox7e6-5oXDvXfzQK6x3nA063vDlF4W2t0EB2tkODRGjkuo3i35MXvoWTL4dpJlh0sSfNbqCvu2eabW43mDJcvTxSdCRadpPzHxubIaVPBZ5IJY9uuAD4NEi7RoyAhPq6_6Z2WUpA_Siy82f4Qwc_Oo_QjKEQyOnDGMWCI7a8PdhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=oZRJdhPWDE9hjy1945QBBYN_PwMz6XJeKF-Q8lp2MVZIvr0sUURGFxaKC8fIyPBErtx4pfE29KiQob1OcQCspYGS092MttygsS6vKbJd9aH03VyvEXkjy9irIYP2SAKISc8-qX6c22_JwAAI2KGguPLNB8aReeg4MluVkSgK3ox7e6-5oXDvXfzQK6x3nA063vDlF4W2t0EB2tkODRGjkuo3i35MXvoWTL4dpJlh0sSfNbqCvu2eabW43mDJcvTxSdCRadpPzHxubIaVPBZ5IJY9uuAD4NEi7RoyAhPq6_6Z2WUpA_Siy82f4Qwc_Oo_QjKEQyOnDGMWCI7a8PdhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLvhq8rnYGXGF1bjpVGm9SAqSqxQjmr_i6F86cJMylMr7poIaqZa-DMTBgg0XKAhxJyqAFE5kg8SOP7ihLVC8vHX6iLC0kmwfSlLzLFXSyo2rzoqaIu_XPJcIW3FoEfnoAoZ1AgYoTBjDR6FK20SyxfLsKjB3NP4dolFs1bX6PIFD7CTgu2ehLKjP7u2jvu2kQ-PjNPZrVd3p8A4n-vLg57_0ObPpxAxavvMNIg0tKeJ4KRmxHsTVpRHKpz8ZdQKDU90a9d9WP-v522rHyekTqLi2TqUU-oPZwkqBfE4LRn_LogjDUbN8gvPiFg_r-g7tjTAlwCbR40gE3zHWRo7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=tK4ouzkj47sQ22l-nSrXEQVpINgcUE3G5Uddo80lpQ0wFvVrUovvIkNCn0vtqnJLmIbG6nHeC1PY1c5OV1Ro9DZvp7L1dJwq8ZWzEF4Fp9EztXzE8U97Zd3h6lHOyO51lblWdhKpIzYf2h67nUOlGIBwCyCfB9egeT1uT8GvNLDm_G_r2CqWQeiJ4wT9A_hRqjYxxpPR_t_iBLgOYPws8JfdOrC-aqgi4EhJ7bWFKGb4Nl3ldLbyYS6hsFyLkRYLaoBVW-uqCP6f9eZeeoUDbA7QQCD7N8PdMQc4Rz2r-mHwhVAKLZqIVARnlDnZbYtSf9y58WwResO6XLQxxp5rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=tK4ouzkj47sQ22l-nSrXEQVpINgcUE3G5Uddo80lpQ0wFvVrUovvIkNCn0vtqnJLmIbG6nHeC1PY1c5OV1Ro9DZvp7L1dJwq8ZWzEF4Fp9EztXzE8U97Zd3h6lHOyO51lblWdhKpIzYf2h67nUOlGIBwCyCfB9egeT1uT8GvNLDm_G_r2CqWQeiJ4wT9A_hRqjYxxpPR_t_iBLgOYPws8JfdOrC-aqgi4EhJ7bWFKGb4Nl3ldLbyYS6hsFyLkRYLaoBVW-uqCP6f9eZeeoUDbA7QQCD7N8PdMQc4Rz2r-mHwhVAKLZqIVARnlDnZbYtSf9y58WwResO6XLQxxp5rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=nHtusmmQohlUYhSn9m4h8nSl59nhf_kWjT778xfOtvTNnsgedn4XaeGt21uG9PhRRJvngpRknRiL7Gz7SMBUYCo1G9wUSsFuDMtNBL-bhllD5xPvgN2rRlCBMZ4fhgc30AQ9XO-eHsuQI2FhNlZsRZ_qhu-boj1kr2TF8CcV9qsevW8AmaHoLIZLLfmL6ilduC79uKpw2T2f_t8bMDnakW2ndZg7aCNIg9u1U-K6VZ4Kj_kuyKiGDlMKQ7bzLqeRu9qSmguBogxvzchxJ0T7lbdkzoZ7CnMKafRw3xeU2AExKWHoNlwuxSR39Adk8wHhuGjGUAp8Dcz-g8rbdXNMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=nHtusmmQohlUYhSn9m4h8nSl59nhf_kWjT778xfOtvTNnsgedn4XaeGt21uG9PhRRJvngpRknRiL7Gz7SMBUYCo1G9wUSsFuDMtNBL-bhllD5xPvgN2rRlCBMZ4fhgc30AQ9XO-eHsuQI2FhNlZsRZ_qhu-boj1kr2TF8CcV9qsevW8AmaHoLIZLLfmL6ilduC79uKpw2T2f_t8bMDnakW2ndZg7aCNIg9u1U-K6VZ4Kj_kuyKiGDlMKQ7bzLqeRu9qSmguBogxvzchxJ0T7lbdkzoZ7CnMKafRw3xeU2AExKWHoNlwuxSR39Adk8wHhuGjGUAp8Dcz-g8rbdXNMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW-nm6rU2QNmGtk00FjjVHhFhe8O6HACl-bWaAz5SsP_HVoRSDqu_aPovQHL0UfJwPIoRrmMEWC8caXlgzAE_MIe7gNjf2XKJRsJEH1PSC6K2ruxHNBWbWZVQRN7S1YMfv3F60C08MYyeolc2khIaayG_zhIWJCndyX8eC6Ok2izBkLyqNLha1eKVixI7Z77pSVq-nn2SXC7PJKmFr9Tob2TKCdXKJJCN8zI8oIwtRN14P3ilpiI7hkna8QJetmtr05rcpftddGy3iTlyrIMguIwVyUeeBulCAJUigcCe5HSsSYSoiRIVzzaG5pzoZQT0tHya630rHPsMHMcgad78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BptAQo1izwC9wFrfN72ltGcl7JvgjHZHHNeNr4XZhF6Qv34pWjI-SEA1aZW6zZV3RVOvwzo-BgEyC8oLsUoAnR2BOVlBpInP0_TtBVAyVTq1bUjIn9UmfteAiIV5l5ZZx82r6xlId6W-ryJYL9EbLomd3wwdzOGpIroim8H0vIfMGpWLbZMWp4hOKVTBdIk7b05SbY7RuriwnVnXL0NgxLLNHEPZAVIEgGLIHloDZXtINDOTXc8GOBf0aQALX3kn4MdpPlayfRvfp8SaxLspDvgbkxmjCe64m1WcpTz1Tsik76Bd_ZU5zFeFcPiz9y7wWY1QF_B7-V5nmR8HeJ65rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-jj7Bb59eu_rZY1bX6_KSOjohIswGy9klMCxYLQZw_1A5HPUtHZIM_FAFGG-YNgAi9ahfr8rAi16BnsFtGMLUWMMAe-U5LTfUTNkaVSYtZW2BUN6brDSzhQtpQXIhVKUjlG-zz07iNyAFEblQhNSXpTxbtLjsS3ZND_r1UueFOMJq763ejl7UmCTIFTOhdZzRqKepkq0LhKave2UGQChmcRSIH4PSQPpk4T-1Q97jEwLMTkGMaNLgSnxpK2oaU9jlpsfpc_oAAyJ7BpadGZJ1aQC0SQiF6pLEjhciUGzjZrKaY0IpbyNzFGhmUQnYpsT5yRnd7Ct6Q_LxHRrCT0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=juAu-LJgvdL9Yg6oBzenhyVdVSyEw8fPf3uPb7oUTABH5ggZOBLJRqvAr8SCuO1tt7niB8TjCGzJHaamz16kTeSoaqsNnQM8r8hJ0lVLNaOj7YJ9ArniID6m6ukSs9-zrWN-_qrJiOMr7nV5DPoA29fbeJ8h3rBnt4qZVNHrXCwOjT0W7zHbXJ_RbT8F_5CFIWxfSjYz_snYRIRw9g2jnYbiNuKcEYCuTu5w9BSDjSMGOcVcLj5aYpQecN7Es08soiVSuETGV72Mny6VjaHVLMN-gdvXZzHXxOgYgpfQMs67LGzWoVSEeGJE8eO8AReeSKJ-hDCvxHCcayIpblb1Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=juAu-LJgvdL9Yg6oBzenhyVdVSyEw8fPf3uPb7oUTABH5ggZOBLJRqvAr8SCuO1tt7niB8TjCGzJHaamz16kTeSoaqsNnQM8r8hJ0lVLNaOj7YJ9ArniID6m6ukSs9-zrWN-_qrJiOMr7nV5DPoA29fbeJ8h3rBnt4qZVNHrXCwOjT0W7zHbXJ_RbT8F_5CFIWxfSjYz_snYRIRw9g2jnYbiNuKcEYCuTu5w9BSDjSMGOcVcLj5aYpQecN7Es08soiVSuETGV72Mny6VjaHVLMN-gdvXZzHXxOgYgpfQMs67LGzWoVSEeGJE8eO8AReeSKJ-hDCvxHCcayIpblb1Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=VvfPNX2hqwPAalmqjnwoncKfblVbSvQbo9hXEbLfHniXRadFp-trgY8MyKso5obe1bG60Cphgon4gPS0EX8AZq5cuiGzSb3nj1JiBPh7Vp6joCfr-WUCdGJNyPpuyvNyBwy1LKrMRODto_XfDfwZyJfQ0fJj1-eoiGo0R7dyjF0QP8tDh48EJxDeOvIHJjK4l0zqomVfyqQlqQDbp_TaIxB1UwiR_1OVTiy1p4kMjT-v_13IZsXtOpwYZWqwUzQrVcMjdBfOkpll0RHo3Bm-_eYqvD8LY7sJFfEk0JduSCpxzqipItq9juQgQi7IXJw82hHuq8Gy27xjOw6eEpqX_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=VvfPNX2hqwPAalmqjnwoncKfblVbSvQbo9hXEbLfHniXRadFp-trgY8MyKso5obe1bG60Cphgon4gPS0EX8AZq5cuiGzSb3nj1JiBPh7Vp6joCfr-WUCdGJNyPpuyvNyBwy1LKrMRODto_XfDfwZyJfQ0fJj1-eoiGo0R7dyjF0QP8tDh48EJxDeOvIHJjK4l0zqomVfyqQlqQDbp_TaIxB1UwiR_1OVTiy1p4kMjT-v_13IZsXtOpwYZWqwUzQrVcMjdBfOkpll0RHo3Bm-_eYqvD8LY7sJFfEk0JduSCpxzqipItq9juQgQi7IXJw82hHuq8Gy27xjOw6eEpqX_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl6YHMgz0TTJbGSfYDl8QRNUVeq11jTeJohoFO9kKtY_nZtKpyDwn_57hmj2QFrOF86DM74J08Mh5r-MVkwVVEiWEXy7NhZMjrB0wjEYGm1Vco3SDJA0RSKK6kICe35ob2Gf_blyDhHNgKbhXCy7KRvVdo3B1ZpZk8V0InhMCsccNpOmczHX8zzlDuT292YrsZ_7jEzVYdbKtAqpFaQ87PFR6oWUl_Q8yF85-fQWL4-hIR4zd5vU-6XZXwswNUXkUi3rdO66Tmxz-eZo8Fmf8_im8uzTxmjscrAcoMVlLKUQq4wOkgiTLAOc8P3YnESFWiLNGxwWccyHLaaYxVvFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChzNS8c-D8YBmlT_e2ogWCSe9WfIlAK7ERVtrVDX3n7FuFGVaG_MLful8kuLIAAK1RAjxM5KZ0ekMp4V8x5IqV8T-ht8OHZfsaXnJCkmnJANAEATYAAZyC9dzv-1eMDXYKpQCDs8ypuUQ2LtPQ96G3BQ3iJQaHlG0wKkaaXAv1c3MwpF3kQQ62idddJ68KoeqmDqcJOPmMi8T607bwgZRPuCMoRW1OObfA1QhrlLGZyq2eqONT6RjSsabymbS5NfaAhhXRmwgTlAdFLXzhtszDiycXx6M_DYuK83a5Y92ComPN3iKwOuFYD6Zzg0KvHtUrgSR5wohFZBbq9TjB4tbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9KMy800uBYANyqDN66ZIBAs6ovNrDP6f8E6VCxQN9P2817_ombmZakpYclCYIfOcFuZWk98Ns3l0fxl3K3iG_m40LYmjtxkZZJ8cBWINuZSXgUeyHG7sduM9wMMNAEfz8PCQfV4rSMSxsVPMParxLjaZMjbs_OKvpwaIo-QzAfkChpLINJVIQx9RP6eIQUfDQTdKVyPliBbwn2Ng6PK0-QssZjL1alcyIvOJHdATWr8P9ABEgCpS8j57gfiHcs7mpVtUJeuHcYjHTDXE5cZVUXYT1IpE6mtGVugPRTPjeC_vn94bbqZhhpGv5n1QykZafdtJRQ9H6vWEcFF--e9Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc2cF-389DZDnogwgW9xSP1gb61qR-b3DKZqpa_zFoXyGydd9kMJcd_43TZa9vINmLEt-kJwFGQOBfsJLbdeKB1WU1WTFDj_B_qtDL_newrXsvaTbU3HFS5Ki1E5gspUbiVekiJePWiRgY242AQs06OXzZ_5scHQjep9Gn4cRxLLyhtPk5auen2FUFGUKcN3j9dA13jxUwQ9WA5qwFrOiHQuhqqCzGk2Nub2jcKuJCEjcFzKFACABQUPVvMFZTJmFb3brTMjP8Ie8Ebchm3IWpueNafbD4uujGu_cRQhpGcC2Tsmq4sgbjgcwsvQfoyOyd73lmRCSLyiQkM6n29VUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIsN1bgbRwi4_zllho0qR2TPaN0_-02sd5nEaZwzJLBz58KOPqAZWL5QGbYObfH85oHpwSCD-LTWlnvxe-B8jshMHr6nilIbJEJzzi1elkK7a4htyOOyyYZ0RorIBKCV5FVkWmJ8B8BoCDij_B5c54XqRYBjUsppWwYmZLFa82_c4BupNddfRaWW_hnip0nTffd771Z-1IiZRNA04CNYxjCp9dhLh2e_QyZlPNb4q5AUuzKspnpkSpqFKJ9IXOSwlf3YsgyiLm_ShwRRTQ5cRiKlJpydHSTULi3PpbZlvbPjktNma5f-grUMwKo_DQtLPWf7HhiMrZJgSBx7jREAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
