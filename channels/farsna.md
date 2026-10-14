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
<img src="https://cdn4.telesco.pe/file/ocKYKs9iU315xM4wHHhfrLd0x9QiDVbveYlc4rKECH2cyQFrKMZei-VrfsjIu9zBGsLRRsu2st9hFVm4B3G3I8sXOaHef5m589DIYK2f6JqgZmbvh8A6BStTM4RDG0gKDtv-CdnfnH1Va6WR_rEACpK4GZIkLiCQEbVb3eRRAbLw32RPXAV2PLqwWOQZjNUefb5thxw6XiKBc8yuWtlwUEf27RhReZEpAzO430V68zqevFBvOb7rPQbF2uNKb6m1gXiNSxdjEbiKgzaCvRHQDdRbBzzynNAUtPKVN1EoJ5hdGtsOA4OYS6RfA1kItNoAyaO2EbqDsSQPzxuePxI3Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-468405">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3272863e3f.mp4?token=Y2sgq-Ui0MJYwXh7oO7m1HOXXuEyGzOGyRSkEg9tc3rYGFe3LPRlMb9OzflPosP0ZzvvxRsLXUhqiZ4QWruF41jbbVq5qLubo5oV6rIjCI8YPnD2my-yPVHDrQ_C39SlesaXD7AQQQKdLKq5SjczS6WFBNJs3Q47b0TM8LT0EjQ3S_zyDekRfO5dyGVcMmWxZ_rppeWlX9cKVoVWfWEInbwycAd9jjdmX4iOI6bEg3SzjQR7W0qtAbjpR4kGJ8a78Vtg3Q5JQh12TzE38H0rZVTCfpQTlskQmkOqnOZhR5BNTwJ54e2axsJFJHdAFJH_7-nhykeQG1n9Bs0lhs77WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3272863e3f.mp4?token=Y2sgq-Ui0MJYwXh7oO7m1HOXXuEyGzOGyRSkEg9tc3rYGFe3LPRlMb9OzflPosP0ZzvvxRsLXUhqiZ4QWruF41jbbVq5qLubo5oV6rIjCI8YPnD2my-yPVHDrQ_C39SlesaXD7AQQQKdLKq5SjczS6WFBNJs3Q47b0TM8LT0EjQ3S_zyDekRfO5dyGVcMmWxZ_rppeWlX9cKVoVWfWEInbwycAd9jjdmX4iOI6bEg3SzjQR7W0qtAbjpR4kGJ8a78Vtg3Q5JQh12TzE38H0rZVTCfpQTlskQmkOqnOZhR5BNTwJ54e2axsJFJHdAFJH_7-nhykeQG1n9Bs0lhs77WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ استارلینک چگونه در حمله به ایران مشارکت داشت؟
🔹
گزارش اخیر رویترز نشان می‌دهد بر اساس اسناد افشاشدۀ پنتاگون، «استارلینک» ستون فقرات شبکۀ نظامی آمریکا برای هدایت پهپادهای انتحاری مانند لوکاس در حمله به ایران بوده است.
🔹
طبق این گزارش، دیش‌های استارلینکی که…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/468405" target="_blank">📅 16:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eK1xrZjPvgN76n20FQKYpS6aB5iVKefGsVPivDQPCrtmt6hMbrZ_J8Q2_63C3vDCq7YwrlzByADsA2oB_fuopXjC961Fe_xw52oqCgnQj2DCXP_4RWfYPSKTevaBMEBJjWxhKO7bnpnhR-D0h0MuC5Jm2ClMhvlgPyV7-h5oWIycFptKqKbXMmonQGnGJoNb0cbJUcnSEIr_HGbmNk2K_Dg7frE9vg4tS92kHiTw9-JJNli3nQhp4C0fW_kXqIGg7GiZ4BfmFshc95lPMAye7S7ISnrO0CCyzzm-edyPPMCMToFVT4HrsPmPicF1XbotlPI2NfV2FdlNuL1wkHkLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdIO5CzoROpsPvgpeB473Z7IUE5q455cMBTU9VLQ5UcDM-t-2KTxTIprKXhWCLxxzGbNmKsW8VGzYhE4EzQBpvSV0Av-HdILBedWTwfEsl9X7QP3EZ5An5LXHylWVgVOEosUxKa2qyJH9-5kYB7dtIE6bbUe5WTBuP0dS7wNYL3pdBx-syQ_gqGFfgCm4D1lYXCQD4Xs3VoxjFr4Of1fdbETSjzQIdTHgg3GtyGiVbnIzlIe1gQx8Lx22hbsmS8FZGT_aQr7vpgMjHiyx6_6BIypcjO4I1mHtw4mkpUt0XurwhHy0lwFDD0Ts8E1RmuCYE1hYSPAu11TSaj7lyz9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkdte265ffHKkovx__Usjw77GrhLMqwo1L7k6YqTmykRxoh0PR94DiXPPGQWkumNiZB752V8Zxubyq4Rd861fMuZoSi2pvC7F3ormX_SKbtKbr2D2IL1aS431LCp1v-gULjCvyJYXSbZF5Q29b44TkAAcJkzESk_Hy9CGHn9As3NZEruu3nPQGOaptE1XJ_4SmvUUDHLIQEZ_JHK4gR3fNhWeLkmaT6Ryd_W8Q35ieKGQHgchpDQUDv4dgq250eRqsn_w3dbT3O46KCk9jLcWU1FhsE0qn-ku_-SKUYVfhOfBN7Httva3-vX8X8MknS1-ht2tnW9Hm0hDAi3VgrfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3h8_UhL9nYJL5towWdXPdrvjNwzPk22ZGRvpdSfWoNJMBhvuwxV_AdAN3euf5cWmhuvfUOZ7wbrtNqrNhB6VhO6uMI3epXsRyToD-Aeu6_A2u-Ql5EU9-XNuErUENqYtHlAzTTfW66zLV4ouk1ysjdli3rJgmFd3mrt9rVzwyZU545ShP_h4XDpZJMymstmw-ZkRUhQPOKan6qlhmk8n03ZbyJkGnrNCxy7-3fQdIhvQNceTTLiYzQTGOcj_BS_MTygK0-qsMNCxCWo1a17u1NVOpDjU-fi_-hlprs2adsMOGs3axZp0J743TE9Kv6kl23JTFc7WFtUmScWhpS8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRHj_aW0r4mbbwRjdDU9S4NVAhk6RlZ2HaQnIV_GMnYU4-QKaKwfp5nAEah2gNzryBU7YWkQn5_Kv_e-YAnJPeVdhwNtRk1nWdCVPowIYBMPhkUAsNM6WeA_2P5TgH9b9yGcN5JsoFKpAMVZ2sbaQT2aRi87OGO71S6pHUEQISiVfIgBFExXiHcT1bqFuyZARsgCA23YMysyZvPmHBI_p-MGIfbsQUD997DAg3WnXzUJM2pk1HBAMgRcuOCCCJdT3_RyKK5kaCo5fIZeLwBPLdPpD1HUeKrJG6ubEWfUhl4PXf1Cf6VNqOzskySvcpKnwFkzngP_gd99D_NP_ZjrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpv9ushtHNWs-RH1vukxtWGrP4OLwoAEPOJlxTuc2OQkHGtyxLWHFjgdy9_vtcW_Bdmq6jkGcdnFK-1ax7OnUeYZ2xjt36_8PzSqtynVsxSMtk2T1DGlygsrBkLrAeGjpMQpYd9H3A8F8CZly7LT1o_2VfjzuNh4dgeKDVHvbz0zibXRGSq6ZtiXUOoAsBXUDo84wLOtHOTx9Oyl5omfVfaO6XwJh-ttQyJjjzIRKtTh2WkSzBExXuNuKtaci8EdhxzYXa13IhhKvVSmMzyeUFUFFtmKyL6VeJycmwe4CJbmg9ZQH0-SZdz8N7fUMp15-8yofA7D6UfXJ7AKUoP-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgNX_ye9chl5RuUpHCLxBqgSokXll1-PScVEZQa97sWT5NdddFGEmBWBS8VFmnsSOwO7QPdibcxksss6y3pWaRBDeKUGHe8MB_7Sj_7LRCBnHerQW5TKVAQvKdj2xsGh8iMKjVdKclsynHAGNpW0iQmvy5Uo5VbRGxchqWTwWVVU-NyrF1FNfABTX5ojqYwqsGtwPQPQLErHuED2ajukICpjV03XDuB5ORWMT0WCjXXw8ai3wk8XNm3V6wJtiVK3vZCdTjHRd87CDG7BzgydIHA4QwxBE9OG7WU1b2jyx6XRLwVpRo6RXl4DN4R51sspNAiTXTv1izNF6GJmvGbTrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
بانوی گرمابخشِ دست رزمندگان جنگ تحمیلی و مدافع حرم درگذشت
🔹
فاطمه فلکیان معروف به «ننه‌عصمت» که به‌دلیل بافتن دستکش برای رزمندگان جنگ تحمیلی، مرزبانان و رزمندگان مدافع حرم مشهور بود، درگذشت.
🔹
دستکش‌های ننه عصمت در سال‌های گذشته به نمادی برای مقاومت و جهاد…</div>
<div class="tg-footer">👁️ 337 · <a href="https://t.me/farsna/468398" target="_blank">📅 16:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0fa9c476.mp4?token=RwqrUEFqbJxwlZQEo9KzQXym_502NSvzPcWKFBaROARmLNcW3Xngxuxh8Xc27W0nO5mhugUOh2UfrIekL-LvTJh7b8lKgCbBdbjQzwzhmx5-LrGtDZK-qprCXysVBOGLowx9S_LHXVocWfGlwIL7Grd4gQvp6GcdTuA26A8BA5fu-49amzA9BvBiVzHH7Brb1I63wnfp5oBoduVc8I1WceAWVYU_TcqienNr7GjLem5Zq95Jx1PhV70LIChb6A1uP_k2pj50LU9OTHr2hkAxxlxQKB7PZPQpaZQpwcAVwsS2P0FluYqNXd4d2uFzHNxzPSTNVmPFLCgYPyw_8oZ7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0fa9c476.mp4?token=RwqrUEFqbJxwlZQEo9KzQXym_502NSvzPcWKFBaROARmLNcW3Xngxuxh8Xc27W0nO5mhugUOh2UfrIekL-LvTJh7b8lKgCbBdbjQzwzhmx5-LrGtDZK-qprCXysVBOGLowx9S_LHXVocWfGlwIL7Grd4gQvp6GcdTuA26A8BA5fu-49amzA9BvBiVzHH7Brb1I63wnfp5oBoduVc8I1WceAWVYU_TcqienNr7GjLem5Zq95Jx1PhV70LIChb6A1uP_k2pj50LU9OTHr2hkAxxlxQKB7PZPQpaZQpwcAVwsS2P0FluYqNXd4d2uFzHNxzPSTNVmPFLCgYPyw_8oZ7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری دیگر از کشتی کانیتربر متخلف در تنگهٔ هرمز که هدف مین دریایی شد  @Farsna</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/468397" target="_blank">📅 16:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468396">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5fwV-YmRwsHrOM23upPDUM7sPQ7c-ffDMCpJHNGWmuNKly2RtBC4o3jqWoYoJXTblHcnT4mb48mei1RyxaJY4dhW2UuOdYrx4pJFMyc9Zz3bh8kT0ve_kwQh_xzID2_7IWJK4zHZELgo3eH6zWP863SCc3TasyHq5ze0L30JegZCzxRAAznMak7VM9aZfXduYCSErSCvdwVBd9b_-0COPm3nTj7RE7Y_M6oIZ_WKO6xVMwTJEO8ggFJBxvLftHVQUonMWD5dugd7WQgGTlKRMxmRNLdW8UmHe4LAS2VulT507R12frOJJLjwT0cXfvNGoHTr8Xt_rfc8OpiOUAkeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲  گروگان‌گیر در سیستان‌وبلوچستان به دام افتادند
🔹
رئیس پلیس آگاهی فارس: یک مرد ۴۲ ساله ۱۴ مرداد امسال، هنگام کار در یک میوه‌فروشی، از سوی سرنشینان ۲ خودروی ناشناس ربوده شد.
🔹
کارآگاهان پس از شناسایی محل سکونت متهمان در سیستان‌وبلوچستان، ۲ نفر از عوامل گروگان‌گیری را دستگیر کردند.
🔹
با تنگ‌شدن عرصه بر آدم‌ربایان، گروگان آزاد شد و به آغوش خانواده بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/468396" target="_blank">📅 16:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e1f81f31.mp4?token=mDkGsZXHlZwPJP-D8W_Tn7Q8KTs2m82tD7w5Z3vxgKJWJXBwvRZQYGZDfaGMUPTVLC8jyqbItKoUvWZAWurgO_JzgRz2Nf6W6PhXyJrLGa519HMODkHIfbgqZc0O65tk7qwnKjisfr_71iqpNQWWUz5vsgxsDgqkz1DZsdBfXP-B0LvRtsuBQLkEPL5oCTgIUZGbN9zhK0S0X-tRY-IpxqGifZRDW-3NvxZuYjKztt9UYNrgXn0y9p9aoJP6EGCge9Yp7fI6OeekTYuGJYmMWE71SBpkawBAfRKUBV05yudCddq91BDrR71FBUPsenEFOdVbcmu_4cwCMu1HS7f-hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e1f81f31.mp4?token=mDkGsZXHlZwPJP-D8W_Tn7Q8KTs2m82tD7w5Z3vxgKJWJXBwvRZQYGZDfaGMUPTVLC8jyqbItKoUvWZAWurgO_JzgRz2Nf6W6PhXyJrLGa519HMODkHIfbgqZc0O65tk7qwnKjisfr_71iqpNQWWUz5vsgxsDgqkz1DZsdBfXP-B0LvRtsuBQLkEPL5oCTgIUZGbN9zhK0S0X-tRY-IpxqGifZRDW-3NvxZuYjKztt9UYNrgXn0y9p9aoJP6EGCge9Yp7fI6OeekTYuGJYmMWE71SBpkawBAfRKUBV05yudCddq91BDrR71FBUPsenEFOdVbcmu_4cwCMu1HS7f-hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقای رشیدپور؛ باور کنیم شما دغدغهٔ تربیت کودکان را دارید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/468395" target="_blank">📅 16:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYIIAgw64aysZafuwQOnJB0AKpqEC3Iy5IopGotzK7az2kN3gCRQxQ-LLE1AjaRL07XLlykdU8HtQOWD1AjpHS6u2SlSBN413Fb8hQhBo5YLCrgn1o8z4ow3hVd-F3mud-XKLxPWmQqqGnHpoA6_h-7ADu_-T_O3oeM43-FeMyL2HZcX_DZVM4S5ADzjggTqn6dE6gmRFrvi97NPcc6FAHtU0-ebARDVBxJLb5aBZ2YpJz4fzh1ds_VS2FkOC-fnDuqm0fKRGoYSya2eayE7oMGdIR6Be_P3fYfY2DzTgduiOEDbKaxEEEijep3XWTmSGOOYXumQrvnmKBFg75SSEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمان ثبت‌نام کنکورهای ارشد و دکتری اعلام شد
🔸
دکتری: ۳ تا ۹ آبان ۱۴۰۵
🔸
کارشناسی ارشد: ۱۶ تا ۲۲ آذر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/468394" target="_blank">📅 16:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سند مالکیت نیشکر هفت‌تپه و کوی مدرس اهواز صادر شد
🔹
سازمان ثبت اسناد: با حل ۲ مشکل ثبتی ۷۰ ساله، سند مالکیت شرکت کشت‎وصنعت نیشکر هفت‌تپه و همچنین سند مالکیت محوطه باستانی شوش صادر شد.
🔹
همچنین با صدور سند مالکیت اهالی کوی مدرس، مشکل ۴۰ساله مالکیت در این محدوده برطرف شد و اراضی مستثنیات سد کارون ۳ نیز پس از حدود ۴۰ سال صاحب سند مالکیت شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/468393" target="_blank">📅 15:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468392">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXuX6JlzcbRktKc5qRGjZ7imKrM_CfmhK1fpYZ62MhW3Hu975etXN-_O9gz1QdiflL9j9RQL2pqTco1_t_q51S8wo3OTUe_fgWg1qQqPoQIfDhsaGWFZuydNygQqeP_FFmvgqb6d_98lix5p3fCgVSbsXB4qA4UmLdpaDi1tmWBQTl_UvOYBU4olCOrb3UbUOquZOeKJovfZg_F4cAwIzDbig8c2OrjCy2mNipbCnvy29StT26KyACTeTGOH4L-kwsSEQunS73G6PJWAqdQCDkfiXdBxwOVgY2GSCfhWxrYGoMLnUXdXIT33gurnreKAi7XCvt_d2o7ym_heQcqOlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم انفصال از خدمت مدیرعامل‌های فعلی و پیشین هلدینگ خلیج‌فارس قطعی شد
🔹
دیوان محاسبات کشور با رد درخواست اعاده دادرسی، حکم یک‌سال انفصال موقت از خدمات دولتی عبدالعلی علی‌عسگری و محمد شریعتمداری، مدیران‌عامل پیشین و فعلی هلدینگ خلیج‌فارس، را قطعی و لازم‌الاجرا…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/468392" target="_blank">📅 15:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468391">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdVrMEr0m0AmiGpzIxTIbdhFz4ppQQ6ldEH8-KGHRhD99FxqveQ6bk6-5xQCi0v6HQ_-YT8qHe8V70PZ5naDopWgBf7w5q32qFyTGtMbWy511dTTjIxno3h73_hXekEzK7Y8C2dZMZMAUqC9eZyLfMHNMVADmYX9KD_auJkbLP5_cC29nmuX2g7200jDmKQyvhFhRj-VeacYV_zy_FkyZmq9NBxCJtW3E6xEssDrZd29NGFJNGVun_uvGfbs7MI1aFy2zU0qJpaEL4DTcwwmBtXHTctdIWgg4QlrIQdMAXKASnS_oJxahuylRByT9YL0uEjk5kjawwE5orKvhhZkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشکیل پروندۀ قضایی برای بلاگر هتاک اینستاگرامی
🔹
درپی انتشار محتوای توهین‌آمیز و هتاکانه از سوی یک بلاگر اینستاگرامی، با ورود دادسرای تهران برای نامبرده پرونده قضایی تشکیل و برخورد مقتضی صورت گرفت.
🔸
این بلاگر اینستاگرامی در فضای مجازی، اقدام به تولید محتوای هتاکانه و توهین‌آمیز کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/468391" target="_blank">📅 15:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468390">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959217c881.mp4?token=ZXUW_QV6gvKdinZ_pHKrjJ-kQGGXNrpidfF4i5lFl9dK65jS-xiPEpbfOzNcBAtr9PHnQ_VuNUZusVaT6IojxTu1gTqCROB6x-R7XKeXuYFYNBmoDIcpawm-3w3tOGOiHQbtwkOO3XuivprxY5whTuvhFKK2zSQC_Q-0Toe8-QP20TsjD67BIBK6Y9A2xIA4rTYUr1oUM4ces58rKCc811F8-ek-WEYQTWG9YRfcjlHgPTPL29PO6J4AU9ET-5PuF_uH4roIi0s3-pdXaw2KIaD0vvWcxltXc9-Ijg7c78EsF2GxkQUhd-B0OShQy8Wqb5rHVYP_JcChjBxRkDvlYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959217c881.mp4?token=ZXUW_QV6gvKdinZ_pHKrjJ-kQGGXNrpidfF4i5lFl9dK65jS-xiPEpbfOzNcBAtr9PHnQ_VuNUZusVaT6IojxTu1gTqCROB6x-R7XKeXuYFYNBmoDIcpawm-3w3tOGOiHQbtwkOO3XuivprxY5whTuvhFKK2zSQC_Q-0Toe8-QP20TsjD67BIBK6Y9A2xIA4rTYUr1oUM4ces58rKCc811F8-ek-WEYQTWG9YRfcjlHgPTPL29PO6J4AU9ET-5PuF_uH4roIi0s3-pdXaw2KIaD0vvWcxltXc9-Ijg7c78EsF2GxkQUhd-B0OShQy8Wqb5rHVYP_JcChjBxRkDvlYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ استانداری هرمزگان: تاکنون موردی از فوت سرنشینان لنج صیادی که صبح امروز مورد حملهٔ پهپاد ناشناس قرار گرفت، گزارش نشده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/468390" target="_blank">📅 15:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468388">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KKMUS2MM401miWqk38F2BhgdT-LABt3tG6ZhXvJEXxuf6wSO1Q4kGn4kYdK4KNn6pmlI0fSJ_u5MAP3r4PdOM5JpNe-gxAbOypBZenWEujqac9VIzvkOYA9hlA7cTfuu7c3-3YPa_VQ5Kiy58Em--DiZxBTxaqcLFtWnBR24fXJSO__NdTzwn6P905ZPyBbZhBOHlfCark-kwBSJ5Ro7NXwLagVXEupfeBL54r4bK-tRh1SVMdf30iFd0kwDRccz7KkMA5t9WXtmPdak-1r7bIhhaL0CGEqs_0N7KmuxTaZXsr300tm1ST8ZedzBDSrSAVr7eMnCcoBTV8CNZEH2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/li4QfPusC-_Q-pe6BjawaXgViJSutoW6ITpBS5lEsVcGpMR7L74SMkAslW9oOAE6WOJuQ64BPDU5_tBVYGSEuchYByhUhgNr_jny3pE54YQCMe6_MlEDUFrj_io9_xYiVLCj4_EaFe0U1IYE9M3qWaW13g3gcM5MwdGudrORG_6IOvFy9BiswGOGkpC38KRNA8xSjeijUa_ESPVMHWOIC48hnb2xxfY_EiCIVclSEadcNB_Kv8PY2POX1DmDUiBCmJVeVhNh0eqva06q8SveSTXayXPn9XJsloNs1lxxeAzHkH8Ga-pYva-RM8M9kt5pQQJHw2PY1Mqj724hXIfNmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خشم کاربران ایکس از ممنوعیت حجاب در مدارس آذربایجان
🔹
کاربران غیرایرانی با انتشار تصاویر و ویدئوهایی از دختران محجبه آذربایجانی از اقدام دولت آذربایجان در ایجاد ممنوعیت برای حضور دانش آموزان و دبیران با حجاب در مدارس این کشور انتقاد کردند.
🔹
کاربران خارجی با اشاره به اکثریت جمعیت مسلمان کشور آذربایجان اقدام دولت علی‌اف در ایجاد ممنوعیت برای دختران و زنان محجبه آذربایجانی را نشانه حماقت آن توصیف می کنند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/468388" target="_blank">📅 15:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468387">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rxi60V15Qfwd4026EcJSHmi2UOoDoRYTYQs2KHj6cT4XY_48J16VIfJM_QeasdjPKSY0czadJzLQ6pb3p3kB_l5haqcfAwhK44Yx3eQZ2QC7ytvbYqusF1NosiBGxvtAUkw91-Xzm6_y9MWtQ2TSNIc1nRPC7niRdnBWY9A-gjD4eSD_B_1ZysbT8IWzPXtkJQLX1flX_9aq12SrAalnVbzd6bIu1y1LNH1uwiQWPkf2sU6_cwbI0pjTymSkhWp5aBlO417c5GUwOgXDIkQyn7ZXiJDyO_brevAnobONxnYoiKYE6X_vk974Vbx4AJNt49g9stAySxQgOwBs1fyMSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rxi60V15Qfwd4026EcJSHmi2UOoDoRYTYQs2KHj6cT4XY_48J16VIfJM_QeasdjPKSY0czadJzLQ6pb3p3kB_l5haqcfAwhK44Yx3eQZ2QC7ytvbYqusF1NosiBGxvtAUkw91-Xzm6_y9MWtQ2TSNIc1nRPC7niRdnBWY9A-gjD4eSD_B_1ZysbT8IWzPXtkJQLX1flX_9aq12SrAalnVbzd6bIu1y1LNH1uwiQWPkf2sU6_cwbI0pjTymSkhWp5aBlO417c5GUwOgXDIkQyn7ZXiJDyO_brevAnobONxnYoiKYE6X_vk974Vbx4AJNt49g9stAySxQgOwBs1fyMSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای مشاهده‌شده در نظرآباد آموزشی بود
🔹
درپی مشاهدهٔ یک هواپیما در آسمان نظرآباد البرز، مشخص شد این پرنده از نوع آموزشی فوق‌سبک و متعلق به فرودگاه پیام کرج بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/468387" target="_blank">📅 15:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468386">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/898eecf6ee.mp4?token=YDzLR4j-dIoIydyYlwnC9di0klbkciCR0cALGHd893zEKvFEM4YUE4SnlQ9v_kMPmuE-XOLbwcW7_sl88u_w-Bpx8YQ2yTwa5nf10xa38RySR7s8p9chh2B2BT52kQF8zpethljKSaYESNjQYtzgmwCGvMo6LWnON0lYsHNfddOeLreIkI9XcDavdhkFjdMnZC1305TRZNLrgFmlWiLYHeuG9tVTt1uVQG8klTLEI8ZqZraVD9tscp9rgD1CHXTwkbEaV_0xUf0ZJMYAHzT9-YUsS5oq8UAvTSRENxydjwToFN7oMQUkzc4tRyaiT6_SccZ4yV0VIogVrhS4rEqJGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/898eecf6ee.mp4?token=YDzLR4j-dIoIydyYlwnC9di0klbkciCR0cALGHd893zEKvFEM4YUE4SnlQ9v_kMPmuE-XOLbwcW7_sl88u_w-Bpx8YQ2yTwa5nf10xa38RySR7s8p9chh2B2BT52kQF8zpethljKSaYESNjQYtzgmwCGvMo6LWnON0lYsHNfddOeLreIkI9XcDavdhkFjdMnZC1305TRZNLrgFmlWiLYHeuG9tVTt1uVQG8klTLEI8ZqZraVD9tscp9rgD1CHXTwkbEaV_0xUf0ZJMYAHzT9-YUsS5oq8UAvTSRENxydjwToFN7oMQUkzc4tRyaiT6_SccZ4yV0VIogVrhS4rEqJGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دادستان تهران: سامانه‌ٔ ضمانت الکترونیک حتی در روزهای تعطیل و ساعات غیراداری از زندانی‌شدن افراد جلوگیری می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/468386" target="_blank">📅 15:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468385">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370bd006a6.mp4?token=AZ2so6AJt7frpa_w13nd2mhHUxsUILwLz8ujdG1vIdzuEZXDVyVDKzIZ4IghxMF6FmPcVMpIXO2OBk-EsWfVGiWEEAQHtJAYCT_Ba8Pfm9B_gGkFXz_BV4uMTsEx9AvwuknWxgKcR6UjYQSuO-va-i5SW91tVOob_S5w-sK6PP7LEBPbQTqxVYAhBNdMaIdsJRcAnXZVPbqb4B-gKxE9PmK3XMfoDIKFbGM7kNrbGwOESg-It8eq_gD2RrvztF-Y6fCpAvf2E46l8Z8xIYcj1uC_ZFMSnKYqlaDP0QvmN5EZX8FC3lmFMy5OovfPiDChY9lja0kWwbN8_uCApd5KmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370bd006a6.mp4?token=AZ2so6AJt7frpa_w13nd2mhHUxsUILwLz8ujdG1vIdzuEZXDVyVDKzIZ4IghxMF6FmPcVMpIXO2OBk-EsWfVGiWEEAQHtJAYCT_Ba8Pfm9B_gGkFXz_BV4uMTsEx9AvwuknWxgKcR6UjYQSuO-va-i5SW91tVOob_S5w-sK6PP7LEBPbQTqxVYAhBNdMaIdsJRcAnXZVPbqb4B-gKxE9PmK3XMfoDIKFbGM7kNrbGwOESg-It8eq_gD2RrvztF-Y6fCpAvf2E46l8Z8xIYcj1uC_ZFMSnKYqlaDP0QvmN5EZX8FC3lmFMy5OovfPiDChY9lja0kWwbN8_uCApd5KmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنگنه، عضو کمیسیون برنامه‌وبودجهٔ مجلس: مشکلی برای اجرای طرح افزایش اعتبار کالابرگ وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/468385" target="_blank">📅 15:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468384">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259d22a2ed.mp4?token=c6HOYfYIUzpQMWM507jwVe6Ymg5U8IeHFsYoM4z6gZoarat5EUF8h5-gbZOa3PQLTSkBs4rFCe1JJG03UxplJQOtdNW6DWdZQTPyouptAhM6lL7m0gdbKhMwfmqTeRUvWCHqPRu7RJb9nxV4-5Vxg8bygODQ-mvgGYXWqncgmKHSDbtcm33A23qOgjKBbxQ8WDFuS-rqkIqWFtcmSs6bdMhrngteYTdW0ldynJjJFBQ3_aXIH8Mq3NKOH2vSFLVmrGlU18bwUIRv1oiaiPvmpPHYZO6Jxf502RCaJjt2ekSi_Yn7adGJoZgjxgbLxhpGqRdRr_gwZ9g85Y7SOqVoUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259d22a2ed.mp4?token=c6HOYfYIUzpQMWM507jwVe6Ymg5U8IeHFsYoM4z6gZoarat5EUF8h5-gbZOa3PQLTSkBs4rFCe1JJG03UxplJQOtdNW6DWdZQTPyouptAhM6lL7m0gdbKhMwfmqTeRUvWCHqPRu7RJb9nxV4-5Vxg8bygODQ-mvgGYXWqncgmKHSDbtcm33A23qOgjKBbxQ8WDFuS-rqkIqWFtcmSs6bdMhrngteYTdW0ldynJjJFBQ3_aXIH8Mq3NKOH2vSFLVmrGlU18bwUIRv1oiaiPvmpPHYZO6Jxf502RCaJjt2ekSi_Yn7adGJoZgjxgbLxhpGqRdRr_gwZ9g85Y7SOqVoUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاهش یک فرایند قضایی از ۱۴ هزار دقیقه به ۲ دقیقه!
🔹
رئیس مرکز فناوری اطلاعات قوه‌قضائیه: با به‌کارگیری سامانهٔ ضمانت الکترونیک فرایند ۱۰ روزه ظرف چند دقیقه انجام می‌شود. سیم‌کارت، بیمهٔ عمر و سایر دارایی‌ها هم به‌تدریج به چرخهٔ ضمانت الکترونیک افزوده خواهد…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/468384" target="_blank">📅 15:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468383">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1eb42e3d1.mp4?token=lOqaFvLDtcY9z6di3g2PGojpz5taUl-qomXtuUrIHQmt0u3XxNqnTIHM19bu0KX_djrLofgiRee0pMoGDhFFJLlV0MaAFV_Qug_O-IOoJpuDeHX90PFvL3nnlUG_GR4G0q5jhHOWgxG86GjiLh-Idn-Qxaen5Tv11Fae7f7HSjdidJLpQHaWnF8zivZQ7xUkKuuBoz-23BKUPfs03ZIKvlfLeH7dm34YMvLT4w8dfiaqt2-L6jt9-fdutzvO81z1GcvMDaghU1WWuJMXrSHZWQXszWamDU1gHK8d48oNdwZa_wu0MCItLtM3GLo1jHEIMX_goDDu_rUDKMBCCT6KWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1eb42e3d1.mp4?token=lOqaFvLDtcY9z6di3g2PGojpz5taUl-qomXtuUrIHQmt0u3XxNqnTIHM19bu0KX_djrLofgiRee0pMoGDhFFJLlV0MaAFV_Qug_O-IOoJpuDeHX90PFvL3nnlUG_GR4G0q5jhHOWgxG86GjiLh-Idn-Qxaen5Tv11Fae7f7HSjdidJLpQHaWnF8zivZQ7xUkKuuBoz-23BKUPfs03ZIKvlfLeH7dm34YMvLT4w8dfiaqt2-L6jt9-fdutzvO81z1GcvMDaghU1WWuJMXrSHZWQXszWamDU1gHK8d48oNdwZa_wu0MCItLtM3GLo1jHEIMX_goDDu_rUDKMBCCT6KWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان بازداشت‌های یک‌شبه با ضمانت الکترونیک
🔹
رئیس قوه‌قضائیه با حضور در یکی از نواحی دادسرای تهران از این ناحیه بازدید و به‌صورت میدانی نحوه ضمانت الکترونیک در این دادسرا را بررسی قرار داد.
🔹
در این بازدید یک وکیل دادگستری ضمن ابراز رضایت از اقدام صورت‌گرفته…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/468383" target="_blank">📅 15:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468382">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7fa61331.mp4?token=K17TCm_1gE3Ae-nJOJ0TiRm6ee7yvaKKM83a824tGh8n2RvaTR45eSOZ8r_VmK3zCBxw5g-F3X_yF7y9myDJVcu2fsu67gtNGgHIwifY9uvCb-gnoII-SY2iJfwY2G7sQ6Syt1mdbUNNGniOK1LLa4JJX_V8GoxFpHRSxpzsUYO6uYDzx6PeAoNmbXMw8VI0Vf4HYHwNeqnFqSAOpn8kwXd7N113ZzwKDCoyAJUfXaTBiuBLMYmE6InaroR0BnVWNrXZFkrVlfR_vkGSMtAtHf2B7wwpqs8wU5rAIWy9EVYg4hATadp7SFYhIws4A9K1k93jC3Aqz47vsCZS6cM-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7fa61331.mp4?token=K17TCm_1gE3Ae-nJOJ0TiRm6ee7yvaKKM83a824tGh8n2RvaTR45eSOZ8r_VmK3zCBxw5g-F3X_yF7y9myDJVcu2fsu67gtNGgHIwifY9uvCb-gnoII-SY2iJfwY2G7sQ6Syt1mdbUNNGniOK1LLa4JJX_V8GoxFpHRSxpzsUYO6uYDzx6PeAoNmbXMw8VI0Vf4HYHwNeqnFqSAOpn8kwXd7N113ZzwKDCoyAJUfXaTBiuBLMYmE6InaroR0BnVWNrXZFkrVlfR_vkGSMtAtHf2B7wwpqs8wU5rAIWy9EVYg4hATadp7SFYhIws4A9K1k93jC3Aqz47vsCZS6cM-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صادرات دارو روی ریل رشد
🔹
رئیس سازمان غذاودارو: صادارات دارو در یک سال گذشته با وجود محدودیت‌ها حدود ۵۰ درصد افزایش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/468382" target="_blank">📅 14:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468381">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjrOcLM2lEexrRcLxjTdFNhEpPOfXvQv4DwmtI01_njWpzOzwFEvS4jakkMFGTT31GGFl7Uo3zxZrGxFzUHWGXRxaQkGY_PYC3fhImfY9xS_aogqyqkRGTu_I9n9hlEJT6OFhYq6BKOAkROnzrDJFhn2_VuqCmJCYrJopxLBjwF26hSXcwyeGEsHNKvzkqCtJs5qsqzqDRRzCHScafDz62tu_ui8Cdf9kjV6rgitmpya6EeuRXfViVePR6QKMw7ngiZAKKfv-m3ZV10iG5a_DtgqBIboXY1GOlJFjsiF_iCQ0zMsW6YF53IEmW1M0JjWl6lwf_ON_vOmJPHPH_PHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشتیبانی ۸۰۰ میلیون یورویی بانک شهر از بازسازی تأسیسات آسیب‌دیده پارس جنوبی
سرپرست وزارت نفت در بازدید از روند بازسازی پالایشگاه پنجم مجتمع گاز پارس جنوبی در فازهای ۹ و ۱۰، از حمایت‌های بانک شهر از صنایع نفت، گاز و پتروشیمی قدردانی کرد و بر نقش تأمین مالی بانکی در تسریع بازسازی زیرساخت‌های آسیب‌دیده و بازگشت ظرفیت‌های تولیدی تأکید کرد.
بانک شهر با مشارکت در تأمین مالی بیش از ۸۰۰ میلیون یورویی پروژه بازسازی این پالایشگاه، از احیای تأسیسات آسیب‌دیده و تقویت پایداری تأمین انرژی کشور حمایت می‌کند.
این پروژه با کارفرمایی شرکت نفت و گاز پارس و مشارکت شرکت‌های مهندسی و ساختمان صنایع نفت (اویک) و پایندان، در قالب قرارداد مهندسی، تأمین کالا، ساخت و تأمین مالی (EPCF) اجرا می‌شود.
مدیرعامل بانک شهر نیز با تأکید بر اهمیت حمایت از صنایع راهبردی کشور، توسعه خدمات مالی و اعتباری، تأمین تجهیزات و تسریع بازگشت واحدهای آسیب‌دیده به چرخه تولید را از محورهای همکاری این بانک با صنعت نفت و گاز عنوان کرد.
تسریع در بازسازی تأسیسات پارس جنوبی، به‌ویژه در آستانه فصل سرد سال، از اهمیت ویژه‌ای در حفظ ظرفیت تولید گاز و پایداری تأمین انرژی کشور برخوردار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/468381" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468377">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SA2ZebbkmbX1vGiYA7gkYfSz4Jw5slMoIs707qrIkC1un0iHmbNAX5cwJTwY_VH3qACexLEYVEfdLC-47_I5qnAvT_u-Q7dWdD5czRfM-52rkabDdcZ_IP4gx8ndXSo56kAMNyM_iiOYsAS_diVJ6qlOM1euYmVmQSRBmkqq6luxLrNYqKkGnkOMKWJqwyaQmM_AWc8ewg0Uh0uDG2lAprMMt36fROLlaTqjAMGsbBYSRcTAaX1Un-2rO1MjempqE-_hB8LyVpw7ZWKTe580zCGs3EO_vQHVZgZxFI0O-U8ylsjKah9ovBCZGnJs76xtLHxBgRwHI6h_UhHOjRpOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERhs_xIaY8qlNF2GnRSUOShr_Z5PWfbM6PIKeJkFpc1HyYF9XfUiIIY4RQei4C0ZdZAwp-j7O7w7gU1ftv0Hqigyg07XhwF7Iyq7amCxqDmytFOybnkj0pxSsiIMWRmSjKvWreEVes9AZdDB2xM-_utwtgDaqKbvCwbqW8Dpfpt9UE3P1CvCjf2f2_RRuKJj9_ci5i_c-w0yOA5kCMfuw-AXo1Z72U9_KWS0miYYi81drnqj-qKqFikvKaIndECDwU03Y7Psd4LoGxVQ6uT8_kYq6Ari-2gfXp3J-o4SYsyGGZq5IH8Qoam6IdmfufiRUkxnxghE_2oP9ooUZ-cw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDxGaW9Ks6Eb2Ur75MNBaELgwLX5hF3pZUOLLc5GWUdRwRstyMzYVoyymZoPChJxFNG5Z22yLGmeDf3Y01vwaNSuT_Unm7WtK0mQD2KAbC3VzUcZwMpqgGucFsIE9GfQejrqYQYiwnBY_cPd58PJRfDvrck53rCfqVVdhPZCs12KDdjL2ou6tQcReFJSBJExFsYZUQVGi-83azhJfPenvYdi3mTCx1c6IpYmkvfpwFO6IEj9-B2z_2CnKH42U9ND4FNoxGI2w6JKmXYyOcYrE9frZr2uPIm7xfDA7tL154UHUd_aulD5l3Z2kwBh70Hd-dHBfw2iV-WFwqWgpiWN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqM37OmcNsh6YZmZOPpaAs7Wo9Mp48WF6VlxTpgepRRckGqNUlNpagyUR7bBy6nfPkOfYzR0QlorB-A2yDOf5mvWcuWRCc62osmcMh6zuwO6d7mQ1oyhdpgZda9sEtGCpdyoZx1wGCO_VLAFVGwIzjzPQGNRLAplV4JBiTD2J2GVPgD4i5zM_LL8ha3mc9Py8J3IwnnicUPXwzbO5zxz4V4rnORQj5bWCw_6lTE1wfOedNirKHqF3N6RCIaQ-6re2qcKt_j8U8zxslRSFW3EdbRDc4iVEQl7rX8MvhbEaAJ-UR-Pk8vxJZEhXva60POVujFNVxbs-WWH3mMwr-fDYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در راستای تقویت ایمنی و تداوم تولید صورت گرفت؛
🔰
جذب ۲۳۳ نیروی ایمنی و آتش‌نشانی در مجتمع‌های مس ایران
🔻
معاون سرمایه انسانی و پشتیبانی شرکت ملی صنایع مس ایران از جذب ۲۳۳ نیروی ایمنی و آتش‌نشانی در چهار مجتمع این شرکت طی سال جاری خبر داد و تأکید کرد سرمایه‌گذاری در این حوزه، سرمایه‌گذاری برای حفظ جان انسان‌ها و استمرار تولید است.
🔹
عباس پورافغان در اختتامیه سومین دوره المپیاد علمی و عملیاتی آتش‌نشانان ایمیدرو در شهر سرچشمه، با اشاره به دشواری‌های حرفه آتش‌نشانی گفت: مطالعات نشان می‌دهد آتش‌نشان ممکن است در یک حادثه عملیاتی طی ۲۲ دقیقه حدود ۴۶۵ کیلوکالری انرژی مصرف کند و میانگین ضربان قلب او به ۸۷درصد حداکثر ضربان قلب برسد.
ادامه خبر در مس‌پرس:
mespress.ir/x6V3
@mespress_ir</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/468377" target="_blank">📅 14:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468376">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/468376" target="_blank">📅 14:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468375">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8bd95a66.mp4?token=Jgus9Ic_wVXaxSbSctyHSyCm-T9czbd0a69UFH-q0eQWTjZtuSyFbN4Hw-NKHOQkThp4stA4OTOgVAQIqXC80W-pPhjq3kEMNv0dACNIegZ3Uq4q2dxqlKt47iuZ0qrYLDi9UzNgfM-bWJcMsPCMgoJUmVYzOXK9nKtX4iFz-EWLu34G8js2jdltaq-MHXGqSQR8XruM-a2Ko3O-xBhdOzRb_yiPhwwGtxuoOrMjTrnGJ5Q_B2qNqmgkxEW4Jbtx7xvEY_44NwJWnB09UcdKtAfF2shL_VjrucrTCsmGevplI2S_XRGRIITMwGwmW6oTXXyPl9OqgDuJb64Uo4MHZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8bd95a66.mp4?token=Jgus9Ic_wVXaxSbSctyHSyCm-T9czbd0a69UFH-q0eQWTjZtuSyFbN4Hw-NKHOQkThp4stA4OTOgVAQIqXC80W-pPhjq3kEMNv0dACNIegZ3Uq4q2dxqlKt47iuZ0qrYLDi9UzNgfM-bWJcMsPCMgoJUmVYzOXK9nKtX4iFz-EWLu34G8js2jdltaq-MHXGqSQR8XruM-a2Ko3O-xBhdOzRb_yiPhwwGtxuoOrMjTrnGJ5Q_B2qNqmgkxEW4Jbtx7xvEY_44NwJWnB09UcdKtAfF2shL_VjrucrTCsmGevplI2S_XRGRIITMwGwmW6oTXXyPl9OqgDuJb64Uo4MHZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم فلسطین توسط دانشجویان معترض فرانسه به‌اهتزاز درآمد  @Farsna</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/468375" target="_blank">📅 14:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef5a1b7bfc.mp4?token=KfMLhPWImyCgE-g6pcxNL1EA0YdDXTVF9k-ot4LCRRI6rDovU0uyknOtOgApM0SgMcWQEVgaF_geS3jhs64UrBtBP9teTpBNutxWP6nwHYSnC1my_Sk6NXTzahA_lwvJdflXrZSM-yq4AwVJ8tuQ_u7zG5w2wrB_RQG3dJK_7dlpt3cO6fQ_lMV1FTNdU0wWZCB1JDFD1anNNzJEyCre_hlVHvryhpGVYyTdHDgQGvFO0XbMTjs0BNk5jMb-XdmPO-B6Z3-kGEA5wmPM_sE2HYLCNgHuT0mwHrgaaTOvZZTj3XpsOgARdWdQuXqRwav9_ukpeJMVOe4gTXTLaKAduw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef5a1b7bfc.mp4?token=KfMLhPWImyCgE-g6pcxNL1EA0YdDXTVF9k-ot4LCRRI6rDovU0uyknOtOgApM0SgMcWQEVgaF_geS3jhs64UrBtBP9teTpBNutxWP6nwHYSnC1my_Sk6NXTzahA_lwvJdflXrZSM-yq4AwVJ8tuQ_u7zG5w2wrB_RQG3dJK_7dlpt3cO6fQ_lMV1FTNdU0wWZCB1JDFD1anNNzJEyCre_hlVHvryhpGVYyTdHDgQGvFO0XbMTjs0BNk5jMb-XdmPO-B6Z3-kGEA5wmPM_sE2HYLCNgHuT0mwHrgaaTOvZZTj3XpsOgARdWdQuXqRwav9_ukpeJMVOe4gTXTLaKAduw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تروریست برنو به‌دست در خط پایان
🔹
علی‌سینا مصطفوی، عنصر مسلح با سابقۀ چند اقدام تروریستی در کرمان از جمله اقدام به تیراندازی در میدان آزادی و اقدام به تیراندازی به‌سمت سربازان وظیفه و خودرو‌های عبوری در استان کرمان به دار مجازات آویخته شد. @Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/468374" target="_blank">📅 14:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468373">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380c18fc7.mp4?token=vFsWiMZs5s3xQv7uU4FAqbqhT6kliUskqPp7wCv0I2YSEOOMyhVt81DJWzAObT67U8GrUzcUkyPEq-xY_IjZIxJUqGGEJKYcl9VSukYugot-ozF4luuMws8tDHV228PWAFdBc9urdjmhZ5Oo5KRqWeOWWKvwwbP5ID7OkQlNS1qxtKzgsJNijI_dNInRHN_Ugw481GO-EW2XaehZIjcPXyXK9pUxOFc6s6hlLEO6FgHRnbkoF9WB36_gfwLVN3yzDF0w5i91lEJb928eY2912sLHrRoqv_NVfM5y7p9qjv5wxzRzrNXk7H7HK3wgmhQAT3QUXb9WVrjDBHeNnT2d2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380c18fc7.mp4?token=vFsWiMZs5s3xQv7uU4FAqbqhT6kliUskqPp7wCv0I2YSEOOMyhVt81DJWzAObT67U8GrUzcUkyPEq-xY_IjZIxJUqGGEJKYcl9VSukYugot-ozF4luuMws8tDHV228PWAFdBc9urdjmhZ5Oo5KRqWeOWWKvwwbP5ID7OkQlNS1qxtKzgsJNijI_dNInRHN_Ugw481GO-EW2XaehZIjcPXyXK9pUxOFc6s6hlLEO6FgHRnbkoF9WB36_gfwLVN3yzDF0w5i91lEJb928eY2912sLHrRoqv_NVfM5y7p9qjv5wxzRzrNXk7H7HK3wgmhQAT3QUXb9WVrjDBHeNnT2d2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
ملاک‌های جدید تعیین وسع اقتصادی برای دریافت کالابرگ چیست؟  @Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/468373" target="_blank">📅 14:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468372">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59dc0ea4f.mp4?token=lfh_vOM5v4X7QcfXR1RGEVPeHKeDou5J9kixxmnR55CRSgDTxMK32yFfqKBqPf8R5i1mT8QUGFCRvU5bjOFWCN8VwvXXH6vWBWjEk0P-mvAxZJrN_R2wjnwj2H8WFIkAyOVwVRI5qFDFlGlcBismotzNGhpG21MMRLHOQvaYYEalG6lnffhkasgLpX2XXNDA0kZL6hxNhm5fh4kmMsyiZQH97Ul2-D5eceWH60qHg1K15_EAYem09nOuyo4KBBuaiUxfFfu4wTjPkX5LNtspu-YvFF26TanJI6bEfEU1cGOm-NVSsBqadcJiHvGsENECwZXR6j9INu6N3gRlLLzftQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59dc0ea4f.mp4?token=lfh_vOM5v4X7QcfXR1RGEVPeHKeDou5J9kixxmnR55CRSgDTxMK32yFfqKBqPf8R5i1mT8QUGFCRvU5bjOFWCN8VwvXXH6vWBWjEk0P-mvAxZJrN_R2wjnwj2H8WFIkAyOVwVRI5qFDFlGlcBismotzNGhpG21MMRLHOQvaYYEalG6lnffhkasgLpX2XXNDA0kZL6hxNhm5fh4kmMsyiZQH97Ul2-D5eceWH60qHg1K15_EAYem09nOuyo4KBBuaiUxfFfu4wTjPkX5LNtspu-YvFF26TanJI6bEfEU1cGOm-NVSsBqadcJiHvGsENECwZXR6j9INu6N3gRlLLzftQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  عربستان حمله به فرودگاه دمام را تأیید کرد
🔹
سازمان هواپیمایی عربستان خبر داد فرودگاه ملک فهد در دمام هدف حمله قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/468372" target="_blank">📅 14:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468371">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqnhgOYRrERK85w8gCNPse9eh8B9cHFu5aRGhSSn-oDgB0YtOcTQg2YOMoWe6yXcsytaMenR1-Cg1jw5OtGnXJffU_RSqp6MG_mO1DTAKbWUOCxmEtP-5NBlTFjKXzajOTdl-w2kHfgOsb7dasNppV0hqNSgeGOdeKWRHXV6RD7BxFGDCATsjriuvw5dESolOSlxtA3QnbK3KRDvWbGVueE8rIme0_EzNrVr-UUIfQc4-PjR8VuFZQvE_2wG22H9XS0GrgoCSTGyF_JZ_CUHYN321RV37aaxs60PWTUZ6fD0e7nbhKlWQVO7RwFLB-nGfZ-c5s1JFlPWrtW8StI9HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی انگلیس هم حادثه برای کشتی کانتینربر در تنگهٔ هرمز را تأیید کرد
🔹
سازمات تجارت دریایی انگلیس: دیروز یک کشتی کانتینری با ظرفیت ۱۹ هزار تن، هنگام حرکت در مسیر خروجی از تنگهٔ هرمز، هدف اصابت یک پرتابهٔ ناشناس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/468371" target="_blank">📅 14:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468369">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c19a77bc22.mp4?token=LocB1Xd3Gh2ZJVfxjNQLj48xvnEHveT7T2YZyTCC0TUzwyfrshH56BGaYM0-UMVKb81D6dn0S4hzmpQPt-mHT6WJjZN71ax1dtaS9nWLHRhuXO5fxOXhcJ9Nxg_oPrlNCEpSJ58QpizwDDGnAJ0CKZVwCK-CENcbTBPFkSofOEa6ueEDWykYg1wluPydvAqCTyL1DCiW_dJy8pMjVYdYS546ZFSBlhCr4LxtNLDI42k3oiQ2O8KSpCjQAGyRMfDecy2R8h7u_470Vdvyg2E5N2CLqSH01Q0tqKcG6K-XZcwOq8urmADEg9dPDvBUScUQCNhw9-gmNSqjxfQsh9_tag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c19a77bc22.mp4?token=LocB1Xd3Gh2ZJVfxjNQLj48xvnEHveT7T2YZyTCC0TUzwyfrshH56BGaYM0-UMVKb81D6dn0S4hzmpQPt-mHT6WJjZN71ax1dtaS9nWLHRhuXO5fxOXhcJ9Nxg_oPrlNCEpSJ58QpizwDDGnAJ0CKZVwCK-CENcbTBPFkSofOEa6ueEDWykYg1wluPydvAqCTyL1DCiW_dJy8pMjVYdYS546ZFSBlhCr4LxtNLDI42k3oiQ2O8KSpCjQAGyRMfDecy2R8h7u_470Vdvyg2E5N2CLqSH01Q0tqKcG6K-XZcwOq8urmADEg9dPDvBUScUQCNhw9-gmNSqjxfQsh9_tag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری از لحظهٔ برخورد کشتی کانتینربر بامین در مسیر ناایمن تنگهٔ هرمز  @Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/468369" target="_blank">📅 14:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468366">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEO-xCUFpPMNatdSZa4cr7qIJ09vxQEpGzd3C0fz9HzcZTvfMWjDNKMXk8Ivi1OV_tC2Ek0WzTZFG3Bfwwg8fCegIpb30MsxBcAzfhOBcNXR3FKnJ_-K9psH-hm9CnbIOJm4stOl7SzanN8ZckgSFbQSZ0ZhXwf3dh0oNZzU1L3p7bt-XO7K4xxDjyv4IFl5BLGD9tPZEcJjuMcZIdjM1wpXj7vPTjD6PStN6sZ5lsPchkaxLb2WNbQ-jdX9Ez9RwLG1Xr8Mw5F3SrusOQ8QZNyZ2Oy5TxVR-eIAVHUQam9QfhtaWk5Zv9UbyuO1XfK-YLzWYXUMYiRMZ6BjB_fMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axatD2zNC0ud7U_mpoFx4OOhhG1uOjm5OavTP4Z03q9UEpm3uBdTxoqxvBc_jnQjKVFMIE6LhsMbbgt6CjyThsu7KoHq3ga7CsRhWN7ZoiD4iA7nHbax_VqDHWg8SuoX_J_XKgK7QbaeZFYJrsXculDcoA---6afwZ-GPRVKltOMmKRjQEPeFieycvOEiU9m6ykkioZnOxkRqMEzRGN0XUTrv8Wo2kZCWo7w6inYGr2TDzs2PAn8Wu5VnyFm0l3NSRHwUOxG-azRqLLqMG8HGxDxoPvFYHr8KGmfgAlEV5Ygk9pMg7YAHy2HB6_ud0666mOObdHQUGk6FTw1Qu9gjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtWZ_HWEsE1Y_eDLpu-wZXPeGkvBW-nfIYgIRjVhouCkPqP-0FcdL6ILu3paL8z_vlocyJM4mjxgir6xhzmjRM63dN8ICgR4jdwoH_U7tKq4a3FeTXWcTYY5S_9q6t_qpPOZ1c9vKljUEO2KqyJR3tt42sSkjfvoEdQbwZ4tUyy2UQgMFxuzWdMmidC31tCHlKonSxEthir-ocIzyur5BLVBHn9cr9u3fmb5dyXmyou7j6jq0VZ3nbDkCYEcVjxDpHJb7ZRuIp8VOQp00HU9i1uu15xUIJDcf3gJW1QQyimuSR9c8gmTGFWbstuLAon18Pulh_0Oc5mG29wCRzaejg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
کشتی کانتینربر متخلف با ۲۵۰۰ کانتینر در جنوب تنگهٔ هرمز غرق شد
🔹
نیروی دریایی سپاه: یک کشتی کانتینربر متخلف که قصد عبور از مسیر غیرمجاز و پرخطر تنگهٔ هرمز را داشت با اصابت به یک مین دریایی منفجر و دچار آتش‌سوزی شدید شد.
🔹
این کشتی با بار بیش‌از ۲۵۰۰ کانتینر…</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/468366" target="_blank">📅 13:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468365">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2709a41cad.mp4?token=c99c78K1xdiZ2SLB1zOtWNlKdyLyy3YoT-Y-ov8Vu7STeUh91aR3MgLslXWfGJR4iLWd6GlYR5XPlepV2fCSd2a7v4LNb0JnQvIejplG_bPpE5soy37JKuJ-qdC6j385DmEgXdrDJb4LZaSnSAsuYXOqFRXZBkJzTOYB1DD5hWnAoQz3sEqcChZg2_w_HFci6ZLTxnwEOTCJ98XYu8D8E--vy2YT7zH7xw0wuDTyLSO3P1EWvr4_8a0jCzoAFvsTBagykyM9YMziCon7k6MYAG6kHK6tbuRU9cxMhavVkkaTJvXAa619QzVEPE47kzM9FB9-4KGeoYK3QPfDhcj8NacmlWUBeOdwnq4CKhRMjJjry2eHYSzbPisyyggUKuKw6Q-ffueXxm3DLouTRj4DWdxgKihE6lkSIselnzgSyser3erKV2R5zClcJcHL2L5TwOTPSPBFyJOUc_EmWfsKcaX57Snr4z7KZm5hnO-k583ic0NNPK_GIS23IRPVKyITRrqbDf9eUH9g-jlAA3QU-dbIV48xwIN9AVGHVnhyjonO6bO0QskJjF4T7ELW7dOedra0HUlZOIgMOzO3-0YZhv9sRdo-C8Y3OyEQBj5G7u3s1Aq6tiR0xlsv0HV9QPvgmVkvMKxHZqMS2XU6lE5N8IjC_fdvLu7mMO2kAexQRTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2709a41cad.mp4?token=c99c78K1xdiZ2SLB1zOtWNlKdyLyy3YoT-Y-ov8Vu7STeUh91aR3MgLslXWfGJR4iLWd6GlYR5XPlepV2fCSd2a7v4LNb0JnQvIejplG_bPpE5soy37JKuJ-qdC6j385DmEgXdrDJb4LZaSnSAsuYXOqFRXZBkJzTOYB1DD5hWnAoQz3sEqcChZg2_w_HFci6ZLTxnwEOTCJ98XYu8D8E--vy2YT7zH7xw0wuDTyLSO3P1EWvr4_8a0jCzoAFvsTBagykyM9YMziCon7k6MYAG6kHK6tbuRU9cxMhavVkkaTJvXAa619QzVEPE47kzM9FB9-4KGeoYK3QPfDhcj8NacmlWUBeOdwnq4CKhRMjJjry2eHYSzbPisyyggUKuKw6Q-ffueXxm3DLouTRj4DWdxgKihE6lkSIselnzgSyser3erKV2R5zClcJcHL2L5TwOTPSPBFyJOUc_EmWfsKcaX57Snr4z7KZm5hnO-k583ic0NNPK_GIS23IRPVKyITRrqbDf9eUH9g-jlAA3QU-dbIV48xwIN9AVGHVnhyjonO6bO0QskJjF4T7ELW7dOedra0HUlZOIgMOzO3-0YZhv9sRdo-C8Y3OyEQBj5G7u3s1Aq6tiR0xlsv0HV9QPvgmVkvMKxHZqMS2XU6lE5N8IjC_fdvLu7mMO2kAexQRTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان بازداشت‌های یک‌شبه با ضمانت الکترونیک
🔹
رئیس قوه‌قضائیه با حضور در یکی از نواحی دادسرای تهران از این ناحیه بازدید و به‌صورت میدانی نحوه ضمانت الکترونیک در این دادسرا را بررسی قرار داد.
🔹
در این بازدید یک وکیل دادگستری ضمن ابراز رضایت از اقدام صورت‌گرفته در دستگاه قضایی گفت: موکل من ملکی در اراک برای وثیقه معرفی کرده که الان ظرف چند دقیقه این ملک توقیف و به‌عنوان وثیقه در پرونده قرار گرفت، همین مسیر اگر می‌خواست به‌صورت سنتی انجام شود، حداقل یک هفته زمان می‌برد.
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/468365" target="_blank">📅 13:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468364">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در رودبار کرمان
🔹
سپاه رودبار: امروز به‌دلیل خنثی‌سازی مهمات در حوالی رودبارجنوب، احتمال شنیدن صدای انفجار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/468364" target="_blank">📅 13:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468363">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f60420a9b.mp4?token=cM5vVA4965mMPpktqM1gAYlgddwtf5_RdTrT1DM_TbuQMKXpS7RddJP5F87Kkd0UHUrmhf7pE9YZ0BrJzASkolVSEw39WBMFAIc9ydpnx_OcqWh-Pr_GvH18f5eQvv1GbJaVQfsPwGz2gTBWfGECdCuzFYnhnRLTi3EZF_klCooLgIjVvTkLFbILICjn3yUnpB0fT9UCcQNm_J4oxfrdLQ1aYkdQeiSSlAUsxlZGidDpQYpAqKgHTSe6wqwemohhmcIHG4gP3GeL-44NjCXFIdAQ9r2PzOiKwweYzkJMEx1YoocuWNSc-VbV3--DnOQgJ2hnNilTRXMZ_OQjOc6cnGWX7Yd9aGdXfgFLdYkdvUsDbfGJ07HNkBVi4zFWtw0E0L2BE2dDkFNMUm0NjOFLqcXtMCTxuaZ3FsXX0e-vZXWmwJMH8phUR-tehHJROQrBypHRoVN9cquhPrkT1bJrFTYp2jLTN1BV7VxCRFy9uCL-FxiC1UeypQsZGWITW6dpHtJrzLFuIcLa5gGZNw_dMwFy0T9vBvdBN_LWcF7M7dG7cs2hRzTIHHwawu4barZWQT5M9l1vd7kU6QyyQrouF2LrewdFYlqXylrvXF6IbHERDkad6UL0svOT-7kGjar8HHFKOWmxqX8X68lshX2kfpZ7lgHoEu4MAUXutbc2ffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f60420a9b.mp4?token=cM5vVA4965mMPpktqM1gAYlgddwtf5_RdTrT1DM_TbuQMKXpS7RddJP5F87Kkd0UHUrmhf7pE9YZ0BrJzASkolVSEw39WBMFAIc9ydpnx_OcqWh-Pr_GvH18f5eQvv1GbJaVQfsPwGz2gTBWfGECdCuzFYnhnRLTi3EZF_klCooLgIjVvTkLFbILICjn3yUnpB0fT9UCcQNm_J4oxfrdLQ1aYkdQeiSSlAUsxlZGidDpQYpAqKgHTSe6wqwemohhmcIHG4gP3GeL-44NjCXFIdAQ9r2PzOiKwweYzkJMEx1YoocuWNSc-VbV3--DnOQgJ2hnNilTRXMZ_OQjOc6cnGWX7Yd9aGdXfgFLdYkdvUsDbfGJ07HNkBVi4zFWtw0E0L2BE2dDkFNMUm0NjOFLqcXtMCTxuaZ3FsXX0e-vZXWmwJMH8phUR-tehHJROQrBypHRoVN9cquhPrkT1bJrFTYp2jLTN1BV7VxCRFy9uCL-FxiC1UeypQsZGWITW6dpHtJrzLFuIcLa5gGZNw_dMwFy0T9vBvdBN_LWcF7M7dG7cs2hRzTIHHwawu4barZWQT5M9l1vd7kU6QyyQrouF2LrewdFYlqXylrvXF6IbHERDkad6UL0svOT-7kGjar8HHFKOWmxqX8X68lshX2kfpZ7lgHoEu4MAUXutbc2ffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا با وجود افزایش تعرفه اینترنت، کیفیت بهبود پیدا نکرده است؟  @Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/468363" target="_blank">📅 13:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468362">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سخنگوی سپاه: پس از جنگ ۴۰ روزه به سلاح‌های پیشرفته‌تری دست یافته‌ایم
🔹
ایران در جریان جنگ ۴۰ روزه، عمدتاً بر تسلیحات نسل قدیم خود تکیه داشت؛ اما از آن زمان تاکنون، به سلاح‌های بسیار پیشرفته‌تری دست یافته است. @Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/468362" target="_blank">📅 13:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468361">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سخنگوی سپاه: پس از جنگ ۴۰ روزه به سلاح‌های پیشرفته‌تری دست یافته‌ایم
🔹
ایران در جریان جنگ ۴۰ روزه، عمدتاً بر تسلیحات نسل قدیم خود تکیه داشت؛ اما از آن زمان تاکنون، به سلاح‌های بسیار پیشرفته‌تری دست یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/468361" target="_blank">📅 13:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alqpCIuiJnmADLQwuaCspqe0oH1rm2WSMyVHvkKuoxzUsAcT1a3myW6k2DdDdf6cczSE0seIUP_rqKWt03ZxcjBPU7AYFh954bAUGGI6EUdF41Rt7cyl-GKuGFAJ6DhQ2Wt6x0b-k3bQkxvNSZCfPAjonqn-ORtMLBZDvWsaGx_ngFLuVCChnKzlmowiiIl2EYzg3sgKrrqYxlXd-7AumtwZ_9zda4bDqNsPTGjGvZqe7ZwbUOTwA7vjT6sH1K0MHqubgCI-hfSe-crQL0U4K8AIgMdbHPqX00PvFKf2jrzfsGSB2goRY_MBiSl8rjmdJRKWyk8Gup4aTfcD7QVHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت مامور پلیس مهرستان درپی حملۀ تروریستی
🔹
پلیس سیستان‌وبلوچستان: درپی حملهٔ تروریستی افراد مسلح به خودروی پلیس در مهرستان، گروهبان یکم محمدعلی شهریاری، به‌شهادت رسید.
🔹
مزدوران تروریست پس‌از این جنایت از صحنه متواری شدند که اقدامات لازم برای دستگیری عاملان…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/468360" target="_blank">📅 12:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468359">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
کشتی کانتینربر متخلف با ۲۵۰۰ کانتینر در جنوب تنگهٔ هرمز غرق شد
🔹
نیروی دریایی سپاه: یک کشتی کانتینربر متخلف که قصد عبور از مسیر غیرمجاز و پرخطر تنگهٔ هرمز را داشت با اصابت به یک مین دریایی منفجر و دچار آتش‌سوزی شدید شد.
🔹
این کشتی با بار بیش‌از ۲۵۰۰ کانتینر صبح امروز در آبهای جنوبی تنگهٔ هرمز از شدت آتش‌سوزی غرق شد.
🔹
شناورهای بومی و صیادان نهایت ایمنی در تردد از این مسیر را داشته تا با کانتینرهای شناور بر روی آب برخورد نکنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/468359" target="_blank">📅 12:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468358">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kc7zqnw_qr2axrtOi3FlAydbpt-bQAL_oaLFUquO3gFAcRjllimYo5xWxvqWujoPXl-z_jQNdT4MdN3tPBT9YW61i-ruDgWfWV9uDQVL0g6HiT1t3ZNxEAAOXX_wr8ad_FLUZh64EOsYT_zIJfW5B2NA925z3ry8ZdgSt2lvPNZLzHcC9bsOYrt-TgoAk_9S1OEBOIYPLaNWwRrObX_zxKxuOHbJfozW9puOxjqfly2qY-y_2QQM2ufm3wahT5wgdP-qvbBYbVQ0-WX0He-MqJD44pzSF5idNKLnRUkIv0Bcz4Ritg7BjrDsR6j3uUosuyag3GOpFFkalB_PKuFbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت مامور پلیس مهرستان درپی حملۀ تروریستی
🔹
پلیس سیستان‌وبلوچستان: درپی حملهٔ تروریستی افراد مسلح به خودروی پلیس در مهرستان، گروهبان یکم محمدعلی شهریاری، به‌شهادت رسید.
🔹
مزدوران تروریست پس‌از این جنایت از صحنه متواری شدند که اقدامات لازم برای دستگیری عاملان آن ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/468358" target="_blank">📅 12:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468357">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtmOaXOmAmuxKnRojj4ZsyjnjeuAQu8TNKt7FOCPScNBP2Dj3JPxVjjGwLaZayp9VEYhS7ik8ol48PbP0U4yW9_kezHkfNYz8o-FU4SGfy4p_x2OtWRSVwa-48-8GQyPjf3Bz2ztOGdKipeijFevvLEgfm-cYMaVMbpdwvr1O3WAHG-FvSSO4mFeQIDeHnJoVO9jQG8AthLH0oRvnqd7DMtTLzHJGRdF5pyHlVJKvXBnl58WwG2G_tbF7j5Tna3SyyL_FbfQpJ860-H865mgCXrLrYUOeJfbVuQbP9JljYW8X-Pvotz3iH4wo0QaaL0PgF1cEKPhlhVWEvQp9O4eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس هفته را نزولی تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۳۴ هزار واحدی به ۸ میلیون و ۴۲۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/468357" target="_blank">📅 12:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468356">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab6b0238e.mp4?token=stFa6iAYjuRZhrNj4-OuGnwwfreucQhT9OTvssYxkC9v_ok_SeATCDV0RIsdDk1_mGHTpWL1JE5OidagfyhxRBN0Wu4baBGTWxtdFVLLjZc6IWT0J8Nf2LiTT-fA2ZuBEygIVL1pm2dr4L_bwwuVn-vbXi9VeMtLbje9B9yifBA1S4yzMWtgmpausaXZvrrLQxI3QRoQ0oBRy9yybGP6-sncmYz_lmdZrz8_GRvHD0B3iHyUi99klFRPDwlKMbw-rOAVotwIzbwfSFfyg2Cu6zl-aYPE2hwpimmuV2r9PnlhWZMj9_uG2iqAOs3Cyv6LiB8hqI2FK01RgAeixXQ_9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab6b0238e.mp4?token=stFa6iAYjuRZhrNj4-OuGnwwfreucQhT9OTvssYxkC9v_ok_SeATCDV0RIsdDk1_mGHTpWL1JE5OidagfyhxRBN0Wu4baBGTWxtdFVLLjZc6IWT0J8Nf2LiTT-fA2ZuBEygIVL1pm2dr4L_bwwuVn-vbXi9VeMtLbje9B9yifBA1S4yzMWtgmpausaXZvrrLQxI3QRoQ0oBRy9yybGP6-sncmYz_lmdZrz8_GRvHD0B3iHyUi99klFRPDwlKMbw-rOAVotwIzbwfSFfyg2Cu6zl-aYPE2hwpimmuV2r9PnlhWZMj9_uG2iqAOs3Cyv6LiB8hqI2FK01RgAeixXQ_9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده انتظامی خراسان‌رضوی: طی عملیات‌هایی در استان،‌ ۲ تُن مواد مخدر کشف و ۷۰۰ خرده‌فروش و ۱۵۰۰ معتاد متجاهر دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/468356" target="_blank">📅 12:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468355">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru4EEr8zLaTK0TT8DtT2hEZeDmFtKnVJcNFhbgjSyJ_J-4TuOXY0NL0Ot6zONYS7RetUg3Y1JnM-ZY_QGU9qL74tscJhxWKQgfO_ZPnNk7Aumzx0vJJ81ptZ1Jonav_LdUjUiavm2VgYOUMCBSLQlBDTZjB9P9SL9XSZKw1C9IJ8wkhfTc-SNaqDwkAOaqS_sQSAIMlJUX0KtYmO1e6QLV5De4dqFzxNzKhQuPVQxUiAWRRB_qthnYM8_iLKP-F2HlT3kA7atv5iqvogC4iheRxou1lhfpIuWKh_HK_KacfTOSialATQSqjtOYQwEojmzx6hhQtxz1zHPWo31Z4luQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴.۸ میلیارد یورو ارز به چرخهٔ اقتصادی کشور برگشت
🔹
رئیس پلیس امنیت اقتصادی: تا دیروز با رسیدگی به حدود ۱۱۰۰ پرونده مربوط به تعهدات ارزی، بیش از ۴ میلیارد و ۸۰۰ میلیون یورو از این تعهدات ایفا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/468355" target="_blank">📅 12:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468354">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkujOupvLrU-q-jFU0NbC9WDm1Y8rv-SpV6dvnRL2QFWXdRuFu1XOqV-HhnyvSXUV778EQREsTbyQp0g-urPZFNCqX2m-CtfKj3TML2Kg4BPT-szJoOMdIamJogHzcPOM4apceGSj8f4MaiPDxNuTmck_lHNbC7J9Rpw9fPyzNpxsVTClmgbT_8thyQZKQ2DEidIEEoDMQXlTEGT--LZS6n-emiX5ZsnkCJ2nlDrZA0zRcqV0v3Wa8zwFY7oatodsN_MK6j7cNWqPRBtBvcH7pYDwHnQrr6Q3SfvZyfQyTmKt89F6pvEzK_OttZKk-QSWQR6ew55tDP0xEeUTo97SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک‌مرکزی برای شرکت در نشست سالانۀ صندوق بین‌المللی پول و بانک جهانی به تایلند رفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/468354" target="_blank">📅 12:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468353">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4QokXsuALfkUGaTzGS9nAJHZfDrngBiA5xsO1b8Qp4IFs9_I-ZoA1L2Uz4Mam5nqz5HERa_oRcxjpA2_5LPCcEhGb5UTJJKzrP8GjRlRUhDidLkRQbceU-wn_LMh1sTxbFGKZtqycaB98yrHGVe5rmeNEgv2TLBcuQRehRerHa3Khu60vHg4JiTliguSmi_QMV3fDdqz1bwT3K1kocxHC-_TX_FpmOi0GFM-no_4uHz_2AmcUkssX1AbkltLa6bKAQRvvAFWvBIrIYTJnb4voiOnlkIiYRNfqDHOp-7dh7iud-2dqokx5BBprXtTZ8DvEQO_IvhfvPRk_TAtk5iDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
فرماندهی صنعت نفت سعودی تعطیل شد
🔹
درپی حملهٔ موشکی شب گذشتهٔ یمن به آرامکو در الظهران و آسیب ۳ طبقهٔ فوقانی یکی‌از برج‌های آن، همهٔ برج‌های این مرکز فرماندهی نفت عربستان تخلیه و فعالیتش متوقف شد.
🔸
مجتمع الظهران، مرکز عملیات اصلی آرامکو و محل استقرار مرکز…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/468353" target="_blank">📅 12:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468352">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9582b95da.mp4?token=blaGiNR0j6g0yCaOyErWtk5ha5xyuYpCeUe9H7KLN5jvUMTFb8WWhLXMQNyms61Y2Ndw4PTrOp7lyFO0Nk1RJuCVfC7XysiDYFn4ifI5rFn3VihJlAsw4iMcswvuU0zmRYBp7xK3quyfTBhfv3tIVEDEjkmqADPkHjwlEHPfTR6yi4jybsEYEGEq0nH1p9WOI_vN3nD9Nw5iqu8WK3AqV3-cwGec8NNvQDcf4CYWyNm36E21lXyJw6UiwimBngiyw9XMU8384qYFXwo5AUMKcpYN1yW9KHicZ1oCqXk8-YbnxIC5S4wosv4ddg_Tq16jcJ1CnvGHaDB2HARWF4kkpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9582b95da.mp4?token=blaGiNR0j6g0yCaOyErWtk5ha5xyuYpCeUe9H7KLN5jvUMTFb8WWhLXMQNyms61Y2Ndw4PTrOp7lyFO0Nk1RJuCVfC7XysiDYFn4ifI5rFn3VihJlAsw4iMcswvuU0zmRYBp7xK3quyfTBhfv3tIVEDEjkmqADPkHjwlEHPfTR6yi4jybsEYEGEq0nH1p9WOI_vN3nD9Nw5iqu8WK3AqV3-cwGec8NNvQDcf4CYWyNm36E21lXyJw6UiwimBngiyw9XMU8384qYFXwo5AUMKcpYN1yW9KHicZ1oCqXk8-YbnxIC5S4wosv4ddg_Tq16jcJ1CnvGHaDB2HARWF4kkpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الکساندر دوگین در گفت‌وگو با فارس: انقلاب ایران تمدن اپستین را به‌چالش کشید
🔹
پروفسور الکساندر دوگین، فیلسوف و اندیشمند روس در مصاحبه با فارس دربارهٔ نقش تمدنی انقلاب اسلامی ایران گفت: انقلاب امام خمینی صرفاً یک موضوع داخلی نبود؛ جامعهٔ ایران قیامی علیه جهان مدرن و هژمونی غرب به‌پا کرد.
🔹
این را پیروان آیت‌الله خمینی به‌خوبی درک می‌کردند و دشمنان ایران هم آن را فهمیدند. اینجا نقش‌ها تقسیم‌شده بود؛ یک‌سو سپاه [حضرت] مهدی(عج) و سوی دیگر سپاه دجال. انقلاب اسلامی ایران با تمدن بعل، اپستین و دجال درافتاد و آن‌ها با سوءاستفاده از رسانه و هنر، تصویری کاریکاتوری و غیرواقعی از جامعهٔ ایران ساختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/468352" target="_blank">📅 12:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468351">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مبالغ جدید وام دانشجویی اعلام شد
وام تحصیلی
🔹
کارشناسی: ۷ میلیون تومان
🔹
کارشناسی ارشد و دکتری حرفه‌ای: ۱۰ میلیون تومان
🔹
دکتری تخصصی، دکتری مستقیم و دستیاری: ۱۵ میلیون تومان
🔸
برای متأهلین به ترتیب ۱۴ میلیون تومان، ۲۰ میلیون تومان و ۳۰ میلیون تومان است.
وام شهریه
🔹
کاردانی و کارشناسی: ۵ میلیون تومان
🔹
کارشناسی ارشد و دکتری حرفه‌ای: ۷ میلیون تومان
🔹
دکتری تخصصی ناپیوسته: ۱۰ میلیون تومان
وام ضروری
🔹
تولد فرزند و ازدواج: ۲۰ میلیون تومان
🔹
حادثه‌دیدگان، بیماری خاص، لوازم کمک‌آموزشی و بلایای طبیعی: ۱۵ میلیون تومان
🔹
وام عتبات عالیات ۵ میلیون تومان و با تشخیص رئیس صندوق ۲۰ میلیون تومان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/468351" target="_blank">📅 11:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468350">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFEMLcKLePvpqDOB3JOdM8yxYpxjY5F7CMlrjiwzzFf2g6OeU0ZttlgGsrVSrpQlqjZoxqcOFQZ7F-olhnaUXaH0GMNNHzR_oAgIxMg8V6Qb0yZqUxuouRpO6EPrVtMIYYy7LSft-6nqA6KQ3kAzjlzy8CEXzqkHcqbUT2Yszn8-ahWdaU2qN5yVxgB9uH3n5LN-YvDBHx22m8aF22QToJw8XHH0SOGmRk5WsCBXGaPiMon1UQQnM9Ap5oTpMSJyZMzI_6QYayeppsCmY7GAyBcMT5gFdx8walEGEVB8MCwwmsTzrAvqO4tGMiyawedbZfgAKPwLpax2Y98C_Yfkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ انتقام به‌هم‌خوردن آتش‌بس انرژی را از زلنسکی می‌گیرد؟
🔹
سیستم امنیتی اوکراین گزارش کرده که فعالیت استارلینک در اوکراین محدود شده و دولت اوکراین نگران است که این موضوع به‌درخواست ترامپ و پس‌از به‌هم‌خوردن آتش‌بس انرژی اعلام‌شده توسط ترامپ انجام شده باشد.…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/468350" target="_blank">📅 11:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468349">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجار مهمات عمل‌نکرده در سروستان
فارس
🔹
فرمانداری سروستان فارس: امروز به‌دلیل انهدام مهمات عمل‌نکرده در شهرستان، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/468349" target="_blank">📅 11:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468348">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
برخورد پهپاد با لنج صیادی در محدودهٔ بندر کلاهی
🔹
استانداری هرمزگان: یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدودهٔ بندر کلاهی برخورد کرد.
🔹
براساس اطلاعات اولیه، درپی این حادثه ۳ نفر مصدوم شده‌اند. مصدومان درحال انتقال به ساحل هستند. @Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/468348" target="_blank">📅 11:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468347">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d0e2ae3d.mp4?token=CWF7bgZXsb7ujg1WA94NHJ-XWTHqnZzxDSnqNTg_DdqZWSf8NBYGJB7EHkND-ts9OgyzYcaubt4jXTFY6qlMnTt1UgXC_wZ_8whuxKyIwa-k97xT26WiXbBdeyJL7gaQkKmD6AnhdZQ__wHVn7R_oyLQGlAVCZfe33gghVXlIY3p8f89YXD6qiJDTr4FYu_v3A0h4-PajvAtgmANbJVOwL3Z3mcPBIKl1si0vYfq3QJMrD3w4frG3_GKhUiSZXIsaf9uCn2t12SwQ6DuZcpyesxtLApwOa2WMFfw73pN50YkhwC-FYDMtV10L7N2YkdSj-BylHtiy1Yb0RuHSYnssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d0e2ae3d.mp4?token=CWF7bgZXsb7ujg1WA94NHJ-XWTHqnZzxDSnqNTg_DdqZWSf8NBYGJB7EHkND-ts9OgyzYcaubt4jXTFY6qlMnTt1UgXC_wZ_8whuxKyIwa-k97xT26WiXbBdeyJL7gaQkKmD6AnhdZQ__wHVn7R_oyLQGlAVCZfe33gghVXlIY3p8f89YXD6qiJDTr4FYu_v3A0h4-PajvAtgmANbJVOwL3Z3mcPBIKl1si0vYfq3QJMrD3w4frG3_GKhUiSZXIsaf9uCn2t12SwQ6DuZcpyesxtLApwOa2WMFfw73pN50YkhwC-FYDMtV10L7N2YkdSj-BylHtiy1Yb0RuHSYnssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر علی‌سینا مصطفوی، تروریست مسلح و عامل دشمن آمریکایی صهیونی در جریان جنگ رمضان که صبح امروز اعدام شد  @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/468347" target="_blank">📅 11:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468346">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8OCg3Goq2ftZqyA4uFrfYk8peEkc7ZCLzhKbW67LamAyCOJzeZeaPiS5HcvpDDrXxjZsCfLDW02ODtN1ZQUhSHbFn155EcVebasPiiCILBiHCsbt1kvnBq44WiyaekLIW4HjbO3NnrP_eWDweAW_ncs8dw6ACTUvhrxYyLXaVOHlq2O0RuTYwczJaXIK8lXPYy_dp88Zu0qid-ztVV18Vt4yEMac-1-h6RbW79pszSE2bZ-aQqXy8uKJmfJ6p98UGKPmFDOwCsT4QHZPGrops-B6ZwGvKZBMaAI3Lw6p3EAFaPce1eNjKMxsrh0oMQ6IwkvcthNozL4ZVq42XATdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوآوری مالی در سایه تنظیم‌گری؛ چگونه می‌توان میان توسعه و مدیریت ریسک تعادل ایجاد کرد؟
گسترش فناوری‌های مالی در سال‌های اخیر، شیوه دسترسی مردم به خدمات مالی و مدیریت دارایی را تغییر داده است. از خدمات بانکداری دیجیتال، تا پلتفرم‌های جدید سرمایه‌گذاری و خریدوفروش دارایی، نوآوری‌های مالی توانسته‌اند دسترسی به خدمات را آسان‌تر و راهکارهای تازه‌ای برای پاسخگویی به نیازهای کاربران ایجاد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/468346" target="_blank">📅 11:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468345">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📌
حضور  نماینده ایران در مسابقه جهانی ژیمناستیک هلند با حمایت بیمه دی
🔹
هومن جعفری، تنها نماینده ایران
در مسابقات جهانی ژیمناستیک ۲۰۲۶ در  روتردام هلند   با حمایت بیمه دی  به این مسابقات که در هفته جاری برگزار می شود اعزام می شود .
🏆
بیمه دی حامی قهرمانان کشور</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/468345" target="_blank">📅 11:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468344">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/468344" target="_blank">📅 11:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468342">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9ad5053.mp4?token=DyKMUezSWmqzH_i1pb91EHEMU-CYBrlIE8jHsQphzXYRERF23lE2LNtWGiHpzHYf0DkdJ5Pi7bbaDCAM5CAR-whCiQQ6FExvuQp_rq-Lsl0pr1s7yUrtsIjLMcuI1KJt_sN9_NYPOpdaLGzZQyv1SiJcv0OQHDhlQ95LKlqCEKe_YOjwvZNg0xHhsw4jchuXdRkbiafqHp-WtHIaOaFjx81PdqiuZZgvk2ASCf58rIiS22F9Nv01cAGn1BxIJeCZDolpoO_lHfBsbLTAgC38A7S9p-9icdXTrpepGtPa4mIi8RWhu8DRQFPS76N53HoZvXTROyAGFPIGOtyh01UvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9ad5053.mp4?token=DyKMUezSWmqzH_i1pb91EHEMU-CYBrlIE8jHsQphzXYRERF23lE2LNtWGiHpzHYf0DkdJ5Pi7bbaDCAM5CAR-whCiQQ6FExvuQp_rq-Lsl0pr1s7yUrtsIjLMcuI1KJt_sN9_NYPOpdaLGzZQyv1SiJcv0OQHDhlQ95LKlqCEKe_YOjwvZNg0xHhsw4jchuXdRkbiafqHp-WtHIaOaFjx81PdqiuZZgvk2ASCf58rIiS22F9Nv01cAGn1BxIJeCZDolpoO_lHfBsbLTAgC38A7S9p-9icdXTrpepGtPa4mIi8RWhu8DRQFPS76N53HoZvXTROyAGFPIGOtyh01UvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخورد پهپاد با لنج صیادی در محدودهٔ بندر کلاهی
🔹
استانداری هرمزگان: یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدودهٔ بندر کلاهی برخورد کرد.
🔹
براساس اطلاعات اولیه، درپی این حادثه ۳ نفر مصدوم شده‌اند. مصدومان درحال انتقال به ساحل هستند.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/468342" target="_blank">📅 10:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468341">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqsmsd9YCaRDq3r0oBeRUQy3bUa9s6oug-wqUScKg5IbENcHDyG5cdjtiFqO8oamtfjFadSIoGJ8CgeA5ll_KYPL7A49eNZ-BCivEmaoDawdb1g5rvMykBa6JwzAvZzdX4s84IEBfDoVDs3PlcL6fvKyGJYbGoAixDtwcrch_Iu0riU21IvcnTloPrjgXoEM1ED8XYhgecGQMyPObHr9AskwUOTsJ6tCNiOm0z_URxMgMMJhHJEkbTADXblygQCzMr9Pi_jrohmEW03_ff5eSGc3Ym67388BtTYh55eHRSx9Y7z4UvfDI24_nVg0SETeIwUfhTB-FRbdOYfR57M_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: پوتین حرف‌های ترامپ را نمی‌خواند
🔹
رئیس‌جمهور اوکراین: روسیه بلافاصله پس‌از اعلام طرح آتش‌بس انرژی توسط ترامپ به تاسیسات انرژی ما حمله کرد؛ مشخص است که پوتین حرف‌های ترامپ را نمی‌خواند. @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/468341" target="_blank">📅 10:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468340">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d875783812.mp4?token=so1cFVzMmqFb576AvFq3VT9S3RulIPxfeIoFDzGZ1Ey8rjCD9cBedyYqlOhVzm3YF3OWHxscuCd3kXvG2Ax4hVlX1h22dHBIUHIsTcrWWpbuIisxs8BDHXuouCfjLR23_NR8z8OAwI3vCKeZgWbRwsOFgcwjWG-hL36NSh-UH1qrgfMA2hXQpSAb7z3l8XWipvYy0bgh5NxII1EWYO005SVPajadBjNC7n07qDVly184krHKyBWzmYJeeOn87c056RP2ye7l9vwN9cgjImvzHIgQXul5jMGiGkiYLofXYpMWlY4i7XHphhDPQ3MIi7nkYg-qGPot3jd7-iVlYbgptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d875783812.mp4?token=so1cFVzMmqFb576AvFq3VT9S3RulIPxfeIoFDzGZ1Ey8rjCD9cBedyYqlOhVzm3YF3OWHxscuCd3kXvG2Ax4hVlX1h22dHBIUHIsTcrWWpbuIisxs8BDHXuouCfjLR23_NR8z8OAwI3vCKeZgWbRwsOFgcwjWG-hL36NSh-UH1qrgfMA2hXQpSAb7z3l8XWipvYy0bgh5NxII1EWYO005SVPajadBjNC7n07qDVly184krHKyBWzmYJeeOn87c056RP2ye7l9vwN9cgjImvzHIgQXul5jMGiGkiYLofXYpMWlY4i7XHphhDPQ3MIi7nkYg-qGPot3jd7-iVlYbgptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید جلیلی: سایۀ جنگ باید از سر کشور برداشته شود
🔹
آنچه باید در برنامۀ کشور قرار بگیرد، این است که نه‌تنها به جنگ پایان داده شود، بلکه سایۀ جنگ نیز از سر کشور برداشته شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/468340" target="_blank">📅 10:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468339">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu2mffYdl5douxRTvj3aPGrc4dOpAg0PtQUIRcxT9ARcKae-rMkLA56NIDIDx8R_mOLpMtodj7FgmRIRXVCA7Znjl9Zas_l9tfe94mNdo7T8m4iVEgaBuKGMlqsMB_tBO8m51BxVyVhLCHnZgj1L3o_lu0EsFHG2xgDx-MNmdbHgnJJcYbkoX78y2jhqLVTCUqyvZHoE2UI7G9eE1tA4aNGdPU0rAaDSaorZxkR_s7aZUeu6Y5RYIpnBjbY1Bzpb7hegxhvPDepcVdGY4eiLu6OJOfsXVyJ1ZzY0JUP6PSjvH4bVZq6b_j1RN3PrlU6-zuGPjnMaFOn_7rbxqpqUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
اقلام کشف‌شده از علی‌سینا مصطفوی تروریست مسلح و عامل دشمن در جریان جنگ رمضان که امروز اعدام شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/468339" target="_blank">📅 10:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468336">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDcr7-rrX5WLuhcPAzSCDzLCAPLpypjIVXbjKf-LTeH_d1QybO27ATLHx00-c6xCSYru4JyZCPvnp2hTknLC0cTcK69TlBujJlYxX_TlxTckO0q6nCd5ej-d3w37v7W8c8q-Rp11qz9B_hjtuWrYpNZM5yueryflhGtkuoYsx_ul_qK1_YGjGuJFLE0cvaaWx8nQpT47oWvGkMXxeFy6zo2_FSSJaG4ig_1dXVLrV0w8QsixtWWIM5cGB-qjQH95NNbsoz_RrEg0kH11rozDIMNERF4LVNK94AKNq9OszsBaCsiiga7qrlPTqlupnXRxGE12oDA6xsjq57ZT-QV1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HO3joU2LzvD4PXCtrBNFq5qooGuxe0VpQpmq0aVzw1Ep-epDm4AvU26FjXyy2WjcyZDSIBsZI7NpTssHpY9N6qaKaQez11wizLf4NvUbqKZD8zRJUQoFbjCFx07rMV5LnNmcK5k5ITgMXZArot4_F9bq4EpSxsqAGeTEIpHVmfh2_AeVzJgGMb_YeuX4pivw7HLe5N0Ifh1Z8pC1kv0jOog2fF2qh1UbkkPMVbQllffO6VVemIrPxIqn94iS6gIb65rgMLJ6A7QLNnwBAUVmRwGQ2_WgGxctdaHKaGfZjsWszPAzBYjr_-ZzJXjp8avguEZuv9PG1dJExklaBctYbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNG0qUeAuCeb_SYLBuy02QsaYNsnW6lgnrjm8Eif7eMb4VA1TxYKhVH93jNR5PVJo1h6bccQGAXIun1fx7sSyTDqFYMC9eG9ATGJMctXNXUWjRDcs-ttu6YsDAyadafoLdUT-b1oUGhf1Ql3ZEsbNjsBopzoRl0S-mOGuszNpG9OmWKc5oCtXRpSwEwcIo8mAZ1i-1_kBY7tDAG3dWynDL2wV3sWDMT0dIQGZrZ3X89rl0ElIqxC7jmtDTZ81HJlOFCNMw8MsqfU2B5cdkq20OfNnvjP-mV2v_BLv13S4wU4IPTZFLficSIRRjdDXrPkI6cF50PZ1gvu6Irhddi2ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعدام تروریست مسلح در کرمان
🔹
حکم اعدام علی‌سینا مصطفوی، تروریست مسلح و عامل دشمن آمریکایی صهیونی در جریان جنگ رمضان، که منجر به مجروحیت تعدادی از شهروندان و یک دختر خردسال شده بود، به دار مجازات آویخته شد.
🔹
علی‌سینا مصطفوی فرزند غلامحسین، از عناصر مسلح…</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/468336" target="_blank">📅 10:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468335">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jt9VMFGDjJw7iKqWt5NlA3MvEL2PMQXAibl9ihQDGQNFH683V57YQ4Lns7Nu_tY8UOrkMv5rvs84xw0g08yST3tjzCYzKTFjI3EwD9ljNyZynK6krswISTdE9O86SZztmSPvT6UMKh0OcZ-eHwQ8KqRJnqzr4UmVImAt3Rj1OmovSHLfKgx_FobZFDNecdm4wBO-ECi0DJj6ie2Wc1Vh7_Rbm12RYwSu55CObbnQfiuWEJhfsyKwkFLLpZan420o2lbWqxECYfCfJbMLrUthDL-rJlz9vrqZV-zWtKim8dShmieA0QLH7jfzDbLfh716MUM2edkaDXfB_DxMUXaAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات اسرائیل زیر سایۀ افشاگری‌های حنظله
🔹
گروه هکری حنظله در پیامی با اشاره به باقی‌ماندن ۱۳ روز تا انتخابات رژیم صهیونیستی، از آغاز مرحلۀ جدید فعالیت‌های خود با محوریت انتشار اطلاعات و افشاگری دربارۀ مقامات و شبکه‌های صهیونیستی خبر داد.
🔹
حنظله در این پیام، انتخابات اسرائیل را «روز بزرگ دروغ دموکراسی» خواند و اعلام کرد که از این پس، فعالیت‌های این گروه با تمرکز بر انتخابات و انتشار اطلاعات مربوط به مقامات و ساختارهای رژیم صهیونیستی ادامه خواهد یافت.
🔹
حنظله از آغاز «کابوس شبانه مقامات صهیونیستی» سخن گفت و تأکید کرد که فعالیت‌هایش از محافل سیاسی تل‌آویو تا دیگر مراکز مرتبط با مقامات این رژیم را هدف قرار خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/468335" target="_blank">📅 09:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468334">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c56adea1.mp4?token=iA0dgdolEC3M6xBiuH-NrU1aFz2Ad2VukpZGWenChr8Mjob7TeA784csNhVtOPi5-hll5bMkCsJ-a7RIwvM_F7IEoWha4psZX8yG_-nOgzlPvAkRlqm-Pfhe_DOZIaiP2q1Qyq-YtEH6cUaoLfcf9oVudVSge_pMcywbctw4s4ZUZ1OoSq18xNjFImkZEXJYKpyeXgcP9v_3AL5HEBfy12R4JYmQLUxqt6IyqTde1IUcVq_5s6OZxoC9oKlD4_IvM8rAXKmuPrArk6c3IVc97o53vJb-uk100DDhMkb0H4Ek42eR-yTlVcO0qYMipoJiYge-Ep_eXBUlmeXDdZZnjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c56adea1.mp4?token=iA0dgdolEC3M6xBiuH-NrU1aFz2Ad2VukpZGWenChr8Mjob7TeA784csNhVtOPi5-hll5bMkCsJ-a7RIwvM_F7IEoWha4psZX8yG_-nOgzlPvAkRlqm-Pfhe_DOZIaiP2q1Qyq-YtEH6cUaoLfcf9oVudVSge_pMcywbctw4s4ZUZ1OoSq18xNjFImkZEXJYKpyeXgcP9v_3AL5HEBfy12R4JYmQLUxqt6IyqTde1IUcVq_5s6OZxoC9oKlD4_IvM8rAXKmuPrArk6c3IVc97o53vJb-uk100DDhMkb0H4Ek42eR-yTlVcO0qYMipoJiYge-Ep_eXBUlmeXDdZZnjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس مسائل راهبردی: تنگۀ هرمز هیچ‌وقت از اهمیت ساقط نخواهد شد
🔹
بهروزی: رئیس‌جمهور آمریکا شفاف دروغ می‌گوید. جنگ با ایران برای آمریکا خطای محاسباتی بوده.
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/468334" target="_blank">📅 09:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468333">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شایعهٔ حکم شلاق برای کارکنان پتروپارس هویزه کذب است
🔹
دادستان عمومی هویزهٔ خوزستان: اخبار منتشرشده در فضای مجازی پیرامون اجرای حکم شلاق برای تعدادی از کارکنان شرکت پتروپارس کذب است؛ با نشردهندگان شایعات برخورد قانونی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/468333" target="_blank">📅 09:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468332">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2116816ec6.mp4?token=uFIlQ7QTW7KLnSThiDxSoyR86zJC3cGxMVFPfMV010hhM7-5Mdg4HST8aJJCWFABaG1PLqnr7zOzoTb74oA3LRdSdDalhS-cgp5unrh6WxqTa-mQOXEN2ut9QoqCeprRnYgoLtFnICSkomcxXmApnSVKLJXJTYqMHeqs8JvM44FJiKG2vN-eCJjDym0OV9OPbjXe4evWHMMUOd9m2-JIV2ykLopt-J_Jt8uoEf8bpFjOFb4X1_o3QMoYn2VjxLJwkwWTrYSW21KPPbLFZSQS7tu9szfYGm9WE2aR04xxaqymYe1TDW0QeaZ7YS3tUb0JVm1X4vLaazNDUkjtd4dBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2116816ec6.mp4?token=uFIlQ7QTW7KLnSThiDxSoyR86zJC3cGxMVFPfMV010hhM7-5Mdg4HST8aJJCWFABaG1PLqnr7zOzoTb74oA3LRdSdDalhS-cgp5unrh6WxqTa-mQOXEN2ut9QoqCeprRnYgoLtFnICSkomcxXmApnSVKLJXJTYqMHeqs8JvM44FJiKG2vN-eCJjDym0OV9OPbjXe4evWHMMUOd9m2-JIV2ykLopt-J_Jt8uoEf8bpFjOFb4X1_o3QMoYn2VjxLJwkwWTrYSW21KPPbLFZSQS7tu9szfYGm9WE2aR04xxaqymYe1TDW0QeaZ7YS3tUb0JVm1X4vLaazNDUkjtd4dBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  انفجار در نزدیکی مقر آرامکو در شرق عربستان
🔹
خبرگزاری رویترز: صدای انفجار در نزدیکی مقر شرکت آرامکو در منطقۀ الظهران شنیده شده است.
🔸
سازمان دفاع مدنی عربستان ساعتی پیش با اشاره به حملات به الظهران در شرق عربستان، مدعی شد که موشک یمن را رهگیری کرده است.…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/468332" target="_blank">📅 09:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468331">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رئیس بانک‌مرکزی برای شرکت در نشست سالانۀ صندوق بین‌المللی پول و بانک جهانی به تایلند رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/468331" target="_blank">📅 08:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468330">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvojmh1A54k8dXhnd_MI7cZ1Hd2LIhLsYM3yp6IRdPLAr79_OUFiZvfS94U-HJ5MbDDLz7HKtUxAJY_MvSQsyHA4qMVY24RK1nr2iY1d-NRCu7magWiQhLtlIKg8kgdc7l1fojPYIfjor6FRaRgW0p03UlrwtVdT1Y1zjQn24QfxyKzUYShIIK9PbG7nMHVBjhVS4gJMl6RZw-VqILVjGl0_J85FmiQl9pxVESXvxO7WbeMKRRz9LuaqIAtUJnl3gb41znYP7RBI1a31hFxrm6ZiAGTywabMSnbiHjXOfiscO8L6FGlgWVjUvFuB7JSMGZFjVpea5Dnmuy44RkmHsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  وزیر پیشنهادی دفاع: تقویت پدافند هوایی را با جدیت دنبال می‌کنیم
🔹
مهرداد اخلاقی در نشست ویژه مجلس: اولویت‌هایم برای اداره وزارت دفاع در برنامه پیشنهادی ۱۶ مورد است که یکی از آنها باز معماری و بازآفرینی وزارت دفاع آینده است.
🔹
باید تلاش کنیم که از داشته‌ها…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/468330" target="_blank">📅 08:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468329">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076a0df338.mp4?token=U8SEkhCNvYQunJ-ko-_AscjLxciohcEwdnJR3RM9Nf43bUBSKsNRg_5r0nXf-UbDT051kBpBXCn7loLxpDJS3zdKMCjhtBfeHIO_CV7K4rHCyBY-B8b2Y_qS9igKDo_eE9BclMYJh9H22OH5s6weCr63Jx2_AiFvGMgTBoFk39oyZJ445G2HS-WSwMpITETjNyk1U-Dg8mWVvgzhOZe_A2KQD1AlcAESDFDGa-zfu1_MT1ZP6G39ZLfzf8bc_CdM92nDiMI0LWaRc0OWgpbV1fnRro-GSEezBuj05Jm8-Ym5lolCdRMjHUGw2H4inwyqgHxcXzu0p2ilvNlMyvb3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076a0df338.mp4?token=U8SEkhCNvYQunJ-ko-_AscjLxciohcEwdnJR3RM9Nf43bUBSKsNRg_5r0nXf-UbDT051kBpBXCn7loLxpDJS3zdKMCjhtBfeHIO_CV7K4rHCyBY-B8b2Y_qS9igKDo_eE9BclMYJh9H22OH5s6weCr63Jx2_AiFvGMgTBoFk39oyZJ445G2HS-WSwMpITETjNyk1U-Dg8mWVvgzhOZe_A2KQD1AlcAESDFDGa-zfu1_MT1ZP6G39ZLfzf8bc_CdM92nDiMI0LWaRc0OWgpbV1fnRro-GSEezBuj05Jm8-Ym5lolCdRMjHUGw2H4inwyqgHxcXzu0p2ilvNlMyvb3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رخ‌نمایی دریای کاسپین در نقشۀ ایران
🔹
هواشناسی: امروز و فردا در برخی نقاط کشور باران می‌بارد. جمعه و شنبه از مقدار بارش‌ها کاسته می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/468329" target="_blank">📅 08:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468328">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اعدام تروریست مسلح در کرمان
🔹
حکم اعدام علی‌سینا مصطفوی، تروریست مسلح و عامل دشمن آمریکایی صهیونی در جریان جنگ رمضان، که منجر به مجروحیت تعدادی از شهروندان و یک دختر خردسال شده بود، به دار مجازات آویخته شد.
🔹
علی‌سینا مصطفوی فرزند غلامحسین، از عناصر مسلح دشمن آمریکایی صهیونیستی وابسته به جریان منفور سلطنت‌طلبی در جریان جنگ رمضان بود که همزمان با تجاوز دشمن به کشور، اقدام به عملیات مسلحانه در کرمان کرده بود.
🔹
براساس مستندات موجود در پرونده، نامبرده در چند مرحله اقدام به اجرای عملیات تروریستی مسلحانه در کرمان کرده بود.
🔹
مرتبه اول در چهارم فروردین ۱۴۰۵ اقدام به تیراندازی در میدان آزادی کرد که در این حادثه یک شهروند و یک دختربچه مجروح شدند.
🔹
محکوم‌علیه در اقدام بعدی خود نیز در تاریخ اول اردیبهشت‌ اقدام به تیراندازی به سمت سربازان وظیفه و خودروهای عبوری کرده بود که منجر به زخمی‌شدن تعدادی از شهروندان شد.
🔹
نامبرده در جریان کودتای دی‌ نیز فعال بوده و اقدام به ارسال فیلم و تصاویر برای شبکه‌های معاند کرده بود.
🔹
او در جریان جنگ رمضان نیز از محل‌های اصابت پرتابه‌های دشمن تصویربرداری کرده و برای شبکه‌های ضدایرانی ارسال کرده بود.
🔸
در مستندات کشف‌شده از تلفن همراه محکوم‌علیه، او در پیام‌هایی که برای شبکه‌های فارسی‌زبان ارسال کرده بود، اعلام آمادگی برای انجام عملیات تروریستی در فرودگاه کرمان کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/468328" target="_blank">📅 08:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468326">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adaaee1a17.mp4?token=Gnz7grgxGt1ArIh68O5b4W8taGoSX4z7MdeN_bKS9bTgi5cGr6FW9lJGUuLImWZ1NnZp1qwwcAApKMFgi-Y-VhDLYNQ_yyf-mAFuuR9JpYJjo6WelbAbl9kLA5EhdYtkho6JFlH9m-yJmi92TcrEC9yG5t9I0efNy0skNgBb45JGnLD3y2bmdHVtByNqd30toRQvQl0WbvWZdnsN6d9LqFoe6LlpIs3RRtbxGyUhc51C0Us7ZCSSpLpexh2xofOSi4mxz8cDft4v0erjBxVDrfRXc7Qv57LgmULQOwr7GmZB7Rbo5diTlXHOaMWg5nWxJyBQh_3_U2orOGJmkVZykw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adaaee1a17.mp4?token=Gnz7grgxGt1ArIh68O5b4W8taGoSX4z7MdeN_bKS9bTgi5cGr6FW9lJGUuLImWZ1NnZp1qwwcAApKMFgi-Y-VhDLYNQ_yyf-mAFuuR9JpYJjo6WelbAbl9kLA5EhdYtkho6JFlH9m-yJmi92TcrEC9yG5t9I0efNy0skNgBb45JGnLD3y2bmdHVtByNqd30toRQvQl0WbvWZdnsN6d9LqFoe6LlpIs3RRtbxGyUhc51C0Us7ZCSSpLpexh2xofOSi4mxz8cDft4v0erjBxVDrfRXc7Qv57LgmULQOwr7GmZB7Rbo5diTlXHOaMWg5nWxJyBQh_3_U2orOGJmkVZykw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اولین طلای کاروان ایران برای ابوالفضل مهمدی
🔹
در رقابت‌های امیدهای جهان، ابوالفضل مهمدی در دیدار فینال با نتیجهٔ ۲ بر ۱ مقابل حریف ارمنستانی به پیروزی رسید و با کسب عنوان قهرمانی، نخستین مدال طلای کاروان ایران را به ارمغان آورد.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/468326" target="_blank">📅 07:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468325">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حملات روسیه به نیروگاه‌های برق اوکراین
🔹
به گزارش منابع محلی، نیروگاه برق شهر «خارکیف» و نیروگاه ترکیبی منطقهٔ «کی‌یف» هدف قرار گرفته و خاموشی گسترده‌ای در شرق پایتخت اوکراین رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/468325" target="_blank">📅 07:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468324">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuiS8vojKSAI6mZhisqgxWDJ-XafgGrzWL86vd4NeXQnZt3HbBk8JIl31cMhvnKO4Zb_KzgO1GVkyUMVke79e-zUIjYibEkqSsdu9olfRfQPk0wosF-lgMa9xCBgddrholuoTm6xgmB30j-jo4otaQe7SfX9Yx5QgZ28-gxxu2uAuKUvfIu6izsRauFBPxs1s8h9ZhB-SMEZBYv8KKoXmZoFjajwgPVTjglqzLjHsC83_UHScjpvLRO_MQR8vWFHAzzVt7Hn_Uaqb1vLMoc7OUcmlLmEY_BXzGvUGFkJzw-o4D4ZhyE6SQD58CdS25HKD-RCKNob1oqt2E70pDJtJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین تا قبل از ۲۰۳۰ عضو اتحادیهٔ اروپا نمی‌شود
🔹
یک دیپلمات اروپایی اعلام کرد اتحادیهٔ اروپا برنامه‌ای برای تسریع روند عضویت اوکراین در این سازمان پیش از سال ۲۰۳۰ میلادی ندارد.
🔹
او در تشریح این خبر گفت، فکر نمی‌کنم هیچ برنامهٔ کلانی برای تسریع روند الحاق اوکراین به اتحادیهٔ اروپا وجود داشته باشد. مذاکرات درحال انجام است، اما من باور ندارم که اوکراین قبل از سال ۲۰۳۰ عضو اتحادیه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/468324" target="_blank">📅 07:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468323">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌کمالی اولین مدال فرنگی را در آمریکا دشت کرد
🔹
محمد کمالی، نمایندهٔ ۶۷ کیلوگرم کشتی فرنگی کشورمان در رقابت‌های امیدهای جهان، با پیروزی ۶ بر صفر مقابل حریف ارمنستانی صاحب مدال برنز شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/468323" target="_blank">📅 06:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468322">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqpsT72XXiVqUKnAXiY-N7Fop83Ugrv3QzgfjEX94XjbAb3_aliDisqPp5549gykZMwKhrg1PjHfPa0y0mqThvuOMSHlvdx6gSXpkvwn18UCnAWdcCKx781VJQUIYWWEYUI2pzrllHysMzp7yGiCiuFYMRt4CTBr7Bf7QrwLa83IWG079F9TGdyC_hxKl7JzbBZhD38CaqA0ok8DSpSxXdIpmrhgf2VIi3DiLLcGJNLieVYSWnDAjDhGwrVwrJwI2-SHQ8bBYavc6UFIK9tL8Q8sBeKLkMAwxlVqZLw5wSNyn6wou294PtdH0HJm26beBC-Kc2U0yB7qZanCHs8hcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت روش جدید شناخت پردرآمدها را تصویب کرد
🔹
هیئت وزیران در مصوبه‌ای با عنوان «شیوه‌نامه شناسایی و گروه‌بندی اقتصادی خانوارها»، سازوکار شناسایی وضعیت اقتصادی خانوارهای ایرانی را تعیین کرد.
🔹
براساس این مصوبه اطلاعاتی مانند درآمد، املاک، خودرو، دارایی‌های بورسی،…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/468322" target="_blank">📅 06:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468321">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vinqL99oJsajL4w8wNrg0zmv5tDViMrjCeuljK1i5HVEFTDW6UNALC7oYOWXmlLhQWC59fWljJMHsB7zm0QChlhpTkbqokiDzVoRN_ABDDRdF_9541VmqUqE4qi2MdsA41KtsKg6gekG5wqgy4rNixIJmDRH6ZsLSMzqVUkX-UASk0945PUqGoV4Y6TcNvRHX9Vi3eiijFPg10Nh3vSwp6JBpKQN6_4skkNIIRZqUxykPfxmrM6MM-BOqtDCV9SeH16Ei9GYL3Lei9BFUfPZaURI8P3uZfHJ_JpbWvrHjRFvh38X0vn5by6Ds5ImIg4H6nwcWzBJ-scLL4pdnYMm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رقابت ۲ ملی‌پوش کشتی فرنگی ایران برای طلای جهان
🔹
در مسابقات کشتی فرنگی ۵ وزن دوم امیدهای جهان در لاس‌وگاس، عرفان جرکنی و یاسین یزدی راهی فینال شدند.
🔹
جرکنی با برتری ۵ بر یک مقابل حریف ترکیه‌ای به فینال راه یافت. یزدی نیز با شکست ۳ بر یک لوساک از نروژ راهی…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/468321" target="_blank">📅 05:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468320">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رقابت ۲ ملی‌پوش کشتی فرنگی ایران برای طلای جهان
🔹
در مسابقات کشتی فرنگی ۵ وزن دوم امیدهای جهان در لاس‌وگاس، عرفان جرکنی و یاسین یزدی راهی فینال شدند.
🔹
جرکنی با برتری ۵ بر یک مقابل حریف ترکیه‌ای به فینال راه یافت. یزدی نیز با شکست ۳ بر یک لوساک از نروژ راهی فینال شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/468320" target="_blank">📅 05:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468319">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گفت‌وگوی ملی فلسطین در قاهره برگزار می‌شود
🔹
الجزیره به نقل از منابع فلسطینی گزارش داد که گفت‌وگوی ملی فلسطین با مشارکت گروه‌های فتح، حماس، جهاد اسلامی و جبههٔ مردمی برای آزادی فلسطین آغاز خواهد شد.
🔹
جلسات قاهره تا پنجشنبه ادامه خواهد داشت و درمورد پایان‌دادن به تفرقه و بازگرداندن وحدت فلسطین بحث خواهد شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/468319" target="_blank">📅 04:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468318">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUfTRe6LOaie8KTZGNawXDyDXB5Kx5HUNCIC4FKEE-tVkCeNMQFXNyC668nsD141ujE-6jh1jNwU6hpCngnxN2xKemoYYv08MqanrXniYSTfm_MdNwhsvtHZVamDH8JSoCmnDshuUjU9LPX3-YzjP-M1xX4YV-KCVsKOczCGw4aJMLGcWs0ZBvKiWRg64MQOACyzsacSlAsa7TACH61sHn3DLR4v18HUDOenUoNz_z1264XsozZNQsOAxcg11u7SIHbOa2WAyNZgTvrdNZJbC0twF7Jg7UzucWokjOjDJXDkS_eJ8-uBT9PlvYwXFdgC11E5xf0WlJYb1ALzYcWeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف فرماندهٔ پیشین سنتکام به قدرت پهپادی ایران
🔹
دیوید پترائوس رئیس پیشین سازمان سیا که فرماندهی سنتکام را نیز در کارنامه دارد، گفت: اوکراین روزانه از ۱۰ هزار پهپاد استفاده می‌کند. فکر نمی‌کنم ایرانی‌ها این تعداد پهپاد استفاده کرده باشند؛ با این‌حال همین میزان استفاده از پهپادهای ایرانی نیز به‌اندازهٔ کافی مشکل‌ساز بوده است.
🔹
او پیشتر نیز گفته بود که پایگاه‌های آمریکا در منطقه در پی حملات تلافی‌جویانهٔ موشکی-پهپادی ایران، بی‌استفاده شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/468318" target="_blank">📅 03:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468317">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ2pwBtx3YGVsj22u_qmTgPJ3GSZqQxL_V602CaPlHtdGpw6T8y9h0C5bfxNpY4XTVCSfmNNLjjRhfVu0uqs3wn1dXAKLEiRk-wSdswfpRSnaBqX6ohtbP1seDiBC7fvHkVAuJNNcEwtDjDrQs35opfUmokpERvVe4JazX-TmXOUuFIaiofRft7aM1jVPteMr-XVwU5_IFQVyWeNSA4Qestrqx5Nw5Wa9uCdwF3U4xWNmJ6v9rlMi0eLfhJ2HZ81fcuwZuAP49nK-Toz22prbwvutJmpfKwzcUtJGecgD3pVOSPhhV52089N3sHDwZx4qBjP9KARNe2sk20rhWTX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتیکان: پاپ به سرطان ریه مبتلا است
🔹
واتیکان اعلام کرد که بعد از عمل جراحی برای برداشتن لوب تحتانی ریه راست، مشخص شد که پاپ «لئو چهاردهم» به سرطان ریه مبتلا است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/468317" target="_blank">📅 03:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468314">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP4LwaMXK752EYVh4qlum5xymqthPcESboF1Tx84KPJUx7DXnmfunPYJ0HWP9y2mR7txNYpIPfUAj62BVQRr1dNOqSYNF0aYS9TOTOv2zKrroBUduVdtS6zjhnt-5oLxhB1Q8QgxOjRsG5qhk-jhkV2_67adV-KSXMXgX_hH8neQV_foRSJTpy5FEcNBAMHQLL59BSNunvMr7B2VnVWd7uTzeGpMwjSQbl8ZNP-71n4mJUh5q3h6CJcrQmbJpraZbVBc5LudbfCb3u_Kz6n6MQIOlJZ47C28XXxmAPa2rS8BIvGwKbTwB5Awo6r3xerqd8pF5N85sW3rHY_mMSqMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکسی‌های اینترنتی حق دریافت عوارض شهری از مسافران را ندارند
🔹
با تصویب لایحهٔ دریافت عوارض شهری از شرکت‌های تاکسی اینترنتی، رئیس کمیسیون حمل‌ونقل شورای شهر تهران اعلام کرد شهرداری مجاز است به‌ازای هر سفر انجام‌شده یک درصد مجموع هزینهٔ سفر را دریافت کند.
🔹
براساس مصوبه، پرداخت این عوارض برعهدهٔ شرکت‌ها است و دریافت این هزینه از مسافران مجاز نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/468314" target="_blank">📅 02:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ots7hXgBNIp9hr6mwoayGWWoxmuNrDZ0Ef3Adv84cltAWEsEO8-Bp8SvA3YMfZ-TDhxjQofRu2rZX9mRE9maby3NQthPa4AMabQefR3PRFtL5UDdlf-mFM-RgoBemwi-dZAMbzDssyWxIdZhLW9C_37CpRez3hVgv_vP7UeO4YMWVQz8hHKiuGSis4Jda0I10gMN47LZgcXCYyZruJJP63wXwRsZ56-lN8MOvRxO0r19yoND5WaVJMVgGpBOTHfmGMDu38JkNgf0lY70v24p6Zv3hYBsB-0wEgX3XsuNBGYt5cUqttium480HM-6Uk5zqU1ptyl9oEtsyOcY4bl9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qW04Fr8_PvnYMRNItPF-2RPhhSdyUMXN79DeDkb73iLt7B8P-4lN0KmbJsRYHb92rZe9FjtRb30oTV3keLoyPUB_jdLZg2uFf5IOcdIvbZaRtVSKUITwtNxS1B2lc2TRg8wLTcLUU0kWmQe4EKLV0hAwKT2LEcBM1qt0JNub7uGvIgjdqhI5ak1nwp_jOmQrJwQxq1zMaEkAnfjD5RIk44y0JM3cvDS5bvqTZwYtCSFOcH1QwJh1M83KGxn-AuzxDL6SB01TsfN1sY80rOpoO_Wfs87fKbU3WZFvVO-XyvymD4S083NS4ip8BtUnb_HtcShvynq9Wm1hzKxJ-DsDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsMXiqB8Oaibjgosm7Aw-pZ569tXURsIdYT0dg76R1QFmN-YlaH4pW5kbHuPFfR_b3K8MrrZhYIaUN5ORnUUXAK5v0onnsHd5UxhG1sDwpcuZtq8WfS7lVF3nsDidCf_esYeDW8uTmYAvcDEmSJUkX3nx-v8sVtPxlamqbilfCOZx1SkKjfYmC83hCOP2m8FaFbYOTX05Sx-mYi36pkmW9jUpo-cgV0OEOLAYXCFQHhVJ39m9nuauKz5StNrctqevRKYUHSj4wA62LoeqwV1WqevwFNzpMQVFvzRtgUwid0h3D-9NfZRh1Iampa3asIKPdnn0dHvNrJgYWce-VAi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoDohURKNhImowseUweLLy4CMXQHZxWyUkRN5EAw0t8BV60D06CPm3kcMsguD3xS_iO4UY-ID_LM3w22GdHLdJuLQA44-erVL0SlmO-gSJDSuUnyaZHS8yvuWp9Q5rHG8YtArGqXrK20gRdVeXNSifcwbsGTbT4IR1uu2_KdjVMHlvrT7EapQ9Wfd3fhMVq5xqfh-i1WqUYwLLWWo8ZH10cX-hgFxgJ_eeDr5crItcX8DzQq-5dZ7l6GWIL0XV-gdo3cudQ0hIq25_Pr7l63SO0cNRwEESrox1-q4WcgbSfN6-neRIgLbWJLFrn4tP6JVtO9C3Mjz0TRtpKY1KMqaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انهدام باند ۴ نفرهٔ سارقان سابقه‌دار منزل در تهران
🔹
اعضای این باند با استفاده از خودرو‌های پلاک جعلی در مناطق مختلف تهران اقدام به سرقت می‌کردند.
عکس: فاطمه جاوید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/468310" target="_blank">📅 02:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🎥
وزارت انرژی عربستان: یک ساختمان اداری متعلق به شرکت آرامکو در شهر ظهران هدف حمله قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/468309" target="_blank">📅 01:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7bv3EaJS11a6j8_oTMUP3tm-Qyx4NvEeyEoTngh4LDb_nHC4iAorWESZfac7BjJF8i3BkFut7eeYYRE4SjqviP4tx2tJyC_OSQ8hDenhjX864exok2ay5mDjEF_b8VD2t0zBkIijMQPky-4BQpKMxrmyLJIkTWcw_0eSuJxhytFOUEw7hYUuf3fUDuJEX0mQuoB7dHsTxTjR9qBFbzVqwOHT8xhx1vBRRiKjbJf4bzOnnFcQqgve_IFqYm9Rt8YgqJwPHI8KoOhBi8Km3PbdCoqhcggLf4Gl_ROWQEOUT9KosXJHR67W52A4CVlX0PHpimHqhyck4z9V0hVRfbXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال تایمز: فقط در یک‌روز ۶ کشتی متخلف در تنگهٔ هرمز مورد حمله قرار گرفتند
🔹
نشریهٔ انگلیسی فایننشال تایمز نوشت: برخورد با کشتی‌های متخلف در تنگهٔ هرمز به بالاترین شدت خود رسیده است.
🔹
به‌حدی که تنها در روز یکشنبه ۶ کشتی مورد حمله قرار گرفته است؛ درحالی‌که در دوهفتهٔ منتهی به ۱۱ اکتبر، ۲۴ کشتی مورد اصابت قرار گرفتند.
🔹
همچنین به گفتهٔ کپلر، محموله‌های نفتی از طریق هرمز در ۱۱ اکتبر به ۲.۹ میلیون بشکه کاهش یافت که کمترین حجم روزانه در این ماه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/468308" target="_blank">📅 01:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUQoQcqQvUrxxEkyfH0guxh3y00IlT2eHjYeyf1_8vmM3EEc5TFUGT6Z7QdTHlDZIVx9nK62ORNjiiXIZ5aKC6ManwW7iVXmpVlABb2GnChm5E2JPJZ9P9S1vwvyYJu5Yg731PEkFDgHWA2athUUOtI7pagQujU3jjNuIvmXa-oLDSo1tC4Kz24SbQQX8cC5JQHD2PbiBYHFuk3hgDfnOJNdU2-Pt3oGIljW8I0BYrG6Wsj5hH39FuCJAFBDhZS2UtZpIWCoU-XHZ9jlCMGJUSX-zUamYOh41JBOI0h1Xen4h7R5onmqayfPsdRPJ0rVorekv5-F7XScb_6cSbp7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم حملات رژیم صهیونیستی به جنوب لبنان
🔹
براساس آمار منتشر شده، رژیم صهیونیستی طی ۱۱ روز نخست اکتبر، ۲۶۲ مورد حمله به لبنان انجام داده است.
🔹
این حملات، با تعرضات تازه به شماری از شهرک‌های جنوب این کشور در ۱۲ اکتبر نیز ادامه یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/468307" target="_blank">📅 01:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08fe5dcc83.mp4?token=Zk8LrYxWvkGKD_ErJ_XXAy4oT_RJwN-PkzFVJiqjj0umJr6Bkj_PPf-5gWuXKLYze7E4-wit-Hfg4GFidunV7zPlGsfd0ClpBPJeX5-gHws7f7yBZGR6yaHIxOhLdgPkDLzjPzkk34tLxSEni6NWvwpUzt4bhBGFtWSv1IAztR71lZ9cDcwFyXDTRTAufdR5JA2QlIYnumq_S7SUkGS4BLGpYms-fFqs4M0_Foo7HxHR2dzRG8z3rzvaPSKIq3XOZRzS-1ulPXpBvZVWA4IX9h1qK_2keKpDlRlJO0gJVVjkeqI5G-zg66Vn7FX5MlT9EOkE7Zvmg2FvdR0MwtImtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08fe5dcc83.mp4?token=Zk8LrYxWvkGKD_ErJ_XXAy4oT_RJwN-PkzFVJiqjj0umJr6Bkj_PPf-5gWuXKLYze7E4-wit-Hfg4GFidunV7zPlGsfd0ClpBPJeX5-gHws7f7yBZGR6yaHIxOhLdgPkDLzjPzkk34tLxSEni6NWvwpUzt4bhBGFtWSv1IAztR71lZ9cDcwFyXDTRTAufdR5JA2QlIYnumq_S7SUkGS4BLGpYms-fFqs4M0_Foo7HxHR2dzRG8z3rzvaPSKIq3XOZRzS-1ulPXpBvZVWA4IX9h1qK_2keKpDlRlJO0gJVVjkeqI5G-zg66Vn7FX5MlT9EOkE7Zvmg2FvdR0MwtImtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  رویترز: ساختمان مرکزی آرامکو در الظهران مورد اصابت قرار گرفته است
🔹
خبرگزاری رویترز به نقل از یک منبع آگاه: ساختمان مرکزی شرکت نفتی سعودی آرامکو در شهر ظهران، امشب مورد اصابت قرار گرفته است.
🔹
هنوز مشخص نیست این ساختمان مستقیماً مورد اصابت قرار گرفته است…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/468306" target="_blank">📅 01:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/468305" target="_blank">📅 01:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468303">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEGMFE9ZCtv51fN1897g_1sqJ_NKKr9FQiffSySkUUc4HY--CDmisWgUzgfqvjyUkIzSAVJ4FtBwpCvT0Yfr2zzERmw_j7PNrU-0CJ7Vqcu6LGYwfMeoBcZ71KUjjR11OvxdndgwwpRRffarXXDek1tRd2nuQlyVMeWUj3vRSi9hXd98J9UFVwf3q4v8_-Zru4cCyYSqFz2_EDUPzgZKfl9ZoufCG7QWZP5WnRlGjQNfzpCMAQa5Y0AqIuPLgXZUNpBEriW-IzAIgmCo4Pwayh_CwgE7bsI01ueftYVNvV5Z2N03QplVz6FV9BocSCWHaHKS0LIfnJ3sYB5BlKDhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانۀ درخواست افزایش اعتبار كالابرگ همچنان در دسترس نیست.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/468303" target="_blank">📅 00:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468302">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3bc0b915.mp4?token=ITL5Q0lY91uCxBiMtW6R3MhAdm-Hq2ZeVXtYPz1JZQFq7f7dTyXlwN5CYItOs_iM_ZJbAddjgRJwpVYKxqEbjccWOwhvidEpKcrF7cGwS3eC_Y-qswX3bIIuAY5Utsyv48_Q_-d3XqRf34TQwju2m4EX5qF6U4ZZjij5mTeuq_GJTjTPJYKAlTotvTNuhWa3LuCqz2pjlLjmz0lIX67885UIvs2hyUZKunGOv2IX_-BfzWmk2TgOh1Y3_vKH8y73fyusak6XEu7z3walnRUt6wb-xI3ZCpIRAw72jjb75R_QDBkCpXNMwvRVYf8CFCnm8-ttTmJ6kvxVkZLdF8vwR7IPoavRgRYMg51enurmbqGJEopg_GxhgNxewFXLa8b8EgaKRbqpMyK1Bz8X28AbDN9Hb7eZKZUH97TVz7Ouq7t_DDLvUsBzyMsPXvw7rO7UoZF9Vi22QZ5vWFEMDC1VVyS4vGebo8XDsqpxOcqTiPL_ZjDz77BtrrsQS4ScbmVFCv-SZveBCuBJkplnRCpLYmokQF2tlyfUUKAMYXi_etkdaMPd7Zj_YX7gn_4OumG6EAb0SCHRp0_37T7r5zs3TCU6UUZxe--n2sEHsnkIWK5IuJc-jvDh9m6s6Kvn0Xb0Vg_WVZuFS44Q87BSWKv_dR21dHhgLgF-aI_24mr-r5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3bc0b915.mp4?token=ITL5Q0lY91uCxBiMtW6R3MhAdm-Hq2ZeVXtYPz1JZQFq7f7dTyXlwN5CYItOs_iM_ZJbAddjgRJwpVYKxqEbjccWOwhvidEpKcrF7cGwS3eC_Y-qswX3bIIuAY5Utsyv48_Q_-d3XqRf34TQwju2m4EX5qF6U4ZZjij5mTeuq_GJTjTPJYKAlTotvTNuhWa3LuCqz2pjlLjmz0lIX67885UIvs2hyUZKunGOv2IX_-BfzWmk2TgOh1Y3_vKH8y73fyusak6XEu7z3walnRUt6wb-xI3ZCpIRAw72jjb75R_QDBkCpXNMwvRVYf8CFCnm8-ttTmJ6kvxVkZLdF8vwR7IPoavRgRYMg51enurmbqGJEopg_GxhgNxewFXLa8b8EgaKRbqpMyK1Bz8X28AbDN9Hb7eZKZUH97TVz7Ouq7t_DDLvUsBzyMsPXvw7rO7UoZF9Vi22QZ5vWFEMDC1VVyS4vGebo8XDsqpxOcqTiPL_ZjDz77BtrrsQS4ScbmVFCv-SZveBCuBJkplnRCpLYmokQF2tlyfUUKAMYXi_etkdaMPd7Zj_YX7gn_4OumG6EAb0SCHRp0_37T7r5zs3TCU6UUZxe--n2sEHsnkIWK5IuJc-jvDh9m6s6Kvn0Xb0Vg_WVZuFS44Q87BSWKv_dR21dHhgLgF-aI_24mr-r5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغ میدان شهرداری رشت امشب هم با ایستادگی مردم روشن بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/468302" target="_blank">📅 00:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468301">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دیوار چین</div>
  <div class="tg-doc-extra">قسمت ۲</div>
</div>
<a href="https://t.me/farsna/468301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱ – دیوار چین</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/468301" target="_blank">📅 00:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468300">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7cVymnkUnDbj0sD1Z_g_N8KviBGOBWZJyA_i8Q-JZA_DvMrosVvix5agFuwpPf8cWw172-ljRQIa9iy7HXFx5bSdTC4yupQt9Y5pvwLFXT95imZ3NaheL6dfGSoi7NtQVEIpw9fTV7fD7Puiy2nh1kJ1DiVkqdYfUYCixpiEEhanKs7ddtz1Zl--e-9tKA8KEqAC3vphyHl6EYl-Q3h-QqQq1vc_WFKIsCBA2dCRL7a5UI7YwgdPMa7f6qsXirz4gn9S0fMLoM8NfyGnjUGWSYV-FkADGBeERimVVeT51sU2sYrUElObk_PmtLq0MmBwIPQ5VxSAXeiW6b3gjeYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زخم مال و نمک طعنه
🔹
بازرگانی در دادوستد هزار دینار زیان دید و سرمایه‌اش از دست رفت. رو به پسرش کرد و با تأکید گفت: «مبادا این راز را پیش کسی بازگو کنی یا بگذاری آشنا و غریبه از این باخت باخبر شوند.»
🔹
پسر گفت: «پدر جان، فرمانت را بر چشم می‌گذارم و لب فرو می‌بندم؛ اما می‌خواهم بدانم پنهان‌کردنِ این ماجرا چه فایده‌ای دارد و مصلحت در چیست؟»
🔹
بازرگان گفت: «برای اینکه اندوهمان ۲ برابر نشود؛ یکی ازدست‌رفتن سرمایه و مال، و دیگری طعنه و سرکوفت همسایگان و بدخواهان.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/468300" target="_blank">📅 00:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468299">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌ منابع عربی از حملۀ موشکی یمن به ریاض پایتخت عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/468299" target="_blank">📅 00:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468298">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/renvYPPKWdz-S6vxMLNNaepEvgEVXjVO4kENvHOTXtMXMGP99sJy7hCREFMgHVI_5Ki1yhqLUhC5vXBCnPfz8n81dpZ5YXTEgu-JA5xdVCbwSusFVV_niIkZ8auvflugfcsFtAquFfq_1O-oNP3lljvnhbg8EsKF-yeVFpYU1LueWCH-ItFVcQKpV5d4lKJmzqJCKa3fHVWr2SX2GK9mOLA0tPp37vy7yszzfVZiZ4l8F2HaKWgawg1BWSd8m8Zi8tznjEtliayNl7EsN3oyBnR1fLwUhjUBuNQ1Mrwow3PNmJKplhJ_ODYmJ0BJTNyAKGx_pbr_Ocs-W3nJT03D8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/468298" target="_blank">📅 00:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468297">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmwi8eLhM7uIEahCh9IB8b3Phg6m-vl8wRCaRfreaK_e5aIrCSwMnS9fuegFlX6oxMKEGnAdHPFD5YvkV16Imns9C-BJp6NOYQ8Ea76SvPqS3ZDmLOYED1HdA2hXSG8DrValFgZPSm2CA0Q3OFtClhV4nZ3BjcKhy3z6JJLcOAUbfjJbByYkP_vFf1I9ZS-VGNEnLCkmNCdOLmijvRm1WQRvNfX6JOIFTBsyCCGqSeVHwLy_GaL3kR-dyDDxczPLv7vXHZQHZ64nSD7bbvULfcOrhbNIm4qI7U7c0sUoHYn-_AuIKTUBIwyYwUxyWXI4xS741pMEhRTmCGdeKDWZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره شمالی موشک دوربردش را به رخ ترامپ کشید
🔹
بعد از آنکه دونالد ترامپ اعلام کرد ممکن است با رئیس کره شمالی دیدار کند او موشکی را به نمایش گذاشت که قابلیت رسیدن به خاک آمریکا را دارد.
🔸
رسانه دولتی کره شمالی روز سه‌شنبه گزارش داد که کیم جونگ اون رئیس این کشور، از موزه‌ای در حوزه صنایع دفاعی بازدید کرده است که در آن یک موشک بالستیک قاره‌پیما با قابلیت رسیدن به خاک آمریکا به نمایش گذاشته شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/468297" target="_blank">📅 23:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468296">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c991654e.mp4?token=LLybbiKal4s-G5u_JL4WjibB7i6EhXH44XVje6t0-FTeoDXvF91QHYfWTK09p1J8umA8VBEXg0ojdqJFNNtmsBFG-PVsARUeTBVFDi0PT90ofgWxRaRRPhq0ZG-SPmuSK-Ry-aXJBOSHABYcddvTr52-f2v9HMc1KHlhU3N9-VZRRbElkq7JkX6cFaxm99EdMNsHKnWFD-xlcQ5HsN3bMw2IVWyqLLlBJK2gD3dHXKinYwrnBzTGql9ryKxdqu9RxJrnCt79bSAdBWqlLuTdSagvc-QN2Zhj-D-PuxZMMjp_gjFMCWsu1XK_eRrzzd9_tedVIuFhx3jm7dBXIlAhfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c991654e.mp4?token=LLybbiKal4s-G5u_JL4WjibB7i6EhXH44XVje6t0-FTeoDXvF91QHYfWTK09p1J8umA8VBEXg0ojdqJFNNtmsBFG-PVsARUeTBVFDi0PT90ofgWxRaRRPhq0ZG-SPmuSK-Ry-aXJBOSHABYcddvTr52-f2v9HMc1KHlhU3N9-VZRRbElkq7JkX6cFaxm99EdMNsHKnWFD-xlcQ5HsN3bMw2IVWyqLLlBJK2gD3dHXKinYwrnBzTGql9ryKxdqu9RxJrnCt79bSAdBWqlLuTdSagvc-QN2Zhj-D-PuxZMMjp_gjFMCWsu1XK_eRrzzd9_tedVIuFhx3jm7dBXIlAhfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین باران پاییزی شیراز را آب‌وجارو کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/468296" target="_blank">📅 23:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468295">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7781b10e.mp4?token=FFauvFWO8Z9DGLUz-OqfL9OFbRzh-GoKoo-tbJGnjSp-KFBwItXHEv_QXdsGQ34zRYFT7pHKcAUUbTBOJqmjL0fGAW3tq1-gQEr3DDHb2_CcBnukeU49BPuVdh-LaFwxpaF5x0K19BqcY33RKy1cifKt7Q92AFAfrh5VjYl9QBbWtinSAd2FbOYCGAQAWGQnUscSfb9vw1aAPQoZcJ7OcaA0LI660AVbVQVXLA2LaI9RX_RSBGMGa7kKEWSor3gHoosAV-0LrIIaULaW9JraNb_G4SAyu-Xf4IWCZ-LdX5TKMDsuuN_MMKrSptVD4-uECL9swHr3xtCmJjTYVvenyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7781b10e.mp4?token=FFauvFWO8Z9DGLUz-OqfL9OFbRzh-GoKoo-tbJGnjSp-KFBwItXHEv_QXdsGQ34zRYFT7pHKcAUUbTBOJqmjL0fGAW3tq1-gQEr3DDHb2_CcBnukeU49BPuVdh-LaFwxpaF5x0K19BqcY33RKy1cifKt7Q92AFAfrh5VjYl9QBbWtinSAd2FbOYCGAQAWGQnUscSfb9vw1aAPQoZcJ7OcaA0LI660AVbVQVXLA2LaI9RX_RSBGMGa7kKEWSor3gHoosAV-0LrIIaULaW9JraNb_G4SAyu-Xf4IWCZ-LdX5TKMDsuuN_MMKrSptVD4-uECL9swHr3xtCmJjTYVvenyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
حضور نیروهای ویژۀ نیروی زمینی سپاه در رزمایش  ضدتروریستی اوراسیا ۲۰۲۶ بلاروس  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/468295" target="_blank">📅 23:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468294">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌  انفجار در نزدیکی مقر آرامکو در شرق عربستان
🔹
خبرگزاری رویترز: صدای انفجار در نزدیکی مقر شرکت آرامکو در منطقۀ الظهران شنیده شده است.
🔸
سازمان دفاع مدنی عربستان ساعتی پیش با اشاره به حملات به الظهران در شرق عربستان، مدعی شد که موشک یمن را رهگیری کرده است.…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/468294" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKXyWyO1izBonusN0UpdylBAB6ETEMHEAKsQ7KBjz-oy8dNRhdJ5BJMKMUnmzQetT2YWnAJ4LbRO3ygvKYNU6yGEAvRz6E2_mskAj6GAAIFS2E0BuREB1yqHmVnvF79Bb5JFJ_y48ufiUh6QBN5wLmWBhhkOGIMLVlCp0lRH0U3otUJwcPnrSPMgTTVM0QZ9_HMhggvY9zEE031gYGZSBR6SxlL0GRTyg7mkA3Y_rrZf0xOVRpXrzrJWRXIaASwXYdMafxMY2Ggio6epiTWh_aQ39DUIu1lHZ4vXTuxCMGeIANQw0xkKCIoutvKOHvZ0AfjOyOYYtKpNYno_3UNdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gcgnGdoOnOeq66tp0ZYtivte8sn8a-ffrLlS27K9bLDwSSxeBcGUYw8fOJKwEMxJHb7W3EKU4Va19ESW48kyJDnFovDLnaB240IupvC2DIh4gA8Qm75wEQHt0CywcVXeKMdr35Zg0Qk6kmffs8m2qY_xAeAqw4ub05KGjGQFDtLGAawUyVGpALYl6NMUbI_xWp0i4s1xeuMi0p3aEU_s3Fbaf-jyl8d_uBlLycDX1VexreNDTNh469ilf6VlSq3ZQsHFOCuLy-qm-_-8GGUY3QI44vjq_caXI_RzHbBwQ8VhMFPxajBkeOF0df-IHFQyGZ-1Y1HjjUL0OxEPidE7mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور نیروهای ویژۀ نیروی زمینی سپاه در رزمایش  ضدتروریستی اوراسیا ۲۰۲۶ بلاروس
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/468292" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468291">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyZlPPtWFdMgG8UeD1yD0eaJAFt2s6x4Oe1OdsryN2oNXgl4AEgUZ5dUlkfDTeTJz23-tJbUOazocTNICzUCkxSLCbq_vPCkFPc5CpeaDkO0WyfjJ6HuzKVAM76HQ55QO1UKY0J9gwXT2N21ZFy8SRaQ_HHala4qbJBFI1Xmvjf57ke1dOPFsBwmFCnL6oMa66LEFOhnY6o614dYmwHgQfp9V-LOe59DYCMhwCeNWES41I7ePOP7lPgk1ELbdmxHtn7on_hkpiT-Lut_Otz3T_21QTPL5S5C0OxiU2ErRD-hfnyyEq96eCy3PBFt6xUJrCoBJ5nJ1TJcHxMH5HLsxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ سایبری به فروشگاه زنجیره ۱۳۰ سالهٔ هلندی
🔹
فعالیت چندین مرکز توزیع شرکت سوپرمارکت زنجیره‌ای «آلبرت هاین» (Albert Heijn) در هلند، به‌دنبال یک حادثه امنیت سایبری، به‌طور کامل متوقف شده است.
🔹
به‌طوری‌که وب‌سایت، اپلیکیشن‌ها و خدمات مشتریان این شرکت همچنان از دسترس خارج هستند و قفسه‌های فروشگاه‌های آن روزبه‌روز خالی‌تر می‌شوند.
🔹
همچنین، گزارش‌های وجود دارد که کارکنان فروشگاه‌ها مجبور شده‌اند برچسب‌های قیمت را به‌صورت دستی روی محصولات نصب کنند چراکه رچسب‌های الکترونیکی قفسه‌ها قیمت‌های نادرستی را نمایش می‌دهند.
🔹
این اختلال به خارج از هلند نیز گسترش یافته و سایر برندهای متعلق به گروه «آهولد دِلهایزه» (Ahold Delhaize) را هم تحت تاثیر قرار داده است؛ از جمله فروشگاه‌های زنجیره‌ای «هانافورد»، «جاینت فود»، «استاپ اند شاپ» و «فود لاین» در آمریکا.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/468291" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کشته شدن ۴ نیروی امنیتی الجولانی در حماه سوریه
🔹
مرکز موسوم به دیدبان حقوق بشر سوریه: یک گشت امنیتی در حومۀ شرقی حماه، هدف حمله افراد ناشناس قرار گرفت و طی آن ۳ نفر از نیروهای امنیتی دولت الجولانی به ضرب گلوله چند فردناشناس سوار بر موتور سیکلت کشته شدند.
🔹
در یک حمله دیگر، افراد ناشناس به ایست بازرسی الحمرا در ریف حماة حمله کردند که در این حادثه هم یک نفر کشته و چندین نفر دیگر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/468290" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkxe_mLWhYZoX0OXTcwMQy-iTbZEtx3cgpGz80detkt4QIsjAwdy8aFrgV4dIewnOR6HiK9IaFnnGO2s4spWz6tK9r6rPblljxQYcoaBEk1aYlVq81gB-_Z-9twy60Ou9C5XbOIwAL43x7EZ0Jy-iDSGTpHFs-XhiONyWlxl-Ysb_w0ExEVKd15EFhp736rJUBwz6no2gLTOx0EvHikVuQ7krWIpcbYZKMOh1uO08pb-IoyssZz-1pxi7_SU-CPdhRclF5HsH8nA13wSQCNPlDGexyOzYEM_n0Q36RcEHPH6qOI2v115TgQr-F3aXCZUaalFPucrNT2-93wQfhHyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دستخط رهبر شهید انقلاب در تجلیل از شهدای مقاومت
◾️
سلام بر شهدای مقاومت و خیل عظیم مجاهدانی که در این راه جان خود را تقدیم کردند؛سیّدعلی خامنه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/468289" target="_blank">📅 23:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468282">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eN-tSoPw0L5aHOLeh4ls9m7k2MseL1bn2naVZAfCiqD1KxbX0HVJdGxksFyMRXTqnAQQbie8xc_cVZ6c13pX4-MGLdtKWbl8znvCh2QcdqnebCoTix3Bmhx5alM1_ojMVXDp6YOH6k7LhcvLuVWVK8E-0J7gjrVY7XHSYI8Yxvi5WYQjjAZogsBCOPlvUb2W-CgN7YMnJSiDDXUqyMTQvp0BFh0To7A79z2xBZ1NWtVcT-V4Zl6x5e8uQ_7DHRQamRqhlhz5yBqonzQV0C93gCZZmvgq8aJNF7luUEJWCDu_m45VANGvKIP5ps75ieHBR2XEP55278ZVbGJcX7BgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8cwAxkp8PI7urSclvhYfdUP4IFkipuOVotTl0akRpLOG8L7_DNccIFg7uaLeZp6B9wAr62j-hSS0GepPWVsayKUspK1Bft2q5CehTErDlpliYK_OfLIw82Oj9CPoJ-2MXVNQm7EX_az9XGPhZ_1nUiXzMV8CiQkh2N4I3Un2eEwou0VVgLJxIK9B2Tm7n_Q3sinBTR8bLsvy3GjeTujhoAfYJkaU8cc_oC5JNSzbWsP3UnlJIXN1YlJo_1_OWRb9FQKP3EG-2xCvuntbVFWJRofYLCC0t7kryDzlE8PxAEF_vPLyNxNvmBVJUREB0GtN4UbQXscJI-Khex29IQb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qa9me7qGKpldyFqTF7VQ6J2_ik1Yic01wYaSTSRSQXDCWNwR53HrwZEJFdtuQRdgJJI54Z_HAcZqJtxIdKboJOdSTXRErqR_THVfQgcIR1goLAQcOL2ewBy6VLjwlYqTpJ-C6aTKVaiY98KV7dRelnDA1cOwPlH_D7TWe85ab9Q93QAawOo7ZeCe0YQkuw-Fh2LWZpE2kaCtJ-giQyt73vY4_ghhKZigrevyGnbW2RUYheL_LqK_BvHlYMHQakMR8CJ8o7fp_xaMYgrnvA1YeKeaoYm_HNugdaUcUypAYV9XQlDr1PCtMnq_ZiJsZT_dvbtWvakSiiinrNbS-Sg9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEJpJYGS0L6K2UX9O7mqfzcTt8szMihYlN9H1gtWTWvX-X84HTxzYcn_HZfYKzn45Wseg-3j-N7_3W7o2CiI_crPoR6PTJ8phod4faVtwfOoQVMB7ZjSAcvco6NVlNHSBrKQrehVmlqK_4T_wHxwNqrUhGTN3XEiXCiJ_3v2o5gYowaUjWKNWU7fu1gTfwqDx3zzo5i44XhRGT9sfJ8w64lnnovp-n2BjBa-8R3iNjg160uM4l0sDDEo7AMlKvJHQWR3Vg3VFREmeug_6d5Xej5Ox3u8mtwCXbnYEt6ksQAmXy-ebVkxrwCLhHuD8sbI6r3kbEXNOmvejZnCQWJBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERqyAN45NbiIxg6EeV60ftQvVB5-ICLOzNF7-ZiqX6yp8kMhFvQ6O9IRCMaBLM8DUmqBFe125xoMPAE75qwwVzFHbXCpzmRTx8wvjvXKcNCCGl8TrnV5E4DMPeKL3kW3Bpo3jsfA5xRyuQV9iwBFMyDGhqZ6bLox4cEUBL_oq16DrEd6nfXP3W_wlpBgh6e48UhY3yTF1UBZYjHKzA66sayIa_86hyEB_Bft5o0SRUWgHn3HMVZUt1gq_bSy82rozfF5WOOLlvc9BwzHnKTBbH7P-dL1ae0d2mj0lczqSxM2lPSmx4QmgfNf-HLQmgxRu2tgpZdqVhur1apVFnfvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XT9uuHiovclevfmGzRe97ccqtzveSmN8TxdqjBtf2LEv0y8rYDgn__6-8QXQVOlfCQAqx8ZW7Zk_js6zfUEdUO7j2uUoRp87PYrPQhVnHqQg2AcGIEp30M7-PjI-CGxo0dVZEEtRoS4whB7iA2oF4ac_5BXdEMw3HCI52ovS8MZCFn9gXpebIPfI0YG9ojwCi3uKGdJ-KK6spzn9pzKd_xc_kmhIJQKbobeXA3wkw6_RztTVLUXJSikOkx1E_qvaG3R7sK0Ik3k7G4gNDjTpv_2qEyTtcekKmtqIDb0uTL_PC8-Uu49hXRsY_WFyZRb6-v8FnboQbA3Xz1-idEtDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXGm6nMHHzUjmzKwcY10yZ4TjauzrtygH0wWkZ1afmDAz6Ugz6R5bXJLFRnQdNWwjaGtDYZYpVt7HXT5atrWbFDhO3NZB4i0WpXbyL-S9lbuCTG2xG1DVk37OGng7O2LkMqs0HOcx2AScrJUsZRDONhd020W5F6GeQ-LdPhZ9CB2ojqqEcKvrvZjiPGdQ_gbxbXuL7aI16XiG8gTywYb9X6njsirKfzH7QWC1ieUv07OQ2Px0uyOM8gVmdm6e2nG_5rrq582Rv6Ci7g8rUgYINQpP4t5LQH5SqhFiSLe86BAII8icvJT2fLZ5Z3NtWhrSONc8ptKnDnAIZ1AQlrIVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سرخ‌وسفید پوشانی که شایستۀ تجلیل هستند
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/468282" target="_blank">📅 23:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468281">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ec1cd3c7.mp4?token=Do38GIrskSyMgUXn8FgJZYLV0_AFIofCM75Ij8VUhPFwsxnxjlvoiE8NeNuRhYl03lED4CgTy_xlFeOBZfQS097r_YyA20Diw_6XyUbOYV_vZNghwIh-m6bbVNtJdv5ZxMmuPuFpvxjjXFy3qydDi_VREGdZSO8JJfFM4dg2pgiELt-K_RlZTE10f8KRqiTKkj8pg1-kHPh_W3Z9ThA5XXv5fMOFBZzimkNnBANkmdGWNcTNyj7NmuEUOlXnRm9_xaSpKnCTJyeDCynEa2el_MMl4thJZKnjpMu3vjm2AHQxdJq1DlTNdAEJ8c7v7marbcZdXux3bgzUrke4CYKrvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ec1cd3c7.mp4?token=Do38GIrskSyMgUXn8FgJZYLV0_AFIofCM75Ij8VUhPFwsxnxjlvoiE8NeNuRhYl03lED4CgTy_xlFeOBZfQS097r_YyA20Diw_6XyUbOYV_vZNghwIh-m6bbVNtJdv5ZxMmuPuFpvxjjXFy3qydDi_VREGdZSO8JJfFM4dg2pgiELt-K_RlZTE10f8KRqiTKkj8pg1-kHPh_W3Z9ThA5XXv5fMOFBZzimkNnBANkmdGWNcTNyj7NmuEUOlXnRm9_xaSpKnCTJyeDCynEa2el_MMl4thJZKnjpMu3vjm2AHQxdJq1DlTNdAEJ8c7v7marbcZdXux3bgzUrke4CYKrvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌ای که هرشب در اصفهان پرشورتر می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/468281" target="_blank">📅 22:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468280">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/783f7423ad.mp4?token=jdLVfNMAACLq3WSCLmGPcQTYwvh2hBIbzWeMJ1JSCyy4rCo5eWYIbAqNE-lUnhw0ZCN57HHbm5iC-nXDZIYaSvnpOQNseM6iY_Ib9YBiKHvTd5JBxuZOtJTnv3-4OhOcnXV9nnDO20EffjUEGcFrwyQZDLcqZKllQuUFm6BFZ1FqOciNkjXb0Vae_UHOIt4h0ZfT2shXlcuKnZ7ZiDyFgrrY5S6S9HE4N-CJE9JHZAsgRH3_x4XL9pNQjZmcjfWaG89JIjh-oK4EyKhKwff6M2fwP57lNimRwOVib4xfo7oncUTAVY4Vds97T9pXnFo7sjnNr0LmOp0Nu-32Uz6qKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/783f7423ad.mp4?token=jdLVfNMAACLq3WSCLmGPcQTYwvh2hBIbzWeMJ1JSCyy4rCo5eWYIbAqNE-lUnhw0ZCN57HHbm5iC-nXDZIYaSvnpOQNseM6iY_Ib9YBiKHvTd5JBxuZOtJTnv3-4OhOcnXV9nnDO20EffjUEGcFrwyQZDLcqZKllQuUFm6BFZ1FqOciNkjXb0Vae_UHOIt4h0ZfT2shXlcuKnZ7ZiDyFgrrY5S6S9HE4N-CJE9JHZAsgRH3_x4XL9pNQjZmcjfWaG89JIjh-oK4EyKhKwff6M2fwP57lNimRwOVib4xfo7oncUTAVY4Vds97T9pXnFo7sjnNr0LmOp0Nu-32Uz6qKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تگرگ در بشاگرد هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/468280" target="_blank">📅 22:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468279">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ecf4b508.mp4?token=AwK_MmavvbvvftRMtKuLXnOK0NTxlzbpwl-3gkuLrBPmA9CJ1XLsCRXiods5QSpOc4p7SgcVhVnNMfNhfheA_dRWpF6CgJxejCiEo5DiiD0wkgtjCrSGx415FL-mk9IrktFK5k4uJzjY4llbkOPixz_wveG-28jaJoiogw3D0UPISu62PuXNW6HUl0f9xwM_MPI6Vq3uuOYnVS1KQc7xEo9Ax-HoV5ymjubjTvNHjPtKPf4tX5V7eYKYX3NTAOgHHdqPow0sSOffi_HQdJy8D-dmhtfuUc2HouJcA1oF0X7O6zPlrRDR79OcclImA9T45dNw_AMmMpHGnxBRY7_krg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ecf4b508.mp4?token=AwK_MmavvbvvftRMtKuLXnOK0NTxlzbpwl-3gkuLrBPmA9CJ1XLsCRXiods5QSpOc4p7SgcVhVnNMfNhfheA_dRWpF6CgJxejCiEo5DiiD0wkgtjCrSGx415FL-mk9IrktFK5k4uJzjY4llbkOPixz_wveG-28jaJoiogw3D0UPISu62PuXNW6HUl0f9xwM_MPI6Vq3uuOYnVS1KQc7xEo9Ax-HoV5ymjubjTvNHjPtKPf4tX5V7eYKYX3NTAOgHHdqPow0sSOffi_HQdJy8D-dmhtfuUc2HouJcA1oF0X7O6zPlrRDR79OcclImA9T45dNw_AMmMpHGnxBRY7_krg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش اختصاصی شبکه سه از وضعیت نابسامان کمبود آب و غذا در غزه
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/468279" target="_blank">📅 22:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468278">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌ ‌
🔴
سخنگوی ائتلاف سعودی وقوع حمله به نقاطی در الظهران و حرض در شرق عربستان را تایید کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/468278" target="_blank">📅 22:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a00I6F83Dk5s7dRcBu5EOVJu-4w6CYAVSDpsCMIf4lu4JupYMOirum32fCuyR_ctgWbrtMc2-_02ePjIyLVLdRK0ORTYFPoPjnB6EZ0YeoWXEwerdLhf2KAlu_JtW3yyR33w1xa2tIhk_tw4XAwMVFgoeltix9MnH4wboLhDuf_dWlhKAPe4KtpxxzFHpZ2lPiSMmhE3Lz-hMradBTVj-zhgAaYE0NLK_QXAntiQJ2tQTgUjCxyex4Dnv6kBRT3XlFhECyLOdlal73pZnRER8SA56ATA4nAS-HUbWTjldkJ8BP3-s_EfMcnd8bQSfwkReMoLcPEXqZ0aQwWkERyVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش دیگر در تنگۀ هرمز هدف قرار گرفت
🔹
سازمان تجارت دریایی انگلیس: یک نفتکش در تنگۀ هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/468270" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">احضار مسئولان میراث فرهنگی همدان پس از انتشار فیلم یک بلاگر در غار علیصدر
🔹
معاون دادستان استان همدان: درپی انتشار فیلم شنای یک بلاگر در غار علیصدر و انتقادها دربارۀ نحوۀ حفاظت از این اثر ملی، مسئولان میراث فرهنگی برای ارائه توضیحات فراخوانده شدند.
🔹
هیچ‌کس حق ندارد به بهانه تولید محتوا یا جذب مخاطب، ضوابط حفاظتی این اثر ارزشمند را نادیده بگیرد و آن را در معرض آسیب قرار دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/468269" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
