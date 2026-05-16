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
<img src="https://cdn4.telesco.pe/file/p55QLV82DLAinGhqLUeLVvV6oXyjZpjkLwteuGRTGmT3p5BKExY4JDulxVB5JwMjTB6291_r3kUgsq51ryBecyz6gtGhjAa-PuNUGUCzLyZIb1bOUyXidKCJSCyrxYTxttmLNLtvqnUl7wJOBAAnQ8MnEAi7jINfYD29COx4Af6BB5DEJAh2CJ8XSfdu6C9_IAjgDRZ1JYpOCGlmGkgrW1hCMAMErjKTNInhxa02UQYFgcoNSmSYKk2R7oE0KSHhauKDvho9d4Fi0qIdKUeNX19AkD0bJ2W4pPRgv8lDXc3MTni9G0Z8bm5UyCWo28SPfYxm0ERT8W9wyuWzGsR6FQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 146K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 16:31:47</div>
<hr>

<div class="tg-post" id="msg-75064">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بهترین نوک تاریخ لواندوفسکی از بارسا خداحافظی کرد.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/funhiphop/75064" target="_blank">📅 15:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75063">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKHzs2rStIT-GB7OXBpwsCLRjR8iY6EykiuRG2ABmx8tQX7ZeKDxLa621AQQ2E6FVCP2eQaDfyo7vMEFFe-VWsWfTgc3_jNeVKpPU3rr0pIFkeMTM-xlVE5d6dlYtlRjhOqo0JH7LwoYkcl9MsuVU6PSS4o6WKL-K4t9SgFKxuy_ET6ltXzVUtX42bK1wTZg6Lhqbq0uaRTZAGgdF4E7XWT1ygTFWkiCagaCI5pQJqbnOL9jFJQaFbyiDOnlzxY0wE9gtyxAQ_wnd8mB1Rq_bb3h9aAIH6QVNbhGCQX6zlkoYoU7fgy5jffxubvH85uS8COy0hoMg1ZGpo0WUz9vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین نوک تاریخ لواندوفسکی از بارسا خداحافظی کرد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/funhiphop/75063" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75062">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قبر بهار شاه‌مهری، جاویدنام ۱۷ ساله نیشابوری که در ۱۸ دی‌ماه جان خود را از دست داد، در روز تولدش توسط افراد ناشناس تخریب و شکسته شد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/funhiphop/75062" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75061">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در همین حین که رسانه های جمهوری‌خواه معتقدن آمریکا جنگ ایران رو دوباره از سر میگیره، رسانه های دموکرات میگن ترامپ دنبال یک راه خروج از جنگه و نمیخواد ادامه پیدا کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/funhiphop/75061" target="_blank">📅 14:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75060">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚀
فیلترشکن گیگی – دسترسی نامحدود به اینترنت! فقط 148 هزار تومان با تخفیف ویژه
🎇
⏰
فرصت محدود: فقط تا ۱۲ ساعت
✅
سرعت بالا و پایدار
✅
امنیت و حفظ حریم خصوصی
✅
نصب آسان روی تمامی دستگاه‌ها
👩‍💻
همین حالا اینترنت بدون محدودیت را تجربه کن! @karyabierbilturkey…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/funhiphop/75060" target="_blank">📅 13:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75059">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SILiZNulVWaGcMkPb-0oS8wnO5IcyF20VtHhoIn2GS4SSCzqserMYhuzE99vTu2GdVtAjkg0UbGSSI70qAm4LYgtdIXCaNmagDoEadZ2mTlU4AuQjWEpXQu3TKgeaCNbAOw301tPeePtADl6-uqJaGqfjty0ZpUJvoRymP-qDr9shlSy6eAwf1wUJt49qBR9CTMbV3lkQvwTnxIeS-s9k2SvObyfOaSJT0DaIiJHeFl_xYWZLsU58qCcPcPDHmYDj3e1LIVDS7HFfwx2R25IN0lyBGtqLo11U-yf2vvMbZr___PGxjx-u_L-VLxo_Smr5xjIDKN_Ac7rxbe879exaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فیلترشکن گیگی – دسترسی نامحدود به اینترنت!
فقط 148 هزار تومان با تخفیف ویژه
🎇
⏰
فرصت محدود: فقط تا ۱۲ ساعت
✅
سرعت بالا و پایدار
✅
امنیت و حفظ حریم خصوصی
✅
نصب آسان روی تمامی دستگاه‌ها
👩‍💻
همین حالا اینترنت بدون محدودیت را تجربه کن!
@karyabierbilturkey
کانال نت فانتوم
https://t.me/NetPhantomVPN</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/75059" target="_blank">📅 13:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75058">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بارسا داره یه رافینیا دیگه میخره
ژائو پدرو مهاجم چلسی</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/75058" target="_blank">📅 13:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75057">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0jSSvEvCVO1i5spzBJknvbcWc-1IwCQxjuktF_nt2JSJOROE1zQlk0SM05mgFga36F7B2-JGQsKdzehwUUw9CsELxLFXLDWG4stVL-9KwBIPd1vJ5VN2oHQex8x_KLyeGtQMAADq_MgXacYKaCL6DaW6Qf5oyQ43P4EiCfY_oj1kmjDlOi-hqZ1jA99Jt1JfLNIDUdUbOxgg8N5_347DUK21woSicZbObqR3s_wRXu0JP7oLX3CAHIVOD7Fei2DgfI65VkqLkdJ8V2yn5sSlBAU0ICy6KXYuj5zm3wa8NkI-L48RpKBbScaiYKWlXcmhouTYpmyWFX2fAK5EHUE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی محمدی مشاور قالیباف :
ای لشکر صاحب الزمان آماده باش
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/75057" target="_blank">📅 10:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75056">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رسانه‌های آمریکایی: ممکنه دوشنبه جنگ شروع شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/funhiphop/75056" target="_blank">📅 08:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جسی واترز، مجری فاکس نیوز:
ترامپ درحال آماده‌شدن برای دور جدیدی از حملات نظامی به ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/75055" target="_blank">📅 08:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">علی یک تنه ی پایگاه رو با سیگنالاش پولدار کرده دیگه شبا نمیرن تجمع بخاطر ۶ تومن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/75054" target="_blank">📅 07:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فعلا برای هر معامله ای چه خونه چه طلا چه دلار و کریپتو تا اخر این هفته دست نگه دارید ببینیم وضعیت چطور میشه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/75053" target="_blank">📅 06:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75052">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از ساعت ۵ تا ۶:۳۰، چندین پرواز در ارتفاع پست توسط چند جنگنده میگ۲۹ و F4 خودی در غرب تهران انجام شد، که صدای شدید آنها در بسیار مناطق غرب و مرکز تهران گزارش شده است
تا کنون دلیل این نوع پرواز در این زمان اعلام نشده است به احتمال زیاد شکار پهپاد متخاصم(انفجاری گزارش نشده است) یا پرواز آموزشی بوده است
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/75052" target="_blank">📅 06:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75046">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درس امروز اشخاصی که پرچم های
🇺🇸
🇮🇱
میزارن جلو اسمشون هیچ تفاوتی با اشخاصی که پرچم های
🇵🇸
🇱🇧
🇾🇪
میزارن جلو اسمشون ندارن هر دو از یک میزان ضریب هوشی برخوردار هستن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/funhiphop/75046" target="_blank">📅 04:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75045">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">درس امروز
اشخاصی که پرچم های
🇺🇸
🇮🇱
میزارن جلو اسمشون
هیچ تفاوتی با اشخاصی که پرچم های
🇵🇸
🇱🇧
🇾🇪
میزارن جلو اسمشون ندارن
هر دو از یک میزان ضریب هوشی برخوردار هستن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/75045" target="_blank">📅 04:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75044">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyn-0CHoqhxIEoppKaH9LzN5HsTQ54y2b5v_hvyBeGZfje6QJMvfSNccNPqhbAzaXq0IB-suL0EIa-3lw_vHa9CBXZ2NGLBNxYQ8agtQGAxlL11kdkgzm3WBvq0eW8_CdEaPCAcd_XyIJJ1RulPEQ9HM1RtgnMZ6XTgI2jb2IlxURT0Y-n_MnXijpDG1ZLJRZO9rQ8R2WAdWQiswz77G7kWOvXlmPj1nI81o_vU7VSXwocjo8cloWoljAQI-gkFXubh3AqyIpx85ERkUThWVzfKr81KRSkLiB504gkoHBqlR-tMjRC6T19ckX4mWhH04iQEbeyf9wqiLQr-oAxxAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجله
جدید تایم درباره دیدار ترامپ و شی جین‌پینگ
دنیا دیگه مثل قبل نیست که آمریکا تنها قدرت اصلی جهان باشه.
😊
🔜
الان چین خودش رو هم‌سطح آمریکا می‌بینه و این دیدار بیشتر شبیه گفت‌وگوی دو ابرقدرت بود تا مذاکره یک کشور قدرتمند با رقیب ضعیف‌تر.
حتی اگر توافق بزرگی هم امضا نشده باشد، خودِ تصویر کنار هم نشستن ترامپ و شی یک پیام مهم داشت:
دنیا دارد به سمت چندقطبی شدن می‌رود
.
👍
🤯
چین با قدرت اقتصادی، صنعت، فناوری و نفوذش در زنجیره تأمین جهانی کاری کرده که آمریکا هم مجبور شده با احتیاط بیشتری با آن برخورد کند.
خلاصه
آمریکا هنوز قدرتمندترین کشور دنیاست، اما دیگر تنها کشوری نیست که بتواند به‌تنهایی مسیر دنیا را تعیین کند.
👀
😎
مطالعه بیشتر >>
لینک
مرتبط با مجله اخیر تایم
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/funhiphop/75044" target="_blank">📅 04:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ببین اینقدر این هکرای چینی خطرناکن که آدم میمونه چی بگه جدیدا رباتای چینی زیرپستای فان هیپاپ (
💞
) میزارن.  @Funhiphop | reza</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/75042" target="_blank">📅 02:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75040">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ببین اینقدر این هکرای چینی خطرناکن که آدم میمونه چی بگه
جدیدا رباتای چینی زیرپستای فان هیپاپ (
💞
) میزارن.
@Funhiphop
| reza</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/75040" target="_blank">📅 02:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75039">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUyoKTqEsNtnyYH_GRKKq4irBh05tjef548IqXrSxTqMbNVA9OCZ0hwXbY5FuKTKidl1Ns__4CM03iRBkI-OTbO3u8KJZETfvcdA-sxbGZo2BZdyA-_DEha3mufKUuNZHXt_gx_IRmJlARmq9P_zj9HbyYA1BvesK3TQo1ojeDA6TGQhLBoVPEdxeb_JRtoW_Zpw8Wuz-yvWnIRvwAKVKsWdhujQkbzZnEs1qg--G49D9xkxiDXtpe2L7NrNUp-mxFdVs2pGWmjIv4gFK5M6IiCPBu1HQWn-HE2_vmzaRAH2dStxwKHQ9FV2wq7H68hT45l8AWOpdzdf0e4sXntmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید از آلبوم دریک حمایت کرد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/75039" target="_blank">📅 01:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75038">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دست مغول‌ها چهارتا آجر میدادن تا الان اسرائیلو نابود کرده بودن
😁</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/75038" target="_blank">📅 01:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75037">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تایوانم پوشش بدیم؟
@Funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/75037" target="_blank">📅 01:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75036">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مورینیو:
سری آخری که سرمربی رئال در الکلاسیکو بودم ۲۵ تا موقعیت پنالتی داشتیم هیچکدوم رو نگرفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/funhiphop/75036" target="_blank">📅 00:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75035">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مورینیو:
خیلی خوشحالم که این افتخار نصیبم شده که سرمربی وینیسیوس باشم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/funhiphop/75035" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75034">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فوری از فرید رومانو:
مورینیو سرمربی رئال شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/funhiphop/75034" target="_blank">📅 00:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75033">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">[ Fun HipHop ]
pinned «
رئال بازی خودشو برد و یک قدم دیگه به قهرمانی لالیگا نزدیک تر شد
🔥
🔥
@FunHipHop | Farid
»</div>
<div class="tg-footer"><a href="https://t.me/funhiphop/75033" target="_blank">📅 23:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75032">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCL3KGC2G9XO63gKImQ8iZuQ8joO5g2CVL0ozO4XJHllyvHBq5HhlXZXsTeJU_BhEE4hNsNgZx-mooht4Yr84yJQTSCapjnvrHS3iDVaUcENR7V61c2lo6Pu3qVJIZJ8TYteiml4FZknKzUQzfgeuI4uad6xWXOWfRPWrkRXLfH9ThGEdllqh2G2laimf03Go88vglL0FZ_IplE-8-g988LFxBl0-wXVNj60CoZur3iHL2MYnn7WdFbWPP_AZJT2xBsQV66-FRn_scR5zdeh5mRLIl62f9XJNARWlMakwe0oxpk1p7lBim9Hs7i4eVyJJn0mpGoAtsJCoGiAmc_SMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">د اتلتیک: راب دیپرینک هلندی که قرار بود یکی از داور های VAR جام جهانی باشه به دلیل تجاوز به یک پسر 17 ساله دستگیر شده و از لیست داوران جام جهانی هم خط خورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/funhiphop/75032" target="_blank">📅 22:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75031">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیایید بالا دلقک شدیم.
هادی چوپان: ما با زحمت و هزار دردسر به قله رسیدیم، نباید بازیچه دلقکان مجازی شویم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/75031" target="_blank">📅 22:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75030">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👑
دنبال کانفیگ استارلینک با قیمت پایین هستی؟
🫰
🚨
بدون‌ محدودیت‌ زمانی
❤
کاربر نامحدود
📞
بدون‌ قطعی و اختلال و کیفیت عالی
🧭
بدون ضریب
✉
دارای لینک ساب
👍
مناسب انواع بازی های آنلاین بدون لگ
🍿
مناسب یوتیوب، اینستاگرام و برنامه های حجم بالا
👑
یکبار خرید کنید و مشتری…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/funhiphop/75030" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75029">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6p1BFlKyx1LkkjXKLJqyNI-2IlvdhdkHviVxbwoqU134Oypu6mkPfWWgxqX8LmwSvdCaUS-90vNHimLzGg7ve0tsRvBQwu8r-Bb0kfJrqMFBv8_iQ095buJBciCnqXNvdnlafFR26yMz6bdHmp-lPHaM8DdAjosg0AOnGJtf0NeVZqOcDjBmKLM57mzWZ5zYxjp5kWL8lQFSOvNTMqXmD_se3NHRLb0y-BsxVglCRGKvUziQyAI4JT4exgHjs4CHE37Www8krj1hZiUdpsIdoUo170knzTeZfSdYW8SdulRwZLZuiRTd6kDtpuffDLHvXfNDlho2qjvUvVU5LbLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
دنبال کانفیگ استارلینک با قیمت پایین هستی؟
🫰
🚨
بدون‌ محدودیت‌ زمانی
❤
کاربر نامحدود
📞
بدون‌ قطعی و اختلال و کیفیت عالی
🧭
بدون ضریب
✉
دارای لینک ساب
👍
مناسب انواع بازی های آنلاین بدون لگ
🍿
مناسب یوتیوب، اینستاگرام و برنامه های حجم بالا
👑
یکبار خرید کنید و مشتری دائمی ما باشید
👇
👩‍💻
@ConfigRahNet</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/75029" target="_blank">📅 22:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd67VsawsojBitvGptVY6B9SISb-AObG_MWC61hiFU5J312lSHU5vB6U_-8DKMzPqgIJY45OdZO7cRJESNFacnUGmN7KbETgRVqygnjLWasu5U849OxUKp-GglzgbgNkiRr5PdBgsnXjLukKER5oPXe_CXfhT8zeUnuuRK0uhubE8Tncw_JlqAYl1-1VgdQYaKHN9-y8mDIteXSatEAW1L-MBQ-zz1ufMo4Bk2Q1g-EIx1-B6osnBtcvWyVqwerbCDjGruz6DWPrX6vFvMf8m306arTCeAUibFb7ay5qqOtVrTLXIVEuKHotNDDwtLlTjSD8B780m44-wa48wwZEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/funhiphop/75028" target="_blank">📅 21:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش های تایید نشده از ترور فرمانده حماس  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/75027" target="_blank">📅 21:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75026">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش های تایید نشده از ترور فرمانده حماس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/75026" target="_blank">📅 20:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75025">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امشب میزنن</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/75025" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75024">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تحلیلگر های بازار های مالی نسبت به
قیمت نفت
یک دید
صعودی
دارن و تو تحلیل هاشون
راجب جنگ دارن سناریو نویسی میکنن
که با از سرگیری درگیری های
خاورمیانه
قیمت نفت میتونه تا
بشکه ای 140 دلار
رشد داشته باشه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75024" target="_blank">📅 20:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75023">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نشد یبار یه سامسونگ بگیرم دستم داغ نکرده باشه</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/75023" target="_blank">📅 20:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75022">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-CkkhxtQUlxYRpxZIXGG5LxEfrd90RmN1eUSG89HFoFfTWt5AS9AEVw25B-o_8i131WfJ01ikRlHm3N646_c33fwoVaYIPLNYneqQOTBny33VscEHVkgqUvCs84QS94yj-H_h_fEaTBHjiNI_pFB8JlDTdnxuO6aBzfsmq6Zwu2uSemHkxKf2H5PFbwEuTX52ye1NYu8Rcu1WkgTXt4m7WiXKbWi2Y-Vnw3OC39Te51slidSA4P75E46Qk1N9OmuPRsZC9hE9bz38eumGtgeo70F3rqC0StjvSUEO0KMEWqlmVyA_GYUQjjgneo5QyO_0OgPzQwkMAla4Cqhnw1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا وضعیت اقتصادی خیلی خراب شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/75022" target="_blank">📅 20:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75021">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پشمام دریک میخواد برا تیم ملی ایران سرود بخونه</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/funhiphop/75021" target="_blank">📅 20:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75020">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cASMbRbrLL674ihkqSi6ZalS4L_-HQISqCUSPqj4mPhgQROP8aerReSlN7GH6GJcTmRlZpnxsWYLojypvp58QriE1ZCvS7dDP32P3luWGfv2pKrYvj949nHKbv-h3IkF6MNNytgTt7KytYHmRsstrzGfWDussI6x0_X1f_Snhnpt8suqecf6T_Td0ofDLAN6k2cO554MpST4Qubo_ryjN1l0nEzqsb3m9-VTgBnwsHxkbt93ntdF8ZtEIJKJkNbSbO-uWy01-UNpK1e9ZOJ0Sw6ogML4Bi-MiCyBiTZkfZmisBXehSFtR7q-4L4v9gKxK7soaua4pLmJuykNwW0bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/75020" target="_blank">📅 18:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75018">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت نیروهای مسلح فرانسه:
ناو هواپیمابر شارل دوگل در دریای عرب است و احتمالاً ماموریت آن بازگرداندن ناوبری در تنگه هرمز است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/funhiphop/75018" target="_blank">📅 18:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75017">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-msQ3FsW608Gst3CamI-fLtpa_2qr9wIe2qDVyfJBeuSb0ya8v6PaSB9zIHdn_lRe5S6XylJhTvlp1nKpcMgap5_kGtuijjbNv9yvA-wWC-H73J1op0YkKCH4BNB6ejdDQhHChav8ENNpx1cKlcRfGNsKmhRY8bCLJ2P6bA-0aj-4-6_TXnY7TPDfzLisyc5tnV7R4uGjLhbd9UMvHR7VQqsMvwCU0YOiCclMk9C4qs0z2ngHeeip_xnark6JtGToTQc_L7gNbi3lnpjQsYH24bnXH_2Xns1eTKWhhSvR4GCWvW2hizIUMmG8Zkpkh_z172NxjBnNsieeLkG5I55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: ICEMAN
🛑
Featured: Future, 21Savage  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/funhiphop/75017" target="_blank">📅 18:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75016">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTlCxohNsPwRiwI41GyECK6oOl1v7i5g6e9YD5YagmEwsKkjybqSZo6urBDhWVekNmM0UB5-RQRgv3FxZXylnlJO6vsfZsPjeYLBViQzdk8NHW6wuAPsA43ZjUjB3ew6EInYpFT1zRh2tQ83ldmlyAm_zCOZJ9DzarbYJ9mc07no8tw9A0ww3TXgAItl61NFAjNS54wBi_WaGX1L3qCXDznXlQWtBkng4GSsjG7DiGJRfOlJAO7i6bdp6wNqc3KL4T3XytSdYYg0r9cR2qmF30AWCB-bhBOI3A3qeHtEBxdtIqjcqU2E-cAvgMvhughQjCCemQ2nqYZvVRdHl-k7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیتکوین بگا رفت
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/75016" target="_blank">📅 17:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75012">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNbQOyXN7IE6gKQC9b49TOFsllchiTPbjmfismMAtp5U8pCg2k1OlUlTxk48KOT67Ta1pFnsIx-5e8fGxSfKd1f06mxUL7stWcDGnj6Yecs4TbFR_u5DdBHNN28fsYXjiv5S_Q7xOVauAvRZI4oVNbLWPchidl3FNdQD_sFWoaQY-VgA3Axb_6dXTCob9J9oZheqMuk82SQRyybcME7ogZhPU1zxeFzuZSOlyHBt1DOBCmaGHb_Q9CJdanAZtH7Eu5T6NHYKQ-W4hHcynjqnqoQosTplrnKiYdA5HkSDpY2qRy4jVQkEsa9PEl_0qkR4fGDIV01ErV0-A87YLxEFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک Little Birdie  "همه ی دختران عرب یک طوری با من رفتار میکنن که انگار شاهزاده فارسی ام"   @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/75012" target="_blank">📅 17:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75010">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">موزیک Little Birdie
"همه ی دختران عرب یک طوری با من رفتار میکنن که انگار شاهزاده فارسی ام"
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/75010" target="_blank">📅 17:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75008">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حس میکنم تو پکن ترامپو دزدیدن یه نسخه چینی‌اش رو ساختن فرستادن آمریکا</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/75008" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75007">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546804485e.mp4?token=E3XoVrOcx9GvN3qHBXnGblzdW-Nxee8pgQNQmnna0oZJ7AqnVz4tS41ly15gudWGsD3xF73HRH7eWbWgT6XpMOQ_MV0fTHTTpDq2XkbQ3XqKWNOqcX4Ki2RnQrhIVZmc3ysgBz17z3FwqGowFZnRZy0RankwGS0_ikxEHDhgQd1jbsPgjloy2523VnBFK4_M9CkBz4LR-hCiDIszh3OJWDM1xkQnopRnS6UtXEC0ZfSKjxbjMLP3zFe0c-HU1AI6EzTOVTwIfQWUP3nfdTGM7I2fMJQLtVZ5QX16L2IgjjvKnMw6p01uUPDghjYCx1g5aCnO6dmH6XuAcjkh5I6p9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546804485e.mp4?token=E3XoVrOcx9GvN3qHBXnGblzdW-Nxee8pgQNQmnna0oZJ7AqnVz4tS41ly15gudWGsD3xF73HRH7eWbWgT6XpMOQ_MV0fTHTTpDq2XkbQ3XqKWNOqcX4Ki2RnQrhIVZmc3ysgBz17z3FwqGowFZnRZy0RankwGS0_ikxEHDhgQd1jbsPgjloy2523VnBFK4_M9CkBz4LR-hCiDIszh3OJWDM1xkQnopRnS6UtXEC0ZfSKjxbjMLP3zFe0c-HU1AI6EzTOVTwIfQWUP3nfdTGM7I2fMJQLtVZ5QX16L2IgjjvKnMw6p01uUPDghjYCx1g5aCnO6dmH6XuAcjkh5I6p9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سؤال که آیا درباره حملات سایبری علیه آمریکا با شی جین‌پینگ حرف زده یا نه:
'آره، بهش گفتم. اونم شروع کرد درباره کارایی که ما تو چین کردیم حرف زدن.
خب می‌دونی، هر کاری اونا بکنن ما هم می‌کنیم. ما هم حسابی ازشون جاسوسی می‌کنیم.
بهش گفتم ما یه عالمه کارها علیه شما می‌کنیم که اصلاً خبر ندارین.'
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/75007" target="_blank">📅 16:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75006">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZy29Gdb97VwQ3YgRBU_lV8w6H-wqWfeQzCnN8MEHqYuYmAXn1VHPlyj3n4WLK7VIkeHLYjyz0n6_fHCn759V9LV8Q_ObKoIEm79gPx5Gj_v9IQLdjAa_WZgbErg9YrfJyKxRzCODwbNIli_-Npa5CXNARujoQigcndRCaG5C4JY2fyXxmUr05HzR301Z1gqXmrrYJ6xxgkesy6blkTBVTPmvd7Po3L3j5IjB34zFQ504-GUh588he3GPOQu6G1nrYrDXmG2pRyprPylBrJtAk6z0eUQo_bR5ZWCAeEaxJfDCt8zx4CQcjjMQHJn54rIuMmkI_3B-APg1TI2FHNBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتلو داره برا جام جهانی آماده میشه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/funhiphop/75006" target="_blank">📅 16:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75005">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📣
جشنواره تخفیف نت اسپید
📣
🗣️
پایین ترین قیمت و بالاترین کیفیت
🔄
⭐
اشتراک‌های حرفه‌ای شروع قیمت از ۲۴۹ با ضمانت پایداری
🔸
اشتراک‌های پایه شروع قیمت از ۱۵۰ بدون ضمانت پایداری همه طرح ها V2ray و با لینک ساب
🔗
بدون محدودیت تعداد کاربر
👻
بدون هیچ گونه ضریب
⭐️
…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/funhiphop/75005" target="_blank">📅 16:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75004">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snDCKsYrU1IKV-2abjk_WM61zTOCQrHnyRp9LQuA7Wk7Bdbi5S2k0WG8IDepmFVH_kOj4-djmcxzC70KLGnALZ4rYu5lT0K72PHaq3c2J7KFUBxWVyDHkHpiNqT7lDdFA1tJSzDIEEbMb890acptzqPbgsE1_U33Pc97L94K5c3nBwTRpvLsEpo1lGfRAW5KM7cmEMla9idj3ugQK49z6eeFU8gKyb2IwqM15pUDCRR_24dkA3-Qm2hpdFC8cDAt_tP-mL_m-C46vd8iyfSxfQQG7uXc5gldzKvtC38ezsuA3MOa1IeotEkWAnLBkBJHLH0aBgl56YitXnDPnrMXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
جشنواره تخفیف نت اسپید
📣
🗣️
پایین ترین قیمت و بالاترین کیفیت
🔄
⭐
اشتراک‌های حرفه‌ای شروع قیمت از ۲۴۹ با ضمانت پایداری
🔸
اشتراک‌های پایه شروع قیمت از ۱۵۰ بدون ضمانت پایداری
همه طرح ها V2ray و با لینک ساب
🔗
بدون محدودیت تعداد کاربر
👻
بدون هیچ گونه ضریب
⭐️
مناسب تمامی اپراتورها
💡
مناسب آیفون، اندروید، ویندوز، مک و...
🎮
خرید و دریافت کاملاً اتوماتیک از طریق:
🔒
@NETSPEEDxBot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75004" target="_blank">📅 16:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75002">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فریدریش مرز، صدراعظم آلمان:
من یک تماس تلفنی بسیار خوب با دونالد ترامپ در راه بازگشت از چین داشتم.
ما توافق کردیم:
ایران باید اکنون به میز مذاکره بیاید.
باید تنگه هرمز را باز کند.
نباید اجازه داده شود تهران سلاح هسته‌ای داشته باشد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/75002" target="_blank">📅 15:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75001">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیایید از تأثیرات محاصره تو بازار الکل بهتون بگم
آبجو کرونا تو بندر عباس شده ۲ تومن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/75001" target="_blank">📅 15:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75000">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خب دیگه ترامپ بسه. ادامه‌ی سخنان قصار دکتر عراقچی: بزرگ‌ترین مانع در روند دیپلماسی، پیام‌های متضادی‌ست که از آمریکا دریافت می‌کنیم که هر روز مواضع متفاوتی می‌گیرند. گاهی اوقات در یک روز دو پیغام کاملا متفاوت دریافت می‌کنیم. البته این وسط جنگ طلبانی وجود دارند…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/funhiphop/75000" target="_blank">📅 15:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74999">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f637359e4.mp4?token=ZdzL7EERV43m00gp-p4BZXYr7yuutcPbFY210t8hpEl__iAh71_hz5WuLiNYIicouzHsX1qDQDJXNyO1gGeb-XlOBRB_gP8qXkB94WaQRF5hBj9fHDPcxpP6bbNVHAp3sB6O7fvM9pYkUw1CsztO-l2GwEm7eIvhLm-yi08Lu98nD2naPLT_g2_8pLy6Q924wXJ1bZUNH6SXw39Z6q9ybGqZJilXkQMwK4gqgvA2_lkdmR3UdQsNjxwoCvLsvH9SiYv9CJJi0xomC4qjM8tyUhnOya9gGkJK-41Xd4zuBVbnPawyKhfb1IjDnZkeE75AV3YTA5pWOUh0pJwSaNgSWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f637359e4.mp4?token=ZdzL7EERV43m00gp-p4BZXYr7yuutcPbFY210t8hpEl__iAh71_hz5WuLiNYIicouzHsX1qDQDJXNyO1gGeb-XlOBRB_gP8qXkB94WaQRF5hBj9fHDPcxpP6bbNVHAp3sB6O7fvM9pYkUw1CsztO-l2GwEm7eIvhLm-yi08Lu98nD2naPLT_g2_8pLy6Q924wXJ1bZUNH6SXw39Z6q9ybGqZJilXkQMwK4gqgvA2_lkdmR3UdQsNjxwoCvLsvH9SiYv9CJJi0xomC4qjM8tyUhnOya9gGkJK-41Xd4zuBVbnPawyKhfb1IjDnZkeE75AV3YTA5pWOUh0pJwSaNgSWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب دیگه ترامپ بسه.
ادامه‌ی سخنان قصار دکتر عراقچی:
بزرگ‌ترین مانع در روند دیپلماسی، پیام‌های متضادی‌ست که از آمریکا دریافت می‌کنیم که هر روز مواضع متفاوتی می‌گیرند.
گاهی اوقات در یک روز دو پیغام کاملا متفاوت دریافت می‌کنیم.
البته این وسط جنگ طلبانی وجود دارند که می‌خواهند ایالات متحده را دوباره به یک جنگ دیگری بکشند.
ما عمیقا امیدوارم که آمریکا این اشتباه را دوباره تکرار نکند.
ما معتقدیم در نهایت این دیپلماسی است که پیروز خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/funhiphop/74999" target="_blank">📅 15:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74998">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: نیروی نظامی ایران رو از بین بردیم ولی شاید نیاز باشه که یک عملیات پاکسازی سبک انجام بدیم. وقتی به پیشنهاد ایران نگاه کردم، تو همون نگاه اول از جمله‌ی اولشون خوشم نیومد پس پیشنهاد رو دور انداختم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/funhiphop/74998" target="_blank">📅 15:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74997">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مارکو روبیو:
اگر ایرانی‌ها تصور می‌کنند که ما برای رسیدن به یک توافق امتیازاتی خواهيم داد، سخت در اشتباه هستند.
تحت هیچ شرایطی یک توافق بد با ایران را نخواهیم پذیرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/funhiphop/74997" target="_blank">📅 15:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74996">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: نیروی نظامی ایران رو از بین بردیم ولی شاید نیاز باشه که یک عملیات پاکسازی سبک انجام بدیم. وقتی به پیشنهاد ایران نگاه کردم، تو همون نگاه اول از جمله‌ی اولشون خوشم نیومد پس پیشنهاد رو دور انداختم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/74996" target="_blank">📅 14:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74995">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ:  آخرین چیزی که الان نیاز داریم یک جنگ است. در چند روز آینده درباره رفع تحریم‌های اعمال شده بر شرکت‌های نفتی چینی که نفت ایران را می‌خرند، تصمیم خواهم گرفت. اورانیوم غنی شده ایران می‌تواند به چین یا ایالات متحده تحویل داده شود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/74995" target="_blank">📅 14:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74994">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">طبق گزارش خبرنگار الجزیره، انگار واقعا اون ۵ تا شرط پایان جنگ فقط برا مصرف داخلی نبوده و جدی جدی اون ۵ تا شرط رو به صورت رسمی و مودبانه به آمریکا داده بودن و آمریکا هم به صورت رسمی و مودبانه یه تک تک اون شرط‌ها قهقهه زده.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/74994" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74993">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:  من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم، اما این باید یک تعهد واقعی باشد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/funhiphop/74993" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74992">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترلمپ:
هیچ پیشنهادی مبنی بر تعلیق ۲۰ ساله‌ هسته‌ای وجود ندارد،</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/funhiphop/74992" target="_blank">📅 14:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74991">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بخشی از ریلیز جدید رهبر جدید انقلاب: همه‌ی اقوام و اقشار ایران را در حفظ هویت، اصالت و استقلال خود و مبارزه با «ضحّاک‌» متجاوز، همدل و همراه و همساز هستند. از سوی دیگر مقاومت غیورانه و پیروزی افتخارآمیز در برابر تهاجم دیوسیرتان و شیاطین جهان، ملت را برای پاسداری…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/funhiphop/74991" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74990">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بِعَون‌ِ الله تعالی.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/74990" target="_blank">📅 14:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74989">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بیانیه جدید سید مجتبی خامنه به مناسبت روز بزرگداشت فردوسی زودی ریلیز می‌شه.
❤️
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/funhiphop/74989" target="_blank">📅 14:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74986">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بیانیه جدید سید مجتبی خامنه به مناسبت روز بزرگداشت فردوسی زودی ریلیز می‌شه.
❤️
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/funhiphop/74986" target="_blank">📅 13:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74985">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVAHID</strong></div>
<div class="tg-text">عشقم لبات مزه دموکراسی میده</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/funhiphop/74985" target="_blank">📅 13:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74984">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSeuW_kYo6Mk3zLOcYjLIB8ufJzGCKg-pPmoCkWZtU7Dp9Gc32Fw0FUDJyeIFZntIXvQpagGI8uC9aOS0mv3VQ0wdhiDr73jPm2N5DWNqA8gLpoZ3PAXgisBIwylTt2ttNHnHbm-z52utnppZOJqscH0_WQwMZebHyd7JTjPZaH8TGmP5hNn836zz4oqqL0goYJskucj-6l1-J9y4QUGzX_DSWvbuFY1i0JUFl2rOgUA9A1LP5fSEGZCbLLjVFCPW2ayFivyXLu4iELVxgVll9ZYV-fb8v-oefI5TR5oKt2h6WQfdfRcv8k5-GpBrUzMp5eyvjm843wSN4oSbO9TUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/74984" target="_blank">📅 13:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74983">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دکتر عباس عراقچی:
آتش‌بس بسیار شکننده است.
هیچ راه‌حل نظامی در مورد هر چیزی که به ایران مربوط باشد وجود ندارد.
ما فقط در صورتی به مذاکره علاقه‌مندیم که طرف مقابل جدی باشد.
ما به طور جد به آمریکایی‌ها اعتماد نداریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/74983" target="_blank">📅 13:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74981">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرهایی به گوش میرسه که ایلان ماسک با بریکس حساب می‌کنه پول جنده هارو.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/74981" target="_blank">📅 13:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74980">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd7ioXz1YKoI_HM5OCGeLEtVlI2MRXwMQDR38VqrSoDoBQxj4eSfcDfspWNpMeEkCkbHUcAsn2-NSDrefPZKW6Rkij-C1M8yB_qllh-cb3vdK86vZIEtMQ3xBIjKko-dTa8TIO1j4lE7xRVgbSx6sc_8vsjdMQ8aywiZkxbiTldFC4t2nBzVXpja9QDS3djnGkqPslb0yefs1dkxu97aj9Nu0ktdJxXTpdXLkmjfbCfwsOnAnpv3LOyB1qjHMD9sShQzGEY2Ee2VSh0GsyahUmsgtsNO7Cf8FU4icQ--js79M2yPavonSgy6zrTJoHZg_qu7GXQCx3SamkNt-b9lww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایکس تو چین فیلتره
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/funhiphop/74980" target="_blank">📅 13:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPMOjaQlOR4PmM1IlBLtxAVaFjjb6JmlZVeCgHFNDiZipmX7ehewu5WtZU2hBX0wSTIsUqqNukQgkh8nL6w0OHFR4rCRQEUgB6rTBLXh4zcp-PlFEK7u2bRpk9Y5rvC_wNauGaApffs9DGmUDWchpSvJ-KbFXi5Mk3m0uOvbr6zspZd-Ig3Q5MXKvMfNod2JuW3JSIN7Wgx0bArElq5mmVyn2KcMwJD5sxyTkQKP4IY1JJNOd3YJYR3FwgYP62q54kgz76109V6LLgnEDGS8-N-WG3KqEHtiPKU973W_BM6OHUVbYNHdkWhDcAZgdZlRl03LcV2FgHVJVxoAB2cStg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: رهبری ایران پنج شرط را برای آمریکا تعیین کرده است که باید قبل از ورود به مذاکرات پرونده هسته‌ای برآورده شوند: — پایان دادن به جنگ در همه جبهه‌ها (خصوصا لبنان) — رفع همه تحریم‌ها — آزادسازی همه‌ی دارایی‌های مسدود شده — جبران خسارات و زیان‌های جنگ —…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/74979" target="_blank">📅 13:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74978">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دریک تو آلبومش: ایسپ راکی، ریانا، بچه ی ایسپ و ریانا، کندریک لامار، دی‌جی خالد، پلی بوی کارتی، جی‌زی، لبران جیمز و پسرش رو دیس کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/funhiphop/74978" target="_blank">📅 12:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">از سیاست چخبر؟
دریک تو آلبوم آیس‌من خایه مالی فلسطینو کرد، خایه مالی ایرانو کرد، خایه مالی کانادا رو هم کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/funhiphop/74977" target="_blank">📅 12:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جمهوری اسلامی به مناسبت سه تا آلبوم جدید دریک در سه موج به مقر های گروه های کرد عراق حمله پهپادی و موشکی کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/funhiphop/74976" target="_blank">📅 12:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74975">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: ICEMAN
🛑
Featured: Future, 21Savage  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/funhiphop/74975" target="_blank">📅 11:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74973">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۳۰ اردیبهشت پوتین به چین میره و با رئیس جمهور این کشور دیدار میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/74973" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74972">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بخاطر آلبوما امروز دریک اسپاتیفای بخاطر هجوم مردم چندبار از دسترس خارج شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/74972" target="_blank">📅 11:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74971">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قیمت اشتراکشم نسبت به شرایط اقتصادی هر کشور تعیین میکنن، اگه تو ایران آزاد بود و قیمت براش تعیین میکردن احتمالا ماهانه زیر ۱۰ دلار میفتاد</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/funhiphop/74971" target="_blank">📅 11:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74970">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قیمت جهانی دیش مینی استارلینک شده ۲۰۰ دلار  تو ایران چنده؟ زیر ۳ هزار دلار پیدا نمیکنی  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/74970" target="_blank">📅 11:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74969">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP0f83hnUnIOTFQVX-AF6CQwaUKcBgUHY-JPCBP6pUDa-WRsCufTOLWKN98H4ntuyNBQiOlbySigYeV29EJz-zJvEbIQGbH65KrA02ZnLykNbeTfa1mzHwbtaRmm6t7wvl64LWndwK1D6L_AlDaHWxHmhpgWYrQvAKV45dDg0T74KHpZJuujizeWOlb08jQOYZHaEiCH7xVYHK4voh3uzVacP-6LRNgKLBKKh6pHHm1j5wJVU_ZPJjJQti-7cFhaKWChPo0eAUvmH2uq124iwAd817Blk1wc4qS4-HAQEdi-Ku4ZoUONtegPds2V3SdFsXvhMwvqFqMoqGhW7yvw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جهانی دیش مینی استارلینک شده ۲۰۰ دلار
تو ایران چنده؟ زیر ۳ هزار دلار پیدا نمیکنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/funhiphop/74969" target="_blank">📅 11:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74963">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WALDK56_6DCofFbLKuotMyqJip8D5PrPbSwI5_uvIN2BxHnTFuHEogEtnOIpX1p8KzXQa4FPxpLto7Te8b9T5Y2xqFrpAizGIpnSaJJMuVnayH0iChvtOQNfEQWLsJXPeICDJcFXM__p0JyxJbU49GkiKvHxClyXr6C3232joIXamFwKaCt6224MZ1rqpMNTHwplT6upLD_46jIGeA8c47hSONRmG7wXFporCEc8wQ95LA0AEKfqlcAsI-Q8YLc4mkBCIeKsG22N1cycGpHcfPQHoU2mUAwhLXwp982hyr7SR4VW42YzL628PB67hnRznIVHoyJ3wjAXUnG2cuwpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دختره تا دیروز توییت میزد رضا پهلوی کنار بیت رهبری میخواد فراخوان بده
بعد الان همین دختره فهمید ولی شما نه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/74963" target="_blank">📅 10:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74962">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFTE3FGd2Js0D4PJuIk7qzrTxq_qtfIINs6Zm0zqOiLCdk7Cq6Z_O0bQFXoHq53SaTk8SyN9N_B0bZ6-DKVaeG3x7GoW45prJrMM8S37oAFTsz55gN6ocIak3gwnTYDWacXMM8XfhTLQOhrNZiIqSkq4afz3ByNkil-SOTA_6RUiBjedw25BjLhA0pD0WenUZ9iGwT8_7jjG1KhUUk60Lu95Czdrop0hPK5smYBSFMEBZm7OklftMLsMSw0CWpA0pZamiGlP4WdoxLPlFDSib8qOIDQNlf1kXxQPzprMY1KBbGs-7h9FchV2dPu3cdSVgGkGiK9CmVHVA4zJX9H0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title: Habibti
🛑
Featured: PartyNextDoor, SeXxy Red
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/funhiphop/74962" target="_blank">📅 10:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74961">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJsxNgEvP1lIpLF5NN0Jar_L1q82HdbNGTn8czJuvJ5dRm9aP6BpFBLEDXnbgh5K31ns6zjrJiXiv3409wE0-AI5ekk1m-uZ4RHHBM_pQXKLAGQ1XCbGvD2WT2E3nLrHxfyF7DZkV8gLmdRveWQAo_yro5xgjoHSV5-soXM7e7vnbHK_i0pDoamutvD7-8SmVnm4agGXntac3a5bl1NSH1pT7ueoA91JdtOyw8OVD0mwZHHicbb1TaermpMV09zPBdATWxL8wPicwqls3B-H0ILqoikeJMsc-WZd03-UgmmNCH14WR4WdjVzV8AukUnTWDYBY5n7Geez01CvIdnXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title:
Maid Of Honour
🛑
Featured: Central Cee, Sexxy Red
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/74961" target="_blank">📅 10:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74955">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reexmgXD8LuGjkf9qy7y4iMOYo8CzzHLm49gRVdPmqMZMn60BYxCz61dc5c0mSs4oAIrPc0b0GQQENVxaiYs7MFcQXUiA-xIWE4MF1HJ8HS9lNM_bm57WcLN4RVJhwullH-28F2DAIkGHoiZwEt8ISwlhzl5ikFYQOuLDt_3UBbpJFHmYxr26KoeEhja_fNo4HyWigokIKRh0NF9Nxl2BkIKIspilot85MyBmNAoDp9daZJIeoct-ercHkiyk4FM2W63NH_Gy5Eyg1p5ka-rfLYPPQRDjhyW0r4AggAn8B74GoybBqQoWhwlkzrrI55v0mePtl_kSZU0Iq6ueDSuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title:
ICEMAN
🛑
Featured:
Future, 21Savage
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/74955" target="_blank">📅 10:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74954">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امشب میزنن</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/74954" target="_blank">📅 10:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74950">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2d7d91b2.mp4?token=PW8Kr7FGMIUXPIFbquh-6Ecqkw3TY-hXXaUxiWYkJeQ3ZftDq3f_aqzJL0ZYneXtEdzkOUabPZKUk_MROxgT0UIhauPKOKSM6Nooi26yWK-0asE7B6RHUBO1Zz8lbLF_c5P_lMRgOcSsRtrtNQUL3MV4RMk2-oaoUkgGLVSG4RhoNYQyZOxPO4lHdU-V3Ty-8uvZYsfdPoHr_89HyAGBSaoGpVyEjxs2BEg3uFlWtrNeY8kUJrC3KbUIz5SqNtzddQOtKGhmBIhN_7u6WXxHQHm7PtT3-mk3fcOualnMsrmJ7J8xF2SEkfZui_dztIuT6_bYJwWSi6sBMraTjCwr_oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2d7d91b2.mp4?token=PW8Kr7FGMIUXPIFbquh-6Ecqkw3TY-hXXaUxiWYkJeQ3ZftDq3f_aqzJL0ZYneXtEdzkOUabPZKUk_MROxgT0UIhauPKOKSM6Nooi26yWK-0asE7B6RHUBO1Zz8lbLF_c5P_lMRgOcSsRtrtNQUL3MV4RMk2-oaoUkgGLVSG4RhoNYQyZOxPO4lHdU-V3Ty-8uvZYsfdPoHr_89HyAGBSaoGpVyEjxs2BEg3uFlWtrNeY8kUJrC3KbUIz5SqNtzddQOtKGhmBIhN_7u6WXxHQHm7PtT3-mk3fcOualnMsrmJ7J8xF2SEkfZui_dztIuT6_bYJwWSi6sBMraTjCwr_oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتما ببینید بلکه عاقل شدید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/funhiphop/74950" target="_blank">📅 09:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74949">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دریک همزمان سه تا آلبوم ریلیز کرد</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/74949" target="_blank">📅 08:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74948">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">توییترو باز کردم دیدم یکی توییت زده اپ شیر خورشید رو گارد جاویدان ساخته، بستمش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/74948" target="_blank">📅 08:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74947">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">توییترو باز کردم دیدم یکی توییت زده اپ شیر خورشید رو گارد جاویدان ساخته، بستمش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/funhiphop/74947" target="_blank">📅 08:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74946">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4E-MSyojigRo-7xz6tAWoNiAUCbBz_hz4U4W5BR4d6TFsADcqTZa3zmVSzdYqvNXSS-9EsAfZyYT1WasoOm587UYrrSowTwe2ljgZ3K3V1zaNDUnIByeDljMPejrMBqu-TzNAxtEG_IRTC-0uK6-y9tCBqbyx9E3ke--gxdkrCCrTCkC4vRQtTyqfWInp2OzbXXzZLMZhTR0xktL2QmlH8IUdY7ayK6d2MYTOZzAHzTW_vjiHbLsYLHuOgari9EfRz2M-Mq8MlQ9VUz9whQ75IwVzZ636GCoz2EKOcCJHI9L-Dy5AsRTGz8bzK1PQ7ZlP3Wq_PLxq5LWAvEWKh8fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗿
وزارت امور خارجه آمریکا
اعلام کرد که در اواخر ماه آوریل، ونزوئلا
بیش از ۷۳۴۰ کیلوگرم اورانیوم با غنای بالا
را از راکتور هسته‌ای RV-1 در منطقه آلتوس
میراندینوس
به مرکز
ساوانا
ریور در
کارولینای
جنوبی
آمریکا
منتقل کرده است.
این محموله اورانیوم با یک کشتی
بریتانیایی
جابه‌جا شد و آژانس بین‌المللی انرژی اتمی نیز ضمن نظارت بر تمام مراحل،
حمایت‌های فنی لازم را ارائه داد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/74946" target="_blank">📅 06:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74945">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">😠
دونالد ترامپ
فکر نمی‌کنم گرفتن این اورانیوم جز از جنبه تبلیغاتی ضرورتی داشته باشد. به نظرم این کار بیشتر برای رسانه‌های دروغ‌پرداز مهم است. من همان کسی هستم که گفتم اورانیوم را پس می‌گیریم و
حتماً هم این کار را خواهیم کرد
.
ما کاملاً چشممان به آن است و زیر نظرش داریم.
به آن‌ها گفتم اگر بخواهند نیرویی به آنجا بفرستند تا شانسی برای خارج کردنش امتحان کنند، یا اگر ببینم کسی دارد تلاشی می‌کند،
فقط با چند تا بمب آنجا را می‌زنیم
و همه‌چیز تمام می‌شود؛
آن‌ها جرأت این کار را نخواهند داشت.
ما در آن سه سایت، ۲۴ ساعته با نُه دوربین همه چیز را کنترل می‌کنیم.
راستش را بخواهید،
اگر اورانیوم را بگیریم خودم هم حس بهتری دارم
، اما معتقدم این کار بیشتر از هر چیز دیگری جنبه تبلیغاتی و رسانه‌ای دارد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/74945" target="_blank">📅 05:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74944">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">😠
دونالد
ترامپ
به نظرم آن‌ها اتفاقاً از خیلی جهات خیلی منطقی‌تر شده‌اند. از آن رده‌بالایی‌ها و رده‌دومی‌هایی که دیگر بین‌مان نیستند، باهوش‌ترند.»
هنیتی:
پس چرا مدام شل‌کن‌سفت‌کن در می‌آورند؟
یک توافقی می‌کنند و بعد فردایش زیرش می‌زنند... مثلاً ما پنج روز منتظر نامه‌ای ماندیم که باید یک‌ساعته می‌رسید.
داخل کشورشان بدجوری به هم ریخته و آشفته است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/funhiphop/74944" target="_blank">📅 05:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🤑
دونالد ترامپ
در حال حاضر، هیچ نفتی از جزیره خارگ صادر نمی‌شود؛ هیچی، صفر.
مردم دارند جاهای دیگری را برای خرید نفت پیدا می‌کنند، مثلاً تگزاس. بنابراین، نمی‌خواهم بگویم که داریم ثروت هنگفتی به جیب می‌زنیم. اگر این را بگویم، آن‌ها می‌گویند: «اوه، او آدم‌های معمولی (قشر ضعیف) را فراموش کرده است.»
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/funhiphop/74943" target="_blank">📅 05:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صحبت ها مقداری زیاد هست
بابت حجم زیاد مسیج ها پوزش مطلبم
❤️
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/74942" target="_blank">📅 05:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74941">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">😠
دونالد ترامپ
من به شی جین‌پینگ گفتم شما نیازی ندارید که ایران سلاح هسته‌ای داشته باشد.
هانیتی: او چه جوابی داد؟
🤨
ترامپ: او خیلی واکنش نشان نمی‌دهد. آدم بسیار خونسردی است. قرار نیست بگوید «بله، حرف خوبی زدی».
هانیتی: فکر می‌کنید موافق بود؟
ترامپ:
فکر می‌کنم بله.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/74941" target="_blank">📅 05:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74940">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">😠
در ادامه
مجری فاکس نیوز، هانیتی: فکر می‌کنید شی جین‌پینگ و چین توانایی تاثیرگذاری روی ایران را دارند؟ با توجه به اینکه چین یکی از بزرگ‌ترین خریداران نفت ایران است؟
ترامپ: احتمالاً… ببینید، او با تهدید و جنگ وارد نمی‌شود. تا الان خیلی خوب عمل کرده است.
هانیتی: منظورم تاثیرگذاری بود…
ترامپ:
آن‌ها می‌خواهند از آمریکا نفت بخرند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/funhiphop/74940" target="_blank">📅 05:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74939">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">😠
دونالد ترامپ
امیدوارم ایران این حرف‌ها را ببیند.
ما
دقیقاً
می‌دانیم چه چیزهایی مستقر کرده‌اند.
آن‌ها یک فرصت کوتاه پیدا کردند و حالا سعی می‌کنند دوباره بعضی تجهیزات را
جمع‌آوری
کنند. چند
موشک را هم از زیر زمین بیرون آورده‌اند
، اما همه این‌ها در عرض یک روز از بین خواهد رفت.
تمام کارهایی که طی چهار هفته گذشته انجام داده‌اند،
در یک روز نابود می‌شود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/funhiphop/74939" target="_blank">📅 05:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74938">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">😠
دونالد ترامپ
جنگ ویتنام ۱۹ سال طول کشید. فکر می‌کنم جنگ عراق هم حدود ۱۰ سال بود… در ویتنام هزاران نفر کشته شدند. اما متأسفانه در این دو جنگ، ما ۱۳ نفر را از دست دادیم.
13 نفر در مقایسه با 75 هزار نفر و یا حتی 50 هزار نفر.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/funhiphop/74938" target="_blank">📅 05:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74937">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">😠
دونالد ترامپ
قیمت نفت نسبت به چیزی که بیشتر مردم، حتی خود من، انتظار داشتیم خیلی کم افزایش پیدا کرد.
😶
فکر می‌کردیم بیشتر بالا برود، اما برای یک دوره کوتاه این موضوع قابل قبول بود؛ چون ما نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/74937" target="_blank">📅 05:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74936">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">😠
دونالد ترامپ
اگر بایدن به چین می‌رفت، حتی فکر هم نمی‌کنم می‌توانست با رئیس‌جمهور چین دیدار کند.
من فکر می‌کنم شی جین‌پینگ آدمی گرم و محترم است، اما کاملاً روی کار تمرکز دارد. اهل بازی و حرف‌های حاشیه‌ای نیست؛ درباره آب‌وهوا یا چیزهای بی‌اهمیت صحبت نمی‌کند و من این ویژگی را دوست دارم.
اگر قرار بود برای نقش رهبر چین در یک فیلم بازیگر انتخاب کنند، دقیقاً باید کسی شبیه او را پیدا می‌کردند. واقعاً فردی مثل او کم پیدا می‌شود؛ مخصوصاً با آن شخصیت و قد بلندش.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/funhiphop/74936" target="_blank">📅 05:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74935">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AihVcoTNGEgkVDcrVQJjKMbnpjbJ_eQnvjKwA-FKfDzbO0_0S2yUI6pLHaW2D7qVH-HG21SqomFbFnBiAVwvYwtDqEtHFhAmk9zVAlec6j6aElibST51ank3ObaYx_aLTxmPbWbDcT_QheQI1ELnO0BT1PWlXZD9vd0bN6XQOru-tXskLAK7Tb_BXfrmD7jkM2qW_wZFqmOP8RCY95Xrgjl95o3mKdwsjz-yNb4Mg6rKrJypj1TKAxkvS4DMuFRMuKLY-fwxBtkqb8vg9F2L4fn1kWO4zK3fzjG6ZzkPoJO9S2vJR5b0r6_uWDPtnM7f0E00VooYGjp6s0zCH174xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز عصر دفتر نتانیاهو گفت طی جنگ ۴۰ روزه، نتانیاهو شخصا سفر مخفیانه‌ای به امارات داشته تا با رئیس امارات دیدار کنه و چند تا مقام نظامی هم تو این مدت رفتن اونجا که درمورد جنگ هماهنگی ایجاد کنن.  الان امارات کلا همه چیو تکذیب کرده گفته ما هیچ‌کس رو اینورا…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/funhiphop/74935" target="_blank">📅 04:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74934">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل در حال آماده‌سازی برای احتمال جنگی تازه با ایران پس از سفر رئیس‌جمهور ترامپ به چین است.
مقامات اسرائیلی تخمین می‌زنند که پنجره احتمالی برای اقدام نظامی آمریکا ممکن است از فردا آغاز شده و تا شروع جام جهانی ادامه یابد، و انتظار می‌رود ارتش اسرائیل در صورت از سرگیری درگیری‌ها درگیر شود.
هنوز نشانه قطعی وجود ندارد که رئیس‌جمهور ترامپ تصمیم نهایی را گرفته باشد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/74934" target="_blank">📅 03:17 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
