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
<img src="https://cdn4.telesco.pe/file/AHGVQRwjnDu03HUwWlU4xv9qrO4mqXSA4GbV7LdAWpu_K6-zmu0mf7aJZC2_g1a5smW7j10hAuG8WGeG3lGx2Thza6BncWJgD09iAEby4D7qXKp6lKlqd8ksVVRX4Iu65Alfv9hW_xGqf0zNixFO3glg_cBDXj2YWIS4NEDVeraOCxhVpein-Ti4wSjrKGYzK4XPT-JblbLR8vPR-pLox_zAEJDE-JEnZsvdpElwXOd-cE0JAfDSVKenK7NMYNtctEfs0Cy3zV_y9cRSmcV1NpAEMeoEYdGpoMD1-IkB5BjFeTMwA8DnbWMNvR7BNybUt6HVidqZx1WXaWSKqc1zBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 19:49:21</div>
<hr>

<div class="tg-post" id="msg-666057">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
دیدار سردار ابن‌الرضا، سرپرست وزارت دفاع ایران و فیلدمارشال عاصم منیر، فرمانده نیروهای مسلح پاکستان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20 · <a href="https://t.me/akhbarefori/666057" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666056">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd7190233.mp4?token=rIdBSsRHYy0SS1_j3s3ujVqXXpnz2cKlaOrJ3317KnhVdVRVibN982VOhV2I3S6d7vr4f_66tj-bRSV0TWVjHmVbZJjluRNo5CR_uQ3y1AnQf4ePiYmWllNkary0PkdQE0qjE-KPct9s6DCee-ZfHz3H43zerK7tCZSSLZdf6f8-WEjSU9s7ay2a_CQ_29UmTHoDeC4uKuw-YOxmKyxjt2qPTRzN5IhbhA99vXp1w9GX46_E2AJ0-SU4Lcd8LxvKNlOmKgwa-WCS-4V2bzXLzQ5_E-s7knKnz3ISA2vaR1Dvvpkr9tUBLODTXGCYEVuJDuWboQiBeoDwn67pBDqQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd7190233.mp4?token=rIdBSsRHYy0SS1_j3s3ujVqXXpnz2cKlaOrJ3317KnhVdVRVibN982VOhV2I3S6d7vr4f_66tj-bRSV0TWVjHmVbZJjluRNo5CR_uQ3y1AnQf4ePiYmWllNkary0PkdQE0qjE-KPct9s6DCee-ZfHz3H43zerK7tCZSSLZdf6f8-WEjSU9s7ay2a_CQ_29UmTHoDeC4uKuw-YOxmKyxjt2qPTRzN5IhbhA99vXp1w9GX46_E2AJ0-SU4Lcd8LxvKNlOmKgwa-WCS-4V2bzXLzQ5_E-s7knKnz3ISA2vaR1Dvvpkr9tUBLODTXGCYEVuJDuWboQiBeoDwn67pBDqQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یه تکنیک عالی برای کنترل نشخوار فکری…
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/666056" target="_blank">📅 19:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be-XjI8SL_RXpkZ8CrmUblLUgNqGwtNZ7ZLF21wYykDydVYK2GXTUXY8ZuRuND9_EWO7ahtujSHSsJ6KTLQdyI19NNTZfciX15-OxnNc1h2OluK3BkvHXkPSOXiVxy1ROBJLnjl8s8Y9TRw45BinzoZvz_fLJrmCfVLfAx8sLufa5til2SLa8zf11apuC4hOc_toEGBBLQP-yX3HcdAMpRiadnmb7v-yc8xvzrbljxN96YH6agi9kmfDVF13JzklP_j2GXMem12cp8u2K-s1odBPgPi4wrdwa1E1wTD4lz_wsbNiviYOhDzQJaTBaVjP1QAyMWjFWrzFsVOmvviIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داماد شهید رهبری دکتر مصباح الهدی باقری به همراه همسر و فرزندانشان در کنار آبمیوه فروشی خیابان کارگر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/666054" target="_blank">📅 19:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666053">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSQrEVi9keVDibfoGjDGHywNPCACx2vPzj76WFqnChbFrwbbmbjVChr_2pik4WJoNF3xLShvBkNEJSkvdp4I34bOFefuNWh4cqcmxdVn4TAK5akYvbi8jAiiyGl2nUy2GyutpfpMIWkeMIh59XwRiebI3ggW0tUYf6UFgKmi1Ol6htwFKLay8-6sdSMxsuAolEqoTEFky2DDl-hl3MtNMCwrwO8zd6-pflSAQ7anIRzmiWoaneRkEaCgA0PN_oUTbHHOf01fChwAafaSP_xxox8ENSvdfo7MeT3l49y1RtcKd_BSExu4fGz97RdocLGbVrJr3Oh4rIGWbI2sBxR3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار عاصم منیر با عراقچی
🔹
فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان پس از شرکت در مراسم وداع با رهبر شهید، با سیدعباس عراقچی وزیر خارجه ایران دیدار و گفت‌گو کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/666053" target="_blank">📅 19:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666052">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4fXfNpaQblHBQ-YjJT8Ev8_IfWGqTXSCT6YvxJ9ZD_V_9NIkK92A8jux9qWaMmRDx_q6OrpT7KGOEwFw2vIAvYAXXgAwTjXQXBaaIMIhJO41TOKJNamVKuN2oW2HHaIMJrRbsmz4EK0J9FTbXNR1gEKCVsoCFMU64UdyEZyB6nEej1uWtj5Hq9HoE9UE4ZwlK0GUS-ArHi78k9s40eWjXy6AOZF-fJ7HnW2FyGlBxi96khiSRfFagRN658cuSovGPMYel5NLd0Da0Jncyy6g0y2r18Md_HTSvnbuQk35jWSiFd0CPpRU-GKobqJzVwR083pD6k_fsa0QjN1ADJ7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشتر به سفر خارجی می‌روند؟
🔹
در سال ۲۰۰۰، آلمان، آمریکا و بریتانیا بیشترین سفرهای خارجی را داشتند.
🔹
در ۲۰۲۵، چین به بزرگ‌ترین مبدأ سفرهای خارجی جهان تبدیل شد و هند نیز وارد جمع پیشتازان شد.
🔹
برآوردها نشان می‌دهد در ۲۰۵۰، هند، چین و آمریکا بیشترین سفرهای خارجی را ثبت خواهند کرد.
@amarfact</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/666052" target="_blank">📅 19:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666051">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
جنگنده‌های عربستان حریم هوایی یمن را نقض کردند
🔹
نیروهای مسلح یمن اعلام کردند که جنگنده‌های عربستانی بامداد امروز با نقض حریم هوایی این کشور، تلاش کردند از فرود یک فروند هواپیمای مسافربری ایرانی در فرودگاه بین‌المللی صنعا جلوگیری کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/666051" target="_blank">📅 19:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666050">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
هشدار  پلیس فتا به مردم؛ هوشیاری در برابر عملیات روانی دشمن برای تحت‌الشعاع قرار دادن مراسم تشییع
🔹
سردار «وحید مجید» ؛ رئیس پلیس فتا فراجا در گفت و گو با خبرنگار خبرگزاری پلیس  ضمن هشدار نسبت به تحرکات اخیر دشمن در ادامه تلاش ها و جنگ رسانه ای به منظور  ایجاد اختلال در مراسم تشییع پیکر رهبر شهید، اظهار داشت: دشمن با بهره‌گیری از ابزارهای گسترده و ظرفیت‌های سایبری، در صدد به حاشیه بردن این مراسم باشکوه و ایجاد ناامنی روانی است.
🔹
وی افزود: دشمن با جعل اخبار به نقل و به نام  برخی  مقامات رسمی و خبرگزاری‌های معتبر بین‌المللی، تلاش دارد تا محیط‌های برگزاری مراسم را ناامن جلوه داده و با بزرگ‌نمایی تهدیدات خیالی، آرامش شهروندان را مختل کند.
🔹
رئیس پلیس فتا فراجا از عموم مردم درخواست کرد ضمن حفظ هوشیاری، به هیچ‌وجه به محتواهای مشکوک، پیام‌های ناشناس و اخبار غیرموثق در شبکه‌های اجتماعی توجه نکرده و از بازنشر آن‌ها خودداری کنند.
🔹
وی تأکید کرد: تنها مرجع رسمی دریافت اخبار درباره مسیرها، زمان‌بندی و اطلاعیه‌های میدانی، «رسانه ملی» و خبرگزاری‌های معتبر کشور هستند و هرگونه اخبار خارج از این کانال‌های رسمی فاقد اعتبار بوده و بخشی از عملیات روانی دشمن محسوب می‌شود.
🔹
سردار مجید همچنین از هموطنان درخواست کرد در صورت مشاهده هرگونه محتوای مشکوک یا جعل خبر، مراتب را برای پیگیری از طریق شماره تلفن ۰۹۶۳۸۰ و یا وب‌سایت رسمی پلیس فتا به نشانی
policefata.ir
گزارش دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/666050" target="_blank">📅 19:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666049">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtlLDRLGRjLPsbOTdUYZKsci5h-nwQQYZQo60EncZkuVHo9lAzNy2Bg_lxAt0QhOmSm89bB_URdKGxjPDku-qLeQ40KQ5hozK_i_k0xL8uSuUrqYYGISkJK26GyyVnHDlhmGmecnMlz-Qm-_ThMuoo2-qW99teRYyxakcg7wQV8PKVziPYLmqKOx_YD23tQs8M-xEBvzyNXyv91vkrGyTjTSwH2wlYT9wBS-sLdUz30DPOcP9GmxOf4-VPjmVGbt1ePQYe9vJtbORzCvA-U-NseGJS5em3JYcLj__Ein64J9IdhzDPo9HzX0W8PGIic5K78QDiclORL-wkQMxHmVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار عاصم منیر با عراقچی
🔹
فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان پس از شرکت در مراسم وداع با رهبر شهید، با سیدعباس عراقچی وزیر خارجه ایران دیدار و گفت‌گو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/666049" target="_blank">📅 19:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666043">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105522b658.mp4?token=eHNPOhQ3djK7DxX-zdgB8squiws_Av5xzFIi2Rzfjm_CP016KwySl7KSrVsyxfz5nM5y5ys204ZJhsjyPdXuS-cCcakPAZ6oLO7o9KhTXt-Jl-xLZTyaULq3BXf25QloUC0tWml39PsPKvDDqqKovoh--_mk1BNzH7CvyM4oiTJ6Gskbo6Jb9vDgNS7y163hrztHK3txY0LftgA73aslR2Ec5pi8Mn8nPMXJvrztU74GDCNpWtpfmoqCOu_RTGCm5DsTMNvCNbP-T5Hcvbws5sKEgyngW-aLPsLwntXsE3W06K_h1OCSGJ53fFGgJVpmfj-UmGMsPMURHCRJuTGkbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105522b658.mp4?token=eHNPOhQ3djK7DxX-zdgB8squiws_Av5xzFIi2Rzfjm_CP016KwySl7KSrVsyxfz5nM5y5ys204ZJhsjyPdXuS-cCcakPAZ6oLO7o9KhTXt-Jl-xLZTyaULq3BXf25QloUC0tWml39PsPKvDDqqKovoh--_mk1BNzH7CvyM4oiTJ6Gskbo6Jb9vDgNS7y163hrztHK3txY0LftgA73aslR2Ec5pi8Mn8nPMXJvrztU74GDCNpWtpfmoqCOu_RTGCm5DsTMNvCNbP-T5Hcvbws5sKEgyngW-aLPsLwntXsE3W06K_h1OCSGJ53fFGgJVpmfj-UmGMsPMURHCRJuTGkbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
خدا صبور کند در مصیبتت‌ ما را..
پک
#استوری
#رهبر_شهید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666043" target="_blank">📅 19:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666042">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqFoFB53H0fo5XSYqovF7F_gUEIGdy56KBYVC0OFKgBQh6cepUVB7llY0ApxCWluZw3ohRzduWPij_Sk5msv5MLju2Ku-jKFW3HqDrT2E9K6vpGcA1xdV4XADVhCwakOsrouzVWSY00VUXF1p_X1ZDKBekM0BRwu-To_IhlOeEoobdjfo2L-vNTr0WWKkgo0stdxsjs5HRY2-b72zrihJ63eTidfuDbs_rCm2HTHJ596LpUf97Ptg7iuKxLDjdSSe64-Ic5MlGisELVxKzoxSwAaGLy3Ee4Psi0_6zNzMfjPvSVSFmN2zVmPWUFr1Hfcacu7LUNkvcV-LAi7jYckMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متفکر الجزایری : دختر رهبر ایران را تمدن اپستین کُشت
دکتر یحیی ابوذکریا متفکر الجزایری :
🔹
آمریکا، دموکراسی، تمدن و حقوق بشر... دختر فرشته‌گونه زهرا، نوه آقای خامنه‌ای را با موشک، نه، با تُن‌ها موشک کشت.
🔹
این تمدن شماست، ای فرزندان اپستین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/666042" target="_blank">📅 19:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666041">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
در مجمع عمومی سالانه مجتمع فولاد خراسان عنوان شد:
🟢
عبور درآمدهای فخاس از مرز ۳۲ همت و جهش ۲۱ درصدی درآمدهای عملیاتی
🔸
بر اساس گزارش ارائه‌شده در مجمع، درآمدهای عملیاتی فولاد خراسان با رشد ۲۱ درصدی از ۲۶.۷ همت به ۳۲.۲ همت رسید. همچنین این شرکت با وجود محدودیت‌های انرژی و افزایش هزینه‌های تولید، موفق به رشد ۱۳ درصدی تولید شمش فولادی، ثبت ۸ رکورد تولیدی و کسب رتبه نخست عرضه میلگرد در بورس کالا شد.
🔸
در پایان مجمع، صورت‌های مالی شرکت تصویب و سود ۶۰ ریالی به‌ازای هر سهم میان سهامداران تقسیم شد.
مشروح خبر:
👇
https://t.me/khorasansteelCompany/6485
🔘
روابط عمومی شرکت مجتمع فولاد خراسان
تلگرام  |  اینستاگرام  |  بله  |  سایت</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666041" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666038">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک کارآفرین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b6320143.mp4?token=fTnBC1Jdzw87lOAfnUEZbQhoL9zWO7u5LZ_WT86icY_qnljAkg0Lr7Co-epqKW0xPw2IAIDg-a0hn9NDVuDk6JI1xS1_QHm1Vr57pEOln14Qb--_P0nJvkSqnpsl9-6dCZHwa3rsTYrrSqIIaV_l5P88h9QVPIrbi4uJx-vh96MRWEdJ8iJjLKJ0pjfO4wvpZBeBPRmwsCQn1KtTDlVKS2arfT8IcLj0ZnKs4PeqbPk5OoXOr7rurLFvFFb7H_EQsARPK1u6Fd2XUdKE3TmVtnNSauohW40h4dJWFQDKQHPp6zsaKpbG3LFzRKQ-0sRtXiWZE_RVef-KKuVpQXKqnVcZODmw0PemsQf1FFcNrIwTyE2pjIKOQNftqwLTAxPiAWnoSD8bZ8ypka91gXnX9ixE0-PZmTI_1OXWVh_duL-eZxjrtEcc0sl6Hlrqa9ktAhW5KcWvfCa5-ROovgZx43DYUWgk4efOU6zdL_dlb2xtlay7PEGHvCrz6cgwVdGezwIyzDBA_l-86rRq2d5ztZviu5glVNX-ao1saUT3vX4kEJEZbSJSoV-ic_fGXPL0mifbFwsKY8ERjT6knovK5nBxTVqx9SEWbpsOZRCZLzBZLwhidFQkawihSqKdB-24_qpGL3Kd81KrB5Xy3gFXmjRTvQWLcbq2emXMFiFR-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b6320143.mp4?token=fTnBC1Jdzw87lOAfnUEZbQhoL9zWO7u5LZ_WT86icY_qnljAkg0Lr7Co-epqKW0xPw2IAIDg-a0hn9NDVuDk6JI1xS1_QHm1Vr57pEOln14Qb--_P0nJvkSqnpsl9-6dCZHwa3rsTYrrSqIIaV_l5P88h9QVPIrbi4uJx-vh96MRWEdJ8iJjLKJ0pjfO4wvpZBeBPRmwsCQn1KtTDlVKS2arfT8IcLj0ZnKs4PeqbPk5OoXOr7rurLFvFFb7H_EQsARPK1u6Fd2XUdKE3TmVtnNSauohW40h4dJWFQDKQHPp6zsaKpbG3LFzRKQ-0sRtXiWZE_RVef-KKuVpQXKqnVcZODmw0PemsQf1FFcNrIwTyE2pjIKOQNftqwLTAxPiAWnoSD8bZ8ypka91gXnX9ixE0-PZmTI_1OXWVh_duL-eZxjrtEcc0sl6Hlrqa9ktAhW5KcWvfCa5-ROovgZx43DYUWgk4efOU6zdL_dlb2xtlay7PEGHvCrz6cgwVdGezwIyzDBA_l-86rRq2d5ztZviu5glVNX-ao1saUT3vX4kEJEZbSJSoV-ic_fGXPL0mifbFwsKY8ERjT6knovK5nBxTVqx9SEWbpsOZRCZLzBZLwhidFQkawihSqKdB-24_qpGL3Kd81KrB5Xy3gFXmjRTvQWLcbq2emXMFiFR-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
«تاریخِ جهان پر است از لحظه‌هایی که قدرت، بر انسانیت سایه انداخت؛ جای آن همه رؤیا، فقط زخم‌هایی ماند که هنوز روی دل ملت‌های مختلف تازه است.»
🔹
«روز افشای حقوق بشر آمریکایی» ، روزی که چهره‌ی سیاست کنار می‌رود تا حقیقتِ قربانی شدنِ عدالت نمایان شود.
#مناسبت
☎️
۰۲۱۲۳۳۵۰
🌐
karafarinbank.ir
📱
@karafarin_bank</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666038" target="_blank">📅 19:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666037">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN8ugfq1IzZs1v2QgadYwzcl3gbWEMj-CGKDZ5b4rSTkZoJk76ZWF1zFIZfF_obph0_rysYVJ-A4paado1W3nUw6Fp17joMjgnjjVR_Y6wPTZvjUEQ5YQxRyiihdZqVNc_GVaHp_T-MW3hKhwUDJiZ05GNsCmpThlKgfFyUtzwV22fBxN9tio7S-Sg8915ddrTnjgm9Nbx0WD1rIvgpmE-YjVsZoGnoiFPGu8Kzd_XAIGvGzXTLLLsrYhFxO6bGY7cm5XfZ96RJ1rZqCHcKSa-53sIU1Q5nQSPUXrVEnZXGKP7YgYLSGZCrjBbR4Mvs3G-UH4ZPzLywjSYDLId63jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادای احترام خانواده امام خمینی (ره) به پیکر رهبر شهید انقلاب اسلامی #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666037" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666036">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7dd42f9c8.mp4?token=s5-vLd6iXs0sM9fCc2M41YIPzK6G7uOHISuKrc_YRBU1PaH2pSF3H3Ca0YH7h2ZDF1E3LzJH6vezhJGCSvWUAAYly4wWsl1_RAVfCISUr8Ditwj78-8gelCZlJXv2_tGol2EiVbJSKcmPeaZRKGjdbFYBs73BjA6X8JTcoSf_UnrFWtdSL2JgiDtHQe9HV5Vf9RK6aUNW2VnhKs_2tawScsiMD3-x-T_VAL5F438-DsGD7GVhLqXgvU4fF49jZ5QabTt1KUkIidesJXzoFH3nlgS47QmLui1vriZkpzlbB-Apw80wd6WagEtkTDrI-8vBm-FQYv5v0D28RnPM0lC8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7dd42f9c8.mp4?token=s5-vLd6iXs0sM9fCc2M41YIPzK6G7uOHISuKrc_YRBU1PaH2pSF3H3Ca0YH7h2ZDF1E3LzJH6vezhJGCSvWUAAYly4wWsl1_RAVfCISUr8Ditwj78-8gelCZlJXv2_tGol2EiVbJSKcmPeaZRKGjdbFYBs73BjA6X8JTcoSf_UnrFWtdSL2JgiDtHQe9HV5Vf9RK6aUNW2VnhKs_2tawScsiMD3-x-T_VAL5F438-DsGD7GVhLqXgvU4fF49jZ5QabTt1KUkIidesJXzoFH3nlgS47QmLui1vriZkpzlbB-Apw80wd6WagEtkTDrI-8vBm-FQYv5v0D28RnPM0lC8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روحانی: رهبر شهید، دانشمندی بودند که مسائل دینی را به صورت عمیق تبیین می‌کردند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666036" target="_blank">📅 19:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666035">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
حاج حسین یکتا: خیلی اذیت شدم وقتی حداد عادل در مراسم وداع با دخترش گفت جای آیت‌الله مجتبی خامنه‌ای در مراسم خالی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666035" target="_blank">📅 19:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666034">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: تلاش آمریکا برای ممانعت از ترور عراقچی و قالیباف توسط اسرائیل  روزنامه نیویورک‌تایمز:
🔹
واشنگتن با اطلاع از نقشه اسرائیل برای ترور عراقچی و قالیباف، به‌شدت نگران بود که این اقدامات مذاکرات حساس صلح را به شکست کشانده و شعله‌های جنگ را…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666034" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666033">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyFohy1PaEBcVZXKvwq8TFZQH2DcRO1pV2oc0TmLGsh_YB87YjLrnfSPo3ZmwsdhH-B2WqV5I4X_z-ix8QuJKKZ5fbdwIJThutb0FzERfo1O-hix12SY_ASygM2KnICgb_kcKUHT9f6ZDwxOmKexSXhqFviyYGtVtvh7u0bHjnyZXb6651LzaQrQaGEHS-idudoKQSy68JpvwDT288wBEgMr7Ef__8KuqmW3qwdEappWfsazJDli5G_sJfjZzw_DDtcl-OWY56UAvfg2oLXnw6djXwesdpW2mYFGvmaEt76JXDOdae7X0lXdhjGanisRMINReNJKhTbt9TQKx7O7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666033" target="_blank">📅 19:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666032">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دعوتید به دیدار
این بار برای وداع در مصلی...
🔹
وداع با پیکر رهبر شهید انقلاب اسلامی، حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای
🔹
مصلی امام خمینی(ره) تهران
از ساعت ۶ صبح روز شنبه ۱۳ تیر ماه
الی اذان مغرب روز یک شنبه ۱۴ تیرماه
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666032" target="_blank">📅 18:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666030">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cee7d6c7e.mp4?token=rGJlttLotyGNspu_AcWo_09mhpeUD4WVseJTbAYY-kAPw-nKzn6bn4cOV602GHW_AYG6KYX5bsORw1S8QUjY4lNQQqQtTX5ILV0ngKwooyyblPX7sifp1s0cRykdkC9zz3AFMl4h71oUxEMUrFkNb03SCjBFoXN3JTuTf7pJRNIgGz6-QAXiUdqHlBrMzwpn8Cu0Q3_gfIuXxIaC2Fcs-79S0HDFu2W_v6MZYGshWgx6P4Cyb2W1totmXaea1GT5KvGM1VyohXUN0BfEtpT5Ec12EkNJOhUkU7msJsjPhxdhQ0MUSowrWgVe310ul66PlZx4xryCRIGRcf4R_GTQsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cee7d6c7e.mp4?token=rGJlttLotyGNspu_AcWo_09mhpeUD4WVseJTbAYY-kAPw-nKzn6bn4cOV602GHW_AYG6KYX5bsORw1S8QUjY4lNQQqQtTX5ILV0ngKwooyyblPX7sifp1s0cRykdkC9zz3AFMl4h71oUxEMUrFkNb03SCjBFoXN3JTuTf7pJRNIgGz6-QAXiUdqHlBrMzwpn8Cu0Q3_gfIuXxIaC2Fcs-79S0HDFu2W_v6MZYGshWgx6P4Cyb2W1totmXaea1GT5KvGM1VyohXUN0BfEtpT5Ec12EkNJOhUkU7msJsjPhxdhQ0MUSowrWgVe310ul66PlZx4xryCRIGRcf4R_GTQsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی از پیکرهای مطهر رهبر شهید انقلاب به همراه شهدای خانواده ایشان در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666030" target="_blank">📅 18:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666029">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893408b9af.mp4?token=iDCFEQxr-7EToVHeGB8yBOUFrt88T21dPBI2DMtppIKT92y1Q_Nzc6whLn_PUkhOsd5zx84OTto5aFRjPe27gS-dEXX8L3nSvTMLHq1Cvrb5_bP1YLAY5d-eItYsVwyF-IeE6MUF3Ke3qAszUwb2MnIEpzGKsTDDSOO_KKCbGI7uuNfF7wnDmBz6v1CPwjKXCuR4ikNeA5eV_fsPR5bMUdVSPRJbGQ2s9ASAqM1SfZFrlI4BkPauIILm7lprGiooI3gjsMW2HoyqWd4uqBALv-J1WJA2DL0BS94VsDP4fum_xXN4Q-eM2lITd7VPaGiub5TBXDf5MmytHrZqBlLOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893408b9af.mp4?token=iDCFEQxr-7EToVHeGB8yBOUFrt88T21dPBI2DMtppIKT92y1Q_Nzc6whLn_PUkhOsd5zx84OTto5aFRjPe27gS-dEXX8L3nSvTMLHq1Cvrb5_bP1YLAY5d-eItYsVwyF-IeE6MUF3Ke3qAszUwb2MnIEpzGKsTDDSOO_KKCbGI7uuNfF7wnDmBz6v1CPwjKXCuR4ikNeA5eV_fsPR5bMUdVSPRJbGQ2s9ASAqM1SfZFrlI4BkPauIILm7lprGiooI3gjsMW2HoyqWd4uqBALv-J1WJA2DL0BS94VsDP4fum_xXN4Q-eM2lITd7VPaGiub5TBXDf5MmytHrZqBlLOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی از کارهای به ظاهر دشوار را میشه بدون وسیله خاص خیلی ساده انجام داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666029" target="_blank">📅 18:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/54cc7be978.mp4?token=qcrMd2lpBaw37NLRwSILPFOAi-hF4p94FtevYOaN81-OYxE8WY-DYQ7JhMuS8R9-0_K90K9gA1vOk-35n_p4hJiEpsS_8YbvdS7hbe-Ij0qCLs7gQXtu7o-5xbBYokmZcuGUXMycJwaJE0155ptJ76IQtKuXUUpmBcwHbBirHGw9hEAafiOeJ6dzfd7AByrYtBp73b4BPJ9nLTzzs40IA4uLQzF5dtvlxkTwItVq5JnvQ1PMgeMqRMnuU-vsWYcDd9-uH7SSN0ybAGz8kkIaxWFUVEuG7M2_64UJFRXTo28xGefBJhYcuERxmpSk1UKSlNGxKtnxLOO034VieXH8A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/54cc7be978.mp4?token=qcrMd2lpBaw37NLRwSILPFOAi-hF4p94FtevYOaN81-OYxE8WY-DYQ7JhMuS8R9-0_K90K9gA1vOk-35n_p4hJiEpsS_8YbvdS7hbe-Ij0qCLs7gQXtu7o-5xbBYokmZcuGUXMycJwaJE0155ptJ76IQtKuXUUpmBcwHbBirHGw9hEAafiOeJ6dzfd7AByrYtBp73b4BPJ9nLTzzs40IA4uLQzF5dtvlxkTwItVq5JnvQ1PMgeMqRMnuU-vsWYcDd9-uH7SSN0ybAGz8kkIaxWFUVEuG7M2_64UJFRXTo28xGefBJhYcuERxmpSk1UKSlNGxKtnxLOO034VieXH8A4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطعه موسیقی «باید برخاست»
🔹
موسیقی ویژۀ آئین بدرقۀ رهبر شهید انقلاب به همراه تصاویر کمتر دیده‌شده‌ای از رهبر شهید انقلاب منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666028" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666027">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eda90d158.mp4?token=HzzroHjPBD3ZSnKopPwtldhOt7aR699mPttsIeQIJxAv4ZCJl7l5FrKxwi5Q_x20Plhh5n0HaC6Uym1ewv0qIdwCTFjLMRtiV0H6tIA_bz9tVIRZOLZGVrdgwW0tKko3BHjTPWjnhHyq9q6cQYYA87NjDFRxIX610K9Vop1pMKnDXTEaI-Afp_kabHm9_7-WOnMISXrbdkdLYwQ9CDiRVwz9hcRqSWjmBMjVPT6z_dpkaJqNtAr3mJN-37YkHadEJFD5Lpr5yIV3PXQ8_OjrlNQGzBp_onLsDOsgnSDCtYPRYbLb6Ck8AzVDXMdBNCh56eWn6RXrPCOVyqd-nfF9EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eda90d158.mp4?token=HzzroHjPBD3ZSnKopPwtldhOt7aR699mPttsIeQIJxAv4ZCJl7l5FrKxwi5Q_x20Plhh5n0HaC6Uym1ewv0qIdwCTFjLMRtiV0H6tIA_bz9tVIRZOLZGVrdgwW0tKko3BHjTPWjnhHyq9q6cQYYA87NjDFRxIX610K9Vop1pMKnDXTEaI-Afp_kabHm9_7-WOnMISXrbdkdLYwQ9CDiRVwz9hcRqSWjmBMjVPT6z_dpkaJqNtAr3mJN-37YkHadEJFD5Lpr5yIV3PXQ8_OjrlNQGzBp_onLsDOsgnSDCtYPRYbLb6Ck8AzVDXMdBNCh56eWn6RXrPCOVyqd-nfF9EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی از تابوت شهید زهرا محمدی، نوه رهبر شهید انقلاب در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666027" target="_blank">📅 18:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e246b2ba.mp4?token=FfSJxOmq5juzfjwdf_o8BgUdFr7I_sLDqPUc0l18SJT-XpdMBTP5vAHTd6JW309EBSp_a5bVUU9F515eGsvDKtY7JYsAfL-F_4NUaQR1PN6QbVach0pgFRCUm44Tvgi38SkZRnsTNV3laZn5YGHxg-ECSs-rQFJGcfHY1iyF-bWXAtgsUiQhKF-M05t1ZwspAGjCB55CKHyHWJNeVRPtZBsaoydfJYETg964teF2z_c0Y9un1j3v8ICRSAAwuvUb0ju_I9dinB-B6QXlnae3ZY5l9Pfol6Qd40xlr_3ypW-klnfXEF-Ar-I3y7pQMYoK8aXFL4ecwpEKgln_pnS8Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e246b2ba.mp4?token=FfSJxOmq5juzfjwdf_o8BgUdFr7I_sLDqPUc0l18SJT-XpdMBTP5vAHTd6JW309EBSp_a5bVUU9F515eGsvDKtY7JYsAfL-F_4NUaQR1PN6QbVach0pgFRCUm44Tvgi38SkZRnsTNV3laZn5YGHxg-ECSs-rQFJGcfHY1iyF-bWXAtgsUiQhKF-M05t1ZwspAGjCB55CKHyHWJNeVRPtZBsaoydfJYETg964teF2z_c0Y9un1j3v8ICRSAAwuvUb0ju_I9dinB-B6QXlnae3ZY5l9Pfol6Qd40xlr_3ypW-klnfXEF-Ar-I3y7pQMYoK8aXFL4ecwpEKgln_pnS8Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگنده‌های عربستان حریم هوایی یمن را نقض کردند
🔹
نیروهای مسلح یمن اعلام کردند که جنگنده‌های عربستانی بامداد امروز با نقض حریم هوایی این کشور، تلاش کردند از فرود یک فروند هواپیمای مسافربری ایرانی در فرودگاه بین‌المللی صنعا جلوگیری کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666026" target="_blank">📅 18:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666025">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d1f1d950.mp4?token=dotXLQ6pK0JY5KOXVQHRyQM_dRrcecWuETsm8j_9-OaQF5ED_TN926zPU1tS-k0wfLpo9SvE9cRIATHZIel15Vb5cSqmi_fjUVT01sJUoNp_g-fHrxLn_YJpNevC1wtm5hyEcZZCzH0SfdXmpztKT_4IUgkgUdIaKqxLvNL8gyNK__94PlP9yxO30b3w_3n8eOh5pCNDfFHhzVAmqtc79UBmKkxMLbJmY6qSJT-PcRm3E0ADcAY5tlsdChBcCB3W4UWqj5oUhFQY5cyflVwVhxrbfPLsW1EH0yrswrF-dqQg34bRy5Bpx0iQghMpHvkWH8D8aopCCfROUwv7QS1r7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d1f1d950.mp4?token=dotXLQ6pK0JY5KOXVQHRyQM_dRrcecWuETsm8j_9-OaQF5ED_TN926zPU1tS-k0wfLpo9SvE9cRIATHZIel15Vb5cSqmi_fjUVT01sJUoNp_g-fHrxLn_YJpNevC1wtm5hyEcZZCzH0SfdXmpztKT_4IUgkgUdIaKqxLvNL8gyNK__94PlP9yxO30b3w_3n8eOh5pCNDfFHhzVAmqtc79UBmKkxMLbJmY6qSJT-PcRm3E0ADcAY5tlsdChBcCB3W4UWqj5oUhFQY5cyflVwVhxrbfPLsW1EH0yrswrF-dqQg34bRy5Bpx0iQghMpHvkWH8D8aopCCfROUwv7QS1r7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشور پاکسـتان: ‎رهبر شهـید در یکی از دیدارها دست عاصـم منیر را به گرمی فشردند و به او گفتند فرزندان حضرت علی(ع) هرگز سر خم نخواهند کرد
‎
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666025" target="_blank">📅 18:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=OFgMx6R3SpzexP8Mtkg0Y5FwTKdxWQVT8KthlRn3xxAxRaZ8P0z0__K_ukdrlFZZGDJfHxpiMJ4TlU1dZYDDd7JUIPPGKih3GPtofxwQY1rpngbW8SCP7Afkx8DC36XBENrLCf96LaWXINl6t5yAXBbDbJh7EVXCdIlx4EThWryYnA5SQgwk3mm5sz_3_Nqmkjrsi3Rf3bXQ9U0BwalFfpjQUJUd-eaiEJ7DDikvYLIPXzOWOL-_7sehXc2RVmpdyTLuF2rt7Opj8Q_t9bxBuDST6aDKDZ3bPPdUC8hiGvNSju7a08rGUQmDrgy5z4IOnKY3rgV3RNyOPzfkUaOo6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dab0c195.mp4?token=OFgMx6R3SpzexP8Mtkg0Y5FwTKdxWQVT8KthlRn3xxAxRaZ8P0z0__K_ukdrlFZZGDJfHxpiMJ4TlU1dZYDDd7JUIPPGKih3GPtofxwQY1rpngbW8SCP7Afkx8DC36XBENrLCf96LaWXINl6t5yAXBbDbJh7EVXCdIlx4EThWryYnA5SQgwk3mm5sz_3_Nqmkjrsi3Rf3bXQ9U0BwalFfpjQUJUd-eaiEJ7DDikvYLIPXzOWOL-_7sehXc2RVmpdyTLuF2rt7Opj8Q_t9bxBuDST6aDKDZ3bPPdUC8hiGvNSju7a08rGUQmDrgy5z4IOnKY3rgV3RNyOPzfkUaOo6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام دبیرکل سازمان همکاری اقتصادی اکو به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666024" target="_blank">📅 18:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حضور میلیون‌ها نفر برای مراسم تشییع پیکر رهبر شهید ایران
ای‌بی‌سی نیوز:
🔹
میلیون‌ها نفر در مراسم چند‌ روزه تشییع پیکر آیت‌الله سید علی خامنه‌ای، رهبر شهید ایران، شرکت می‌کنند؛ عزاداران از شهرهای مختلف کشور برای وداع با ایشان گرد هم آمده‌اند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666023" target="_blank">📅 18:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5765e1db.mp4?token=arZWnD6bRKMvxNXC5Nx_kMsdSyrR1VSniDE5trUBJQOtQaH78cZtwHO3eDxUOuU4OCB6X-6me_oamLTx-qsQPN5WFOC7CZlidIjmXwzRU_ubtIJIrUaIgfJVip2QlTOvLmNYAkm5KBZqKZnekkkLYMvxI6EzQEYwpABXRCXJTeyS83mZYJ52jj-mI7vNKVPeQdhT-87tAY2UZ-MsSNIjC21ihPiW-vT0FtiZELPbVp2kR8oa-JZ1qePwWvlZpP7xX8QBBQndHUw5Lyu324IHWqO1rfMdWIpTFgXYYKNPe9iI28Y8m0XpTQEo2cA0s-SMdZnL77jqT9kmsAhGkYMpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5765e1db.mp4?token=arZWnD6bRKMvxNXC5Nx_kMsdSyrR1VSniDE5trUBJQOtQaH78cZtwHO3eDxUOuU4OCB6X-6me_oamLTx-qsQPN5WFOC7CZlidIjmXwzRU_ubtIJIrUaIgfJVip2QlTOvLmNYAkm5KBZqKZnekkkLYMvxI6EzQEYwpABXRCXJTeyS83mZYJ52jj-mI7vNKVPeQdhT-87tAY2UZ-MsSNIjC21ihPiW-vT0FtiZELPbVp2kR8oa-JZ1qePwWvlZpP7xX8QBBQndHUw5Lyu324IHWqO1rfMdWIpTFgXYYKNPe9iI28Y8m0XpTQEo2cA0s-SMdZnL77jqT9kmsAhGkYMpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندۀ ویژۀ دولت تانزانیا به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666022" target="_blank">📅 18:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSMO9-bPeAgxhh_fAlQpVlVLf19bGdhEdVMM0_U4OTsED4lFAcVK8XGojhypP_IsBrkqvoB-pwcY9bRPIYTYiM530CPChwCo8HNkZEVsklvb0wqWHMDPIb-s3Z7-o94SgfysTB4TWfpLQ927MwZjE1CSAJcO7XaKx-s42QeWZCbkNK4tzeVQnIDw9XrMzFUEVimgW5NWRXlsmQsA_zvGtv-0VL1pOTaAC_TEpdlPAdnWH1Zs7JvOSmUChFhmB2TrInAL5ZAkMPN4Wvl-hYLGtQrHssIHCaPMUQnHPVGK3vvZAtI6xkNCdkF67xsDfEea5TZMEzWjQn_yaB2g9kdSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قله زیبای دماوند از دشت ورامین
🇮🇷
#ایران_زیبا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666021" target="_blank">📅 18:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666020">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVfWfmPkhlIr7ZDThLCdlB3_6rSEHSkp7UtxMZCI7s76GeHmql38SOB2rJhWAu09z-oG70gDUE_kHmPTxPJdN2RTHGFF3fC4MmViLWLMaDaqbIR9EY7seMoK2BGwvzkUFrwrzBVAcZWzStMdeQiOb6YH7BMPPPmI9B9HofH3qWH6OXvlMT4x9PsoOJHSTk8sdqKCeLII59EyBabYAnUSj6nxnVYm3dROc2hhtM-4TlOtegSrynhQpiYQf2EtPThHkUeaPRuwrafdFM4OeDUztY3PaaZm-1lwxjVMEeOlJhGTi-Nn0lbrBmJYSGLdrrNy2adLbv_o8D0dvwx9X0a1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب جهانی مراسم ادای احترام؛ حضور هیئت‌های رسمی از ده‌ها کشور و سازمان بین‌المللی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666020" target="_blank">📅 18:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666019">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8671d75c.mp4?token=oq7-h-VKc2fJxdBbOnn2vPCkmJ8zZxz07d_1_YzhEmyG-YD4lVBDgoyZuy0Ju4jKj4Mj5nP6iGQxgcPmDNR_0XPjhxLt4uJEbIbOavLgrd0wgjCecZDmJPn5Cz_AWDdtIuUAGUsMPfd5vJ_fZ0j-9OnHiR8hNTuCh3rFwV4-d6D9lRjcxhq9ouHMpYJ_WF5ubFMA6BCTC22j5cdvu23QOrO3sCgGqxgVrNh1fJDUHRcuVcXltkKvRQpklwG6XXvx8buLmxTJTa3rewTAy4hxXVV0ydtPaVcOmkyC67rwtzktZ0s_jJ7mp_V8iwSx9UIsdSwz1g1kd8kg53blq88q9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8671d75c.mp4?token=oq7-h-VKc2fJxdBbOnn2vPCkmJ8zZxz07d_1_YzhEmyG-YD4lVBDgoyZuy0Ju4jKj4Mj5nP6iGQxgcPmDNR_0XPjhxLt4uJEbIbOavLgrd0wgjCecZDmJPn5Cz_AWDdtIuUAGUsMPfd5vJ_fZ0j-9OnHiR8hNTuCh3rFwV4-d6D9lRjcxhq9ouHMpYJ_WF5ubFMA6BCTC22j5cdvu23QOrO3sCgGqxgVrNh1fJDUHRcuVcXltkKvRQpklwG6XXvx8buLmxTJTa3rewTAy4hxXVV0ydtPaVcOmkyC67rwtzktZ0s_jJ7mp_V8iwSx9UIsdSwz1g1kd8kg53blq88q9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشته‌های مهمانان مراسم ادای احترام به رهبر شهید انقلاب
در دفتر یادبود
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666019" target="_blank">📅 18:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666015">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAZbsBXAtET8x1X2EwBKmK2x9gaEx63c9JrwiZulpabqCbPisdUBOwDsuuCp_zuUOnVwKTzotL0H-VfLRL_KWEOF-2Ki_FQNoWrpNLkBFNT-yMd9dCBnZO1JYg-vtoSi480M1oEoaeITDREBO7hOfCX6DtcDBztS4znM0euhhPwUdiqSCn5Relp9cJE6rkvbZA6iZe35dDDGJz79sUtN3OmfuEHqPPcoNmTX19UMVGtTBZmoaP5tvFWRIjzx2N6HLd8RaSjG6PdYKK_z8BNS8B8la0KKp2oOW237At1mYRm0lY8CWgowu_iFEaKqZuHX9r_2RwFcVXIG96nCW2oIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iK3X5g3_ey31TTSFSAhVkAVsn_OWIOBAR5TYgP6Y38z2lu0Qv1En39P-g2h7diNQlHYzCj467ifw7LKWp4QFJ8ggHssUtsvkcHdJv7V1pS7FLfACSeViB0I2VAK-SVEk1rrwqrnVghSFxeEFtJjfKvLtmdcufWyO83auG03IyLUON1AdttiATDtidNja9QSCuc20575CTJoIDP0xLNIuJkC5CeWywTkx_10hCkSyCFF_FsX85-RJY8oR_tMIMZaeiV6ovRU3hFff5F_njxdnVMII6ELmC0J58MuoOKw-O8krq156Mr9VH67hC1U2bdV673Am8-0g3ovfDWXRIeEKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBdLZet3Z6-01H0xwFXv_x8LGD7_172eQsrr09KlxSDUmlBmYNdhRgk2PtoURQFcm38kwzDlqUFkwa9lRzNopiXrVSQpBkf7pVNITtRj2CEqptmHGh-39i9cnmaV546H2JEY2a2ehe9-gK2ndxAE_TUzCr0UKe0wW7YzFk4pIVMhnD8Cp4voRtoMRdZuEWqrcR6iExMAQ7Ec7FjpALEHyOBLMIFhdx1f4Ypg1KpfG-LEI304cMR62mFZ_mFQrpY2no50IIkAtvhZuNxFboLoAmMnQycPlYDDlIBqBYBqsdnTHSRqie6IMQRLUk1UJnm0HxBssF02doUUARgIKTqBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVJQaCAiH0W2dQ0SKyY8JkiWAvtZ3L7Og8TsoOVGDxDV20JSzcQduBLSAeXIjDUtaFCzwVgkEIUgSPCZEYcSrVb5Q6qB3iQ5fUFmMv5I6uv6PDdjA4X0oVllRQ0oP5mQ-8G0LV9FD6i2a5gjA15zhq5dwIuZA6ckrNDg7ilCTFjjiXeR-Bxksx2zXivMjaRCgeFy9nM5R6Y8B-HFVFmbW-LVYBqcQhFdC3NG97QUubD1swkEG-z393EJXTuSpiBlHFCRBbiJ84wjDWzdaEQa1te8KP_QIObh0BC22EBuGFNmE_QUXu5iCA-C__Rz5dXRq8hSrxU9ZpItfDB4LjH5Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۲۲ ترکیب مفید با ماست
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666015" target="_blank">📅 18:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666014">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
آغاز مذاکرات ایران و ژاپن برای ازسرگیری صادرات نفت
رویترز:
🔹
ایران مذاکرات با شرکت‌های ژاپنی را برای نخستین بار از سال ۲۰۱۹ آغاز کرده است؛ این روند که در چارچوب مذاکرات صلح ۶۰ روزه تهران و واشنگتن تسهیل شده، شامل بررسی خرید احتمالی نفت توسط سه شرکت ژاپنی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666014" target="_blank">📅 18:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666013">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c077414a9.mp4?token=MqLl52wlszd6nA1CqTGJd3EFy1LgG0S8Kr4Hv6z6nh8Qfg2vOzU15X9zhqrbIOCXAmjOCTclINPij7AfpMYRHmxqKnpkR0UIuF5CD-9EfAfe-X9u0st_I8-QM8fAknXv3ZDvKV4mo-OmYLJvd6rhei-XIHD_ZRQX6l9LCAfd6wvO0XtLe108q2F_yABBmX8ErhQ37H6gf209nR0POvZ6NxP-nYnbAIDS5OBNwz5cn-AWWY_RqqATYrYcTbFed4Z-pCFHNUjYQiH5HAHvBWUB8Qf_sUfaoB1zRl2JcmL0LRmYgi9GWumlceDuMvypru5-TYzSNOkF65dVZO0_wjJGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c077414a9.mp4?token=MqLl52wlszd6nA1CqTGJd3EFy1LgG0S8Kr4Hv6z6nh8Qfg2vOzU15X9zhqrbIOCXAmjOCTclINPij7AfpMYRHmxqKnpkR0UIuF5CD-9EfAfe-X9u0st_I8-QM8fAknXv3ZDvKV4mo-OmYLJvd6rhei-XIHD_ZRQX6l9LCAfd6wvO0XtLe108q2F_yABBmX8ErhQ37H6gf209nR0POvZ6NxP-nYnbAIDS5OBNwz5cn-AWWY_RqqATYrYcTbFed4Z-pCFHNUjYQiH5HAHvBWUB8Qf_sUfaoB1zRl2JcmL0LRmYgi9GWumlceDuMvypru5-TYzSNOkF65dVZO0_wjJGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های قالیباف هنگام وداع با رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666013" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666003">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CG_z16Q9Uc5dzwOqgGW3mKYPpTV4rR99q0xHmqNN7SYTxnstb81X8l0dVFzjXX5Ie2NneFeODsCcJd-5W_Z2j8e0IoxjUjep9hFRylakj7EFJ5N3f-y8DEoA_QOes-6A0Ks4U8UeBlb2xTS-eMXnO_2ZA94D8IAvEUHwTIxA9aRxcNMsdn5Dzbjcm-mhEDZwDwOtWVZyLx_P6342Oqc4mtfEIybTjPUVF2IyihfizpSHmtuu13qCrKiTl5sZUGUCMQ7jRvki0AezrPcrHxg1w8FAkIMKylW-fXvwYtbbtXXzrLAsAlf4AbSM6VFTRaGSxn1HMLdCJ3jp5cn0ejKH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGYgN5nhi1Lcw2wqES36uw18UMifs6n8FaPbMF4GVqyOMp8jO4JLdXskjE2_4jNYXgOgTifPFh3DCBUeBWkf26-QIENK8mtYeuSJ7pPaf-IPFnbIdM_kUxbMcSUSr37Z1cqQDjRYjjb3VkAdZEHhe8Kmqqle1bp1zAU5AtHN8yLTRF-QUQC2YkVDCd1oNxIPGiFiWqLzUoH6B3RHbDqdXdHHIU2Td35EYEIfp5obcuNPKKC5DpIKDASeJFNJKukZsDy16WoFwlpkN4DmQzMgk-4zFN7H71KEaTMiFJM0eFKwcP3ljwaFH602Bbxr-3MHMPYs9Yltgb_llne8Q49mYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxl1wzGMB0lf9jKbXr-1a3_-Ea5bKKGBClxznCUJwW0TnuIoF31H-XkeMmy8rdkZvx9i3mPV8KjMnFPCJssPFB3sK-v_S6Xu4SxcWXJwqWfuPbnUnZbUI9P85nt66fnKmQrCIGEznkE8phGHzucs2g_6lxa-vRAKNDgXfkBRnpWN8c_ME5GPPlvdcWsA2hATM6LPjndxkKLZ-Hd2-q7BDOo2UbYtH4t5rBO7WML1x08cC4LGJC9jG0IqHgoXt2UnpVRfizkT0EDlq2oGWe9gJlcTtr-Qoy4UsnlLJMlg1sF3kJy7Mq3yqePEo6ciJDfIu2fG8ljHiGIK2ddUcvA4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4kxpHca-hrgDRjm-YDCeBJ6QcMxfhC_wFvAEvckAHcV5fAdT7sPJfvRpCwtGFeKK6iQdZKvcKGqhpGAshKj8-I7vi7vdGSa3FCaEinZvvyaJ6KWXiM12z15wV1UwTFRdDgDZGtJp2OXKFOlX0mmUbk8k9GAf0XVFRwy9rZFXOvs_gDV1ehT3DEkpsMHLDBr5zJjG84v22AMvBkIonvnRQBxWFa-iuvJ-7ZSMdKv7vE2SstBpp4xL-_MZrazUdEfd_SOCHNSlJRg63H5R3Z8diOKX5pO5Z8v5vOJONt41P3OEh8VySd4ymrsCoRtL1aK2Qw053Vwan6VhvNv0h_6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXxOft8cYxNK8c55IVlIe-iIuuGUK6RoFWlg-PEDtvxhdpkuwjgctmZxJ_25FSmkIERn8oSleMUihoTk3Abo06dMpW3f6J-tP3BiqbR6OwmAVFMqJlmZeXrhSJc00xIx0SEzo1vzNBRiT8ZNAEQBHrqWQsN-pKNNdwuFmkICkBaKeOJ3kw7T0Kfr-IYghYFA1VpvODIl-AyqOPMo_GQ9eqnUvBIUUGTlaQCFCel6FPfmKkIHb0aIsgCat3qw8-a491WU3mNoJTrwVY0IVmoGFzfWtDbvsmRSIkKyaZPzyVUC3ioIk9l37LEtUDx-r35OeU0QM3XD1MAdoSkvI5huxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEAMRL3MIQJYYZ7J4AtJ648sJ22BwCiShVyXWsws8dUiVOwhj2iwYMP42fP6WF-AKOCJQftXr9M4gfJoZV6zgLxm5oXC976aWFj73mAr4cQ6wVOV78xJkwphZfXMgpzcOcV7Z8lmjCNxq26ql0kBprvCqS1v0IO6YjJbcEbo8lorK3J8UnbVV1UMFjYH9qH_e5jfD8y_lhSx7DWdgeBvecrny9sl56FQxfjZswxD1mX4R_Sdqjzf6LboBftO2NuhLR4TDRpuOe0YY0q597K0N5myIH_bYQKcFcn3hQJKm6iWeUvlB2qbu7Cf1IcbIZZqKcc3DT3Qpiz4Mk79BkDfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O33_V33z2iTZSlQsQjD0NI6snOI6M7-Xy0BrCMFCtMDyCfYhJJzKdvB8aW-oye3tk9LmfE_zV494Cd_mK-hblxn3cnZNOF1oHw0LzlmvDUoJzkUb5BEXtyWpDoQkN_n6AQxFxhKEWsIdnHOiw0jUXpCcKVCWR3SOp7ufXq-ZWA2azqqDvc1JLv2B4ma2eA5zPJgrpuiMa7GQXLA02wyIu22oUKeApushZVcf8dQKFR888mLp4sb5Sv7FKKJViU1pSRa64NsaJeyxloK0CCu8_IlhFCxepJrQw8v4-p_j-QKRHquLNPJvU73O9iWs_HLZ1FbtKDHbR9bsfgrldVc5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rh-BKpuweUGQfR_8C-SH1AiBdMOtF8FBRHK1qv4zuDuqtX8wYb-9KhgbumxujFTZQbFMPWqHr6pRirOFPPbAg6fEV8Uymh0WESx4TOsjPmhOmwUnGvfmY3fXAxW8vSlhbHIRN1igmMmTMCS41_lCVUdwYW2XqhFgJHEOCxuB23Bfdv0eFBn46gzvwCMayA_NYutkRGap10zCDs-9JVcVlNCh9hwu2-4mONf1e5iVMCZg9QyHzBQ2xfCS-Xq0po7kDUoLBeLKN8CwfDEffkPYyPdujJYxkzIqJamDbSad96Dj2GAwyQ1KlcuaiqzERtcu8tCn3U0EK-sB0eRw_sa-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNQ-Sa1uyWCSALxMlo_ct8DmUUzl0I33wMF3LWULi_wfOGtWgXwSxddBbOW61zo7gRr83H6cOUWrdKvG510ga87FH1gsviRcD37G6TdKTDQCEgGFs7vGh7PpTAtH-MHY1r8ws7OUj7vHrlquZrH5H_SbbLdkmb1wyWzpcAohJtRdtwlc2Hc6MS5BnZtJ-3iFlqX_2vrWTunivSKKE7UT0GioceaU-A829XH23BqU_eRPFcaBvHTQzhESaTIOFXQOc_1S5Mx2kKddnreRmpFLpwHlT2EF87AhfS8nvV31XM_dnDTO-zxEBVq_FZ2ZZhbjKOIw198MbBUMt_Z985Ur2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqvkFnhhE9X7o5SILm-OpD-jMFTstDZZfMsBCy6cxj512ZK_41bmflgKPw7Pdr-oVpIEp8YBkYH3Lw9pAq51NYUD4SPtORbsqg0ChLbOilexKPk0N08uzizBfkEmf-uK5LWg2GTQL8o6LqaP-X2v5E4op1agiXyxyYGLJrtGPUkzxOFzXglfRTbDPXDaf055Irc4j3kYt5EWuKgoiAEhTNI-lJZCURsw3msYN041WaFlAd5twSs4Ty84-Nxv3eVCQmoUAAHFw4l7yOcG_D0lEU238UbAlYe0reJiDEjniMOw89r4gFkC7ranQ9oUIYuX5NBpXfuVO49ABCughY8DLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سران قوا در مصلای تهران برای وداع با رهبر شهید و استقبال از مهمانان خارجی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666003" target="_blank">📅 18:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666002">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=fk-9IZeGTxCkunJih09CsxQWPEJU32I3gAY_tl8wFjVPnRczxV45KAbLY9I9rEE87Z-tv9v_bgimmCw3Lcvfk3epBRxktj8bfHgG-moJfONn1rKePAYBQR4mST_Gv2zBHMGOwKxFDowuo_LKVi7yCRfLIfZ9hRb0QLN1uA-mmRqIO8fT_r1FbDAzPCXr-JXXzQrVopsXi2m5EGk22EQZE1bEwhnXgImLJEVS2WVDyS9dExyOmvMw-u4xgaBbS_VmbbBfjDA2pBZl1-yMoaehkMs97j3ycZIydH5P3Q-QEOE593qUtdBucE1lHO0-3u49dSWPjhS5KysRgOTY80UcdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=fk-9IZeGTxCkunJih09CsxQWPEJU32I3gAY_tl8wFjVPnRczxV45KAbLY9I9rEE87Z-tv9v_bgimmCw3Lcvfk3epBRxktj8bfHgG-moJfONn1rKePAYBQR4mST_Gv2zBHMGOwKxFDowuo_LKVi7yCRfLIfZ9hRb0QLN1uA-mmRqIO8fT_r1FbDAzPCXr-JXXzQrVopsXi2m5EGk22EQZE1bEwhnXgImLJEVS2WVDyS9dExyOmvMw-u4xgaBbS_VmbbBfjDA2pBZl1-yMoaehkMs97j3ycZIydH5P3Q-QEOE593qUtdBucE1lHO0-3u49dSWPjhS5KysRgOTY80UcdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندۀ ویژۀ دولت هند به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666002" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666001">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMKAPH1AZ-51a302F-Phxkdnao5CSOBhTTCW5ZVEVijWgrgTVXyBnjJWIDRsxqw0PiD_Szohi89Vc7aJVqA_EcNYhOaGs9w9O3_Zq09ov9appv3K5zjqVARViHrPGM02cmGdo5vCz_uuSqDjekGyibcR3tKdwCAd2eLX49QMt3Y8uKY3gEPLvwlS-FTT_0SSSlIsyT4DaYf68L2aA_jjak82T3mXMEDpXvKApbqVubgTGYADM1PEIWrCcgO3wqmhHevgmJg1EiP0_rr1rNEOZREJUrH_UFnfEd0jBAo8gFsca_wXCpsb-9qpii1H7eh59NyT5v6Di7_GAkR74EHHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاگرس؛ اصالتی از دل ایران کهن
«کالکشن بهار و تابستان پوشاک زاگرس»
«برگرفته از دامنه‌های زاگرس»
📍
شعب حضوری:
https://zgrs.ir/b
خرید آنلاین:
https://zgrs.ir/hz</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666001" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666000">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=WXllNUEfm5y8eUFJdiZjtfHZTasXaVgyOPTCvuRKsBYWqOLwoLgLOy9gcY_MmjFpwmfAiMFKb0I1PkGxDfcqKXoalSGG5ONoRWiMjEGrB9fqV--1uH498CrFo08jtCjuL3AtHWYHl2Trm5aQSE1ze2idxw-zFOXYvmCkzvQ8ABwjkshfGMLKmxvgYrYRe9-8bcqQBJzlT1tZUsby8Ybu2n7GbWzCefjUip9BuFr0GEHZWxJEC18oziWnS2VlxIv9HDbd-eHR_MBTVAcKhFvKy2gstos1b7_n9V8GwW5o-_5G2O_5BwvxrJskU3X19Rb-7TETfEi3nXX_z4nKxJECpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=WXllNUEfm5y8eUFJdiZjtfHZTasXaVgyOPTCvuRKsBYWqOLwoLgLOy9gcY_MmjFpwmfAiMFKb0I1PkGxDfcqKXoalSGG5ONoRWiMjEGrB9fqV--1uH498CrFo08jtCjuL3AtHWYHl2Trm5aQSE1ze2idxw-zFOXYvmCkzvQ8ABwjkshfGMLKmxvgYrYRe9-8bcqQBJzlT1tZUsby8Ybu2n7GbWzCefjUip9BuFr0GEHZWxJEC18oziWnS2VlxIv9HDbd-eHR_MBTVAcKhFvKy2gstos1b7_n9V8GwW5o-_5G2O_5BwvxrJskU3X19Rb-7TETfEi3nXX_z4nKxJECpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندۀ دولت تونس به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666000" target="_blank">📅 17:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665999">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شروع فعالیت ۲۴ ساعته مترو از فردا صبح
🔹
فردا از ساعت ۵:۳۰ صبح مترو تهران فعالیت خود را به صورت ۲۴ ساعته آغاز خواهد کرد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/665999" target="_blank">📅 17:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665998">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce7a7ff500.mp4?token=iIX2MQuHE1WrJsMFAP4ZH_AP2r3lB7GbPS2Eh1m0KYczDWjvR52MXlFJzSM3-FXZbkX9LMR7obxgOSR0pbdm6sDepbvg8DhojhGWHCyIJJeqjvh5yDqACp_lkhDLw81csV8c8VUVCafUc2yt3kudqS_exrtgkFjiN8bpJvJEtuuVddgssLuVpHkYoitRKMHe8lR-ygrDp9YWx23dBV0Q-rxHa6hqCnbG3DLMbNyGNBQih9Lzuv4is5JZnX_ja2eVSaQNwQx56Vt1XavA9eSOckRNlODl7h1Hnp9Azl06aJmjYs2M3Zsldt_oRGYJAIpvjXSoGvFFf5IvyS-ptUpYbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce7a7ff500.mp4?token=iIX2MQuHE1WrJsMFAP4ZH_AP2r3lB7GbPS2Eh1m0KYczDWjvR52MXlFJzSM3-FXZbkX9LMR7obxgOSR0pbdm6sDepbvg8DhojhGWHCyIJJeqjvh5yDqACp_lkhDLw81csV8c8VUVCafUc2yt3kudqS_exrtgkFjiN8bpJvJEtuuVddgssLuVpHkYoitRKMHe8lR-ygrDp9YWx23dBV0Q-rxHa6hqCnbG3DLMbNyGNBQih9Lzuv4is5JZnX_ja2eVSaQNwQx56Vt1XavA9eSOckRNlODl7h1Hnp9Azl06aJmjYs2M3Zsldt_oRGYJAIpvjXSoGvFFf5IvyS-ptUpYbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم تشییع شهید مصباح‌الهدی باقری‌کنی داماد رهبر شهید انقلاب #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/665998" target="_blank">📅 17:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665997">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ارتش یمن بیانیه مهمی صادر می‌کند
🔹
سرتیپ یحیی سریع، سخنگوی نیروهای مسلح یمن اعلام کرد که نیروهای مسلح این کشور ساعت ۱۸ عصر به وقت صنعاء (۱۸:۳۰ به وقت تهران) بیانیه مهمی صادر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/665997" target="_blank">📅 17:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665996">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار اردبیل(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139ef7c55b.mp4?token=nnTUQZr5FH8mkYu16DQbNYN7vOAFyjhoYHb2mjue33Zd0iBWUPhdbLKNbdSJwFCp3kSwfHXz-a5MB34iQJTyjzYw2axJNCWgkPUJTLBbrwDcewtlV4BZriBgfPi6VvoHft1nHWzKx_Pnp7adyqqx40xfhqC6lEKmN4HsTsU8OJ3oIfU7EunfgPBsPboMcBLbqYgl6EtYkFHKmy6h8pvGec9--_0gN7fzuBdO97jSxo7SFVTibsfvwBiEXJ7BYHORfqN2sK51vy7LjTSPP4eFutDNIGw9t1JLQ2giiMvDYWIbtugLvAk2Ybhu0cXP0KvhuUkAZMiL4vZFiOX0E2oURoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139ef7c55b.mp4?token=nnTUQZr5FH8mkYu16DQbNYN7vOAFyjhoYHb2mjue33Zd0iBWUPhdbLKNbdSJwFCp3kSwfHXz-a5MB34iQJTyjzYw2axJNCWgkPUJTLBbrwDcewtlV4BZriBgfPi6VvoHft1nHWzKx_Pnp7adyqqx40xfhqC6lEKmN4HsTsU8OJ3oIfU7EunfgPBsPboMcBLbqYgl6EtYkFHKmy6h8pvGec9--_0gN7fzuBdO97jSxo7SFVTibsfvwBiEXJ7BYHORfqN2sK51vy7LjTSPP4eFutDNIGw9t1JLQ2giiMvDYWIbtugLvAk2Ybhu0cXP0KvhuUkAZMiL4vZFiOX0E2oURoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفرِ رهبر شهید انقلاب به استان اردبیل/ مردادماه سال ۱۳۷۹
🔹️
اردبیل، نازلی صَدَف، سَن‌دَه شَرف گوهری وار...
@akhbarardebill</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/665996" target="_blank">📅 17:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665995">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
درآمد ۵۰۰ میلیون دلاری ترامپ از پروژه رمزارزی خانوادگی
الجزیره:
🔹
دونالد ترامپ در سال ۲۰۲۵ از طریق شرکت رمزارزی‌اش (WLF)، بیش از ۵۰۰ میلیون دلار درآمد کسب کرده است؛ سودی که با یک معامله «دیپلماتیک-رمزارزی» میان واشنگتن و اسلام‌آباد مرتبط دانسته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/665995" target="_blank">📅 17:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665994">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=dKw3iBYMXtrMU7Q-K5B90Qmhmu6WLbHinxASCe2fz3L7vYIkJI1PQfgQ3IwOvsg6Nc0cuamzp8sq03nUj-cFHiIkLCqwS4AVvPGsswKXi6UDvzW98uwrmOw5Zhb2gwu7XPubDnB5VTLYMW4WThjVm_XzCZgUJoOtocG5Qs6UpRwRQ35s6b7bqbO5ltFpvDQyAenf-9xRJ9XPOZSCBX_emN5wUE0RuXWnqSUkzAMrC8fQ0VlEBPBLIRstZEvZO_h4saDEPvRCsot3jeAVFnJiw0_r1IdPdEG5H7W9Mew5SvYoQ9nnbFKLYNakwjkAuOGXwbT0iS1czVpHsgTtdJyUHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ac75c7af.mp4?token=dKw3iBYMXtrMU7Q-K5B90Qmhmu6WLbHinxASCe2fz3L7vYIkJI1PQfgQ3IwOvsg6Nc0cuamzp8sq03nUj-cFHiIkLCqwS4AVvPGsswKXi6UDvzW98uwrmOw5Zhb2gwu7XPubDnB5VTLYMW4WThjVm_XzCZgUJoOtocG5Qs6UpRwRQ35s6b7bqbO5ltFpvDQyAenf-9xRJ9XPOZSCBX_emN5wUE0RuXWnqSUkzAMrC8fQ0VlEBPBLIRstZEvZO_h4saDEPvRCsot3jeAVFnJiw0_r1IdPdEG5H7W9Mew5SvYoQ9nnbFKLYNakwjkAuOGXwbT0iS1czVpHsgTtdJyUHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو ادعایی از حمله امریکا از خاک کویت به ایران با موشک‌های هیمارس در زمان جنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/665994" target="_blank">📅 17:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665993">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632090959.mp4?token=t5xljek_o-E3aOqn9MBfC6_VLnPYLyaAqRjhmk3e4A6EfjvdkA9imnV4YheZWEszDsHB7DXQa-fEMjt6UueQ2CWvxktKiZqAnNaSlGv6ophCDfxGAeUmL-Tmzd4dzMHvg4P6O-usYlh56khgPSRLGyk3PKVrI1MmHiQRAPnkRyL5nRTMl5IFf_p26IB82DynbVfnkVqmkbN3szaN-cspRPVnXDMdILqAtZaRNI4hyA78Jh_JR97NuPM5oGkwHKTEkf6uAY9vBF98eVEq9cmB5CJ-evO4R6UPqd811gInYcL38dMzZcRctTuA1FIWblylneFTTqf42yf8so-OFw4OLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632090959.mp4?token=t5xljek_o-E3aOqn9MBfC6_VLnPYLyaAqRjhmk3e4A6EfjvdkA9imnV4YheZWEszDsHB7DXQa-fEMjt6UueQ2CWvxktKiZqAnNaSlGv6ophCDfxGAeUmL-Tmzd4dzMHvg4P6O-usYlh56khgPSRLGyk3PKVrI1MmHiQRAPnkRyL5nRTMl5IFf_p26IB82DynbVfnkVqmkbN3szaN-cspRPVnXDMdILqAtZaRNI4hyA78Jh_JR97NuPM5oGkwHKTEkf6uAY9vBF98eVEq9cmB5CJ-evO4R6UPqd811gInYcL38dMzZcRctTuA1FIWblylneFTTqf42yf8so-OFw4OLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
آرزو از پدر، برآورده کردن از پسر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/665993" target="_blank">📅 17:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665988">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DonzMTdA1phrUFV4lO8l1_0Zv8xlOoDHZVtjj-SgKR-uH7kXoWYc99JiBVPx433dMUEfCZfp_IehB2W7clvj5O5_RJLDcDT-2N3U5W4t4CwbujUppN-O7Mg5vb_9WFZrdWG9ktDMKHrb3mNQ1Q_vSL5XXYHFrhIFrwaa61p1qRSQvU40G72n6XmgcjsKIi05K-rmGZssN6cyW90qRfV_5YN3E_CQXxG8cFn6pZLElPX7lvQxpurnaTBc988eLDaVzsElPXMw1KwXMI5tIqp2T1PU5yb_K4yBcrOn0esZ6WnA1O-yyZPATFGlzp7Zl4uf2n3yJDMPwXE4CqtUDEoOwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ed8lxXXvQ_wp87gUXlobQ3HjqL1SnRvXJ0JQHDY9EGesGBv2bowuoWAD_Ww4P-A0bXasHq5qeqdhVZjFl3cJkRHEx21hNpfIq3suTfjMGHYoVqViXmnKIK7UlvZIuaJmEeCQE-evrHE0ETOguQenaE7HARKErLdxFh3HamJZAZgBAQCBkeyncSIYlCFXtMqE-shVHRzbEZ6vhrHGwRngdUwea9NfE4hnoTTXwauMVP10neu3nHkDn9XDi3HrbjV4sedmr0tgvAGlEsfoySmiPpSn165Qr3WFpjDDy6EgtqMtuE9j-NDStuQZz3xPv4k06w0uiIB41g5hQH5-hlhUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7xur1-E36Wl47vtsPcLMe5cyj9v0sifqx_Nbefnr9coVIykeOpsyQicrjwifPUhD4qyL8Gk7qjhTtW410gIJJLbbgS3KaDh8pPDizNyvPvPRqNQH2rdntdzpvnyCjRJE8QxhzdQnjyWErxwbPOI5-coCVdh5C8qmSyMneIvHBv-Jf6GmZxcUGURC5Elu2cGPPS43_sqoHY92rlF4OJXRpmyf8j_NVlAu7LdqkLIvtCTLiRg1U_-47aF3RUn-ekfQh5OyWpVpT21l3DLghbBMyArWIZSzkxvgnm1t1PMNAlEWzH6hKnJO-jV0y9vv0rRfTYWx4FfU-naceqzFTvOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3Om8mw1_uSL_hTxQITO8k7RXR664zkpdLcmPsxYEhW3CFgAW2l27h8BMjO_jezyAJiJ9zstviuxrekTqm-92IsMHudrpR6ksxtE4eKKW3MDsizXVLTyXQfHJor84GbJI2GRv34_-SKlumEbGkmAA8uuQR6eYQov8AoMi-9h6IDk9lRpPbbs77cmtVnpNACZEcf6DTNDdI1Yv8Y53rgvbmXyKZnsi0RvcSrZ-nblQgQ1bMSia9etxBVLLPW4S-KmdSv9kblCLlrchoE9ps1IQX1uCH2grBamdRGvTaRqqY3psESGJBtF1PFIrp4ZvFANHzQl25hc-irppGwdMp9kyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CR_cSsUkrKedTyqriy-Egz5GPi5UZ5HJ8UkfmasBtjSpY-hLWUsMJfgkVGKa_x6QfAXk6tieqVVs-GxIHvVpLFlN5_KimlGTDozJC0k75hkrWfiPMVJF-3H9iORCmE3mxtGuW92LM12qi2p88FguRfYwRzDx70Rd9IltKMNPXEAOOg0tur4JvEA_kmzocgx5uqcU6LFZstU9cRsv_k-E4PXN877zXuKVoahu2Nvzh_qbhu9N1DqtOEkGE2QN7YWwTqt3l4Y4ftp9b3NNRIkFta-z4fq4dRo5djIm7VykFr5S5jAGySJfdovAj1HqB_XqmgQL2ITDWxGQaKVR4VfkbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گلباران محل شهادت ۲۹۰ مسافر هواپیمای ایران توسط آمریکا در سال ۱۳۶۷
🔹
عکس: رهبر امامدادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/665988" target="_blank">📅 17:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665987">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c70f74be.mp4?token=omdGspvUc9_PrSr537ov9WdmzW0zFHrfvLN-CUWoiF5V-SkQ_AJl0UCCDm7KoTmkODbN2uAb3wHzrL9ERqwWqUSg080TJnniXyV96dl82gJlNITjsdFH5DOKFXZ5xuLvx1MRp415L95HxqDwTiRyIaDNEiK4RE7jN41_2v6Xe1F6lR8gotwopPs_BawmGXV7SC5J-LuVND82oZ3vYlMuoL495ZGwdtPmeemcvbGfSlTgusOj5ZIAz7wau6-U3Iz-0NcYxyHjE4FsFbwsjRdm3L7pdFqHGu9Jmi_ZNB324x_LAX2sTQmX0Ru_ZRrAZrjCgpUwAHbHTxVxI9VxhGAvVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c70f74be.mp4?token=omdGspvUc9_PrSr537ov9WdmzW0zFHrfvLN-CUWoiF5V-SkQ_AJl0UCCDm7KoTmkODbN2uAb3wHzrL9ERqwWqUSg080TJnniXyV96dl82gJlNITjsdFH5DOKFXZ5xuLvx1MRp415L95HxqDwTiRyIaDNEiK4RE7jN41_2v6Xe1F6lR8gotwopPs_BawmGXV7SC5J-LuVND82oZ3vYlMuoL495ZGwdtPmeemcvbGfSlTgusOj5ZIAz7wau6-U3Iz-0NcYxyHjE4FsFbwsjRdm3L7pdFqHGu9Jmi_ZNB324x_LAX2sTQmX0Ru_ZRrAZrjCgpUwAHbHTxVxI9VxhGAvVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون رئیس کنگرۀ ملی خلق چین به رهبر شهید انقلاب #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/665987" target="_blank">📅 17:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665986">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=Wxm3owcOm-KLC79Y3gqbpPHuT4PfCvxOy3uaI1sS0u9HndGx1eDvInBAXKDvAo6g6stdiKK7vcnOgHZXvdxZk7uOSZMNRJ4xKGR1a9H5Q4EE6mVi96w8HsYk2LfyTJlZvMQVU2zDaHljrk0sriyzPV_HyDfFe7FwvNiNH417THXMTRTgKh0FkUZAvWLBtrTwdQ7NKuYMl26bVK1aetRR9TZPyY8qRJU5TqlCevxMXsh2Q8Gn97YqLgTIs_Lk0mU-1tN0-UE3A_gDSO8TGXj5pIYabC2qgr0FtSeGWA9p7YVIQJkbV603pPtj-qOyICAdsIfBhFm9U933e9Fn0R4XMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=Wxm3owcOm-KLC79Y3gqbpPHuT4PfCvxOy3uaI1sS0u9HndGx1eDvInBAXKDvAo6g6stdiKK7vcnOgHZXvdxZk7uOSZMNRJ4xKGR1a9H5Q4EE6mVi96w8HsYk2LfyTJlZvMQVU2zDaHljrk0sriyzPV_HyDfFe7FwvNiNH417THXMTRTgKh0FkUZAvWLBtrTwdQ7NKuYMl26bVK1aetRR9TZPyY8qRJU5TqlCevxMXsh2Q8Gn97YqLgTIs_Lk0mU-1tN0-UE3A_gDSO8TGXj5pIYabC2qgr0FtSeGWA9p7YVIQJkbV603pPtj-qOyICAdsIfBhFm9U933e9Fn0R4XMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندۀ ویژۀ دولت مالزی به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/665986" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665985">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2ac15614.mp4?token=YP8xUenyR6yWplhFjJonYtlPqPa3mM7NSIA0mWupDrTa9GEhxG8XJfrox7xhn0rBB8I0i0283_-cwoG80NepzLlF8UU_FLAK0bZ8p0ME2QegtaQO6M6u9qnGMDyO8PTPA8JMcEhxAddGQkC4U3X_izsvAt6_9y6LjMZev9wWxwjXne5SIBHy6wot04YK_gPtOrTuA00RS17y4MGhZOnyVsmQVRwBKahqSOh5h20ZA0zH2ZFCzQj5EyOjPIpC0E5qroYC2USxQGUFfg43b8Nrp0puNPD6eY2jT0w2J9XVhVhw0PAGTvNDaCrEuRsYFixlEDrnVwSBrBYc_yXdSwHX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2ac15614.mp4?token=YP8xUenyR6yWplhFjJonYtlPqPa3mM7NSIA0mWupDrTa9GEhxG8XJfrox7xhn0rBB8I0i0283_-cwoG80NepzLlF8UU_FLAK0bZ8p0ME2QegtaQO6M6u9qnGMDyO8PTPA8JMcEhxAddGQkC4U3X_izsvAt6_9y6LjMZev9wWxwjXne5SIBHy6wot04YK_gPtOrTuA00RS17y4MGhZOnyVsmQVRwBKahqSOh5h20ZA0zH2ZFCzQj5EyOjPIpC0E5qroYC2USxQGUFfg43b8Nrp0puNPD6eY2jT0w2J9XVhVhw0PAGTvNDaCrEuRsYFixlEDrnVwSBrBYc_yXdSwHX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نائب‌رئیس جمهوری یمن و هیئت همراه به پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/665985" target="_blank">📅 17:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665984">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=tj0vvdPV_3rM-TZWf0xa9tHbu-gtCK6mXvk4Mx6UbyOTS4YKJqBqxtCqVlb52vio0iBgARFy4tHdRD-LNZKcQMHj7xuKJb-3fba6ErWYePP01T6ejTGdBpzEvHU2lzBbl--kNbTVUepdY65XpqN7KvHEubIj4BnDJZg_41UqAsnTLLje-Rzzhv0ECTbPBKnW1wcXVQ7wGuyEABEeSg63-jldWRY4BW7LMxFZ2wVGUgPfyM-pvmBTpt28UwvsJXT2FKxAyvFjBlzNcvScGuqLpeTzRq3qaCRma-7YA2T6nhTmtpObO73MddjXK2ie5SDRVw8ce0tZT4CSHnjK8tZreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=tj0vvdPV_3rM-TZWf0xa9tHbu-gtCK6mXvk4Mx6UbyOTS4YKJqBqxtCqVlb52vio0iBgARFy4tHdRD-LNZKcQMHj7xuKJb-3fba6ErWYePP01T6ejTGdBpzEvHU2lzBbl--kNbTVUepdY65XpqN7KvHEubIj4BnDJZg_41UqAsnTLLje-Rzzhv0ECTbPBKnW1wcXVQ7wGuyEABEeSg63-jldWRY4BW7LMxFZ2wVGUgPfyM-pvmBTpt28UwvsJXT2FKxAyvFjBlzNcvScGuqLpeTzRq3qaCRma-7YA2T6nhTmtpObO73MddjXK2ie5SDRVw8ce0tZT4CSHnjK8tZreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون رئیس کنگرۀ ملی خلق چین به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/665984" target="_blank">📅 17:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665983">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=c6BkD_M06VJXn8nfERxCpfL5IXGVUydnKS3CagMRm_EmglLBwiOOr4eFhM2yaiouo81HveaoZUi5v4u7lLJjfOAcT06CMzwkLQs1WISFArSJsZe_NdMdtGkPZSBjeyA5DQG5E60cDwSahEovR4PgiCZZOiOlhK68qcuQD3B4oC-HiuArnhlufQl1weQnmY2-AsDAVZhXsO1wn5Ir0B7yhM84te3FD3z__x-xOGfs7ihldQddFYc3tzUtcrvnFa6CyZ30QX9JtEyd3lRuRorgGWdSNtn4JsViOcldws0RzpDlgIv50S4tZPLxvvnZOf12RoKZtO-FOoo2bK0cdBx8mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=c6BkD_M06VJXn8nfERxCpfL5IXGVUydnKS3CagMRm_EmglLBwiOOr4eFhM2yaiouo81HveaoZUi5v4u7lLJjfOAcT06CMzwkLQs1WISFArSJsZe_NdMdtGkPZSBjeyA5DQG5E60cDwSahEovR4PgiCZZOiOlhK68qcuQD3B4oC-HiuArnhlufQl1weQnmY2-AsDAVZhXsO1wn5Ir0B7yhM84te3FD3z__x-xOGfs7ihldQddFYc3tzUtcrvnFa6CyZ30QX9JtEyd3lRuRorgGWdSNtn4JsViOcldws0RzpDlgIv50S4tZPLxvvnZOf12RoKZtO-FOoo2bK0cdBx8mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون دبیرکل سازمان همکاری اسلامی به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/665983" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665982">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtybezPfjjxaDhWd2wYSkwF2pE2DXBUoTygMOjCHDr1vNGQlu2k_vuUJBbUnGHbGsKbwhB3P_kQa9y4K5T-qM2L2w8k4-xlqsC91RJeY9Ge64x0lbQFPRLTrsa0dpWG6okFQXcrwaYXV8-XDWqcWuXMIo8ATA1InRBvW6ML09cNsSlRKwlYcHE7v5TQIUwdxWLhJbU-SO13pmMFrqW-sRcz4NKCjjUB92e9V6i6PnEd5edbjEjeEPJJtYwJbZJmCxLcfsciVTFmjEuY7hDYOgzyDXAZNh0V5b64uzdnbuwj2sXC1_w7hu90DX_lL0Lpcx-ree9aTpoSjmxaKlqGs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمانی مراسم وداع با رهبر شهید با سالروز جنایت آمریکا
🔹
سخنگوی ستاد تشییع، همزمانی برگزاری مراسم ادای احترام هیئت‌های خارجی به پیکر رهبر شهید با ۱۲ تیر (سالروز حمله آمریکا به هواپیمای مسافربری ایران در سال ۶۷) را نشانه‌ای از ماهیت جنایتکارانه و تاریخی دشمنی آمریکا با ملت ایران دانست.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/665982" target="_blank">📅 17:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665981">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f186ac745.mp4?token=dR4xTcta5nqWLmTNhhAyQTOrxi54VwQEyvgFAVUcbEYtvGeX0TdDS2K9gY4aValb26XOgIWfpyhlaHkt8NEAhM8AVmtIdb-CyC-ShFSs0myjIlG9PRHSm6QH9Jz-LY_-zAjNQHx-9SiDbXvWchCmQxcEIdYAA31hWWQsr77E3AS629oK0DaiZX4mCzMjsP-UY_KP_CIL0s4kLs2aA9DVzmk7gOg4OKu2FSyE33Jk_vF8Sn8uno2OLnR3FCBgwIyPpR_Z0RzQ0Fjg9P8E4VUaITIHcel9OwbG9kY9NcnM_Im94HVFRmDQzBHtfjwqvOOBF2oFjL5YC2eXhvjAE9h1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f186ac745.mp4?token=dR4xTcta5nqWLmTNhhAyQTOrxi54VwQEyvgFAVUcbEYtvGeX0TdDS2K9gY4aValb26XOgIWfpyhlaHkt8NEAhM8AVmtIdb-CyC-ShFSs0myjIlG9PRHSm6QH9Jz-LY_-zAjNQHx-9SiDbXvWchCmQxcEIdYAA31hWWQsr77E3AS629oK0DaiZX4mCzMjsP-UY_KP_CIL0s4kLs2aA9DVzmk7gOg4OKu2FSyE33Jk_vF8Sn8uno2OLnR3FCBgwIyPpR_Z0RzQ0Fjg9P8E4VUaITIHcel9OwbG9kY9NcnM_Im94HVFRmDQzBHtfjwqvOOBF2oFjL5YC2eXhvjAE9h1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام دبیرکل سازمان همکاری اقتصادی D-8 به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/665981" target="_blank">📅 17:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665980">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ceb73e56e.mp4?token=CVX8JIe4XaV431FijnkwBcF5ASBy7HNP-NyPVmeqi_G20nfL_0slG4ZCWcd9Ts7gN0aIYmJGfKj_13z30fQ37Q9a7Yt8Tmt1wYUd6CV-mqbf4DRj24BDSXry32gFuy7lPQ3q3ee0DzjbIID_71l1MS5_Zvi4vB4Hqj-IIag5buUDxGatTi8w0yBMd4UVpITuQHQ2PTe3vE2R1gTO5u25xpUfNYfpFOafedmxoV-2R0s-rW4Db6v-s1rxJ_ylDHgxg_yB6Rf-Y96IlO8qUTRwSOC9aI-PyDBcKW2LQ0IfF1PxgxmqO3UNuRADVx5md8LQf_Ohr7IJqxwoygOnsTkRXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ceb73e56e.mp4?token=CVX8JIe4XaV431FijnkwBcF5ASBy7HNP-NyPVmeqi_G20nfL_0slG4ZCWcd9Ts7gN0aIYmJGfKj_13z30fQ37Q9a7Yt8Tmt1wYUd6CV-mqbf4DRj24BDSXry32gFuy7lPQ3q3ee0DzjbIID_71l1MS5_Zvi4vB4Hqj-IIag5buUDxGatTi8w0yBMd4UVpITuQHQ2PTe3vE2R1gTO5u25xpUfNYfpFOafedmxoV-2R0s-rW4Db6v-s1rxJ_ylDHgxg_yB6Rf-Y96IlO8qUTRwSOC9aI-PyDBcKW2LQ0IfF1PxgxmqO3UNuRADVx5md8LQf_Ohr7IJqxwoygOnsTkRXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون نخست‌وزیری تایلند و هیئت همراه به پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/665980" target="_blank">📅 17:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665979">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aceb48cca0.mp4?token=aw5F2uanrLuGUA6L1hGiK9EzAcedS-ct5yqp6FnPP7_RPldSJCufcNUEZEbnO4MjE35QkRYOQI4JWV4b5NQxfM7JH5ckd9G6NLhTiEPaQYA_mAfGl43s427vcai0wi2PDyKTOKXxmZ2ZNfyVKhTkykaMu81R2Q_Vg3vYNB5qIA_WAOTdgc9tsazXPK2xsuRdSu6g9BOa7R55MyWAJK0hWZbd_95wRv1mRPV-_ydGp2DHHm38Pn6rLY_Fj5LG5YsYdTkgXdGnDe0MEvr7xtLWN4kg4toJ682muUOTxJkMXtOFJ159pDY-PL-pn1RyWyBHBYnqxlKQt_2v8PSvxATdOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aceb48cca0.mp4?token=aw5F2uanrLuGUA6L1hGiK9EzAcedS-ct5yqp6FnPP7_RPldSJCufcNUEZEbnO4MjE35QkRYOQI4JWV4b5NQxfM7JH5ckd9G6NLhTiEPaQYA_mAfGl43s427vcai0wi2PDyKTOKXxmZ2ZNfyVKhTkykaMu81R2Q_Vg3vYNB5qIA_WAOTdgc9tsazXPK2xsuRdSu6g9BOa7R55MyWAJK0hWZbd_95wRv1mRPV-_ydGp2DHHm38Pn6rLY_Fj5LG5YsYdTkgXdGnDe0MEvr7xtLWN4kg4toJ682muUOTxJkMXtOFJ159pDY-PL-pn1RyWyBHBYnqxlKQt_2v8PSvxATdOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم تشییع شهید مصباح‌الهدی باقری‌کنی داماد رهبر شهید انقلاب
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/665979" target="_blank">📅 17:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665978">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dcfe28f4a.mp4?token=nhFh7wLrMr3LDts-fh9aFZ4-WnlsMIO3-W_0FCm_0aNVTSKOzTTMdRlO5Ysq9XT75FxPzYMAUdD1w16Ji_vDgQuK_hfNSdIo7n_Jfst5FAiQQ5lKdzgIkubZLOpD2qH-K8oXGW0NgALlxBEupuZUFGGDhpqjB6IUP_Sa0ZP3Sq0txey34pFOmiRL-CiVt9wj4PzXxonZajxLOW2P9HpjYwy_FQo-pRf_6pd6qXHHRsvJ2u0UY_0i39k96mtbqvYMD_B4jmcymijERyIrcfwijrza-7Kw7aGPtN7BkfxByo_GaFi-SoPH3OmzT7gcnR0d5J2lScZjMgO-XqTO6HGhFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dcfe28f4a.mp4?token=nhFh7wLrMr3LDts-fh9aFZ4-WnlsMIO3-W_0FCm_0aNVTSKOzTTMdRlO5Ysq9XT75FxPzYMAUdD1w16Ji_vDgQuK_hfNSdIo7n_Jfst5FAiQQ5lKdzgIkubZLOpD2qH-K8oXGW0NgALlxBEupuZUFGGDhpqjB6IUP_Sa0ZP3Sq0txey34pFOmiRL-CiVt9wj4PzXxonZajxLOW2P9HpjYwy_FQo-pRf_6pd6qXHHRsvJ2u0UY_0i39k96mtbqvYMD_B4jmcymijERyIrcfwijrza-7Kw7aGPtN7BkfxByo_GaFi-SoPH3OmzT7gcnR0d5J2lScZjMgO-XqTO6HGhFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام فرستادۀ ویژۀ رئیس‌جمهور میانمار به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/665978" target="_blank">📅 17:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665977">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/665977" target="_blank">📅 17:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665973">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfJsd4uYdZp1i8I98XlZlYEmHmVo36nUztPRvXV5_hUFb4rsHojVI-FI31AmgEQk6XjODdPceZpDm9QrjDGGNlZOOj9kOgmCajfoN6H9iULjzBBvEV862TO-6c1BFnh7bZm-7ugOwHZq97DZqQDet39lU2BlOQqXPFvphlHAxeMb0IcbYl1bcJUAtLd4b8NJ7PNKnnbLHkBGPUbD6pV-WnpcaPC3sRh-U0ZOt9Xhn1GAbs0vgAllhR6JgzUa5V9dRqdMVTeObwOjQX0BTeTb_eYVy6PSGhd-xXoNJITOt6SL7LiGEAdIP2K0ertB1ovWbC1O798s704a_ZnhkKoFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bx0QeBlR--7K99iqvbCI9W_kCr0pig6OD1N7R7OElvcCYzVcT87pv5Vua8Nb1a49upi7NQgwNEIHpAx4HL7PoYs5VAebeQB4H4RGVZAVcQdFXITEQxE9jnhiV4AUKdOV0Z-T4nHLwBy7pCDZcEpRZSGtPK_B_3sjBMrF0LAL70aaIMOFVA8-J8CKCJai5GQhjA9LnuJua7Bd4eX-8Vm8pEiaFYLrjn032soOa_AdiyJ9-2qTyxg1NkkyU7ZQF2qXY_rXh9oiBZcpPUUK_vzg3YJ2ySM3NQeFQG2WRoZSp8bDSJZobkqp60fL0hJz2lzz67ZjdBLR4qY9RQG5KyWDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjZ_ht5tVdr707yZvziKn4m54FA7tfJfhz6itMeEyuWnaWON7sxYWaknGOOMsf3K0oxiGzEp9t4mrBGDItspyIbuwcVId55xeGuHMk1jYFdZSBKrpVp-16hUj_5kRdLlOjVieSf1ixSrsJYZIrlBbzMSUCF6hfqEScFrUyfr3dGokHd4pUhhoMK7UsiQnbJxLMGynpAekH9UAFJ1dan1KOKwkYx6B3ZfaNE7oWF9rvxlAFg9PGFiHvWez9dxtSGu2o2uEY7HrYYIKh1mfN9Z9TVNwPipehl4GEvzyBEeKn__tYzKJuXkAB-e77Vt-Xy9mqxfRM4_flbYjsUgB-EBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxmnDIk7jZvA5Wl9ubB1RFI5OZJwCWGlY9fRBvfcHnf5DO35lKYe_ZMfmyxdaImSJv_SnPxIbet4WCCI515niU3_wZul5exaro4pTJ8N4mFofYCL0Y7HO6A37NsEr1ZG-LRw7mUIHspeSItQPxOxInAcMKg9cETQ31wTYwRVm2l_23QI_CFQHnsULLmyDZ5f-bMmklEQxEcVsBseI2EZpyFC9b1ETt0jOD4C9Xyda8dMuZw4yvOJw6qMu163wVUdYiktxFomgf6Hdp1CHLEpG4bame3CJCBUn68yq_ZdGkQDQ_oZ-EBwEBfwsm73xcs5A-36xf--heT7fuLTms32Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ادای احترام نخست‌وزیر و فرمانده ارتش پاکستان به رهبر شهید انقلاب #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/665973" target="_blank">📅 17:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665972">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc21aa2be.mp4?token=Hw6eDKx1WTZkGukfaMlMHLZAsb-QD9MRZV2IlTaII9OEbD2ISNmww7T92HhKXR12FzxzOCtCPXGPMHIVNsKB8ULaSTcEaSUJqpFHAL_k8zRidQn3pEU3eDssd3daUCxPBzBwoHsW5ryVaE8WxECXwcA469z_zNRc5u0aXlQ0GPALX2Va5fnceyRjxlRToTtnz9JX2k3jW5Qnkl6zJO4BkDZG9YwFzOCaqcfrse-z5djj2URJ8ejDKdSIYjw0Icx8lgxpa1sQlS6B1niKiFxHWfsX1KpA4uigdY0jO-Wf1JO4xvn-1f_1t_9degzdfW5enDku9cNZfr_nmzuRHmfpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc21aa2be.mp4?token=Hw6eDKx1WTZkGukfaMlMHLZAsb-QD9MRZV2IlTaII9OEbD2ISNmww7T92HhKXR12FzxzOCtCPXGPMHIVNsKB8ULaSTcEaSUJqpFHAL_k8zRidQn3pEU3eDssd3daUCxPBzBwoHsW5ryVaE8WxECXwcA469z_zNRc5u0aXlQ0GPALX2Va5fnceyRjxlRToTtnz9JX2k3jW5Qnkl6zJO4BkDZG9YwFzOCaqcfrse-z5djj2URJ8ejDKdSIYjw0Icx8lgxpa1sQlS6B1niKiFxHWfsX1KpA4uigdY0jO-Wf1JO4xvn-1f_1t_9degzdfW5enDku9cNZfr_nmzuRHmfpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام مدودف، نمایندۀ ویژۀ رئیس‌جمهور روسیه، به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/665972" target="_blank">📅 17:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665971">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e498694bbd.mp4?token=N67ZcvLYYeg0gTlXjVjwsAHFIDxMnswks7wur3Bo1fs6K_JfvvvrFRx9egJmG0p0qyR0V6-gAdL7DC6WxIiiJQEvKwi_1WrRRl3N9jdyWZH8QqWBqvHAo91NZJH0OxWjGLfbJbBm_HB8LpuWDPLFSTMTUmObEfJcEgoQ1baHQ_w48TbgeB_bsRu9Eb-tg4DJIXwEc_3GiPp40ImVXe4g_uJfOX8IRRUOfX_ccP-GlT4VZJnKWfJPI390MA45Nl_U7WAM_o157zeF3V--IdW-k4jzJr7vtaBtclqIUBkSJoN42nXFXfHJ1_xa3LNOe4cwjcRazYi1YgXc_UXrXy9t4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e498694bbd.mp4?token=N67ZcvLYYeg0gTlXjVjwsAHFIDxMnswks7wur3Bo1fs6K_JfvvvrFRx9egJmG0p0qyR0V6-gAdL7DC6WxIiiJQEvKwi_1WrRRl3N9jdyWZH8QqWBqvHAo91NZJH0OxWjGLfbJbBm_HB8LpuWDPLFSTMTUmObEfJcEgoQ1baHQ_w48TbgeB_bsRu9Eb-tg4DJIXwEc_3GiPp40ImVXe4g_uJfOX8IRRUOfX_ccP-GlT4VZJnKWfJPI390MA45Nl_U7WAM_o157zeF3V--IdW-k4jzJr7vtaBtclqIUBkSJoN42nXFXfHJ1_xa3LNOe4cwjcRazYi1YgXc_UXrXy9t4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نماینده ویژه صربستان و هیئت همراه به پیکر مطهر قائد شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/665971" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665970">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123fc63366.mp4?token=RgvftEqCT37NSa38jlAFoY8QL14uphudIh5eLLA90Z-VPxSB_JZEiDYh6P--ECzGpU1E4VppiCU7MPYv2n0dwAjPDksGPxhr9UUDcV9CimTO-30yCuBGA8f1zaSuNU-th87Ogxqyr3htfHLiqn1xdE7lGtL-PwN7LYD1F3Dro5v8gAB6Nm1YNuFSt5pK9ABbyiGyo3llIpj1_p-H_6TQTItsVok-wLsWseaXCJtmVNFQMvt7qChpAm-zbnvIzWF1OnjWU1Dy9ts_eEEiFXfuoMexk_dX0PrTDFas-BbI03rvvzlTDtv-hHD8QoIiy4MTeT6Kph9yGYUwZZK3dmDcHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123fc63366.mp4?token=RgvftEqCT37NSa38jlAFoY8QL14uphudIh5eLLA90Z-VPxSB_JZEiDYh6P--ECzGpU1E4VppiCU7MPYv2n0dwAjPDksGPxhr9UUDcV9CimTO-30yCuBGA8f1zaSuNU-th87Ogxqyr3htfHLiqn1xdE7lGtL-PwN7LYD1F3Dro5v8gAB6Nm1YNuFSt5pK9ABbyiGyo3llIpj1_p-H_6TQTItsVok-wLsWseaXCJtmVNFQMvt7qChpAm-zbnvIzWF1OnjWU1Dy9ts_eEEiFXfuoMexk_dX0PrTDFas-BbI03rvvzlTDtv-hHD8QoIiy4MTeT6Kph9yGYUwZZK3dmDcHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نماینده ویژه کوبا و هیئت همراه به پیکر مطهر قائد شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/665970" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c46ddd78f.mp4?token=euxHp_xXxKWhKa0NRGCCZ8201GvoxYwQxHjPwruEj7EUbH4a-VUN0r9UM1uzywMEkliSRvBH_MPnsqaMwW0j2MIFVqFI-2SV4yFpyYI4YSYk6YIYwYXVKMUf31vWaiWlFrNckW-FEMWAoHMQE5XKbTfdZsxohyREJGjETtjne440uywVNcAQSCY6ucKZzMHfOIOpG5DiR6do2ALsQwkWl4jRNmXCbGcOSr5xjtTaNG87bmJkVw6i6toAYrz7y-NJvaJxPHOfKnqFL4gUbKRRZRnEfJMa1BEVQXV2DHVT1FzTfx9dw_CSz92BW5TFbwYLYCIpY1e_y9v-O_hFNbOl3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c46ddd78f.mp4?token=euxHp_xXxKWhKa0NRGCCZ8201GvoxYwQxHjPwruEj7EUbH4a-VUN0r9UM1uzywMEkliSRvBH_MPnsqaMwW0j2MIFVqFI-2SV4yFpyYI4YSYk6YIYwYXVKMUf31vWaiWlFrNckW-FEMWAoHMQE5XKbTfdZsxohyREJGjETtjne440uywVNcAQSCY6ucKZzMHfOIOpG5DiR6do2ALsQwkWl4jRNmXCbGcOSr5xjtTaNG87bmJkVw6i6toAYrz7y-NJvaJxPHOfKnqFL4gUbKRRZRnEfJMa1BEVQXV2DHVT1FzTfx9dw_CSz92BW5TFbwYLYCIpY1e_y9v-O_hFNbOl3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از تفاوت رفتاری یک پسربچه با مامان و باباش در یک روز بیش از ۶ میلیون بازدید داشته
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/665969" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665968">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
آغاز محدودیت‌های ترافیکی مراسم وداع با رهبر شهید در محدوده مصلی تهران
🔹
محدودیت های ترافیکی در محدوده مصلی تهران به دلیل پیش بینی حجم بالای شرکت کنندگان آغاز شده است و ضرورت دارد شهروندان برای شرکت در مراسم حتما از حمل و نقل عمومی استفاده کنند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/665968" target="_blank">📅 17:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665967">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=YQ9kMx-rpPZuHvYeaehb0z9cSi4iG0Vu1EI7yPd2Ml7zCr-Fg4Suwtz3Q2pexxg234CfuGXStkQqGjlxNqf5owkT3Cdzg-Ppoa_POOrBkhmduMumu4pspt96vHrJsvUT3zU2I91B14Y8YiKcozqWmShkDWHWcZtJt9-h2JfFsKnSTW_qhPWU8temtO6JqBnZEmHxhSdJVKT6gVhHoXqfCwRbKPq1TGmPDVDhwvi_lWHXCdscsMLrkloOXhTyNifxgLdkzqoyk-wk3P-n-jLJIP61sJPuSJWt7WnXfJnSZMLkS9qVTC7ybe4v7YruJJRxvOMU4aYsGvZHhcsyoAcapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=YQ9kMx-rpPZuHvYeaehb0z9cSi4iG0Vu1EI7yPd2Ml7zCr-Fg4Suwtz3Q2pexxg234CfuGXStkQqGjlxNqf5owkT3Cdzg-Ppoa_POOrBkhmduMumu4pspt96vHrJsvUT3zU2I91B14Y8YiKcozqWmShkDWHWcZtJt9-h2JfFsKnSTW_qhPWU8temtO6JqBnZEmHxhSdJVKT6gVhHoXqfCwRbKPq1TGmPDVDhwvi_lWHXCdscsMLrkloOXhTyNifxgLdkzqoyk-wk3P-n-jLJIP61sJPuSJWt7WnXfJnSZMLkS9qVTC7ybe4v7YruJJRxvOMU4aYsGvZHhcsyoAcapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام وزیر آموزش عالی گوام به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/665967" target="_blank">📅 17:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665966">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb914d9b40.mp4?token=V1QycuO_5DX5MWZFbhem8VVZqIGTlcOi-qT0y7xVYL7KVGiR61Dp5jzdgc6xZWkjel10q_7TB8ACbHi6iVN6R3glePusCiFIPRM2ZHqAmJOMENyUHqaxVLV2LO3lRWN7jAtPz1JrgJ4cM4U2G4RfUjvTB-by1TIF70klJV8KDB1lS35dynKIvuEJwpkXmKEoGIY__4H7ByDAOSnJc9M43iPHV7QETvJuzkZ5pJqdCpbNFyNszshSkHWkMnRxRLNfvVjuAqYXV8EjZ-lvPc9CK7kwCP3snQLu9dFYPCFK3-ub-I6eznzk79a-EKjQQozUPSJiRvq4B4W3ipjflxy1Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb914d9b40.mp4?token=V1QycuO_5DX5MWZFbhem8VVZqIGTlcOi-qT0y7xVYL7KVGiR61Dp5jzdgc6xZWkjel10q_7TB8ACbHi6iVN6R3glePusCiFIPRM2ZHqAmJOMENyUHqaxVLV2LO3lRWN7jAtPz1JrgJ4cM4U2G4RfUjvTB-by1TIF70klJV8KDB1lS35dynKIvuEJwpkXmKEoGIY__4H7ByDAOSnJc9M43iPHV7QETvJuzkZ5pJqdCpbNFyNszshSkHWkMnRxRLNfvVjuAqYXV8EjZ-lvPc9CK7kwCP3snQLu9dFYPCFK3-ub-I6eznzk79a-EKjQQozUPSJiRvq4B4W3ipjflxy1Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام قائم‌مقام وزارت خارجه عربستان و هیئت همراه به پیکر مطهر قائد شهید امت #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/665966" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665965">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce8a8ec0a.mp4?token=Lo_IwHKA7XryivlDPzEuj4AHq0WXp-RBDrcKMeZazrEBlnBZ_N2jv6wngMBg9S7Zwi6JMr8R6YiOTY3wGWhPr2N61q0JPiEdeo661gkIgS4ZfhV2BmGsB-Y3s4GGHsKSjmQgmJEUW_uNgQTEpWZD464Kwyimev3p4JCoOY6gpAvPDyOtoj2cbDfIqD9ZpmJFoioqH72Bd8EBzpXbHGsacPKa_zn5MJ64ILY1ll6O5CIf_B_IoXAszb7lWNWJWrlbNQXWSNSy8CopSzsFUmaX7B_2KO9QMaH98QPGZv5Z1x9oduQy-Y6s-lpDNlv0u7vLgNQ7AVDyG7q4p9gIw2X95A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce8a8ec0a.mp4?token=Lo_IwHKA7XryivlDPzEuj4AHq0WXp-RBDrcKMeZazrEBlnBZ_N2jv6wngMBg9S7Zwi6JMr8R6YiOTY3wGWhPr2N61q0JPiEdeo661gkIgS4ZfhV2BmGsB-Y3s4GGHsKSjmQgmJEUW_uNgQTEpWZD464Kwyimev3p4JCoOY6gpAvPDyOtoj2cbDfIqD9ZpmJFoioqH72Bd8EBzpXbHGsacPKa_zn5MJ64ILY1ll6O5CIf_B_IoXAszb7lWNWJWrlbNQXWSNSy8CopSzsFUmaX7B_2KO9QMaH98QPGZv5Z1x9oduQy-Y6s-lpDNlv0u7vLgNQ7AVDyG7q4p9gIw2X95A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام رئیس مجلس پاکستان و هیئت همراه به پیکر مطهر قائد شهید امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/665965" target="_blank">📅 17:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665964">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed2e29e6c.mp4?token=IEkOaP2CmJzC7BuTyqZyihKW7yuOi4mT7TdfwzP6QQQxOK67SK1teMXEDUoiRzRjBhMz7LNAl8BXseY7zx_30_JkYarXaaNN5ir6QMm6cD59IYF_R-8VwMDKtyKmDaj5Uu6hiegS6CBqc-kdpkamSkU8g241w5tE7f1AewMpm7P6Nu07Si8Msa9eAa1mtz1Isu4KKS5fkynEagSWnL83DtCIKUkuFid9BgcN7ru5k5uAkUweloAyAG01AK1SW36BxYFPr7ZouD7-MrFbO_VNwIJ0jb2zWsDu1L9vWBZ59cz_qJ1dYbE9bgcWKQQQpyMiqGdU2Z19OYSAE4fdOgsLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed2e29e6c.mp4?token=IEkOaP2CmJzC7BuTyqZyihKW7yuOi4mT7TdfwzP6QQQxOK67SK1teMXEDUoiRzRjBhMz7LNAl8BXseY7zx_30_JkYarXaaNN5ir6QMm6cD59IYF_R-8VwMDKtyKmDaj5Uu6hiegS6CBqc-kdpkamSkU8g241w5tE7f1AewMpm7P6Nu07Si8Msa9eAa1mtz1Isu4KKS5fkynEagSWnL83DtCIKUkuFid9BgcN7ru5k5uAkUweloAyAG01AK1SW36BxYFPr7ZouD7-MrFbO_VNwIJ0jb2zWsDu1L9vWBZ59cz_qJ1dYbE9bgcWKQQQpyMiqGdU2Z19OYSAE4fdOgsLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام وزیر دفاع ملی لبنان و هیئت همراه به پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665964" target="_blank">📅 17:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665963">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سفر احتمالی اردوغان به ایران
جودت ییلماز، معاون رئیس‌جمهور ترکیه:
🔹
رجب طیب اردوغان پس از عادی شدن شرایط، به ایران سفر خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/665963" target="_blank">📅 16:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665962">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135827909c.mp4?token=g-Tc4gdNxlN0Tmzrm83grPF2MolIS2uFSnzaTA46vRleOkG9guHWThz1BaB_8_VT0CPz2oAqd7rkjlBGQvq9s5CuP2j8g-kdfqGmTc6PaUAZhm9qylTD2o5oyWJdc_EberC9Y6Re9JSp6KOMz7mCnn9gwWIEU0RzJHxaycQfACqEO9P10oM5iahP6l1lhfwZSJHzdIOMrqtf0D5zy0bw6LhpYRWDZs7aharJQEJGfhoTxJ37UWv0NwpEG9mMf92qSI0ywTRx_frTInYN1UuxUt9uTkUAoIljf1_AYazJz9ZIa5p9j8TG3FlMlAqA-tLh_mUs9Mqch4Fatt8jbz3P0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135827909c.mp4?token=g-Tc4gdNxlN0Tmzrm83grPF2MolIS2uFSnzaTA46vRleOkG9guHWThz1BaB_8_VT0CPz2oAqd7rkjlBGQvq9s5CuP2j8g-kdfqGmTc6PaUAZhm9qylTD2o5oyWJdc_EberC9Y6Re9JSp6KOMz7mCnn9gwWIEU0RzJHxaycQfACqEO9P10oM5iahP6l1lhfwZSJHzdIOMrqtf0D5zy0bw6LhpYRWDZs7aharJQEJGfhoTxJ37UWv0NwpEG9mMf92qSI0ywTRx_frTInYN1UuxUt9uTkUAoIljf1_AYazJz9ZIa5p9j8TG3FlMlAqA-tLh_mUs9Mqch4Fatt8jbz3P0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام دبیرکل سازمان همکاری‌های شانگهای به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665962" target="_blank">📅 16:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665961">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHP8-hHi0IDex7LzGrYBl0dVYzR3secMKB9gysx1Ec-jS6Gfua8seeGqa2Bcsx6eCFw-SMpfGInbyANOACHsn77L0D98-5hptvyGy9Edv49xeOwMECNd06Cos-L-1l-Vv_UUd6N7xV2YtCqHTXB-2YeRFnEh7Gex0H_3qDlGKGcBktGqtQtlPBAhlfZ1Bwfz6tAGUBscykMJIIjcEdqR8H9uuw2laa5aypIcpZFUEAvNSMywmPyEArO6Fv16bByqj6UrmijSneIOP0jplSkYjxTkYo-EaCnN1jdB4qub9dCm-9CZR-lLI5YGCd-8c7n-U1uuAynTfIlA0lvjaBJNAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
توپ‌های جام‌جهانی ۱۹۸۲ تا ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665961" target="_blank">📅 16:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665960">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0695c6fc2.mp4?token=k1AR6rgKfd4sADMz2ry_AVnzyuB-jF52rkj_mx3U-xhCgEcZUYYawTxrFCLzpY1hZ216d55qzR8fluhZ_0zmS5bpcKHUxbo0E3v3CRNvQyZjQ-EX1B52NAsXK9LP_-l7sUAos5PXaykrUBmnp2T7AUiIyjOPShiD9ZyuTeZGcl40oJ15nHsA_RjtpCAujgIJECDqVSMwzsrUY6alggI_Ckmb48CH6fz3u_-dRmbZuWY9VmaBtBDlyWCgAAfOrY4QrfZyB9Qs6YiwsCoeiVWhwQtRe5DbSmvxI2wQ-MJOKwNr5ijRQBHlPzJezn9saVEKhsf7jel2Fl6GfkNye_KTMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0695c6fc2.mp4?token=k1AR6rgKfd4sADMz2ry_AVnzyuB-jF52rkj_mx3U-xhCgEcZUYYawTxrFCLzpY1hZ216d55qzR8fluhZ_0zmS5bpcKHUxbo0E3v3CRNvQyZjQ-EX1B52NAsXK9LP_-l7sUAos5PXaykrUBmnp2T7AUiIyjOPShiD9ZyuTeZGcl40oJ15nHsA_RjtpCAujgIJECDqVSMwzsrUY6alggI_Ckmb48CH6fz3u_-dRmbZuWY9VmaBtBDlyWCgAAfOrY4QrfZyB9Qs6YiwsCoeiVWhwQtRe5DbSmvxI2wQ-MJOKwNr5ijRQBHlPzJezn9saVEKhsf7jel2Fl6GfkNye_KTMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام وزیر خارجۀ قزاقستان به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/665960" target="_blank">📅 16:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665959">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8daadc4ab5.mp4?token=M2GPXnmk6k-a5IQga_8ABUN-aHGgZhi5lf1LxuMrhD7HiDXSZlQxEqQfaijgQEWY1FZrzLLKuUOlXuJr2Si4N3xClrPhylFjqsZ_fX9RPC3OFEG5l-l3t0s5-kNFB7xWB_p1J59k2WmpUzK429zx4qx6OL3Y23_9Tdf2nBeeapNJJU5XTV0893eW6Ac5nLiDy3PR4qn5ln4VSieOqJxbRaJuJhbZ5FxyKpNM4Z_nsHctlb5sjFnhqwDCmM4gGDf0T5xLjB6eQOGslygVCdo-230qvN9RHQsF-sQQfqLHjhooMBLTipEJLz8AzNKpy8s4Q1AwYohKLgH8vtZ35Gj8sYY0SL10q_o50wCCMviLLW857lcXTTr5KkC4wYkI_TCpNANZlTQh-AtcvMudMubpLV1AaH51eBygz5e6YG9tR-mNr5KWOdvCKNObNkJt4q4l_XO-fUN3iu39hw-SWK31ewk50coe7GWbYhCcxum4ytaiRu9AD7g-XLIQA_yEmG2UupW3rD2QzbVQMNfKd41ziS_FK-emeeFJQmgWbFnIu099XpeOZT4s3xcvYgbTd5o-0uDHiT4bASk2Ps7WSHwENkZkhHRN6incKhlfB7WZTM_G3WmmI2H5L4tw9GW7QWDdFZam5HpAG68ecqi0zBxHF5xLsMc8VzO8cymeRJXvsMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8daadc4ab5.mp4?token=M2GPXnmk6k-a5IQga_8ABUN-aHGgZhi5lf1LxuMrhD7HiDXSZlQxEqQfaijgQEWY1FZrzLLKuUOlXuJr2Si4N3xClrPhylFjqsZ_fX9RPC3OFEG5l-l3t0s5-kNFB7xWB_p1J59k2WmpUzK429zx4qx6OL3Y23_9Tdf2nBeeapNJJU5XTV0893eW6Ac5nLiDy3PR4qn5ln4VSieOqJxbRaJuJhbZ5FxyKpNM4Z_nsHctlb5sjFnhqwDCmM4gGDf0T5xLjB6eQOGslygVCdo-230qvN9RHQsF-sQQfqLHjhooMBLTipEJLz8AzNKpy8s4Q1AwYohKLgH8vtZ35Gj8sYY0SL10q_o50wCCMviLLW857lcXTTr5KkC4wYkI_TCpNANZlTQh-AtcvMudMubpLV1AaH51eBygz5e6YG9tR-mNr5KWOdvCKNObNkJt4q4l_XO-fUN3iu39hw-SWK31ewk50coe7GWbYhCcxum4ytaiRu9AD7g-XLIQA_yEmG2UupW3rD2QzbVQMNfKd41ziS_FK-emeeFJQmgWbFnIu099XpeOZT4s3xcvYgbTd5o-0uDHiT4bASk2Ps7WSHwENkZkhHRN6incKhlfB7WZTM_G3WmmI2H5L4tw9GW7QWDdFZam5HpAG68ecqi0zBxHF5xLsMc8VzO8cymeRJXvsMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلوه کوچکی از خاطره‌های به یاد ماندنی دیدارهای حضرت آیت‌الله خامنه‌ای با مردم شهرهای مختلف و اقشار گوناگون استان خوزستان در جریان سفر استانی رهبر انقلاب در اسفندماه سال ۱۳۷۵
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665959" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665958">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0176f3485e.mp4?token=YhetNGABEROYlN31hOhKMPX13SwaVS0etcTkK7w6Th6wHi-Irmqc1OesYPGWkO8SaL7XQAZkclgDnWQxiwYltItGGao8zYW-D_DNSppWedUKJLcK2nPRSKYXyxDFEbBKmgorLv0TspBzuz9HSYPAJzcJw3jCkqdMRfhc-H4bjqsUpImp0AvZHX6pQaUhVLjBDvlbxaV7-LU8Ck976hGz4tXFHxZ9uhA0cOyjuvSDJgF0h66RC8iks_bOeBSqNIVxQyUkst0M1GgCdyphp4yRmrzmvBSlUTW0CDdMmuNk-s79TgbEwfqCJeXn2D_s3_cepi-cJU2LbohAneJEMTjQ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0176f3485e.mp4?token=YhetNGABEROYlN31hOhKMPX13SwaVS0etcTkK7w6Th6wHi-Irmqc1OesYPGWkO8SaL7XQAZkclgDnWQxiwYltItGGao8zYW-D_DNSppWedUKJLcK2nPRSKYXyxDFEbBKmgorLv0TspBzuz9HSYPAJzcJw3jCkqdMRfhc-H4bjqsUpImp0AvZHX6pQaUhVLjBDvlbxaV7-LU8Ck976hGz4tXFHxZ9uhA0cOyjuvSDJgF0h66RC8iks_bOeBSqNIVxQyUkst0M1GgCdyphp4yRmrzmvBSlUTW0CDdMmuNk-s79TgbEwfqCJeXn2D_s3_cepi-cJU2LbohAneJEMTjQ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام قائم‌مقام وزارت خارجه عربستان و هیئت همراه به پیکر مطهر قائد شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665958" target="_blank">📅 16:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665957">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcd1a9217e.mp4?token=NZ_I_-YJkeFZlv3rQa7C7n5Syaz06G_NvVAyW5Ti3i3co0wD6tHNgXZSlSx8Z8Cr69jENIm9efKCQvbDfy7TYkzMdeDLohC0mEskc37JL9madUBJH7-tEeSD4UFpR8OvCJJeVEjtulSPJMYnvmoQRzYpmY2dS6UnVvSFZRoVE8utBgg3XvgqYQAgmuAJXMD-jNSDn8XNFZiHt9TWzC0pPiazIRE1teoBI8QT7qfjJi7mGrd9FYLYQ40ScOvfyLy_HSkbhWnwNhVP5DwrJU1yCFXqPga7fG9ET4Rcq0365yUQ98KDU23UzL0OKB7JrUJHfgAesi5Ka7LO6m3-IyLGOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcd1a9217e.mp4?token=NZ_I_-YJkeFZlv3rQa7C7n5Syaz06G_NvVAyW5Ti3i3co0wD6tHNgXZSlSx8Z8Cr69jENIm9efKCQvbDfy7TYkzMdeDLohC0mEskc37JL9madUBJH7-tEeSD4UFpR8OvCJJeVEjtulSPJMYnvmoQRzYpmY2dS6UnVvSFZRoVE8utBgg3XvgqYQAgmuAJXMD-jNSDn8XNFZiHt9TWzC0pPiazIRE1teoBI8QT7qfjJi7mGrd9FYLYQ40ScOvfyLy_HSkbhWnwNhVP5DwrJU1yCFXqPga7fG9ET4Rcq0365yUQ98KDU23UzL0OKB7JrUJHfgAesi5Ka7LO6m3-IyLGOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام رئیس مجلس سریلانکا و هیئت همراه به پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665957" target="_blank">📅 16:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665947">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZumiXOII0-FjPfd4ADo4O0NxCot4WWF_qgWQsC-erNXdDRQGTpUPzJ-cCAc_umsdTpSjN1UZft_YVKSrojVhM4Ut4fa94vvtfE2LBd81oylY03VDXRYU1cN2ZSOX074xq4A48fgc8EgL50uiV2V5_OfaiPM1cJPijcvrf96lxVgq3sCtT1i4gXw4VYlEdMK_TIH8FOqefUdOJcp2IzZSYTo8h1kluUtJjXKn30j8ooCTSdjQlbNGUmyd3ZGeo43L-UeJ77PVGcKrR0lHpFWFEbwlPnoN4GvwncyAirxYnL-Z9dU1jZCF_VG5HgDuvWPxO6jfg_Ouo1-e3kw3-9u3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDbJWtLFx5OMOeByy8omlOW8AJd1ri3nx3wsPsvhac11ahRZBQ6AnJZ6YrU9rQdAe3AZudCFwixd_eZne8Qx5jSi-0LzmZiPDX4bJSymYq41ZbGOfY4nzKh3Q3v3RfkEivAHgFCyQnRNvXaY-FGiAVmpHNZR55SoCLxZVthnt29eq2OJWRNZZ24cv6xljRzhwHPmyBN68yxv5My2aZ2qagyiruA-NZay9DXLz4OYX8CKrjC1AocosxZgP8tKLL--woKBRD1wFMeZhfA1iUjRThkIVJisEJOfs6UyLAIK4XoA9o2C40tq_OI1PJIeBDSaAnmvxle-FsIO5wI3tMpPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJmpL1Su0XaywLACSyRKF_m3T1tpTnhwpBWe9DqBcfjTay3PM5DCbhkmDYnYTzhc7nxpPj6ESxEM_j3bReyrSg7bDHTOKjV-PsX_0-D3SCUntu08ro0h5Ec-iKw7nf4OyJHwOuIafyoHKAZq7EOqe6O0z1dHez3EwqXM2YaupWXNv5quOR3zgJ8ktE_ZAcxCMf9hdDAcVwKplH-RliKE8YcRWbdrjOK2y_JYBYbBlx2jMRN70EI34J3upAPhhEcwaj1X6HBpKd-Ua-SEfYu-RwdeI_1Y4Zu36GOUvy8ndL7t_jseKRgsQSfLxySQGR4iwT-LLV9nyv6HdqXBARNOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1NCFinKnO4hCj15fMmT30JbH5tANcgKhDL7GVe8_KsDdbhodZrjjmSVMdzy-sKENrSIvjkHEtbuNyhu6mkCZSPb6R6Rzu0CkDU6h-lRaNujsh4GUGQOEvkclwyWha1K6WfeL4LacW1QJ2EyFl9DG80glYsyl035Ur1XZCRIwGu_XZhsNlUj-aObuLw0MNP19o9lgk0B7svZLZszQgBqbnjFzPLYiCJ6F1JWmlK5KRnZEfd0iVqcakR5_eJf1UsYcif7taoK2G4BzzLiFFpLDWESo6Aoe_RpuNPywiLF-gWoYzgnlFCjsWxW9wnH24wyW9TFU3PJtYbiIlSWoW391A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dleOJFexdtg2kYq9cEh5cttHDZ0YounYe8U2791eayA5fbfdeNcCRf7O0yLB0617Nh301wrtZZeF49Qx8ceKK3-WFkdMdFPbVs-50qgjVQ5Crjltn6jOMM0QlxxsvPZ7jes8mrDSV0Cy2JDsSVgiCsLhMV8kp6CIpj5Z9EnBgLgsJIdbRaXPT-oMxFAI-PQchgW29g4Ao0KtpoLVMeX_Eg1Yv_TFyI0D2M0z37SKy-NeUD8L6DdWgdXAttp-j1Ydkm88a3JXFsy3M0QmrWZRLBvUJkcjUVujUc6iYIhN_C0r2A1WIqpSNXiwqSrKBmi6bZ4zg8qDzQ9Y-C18Y4xRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eb3EOLANeIN-YamorjI3sSC5OwNqPEy351HvGonvdJN24-qVPiBQd4dsP-lp4TmSiynylMOqU_zkkM5IhWBFFwDKwXa8Kzf-RB0PK7fk_jNjCdrG1TuHCFujh_JS0oWu9g0W8VJdSmIckGzYHJ8UZgBE-s27HK0yG62O110bqmj3gNpbj-9nQFpbI9z0ER8CIvFRkua-Az3LO1nlBkv2fNeTUQFDKcVra3FbBbf0qDYhQAEylaDjuiqjbq6hnBHlNgZY-C5y2oSxGenoREgKDGiyn-n37hkECbU90K_-g9mq_EjD0PatfJT5geWhOYIlJDFVLBLiFWzCToOGAtQYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGH6Oyx5eohTi_x_fGIFc4jB-gm0E6dGlQ7abrwYYNEMz0ZkPnVjFJaFdzUjLh457UK8jJjR6dxtCVTeBzO_XOgF6znnKxHxpnc9FLpAEw4rp9X1np9KC4NeBpKlN7KDbTdA5Zni6cS3wfPlgIFiMRjaeiDLHSlsr3sNDyRQYAhfOEAeslhKePeAUOTeYe5nvPC4toaqH2VkE1XRZSt9rg_QpwzYt_Kb-E4-RO46Z32Al1rUMzRhtGGbbm0Tmj1p-AvoFO7QzhcVcrYeaNqtwZCGs7H1zqzqk_ZFaOv1jAv-f1Fa1rrTUhlAfYIqiWIMlU_FFcR436DTmFqjYnPetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qers-kN5UFasEyRWx2i1HSRHdl8FFZKZJr01AvN6cnvm2BKOKzH3X3UrfUFGcsHZeV2aMPDYRz2Y2qy4CZX6RrkP33YDc2qX3IBP15MVZ-cJVC0Mm_64uMPvoGh_-CXJ9fG_uLteevz0IesZGtrUvSsM3pF8zomViBnIfKM34CpunJHkiPVwFl4drrYxCCiIsv4T2TFMvbIOBmEIxPt02Py6zX6FRj8WUsnAH1Abp-3LhAF1feQbUHObQTDHNQGTk-dnktbLbW3-aTdj_mNv2vtWXYstjxZ2Fo1TetPY4POhA4CqC-2h2M2mZxg7Bwi4-jp3PBCbOgUHh5dU5y_01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wi7lbin41vRBEQItoW19bmxw9YJ3CRrjOSzUjkwrhgtxo37zegcI0dZRuBWww_zfE0TM3o0KYbGb7JEMZUNS-UkEOT1Bi0MSDA2qpuV-ONsIJIUdsA45JddKP_SMy6vNOV6o_PLSNuqsc2En2I07IutIdhnqet90RxuJGavrL4rhUXeFEtBzj26uCeQSV87BC1tGLwEbkgsGvfGBBeU1QDXA65i5LYLyAk6_cEW_z4G0X6ByV3hWiso9LpU0cgxqyKnxiya2oIYjuqj-F6u1DPAL9Iq7By3eEsbLH5SL_JWViv9FnPmS1rMfTSeFOACD0897di-AxOtiNGonqwjRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJ1PyGQjhTQSOKkYZHORWUsJgULCNHIGZskMo1u8hhKjhQGh2OGDE-YCM2OIoTA8kbW7NoqrTbMVm4-P4doZYIVEJDuYP3uMyInfAPy0ROELl-A-_Vns1618mqnR1y_Sl8DPFhganc8PvIJ_DvYCMYLO02NkhUKwPFDJ5wlK19Uyj5M0NF_0LjO5a1mjAdeb7Z5eMwwMfRCBhQwK4S7ww7dYD926pB-TpLEijwLUUPFBiThqnjeZ8rskR5m_k39wmuIDiB8Ty8LIc2L70K8JPE36j4SM3V4skylIFrpUc6UlknnfN1-d5b4YV5Rh9CKlJ3EWu_959z30HorMbuNLPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عکس‌های کمتر دیده شده از آقای شهید ایران
🔹
آرشیو ملی ایران در آستانه برگزاری وداع و تشییع رهبر شهید انقلاب، تصاویری از ایشان را منتشر کرد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/665947" target="_blank">📅 16:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665946">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807a058ab8.mp4?token=O6YH1T74CJMnS-czGpkxr41Ft7tj_GdLqPeqZ7W6zYKj1DEGT8lsqsEZvzQ5rZUm70NHMc5kW3u_-u7qHx6ZEM4OumshvcSPXmMxRwesJGTMwbrq97aKWDtlsLD7CsC_ZsUQRkm45_zr5bebUEM21I-a-JFz261S5ZzeVHDprRp8ykHRtuuuNeDF-lheTSuLPaE0XW9T2iVNLusZoI-51pRDsgQBIqzY6pJfyN8KkJOHMgDCatH7a8ZRpyAaO0DNBlT1MF86h32YxnqcSNUWPwL2Q9TavOhYvTNC-NhXIIi-myQhh1oPIcyAM2Or2aN9HRMAAasS7yk5qQtGDuopeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807a058ab8.mp4?token=O6YH1T74CJMnS-czGpkxr41Ft7tj_GdLqPeqZ7W6zYKj1DEGT8lsqsEZvzQ5rZUm70NHMc5kW3u_-u7qHx6ZEM4OumshvcSPXmMxRwesJGTMwbrq97aKWDtlsLD7CsC_ZsUQRkm45_zr5bebUEM21I-a-JFz261S5ZzeVHDprRp8ykHRtuuuNeDF-lheTSuLPaE0XW9T2iVNLusZoI-51pRDsgQBIqzY6pJfyN8KkJOHMgDCatH7a8ZRpyAaO0DNBlT1MF86h32YxnqcSNUWPwL2Q9TavOhYvTNC-NhXIIi-myQhh1oPIcyAM2Or2aN9HRMAAasS7yk5qQtGDuopeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام رئیس مجلس قطر به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665946" target="_blank">📅 16:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665945">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d77fb218.mp4?token=biYWiiymOSAHDpLSRCw3nwURj0DYPXLPX30NZpMWXD-9I5Ld1F8BfNkyuYgonIgZG_AfxNOe_nLwYVfa3wAb8HDY5Nna-u5HGcxMLUuaMwyNYnJzZoxOEkSKrKMoPXWwITtzX7HU_F_lIVpIw4Nl9qsLknD0OftaVL1A1dpojp_bSJ4DNq9bYf30kNPu8K92JepErtWyQ2P253xRxe6AWEGtbhbQdACZ48HsqrFyEbccRJg2E_diHj7qgx8IZszvba449vq59cy25NrW5BPBDikrJ5sm5Sd7CvLYyS3pPCvxN8lFFCS64ng8hBmBDHs_jSJlT5xrIUgqe9qp5EljFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d77fb218.mp4?token=biYWiiymOSAHDpLSRCw3nwURj0DYPXLPX30NZpMWXD-9I5Ld1F8BfNkyuYgonIgZG_AfxNOe_nLwYVfa3wAb8HDY5Nna-u5HGcxMLUuaMwyNYnJzZoxOEkSKrKMoPXWwITtzX7HU_F_lIVpIw4Nl9qsLknD0OftaVL1A1dpojp_bSJ4DNq9bYf30kNPu8K92JepErtWyQ2P253xRxe6AWEGtbhbQdACZ48HsqrFyEbccRJg2E_diHj7qgx8IZszvba449vq59cy25NrW5BPBDikrJ5sm5Sd7CvLYyS3pPCvxN8lFFCS64ng8hBmBDHs_jSJlT5xrIUgqe9qp5EljFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام محمد اسماعیل درویش، رئیس شورای رهبری حماس و هیئت همراه به پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665945" target="_blank">📅 16:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665944">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae22d0a81.mp4?token=Z_ipBEXLMQ7EFJFYjX3MK9hyjvVRxzRD03b_qsHV_W4MtFnZ0DZ7I7uh7TBCIonF2w9FmltXrRKRqge5NY9nX_8-4575epoCLllyq9WYTRuO0FL8Elz8l4-03w0rPPrOV7rleZSS2rnZMT_N93M1AXS3Oe-g0914Mt-GCv5lmkDu7nno7Zrmi8jkqPoVbSIA_UzzICCfy7k7I_obP-QjSN6SXKNmLmCeQ7HK5HZ0YJRfr-1owI0iXdOPZVt88rZfx1OWkbTRRifOUBul9ZGluFcqx-zQSy6Z3v06g7P0xtFlNOEzryRzQeC9lgMlNMDJZq8iM8nsP2QnZn7GHsvY8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae22d0a81.mp4?token=Z_ipBEXLMQ7EFJFYjX3MK9hyjvVRxzRD03b_qsHV_W4MtFnZ0DZ7I7uh7TBCIonF2w9FmltXrRKRqge5NY9nX_8-4575epoCLllyq9WYTRuO0FL8Elz8l4-03w0rPPrOV7rleZSS2rnZMT_N93M1AXS3Oe-g0914Mt-GCv5lmkDu7nno7Zrmi8jkqPoVbSIA_UzzICCfy7k7I_obP-QjSN6SXKNmLmCeQ7HK5HZ0YJRfr-1owI0iXdOPZVt88rZfx1OWkbTRRifOUBul9ZGluFcqx-zQSy6Z3v06g7P0xtFlNOEzryRzQeC9lgMlNMDJZq8iM8nsP2QnZn7GHsvY8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون رئیس‌جمهور ترکیه به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/665944" target="_blank">📅 16:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665943">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9cddcc3e.mp4?token=rUDoGSmuNWdM8XpwjUBrrbmii4r4Pp4PPog-1Ru-TSqP2GuWb4OP7cpB8yjWGUcPS4gLeGs2rgU3xOUgMIBxHMyX1VMANAFzWpP7paayPM9nPp67fNTOuV19BmPct3oqvblkJJtwkzij_2wEFzJnvRgO-Xrg6RhOtXa7Y0A_M1gs5hWNnla4uYzm6G9qDNodjcTd1rag1IxaDtGhUzvYLAncs2Y0c4OkWGwYkIx26wE0hrjVYbN2vhom13JInQNIAtGe_Khh19aimn707y7HoeWB2LBwaPmpQOj1ZRxk9CnppuLT96u_qxQ_BY7hCOOLiL53wAvlayfKX_xnkUO00w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9cddcc3e.mp4?token=rUDoGSmuNWdM8XpwjUBrrbmii4r4Pp4PPog-1Ru-TSqP2GuWb4OP7cpB8yjWGUcPS4gLeGs2rgU3xOUgMIBxHMyX1VMANAFzWpP7paayPM9nPp67fNTOuV19BmPct3oqvblkJJtwkzij_2wEFzJnvRgO-Xrg6RhOtXa7Y0A_M1gs5hWNnla4uYzm6G9qDNodjcTd1rag1IxaDtGhUzvYLAncs2Y0c4OkWGwYkIx26wE0hrjVYbN2vhom13JInQNIAtGe_Khh19aimn707y7HoeWB2LBwaPmpQOj1ZRxk9CnppuLT96u_qxQ_BY7hCOOLiL53wAvlayfKX_xnkUO00w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام وزیر کابینۀ نامبیا به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665943" target="_blank">📅 16:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665942">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a0eebaab3.mp4?token=mRt4sVXbKE-E_wa9qGwpUwip55F3fDiwY7zguJdBsnGFZu80eEL_ZTZ4X2nAilPUWr1IANLMQT9c1z2iJ9DPFAYJvhPNzNkUA1u6OtDmYUUaUcyZurZZly4DRpRSVuiQfdidlFW5C39pAOfj2U27E_rN3SgvJdNINeRUk2fL8SiIpTCjGAeZLe853hBhy412osYVcbv76NZbYRiyKw21EHYg25pl6IaZIVJSc31CfYqYJ-FADgKZd_zQxC8YM6LCOWKc1uR8kKJxhP7XFHNNS57D2XNO3yo6wo1bBLvMJaLLWFUYIYqYcdWdwddO7Y7Diy3VP_Weo6tqbF401ULKsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a0eebaab3.mp4?token=mRt4sVXbKE-E_wa9qGwpUwip55F3fDiwY7zguJdBsnGFZu80eEL_ZTZ4X2nAilPUWr1IANLMQT9c1z2iJ9DPFAYJvhPNzNkUA1u6OtDmYUUaUcyZurZZly4DRpRSVuiQfdidlFW5C39pAOfj2U27E_rN3SgvJdNINeRUk2fL8SiIpTCjGAeZLe853hBhy412osYVcbv76NZbYRiyKw21EHYg25pl6IaZIVJSc31CfYqYJ-FADgKZd_zQxC8YM6LCOWKc1uR8kKJxhP7XFHNNS57D2XNO3yo6wo1bBLvMJaLLWFUYIYqYcdWdwddO7Y7Diy3VP_Weo6tqbF401ULKsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام معاون رئیس شورای سیاسی حزب‌الله لبنان به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/665942" target="_blank">📅 16:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665941">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سید مجید موسوی: سیلی‌های سخت و غیرمنتظره‌ای که دشمن دریافت کرد، پایانی ندارد
فرمانده هوا فضای سپاه:
🔹
اینک که با دلی خون و قلبی محزون، رهبر شهیدمان، آن یگانه دوران را به جایگاه والای ابدی خود بدرقه می‌کنیم، با خدای ایشان عهد میبندیم، تا تحقق اهداف عالیه‌ای که در طول زعامت شریفشان برای جامعه اسلامی ترسیم کردند، لحظه‌ای از پا نخواهیم نشست.
🔹
خط ما همان خواهد بود که رهبر معظم انقلاب حضرت آیت الله سید مجتبی خامنه‌ای اعلام کردند: هر عضوی از ملت که توسط دشمن شهید میشود، خود موضوع مستقلی برای پرونده انتقام است.
🔹
سیلی‌های سخت و غیرمنتظره‌ای که دشمن دریافت کرد، پایانی ندارد، چرا که مسیر مبارزه حق و باطل پایانی نداشته و نخواهد داشت. و به امت شریف ایران اعلام میکنم، جانفدایان شما در نیروی هوافضا به نیابت از شما خوشه‌های خشمتان را بر سر دشمن آوار کرده و خواهند کرد.
سرباز ولایت و جانفدای ملت
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/665941" target="_blank">📅 16:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665940">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeDUZN0T35VwZQJdEXP_S2nQbXQLzwNpN8AMysrpovzddR3EoPFvlB6OrQAvaVK2R2RYTf8vsJ6PUzI_osEH_TvfHH9YGkmLnosMj_Bkm2NG3ToGYnVl3oE94S4GGp4cCnzv5HKrMMLvxj0sDk4r3b4vm2nZKDQ7ET5l19WjWkXhPdPulXdG2mherSAkZklUOpsXiwVCdsciefn-H2sClTNLWbE3eWLrDqnORKjOP_J_0hwDCvsvUEaYHDE8PgWiciaKdlPrKGFdcRdD00rZ3VDEU9NjjZbIiA0yhVxgFOadHv7IJvYPqyPmiQksc61_yCdP-kdQSnG2PlHZr2ZUUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری دیده نشده از اعطای مدال به شهید حاج‌قاسم سلیمانی توسط رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/665940" target="_blank">📅 16:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665939">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1034b5518a.mp4?token=LMSL3otgtmVWUPNR_80FIEd80FwSrSY-b8nhr-rjIF-hQIhnIJcGcU3YFxsiMvoE0l5RvBS9BKJ0RLGdbsYQnJKWXuiF04f2eNfBo364O-mZ8hx0kLHtmhTCXxvBhKlLk1t_1j3CHhXIbzKcgOhdJ1ZXx5fFpF1__ZWiNhwpvV8ZW1ysXAxiD-epbuU_WRpc_jsGXdE_i2d6zpE9lpsRTo7100QJVui2zvHWKU7aLj3k59rUeaa3dzm5r4exLSOMFb-mCHkg_6Fy0GwYAbCoU-qEdjjdKJSm74Gvzz0dfz-svJooTUDY5vgBIO89Ej8YXtvGqVoChcrsy5mSpt97Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1034b5518a.mp4?token=LMSL3otgtmVWUPNR_80FIEd80FwSrSY-b8nhr-rjIF-hQIhnIJcGcU3YFxsiMvoE0l5RvBS9BKJ0RLGdbsYQnJKWXuiF04f2eNfBo364O-mZ8hx0kLHtmhTCXxvBhKlLk1t_1j3CHhXIbzKcgOhdJ1ZXx5fFpF1__ZWiNhwpvV8ZW1ysXAxiD-epbuU_WRpc_jsGXdE_i2d6zpE9lpsRTo7100QJVui2zvHWKU7aLj3k59rUeaa3dzm5r4exLSOMFb-mCHkg_6Fy0GwYAbCoU-qEdjjdKJSm74Gvzz0dfz-svJooTUDY5vgBIO89Ej8YXtvGqVoChcrsy5mSpt97Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام دبیرکل جنبش جهاد اسلامی فلسطین به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/665939" target="_blank">📅 16:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665938">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c47bdcde23.mp4?token=e47mjcZGnIUIpDDU6M4HStc_7djOOENjshpp_lRAiJoYjhqioxLPGfp7YwGd6mv1dVo6CFXBy9MJ1swnd2HxgXJJiNcHid6EGNAgy4me_oOnyigB2jICvXWOi_Akjziz-23t7h8_ANuNX2IbVc5g_0w4mlcuIhfaBZNPRwGTxg0mZGCV_H91HKwwawLMFZUA4p_RRYH-LDaD61KnKIxJCJpMCyRWkNXS-tni6nxY9_JmV6VpkwSoG4aKNbtCJ85M5rt7sKk-Jwbs9OxbuzRXqNV6MSH5ZWlV-XNV58EiGI-USK9FCt9eHLvPJZkPDOp2-RXktrELLzPdsYWMnfnyMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c47bdcde23.mp4?token=e47mjcZGnIUIpDDU6M4HStc_7djOOENjshpp_lRAiJoYjhqioxLPGfp7YwGd6mv1dVo6CFXBy9MJ1swnd2HxgXJJiNcHid6EGNAgy4me_oOnyigB2jICvXWOi_Akjziz-23t7h8_ANuNX2IbVc5g_0w4mlcuIhfaBZNPRwGTxg0mZGCV_H91HKwwawLMFZUA4p_RRYH-LDaD61KnKIxJCJpMCyRWkNXS-tni6nxY9_JmV6VpkwSoG4aKNbtCJ85M5rt7sKk-Jwbs9OxbuzRXqNV6MSH5ZWlV-XNV58EiGI-USK9FCt9eHLvPJZkPDOp2-RXktrELLzPdsYWMnfnyMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئت عمانی به پیکر مطهر امام
شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665938" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665937">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1575f179.mp4?token=AnQ-OYEfi4guuO92jQsMn8a3bC5-eLNQ9sYMl6jVYRctu2Vak5KAczcuazd7UT323-QLy7gYsoHXov2ax45vVAeihwg75oxUc5oDugZM05JnszCY05-F4woLKMw90XeYLsZwewZSb9laVldFHz7Df4kNOCF_bV5BmRdNYnPlFvbeLWeOZtn_m0s506WjBhfKakYjquVlQrR2J6l_E6G3i3DVN7mJwUvG-WMa0LQ57G2G3woTzTdUtYUW8AQFuRlsjqf3kfC_aBa523Whyn2CpKk90KBXt0uVAIYlOiOXa5i_8EferbhfOpgcHNdt5LiCjPVyVL_2sL2tRi9qv2QQkoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1575f179.mp4?token=AnQ-OYEfi4guuO92jQsMn8a3bC5-eLNQ9sYMl6jVYRctu2Vak5KAczcuazd7UT323-QLy7gYsoHXov2ax45vVAeihwg75oxUc5oDugZM05JnszCY05-F4woLKMw90XeYLsZwewZSb9laVldFHz7Df4kNOCF_bV5BmRdNYnPlFvbeLWeOZtn_m0s506WjBhfKakYjquVlQrR2J6l_E6G3i3DVN7mJwUvG-WMa0LQ57G2G3woTzTdUtYUW8AQFuRlsjqf3kfC_aBa523Whyn2CpKk90KBXt0uVAIYlOiOXa5i_8EferbhfOpgcHNdt5LiCjPVyVL_2sL2tRi9qv2QQkoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی تلخ از خرید اشتراکی موتورسیکلت توسط ۸ جوان؛ آن‌ها هزینه یک دستگاه را تقسیم کرده و به نوبت از آن استفاده می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/665937" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665936">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815cbe27e9.mp4?token=RqJchpTvue5n1NChUb8eRsDaPuPa1vpekBv8Kc8ifSoUybmTzPoT1ICNbgpmLYACbvMW9s_ABCf78TEaKJ3bFkijqeGBh5p3n8u4Moa15QaR9ElInnZnEdtpc8S-27u9YKNnjCyw8E8ubqdHBzFC-JDnjmww-MKG6M-i4iOKBPljbBmkj36zSYWgNmWZ4NgxfX7uUidyCZzzlr9l-gRrjzXROgksxx31D534jtf2_9FaYyBqODYaQTGQptxn6I7JgVNhbtqKLGW2Pbw46s5Wnbz-42lVPNjbaCdFQou2st-KQSOr9y4QJb1rFZ_rdrH5xFsB3PMVDckyciv4nO1x1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815cbe27e9.mp4?token=RqJchpTvue5n1NChUb8eRsDaPuPa1vpekBv8Kc8ifSoUybmTzPoT1ICNbgpmLYACbvMW9s_ABCf78TEaKJ3bFkijqeGBh5p3n8u4Moa15QaR9ElInnZnEdtpc8S-27u9YKNnjCyw8E8ubqdHBzFC-JDnjmww-MKG6M-i4iOKBPljbBmkj36zSYWgNmWZ4NgxfX7uUidyCZzzlr9l-gRrjzXROgksxx31D534jtf2_9FaYyBqODYaQTGQptxn6I7JgVNhbtqKLGW2Pbw46s5Wnbz-42lVPNjbaCdFQou2st-KQSOr9y4QJb1rFZ_rdrH5xFsB3PMVDckyciv4nO1x1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام وزیر امور خارجه کنگو و هیئت همراه به پیکر مطهر امام
شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665936" target="_blank">📅 16:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665935">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9WuLTcSg99P3dxBf_QSayP-M6Q4VqrenZXV4BS5xkkdEHoHFFlOcIX-dcRDFbfrOqNY4kHsfZD__d4HxmdmgRvkKfxBMIdbplBd9Npjwn7f3Ooz98GzlyTnqvDH1sUu0Og_Um6Hl9eQAsFKHi5X94gqdiCfmJ2cMeXVBwESTMEl_sd8bDNDf6LGDEGgzzZOm9hEO_g9LMJd4quoL3tXIjzeNT2wavlc4lXNxZolSkwo0mACddN3ewef_wGMPJ4rwvzCaHRKI0VBhbMrrJGwdr6L0rEcVlsyNj0s55Z68CDJdGJmGj1hunWCwgxfDkeTzylae7vZ8fGVYj_bX-OkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیه‌ای که در جایگاه پیکر رهبر شهید انقلاب نصب شده است
🔹
«قُلْ إِنَّمَا أَعِظُكُمْ بِوَاحِدَةٍ  أَنْ تَقُومُوا لِلَّهِ مَثْنَىٰ وَفُرَادَىٰ: (بگو: من شما را فقط به یک حقیقت اندرز می دهم [و آن] اینکه دو دو و یک یک برای خدا قیام کنید) سباء ۴۶
🔹
امام خمینی این آیه شریفه را در ابتدای نخستین منشور سیاسی  خود در تاریخ پانزدهم اردیبهشت ماه ۱۳۲۳ شمسی (۱۱ جمادی ‏الاول ۱۳۶۳ قمری) نوشتند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665935" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665934">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789df29f8c.mp4?token=cOYkDqtLOfzj7agkqa5yMWAZlObjR-x9n8PJ32_lw0mKQ3Gc9deIdWYsSA4ZGDVchONvfz0UEIhhwByMOFL9tu5uRipoF4YQz2rP-HEjClHaxTtzL4Z5N9Iua38szwN-9DtVWyVFKcF3JoDbdvDR5DUVkM-laHqTWUuDDJNCDDRwN-ZJm-GcPXay6LijJJegvPpH5qX6lc4SvFHLMMCmiS97KzwZuhJVqmzqZcbCwxoHaiczBr7-D-GRDC2xCkx7PVDpJ5Xe9Tnh8K1zF27BgBHn5qp3m0923k9XkUfiVqrJ-lDvtu2PJEeK5tFLzy4pyS6ERjEHGIRX7aR-fn7RNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789df29f8c.mp4?token=cOYkDqtLOfzj7agkqa5yMWAZlObjR-x9n8PJ32_lw0mKQ3Gc9deIdWYsSA4ZGDVchONvfz0UEIhhwByMOFL9tu5uRipoF4YQz2rP-HEjClHaxTtzL4Z5N9Iua38szwN-9DtVWyVFKcF3JoDbdvDR5DUVkM-laHqTWUuDDJNCDDRwN-ZJm-GcPXay6LijJJegvPpH5qX6lc4SvFHLMMCmiS97KzwZuhJVqmzqZcbCwxoHaiczBr7-D-GRDC2xCkx7PVDpJ5Xe9Tnh8K1zF27BgBHn5qp3m0923k9XkUfiVqrJ-lDvtu2PJEeK5tFLzy4pyS6ERjEHGIRX7aR-fn7RNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود مدودف به ایران برای شرکت در مراسم تشییع رهبر شهید انقلاب
🔹
سرگئی مدودف، فرستاده ویژه ولادیمیر پوتین، جهت شرکت در مراسم وداع و تشییع رهبر شهید انقلاب اسلامی وارد ایران شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/665934" target="_blank">📅 16:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665933">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opPd9kiMNa6F-o7qzNPz1e9QszlcGnloZgAwblhZzdsGKx6-QLm4fw4egdLUXq1di4zudcmJKkJgIuI6OGUFBDQpEquwtCbTqJmukz60w312dQsmJ7-aF4AoRy7fIzD78wDC-Q4fxK5tpHJpXu6RPDVYeax-AWkRAuZMew5WBtdzTu0687INncFzY5OtyH7ucEuqxCLadchEd-MShwJE45RRk6Fj0RtkNsUllEyscBka0jVirPkP6bkCubFYlN7n5CMb7bF9ZZDILEruWf7Rb_JrovFtMQ-LU5sUq8WKT1QTfPr77F5xZfQ2psfVqX0JLrhh4nOXoxdpC_BkQq-zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک بازیگر به عضویت مجلس انتقالی سوریه درآمد!
🔹
«رزینا لازکانی»، ستاره ۳۶ ساله سریال «الهیبة»، از سوی ابومحمد الجولانی به عنوان یکی از اعضای منصوب در مجلس انتقالی سوریه انتخاب شد.
🔹
لازکانی ضمن ابراز سپاس از این اعتماد، متعهد شد با جدیت برای ساخت سوریه‌ای نو تلاش کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665933" target="_blank">📅 16:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665932">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4429ac1471.mp4?token=CClMk3NaByPF2Tr9KaJiFPPTPC-b4g-VJJ67W_AplIaOgf5ivws9Zw27S0uOOMv3h7jTTettMufa1la4zhLuFisSasCv0cJhzWVpsGqqmJev5_pXVwf9f4qeXxF0PDNUmOkpPnfpdpf3d8-vp0qSKzLJS-fkoWNpviplyk1CFZ_qbwG9wCXZvHa8eItbPsiTUFcQkDbIYdxWZy0Q9cU7tEVeFnCpz2QhqSqvGCkcs4oz2Gfz5BXHw68DkotF-jfnFTAQt9L1cWakoLp3OATPpBI_c2-fXnZL5TR8bpyXhVb8Yi-3EYhaWgXKlQ8CPNL4SiO40PtWbl1TQVfzC3F6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4429ac1471.mp4?token=CClMk3NaByPF2Tr9KaJiFPPTPC-b4g-VJJ67W_AplIaOgf5ivws9Zw27S0uOOMv3h7jTTettMufa1la4zhLuFisSasCv0cJhzWVpsGqqmJev5_pXVwf9f4qeXxF0PDNUmOkpPnfpdpf3d8-vp0qSKzLJS-fkoWNpviplyk1CFZ_qbwG9wCXZvHa8eItbPsiTUFcQkDbIYdxWZy0Q9cU7tEVeFnCpz2QhqSqvGCkcs4oz2Gfz5BXHw68DkotF-jfnFTAQt9L1cWakoLp3OATPpBI_c2-fXnZL5TR8bpyXhVb8Yi-3EYhaWgXKlQ8CPNL4SiO40PtWbl1TQVfzC3F6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام رئیس‌جمهور گرجستان به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665932" target="_blank">📅 16:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665931">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a56aefedd.mp4?token=PAXthl47IWx3GDyZJuXqqY83OGq62K5MkPEtrEVL4-W0kUtCYq2DpW0Stc2vkPfQyOyZ9OQLye-GtmwXp6WMoLqWhvurJ-pIKT7GXQ3YpbZPf9SsSmyzzDTxAHKiwcuWTc2BHIYMeRjL4GKpET9Z6jLbCy995Fksxo9zLhXD9xiyXIdvCNgZl71kxVIONOmKKtrLTjeWfUQLsJMgSred8A4zCTuBPACtjeaQLwjTJLKGfTHbKcogD1gWWhxoW9DvLXlQXx0XMBvuEIBFhsh_wqyr-YnRRSPtQ2B8GRCiU6HFF9wgN-dORfR2iRj309nKLds2rs9GWFHkcbmVPfHxgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a56aefedd.mp4?token=PAXthl47IWx3GDyZJuXqqY83OGq62K5MkPEtrEVL4-W0kUtCYq2DpW0Stc2vkPfQyOyZ9OQLye-GtmwXp6WMoLqWhvurJ-pIKT7GXQ3YpbZPf9SsSmyzzDTxAHKiwcuWTc2BHIYMeRjL4GKpET9Z6jLbCy995Fksxo9zLhXD9xiyXIdvCNgZl71kxVIONOmKKtrLTjeWfUQLsJMgSred8A4zCTuBPACtjeaQLwjTJLKGfTHbKcogD1gWWhxoW9DvLXlQXx0XMBvuEIBFhsh_wqyr-YnRRSPtQ2B8GRCiU6HFF9wgN-dORfR2iRj309nKLds2rs9GWFHkcbmVPfHxgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام وزیر خارجۀ بورکینافاسو به رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665931" target="_blank">📅 15:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665930">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
خطیب جمعه تهران: خونخواهی رهبر شهید، خواست همگان است
🔹
آیت‌الله خاتمی، خطیب جمعه تهران، در سخنانی با اشاره به شهادت رهبر انقلاب، تأکید کرد که جهان اسلام بزرگ خود را از دست داده و این فقدانی عظیم است؛ وی ضمن اشاره به اقدامات ظالمانه علیه رهبر و خانواده ایشان، گفت: «خونخواهی مقام معظم رهبری، خواست همگان است.»
🔹
وی همچنین با اشاره به حضور گسترده مردم در آیین بدرقه، این اقدام را پیام مقاومت و استقامت دانست و افزود که حضور ملت در این مراسم، نشانه‌ای از ایستادگی است که در نهایت منجر به شکست آمریکا و اسرائیل خواهد شد.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/665930" target="_blank">📅 15:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665929">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1867a167c7.mp4?token=ES7ywz8Ub55tKSqLLozFU-QyqbHKzWj_wPvqUmRQ-0s3NC177jm95M1ENq6wHcEdb9lQIOpjnkNlTmox0XBkz1qwTJDaPzbeaOCn2GA3IqVtaADYltF-W66BRo4LpyR0Cm9n6VT97AyOkPvdF8vksGurQYdYAmvurbmhK-MHAFTSJGKDv93TN9PFIef3kAYXRkroNKeMZgNHCuuqROEJ2RlELiJLVuDkL32W2KF-Fok50sH9fZaGlaBJazNmYc_gaFut8wI-r_hwggYTloWIyudBsi4LOD02riuY7Z390tlZ_VF_OtNDYfYvU4akoSKCTNaAqrXLDO0SNjDfVQjeYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1867a167c7.mp4?token=ES7ywz8Ub55tKSqLLozFU-QyqbHKzWj_wPvqUmRQ-0s3NC177jm95M1ENq6wHcEdb9lQIOpjnkNlTmox0XBkz1qwTJDaPzbeaOCn2GA3IqVtaADYltF-W66BRo4LpyR0Cm9n6VT97AyOkPvdF8vksGurQYdYAmvurbmhK-MHAFTSJGKDv93TN9PFIef3kAYXRkroNKeMZgNHCuuqROEJ2RlELiJLVuDkL32W2KF-Fok50sH9fZaGlaBJazNmYc_gaFut8wI-r_hwggYTloWIyudBsi4LOD02riuY7Z390tlZ_VF_OtNDYfYvU4akoSKCTNaAqrXLDO0SNjDfVQjeYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور بافل طالبانی، رئیس اتحادیه میهنی کردستان عراق در مصلای تهران برای شرکت در مراسم ادای احترام به پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665929" target="_blank">📅 15:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665928">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257aca00ba.mp4?token=DUYhzCli1I8uzF04rT-G3QoIZLmyRElot5zyO8b5rf3lMOaFwGqwEq3tHMfPz-Tf5ax2_Cdu1BBznEYrQlUw77t4ErjCpNvdFfVcPhzPVfy4_Age062T14djWw2sGpVxCcyR9rEKpuucS7oHm46os6KqqxB_j1RG8VJwUgs0mGqy3ilRg2EcFvsa6qG6nvJ0CkWaLPvJwYcp9kYsKGptpH8vb0UvYEx__46ZKljkAmEcGsp-ah_oeyVtnR-ejF7UF0aqrOyGRQp7jRQVjIX8AyZnODWX-grJXFIOZ_Qo9FJB9xg0lsxrUpXCvYa3Wr1TJp-teLvNuCPOfnRh0SgtTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257aca00ba.mp4?token=DUYhzCli1I8uzF04rT-G3QoIZLmyRElot5zyO8b5rf3lMOaFwGqwEq3tHMfPz-Tf5ax2_Cdu1BBznEYrQlUw77t4ErjCpNvdFfVcPhzPVfy4_Age062T14djWw2sGpVxCcyR9rEKpuucS7oHm46os6KqqxB_j1RG8VJwUgs0mGqy3ilRg2EcFvsa6qG6nvJ0CkWaLPvJwYcp9kYsKGptpH8vb0UvYEx__46ZKljkAmEcGsp-ah_oeyVtnR-ejF7UF0aqrOyGRQp7jRQVjIX8AyZnODWX-grJXFIOZ_Qo9FJB9xg0lsxrUpXCvYa3Wr1TJp-teLvNuCPOfnRh0SgtTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام رئیس مجلس سنای مصر و هیئت همراه به پیکر مطهر قائد شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665928" target="_blank">📅 15:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665927">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9717183431.mp4?token=bVQY462wOvijQknJmIOjRie2L1RFuOjlUnJ7vqHbM3yPdo-bDIJW2TJqQGmjUlOntZ6CrHZxCiPGtUatLKWSFMcvtwKrkz0FFk26bM4NOJx5NPbi6E7IoMU4AZmJmJqdJeSchTyTvdGKcDNBWdKVeI0GrkL92oB0SnHVgZkkzok3VWwr2iC7Xo0nugkaxEcm8vXpf4azPGmqVRrtOIq94EA-FG2GTXR9cs6YVzabLWy5w3Z5ApqVheIcjI8FlKedW69U22VC_prBnWVSPczneKT1mB1aZaaLJqUJiSXyyxVO5cY30xjclwotBfJWR8dkfYCP3WwU2zH278TflZNdPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9717183431.mp4?token=bVQY462wOvijQknJmIOjRie2L1RFuOjlUnJ7vqHbM3yPdo-bDIJW2TJqQGmjUlOntZ6CrHZxCiPGtUatLKWSFMcvtwKrkz0FFk26bM4NOJx5NPbi6E7IoMU4AZmJmJqdJeSchTyTvdGKcDNBWdKVeI0GrkL92oB0SnHVgZkkzok3VWwr2iC7Xo0nugkaxEcm8vXpf4azPGmqVRrtOIq94EA-FG2GTXR9cs6YVzabLWy5w3Z5ApqVheIcjI8FlKedW69U22VC_prBnWVSPczneKT1mB1aZaaLJqUJiSXyyxVO5cY30xjclwotBfJWR8dkfYCP3WwU2zH278TflZNdPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام مارلن مامتعلیف، رئیس مجلس قرقیزستان و هیئت همراه بر پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665927" target="_blank">📅 15:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665926">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53048897d6.mp4?token=Phu0A-ZvMfI2leOWDFC0ec58_odEcodzVIafOOvTxcwFHYGZGE-zen042UwA34z9pF0gwHLO9VyjINj3Lp5VGNwPb0F8xe_32z7IyhvYpEC7IyYq1BW3Wtzx_9MICJZw9aCCQ_9m8mt0uKCXYL4nNDOAMpFgPx0Whuxr6X2H7LBHQ5nJWZNGSam3LlKvEKMFGrATgPSBjNNJixcXiSyoTQ66ys0qw0OiJ02RQp9xbeDnh06-I8hUUdP0UYJbqdKWYKFbaybGTH_P4skOIgw2jagkYmhBE0JeqrrVjb802gmuma045s7oTU1U8BqSLOUFD9P90WP6CG-ul-mgBOFByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53048897d6.mp4?token=Phu0A-ZvMfI2leOWDFC0ec58_odEcodzVIafOOvTxcwFHYGZGE-zen042UwA34z9pF0gwHLO9VyjINj3Lp5VGNwPb0F8xe_32z7IyhvYpEC7IyYq1BW3Wtzx_9MICJZw9aCCQ_9m8mt0uKCXYL4nNDOAMpFgPx0Whuxr6X2H7LBHQ5nJWZNGSam3LlKvEKMFGrATgPSBjNNJixcXiSyoTQ66ys0qw0OiJ02RQp9xbeDnh06-I8hUUdP0UYJbqdKWYKFbaybGTH_P4skOIgw2jagkYmhBE0JeqrrVjb802gmuma045s7oTU1U8BqSLOUFD9P90WP6CG-ul-mgBOFByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام رئیس‌جمهور عراق به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665926" target="_blank">📅 15:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665925">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61bc4c44c9.mp4?token=QvzjBsOg9U2xEvTd3KuB2bF9TjXpRfWX6lJYzdQ-EEWAzrMSOQlZJ0RMPB-Rn7Djg0JdhQAVcgE7Gw2ImsJnHe1Q7p2k7jgWgWtGT4mOcgqWVUJhmtE2b8-I3jLqK2cZsH60MRDTeeZDOXDhPpWPDrmAEUFdhcWko3HjVqO-HG7Go48OLjdi58C-4kzfmHICmWR_Uq3VcyHnPYNDjfGw56QAX_bpxw7LJWXEaDsNbFYkfVBgRadJkrfeBhyP-sg2O57OFR0OAk4ytlEfCOvEtCFlDq-XsjNu_iacvSqd4QeTTg5qLj4CPaMY5FQriEj1CBjIX1Jb6Gw6B33c7VSAlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61bc4c44c9.mp4?token=QvzjBsOg9U2xEvTd3KuB2bF9TjXpRfWX6lJYzdQ-EEWAzrMSOQlZJ0RMPB-Rn7Djg0JdhQAVcgE7Gw2ImsJnHe1Q7p2k7jgWgWtGT4mOcgqWVUJhmtE2b8-I3jLqK2cZsH60MRDTeeZDOXDhPpWPDrmAEUFdhcWko3HjVqO-HG7Go48OLjdi58C-4kzfmHICmWR_Uq3VcyHnPYNDjfGw56QAX_bpxw7LJWXEaDsNbFYkfVBgRadJkrfeBhyP-sg2O57OFR0OAk4ytlEfCOvEtCFlDq-XsjNu_iacvSqd4QeTTg5qLj4CPaMY5FQriEj1CBjIX1Jb6Gw6B33c7VSAlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام رئیس مجلس بنگلادش و هیئت همراه به پیکر مطهر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665925" target="_blank">📅 15:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665924">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a33955f8.mp4?token=rd50BCJt8R_wPxXtdNEMd1WYYFj5buJLInors6W3PtaO_2UobXkH7n3Wpc2SNe_A8Wm4WgF9VUo_fEg-n-K2-a3xvFtiprdAmu5dELHhOHYlay29e9eV1gHec-VMxZyEaiQTZknpm1lZpoYrXcgxb8_HcFlB9au8ab79WnIIOJbKLKME0Rc3Q7DNlL16v7F8CbbqxifixKztMElnlk5xfAwggh1tPRLPyL1T1bnT15LR5QSTysKHI1ECUmhlTpEnK1jWPnDnlGBo1Gu-htyuJo1h5fk8QNEbR2lcXeagsOPXpoxjOurl2X96LumvjVoqpqxo5Zp2c66iJaRSOQDmsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a33955f8.mp4?token=rd50BCJt8R_wPxXtdNEMd1WYYFj5buJLInors6W3PtaO_2UobXkH7n3Wpc2SNe_A8Wm4WgF9VUo_fEg-n-K2-a3xvFtiprdAmu5dELHhOHYlay29e9eV1gHec-VMxZyEaiQTZknpm1lZpoYrXcgxb8_HcFlB9au8ab79WnIIOJbKLKME0Rc3Q7DNlL16v7F8CbbqxifixKztMElnlk5xfAwggh1tPRLPyL1T1bnT15LR5QSTysKHI1ECUmhlTpEnK1jWPnDnlGBo1Gu-htyuJo1h5fk8QNEbR2lcXeagsOPXpoxjOurl2X96LumvjVoqpqxo5Zp2c66iJaRSOQDmsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئت طالبان به پیکر مطهر قائد
شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/665924" target="_blank">📅 15:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665923">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBruQ2CeXkTJQI8h261MdhN9JjhDadWT1SE3JBFGn5OATQKd1YnnCmS6tvLGGfYsS0qSjdsrG52rlEcIThMILoVHBciJDV_MV_pBeQV3S4XQVfsU0amncuMU7eFMSJ82SX45ujELCVg2IW-qGBS3MNqnnEa7Rppr3vWEpMJFB2q9HLhK7h6LJ3kNRWaGK8lA7G_NSusKOerrxHTj3zHJKcLt1dxLKJNrmTtoZ1D7UjtOO5mCRunUcsawL4SwIZqIglK7Zk_w2VJSZFui0gaGVN1KbyOu0I-2dM22MGvnnVj7QTbk8CaDkAApdeUa9dD_ya1pI_cLtbJt4YjvxVCGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف ۱۶ کودک در شرایط غیرانسانی در آمریکا
🔹
مقام‌های ایالت اوهایو، والدین و پدربزرگ و مادربزرگ ۱۶ کودک را به دلیل نگهداری آن‌ها در شرایط فاجعه‌بار بازداشت کردند.
🔹
طبق گزارش پلیس، این کودکان احتمالاً چهار سال در اتاقی ۱۳ متری و مملو از فضولات انسانی زندگی می‌کردند؛ شرایطی که کلانتر منطقه آن را «بدتر از جایگاه احشام» توصیف کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/665923" target="_blank">📅 15:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665922">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af14934df.mp4?token=nDUNRzsTGDjpo7xomoYqle8ec5czvJCYRMF-bmwyI-7xCkJyZ7IK24_YlCczk7bIhfyb7rUVfyPnghr7zIJb2zSZ6Y48wV1EIxrwl9-u62N4no2_PHinSBZyOeXN46sF9erigStPhQ99TicP2f9ioZx_DsmokdIUL2zfoNus-zD5rt6QGQkLL6bLkB08vfQMRGLiHLVrdIuVk9T96kqv0Ic9N6F11tdCtXLQaPB4Ty35mWJVWKDktqtqqfYVpqe4OLHxFLk33E4OdhV6Zdyt6EMZBZnwcRww7cSKv6RMv8HiNTX3yuPjStTiXjRG8_DEy_wkJhAxg3EpFmMW2ui6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af14934df.mp4?token=nDUNRzsTGDjpo7xomoYqle8ec5czvJCYRMF-bmwyI-7xCkJyZ7IK24_YlCczk7bIhfyb7rUVfyPnghr7zIJb2zSZ6Y48wV1EIxrwl9-u62N4no2_PHinSBZyOeXN46sF9erigStPhQ99TicP2f9ioZx_DsmokdIUL2zfoNus-zD5rt6QGQkLL6bLkB08vfQMRGLiHLVrdIuVk9T96kqv0Ic9N6F11tdCtXLQaPB4Ty35mWJVWKDktqtqqfYVpqe4OLHxFLk33E4OdhV6Zdyt6EMZBZnwcRww7cSKv6RMv8HiNTX3yuPjStTiXjRG8_DEy_wkJhAxg3EpFmMW2ui6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی که اشک فیلم‌بردار حسینیهٔ امام خمینی(ره) را درآورد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/665922" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mli5Gju2-AOHk1ySE6yrIdLu-mgNoZZgL_arLsjJT0wN2obdMQ_RHxk8Dhh3cGffv9dNjWJtv1XD8bS9fOAFhuvjBGcatc0Vtowhaaq4cZV7lVauSxDKEGdE9UWC1SK9qcz-k-L7I1093Lfif8ybUYGiMFX7cCI-ds2vqqvtXEFNmapOicWEpjh2KnrKTeb1uLUbRIsz_FsjwwyePR476Qb2FapDJa_yTjI9d7bmtIJDKB4piAUMQWBPLluCoF60lwTwiWrnHNLKQdWjA2BsxfXmYGIR4ezSTNIxINrMgLKcip345etEgWOnSFlrJFxOnDw3LGsquvhNI-TqEDDcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTMKsccbH55Jcdcpftv3DRk76uPBfR1kHohCOW12uVg7KSbNZKthUM6FzW1ckxcN4M8AjAKOxu117HgL5NLES_EswrtKJZRyCvs2CzVXbTs5m5CZvFzW1NG1POCKQynI2Mbo03sqBZ4e8kipDwSOVA8A1E4NSOg67nho9vUZWEHz1LqzbqVGZE2KHkLdDswTZ1_h45IzJr8vAleHXhxCA_Fgc97pbqySqUOR0K0pz0OxfwpyVJPsF3rBoZVKBUJENiiBdafGX2WaWQMj5DA7F2Rh4NkHXSFOQLWW-XxRkl5WfNiHmtbKECaPPEJJwl1SVTKgCyYyF6kJgriG-Thblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzNIpR6pwSTbhBCQtr7YQYvO9zYyWMTG0g-RjJ9QErALeuvB-1EmZxIU1sSnoJQuktyReB0w_Wm-kDRg9tP13p9TV99wqoLnXVYD2CfXoFVSuLRLfQISuCTDidKojH0yOgNj9JSjSnBvYA06IHDmaoMbHUVa-2sbhVWuWXMGkxkHFnQL_u2RZyuJh1GRXzv_gX8I5IFw987GMe7wmJ-iXfgx36Qtj64U_vaswDTEYCz7UcrJhNP4k4Qv-DlalZPPt0Y9y5fbju6B2rouqbu6IC6iEzm0V96uGSkrrWd-za0DD3JtdKX9SF1c91ghWtxOb2wD3M2PdkBOkr_41uhQSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دست نوشته قالیباف برای شهید طهرانی‌مقدم
🔹
برای تحقق شعار سنگ مزارت از پای نخواهم نشست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665919" target="_blank">📅 15:37 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
