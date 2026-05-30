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
<img src="https://cdn4.telesco.pe/file/AXI3kVeVnvMhtoMqjE7KhrY1VfRvc_B-jncJDO3BhaymhX0Z1iF39Fdvs9Wg6-o2Qbmv16JDdxN-rRTlJ1nv_ZKxqjobYXkE0kpRctwnP-Boo4DqAxKkmXYjVyZsvd8tMwZKrN8rog1KmaKAw9QROFEvJ7fEiELL2xFfJttfHs6mix7rI5NkpB10aEv86ERY409KVTOBE3IWRJOSVRClThbsGFaSkxUawmtPvQBc06ZH44U7libCZWmCK8ri-STBG6bJQgwiwbG7ZgNpyB0s6fY_A45qPDqXyTQ1d62QgOPkCIX15XQotBmH5_hRsKtKgZ0AoqMxzh8Cq8FivZN50Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 281K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 13:51:29</div>
<hr>

<div class="tg-post" id="msg-12934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/withyashar/12934" target="_blank">📅 13:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#shahzade من تا آخرین نفس و قطره خونم از شما پسر شاه فقیدم حمایت میکنم تا رسیدن به آزادی</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/12933" target="_blank">📅 13:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓡𝓪𝓼𝓪</strong></div>
<div class="tg-text">#shahzade
من تا آخرین نفس و قطره خونم از شما پسر شاه فقیدم حمایت میکنم تا رسیدن به آزادی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/withyashar/12932" target="_blank">📅 13:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">#shahzade</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/withyashar/12931" target="_blank">📅 13:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سفر قاهره با یاشار غمی ندارد فقط لذت ببریم از وقایع
👑</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/12930" target="_blank">📅 13:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صداوسیما : طبق نظرسنجی که از مردم انجام دادیم، اکثریت مردم از وصل شدن اینترنت ناراضی و ناراحتن. باید فورا مجددا قطع بشه
@withyashar</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/12929" target="_blank">📅 12:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تسنیم : با وجود اینکه ترامپ در شبکه Truth Social اعلام کرد که محاصره دریایی ایران «اکنون برداشته خواهد شد»، ملوانان ایرانی گزارش می‌دهند که این محاصره همچنان به طور کامل برقرار است.
کشتی‌هایی که پس از اعلام ترامپ تلاش کردند از خط محاصره عبور کنند، توسط ناوهای نیروی دریایی آمریکا هشدار داده شدند که فوراً بازگردند وگرنه با آتش مواجه خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/12928" target="_blank">📅 12:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا،ماه گذشته احتمالا با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!  @withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/12927" target="_blank">📅 11:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا،ماه گذشته احتمالا با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!
@withyashar</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/12926" target="_blank">📅 11:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو خطاب به لبنان : درخواست اتش بس دولت شمارو رد میکنیم
باید بگم که اسرائیل تا نابودی کامل حزب الله ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/12925" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کاخ سفید به الجزیره گفت:
ترامپ تا زمانی که خواسته‌های آمریکا برآورده نشود، توافقی نخواهد کرد و ایران هرگز به سلاح هسته‌ای دست نخواهد یافت
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/12924" target="_blank">📅 10:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12923">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNxlVL8dD6QbN7Dwssek1cnOBrUQUTCRvhwaA87xblT3IobCuOy7edLQKf5ds1FlAq5u-DfiQbV1Iz4HRjcQQ04LMM2Lx32JS7R1DjXpKbNBI0-Q3F9YDcmf6JyosZrSLqU--PbVKOYG3pycMCUzZUknM8I2yZ1IK4-C_j9-THfWx6z_uwZbaiIim7Kji812TGSbNbj4Ct37rcCh2CgroVHQq__IHpKEhWOPVV8MtotztaBKeQSbQXu7YHJcM3L24tC_KolbnOYegz8VEx436Uj5BkgI1AW2ItyPBtw1Xl8FugtijPUCWPHO0zM6HE56oTbWO3wJO0bqJpukvRABPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشک ترامپ: «دست دادن مکرر»، علت کبودی دست‌های رئیس‌جمهور آمریکا است
این یک اثر شایع و خوش‌خیم است
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/12923" target="_blank">📅 10:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سنتکام:  هر شناوری که در حال انجام یا حمایت از فعالیت‌ های مین‌گذاری در تنگهٔ هرمز دیده بشه، توسط ما هدف قرار خواهد گرفت!
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/12922" target="_blank">📅 03:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12921">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80123d2be0.mp4?token=B12E47vmYka50uXW17DSM5H0jqKG6ZnMJ_lPDqXSimw7drRHXvKVeH980Yf-s_vK2w97PxUSwMvz2_5wTJodDxZ9kfnsqDtbjUQprBZC4Kk8o_7RAPzhYaGOSU9sNQU-hy0GR0Z2lpcx6BSd8NuHcCBNkwTg3dYGmg37iCclBOtlI2FunprSRoyCbuifkF13vCRPKuWVFo7evpOJGk2-rbbJbS2QAaKGxohe6rptfNVKNhDKWp8E3Pa9xv6YnCHRnaEtOIF43nh4vsuiJFjvlV5oG1IX3jEc_hTkozRWPW09nWh022XNCMvD2MAb5Fp1coNxECpWZ-O3ecg4v8EQyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80123d2be0.mp4?token=B12E47vmYka50uXW17DSM5H0jqKG6ZnMJ_lPDqXSimw7drRHXvKVeH980Yf-s_vK2w97PxUSwMvz2_5wTJodDxZ9kfnsqDtbjUQprBZC4Kk8o_7RAPzhYaGOSU9sNQU-hy0GR0Z2lpcx6BSd8NuHcCBNkwTg3dYGmg37iCclBOtlI2FunprSRoyCbuifkF13vCRPKuWVFo7evpOJGk2-rbbJbS2QAaKGxohe6rptfNVKNhDKWp8E3Pa9xv6YnCHRnaEtOIF43nh4vsuiJFjvlV5oG1IX3jEc_hTkozRWPW09nWh022XNCMvD2MAb5Fp1coNxECpWZ-O3ecg4v8EQyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلزار: نماز میخونم و شبا هم هر موقع بیدار شم شروع میکنم به دعا کردن
@withyashar
❄️
👃</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/12921" target="_blank">📅 02:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یک مقام کاخ سفید در گفت‌و‌گو با خبرنگار شبکۀ الجزیره مدعی شد: دونالد ترامپ هیچ توافقی را امضا نخواهد کرد مگر آنکه این توافق مطالبات آمریکا را تأمین کرده و با خطوط قرمز تعیین‌شده از سوی او همخوانی داشته باشد.
«واشنگتن هرگز اجازه نخواهد داد ایران به سلاح هسته‌ای دست پیدا کند».
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/12920" target="_blank">📅 02:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12918">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">@withyashar
وضعیت</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/12918" target="_blank">📅 01:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12916">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسرائیل هیوم: مقام‌های موساد معتقدند عملیات‌های اخیر علیه ایران فقط یک مرحله در مسیر سقوط جمهوری اسلامی بوده است. رئیس پیشین شاخه نفوذ گفت این واحد اکنون با شدت بیشتری فعالیت می‌کند و هدف آن «سریع‌تر کردن ساعت شنی پایان حکومت است».
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/12916" target="_blank">📅 01:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12915">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">https://t.me/boost/withyashar
بچه‌ها عالی بود
👏
👏
، بوست ۳۴۸ تا دیگه لازم داره. لطفاً این پیام رو برای تمام دوستانتون که تلگرام پرمیوم(تیک) دارن بفرستین و ازشون خواهش کنین که چنل رو بوست کنن
❤️‍🩹
چیزی‌ تا ایموجی نمونده
🤰
🫃🏻</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/12915" target="_blank">📅 01:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12914">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شکست مذاکرات پنتاگون
؛
اصرار تل‌آویو بر تداوم جنگ در لبنان
منبع رسمی لبنانی: طرف اسرائیلی با درخواست هیئت لبنانی برای آتش بس مخالفت کرد
یک منبع رسمی لبنانی در گفت‌وگو با المیادین اعلام کرد:  هیئت نظامی مذاکره‌کننده در پنتاگون، به درخواست خود برای برقراری آتش‌بس واقعی دست نیافت. این هیئت بر مطالبه آتش‌بس پافشاری کرد، اما با مخالفت مکرر اسرائیل مواجه شد.
به گفته این منبع، هیئت اسرائیلی از عقب‌نشینی از اراضی اشغالی لبنان خودداری کرده و بر «نابودی (توانمندی‌های نظامی) حزب الله» اصرار کرد.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/12914" target="_blank">📅 01:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12913">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgR4KqqdzcSXcdPa6nCq_L2N4OhopP4IxIEk763RbnOCaNGtt1PAEkCaJZ7WBdYYltXNIPrlOp9I0LXP4pVaoMGfn-KIkHcIzeQhK0CvK-pha5B0yZIWpuwWjPpzlBVEFtcm0p-jhpgemJyJ_lEY1T0Js81v6a6nPT9-f2ubo2fnGX7NVWv4KlOo5gIh78Xdh-gNE-kvDvyX9WLCqC21QeD48A2tFvsvOzzyVbk1VNxSy-5ulXSZTcBq_q7vVKp90qXXyXxNN-dFMVRgNbwkrtTMkzPoZ6e7z_nxdhxpDuAHYODbEVm7nn2MNKDVofG4AkekjVPGahVd7JctdoOwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از داماد ۱۷ ساله و عروس ۱۶ ساله در تجمعات شبانه
@withyashar
زبانم قاسمه کتلته…
🥴</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/12913" target="_blank">📅 00:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12912">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">صداوسیما: منابع محلی از فعال شدن سامانه پدافندی در جزیره قشم حوالی ساعت ۲۱:۲۵ خبر دادند.
بررسی‌های اولیه حاکی است این اقدام به احتمال زیاد در مقابله با ریزپرنده‌ها انجام شده و با موفقیت همراه بوده است.
سامانه‌های پدافندی آرش‌ کمان‌گیر در روزهای اخیر عملکرد موفقی در مقابله با پهپادهای دشمن داشته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/12912" target="_blank">📅 00:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12911">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حسین علایی:
سه روز قبل از ۹ اسفند به شمخانی گفتم امریکا جنگ رو با تـرور رهبر شروع میکنه؛ گفت نمیتونن اینکارو کنن. چون نمیتونن پیداش کنن.
سه روز بعد هم خودشو زدن هم رهبر رو. اونا اطلاعاتشون خیلی قویه.
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/12911" target="_blank">📅 00:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWB40nCXEeA_6NmO8CJD9LDZ60qRQNtX_LNr-thmQyyx9RbRyRa5WIfGCl4qE-Lxw8IzgExCBR53azkQq-F8-93oxTdRKzqSfKxN8AfkeoqoUV15dIaqmvsafny1m-kpy4UCMI_Qw1Je-Xz25hSkhsEcNIVZ4lnkTX0vRdBywq0rWdSNIJA7vmed96NStsdb5_IQDRPWTA66AV8oPYG2cPR0B4Bu_HzLF3heQ7vt6rj5-LgM37W7E5XozAtiNazkJ6LTRyfcUR3rqsSuDlR5W1jOMLbZNDcnXOvotTfNQ3xk5xEKkQacLr_Yro_l6upfWON5gd0tSj3BsV2nwpGEgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالک شبکه ایران اینترنشنال به ادعای فاینانشال تایمز
گزارش Financial Times درباره ایران اینترنشنال می‌گوید این شبکه به‌صورت رسمی توسط شرکت بریتانیایی
Volant Media UK
اداره می‌شود، اما ساختار مالکیت آن پیچیده و چندلایه است و از طریق شرکت‌هایی در بریتانیا و جزایر کیمن انجام می‌شود. طبق این گزارش، این شرکت در سال‌های اخیر با زیان‌های سنگین و بدهی‌های بزرگ (بیش از ۴۰۰ میلیون پوند) روبه‌رو بوده و اخیراً بخشی از بدهی‌ها از طریق تبدیل بدهی به سهام بازسازی شده است. در جریان این تغییرات، سهام قابل توجهی به یک شرکت ثبت‌شده در جزایر کیمن به نام
Info-Cast Cayman Limited
منتقل شده که مدیر آن فردی به نام
صالح حسین الدویس
معرفی شده است؛ او در گزارش FT به‌عنوان مدیری مرتبط با گروه رسانه‌ای سعودی
SRMG
شناخته می‌شود. این گزارش تأکید می‌کند که مالکیت شبکه شفاف و مستقیم نیست و در قالب ساختارهای مالی پیچیده و آفشور انجام شده است
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/12910" target="_blank">📅 00:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12909">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شاهزاده رضا پهلوی :اگر اروپا می‌تواند اتحادیه خودش را داشته باشد، چرا ما نتوانیم در خاورمیانه اتحادیه‌ای داشته باشیم؟
چرا نتوانیم در پروژه‌های مشترک مربوط به امنیت ملی، اطلاعات و حتی همکاری‌های نظامی همکاری کنیم؟
چرا باید بخش زیادی از بودجه‌مان را صرف تسلیحات و مسابقه تسلیحاتی کنیم، به جای اینکه این منابع را صرف رفاه، صندوق‌های بازنشستگی، بهداشت و آموزش کنیم؟
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/12909" target="_blank">📅 00:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12908">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نیویورک پست: وجوه مسدود شده مستقیما به ایران ارسال نخواهد شد، بلکه برای خرید مواد غذایی و تجهیزات پزشکی استفاده خواهد شد و پرداخت آنها منوط به تعهد تهران به باز کردن تنگه هرمز و پاکسازی مین‌ها خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/12908" target="_blank">📅 00:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12907">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شاهزاده رضا پهلوی:تصور کنید که فردا مدل سیلیکون ولی در سیستان و بلوچستان اجرا شود. چرا که نه؟
هر چیزی که کشور نیاز داشته باشد از هوش مصنوعی گرفته تا فناوری و نوآوری می‌تواند در آنجا توسعه یابد.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/12907" target="_blank">📅 23:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12906">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مقام دولتی:
نشست ترامپ در اتاق عملیات به پایان رسید وحدود دو ساعت به طول انجامید.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/12906" target="_blank">📅 23:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12905">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نیویورک پست:
زمان نهایی شدن تفاهم‌نامه بین آمریکا و ایران مشخص نیست
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/12905" target="_blank">📅 23:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12904">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f2fb766b.mp4?token=ciyizOj8UegN5nLl57vLezTtzBzuP2M3bKa2NcxFnllUfVdgkkiN9r2_5rPZfJ9Lu4B1MCCQtEHI3H1oZidQZngHcbc68ysZHBkIN_KF0gi26kAwPz-bTn_Ht_4zc1SCX06zv6XEcZn-cXbbNF86UYWdxC_sWGiNWh3NIdI9Fs6eKxAztdi7UTcKew9ZOIo1_Ukm_BQoD_oAYOlczQZu59w_DfRTISntk6kgZ3cgZfilWmMMaJunlrDlJFCGDMesqSVFCijlVdQAUnsSa_r7cpy3_kzLpl6_j0xquXxdYWgvpgh52iLrQFDfsMA-5D4XwLQL9Pz2ErRlZFUVw_MTKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f2fb766b.mp4?token=ciyizOj8UegN5nLl57vLezTtzBzuP2M3bKa2NcxFnllUfVdgkkiN9r2_5rPZfJ9Lu4B1MCCQtEHI3H1oZidQZngHcbc68ysZHBkIN_KF0gi26kAwPz-bTn_Ht_4zc1SCX06zv6XEcZn-cXbbNF86UYWdxC_sWGiNWh3NIdI9Fs6eKxAztdi7UTcKew9ZOIo1_Ukm_BQoD_oAYOlczQZu59w_DfRTISntk6kgZ3cgZfilWmMMaJunlrDlJFCGDMesqSVFCijlVdQAUnsSa_r7cpy3_kzLpl6_j0xquXxdYWgvpgh52iLrQFDfsMA-5D4XwLQL9Pz2ErRlZFUVw_MTKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، اسکات بسنت:
ما حدود ۱ میلیارد دلار از رمزارزهای ایران را توقیف کرده‌ایم فقط مستقیم کیف‌پول‌ها را گرفته‌ایم.
برخی از آن‌ها شاید همین الان در حال تایپ کردن باشند و هنوز متوجه نشده‌اند که کیف‌پولشان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/12904" target="_blank">📅 23:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12903">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شبکه کان اسرائیل :
نتانیاهو خواستار از سرگیری حملات به ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/12903" target="_blank">📅 23:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12902">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پست جدیددد اتاق جنگ داغ داغ کلیک کنید و کارای اداریش رو انجام بدید
💥
https://www.instagram.com/reel/DY7xeuCRP_4/?igsh=aW9oOXNnbno1NDJ6</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/12902" target="_blank">📅 22:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12901">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNW2y9F6aqjs1B6Qjx12shcj617DkjhDuRQL4wFNo4pHiLUC16l00RrOlCT0rumeQSgpr-ADzi0NAcxxjVTJcA_5p74TVf52CT9kZpe-p0oQ-Ql9EZOvN_7PWWy7UkTFbkkRN4ps2KEHEOQtKerEuos76RZmoLMhvGDbVw_as5tDWXiCK4gY3-qRYk-zck01vafNgL0WIti7bGDGPvE9i75wsMJ5Zwd9Nz9X7K9cTwU1KrkFhYEFakyLN_B6MFtWZ-G2XxZxMHr3KtT804zBaHX14VnLidmM2pFfVZPtXb6EIhJzdFeLOU2uWiKLUvUn2-jB1U91bpA1HK6yxVofkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/12901" target="_blank">📅 22:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12900">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">المانیتور: تیم ترامپ، در اقدامی قابل توجه، ایده ایجاد یک صندوق ۳۰۰ میلیارد دلاری را برای ایران مطرح کرده است.
این پیشنهاد در شرایطی مطرح می‌شود که پیش از این، تهران یک پیشنهاد تجاری مشابه را رد کرده بود.
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/12900" target="_blank">📅 22:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش انفجار دارم از‌ بندر</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/12899" target="_blank">📅 22:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/12898" target="_blank">📅 22:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12897">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدای نوتیفیکیشن پولای بلوکه شدست دارن واریز میکنن
🤣
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/12897" target="_blank">📅 22:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12896">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تسنیم: ریز پرنده دشمن رو تو قشم زدیم
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/12896" target="_blank">📅 22:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12895">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/12895" target="_blank">📅 22:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12894">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">منابع محلی ۲ انفجار در قشم همزمان با فعالیت پدافند هوایی گزارش دادند.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/12894" target="_blank">📅 21:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12893">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cf89fccf.mp4?token=iGNKf3wsFQlGvv3tRCUrCPMJRO1SgZo5d_SUMo2ijSvuL9SQw3xhHSrn6fIvLrcXbcIS07OtlT19XVIJwNuQlJWqFU_uqzCDzbb9jMqfxKr1W5tO8qYzXDZ8Lrr2pQHzpbv6uAc5Y7PhLtD_wgpJr-xiG9cT9Qb8_Mwj533vq-pq_hpjFf89JMNqNDfWXYymzDXcccUFAEGqy8ZNyVUmIYGSFk7gNdkHtHaHu-0LZTPCRgTM6SYE8cTKY9w7H5nRv0TWJyIxsJaSfR_xviOHsO2cuRvqMMCMhx2opxKjj1yOpYl6xkDNkynck8rbZYluhhFckugnSc8jVHAGkS6jmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cf89fccf.mp4?token=iGNKf3wsFQlGvv3tRCUrCPMJRO1SgZo5d_SUMo2ijSvuL9SQw3xhHSrn6fIvLrcXbcIS07OtlT19XVIJwNuQlJWqFU_uqzCDzbb9jMqfxKr1W5tO8qYzXDZ8Lrr2pQHzpbv6uAc5Y7PhLtD_wgpJr-xiG9cT9Qb8_Mwj533vq-pq_hpjFf89JMNqNDfWXYymzDXcccUFAEGqy8ZNyVUmIYGSFk7gNdkHtHaHu-0LZTPCRgTM6SYE8cTKY9w7H5nRv0TWJyIxsJaSfR_xviOHsO2cuRvqMMCMhx2opxKjj1yOpYl6xkDNkynck8rbZYluhhFckugnSc8jVHAGkS6jmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدافند قشم همچنان فعاله
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/12893" target="_blank">📅 21:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12892">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">امشب از ته وجودتون خالصانه از خدا بخواهید امیدوارم که ندای ما را بشنود و بهترینها برایمان اتفاق بیفته
🍀</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/12892" target="_blank">📅 21:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">سلام اين  مسير دقيقا مسير قاهره هست  . درست داره ميره ولى ما چون مسير قاهره رو بلد نيستم فكر ميكنيم داريم اشتباه ميريم</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/12891" target="_blank">📅 21:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12890">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a2a5d870.mp4?token=b1SGuR5CFqWq-g0pes1f51xsiyuAJBynZpMZDJ8usdDKMfRItQheqvteNVebyukTK3S6vJNndSJa6VRUDMvCOAI84TZrgZy9r0FDCGTevjuao6087a4mcn4Jh6tBTeeYC6A8pIfQDYj_2FF-5vb3AjAAbj4iCFC4mMvEUWgBVqj_gWOml7M9w-gMkFvXdMVm4wvRv8YO2YWzmYdOiK7sLLl0z_oJajwb0z7OTcBzvXt5Qix4F71kpRtgL3FhhHM4qOVAXK1aq3KhAXz4kZ3JO45-q9kpbHQQ0XFEijPRvQ8sk1Dlv1uJ6l7WJvLXiJumVCDJK5E6O7UcCMpup_s-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a2a5d870.mp4?token=b1SGuR5CFqWq-g0pes1f51xsiyuAJBynZpMZDJ8usdDKMfRItQheqvteNVebyukTK3S6vJNndSJa6VRUDMvCOAI84TZrgZy9r0FDCGTevjuao6087a4mcn4Jh6tBTeeYC6A8pIfQDYj_2FF-5vb3AjAAbj4iCFC4mMvEUWgBVqj_gWOml7M9w-gMkFvXdMVm4wvRv8YO2YWzmYdOiK7sLLl0z_oJajwb0z7OTcBzvXt5Qix4F71kpRtgL3FhhHM4qOVAXK1aq3KhAXz4kZ3JO45-q9kpbHQQ0XFEijPRvQ8sk1Dlv1uJ6l7WJvLXiJumVCDJK5E6O7UcCMpup_s-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ :  الان پدافند قشم
💥
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/12890" target="_blank">📅 21:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12889">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
پدافند قشم فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/12889" target="_blank">📅 21:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12888">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری فرانسوی: جارد کوشنر مانع امضای تفاهم‌نامه بین آمریکا و ایران شد
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/12888" target="_blank">📅 20:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤣
😃</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/12887" target="_blank">📅 20:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/12886" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مدیرکل آژانس بین‌المللی انرژی اتمی پیشنهاد داد که قزاقستان اورانیوم غنی‌شده ایران را نگه‌داری کند
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/12885" target="_blank">📅 20:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">لارنس نورمن، خبرنگار وال استریت ژورنال:
این توافقی که ازش صحبت می‌شه فعلاً یه توافق کامل نیست که تمامی مسائل از جمله هسته‌ای رو در بر بگیره
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/12884" target="_blank">📅 20:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کاش جای ترامپ دو تا بی بی داشتیم البته همون یدونشم کارو در میاره .این کله زرد به خاطر پول زرد میکنه اخرش</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/12882" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza Rohani</strong></div>
<div class="tg-text">کاش جای ترامپ دو تا بی بی داشتیم البته همون یدونشم کارو در میاره .این کله زرد به خاطر پول زرد میکنه اخرش</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/12881" target="_blank">📅 20:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خب دیگه عمو یاشار با پای پیاده میریم نه با ترامپ</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/12880" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParsa</strong></div>
<div class="tg-text">خب دیگه عمو یاشار با پای پیاده میریم نه با ترامپ</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/12879" target="_blank">📅 19:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/12878" target="_blank">📅 19:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پرزیدنت ترامپ در اتاق وضعیت کاخ سفید مستقر شد.
تصمیم‌گیری نهایی درباره مذاکرات با رژیم ایران در دستور کار است.
نیویورک پست: واشینگتن برای گام‌های بعدی آماده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/12877" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12876">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به نظر میاد قاهره کنسل شد مارو وسط راه پیاده کرد</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/12876" target="_blank">📅 19:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12875">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAm.ir_reza</strong></div>
<div class="tg-text">به نظر میاد قاهره کنسل شد مارو وسط راه پیاده کرد</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/12875" target="_blank">📅 19:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12874">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jangal bedoneh risheh (iG @yashar)</div>
  <div class="tg-doc-extra">siavash ghomeishi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/12874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/12874" target="_blank">📅 19:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12873">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فارس: متن توافق که تحت قالب «تعهد در برابر تعهد» تدوین شده، در مراحل نهایی تصویب در ایران قرار دارد و هنوز تصمیم قطعی اتخاذ نشده است.
@withyashar
کلان رژیم جمهوری اسهالی‌تو کاره فیفتی فیفتیه
🥴
🤣</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/12873" target="_blank">📅 19:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12872">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فارس : ترامپ تا نیمی از پول رو نداده همه چیز باد هوا است
@withyashar
🤣</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/12872" target="_blank">📅 19:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12871">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرگزاری فارس: ادعاهای ترامپ دروغه و فعلاً خبری از توافق نیست.
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/12871" target="_blank">📅 19:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12870">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOeSelKbg53sYe4lf6PIR5Evz-cKhpnmjFV1n0tL1L14H41ratVDNVytTPay5gjO1z9oL_bHa3kPV_SXegT4gLm48nj43jBKzgl7m0B0nY_vch6fH-KDKtRz8M3YqsvITW1_Pjzt2wbDpfjcy37clQ01w_Qiw5pQqte4J3bsyHzBIP1THtM-NiORW-_2Tf3e6NxNxgLip735SVAkGoVzrB7nMyzLtLkz_nhA58gM4jCAvgZtu-virotsL0E04b5UMVnftJjipNVHqdh57oGc6dPm2xDgfIbxL5liYoZo8_a-HbV1f4I5gny-OvUTw_xEF_htc3vwrSWwga3tJHdHhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از پست ترامپ در تروث سوشال، قیمت نفت برنت برای اولین بار پس از 50 روز به زیر 90 دلار در هر بشکه رسید.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/12870" target="_blank">📅 19:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12869">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اتاق جنگ با یاشار : ریلکس‌ باشید ترامپ در هر صورت کار رو در میاره ولی حامله میکنه
🤣
🙌🏾
داریم میریم قاهره</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/12869" target="_blank">📅 19:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12868">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خبرنگارهای نزدیک به کاخ سفید می‌گویند: ترامپ منظورش را در پستش اشتباه بیان کرده بود؛ او در واقع پایان محاصره دریایی علیه ایران را اعلام نکرده.
بلکه منظورش این بوده که اگر ایران با این شروط موافقت کند، آن محاصره لغو خواهد شد.
@withyashar
🥴</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/12868" target="_blank">📅 19:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12867">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اتاق جنگ با یاشار : یا موسئ ادرکنی
@withyashar
معنی ادرکنی : مرا دریاب و به فریادم برس</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/12867" target="_blank">📅 18:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12866">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اتاق جنگ با یاشار : ریلکس‌ باشید ترامپ در هر صورت کار رو در میاره ولی حامله میکنه
🤣
🙌🏾
داریم میریم قاهره</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/12866" target="_blank">📅 18:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12865">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ۱۵ عبری: به نظر میرسد ترامپ با یادداشت تفاهم با ایران موافقت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/12865" target="_blank">📅 18:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12864">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الجزیره: ناوگان سوخت رسان های آمریکا در فرودگاه بن‌گوریون تا ۷۲ ساعت دیگر به پایگاه های اصلی خود در اروپا برمیگردند
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/12864" target="_blank">📅 18:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12863">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/12863" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12862">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.  تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما…</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/12862" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12861">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhzWybJLCveQhCn0nBjuuv12wk7VyWmda06d4mRrte7EnjNcHmwf0g7DSIKSlWg1F9iErh5ZMXdzh_yMTQ9M72QKVc2qYF9ASBnpRMhfzwagwpx4ZgbGfCJtRaXzMby-SwfPd8TtWaDKdA9wmZPDsGm8uG2jQnKGuLJgFgmfWXzc11nR_ZXa0ZE97sx0YIPZHfzZ1s3WBKrvFv-3iVF75NxS39HeZiu4S12DHcr4qPL8-_R0vPC1YQO99w6ccqxEEazkvvzFN_r6zY5J-of-6o205pjlLUPeaOKqZJcSjK3Dw_uyNInW-6llQZttL-kTdPCSzLRaGPROtR-tOhLg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
@withyashar
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
@withyashar
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/12861" target="_blank">📅 18:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12860">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02caddcc.mp4?token=t32HNtNIISM17fbPwT6UmADc2rihdkwEecs4SZwzif7_PYAS1Xa2Xps9YpeYWUt5umWhNKiAAjml1SBMg57CPtRcUcdbor6W0AUwctuoumPJG1oD8GuSVI8tp097oxBcQE1m4YZGWsw1TTh79J6L4HRsfe38shnky9AVN17pYH2_H-KoYbaa-0JliyEy2TO1X4omP9-RTiDezK0L2hLBxAT-jlcqh3KvFC98HyajiSjs3oWhiU00L2sSZeUHYwAvheeIKfpcuRWS7bMuK-MNtATa7kooABrg6rqZkc-nM1wGJUkIKZpcrzwdTOM4pt3IxNd1MHsJmkFgeIbL9zbTOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02caddcc.mp4?token=t32HNtNIISM17fbPwT6UmADc2rihdkwEecs4SZwzif7_PYAS1Xa2Xps9YpeYWUt5umWhNKiAAjml1SBMg57CPtRcUcdbor6W0AUwctuoumPJG1oD8GuSVI8tp097oxBcQE1m4YZGWsw1TTh79J6L4HRsfe38shnky9AVN17pYH2_H-KoYbaa-0JliyEy2TO1X4omP9-RTiDezK0L2hLBxAT-jlcqh3KvFC98HyajiSjs3oWhiU00L2sSZeUHYwAvheeIKfpcuRWS7bMuK-MNtATa7kooABrg6rqZkc-nM1wGJUkIKZpcrzwdTOM4pt3IxNd1MHsJmkFgeIbL9zbTOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم تحلیلگر ارشد صدا و سیما:   دوران بمب اتم دیگه گذشته الان با عملیات میکروبی و بیولوژیک میشه حمله کنیم و بعدش نگیم که ما بودیم
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/12860" target="_blank">📅 18:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12859">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">️فاکس نیوز به نقل از وزیر جنگ آمریکا: ایران دو گزینه دارد: یا از طریق مذاکره برنامه هسته ای خود را کنار بگذارد یا از طریق نیروهای ما
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/12859" target="_blank">📅 17:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12858">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تسنیم : مذاکرات در جریان است و متن توافق تغییر هایی داشته است
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/12858" target="_blank">📅 17:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12857">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzQswYxV6hC0YK6L3_rVd8tCaihPxf2pk4PXTTOaPnhYH4851yRPl5H8cG8dtqr8wjhj9HvScdzMeSW6vl2hOMN7abA-vYzzEZv9WWtjeOQ0xaf3WJM14kmIKU53aKwRksgtJd-uKh37ZJBsTdmhG8JffmJgB5Bd20vgPD7-xWr_VZam_DD1ttpZg8XYpyzWlqLQn5bSSg7PNt-UrHE44gpE-ZBWV2-n49Q7ADCKiydS5RB7yfAU9DCvhhEo8K6MpDPGJSVivu_Ud3hhGKIc_c5sN3x0j1JaqRBe_G5gpTkPr-Iyn2qJwdvtxyeDYd9fwZQ87TRUAVa8tno106q1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مم با قر خالیباف‌ در اکس :
۱- ما امتیازات را نه با گفتگو، بلکه با موشک‌ها می‌گیریم، در مذاکره فقط آن‌ها را تثبیت می‌کنیم.
۲- هیچ اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است. اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد.
۳- پیروز هر توافق، کسی است که از فردای آن بهتر برای جنگ آماده شود.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/12857" target="_blank">📅 16:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12856">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">️سی‌ان‌ان: ترامپ به مشاورانش گفته  که برای تصمیم‌گیری در مورد امضای توافق احتمالی با تهران به چند روز زمان نیاز داره
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/12856" target="_blank">📅 15:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12855">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEZD1ZDSl0z5CY5ygiFGwxVFGZ7Vnn5IkqQQ-8zmEyNdKoBG6CmjJICFJbDs-rwB86ZNs6oI4BTtK8fFIY7FaUF6qMx8fmoiW0Tlc5Sm9fnmwSazxIZWGe97k7P8fFVzIEwJXWaJzpchZ-47sH9WGSIb-6SVc13PJdaK536Y2YhN6TsoUc5g9tFl_9s3V1xEDU2wKZNRlqzOtLGeHCP1-IffbMYGnBrnzAulTe-s83ibJd3MeXy-RLphyLqxNv3LVjbHSMZPxzLWeO8QAt1gZ_ABUOLGtdbS4orvp58VhN34VCF3TzvwEJBtZWVDR8CV6rwapgD5uTDJKftKW5Yukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سری سوالات بی جواب تجمعات شبانه
😃
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/12855" target="_blank">📅 14:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froms@ti🍁🍂️</strong></div>
<div class="tg-text">سلام یاشار جان
من نامزدمو یه هفته پیش از دست دادم سرطان داشت
😔
تا لحظه ی اخر میگفت ناامید نباش یاشار گفته میزنه،تو دی ماه هم واقعا به سختی نجات پیدا  کردیم از تو خیابون .واقعا اگه ما پیروز نشیم من حس میکنم خون این همه ادم پایمال میشه،ما فقط به امید شما داریم زندگی میکنیم.هیچ وقت اخرین حرفشو تو ملاقات اخر یادم نمیره.فقط پیام دادم بگم  حتی امید اون ادمی که روی تخت بیمارستان هم نفس های اخرشو میکشه هم  هستی
🥺
خدا حفظت کنه واسه ما
🙏
❤️
🌺</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/12854" target="_blank">📅 14:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12853">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ffdc5f87.mp4?token=tHqA5cXvNEGHHoeMdz-UAiRQf4vYTR8afIb3vlNqVMtcgWj-AjiWgOCo5imkLcYdCZ0u4oRkHL6reeTBjR0Ocm5h850AUvf64YRhAbo6J7NllbDuF8YWUUFDpKB4AEe-tsO4wC5xvqNs1AWiHn0VOr4xTMdI0cZpxTTSL48NOV079sWFJXdh_BK6uYfqznwE0pF7mh8EevH8uyKuNrbeK2wT6JgzwU6o_6QJyokubQ50JCpiRmkrDxND0Sffz0O9rEZbShChVpHMqTQ4bkHAEOkFXD-vKd5ZCiY4vW-QDUBAOINCmmJZVTA3CFQ1KBhhJKGIWqTaceR6IR2oYPXH1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ffdc5f87.mp4?token=tHqA5cXvNEGHHoeMdz-UAiRQf4vYTR8afIb3vlNqVMtcgWj-AjiWgOCo5imkLcYdCZ0u4oRkHL6reeTBjR0Ocm5h850AUvf64YRhAbo6J7NllbDuF8YWUUFDpKB4AEe-tsO4wC5xvqNs1AWiHn0VOr4xTMdI0cZpxTTSL48NOV079sWFJXdh_BK6uYfqznwE0pF7mh8EevH8uyKuNrbeK2wT6JgzwU6o_6QJyokubQ50JCpiRmkrDxND0Sffz0O9rEZbShChVpHMqTQ4bkHAEOkFXD-vKd5ZCiY4vW-QDUBAOINCmmJZVTA3CFQ1KBhhJKGIWqTaceR6IR2oYPXH1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست ، وزیر دفاع آمریکا با لاتی‌ پر مانند مربیی که تیمش را به زمین میفرستد،  خطاب به نیروهای آمریکا روی ناو USS Boxer گفت:
«رئیس‌جمهور گفت: ایران یا می‌تواند راه درست را انتخاب کند یعنی پای میز مذاکره توافق کند یا با مردِ سمت چپ من طرف شود.»
«آن مردِ سمت چپ، اتفاقاً من بودم.»
«اما در واقع من نیستم…»
«شمایید.»
یعنی شما نیروهای نظامی آمریکا هستید.
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/12853" target="_blank">📅 14:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12852">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromomid.behroozi</strong></div>
<div class="tg-text">سلام یاشار عزیز من امشب عروسیمه امشب میزنه آماده باشم تو باغ مهمونا رو از قبل آماده کنم میزنه ؟؟
😂
😂</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/12852" target="_blank">📅 14:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12851">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بر اساس تحلیل نشریه اکونومیست، طرفین درگیر ممکن است بیش از هر زمان دیگری به یک توافق نزدیک شده باشند.
با این حال، این توافق جامع نخواهد بود و جنگ را برای همیشه پایان نخواهد داد.
این نشریه در ادامه توضیح می‌دهد که چگونه ملاحظات و بازی‌های سیاسی، عامل اصلی ارسال این پیام‌های ضدونقیض از سوی طرفین است
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/12851" target="_blank">📅 13:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12850">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیویورک تایمز: یکی از جدیدترین و شگفت‌انگیزترین عناصر پیش‌نویس توافق صلح ایران، یک صندوق سرمایه‌گذاری پیشنهادی برای ایران به مبلغ ۳۰۰ میلیارد دلار است.
ایران در ابتدا این موضوع را به عنوان غرامت برای خسارات جنگ (که آن را بین ۳۰۰ میلیارد تا ۱ تریلیون دلار تخمین می‌زند) مطرح کرد. طرف آمریکایی آن را به عنوان یک «صندوق سرمایه‌گذاری بین‌المللی» که به تسهیل آن کمک می‌کند، بازتعریف کرده است
یک چارچوب نرم‌تر که از کلمه غرامت اجتناب می‌کند.
به نظر می‌رسد این ایده از استیو ویتکوف و جرد کوشنر نشأت گرفته است که پروژه‌های املاک و مستغلات تهران و یک ابزار سرمایه‌گذاری گسترده‌تر را به عنوان شیرین‌کننده‌های معامله مطرح کردند
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/12850" target="_blank">📅 13:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12849">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستان من گفتم فردا میگم کجا متن ها رو بفرستید دوبار هم در متن تاکیید کردم! پیغام هایی که الان دایرکت دادید بین پیغام های‌دیگه میره و از دست میره حتی نیمتونم بخونم
😟
چرا درک نمیکنید خیلی واضح گفتم</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/12849" target="_blank">📅 13:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12848">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خب این متن را مینویسم که همه حتما ببینند. امروز و فردا روز بسیار مهمی هست. ما هر دو شب را بیدار خواهیم ماند برای گزارش و برای دوشنبه آخر شب هم در صورتی که حمله نبود میخواهیم یک پیام برای شاهزاده بفرستیم ساعت ۱۱:۱۱ دقیقه . در نتیجه از همه شما دعوت میکنم خیلی…</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/12848" target="_blank">📅 13:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12847">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71af41e04e.mp4?token=UjA1sTp8DvDoRjsAcFKDrvzqxJeomAzMQRXGC-ZdCwD_0EboiAGJBREV6zw_8Id0OBZEGA68QnAn72Q1tVAdBELxA5Y1xbccPrzfB0hVRej4j4P7lXkAstXopf36-hIobYgMLCwQMwQhANnij_eIYxUW13aaA_THiPwd3QXt82ykXVYWevCJnCj-BKDWCPnyjz7tW7BZrC-id0qdDTnu-VZXUmBDxkZVcKAwXmSugbfmGm4sTZSIxNh71wLVwBwMyFObp8Qw6bmUffq5OtVuEt7PiJ6R6h7OY9Z0MLln3RJGr3GANm75AtrvPBNhNd9BoDcm-h6tskZq3rp4IWaoV15NEsM6LlKuhe4fxtsNVVRkCHnEbhp4e5Bbal61A_i1c1oghIMWOCc0230tF7lMaoTD77FYS3wlkkxTZt_2xIqzzbX2FeEu6Hgrdhn1Xk-ttXcB50EZuLyYxFXOFXrUROBQ0MHdsZX26NTuwxbp9QjNRsSQwQ-imKNVS8nQf4iWiH7e5vXJttsLEpUlOmGGMworvddV5_rXxaQo50wqjO6I66B7-4rep8bBEKbeCqEuJb9ABshe2lF2vUqE10IKHbmqGkABsmcUkjmRevVKPQ4rRclv16fk2nopxkOVSS4zCX8K02U-86KOULVQRk8HdeLMlauCvHvteB1ZZw_oLLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71af41e04e.mp4?token=UjA1sTp8DvDoRjsAcFKDrvzqxJeomAzMQRXGC-ZdCwD_0EboiAGJBREV6zw_8Id0OBZEGA68QnAn72Q1tVAdBELxA5Y1xbccPrzfB0hVRej4j4P7lXkAstXopf36-hIobYgMLCwQMwQhANnij_eIYxUW13aaA_THiPwd3QXt82ykXVYWevCJnCj-BKDWCPnyjz7tW7BZrC-id0qdDTnu-VZXUmBDxkZVcKAwXmSugbfmGm4sTZSIxNh71wLVwBwMyFObp8Qw6bmUffq5OtVuEt7PiJ6R6h7OY9Z0MLln3RJGr3GANm75AtrvPBNhNd9BoDcm-h6tskZq3rp4IWaoV15NEsM6LlKuhe4fxtsNVVRkCHnEbhp4e5Bbal61A_i1c1oghIMWOCc0230tF7lMaoTD77FYS3wlkkxTZt_2xIqzzbX2FeEu6Hgrdhn1Xk-ttXcB50EZuLyYxFXOFXrUROBQ0MHdsZX26NTuwxbp9QjNRsSQwQ-imKNVS8nQf4iWiH7e5vXJttsLEpUlOmGGMworvddV5_rXxaQo50wqjO6I66B7-4rep8bBEKbeCqEuJb9ABshe2lF2vUqE10IKHbmqGkABsmcUkjmRevVKPQ4rRclv16fk2nopxkOVSS4zCX8K02U-86KOULVQRk8HdeLMlauCvHvteB1ZZw_oLLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس دفتر کاخ سفید در امور سیاست، استیون میلر:
ایران امتیاز های خیلی قابل توجه، مادی  به ایالات متحده داده که قبلا میگفت غیر ممکنه
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/12847" target="_blank">📅 13:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12846">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فارس نیوز ، خطیب نماز جمعهٔ تهران: دشمن متوقف نیست، ما باید در مرز دانش و فناوری حرکت کنیم
حجت‌الاسلام ابوترابی: تعرض آمریکا در سحرگاه دیروز به نقطه‌ای در حاشیه فرودگاه بندرعباس که نه خسارت جانی داشت و نه خسارت مالی، اما تعرض به آسمان و زمین ایران بود. این تعرض از پایگاه هوایی آمریکا در منطقه انجام شد
@withyashar
🥴</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/12846" target="_blank">📅 13:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12845">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب این متن را مینویسم که همه حتما ببینند. امروز و فردا روز بسیار مهمی هست. ما هر دو شب را بیدار خواهیم ماند برای گزارش و برای دوشنبه آخر شب هم در صورتی که حمله نبود میخواهیم یک پیام برای شاهزاده بفرستیم ساعت ۱۱:۱۱ دقیقه . در نتیجه از همه شما دعوت میکنم خیلی رسمی و محترمانه صحبتهای خود را بنویسید  و امروز بر روی متن تمرکز کنید و فردا از ساعت ۱۰ صبح تا ۱۰ شب برای من ارسال کنید تا چکیده ای از تمام آنها را ارسال کنم و فقط کلام من نباشد. حتی شده یک کلمه از پیام هر شخص را برمیداریم و متنی باهم میسازیم که در خور باشد. پس از شما دعوت میکنم به این کمپین بپیوندید ،لطفا امروز و فردا از فرستادن دایرکتهای غیرمعمول بپرهیزید سوال بیشتری را نمیتوانم پاسخ بدهم متن کامل است هر صحبتی که دارید  در  همان متن بنویسید تا همه با هم متن پایانی را استوری،  کامنت ، دایرکت و ایمیل کنیم
🙌🏾
. شروع ارسال فردا ۱۰ صبح و آخرین مهلت ارسال برای من  فردا ۱۰ شب است.
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/12845" target="_blank">📅 11:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12844">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تحلیل عوستاد رائفی پور :
آمریکایی‌ها نیروهای بیگانه فضایی هم کمک گرفتن
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/12844" target="_blank">📅 11:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12843">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد جمهوری اسلامی می‌خواهد اورانیوم غنی‌سازی‌شده خود را به چین منتقل کند، مشروط بر آن‌که چین تضمین دهد این مواد را به آمریکا تحویل نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/12843" target="_blank">📅 11:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12842">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسرائیل هیوم در گزارشی نوشت موساد در سال‌های اخیر شاخه‌ای محرمانه برای نزدیک‌تر کردن سقوط جمهوری اسلامی ایجاد کرده است. به گفته منابع آگاه، رییس موساد متقاعد شده است که اگر ترامپ با تهران توافق نکند و محاصره دریایی را ادامه دهد، جمهوری اسلامی تا پایان سال ۲۰۲۶ سقوط می‌کند.
ماموریت ابتدایی این شاخه که در سال ۲۰۲۱ و پس از آغاز ریاست داوید بارنیا بر موساد ایجاد شد، عملیات‌ هدفمند برای کنار زدن مقام‌های ارشد جمهوری اسلامی بود، اما به‌تدریج به بخشی از راهبرد گسترده‌تر موساد برای «تغییر رژیم» تبدیل شد.
رییس پیشین این شاخه به اسرائیل هیوم گفت موساد در گذشته بیشتر از طریق ترور افراد را حذف می‌کرد، اما اکنون افشای اطلاعات شرم‌آور یا آسیب‌زننده درباره مقام‌ها می‌تواند آن‌ها را از حلقه قدرت خارج کند؛ روشی که به گفته او «ارزان‌تر و ساده‌تر از عملیات ترور» است.، مقام‌های موساد معتقدند عملیات‌های اخیر علیه ایران فقط یک مرحله در مسیر سقوط جمهوری اسلامی بوده است. رئیس پیشین شاخه نفوذ گفت این واحد اکنون با شدت بیشتری فعالیت می‌کند و هدف آن «سریع‌تر کردن ساعت شنی پایان حکومت است».
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/12842" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12841">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سنتکام : ادعا: تلویزیون دولتی ایران ادعا کرد که نیروهای ایرانی یک هواپیمای آمریکایی را در نزدیکی بوشهر سرنگون کرده‌اند. نادرست.
حقیقت: هیچ هواپیمای آمریکایی سرنگون نشده است. تمام دارایی‌های هوایی ایالات متحده در نظر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/12841" target="_blank">📅 10:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12840">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWxvvOfJ-2IV9ikp9duXnyv2bi3mX_g_7B-v2_g9OE4S6FkUvyhDdBQss6TnvBKzW7HI4Pbos-LPj5StNobIWl5jU9fXyhyd4SCfZpMNypSiF4hkJe5ULzWnLEEzTB1w8P5MmFL01RGsLYgMoG0NYN7OU1bEud7lwMRnJq_l1Ea_MSsR45KXBHK89MlEuhxaNyQdVnlF4COjsjRBmVT-_rjTKjUkwvq9TeDSbc3qqhC3D7RHIa4oH1JOyJVa0_fqvZ8Xd_vUogzcvVbsgXkCHDtzY_lbLTNhXchwn7R6fG4a1GfyVobV3ytNwDcjLIXm1F8f9P3tovcUhKvePqEdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید علی کریمی و حمایت از شاهزاده رضا پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/12840" target="_blank">📅 10:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12839">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس: آنچه امروز جمهوری ایران دنبال می‌کند، مدیریت هوشمند تنگه هرمز است.
اعمال کنترل و ترتیبات ایران در تنگه هرمز ماهیت دائمی دارد و بی‌تردید مقطعی نیست.
ایران قصد ندارد اورانیوم غنی شده خود را به کشور ثالث منتقل کند.
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/12839" target="_blank">📅 09:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12838">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز: ترامپ در شرایطی به دنبال پایان دادن به جنگ با ایران است که همزمان با دو فشار متضاد مواجه شده است. از یک سو افزایش قیمت انرژی و نگرانی از تبعات اقتصادی جنگ، کاخ سفید را به سمت دستیابی به توافق سوق می‌دهد و از سوی دیگر بخشی از جمهوری‌خواهان و متحدان سیاسی ترامپ خواهان ادامه فشار نظامی و جلوگیری از هرگونه امتیازدهی به جمهوری اسلامی هستند.
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/12838" target="_blank">📅 09:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12837">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a0d910cb.mp4?token=nd409Z2bzG0P7EhUAsRJwWT-Dq9ATafP0ly5xBSgTKtHBbNOX7acPjCFWuyMpkhJHvr_HKzMKUjgLt_HubytttBGKs4pDckzOpQGJW-un6hHmRo_lwPDIcCZwAiyJFxfFXf0kOJeXsYA62FM-thG9a86qH5eOz-pxjMgPbqxc1IEn4vZfM5roALr8SEQjxrXJ9tItUfhL65Shixoo7TwA2YnKqMEtJ5jjXV4k2x-r7w_1OSRrcNh1GFZSY2iZ_MMxzSLaJ5Chm4YSSkx5x3YLpF_CnIvAIgZZHXpZkyNLdnfXN6-qydHLSzUmoz5VfTYoQShqmq3lNxGHOWpjPDHDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a0d910cb.mp4?token=nd409Z2bzG0P7EhUAsRJwWT-Dq9ATafP0ly5xBSgTKtHBbNOX7acPjCFWuyMpkhJHvr_HKzMKUjgLt_HubytttBGKs4pDckzOpQGJW-un6hHmRo_lwPDIcCZwAiyJFxfFXf0kOJeXsYA62FM-thG9a86qH5eOz-pxjMgPbqxc1IEn4vZfM5roALr8SEQjxrXJ9tItUfhL65Shixoo7TwA2YnKqMEtJ5jjXV4k2x-r7w_1OSRrcNh1GFZSY2iZ_MMxzSLaJ5Chm4YSSkx5x3YLpF_CnIvAIgZZHXpZkyNLdnfXN6-qydHLSzUmoz5VfTYoQShqmq3lNxGHOWpjPDHDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس: دستاوردهای ما علیه ایران قابل توجه بوده است
جی‌ دی ونس، معاون رئیس‌جمهور آمریکا: اگر به آنچه تاکنون به دست آورده‌ ایم نگاه کنید ،در صورتی که بتوانیم به یک توافق نهایی برسیم ،در حال بازگشایی تنگه هرمز هستیم.
ما پیش‌تر توان نظامی متعارف آنها( ایران) را به‌ شدت تضعیف کرده‌ ایم و در موقعیتی قرار داریم که میتوانیم برنامه هسته‌ ای‌ شان را به‌ طور قابل توجهی عقب بیندازیم،نه فقط در دوره این رئیس‌ جمهور، بلکه در بلندمدت.
این یک اتفاق بسیار، بسیار خوب برای مردم آمریکا است.
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/12837" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12836">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یه مقام ایرانی به وال استریت ژورنال: تهران نگرانه که اسرائیل، آمریکا رو از مذاکرات خارج کنه
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/12836" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12835">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9915e2bfef.mp4?token=QCBv9NB3PrbsmUuOldK1P88Q5fUxQZoRXp10QVhhROhdTS_y4g0xGNI-ly9uSCiAb2LrrGtVeN3LFZ7IoJ6LlH__Nuq0BNA4Dwz9ahkjZj3HrU5WeoolAmmFI3KcudL2GTLYXarj-pEk1mxzqsU27AJGzvwbWO-dErCBQxUIdsYP0M2id6-ePoXvvw8AKKdhf6XH-AgNvBASASMy7pGt2l33M6gP8YRmCcUfWqbo8yUs8HDqmEzSpSJ1W2dSz-VuJflKzPw1ZcdGXOMuO4lY0QM990HPaQr1Jlf-HNsyqmbKKhBeOZqY2TFc3AFB7Alc2GdcI_4ju48uWbugHa1LGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9915e2bfef.mp4?token=QCBv9NB3PrbsmUuOldK1P88Q5fUxQZoRXp10QVhhROhdTS_y4g0xGNI-ly9uSCiAb2LrrGtVeN3LFZ7IoJ6LlH__Nuq0BNA4Dwz9ahkjZj3HrU5WeoolAmmFI3KcudL2GTLYXarj-pEk1mxzqsU27AJGzvwbWO-dErCBQxUIdsYP0M2id6-ePoXvvw8AKKdhf6XH-AgNvBASASMy7pGt2l33M6gP8YRmCcUfWqbo8yUs8HDqmEzSpSJ1W2dSz-VuJflKzPw1ZcdGXOMuO4lY0QM990HPaQr1Jlf-HNsyqmbKKhBeOZqY2TFc3AFB7Alc2GdcI_4ju48uWbugHa1LGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پودر شدن موشلی ۹۰ روزه شد
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/12835" target="_blank">📅 09:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12834">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">https://t.me/boost/withyashar  بوست داره میریزههههه</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12834" target="_blank">📅 00:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12833">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست داره میریزههههه</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/12833" target="_blank">📅 00:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12832">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دیکتاتور مهربون ردبول رو امشب میزنی یا فرداشب؟
👀</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/12832" target="_blank">📅 00:09 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
