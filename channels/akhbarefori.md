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
<img src="https://cdn4.telesco.pe/file/XsC6sW3Ug4EOkokJQpk_lMnxVg9_YQ0I4pzD-VZsv1pRr7dvE1TahgD4Brr_EZbxf47ZbsGbKd6K3AgHnImN6wUt4VZ8nGqlOmHEzKTUptt3oEB0AKU-HeL5Y3YLeB2LZFRCGsSul7ZKgIuELS1FMsDvFADoh8vOcBlxewx5omDIpF3zoCBX5L24X2lIlHRzrauF6-Oy_y-TaId4HRaV0aZ_BhaWIQFaZfbWE-ppm8oatz-G-iUXwNWAN2EOByoXic-e4iwxL3e4J-yaM24SeLM9YrsMiMBJ1oDPCdQG5FNx56XGii6V83gZKJ4CIEfKrnDOWIzqkTakku2YyHnuVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.27M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 13:15:04</div>
<hr>

<div class="tg-post" id="msg-672908">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neSr6tbPHhxwKb5sQAdZZpMUD4_yOA9wjTdmALwowgm82tAUSWdJDg5XU14wlnTXJxx8pqgLVh-bUWhVEcTGNjBZgbLw2XO4txTL2r0AdvnQuhM3hmf7CIKhacOuWSFt1SrX7CZ_XpHP-qVsktXGWqPms6j340s8Xv6O1aSGIYwlPb-jWh44PfL2ctnPL5VqEsGgFP8IkBBSLFZJk-Y8DcOMDickiuN0NKzyeSq-2kxbRavVEyZIbm4hgjycd8FXrbSioql5n6NmYYJkijVF6MVHR_PlIdHa5PyTfyJAYudVmk3MBCDA2W8Z7Pp_unpwZXk7ntg7P45M8t52M695-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پهپاد دشمن در دهلران استان ایلام ساقط شد
🔹
فرماندار ویژه دهلران از ساقط شدن یک پهپاد نظامی دشمن بامداد امروز (یک‌شنبه ۲۸ تیر) در اطراف روستای «عین‌خوش» در این شهرستان خبر داد.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/672908" target="_blank">📅 13:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672907">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9323938ddd.mp4?token=JpHu_vpop7av1qYGDi0egXe34yjwzStcFkFZNqfHLlHKk5MkboGzwsWXaXpA99UbbS8kuuFb0fckMsNNfWO_ebNZJuy1VSmrhzMXeldQ7t-yt3gAG4J55HfdwErOv-sPsnT1BS7fc2zJLLDFClzXM6il3v1E6nFqUWvjv_pgM7XofpopvXtJz3adKO_stEn9NnqWOELdGWWP97uPDksEnl6rJ6yGInViphkSYBYelnZAltTzMRVMSCzKikB6x8i7vn3qmNTIYBKILXr-cNwXUDSoXo0sdQPIEAFbFtiKYbTucGepB5YOCHURhdfONwpALJOfapc7Pb9Da5jHlAc_bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9323938ddd.mp4?token=JpHu_vpop7av1qYGDi0egXe34yjwzStcFkFZNqfHLlHKk5MkboGzwsWXaXpA99UbbS8kuuFb0fckMsNNfWO_ebNZJuy1VSmrhzMXeldQ7t-yt3gAG4J55HfdwErOv-sPsnT1BS7fc2zJLLDFClzXM6il3v1E6nFqUWvjv_pgM7XofpopvXtJz3adKO_stEn9NnqWOELdGWWP97uPDksEnl6rJ6yGInViphkSYBYelnZAltTzMRVMSCzKikB6x8i7vn3qmNTIYBKILXr-cNwXUDSoXo0sdQPIEAFbFtiKYbTucGepB5YOCHURhdfONwpALJOfapc7Pb9Da5jHlAc_bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسمت چیه؟ احمد نادری
کلاس چندمی؟ دوم راهنمایی
کارتون چیه؟ "دفاع از خلیج فارس‌
"</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/672907" target="_blank">📅 13:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672905">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=NoDLYEGemEphDYKi0Z9YK-NIrAUhkfOg0tyhDkoO4_IyH9KlOb8-t6c9ge4CN1JnuUww1yTXNeMbXnJm9UshkCvMVi1UHudhEVYrmpFUf89VoLKhsugDWxCQPveVRfDscze-AjJykFkdj4UckJRIsosDbs9l5TJU1_Wlo0AhsOHjW_hf-OSFjruZ8LAnu0ly5b1JbA49QdKvCnftukm-Cns2tl3khzYDeyCgj35RkMD2hSV7TcB9qvpmdlkYrGGqpmcgG9zI5yYgap0GFrZkHY5VcrMkJa9xRfhc4bhRh0JglRw-DNaJQlbUwaEHgpB2x6zC483Z1b7v1IqIrIOEMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=NoDLYEGemEphDYKi0Z9YK-NIrAUhkfOg0tyhDkoO4_IyH9KlOb8-t6c9ge4CN1JnuUww1yTXNeMbXnJm9UshkCvMVi1UHudhEVYrmpFUf89VoLKhsugDWxCQPveVRfDscze-AjJykFkdj4UckJRIsosDbs9l5TJU1_Wlo0AhsOHjW_hf-OSFjruZ8LAnu0ly5b1JbA49QdKvCnftukm-Cns2tl3khzYDeyCgj35RkMD2hSV7TcB9qvpmdlkYrGGqpmcgG9zI5yYgap0GFrZkHY5VcrMkJa9xRfhc4bhRh0JglRw-DNaJQlbUwaEHgpB2x6zC483Z1b7v1IqIrIOEMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدادیان: رهبر امت به ما وعدهٔ پیروزی داده/ مردم‌سالاری دینی در دورهٔ رهبر شهید به بالاترین حد خود رسید و کار را به ملت مبعوث شده سپردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/akhbarefori/672905" target="_blank">📅 13:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672904">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
دو کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند
نیروی دریایی سپاه پاسداران انقلاب‌ اسلامی:
🔹
ساعاتی پیش چهار فروند کشتی  متخلف با شیطنت و حمایت تروریست‌های امریکایی و با خاموش نمودن سامانه های ناوبری و بی‌توجهی به اخطارهای پایگاه کنترل تنگه هرمز نیروی دریایی سپاه، قصد اخلال و خروج از تنگه هرمز را از مسیر ناامین داشتند که دو فروند از آنها دچار حادثه شده، در جای خود متوقف گردیدند و دو فروند دیگر از ادامه مسیر منصرف شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/akhbarefori/672904" target="_blank">📅 13:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672903">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD01RZ5bgryfC7hzhbYWMNPx9l7bzz0ZJyaePHBN4nB9jj0HzLmx2MWFoEk3jT5Uems0AnoqgNBdhj-DcwV_aPnp3UV8a-W4bgiLNYs-ubNjgcTR1Tq3obm5eShykTe49B8LozYBMYBUJXewHrEzUxmcr2gkoNcp0qxk2vseWv-_pCG1C868Ud-jVGJwRvrIx1--bBsscfGru5dVbEXq2vvULkhq8cUkMmS4k3_sdQEKXEEs9h3zSezJjSRHep48JQVhIWbXdlOt6_ntBQtyf1zkFs1wfYmNJMjiPBXy3Kc4CnYo4Vn-5mx1rbchg6q9irJn2yry9SeI0O2Nk2f7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: اطاعت از حکم رهبر معظم انقلاب در اصرار بر اتحاد مقدس، شرط ضروری پیروزی در میدان مبارزه با دشمن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/672903" target="_blank">📅 13:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672902">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDSfIGZDO8FNMbguUngfipVwq3oVP0uTVlcfe1QZu11TInQQn9qrACXSH95s490fBKvSJG0Mp3k722r6pH2yHXAsr7JRqXmnI_xNfsSrSEA5l1OG77I9pHp0IU6SqqBftlUJifVh6sZ9l4H2Y-C0nlGgxtlK2gDI96HRD8Sc3hSqtr0Pb6k5njyvixEDT56PJ1oRRewwBpnC79Fk75sbO4X8qflV6hRN8O9z5EJd4S7xnG7jPg4nQShwfXtWukIyxvv_JPYXNLkFd0uQ0JQ8RwuOYRFBhwii42splAWvu1VgqhcTn8wnS-r0c5adx5wPvPet467zMYSmbWL8TM7fMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام و فیسبوک از دسترس خارج شدند؛ مشکل جهانیه، نه اینترنت ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/akhbarefori/672902" target="_blank">📅 13:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672901">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkYDzOA89Flb3duS2KRILc7ZY_tRvPzCQjINlw--TQMcmFvo4qMZ0ily96KKUhCZRSkpc1ulm7t0i35LBfm4Tc5x4D_rvTx73rwCcW-mnDSYcq_AhLjE48TJKG9tuwhKEhGXy3sH9Ahohcc1AB06s7d1qoeX7RrvNppV13_mrST8gVrN-hcWx657cBp0kSYdE8EYBM_Jg9dWTR20Hncmpih8_dfr2mqW-9VCXWJ0pYydzjmFyfegTv7-WvbfeFKVjrS4XYEUBHFlApVm2RV1rt_FFBCc3dqGDyI624JnOU1K_VcepApej7vohgQ7ygbmkCD0wpjHIWaEzjWEk6cMJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۸ تیر ۱۴۰۵؛ ساعت ۱۲:۵۰
🔹
دلار امروز روی ۱۹۲ هزار تومان بدون تغییر ماند و پس از ورود به کریدور ۱۹۰ هزار تومانی، فعلاً در همین محدوده متوقف شد.
🔹
همزمان با تداوم تنش‌های نظامی و ابهام بر سر تنگه هرمز، بازار هم در فاز احتیاط و انتظار قرار گرفته است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/akhbarefori/672901" target="_blank">📅 13:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f055e0bca.mp4?token=jEN1MC7mtqYI7GBK0RIdgCrQIzYGVfVPsLrvyuwkOFuiiR_LkAuc2SQq05ImCFYxL7v81s_7npLTTUl6fQ-w0QLvzHk03IOYfvEc4ghD3F2JTRvfZAtUP5C5F6sNaEkQJd16Of_PZVPOXlTqs5yb8VmIIBFXR89xV6eqb_H8VGFrC6-wJph8EZUi6q1bAobP-lPI2OpZQ7JUQxz7xQZ8sXScTFdfkd5ZaFCeyoxCVxGz_uxANkiktjsfK5rPPXHzm4lFOLh4Vfb3nStPvMJREij_3BPEam4_2H9Cr6SrPeSeBAUutu3mhZq3-ZJ4RszJrm8GvmUGoqbTBfMb1VCR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f055e0bca.mp4?token=jEN1MC7mtqYI7GBK0RIdgCrQIzYGVfVPsLrvyuwkOFuiiR_LkAuc2SQq05ImCFYxL7v81s_7npLTTUl6fQ-w0QLvzHk03IOYfvEc4ghD3F2JTRvfZAtUP5C5F6sNaEkQJd16Of_PZVPOXlTqs5yb8VmIIBFXR89xV6eqb_H8VGFrC6-wJph8EZUi6q1bAobP-lPI2OpZQ7JUQxz7xQZ8sXScTFdfkd5ZaFCeyoxCVxGz_uxANkiktjsfK5rPPXHzm4lFOLh4Vfb3nStPvMJREij_3BPEam4_2H9Cr6SrPeSeBAUutu3mhZq3-ZJ4RszJrm8GvmUGoqbTBfMb1VCR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه دیشب بیدار نبودین، یکی از دیوونه‌ترین بازی‌های سال رو از دست دادین؛ حالا امشب نوبت فینال آرژانتین و اسپانیاست
▪️
قسمت شانزدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/akhbarefori/672900" target="_blank">📅 12:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672898">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فراخوان مشمولان اعزامی پایه خدمتی مرداد ۱۴۰۵
سازمان وظیفه عمومی فراجا:
🔹
کلیه مشمولان دارای برگ آماده به خدمت به تاریخ مرداد ۱۴۰۵ می‌بایست در محل و مراکز مندرج در برگ معرفی‌نامه مشمولان حضور یابند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/672898" target="_blank">📅 12:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672897">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b96146359.mp4?token=I81pFAhZ2e4pyL0yw3QGkGSBcglhSKFOP3LZvCnE7h6Dp49mdRuB5t2EGmsnX-To1eO7Q3uvs-JczZGISxEQDOmi8Cro8_XNa3f7RrGR7asi-QjmXfOgfXa4_lYUm7aengXyONXqW4Xl3pPYsV3D5mHsQ2-twSI8Ygm34YFp-zpCpdVlmr3RweyY-PgTX4fgH128bKXO3ZoMrKnZkDN9-VtvuQMw8xfLkC7HP-GZ-jCDghYlK6iI3bfxFQHdP55oeRVJdlzb6AI822yayVesyoelDolXxHx9dM4IBZgM0tP6KUq0mYyy7BXMmBEc79yuHtLxPCyCx8Yi0HsQAccU0RQlzFWynCjZ_9sJmov0HjlAifFVUQHJdU2UjhmGZ0CcWetwqvFERVzaIJVggSINdKAjvpDbvphyP4ekydrLznMrmd6V49GxuBZ-vQ0epoxC3f-MJUAuiQFsGuwZ2HgyNXCafYr8Fbt0gbqqSA7jt4cGTGG_gxdyEZelttwSP224Qlsln7x4ThHBA3wPI20biAV_aTaWyWIBLQd93Z-GrtYkrqn70FoMVYgTg6VM_f6Mqcm42dKYl99VcmQWFPt2OjzGoyJtaICzVROfB7DFtMM_z0Ag2VcWDG7sY-ugkEJbZC_M1y5U1wTuhzKNrEtsWHCFt_nJndMdVtLI7tuRkQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b96146359.mp4?token=I81pFAhZ2e4pyL0yw3QGkGSBcglhSKFOP3LZvCnE7h6Dp49mdRuB5t2EGmsnX-To1eO7Q3uvs-JczZGISxEQDOmi8Cro8_XNa3f7RrGR7asi-QjmXfOgfXa4_lYUm7aengXyONXqW4Xl3pPYsV3D5mHsQ2-twSI8Ygm34YFp-zpCpdVlmr3RweyY-PgTX4fgH128bKXO3ZoMrKnZkDN9-VtvuQMw8xfLkC7HP-GZ-jCDghYlK6iI3bfxFQHdP55oeRVJdlzb6AI822yayVesyoelDolXxHx9dM4IBZgM0tP6KUq0mYyy7BXMmBEc79yuHtLxPCyCx8Yi0HsQAccU0RQlzFWynCjZ_9sJmov0HjlAifFVUQHJdU2UjhmGZ0CcWetwqvFERVzaIJVggSINdKAjvpDbvphyP4ekydrLznMrmd6V49GxuBZ-vQ0epoxC3f-MJUAuiQFsGuwZ2HgyNXCafYr8Fbt0gbqqSA7jt4cGTGG_gxdyEZelttwSP224Qlsln7x4ThHBA3wPI20biAV_aTaWyWIBLQd93Z-GrtYkrqn70FoMVYgTg6VM_f6Mqcm42dKYl99VcmQWFPt2OjzGoyJtaICzVROfB7DFtMM_z0Ag2VcWDG7sY-ugkEJbZC_M1y5U1wTuhzKNrEtsWHCFt_nJndMdVtLI7tuRkQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحید شمسایی: به جنوب کشور آمده‌ام تا از مردم اینجا دلاوری، سخت‌کوشی و میهن‎دوستی یاد بگیرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/672897" target="_blank">📅 12:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672896">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وال‌استریت ژورنال: ایران از آتش‌بس اخیر برای صادرات نفت خود به چین استفاده کرد.
🔹
دبیر تشییع رهبر‌شهید ایران: بیش از ۴۰ میلیون نفر در مراسم تشییع رهبر شهید انقلاب شرکت کردند.
🔹
ادعای مقام اسرائیلی: تل‌آویو ممکن است در کنار ایالات متحده به جنگ بپیوندد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/672896" target="_blank">📅 12:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672895">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رسانه‌ها از انفجارها در شهر حمد بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/672895" target="_blank">📅 12:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672894">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5gCi2PP8wn1fXf1JhgyiQoBKg7XJ0iw3KL2dWYw35GAjjshDk5STdnRPLkTkiG4smmWlkrBKBCgi5IX3JjdsK2_zPQZo0p8KT27iFgVS3ea88cOyfwv6KQiMVLBWPaw1Lrz29zsznHg6UcLVpPczX-rQDEjxVg-fvSlGesJ7FIAneGgXuaYeU9osWwBvqYl5EypW9qEdxSa025R6LxxJm_nh8K-bbzxWAv4X0enRVBF7Wxefmrg8GKODFJCVDPD36HfUxKbBhVWoZYLQFmyqHjKJ05U_qRLlk2T_oKZHjpArpLeeqEhKLYqMklAzNubeH0rvpKtDB-gihItJRIlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدون اعتبار، بدون ارزش
🔹
نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران ایران و امریکا بار دیگر این حقیقت را به همگان ثابت کرد که امضای رئیس‌جمهور امریکا چقدر بی‌ارزش و نامعتبر است.
📜
بخشی از پیام رهبر معظّم انقلاب درباره‌ی حماسه عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور | ۲۶/تیر/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/672894" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672893">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA643PKtxfsvgqrBBEGtmo2BIUWJRz01ZV6wjc44Ng86yDbWid89T5I94pzvQt5haw9iVb9mVqBGKFdRQALXxoO0QYivfxeLFQx0-iIEeQVAdaoEg6sH0xTVonkjPoJVurhISwpvxJqeC7k0BMgLDFoSXAkphy7tvTTS6AS5u2fxc92uzoYArDqPyXsOeDws67kZs2JT74pzy5K_RMxAIU1WrfKyVT6tJKTw66uSg1bO--CLw3VwKMatZV0QrLII60dZG_4-5pRne7hEw_jG2yC59koc9GdktPKaYMFrHhC0miaC7tJdnSor7w3HuRQ0rMb1_0bN6liFiNKraT_OhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتو های عجیب روی بدن اوتامندی بازیکن آرژانتین ؛ بوم‌نقاشی است یا کمر انسان؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/672893" target="_blank">📅 12:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672892">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f18e2d1e.mp4?token=if-pYB749KPp2SWWzeReUMpLzvltP7jhHC5sOMLV5OGDJMZQb5f2Prr-Ukdha-WiWguscvoMlGmh8h2LcoNb7ITteTyNz3tGG1U4iAvvk4TlNlhgYMWPjTpJY1-G7qZQ0wLi3rr5oGPzt6l9OHmgTRQh9EPpwKG6pTjFkNSLPYtbEbp7kpAwMtpnpWVwQl1b18Cr6mHYRJxtssPtKb46k4ixwjlDvRshXb5rT_LITu4rItZIDsru9CFzivcA1bbq2kveHccXaTxpGrKezW240K6YynTmz_clAS3jvM4vMCZv_zmdaLIsBVWDzyvQ4u-9wlT_86GSrmPbooOGv2yd5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f18e2d1e.mp4?token=if-pYB749KPp2SWWzeReUMpLzvltP7jhHC5sOMLV5OGDJMZQb5f2Prr-Ukdha-WiWguscvoMlGmh8h2LcoNb7ITteTyNz3tGG1U4iAvvk4TlNlhgYMWPjTpJY1-G7qZQ0wLi3rr5oGPzt6l9OHmgTRQh9EPpwKG6pTjFkNSLPYtbEbp7kpAwMtpnpWVwQl1b18Cr6mHYRJxtssPtKb46k4ixwjlDvRshXb5rT_LITu4rItZIDsru9CFzivcA1bbq2kveHccXaTxpGrKezW240K6YynTmz_clAS3jvM4vMCZv_zmdaLIsBVWDzyvQ4u-9wlT_86GSrmPbooOGv2yd5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای یک‌بار هم که شده، به خودت باور داشته باش #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/672892" target="_blank">📅 12:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672891">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پایش شبانه در قلب شریان‌های جنوب؛ عزم وزیر راه و شهرسازی برای بازگشت نبض جاده‌ها
🔹
فرزانه صادق، وزیر راه و‌شهرسازی، در پی تهاجم ددمنشانه دشمن به پل‌ها و تونل‌های استان هرمزگان، شب‌هنگام راهی این استان شد تا به‌طور مستقیم بر روند بازگشایی، بازسازی و ایمن‌سازی محورها، پل‌ها و تونل‌های آسیب‌دیده جنوب نظارت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/672891" target="_blank">📅 12:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672890">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
حمله موشکی به کویت و اربیل عراق
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/672890" target="_blank">📅 12:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672889">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای سی‌ان‌ان: ترامپ به دنبال جنگی طولانی علیه ایران است.
🔹
جوزف عون، رئیس‌جمهور لبنان وارد واشنگتن شد.
🔹
جهاد دانشگاهی: ثبت‌نام دانشجویان برای سفر زمینی اربعین آغاز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/672889" target="_blank">📅 12:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d10d920.mp4?token=N3GVkQ-etnM3GqUwuujyezA59mm_Q4rbLvhOl7r1EeLbUKADTdv9Wa0vuJ5T1jY6T00As-BQhnD05aDq4_dm3UtC4P-tfoYIt_XOV-_jX0kVk1BWSgkqUIjIiCQocLRW5pdzYO7OvyIg4UMXESxd3Eo4HBOUH1GwMJXEg1mPo3dEq4M3BTqdf4iYf_4nUaBwK3jy2-wes5m4c3JmCXTWLV1UfthZlLsd7oew11jKTSE_1ds-_mVphm7AgQhLWBED8fvbTOuOHEuhjJ9Q1BWGq-sQRJF8R644mCWoUHVdRy4_KNfh7CsB7OcGBp5y2kT89Q2F74-8CgcPNqTI7U7I2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d10d920.mp4?token=N3GVkQ-etnM3GqUwuujyezA59mm_Q4rbLvhOl7r1EeLbUKADTdv9Wa0vuJ5T1jY6T00As-BQhnD05aDq4_dm3UtC4P-tfoYIt_XOV-_jX0kVk1BWSgkqUIjIiCQocLRW5pdzYO7OvyIg4UMXESxd3Eo4HBOUH1GwMJXEg1mPo3dEq4M3BTqdf4iYf_4nUaBwK3jy2-wes5m4c3JmCXTWLV1UfthZlLsd7oew11jKTSE_1ds-_mVphm7AgQhLWBED8fvbTOuOHEuhjJ9Q1BWGq-sQRJF8R644mCWoUHVdRy4_KNfh7CsB7OcGBp5y2kT89Q2F74-8CgcPNqTI7U7I2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام یک پهپاد MQ9 در اهواز
🔹
دقایقی قبل، یک پهپاد MQ9 با آتش سامانهٔ نوین پدافند پیشرفتهٔ نیروی هوافضای سپاه و تحت کنترل شبکهٔ یکپارچهٔ پدافند هوایی کشور، در آسمان اهواز ساقط شد.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/672888" target="_blank">📅 12:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7764fe68bf.mp4?token=JHFyJMF1LH7JtJEqrDge8vK_Tjw6OmLthWzmj2SN9zEqgUik0xXcQmKUvxTEFAMM38ZbjMmJFpgg6Mw1pjnfFJC7CkupIl_JJpTTGmm3313rTDHegXndWgcodkSndKk8ru3BBoom1nIoEw7yWY_Mg36DMqU7ILJi4ozkxAa4LtjCOHt7biDcS6POdzvby9kPtvUa621iL46wad1rzYdqGwlcqltNfruKDf84CtcNFiQhuuZHaElraGalwpTQbc6Vzfg3rmkmyQ_MCNJ4MQgN4AqEJUsfanR0He-vUug91spc3PNpQ6EWiIQ8lpj6nacl8HwP9IVsENtlH7kFWVEESg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7764fe68bf.mp4?token=JHFyJMF1LH7JtJEqrDge8vK_Tjw6OmLthWzmj2SN9zEqgUik0xXcQmKUvxTEFAMM38ZbjMmJFpgg6Mw1pjnfFJC7CkupIl_JJpTTGmm3313rTDHegXndWgcodkSndKk8ru3BBoom1nIoEw7yWY_Mg36DMqU7ILJi4ozkxAa4LtjCOHt7biDcS6POdzvby9kPtvUa621iL46wad1rzYdqGwlcqltNfruKDf84CtcNFiQhuuZHaElraGalwpTQbc6Vzfg3rmkmyQ_MCNJ4MQgN4AqEJUsfanR0He-vUug91spc3PNpQ6EWiIQ8lpj6nacl8HwP9IVsENtlH7kFWVEESg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز روز امتحانه و در روز امتحان جز دفاع از خاک راهی نیست! #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/672887" target="_blank">📅 12:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی بحرین در پی تشدید تنش‌های نظامی در منطقه فعالیت پروازی خود را متوقف کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/672886" target="_blank">📅 12:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krFQHisfU72ouKL8CcZmsVdhbEKMnIwysF3EPG4Vnc1nytuwD6gba41CisCMiE6FuikkK-POobua3XPK6yMUjIbh8ovft5JpZ3_WlZ5Bcoi1ynIHamMTax5HdLCV9gFx68vHzH4xlhELnAitn0_Yi4i46-yyR2J6vQGsJMmWLXs--bCw1IVy_cpqxbz1BKaJInMDocyhCU4j59xNh1eB2e05vHsWXHovnhBl2LDBauHtPr5y6CqxjaGr4Qb8huCl3XRxt6ydu6irFhRt0gMHSVW-mJ_jjr1oAVl6JTuxxE86zG7rmJqmd3h8-PwLY-LH0oYfs0xgv1NZxh14hh-sFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدن شما چه ساعتی خودش را بازسازی می‌کند؟!
⏰
#سلامتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/672885" target="_blank">📅 11:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای خطر فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/672884" target="_blank">📅 11:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
عبور از چالش‌های مالیاتی در بحران با مشاوره تخصصی اتاق تهران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مالیات، به بنگاه‌های اقتصادی کمک می‌کند از ظرفیت‌های قانونی، بخشودگی‌ها و تقسیط بدهی‌های مالیاتی استفاده کرده و فشار مالی ناشی از بحران و پسابحران را کاهش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672883" target="_blank">📅 11:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2e93e791.mp4?token=vT_FTuSX3CczT7eAR0GFk9NbxjQpyLcvYhZx_AYpYLQOe_2sO1QDKFrl-Ai9EABXqqFHTcfuY2BlhvQFfrfWIyAY51KTfZ2ByPyC-i7t4inuNanDqmoLDRdLj66WGMeLJoWI6GtAPrwkCMlQdOKb_2hx5O92zx4UAJKKncVnpfoqKemVaaJMjI65vpIvksmrc5qogzeuDGXMajKRwnmlWLY2UXcBkyZWpgtUHC1e5mFmBMCj-8mWXJdzpKUICnUcr3KRB4RtXZKay8tfjSH3Zzpm6Uy55uYXNqtvvNHTSpZJB4UPx9q2WNRX7XsnFFqXOPCrBzKdCpDnU2lz0XwBUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2e93e791.mp4?token=vT_FTuSX3CczT7eAR0GFk9NbxjQpyLcvYhZx_AYpYLQOe_2sO1QDKFrl-Ai9EABXqqFHTcfuY2BlhvQFfrfWIyAY51KTfZ2ByPyC-i7t4inuNanDqmoLDRdLj66WGMeLJoWI6GtAPrwkCMlQdOKb_2hx5O92zx4UAJKKncVnpfoqKemVaaJMjI65vpIvksmrc5qogzeuDGXMajKRwnmlWLY2UXcBkyZWpgtUHC1e5mFmBMCj-8mWXJdzpKUICnUcr3KRB4RtXZKay8tfjSH3Zzpm6Uy55uYXNqtvvNHTSpZJB4UPx9q2WNRX7XsnFFqXOPCrBzKdCpDnU2lz0XwBUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من به کشتی گیر آمریکایی باخت ندادم!
علی دبیر در خوزستان: مردم اینجا محکم ایستاده اند‌. ما هم آمدیم تا در کنارشان بایستیم و همه را دعوت می‌کنیم تا بیایند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/672882" target="_blank">📅 11:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgHv0FgBlk-XMws_rsMbrWWygHY4g_oJMR_OBExGRSLpvkQBpuQDajcV8ZpKd7OtayrSr9KYNrkDfKeepiNjPyEuRB_vkJHlAL3Yj6klYISplVN93SP5OBpD12YS7jcXc8O4s0fsQaApAZUTZOWhTTdtuGY8bs7b0hcSFz94YhuXoayLc7fUyu9HfpRSGyETzQq-HMMrRSj5I2LaUdStrH0UncKj6utpno_XeBa6fwI4yuGrOaUuMYiMcDaTcnIyWxZuQUVmOiMK2V_KXWOX5azVaU7CbKxNSYACR9IcS9f--muLkOrx_kbOtgFpQIxYCPbUT7GWm_LYZCoVqFAIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم اسپانیا قاتل فوتبال زیباست | چرا معتقدیم یک فینال کسل‌کننده را در پیش داریم؟ | این آرژانتین یکی از حماسی‌ترین تیم‌های ادوار جام است | همه‌چیز درباره فینال جام جهانی فوتبال
🔹
برای عشاق فوتبال، فینال جام جهانی نهایتِ آن چیزی است که وجود دارد. یک بازی که هر چهارسال یک بار برگزار می‌شود و تبعاتش به اندازه چهل سال می‌ماند.
نظر شما چیست؟ گپ و گفت خبرفوری دراین‌باره را ببینید و کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3231456</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672881" target="_blank">📅 11:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
به علت گرمای شدید هوا فعالیت تمامی ادارات در استان خوزستان فردا ۲۹ تیر به صورت دورکاری خواهد بود
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/672880" target="_blank">📅 11:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCauXsbvn9iaaYxvUjD-yuebd4sRP2pPr529ArhPqw42-u3fc4xir3aUcTz7h-754onIppIjbR_Plu7EMUwa9hjOqpBY1XhC8gFjzWJIggNmra5iZAIAtLm51-0TbZ8GpJEVt7J_Y2grQ-EKXjyfyy_7xi7HXjbPNNR80g2RcGyGzZH03PC_h3AtyBGnvWCCRZ6qMddkWfox_HrmN5qZfpJq4oq2kGTaMnDW2W1d3ziEF5nXHoPJC7UEhYz-tnk481NMhu2Coj6DpLYKy6uqXxEZwayPZirkmxmFjR1KZtGU0CwzXwNjPKTwadujAZwoKgdbzuAnIhRUN488HlBs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از انهدام آشیانه جنگنده‌های آمریکا در اردن
🔹
این آشیانه‌ها محل انجام بازرسی‌های پیش از پرواز، مسلح‌سازی، سوخت‌گیری، آماده‌سازی فنی و رفع عیوب جزئی جنگنده‌ها هستند و نقش مستقیمی در حفظ نرخ سورتی‌های پروازی دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/672879" target="_blank">📅 11:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
حمله موشکی به کویت و اربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/672878" target="_blank">📅 11:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO3cOh9MtMgUH1CymUI6dkEXY5diuSDvYjnIRg6gSBiHPWDDSOEuaFL4o6V2TzGaybfEqv2lAYcm-jzMOLmfkp2sTjJDmYyikdc_Bu_yklzRC5sIbtwia3irkdhPTePwIIPrrFjOZeWf35EzR7H7dU3D2nldM5GR9zsrmeVqEyKzhzreetbexioyXiRnx83Lg5joItoOq7RTeCF32PQ-LhiSFkbjfIcv7ewu2I0YmZjRcq4QIqRQR6XMFot32NUt7lwMLvg2eskXqcGVh9-vGtF77n2lr7xalAqo_8ZDVsyG1mZIqC684qQTEpYyc_ziirfxUPwGIO4HlCZU8nhf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر مهم برای خریداران بازار لوازم خانگی و فرش
🔹
در شرایط نوسان قیمت‌ها، شهر فرش و شهر لوازم خانگی قیمت محصولات خود را ثابت نگه داشته‌اند و با اقساط ساده و آسان، خرید را برای خانواده‌ها راحت‌تر کرده‌اند.
🔹
همزمان با جشنواره بزرگ ارزانی، خریداران می‌توانند از تخفیف‌های ویژه، هدایای متنوع، جوایز ارزشمند و هدیه در لحظه خرید بهره‌مند شوند و بدون نگرانی از نوسانات بازار، با قیمت‌های ثابت خریدی مطمئن داشته باشند.
🔹
آدرس شعبه مرکزی: تهران، بعد از میدان آزادی، روبروی تهرانسر شعبه مرکزی شهرفرش
سایر شعب در مشهد، ساری، رشت، اصفهان، شیراز و یزد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672877" target="_blank">📅 11:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d0db51ee.mp4?token=C2_12q2z01YVfcfUccnfoFzhwLoIGcpRRGkKSEA5WggOvIsvEjGyzx_ORy3IvdvJAit86VIxc5aS-XRxr6pmGB1NFaqpAee4TvFrc9HNBabfD6i7AKbmulSUmUOT-D-o-dLqwh-CdC7NJeFRBbQnYS6taRbI_v8BQS9EjRnosc79xv6_abwagAAms7dBS7lF2rQVBCSjjwm5YQF7Sk8cuNLpMzRov3Qd0I_yC4zK4XrWvgtETOGaiyV9fE97S9z_phI83qImFENyUO-iwZzh8MMDt3ezfetEIiUY_oUPRy189iDEm64HgY25aTX5RjJ3I5afLABVnJ-wxHk88h_IYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d0db51ee.mp4?token=C2_12q2z01YVfcfUccnfoFzhwLoIGcpRRGkKSEA5WggOvIsvEjGyzx_ORy3IvdvJAit86VIxc5aS-XRxr6pmGB1NFaqpAee4TvFrc9HNBabfD6i7AKbmulSUmUOT-D-o-dLqwh-CdC7NJeFRBbQnYS6taRbI_v8BQS9EjRnosc79xv6_abwagAAms7dBS7lF2rQVBCSjjwm5YQF7Sk8cuNLpMzRov3Qd0I_yC4zK4XrWvgtETOGaiyV9fE97S9z_phI83qImFENyUO-iwZzh8MMDt3ezfetEIiUY_oUPRy189iDEm64HgY25aTX5RjJ3I5afLABVnJ-wxHk88h_IYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعوت حدادیان از سربازان آمریکایی: پاتو بگذار تو کشور ما ببین چه بلایی سرت میاد
🔹
اون دست‌هایی که به تابوت رهبر شهید نرسیده می‌خواد ‌بخوره تو دهن سربازان آمریکایی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/672876" target="_blank">📅 11:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌹
دسترسی آسان به فایل‌های تصویری برنامه "زندگی پس از زندگی"
داستان افرادی که از مرگ برگشتند
#فصل_چهارم
🔹
اول
🔹
دوم
🔹
سوم
🔹
چهارم
🔹
پنجم
🔹
ششم
🔹
هفتم
🔹
هشتم
🔹
نهم
🔹
دهم
🔹
یازدهم
🔹
دوازدهم
🔹
سیزدهم
🔹
چهاردهم
🔹
پانزدهم
🔹
شانزدهم
🔹
هفدهم
🔹
هجدهم
🔹
نوزدهم
🔹
بیستم
🔹
بیست‌و‌یکم
🔹
بیست‌و‌دوم
🔹
بیست‌و‌سوم
🔹
بیست‌وچهارم
🔹
بیست‌و‌پنجم
🔹
بیست‌وششم
🔹
بیست‌وهفتم
🔹
بیست‌وهشتم
🔹
بیست‌ونهم
🔹
سی‌ام
🔹
سی‌ویکم
🔹
سی‌ودوم
#زندگی_پس_از_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/672875" target="_blank">📅 11:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
انهدام یک پهپاد MQ9 در اهواز
🔹
دقایقی قبل، یک پهپاد MQ9 با آتش سامانهٔ نوین پدافند پیشرفتهٔ نیروی هوافضای سپاه و تحت کنترل شبکهٔ یکپارچهٔ پدافند هوایی کشور، در آسمان اهواز ساقط شد.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/672874" target="_blank">📅 11:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKE941khMiPYbMzBf2N2KMKdluFE6FQS4MNIFPVcvxB1QLygKHdsBKjP2KKZzdWhKmyStrQhLBjZUfXyqwR3Py1eBxkAOiFgu6dMVoFhYPG3Ej9yD-ZL4fL_wkIPjfd4aCnNXwxljnmGjWEjyMihorXhoMMEmg6IxfOKAYf4DmnQCGPtg2AFSzezbJwTs9Wkakz8jOPKm_S1FGFglStpD44PSi5gdPjSlTtC536CynS5s43kgfh6AjQPk9a9G39F1iklsp_LaF-6LcpxrBsT_QTmndnGjRP5uSLEOrkV3XrDHo_7WjaKe-EODLufekE0aB4xGSAcTF7yKr2410f8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر نفت آمریکا به کمترین سطح در بیش از ۴۰ سال اخیر رسید
آژانس بین‌المللی انرژی (IEA):
🔹
ذخایر نفت خام آمریکا با کاهش به ۷۲۶ میلیون بشکه، به پایین‌ترین سطح در بیش از چهار دهه گذشته رسیده است.
🔹
برداشت گسترده از ذخایر راهبردی در جریان جنگ با ایران و کاهش ذخایر تجاری، نگرانی‌ها درباره امنیت انرژی آمریکا را افزایش داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/672873" target="_blank">📅 11:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی شورای‌ نگهبان:‌ مجلس از هفته آینده به کار خود ادامه خواهد داد.
🔹
مهاجرانی: دولت بازسازی مناطق آسیب‌دیده را در دستور کار قرار داده است.
🔹
کارت ورود به جلسه آزمون دستیاری بر روی سایت سنجش آموزش پزشکی منتشر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672872" target="_blank">📅 10:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pblsvR8OtxrW-88kDFWpMKVUkr8wjDt_9qjWC6NHYfL4J1NJZQ_w0WXTT0kBu-ds1LfYCkC9qnXRmVJOT8WyAdpfVOA9FNtjj7aq9rVGvbaG6QJj2pehzzDAHiubUmRvSTyDvZkl6ZWEl7XRwEMo4u-GkX58-yIPv2AxIYhOtDOL78syFatHkj17aImS7qadZBHKl0jTFZx-MB-gEkTKJ9xs8ddtg8XmEavdtOTjnRUPW1g6CTjbCcn0iNO9I1rBm6GCR_cpKg_3Mjs2fTwnX4WULESvR7FJFCKdZ0nO7TGDk4cKZgzpe_V1KCXNILNcc2svhCmXkT1cE0eQAD-uYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید گاز ایران؛ ۲ برابر سریع‌تر از جهان
🔸
ایران در سال ۲۰۲۵ با تولید ۲۶۴.۸ میلیارد مترمکعب گاز و سهم ۶.۳ درصدی از تولید جهان، سومین تولیدکننده بزرگ گاز طبیعی جهان شد.
🔸
میانگین رشد سالانه تولید گاز ایران در بازه ۲۰۱۵ تا ۲۰۲۵، با نرخ ۳.۷ درصد،
بیش از دو برابر میانگین جهانی
(۱.۸ درصد) بوده است.
@amarfact</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/672871" target="_blank">📅 10:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672870">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7297470d33.mp4?token=qW1kMzkdebXZIHdSrhp4HFsNdZJx3-CrF5FUtXACVHDZhOdEBDOdHmAyCT5CXgUzyxvPG76Zk3md51dZ9zzKT7tQDvJAznX3ZeYQhkUl_Vue_OVAiQExkPHfr6_pRe5eIOszXS7QC5koB-p4UZMM5iIw6LuFpepRkhxhfqCW0Z_EjZhz1HVJb9Qc88rnypW83FmX2WjRpsQ0DpGo1osWGZ-S37Y-ciTb0nxVGcdw3qouZlzesYC0DUfvCBMfic_1N-LVJZKkg73Yg-OxdUMlwSI4uHrJI7xhAnXnfAesUJCnXYA48cqFJ5w63QohsAsoEx2a5gI7wOBGerdLC9TFIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7297470d33.mp4?token=qW1kMzkdebXZIHdSrhp4HFsNdZJx3-CrF5FUtXACVHDZhOdEBDOdHmAyCT5CXgUzyxvPG76Zk3md51dZ9zzKT7tQDvJAznX3ZeYQhkUl_Vue_OVAiQExkPHfr6_pRe5eIOszXS7QC5koB-p4UZMM5iIw6LuFpepRkhxhfqCW0Z_EjZhz1HVJb9Qc88rnypW83FmX2WjRpsQ0DpGo1osWGZ-S37Y-ciTb0nxVGcdw3qouZlzesYC0DUfvCBMfic_1N-LVJZKkg73Yg-OxdUMlwSI4uHrJI7xhAnXnfAesUJCnXYA48cqFJ5w63QohsAsoEx2a5gI7wOBGerdLC9TFIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشر شده توسط خبرگزاری  «اسپوتنیک» از حملات موشکی روسیه به کی‌یف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/672870" target="_blank">📅 10:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672869">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5597b0e4e.mp4?token=DHzXb3k28kpMFHtzVwpE4VGyEBJwIdr7G1QA7F9OKnpj3Oa43BCsFsv1aRhPmusqQZpvXHCNzzEaIcGaxQeLiDni6_tGnaNaE0SGoV4aZAhkopvuTmuaAMkSfgWuuwze0EKAj99V-vUAWMMKXhk2Nzj79Lm0i2a-k4W8kRuovnJGnt0nB2GCalN1RnUgl0QMD5UlYMYv2fIz7ysTUxT-yv-f3fTGHYLUSqsrlRXZYT2NIInCa0XuGtYLFMTod7G60yMAvM39CpgaeBqIm-tWlohKLbZTfdFareu08wXwTMVMlPWWFaXtG0zBLOZsJGX-NLtN5pheAy6c94H5pZfevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5597b0e4e.mp4?token=DHzXb3k28kpMFHtzVwpE4VGyEBJwIdr7G1QA7F9OKnpj3Oa43BCsFsv1aRhPmusqQZpvXHCNzzEaIcGaxQeLiDni6_tGnaNaE0SGoV4aZAhkopvuTmuaAMkSfgWuuwze0EKAj99V-vUAWMMKXhk2Nzj79Lm0i2a-k4W8kRuovnJGnt0nB2GCalN1RnUgl0QMD5UlYMYv2fIz7ysTUxT-yv-f3fTGHYLUSqsrlRXZYT2NIInCa0XuGtYLFMTod7G60yMAvM39CpgaeBqIm-tWlohKLbZTfdFareu08wXwTMVMlPWWFaXtG0zBLOZsJGX-NLtN5pheAy6c94H5pZfevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ ایده جذاب؛ برای داشتن آشپزخانه‌ای بی
‌
نقص
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/672869" target="_blank">📅 10:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
فرمانداری شهرستان چابهار: صدای انفجار شنیده‌ شده در روز جاری (۲۸ تیر) در حوالی شهر چابهار، ناشی از عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده است
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/672868" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e43d0a32.mp4?token=DNlzfdjGJf4C-0EM5xYDNdOJlis7KZWWadBebveK2z4aHb7J936HzTrMFGXl1QjNYnKTDDiURpB_o0O_bjopIm0aiXOjAHaMfiS9eC30rC3CLzPq8Y1cMQ-xadHyTFYaBeo2U5PNYWrx2Q9M5QEsz5QzTqmqFOpJqUghNKgWIuwRCi7JOECHkSjFhPo24-WKUegU7iGp17z5AWuHlQmMXjwjq16auSn1ZgFaGf0Z1JGsTf34csmqsqJdeEaDqsGFbI_OH5jjwsII88qRhhvvSi1MitI4w8gBZtCQ5oIIRDvN_ruigk3jWLbBMA9GpeDefCmXeVeN2lZ6CQ9uDqS2wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e43d0a32.mp4?token=DNlzfdjGJf4C-0EM5xYDNdOJlis7KZWWadBebveK2z4aHb7J936HzTrMFGXl1QjNYnKTDDiURpB_o0O_bjopIm0aiXOjAHaMfiS9eC30rC3CLzPq8Y1cMQ-xadHyTFYaBeo2U5PNYWrx2Q9M5QEsz5QzTqmqFOpJqUghNKgWIuwRCi7JOECHkSjFhPo24-WKUegU7iGp17z5AWuHlQmMXjwjq16auSn1ZgFaGf0Z1JGsTf34csmqsqJdeEaDqsGFbI_OH5jjwsII88qRhhvvSi1MitI4w8gBZtCQ5oIIRDvN_ruigk3jWLbBMA9GpeDefCmXeVeN2lZ6CQ9uDqS2wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/672867" target="_blank">📅 10:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
انهدام یک پهپاد MQ9 در اهواز
🔹
دقایقی قبل، یک پهپاد MQ9 با آتش سامانهٔ نوین پدافند پیشرفتهٔ نیروی هوافضای سپاه و تحت کنترل شبکهٔ یکپارچهٔ پدافند هوایی کشور، در آسمان اهواز ساقط شد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/672866" target="_blank">📅 10:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8401e7c6a4.mp4?token=cvtRz6_1LJowkjm2ggO494YdU3yfgMWKm07IwWzoqFTQGHgIBJ5zGjoiWhKOMCCn3XKcp_m7cPdsff1ifXECngGvKuSCBaPMgZuQwiU19mt5t49Hv0gC7dVRpf64mVNUg39icfw--ezDmdFe-ZvG1V8-YUwVHCRDDw_GSNv4mF-yQwZUXt5PZz-CbAGXxssQdytgRjfIBLWFDCFl--8F8Vsc0OAflq5-1010Brk4QOzSq5o7eWlNUNEBUk3gp3IKS3S9eUEKnU3EPVZtBxhvQe1tTWvpM4zsh45Ta2EJVZGaCGEvdvX0TiFuGTo5fGMoZe5--JYzPvUXyNsPvq5pNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8401e7c6a4.mp4?token=cvtRz6_1LJowkjm2ggO494YdU3yfgMWKm07IwWzoqFTQGHgIBJ5zGjoiWhKOMCCn3XKcp_m7cPdsff1ifXECngGvKuSCBaPMgZuQwiU19mt5t49Hv0gC7dVRpf64mVNUg39icfw--ezDmdFe-ZvG1V8-YUwVHCRDDw_GSNv4mF-yQwZUXt5PZz-CbAGXxssQdytgRjfIBLWFDCFl--8F8Vsc0OAflq5-1010Brk4QOzSq5o7eWlNUNEBUk3gp3IKS3S9eUEKnU3EPVZtBxhvQe1tTWvpM4zsh45Ta2EJVZGaCGEvdvX0TiFuGTo5fGMoZe5--JYzPvUXyNsPvq5pNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی ۲۰۲۶
🔹
برنامه بازی‌ روز آخر مرحله حذفی #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/672865" target="_blank">📅 10:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
این‌بار پاستا رو به سبک انیمیشن باد برمی‌خیزد درست کن
🍝
مواد لازم:
🔹
اسپاگتی ۲۰۰گرم
🔹
گوجه‌فرنگی ۴عدد
🔹
سیر ۲حبه
🔹
روغن زیتون ۲قاشق غذاخوری
🔹
ریحان تازه
🔹
نمک و فلفل به مقدار لازم
🔹
پنیر پارمزان اختیاری #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/672864" target="_blank">📅 10:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/672863" target="_blank">📅 10:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672862" target="_blank">📅 10:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdd44b039.mp4?token=CLAxzj_OBOqlbKwXjCJZMQDYdCMJS_iQ778WY63Pt1yjS0Yevl5PHcGz2hc1DCkAhBKuWGRrOaPq-7mwsCIeHxClNnJHVDKwfuXxR4a4cDaHWpf1qCdMOufgCo45dIH8fcEudKR2iy3Bamngu63bFvC6XgePQ-_FXSBh8PyKRAKuj6ie0rDFQes2BXc1uhca9Kicvw69Fxn-dHHWhXO__s0uRvF9C9P5lpH2_neVuv2R_cUONFhxxav-G4xWsqrZ0eH5xQJ81pxfyxtQgm6CZNK2EnAfbT7RsWn1QLAa6tMGrraOEShWsadsbUDUoLmGdtjgkKNTINSz7uHakBanSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdd44b039.mp4?token=CLAxzj_OBOqlbKwXjCJZMQDYdCMJS_iQ778WY63Pt1yjS0Yevl5PHcGz2hc1DCkAhBKuWGRrOaPq-7mwsCIeHxClNnJHVDKwfuXxR4a4cDaHWpf1qCdMOufgCo45dIH8fcEudKR2iy3Bamngu63bFvC6XgePQ-_FXSBh8PyKRAKuj6ie0rDFQes2BXc1uhca9Kicvw69Fxn-dHHWhXO__s0uRvF9C9P5lpH2_neVuv2R_cUONFhxxav-G4xWsqrZ0eH5xQJ81pxfyxtQgm6CZNK2EnAfbT7RsWn1QLAa6tMGrraOEShWsadsbUDUoLmGdtjgkKNTINSz7uHakBanSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ضبط‌شده توسط یک سرباز آمریکایی در پایگاه هوایی موفق السلطی در اردن
🔹
حداقل دو سرباز در این حمله‌ی ایران کشته شده‌اند، بسیاری زخمی شده‌اند که حال تعدادی از آنها وخیم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/672861" target="_blank">📅 10:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGs4s_lsWidc4D8MXKGL3BIJfTgvTxhp_VN8r9bE6gDqSuWKj9KbplMWcqaFhNZFCHouB8zbASDoR1LjyF5SVTSlMAggJENpPciVB7FXN3rsj_d_yDSE3f_290QuOh3JAA-xxhr0ihW690dh1oFOLVPD9FOkzmZjU09N5BiE9KP6L7a_G1ud1GtZpEWBzpKiEPAiR_MPj2_UNXkIB6clHcg42zLrqeINnEvTx7zhxdRT0G3JzDbtvaqbvC_QlrLOUKtejrg5vRDrqXHu1Ab-iJXkf8ytsNxz5cFLiatQi83EsuuWB7PjLNbC6jYl-dkOFwL4YeceC4bnbrkgp3s9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی خطاب به سربازان آمریکایی: فرار کنید؛ حتی یک ثانیه را هم از دست ندهید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/672860" target="_blank">📅 10:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672857">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsmYlMllRudnX9KXTaP1JCHRh2jyUUyvbf2lbehMz3A5Fy0qXhHaxv3wUEp1-PmjvD_E3BlmCvi_GN85RYxrdqB7_HJJJTSdLcQLIBjlRdnk-hjFGbLBlxjgo-GwxghQVMfXiFrl34tPer27x_NufoThhP0K1unBFRJ5qt5MjlfuDEkeNZl_zyXK78qHNCGDaWz00BsT4SBnHLII1kI19rAk8yolovx7TG_GtHQeujn1LMbVkU2d_GapNrvBVNowjvlu7QZWgxKtNGlvahbwYrk16ZLbdivEVp6Pa_wKQ_aRhu38DkSX3uOcbWLK9E_fEjMtYRqGIVASgOpB9xdpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران تشنه همدلی ماست
🔹
بیایید با چند تغییر ساده در سبک زندگی، از ارزشمندترین سرمایه کشور محافظت کنیم.
🔹
هر قطره، امید فرداست. #همه_باهم_برای_ایران #صرفه_جویی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/672857" target="_blank">📅 09:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672853">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ایران به عربستان سعودی و عمان گفته که قصد دارد «به شدت» امارات متحده عربی را هدف قرار دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/672853" target="_blank">📅 09:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672848">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سامسونگ: هاله قرمز نمایشگر گلکسی S26 اولترا نرم‌افزاری است
🔹
سامسونگ با انتشار بیانیه‌ای رسمی، شایعات پیرامون نقص سخت‌افزاری نمایشگر گلکسی S26 اولترا را تکذیب کرد.
🔹
طبق اعلام این شرکت، متمایل شدن رنگ صفحه‌نمایش به قرمز، ناشی از اختلال در سیستم هوشمند تعادل رنگ‌ها هنگام قرارگیری در معرض نور شدید است و این مشکل با یک به‌روزرسانی نرم‌افزاری برطرف خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/672848" target="_blank">📅 09:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672847">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f2c9672b.mp4?token=OoTGSeD0cuAU_BETFbOBZosWwYBYxk-Vt70EK7GvwmHhq800skCzSJVjilbQZnUr0xCSe8ueUJMrZweiQcKwE6jfHSIECuDeyvOkVjfMCHzsXquLOjX7xCEpJxc-I81rUTkNzL9oYxh6uQwHAfkrn_2Bf2R5lBYKIw6xj3C5fmfORhCe9aqQqkglxHoUtsN5zPnBcaWAxI47MOqwmwYEOUUQjQusZgSIErSHf5ODtSftIfPYBBJhE-OJ7_feTfO9_UYmxyXkGBIOo6TCKeDGZJ1lCdFZNzhQORMr1rLuGryzAUc48JNjTTNg1ZqrPUVtZ0o1S2maf_eaFl9PyU596g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f2c9672b.mp4?token=OoTGSeD0cuAU_BETFbOBZosWwYBYxk-Vt70EK7GvwmHhq800skCzSJVjilbQZnUr0xCSe8ueUJMrZweiQcKwE6jfHSIECuDeyvOkVjfMCHzsXquLOjX7xCEpJxc-I81rUTkNzL9oYxh6uQwHAfkrn_2Bf2R5lBYKIw6xj3C5fmfORhCe9aqQqkglxHoUtsN5zPnBcaWAxI47MOqwmwYEOUUQjQusZgSIErSHf5ODtSftIfPYBBJhE-OJ7_feTfO9_UYmxyXkGBIOo6TCKeDGZJ1lCdFZNzhQORMr1rLuGryzAUc48JNjTTNg1ZqrPUVtZ0o1S2maf_eaFl9PyU596g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله هفدهم عملیات صاعقه ارتش؛ ادامه حملات پهپادهای ارتش به پایگاه های آمریکا در کویت
روابط عمومی ارتش:
🔹
در پی نقض معاهدات بین‌المللی و  جنایت‌های دشمن مستکبر در مناطق غیرنظامی، ارتش جمهوری اسلامی ایران در دور جدید حملات پهپادی و مرحله هفدهم عملیات صاعقه، از بامداد امروز، انبار مهمات ارتش تروریستی آمریکا در اردوگاه العدیری و سوله‌های تجهیزات و نفرات این ارتش کودک‌کش در پایگاه ‌علی‌السالم کویت را مجددا هدف حملات پهپادی قرار داد.
🔹
ارتش جمهوری اسلامی ایران تاکید کرد؛ جنگ ما دفاع  ازهویت اصیل و  تاریخ چند هزارساله ایران و مردمانی است که در پرتو تعالیم اسلامی نه ظلم می‌کنند و نه ظلم می‌پذیرند، براین اساس، رزمندگان ارتش، با اعتقاد عمیق به این آموزه الهی برای دفاع از مردم شریف در مصاف با دشمنان ایران و بشریت محکم و استوار ایستاده اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/672847" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672846">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07364b31d.mp4?token=GaFZZoGGWNI2ulq1PCvJkjW82gAeD8nevpXsE-Rbyt34cxewsQBouX51dSWbyQnQJbuO2piqOSexqilYG5s8LsvMeCMZOPUDgDq08ZMJWiXbIq095oiv1vnQJM7O8zaBDxHgUrSjmzu3luwP-L5oRGq_g5R1rD9BxHYDJCCD8yudbrDuuEEJHj5KyRaStigof1f8tiVPypoNecoEZARLE4clw3DAZv-MTDM4DqJScXpilCiicPb7JlySOGGEl8x81Iq4Or11EcOlRoiIcChru5_6KMfjKHGdVBACcps7T1J77HeNOjkKcQEysh5OXxvKHc-K7Y_XcihrluWaSNfM1RXTbSLcvQuUNX5ZiyWnv_pzqi57oYH_TER_1iRfRK6qUK43yD_P0IdIVdJlxDwEapFiOE1uHeDep4oPcSudmj5M0aY-7ALiSLN9vItSF0BWZiX_VkP3IShc5Hb2FXbSi4CgWblv5IUJ5Do_SfOpNWr8lauPvhBipghlMZaEH3DGYNXEoTuMzP7T-L8FSlki3DxtGkSFOsy3VgDENOsBUIh4iUenE-oDCrkro5MG4Rv6-k8jMRU51s_lEfSjedLC3D3ProYxQA_tpiGq6jcXviOhrCGeAJAMLyQNPsf1uIyUNhUyRuZGwEyHcAWowC0Pfa1aw0DqwyYWgxiyqWA-gEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07364b31d.mp4?token=GaFZZoGGWNI2ulq1PCvJkjW82gAeD8nevpXsE-Rbyt34cxewsQBouX51dSWbyQnQJbuO2piqOSexqilYG5s8LsvMeCMZOPUDgDq08ZMJWiXbIq095oiv1vnQJM7O8zaBDxHgUrSjmzu3luwP-L5oRGq_g5R1rD9BxHYDJCCD8yudbrDuuEEJHj5KyRaStigof1f8tiVPypoNecoEZARLE4clw3DAZv-MTDM4DqJScXpilCiicPb7JlySOGGEl8x81Iq4Or11EcOlRoiIcChru5_6KMfjKHGdVBACcps7T1J77HeNOjkKcQEysh5OXxvKHc-K7Y_XcihrluWaSNfM1RXTbSLcvQuUNX5ZiyWnv_pzqi57oYH_TER_1iRfRK6qUK43yD_P0IdIVdJlxDwEapFiOE1uHeDep4oPcSudmj5M0aY-7ALiSLN9vItSF0BWZiX_VkP3IShc5Hb2FXbSi4CgWblv5IUJ5Do_SfOpNWr8lauPvhBipghlMZaEH3DGYNXEoTuMzP7T-L8FSlki3DxtGkSFOsy3VgDENOsBUIh4iUenE-oDCrkro5MG4Rv6-k8jMRU51s_lEfSjedLC3D3ProYxQA_tpiGq6jcXviOhrCGeAJAMLyQNPsf1uIyUNhUyRuZGwEyHcAWowC0Pfa1aw0DqwyYWgxiyqWA-gEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف فرمانده ارشد پیشین نیروی دریایی آمریکا به اهداف احمقانه ترامپ برای حمله زمینی به ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/672846" target="_blank">📅 08:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672840">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnGMjMmCo_b1hFK9nNPmuftI0YBIWQuDKBTY4zkbnafFuHwwv3Tqah5bnUbQk87UW9TjMexJTFBF8PtR4vPKYSGa0O4l0GjjeyQ4P0vDahiKiOQNmA58DezixOIG6J7B7VgYR1xjy_QqEDbFvRSBBrMbRkv9yAgKhxvgZr5UJqLJ8Dc_8gA0ShQDIzpgWenj4IeV3GQOOd4YZ1gwzfXce1eKBhT62gDORX60VE_QYQnWYBKJXN0-WqzMum-zopuEOGCypBkdfIyxL_tzKa-_Hfwo91j8hieRuNHWNXCRxRIb49bv629hqDkOsXU5ebBTsa_XYAh8gBfw5YUBdy8zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام جهانی ۲۰۲۶
🔹
برنامه بازی‌ روز آخر مرحله حذفی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/672840" target="_blank">📅 08:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f06efb4c.mp4?token=W3IsnfGxPbjk9Q8atuHUTLAUINakvSVZcXQtWqCw5sf-WD9sUeYjjFV6WZJZbCPN4At5XA6MrsIncDJCh_FiyCZpNjR9EFRopL8iqMFsY8u7JTtFORmy2Y7H3Wwr2DG1wYThJnFL8gnKt2RPluZcW6MWlaP4tPQ7vLvQqzMiJ_pRcJuWHRH-sqUR7MBviaCmdxpGOkZ0_8NNgwjxWDzWxWjZC_p-jVWmnBzpCUaBvOFhXAYiAVgAT16yUyhy6rIVrGjEIhTglvXPdiS40mI1ONJI6upWuzOwPch-8NElwZ0HybinepSQHNb_nj4IrIIzHq0ibYy1YbPuMKreL7QDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f06efb4c.mp4?token=W3IsnfGxPbjk9Q8atuHUTLAUINakvSVZcXQtWqCw5sf-WD9sUeYjjFV6WZJZbCPN4At5XA6MrsIncDJCh_FiyCZpNjR9EFRopL8iqMFsY8u7JTtFORmy2Y7H3Wwr2DG1wYThJnFL8gnKt2RPluZcW6MWlaP4tPQ7vLvQqzMiJ_pRcJuWHRH-sqUR7MBviaCmdxpGOkZ0_8NNgwjxWDzWxWjZC_p-jVWmnBzpCUaBvOFhXAYiAVgAT16yUyhy6rIVrGjEIhTglvXPdiS40mI1ONJI6upWuzOwPch-8NElwZ0HybinepSQHNb_nj4IrIIzHq0ibYy1YbPuMKreL7QDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با انجام این حرکات هم عضلات پات قوی میشه و هم درد زانوت کم میشه! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/672839" target="_blank">📅 08:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672834">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7N989uJ7kUiP0SIgd-sDNviAsuxJj9RSAI_8ksUF7fiWgqQjATU5Tw6BeUQpVDltOit7u-dxcEqOoutxr4G4lvO5BEEl9FI16ppgFq8WJpVOBQqseAlPB7m7uLJ2wlHitSEWrHPbfQBX9P0HiqlZrOj3MCSTQSJUSyckhaii51CqDoy8Bbvu3y-WyCT2svJ5pEI51mGQ3nXVVPWTI9YetpMos40YIWIie3cvJAmr7UraSGXHbrG5YV-Cdwf7mbRP-PUVcD7CA3ai0ZoqtAoJ890ptvj_wwCWBecVm_QvXAdeFb5EXLej7XNSEEJl5fcGDr3hUFQihlgCHnEScaB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwlRuabs8EUpnPHZ5JGP6n-BU3YLV5NpCkB06E-Wge7-3ar9rpuYHV5-beCW7NWPVAg3dFm51QmwQgs631svLN7pob5YzYUKdQdqwoYiFB9de3ECBLkjRl_OAFYwz9gd3QyjKYSSP3Dh2VphqFtnHDBYyIZPo57nQv8Gx0Q9A7ql4LybT5Q0m2aDH3mi6ALecJyFa9lOh_auEk0IXmE4GfXp-WL1k_dncDddKcm4LWaF8KZDez1OOnf2_m4TOPLKDSW1nqP1osciBDMYCIO6HoPjw4jFicL4H-TJIamtAiZ0KjphHupyZ9yDeAxQ-ZxEwC_OacCnyKer8UcDi9UyRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1694542022.mp4?token=jtJLQ4VM8igAxyFryKYlL52UlLqhS2fcdrP03CbrJOCzEo7J1-1HjsW2jwd3INJu-YaaGdJ1fz1xnmnMnRZZHnfHDRxLcRfQfDCnIF9kdxkDSrES1A1JXruE62XV0XtKXM7lEb-E5V-SzEy4liuGG9hUMmEktd7fIB2xhdYsRk4Hqk34TnJ8AA962KR8xifY-rAezy-rCKiXImwcqbmEcWKo0Z3X8me0L3WMsGljBh07ZAIzrV-ZNdhH-oYcnlGK6bV9ODRAlV5oA8HC6jPKGBDEIn_6EnLPdsHabhQDeALJUuVHlmKzmGq6H9dnSEUgtZPRJht1JzzYHZwYc5C1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1694542022.mp4?token=jtJLQ4VM8igAxyFryKYlL52UlLqhS2fcdrP03CbrJOCzEo7J1-1HjsW2jwd3INJu-YaaGdJ1fz1xnmnMnRZZHnfHDRxLcRfQfDCnIF9kdxkDSrES1A1JXruE62XV0XtKXM7lEb-E5V-SzEy4liuGG9hUMmEktd7fIB2xhdYsRk4Hqk34TnJ8AA962KR8xifY-rAezy-rCKiXImwcqbmEcWKo0Z3X8me0L3WMsGljBh07ZAIzrV-ZNdhH-oYcnlGK6bV9ODRAlV5oA8HC6jPKGBDEIn_6EnLPdsHabhQDeALJUuVHlmKzmGq6H9dnSEUgtZPRJht1JzzYHZwYc5C1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک دوباره تبدیل به ونیز شد
🔹
وضعیت نیویورک پس‌از بارش‌های سنگین در روزهای گذشته مورد توجه کاربران فضای مجازی قرار گرفته‌است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/672834" target="_blank">📅 07:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T24w71XDKlFPfrfCtUGbSVDLLaz6ocqwW3Ki_0oz0eQj-J8XnONvvk9sjMabfqzGuZ4mcbtXoyUgslTDfBrj6tUM5gUlb-6aG2UkVDsSLyk7Spr8BFRyLx_GC54M2g0xfubcIhBDSsKe3qfzPur045Me-TH-nTduHBN9VUbt0FxC8H1GP_ZH5oZrYg58Pe7FdLja8ehmlb2yrgx634Fo2lL-69AIJTVIq0_x3navflJIAUbjciULrH1RiMdK5iSZIgwOZSBi9WTgc8OqjazSu8W4-IQNaga_U-Dt7QZveTddeW9tldiUobLKqCGv6SHhx8MMQnGWAnj_BkVc87zamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۸ تیر ماه
۴ صفر ۱۴۴۸
۱۹ جولای ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/672833" target="_blank">📅 07:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672832">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
زمین لرزه ۵ ریشتری سالند خوزستان را لرزاند
مدیرعامل هلال‌احمر خوزستان:
🔹
ساعت ۰۵:۵۵ امروز یکشنبه ٢۸تیرماه، زلزله‌ای به بزرگی ۵ ریشتر در عمق ۱۲ کیلومتری، سالند از خوزستان را لرزاند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/672832" target="_blank">📅 07:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672828">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db885829ed.mp4?token=lF_VJbH_TfiQZNQgKMYjTPnaFhgCW3yfg6CzP4XvOy9dsyi7gh43DUO3FxzsyBTSSz6IdY_5J2xwZD8QWrV7LmmLA5Pm5ONLh6R4M4pOXXZftesLl6bmzAvaKAUtznxS07X7x5Qp2TjxgTjkWxV8iMxBJh4JY30JX4BQwCgqRHqKraoOtkOcIeNoX8-tsk2chMx2BgecDAAAJbUJMTctxpzQPGNhC1nmfErDHH7vF3__8XTU-LjgMiLC7Scrqez0CRBBeVhsbAfT3gU0tu_vOwHif4YFHHOeZMgTGCWV4ENOX5FxQyj_97IJVlo9L_ubD328r_Op7hrdSLVjMs537g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db885829ed.mp4?token=lF_VJbH_TfiQZNQgKMYjTPnaFhgCW3yfg6CzP4XvOy9dsyi7gh43DUO3FxzsyBTSSz6IdY_5J2xwZD8QWrV7LmmLA5Pm5ONLh6R4M4pOXXZftesLl6bmzAvaKAUtznxS07X7x5Qp2TjxgTjkWxV8iMxBJh4JY30JX4BQwCgqRHqKraoOtkOcIeNoX8-tsk2chMx2BgecDAAAJbUJMTctxpzQPGNhC1nmfErDHH7vF3__8XTU-LjgMiLC7Scrqez0CRBBeVhsbAfT3gU0tu_vOwHif4YFHHOeZMgTGCWV4ENOX5FxQyj_97IJVlo9L_ubD328r_Op7hrdSLVjMs537g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش: دو پایگاه مهم آمریکا در کویت، آماج حملات پهپاد‌های انهدامی قرار گرفت
🔹
در پاسخ به تجاوزات مکرر دشمن، شهادت هم‌وطنان عزیز و حمله به پل‌ها، زیرساخت‌ها و مناطق غیر نظامی، ساعاتی قبل و در مرحلۀ شانزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، انبار مهمات ارتش تروریستی آمریکا در اردوگاه العدیری و رادار پاتریوت و رادار هوایی این ارتش متجاوز در پایگاه علی‌السالم کویت را، آماج حملات پرحجم پهپاد‌های انهدامی خود قرار داد.
🔹
اردوگاه العدیری یکی از پایگاه‌های مهم ارتش تروریستی آمریکا در منطقه و در فاصلۀ ۱۰۴ کیلومتری مرز‌های جمهوری اسلامی ایران و ازمراکز مهم پشتیبانی و تجدید سازمان نیرو‌های آمریکایی است که اخلال در عملکرد این پایگاه تاثیر قابل توجهی بر عملیات‌های پشتیبانی ارتش در منطقه می‌گذارد.
🔹
پایگاه هوایی علی‌السالم نیز از پایگاه‌های مهم، مرکز اصلی ترابری هوایی و دروازۀ ورود نیرو‌های نظامی به منطقه غرب آسیاست که نقش محوری در راهبرد نظامی و لجستیکی ارتش متجاوز آمریکا در منطقه ایفا می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/672828" target="_blank">📅 07:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672821">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: هواپیماهای آمریکا در اردن هدف قرار گرفتند
🔹
روزنامه وال‌استریت ژورنال آمریکا گزارش داد که در حمله موشکی ایران به پایگاه موفق السلطی اردن متعلق به ارتش تروریستی آمریکا هواپیماهای با سرنشین و بدون سرنشین هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/akhbarefori/672821" target="_blank">📅 04:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672814">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccZ68D75Nf4pyHx_opDxK4_Ojcc8T4gbsHdnzLV3R6uOs_EBNuikFHT8R5TZmsb9YaXf_lHUvCgTmYpMQ2oYlLKx_tVnnX_V8QHQaecV-AkqwNRsHJIMv-2LDsq4FmpdX0rlU4IVFATv_i9f2M76ni6QdOo_4ZP-OboqfVYAr2PrL876vsf4evC491I-bIALGSVLng2Jj-P0aXHxBDcljNKQ_eMP9pjx9D5T7in2FFt9bQXHZdp7GZlsidp5_8JmxjAtTtSn8rsmdkHSm5JfR50JmXM1cmISt-RD9jM1zKbzwzwDKdLzLXrzQ19K225RwERmnlSoCBvDNJY_oad-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مدال برنز بر گردن انگلیسی‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/akhbarefori/672814" target="_blank">📅 03:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672812">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=j7BKXw-NJ0gc7F1Vj_V7vZ9R_aFkAe1jJNCR5fURm1Wx1Nk0IdNon_NdYY18nV1OMWrmuDEcHPnd7ROUC40MM8-Z5PMl1g8Fieb0-AB8rfalVzMma9GA9xWkCr8XDkv1M8Dvi2DgpIsOqioZEkzoHjv5tSBjWzz87_8YsTIcM7RG0Bc-V2xTn2xmvz4hGI1XkEzQu2hGynKJsAPAftNmolSA4TIZmJBeZ4MTOB33PwLjXsEhQ-ZPk-jimyaS6R7qNLY9cdXInGM_y1j6WTEd-nHh4vJtVkeV8_otSSj0k9l9_xKAfzsMU6m5ojLmnzTllzA1xTh6WKTPyyGt-6VM2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=j7BKXw-NJ0gc7F1Vj_V7vZ9R_aFkAe1jJNCR5fURm1Wx1Nk0IdNon_NdYY18nV1OMWrmuDEcHPnd7ROUC40MM8-Z5PMl1g8Fieb0-AB8rfalVzMma9GA9xWkCr8XDkv1M8Dvi2DgpIsOqioZEkzoHjv5tSBjWzz87_8YsTIcM7RG0Bc-V2xTn2xmvz4hGI1XkEzQu2hGynKJsAPAftNmolSA4TIZmJBeZ4MTOB33PwLjXsEhQ-ZPk-jimyaS6R7qNLY9cdXInGM_y1j6WTEd-nHh4vJtVkeV8_otSSj0k9l9_xKAfzsMU6m5ojLmnzTllzA1xTh6WKTPyyGt-6VM2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ اصابت پهپاد انتحاری به مقر گروهک‌های تجزیه‌طلب در اربیل عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/akhbarefori/672812" target="_blank">📅 02:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672810">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
انفجار و حمله جنگنده‌های آمریکایی به قم تکذیب شد
🔹
در پی انتشار اخبار مبنی بر انفجار و حمله جنگنده‌های آمریکایی به مناطقی در قم، مسئولان امنیتی ضمن تکذیب این خبر اعلام کردند تا این لحظه گزارشی از انفجار نداشته‌ایم.
🔹
در حال حاضر امنیت در استان قم برقرار بوده و تاکنون هیچ انفجاری در هیچ نقطه‌ای در استان گزارش نشده است.‌
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/akhbarefori/672810" target="_blank">📅 02:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672809">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
مقر گروهک «حزب آزادی کردستان» هدف حملات شدید قرار گرفت
🔹
گروهک «ارتش ملی کردستان» شاخه نظامی «حزب آزادی کردستان» اعلام کرد که مقرهای این گروهک تجزیه‌طلب در ابیل و سلیمانیه هدف حملات شدید از سمت ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/672809" target="_blank">📅 02:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672807">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90746d4c73.mp4?token=bDk7T2q_G80w9TGdk96ZxAQH1xY7WGVbx0ko89rigI0v-MJaj4hzi0FPM0V-MvVHe8xQuo5L6tuo75-EQuiZb_s-AA9qk6tmekg619I_2wOSCKd1XCDxOhQo4HJjcuUiGiXPay9VlK9L2kpnP8x33mLfBjtmgwN1cnQXiUhf4g13J1ogtP1d1Vyji0qr93lyRI0SzhcghDWAeR2esQiIZsY5AVC7MhVYgbdQVmcLlRYGGStn473m7NrKY9b9poA7qiTQj3WMemnxIH0bM6t_LjFEwCAXD1oj5jaH0mGKtU8FDHUwWAK7ptUh_niedJJFABBbDeHv22rH2UWZxZ1l0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90746d4c73.mp4?token=bDk7T2q_G80w9TGdk96ZxAQH1xY7WGVbx0ko89rigI0v-MJaj4hzi0FPM0V-MvVHe8xQuo5L6tuo75-EQuiZb_s-AA9qk6tmekg619I_2wOSCKd1XCDxOhQo4HJjcuUiGiXPay9VlK9L2kpnP8x33mLfBjtmgwN1cnQXiUhf4g13J1ogtP1d1Vyji0qr93lyRI0SzhcghDWAeR2esQiIZsY5AVC7MhVYgbdQVmcLlRYGGStn473m7NrKY9b9poA7qiTQj3WMemnxIH0bM6t_LjFEwCAXD1oj5jaH0mGKtU8FDHUwWAK7ptUh_niedJJFABBbDeHv22rH2UWZxZ1l0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک رده‌بندی در حد فینال با ۱۰ گل، گل ششم انگلیس به فرانسه توسط بلینگام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
6️⃣
🏆
4️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/672807" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXOwigpkfi4CwhLyRFU0X3fT3B9JZKq5Jre498z56Wd4EwFYx_yg3EXAeHy1lsjS2asyY9Z0KL4d-3XmyIVLFUiK5fEkZ0DUvxK0UGjdRi-dvhnI_i0aAyid79XEmvpZTfGt_kqYP1ZG6pUqI-ZgYT_i4b6p6c5iTY0PEoBcvN2Samr9Vq5aTsfB0GbUxy3dryLrR5HoL4T4xXI3vq_Sp6-AfdD9qjVvhInHVtoFSzNs0_UkUrCuwaJ2filTA5ATGwFZv_Q1zUxNlbLHqhfpUoWC6cK09s3MRuEVAk5CcuXb0T-6gzbueOT5SI-PSc5NZw81T1X9CqWjceWbbEEnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
انگلیس روی سکوی سوم جام جهانی ۲۰۲۶
🔹
تیم فوتبال انگلیس با پیروزی پرگل ۶ بر ۴ مقابل فرانسه، روی سکوی سوم جام جهانی ۲۰۲۶ ایستاد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/672805" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672804">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a14d10202.mp4?token=pBZfSy4UO_yA2IXivzZ0oGmk4ggRpNcP9-C5f0-S_fvz4VNrEUDOuSY4iXJGS2SXzTm7sRIrz1PkcMGCcl3ByEZF5zIt68YrbRQ4d1CjFscXrbOjuOtPK8oxbayXMOCPOZe7Zn30tk3SK2m1cPZiErMwWnQXVuInG55Je4vxeZ9VMOwbL3QVkzriWR-8KgMw2yrefFyxKAl33afE7Ow3IuaqSNjsAI3OGatdQjsOC2KZc4HTPsKh-lUmZnpoIfBD4ZXH87scOp-gevvmlwjvnS1ubgX3YyQDoXLJ3D5pk06pYKJ9tZe61BtBbFXXm0jX8WI-aHgYyV7mPXSL7CKWFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a14d10202.mp4?token=pBZfSy4UO_yA2IXivzZ0oGmk4ggRpNcP9-C5f0-S_fvz4VNrEUDOuSY4iXJGS2SXzTm7sRIrz1PkcMGCcl3ByEZF5zIt68YrbRQ4d1CjFscXrbOjuOtPK8oxbayXMOCPOZe7Zn30tk3SK2m1cPZiErMwWnQXVuInG55Je4vxeZ9VMOwbL3QVkzriWR-8KgMw2yrefFyxKAl33afE7Ow3IuaqSNjsAI3OGatdQjsOC2KZc4HTPsKh-lUmZnpoIfBD4ZXH87scOp-gevvmlwjvnS1ubgX3YyQDoXLJ3D5pk06pYKJ9tZe61BtBbFXXm0jX8WI-aHgYyV7mPXSL7CKWFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم فرانسه به انگلیس توسط دمبله
🏴󠁧󠁢󠁥󠁮󠁧󠁿
5️⃣
🏆
4️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/672804" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672802">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
منابع بحرینی از پرواز پر حجم جنگنده‌های آمریکایی از خاک این کشور برای انجام حملات در ایران خبر می‌دهند/
فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/672802" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672801">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2785127527.mp4?token=ECksUq7SEBXAqcrRvvQznPxR_ZIo6aq8w23_fK0iCJreYZaRLkKtbyyk8DDdodEyEbBPXEJRW5S-swy8UrV3nCcPsbeIHke-OrgHvS3VD9ZbaPflEsCynMeK3JtdsHHYR9vDdgT5a5Ug1mqMSPP9gWrm-Te9yureVmG_sPNs1hRxN-Owopl8Ssb-1qxHIPqS3wcmfJrSrXIRXIhYyhWZ4d5hqPscK-rMPu-qJBWMX4S85_wIeZ2lu6vJhoHvlEhkcvq58HWkHVrcCCkb3ZK535cskK-oBxchFLyxJ-POqKImaIO1bqTMtIw9P6M5JKNnA9ngS7FJPyJpDHqtUXBMmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2785127527.mp4?token=ECksUq7SEBXAqcrRvvQznPxR_ZIo6aq8w23_fK0iCJreYZaRLkKtbyyk8DDdodEyEbBPXEJRW5S-swy8UrV3nCcPsbeIHke-OrgHvS3VD9ZbaPflEsCynMeK3JtdsHHYR9vDdgT5a5Ug1mqMSPP9gWrm-Te9yureVmG_sPNs1hRxN-Owopl8Ssb-1qxHIPqS3wcmfJrSrXIRXIhYyhWZ4d5hqPscK-rMPu-qJBWMX4S85_wIeZ2lu6vJhoHvlEhkcvq58HWkHVrcCCkb3ZK535cskK-oBxchFLyxJ-POqKImaIO1bqTMtIw9P6M5JKNnA9ngS7FJPyJpDHqtUXBMmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم برای انگلیس از روی نقطه پنالتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
5️⃣
🏆
3️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/672801" target="_blank">📅 02:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zof9YiBwxSoRclEv-7eX1O2SQUGFOGTBRizXTjbaau4fuomBnxvUWfIro0FXTy2a46aJlzOkrRv11y4ghqyGkgea5DYn5ILJyH2DHhlKQkTPcRaGXRP2G26c5j8ZWJ1CE8zCUcyoclsshz2Y3rudS--bvWOZ3eYYc9eiHrbg3M5J8w6xrDb4fIUeTJsoxMGYMnPv8Rj0AoKb2BUpffBHrg-Mu8pDkN7bYfaRYVODWs7Y5S5nEf93lEZOLDYih6lxGASGVaeDiUHxkI06fXkO_vSHPb5R6nFix8VlfkUPbuYUhg8ccoOze9Xe3y4ZMVK-8FWzfReCyzM2pq63uvI1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امباپه با ۲۲ گل بهترین گلزن تاریخ جام‌جهانی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/672797" target="_blank">📅 02:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672795">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی انتقام از ایران به خاطر سربازانش در اردن شد
🔹
ارتش تروریستی آمریکا در پیامی که دقایقی قبل منتشر شد، ادعا کرد: «حملات جدید به ایران با هدف مجازات فوری سپاه پاسداران به خاطر حملاتش علیه نیروهای نظامی ایالات متحده در اردن انجام می‌شود.»/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/672795" target="_blank">📅 02:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672794">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0813f70fda.mp4?token=WmjN64--QkJ9vwdaRMcIeWRdHMvG3yBOkdo3o16qShTV9L6t9UR071gRgqcHtk0dTmZqlSkstifAWsb6jLkzviRnJePlRnW80Dn2MS1-o2ejMHJZtxUIV4VUSIHlHRZInFQJdFttx2G1k8nZt0qMYg5Veq4HtcEw2uMyBmBEKK3FkxgaQR7RzOGBhEUeG5qWtNfUCZevfaSdIE-m8PmT2oPPQwpjmJG6h3CZqZkD8SH3iWXMo9b8_NrT65U5oUnoTe1LS-7b7FwtCh41pFYDcMD0GJJs-TWWXX5ruVO78t3ib6mYrNj47R4cIuqvtUWz_rjNz_Xe12LR0xy0LAiVeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0813f70fda.mp4?token=WmjN64--QkJ9vwdaRMcIeWRdHMvG3yBOkdo3o16qShTV9L6t9UR071gRgqcHtk0dTmZqlSkstifAWsb6jLkzviRnJePlRnW80Dn2MS1-o2ejMHJZtxUIV4VUSIHlHRZInFQJdFttx2G1k8nZt0qMYg5Veq4HtcEw2uMyBmBEKK3FkxgaQR7RzOGBhEUeG5qWtNfUCZevfaSdIE-m8PmT2oPPQwpjmJG6h3CZqZkD8SH3iWXMo9b8_NrT65U5oUnoTe1LS-7b7FwtCh41pFYDcMD0GJJs-TWWXX5ruVO78t3ib6mYrNj47R4cIuqvtUWz_rjNz_Xe12LR0xy0LAiVeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه در آستانه کامبک زدن، گل سوم فرانسه به انگلیس توسط امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
3️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/akhbarefori/672794" target="_blank">📅 02:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672792">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
حملات نظامی دشمن آمریکایی به حوالی سیریک
🔹
در ساعت ۱:۳۰ نقطه ای در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.
🔹
در حملات جدید آمریکا به سیریک هیچ مصدوم یا خسارت به زیر ساخت های مسکونی و تجاری  گزارش نشده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/672792" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سنتکام: به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه اهدافی در ایران آغاز کردیم
🔹
امروز ساعت ۶ عصر به وقت شرقی آمریکا، نیروهای آمریکایی به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/672789" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672786">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=tfzwm9Fxa01blINuPwP8JmcciD-oe0v7M2lK9yvdtB_BFQTnI7UfBgVC_3wWW1rW5G9_YBLsvO2v9H51kkX7OF09Bu0JQkuTzytnZ0UrXWbn7RvGrXYZr6eOdRhcQrm0dl6yt0jJe5tIfB2ua2BONrMgrRgNJDzSzATyNALxb1TCu-4XRKvz6JqSr3g_hYwBzNb_vuFNfVeMp_KPc_7CA__vROWXVO6ZWTAraGct7IKywAy33qxAtvQuoNaSeUy4A9goOnJnWAkm2LEC-9_JtoevkKTFJJvyWoigmczOtTGvKkTaH3cCMb-YAQhSDAkn7-IOHDPGEzkLYW-YBAINXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c15e9eec1.mp4?token=tfzwm9Fxa01blINuPwP8JmcciD-oe0v7M2lK9yvdtB_BFQTnI7UfBgVC_3wWW1rW5G9_YBLsvO2v9H51kkX7OF09Bu0JQkuTzytnZ0UrXWbn7RvGrXYZr6eOdRhcQrm0dl6yt0jJe5tIfB2ua2BONrMgrRgNJDzSzATyNALxb1TCu-4XRKvz6JqSr3g_hYwBzNb_vuFNfVeMp_KPc_7CA__vROWXVO6ZWTAraGct7IKywAy33qxAtvQuoNaSeUy4A9goOnJnWAkm2LEC-9_JtoevkKTFJJvyWoigmczOtTGvKkTaH3cCMb-YAQhSDAkn7-IOHDPGEzkLYW-YBAINXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع ۵ انفجار در اربیل؛ سامانه پدافند هوایی کنسولگری آمریکا فعال شد
🔹
بر اساس این گزارش، هم‌زمان با وقوع این انفجارها، پهپادهایی نیز بر فراز آسمان اربیل در حال پرواز مشاهده شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/672786" target="_blank">📅 01:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672785">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d35cb592f.mp4?token=LgqikZTzA_L_AKQSNAw7j6zilX4SGosAvHMhhduOm6eqKz_sdNJuMB8Oh3jmUmNQShhalPzzI5uT6qsCxe_GAKR8ou9uK6jKSDLczSZ4PUpcp_qqcl5-vZJL4bhJFPVH2QLBCWL_EAimouMNvMMKFE_eJ8QEjjmNIErgT08PFr5x28Z6X9V3aF24CA70FyXn-rdbyHC4uhfASXWKsflXrCMsscb-1X_GpeyIP6pKeOigLnh4JvLOIYCu3_x9TwsncfqNhcYdYg_SfazUV-q5s7PYKM02uoHxIfMW4nKbhI2ZZmHbbcuZxeQcz1wlwKfeSapWS2Gn-TMtetMYtG6FJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d35cb592f.mp4?token=LgqikZTzA_L_AKQSNAw7j6zilX4SGosAvHMhhduOm6eqKz_sdNJuMB8Oh3jmUmNQShhalPzzI5uT6qsCxe_GAKR8ou9uK6jKSDLczSZ4PUpcp_qqcl5-vZJL4bhJFPVH2QLBCWL_EAimouMNvMMKFE_eJ8QEjjmNIErgT08PFr5x28Z6X9V3aF24CA70FyXn-rdbyHC4uhfASXWKsflXrCMsscb-1X_GpeyIP6pKeOigLnh4JvLOIYCu3_x9TwsncfqNhcYdYg_SfazUV-q5s7PYKM02uoHxIfMW4nKbhI2ZZmHbbcuZxeQcz1wlwKfeSapWS2Gn-TMtetMYtG6FJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرانسه به خودش آمد، گل دوم فرانسه به انگلیس توسط بارکولا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
2️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/672785" target="_blank">📅 01:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27409c54f4.mp4?token=NJMLnE0deph-dCcBqD8qBhNliBTR9GwZcBzRlOdObshLFJJG2aAYsa_Om0A_6sX50K2hYcf8SWRCfgjVIyEVg_Z0lfG-wMbUqwb4Plrs3WFde8z41RsBYdrUshznlulI7piO7qJ6Tm9YuG-u1bZeGeAZIMlk5CKgdF8LGdH-0GN1Q7Dg0p1ZNFgyY7kpl3UNL0owsNPGcp4yIKPPT6ebrf8LO3ux1kmppHioSFCuP-IpOy_78PCzSLsH7HsrXVl16ZskZbX_11_7lfzHu8REEmxHrVyeL9H5tBGXgxcxrLDMmzaBMPoH8adet43MFnnW5rRgnBFeuDJccsztvNCfow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27409c54f4.mp4?token=NJMLnE0deph-dCcBqD8qBhNliBTR9GwZcBzRlOdObshLFJJG2aAYsa_Om0A_6sX50K2hYcf8SWRCfgjVIyEVg_Z0lfG-wMbUqwb4Plrs3WFde8z41RsBYdrUshznlulI7piO7qJ6Tm9YuG-u1bZeGeAZIMlk5CKgdF8LGdH-0GN1Q7Dg0p1ZNFgyY7kpl3UNL0owsNPGcp4yIKPPT6ebrf8LO3ux1kmppHioSFCuP-IpOy_78PCzSLsH7HsrXVl16ZskZbX_11_7lfzHu8REEmxHrVyeL9H5tBGXgxcxrLDMmzaBMPoH8adet43MFnnW5rRgnBFeuDJccsztvNCfow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به انگلیس توسط امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
1️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/672784" target="_blank">📅 01:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672778">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2530637954.mp4?token=DLjqnGk3ZVHgdXjDmRWyBdmaYVMpv5Mp7Y_bQbpneQGAOkHs08Y5Qa8MArlaUyuEgxLyJcU84a3xBwXdQKlu-YGxsTYbPHKS4n9JX-3826pFGKSQRknTRGcIZLmOolBhErDtOa0cMJKii4HWrDlA6tKaZZglY9ZcyhVXFR03ATFQm6fileChcZqftnv0RYuPmGfuz-hGsa-L0QnIyYN_2uhWHEx9oW1rZ3jLPA8GfwTwreRB-A8gfhRhk5STYRP4SgQPU2WtLDHIHZFAjHwM8HyQIcRVg4f8WwmRTUmd8zEUkvM0QDIFIeFJ7VLS1ZbFW5G2sZjyRPA4M-_BTU1U9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2530637954.mp4?token=DLjqnGk3ZVHgdXjDmRWyBdmaYVMpv5Mp7Y_bQbpneQGAOkHs08Y5Qa8MArlaUyuEgxLyJcU84a3xBwXdQKlu-YGxsTYbPHKS4n9JX-3826pFGKSQRknTRGcIZLmOolBhErDtOa0cMJKii4HWrDlA6tKaZZglY9ZcyhVXFR03ATFQm6fileChcZqftnv0RYuPmGfuz-hGsa-L0QnIyYN_2uhWHEx9oW1rZ3jLPA8GfwTwreRB-A8gfhRhk5STYRP4SgQPU2WtLDHIHZFAjHwM8HyQIcRVg4f8WwmRTUmd8zEUkvM0QDIFIeFJ7VLS1ZbFW5G2sZjyRPA4M-_BTU1U9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تازه از لحظه شلیک موشک از کویت به سمت ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/672778" target="_blank">📅 01:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672777">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc83a1fc86.mp4?token=M7Eu83G7nSstAcsdeqRh41kzFE0OVxKbmqDDDTihetk2j_S84jegYd4JecjnhyyneuWFThjaU9vLRjdsHMxCJdtPJ1AZ8l6IBEv8-oPCTvnMZt8qwn4s4PPQGeEhQPC0pDSyeYJ4yfiotAAzg5_BWqX9iX-XFWJ85VhXNsElHUb4NeY982tbeOKuet5HCT1rcg4VcmmW2k13NUeGviANX8IkxAlecqYZu3oidmWoDUDf__O21GMeUHnIVOmXrvt7KVcv7S_LUxA_Ck7Ox2sD-cRne_r4ZQvQSyWFa_VpXygRR17azYIdggsduVzcXXu2Ax4oTbdBQ8sP6Jxc7JTOfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc83a1fc86.mp4?token=M7Eu83G7nSstAcsdeqRh41kzFE0OVxKbmqDDDTihetk2j_S84jegYd4JecjnhyyneuWFThjaU9vLRjdsHMxCJdtPJ1AZ8l6IBEv8-oPCTvnMZt8qwn4s4PPQGeEhQPC0pDSyeYJ4yfiotAAzg5_BWqX9iX-XFWJ85VhXNsElHUb4NeY982tbeOKuet5HCT1rcg4VcmmW2k13NUeGviANX8IkxAlecqYZu3oidmWoDUDf__O21GMeUHnIVOmXrvt7KVcv7S_LUxA_Ck7Ox2sD-cRne_r4ZQvQSyWFa_VpXygRR17azYIdggsduVzcXXu2Ax4oTbdBQ8sP6Jxc7JTOfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم انگلیس به فرانسه توسط ساکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
4️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/672777" target="_blank">📅 01:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672776">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5f17f766.mp4?token=BxhWVSMndOGVCQgGiHTvlF5B0PWa_Q8AKlFTkXts7iEmoUgYXuH4S95MjpStN31igvF3iQfFGoOR1HnHAnxbPEcbw9-7Sd3jKO5DImBfuCNCuH7IE3QEAVEzqGlxDdZFy6rQtX_8qqD4V7ipmqI0OXir3r2N6TdGgEjiLOvNC6q5zqgBOF7-VrElZX-oPxl3549QiIAL_wV0HTkB7BUWQjhuKH2Ge7ExDhYnCdPinJ4wxJNTX2duR_wFZyyg2xBk8n8w8Efb2hjwh11nKeUjavUwYnOYhWUbnwp_vIkOEzTASx1UZVU7iJng0LEg-6dYt4xllA4NkW3B61QXRI2-tpixxjLZCDvVGZmgyIYoutSdvvUN0qKpOYzy-fPR96NBucgWht7_6Ba27Yo8IOawHff5HNXb-UnaHs0lOBZCh_TCARpnnDEUl3Ohl_8oKyyYantevisCJpya_KgDk1I1DY29cDALR1eOpcAoTNP7bl-I7m3fyu20E2eT9A4wWXIOIYhbgb3aht_cbwXcpDqwQxG6XVNYeSxrW65ShkSHeAh7emcVMpDkWGq_k9iiIAqfuYNEXWBYlxMhysZ_oOUwZgr0p5TNqye9r1A7_cqiLtXe1qfts_uYm1lTYF-0qr3-96Dki-0rOdMEF7-ubawwuIcHDEFQNfn3afi-XmTJHyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5f17f766.mp4?token=BxhWVSMndOGVCQgGiHTvlF5B0PWa_Q8AKlFTkXts7iEmoUgYXuH4S95MjpStN31igvF3iQfFGoOR1HnHAnxbPEcbw9-7Sd3jKO5DImBfuCNCuH7IE3QEAVEzqGlxDdZFy6rQtX_8qqD4V7ipmqI0OXir3r2N6TdGgEjiLOvNC6q5zqgBOF7-VrElZX-oPxl3549QiIAL_wV0HTkB7BUWQjhuKH2Ge7ExDhYnCdPinJ4wxJNTX2duR_wFZyyg2xBk8n8w8Efb2hjwh11nKeUjavUwYnOYhWUbnwp_vIkOEzTASx1UZVU7iJng0LEg-6dYt4xllA4NkW3B61QXRI2-tpixxjLZCDvVGZmgyIYoutSdvvUN0qKpOYzy-fPR96NBucgWht7_6Ba27Yo8IOawHff5HNXb-UnaHs0lOBZCh_TCARpnnDEUl3Ohl_8oKyyYantevisCJpya_KgDk1I1DY29cDALR1eOpcAoTNP7bl-I7m3fyu20E2eT9A4wWXIOIYhbgb3aht_cbwXcpDqwQxG6XVNYeSxrW65ShkSHeAh7emcVMpDkWGq_k9iiIAqfuYNEXWBYlxMhysZ_oOUwZgr0p5TNqye9r1A7_cqiLtXe1qfts_uYm1lTYF-0qr3-96Dki-0rOdMEF7-ubawwuIcHDEFQNfn3afi-XmTJHyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم انگلیس به فرانسه توسط ساکا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
3️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/672776" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpq0LEsDKJilUPMd3UlSZPHvLpdr8WmNByL8VROZiTX-LBFKi1q2m6-6k0cXXPHcQs5n14Q6Vojc1-zsYZQQIvDtQEikJPvgGKsdDKpRZ7mXBZjDV6A_Nm94oIlQJJ0XghNkPFlgIdj-aO09GGGgPgqUMZc57tVk6N3gMuOAMrY4lIqF52Y8Ti9PpEfkjr6nyzLLyODIfszt7vN1Xt9UnNVP5h7IkQMVtCVPLqp2POHzkqVwKqArkNqmXtWfOBoJbt87HlMhq6zDPzzSUA0WSlg8XWFAiYxlloDFtqkUmJvY366MDvF46nvl6vyaGUwc88LpMjTbDpEQycc8spTf1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LGg4TKcoQS8wKG_dKv-W-n7-hAHZ2pW_ieEsCCvgmED5bdldv8lwoKWmu99VC5bQfogin0Rk9wwl2Hl2053y0S5V5Gd5hLETBCfiCpKHUzS3YtIEO3W9JVHSQQQGvYyHCiXp9OCZweq5wRh2VkrQ-83LvOrdAhQL03io_kWzu_naDmlw8I5mCPkXEvKTZYPvkSGpda_cWk8oHUbZ0tBRKocIWNNNsybUjAoAhzVgz42biWSNd_JQBdvZmbhybTEG7lcQHpOQniE21tNB6EmEJ2Zje3conNNRbtxAzmJ0GipzwaNSEPhioS-fyDK9grq3k53WLA6RiJih9FzTlD5a3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4894ed02a.mp4?token=YgtyDC53-89DTF4-_XreBbhZ1cNuOqIw9uGIt_-pL01McNCFBAJtX7Z06-4TRnrpxwcD3lJnBRhKL8v1RDVFWH3HaiMQueQj_vCoNEaIrCQvxeZKla0FUaX6-Q_eO1IyLcutFK74oH3yD0ydhg6rCayxQVR_tc582ERP0OgRcDTIMimC7B4gFT0ME_wnwYbswSVFSDEOEK7ZvJ8voWXlVKBpqdy_o6PeCDjt9GLF05vaOJxSftH2n84oevAV-e7vsDhmSzQ0kHuj0KOAEmv3Gms-KCKu-42iqf8iIP7v8ypciwJSAN8FEL8ard6AdlyA4-M2FZ8JUzgZvQvVgujjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4894ed02a.mp4?token=YgtyDC53-89DTF4-_XreBbhZ1cNuOqIw9uGIt_-pL01McNCFBAJtX7Z06-4TRnrpxwcD3lJnBRhKL8v1RDVFWH3HaiMQueQj_vCoNEaIrCQvxeZKla0FUaX6-Q_eO1IyLcutFK74oH3yD0ydhg6rCayxQVR_tc582ERP0OgRcDTIMimC7B4gFT0ME_wnwYbswSVFSDEOEK7ZvJ8voWXlVKBpqdy_o6PeCDjt9GLF05vaOJxSftH2n84oevAV-e7vsDhmSzQ0kHuj0KOAEmv3Gms-KCKu-42iqf8iIP7v8ypciwJSAN8FEL8ard6AdlyA4-M2FZ8JUzgZvQvVgujjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوکراین به مرکز لجستیکی ویلبریز روسیه در شهر الکتروستا حمله کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/672772" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرفوری
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/672771" target="_blank">📅 01:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672770">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
خوک هار در نخستین اظهارنظر خود پس از کشته شدن دو نظامی آمریکایی در حمله ایران به یک پایگاه آمریکا در اردن، به NewsNation گفت: خیلی غم‌انگیز است، واقعاً اتفاق بسیار غم‌انگیزی است. ما از دیدن چنین چیزی متنفر هستیم. آنها در راه خدمت به کشورمان جان خود را از دست دادند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/672770" target="_blank">📅 00:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11dfde57a3.mp4?token=hdYbQGURWIye7NrIJGOoKv9L2qJqG6mEqzvosqMOj3eoSKBANZ8m-XDrGO5y-SoJ5mzbXr1ZLj1nIqSeZHEDJoY1tp5FXoG9Jelx-0-Bol8R9z18PdJlErL60pzCUAtHSe0_xdUy-ncc7Fd2zf0n-JFPwQ-yUpxUFWC7pRraY9_IOVhJK2sSlJPXT0SZFszbHr487-ZAxl8Zx1Mu-5te4Gf4lYBJFbK_7jl8O04WKTJLM2wChF3SitghnQVDMA1rQmT7gk7J5beAPQmj_Bw3OHQOF_jauWAVyj8bQXk492p6SAmixQGm-vVH6Zt7wZNknX8jbaeNbmG44EBkgcPqwF4b7LqbBKV3s8War_2trS96SSyPGCCemL0It8GdGkvar9TJEQ5oENpnu-sW4IUIKMiCuuInNY6zCQz1eD3aAshp2pHCDBw0VL6JPSil8SreQ3MnrPSJZjrW1mqFASHBAoPQ0Ohu4arPTZO3JVU4EkiPy-PXEeB-y59iajt50VscmD-bGoWo76JyDFvpjOEveQXIg8rjl8jAiLDNKSFXz5q8pugNSQxLiM_N16asJ_SYXyTbD8_8GqocT2drhhBu3dXjwsaeCkVqa3JqPf4XZz8mlicQf5xiAeX3XVYf4XxQNOh-lz5UUWuQOF_IhDWLythazbjVt-sZvbUcO9RY3P4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11dfde57a3.mp4?token=hdYbQGURWIye7NrIJGOoKv9L2qJqG6mEqzvosqMOj3eoSKBANZ8m-XDrGO5y-SoJ5mzbXr1ZLj1nIqSeZHEDJoY1tp5FXoG9Jelx-0-Bol8R9z18PdJlErL60pzCUAtHSe0_xdUy-ncc7Fd2zf0n-JFPwQ-yUpxUFWC7pRraY9_IOVhJK2sSlJPXT0SZFszbHr487-ZAxl8Zx1Mu-5te4Gf4lYBJFbK_7jl8O04WKTJLM2wChF3SitghnQVDMA1rQmT7gk7J5beAPQmj_Bw3OHQOF_jauWAVyj8bQXk492p6SAmixQGm-vVH6Zt7wZNknX8jbaeNbmG44EBkgcPqwF4b7LqbBKV3s8War_2trS96SSyPGCCemL0It8GdGkvar9TJEQ5oENpnu-sW4IUIKMiCuuInNY6zCQz1eD3aAshp2pHCDBw0VL6JPSil8SreQ3MnrPSJZjrW1mqFASHBAoPQ0Ohu4arPTZO3JVU4EkiPy-PXEeB-y59iajt50VscmD-bGoWo76JyDFvpjOEveQXIg8rjl8jAiLDNKSFXz5q8pugNSQxLiM_N16asJ_SYXyTbD8_8GqocT2drhhBu3dXjwsaeCkVqa3JqPf4XZz8mlicQf5xiAeX3XVYf4XxQNOh-lz5UUWuQOF_IhDWLythazbjVt-sZvbUcO9RY3P4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیارت
از نزدیک‌ترین فاصله
🔹
فیلم یکی از زائران سیدالشهداء از لحظات با شکوه تشییع و ورود پیکر رهبر شهید انقلاب اسلامی از بین‌الحرمین به حرم حضرت عباس علیه‌السلام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/672768" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر بندرعباس را لرزاند
🔹
بامداد یکشنبه، زمین‌لرزه‌ای به بزرگی ۳.۷ ریشتر حوالی سرگز در استان هرمزگان را لرزاند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/672767" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672766">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9defb1eb81.mp4?token=hmJUW9ZDIMfkGXfEL5kWD6m7JByrBnBBI7AE0gWUqa07cKnK-bqba6fgRDAZQPifUijL5DTN_RcJjWWn7TBjUODNB9M_CGBPZPATmnyqbeEN4fNdx-SKVbBhEykYgLOngNFh0Oae3GoWK-tcxq5tDMlRBzzs-BfJtsvIzieAhGRau4wbwOUNQTdwXUOM2ys58dpAzMx6SmlatmG1ZQmyANMGNPW3CzRU4l0d75QLqOEX7eZ7OYpsmGpruQyh_TpZnJFcO6lt32z50z6MA4mj3Ljr3lQUeVXySmmoG9YEGDNYrosTPUi5LUc-gDNYRuUdeFz6wCSoPKM7eLDlUbe9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9defb1eb81.mp4?token=hmJUW9ZDIMfkGXfEL5kWD6m7JByrBnBBI7AE0gWUqa07cKnK-bqba6fgRDAZQPifUijL5DTN_RcJjWWn7TBjUODNB9M_CGBPZPATmnyqbeEN4fNdx-SKVbBhEykYgLOngNFh0Oae3GoWK-tcxq5tDMlRBzzs-BfJtsvIzieAhGRau4wbwOUNQTdwXUOM2ys58dpAzMx6SmlatmG1ZQmyANMGNPW3CzRU4l0d75QLqOEX7eZ7OYpsmGpruQyh_TpZnJFcO6lt32z50z6MA4mj3Ljr3lQUeVXySmmoG9YEGDNYrosTPUi5LUc-gDNYRuUdeFz6wCSoPKM7eLDlUbe9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به فرانسه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
2️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/672766" target="_blank">📅 00:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672763">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e924394c6.mp4?token=hAd5EVdXAL1UIxFDIBmo5-t8EHO1qcoKdb8Rfw-4xminrWFAEy17J3ErQesl337wkEapinTovBbX0YH38SXjpPrDGzq343dKL4_uI6VzTRbdXR60sNQsJBaUxDbIarNPDLKkRSQB3yK003xXo2XEaZA7bb1chzyK8VRp6rKN5mtwdtSZ8j2e1v-LDxElT_a-KOzveQCCBO-WeMa6_Jcm7xOm07gF2aHJWbRHwgZ3MM7eBXvi1s34srZkTJA2SCMc5sI63JXCB5Kq4EwK8xYXclvCjgYi36mqQ5Zi32C72HDT8nSaawcIIPYPms-KbOSLVyAPsNp6XUppgsSYsk-wIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e924394c6.mp4?token=hAd5EVdXAL1UIxFDIBmo5-t8EHO1qcoKdb8Rfw-4xminrWFAEy17J3ErQesl337wkEapinTovBbX0YH38SXjpPrDGzq343dKL4_uI6VzTRbdXR60sNQsJBaUxDbIarNPDLKkRSQB3yK003xXo2XEaZA7bb1chzyK8VRp6rKN5mtwdtSZ8j2e1v-LDxElT_a-KOzveQCCBO-WeMa6_Jcm7xOm07gF2aHJWbRHwgZ3MM7eBXvi1s34srZkTJA2SCMc5sI63JXCB5Kq4EwK8xYXclvCjgYi36mqQ5Zi32C72HDT8nSaawcIIPYPms-KbOSLVyAPsNp6XUppgsSYsk-wIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول انگلیس به فرانسه توسط رایس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
1️⃣
🏆
0️⃣
🇫🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/672763" target="_blank">📅 00:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672762">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ضربه به شریان نفتی جایگزینِ هرمز در عربستان
🔹
در حالی که عربستان برای فرار از بحران تنگۀ هرمز، صادرات نفت خود را به بندر ینبع در دریای سرخ هدایت کرده بود، گزارش‌های غیررسمی از خسارت به تأسیسات نفتی این منطقه حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/672762" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672761">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX7owXoZ2yNQfCghggDUDLhbgE2mazEXU4uwOSlvEybV0BYwPyDHRBI-jf0J6PplgiNGUgGMU8-bEDqVIiTpqZzhru7FNjPF52IOzSbiCHlun1mnYDjn5VS_OTW0u7iC9VUEarSY0Cpe1XsYlg99pMavwIQZTxr6OvNAtiOqFVdcdKVDkGtsDdLJbchfEdauL3UJydSJlRgK_L5CewBszTvsWeHT7AiVboAI8NVCR-Qu7f5-TPYjS4QZCliSwHJL4RmZGd0iwq4PwwdX1XWHQ0XNF83M6d9qbgk0yshUQ0yduwspkAOzCW0PHIDZ1lm9bnafLn0QlR1b5_tOX72Rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا هشدار امنیتی جهانی صادر کرد
🔹
وزارت امور خارجه آمریکا با انتشار یک هشدار امنیتی جهانی، نسبت به افزایش تنش‌ها در خاورمیانه و احتمال تشدید غیرمنتظره بحران‌ها هشدار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/672761" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672760">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
افشاگری نیویورک‌تایمز از حملات پی‌در‌پی ایران به پایگاه آمریکا در اردن
نیویورک‌تایمز:
🔹
مقامات آمریکایی جزئیاتی از حملات ۵ روز گذشته ایران به اردن ارائه کرده‌اند که پنتاگون هنوز به‌طور علنی دربارهٔ آن‌ها صحبت نکرده است:
🔹
حملهٔ اول: به یک مجتمع مسکونی در پایگاه هوایی ملک فیصل اصابت کرد و منجر به مجروح‌شدن دست‌کم ۵ نظامی آمریکایی شد.
🔹
حملهٔ دوم: پایگاهی در شرق اردن را که محل فعالیت بالگردهای بلک‌هاوک آمریکایی بود هدف قرار داد و خسارت شدیدی به تعداد زیادی از آن‌ها وارد کرد.
🔹
حملهٔ سوم (۴۸ ساعت قبل): موشک‌های ایرانی پایگاه هوایی موفق السلطی را هدف قرار دادند؛ یعنی همان پایگاهی که روز جمعه نیز نیروهای آمریکایی در آن کشته شدند.
🔹
در آن حمله اولیه، حدود ۲۰ نیروی آمریکایی که درحال دویدن به سمت پناهگاه‌ها بودند مجروح شدند، اما کسی کشته نشد.
🔹
حملهٔ چهارم (روز جمعه): با حملهٔ مجدد ایرانی‌ها به این پایگاه، ۲ نیروی آمریکایی کشته و ۴ نظامی دیگر مجروح شدند. سایر پرسنل نیز  جراحات سطحی داشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/672760" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672758">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
شبکه اسرائیلی i24NEWS به نقل از منابع خود ادعا کرد که یک هسته وابسته به حزب‌الله لبنان قصد داشت یائیر نتانیاهو، پسر نخست‌وزیر اسرائیل، را در محل اقامتش در شهر میامی ترور کند
🔹
بر اساس این گزارش، سازمان امنیت داخلی اسرائیل (شین‌بت) این طرح را در آخرین لحظات خنثی کرد؛ زمانی که اعضای این هسته پیش‌تر به طبقه زیرین آپارتمان محل اقامت یائیر نتانیاهو رسیده بودند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/672758" target="_blank">📅 00:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672757">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
شبکه CNN گزارش داد که دولت ترامپ به‌طور اولیه با اعطای مجوز به عربستان سعودی برای غنی‌سازی اورانیوم در چارچوب برنامه هسته‌ای غیرنظامی این کشور موافقت کرده است
🔹
اقدامی که در پیش‌نویس توافق هسته‌ای میان واشنگتن و ریاض آمده و اکنون در انتظار امضای دونالد ترامپ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/672757" target="_blank">📅 00:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672756">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06c16cad.mp4?token=niRMLl8reYd20A5vZ9d6jJ8DdMDGId9RiavFV928pdVM2YeFxwo_jUeCiWhvbBew9v6oebCK-LDh52fe0qcbBxdXTt5JVkRxMXkSzI5u41VzBi1caDAFbrsDI8zJOVaieC4mKXMJ8__atTpeH5r53wYg4K7_oUY0jVtTwKjXjEiMtT-nHrh6f80FOfire1rdFH7X1jOsaHim5B_7SHlQO3kKHF35gDMOQlQ4ma5M92UXjAiRKslCwktmbts28KoFmZGJh_YT7X2-2w4vZZakDR132s2o9rRcg-uI2g88uBSDfg2hfBZSIszojCPJmBGnjImEywbDMre7GdBo0SLCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06c16cad.mp4?token=niRMLl8reYd20A5vZ9d6jJ8DdMDGId9RiavFV928pdVM2YeFxwo_jUeCiWhvbBew9v6oebCK-LDh52fe0qcbBxdXTt5JVkRxMXkSzI5u41VzBi1caDAFbrsDI8zJOVaieC4mKXMJ8__atTpeH5r53wYg4K7_oUY0jVtTwKjXjEiMtT-nHrh6f80FOfire1rdFH7X1jOsaHim5B_7SHlQO3kKHF35gDMOQlQ4ma5M92UXjAiRKslCwktmbts28KoFmZGJh_YT7X2-2w4vZZakDR132s2o9rRcg-uI2g88uBSDfg2hfBZSIszojCPJmBGnjImEywbDMre7GdBo0SLCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امروز روز امتحانه و در روز امتحان جز دفاع از خاک راهی نیست!
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/672756" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672755">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHUHjBtddNmnw4DPgJ0qrBzsqyvoXTHyqRjxWhiHKixPPGEk0OXxcdyj91KUedDVg5w0UYtfB15Sx0w8cXvJn14T1Thd_KZAuvpDE929g6zlXAKVTywJZGCXllHowFfrEvGMtDMiwW8ug1du2P3imo5-NWqc4XgpsQSLll3bxSW9hbvRgLGn1j6QPB-Ox-mOevcgNuDfG8NsfHJgm83INEQE0irv9_HfdrIX6eJ0uvzztyBCm7row9HdgqzSAa596Fa-cFsMNCtcSk0oLvrDgwIrjEJavXQKxO_0ol726bpemJedflmvQg83-WuijaXP9mvIY39uUMQNhO4jWmSnJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارس‌خودرو قیمت جدید ۹ محصول خود را اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/672755" target="_blank">📅 00:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672754">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FieSlzgb39gmidLXaobo-teQXDSRDyuBBYb67YfUAAZSaVApRzMiNa1esz-roZdXvWd4ZIK-jO82ToWarx6Bd8Tm2CKa_CYjBHIRXxxAsgQ918xxb3a4JPRLImFkqbAzg59sPzFZ5khp2NLmok0iPyBtqMk4xl9RwcAbVvQiOtzAl_XYJeVJXUuhKgbgVXZfMkwJM_Y67lwyf45yRW00Xsj1OkLi6MMuAoiSp76l_dkcrOop1-MxU5D_N1OpHZtQfWwrRS2VjxLNbfN9Ehxxs3q48el7ub9UQ0RMEpPhBr6VCmFPOc2gIcLDKjAInKLW1pzIU4H9-zsaq4LYBY0m_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اتحاد
اعتماد
انسجام
رهبر معظم انقلاب امروز در پیامی فرمودند:
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی سطوح مردم و مسئولان و در تمام عرصه‌ها برای تحقّق آرمان‌های بلند انقلاب اسلامی و تأمین عزّت و استقلال ایران عزیز خصوصاً در برابر دشمن جنایتکار و حیله‌گر امریکایی است. همانگونه که پیش از این مکرّراً و مؤکّداً تذکر داده شد، صیانت از وحدت و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوتهای اجتماعی وظیفه‌ی همگانی است و البته نقش مسئولان و عناصر دلسوز و دلباخته‌ی انقلاب و امام و رهبر شهید در انسجام و یکپارچگی کشور، مهم‌تر و حسّاس‌تر است.
🔹
هشتصدودوازدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/672754" target="_blank">📅 00:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672753">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBCQ6NalIGn0aVD7wGk4k5-DEmQ5izM-AKU05ruySL6kRxCrzZ5w42NaQF39n9idHNZVo_EpgyQ8XoludqtzQDvbMU-QdmYiY9-Qly0ez33-VUdkoXvI5tOunWF-Q_tFspHN7zRdpxw35ikzr5rkM7az4MWzqOd8-0mIxgxzt0QdhUwLXchRfPctqYq7YLHiZAUCy0tBP-c9rN-yX8pMfqEk7FzrLxh4IBBQyMTKVmP_k-I6CbFn0X7cQX7ewu4Ar3ChxwrW9SDqTDe5odLMZxpYffzjzPbR8FHq7--kAeixucKnCEvpFEqUyQHZ14oGdUsLUf96wif-5w6jap9GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت آب‌گرفته خیابان‌های نیویورک در فاصله ۲۴ ساعت تا فینال جام جهانی ۲۰۲۶ #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/672753" target="_blank">📅 00:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672751">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhPngkEIiKyeNiFdoryuLLyEDmfERf8m2ZkQbJHcbnl71wrAPgY59yqKF1DV-NxnXlZ-nph5uZ_6epPxnukDZBNELOZ8Vv6SP4N3nO_joXnXdz3E8s82diWYP5BNsh660B_r4TuGePPz7r0h2INEdcZJWvJoWpG48Ky2ZcrT0A2q5PKEjOfnBelxUMWhVCkG2pGmzebzxhEJBcVYI9KpH4UbyQ3vOYImFsP7BYoP-chnp3TyJCaUHP35SbW7aXGF2BAyXNV9_9SNPjGZaFAxHydF4LcSDZ5t7fXjs0fe1-1kZJDTmF_4KTrqYfyBuVK-NL0fghYjZZ2C8cVcxN7coQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/672751" target="_blank">📅 00:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672750">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3be390f66.mp4?token=BoB69xWb1iABo4aOKFXku8iEAeTPcnGtZIUYZgwecH105S3v1H63IrdFkj2S3-pgbvWsAq5zD8xz6d60VHvPf7743Y2I-rGrAlZQutiaJUj_k78-xsvAe2_1a-BoXDkM_UInZCZmr0zWEREzx1Cgv7ot3pCX6KXRaDARQupMHmJXiR9UWJmHtBIct7GC_Y_IczgfOOdNi2t3x_MklLb0w_dLwE0JgRM0XgV4r22Wrf7e0Tf0oqMCgB2qdouXCalkhI6tS5CMM_gGMrlUEbO7fdGciT8iRdXOaV8KnXjXBUi-5hmIIS2aBrlRfIags7TFTyrqW_AE1MJC9rL2jhRxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3be390f66.mp4?token=BoB69xWb1iABo4aOKFXku8iEAeTPcnGtZIUYZgwecH105S3v1H63IrdFkj2S3-pgbvWsAq5zD8xz6d60VHvPf7743Y2I-rGrAlZQutiaJUj_k78-xsvAe2_1a-BoXDkM_UInZCZmr0zWEREzx1Cgv7ot3pCX6KXRaDARQupMHmJXiR9UWJmHtBIct7GC_Y_IczgfOOdNi2t3x_MklLb0w_dLwE0JgRM0XgV4r22Wrf7e0Tf0oqMCgB2qdouXCalkhI6tS5CMM_gGMrlUEbO7fdGciT8iRdXOaV8KnXjXBUi-5hmIIS2aBrlRfIags7TFTyrqW_AE1MJC9rL2jhRxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارت سنگین به آکادمی امنیتی کویت در حملات موشکی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/672750" target="_blank">📅 23:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672748">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
آغاز دور جدید عملیات روانی دشمن با ۳ محور هم‌زمان
🔹
ارزیابی دستگاه‌های اطلاعاتی حکایت از هم‌زمانی ۳ جریان در روزهای اخیر دارد؛ تشدید القای فشار اقتصادی، تحرک رسانه‌ای هماهنگ برخی سلبریتی‌ها و افزایش مواضع انتقادی چهره‌های سیاسی.
🔹
آنچه ناظران را نگران کرده، شباهت توالی این رویدادها با روزهای منتهی به وقایع ۱۸ و ۱۹ دی‌ماه ۱۴۰۴ است؛ الگویی که در آن زمان نیز به اغتشاشات انجامید./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/672748" target="_blank">📅 23:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672747">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0TkhWO6rNdZUc9-A2lyYSjpNNzXRUH0N7FOevHL6dziw8uSnMV2HhmpliTrJ2LzkWpdngGzxJyCnTYOr2FvFVr92KIC9keASaunH3Ks69TVCyFLidbtAuMBGHgr2Bh1iLj63FH-reQ1TQ1oofLEbqSxWQRt8sc2ObZzoDswkIg6qzjZNS16mTrRqm1v07LYDTFXCOog2satlOtMggNBjGMHfsC1J73gMYNrI5IpTjf73b1T-asNsOUzSq_VsfNRL5U6B83TZXyKVMOPgR-iLjiN6m0Gv53OD4rhrlaYR1ZY7uWK4aK9yrHTvxX-1HNoC5ed8HY0R2C8tTyriPwE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی دیگر از حملهٔ موشکی دیشب ایران به پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/672747" target="_blank">📅 23:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672746">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
وال استریت ژورنال: مقامات آمریکایی می‌گویند ایران با استفاده از موشک‌های فوق‌سریع و مانورپذیر که رهگیری آن‌ها دشوارتر است، خود را با پدافند هوایی آمریکا سازگار کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/672746" target="_blank">📅 23:37 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
