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
<img src="https://cdn4.telesco.pe/file/uOjE-jBvy0SBNKaCgzMCLwWI1S5i3llXovSkYAoRpq2UYvKJ4CzDBbLhkxxB9la7gjyjE7eO-1Vzma93lNGjiRau2JGiTg5b9O2scYlRu9029JH2D7QRLZzrRL8qH5arV6LjHRXvZhDhNnpoAsoGSVUdxCpDX0BKU2LkOIZOYi1gfYBJAyLXQi69Is-oluJJ2Vo4y8kmgb9OH09_Jo2ENL1iT07JjYwW3m6ZfdwaIcno2B-oFOobsXReM9FyDg-IOBBDldmGG6iavVs3EPwbc0TPsC-kf07dM9ZnRCILma0ybP0oaI_pQnHl4jDK0AYy8qp3KaF7W7W2NEsCqUGRMw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.33M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 00:42:49</div>
<hr>

<div class="tg-post" id="msg-683814">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزینه حمل برنج وارداتی ۸ برابر شد
محمد مختاریانی، رئیس انجمن واردکنندگان و صادرکنندگان برنج ایران در
#گفتگو
با خبرفوری:
🔹
هزینه حمل هر کانتینر برنج از هند، قبل از جنگ ۶۵۰ دلار بود که بعد از جنگ به ۵۲۵۰ دلار رسیده و هزینه واردات از پاکستان هم افزایش یافته است.
🔹
با این حال به دلیل پایین بودن تقاضا، این افزایش هزینه هنوز اثر خود را در بازار نشان نداده و برخی کالاها حتی به مرحله ضرر و زیان رسیده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/683814" target="_blank">📅 00:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683813">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ed1ee222d.mp4?token=YYdzHNJ7b69KSo14yXtBdZvFa_zTkTvMarIuvoETKbXl7dsjFpxw06La5PxnhV3WQpGYiYvGlT0SAT046o8Q55n6QbG7IOta0m1E7ydZVCNRHeNpm8LVkrvoiYjaZbxmxvQQIGw_33vGfh6yNiwsGoY7hoJsPQINvyEGQiW6AP_fFqcKgseZJpGyohS9WvOeRmw0ZlJoC7MtMPKy4eE-lvQbUtcgknxHYKuSSFMgy65BxAgPJRXfDVJq5c6XOHdZ9xLjBcIGLJesyXmPC1DOONzUtUWq2AzU7LjNvOqGBzX6V3CN4XwPs6jdpCb8Z4TkA_U2cPqU4M7cZFDL8rsQcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ed1ee222d.mp4?token=YYdzHNJ7b69KSo14yXtBdZvFa_zTkTvMarIuvoETKbXl7dsjFpxw06La5PxnhV3WQpGYiYvGlT0SAT046o8Q55n6QbG7IOta0m1E7ydZVCNRHeNpm8LVkrvoiYjaZbxmxvQQIGw_33vGfh6yNiwsGoY7hoJsPQINvyEGQiW6AP_fFqcKgseZJpGyohS9WvOeRmw0ZlJoC7MtMPKy4eE-lvQbUtcgknxHYKuSSFMgy65BxAgPJRXfDVJq5c6XOHdZ9xLjBcIGLJesyXmPC1DOONzUtUWq2AzU7LjNvOqGBzX6V3CN4XwPs6jdpCb8Z4TkA_U2cPqU4M7cZFDL8rsQcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع محلی از وقوع آتش‌سوزی در شهرک «الرام» در شمال قدس اشغالی خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/683813" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683812">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d8a90682.mp4?token=HjrnMH0hKVsJp-Y_adOWBikQ5yu7stRb2A6PF5-tpkhWgKKMGdL2tqqGue8vu69DSi2VfYSReXGfn5GgFpNKJYAPpKdTTOoXlyRA2TOQonJfLiqpy7Gc6R0ZbN8zw28QYOKhYEjgczuKh2adheHzIM1U5I_UepcHmxlBmOGyu5Un2rMuNZkx7x2qQ2YqvjNsq3wqxLihsZSipTFpk6aol_UtFeyuT_fnsWzOMv593KplU5Zy7hEiJ07Z07pcfukngULBPMmjY_BvyeqVRIRGBxTHmVQ3qedaiXOOEzCmdbeGjsCHQqBplEaM47v3entPaNg4em2mkkL-WiepejB4Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d8a90682.mp4?token=HjrnMH0hKVsJp-Y_adOWBikQ5yu7stRb2A6PF5-tpkhWgKKMGdL2tqqGue8vu69DSi2VfYSReXGfn5GgFpNKJYAPpKdTTOoXlyRA2TOQonJfLiqpy7Gc6R0ZbN8zw28QYOKhYEjgczuKh2adheHzIM1U5I_UepcHmxlBmOGyu5Un2rMuNZkx7x2qQ2YqvjNsq3wqxLihsZSipTFpk6aol_UtFeyuT_fnsWzOMv593KplU5Zy7hEiJ07Z07pcfukngULBPMmjY_BvyeqVRIRGBxTHmVQ3qedaiXOOEzCmdbeGjsCHQqBplEaM47v3entPaNg4em2mkkL-WiepejB4Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۸۴ ساله، اما همچنان در خط مقدم مهندسی هوندا؛ Chief Engineer با ده‌ها پتنت ثبت‌شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/akhbarefori/683812" target="_blank">📅 00:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683810">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4afcac9a7.mp4?token=L3OC4DlnNHTT6XZGffpp1ZLjyWPO-z5s-SoQx5X0TkHFWaXN8MpDJvegrsdQV4euq7hqOAOljaIUtjwCXmR0Mgu5PjWFlG_x_JHS5Lb7Tjxg1W5mreORjftjM5sntuM-DHx_c1tf-sH-HYIattjhqGV6yu3OAu23xNVICJteXzVJ4veb0PWNldWtmc0MZaYkWgI-gBUwVqrgybxwYU02UTSafFgo3Mbt6nT7o4tl3PK4ymoNooe7eKludMASqrZti7aTVxM4iPEHnkGbb6h_7sHPsbNg543Ftoy5noEQorsbk6IosiKRIJ_Q77bCatasCPsp7GHAI9JBK3n321mNWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4afcac9a7.mp4?token=L3OC4DlnNHTT6XZGffpp1ZLjyWPO-z5s-SoQx5X0TkHFWaXN8MpDJvegrsdQV4euq7hqOAOljaIUtjwCXmR0Mgu5PjWFlG_x_JHS5Lb7Tjxg1W5mreORjftjM5sntuM-DHx_c1tf-sH-HYIattjhqGV6yu3OAu23xNVICJteXzVJ4veb0PWNldWtmc0MZaYkWgI-gBUwVqrgybxwYU02UTSafFgo3Mbt6nT7o4tl3PK4ymoNooe7eKludMASqrZti7aTVxM4iPEHnkGbb6h_7sHPsbNg543Ftoy5noEQorsbk6IosiKRIJ_Q77bCatasCPsp7GHAI9JBK3n321mNWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سروصدای برخی از هواداران تراکتور مقابل هتل پرسپولیس
🔹
تعدادی از هواداران تراکتور امشب مقابل هتل محل اقامت پرسپولیس در تبریز حاضر شدند و با ایجاد سر و صدا، برای دقایقی آرامش اعضای این تیم را برهم زدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/683810" target="_blank">📅 00:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683809">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سانا خبرگزاری رسمی سوریه به نقل از یک منبع دیپلماتیک سوری: یک هیئت سوری به ریاست الشیبانی روز یکشنبه با میانجیگری آمریکا در اردن با یک هیئت اسرائیلی دیدار کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/683809" target="_blank">📅 00:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تداوم حمله هوایی و عملیات انفجاری ارتش رژیم صهیونیستی در جنوب لبنان
🔹
رسانه‌های لبنانی اعلام کردند ارتش رژیم صهیونیستی منطقه جنگلی «علی الطاهر» در سمت النبطیه الفوقا در جنوب لبنان را هدف حمله هوایی قرار داده است.
🔹
همزمان منابع لبنانی گزارش دادند نیروهای رژیم صهیونیستی در شهرک «الطیبه» در جنوب لبنان یک عملیات انفجاری و تخریب انجام داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/683808" target="_blank">📅 00:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683807">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس:جبهه اصلی ما، جبهه اقتصادی است/ باید طراحی دفاعی داشته باشیم
شاهرخ رامین، نایب‌رئیس کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
ما در یک جنگ ترکیبی هستیم که جلوه‌های اقتصادی و فرهنگی آن از موضوعات نظامی مهم‌تر شده و جبهه اصلی ما، جبهه اقتصادی است.
🔹
طبیعی است که یک طراح دفاعی حتما به دنبال محورهای اقتصادی بگردد. بنابراین می‌بایست همگان را برای تلاش و تولید بیشتر فرا بخوانیم تا تاب‌آوری مردم و نظام در این فرایند بالاتر رود.
🔹
باید در نظر گرفت همان‌طور که جنگ نظامی نوعی علم است، در نبرد اقتصادی هم باید هزینه‌های مرتبط و سود ناشی از آن با روش‌های منطقی و علمی سنجیده شود و مبادا کسی بی‌محابا وارد هر حوزه اقتصادی شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/683807" target="_blank">📅 00:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6As-GgLgI_rdM_klh2OSf9P2zQXHIc8hcFSvhhFUQ9WUkvuYCGU0wd3FSnTf9H1qVbdRotWeEYk91TYoqrJBj4-PG71gGQcdtGZZggjDaucoISGJ8qQISyiisrgu14Xoc6yYrP1ysB2arSpyhHqPhMAAVucNmL9-sKUKMT48IjCjuLzN6PU_rx-MmhVRbtHjiWGabDnukxlZmEZ-io5PDe2SC__D1wIzL4TnOuOt5eHp6cusUqkY-6idRUfP-Vh9w_JR-r1EY__Ng3Wh2wDGKUuaSIMkiOVtyRpLEAG5JL0GvSERCqYSSsH5KChRPIbC6a0F20cjxJ6aVhntG5i1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پکن بعد از گذر صد سال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/683806" target="_blank">📅 00:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683805">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
رئیس سازمان بسیج: این ملت سست نشد و درخواست مذاکره نکرد؛ بلکه این آمریکا بود که درخواست آتش‌بس کرد
حجت‌الاسلام طائب:
🔹
در مذاکرات به سند رسیدیم، اما طرف مقابل ۶۰ روز هم این سند را تحمل نکرد و آن را نقض کرد. فکر می‌کردند می‌توانند با بازگشت به مذاکره، این ملت را خانه‌نشین کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/683805" target="_blank">📅 00:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683803">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHmQ9HViv9_2mGDV1h_fzH3E2Pz1DyFeQTCBW2ABDrMqRPIgeQdOOgpZNsNtyZzmizBhX47b8JPkauB7Bib1IuWO2dAFtQx3BNLSWSkjM3D63lRZ5gMpxfXM7LfkTwTu84lYAZAbjrbyPuOUyWCczPz04gDb8IIScieVoU-kpx2TM5bQ_1j3cTI1fVYudtIKWUdRUrmaMJEPuDAumW0XK09-owQhszAueoqGva1SyCsJ87T4Fn9bbIPrJcQznFsMGIjRphHA34MicD4U0KnFtxr-fINTbXZVHJgB--Ub7w0MK-hde2bZTiQRfPGLvt-yYm6Lq5MRnIFD0x0gUNfVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/683803" target="_blank">📅 00:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683802">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
رئیس دفتر رئیس جمهور: جنگ رمضان قدرت ما را آشکار کرده اما برای حفظ این قدرت به وحدت نیاز داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/683802" target="_blank">📅 23:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683801">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
دلار ۲۰۰ هزار تومانی و طلای ۲۲ میلیونی | تبدیل سرمایه مردم به کاه
👇
khabarfoori.com/fa/tiny/news-3239874
🔹
پاهای خسته‌ای که جای چرخ موتور را می گیرند/ «پیک پیاده»؛ فرزند جدید فقر و فشار اقتصادی
👇
khabarfoori.com/fa/tiny/news-3239896
🔹
20 جنگنده سوخو 35 روسیه که ایران سفارش داد، تحویل شد؟
👇
khabarfoori.com/fa/tiny/news-3239775
🔹
روایت فرزندان میرحسین موسوی و زهرا رهنورد از جدیدترین وضعیت حصر و محل نگهداری والدینشان
👇
khabarfoori.com/fa/tiny/news-3239765
🔹
خواننده مشهور زن می‌گوید اجازه نمی‌دهد فرزندانش فیلمش را ببینند!
khabarfoori.com/fa/tiny/news-3239841
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/683801" target="_blank">📅 23:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683800">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5274835f2.mp4?token=PVONc5H40nsXDizG4Y41K0HlzUGR4xa33khipdINDoRe_HVzid0X-oSLVEdmTbJt09A9FJp4DjzFCWVYe_8l98g9jPnaMllVxBqWGzaZe-67RP6QAHcxKoyQDCBI-U0Xa__kqIeYBIOf9vkm1IgLrkXELIHATsaspJdrjdx8xZrRX9yrLgQhFS-TtIBoREZsb3LzQODXJTYgzEmSTLm4-hEX-RJObE7Eg_Pe9uTaxJark8MgXyswekLtFY0QpvgKG5F0UlIuu2xB-pWSnlecMM3e95-HG-6dtlkC1rha2ac88ADH8s9L_cExyZ9umAWEcQ_neNrtJO326e5VCZm80A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5274835f2.mp4?token=PVONc5H40nsXDizG4Y41K0HlzUGR4xa33khipdINDoRe_HVzid0X-oSLVEdmTbJt09A9FJp4DjzFCWVYe_8l98g9jPnaMllVxBqWGzaZe-67RP6QAHcxKoyQDCBI-U0Xa__kqIeYBIOf9vkm1IgLrkXELIHATsaspJdrjdx8xZrRX9yrLgQhFS-TtIBoREZsb3LzQODXJTYgzEmSTLm4-hEX-RJObE7Eg_Pe9uTaxJark8MgXyswekLtFY0QpvgKG5F0UlIuu2xB-pWSnlecMM3e95-HG-6dtlkC1rha2ac88ADH8s9L_cExyZ9umAWEcQ_neNrtJO326e5VCZm80A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، فقط یک سرزمین نیست؛ خانه‌ای‌ست که ریشه‌های ما در خاکش جا مانده. ما، مردم این آب و خاکیم؛ از جنسِ همین خاک، با نامِ ایران
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/683800" target="_blank">📅 23:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683799">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd65fde1b.mp4?token=Yt55OFKwCOYd4PhCYmxOMB2C8eu0O-ZWY3hK11K9dnI4onHXR9k1g5i1Fzxn-juzBbgWcDre-tsjW6EF9Ll0Ez_c7DbiSfQV5FucpcK8apl1poOjeVe1Z0oO2o4Mp7Soz61yFMty9420uhYEO_BAUr47mvjfBCUJwXF7kt0z5GTBufYxQ3p-pq8oblmOK3M74vmSXRYr78LHnM3F6nonID2BYxPXWpk-mhJC6fv99YZzkNb1tvLXxhsRV8VT7ZUFnwxGIs2pdMt3PvxYHhOIPDQfIb8h72Zc6kHMuTDV7GnVp6OxYHjOgC5KU2FoDEQbdu00BK2Qtu_2Z8oPl-cEMybw7ibuiDc5Bu5VJ5CJcAZ4kUydohWh4SJ1D18bFmYoD3eR-Kvjt2PABBp5zNjkIXaOi-oroCf44YvP6qoqaK5Vlcbi63HXJ95GABOaKfqqFxgv68JFgHqmVIjvmtlm99pFLYya9blQ6t_231o6Ad_RskGXGFvqCAt7R7_sk-atm7em8mMOkDz4CK1B__Raym1N3sedBm9XjKbE7a5YPa8Mr1tHRvfyUX5qiwsPlHBY7jDisaZocZ33EJBdg5_KhsGquTVvAt-QQcEoaePYCifuqqRwLncFtm-o_FQ1Z9Kwi8c5l7vAFwYaa6Jol0lwR9RbLjZ5eiYIfZJ_Rtj9Jos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd65fde1b.mp4?token=Yt55OFKwCOYd4PhCYmxOMB2C8eu0O-ZWY3hK11K9dnI4onHXR9k1g5i1Fzxn-juzBbgWcDre-tsjW6EF9Ll0Ez_c7DbiSfQV5FucpcK8apl1poOjeVe1Z0oO2o4Mp7Soz61yFMty9420uhYEO_BAUr47mvjfBCUJwXF7kt0z5GTBufYxQ3p-pq8oblmOK3M74vmSXRYr78LHnM3F6nonID2BYxPXWpk-mhJC6fv99YZzkNb1tvLXxhsRV8VT7ZUFnwxGIs2pdMt3PvxYHhOIPDQfIb8h72Zc6kHMuTDV7GnVp6OxYHjOgC5KU2FoDEQbdu00BK2Qtu_2Z8oPl-cEMybw7ibuiDc5Bu5VJ5CJcAZ4kUydohWh4SJ1D18bFmYoD3eR-Kvjt2PABBp5zNjkIXaOi-oroCf44YvP6qoqaK5Vlcbi63HXJ95GABOaKfqqFxgv68JFgHqmVIjvmtlm99pFLYya9blQ6t_231o6Ad_RskGXGFvqCAt7R7_sk-atm7em8mMOkDz4CK1B__Raym1N3sedBm9XjKbE7a5YPa8Mr1tHRvfyUX5qiwsPlHBY7jDisaZocZ33EJBdg5_KhsGquTVvAt-QQcEoaePYCifuqqRwLncFtm-o_FQ1Z9Kwi8c5l7vAFwYaa6Jol0lwR9RbLjZ5eiYIfZJ_Rtj9Jos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگ خطرناکی که دیده نمی‌شود اما هر ثانیه ۳۳۳ هزار دلار خسارت وارد می‌کند!
🔹
ماجرا را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/683799" target="_blank">📅 23:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683798">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0214e220b3.mp4?token=YXbsf8GKEwPipGrpnzKwLezVifCyPKqXHDxFLxoAamiYlItNBjHMnDhI64sFUr9DfcHAtcrV_zJsTuC4OfUMQeKmFnR3pXcaeXHH9YvRwyd3PjZd17Nk31tPwCv0MOx1HoyB0A2nIZvo_EKkbpEsjFImFm3IdpmZ1Mo4G3FNFfrJqepz-D9DGpdTRSm9Y7OJPAQ38nxngy0ahvCwnKu5Q8Zb8zk-_lO1ArtGwJ5oXXnVCGFNMDDMez3gfRr-GKyqIrdkG04kwSxEUbhdKo0MBjUqUJW3Yre8zI_YH_0kndq5XmcXxFgbljZYqSrr_9J2v7aOVb6xdF3a-bvuIcM2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0214e220b3.mp4?token=YXbsf8GKEwPipGrpnzKwLezVifCyPKqXHDxFLxoAamiYlItNBjHMnDhI64sFUr9DfcHAtcrV_zJsTuC4OfUMQeKmFnR3pXcaeXHH9YvRwyd3PjZd17Nk31tPwCv0MOx1HoyB0A2nIZvo_EKkbpEsjFImFm3IdpmZ1Mo4G3FNFfrJqepz-D9DGpdTRSm9Y7OJPAQ38nxngy0ahvCwnKu5Q8Zb8zk-_lO1ArtGwJ5oXXnVCGFNMDDMez3gfRr-GKyqIrdkG04kwSxEUbhdKo0MBjUqUJW3Yre8zI_YH_0kndq5XmcXxFgbljZYqSrr_9J2v7aOVb6xdF3a-bvuIcM2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس‌دفتر رئیس‌جمهور از حفظ پایداری دولت در سخت‌ترین شرایط کشور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/683798" target="_blank">📅 23:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78553ca3db.mp4?token=ozFLw4QsgxNzufksC8pwUL10qHkI8TIbdys8GNUwMe_MWWHh6a6if5ZnLUsX-AbAG5aDHyO72XZ3Nj5WMxgvscYT8duWa6lQqG8Wz_3SnlLhAFaNcvc8ERzbnUOPl5Cw4KpFcVljpQkRcEZw4zeHPCKoaHdicNGpda-sr801-3n-PF2smqHu9keqpFbNVic4VTCa2wkKFZAbx3-aEi7rPgIpHs_zzT4qG1RYD5UiKpIKfVs3-WBz841Qn9q85N1Mt6in8lJA-WDCyHRzv90mjVQFTtP-gQ8CrS_0qrH8sEMpBESawH3TFQE0J3IKeVrw-ZU-VsIJaovZbdyejiZSVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78553ca3db.mp4?token=ozFLw4QsgxNzufksC8pwUL10qHkI8TIbdys8GNUwMe_MWWHh6a6if5ZnLUsX-AbAG5aDHyO72XZ3Nj5WMxgvscYT8duWa6lQqG8Wz_3SnlLhAFaNcvc8ERzbnUOPl5Cw4KpFcVljpQkRcEZw4zeHPCKoaHdicNGpda-sr801-3n-PF2smqHu9keqpFbNVic4VTCa2wkKFZAbx3-aEi7rPgIpHs_zzT4qG1RYD5UiKpIKfVs3-WBz841Qn9q85N1Mt6in8lJA-WDCyHRzv90mjVQFTtP-gQ8CrS_0qrH8sEMpBESawH3TFQE0J3IKeVrw-ZU-VsIJaovZbdyejiZSVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرار نیست کالابرگ همه مردم افزایش یابد!  رئیس دفتر رئیس جمهور:
🔹
برخی از مردم نیازی به کالابرگ ندارند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683795" target="_blank">📅 23:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cee0dbb22.mp4?token=A3_yg-y9IFBcvBR3_TMgoP9ue_XzQu99cc2i7bYL5ufmDrINnBWlXJVCHU6bCu041aywbDA4U-vEe6juSrtGy85QjOdlm_0mYEJNggFgRCHW7zJW-kS3UStpgJrc8HxAAAn-rNI7H01AnzyASJ44rvN8DKXCZcfrdxxrSNwfR0VZPIlIUZBc-zro4pV4GJyv6rh2oCYbvv4TImaKjVken3bp8K-azBa2ymbGWrqJgG1D9Lc9aEURdNU_-ds5j16Gdp8QMtnSdOvdxeAgb60SSKAMZc7vddrYe6Fjo1Xyl95dPcZgzDUOMPlrcq5olEIiyZ8SDDGT9Glxz0iRc7VAxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cee0dbb22.mp4?token=A3_yg-y9IFBcvBR3_TMgoP9ue_XzQu99cc2i7bYL5ufmDrINnBWlXJVCHU6bCu041aywbDA4U-vEe6juSrtGy85QjOdlm_0mYEJNggFgRCHW7zJW-kS3UStpgJrc8HxAAAn-rNI7H01AnzyASJ44rvN8DKXCZcfrdxxrSNwfR0VZPIlIUZBc-zro4pV4GJyv6rh2oCYbvv4TImaKjVken3bp8K-azBa2ymbGWrqJgG1D9Lc9aEURdNU_-ds5j16Gdp8QMtnSdOvdxeAgb60SSKAMZc7vddrYe6Fjo1Xyl95dPcZgzDUOMPlrcq5olEIiyZ8SDDGT9Glxz0iRc7VAxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توئییت کاربر خارجی: با مناظر سخت جنوب ایران آشنا شوید، جایی که ترامپ و هگست در حال برنامه‌ریزی برای استقرار نیروهای آمریکایی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683794" target="_blank">📅 23:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fe92a5304.mp4?token=VW9tLS_f1t9ClWbFl7L0uOxi5w1XNmINSJpYL1x4ERZOp6tNtIPiip8L39R517deSpupxx4XEwj635vFM_pOA6MhMWkdqySfuj5cE-2P0pgewtYPM41y9dJccDoIyRBq9yF3x2gJ814OF9VWhUUCdo0Cy-D-7fcsfdSbLBS4eRibqSyJS56dkbXukPuUtxYWHoJVovkKpAVD4L3_3Bisa6K6z_Ped1e-i1Ar4OM9YONpM_paF9RCK4CLslNh1YRJ6rPhbtfeN32FODcdkIdMj0_t2bF-QGjEbykiasLbBmdJoqKQjn5j2ATgo0dZ9ow6IqgR5w_j5MvDFOFazmPZgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fe92a5304.mp4?token=VW9tLS_f1t9ClWbFl7L0uOxi5w1XNmINSJpYL1x4ERZOp6tNtIPiip8L39R517deSpupxx4XEwj635vFM_pOA6MhMWkdqySfuj5cE-2P0pgewtYPM41y9dJccDoIyRBq9yF3x2gJ814OF9VWhUUCdo0Cy-D-7fcsfdSbLBS4eRibqSyJS56dkbXukPuUtxYWHoJVovkKpAVD4L3_3Bisa6K6z_Ped1e-i1Ar4OM9YONpM_paF9RCK4CLslNh1YRJ6rPhbtfeN32FODcdkIdMj0_t2bF-QGjEbykiasLbBmdJoqKQjn5j2ATgo0dZ9ow6IqgR5w_j5MvDFOFazmPZgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از شجاعانه‌ترین صحنه‌هایی که در غزه بارها رقم می‌خورد، امدادرسانی در غزه است
🔹
در حالی که بیمارستان در محاصره بود و خطر شلیک تک‌تیراندازها وجود داشت، بدون لحظه‌ای تردید جلو رفت، خودش رو به بیمار رسوند، اون رو از موقعیت خطرناک بیرون کشید و جانش رو نجات داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683793" target="_blank">📅 23:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683792">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a01e8675a3.mp4?token=tq0nV-KxjEDvozA85UztnuVCiow8mzdF8fAOTLI8tPxwD1JWG4LThSiRfl_7-qfLyDPxakKEw2F9PzPTGiOpiwUDj-22G7w1klmRLWSritbQRfnC7qobfYVc9QQw9auVnY3E-I3NLgszmEpgtq83f74rwNDV8of_b6mmC4x5lRPkXiQtTJ0viuRGy--TO0WknGAHAoJd5JwzfL6uuHNJ5k-QR1pd1YXuobMGBkAlDeqzqvF93Olh1AADh9mIyW6sv63l-H_nHzEh2IBiTO0FsiuW88A2hTgk8c5KmCtX9Kv31ypFMUKPUWkXtvgBGgnMZiyuZRD2rmXNouVTm3z6Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a01e8675a3.mp4?token=tq0nV-KxjEDvozA85UztnuVCiow8mzdF8fAOTLI8tPxwD1JWG4LThSiRfl_7-qfLyDPxakKEw2F9PzPTGiOpiwUDj-22G7w1klmRLWSritbQRfnC7qobfYVc9QQw9auVnY3E-I3NLgszmEpgtq83f74rwNDV8of_b6mmC4x5lRPkXiQtTJ0viuRGy--TO0WknGAHAoJd5JwzfL6uuHNJ5k-QR1pd1YXuobMGBkAlDeqzqvF93Olh1AADh9mIyW6sv63l-H_nHzEh2IBiTO0FsiuW88A2hTgk8c5KmCtX9Kv31ypFMUKPUWkXtvgBGgnMZiyuZRD2rmXNouVTm3z6Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیو را حتما ببینید: نکات مهمی که در زمان قطعی برق و وصل مجدد آن برای جلوگیری از آتش‌سوزی و آسیب به وسایل باید رعایت کنید
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683792" target="_blank">📅 23:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683791">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای یک نماینده: از ابتدای سال تاکنون ۷۸ درصد تورم داشتیم
رحمت‌الله نوروزی، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
در سه سال اخیر تورم افسارگسیخته داشتیم و از ابتدای سال تاکنون ۷۸ درصد تورم داشتیم.
🔹
در حوزه رهن و اجاره، خرید کالا و کالاهای اساسی سفره کارگران عزیز کوچک شده و باید به‌صورت عملی از آنها حمایت شود.
🔹
باید از ظرفیت‌هایی مانند کالابرگ و افزایش یارانه‌ها برای حمایت از کارگران استفاده کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/683791" target="_blank">📅 23:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683790">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
بورس یک رکورد تاریخی برجا گذاشت
🔹
بورس تهران در مردادماه یک ماه متفاوت را پشت سر گذاشت، هم شاخص‌ها سبز شدند و هم ارزش معاملات جهش کرد.
🔹
ارزش معاملات سهام در میانه ماه به رکورد تاریخی ۶۵ هزار میلیارد تومان رسید و میانگین روزانه معاملات نیز به ۳۱.۵ هزار میلیارد تومان افزایش یافت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683790" target="_blank">📅 23:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683789">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2904c213d6.mp4?token=TDvt5zNzSKMyGbEt7ziV63_TSv4E_9Hs2fTXH51NvObwDcmiuUpzQytfZQxaSU8lYwjRhjhxXyP-zr1uw1DahPRmarJEdn3kAj0mr3N5NyWJ-CFn6-fmK6DGglNGZFE3Hv95NbA8IlWWcuRsgC-P_nhu6jxbOomIqvKZg8tY1baWw5-u1NGPsxBEOwOAqoEZGuo1uYj6suBM4LWaOdwKRsaepWXaLbJx70rcRi9tf8XrxYeL8ZSZ1zCT8BpaTFFnEDfqsOyI7wMDo1T_K0MeVAyXcr0ose4S5QfbRxlqOynDe7a8lKgfLx_DbBbZhSP1DA4qmSRgUV79zWTZJ88Grw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2904c213d6.mp4?token=TDvt5zNzSKMyGbEt7ziV63_TSv4E_9Hs2fTXH51NvObwDcmiuUpzQytfZQxaSU8lYwjRhjhxXyP-zr1uw1DahPRmarJEdn3kAj0mr3N5NyWJ-CFn6-fmK6DGglNGZFE3Hv95NbA8IlWWcuRsgC-P_nhu6jxbOomIqvKZg8tY1baWw5-u1NGPsxBEOwOAqoEZGuo1uYj6suBM4LWaOdwKRsaepWXaLbJx70rcRi9tf8XrxYeL8ZSZ1zCT8BpaTFFnEDfqsOyI7wMDo1T_K0MeVAyXcr0ose4S5QfbRxlqOynDe7a8lKgfLx_DbBbZhSP1DA4qmSRgUV79zWTZJ88Grw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرار نیست کالابرگ همه مردم افزایش یابد!
رئیس دفتر رئیس جمهور:
🔹
برخی از مردم نیازی به کالابرگ ندارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683789" target="_blank">📅 23:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683788">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54768405de.mp4?token=t45SakOYTmyaLN6LAI7IMYXy1-lUTH_pYyvrrKv50NYOUk0Hgq3QRQFFliaf2IIuMLfp63g6GE6strAajiXSqAj-B59OQhHak4MZSSAU2lX0j8uE2txv51gwszPpSuSD1TfRYS3c5wZ4R72l1pFzRz5WPTVUPhpj8c2fgP3S3O6zJQ8tX-CR3_aMYF8Rs_QMugBmeO-T3q2MSfyHRVZMKFEKPB0Ww9VbYqDRmAkUVut3oaFFovP84B-kmB2Ifmc7gUHxb2v4s8cOPZKEnnhaN6k-xlS7hhyoNMaw4XCg9Vx68YWmXqTasrkREcWaLWvCOVnII8n1n7JVErFxu7mmMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54768405de.mp4?token=t45SakOYTmyaLN6LAI7IMYXy1-lUTH_pYyvrrKv50NYOUk0Hgq3QRQFFliaf2IIuMLfp63g6GE6strAajiXSqAj-B59OQhHak4MZSSAU2lX0j8uE2txv51gwszPpSuSD1TfRYS3c5wZ4R72l1pFzRz5WPTVUPhpj8c2fgP3S3O6zJQ8tX-CR3_aMYF8Rs_QMugBmeO-T3q2MSfyHRVZMKFEKPB0Ww9VbYqDRmAkUVut3oaFFovP84B-kmB2Ifmc7gUHxb2v4s8cOPZKEnnhaN6k-xlS7hhyoNMaw4XCg9Vx68YWmXqTasrkREcWaLWvCOVnII8n1n7JVErFxu7mmMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاجی میرزایی: استفاده از انرژی خورشیدی در این دولت بیش از ۴ برابر شد
رئیس دفتر رئیس‌جمهور:
🔹
اولویت ما رفع ناترازی انرژی است و ۱۸ هزار مگاوات افزایش ظرفیت نیروگاهی داشتیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683788" target="_blank">📅 23:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683787">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e97f1ae0.mp4?token=kjs_EoJco34kUC-HIw0W3AvqKlSrrV8ZDRhxNQrmAYd68Nn2VHxoQzKMbuKg8sZvqqDjU6zXxngEwn1MsoZsYGBH-alELdhjc64NFFDSFBb-aPOHnSD16fzabVG3fprBm7tf64TT7VQOqVf7O5_PzPUnZnQJXzkQtB1wPgEkWMemhApGDcfGTvYXWnzFRnKFGEBPjSLHS9oIiaSoVcwUtoWf5YNAs99aw0BaVXbmrqLC4mB-3flxoHYxXAU-42GvqIYkVUt4PxHW-XqUc1Tgb3SHo_U9tF1iVQF6XmQpUGaCI-l9T_858AP4cHtCN23J1E3Uui9b6DR2rfY222pugzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e97f1ae0.mp4?token=kjs_EoJco34kUC-HIw0W3AvqKlSrrV8ZDRhxNQrmAYd68Nn2VHxoQzKMbuKg8sZvqqDjU6zXxngEwn1MsoZsYGBH-alELdhjc64NFFDSFBb-aPOHnSD16fzabVG3fprBm7tf64TT7VQOqVf7O5_PzPUnZnQJXzkQtB1wPgEkWMemhApGDcfGTvYXWnzFRnKFGEBPjSLHS9oIiaSoVcwUtoWf5YNAs99aw0BaVXbmrqLC4mB-3flxoHYxXAU-42GvqIYkVUt4PxHW-XqUc1Tgb3SHo_U9tF1iVQF6XmQpUGaCI-l9T_858AP4cHtCN23J1E3Uui9b6DR2rfY222pugzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توریست هلندی در ایران شوکه شد؛ تازه طعم واقعی یک غذا را فهمید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/683787" target="_blank">📅 23:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683786">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاطلاع‌رسانی بانک سینا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot9Zhj75Kkn19QbaWo0Vz2tw0y5CNgf8QlRvqW_vWv9XajSfiSuxDCyV816dvf_pLOcPZiMQDwF61R8fbfHZkG33Kq2UxHYVU4ao9JiYgC83yMkQcU0YRBnjuDtJtqy_yf44tR7vOhzvDMYKp372C2GCxxjctw8ghOgViNQFFd4vJd4qKGHJowrt6kPlXtAz7SclZkr8C-Vuft-vYkZz8j2K8suUUdesR-P4bM9KFsHVZYzBs9iQaarbvfFza2hCGeRUxdFcCiuFOdyLvaP3_VEhCCh-O5DGigXlZ9nLUSrKbeQcY_w4MIADJ2wOcMzvJ6vv3Jruqoz4JGi45ubGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک سینا در جمع برترین‌های نظام بانکی ایران
از نگاه مشتریان
🟦
رضایت مشتریان، مهم‌ترین معیار موفقیت یک بانک است.
🟨
در نخستین طرح نظرسنجی رضایت مشتریان شبکه بانکی کشور که توسط بانک مرکزی برگزار شد، بانک سینا با کسب امتیاز ۴.۴۴ از ۵ (معادل ۸۹ از ۱۰۰)، موفق شد رتبه سوم را در میان ۲۸ بانک و مؤسسه اعتباری به دست آورد.
🟦
در این نظرسنجی، بیش از ۸۸۰ هزار نفر از مشتریان شبکه بانکی کشور مشارکت داشتند و ۳۰ هزار و ۶۱۷ نفر از مشتریان بانک سینا نیز تجربه خود را از خدمات این بانک ثبت کردند.
🟨
این نتیجه، حاصل اعتماد و همراهی شما و تلاش همکاران ما برای ارائه خدماتی سریع‌تر، دقیق‌تر و مشتری‌محورتر است.
از همراهی و اعتماد شما سپاسگزاریم.
▫️
@sina_bank_ir
| بانک سینا
▫️</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683786" target="_blank">📅 23:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxrohinjDKll404uTsrryzDPNvyFitBUyMiQ-KalZR6yo15h3Eqj7ONQZS7kxZdUry0vu88g8qTsSosuLi9uvQCMNDNc5Bi33-bpy8uNgNSJjEj3rutOLUZ23pCrrX_GOzWygSjsGBjkXoI5RVWPgJRBuNiFj0UOpfh64R6PyD1o1VbSa2LnTFsF57AelYQwMyv7ERmvIlW3T9cZkLe4WJBn6hfDYeJmeoOG6mqv2GYPYAPLzbIpNQkoVKOcYGqmJsXP_KSCQ7T-CKCw69W1eJw9Pcrthypa-Y_n7ZCUWXaYb_2Dz3xEXMCDuFjy86yloBPJeR2t8JJE8_Ji72zoSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار و تحلیل‌گر برجسته تایوانی: اگر آمریکا می‌توانست مسئله‌ای را با «مشت و قلدری» حل کند، قطعاً همین کار را می‌کرد؛ چون برایش ساده‌ترین راه است، هم هیجاناتش را تخلیه می‌کند و هم زهرچشم می‌گیرد اما از پس ایران برنیامد پس دوباره سراغ اقتصاد رفته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/683785" target="_blank">📅 22:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
مشاور امنیت ملی نخست‌وزیر عراق: بغداد پیشنهاد تأسیس یک شورای هماهنگی امنیتی واحد با مشارکت ایران و عربستان را داده است
قاسم الأعرجی، مشاور امنیت ملی نخست‌وزیر عراق:
🔹
گروه‌های مقاومت، دشمن دولت نیستند، بلکه بخشی جدایی‌ناپذیر از ارکان و ساختار ملی عراق محسوب می‌شوند.
🔹
نخست‌وزیر عراق برای دوره دوم نامزد نخواهد شد و به عنوان مرد این مرحله فعالیت خود را با تمرکز بر اولویت‌های فعلی کشور به پایان می‌برد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/683784" target="_blank">📅 22:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V50jb4P07YgVzZb8QqTmXHevMvn8l-nXk1UWPq0nOT4Y01CbtiOfCOIPIvVnHwfCGYBCmFYWNDh2ZbjktsVB0Yidvd67pKKfNn8vu7vUm0Bwf-pBCLuZLnGa3nFqLTW3UfPMHK0euq-QLJX7UwtcLYGhTBwTEOjHjFthWRyWiQMDSft-u-aN3_ZWt2rPDv2qtguydb3u35XLDb-ZolOeN8X6xT0ZumoAI17tIPxsfIvcQq0SfagoMHh3SKjWpi7jU-rKxlaCCl8iIecjqDDyEVzGBsF2nRE6rh1a25GDPfhgH87Kp8T7znerXPo9eAW-y1PA7jir_YIu889Bt1OqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سید محمد مرندی: در روزهای آینده، احتمال ازسرگیری درگیری نظامی بسیار بالاست
🔹
هر کشوری که با ترامپ برای محاصره نگه داشتن مردم ایران همکاری کند، به شدت تنبیه خواهد شد. اقتصاد جهانی در آستانه فروپاشی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/683783" target="_blank">📅 22:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
معاون سابق ترامپ: باید آماده حملات بیشتر علیه ایران باشیم
هیل:
🔹
مایک پنس، معاون سابق ترامپ گفت ارتش امریکا باید خود را برای انجام حملات بیشتر علیه ایران آماده کند؛ اقدامی که به گفته او «اجتناب‌ناپذیر» خواهد بود.
🔹
پنس افزود: «کاملاً ضروری است که فشار را حفظ کنیم و دارایی‌های نظامی خود را در منطقه نگه داریم تا بتوانیم اقدامی را انجام دهیم که به باور من اجتناب‌ناپذیر خواهد بود.»/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/683782" target="_blank">📅 22:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683781">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ML4awDcit9QGf7X7FbR6Yz4Q-adpyh_jeYhd3_xfz6t-P9phh7SbADC3anBLHoSqxjWEnpJ5NXnb1cupss-cyLRAtUB484ixBCKfXXbKMeLEvAVlWriRGnW6o1OqsecOdj9ZlT5ujf4lt5vvhWVu0dchcp-X6c1E2uXHh7k8UtaVNlL_owJff0PtYuOZor1grjDqUG1ls-DhNfg1nHsbKhEig3JViwaaLPo4vAeeW7Yx0IFWu6fjCnyobbnba1VIlWYjWNd26vf5CkEJkEuWe9Ov4eF0BigqFFQi-6j2AB5mpPwIGNulHtC7rFJuExidScEUyolRyavV8JX0_x2I7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌سوزی جنگلی نزدیک  نوادا و کالیفرنیا هزاران نفر را مجبور به تخلیه منازل کرد
🔹
هزاران تن از ساکنان منطقه رینو در شمال ایالت نوادا، در آمریکا با نزدیک شدن شعله‌های سرکش آتش‌سوزی به این شهر، به اجبار خانه‌های خود را ترک کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/683781" target="_blank">📅 22:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683780">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
وزیر کار: پیش‌نویس افزایش مبلغ کالابرگ برای گروهی از مشمولان تهیه شد
میدری:
🔹
با توجه به حساسیت اجتماعی و ابعاد اقتصادی این موضوع، اجرای آن نیازمند توافق دولت و مجلس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/683780" target="_blank">📅 22:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683779">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تقدیر رئیس شورای اطلاع‌رسانی دولت از همکاری شهرداری تهران با دولت
🔹
رئیس‌جمهور بارها از نحوه تعامل و همکاری شهرداری تهران با دولت ابراز رضایت کرده است.
🔹
پس از انتخابات، شهرداری تهران با تمام ظرفیت وارد میدان شد. موفقیت شهرداری، موفقیت دولت و کشور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/683779" target="_blank">📅 22:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683778">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae4dda833.mp4?token=tOI_Ui0-ehpTj1rpoa3hUVe8s97pKVS-xe8Ykd1GqV5lcJvpSvo2X52TKqXmh9YyB0VX6mbpEs7aMAtETMVQ8qn7Kc32tRRcneLBUegsigvb5FE3Ho387MTE8M72WCmE8JS4aSiNFSXJsfRoCXGuL6yhzPRVQEgA8cowUrn-ZeYXPnHaxXgFNDBjnScytDpZtKw9y-0zfkiWLLbP--CEEeGMa_Tpl-E6Eg09ceu9Om1U0JdrkFHaFiuJ3CLnQI_6XO8VvDLj4SFnBjGhpzxzKwJ8_ce56X8hiBQk_ItAltFkuzmSU4bSfuT2EP3ourGmP8z2qPJkn40LvBJEDL0OUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae4dda833.mp4?token=tOI_Ui0-ehpTj1rpoa3hUVe8s97pKVS-xe8Ykd1GqV5lcJvpSvo2X52TKqXmh9YyB0VX6mbpEs7aMAtETMVQ8qn7Kc32tRRcneLBUegsigvb5FE3Ho387MTE8M72WCmE8JS4aSiNFSXJsfRoCXGuL6yhzPRVQEgA8cowUrn-ZeYXPnHaxXgFNDBjnScytDpZtKw9y-0zfkiWLLbP--CEEeGMa_Tpl-E6Eg09ceu9Om1U0JdrkFHaFiuJ3CLnQI_6XO8VvDLj4SFnBjGhpzxzKwJ8_ce56X8hiBQk_ItAltFkuzmSU4bSfuT2EP3ourGmP8z2qPJkn40LvBJEDL0OUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری بازیکنان و کادرفنی شمس‌آذر و آلومینیوم اراک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683778" target="_blank">📅 22:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683777">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKbanpI2chdseKmVvbcPV9EaB89LsNf9v7GA57J5RVYr0FBYlamFkYpw3fJg_nU-fa88Wa6hLr8PVXXTWmq5Th4RBXrRk92ceyrTu7F1SmygBIEv8-lG0F5fwvXccYd73GErATWelpAIIAj1s_9iqfpyj6klNd3SAvN8CIG_Gwifs54THNbRgYyMX-HSC_80EB-1jgaKplLhs6t34HWXIO12zjHb7b5M0J-Tt_Tt2vHaumbyiYFFyMtG77jXP_HC6U-VwHXruFGYiAtlfGlJLq1ARxkXQ41xiFL0UM0LdszKzZmRgRI74jWQXizjwJoMn1MyI6CZJOOkuTArjRublA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: جنگ اقتصادی ادامه یابد یک قطره نفت از تنگه هرمز صادر نخواهد شد
سرلشکر رضایی:
🔹
اگر جنگ اقتصادی ادامه یابد، حتی یک قطره نفت نه از طریق تنگه هرمز و نه از هیچ کجای خلیج فارس صادر نخواهد شد. ایران مشارکت یا حمایت هر کشوری در جنگ اقتصادی آمریکا علیه مردم ایران را به عنوان یک اقدام جنگی تلقی خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683777" target="_blank">📅 22:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683776">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-text">🔸
اختلال اینترنت ایرانسل در مشهد
🔹
بنابر اظهارات تعداد زیادی از مخاطبان اخبار مشهد، اینترنت ایرانسل در بسیاری از نقاط سطح شهر مشهد قطع یا ضعیف شده است.
🔹
طبق نظرسنجی اخبار مشهد حدود ۴۰ درصد از مخاطبان قطع کامل اینترنت ایرانسل در مشهد را اعلام کرده اند.
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/683776" target="_blank">📅 22:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683775">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۴ قطعه یک پازل برای فهم جنگ ایران و اسرائیل
🔹
اگر فکر می‌کنید جنگ ایران و اسرائیل فقط درباره موشک، هسته‌ای و حملات هوایی است، شاید مهم‌ترین بخش ماجرا را ندیده‌اید.
🔹
پشت این درگیری، چند مفهوم کمتر شنیده‌شده وجود دارد که وقتی کنار هم قرار می‌گیرند، تصویر متفاوتی از این جنگ می‌سازند.
🔹
این پازل را کامل ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/683775" target="_blank">📅 22:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683774">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfWgmQ4ZuMGvWDjQoZM8WGxt1ALFiUz_SohbCwdLIpC_UjEiEvVl2RbrNfEYRkYMuJb9RypxtsDKHkKdCP2zTGVmEwS8ZxBcNh2Dx4ql5iQxMtI1V3tskiNRY96IASMJABPfkQfPCPiubyMxh_jK1AqzOK2bG8XHA0WzEV--3BZlZPhhPO1ETcs64rqUmufux0sk_9WbwY5UIX5h-yCwIIIgy0CErFq1rYR267dKtG--bUKJpLb-AwWCsoUHk9cP5PMDmZQEyvz9NtT0n8COn3sMlaptedRElb5zeskqoRlb-Jv9hX3egcWPP1h0E2SyrxdSvJcv8KQt5Dd4iQTTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: جهان ممکن است روزی از اینکه آیت الله علی خامنه‌ای صحنه را ترک کرد، افسوس بخورد رهبری جدید کشور که متشکل از نظامیان است، به نظر می‌رسد سرسخت‌تر و سازش‌ناپذیرتر باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/683774" target="_blank">📅 22:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683773">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پول میلیاردرها وارد انتخابات آمریکا شد
واشنگتن‌پست:
🔹
۱.۶۹ میلیارد دلار؛ این رقمی است که تنها ۵۰ اهداکننده ثروتمند تا اینجای انتخابات میان‌دوره‌ای ۲۰۲۶ آمریکا وارد چرخه سیاسی کرده‌اند.
🔹
حدود ۱.۰۵ میلیارد دلار به نفع جمهوری‌خواهان هزینه شده، رقمی که می‌تواند معادلات کنترل کنگره را تغییر دهد. در صدر فهرست هم نام‌هایی مثل جورج سوروس، جف یاس و ایلان ماسک دیده می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/683773" target="_blank">📅 22:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683772">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
دیدار نماینده حزب‌الله در پارلمان لبنان با عراقچی
🔹
حسن فضل الله از نمایندگان ارشد فراکسیون وفاداری به مقاومت در پارلمان لبنان عصر امروز یکشنبه با سید عباس عراقچی وزیر امور خارجه دیدار و ‌‌گفتگو کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683772" target="_blank">📅 22:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683771">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHXzfrSqRTqdxT1qk8Z56FM6KiXANIuOQyBcU5l00mG_sY4grzd0in-huxY_QWzpHo47wtSlrz58mZqoF-KTJ_SAih4QAiAxN0hycOMy6aILb2QKDCzBzmAroAY11MhTumokQLUiZJJhi1i6xfICIP7r_WBFQWa_ksSZDNjtWRH9X5R4RRxz_M6F_mRE19TxdssnjpXelsY_QzaPa5qv_fBbB-K3alVyKg3M60Nq0SgAhaR23q80ETSpJAM3EB1FKHump2_ldAVhqi9cuDQOu8qCl9gIWFtHbNuaMKG-6mEMbPZErp4lR-dfbz9rzfqwrA6GkNK9OsSdBdhsKKs0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم اندرسون، مدیر اندیشکده مطالعات ضد هژمونیک CCHS در استرالیا: این دلقک نارنجی ادعا می‌کند که تنگه هرمز، به‌همراه بخش‌هایی از جنوب ایران، بخش‌هایی از امارات متحده عربی و بخش‌هایی از عمان را به خاک خود ضمیمه کرده است
🔹
اما او آن‌قدر ترسو است که جرئت ندارد یک ناو جنگی را در نزدیکی آن منطقه مستقر کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/683771" target="_blank">📅 22:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683770">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsU8RTWIW90adzXvqzQbV-eXv3Rql3L777Fl5u6p_tIm-QMGAikr7kHdCe2Edne_e9gLJibW4B2599lhG9YQb4A44DAOLsT4jxtYwuFHhN27CDUSDducPcC-lIYFVAYkaHPacgUSsbkA3zAAUq_EztBFbF-C3V2YLRDp13g22psDJOnhuKHX7aXmpvceYNlC_GbLPP-gRzxdch8gil6qFGMipETGU7MXQHdMvT51qPQKSk1XLw9_GGa5MrJ5Ma6D-6Dmhb824ZDQAhKEMXHIrLL3bt8aKW9fzWXrliFOa8_awkP--dxIijvxYYwGUobsynB3Mb7lUXv7XNpHL5AxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج فارس: شناورهایی که با شناورهای متخلف همکاری کنند به فهرست متخلفین اضافه می‌شوند
🔹
با توجه به تخلف برخی شناورها از ترتیبات ایرانی تردد از تنگه هرمز، این شناورها در ترددهای آتی خود از تنگه هرمز با محدودیت‌هایی مانند جریمه، توقیف یا مصادره مواجه خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/683770" target="_blank">📅 22:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683769">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKc7wBRhB3jVDX8pwRwlKxfObD8UJoCJBjB9S01gVNQ8mu2Z84GeFNeIniBdQLjWETIS9ipcQEBMMpCPRo6KlqiPqiY_7Xebr9x7xyNKQ5CtnL93J7OUQEhMrUovULOi-uPKhURnvwKISRAROR_WzdP7ssuRhuuuJI5HnHth92FJ6W3ujJht66yxLcGc_T6wuYdV0W97pLHQCXWXA01ESn1_uC-0FwuNXi9vHKEsTZZiEqgcHGtIWgeLsMU-e3ow6RHSk2CgTE5yvoDxUYQ1x9hbgcCToSsIbdZXyr4gsMM-em_Y_O9TmHgksOZW7KxvquBRQL40ZViLIM1CV1v_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: انتخابات میان‌دوره‌ای آمریکا در سال ۲۰۲۶؛ اقناع، انکار و لفاظی
🔹
ترامپ در آستانه انتخابات، در جنگ ایران «گیر افتاده» است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/683769" target="_blank">📅 22:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683768">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e6de6f328.mp4?token=n-Ol5B86rP2_SVHTNGjfzbp1ZKKHETt7MyUoNEEtj-FVjcaYk9nSv-tBgeHUhk-3pQuo8rRcZbcLYc32kdMmtVyLL5zF2IPSu3Npc6ZElDdNyT4MphAudgtHiRV8MCJLWWZYUI3ENA1HdmP8VpJKGOqKgFqteez3tuahrWwieLxXSUSBgEP4_BHVaKsbEGmZLG8C9N0arf2vKQ5-R0GGVR00jPFaS_2q66ZS4ZpCkY8jaVW41kL2cMWJKfLE6JXa8p5oDgS_5ChVgkdW4ryJggUvPf9GcjpXALYU1YIWLh6Sgy1CiFjcm9dEOI2sFLNQ1hqJUSnJvEotFLMzIRBAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e6de6f328.mp4?token=n-Ol5B86rP2_SVHTNGjfzbp1ZKKHETt7MyUoNEEtj-FVjcaYk9nSv-tBgeHUhk-3pQuo8rRcZbcLYc32kdMmtVyLL5zF2IPSu3Npc6ZElDdNyT4MphAudgtHiRV8MCJLWWZYUI3ENA1HdmP8VpJKGOqKgFqteez3tuahrWwieLxXSUSBgEP4_BHVaKsbEGmZLG8C9N0arf2vKQ5-R0GGVR00jPFaS_2q66ZS4ZpCkY8jaVW41kL2cMWJKfLE6JXa8p5oDgS_5ChVgkdW4ryJggUvPf9GcjpXALYU1YIWLh6Sgy1CiFjcm9dEOI2sFLNQ1hqJUSnJvEotFLMzIRBAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار نماینده حزب‌الله در پارلمان لبنان با عراقچی
🔹
حسن فضل الله از نمایندگان ارشد فراکسیون وفاداری به مقاومت در پارلمان لبنان عصر امروز یکشنبه با سید عباس عراقچی وزیر امور خارجه دیدار و ‌‌گفتگو کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/683768" target="_blank">📅 22:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683767">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee2ZN5h_0Tza7OzlR6K9JjmurmdDqW8HVNZrQgtUxoywhXpg5aGV9_9fv0dvw4Pu-er3FEgl6gqdtT6lUFESU3F71dD61PxoMlOSucuIt9ZqJpkdRubJSx1xO1xUk9mZ1k3_6KLETPOBx_DN3YEMvhg8WheSB7fk_h9lEisUByzj-GPG0aOBFBFcV_-CMzpOy7fg41WxQzW9ezMkPtV3XmP5iO_2H4W4LQ4aqXkH0jTa0QFoWfM_U2E_zM7o9XA4ZGqNdxmMopsWvGYKfFBidRu2VS_1U8Zgt5FqoWKbqIVvp0BZA2DBn-QTau555d2fALbOvI7gUWpbdj_yMmxhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار: آیا تعرفه‌های کانادا هزینه‌ها را برای خانواده‌های آمریکایی افزایش خواهد داد؟
🔹
ترامپ: بایدن این آشفتگی را ایجاد کرد. بالاترین تورم
🔹
خبرنگار: تورم وقتی بایدن رفت ۳٪ بود. حالا ۳.۴٪ است
🔹
ترامپ: جو بایدن
🔹
خبرنگار: بایدن ۵۷۰ روز پیش رفته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/683767" target="_blank">📅 22:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683766">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
با مفسد مماشات نکنید
🔹
فارغ از تمام هیاهوهای این روزها و جنگی که دامن کشورمان را گرفته، یک حقیقت را نباید فراموش کنیم. روزهای پیش‌رو، فقط به آرایش نظامی نیاز ندارند، اقتصاد کشور نیز محتاج یک بازطراحی عمیق، فوری و شجاعانه است.
🔹
امروز دیگر وقت بخشنامه‌های بی‌اثر، وعده‌های تکراری و برخوردهای نمایشی نیست.
🔹
یک جهاد واقعی و ویژه اقتصادی لازم است، جهادی که مردم نه در تیترها، که در سفره، بازار، شغل و زندگی روزمره‌شان آن را لمس کنند.
🔹
باید با مفسدان اقتصادی بی‌اغماض برخورد کرد با دانه‌درشت‌هایی که سال‌ها از رانت و خلأهای نظارتی بهره برده‌اند، با محتکران و قاچاقچیان، با گران‌فروشان و اخلالگران بازار، با کسانی که ارز، منابع عمومی و اعتماد مردم را ابزار ثروت‌اندوزی خود کرده‌اند.
🔹
عدالت، اگر قرار است عدالت باشد، نباید پشت هیچ میز و عنوانی متوقف شود.
🔹
باید با مسئولانی هم که گاه با یک تصمیم نادرست، یک بخشنامه عجولانه یا یک سیاست غیرکارشناسی، معادلات یک بازار را برهم می‌زنند و هزینه آن را به میلیون‌ها نفر تحمیل می‌کنند، برخوردی جدی و مسئولانه صورت بگیرد.
🔹
مسئولیت فقط اختیار تصمیم نیست، پاسخگویی در برابر تبعات آن نیز هست.
🔹
در روزهای بحران، فساد اقتصادی دیگر صرفاً یک تخلف نیست، می‌تواند زخمی بر پیکر امنیت ملی باشد.
🔹
مردم نباید احساس کنند که در میدان بحران، تنها مانده‌اند و عده‌ای در سایه همان بحران، ثروتمندتر می‌شوند.
🔹
اگر از مردم صبر می‌خواهیم، باید هم‌زمان با مفسد، رانت‌خوار، فرصت‌طلب و تصمیم‌گیرِ بی‌مسئولیت برخوردی ببینند که صدایش در جامعه شنیده شود.
🔹
امروز کشور به یک جهاد اقتصادی واقعی نیاز دارد. جهادی برای حفظ ارزش پول، امنیت بازار، اعتماد مردم و عدالت.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683766" target="_blank">📅 22:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683765">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3afca9dc.mp4?token=tnTAtsBhYzM-GODBq3KC6PR2AuQlpR6Rhq_N-KJvvC1V_RJArG4RsiNM7jWaxd0YouH0cQJ6uqfhkGBl6t3df0scCLwns3ohbJF_W9zzLkBllLpKhAOB2cLtXyMa4sDkTP9rUKOg4lvM5cKktxBnv3gQRq60yt7DFBf5-Ep0mUhqrTe8gnlLQiX_3DVKf4hbcHxLBY7X9SbJ0jSFwKMoHfB06i0J-Eg7oBKeJ9yyMgIn-uGFcpB0nMNvNUTnG7CQReM651m0aiKyYvAGGAL2l98dCscFeAI4qtl9PZSNFAUexjDtVUWVq-5q2dBUKrA95GKqI4Jcj-D1QwwQPpQm-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3afca9dc.mp4?token=tnTAtsBhYzM-GODBq3KC6PR2AuQlpR6Rhq_N-KJvvC1V_RJArG4RsiNM7jWaxd0YouH0cQJ6uqfhkGBl6t3df0scCLwns3ohbJF_W9zzLkBllLpKhAOB2cLtXyMa4sDkTP9rUKOg4lvM5cKktxBnv3gQRq60yt7DFBf5-Ep0mUhqrTe8gnlLQiX_3DVKf4hbcHxLBY7X9SbJ0jSFwKMoHfB06i0J-Eg7oBKeJ9yyMgIn-uGFcpB0nMNvNUTnG7CQReM651m0aiKyYvAGGAL2l98dCscFeAI4qtl9PZSNFAUexjDtVUWVq-5q2dBUKrA95GKqI4Jcj-D1QwwQPpQm-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادی پس از گل ربات فوتبالیست به سبک رونالدو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683765" target="_blank">📅 22:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683764">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
دویچه‌وله: جنگ‌های ایران و اوکراین ممکن است به یک جنگ جهانی تبدیل شود
ادعای دویچه‌وله:
🔹
جنگ روسیه علیه اوکراین و درگیری آمریکا و ایران به طور فزاینده‌ای به هم گره خورده‌اند. از پهپادهای ایرانی در اوکراین گرفته تا حمایت اوکراین از کشورهای حاشیه خلیج فارس، مرزهای بین این درگیری‌ها در حال کمرنگ شدن است.
🔹
اگرچه ممکن است این دو درگیری به خودی خود خاموش شوند، اما هیچ راه خروج آشکاری برای هیچ‌یک از طرف‌های درگیر وجود ندارد.
🔹
در همین حال، هر روز احتمال اشتباه محاسباتی یا تشدید تنش وجود دارد. ادامه همزمان این‌جنگ‌ها شاید جنگی جهانی را رقم بزند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/683764" target="_blank">📅 22:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683763">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbc2ff0e9.mp4?token=WXmpjkqnD7gfyZ3uZlt0HOiAT6u9uYPe5sRW7CmmJol5Cg39e_GyTBx3o_hCM6_nwnpyEcjc9Rs-yi4g2kmt37T8HxcdFf1Z4YbNtVigflGSJRGAcsuVgS-f49wA_ThcdUN6VFVIJ-jNw_f-9uYo8MvCDNLpYpfYFLTTxREn2XdDduR9OVWzBaTgIcpMWVLoK8MBrpXzFll-AtTL13GmGNbAc3ZOrwDwKHrZmdaATl7JySn0AtPRtpXRrwbBhmfIZYG2R-OZ-RV2eUM9B0V2AnRX7YPDKi2TsZxNSkJbfAY-q4tyo__vuk2YthcqLAk8dJGyequq9oEP2fmCsrgGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbc2ff0e9.mp4?token=WXmpjkqnD7gfyZ3uZlt0HOiAT6u9uYPe5sRW7CmmJol5Cg39e_GyTBx3o_hCM6_nwnpyEcjc9Rs-yi4g2kmt37T8HxcdFf1Z4YbNtVigflGSJRGAcsuVgS-f49wA_ThcdUN6VFVIJ-jNw_f-9uYo8MvCDNLpYpfYFLTTxREn2XdDduR9OVWzBaTgIcpMWVLoK8MBrpXzFll-AtTL13GmGNbAc3ZOrwDwKHrZmdaATl7JySn0AtPRtpXRrwbBhmfIZYG2R-OZ-RV2eUM9B0V2AnRX7YPDKi2TsZxNSkJbfAY-q4tyo__vuk2YthcqLAk8dJGyequq9oEP2fmCsrgGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در زمین گلف جان باخت
🔹
یک بعدازظهر آرام در زمین گلف؛ چند قدم، یک نوشیدنی و اتفاقی که ناگهان همه‌چیز را به هم می‌ریزد. اما ترسناک‌ترین بخش ماجرا، لحظه‌ای است که .... #کابوس_ترامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/683763" target="_blank">📅 22:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683762">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzCmCb-DvTmg0ax4mY__Z9N5jNaTahrcNf1wxUjj7mViwqQFRGOAKfAmCmg9ocZeTEtfBd_3YlY1xDRwHkNlN1V-EsytN8ghAAx6uwjwiqJrerFSn_Ly0aaUymzft3SmHem4TVTq8BMFeZAnov9dk4nNhGyeaZKynXKTJZ9jbdjxYolUoDBjd2fgR7Rlbv6r7TNsFH6pSa81WT8QByjk4TrCLPHSvpqSI4e5iT09CFr74EO7NPYVgJUldNX7d3p7pL7NcItXbCoedf0pgv4rx6oH58Z9ivw4C-KrJgFjjiAn8uME0bzxgCBj6TkOM1Ytm1m8uiXFQn6GI_4N11lNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نعمت، امتحانی برای انسان است؛ نه دلیلی برای غفلت
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که انسان باید نعمت‌های خدا را بشناسد و در برابر آن‌ها دچار غفلت و عصیان نشود؛ چرا که هر نعمتی می‌تواند آزمونی برای شکرگزاری و بندگی باشد. #نهج_البلاغه_بخوانیم
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683762" target="_blank">📅 22:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683761">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuMtPEMhjG_pIsZ8qqUSsCrm2POxeJ1nTwH4zrVsbdSZ7pKJe7o9PAV8qn9lFbtAhHFyeIl9JA12lPlDEUvy1BicBmJmbRojrjaJmSLCd2VQWYaN3FC8zTowTfkpN0V0LH_EsmGxERkTjKXcKabrXe2k2A5iUWG2F7I_3XB5uui97dGqMxRmrkdiRSzjWECX86fKRkABhoJk9fKV-lmT8GJ1MzpQ1TlIYE98V13VMHt7F6aZuEkCdn4qGOXHsX4A20B9JUds6r9tB1HKA71TgZun5ALtOOSSZxe0TRUSwSiROw5k9dkyh_-CdBM80_GO6HYB_uDEvQimnzF2iCtMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر پس از پایان روز اول از هفته سوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/683761" target="_blank">📅 22:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683760">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f548c60e11.mp4?token=Tw30NcCCwR7IUEOAGWux2k9KQrLrfZrV5_To4fXSwMSc5fr_3tNB5eureMJrOqX4kHFz4RLYaLez4lgOVx01Xe6h9epRpIBG8kodKY6IjdU9loxkycVKIUTs-4DxBUI6BB_24lLII22hF1mRaQCoKbUTiLRy-3r7XK-1-hH-t0OJV06lvWm5NF21Sjmrvh8skdTCjsxQCAwTK5H8mhowqdLjGg8HNM4NLS_Xd6Hi1cc3zwHsq2e_GYcXL-eOdpflyEy3BtWXpUZblX7hv4nAqcztYhrGhvEDU4yzm2bg35U_-fbN4XqJrEAckThl4Ee4NFn5KD_8XL0MHEBVTxUbiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f548c60e11.mp4?token=Tw30NcCCwR7IUEOAGWux2k9KQrLrfZrV5_To4fXSwMSc5fr_3tNB5eureMJrOqX4kHFz4RLYaLez4lgOVx01Xe6h9epRpIBG8kodKY6IjdU9loxkycVKIUTs-4DxBUI6BB_24lLII22hF1mRaQCoKbUTiLRy-3r7XK-1-hH-t0OJV06lvWm5NF21Sjmrvh8skdTCjsxQCAwTK5H8mhowqdLjGg8HNM4NLS_Xd6Hi1cc3zwHsq2e_GYcXL-eOdpflyEy3BtWXpUZblX7hv4nAqcztYhrGhvEDU4yzm2bg35U_-fbN4XqJrEAckThl4Ee4NFn5KD_8XL0MHEBVTxUbiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحقیر کانادا توسط وزیر حمل‌ونقل آمریکا
🔹
این کشوری است که ارتش ندارد... نرخ مرگِ خودخواسته در آن به رکوردی بی‌سابقه رسیده است.
🔹
اینکه فکر کنند می‌توانند وارد جنگ با دونالد ترامپ شوند و واقعاً در جنگ با آمریکا پیروز شوند، از نظر من کاملاً احمقانه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683760" target="_blank">📅 21:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683759">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzdIbKHrwqSW45oLmx87PnGKnjwHJIwG3u10110yGZ_PNNcADRHkjj14Xdt8sB2_xK_oVj9etJ2GeziY1zLKyJDQFCQ4u-BaJXmeF0O-cjGROiAphpBetZ2ivyy_peV_GP5OmR85o2KwKz-F7tZotWfGZ5cHg5-I2A5iE5-kBisYyPgdsGOifrMRww59O5vlQY9OmOBYeWmD-2GaLdO6-GDzy0KW8K0jplIDJnDZTMJOZLAPBlrIcLIKdmokhytZBW8XRbwZt3lHifJRlgKBU9xrzeBq0hNCHa3fjCqrys85x9fSYFdF9dh3uGr2QojnIjO3BIAWiIBeLAwRyN3h5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت یک صهیونیست: دیروز با یک ایرانی برخورد کردم که او مرا در آغوش گرفت و از من و کشورم تشکر کرد که کشورش را بمباران کردیم
🔹
این‌ها احمق‌ترین و ذلیل‌ترین مردم جهان هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/683759" target="_blank">📅 21:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683758">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c314e76d17.mp4?token=knL9Mw2zfaKcGxRpEkeC823RWYFjdhHUBwWRSRjiLU2z6o50LCJECXSjqwD4K7jxSPbNCcflzH_yrdZNKGAuGiD46qlE56R93V6TYlyhHWzJfj96xqTAOnWoBN7Oc3Fu_RDjh1RlYrKagoLLIOAtuPdMZvsZ1pyiPe5rcg462MRvGwex5-PtJdzItV8TJzOj9neM0khXKL1R0wObj1WfPlk0kN0u18iCaJ_QysyZ2X24IDVPZM2LFs7i6WhEDFN3IQS4NcThD0M4sKg-PxgiKSzJO3nbaEFUrNrWJQjqLYrjpZXaCAwe85uW8gnrxp6Qd7z6ZyXQBG7ons8Gvtn6Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c314e76d17.mp4?token=knL9Mw2zfaKcGxRpEkeC823RWYFjdhHUBwWRSRjiLU2z6o50LCJECXSjqwD4K7jxSPbNCcflzH_yrdZNKGAuGiD46qlE56R93V6TYlyhHWzJfj96xqTAOnWoBN7Oc3Fu_RDjh1RlYrKagoLLIOAtuPdMZvsZ1pyiPe5rcg462MRvGwex5-PtJdzItV8TJzOj9neM0khXKL1R0wObj1WfPlk0kN0u18iCaJ_QysyZ2X24IDVPZM2LFs7i6WhEDFN3IQS4NcThD0M4sKg-PxgiKSzJO3nbaEFUrNrWJQjqLYrjpZXaCAwe85uW8gnrxp6Qd7z6ZyXQBG7ons8Gvtn6Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای قطع کالابرگ به خاطر سکونت در خارج از کشور ‌چه بود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/683758" target="_blank">📅 21:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683757">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
جزئیات پاداش ۵ میلیاردی ارتش برای کشتن یا اسارت نیروهای آمریکایی   سرتیپ اکرمی‌نیا، سخنگوی ارتش:
🔹
هر فردی از نیروهای مسلح یا  مردم عزیزمان که دارای سلاح شکاری مجاز هستند، در صورت تجاوز زمینی نیروهای آمریکایی به خاک کشورمان، متجاوزان را به هلاکت برسانند…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/683757" target="_blank">📅 21:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683756">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اتفاق غیرمنتظره؛ ۹۵ درصد اوراق بدهی دولت فروش رفت
🔹
در آخرین حراج اوراق بدهی دولتی ۹۵ درصد از ۶۲ هزار میلیارد تومان اوراق عرضه‌شده به فروش رسید.
🔹
اتفاق مهم‌تر اما اضافه‌شدن ردیف «معامله‌گران اولیه» و ثبت نرخ بازده آنها در چارچوب قرارداد بود. به نظر می‌رسد دولت با این سازوکار توانسته جذابیت خرید اوراق را برای خریداران بزرگ افزایش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/683756" target="_blank">📅 21:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683755">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfIGBa5FvQZBHbaHZI9n0O4WXGiPSp_r_76g_yDCOMhFGfJnPq05KLNv64GNzeX_8j78qK7ePi4adsI6-syuTE5mLL-AaKrPfJ1sPXFEdELE7md85P1YfJIBipNIe9FCgU_O15TmRHSnViCzGv7xA7vPhUVBzhvITFQmamlWS35vCHvZTwxQtHlJh8m-D4GM28mrAci504IRl_-aLoZP_M7LfSLUPDYWFNykuU0fuajUjsi18XI3AU1u0go32fHRQKNTMdcLCa8heHkdPYA33z7vdLMeaWZ6KatA7VPfSCzZObJ5d9kVeKNXP3tmmjCeiWbvZVO6vplSH-QKhXbsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار کانادایی: شما به یک پدوفیل اعتماد نمی‌کنید که از بچه‌هاتون مراقبت کنه ولی اعتماد می‌کنید آمریکا رو اداره کنه؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/683755" target="_blank">📅 21:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683754">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ژنرال آمریکایی: باید با ۱۵ پایگاه نظامی خود در خاورمیانه خداحافظی کنیم
مک‌کافر، ژنرال بازنشستۀ آمریکا:
🔹
به نظر من ارتش آمریکا دسترسی به ۱۵ پایگاه نظامی خود در خلیج فارس را برای همیشه از دست داده‌ است.
🔹
چند روز پیش نیز واشنگتن‌پست به نقل از منابع آگاه خبر داده بود که پنتاگون به‌دنبال کاهش حضور نظامی در خلیج فارس پس‌از جنگ است و دلیل آن حجم بالای خسارت‌های واردشده از طرف ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/683754" target="_blank">📅 21:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683753">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKlJz-YjaqY_AII4OeZ0jw9fY_FZvOHY7RQXmzJMfOQln65cNLTLuiS4xekBd1_C1aBU4jbZ9FaWzLB7-pdqtzhEzTbtN2_sL2eCJi6xm98CKh2YQJ2LGdO4kYzr_YIUCNCEH8vojG7vYX4qvRmhq6xAclIEWyiR-5zh4c3SVAt-k7UvNer1TgJs76AebrcrtYAUy0yzsWx6nQs0xN5GD3II4MztxqSMHSGPCcBSW0FNkPSdUN0UxO7IRGgVYnfLh-EucK9aU6GFzJAo2IAdXx6tvA1q9UZ5zCE4J8I1lFO3fjkLU1iiIoHBf9ahM-LXnacl8TydkBBDkUSheV2oIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری قدیمی از محسن رضایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/683753" target="_blank">📅 21:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683752">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859c55ee57.mp4?token=GwgSRd8xYCVdJXHLtBwRKZBkK0LkTVF_5s_Oiuv0w7jcim9vm4GL4EkkZoxsKqQfjEIhetpWq3d49FSuZy46Dc6pvwqh2gouJgu9KeqctFDSZRjNrZQbw9rh7WLC2Uat30a1Q4DhQDp9BVookH6ISuUxXzZiqqSPrc16HfFOg0cBcS57u7CEdBLVjniiIk_O68703lOJlMAQyCtn0g6S5Pzg0VKY0ojPA-QqJ5fBS4EkstFRC2hiKhKA7_Ft7d7XbO7wMkHncLPZB6Tx5IXV3lL6gdZKXltHjVnfKlqi6MNaygz8uS-w77Nx1k-quw1zK71iIAyRJEbprICIBeu5lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859c55ee57.mp4?token=GwgSRd8xYCVdJXHLtBwRKZBkK0LkTVF_5s_Oiuv0w7jcim9vm4GL4EkkZoxsKqQfjEIhetpWq3d49FSuZy46Dc6pvwqh2gouJgu9KeqctFDSZRjNrZQbw9rh7WLC2Uat30a1Q4DhQDp9BVookH6ISuUxXzZiqqSPrc16HfFOg0cBcS57u7CEdBLVjniiIk_O68703lOJlMAQyCtn0g6S5Pzg0VKY0ojPA-QqJ5fBS4EkstFRC2hiKhKA7_Ft7d7XbO7wMkHncLPZB6Tx5IXV3lL6gdZKXltHjVnfKlqi6MNaygz8uS-w77Nx1k-quw1zK71iIAyRJEbprICIBeu5lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«تروریستِ اره‌برقی‌به‌دست» به سزای اعمالش رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/683752" target="_blank">📅 21:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683751">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc49270824.mp4?token=sgh1puHztDdkmeZP43KRxenbXTGBboAW0PEq-R9h6HHROqE2OGckyVxLOY0kDtHu2sAdrYjmiSgaY3NyBj-zfXyzDRZfpAO4toJ3yQVaTjWdEbVW6O_aCf6RKeFwfZ0ycPS0cfbYCdezcEgteVUuiqx9rogvNWpoSM0j3FUfqD9m9Umu6MknVAkmszwhPoTFYfO8zbHBZbQLQlGF6ngaTFYBRFzerQ2HJdAd2Ys7xaGdJZG0aTwRq-X8gn0t0vS6roP64GF4DweIICPVv46HqxsNXxmBl-A5LX1BTh_-JtYeG3XS2u0ztYD6xFa3M8Bj5eJ3OOjeaDzpjm4fDfSAfKsyNAHnxYCejE_coIPxnYzHMYCD8buEgTNL4Y7Z6SGdI2vsLKBKbI1QmmZJbMCt2E9GJdy2z71ALMiSE7w0WgvLeT38Y6M00GDM6oSu2xxTFoQ5bfyfKfRIwI5VO4S2261uJJKIBV8sen35-mOhuwqnLvXfDuHRzQRoZVNrbrwE_xyvTbG7KT_Jjy2dRVBnVxIDFaFPdEPoK4NtggwF695Qb7QFvr6IguzJ18bSEqikk3Q41rUumIsgq3NItE_FxTSdvZM_cRGtLiRYUdsv9ByLtQ4R9PnveGGM97RHnHFS_4s9qRAtJR17rjlikkupop8xMLyxeC95Jixbt3wc8qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc49270824.mp4?token=sgh1puHztDdkmeZP43KRxenbXTGBboAW0PEq-R9h6HHROqE2OGckyVxLOY0kDtHu2sAdrYjmiSgaY3NyBj-zfXyzDRZfpAO4toJ3yQVaTjWdEbVW6O_aCf6RKeFwfZ0ycPS0cfbYCdezcEgteVUuiqx9rogvNWpoSM0j3FUfqD9m9Umu6MknVAkmszwhPoTFYfO8zbHBZbQLQlGF6ngaTFYBRFzerQ2HJdAd2Ys7xaGdJZG0aTwRq-X8gn0t0vS6roP64GF4DweIICPVv46HqxsNXxmBl-A5LX1BTh_-JtYeG3XS2u0ztYD6xFa3M8Bj5eJ3OOjeaDzpjm4fDfSAfKsyNAHnxYCejE_coIPxnYzHMYCD8buEgTNL4Y7Z6SGdI2vsLKBKbI1QmmZJbMCt2E9GJdy2z71ALMiSE7w0WgvLeT38Y6M00GDM6oSu2xxTFoQ5bfyfKfRIwI5VO4S2261uJJKIBV8sen35-mOhuwqnLvXfDuHRzQRoZVNrbrwE_xyvTbG7KT_Jjy2dRVBnVxIDFaFPdEPoK4NtggwF695Qb7QFvr6IguzJ18bSEqikk3Q41rUumIsgq3NItE_FxTSdvZM_cRGtLiRYUdsv9ByLtQ4R9PnveGGM97RHnHFS_4s9qRAtJR17rjlikkupop8xMLyxeC95Jixbt3wc8qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به داد هم برسیم!
🔹
گاهی فاصله‌ بین «یک مشکل موقت» و «یک فاجعه‌ واقعی»، فقط چند میلیون تومان است...
🔹
اما اگر یک محله تصمیم بگیرد نگذارد هیچ خانواده‌ای تنها بماند، چه اتفاقی می‌افتد؟
🔹
شاید چیزی که قرار است ببینید، فقط درباره پول نباشد...
🔹
حتماً این ویدئو را ببینید.
#چرخ_زندگی
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/683751" target="_blank">📅 21:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683750">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رئیس مجلس نمایندگان آمریکا به فاکس‌نیوز: به زودی وارد مرحله جدیدی از جنگ با ایران می‌شویم و به تلاش برای پایان دادن به آن ادامه خواهیم داد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/683750" target="_blank">📅 21:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683749">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQivj5fegw8l6vwdDJ4rDWiGTsN_DA9Tq-iBcO-L58rpKH3uOCBX_-AN7DwGIXpYULznVLaHl1bTCVdaqIbveOUJWjiCHJ9YS4ZdGo4abvEjWx0xlJYKPWCLOp9BMo5x59RLA6Vjvkf2zbrz5RJLpfFK9VrfNSFtnQRmeFF6GV4AilzDXlN9xEAovGmEQPeNbRoFH5GMwoVGciPEgc3q4xdzVYJBqGqzeImOAwP9QMiyPiJtcv3no_qINaFmavJYyzmZYcv8yAV4jE8eS76fsiuXHD-4vx6QsDVrfwvuYTMxH62T7k15PG003a6jkzQgkcEV8GHgJbh3dFQ10mCMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل دوم استقلال به سپاهان توسط قلی زاده
🔹
استقلال ۲ _ ۰ سپاهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/683749" target="_blank">📅 21:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683748">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رسانه هندی: آمریکا ۱۵ پایگاه مهم در خلیج‌فارس را از دست داد
تایمز آو ایندیا:
🔹
یک ژنرال چهارستاره بازنشسته ارتش آمریکا اعتراف کرده که جنگ با ایران ضربه‌ای جدی به حضور نظامی واشنگتن در خلیج‌فارس وارد کرده است.
🔹
به گفته بری مک‌کافری، آمریکا دسترسی به ۱۵ پایگاه منطقه‌ای را از دست داده و پنتاگون در حال بررسی انتقال بخشی از نیروها به غرب، از جمله عربستان، اردن و اسرائیل است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/683748" target="_blank">📅 21:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683747">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
رئیس مجلس نمایندگان آمریکا به فاکس‌نیوز: به زودی وارد مرحله جدیدی از جنگ با ایران می‌شویم و به تلاش برای پایان دادن به آن ادامه خواهیم داد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/683747" target="_blank">📅 21:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683745">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
آتلانتیک: از این پس، ایران قدرت برتر غرب آسیاست
🔹
نشریه آمریکایی با اشاره به شکست آمریکا و رژیم صهیونیستی در حملات به ایران گزارش داد که از این پس قدرت برتر و مسلط در غرب آسیا نه آمریکا و نه صهیونیست‌ها، بلکه ایران خواهد بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/683745" target="_blank">📅 21:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683744">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw_-ntlsZQ467Ev2k2bVhlTztr0m5xA7sy67YB51xml7bmUBfs9FH73vgWbK9wpH6xUF2OWCaPOyVCfrHZIyCQBM4HAiR4BPBE5oMJwLJPWizvYvb6fiVP-gSPbokhvEinQH2MdgJSTTZ6YKJzZiXj39z6aavTwwz2dPMaZx2gEWKbTfAE9hi0NJGTkChZ9jPndDHHvHxYD-lECkpnQePpYJUhunVbxGLPDtYyPPnef-srmFsJo9O_kbTJ95YB_XA_zK6mIl0N1qRctbn1XfetAqgpIGZDDh5hIUV0g_QSjMleTnlT_pbYC9_f53wc8vOfH4AvB-9v_fZS7qO9tytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلاهای پشتوانه صندوق رز ترنج کجا نگه‌داری می‌شود؟
🟢
طلای پشتوانه صندوق طلای رز ترنج در انبارهای مورد تأیید بورس کالا نگهداری می‌شود. پیش از ورود طلا به انبار، اصالت آن تحت نظارت بورس کالا بررسی و تایید می‌شود.
🟢
صندوق رز ترنج نیز دارایی خود را در همین گواهی‌های با پشتوانه سرمایه‌گذاری می‌کند و تنها در چارچوب مقررات امکان فروش واحدهای سرمایه‌گذاری را تا سقف تعیین شده دارد.
🟢
بنابراین هر واحد صندوق رز ترنج، متکی به دارایی واقعی، ثبت‌شده و قابل رهگیری در سازوکار رسمی بازار سرمایه است؛ بدون اینکه سرمایه‌گذار دغدغه‌ای بابت تشخیص اصالت، نگهداری یا امنیت فیزیکی طلا داشته باشد.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/683744" target="_blank">📅 21:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683743">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
وزیر نیرو: اگر روندها مثل همیشه باشد، همین هفته خاموشی ها تمام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/683743" target="_blank">📅 21:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683742">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b3ab7f19.mp4?token=vyQ0vvo8N4YyVyw-KHdyCUuZg0zpcogbeOi9uDz949b6j0zFi54sCof4yAsgzr-Y_2NsheqAfJlN5RJpB5AAVaykkVeJsKHaud5-ig3o2HnYaA7N7vRNEI9BZwkQDSfJ5zz_wgRVDEll86FKPkmqOFkIkUxk8R_jGy-Px3X3FYwl0OFhxDjfCZVxzL-fLucOmNo2K3Klk8-oGu1Qav20zbsQtTuCRLtLyWdV3AkHJD31LPzDAj1jhZFOTRNHqsIxITj1ROD5D8OgxUPXi-HXPy8pz8-4fVshTWTf7cqqRThJOOskRYVDGZz7wZAztE4hB4Ov2QRdV-024Fi4323uqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b3ab7f19.mp4?token=vyQ0vvo8N4YyVyw-KHdyCUuZg0zpcogbeOi9uDz949b6j0zFi54sCof4yAsgzr-Y_2NsheqAfJlN5RJpB5AAVaykkVeJsKHaud5-ig3o2HnYaA7N7vRNEI9BZwkQDSfJ5zz_wgRVDEll86FKPkmqOFkIkUxk8R_jGy-Px3X3FYwl0OFhxDjfCZVxzL-fLucOmNo2K3Klk8-oGu1Qav20zbsQtTuCRLtLyWdV3AkHJD31LPzDAj1jhZFOTRNHqsIxITj1ROD5D8OgxUPXi-HXPy8pz8-4fVshTWTf7cqqRThJOOskRYVDGZz7wZAztE4hB4Ov2QRdV-024Fi4323uqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوگاتی و C SEED از تلویزیون ۵۰۰ هزار دلاری Bugatti N1 رونمایی کردند؛ تبدیل به MicroLED ۱۳۷ اینچی تنها در ۴۵ ثانیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/683742" target="_blank">📅 21:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683741">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f081bdae0.mp4?token=ZfVVxiO55FAczbnblMzirPakeWrZ5nEk9JIZFAnIfHngdhMDFr1z156i1lxzuaYdKGRdMSAT4eeq_P4pD3IztE_hHIJj-cHlT2dVnPEKE_KClcQvqD1t-OXPMWklkTdxp1KbIqCGFnRufz9BJWSYBidTUEuBRksS7793Dq40x1BFdI_qFTVpUWVhfk2Rbij453yptYY_S2r8NHTOBbUEYVRuQEqxkB4BHLpuXjNezAMDPgFU6OnQZsRN0Gxo2fQjefu0rm_l3XXJe5a4o9VlcYiKxAAeMBnnbb4I_i5bx82Dn74C7MLx-jOSDodv_FvLHf6FNe8SSgIKY9vC6j_kgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f081bdae0.mp4?token=ZfVVxiO55FAczbnblMzirPakeWrZ5nEk9JIZFAnIfHngdhMDFr1z156i1lxzuaYdKGRdMSAT4eeq_P4pD3IztE_hHIJj-cHlT2dVnPEKE_KClcQvqD1t-OXPMWklkTdxp1KbIqCGFnRufz9BJWSYBidTUEuBRksS7793Dq40x1BFdI_qFTVpUWVhfk2Rbij453yptYY_S2r8NHTOBbUEYVRuQEqxkB4BHLpuXjNezAMDPgFU6OnQZsRN0Gxo2fQjefu0rm_l3XXJe5a4o9VlcYiKxAAeMBnnbb4I_i5bx82Dn74C7MLx-jOSDodv_FvLHf6FNe8SSgIKY9vC6j_kgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس بانک مرکزی: صبح تا شب داریم تامین ارز می‌کنیم و سیاست پولی اعمال می‌کنیم؛ به جوسازی‌هایی که درست می‌کنند خیلی توجه نکنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/683741" target="_blank">📅 21:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683740">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
شرایط نه جنگ، نه صلح به نفع کشور نیست / نباید از مذاکره دوری کنیم و هر جا منافع ملی ما اقتضا کند، باید مذاکره کنیم
رضا سپهوند، سخنگوی کمیسیون انرژی در
#گفتگو
با خبرفوری:
🔹
شرایط نه جنگ نه صلح به هیچ‌وجه به نفع کشور نیست و به اقتصاد و زیرساخت‌های انرژی ما آسیب می‌زند و بر مردم فشار وارد می‌کند.
🔹
باید کشور را از این وضعیت خارج کنیم. ادامه محاصره دریایی آمریکا صادرات نفت ما را مختل کرده و درآمدهای ارزی ما را تقریباً از بین برده است.
🔹
همان‌طور که ما در مقابل آمریکا خوب جنگیدیم، می‌توانیم خوب هم مذاکره کنیم. نباید از مذاکره دوری کنیم و هر جا منافع ملی ما اقتضا کند، باید مذاکره کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/683740" target="_blank">📅 21:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf2bZIxEIgi5jg4a_nes_TB6N-YKJcOwgR7aLMX3XRCFF2LIW446rNkG3YYQdxOFPlNHJt1Fvtegy8ZthiN9lqMDT8syOc-rIKcs7Y4AgURTpFpJJdt4gF8AH0Kh01gGEe0OXbFskvmZ5s_ORj4kK1Vpuc2T3cdC-xp7DFT4Jf2UPPDAKwBR4vAW99TrVpr_JrM4k-CeBwugUKhFOe8tGrvg5m9zKF1Lz5ZncBgfhE5l7kEZSBCZCB1cwDEdMIv0ZoIo_uIoQmoC1I2VvNH1y8S3FReeizJZ5O2lv4J7wKVHiSK7gcY4hU9tFFV0gWiYrM6zW7Q1uGAxlQIIP_ssZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZMBMM9xRK9NXFrD_RoG-CGAb8axP0gnGHEO7cXWa3Dv7SSAhMF9y89QnZimyEAWNJFOkLUcuK9F6m3n7FgCl5puY4g5HSb7iSGrPlafQnTTg59x4N4RC4tCrOjY73n0VWrnXdei2eROtE3J5Ia74dBmpAbUP2nPsmNU2sJ_UPxel-vCCADW4WEN__9wYwCVGfs9gs_Bf_4BiW4USPevk2rorvlTVIiL41693wTMRp50RxU5Dc4AmHib29wQnwlUz6icp_jpXZLpz2sc1lhOBJgcEpriqlQ1i54SoWZcwxsy101Qk9zdUZ-fJ74s2CRoqNpMsXhpzseY7cBq38j8wDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1DRiJDLz2Wzn77N_iB8awFpEQpMhBt5dU2tpSkhh2uIA9Q3DQ33ibA_OQav577BnAljU5hdJLBd7DyIhT78QioONkkIIraugaHUbShzboz469Q_z0PHb6uNzpBZ50kXxH98Thxc3MV6Wfq03NFvH3XjS5q-YMYPHkVSBILzvh9pdOizY_ACuN2PcxsLypsrkzXugUWKUQuVhJF1kTnbdWY2CgJGd_EiGx_2eFkNEPapkf0FgBjqykavGJOdGUpw8IIWKVfWvuK1w06LjwR59BJO_VncigIx7Klm497yjGWj6-cWcnrVtnpkFirHQ9w6ko1IdiQ-HejdYDKGtnAtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrnkSgiA4vJEgWmHWUs1U2XkLALA_vVr7sh_17fYKfZDn7SmmM7uEsxYnYkMnPwp5pjJPWvXAL5pNJ1AtXQe2iBx4I4UAjyqt48D4c17gV24eXsQVuEdZOsWWizHjEiiKDgpjvldb9cQPen9w4EecQpW8SSG1h28R11X0TBhPdCzWhYBlCK6SL1dKIL4rLREjTSU8-xwMypHWqHIEo946LHiP1FC2kzjsU51bV3bhtCRHmuzTUUGoiv-kPY8Giys_SZ-izqyI55CrXKFuNSbGGSqrxxTjv8BZM4GlMSnhdZMa0NkRuiMB3zL0JySgDY8CN4dDeLyIrzb-t1WJt4cog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3yQ093IGKjUY-iRtsuVKNq87_3fRLS_6ijbZ3f2E9TzNylh53gW1mAVQeTjRl3m9RF9msGFemyqnDP6oUSKk4EaO7kS5C0AFHr7O_w90NSUpv8K9AY3NNpjjQG4037mSBHCByF_yIA8tKzzCrLp6bERTZAFVocNmvZV4Ix2n_UKDUiKLTx8dKDq9ScBdkkDBUCH0NjZE3Ah4e61PJMtkbViupGHSh4B5P0EMzUgw_7YEDmlljBiTKT2xO3dc9Vt1PNU6G0UJTE_rnr0QTa7QdiIwPhcZah1Y0GblZhQ_wkBy2ttzUOAqyh1Plx4GMzx9stCkfqmDyXXrCMTpDCsbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تفاوت پرامپت بد، خوب و عالی فقط در چند جمله خلاصه می‌شه که می‌تونه خروجی شما رو متحول کنه
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/683735" target="_blank">📅 21:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
بلومبرگ: یمن نه‌تنها مسیر صادرات نفت عربستان از دریای سرخ را مختل کرده، بلکه مسیر جایگزین ریاض از بندر ینبع را نیز با مشکل مواجه کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/683734" target="_blank">📅 20:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74d1f2107.mp4?token=B9JKf4OtElV8fGxG6Cf-AJ8XUjBxo54c8dLmirSZEHeK9H7JI7JqvW1bFk1AChTjirS8ooFhd0nxzIQ8jvnBbG6vWSZ53_Ott-AoXBBbYiX_WyQS7TKzuj3cLBew2VjqhkpiBPikKGryiOJojMPzzNTZtjfGoi23cFqSQK2KqSbQHqyYlG4OcvLaKF1Sw2oHzL1lutASXkM7SQr5hCj5O20ysXGkvXdLjfbkCJyJ50nNKcU-tyurOIyUHUzBRrVXRBZ6EFFIXE_ouGGoTL1nWvzy5XhAbw34-smDcosgVdsg090uE2erGFVSh7nqO6E0zjyzf_NYdPzwZpOtFOV8Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74d1f2107.mp4?token=B9JKf4OtElV8fGxG6Cf-AJ8XUjBxo54c8dLmirSZEHeK9H7JI7JqvW1bFk1AChTjirS8ooFhd0nxzIQ8jvnBbG6vWSZ53_Ott-AoXBBbYiX_WyQS7TKzuj3cLBew2VjqhkpiBPikKGryiOJojMPzzNTZtjfGoi23cFqSQK2KqSbQHqyYlG4OcvLaKF1Sw2oHzL1lutASXkM7SQr5hCj5O20ysXGkvXdLjfbkCJyJ50nNKcU-tyurOIyUHUzBRrVXRBZ6EFFIXE_ouGGoTL1nWvzy5XhAbw34-smDcosgVdsg090uE2erGFVSh7nqO6E0zjyzf_NYdPzwZpOtFOV8Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال خبرنگار صداوسیما از وزرا: تا به حال توسط رئیس‌جمهور ویزیت شدید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/683733" target="_blank">📅 20:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683732">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c8219b57.mp4?token=uAzyADdj3p6C1kcpzkqi5KSXwaiFlHGug3xhW2HpuOcL10D2WXyyJitQmSFxPAqppS9veQ0xShZu7ZCuWerRXYqbnz4-Q2oqUUIVXkACoGQSKdXM9HlnfAb1Er30-suyc0OZRJymbKZ7e0ZVPw5zi8fBVIajFweIWm686uZeN_UQWSGfSDBhoyXUYAFOVxI3TGI7Kfz-kn_rZe4oVgAb5VhywI5oT__cMd3ney4T9dgE87ld5BxoFI4lc9OzYtPvIiep-iqIZuXQH6nJRAl6zXFpshx-ElpJPjNLGQuR64OnfHKOXT7tJ8XWoUoMtq9b-WNwyiMCNreYtciHFkRj0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c8219b57.mp4?token=uAzyADdj3p6C1kcpzkqi5KSXwaiFlHGug3xhW2HpuOcL10D2WXyyJitQmSFxPAqppS9veQ0xShZu7ZCuWerRXYqbnz4-Q2oqUUIVXkACoGQSKdXM9HlnfAb1Er30-suyc0OZRJymbKZ7e0ZVPw5zi8fBVIajFweIWm686uZeN_UQWSGfSDBhoyXUYAFOVxI3TGI7Kfz-kn_rZe4oVgAb5VhywI5oT__cMd3ney4T9dgE87ld5BxoFI4lc9OzYtPvIiep-iqIZuXQH6nJRAl6zXFpshx-ElpJPjNLGQuR64OnfHKOXT7tJ8XWoUoMtq9b-WNwyiMCNreYtciHFkRj0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان انرژی اتمی: شیوه‌های نوین درمان را در کشور برای استفادۀ همۀ مردم گسترش خواهیم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/683732" target="_blank">📅 20:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683731">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
نشریه نزدیک به کنگره آمریکا ادعاها درباره تنگه هرمز را رد کرد
🔹
نشریه هیل روز یکشنبه ادعای دونالد ترامپ و برخی رسانه‌ها درباره عبور گسترده نفت‌کش‌ها از تنگه هرمز را به چالش کشید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/683731" target="_blank">📅 20:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683730">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4a466bf4.mp4?token=JAV5LHg7q7WHivRcK_q8OeqGfArh20flmJZWZjsJcdM_C73JWBQWQT8la_TnlRKHIEpWi_ww6wcchrVuVWvo9CCDxuHKZnC97dFxAwzhJOTIAzaV23HW0-3w9q62sv-BIQ86icrKw0Sl1LAyK45-GviAY0dvog75xt2nbJ13MkF8UFttpDAVPMsbYL4-A2CUrWcAff-bgKyGFJK-1N3MN8UROyqhE26uyl55MGOfoCQJM5WLLC4C_QMDB32uaJzsG8n9cZRjOFxKjUC8oDEDXcOhRrGVrhJZQAkJsqp6GfsBHd-Nm6FNE-ghKMLJb-M6qd9znuWc6ECi6mSEdzZH-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4a466bf4.mp4?token=JAV5LHg7q7WHivRcK_q8OeqGfArh20flmJZWZjsJcdM_C73JWBQWQT8la_TnlRKHIEpWi_ww6wcchrVuVWvo9CCDxuHKZnC97dFxAwzhJOTIAzaV23HW0-3w9q62sv-BIQ86icrKw0Sl1LAyK45-GviAY0dvog75xt2nbJ13MkF8UFttpDAVPMsbYL4-A2CUrWcAff-bgKyGFJK-1N3MN8UROyqhE26uyl55MGOfoCQJM5WLLC4C_QMDB32uaJzsG8n9cZRjOFxKjUC8oDEDXcOhRrGVrhJZQAkJsqp6GfsBHd-Nm6FNE-ghKMLJb-M6qd9znuWc6ECi6mSEdzZH-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در منطقه صنعتی در بیت داگان در سرزمین‌های اشغالی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/683730" target="_blank">📅 20:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683729">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFBm6VzN6nX0WrG7DtFm8ttlTu8Fnm_ATZ--M4sbgHEc9eYwWZDoawCIAKOx3YNoFwz0efFMqD9ictAVYPwzcK_mhd_VomtX0Z6zq_w6_BCgRLHhny0MFn4degdC1rfSgvGDVHK-rRBD7MiERwHVCjZ1raSrpuY1IzHEX3njwquDb-7dzCz5RhC0ejgOT3cRPWOyLK7mZNwhe2BDuj7uW4Sl8Y1cMPIl45IJsptgIdfCTZ2fO0_94U_wMGnvYasXv2ec8kQaYi2k7tVdksPJW49Qdr16x_7xOOrnazQSQKb5Ksp-RxIsHm8XvelFdLVXjuiE4nue2Sav9LoKbtAy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دلار ۲۰۰ هزار تومانی و طلای ۲۲ میلیونی | تبدیل سرمایه مردم به کاه | از رهن خانه تا پس‌انداز خانوار؛ تورم چگونه دارایی مردم را می‌بلعد؟ | امروز چقدر فقیرتر شدیم؟
🔹
این گزارش باید از قیمت کنونی طلا، سکه و ارز آغاز شود اما نکته درست همینجاست؛ اینکه این قیمت‌ها در زمان نوشته شدن همین گزارش کوتاه تا زمان خوانده شدن احتمالی آن تغییر کرده است. چیزی که در این میان برای ما مردم عصبانی ثابت مانده یک گزاره تلخ است؛ تبدیل سرمایه مردم به کاه!
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239874</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/683729" target="_blank">📅 20:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683728">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
معاریو: احتمال درگیری اسرائیل و ترکیه وجود دارد؛ شمال قبرس می‌تواند به میدان رویارویی دو طرف تبدیل شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/683728" target="_blank">📅 20:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683727">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwSIXIiODb1M4ghjJSNvi-vQ62N2Rkt1Z9c-21oFfAw7Z54MnbHgfTB3xFH_7D6gIwSdAIG4xftaA6dl0dLqkd-ehhLFDG-85g7t6MOOIOjC308rNil7rn2Y5DQyA68XTSuHM-XqZ8gdMTkco68aEN0HNaSeJsOWh4IHs61mSp1IJauUFtoRYbZdULeKLNBUbjgKdKJ4xjQaOcAj7sxxSZsypcrUAOLLaBlb4t7qB_2gFOVWXfzhb0nwSBryCHCpXrpkiYtavJ4UBlyVDQ6kuxSlhB7vH1MnHj5CBUU1prFZf2nxw4deWOEho1PD9kwuppnBvjln_OR-PMthT9V7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درد دارو
🔹
گرانی دارو در سال ۱۴۰۵ وارد مرحله تازه‌ای شده و این‌بار دامنه افزایش قیمت، داروهای عمومی و پرمصرف را نیز دربر گرفته است؛ اقلامی که تا پیش از این بخش محدودی از هزینه‌های خانوار را به خود اختصاص می‌دادند. طبق اعلام سازمان غذا و دارو، میانگین افزایش رسمی قیمت دارو در سال جاری حدود ۴۸ درصد بوده و در برخی اقلام به ۶۰ درصد رسیده است. با این حال، بررسی قیمت تعدادی از داروهای پرمصرف نشان می‌دهد رشد واقعی قیمت در برخی موارد به بیش از ۱۰۰ درصد رسیده است. این شکاف قابل‌توجه میان افزایش رسمی و قیمت‌های بازار، هزینه‌های درمان را برای خانوارها سنگین‌تر کرده و دارو را به یکی از اقلام فزاینده سبد معیشت تبدیل کرده است.
🔹
هشتصدوچهل‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/683727" target="_blank">📅 20:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683726">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a42126f5e.mp4?token=nnt2wSAYHq0skjmokd1OMgISkj7774CgZ4ZG33THIYP5ESLJN1z04xcnI9bUyVebCkOyaFFz5WC7F0ZeGsLjKJlTU4R1VxDa7HSj-p-qvAgbm0alCJGOdQt617uaM2QIPWEoPE0JK3-EFO6zb2ZyM2VgNATIq3iFm-1yAqHhb81p5haBs2xWwm2gZ43kYcebHCZhnJAlfFT50Z-xCRJDC3qU_KxbItapYgAn3osLi_ejnqHYuJkSyfRXRN7GSB5ZAfy2EtUGPvDBqvAlznSaOfmVfdfPAB7Jm5ZZgPtsFkdqep4L9b-bAC_fRclPtaNopAGNzgAr6L0GNBUHCOzS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a42126f5e.mp4?token=nnt2wSAYHq0skjmokd1OMgISkj7774CgZ4ZG33THIYP5ESLJN1z04xcnI9bUyVebCkOyaFFz5WC7F0ZeGsLjKJlTU4R1VxDa7HSj-p-qvAgbm0alCJGOdQt617uaM2QIPWEoPE0JK3-EFO6zb2ZyM2VgNATIq3iFm-1yAqHhb81p5haBs2xWwm2gZ43kYcebHCZhnJAlfFT50Z-xCRJDC3qU_KxbItapYgAn3osLi_ejnqHYuJkSyfRXRN7GSB5ZAfy2EtUGPvDBqvAlznSaOfmVfdfPAB7Jm5ZZgPtsFkdqep4L9b-bAC_fRclPtaNopAGNzgAr6L0GNBUHCOzS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلیلی با فریاد یا امام رضا طلا گرفت
🔹
سینا خلیلی در وزن ۷۰ کیلوگرم رقابت‌های کشتی آزاد جوانان قهرمانی جهان، در دیدار پایانی مقابل کرمیوف از آذربایجان با نتیجه ۷ بر ۳ به پیروزی رسید و صاحب مدال طلای جهان شد.
🔹
این کشتی‌گیر پس از کسب مدال طلا نام امام رضا(ع) را فریاد زد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/683726" target="_blank">📅 20:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683725">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0bb69875.mp4?token=so7knFLJiCfuoIUNNjasVy8T5GMoCDsa3WCwkncZfT5tKt_YYq-4eF28JzjUuuazEqV-2g75qe1tv10S32GG0J3b7RVhIN_5nKdU75EOycccMNbvad8PAwKScrdTO5ZMfLawjR__LzJkvnQx3wn6HhOJiuIqNRNbTJ-x1osxs3dH9apfemoA3dUyR3MkWSw748Xu3x_pAJ75IVjCzvKEMbXWbq_0i4NAB-jYOirhPNraa7Je0yyK5K9XZLdtzg0WKsETqI_EW6nC3Er7LKLd0BQwCxzEDjbg_tPtg4YCZwkOo1hlDl1WKdYZIvjkKeFAQuQ3l-kkmSYmn6zIi7rUNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0bb69875.mp4?token=so7knFLJiCfuoIUNNjasVy8T5GMoCDsa3WCwkncZfT5tKt_YYq-4eF28JzjUuuazEqV-2g75qe1tv10S32GG0J3b7RVhIN_5nKdU75EOycccMNbvad8PAwKScrdTO5ZMfLawjR__LzJkvnQx3wn6HhOJiuIqNRNbTJ-x1osxs3dH9apfemoA3dUyR3MkWSw748Xu3x_pAJ75IVjCzvKEMbXWbq_0i4NAB-jYOirhPNraa7Je0yyK5K9XZLdtzg0WKsETqI_EW6nC3Er7LKLd0BQwCxzEDjbg_tPtg4YCZwkOo1hlDl1WKdYZIvjkKeFAQuQ3l-kkmSYmn6zIi7rUNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نایب‌رئیس مجلس: ما در قانون گفتیم که بازنشستگان باید ۹۰ درصد حقوق شاغلین را دریافت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/683725" target="_blank">📅 20:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683724">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت: جهاد اقتصادی باید بازتعریف شود
عباس مقتدایی،نایب رئیس اول کمیسیون امنیت ملی و سیاست خارجی مجلس در
#گفتگو
با خبرفوری:
🔹
قیام اقتصادی ملت برای حراست از فضای کسب‌وکار، تولید و عرصه خلق ثروت، یک ضرورت عینی است. همچنین می‌بایست مقامات دولتی، نهادهای قانون‌گذاری و همه بخش‌هایی که می‌توانند، در این زمینه ایفای نقش کنند.
🔹
در این مقطع زمانی، جهاد اقتصادی باید بازتعریف شود تا معیشت خانوارها را دگرگون سازد و  از مرحله بیان به مرحله عملیات برسد و زمان‌بندی آن محقق شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/683724" target="_blank">📅 20:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683723">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW7wm1hmhZyT33OJrtVNq5FUncOc_WvvFNrvvQ7nDhlYi8DlYly7wA-ai5ZbhjohKDACZ8FrvY1dM_5734gBL8FwNA4RXYi_PxYsh6KmwAvt3B-xE8UiGqdbKYsf9zRQ3zrdWOcmkgLLJ945tmL3K-vR7YE3SXHIURyoW2JUl3XBJpZUCRalDMzYUa3S0cbk-kM1gd88aSCfJS-_VAwNgfkauHXWXM-oiXdEH4Ts_tMKskvAdktK3Mr56ArWQImboxCl4R-xG4stxZSomxNxrgHYyaPSKvT3btufeL_SFCJqV5dCbgXZ_Tmw0KEuduwdXY4qkd4E7xhzk1rUBfkqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جلسه اضطراری نتانیاهو برای مقابله با بادبادک‌های غزه
🔹
دفتر نخست‌وزیر رژیم صهیونیستی از برگزاری نشست فوری با حضور نتانیاهو و وزیر جنگ این رژیم برای بررسی تهدیدهای ناشی از پرتاب بادبادک‌ها و بالون‌های آتش‌زا از نوار غزه خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/683723" target="_blank">📅 20:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683722">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">02 Ane Manaee (1403-07-19) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/683722" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه دوم
حجت‌الاسلام امینی‌خواه:
🔹
روانشناسی باور؛ تقابل عمیق بین مؤمن و کافر [01:45]
🔹
دسیسه‌های شیطانی: شانتاژ و تخریب مسیر ایمان [02:55]
🔹
قرآن، کتاب زندگی یا کتاب مراسم؟ [08:00]
🔹
تماشاچیان عاشورا؛ بازیگرانی خاموش [19:00]
🔹
حضرت حمزه و درس‌های بزرگی از غیرت و تعصبِ به‌جا [25:28]
🔹
وقتی پیامبر (صل‌الله‌علیه‌وآله) کوتاه آمد ولی امیرالمؤمنین(علیه‌السلام) کوتاه نیامد... [26:45]
🔹
تکرار تاریخ؛ از سکوت مرگبار جامعه تا فریاد‌های رسای حضرت زهرا (سلام‌الله‌علیها) [36:50]
🔹
۱۲ قرن تنهایی و مراقبت از دشمن؛ روضه‌ای که با زندگی سید حسن نصرالله دوباره خوانده شد [44:56]
🔹
چقدر باید ظلم کنند تا بیدار شویم؟ [51:50]
🔹
پاسخی از جنس شعر، کرامت رضوی در کلام صائب تبریزی  [55:20]
🔹
رهبر معظم انقلاب؛ دلی که با یقین می‌تپد [59:58]
🔹
توبه جناب حر؛ امید در تاریک‌ترین لحظات [01:017:00]
🔹
معجزه‌ای از کربلا؛ بدن سالم جناب حر پس از قرن‌ها [01:23:43]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/683722" target="_blank">📅 20:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683721">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c153e7d278.mp4?token=v3vpsmKog4KHtv93eTDkQ78WAzZVOSX0JYB2A2DSLRu-szAHZ4TdcaVrN5ZlFS3hGzj9e-3SwJSuCTcSJ_Nc6S6McUSMos7ZLP0lb-I_4EsSRYqmvaQHgGNOiqf4db62D2uwpCfWaKeKUASg9i9Tvwx0Spw0SD1pdk96TH0HSx2LCZa7HwtACYnhWgiVRA8PK2cBRgO2EuTbOgWoNacHNKG2JoFBY5zBYjIjcfiN-HYA7mZ2UTFISPoS8bj149LcHgY9L1IjNkWZDatLSGS5207ICyO8UHrjRRMVdtleSoQLAdWQ_c-w7uNFYPfjoQ5qlT4SlJN9oatE01lv-K77IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c153e7d278.mp4?token=v3vpsmKog4KHtv93eTDkQ78WAzZVOSX0JYB2A2DSLRu-szAHZ4TdcaVrN5ZlFS3hGzj9e-3SwJSuCTcSJ_Nc6S6McUSMos7ZLP0lb-I_4EsSRYqmvaQHgGNOiqf4db62D2uwpCfWaKeKUASg9i9Tvwx0Spw0SD1pdk96TH0HSx2LCZa7HwtACYnhWgiVRA8PK2cBRgO2EuTbOgWoNacHNKG2JoFBY5zBYjIjcfiN-HYA7mZ2UTFISPoS8bj149LcHgY9L1IjNkWZDatLSGS5207ICyO8UHrjRRMVdtleSoQLAdWQ_c-w7uNFYPfjoQ5qlT4SlJN9oatE01lv-K77IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند ترفند ساده، اتوی بخارت‌ رو مثل روز اول تمیز و آماده استفاده نگه دار! #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/683721" target="_blank">📅 20:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683720">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: ۴ روز بعد از آغاز جنگ، جلسۀ دولت تشکیل شد، آقای عراقچی در جلسه گفت ممکن است دشمن اینجا را بزند، رئیس‌جهور گفت به درک که می‌زند. من جلسات را تعطیل کنم از ترس اینکه او می‌زند؟ خُب بزند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/683720" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683719">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2781b49bbf.mp4?token=MtyhS_tjR2ED2Y_ee9Zy6tfZ5ct7S_1msayDeTMm08YQwmt3F9ktpStmStCUmzClYm5Et36gFoOSuBkPQZFhJD4RmRJVPXU-KW_hojR3lvV-xkiuF_J7mKgn9vo1w3nTA-zvS5QFqstJLwl1FZm_45i2Pwcna3BCGq7-ZR98wlOiQGg_Np1ZKYBKHeldEzgfdkO484sbKJ_F8_6Vzw_4a_8dwMVK1z2PMfywy9GnEG7O7mZTjB-mL0FW4SRnSXrmp74k5ZT8zsBiDOsxQObyRYCC0ZM-q2hxK2UkPrCGiX3bZDb68tvEAncu09BLg9dlNwGmF2L695uXtepdVqS0Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2781b49bbf.mp4?token=MtyhS_tjR2ED2Y_ee9Zy6tfZ5ct7S_1msayDeTMm08YQwmt3F9ktpStmStCUmzClYm5Et36gFoOSuBkPQZFhJD4RmRJVPXU-KW_hojR3lvV-xkiuF_J7mKgn9vo1w3nTA-zvS5QFqstJLwl1FZm_45i2Pwcna3BCGq7-ZR98wlOiQGg_Np1ZKYBKHeldEzgfdkO484sbKJ_F8_6Vzw_4a_8dwMVK1z2PMfywy9GnEG7O7mZTjB-mL0FW4SRnSXrmp74k5ZT8zsBiDOsxQObyRYCC0ZM-q2hxK2UkPrCGiX3bZDb68tvEAncu09BLg9dlNwGmF2L695uXtepdVqS0Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقاب اصفهانی: بخشی از مصرف بالای بنزین به خاطر کیفیت خودرو است  رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی:
🔹
با اینکه کیفیت برخی تجهیزات پایین است اما تغییر رفتار، زودتر از اصلاح تجهیزات و اقدامات دیگر قابل انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/683719" target="_blank">📅 19:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683718">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08c8d12a6.mp4?token=MclD0lcZNoLJ-YDHfTGoL91OOS3Mb_UVRQmTynUPeNuDi9mLxXRGDarJg7ffiJuoBhM4m7aPpWNF2WbVIC3nwckui6LUg5VGisInzXue6ZPuI3JjzdgqMVC4e5a14oqVMUI0PDzHPMvMTgCXs9-DQSufXZnSefD4FIDTWHFAVhY5fY_emeCCjMVJTIYa2GKIHjErg6bnzOW1Cv8Npo4ctWVZmwoH4LA5gpoMBkxThokfy7L9wg4rpoQiBiB3W-iW5ZeGREDh1E75UbiAun55ZTnmDuaBiwEpSnYjDKF8Q2pEfm5ZJlJp4JVIrLqENalJKRPWcc-HHR15YR9to7NLlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08c8d12a6.mp4?token=MclD0lcZNoLJ-YDHfTGoL91OOS3Mb_UVRQmTynUPeNuDi9mLxXRGDarJg7ffiJuoBhM4m7aPpWNF2WbVIC3nwckui6LUg5VGisInzXue6ZPuI3JjzdgqMVC4e5a14oqVMUI0PDzHPMvMTgCXs9-DQSufXZnSefD4FIDTWHFAVhY5fY_emeCCjMVJTIYa2GKIHjErg6bnzOW1Cv8Npo4ctWVZmwoH4LA5gpoMBkxThokfy7L9wg4rpoQiBiB3W-iW5ZeGREDh1E75UbiAun55ZTnmDuaBiwEpSnYjDKF8Q2pEfm5ZJlJp4JVIrLqENalJKRPWcc-HHR15YR9to7NLlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: در ایام جنگ به رئیس‌جمهور گفتم حاضرید باهم برویم پای لانچر؟ او گفت برویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/683718" target="_blank">📅 19:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683717">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cb82fdaa.mp4?token=E5Syvsrgu0fOBg3hM5x5VdmuUCdZFJrC_t-JkkBwMlsp18Xp92DtK3ruk2lsV0jf0rngy3QUIzfzxva84KSCb7C7lZlhVEEZQw_9MFy920zffi4JAS14c_Bk6kTNcIX_hQOK0pIUOvLEVgXIXXerJ5KFjsSYIBKJVab3RRPUCupIACxyeZ6-K5H1jQ3sm8SAprjUxHM4o7jtCcz3ApqCNfR4UbtgHsC9Q08yZUyNeL-M1Z8AZoKp7w66xMFLjgRv8wBWueVw8zKP7gKdXeL6E4ifUn5gFGk1L62ca021vxAEiPpZbk3NbTiO_RVuy-bQxEHQNtbSejffeFD9ZdLLVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cb82fdaa.mp4?token=E5Syvsrgu0fOBg3hM5x5VdmuUCdZFJrC_t-JkkBwMlsp18Xp92DtK3ruk2lsV0jf0rngy3QUIzfzxva84KSCb7C7lZlhVEEZQw_9MFy920zffi4JAS14c_Bk6kTNcIX_hQOK0pIUOvLEVgXIXXerJ5KFjsSYIBKJVab3RRPUCupIACxyeZ6-K5H1jQ3sm8SAprjUxHM4o7jtCcz3ApqCNfR4UbtgHsC9Q08yZUyNeL-M1Z8AZoKp7w66xMFLjgRv8wBWueVw8zKP7gKdXeL6E4ifUn5gFGk1L62ca021vxAEiPpZbk3NbTiO_RVuy-bQxEHQNtbSejffeFD9ZdLLVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: به رئیس‌جمهور گفتم باید کارهایی کنیم که در کوتاه‌مدت فحش بخوریم اما در بلندمدت از ما تشکر شود
🔹
آقای پزشکیان به من گفتند حتما این‌کار را بکن زیرا ما باید مسائل را حل کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/683717" target="_blank">📅 19:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683716">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=EyzWCJmvuZLL5BrDuG6_BZOgeiOdJtvg7Z7KQkT44-ius0ctibhFYsGLnS8qXb6nc1VzhTGQOu9a83_LxJbNtWKpn4MwLHCj2JfJvJhS2HuRfU-cTuDf5YbtFf2ZiHyI49fYRkP9BpF7otlE90_exvm2P0xPkEI2FYv0HiJJ7n6UiqyzgQc1YAFH2vV2gjYAzvAP86vDKr8234Qz_K7hQApFJqWABeTfXUEBEX_xUFw0f8u7LjLtxtNklwaxYSkZ5jeyIlpwniTobce287iHjJOM7YfiBAq-qtcrX0CtApK9VkkP30bClqs9rAbybRGHB1dg73S1UiMYW5T1ZlQZRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96dbefcd54.mp4?token=EyzWCJmvuZLL5BrDuG6_BZOgeiOdJtvg7Z7KQkT44-ius0ctibhFYsGLnS8qXb6nc1VzhTGQOu9a83_LxJbNtWKpn4MwLHCj2JfJvJhS2HuRfU-cTuDf5YbtFf2ZiHyI49fYRkP9BpF7otlE90_exvm2P0xPkEI2FYv0HiJJ7n6UiqyzgQc1YAFH2vV2gjYAzvAP86vDKr8234Qz_K7hQApFJqWABeTfXUEBEX_xUFw0f8u7LjLtxtNklwaxYSkZ5jeyIlpwniTobce287iHjJOM7YfiBAq-qtcrX0CtApK9VkkP30bClqs9rAbybRGHB1dg73S1UiMYW5T1ZlQZRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان بهینه‌سازی: به رئیس‌جمهور گفتم باید کارهایی کنیم که در کوتاه‌مدت فحش بخوریم اما در بلندمدت از ما تشکر شود
🔹
آقای پزشکیان به من گفتند حتما این‌کار را بکن زیرا ما باید مسائل را حل کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/683716" target="_blank">📅 19:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683715">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534e133ebb.mp4?token=GsQbQiH1G1GQp04bL2Rykj_skGCwXf50GnFKF3see7a4KfNfPPt3uklNuB-09J4dLWDx7HZOxrw25SYNo9nwmLuBCMqDb8pKt7zOYpUJTZvDuonWUZEzCWr7YZS7bXOgdJkWi9gu5_ruS64REpn_HAL0C7B8O3qPPfvQksTWEUezA6e2u03ECARmCS4H7pIRupyghp-ZdTe-d3_SJHEAPX8dOwR3MedNiLdSSZmJWeB2QN7rpuuGUu5bpIArnD1X0mB_HIYCJbAEzLfRxAv3rJk1ulTJzZA_AauW5Qy2fgJ41C2aDyv8QltXgWyI5xfDmpaGrR0cxUw_UoiuJ9Pv6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534e133ebb.mp4?token=GsQbQiH1G1GQp04bL2Rykj_skGCwXf50GnFKF3see7a4KfNfPPt3uklNuB-09J4dLWDx7HZOxrw25SYNo9nwmLuBCMqDb8pKt7zOYpUJTZvDuonWUZEzCWr7YZS7bXOgdJkWi9gu5_ruS64REpn_HAL0C7B8O3qPPfvQksTWEUezA6e2u03ECARmCS4H7pIRupyghp-ZdTe-d3_SJHEAPX8dOwR3MedNiLdSSZmJWeB2QN7rpuuGUu5bpIArnD1X0mB_HIYCJbAEzLfRxAv3rJk1ulTJzZA_AauW5Qy2fgJ41C2aDyv8QltXgWyI5xfDmpaGrR0cxUw_UoiuJ9Pv6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد ضدصهیونیستی در آرژانتین، معترضان پایان «نسل‌کشی» رژیم اشغالگر در غزه را خواستار شدند
🔹
صدها تن از شهروندان آرژانتینی با برگزاری راهپیمایی گسترده، سیاست‌های جنایتکارانه رژیم صهیونیستی در نوار غزه را به‌شدت محکوم کرده و توقف فوری ماشین کشتار این رژیم را فریاد زدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/683715" target="_blank">📅 19:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683714">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پزشکیان: صرفه‌جویی مصرف بنزین باید از دولتی‌ها شروع شود
رئیس‌جمهور در جلسه هیئت دولت:
🔹
برنامه‌ریزی کنید که چگونه می‌شود ماشین‌های دولتی و مصرف دستگاه‌های دولتی را کاهش داد و میزان ترددهای ماشین‌ها را پایین آورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/683714" target="_blank">📅 19:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683713">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12fbb21d0.mp4?token=LN90fthTBiSW3gbcrLr2cXD4mBskgR6qdP-kYtD7W3kQVBH7BAw5OMmhnEF9vOTeJRdxBLVK4CyEaHVaECUSRYnEljGK1jJi21o_HKnzSe1uobH1HPgorPHXoNx9QlUPZ2tuqeDwAda9J9U3ZzJGQUFWfb1LW4z0S5VQ7yyjfgwoRWhF8JXviTQ1UgCpSerb5YmeEA2zx7YqJskNVQ2jKjmq1j0nsYSw6Cd2i7cOE0-dyhxbUBtEZdJ5jG3rZE7QJrrssUPV9M8nyO4J78UaVRvMX0VRp72FVV8K3ruD0DxEBQm8dxr88jmG7rvwrK4l6TpUCV-y0pvtCo3qthYjnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12fbb21d0.mp4?token=LN90fthTBiSW3gbcrLr2cXD4mBskgR6qdP-kYtD7W3kQVBH7BAw5OMmhnEF9vOTeJRdxBLVK4CyEaHVaECUSRYnEljGK1jJi21o_HKnzSe1uobH1HPgorPHXoNx9QlUPZ2tuqeDwAda9J9U3ZzJGQUFWfb1LW4z0S5VQ7yyjfgwoRWhF8JXviTQ1UgCpSerb5YmeEA2zx7YqJskNVQ2jKjmq1j0nsYSw6Cd2i7cOE0-dyhxbUBtEZdJ5jG3rZE7QJrrssUPV9M8nyO4J78UaVRvMX0VRp72FVV8K3ruD0DxEBQm8dxr88jmG7rvwrK4l6TpUCV-y0pvtCo3qthYjnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به سپاهان توسط یاسر آسانی   استقلال ۱ _ ۰ سپاهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/683713" target="_blank">📅 19:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683712">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رسانه صهیونیستی: همه جای جهان اسرائیلی‌ها را کودک‌کش می‌خوانند
🔹
کانال ۱۴ تلویزیون اسرائیل اعتراف کرد، حتی در دور افتاده ترین نقاط هم صهیونیست‌ها را کودک‌کش لقب می دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/683712" target="_blank">📅 19:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683711">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhGaOTgg72hVrf6USvnVQR2JdrFr4b5QxQMcYAGdOleeVExtpfDBx2ey7ZgINg_WnFYRoxInlbSq30j3Ap5qVWuVdmYY0kcP-JtqxmMj08QT-RaNHh2mrVJh49G1IMA6LHeztAx3179Q56VGAP-FQZsFGhRC9-XjhYnunA7E-6LBY2v3yRwo0lEveSP6V70QyDbATbjrk-vPJ1wwFRzxeqo4aWD4xIkUtd63TnYuGuMmXOgeXvcoDpZmZhxZBG_cofrUKaNmcqBqfOZX2EoyN9cGA3yuWCh0Xi2gL08yzPqOX-Msl6nZKBmJYRpfiAuyzkAS0hjRjmaGqHJu_GAFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گسترش فرصت‌های سرمایه‌گذاری در وال‌گلد؛ نقره به میدان آمد!
💎
تنوع، کلید موفقیت در بازارهای مالی است. پلتفرم «وال‌گلد» در گام جدید خود این امکان را فراهم کرده است تا کاربران بتوانند در کنار طلا، روی «نقره» هم سرمایه‌گذاری کنند.
🔸
روند یک سال اخیر نشان می‌دهد نقره بازدهی‌های چشمگیری در بازار سرمایه داشته است.
🔸
با این امکان جدید، سرمایه‌گذاران می‌توانند با ترکیب طلا و نقره، یک سبد مطمئن‌تر، کلاسیک و پربازده بسازند.
ورود به بازار جذاب نقره
ورود به بازار جذاب نقره</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/683711" target="_blank">📅 19:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683709">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96b95162d0.mp4?token=PwvRP6hIMyjPXbrFd8IcwyMhI58MLgbPrD0KTDUORDBrKz1TwxUQYB8EmxYTuQXSZoHMCI05aTbwZ0KO5kPUanVWM6T1XDszhly0wkyWBlVhlAgO8SwtoYniveKlvCQnXvb7Pn5TkpQXj8P64FfSxfYhcnzAitugi9N6_zh8yWe85Ag7vduQg_sbNERG0rMo1ui_cG-hWNA_lsSdDCdrRjs5LPfuKiLtVjj66jMtjbCvXnmKaVUS8wcaWk3AX2IN6lk7kJBr4NdC2PtpCPsPKl6GnCuw22t_CndD22xvbUac5OBECQxaEjjKvBkcSaSLEpGHddL-QkkMGDSqKuw_WUX-h6osgBjor7ZkysoXBwtvQZ8ezG2xg76bdmSv-Yyda9jxUtxYAxUD8bw_MeQW8LRF2c69FZOSXGOqJffh94msIb-nMrgDdfvnoFtReYCTKFy7pj_mOxHs3nQ80RQaVDHhJ00fqGlbBgVsoGLG50-k0QoWDBuLf3ORFJtGAFSYqdSkKd4MYGm_8sqovTatKHhMThLNmAxmtDJmomD27jW_RoRn2jZNk9f1Pr86qzcy1R-kUg0uPZoiOexxP2N0G9gavIzTvDybsM6lhJuAIlvr0l7kP3p1tmvnmJSFAeRLN_8xZDaJiugsrBUn8w2HxO2FOQFwRyBBsn_rHYccRuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96b95162d0.mp4?token=PwvRP6hIMyjPXbrFd8IcwyMhI58MLgbPrD0KTDUORDBrKz1TwxUQYB8EmxYTuQXSZoHMCI05aTbwZ0KO5kPUanVWM6T1XDszhly0wkyWBlVhlAgO8SwtoYniveKlvCQnXvb7Pn5TkpQXj8P64FfSxfYhcnzAitugi9N6_zh8yWe85Ag7vduQg_sbNERG0rMo1ui_cG-hWNA_lsSdDCdrRjs5LPfuKiLtVjj66jMtjbCvXnmKaVUS8wcaWk3AX2IN6lk7kJBr4NdC2PtpCPsPKl6GnCuw22t_CndD22xvbUac5OBECQxaEjjKvBkcSaSLEpGHddL-QkkMGDSqKuw_WUX-h6osgBjor7ZkysoXBwtvQZ8ezG2xg76bdmSv-Yyda9jxUtxYAxUD8bw_MeQW8LRF2c69FZOSXGOqJffh94msIb-nMrgDdfvnoFtReYCTKFy7pj_mOxHs3nQ80RQaVDHhJ00fqGlbBgVsoGLG50-k0QoWDBuLf3ORFJtGAFSYqdSkKd4MYGm_8sqovTatKHhMThLNmAxmtDJmomD27jW_RoRn2jZNk9f1Pr86qzcy1R-kUg0uPZoiOexxP2N0G9gavIzTvDybsM6lhJuAIlvr0l7kP3p1tmvnmJSFAeRLN_8xZDaJiugsrBUn8w2HxO2FOQFwRyBBsn_rHYccRuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به سپاهان توسط یاسر آسانی
استقلال ۱ _ ۰ سپاهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/683709" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683708">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سرپرست وزارت دفاع: یافته‌های فراوان اطلاعاتی و فناورانه‌ای از دشمن به دست آوردیم
🔹
کمیسیون امور داخلی مجلس: اعتبار گذرنامه افراد بالای ۱۵ سال ۱۰ ساله و زیر ۱۵ سال ۷ ساله می‌شود.
🔹
وزارت دفاع عراق: ۹ مهر تاریخ نهایی خروج نیروهای بیگانه از عراق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/683708" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683707">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
خبرهایی درباره انفجار در حلب سوریه
🔹
منابع خبری از انفجار در حلب خبر دادند، ولی هنوز جزئیاتی درباره علت انفجار منتشر نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/683707" target="_blank">📅 19:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683706">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc966282fc.mp4?token=vCJ0FoRjEyDZZXMG9V22gNIpPMgsT0MJ0xSec4jo4tm7zauu5IO-Nhi22jyXx25LBuw6Ebm9cXv0NLNNyt1a_Q6hXruf0WlSw47ZLvNJ0Ds22U5pLijOyTaQw9dU0jOskfRT26kY3HooEiy7thd_CZdzfwb9c7ozjugF-jzYBU1Cphx4ICRHicH4SQ27TDFvSjHBMliwu54TQEVNe1KT9HnRt3ijETv91si24SVUZ203At7v7Q5JaG0F0KAcsb4VP61IawIvqw9v9pS_Vo60jaA-8J724ly-w5A6nOgqwlMz_Ue2dhyAkfGYKqSaHjiH6EmrGyJkcNI_W6lUHigWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc966282fc.mp4?token=vCJ0FoRjEyDZZXMG9V22gNIpPMgsT0MJ0xSec4jo4tm7zauu5IO-Nhi22jyXx25LBuw6Ebm9cXv0NLNNyt1a_Q6hXruf0WlSw47ZLvNJ0Ds22U5pLijOyTaQw9dU0jOskfRT26kY3HooEiy7thd_CZdzfwb9c7ozjugF-jzYBU1Cphx4ICRHicH4SQ27TDFvSjHBMliwu54TQEVNe1KT9HnRt3ijETv91si24SVUZ203At7v7Q5JaG0F0KAcsb4VP61IawIvqw9v9pS_Vo60jaA-8J724ly-w5A6nOgqwlMz_Ue2dhyAkfGYKqSaHjiH6EmrGyJkcNI_W6lUHigWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش زیبا روی خورشید
🔹
این ساختار حلقه‌ای تاج خورشیدی، یک مسیر مغناطیسی است که پلاسمای فوق‌داغ پس از یک شراره خورشیدی از طریق آن به سطح خورشید بازمی‌گردد.
🔹
ثبت این ساختارهای ظریف و رشته‌ای در هیدروژن آلفا با این میزان پایداری بسیار نادر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/683706" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683705">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a398e28d40.mp4?token=AaD_fulNOvey57FaryfS4HjUMygBd20zNidkAtkg4r79SIWjYoUrqA7FWcX7CpSAth6yOYNokjjXzxsDmX3JIaimsUTIzbGoYuytgGWk3aXtH9MsmW18dcn-BUzmLw66Y9jkOqsk-KascJbWDVWzQAjJ0m6red9-3FykxZzeBwGNh7qx8WeZRsNfaXC-Q1YR0gXBJ2YOCI67pJFJ1lB9jgwVZPtxYh_GSOobIQM3Mpo_eBzAFTVmlgs_M5O0bhphsPpe-M1ZT_9WiPRNwNKYuqaTxOXxYvX5fFTrHLFGf_oD1yGbe0FNu9HMptDZCyPPpImqBF8Ez9ZEKWlk_n8OVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a398e28d40.mp4?token=AaD_fulNOvey57FaryfS4HjUMygBd20zNidkAtkg4r79SIWjYoUrqA7FWcX7CpSAth6yOYNokjjXzxsDmX3JIaimsUTIzbGoYuytgGWk3aXtH9MsmW18dcn-BUzmLw66Y9jkOqsk-KascJbWDVWzQAjJ0m6red9-3FykxZzeBwGNh7qx8WeZRsNfaXC-Q1YR0gXBJ2YOCI67pJFJ1lB9jgwVZPtxYh_GSOobIQM3Mpo_eBzAFTVmlgs_M5O0bhphsPpe-M1ZT_9WiPRNwNKYuqaTxOXxYvX5fFTrHLFGf_oD1yGbe0FNu9HMptDZCyPPpImqBF8Ez9ZEKWlk_n8OVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام پناهیان: کسانی که در مسئله علی‌الاصول دل رهبر انقلاب را خون کردند امروز همچنان از بخش‌هایی از توافقنامه دفاع می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/683705" target="_blank">📅 19:11 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
