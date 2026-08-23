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
<img src="https://cdn4.telesco.pe/file/mLFqCLMYaaMKI9A7URfo6A2gDW9jgBODHpVVJRAAld2On7EBPa5_KLr2kxt31x1dZv0G3WFGmBa7zpvnuJXiLvorwNnJArxSVRDrnJ4J2QkMFZ3sBN7DAiNozhxzDI6KEpQU9G3qXcW16mCTMaXIBgmsqQ_GmVum0sQjuxjSBUx3cRGCoOu5lop6cl1EEGRXhNmd8vgP2zrGKxdGKDUa4ZNVu2XvlEUe0FyM06Y2wJU9GUWiQK370utrS9SCd-SpDsuOzUxmNvlo0v4zS9RFGbB3A2U0ODt7ef6TSu6Wuvqj6Hk_-Ewoao5_eVLFES4QRQg657NIBFYUEO4MZl4xmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 09:00:03</div>
<hr>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWhoxdI0dhtXFClPcvJYVdc1iidV6UoxgS8yNh-XRzaZhAo7Rz1OPdZetnF76-n76dx7QSQoJuhgTPWr5AwFb2BcSomyrsBw1g8vKMPvx_hVOH5a0B5MfK2Vd27wD3r7jN1GcExLY9hH4-tFIM1mw2G6Yb0_HgNxwx-9VP1l0mk9r7_tN4VLEeFgz_oJKWL9UmmbA4YOd-wwbXb6GiIfdaT3mRvafjm8PWbLfspk8ppu4bpWaVjmQeuuOTRiKY6q1qiglV1rodfl3_qRHolfVysov4OcQkalW1P01vbzlBT9NVQv2CjK2AFY6LErfGxqDxrwEQlWDmxBra1hryHddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iva_RPC2gl6_FOb85jOrHGoCqrzfMfI3GCqfmflfT8rUkZaJbaC2PW3CuFr9gZ-3p6Gjq4lGcB6KZrZwueKYxYhiZKF71NmShoS6q7eCxhKXNqpCsuiBUxDTZSPA56WFnf8oK6Yrg4NvwopCXJuHK3frVHlE0K9PzRytcGkvIFAOhXnmjRwmf3NMPvpuXobux-hJwaHmc2MCWpWuVR-QfBtx49F79gIz64uW8cJqvUzjluKvLC36QIR8CFg8vR94EdXucQt9m0SNUU8uD9teLJvzGnhh9XwcJDKBPEwfsFytE34soUYJ3LKDdd3EOb7wA_l7pdZC-_dqbExQx44DUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTEP4VgTMFVlurk-LsKID8OPSYINxsnbM33Zw7StCFEPi8SZdHMeHYK2TwO8dC1YUjIbycvawcNG17cz7bZnKza2rwX05DrhG7wKNrDYq8nlxJ-w0BVryXd1ZaJuOVkLN7uOWNuv3u8DlXGsKSD9BOv8CSLCPgLKrPENxPTo3rfwoRgHdFim96NjwYDY0kuaNRfVp9EozOndSFaqHcIlbi2uWOgBGT0_RPs_hN7oFyDhlIOszXs9KxNOioYzdj084xgnH3piaNrgVAgBEfEIidasYUwAf5_2mrpR2Ow42DD-nUurOkQfBgtY_SNaDS-NUCq2j53FLvM0-ca4xdgBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnP1BISiyckWHKYlVOV1ezMHw0IMGmbiXpS3XO4UhYXLLrUijXXcCohZItYqgxaXloUkDkj-kSJq8Zl-I-tDkXd5FiZe6zDjDE144fo7oc9jBvWAjFmE8RYIZ40o_TNxNGgiyDnVArfEgSio_Ay-o27g0OMA-k5U0x6rdlNsg_0raKLH2PXbcM3prl9CwQOM5Pm8vfSOnHSAQpAO0FwntZPtjdnonF9qBI_NVx8Led9nAXwBluMoZ0epCS2cfy8To-9maMOATEliKXzwx3PI43gnM3e8oHxWhbGxxSUOlqvnasRlyjuS1XglsYmGGGkcohFhCEYhh8E-NtWJrvsXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSISjKurILtq3tzGcduL-OZ6Jp6sjlWfqEjf1bPgo-UI1L6PDJAEUY0Z8IbixJr5Mh7aFKiBzr63ef4qDu0--Fve5i7-WsVcrwGa-tsseHy1fg0Nt5OXvIJzkXNtv3HAB9pZYr1QivpEkjHiRa7A5uADhrc_qBzAM_BSCtThRMoR01jZ_MlmnYzB2Rv9eotWt7CnnTM8aJudEcTrXcqaqae2_6n1G64LYvvmzzXxUqVw0HkHAaRobBQY-s5C6SZ7FiBK-wpAyoB4Yc5w2Ndf7pkfwt-RXsBzy5Wul9qUS_ofMtdzNwCx72-4QkgR4WBiznucNyn7hGJvFSCe2VpaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwLqtbj4B1xYGhdTkDGk29kLJFJVNv9a9HI4QzDdMAKeslrhj1uoELWTBai2r51mam4JpcFYNxTWGxVjSvuWugpyELdxAK3m_TAjcIiOWX2Bo0vyCUbcjGLG0QQZ89HFOIstnD-eXf3ZF83Q4xCGINupyWWw8euB3E1C51WZKdNp08u-Y2YukfPN5qDfRxb_pFSh7PmN5UJW4u9189yBCMnFFMoNCpqBi6jumTy28KQNpgTHeshnDdxB3i_4RCv-DPbaXPqJTtwigBlG-5UuHfGhPprSXg3hJx1nD_atAFUmCp3YlxAM4_Z2YbesD7oqKUB0ZMG1USRzw-BHkPXgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4X9kgu0GMN5xTmPUjlID3bNCqv6rfvf9ygjnc9nAR6wDGSniKmYt0aLRs00ZES3GrNhmpL9KPczz6oghdcZbLMBJhr_46XojSwqR7TKiklUAtqwYlUfSWPUgPX-NxgNZUyttidEz_LALfvCXXCldXy4j2uTL2Bgpl-RRU07dAWf09JhwnqX-UvGVp1EMz3vJY2km068y4SVA0EpYYFeZ5aUOpYej_UlNDSKA7FNphTny-Q-2YH62ttTc3x1bZqFv4zezSkRfZ_xVQsBWJJdRmXtEzpbcZ1JLzwurrB1Hb8fYlqtptghLOQFuDJ7oP2FbQX2GlaFwC_6YALEoDM1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcfn69DWDRB3OV4pLRSaVR_swYqIAAElli1kzKzmTHsPDJvy1CexK0TPPk1lzhQG5crzhOb59IzuA5EUPdi0ZNrHMv8u-DKEuU9BfQ4ok5KWIG8hGyO7DgkKqhcap1E6Eeve7zadaT3eQa9CHjC2Hp6irNjE1VCEaPNfOCakqdNTU2wyvUzhiSmJ92fj8KMfGJqddLQ83a2wlQ6bYwbpRL6fz63B5YyWxMSunqlbn2vFSvB0OCgcJbkjDWI3DRZNoXl2i0PVaIXpnUHK8Nh5qJvzW2juiQSn3gqu4GfTz2KHA8lUqs7m-7je5TeMS1hQRNr_Q4j_CiPy3hoGuZQzQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWjQKQtEBg64VTqKYxNshaOICEeHmR_Rih_xX5BeTDBWpPbiexND5_aE4drcgTPRqNPMjQimZrwqEINz0ej9OZXOCceqtO7TxpT-9bI0CjavAsSU2OC2_dfIlLHfwlo1iH0G84871kzbf3nRJwZY1NscOVwZuIz_LyxRKnx3yyDbOXanCNghas4rr1apmZbuJynfS8BSJAn96sWPFRM0gRYt8qow-7JyNKuifDRt0I0pyuoNJpdFAa_kF7764qS5a5-xTisPcmrSVpxVxASmzQWIuN1FnUFLM8hs2iP1BzdtZUgly2_ZmKOPoVqOdQmc47e0E5n017mER3iury5GTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYVkh2R5Ouj92ry9ZNEac2JXvQeArRI77S0x481sF50P7YRQUTkLNC9OwYaqhE26EwioZvU624N9pgrIeZp3_hIBC_6PijH4PfU3leRX3sZjU2yHJigx4VMnUTOmg1863Y-jLOw5npt36KIzyEiqENCJi9kEM5JSPHsRxeKnaiLWWXVGfo3JRIVgmVTsoaFXN_G00twCa9Y5klArz3Ce3aVjep5C8OZu3h5OG2L6gxdeXoz73sjep_BHUiUTHtFJHgzFiVBjWXl3M5CWTjkXLVL_EecbZA6fSkrCwC4oZdMq6OWDlvZ51kY8lS4ukzxG2N7yaY8zW6P9NdTYvc-7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI2hR_zJUJJsWAGRMY83WCtlRWXJTc-iK8HeRBFcWaR7iRa0ZpeytYSIaf5GGqd2LQtg7Bd7fjo78ruhHwI6HaivHBpcHtJiZakNAku0UpsyQ55MnGB6sSRlu5_dNxKwZBFlAVNJ9P6ukOBMDHru90NWfoGlkCovwGaNMzwij8BInLOODF60S3Ke1pPxG8pFOxiUB-WMSDlqzE1aqqwy4lvtXPiNvE0lJbX2xIuMsM8GaVMfJ5S5Y1GrLPwTKUkP4gFyV_cGYiFYaHywDT3RoOx3-ynZoDodc37v8zmkq2dj_1HbqsbL7kFA4aRbKs3PRzbU01cP57Wamh43ejFmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGZ4q9T0G-kIQT7PTrlhM-0UTj5NJWfp4XBYTj4zSuYrb1KEHDgSp67KbHO-II6sLjV_e4HsjzY-20KNZXHTijBsnThw_LpqGnpGqEVbQInZ3VhPOQRr2OFyHasq5PUf6PWyvwmsJ6xvYXsCqppDXr1_4aExG-QmVszbkJWqRfhoZYo5kzhixAOQ8BMjHYhyVKrAD_lq1aQAnG-VSmcTqk7J2Pw_PBCA4YlZpB0G021KkYjZlDkkXDx_tHURpch5YV6KBLf6LFhwV7fs4lb6ae5F7mUPz4pmi0i1DUvnTltb0YcVBcjBalAzn3tLifQHY-egQcEoeLMmYsSJj5PdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeW176jniQjRphNlt9cljSQ_CSLS8eC3JZFkLrmdbczX_smxMN4phSPkcKswGECcKxIV3v4mbQodF90OtVL7XwqBBDk0B6tQPy5fAIoKIIypDU016WznBmK4aiamA9ekdxqZs7PK6-vYLWID5G57kFBxg8dg7_D3GMZQBPksdP_PoOuYYT01D2LLtSn9Qt_XdYPyo8vVNL-H9B09_58hp2On14LDGrTbpxKT3m5xNd08ExfPYzJ2j0T03iUtbn0rmIURA3xZGJispWZ1c2J3MaxEuDvecBnoFpvq1rtws4Rj-1yIr1kTpCf2hJNNoZ7Ey8MOZmsZ080t2miikVRGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwsfBCwvfTmQDd2kdMA1C5otlmm76jak021xo4hVi9jxcE9hgAs8tV4jti5JaEOMxznzSjH7jlMd9rnEVmcsPVjEvbqBD0QdBE0wqEiZ5NLuY4JXh7rR81hS8uXIX62LrpMqDrJ7Cv8KTjJRfpyXoshoDneRN5quMs6eb6fIFaDxb4NJE4rExaXGG-J4Pa4EwILWOU-eZGxFgSOyYZHJwLMnuyPLzSApZibMZfiKyDmD1IWV9QHIrCOeXb7Jp-HgMG_QOQRMwCK3vE8gBO_SxtGgHp8G5QTPk52Z98P4QMKL5vypNHqdmcyh9udBzQdcTDQdGnIGpHRY2roh9v9sVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHzzg8JCjeRahuN3X5tLXtu0hbqjfjDABqsInM1BQQLMvcA0T3g8bHNL_iJ09t_QDQmJI_C46zbERam9JdaLYeqknFIE-O38k1KRecFDozuVMyv29DKZIja5Q27h-9v2-Auost9B_zpR1__FAin3t08GZv2kOedAlCNvm3qSloEiiXjR8Tcq-SIAszJYgaaUEvBPhcy2ULVBCnDkvLGbmvu6VQsR6rgVKK6hJl_rN4lq1rvT85stX8RU_jlFOxUcm-riwMs0Qx6vmLOn7hPfpXVBHoxjNlvY-dKLdfoNhX2eUJrrbDf2qVh-sH6z96Ty6edMG3KK12cteEF_4AEksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbR6h7_bW1_Q8eyR6CnjcPqxNeU_hRG25kydVtB8nlETrI5vd_kUWvH-3SMcNJuu7qKI9AaC7y569bOhuRowcmdG_ChYLvEapZq9pJYl9DqRlWzuCnai0VC591DD2V8MFqQVcpjP4YTm1pUqm7YbZYjMjs5qB5zK3hZ9v8in-VeX01nc8emnM1BnCHITAg2OPWuNWAFzoBapBtEEk77d_aYUIVyElpfCClhQooAjewVZ6USofDgoRJcI3xE6J2VVnLeRswehqbQ67XL3WbCxZSvYFrXZT5yBMZgSM8lTr6GiwCVGhL3zhTqBb9MCjcB3WCDf875z2r9DqqKniDS9Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qs9JRCCSUvjji9MM-i9OShCHW2kiuDXlUddeWswxuXjooxkMWBeTMgWzKB802VLQkJcPqSy92Xu135huux_9DPdFO897FbZnzR68SCZDbKohf06b8SIjxEC3CSlcBweJsnuFLtl0pBXNTMIoLnps2FWW9f-od7A_negQ4_t-A6HfQGFzuKj8UF3FyBDCMyz99y8Mm9vwv9sPMo1JI1tTFKzcZAY2jDwQvPd2sHuykL2UGvBoIqdxdt9lLwTTVm2G3Io8go-MdCLFZonjq7ZJ8veW048IOQjvxCitSuiIuYbzE9jaBrtEx7vMXuRAiRxU6faqPcq0ybcorF0JuLIDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4moI18Af-WzGs5erdr-QkhiovBqeSLmDvzel9gk-QHn4jUL0gAVPPl4TiVHH2n3nILXjQKHHbAEFNiYiuJ9Uz_fNGDNQDIfP22tAjYZGfD1dYOvJiokgufCEifFOYktb-pBrf3w2-CCmcItgC4va48DdDlysMEnU7U2F7U5Icw8Tkpp4e2IShlbUJHeHPiDkqNQvWaIyvdBfxQJoalPRAPXFbYZgugaw8xDe3gUKwmBvliTrC7H4NM5Z5_8SFZ02iDfIA56zMs-qTw-dffHHZd3eZ-gukIbiHKMnDLumOWpJXKjdEn_jFGClKMo-NinT1QAkQR2_ADkPGDJNtmRVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKJufKNfJ6rLM8GneTJE27Z2G0DU6XUJQptkQXftpjJqGLiW-unfjQUyb7Olt6Vt94X_XRt2twusvp4yZcx_R2Afy3AZua9enLe6J8b7N53JWQrKKTx-jfZyqrhDINMg5B7xPR_d4kbMKSnVnz7DwQL5sDrbeHBIPGajqSzLFf3ffFhI7nzEFGUJk41aAdTq5vOZyrsQKb-xAOo8q-fQtmhRdZGYMLqYGEZcflxIplsdSV_5BDGUqAsnHWb5UCB-9Hog1WRWYwFtgL15M-anbVX9pMreKgPUAsNdexisGTNsCEx_g8z8ZlB3hw6WdyTMNKDUDHiWo41lhNSDZUXpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USwyVwVPQwBZ-PBq9OTQ12qvW0xRRGZiG4y5xqkdIXiglIgNoHvAYdSJ_NmDokqp2RefYqQkJO9ed3KVzoVfZpaslIs2eLmbtXGFLp77RFOK4lAZLZsCJMFwiOl7X5P4FL_x4QfNikjT7p1vUggGYeLzSpY6LQDt-CPqtnnlkaNADcv3EthkmwIaAA7nEwB8hvbrFzrJy_aoxdDjQG-1Ozx65457q2IlXG5LTvKzeCafTRuUcxpeAZ_Dz6VW3WiKrFgkAgEkRdOOn5qLdUDz3VWC-j_xvkjRaJJr4dc-VGw2gpc7uEBXZuN4S_BZETqVYPk6DUWcVEiV3vOUUn33Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrPveIFmpen9Y2dn6k9HqjdLg-F3f4fbpeX0ddRpzwKD4JjJJQTq5XCvrgqohe0vl0jwx5qHx9NC9Sv7C-fVTwMCGP9Nx9VAHjlJKObJ2thUHaR3ZGtF_BXwTgXr8LnDkmRHBW3QOamcC_xg7qrqNidfvj-_kj0IBLAFNVjj1R-5iawtF4xktLCQeoc7pev5TJxrj5py33ltbrh68hrVSCuTdNr8jS6uWUKJpVshfGl2EQXsfsimL_bO2fg2VxiGU3_j8BeYtvdI2EvlukBuVKyH3BtucQNBAQr98RpHcuXwQHDLwe10IRGa4kB9ciI0Lgqy2dGsbP91om-p4fPUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DE68KL9c1xHs459ZTDkAoc1jj7d8bKG-yhn8sQz_RbS5U7Ls6fDtppn4tHs-mYFOPC6o0W98kWEFaqE6tRq-KnddjOcpxIBXrd9pjE7wgQJv1YLBDWDt-w1dnzTFDg6goJ--FQ85yjRUHR637YJ1gJXCbE-XLFEXk01lgSw2_-ILilwFddhqR0e1rSblWcISze85oMjMKtuLseSHt3SoC0umXMoE8paU5MSGcgvF3DrNaeIswx8TLfcs-WBOvSNy8v1juviTxI0M4EGxvfAgIIBv5zCLnTJv7ZTlguYMftp52jpGEkpWVKz93ob6LRptREHVsQuiBjwiyaVl8WG8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRkZ9CKafz2lVRyixFP-Sp4MUtIVi1S25j3bFxMpp8aDEzRRQHsD_dq3X8qH6FFX4bMOoCT0gziFu2_5MaeDQAB-Lee2ZKIpTVzFazvphl9Fl-sVtuICJ9bDly7xtOovpeaDcmLDaQMcXQUeOtQ6i5TSql9NUsx3E-tKmLut-kdNnAfQ4umeTaTAa_j-x5dYuQHBW3A7dbXIh8D2YUcKAnw5mhEsL6YaO3UG-TASJA5UmA120ztfLqNgEBjXrXyf82_RWdOxQ-CqbINGRy-EOoKbFHY_75Z_uwHgCYOr4uE0oG3t5-0JAxS38vDNEjbo3OMU4cMY6ZBVFk4xkaniXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWYz0Whd_g0MJWySYHoDQEirSogBVh11yq5P1VpT7qSfLfPTuwVLnxEkhV571maeW5MmH2EMz90vXIfM8LFf0jcKGVXk64z_EqxVGNS98JJUa8AOROqUJnGcnIsAQO85zxy5zLlbetxgPjkHuj1mhTI9vdMnFEY6tTzKTTZscIbVigDiBr6dhW0lmDKZ0Jc0G3MG2zGkuO39eRlSy7V7l3_4DylQWbfgQBooYD82k4_sB4AOPYvCsOz4vuDHDB4CVXw50xGvfrVTGbxe3_UlyEeo9MTfnFK1AB2axiPcZMcpDB9Z2ir8x9rVOw0chzv9UhjUy6X1yAwemB8To0xaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzTr0QglUpzz7jBiu1FHqLkDIrLO6T1HLmJSeA1-kdPw51cfvbedLUdYbyzN6XGNhwTPI6CBJ_nTG5T5_sy0nKSmVhtwKq0ZOivEIA8bx7Ry7geKRvW87X-slXGnbbKB-Zq9d_jrOyNFq8o3VYa_UqHpBXGpCf0eTVzcvFTtZEJpBjNhTRV9vNNWv_KKwWgmwpizD4Ga0FkZ10QTHDdaD376A2EsDN-ATfpbl7mVEX3gl9Fsb5vdE2knO21vWGTLWwX4jebaRPivODgoeC27RP-__qT0XC9p2BW6_yBSrELXfizvWdFrMnQdhQ9-IB2g4xg8kg1HON0lXUAoeQuLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu1kvv70FLgk3kkWGXop4INWUzWXdfheWb3jsU4849bO9LFz4EUDhN0wgIS7WbJVRf3bJQYoG_GhqMy0ZAuiUd1d5QnRHYQCxUTbcXLltdsPJVkDw54w-18JNUbHX1K4tfmqYavCW95fOJMY6GaOp6XsVlO3mED0q6ebZoZM-S2_Bztceztf0E7hSH-TuMrcxAeYU5EZH6oCeiAQ7rRxim5fJZYdxKm9T9MWHNn79jBSIn8jRsaWsOb-yzp_83n-d2OJa4jKErV1tNbPT2AxvlgRAXHNiP5I1Po_KnpxHddcOqsNeZ2qP36JWgS-FDbbJh8MP7pZyLzPB__Yo52Zmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU9MJUOaDddNyAlH8cupo-Ymavd_Rv9bjFXYNgOGCHDh2edAAolSvb9GrvznkCxZGf9SYYpn96q25lrBNO3NNmBfKkA_f-fpmzVWlEjgC18xc4_npfnUdY7W3c3ch0fn2ZW0rEef6uw4A3ZBav_vCyHj02N9IOrV1JWmkPiJAm5hicQTjWMFS-R_e7eWPV3kDj_PrP2WDTLZHuXJMTGuaQEBohf8H_dM8ckwDBF3Vuub2skoiqgpADnJZlvwjHSx22vRtOlWl8UX3SzyVmnkxmiJCwMU3R5CwMG36QmQLad4sv2fpFPOi3cSUfx3A6RRRyRNPPQRNLDcL1n5ULjmxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaNdn-MHvb5etyi370hOyhYLMddLorOMFMdD2laI2GbYFTT68kRLMMwGiT7WBqvwv5U8COJMyedI9cHeigjlp8DsrNdsalMeVDjg9_UX1Ftwljc5yEiTHhmjnAkrguh5kHWzQ10QyOsla_yZXa4cHn-RqMeXNy6jOnWWFNhtyKhWF5C3shvJOMo9K_ICdlO6uLUnSiIRjGLw0Dr4xVEZ0_gX6RtIXakbzaS4r1XTShLPH5gS-QYqVeUh8l_cCs-g1sk07KmKi5ziYkCEvJgJ5apOGUKxzNQ1tlyVcpDxftA9D03e03NkyKmweDPopZAQ56QELzfc5TYwE9eAouV5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATn22ppCg7gspydc59TfsZELHcRvIVKkGErUIxvtiCREDLADaUNA6eoc_SDFiUzQi_pHu60cicQtdxWxrmSvtvqOGqzj66_s1bny29ZfCumVjozNTrvHbQZfUc1_U5rAZgfw1up7M3D3_z6gUl0TtCJaG1ArjXvSFCV2c_cGLXxdXxLQfPZ2TmTRjYIt9KGkuzVOzyz0FeeJKnBplnYhad0dQkfJ-6vS1Fjf8VGvAujdd4yMKiyT9ml44CaUFJ83BCiU5Iaf2wi6o7RAAv202aGue9Ob07jLB-cPwCT6GtZsXN6_aMWF29iMDkFsG-qp1NgU9TlInckUNnhgqwIlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKQXClSggtLdT_rCxJHD98MAAfz_UOc-vtdL1T1hvJAfPpCQyK4-frPnPRrywRYawUu2x2i70R8YC3E4UfYsiS8WVrEuwjAXCXmcySrVUfH0z3U8cPSGNg3PrmZnhsyMSKj_taiIl6RkldXmY4GJaDtcTdicidwYm14zob8RHOW9bv-nB89ser_3ZCoMfKWqKzLVG25cNT0Isr_BsZeRxJJgiJ9NLnu5ThzbnJ8PoUScSpM6q9CSchknZTgj4AXMyJMK4E0Ur_CtOLVGL0NI-Y0X3Osu6s4MvtBrtVgdO-QXhsbACRjc2BWj54Qy1QcRVAb8mxtE7az5uxqEGKrKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnQOdGmSLjZ-LIz4qQaQeNqLO7qfrTmCZmpZq1he1RQWL3UAJV_VDjiKOMOfCxaQWW5ZvJnA_bE3t4cYkr4FhJn9tO94gfIxWWEm1yKAYUzw2VAy0Va1BFQxZo-DgAEatyfNBFM1eKXHl2Sfbf_ymzNMcIhGZqhgdFa5LPgHW-nexNVW4gIjzc4vYOLWcXATwBQovoPlztynj05O662-dRqoCHJYIvfJ5_lHHEEVLHi-ecMnTrYemhcYPB0ZeCwhZmpiQriBfxToBo4EumnyawW9iXGakrJkAVaN1srnC4-ssMT48x0h-_I3ICDaMAoc4t6rLMgMqGufsOxfFQKThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoqTJSCYj48CM-HeJCHCVlK668DvrmjMDflAorhr5SZjXmAbf7m00VWiEcj7WXXJA18RUcpz80aNsdxBYknByUJX6ifCrZ-EnYeCLHgBkI7UdSYVCSiIsxJ-aHfqCoVodnmrxgDekTx3GBNSnzc8nMvsd-8hpzgixz2cGxaPOlPIGX4-PACGX-jG3KQ82nKE2Gm3HBJS4KCTdC8Dpfo9Mc0aNf7ZoAKOzfWA7hSfCMvTy2OX0lu2vw30pE5HrjP57OPh5M5RDCg9oN0e-nH_Q6a5w7HLsBAPxMs_dUbuF66bshdXBrjPDPPBWnksl8KdSWYoDIDeP9tyEmS0gl0k6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgw7VfT9n2-9DbMsEOKXPH1Ajs3bdgmaE3SA_weUBCRaChcocVo9v7MikOwTgvQtQ9pARdqIyhicmjDBzEZgRQEgG-eruoKsEKzMxwfCgcKOuNNjstH0jH_Y0pXuHca5o8_IDAU5fsC6OzdTpC_nWDzZC2MqV0Jr2VBwkBvGiCYj4Ia_Q9bVJTJOnw8ybhnHvpC7m-fJ5rnA_IRXmKGGWDmjICGYBVdJ8Ia0sLZiO2yprSKX9VjTMoCTKwRtzG77T3r6OwpfgMh_sPEVECFBpzERj-TKNvBMB_uKWgQhq3oTpefiT8UreqEiL5CnIpaqqfXk78g0MDl8rKAKuopnWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfYqCSjo6B3Uhcab8Ady0Ib8VVJ9zjXG1TjsJtQj5a2I6IqVGhKizMzdj5Q8LA5xHeRXeG5SdCyrZ8bEyrGkcC34HocsKw367nOpZjSDhKixtvCz1offG-gra6GTkOkvojloZEtf2KArUt1s4oBPhZlfulC4ZVjTeSpWEx3oiIbpnPmbjykx5iUG-fLH6IUZ1pIaG_Hhj2dLpPN5KIl7gt-0ZQz7suqETOiIXwoJJc4zhKESMhSiJqCaHQkZbb4vFh_4_D61nr2saEcI5ZbFNbzuyM507nIXEkyVi6J6DQNJsBnMH-4nU3sRfb7zurvqD4SRs-IvDYoxLCv-XfS5wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=oZi6aTbkeEtK96vIagRFpMHb4B3PohBcIKszJn8Ri4PBbbqJyNV7eoEZNkUI4ncvB9eCLonwgo2-CnOSuNp6Cg9TV7sSj34qE-evIa-vwniq0IxlcrY-BkKohdn9cBz_ZAsYklykrsz3cZPKayqPwkaNJvpxsVfPSvLK6t-7zl9G2QGjQDo1nEt44mllcAJjzuk3BCjsYDhG3oB6myTEkuatnDYs37zPFOe6zXXGpoiRhFu-hIMbJAB_ld0pV9vyurYbePhWaYKWQfQZRKXvwoRP4XbOw2TVeCgkZ6LC1W_bfNKpFAKemNzuxxzXykUrQ_mTBM3ar0h_tZvtcXFIoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=oZi6aTbkeEtK96vIagRFpMHb4B3PohBcIKszJn8Ri4PBbbqJyNV7eoEZNkUI4ncvB9eCLonwgo2-CnOSuNp6Cg9TV7sSj34qE-evIa-vwniq0IxlcrY-BkKohdn9cBz_ZAsYklykrsz3cZPKayqPwkaNJvpxsVfPSvLK6t-7zl9G2QGjQDo1nEt44mllcAJjzuk3BCjsYDhG3oB6myTEkuatnDYs37zPFOe6zXXGpoiRhFu-hIMbJAB_ld0pV9vyurYbePhWaYKWQfQZRKXvwoRP4XbOw2TVeCgkZ6LC1W_bfNKpFAKemNzuxxzXykUrQ_mTBM3ar0h_tZvtcXFIoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu6bElhO8DgFPTkNcSyRMLl852-BweS2XRZXxjImOTMfcxwQS05NHmgdQEHxpG3gTaTM-If7jfhyXHazrKWm7va-Y8X_BEVtMvy-STiwMEEYledOxr_ABvy33xF9OPHG5h-VxssoxmJIqhky1J4LfWAQNN6py3UG2Z0LV7_bQIK2JC3OhB_XTOQPPqQdS3bY2tmsNio9BXD62seTYb_2JTkRqD_7t29muJBFqqs-GgcmDwIuIa5mVxJyoFZ52kLm8DN_j-LrWxOfG-Z6I-Ue85-avrkorE8Ul4khjle5Ct_MYFmUaFQ9Qr66yZQMPManAlrJKRIGdldGgYnJTHb7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=CG8boF1If5ojts5leSf2xXXobtWVdX99Yf16S0W5yLnf7qlMsUrC8CUaVdS9ZnvOQ6QN15tQEk23HcVAT3ecIUCnm6jjTlNRV4P1D3Kz9U4R4LBnPBJWDq1lJvm7J9sJFVbzYftFS98tMfs6WzGnpvN3Z4jOfjklT69eHGQ3nMCQBAEu_zqvTHxp3bHYMdaxAo1RA1ShmN6xI5t72hfPuIMhAvTvX1MbXTCcICEIhT89-Igxc5cZE0MCKxFpaMGdtRi6bPy2CwzfKl7wN75VDRVphmWlPSd3FwaV3fMeAFwqSBrrxyjfT7QSiFGme_9kIL642HOcyNvqmY2HOEgazQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=CG8boF1If5ojts5leSf2xXXobtWVdX99Yf16S0W5yLnf7qlMsUrC8CUaVdS9ZnvOQ6QN15tQEk23HcVAT3ecIUCnm6jjTlNRV4P1D3Kz9U4R4LBnPBJWDq1lJvm7J9sJFVbzYftFS98tMfs6WzGnpvN3Z4jOfjklT69eHGQ3nMCQBAEu_zqvTHxp3bHYMdaxAo1RA1ShmN6xI5t72hfPuIMhAvTvX1MbXTCcICEIhT89-Igxc5cZE0MCKxFpaMGdtRi6bPy2CwzfKl7wN75VDRVphmWlPSd3FwaV3fMeAFwqSBrrxyjfT7QSiFGme_9kIL642HOcyNvqmY2HOEgazQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBe2C0Pn7TZhBbyC_pBhl3j-uxAwNBi766EaTXPtPmPOYEtjhtVcPA7JsXD7SQG-Vmja72E_D_jB25cwdCHN30U4Bo_sEtLbw6rZhPggTkdehYLVme5IPIJ_c3kQIiBuYuiYPI0-ZwEhaLhLkUlQGelhpipiuyS_WiyqcnWVEx6WKpt7FvmvWZOUiM3oKyh325GH7SjLKz7Auu7Ewo4sM_B4e0zMj8w0cbX3VsJvjAIp-b-R5dFjjg6Sv1j5P4u1YkoeZUpV9oWUrK1NiVRg9TLnTpn9cmhqJh99Lsc4B0PM06H6zSE4WSRaUGttiqb_84E006s4zRoDQ8pV4wD0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClqnGkretcKI_Fsnv7Fc148QDPeQbA7_Ox8bFVuSRqbe9bhGHK-k8-WLBKod-dQLhiIGfzpwY3G45ZVkiPjs2mQMZAcV-9fVbKKN4kw2M_A4Xxz-U7sRMmWYgMwJEJ5mFJ6pAHChKF-3vIHfjPJDfglqqDOS3VKIfMqF_P-KKee96bbXpPK4ZFDghEIiaRCsNTCA4Us3npiqCj4CmC2gWSH0Dag9Vs3wxjnERVr1mWMWAoKk8N3nqvyV9WUgTpi8cet1CuKOp3k0QrP5XcXZsBQG6Mmm7REZzibN4ZrRBjPTrzCDtHXQb9gx0GWxSNBpfdQslPU0Ktw_MDCve8kmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=kA3i1E55VDjgRpmUWCuMI-17NMG69KhFJkaozDJiAxcRSpYvK3hGEivskVJfUXKU_Dn-PHKM7TQnY_yEGTrcSWI7aAD5PWnB_S5_pbvMpnckjqRy04wP8ShmsEb_vL7qs9Kl2fn3Fqv9L02mVxWtBUtnanFtY-Qm-xrVPcG44Y4-VYH3S8rm9GjMG2_AepZB-cHFiFsqclap1IhyHDa14IQ8hBU82j4sbp_xRO0Y0ejHvTb2jrFwgPjchBnLUn944YF24NwDfbbc3wwx9BUmKxf64pl5uu5DtvCBdzSH99d7HvE9W0ncjUgX4CtTBLD11ZldSN8YN26bBBuy284q3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=kA3i1E55VDjgRpmUWCuMI-17NMG69KhFJkaozDJiAxcRSpYvK3hGEivskVJfUXKU_Dn-PHKM7TQnY_yEGTrcSWI7aAD5PWnB_S5_pbvMpnckjqRy04wP8ShmsEb_vL7qs9Kl2fn3Fqv9L02mVxWtBUtnanFtY-Qm-xrVPcG44Y4-VYH3S8rm9GjMG2_AepZB-cHFiFsqclap1IhyHDa14IQ8hBU82j4sbp_xRO0Y0ejHvTb2jrFwgPjchBnLUn944YF24NwDfbbc3wwx9BUmKxf64pl5uu5DtvCBdzSH99d7HvE9W0ncjUgX4CtTBLD11ZldSN8YN26bBBuy284q3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDn5S2Lu9EPmnzgUqBlMKfuR4Ma2KVWObjMaphV_ZjT6XMeUpFNN6WmJsr-inEY_YS5TTqkYjgclIp9hBGg_wMw_yKm_qIXiMQQ5Gr_u7Ty2zammkGV8Baj7hywybwKNtroQayxkNs2KUEY8D2pycN4Kmp-yW5BEMWrl7KgS812Vj5ySNPGeLHD0kB_0APp4BK47qJCyLwYWaGpgdprhjE7qIYiEuBgjh6FPDPml2D_6IPiGAZ8IfF_BH2PLcogyED2Bvqpl-OM72p-YrkCLI-PNFF7LvvNKql-uUV4IZgC-xSeAI4mfd-j3dD-5oDlsylReWvU0qLQWxkw5upjCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-jBkVwcOIJN0gtFiwayfiHIL2OqMJEC9YQdjp3xHLeY382e46BJ5siUM41aYJwszByu5pe4u6x6Px2vIl4InXJiFkbN3YIeUtvVOP5viAUoVEQlIJ7dHqRTyBkoLy9NDqSBL0RZFlHVsGu_lVDQCu6mWy1QRnGw663PNzfeSZAVIdCetV4bYRdux80UDC4-ZdNNMgYzJ3Zn1nV4wHGZ5xVo5z0XLhSz2Zxd126f2ToDVvikEL89ISFSBc-gB4cMHJbgN82CMcDHDxlXaEMrLR1wmo6kYUz_aGdc8Y8icou7xX9TlVGpop62stvfrLyPzkMFiIqhvzvry3SLmu61uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG-z2wdYqYCjYy8vd0gXUuy0YFBlmElIFm7Io-HKojZVHTF6ltBM_FinNizMpbQ0BB69CuclfPrEDOoHHpBnuYT_lQ4oJ-GNHFuTu8raae4L3ZGg6oqpnv8ZvbOoS9qL2aggu2XWORdjlN9mMlCZNslnFPG7kYXgsx2_6DG-DWFO1HkYsBD39EubUCpCYXqW9EVltGteqwX5U_XnRA_7ovjxnYpNmCfH17gKNbPhQsHu4dqODaBtdmtx78Ei-sNQRt6_CNUVh4aThEjx0ihq5XsK8GSVawB2EF67t2lXPGoi4hEMBZeEpQtgOGs-Qv26TfhMpHQW333_v_XEYuPl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=Sa5P58iLbkHBDfS2xCHXIbuV_BfjByq0ShCZLSawd_m5XLnh9RvrSAjW9NhrmiC75gQWEyVB94DG0ZaOptug8USFBikgNfexmXZDWr7BIgQamAnHvWwL0al37HJ2FG0ILj6xAPkWudyftb4MQgkHdp20T5SNPCx3glIGr5TjdnXHyhwa1C0wD9_sehogS-9Sh44JW0mdT5Y9047js_nqaFQF7dX4Bk3T-ysj5GClSJCrPwuQ6dSSqNosUy27GQxp3BI2Qb12QmuxLQ9CBO2Nxt69PJLq-MBVCEjWhR74pEPKqOJZuYtXn65fdE9BOod5pix-KiL3NpMtT0Gv0r1XbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=Sa5P58iLbkHBDfS2xCHXIbuV_BfjByq0ShCZLSawd_m5XLnh9RvrSAjW9NhrmiC75gQWEyVB94DG0ZaOptug8USFBikgNfexmXZDWr7BIgQamAnHvWwL0al37HJ2FG0ILj6xAPkWudyftb4MQgkHdp20T5SNPCx3glIGr5TjdnXHyhwa1C0wD9_sehogS-9Sh44JW0mdT5Y9047js_nqaFQF7dX4Bk3T-ysj5GClSJCrPwuQ6dSSqNosUy27GQxp3BI2Qb12QmuxLQ9CBO2Nxt69PJLq-MBVCEjWhR74pEPKqOJZuYtXn65fdE9BOod5pix-KiL3NpMtT0Gv0r1XbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=HyZY4VrLgMTwTU1pyrg6yLiiOOeMbqJU0WFzMmyNJ3UG-W787DRJnE77LVT9Bp7w2mKyDCVLGUka_0EBYk_gGDoveCR09KJrRtk5zptcbOWYNXRdZHzzc9KLHq5y6Ue-3GL2Iees5ZJAB0XP49mzBOEWeCo1ymFGTO380wNXOnIO0l2vm7Dqlz16GLoQryh5Z1PFNllro4fE8K6sASTBWR36mBd3N1a8QaUKOWk7hMWv2_tLOtq3HnUGTextEXEvgmWJuuZ50PzD9ozZz4PyDip6ZTibix8P7-Qm4Oy_C9LQyPT5gO1EMMcsfx4gS8RMfwzBUmFlW1_tt8p7W6ry-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=HyZY4VrLgMTwTU1pyrg6yLiiOOeMbqJU0WFzMmyNJ3UG-W787DRJnE77LVT9Bp7w2mKyDCVLGUka_0EBYk_gGDoveCR09KJrRtk5zptcbOWYNXRdZHzzc9KLHq5y6Ue-3GL2Iees5ZJAB0XP49mzBOEWeCo1ymFGTO380wNXOnIO0l2vm7Dqlz16GLoQryh5Z1PFNllro4fE8K6sASTBWR36mBd3N1a8QaUKOWk7hMWv2_tLOtq3HnUGTextEXEvgmWJuuZ50PzD9ozZz4PyDip6ZTibix8P7-Qm4Oy_C9LQyPT5gO1EMMcsfx4gS8RMfwzBUmFlW1_tt8p7W6ry-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbSoLlzfUtt_jh2VKWQIapslNSqDen1TfNAhzX_wliy_4F5mxtnVy_Wdff4066cP6XhqNidzRphGiyRBR-NxEFqtRUXykaVJIKVSTRcsQ22Y6y7y8TFrVEI98JriAanA1Do7e0b7SPCXzmRaDG80KLgML5VCx8IkekpiNyhEiTbddme1swbuKsT1j1LFKmk9FpeDe2l5qXLojp1YjjWnFwSu_V7X4_CoPrYLmzV44E6YfF0DFEZfuumdWx40fuOWWg0h7-IJM6yrcRhsyTrv_XowRG2IfDCm-4mtnDhKCjSJfKXMpdf3fElRdgHNh-Ufv_kwvdsfWt6JAlEL4pIfxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrEH2EJc3k23yQ42gjJySRJSWXtI9TgUN4JH07-o9c6L2gekFQkSCG6XcTxPsm5Pn-WzV8hLh6wcnLqnWrjIj09Ne4Yv5aOAh1bAsyiRBnyEFyX2Kmtpv5roRld3jN9V7mn63xkOLUgk7QoXSmB3jCOu4kP-bTkxe0AMX093Uw3vO2LmFcd18qoqyyQLt_x2OSzLgfQF9AXzGl53sSmYejW-iesnD1_zjae-ChGqRHK9OA3Una-RaFzLfCdIcn_P1twcVUwjXtLBhG-nhk7GiaLPDiWtPnTwEhfjcUtbTSnkUfTMiLTOdu3aSG3iHLwv1N_LLkIu6wQ585jZBDkQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6bPBVH5qkDQb6kyscAFCe85uGt5u0WEfOovfsWk14TUjSD3bto66wgSVyQ8_pkTwna4yE7oe_tmE48_nWXt1Ma66M9Rv8IO2Br4Ouifl8rjq2RSvbLPCGVhfhcI5VxHjNOhySG6O4EtQrLdUhxmHeEZ28-26moWcfBMdeTrCF_7f--Y13EK5yaGyETtiTM9FP9eOeUSM62NqR3MctGySV1ljzGCw_WK4-7PALLxNlU_qOGjqSS4bJ_cogNeHVn37tGYQcARif6VHWK7htbIl-znNbKZRioEH-FPUYoUzupdQ8tbLNas4X5HnTE2hgi1Q4vq6Mg2YXCVsEpLXrv1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEQnArIcstIlM_q1bEXUXU-uexakY8dHXyWCoIn6P0VQHzF1-t5NVQookqfHf0KYg8orbV2X17840XZlynf_WjCuIQFKpUAhOZmliaoHafMnGG22sX6P5K5i-IZIsvSn3BU4JRptusMx38I-vaahgBmaBiGox7YHdgnpgOA2y7_j2A075u9UqSsiWUnGFTt-IxdndSu46l7_6wbWtuX7zz6vu7A0k8fqReOknhTUSbfKexEZVE1hIz7sukPZyofuILbof_30I7Y3RyV0XQWe3UIiitqoLNi3CtawtbRq4gyrFvyDj93NtK2qRCGNEYPQPmGGqbr5cPEzeXPIQmk5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrJWy0Cg78VWbWW59Nf-EHov373ucmW8rm8QzPgX3jk1AErR5PS5qBCMYA1pVMcHlRjveIZPZHRrfVn5JQWUgtpsQAam_XtcTE1UWxkMtWz3B3m4m-s2BoP3ZqiY1O7LSHm89pLaUKSjFoBlKN76koWFmoh_AfJftMVCcDEQZy_aebAt89seYWeFqmqOK8npO0g8kKpkP_QerXFjWFq_BiUnLA2-y7k7qBbs_9e9b7BGVzp9i2h8jlP38G9vrU1imLFG8OLJIi31y-kn9IUL0GkRkO_mT-MXOkoqVcwdMi-g1qX-TCrHCi9FudjbqLynUP_g3LtsAo41JycDg4H23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqNhXr4TUa4Q2C5faPSPPPXcOFRZGVw36hEkLnFgMC2izXDX_-kGfu-hMjBCHHsnn8OU9mD0EputmK4MBui60P7YJzruOmS-pLj0btrQdBXc6a-5Bz8DcIAf4azlUMwCJph0zl1bt256QZcbIKkCAoVBkYFw5n3D4JnhbllA0UDnzg7tI0-GQ6Ixr_FaESbgKwFmpO5Kr9WJWzT-za_WpVhdFn-5Q2dmOAZWgp7rGjK3aFmJE4-YS0ORg10BUauWogaE6E6s5EJkdaRQekZJC0y3o6Hu3XFOLiVvybr0sxZsG7dZU7Q9QqXQDERzliUYPlgn7w3zHC7i7EV5YFUrqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wx03RlWWEBO0MdzISvUysxCNZZw-MWsuOuxaGHfFBMXuPKhB5hVruDJVgV_LQE2gM6ad9E84VgJZbzSNSIiPzM89ocJTjeEPX0zs13A8563TbvWIl39S5MnMLz0SNZNlBeLszrwb4mgEvFr1aUcj9CSBL8rPJeu6LVPShWYXkBgKrGntZN85x207VlRL15qV9ahykEkeROOinvI501j_UC8eWVPTCmITZv2hqdhKwGyqnlaKHq30sAl2MRBXS6PTKjjuNQVwU-d1mEybzBrPQ57T480iwJiw14H0fLBy0WfNRS9Rp66HHEFAbbODDq4rIIAIlMril0C9_3qb7j5YeA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=t-iaHb-mgUyb69i69fJMGJxpOZud5os5IiUaq6QH8NBnqaQEvj0ZTPfa4AtwT2k2mM6nsfHjg4aMw15vj9R7TvwIjyzgzYndaTHMdaFBYW0XJWWVxfRPzVggwXPvuQdIeG6kSoeBPEv3zq3flEIl-HabOn3vFiLkSmXQd3AeNWMtm24mQno-Kks4mkZvksCXHBvnSxb5_O6EVOi5UrZT-IjxdnocH9recopNfd5bYFxJic8_hMBiYoY1AoNx91mmrwLICJ6v7and4W7jwRd4btybxR3d-VksYX46V9TmttUsGZfYhjjw0aLt9JSQLfK3R4cQMTpjSkPJI8zEAziuLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=t-iaHb-mgUyb69i69fJMGJxpOZud5os5IiUaq6QH8NBnqaQEvj0ZTPfa4AtwT2k2mM6nsfHjg4aMw15vj9R7TvwIjyzgzYndaTHMdaFBYW0XJWWVxfRPzVggwXPvuQdIeG6kSoeBPEv3zq3flEIl-HabOn3vFiLkSmXQd3AeNWMtm24mQno-Kks4mkZvksCXHBvnSxb5_O6EVOi5UrZT-IjxdnocH9recopNfd5bYFxJic8_hMBiYoY1AoNx91mmrwLICJ6v7and4W7jwRd4btybxR3d-VksYX46V9TmttUsGZfYhjjw0aLt9JSQLfK3R4cQMTpjSkPJI8zEAziuLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=T1JI4RgLlinn1geJhBMSazfhO_XiWNY2eNX8PTPFvgd6DutsYE0WD2dDGE3c7sGsDvsDB8dwbGOgq4ODLd16FWfWjBKKWNbMk3IL5iPWMh6H2CWa2OMPzaDP39cfVO2cQoO9q1NBZaof289eUkV-5lV-FPDbSuXI3cgqf3udVzVyr5vegpmt7qWAb8gJynt-09a3cBLqAOG4w_mtGlLQznjYowoC0nVRHs3gX5nqQzNc9C-6VvgugP8ep5e_dxZX15C-Nlab-pyDAzPZRhceHKUpe3oTQqOdXH7r8PRT0diehySUls4ZHU9cqnDy1MpJRPMYz-V5U4SAHGOzy4Nlgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=T1JI4RgLlinn1geJhBMSazfhO_XiWNY2eNX8PTPFvgd6DutsYE0WD2dDGE3c7sGsDvsDB8dwbGOgq4ODLd16FWfWjBKKWNbMk3IL5iPWMh6H2CWa2OMPzaDP39cfVO2cQoO9q1NBZaof289eUkV-5lV-FPDbSuXI3cgqf3udVzVyr5vegpmt7qWAb8gJynt-09a3cBLqAOG4w_mtGlLQznjYowoC0nVRHs3gX5nqQzNc9C-6VvgugP8ep5e_dxZX15C-Nlab-pyDAzPZRhceHKUpe3oTQqOdXH7r8PRT0diehySUls4ZHU9cqnDy1MpJRPMYz-V5U4SAHGOzy4Nlgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=Fd1_bq5gkkDmW_hKRxqFUftRBBGnLPjHoF_h5QIBrgugUloJyo3Ceflsrbp0EAikYjo0EgV3p_jVogRoFHLyGzUcCxzEGJHSss2r-yqVkXA8GUkqlJud0eEpNvE3KmQ0kU1zmOn770TpRARwuSumTHub1T8TfBJuv_9lmmSLNWweGo-MG1APjG9Hmnf-wm-lJ_DPFBMkCw03J5EXTsP6CVqIfx96kq72Tz345DHjQvpOxnkgpakctkur2312pWvc0QNQLNsWezPmfMew3CEcEh009dQuZ27845yvdrRpLCqpqW6ANXuA-_m6dsrQJlO0pbLtoL_rlB8BbNS3XQ7DNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=Fd1_bq5gkkDmW_hKRxqFUftRBBGnLPjHoF_h5QIBrgugUloJyo3Ceflsrbp0EAikYjo0EgV3p_jVogRoFHLyGzUcCxzEGJHSss2r-yqVkXA8GUkqlJud0eEpNvE3KmQ0kU1zmOn770TpRARwuSumTHub1T8TfBJuv_9lmmSLNWweGo-MG1APjG9Hmnf-wm-lJ_DPFBMkCw03J5EXTsP6CVqIfx96kq72Tz345DHjQvpOxnkgpakctkur2312pWvc0QNQLNsWezPmfMew3CEcEh009dQuZ27845yvdrRpLCqpqW6ANXuA-_m6dsrQJlO0pbLtoL_rlB8BbNS3XQ7DNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=ERi8VTNK801Nlh03kNm4CA4Q83yGYOYjTKBkUitV-6PBAQJ90A2Gcn0n2601-__PVoQQpJtJ4IHM0wnZ7Q0MVUsJbLH5JKwuvKMaJdY2k1911TzUB7uKZZKNC6F9QH-z0Qps_50O5kf7rPlQaPkjfrJAusTnP6uJKEFuFYkNbdfGdxRCPOn2Vv0CiTUmA6VGFRf0sNBYXR8P39MuCV4XgzyrV236WB9DOXGVBv2IXfDUNldDawQ6JMx2B8hFur9Wif33iNJ26udbHG_T-t65FGJNORUcT3B-JK85pF6OJwuk75trmRWEX3RV6kKKanPmM4N844w3SIOnY5gxtMwIVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=ERi8VTNK801Nlh03kNm4CA4Q83yGYOYjTKBkUitV-6PBAQJ90A2Gcn0n2601-__PVoQQpJtJ4IHM0wnZ7Q0MVUsJbLH5JKwuvKMaJdY2k1911TzUB7uKZZKNC6F9QH-z0Qps_50O5kf7rPlQaPkjfrJAusTnP6uJKEFuFYkNbdfGdxRCPOn2Vv0CiTUmA6VGFRf0sNBYXR8P39MuCV4XgzyrV236WB9DOXGVBv2IXfDUNldDawQ6JMx2B8hFur9Wif33iNJ26udbHG_T-t65FGJNORUcT3B-JK85pF6OJwuk75trmRWEX3RV6kKKanPmM4N844w3SIOnY5gxtMwIVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=Jgh02nRf-uHH-ijq2kJ7mRtaZqwbUOoY90eyvMZuxlWgzVZPwUgLXxXGwkUQnHcvmaGQRlO-FeI-cdw6fEupJB_EdWx-DWYTpYv-_OpgNXgpnxcH9BB4oCpfAOcMmz62D81vEI7LF1VR7tNIN545q6Zb4gCVb6EbaDUphbKoZrKiOSV8zdNKYSPKmSaGkHz4cvCOxGROBBiqcna4qkG_wy-yfYWajOc8T2iUIQdXS7HK8mMmmy1d57MubkvI-t7geCn2dsO9cpjwI8tvMwUqkl-25n16KMrf2IXsDDW_tFUG898LrIJnbHHikphpSjMJQMRe0LtUeoZ-QEI6WrRPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=Jgh02nRf-uHH-ijq2kJ7mRtaZqwbUOoY90eyvMZuxlWgzVZPwUgLXxXGwkUQnHcvmaGQRlO-FeI-cdw6fEupJB_EdWx-DWYTpYv-_OpgNXgpnxcH9BB4oCpfAOcMmz62D81vEI7LF1VR7tNIN545q6Zb4gCVb6EbaDUphbKoZrKiOSV8zdNKYSPKmSaGkHz4cvCOxGROBBiqcna4qkG_wy-yfYWajOc8T2iUIQdXS7HK8mMmmy1d57MubkvI-t7geCn2dsO9cpjwI8tvMwUqkl-25n16KMrf2IXsDDW_tFUG898LrIJnbHHikphpSjMJQMRe0LtUeoZ-QEI6WrRPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=unu7GX1r-hQSE3TBGe0ybvGi4L9ou0x3Rq7J9wDHBWk1UQq5dVqrVOTEQR6JzpYCfBDrxpQDi4xYVmPLWJYkMzNAUSTblafctlqL_DMpq9YmdyCv4xBO8YYvi9AyLG8vh_1yxGujmI86UwK9CrDft6HFedpMiZvdUrsiYDAbYB9oaPZE3RRuxMzZRl6bRV5NvDjl6ACj7zX9ZNjyHWlICpWYN-Ek-US9C2uAcm-mxzN9qLBCGDOsflHhvlg43706jX8Lkrvw3vearJMarhV60uk9XlDN0whswO5Nq6r5dJJdaA2VXwbSvMUAzSXdBmP3i1KDsoNJwQBXnyh-zD0OZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=unu7GX1r-hQSE3TBGe0ybvGi4L9ou0x3Rq7J9wDHBWk1UQq5dVqrVOTEQR6JzpYCfBDrxpQDi4xYVmPLWJYkMzNAUSTblafctlqL_DMpq9YmdyCv4xBO8YYvi9AyLG8vh_1yxGujmI86UwK9CrDft6HFedpMiZvdUrsiYDAbYB9oaPZE3RRuxMzZRl6bRV5NvDjl6ACj7zX9ZNjyHWlICpWYN-Ek-US9C2uAcm-mxzN9qLBCGDOsflHhvlg43706jX8Lkrvw3vearJMarhV60uk9XlDN0whswO5Nq6r5dJJdaA2VXwbSvMUAzSXdBmP3i1KDsoNJwQBXnyh-zD0OZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Aa3Cfzl9zt4nJb89bHa-zkLPH43UawDNtxLwHqvoaKjJPsO5ewWHfIQGMAtEyAvI_mAWrZoBZGi4rq22nP8XUebS8gICjK3G_HozK9tZ5GyU1uHN_qQjvJJL3kKtVk-f9IogfiY9dbywOk2fPOJNrrY6mr6Sz_P9q2w3RlvJc4bwx2OayHp2EX32oacTezr2mYfZqdo8oNXKibF7zb6RAOELuSI-I6nU3RZgiYZstcKEhvtg93rnJVopg2dY8yeeKWETTd5rUOV9ezOVh--yzBW0AL0MyFoIhqUqLKXOcyunKpwcVbdQDMSXuhYyRn_Rk6JKdoiZ55hHWNOGZYr2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Aa3Cfzl9zt4nJb89bHa-zkLPH43UawDNtxLwHqvoaKjJPsO5ewWHfIQGMAtEyAvI_mAWrZoBZGi4rq22nP8XUebS8gICjK3G_HozK9tZ5GyU1uHN_qQjvJJL3kKtVk-f9IogfiY9dbywOk2fPOJNrrY6mr6Sz_P9q2w3RlvJc4bwx2OayHp2EX32oacTezr2mYfZqdo8oNXKibF7zb6RAOELuSI-I6nU3RZgiYZstcKEhvtg93rnJVopg2dY8yeeKWETTd5rUOV9ezOVh--yzBW0AL0MyFoIhqUqLKXOcyunKpwcVbdQDMSXuhYyRn_Rk6JKdoiZ55hHWNOGZYr2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QybvlCGUvHQPEjyQ0wZS0frhPl_Bv68fgBXT1JsPoZebMnFMqxj0u4CkhMOierFLV2oiNE-_ozaxU0RvOh0wZ68TWRhaEGH0SDn6gAFABivF3wzycLsCECzTPKxJJyrzW95drtqYWV5xjNIJZu9dqgmWgglOfMhJTk88bGhMM2Or8uOg8z4sbZbexwoqD5hnMcI-bRqMm7oES3vmWinCObcc3ZQb2weS76BPn1J--siP1qKmh9zgsNaq7zfB0ikYiWG7pbLLcY1FHaIeTBR-IPfEfrE_8404Vd6FYPpQ-guao4x_D5e-wtm8B-vNJnvMiljOoa88qF2NOy9JbELK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=g2E9SGtgmw3TrcRvSFXSPcSRCniM7zQirPoMaF7k9pbbGXV6AOOojgUmu4ZPB9Az_65UB0wAVMoQbJEaqZ6Y2WXWGUv6AuU2vmUzTnqcPuzgyQ0ytnG3ecjp9eNy_F_ZNbKL7Wb-xGSuZATguyj6teJoPzc1mPQ6krhu6R0LBug2n05yJhyIQWDFXlt8C0xZThOUP89Vo4Gn6A2xEcnljGuM6Dq69juedJZSnkc0MbPmVBNBHc1Gwia-uuihnPW3yILBdndAs-9ydDtxLCSTs3DUfYkS83EAg77UA_5SqLwulBo95OQN0y5CkBv_uSCyVNXc5WWkxwCUFE9CeNEREQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=g2E9SGtgmw3TrcRvSFXSPcSRCniM7zQirPoMaF7k9pbbGXV6AOOojgUmu4ZPB9Az_65UB0wAVMoQbJEaqZ6Y2WXWGUv6AuU2vmUzTnqcPuzgyQ0ytnG3ecjp9eNy_F_ZNbKL7Wb-xGSuZATguyj6teJoPzc1mPQ6krhu6R0LBug2n05yJhyIQWDFXlt8C0xZThOUP89Vo4Gn6A2xEcnljGuM6Dq69juedJZSnkc0MbPmVBNBHc1Gwia-uuihnPW3yILBdndAs-9ydDtxLCSTs3DUfYkS83EAg77UA_5SqLwulBo95OQN0y5CkBv_uSCyVNXc5WWkxwCUFE9CeNEREQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtWcjAbf-p5Fr5QskGr-zXQASDEljoRbDtmi07rw63-KStwMOAsXIscunlNzR1k6Pkk2XnkivlXYbbN-Jhzp-MfMNiVDjuqRTwFa5lBHb5a_Zkuct-YUj5PWFKI-YZj5GWIhmSsJSyoWFVyHQeba-DscHQtuDk6_T6gPyAT9iJs2bYVoLYyQ3WZTr9cs5zvnLiDRx-Bt0y2A1FEBFSXN2lOFylItr4Ee2isAZ3LaXRPCGR_ChWAAaXKxJyoost9jGOPglr8hEtlrdIlHEZwI1g3r_civiwJ6S3UuTY-LeGrqIFuvV_OanoupkH66efEwVXR63-oJbc3gPrgyawFWKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgW0_poHYk7J8lsGA7lq0ZmPzYp9ZWDzZ98nue0Uc4VyBxvNTpXRaqGVvS81OomyR4QmdRLWPNli8l-QqE_7kwtabuYk578arC57sMquJxgYPFBqbiRbJgQcSdaAjJrobtHmZOokMY6owy9DqQs9PXZJT14zPtKto5szn8dfFmqyIx2swvUGhzwsSG_7NuETByW35bSQFEVivi2CfX8O3Cff_ESWIrnHSDdj9QW1nlFnkR7yp8yxwKcuLvNp8Z7SdOVZxeBIW4JtfETJB6c4RALYn5KTm6FqopnLljmZOw9r6_CVU7kKDOhcRTMR-8Z6oLMfbVp8OH5YEzWdjU82iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-mcvAt6JgojiHXp-KHhfqjwHGFAeIwvcLd61B3XyYZ-w9cvD7NCCo6pIpYauSBePLtRrpnWQ3hgLoQC2UI9g5WYbRK8BUCq-Vz2Z8EqgvOkjTrqPboYLIzySAuHYgYNoi80EDbcfisvB0-_Mknt2Y1JsGzsyP5S3clHMmO8exXXeJag_F9R0PwLjj5Jwr4a0_sNK84fdFLFieDdY4KQ9QnmUCH3HFQQV5g2afujRxyw60ZD0-V7igK6-fApDwsIeL_4th8lQ2Qe7dVaIZKohFLRCQ1t-bU4ECo8WoTTwhKQHjQxvkInP6yzwC5erkHc3BnFQNL3VifAn6KPd1hDNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJZccOL4QhmculFvXXQY9Vm9qAY4BWQNn_7hPeWC6PFKgDMompsqCti9SWOj_QEKuzBGjnX5i5hcSzzVF9kWj1TvINdd2WBoYAsYkYu4Seqmln29HYdGZiCG8U8QS6R-B7Rc2GpxNybuR7uROgdW1QnVbdMLEDxYf_WvZehPkUiamJocdwLJRecU1J8YJocNEGoXFvnQFEbROP1XSC49U83diD2KrcPXaQONWtQ9aOlzbDxrhM4UDlHSkpUKDhVSIaN3qbzh-62n9W-dbIGmiqIMp_BxmXCY4dG4aKQVRfdAz5Q3L2lNlRpYCIZaNSE_YKAf_eHvp4pFpsdpJzTAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=tJ0u6De3QmdUQUd5SdnS0HGlJPz8k5KNGDWBhqBeUCaPfibdDM2ItbU7hVhqx5Mx65ysla-NTF4g4Cd_6BlOytkqrR-mBNu22aUnWhv4xrotuG73HOONLEUtJVBNr18bkJ7iML49QATMH2kElomWTa8ax5yN3nH9Fwk5slc1cqVuVe-iachPPaWpuDifA8A3TNlsZhyfTre0mGaOgvwrrgADC5POgur2QsIaL4evVlfleHCbJQJEbHJU--PC9i54mAWQqUMTzQluEMmIbjs7cQswCMkEEOd_858uFY-8ofC_DVfT4VekuAXr2Aj4lL1geOM3WsxrJhZL9C51MxjWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=tJ0u6De3QmdUQUd5SdnS0HGlJPz8k5KNGDWBhqBeUCaPfibdDM2ItbU7hVhqx5Mx65ysla-NTF4g4Cd_6BlOytkqrR-mBNu22aUnWhv4xrotuG73HOONLEUtJVBNr18bkJ7iML49QATMH2kElomWTa8ax5yN3nH9Fwk5slc1cqVuVe-iachPPaWpuDifA8A3TNlsZhyfTre0mGaOgvwrrgADC5POgur2QsIaL4evVlfleHCbJQJEbHJU--PC9i54mAWQqUMTzQluEMmIbjs7cQswCMkEEOd_858uFY-8ofC_DVfT4VekuAXr2Aj4lL1geOM3WsxrJhZL9C51MxjWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep-okB8rQ8pkudL_MXDJY7z2JrsGKhnytC5z7_IBb6EgN829zPdfT-iMQ_aV8pk5sIYgSaBMmt2zidIWjS9O5P_NrGtSgZF9rg599k68Zh_jJyMRZN-owejnwDB-7kjWdw_eS-KAY36m6XGai1l3YHhiwMmmXDR38Ye9Cqqj2KAAcIKS4zMpBoRGU3dQU59lqHTMq0EtFiJdTLHrVELnsTWN1qn6TvUcRegV51dtDC4CnnInjyVGkMnc9BNHD-7E9Rg0aYZC_t6_tkUUO_lXkQ-E7kETuAON6BADCDiLMxF-UHkw4NjjJyq8GqDoBIhV609TOVvIdilCkPMkjaUhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=QGD-NIHLpfCbGjvzCWxaHGZZJz0GxLTK00kc-EqShnCvhCGpNetAnFGtzQmsMq-9YwypXR8GkenzHLGJW1eSeMURZrdHOKXHXYttRK1owv3V0ZwUN1BUlOKnsEYDbRfA77dIcF9HnIVBvSX3eQu8pPkkV2ZH281DuQtQc7-Q0tHxYZ325T7pBqHj1RjEBM7fJt5svmPSs4ZL8JfNDxhZVKLG-9vVGmzKqc38DM6z91vPmlS_nrW1mTZ2620llCKtq_O-PbYt53ejWxwVsoTFu8v7okJHWCxpOtUGdvEykeefXmR-cyAG1bn87Geco6kSap6AqabBXO_ceJ3QldN33A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=QGD-NIHLpfCbGjvzCWxaHGZZJz0GxLTK00kc-EqShnCvhCGpNetAnFGtzQmsMq-9YwypXR8GkenzHLGJW1eSeMURZrdHOKXHXYttRK1owv3V0ZwUN1BUlOKnsEYDbRfA77dIcF9HnIVBvSX3eQu8pPkkV2ZH281DuQtQc7-Q0tHxYZ325T7pBqHj1RjEBM7fJt5svmPSs4ZL8JfNDxhZVKLG-9vVGmzKqc38DM6z91vPmlS_nrW1mTZ2620llCKtq_O-PbYt53ejWxwVsoTFu8v7okJHWCxpOtUGdvEykeefXmR-cyAG1bn87Geco6kSap6AqabBXO_ceJ3QldN33A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=Wr1zkRvi-_b_a9kxRxOIfQYb15Den08DUSP-qybi6WUrMPkFpTLjCmH1gVE_JzvEiEzNmfUbmSPe1Q9Oek5oTQ2esvIkMb3ka0ITHWGsLzm9wRonNWFv71cY7ythjDpbHnh3bcSTsV21PcPd6koM6IgSiGYwQedAHLKb9sZXKYqgH4jPfLf7ilxgkmgZSIIUayftm0AyuOz6far2mJGr8R0oGJMWeFoHFdG_rrv6kvpubyo9kY5bqtO5Oz5YS2--MTfpEFmWxlGPDeizjK10tOXW5wj3ypUIT6QZo3BMaW2dIBSe5lHbZiWK6Abp_Jjp4zGriISTKyfuk4fJFhqnlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=Wr1zkRvi-_b_a9kxRxOIfQYb15Den08DUSP-qybi6WUrMPkFpTLjCmH1gVE_JzvEiEzNmfUbmSPe1Q9Oek5oTQ2esvIkMb3ka0ITHWGsLzm9wRonNWFv71cY7ythjDpbHnh3bcSTsV21PcPd6koM6IgSiGYwQedAHLKb9sZXKYqgH4jPfLf7ilxgkmgZSIIUayftm0AyuOz6far2mJGr8R0oGJMWeFoHFdG_rrv6kvpubyo9kY5bqtO5Oz5YS2--MTfpEFmWxlGPDeizjK10tOXW5wj3ypUIT6QZo3BMaW2dIBSe5lHbZiWK6Abp_Jjp4zGriISTKyfuk4fJFhqnlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7DSZjxNKtRBdPCsUdovnzETZwe-v8hqyi2Jb3fFovN0AzS76G494QGvKQaWt7rHR7M48YCpgKM7B6q_YWDYI60IJ3z6fSk6pN2w4IAiVwCrFE4WnzZ16h2uT5RnV1hU0Sdfe0hjsL6a0QCLVvONA1yI08VhsUsNlzEtD01KP25I4dPGh4-CPdrQuYbDwfeyiW6oa6MLTtRFooQYJcCtnE2YYAj-ePgPl8RsCdIkBt4YDwJJROoHut0U0ydmH_dwCx1GS0aDbJ78HwS-kz5gSV9B_0jMiCUctIq2LWXovehnfKQL_duI6ivUjnvIGUVenuhES1OQX62IGXrXvm4i2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rePhQjM98-j6njDx18XUQll194T7bz0wj0XQnX0GVTkDZzSi0xfi___Me_vIli_jDqBXcv7gKbTX3AokI6qHgsYkfsQWa66Hkf0vjNIe-WmF8NoqOaCmGa43HdgSHYpSk1QEq8N36WqhsAZTx-FzBLME1qSA8wkJY4kI_1_OvS5SqI6sIYT35vTne877REtfJkaD5PYTTVqxS-1-1ts_4NGqqFRv2tH9VS5cc0Qb4DpY4xPYcu5EL6GMIRsNfWtXHb6KqN8iFa33HZi6_AJiPKpqTSk1TpWE0dlUHJoV0JxzAamR3ruaSf1XJyvEAJQpMOSZFJ1cvGtX3vSxgPPTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS_rdxaP-EN8f5z5XyFBpQx5Ho4RqxcE8PGidD3_J_NPRepLmlu7S7NFWt8EtBgIiLU_sj1-v0MqENtBu7bmMGEV216g6cK_yA5dSIuUiputjyslcTn3DERBbWxkUfvSkF_Z1_b8w0g8DWAM73bkrI18F_LzidU9jKquH7WqbddwVPi3DM8eZxEPy54qDHkMeDIsWCWPpf68of0ZeGCQ2LEEeynEI6GtZB1nAuYONwoMM4yIZb6e98fvkALSDv2Px_QQN3n0XS4aXjwQ3bywuuMDoE34ZYC2_Z_GW_ylYbJ7wswpORV3PBQHXoMpSlMldB024I4HhFcSxHCzJPR7dw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=PTnXI9ZQ6xYLMbWPZ1c9nlsmgEiwZc8oO45JnSG_75HE0rOJ_xOxVrKPZc4VcghyolNfaRKg5Qs2afeXHghQEWmo5GoLVibrXZWjw65e54rKNsrnzoYqHSZDri0MpOgUXzG95qLZfF3GolNxeppJKeSu0Tf_oBpfvv8lBpv4J8Od2XfFLbS364MpFQi5HmSoRgeeXUOA8Dlw--uwh9qO0ov-tKkpt4F8g9PNmFTakzKnOsKTO9rMYWpKfFhutCMvEs3yd5ERpm1bK54EoqAM0ysckPPyEYH_ysUJluF2em3JF6mk8Yb48OpRFmAfklVQdrNrMtgl9TduMTcy52xEew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=PTnXI9ZQ6xYLMbWPZ1c9nlsmgEiwZc8oO45JnSG_75HE0rOJ_xOxVrKPZc4VcghyolNfaRKg5Qs2afeXHghQEWmo5GoLVibrXZWjw65e54rKNsrnzoYqHSZDri0MpOgUXzG95qLZfF3GolNxeppJKeSu0Tf_oBpfvv8lBpv4J8Od2XfFLbS364MpFQi5HmSoRgeeXUOA8Dlw--uwh9qO0ov-tKkpt4F8g9PNmFTakzKnOsKTO9rMYWpKfFhutCMvEs3yd5ERpm1bK54EoqAM0ysckPPyEYH_ysUJluF2em3JF6mk8Yb48OpRFmAfklVQdrNrMtgl9TduMTcy52xEew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=K7acmilzouvgZuZTr0Rsp4y-swiiw7Da3iyr8rTNxTdatIJdmKKiB-qvrmvEKnBm5Yd7IXeZ6IhNfRl38bF45uR0pnwqbaaqZ-lWuRskrSv7xdOHlqC5KCjBOEi-Rj2vjxP0uXFPzgSFoad6MdcowMBqmtwdV624g6HciKhmaFsk7-KQE9-AAeY54x4ifeKM8UEqx4xkmFSco-wHTI8c7Nl48U-aX1gi8KkC7vyJOMlH15xJzPcIwPCZewRbzlPKYIm4rCM3Kb5YZu_79qEPQEJykTh4XpKPvTAsAT2T-NW1UldCxs4BXwepzWTU6S99uJ289OFdmHKdwIIKinLQ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=K7acmilzouvgZuZTr0Rsp4y-swiiw7Da3iyr8rTNxTdatIJdmKKiB-qvrmvEKnBm5Yd7IXeZ6IhNfRl38bF45uR0pnwqbaaqZ-lWuRskrSv7xdOHlqC5KCjBOEi-Rj2vjxP0uXFPzgSFoad6MdcowMBqmtwdV624g6HciKhmaFsk7-KQE9-AAeY54x4ifeKM8UEqx4xkmFSco-wHTI8c7Nl48U-aX1gi8KkC7vyJOMlH15xJzPcIwPCZewRbzlPKYIm4rCM3Kb5YZu_79qEPQEJykTh4XpKPvTAsAT2T-NW1UldCxs4BXwepzWTU6S99uJ289OFdmHKdwIIKinLQ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpQ9aUQA0rW7NiU_dF1KwOO774qrAhzvSkgmL0-UAZEYIBgIredn2aamTaw6nc91MXWb3dxa_j4HPegLaJkAT73A4qifu26KBfcnCQX_MFQjQB1FMO0ZoOD-wpyGONcVKYyrzKXdKLyNhavOzlVNHGtsrbxTrU2L28pZujUZX1jybgcs587T9nqtcx0Ertl6uhgPWjPHY4a-WlFkKeg_9I_JGwCbpMbXMILBc6Kg4QdDQEBsjSg29Gp_fIMga6WY4VMpwZFMmpvoDjEQ0lKllq2GbfMoCTw43w7KWCi3WaK-fZI1GbA55RCDbVIUn74rThTrkvSMkwUzB4jRQEsIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVBiSCt8A5PPaEAlRkDFq2QucDIeQiAWrXfXnxTWABPL2Uc66tR0LuJT3dpu3Yuy0ZuFVlePxZ5UEwNwf7A6ih_PIQxw9m_Bqbniq9ZadILAd2lw5eEaxYLDvo1dJFd3zbCCbCZEI9k2DRUyYKsz9xe-1jE1I5H-ykKkxT7ttuRfMBfhoFvdsZN6NIA0ychHKsJwflL_P6fP3lrdsjL_oZcK0MHXJ2B_wwlX0MFgsEX7PYneZDrffLm05bCM8gEISAo_EhDP9KaqlicPTOYcOgttRJxUZ1X6C5L12yfDlcAPA6OHJgxMTxgjlgiyRJuhEX_VC3tHNZMqOFavuqNCwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsG-DGDx1Ujk7gP9CSbNy1yY3iBoOUXPPNPsFpxtO3ptynXGpCFlmb4LKJVGMDAL7ICSksbji9eofe35pH8jMK-DNZWVxHFAZcMz5rSFEQfn1MBXspXcTWh5vLozdhi4Q-t69vMcBX7qghoUlVOX709HrKrr36SHSRQknMCw-jWPE_WS2U3Ykj-S4mY1cOQXqoXzU-b7pll-gVmFDzSfE89MaG4brnhGzRp9VN0TXG-9Jt3wqWvxtezV0CdvFmYfjUXd1aOtBwR1Jb8eOGx0fQzE0GFMHwPHyKgeYZ3V4uo5a0PUP2RVu3sETN-iBUoeJ1_OoDC-2tckfrJ6ne6MNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZShC6JXi2v3ta_Gv_m7mhYrkj0yLvTShxRdKmJVTvgkhUpKzFpBYfzCRgqLat8bPI7vMg4jB1skE5sUAAvCVqFvYdK3yqqshFMFuoQYhhPU4P4bzfg4iUCfye7miiNQnSofHJ5dsAqNNfawLyuFG9DoGQQLjILdX4JUNUbLUGaZEhLUmG1U6kj55_rydjQLLI9iIoMegK2_XrRGIf5l4WxWuG883HGfR38I96mCpBnQxIDTmEjBOC-crjHAtyNGKuTMQR1ru2Fy8uGu4nq6VEoqCb0jD9cpK_C02A4hMO9mX39LQuMRUptiD2CvRFdLQCVKLVF2cwc-FqhOwuv04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZxFcq9kMkK3p7HsiHoNuCz8zIV3XABjFEaPdkGwFY_KOAqydrkjHDnFljBRF8ijhW4bCg-uFjnKRnV87jkkri31bh1NFP9cLI1VZ1zgV-s-qGvj8YKbsfIdN_oG-m1WthN9tlOCrEz1cRe2BaOkP0qDU_Ii_RXCvh1y6tQgTfTTbTlbvuzz2pWk0UiUkY1FFqJvHSP6eQaYhOXArpxTpZ09miAL-_MJvIOO8CMmvdhFaJeE27rsUQpk8w-35coV4oNTVLPWgV_mfwHrHqEnee0qr-KeDTK6QaO4GZnJ4qEMsPg1FExHMRVNrQororP1K_huTToHJUx3cleYCwynjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
