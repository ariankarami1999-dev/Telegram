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
<img src="https://cdn4.telesco.pe/file/pfygaUdBuvQ6CiXNAr-NW02XQ9To7WDc2bTmTs86RJwWSe5RgAxDjE8i7GPbmdLnaG3T42helf7ZYyt47ojMTTLjCYAc7VfPv7kxGrvhWN2Wzr7nkPFdWYETbFbojHZ4KX-HRCjDFGGI_Nh37-OK8nT6QRCXZsbib_fQL4bFo7Jcv_CGw6pkai9Wr9mOSHlX5ksDUrsR9M5iSdU1NClmgr2X3M0Hk4c_Z1GgS96kY4DNZJ90vN8zGgyp__KGR0M6BiVK2mvlGGWsxMYkX2q2OIF4KCf6dKesq9Z87tmS_vD9svWHk98MYp-REenG21IPhNWztB-2pD8NCYVFPP-7lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 337K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 15:31:33</div>
<hr>

<div class="tg-post" id="msg-16399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=JqOyo9C4rVEvpZkxRWgS9Ny_cED4UUyHEzJjjzG-TrBEZKChjzRqaEF9mF4UCDCvaY4LEFN30e9pfcVv4xKAj-Yh6kzvSiGMPSQq0Yr0gldveBxVfls6gcLK4429bah5wOdMa0i1phN7p6l821o3tyyYLRn-U1zc7GehmyxmN2FvHSKAxsbC6K46y-zqbcTTMBGjHfl8jgkEABsXW-jJzcBOWBf9SMYNtF2OqqpzJtyaQunqiJA_8z4VJE5b3KgADT6FvTgLR5_1ieZ7QvigMh9sCVSA_iHummF1lPT1ahZLlGPr-pWT-NweMT-YRV2hymYWIpDq0mPQnYQj4XzyMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=JqOyo9C4rVEvpZkxRWgS9Ny_cED4UUyHEzJjjzG-TrBEZKChjzRqaEF9mF4UCDCvaY4LEFN30e9pfcVv4xKAj-Yh6kzvSiGMPSQq0Yr0gldveBxVfls6gcLK4429bah5wOdMa0i1phN7p6l821o3tyyYLRn-U1zc7GehmyxmN2FvHSKAxsbC6K46y-zqbcTTMBGjHfl8jgkEABsXW-jJzcBOWBf9SMYNtF2OqqpzJtyaQunqiJA_8z4VJE5b3KgADT6FvTgLR5_1ieZ7QvigMh9sCVSA_iHummF1lPT1ahZLlGPr-pWT-NweMT-YRV2hymYWIpDq0mPQnYQj4XzyMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم
@withyashar</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/withyashar/16399" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">محمد نعیم جُندیه، رئیس امنیت نظامی گردان شجاعیه حماس توسط ارتش اسرائیل کشته شد
@withyashar</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/withyashar/16398" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">واشنگتن پست : مقام های آمریکایی فاش کردند اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
واشنگتن برخی طرح‌های اسرائیل برای ترور مقام‌های ارشد ایرانی مثل عراقچی و قالیباف را متوقف کرده است.
در این گزارش آمده اسرائیل به دنبال براندازی نظام ایران بوده، اما آمریکا به این نتیجه رسیده که چنین هدفی از طریق جنگ عملی نیست و به‌جای آن تمرکز را روی تضعیف توان نظامی و دریایی ایران گذاشته است.
همچنین ادعا شده «ترور لاریجانی» نقطه عطف این اختلافات بوده، چون آمریکا به دنبال فردی برای تعامل در داخل ایران بود و با حذف او این گزینه از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/withyashar/16397" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد @withyashar
🚨</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/withyashar/16396" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/16395" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7lZdeQKmaA-MVN6zyUiAOIQmk0g24iRcliZXKK__ZmAr45p7LnTBXLrzwz655W8a-ujXuBCDfp2DUGHZECZiHxm0HK865zseda9cqUgjJnPuwIxuxU2ulJLfOq9r9QA9iohcDirVjNwD6D10-kdAp0sE3vAlbTY0LygxRKMBP0mshrLhjWd37HPooX1Epmdz4J4DXvBKILZIpg6uJt7njq-QeH6Yqqbeo-6A084DhrOJRAvi2pcDkJWGnorlMUvnpqc7x7zAXgHHVayGJ0q3dAGuqjaG8Lw36WYazX7v6eJ7rbzbvWHuOe-_ZFhRJraUvVhHXv06FX9wJzGBO2pCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار فروش آلت‌کوین‌ها به پایین‌ترین سطح در چند سال اخیر رسیده؛ به‌طوری که اختلاف بین خرید و فروش در آلت‌کوین‌ها (به‌جز BTC و ETH) به ضعیف‌ترین وضعیت چندساله خود رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/withyashar/16394" target="_blank">📅 14:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKqddCCMcxE-otCl2oNtqdSl9DraF438TQ7JoLYw8zJAr1ZQNqcFOzKvx4yq9yWtP0_bl-LrSN8qhbv6MwKoDWesl4bHvbasl18BdDx9xFWJAop88VWH0t_rZtFCjyBXRsFD-NSMOvnilRMLEmHwGgkp0bq_aLFKSDnugbwyvEUvwI7R27e6BRzFVgjNGRTtYE6E1c71rC8hCaz18X-S8hOktyla1p_gB7uRxVyucyoNcqsKyj97m1eWM8NsYVeDBUc7IHW-MOEMPZmjZ2wCe2FWav0HDYbfqhBsSMsZgtX53uBwlIC_dsZeHkhsMtcdEKgaJObPWuj5nD6YQslAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/16393" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/16392" target="_blank">📅 13:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">WarRoom with YASHAR
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16391" target="_blank">📅 13:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">1$ Tether 176,000 Toman
Brent oil = 71$
Gold = 4173$
BTC/USDT binance = 61,685$
@withyashar</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/16390" target="_blank">📅 13:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16389">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQ5naQPBCbaIcSsEjeQ5DGe6tt1VsfnnsgYc4eWslqfVkBR-ZdDERU90U_5P4JJJmlGP_gxGFHyVNEdm-df58LGOeBCkULnDmtShD1PZD39Cp3zhVN7LAa9Jf7_htvCef4Ry0tBn1rSfeytW0PrPW6fUcYGMxRbMQ0C_SBIeDYiHyOi-Kj74WefEoKlJH39K7Vd94-xl93Jf4nGKEV-I_6mVkzZx9cIn5U7sHfh28OEC_Ymo_vsZW-nTLptRX9KHQrQpMtPv_Pqwn_pmWcz2JxIY9cY8eYiY9PTqlkPsX2Brlh7MCBK2UNqGAwzWXW2ytM8_Cnj8SVF2Jz3ZHW-4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس از تفاوت تابوت محمدرضا شاه و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای  انگار پرچم عربستانه
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/16389" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16388">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فیلم مستند «جاسوسی از تهران» هم اکنون با زیرنویس فارسی
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/16388" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16387">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">۴ تن از نیروهای نیابتی جمهوری اسلامی عضو کتائب حزب‌الله توسط سرویس ضدتروریسم عراق (ICTS) در بغداد بازداشت شدند
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/16387" target="_blank">📅 12:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16386">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDwE16fpBV2nxlLTUJmeINNnk0nS7rWIOdQgcUUEbUY_OwRmGMHtZNNiCbKCXPsYmHkur8fToRtNM7CHIg3J48KzgoxOsZsOtiqekhe4_rM0ci8WMAOl6mrenthXqTLvD1DDQvI4XweMK64M9XXKM0_iYuuZgOlcurfo-zUM4sewfQDA1ldoMAjJ3jpkEAms0sF1hYCieF5PUJi9LFiX89QYs6c3FPlqWmCQnOjHtw9-LQJPMJ9rWZ5CtcQo_Se534DExHoPk7WsYueVMRNMYor7g6lE2bwBvTAuTyuHbsTKrXI_lTqMvm5vs5qEMZB3vHkLz4IBzrs8P7jZTFrUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رادان : یک بمب گذاری ناموفق در مصلی خمینی تهران شناسایی شد و خنثی کردیم
با برهم زنندگان امنیت تشییع جنازه بشدت برخورد خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/16386" target="_blank">📅 12:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16385">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پشت گوشتون رو دیدین، بیرون رفتن ما از جنوب لبنان رو هم میبینید. @withyashar بنیامین نتانیاهو: تا وقتی تهدید برطرف نشه ما از جنوب لبنان بیرون نمیریم.</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/16385" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16384">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgiY-HETiabVSbsD-3ML6Rratqg3A6JxSFnuNExY-RAXKn6UdUmK8rpa3WTGUapnAYBzq6IINtUuekg9mnxzsxTiuQ1dMAkEotAlr6KSiRHYaBGCZ049-9p2ze1j1f5XMidf5Lvq-BAepqdhPlsesvDnHa-UR70uddz2t_86JRkQgk9VbSfpHJHoOVtPRUHqiDiKzYUNLrV0PZhFWx-O5E6bbnGpT_e5EshaLS009JiOmn9YJ1LVYXlFj2y0_xwaQByIGyTm1bDy8J7hCeuZ0U44piwpNB3FUDU4BG-ILGFudxs87H8tiK2--1ajJBmC4dZFZybuPrgHtgqQPt79Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس تصاویر ماهواره‌ای به تاریخ 7 تیر 1405، آواربرداری و پاکسازی اغلب سازه‌های آسیب‌دیده در جنگ اخیر در حال اجرا است و برخی از آن‌ها کاملاً پاکسازی شده‌اند
هم‌چنین جزئیات موجود در تصاویر نشان می‌دهند که فعالیت‌های تولیدی در بخش‌های سالم این مرکز با شدت بالایی دنبال می‌شوند
@withyashar</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/16384" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16383">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کل تهران در زمان خاک‌سپاری رضا شاه (۱۷ اردیبهشت ۱۳۲۹) جمعیتی حدود ۵۵۰ تا ۵۸۰ هزار نفر داشت.
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16383" target="_blank">📅 10:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16382">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJIBQ8LL1ciTAqfIknnVkyRRUS00yKjk80LKLjk8x1l_8jruvrYPR8Nght7B-wRpdc-JmvTmnLMXPlEpAHLqbyN4hfpHJy5lflxXhqd-LKAaVhgVxGHVnXkB5xcjegaS2hG_9woSn-ZoqANTNlejyFRSgyaVICwUeb-3ciB2uv3UfiKKr2LK2-hqnHbUQyOO6zK3ScqYPcPB3LgTmzboC5X4HxmbDf1Btr2JK5Pg3Pia9umMLmWrK_ZjPDawYjqXukwJXWq7a7zEDYrQjlnHIuLqQUXIs8nd1b3yEXUimFXv4z2a_dx8m00lasiqCa3Jxq6aTzWMHpRF0IksTZo33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/16382" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16381">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس:
به دلیل تهدید مداوم وزیر دفاع اسرائیل به جنگ و ترور، ممکن است در دکترین هسته ای خود تجدید نظر کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/16381" target="_blank">📅 10:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16380">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZLCnQb2KRDReWKmM_1GJl7_8W7jJusiNd0nvVv-dekO_ZuBBalOq2gdVV0q1ZqXVBLHCsCunkvQ7gdlJEG4lB83k7O9Bp4ft-68TWznTecG-FXEs8LYy--sGpa53WU17914Gn6D9ImabNgCuDt6Or9GKdXuf0iDZRZMw4aQP8m9JyRoKcyIErWIJT9z7paWOLNY3uOAaFg_dKtI9DsCughuogr-HGaYkRhd4tLn4srDuCR9zPAOP-T68mclav2HD9PXANBwsaI7nCasAczhqNAasE4TN5-gKiNjiY7MlejM6yC8JlA63yEu6FEje2Ti33roBQRlp_jntu7UBodvmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادای مفلسی احمد مسعود
(فرزند احمد شاه مسعود) و هیئتی از افغانستان به تابوت علی خامنه ای
@withyashar</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/16380" target="_blank">📅 10:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16379">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/16379" target="_blank">📅 09:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16377">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ورود هیاتی از حشد الشعبی عراق  @withyashar چند نفر از‌ موساد حظور دارند ؟
😁</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/16377" target="_blank">📅 09:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16376">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ورود هیاتی از حشد الشعبی عراق
@withyashar
چند نفر از‌ موساد حظور دارند ؟
😁</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/16376" target="_blank">📅 09:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16375">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ: من به دنبال تغییر رژیم ایران نیستم
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/16375" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16374">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اتاق جنگ با یاشار : با توجه به داده ها به نظر میرسد کشتیهایی که از مسیر امن آمریکا در نزدیکی عمان رفت و آمد می کنند، نسبت به مسیری که جمهوری اسلامی تعیین کرده بیشتر است. @withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/16374" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16373">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=d89AWsGLfuvhXUDkcA7yJHZB1lW9uDtBeX0ViUbvwoBXxyoJt8T-q9LpW8L0rn4lIEgkxSEQzK30EhmzsygcTJuzeNBqSgcYTgcYuwWlHf7huE7af22b0xohHZUZw8W2w1DQ56rnVmji2CzeGPTCb1JLidRGpW0mLpYrOw_hZREM2mkmiU4QKbUzrQnyHfkU0awba1MFeqyoygpJfWRbdya3N92xRqOrNe8JzJiFr2EEvRB1VzzccuKpoE7j6ADQGjvdNWaHe92yrsXNujHPFVdiwYGSb5oHKUgDmVYmG3a7x__i76RLPPKqdQLBN_WwVYOMIhoOZm7mVZgnd9Dz84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=d89AWsGLfuvhXUDkcA7yJHZB1lW9uDtBeX0ViUbvwoBXxyoJt8T-q9LpW8L0rn4lIEgkxSEQzK30EhmzsygcTJuzeNBqSgcYTgcYuwWlHf7huE7af22b0xohHZUZw8W2w1DQ56rnVmji2CzeGPTCb1JLidRGpW0mLpYrOw_hZREM2mkmiU4QKbUzrQnyHfkU0awba1MFeqyoygpJfWRbdya3N92xRqOrNe8JzJiFr2EEvRB1VzzccuKpoE7j6ADQGjvdNWaHe92yrsXNujHPFVdiwYGSb5oHKUgDmVYmG3a7x__i76RLPPKqdQLBN_WwVYOMIhoOZm7mVZgnd9Dz84WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان، چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست. @withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16373" target="_blank">📅 02:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16372">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDl0Z6DT1YwMJvv6C6y0GUNvU6mzJgYdD7uacOQ3mv0pbqb-XKmJcvBv66XSU9IVgrNfO-XjUxA7OpP8Svavfhb5N4Xp3iTFYUDS4KreWwdFMsKsJ50q0iK-VOdtpjbyxJLXTbzVPY_El218LsRvi2zVuWpfHB2Sesbm6QHnsUWFrQ4ZldVE7B1QnxcgzSFTIHveQ1wR5yWFVPVjUDc8zC8vj_lMo25-S8a9sQkPV2TpFp58WonPF3LrmeImdrDsH_ndEQunyCUsEfsubVUmWZigH3vWdHIqUVfj58ZkBVoefF8uipXwYvflZTwJ9muCCaW5yUGKQAIHm1PidhUC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان تجمع و عزاداری شدید نیروی هوایی آمریکا برای عظما
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16372" target="_blank">📅 02:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16371">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان،
چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست.
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16371" target="_blank">📅 02:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16370">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC7vS3AgLwSQ2y0k1TeOcBgRah_kDwhbIeK780UqjvxkVxfpLpmxnEsfhzezuCRYFIcKGH0pFXmqAXYxDLykD01TnkiZTBkT1ZC3iZrTrWQnTHm5xPRdJ1K49hkreoleqD3efqmaslGrBMQjDpEc2QkI1JoismPxMWND57FtAjxk5CCh6e84ZGSAoMcyEG6-2ZQzACac6mWs5TcZ0wQX2H7vxRLD22uS-f89fo5DicN2LyObsx2t1sNlYcgjXWqIUsK-KwZy3npaG0AR6SD3A-4gwP6F_kHgRk0WiqsqpELEnnQdTWDu1clJkj1uFdVzpE1q5lN7YqfvIybgc2xbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند. ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم. @withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16370" target="_blank">📅 02:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16369">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=qBNVfbQhh9YSDVb2iPy4ilPfocApyTJaio3oCEVRIvVBR8pmuHmXEflXj8Iv-0sGJmvdvgpWQHEsafwkBCk6D30C7EFF3OyOFsGzhtqhiuF9uOJBpGJCOW6oSCkYnTkNjM_XzkbsPZgj67H179eRkY40HTjefExcmcgb5GvqpLdYw1ymfDNSeq-1R5nLq4t7KWYYFQzksk2SHpyTNhOhHDumGNV8YhQhqj_sVaRf_Pg1kjL-f6q8okQEWQM5Wcek_6OivrIm9TPVBrAP9_g8szNN6DTep9w36w9q67TKKw2lSkL0DAFb-XqbOn1UvUOG8XdLCw5lyewfJYiLhdXcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=qBNVfbQhh9YSDVb2iPy4ilPfocApyTJaio3oCEVRIvVBR8pmuHmXEflXj8Iv-0sGJmvdvgpWQHEsafwkBCk6D30C7EFF3OyOFsGzhtqhiuF9uOJBpGJCOW6oSCkYnTkNjM_XzkbsPZgj67H179eRkY40HTjefExcmcgb5GvqpLdYw1ymfDNSeq-1R5nLq4t7KWYYFQzksk2SHpyTNhOhHDumGNV8YhQhqj_sVaRf_Pg1kjL-f6q8okQEWQM5Wcek_6OivrIm9TPVBrAP9_g8szNN6DTep9w36w9q67TKKw2lSkL0DAFb-XqbOn1UvUOG8XdLCw5lyewfJYiLhdXcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16369" target="_blank">📅 01:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16368">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=G6BTB-SJqWux4PXKg98r4G9sSeIcZaP90Bhu5rlmbVJI0hfEar3hmgJMb8E4fHfsXUlPe3eOI_uk2H_rjRBlDeJbbROutsgQukGgYykDFUxLHTKAXsATulyduvvni1DJQYh0zvmpheypyP7-UuSl6W8THeAr1BU31BKcr1kpvf6z7yggYMZXfzty3Q1hdSgrF39_jo4_pksqkYs_svnio_Fnj_O8duJpYleBKFfS0xSddu7Js2TeCj_opzzvPgkVBKRFbC3DUZhc3d4Kf2moVF-oeTlvxprT7bg702sSzM2UQ_qkLpbqO8BjyP-3uRat8fTyl2oDPV3sPnJ4tai4nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=G6BTB-SJqWux4PXKg98r4G9sSeIcZaP90Bhu5rlmbVJI0hfEar3hmgJMb8E4fHfsXUlPe3eOI_uk2H_rjRBlDeJbbROutsgQukGgYykDFUxLHTKAXsATulyduvvni1DJQYh0zvmpheypyP7-UuSl6W8THeAr1BU31BKcr1kpvf6z7yggYMZXfzty3Q1hdSgrF39_jo4_pksqkYs_svnio_Fnj_O8duJpYleBKFfS0xSddu7Js2TeCj_opzzvPgkVBKRFbC3DUZhc3d4Kf2moVF-oeTlvxprT7bg702sSzM2UQ_qkLpbqO8BjyP-3uRat8fTyl2oDPV3sPnJ4tai4nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو قبل از خواب ببینید تا پستای قبلی جمهوری اسلامی رو بشوره ببره.
@withyashar
🌟</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16368" target="_blank">📅 01:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16367">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
@withyashar
نسخه اصلی با زیرنویس انگلیسی و حجم کم تا بعد با زیرفارسی شو بزارم</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16367" target="_blank">📅 00:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16366">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=Z7ejCZZX53ty53X2T7hk43JUCBdi9UaREusMSXTyAPQi0PibjrKPtrpSM1EfLv-qxpV3uDnUSzIqmCRogbbJFIvorihl3GauFFYEbwMYc9MUFPgUzbK03XMO2VRd6uqyp2IrGTmZmpIofAolBP1qa253zqO1a0dBRk-97_77egHbQm0PqWdsKHWCh01x35SwLN7ZH9Lop-aju8Xp8qrf2wUD0U1J0-fGSk5MskfdKYuCOlrffYyIMzQ1UKkuPlSSjBoxQf-pU5QPPXG7jABqlblYM1BUTP9wtqMFpkm5Ety6pAHI2BhzxhrUcKNeRL951clEu8v1HdfTvMf6NOVUCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=Z7ejCZZX53ty53X2T7hk43JUCBdi9UaREusMSXTyAPQi0PibjrKPtrpSM1EfLv-qxpV3uDnUSzIqmCRogbbJFIvorihl3GauFFYEbwMYc9MUFPgUzbK03XMO2VRd6uqyp2IrGTmZmpIofAolBP1qa253zqO1a0dBRk-97_77egHbQm0PqWdsKHWCh01x35SwLN7ZH9Lop-aju8Xp8qrf2wUD0U1J0-fGSk5MskfdKYuCOlrffYyIMzQ1UKkuPlSSjBoxQf-pU5QPPXG7jABqlblYM1BUTP9wtqMFpkm5Ety6pAHI2BhzxhrUcKNeRL951clEu8v1HdfTvMf6NOVUCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یک مداح حکومتی:
ترامپ رو هلیکوپترش غیرت داشت، اونوقت رهبر رو زدن هنوز خاکش نکردیم.
چرا راستش رو نمیگید هسته‌ای رو دادید رفت؟ چرا نمیگید هر روز لبنان رو میزنن ولی بازم کاری نمیکنید.
۱۰۰ میلیارد دلار طلب داریم، بعد برای ۱۲ میلیارد دلار مارو کشوندن پای میز مذاکره، تازه نصفشم گفتن ذرت و سویا میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/16366" target="_blank">📅 00:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16365">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=jOBvRH7c1EzpEzPQOp2fCgfzDw5jdwAPRW97Q6xWHIPcxhLOpa3q1emZRfitZFEegqO8_kNsSJ6LP0o_fIruOkj650LC3bFZDQJeXZ1QTDcvWHPzZ0jtCUhNZ7ws3WxNiOKJArwxWANc8vGlqAVae2cigmz7GEVJDEzzWlH1AtEVS79O_-tMDGCClU1FxSlnNGtK7S2tC99g72ZAOB7f4jYMIQx8Qwsp27UKVSoqBgdKRBA_NxWfiYJRKGHP0dPvTQ7hwPYhkeQ5M8R8Q3CfKheYmkNLHWfXWhqFRsbN_rRWmdmBnoDR-o9DpFVyWuEq1rEXlMTgepxoM5yyflqQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=jOBvRH7c1EzpEzPQOp2fCgfzDw5jdwAPRW97Q6xWHIPcxhLOpa3q1emZRfitZFEegqO8_kNsSJ6LP0o_fIruOkj650LC3bFZDQJeXZ1QTDcvWHPzZ0jtCUhNZ7ws3WxNiOKJArwxWANc8vGlqAVae2cigmz7GEVJDEzzWlH1AtEVS79O_-tMDGCClU1FxSlnNGtK7S2tC99g72ZAOB7f4jYMIQx8Qwsp27UKVSoqBgdKRBA_NxWfiYJRKGHP0dPvTQ7hwPYhkeQ5M8R8Q3CfKheYmkNLHWfXWhqFRsbN_rRWmdmBnoDR-o9DpFVyWuEq1rEXlMTgepxoM5yyflqQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت
دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند
@withyashar</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/16365" target="_blank">📅 00:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16364">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">لحظه ورود تابوت علی خامنه ای به مراسم
،
امشب در حسینیه عمام خمینی
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16364" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16363">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : خشک خشک ، از دیدن بشقاب پرنده بگیر تا نرم باز‌ کردن تنگه هرمز
💥
کارای اداری یادتون نره ! برام بنویسین چند وقته منو دنبال میکنید ببینیم ترمیناتور شدید یا نه
😁
⁩
https://www.instagram.com/reel/DaTbNq0x1Pf/?igsh=cmx6bXhnYXB6aTN5</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16363" target="_blank">📅 23:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16362">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بلومبرگ:  ۵۸ میلیون بشکه نفت و میعانات ایران روی آب انباشته شده و ۹۰٪ این محموله‌ها مشتری یا مقصد نهایی ندارند.
با وجود تعلیق ۶۰ روزه تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خریدها محدود مانده است
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16362" target="_blank">📅 23:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16361">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz3MJjiQMeQelfD3KdkwT0K6pIzKEFM8MUpjIdPRWOz69t7JluQl-_i4_Yx_QOerwzbfc8Dv6wO2Ac9W-rdiNvpzg9JHyrTGJqtaA5VlD2NZsnfgekRJ_crHd2Dh-LFnMD-tkDTAbTp00f3qBZwmaGOF4k57VZ7r1gZIbdsZjF-uyXUwiZKl5UXmTNgef8u7gcnRarMptfcFuzZ0zUBs3obSfUgSsbnBaPHQX1Qp2QTv62rPIVpvKt-aN-FUPsvuwEMeTZv7ARwwxxOIfn318ag32A3iSdCogHEQdzTaVXOp9jASdtQsMXXlw8Y3PFp2JIEfeybJkVwSbwt4fe2rYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست جدید اتاق جنگ
💥
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/16361" target="_blank">📅 23:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16360">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مهران مدیری : با مرد ۳ هزار چهره که دارم میسازم باز به اوج برمیگردم
@withyashar
😐</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/16360" target="_blank">📅 23:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16359">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNkntL6n5Z6NM2Xm0L_vYR0xumdsLa5Ag6hdHhV8pFIsppA4gN5sjGAXw3phnEZdeW20i3TBaGmD3nBVWNagdG4qp0xP0XaPY-5Si6hq5cY7ismvmK8e3YK2c0v720zxVzvJiEOwyAR4W8rg6Sd1CQjjLIV1TMuakdgOGZQBEb4PBjf5hSsazFQ1ICJIH2omVnh82JLP5hlns5vTScm4rO3sbv_uO5WpQX2ufMzvIabphL0wq8RP7zcfauqz01Q4YhMMt1_EFVtmKFH6n_-yWx44tgQC-_Y-bIBlotYKalywLq6Hj7y92FuYRaEhWugVmhFsF5dPmVWz0BgW20Au4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های عبری در‌سالگرد ۱۰۰۰ روز پس از ۷ اکتبر : آنها بدون هیچ نشانه ای از حیات، در حالی که در آغوش یکدیگر در تخت خواب قرار داشتند، پیدا شدند. یک خانواده کامل که در تاریخ 7 اکتبر به قتل رسید.
ما آن را فراموش نخواهیم کرد و بخشش نخواهیم کرد.
💔
@withyashar
یاشار : اسرائیل درد مارو که ۱۸-۱۹ و کل این ۴۷ سال کشیدیم با تمام وجود درک میکنه و اینارو ول نمیکنه خواهید دید!</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16359" target="_blank">📅 22:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16358">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند. @withyashar…</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16358" target="_blank">📅 22:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16357">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16357" target="_blank">📅 22:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16356">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16356" target="_blank">📅 22:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16355">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ58fcbqIJYUH7XeZ2SMMzUGc-Y0fG13e6aPZFNqenx_1Nl6inklnQZkCOyh-uVt86QhYdBoqtn-OPRYvKNmBCENdhjApQOHc0H-OgBacyu_6x79buDgHRITTT3m18uPku8DfsTtthnc91D3KIwS3ssGwmLT9oHH6XjBk7a6ruFEsihfAcfhSxV1O9LZiG8LLyPrX_CXxeyeTHmqtH-_xrDwFMSup2MykpaQ3JCWXPvguMSaK4bvuF6337tQsYcXzmzrvkF_oG2Urswa5nczhoeAF7fYV2WZGMpRLCRcNH6Il6dD1XanrYva-0InJiApPMD6UAejUp1Hbw7S1vo58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت گوشتون رو دیدین، بیرون رفتن ما از جنوب لبنان رو هم میبینید.
@withyashar
بنیامین نتانیاهو: تا وقتی تهدید برطرف نشه ما از جنوب لبنان بیرون نمیریم.</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16355" target="_blank">📅 22:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16354">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBYVc7_uHCW8nMrfchSQy2R8vssVJwAS6jb6QEoPKcfursiqdw1UVaEO44ITgYOTwse47eDDtwkCxAwlhbPvS3fdaHmcTxdx754tao2TbHOWWtbqjXzefL2FwcbgB2glnQZBfYI8l1iJ_9Jgb_Qj1i5MEeJu8teD4u-pb3pE3jgIJj7nnAvyz840KdtgKMhWPMdgWOCTQQ7TAKeyyLlWZHmGLvTd0Q_VDJ-AO66NqTm8Ng_wvjGm-cEOdUcc0WyM5Tdi1XnPOljyfEMI1sBRG9RIHc-pEa39f1PZTHzjnA-RlKRpBhuWcOJIVSYnAa7AYHRu227PWu0e__fYXTFuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام صفحه مجتبی هم اکنون
من این توفیق را داشتم که پیکر ایشان را بعد از شهادت زیارت کنم؛ آنچه دیدم کوهی از صلابت بود.|  ۲۱/اسفند/۱۴۰۴
@withyashar
دروغ نمیگه تو اون دنیا بدش دیدن همو</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16354" target="_blank">📅 22:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16353">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزیر دفاع اسرائیل: ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود
@withyashar
🚨</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16353" target="_blank">📅 21:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16352">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7b14f43a.mp4?token=rdqJpCT-owmQicyScOl3a2MYCAlv5FijrwTJD5lTuHfvtxgTChEb_6U_L57x8r0kiDm4E_GzMrDfWZFt4zaWAqBcJju07xmwcoaxQla0RkgNdVjgzDpysdOofQ3-GcQUyFnD2Q_KYVly5Jp8fr-fFA5CQE47ZcpeKYeTQ-lQQExDB-x75V2mNiR949n1aCF7uFjD3JY7NgGWYw_6zc_ElPMWn5IUsUn6jfU1wti9VAHdpZ2HlitSXGuWWHMSz6e8VZKMrh5iLd_OVeqzlcBtkdtwkp1atIe9ggBjWK3ufz3DY7bZZaQcmraohXOEPT7p83JmuXUbj_S2XICtOxo8FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7b14f43a.mp4?token=rdqJpCT-owmQicyScOl3a2MYCAlv5FijrwTJD5lTuHfvtxgTChEb_6U_L57x8r0kiDm4E_GzMrDfWZFt4zaWAqBcJju07xmwcoaxQla0RkgNdVjgzDpysdOofQ3-GcQUyFnD2Q_KYVly5Jp8fr-fFA5CQE47ZcpeKYeTQ-lQQExDB-x75V2mNiR949n1aCF7uFjD3JY7NgGWYw_6zc_ElPMWn5IUsUn6jfU1wti9VAHdpZ2HlitSXGuWWHMSz6e8VZKMrh5iLd_OVeqzlcBtkdtwkp1atIe9ggBjWK3ufz3DY7bZZaQcmraohXOEPT7p83JmuXUbj_S2XICtOxo8FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه 14 اسرائیل قراره سه‌شنبه و چهارشنبه، 16 و 17 تیر مصاحبه ای که با جاسوس های موساد و شاباک تو سپاه کرده پخش کنه
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/16352" target="_blank">📅 20:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16351">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کامنت جدیدم برای ترامپ. حتماً فقط همین کامنت را لایک و ریپلای کنید. میتوانید با اد استوری ( با نگهداشتن روی  کامنت)، انتشار بیشتری دهید.  https://www.instagram.com/reel/DaSrqH3NjVK/?comment_id=18333946015271080  ترجمه : آقای رئیس‌جمهور،  بسیاری از ایرانیان…</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16351" target="_blank">📅 20:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16350">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نماینده آمریکا در شورای امنیت: اجازه نخواهیم داد هیچ عوارضی بر تنگه هرمز تحمیل شود
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16350" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16349">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPKNymxkGEOY38z8q6owFNX6o6LEtWb1kDiqidDfQ0zNDv4KVdEukPoKpqOIto7BW5ifVuN9QQhDxk22YEXTdmwpEghKWU0aM9ZB7f1WfEn1G4VyuUbCHlRCoR37QHJk-j_eytP5pLqTBFwZlDwqyTeyBAEYxCNubN3fcnXplW1pKz12LxdBkra4f9_GpYA19AmtmXT4xJTgx5FvTYwEF5py_byAkLYc74bcK-4umksu0f-QSfq8Hs-4VikyBzfIZ15fxyRTzYfSJC0dVQB-RXhckNfA64SyBYUxn2d1aAIaeZ59SO9d1hOkSYeuNXKfsvKFuVh94s7b7x02JIzuIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحیدی؛ فرمانده کل سپاه پاسداران برای اولین بار بعد از جنگ رویت شد. @withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16349" target="_blank">📅 19:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16348">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quQUAMfUUXsWekT_t6ClxAWDMtQ5h-mGvdc0-X8u59IJoxMN1vMZaDtRlC6tGxcc3r5xZoACFZmE5lFwAacyVk8mI8xJQY561cNlkIszapM7echp0XCOId0DV2J2GYjPyYjcGSowjhH2rHyUvIXoCegD7G42MCtBRdyOg_ipd0FC5w11bQQ08ldrJOiC4VAHglYTsbn5TxYYI7enar3fFq0HsGOwof3sLiUkBAD5jlnQYd7FeH_BQRI2I00m7kzv39tfatnmFUbV4da5DqpSzE8h1-D8Qq6rcItBQz3xml0zakqh-vkKhZxDkH60qVeWIpevcbIIbRBHaIeBLbFfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحیدی؛ فرمانده کل سپاه پاسداران برای اولین بار بعد از جنگ رویت شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16348" target="_blank">📅 19:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16347">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">طبق گزارش ها برخی از مقامات ارشد سیاسی و نمایندگان پارلمان عراق از کشور به صورت پنهانی فرار کردند.
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/16347" target="_blank">📅 19:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16346">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وال استریت ژورنال: ایالات متحده به جمهوری اسلامی گفته است ما بخشی از وجوه مسدود شده را آزاد خواهیم کرد، اگر شما از دریافت عوارض در تنگه هرمز صرف نظر کنید. در حال حاضر، تهران این پیشنهاد را رد کرده است
﻿
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/16346" target="_blank">📅 19:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16345">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش ها از استقرار گسترده نیروهای پیاده نظام و توپخانه ایران در مرز با اقلیم کردستان، عراق.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16345" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16344">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش درگیری در مهاباد @withyashar
🚨</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/16344" target="_blank">📅 18:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16343">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جان‌باختن شش عضو تشکیلات مخفی حزب دموکرات در کمین سپاه پاسداران در پیرانشهر
بر اساس بیانیه منتشرشده از سوی حدکا، این درگیری در ساعات پایانی شب چهارشنبه ۱۰ تیرماه ۱۴۰۵، در حوالی روستای قزقپان، در سه کیلومتری پیرانشهر رخ داده است. این نیروها هنگام انجام یک مأموریت تشکیلاتی و سیاسی، در کمین برنامه‌ریزی‌شده و سنگین نیروهای سپاه پاسداران قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16343" target="_blank">📅 18:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16342">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پزشکیان: کشته شدن علی خامنه ای آغاز فصلی نوین در جمهوری اسلامی است
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16342" target="_blank">📅 18:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16341">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش درگیری در مهاباد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16341" target="_blank">📅 18:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16340">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این ادعا که «سرکرده حزب دموکرات کردستان به آمریکا گفته در صورت حمله به ایران، ارومیه و آذربایجان غربی به ما داده شود» کاملاً بی‌اساس و فاقد هرگونه منبع معتبر و فیک نیوز است
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/16340" target="_blank">📅 18:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16339">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">روزنامه بریتانیایی ایندیپندنت : لطف‌الله کاظم افراسیابی شهروند ایرانی-آمریکایی مقیم ماساچوست ، استاد سابق علوم سیاسی که در جریان تبادل زندانیان میان ایران و آمریکا مورد عفو قرار گرفته بود
به دلیل رد شدن گل ایران در جام جهانی شکایت ۱ میلیارد دلاری علیه فیفا طرح کرد
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/16339" target="_blank">📅 18:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16338">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/16338" target="_blank">📅 17:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16337">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/16337" target="_blank">📅 17:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16336">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آبدانان</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16336" target="_blank">📅 17:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16335">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کامنت جدیدم برای ترامپ. حتماً فقط همین کامنت را لایک و ریپلای کنید. میتوانید با اد استوری ( با نگهداشتن روی  کامنت)، انتشار بیشتری دهید.
https://www.instagram.com/reel/DaSrqH3NjVK/?comment_id=18333946015271080
ترجمه :
آقای رئیس‌جمهور،
بسیاری از ایرانیان بر این باورند که صلح و ثبات پایدار تنها پس از پایان حکومت کنونی امکان‌پذیر خواهد بود. از شما با احترام درخواست می‌کنیم هنگام تصمیم‌گیری، این چند نکته را در نظر داشته باشید:
مردم ایران
گرسنه نیستند
(لطفاً به ویدئوی آبادان مراجعه کنید).
بسیاری از ایرانیان از شاهزاده رضا پهلوی به‌عنوان شخصیتی وحدت‌بخش برای یک دوران گذار مسالمت‌آمیز حمایت می‌کنند.
مهم‌ترین اولویت ملی ما، ایرانی آزاد، دموکراتیک و با تمامیت ارضی کامل است. حتی یک سانتی‌متر از خاک میهن ما نباید مورد خدشه قرار گیرد.
لطفاً با آزادسازی منابع مالی یا توافق‌هایی که موجب تقویت این رژیم شود، به آن کمک نکنید.
از توجه مستمر شما به مردم ایران سپاسگزاریم. ما به آینده‌ای بهتر امیدواریم و از تلاش‌ها و حمایت‌های شما قدردانی می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16335" target="_blank">📅 17:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16334">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وال‌استریت ژورنال: در یک تغییر راهبردی مهم، فرماندهی مرکزی ایالات متحده (CENTCOM) در حال بررسی جدی انتقال بخشی از سامانه‌ها و زیرساخت‌های عملیاتی نظامی خود از برخی کشورهای حوزه خلیج فارس به اسرائیل است.
بر اساس این گزارش، منطقه صحرای نقب  به‌عنوان گزینه اصلی برای استقرار این سامانه‌ها در نظر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16334" target="_blank">📅 16:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16333">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استاندار تهران: تمام تلاش ما اینه که مراسم تشییع رهبر بدون تلفات به پایان برسه.
@withyashar
😐</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16333" target="_blank">📅 16:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16332">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ در تروث : ایالات متحده بیشتر از هر کشور دیگری برای ناتو هزینه می‌کند، و این هزینه بسیار زیاد است، بدون اینکه هیچ سودی از آن ببرد:
آمریکا - ۹۹۹ میلیارد دلار، بریتانیا - ۹۰.۵ میلیارد دلار، فرانسه - ۶۶.۵ میلیارد دلار، ایتالیا - ۴۸.۸ میلیارد دلار، لهستان - ۴۴.۳ میلیارد دلار. سایر کشورها، از جمله آلمان، بسیار کمتر هستند. (۲۰۱۴–۲۰۲۵) مضحک است!
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16332" target="_blank">📅 15:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16331">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دریاسالار برد کوپر(فرمانده سنتکام): امروز، با افتخار از سربازان و ملوانان آمریکایی که به یک واحد مشترک ضد پهپاد (C-UAS) در بحرین منصوب شده بودند، به خاطر عملکرد استثنایی آنها در سرنگونی ۱۴ پهپاد تهاجمی یک طرفه جمهوری اسلامی در چند هفته گذشته، قدردانی کردم.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/16331" target="_blank">📅 15:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16330">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏دبیر کل حزب دموکرات کردستان ایران ، مصطفی هجری گفته: ‏حمله زمینی به ⁧ ایران⁩ مطرح است اما پیشروی تا تهران در دستور کار  نیست، اگر شرایط مهیا شود تا ارومیه پیشروی خواهیم کرد @withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16330" target="_blank">📅 15:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16329">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏دبیر کل حزب دموکرات کردستان ایران ، مصطفی هجری گفته:
‏حمله زمینی به ⁧ ایران⁩ مطرح است اما پیشروی تا تهران در دستور کار  نیست، اگر شرایط مهیا شود تا ارومیه پیشروی خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/16329" target="_blank">📅 15:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16328">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال ۱۴ : منابع مستقر در قطر گزارش می‌دهند که ایران در جریان مذاکرات غیرمستقیم و مهم این هفته با ایالات متحده در دوحه، تضمین‌های امنیتی محکمی دریافت کرده است و تضمین می‌دهد که مقامات و فرماندهان ارشد نظامی این کشور در مراسم تشییع جنازه آیت‌الله علی خامنه‌ای، رهبر فقید ایران، هدف قرار نگیرند.
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/16328" target="_blank">📅 15:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16327">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الحدث : پس از ۱۲۵ روز از کشته شدنش.. ترتیبات استثنایی برای «تشییع جنازه خامنه‌ای»
@withyashat</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16327" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16326">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الحدث : دور بعدی مذاکرات هفته آینده با حضور عراقچی و قالیباف در  در بورگن اشتوک سوئیس براگزار خواهد شد
@withyashar
العربیه: دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه برگزار خواهد شد</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16326" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16325">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cdb8cfe8.mp4?token=cZbSz_bDEET7KoNuPGgvItH-bskz6EMkxZTqnKgRTxNW2Pp5tzRZaDpdbHV-6k6-MDB8vzDWwtnc5UsYaweU4VuJGgQJD4LuPquLy6eQ4vYSNWGD2-5DvPpXYvjMeRPr3U85jwGqdChcHCtEoZFEDs2uBfv8vyQ983oP7-wuY3d_NuE3OFcysLvi8BOIyfRcT2I-wxqxsSZawIvmbTWvVaCxcgZqmwFN1typVBvNR48Wd8AISyMW-dQaJvl44Hesgrn9oeC83n2WG5_cBY4ZwY4PcIwj1hmLGB03zb8bt3Rgu91LaemA6r8K1qTkXEHGXz8U_9q8BiTnsdjCNk5_zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cdb8cfe8.mp4?token=cZbSz_bDEET7KoNuPGgvItH-bskz6EMkxZTqnKgRTxNW2Pp5tzRZaDpdbHV-6k6-MDB8vzDWwtnc5UsYaweU4VuJGgQJD4LuPquLy6eQ4vYSNWGD2-5DvPpXYvjMeRPr3U85jwGqdChcHCtEoZFEDs2uBfv8vyQ983oP7-wuY3d_NuE3OFcysLvi8BOIyfRcT2I-wxqxsSZawIvmbTWvVaCxcgZqmwFN1typVBvNR48Wd8AISyMW-dQaJvl44Hesgrn9oeC83n2WG5_cBY4ZwY4PcIwj1hmLGB03zb8bt3Rgu91LaemA6r8K1qTkXEHGXz8U_9q8BiTnsdjCNk5_zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : با توجه به داده ها به نظر میرسد کشتیهایی که از مسیر امن آمریکا در نزدیکی عمان رفت و آمد می کنند، نسبت به مسیری که جمهوری اسلامی تعیین کرده بیشتر است.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16325" target="_blank">📅 13:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16324">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بلومبرگ:جمهوری اسلامی ایران کنترل مؤثر خود بر تنگه هرمز را از دست داده است.مقام آمریکایی اعلام کرد حمایت نظامی آمریکا و کمک به احیای جریان نفت و تجارت از تنگه هرمز در هفته‌های اخیر به بیش از ۱۰ میلیون بشکه در روز افزایش یافته است.
این افزایش ایران را غافلگیر کرده، توانایی آن برای کنترل ترافیک را محدود و به حملات اخیر اطراف تنگه کمک کرده است.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/16324" target="_blank">📅 13:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16323">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">غضنفری نماینده مجلس :
یک کودتا علیه رهبری مجتبی خامنه ای در جریان هست
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16323" target="_blank">📅 13:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16322">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امروز صبح، علی عبداللهی، فرمانده "خاتم‌الانبیای" (فرماندهی عملیات مشترک نیروهای مسلح ایران)، هشدار صریحی به اسرائیل و آمریکا داد و از "هرگونه محاسبات اشتباه" در طول مراسم عزاداری خبر داد. او گفت که این اقدام، "واکنش‌های شدید و ناخوشایندی" از سوی نیروهای امنیتی ایران به دنبال خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16322" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16321">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وقتی یک ماه پیش من گفتم در روابط عربستان و آمریکا تنش جدی ایجاد شده ، یک اینفلوئنسر تندرو سلطنت‌طلب که شبیه ته نون باگت است، حمله سختی به من کرد.</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/16321" target="_blank">📅 12:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16320">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است @withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/16320" target="_blank">📅 12:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16319">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16319" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16318">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک منبع عبری : سقوط هلیکوپتر روز گذشته آمریکا توسط ایران بود
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/16318" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16317">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو: ممکن است جنگجویان کُرد ،حملات خود را به غرب و شمال غرب ایران امشب یا شب های بعد آغاز کنند.‌‌‌‌
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16317" target="_blank">📅 12:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16316">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بعد از حمله به بیت، اعلام کردن منصوره خجسته باقرزاده، همسر خامنه‌ای کشته شده.
اما بعد از اینکه مجتبی پیام تسلیت داد و یادش رفت اسم مادرشو بیاره، خبرگزاری‌ها تکذیب کردن و گفتن زندس!
الان دوباره گفتن کشته شده و قراره همزمان با علی خامنه‌ای، براش مراسم بگیرن.
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/16316" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16315">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn0yPU3n1qmWbaDPLfDEedX0FtPaqblw-4nm5t1lKzcl5SX5tTo1PDmfilxWQvMiRUKR2GzjPkADg7Xe6LwR99FMPmKNi3SHZFkRiaUJ_m7KgcGNxhISibHkOQ19TlnCt20pIbHmhETvVOCopGtFdf1ztVel47nym7KURmvd0u8VRfdx0EESPfpEXEC5EZ3u_X7FLZjFQVPDFiAZTIN9SYrZe4fKZQqaqCnU0t_JerOOg1E3na5bjS3P03Hmhmkjwh_dhzbJMA6FoiCLoWqATVWhXGTWRQtwSpsF1PGVobjOKpQdu-Gw7X5-LoKbj3g5VltnnYYSsBoZWSanYiAq4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار سقوط دستمزد و ارزش پول ملی ایران از سال ۲۰۱۰ تاکنون
حالا اگه درامدت دلاری بوده این نمودار برعکس میشه
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/16315" target="_blank">📅 12:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16314">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فرمانده  خاتم الانبیا، گفت : «تنگه هرمز زمین بازی آمریکا نیست، بلکه قلمرو حاکمیتی تهران است. همه نفتکش‌ها و کشتی‌های تجاری موظفند فقط از مسیری که تعیین کرده عبور کنند.» آنها بعداً تهدید کردند که «هرگونه عدم رعایت پروتکل‌های ناوبری ایران در تنگه هرمز با واکنش فوری و قاطع نیروهای مسلح مواجه خواهد شد. ادامه حضور جنگنده‌های آمریکایی بر فراز تنگه هرمز، امنیت کل منطقه را به خطر می‌اندازد.»
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/16314" target="_blank">📅 12:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16313">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">1$ Tether = 178,000 Toman
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/16313" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16312">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071529db45.mp4?token=LcbQs-DNfu3wB_o4UaBT3sETxzFlY1vslht_CVC8JV4C_vcJ6GpphFqEH0p-w_4u5HHXKlyKCRidRjZpBbRm17b82Q-buIF7GhB0xXyYOTxVzpJ-Mf-jbXF0mUQYYjpiz5joUwKnebzBER42M8cOlgdoB0-fwRXJWTJw6aNtlc6I_MtYPLv4pLhu0S9s7hoYi6dNUt5YWpqlQ5Hw3ci_3es1r9quSUZrAScCI1x-DWVCnxPe6eJVWHRZgg3Qxa3zVjabAClyxlWIZaFMR7m5I__dn67PSQac7iyw803YG6PCcj-Vpe4HKqiAMfh13uqFWnfLZ1AxI88ep9oP1FZJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071529db45.mp4?token=LcbQs-DNfu3wB_o4UaBT3sETxzFlY1vslht_CVC8JV4C_vcJ6GpphFqEH0p-w_4u5HHXKlyKCRidRjZpBbRm17b82Q-buIF7GhB0xXyYOTxVzpJ-Mf-jbXF0mUQYYjpiz5joUwKnebzBER42M8cOlgdoB0-fwRXJWTJw6aNtlc6I_MtYPLv4pLhu0S9s7hoYi6dNUt5YWpqlQ5Hw3ci_3es1r9quSUZrAScCI1x-DWVCnxPe6eJVWHRZgg3Qxa3zVjabAClyxlWIZaFMR7m5I__dn67PSQac7iyw803YG6PCcj-Vpe4HKqiAMfh13uqFWnfLZ1AxI88ep9oP1FZJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از خودروی حمل خامنه ای رونمایی شد
رئیس ستاد تشییع، وداع و نماز رهبر انقلاب در تهران: شکل کلی خودرو شبیه ضریح حرم امام رضا(ع) است.
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/16312" target="_blank">📅 11:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16311">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت
وزارت امور خارجه پاکستان اعلام کرد ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
طبق اعلام اسلام‌آباد، زمان برگزاری
نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر سابق ایران تعیین خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/16311" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16310">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک منبع آگاه:حال روحی آیت الله مجتبی خامنه ای مناسب شرکت در مراسم رهبر انقلاب نیست
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/16310" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16309">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634f71e520.mp4?token=lZVsnyG-7SGVa1tiZJfHB4bBLSilv1qsGIwkE6BWLQHS-MsSB1kXPgISZl3qNnZuvutmWW9zamiBO1-dMj-EEd06w1wQVGyccDAfPqT9qp2kEb1EZrKj7BjlyPjKDdEsWWfRTrp3PMsWeH0b_Ddao2RtyPDX_1RhuXHEbzvIY06nYnBpNiavIh8YfCYL786ONSjLPrNGQx5T5eh1cIpB8EfM6JQohxATtipu4VoI9Uqnjw9TZlHLFBbbFknY8VXbN2QM4YkTwrxokTGMS_LpZ337Pba_uMAJQ_tuJdYCNuA2v9w1cCbVgmym2z1D82ACvNr9F6aox5UjYf3blSi6MYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634f71e520.mp4?token=lZVsnyG-7SGVa1tiZJfHB4bBLSilv1qsGIwkE6BWLQHS-MsSB1kXPgISZl3qNnZuvutmWW9zamiBO1-dMj-EEd06w1wQVGyccDAfPqT9qp2kEb1EZrKj7BjlyPjKDdEsWWfRTrp3PMsWeH0b_Ddao2RtyPDX_1RhuXHEbzvIY06nYnBpNiavIh8YfCYL786ONSjLPrNGQx5T5eh1cIpB8EfM6JQohxATtipu4VoI9Uqnjw9TZlHLFBbbFknY8VXbN2QM4YkTwrxokTGMS_LpZ337Pba_uMAJQ_tuJdYCNuA2v9w1cCbVgmym2z1D82ACvNr9F6aox5UjYf3blSi6MYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌ پست جدید تروث ساخته شده با هوشمصنوعی دکتر می‌شود و بیماران مبتلا به «سندرم اختلال روانی ترامپ» را درمان می‌کند از جمله بیماران وی رابرت دنیرو نشان داده میشود
@withyashar
😂</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/16309" target="_blank">📅 11:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16308">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d47807c6.mp4?token=AeAKbg82d4e3lj2peLnUBodFflRPAF9zNIfZEls9JvX1dNJB0WlcEjzNRpCkjR5mw7huzdbcS5RuZE2qQLZaE4B0EvHuC7tKWCtcTx0LZ8nR0U1Rwpg_BzIbq6kMaHQu0gkywTaNWrM_wO-f5IoNDDUYLBFAwUV2xoBLQpNqO-DvtUcuxq9RulCvI_gJQOGCfXmo_JCXrkBA20Pbq9ceBNDHW-gVzC52PHTg9BHMgoqone7lRvGk3QxtpXyhM0gkUQkL3YpUdRXYVtyS8fcTMW-bI6hq1BeTvfbHITGFWZWvPwz13lFqR-Mdu8BOIDzX8V6hm-4wy3k28q3J0ZcgIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d47807c6.mp4?token=AeAKbg82d4e3lj2peLnUBodFflRPAF9zNIfZEls9JvX1dNJB0WlcEjzNRpCkjR5mw7huzdbcS5RuZE2qQLZaE4B0EvHuC7tKWCtcTx0LZ8nR0U1Rwpg_BzIbq6kMaHQu0gkywTaNWrM_wO-f5IoNDDUYLBFAwUV2xoBLQpNqO-DvtUcuxq9RulCvI_gJQOGCfXmo_JCXrkBA20Pbq9ceBNDHW-gVzC52PHTg9BHMgoqone7lRvGk3QxtpXyhM0gkUQkL3YpUdRXYVtyS8fcTMW-bI6hq1BeTvfbHITGFWZWvPwz13lFqR-Mdu8BOIDzX8V6hm-4wy3k28q3J0ZcgIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای از سایت هسته‌ای اصفهان نشان میدهد ورودی‌ها همچنان مسدود هستند و هیچ نشانه‌ای از فعالیت جدید دیده نمی‌شود. گفته می‌شود بخشی از مواد هسته‌ای غنی‌شده ایران در این مکان نگهداری می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/16308" target="_blank">📅 10:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16307">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سایت The War Zone با استناد به گزارش‌های محلی اعلام کرده است که هر شش بمب‌افکن استراتژیک B-52H Stratofortress حاضر در پایگاه RAF Fairford در بریتانیا، پایگاه را ترک کرده‌اند و احتمالاً به ایالات متحده بازگشته‌اند.
دوازده بمب‌افکن استراتژیک B-1B Lancer همچنان در پایگاه باقی مانده‌اند که این تعداد نسبت به هجده بمب‌افکن استراتژیک قبلی کاهش یافته است
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16307" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16306">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سقوط قیمت نفت برنت به کانال ۷۰ دلار
بعد از افزایش عبور از تنگه هرمز، قیمت هر بشکه نفت WTI به ۶۷ و هر بشکه نفت برنت نیز به ۷۰ دلار کاهش پیدا کرد
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/16306" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16305">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16305" target="_blank">📅 02:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16304">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گروه
حزب آزادی کردستان ( پاک ) مستقر در منطقه کردستان عراق نیز در بیانیه‌ای اعلام کرد که دفتر مرکزی آن در استان اربیل هدف موشک بالستیک قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16304" target="_blank">📅 01:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16303">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانال 14 اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/16303" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16302">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رسانه های رژیم : در ساعات گذشته دو مقر گروهک های تجزیه طلب متعلق به گروه‌های تروریستی در اقلیم کردستان عراق هدف حمله قرار گرفته‌اند.
بر این اساس، یکی از حملات مقر گروهک تروریستی دمکرات در منطقه کویه را هدف قرار داده و حمله دیگر نیز مقر گروهک تروریستی پاک در منطقه بالکایتی را مورد اصابت قرار داده است.
‎
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16302" target="_blank">📅 01:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16301">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سپاه: در پاسخ به اقدامات گروهک‌های کرد که منجر به کشته‌شدن سه نیروی فراجا شد، یکی از مقرهای این گروهک در منطقه دِیکله (شمال کردستان عراق) هدف حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16301" target="_blank">📅 01:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16300">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش هایی از ارسال تجهیزات گسترده ارتش جمهوری اسلامی به خصوص نیروی زمینی به منطقه غرب کشور
این حجم تجهیزات  بعد از زمان درگیری با داعش بی سابقه هست
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16300" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16299">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رویترز به نقل از منابع امنیتی عراق گزارش داد یک پهپاد حامل مواد منفجره به اردوگاه یک گروه مخالف کُرد ایرانی در شرق اربیل عراق برخورد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16299" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
