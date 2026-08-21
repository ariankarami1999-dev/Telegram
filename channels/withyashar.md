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
<img src="https://cdn4.telesco.pe/file/grMJnQw4P_RGPE-oMfTsOYWoKrmgZ9nDwDdOtfeNbVax25aYzla3I3F0hRBQCsE_EVFZIbFV7MwlO-vrIONZquOfC9RcTPkagzWwojdaChKvUSQck9lZTPOUFqInXJfwwiLvErXcV7xot1F-HIvE1RsW1Jh5jGlkcznh6M_saGzmoPxFFof2lyOxshB1G5kdx08LagEcFnegaLFsEriBJDRxJqX1EE2DZCx_UsMQYA1yAsdYsOVxvcgCVdvKwUnP25YUs6wFIaaPYUQtnL4fVQwMIxf-5-HhGw9do3WYd72vbFHJkUSgn1a9ZUuJ1a68L4rEJrNj-yrrHdVAik3RYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 16:55:57</div>
<hr>

<div class="tg-post" id="msg-21286">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7e5ce77a.mp4?token=laY5b_ehKAg0qBRq1CI_ZUSkPXFpKE64DArJwgYXVOK6XvaDbXNqggxpt2zzF0_Aew7XgnINq5PlX_ON1xkTloeLDHWD7NWgxcjsOFPx_M0LrH9b3ezYR2YOSspYIc-xVQtnmr5d-MLRZgXHTVH9vwMt3yGsY3W0TfWETmiCCq0k--YKRyaVXb2Y_06jU_I-oPS2-GnyUBu5DacG5a72JowCwU1mc-0XHu0eSsTVftttlB2aCtCQTJs4zZf1fJzDbJUkiEW01o7_g5mspCVfbNFpkQfOMw9btcQ1N76zZD4BMxv40YL2Lt3YexPrAFAi47SB9NwpQbkD7Z0111IklEr31g43kgBV6nmjiadbeEIKNUfWVbwPsgjVmJ-Dm2XHqsqbwOXd56oi3t6JAS3VxM_OCvprtldVWS402HhKpHTxvQphHPeCU5JRWk-OWpucgsfMhWb6AFCZQtZ66hcin0NKKI1K6mGaNtGPFrDWrEumk0WRvhHduEFuKRfjx6Lax6XNtCYS1mXW4PtjbwowH3SHuPYuT9S71za0LuG8QR9oZ75yCdrb3Ipok6phF3rO5IcDwLWQ4UvQaYySdz0jjSnQPBng4gzsjQhiP_P7XsQQonA_odvL_LJK7vSxHMGLwlIZAyrC3n3CWLvqlzAFd1BJcHX_p9fYEW0hbwRZBSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7e5ce77a.mp4?token=laY5b_ehKAg0qBRq1CI_ZUSkPXFpKE64DArJwgYXVOK6XvaDbXNqggxpt2zzF0_Aew7XgnINq5PlX_ON1xkTloeLDHWD7NWgxcjsOFPx_M0LrH9b3ezYR2YOSspYIc-xVQtnmr5d-MLRZgXHTVH9vwMt3yGsY3W0TfWETmiCCq0k--YKRyaVXb2Y_06jU_I-oPS2-GnyUBu5DacG5a72JowCwU1mc-0XHu0eSsTVftttlB2aCtCQTJs4zZf1fJzDbJUkiEW01o7_g5mspCVfbNFpkQfOMw9btcQ1N76zZD4BMxv40YL2Lt3YexPrAFAi47SB9NwpQbkD7Z0111IklEr31g43kgBV6nmjiadbeEIKNUfWVbwPsgjVmJ-Dm2XHqsqbwOXd56oi3t6JAS3VxM_OCvprtldVWS402HhKpHTxvQphHPeCU5JRWk-OWpucgsfMhWb6AFCZQtZ66hcin0NKKI1K6mGaNtGPFrDWrEumk0WRvhHduEFuKRfjx6Lax6XNtCYS1mXW4PtjbwowH3SHuPYuT9S71za0LuG8QR9oZ75yCdrb3Ipok6phF3rO5IcDwLWQ4UvQaYySdz0jjSnQPBng4gzsjQhiP_P7XsQQonA_odvL_LJK7vSxHMGLwlIZAyrC3n3CWLvqlzAFd1BJcHX_p9fYEW0hbwRZBSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما: نتانیاهو خیلی مرده؛ نه خسته شده از جنگ با ما، نه پشیمونه و هرآن ممکنه بهمون حمله کنه و بنظرم خیلی مرده.
@WarRoom</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/withyashar/21286" target="_blank">📅 15:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21285">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترکیه، حکم بازداشت اینترپل قرمز برای  نتانیاهو صادر کرد و او را به عنوان متهم در ارتباط با حادثه "ناوگان مقاومت" عنوان کرد
@WarRoom</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/21285" target="_blank">📅 15:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21284">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba907831b.mp4?token=Kmhs4clyMbDnwYswN7DdE4993gH9wCzDHRljWHMVt6lFctJmL4idqBe6T4F1J1zSEtGb28p0_6ReAQX_wakO95U-sF1hoIM1rALPePlqLVbzT1UPvfGuoE4fKn-BCi6GAB27KmXZN1s7sDyX47k6IY2_gkSupLAfJcftHSdyoHgbFs8wDeAzR8tKxV2wkRwq2b-Sfzy52p2oVEntc7UJDAZBzxmmIIxb0iJcYENQzS390tYH24Rk8Gm-PS5MZSmQrp7OxDtNqTVcGVCFEBuF_-D82dC-2i4b-i_rkSgmXJxw5SKjy9Dhk2zmUZunKOsMx9Ty0NNjA0bTdhe1JfiwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba907831b.mp4?token=Kmhs4clyMbDnwYswN7DdE4993gH9wCzDHRljWHMVt6lFctJmL4idqBe6T4F1J1zSEtGb28p0_6ReAQX_wakO95U-sF1hoIM1rALPePlqLVbzT1UPvfGuoE4fKn-BCi6GAB27KmXZN1s7sDyX47k6IY2_gkSupLAfJcftHSdyoHgbFs8wDeAzR8tKxV2wkRwq2b-Sfzy52p2oVEntc7UJDAZBzxmmIIxb0iJcYENQzS390tYH24Rk8Gm-PS5MZSmQrp7OxDtNqTVcGVCFEBuF_-D82dC-2i4b-i_rkSgmXJxw5SKjy9Dhk2zmUZunKOsMx9Ty0NNjA0bTdhe1JfiwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : ایران کم‌کم متوجه می‌شود که رئیس‌جمهور ترامپ و ارتش آمریکا در خارج کردن مخفیانه نفت از تنگه هرمز تا سقف ۱۰ میلیون بشکه موفق هستند.
بعضی شب‌ها به ۱۵ تا ۲۰ میلیون بشکه می‌رسد... این جریان قبل از جنگ است!
حتی سی‌ان‌ان هم مجبور شد اعتراف کند: ایران در حال از دست دادن کنترل خود است
همچنین رئیس‌جمهور ترامپ جبهه دیگری را باز می‌کند و کشورهایی را که به تهران کمک کردند تا سرپا بماند، تهدید می‌کند.
چیزی از ایران باقی نخواهد ماند.
ملاها این را خواستند.
@WarRoom</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/21284" target="_blank">📅 14:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21283">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ای‌بی‌سی‌نیوز: FBI از احتمال حمله پهپادی ایران به کالیفرنیا خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/21283" target="_blank">📅 13:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21282">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کارشناس صداوسیما:
علی خامنه‌ای یک پله از امام علی پایین‌تر بود و معجزه هم میکرد.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/21282" target="_blank">📅 12:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21281">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بیتکوین 77,000$ را شکست و در چند روز 15000$ گران شد @WarRoom</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/21281" target="_blank">📅 12:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfUUQ04jf6tN0muTtiT8KuU7oDhg-w6ohKlkftwLvY93MMzOMGP_1APwV_eSfss8SsNSUp4dO-3AfT6SNREJ_8xJL_5dHasK12ZMXSw9KKQfL2BQhpjI_E5v1hOJDfrqcBo76hszu1jeVuvFEwaSrnDIyz927k1FDAFPZnEQeeShEGGE1h0Fi5vdFxseOYwnujzigAq_fkRyMdXnCjSO5u5o7ZCvdWKls7FVXOp-9tf7VBSE9PATsA0gEoVWKCpH1fCEssqrnAkwXZKeZIux_j1K1ABQNkZ8F7Gl_zHeAUR1egUPehok4_UUvsE_vy9fzuTi1jNjRxGAkB3vSutkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3MSWIurcaXzRgKjEkwpBkEVZ3i4wN829D54JN_1HR6ZyD3OtX3stAYpw86ABVl8mj8EZtjHX30q-nrgbO1vl0HWJyXBjwYERNl8C0mkK8SqnW8gFEOFya8v6uEVS9DTXcERTegU01S_vpEAB9FuGyZnsm1cvrhQm1nzyA-hM-8BRoWqF7g3FhZ23DgaP1mw_6zVhF_a9IofMNa0Lv04o-b4acEi3--OFWEnHmTq8t1GW5veKeDDP8SoaWB6ywnqvf9YqbvgjNe_igr28_5kqYj6N1nv0g9X33CIjJf9JwubaI8I4e5uCtyzPbEfe3reBYOFg83k89wTU-gqJRRzjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب یک هواپیمای بویینگ E-3B سنتری  AWACS آلارم 7700 وضعیت اضطراری روشن کرد. ولی اکنون یک هواپیمای دیگر با همان مدل و مشخصات به پرواز در آمده که نشان می‌دهد که آمریکا تجهیزات کافی پشتیبانی در منطقه بسیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/21279" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بیتکوین 77,000$ را شکست و در چند روز 15000$ گران شد
@WarRoom</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/21278" target="_blank">📅 11:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce_U_sMlafUnrSkE7QUL413vONFtYOqyXYNQJvliB5WaplaEy4_QkKoagt1BGHKUwRtNJOLe6sKz95-1SGqqRE2oLaWZqCdf_ZNhoKsdbrS3DvVCReMSMXFwRj4TTYZVgbcIeU0Sr0kL-llFoY0q0TsPDS7sMLyzlh_zg6eVn5K_m4ieS6o3EPeFxAKauT2VWQpj8dcj5W7PAENaYVnUM16ggFa4m215GRJ95GjI75zoOFUQQe6W2FzVhpS_wPsaZQ75JZpDkGuUXWg2rd1416v3WoEtM71Fh6eMv1IJScXGUn8M-fihKY_OUmwFg2zGknfPkkR49XXYPP1iHLi3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده، دومین هواپیمای تانکر سوخت‌رسان را از مجموع شش فروند هواپیمای جدید، به نیروی هوایی اسرائیل تحویل داد.
@WarRoom</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/21277" target="_blank">📅 11:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش های بسیار از چندین صدای پرتاب از سیریک ، خونه ها لرزیدن و صدای انفجار از تنگه و صدای جنگنده ، همون فرمولی که گفتم جمهوری اسلامی میزنه نفت بره بالا  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/21276" target="_blank">📅 11:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏سقوط چشمگیر تردد در تنگه هرمز؛ تنها ۷ کشتی باری در روز پنجشنبه عبور کردند.
‏داده‌های شرکت ردیابی دریایی کپلر نشان می‌دهد تردد کشتی‌ها در تنگه هرمز روز پنجشنبه به نصف روز چهارشنبه کاهش یافت و تنها ۷ کشتی باری، شامل ۴ کشتی ورودی و ۳ کشتی خروجی، از این گذرگاه راهبردی عبور کردند. هیچ‌یک از این شناورها نفتکش یا حامل گاز طبیعی مایع نبودند، هرچند یک کشتی بسیار بزرگ حامل پروپان و بوتان از مسیر ایران از تنگه خارج شد. پرزیدنت ترامپ نیز طی روزهای اخیر بارها تأکید کرده است که ایالات متحده کنترل تنگه هرمز را در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/21275" target="_blank">📅 10:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21274">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏کانال ۱۴ اسرائیل: ترکیه با وجود هشدارهای نتانیاهو، محموله نظامی دیگری به سوریه فرستاد.
‏بر اساس این گزارش، ترکیه محموله تازه‌ای شامل حدود ۲۰۰ خودروی نظامی، از جمله ۲۰ تانک، به سوریه اعزام کرده است؛ اقدامی که با وجود هشدارهای نتانیاهو درباره تحرکات نظامی ترکیه در سوریه انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/21274" target="_blank">📅 10:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21273">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رویترز: در تهدید ترامپ علیه کسانی که به ایران کمک می‌کنند، حتی متحدان واشنگتن که در میانجیگری مذاکرات صلح نقش داشته‌اند هم ممکن است در این دایره قرار بگیرند و آن را شامل هر کشور یا نهادی کرده است که به تهران آنچه را او «شریان حیاتی» توصیف کرده، ارائه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/21273" target="_blank">📅 10:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21272">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/21272" target="_blank">📅 09:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDr.t</strong></div>
<div class="tg-text">کجایی ؟ داشتم نگران میشدم</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/21271" target="_blank">📅 09:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21270">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ : ما گزینه دیگه‌ای جز جنگ با جمهوری اسلامی نداشتیم و اگه لازم باشه ۱۰۰ بار دیگه‌ هم اینکارو تکرار میکنم چون آنها نباید به سلاح هسته‌ای برسند!
جمهوری اسلامی به کشورهای بی‌طرف مثل عربستان، قطر، امارات، کویت و بحرین حمله کرده!
اگه برجام رو پاره نمیکردم، الان سلاح هسته‌ای داشتند و ازش علیه همه کشورها استفاده میکرد!
رسیدن به توافق با آنها اصلا آسون نیست چون درحال حاضر هیچکس نمیدونه دقیقا چه کسی داره رهبری میکنه!
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/21270" target="_blank">📅 09:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21269">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سخنگوی پنتاگون به وال استریت ژورنال: ما تمام امکانات لازم را برای شروع حملات به ایران  را در زمان و مکانی که رئیس جمهور تعیین می‌کند، در اختیار داریم و هیچ کمبودی نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/21269" target="_blank">📅 09:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21268">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_R43Rrd4jAVqw7IOi0bZqgI-7cQJ3HpR7ET-DpfbJsvVG3-YBidRAP0CTQ4_imylWjk3SaqGFhTJta6li0gD2ngsVtVeVCc_Sx2Pn2uKoNx2DV66D8H30oiKRiIp6difLRTgTUTb4NSQ7brJUV8329P6PHfSuxoE4dc3n3Ac4nsu5ArxmF2EyDub_DrV37bzDsymOiu7A32Nv6zONujKEwmb9--iZyDF33Ij-cissNhHEVq6OftC9rl6wwZmkQUUGBHcDyLqL5zKYkGKSUhsDTrJTn2IQEId59Vr0q2wUmTtKXaMVsMNBGkziy9G1RYVHsniKzGCeD3jwTIEDxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند مرفه رژیم جنایتکار ایران برای فرار از بازداشت ICE و بازگشت به زندگی لوکس در لس‌آنجلس پول جمع می‌کنند.
یک فعال ایرانی‌تبار که در جریان اعتراضات ایران بر اثر شلیک سپاه یک چشم خود را از دست داده، از
سید عیسی هاشمی، پسر معصومه ابتکار، معروف به «مریم جیغ‌زن»
، انتقاد کرده است. هاشمی ۴۳ ساله که از سال ۲۰۱۰ در آمریکا زندگی می‌کند، چند ماه پیش توسط
ICE
در کالیفرنیا بازداشت شده و روند لغو گرین‌کارت و اخراج او در جریان است؛ اقدامی که بنا بر گزارش با دستور
مارکو روبیو
انجام شده است. او اکنون با راه‌اندازی کمپین
GoFundMe
از مردم آمریکا کمک مالی می‌خواهد تا بتواند در این کشور بماند و به زندگی خود در لس‌آنجلس ادامه دهد
@WarRoom</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/21268" target="_blank">📅 09:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21267">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ در تروث بازنشر صحبتهای مقام ارشد کاخ سفید ، استفن میلر: او (ترامپ) ناامن‌ترین مرز تاریخ آمریکا را تحویل گرفت و ۱۵ ماه پیاپی، ورود غیرقانونی به کشور را به صفر رساند؛ برای انرژی و زنجیره‌های تأمین آمریکا دستاوردی تاریخی رقم زد، با کارتل‌های مواد مخدر مقابله کرد و آن‌ها را سازمان‌های تروریستی خارجی اعلام کرد؛ مانع دستیابی ایران به سلاح هسته‌ای شد؛ با ساخت خطوط لوله و افزایش تولید انرژی، قیمت بنزین را کاهش داد؛ تورم را به ۲ درصد رساند و با تصویب بزرگ‌ترین کاهش مالیاتی تاریخ آمریکا، مالیات بر انعام، تأمین اجتماعی و اضافه‌کاری را لغو کرد؛ یک پیروزی بزرگ و تمام‌عیار.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21267" target="_blank">📅 00:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21266">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک مسئول دولت ترامپ به واشنگتن پست:
ایران "کاملاً ورشکسته" است و ترامپ ابزارهای متعددی در اختیار دارد که می‌تواند در هفته‌ها و ماه‌های آینده از آن‌ها به شکلی قوی‌تر استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21266" target="_blank">📅 00:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21265">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21265" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21264">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کانال 14 اسرائیل: مجتبی خامنه‌ای «
ایزوله
» شده و سپاه کشور را اداره می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21264" target="_blank">📅 00:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21263">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ارسالی تایید نشده : یاشار همین الان اهواز صدای شلیک موشک میومد قشنگ ی دودی توی هوا معلوم بود ولی دوربین گوشی اینقدر قوی نیست که بتونه دود رو بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21263" target="_blank">📅 23:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cf8ca15a.mp4?token=mcInJd-bAAT9-9BdFdNR2OjtnPs_LKs9-ttJnRjgVtDU-sjpDPb-Rc_0ruV6Id6kldAHDNGFvN1UqMtOfQA0dHz6YtDJrDVO-IAf489eQLqmhZITn-PrUvTA7HvY6KhkAOqh-azWdMltdsCMEdAhzltMI6KVLYcSU2etHPA4GIx-89GiIVp7E3BYi7YLm6mb_QGSCNVpngIqtPFkDnav9R-5KdV8z3ZoMwq1avVgTh6e7ArKWamSsRdGmcPyQSujR8EnpxCdl3Qi8wIT2zEsXxjqp49t2vVGVE2LDdHKyJJAA0PxyWsyUpv-XNTBgGmd-FeICmi7d9md9tMSm2in6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cf8ca15a.mp4?token=mcInJd-bAAT9-9BdFdNR2OjtnPs_LKs9-ttJnRjgVtDU-sjpDPb-Rc_0ruV6Id6kldAHDNGFvN1UqMtOfQA0dHz6YtDJrDVO-IAf489eQLqmhZITn-PrUvTA7HvY6KhkAOqh-azWdMltdsCMEdAhzltMI6KVLYcSU2etHPA4GIx-89GiIVp7E3BYi7YLm6mb_QGSCNVpngIqtPFkDnav9R-5KdV8z3ZoMwq1avVgTh6e7ArKWamSsRdGmcPyQSujR8EnpxCdl3Qi8wIT2zEsXxjqp49t2vVGVE2LDdHKyJJAA0PxyWsyUpv-XNTBgGmd-FeICmi7d9md9tMSm2in6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملانیا ترامپ، بانوی اول: شنیدم دلتان برایم تنگ شده بود. من اینجا هستم.به کاخ سفید خوش آمدید
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21261" target="_blank">📅 23:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏تانکر ترکرز:‏ دلیل اینکه دیگر در خارک شاهد بارگیری‌های زیادی نیستیم، این است که تولید نفت خام ایران در ماه‌های اخیر به سطحی کاهش یافته که فقط اندکی بالاتر از میزان مصرف پالایش داخلی این کشور است. این یعنی ایران در حال حاضر فشار چندانی برای صادرات نفت ندارد.
‎
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21260" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/471bef475d.mp4?token=gfhcNygdB04iEXIAD2SQ3HIvfPyWtZ6Y5yzwcyShatN9tWqVYjN9epypPadAbOu1mFwozW0GKzK2cMdoU2G-xoq-EERy_f86EcrvjoF-LjliPiSgO5LYNcKBZcov38WX6iohc08j8DVi1jLD4R86CyTj94ih-mlFYhbsr_D2J3tIwUDZWbkHEDzX05M9WgwMef2ESyhj50aU-VF5SrLqZISCdXrAYum155oZs_3FkND-FdbtuDCQhwuJacXFyT3NnoycxuPR4XU1wEnkRuQ_N8WTm5GsTlkZ5BTXvYi_o1a6ltz7yUQsKm6qfEdlCkU0PVCJT_1io3AAF2p3blXEyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/471bef475d.mp4?token=gfhcNygdB04iEXIAD2SQ3HIvfPyWtZ6Y5yzwcyShatN9tWqVYjN9epypPadAbOu1mFwozW0GKzK2cMdoU2G-xoq-EERy_f86EcrvjoF-LjliPiSgO5LYNcKBZcov38WX6iohc08j8DVi1jLD4R86CyTj94ih-mlFYhbsr_D2J3tIwUDZWbkHEDzX05M9WgwMef2ESyhj50aU-VF5SrLqZISCdXrAYum155oZs_3FkND-FdbtuDCQhwuJacXFyT3NnoycxuPR4XU1wEnkRuQ_N8WTm5GsTlkZ5BTXvYi_o1a6ltz7yUQsKm6qfEdlCkU0PVCJT_1io3AAF2p3blXEyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن وارد مرحله جدیدی در قبال ایران شده که در آن
فشار اقتصادی مؤثرترین ابزار آمریکا
است. ونس گفت ایران در دو هفته گذشته فشار اقتصادی بیشتری نسبت به آمریکا متحمل شده و واشینگتن قصد دارد این فشار را ادامه دهد. او تأکید کرد تأسیسات هسته‌ای ایران نابود شده‌اند، اما هدف آمریکا ایجاد
«واقعیتی جدید»
است
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21259" target="_blank">📅 23:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c77add985.mp4?token=hYn5wsq1T1JxJdy1Suejs85At_d2eSOaIDTGg4g_9Enkt7qesFwLNL4RTtoM1eRXtvP6EO03AFPv2Pr6l7c0qcujUq04DLGHWITcClPKPzftGXSYlotDGGRKQebBF3kjSSndVMNST7H1QpT1ZX-jfHKYU7jNENUqVvp_opmS114-i9iTRcZLaoSUx3JDiDxS8oG4VWPuW76fbAkGok2_i76MJRRXVt6R3B68Qgk5iXsr0eloIMEGFsylL1CsTO4nFBpKjY_p9AGsqPp4NWHqosW2NiNZM8ZKXPfMl0bTwrIzbSiG1XDocyItAg42Kmhi8zi7bC6hdqL1W3wuH5mCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c77add985.mp4?token=hYn5wsq1T1JxJdy1Suejs85At_d2eSOaIDTGg4g_9Enkt7qesFwLNL4RTtoM1eRXtvP6EO03AFPv2Pr6l7c0qcujUq04DLGHWITcClPKPzftGXSYlotDGGRKQebBF3kjSSndVMNST7H1QpT1ZX-jfHKYU7jNENUqVvp_opmS114-i9iTRcZLaoSUx3JDiDxS8oG4VWPuW76fbAkGok2_i76MJRRXVt6R3B68Qgk5iXsr0eloIMEGFsylL1CsTO4nFBpKjY_p9AGsqPp4NWHqosW2NiNZM8ZKXPfMl0bTwrIzbSiG1XDocyItAg42Kmhi8zi7bC6hdqL1W3wuH5mCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل و شاباک فاش می کنند: سازمان تروریستی حماس در بیمارستان «ناصر» در خان‌یونس بازجویی‌های امنیتی و شکنجه انجام می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21258" target="_blank">📅 23:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ادعای نیویورک تایمز :
ناو هواپیمابر
آبراهام لینکلن
پس از حدود
۹ ماه استقرار و ۲۷۲ روز مأموریت
در خاورمیانه، که بخش قابل‌توجهی از آن در پشتیبانی از عملیات آمریکا علیه ایران گذشت،
منطقه را ترک کرده و در مسیر بازگشت به سن‌دیگو قرار دارد
. این ناو در
۲۱ نوامبر ۲۰۲۵
از سن‌دیگو حرکت کرده بود و هزاران ملوان آن تقریباً تمام این مدت را در دریا سپری کردند.
ناو هواپیمابر جورج واشینگتن
که از ژاپن به سمت غرب حرکت کرده بود، اکنون وارد منطقه سنتکام شده و قرار است جایگزین لینکلن شود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21257" target="_blank">📅 23:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش های بسیار از چندین صدای پرتاب از سیریک ، خونه ها لرزیدن و صدای انفجار از تنگه و صدای جنگنده ، همون فرمولی که گفتم جمهوری اسلامی میزنه نفت بره بالا
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21256" target="_blank">📅 22:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تنگه بدجور دعواشده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21255" target="_blank">📅 22:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اد
میلیبند وزیر خارجه بریتانیا دیروز
از طرح اسرائیل برای ساخت‌وساز در منطقه
E1 در کرانه باختری
انتقاد کرد و آن را اقدامی «غیرقابل‌قبول و مخرب» خواند. او از اسرائیل خواست طرح را پس بگیرد و گفت بریتانیا در واکنش به گسترش شهرک‌سازی، اقدامات و تحریم‌های هدفمند بیشتری را بررسی می‌کند.
در پاسخ،
ایتامار بن‌گویر امروز،
در شبکه اجتماعی ایکس خطاب به او نوشت: «کسی باید اد را به‌روز کند که قیمومیت بریتانیا بر سرزمین اسرائیل در سال ۱۹۴۸ پایان یافت و اسرائیل کشوری مستقل است» و سپس با کنایه به میلیبند گفت به جای «بازی با دوران قیمومیت»، به لندن نگاه کند که به گفته او «به‌سرعت در حال تبدیل شدن به یک خلافت اسلامی است».
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21254" target="_blank">📅 22:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIR0tC47QfnWdlkjSQ_Oo5SnKWbMH1-GfA1G_fMwfkL0-E-tcxM2NL98uBw-mAEpnU-NPHHBr39N0WbrrJnrSk91_UAoWBKXp3lpUYY6QW9t0TwMD3gF9ImfbLuY9b7YAG5JsXGa_J4ngV56ONfTcy88EH12Ge9F12ga3pPxntb_IlJWIlLNjAER91iZ1tT8TBR8IQuZmKm2qAbOwWZ9s-_acURJErrXfC1HAqdo-zSp6TlYy3YGFMWCh3t3Oy6I8RlOvB5O1EDGqmalZmnIiAr-Eo5RDEW91UwvgZZy-zMJJ95NeNEGBsRXZqiC2o96hz_q_6FBBHuTJzG9Dlt37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظر یک کاربر اتاق جنگ
🫱🏼‍🫲🏽
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21253" target="_blank">📅 21:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بر اساس بیانیه‌ای که دقایقی پیش در وبسایت وزارت خزانه‌داری ایالات متحده منتشر شد، ۹ شهروند با پاسپرت ترکیه و یک شهروند ایرانی با نام مسعود مسافر به‌ظن ارتباط با حزب‌الله لبنان یا نیروی قدس سپاه به فهرست تحریم‌های ایالات متحده افزوده شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21252" target="_blank">📅 21:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال 15 عبری : نتانیاهو در حال حاضر جلسه‌ای خصوصی با حضور روسای سازمان‌های امنیتی، از جمله سازمان‌های اطلاعاتی، برگزار می‌کند تا در مورد تمام تحولات آتی، به ویژه در سوریه و در روابط با ترکیه، بحث و تبادل نظر کنند. این اقدام در پی اعلام ترک‌ها مبنی بر ادامه فعالیت‌هایشان در سوریه صورت می‌گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21251" target="_blank">📅 20:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
دوشنبه جزئیات اقدامات جدید را اعلام می‌کنم. اگر سیاست
حداکثر فشار اقتصادی
ادامه یابد، فعلاً احتمال آغاز دوباره عملیات نظامی گسترده کم است. آمریکا در عین حال کنترل تنگه را در اختیار دارد و می‌تواند جریان انرژی را مدیریت کند. ما در حال اجرای
بزرگ‌ترین عملیات هماهنگ انزوای اقتصادی در تاریخ جهان
هستیم و به کشورها هشدار می‌دهیم که اگر به تجارت، انتقال پول، خرید نفت یا انتقال کشتی‌به‌کشتی با ایران ادامه دهند، با تمام توان تحریمی آمریکا مواجه خواهند شد. هدف،
درهم‌کوبیدن اقتصاد این رژیم جنایتکار، قطع توان مالی آن برای حمایت از نیروهای نیابتی و تأمین هزینه‌های نظامی
است. بسنت تأکید کرد: «این روش در همه جا جواب داده؛ ما یک ضربه دوگانه شامل
محاصره و سخت‌ترین تحریم‌های تاریخ
وارد می‌کنیم و
در ایران نیز موفق خواهد شد. ما این رژیم را فرو خواهیم ریخت.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21250" target="_blank">📅 20:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بسنت ، وزیر خزانه‌داری آمریکا:  ما نظام ایران را سرنگون خواهیم کرد @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21249" target="_blank">📅 20:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏وزارت جنگ ایالات متحده در حال بررسی برکناری مکس لدرر، ناشر باسابقه روزنامه نظامی «استارز اند استرایپس»، پیش از موعد بازنشستگی اوست. این اقدام پس از انتشار گزارش‌های انتقادی فیک این روزنامه درباره وضعیت خدمه ناو هواپیمابر «آبراهام لینکلن» در جریان جنگ علیه جمهوری اسلامی و همزمان با تشدید اختلاف میان این رسانه و مقام‌های نظامی آمریکا مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21248" target="_blank">📅 20:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpZG7G-Ghs6cp-xTTIOzy3m_b09nCP4PV6l5g07GsesAqUknWr07onOBTsuRxLvTJm3V-PS8UDH6BMdZGQtFxGxkAGSrEBtIX9Yw32bBzdgQ4izXGG0BF_DSeZFEKEJyZ4W_UyyjZIKnJrpBZsSVVQesmaVnBGlchSfoxq9taWgv2wEGY2Houpa6d9VZmacHEUAH8byrF0bn0eKppwihFmzn6O4u_vhJcm4DuozxpkiCbcoBvbc5X0JClKuCh7EJzRjvyo-icynKDbWLckmfkWrnTb4r6tKI1F88895iqAJ40gWYxvzsb5RH6IU8mNPudNrfejfo_Zrfu7A5du1rjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنت‌کام : نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۶۷ کشتی تجاری را تغییر مسیر داده‌اند، ۳ کشتی را غیرفعال کرده‌اند و ۲ کشتی را برای اطمینان از رعایت مقررات به بازجویی و بازرسی برده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21247" target="_blank">📅 19:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانادین پرس :
پیر پویلیور،
رهبر حزب محافظه‌کار کانادا و رهبر اپوزیسیون رسمی این کشور
، از رضا پهلوی، ولیعهد ایران، دعوت کرده است به کانادا سفر کند. پویلیور روز شنبه در مراسمی در بریتیش کلمبیا اعلام کرد که علاوه بر این دعوت، قرار است به‌صورت مجازی با رضا پهلوی دیدار کند. او در این مراسم گفت این دیدار فرصتی برای گفت‌وگو درباره
دموکراسی و امنیت ایرانیان خارج از کشور
است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21246" target="_blank">📅 19:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بسنت درباره ایران: ما از این وضعیت مناقشه با ایران عبور خواهیم کرد. نمی‌دانیم چه زمانی. @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21245" target="_blank">📅 18:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21244">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3286979e.mp4?token=cbDolKyd-8dKTzKE7umfWhnM3fOYJitZT37elXu4LeGhC7HxWXOZDDYLBpaIC5b422EF-8zJfu_QCw0gT5_Z3ZZ8bp5W6r-4jfsO7Fys8q3NoYjxQSCejAnIBqA0Zcp2B5hYARK7_JKDcejqM99ysi7vAQPI7qK5SajcJcT6hoVg9n4RvpUy7OIqnug8QE7IHHyYDiidlmg9aEhAdrLu38PY2K0PmtZfoNn7mKtvY851qlGznQS6TSVtDKprJhhFCNqGOulkAmH4VsH-4p21BRy-0-4KCRDTlF4dy_tXW59pMWPhyTEj3Rt6RWpdWgYkyVJtwkN4EQ1Ch2uaYYCcgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3286979e.mp4?token=cbDolKyd-8dKTzKE7umfWhnM3fOYJitZT37elXu4LeGhC7HxWXOZDDYLBpaIC5b422EF-8zJfu_QCw0gT5_Z3ZZ8bp5W6r-4jfsO7Fys8q3NoYjxQSCejAnIBqA0Zcp2B5hYARK7_JKDcejqM99ysi7vAQPI7qK5SajcJcT6hoVg9n4RvpUy7OIqnug8QE7IHHyYDiidlmg9aEhAdrLu38PY2K0PmtZfoNn7mKtvY851qlGznQS6TSVtDKprJhhFCNqGOulkAmH4VsH-4p21BRy-0-4KCRDTlF4dy_tXW59pMWPhyTEj3Rt6RWpdWgYkyVJtwkN4EQ1Ch2uaYYCcgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت درباره ایران: ما از این وضعیت مناقشه با ایران عبور خواهیم کرد. نمی‌دانیم چه زمانی.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21244" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مسرور بارزانی، نخست‌وزیر اقلیم کردستان عراق به المانیتور با اشاره به بیش از
۱۰۰۰ حمله موشکی و پهپادی
علیه اقلیم از زمان آغاز جنگ آمریکا و اسرائیل با ایران در ۲۸ فوریه، خواستار تقویت پدافند هوایی شد. او هشدار داد خروج سامانه‌های
پاتریوت و نیروهای آمریکایی
، اقلیم را آسیب‌پذیرتر می‌کند و از آمریکا و متحدانش خواست برای تأمین پدافند هوایی، سامانه‌های هشدار زودهنگام و تجهیزات مقابله با پهپاد کمک کنند. بارزانی همچنین گفت حملات اخیر به دفتر شخصی او و خانه رئیس شورای امنیت اقلیم با هدف
ارعاب و کشاندن اقلیم به درگیری
انجام شده است. او مدعی شد پهپادهای استفاده‌شده در این حملات
ایرانی و از نوع حدید-۱۱۰
بوده‌اند و هیچ کس دیگری ندارد؛ ادعایی که ایران آن را رد کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21243" target="_blank">📅 17:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اتاق جنگ با یاشار : فلورا جون ۲ @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21242" target="_blank">📅 15:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">العربیه : ۳ نفر از نیروهای سپاه در حملات به مواضع حوثی های یمن کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21241" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یک مقام آمریکایی و یک مقام کاخ سفید به خبررگزاری سمافور گفته‌اند که دولت آمریکا معتقد است
مذاکرات ایران و عمان از چند هفته قبل عملاً شکست خورده است
. احتمال دریافت عوارض از کشتی‌ها برای عبور از تنگه هرمز و پیشبرد سازوکاری جدا از مذاکرات مستقیم تهران و واشنگتن از دلایل اصلی نارضایتی دولت ترامپ عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21240" target="_blank">📅 14:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو: بازسازی نوار غزه تنها در صورتی امکان‌پذیر خواهد بود که حماس به طور کامل از سلاح‌های خود محروم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21239" target="_blank">📅 13:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو : شما سورپرایز خواهید شد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21238" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cd8ea5eb.mp4?token=IXprD0R_qmIruvAu0dPe6rr86-xzW1qdmChthPR7qrk-CTVmIUTQWC9cl2BcjkN9RVUln7Zd_kPfklIz0dwrlAMexOyKkOBG_P6SmDxgwKbgiLUGfiIQNaXkmAVRpg2hiHLodo9xyjPIXQxDWHRecBtdfc0oYUL1E-YA0uCsVeuRSEOPFz0o0eae3vNiPsSKfftdNYpt665EELjapA9JpRNUHeuG8UhZb592GpKYAvcQojlLKwHGnKTlWRh9enO_5qiPslhaIqGsdWuTu1HbzntZmJ7AmmmFKzX58I5MrnV1T6frJHZ6Pi4JjHqpaLNplKPAft3JBHXXdNYmMcrxsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cd8ea5eb.mp4?token=IXprD0R_qmIruvAu0dPe6rr86-xzW1qdmChthPR7qrk-CTVmIUTQWC9cl2BcjkN9RVUln7Zd_kPfklIz0dwrlAMexOyKkOBG_P6SmDxgwKbgiLUGfiIQNaXkmAVRpg2hiHLodo9xyjPIXQxDWHRecBtdfc0oYUL1E-YA0uCsVeuRSEOPFz0o0eae3vNiPsSKfftdNYpt665EELjapA9JpRNUHeuG8UhZb592GpKYAvcQojlLKwHGnKTlWRh9enO_5qiPslhaIqGsdWuTu1HbzntZmJ7AmmmFKzX58I5MrnV1T6frJHZ6Pi4JjHqpaLNplKPAft3JBHXXdNYmMcrxsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی پالایشگاه نفت تهران:
ستون‌های دود در آسمان تهران، ناشی از آتش‌سوزی در دو مخزن مربوط به بسته‌بندی و انتقال محصولات نفتی، در محوطه پالایشگاه نفت در پایتخت تهران است. هیچ آتش‌سوزی در داخل خود پالایشگاه رخ نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21237" target="_blank">📅 12:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رسانه‌های سعودی به نقل از منابع گزارش دادند:
دولت ترامپ از اطلاعاتی درباره یک طرح ایرانی برای عملیات‌هایی که فراتر از هدف قرار دادن کشتی‌ها است، و همچنین طرح نیروهای یمنی برای افزایش هدف قرار دادن کشتی‌ها در تنگه باب‌المندب، مطلع شده است.
ترامپ به تیم خود اطلاع داده است که در صورت ناکارآمدی تحریم‌های اقتصادی، احتمال انجام حملات گسترده علیه ایران وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21236" target="_blank">📅 12:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیتکوین در حال پرواز است و با قدرت از مرز ۷۱،۰۰۰ دلار هم عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21235" target="_blank">📅 11:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e050dd4cf1.mp4?token=CfXFokdN_zRmiSS74QsKxJISX9G71-nPLImkYx4oUQExHo2PtNLLmZRbqlKDywGKvD_tWNFH3xcOd5BTcQN6KD4SciNyY8Zi9MLuhq82Sl4XVi0oABtyClMLLLgJL9VB_MHvcP3SCWqdQmtWzR8Kh7IQTZgr1_0-TTn2RD4yDtEr5Kag-ap7wnxwS-aJ7zn3hexO-3P1l8zZeN_lEJVO8xv-rhDAevtpW-bbV4BOBaSap21ptJemGvPFHvxq9t4gOgzyZIIRyeJQbHM9la56G1p-R9OB9t6BhHMcB4DRq7MA8dlr1TZ2BEDw8Y72VVwNOB69JmHByXBJDvhc-8AWRaGdt7uO_Vfw_FtjMOkY66hTPwBqIfM4XeWgppeMctc8G8y6SN7fdtDOtT2JzkSsyPHapBpAYp3InXxwTllTq86yAsMtuy91OqHgBkGrM0FrIYF50HPdugmxOaX8HslHa1q59RAvv7tKzZ0PgjJJUtgNAQkpcORXDhnvYs7LLsx03WaIkRDShqSYkY_BdZ_Thh3BOKYcXHUVKlZHj6eowlTNZW862hOn1eTYeOEzM3MIJo7puh5k1yev7CYGifpwjSIPHlU8olLzi9pgsr91eoNxzHTbAJcyotwvFXcZyei76F2PBVPI09kTHHvZFmjgbRrMguO27rws9ehIFs8GA9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e050dd4cf1.mp4?token=CfXFokdN_zRmiSS74QsKxJISX9G71-nPLImkYx4oUQExHo2PtNLLmZRbqlKDywGKvD_tWNFH3xcOd5BTcQN6KD4SciNyY8Zi9MLuhq82Sl4XVi0oABtyClMLLLgJL9VB_MHvcP3SCWqdQmtWzR8Kh7IQTZgr1_0-TTn2RD4yDtEr5Kag-ap7wnxwS-aJ7zn3hexO-3P1l8zZeN_lEJVO8xv-rhDAevtpW-bbV4BOBaSap21ptJemGvPFHvxq9t4gOgzyZIIRyeJQbHM9la56G1p-R9OB9t6BhHMcB4DRq7MA8dlr1TZ2BEDw8Y72VVwNOB69JmHByXBJDvhc-8AWRaGdt7uO_Vfw_FtjMOkY66hTPwBqIfM4XeWgppeMctc8G8y6SN7fdtDOtT2JzkSsyPHapBpAYp3InXxwTllTq86yAsMtuy91OqHgBkGrM0FrIYF50HPdugmxOaX8HslHa1q59RAvv7tKzZ0PgjJJUtgNAQkpcORXDhnvYs7LLsx03WaIkRDShqSYkY_BdZ_Thh3BOKYcXHUVKlZHj6eowlTNZW862hOn1eTYeOEzM3MIJo7puh5k1yev7CYGifpwjSIPHlU8olLzi9pgsr91eoNxzHTbAJcyotwvFXcZyei76F2PBVPI09kTHHvZFmjgbRrMguO27rws9ehIFs8GA9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : فلورا جون ۲
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21234" target="_blank">📅 10:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoPxul1u_qyLLQmyx-S6pFBx8HEilhixPd3DibcAstca0Sb4grIYYMN_ht3ZS5ugfHWgcUbFV1W6ADJfrxn02_sMkcq8Pbm2phrGfSh0e7deeisBMguNaBovWUXpJ9gkUyeQFxgR2erh24vyxwo-Bm8MoMkSb9DdFLKmfd8diMSmTT41v8AZHqmj7LNdh_eV8CPl0w7waxTGY09iCo8R4mzl-vDzEk8zGR-q5R3hxW-uzd6jBIGpJSyX0jx4T3Le6LWmwR9LmGzozuHhGEoP_GSy7j2-kOogKGeZn79r6GRuJcas5VL2J0y-CSUJK9kPrfEdwbUkik8SKsQumGEgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه اعلام کرد: حکم قائم حسینی معروف به آرین ، تبعه خارجی و از متهمان پرونده موسوم به «میدان علیخانی» اصفهان، اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21233" target="_blank">📅 10:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اکسیوس گزارش داد که ارتش آمریکا در اقدامی محرمانه، یک کریدور دریایی در مسیر ورود و خروج کشتی‌ها از تنگه هرمز ایجاد کرده است
تا روزانه میلیون‌ها بشکه نفت از این مسیر عبور کند؛ اقدامی که به گفته دو مقام آمریکایی، با وجود بن‌بست در جنگ، موفقیتی قابل توجه برای واشنگتن محسوب می‌شود.
بر اساس این گزارش، این عملیات طی چند هفته گذشته در جریان بوده و هر شب حدود ۱۵ تا ۲۰ نفتکش از طریق یک مسیر جنوبی در امتداد سواحل عمان وارد تنگه هرمز شده یا از آن خارج می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21232" target="_blank">📅 08:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTigAtWNVEIBuUDmIyL8KECt7DFU1QmoJPOxH_z97vX8Rjt2wsMDGpYIaA67vGYSKkV4wBSGxO-1QUzhEJ6e-3TEMj8m10QcLhabv18uOUmeND4w2IGA6vopgMMsH70BcE9PBVtDCe2LBZBoYAjwPfXPC-OEC987MKuHVwiKEsn9jihIHwREeX8876LYzWYWzvZJGiOUXl10naYQ1aAuJ8AvwzIvpCtQyPtjdLOQTXLjG0kcrQyqPVijhu7MrVRgFjlNXCWhQ9PsYF7WPvIH4MLbO6gMqtQK4EceqPxgjxmlSXrYJl2n7hmLuWrkRj0Vk2h8j9OggFRBMCBvkW9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : هیچ‌کس به‌اندازه من به جمهوری اسلامی ایران فرصت نداده است تا به یک توافق برسد. متأسفانه، آنها از این فرصت استفاده نکردند. بنابراین، امروز اعلام می‌کنم که
کمرشکن‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است
را آغاز خواهیم کرد! این عملیات، جنگ اقتصادی و انزوایی در مقیاسی بی‌سابقه خواهد بود. نیروی دریایی آنها از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان به ویرانه تبدیل شده و ارزش پولشان از بین رفته است؛ کشورشان نیز به تار مویی بند است. امروز همچنین اعلام می‌کنم که
هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هرگونه کمک حیاتی به ایران برسانند، خودش با پیامدهای اقتصادی بسیار سنگینی روبه‌رو خواهد شد.
قاچاق نفت، خطوط مبادله ارزی، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی —
همه اینها باید همین حالا متوقف شوند.
خودتان می‌دانید چه کسانی هستید. این یک
«روز دی اقتصادی»
خواهد بود و ما نیاز داریم همه متحدانمان در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند. این دیوانگان در آخرین نفس‌های خود هستند و این اقدامات تاریخی، آنها و توانایی‌شان برای گسترش تروریسم در سراسر جهان را فلج خواهد کرد.
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21231" target="_blank">📅 07:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بامداد نیک و خجسته ، پیج اینستاگرام رو برگرگردوندم ، خواب بودم
instagram.com/yashar
پیج دوم پشتیبان :
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21230" target="_blank">📅 07:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=V97PMqM_N3hosT91z7Tvxg30V8S3pCvnSF1JF38sl2Xw5K-koIqEnraxjJjAjCF_6l47VLsE2GrNiyvT7hSudqhO1LK-sw2Mf6nzPSVcTsGugDub2IsoEDKYxSsu7gppOovcEaqsRFdnft52xl6CCAx7wCv1EtUyI-9IxhR0SJkWtnDzRnBfa9vfv3PoyS4BWqGzk-GiV0z78knlQYH5CQqBSWdYv8ePFsbXfE_TsOAeinVld96llnaZguaKvsYK3rqFe3Ju_H_gYjEqutaktbsFc0gpI8s9xSpIdVv6qfYBKlUfI14sKYyO0PZCD3BPZKDHgelGKMTi4qXUUUt1C72TM25EJM0yEhWCFvce36p4WPOHRcX1C-3Cm-954pljWAoAo1s72Vi7ZTRie_MJpptb2d5U8QTmipAEZJ-hhT3fToGcF__ltyAj6wLDv4thXQu8RFzQdAvAu7iQF1itIpN-8P3pdJBHxrHZeKq0DwUdXVQjR6BcU8NSRtQ7S6Iet_LUKWb8rSFR9pSJXQ8wNeh-ZzCidZ9_Jkpj-FlTwp2x6hZWxSEUvi5cF4Cggu5Npp7rK9GIoyCTfPbx0pgvj_xGwyKdSOJ3SZ_t0S1XFZLDOdj3HyZlKP7tLp13iowJPvFaFpsvN8cegNwYY8Jyj7MPb9T4Hx1jU9R58nKvPJY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=V97PMqM_N3hosT91z7Tvxg30V8S3pCvnSF1JF38sl2Xw5K-koIqEnraxjJjAjCF_6l47VLsE2GrNiyvT7hSudqhO1LK-sw2Mf6nzPSVcTsGugDub2IsoEDKYxSsu7gppOovcEaqsRFdnft52xl6CCAx7wCv1EtUyI-9IxhR0SJkWtnDzRnBfa9vfv3PoyS4BWqGzk-GiV0z78knlQYH5CQqBSWdYv8ePFsbXfE_TsOAeinVld96llnaZguaKvsYK3rqFe3Ju_H_gYjEqutaktbsFc0gpI8s9xSpIdVv6qfYBKlUfI14sKYyO0PZCD3BPZKDHgelGKMTi4qXUUUt1C72TM25EJM0yEhWCFvce36p4WPOHRcX1C-3Cm-954pljWAoAo1s72Vi7ZTRie_MJpptb2d5U8QTmipAEZJ-hhT3fToGcF__ltyAj6wLDv4thXQu8RFzQdAvAu7iQF1itIpN-8P3pdJBHxrHZeKq0DwUdXVQjR6BcU8NSRtQ7S6Iet_LUKWb8rSFR9pSJXQ8wNeh-ZzCidZ9_Jkpj-FlTwp2x6hZWxSEUvi5cF4Cggu5Npp7rK9GIoyCTfPbx0pgvj_xGwyKdSOJ3SZ_t0S1XFZLDOdj3HyZlKP7tLp13iowJPvFaFpsvN8cegNwYY8Jyj7MPb9T4Hx1jU9R58nKvPJY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خونثانیاهو
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21229" target="_blank">📅 00:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fmi8c3Ztmg_n6JReiA63IOmfisCXWMDGa5Vt5x50h-00TbKktCrQmSxQAcehkULJ42HRP-gLpiOJfwFq0_J_1oCqJe56vs29J5roYjYJ8j2ktX6qxp9oEWVAeLP1YKuz_K4WPVS9q7M8QcD_SE8gP5EOicNZ1dnwDXELNQgGa__44X_LTWmBXqlLXr7xaVF9Yfz5AH0nv9J12J6VeotgJAPm64hDVEXAG8irYUxjYHubwHeWqhhOgT0ovHUL2-nCcvRH2S-Cyz6SgcHHWA_ty7cq1fg0s-zOtCxFeR2ye16d9Xhj_hP_D3ScgALjLLCgqBtT-muecT36MJnBcdULAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWxEVhqA6vh_WypCpd0OJaKtkUSu39QQRTVPvi_lOvJY4EVl4UDqA4FNGekopI3aghqA0gMU4ijhDukFIcfM4YBAMLlGchkkGki31_9WBa2UZCWzxIWeo1dBra5kK2J2aCr2NiXxmSt5Yk29AAERH88pjVyrgR-SDJuHhDYPjSJgkS2LGtjApe4b2QZC9nUzCl9NHnw40vZ-mCfwSGX5eaAWW-KgArIl0KXGIfL0dPfYHwyd6p7urLlsqkH8jv2IIVcSf1SbrBJSeutwhatZCj586HWWdzFe0s1zAeuDvjUcUlNewQzPFau96xTT8-iwC-EVf1zDwe2aFPOrO4he5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تویت جدید مم باقر که با سرش تنگه هرمز رو بسته نگه داشته
🤣
@WarRoom
یاشار : خودش داره میگه تنها راش اینه سرم بره</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21227" target="_blank">📅 23:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25637c93b.mp4?token=VHquAzpYVJDGsmnnsjm6PHSwv9vnkZiPYUNVo5eaDGgv4epbDBPT1V_aFxzcSSo-i9EMOwE_1OZSj5nFy5af60a2C1_BY3B2zgExOp6bVeVU7hnjjJjQQBy-XynTX2AedkLvM-30gMM42Vn8ZzpdtIbvdWdAY22O2BPN8SuXR8d3EHiVeTJOiDJUCxJUuQMofeglRZNQ0ANQGHKmomNChhOi3grOaL7bwVHmI1nPpliGjt1DkCfF07ydjZhBbodYOnv6snRMSiYVLx4jNDbU6W0c27leUi29d9n9IOovr4oUkpl2GudLVGp8X6lQLJ0KceE2nz-lbMjWHkzenvJ_fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25637c93b.mp4?token=VHquAzpYVJDGsmnnsjm6PHSwv9vnkZiPYUNVo5eaDGgv4epbDBPT1V_aFxzcSSo-i9EMOwE_1OZSj5nFy5af60a2C1_BY3B2zgExOp6bVeVU7hnjjJjQQBy-XynTX2AedkLvM-30gMM42Vn8ZzpdtIbvdWdAY22O2BPN8SuXR8d3EHiVeTJOiDJUCxJUuQMofeglRZNQ0ANQGHKmomNChhOi3grOaL7bwVHmI1nPpliGjt1DkCfF07ydjZhBbodYOnv6snRMSiYVLx4jNDbU6W0c27leUi29d9n9IOovr4oUkpl2GudLVGp8X6lQLJ0KceE2nz-lbMjWHkzenvJ_fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما چیزهایی داریم که می‌توانیم علیه ایران تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21226" target="_blank">📅 23:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0003edd740.mp4?token=UJRF42FwhLuh2_mRPQV2LUcUEa2E3gTQlWkvZ7TMfTllkGrKLumVkSkrVuFJMXgQdsD1zW-yZ1C9AQo2e_U1UGzKra1Fjwf-hK0I5qlBqwfs542DsjQXLr2OLW5nsbbKLlWMhntw7__y_C8npDfjQ96qSPMHCFvxqFndaHvT8KlV1utE-uMrKUEE-ECLsuE6tIm_WLzKl2sloSqYoZ_oUMKcvYTb7yTsVtz7i8MOZUx5zVk6mPdhLihF5MovQPfd2y_ZaGkqSCTYgiTz5cncAxOAecQR_AHjmv9Yp6pDap4a3pxf1wrSS68LF0gC2gmSwsoTCdY1eQzrH9LFT48ruw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0003edd740.mp4?token=UJRF42FwhLuh2_mRPQV2LUcUEa2E3gTQlWkvZ7TMfTllkGrKLumVkSkrVuFJMXgQdsD1zW-yZ1C9AQo2e_U1UGzKra1Fjwf-hK0I5qlBqwfs542DsjQXLr2OLW5nsbbKLlWMhntw7__y_C8npDfjQ96qSPMHCFvxqFndaHvT8KlV1utE-uMrKUEE-ECLsuE6tIm_WLzKl2sloSqYoZ_oUMKcvYTb7yTsVtz7i8MOZUx5zVk6mPdhLihF5MovQPfd2y_ZaGkqSCTYgiTz5cncAxOAecQR_AHjmv9Yp6pDap4a3pxf1wrSS68LF0gC2gmSwsoTCdY1eQzrH9LFT48ruw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
خطوط لوله زیادی در حال ساخت هستند. من فکر می‌کنم تنگه هرمز به اندازه گذشته مهم نخواهد بود.
در حال حاضر، تنگه باز است. قایق‌های زیادی از آن عبور می‌کنند. مردم این را گزارش نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21225" target="_blank">📅 23:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: در حال حاضر با ايران مذاکره نمی‌کنیم، زیرا مذاکره با آن‌ها اتلاف وقت است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21224" target="_blank">📅 23:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNnIYgZgxgCRpgLkxZ7XL7swn_yKOG_63mLAOLbVnluuWHXc8rBZ5N1tH8JGqxDKGnMOmk2P4ubvR01ne2St3i8wXmVnd63O-Rq7L_y1ayhDPLDhRXe-tdscza4XUGkZE51ZEym1mSzwDYV0O4bAWu-xSYZjK5iBwmvbuOYaxmiOgZUmB0UeHO1PWA8ti-4suynrzdrNSq9-1od3TDrDyH92B4UA0-cPPR7IuiwyH4syIMqo9AvlFMh-p-bgJYmVbQG4CX__R3qk7IIlbwwRtg8uxdqfRmRiIzivghjVg_zRMYVgFk_opa41tUj2JAUTdTIwkIZ-py1Tk0wKAD9iVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه نیلوفر شادمهری، رایزن فرهنگی جمهوری اسلامی را از این کشور اخراج کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21223" target="_blank">📅 22:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زلزله ۴.۲ ریشتری حوالی گیلانغرب در استان کرمانشاه را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21222" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانال 13 اسرائیل به نقل از یک منبع نظامی: آخرین چیزی که به آن نیاز داریم، یک جنگ تمام‌عیار با ترکیه است. ما از میدان‌های درگیری کافی در حال حاضر برخورداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21221" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو: ما توضیح دادیم که با حضور نظامی ترکیه در سوریه مخالفیم، و به نظر می‌رسد که آنها به خوبی به ما گوش ندادند، بنابراین تلاش کردیم تا آنها بهتر درک کنند.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21220" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ممرضا نقدی : ما باید به بازدارندگی دست پیدا کنیم. برای ما خوب نیست که کسی بتواند تصمیم بگیرد به ایران حمله کند، و سپس، در صورت شکست، عقب‌نشینی کند، خود را سازماندهی کند و شش ماه بعد دوباره بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21219" target="_blank">📅 20:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مارک لوین : من با ویکتور دیویس هنسون (مورخ، نویسنده و تحلیلگر سیاسی آمریکایی) موافقم؛ او در برنامه من در فاکس نیوز استدلال کرد که ما باید از تشکیل یک دولت در تبعید ایران با رهبری شاهزاده رضا پهلوی حمایت کنیم. و اگر رژیم ایران فروبپاشد، او می‌تواند در دوران گذار، به‌عنوان یک رهبر موقت ایفای نقش کند.
به مردم ایران سلاح بدهید!
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21218" target="_blank">📅 20:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رویترز: بریتانیا امروز ۷ فرد و نهاد جدید مرتبط با ایران را به فهرست تحریم‌های خود اضافه کرد. این تحریم‌ها در چارچوب تحریم‌های رژیم ایران اعمال شده
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21217" target="_blank">📅 20:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارتش اسرائیل: ما دیروز در منطقه ساحلی، یک فرمانده گردان و سه فرمانده گروه را از نیروهای نخبه در گردان بیت لاهیا وابسته به حماس به هلاکت رساندیم.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21216" target="_blank">📅 20:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ امروز در کاخ سفید با شماری از مدیران و چهره‌های بزرگ صنعت رمزارز دیدار می‌کند. در این نشست، مقررات جدید بازار کریپتو، قانون CLARITY و تعیین حدود اختیارات SEC و CFTC بررسی خواهد شد. رؤسای SEC و CFTC و مدیران شرکت‌هایی از جمله Coinbase و Ripple نیز در این نشست حضور خواهند داشت
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21215" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab2cd42e14.mp4?token=D9QJrXbs_dq6snmuuBAgcVN0EwcLCmR2LXXMvm_qZE9OMRJQ14a-eGLARdXihHzFuuFP5Cd3pE-XnrfRkJCvA0CAoPD8zHJae0Gy4LfHFA8Ba_WBDnBHtNjwqwrhLSfNsgAhfReBjD9KO6dhotTVdCrbPsmscja1Gbg55eXVfTLPorpGHxAbMqF-mFbDqSCdQeCPx_LE-tHYRtKb_0mYp1EyYJ80dLCQ2cDgSj4e7xkrSvZKraZELwpuoqlWArVkBYvsTLAKV0KwpJySNLjjKNUjm97mEXMLCZZ5Ou0wgdCMFw0OyhDnu3EHJLFO4l-bnjYHVGry84FedkaPxZGRkgHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab2cd42e14.mp4?token=D9QJrXbs_dq6snmuuBAgcVN0EwcLCmR2LXXMvm_qZE9OMRJQ14a-eGLARdXihHzFuuFP5Cd3pE-XnrfRkJCvA0CAoPD8zHJae0Gy4LfHFA8Ba_WBDnBHtNjwqwrhLSfNsgAhfReBjD9KO6dhotTVdCrbPsmscja1Gbg55eXVfTLPorpGHxAbMqF-mFbDqSCdQeCPx_LE-tHYRtKb_0mYp1EyYJ80dLCQ2cDgSj4e7xkrSvZKraZELwpuoqlWArVkBYvsTLAKV0KwpJySNLjjKNUjm97mEXMLCZZ5Ou0wgdCMFw0OyhDnu3EHJLFO4l-bnjYHVGry84FedkaPxZGRkgHcHH5EF35LOATnDFTPV9LbOPoimhSZPpAFeldj8DBYV5fwnha1f7BkXUzQB0b_wlmt7V0ubKi_CQhq_HKUlgTFJ9IGfknsX9hlOWIz9FOI5rqohwRup-eIIdeKaYciwHg3LPAqk71ZOc_XDaqg1fEgMn8Y9FzKbGJ2WQPyYQWj3p3NPNIOB0oyWUxjv_qF4SwccnsqUpdHw_5i1fvQfz7V8JvTy0Bn_R8iLC-tAu0p5qfxjKsw0Ti8qKDpEpgnfqf-vNcrYk42ecAbOQOkpbRhNrCeLcLCaOt9g_HmOgylB86zUaDqWwObVWYfI3Azo73WNUrVUx6p3gCwMAJhosY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : مردم دارند جایگزینی برای تنگه هرمز پیدا می‌کنند. می‌دانید جایگزین‌ها چیست: تگزاس، آلاسکا، لوئیزیانا.
مردم برای نفت دارند به آمریکا می‌آیند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21214" target="_blank">📅 19:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce66acfb3.mp4?token=Rcb942gW5roIYmOf-erCGiw6emms0_KK_aQTgwEkUUV3kqmZRV7wEQcnWmYrfvf_Ljh3o8ubOE4RZpFYG0t8dgQEhxtZrnV-cMhOjFKpnZm5whNN6JXtP6-Q-Y5SBLcLa_2WJ3lcJVtmS3ZY1AVoFS_C9OO7u_VJjH8I-hfQsXWw2WMJFV8zIY-0GvfJhfziZEUfGewvnwOySR98fBFNp66djw3IPlyyKk7kzzzx2l4Les1HJYsddqhmJzUOSWQ6I3QMm-jjPBA0NcfRLnhC5CSmr51sMJSz-CL50JFCH-C10ONPbxsf0ulxWX6qCvbWABCJ8i2D686rD3LGKlAI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce66acfb3.mp4?token=Rcb942gW5roIYmOf-erCGiw6emms0_KK_aQTgwEkUUV3kqmZRV7wEQcnWmYrfvf_Ljh3o8ubOE4RZpFYG0t8dgQEhxtZrnV-cMhOjFKpnZm5whNN6JXtP6-Q-Y5SBLcLa_2WJ3lcJVtmS3ZY1AVoFS_C9OO7u_VJjH8I-hfQsXWw2WMJFV8zIY-0GvfJhfziZEUfGewvnwOySR98fBFNp66djw3IPlyyKk7kzzzx2l4Les1HJYsddqhmJzUOSWQ6I3QMm-jjPBA0NcfRLnhC5CSmr51sMJSz-CL50JFCH-C10ONPbxsf0ulxWX6qCvbWABCJ8i2D686rD3LGKlAI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما تنگه هرمز را کاملاً در اختیار داریم و کنترل آن را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21213" target="_blank">📅 19:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون از آن استفاده خواهند کرد.
ما اجازه نمی‌دهیم از آن استفاده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21212" target="_blank">📅 19:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d548b77d.mp4?token=PKIjmU2bQRIv-6pK1LBsKsu7MXSYDfe2ejxNQHeaKacJIlqOpNVh8mwDVTETb6LgggyUv2AsNJqgajgPgekwDELzmQefjU6AEw0i-dIMaz_iLbRtdrqj56wAMG5TEzOmHYJxu6GtJqNCQxTcWsLACnbnuOuNdUMESwnxOt6eiICfvtZL34-4Z-HVjZBqweapPccV-oUJI3dfZSHUn5MQfVv7s3SD7swcWHCOVssAYboB4861-VG_pmJaE7vnS3Rfmw_H1EDBgUnnDG975FjQ3beomfl7oG5J_Bax430drf_diiTby_XAN1wRYWj1PJEzKxGW75H95SDTtwzOp-g_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d548b77d.mp4?token=PKIjmU2bQRIv-6pK1LBsKsu7MXSYDfe2ejxNQHeaKacJIlqOpNVh8mwDVTETb6LgggyUv2AsNJqgajgPgekwDELzmQefjU6AEw0i-dIMaz_iLbRtdrqj56wAMG5TEzOmHYJxu6GtJqNCQxTcWsLACnbnuOuNdUMESwnxOt6eiICfvtZL34-4Z-HVjZBqweapPccV-oUJI3dfZSHUn5MQfVv7s3SD7swcWHCOVssAYboB4861-VG_pmJaE7vnS3Rfmw_H1EDBgUnnDG975FjQ3beomfl7oG5J_Bax430drf_diiTby_XAN1wRYWj1PJEzKxGW75H95SDTtwzOp-g_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا شما دوباره با ایران مذاکره خواهید کرد؟
ترامپ: شاید در مقطعی، اما الان به همین حالت اوضاع خیلی خوب است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21211" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2b72a973.mp4?token=fels-pyjlQ9sVfDF9Sh4uBA581VMUfMVAxJvJMX5QJnV04dEOQsqaQw610bcDyaZZP2TbDfOvbFQVVdZuuos8yTHJjts2cvuqKNdkSsryRorfiwKbVtqL60ltSyh6wOK-z9yMk41TPXr9c-ixIdl6cYbTmm0h7tmMD8o7su_SD2VmOuSq592PvEtuKE21mMWfmLh2Ww2SHs8H9J0PwBx0PdRu7h20xW0h8rixoiTfhEp9y4waxjJTp8efQRiwlhAjQPKEG0qscGlA-K5TTmx8OSMIvj-rrlGlxi_h6AJBbMd2K_xaAqj4Qu879zPK_LDuQsH_4BnYeL6ZfxnnRP-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2b72a973.mp4?token=fels-pyjlQ9sVfDF9Sh4uBA581VMUfMVAxJvJMX5QJnV04dEOQsqaQw610bcDyaZZP2TbDfOvbFQVVdZuuos8yTHJjts2cvuqKNdkSsryRorfiwKbVtqL60ltSyh6wOK-z9yMk41TPXr9c-ixIdl6cYbTmm0h7tmMD8o7su_SD2VmOuSq592PvEtuKE21mMWfmLh2Ww2SHs8H9J0PwBx0PdRu7h20xW0h8rixoiTfhEp9y4waxjJTp8efQRiwlhAjQPKEG0qscGlA-K5TTmx8OSMIvj-rrlGlxi_h6AJBbMd2K_xaAqj4Qu879zPK_LDuQsH_4BnYeL6ZfxnnRP-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
قرار نیست کارمان بی‌نقص باشد، اما نفت زیادی از آن خارج می‌شود، خیلی زیاد.
مردم شگفت‌زده هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21210" target="_blank">📅 19:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca74a36348.mp4?token=oApoYSR3jsVa-M8hLHPJH7kdylhilKZiEC2xyvozMpmtxw4q_bDiZ6G75Q_uXijD-ncHGtJ7uWMV9qY7m4IRIdyvn0bMwtpq6mfm5iuGNHjNRCa7C9UMd0QXeRT4TFXF0C1Gb2NduUiklt-HqnNjNulO7dChNzX2vWqpSmtYtVq5YBiHpcfiGNoy7FzLva3KD2TSRaAMv2qoagP3JelHw5JR4IMoa7dGYk_q-A6oX6pW3PZQTBSjf378_GJpcFxxPPlfIzcbyba0jlxNXon8pY0ciP_qxuU1yWsy30i480cwxNqQ6CEuIvGF4eOtcn1f-GQj7FEv5Plw8Zhtz-6lDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca74a36348.mp4?token=oApoYSR3jsVa-M8hLHPJH7kdylhilKZiEC2xyvozMpmtxw4q_bDiZ6G75Q_uXijD-ncHGtJ7uWMV9qY7m4IRIdyvn0bMwtpq6mfm5iuGNHjNRCa7C9UMd0QXeRT4TFXF0C1Gb2NduUiklt-HqnNjNulO7dChNzX2vWqpSmtYtVq5YBiHpcfiGNoy7FzLva3KD2TSRaAMv2qoagP3JelHw5JR4IMoa7dGYk_q-A6oX6pW3PZQTBSjf378_GJpcFxxPPlfIzcbyba0jlxNXon8pY0ciP_qxuU1yWsy30i480cwxNqQ6CEuIvGF4eOtcn1f-GQj7FEv5Plw8Zhtz-6lDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد کیم جونگ اون:
این واقعیت که من با کیم جونگ اون خوب کنار می‌آیم چیز خوبی است.او ۵۷ سلاح هسته‌ای بسیار قدرتمند دارد. هرگز نباید اجازه می‌داد این اتفاق بیفتد، اما او آنها را دارد.من با او خیلی خوب کنار می‌آییم. من کیم جونگ اون را خیلی خوب می‌شناسم. او خوب خواهد بود.تا زمانی که یک رئیس جمهور باهوش داشته باشیم، او خوب خواهد بود. اگر یک رئیس جمهور احمق داشته باشیم، احتمالاً او خوب نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21209" target="_blank">📅 19:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پولیتیکو : ایران و آمریکا وارد فاز صبر و انتظار شده‌اند؛ هر یک منتظرند تاب‌آوری دیگری زودتر تمام شود
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21208" target="_blank">📅 17:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ60R3-f1VL1AZ4wqEaydQw5hEfBiRhug_bSPBDA2bh4cpWK_uK-DiXXmwlrpknC4USwA1z9698E95F6pA31NoeHxs95koAgjyWk9BuXnLxoPz6U6CHcNxA1ML95bJ508raPRYyEHUjPxalmdVeDv7OBfUnLeDPjD-nEMaAEZcYapQANS5g8MghKj8Y320LwBhVLuT6Sqxf94MXkxU37z8pw597ZYK1jWEsCtwd_fMz0C4euu1kYvsvnP5dzsRDGxwv73NAEQ1oUERLkN6cNnMpfQUQReNVJoh-nqpvFo-HSdCx5ZsC8LGm93QUhW4C5PN0SnZa9RtaFzwpvrPOD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: یک فروند جنگ الکترونیک EA-18G Growler نیروی دریایی آمریکا، هنگام انجام گشت‌زنی بر فراز خاورمیانه، از یک فروند KC-135 Stratotanker نیروی هوایی آمریکا سوخت‌گیری می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21207" target="_blank">📅 16:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مرندی مشاور تیم مذاکره کننده : دیروز، کاخ سفید گفت که مذاکراتِ وجود نداشته با ایران را «به حالت تعلیق درآورده» است؛ ظاهراً با این هدف که فشار اقتصادی را افزایش دهد. اما چیزی که کاخ سفید نمی‌گوید این است که آن‌ها تا همین امروز همچنان در حال ارسال پیام به تهران هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21206" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک مقام ناتو در واکنش به گزارش‌ها درباره احتمال تهدید اهداف آمریکایی در اروپا از سوی ایران گفت:
ناتو آماده مقابله با هرگونه تهدید علیه کشورهای عضو است و برای دفاع از همه متحدان خود هر اقدام لازم را انجام خواهد داد.
این مقام تأکید کرد که وضعیت بازدارندگی و دفاعی ناتو «قوی و مؤثر» است و یادآوری کرد که سامانه‌های پدافند هوایی ناتو پیش‌تر نیز موشک‌های بالستیک شلیک‌شده از ایران به سمت ترکیه را در چهار مورد رهگیری کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21205" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ناو هواپیمابر یواس‌اس جورج واشنگتن به عنوان بخشی از عملیات خود در منطقه عملیاتی ناوگان هفتم ایالات متحده، از تنگه سنگاپور و تنگه مالاکا عبور می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21204" target="_blank">📅 14:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وال استریت ژورنال: مقام‌های عرب می‌گویند ما «بین ایران و آمریکا گیر افتاده‌ایم»
آن‌ها معتقدند جمهوری اسلامی در نهایت به افزایش فشار اقتصادی، واکنش نظامی نشان خواهد داد، در نتیجه، جنگ دوباره می‌تواند شدت بگیرد
حملات اخیر جمهوری اسلامی در تنگه هرمز، روشی را که برای حفظ صادرات و تولید نفت به کار گرفته شده ، تهدید می‌کند , در این روش که «سفرهای شاتل» نامیده می‌شود، نفت خام و فرآورده‌های نفتی از داخل خلیج فارس به کشتی‌هایی منتقل می‌شوند که در خارج از منطقه منتظر هستند تا محموله را به بازارهای جهانی منتقل کنند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21203" target="_blank">📅 14:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش اسرائیل : ما در چارچوب خنثی کردن شبکه تونل‌های سازمان‌های تروریستی، دو تونل زیرزمینی حماس در شرق خط زرد در نوار غزه را مسدود کردیم که در مجموع بیش از دو کیلومتر طول داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21202" target="_blank">📅 12:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47b2eca4.mp4?token=iyQxSi5b6lz3xLXP3mdrMvdpBjxh5SsHzPV-G0RKZ9YKxwnCYWSOuz3TJO2E24II219JCTpoabx8AAAwoUEO0ozWXpJL2cHQ4oaINECTObrFXBA6G7Ni_SKsuuFi1SnOQ4Xi5g9tzhsrH8OuAHI_U465wg3ZFA7wBuvRwCJ4Vo8geTbYNW6oBu8SJ1Fu4vQKFrpXaC89ZAhePe811ifXar140E0d-Lm7oI4C55NyXzmWmUpdliwLP4WwRAmxoG503gqs1BkD0wCAzXVlSdXixxTyTpAEwxug9dHbY5UgJvs8cI-dw9uYKDxT2LuiipqZi6hZrXhWcgqjuy81-z55KYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47b2eca4.mp4?token=iyQxSi5b6lz3xLXP3mdrMvdpBjxh5SsHzPV-G0RKZ9YKxwnCYWSOuz3TJO2E24II219JCTpoabx8AAAwoUEO0ozWXpJL2cHQ4oaINECTObrFXBA6G7Ni_SKsuuFi1SnOQ4Xi5g9tzhsrH8OuAHI_U465wg3ZFA7wBuvRwCJ4Vo8geTbYNW6oBu8SJ1Fu4vQKFrpXaC89ZAhePe811ifXar140E0d-Lm7oI4C55NyXzmWmUpdliwLP4WwRAmxoG503gqs1BkD0wCAzXVlSdXixxTyTpAEwxug9dHbY5UgJvs8cI-dw9uYKDxT2LuiipqZi6hZrXhWcgqjuy81-z55KYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممباقر در عراق…
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21201" target="_blank">📅 11:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سی‌ان‌ان: ایران بخش قابل‌توجهی از کنترل خود بر تنگه هرمز را از دست داده است.
بر اساس داده‌های شرکت کپلر، در دو هفته گذشته
بیش از ۸۰ درصد کشتی‌های عبوری از مسیر تحت نظارت عمان
در بخش جنوبی تنگه عبور کرده‌اند؛ مسیری که ایران با آن مخالف است. برخی کشتی‌ها نیز با وجود تهدیدهای ایران، با اتکا به حضور نیروی دریایی آمریکا از این مسیر عبور کرده‌اند. یک تحلیلگر کپلر گفته است که به نظر می‌رسد ایران
دست‌کم بخشی از کنترل تنگه را از دست داده است
؛ هرچند ایران همچنان با تهدید حمله و ایجاد بازدارندگی، توان تأثیرگذاری بر رفت‌وآمد دریایی را حفظ کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21200" target="_blank">📅 11:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الجزیره : این ترامپ نیست که مانع عبور کشتی‌ها از تنگه هرمز می‌شود، بلکه شرکت‌های بیمه این کار را می کنند
تا زمانی که تهدید فیزیکی علیه تردد دریایی وجود داشته باشد، این شرکت‌ها از قدرت مالی خود برای جلوگیری از عبور کشتی‌ها استفاده خواهند کرد
بدون تضمین‌های قاطع مبنی بر اینکه کشتی‌ها از حملات ایران در امان خواهند بود، مالکان حاضر نمی‌شوند که در تنگه تردد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21199" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اورشلیم پست: تام باراک، نماینده ویژه آمریکا، هشدار داد که حمله اسرائیل به پایگاه هوایی ابو الظهور در نزدیکی ادلب در سوریه، می‌توانست منجر به تشدید تنش‌ها و یک رویارویی نظامی مستقیم، احتمالاً با ترکیه، شود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21198" target="_blank">📅 10:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21197">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رویترز : آمریکا برای
بازسازی ذخایر تسلیحاتی و افزایش توان تولید مهمات
، بودجه‌ای بیش از یک تریلیون دلار پیشنهاد کرده است. پنتاگون قراردادهای تسلیحاتی را از پنج‌ساله به
هفت‌ساله
افزایش می‌دهد تا شرکت‌های دفاعی با اطمینان بیشتری کارخانه‌ها و ظرفیت تولید خود را گسترش دهند. هدف، افزایش شدید تولید
موشک‌های رهگیر پاتریوت و THAAD
و جبران ذخایری است که در جنگ ایران و دیگر درگیری‌ها کاهش یافته‌اند. همزمان، آمریکا تولید موشک‌های کروز را نیز افزایش می‌دهد؛ از جمله قرارداد
۲۲.۹ میلیارد دلاری هفت‌ساله با ریتیان برای افزایش تولید تام‌هاوک از حدود ۶۰ فروند به بیش از هزار فروند در سال
.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21197" target="_blank">📅 10:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21196">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فایننشال تایمز: ایران در صورت تشدید جنگ از سوی ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی می‌کند.
به گفته دو منبع نزدیک به حکومت ایران، نیروهای ایرانی گزینه حمله به دارایی‌های نظامی آمریکا در
بلغارستان و قبرس
را بررسی کرده‌اند. همچنین حمله به
کابل‌های فیبر نوری زیردریایی در تنگه هرمز
نیز از گزینه‌های مورد بررسی است. این منابع هشدار داده‌اند که در صورت حمله آمریکا به زیرساخت‌های ایران، تهران ممکن است دامنه درگیری را فراتر از خاورمیانه گسترش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21196" target="_blank">📅 10:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21195">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEQa6sY4KjZXqcOWUNH2ua7TGXBCqNXQta1PK77yiY0Qk1mVGRt3T11KbaxRC2FFpxgJVHnCW-YvadzvoZ3mp9S7gvsMG0jAz3d0WegqDzVL-_N-er4spoCXgz95ACk3tWHwC1kIp6S4Q4jYI2lMsuSWFdQDZD_MpB7nTQCJ_CSqyyjvP4RV2_vBQ091-U2lxK4WJZs35BmlwoqD6reFZSVeUpjK5d8uNeWiMhQgvNNkrTzSfAoB2V83VRILr9wFdsd9_bOq3ylEywjJp8xD84io-dZpn9CU8S-f7g0bQ7YAkZkNfqPbGyv-K_P0T_52T7RTM6FM0BOttksrL9VTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا سقف ۱۰ میلیون دلار پاداش برای اطلاعات درباره هکرهای ایرانی
بهزاد مصری , کیوان فیاض ، مجتبی غاله‌کوهی ، آرمان کهزادیان ، صابر شهبازی
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21195" target="_blank">📅 10:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21194">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک مقام ارشد وزارت خارجه آمریکا می‌گوید:
«اهرم‌های متعددی وجود دارد که رئیس‌جمهور می‌تواند در هفته‌ها و ماه‌های آینده، در صورت انتخاب این مسیر از سوی ایران، فشار آن‌ها را افزایش دهد.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21194" target="_blank">📅 10:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21193">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21193" target="_blank">📅 03:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21192">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21192" target="_blank">📅 02:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21191">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21191" target="_blank">📅 02:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21190">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21190" target="_blank">📅 02:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21189">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21189" target="_blank">📅 01:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21188">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21188" target="_blank">📅 01:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21187">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الجزیره : ترامپ به تیم خود دستور داده تا زمانی که ایران آماده امضای توافق نیست، با این کشور دیگر مذاکره نکنند @WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/21187" target="_blank">📅 00:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21186">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینترنت</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21186" target="_blank">📅 00:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21185">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرنگار شبکه ۱۲ اسرائیل:
نتانیاهو با یک رویکرد برنامه‌ریزی‌شده، در حال آماده‌سازی جنگ آینده علیه ترکیه است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21185" target="_blank">📅 00:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21184">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ در فاکس‌نیوز هشدار داد که اگر عمان مانع منافع آمریکا شود، این کشور را بمباران خواهد کرد @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21184" target="_blank">📅 00:02 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
