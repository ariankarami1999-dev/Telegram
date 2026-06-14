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
<img src="https://cdn4.telesco.pe/file/ZrXuPUqlNrc0vh43nv6XWRLjb3nlEoLniLr96zNXgYPtBnJ3gyEWIxVrk1WGopuJLjDaEv2_l2JxUCqQqHUU4z3ukiUC2_xA2x3lO_6xPWRwuS72GJRqTQqL06vgJuXggT5i92JxraNI7LIZcoNWtrVpIV7OsiWJh-38rbDYXOHSuH-Ajmjol2N7KsKDoEniOxTyyxKXYaooz6SWWgaqmfHuVuoHp93voWwzgLglpNWz3bWXu-jYlPBVjaNfyL8TfxCopDqG2QaHZk__Sa81ee5RzxXZaPqs4Tb81UcAEPQFL_CC9_gN_e3BH0FS10LG3Q00_UucsWg08j0YKDNhOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 00:14:42</div>
<hr>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4mVibPBw0eTr1gRTGNQb3XRCfny3Oz-uh82TwTsV3xvMGClyO5fmI6shvbZpKO3XEey5XidRloasQiHdbrALRSFQZAnisgoaRceVWlI4CTKNGoB00Ghe5CNX0baKLelkuhdT_iQQYC6R1cKSkDT-QdKb7xG2HyJeYdTcbpNYQfJF62EvT2qREMpgg72uID-BgYQXRuufpMUEYKXaIsoR98w56qi5eDOPV31uMsOMUmdiiJb3ba9oX6hVb9z63MOK-DUDfFC5X88bAtLXs62907JLlWfcpIy_lhoy1aIlLLZEMtLoo-fdn5qg5ppozUDL6y7ocXanJeMU1m4OJcOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-BzrRHeVQ2UMm9WuY2JtXe5_pV9kg1-2rfhdVquGkw9j4gBVXeCkCYZX9ziQVOvFIRyqp8V1y-tWNRHg1ZT3Qi4YSYoGJg9u_mfGwmYRfXI8GPV46QIGw8lIB6L0TVCJ5w2H7L3rSzMGrExDF_-AcQ3xu_A4nWAQvLNnT_XWD46MObcGK0sMN92FPYG41BH19LRgq4YK7iFXK1hFIQst-2BPIqEap-5D50stkDm2Uu8sIsONpqrr3W5D0TeMYCmBz-im5D8ZfEcn0oY_RxM17mfofIocWayViApPRhL2dO9OPVKKn_ZeXKtZkpT4ulXU4d7I8BhGiAA1sBFivemXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcTQKFWjSocS4SiURLk0QU8VKDJbJ3ZvZtIoL1Zdd7eIdtMnINUgw_suDMlRPq4xhGD6J0PnZxqPoF66wOX4C7WEz7hxwOOClopXQsFYYRzQ0iSzd5ABJrz437HPxBx0YWK0hyDfctCvoXwczBiCZzg44nk6rzxYvTAjNM2AsjA1-Gu_tKcPl-ZJbe9q7JOx3vxoA0dF-I65tgvlGG5qEwDNrXnq6GzmjAM46MEgTuG-sFna2fqwyqIHoaSs1ui2EUXCQTR0oDJ54xGuHn6N3KV6NA2eOQm9L9KpxbkaOOEH4_SwYp1Oq8c-x-6GbqfdkzYgSTAkeGhAnpkk7K8MYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M03B7noW6qpfJyjjTW-RS8nZ6WmvQ946LYKNhoR89xFn8Pioz_m_X40n1XPxopGpcFsgNQX175DEJGJ4j2KU0SeyZ5h7xF_bx8uFFXuOX8jj1ZxQkWABP-WtxtoHjpyJNGAQkekDxOnGPAH1Dc4nsWeQNjC7piquw7uP4VkEoNkJj_vdCVhb5jME70-wLWtILzqnDgZvFCqL8j1DaVojrX-LtGBO8_AJ5E04m28SdEptNzefVeiUfOPIakWAed0UayHGisY8nw44lJvykCkczegOQWAp3xKgNwwqEVajXHvLYzDQcYdimzSqiKalqFAgY8VkfN1i5b3fRIsnDuIILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOn4FVtZPOksup3-ez1BI-nJRPNbncnyMtzk_w2mxk2zdrfkjyvjCYVakTgR3emLPgN94hYGWl0OR5dM7sJ46NkZAX5kOaamDdM9R5PQY_JBtqabf-degEFgvTp3kg2LRSgTSwkXJPTe_j1yqmGYhsEe86vER959rrWNbTHY8tGvl2Fu6MrhbNilanJOY5-gkPKs9gKE8q4wyHVwu6zpp6XDj-M24_iZ0NMCp0tCZjCm-bgvrGTx5ibw5XBlbuWLz98gCFip2GNMX056rBbnst2HqkPadUl8O3Tzwz-D7U3B8zMXQ-o7KhWI3f0vmWKV6NvSk3Of-Kn0CMfr2vCY9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMNMVmk5kk9580hCIUT_or_h0VtIQFJr_H49C2h0nZxUAYhiGraBg9eADo67OEtSclphit2yRxIRU41bQLssY3MxUrfsgg_s8CoDxRw_nBDBQNrQq_LJo_w1ZnOTadeH7DjlkQQLsrXgz-2UymRQ4DEuZf1Xq9RjWMwfS4AR2EaLsUY7iSJHzaWbkL5Oqbbxh-U6S2FMIebSKsMYef8S8lBePHLjPeU1ijhJryZvDtYGsbRChtndunFCOdO46pNYNjx03fUPnOlybq84nH93YJaezeaRjLuzWka9sxTYXjjml3Xx2iPn1HcUgPQVaKsP0xkCQGKTagpN4Kvp8u3TiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCih9Wib4QqmE-nmlaYMaTAww_1_BKpyJYTVv2ZOMd-hrWF-Vp44dbm9FbzDE9N4HtLIm5Ub1jnCNU4X5D1fHdGmw05wH6Dr2vU3CObOS4VpKgmktmRRGIpaV1PlGOgUTuovF6m78HtxKYgvobyT-yj91baQgxlHG6Ipd6qnnqWyqyM30J82m1cc1RLEPag1GodvEYB6jsqQF21Y8lUllGZz7SLtKkzRt-pTpAXbv90MDW_tzZIUSG4TiIkY6j118Li1QiqjEj4v-2pSQpsjmiOuB_MZG4JxeKK35Uk09rehQc54HMbegpsgIqf6zDnajP2DQ1gq6toc7KwLss85OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=pQo1-GOe1snUtoy_Aq_ljtI_nchtHDugG2naDUkl9RVBQ3hQ-b3d8IqDzX1CJ6xXm6qVnrU1XGc_MCW9hxMeDxTAnv2kbmSUlECoAB9glr8q1KUM3wR0W_7EM-2_FcwPLLojfz31R4aO8tMWb2GgNrA7xfCagrifwNc3cfM-gqdFD9_59kly605190pXeTQUQkDmz9Kn3aNo39nipA7L8ycYoLnIB_q35rF80pO7xsR8nsuaTK_2v_froEr4eln-_fNnR-NOAE1n1TJNbZ9bJZTm5Wmud35-RNmuvjQTh1w8EUQ7EqMncZQBjkkmmm8Aaia3xXYRSGW2a7bD5jFoRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=pQo1-GOe1snUtoy_Aq_ljtI_nchtHDugG2naDUkl9RVBQ3hQ-b3d8IqDzX1CJ6xXm6qVnrU1XGc_MCW9hxMeDxTAnv2kbmSUlECoAB9glr8q1KUM3wR0W_7EM-2_FcwPLLojfz31R4aO8tMWb2GgNrA7xfCagrifwNc3cfM-gqdFD9_59kly605190pXeTQUQkDmz9Kn3aNo39nipA7L8ycYoLnIB_q35rF80pO7xsR8nsuaTK_2v_froEr4eln-_fNnR-NOAE1n1TJNbZ9bJZTm5Wmud35-RNmuvjQTh1w8EUQ7EqMncZQBjkkmmm8Aaia3xXYRSGW2a7bD5jFoRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=EUs3O-rcTBxN1b6Ro-k8V1OqRxa6_ArXvwScd-uOTNGRZMkGDIWfIUIHznB3h_stfVZQGwf1_qKxLT_MUTwKy0-KOjvg34mezm4rRgSJrZnsxv_HE3s7-K7FF2dDW4BR67q3diDjrBgeC61Xv7V1eiiqUXaqRj8KwmHSdtXethZYTCwBjFlCPt7yOU7BAFrh4cgzdMt2kdA6YKFlHjAn4zZQezx6alg5-6fUxUiJAUnrIRJRY_md0J98fMAnRoGT1iMIonhFx-FMmh5a01p8wzsYBeu1DnRqX0-rd1lgSjiY2T5ZyFUqTdnSPFBKGYma9wrYJJNqcxYglgB9Prtn3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=EUs3O-rcTBxN1b6Ro-k8V1OqRxa6_ArXvwScd-uOTNGRZMkGDIWfIUIHznB3h_stfVZQGwf1_qKxLT_MUTwKy0-KOjvg34mezm4rRgSJrZnsxv_HE3s7-K7FF2dDW4BR67q3diDjrBgeC61Xv7V1eiiqUXaqRj8KwmHSdtXethZYTCwBjFlCPt7yOU7BAFrh4cgzdMt2kdA6YKFlHjAn4zZQezx6alg5-6fUxUiJAUnrIRJRY_md0J98fMAnRoGT1iMIonhFx-FMmh5a01p8wzsYBeu1DnRqX0-rd1lgSjiY2T5ZyFUqTdnSPFBKGYma9wrYJJNqcxYglgB9Prtn3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=eAysldjlsqceRApPskBWBUvGYuLqnczF-RICTMtWLrqLhEQjz4a9Ua5KnKsg0sl2ce3SAYtt0OXZKgH9jBr8jTb7Iy5pTcqcdPkVotL4W5cDLpg64n2brMwD_8AjdzB_UkN6LqcwRuCabDkx8IbHJuwR2e612_mV-E0XRLYrIcETtJKCTTScgfrqbgv2shdZ8Kz5ydCCiv0L4NxrlSp4ajkUfJbjX5qGuEddq_9ga17xvcAl2j5tjtE3WItRplqbdM45RoW3039sZktlxJP7ZG-6D3RMGIFnl-9VWjdIbRcuQTyt0Eq328RpJRVsps621xXAe9diDLFRrJ0v633OsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=eAysldjlsqceRApPskBWBUvGYuLqnczF-RICTMtWLrqLhEQjz4a9Ua5KnKsg0sl2ce3SAYtt0OXZKgH9jBr8jTb7Iy5pTcqcdPkVotL4W5cDLpg64n2brMwD_8AjdzB_UkN6LqcwRuCabDkx8IbHJuwR2e612_mV-E0XRLYrIcETtJKCTTScgfrqbgv2shdZ8Kz5ydCCiv0L4NxrlSp4ajkUfJbjX5qGuEddq_9ga17xvcAl2j5tjtE3WItRplqbdM45RoW3039sZktlxJP7ZG-6D3RMGIFnl-9VWjdIbRcuQTyt0Eq328RpJRVsps621xXAe9diDLFRrJ0v633OsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ncXGbYG5jnvquXnzH_EVjiQdu0sAGnBV7PsEbOFGkK4ufRIn2-xK7ji44X3zv1S0TeGpm44gTFZ--HBlImOSIjHN0iVksRcOovMVBCr09FZgVRJlSB84DvBAlc0hebmP0I5BQJuBx2V4kOTa_DI8_bd74sOOm6Ug1nbShEWrhpQ9YHQxn8WjdQaw5ej2SVLIda8y1ZcqoBHH9x_q-2-R40yqkoqnKgWFQqohoLKIyMo_yhjnneOC0hMjl50ZLyXt_rm7vfQ0tXuJGDEYeIStmufzkz12cevN1fvTLnSLRGWHeHa29qLzd4Gbm6gVdijAHqJ4uirLokRslmbjVlsSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ncXGbYG5jnvquXnzH_EVjiQdu0sAGnBV7PsEbOFGkK4ufRIn2-xK7ji44X3zv1S0TeGpm44gTFZ--HBlImOSIjHN0iVksRcOovMVBCr09FZgVRJlSB84DvBAlc0hebmP0I5BQJuBx2V4kOTa_DI8_bd74sOOm6Ug1nbShEWrhpQ9YHQxn8WjdQaw5ej2SVLIda8y1ZcqoBHH9x_q-2-R40yqkoqnKgWFQqohoLKIyMo_yhjnneOC0hMjl50ZLyXt_rm7vfQ0tXuJGDEYeIStmufzkz12cevN1fvTLnSLRGWHeHa29qLzd4Gbm6gVdijAHqJ4uirLokRslmbjVlsSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=He85OZZysVkYkjQ5ck07q1Yqpz85YdkTOB067hHEIOnBAgis2CcAvxxSjuJhst0bbuJCm76gDQK6A59_l0Hn8Nrq1xatkfnp7MK725bYi4apVbLm3kpUXdNIfVSffLX3b_QQqXOk-no3ikYn9bHTRt4cc4nvVLFEyjfid0YbKEFa6P7yofbpMNawkJKscEg_dqfoMqrxkf2zxhu8zmdvTK9tu0b9fRCjftBhQYTCzX8vV27rly6UfUb1NrWuEpA8m3fKDGKnaWVdJ9Uf1f5a82Sljr6_VUNYLcsc2ezhbBQ43dtJapSsAoT_decvbUU4kL5eDvEYg9RGGNghYEL3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=He85OZZysVkYkjQ5ck07q1Yqpz85YdkTOB067hHEIOnBAgis2CcAvxxSjuJhst0bbuJCm76gDQK6A59_l0Hn8Nrq1xatkfnp7MK725bYi4apVbLm3kpUXdNIfVSffLX3b_QQqXOk-no3ikYn9bHTRt4cc4nvVLFEyjfid0YbKEFa6P7yofbpMNawkJKscEg_dqfoMqrxkf2zxhu8zmdvTK9tu0b9fRCjftBhQYTCzX8vV27rly6UfUb1NrWuEpA8m3fKDGKnaWVdJ9Uf1f5a82Sljr6_VUNYLcsc2ezhbBQ43dtJapSsAoT_decvbUU4kL5eDvEYg9RGGNghYEL3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9yL2KuH9bMZ_Cq6R6kQ14U_5KNeRGlstcU7lnqJTxv2TjtnboeANFL53eza4u56G9b_IqyammmLwyu-XUns5g0DzItI0RfgRUeS4EmT-TT-K5MZfBZ8m0PUqCjS5GPm8DdfwPfdgPICrJ5O4a0ltms7XWGhtJxdN3ITT4r7oCPNnkAqkOd-F3FhDLx1gZtmtczsbsr3pEjHrN7pcrwy2mk0EA1YFU0ExmxZwTGIziH9_BeVxm1_XGI7sLM97i9A8RQAPTdENkX1IWHt7W7iz9VVcdBqJIL2-shKlMqKR5fXMQ4Ua1PsVsZW3RA8a3v1hwCxXf36AcEBCvi2u46LZTAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9yL2KuH9bMZ_Cq6R6kQ14U_5KNeRGlstcU7lnqJTxv2TjtnboeANFL53eza4u56G9b_IqyammmLwyu-XUns5g0DzItI0RfgRUeS4EmT-TT-K5MZfBZ8m0PUqCjS5GPm8DdfwPfdgPICrJ5O4a0ltms7XWGhtJxdN3ITT4r7oCPNnkAqkOd-F3FhDLx1gZtmtczsbsr3pEjHrN7pcrwy2mk0EA1YFU0ExmxZwTGIziH9_BeVxm1_XGI7sLM97i9A8RQAPTdENkX1IWHt7W7iz9VVcdBqJIL2-shKlMqKR5fXMQ4Ua1PsVsZW3RA8a3v1hwCxXf36AcEBCvi2u46LZTAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1CiZn9clndjWb9WOtTUbFUAvOT4sIvoMgCZMBhb7NT72BBj0mmDkRi2ieERLteLquysldqws6KbkV7igve63GAPaUB65Ttk1yqUCtEvYGgaMs59RGOCDcZTIIXwzfoVsGzG-5a41aCKosClH4zLuVgt1b5oMXhvIBupXeYm-uvXIo434nfpkpfwHZ5nq0OZXWBLVQVtlK4AxFvFmrCd1lmXaU9a6dmr_3xtSn1sX5i_VL0Caz64z7fi9W1IN6eyoBaeJ0lpkdqo4u1eNwiJJXbfSp5w1qeGhTM87ScP3WPSZyStUK3LQdgvA5anTMA1rEpbjqMPGxBO1-5yR-p3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=CQAVgiT4URJFtRo7mVMn1n8DJ1TQm2b_TVufF33JkO1xh2i7JT-3R6tJ7zT5ChRZsW7XRbZ1u9-yNuHLt8IEdLjhlDxx0dLr_OaQ-wJdKgLTIIX6qDeoQOvLbS0PqG4RtCI4LmYMevRPGeGcjH7C77O74FNe6FQVDqMT01U8lm2J2ZYpVjwsSAB52o4AtHhss33vRSBZoWjiLmyH53907ZnA55UOINcoRbivxtJM4qDAo28bH5q7KIpmV1dftGAu1cTvb0x7-oBBzC-FAFet8MouBB5xswgWeL4NJOYZ-qzbxBj_ZgjEXLNPSzDYJfHmZMTbesoL7Um2ZfxIszuVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=CQAVgiT4URJFtRo7mVMn1n8DJ1TQm2b_TVufF33JkO1xh2i7JT-3R6tJ7zT5ChRZsW7XRbZ1u9-yNuHLt8IEdLjhlDxx0dLr_OaQ-wJdKgLTIIX6qDeoQOvLbS0PqG4RtCI4LmYMevRPGeGcjH7C77O74FNe6FQVDqMT01U8lm2J2ZYpVjwsSAB52o4AtHhss33vRSBZoWjiLmyH53907ZnA55UOINcoRbivxtJM4qDAo28bH5q7KIpmV1dftGAu1cTvb0x7-oBBzC-FAFet8MouBB5xswgWeL4NJOYZ-qzbxBj_ZgjEXLNPSzDYJfHmZMTbesoL7Um2ZfxIszuVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSFbb3dfi5m6VppYUvOA1ZJoVWG4WAEAjUcjAa3ZZ8tN_kzppFNtbhHyhgVcSUm-4dDwyKBBIy28vBjpSGxRKhhqd5RNTepPn1yQppufcd7grwrX-Z2wOE3FgCMgd6F4Uh5g4oG02fu8x8rfh-CGMNI25AR33tI0QoBVmMPLSF_TEmogMHzyw8uKopXqtU8ZfxvXpjiGPzXuzm1dDfOlwtAFggVEDU0JqwZhxKlQLRVP9_OyHnF0zlAmlkvE5EVpCErzzZEYElYma4c9x-IR0JWB5R2z4tnBJOpCztwLaGfZ2mOSiUKFodr7ggaVBgqmiWEVYSnZ9zRcdqKXOVow-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3On4CliEzMDco_oI-tghFhubnwpSWZbL-OcmLuW5mkK7Z4ACE3gCUUVY_8AVDAIw1T6vI4TsJv82NNUKIjDpG0Q-d2IhP2n9iL2_FwAD1WM51VaKkBifzy-uMU_H0rshddk-_d0MuLxnMPCaeDXxQ_gz5aIrIiE87D2rBe1JNW9YXyZr3k9eP8yFRIiQH5vwYFLMrPHlsu0bttXjp_FcU2Fuamd4NRpEyt7QwRDUE6my79PJ5NQOVNb4kk8Mham5fKnV5VW-4AaPmg6pEwAOTm64Sr6URB-_tuWd6_LsIIvjkmq_a1oOPdhgqK2Ka-7YXfjzsAHIqK7JbWfJgKOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTh-tJwWK6FfIre48N7D7KOWU0jsjUTbi4EkOdf4gNQCbuvN03JzxkoNfRg0RSsPhaWMa994w4s2OsmuL3laz8xLAjNrmOQx2gVK7J5lPb9aRKzT__3KfOF21KUDaaSH_r_tET_DOIc0PGzejLQNHH0W-F1dt6KC73Pbiw7NKhUGauV04PzdQsHwGD3YSTf3e28Y4sCHC6KpJxttQPkLRqwsHBHIj1ZPPsD2U3-L1t3UoMUTd_nwK1v_Vgt-CQHrC8yaxJ2REpgzXV-S0biy3FDePfQ25I4wNp90jnscFx1dIKPDceJrqzciJFjoXP9dShAYcP2mbh8xR4L3q742Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=U9HYd1XQCUivo8SqAPJWDQeL1XQBsaXV0qFyPVX4olCGZqa3yBXn3PZ4E-DsB3ZL8RGQ1tnZDF6cWKqlhcJ2nLfZsPsjeoFmBCXOeF9Bu7zoxpHj6JQYcaZowvvK-2RESyDC4W-NTkW8NqTsEansUqxrc2300aoa8_JAFV_lpvWGuG3mY3IvZYoVTc0pi_gCAilpmGfjzYeZXhKVpErr1jUqxWY9AKOXVnsCrzUWP2WlKiQKjievm3PePrFIoH0NLB8YVJ32XqiuP5cvlQsTdOnHWS9-WMCYESrITX1JCH9cWKUMU4KsfhoJtCqVZfrVRGpVwc7NPEhDKCtZrtktNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=U9HYd1XQCUivo8SqAPJWDQeL1XQBsaXV0qFyPVX4olCGZqa3yBXn3PZ4E-DsB3ZL8RGQ1tnZDF6cWKqlhcJ2nLfZsPsjeoFmBCXOeF9Bu7zoxpHj6JQYcaZowvvK-2RESyDC4W-NTkW8NqTsEansUqxrc2300aoa8_JAFV_lpvWGuG3mY3IvZYoVTc0pi_gCAilpmGfjzYeZXhKVpErr1jUqxWY9AKOXVnsCrzUWP2WlKiQKjievm3PePrFIoH0NLB8YVJ32XqiuP5cvlQsTdOnHWS9-WMCYESrITX1JCH9cWKUMU4KsfhoJtCqVZfrVRGpVwc7NPEhDKCtZrtktNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv-q38zDJtQr1nptmS4F6rQN_27UgC_7pLUjgFNWC4lLg2oi9KOBPopMS4oZSAb1mhFu9sNlBOGWaDUvpyZdHU7-cPWnjEp4tH6eigkCIcrPWbCZS3Z4Fy_pMOoGshGD72YsynhJk00w4M4FO7sJYac1CsA95dqhQvGTlmBHIRkpaXN65G5m4TZ1ZOS_S-BWuuXebQAX-Au6ovxwk_c7ZyHcHi_FcA02gjkWPJgguUso3zJ_Fy6vtZC4KIxKBnaG8xFx4mDFy8gSKMr_3JQlBLXzKyLoxElaiPz7RpZwk5NNHJ16sjh4oRHpJ9L7dV1ddLiXWOtTehVWK57eLmRaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJlkylajHRRRw2O2QGeetO9X2kMOcUvmLpbPM9uXw9ogQS5PbFTo4cfUx6TUbDX4I3xmVT42WtMhcUC3TmmuxKkqD96AvCxlDwVzCW6XlVM3Wy4Ig1n2il5U5sc94Z0fGBERKceJzoxth8azCLI3o4B9PFNe_dhZwIiOLqzOfezY5qLNPVJmEl_pGLOCPFAO6U4395OBlNgt_GXFtFbsiXb-8jnQXOLHbzW3Z1rD-yxRT5i0Z1a5Ko5qIVGEwdNPi4Taq_A89ocq3iSIHTUsdkS-Qk5jWjmd8R_S9m9dn89WX5zVpCxOBKu1cyo4cimEBQ4vWlOlyVprSeSEd-LrJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Khz7wDlyNnvo0dpM09OupZ7PUx_pDTe07kSNTGMAbtJDN0BfDeQ04E6VbnbNUjwLXHJab4qd2z1VZYbqmz8b90WwlBpDmsW8vJbrokdATkhgYkN6PiKc7ZedKaASAbRyV0JMS-ry4MU7ZlalJ0h3PP8N07bcMSBGKVNM3zLrOUluXMYPOrev_y7GbkTUPEDHAOuLyDggIHQzRJGjaeyx2a7K9HBnSwMT932waIf-z-v-fWVC85X42NHb3zSGJhhJgnXjnLPAGY1wCfQvW4fV6YxKJIxKUrKCPqjmWiahgr3yih2J6EChUBVqrKAR7Y-ZgZTUrrZzlfHRy__MIQnjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vieDyFa2Bz9VviR1DSc8VGBvRKp9CYPtW6O6xLgL51ebiCsH4M4JQO760Tcx9stgh3uH-Efcs7_zEMTmNrS1EBV6k-TncQwYzwcnghiYEO6DAAbJ2YznbzGoiQrWilny5WVUzl0RAyZROuSfKayyz4WBWVpTdKb_9JHiAO3ziM3iBg4deKY2D3R5GZwFwn_ww7GAcXk1-TI7yBN702uEPacxsf3BV6XVgc6u3A35dQ2Y_Vsrie3ensXWZKIcAj9HiFGo1dPivqE0lvj50GoRemtOyXeOVyrr5NkbfFvuhKaIXcQSDnuhPJXJ22H5K0X3paTMVIjefAwa2jJMoDSJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=e--0OqaJAH85iRJVuxFVzLjA30EvU4aPJuMVhEQu_McbMz9xcJuP8MLbyhJD6T2XbLbgvzXZmJuXIg-03nVAxML2evapJ0l1jGvZfa0g5jWdWsdABdZghN4EAbZeFddReAUUOVBkBDqSMVNhlLQN21SnXlA4d6uuCssoCJYM1OZ7zdu_nXYlPumoZPR0uwoSk2QIN64q1zClpbC7JJuM_F1455urmT7HCW-jOxOpGxOEGGYaDvb36gQh2qchg0dP8oQaqp092O0cj1OnWlgaX9DVL-Yg_qqVyYMBhuvkmKY4WckB46zp2wLRVpxnxG2iIUCQQb6uUeHKTPk8YB7n5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=e--0OqaJAH85iRJVuxFVzLjA30EvU4aPJuMVhEQu_McbMz9xcJuP8MLbyhJD6T2XbLbgvzXZmJuXIg-03nVAxML2evapJ0l1jGvZfa0g5jWdWsdABdZghN4EAbZeFddReAUUOVBkBDqSMVNhlLQN21SnXlA4d6uuCssoCJYM1OZ7zdu_nXYlPumoZPR0uwoSk2QIN64q1zClpbC7JJuM_F1455urmT7HCW-jOxOpGxOEGGYaDvb36gQh2qchg0dP8oQaqp092O0cj1OnWlgaX9DVL-Yg_qqVyYMBhuvkmKY4WckB46zp2wLRVpxnxG2iIUCQQb6uUeHKTPk8YB7n5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cua5lpEW7DZMHuRGSiN9ltxtCc-BeUSrhDHa0hdjZ2MDmzgaCOroxdxAzMLyx4JvPMzShVdNiq8zeL9cgk6_kVz4AiAoLVUWC0ygzj8c6VjhnZo8i8UqZed9KdHPh-Ge4-xgje8nOs9EOtRQOdNg2ViSJxwt3YL5ue81IjOzTHNwOCdqNk9u5dsoBZrr3GInWLHmusJYU97DBB2lCB-iJoHU_qa6darqEQ0mZZVDEeXLVEnUvXtRnYc9Yt5wu5dQLx0mfxtdSYTI-2HmI0UHk7jwHwNErkOw54HZ2iaEjDaCIC5jT37ACWcMA28VFuM--EkTdCU9WQ0xmEU--AbYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6mSaSAOWp0nRwqbDkAxa4ta-AIAt7bEt9hbHYDlpGsjeCaGwYY3KIHiGivBVfZsBoTMNeUfVJIoJLXnjW72kHccDQtZTN3RnJ0tymUzsCHYlEl_-4XiCLyXYfpx63qvI8owdW1T-PWGnJC_Hcu3PFkM-WlmxGDQSGeHZcFvA0XPIzlMRq4rbX4EITCL-LySbv76aghPB8_X_BYLIScnuWaxHQQlwPsXqkuNeiAFB1ZFfJDTvlfGuDeN0t1n1pTNU5sM-gC30AYI7cHksSNqzWep7bkeY1CO5IbdXjr402dwwQtugr7U_JuafHwUWqWVn6-bafPKW9j77l0RHKsfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=aaH7l5e0nZj9KtFmmj5vNQ9DTep5D3RhR6N6daeadCJZEST9YXF1mI7HXDMi5Uc2ffL-RQgIjwhchcImOe1E6zqklA5pC4odFI5MZ6c0VUGY2CB9x_qb1GmAL1WBLqislDEDcva8Z0jUFIOPBD5iqiu6oKvcifhL279FkVFdIaEMItgg52L1cBgv6Ndj7ae6zXYCPAKcSmmu8M_HeUCOlN9vwF3dKYK0k8sWHRaQYVKGFirwZ8rmicJXvKaDTFVqQevzZ7W3xx7poCnh54JebGPTGx0yxEWAxMz9bexSE_I_C0h_l9L1EDMwkKt4QOarkNAaYjVoNln7_UGf8jprJ2iEP7vq6bT_cG4ccJmZDCmIgVcd6fdncnvyVLc4kDyyIt1WWSXGKhOMN4g2i0BIrQ0X88W0w0kb7Ve0xuItJJJ4qSqtN0KPM-6cSyC9tgnFUqVydBIQNGdTckLS0i3AekV3ZVzEBzSFzRPa9HSX5NhNqHB1mRph0KpFuVLS9yb1aJ6U0rpeMac7TkhBI2AkhF72Nsga8AvsIfeXK-Yq9DaMi2kkH-PcU5_DqVUQcz7KiB5r1PGHOX5au9Cg1QfEhfnsxWP5fVqoHeNhQ8zaFhyTFz7TM32ifkFoyzayZlY4SKfJYHp61yFQWQFU6PwMoAZNPY79bNJTfzqAVCroNOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=aaH7l5e0nZj9KtFmmj5vNQ9DTep5D3RhR6N6daeadCJZEST9YXF1mI7HXDMi5Uc2ffL-RQgIjwhchcImOe1E6zqklA5pC4odFI5MZ6c0VUGY2CB9x_qb1GmAL1WBLqislDEDcva8Z0jUFIOPBD5iqiu6oKvcifhL279FkVFdIaEMItgg52L1cBgv6Ndj7ae6zXYCPAKcSmmu8M_HeUCOlN9vwF3dKYK0k8sWHRaQYVKGFirwZ8rmicJXvKaDTFVqQevzZ7W3xx7poCnh54JebGPTGx0yxEWAxMz9bexSE_I_C0h_l9L1EDMwkKt4QOarkNAaYjVoNln7_UGf8jprJ2iEP7vq6bT_cG4ccJmZDCmIgVcd6fdncnvyVLc4kDyyIt1WWSXGKhOMN4g2i0BIrQ0X88W0w0kb7Ve0xuItJJJ4qSqtN0KPM-6cSyC9tgnFUqVydBIQNGdTckLS0i3AekV3ZVzEBzSFzRPa9HSX5NhNqHB1mRph0KpFuVLS9yb1aJ6U0rpeMac7TkhBI2AkhF72Nsga8AvsIfeXK-Yq9DaMi2kkH-PcU5_DqVUQcz7KiB5r1PGHOX5au9Cg1QfEhfnsxWP5fVqoHeNhQ8zaFhyTFz7TM32ifkFoyzayZlY4SKfJYHp61yFQWQFU6PwMoAZNPY79bNJTfzqAVCroNOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=Ovfy8qjl_5z5I-BZ3vEjRfcuhcU3H8Rxp3mM5qYrKiFycwa_qtczDO-l6u-j6JlwtuJQQHdOdlhvjonY_EXvLY5eWVHfchaqr4JOo29bikrfEQ_0u1Nv5UJBFwXEgkxP40s7olMYchE8QemuZV8-3NG06AUmuuixgybvbkOMDs51tjETLe22QVcdfiG_anVA7S5ASzBheu8KRCea-YLkf-R0GTtEhg3WWHuDSUFqDnQ8pJds2IGnlrELBt2vzdmv1-UgfXaocy1zq9YTsNm8d39QesvbCqbYOSVGbxKz85vudxs2FUhKY-zmWZvQ_WF725QYLLH6sCPYd0ZMYo7_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=Ovfy8qjl_5z5I-BZ3vEjRfcuhcU3H8Rxp3mM5qYrKiFycwa_qtczDO-l6u-j6JlwtuJQQHdOdlhvjonY_EXvLY5eWVHfchaqr4JOo29bikrfEQ_0u1Nv5UJBFwXEgkxP40s7olMYchE8QemuZV8-3NG06AUmuuixgybvbkOMDs51tjETLe22QVcdfiG_anVA7S5ASzBheu8KRCea-YLkf-R0GTtEhg3WWHuDSUFqDnQ8pJds2IGnlrELBt2vzdmv1-UgfXaocy1zq9YTsNm8d39QesvbCqbYOSVGbxKz85vudxs2FUhKY-zmWZvQ_WF725QYLLH6sCPYd0ZMYo7_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz2Qfm1ZXBla5v6Dd7BQGc6w9DCIojBrh0mAr488huT-GKM6IafujRbdB18jpUnpMBmAKqdcjJReDsCNwp5sHRHV0Ppj1c5ii9qx3FrLolWOAJlDpDogXJKK4o35_IbWIucqQhpD3SxoZmfcpmZJQEZc9KGhaZDgiWXsfaqRTKGhlObsM3lEVGHB_EZjs_aw728EPxOZpUQFM3WnyVEBemR1GqZioWQqZ9yBkLahxnD-jABMykIZqtDlrnhEQie5whhlRKqgkAmotGsjtLY4Y5FxuiPTgvJPnTtImNfWwxEEcJWDOaLsh9zh3ANmBK1cHRNx3xh3xKVa_YTmHzYFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=N86MkV04Vl2KWVS19MqBFSy9urKygSC2HvpGJkjXvokhjpzgWz-vAnCgcB3qkj6jFhVCj77LmFjTKixMG-uwnPaGZJl72gZz6oG-OrbpATMDm82vhMp2Tia6CKx-zQJ7mlJrBbiweewj9Kj78ApUdNsR31K5D-Zk_QLRpIIMU9OuC-nlSvkw4E8IQziGzyV129xEdcjY2LRSZ_RjQScNbEzGuVMuLw6NqXEFrnJjVNVCZu86g4n3SZaDLi1mCciwQo8CEkx4wt-PpnfJXoJnpFdjr76fEXgwdJzfFIbKYLUMFSB2k8iHOhZg52yvLyWNjUTCUjimtWJS0mpBqWTPHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=N86MkV04Vl2KWVS19MqBFSy9urKygSC2HvpGJkjXvokhjpzgWz-vAnCgcB3qkj6jFhVCj77LmFjTKixMG-uwnPaGZJl72gZz6oG-OrbpATMDm82vhMp2Tia6CKx-zQJ7mlJrBbiweewj9Kj78ApUdNsR31K5D-Zk_QLRpIIMU9OuC-nlSvkw4E8IQziGzyV129xEdcjY2LRSZ_RjQScNbEzGuVMuLw6NqXEFrnJjVNVCZu86g4n3SZaDLi1mCciwQo8CEkx4wt-PpnfJXoJnpFdjr76fEXgwdJzfFIbKYLUMFSB2k8iHOhZg52yvLyWNjUTCUjimtWJS0mpBqWTPHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neQgR4wI3gQYm18AdlifM_184-7WxPo-uOPTWmSRQ2_UDiUouHIKNEK4tBMC1ZyIFrMPuFd3HcxwdgE9ANgLKb6LFKWFOYVxZtpzLzSupzJ5yG2HDnjdhmqAXsvYn4VZpTf1GAH5kCCw-HepYN7POeegqun7ukV_bYeKBxxw6JQ-dTp7K8U_Mm9TzE8WP1dYZyTa3Qx2og_ck4BJQQp-ES6A-i9D5LS_uRqT0WsdUB2l7SddtHmnrTcq4En7JWzBNWBdYPdN2EI5Z3E6yQQkv6hyOajlTHaUQdGaUIFBT0P3QHrCcHZRhTZltHZFgbKWu9lQk_db6WFDVY68i5_xcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=FxI5_IK2aB6kkJ4uwnLguhHFvpUKpLjpN8XzVgbWzVt1nUWeluUl9bKuEL6oTcyMM7tuqYPAVh9l45apSoJIzCq562tNfPiOOrN69QdlhLlXtp2CyCl5aLiuAEZuzViZFe5izl3MKFz-N6jyCXqS_zn_TLQP4eDlHIqe5f_WUcFG8xW97_BH05-uIK4YZOB2lxcKqeh9-lJls9zns66R9s1TX2uPMg1MWIQGVRfWP_EG1bg3LdFUP318-zY_qcYuqENCRGP9fVfwR7t28G5AhqfU7lF0MOSOdCDUzbrfkOVb79hlwLi8LMfqd_ox-bICOBWbosKFSQ5ZEvKS8f1oYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=FxI5_IK2aB6kkJ4uwnLguhHFvpUKpLjpN8XzVgbWzVt1nUWeluUl9bKuEL6oTcyMM7tuqYPAVh9l45apSoJIzCq562tNfPiOOrN69QdlhLlXtp2CyCl5aLiuAEZuzViZFe5izl3MKFz-N6jyCXqS_zn_TLQP4eDlHIqe5f_WUcFG8xW97_BH05-uIK4YZOB2lxcKqeh9-lJls9zns66R9s1TX2uPMg1MWIQGVRfWP_EG1bg3LdFUP318-zY_qcYuqENCRGP9fVfwR7t28G5AhqfU7lF0MOSOdCDUzbrfkOVb79hlwLi8LMfqd_ox-bICOBWbosKFSQ5ZEvKS8f1oYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=m3legXKoHD1wt5TfsbvdE7zQ0yWV3jmYQQ_D1UTAR56yseY-P7UkftZiLVC_m4nfDS5AFD95vcdR34Sxx4h1qbf07KgtaopIH-3fPJ2Ty3_bkBebxIkt-fFnQiZh_a1DVw9N_mDbd7oR6og8QQ3lAibxa6NS5LK72xVZOJ58G-sYRj7iSUj3YlVkJl69xNDlsJznr7wpjo7r9ywv9rTeHtQpGmY6lX7z7b6XpcJ4b3aTcT_tTx8YY5fIRlOgE6yh6tJvIOTYQ57ZJqwOJblA0xOf9om__tD4pxpV_e3GQATI6wxlLVc9fgVDOnZbZy0-34bgiBBCXwFWYIB4hhyvnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=m3legXKoHD1wt5TfsbvdE7zQ0yWV3jmYQQ_D1UTAR56yseY-P7UkftZiLVC_m4nfDS5AFD95vcdR34Sxx4h1qbf07KgtaopIH-3fPJ2Ty3_bkBebxIkt-fFnQiZh_a1DVw9N_mDbd7oR6og8QQ3lAibxa6NS5LK72xVZOJ58G-sYRj7iSUj3YlVkJl69xNDlsJznr7wpjo7r9ywv9rTeHtQpGmY6lX7z7b6XpcJ4b3aTcT_tTx8YY5fIRlOgE6yh6tJvIOTYQ57ZJqwOJblA0xOf9om__tD4pxpV_e3GQATI6wxlLVc9fgVDOnZbZy0-34bgiBBCXwFWYIB4hhyvnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAw2TRhaazShRbC6YOXHjsu2K51mOZlAeZKXXMx_O0EnMMT67PnYVrLPeNnkMROaEV6yORbpCnYqN1MhlumxUS34yyqLH9JSbK_8WQct1PvAkOtR_1LH5ri9CkeZKJsJeVzGPBhAZwutQPOJpsfVSAd-OqKdXHhIcWSZZRybzcXjvjzcrSdiGBzkHD1YcnlqLTE_YudblctGhvL6By2hvA_Ccnla-pe76xPlOQYciaSR4nWy1T1sMr6drAQEGcjxi2EEZVJdxCPrmKRR_Cux0MYVhG2pHbgaJ51KMCR2IxmW4-Y7EwlrX5sLJeqfZa6pEoeiqZaUs20tJGAgXKwlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=DRcwKGedAcfPgFvAWj0XrFKvi5Mk4AQAgMyru_Kgx36m0ZNf0WQ6-uLlggkHN7vmC6ZZmY3Az3APe1MLDDp5lgGY15t-uerSR3lSDzrVgcBi2P6s9cdHbm4C0ab4vQE8IUBhs3wf002hkuPRGN-90-rOaqXtcrtKF1IwNhvQccf68-hR9yB_JK1h2PJsvNu3Am2i91Fx4SkbnoQifeZlw71YbblwOPbt8lGZl60HqJP96LSOpm4SYHZndBIJ43TpD7z1WgmFeKVSEmIBN8M8nr4xG8-9PQ1NIY6e8ZmHwAVN7GodMxwlaTRFS85fiWVqpHOMt4awnYx43aEm1OzEnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=DRcwKGedAcfPgFvAWj0XrFKvi5Mk4AQAgMyru_Kgx36m0ZNf0WQ6-uLlggkHN7vmC6ZZmY3Az3APe1MLDDp5lgGY15t-uerSR3lSDzrVgcBi2P6s9cdHbm4C0ab4vQE8IUBhs3wf002hkuPRGN-90-rOaqXtcrtKF1IwNhvQccf68-hR9yB_JK1h2PJsvNu3Am2i91Fx4SkbnoQifeZlw71YbblwOPbt8lGZl60HqJP96LSOpm4SYHZndBIJ43TpD7z1WgmFeKVSEmIBN8M8nr4xG8-9PQ1NIY6e8ZmHwAVN7GodMxwlaTRFS85fiWVqpHOMt4awnYx43aEm1OzEnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA5dZBZDKHVUWJgs0yrXgpx51P87a-NlYmFREWrBAYbjiXxoelJrXeYfQhgJVa_4BjYFpB09I_mJdMKPyBotZ0OeKhLiZpkvmX5S-gLhz-CYWcSOfXuJypaIjbcDofdqlMy3-MZZoX-e0uFYLGkxzEBOUiDhwycG-f9kMrb2qcOPR9SGBRwZftA2ACNrTqUODgKfAZi2KKbzk0M1mBIr3HnIBIjMMZHQ1paghakpMgdPjl7FSXPZTZNav4Xm2_b_MXUoI2t5Uux1yStZbUd6LonlyYSM3rvShwoBbNsH4HqeR3HTx1lfbBvywKcEVxvjjvgL5M8xuAOEAjstMiiEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3qvsHR0oen1flqzKfFizQcFYPRMZbISwfcWFdc0_M4qlA7ZzHg08XB0r9Pm6wBz3HdhzQlWgnfQ6VCwvfwu4m9_FdGFRqq56tdeymoISoeqTrfS3Rga93IT2Tjek05_zGAlpGNESiMEfnFz4yt54vyFOFAmdhBofWHmiAa_XJ5F0NiUjkb35DtYP437ErSx6NJDBCqWEGbWBRe2pNVkwd8rrqNX-JDhrsyUGWavaBE_2HzMvqKtG24U4_eaPaOqBZ4yUqrp9KYsfj2sbnN8w_CMcPvm9dwr9A2JhXaQxXNJht06AvaBuHdKSJIcVvR-rbuuQNsZ-zW65SDX9G1Xtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe5RhaA3yqT6bXWE64ox_wcfcD4mMatpG25nLXbYpBg8QqRko5bJYnjXWHAOLD8tFJPkYl_n7WZnISfCagkWy_hEubkPWoo5UV4uNxStGmDRTyK06Tx9wbGN6oEi_KKySlt8nHiVt45N-i0g46Lxyna7l0MLJ-7ScVKzS-ppxdsMLF7lq81v1YFVhdqeVy-o3F71h9iG0GEpsu8erE-1WjLLa15rqdZN-eAl6UfONrA9ReiDernuebw22jx7Q2NTwNRS5z-wa8jdSLaruR_b1p3jHRmVPfkZKKF3GG552w_OZg_XF_vuNK2PRfiAGwYzLQSJReOc_lvLaZQ_t6qdPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzwQr3VMV-ReKWgNVzuCykmO52f3Qo210tavt4FuNxknoL3J4JvZGE0HVFyKd7Y-Ft1xopayeRx7V0sQB30FLpUcDQR4bgwIq1IlXyctZnOA1OJwPaOQVX50W2i3LLJW381j0BR156LmXnD3tGX-q_sLnYhtVNQOf2aMsioe2YdYM_fAN0OESlJ-9DdQANlvlewdIiiIdBQB0jd4EETsMhjMWr_UASeBAlwSf3x16Fn0W7qhhRFo7Hpl6MiG6IH18BWDYgZrTxLyXYO1on2YkuU-UQXVdHPked4SpAx0ZFt5Gpwo0zeiTlINDGj0I2dzrXVAiZJvvuY6Yn_GI0Ircw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyiukmjvEHYiRWm0Y9Q45NaKQzLSmaT-kfnB7RfTpBgyEPFiIJgzGOTlHNbqcGt4J1QaHP4BYuZ0Z0gPGBImEhBoWRPHE4kRRLAV65KPmuhM9txkcsWnLH-BLXAA1wf9WvBeLJgmpOwuTgWhmLwis8vVUkIEDOT_izFAOP1N5rwzOHvWYGqBUYsLtZroOGj2N9lElMQVPgV7uOa0WJpRGl6C7txsQuz_6nnyVVYix-nYZCmKTimSNwNxTnSAKqGJgEkhGvDFQxcoq1Sam4rCWAyTfcbmUkoChdUy-02jGFzU7E5RVzzdxl5t86rxxxPQA5yZbiB1J4Sye3Gt1_K8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDXmugb1U5Pli-xeDYDetNlA760q4DzYgzxb1GdHMhcuTbrgRY4KrCegdy0YGsKj2XIUXI0dYOrxnrTlPsq8XVGtINUqoSPV0N7THaLiFDFBPgSRqvaX8gTcpMrffgTxZ_Hh1LGvLaTDMnFTwh0ptEjDWMaYHlfUzoox1BrHBDnZL2lC_KbkNUPPI9aStaTJs26QA0zWbaQhfsRnIq9h9INXBFrW5oBoOldbTefUuXaPGAB5MzxotNhboC58s4dOeGZAguhEh5byV5o3zIK3oyqse-b-k5bzvK785bd15Xl0K0K_ZCY0uWhsSM7lOqPM6Tg3JxrA2WI5JRWK5BCSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=nFZYERyA3QG06VGxQDePV4hnsBNPLQYUIBkqDEnKoYRwAbaf8JaB5rx_w4agT0xRHmkh0KLQKnU31Deh4lKrfG3pIb7gkDvN2dV956Ky58FA7vP6aqFYk5oLYNJ_u3FXUHhIb8Oqz1iW_VsFiS9oB9Y8L20kfjopgBFrcqJB3rtojBfnVGSjO5Hawy-DcmKlJMrZcboJZCqa1w5otxIcL7nkIwenA4NDTNkmyRVOaPcrXleIeWm_d0QOqn_uH1AsRpNSo-kjADc-lI_4LgwEz0la-fNZOYvSKvBTDzT8uMZDQ40gV442eI3Y0pogzsB0RAUJz8VSfxf1ElwDQXcekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=nFZYERyA3QG06VGxQDePV4hnsBNPLQYUIBkqDEnKoYRwAbaf8JaB5rx_w4agT0xRHmkh0KLQKnU31Deh4lKrfG3pIb7gkDvN2dV956Ky58FA7vP6aqFYk5oLYNJ_u3FXUHhIb8Oqz1iW_VsFiS9oB9Y8L20kfjopgBFrcqJB3rtojBfnVGSjO5Hawy-DcmKlJMrZcboJZCqa1w5otxIcL7nkIwenA4NDTNkmyRVOaPcrXleIeWm_d0QOqn_uH1AsRpNSo-kjADc-lI_4LgwEz0la-fNZOYvSKvBTDzT8uMZDQ40gV442eI3Y0pogzsB0RAUJz8VSfxf1ElwDQXcekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNHgEChL2suc8jt_OEuRPkdUikQAUX351tT7TIK6Um6FSG_Ws2VGvOp2WPeeFOGgBuCNhNy9RDWxaxmiZeD13iwYnRLRxSFMuBC6Y2FdtBXxQQwTc5MOUu_0ks_F2snAkw5HBMZfFDrFvCOn5U_1dka9q9pKu0y5xxkPPRQGM3-515W3ERjmdrNKg1wcw7XFLCCWupUrA-scBqaMJjIKI1HhN1DTVO_CzdvI0BS6a5N6lMVHMK4ZAmjpCvJ9va13Nw83T84HMyZnok0kbVfPIW39tnruSDajPOQhZxintHq1iyKEftckOA_gEg1toVUR0AmD2vulsbKgBgDZTvEBEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG3aH5Vz4fc3mZYwcGaKtgBspvGaOTn4l-1Ap-jHY-ZE708cfn-nvPD6YZdoS-PEzVOz6ySXSFc-K4bqG9WdHMResTFUozwLCRvXmX4totX0dDxV7k7lk-z_u6ANrZ9sAUFpnMjVJpPQ62r9dE3P82sNB8X6ZpcEFK6vfGm7v5Ba17IeKppeamdJm-Yw6G2cwGu3kRIOswdWdfT6AOtmkWz2tXfGGubxTQrJ2iYtB0w-R_0GqcOP6VuYCtWfIwD6cVQbsLneOTy9gJ9S83GPKiMU2fw4dmyH3g7bK4gElcdEqHuV5DF1jHP9sd7iqhYWusma1QUsFfZM1M-TtvBS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ74eRlE1s26ejUoqv6fhy5cTYVL1XGFfKR5wEQeCpHf92IBxRfNuwTDbDoAzEVFWunlqRO8dY8xRJWYTFXDW-Z2-Ln7auL97PvEKXjolns6pVRvnvE-PUdKQxLe7-xqa1ivXfvIzTq0axTrTz0I1Jazzz2XFII9wkdtlABw3zZfuMrbKq5PxkzplqOHRgIui3a2bMjvsXU199DcWqgSVENFffpA64T_5b6GVEcKLkO8ntYF5TVZ2It4y8C9F6farAAPf0VKJ3mRBgixGhxP5DNEvXl4ComdPDPQfTvkV5bgLyr688aXEppa7KFFdhzpwy7npsY-MP5Z39bDjWy8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gxl25RUSOXYOQnNUWudWQAmSZJ6PB2IZiVaUcVXksjHQKwXk6Kknt45cu3Wkss4DUxrkDs1TEukz5_5Y1L0X5IQ7NaG6ELvmz7ebMkBtzgq1XOlvK__ngHTnWxzj6-GTsViU3EZ2zJyaian3-Ii9NI0CBOGjH9U0BrQlMIut6XeALlcS4imLlghTIB8V2YxXr3k8_N68MUAsjz5m6Y2_oPmmrnmD_Zk--Nce_SisnoVaoMT8up6g_HZdglWoyMhV2aOcsrNUrdNBk-DhI3XMryWidkVC4WdzzmAAIQkKjBkUXnR8wupnuAltLRaNXPSMfBA_9ZgOsZS7MWdy09ZkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=E3d8xmoXopm7nn-PRy9Owya2fPMz2ChfLzk_OvH7vqcc5EtzpQlVK44eLm5ZJML_uTc7BYC3FnrSNjGyKt131huZQLGIYHDt7EZ1MkktJb5VIVlmFKvVhX2gs35khAHHT8Pokw7vQq8D_Et2Kbdpoo5nViiNmO9NpcUV6biMuXnOIzyt6pVP6q1s_ZBzOQhx7LKz4-kn4vNr9xxHTzevpHrXPzGbJuiocZUrsnZFnhYcUtuIGZdAsJT-aYtxSqgG4XnPC-8A6wR0JWd5cPIcYsetICMwSbTDpt6dOr-NzLoOu8c-hQC-VU6KpfRGtau6ma8zQDBaAicDKhYB9SRZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=E3d8xmoXopm7nn-PRy9Owya2fPMz2ChfLzk_OvH7vqcc5EtzpQlVK44eLm5ZJML_uTc7BYC3FnrSNjGyKt131huZQLGIYHDt7EZ1MkktJb5VIVlmFKvVhX2gs35khAHHT8Pokw7vQq8D_Et2Kbdpoo5nViiNmO9NpcUV6biMuXnOIzyt6pVP6q1s_ZBzOQhx7LKz4-kn4vNr9xxHTzevpHrXPzGbJuiocZUrsnZFnhYcUtuIGZdAsJT-aYtxSqgG4XnPC-8A6wR0JWd5cPIcYsetICMwSbTDpt6dOr-NzLoOu8c-hQC-VU6KpfRGtau6ma8zQDBaAicDKhYB9SRZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiD2UQb0Vlb-FQeDrkot_3KTovH-lOCQ2coONhwTDliGCnG0tkvBIH6aJsJ9ohMZaWPJbba-saGaeIJiYwHO2VWqMv1a2F9mDjFskSYMPx53D9eqt0p7vMKWZbQouRnF6KIVitXPH378y7IClbsDIEIfmOlueGYUPq38O74m_TYpS1WUiVLujJeBSiKh6wbDW6waTiJ6Csr6KB-qmB3lRS9hQ6WwKkukoLhgZrp3gsS77bwDfIJ3El8UH_IkfMYYwPtAhGp2u3N_o1d_iDnhjYNdNNtb_fb88fDUKoA-ckRhvepZD8_GMBLKhmI5qBe_6zb9524wZXQ8wcS5X5hLGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKh5og08cHbNrFkWn0UOWqSMAdLotILOxfY44JFSTtOX4QrbCg1E6QzXNTg0QpGUW0cpS3lt0chyh_caLCIncqIqHPf7RcgXZDckIX4Uc4dFsqYxQUc1drCdj8Yjftj8pibb5n47DbJW_XGzPkYghljpJGb67fo5Rwr6wPV-eT5hxE79a0D4a37arP0zXJadnQfpvvvXg1PZLq9hbeB80ZBPvqpqQTaLRbIlFTQP-D27puc87cj98feQeiWb3RWkvfI5myH8dmQeBm8lBcdD4LXUqnzXdUlDPQomCV1bi51MlV-8TM5WEJMX6ZVxUfEk5zOA-_KJrQIuCo5AMvngkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsJ0RtWgbKg6LZUA0GEhJ9tmfhna16erlDD_dvZlJFG6dGSWsBtKjb8q3lEdaKFsgWWemdaHgnqSm3grqHR2MwSyLs1zSPVwKrJ8ZL8k_ASJMG9JjKX18-lvXHCbytv6Nyz1sKpti-TWMVRXiUhiy52Jnl4v9Fx8cb2bpXyqHFpJhaPJ5uqc0rXOcDjdrsCOzyFkl4OZLTrg7KHgEMYg8jwd2P2hSqtcMzho1pb6FDHqD63750OaDf8uepcD2V5jNm3IWrT0RpM-Tl1_iAvrnNKbr0gWiFtfy74ZkviCeYkHlRUwDWBUKti_OzWIIAz4qASkb2SrdWcEFupSn_PdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkI9kvXXBFH6F_ygGzsh1AHyzj8VgqtrHVeL-vxgE9UQmEdxwt9V8RW1M0_4ojJCcjTYgRDv60yvzR9NRIZjnUMsZm2ybuVWJ7Ho-XTOOIC3yJXFlwOj0TKAq3fb5FZGQbTOoMGh7jUVrEnWiNukKRNBCck4Yh3CE_3EYsdlv1JZ8iZL9VIE_D_DaaliZd61uoIuUHMnGhWBeZhBgOy_eFZnge8drteZ1iArx10jb8wxYfzdV0ZNA-RO4bPKt4QFZvWDXlNjx-ABWcZKjvyKeEl_YrI4gXdH9yTLQu6FtZcIx1LTlrS1iQ6KAG1THDpt5fMHxA3pDWNTUTjM2tISzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soioWcbD8hrEdGxsiZ4Qd0vzb9uJ0LHi-dxPBeeAIXIj5iKGTilyk7bgNiBqXbpuxpYbDtoIUapVYhUDqe126sH5rJ_icNiHEyTKWUpuMeGGsiuXNCqhAyQ3k9-B7DaEr7BvSr0bHKRcWC0z3jLQVhwulicWMZoVBF9cUEZEWTtdUagjvHj-Pp8RT5ieVQ5IZrhhp6JDRzIZ3P5uePJpgVhH5A4NIuYLDH7VJee6gQ_ghE-4KAEoax0LUyXDPGCB_A-he-86Wu63SQY7a6P8KCnkFjZb2zFRUzjKBwnZmshAIGW1FVdt4bpH6BbxXrJpKSxRky1xKKPvlpNHDER4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5akB5lzmql69Bpd6UQ9rLRgnNAthSBGZpeLEf11AhUboSweMNCVnayNJKdTWDguYqdtaJ6Wfwa-ISQCIf9C13l5mfqbxmjuR8JRMpsS6ek6RXOmd-hYd6Q2TLEiIZYHOZQIW6Ypx_ltK8QPd64W98BPCuUQjlbwem_AjcMQQyoUnkILf5mGYInC4vwY9lfNsUVePlek2m2IYouKRV3GtsEaWUeRwcjK3KDMOGHtvdmsoRhiHI1Sm5R6vMA-VtpkxpxVvWp4MRjuYCOLk0fnP5DukCFSyzUGPvZHywslCEeGZmUuoASdAWgH0hDcCwilRKQViqwC19yliP_vCxqZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMzs5cUPssCIR2PCYAyY_4xf_nTxhczujqBa610ihR7ITh0q8OUqNROUhBPTfROPoIIttcXYRw4Lm_pzTZTsWrAbKKX_xasSh1vqLHjVUSn2zh4y7d8YZ-uBH3joyEP1oy1thXapfJoEvnfe18iPH6W2L82sZt9wjJYH40FIVfB9P9fsZxZ-omnMN7n2V7h9FO0Bbky0tgphlFr9OzwcqgbtEErPKsLiTbn2ye3Z5LUhxOlHNjkpXI8cWtJMN7Um6hOYRf5pb4UDI6qDVFXeSYxE_kvMis1v80aLhBcfmq0TjHYvEeM4MxdjueMYVMPQT_qqmkCQzopa5DdHBRgrHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
