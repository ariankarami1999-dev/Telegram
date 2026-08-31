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
<img src="https://cdn4.telesco.pe/file/DSDJzEdDq7NjvIDWDNOAuDsPTeZKzsa57xijsaO6jKbsnylZXUjhp0VrgEHlz3I515TRpb-qDBNb6-wfPrXOIpM1GE-vixDvuLDAqgLb-hXk0dwPX_vORQ2NY_1w7IJsbPzF7PiBJvdf5qeJ5Hl-wfIP1IyTZTJpELFi2JyZQ3yCcJZXfW5KjycseiySCUPr8Y-ze_Ar-UCk42_kh8ClffAYplhDJmZysUH7rOj13Gz5UAKomzwcjahH-Zf1zJEFBalkKYcwJ5nXARyR3mYQc2STdV99tm1xnmyAimEbtgNhEZainSRJM-iqEyyketx3uHUhgJ8q1xBot3xi4LENeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-459282">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجار کنترل‌شده در محدودۀ کبودراهنگ همدان
🔹
فرمانداری شهرستان کبودرآهنگ: عملیات انفجار کنترل‌شده مهمات باقی‌مانده از جنگ رمضان فردا در محدودۀ پایگاه هوایی شهید محمد نوژه انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/farsna/459282" target="_blank">📅 20:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459281">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0YXtgqmghnRnmDYcEfcz_ACYmXVH17wpR08JGxoVd_p1M2etmaEUTYNzB8I1gAaS78vqPY3CuFWd8T8zTOTPqB-WTFelEfE5ddTEVUo0MQsU5-89ZcAJ7p25uJ3bzBhSZqyredNYgNVnLSmSxArArLpphISZMQ9IXhgxoXcrHhA99twSHYFVkxXRCY5LoVR_enodXH69CBVJtKm-XMM7NmT1LTwzbnyuJ7rQ8b63dvDtFeYXH8CRRma13Vy2FCEP1EKXlrbhVt1tsjYdoF6V0ezm-xn5W06-nGl3RxMNbPM4236srI0rHdb6tQZm9X237InPST_suiPo8g1NSeqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز فروش بلیت شهرآورد از امشب
🔹
ظرفیت برای حضور هواداران دو تیم در ورزشگاه، به‌صورت ۵۰ درصد برای هواداران استقلال و ۵۰ درصد برای هواداران پرسپولیس اختصاص‌یافته است.
🔹
فروش بلیت این دیدار از شامگاه امروز و صرفاً از طریق سامانه رسمی بلیت‌فروشی انجام خواهد شد.…</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/459281" target="_blank">📅 20:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459280">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIPyDYN9q8IkrFki4ZX8hXgJw94qKspEjPJPPVB1JkYI9te-z8f7d8DT2NiearKwjL8Srwh6fD61RPyLdG6q0t-sD7M0VUQGqY-3XRf8xFT0NDdQaEQbOvwZ4U-jU9b6ocMmCdzqwM2YbPCJy7ZJBReB7olIukFs0gwPnbNlaZ4xFtPydJdPe6PmdBhUDtFvHyGdmSdR_2R0CHtw00PvsiiKxdrMdE7E63REmK7a_FwLnkmmkVU9S5rEJ6FhGeZo8sDggMqwSctvM0g7QeGp5AWl7Be4arNAAGNbRzurSvNr765IyRmxMrFNZcxesmzuEqKyRhiqwzyXB_nR251hvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو آبراهام لینکلن در پاتایا پهلو می‌گیرد
🔹
ناو هواپیمابر یواس‌اس آبراهام لینکلن با ۵ هزار ملوان و تفنگدار دریایی که بیش از ۲۰۰ روز را در دریا سپری کرده‌اند، روز چهارشنبه در پاتایای تایلند پهلو می‌گیرد. مقامات محلی ضمن تشدید برخورد با روسپی‌گری، برای جلوگیری از آسیب‌های اجتماعی ناشی از ورود انبوه نظامیان، گشت‌های پلیس را افزایش داده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/459280" target="_blank">📅 20:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459279">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyy3F5WoFJLnshST-U3ZBR-jEwPtyeXWx94G5sQCcicJysosmDY84ciZKBABA8fmNE3O1B4tYpMvCxcGGOiEph8ULYOoi3k39hmpQwdNdRIVu_JoIe3BGLAWiaQ5u3KCYKvxmJ4XVGTaUsgtvCvypIZVKh2HyB-ZDpc_fYg0ciQb55ijrxTpuWSqxAznX3LAUCtkaRE5TVjF-E9cQEsRCVjl6VQLH1TtOgQ5b1PFGLxTyH6_y9bQ05buUgRUNDeCkxJx9jR_K5vPBnv1t-SFLApiHBYQ8JdHdK_pIIXW0FWtlwqGfmy8SsgyNRagGjU_-OtUpn2yXMq8UDH949hNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم تجاوزات رژیم صهیونیستی در جنوب لبنان
🔹
رژیم صهیونیستی بلندی‌های علی‌الطاهر و نقاطی در حومۀ شهرهای کفر رمان، میفدون و زوطر شرقی در جنوب لبنان را هدف حملۀ هوایی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/459279" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459278">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2pDIhgJED1LQ6X6ytXd4Xyi-8oCcz5BvhIYB7IdZwDOGxSiXgtuvGmGzaH2_YyqJ7BwFtuSyU1xT_Apa7csNNlgZWdFJJOrKWroOWGsp2rGMDBkVR7UdSdU4WrizWNLeJUl_mRHFqmg0WWGvqen16pCnDjtsB3YbrXcTI-VYV-Gq6sq0NG-tA5fAmDhvBwZibbP-cmGe8Wb0Wepw6ZPxDdLsa_auosgHJ4n5ihGOVxh5iwiGHpMs5Rd3ReyfFlhVpPVxBg6jrpprOXTmkv7-wbz6MslfSkSrwuZ47N6J4NOOn2UE6sQIgd-MzvFxQ2yZRne7qm0_PkuTo6jxDXfNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی حالا باید پاسخگوی اروپا باشد
🔹
رویترز: کمیسیون اروپا چت‌جی‌پی‌تی، ردیت و روبلوکس را در ردهٔ «پلتفرم‌های بسیار بزرگ» قرار داد؛ تصمیمی که این سرویس‌ها را مشمول الزامات سخت‌گیرانه‌تر قانون خدمات دیجیتال اتحادیه اروپا می‌کند.
🔹
چت‌جی‌پی‌تی با این تصمیم، اولین چت‌بات هوش مصنوعی است که در این چارچوب در چنین سطحی قرار می‌گیرد.
🔹
چت‌جی‌پی‌تی در این چارچوب به‌عنوان یک «موتور جست‌وجوی بسیار بزرگ آنلاین» و ردیت و روبلوکس به‌عنوان «پلتفرم‌های آنلاین بسیار بزرگ» شناخته شده‌اند.
🔹
بر اساس قانون خدمات دیجیتال، پلتفرم‌های مشمول این رده باید خطرهای مرتبط با محتوای غیرقانونی، آسیب به کاربران، امنیت و حریم خصوصی کودکان و سوءاستفاده از سامانه‌های الگوریتمی را ارزیابی و برای کاهش آن‌ها اقدام کنند.
🔹
این تصمیم در حالی گرفته شده که اتحادیه اروپا پیش‌تر نیز نظارت گسترده‌ای بر شرکت‌های بزرگ فناوری مانند آمازون، اپل، گوگل، متا، مایکروسافت و تیک‌تاک اعمال کرده است.
🔹
اکنون چت‌جی‌پی‌تی نیز وارد همین حلقهٔ نظارتی شده و باید خود را با مجموعه‌ای از الزامات اضافی قانون خدمات دیجیتال تطبیق دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/459278" target="_blank">📅 20:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459277">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOVnOmQ5DuJe1CjhcdLZ_JZz44py3xA_JMsNTox75o7WFxOCcrZ6s5bw57_20SSXjTRTk47A85tu5i1rYzTGsP3XiRt7waMWPCS-rW3l7jaVjPCkYq6DfuqyoxTD5sbah7cth_HF7cp55F_1115WCgab4DSHjcQorkDyNPH2V65IjPO7ybn16Q83Sn8Bu9kCvtLPyj8qpUw_mU4mJoqoNGKVSq0AzuZBJa9KlpSGg0Nz3BAyc-KgvLv390xLR-FBKVOJ6ewgDoVXEHNebEv8Um99smLhRn5v6xZOZfoGIvJMWaCb_HAUAn008lBI2rC7lL6MWxNL-cF24mhDLQP9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت‌پردهٔ «آینده‌فروشی» قیمت خانه
🔹
برخلاف طلا و برخی دارایی‌های مالی که تغییر نرخ ارز را تقریباً لحظه‌ای در قیمت خود منعکس می‌کنند، مسکن بازاری کم‌نقدشونده با دورهٔ معاملاتی طولانی است. به همین دلیل جهش دلار الزاماً به معنای افزایش فوری قیمت معاملات مسکن نیست.
🔹
مهم‌ترین تفاوت بازار مسکن با ارز و طلا، سرعت کشف قیمت است. هزاران معامله روزانه در بازارهای مالی می‌تواند ظرف چند دقیقه قیمت جدیدی ایجاد کند، اما در بازار ملک ممکن است فاصلهٔ میان عرضهٔ یک واحد تا انجام معامله چند هفته یا حتی چند ماه باشد.
🔹
کارشناسان معتقدند افزایش دلار اثر آنی و فوری بر قیمت مسکن ندارد. به بیان دیگر، اگر دلار امروز جهش کند نمی‌توان انتظار داشت قیمت واقعی معاملات مسکن نیز فردا به همان نسبت افزایش پیدا کند.
🔹
اما شاید مهم‌ترین اثر جهش ارز حتی قبل از افزایش هزینه ساخت ظاهر شود. یعنی پدیده‌ای ایجاد می‌شود که می‌توان آن را «آینده‌فروشی» مسکن نامید؛ یعنی مالک افزایش احتمالی قیمت‌ها در آینده را از همین امروز وارد قیمت پیشنهادی ملک می‌کند.
🔹
این قیمت الزاماً قیمت واقعی بازار نیست. ممکن است هیچ خریداری حاضر به پرداخت آن نباشد. به همین دلیل در دوره‌های شوک ارزی می‌توان همزمان شاهد افزایش قیمت‌های پیشنهادی و کاهش تعداد معاملات بود؛ وضعیتی که فرآیند کشف قیمت واقعی مسکن را دشوار می‌کند.
🔸
کارشناسان معتقدند برای خروج از این وضعیت، باید با قیمت‌سازی غیرواقعی مقابله و شفافیت را به بازار مسکن بازگرداند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/459277" target="_blank">📅 20:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459276">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo_TvdGINy8Xuodjkwgxg8zg8rICbIc3Ku8XFlYY65VEqV3QeZMKqGWFY_YnDZZyBaqBXCE2WwxXKn7HHkmCs9KHCGuMKjIkeUe7DcYCA7CdjWmQkqHEOVNNckZVpFJuP7_X2OOMoFwHKuX-3Lqsrc0tAQh2-bj2-mF84R9vBmZ32OhqzkUoutDqv0t5vFHie8MpU_N_J6k77X26PcxWj7JfmrWBct0asGzaX3f_aPZkImIhZMZYZsimX-5q1JPk4d1V4OvU3-KhxRHvmsq8qXubaB8bFSrzVlp4odhWMkST68e4PjmnpZqn3gfPV1jjptnZnwPE5nAC74D-rOPv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ جمعی از نمایندگان مجلس به سران قوا دربارۀ عملکرد همتی
🔹
نایب رئیس کمیسیون اصل ۹۰: جمعی از نمایندگان مجلس به سران قوا دربارۀ عملکرد همتی در بانک مرکزی و وضعیت بازار ارز نامه نوشتند.
🔹
در بخش‌هایی از این نامه آمده: «نوسانات شدید و تکرارشوندۀ بازار ارز را نمی‌توان صرفا به جنگ با آمریکا یا هیجانات بازار و سوداگری نسبت داد.
🔹
بانک مرکزی باید با شفافیت بیشتری دربارۀ وضعیت موجود و برنامه‌های خود برای مدیریت بازار توضیح دهد.
🔹
از مدیریت بانک مرکزی انتظار می‌رود موارد زیر را عملی کند:
🔹
وضعیت بازار ارز را شفاف کند.
🔹
برنامۀ مشخص برای مهار تورم ارائه کند.
🔹
درباره ناترازی بانک‌ها با مردم صادقانه صحبت کند.
🔹
از تصمیمات غیرقابل پیش‌بینی فاصله بگیرد.
🔹
گزارش عملکرد بانک مرکزی به‌صورت منظم منتشر شود.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/459276" target="_blank">📅 20:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
🔹
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/459275" target="_blank">📅 19:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a825933b.mp4?token=Vo9J5xqEuIHjBGmw-S85Y0Z78P9v8h80MEEPGClDrUrmryfZmsAPhLIBJKd-F_9CVM71LDwtf9LGit63VGDMxKMoxSOljM3_aoXiyEaM63R9dMqXRkcUc8J86vhi4po9avdW1F2M4YC0HYYxMeZIRSjDeGxpfIFVZamJ35TetXBMkbsbhaKqFx7MKSBvUhKLjIeiZfxTamKx_2vAYyt86Z0yzGgPbHZ6rr32HSiDk8raC-6-fg8CiiSJyfQX1SkEJBL4En2DE2aUQjlvHGf0ucZ9Zf2adOeKkjiLqe6XjvDeI5ZlAZUXGa_W3ty6kSlz94fTDzyDpTM08Hpf1Hv3kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a825933b.mp4?token=Vo9J5xqEuIHjBGmw-S85Y0Z78P9v8h80MEEPGClDrUrmryfZmsAPhLIBJKd-F_9CVM71LDwtf9LGit63VGDMxKMoxSOljM3_aoXiyEaM63R9dMqXRkcUc8J86vhi4po9avdW1F2M4YC0HYYxMeZIRSjDeGxpfIFVZamJ35TetXBMkbsbhaKqFx7MKSBvUhKLjIeiZfxTamKx_2vAYyt86Z0yzGgPbHZ6rr32HSiDk8raC-6-fg8CiiSJyfQX1SkEJBL4En2DE2aUQjlvHGf0ucZ9Zf2adOeKkjiLqe6XjvDeI5ZlAZUXGa_W3ty6kSlz94fTDzyDpTM08Hpf1Hv3kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژۀ کاروان ایران در بازی‌های جهانی عشایری قرقیزستان در حضور پزشکیان
@Fasrna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/459274" target="_blank">📅 19:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459272">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عامل شهادت ۲ مامور فراجا در سرباز دستگیر شد
🔹
فرمانده انتظامی سیستان‌وبلوچستان: درپی شهادت ۲ نفر از کارکنان انتظامی در شهرستان سرباز توسط اشرار مسلح در فروردین‌ماه دستگیری عوامل این جنایت در دستور کار پلیس قرار گرفت.
🔹
با وجود متواری بودن عوامل این حادثه یکی از آنان در شهرستان راسک شناسایی و دستگیر شد و تلاش برای دستگیری دیگر عوامل این جنایت ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/459272" target="_blank">📅 19:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459271">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5ab3b8a4.mp4?token=ZLIXao1iTfTaG6uqHj7nMHpF_XJQIxmNzl0ERTzduSQDcliufAIgi--0UOhDPoKOXljoC9jW-PfBi8umiGFmpldXA0j4-ATZYsacFOE30IyQOne8KUXjxG4WMa81MSI9KrU173hvLM0bFW51UbQELdgl0k3Eezp7J_GVvgasyXgnQGNvgUbF668i8Gzc-PPMK-TQyOk-jWWXOVCoVZxA07bav-IqUzaNLQ1FB-l4b3A15uucf7gk_tolfnQsaeeM3E1Tj7cpF828M_JKAkZUcKw18EOjKoQbaB0yybyeIjDZd884HBSMTZkIr9K5jmq4Pf_2oc5IAFWtEA_pghB98FvIpoxuqDsT-f33WCpTe-ba0NZAjFsz3HpvnFGYIjy1838YRln1fi1Y2-qSyxwTF40K0l3v2XG0O9b6IO2MtfeLOKEwqiaUmDwj-XxhHgzubgikfbCGm4zvTSJPpmpnChLhActyddVhpcmyQMoXEv9DM5IiSrdSpnW6tO4V6vcRzJxbV-jpRtr-5_kFhD5D9p0-jwaKJ67HDsvzqg2NXJMutffscC7Ww28W9P65XikoD_uP23iRkEY1Be_UUZb2ZB6dX7DOwus-Nvy_VhvpxRLylkGrOGAQYYS8NtWwqGE-89emC5FrO2FWeuJLDuPrIC6ouccsGaX0eB8Amzf11B4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5ab3b8a4.mp4?token=ZLIXao1iTfTaG6uqHj7nMHpF_XJQIxmNzl0ERTzduSQDcliufAIgi--0UOhDPoKOXljoC9jW-PfBi8umiGFmpldXA0j4-ATZYsacFOE30IyQOne8KUXjxG4WMa81MSI9KrU173hvLM0bFW51UbQELdgl0k3Eezp7J_GVvgasyXgnQGNvgUbF668i8Gzc-PPMK-TQyOk-jWWXOVCoVZxA07bav-IqUzaNLQ1FB-l4b3A15uucf7gk_tolfnQsaeeM3E1Tj7cpF828M_JKAkZUcKw18EOjKoQbaB0yybyeIjDZd884HBSMTZkIr9K5jmq4Pf_2oc5IAFWtEA_pghB98FvIpoxuqDsT-f33WCpTe-ba0NZAjFsz3HpvnFGYIjy1838YRln1fi1Y2-qSyxwTF40K0l3v2XG0O9b6IO2MtfeLOKEwqiaUmDwj-XxhHgzubgikfbCGm4zvTSJPpmpnChLhActyddVhpcmyQMoXEv9DM5IiSrdSpnW6tO4V6vcRzJxbV-jpRtr-5_kFhD5D9p0-jwaKJ67HDsvzqg2NXJMutffscC7Ww28W9P65XikoD_uP23iRkEY1Be_UUZb2ZB6dX7DOwus-Nvy_VhvpxRLylkGrOGAQYYS8NtWwqGE-89emC5FrO2FWeuJLDuPrIC6ouccsGaX0eB8Amzf11B4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داستان دیدار حاج قاسم و ابراهیم حاتمی‌کیا چه بود؟  @Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/459271" target="_blank">📅 19:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459269">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سرکردهٔ شبکه تراستی با بدهی ۷۰ هزار میلیارد تومانی دستگیر شد
🔹
مرکز اطلاع‌رسانی پلیس اعلام کرد «الف.ل»، از سرکردگان شبکه تراستی که طی سال‌های گذشته مبادرت به دریافت ارز حاصل از صادرات کرده بود، توسط کارآگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد. …</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/459269" target="_blank">📅 19:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459268">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f6782742.mp4?token=nXca0vZDuK1viXJ-jYdNWqPo1EoTqQYsSsw9yqEBmdxm4igrpUUrY6_CBjCFY9Xj1Sage7HtR4kyl7mnMr3yJFA-eAaeEEvhDhArHL8EXNzcDkAVdpFF1vsv29CPv9CLeKYUJkRTOwvL-RQ28epgVZlHchjDT5qfdvnZgUW1kPImoQ4RTzGOYEvIVHII9Q3pQ2N4I5paiIHVojRWwKByGIOm2wyLkDV5E6Ym-pySAnXM9MrR0uYdUAKN3n_djdumoa96I3JLscNQ-K7EwRBh2KNJKv7tzIrgfXyQYQTtEP6CKcCsXf8FJ1Lqh0Oi_NKG13Z93iCvjOH-WCIUg5LrzFW5dsfGEQGRTTwR0ijnJoGUtPzbGBjUhTM7ueLEkNOWa0PWZt4liV3Ed7qH5muxkxp95ePnLV2gIon8TSqhkNZSeJ-i-faF7afkfT_cbcZl-PauSh61plUL41us6j9APwG6aFMm_r9zNrh_nCpQlf4blsbrbaH0x9-Dcqk8bweV5gPYop_sXTKh-1pEkqpxfgwEhU8dxi-i6Yow-YZq4NE-hN9L13BUDaSCx82ZUeOisnqvy57YSEUmalpJD-NCryo4bBaezjt4YJrPIqPz0dlH43HtoPueiq1CEJwso-MkNaB43vTxmOB5KN-50OuSfMvNqKPCtI5hAVpx_ZImz0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f6782742.mp4?token=nXca0vZDuK1viXJ-jYdNWqPo1EoTqQYsSsw9yqEBmdxm4igrpUUrY6_CBjCFY9Xj1Sage7HtR4kyl7mnMr3yJFA-eAaeEEvhDhArHL8EXNzcDkAVdpFF1vsv29CPv9CLeKYUJkRTOwvL-RQ28epgVZlHchjDT5qfdvnZgUW1kPImoQ4RTzGOYEvIVHII9Q3pQ2N4I5paiIHVojRWwKByGIOm2wyLkDV5E6Ym-pySAnXM9MrR0uYdUAKN3n_djdumoa96I3JLscNQ-K7EwRBh2KNJKv7tzIrgfXyQYQTtEP6CKcCsXf8FJ1Lqh0Oi_NKG13Z93iCvjOH-WCIUg5LrzFW5dsfGEQGRTTwR0ijnJoGUtPzbGBjUhTM7ueLEkNOWa0PWZt4liV3Ed7qH5muxkxp95ePnLV2gIon8TSqhkNZSeJ-i-faF7afkfT_cbcZl-PauSh61plUL41us6j9APwG6aFMm_r9zNrh_nCpQlf4blsbrbaH0x9-Dcqk8bweV5gPYop_sXTKh-1pEkqpxfgwEhU8dxi-i6Yow-YZq4NE-hN9L13BUDaSCx82ZUeOisnqvy57YSEUmalpJD-NCryo4bBaezjt4YJrPIqPz0dlH43HtoPueiq1CEJwso-MkNaB43vTxmOB5KN-50OuSfMvNqKPCtI5hAVpx_ZImz0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داستان دیدار حاج قاسم و ابراهیم حاتمی‌کیا چه بود؟
@Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/459268" target="_blank">📅 19:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459260">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrtrSs88KUENtNsTPRVfDQH_Il6DSp3JMhgl-xgzoKU608CgTHwGTMbj4GQq-XG2JsIFb6tH7PvKx5eWctOWkJcaJ97ZRiYPPKAncjH7lIZDZn6_0PlR0qmIsQt2v81fJPvZF4zxazPmw97cmbCVafobHXHUqTiFxZeuoXtkFMUYttRxNiL4dIeZR5eplM7FaGfTCsSDji3czabqd3zxFVIWokPmkbJmomAeuNeozlXYKVnyzrllaoVcjmufChc_BMy-i2T9Bj123zH8hElVJx5-V2i4kJS3IngKc0VUaz9JJLWsKOIJq0-kch38ktx35yY4OJ3ldjEQc3EecMmxnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_4slxGCtPNzUyS_sVSUtZKDTG8GfSEfyz0lHHNIZmCY8auWTSkTs6waXVJqDsikEMpdDKXP4TCmR1uYOUix39SGHTqWSj07Pk-T0GwuJZPfAo-MDw68jx98Et8rwJODSijLoR858F0y6IVnMP82ZFquhH_W2vkIS-ZJ6ykbMu-COiHBoIdJlPMFTFUCvU6BwQE9AfiTFjI8OOD2RFaKH2leHP02hwbM1b6FaI93HIXHVwCnq2nvMD9RWEN861ol-GRSWb1pj2o6YY1BBTrwtRmDWJHu0SyD-6AbUw8cgL9ISfW_YoRayKvhHhJF__2QAVXvFS6-erLMQBAPuyCrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2H4OlZqmfKP1s4xcVBWqiYQrOyU6a-UuNKiC8xdrBzIsJ2J65eXBbDlDVJmpshhHMAmUsdjBsFg0Yvhe3XzkcgFMuTZd1g_rMpv_dem-PYhsAWFCQRj6_1RBCtlAx8gna5HzyE6B3veKKBM8bbFD34alrBXmUAlEEQH6pU6ug1RpMBIQQ8OItrlq55PJh-8YhX52QhZQGXsVF_-P0VERYrFYW_sHqm-73xKpij5CqWmB45ulinWguHqy58fXvLVpCucB2aQhojG4AsJdtGgGn-TPc0_cSX9jr0DulD0_A2D1Ta47ctU6SLEBsNgSGBukRaj1ggRdOE2upiRXvKjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvKdbKOhFnux3R39ZHxKABTH7sy61QQhM3ZbLn9WLvE4yVhsi6aTLFDZLZxbwTP8Rb2qzh7AbTkztQzJXs5jagyZS5-5u25bKfBcjjf8qSFYQhYX3v8fPndz57XbFXywe8ntbPz3Crjkm4oqZp4OM1xtlVO7hxpHzQQnlApmupW4yl2fXLI6IOnLun3jROjwBGbE-aoPdqbWGUHIDIE1K4cGLT_KnLaQRSpIfQRZYFtIw8k7wDH4bZgFcqqHFCjUlynBX4nC8En-VV_fzaTSrRc-NEujNaluHzsixUb1nVEwXBw9E8uyZBLETzEAgGB9cNWT0iMe5rBj-rsaVxN6Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zlszm8JRQpREYm6GeQaODiH6NfmXHhUcGHsO_Ez3cnGkjtKoOQ_aR8g94VzqvOt04Ky2WeGKOJRyt8OELP-jcpV2D17u1xHazx2-2wtvtSamON4vdhGfuLFcNCXQHXEn0skZCKHs1w6fboTBgCwjEhjsY0BU8NVHmJONkrEiYvo2APyUo-r7tWvaNkgP_U1LEOaHCWoBBDe8FTJ5kWsAgEL0cDRbu2PU-eG47dJUWB0jHVGEhwScsqFilXBAGQPqX6iol0Fv4BD-2yXhMjFs4C9pRoTaUAZ-Zx3VpuQffpsgIgSiLnD-LVLz2nPW4cCXsbKTam0nLFZePBRHO9aoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ER-kOcTM4DAVSlGBJIvcvG2pM-8lAxe_COnW5KgVFDI4UGbLfe-0UWGSLmzzQVl_1fxThikVzj7Fel5LdQrwg6BtdxK8_3qLp76sQDD3AEoecCNTXXXzHF6_ClIS5aHLxol97Bfe4AVEyOKa8KbO64MgN7VR8lGljojF-gUMQHcHPth0LKCDHM50oAZVMZMvwT-U1kgS3u6sbOmnttwtGBEq2ymctBcMvytsF5jzkORgzZHF--8jqVRK4WhENlYb3PtR2oNp-KKvKgfE0JBjcs7GNf78-ozEoVXXMkEu1qPm_bZ9n7KVhm5WMoDcCOr8nsUV75papxwfpFKPZJHYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/db1DqlJhD8hM-XAfWXOuEW4RzxJceA9AUI7ilTPIwCM6F5PtGnZuqVR3kER7isPoFfSK0yEFpKqHxgkKKgJfdWRoLUBiTMjuDYNNldWqqWDiErJNla0bsJNFtp-L-K9sFgXxme1o8WFZ4xskvGFywPHu4c3YOEP7iK5rI-QR2DXWXDgNSzc5KjsKtdhfTjfKRdRHodJOcHBpMTRpXbmEmXQ16R7Rv-8tiym1dgSkQL4XWR4WurHcG8v9an725huwYBZgP89FC5NXx-KR_p56bn8jLhF6fyOnnd8REDFXDZuYENpN4aIuwVT-0gh44SyFYq5UErszg0FhtAY0pqADkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید وزیر میراث از منطقۀ توریستی قلعه الموت
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/459260" target="_blank">📅 19:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459259">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9967b11f9.mp4?token=N8oS3_vZtANvfbbE5gwGB23O5CBqeRJrGLgQtLq2xjQX1ZKklEwDvJ-q9lqEaFgv6GmLOQqG-Q9iVYEStuxrjMrEMhuW2lqDI3V8LPKefCKfg5jxOpr8ydLZyN-bua5BgOuLD3M2rM_8LJjqyVsaDAs_PlXWI449Oz7_rhhqiT_yu0sNbZouMqzzFGtd1CP_kOQSPAMYhuKP6zKt5GNXviaDbhDNpqqNchzSAKxRSs-ZOs_858Ya76lgvP_x0DPW8peuxt3rS1bxmsU_0_7-CoEdDRK4L_s7JAKuYOI2PJUhkAhkqpOm8LuL-NtsdI-ab3ELhPhnI3nn92I22t6yq5h8juLnjs8YfXVCW_o0qcc9UMBBScgZACpSvtYFFB4K6jHJYYpbk6E_cKn8-OBfQWAxAjOmqgSrtZ95RRVDTbrHwHFDLZrM367vWUhC5opevH0K2rDjVwil4ci3-kYL8u8YQ4lJnczqkvTVVjqLczJQi3nfmfYIteE3hF7jGr5mz-364XfYDZDAoOUd_4cZSyn4164B63bCxPNg9yImpFVUCw2XTNtvQcj9BkKHL-iGIhuvA5mV7rFsrmQM-so8mo8gpM9xLCaylIBpRk7gNIk0Y3vA-gThFiIpeHrqW0CVA_x1njSQAfGKcr023-HAhuQpAzS0qTjJcfdqn34FBwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9967b11f9.mp4?token=N8oS3_vZtANvfbbE5gwGB23O5CBqeRJrGLgQtLq2xjQX1ZKklEwDvJ-q9lqEaFgv6GmLOQqG-Q9iVYEStuxrjMrEMhuW2lqDI3V8LPKefCKfg5jxOpr8ydLZyN-bua5BgOuLD3M2rM_8LJjqyVsaDAs_PlXWI449Oz7_rhhqiT_yu0sNbZouMqzzFGtd1CP_kOQSPAMYhuKP6zKt5GNXviaDbhDNpqqNchzSAKxRSs-ZOs_858Ya76lgvP_x0DPW8peuxt3rS1bxmsU_0_7-CoEdDRK4L_s7JAKuYOI2PJUhkAhkqpOm8LuL-NtsdI-ab3ELhPhnI3nn92I22t6yq5h8juLnjs8YfXVCW_o0qcc9UMBBScgZACpSvtYFFB4K6jHJYYpbk6E_cKn8-OBfQWAxAjOmqgSrtZ95RRVDTbrHwHFDLZrM367vWUhC5opevH0K2rDjVwil4ci3-kYL8u8YQ4lJnczqkvTVVjqLczJQi3nfmfYIteE3hF7jGr5mz-364XfYDZDAoOUd_4cZSyn4164B63bCxPNg9yImpFVUCw2XTNtvQcj9BkKHL-iGIhuvA5mV7rFsrmQM-so8mo8gpM9xLCaylIBpRk7gNIk0Y3vA-gThFiIpeHrqW0CVA_x1njSQAfGKcr023-HAhuQpAzS0qTjJcfdqn34FBwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا خارگ است؛ دژ مستحکمی که به هیچ متجاوزی رحم نخواهد کرد
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/459259" target="_blank">📅 18:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459258">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvjF_eBYm3d8Gp_461eP8lJBzmU5p7aDQlhaJRB48g-xf_xDt4ZWZm5uMzOIHGjTi_dMMHXYxVpg7CDcfsRYMGkJCEDe1TYUJl8quIkZ6_jehdi9Z_heyAhorvmL9gUDicapIY-Mk3t1F_x_-eaLDBnq4DgkoV-uz910zIm75BzzItUuBSUJ7aUAuq94hrR881w2Ie57nNlqMlYpMSI4jPHuIxsRpx7VKGKluAGEFgP-0bNo0R-GJjHApVrDDivhN9lHEVT64Z5LArwCVkqWVkg-_y59tYIQG8UJ6BCgIo2hfPOYbigIK252EMPsISz_GR64Iy0iiaeblxtrS7JCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزمون سخت خودروسازان آغاز شد
🔹
رئیس سازمان ملی استاندارد فرزانه انصاری می‌گوید استانداردهای خودرو از ۸۵ به ۱۲۲ مورد افزایش یافته و این تغییرات قرار است به‌صورت مرحله‌ای پیاده‌سازی شود.
🔹
خودروسازان باید پلتفرم‌های خود را به سطحی برسانند که هم امکان تولید محصول با این ویژگی‌ها مهیا باشد و هم زیرساخت‌های آزمایشگاهی لازم برای آزمون و عیارسنجی آن‌ها در داخل کشور شکل بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/459258" target="_blank">📅 18:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459257">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-l-ClePHCABtVScoZ0JYCXAOWD75NAFjSEM1giz9U68nwqmvELDDKpKD2pWgZhdJQLPWzDWL8CKx3unZDeA22qcOsQedGCUjdb0GlBZykYOTBqfpRA9mbk93SosuD5exjxMwVyo71JOgsoBPoRtwy7_oIDQphr_veWjJ7e7Ooa6VF5L0vhREgW00nifKe4-inthioCeowrVyhT2tXSZx1zNXPOr3hzzsKcoXlDdVd7PA5Y7kYrqk4CCBBV8yWR-hz_iaUqK5oZpT9SBxn9fbZFlRsIS-ZvfkNZWREtqt3xhUx0iDbqEZKzkLHLYkIg__l4HJgqoTqUNLNO87FtVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت: حقوق بهورزان ۱۰ برابر شده است
🔹
ظفرقندی، وزیر بهداشت: حقوق بهورزان طی ۲ سال گذشته افزایش ۱۰ برابری داشته است. باید توجه داشت که به دلیل پایین بودن پایه پرداختی بهورزان، حتی این افزایش نیز لزوماً به معنای یک رقم بسیار بزرگ نیست، اما به هر حال این افزایش در پرداختی آن‌ها اتفاق افتاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/459257" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459256">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcvOf3XCQaBylcvw_DOgn2h8Xb8oIkTugD4B_E3H1cKRTdI_PyRxoUIe0AItJJ1qMqSBtSx8i8FSmbiO-q3ra8LGp25P_FsVfpqy6WbnXB8nwMTStVp9R638mX_h08EDYJH2xH_l06y-7SgN2Z4ABeE-np0ZXC4SnOQDDOj09-RVxO7LoCdUEemZZewkKoG6Ai9DZ6JOH_ZkZuxsEkj72B3yqbeaqu6TvkPic01tmk8eBHHcjMx8HMjtcUfyHbp0ifG9OArcp749woZZMFXw8wbtHDQ_xTKeApT5SS-OnKuBwF86GrwjXVO9VM0MpDep2mqJrtDnNQ5gIV9yPFo1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا فاتح جام‌جهانی فوتبال شد
⚽️
اسپانیا ۱ - ۰ آرژانتین  @Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/459256" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459255">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN3UnzkSe0YJ2LRLfEoe4nQTZJdLcugTDgtVW8CPQR_PQg3r32Bt4dxpa_ClRXxobp7B52ZfWnUMCG74OPrtW-8K-9ChjannQvJST1RHRrwPxL5y--ShgXw8MyE7Na91x7fvBTFs9irvvaVLbuZgSjZHtGJYhswxNZvyBLtD0vGn6DdXBZzQKj8Px04uz1GrBlxzcPnXb5X1pzKQEPC3RxueAay2Xc8kx8yITK2Q78vqHywL3Dhylzsoei99LmtPmmUiJ-sikVdVY14XXPV6dObrYnLKSrgbZixnyGU5TXAecb1Vejuh30-Az19nA_ltWe7588C7ZU6i9kZ_N-KOOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در آیین امضای توافق‌نامه بازسازی پالایشگاه پنجم پارس جنوبی (فازهای ۹ و ۱۰) مطرح شد
🔴
مدیرعامل بانک شهر: حمایت از بازسازی پروژه های صنعت نفت و گاز را مصداق جهاد اقتصادی می دانیم
⬅️
توافق‌نامه طرح بازسازی پالایشگاه پنجم پارس جنوبی (فازهای 9 و 10) میدان مشترک پارس جنوبی میان شرکت نفت و گاز پارس و کنسرسیومی به رهبری بانک شهر با هدف تسریع در بازسازی و بازگرداندن ظرفیت‌های تولیدی این پالایشگاه به چرخه تولید به امضا رسید.
⬅️
به گزارش روابط عمومی بانک شهر، دکتر سیدمحمدمهدی احمدی، مدیرعامل بانک شهر، در این مراسم با تبریک سالروز ولادت حضرت محمد(ص) و امام جعفر صادق(ع)، با اشاره به نقش بانک شهر در این پروژه ملی اظهار کرد: برای این بانک فرصت مناسبی است که در همکاری با شرکت نفت و گاز پارس، در به سرانجام رسیدن یکی از پروژه‌های مهم ملی کشور نقش‌آفرینی می‌کند.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/459255" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF7AFsyDsOckMW5gCmJ_vDSGbpiO0Cx_M7NsPCsFUhnci9sn6COrbv7pRduH3MvrHbW4qhXWNuCqZDbZRsWxQ7Me9Aw1sxIMzXHvb1T9QaVhFSsreGUn3iqbhOm3YXY3frKSvPvqN3RHaAYq-XrdtYIHwsRPY8TLpgGQaKPm2CCdtTFEVJ5_n-nw8__Un9521E9pWoCp0Jq9dcLq7XR_B3VDhFEgR2x1zSefaNzvth8E2IiFXHQiky0g8VI788wpeGDqkGUCUynUghI_HAfaUITZFKMHYyS9RYqm-9C_37ij0-BDc2VvoeYWDyKt2OCHHz2HpZ4R6ruKp9XDfT-5sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشتوانه صندوق طلای رز ترنج چگونه شکل می‌گیرد؟
🟢
از ورود طلا به بورس کالا و تأیید اصالت آن تا نگهداری در خزانه و تشکیل پرتفوی صندوق، مراحل مشخصی طی می‌شود تا هر واحد صندوق طلای رز ترنج، از پشتوانه فیزیکی طلا برخوردار باشد.
🟢
این اینفوگراف را مشاهده کنید تا به‌صورت کامل با
نحوه تأسیس، امنیت و پشتوانه صندوق طلای رز ترنج
آشنا شوید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/459254" target="_blank">📅 18:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459253">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/459253" target="_blank">📅 18:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459252">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDELSFvsNAWljVDwBEhak--ATZ-htWZL7frI2ri9EuOXJ8Soya8oJyei0vM9OGP_ANROqfoNzYrP8xCAT0gsq5mczirmM9lQJS9lP_vQC_yQd9m4UzPIC4lj_PMEUVOlz8lEz084dlS8gnsowZnfKosOLE3MT8pdTAGnL5-8XYM38LFD08e6Wi89Cl_oXVwoWuivetmMBHTmwaAFcwZ1MHDkGfg3uSvwdfSiz7E0hF4c3fhp52qjlk6v7yFRCDtmJVlOqePgRF7dohMLfZrWF6TBsruYpE6WI2OVZa_9UcjR7y7ncnWrz44VIePc21TZlHdgf79ACMFHyO9nS7BAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاس گل شانگهای به پزشکیان در اوج تهدیدهای ترامپ
🔹
روزی که ایران به سازمان همکاری شانگهای پیوست شی جین‌پینگ، رئیس‌جمهور چین، این عضویت را نشانهٔ سرزندگی خانوادهٔ سازمان همکاری شانگهای دانست و همان زمان گفت که چین آماده است فرصت‌های بازار و تجربه توسعه خود را با اعضای سازمان به اشتراک بگذارد.
🔹
در همان نشست ولادیمیر پوتین، رئیس‌جمهور روسیه نیز تأکید کرد که «اکنون وظیفه مشترک ما این است که به همکاران ایرانی کمک کنیم تا به‌طور مؤثر در فعالیت‌های چندجانبه سازمان همکاری شانگهای ادغام شوند.»
🔹
اهمیت حضور ایران در این سازمان در شرایط فعلی حالا بیش از گذشته است؛ چرا که هم‌زمان با حضور تهران در کنار چین، و روسیه، آمریکا بار دیگر از تشدید فشار اقتصادی علیه ایران سخن می‌گوید.
🔹
از سوی دیگر مسیری که چین برای همکاری اقتصادی در شانگهای دنبال می‌کند دقیقاً در نقطهٔ مقابل سیاست فشار اقتصادی آمریکا قرار دارد.
🔹
این رویکرد نشان می‌دهد شانگهای صرفاً یک همکاری سیاسی نیست و در حال ایجاد مسیرهای موازی برای تجارت، انرژی، سرمایه‌گذاری، حمل‌ونقل و مبادلات مالی میان اعضاست.مسیرهایی که می‌تواند وابستگی اقتصادهای عضو به سازوکارهای تحت نفوذ غرب را کاهش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/459252" target="_blank">📅 18:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459251">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سردار نقدی: بیش‌از ۹۰ درصد موشک‌های ما در دسترس هستند
🔹
مشاور فرمانده کل سپاه در گفت‌وگو با المیادین: بیش از ۹۰ درصد موشک‌ها هنوز در دسترس هستند و موشک‌هایی که دیگر در دسترس نیستند، موشک‌هایی هستند که ما پرتاب کرده‌ایم و موشک‌های دیگر جای آن‌ها را گرفته‌اند.…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/459251" target="_blank">📅 18:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459250">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سردار نقدی: بیش‌از ۹۰ درصد موشک‌های ما در دسترس هستند
🔹
مشاور فرمانده کل سپاه در گفت‌وگو با المیادین: بیش از ۹۰ درصد موشک‌ها هنوز در دسترس هستند و موشک‌هایی که دیگر در دسترس نیستند، موشک‌هایی هستند که ما پرتاب کرده‌ایم و موشک‌های دیگر جای آن‌ها را گرفته‌اند.…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/459250" target="_blank">📅 18:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459248">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfmxIzD-v2PHfUgrp5LfHEu-qz-xlib4DIp1X3aHd_sVs1H5D2WPgTOwt-xX8jiYoyD3CuRpXcHL-JZBRGrWKTwnnNLKWGeURA51atNGTxR9GnbQhVAWvPpWJJ3A4ozJyrsW46cybp0lKx9ymlBtplxOMnEDjz5vtICiJZAMUoYp7t20Ht4_cS3TMJLhOcRiC2fd34mjgNCQXuWlnpmjQi9bBPuxxeCfZIYUNxdGZFFz3n1jWL1AIjy8J8TJSM7ZdGhSLWttX3jXT1xH6EJKAsPzihB4CtB8FuT9bqnsKMp2aGGY3-1p5_DzMNAehADTnhEhsmX6Szh3zHlTzFpTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی: بیش‌از ۹۰ درصد موشک‌های ما در دسترس هستند
🔹
مشاور فرمانده کل سپاه در گفت‌وگو با المیادین: بیش از ۹۰ درصد موشک‌ها هنوز در دسترس هستند و موشک‌هایی که دیگر در دسترس نیستند، موشک‌هایی هستند که ما پرتاب کرده‌ایم و موشک‌های دیگر جای آن‌ها را گرفته‌اند.
🔹
ما فقط یک نقطه ضعف داشتیم و آن این بود که برخی از کارخانه‌ها و سایت‌های تولیدی در مکان‌های شناخته شده و روی زمین قرار داشتند.
🔹
در ایران وحدت وجود دارد و رابطۀ سپاه و دولت در بهترین حالت قرار دارد و بسیار قوی است.
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/459248" target="_blank">📅 18:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459247">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB-Sdmqeus-bamt0Hu5U1A1djmQ5_SuGH_ONVzuqEBjCxBglVeiZlt7sgoqDbBPL4oHyvtj5bEaMIOvSTxoljMFFLSD18RQBT7qY5RtEdfRYsBq-zB-8ShfMFReka-36NTrcGUm0MlZPGafkqw2iQlaBYGgRqNvg5_NTLobrenxhOMl3p_OCeT1CesdXKWg6u6YTjfQVJSXmXuUiTVwc7hZkhzemLNqNOFlrySNp4K7aEVMD2VZs-NzXVwJ5-vU37qt4NU6g2dySV0THW0azFtxkVAhoND37q-koCfq7vm9Z5AN0KxOTmuUvFBEYEB7NsV9hUiR3XGPyGigLi8NJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش پیشکسوتان پرسپولیس و استقلال به جنجال اخیر علی کریمی و رضا پهلوی
🔹
بهروز رهبری فرد: دعوای اپوزیسیون خارج نشین را که دیدم، فهمیدم همه چی مهمه جز خون بچه های ایران!
🔹
هاشم بیک زاده: خون بچه‌های ایران شده بازیچه دعواهای اپوزیسیون خارج نشین، واقعا شرم آوره، حیف از جوانهامون.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/459247" target="_blank">📅 18:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459246">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFDHOj9VLBexUDJy51PcwwLIIdmN3OGuCMaMpeBU6MQPuBroNsOJK2vc2IrXICaV-BEFeI1RYjvOvnHjC2fE2YCy-bwAz1rK2k_qZ3co4r-p0Sc-KDm3NeBtNk4AdAiU6POg-viqKn9ew9JGhSL8eYSPReF-Ii56K-tfUeUrPQ02LkH4K_HibNjvB8_scTcr-5imSXRCPQ1Mq_qS955GJ9xzfnW9uxp0k3lQaJmH2qSwvfOMw_Ewk9q3mhpqkrzZ5xvE94BIXyVJL0gThC49eXZklD_3-oMVElftC3ME3bYnJ7VKHuIHFK9-WCr8AUQoyN8asBPngYWULm3tR93mVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
اسپرسو با احسان محمدحسنی
گفت‌و‌گو با احسان محمدحسنی، را هم‌اکنون در
سایت
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/459246" target="_blank">📅 18:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459245">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVCtVaeRGNg_tJ_4Ke435hxlHU0y3TAUDharOELlshexqXGMsqVNj3nfKqRATe1DDEKi5cofS7ym0j_0p8YsLhyHz-CXLGrR9CCNvhe_gu0MNW8gT80UUENEhf0FOfdjZvuIzGKrP2KSCAPJ00JgVZyc-pLe41GpvRh72Nr9Arc94v18nQLRfSfKys8JoQFoOwcC73exFVqI_h-CioNVqVAu9RuSrl5GjK0ZUIdqCeym1XqnZ8hALJ-7c-i8gfYkoWB4p4UZ_uSc_ludPgjWc70iMqMmEoS6NuVno8BLV_iGXanjRw5uNlwvM2CpwRXCwNG0H2TVSRJDABwCF9vDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پزشکیان با رئیس‌جمهور تاجیکستان
🔹
پزشکیان و امامعلی رحمان در این دیدار، ضمن بررسی آخرین تحولات و روند همکاری‌های میان تهران و دوشنبه، بر ضرورت بهره‌گیری از ظرفیت‌های موجود برای توسعه و تعمیق مناسبات دو کشور در زمینه‌های مختلف تأکید کردند. @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/459245" target="_blank">📅 18:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459244">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/459244" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459243">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx8Bn4hBMnn9tVT-ln_zAkFDrUtyDZmErjCyYzkf_Sh_C7lR2bxE8O4kD-na0ReZ4WLZ9QRX995Q7QatUq0HrjlNpaAAm0xZTctQde3_1dOx4oxuRNM6LLra5DyQ2ijbVZugLE7EoxqiSRc0J_apkNo4UJwaKLPvJe_3TLH1tllhtJmsrKc-R1_V3njBSGnYBlQu4B3Qp6rMA7WELfMfJ-vL216NnqHe4fJ4Y-PDRj0uxnjCsfuEI8wujuSjAzIfPp3kXEb0Dmb6IxxlxOB9qRAAAXWVXhvAkLxb2MAPCHQQNCLsTh64Ncbq5LsAkuCI0HmPLzI89d83EokIeeHUlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاسمین پهلوی: اسرائیل این‌بار «بمب اتم بزن!»
🔹
به تازگی یاسمین پهلوی با انتشار یک استوری در صفحهٔ اینستاگرامش، ادعا کرد که ژاپن با بمب اتمی مورد حمله قرار گرفت و پیشرفت کرد.
🔹
کاربران شبکهٔ اجتماعی اکس می‌گویند هدف یاسمین از این استوری، عادی‌سازی حملهٔ هسته‌ای به ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/459243" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459242">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971bdada75.mp4?token=dc59wLHTo4OkwDZH-LdDGROuR_emfOAA0jx99VAMn_6zEhjmZfyVS2GG59sIOMHHLCfCGraTKPHLiFvrvXfpWdn0CYMY5-_6L-dbW5OyW3_vBta9r-t1LjSlzIOOenBA-3f6M_21UN44rqOtXJwGxDh-CCvqWGWetgRIxcb_iKNNVPmjjKICJ9jMvXt814TZTx90zk2d1FuZozbMtxJfz5lO4AlJF-ibStTRvMcTowYHWY_bCH3hbcSSunFVmX6W4FLRLpRoyU0Vonv4iAubUzYs8qbB9gWgDwVztyRu-jHnMQsNMipxcuZ08uP-gAZ9QtXkSJ-sEqwEgnT6PqXSXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971bdada75.mp4?token=dc59wLHTo4OkwDZH-LdDGROuR_emfOAA0jx99VAMn_6zEhjmZfyVS2GG59sIOMHHLCfCGraTKPHLiFvrvXfpWdn0CYMY5-_6L-dbW5OyW3_vBta9r-t1LjSlzIOOenBA-3f6M_21UN44rqOtXJwGxDh-CCvqWGWetgRIxcb_iKNNVPmjjKICJ9jMvXt814TZTx90zk2d1FuZozbMtxJfz5lO4AlJF-ibStTRvMcTowYHWY_bCH3hbcSSunFVmX6W4FLRLpRoyU0Vonv4iAubUzYs8qbB9gWgDwVztyRu-jHnMQsNMipxcuZ08uP-gAZ9QtXkSJ-sEqwEgnT6PqXSXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران برای حملۀ پیش‌دستانه به دشمنان آمادگی دارد
🔹
امیر سرتیپ دوم محمدرضا علیان‌نژاد معاون تربیت و آموزش ارتش، امروز گفت که در صورت نیاز به حمله پیش‌دستانه‌، «نیروها آموزش‌های لازم را طی کرده‌اند و توانایی آن وجود دارد.»
🔹
نیروهای مسلح ایران در جریان جنگ تحمیلی ۴۰ روزه نیز تجربه اجرای عملیات با رویکرد پیش‌دستانه را داشته‌اند.
🔹
در یکی از این موارد، پس از انتقال نیرو و تجهیزات نظامی آمریکا به اردن و آماده‌سازی آنها برای انجام عملیات علیه ایران، نیروهای مسلح کشورمان پیش از آغاز حمله آمریکایی‌ها دست به کار شدند.
🔹
در این عملیات که بامداد ۷ مردادماه انجام شد، نیروی هوافضای سپاه یک پایگاه هوایی و مرکز فرماندهی ارتش آمریکا در اردن را با موشک‌های بالستیک هدف قرار داد.
🔹
معاون تربیت و آموزش ارتش گفت که «دکترین ما دفاعی است، اما آموزش‌های نفوذ و حمله در تمام سطوح و با تجهیزات مختلف در نیروهای نظامی ارائه شده است»؛ از نیروی هوایی گرفته تا نیروی زمینی و نیروی دریایی که با دستور فرماندهی قابلیت اجرا دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/459242" target="_blank">📅 17:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459239">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E15AkD53-XZbmNHDwbGZmNW6Z6yOKZ8z7BqGSdpJvHGrEY3UU1bQZ0N_mhSXeCkzr4YZhYvcMSmOdOG_Br8eUUDMXAeZ57bOGQ0C-soFna1tHktGVbxNNz5A-aL-0Dre4oAFiTp9zjGF756DFsAu8j2Y0N_8O6rEeO6elPhc43cvZkOzyacfcR_-rjnnGX5vuoga4Rcrgnh5nMi4R8MeNEQXytTXwZFIoMuQqzfzqB8finyO2qxY4tJkajitV1_gTBEfb7kwy92HgGzlE40BZwkmuJnUrSDGb4TYW6aATTTe-UgtaJppK5ubQ9m51LEco3bgPtPaPz-cnHSJbzWxug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbQ-qu7Zl0p88WE3phtNM52vBUwx1VD6dF2fbB4Pw-W93HeLYYQs-Nqd-gt7ZoyPL_O8SmGZf605jDQbR0ILYJmsR2T4aj833NU403fVeRLeZDsA3AzNd6kKtf3y_o3cozvjhhEtNrf0fJF1YwtfVlwWPhgkssdMQtFgt09QXLX9DzBWja6CsHHDkGQ_EeZ67jDCBVXS9PDvXpS5ZfiDugzfWbrCJjLnPYXpgvUPMz4w18xHjPf8bQRC1Gx3nnWGM8e_OvF0SbMf9fouoY_Foh7jkPLPx39v-pRubH-NDXGaSaWXfMAyxo-RStFGEfVCEjleCTqAuJ65eatq5GpzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R9824VC-XXPV_TdkT1fQQd4vKxyCB66kr0Lq9TVOp86EZnAKNwJpyhQrPJjjKZql6qeKESNMmuCEWxld_9zSfPJBURmepAUCWp1MDKopnh705bZMwLjQZc_HVuikEbmvDJR2PvBd9moijmP6M1z3EfAg04FeZCvU4YkKol02IoZKCEcu6ZwuPvur6P8Ep-6Ue_i6v3S9esavAufgx0WJulafTp0yTxSwEy5BVX-Lf_3hFHPQe5e8In8ZFLI9ghyZIsyFVMzuRz6ow51WiJ6zY2hPMnnBF9f-qAn33DHQv2QyR3M1xYfPZKzKjIuooxl6cRUYdnBGqo1Z_J5C5mTl4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار پزشکیان با رئیس‌جمهور تاجیکستان
🔹
پزشکیان و امامعلی رحمان در این دیدار، ضمن بررسی آخرین تحولات و روند همکاری‌های میان تهران و دوشنبه، بر ضرورت بهره‌گیری از ظرفیت‌های موجود برای توسعه و تعمیق مناسبات دو کشور در زمینه‌های مختلف تأکید کردند. @Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/459239" target="_blank">📅 17:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459238">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNb9KPCGRS4cl9FkLuV98c9Tat2u0TrRdm6ENk6GapxgsOo8gi9c4U_DhMkf1CVbhiDLhUoolm2P63yODQ5j9qpDiPWpmCsVWp1ins1yyyXe-VwCdrIQydXnmzuJBdX1XsKHOCodVoZnX_vysKwDiai_cJoLuo9U5Y8VdMzq68ryFJSTlfWfXKjHZocs3EgBS2nOh1akXXKwYr2KSYQFI3YHrxwdRsWtLd80SglVwxDJ4RnscEb-29GJ-u6--S3mlXw6T9wD1fymmZbcDAGi-PWvByZIsRX8qRu8yIAwCsVQLTrV3rMJD73ZXdzZMqc2A-VvRcnPvy3AiVMbU7TaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش نسبی دمای تهران از فردا
🔹
هواشناسی استان تهران: از فردا شاهد کاهش نسبی دما خواهیم بود که این روند تا پایان هفته در استان تهران ماندگار خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/459238" target="_blank">📅 17:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459237">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PceeCN2LhwMOvN_8agwO-fOcKnN0F8Qo9L3C2dyvHK_O12xNvSUgxzDa60BmtuA9iRMR6eU03kWrGCx4YqXVPv78AHleepNcnpB15McvZFIYxujGsCFdcch5Fe_q4QLGrNZuzGgtlDfnQBrpnNc6LKqedVWlXGtD54AUfpgu008bGaG9GUh-1BZ5gWZ_Fy7K0MG4gabNzKWt8wnVUgsrQaZdXHz-0heLSGXMDhpzdMZAfcFnW4VDrEHDm0CDARcJduxu_PRbHTxH06dpwAOF0Zh32T9RWx_6Po9NA1qyYBoOHptabewOMlUltfgHiI0LdERpfZl5x5KsST0c4pjmRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست آمریکا از کشتی‌ها: با هماهنگی ایران از هرمز رد نشوید
🔹
آمریکا به شرکت‌های کشتیرانی هشدار داد که پرداخت هرگونه عوارض یا دریافت خدمات از ایران برای عبور ایمن از تنگه هرمز می‌تواند منجر به تحریم شود.
🔹
آمریکا در این اطلاعیه همچنین از فعالان صنعت کشتیرانی درخواست کرده، پیش از عبور از تنگهٔ هرمز، بررسی‌های بیشتری دربارهٔ ارتباط کشتی‌ها با ایران و احتمال پرداخت هزینه برای عبور انجام دهند.
🔹
این درخواست درحالی مطرح می‌شود که پیش‌تر ترامپ گفته بود، تنگهٔ هرمز در اختیار آمریکا قرار دارد.
🔹
با این حال، متن اطلاعیه آمریکا حاوی اعلام تصمیم جدیدی برای مسدودکردن تردد کشتی‌ها در تنگه هرمز نیست و محور اصلی آن، هشدار درباره تبعات تحریمی تعامل با نهادهای ایرانی مرتبط با کشتیرانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/459237" target="_blank">📅 17:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459236">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حملهٔ مسلحانهٔ عناصر پژاک به اهالی یک روستا در مریوان کردستان
🔹
جمعی از اهالی روستای «دری» از توابع شهرستان مریوان، هنگام بازگشت از فعالیت‌های کشاورزی، باغداری و جمع‌آوری گیاهان کوهی، هدف حمله عناصر مسلح گروهک پژاک قرار گرفتند.
🔹
در جریان این حمله، تعدادی از شهروندان محلی زخمی شدند.
🔹
کارشناسان امنیتی معتقدند در چنین شرایطی، برخورد قاطع و مستمر نیروهای امنیتی با اشرار و عناصر غیرقانونی گروهک پژاک و دیگر برهم‌زنندگان امنیت منطقه، ضرورتی جدی برای حفظ آرامش و امنیت مردم به شمار می‌رود.
🔹
در کنار نیروهای امنیتی، روستاییان و اهالی منطقه می‌توانند با شناسایی و طرد عناصر برهم‌زنندهٔ امنیت، همکاری با نیروهای مسئول و جلوگیری از ایجاد زمینهٔ فعالیت برای اشرار و عناصر وابسته به گروهک‌های تروریستی، نقش مهمی در حفظ امنیت و آرامش منطقه داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/459236" target="_blank">📅 17:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459235">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMn7OE7fwPYCz7NiFolzq2oiO68iu_FfiYP-I6c9hhXYnDuzFU7maS2bRB7riytg0Fb4nucqKbxB4VEhw3g-HNLjlxKC8rnqmXVjNLkQ7VfDYqThkwlXodjEs0DHkMsVypj_p8l2IB1FaV_BZe5Vcx-Q3lwa7rMi0H-ko9CeRW0ttQirt-5eDhJxL2ehxvqM2EhEtlS9GERMeSkr-naiZqEH9i6Py92cnIQBs50hkhFJEEDEKgxpLnCarQICfG5Y-Pd74Rse0PNT-OIPgelKV9_SipX1qXfV1XmxN8VF0u3ujPp2sej2I3C_mnQvoQCEuLA89kntewWQHot-KNvnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتباط زنده با جزیره لارک تا ساعاتی دیگر؛ دیشب در حمله آمریکا چه گذشت؟
🔸
امروز ساعت ۱۸:۱۵ از شبکه سه ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/459235" target="_blank">📅 17:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459234">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/770e1cd67d.mp4?token=NLCGkkUNd1Zh-dpRjHpNLhJALuvUVR54A22a8bLHGFw3Ys1LRZNakHQE2GVczksKA419EJEttPiFkcSKIGuolegJhuBqWxodou34kjFRRZwJmwE93KULKtheyYgNQXMIetTBPvl3n_lfTRy_Qs5qk6B2OWdec8w8ljeCbesOFNMpSBwkff2RTNyzkSzYnIm1CyL1QvMyl5FUXQaSLEe3YC-beCYW60StsoWpLfXWyGGqZdrXmDh8LYbkmKKO26lr-NM_kC2nUpNlzLJavV12mOXC74SWb61kAUt7cRKCfOWH_X-siFeobqVRjFdKChCMVkfAbEhWizXpFfWNszNDyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/770e1cd67d.mp4?token=NLCGkkUNd1Zh-dpRjHpNLhJALuvUVR54A22a8bLHGFw3Ys1LRZNakHQE2GVczksKA419EJEttPiFkcSKIGuolegJhuBqWxodou34kjFRRZwJmwE93KULKtheyYgNQXMIetTBPvl3n_lfTRy_Qs5qk6B2OWdec8w8ljeCbesOFNMpSBwkff2RTNyzkSzYnIm1CyL1QvMyl5FUXQaSLEe3YC-beCYW60StsoWpLfXWyGGqZdrXmDh8LYbkmKKO26lr-NM_kC2nUpNlzLJavV12mOXC74SWb61kAUt7cRKCfOWH_X-siFeobqVRjFdKChCMVkfAbEhWizXpFfWNszNDyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردن همچنان تکذیب می‌کند
🔹
اردن همسو با سیاست کتمان و سانسور ارتش آمریکا، ادعا کرد که ۸ موشک ایرانی را در آسمان این کشور ره‌گیری کرده است.
🔹
ارتش اردن همچون اطلاعیه‌های دوره جنگ رمضان ادعا کرد که این موشک‌ها به اهداف خود اصابت نکرده‌اند.
🔸
چنین ادعاهایی در…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/459234" target="_blank">📅 17:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459233">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62e4e0c72f.mp4?token=v1LjiavvapuX8azz4sPPynmabstIOVcOAbhkvQUIJT56YE2P7riYY6wDxEAYKW9ZLVvAyWngfBtre9SGaGnHqNjnZIclsLnGgQAlLJROTDi0RWCMQdWs98e9LGktbeXgWdCawyo6KHFS2s8UmRZPwCgZix1x2VLXqofKYiv-MNXEsgtLGH1fyhkeVJlCeEGKI--1rUNT9yhmZtEoBIIOd2Jc3D_qb66brrV2ro2CcRR56LSuFhyeiyWDc9S6H5uC9Cadu71mKYDxfNA3S2oIQLN7of4vZdUG7Vfq3MOG1uAhDEHtozjzEGlNllLOkU1MTL1SgN6nqcrS1BcAExJg8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62e4e0c72f.mp4?token=v1LjiavvapuX8azz4sPPynmabstIOVcOAbhkvQUIJT56YE2P7riYY6wDxEAYKW9ZLVvAyWngfBtre9SGaGnHqNjnZIclsLnGgQAlLJROTDi0RWCMQdWs98e9LGktbeXgWdCawyo6KHFS2s8UmRZPwCgZix1x2VLXqofKYiv-MNXEsgtLGH1fyhkeVJlCeEGKI--1rUNT9yhmZtEoBIIOd2Jc3D_qb66brrV2ro2CcRR56LSuFhyeiyWDc9S6H5uC9Cadu71mKYDxfNA3S2oIQLN7of4vZdUG7Vfq3MOG1uAhDEHtozjzEGlNllLOkU1MTL1SgN6nqcrS1BcAExJg8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروغی که باعث حمله به جزیرهٔ لارک شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/459233" target="_blank">📅 17:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459232">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvpy-3Vo533Ai_QBvWmABdlkilb11Y9bl9iHFJcsVDWyAa5n0Wp4Grk7h5070B55d8VZciSqJCQPM0xe35ErEsJY36h1ZKO2qOfmaFmfitsCD6NJIMUO1s5k23BnkgvEjMpLRfDbLT4uTXu9ncJ2h2FxE-Yh8xAwBoCktqZ-vKbAhmzCpBCIKg52Gf8sjBgfWiHPVhOQTlf894WObSe98n8tdO6qgwPbm8hP56WHEJ_kUgPnlMcm-18J-Jewc-xJdR4KeBQfwXDjAwviP9r4UIZNCMCdKNLu8Hr1qzH75nzKJG2X50zWx0Kv7NILPoVoMFvRKyJodA8FvG0LZPBzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخالفت عراق با ادامۀ حضور نیروهای ائتلاف آمریکا
🔹
سخنگوی دولت عراق، حیدر العبودی، امروز خبر داد «علی الزیدی» نخست وزیر این کشور با پیشنهاد باقی ماندن برخی از نیروهای ائتلاف بین‌المللی آمریکا پس از ۳۰ سپتامبر مخالفت کرده است.
🔹
العبودی در یک نشست خبری گفت: «دولت با نگرانی تحولات منطقه‌ای را دنبال می‌کند و عراق بخشی از درگیری نخواهد بود.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/459232" target="_blank">📅 17:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459230">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a2b39ede1.mp4?token=mBPyl2s0wz_ORJp7vJBDRNZXVgljV__ZeNUxAyp4xAxSu6sGfviUmRI01vqmXPmTOqkiG8hcXHDo2QU7iTx14LmFR5x5BvYIY6dM7Lec6d9BO0Zj7WYroOI4sfQR26w-ELQkeK7_SjWuRNspAsLp7XnvdePAIqLpyHRc5qzlgvCvZ8KvJRtqHgRR0wDmBW1pTN6-3LRdR7vZ2uh6LJvrL91BDHJLvWotuLgLPp0tb0NFnybX4C10I5bRtu4EvepZuleR3SLEmuZaldlVTUM2jGljo-o24pxhA6oDyKORD0z50XPOHrAQzWVAd5fgRmbnZa9hvetXuD0lzbgslVEk8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a2b39ede1.mp4?token=mBPyl2s0wz_ORJp7vJBDRNZXVgljV__ZeNUxAyp4xAxSu6sGfviUmRI01vqmXPmTOqkiG8hcXHDo2QU7iTx14LmFR5x5BvYIY6dM7Lec6d9BO0Zj7WYroOI4sfQR26w-ELQkeK7_SjWuRNspAsLp7XnvdePAIqLpyHRc5qzlgvCvZ8KvJRtqHgRR0wDmBW1pTN6-3LRdR7vZ2uh6LJvrL91BDHJLvWotuLgLPp0tb0NFnybX4C10I5bRtu4EvepZuleR3SLEmuZaldlVTUM2jGljo-o24pxhA6oDyKORD0z50XPOHrAQzWVAd5fgRmbnZa9hvetXuD0lzbgslVEk8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فاز اینترنشنال چطور تغییر می‌کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/459230" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459229">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPOC64BQfFLyrQdhBezExUY5uIrXdq_Yb7wsI-MVGTFMYztyOgZLnZY8Vznps97HDcJxT2opFWGGHxC_R3wb6LDStPlM24ooYwW_M2v3utbDar-is7apc_FAXOT7CLPEnNpuM6k1Nx-CndT9L-flFIvNZeEM_EmtrgUCYANNjed6_XdxEIxoL1kcdY3TJBx1oJ8U94i_2qO0iEmMq1Pbc2St-VILvWl6rOewMm-HchNKDxI1s_sdNfiAnNirR_X9YI-DMJKWec6LQHrH9-JdhW2jgxuuPOK5U_CJwp77rMt3dtkb0AFq9jsFfGnk5GsabvaAno3XicarmdT7bj7ogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز فروش بلیت شهرآورد از امشب
🔹
ظرفیت برای حضور هواداران دو تیم در ورزشگاه، به‌صورت ۵۰ درصد برای هواداران استقلال و ۵۰ درصد برای هواداران پرسپولیس اختصاص‌یافته است.
🔹
فروش بلیت این دیدار از شامگاه امروز و صرفاً از طریق
سامانه رسمی بلیت‌فروشی
انجام خواهد شد.
عکس: محمدرضا علیمددی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/459229" target="_blank">📅 16:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459228">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO7X4b0PZpU4ajouDQgCeCcZjoMIx0zqfP_4HnpStmkQZ-JT-ny6JEHvGvit-qINECt4gAavN6CsumypGNa_Mei_SybZEwGlaMhwgNP28mbFnAqBv0Y2VyaZcjIFWVQ8-ar1-2MYpolTKpInqajm_SRuzAu_pJL_dd09ewp5IgNjCTnWV42f7uY4i3u9zExHaIt5UcJs0gvG2aYn89Fq_mriziMV0nOWjqw2HZMMviE3ws4O7zszILmrEjSpnMfWtAJ8eStKa35IO-OQwTDByjcX-bKZcg4wn6hxSdiWBfLcQ2Q9FKqlulve9lpzK54m11RlFBWSazqAVmWFNJI_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور از تنگهٔ هرمز فقط با مجوز ایران
🔹
پیگیری خبرنگار دفاعی فارس بیانگر این است که تنگهٔ هرمز به‌طور کامل مسدود است و هیچ شناوری اجازهٔ عبور از آن را ندارد.
🔹
براساس این پیگیری، نیروهای مسلح جمهوری اسلامی ایران کنترل کامل تنگهٔ هرمز را در اختیار دارند و تنها شناورهایی اجازهٔ عبور از این آبراه راهبردی را خواهند داشت که مجوز لازم را از نیروی دریایی سپاه دریافت کرده باشند.
🔹
بر همین اساس عبور بدون هماهنگی و مجوز از مسیرهای تعیین‌شده امکان‌پذیر نیست.
🔹
همچنین هرگونه اقدام برای عبور از تنگهٔ هرمز بدون مجوز، به‌ویژه از سوی شناورهایی که اخطارها و مقررات ابلاغی را نادیده بگیرند، با واکنش قاطع و فوری نیروهای مسلح ایران مواجه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/459228" target="_blank">📅 16:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459227">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af76ddfece.mp4?token=CaieHzFleuvSQAavwjqQNEWMVcgyVn8mNqC_adbR0sUhldtfoUiFobruVtycWsCimia_SvSAFxE_TadH2Pp7Cobzg3qdbwzeTTWZbypQDNN1I1bVegGw-_ImrdfHRjt6Rrtl6Jl_DErP_yAAVv9mqnC98P-hN6w29VkskWdgPVb5DbdF3snktNhdZOxzwEZdPXwnhOH1mQBfkrxh4kfVcOP8jeR0rUx2g5AxkdJExwCk1Ym4wIA63fYj2DQT5ncg6mQ3ojPOu0MV-BUMi0IaguGvfOsr3kUVlX9pzjGP088Bvd4d2casBbULmKqXmksdl8gR27BogD7ShHQHpSPXvn9g8Sh2vDb_TQjWvX2_CDa6ODUhadcwnc8b8wr4KBdu-oyCW044ZLryebdsPqIUngZ7cfvIMgdyUCg0nfMODh_wNDYB7LTbQfTs3YD3pt-yM0DuKyshSEIvNoc5B84S8-H7d3Hdvj0_bYf09b85RVkaGzaxE4b9-zVpzt-yQPRpbYnS0S0pBCkN-JX_pvc5Wz-zj2N0AOA9_1ofW7KJgYSyM2llWiWcsx6ZQcxuF8qU0R4D705Rx3-nPnC-EaSLQkVWnKfjXVG4xqAPrYndpbcFD-CKDkSkh6RaiOZZ6bSOJzMa0mpn6kJZjPCVCQNtsfwS8Dqb2TzJ3DVIQLWZcn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af76ddfece.mp4?token=CaieHzFleuvSQAavwjqQNEWMVcgyVn8mNqC_adbR0sUhldtfoUiFobruVtycWsCimia_SvSAFxE_TadH2Pp7Cobzg3qdbwzeTTWZbypQDNN1I1bVegGw-_ImrdfHRjt6Rrtl6Jl_DErP_yAAVv9mqnC98P-hN6w29VkskWdgPVb5DbdF3snktNhdZOxzwEZdPXwnhOH1mQBfkrxh4kfVcOP8jeR0rUx2g5AxkdJExwCk1Ym4wIA63fYj2DQT5ncg6mQ3ojPOu0MV-BUMi0IaguGvfOsr3kUVlX9pzjGP088Bvd4d2casBbULmKqXmksdl8gR27BogD7ShHQHpSPXvn9g8Sh2vDb_TQjWvX2_CDa6ODUhadcwnc8b8wr4KBdu-oyCW044ZLryebdsPqIUngZ7cfvIMgdyUCg0nfMODh_wNDYB7LTbQfTs3YD3pt-yM0DuKyshSEIvNoc5B84S8-H7d3Hdvj0_bYf09b85RVkaGzaxE4b9-zVpzt-yQPRpbYnS0S0pBCkN-JX_pvc5Wz-zj2N0AOA9_1ofW7KJgYSyM2llWiWcsx6ZQcxuF8qU0R4D705Rx3-nPnC-EaSLQkVWnKfjXVG4xqAPrYndpbcFD-CKDkSkh6RaiOZZ6bSOJzMa0mpn6kJZjPCVCQNtsfwS8Dqb2TzJ3DVIQLWZcn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم مقام حزب اعتماد ملی: نباید به خاطر اخم غرب از تنگۀ هرمز عقب‌نشینی کنیم
🔹
به این زودی فراموش نکنیم چه کسانی حامی اسنپ‌بک شدند؟ همین اروپایی‌ها. مگر این کشورها حقوق بشر را می‌شناسند؟ @Farsna - Link</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/459227" target="_blank">📅 16:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459226">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پیگیری وزارت خارجه برای یافتن ۱۳ صیاد مفقود بندرلنگه‌ای
🔹
نمایندگی وزارت خارجه در هرمزگان پیگیری سرنوشت ۱۳ صیاد بندرلنگه‌ای را که ۷ روز است از دریا بازنگشته‌اند، در دستور کار قرار داده است.
🔹
مدارک هویتی ۴ نفر از این صیادان به نمایندگی تحویل شده و مکاتبات…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/459226" target="_blank">📅 16:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eznDpC_vGNy_rrGt-Ib24RpoJO08lrPYe29m33RwucHv88cig9CUQLhfL-h7khM3bHRjWil13MbcXFElN197QjZxNjAkPo3nOY8WUzLsFzgm6SlZ3zrkwzkDh4HLcRPtZ0W1KYUZNY5peLbE4jMFOprA50bbu46p_yoAiZTf5W2YbR-UvLcZ_p4RqdWGsIVRtdGfqzbMGNYhqgN21qTKX94CL0CXYyMygqMxG_bZf2hHRpYlLLSZzN4YdiEtfzzgeC4F40uLIxZppaC1LNmHI_AeNGXf1EE4e2fAMHIPfHgRr752ABA-q6qqFzRPAWda7qBlfkzCIf-iO2zpDRSuRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  سخنگوی نیروهای مسلح: ارتش آمریکا یک ارتش هالیوودی و تبلیغاتی است
🔹
سردار شکارچی: امروز شاهدیم که نیرو‌های آمریکایی در منطقه غرب آسیا دست به خودکشی می‌زنند و به زور سرنیزه در ارتش آمریکا خدمت می‌کنند؛ نظامیان آمریکایی سرخورده و افسرده شده‌اند و بسیاری از…</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/459225" target="_blank">📅 16:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459224">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d63a9efcc.mp4?token=ReOlLXJDvb3-jV3aGSrqdT5TBmOTmOsWFoQVVJZLeG-mH2uKBb66OISC1ONL_yYS-wm94VkSRnnr8eOg1e3MoUVZujWkc6iVWlMaNJb2WZDsOhFxHQ1QbIUludm3XFjTlqFEwqkgSZ4o2iyMlrUvCsWuJASHKXEmdMRMWEh5n4dFuTdxWNCqTZ0pHOow-luT5T1ccyBkhRxAp4e2cjN1v3ZQxIzYURZsDe1qnLk_6m_QwkTL9lDC3KWnVl_VAzx7pPWZLyd4L9jW4Jl6w4CW6jEH0YKGuh_I6fIcv9MerXFD8GVD3nOnZFIW87si5sMhNumwLR1euMc4CdWa6U06BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d63a9efcc.mp4?token=ReOlLXJDvb3-jV3aGSrqdT5TBmOTmOsWFoQVVJZLeG-mH2uKBb66OISC1ONL_yYS-wm94VkSRnnr8eOg1e3MoUVZujWkc6iVWlMaNJb2WZDsOhFxHQ1QbIUludm3XFjTlqFEwqkgSZ4o2iyMlrUvCsWuJASHKXEmdMRMWEh5n4dFuTdxWNCqTZ0pHOow-luT5T1ccyBkhRxAp4e2cjN1v3ZQxIzYURZsDe1qnLk_6m_QwkTL9lDC3KWnVl_VAzx7pPWZLyd4L9jW4Jl6w4CW6jEH0YKGuh_I6fIcv9MerXFD8GVD3nOnZFIW87si5sMhNumwLR1euMc4CdWa6U06BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا بعضی بازی‌ها +۱۸ می‌شوند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/459224" target="_blank">📅 16:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459223">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0lIQI25RgDTtrfrRznip4vEAvkwzTWfCPwMPAXOMZCoGxivOyWO3icn9s5zAO0bjtewOpLnhOOAjTXATc2-FOBTySlT4JOUALkneThQ9YPv5bthB1ho9qNv06fnChU2ZQijr58lEgku506tXNItTNMQcsy2SvKZpxrb3BToQeUSaBvR_unN4swEExxVHgfJ88aavj2MQAU_LbsnZ3QAJJPU318KM1dfnMH6ASmYD4ZVbeCowFpopoCUHHcUYOZS9G3lIEgintZUlCG43q4XUO_2tUIDzEFetruMyEtJesF4myiic-q0TOfP7yqIH0yslNskGVFCE9rlLHProsxMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
به مناسبت هفتاد و پنجمین سال آغاز فعالیت بانک صادرات ایران
🔵
اهدای جوایز ارزنده به کاربران سپینوی بانک صادرات ایران با برگزاری کمپین «۷۵ ساعت تا ۷۵ سالگی»
🎁
بانک صادرات ایران همزمان با فرارسیدن هفتاد و پنجمین سال فعالیت خود، جشنواره «۷۵ ساعت تا ۷۵ سالگی» را در نئوبانک سپینو برگزار می‌کند. کاربران می‌توانند با شرکت در این رویداد ویژه، یکی از ۷۵ برنده جایزه نقدی ۷۵ میلیون تومانی باشند.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#سپینو
#جشنواره
#جوایز_ارزنده
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/459223" target="_blank">📅 16:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbS298mcgF8o5Ff71vroHuOQdnaQ7pGxk4YG77wu5pCcwjGwwOKkWotZr8MxXwep7gHHwWtm1aHpGlaNINSo8vds4fwyZ-4OtfHuqKlemfL6KENNgTGxEASNttUnMx-9DOn6wyDcPHvpg-7ZL8RR56QdBxs_RvZl3dhSWEqn42-AaJS50fLyAUomtoJoeFA1dXYnTP4qajEu70eRNXUt9B4dHgqrkqOahPJ5cR5xwGlbDeKYnw3Ib05JMh-gVxtl2EgGevcyGV1nJOciZwQ66Djqo0SomLI_sNC6SylrzASOQP46sv0MFStTseP6BxDBCZiCntDh_x7C00LMlJxbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*بازوی سرمایه‌گذاری بله؛ از طلا تا پس‌انداز*
بازوی سرمایه‌گذاری بله حالا دو مسیر برای سرمایه‌گذاری در اختیار کاربران قرار می‌دهد؛ *خرید و فروش آنلاین طلا* و *حساب پس‌انداز با سود سالانه حداقل ۳۸٪*.
در بخش طلا، امکان خرید از مقدارهای بسیار کم، خرید و فروش ۲۴ساعته و دریافت فیزیکی طلا وجود دارد.
در حساب پس‌انداز هم سود به‌صورت روزشمار محاسبه می‌شود و برداشت از سرمایه در هر زمان امکان‌پذیر است.
این خدمات در بستراپلیکیشن بله، پیام‌رسان رسمی بانک ملی ارائه می‌شوند؛ پلتفرمی که سال‌هاست میلیون‌ها کاربر از خدمات ارتباطی و مالی آن استفاده می‌کنند.
📌
https://ble.ir/GoldBot?start=161</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/459222" target="_blank">📅 16:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/459221" target="_blank">📅 16:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سخنگوی نیروهای مسلح: مصمم هستیم آمریکایی‌ها را از منطقۀ غرب آسیا اخراج کنیم
🔹
دشمنان با وجود آنکه می‌دانستند ما کشور قدرتمندی هستیم، اما علیه ایران اقدام کردند و خود را داخل باتلاقی انداختند که هم‌اکنون نمی‌توانند از آن خارج شوند.
🔹
پاسخ ما به رئیس جمهور…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/459220" target="_blank">📅 16:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459217">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vit6M5O8kKTEecVYd4oZokc1WkMir5MDPwZKWBwwJTDUgg1eRgwQhVVHFlUAPH5XD1RsHMYeDvDcOvVT57UT7RXPB_UfqdZcmU2pOR10pwtIp6hsenPhCTeLMrWDwWy-L1v_FfLt_yC7tOltVoED9ykHQ3ebNhKpxYNYh42RDztx9DNfgEZK4LTyVgk34q3Ii-kRXzXHnRewN-Vgwtrg8aptdrF73FMP1HCUh6ItKEboOrXMDea0IVv2tTEhc7-QwNO_2SQNBTVq7-9uqs-KozV1Yn-jNGJDpH9Ih1iMCl2bWn4K1lfagsBR5WOwYv7Lfxp-7eHzlY9TgoLT-FH0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح: مصمم هستیم آمریکایی‌ها را از منطقۀ غرب آسیا اخراج کنیم
🔹
دشمنان با وجود آنکه می‌دانستند ما کشور قدرتمندی هستیم، اما علیه ایران اقدام کردند و خود را داخل باتلاقی انداختند که هم‌اکنون نمی‌توانند از آن خارج شوند.
🔹
پاسخ ما به رئیس جمهور و سران آمریکا این است که مگر در خواب ببینید که تنگه هرمز جز قلمرو آنها محسوب شود.
🔹
انتقام امام شهید، شهدای مدرسه «شجره طیبه میناب» و «لار» و مردم بی‌گناه‌مان گرفته خواهد شد؛ این موضوع دیر یا زود دارد، اما انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/459217" target="_blank">📅 16:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459216">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpi3G-OLec2kDh4cf3Jza37H-bXdxULXEzbPW5Xl66kAhIcZlVdMHgNSlsqQoczlo1sMYy9TLpBh96EEtRqLxdbmeqR-Ss2LwyZQcTpIOERGSoMlczFRRtc8_W6652Efl22P_DqkGSUwcdLvv88Ie6zQgjEpz0gzPN-OqUTNs77VHjXMmpOMVIOksAfnJh94L9U3O7KWhCCkw7d_f1BIZb2r6xa-BL1AdLu230WuYkF_LKw6W_dYsHgXsiqCgmCoUqc-Z3FNNKQuF72BT9k4587Yima6VgqlbVYy0oPGIGTmvUSiOmY8mXqaXlJjCh9iZMAawlFlN3lM8S-N3pHr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان با شهباز شریف دیدار کرد ﻿
🔹
رئیس‌جمهور ایران و نخست‌وزیر پاکستان در حاشیۀ اجلاس سران کشورهای عضو سازمان همکاری شانگهای و شانگهای پلاس در قرقیزستان، با یکدیگر دیدار و درباره آخرین وضعیت مناسبات و همکاری‌های دوجانبه و راه‌های تقویت تعاملات مشترک گفت‌وگو…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/459216" target="_blank">📅 16:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459215">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5XgXRq-UJFjdWdWHLpvWIE_xXmwhHTuNrADF1GHMfspHpMsvcDgigZFiEXm4uwasGf-5NSaIojqPRvwuF-CPasDx7leueIWgYyE_qPCoH1R-Ij1AtV9snfRar1AT3hJ5xLDj7Vm1huhtqXHsJv0gAPcUzQoCVBhRZF12_-uWewAPxnBlXIAqcK2ycvAgD1bGqyNr053jb34kiXk50d-xC4dlwTv4d04QWeylIe7DKWGOFoRFMxHXQR4_DqWbA7SP25e8jZhpkf0ve3jqcwIIJqGzU5mHeQneHiVKUUjTRoaOHyUzEnomQWOyyiqnmtCIRKGNK7LtipdfFjb4fiyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه درروی آمریکا در تنگهٔ هرمز بسته شد
🔹
مارهلم، سامانهٔ تحلیل داده‌های دریایی: ایران توانایی‌های جدیدی برای شناسایی انتقال کشتی‌به‌کشتی تحت حمایت آمریکا در تنگهٔ هرمز به‌دست آورده است.
🔹
تنها راه موجود برای خروج نفت از تنگهٔ هرمز فعلا اتکا به روش کشتی‌به‌کشتی است اما این شیوه هم‌اکنون تحت رصد و اقدام ایران قرار گرفته است.
🔹
تانکرترکرز هم می‌گوید، تنها ایرانی‌ها قابلیت امن کشتی به کشتی در تنگهٔ هرمز را دارا هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/459215" target="_blank">📅 16:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459214">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7068524a54.mp4?token=piEW4RZgEvK4SFBkgLIbmEZE668n0hZT3r8zrdj66iRm3BZNdejACs1l9OnlzcFCv3T2sU78Ju3P4u4MeBcHSFCONGP-btwR7LxjGbN--uG-BAbRwTS7ltLTmJUy6ZL5T8arc-YW5sLl-w02-A-KcKiYjrpF6xNJzuVP5VJ7TekQwyM3S4RoGoDu89pw3Zzw77MU2s9f5U3SYYqGoMUJPjD3ayNvqzKep9xmbuLMmmjNeqqMfr8DSxbjAqBlH82at1UBvTROGzhSEMAlVkecw0Bs6lXO0gq_qMgSJgdVimUoigLMv9mLnMMBvWbw7nTx3xSTGdLDZw3vsvrf6tLDk64EC0tEfB9vE-1LPTd6MWksra3BKCaM286PynoFBBwxIJT7GsqyqRQosXGVDjovNLuCA3Tc3OLq0adBlstlom7oQThQNGqBSRIenN523OZENBqWy8w-o-463yEjq1WTpTh34j_iGzjJJU4mqakQ7lb1Pfo8PtItaGFAESl7fziYUa_7SqLjxGbvwLlDiAvh_b0mW1ppB8SaF5x0F8wcUof8GNgKehj8fbxyxMPuD4KsCraS1CEb1DIMsff_91E3srZT4hZn7ZKszzsPf-apJiX6U8V2kBKaM61UJuijhyhd3GJD5_dOw9SH_5nS9xT6bSKbVGxhzncdCq8BNf89Tfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7068524a54.mp4?token=piEW4RZgEvK4SFBkgLIbmEZE668n0hZT3r8zrdj66iRm3BZNdejACs1l9OnlzcFCv3T2sU78Ju3P4u4MeBcHSFCONGP-btwR7LxjGbN--uG-BAbRwTS7ltLTmJUy6ZL5T8arc-YW5sLl-w02-A-KcKiYjrpF6xNJzuVP5VJ7TekQwyM3S4RoGoDu89pw3Zzw77MU2s9f5U3SYYqGoMUJPjD3ayNvqzKep9xmbuLMmmjNeqqMfr8DSxbjAqBlH82at1UBvTROGzhSEMAlVkecw0Bs6lXO0gq_qMgSJgdVimUoigLMv9mLnMMBvWbw7nTx3xSTGdLDZw3vsvrf6tLDk64EC0tEfB9vE-1LPTd6MWksra3BKCaM286PynoFBBwxIJT7GsqyqRQosXGVDjovNLuCA3Tc3OLq0adBlstlom7oQThQNGqBSRIenN523OZENBqWy8w-o-463yEjq1WTpTh34j_iGzjJJU4mqakQ7lb1Pfo8PtItaGFAESl7fziYUa_7SqLjxGbvwLlDiAvh_b0mW1ppB8SaF5x0F8wcUof8GNgKehj8fbxyxMPuD4KsCraS1CEb1DIMsff_91E3srZT4hZn7ZKszzsPf-apJiX6U8V2kBKaM61UJuijhyhd3GJD5_dOw9SH_5nS9xT6bSKbVGxhzncdCq8BNf89Tfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحشت در شاباک؛ نفوذ دستگاه اطلاعاتی ایران به اقشار مختلف جامعه صهیونیستی
بابک اسحاقی، خبرنگار اسرائیلی اینترنشنال: شاباک و پلیس اسرائیل اعلام کردند که این‌بار دو نوجوان 14 و 16 ساله از شمال اسرائیل از راه تلگرام با شخصی که خود را دانیل معرفی کرده ارتباط می‌گیرند و برای او مأموریت‌هایی انجام می‌دهند.
جمهوری اسلامی، اقشار مختلف جامعه را  مورد هدف قرار می‌دهد؛ از مذهبیون تا کسانی که به پول نیاز دارند و افراد عادی!
@Fars_plus</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/459214" target="_blank">📅 15:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459213">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nENeiKAn2ZCw4e9C2-eOQzR4LTzwn8W_ZPGoufZgb2q1pbsKH_hqLundEelbSGJn0cj49AMbr_OjP8_W14VJoi3TM1DG9Orp1sFX8d0lpX5FpOhCuSt4yMo1fdCpRj_Vn2eZ6qlUnvEBSzv-u3sJrhGK-ntKFju92u-v6oNvl7R6HDHmT4DPUJfAL-N3iN2m2gsesgTDDFnsHUYrf84_GDOg7ac4FVWhHW1mt_JWUJTqWedrIhr5EBPyZUd_tGSs9Ygx6cQufoimKqiGWkvxsYfV38kggk3D_Cb7JvwYLV9LBiDLgism2YsNs8HtJFqYrAfO1wLrysuvfhsYzNJWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده پدافند هوایی: دشمنان اگر خطایی کنند، حتماً پوزه‌شان به خاک مالیده خواهد شد
🔹
امیر سرتیپ علیرضا الهامی: طی چند شب گذشته، پدافند هوایی ارتش از چند سامانه و همچنین تعدادی از دستاوردهایی که در جنگ تحمیلی ۴۰ روزه به دست آمده است، رونمایی کرد که این اقدام پیام مهمی برای دشمنان داشت.
🔹
البته تلاش می‌کنیم اطلاعات مربوط به آنچه در دانشگاه‌ها، مراکز علمی، وزارت دفاع، مؤسسات پژوهشی و حتی جهاد خودکفایی نیروها تولید می‌شود، کمتر منتشر شود تا بتوانیم با حفظ این اطلاعات، بهتر از آنها در صحنه استفاده کنیم.
🔹
پیام دستاوردهایی که امروز در کشور تولید می‌شود، برای ملت‌های دوست، همسایه و ملت بزرگ ایران پیام دوستی، آرامش و صلح است اما برای کسانی که نگاه ناپاکی به مرزهای مقدس جمهوری اسلامی ایران دارند، پیام این دستاوردها قاطعیت و قدرت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/459213" target="_blank">📅 15:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459212">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zesk69xa09sdZUe5SQgcOzxk8cV8GTTDRVUc78xVKE1FDrB11sM2GBtRWx0oP7zPw1YR8ZODk8A8rwv74Hm1F78WhyUhACcHfoQll4JIOwS2mThspb_mPzIo2vCuvRSm_1Hx7XVMfHpYyF_ZLmCmuV6N9q8w49FokPoOE2uRBohyVm1XzPGAFLZmKvz82zmWMyW-5H_I9BOmxmtxSNE6SMx0JKjYVgNZvE2uIKKeisj_FXXut80Kn0XhSXRHE00rVikWz93ksWFSJsCzXDCUWrfJisFgs8_d-trbEOYxDiCUmbSJXxGsKtqEMEOWWRi9mOb_M2IysRrSdkXmJVWh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ درصد توله یوزهای آسیایی به بزرگ‌سالی می‌رسند
🔹
سازمان حفاظت محیط‌زیست: نزدیک به ۶۰ درصد از توله یوزهای آسیایی در ایران حفظ می‌شوند و به بزرگ‌سالی می‌رسند؛ این آمار در آفریقا تنها ۳۰ تا ۳۵ درصد برآورد می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/459212" target="_blank">📅 15:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459205">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwP03GXZ7X-JQ3tFogdTgXmBEMkWDXJCGYpS9TP5NmSbNyGeUg47CsuN2BfdF8dZ165rnXl6L1a6i_9JKwYiElf5JfjVUcsnM8Qg6q-OmVFv3hkhoLF29mb5aYZTtcxn1Yj97CtQJtEvRbjSQgV5-X9hOOkOcNb7VtRGLLl4_33ap5tcndkEKcykgiKw2BeRaZNmYCVyk1eKLOTPbgt47U7Zu2NH4y0fQ2-oCWRoZLCRrVwYQCNA_XwBjCA4ZcZ1qcnoieVctPG1V_i6koDjckRRYM0gBE6qNlDzPYtl1oMiCuBeDxpbvDw_Hn6cFHpcVm6YMMNZdV7ED_4fUAkaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz3mGaXJdZNI6VlCmfN1Bq8_GV0rsQY5Wbfhog7IKWm5iHwuXNwI4xB-GsbBZ11vZHR3W16DW22AkPDydUzaEAOOeDHaZSOpLvL6ghChnGDQd8hZ0r955RY1Nmi4ayzBNK_rSy7fMW48d_Qb8g5ZjkyI9zTNzwElEiueTFPy8X3s_I-EiF7K-mHNCkJ36oqUFCr9JSp54WpdBTounKSHMO-NKMNt62K74xkknjgOPGKONtng-7VblSXzf9A0jeAlmFWc9HMeStOTID7zMAJNQy-AD0TiRfmVhH4wJGPTV22Vx4nBN4Ww15WvpzqhNMO6suNfBb2hO7GDMFznxiAZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKcLZ26qbQAM0fYimWK4VSeQHYof-Hny-y7Uvm4RQV9gzuBcHgV-3F4AO9S3ZkpdzT7IWjaXkXRGTN-u8JbXXfTMrQacog16jCaiitWN2qsZKk8Ixm1WNxGOHs-jiT87ZkWWffsbFHIA42Hd_9HBv3bk_zwVw9f9k1Yr55NNEjN5hZV-ovY-zTVuTQeWdlygWB6khT5kIwjWTslTp95YhSC0k7GPscNWCDvFUOFLSmNMElMYLBc1_B4uuJ4fyieICWV7UBKnFlHgYk08vOfZ-xESETBg5BfERL0vcZ_R8e8sD0DE7q_QwLLMVk34l9HXTi-1Tpr4EcHhKPUl7LKH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kOr2KTwjs0wZhl2aE7VP2n8EDoXTrcpLKN9Mj1leCKsfkEuUTyM9zLKO15Gzp8ybT5ennhUG7nYGIuV_bHPc7OqCCrsJlLNB2S0uKaEpcRlZuj6LIj5r8haT0UIb_RQYpwmns6Z_i_KsPYf_iZMSd4uSdgPQtfT3HstWvvGhbgmu4DnLguanwFF8C1jVpNg6O-QLFyrDzrCuQzBzE36DxVAUq07Cgh-XC8owGVMXS0cvug55Q-wplWIZ_vA7NftYQpF7wdgR_n4PHoEgiUVlySInjKtBSOc0snCF1uBO3ZicGn5RrVFGKOVAYWOY8RcwuGdZ1oxTzxFFbeN7P6qFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxIjeN7XBmsqFexJmzlIqwOmdrg7dxyWZpCdb8dBT0A24TBn7fkR_WaV_QbcZVJPam7112She55dwELLp8y9RzlbU5efvM-wRUG_pzNzzM1ifWrbJx_IR2p2T85za-RjUPEj4_gHfSqtYsbnNPtFCCHaoTnxpxbza2gzQt2m5sH_y6AJ5WQr8WuUZzw8qf1mHJzESE5NhfbstPQ8wCOHrsRC8vZp1hayf-TM63ghcT_LBV348u5E3yiubr70qdPs0Ia_fztBA0qpYz9k2-iag0QSGgqC9Ee4rf76ZRT9Yio11EEchosM9BfHB0zqia6x1AASwWFt2TLcCnn2yng1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKxfqv_k8IX-eImhunKujuu7LmFpukRuWhKUOI3nzZOmmHgvks0v2SEtXe1SLZRYjbwjdieFO_r_amdkxUCMsBZQe7Af-ZsJwu6skRk8XugCr9BEHRVCje233CsZ08L_2_6U1cITyP75iMkXJgpPYzPGANA_wGeYNi-VudE2Jj55m2nLrHlLBoAZaVk1Wpbc2vHtAvQNO-BpZYY1uHw03XacGF-_M2T024h9QMaatF4BcQpkPK7M3Y2oApknpEFhru6rvgynmVyV1AozG6q04609sm0h9YESDl8n-Y2zqUzPPeDzDaA70YyUM58cv_bLknBI_zW7GWLe2pG83pr--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFfNIPmvLWNZJaZ2RirZPHXPqOK3I63xKisW7zgo35ABX57se64Q59-rM4cCFBfs4H2HGGwJAKSjF25esmUEiOXQ0XN5NacPJ8GkY_1uVFU_fgWUmp2YAGoQT00uaKhmtasGNRBRR7_Cn8XFzXgq_SC1w4t6ownzjsoN9E5ThmRmZAAUUXGWp9hQ3KzW95Eel9VG1pRDOrI9rTekifvJcrP51KRipC8Dcl_xlYxuHFwjcz57jw2Q1pFof7sGwKtitDxyVJLIlAsvNn6NGNuXkj8zUkYw0CXEdd5qmXPgItUAWxPC574h-Z87gPpIeAeLEza7VFvGf-QgAtPqRrfaLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار روسای‌جمهور ایران و قرقیزستان در حاشیۀ اجلاس شانگهای
🔹
پزشکیان و جباروف در این دیدار، ضمن بررسی آخرین تحولات و روند همکاری‌های میان تهران و بیشکک، بر ضرورت بهره‌گیری از ظرفیت‌های موجود برای توسعه و تعمیق مناسبات دو کشور در زمینه‌های مختلف تأکید کردند.…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/459205" target="_blank">📅 15:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459204">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuYrH_3NTZs86x3OHoa-sBnFwW3KShD_ulkxnOoZPq_Ei01kF_WCJJb0PdjJTsgQlNhZKgEX0sJ9mURBLavBePkYKE2BEvyIoEsLFmuyHfYOzFEFysfjXLXw11Vap5T6swA6OKWm6Go_oyVvs7slMZlO08SgZjEQZ43mRObYHmSC7bxzKoUkPI5aMzy03H_91B0HheRmy9_9Bs6U7blWFv1Ge5yRU0c4hTCv3IN5hjN1G5sR1VmlantGI3OqPy4yfRu4-CR1J8PQkyEDxs5lqwpj5ye_xxd1gPMU3N0fZjREScwzhjFf7WawRhaQHepon57rTxcyCPafyG_b9Lya4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراض به حضور بدون حجاب در جلسۀ رئیس سازمان دانشجویان
🔹
برگزاری جلسه‌ای با حضور رئیس سازمان امور دانشجویان و مشاور وزیر علوم با برخی اعضای شوراهای صنفی، به‌دلیل حضور تعدادی از دانشجویان دختر بی‌حجاب و انتشار تصاویر آن، با اعتراض جمعی از اساتید و دانشجویان مواجه شده است.
🔹
بسیج اساتید دانشگاه علم‌وصنعت این اتفاق را مصداق عادی‌سازی بی‌حجابی در محیط دانشگاه دانسته و از وزیر علوم خواسته نسبت به عملکرد مسئولان مرتبط، واکنشی قاطع و فوری نشان دهد.
🔹
منتقدان همچنین نسبت به انتشار تصاویر و ویدیوهای این نشست از سوی بخش‌های رسانه‌ای وزارت علوم اعتراض کرده و خواستار بررسی ابعاد برگزاری و نحوه انعکاس رسانه‌ای آن شده‌اند.
🔹
مطالبه اصلی معترضان از وزارت علوم، شفاف‌سازی دربارۀ این جلسه و اعلام موضع رسمی درباره نحوه اجرای قوانین و ضوابط حاکم بر محیط دانشگاه است.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/459204" target="_blank">📅 15:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459203">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhccRSTzmFms1pwFcbx-ydU3ocP9x3WAuDlkC7Rsl92qhq3cswz4SA7yqzPI68sOlk0m2_yRP9gQML0k1PYr5ZGnoO3-hwDHXLmvPjBUdRh3wkB1UE8kL9oWSqGIq--CIUU_fQwceYwYhxiolbfzRYCJa3CI07kmolNzby2D_0I11UpZbGwvI-9QCj36UYig3wKMTltB1MVFLOcVJuR04FW219E-phjdC_qRuILl5cet-twwmaJCP5AztSTzcEY3lIjfuOrrfoJS_kHD1s_zeTpjnWWiJt5Rx11_8O1uY-IwvxVTzeEG-UUap9Y8xMDPXLehdUZvErv1Of7AA-7E-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ادعای ارتش تروریستی آمریکا درخصوص حمله به لارک
🔹
سازمان تروریستی سنتکام ادعا کرد که حملۀ اواخر شب گذشته به جزیرۀ لارک را با هدف مقابله با مین‌ریزی در تنگۀ هرمز انجام داده است. @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/459203" target="_blank">📅 15:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459202">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af54082f9.mp4?token=ddwTdUUZZygxjHEDl45rvoplzl-S2ppda4Iju2VU4ioKtRSIIwrWDnF-wDSbNI6kbtULA7D0vOJ98fiongwMDYjY-B3dL-UHhbaFgmgEmFTVarzjLGXiDECku1W3Y3X2WtIFLE3C4HKkbY30M2kIS1hLYQGmhcF0smlYrg-E_LUHw47vZnQLXxSRtG5h7ZBEHbwvucGr_YwQZULPsxGHk33Ma-8zzZ_8Q2rU-Yy5WE5BYYYaACYPbMqIUdKdHdb-H7UWNTxyW-vfXR-6VtTs0uWUhUF3dKJRMaeRqhV6i91PvNxRgDu_9TYd_SYn_cqlGYejn7CX7a1jgbY1zZ83YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af54082f9.mp4?token=ddwTdUUZZygxjHEDl45rvoplzl-S2ppda4Iju2VU4ioKtRSIIwrWDnF-wDSbNI6kbtULA7D0vOJ98fiongwMDYjY-B3dL-UHhbaFgmgEmFTVarzjLGXiDECku1W3Y3X2WtIFLE3C4HKkbY30M2kIS1hLYQGmhcF0smlYrg-E_LUHw47vZnQLXxSRtG5h7ZBEHbwvucGr_YwQZULPsxGHk33Ma-8zzZ_8Q2rU-Yy5WE5BYYYaACYPbMqIUdKdHdb-H7UWNTxyW-vfXR-6VtTs0uWUhUF3dKJRMaeRqhV6i91PvNxRgDu_9TYd_SYn_cqlGYejn7CX7a1jgbY1zZ83YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: تا چهارشنبه در بیشتر مناطق شمال کشور شاهد بارش خواهیم بود
.
🔹
همچنین در نیمهٔ شرقی کشور سرعت وزش باد افزایش می‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/459202" target="_blank">📅 15:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459201">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b89177cab7.mp4?token=e-Rme7QdGnIf_RXkOldG7NGsgHDcgk-ph6YAiWmW5zV4IYt9iJ04qepLMsIZTDqN3E6N2ltXsHm1i7W0ttgGN9i82EcRJADEI4SNkwPXzkVD02Y9UJU3ZYLmupqeEC_jbJOvvJGZDKjm-KAsc6qAR7-HQtWiYX-MHKTjMfQvTmtX6QwjhPlUr3TlEfg1k9bfWwMILzq2ehokKLVUuJeZNH8nMm15l5o6Va1ffRwKhMLNPhiTlZWHhjRtYOHKnV_14KnW5GZI6YRi4E6JVsyKjsxg6CMu4cQgQAg6QFcIqQ4X3WxOgjpFDyWjDg5Oz0NgDcxcU3mXF4oIaD3RFglYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b89177cab7.mp4?token=e-Rme7QdGnIf_RXkOldG7NGsgHDcgk-ph6YAiWmW5zV4IYt9iJ04qepLMsIZTDqN3E6N2ltXsHm1i7W0ttgGN9i82EcRJADEI4SNkwPXzkVD02Y9UJU3ZYLmupqeEC_jbJOvvJGZDKjm-KAsc6qAR7-HQtWiYX-MHKTjMfQvTmtX6QwjhPlUr3TlEfg1k9bfWwMILzq2ehokKLVUuJeZNH8nMm15l5o6Va1ffRwKhMLNPhiTlZWHhjRtYOHKnV_14KnW5GZI6YRi4E6JVsyKjsxg6CMu4cQgQAg6QFcIqQ4X3WxOgjpFDyWjDg5Oz0NgDcxcU3mXF4oIaD3RFglYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌رهبر انقلاب: اتّحاد، دفاع متقابل در مقابل کفر و همکاری مسلمانان؛ ۳ گام برای رسیدن به تمدّن نوین اسلامی است
🔹
درس مهمّ اتّحاد و عدم تنازع، درس اوّل مکتب اسلام در مورد نوع مواجهه با دشمن و دوست است. امّا درس دوّم آن، دفاع از یکدیگر در مقابل کفر و درس سوّم،…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459201" target="_blank">📅 14:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459200">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672186ba86.mp4?token=QhcMwQ3hLSVRVrV3meUCTIhpt4I_I3EZaNO2UPha9OU9rwge2CuKyFlUoUZK2pzuH17PzNQu1xT4MxA1cUYyGNljkaomapp_DnawolC4xZfhNy3tuUKKFVuxfzpb940u53udgRaNO-CN_zOTeKQs-YKaZAxC7wU3hC58d2KpWJ5BKyXq6v8MKi8szvieNvJLDYObykjz9L57plwzHzQlseH4VE4Bvfw3uxZQ4RD3zcdGTeN8Iy7jrUDJLKrR9f2LJJQPYUoTRSgXol0HoDvjdvK1AOZsqepgVfzYYlLtnIubM7HgUrPjxKZ_uXJ46O9prHW8nRXQAbbW7DoIqN_RX3F2p4gNGOijkUfaV9PePc-2OB6OUoFETCYxADUUWJN9Rl3RMhCPxwJbGGQ1zV2XbDwR7vyBP3ZgCoIgnv1l8A0-dQ7I97fE9j6oWe1lo0IUYqUnyBTG2P3qn1fnIsEj3gM5qefvhE3884R7i3qslc6_WhO--ME22HFsYkx8EqbU4GlroSS7zexA70OK4gNIsa8BI99PMlyhNFjrUZAacH3e4GOGzVeKknVc543e50FLKBPbcH2AX8CkRn3zcpTh2Gk2-n8WQTumMyccUqMDUMunC9rBChhoos_YzwvzAhMnSz1wKFwizWS7LyvZltdhBx_G029Gqv5_Iignux9Ck44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672186ba86.mp4?token=QhcMwQ3hLSVRVrV3meUCTIhpt4I_I3EZaNO2UPha9OU9rwge2CuKyFlUoUZK2pzuH17PzNQu1xT4MxA1cUYyGNljkaomapp_DnawolC4xZfhNy3tuUKKFVuxfzpb940u53udgRaNO-CN_zOTeKQs-YKaZAxC7wU3hC58d2KpWJ5BKyXq6v8MKi8szvieNvJLDYObykjz9L57plwzHzQlseH4VE4Bvfw3uxZQ4RD3zcdGTeN8Iy7jrUDJLKrR9f2LJJQPYUoTRSgXol0HoDvjdvK1AOZsqepgVfzYYlLtnIubM7HgUrPjxKZ_uXJ46O9prHW8nRXQAbbW7DoIqN_RX3F2p4gNGOijkUfaV9PePc-2OB6OUoFETCYxADUUWJN9Rl3RMhCPxwJbGGQ1zV2XbDwR7vyBP3ZgCoIgnv1l8A0-dQ7I97fE9j6oWe1lo0IUYqUnyBTG2P3qn1fnIsEj3gM5qefvhE3884R7i3qslc6_WhO--ME22HFsYkx8EqbU4GlroSS7zexA70OK4gNIsa8BI99PMlyhNFjrUZAacH3e4GOGzVeKknVc543e50FLKBPbcH2AX8CkRn3zcpTh2Gk2-n8WQTumMyccUqMDUMunC9rBChhoos_YzwvzAhMnSz1wKFwizWS7LyvZltdhBx_G029Gqv5_Iignux9Ck44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر لحظۀ شلیک پهپادها و موشک‌های بالستیک در عملیات تنبیه متجاوز با رمز یا محمدابن عبدالله(ص)
🔹
هدف این عملیات زیرساخت‌های فنی و تعمیراتی و محل استقرار جنگنده های دشمن در دو پایگاه هوایی آمریکایی ملک حسین و الازرق در اردن بود.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459200" target="_blank">📅 14:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459199">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27809dd9eb.mp4?token=LbYhTHk84NCx-u2Jx1yefNw97YUoPjHZopxfS3TTyvZ97rtE75Zh1gFDux4adfZFFdSpzs5N421k9vuwLRgUUUj1MvR0vDf-Afd_Y0sXP4jHDH7sNiNsx9v4mnHl6do_FEyH3VmumL2fyzol1cKHQTH-mhc7S6TZT3rEetP7kptsklmz2UuIGQ0zY3pxiqnSiU75ydXRrsRTSJ6qOw5faqWt7E2jYaJ3pO-KZ5ieNhN3narEiPc-LES8RPKjjh1dSIocwQgfzmTal_F-OK6AOaqoefae_0hvp_lrbSsksa8A3Db7xQyMOZS4FjkaRxWClpnrOtFCRPokpQ-SCXU35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27809dd9eb.mp4?token=LbYhTHk84NCx-u2Jx1yefNw97YUoPjHZopxfS3TTyvZ97rtE75Zh1gFDux4adfZFFdSpzs5N421k9vuwLRgUUUj1MvR0vDf-Afd_Y0sXP4jHDH7sNiNsx9v4mnHl6do_FEyH3VmumL2fyzol1cKHQTH-mhc7S6TZT3rEetP7kptsklmz2UuIGQ0zY3pxiqnSiU75ydXRrsRTSJ6qOw5faqWt7E2jYaJ3pO-KZ5ieNhN3narEiPc-LES8RPKjjh1dSIocwQgfzmTal_F-OK6AOaqoefae_0hvp_lrbSsksa8A3Db7xQyMOZS4FjkaRxWClpnrOtFCRPokpQ-SCXU35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نیروی دریایی سپاه: یک فروند سوپر نفتکش متخلف در اثر اصابت با ۲ مین دریایی دچار آتش‌سوزی مهیب و به‌طور کامل متوقف شد
🔹
ساعاتی پیش یک فروند سوپر نفتکش متخلف که قصد عبور از مسیر غیرقانونی جنوب تنگۀ هرمز را داشت در اثر اصابت با دو مین دریایی دچار آتش‌سوزی‌های…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459199" target="_blank">📅 14:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459198">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a5cedaf0f.mp4?token=oNYUw4iAl8w46sOu6x3D9UB0vmq2zKBMFhHWjp6aWloa-j00gIbGVP14k7_NLT3trQCmXbKV3ahipUx4407gaLy4CFC0ygif5Iw3e56ceclEHjC03evsNNgIG3Xy8pYVxYcpdkMLpJ6rOKWdkMnywDFmAB8QlvZeMLIfRgJKsNydodW0vVRyVFLdgTULjr-6fEHon7GnBVFrCK-KvEXPQ7gkYOIY25Aio7vLqO3t7jHQ9pdapD_40PXJcyg3JTon_EZDHo4eSCzZYAviWzbL1IXFb_fPoGgDBDthhIUCNEL9tWl3HIDMAvFDTnyEid3-inqvYaT_RtbAcXCwo2pAsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a5cedaf0f.mp4?token=oNYUw4iAl8w46sOu6x3D9UB0vmq2zKBMFhHWjp6aWloa-j00gIbGVP14k7_NLT3trQCmXbKV3ahipUx4407gaLy4CFC0ygif5Iw3e56ceclEHjC03evsNNgIG3Xy8pYVxYcpdkMLpJ6rOKWdkMnywDFmAB8QlvZeMLIfRgJKsNydodW0vVRyVFLdgTULjr-6fEHon7GnBVFrCK-KvEXPQ7gkYOIY25Aio7vLqO3t7jHQ9pdapD_40PXJcyg3JTon_EZDHo4eSCzZYAviWzbL1IXFb_fPoGgDBDthhIUCNEL9tWl3HIDMAvFDTnyEid3-inqvYaT_RtbAcXCwo2pAsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در ادامهٔ بهره‌برداری‌های دولت چه طرح‌های جدیدی افتتاح شد؟
🔹
چند طرح صنعتی، یک کلینیک تخصصی و مجموعهٔ ورزشی کارگران مرودشت فارس
🔹
ایستگاه پمپاژ نیلهٔ خرم‌آباد
🔹
بهسازی ۱۲ کیلومتر از جادهٔ گچساران به گناوه
🔹
نیروگاه سیکل ترکیبی ۲۹۰ مگاواتی دالاهو و آبگیری سد کبوترلانهٔ کنگاور کرمانشاه
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/459198" target="_blank">📅 14:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459197">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سبد معیشت کارگران دوباره روی میز شورای‌عالی کار رفت
🔹
صالحی، عضو شورای‌عالی کار: در آخرین جلسهٔ شورای‌عالی کار، تشکیل کمیتهٔ مزد به‌تصویب رسید و قرار است این کمیته مستقر شود و موضوع سبد معیشت را بررسی و محاسبه کند.
🔹
معیشت تحت‌فشار است، کالا خیلی گران شده و قدرت خرید کارگر کلاً پایین آمده است. در بند آخر مصوبه شورای عالی کار آمده که «مزد در سال ۲ بار بازنگری شود» و این موضوع باید مورد توجه قرار بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/459197" target="_blank">📅 14:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459196">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Chi-r0vo-eDIKykNZGtjTU8vqvf0zBd_gg-wo9u1PhZ98ENNcsofhxu02KcxoRFKPlGARkxse4kpwAfnx3wut3y_jlDq4Gx4NZ0RxWJvwT0g9gpSiC3EoHp9KN21BTDxukvH4vN8OrQQWTJKYZ45c4663kkQ5AQ1tzlonoQYZ8G8rMayVfmLtq0PHhs05ZQ-XYoY6Mp9piNQ-bntK5PKH69Q76K8eezoaP6IX3acjD6rNwUozZILRc1QJ3rR8BnijVVDbjEFVPxlrsO0nXLqEQBwNSAJZZvT2C6fmBMoXMM47u_hJkgx_5g4f8ihGqNytxcGpzZQKzJoiKLduL-DZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
از ابتدای فروردین تا پایان مرداد ۱۴۰۵ ثبت شد
💵
افزایش اعطای وام قرض‌الحسنه در بانک صادرات ایران/ تداوم روند صعودی در حمایت از مشاغل خانگی
🔹
بانک صادرات ایران، مردادماه سال جاری را با اعطای بیش از ۱۸۰ هزار میلیارد ریال انواع تسهیلات قرض‌الحسنه به پایان رساند.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اعطای_وام
#اخبار_سایت
#وام_قرض‌الحسنه
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/459196" target="_blank">📅 14:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459195">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXQ4nZ02JK5o5m0e9hQiEVqP8OcRWN-nC6iazEBwwZDs-Qyudze0VerY6RH8qX_Qt-CIqmjO-861fcw6GCgxMhm9hwExRfM3cMdUorJKO0xclyFVcnEkUTwgHXLdrZFX2h6GUO7okM8cWxKznz0LRoWeManKFyFQD5I9XuwN7dXKE6z8c-JruQ3UycvJt2x-tBgQK44PEa_Vc91GnzXTJicGQlxTC0ueazrabghRsC4n2X-yvJh9EZv7X6yzN_roWTwj7_mKAM91vhl0P3boG6H213xpaCFQxoC7_quoVaS1h7TYeI5STRQmgwn5bQTAAcEjzlt3xtjOyMKp79DiIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
آمادگی بانک رفاه کارگران برای حمایت از فعالان صنایع دستی
🔹️
دکتر اسماعیل للـه‌گانی، مدیرعامل بانک رفاه کارگران که به مناسبت هفته دولت به همراه وزیر تعاون، کار و رفاه اجتماعی به استان فارس سفر کرده است، از نمایشگاه صنایع‌دستی شهرستان فسا بازدید کرد.
🔹️
در این بازدید که با هدف بررسی ظرفیت‌های اقتصادی و اشتغال‌زایی شهرستان فسا صورت گرفت، دکتر للـه‌گانی از نزدیک با صنعتگران و هنرمندان این منطقه به گفت‌وگو پرداخت و در جریان مسائل و چالش‌های آن‌ها برای توسعه کسب‌وکار و بازاریابی محصولات قرار گرفت.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/459195" target="_blank">📅 14:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459194">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/459194" target="_blank">📅 14:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459193">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrH38S3k7xtDv_W8d-l7jo1490h0sub26AEDFbAALwkii9wFVlYu_d3_-lA2sixmmyYagJFlKRlqExVL1cU1ccExsZnj55jS_ADgxjxfepGF0JPVsLGh0VYHKGF4tktfqwz8eEO8sfMXkmXYGAZ5dTLhhuzcAEN5GZb1GLZMaeaB6CNKUaj352DzpAuO9qFnrylJsXvgqEoE_Jfx1Wq_qz6hA8WeGsKUIj4ujQZ2XH-Hux_vSB_miWLr_U-U2ApHOxTbKjCdjFZ4W-VP383KkZZmbwiszzEVXqC70UTT_BjbMfUZaUzEjaX3SpZPOy8-JFPoqvDi4MdPSYgh0Yx9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: در داخل آمریکا جریان‌هایی وجود دارند که منافع خود را در تداوم جنگ می‌بینند
🔹
رئیس‌جمهور در دیدار با نخست‌وزیر هند: ایران هیچ‌گاه از جنگ استقبال نمی‌کند، مسئولیت ما ایجاب می‌کند مردم را از خطر و ناامنی دور کنیم و زمینه را برای دستیابی آنان به صلح،…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/459193" target="_blank">📅 14:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459192">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlNUmf7wwhvXvIzhqZgiNjvSZhKLGVB0DwhhOHHMxUqwWEJzz5AKvwE4uf1fzZxOtdLd3IRXoTMCxpCY8odlXG_0cSZ_orH7KDjGe-bse-JF2hWpx-YMdkvmDJgqmLYIXbsNFOW0ngBsddhWeZpunOXmCbuqgugSxYn88WL1JRBXTu5axjWhRTXxXrO5Z04uSHDe-6YkgXTtvnRodsFunI03Uh-Oy5hBX_CiKJzCb51Y5xDDx7unuVf-9PFXtYVZrOxDCd0oDuwJkEWcOEJgEg5woiZTe5GPrg8eIRdF-MxhEvYck_Y0h1_78oixn9tx_-H9AyBI2OkROlWsqluTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروازهای فرودگاه‌ بندرعباس جریان دارد
🔹
اداره‌کل فرودگاه هرمزگان: پروازهای فرودگاه بندرعباس طبق اعلام قبلی درحال انجام است؛ امروز پرواز دوبی نیز برای اولین‌بار پس از ۶ ماه انجام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/459192" target="_blank">📅 14:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459191">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c01e2eaff.mp4?token=PAvDdBTUOeWRVE1_0lupAZbxLB52ywDP5ciJ9iiqv72xgPhmQwuW3Fxl1Plcvf19S4MPpe9ssNnrvJhwE679m3yuEcgPJ2tLW52ShLCwTQI_sYsuz4-ib24Q6ImqpeAX5zBDDbBe1lXZiV-8ebfkNqwd-QFGDNxAdQVVyHQYIdM-k2VS6aJlhxcmO_RWINiIgX4mZVOkkaTX0zV_RQZQ_oeoxlhE7imj3-oaE7HDwEJuQa18XtEuAIi_US37XFEC4X6HMuByx4eUPCTC3PjcECR01AlMFDPcCmjbfj-YLTtHdzTjJPJXSEOKtyd9LhUogkgcac8cuwsRQnts5_rOGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c01e2eaff.mp4?token=PAvDdBTUOeWRVE1_0lupAZbxLB52ywDP5ciJ9iiqv72xgPhmQwuW3Fxl1Plcvf19S4MPpe9ssNnrvJhwE679m3yuEcgPJ2tLW52ShLCwTQI_sYsuz4-ib24Q6ImqpeAX5zBDDbBe1lXZiV-8ebfkNqwd-QFGDNxAdQVVyHQYIdM-k2VS6aJlhxcmO_RWINiIgX4mZVOkkaTX0zV_RQZQ_oeoxlhE7imj3-oaE7HDwEJuQa18XtEuAIi_US37XFEC4X6HMuByx4eUPCTC3PjcECR01AlMFDPcCmjbfj-YLTtHdzTjJPJXSEOKtyd9LhUogkgcac8cuwsRQnts5_rOGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گلهٔ میش‌ها دل به رودخانهٔ خروشان لار زدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/459191" target="_blank">📅 14:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459184">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQTOzD4Aqag_kOGgk4v9sWHaCtXVnYMIf1TdBZJkeJa9GTKqFHqQFPWIqEedY5DcJPJtarc8bq7pFgq7lw6xx4VCbc4uSAlCmDwXDEayvIB7zrTD7e1uZqGB9SVhGDg1CE4d7_FVjvQTM81YePLr2cnvf5g3wnbP-byWkDUnfJLpKs_IJOgN3yXsv0qFKIbovS2Hd2a8YRnpDKcWKzpKRjOn1qWFpgDqfejp5io2fS3CxkJPNAYiaMvwGKpU9zuZdHhTfvjAdQZf0MT4c7C_aHPECCxwsuSL7o_BDhlKYihVmAF6i9rh2iQGHUgJGIr8w7cHXZ_EeYsWpyO0aelwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cv2CLtMRFKtz5a4E1zfG59lqAK3KkIOZQBdTJzlkWjdZiW7wx1GEsZryypbpsmNzMKzVN4ruo1iyVtxjlxpZtxU7UQulpuddu35sZjMN5HvMifDGz_j9twYmqn9d_yEgyKFiuayh315O4ueBgaVWGDNEs0CC6HcUnXhRjqJqKYeF0qDS2gbBM_wOdii389VBKFMyOGEDifCVyhrLJ0BnUzVwdZ1JTb6vGGYVDawosnTTiaOCutGe_VcX1O5SGnGJ33L2Q_mmhiAIrSkk3IqbwOa04AwabwHLyz5h18bTRI6LB6HiT-qazs7_OrwmoWl-w2yF76ct2bSo9myBXjQEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oi04p_xttlGmFjkJLB4LQgKgacvZ2GRR5z9gjjGI7v5gAoKoU0FBCrVaSLV8AeaOoX6mHtqQPkXCt_eZ2XPHdvIlutQfHxWYTJfhDf0JL37XoEdW6rgLiY3MrPykXn-fwzlHJhG5a3s_kn93Z79fRRfBX7xhnRBlwdVLG8_gliHbUhAKFpNU-_TLpT5cmXWF9u6gn-mPmuejo4jdWQcwFqf2XrR9x01SVGSehmfY4lKxBfi0ceFvwQfR-lxodasU_6oMiZsbnnRksJDmYsw6ZII2KByov1X6rAy87qBLwKA-T2SnL_infQqUYQj3KoOpVZ_AIjV9AVLlysapUN36qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myB1_kWom6DdGFi3qVPuw6EeYtdq_njtUynCdLGxoCGjGfHi9Zalv649FZIMs1FCbqcs_Es2Eg5iG6ARZ6S6-rh6ZQKUmPty-urbN3JmzRttEhrYQiY0sVMoFbWg_j4xH7pzbIfoUQ7CUVL0mLktyxQKXye4nI5YsAV0Zf8HSKgFEjmh5XztaH13j2s7ebUXBk8DaVyK0Z03W3KXM0TyWKjfGeEPOgPQ1vH90-_Z0qgZ8CA182MwtIpSwT0wqS7HFhzMDt4UCbo83xp9YGQKBEUFP_H37kWIPohAewkheUab--RktkX002g0Ic7TeAqPbgSIADtP-6MV7eN78Bi7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOJWGBlDFufQD8r9mnSsIRRvpLmB5ilbDMy3-BPbXZTN-Cp__wEup8CFrumGmqhYv1k64ajTt7Ic60zX4x_zHgag9R1ysj5t2fR20aefV0lFBf7Uj1IrEqg8jQZ5Wpvavl3feGK81sZA50SOsxhXSI2gQ2SHMXLfXMY7SiOyLCszqrQp0WEHQgch6toaD90jWWv7k_UzzAvncGv0ELPkzT2wh3k2DRHsZkqfFflcWmLs4qWBEuRVhhP4Zbqbg1Xzem5OgRa2FmIgduskqQjzabA-FtZ3MplxRQmYCen1a7Acuuumbrs96JsM9s6kOq6neU9taCMXv9X-logRGDEO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BC0Z6bVCYzizk3m0cHIBKv4sUf5CWHtCfJtoWVgEH9ThZpdr598xV1WnUTZWtYvOVGwxWoZiO6nv7TEwyeGTDJTbytpqLGprvoDJ_rSUF3s3tTRJEmoEViWd1r_4M5W_gC2HfgW91VQLUEfqwIxWJ7m8FNJgDDXBE2l1L4W0Yww69Tg0AeLylFmycMMTEFJQ-gg3NN9jNXFlsEeLB5h4XNrW5w-b8o12L6w6q6yfWKslH2UgIjO0TCLvx_7BcB07ZTB6YJPyWE7MYeFjtnJJnIUCisxcLMuQWQ8rOQK_2oQQMWWRhby7KxkIgjFIlNJOmYyp8z9MhHZRnK5fBd5p7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yl2DpyI5-8P0Nuj5mk_UJjpTBa1onAIhUPJP71w0beGG617DShn-wO0Fk_NyYBUkW5uom8U0bIHhzYFDb423xw6zzB_bfiWeyQMXSTQSz1IDwySPQQ3PyBABY_apqdh3PxWB41w-aaciCtC3Z86yKH5DaFaF1UX5q9OkRx9uP9N3q68hnHCKOlyL-qPCUXlTev1SFq93WrGPGOHhcLAsJr8GktyyKBT4CbH--FJKKFfg0eAslnmRa5g0EBOfKF_1LKTVUqxlt5Dx1e_Q0V_glWTEbLd3taOw1VgnanyGxJCru7Qq6ONq_TYp3edBLG8Lo51vkqyrBSXqeL7Wcj8qzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار پزشکیان با نخست‌وزیر هند
🔹
رئیس‌جمهور در نخستین بخش از سفر خود به قرقیزستان به‌منظور شرکت و سخنرانی در اجلاس سران سازمان همکاری شانگهای و نشست شانگهای پلاس، با نارندرا مودی دیدار و گفت‌وگو کرد.
🔹
در این دیدار، طرفین ضمن بررسی آخرین وضعیت روابط دوجانبه،…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/459184" target="_blank">📅 13:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459183">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b6bbf0bf.mp4?token=IART7emwNYqaRySaRAGV99m_GQts9OmEIFbVD6JgzZaV8iZEUlMPZWenUjn27F56qGlzcsg6woJyORTYrAmYywOJW0jTAScHIn7YjIc-4LZ1tWEsvShMIft6Odj86M-jumY_BcQ-kTbc0bbVtdHmah18BT-abePJcdKRGyYwRM_xyEOtNVizYPJaacppseVbMQDbV14M84ckTB4xDuaTXs8amVBuXROEOCiWkAbAnSFCZexicR1Bb1897A7X58h8J5-E-d1Kt10CIVdrSJn0iKBO2dowp-7zoVoMnSxy9Jc9pDxeMRaYyv9vjGc6MO7VpB_we1CuESRLvvgFOjUh2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b6bbf0bf.mp4?token=IART7emwNYqaRySaRAGV99m_GQts9OmEIFbVD6JgzZaV8iZEUlMPZWenUjn27F56qGlzcsg6woJyORTYrAmYywOJW0jTAScHIn7YjIc-4LZ1tWEsvShMIft6Odj86M-jumY_BcQ-kTbc0bbVtdHmah18BT-abePJcdKRGyYwRM_xyEOtNVizYPJaacppseVbMQDbV14M84ckTB4xDuaTXs8amVBuXROEOCiWkAbAnSFCZexicR1Bb1897A7X58h8J5-E-d1Kt10CIVdrSJn0iKBO2dowp-7zoVoMnSxy9Jc9pDxeMRaYyv9vjGc6MO7VpB_we1CuESRLvvgFOjUh2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: امروز زمینه‌های پیگیری مسائل قضایی برای مردم نسبت به گذشته بسیار فراهم‌تر است
🔹
اگر برای گرفتن حق مظلوم از ظالم غفلت کنیم، اولین کسی که ما را تقبیح می‌کند، وجدان ماست. امکاناتی که امروز هست، با سال‌های قبل متفاوت است و می‌توانیم از این فرصت استفادهٔ…</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/459183" target="_blank">📅 13:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459182">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5f5ca006.mp4?token=T7Oq_jZrNaPloTH4uuCc7cjvP2-1tIxzULjAeYpY7Y1yFqOc-XNMFaXNpyCBPBvA-CFd9mgHQ-cxvwt5ENFZ_aQwgtlbwEg_qEiV1wiSM-0XwMqtd9csL4sMQHMBxVG4aNG_9H0axfqe8POvUXqjto8dwZHnbk8YV6_gFKd9jt5GQ8LzjStB9kLFTsZ22KpWL1Y6GdggGVhHDLwHVuelZ94RhHcJGqHYCTxJ0q4AZNoclZ64b1LYjYifqLSrPlDcBz9DDUPavgTtm-qdPn8Ry3oBDkrYydsy4jTfGAd_EMBVMe86qfrfJURQH91TtX3KIhtYf10JurdBaVvL8EhofA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5f5ca006.mp4?token=T7Oq_jZrNaPloTH4uuCc7cjvP2-1tIxzULjAeYpY7Y1yFqOc-XNMFaXNpyCBPBvA-CFd9mgHQ-cxvwt5ENFZ_aQwgtlbwEg_qEiV1wiSM-0XwMqtd9csL4sMQHMBxVG4aNG_9H0axfqe8POvUXqjto8dwZHnbk8YV6_gFKd9jt5GQ8LzjStB9kLFTsZ22KpWL1Y6GdggGVhHDLwHVuelZ94RhHcJGqHYCTxJ0q4AZNoclZ64b1LYjYifqLSrPlDcBz9DDUPavgTtm-qdPn8Ry3oBDkrYydsy4jTfGAd_EMBVMe86qfrfJURQH91TtX3KIhtYf10JurdBaVvL8EhofA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: نباید فقط به‌خاطر مسائل مالی افراد را چندین سال در زندان نگه داریم
🔹
پرونده‌ای را به رهبر شهید گزارش دادیم که دورهٔ حبس مربوط به جرم محکوم تمام شده بود و صرفاً به‌علت بدهی در زندان بود؛ ایشان فرمودند «دربارهٔ این مصداق، حتی اگر شده از وجوهات بدهی…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/459182" target="_blank">📅 13:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459181">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سفر هوایی عتبات متوقف شد
🔹
«کاروان هوایی نداریم.» این پاسخ دفاتر زیارتی به زائرانی است که می‌خواهند در شهریور با هواپیما راهی عتبات شوند. مدیر دفتر زیارتی می‌گوید «ایرلاین‌ها حاضر به فروش بلیت پرواز عتبات با نرخ مصوب نیستند.»
🔹
ثبت‌نام دور جدید سفرهای عتبات از حدود دو هفتۀ پیش برای اعزام تا پایان شهریور آغاز شد، اما کمتر از ۳۰ درصد ظرفیت به سفرهای هوایی اختصاص داشت.
🔹
درحالی‌که ظرفیت کاروان‌های زمینی همچنان باز است و هزینۀ آن از حدود ۲۴ میلیون تومان آغاز می‌شود.
🔹
با وجود اینکه اعزام رسمی هوایی نداریم، برخی کاروان‌های غیرمجاز همچنان در حال اعزام هوایی زائران به کربلا با قیمت‌های نجومی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/459181" target="_blank">📅 13:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459180">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d672c27b11.mp4?token=j4fAOuNqoXzG-ar5C0tq9G-SQjKoEnfCjzKIyXfy-VlOkUVEcEtBXS7B_PXL4xQ8RbhwkJ9X5xjgesTJ1EuYr6NhKrsrriJ30o9jbqJLgfUA41t6y5E-uaHZ621AuawOwDP-Y_najzV9Po749eVp_-a5r6xwWMolH8IcXPw4wsrSBX5kO2PPlFpb-Uak7S0Ywc1NFYjG1gwY6rVA2ox_7yW0iuHErIcT-sS6lmujBcDBQ2smaZRM0z8pGtDNtr627nJm33qwFPSTHKW2YbnoUKEHjURqQ-SJG-DBC_J4WVOwnRnq7FBJh6nPpmpFR7H5r6opmQHVniVghafCs6dDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d672c27b11.mp4?token=j4fAOuNqoXzG-ar5C0tq9G-SQjKoEnfCjzKIyXfy-VlOkUVEcEtBXS7B_PXL4xQ8RbhwkJ9X5xjgesTJ1EuYr6NhKrsrriJ30o9jbqJLgfUA41t6y5E-uaHZ621AuawOwDP-Y_najzV9Po749eVp_-a5r6xwWMolH8IcXPw4wsrSBX5kO2PPlFpb-Uak7S0Ywc1NFYjG1gwY6rVA2ox_7yW0iuHErIcT-sS6lmujBcDBQ2smaZRM0z8pGtDNtr627nJm33qwFPSTHKW2YbnoUKEHjURqQ-SJG-DBC_J4WVOwnRnq7FBJh6nPpmpFR7H5r6opmQHVniVghafCs6dDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: دشمن ما عهدشکن و جنایتکار است؛ هر روز در لبنان جنایت می‌کند و روزی نیست که مردم جنوب لبنان و رزمندگان سلحشور حزب‌الله، به شهادت نرسند.
🔹
دشمن مطمئن باشد که فرزندان ایران اسلامی، انتقام خون‌های به‌ناحق ریخته‌شده در ایران و سایر سرزمین‌های مقاومت را…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/459180" target="_blank">📅 13:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459179">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0911fe42.mp4?token=XjFUzMXuX9VVKqDJwAxV7QVRV1DzXegvKZg_BugPASr0Zd-IDhCq93-9QtqOhiQ1B98ZtllGOtMqodqq1qaUjgpr2B2z1R_IKhPdddhB2cpBgWsr68HFH31o01CWnJ5qVfC82yVx_JQFTJGZtUAU28QM_3O-4rfr2r0Ko0THgoiNBwJMg6oXmh9vpJL1ilfgY-FWTa4lwGdM6Dr6IGfugFLddaEn0TxtkTct-Rv4yZYFHlZygk8QsSYwgfxqN8_QIVoP1S-P8fEea3QQYxbIoQ-OZkjZ41j8fBDCCtlqcIrr_xr_rcBF-1OlESwtP9sXVipcocG6CVErgYB-tCgb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0911fe42.mp4?token=XjFUzMXuX9VVKqDJwAxV7QVRV1DzXegvKZg_BugPASr0Zd-IDhCq93-9QtqOhiQ1B98ZtllGOtMqodqq1qaUjgpr2B2z1R_IKhPdddhB2cpBgWsr68HFH31o01CWnJ5qVfC82yVx_JQFTJGZtUAU28QM_3O-4rfr2r0Ko0THgoiNBwJMg6oXmh9vpJL1ilfgY-FWTa4lwGdM6Dr6IGfugFLddaEn0TxtkTct-Rv4yZYFHlZygk8QsSYwgfxqN8_QIVoP1S-P8fEea3QQYxbIoQ-OZkjZ41j8fBDCCtlqcIrr_xr_rcBF-1OlESwtP9sXVipcocG6CVErgYB-tCgb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: برخلاف دروغ‌پردازی‌های دشمن، تمام مسئولان نظام مثل مردم عزیز در مقابل دشمن یک‌صدا هستند و در مقابل آمریکا کوتاه نخواهند آمد.  @Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/459179" target="_blank">📅 13:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459178">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109dcd13b9.mp4?token=AqR0VJE7tgA7kfVd-ehYuXMy7s4aEZU5QoA3rZRZCyHqhLxN5T1gmZih4G0ZX7nMFeOBWaJgokvJGlXJJD60o15jE84sQuFg-HltkCEGJ-S2X4GiycZ4D79xo1wPjJrKQZZ8Bnict6Y_3o6jXrzY2c45_O9KLd6fMokIRGTH-sZiJ536hxcFEKxTe_JGVsxx5POz5iAMLzSWIwTbVOGYd9sIKt_3vcEEfulmlD588LsSllGUtEYFAmOHSRTbG3_qQ5VaDBGYBLlEJf9dI3fhML92tkDkgZkdbRDdSKIou6jvXVvxUX8tEsyDfg8eePg7pWIQBWyoTMZ1SS19t6An7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109dcd13b9.mp4?token=AqR0VJE7tgA7kfVd-ehYuXMy7s4aEZU5QoA3rZRZCyHqhLxN5T1gmZih4G0ZX7nMFeOBWaJgokvJGlXJJD60o15jE84sQuFg-HltkCEGJ-S2X4GiycZ4D79xo1wPjJrKQZZ8Bnict6Y_3o6jXrzY2c45_O9KLd6fMokIRGTH-sZiJ536hxcFEKxTe_JGVsxx5POz5iAMLzSWIwTbVOGYd9sIKt_3vcEEfulmlD588LsSllGUtEYFAmOHSRTbG3_qQ5VaDBGYBLlEJf9dI3fhML92tkDkgZkdbRDdSKIou6jvXVvxUX8tEsyDfg8eePg7pWIQBWyoTMZ1SS19t6An7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای: قوه‌قضائیه برای مجازات عناصری که بخواهند امنیت کشور را مخدوش کنند، قاطع‌تر از همیشه است
🔹
تحکیم امنیت و مقابلهٔ قاطع با عناصر ضدامنیتی، جزو مقولاتی است که آحاد مردم و مسئولان ما، در باب آن اتفاق‌نظر دارند.
🔹
همهٔ مردم و مسئولان یکصدا و متحد هستند که…</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/459178" target="_blank">📅 12:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459177">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh80Qy6mC8W56uRfM8TGsMbu7Zp2ytQVtcNeHObkk3xPLj-hKIzVkM1qSaf_sneb1ftdnvP5lhO6EZZ545WgGCOjyiVtValvLUTafHnYX8d2IYBFBuRWqBnOAgLT4VviKdikv2gzcr2Y0A2tXjCBqKGgudbge2X1xB0wJoOIoe5nx8tZ4S1-KVkU7nLZ97TCq_Xio_PgaBdaCk4cS_2LiJR7ZO0FHAhoRLQoN9L2RZVW0gLSmUCBeuppyJP97F5Ll8dlhoK5hpDwa45i4Di_iAp0XMyEocSz3GKCFRpM7dJpm1GSZt9xt1t9F34PvYsaYe-Fq2cSveaTzAZvgst7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
انقلاب مهارتی در 51 شهر ایران؛
از دره‌گز تا سرخس
🔶
تا همین چند وقت پیش، شاید نوجوانی در شهرستان مرزی «درگز» تحصیل در رشته «هوش مصنوعی» در مرکز فنی و حرفه‌ای را رویایی دست‌نیافتنی می‌دانست. یا شاید جوانان بومی شهرستان سرخس فکرش را هم نمی‌کردند که روزی در شهرشان رشته انرژی‌های تجدیدپذیر با کارگاه‌های مجهز راه اندازی شود. اما حالا این تصویرهای ثابت و محرومیت‌های کهنه با تغییر مسیر هزینه کرد مسئولیت‌های اجتماعی شرکت‌های بزرگ نفت و گاز و پتروشیمی از جمله تاپیکو برهم خورده و جای آن را به صدای روشن شدن تجهیزات مدرن در کارگاه‌های مهارتی داده است.
🔶
این گزارش، روایت تزریق هوشمندانه ثروت صنعت به رگ‌های مهارت است، وقتی یک تغییر مسیر در هلدینگ «تاپیکو» با همراهی وزارت کار، قواعد بازی را عوض کرد و راه اندازی و تجهیز 51 کارگاه فنی و حرفه ای در نقاط مختلف کشور تنها بخشی از نتایج این تغییر مسیر است.
✅
گزارش کامل
انقلاب مهارتی
در 51 شهر ایران را اینجا بخوانید:
https://www.tappico.com/NewsDetails/981862f4-ccd0-42b2-a33f-08df05c15530
@tappico1381</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/459177" target="_blank">📅 12:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459176">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5Ph_gXhKO1to9SdHZUY4S77c6gvIluh_VBffNn1K9MJ_0-fB7Vjkq0itC9N1DP5kWEX4uMlGFDlBw76z2iLkWgD_5Lqhpp7c1uvp6vU1gy6Fi8IZut_dbWpjRm_OVpEq5WfPHWUwlJbURaY9g--cWa86bzJCMl7NmZhEb63K6eiFsBZ7-EygUXwbHHKWRCYAEVHEJYBhA5vK1fvz5OS_A1Y8TAw0K8-smr577yNdjOOUIyiedxcuFCVdOE53kRLp_k-Y-HJdRnOI6ZcDLbF4of80ZWU7Ie-2OqJneA3ZGUFvvv4LC-7YUtONHerW4kgyqpAfs3Sf188a0oVIBgWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
حضور بانک شهر و شرکت‌های تابعه در بیست‌ونهمین نمایشگاه بین‌المللی الکامپ
🔹
بانک شهر و شرکت‌های تابعه این بانک با حضور در بیست‌ونهمین نمایشگاه بین‌المللی الکترونیک، کامپیوتر و تجارت الکترونیک (الکامپ)، آخرین دستاوردها، محصولات و راهکارهای نوآورانه خود در حوزه فناوری اطلاعات و بانکداری دیجیتال را معرفی می‌کنند.
🔺
به گزارش روابط عمومی بانک شهر، بیست‌ونهمین نمایشگاه بین‌المللی الکامپ از امروز (9 شهریور ماه) با شعار «هوش مصنوعی، امنیت دیجیتال، آینده ایران» در محل دائمی نمایشگاه‌های بین‌المللی تهران آغاز به کار کرد.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/459176" target="_blank">📅 12:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459175">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/459175" target="_blank">📅 12:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459174">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-opumx5kmp3sL-_NPzo_xlhDBdPKmKyIuwReVK8Ico_oG6wFrJkiix1i3eR6N-hYPktZrv9kOKW-LpwTHZJBzD0a3YLFKM3qyo9FPHqUmPVdFNyzQxGHPheTTHYeW_iHOJXqvnGXgJFDDyQRBcLr2bB8S15x7ypuvh0KE1eP3k7QReKCoHj2BS1FaFkTsDktPiGwV-V07weEtuVaOZoH0lzmcjQecYEM3bP2s2NHOaprTCcp5xi3e4wdIm9H__Krx57Jz0KAqT0HMsl6uRk3n63YSzrKBphtzFLDDr5hpy0NjBXcql6sbuzqbZYw-EdofscQ69mq5KPUY_sC-hnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس روی خط رکوردزنی
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۳۲ هزار واحدی به ۶ میلیون و ۵۴۸ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/459174" target="_blank">📅 12:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459173">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI58Co0dB8_qsH0dDnQxljT8igJnjk8c1nysp-mFJuOwduvEUaRA6ijYwAlAWMpKv2IIM6UP_7ETmIOsd7UQ2wpwp07LWsHw0ZQdNTUNXf1AprolbwKrSr_R291IhQ8bx-gORwNZFljW-Qh8aUEnnqvSPEDxqEm1XkWz8hZE2oi2xk9_jZCXYhlMTlU9gtirYXKXO-Y57PCqhNEvFj2FV_QUwf4bcLydFezgD-ygUNYcnoKA5I76dvXctKeXF395kYa1zaMign6AYKI1ZSwjI9vuTiOmuz39mvPzrZCzJ_IXdNojCz6wgjOHZNmd2gKUkcjREbqGzXtROJfIjVfPgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۲ سلاح شکاری غیرمجاز در گیلان
🔹
حفاظت محیط‌زیست آستارا: ۱۲ سلاح شکاری غیرمجاز به‌همراه تعدادی فشنگ از شکارچیان متخلف در تالاب‌ها و پناهگاه حیات وحش لوندویل کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/459173" target="_blank">📅 12:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459172">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEzzShkEGta20qkBc5GCkHB0G6HOhVNU9KIqanrLiOB9MtUYIOYKJZG8Asp6wZDm-ZQEQYst8AfgfKxnGCjLvDs5W1H9HrcVIYlbTW1UWZoU0NyPjGfL1Nu1mLNZWOwlWz8_RRD45c0zZcGCI5Wf6uVRdHde9B8FRvwTXpwiaDSuqmQzlPBYF2qIwF4pFE1ocSmVpBJvjAnILhERPamXFCvsON5F3Hiaw-Ea4-9B-clbn_jpPc8kiPQeqZqf90eQBw54oXHOwADZpEMQOJ76lZgIwSFc71BosHGkc16ClcPLFCLyU5WQbsBAcFSfBhmx3Qqa16d8J8p8Nfp9RiiAvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: قوه‌قضائیه برای مجازات عناصری که بخواهند امنیت کشور را مخدوش کنند، قاطع‌تر از همیشه است
🔹
تحکیم امنیت و مقابلهٔ قاطع با عناصر ضدامنیتی، جزو مقولاتی است که آحاد مردم و مسئولان ما، در باب آن اتفاق‌نظر دارند.
🔹
همهٔ مردم و مسئولان یکصدا و متحد هستند که باید از اقتصاد و سرمایه‌گذاری مولد حمایت کرد و موانع تولید و مشکلات معیشتی را برطرف کرد. در این زمینه‌ها هیچ اختلافی وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/459172" target="_blank">📅 12:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459171">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae623a42d.mp4?token=Q-JL2thOJ1Fiua5m2yBEwJg4GEDyoYhfYQGOwVFtdy1bJIzqIPgUk1rvTftzEb-r5IGvW5KMhem43DY7GQao8XobzkrDQALpFADbRHJOd9_6rXWKpNkPfyia5VBXNjs2sDThMbZhl62zTLK2V6PmeYi2D7l91F1Hv6mzbFAyEcGmQM7HygL2iNNz_YO3AdcW8GuwOZFPp4d-ZeOOYIS2SOY6_PgCagNi79m5IZ5v1Gi38GJeZ5gCGZGpspLNc8R3fpm7vR37mDaRnpA21Y4yoUiagqJHNbAObDbu0_adNf-xP_sfv6wFL1MyQ72K1rGSZiKXTnJrKOp1g_XF1jfgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae623a42d.mp4?token=Q-JL2thOJ1Fiua5m2yBEwJg4GEDyoYhfYQGOwVFtdy1bJIzqIPgUk1rvTftzEb-r5IGvW5KMhem43DY7GQao8XobzkrDQALpFADbRHJOd9_6rXWKpNkPfyia5VBXNjs2sDThMbZhl62zTLK2V6PmeYi2D7l91F1Hv6mzbFAyEcGmQM7HygL2iNNz_YO3AdcW8GuwOZFPp4d-ZeOOYIS2SOY6_PgCagNi79m5IZ5v1Gi38GJeZ5gCGZGpspLNc8R3fpm7vR37mDaRnpA21Y4yoUiagqJHNbAObDbu0_adNf-xP_sfv6wFL1MyQ72K1rGSZiKXTnJrKOp1g_XF1jfgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرقیزی‌ها با سوغاتی‌ محلی به استقبال پزشکیان رفتند  @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/459171" target="_blank">📅 12:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459170">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac497cf83f.mov?token=HawaPvQyiyLC1rxGxws68YFXInjNbO_xRJx2OepWeGgLkqA9D_XBUwzU27yzy8N-wpE4dAfs5AQjd8J5eThxanYGlCGq4YH8LfHsi2ykwETsVmboNSfICPIEE6WBbzMnBcApmqQiBcJ_ZEQz2qfm-61DQ1TnwVq8F92Q7LIEfSVmO9mTpKwCLiMDLkginNUy1Up7gWDjeuDreYQgBBX8gnSPSWWZylqeT7ttd8D8htg1yPzJCOnU77mA3IOmjd16YwfiCYiwpGpG6ICSU1E4e_XR8dKeHonbtmSz2OLx80NRvseFeH6c52VZEUV7R642dPygxtB5aDr3Fzj0j1R68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac497cf83f.mov?token=HawaPvQyiyLC1rxGxws68YFXInjNbO_xRJx2OepWeGgLkqA9D_XBUwzU27yzy8N-wpE4dAfs5AQjd8J5eThxanYGlCGq4YH8LfHsi2ykwETsVmboNSfICPIEE6WBbzMnBcApmqQiBcJ_ZEQz2qfm-61DQ1TnwVq8F92Q7LIEfSVmO9mTpKwCLiMDLkginNUy1Up7gWDjeuDreYQgBBX8gnSPSWWZylqeT7ttd8D8htg1yPzJCOnU77mA3IOmjd16YwfiCYiwpGpG6ICSU1E4e_XR8dKeHonbtmSz2OLx80NRvseFeH6c52VZEUV7R642dPygxtB5aDr3Fzj0j1R68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرقیزی‌ها با سوغاتی‌ محلی به استقبال پزشکیان رفتند  @Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/459170" target="_blank">📅 12:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459169">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1575014125.mp4?token=eA8ibvPc70b_kOl0xgg-Eb-1OG8d2uhRA07I0OwWkAP5eLbytFotkJce1vzcXk7m3cZhZAul7T8atl8lpc-Oh44cN63NBXWYDoU6uA5n96RrT_Oe8TfkEKSGz5L6cQ_UOQnDYqumMWovb1B5tC8zm3KL4BptPbblKWT9rbnRB6PlTubGoS0L5eDmTLUcZ0YQ49YdC6U5AUgzcyLjA4iAz7kxvHDwPCdR6LYerzt_cXOsRnCamhtGXdYUkZWjXaQmSreDh_MNOXJ76uL_LM7HXHj1X8iErTLGNDEsuoo8DqJbqVkWmeA9naREVKE3ysQvf1kt79khmONl46zm-uxE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1575014125.mp4?token=eA8ibvPc70b_kOl0xgg-Eb-1OG8d2uhRA07I0OwWkAP5eLbytFotkJce1vzcXk7m3cZhZAul7T8atl8lpc-Oh44cN63NBXWYDoU6uA5n96RrT_Oe8TfkEKSGz5L6cQ_UOQnDYqumMWovb1B5tC8zm3KL4BptPbblKWT9rbnRB6PlTubGoS0L5eDmTLUcZ0YQ49YdC6U5AUgzcyLjA4iAz7kxvHDwPCdR6LYerzt_cXOsRnCamhtGXdYUkZWjXaQmSreDh_MNOXJ76uL_LM7HXHj1X8iErTLGNDEsuoo8DqJbqVkWmeA9naREVKE3ysQvf1kt79khmONl46zm-uxE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وعدۀ سرخرمن ترامپ به آمریکایی‌ها دربارۀ ذخایر استراتژیک
🔹
ترامپ مدعی شده که ذخایر استراتژیک نفت آمریکا را با نفت ونزوئلا پر خواهیم کرد اما طبق گزارش وال‌استریت ژورنال، شرکت‌های نفتی آمریکا علاقه‌ای به ورود به ونزوئلا ندارند.
🔹
مؤسسه ریستاد انرژی پیشتر گزارش…</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/459169" target="_blank">📅 12:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459168">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKPIR1WfjUAiw9Kn009ZoTWycIayLLoKlELw-NUrpNBtdON9aEvzpHoga81feytivi-zY5NhgX241p7ZvPx8Pt3MLlnPavYr2MT9lDmJa_ttuCU-xZ6l0dePZ7SHVCKRV4s8JrIDDLCNnLLFKZoFz43V4_h9OChBxGjlSsrl9zlO6C-oS19M5mrNbvP_VkrZ5Az4D4nokVeYr5wii_74T3Bx3iBpxFMkjMaOImkpFn0sBFmqi0TtTk4Clri8zxG5YLFKn8JiCvUpJwVTTvM3Vns61h6yNE0MmP3Zj25x2TbBlPVzLW8oAAJxFHW0Ewo-K5-9uNTekap0voxzGMvdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: نتانیاهو یک افعی فریب‌کار است
🔹
نتانیاهو با زبان عبری با افتخار می‌گوید که دولت آمریکا را فریب داده و آن را به‌نیابت از اسرائیل وارد جنگ با ایران کرده است.
🔹
او صراحتاً با خنده می‌گوید که چگونه از طریق هزار ساعت حضور رسانه‌ای در شبکه‌های تلویزیونی آمریکا، بر افکار و سیاست آنها تأثیر گذاشته است.
🔹
اما وقتی انگلیسی‌ صحبت می‌کند، او از توان رهبری رئیس‌جمهور آمریکا تمجید می‌کند. افعی!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/459168" target="_blank">📅 12:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459167">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تبلیغ خریدوفروش وام ممنوع شد
🔹
بانک مرکزی با ابلاغ دستورالعمل جدید تبلیغات اشخاص تحت نظارت، تبلیغ خریدوفروش تسهیلات و امتیاز وام، سپرده‌های بانکی و اجارهٔ حساب را ممنوع کرد.
🔹
همچنین تبلیغ خدمات بانکی و فعالیت‌های مرتبط توسط افراد و مجموعه‌های فاقد مجوز بانک مرکزی نیز ممنوع اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459167" target="_blank">📅 11:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459166">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR152lG60beULRSLF8Cr-AOqtx9lZaocSt4chDu_zKQAYaQw-lcm5PHCLUGlzQF8h2_Bu97MKHqlFubo3Qd5vTx48YfMj7Jc1PR-5ekqqnBEH3HyTQbamxNtn2fron5iEISHjI6bHqYyGnKtRIn16lTV0htxNN0fQF0Pwzzp4qI8Cp2nR_pi4hF2l-OaWMmomh0oX9bVEqUqx2TQMfR8eLZjBw-3-G8msZhwNeg8a7tfv5c-3H9YhpprqCQF3wu7t9a8EmxaBznmcORYIhI4gtgLDw2UPCzlJa804-ixXr5R6CvxquK9NJELzJaGGztjitJX3o0HWNZG0TAbSD8r6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کار: امشب معوقات بازنشستگان واریز می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/459166" target="_blank">📅 11:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459165">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bdea93d7.mp4?token=NAadopo26AJx2ADc-2eWcb-GqGzZfFWhLptC1kUM3z7sYCxxq9Gb3rl8QmujQtfAWVk8Hw1AKdx5Ey5GNgU2clY5kzRAzbMMblih0i4chXwBYU81i4gccUtFyhbRpzSSNCgmn88LrMBPw-3KOJSy1Y2Ki3Oqy5BWpI3flaspAGhgePehgv6rlfukhqao_k_u_ApdiKbfuSIvp-PLF1Ujyu9pczPD0lHPgIrzMSWwkyODhnkHvUS7IHjJKm2IDBxs4PFpZ3xqwO0px3RdDEIcIa_yYe4dOwn5hMK8qJvRJPsDaX-woM-H29ugVVHjT67tFCp9zRSJb5x0uGEVcGG72oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bdea93d7.mp4?token=NAadopo26AJx2ADc-2eWcb-GqGzZfFWhLptC1kUM3z7sYCxxq9Gb3rl8QmujQtfAWVk8Hw1AKdx5Ey5GNgU2clY5kzRAzbMMblih0i4chXwBYU81i4gccUtFyhbRpzSSNCgmn88LrMBPw-3KOJSy1Y2Ki3Oqy5BWpI3flaspAGhgePehgv6rlfukhqao_k_u_ApdiKbfuSIvp-PLF1Ujyu9pczPD0lHPgIrzMSWwkyODhnkHvUS7IHjJKm2IDBxs4PFpZ3xqwO0px3RdDEIcIa_yYe4dOwn5hMK8qJvRJPsDaX-woM-H29ugVVHjT67tFCp9zRSJb5x0uGEVcGG72oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادارهٔ بنادر هرمزگان: یک کشتی آلاینده در آب‌های هرمزگان توقیف شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/459165" target="_blank">📅 11:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459163">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aArVvxBnuYDwNP6tr2Hx6tTkG986xS1Wpb7KMwyCXOJJGJkA73hyqufE9ozAEE57vSjT8lH5J9Nw8yf3If0EJpzFktfrR9VOYAFh7Tz16APYcc1rVWrW6nVhoXGS2-lCsiHIVY0rvNSrEWWJXAFGQOQsSEPaxB77qLk6EB5rPFl65tDPDscKzfppRIMrmcp_KbvAsVf8BngswpWDbHB7fdy51Wqd6KuC8WLGzCWcO2MkDcl6qrPDzurbSvWeErON_t0vHWeGT9r1DUP98RnE7E6Tz7GQ0j40IqgJL5NAB6SmHjNfHB_WOLZ6MYafagTbiqgKJXrVLe7EYuZ45Rub5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVH2w7bV_ogCCl0_vBY4w3qxw-Qui-1qOV7p5J7cPmkRRSMrJ4RNQ6Gd53GKf4sRBRY-tyLMyhPtgWK4GSs7Xk9e5rJlVet03r1kQo2g1G-MI5FKWsjX5xNBLJ5EspyCorBbb_ESrBHHudeq7HmMFo9EDQL-d6eX4EpwuN4gMhwG9rNSS7dx0e-7B7PoJJhmyWHBvY3dbu1v3Wxn9UzM9BC6ouneddq4SGC-z_C8YEQbdRcBzEyoy3KMSZ9hdaCBi7zEyRqy_PDcJ2CeCz14JRbswP_86NoUrZUwbyHiZQbP4ZrOgiEhHgcXkSuzKUKDgeDpdimR2cCdIIay1A4UYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادعای ترامپ درباره نابودی توان نظامی ایران سوژه شد
🔹
صفحه‌ای با عنوان «پست‌های تروث سوشال ترامپ» در شبکه اجتماعی ایکس با انتشار مطلبی اذعان کرد ایران موج جدیدی از موشک‌های بالستیک را به سمت تأسیسات نظامی آمریکا در اردن شلیک کرده است و از کاربران خواست که برای نظامیان آمریکایی دعا کنند، موضوعی که به بهانه‌ای برای تمسخر و کنایه به رئیس‌جمهور آمریکا از سوی کاربران خارجی تبدیل شده است.
🔹
برخی کاربران با لحنی طعنه‌آمیز یادآوری کرده‌اند که ترامپ و مقام‌های دولت آمریکا پیش‌تر مدعی شده بودند توان موشکی و نظامی ایران به‌شدت تضعیف یا عملاً نابود شده است، اما گزارش‌های جدید درباره شلیک موشک‌های بالستیک به سمت مواضع آمریکا، با این ادعاها همخوانی ندارد.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/459163" target="_blank">📅 11:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459162">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76191ab23.mp4?token=a5u6T7jRCCwQtgmXic2scY1lTW4L3CxYuxmjD21JP2o9Y5rMBzQkLElXkZ5KW-V1H9ofUF6fTB5Ob8pt1p-YuePH3L2HD8qE2x_AFgt4U0w9eouo6h-YoMdGtM3_PR_jdI_dHOra44KGrrKbbuKnuZSIUU7bBNFuI4jsYuHkh2opIeH4yJsBUmeZSSjFZC7F_iCTjue63asUoMQKwp5wTF-KLjkXY0beX3QFoepetyq57LLFIDg6-81WbPxB7-hLd1m8Llb6DVoLOZeg0HiTeUbaMEMdBp623OMlmbbYGi6z7Tl1wjRjhpx02SNVia6TWA8uSoDq9dvFemHXaQjpeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76191ab23.mp4?token=a5u6T7jRCCwQtgmXic2scY1lTW4L3CxYuxmjD21JP2o9Y5rMBzQkLElXkZ5KW-V1H9ofUF6fTB5Ob8pt1p-YuePH3L2HD8qE2x_AFgt4U0w9eouo6h-YoMdGtM3_PR_jdI_dHOra44KGrrKbbuKnuZSIUU7bBNFuI4jsYuHkh2opIeH4yJsBUmeZSSjFZC7F_iCTjue63asUoMQKwp5wTF-KLjkXY0beX3QFoepetyq57LLFIDg6-81WbPxB7-hLd1m8Llb6DVoLOZeg0HiTeUbaMEMdBp623OMlmbbYGi6z7Tl1wjRjhpx02SNVia6TWA8uSoDq9dvFemHXaQjpeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
بیانیۀ وزارت امور خارجه دربارۀ حملۀ شب گذشتۀ آمریکا به لارک و پاسخ دفاعی ایران
🔹
وزارت امور خارجه ضمن محکوم کردن تجاوز نظامی آمریکا به لارک که نقض آشکار بند ۴ مادۀ ۲ منشور سازمان ملل است، مسئولیت شورای امنیت سازمان ملل متحد و شخص دبیر کل را برای ایفای مسئولیت‌هایشان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459162" target="_blank">📅 11:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459160">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffc673694.mp4?token=JJW2ykYrZG0mWLR3OqsqwPb3wVORTyVpGOLChVfMs7dK19t0qQ2wm_bUZt5Si5ZnJ5e4Rbj21xO60k_5vd9LQ5wrSnP7mWyTdw8X3oJjyv0ZKSG9JGWy2jOPjb8iz-0T5Jwk7ajwdxWktjWmswukgYpvw7OrVv3tbAOh1NcGONl10KGqcm9YV1Q3eSFQ30_iTHuL6urAdUG8RccUCxkH5nkmSNj_WcgQNbuPreoKgtheMTMpvooQV1We8kYQF5cD9usdXooamGePbvjv0sJiCK9iCl8EVPziHNNNawy8imzMmUWDcmfL9NJd4FLIwVjfT8C2-5sfl7XY4Xcu6oKqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffc673694.mp4?token=JJW2ykYrZG0mWLR3OqsqwPb3wVORTyVpGOLChVfMs7dK19t0qQ2wm_bUZt5Si5ZnJ5e4Rbj21xO60k_5vd9LQ5wrSnP7mWyTdw8X3oJjyv0ZKSG9JGWy2jOPjb8iz-0T5Jwk7ajwdxWktjWmswukgYpvw7OrVv3tbAOh1NcGONl10KGqcm9YV1Q3eSFQ30_iTHuL6urAdUG8RccUCxkH5nkmSNj_WcgQNbuPreoKgtheMTMpvooQV1We8kYQF5cD9usdXooamGePbvjv0sJiCK9iCl8EVPziHNNNawy8imzMmUWDcmfL9NJd4FLIwVjfT8C2-5sfl7XY4Xcu6oKqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در برنامهٔ سمت خدا: بعثت امت یک معجزه است و حقیقت آن مقابله با ظلم است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459160" target="_blank">📅 11:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459159">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edac3d8a5.mp4?token=CWTBNqulTE_I-fogCfhS_PN_W1gL32N8HMdWv1dZCxzLJmpNpwefD0TMvByT_ZNkZTuX2TOJkXkkiQmK0KmvhjX5OS-KDh6fvDK0vGbHfd3fn-rz4beovvGORI7HEXdSc262Upwjm8fqqeULV-fflAc2SNYdmWQTUzi-EP2n-H_YDILGPBTPIwd1aKDTL5ZqnhCdBOdJDKKdIlnpHzfX8nFUXt6KGIH4FUDT86OUlnWOCqAEDztQhSJobFvR1rDahn3NT4ecQykyILrHkC-fEzK8PFW8dkiXu05Fr09EK1IabEHWxWFwcg7PSrJ8zAyMe_IuOVzyNI-eiWUveR0mPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edac3d8a5.mp4?token=CWTBNqulTE_I-fogCfhS_PN_W1gL32N8HMdWv1dZCxzLJmpNpwefD0TMvByT_ZNkZTuX2TOJkXkkiQmK0KmvhjX5OS-KDh6fvDK0vGbHfd3fn-rz4beovvGORI7HEXdSc262Upwjm8fqqeULV-fflAc2SNYdmWQTUzi-EP2n-H_YDILGPBTPIwd1aKDTL5ZqnhCdBOdJDKKdIlnpHzfX8nFUXt6KGIH4FUDT86OUlnWOCqAEDztQhSJobFvR1rDahn3NT4ecQykyILrHkC-fEzK8PFW8dkiXu05Fr09EK1IabEHWxWFwcg7PSrJ8zAyMe_IuOVzyNI-eiWUveR0mPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان وارد بیشکک شد
🔹
رئیس‌جمهور در سفر به قرقیزستان علاوه‌بر شرکت و سخنرانی در اجلاس سران کشورهای عضو سازمان همکاری شانگهای و شانگهای‌پلاس با تعدادی از سران شرکت‌کننده در این اجلاس از جمله نخست‌وزیر هند، نخست‌وزیر پاکستان و روسای جمهور قرقیزستان، روسیه…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459159" target="_blank">📅 11:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459158">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5261a5e1e2.mp4?token=B1VT1NJF1Mo5ejSyS-jegD1T4NHvHcHtNRHxBJvQ2rqmHQlfxdVKM4ERu3sRw5bJcGhRF6z62eGVBXQScBp3P3GmQyVcCRL9HZ-_TOXIfP1Kd1CGz-zQouW_AEf3x-aAkvUdgYhRumIVVmLWOtuijWudgXNwVb_oDVYktlbl-O6mCYKPo8gzpPlM1tzkd84Df1sVtNa5DGJ23aeUE20gCl9APah0b_oW0VcY3EDKeqC3bbpAhcec9l1R2Mk26lB_vyo4ggHY3SxBv1nGvXFB0h6MzqNI3DYoP77f3b93B3SorQYi6N6_PxxAhVeLiSMj4mczG7N4KV2LAp2bn3Psmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5261a5e1e2.mp4?token=B1VT1NJF1Mo5ejSyS-jegD1T4NHvHcHtNRHxBJvQ2rqmHQlfxdVKM4ERu3sRw5bJcGhRF6z62eGVBXQScBp3P3GmQyVcCRL9HZ-_TOXIfP1Kd1CGz-zQouW_AEf3x-aAkvUdgYhRumIVVmLWOtuijWudgXNwVb_oDVYktlbl-O6mCYKPo8gzpPlM1tzkd84Df1sVtNa5DGJ23aeUE20gCl9APah0b_oW0VcY3EDKeqC3bbpAhcec9l1R2Mk26lB_vyo4ggHY3SxBv1nGvXFB0h6MzqNI3DYoP77f3b93B3SorQYi6N6_PxxAhVeLiSMj4mczG7N4KV2LAp2bn3Psmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: کره‌جنوبی گفت که برای مقابله با ایران به آمریکا کمک نمی‌کند
🔹
وقتی با رئیس‌جمهور کره‌جنوبی تماس گرفتم به او گفتم: «آیا تمایل دارید در رابطه با ایران کمکی به ما بکنید؟» او گفت: «نه، متشکرم.»
🔹
من گفتم: «یک لحظه صبر کن. ما ۳۹ هزار سرباز در آنجا داریم…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/459158" target="_blank">📅 10:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459157">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnT7jg2Kw2cZ6Bj4jWZGIlOue81g7sTIguVcXlftnB54V9hCoT0sCfZFRQxqYlQpjF9JyztIDXb3VfGvQnzySs09pjfQB9QcSA7V1plUfNfGv7vY9eh7YsD9j_StWflyMptTI1IsKaFocsH-N16_i0bOP9Fsa3oEQI3768l_qw5-2WaZfYYqljbszbBk5Qea7ZHtKDRxWPJs6UsPAcsnPVGnFmfFTnzLnohTBQNUsv5D0TbWnNwS5Eobpg64rJRnbFh5V5K5EizbUDj_epiT-U6p1yA-pxZE5Q8cmMmfdNaYH0yJPgtszArvlFHcxEMN5pu2CADlvGmRLkCwnPRp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاج دبیر جنجالی را برکنار کرد
🔹
با حکم رئیس فدراسیون فوتبال، هدایت ممبینی از دبیرکلی فدراسیون فوتبال برکنار و حامد مومنی سرپرست دبیرکل شد.
🔹
این تغییر در شرایطی رقم خورده که مدیریت ممبینی در ماه‌های گذشته با حواشی مختلفی همراه بود و یکی از مهم‌ترین آنها به ماجرای سهمیۀ آسیایی فوتبال ایران و پروندۀ چادرملو برمی‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459157" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btENMZRr3Q_EGL1co9k-bmuNH4WcbjYrE3fm_ETu5rJvU_GXTycwg-RDCO_mAxdVB92OA3ejl5BPw5a8d2rnJE97mJAW916q6pWO_pSnSMD6PVcdwd4maJIiAZUi2qfJaVYTlwGZXjysEBwyS3YuOE2NNvroJrG5N3gNZy-seOgijAHTWOzM6oZ8Wgfcc3oEYgxH7Jn0CwYBiClNKTJ34yEiBmgZpI129cLJ7nZ-gAmJNWF081Yw3Lyi9Qdon104vJYZAh11kJa6Q4ou6P9Y-yfGGp6knH1pooei1hDkAvx4JIJH5Od4cXoaRbpYVLJZSdQ-OJuyYMFVf9uEPWJbyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر رفاه: معوقات بازنشستگان تا نهم شهریور پرداخت می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/459156" target="_blank">📅 10:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459155">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIKGwoBSTH_p4bhQPeDYvDIFQiiv-inNnYhj_BextNNQeNw0c2nKlXxrl9nSSLgC_ESTH-bvp-VpjEICJKP1UJkN-Gqs_r8O2Z8L5Hm7uCfWmAgwusab-vwiTP6-saNFfeTM3FapsE2cRK4zpsf_xEgrQMxQYhpuVZGeT2e354HR1EBOn7ADlbPY-rsCvuucPunjsEXgFE5zllot9l5R8YtRQJGMSvsEIE8chXWMSKfGkM3kLBjCceHFj7qc49OTd7zCeE7dJyvU5nGnPWrwww8Xk6tuOOK_jGJSmRN3ibFl18YT2TS6beZzpg8CrfLdzBKSP4AFLVj1VVg1wljX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وارد بیشکک شد
🔹
رئیس‌جمهور در سفر به قرقیزستان علاوه‌بر شرکت و سخنرانی در اجلاس سران کشورهای عضو سازمان همکاری شانگهای و شانگهای‌پلاس با تعدادی از سران شرکت‌کننده در این اجلاس از جمله نخست‌وزیر هند، نخست‌وزیر پاکستان و روسای جمهور قرقیزستان، روسیه…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/459155" target="_blank">📅 10:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459154">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66874910f0.mp4?token=R_fCMOdAFxh4LslbZ_YjroLbwZK4hnRqMwnxkKk62tXOL9dR0sXK4GAW-CHDOZEP9H8QwJfjtK3QqvYetiGmhc9wxCyA2tQxjOGFUk3Z2InG4P5-fTrEgJqm7tvW3KHLTDUmF4NVZitFhWOxa-X2B3VetbXEKuAOmRGwKhyl8sAMidOhIZXkENADlsGA-6VoN-aEagAeA18XurY5b5m_6TZVWHc5E0ywn6Oeb6qtNshoCunDQmGV3M-9Pgek40Rm996zHsbtg4x8AnwyWEGySOW726vRuqjBDmwsefMnsNJCPambf7g9b_RWwUYwBDHCO8cFUs2GgHdjpl3SdIry3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66874910f0.mp4?token=R_fCMOdAFxh4LslbZ_YjroLbwZK4hnRqMwnxkKk62tXOL9dR0sXK4GAW-CHDOZEP9H8QwJfjtK3QqvYetiGmhc9wxCyA2tQxjOGFUk3Z2InG4P5-fTrEgJqm7tvW3KHLTDUmF4NVZitFhWOxa-X2B3VetbXEKuAOmRGwKhyl8sAMidOhIZXkENADlsGA-6VoN-aEagAeA18XurY5b5m_6TZVWHc5E0ywn6Oeb6qtNshoCunDQmGV3M-9Pgek40Rm996zHsbtg4x8AnwyWEGySOW726vRuqjBDmwsefMnsNJCPambf7g9b_RWwUYwBDHCO8cFUs2GgHdjpl3SdIry3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیعه و سنی یک کلام، انتقام انتقام!
🔹
رونمایی از قطعه "منتقم" با حضور مجال در جمع چند هزار نفری مردم بندرعباس
#امت_احمد
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459154" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
