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
<img src="https://cdn4.telesco.pe/file/Qw8e_ZfkHvuaHQ1gHi0CWP0Pb0srIIKUEt51aOXDHZhCODLZKFtDKyfbq9_QjiNDkVNGFeX8vCuWT55o-zIHGi7q7y8iNaTwX1mMlwRvLjw26yu-XLo2m3VTBaL9QOJvGTzFL4zspsofWcyQtlY0wWOC2WFeH4e42o5KVzUpwfPqNHzAN1qM5dLnKA9rWwTx_GMHyiaJu1ctaimIdSUTCdrmk9mL-OtD8Vq281Z8IFhP-tIqN5-ZodlwMLxhTeqcGvmlkFc-NLhIJaaPlxEPj6miySu2VHcmEYIb0gllacCc4I2goVuUEyQ21Tf0Z_LRbiIh6vemPA6JMrGtkbd8tA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 14:39:06</div>
<hr>

<div class="tg-post" id="msg-445119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e4635e5.mp4?token=TMnUvsIA5Y4F4mKzgjMfOa_tkAYBIHXm-Rcc7m_mTWaz1cCYe3qz1qzZFuuVMIrJa_-Wmqq74HQiBwWZPAVoNO1RFh4v8C1qFHYyGyaNKhILd_k7RZScsOg4v6U8WRdHL2f8SP-cNHPlcAbt0IdSc2_MWlXG0R3vZR27pOyTO-IRkXkM1eYj1VI3ewCr36T6b_nDApQK9SnWDQLq64GHv8BcObsSjvfy3vP8dwgrwBEcQnvjUlEfpBU_ZhJN9H9Eio8JWBTdZ_AohYbc1h4oXbfegN82NVbPdn0XETHEXNWMY9OrIo-Vvg9YIDjYj3A1d3i_tSjIrHYN9YoiO0kQyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e4635e5.mp4?token=TMnUvsIA5Y4F4mKzgjMfOa_tkAYBIHXm-Rcc7m_mTWaz1cCYe3qz1qzZFuuVMIrJa_-Wmqq74HQiBwWZPAVoNO1RFh4v8C1qFHYyGyaNKhILd_k7RZScsOg4v6U8WRdHL2f8SP-cNHPlcAbt0IdSc2_MWlXG0R3vZR27pOyTO-IRkXkM1eYj1VI3ewCr36T6b_nDApQK9SnWDQLq64GHv8BcObsSjvfy3vP8dwgrwBEcQnvjUlEfpBU_ZhJN9H9Eio8JWBTdZ_AohYbc1h4oXbfegN82NVbPdn0XETHEXNWMY9OrIo-Vvg9YIDjYj3A1d3i_tSjIrHYN9YoiO0kQyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصری‌ها سلطنت‌طلب‌ها را از میان خود بیرون کردند
🔹
در حاشیۀ دیدار ایران و مصر، تعدادی از حامیان پهلوی با در دست داشتن پرچم‌های اسرائیل تلاش کردند وارد جمع هواداران مصر شدند اما مصری‌ها با سر دادن شعارهای «غزه آزاد» و «فلسطین آزاد» باعث شدند این افراد از میان جمعیت عقب‌نشینی کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 348 · <a href="https://t.me/farsna/445119" target="_blank">📅 14:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7adc9a29.mp4?token=lRc94IV_cP_HRlIQndqmIDyUunMQ9TGGGKW8UrdWqqpf6v8QpkOosWljmuM6vF5J39Z34Yyyq96d6y_seTNP0as4m2UFjoOVhh9ycuKzGJqr2XKrQgjvZbOYugFn0cgn1ljZ5UZcs6bcU-Jm1zklyK-UVLZ1ABn8Xp4gA8HIJvKTBBiUHO1knH2_CxmSk5W18qvLOXddWoUVdS7cQIFjibAEOxNS9OLyBvQA-hWU_yEvzCDCcxmnxwYqh5v3okWK3K-IUWFq8Z0OJNeOf1fJB7G1Vm-PQ_dBC4Cu8g62_wQ9RRwHUE5-ZKaRKPMlfdOWb3iBWAOgtpBqQo5gFFDJyLbsZaUVn4FDg9YCDorgD019ZKr7H1q2PMYYiff7oUF__ChoDSo31fJnMm2yDf3mkQOUBegAQwErOhRFnNQlqK1okIx0YASBUHeO1eXxg4ovh1xeLb-E2lZPvW9j_DfRKdASWBOpY6GedupQt1kEEZoGbeI52Ekab6PAHhJQATpuI8wOe0pYKqJ3wQlma82OxMDFtU0YHYl3IE0ODD14K9Kx-beBBUJwJseJfNEBLsS30u5NV_WpuT1Bhv6HlOjzU3f4KEN0FiZ2_LVfa7VwCaZggHA6A6B0Vo73RIdLW5p6i91oZ8LWB2ghtO60KIV2w9AW3QnzMJ7PAMFoKoLkhi4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7adc9a29.mp4?token=lRc94IV_cP_HRlIQndqmIDyUunMQ9TGGGKW8UrdWqqpf6v8QpkOosWljmuM6vF5J39Z34Yyyq96d6y_seTNP0as4m2UFjoOVhh9ycuKzGJqr2XKrQgjvZbOYugFn0cgn1ljZ5UZcs6bcU-Jm1zklyK-UVLZ1ABn8Xp4gA8HIJvKTBBiUHO1knH2_CxmSk5W18qvLOXddWoUVdS7cQIFjibAEOxNS9OLyBvQA-hWU_yEvzCDCcxmnxwYqh5v3okWK3K-IUWFq8Z0OJNeOf1fJB7G1Vm-PQ_dBC4Cu8g62_wQ9RRwHUE5-ZKaRKPMlfdOWb3iBWAOgtpBqQo5gFFDJyLbsZaUVn4FDg9YCDorgD019ZKr7H1q2PMYYiff7oUF__ChoDSo31fJnMm2yDf3mkQOUBegAQwErOhRFnNQlqK1okIx0YASBUHeO1eXxg4ovh1xeLb-E2lZPvW9j_DfRKdASWBOpY6GedupQt1kEEZoGbeI52Ekab6PAHhJQATpuI8wOe0pYKqJ3wQlma82OxMDFtU0YHYl3IE0ODD14K9Kx-beBBUJwJseJfNEBLsS30u5NV_WpuT1Bhv6HlOjzU3f4KEN0FiZ2_LVfa7VwCaZggHA6A6B0Vo73RIdLW5p6i91oZ8LWB2ghtO60KIV2w9AW3QnzMJ7PAMFoKoLkhi4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز خوب بودیم اما روز «بردن» نبود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/445118" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
آخرین وضعیت پروندۀ ابربدهکاران بانکی
🔹
سخنگوی قوه‌قضائیه: بر اساس گزارش دادگستری استان تهران دربارۀ ابربدهکاران بانکی، پرونده‌های متعددی در استان تهران در سال‌های اخیر از جمله پروندۀ گروه ایروانی، دبش، رستمی، مولی‌الموحدین، تعاونی وحدت و...  تشکیل و رسیدگی…</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/445117" target="_blank">📅 13:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up9jbxRXzUEVgYe4DYB7pkNXyHmZ5r6ItBY_tQcarw4Hb5RWOm5D7pNTKoa2oOWkYvAN27jUFExr_DQwKx96702Csl6ZN3AD6FXWooivwODIfAzT6mgeoXv1ndZIJVTsdZJ8Wb03o9J5_eNSzZKSZNMxz9qWx__PWNxe7j2kV0oh5AswHz4Y23-zXoSxevuA6rZPrcrsNO4by86fCD6rR41yovgWAzLdvCH7FBI7TLK86dY3hQarZdGKh-0wb_FVU5PXfoxiEytBVPRBKJp4YsHaS33Ce1Ms_x7DVedrk284pWjAYF1hZY8CcK6wMEPoF1IMh6IpkgDtMYj5Zc6ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل ایران به مصر  آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/445116" target="_blank">📅 13:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حملهٔ پهپادی به مواضع تروریست‌های ضد ایرانی در شمال عراق
🔹
رویترز به‌نقل از منابع امنیتی گزارش کرد که یک اردوگاه متعلق به کُردهای تجزیه‌طلب ضدایران در شمال اربیل هدف حمله پهپادی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/445115" target="_blank">📅 13:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQoAoHjQuDjX1NsxyfMQCLfovPANXp0nNUZU-3nnh7Nqoe23PK183YFLWDmMEoaAOvYlUZaL4nnR1nhTH4O4KZunoOu4SWpYMXuWeOKCnQGHRAd8kIitDfDhVJkCCQ3Wg-Vbt8UDocuvoHdssqlNYI08tZuYNT32Ox2EtiR9-ZO3kgyK_KL9vtXSRKx4tvDJ0VhksRDRNnEyfvc9fgr3apz9j6Nb0x8zVUFEVD3uWd1sP7bS8npj5UaSgUSVXCgRYt7hsHgLf9LthJoNpX6LAsAOBXEg-pz-BFiOCRM8q9cd6GEL_axseojGie-4pHQRBdINpZ9ErbOZ3wzi39VfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمان بازگشایی مصلای تهران برای وداع با رهبر شهید
🔹
ستاد برگزاری مراسم وداع با رهبر شهید: درهای مصلای تهران از ساعت ۶ روز شنبه برای حضور مردم در مراسم وداع با رهبر شهید بازگشایی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/445114" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس: گزارشی دربارهٔ وقوع یک حادثه در تنگهٔ هرمز دریافت کرده‌ایم که براساس آن، یک نفت‌کش هدف حمله یک پرتابه قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/445113" target="_blank">📅 13:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی در پاسخ به این تجاوز نقاط استقرار ارتش تروریستی آمریکا در منطقه را مورد اصابت قرار داد.</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/445112" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آزمون‌های امروز و فردای دانشگاه علمی کاربردی لغو شد
🔹
رئیس دانشگاه علمی-کاربردی: در پی اختلال در سامانهٔ ویونا و برای اطمینان کامل از امنیت و سلامت بستر آزمون، برگزاری امتحاناتِ مبتنی بر این سامانه به‌مدت ۲ روز به‌تعویق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/445111" target="_blank">📅 12:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1418eeae.mp4?token=e9E_eR1FrHuxCStai6qBDpXbUXDxGu95PVzy6P8eiE5jUHmxv5PfxstRgZWWUZnZlFdyRpsG6y6D2lDb9Pfe5-1HLqeuRcWl-F2reEuYJPj5lPOd1ADV_uKGPTrEj-y04Dl7OqwKiTCeGdb1PRXaL7sHpShHfnZmuw58cJNFu-zbU5CN9YUmJ3mFeCAUcMkFr8kjYCBMnN0qqu2DSA8NElY9TryZ1avJUJtDkj_j51kPzDjHlaKLsIsvv6oVxtWz3tg-vNPSZBJQBCoNmEhI4FV6-gQOLdkjZ7twsMOpsSSEOb70-hpaEaFQ3OVqRJZNoO4dvkDO17ivDc7Zyu0Enw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1418eeae.mp4?token=e9E_eR1FrHuxCStai6qBDpXbUXDxGu95PVzy6P8eiE5jUHmxv5PfxstRgZWWUZnZlFdyRpsG6y6D2lDb9Pfe5-1HLqeuRcWl-F2reEuYJPj5lPOd1ADV_uKGPTrEj-y04Dl7OqwKiTCeGdb1PRXaL7sHpShHfnZmuw58cJNFu-zbU5CN9YUmJ3mFeCAUcMkFr8kjYCBMnN0qqu2DSA8NElY9TryZ1avJUJtDkj_j51kPzDjHlaKLsIsvv6oVxtWz3tg-vNPSZBJQBCoNmEhI4FV6-gQOLdkjZ7twsMOpsSSEOb70-hpaEaFQ3OVqRJZNoO4dvkDO17ivDc7Zyu0Enw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احتمال وقوع سیلاب و بارش‌های شدید در ۹ استان کشور
🔹
سازمان مدیریت بحران: استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، اردبیل، گیلان، مازندران، گلستان، سیستان‌وبلوچستان، کرمان و هرمزگان در معرض بارش‌های شدید و خطر سیلاب قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/445110" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i339ZDwxFi0geEgHNvgym9XNKC03_cDr-StVlrSfX2GRA94NUwEbXR_ZT8AgVDSgBX_q5CqKa-fqHuJNxaxiCM_HDCc2XhzRHMNH3UDiDf9sDYu64cRUFxC1w64VUXRzJ9fvfE5Cq-qAcDNxT5xPm9drlYNoQI1c7ypxHclErVKwOGunvOV9uJU1-rZx1Ttv9g8EkMM5Sh-fa0bp6zyVE6TRFpdRwPQKTDjVYMwJ_kU3nP51J7jGBpXD5nFkATVEuOvggxVsfcZ95ETWqI9mpeDwRxUtDjQZN79crxpzoGh8wU1irQFZv3x3mRKJJVpPoyJH2SrSHzXi354x4aWyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۱۵ هزار واحدی به ۵ میلیون و ۱۷۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/445109" target="_blank">📅 12:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445108">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d94bea0d.mp4?token=Qt86pX_ThKlDUQTkOr5ac2_Sh317BFd-4AVpoyP87b3CE6L-OerZqya9D_2j5jxa4Mutv0KvT1s2S8_emMn2CbRyJl2DM9OWWmB-XXudVrGSywcYB-SnPIQfOjmsvoeEanoM0m3Gaclu8EaZUlW0KjEDhuKlIY0IY8b1vjKAkIgnv7NwC0E0JPxNW4IUQOZD5r95WQbu1EPPc7bo4SWb1jzo5jVtaZbdczQBzOY0b63xldwb3_RyaKmQF0ZlfPawTTgDEHOTVu9BnaKan3l3mkugsYR7kjO7IRoceUua4uPqUhOFnebXolf8Mk8DRq0H-0z8LRN3UICwFjrNerZ6IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d94bea0d.mp4?token=Qt86pX_ThKlDUQTkOr5ac2_Sh317BFd-4AVpoyP87b3CE6L-OerZqya9D_2j5jxa4Mutv0KvT1s2S8_emMn2CbRyJl2DM9OWWmB-XXudVrGSywcYB-SnPIQfOjmsvoeEanoM0m3Gaclu8EaZUlW0KjEDhuKlIY0IY8b1vjKAkIgnv7NwC0E0JPxNW4IUQOZD5r95WQbu1EPPc7bo4SWb1jzo5jVtaZbdczQBzOY0b63xldwb3_RyaKmQF0ZlfPawTTgDEHOTVu9BnaKan3l3mkugsYR7kjO7IRoceUua4uPqUhOFnebXolf8Mk8DRq0H-0z8LRN3UICwFjrNerZ6IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا امروز همه سحرخیز بودند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/445108" target="_blank">📅 12:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445107">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/445107" target="_blank">📅 12:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445106">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حکم بدوی اخراج دانشجوی دانشگاه امیرکبیر به‌دلیل اهانت به پرچم ایران صادر شد
🔹
در پی بررسی پرونده دانشجویان متخلف در تجمعات غیرقانونی دانشگاه امیرکبیر، کمیتهٔ انضباطی این دانشگاه در حکمی بدوی حکم اخراج یکی از دانشجویان را به‌دلیل اهانت به پرچم جمهوری اسلامی ایران از دانشگاه صادر کرد.
🔹
انجمن اسلامی دانشگاه امیرکبیر پیش‌تر در پیامی اعلام کرده بود که «دست‌کم ۶ نفر در ماجرای آتش‌زدن پرچم ایران در اسفند نقش داشته‌اند». براساس اطلاعات به‌دست‌آمده، بررسی پرونده سایر افراد در جلسات آتی کمیتهٔ انضباطی ادامه خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445106" target="_blank">📅 11:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445105">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cviSMuJe2hJkpekq5wNscOD2UvJSw00NVQoEssXHXQ5IUiwEMCbI_q3gmV3-WXQzmA-6PmLjagXZhOvfkbwf5o_W67zmbjQSHatDg54Pu8lZuNkefb7iOuLIpKCATJVYMuzE1toFiT24MvkGfzjlpVBfmTdy4dZV7sK8pUt5AqrAfvwwKKWx8DnJtzqPkWVKTU7zL_-Yph4NFfj-WLeGo-_iO8hznVO1NBDj4a1pIrryRJ6J91fbaslJdVpabflrsHFeCFWuB18MkxIPm7z01NL-51XnR17RazHasipZrzRwQBvVlj0LSyX1GCPPazFe5V_-mZ1alTTRhI-Dw0FKEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رایگان بودن مترو و اتوبوس در تهران تا ۱۹ تیر تمدید شد
🔹
با تصویب اعضای شورای شهر تهران مترو و اتوبوس تا پایان مراسم تشییع رهبر شهید انقلاب ۱۹ تیر رایگان باقی ماند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445105" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445104">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsgIN_3Od6VdcH5ewgHgg9d5MycIDIBHvaEhDPtrUK9JrQ_oChQ4foVC-e_JZ_om3xkfJ--tJoh8a6yuW0BtiVdXQqOWM6TfXBn-MLDMcKSuSJLmUpvs0tee2-uw3_mpi_mbC2-Ltm7nGucDhVQEDyZgO9CM9s07Xw1eOQ3EQHsroUyiM6tKw77UQnLBaeBvW-6I0B17smabNy1wfYNohulpNbzW79w8do75yhhf35ctVu-CCIlEtngGAUpBdF6k4eSps9hTCUGskU0QfZKziNityYNnSUnxYWebREuO_doK8TBpX7hKWpnBaD0boUkGAti3wIvZLoGhJ4nkW793fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پاسخ نیروی دریایی سپاه به تجاوز و عهدشکنی آمریکا
🔹
سپاه پاسداران: به‌دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان، ساعاتی پیش رژیم پیمان‌شکن آمریکا نیز مانند همیشه دست به نقض تعهدات خود زد و به بهانۀ ممانعت از تردد یک کشتی متخلف از مسیر غیرمجاز در تنگۀ…</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/445104" target="_blank">📅 11:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445103">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph_UZlVRcGCxa6U269kLe-LgUL8ugK5uKtquW6bn-pikFYKoEtCMSwKg2oH7JZ1GVcA8O5jWaEXonjntU1eqYJxnLDkfg3aW1WRmJdvM10wK5os0NCGIkCL6iHXody4ilBba3dLS_81ogGKKYSRpdE9yyac4_6PnhwyfEVFyzdSvQknF_xBDf1xBAwQb2aMqCxEmYov1A5DVj-EZTa4ayo4xYmKgb1lDfBGCjFtUoJAzcj6ovbWmmZHlhcXukbo5uXD5GRIRVFfo5ZiXgWsjqlJFB1i3v4OqwrN0pcV-p7phUYR57wCm0bV_9pduMUT3E4AQcRLQEw4HQ0zQ4gxmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیئت‌رئیسۀ مجلس: صحن به زودی بازگشایی می‌شود
🔹
سلیمی، نمایندۀ تهران: با توجه به تغییر شرایط، آن دلیل ابتدایی که موجب می‌شد صحن تعطیل باشد، دیگر منتفی شده و ان‌شاءالله به زودی شاهد بازگشایی صحن خواهیم بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/445103" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445102">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1wKbI_hT5l21WIb-0PbORVynqktrXmYv4BX6vZaS2yu3J9QRBT0gMhRT8i49s4Tqx45Vjq_mnSeqDFwo9xjLue1NTxtMQ_sNUi0z6F-aeiPTLfq6ZTKPNk_4ohW_mWkiUkj8gezgd8kFVoLbhElhfq4LJPNU09AE6dWNrjPQvBRl-YBuB1xXckOaKjuQirq7lhbfY6NPBm4PH8F_Ex-VwoSM_fi4zBePOBkOl2aUqr1rGtOxQC07_J-6KLHFlGouD_E14NUArWtyQLRcRLO8s0GeFo99atO6Rh36fLUXkMu7DxBxmcMZKY-dgFA4oRwwGdrgWj9V7hUF1jylQGfVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهداری کرمانشاه: از ابتدای ماه محرم ۲۱ هزار و ۶۷۱ زائر از پایانهٔ مرزی خسروی تردد داشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/445102" target="_blank">📅 11:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fL4F4mwdq2gmiak-hmIO9R1uxww3pbqhhfRAUVPmIFb6ymfJKeaRESIPEpm2fW97APaUC5SLAmgxggJm6OiOsDAf7BWSdwyh2Otan66viwg2iDZ885LzcTNPk34sX_gLNmK_f-JzVZTQum8j1X2gs_Puk-wVMzjOB7iTD1StkZoUKlaOwAaquVd50sZmH6s_NgRyDsSD0jpq2qVy-66MXwY40aEFPMdzNblgf20JrSpfDbXxAgX4-mPgpYFV_oh0kPduViA8c7zlOqOVYR4bOjq_YO0xmcdY_n827TESqk7YUZW9xVvy6Mv-w4PWbgSs54Lr76N51WWWiXDvnynYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLOC_l0WkL1_5kn-yIFLg-IvKvynuzxSiSOjHSpl4yN1msv2mwm5rmE6IPBouXtAKdBhVwtMlBuILc--YTrlWrqhpbfdk9lNB910dCuRMg-84GyBiQyK_sNXNFtY265PamT8Gbpxh2oN77Sm0_l9X_tilWG5DDJNYhvCFDrsBxet1JBu8qYIbxYrB5m7azcoUnI1_XepTxUagOV7W2P_A5ebyrhwJmyXQuQtE3tJyG0bmHF3s3u-YrGb-Q-ZYN8bdOuFXhBXwG7JejxsMZDpiES-F7yfYSr_ulRHs_v64Pxar19BkDSUkAkhsH2EHFgBjZt-_JFBq_AzcQsQoTx6qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
پرچم یازینب(س) در ورزشگاه سیاتل  @Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/445100" target="_blank">📅 10:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ1DyR2HgkfjEigw40xYwSdwpc_fRlP7Tcu4TEu5HlYMGMOZGUnta6xVWuC5L7j1z_cCLxIjBqLnaJEiz_VuZWG_mlfV9md3hR3SpPEzcmR-eWw3XWbLsf4ybVjXZ6p6pTQc8iWaB5s73fXXMk5zELknHWPZ86r02sHtr3WrB-z6j6QwYD8jrhswsUY-Dz5OIabSiLk0u8LuFbwkR1wZVJ44JpDrL1aW3VlXKRYuqVMz5ZSKQ-15BGPL18fsWaeVwN7Nz2i0q-fCqSAnvoAsw4EljBsjCcpq9YAZhn7RlsUGSfD7_YTu1qO86bSFFA2E3acw1ELtcIplZMc9Abd1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار: تورم نقطه‌به‌نقطهٔ خانوارهای کشور از خرداد پارسال تا خرداد امسال ۸۸.۶ درصد بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/445099" target="_blank">📅 10:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=AVX4CiyYjBaHIr9N8GGEoUmEDo1CBJxJxks7ThAJzaCZTWLSlXxuLaeE0J6i7BIl0LUkjqCmg-hVXAJ8iPskOjE87Zku2xtaE4IjkE4QprZ-6vE1zhAvbv8csGfFx1-x5tP1oECKskr73fM74raBhq0Nvqy9JnItA4HB2Pqec_RfuBkany3IVuXzF2NnfEbwLCocc-UjP85di_jL0TnyiX0YIXg5HzWyCx6aqksXGMMJOdz1ZjMf2jx8ZbpMQc3zbNe8bIkdQ4Nxzh6c26h45u39y3f4VEUp8wJpVGifLL47yeb7AEekhblcx0dZKaV9BSVl8jn5JSnxRNbkTImeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=AVX4CiyYjBaHIr9N8GGEoUmEDo1CBJxJxks7ThAJzaCZTWLSlXxuLaeE0J6i7BIl0LUkjqCmg-hVXAJ8iPskOjE87Zku2xtaE4IjkE4QprZ-6vE1zhAvbv8csGfFx1-x5tP1oECKskr73fM74raBhq0Nvqy9JnItA4HB2Pqec_RfuBkany3IVuXzF2NnfEbwLCocc-UjP85di_jL0TnyiX0YIXg5HzWyCx6aqksXGMMJOdz1ZjMf2jx8ZbpMQc3zbNe8bIkdQ4Nxzh6c26h45u39y3f4VEUp8wJpVGifLL47yeb7AEekhblcx0dZKaV9BSVl8jn5JSnxRNbkTImeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمار کشته‌های زلزلهٔ ونزوئلا از ۹۰۰ نفر گذشت و ۵۰ هزار نفر همچنان مفقودند
🔹
عملیات جست‌وجو و امداد در ونزوئلا چند روز پس‌از وقوع ۲ زمین‌لرزهٔ ویرانگر همچنان ادامه دارد و کمبود امکانات و تجهیزات سنگین، جان صدها گرفتار زیر آوار و هزاران مفقودشده را تهدید می‌کند.…</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/445098" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445097">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a605d47d03.mp4?token=nyQN6aqIeJuBcT_8LBCjPl_Ku4uLh6HfMWwYHIDCTMEQWtKNofwp8oRBSaS6nxE4-ZpZf_WLVq6dj9viieYTFwNFQ00KvwQCk56vjlKoC83fLVpEKCrULFfka_HSI41I0FSrqNMtvV79h86p2Q0Zd6ww8uoS5ZvmftUykhp87uATkBpTm40epOIPKGDljBHK3cytZkx9IK2axvLeSLl6SsH_n7RgyDZL8f4Nc3CFEPIxiTfyOWrfINpigiMPvcTFQnYChzVMfwPadzXai1Vq-LrOKCZdC4jI0a5xO3qlcXCHV5RTGPrb-Iot5KdR50nKDtpb8gfXtosJuEdxZerQew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a605d47d03.mp4?token=nyQN6aqIeJuBcT_8LBCjPl_Ku4uLh6HfMWwYHIDCTMEQWtKNofwp8oRBSaS6nxE4-ZpZf_WLVq6dj9viieYTFwNFQ00KvwQCk56vjlKoC83fLVpEKCrULFfka_HSI41I0FSrqNMtvV79h86p2Q0Zd6ww8uoS5ZvmftUykhp87uATkBpTm40epOIPKGDljBHK3cytZkx9IK2axvLeSLl6SsH_n7RgyDZL8f4Nc3CFEPIxiTfyOWrfINpigiMPvcTFQnYChzVMfwPadzXai1Vq-LrOKCZdC4jI0a5xO3qlcXCHV5RTGPrb-Iot5KdR50nKDtpb8gfXtosJuEdxZerQew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای در منزل شهید لاریجانی: کسی غیر از خدا نمی‌توانست مزد تلاش‌ها و رنج‌های ایشان را بدهد؛ شهید لاریجانی سرمایه‌ای بود که یک ایران او را از دست داد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/445097" target="_blank">📅 10:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445093">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzrJvw8M7rIFj0krRK59uHqrhtU8U0NWAqseAz8swfPW-AGoBCIpQHlayxuWgCgfcryNBqW-_2q89ply4ki97TUAo3ecHzE-gBbSFY8QitfpdQYFAj-P8V6QyQUWC8hXnQv7mkbHOxyWJsyXjq8JbYgtXlfg3r6kYkO8nIMvjS9gEwZqb7PvRDRwxJAMkT7gmqwhCrkpheJRxM-Ium_fRhUZSzlhXHGQ-PZuBrZGkMANPQxHjd-fd8PBEnwsDzyJsNvkMnhfi0r17CyqvXKt3p1Z1lu5XaQgcPAXwRM4ycucRz2LFoJ1ASnR830h0vkTdj8-H6ry7ln7IWXIQwtFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFJRR3SAkPREkGK2q1bg5GEZnBEFfBejpXhkg3oLw2b0bLbfxogn117b8x-jV94XXIRKtUJUxtRgK1_MPfZr4ZFka1RCUut678bJWxRpw2_qCj_2skHnhUJlPAZrXYUYvq6TFM9hv1J5j0JsRV65gVkEtuhqt_A6tqnNflnOITNoARrBQ-fcmBB6ufVBNNkeB8U8MgDxFQwhBhYVkRbPo6rLRT8MUObsZgGvnkYkhwbvPLvEch3_TtCxpmKDogTaBh8AG6V5FSteTRVtUsw2I7IXA5PqUfVKKJWnf0kautLV-NX8BptuGbC314fQSMPIxDMfoKRvMsD6x7HjaGJNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jN2JFUhh2A9Cmyn-hkQF_Zx8rmz-9EbfuVmYOeSi9t4sRlsimH2MKh6-sr1RM_XUoEw5hv8opn-cSkou5CqN0uwgspL7nJxz6ct6prdg4Xj4DgRDTs7IAyjOTHhByZrbs6t3QcMfhJXCL2J7Gp8aZ0zJX7b6WHCM0ioJuDJ3SrGFHDzbaIsvZ6ibuOroyu1KugOOam3ZRUEaQ8vw9OKZ_dU9v5WEi_aPt1aBz-1MtcQMpyc79hhPXPljIInmvhGHdp7CqbDgW91xlTgy4HjxtOdRbvZHDwE5r45ZOfcrddPfc59vxNpZ9zTU1bLYQ-Bl4eBFySIVs89k1QnDhFKTYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V04nykkLsjvlQa6dV02NvfYEuQiHRxHSAAsnnFhu7UFkKsGgpB24RnWkOQqVTtJ6SdLk_wOXQOPdtD-1an7izn2eKqNvakdKs8STHJZDqqnCq7CExe6nGkf3O34hfz-xTj7YUa2chRXo5p_gcP44qCeJkLdRyJG-QMHqZ7a_rJNRRSQuB6rB96zD7GOKH5mKIhzkkCJZTEduYoD-uq2j48CTvSbyL_GaFKUp7N2ImTaaY-2nRchDT_AOTajBcJ4PXHVfQ_jcxqJoCSuo6BXhJTIKOKZ-I7O0UROHjF5mbRrv6u9GmPE6TpiWS1VdI0BMZOJ2Dl2S92ugfnjuQJbnKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
تلفات زلزله‌های ونزوئلا به ۵۹۸ نفر رسید
🔹
دلسی رودریگز، رئیس‌جمهور موقت اعلام کرد که درپی وقوع ۲ زمین‌لرزه پیاپی در این کشور، دست‌کم ۵۸۹ نفر جان باخته و ۲ هزار و ۹۸۰ نفر دیگر زخمی شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445093" target="_blank">📅 10:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445086">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uo8flduF0ntuaXeiyP4LjbIzLMHl1McM-zfu3MqZsIzn54nm2cfmtei7_ONai5LBN1Cx6y7UBcIzL898oiM9u8lBSv0R_ceUj3_xD_k5Ait2mepEVCaKeSBqcQoVSGaFHwUyr5G81l8jbobdKR9jt7rAeVKj4uOVIeP1J0MyoHnJTQkY5_HPrV4P9HClryUvy-adI4EjiPPYVMzRDu_QwqIgd_CYFmQziypeFIQHKzJ4pVETGQnBPfv-raJMxDCT8zuti2S8ZmTP6j7SO34xreAv-yVj4gXlzhzreAA0VkCfW4qNU3qPSCusAsI_2eiRfPzAOSPyMMHGfqACsL9_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMGugm50WshpBlH8aBdlHSDMsO6eFsR1buG43qGkwldO44wve78eIYGTbeokM8HpmtfIWDS-j-88h5foTTJvpRqzDVOY9UGQHULl6f9yID8Rgge8-vGvoMLODG8X0TuKAW8hNc3ejL7JstntFnF9v8Az5ptt5xqFbEI0dQ3sX9AIpKLTtRqvs5axLrPdNa2zzWteDsq3t9sUwDtOBKXVH3Z2q1hGy2vbF8WV0yJaIR7pzrCPb-LLJfUF49VEHPegFrF9qX4hxGKOjvcFRnFD9D9ch6_tjJ7aIwTw3yybyFjAC9AxtuLvWj6_1pXx9RQZdDZTfTxUZfeo9tgn_Z-n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AalIDxm9iRjJKJflfzLSkIEk8j7aZjQulU8hP_8viLdSO5-T81KMJgDC_gFjMdMLHFBGW59LFFfTB77jyBt25jz1wkTT23sQMh-sHEMjQ-N3twodDhu0sdprGWSj3na9euI5o1sOeaFxdqXwkpxMpZ37LOkyX3ii96AGqpzQCYcYU4x0Sr2mA_ZZQvm0XF9SsLkQf_0Jt_8KY4K3spf32CKIiiAdwXo0LSG3p-svmLUYlQ-V9PgDEPJsQj_y2BBcUpT33DkpS2VtxsZTXjDi3Y8d80W3f4bXQs8Zji8O3cDqwueDeup4l-Qpecewt0Crbh23T5dZUmFW5ZaldhPVrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQ-qV5-kMJIAkWTNmNKaKNmQvquBu4--4EUQUk_ldlEjncDfi76i-H9gPCXLdFY62fAl98uUlV4sa_erM57gUX6z7X_gjTQaajB0MoN0W4-ZA7Wr47RD_NanZdm7J6SgyBuOajwOKVl-KKQx27gy_Y_WiqRAxKafplhUndsNTVS-cIFXpCI_9p82a7x7jSW0xXqvNUYP_94EUw-MeLbIZAACsuX8KHDeHO881qFtG9kROynpQ2w7BVX3Zv26RRvSDGw6KvevFEN7Vn5kO7qwWYKwrvNbZ_ivApX1IA3mvPk3Ub5Dn1pVd5qC5bKRlyNLA_SGY97Ewnyg4kreM80T1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOieb67SSDzT1i7ZeeUarnCwa4u_5uwWeqwDSaJAnrMlDgr69iOs9BwbPQW5-5QC5vsXs3xfsrTyR1ynACB00ZQ2Zhr_sy34K0IIcQFUcOamqUGH-Oj0KHEdx33ddIHrtpBDTID3iWM6qjHyBV3Xl077RrM60_3-hLt1C7iNhkf8ijMXeNR6mEAEOOer0S_5zLYBbBSqLAAOxCPVMV1Yk4hTdBvTI1gTQoFB2kwchaY59t03zDsUcZjJ_HkHlWvmBE6jpo-P8gYN0YyiSZGW0FC5_QZCJR5b1QBdFY1ZO3WDastagsaOQdHZyFRHbePugXipDWaBwAxHKSFZqbjYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7oEBCzpLgrkctbfel_-sp7q7_f7LDRi9i_wN7RlAW1srWM1DYyY3baYvmfazqYhNE1-o20zgXDAmF0zm1ItIMzvool1lG6kZ2GZ3aawyDr-EkLYDbClEM7lF6QZJun3EWFE1sTIZzijKxUzw4dhWCKEG19J8RRMNZHWjU6uQkjphBcd_BMbkNsfcN27NoCyMDcElxHxHad1u4XBUej1o6Tcny3OKeA70gJ-E3T-Ft3xtx0xg5rIT1601Xg5QWFyoZhgIiQH3v5GFuvZAMTuQxHAaKnCv0QhglDRwFVLliYs6zJNlLbj-_lts_K_sa9pKGy9m6EqfqbNojXaQB79SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nM7kqK3v0bxw1Q2jUDu_dZ61_laIkW6iihuyhEzV-CTXTODgQEhE3cT2UHgocggzoVKoWafGT3meKKBLCPhx3gKKp3dH-k0DG9mncnK200NIuiQemAmxMsyuNXc9dD0Rp8tbf4vBdcrSyHXXxEIxl_Jgng5bK8h_f1e59EzuJZodmQJqMKJPor0oZRGsFCBfQuPjSva6uGQ6q_wKilUcB8biCzkNe5IasipFzqxFIY7AtGs6FRsxa7ZJZjnlvmjIEloEAYovhUSA7RpmbdJGXpXDWrTI73vhB0Dbp6Lp_wFXrHEJE_1W-7gPJvSbKL8L15Kko5jVXuj98A1g4WV_zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تماشای بازی ایران - مصر؛ از نانوایی تا کله‌پزی
🔸
همزمان با دیدار تیم‌های ملی فوتبال ایران و مصر، مردم در نقاط مختلف شهر از جمله نانوایی، کله‌پزی، املت‌فروشی، سوپرمارکت، ایستگاه راه‌آهن و ایستگاه‌های تاکسی، با تماشای این مسابقه از طریق تلویزیون و تلفن همراه، بازی تیم ملی را دنبال کردند.
عکس:
محمد‌مهدی دهقانی
@farsimages</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/445086" target="_blank">📅 10:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445085">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ugjd-Qs4t-m6LxOmSLC46RIyGgxXQlOt_C4u0SUA1Ej711sjPVsfzAX44LhXyoAWGLyJkawsFT9hOVeFMiIpw3GHvwn9JmNQKX0zsuJHO5zVXIqENTIPZKt5JOawwOLM-Al7dFNBijvNK9_pITtliQ_sylEw2OBvHnQIbKRrR_NTUwRQ4tQPuajNFWqml_GYlxeKdNTYdPNdNTy8rZu5T8NQhtEdtkwrcS6nU-VRg5qbXgY9gLXIMeoGriSKkcvqJ6zgYURKrILo1mkO0wI2-sOjO4HTfMs5JwE--VhBrTRXmcSOCztQu4qXUeOSBdqc2HsPkAJzYyCdP1JeakXcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران و بلژیک رکورد مصرف اینترنت کشور را شکست
🔹
براساس آمار شرکت ارتباطات زیرساخت، همزمان با برگزاری دیدار ایران و بلژیک در جام جهانی پیک مصرف اینترنت کشور به ۷.۵۶ ترابیت بر ثانیه رسید که نسبت به سقف ۵.۵ ترابیتی هفته‌های گذشته، افزایش ۳۷.۵ درصدی را نشان…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445085" target="_blank">📅 10:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445080">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgJxHI_3ptXXedCq9LE7FSdTOvSJ_ZOarasUJaX-QXIdE_qbzqkHVsjvzGQd6MvggdR3BBv4SpDlw_XBuVqdNszDrZQyaffW1oT4L0V8OO0lh95aIHCok7vYGQUmKekLiCHLkO1KIhsCCVATEudETiI9Qio_ut69TBefW2yrRI51RKPK1isUFQ6h0bMw2bxipgXSEm22u99BCDTnXgGo77z9zcWGsaJdboYpeFWvjQTQ36AraTC2chJYzgSbwi2wsBraYCQWCtI-GOE475qQ7NpdWtlzeaxX7RtR-JXYPSKbksP-SGOXyKiKD7an9J_im75AN8XLd8-ufGap937RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMhe6FYtidjIsb4F1XIXFW2f2D9SldLCiF0fdv-3kaTaerbTdv6VUNy7JHfVyGZZQremxh9qH2EBlvaElmp_I_4dj-9VKhWRoZwXwO1BFhb_S0NHXooCO8smrQBMxr54QF9hr_YrT_6gwop-OUH0J_dyhNxjEIsqWoxzXB0Vj9dnDSrgi7I25xyR4mJV66_ImCmgh3FcmUY2gbjk6yge84SIR_0AQKINbB5WuMBYSuwHOxly3VtOZyxX2lmNFyB1vE7HAbRnMonKXBPG506UIyaICKV3js8CouCJAWh4jyXDi3dlbItnF98Qxif2N2QP0KibBIE6ne4GfzAKy2mbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWtof20HhLYZ1A4GzYxUX9ZTvnKVYCHqvC8fQnRvTvA9d0hyM8eX_dE_EVlqeThgDU2suLuq4VXOd-R85UsMpSFTGE-n2XgVd-rOTjsmexsZKFN-40QeKKlGqfKrVR0j3_tx6IndocZj-V0-qdRGB7BdmDX6c1-bU02_1mFtpKeKkfI5NLACKkU2edmWZZLnrO0uxZpGfP-rOiMCzO0_JtjteHpexh9DRdYlqYlT52-r-F3FwjKXhfGMGMezjyVh0FTjg_xwJkyQZXcAz4zBBQhpteh1rxX1OU5eGgcbmOKkm44vxZEI4-jNrG7DV3GQuBwBU8PvGyOnOkc4ZI9A6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5e12dSTz7jkQQD2p9Q9BQIhcTToam_AtZTtpJAvVrttSR-WiZ10J0-Zj7cvzofaJIx2oCBcjM1s_1xdPyIpDuS1pdBNlvCs7ZHE3CQgTAjeKi02CeyB6v96n7QNcNkAaV9yL1ibOHcLyjKs2dzqRZNvaxTy6Dpn5ggyGXOA_Yb5gtCFQU7MN8t1fdJNTsyB78UD-uPe3olAkk6vfManufSoG1Xz2j3-N3jihDgSwv8343BHgJ52jhtJIdDh45EOruT7irXZZ52iaMW07IX0jTGrZNlAE7LTymR1YacGoaO5FthMX7rQ3AY-Z35O_wZ8yYJ_uwWZJNqVFiTYp-Lq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaQMzHi-CZnr2koGL1hXKu4_52u2pDU0f1fZ_R-0iyoUcSMYIigN6KGmg900NK-R0auNemx03u49lLQjn2RKPdFCRKZ3ztYdp1VLvDtySpRBXXN-oPy9PZWY8bN9XiZ8PueB-sHK02VhAL3iP3efiJctkOxipJ8gZ_V3INhFwc2Q8ZRBPdxbIlRDE1yP_e19ZGzOtKGRT6PnpJRE9GFlyMf_K0Z26ciVu-SpOk9iCGLtKqASgkf0vpXZWSgsCsR74HXduy3zWzvdHbqxxwi94U-b5IjCDItn-dr6Gk44I6ftxuV-BS-4n-wyJ-l8yGRvCb-iwQA3kMpGv4x3aA8QvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
همدانی‌ها در هر شرایطی پیگیر بازی تیم ملی بودند
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/445080" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445079">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLumd1sBDbmG_k4xaoPRRjmk0iFBaHvdwISd7RY1Y4CruQASN-ilvCz5aWog_ybn-NQ-Qtg3eaFdFvGNU7_VFnkriC-q2kW0z7finc_Zt8qA9Xg6tfvXq9-YAIfsGlipSziTECLq2vjH05E58gZ4cuWfPCHaHewwDWL6ja3UrPXYUZVyJTulsmnR1NOvz8JezlvyIWy_FQRjGwYA2l4U7j15Q-yaiD-7o4mAFv07rnDeOL3vgGSQNEhD0TuedzOwnXmuITv3q6fPe6VrwHTnON60-f2o4DQogmS_os2Yi_rR_J95eeosPPtg-1db7uRWPSf6ihu4fsYK_IEJEE4Gaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس ۹۲ درصدی ایران برای صعود
🕯
برآورد سایت اتلتیک از احتمال صعود ایران
@Sportfars</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445079" target="_blank">📅 09:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445078">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c970fb9dfc.mp4?token=kkEnv1OA0QQftSxYdqkED2KQMWmsbanXR_wVHZUtSZOUW34rDcPy0Bg3yrfbLYiRiF8fOT0F5M1uFkv2Rag_x6SYjfXcOb6IWCMlR6UECaKNkZey60TIGzDY_iMcUPCfW3Os_6yLndtGcdfRAdXhF2VVKKKhapETO8KBBHdcUr7NqKwRClGbGlreylKmSS_Y2sYMjY49kD5qNLgkjYq1Qc2wmT1qkjYmEy07HiScl4e1fI39ds4vrhIk-aaQ3yoIZjgZ_NWkQhRN0obucwZIyIKDiinF7jEGJq__cIGwJe5SOu27Z-H5-x7SqFpSZJ97o366wT5CKYPdbOy_x3hu7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c970fb9dfc.mp4?token=kkEnv1OA0QQftSxYdqkED2KQMWmsbanXR_wVHZUtSZOUW34rDcPy0Bg3yrfbLYiRiF8fOT0F5M1uFkv2Rag_x6SYjfXcOb6IWCMlR6UECaKNkZey60TIGzDY_iMcUPCfW3Os_6yLndtGcdfRAdXhF2VVKKKhapETO8KBBHdcUr7NqKwRClGbGlreylKmSS_Y2sYMjY49kD5qNLgkjYq1Qc2wmT1qkjYmEy07HiScl4e1fI39ds4vrhIk-aaQ3yoIZjgZ_NWkQhRN0obucwZIyIKDiinF7jEGJq__cIGwJe5SOu27Z-H5-x7SqFpSZJ97o366wT5CKYPdbOy_x3hu7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان: من نمی‌دانم چرا اینقدر بدشانیم؛ امیدوارم صعود کنیم تا حال مردم خوب شود‌
🔹
مردم ایران ما خیلی دوستتان داریم. ما را ببخشید. @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/445078" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445077">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5a003f09.mp4?token=TjSPquCuHKIvyXZWi-QlJkZrwtjJy4oliEFtKGvHDYP6KGT1e_yi0bOHL-awS6W-4-VnG6V3XbpHT9VAs7wGVxHqa7vdJEonOKWREyGETuHRQR9RcyqBN2S6Gwlu9o-BTozQVLPtn1SkzIlASZPbREw4ekw2ucLVdAVJWTzrsE2KO7hWggvzEypO7Q0jFEHuudDfxgdqVM_p6o1NYW6a5TEGaWkgvIP92skvGq4HOOaHlmjtKgRrGUFcJOagbSJvejjMIwvonMlhsaNf13fGO_9Ip5d6OKI-r_FabDzGlOllnhhHjTqoknr_xA5x3tfJQ7UFem9xH79Q8V_N0LEPKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5a003f09.mp4?token=TjSPquCuHKIvyXZWi-QlJkZrwtjJy4oliEFtKGvHDYP6KGT1e_yi0bOHL-awS6W-4-VnG6V3XbpHT9VAs7wGVxHqa7vdJEonOKWREyGETuHRQR9RcyqBN2S6Gwlu9o-BTozQVLPtn1SkzIlASZPbREw4ekw2ucLVdAVJWTzrsE2KO7hWggvzEypO7Q0jFEHuudDfxgdqVM_p6o1NYW6a5TEGaWkgvIP92skvGq4HOOaHlmjtKgRrGUFcJOagbSJvejjMIwvonMlhsaNf13fGO_9Ip5d6OKI-r_FabDzGlOllnhhHjTqoknr_xA5x3tfJQ7UFem9xH79Q8V_N0LEPKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان: من نمی‌دانم چرا اینقدر بدشانیم؛ امیدوارم صعود کنیم تا حال مردم خوب شود‌
🔹
مردم ایران ما خیلی دوستتان داریم. ما را ببخشید.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/445077" target="_blank">📅 08:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445076">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">📺
ایران با برآورده‌شدن یکی از این شروط بالا می‌رود:
🔸
بازی الجزایر-اتریش برنده داشته باشد.
🔹
غنا پیروز بازی با کرواسی باشد.
🔸
کنگو مقابل ازبکستان پیروز نشود.
@Sportfars</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/445076" target="_blank">📅 08:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445075">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef484074c4.mp4?token=QLnlxgycavV7-sNpT_QbLYwbY-3exDOtvmQXQR3vHdH5H0OoKvu57fnfyWNNAE4v_68WJfEGbZ3nRj4Blq2VYucnilewkVVaTCaYnReAPCyJ5wlgd5AvMzbOW1ZyGIu5l9m1h1iq2QTOmt8Vv6t2txGM7f6lnjuh3qW8EYAuZPqlPbu62vEnJRtqT_tIyeUFkTw5y6sqYIWDjWF5ytXcMM_9G4wZVuSGyIxyz5y2H7tWKlAakN1P2BfyhFIEDed3fILOyFJm1RJ6NS0m1UTQobFWJtg7ja_eUsKkizC5r5zNmZbalJJtICPv2KgcVNoXYjaBuaNPJW1BBad2Xd8ohA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef484074c4.mp4?token=QLnlxgycavV7-sNpT_QbLYwbY-3exDOtvmQXQR3vHdH5H0OoKvu57fnfyWNNAE4v_68WJfEGbZ3nRj4Blq2VYucnilewkVVaTCaYnReAPCyJ5wlgd5AvMzbOW1ZyGIu5l9m1h1iq2QTOmt8Vv6t2txGM7f6lnjuh3qW8EYAuZPqlPbu62vEnJRtqT_tIyeUFkTw5y6sqYIWDjWF5ytXcMM_9G4wZVuSGyIxyz5y2H7tWKlAakN1P2BfyhFIEDed3fILOyFJm1RJ6NS0m1UTQobFWJtg7ja_eUsKkizC5r5zNmZbalJJtICPv2KgcVNoXYjaBuaNPJW1BBad2Xd8ohA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افسوس قلعه‌نویی و بازیکنان تیم ملی بعد از پایان بازی  @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/445075" target="_blank">📅 08:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445073">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMtQtS-sBAjsgT_Xhf-CfIT501mh3oWFrCASj_WD8X8FFRM-cQ1dqtBxrwwe8MrcVNbN-3z13NrGLyQQ-eKyxJrf8wg8gnWjFTQH0oBlNTZiopcICWsaAFAKno-etaUcyssEvS1cKnRPel8BwjrZLobOOaNYMKmaINdAUu-H_gnQAmLXqaukN9ZO2NfAz32wkWkjZP1HUlsLXhhKKeDfoY2s6gO8vX0Q98cZ9YXvrvVhZHgYL2qDExhm-tDjootZi1ihjILzJgOycJp88OFZ1JwuaH0r26SEXN1Q71zBb4lQ-N4zkMMoUtmm5oxx670JxVzsEZpO1H7qeDVKL_e23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جدول نهایی گروه G جام‌جهانی
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/445073" target="_blank">📅 08:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445072">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=IZD3DMhV6fcRb9-SM7uS3HlQmatBAeZJ47GgWr0ieTV351TUiY15NxG41I-_W1fnOOHTchbrRc8FVEsxL4ow3bQk-GisJeybykrEv_tWDVJrY-0MNyGD-j8nzVq0259gzPukH5FK5HrX-PjzaKvBSyk4izVmNLmB2Xp1fqk1WWi6jnrvQ2EygPnPCVa4BZz4-tcz1Pj6_aIo56clFZVv4TdRw3wiu8Q-n7KZf1zuAUvmgvpidvo-OEl1BFn196OMPM-GWkpxLyYVCT-ycf3JBw04HYK167bvQonc2bthvqu8V5ArzRRo109KWGSe1noW2M0pO8tr0ll-6LVrGBNIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=IZD3DMhV6fcRb9-SM7uS3HlQmatBAeZJ47GgWr0ieTV351TUiY15NxG41I-_W1fnOOHTchbrRc8FVEsxL4ow3bQk-GisJeybykrEv_tWDVJrY-0MNyGD-j8nzVq0259gzPukH5FK5HrX-PjzaKvBSyk4izVmNLmB2Xp1fqk1WWi6jnrvQ2EygPnPCVa4BZz4-tcz1Pj6_aIo56clFZVv4TdRw3wiu8Q-n7KZf1zuAUvmgvpidvo-OEl1BFn196OMPM-GWkpxLyYVCT-ycf3JBw04HYK167bvQonc2bthvqu8V5ArzRRo109KWGSe1noW2M0pO8tr0ll-6LVrGBNIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی مساوی تمام شد
⚽️
ایران ۱ - ۱ مصر @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/445072" target="_blank">📅 08:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445071">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZKs347WWWHCFUfbQQwMV2sfqsiMVGMjwsrSyuSlY30RU2J_wak1SX5XwV4HRtrbMgS2bjFvinDK0ydNdSDkeku6cyczWxYXk5c5tbI4wWcSN2lW5-Z6DASyUm6UpHG5TBgadWwWYWSWVAaa3YaxSHRjkfm5nmQqySN5kwZRUWTpyR0MmHxHwCQcvAErLo_R5eynvZ-7QioPao-34RZUjb7t4siqq46PYhOt6FvCk90XcEwe1-5jaqLqJyXq3UmTsuKE6-r_8aqO66tj5I2jtbjn639sU5Ek09Ow0Tq_bgWSgN9GM--Le_ChwTqEeOmtpp_Ych1VwJVOMdh6Fpi5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی مساوی تمام شد
⚽️
ایران ۱ - ۱ مصر
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/445071" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445070">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4RZPxGrUUl-xSNqc5vXvxDYVTUhSRI6kYP6aw2NQ0WN-3f2hBMvhS-JKksR5TvMsLFywue-AZS-H5kkdqiZwxB78bLfU9oORATiSkObHeoy6l8APCEmDhPZKNuh7bNHv-PkV-mHgM-Nda1qH5DRZeEDN7muys2kpDb7UmyCU41vAAtbK-5X68kBcPFzepsTw_CYxR4jW0AXmw4KjO_5Nmpdg9wn6xZj1-NC8OHusHGRt0sO1FVTw4H1qoKb0XZaiqDSd_j7ea6IJ0PbJknlGRB_L9klSxtzKjnnEey4Aw0ur0fZjXCy3_z3F9ER_c2RCvC-Mq6lsuTbVIltLr2ANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امان از ۵ سانتی‌متر آفساید و تیرهای دروازه
@Sportfars</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/445070" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445069">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1111467265.mp4?token=a8EnLXaJHVPWYjTn4GVkcpHzIghu-hx0nyrVE58d93SGnSUv3zohr4_pYYMCdB6BDj74tJxfNdiwDvB6D_Tpfn-drFg-vCp_Hwy7WSM636c5RHikwOVC9Jf2I74WlCMSvgMOaccealxudIOntjEMmu3oF1SEQMIoeQzCI_grLWZtt-GUf8CZ_YcHbsOxkm8zWTIndQWIqoc1xNhIn_yLkSwbSfneddCfppcWQGWUQWvbI8h2CgVb85TW6qveIbZsw0ZIv-fCQctVMYgkD7HDBCL72aMqadGWKwnBCWrsT27XN5qAxCn0PKIlRt5yonnC7zVssLbUJi2VL0X7Lwkjlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1111467265.mp4?token=a8EnLXaJHVPWYjTn4GVkcpHzIghu-hx0nyrVE58d93SGnSUv3zohr4_pYYMCdB6BDj74tJxfNdiwDvB6D_Tpfn-drFg-vCp_Hwy7WSM636c5RHikwOVC9Jf2I74WlCMSvgMOaccealxudIOntjEMmu3oF1SEQMIoeQzCI_grLWZtt-GUf8CZ_YcHbsOxkm8zWTIndQWIqoc1xNhIn_yLkSwbSfneddCfppcWQGWUQWvbI8h2CgVb85TW6qveIbZsw0ZIv-fCQctVMYgkD7HDBCL72aMqadGWKwnBCWrsT27XN5qAxCn0PKIlRt5yonnC7zVssLbUJi2VL0X7Lwkjlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل ایران به مصر  آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445069" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445068">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6be0c6ce.mp4?token=OYdCU5fS_rkTXjZVjrCpCk7OUNkxlTltiDg51Pwc74cuRLV2jp13mNzeP2ehh9cQOwhyOjSmyzX6XvTub0oOj8y5RJzQJqOD1BQX1x1Z3duYz1aSjRG4BclY1bV_8oKLXARrxLhOMOV30a-6DHrMW4QN-NaGwK2baNeHhz4GviSLNlO_6z3LaEaHmq6BI4xSU5xYIJNRsgKiRnuFcgiN7RsjJIcKt9sGPWofXKzLkXffNSqQBBw8dXKTjNkf82lfRHOMieo4KquN-_35kLglHqlXEl0hTboxKMtbuToXQ3Qh8vwAB7t1HmoZG7vqDyYko6Fmn3ng2_s-Dcrf9MdZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6be0c6ce.mp4?token=OYdCU5fS_rkTXjZVjrCpCk7OUNkxlTltiDg51Pwc74cuRLV2jp13mNzeP2ehh9cQOwhyOjSmyzX6XvTub0oOj8y5RJzQJqOD1BQX1x1Z3duYz1aSjRG4BclY1bV_8oKLXARrxLhOMOV30a-6DHrMW4QN-NaGwK2baNeHhz4GviSLNlO_6z3LaEaHmq6BI4xSU5xYIJNRsgKiRnuFcgiN7RsjJIcKt9sGPWofXKzLkXffNSqQBBw8dXKTjNkf82lfRHOMieo4KquN-_35kLglHqlXEl0hTboxKMtbuToXQ3Qh8vwAB7t1HmoZG7vqDyYko6Fmn3ng2_s-Dcrf9MdZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربهٔ سر طارمی به تیر دروازهٔ مصر خورد  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445068" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445067">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608fda927c.mp4?token=mTk9vtFnOTUCyH0of8-Lz4HVru7U6tef4GocmuE4PuSv2Itpm017y-OvwGCHqfwstjV_hrkZW4wB5fmrb72hTZZ9hdhaExUhBv1rxzeho_ZYCdzwVJShfA1_CMBoG-U-Y57GYgb55UX4G3DlEfd-PQUgooFL-lWLF9sbk1RBBGmh-EAVsS9u-WL0_Eyb4P_26ehsdhOo5CCm4QNdilhOdOkZEVLeCh7o2iILgKPqoi4g-LSrNm5WaT1BCDXHW9JK-JA0RR4fKMhb3ISrPy1jWietoUUzPG8NUF-O-Tr8v_Bb2WLhq3E_L8Q-m7YKKyYRnct80RDmrxlqHLFfJG2tjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608fda927c.mp4?token=mTk9vtFnOTUCyH0of8-Lz4HVru7U6tef4GocmuE4PuSv2Itpm017y-OvwGCHqfwstjV_hrkZW4wB5fmrb72hTZZ9hdhaExUhBv1rxzeho_ZYCdzwVJShfA1_CMBoG-U-Y57GYgb55UX4G3DlEfd-PQUgooFL-lWLF9sbk1RBBGmh-EAVsS9u-WL0_Eyb4P_26ehsdhOo5CCm4QNdilhOdOkZEVLeCh7o2iILgKPqoi4g-LSrNm5WaT1BCDXHW9JK-JA0RR4fKMhb3ISrPy1jWietoUUzPG8NUF-O-Tr8v_Bb2WLhq3E_L8Q-m7YKKyYRnct80RDmrxlqHLFfJG2tjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت مصری‌ها به کرنر رفت  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/445067" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445066">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607ba533a6.mp4?token=YyObhuEjAPCh4GpVfLuCtJryM0XAA4VIStEGAfNzpGsVHEw3awHLjPY5W6vNjdgLoNF_bN2SIPlIn6WIr6nDfc7kACurwQj6hBsx6_l-MWCd6F7I-fuv4nE_idfgfUICM3YDNArY0h-Whz3zunbnO7dPx5TVPMKmemw9BBT4dPTSY9to1Q_L1NTSe8ZurihKsi_bv39r1EN2hMtdbi4-qr1TTItxFIFwx5fbvXZKJ1aQ9pdTCKE_IgFWjAR9Y9Se8BNz4qZqxyBO0cHUDwxgRmpxdLewuGuWsoKVLAG7yWtK0cdXW1aDk1RGrN5kO87Uk4-n3LAkTiMFU8NMwpixNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607ba533a6.mp4?token=YyObhuEjAPCh4GpVfLuCtJryM0XAA4VIStEGAfNzpGsVHEw3awHLjPY5W6vNjdgLoNF_bN2SIPlIn6WIr6nDfc7kACurwQj6hBsx6_l-MWCd6F7I-fuv4nE_idfgfUICM3YDNArY0h-Whz3zunbnO7dPx5TVPMKmemw9BBT4dPTSY9to1Q_L1NTSe8ZurihKsi_bv39r1EN2hMtdbi4-qr1TTItxFIFwx5fbvXZKJ1aQ9pdTCKE_IgFWjAR9Y9Se8BNz4qZqxyBO0cHUDwxgRmpxdLewuGuWsoKVLAG7yWtK0cdXW1aDk1RGrN5kO87Uk4-n3LAkTiMFU8NMwpixNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکل زیبای حردانی در دقیقۀ ۵۲ مانع از گلزنی ترزگه شد  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445066" target="_blank">📅 08:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445065">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
شهادت دو مأمور پلیس در حملۀ مسلحانه به ایست‌وبازرسی بانه
🔹
ساعتی پیش افرادی مسلح طی اقدامی تروریستی به ایست‌وبازرسی ورودی شهر بانه حملۀ مسلحانه کردند که منجر به درگیری با نیروهای امنیتی شد.
🔹
طبق گفتۀ منابع، در جریان این درگیری دو نفر از نیروهای پلیس به…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/445065" target="_blank">📅 07:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445064">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc26fd716.mp4?token=lQyuqfhb08YiFpFajtNg5U9Yvz6JU9RAvTtY-3581bTwBT3ofSrgxhYgrR6ICE0TT5ZslVHl32iClaW-HT5oQNhFSU7mHg_oxbAMQwI0y_0q0-cBvTxAPFd9M6N6xuTxSOJl3WBXvW-RuMNHsEgJf3Umug5rYSquUkauWREGASDclc5bO2kUd3Vo9gd_4EcoaWGLgv2KhWIoHEL8q2gD1BEXooTWoGEIMbCcEw4yEBoZMSUS2-bVFEWV474V9rBijwRPH2FJgASC59l-7dA15yD7Cv5DDjW7igbT6Wuy178GmSs8ah3JUSueRYLY4tpchbP1gu9AV9qiaiYcQx9MSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc26fd716.mp4?token=lQyuqfhb08YiFpFajtNg5U9Yvz6JU9RAvTtY-3581bTwBT3ofSrgxhYgrR6ICE0TT5ZslVHl32iClaW-HT5oQNhFSU7mHg_oxbAMQwI0y_0q0-cBvTxAPFd9M6N6xuTxSOJl3WBXvW-RuMNHsEgJf3Umug5rYSquUkauWREGASDclc5bO2kUd3Vo9gd_4EcoaWGLgv2KhWIoHEL8q2gD1BEXooTWoGEIMbCcEw4yEBoZMSUS2-bVFEWV474V9rBijwRPH2FJgASC59l-7dA15yD7Cv5DDjW7igbT6Wuy178GmSs8ah3JUSueRYLY4tpchbP1gu9AV9qiaiYcQx9MSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکل زیبای حردانی در دقیقۀ ۵۲ مانع از گلزنی ترزگه شد
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445064" target="_blank">📅 07:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445063">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e77ba796b.mp4?token=tVzlPxhPBv5FcP4bfgJb0TSwEF9uildiqkIVHt6Z2SeEWsmwQeFqPhYDr7RAVrRC8dimD_nh2wN1ZRc5McM7-nqh93CghPNxuZ7PjG_pgRi6s7UB9sGcTlfX4k3yDNc5Ug-HJObuHef32gnnQhZE7D1RZhwCGB-vgVdko6db7MvD2rb5J-t-95VYIiFpAcra3Y8BBlJWTotV4iCqq6G63j1d-f9db5ItQcR6lcpl9KrL4jvLo0TuI1gTZ1FVDa4vm3JDe21aS0xAvVojFQxEObGF9_AoT7y5xshXdQFuvJCUOIyzwbzVvZy0I-o5ykbw6tibWfo_OzPz3Rt0q5GEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e77ba796b.mp4?token=tVzlPxhPBv5FcP4bfgJb0TSwEF9uildiqkIVHt6Z2SeEWsmwQeFqPhYDr7RAVrRC8dimD_nh2wN1ZRc5McM7-nqh93CghPNxuZ7PjG_pgRi6s7UB9sGcTlfX4k3yDNc5Ug-HJObuHef32gnnQhZE7D1RZhwCGB-vgVdko6db7MvD2rb5J-t-95VYIiFpAcra3Y8BBlJWTotV4iCqq6G63j1d-f9db5ItQcR6lcpl9KrL4jvLo0TuI1gTZ1FVDa4vm3JDe21aS0xAvVojFQxEObGF9_AoT7y5xshXdQFuvJCUOIyzwbzVvZy0I-o5ykbw6tibWfo_OzPz3Rt0q5GEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت عزت‌اللهی از بالای دروازهٔ مصر بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445063" target="_blank">📅 07:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445062">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc44ca4f13.mp4?token=oki6A2UmTCqEsdNeMwA01AeDv9MYGE2Sgcidr352vR41cz69WZBcAYinnflbODrR6_83aPxhvGJrN2HbJv4poGV0seo1vW8bZVay1KjnpWiM8_p5Sg6O-48mbNUibzz7eH6LtdPHwnJtRJCU_87rCrWbvdDhzYrjUZ3-G-ogs6v8Ix6ecyybdzllmZR-i1LY7Y2ld_dr73UDHCfyFair0HeHLvN5TcZ94KCSAR05V4wXRJvcifhUg55jvFwqAVi96Q030oq7qwqFa4gtGFBhpiUFWmCIIVKiOiQ5o3tbcnOtzDL4mZZry_IDv0l1_eLVLroRxPB89UZXnEHOc35xpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc44ca4f13.mp4?token=oki6A2UmTCqEsdNeMwA01AeDv9MYGE2Sgcidr352vR41cz69WZBcAYinnflbODrR6_83aPxhvGJrN2HbJv4poGV0seo1vW8bZVay1KjnpWiM8_p5Sg6O-48mbNUibzz7eH6LtdPHwnJtRJCU_87rCrWbvdDhzYrjUZ3-G-ogs6v8Ix6ecyybdzllmZR-i1LY7Y2ld_dr73UDHCfyFair0HeHLvN5TcZ94KCSAR05V4wXRJvcifhUg55jvFwqAVi96Q030oq7qwqFa4gtGFBhpiUFWmCIIVKiOiQ5o3tbcnOtzDL4mZZry_IDv0l1_eLVLroRxPB89UZXnEHOc35xpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربهٔ سر خطرناک شجاع خلیل‌زاده از کنار دروازهٔ مصر بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445062" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445061">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚽️
در شروع نیمه دوم، دو تیم تعویض کردند
🔸
صالح حردانی به‌جای کنعانی‌زادگان
🔹
عمر مرموش به‌جای امام عاشور
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445061" target="_blank">📅 07:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445060">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYs7uUEZKdpXgQEYcYMfQ-MNTxe_45GufvPdGdHsRGf8HgqjuIPDG_cOwnVLqk7chYbG2DrGfqtcMSNzxZasVJvHnpayNAi2Yn6L86PvcQgYof1R-wwUdVnVmg3Y_IHzy09Nk8fHZbk0EvDdS0XamDAgFJnSaQneevJyvyygZcA0b5YNnWZ6t4j338X3poHW6BOgptjL5BQERIUyhSl6T2AjoFYRdH_ifCKWfpAvKYSA2X0H_vHcdSHZIcHm5yf-1Gf5G6aQ9Ii5G21XWA2fgfg4jxJ1NYj-2q22CNhEtccHRJ2dQp6RNDaLpD7ouWsxQRt-r9URsHpi0oQRpcF6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نیمهٔ اول بازی با نتیجهٔ ۱-۱ تمام شد  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445060" target="_blank">📅 07:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445059">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚽️
نیمهٔ اول بازی با نتیجهٔ ۱-۱ تمام شد  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445059" target="_blank">📅 07:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQhzZyfz0R9YgyKQU1ayxJ4FxCYrVPd5Ny9EDB-NWu2Ums-spvuWCjU56dQry8wTqBwhqTn_TgWIEjilcnuXqygsKHcIsZT4RlKptPrPDZrJ_FjjN0uh1Zv1SFRq4p0DbGxzRXQrujsV9kSWVT_-AZf1d_q8-IPElFN9GCjXRjlLSHn06BS7v35yK5lK-aPeEJ3MP5MXXVaPr-xotPws1e9jZCW8YBVG_v-T2bQED2HK1GHvPfG08xQEpmjn5dZvSkXO0Qx5-0-XQaT3HEvNhRMNtwQIx9IPKY-XkH2WRzyymInAgGnl4CTUyaOB3QV71Rl2_Fk6-FsQQnd4YalCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نیمهٔ اول بازی با نتیجهٔ ۱-۱ تمام شد
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445058" target="_blank">📅 07:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f0751411.mp4?token=aBPu3dDxdxRC818nCLE0vbPhAGi7I-vNXqotLFR67a0Fgf3Ot7xthOsjhbC82GNcPFw2RRNyQlNnNPxonG8oF_WBbOG7g6uhGceJ7itglqXpq8lM_rX1VLhLdlOS7vlP2SnxVQ3lozM9Ohys_Fc02caSz8EBTeB3FfzV0MQLUiX6goHiOEy6Hd_og0w_DfkRVvyP4UgnNNkJ1C-N6TE89F5cC6UnpitOzNlLuHwKeRB76qm1sXZ-_mV8rGbt6vIyNhiL3q2mnwTcRO7So8fO93CCt5L36d-rMJHUhHXOQih5gvT64VArrGGGhjZLXac6ryWJ1Gmm7rb3AIeBiG9W-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f0751411.mp4?token=aBPu3dDxdxRC818nCLE0vbPhAGi7I-vNXqotLFR67a0Fgf3Ot7xthOsjhbC82GNcPFw2RRNyQlNnNPxonG8oF_WBbOG7g6uhGceJ7itglqXpq8lM_rX1VLhLdlOS7vlP2SnxVQ3lozM9Ohys_Fc02caSz8EBTeB3FfzV0MQLUiX6goHiOEy6Hd_og0w_DfkRVvyP4UgnNNkJ1C-N6TE89F5cC6UnpitOzNlLuHwKeRB76qm1sXZ-_mV8rGbt6vIyNhiL3q2mnwTcRO7So8fO93CCt5L36d-rMJHUhHXOQih5gvT64VArrGGGhjZLXac6ryWJ1Gmm7rb3AIeBiG9W-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضاییان توپ را مقابل دروازهٔ مصر بیرون زد  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445057" target="_blank">📅 07:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445056">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5644e6d580.mp4?token=tXSAEBWpFesUiC_Qy1sSs2Pk6SSTsI6zS1U6qy9xVy2yFdy5D8V4SM_4MyZZ0cnY9TONWpqyl4IMiwyHipr-wbO8ucXAAgf_1XXjV2lctaGEvgPcYicjaBnihkJe0vxFN9p4Lq5cQ1lmRsaGcp5bqgNO5o37JiE1vpl-lv_TYdVvYgVcurq-Rs3aADIoB8EGIQvND34uPDYXoRxAtnn46ggqKMBOVEfmGqFYY10ao77UPFLo_fvunuooV_v5Of2eX07DoGriVxncWPWUBbgXPM0RHg3fz4v1MMZyfTqUKja-vdDnoa6F3Vlar54KVBz0rTgBGvkaKTasLuPohA5fhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5644e6d580.mp4?token=tXSAEBWpFesUiC_Qy1sSs2Pk6SSTsI6zS1U6qy9xVy2yFdy5D8V4SM_4MyZZ0cnY9TONWpqyl4IMiwyHipr-wbO8ucXAAgf_1XXjV2lctaGEvgPcYicjaBnihkJe0vxFN9p4Lq5cQ1lmRsaGcp5bqgNO5o37JiE1vpl-lv_TYdVvYgVcurq-Rs3aADIoB8EGIQvND34uPDYXoRxAtnn46ggqKMBOVEfmGqFYY10ao77UPFLo_fvunuooV_v5Of2eX07DoGriVxncWPWUBbgXPM0RHg3fz4v1MMZyfTqUKja-vdDnoa6F3Vlar54KVBz0rTgBGvkaKTasLuPohA5fhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ایران به مصر توسط رامین رضاییان در دقیقهٔ ۱۴
⚽️
مصر ۱ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445056" target="_blank">📅 07:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSeZaQDGJEJ6z2s7CnvYR25wqg6pA5FCTrgmRTNlNBS7lhO0Hl6CIdoAZPseYjt0O9XbBs6wtls2e71rsoRQQAthVaan1ZoS25krW2RmdNq5m3Q01C3A34wdGajzXnzrsSGJR7jTiyQBgUt71LnrhsGQ4Lmj3WPNiNEgWuS8exxxot3ffJiPGW9Apj4Ijq0kBLq4N_E7_u_-9PKZSFZi0gBg0rNU-dJiVyYLu2--YmwTkQviyLDJeHTK7Mdq06zjJxVccMwYBZ2mA2h0K-QDx1pKTsKaJhT9uDbYS5e1XFasWFwHperL8mhrd998PXLpNvZjMs1AOgxxH1XNtc9fpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پرچم یازینب(س) در ورزشگاه سیاتل
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445055" target="_blank">📅 07:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtHsV1M8oeGqJwJDmrf_VA6PqwZkn0qe-20fpMagfwntJROAdnpZsUa2rYTTCBinPiURoV8OtBpJBWTtMl-_y5DDY7hlzVozHnO6dmuQDbq3am1jht77fJCD0S1WPJU1Hgsca0WsSlP44pt-GouA3bvg-51OZ_oTSsuNWLvQce8KzTDH8DfNlAsO1xExRuCPN_pG5HE1DlbjZGzZ5jkiOchBbtcv3KbbVZ-O4sEE6oK5lPPmn07N7tww2JdxyB87-6Am04Giairwb_5e-aN39NC_X7QwknstJbRkEPlk48_3kLBoEHzF8d9h--3xPf8uF13c2Pz7DDHVKkf3YFkmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل اول ایران به مصر توسط رامین رضاییان در دقیقهٔ ۱۴
⚽️
مصر ۱ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445054" target="_blank">📅 07:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">حیدر سلیمانی کارشناس داوری فارس:
💬
گل مصر صحیح بود و بازیکن مصر در فاز اول حمله با سینه‌اش به همدسته پاس داد و دریافت‌کننده هم در وضعیت آفساید نبود
💬
طارمی با زیرکی پنالتی گرفت و مدافع مصر بجای اینکه به توپ ضربه بزند، پای طارمی را مورد اصابت قرار داد و پنالتی صحیح بود.
@Sportfars</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445053" target="_blank">📅 06:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87b88bf91.mp4?token=ByZBqUUGMvP5QyA0KrqYSsfSrH6jYzLGr241Q1qIFTcLtZN9N1iJFwVFG0u4IBFXzMHR7lslvRezOFCqCFKNIn-FmqyorWcRA29udgqOCzMu71xm2ixyuqT_rtQvHbV9sjReAz-oFazt5Kit6HGNta9BK_dKhrkuObZ3uMV-Mq_cogoXLbQlsTtCgvgNpoZWXUEqovz1xXFMDXzvbTLLyV1fUROjQnmrPDcHanoOIeybUDT2gdlwtnUSSKIubROHHQq7OCzaenbtavBX-grC_6mwyCnEF0OqBHI1oFWHD8cHSindkbCS-4RoCWKXVN1Zv8ISiBXx6As_vuM8UUf9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87b88bf91.mp4?token=ByZBqUUGMvP5QyA0KrqYSsfSrH6jYzLGr241Q1qIFTcLtZN9N1iJFwVFG0u4IBFXzMHR7lslvRezOFCqCFKNIn-FmqyorWcRA29udgqOCzMu71xm2ixyuqT_rtQvHbV9sjReAz-oFazt5Kit6HGNta9BK_dKhrkuObZ3uMV-Mq_cogoXLbQlsTtCgvgNpoZWXUEqovz1xXFMDXzvbTLLyV1fUROjQnmrPDcHanoOIeybUDT2gdlwtnUSSKIubROHHQq7OCzaenbtavBX-grC_6mwyCnEF0OqBHI1oFWHD8cHSindkbCS-4RoCWKXVN1Zv8ISiBXx6As_vuM8UUf9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طارمی پنالتی را نتوانست گل کند  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445052" target="_blank">📅 06:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e348ba189.mp4?token=gQ7QByGQEpHtGniB5jsoJZ_ZEZAC5kGUWIPxAsp705CVaBTc623_GOQkJwhQtGJDv9vL5KT2GmP-_RIHssfojpPVJl-KmW_VshRFhNCSwlRCqikWDMAmJ22YL1RpZeFh1r6vApF15rVLcjPH9FDU2kdeAtBg4gm7MEMb1ba9CFMYzSJEJctue6dyHacliQXmcUVBxfSunIJNI-aWEgG7zNmMvc7KuGCWHvuaJhPxZmzW5mg7w0afGhaGDUlzJCW_bxwmGX-OcZPlQpBkjgz5aWhoWY__TCQ_nvkSsfeaG0RaNn0nVviM9JNvBzOdqHxlS1SyJb_uv4DSt5OapOeJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e348ba189.mp4?token=gQ7QByGQEpHtGniB5jsoJZ_ZEZAC5kGUWIPxAsp705CVaBTc623_GOQkJwhQtGJDv9vL5KT2GmP-_RIHssfojpPVJl-KmW_VshRFhNCSwlRCqikWDMAmJ22YL1RpZeFh1r6vApF15rVLcjPH9FDU2kdeAtBg4gm7MEMb1ba9CFMYzSJEJctue6dyHacliQXmcUVBxfSunIJNI-aWEgG7zNmMvc7KuGCWHvuaJhPxZmzW5mg7w0afGhaGDUlzJCW_bxwmGX-OcZPlQpBkjgz5aWhoWY__TCQ_nvkSsfeaG0RaNn0nVviM9JNvBzOdqHxlS1SyJb_uv4DSt5OapOeJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
پنالتی برای ایران؛ خطای روی طارمی  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445051" target="_blank">📅 06:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02fad4be22.mp4?token=Byp6uMiG5fq725CrV-4BPidTEJSUgGq7eMDHDj_5QCNJ3feJa4SAfAQDS5s6NDRtvLckfxNBr955zAER2dhBsOsikSfV6BN8R93bV6sOYlY8WJ7UHZ7mE_TYVcpbOZW5TIYlFjBJKsJ0JOMLSuDePk2DyCnPDUcIGRTE3EIIcqer_9TbdyBVtyXou5FYRUIXrN5mbpDQTZw-DkAOSH4RzTVbiA4It7qzbREg_RLu68M1EFN5r-d1UmwkGo3ru_t_8kw3kF-CXx9a104m15GvhKFK6DLWq85mE5KFf1qf6pvEw7Ff2hoc_G64SCPhGOo4_Ao2v0CpVgXePvmR6zuQ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02fad4be22.mp4?token=Byp6uMiG5fq725CrV-4BPidTEJSUgGq7eMDHDj_5QCNJ3feJa4SAfAQDS5s6NDRtvLckfxNBr955zAER2dhBsOsikSfV6BN8R93bV6sOYlY8WJ7UHZ7mE_TYVcpbOZW5TIYlFjBJKsJ0JOMLSuDePk2DyCnPDUcIGRTE3EIIcqer_9TbdyBVtyXou5FYRUIXrN5mbpDQTZw-DkAOSH4RzTVbiA4It7qzbREg_RLu68M1EFN5r-d1UmwkGo3ru_t_8kw3kF-CXx9a104m15GvhKFK6DLWq85mE5KFf1qf6pvEw7Ff2hoc_G64SCPhGOo4_Ao2v0CpVgXePvmR6zuQ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول مصر به ایران در دقیقهٔ ۴
⚽️
مصر ۱ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/445050" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea02389d00.mp4?token=Qp0FXMCW0-6I8NuOWXRzNvdI66brjg_Y1zuEPR8C0kQV6Mazz9zwJQSr80XJood3wYMCvwxFiYCz5nZW1tiZLxUnS6C2eMSG9Y4RvpyG11RU8sZy9JiOlV28-1KqxmGcDFKRDs4d7DUL4aXfGmHTJbJG9XlVBaMPMabWiUeExi8deHQRT-0ihDQtS8zHJSiA6XghngiuRCkY1DcFY2DPxrjB_3w4LYZKr-s5h4dVERuBr4EmDn3K8ACgQSeVXqRBP7agEnsP5xN1rL2eqcmKCYk22Pd8kiGf46oJK-0HPhvrthRofFMBN6j1JkxFd_QUUvls8NmRV1L7szAbbv83TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea02389d00.mp4?token=Qp0FXMCW0-6I8NuOWXRzNvdI66brjg_Y1zuEPR8C0kQV6Mazz9zwJQSr80XJood3wYMCvwxFiYCz5nZW1tiZLxUnS6C2eMSG9Y4RvpyG11RU8sZy9JiOlV28-1KqxmGcDFKRDs4d7DUL4aXfGmHTJbJG9XlVBaMPMabWiUeExi8deHQRT-0ihDQtS8zHJSiA6XghngiuRCkY1DcFY2DPxrjB_3w4LYZKr-s5h4dVERuBr4EmDn3K8ACgQSeVXqRBP7agEnsP5xN1rL2eqcmKCYk22Pd8kiGf46oJK-0HPhvrthRofFMBN6j1JkxFd_QUUvls8NmRV1L7szAbbv83TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش سرود جمهوری اسلامی ایران در سیاتل؛ بازیکنان ایران با مچ‌بند سیاه در این بازی وارد زمین شدند @Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/445048" target="_blank">📅 06:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d6204e02.mp4?token=b86DWmqDu9yoevYsviwbD-g5tUNvl--OBt0zsKswmZJIZSAmVbuX5m5AU7Eypt2a6SVZUrfYZUQOgKH7mpfglHwuOD9-9V1O_n9JerQZxapvPihc1ntEEKFT1y8eXdLmjA37euIOj8-ItWsE4ydeNK6LJDTP7E4Yt3qJnuBYLG_JbwMy43HSajGVJ0RZJcHIPTEX2dGUlO1t5gjgzw9ZdjaqlORBhQ48MeCYjLcBHmf0I4BqwHxpjQgi9dp08kT64IQwHbw0Mj4zQT9JO-U1k_AgYuLu9gJkQ9Ih9ZOmDDfS0pQhkpIXtP0WX4fJYvnnwECG2ygH26iVphVjRUrhfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d6204e02.mp4?token=b86DWmqDu9yoevYsviwbD-g5tUNvl--OBt0zsKswmZJIZSAmVbuX5m5AU7Eypt2a6SVZUrfYZUQOgKH7mpfglHwuOD9-9V1O_n9JerQZxapvPihc1ntEEKFT1y8eXdLmjA37euIOj8-ItWsE4ydeNK6LJDTP7E4Yt3qJnuBYLG_JbwMy43HSajGVJ0RZJcHIPTEX2dGUlO1t5gjgzw9ZdjaqlORBhQ48MeCYjLcBHmf0I4BqwHxpjQgi9dp08kT64IQwHbw0Mj4zQT9JO-U1k_AgYuLu9gJkQ9Ih9ZOmDDfS0pQhkpIXtP0WX4fJYvnnwECG2ygH26iVphVjRUrhfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش سرود جمهوری اسلامی ایران در سیاتل؛ بازیکنان ایران با مچ‌بند سیاه در این بازی وارد زمین شدند
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445047" target="_blank">📅 06:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d193837db3.mp4?token=hy7E7N8lcu8Hfo7c2QHbq_F93XA89Y1zJETXzd9JFA48oUGJ4UkuvtYrmKiGjFXrmSYsjmEipdxZBx5S7QhYo5YSVyq5RQn624zTjgAGM2Dg2IfFZewKB2AsdoBaUgb4DP_1vSuk5JSNqSLCU0uckmbpCef3KfRmXTnqPFUswUp0_9sug3GBpc03OA8_YuEfKzVlL2SL7PdGtMTNbw7EC13TceHRcid9c3oQiSBxH2GBhQJ7bu5bfR4mW_X9bUAGkS8jd64yIkMzuw_xe-KU3ZqmuKz-cipEbddSnF07gh87HOR2Y76kSIDRALlXi9qu92h5CS9F1sk2B9MR-NHZ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d193837db3.mp4?token=hy7E7N8lcu8Hfo7c2QHbq_F93XA89Y1zJETXzd9JFA48oUGJ4UkuvtYrmKiGjFXrmSYsjmEipdxZBx5S7QhYo5YSVyq5RQn624zTjgAGM2Dg2IfFZewKB2AsdoBaUgb4DP_1vSuk5JSNqSLCU0uckmbpCef3KfRmXTnqPFUswUp0_9sug3GBpc03OA8_YuEfKzVlL2SL7PdGtMTNbw7EC13TceHRcid9c3oQiSBxH2GBhQJ7bu5bfR4mW_X9bUAGkS8jd64yIkMzuw_xe-KU3ZqmuKz-cipEbddSnF07gh87HOR2Y76kSIDRALlXi9qu92h5CS9F1sk2B9MR-NHZ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورزشگاه لومن از نمای بالا پیش از آغاز بازی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445046" target="_blank">📅 06:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445042">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHX_etAF4d91OVDBWKptKtjDgJKZ_L2ExwbcVK3y2RaPpq9wN3kdPRDUvsM5J3nzg528a8swQMkUh8_FAcpcW0i9gv66dNo8dK8ANIxNLUdkS4qaLgEeXDNAw4ZQo0xb96QeaTI27lXTG0XKvebkG56iNFxKmP-FsSYvd6MxBN539T6WEl4pMFozTghxV2JFLbdkrwNPW40j0YBr_rpEDWOHidM6yQo4mibAzRZFkpckxtnQLFu7l92liKdrJxhlKnjKSkoVzSMr6Bw_kBQnNCmhPmR9Z1JLEPInPoFLY1i1csjxI7aQzGv2dwSqWWh6CiUXvlempWVPN2F_Pzb5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fz9G_4YnsWBbYXw5xWMYwqCO7BrpYIJDQ-QgpKxtDyD3YPs_Ql_djSoumSDZfFvPYxTt_HX4dpIq8WJYRvxJIMiSps_W11fAHnbumokoNkaeZXXs0S7fdbX8vveqGmt1ceJ0IQKtFIBN6W47QNX-J_Gg8GcEJird7hpMsePXRUscKY55HF9XANjLHdSo7Z7GyPGokMBf6IDZqEfG3qV2aEjtVpFiiBeGDcDpL7r6q5BwE3smpYMZXq7CjM6CncoEtvUOPGvjXPG0DV5E0rXH3N4nfvIUD47vcQ9EDyD3HePrRpZO3RRYJ_5YbrGV6yOkLPxVSZ4NuBn-g0rj-19wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jy4jbg0ah-9fTbHBHaCD2ZygaScKovYGmbI08cO3Q8yxAh_6Pg6TvwmqLKVIcZjNwE8uWLesrW0hObRDq7ZL11cCUpzmgfNSCkPluDLeuMPckdJVfcW6U7I9rjgdPh5MjR6a2GxOMzb6DhWRe6iIpDOtxJc6tygAf7JyYPjf7ARao8zySNlb9Ly0JhejVLIrrA-JnC3V1x0hNGPeXB0c9xChv2giJJMUb0Ry9YQnUUhIkL8oMUJgT9PsUQyAk5-d9vo-oByP6QeKbxHZiRE6ev2aMdcA1t7MvGvXTCwlXgELRYY-ha-Utcxjs8GonCzHR6ntgaQBFBvkLo0KX-fBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLlKmRVhzYFNjiD9zqPO3WQ60nOWX31woejC39gKGGdP4B8Ikzg9QhVQD3PodrC-Pp3YEscMDPjmTii9A85dcBwbzLQi08ZJoCdC3mJOnAoKjKMtvX6_Ab0CqjTq7yOxyMdZCNzB02E0jP9B-7_G18l0lEsN_KzUBIXoLnsNmHnV2iPolg06bILyNgCpH0_cCk5B5MoTkACAuoTDtj0xcwX6Q_GeJJ78P1biAHnSuD4wKH-QnX6drpWW4EZdwKUzjr_IjkHxdgO2LQIcwyF7TBokFeI_-Urglzy9NTMX0Xhg1rWKwygNeEID-NiRFyMT5mUGHRDH6B9hywkgnEi-BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازیکنان ایران وارد زمین شدند
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445042" target="_blank">📅 06:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445041">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK0DB1DZBgNT10ic0Samcv3voCD-eUfzbUtp1W0e45jKnwcNWtO_puuWM7DwRrET_rVr85eFHmmwMka4aDj-0l-oJi5DQ34_MR31H4Ql_uR13nSvJMh2zFIEWQ_wJDKtN7918SU-IASW3KB2dyutDT5IYFDQIcT2fGdi2JiQPU7w2_ElknAeMbU2xGgECxsSHkkxVK4lskcCz_YXVQBhI3Go3R5OdQecSJs0a2OZeoIDTnI4AdwqIqdfLv7q0iTXFdwwwvUCivXZ-bWIjDJitCxJpdPIYjC7E_TR0zQPALBoCmNcftXVF3qcX5YxHH4Ratg90uBXVSNi64Sn50zq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بازی ایران ـ مصر فعالیت ادارات کدام استان‌ها را به تأخیر انداخت؟
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های
کردستان
،
قزوین
،
فارس
،
سمنان
،
گلستان
،
یزد
،
مرکزی
،
خوزستان
،
کرمان
،
مازندران
،
زنجان
،
آذربایجان‌شرقی
،
آذربایجان‌غربی
،
چهارمحال‌وبختیاری
،
کرمانشاه
،
اردبیل
،
ایلام
،
لرستان
،
هرمزگان
،
گیلان
،
خراسان‌جنوبی
،
خراسان‌شمالی
،
سیستان‌وبلوچستان
و
بوشهر
با حداقل ۲ ساعت تأخیر شروع به‌کار خواهند کرد.
🔗
جهت اطلاعات تکمیلی، نام استان خود را لمس کنید و شرح خبر را بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/445041" target="_blank">📅 06:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445040">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">ایران و مصر؛ نبرد صبر، انتقال و صلاح
🔹
بازی ایران و مصر در گروه G فقط یک مسابقه معمولی برای صعود نیست. هر دو تیم تا اینجا نشان داده‌اند که می‌توانند مقابل حریفان قدرتمند رقابت کنند، اما مسیرشان متفاوت بوده است.
🔹
ایران با دفاع فشرده و نمایش منظم برابر بلژیک یک امتیاز ارزشمند گرفت. مصر هم بعد از تساوی مقابل بلژیک، برابر نیوزلند به اولین برد تاریخ خود در جام جهانی رسید و با اعتمادبه‌نفس بیشتری وارد بازی آخر می‌شود.
🔹
سؤال اصلی برای ایران این است: مقابل تیمی که هم می‌تواند دفاع کند و هم در انتقال‌ها خطرناک باشد، چه باید کرد؟
ادامه دارد... | در
فارس ورزشی
بخوانید.
@Sportfars</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/445040" target="_blank">📅 06:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445038">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPWewV6stSKxb8FpTLsK27FtXzAcEGo59F-xzk3qMqCAHv5KrwHhjm4gNM3MylwG7cNufL2VKYvWCMchz2PYB3gI0MBodiZn5Ya6as8NCviVyRjGY3EdX90oAtp0xisyrQIwE95fy0Q8Z69NuMMZnOuh2VP-XdZHCU8gsbV75vZlYgnAVWAbnEIdpC-iabkx3DbUFJZ11NVc-5cQZzKvgXs49EGWDS1AvvbrqoA0PS3OmSVAOa08YkdTlmZdUhyd9qLIHH5cekvM3Qn0CkDpNiTZKMq8Gc865TO2tYhtx1alHddOBoXwFF-pxq9RbiUBipZrwCBnaMCCaJMWrCa8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
جدول تیم‌های سوم تا این لحظه
📺
ایران در صورت کسب مساوی با برآورده‌شدن یکی از این شروط بالا می‌رود:
🔸
بازی الجزایر-اتریش برنده داشته باشد.
🔹
غنا پیروز بازی با کرواسی باشد.
🔸
کنگو مقابل ازبکستان پیروز نشود.
🔹
تساوی بلژیک و نیوزیلند، به‌طوری‌که گل زدۀ بلژیک بیشتر از ایران نشود.
@Sportfars</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/445038" target="_blank">📅 05:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445037">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib5_RlURpg1_sQH5jZWXaggjQ2NRDtSZLG8VPKUjQ32twK36StGUt_QXslLZZhfCrGRAUUzuVEcMEOossG0Be6zJpIMvOmsbNd1H8bSHqxpvt_HIBOkKPUNmcODo1c3YLoEddsAZo6HbVNXtx_E4X4KLEKVNbELQwDq47oQ6qlI_KV8fJUQduLSOUjkCFEynMq2snvfmx0_J-9jN3gryGySjcWKuOT4IlrcK7CDk2GO1DltWSeboymH_nAHvK_h91emNHULBAorULK-VopVL3VfknUzggV0nw_-qzddipPTFuIZ2rcAZvAhBrGC3V12mQuWFDXiVqF64CRt1Iz4PbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
قلعه‌نویی: مصر تیم قدرتمندی است؛ اما ما هم ایرانیم و برنامه‌های خاص خود را داریم
🔹
حساس‌ترین بازی تاریخ ایران است. بچه‌ها فقط باید مسائل تاکتیکی را با آرامش باید پیاده کنند.
🔹
شاید بعد از مسائل ذهنی و فنی، تجربه می‌تواند عامل موفقیت باشد. نتیجه دست خداست.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/445037" target="_blank">📅 05:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445036">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-xCTPzvKg1FwqZ6YVHmmGiOJDjkbBHZfBVmUsFALzHNJMJ8Hi_t4mZcJMExUCyAPfYooxo6cUtpjjFQZInpoI6qc2PHOyWO-sjX5mx1DgFHywAzz2X42bWLuylASnmNoi0uePVHHGY4yoXlyJEqQvA_OqBmUbuXbgmMPUQSBntU-KjbWh9Z9Gx8yexJF3FYvsByAwIPsWRejQ_gkERoA2sg5js3Uy7Z2TJBOdDoTruIavRoM3eJjibhIkmg9INJROecszCx5oR7jPZvjTt-qmfLZzzcZ7AW2O35cebPQZFLdm3ZAQvGKCjdmZefN2KLTcDlAhT6LLmf6Z3M0ZKuvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از توافق لبنان و رژیم صهیونیستی چه می‌دانیم؟
🔹
توافق اولیه میان لبنان و رژیم صهیونیستی را عملا باید طرحی برای خلع سلاح حزب‌الله و پایان حضور مقاومت در جنوب لبنان توصیف کرد؛ توافقی که حزب‌الله می‌گوید با آن مقابله خواهد کرد.
🔹
لبنان و اسرائیل شامگاه جمعه، پس از چهار روز مذاکرات در واشنگتن با میانجی‌گری آمریکا و در پی برگزاری دور پنجم گفت‌وگوها، توافقی کلی و مقدماتی را امضا کردند.
🔹
این توافق با حضور وزیر امور خارجه آمریکا، ندی حماده معوض، سفیر لبنان در آمریکا و یحیئیل لیتر، سفیر اسرائیل در واشنگتن، به امضا رسید.
🔹
بر اساس مفاد توافق و به گفتۀ یک مقام صهیونیستی، باید هرگونه تهدید از خاک لبنان علیه اسرائیل از میان برود تا ارتش این رژیم از خاک لبنان خارج شود.
🔗
اما این توافق چه مفادی دارد؟ جزئیات کامل را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/445036" target="_blank">📅 05:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445035">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8ePCwosmg_KR6taXlCnox1HvqFFjEojAY4XY4nu9gSfUmg9Kbid4eCNbtsShshZadlBgpEbLbdBXR3FAtSu7IGg5Y4fHOVHw9T3hzkFud2wj4gOIoAdZYJB8y1-vyf-bWXqJtBtW0hjKy9VksYMP0Y1Yhbz9HB86bMGgWwNp9bjtNdEIs6cOxxWA5rSERLn1UYBP22nK8DXH8FYIZUcBMsgOxsY4KgszNiLOTuHcgRI6Iinv0K4mjD9n2zH0zRsy9WkA1j2j3-Y_FLc4ySpfprN_Fz7JfFcuQUIPCe8KLcFEOqd7HD7hJLVZ_o8jY1_ldGz1rgfOCIr0MhA3w-ciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا مقتدرانه در صدر؛ بالاخره یک بازی به نفع ایران شد
⚽️
اسپانیا ۱ - ۰ اروگوئه
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/445035" target="_blank">📅 05:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445034">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9MqQIlNZsdBg-Aux4GX7tiZ48D0DBE7EtQI3gtoagMBzmmV2__CTQKPf2AWpo8HNjk8v4XUNSxlXtXGdQ_ArQurgfTLM_hsQHdjoU2iUiNUBkhla_RvfRUUVE-aP3qL8XzY_6A7AFpwJqpJxv7c6y9ccNBeJkty2gMISpD9--RWPQjrulCQY4nMdVhWAnRcIaxIOe-HBZv6dN3COk7rvjsRASPhYBg2EaZfdNIkblj5JhjVOEYgJ7v0ZiESIuaclP86PJ1m-8kl7styh8DZy7HxfLy9J_KYtLrI9Ky-sWf2x1-FAIqW2dMIyKQ4qN0XXqLYAOqneHGK4Krzmk4h0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدار عربستان و کیپ‌ورد با تساوی بدون گل به پایان رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/445034" target="_blank">📅 05:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445026">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mg9GcDzcZReHlxiaGuRW4vBe7Y0bQDiDiXCfavyS31RwFiRzN-e0iinl3JfpwjFKcpmZcg3FziFE1qD_gArLA7XBH7Xf6vYgVGtgliEzTpLhOF3GVc7h8ioAAsFcV4jvoQ4s38Np4IJyaWrpOz-3fV6SGqkpptMes-FEWkaD8Xxnv5uB_ZhJjLSgoKLZHeEZkYTQJANBt_doEfahDj3NNS10XoIqR7TNcolmNW3rcyIdqogpfJZ3136P_s80vFtzfD-S5K1Tra7JZO9HIl4bkiJp9f1ImkOkEzwLVQNhfJDhjYcwzyR31Zk8BuJILzf67JKnOpuuagD2lQEx3tTHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5yDNuEwq9ZUIg6sNJHzQX6Fiuz4CjxheIIrxWzrVJmXpyqxkk2SX75QBMz7BR1Kyx1gINLuRahxfuWRgj90L4qbYqXK32ZQysZxaeWu7Uao-UgXRdeYz_BkFPK11EObBXcyuFFHgXmxixDR-SDGA7ESrPqIZYE4Wht5qEKsP1riFgP_KpD5xG2CpXRHWOiUvyYCH1g6k1zuz3SORbkVYI5STngMy7y9m0oug1oEBjxOQyz1Cm2U-bah2EGkotk5bh-x_0_FkoHhM8lUrNJyQrEsbRpkuhkS7DDbkH-zR6nwJHg9W0sgC2qYrjixJt5KOa_9gWx-JMKXY4s2_WjYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0w-oJdfYrWBuRswwiAVdlelepQN5gYnJ8JCpiGv4JaoGrqdXcSWM53JARqrP0ZNVBe_tUaDEy4gQZFcw0pe3NibhahGtSeq_HXxz7YfL81yurg0HURfHtJKvYUv5thOHTjOClAAx4WgEdUCocvkmXstn1yKAo5SG5g70nQjGecfQ11KgxBmi24J8glZtFYj7mK3qRP5MQXKsc2A2QoPetB2-PqzmzqdtGQaoU3csV0icUBzeu1PWNn6954vJFC7YM064dnMEE-QL2wUyUs2Tu5Fv2BCilByiHvp9e6njWI5oaX1lPlVgYS7iRXnatl02ujlrHnCh5Y8W4OpIH7SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSyY7Inm7EUlM0Tgcx3jwj8EBKec54FefVA-u0_jwxUjBNhk4x4p3aXozdWhocASYq67n8npPoMhWJiu5Op-GwhD8LxlcPSYu-4JxkCEMmPlfZ4Vfy-RtGlqIuabIjZCVNSU85K8S8XGcRkke0Mdg7BTCIJZw0tqkcpcoVUNKhWFd2EojVJORM3nDdJjCZZR6kXUHDzr_9aqLo2V9alFGGmlovcoVqYVQcnb7dteK5Dua6_0C1UdeIZCbvrZ5T4sre2KnUSoGM4jQUl5kbTo7hzQqK-LKVNDP1OznIACCgJUx_Ry-PJ4GP-H9JhfNXCfvW4uN6Waw49RP3L9C0QshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIJgCcO2LuQePDG69GQXj9JdaxLVS0EShi4MuQIEKY4wBiy_-1su3sZdk7wNBF6w2B-dPyc-J3au5cjTh7PgAwASRwd9QYOhijO0Ds9e5SDFkjKZhamXHpOxEIT3kpDELbzxlWv7J86D3zpf6BJHlgn0I3OldSKeGgxgtCO0stjHctcv86ptisTjhiyuvIu2sGYw0MK-YftVhe4ZiQ9hKzJWJjHqYK4vytu36h_8WVutsHmphoZYCfVDlBSX-D2WUNOE8q5J3G3OjbvMVL_aRpwmju8lZ2SCjgmfX2wWRVdLkCJoCvkbfmMJrwo7bQFVpmShAJV9SDyeQ04EbXeyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mm3z5-9Vp9eQGmBLzWHUaho32RPffFsdphGnoQClr1SjkU78Kn16xulDE3xALf7qY79nOCDLp9IrJFdk2-oQEZW4svz4lmg7WIQQ830LmrZDGhG2jmUkD-AH-wYYC-nfPO3AhoARlvNbgfV6u1iwXVICxJYatdlMlhR7gob7rOJDmC3y_chQ7qmEI8FQG-kuQevCnmHKAh5J-DxAypv2Svs04_3ZgoFFL754acC1Yz9bzyI19AuhQgK7FvVLHGiCRLoVx72yAMnUywUAqj0jTix5Hj5-fjk6zOwzL6u3P7Ja-92OrBWsjQYJ0rmNToMPdAvVgHtJuUhLrBRhKBKXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnIbeYge56e5_CKR8pWaN6rIwCbBaN6D16mfff8DtgXmQI8nIke8Uyqf5-Qpm825TbYneH8trxvU-UhQmgl8urUdZOJI590DQ8RO8w5pafh_WKEAZ97hFbwzo6BUj_FWSQvSw-PCjfu7ZbeNLuueYqiRlJvdWFSzxqkEMFctC0bAHs7NQ7CVEMpneBEgRB9VKwRYHTC1zXPpO5RZuuLZ-t-tGy2RcrOLo8sjrtmhf3rdx4J6YjYrlWPIpAyp0IFEVpyiXH811mKqq-8xX474-ryZCaZhRJ-kabNmRBIS5tm4O1S8XgXI_yztE2fTPkVunfP2xufrr3RuomPJVsnnuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXH1FgQTUUGsfDwKGMG5Vq5g9Z1mvnHCq_R-QEbeYY-Z171BnnUgFskt4fRYZqH-gOIYxMpFMgQgXc966owW1d9Y3PAfCLrKav-Lm0LH9I74r_b7ilnARMNhrmJjnRm5kvn5gthiPl-X0b0C3ic0EAJqOOgqTiDL3x3zBdtW61WHfHYUwsUwI6nVh5GzmqNd-0bPg-LvSLD8AmDHE_EgLk7GeCkXT25KMezWeQknyFNA81Qi4jOj5XHC-uTpsZjU-zt-2K50kp09zTu6gMVHz-_OOaWz-IDXMPS439M9FoBzKrNhAwlozOXKcldDgNv1cSMlzVelC3PPmr1YCWlK8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حضور بازیکنان ایران و مصر در ورزشگاه لومن فیلد
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/445026" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445025">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o56tthm_pdoDtzb6TVJp5_eAJ_islcwSPGgLFulA_54dgsl_QEj3wdOvOlDdFnMe_frPgKpyLPuTwrJWvDViBAKN8A6jKUUtw7Gtpj0sQ6vAwxM0yXm1lAFjQZkzz2rbs81D3D92LubfWPv4XWxUBRuonlmjM1VuutatR9mlMGNuMbCoaA7M1jYczc5NtdckCbIIF1E0ZTd3ld4b70LcBT9UurWxXDPUphVsvih6-2z92Bwi82z9Mf-6nxoUA0hdWqDW5vmMqjK8y55SpDO6MUuStEMCB_32nx02xnvIWrYE4tvur1680epCaqC4kNyrXr8Xzz065qyLhcEDrw1Oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعال شدن آژیرهای خطر در شمال رام الله
🔹
منابع عبری: به‌دلیل ترس از احتمال نفوذ افراد‌ مسلح، آژیرهای خطر در شهرک صهیونیست‌نشین بیت‌آریه در رام‌الله کرانۀ باختری فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/445025" target="_blank">📅 05:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445016">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpcRbjvDNb5IeRMsb68TKHuYmPoAoxjoCweFhaOk9WqjVbtM5-M2hxl2dflBNi6rbDnWxcFK8f7_dzQiZym7utW54awZxKUnoYDDMIjasBNh_flA9EpgqdOncvew-jz8OLPC_xR5b0c5W5AbnIxjmG3ySNE3TuSTethhYdmpaPNiyNyUahNp6fM_n-k96lhknYtyFrn7DGOmI5qV0RbG0NafcQ1VSWgKSnL6NmDVmTEb8nLCYrg4dQzkl-guGW1eHjSW9mLASvhd73rlu_YGrGeu9bag-XcYJuHEMhmBbOPKymg12obgrV9UB-A-8lxE2KMeu_kS970uWFxdwYYYOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_9E2e7BkhA-bhi0BIaNrhOisPUXA_Kr_HEiNRv-QjyCr_EWDwSFT_alqjCxtDg_X8u5_7tG7eDpOkiFycTes7Z8Urw4IKReS-F9WVSotVvUmSOoCV4OmoZ-Ctkdx_KfdSGbGqQuMfR-vTDpOcC3Z7lw_Un8RTQV3-JBQYaNLPJevNfGEnwLur1jx_5k6YtCQCgyxHHGxu47ruUq4wivU8YsSsWQePeEWf6byiK4H3R3JSk8oUwnQaUmvsaLvL-DE8aNxSwZz4nuksf3pwVj-1ICs75yHq5mVphWvktPMH7iguQ-o5ZKcAzzDORVe_QDG0ReYfBpvbRBKZmWN46nEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGQvHKlQpvNnzTshtwR9T0pYyTc6j8aW66ZJxtn7TD5V18EPtjty-C-VwnrE1_gQ_5WxUSMycuqReFR_O9jCCkodxyVKJkfkROTHdHPI9cKss_BWHEcqCi9rU0EDKWwxZ8rCKFZyrXwg2vkFURQdyTq_t6sBiOQSF60outiq6VAs_k2wGAYDAQT_bPWGZ6nfs8VofM_QxOZJd5vHb5pIVe5p8GcQyaGozoPef34n_nlxbzExUuuwXa3MOSL6SOretTJWNCOgAMf7mAYd46w50ICVeMwJQeamv33SAWTusCbbqaTlVMjsJke-dOxgaLRXZqsql31A2-0Owsv5i-ewHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIK79hC-lzYZjJKWru9H321m_Y50iowV3cn3UHgBgoPDDhLkO-cvdPy92nVPLlRUuPadTEfo3VC-ZQNi1r8mf2mKOgLflsnQWmu8tM55Dcak2YdNneO_OO1lVVb3HIi0QC4uxppadw61KfvFb1cm2963CRV6Cx0OkwThU2aqQXShegDT4FIsePT1zQvbnw8r9kCFs3QGFIhkD_rMlkVacG57AOkfJrQcotS3o_RzYYqhsnHyfXJCHVVxc4XOv7KsKDvidizu5nwD0wwAvBBKhLygZjov75TUFzjjcgYnuBrvs2HEUqGjineQ-CERk5RiLABLCqjJehpcfmNRFKClDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ou500dlY59yFsfF7gTb0QagW35M6AIZ7rlCocWpzb2Mpn-g5fs3uDofwAwL4gZltRgmO_9yqpfGKd5w7qEquqz4H0CWA035wQj3rbc93iizvnAwNz_cGvGG8eOuj6hsqFRyMyaW_MJNA6El-jlXD98fASR_HBX9bazMqFStNZ5kKwe946bIgz-Ih2jXGDeWoQxuLj3Xdsvm-_OXqpMQxs-IKoMDH5sZv7wtQtp5wJUrHZWA6Vdp1xKXtpkmWwLsDzX3ya8UJ-xiuIDHFL1mEOvzrqSgdLzudrAPhBLw7Uo5wqM9pb01XWhzd0ywCJa2ug7Wkzv90s7P9ad0h8YCPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ij2YUV2C3CEvp6Rb20GLd5PVpASSHogGgP-aSyZ7Qnmx1kppHHyxfwDsWqHdMtprybmahpT73VBA7eJ-LctuuQ7dv15f55bAvumUjK_4tRfkSAglXr7M9Ng-yXczKB_ylDnSQwgmmAV-ZH6MrSEowPZsMx-SGKEuD8Q0etCgQUtuB_TqCirabws0sKzIvyMvRBovxXFBmFyz-H6JFuLCkCLQb5jp-3DEnLYSCDM9INZTRuMBsKhtXQL6sLK0SJqiAlTawOvn7TT8gc3z5WC_vgtssVYIsHan51fCiAlEz7MmGE5lIG2JvqnqDjhmgt1Ck78HJtZuD4fOzRZN6RhAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npIDJalGjRoOmNfHxr_XfICLy5gFpqjUf9o2F8NHhBJ9zYZ6nZ9Nte9wUlvLstjLwXUA7rGF23HBFoCfWqB9U4yLbcNF2CaTdKShLWhvRto5bMjPe_t6nUtagJ56Rb8Bo-r4yYxGYur_u8Xj57ddxVq6nrvPjQWzY-uBuavYIxRsoTQ-qu2__ST0uAuh7ArWALxDUexsdnGPdYO8vS2SNGf5pO2kvkOEwTbhTx0jM01rHVmdqNeoJwxsyYZowYypNFFxmBV966qNPQbxZyb4TfP6gVrHK2smznf6F_qFIxvufvH1l9GGhvh1RL8OzJGcNf7SCsOWq04z_EAwuPtMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL_yIH1srLUVfjBrvrZTisdxaBY0Z1E1kE1t4238nqoryBDI5oNFnO-vRM_Kqd-XDk7oh1K773RcgWbqIH103Zc7SgmJCfcXpv5FXAWcueQn55r99-ptrg8rpuBRZwHKOUHhMOOsf4RSnlg9KYULSe0lNWdO-8pX6nZA1-UHGCYkF5BFLIU4NSiLrcegzphet-FcRPa4GpXiAPr7k1S1N7etxjIBldzQJtlZAbzcaynH6JFKw7qXwa9qSoAnsjpAM_dDggdp8n50RAh-B0ZaUCedFLbhijyrCsnGB3ebnOhFw8OFqDo6XeHu58dC0yoqQLsTbO6PAoAhpUZKdU5qOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwodjCPxbegMpVI7_zmkBB5M75q_4fW7jiIqEZ84pI2xGf4Z78G9AKJ9gb_8tFjlNi54Aett898D6A1TlKJILJr7I3D63RzJxb0fLcfI7JBcHdboC0o5mkUdzNsHPmaYqgsnDMtE9NZ23rmz3wuVov4GlhqKvpza5Pka6l24NQ_odzkOSCifnxEttmz0DaKGUy6TOnBL3lVZROlHcXuKxW3OoeSORhAfbbRQvFs6cxjmNl-dVTZLAeKq5P9j-R9L2dvSsGHs-EW-ccoe_AJTzlkC_BhHL5wv_SP5mDQVx46XOXVNEb7LoRyfuGHBXBUYXjierewHExzPiLKab5K6uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
تصاویری از ورزشگاه دیدار ایران و مصر، ساعتی پیش از شروع بازی
@Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/445016" target="_blank">📅 05:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445015">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4h0RBO3wsGb4OP4v6G7iScrxwZczIut85CK6379xjW125kchL6RcEBTAcyHmGO3jfBs2e2SXykBuaCreScTU9a4Ouk9UrudOmipzhtpp20gOzEOKjG940t_eBF0gGpVPLL-L_H8-CpmNotxa6F0E_PtiCe7uv0yuZbX-XaBQNMxzYOFPJWiPTp57Iu9h5akU5QwSE__uVyrzkrzV1ozUK2-FZMoWWJn-xJa3UQ6LP1swKrKNRf0RTOfecl0silQrEsSh7MTb_t2R3WLodpQwLOF6_12yctcJWGgbqIuI_NMQcN5oejQa0nB9zFt8Nztbbw4Gnm8IqJg3RffUNDRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب ایران مقابل مصر
میلاد محمدی و محمد قربانی برخلاف دیدار قبلی در ترکیب اصلی تیم ملی قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/445015" target="_blank">📅 05:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445014">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2904b58e7e.mp4?token=R5tWymVPzGcAoT8G8grZ95qcAlFaT1MCkyfH4XMjeqTt5eVP71X1urnIoWvfcIjZe_ua98-km5QPru_7Fi6XpVTspVNgAuIfVxJ-uAMDs8dPxyKKYXXWXaeSoxv9JbhYzKlRyVdaHW4IWS-oKQQgjo8_90UsP1pH2akZbeeZLK52hpbJNvHEv-2R3CbPoW0VoTws5JtaCkf7nc54Vn-hDJ7j-m3EPnYYGw4fKtpD91X_el93hdAwGdFhQz-FAUbWfZGDqTB0vVO1FKJhVUSLS_jyrAsl6xPD9wTK9MCRP2ZIUkf5FsRoKmwtJTSdCVUh15rxyvhtuoA4ojjvs03ZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2904b58e7e.mp4?token=R5tWymVPzGcAoT8G8grZ95qcAlFaT1MCkyfH4XMjeqTt5eVP71X1urnIoWvfcIjZe_ua98-km5QPru_7Fi6XpVTspVNgAuIfVxJ-uAMDs8dPxyKKYXXWXaeSoxv9JbhYzKlRyVdaHW4IWS-oKQQgjo8_90UsP1pH2akZbeeZLK52hpbJNvHEv-2R3CbPoW0VoTws5JtaCkf7nc54Vn-hDJ7j-m3EPnYYGw4fKtpD91X_el93hdAwGdFhQz-FAUbWfZGDqTB0vVO1FKJhVUSLS_jyrAsl6xPD9wTK9MCRP2ZIUkf5FsRoKmwtJTSdCVUh15rxyvhtuoA4ojjvs03ZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتوبوس تیم ملی ایران برای بازی با مصر در میان تشویق هواداران، راهی ورزشگاه لومن فیلد شد
@Sportfars</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/445014" target="_blank">📅 04:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445013">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ساخت اندام انسان در آزمایشگاه
🔹
پژوهشگران چینی برای نخستین‌بار موفق به ساخت یک مدل آزمایشگاهی از دیسک جنین انسان شده‌اند که می‌تواند مراحل اولیۀ رشد جنین را شبیه‌سازی کرده و سلول‌های اولیه تشکیل‌دهندۀ اندام‌ها را در محیط آزمایشگاه تولید کند.
🔹
این دستاورد که نتایج آن در مجلۀ علمی «سل» منتشر شده، می‌تواند راه را برای پرورش اندام‌های انسانی و توسعۀ درمان‌های پزشکی بازساختی در آینده هموار کند.
🔹
پژوهشگران معتقدند این فناوری می‌تواند زمینۀ تولید انبوه سلول‌های اولیۀ تشکیل‌دهندۀ اندام‌ها را در آزمایشگاه فراهم کند؛ موضوعی که در آینده برای ترمیم بافت‌های آسیب‌دیده یا حتی ساخت اندام‌های قابل پیوند کاربرد خواهد داشت.
🔹
از آنجا که این مدل‌ها یک جنین زنده محسوب نمی‌شوند، محدودیت‌های اخلاقی بسیار کمتری نسبت به استفاده از جنین انسانی خواهند داشت. این دستاورد می‌تواند به کاهش بحران کمبود عضو پیوندی نیز کمک کند؛ بحرانی که در حال حاضر تنها حدود یک نفر از هر ۱۰ بیمار نیازمند پیوند در جهان موفق به دریافت عضو می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/445013" target="_blank">📅 04:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445012">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR8cG7fl-Fee7s6Ju9Nxg31P0I0XZiHfEx3dktIKfL2PsJ7GtVztcxg17TSRgXUp94y-1NIIhgJYydXx7cHq-xTsZoT3seRA609C8mnzaE6m6Lqh3horHxAKySmobfZSvBE14YrSy3MsyynJrZTGH6RUPeO2URElzSJid0d3WZgA8A12a6uShD4Rq3D2FSLy_75zcmuM-DmttZn-axJNaUOuP2HIsU0fg8MxHJlKIZcTpIu1FA2R8qRUtbzbEE4mm6Ucf0PuiafCmVdPFoVTbQ_c6Cs_ZWaDRR4Y6idckN8vr1vVoe3SRwbx5saqMyRkC6gqicT4dLUrTTN-Tb9U5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور هواداران تیم ملی با پرچم‌های مقدس یا اباعبدالله الحسین(ع) و ایران، در هتل تیم ملی در سیاتل @Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/445012" target="_blank">📅 04:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445011">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">روبیو: کارهایی زیادی در لبنان داریم
🔹
مارکو روبیو وزیر خارجه آمریکا گفت: ایالات متحده مفتخر است که بخشی از توافق چارچوب سه‌جانبه تاریخی منعقدشده میان لبنان و اسرائیل بوده است.
وی با تأکید بر اینکه هنوز اقدامات بیشتری برای اجرای کامل این توافق مورد نیاز است، افزود: با وجود دستیابی به توافق میان لبنان و اسرائیل، همچنان کارهای زیادی پیش رو قرار دارد.
🔹
روبیو همچنین مدعی شد: در حال حاضر گام‌های جدی و معناداری برای حرکت به سوی آینده‌ای مبتنی بر صلح، شکوفایی و همزیستی مسالمت‌آمیز در حال برداشتن است.
🔸
ادعای همزیستی مسالمت‌آمیز وزیر خارجه آمریکا در حالی است که طبق توافق کلی شب گذشته،  ارتش اشغالگر همچنان به اشغال جنوب لبنان ادامه داده و مانع بازگشت آوارگان خواهد شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445011" target="_blank">📅 03:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445010">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/472e134bbb.mp4?token=RjmJ5wMTbiGaH1txDlJtp13UJtbaLBuyPzh6ktrcth_Pg3vioxez3R-0hrd39vcQjrLL4AaOdVoXepW_hEf6leN1GkQvPgNA1ZHUYZbC08-NRjbirxV8cigfeqzkgOSvWd4esUeOofKyreqbal6zlJjSjstld7wqeNsgKelZ9t5GUj_oLLi5c6KtebLQfhPrKUVFYhMS4m5VY2IAHS7VFyenm3R9yqySNhzkf8qXH2unXnayerBQVMjEe--9V0V8b4gaDnXnneBKl5DtmcfJrtJNZ6939HWeu5uNfF_YKDTjjw6aOYQWu-O2JB3u0qNq_eB2D5hBJ5PbrPl0oexAUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/472e134bbb.mp4?token=RjmJ5wMTbiGaH1txDlJtp13UJtbaLBuyPzh6ktrcth_Pg3vioxez3R-0hrd39vcQjrLL4AaOdVoXepW_hEf6leN1GkQvPgNA1ZHUYZbC08-NRjbirxV8cigfeqzkgOSvWd4esUeOofKyreqbal6zlJjSjstld7wqeNsgKelZ9t5GUj_oLLi5c6KtebLQfhPrKUVFYhMS4m5VY2IAHS7VFyenm3R9yqySNhzkf8qXH2unXnayerBQVMjEe--9V0V8b4gaDnXnneBKl5DtmcfJrtJNZ6939HWeu5uNfF_YKDTjjw6aOYQWu-O2JB3u0qNq_eB2D5hBJ5PbrPl0oexAUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور هواداران تیم ملی با پرچم‌های مقدس یا اباعبدالله الحسین(ع) و ایران، در هتل تیم ملی در سیاتل
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445010" target="_blank">📅 03:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445008">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe6c5dba1.mp4?token=GKrWvF1Dc-uQM_tlAd3-Lz40dB8eB3uQ1RRmNv0ZIxAydrnft9h2N79ZUDowmoUeikPg2x-MHdwDqhG2xMnbkKjwYwjO-xCG40OVgvF065NUDj6XzI7_L_wApYNQq6tevsexraGEc1AWIYTBC1nrHrN63mSG6tphUFS5XvVqa2lAv-XEiGXcuFWHq6WPXkyctUy7FNQGn3DAOEtZFONIF7R7CQyHcU0e09qEvG9Gv68GYDndNwoFnNNx2ZEJB4VCtq9V4o7zF2U-tC3Xh_osOoGtaMmCldcdTvDpu5LFnW_Ea-_Yu2P2l_4nH_Qo4PM8Vm_YUJML45JdPjNqJ5l74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe6c5dba1.mp4?token=GKrWvF1Dc-uQM_tlAd3-Lz40dB8eB3uQ1RRmNv0ZIxAydrnft9h2N79ZUDowmoUeikPg2x-MHdwDqhG2xMnbkKjwYwjO-xCG40OVgvF065NUDj6XzI7_L_wApYNQq6tevsexraGEc1AWIYTBC1nrHrN63mSG6tphUFS5XvVqa2lAv-XEiGXcuFWHq6WPXkyctUy7FNQGn3DAOEtZFONIF7R7CQyHcU0e09qEvG9Gv68GYDndNwoFnNNx2ZEJB4VCtq9V4o7zF2U-tC3Xh_osOoGtaMmCldcdTvDpu5LFnW_Ea-_Yu2P2l_4nH_Qo4PM8Vm_YUJML45JdPjNqJ5l74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکت جوانان لبنانی به سمت مقر نخست‌وزیری در مرکز بیروت برای اعتراض علیه توافق سازش با رژیم صهیونیستی  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445008" target="_blank">📅 03:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445007">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مخالفت جدی حزب‌الله با توافق با اسرائیل: دولت لبنان مشروعیت ندارد
🔹
حسن فضل‌الله، نمایندۀ حزب‌الله در پارلمان لبنان: مخالفت حزب‌الله با این توافق جدی است و اجازه نخواهد داد دولت تعهدات خود را در میدان اجرا کند.
🔹
نتانیاهو در واقع با خودش مذاکره می‌کرد، زیرا…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445007" target="_blank">📅 02:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445006">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5K6Fsp6TRMOysa6b1bUerQ1mDBrofpGptZ0urEANF37B-zB-YhDClNxMGDb6Bgy7ur2oXokMbyyRMq3bQU0hYmrO_rORb6Ly5urD4xAzLh-iyLZE9ABll9pKpZx_fXh1iWg982Ddo4X9NDaVQMyB-_n1BXB2h6lZ6zsyPhHbFcILiHBgzIommak9Lk2SNZDPmOkwLqBOE6qIs4-wSj8rm0ZjoZkJFuhjJF7VLt4AhY8ghfyR8kNyP2H7FNf781dTtefrvcDQlXxd5oUJmfcqdhpc7GVEOkayCLwVALY9LciUVXhGlW0Rj8J3GNbUbk1OpRrT7vuYYYzDFGKlZRiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمجید رئیس‌جمهور لبنان از توافق با اسرائیل
🔹
جوزف عون ریاست‌جمهوری لبنان: توافق اولیه نخستین گام در مسیر بازگشت کامل شهروندان لبنانی به سرزمین‌های آزادشده و خانه‌های بازسازی‌شده آنان است.
🔸
این ادعا در حالی است که مقامات اسرائیلی از جمله نتانیاهو اعلام کرده‌اند…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445006" target="_blank">📅 02:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445005">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ce74947c.mp4?token=bu4WKpM8135Y-eEyzzR0rJEaNd6syhcQj5YStoBi3JvJRVIs-0oRYmn56wHd0TNHX0PuC7xZtK67p4-hNRjb3lhUBeZ5yFijlzq6dO5wjaHlnUOTFhSq63rp0iah_QzZfHXAAGN6gGcCpAPcUJMYZTl3kUKjTbEeu7RgSvyY_oByZJngvAncBUlzQfQXIU4wxG1QBgAyf65DNt6K0-Yfjo4n1tUimfNsk_uOfHImWfCX5msxau6H2g8bW5MQEcV6y0MB7K93CnEEOWZr2Kuk_tg6xzRfjoABSZoSQ859ELx62Fa5p6wtYQGihGh0ZjCynpaveJW3lv7AKqygYHtI4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ce74947c.mp4?token=bu4WKpM8135Y-eEyzzR0rJEaNd6syhcQj5YStoBi3JvJRVIs-0oRYmn56wHd0TNHX0PuC7xZtK67p4-hNRjb3lhUBeZ5yFijlzq6dO5wjaHlnUOTFhSq63rp0iah_QzZfHXAAGN6gGcCpAPcUJMYZTl3kUKjTbEeu7RgSvyY_oByZJngvAncBUlzQfQXIU4wxG1QBgAyf65DNt6K0-Yfjo4n1tUimfNsk_uOfHImWfCX5msxau6H2g8bW5MQEcV6y0MB7K93CnEEOWZr2Kuk_tg6xzRfjoABSZoSQ859ELx62Fa5p6wtYQGihGh0ZjCynpaveJW3lv7AKqygYHtI4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج بازگشت زائران کربلای معلی در مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/445005" target="_blank">📅 02:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445004">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
پاسخ نیروی دریایی سپاه به تجاوز و عهدشکنی آمریکا
🔹
سپاه پاسداران: به‌دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان، ساعاتی پیش رژیم پیمان‌شکن آمریکا نیز مانند همیشه دست به نقض تعهدات خود زد و به بهانۀ ممانعت از تردد یک کشتی متخلف از مسیر غیرمجاز در تنگۀ هرمز به حملۀ هوایی به سواحل جمهوری اسلامی ایران اقدام کرد.
🔹
نیروی دریایی سپاه پاسداران انقلاب اسلامی در پاسخ به این تجاوز نقاط استقرار ارتش تروریستی آمریکا در منطقه را مورد اصابت قرار داد.
🔹
بر اساس بند ۵ تفاهم‌نامۀ اسلام آباد ترتیبات کنترل عبورومرور در تنگۀ هرمز با جمهوری اسلامی ایران است؛ لکن آمریکا با تحریک جهات مختلف در صدد تخلف از این تعهد بود که پاسخ لازم داده شد و من‌بعد چنین خواهد بود. در صورت تکرار تجاوز، پاسخ ما گسترده‌تر از این خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/445004" target="_blank">📅 01:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445003">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مجوز آمریکا به اسرائیل برای نقض بند اول تفاهم‌نامۀ واشنگتن و تهران
🔹
وزارت خارجۀ آمریکا در بیانیه‌ای تفسیری از توافق میان لبنان و اسرائیل ارائه کرده که کاملاً با اظهارات بنیامین نتانیاهو همسو است و دست رژیم را برای نقض بند اول تفاهم‌‌نامه با ایران را باز می‌گذارد.
🔹
وزارت خارجۀ آمریکا در بیانیه‌ای تصریح کرده است: این توافق روندی روشن و تعریف‌شده برای احیای حاکمیت لبنان، خلع سلاح حزب‌الله و برچیدن زیرساخت‌های اسرائیل ایجاد می‌کند و به اسرائیل اجازه می‌دهد تا بعد از حذف تهدید علیه شهروندانش به مرزهای خودش بازگردد.
🔹
این بیانیه کاملاً با اظهارات نتانیاهو همسو است که گفته عقب‌نشینی کامل از خاک لبنان تنها بعد از «حذف تهدید در شمال» و خلع سلاح کامل حزب‌الله صورت خواهد گرفت.
🔸
این بیانیه نقض آشکار بند اول یادداشت تفاهم میان آمریکا و ایران که واشنگتن را به حفظ آتش‌بس در همۀ جبهه‌ها از جمله لبنان متعهد و ملزم می‌کرد، به‌شمار می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/445003" target="_blank">📅 01:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444998">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTYG6AOb8eRlLlCPY5TziCRlpyVCUUeEnx1KIoEtEdNxeDr7o02t9fWWpmBN9N3_8WXJArZhYnBXbzXsdqj_K8Mkrp7p0prbbH82bD0iPcPtTq_Abteq-FbzIDC-jvyGm_ZM-L1Lgi4grF_oG5uTaoDfJE2RORfl0KBUw_H6-nUuc-6Ucc6odOaOeseugYci96AmOrxwhBfh1KsjYKNmiBrJBOobpbJGrU1ZtD4OopkIAX8UZJlmb48PxaDjT5H2KPBzM5W_jlxNi2oTpIfDmjL9O_H0CIlisk2_yBqtn__LnqYEc0mvjufB5UrfAS5imza616ps-4TKwfqgDG3r_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSEKEkZjjTfszkzEsYIwSSbFJoA8lng-Iz7kr2R9oUKutB-zjELmF0CK1X5HAVBfv4lnDFoPLMiRD45m48yiED_HIl2ALGJtafMlZlsLFOs1QqI4-EYx6mkfNiVVYE24RH1YDCsfPoQT4nNmMjBaCdXetqWmq9QYniCOfvGgu39797hMlCXItoJtpuGrHLGHu7iNzQKXvievdsT8m_gZfNAIb4tdVq3qkg5YvIyYAAYElXGw0N_vic7q9X4khcy828ZKDNV3w8F5pyR2I71NA8H3G1rrx2VgDyAeZnMRWsOwSaffefY46ZatLGIS94Y72u8YLRaXVuhCt_OUnAKPCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRlrl0fRiV-R_5RGBFTy2FUNhaSNIAmow1xbf54Z7S1ly8gRJo5tfG23O0kQkrVycrtaUeY9PKM9KZiEIHp-W6zUMj-o5ZJFtT__vMeeNTqq89Uvmj4niToh7WnLwcxWT9RgeSuVlOJFWTQ16OoxrBAoxJcHfT7Y9f3Y5H_31ZOtuQbu-LBmuGgVDKF1CAUGlb4OZfcp0RbxUrGieWrgO0aNxJBbOlkFkU5scY9l9InxpXY1wbSkStwW4ZJ0wx9WRbi7XE8HopuM78VGy2_qF8C7OxFqUjEzYlz5n3St8vN7gCZZ6xxoL5mkZN-Vj10Z-VGNrFp79n5DoghZL1afeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2Ui5n364kIClpYuxwr8A87tYLStId9p2JfG90VsLrYv6_TH9W_UEjkwe3DKoDOokDQz__w84yXQVW7GYOE-QacqyKLOjkpHH2-BbLYGZbNzaJsC7DBjTd8MOAdzy2HZtbs4aazGXaIqL1UVnSjXFjqfLyHz4lfHtqNw1rJhdfXfpuqr8iPO9cQgaMnzR64KzSSoWx5V0Ja0jrewURehptIGhKqK85SyHX77r6-C5pihzoFiqsxkrHLhxBvoYyUG4t8bzdLwjELqfus_utmtoxULeGHzsE6o404bAZ9Iyd9xbfh7HxEiV-TCg296l61oWungsuvSLnPTDMJHiJOScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S75RB4BsGda6OTYIkRVor--gDB5shfUHfErLINQXVqW8KgcMMHMLiOnog_jcb0DuymuzkDHPj9_M6FOzftr80nG3YlZ8i_tyilP4qXoI_iwEzVxFhXRE1C29jrbq7qRDCXvn5KTsFU2Q1EML8G8RlsRXECyUQUvKhLfdZ5MiwQ199ITePqK1pk5mC5K9G5f7TLn2zedTfwMHuaiM4CAgY6xNRCY7TfwxK9og2AZPRd0fKHxXURTONYQdR0oS2gIv4gS6yz0pFTiqsoZ2a75Xx-cByZU4ZXbIdOcPeZBHSEy79K3UG7lgXZOYkxj16VT2q8NvONW6izQ8VTNId35SRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۶ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/444998" target="_blank">📅 01:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444988">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UK4ufrHK3X277s5MLe9eepqrp7Smg70nAN0ZvHXq7e327-bCDAkCJV1YPnR8UxT_YmtuBSxpKoscUTDpLw3q2uFUc7NoViEnG38rnyRBO2TzPOC098NPCzZu1h5oRetpazINb1NHVGLWCDxJW2ENPf-v5nWU_K-Gx4nxGpgq27kOAy0hkzSuXT0E3Rm766EU7E_QFWTrqWT7m2nwRPRcmSMr0x6FS8PZHIsKnFEVQerY4veIJ1a-Ndc26yDDxatUSKUla8DwKkyYlQy7KtYoIHnUaNucjVEY2ZUOGQWFu-AOVdtcDfcHd5vkztHZgnLPG_W0cPBFil6x7efTIdbm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZ2M6N4DwP66i322XNJWhDwTQNSrJqDck9JQKThKc1ex7FDuqhaKGoNc4abM64jnQDKuQvSLOkzfyukrK5WuVJV-p8C7MmXxkrq-GX3mHjWwYDm8lw8trBen5fScbaoZ6uVIKhvmdC1aAg71jlG_p3Xte00Rzk4Sv1-bmJXBlOuMhXX1XjmsWjRB3cY4Qn4WhD6-GAJxpcR6mFtzbJxfUh2oDmiAOLxLURyUzGP6dvLp1HTFxskCC26vU4ZJHQsU96pQd2gTAmMo0dcsQOIYlCbL4kvRNBaidLZgizE1eOVnXruGhvIsq0WtK_9PqLLiIvfJmVBXJ5cxbjQ8IFQLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyV38jyW0jEAdplkciGnMIM4PF0JSCoYCrtKlpXWzQ9vPctMk20GxXzCx2BNdL8yf8XOWQeMf5HhX5Q7zQbTtRiWCJ8fFEJ_TSyM6rx40_VejGJo6BC9tFe8exWhBazM2HITtLrtVb_UOQnBJbLy4SPVTntog4ted6AsS0HH0hE9rzPwZYTa0w-OKfRYIcRhKGQd0jzwQhY_ClMc_505WZdYCdO3oInOdeNIkTju-RpaR1Q-LCOfN6rtekCRmN5DmxV-mpME3EBfIQ2GhlqZZDJ6AkndLvYXe8HBY2G20pxME_XKDjwo8MQgcEq-B1a6pcNYbvN9OU8iUYepymTjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWUBWcoh-tBd53EDhQbgQu5ElJlzyVadlp39wmWh_UXQi2vRhtv7vwl35qfLdDwFiVO5Aso7rKa8dTld4-8JHm2T7G_Qq3D5eL5coSOAkNmRHHZ1OUAWbOjdVC1vANYZ18W6mOk_eprZT3Bot2RDjvTRRmCA2mna--TfyQwkllpPCcgB1oM9Em9PCyxzdRLZMCedvNdK7U-nAv3td_kaHkqtDDrP_5NiK_7eqquvGm7URQyf2foAL0lngsF_f4PiM3clsO-yY3aWvu8r8EZ7FdtIuljHLNJ6loybKaTFuThCjX9joye1UcRB67e80UFy-lK68f-ZECAmMrsnvcCW3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGl-qo_ymj38pnLO9pORrNsR6zsghZQq8ZtJE6bpJFNNJkFUudJBVrGG_5tPXZSMo4xqJLnB8WAr4EZDzvUOSsFD4r-0a9bZtG56adxrljLy8VII4e7ewqi7j23rW6cfuAFp2apOLWGUJgkGXcE2RvY7tTvE_lNA514zJaOiVgklTFzOQBME5xVWz0r8PxNC6VW22B-Acygs6dxL8HijZ0HbQvvIWbC16wLScfGW3FkoQUH8HfuVPzkXqOdwKOlv5tz8noIEf7SuganOG8DYjkpAK9uO_rTsl2-TWmHkqT3j3YDVBqFsJyLpsuFWnzXiU4kV6Y71bKb3QOQLeq9xUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzTPC7i8GIEBgk6wwc-hxufRinISjILsh6isckDwgueCIWd_-KrdpQN67Zi_7U4dRPYyxKfe4fg2rgqYgvE5FFV5Ow6AP69ttxgfFx2uV2lI3avvwhRaxh6Ar3lkKbfoXhwYdTEauil_QAI01xIMyp3fPSQ8G8LMPRn1I6zhJekmnLbgF6By0pG5Gk5h1M8t8btLgNlutXWiKUQ1_zX6cLFQEqp8eJUnKqTNah0IlRL5_JXjNGyi-wVgT9I5U4UJFIrS1XuGwIBmUgWqFEYDB1rMIlBvbEaB1NfiweTKhFkPvmQiJxOdwmW91uT_OMKHwVS_5z7jedDRl_hVGBXn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPDURMQ7gOmLr_hjuGnWXYYAJI5r7VxO0vTsUAeF6ZaPrMlVX0ZMJwIldsUZ80KEVwtqf6Bl6kP4RyOus4D2a-FAgbZKV1_UP3q2uprgmpB7uJNqWW9c_JQZYynJc4H1DcAKSwmuUPaK9w7y9L-4Bl-spu3kKzP-55AUIhDQjI6hoesqztfXead4e93jIMRZp3tbAhu03C5mbnzpAm7QgVVW-GIpywRnDGZ4TwZJ7MlQ5YEraiO7_mIRWwkKseMFHY0XL2UoTEa2bUEdfGrK17gKdsuuQRHvLw0QZgzAAlgQDl9ok12hC6-OMlJwUthRnFX-fQhaG66wlbvL2fC4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiK9GPbmLwLPpEE2s8X_DUyRlSy5NpTTAJ6csb-yqHKvk75MXqTjZ6mBPiU05lBPpBc2mWJshtIKH6FIRZb7Fg2NdGgnwc46R8JKephgekk8ONe7UNDBs1HRHY-Sy9_ufcnHRSyw5HNOBxDXnirOjZXLJxPRFyKKN5JhVzZliFvPGAsmPNAq0crMBD-9INiGE_VKsUY9xS8MF89fs9lGtB1SG6coPH64BWW4z8EfcwcUNlNRou13cXBsDOy3wSAZCtOcP7AQP6n2W3QlX_zFaCBVppBCdG4dvVqwgQtZ6v6eJcnQQdZZzxCZN-45QCZn24y_jZMSORMsZtvNBZNQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9MmlV2w9wBIyb-xkcy_z16SqCDAQJGEmqibOnmR7CYybI4NUHEL3PbnWZZ-XMV5EW0cYHBqwpcJSmnyqTNiwUe7_LFUXMDBMMcrUtz4zSDOkQoyZkfu2mhSk35JRY7bmiR8-jTPRZrDsODCs5KmF1O_h48avYB6dyeBEz63i5uaMxzUoeYNI1ads0aHwFaQ62PufnQ6SdgVpHO-zDBu-ewqgHlx8-DyH20udmEQXbWsTGY50CgLAmPnNVgTmF6KBlcY4122a4hjbbLGr1uswe-wkA3TxQQph-gqQtrjXZfbJZd_tP4oU7YiwUScYX_z8N3pIAFOvcpwoJKp8uHvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIBoD0KNtDZl9UfKkd3u7JrW5ekO5nAdNk6zsCvNE-WvUbkLyVARpdXS-FUQDSSUYAfqaHS_LrYzoZeSA2VodAnV6UNT3vjj9HC_BmXWDEIo6n-KDZGLwZCeHanIyQj8OFlREBumsGDZ2oBc84i57i0bocwe5NZm_XKnqz3UpSnhQVOnrSqeOArFMFxVvs70Rhs24LD8gJjJnwaxgvKh22ORZSc6V0dI_dQTSgrM_Bqxb87qV9Qink1fGqZ9jFJxqsg3WN34LnYotZUPYWYQ2A3UGVec8L2vpCjA4ETAy-bA3DT4EWp3ymiaXQemX2auOvVk9480pJ5ysYPOILUbdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/444988" target="_blank">📅 01:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444987">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🎥
مدیرعامل پرسپولیس: برخی بازیکنان پرسپولیس باید فردا خودشان قرارداد را فسخ کنند
🔹
کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی‌ها مشکل داشتند؟ نیمی از این تیم مدعی است باید در تیم ملی باشد ولی مدل بازی آن‌ها چه بود؟
🔹
بازیکنی که دنبال کسب‌وکار است معلوم است که تمرکز ندارد.
🔹
کادر فنی تغییر می‌کند؟
اصلا چنین چیزی نیست. مگر نیم‌فصل بحث تغییر کادر فنی بود که بازیکنان این مدلی بازی کردند؟
🔹
اوسمار قراردادش با پرسپولیس تمام شده و هیئت‌مدیره باید در مورد او تصمیم بگیرد. اسکوچیچ یکی از گزینه‌های ما است و باید در مورد او صحبت کنیم
🔹
فشار بانک شهر برای حضور عزیزی؟
اصلا فشاری وجود ندارد.
🔹
عالیشاه و پورعلی گنجی؟
من اسم نمی‌آورم ولی خودشان باید بررسی کنند که آیا در پرسپولیس بمانند یا نه.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/444987" target="_blank">📅 01:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444986">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
بیانیه‌های منتسب به سپاه در ساعات اخیر جعلی است
🔹
پیگیری خبرنگار فارس از مسئولین روابط عمومی سپاه پاسداران حاکی از آن است که بیانیه‌های منتسب به سپاه دربارۀ درگیری با آمریکا در ساعات اخیر جعلی است.
🔹
از ساعاتی پیش چند متن و بیانیه منتسب به سپاه پاسداران انقلاب اسلامی در شبکه‌های اجتماعی در حال انتشار است که مسئولان روابط عمومی سپاه پاسداران می‌گویند هیچ‌یک از آن‌ها از سوی سپاه صادر نشده است.
🔹
مسئولان روابط عمومی سپاه پاسداران تأکید کردند که اخبار، اطلاعیه‌ها و بیانیه‌های سپاه پاسداران انقلاب اسلامی صرفاً از طریق سپاه نیوز و رسانه‌های رسمی منتشر می‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/444986" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444985">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
سی‌ان‌ان به نقل از یک مقام آمریکایی: حملات روز جمعه نشان‌دهندۀ بازگشت به عملیات‌های رزمی بزرگ نیست
🔹
هم‌زمان، منابع عربی از آماده‌باش در پایگاه‌های آمریکا در بحرین، کویت، قطر و عربستان خبر داده‌اند.
🔹
فاکس نیوز نیز به نقل از یک مقام نظامی آمریکا اعلام کرد که حملات نظامی آمریکا به ایران پایان یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/444985" target="_blank">📅 01:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444983">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b34d1dcc.mp4?token=eaKDylVuj1MypT3XZ8dPQJGlTGY_mECtDUmtB79UKf8GsErcla2cg9ZCohb6AQhLH-3hfRRY2PAzPJVEbFqDtNJNMmGNcIqAKj_qOgo-d2BY8D6xGn9LtOGU_jhZEt_-tRIKNww2Iq6SsSmeOz_JDAJmOGpixv_V0WLczHlSq__xhbwp2rRqj-MHqx_y4BMOBH32WhG0pCu7cn1cUg9uwDXX0kPcoVXQzdq5who1F9866WtwGrm5QQXri6Pqq67DxdJ8CyVtS5pQ_QGslVNXl5Q244X2lhswqPA54mG7WTdnTR_tDgdQ2OnLeibVNnOYY4DJXeWK_lMaLEP7F2gBPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b34d1dcc.mp4?token=eaKDylVuj1MypT3XZ8dPQJGlTGY_mECtDUmtB79UKf8GsErcla2cg9ZCohb6AQhLH-3hfRRY2PAzPJVEbFqDtNJNMmGNcIqAKj_qOgo-d2BY8D6xGn9LtOGU_jhZEt_-tRIKNww2Iq6SsSmeOz_JDAJmOGpixv_V0WLczHlSq__xhbwp2rRqj-MHqx_y4BMOBH32WhG0pCu7cn1cUg9uwDXX0kPcoVXQzdq5who1F9866WtwGrm5QQXri6Pqq67DxdJ8CyVtS5pQ_QGslVNXl5Q244X2lhswqPA54mG7WTdnTR_tDgdQ2OnLeibVNnOYY4DJXeWK_lMaLEP7F2gBPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراضات خیابانی در بیروت، درپی امضای توافق اولیه میان دولت لبنان و اسرائیل  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/444983" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444982">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
شهادت دو مأمور پلیس در حملۀ مسلحانه به ایست‌وبازرسی بانه
🔹
ساعتی پیش افرادی مسلح طی اقدامی تروریستی به ایست‌وبازرسی ورودی شهر بانه حملۀ مسلحانه کردند که منجر به درگیری با نیروهای امنیتی شد.
🔹
طبق گفتۀ منابع، در جریان این درگیری دو نفر از نیروهای پلیس به شهادت رسیدند و یک نفر از پرسنل پلیس به همراه دو غیرنظامی مجروح شدند.
🔹
در حال حاضر، شرایط در شهر بانه عادی بوده و اوضاع تحت کنترل کامل نیروهای امنیتی و انتظامی قرار دارد.
📝
اخبار تکمیلی متعاقباً اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/444982" target="_blank">📅 01:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444981">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d52f5d052.mp4?token=IoVMehtySZMbnfVvv9o-5jGa2gXbII9wLKAMZ1mKXycw_pUeaOrJk3tVOHQMet1Xau6qoEHKyLGvl62XZxDbP4A9FKWOhvwKVasuQM46HrR5SksiZNMGKThWaAnCOGSbfBfidrUAky0A1krxlbXd9oMnAQ_Vf86tckyKWX-PgQY87nJ67iVlzRD1yEbTYIjdpwe_FmoX9gxmZD0Jqf60j7z0WJ4iMizw6viyBXGF56kSwBm1UkiLgI6BP0SLFtD9-yi1i3P6aknjfwj0gESr_4uFwbdHRAlQjqvIqfs9MPrxKdaeLdCoPU0rseYmK4pE63oluhti7AGPhvidZMtmrUt_irUtknrvLfi46EJ75_ng1-jdS5DHniRSRt5E6zYGExKaSEBTDo6T4VdwYK8DJH0e_cO12LA6SBplDtdWl9zHBjVLK7rjFtetvc0s7y29Av5iKGmGFO3oFR7K8jQaBDwy3rObF2wfNnSaiL951pSWgj2o1AYT_LzRDTC8xlFPAA0fEUVnoL_lm6GNtTstzj8hCYttIH5RPCkmv72-XRGaND9VmVP3dnjzttQ23kpCe588cHPL3z0X84vSE73_oUSKhr-qAQMtFMLqevYM0t-PB0DDo_7H2BUKxoqHGnguuIF1USaktcOzLjm2-H7XWy99sY1XgbbVxoxdYhV6_2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d52f5d052.mp4?token=IoVMehtySZMbnfVvv9o-5jGa2gXbII9wLKAMZ1mKXycw_pUeaOrJk3tVOHQMet1Xau6qoEHKyLGvl62XZxDbP4A9FKWOhvwKVasuQM46HrR5SksiZNMGKThWaAnCOGSbfBfidrUAky0A1krxlbXd9oMnAQ_Vf86tckyKWX-PgQY87nJ67iVlzRD1yEbTYIjdpwe_FmoX9gxmZD0Jqf60j7z0WJ4iMizw6viyBXGF56kSwBm1UkiLgI6BP0SLFtD9-yi1i3P6aknjfwj0gESr_4uFwbdHRAlQjqvIqfs9MPrxKdaeLdCoPU0rseYmK4pE63oluhti7AGPhvidZMtmrUt_irUtknrvLfi46EJ75_ng1-jdS5DHniRSRt5E6zYGExKaSEBTDo6T4VdwYK8DJH0e_cO12LA6SBplDtdWl9zHBjVLK7rjFtetvc0s7y29Av5iKGmGFO3oFR7K8jQaBDwy3rObF2wfNnSaiL951pSWgj2o1AYT_LzRDTC8xlFPAA0fEUVnoL_lm6GNtTstzj8hCYttIH5RPCkmv72-XRGaND9VmVP3dnjzttQ23kpCe588cHPL3z0X84vSE73_oUSKhr-qAQMtFMLqevYM0t-PB0DDo_7H2BUKxoqHGnguuIF1USaktcOzLjm2-H7XWy99sY1XgbbVxoxdYhV6_2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریم باقری خطاب به بازیکنان پرسپولیس: هر بازیکنی که بازی نمی‌کند قیافه می‌گیرد. فقط زبان شما خوب کار می‌کند.
🔹
خاک بر سر باشگاه ما که زور می‌زند به آسیا برویم. مگر ما لیاقت این را داریم؟
@Sportfars</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/444981" target="_blank">📅 00:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444980">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6032822f84.mp4?token=K4Vm1gHvVWshHOVhxGBLmaey8_URtk94ZcI0bRxvaLavgj7M5XYRHgJbDLllLWySO7udIK4PQvfOsBO7QX9EMUPBgXEiqYGQmw88cZ90WVYHGIjoI7LJBfgQjo1eaJohL1tXqgaxAtVetp069AMEpL0oehyxJkcMlzkQgne2bbo9-ehrimYwt5Bm8X1XEaq7KmY3qCxwpH9m8713Rl1lNhTX-PGORmnlN5uQfihm6pKMclPJizoGBgYIZUN7RJ6VpcddYlrb3ZruavKHbPzeuWDuTnRTBLJy_6cjHolroxQOslo88jaP_prCd9tO8sKeqzNJXPwGZSfPFL7NjFToEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6032822f84.mp4?token=K4Vm1gHvVWshHOVhxGBLmaey8_URtk94ZcI0bRxvaLavgj7M5XYRHgJbDLllLWySO7udIK4PQvfOsBO7QX9EMUPBgXEiqYGQmw88cZ90WVYHGIjoI7LJBfgQjo1eaJohL1tXqgaxAtVetp069AMEpL0oehyxJkcMlzkQgne2bbo9-ehrimYwt5Bm8X1XEaq7KmY3qCxwpH9m8713Rl1lNhTX-PGORmnlN5uQfihm6pKMclPJizoGBgYIZUN7RJ6VpcddYlrb3ZruavKHbPzeuWDuTnRTBLJy_6cjHolroxQOslo88jaP_prCd9tO8sKeqzNJXPwGZSfPFL7NjFToEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنت‌کام به صورت رسمی حمله به اهدافی در ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که امروز مواضع ذخیره‌سازی موشک و پهپاد و همچنین تاسیسات راداری ساحلی ایران را هدف حملات خود قرار داده است.
🔹
طبق ادعای این سازمان، این اقدام در تلافی حمله پهپادی…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/444980" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444979">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۲</div>
</div>
<a href="https://t.me/farsna/444979" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۱ – کتاب آه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/444979" target="_blank">📅 00:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444978">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSQayJsEosJ7q_sNGpwvaDnJrGj0v4l3SMNjueKCSg7LHtE9V4Az2WCeV04TcMjMybt8G3098baXtNefnFkBeKgY6ZJh-hNTA15L6C9nOwz-TVvmB4mlB-7txeY-QJlsx2ndJpvMQF_v80RDKO7NMVgvU2wd9Y_ZQQRedYfSH-QJIv6p4R8oIR6FCTE9I_GtYpuP8pplH9rWMXs1DoPMjZGhiA3vh-abOAoUs-ftGqzv75uObLTbbwKx9SzEPVO60N5o1mtmUgX9qyYLezWJDCPT3lgKNuXhpdxcfJ3zyu1AZZLa2KzOHN_LstmLQ4YFAvYyaRv40yH1l01EoNGg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود فرانسه، نروژ و شانس بالای صعود سنگال
⚽️
جدول گروه I جام‌جهانی ۲۰۲۶ پس از پایان بازی‌های دور سوم
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/444978" target="_blank">📅 00:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444977">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApCsVvyZKF4KEhpr_z8HPpHRgu9GDMsGga_an3ccoJxrw7JSr-W6asFcdVHLPWOv9Eh2rCN8AlM0GtusnFwdr-m3nvzNObFYhI_zTbVoch9lSMNtncb10410gvtlLygx52vx720I72oLSQgrGgi0KsKPc8eEIfiPsH7S8Y3mT6YxfXhfP3Gg39X0ISEz5_KPqcal9yg0lgTkiMIr2OIp7bZth-GmU5N65NSE4k3Qi9APQRYWEtxgi6qSU1HotmMYR_V5dxSdrFwEiDPcDtrCXcVlUAgUmaIFgHcxEbVo2_RX8eIg3Z6xu5UbiRaELqa4gdzY7rFQ6XPX_KN8fUfnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگال با گل‌باران، عراق را به خانه فرستاد
⚽️
سنگال ۵ - ۰ عراق
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/444977" target="_blank">📅 00:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444976">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj9PzB9bRW-pg6kmdQWaY4_vRvGkcRDwQPo6SmpfZM8g2U8eX0gnXavNCy_ymj0mzVRj7QwOlKsxChcRTqxwTPmgwWRXkdCaqq8kjKZvjRBNQdB0y5L9qRqwj5n7SnixX4r9IF8cNGcXk-ikdFfIEON6AlRG6dDSr5mrfgx_ysURyRoPZSJ0UapEWs2FbR637MixS9NZ6vKwmsLtm6gBpUSfCguj95KBUxVu8kdwG89f5XRLrPJko7pKhGU22jM3yB_keh5OoJf9L3KPfwdAdsxchhelQwrbfaDdm2eGVi_esJWrREMd7MPzWEK0V0jDfhkb1Mq_IiOmgV-khifHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ گل‌باران شد
⚽️
فرانسه ۴ - ۱ نروژ
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/444976" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444975">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تمجید رئیس‌جمهور لبنان از توافق با اسرائیل
🔹
جوزف عون ریاست‌جمهوری لبنان: توافق اولیه نخستین گام در مسیر بازگشت کامل شهروندان لبنانی به سرزمین‌های آزادشده و خانه‌های بازسازی‌شده آنان است.
🔸
این ادعا در حالی است که مقامات اسرائیلی از جمله نتانیاهو اعلام کرده‌اند…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/444975" target="_blank">📅 00:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سنت‌کام به صورت رسمی حمله به اهدافی در ایران را تایید کرد
🔹
سازمان تروریستی سنتکام اعلام کرد که امروز مواضع ذخیره‌سازی موشک و پهپاد و همچنین تاسیسات راداری ساحلی ایران را هدف حملات خود قرار داده است.
🔹
طبق ادعای این سازمان، این اقدام در تلافی حمله پهپادی روز ۲۵ ژوئن ایران به کشتی باری «اور لاولی» (M/V Ever Lovely) با پرچم سنگاپور انجام شد؛ کشتی‌ای که در حال خروج از تنگه هرمز در امتداد سواحل عمان بود.
🔹
سنتکام مدعی شده این حمله نقض آشکار توافق آتش‌بس و تهدیدی علیه آزادی کشتیرانی بین‌المللی بوده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/444973" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444972">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎥
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
🔸
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
🔹
ترامپ: خب، به‌زودی متوجه خواهید شد.
🔸
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
🔹
ترامپ: از اینکه دیروز…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/444972" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444971">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBEMPi-Wn-kq3IwwlA2LAffFjjPGqJQdERuUsBAJbkHjwkyvdHutLLJWHm9J7ldrrg3VcRm5-zo3OHkB3KNSMcM0BnyIzPNrvRMzXVA-4zwA91pT9K7J-UJivN8OS7xzAucQZWi_QTK-2LeigZu5gML7iz7y41lOy-WCq9x-WsGJ1Q3e1MVP4HSopPNysNLUWxskwtg7Tgv9DwLzKTDPntNQlwLp1ilYBrhjISI6wD5dg3kUh9pc8uuwPmVeAkyNQIY2RIkLeVz6NxiIRYJx1IHVjjkWN0fzX8w_Mj2jyfPXkKoiidTyvRgTM2kx24MDwOz-xBuxYJOwd3YgJLvTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی کوچک‌ها بزرگ می‌شوند
🔹
کاروان خسته از راه، در پهنه فرشی از خاک و شن توقف کرد. بیابانی برهوت و تا چشم کار می‌کرد، خشکی بود و آفتاب. پیامبر(ص) رو به یارانش کرد و گفت: «برای برافروختن آتش و پختن غذا، هیزم جمع کنید.»
🔹
اصحاب گفتند: «ای رسول خدا! خودت می‌بینی که اینجا چه صحرای خشکی است؛ در این برهوت حتی یک تکه چوب هم پیدا نمی‌شود!»
🔹
پیامبر گفتند: «هرکس به هر اندازه که توانایی دارد، بگردد و بیاورد؛ حتی اگر بسیار اندک باشد.»
🔹
یاران میان ماسه‌ها، زیر بوته‌های خشکیده و لابلای سنگ‌ها شروع به جست‌وجو کردند. هرکدام تکه چوب کوچکی، خار خشکی یا ریشه رهاشده‌ای پیدا می‌کردند و با خود می‌آوردند.
🔹
وقتی همه جمع شدند، در کمال شگفتی همگان، تپه‌ای بزرگ و قابل توجه از هیزم در برابرشان ظاهر شد.
🔹
در این هنگام پیامبر (ص) فرمودند: «گناهان کوچک نیز این‌گونه جمع می‌شوند. ابتدا به چشم نمی‌آیند و هر کدام را ناچیز می‌شمارید، اما وقتی روی هم انباشته شوند، تپه‌ای بزرگ از تاریکی می‌سازند.»
@Farsna
-
#حکایت</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/444971" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
بروجردی‌ها: ما و حزب‌الله تا ابد هم سنگریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/444970" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpx6vlgv5Ko1miRdM4Wv38fSrJJLFjmA9db07umUMAFFf0PyuaOyW4C6kNRKUdfMadOndjRLFAO-Bn2b4kb1nVoCt-pDWUkeGKx2y9vg47soFJS4NfckO72bOYEZJYwMxBuWF8YsnbSe1Q-PhpOrMP7dAFn2cFUcZDa4vo1b1Qke8V6vqjnzj6vyyKufqkSDBZfYT76dq5KijVdoaBzXzmQUeyGCOpaLk7t_axnhQjG0exS9Dm56d1R61qDFUOS4um_q6i-QxE9vjVJfpJUrpDnHNxQuoN6v9LwT9J7JP-ZF_hbwqUfdE23PFCJy9zHjEo0gUV_FjkxuZf-kQQ7e9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها قدم نخواهیم زد، میلیون‌ها ایرانی کنار ما هستند
🖼
تخته آخرین جلسه فنی تیم ملی فوتبال ایران پیش از دیدار برابر مصر
@Sportfars</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/444969" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
