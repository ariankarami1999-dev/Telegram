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
<img src="https://cdn4.telesco.pe/file/li5gdq7LJk4jqDFPBT3Xwog_LsHcchQDUGaupdzRu8keTQpOiNn6bKqeQmU7T6VdJ65Eb5_0Lal_ui3bvOEl49Si1Z0uZF4zb83bp97uanxfdi0y3LEqtny7Fztkqhag17BXBjaPjYlMT7iw6h9i2bufAqo3YQQAx2MqimkbCYrFPDlTjIxh-X_vBmi8pSScrC9iGVCcgSg1EB2D5d7CCdeSTcgRZWoFoTjzSbLMC3pLhqCiFYLhJY-2TgWg-ZsAVhXiz1Wgf0zk-nENA4AXuR_ZbBI-iDAn7vy8uKyzMil9ccufvRCL727NkR28u8DdGHovNLQh0usWDyeP5Vtapg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.2M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 18:42:27</div>
<hr>

<div class="tg-post" id="msg-676098">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
نتانیاهو نخست وزیر رژيم صهیونیستی وارد واشنگتن شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/akhbarefori/676098" target="_blank">📅 18:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676097">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3be888146.mp4?token=fwjz9CaeuKNblEN8KZykIVoBXAEc4NXUPDmoryqiC8JiHOoVQ1kafF76T-2m0Ol5yTwUJrkqSPcH_4aWAtJuIGTzlFl6qCrxh0TbRLLdDfN_JvqKndQFy4SlbX7YZ7LyAUaJxfymjpKOfHxHa_Hf68ghuUy8ACnojuc_9hEz5Y75glaaF8leKeX_2q_iK1mUC97l3GqqYEQNAH8EFjdOuDOJtVgnDAhvuDCKMOM3clBnIGxG16D9f8B0XkvQYqlmXpqv66KU70QKLv5MP__i9F4r82swhJ9HgLylWBBXlQeEkMSZC1BhjWtdGZfzMJOIexCPMeV44tU5nXpHw7zboolBtL8ydmcvv12BPPfKvHEhKrY9BLKaKZdM5xf5mQ0w8NnWIvHDRvPTs8HWL7XrNaZwOHMdXoyPAWkzxHhUFBWUkMfI3hWdme_lRTz4NiTbpvo0u_L2FvVwkWJ5h368uxC-ku22vKxxC7-15gq3bfyb1DRPNgLMiUCRc6NP9CrmfsKwbWwVWVkGUO8PxQt0pweNcBrR_znASgn8Rg6WckU6ueuCqnwI6ShFqBhkeEV4WnR8m71E9ew-UNyotErLYmbE5iWqdoAyGDq0ox_eaaqL9MTLIqybvytU6Mq5CqIy_FOivlkJxfk5vhDp0UB_nLGpm1QY5zOf1oxp93hEtDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3be888146.mp4?token=fwjz9CaeuKNblEN8KZykIVoBXAEc4NXUPDmoryqiC8JiHOoVQ1kafF76T-2m0Ol5yTwUJrkqSPcH_4aWAtJuIGTzlFl6qCrxh0TbRLLdDfN_JvqKndQFy4SlbX7YZ7LyAUaJxfymjpKOfHxHa_Hf68ghuUy8ACnojuc_9hEz5Y75glaaF8leKeX_2q_iK1mUC97l3GqqYEQNAH8EFjdOuDOJtVgnDAhvuDCKMOM3clBnIGxG16D9f8B0XkvQYqlmXpqv66KU70QKLv5MP__i9F4r82swhJ9HgLylWBBXlQeEkMSZC1BhjWtdGZfzMJOIexCPMeV44tU5nXpHw7zboolBtL8ydmcvv12BPPfKvHEhKrY9BLKaKZdM5xf5mQ0w8NnWIvHDRvPTs8HWL7XrNaZwOHMdXoyPAWkzxHhUFBWUkMfI3hWdme_lRTz4NiTbpvo0u_L2FvVwkWJ5h368uxC-ku22vKxxC7-15gq3bfyb1DRPNgLMiUCRc6NP9CrmfsKwbWwVWVkGUO8PxQt0pweNcBrR_znASgn8Rg6WckU6ueuCqnwI6ShFqBhkeEV4WnR8m71E9ew-UNyotErLYmbE5iWqdoAyGDq0ox_eaaqL9MTLIqybvytU6Mq5CqIy_FOivlkJxfk5vhDp0UB_nLGpm1QY5zOf1oxp93hEtDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های متناقض از وزارت صمت و انجمن واردکنندگان خودرو؛ ثبت سفارش خودروهای وارداتی متوقف شد؟
مهدی دادفر، دبیر انجمن واردکنندگان خودرو در
#گفتگو
با خبرفوری
:
🔹
از ابتدای سال ۱۴۰۵ تا امروز، هیچ ثبت سفارش جدیدی برای واردکنندگان انجام نشده است. اگر وزارت صمت نظر دیگری دارد، می‌تواند مستندات خود را ارائه کند.
🔹
در حال حاضر فقط ویرایش و تمدید ثبت سفارش‌های قبلی امکان‌پذیر است. ویرایش ثبت سفارش‌ها نیز پس از سه ماه پیگیری و جنگ امکان‌پذیر شده است. شنیده می‌شود به دلیل شرایط موجود، امتیاز ثبت سفارش‌های پیشین در حال خرید و فروش است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/676097" target="_blank">📅 18:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676096">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
تصاویری از نعش لیندزی گراهام
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/676096" target="_blank">📅 18:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676095">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یمن: بدون رفع محاصره، مذاکره‌ای در کار نیست.
🔹
فدراسیون فوتبال: چادرملو نماینده قانونی ایران در آسیاست/ پیگیری حقوقی از AFC ادامه دارد.
🔹
نرخ تورم ماهانه نصف شد/ نرخ تورم سالانه به ۶۱.۴ رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676095" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676094">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iloQhHK9XPkMMd-SP7DgvScjo2xTKGEmRke42NKOku0LbB5ROXlc1FxZAWwVQMAe4mTsP5sEy9dXyANQQbND-V38_DauV7nBnG7JVs_yAb6fyqjk5eFaa0aVZpvLpIb3m5R9n4dE4wabA_lZlOUJFY1gdMUvS5p7MA2KsKz6t0rU8IeeZAILTj5lUJA2IdgX6uhACfwqjNj5PMP4GyWtSmIGR3Q2T0KnWutRtmOAD_gWtI3vCotWPFD_8lM74lJFqI2SfGXqwNobEeRFDFSjy2PDotEMC8D239Em4WKHw1eT4YQliQxbyt5PYQt-CFlZT9uc_NyZOHMpJ8Oy7SsZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشگیری از بیماری‌های پوستی در پیاده‌روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/676094" target="_blank">📅 18:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676093">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVNUORfr_aDaEgKXz5MdoKp1sqkN4mQKC_TIKB6wW5_QHJXxtOVDqRRvMBrVXVL77FxlzbhuLovGpJg7SwCCgOzSt1ARKOKUu-AUWAeI7bXxqdy4ZkVIlDxG6DAnya2geTgqVX1J1pAsB8f1Ju-pbK4AXV0nMKG8Yl9okNQV_djfjKFnyEYNXZkRkVGo8uBUsbJvol5gQ9a9IagMlrIMh8gAd5ZCtPDisF_mPNGcwI55sKJu5kfH69CIY4_Xf3txVUKvyaO3bC1sK4hDIngwxG_yH53HdhRw7aEWAkTbfQvrtarV_Cjyu-nZpZ1tQh95nJLliR3EzfjlUENNlRvFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای سرمایه‌گذاری در طلا چه گزینه‌هایی داریم؟
🟢
خرید طلای فیزیکی با هزینه‌هایی مانند اجرت، مالیات و اختلاف قیمت خرید و فروش همراه است. همچنین نگهداری امن، احتمال سرقت و اطمینان از اصالت طلا از دغدغه‌های این روش محسوب می‌شود.
🟢
صندوق‌های طلا امکان سرمایه‌گذاری آنلاین با مبالغ پایین و بدون اجرت و هزینه نگهداری را فراهم می‌کنند. بخش اصلی دارایی این صندوق‌ها از گواهی سپرده شمش و سکه تشکیل شده و پشتوانه فیزیکی آن‌ها در انبارهای بورس کالا نگهداری می‌شود.
🟢
صندوق طلای «رز ترنج» با مدیریت فعال ترکیب شمش، سکه و ابزارهای آپشن، از طریق تمام کارگزاری‌ها و با حداقل ۱۰۰ هزار تومان قابل خرید است.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/676093" target="_blank">📅 18:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676092">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTvs2vBvZ8BZyQbAoRUmlzznPXB1fBoUnsX4aO52kZxrxCkasYJUQRPcHRgNY8UQCWvFATsPX45Oa2Elfuvw2q1MbPY-1-MWoSH5NI73ZNDOr1tcyiibsoiyGB59bb6vuk6fH8chY154HBE5p3hOla3CKtEC-45gKuPbkUlIxtVgG9R7mWixDMxkT7lBZpCvqiNk6J2kCSsKHNYCPgBxHrI3fJtbFJAtWBK5mgd2XxISEcXc-ruvQOtnO5div_r0Z2xazSBnxp80hHc1OGNG5aU4PCLs23_ErUUO4ysKuCR__Q2vcoq2_EoRfHFHq_9MxJhXhbrha21C9AiBqZ6h6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامبیز پیکارجو رئیس ‌هیات
مدیره
#بیمه_البرز
شد
پيكارجو داراي مدرک دکترای تخصصی اقتصاد مالی و بین‌الملل بوده كه استادیاري و عضويت در هیئت‌علمی دانشگاه آزاد اسلامی واحد علوم و تحقیقات، مدیرعاملی و عضویت در هیئت‌مدیره بیمه آرمان، قائم‌مقامی بیمه سینا و همچنین مدیریت طرح و توسعه بیمه ملت از جمله سوابق علمي و تخصصي وي مي باشد.
#بيمه_البرز_توانگر_و_ماندگار</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/676092" target="_blank">📅 18:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676091">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blzBT2lUDARgtytfXeXu26dxy-Iq1ae1_ZDV9L1KXlQzQjYZpSAeh_2HZ6i2QTEg5aPoEy3ijCESIb6FFEAMQFWTg-aHQHR9lJy3F_93AnsuyNxA8iL96FQwJphgKxpYADPqKYbbIMCPDimLB0TDAwwpsM9Ypdfx1YMYY_qRDe5uWTZcQ1mFH9v8MKRrK_IIy8D7Q1duDBwIf0RvWjXO-LtyvNIb0Jerh2KL6giYxEbRjxsKEQUKa3rx8Bc0QkL5GixyvDBziNgv-n5kj4hqKAI27GfbixcEcTAqMsxIWnAcqvIm73QQbfUG9B4Ih0VqW6uOYR9MyM0xL6M5cQFAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلزله در گوگل؛ قمار ۲۰۰ میلیارد دلاری روی هوش مصنوعی
🔹
رقابت نفس‌گیر در هوش مصنوعی، گوگل را به نقطه‌ای بی‌سابقه رساند. این شرکت پس از بیش از دو دهه، برای نخستین بار با جریان نقدی آزاد منفی مواجه شده؛ اتفاقی که نتیجه سرمایه‌گذاری سنگین ۴۴.۹ میلیارد دلاری تنها در یک فصل روی زیرساخت‌های هوش مصنوعی است.
🔹
گوگل قصد دارد طی سال‌های آینده نزدیک به ۲۰۰ میلیارد دلار در توسعه زیرساخت‌های هوش مصنوعی سرمایه‌گذاری کند. اقدامی که این غول فناوری را به استقراض بیش از ۱۰۰ میلیارد دلار و تأمین مالی گسترده از بازار سرمایه واداشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/676091" target="_blank">📅 18:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676087">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qfp7BJFgpLAh41IcfVjwoLyWupXkSuDedKyztFiuLtH8tmXhxrpBGOadyK0fYc8q24OBa14XaAiKe3hBfixvBHsElZJhgS0MPWU44c8ctmdQmZnDgNgPkS2RZNmKPfmgYHgehVL9AnhewHxUFXvl-Svce_lDI6Prz74fao2Xuudq5-cvfj-0IORlGoMt5ap85yufC7ulqRaZbR0kvxdsCt51TQqZSZDb_I_S9xX5YI7VrfnesoxRgbBKnEsMKW5-FBB4KYQYp9Nx1jSx6OF2eHx9Y1jDwpGGSMgtN_yQKo7TcOQG3ipuUcNqtSquy3n7nI_G-IQhyxKtfaMWxOJtlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfhopGTx9nivtRcIuMNqzS5jRH7LIP9AQg26ui3w0cVO-NO6avzXo3oHULxsBnhNq2G3l8EqNhkwL9NRKRoEm_dFs9DC4nGJOGTQnYM7CXtUqkcdZbnBGHioPGde0czbD04zXMVKSco7Z3AJy3YfjCsUMSJhv5wEk-U4xsxyUEB4uSTSKkLKJ5sFdWH2-m6kbBHyHu6-0Zzyxpgx-XwGzh9psMEI6ebdEh48hfL7kIHq2KjgULoejEtfAEsiDwShrIzT47TaA2UdfyiNMHi6Ijtwz6S_WSwAC4bgVlMdWHA0wDRgAcEYZEAQzNyhyE75RTR0koqvg8wSAEGfWCttxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2SnoD8mbYoy7Z8W7wM8GVFcl25f2u3CHM57X2yNhlwZp-jZDh2ysk3ISLJkw8YIM-Tap1k-317QsgJhtCrO3GwxYyl6Z1lqo_6H6_twph6iNKnfoDVxB_f6-SsA0OVFLxIaWxI5_hxRwhTuOIK-DD2g6IejA2XIOsE6HMges3iqvYTRQMHQs4gAtp_LA3-pN19EX4_FRUKvpB22kSEdp8eb6lvplyA3MiOUkrJmCTTfDcuiV1UOuPij2k7xi3RcMkV_Kugl2kjOvKEucKiQvh-2PeAcnX50_LTXIoAPKl1YHgw6Wf6od10agHI7KFJHtmFCL8cMrQG2jKnxwj6VeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8jhBvsBZ8ZRP6BjY0wMElXkrWVHRXlVp7AMWxnnULJ1b6b9ghf0kNYk8qRk12nDCKNuUi4nW1JZzPiazZwtHJ6QzaHglK7PSS_tZs4SAs10aiquKP5UqiKRbg_niHtyR2Tzwxn9mNih00_1so6gUvewN9pXrtYo9glx-4wSyTm35VANI97O5_6N7y26AfNNfYI32nrmHva_6x6uP5_vEc9Rje3JoDQnyHMyQC_uj8wuWM6Zh84yIMkMBmutpoSUcory8X0C31FTgfv19aiHGZ7GjD0Td2sMi0s9pUhSu3iLMoaaIgg3Z3e48AfuGmKsp7qxMF4A5YNOIdhTigDuZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فروریختن یک مرکز خرید در ژاپن در پی وقوع زلزله
🔹
به گزارش "ان اچ کی"، شمار زیادی زیر آوار گرفتار شده و شماری مصدوم شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/676087" target="_blank">📅 17:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676086">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سه شهروند کرد در مناطق مرزی استان کردستان به ضرب گلوله اراذل و اوباش جان باختند
🔹
منابع محلی می‌گویند
عاملان این حادثه که به‌نظر می‌رسد از اشرار و باندهای مسلح فعال در مناطق مرزی هستند
، بلافاصله پس از تیراندازی صحنه را ترک کرده و از منطقه متواری شده‌اند. شناسایی عاملان، و نیز علل و انگیزه ضاربین توسط نیروهای انتظامی و امنیتی در دست پیگیری می باشد./ جماران
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/676086" target="_blank">📅 17:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676085">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuxIKGqKqiXc2irPihLk_8BYDkheT5HuQ6v4gMibCiCL2JV21ja6oOWYPbTVj8iEqFj8TtWw8xOP3Hnm3xsK2whaFjI76pSOFZYBu1AXSaJ9cryZszqWKHkpdUtCB10kZAFPQWEoL8e-rZRzP56XVI134Rm5GD5fC-Z6vyvI_ZdYIrcnbEE0ALRgSqLE0TzBFiHOOun6_wj0sIf-xcmod4ct24XgS1qKJ3ZMTUn-xP9zmwDRwbT4cgoLs7AZcNkKIyNn-T8NFpxm9JrwxGBmkO0Mn-xni9oTbAglFaj8QW93MymdWjFC7tx594CYz37OBwPDbuJH6FRXiEJkpw6rDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ وابستگی جمعیت چیست؟
🔹
نرخ وابستگی سنی نشان می‌دهد به ازای هر ۱۰۰ نفر جمعیت در سن کار (۱۵ تا ۶۴ سال)، چند نفر کودک یا سالمند وجود دارد. هرچه این شاخص کمتر باشد، سهم نیروی کار در جمعیت بیشتر و پنجره جمعیتی بازتر است.
🔹
بر اساس آمار سال ۲۰۲۴، جمهوری آفریقای مرکزی با نرخ وابستگی سنی ۱۰۴.۷ درصد در صدر جهان قرار دارد. پس از آن افغانستان و نیجریه بیشترین نرخ وابستگی را دارند.
🔹
ایران با نرخ ۴۴.۳ درصد در رتبه ۱۸۵ جهان قرار گرفته و از کشورهایی مانند ترکیه، هند، روسیه، آمریکا، بریتانیا، سوئد، عراق و ژاپن وضعیت بهتری دارد.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/676085" target="_blank">📅 17:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676083">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
کیفرخواست پرونده شهادت رهبر شهید انقلاب و شهدای مدرسه میناب و لامرد به‌زودی صادر می‌شود  دادستان تهران:
🔹
پرونده شهادت رهبر شهید انقلاب و خانواده معظم ایشان و همچنین پرونده‌های خاص دیگر مانند جنایات رخ‌داده در لامرد و میناب، حداکثر تا ۲ هفته آینده به دادگاه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/676083" target="_blank">📅 17:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676082">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iedetnR1k4nXIin-7A-QbSvtB3h-VL9Bhs-VAjt4N2HpJQ-5zAWdf4-6FH1vJ23LgjJNAjWclur9SMD5fsJoH9aw0UbOOqp1oOanVKPxMO-hwn9tTFBL2FiigcTYJvKRr5lLxKizA_0voiEKA1fMn6x3lvHKsdFwhY23RTSWt_4UhY19Wkc27rmsT6SlaSzzSr6Jf3giiMSyrY8opHzFTKbQYQjZFWyi9iVFTF9Qr0TNDppk-Gb3xUtKiopx0TBj16J_4upTsfosr6D5FflfenLsLBsAO_N54yX1R94yfzf8BWAE-6pUIxdt4UvdaxUsZOtT5BSSqWk1A0UfZsLQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه جدید ترامپ برای ایران بعد از توقف حملات موشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/676082" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676081">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
برنامه دوئل‌های ۴ تیم مدعی لیگ برتر
🔹
هفته ۲: سپاهان - تراکتور
🔹
هفته ۳: استقلال - سپاهان
🔹
هفته ۳: تراکتور - پرسپولیس
🔹
هفته ۵: استقلال - پرسپولیس
🔹
هفته ۸: تراکتور - استقلال
🔹
هفته ۱۵: پرسپولیس - سپاهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/676081" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676080">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cf68d6ca.mp4?token=HItpdfBIiVPbIhHzFhkHOr5aTI52-xSXHup-oAR_yQbssJerNw-k_OWQ4XVk9lWrSMRG0U8CEZa5lK_tnByJ0IeuJlPgu4IITYt9uL55C--J6Y9fMrz7S2OJ49pwQy1udB0mCgmjrgcO3je0AIueP2CLMa5PPs9SFCxGIXiRprCNFBYU2xXSFFt6dcU6pbkCkm7K8mk9y_ddLuHVcTmavJgZ-yaau_uF453ooSUvLZoefWgskjlrCisOdipuaJHOq-WMZCFHmbViRxXdvoNLm-z-xiMJBI75XSP8f6UbfqaDwDzf9CMdI6eeCE-RTDzjwkj5yL0d_YQvEFAUYclfoVfprk2r6ubpVPi1uhW-CQtSuPNT2d0IER23IRk6yJ5jOzzgt4B32VAx0QegAp_pBD-hzKPRiM7aEkF6FXHAmieR2REji48bUeFjeXZ5UkfqnX9MQKPjcUaKdjYq2pkr01eVAlh6uv_6L0S5KuxvDzXbCkmTybeXibWIJTSPeCCjKN3YoNTFFsk_Tk6PqIh6zn8d6FBh7AO8_8XjbIDLFNixAKJUyTAMf7Pl11yUII77H2mwSjHWnkY7mtF1Pn5DL17_hP9kgO0KPzBattccu8drbT0fQjK8fqwS4SayluTvSzSh2rmsxecfhqIASSC4rim4_zrmugH7c54cLxd72Y0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cf68d6ca.mp4?token=HItpdfBIiVPbIhHzFhkHOr5aTI52-xSXHup-oAR_yQbssJerNw-k_OWQ4XVk9lWrSMRG0U8CEZa5lK_tnByJ0IeuJlPgu4IITYt9uL55C--J6Y9fMrz7S2OJ49pwQy1udB0mCgmjrgcO3je0AIueP2CLMa5PPs9SFCxGIXiRprCNFBYU2xXSFFt6dcU6pbkCkm7K8mk9y_ddLuHVcTmavJgZ-yaau_uF453ooSUvLZoefWgskjlrCisOdipuaJHOq-WMZCFHmbViRxXdvoNLm-z-xiMJBI75XSP8f6UbfqaDwDzf9CMdI6eeCE-RTDzjwkj5yL0d_YQvEFAUYclfoVfprk2r6ubpVPi1uhW-CQtSuPNT2d0IER23IRk6yJ5jOzzgt4B32VAx0QegAp_pBD-hzKPRiM7aEkF6FXHAmieR2REji48bUeFjeXZ5UkfqnX9MQKPjcUaKdjYq2pkr01eVAlh6uv_6L0S5KuxvDzXbCkmTybeXibWIJTSPeCCjKN3YoNTFFsk_Tk6PqIh6zn8d6FBh7AO8_8XjbIDLFNixAKJUyTAMf7Pl11yUII77H2mwSjHWnkY7mtF1Pn5DL17_hP9kgO0KPzBattccu8drbT0fQjK8fqwS4SayluTvSzSh2rmsxecfhqIASSC4rim4_zrmugH7c54cLxd72Y0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میوه قهوه یا coffee cherry
برداشت با دست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/676080" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5691cab0dc.mp4?token=ApztiOsDY4a5kmJzcAQj1fYgFjsFnCEXzHaoeV_euMc2Xuxqxv42B2c_7fixP4FMBni1AUpLkWiel4ZfC8H-NcNilhrt8WoVahu6pIkLrKWhFsTphPoGm3XDZvhw7DlbQTY_6M-81B4t3jHn98-im3UbHqhAiHKltk-Q2ZwFn_NvpkKIDEH-I6U9h3K0Hf_tP3bG0r-WxnmKdQxCLAzEIZGefO2jha3gXSu4jApvnPpYgN7KskxIDd1-FEpWBWhxAHwDK8-aR5XObW77rED8o7VdP45Me-ILWMxKlBsz0Zb2fE9u-gGlcyyBzRZi-hrTjKA_SFUAo_WKqF56RS1sbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5691cab0dc.mp4?token=ApztiOsDY4a5kmJzcAQj1fYgFjsFnCEXzHaoeV_euMc2Xuxqxv42B2c_7fixP4FMBni1AUpLkWiel4ZfC8H-NcNilhrt8WoVahu6pIkLrKWhFsTphPoGm3XDZvhw7DlbQTY_6M-81B4t3jHn98-im3UbHqhAiHKltk-Q2ZwFn_NvpkKIDEH-I6U9h3K0Hf_tP3bG0r-WxnmKdQxCLAzEIZGefO2jha3gXSu4jApvnPpYgN7KskxIDd1-FEpWBWhxAHwDK8-aR5XObW77rED8o7VdP45Me-ILWMxKlBsz0Zb2fE9u-gGlcyyBzRZi-hrTjKA_SFUAo_WKqF56RS1sbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماینرهای غیرمجاز یکی از عوامل اصلی خاموشی‌ها هستند؛ گزارش‌های مردمی می‌تواند جان بیماران را نجات دهد
🔹
مصرف برق هر دستگاه استخراج غیرمجاز رمز‌ارز معادل مصرف حدود ۱۰ واحد مسکونی است و ادامه فعالیت این دستگاه‌ها، فشار سنگینی بر شبکه برق کشور وارد می‌کند. این موضوع می‌تواند به افزایش خاموشی‌ها منجر شود؛ خاموشی‌هایی که علاوه بر ایجاد مشکلات برای شهروندان، در مراکز درمانی و بیمارستان‌ها نیز تبعات جدی به همراه دارد.
🔹
شرکت توانیر از شهروندان خواست در صورت مشاهده نشانه‌هایی مانند صدای مداوم فن‌های قوی یا مصرف مشکوک برق در همسایگی، کارگاه‌ها یا سایر مناطق، موارد را از طریق پیامک به سامانه ۳۰۰۰۵۱۲۱ گزارش کنند. این شرکت تأکید کرده است که هویت گزارش‌دهندگان به‌طور کامل محرمانه باقی خواهد ماند و مشارکت مردم نقش مهمی در مقابله با استخراج غیرمجاز رمز‌ارز و حفظ پایداری شبکه برق کشور دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/676079" target="_blank">📅 17:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676078">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koENdkJ1ZiBqVusRg5j4fmhCHXXuhUgTAqujtxqVGQ20p1PajLZajOipIdctDTicd68Ktc4CRO0hy1-K9jHlNWvY9s4dp56-VAH16GXqCWb43XJahjVmxYQL3qnJHWCuTn3LkCxv5yRL4X_04Eqe8GLoJ_RxPNBZO9u0AKPUeHkGFWL_qkFCmHZyfseFW7rwBcv5OQYJdA7qz0fuhU8A12FFfrpsqWsSasri7OKmtzKqygW10dffQBckPVQML1jgeTVyoGdsIFlxPVf88a8G0QxlCW9DwL1xkiCcKHUr5SW1tQxnWSBXr89_kWWRXMN3lMVDqHao6Y_GoMxMzTN7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز درباره جزئیات طرح پیشنهادی عمان به ایران
ادعای رویترز:
🔹
عمان طرحی با حمایت کشورهای خلیج فارس برای مدیریت تنگه هرمز، از جمله دریافت هزینه‌های داوطلبانه برای استفاده از آن، به ایران ارائه کرده است.
🔹
منبع خلیج‌فارس و دیپلمات غربی که در جریان این موضوع قرار گرفته‌اند، به رویترز گفتند که طبق پیشنهاد عمان، ایران کنترل انحصاری نخواهد داشت و هزینه‌ها داوطلبانه خواهد بود.
🔹
این سیستم مشابه سیستمی است که در تنگه مالاکا در آسیا وجود دارد، جایی که اندونزی، مالزی و سنگاپور از کشتی‌ها می‌خواهند که برای تأمین مالی ناوبری، حفاظت از محیط زیست و عملیات جستجو و نجات، کمک‌های داوطلبانه پرداخت کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/676078" target="_blank">📅 17:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676077">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dacecfac.mp4?token=HwHuZozJnOLgrelEyK4hza3Kl9eyHyVQEUy79X8VQ5jLHLMbzbnZNsOkvxxWQMZgm9gEuLUagqEWI7sq7DJUhKcjHgUUv2MNBAFCIUfMeB6Ad855Dk12zouWZnZ5WRcGliasMb0WgalmInxxCpc1xeobLL7TbwhrumDnCLkg8P89qPKNuo_idIXaoalGaduo-46zq1bxj6XUZyDGzev06t6wr3PsDOgVxXgyyYHabLMCEt7beZybUmqQ3EMog2OuHFVi2qXfl5SEfhwG1DXYeYdCHf7Dn1swd2tWmCi431hAcMBaF_xXdT-S6a7UzbhOUCFojlvWnpvvKuQAwOtUOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dacecfac.mp4?token=HwHuZozJnOLgrelEyK4hza3Kl9eyHyVQEUy79X8VQ5jLHLMbzbnZNsOkvxxWQMZgm9gEuLUagqEWI7sq7DJUhKcjHgUUv2MNBAFCIUfMeB6Ad855Dk12zouWZnZ5WRcGliasMb0WgalmInxxCpc1xeobLL7TbwhrumDnCLkg8P89qPKNuo_idIXaoalGaduo-46zq1bxj6XUZyDGzev06t6wr3PsDOgVxXgyyYHabLMCEt7beZybUmqQ3EMog2OuHFVi2qXfl5SEfhwG1DXYeYdCHf7Dn1swd2tWmCi431hAcMBaF_xXdT-S6a7UzbhOUCFojlvWnpvvKuQAwOtUOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این پرچم، فقط یک رنگ نیست؛ روایت یک ملت است، خانه‌ای که قلب میلیون‌ها نفر در آن می‌تپد #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/676077" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676076">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb85359332.mp4?token=Sm8r-t4XMePq1h6HDoatY8wG-fIfrEVsJ2pYmZ3bPpkMMj_7GKgG6ABlD5KFaFFbr578_c03ZRVdQASNKXz5MaeuQ95b3UNdo29-8NQZ1TuSg7NiHzOgnk7OErz-I6hZ1zQ5aMNpixRH_NW2icKFfaDE8yQEDDVVQuhFCydJm_-6kgSof5K8avvxjUBoSkYgj-TfDivY71zdhaUoCqFNTlLrpg_H9eaEl1velwKwmC8rm4x3TMZwJFpZUbb53VmbfxVfwcnZaNWqHs_zTOLD8UkO8jwTeJYAV8e2fuyi2FTZK92OVVvollA2BDhMI3T1-beQNQ_yM_pOHGg9LK59eYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb85359332.mp4?token=Sm8r-t4XMePq1h6HDoatY8wG-fIfrEVsJ2pYmZ3bPpkMMj_7GKgG6ABlD5KFaFFbr578_c03ZRVdQASNKXz5MaeuQ95b3UNdo29-8NQZ1TuSg7NiHzOgnk7OErz-I6hZ1zQ5aMNpixRH_NW2icKFfaDE8yQEDDVVQuhFCydJm_-6kgSof5K8avvxjUBoSkYgj-TfDivY71zdhaUoCqFNTlLrpg_H9eaEl1velwKwmC8rm4x3TMZwJFpZUbb53VmbfxVfwcnZaNWqHs_zTOLD8UkO8jwTeJYAV8e2fuyi2FTZK92OVVvollA2BDhMI3T1-beQNQ_yM_pOHGg9LK59eYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گور آمریکایی‌ها در خاک ایران آماده شده ...
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/676076" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676075">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
کیفرخواست پرونده شهادت رهبر شهید انقلاب و شهدای مدرسه میناب و لامرد به‌زودی صادر می‌شود
دادستان تهران:
🔹
پرونده شهادت رهبر شهید انقلاب و خانواده معظم ایشان و همچنین پرونده‌های خاص دیگر مانند جنایات رخ‌داده در لامرد و میناب، حداکثر تا ۲ هفته آینده به دادگاه ارسال خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/676075" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676074">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRvGIMcNG3pIFq6gRfn73yRT4CRdgODWvYTPtHKFPthUXqfXNx370xuLDHP-lsFCogR77rZorGvScMq2BJo6l38bCCkoP2pbyWtE7bv1uSbNmPSI65xXijFdGslL_1OJeffY1aU0fkV1SdGYWJeSoHs3AfbTBCz2ag4McnnAqgIMqJkqKean7RMT8GDpUC4QmFqKVii5T13ro7uljbFHE1G8t-V44VviUCA7bAFspZWAIm74ePA2B86wn3-8my5CcyCPJq74tO8wfVXZl5h7qYsGE42oQ7D_Bo8b7cWsQNziWhMIO7xv3bO6Wrdbb9Fpgxx25PZt3EUgiR474hL1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
۱۰ گرم طلا، برای ۱۰ نفر!
🎁
تا ۹ مرداد با اولین خرید آنلاین طلا یا نقره آب‌شده از اسنپ‌سرمایه، هم سرمایه‌گذاری رو شروع کن و شانس برنده شدن ۱۰ گرم طلا رو داشته باش.
🤩
💛
✅
پشتوانه‌ِی امن و مطمئن
✅
نقدشوندگی راحت و سریع
✅
خرید و فروش ۲۴ساعته
✅
سرمایه‌گذاری حتی با ۱۰۰ هزار تومن
⏳
فقط تا ۹ مرداد فرصت داری
همین حالا شروع کن:
💰
👇
https://l.snpy.ir/50svu
https://l.snpy.ir/50svu
https://l.snpy.ir/50svu</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/676074" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676065">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtFpX-eyIWjvPI5qv1dQblnRHAAobFw7xKhQNpijezN050eAKGsyDT3EAZxpqVcftXq_ugoIGXChfoaVXnT01zTHN8KYtm_TvpLTPNhhLnwlt6TBOqB86QOZLDGmC5KYTLNNMCC-78ZmMmlRf24BbeGHVfWXPw0XynGbXShCrnVqrdZdWqATvl5Dzv2ohrKBMVJ9OHBaH1kLIRm_TKbIXxjJYa1vsgux9sjoYmgsa75VNuDpCcOLFwmi4g5UNpQJYNbN5y1yOFx5WAI65C4CFCB11SJovP66-4PZ8sPcltovgRnUkqFwiCrdl3SyskeArkdnRFLN-Is5kA22CAI0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5PQP5BYyy_0bX6K50Xb7rhLU0GBUJlWIxYSqbi0hKyON0yZPmPXTpswXIE-Ub-ruISR7Es-R-a948jmarLd7T1pE-1B5ngGpTRKMYbT2gKNbqKUm3BguR6cfEcyE-Gx16SNDMmBRSIeWEgJbIG5P5W2snIwT99P59YHY2uhL3wx2sM-4RKh93RkbimKKoww9S9J3hn3kJAI0Ruu4VqwchblkW8a1-IiIq8s1XsS4jPZIua57SkyksW5_0VhjzySARo77yzvJjFV_vl6a__c5LQhlIu41BY_VYpm28vM5aK1O6w1oGDGO2mZsFpFYNOjYDoPU63t0uWfyZujSmfaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hv6YsitITJbSaKUyCgHWfBSEkUFt37eM5HleJ0FE98nsA0Sg0asjJYoYzCmFV1ghsSil0B-tt2xf6-dM_jDj0JsBda6gmpGXwo1pl-bwmTIQdD8uy7x5v3Y7ZRrOF86f01XGZZ6d5uKDU_jyhNvNaY6IFs9FX-diDd8IRLmbfNSaZ8DDGhZbbVjemNwJShIR_zzwgIC4Zp1pRVocUQQobVpueKEqs3bgX9icXDYt0bJZA8ywZT-TdGvHTsE167iUUeqXVAl44T0F-HWNmTrVlGH7wayENd88YamoJ7klermFupYRgCNEH4Is1s5T34012TvFshHKTUXWAvau6yvZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amqcK62uQRJBPZxhn85aVRoLx8DtmEqzSawg0TrMBP91wdstE6sFZS79Me7KwMI3HBHGtolwhfBRC3YbXt8ZgnptU7eDP9y0J4-tccKZLFU9C4MpnvLeS0b53TAF-Cna-ohMDSlCF4AVfndlicslw8ucnGc1vPv2T7SpmWtXN6eMDoc3A-FUZa_pebF7AVoTMyeITYmfRg7I44FNaFfK_4wEhCvGndBfuopdztNVYfH-4llN-enNci5dEi2iG3WgVFoIY0kUfoF5uxxC5K0bXks6PGU9kz9nHgSgPsgsLWv3qtEN6qMV_IhytKHv06WwBW-iuruqBOz9CcrpcidXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aw_d_VUgE4KxKIkHXb2UtagrqX_MtHroWFoDDPHcsuA8OqtqlzYYumbmc-A5DTfQhDo3F91p2nNoBPpz5mJHQgEgTn5V-DDzO4_ia9fpSEX_7Sh1X0V7zYjGLHDS_RO_d9YOn9ctgBlub-f55Wbeol6kfQCgvcTxHMGxvJrGt2ur0mFUaIhMIkrMi7IgQ91JfkXVHBPGL5a3txWtSoFKHoAwDTCqEuTLe7tlbmLWd9ZjNOYa-yc6BlBUvfYJ7HnIsZ8izjdUHXUjrzXM-hS8l59MW_RhR1A55B2FVWbFZXWqvn66bPH1HRhIbobnQ1gFmi-hOomcOjVxbpaSl2Sk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKcPcuq0AIOxjAorsu4jh3M_sC5x5QaoaX8xJnrIJho9VVls8-RsmNchOYiRLL3mvg0kP44i7J7TTun5Uae_-zwc2WpxuOkIWxYSjCZGiMU3GXI5X1cE35r072Vi6JzKDjOY22RWamcTlV9lhOwEBEGHyqj0vdQgilLEMnpJ-uGjJoevgJdH8t5H3p7r9REj2GPhZalrz7LIBoUA4IQ99WGeWLNcwOFU1ABg7LllL9Tx79rVRY93utFdDbQeSIXtlDOq4CH76Hm67EIb94N_wlROf7SZcywhlvCSjau51dEMTWRegqdit0fHFoqHrMVsDxX-gxxhV9vkAEPtmyZ4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGBe9Dz_l_W6jZtqaCDz2gqqAZUGHfR_iGzzI5CKOOqa-1qdiWpiE3jTR1D9kx2oIYMqeKM7Vc0d17CKgnNBpRHGwhkoMRsiGeNYQyH9kT3wiyGsNLyjcHZNNDb0e93c-la_gUA2G_-es_o8hhL36aFJAWhGrv69X7NRccprnYS3Lx99iGfsMBtZZAXbeu1-Au8612hL4YENMjPeUqa2lk5ewd4QIxaOywKAK9ZzgjNZS-3IDX4mF6Y7Iw8YQoKKVAJPhJvlUHVs-QjqLUg8lEF7iYqy_DegjiKIy1Gtj6GT6EgBT3vJk4WyZPbKMOS8r6v3chiiT-Y-Ez5P8tDl-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pb-BQ42nKPwlKkUl-sSBSnrbk3uLX-lz_6YG1cRj7v9-NoCGTqKuvHo4uAIl9ghqhjKL8TJsVH4WBITK-Q3m0ZnXJCZzZ4issSW0384JXaczc5nA6j2NM_lgPYMxLkWk23PLVPaSNcNK1GpkgvrBrTWJyYfqU83V1UgodcO-9Vs_sxsrEQFczIttheu7BXsaCWut9usl5f-mDJu0UugU4bK1PqdqtYiio9D58u17PTSblp4IHSoRG7dpf7hT3WJDfIP1_lEvo8M2y0Dc6vMOwPuRz4_MkEM6TrnpRqas4nOQn8H8S7k7hUyu8vGASDdZ73DaIgBOZb9lrmwFNLWtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMzS1m7F00Q0NMxMskYXpp1OVdo8hqJo1sRTu7jvJA8kby9myq5M_LyxUyQHsDUczasp7M7uKig1aydSJ6MEa8kpP9HGp_kZJzlgKBUmyWmw589pO7v0GN-6yIoL6knN2zTvvtE1GIVfcEcI_Zi9fyio757E0N-E9QCgeWJf5r1OWS-n_AU6-Yh95qFjsdipwm8zH36S8F-BlM70ca5Iex_V-6hmccNNbe_Z6aay-ECh1gCZfJCIsxroVVHNp-TnHskgAou2pKgo5Avjru6ndE33CxX0FjaR7WUbMTmQp4eh22Pa3jG9K0hJmIsrh9-SC8laijjkiBhM_dqZz7AWuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۹ عادت ساده که حافظه‌تان را چند برابر قوی می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/676065" target="_blank">📅 16:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676064">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سی‌ان‌ان: اوکراین به کشتی ایران حمله کرد تا بگوید ما هم هستیم
ادعای سی‌ان‌ان:
🔹
زلنسکی این هفته برای دیدار با دونالد ترامپ به واشنگتن سفر می‌کند.
🔹
فراتر از حملات آخر هفته اوکراین به خزر و کشتی ایرانی، زلنسکی گفته است که بر اساس اطلاعات اوکراین، روسیه داده‌های ماهواره‌ای را در اختیار ایران قرار داده است تا حملاتی را علیه تأسیسات آمریکایی در خاورمیانه انجام دهد.
🔹
پیام زلنسکی این است که ما در یک جبهه هستیم./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/676064" target="_blank">📅 16:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfdreEfGesCeQBuctxkydTyQsxX1JbA81wdGPxBhdwaZ3xEBYnH354SkFdGVNytGYfuLqbtpUHf0CYrZMMMjNIZcd3jgb0MraZAYPlI_PKpqLt38o6LctRbHEe9xAwP93qppb3KUAHm_k-AHMIlPpRx2GhSGerghoVuc9THLYAn2PiX2wCEVFMfzpavhbvbZWZQhzTuMjlTnWwsoDPK06pOPioaFIrC8IBk_qGBMsAzVCRJc6g5po3efjZRsoFrd8FwoEz29mToMEBk269LaXrfe0cRaAaB34DXmlE2p4LejihfLk-rZ5W_fuJU4cOYV8aDEUjvoi6DmNeu7TnpqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XTBMIO3UBgCEourJek5lV06IkRVkQTF7-Att3MS9q84GVHs6CWmG2fG3qhDn_TNXFhFtexYqDhRRX_xZskzs2lcGP1IOmeLwUN0LkPqKnTZ_YzkWrBd5SUcK0Wn-7tW8eR8JNKU5-w4tjCnzj39aXEvJ5LbZo3gvHIwycmFBbSMB5YSKh2Kp6Vla9EKSddUC-SeGqNwOqQMO8PpuLRrDoXRUu0C8b7k-MvJib3hdrYFM_Xgv1ZaNdoTk7nwoTQ0zpNdBsnrmYBvaphzsTtypzTUaLbds1ZU8N6RTtHz5SP-vS1pq7uIW3lxcxn4MT8b-S8SWDR05OaPJ4PYOR3lmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrtzyTxwMahU9Kqje7cjnChz1IPyQrUYQaECbYfrpcsWM2v0Ipvuuyl8XsDP5P92GHNeQjT0kb_Q8BbXLt7W-9nWB_MPB_8Ub4Hrdt2juuc3fjhYnXR7VPzdQFeuO73HgLE9OdeCvg8Pe4Lw9In2dTCYX_5NSm3nHcgtBfGfRaEogCIR_cuvmJQ76Y4UD60yD_-a0Jy4ls2t4KXK3LYVo-ad4k_KHjQTBH3VBEfld9UEUFDDrW85lqul39xhS0ziTEbmNpMJ4UUGUCTkFL_3p0ZKygaTcoZXjcVVNzW58lHuKO4iBTb_3HsUx9Vcn8ZBx3KngC0CjwxjLsFoCrNwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0UQtNzYqv0Z-gf0Q0PEt4uTGkW0D_xreSXXp5AFxT2-C-3G56sE5uRtdxFelh0MLuWXZMzY57vqv63n7YpuwH0pjADiwcx8X1DZngJkPFCpmN0vFbz_CJJN-Rqqh6tLf_3wKRlwdfO1Jfi4Y4g5446o0QJ9e8lLRDIOoo0-LskOpFqyQCtu9NqKvVfY9nN4f-b7VI2aMJmZRk6bDInXOMXi0zhGuT85awFeiSqMcx08nOxLQ1VAgMWeJrCaJFxwkeAUI7p3AlCdclltx-eeJpqSSs1tWwzxVZFivltO2aqKUXEJo1aTzUsmhEEdmOxHP-65U5HDFgXvKdZd31EBtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فکر چگونه ایجاد میشود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/676060" target="_blank">📅 16:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676059">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✨
تخفیف  ۵۵٪ ویژه هتل مشهد
در گروه هتل‌های لوکس درویشی
🎁
هر ۴ شب اقامت = ۱ شب رایگان
🏊‍♂️
مجموعه آبی و گیم‌کلاب رایگان
💆‍♂️
ماساژ رایگان اتاق VIP
🚕
ترانسفر 24H فرودگاه و حرم رایگان
⏳
فقط تا ۱۵ مرداد این شرایط باقیست ، همین حالا تماس بگیرید
📞
05138080
‏
🌐
darvishihotel.com</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/676059" target="_blank">📅 16:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676058">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نخست‌وزیر عراق وارد ترکیه شد.
🔹
نرخ تورم در ۱۲ ماه منتهی به تیرماه ۱۴۰۵ نسبت‌ به ۱۲ ماه منتهی به تیرماه ۱۴۰۴ معادل ۶۱/۴ درصد است.
🔹
پیش‌فروش بلیت‌ قطارهای مسافری نیمه دوم مرداد از فردا آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/676058" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676057">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=OrVGj_Z2jSDfX2MPyB9BGWB5y_2ryTCuuGP4jBMAk_ik0HYsp4aOnVW2MbgJuAPHJGnNHPunwF_tNdQnHLoYTuAwwMTldlQsp0Ma6RxA6Sl2B2pP6zKQVPoy-f-xPuYLXBxkLy_88AC3nwEBRu6Otv8Ax7PbAkr2OOWrU7WLkoN_sBAOS8XPOhp_kU2_pevreP1qcwA2zCqzJfi6RfmFkRUwXwXekVloJGUiYDdgeScVkLysYkrlxz314YhL64mBGIrK5xu_iCRe-PbFFsCQXBPek7xGuSS37oTtrmB4Ze6VqObajgXgOroFYRUl1EMkR2Nlly1iLEYK0YOvDhWC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=OrVGj_Z2jSDfX2MPyB9BGWB5y_2ryTCuuGP4jBMAk_ik0HYsp4aOnVW2MbgJuAPHJGnNHPunwF_tNdQnHLoYTuAwwMTldlQsp0Ma6RxA6Sl2B2pP6zKQVPoy-f-xPuYLXBxkLy_88AC3nwEBRu6Otv8Ax7PbAkr2OOWrU7WLkoN_sBAOS8XPOhp_kU2_pevreP1qcwA2zCqzJfi6RfmFkRUwXwXekVloJGUiYDdgeScVkLysYkrlxz314YhL64mBGIrK5xu_iCRe-PbFFsCQXBPek7xGuSS37oTtrmB4Ze6VqObajgXgOroFYRUl1EMkR2Nlly1iLEYK0YOvDhWC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خانم الانبیا: هر شرکت و کشوری که از محل دارایی های ایران مبلغی دریافت کند اجازه عبور از تنگه را نخواهد داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/676057" target="_blank">📅 16:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676056">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
خوک نجس به فاکس نیوز: نیازی ندارم که نتانیاهو چیزی درمورد کوه کلنگ به من بگوید. نتانیاهو این چیزها را می‌گوید چون می‌خواهد من همچنان درگیر ایران بمانم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/676056" target="_blank">📅 16:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676055">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خوک نجس به فاکس نیوز: نیازی ندارم که نتانیاهو چیزی درمورد کوه کلنگ به من بگوید. نتانیاهو این چیزها را می‌گوید چون می‌خواهد من همچنان درگیر ایران بمانم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/676055" target="_blank">📅 16:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676054">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
خوک هار به فاکس‌نیوز: دستیابی به توافق با ایران بهتر از ویران کردن باقی‌مانده‌ این کشور است. اگر ایران با ما به توافق نرسد، دوباره بازمی‌گردم و کار را به پایان می‌رسانم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/676054" target="_blank">📅 16:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676053">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ff15358f5.mp4?token=YcHc2hhxtgOr32BL9ALKwAj7Ch74jwo-3W-535G-FdUG-cMjumAbj2nV3ODT-th96RXmfWI5criPaF6bbbp07EVA8wp4Pl5zL1XMMPe0EWGcAbAI2DuT-YFJeLxTcaIjMoOvVO0f93UAZDFKxxfOdoPQy8iPzA94kj5G7rn1JIbGxiJ_fGzQzpYFryrVi0EMXC8lvD8J9gHkVIkKWbaQ7LnDo31Z7A_CQxFoCGzVAWDeifElgd13lS6Xmo-FGS9rMg7xSggLPa4U8pMKqM71I3GM92aMsiUUvxLDqxTCfYzrBqOczsm25P6kAzanAA5t18XcSOc7Cj0FxWj1hq4y5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ff15358f5.mp4?token=YcHc2hhxtgOr32BL9ALKwAj7Ch74jwo-3W-535G-FdUG-cMjumAbj2nV3ODT-th96RXmfWI5criPaF6bbbp07EVA8wp4Pl5zL1XMMPe0EWGcAbAI2DuT-YFJeLxTcaIjMoOvVO0f93UAZDFKxxfOdoPQy8iPzA94kj5G7rn1JIbGxiJ_fGzQzpYFryrVi0EMXC8lvD8J9gHkVIkKWbaQ7LnDo31Z7A_CQxFoCGzVAWDeifElgd13lS6Xmo-FGS9rMg7xSggLPa4U8pMKqM71I3GM92aMsiUUvxLDqxTCfYzrBqOczsm25P6kAzanAA5t18XcSOc7Cj0FxWj1hq4y5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور بعضی از وام‌ها به صورت نامحسوس بیشتر از سود، ضرر دارن؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/676053" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676052">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی دو تن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه سال گذشته اجرا شد/ میزان  #اخبار_اصفهان در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/676052" target="_blank">📅 16:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676051">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
یمن به عربستان هشدار داد
🔹
صنعا با محکوم کردن تهدیدهای ریاض علیه عراق، اعلام کرد در برابر نقض حریم هوایی خود پاسخ می‌دهد و این اقدامات بی‌پاسخ نخواهد ماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/676051" target="_blank">📅 15:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676050">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
نتانیاهو نخست وزیر رژيم صهیونیستی وارد واشنگتن شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/676050" target="_blank">📅 15:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676049">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
برگ‌ برنده‌ تنگه‌ هرمز را از دست نداده‌ایم
جعفر قناد‌باشی، کارشناس مسائل بین‌الملل:
🔹
همچنان همان شرایط سابق، بر تنگه‌ی هرمز حکم فرما است.
🔹
بخش عمیق تنگه‌ هرمز که کشتی‌های بزرگ می‌توانند عبور کنند، در اختیار ایران است.
🔹
در بخشی که عمان در اختیار دارد، کشتی‌های بزرگ قادر به عبور نیستند.
🔹
هنوز تنها مسیری که ما مشخص می‌کنیم، امن است./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/676049" target="_blank">📅 15:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676048">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
زلزله ۷.۱ ریشتری ژاپن را لرزاند
🔹
زلزله‌ای قدرتمند بخش‌هایی از ژاپن را لرزاند و به‌گفته مقام‌های این کشور، در برخی مناطق قطعی برق، آتش‌سوزی و خسارت به راه‌ها و ساختمان‌ها گزارش شده و بیش از ۱۵۰ هزار نفر هم دستور تخلیه گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/676048" target="_blank">📅 15:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676047">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGdQ0-3wmZNYwiT1K25_NStEW9YErIxXw2dj9boA7-TrFYG-um48gOb8lIaxtzN8ciPXoTXlE5310SeAxF-Y8YWm2da9Xvv3uuzmT_0iwkPZ8Gc3y9NT6TqNlY00RijpNTur3yANaNVFzxsgWOm--g2-emfsQQgKHd4tLK8Tj2TzFsnG80iv7oJqtP_FSDhHzZeISmPv4PZUemTGtTpsZ3vavOvo50fSg9S6CGRB1r5Ruov6U1sARZLP245u1x8gOxFhoYDTb00z_6lbRx2EPj3yDLIgn-B7UDQHtICjnD9rUa5L8Q7cjeSQ2QjnPE2GwShuQojPmo59wq9W0d2WyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام بسته ارتباطی اربعین برای شما مناسب‌تر است؟
🔹
با نزدیک شدن به اربعین، انتخاب بسته ارتباطی مناسب به یکی از دغدغه‌های زائران تبدیل شده، به‌ویژه برای کسانی که می‌خواهند در طول سفر بدون نگرانی از هزینه‌ها به اینترنت دسترسی داشته باشند یا با خانواده و همراهان خود تماس بگیرند.
🔹
مقایسه بسته‌های همراه اول و زین عراق نشان می‌دهد برای اغلب زائران ایرانی که به اینترنت، پیام‌رسان‌ها و خدمات آنلاین نیاز دارند، بسته‌های همراه اول انتخاب کاربردی‌تر و به‌صرفه‌تری است، درحالی‌که بسته‌های زین بیشتر برای تماس‌های محلی داخل عراق مناسب‌اند.
🔹
همراه اول بسته‌هایی با ترکیبی از اینترنت، مکالمه و پیامک ارائه کرده است. در میان این گزینه‌ها، بسته ۵ گیگابایت اینترنت با اعتبار ۱۴ روزه و قیمت ۸۰۰ هزار تومان، برای زائرانی که در طول سفر به اینترنت بیشتری نیاز دارند، انتخاب قابل‌توجهی است.
🔹
در مقابل، بسته‌های زین عراق تمرکز بیشتری بر مکالمه دارند. برای نمونه، بسته‌ای شامل ۱۰ دقیقه تماس بین‌الملل و ۳۰ دقیقه تماس درون‌شبکه‌ای زین، با قیمتی حدود ۶۶۵ هزار تومان عرضه شده است.
🔹
زائرانی که بیشتر از پیام‌رسان‌ها، مسیریاب‌ها و خدمات آنلاین استفاده می‌کنند، باید حجم اینترنت را در اولویت قرار دهند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/676047" target="_blank">📅 15:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676046">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادارات کدام استان‌ها فردا چهارشنبه تعطیل یا با کاهش ساعات کاری فعالیت می‌کند
🔹
کرمانشاه: تعطیل
🔹
مرکزی: کاهش ساعات اداری
🔹
کردستان: تعطیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/676046" target="_blank">📅 15:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676045">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5MBKmncn3qz49qxnEvt8QXzTCtXuoNbTJk-sNFX7yfNfcp6cNiHC7Y47Jm-qWqmw0ACUT-EbpOJyvnGgjvH4QJY4vNOIoz4J-k7zRcY_3M27vdrW3a2o_lThjkFmXqLc0W1MldtTq-oLcq4ysHpjadiWxxTWjVHJ1Fade0HhMjqbKSiWjZy0nAJ-4IAc5iiRaoHVBZvZSZ9WczF648AKrd4SSudPk6e9QkaYolrjen-4uG2idYajRpbb1DHHZX0XOf7rpdSMbdXhCPRZa7U2Z2ZUO8vJn0xF7oJKFNsoy55W9atpbHD0mMrPXlp4MyvUS0ZqqiRGBJBy4p4DuzP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت ۸۷ دلار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/676045" target="_blank">📅 15:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676044">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBhAa3RRWBS0clYgAoTNo5TzVPxA_FE2skP-udNeJTk-a3J3wuQ0WGgjDe6zwrCAUZKOMwdeIj75t8tbeHvNNucBmx8qbQQi_qB_asq4GlWtCv9o4IDAMUNk7XiG8_BXPjZQZmFR_j7FTUg6IbJmqH3qGl3VkJxAE7-E7j81TDIeutUr3TfXSPgDs8B1TZyShxCuJrxl59zwFJrjRPsNWtYZcNHsiPsm9C3YPshG3GUdf9sgNcS_7xRScTZzvd1Ok1t7tTCORdzp8nR3lAuYdTI9IeqQtacHjZx-46dnaanJLzNmRPxHnXq4bXipBp52UOIwFg8GqwFAgfmTp7VRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
برج ساعت حرم امام رضا (ع)
حرم همیشه نزدیک‌تر از آن چیزی‌ست که فکر می‌کنی...
یادگاری ماندگار از بارگاه امام مهربانی برای خانه یا هدیه‌ای ارزشمند.
💰
۵,۷۵۳,۰۰۰ تومان
🛍
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/676044" target="_blank">📅 15:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
امارات به دنبال احیای کانال‌های دیپلماتیک و اقتصادی با ایران
فایننشال تایمز:
🔹
امارات در حال بازگشایی روابط دیپلماتیک و تجاری با ایران است و همزمان همکاری‌های نظامی خود را با آمریکا و اسرائیل تقویت می‌کند؛ راهبردی که نشان‌دهنده تلاش ابوظبی برای کاهش تنش با تهران بدون تضعیف شراکت‌های امنیتی خود است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/676042" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676041">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تبادل پیام ایران و آمریکا ادامه دارد، اما بی‌نتیجه مانده است
🔹
به‌گفته یک منبع آگاه ایرانی که العربی الجدید به آن استناد کرده، طی دو هفته گذشته از طریق میانجی‌ها پیام‌هایی میان تهران و واشنگتن رد و بدل شده، اما این رفت‌وآمدها هنوز به پیشرفت یا گشایش قابل‌توجهی نرسیده است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/676041" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285d386062.mp4?token=NcXh8ko1FHchy4Z5WwGlt0lEd0rJqrYrxhuCNnD0i47KyItqUZuFdog8RXGYUMH7T130Jk0C5Wn8dUdAb1IlrRJ3-ZSX1FGyB_29wAUSDriFzEfFQSS4MQwOSr2KBd0LP6XKMs7AbW4yF478dh_Z49qYvnJi1TijDITvUEO0qcvkIizP5bzpAiZ7Zo1kzm8V04R87AwMVeb4sQPlzq_Ebao2ndWjzz-KJtz3yeaiHjSiRux2M34wR5eYG2k5C4zlAB-74HK6wdtfDQrv-vMYp9bX22Mk8rAppwxTxcW45_LLbEvSXY6B47KPh1b_umnLL2-iuFYXkl2fQihqH_DTkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285d386062.mp4?token=NcXh8ko1FHchy4Z5WwGlt0lEd0rJqrYrxhuCNnD0i47KyItqUZuFdog8RXGYUMH7T130Jk0C5Wn8dUdAb1IlrRJ3-ZSX1FGyB_29wAUSDriFzEfFQSS4MQwOSr2KBd0LP6XKMs7AbW4yF478dh_Z49qYvnJi1TijDITvUEO0qcvkIizP5bzpAiZ7Zo1kzm8V04R87AwMVeb4sQPlzq_Ebao2ndWjzz-KJtz3yeaiHjSiRux2M34wR5eYG2k5C4zlAB-74HK6wdtfDQrv-vMYp9bX22Mk8rAppwxTxcW45_LLbEvSXY6B47KPh1b_umnLL2-iuFYXkl2fQihqH_DTkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلزله ۷.۱ ریشتری ژاپن را لرزاند
🔹
زلزله‌ای قدرتمند بخش‌هایی از ژاپن را لرزاند و به‌گفته مقام‌های این کشور، در برخی مناطق قطعی برق، آتش‌سوزی و خسارت به راه‌ها و ساختمان‌ها گزارش شده و بیش از ۱۵۰ هزار نفر هم دستور تخلیه گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/676040" target="_blank">📅 15:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU80t5E2QyxWxH8ItDMtnJKdVA0o5YREcDQXD_elkon3nRoL6xXfWZG243YWwRaU1cc2YY5jfltAY9JTKbwH-BJngHRY9IBOhkz5AEHDWcygVEATXQa2W06zj9gqi01VSuP5YtusGiHRo-cqqdBgwJs3OleeWJcAHkQy6IHGvIjIyyGE-mBI_BLX63CsV_EPj2CF2lO18_eopjxVbC5ktQTCiFn9g-5f6HqdYwK4Q_3JGgODFd0NxpA5aiL8n7SAtz5U2TJY2K7pgeFVDMn3CXFGse5GOtdB3IlWI9YAXmqUU_-G-uCTQ9yCmYUZi8XWk6xqayM2HwlRavUvN9ig-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آپدیت جدید و جذاب اینستاگرام؛ اضافه شدن یادبود
🔹
در آپدیت جدید می‌توانی یک نفر رو به‌عنوان «یادبود» انتخاب کنی تا بعد از فوت بعضی کارهای پیج رو انجام بده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/676039" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676034">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arLda7LH83pCa3KvCeSdfIeWWD-ur9K2JhlHtMP_ecLcPsihT2HywlcJv5rZ6BgX4ht2wlCDLSvDcb6qp2R98_CfBo3W8ynLWXRd_7RM2Wrbdv5D98RxPrCMdaMGAPXghYo0a8tQpJ4ptkJ4i2SuWZCK7IkLaWPxYeWjjJeVxdAHfZG8M473f6kdetbj4gaz-p5hdoi-Zgxiq7G-qb_42g8wE5bJj64ZoZ3uXBC6-9nwqqTXABeqyf2ePbld052sHzWHUjAiS0-_vd5pnv3ZLvwEGRtqGBpVbCw9IvF-w8c3XQAYdXiSGDWsYbB_LRMpFZF1Qo5ti8XzoQLbjiD_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UN4zukuzh9pOy5unC36_1jP_dTWCOQgQ9Z1iP-GG6t7UB0w5ZrW_X_2lysv4DIRE8HLdYcSYCIFTUHOeNKB_UxE2ONoUa1nnvLdos97A9vNhmFdxNNz2OmPsW4KBzyPsjwRVPhcFH5wvgK-HyTS_eiXUi8cLEi8ftkU1vW9JspY1HH2t7tUOddaXKKOo3po_Kpa9-3VqJGOmaB9oBJ_gylDtgCM7LSktKBM1BkH_mHtb0vWAk68dc8pvB0GkQ-yB-QwPNvrWHArQ3Jpp-nsjyHP_LOZsQfJQbkf8zqohfIvlypQ7dEA-1L-yFwY55GxPjU5jAMaf25HHCOYDlsyv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjsbvF9lWWOmcaiUmnMq_PfjUtJC3K8JkuH_LURpKvn4N4y9jpZvBE3CPmBK0QeT2xdbme-vXQpsdgsUsMCiItWnmnsSqx4awm_5hWKyprhem8EEK4n3DLyaV9XN5o4hEVsYgza4OXnCY8-85mNW5HyGYNT_hjadGyMToxvBUNvBFpPYR_TSTlinMLSopLWbD3Vp058APJE9Lz7BvNk7rJmwNXk1ZtTH3Ji-Iv-xY5y54iXOP_AQwKXaOyzNJ1f3-6e2pM_blxwqHt5mbhFMowr_9SuN_dNtZITjDdPGU-bFWFhyu215_O0UoNqyzOIEr5is7Yp4TfLXO_Bcxrfx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lz8H-ePBoBZ4JdpWCmxUF1phEEtHqLXgRcdyHtaknFLLKQUNUKF4sUr-b8CHUIvNbPZk1eebpUHdvoi9VG_sjViuepj92kmXcXlC1OcwfyqYdVvcF4fq13O_1Ucl1SVt43aWBYIK7QsGij-174PITUqXsUcV8tMpL-S9Q0M4Ra5m-MdVP7o7Skp1L_l1Y_MX6pVD2Z831hIZG3AQqh_hZC8jrcfMXAIBV1y8Zd5cnw-7ddIUEIjZBELrnTSRls8BBw_xiD0CmTF4BSye-nPWG5_8LT3ozXoiY3wvQSk5sc_QXhd0t_ZXHw-yB1I-VwPUqHIa9w7A46-9nVhRYtrarA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y84Oa6s4kCH5z2CYbkz1H420kxQ3wbPEEUpINUJsehBklTuTXswr1wZuuJgcVKCKJpSeXOGi8VFmwrOAYzuZviHE1jAJHURSAjv6o19DC1zjHr8CHI7_SllMh-HBEqbX5tn6mTPXWog4Met-AxlYzl0mCElITl0y8twJ0f05QzlkEKoykylOD33vKxwXVIDVravAV7Vxdpyu02OZNoDeGo4Cz6jYJ60H991vA3DKw4R8zYumURJlO7oJb9qRVoEer0Q3YBOAvXWVrgoP8YQX1VYPz6T58mcLbVALqJlqiAlmGvLXS0sI9mcm5oEaefNpG45Rtfddhu01Ci6lsFgkrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشتگ
#یالثارات_الحسین
در شبکه‌های اجتماعی ترند شد
🔹
در آستانه اربعین حسینی، کاربران شبکه‌های اجتماعی با داغ‌کردن هشتگ
#یالثارات_الحسین
در شبکه ایکس (توییتر)، فریاد خون‌خواهی سر دادند.
🔹
این هشتگ طی روز جاری به یکی از داغ‌ترین موضوعات شبکه در میان کاربران ایرانی تبدیل شد و کاربران در محورهایی مانند تبیین ماهیت اربعین حسینی، خون‌خواهی رهبر شهید، بیعت با رهبر معظم انقلاب اسلامی، تأکید بر وحدت جهان اسلام و... به تولید و انتشار محتوا پرداختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/676034" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676032">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4cdd20aa.mp4?token=joyUGCfn_eTrdqaz3hgAgvUuKFWirsPQpnhbMla-MQkLx1cCmb57UPa3eAJQaHniGQj5VQiCp5ACVwRGqBtpewVJOsGmRsK9ViV8qSpo900mIzrrP384MBCgZLfLexNdBNd-DHRrbmvYoVVgI5KeWOoTLqDAKnfuS17DjWejESqqOY0mw-Q49-tlEJL2G-t-34SBOLCOCnG2B88W9-vfdn9YRR4NxJtXTBeHEDS5ophd6X1o0j3Ea7hNE_2hzvlR7zDQ-WHCr04H0OMYrQbZDqn_oFp9MY49l7ixFMEXGE-1khNJ6CNHEn4-pwY4Uj9JrSIQRZPqPwT-cDK29LDzRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4cdd20aa.mp4?token=joyUGCfn_eTrdqaz3hgAgvUuKFWirsPQpnhbMla-MQkLx1cCmb57UPa3eAJQaHniGQj5VQiCp5ACVwRGqBtpewVJOsGmRsK9ViV8qSpo900mIzrrP384MBCgZLfLexNdBNd-DHRrbmvYoVVgI5KeWOoTLqDAKnfuS17DjWejESqqOY0mw-Q49-tlEJL2G-t-34SBOLCOCnG2B88W9-vfdn9YRR4NxJtXTBeHEDS5ophd6X1o0j3Ea7hNE_2hzvlR7zDQ-WHCr04H0OMYrQbZDqn_oFp9MY49l7ixFMEXGE-1khNJ6CNHEn4-pwY4Uj9JrSIQRZPqPwT-cDK29LDzRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبیین آیت‌الله جوادی آملی درباره شهادت رهبر شهید انقلاب در راه صیانت از اسلام و قرآن و اهل‌بیت(ع) و وظیفه امروز ما در قبال رهبری حضرت آیت‌الله سیدمجتبی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/676032" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676031">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6502e21a57.mp4?token=O7EKYFo-wFh6vo9x_Zt7TFK9j4luA4I4w3dfPobkzjCiEhvY-05vGDaHkrMKxzytptaVddBUOLpZpEF6zt8Dj4RTyMFGVlqF4oTU87eM3HwYPqoKLkDmRz8GFFLrzhq_gZRjvIRKp5W0S_V6qJD0sEE85GiN_FZaVtub1TC2_usMDg8CWWNNgbuvve3CiZPLJunhTauhu8bpjXYUEigcg9yn4l29Ke6IrfFDeoTJfAC06dBg-z_bjIr-gw7tC1xvoKBqE4tZ2Kq5TCFZOTYs9QHfKVcc1drTWRo0YnYzatdI_5MI7hpMo5h3PxanY_OgBQw68uTcAV0m5x5jcXZ3SWqUkBI5pXOuhiOO_eXemzuZSe9um-nHYey_CRNZEmf4iTRFDEpseu2hO0_roVIOZmI49cxIrUJHRWolHuaAUJgMyw_v4J1WsMULTyTOZGnUF6NxB1yTin73UKpZz8qSQsZ2f3w7cqGyrBToh-rURl-mqtMY6foDu2uNvwdwHj88Oows1ogo5I5BboXDMcr-iHMFlC8Ak1lIvIalCIVu_80fYkoxYqDY-wOT3Rfd4CF4aeRK3rSMzpDJbJ5-602U2228oH5QnJdbWKVL5V2vpIn_lo2hDQv2XRpGYJXzt9XjcFsCiGAi75uh561nujes7U-UXtvrgmR-lU5w3QDJXME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6502e21a57.mp4?token=O7EKYFo-wFh6vo9x_Zt7TFK9j4luA4I4w3dfPobkzjCiEhvY-05vGDaHkrMKxzytptaVddBUOLpZpEF6zt8Dj4RTyMFGVlqF4oTU87eM3HwYPqoKLkDmRz8GFFLrzhq_gZRjvIRKp5W0S_V6qJD0sEE85GiN_FZaVtub1TC2_usMDg8CWWNNgbuvve3CiZPLJunhTauhu8bpjXYUEigcg9yn4l29Ke6IrfFDeoTJfAC06dBg-z_bjIr-gw7tC1xvoKBqE4tZ2Kq5TCFZOTYs9QHfKVcc1drTWRo0YnYzatdI_5MI7hpMo5h3PxanY_OgBQw68uTcAV0m5x5jcXZ3SWqUkBI5pXOuhiOO_eXemzuZSe9um-nHYey_CRNZEmf4iTRFDEpseu2hO0_roVIOZmI49cxIrUJHRWolHuaAUJgMyw_v4J1WsMULTyTOZGnUF6NxB1yTin73UKpZz8qSQsZ2f3w7cqGyrBToh-rURl-mqtMY6foDu2uNvwdwHj88Oows1ogo5I5BboXDMcr-iHMFlC8Ak1lIvIalCIVu_80fYkoxYqDY-wOT3Rfd4CF4aeRK3rSMzpDJbJ5-602U2228oH5QnJdbWKVL5V2vpIn_lo2hDQv2XRpGYJXzt9XjcFsCiGAi75uh561nujes7U-UXtvrgmR-lU5w3QDJXME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
این روزها با قطعی‌های برق، داشتن یک چراغ‌قوه معمولی کافی نیست!
🔦
چراغ قوه دستی ۸ کاره LED Torch
هم چراغ‌قوه است، هم پاوربانک، هم ابزار نجات!
✅
نور LED پرقدرت
🔋
قابلیت شارژ با USB + استفاده به‌عنوان پاوربانک
🧲
مگنت قوی برای اتصال به سطوح فلزی
🔨
چکش شیشه‌شکن اضطراری
🔪
تیغ برش کمربند ایمنی
🚨
چراغ هشدار برای مواقع اضطراری
🏕
مناسب قطعی برق، خودرو، سفر، کمپینگ و نگهداری در منزل
❌
قیمت قبل: ۱,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
قبل از قطعی بعدی برق، این ابزار کاربردی را تهیه کنید.
https://memarket24.ir/product/brief/30291/180124/</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/676031" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676030">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0728305c.mp4?token=J3ksSUsuc3XTeCjG7kTFwRop03fEiv3OyKQEbkhRskAA9-rHwURb7s_NVMDPcpwRxDb5VzKoYZ9ncHKRmK19zuZNE51wquRmveBgmVMiaDP6fKYZlPGurh0nJFI7J03teZvcZwQ9l2kiaGLPT1TC4fjlVrASVvKfaZnWTfq899wjH5BEZaVtaHB0L9jy_YAE3qRrZPLtE0bsj0VpzFEOl1SrnZpIPSf_Ni3yfem3oqWAcd_hd9S3FUcCf4Bh0k6bFSE6euD_WvdUIh_SY8P_zz5zR5xr1bdcAurTY8izimyZqKc6-nK_a1IygBxQWb2-yqy9KDEeFFl3-803VRdBoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0728305c.mp4?token=J3ksSUsuc3XTeCjG7kTFwRop03fEiv3OyKQEbkhRskAA9-rHwURb7s_NVMDPcpwRxDb5VzKoYZ9ncHKRmK19zuZNE51wquRmveBgmVMiaDP6fKYZlPGurh0nJFI7J03teZvcZwQ9l2kiaGLPT1TC4fjlVrASVvKfaZnWTfq899wjH5BEZaVtaHB0L9jy_YAE3qRrZPLtE0bsj0VpzFEOl1SrnZpIPSf_Ni3yfem3oqWAcd_hd9S3FUcCf4Bh0k6bFSE6euD_WvdUIh_SY8P_zz5zR5xr1bdcAurTY8izimyZqKc6-nK_a1IygBxQWb2-yqy9KDEeFFl3-803VRdBoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ وقت در هر شرایطی بد ایران رو نگو
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/676030" target="_blank">📅 14:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676029">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
پشت پرده تکان‌دهنده سریال بامداد خمار!/ فیلمنامه دزدی از آب در آمد؟
🔹
از حذف ناگهانی خبرها تا ادعای نویسندگانی که می‌گویند نامی از آن‌ها در تیتراژ نیست حالا اما حواشی این اثر هنری بیشتر شده.
🔹
سؤال اصلی اینجاست: آیا حقوق نویسندگان اولیه پایمال شده؟
🔹
پشت پرده حواشی این سریال را در این ویدیو ببینید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/676029" target="_blank">📅 14:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676027">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUUUWOYCIeGKpDVcNDE-kf2lGcPy43M_ynQpiJr1eSaHveVIrbcAxXGQUcm10ax78SDe2rAYSXm11szDk_oRs8Szp2SEDcoChptqfwwtlWMV1jM2YL-dD-rO2g9mLP9eACopmRebrqBk6771OYDsYDwNtoxityjEZ7wqDIwicudoT20UcnDAXiG21GQ7UxAVdwA5zqVfTovPdCtInAt-DRjHehHBllbF5ZeZGO5A2H2LiHf6GhFDb4-ntEIvCnidpG7cLlrKuzYP7ye5QSa2ZT0-r0gWu0iuF1p6B0BzjTJ02DD6r9AkKTAw36pBbSrSRHGPjutyPWB3HS6MFU8cIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۶ مرداد ماه
🔹
بازار طلای امروز نسبت به روز گذشته نوسان چندانی نداشت.
🔹
قیمت‌های اعلام‌شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/676027" target="_blank">📅 14:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676019">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9-RNQQUu605cJ6r-FNMl-tTQbI7-11TgSKDK3EKlRO0XAtlx5K6cbDOr3wtgzenRcwIORYP3Tf-CFipmuwDn6RoIcG5ErgTgmVpkfrk8JEHTwgFdNjGNuPCKKgyoiYoeaNcEHHEksCCKpLw6I-qxum6J-xXNV5G4sXlKEKDVSQmYBW1fqTVMJ0gCE-136hVhpb6otPMv7lSqv02b6JqEdhLi1xAVGaX-EQl12RU8N_9R-QybSCC9_cwMQNMMSiUnDDBlSSXtJOSwYE4QoKo_1dCHLAk9GIay1pqwisoCgUZ4U4UaLCspzXY6fhGanV_G7eZvfVwLLwZo7sVo6HnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DvtJh78vxEXOSVo-E80RI1barcnGLsvsX4G82OZeOs1u-5dM4SwhynapOpM2un5ETAlD-3jp7aQTERQh3dZREkx_OXhOKBSrXiRccBG573Vf_2DGKWkEe_cBONQKkge-DrFX7DTR4-aXv9JkStlktusHmUMjuZ8FR5moHpb5_MaFNM1g_d1MiyphDJqntg8AjVWsD0YnpGjjV01lZAjQsO5PCCqk9PC297H1h4s8oDmSx2B6I2dHUK1djKPxYjDXPh6ND3p2IK_YHafrDoh68eAZlk1gwaDAlQkLy6VmEJOpXEI2d89AGQf9e3GuuXV6MqBKOcFwldP1umpfe_dt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhK9J7uWIng2jUyLdnZw29gqB5ap8GQVJPAokhVU38ZZAlRs62XdVMxxOKP1VU9hklDoAdlSYcCulYT9xIY0thVxFuL9l2p8G-zWTqvIo0Uf1j6G-HjN-FQwMtANUGgsOEAc-GekvIbFfbRIHLhq94IowH84ntaYLvIqLhUbaTqUEdOYW-ITCZ2za4LuALBtWBmbAbpE0HZw5F_A5fCrnrSzeXIyPx01ozAnvrsfmIhf9Y1vAUkuTVBToAaS-dmLGFzf0Hr520pswSG2xl_dmLLeX5h-rcSMRvtaTONnU_gLnTM8FHLvi6-kSwMrS7jowEena-3GE3_drQj_zmjfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rg6qyqziPgBQb_VbXz0as_lFoyda28oyhuqwlDs4wFvxKyqzyenrV85bPwNfQswmBi09DTrG1T6C9s6LZ80WNtnqYdOiQWja08DVDXSXr3cLOFPUM5jmKZ00yhmKA1BZQcULlUhEfpIlScnRga2t3dxy5yuU4TC1DYaOvAVgx1keml2J3Ly0tz2bOM8V0iGgxyfD5ZJ_1YwZn-K7HT62wLyo8ykl1R9sv2f16dwIPjBi71L4Ff3W5nIkF86f-H8RYv4J-PToqlS0GbKWh0DvSf6bcb1IQ2aBuD_HVI9WBguuDcqxc1j0qzh0dS9-OXcmELUxxaA7wPmASZHube_Upw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWPH2CJCj9zTTJcjPe4EbriXeX1gcrYk1UzKIUnJQS7-gqPdLz8BMpdc13elY6dHnXKfQWR_qyRBO3xlpbe8xyVMrcAcSAtKM6E_apUpcdt5stBqWhTiPG1CyhU0jWTCs-kcRRDUFgf6pRCMJNPtJKUy5ND-JcSlzvhzdmk4KQzKY9CcJvxwfAqwNMPcBP1knuaYJOWRv4Kjoj4Zk5VkDIpatL3_6r2zUkl-WKk49LX3atyZM5WNhHUdI3pjCpfRtfYFFgJKE6JIN26P2PhkcnE9mBcgNROF5ExGwKooDB936pRJULbsXWGt56pwu-ygbfoxJLNS6fiT1t82E4c9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qagLfIjWxBDyTnSL0UMR9whHuLrGicW8sph3GFuy-jR9atx6pbvoPsLkKJsiwNe-W6iyCRNG8XuCArwbU1x0OEjU_kHP4O00-nY-CYQ29EDFXBy7nae3nb_7DO7rEHPFX3WarsATWdHnov40UL-wiD2X7mFgHRxsB3gE7nVmsxyBD8OS15ZH4du6-e0WDcwF7sLIDFsMX69dG858dFV7LTtUmzF-sTB_vhcsoKVy1cev163qpPfWJFdNXY-aHxJH0GUvyq2SSw15hyRA4uX34YG9YoA1eBga5Nxhpp0o73z5AsXMjT2nxGwncQ0ShsyhMDNE-BAYwVIM_rHGlyJy3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7r9zzHztlvagt3zYBq1tHVnCj96guCoqIqDb2ULAISh5KjEpybk-jmYKgqYZRzMADBQxQTLoJ0uJqRwYArvdoL2uy7b-0les-2Jg_iY3gAdODK0_e0uJ-5ZvxlEu3EuUEMH337NqT6rW2JlBBrjmTOyGc5PbzQ4mr5-xkuxbLvuXshtXYjkFXL1uJThuYxVMTQLOA4BSnLOoP_fziP8vh0QaedKxnGdR996tMFCHctwPpZRvh_sa6obB-7kCRml_pHMxc-UyOtqjFt3_QPCcpmfP_gHRpcOFfKooA7jBhiVc9rU1OOat5xr9o24hoqfzVbhn94H0vsV0YHhsHvXcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اکسسوری طلایی یا نقره‌ای؟  راهنمای انتخاب اکسسوری برای هر رنگ لباس
✨
💎
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/676019" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676018">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2V_g-qfNdSDk5v37KSkLOpS6kiWwOD0hD_RtY8MzORaoZPwryCPqOYAwHP9KvsDI7LmfGyUq7eE88D3l_yOepUv_e32Akvf1pBB7aWbz6nF9X_0s_jiZ8jSCWg_dJPs0aK2nDwObCmFqO7_UONBylXdNzyBOkRR5zo7Ikl6hD4H0b06akY-iAr7eSqwcUu9ueyB95ErfnOuPWZBTd-Gz9_NBG3wQGxlx9oafLkc1wzqpooSQwAu4ILAQ0L0dffVNzR2XPoit8K_7J9tHuICjN_QPAKX3up0pNp_f_atGF5hHUcMsmjFQ7dU4Gq2xBL5C-EuxiCMFgvRWeufkH5Ofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین فرصت ثبت‌نام در وبینار رایگان
🎓
از اولین خرید طلا تا سرمایه‌گذاری حرفه‌ای
👤
مدرس:
هاشم آردم
🗓
سه‌شنبه ۶ مرداد
🕗
ساعت ۲۰ تا ۲۲
ثبت‌نام تا
ساعت ۱۸ امروز
امکان‌پذیر است. همین حالا ثبت‌نام کنید.
🔗
لینک ثبت‌نام وبینار
🔗
لینک ثبت‌نام وبینار</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/676018" target="_blank">📅 13:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676016">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بیمه سلامت: ۵ دهک‌ درآمدی اول و بیماران خاص و صعب‌العلاج از پرداخت حق بیمه معاف هستند.
🔹
معاون شرکت منابع آب ایران: بارندگی در ۱۲ استان پایین‌تر از میانگین است.
🔹
صنعا: ریاض باید محاصره را پایان دهد و بهای اقدامات خود را بپردازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/676016" target="_blank">📅 13:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676015">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای وزیر جنگ اسرائیل: ما قویاً خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
وزیر جنگ اسرائیل:
🔹
۷۰ درصد غزه را نابود کردیم و الگوی آن را به جنوب لبنان منتقل کردیم.
🔹
ایالات متحده در موضوع ایران ملاحظات و منافعی دارد که با منافع اسرائیل متفاوت و فراتر از آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/676015" target="_blank">📅 13:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676014">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeaMh7mqFqe_6yO7Jn6okW2dIMSjV8TQkQipei5lW5RUfRpTqJ9zhTAmIkAK09xEtu51v47hXURuU9x4I_s7ZUhmhnpe9skX4YcDxLrvuUVFm9Ji-gdxUMq7X0jPnadVb1_rwDI3GZQR1zCEIsZx--kF3cGFwlvMkgCpgV-rIS6KEk9TAp3ib8ilBNt_Jd-My1c2crm7G3zZbh-FQnr4pPp3MElJrxZGkugB0TbiocW204D5vajk04ZS_72urgaRu5TNp0WK_GT-oilX8TBn5uurC2-v8ZOSiFayJMIeS9eHy3Kp-uY1iMS6Vr7LFENQOLQWecIJA5Jr23EDW7E6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۶ مرداد ۱۴۰۵؛ ساعت ۱۳:۳۰
🔹
قیمت دلار با ادامه مسیر صعودی و افزایش ۲ هزار تومانی نسبت به روز گذشته، به ۱۹۰ هزار تومان رسید. با وجود کاهش نسبی تنش‌های منطقه‌ای، نااطمینانی‌های سیاسی در کنار تورم مزمن و افت ارزش پول ملی، همچنان محرک اصلی تقاضا و انتظارات افزایشی در بازار ارز هستند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/676014" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676013">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
مهاجرانی: تصمیم دولت درباره بنزین جمع‌بندی نشده است/نتیجه نهایی به مردم اطلاع‌رسانی خواهد شد  سخنگوی دولت:
🔹
دولت حق ندارد منابع نسل‌های آینده را به آلودگی و بیماری تبدیل کند، برنامه اصلاح نظام توزیع و مصرف سوخت از قبل در دستور کار دولت قرار داشت.
🔹
در ایام…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/676013" target="_blank">📅 13:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676012">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbCp9FcYWP6ZIbsVP4Ja4F-abtY23y7XwoFqIkqHMOtbl1MJsvVkfD4RMc1Gokfwzva_AiIfuI7OEqPxBGyxiHf_XtKc1_EtRHMebv4MLj0yKcZRY7Mc2YamixTsFbOAzZis0nKqhKHO5DLtryge3o5UID9VcKsKZnWK3tSCQviKiuxPsSADDRhEd_sYVeXVFMlZiyVZg33v6rmXUcIiONiP_AghcDM7HKSnOsqhKcr6YDyZw_DrlSeNH7cQRz62ueH44R_YSQAOOm6QvtDwGpJPw7mdHNL_OEV4Rfvx9j7du18gGt6_vglOrRR1V-fu074d3Vb_TAO5R8eLMnfj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد ۳۰ ساله مرسدس بنز به عنوان خودروی ایمنی معتبرترین مسابقه اتومبیل‌رانی جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/676012" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676011">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtrFRXhbbu-0rsEdAGFd-iW-b2pb3IXj9zZhzFvAwOba7hv3RH-e7jIjOMynAZ3i3tZP9-RXWueeTmmYI9gn3kvdHbumtSr0Wk-RCA7Pj9b3v1MvCcpI3TrPM7lbdDHuywU2RJl-7zstOquqScGlAfZ554PiiJYSyIb0OH-zN75ppEoDxrl2dbmP_9gse_a-u-g0GY_oAuY0iBmxzyCXi9OcNoRl1L2RCmsoXmO5T7N1_Ci1vS2Z7DX1pjCW08x7DW0JHKYNgM-mc0WMJ4w372j8spVuSmcVq9yktKlJ_XKZEWmr52LvpW-ki_zCjfX-rTC7QpmEdah5JxCJzXi8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوک جدید به بازار موبایل؛ آیا گرانی گوشی‌ها در راه است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/676011" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676010">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR6vKqZvX2vVVSnmt9_NSczrUYm99rFKQZrZfLIrtXOqYECTiXVLZZunrRiDBDUif1Ezcc9wOUeea0l4j2Z9B5PoFD6I4Ne26A8vrSBqSZ2keNM-oja3pjZzIsH2EBbtA0X0SnB_qiCXZ8ArEx_k6xSpGCiMGCWBPzQnR4dlHnTlAjx3uHQ0ZzH7R0lqU6AD15Jx9BuqCWkHB8GoJ2DOyCpQIBkiOr5Aw5hOXS1L7rM-4efEs2nRhQ31fVAG4bvNg1pkWctoqHOLACfWDMP0FfPTYPgemDaJuueA8h69HnSoUeWlbOaq-B61Ga9BlOTZe8wZY_noisDCsY7tH2c0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ای‌بی‌سی نیوز دلیل پا پس کشیدن ترامپ از جنگ با ایران را افشا کرد
یک مقام آمریکایی:
🔹
تصمیم به عدم تشدید تنش پس از جلسه کاخ سفید در روز جمعه گرفته شد. دو منبع اعلام کردند ژنرال دن کین (رئیس ستاد مشترک ارتش) و جی‌دی ونس (معاون رئیس‌جمهور) نگرانی خود را از تشدید جنگ ابراز کردند.
🔹
کین به ترامپ هشدار داد که اگرچه ارتش قادر به اجرای گزینه‌هاست، اما پیامدهای منفی از جمله کاهش ذخایر مهمات وجود دارد.
🔹
کمبود مهمات یکی از عوامل کلیدی در تصمیم‌گیری ترامپ و تیم امنیت ملی بود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/676010" target="_blank">📅 13:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676008">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlE28wZZvj4k8IqKAidfMy7TyVILdbkpQrGsjJiB-WFIlRVa7plg1xy2gVG5QpeLzBnETjcYzY6zG-IyBXmxwG_e-235054WhKrGWYXEgQX3RE1FuxIQAXTlNA9Vs0J0A3Zzl0L1k1Pz_rD5aMdHHlt8W_gW_ic44PkyOOh7DQkhY3fAvWzpc6DVTuudzeO7cBOn-YKqlHdrb6ybwjLlf3AQDNIaFcBm8LuyGWXf3y0DkIfxxplky2QFafY-0h2GYWodWmMw35td6nZv47t26IYekwQRbrYhi9WrH94lIG_8c7wljfZiIqlT7Moj2LzBPcVpYaBPh1xD2JjGZE0Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دنیای شیرین خرماها؛ آشنایی با انواع مختلف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/676008" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676006">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8890acae80.mp4?token=NFBzaX7gdAzGc8Jm68LJypw9xCrOV7OHSgqP_sF6OBLyLCx5dGV7wp80fFJDEPKKSFfA17pxBmQ5K7D-NkeESK_SFadBtESV25K4nkKHpoUUoOOA5SXuhzK6M3EjPvuVJXIrFr9acD9lFZ7tRL7ZXbpmlbprne8hei-YQi20QiVmf9wyQIcMboMCWvCjmLU6eumN3nbRtZQjPtfnbouhhCzs9g337ChBgvZz6fKOH2xOVjHeexV-tUEDaq-Vw54KVgUOW0XNKhnlUnvgZLUolYw5jmOkUZX3oT-UI_a4X-Pnay6-1wHoTPanoDzkBjX9OW2VPyA2du8Uz5Yu4jXjxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8890acae80.mp4?token=NFBzaX7gdAzGc8Jm68LJypw9xCrOV7OHSgqP_sF6OBLyLCx5dGV7wp80fFJDEPKKSFfA17pxBmQ5K7D-NkeESK_SFadBtESV25K4nkKHpoUUoOOA5SXuhzK6M3EjPvuVJXIrFr9acD9lFZ7tRL7ZXbpmlbprne8hei-YQi20QiVmf9wyQIcMboMCWvCjmLU6eumN3nbRtZQjPtfnbouhhCzs9g337ChBgvZz6fKOH2xOVjHeexV-tUEDaq-Vw54KVgUOW0XNKhnlUnvgZLUolYw5jmOkUZX3oT-UI_a4X-Pnay6-1wHoTPanoDzkBjX9OW2VPyA2du8Uz5Yu4jXjxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین واکنش به شخصی که به شما بی احترامی کرده...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/676006" target="_blank">📅 12:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676005">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahvacomplex</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd22100af.mp4?token=GtDegDaxStYKFk5h37Ck9UkLi00xPhPg04iTr6_PS_ZdcW2Wxz0_taWIEgI1PZGzA5MPdLitXG-orxTyNGBAyUTj5RAHN6DiidvRRi8EeOZp29Ol5jw9Bmnw2_-FglLkm_hMe8ngYHlYM0KpO2AxCW1XY6duz7lFqRYwV2_yXgOgnOoWZXHf6VppUiC2re5LjfRP-Ovi1_6HTBqqOkgQ2ldqddmPWBUgHLiRr0QiUQQExuUpEoSUyp-pCJXRvjBG9_MdFRTgvSf_0vQ69di5jPNGNJydSmEjH4JNoq5TxGSq9BeTpqwDMcGcYMFk049lr2--WzsKEzkPTC3My9_i3aMNNi1iCQDIJzK8R8mb4nQJYpy_Yas1wmRXVKkEJkxDCqqldnCO2RtczMfwhUYeg4Qm8OXkzgyZJC0At9B4UDNqxIW6pGfTds_gKfE3wyuH21716P38_pBctNjbg15vUbJ3sI61C9RuNRmhiOhHTzAPkq76UCDS8KDJVWMk6GPFeWZNLIUiwiuoUcMJ2cHOGhC0yfnV7ArDKvRdouDyZlakjHpCnDLr9lyn4ZWRB1ucNL7b3VP9tBTwrykJ2A_Gc_XMCen5OOXdksYtVZ_Sfb8A5ZFy73yjHxQZF3g9gVtGUe2XJCTaFIqG0L96FaeAkyPXp8_9YHMLaW66A4EZWSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd22100af.mp4?token=GtDegDaxStYKFk5h37Ck9UkLi00xPhPg04iTr6_PS_ZdcW2Wxz0_taWIEgI1PZGzA5MPdLitXG-orxTyNGBAyUTj5RAHN6DiidvRRi8EeOZp29Ol5jw9Bmnw2_-FglLkm_hMe8ngYHlYM0KpO2AxCW1XY6duz7lFqRYwV2_yXgOgnOoWZXHf6VppUiC2re5LjfRP-Ovi1_6HTBqqOkgQ2ldqddmPWBUgHLiRr0QiUQQExuUpEoSUyp-pCJXRvjBG9_MdFRTgvSf_0vQ69di5jPNGNJydSmEjH4JNoq5TxGSq9BeTpqwDMcGcYMFk049lr2--WzsKEzkPTC3My9_i3aMNNi1iCQDIJzK8R8mb4nQJYpy_Yas1wmRXVKkEJkxDCqqldnCO2RtczMfwhUYeg4Qm8OXkzgyZJC0At9B4UDNqxIW6pGfTds_gKfE3wyuH21716P38_pBctNjbg15vUbJ3sI61C9RuNRmhiOhHTzAPkq76UCDS8KDJVWMk6GPFeWZNLIUiwiuoUcMJ2cHOGhC0yfnV7ArDKvRdouDyZlakjHpCnDLr9lyn4ZWRB1ucNL7b3VP9tBTwrykJ2A_Gc_XMCen5OOXdksYtVZ_Sfb8A5ZFy73yjHxQZF3g9gVtGUe2XJCTaFIqG0L96FaeAkyPXp8_9YHMLaW66A4EZWSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📣
اکران «افسانه سپهر» در روسیه
🔻
انیمیشن سینمایی «افسانه سپهر» به تهیه‌کنندگی مهدی جعفری جوزانی و کارگردانی عماد رحمانی و مهرداد محرابی، از اواخر مرداد ۱۴۰۵ در سینماهای روسیه اکران می‌شود.
این اکران همزمان با پایان تعطیلات تابستانی کودکان در روسیه برنامه‌ریزی شده و در کنار نمایش عمومی فیلم، یک رویداد ویژه با رویکرد همدلی و یادبود کودکان میناب نیز در حال برنامه‌ریزی است.
نسخه روسی این فیلم با عنوان «Легенда о Сепере» ثبت شده و تریلر آن نیز در پلتفرم کینپویسک منتشر شده است.
https://mahvacomplex.ir/n/938003
@mahvacomplex</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/676005" target="_blank">📅 12:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676003">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmY16FdUXq5coJL3dBXjzw8ppl5PIKkPYmOTDDHyUB_mk7pHnh6nq1lwYQ4TnO15lXB2nV8XmjNM5ZhSbcH025BcMErOHU4FvY5eklqfabkMwHXimXsKp2YRpzUx6bDn-I-sY7V9ZdIREo-jMpSewwJkbyo46dvlwdF32Yy6X0-XAWB15mx-cEXAHRx_MYoZP2U-aCs6HE9InH2w1zhla3UMVP_DlFXwqM4bT-xm8LF00rP41wBLhKvZmoCMdlqjYMrcNCLvLR7XH60zrUBEYyFnwuqChPG2JZw_XKJGdwR5w-OHrVYgC-Tc-RvkOCx3GOg_5UDYAngg2E7QhwuSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه کله پوک
🔹
ترامپ، نتانیاهو و زلنسکی در کاخ سفید؛
یک میز، چندین نقشه، و کلی خیال‌پردازی درباره آینده منطقه، اما مشکل اینجاست؛ دنیا همیشه طبق نقشه‌های آن‌ها پیش نمی‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/676003" target="_blank">📅 12:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676002">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXaqmJK9aIe8kqdjl7ULfius7eR953_vtxg99v_QICNk5o2EPiZJTJlyk6I_3DoJjLWNf3V-nrHHIYgYnSgmW0BBWeXufkJodDgzfvNGGZj4BWkKZnjoE68FqukYxdebBElc1qu8Zd9z_iwroZPeIhywxeyKFLG7Iavnl3ULI6rLJC5xIgDpTMIxPLZHPhPH9Z-zQgf-ZDUDq7K_kdCMbhTdUEAuBAKqoi4eyI66uKWvtgH_PlJKEoZxYXrNb3NHS3cKgL6-E7h1_HjcGlpGlN14x78K4iSyj4Y84y-hw6OMPobQ1kD4ZJnokyFbBuWv1zx8k303Rgn3tBKm1yLNMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زین الدین زیدان رسما سرمربی تیم ملی فرانسه شد
🔹
با اعلام فدراسیون فوتبال فرانسه، زین‌الدین زیدان تا سال ۲٠۳٠ سرمربی تیم ملی این کشور شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/676002" target="_blank">📅 12:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676001">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9233560c18.mp4?token=Lrfo1m_CK6iYiqsMjr4pUoA4ALJlAlZMgCxVF1rYMCNq4AXU3YUI39er42JqAfTIkIC_09BjZUvurjWZG79wIJdlHzlgTlvq3LngsR5CXHbCNK7aI5tOjQkgf1Hz9217Yi2c-UkC8YPU9jkBUj0afoMJzH2edCN5sDcPEBbdNwYAXiIDxWbLUY8a5ndGKFArJjkPb_S14udd1b9SBnMBCVlButlfVnYx3XF2Qez-noGhfGhtzN2C2s2GY9Br1WAFGncT-2T9Ue8YzwzfaQe4bH-w28ss7YJMolZCyE3me2QpZyYL3uysQQ_MFYMTmYKggjkUVws7PSpmZK9pkUsUOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9233560c18.mp4?token=Lrfo1m_CK6iYiqsMjr4pUoA4ALJlAlZMgCxVF1rYMCNq4AXU3YUI39er42JqAfTIkIC_09BjZUvurjWZG79wIJdlHzlgTlvq3LngsR5CXHbCNK7aI5tOjQkgf1Hz9217Yi2c-UkC8YPU9jkBUj0afoMJzH2edCN5sDcPEBbdNwYAXiIDxWbLUY8a5ndGKFArJjkPb_S14udd1b9SBnMBCVlButlfVnYx3XF2Qez-noGhfGhtzN2C2s2GY9Br1WAFGncT-2T9Ue8YzwzfaQe4bH-w28ss7YJMolZCyE3me2QpZyYL3uysQQ_MFYMTmYKggjkUVws7PSpmZK9pkUsUOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهران مدیری چرا به مراسم خاکسپاری هنرمندان نمی‌رود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/676001" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676000">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac175e4e98.mp4?token=ptHNfJPtGSGbcN4tQLSh98YGKV7S0IRqBp30uDp4HdLap4jqjyM-rz4pLjriqvFs333wQkLNj6iM6vAS7pi6riNoJi9zlTv3YLii2gTRD0LylXRt6l8PKRI_dvOJTFoZQLAP8oLjzLAgXpY0tZhToy0Xb2upK0FEsp-vxuQRu53jMG1JAeoJqouxmLoX1WVV7di1w1d0IuA7XBwFm4gAct8wNxbISI-iCd5Ojl3BGjK1KGm6lHFQbILCt8Gd1tCB-bfcUUzJOrXhdEVQ0LuZkl1R5-4rbebmYKCjCd8roUMGk8pBg_BQs8ZssaWLtxs0pRKYt47P2v2-VsxGuqJCbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac175e4e98.mp4?token=ptHNfJPtGSGbcN4tQLSh98YGKV7S0IRqBp30uDp4HdLap4jqjyM-rz4pLjriqvFs333wQkLNj6iM6vAS7pi6riNoJi9zlTv3YLii2gTRD0LylXRt6l8PKRI_dvOJTFoZQLAP8oLjzLAgXpY0tZhToy0Xb2upK0FEsp-vxuQRu53jMG1JAeoJqouxmLoX1WVV7di1w1d0IuA7XBwFm4gAct8wNxbISI-iCd5Ojl3BGjK1KGm6lHFQbILCt8Gd1tCB-bfcUUzJOrXhdEVQ0LuZkl1R5-4rbebmYKCjCd8roUMGk8pBg_BQs8ZssaWLtxs0pRKYt47P2v2-VsxGuqJCbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب ترین متولد تاریخ رند (۰۵/۰۵/۰۵)
🔹
این تولد صبح دیروز رقم خورد ، نوزاد دختر در حالی متولد شد که مادرش متولد ۸۸ بود یعنی ۱۷ ساله و مادر بزرگش که برای مراقبت از او به بیمارستان آمده بود متولد ۷۰ بود و تنها ۳۳ سال داشت ...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/676000" target="_blank">📅 12:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675996">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سارق سنگ‌قبرهای بهشت زهرا(س) دستگیر شد
🔹
سرهنگ سید امین موسوی، سرکلانتر دهم پلیس پیشگیری پایتخت، از شناسایی و دستگیری سارق سنگ‌قبرهای مقبره‌های خانوادگی در بهشت زهرا (س) توسط مأموران کلانتری ۲۰۵ صحن مطهر خبر داد.
🔹
پس از بررسی‌های اطلاعاتی و بازبینی دوربین‌های مداربسته، متهم دستگیر و در بازجویی‌ها، محل نگهداری اموال مسروقه لو رفت؛ مأموران موفق شدند با حکم قضایی، یک قطعه سنگ‌قبر سرقتی را از مخفیگاه وی کشف کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/675996" target="_blank">📅 12:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675995">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589965cc.mp4?token=Pf4TwGz021MW1Kez_ul_BPFZ8JWDG5ZRsNmo5N-FzL7nD2A121D_ROCNsxJvwxo7F79FjEccjGfYqcgeaUgmqFktj7XsrJNezTPK0XOYLal64CW6KsY4NdCWFFGaFeHIhW6kCKLV90uppbZWrIC4z3HlHqqMZW4vTPXAWA0pva_YKfcfJS2ah9T2vZOe7eRS1zcHjfgNYq_rOaoRiAlo1gTZi-YnN6Da9CV6SZglPb_B4xef9C9x5mKJV0CTX5VT3_9CwVfn5JoTcvIMJAgbblodA-k-airxNeFsBYtsn0SSHhyHpquT6ePHUxlzYC6u_D12KW7lK-vGa32PSr5qgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589965cc.mp4?token=Pf4TwGz021MW1Kez_ul_BPFZ8JWDG5ZRsNmo5N-FzL7nD2A121D_ROCNsxJvwxo7F79FjEccjGfYqcgeaUgmqFktj7XsrJNezTPK0XOYLal64CW6KsY4NdCWFFGaFeHIhW6kCKLV90uppbZWrIC4z3HlHqqMZW4vTPXAWA0pva_YKfcfJS2ah9T2vZOe7eRS1zcHjfgNYq_rOaoRiAlo1gTZi-YnN6Da9CV6SZglPb_B4xef9C9x5mKJV0CTX5VT3_9CwVfn5JoTcvIMJAgbblodA-k-airxNeFsBYtsn0SSHhyHpquT6ePHUxlzYC6u_D12KW7lK-vGa32PSr5qgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غرق شدن تلخ نخبه ۱۲ ساله ریاضی در ساحل انبارسر
🔹
عصر دیروز ایلیا پایپر ۱۲ ساله قهرمان مسابقات جهانی چرتکه ذهنی Ucmas ، در دریای روستای انبارسر غرق شد و جان خود را از دست داد
🔹
تاکنون پیکر وی پیدا نشده و نیروهای امدادی همچنان در حال جستجو هستند.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/675995" target="_blank">📅 12:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675994">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3762790f.mp4?token=jCInxTvSeC_yC5m0I-GCg1ciOYf7MT3WedhqQqS5v49_qn2-vHnrvMBtSdmzR-GZson8NQwcSDo9R7kXdwE3kzD38p9xh5tAZ0Q49qSMu_MhTiDqv8kXqqUUWLFR7zCr4y9Cgw_8W8hLqXt--TbaiuweNOAEjs3pWfUuW8j-uHDkbl2Ti41wDjC6it7-6jtEzCHiSy9h0m82WLJviBMD0HKIItPxcRRRNyqjW2PB2pGbQiLv4ieY1EvtJDA7xFdinWVQaXK_HrOA4-5-6g1DGbc_kZ1lQeDyEQ37pi-LmSwDASQq3TZoR1hR7CYmXCJ4xHDyfVA3gzqcqPmCd3aCiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3762790f.mp4?token=jCInxTvSeC_yC5m0I-GCg1ciOYf7MT3WedhqQqS5v49_qn2-vHnrvMBtSdmzR-GZson8NQwcSDo9R7kXdwE3kzD38p9xh5tAZ0Q49qSMu_MhTiDqv8kXqqUUWLFR7zCr4y9Cgw_8W8hLqXt--TbaiuweNOAEjs3pWfUuW8j-uHDkbl2Ti41wDjC6it7-6jtEzCHiSy9h0m82WLJviBMD0HKIItPxcRRRNyqjW2PB2pGbQiLv4ieY1EvtJDA7xFdinWVQaXK_HrOA4-5-6g1DGbc_kZ1lQeDyEQ37pi-LmSwDASQq3TZoR1hR7CYmXCJ4xHDyfVA3gzqcqPmCd3aCiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت استرس و اضطراب به زبان ساده چیست؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/675994" target="_blank">📅 12:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675993">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
کاهش ریسک‌های ارزی و بانکی با خدمات مشاوره اتاق تهران
🔺
اتاق تهران با ارائه مشاوره رایگان در حوزه بانکی و ارزی، به فعالان اقتصادی کمک می‌کند با مدیریت ریسک‌های مالی، انتخاب راهکارهای تأمین مالی و تصمیم‌گیری هوشمندانه، تاب‌آوری خود را در بحران و پسابحران افزایش دهند.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ | ۳-۸۸۷۱۴۴۷۲(۰۲۱) |
www.tccim.ir</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/675993" target="_blank">📅 12:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675990">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d47105a77c.mp4?token=MpYOrZsGWfMFwkkSY5lLgjr1VrzmmcCvzFf9jknSxvlu4Rlwnhodee4IJIZ2GitRay68qOnm9mwQ1zzWUjj0MoUmtp_qFB5vTLuucfR8DZRsFVll7yrWXM2CYowfDZQcwxVwM_W1ulnev1jlLdbV8AfCrLdkJk8--l4L7oa6mh1U3YjxktrnXt4ZnPNJl1Q2Jy0JWzXhWBfNxkFR_caaa7Q9hZpslcM5VxDX_xhXezmt5I_aDGIOTSgXVv8JpuNHMzCoHBOafem5Zigx6ozxnLMBo4KYKO1S7KKeEzvrW1byk5ahNaTsHGC6AZoXeRhEZxBREo-FvxAqM7dxfiqzRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d47105a77c.mp4?token=MpYOrZsGWfMFwkkSY5lLgjr1VrzmmcCvzFf9jknSxvlu4Rlwnhodee4IJIZ2GitRay68qOnm9mwQ1zzWUjj0MoUmtp_qFB5vTLuucfR8DZRsFVll7yrWXM2CYowfDZQcwxVwM_W1ulnev1jlLdbV8AfCrLdkJk8--l4L7oa6mh1U3YjxktrnXt4ZnPNJl1Q2Jy0JWzXhWBfNxkFR_caaa7Q9hZpslcM5VxDX_xhXezmt5I_aDGIOTSgXVv8JpuNHMzCoHBOafem5Zigx6ozxnLMBo4KYKO1S7KKeEzvrW1byk5ahNaTsHGC6AZoXeRhEZxBREo-FvxAqM7dxfiqzRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معروف است به قدیمی‌ترین چای فروش ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/675990" target="_blank">📅 11:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675988">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNz06GsxLGRykpaIXW3ZpA9u04Zio2fPJv44bmhfA7SjsSR3VwXIeM9K5QNIoIlPgIKbWk4UxpnnDSbRI_r1Dy4sHk56ZCbaGHG3OnRK0WiT2ZikJaQC5ncvShQgUJWiS5RMKBnV7YQDuU_spO9DxEQTGrbEgh-0tQOpzqGOxdJGLQt0FDHXuw9xW8WK1foaiMKORjeAdPwvuiBVH2_TY5ElQBTwv4HJd4gduxFXn-BQa1_4eswhvkSLIhCy2uoHYxSp-Lt217GARiGgIZIpd0xCwwiopCRKziAEQdni_k9If5PlvpMeyLVpMV5D7wLw9Lwc_Qdmpoc12AQowVdksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
غاز پا آبی معروف به کودن‌ترین پرنده جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/675988" target="_blank">📅 11:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675984">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uL2tmH_6GvIv-yIYUBj83fYxTKxpT_8_2UVUI13bw5SmnJqJqjjyITP7rtxG9tQB89qNOtnXoSGW4vnef__1rG4xy3RR_-0QL1Nu3wV4iaOraJofNbbWn3xyNRyBROQUG6aVVk6a_RGvNSz3r6fzusP-RAbIJmLGDot6umb2u1trdvaWts-O4LzUTixF7MYijnF9IzS5nRATXqu9ogmQSAWVgL9mosWsLUpItiMfMtNdij6ycc729H2GmpjyG00xAiAl-jfHbRlw3aB9kWxwy9gcYCTB80C1plHYxo8I9PwG9PsXqxLo--sEfpaKedooB6VR4_Ulu8jfCOa_BaD4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzS026CQKDXNROlmUp9y7bwcXtDLhM5ic8X1r3DerF6Py9-7pztP1rpaP9RElSHuWPDCbwn5b_TntZndyKMjxVQhZ7nJ29J0YaGCU9M0Jp_6pMFGdcp2zFuwT8tlzQvRbAv1ANaIMmi9YotnXlOXm2M5LVp3fklGIfHNLlZo4Ch6ukk_rf18T6srcP4TsXfJSehiAoEYmFIW_iqifiFT-4hfSWN5DOsQEBMQKqo3fXXUnCxZaJb7gDaaWTfzKmX1-zWMG29qq_-4of28AlxMLKfQS3IDRgoQad8jyAj6a5w6flC2FKlJRnoQcvZhTObGASBXMijpTzTsoJYo2_Q1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4UrdB8Jw3ddDQ1xDkSbu6O_M-OhwEMOF3mRlT-oRVQDHVHW37k5BehqNNKvCHpaitG1hGhGWZX_vkeOVpGKC2y4TDpt0RYVn7OYaugAiUxd99IF41mKqfSxn8INlxL_xGDNVi-Etf0paJkoXZAVFNPJkBKl5pcdHDTxpyYLRzDMCPXjiUjymjT5xCeYNbahCUujv3qDF7SdvUmylnIrcjp2K501C9e0u4dTTN-g9D69ezjO-SjsFzkTv2ob_jcrAQGbtuG0KVtfpI2Y_0Gywmg_AfzbdBJ073eo0FyuUdsOT5XKbQ9t96cZj2Q70vL7rOpy-R7M2mg6TzMyEAkDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEytCAtmf-NWf67BvQ_7M3fU8SO54BPJOf357JjM_PzEKrV5ka0j3SndeEozLurHpcYhnJhHMur0aB0ACO0Bs1EEg3jH4rt43hocVtQy_q3o3FeL5MCrUKF8i_TBfJRKcaALQUB8_ZyBBBD60SwJet33DdeW7myrVEw8F-B67s2S--4k7zQGrCJKYaE4pODiPij0a4uDuCQSBmQUX0QnPmYGkZ93_RYkSePqBScYGP5iTreYYzerzWWuW_EAJo5DYN7RF-CfMM3ucvhfvNSkjnDXCBaYKo_DpH6f1FC2oCcNlUmsCoMK-bwpkDJFLpEDYG0bRMTzIBjp2f_Sgkh04Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
مدیریت صحیح مصرف برق، با اقداماتی ساده و روزمره از خانه‌های ما آغاز می‌شود.
🔸
استفاده از نور طبیعی در طول روز
🔸
روشن کردن کولر فقط در اتاقی که حضور داریم
🔸
تنظیم دمای یخچال روی ۴ درجه و فریزر روی منفی ۱۸ درجه
🔸
خاموش کردن تلویزیون وقتی کسی آن را تماشا نمی‌کند
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/675984" target="_blank">📅 11:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675983">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141a9579d9.mp4?token=bOTEjKgPMzAz7XU11V0JJATyatTkDabTsRNDW-x-X78FTXw-ozQJQkSw5Ovdg25E2c-nN6CkToa8XhEAZ-XEZ2s_4qoX87Wo0bsR9WhOufpPM2FDAJMa9B-sum55GyFbHZfllU3MGlgofpKyoAUscLPOa7RHUlNDE82QbFQkOOnYp795atHWxXT18d4ympkdnlJI3FG9xJqssRVNqlES_P2A8kPl_cK7XdOV3BeCRabftQV9RCTbEvfSkje6hqXgkhWCWZhEipXZxuHL-0h_EsZeUWHFECvOm-H8WdlXmy3iVvTBPrxQdfG90n1sAzObKVFKsBE_R5ADgPanHjxe5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141a9579d9.mp4?token=bOTEjKgPMzAz7XU11V0JJATyatTkDabTsRNDW-x-X78FTXw-ozQJQkSw5Ovdg25E2c-nN6CkToa8XhEAZ-XEZ2s_4qoX87Wo0bsR9WhOufpPM2FDAJMa9B-sum55GyFbHZfllU3MGlgofpKyoAUscLPOa7RHUlNDE82QbFQkOOnYp795atHWxXT18d4ympkdnlJI3FG9xJqssRVNqlES_P2A8kPl_cK7XdOV3BeCRabftQV9RCTbEvfSkje6hqXgkhWCWZhEipXZxuHL-0h_EsZeUWHFECvOm-H8WdlXmy3iVvTBPrxQdfG90n1sAzObKVFKsBE_R5ADgPanHjxe5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای هوشمندانه برای ساده‌تر کردن کارهای روزمره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/675983" target="_blank">📅 11:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675981">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKFOT6GEY9LsDUmcyTcOICEpwdbDjcptWm_lqCJTiZiIaOk9KLRKOFUfCZLbTkqVuiypiCAb5SPyzbt8VgZH3R2Xs4CMO_oaHdpYvrObDCboraTsN0AMPCMQZNMBnKto7Uc6AAooIk4CZ4J4X5dWDs3IhP9q_MfDeG4aqee18-hDudTRhV-PpcI2NEOzs7rXFrA2G0a74zQb6nNakuobbOlQVQ3nWksE9LzlxACZ3Z_pQmtWuZ6C4MWSUSHv8aA7VHU8OMm2JaLHYVolv5u11kzxL_QEQzUbDNHWzZnq8Y-o4YOzI1KoIi_Kj21GKt1mxK_yJZlb6ZfER3qSUYanyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
۱۰۰۱ سفر کربلا
✨
▫️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/675981" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675980">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88bbba788.mp4?token=TCzj6jdMLWaar4SfjtBPGfbYgf0Z946gdqGwNjaFJrjsVqLReBtRPhrnOXW7woqWqhtmV1pT70rkKPrL97YRi_Vd1XuvwgR0iUHOBt8abRoNvZOF4Ens2J068rIZqzOqm39qTy7tmyjfEDnxaa51S1sKuxD9y7nod2Pc0n_JZlMDvcT920VUzJm_qKfzBY4QuAebL6ckO0Ong91nzQl6ZrRYtYv60jl7pRfIm1CwM3TylMh6kp5sfePLGyIN7atoWk0TKufgdtUAxrlE5msq1o-JPPY7SsFFIqgFNKcbm7rLO2ExKKcslO_HuHppLxl1nx-B0rtX7CTat6kh_yfsRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88bbba788.mp4?token=TCzj6jdMLWaar4SfjtBPGfbYgf0Z946gdqGwNjaFJrjsVqLReBtRPhrnOXW7woqWqhtmV1pT70rkKPrL97YRi_Vd1XuvwgR0iUHOBt8abRoNvZOF4Ens2J068rIZqzOqm39qTy7tmyjfEDnxaa51S1sKuxD9y7nod2Pc0n_JZlMDvcT920VUzJm_qKfzBY4QuAebL6ckO0Ong91nzQl6ZrRYtYv60jl7pRfIm1CwM3TylMh6kp5sfePLGyIN7atoWk0TKufgdtUAxrlE5msq1o-JPPY7SsFFIqgFNKcbm7rLO2ExKKcslO_HuHppLxl1nx-B0rtX7CTat6kh_yfsRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرانی: تصمیم دولت درباره بنزین جمع‌بندی نشده است/نتیجه نهایی به مردم اطلاع‌رسانی خواهد شد  سخنگوی دولت:
🔹
دولت حق ندارد منابع نسل‌های آینده را به آلودگی و بیماری تبدیل کند، برنامه اصلاح نظام توزیع و مصرف سوخت از قبل در دستور کار دولت قرار داشت.
🔹
در ایام…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/675980" target="_blank">📅 11:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675978">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c2169df5.mp4?token=feddCCmPQ7iqBjuMif1j5EOGLvGlJug6v17FXtJPyNcmBbCDz5vtHaTNmzdJFG1sSKlkdykfYZpaulSw_aZBx6JkXiokg0qKgfpxP97gMD5NrRE4NMWVlWX1a1s7Or-uPtYAJoREnQRTpOYKfFsFb-slDMSmA2UUQgMynawDF9iSLdgywzSTKpk6R0A3NNTugJaLidR-gf751-szwokuJIcpuDIxVzZ_15y-fyFtZN9ivzO52p36k1yeRposbz2eRjWerlv72mI1KbDcl45r9pjSZn6r9mAsh_ND3Gtk8KIyOQy4E8RXU_qKDHti9puxxpQMGtxFXEx6NqRZABFZwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c2169df5.mp4?token=feddCCmPQ7iqBjuMif1j5EOGLvGlJug6v17FXtJPyNcmBbCDz5vtHaTNmzdJFG1sSKlkdykfYZpaulSw_aZBx6JkXiokg0qKgfpxP97gMD5NrRE4NMWVlWX1a1s7Or-uPtYAJoREnQRTpOYKfFsFb-slDMSmA2UUQgMynawDF9iSLdgywzSTKpk6R0A3NNTugJaLidR-gf751-szwokuJIcpuDIxVzZ_15y-fyFtZN9ivzO52p36k1yeRposbz2eRjWerlv72mI1KbDcl45r9pjSZn6r9mAsh_ND3Gtk8KIyOQy4E8RXU_qKDHti9puxxpQMGtxFXEx6NqRZABFZwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای کشته‌شدن یک زن در میدان علیخانی اصفهان کذب است
🔹
از ساعتی پیش، ادعاهایی در فضای مجازی از سوی برخی رسانه‌های معاند مطرح شده و عنوان شده شب گذشته خانمی با هویت معلوم در اطراف میدان علیخانی اصفهان کشته شده است.
🔹
براساس اعلام دادگستری استان اصفهان ادعای مورد اشاره کذب بوده و گزارشی مبنی بر کشته‌شدن زنی با هویت عنوان شده در محل مورد نظر واصل نشده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/675978" target="_blank">📅 11:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675977">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfiXGFMxIEUdXvLyB0ZZUHFh82Y6N6tVCVCHGXXq59v7G94-0ndh3ckuTLHQhwSTsSsXu2pm6G-IUZdB7_sTnK08r0kkHssJgxN31QcBK4WUIx91Ftq5w1nOyCm2lohxUtu28VDY7d14t-yGxh4v5wLzMferwwSn9zrSY5rWPm515MVhAG5mgZJv-gpxtZhLfWTlVJEf4xaWXPX9fjprqTBEqQJzWQwQTmpv2pXZ7JnpVgjKcsbs39DhmLkZ29JhPIE4BcuniWJPXnJVPzd5Gh6MJmcG8vER9sjkYxfDnyH3bqPlbU9EcvCd7wHRW3Fy5BSLLL_CHxco071R7o9eaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق؛ عامل اصلی آتش‌سوزی خانه‌ها
🔹
بیش از ۴۰٪ آتش‌سوزی‌های ساختمان‌های مسکونی ناشی از مشکلات برقی مانند اتصال کوتاه، نوسان برق و سیم‌کشی‌هاست.
🔹
طرح «پلاک ایمن» امکان بازدید رایگان کارشناسان آتش‌نشانی از واحدهای مسکونی را فراهم کرده تا مخاطرات ایمنی ساختمان‌ها شناسایی و پیشگیری شوند.
@amarfact</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/675977" target="_blank">📅 11:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675973">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ صدور شناسه برای کالاهای تقلبی
سید احمد حسینی، رئیس اتحادیه لوازم یدکی خودرو در
#گفتگو
با خبرفوری:
🔹
اجرای نادرست قانون مبارزه با قاچاق کالا و ارز و صدور شناسه برای برخی کالاهای تقلبی، زمینه عرضه لوازم یدکی تقلبی را در بازار فراهم کرده و کالاهای اصلی نیز توان رقابت با کالاهای تقلبی را از دست داده‌اند.
🔹
افزایش شدید قیمت خودرو و هزینه‌های نگهداری آن نیز باعث شده بسیاری از مردم به سمت خرید قطعات و کالاهای ارزان‌قیمت و تقلبی بروند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/675973" target="_blank">📅 11:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675972">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سخنگوی دولت: سهمیه بنزین ۳ هزار تومانی از ۱۰۰ لیتر به ۵۰ لیتر کاهش پیدا کرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/675972" target="_blank">📅 10:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675971">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است/ در این ایام ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند  فاطمه مهاجرانی:
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمای نویی که به تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/675971" target="_blank">📅 10:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675968">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است/ در این ایام ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند
فاطمه مهاجرانی:
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمای نویی که به تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت و تنها قسمتی از دم آن باقی مانده است.
🔹
در این ایام ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند.
🔹
برج مراقبت دریایی چابهار با اصابت ۱۱ موشک فرو ریخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/675968" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675967">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/be688382c3.mp4?token=Owg5lI5iOpk4S0wgcZKxXSveXHPTWD5EwD42jF5oi6t_ffT7vAx04T1Qs3MAu_CFHQGK1pcxQgF-31WujR1oOrWUswnTWh3yGLhclCfcD0NRHDM7BjKtVjK6x-YMszi5C_JDWPIhB2LJG_XZmTcVKeVhOJ7cz73KgH9KCrCXnOscFYImgNSwYLNdYcTuEKXZTYARtLzLAddb-inYRV6aNbMUP9VoeLqOE5E2KzqiONj_c4_4ciJejlpVOklOSqIgoH14s4kLJ409HNOwGUvfAr_uKzWJ_egTXl5EJKwb9BECTAJRyLZYHYso3J4H2fdCyb1tltWpHgZZlYMG3jVhHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/be688382c3.mp4?token=Owg5lI5iOpk4S0wgcZKxXSveXHPTWD5EwD42jF5oi6t_ffT7vAx04T1Qs3MAu_CFHQGK1pcxQgF-31WujR1oOrWUswnTWh3yGLhclCfcD0NRHDM7BjKtVjK6x-YMszi5C_JDWPIhB2LJG_XZmTcVKeVhOJ7cz73KgH9KCrCXnOscFYImgNSwYLNdYcTuEKXZTYARtLzLAddb-inYRV6aNbMUP9VoeLqOE5E2KzqiONj_c4_4ciJejlpVOklOSqIgoH14s4kLJ409HNOwGUvfAr_uKzWJ_egTXl5EJKwb9BECTAJRyLZYHYso3J4H2fdCyb1tltWpHgZZlYMG3jVhHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: اهل جنگ نیستیم اما اگر جنگی به ما تحمیل شود خیلی خوب دفاع می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/675967" target="_blank">📅 10:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca2821921.mp4?token=W2oyY_lN8iczLWMGJdEos37wLECkfAw7jZ2fgTA4paELEHrtyL_p5Q1gED-fYNfOWRdwsPW2Mc6ypKiGSj2A3g7dcmwgggs4dI7NxrRkHAlRWn3VGDkhjFnw7SR8FN3my7R-rHtWm9E9gSb_qVijYTBGceaFLN3SmByo52UGN1DXF9qqhDY7X0gOvDUIaMQHeHQ07hlZQY68p7LGdcXv7z0Bz5M_WEGEINxWgKeTPw8r6wkftmf65BeJ4vEnfYWuFjOmGSHBnVMCTILOHpOCHLlvXrviKa5q9MX9ounRz32BVRORtsZWDKST6PXz0t-jlV4K1QmyYrEQDtiX5EcVpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca2821921.mp4?token=W2oyY_lN8iczLWMGJdEos37wLECkfAw7jZ2fgTA4paELEHrtyL_p5Q1gED-fYNfOWRdwsPW2Mc6ypKiGSj2A3g7dcmwgggs4dI7NxrRkHAlRWn3VGDkhjFnw7SR8FN3my7R-rHtWm9E9gSb_qVijYTBGceaFLN3SmByo52UGN1DXF9qqhDY7X0gOvDUIaMQHeHQ07hlZQY68p7LGdcXv7z0Bz5M_WEGEINxWgKeTPw8r6wkftmf65BeJ4vEnfYWuFjOmGSHBnVMCTILOHpOCHLlvXrviKa5q9MX9ounRz32BVRORtsZWDKST6PXz0t-jlV4K1QmyYrEQDtiX5EcVpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ قلاده خرس قهوه‌ای در ارتفاعات جنگل‌های هیرکانی لنگرود مقابل دوربین‌ها ظاهر شدند
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/675965" target="_blank">📅 10:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675961">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2185a55d9.mp4?token=MoVdaWp2DzWS-dlx-5wxXkJaPNtrV45IFfLLJkSJLm0XSOfY4dbS02IIWjw-yoO9s-11TeC0L7Cbtophw4wsQu0q_aPV1RswYxIcBRDH5rnPijYBg5uuYE4iC23Dwn5BnHyf3b-tl42Ab-Jysz5JB0On-6iDhK8Eeh3BI4Aw9sDnX0XeK6ypxqAu2u6XfbJHbGhROc2nPa0hLBwgH6ybpE2R-8FGQMGMdDzOiK81Xc17TrfQslNEMWAxhoJwNreyMGXtS7gd4Lg_8onPyBkHz8TCc7xN_lylVt9igsJxiCtDsxXxZEwX3k_uwXJ69s_7gSRaUVeh4FoHCI3rXgFpmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2185a55d9.mp4?token=MoVdaWp2DzWS-dlx-5wxXkJaPNtrV45IFfLLJkSJLm0XSOfY4dbS02IIWjw-yoO9s-11TeC0L7Cbtophw4wsQu0q_aPV1RswYxIcBRDH5rnPijYBg5uuYE4iC23Dwn5BnHyf3b-tl42Ab-Jysz5JB0On-6iDhK8Eeh3BI4Aw9sDnX0XeK6ypxqAu2u6XfbJHbGhROc2nPa0hLBwgH6ybpE2R-8FGQMGMdDzOiK81Xc17TrfQslNEMWAxhoJwNreyMGXtS7gd4Lg_8onPyBkHz8TCc7xN_lylVt9igsJxiCtDsxXxZEwX3k_uwXJ69s_7gSRaUVeh4FoHCI3rXgFpmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاستا آلفردو رو با این روش درست کن ببین چی می‌شه
😍
مواد لازم:
🔹
پاستا یک بسته
🔹
سینه مرغ یک عدد
🔹
قارچ به تعداد دلخواه‌تون
🔹
خامه نصف بسته
🔹
شیر یک لیوان
🔹
سیر ۱ یا ۲ حبه
🔹
کره یا روغن مقدار لازم
🔹
نمک و فلفل سیاه به مقدار لازم  #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/675961" target="_blank">📅 10:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675956">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
صدور آنی کارت سوخت به کجا رسید؟
🔹
متقاضیان می‌توانند با مراجعه به سامانه درخواست خود را به‌صورت کاملاً الکترونیکی ثبت کنند، رمز کارت را از طریق پیامک دریافت کرده و گزینه دریافت حضوری کارت را انتخاب کنند.
🔹
زمان صدور کارت از حدود یک ماه در روش قدیمی به یک روز کاهش یافته است. امکان ثبت غیرحضوری درخواست، پیگیری الکترونیکی مراحل صدور و تحویل حضوری فوری کارت، بدون نیاز به ارسال پستی، فراهم شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/675956" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675954">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26251840a6.mp4?token=K_bF--DQtwUkaCdxXnGscNOFni-GwYkTnAf1I4bY5pUFGhUOD-spzTByMCxU5-mTLPnClQyU4RLp57Lhfp4aq65vkQwPWtBD3jDbGeigw4q5Wi0z3K4grm0xrIOR76dror8zuNJvi6eQlX8gTre7ifj10B43qKgkh_cxyehpT7CAPQHnkxESJ0FtrQlwBkYuz2_XEju-vmkvf2ls-EzCjULjPQ64gKGqzho8Se0NKSSkuCJ1AQC8NvxtZAjEomoh7AWmbD6zFQh0BsJwQln6gXzM8YLE32yVzbCg5NmPDZ1xKw_v4uFMtFqB0k3OqMUCqkUk7X9wcDz_TNn84NgATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26251840a6.mp4?token=K_bF--DQtwUkaCdxXnGscNOFni-GwYkTnAf1I4bY5pUFGhUOD-spzTByMCxU5-mTLPnClQyU4RLp57Lhfp4aq65vkQwPWtBD3jDbGeigw4q5Wi0z3K4grm0xrIOR76dror8zuNJvi6eQlX8gTre7ifj10B43qKgkh_cxyehpT7CAPQHnkxESJ0FtrQlwBkYuz2_XEju-vmkvf2ls-EzCjULjPQ64gKGqzho8Se0NKSSkuCJ1AQC8NvxtZAjEomoh7AWmbD6zFQh0BsJwQln6gXzM8YLE32yVzbCg5NmPDZ1xKw_v4uFMtFqB0k3OqMUCqkUk7X9wcDz_TNn84NgATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با دوتا متریال ساده، یک آباژور مینیمال جذاب درست کن
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/675954" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675952">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6f327b73b.mp4?token=GFZIlwIg4KQje3CqW3r6M3vC8kH-P_miOJdnt70DktZSPVqq6Cgqyb10RDSOn53tFDtlcd0pidRc9Ar0j8JC24d2iER4ZGcJ2D5iMi55pq-QyorKPESHJ0JiSTG2stMooPjt284IP4UYVn-dUjHb6wFUaKiHAiY-9SZyp_mq0k0TRj2d5Ux_pYH7JNMAfMLh4Im_2WBGgqCbvFuSnA2558UmHjBQUOQRNjDOfdqFm0fPvNAeijO03DD97fdCNqzbteFAGJqSD92pU_q-GV41Pyx8wRlQHNYlpB1ITkQat5oKYFZKhyvRUSdmANSqL5TDRvkyKzEQGHs7wCLOwHrlI3LG1QHVmPqBbAG1jVcklAYd_duSwNxsUsmWv8ImINIxJOPpkT55NbrEMSjTIXNsZOlSt5K1Iwg5HpkESW6UrkRaP8rllCGwXtGiVne1Mk-SuqXH49fSPpRQz_qIa3unpZqftqP-Qf30-LwF-4AvmXDEL5lHlmhaV2-rpQiDjw2zkcYXrEPXZEoKSU6zALLkpQTQokLZthOy59JR2Ng4dJbrNH9jw42qGS_XY_40tUEbnRPrDjfImLi-jx7bzs-8hWBcYctITTaPm27j8wO2keXDO-HZNdckwiXk_Pdgzlxr1nvqYxOypU_I148zNkJHC_s1Ijo-AfPxT-tZDWjZbfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6f327b73b.mp4?token=GFZIlwIg4KQje3CqW3r6M3vC8kH-P_miOJdnt70DktZSPVqq6Cgqyb10RDSOn53tFDtlcd0pidRc9Ar0j8JC24d2iER4ZGcJ2D5iMi55pq-QyorKPESHJ0JiSTG2stMooPjt284IP4UYVn-dUjHb6wFUaKiHAiY-9SZyp_mq0k0TRj2d5Ux_pYH7JNMAfMLh4Im_2WBGgqCbvFuSnA2558UmHjBQUOQRNjDOfdqFm0fPvNAeijO03DD97fdCNqzbteFAGJqSD92pU_q-GV41Pyx8wRlQHNYlpB1ITkQat5oKYFZKhyvRUSdmANSqL5TDRvkyKzEQGHs7wCLOwHrlI3LG1QHVmPqBbAG1jVcklAYd_duSwNxsUsmWv8ImINIxJOPpkT55NbrEMSjTIXNsZOlSt5K1Iwg5HpkESW6UrkRaP8rllCGwXtGiVne1Mk-SuqXH49fSPpRQz_qIa3unpZqftqP-Qf30-LwF-4AvmXDEL5lHlmhaV2-rpQiDjw2zkcYXrEPXZEoKSU6zALLkpQTQokLZthOy59JR2Ng4dJbrNH9jw42qGS_XY_40tUEbnRPrDjfImLi-jx7bzs-8hWBcYctITTaPm27j8wO2keXDO-HZNdckwiXk_Pdgzlxr1nvqYxOypU_I148zNkJHC_s1Ijo-AfPxT-tZDWjZbfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه‌ فرود اسپیس‌ایکس استارشیپ بین پروازهای ۱۲ و ۱۳
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/675952" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675946">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی دو تن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه سال گذشته اجرا شد/ میزان  #اخبار_اصفهان در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/675946" target="_blank">📅 08:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675945">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/382e9450a5.mp4?token=k5s5oETII_Wm1I3PjoUqD7vQvmTrfRXjSRqA6p7pacsvPU8kogI1lyLyZ7Z4D1KfnYt2lGErkJN_ONPxTGPa7OzR0RMna-u16Kv_kcLBP0BE_JekketQ33agQeQ1iKisCphJQkof4GnW0x55RBKSAbGScNaYZ-dkAuZg9ADTGUbluTzbUIH7ROcQztSHgixNsVJEGMBvNt_hjZl43_TpCwGKM4oNa0nwI17QlUJrF31i-pA-sxIyG9Ogpb-5NbN6dlefPaKUSIeUv716X08ORaeddKquwu1te-Kj4wwejeKWRUJv6d_j-G41QjhZNxMiufmcD6YRupRDwiUw8mw6iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/382e9450a5.mp4?token=k5s5oETII_Wm1I3PjoUqD7vQvmTrfRXjSRqA6p7pacsvPU8kogI1lyLyZ7Z4D1KfnYt2lGErkJN_ONPxTGPa7OzR0RMna-u16Kv_kcLBP0BE_JekketQ33agQeQ1iKisCphJQkof4GnW0x55RBKSAbGScNaYZ-dkAuZg9ADTGUbluTzbUIH7ROcQztSHgixNsVJEGMBvNt_hjZl43_TpCwGKM4oNa0nwI17QlUJrF31i-pA-sxIyG9Ogpb-5NbN6dlefPaKUSIeUv716X08ORaeddKquwu1te-Kj4wwejeKWRUJv6d_j-G41QjhZNxMiufmcD6YRupRDwiUw8mw6iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زانو درد رو تحمل نکن
🦵
🔹
گاهی با چند تغییر ساده و انجام تمرینات صحیح، می‌شه فشار روی زانو رو کم کرد و درد رو تا حد زیادی کاهش داد #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/675945" target="_blank">📅 08:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaEOB7vRsoRP6w-wz-cOpV61FAMno6d5vgye-l1T5efWUVVDDsD9EuFpjzCWPtGJGJVzYC1QnbCd6aoSxW-SbNoEEQxk6LayY9YU_mtvpCfrBuH_GF77nQ8ID77gW_Vgh9FoMr9cInRYjTt6MrJbjBqXwBWx8dajMiQkejESqfkrKLToAEuYd9yrsz1Hq54xz3Tof7xTEqCNceYyZdmTtLOCKg_p8NU56zHhCLFHLXnBKWnryeoeQsUF6grBFMWjjtahgwBYfOAu3gqyxhAhTr_gQ5RoIH5kKNE8RxH-7Z4PAiyQo3cKaKbCW2nimKxLVca6qSqPBBvuLag_cY9UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۶ مرداد ماه
۱۳ صفر ‌۱۴۴۸
۲۸ جولای ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/675943" target="_blank">📅 07:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675941">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
مدارس از مهر حضوری هستند
وزیر آموزش‌وپرورش:
🔹
تلاش ما این است که تمام مدارس کشور سال تحصیلی جدید را به‌صورت حضوری و با کمترین دغدغه و مشکل آغاز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/akhbarefori/675941" target="_blank">📅 06:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
حکم اعدام ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی دو تن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه سال گذشته اجرا شد/ میزان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/675938" target="_blank">📅 05:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675936">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czo0vE-CeWlggnZ67Lv3CtMoZmnOqNuVVWu_RhY6ABy80vo4i3KFBSfwVr8xhurVSescAg53lXs9m2F92_82X1v1Fix0JkPWajUcKPETQy3nPctUPo3UXVr7eBIF3Dsmu8ccwJaOZdT29-jHJdASpi72DuCgcEoNwkSVzw_An5g8FmJZLJ2QwvXz1AcPkkd7D2g4tvsX6xVbzNaZoXlHm-dPXjGCd8t2KBa9Ox05vIr8Jgctfm7ldA1aPFuM7s2739yYUeMgBXO6GwCi6vjPpTk3rJECyDyWF1XrE3gvpLnjSe8Yl37fBDelKFhxFmG4ME7fyv2MCh-fX3LKg2BCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز حساس واشنگتن؛ از موجودی موشک‌های آمریکا چقدر باقی مانده است؟
🔹
وال‌استریت ژورنال در گزارشی به بررسی وضعیت حساس موجودی موشک‌های آمریکا پس از حدود پنج ماه درگیری در جنگ با ایران پرداخته است. این گزارش که روز گذشته منتشر شده، بر نگرانی‌های داخلی دولت…</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/akhbarefori/675936" target="_blank">📅 04:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
بزرگ‌ترین تأسیسات پالایشی عربستان از کار افتاد
🔹
شرکت آرامکوی عربستان پس از حملات پهپادی یمن، فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در بقیق را متوقف کرد.
🔹
ساعاتی پیش یمن اعلام کرد که با پهپاد خط لولۀ انتقال نفت از شرق عربستان یعنی همان خط لو‌له‌ای نفت را بدون تنگۀ هرمز به بندر ینبع در دریای سرخ می‌رساند، هدف قرار داده است.
🔹
حالا شرکت آرامکوی تمامی فعالیت خود در این تاسیسات را متوقف و در چندین سایت تولید نفت، عملیات مشعل‌سوزی اضطراری را آغاز کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/akhbarefori/675933" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675932">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7j7Gj3ZO124eubdh0utRnBAUKL1mf6vB3-oUM1BClUYI7tnKip1YR7OYa43T_EyBIOrG8LLVvNEVtPIAtrGJjO67B3UJznvpcdQ-WSVeow9hxeTh39pkz4ftuF0S-VVnlin0sIclFgCMMdNAVD3MNPJHQD5O9raxwnKjnIBLc4GVeFWqHPILxKN_j25j7lp8UtAgJfddUwlrKYIhLQof6hhpJfgCVrZBoc5Ah85rd--GJMB69fmcMIOQ21WaY65LUiUlWjC7mlIr7KjlpePS13SL3y20u4-xOGiE1KPdLapavwa24BOG9_Hjy3cBQba6tg5l4_1eITIwb_HFWN7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز حساس واشنگتن؛ از موجودی موشک‌های آمریکا چقدر باقی مانده است؟
🔹
وال‌استریت ژورنال در گزارشی به بررسی وضعیت حساس موجودی موشک‌های آمریکا پس از حدود پنج ماه درگیری در جنگ با ایران پرداخته است. این گزارش که روز گذشته منتشر شده، بر نگرانی‌های داخلی دولت آمریکا در مورد کاهش شدید ذخایر مهمات دقیق، به‌ویژه موشک‌های تهاجمی و پدافندی تمرکز دارد.
🔹
طبق تحلیل‌های مرکز مطالعات استراتژیک و بین‌المللی (CSIS)، ذخایر برخی از این موشک‌ها به شدت کاهش یافته: مثلاً حدود ۳۰٪ تاماهاوک‌ها، نزدیک به نیمی از Patriot و THAAD، و بخش قابل توجهی از JASSM کاهش یافته است. بازسازی کامل این ذخایر ممکن است ۳ تا ۶ سال طول بکشد، حتی با افزایش تولید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/akhbarefori/675932" target="_blank">📅 02:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675930">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2952ea4a.mp4?token=jRRVHdjLYgPqAGC4JLx2pFvzaoiEIb-oGJJMCuexiIesaDwonu-iR3s6AQ0GJi3YYuZG5t85YIhHmo15viJ93uN49ZE6YPUEKzdq9PZiaD8IYKZKcyE_5L4FoP0HsYCV9OXLkNRAKTfxWHtJ4Cm3rzKp4XKwzA5Wzn8yh2tohfOxNHxOCnr6Xme8XVIxuTTICXkL1OlMA4SHc4bMH-ciKAVZrlQ0kn6zzSb-Pck1CVTkdewNW4jhGmybMVf-ptTz99mp1oyureu_GCD_AYkpMA6_AjGM6Kfsjjp9EUQL45QqbR-rXpn-Z8Q0t6zq_Lh8UuYjXLYl2NdLJcdHLTGckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2952ea4a.mp4?token=jRRVHdjLYgPqAGC4JLx2pFvzaoiEIb-oGJJMCuexiIesaDwonu-iR3s6AQ0GJi3YYuZG5t85YIhHmo15viJ93uN49ZE6YPUEKzdq9PZiaD8IYKZKcyE_5L4FoP0HsYCV9OXLkNRAKTfxWHtJ4Cm3rzKp4XKwzA5Wzn8yh2tohfOxNHxOCnr6Xme8XVIxuTTICXkL1OlMA4SHc4bMH-ciKAVZrlQ0kn6zzSb-Pck1CVTkdewNW4jhGmybMVf-ptTz99mp1oyureu_GCD_AYkpMA6_AjGM6Kfsjjp9EUQL45QqbR-rXpn-Z8Q0t6zq_Lh8UuYjXLYl2NdLJcdHLTGckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو نخست وزیر رژيم صهیونیستی وارد واشنگتن شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/akhbarefori/675930" target="_blank">📅 01:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675925">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05b88909c6.mp4?token=p3BWW9Dov5L33xEIrPgj-lJtqpiakpLlKhIchFzxj7Mt6-qC5vIyuaS9oN_ciMPV3v25qi4YUI3UbPOB-uQWYjraaIO5Mt-0GsFkwJXnvsUWA7ytzDmeFzN67hEWHrKX2tItM2GXgHHSxVg9V3l9M2Sdr30j6CEKE4Ke2nHqokkOl3isc8uSfLdKi8CWF-sCyhRmASDqIH7niZ3FmXPBtAh4WSN9ovi0AUDHI-_Ruzl60oz0y9xfkzu-CJ3MFppZsk_l-d9D84DgdyF6caMllEzc_0aM1GZMSDLpgff6fCyc9qBBIYTamnPkYUGfleRVDIEmacecoPZ4aT24H8a2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05b88909c6.mp4?token=p3BWW9Dov5L33xEIrPgj-lJtqpiakpLlKhIchFzxj7Mt6-qC5vIyuaS9oN_ciMPV3v25qi4YUI3UbPOB-uQWYjraaIO5Mt-0GsFkwJXnvsUWA7ytzDmeFzN67hEWHrKX2tItM2GXgHHSxVg9V3l9M2Sdr30j6CEKE4Ke2nHqokkOl3isc8uSfLdKi8CWF-sCyhRmASDqIH7niZ3FmXPBtAh4WSN9ovi0AUDHI-_Ruzl60oz0y9xfkzu-CJ3MFppZsk_l-d9D84DgdyF6caMllEzc_0aM1GZMSDLpgff6fCyc9qBBIYTamnPkYUGfleRVDIEmacecoPZ4aT24H8a2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از انفجار و آتش‌سوزی در مخفیگاه‌های جدایی‌طلبان تروریست ضدایرانی در أربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/akhbarefori/675925" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675924">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
گزارش‌ها حاکی از آن است که کنسولگری آمریکا در أربیل
هدف قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/akhbarefori/675924" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675921">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a40bf5ed3.mp4?token=mU3CPxXyx93B2Vgu0AXkdCtgR1eUY7n8f0jqSOPGg3wOMDW6ALyr1dhAm1RhgWOef2YmXlS7CKVdHBYQ5H3b65Ub0n0PqpGyLM0NwuEeYy32hXMAuIjXTTTJmbbVK6vSVslszj_jFEUQcQNxyUF1-7--b1WOaPrFdoxKSa_d_BVKqVIHubRCOvzWGjtn0eWU5H9m-uHlOvul0Cl0hndfmLJTiwSXhxmtK1_UH4kYvyEs6ZGnJ2AixGSgbYCreGw5X2HWFoUOXyABT3ZhFa-svPevHFJYHRlL8ygCi_ZcgJCgdbAlUgSGA_BCJckB8_kfPUNlyyPd49i7pLiVZGfAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a40bf5ed3.mp4?token=mU3CPxXyx93B2Vgu0AXkdCtgR1eUY7n8f0jqSOPGg3wOMDW6ALyr1dhAm1RhgWOef2YmXlS7CKVdHBYQ5H3b65Ub0n0PqpGyLM0NwuEeYy32hXMAuIjXTTTJmbbVK6vSVslszj_jFEUQcQNxyUF1-7--b1WOaPrFdoxKSa_d_BVKqVIHubRCOvzWGjtn0eWU5H9m-uHlOvul0Cl0hndfmLJTiwSXhxmtK1_UH4kYvyEs6ZGnJ2AixGSgbYCreGw5X2HWFoUOXyABT3ZhFa-svPevHFJYHRlL8ygCi_ZcgJCgdbAlUgSGA_BCJckB8_kfPUNlyyPd49i7pLiVZGfAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات به تجزیه‌طلب‌های ضدایرانی در أربیل
رسانه عراقی:
🔹
تاسیسات راداری و مقرهای تروریستی در مناطق خلیفان و سوران در استان اربیل هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/akhbarefori/675921" target="_blank">📅 00:46 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
