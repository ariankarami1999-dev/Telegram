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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 21:24:35</div>
<hr>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcTQKFWjSocS4SiURLk0QU8VKDJbJ3ZvZtIoL1Zdd7eIdtMnINUgw_suDMlRPq4xhGD6J0PnZxqPoF66wOX4C7WEz7hxwOOClopXQsFYYRzQ0iSzd5ABJrz437HPxBx0YWK0hyDfctCvoXwczBiCZzg44nk6rzxYvTAjNM2AsjA1-Gu_tKcPl-ZJbe9q7JOx3vxoA0dF-I65tgvlGG5qEwDNrXnq6GzmjAM46MEgTuG-sFna2fqwyqIHoaSs1ui2EUXCQTR0oDJ54xGuHn6N3KV6NA2eOQm9L9KpxbkaOOEH4_SwYp1Oq8c-x-6GbqfdkzYgSTAkeGhAnpkk7K8MYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCih9Wib4QqmE-nmlaYMaTAww_1_BKpyJYTVv2ZOMd-hrWF-Vp44dbm9FbzDE9N4HtLIm5Ub1jnCNU4X5D1fHdGmw05wH6Dr2vU3CObOS4VpKgmktmRRGIpaV1PlGOgUTuovF6m78HtxKYgvobyT-yj91baQgxlHG6Ipd6qnnqWyqyM30J82m1cc1RLEPag1GodvEYB6jsqQF21Y8lUllGZz7SLtKkzRt-pTpAXbv90MDW_tzZIUSG4TiIkY6j118Li1QiqjEj4v-2pSQpsjmiOuB_MZG4JxeKK35Uk09rehQc54HMbegpsgIqf6zDnajP2DQ1gq6toc7KwLss85OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=KcVHTOyTn3MVGouuMMQGKMoHv2d-I2g80VrUGw9qUBnw_rnTJgZyU2TyS2s3jfRvKRo0LRDQBXMASCDD7Jdx7HSwHPPIwx_gdtargChd57G28MsMrdB7KmJPgeTe5OEnjN4HxUCFoD3pg_NLKHC9HwxETeHmTy0S2QaEN1-Km1ddEbAtXbwXHNbjxooLKBldj4UpVqgShwHYh_qO1K7B94_YkdXoo05mUm3hfKkNvxPs8pGab4RSDPAzTXwA_2zNNpbeQSwI5Y0jV-08rIpCCXv6i9Ga3WVxinHh2KJtTtNjbAOBqrWOAYNDBs5HMrbO4P3hP9jd1R44JkDGWAY7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=KcVHTOyTn3MVGouuMMQGKMoHv2d-I2g80VrUGw9qUBnw_rnTJgZyU2TyS2s3jfRvKRo0LRDQBXMASCDD7Jdx7HSwHPPIwx_gdtargChd57G28MsMrdB7KmJPgeTe5OEnjN4HxUCFoD3pg_NLKHC9HwxETeHmTy0S2QaEN1-Km1ddEbAtXbwXHNbjxooLKBldj4UpVqgShwHYh_qO1K7B94_YkdXoo05mUm3hfKkNvxPs8pGab4RSDPAzTXwA_2zNNpbeQSwI5Y0jV-08rIpCCXv6i9Ga3WVxinHh2KJtTtNjbAOBqrWOAYNDBs5HMrbO4P3hP9jd1R44JkDGWAY7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Fz-N3D8H7iUlwJu_hco59y0QPHx7WSdzwJUj3GHhJ9bs7LjOPzEZx_37dYx5txWSs9wUiC14KaMyVgrC_zB3kURBzo1-hCt1kQBACxHWS14liF_oEPNSpG5S3fv4H9OL97quzEcnzViM5U_o9Zy8DbKXwMvd1ScReVBYGsdMIC7OR6IJ0E8Nmai8LfUHf-PLflDXjv_8GMQXVkLIExJJ664nnVFkcDYnNE4ELuIdFw7WJLe6SpCVQMyP3NLCVM-ytAdB_wEd4hv-u9_2V2JMN37Ay-Y3uHbv3yUVg1R7_bDGOduOkGQFg924dSjiI03BtcGtsxQJpQAekkCWLoI40g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Fz-N3D8H7iUlwJu_hco59y0QPHx7WSdzwJUj3GHhJ9bs7LjOPzEZx_37dYx5txWSs9wUiC14KaMyVgrC_zB3kURBzo1-hCt1kQBACxHWS14liF_oEPNSpG5S3fv4H9OL97quzEcnzViM5U_o9Zy8DbKXwMvd1ScReVBYGsdMIC7OR6IJ0E8Nmai8LfUHf-PLflDXjv_8GMQXVkLIExJJ664nnVFkcDYnNE4ELuIdFw7WJLe6SpCVQMyP3NLCVM-ytAdB_wEd4hv-u9_2V2JMN37Ay-Y3uHbv3yUVg1R7_bDGOduOkGQFg924dSjiI03BtcGtsxQJpQAekkCWLoI40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is44pcjiKuZm24IgV4_FHE_hsMr3YSS1uK27ngcoflmVrwQFRfxnGaYC0Aa1tTUJ2nOZ7Lde28Lu5Fgb_cNGEBCXBzS03Mzw9g7x9Sp9BBfJiOC6-1-lw6hU06A-Q0FfWNLe58G8g498wcIvqo6pnNy20tEulb4RxjyW7S2gkokRpnfUcWSj4K47OS1r8sf7bCpblEBCxbyZut55Ih-sPD06y9Ajj5zRK2J3Zs7oDHR4D5FfeodBPPlcB5wig-AWIjR_ssBE2OzSwUjmo0-CVDbhO5qFSOfHRkOWHwqsceZ7-GnVsQASy1t-jZCDdtNvh7IdpsUp75VYDh5gICUJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSFbb3dfi5m6VppYUvOA1ZJoVWG4WAEAjUcjAa3ZZ8tN_kzppFNtbhHyhgVcSUm-4dDwyKBBIy28vBjpSGxRKhhqd5RNTepPn1yQppufcd7grwrX-Z2wOE3FgCMgd6F4Uh5g4oG02fu8x8rfh-CGMNI25AR33tI0QoBVmMPLSF_TEmogMHzyw8uKopXqtU8ZfxvXpjiGPzXuzm1dDfOlwtAFggVEDU0JqwZhxKlQLRVP9_OyHnF0zlAmlkvE5EVpCErzzZEYElYma4c9x-IR0JWB5R2z4tnBJOpCztwLaGfZ2mOSiUKFodr7ggaVBgqmiWEVYSnZ9zRcdqKXOVow-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3On4CliEzMDco_oI-tghFhubnwpSWZbL-OcmLuW5mkK7Z4ACE3gCUUVY_8AVDAIw1T6vI4TsJv82NNUKIjDpG0Q-d2IhP2n9iL2_FwAD1WM51VaKkBifzy-uMU_H0rshddk-_d0MuLxnMPCaeDXxQ_gz5aIrIiE87D2rBe1JNW9YXyZr3k9eP8yFRIiQH5vwYFLMrPHlsu0bttXjp_FcU2Fuamd4NRpEyt7QwRDUE6my79PJ5NQOVNb4kk8Mham5fKnV5VW-4AaPmg6pEwAOTm64Sr6URB-_tuWd6_LsIIvjkmq_a1oOPdhgqK2Ka-7YXfjzsAHIqK7JbWfJgKOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTh-tJwWK6FfIre48N7D7KOWU0jsjUTbi4EkOdf4gNQCbuvN03JzxkoNfRg0RSsPhaWMa994w4s2OsmuL3laz8xLAjNrmOQx2gVK7J5lPb9aRKzT__3KfOF21KUDaaSH_r_tET_DOIc0PGzejLQNHH0W-F1dt6KC73Pbiw7NKhUGauV04PzdQsHwGD3YSTf3e28Y4sCHC6KpJxttQPkLRqwsHBHIj1ZPPsD2U3-L1t3UoMUTd_nwK1v_Vgt-CQHrC8yaxJ2REpgzXV-S0biy3FDePfQ25I4wNp90jnscFx1dIKPDceJrqzciJFjoXP9dShAYcP2mbh8xR4L3q742Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=pAhn3HNirHqRxc2eaegatogpo6AXii28LmthyGXn-MPGyNxvOHXBFNksWb7SRnPYYru3dqydy7afMoOtA-S9cpDtc4Moh4lWreaHgoydSFJuQpIpSKlApc4wpVjGyb6J60uYUl99mZxE8yhl_Z1kNE09TlegunPx51UN16dH4m2qBv84Qolvce9nZAZxDLvfIhiSEdb_pYxqlAwSQAkCf24yc2r7RKBeYypcHn2mTcDyHB1ctK9SZTgARjqDazTct0ePdd_N-0B_6oTx0KZltPX48CYY0Cg4TZhqGA_pGWSEHdXeRRm7Qbya5_ShCzXtTohBlQ-75R_R4Uy5esW0dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=pAhn3HNirHqRxc2eaegatogpo6AXii28LmthyGXn-MPGyNxvOHXBFNksWb7SRnPYYru3dqydy7afMoOtA-S9cpDtc4Moh4lWreaHgoydSFJuQpIpSKlApc4wpVjGyb6J60uYUl99mZxE8yhl_Z1kNE09TlegunPx51UN16dH4m2qBv84Qolvce9nZAZxDLvfIhiSEdb_pYxqlAwSQAkCf24yc2r7RKBeYypcHn2mTcDyHB1ctK9SZTgARjqDazTct0ePdd_N-0B_6oTx0KZltPX48CYY0Cg4TZhqGA_pGWSEHdXeRRm7Qbya5_ShCzXtTohBlQ-75R_R4Uy5esW0dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv-q38zDJtQr1nptmS4F6rQN_27UgC_7pLUjgFNWC4lLg2oi9KOBPopMS4oZSAb1mhFu9sNlBOGWaDUvpyZdHU7-cPWnjEp4tH6eigkCIcrPWbCZS3Z4Fy_pMOoGshGD72YsynhJk00w4M4FO7sJYac1CsA95dqhQvGTlmBHIRkpaXN65G5m4TZ1ZOS_S-BWuuXebQAX-Au6ovxwk_c7ZyHcHi_FcA02gjkWPJgguUso3zJ_Fy6vtZC4KIxKBnaG8xFx4mDFy8gSKMr_3JQlBLXzKyLoxElaiPz7RpZwk5NNHJ16sjh4oRHpJ9L7dV1ddLiXWOtTehVWK57eLmRaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJlkylajHRRRw2O2QGeetO9X2kMOcUvmLpbPM9uXw9ogQS5PbFTo4cfUx6TUbDX4I3xmVT42WtMhcUC3TmmuxKkqD96AvCxlDwVzCW6XlVM3Wy4Ig1n2il5U5sc94Z0fGBERKceJzoxth8azCLI3o4B9PFNe_dhZwIiOLqzOfezY5qLNPVJmEl_pGLOCPFAO6U4395OBlNgt_GXFtFbsiXb-8jnQXOLHbzW3Z1rD-yxRT5i0Z1a5Ko5qIVGEwdNPi4Taq_A89ocq3iSIHTUsdkS-Qk5jWjmd8R_S9m9dn89WX5zVpCxOBKu1cyo4cimEBQ4vWlOlyVprSeSEd-LrJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/du1IF_1ZNIzh_m3sYlYaxBIgD775otBLn-l6vOtJ4LuuRZxliIRo1NA-nj9AVRT9bnwUU400FLeywjp7Yuyvx5NHOYT5stSEJDPSScAyZ3YxJhY_rpGj6570-hySq-2BFgzRobjOmqVV_gusZFhU3ghmOApUUr23qTT7WECUM4azCqx9HzFxAaURCPQwMkrQoptT1hfk-lZmx-HPual0mgbR_UYwrf-WDKwspaXuwyKOYSEpfoji7a7dG7--xzPwS1Bg-vJZC2yN0li4rIfJxVygJ6YJV3dvNVyQ2H59T75ybWhuQKjcKxgVXRW2RoNiOOquaogcS5Ds5Nga4UXjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vieDyFa2Bz9VviR1DSc8VGBvRKp9CYPtW6O6xLgL51ebiCsH4M4JQO760Tcx9stgh3uH-Efcs7_zEMTmNrS1EBV6k-TncQwYzwcnghiYEO6DAAbJ2YznbzGoiQrWilny5WVUzl0RAyZROuSfKayyz4WBWVpTdKb_9JHiAO3ziM3iBg4deKY2D3R5GZwFwn_ww7GAcXk1-TI7yBN702uEPacxsf3BV6XVgc6u3A35dQ2Y_Vsrie3ensXWZKIcAj9HiFGo1dPivqE0lvj50GoRemtOyXeOVyrr5NkbfFvuhKaIXcQSDnuhPJXJ22H5K0X3paTMVIjefAwa2jJMoDSJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=pitKv5kgJDT6WM0JEjW4S-sfwWzqL1exRRxMyWKorIFD_OHBj2zyCLOqgcbkxVtqIdtJ3kVs4Tgzg1GUHOvEDH5ba6UoeaZMkr-ceG0IV3pUlNblAteC8Pm74VGKHAtpFdWUG2vF8h04UqQCT69FusI_S2aye2-O8bqCR-2S5NZP_YZNacL-CcHo7JIJ0DL2etCpXnScOKS89fQbJGq9J0WG2w8u2RcqWqZSlL-tUPKhqUbiJpyKtOI0yyVuPUaPhMKUQ0E8SX93ycFRRD6y6gJJf1qQyiNlwEYSXk3wWpbhU_Sz2Kq0IGaGRqR5Xl5--JZlS-lKCJ_xB_NVvqO92g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=pitKv5kgJDT6WM0JEjW4S-sfwWzqL1exRRxMyWKorIFD_OHBj2zyCLOqgcbkxVtqIdtJ3kVs4Tgzg1GUHOvEDH5ba6UoeaZMkr-ceG0IV3pUlNblAteC8Pm74VGKHAtpFdWUG2vF8h04UqQCT69FusI_S2aye2-O8bqCR-2S5NZP_YZNacL-CcHo7JIJ0DL2etCpXnScOKS89fQbJGq9J0WG2w8u2RcqWqZSlL-tUPKhqUbiJpyKtOI0yyVuPUaPhMKUQ0E8SX93ycFRRD6y6gJJf1qQyiNlwEYSXk3wWpbhU_Sz2Kq0IGaGRqR5Xl5--JZlS-lKCJ_xB_NVvqO92g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6mSaSAOWp0nRwqbDkAxa4ta-AIAt7bEt9hbHYDlpGsjeCaGwYY3KIHiGivBVfZsBoTMNeUfVJIoJLXnjW72kHccDQtZTN3RnJ0tymUzsCHYlEl_-4XiCLyXYfpx63qvI8owdW1T-PWGnJC_Hcu3PFkM-WlmxGDQSGeHZcFvA0XPIzlMRq4rbX4EITCL-LySbv76aghPB8_X_BYLIScnuWaxHQQlwPsXqkuNeiAFB1ZFfJDTvlfGuDeN0t1n1pTNU5sM-gC30AYI7cHksSNqzWep7bkeY1CO5IbdXjr402dwwQtugr7U_JuafHwUWqWVn6-bafPKW9j77l0RHKsfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=cPwOCTSHqXI9UfErdtU2DUKtKM--MNkRxXuypV5hbIgBXYuI2XT6bHHt2BO0gzJu2s8Waq_167PCtV6gMmfK0Gmm-9aAJA9SCqfim2FKLw4ikhYIt8ZBGfaEHZTryGOO4p8vfvObYxZAziMKODdSuWOn_3vXa-Gu8hS_sSlQ1oKWF7tY2PVvHvq5N5MeR6RgmopUljFhVdvFhUgBFzGQ_p4_jDCTfNap74PzHxtXeHNWTH6aGbA457QG1qzWwV33saSRNayxMhF87I1qGuS9O7cxC0i41aUZew7Ci2TVVKmysAKv0ISPkGT00j7tSw6rZXebp9fOJMTxmkAsUaf7gHbkBeURqpXQZ3l5Q5h6Pat3p1gFW8afk9Zl6fpX7qYnOAALZABqhLuI2qL8_3qvkc7lOGOy88LmnIYbyVWmi0Ukuenk-MMHg9UhBxMTZteSnH2-z6MFC7lLG2wNda8eRgjSYVs_TmwnjybmVtVNzK3gf0yrE2zHCmk8I_bk5OCwhxk_44eckkKRecC_MFXVtRj5RnMj8P0HquXokOphMjlyqJ4-_GxEslLrnlvLq8zhg-_jcSKEhOa2qhDaw7U--sTiJaIwSrqYGY9yB1hedtROCwVhG-x7gnNf1nc9_hPjQCoB_HMq6qpgdixCgonFSYSonpGvTbIT4aty6jc9zgU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=cPwOCTSHqXI9UfErdtU2DUKtKM--MNkRxXuypV5hbIgBXYuI2XT6bHHt2BO0gzJu2s8Waq_167PCtV6gMmfK0Gmm-9aAJA9SCqfim2FKLw4ikhYIt8ZBGfaEHZTryGOO4p8vfvObYxZAziMKODdSuWOn_3vXa-Gu8hS_sSlQ1oKWF7tY2PVvHvq5N5MeR6RgmopUljFhVdvFhUgBFzGQ_p4_jDCTfNap74PzHxtXeHNWTH6aGbA457QG1qzWwV33saSRNayxMhF87I1qGuS9O7cxC0i41aUZew7Ci2TVVKmysAKv0ISPkGT00j7tSw6rZXebp9fOJMTxmkAsUaf7gHbkBeURqpXQZ3l5Q5h6Pat3p1gFW8afk9Zl6fpX7qYnOAALZABqhLuI2qL8_3qvkc7lOGOy88LmnIYbyVWmi0Ukuenk-MMHg9UhBxMTZteSnH2-z6MFC7lLG2wNda8eRgjSYVs_TmwnjybmVtVNzK3gf0yrE2zHCmk8I_bk5OCwhxk_44eckkKRecC_MFXVtRj5RnMj8P0HquXokOphMjlyqJ4-_GxEslLrnlvLq8zhg-_jcSKEhOa2qhDaw7U--sTiJaIwSrqYGY9yB1hedtROCwVhG-x7gnNf1nc9_hPjQCoB_HMq6qpgdixCgonFSYSonpGvTbIT4aty6jc9zgU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=UaTh7tNZQde6h9R2JMmGuriG-Swk0XCJfw5zAalaWYt0lCXbmSpKBsFs7pMVMqhRy_CINhtd8-WrjS1Avl7QIlUJIwHXpg6aeOUM_H2F5aY0TEDUYScjaDho6b9taAm2ElFdQH3veiW_IXKBjGVXOWD4OL6sDX9cvvHD-HQ_XV0YuAN-kEEQR4MrW9b50FHPgnnAVcDzPTibLx6pl5MNfCtwoC5tfMZRaZH-bc37V5spigAeQSqDEw78UJyo5hqqrlp5F3CvBQzt7YeStbxtgiFRMOGztyLv64ZDcnUkZfMEK5th090bF6VTMotMQUqkhSvgFh_mwHWFjplhml93GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=UaTh7tNZQde6h9R2JMmGuriG-Swk0XCJfw5zAalaWYt0lCXbmSpKBsFs7pMVMqhRy_CINhtd8-WrjS1Avl7QIlUJIwHXpg6aeOUM_H2F5aY0TEDUYScjaDho6b9taAm2ElFdQH3veiW_IXKBjGVXOWD4OL6sDX9cvvHD-HQ_XV0YuAN-kEEQR4MrW9b50FHPgnnAVcDzPTibLx6pl5MNfCtwoC5tfMZRaZH-bc37V5spigAeQSqDEw78UJyo5hqqrlp5F3CvBQzt7YeStbxtgiFRMOGztyLv64ZDcnUkZfMEK5th090bF6VTMotMQUqkhSvgFh_mwHWFjplhml93GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA8jgWaAVny45cKVZ6C8dA7fKKqARaEIuNX8aox7tHVImFoBiukR9f18xNofHqmQei_2bgJmEWpNBDvfDGP7_yHn9T5y5HA8kWrNZ87BuSIt4r7YqtofIUQcCw_F4pX-M8y_MxnTneYEmVIaSp9K854PoLaUEZUhXGPocuLOvLWAXDdgXagSIXqe5ms1tLMgIcG3blnBiTpPkcR1V_m2m4YZeBMPp5O-L90n8q8BvQExv6OGqOXf4UibU-7oUJ7_2-m6G9PzeHqOWxLYkqAvqAgcHYzpfoOEnScP_8qmQydUPKgzBhs2s5cv_wQzVyLKSewVWwQAN_8PYNrTGYd3KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=QfHK4-mBJnMO0GkK6I8svNjWngeEoathpoJmxs2Sq6q0fQ_CCBk47fFskAln9gbBY-RyNgcWMSlZOEq4PRzPkkqeYr7OR_bJqG4RErRz9E1R2VvuW2S7ltYRv6aE8Wn70pYbiuwVYMEajzLh-WtGMBgRmpjzP6g-iJ1iU9WlUraRkQSBuT_2auaPI8Kyg6acfAn1w9O4nKufh0A8sLUsOWsvbO-VvQejy2BUj8GbvUEVzh33b0xBvjK50cQaxyCTr5ix7A_OEVoz7Qgh32OIXaOOXQZzEw9X5WchkoNW7eGbQET47h34nZ6usYEKRPnmLhdI1ewedkI6a8YFDRvLXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=QfHK4-mBJnMO0GkK6I8svNjWngeEoathpoJmxs2Sq6q0fQ_CCBk47fFskAln9gbBY-RyNgcWMSlZOEq4PRzPkkqeYr7OR_bJqG4RErRz9E1R2VvuW2S7ltYRv6aE8Wn70pYbiuwVYMEajzLh-WtGMBgRmpjzP6g-iJ1iU9WlUraRkQSBuT_2auaPI8Kyg6acfAn1w9O4nKufh0A8sLUsOWsvbO-VvQejy2BUj8GbvUEVzh33b0xBvjK50cQaxyCTr5ix7A_OEVoz7Qgh32OIXaOOXQZzEw9X5WchkoNW7eGbQET47h34nZ6usYEKRPnmLhdI1ewedkI6a8YFDRvLXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hemSMiKoF6fxIjvLgL5ChumLrAT-8CXRG2IiujFX8l6W-UKpcaBKHt1Yrdw6NqTK2ShzTGP8QY-WzNeuvbajXgSpIA4z8DwA7QXhE1cIDFg5nuSfx0cy6OE0tp-cvqKovEk63hbm9WguM8-h0fW4UMZoe0-St7GzD0uJjFfMWy6wG5XWOtDbGbTYOdJvD2S2VwDdxZ0sx9vL5XnJ01DOVZmN4rYW8g6zszYmdwrnPktggQHwMf3EwLx9LPik8Py52UkUpCuPw6D24M_U__bkM9dHI_vxZT1CaNzFF86S6cBIV7VGDf67-xxcOP1fJqCDMaOWEW87RIiURhRgyHK7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=a4OPQ3losFUxQspI527e9fguFhLVBXZE5dRYO1c1vMDGVLAG65R0RbsCBPi0xA8iyNdkjmYmMp647KOQfrjQ6MyybJ7PZJ8s8-lbp0VmW8y2NKpO7jRTOrj0760-_Lj_fevJ6VcDp5iZz_BxxErTkGCkKWuaWelx2RT-kk7E7AnkXqODnEuhtKNjpEuYuhMVU2XfVWAG7j0F4XHkClZqnyCBjDaqDEDn03H8_blXEvm1rY40nC4nY6-Zv62hEGabv2ewKe8Fjx4yYkJRLCfRHXmj571ShkZJEfQKxpK7f9GrErU4yVVMKxGL0hwkEafHhDpVGbHu3oyEKY6CV_lvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=a4OPQ3losFUxQspI527e9fguFhLVBXZE5dRYO1c1vMDGVLAG65R0RbsCBPi0xA8iyNdkjmYmMp647KOQfrjQ6MyybJ7PZJ8s8-lbp0VmW8y2NKpO7jRTOrj0760-_Lj_fevJ6VcDp5iZz_BxxErTkGCkKWuaWelx2RT-kk7E7AnkXqODnEuhtKNjpEuYuhMVU2XfVWAG7j0F4XHkClZqnyCBjDaqDEDn03H8_blXEvm1rY40nC4nY6-Zv62hEGabv2ewKe8Fjx4yYkJRLCfRHXmj571ShkZJEfQKxpK7f9GrErU4yVVMKxGL0hwkEafHhDpVGbHu3oyEKY6CV_lvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=C_3lM7mOFbbbE4vh9Lle10e7CzB_sw_BUQVUjnR-rOrfY4jt4dnLWPc_jDrYecj59u3J-bHqwhYLY2uPItIASCr8T-HS693HuPEOwomhwPkxnj4qVExtFLyFw1nt5wrvP8QGebNHACU7_O8Q3LNADgYCs9WL5TMd8Bl6ldnuxKpmyXYacgfQ4U3HmQYfrDx6UIvossYrKwa5BFYStkh7RoiqseOzbIBuKOD8MMa0DxVd8q5--mB4Je1Pux52tf6110vE-rPvZsL8f9EDN9Z_7LQ16HewyUe7EdIJXx8MsrK4xhGt8i3I3X_q20bP5l6IsojtTOgtZd34Yw_yNvY2Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=C_3lM7mOFbbbE4vh9Lle10e7CzB_sw_BUQVUjnR-rOrfY4jt4dnLWPc_jDrYecj59u3J-bHqwhYLY2uPItIASCr8T-HS693HuPEOwomhwPkxnj4qVExtFLyFw1nt5wrvP8QGebNHACU7_O8Q3LNADgYCs9WL5TMd8Bl6ldnuxKpmyXYacgfQ4U3HmQYfrDx6UIvossYrKwa5BFYStkh7RoiqseOzbIBuKOD8MMa0DxVd8q5--mB4Je1Pux52tf6110vE-rPvZsL8f9EDN9Z_7LQ16HewyUe7EdIJXx8MsrK4xhGt8i3I3X_q20bP5l6IsojtTOgtZd34Yw_yNvY2Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJm-ae9SesmqTCneUv5aebXW9Sj2GidTyeUPmMT0LU91mURx8o4vlcRW8FHeYGixhG4-J_z9t-rCwGTUjrL1AhF9bahq6zqmzzO78yY0dWaWfEm5Yvesn1Pieu9fNcfnJVPuYC9k-kgQC9LC2tagtI9smHh3_Jq_BCx7NB5kK93a8500EzZaICmRTF1elQ9k8kwjC-900Pq8S7qjOLNQBLvPoa7s-iqWiIViGAOL4CFckvs2FfJeYfAzfmXQZerDkSgy8VnqJfPdJXLun6D43pVkcmGF8pn9zcMkJeQUNB_kwhRrVs5XpTR1ICPVdsGTI1ltlvx46Vwj8Txj18bm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=cL9bv-nNq-aSOIOC_oeLyn7ameAtAx_oZ1x_JQHgF0eGHPnvNmtzkGq4Dw4IK0b9wyrPE5EuzNuD8PwvtS-zXnGbtzDGtMzZmyShteNdXcT10YnN_XvCpKfebWl9_XvZdqneKvnAEMt4jefEPuynFSz_Q4l2RD9LdJML2SRxTzROvIlgyY7btygKGE1A1mMidnlcdEuBDyofyr9ArPznfwaylFCMS1kLvIhi7Dyg97wl8cd2B3aU5UK5p46QSQWc9M1bV47VJ_dqIG1hypHGttYQYonrErh0VxdEzCsXGLM57RKMq6tOsXxebackld2c4Uz9d9WL3izXb93OKK9aWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=cL9bv-nNq-aSOIOC_oeLyn7ameAtAx_oZ1x_JQHgF0eGHPnvNmtzkGq4Dw4IK0b9wyrPE5EuzNuD8PwvtS-zXnGbtzDGtMzZmyShteNdXcT10YnN_XvCpKfebWl9_XvZdqneKvnAEMt4jefEPuynFSz_Q4l2RD9LdJML2SRxTzROvIlgyY7btygKGE1A1mMidnlcdEuBDyofyr9ArPznfwaylFCMS1kLvIhi7Dyg97wl8cd2B3aU5UK5p46QSQWc9M1bV47VJ_dqIG1hypHGttYQYonrErh0VxdEzCsXGLM57RKMq6tOsXxebackld2c4Uz9d9WL3izXb93OKK9aWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVLMvCvVvzO6_iCOrggPK8ClSFHGEWD7OsYsDjrkYw6Gp6_eeGEWe1-Q9VY3W6NqCNjS_ueMGO-lu8Sx4wfTHoZo8kB36JGAxTwkjuCDKMTs9ZSIfRJ1PwLWr2Rx_i8bbYxaG4A6v_qKR2BpTfkj5vfx5uyRcwKpEqU7pghr1GQgHgK2w-kkcdpWEO-ywGWZ-uDptFDsQrv66m3MfDwnnDvuqq3QAkcgZJuTBNEXl79_9erX1-0EPKckVyVJru8ETIXEYxJO4pfk9WGlIX8fxaYCAzOZazTxlopzqnUpXclLsZqHNEvGu4rgEByAB6gNwq-QaJXncR6ibfN8aelwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNbSbTPo17gwjR0VV8RAFc-032gidk_kCW__lUxy7Tte4G-i8NNIHSQiSInZclTJOBHLqDkoA2S9qn3JDrT66w92lMpFk3vrZVjEKSYftkYpq3LYlItj2iG4rLvX7vFhG0_-crpswKZjlZZ4Oj7GJA2wBXFZSPSxyazlyutJtX5bQNRFEBwPepjR4D4EigiuMynN638JXBrGK6f0sbCIUGai4te1RAp05zRWXhOE9sbBpWqOVd6w_eVIGNZPSfLwWyRoGmjtygBKgeRNbUvGvNpJh4APdoXNtqEvH9pfY9delFrsPgO0BZaP7PNOn8mWX2vXu6V45J1lt_GSJRldvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBTvtBYSfbvAhbj57BxPRKC8gK4kbqWsBxw3SxoNXfEOrQIce3dSZSPZ21GlUbd2VwIZ2F7SYUVFd-kPZOJKXRMJTgvcg45EBNsoQ3asCQsHicDqWW1gAmXYltyl_yQo1Bup24_loAB3b5yMu8OlHLFwShBhb8x5SWMpJjP6LG5LmikTutJifspI-LiykYiXL1SyXk6U5SAbGOISfjwwvE5Yo2AGMfQnmoy2qLnRzuCWO7gMQxqL8pWLvF2kUTJwUtE1dTiYv9CYvxqhPYF2IKupHxRzqeTJK2uYniAI1YBaVVoVaa-aYYph7i0WClSYNo17p9Gqfu1JCebDOWj8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWMEdLiiBapP7Dq2rjRxZyR3uprOsLN97n72llDZU350BXjshg4WyNO6cRsSf29bjp9uE4ebm4u6j6JE9hyifIrfDHHQX7tUSayDA0eGPQ9AQgXvCJ6OYbXuTbvMGl0vgDzPTZZaYOXlr_21JznfpRkYNFPUOYVOO8lR4K9Wd3vP4-Al3bXXW0KAsBBZORsYZce8t9mLA5PoUwuiZCKxhiMYy_L9LtD2H7PA2Jgu-MipDqjNHh17E1R3MLWLqaFxrFr-7_cfo7J2GF1tys7XMLreznf4XunX58UZDjByFWwluLqYpn3cIwzjoxpCDZmJrLq2q86_7T41ZtO7zwMFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WddNlX5U5aWZClAA6pN8pPLL1-vEeWIklQmqFzlfSHBwJZvONUXTCsTsrIulAbmylHCDixGONNYiG_7gJ7_NYq8FywCAGABAIHFpcHy1niIYtGcog5Z0mtpROP0mKPaEAbzy12j4rR2mcS-LymOP5JdS5wgcs5lABTPD60v7fnm3dVuOfGs26tFjuu3VPouFLQ_7Hje6bZ4Ht7FgJrF6A9gciO0hchR1SJ8gWehGV21Egq4rLK5S6bZtK1QGjpXyj2FdHpPqw7fGSHiKyUF1av9XIPq8uqknJnYgESMzLg9tRQY2t1QuQff0ujpSkEU5OofD2IZ8znCMJeRPHXf7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxEe9pKjHSU3e6-rjZNDwlhTB2wSnEd-r9IHZRiJI_qZVbCX4aHOxwRxZavn8TryXVxRm-_d1ifXwmhyRcMfdUzhzkz9-tdTO-j7GfuxyStcnJXH87uan2Hh9RSeYzE3jRN9PdqqUdX355GXomplPFDSGnZCt8StQyfHKdwo71JBf46qoxibuSHK09P4LtHnsgdk7n8fkpwvW60qVECQGUm_lQ5hMHL_43EzavbOOIhOb5OGYXWuEy96fItN3RcDavWK2ngCj1f84uulLTqNxm7LfCWj90hn2_Pz5mQRlAMOeJjyhL-iCYQCVQ3_Z4Mqece2n6JF97ArV9vGjUpKVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=So5ytUCiuQfm6ErIwH_GvwUYZNVTAXUjz-pekIgrgJWJS_O2l7iplsX_0OsJUMJ9ZTArIhXgOi3K6XemTOSa_TD_rfPUdw51UgUxKOeEkLjNw0hjoucAmh31n9ZGm3vCB4vGS8dNdypD4b0Rfbmp_FuJ9oNHN-4B228eUIN0mvfEBbGst_xz9tz2FdwOMxYfGNAiIz2DIduNEBjuyLhawUNX2aDIcPNj_h4dpY5DvNlwh9QNPeMIZ0uZb7K0xzyesUtPPSV9i7VUR_vOy4gUfD41wlwC2Q8EUwICEtCFiHeDZCb7sZVOZMnMoU8M8sZmasPdp8HahYn7_y4sO70_BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=So5ytUCiuQfm6ErIwH_GvwUYZNVTAXUjz-pekIgrgJWJS_O2l7iplsX_0OsJUMJ9ZTArIhXgOi3K6XemTOSa_TD_rfPUdw51UgUxKOeEkLjNw0hjoucAmh31n9ZGm3vCB4vGS8dNdypD4b0Rfbmp_FuJ9oNHN-4B228eUIN0mvfEBbGst_xz9tz2FdwOMxYfGNAiIz2DIduNEBjuyLhawUNX2aDIcPNj_h4dpY5DvNlwh9QNPeMIZ0uZb7K0xzyesUtPPSV9i7VUR_vOy4gUfD41wlwC2Q8EUwICEtCFiHeDZCb7sZVOZMnMoU8M8sZmasPdp8HahYn7_y4sO70_BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQrgGv6BT9AUEq-uCznh0OzrxADGEX-3D_ETAk-RYtKT2mMlHo5rR4asxN6NTYheJ96jlgf7Q47UaLFpIN8iPtn6srWCHCmkr6UaOeUf8Mn4iZ5Ldwsqw0CdBmmgMhAho0GAvXo24x5_MglLcET8JnjVGfTFZOox8HgOqyZ1IgxIIIHpOjrHT1oYBGxDTcdrynlnDWkNzrY50w7AbgZcvrCdogoPKYalpZQQKUWcGY7hBV887emdUV052v6ypEb-iCYyEoCrQH2i00QVHIqnwXwVYOf9TfEVNf2BdV6TR4DGkHnIKUC2kAd_B9RgU3oeE1gAnJDhlDb7957FAfLaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ_ifvI_FMAqXWb6qQ5cLoCw-qcNH1h7YuS8ykGiUpGpGYUsihlwQTPFYsVhYKQ-P7TcXQASOkg9TPcaIQSYExY_nSbzGGkmeh_5TqRs6GvOHyWSgWKhW2EudwHaKXAE11UuwEqhBZ0FdvmyxxSdMT9dy2w1ozGcd6ag-PLIuV9SaUTtOaC17YgmQW2UHdFhD-IpS_S-Epr-Oi8hP_ZyxwEDpzkKW2AtgJwxeWXdMN-AcSFQdEcZU7aBGijRUinAwjGvMq5B5fXuFtYrG21OPn7oKdMdviO3vzPQY0rffYY2uTmg-v1K7HhXLgyYfK8kTxcwjZ_ORU2PU8Hle2fYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0MudmRMb3nSMiM9EshLstlwxCbrcArTxBDS3tuOAf4udsgO2rSK_ITHd4vrV8j01jAnbZkegNCHjIVES42ddABgWIUCMG2IKM6C_V_-NB-t8b0pPSUbrWWbUKuv5_n0nUqzUvmiGRdH2ScElYuZmn9q9icXfVmHnpm8OQEhZ0SCYIVojRr_2r0nf_AayRGAyhL202JRlCuuVBcVD_ery1AfAwvGTvujydeehuWbaBiWrPYsO_ePyWNCbBX9TeYZ3niIt6askOcuXqvP4tzMjkEmkPu24HsFtt0uCFMNhrrIERXQkZmGjkuHSqMZwbOmHMaq12LWDIFOlgTBHn7j1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrN5JXbJAbjJ7AmFt24hU5zOuSMeorYJ-Ku8NdPdTeUKa4Fw4Welp3mldyitiSkx3_38nqQG6tNDVM_PWLIw5WLaxYu2a6i5eDEU8f5cyUqME2UGdsxULoXnTpZUxeWrU8Il9UBBBqmoNZ70cqX6UISGqf5i_bAAVjqpG5yQYQRukmLk6hyIk0CvDdUHVj7Va01n41JEg5IqqWu0GqnCrJY22SjTwG6nRsLGhvd3vmGZ-WqCsGebzXB2SeXp7zjJX3IrcEznmSKEn-70Roq-CNbZs30tMQbo1Q2r8AosNDw_0Fui4ufzmIBYEsxYQobpJV-lzA8aJbxCH82rA498JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=Vf6YImMwwDtg_mTTKujEgYZOmkzdKdNKCPk1d_qiD_ir8wLcqxF4bDtZo74wRUZcwlHS07D8oAcuDbjvGNvErZBxSQK7DfhvirBH8szwIqcKb4sVRTwmKz-pMXvtfylVrY4cujq7ckouwxjXP8eEAWumZ5hDIneaISE43oLaZDTdD2toNshKV7UE28tYQXhOGuVBEJQV3iX4d6OEbCq65W7cQXvvDKaqA5Phczlo3b0BFM3g6qQ1PlJBirh4vj5yRg84ebu-6uJLSvDqGJp_gjHUw_4lf8YuAcSRjVkPaNVlRs72iwvsz3mnWbyrRrlkpMttGfZs6Qs0_PLnkDMzMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=Vf6YImMwwDtg_mTTKujEgYZOmkzdKdNKCPk1d_qiD_ir8wLcqxF4bDtZo74wRUZcwlHS07D8oAcuDbjvGNvErZBxSQK7DfhvirBH8szwIqcKb4sVRTwmKz-pMXvtfylVrY4cujq7ckouwxjXP8eEAWumZ5hDIneaISE43oLaZDTdD2toNshKV7UE28tYQXhOGuVBEJQV3iX4d6OEbCq65W7cQXvvDKaqA5Phczlo3b0BFM3g6qQ1PlJBirh4vj5yRg84ebu-6uJLSvDqGJp_gjHUw_4lf8YuAcSRjVkPaNVlRs72iwvsz3mnWbyrRrlkpMttGfZs6Qs0_PLnkDMzMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-xCQy7e50uXZX3CWcbVXfDJHf7p-pjvDYwyxCrVWjN33-zhFBqy6caW1sCYWv2eO32umdOdbll0njyisLz7JV64LqZEwqc8mVNCA9M9iTjzRsEXPLCKps63t48xI3cIGiBUFGA3P59wsxQwJ73LJfmMWBkkYED0wPnXGKwY9kwfxcxpmUUoWA1Laqz1gpJDQSe1HDDFBJoAN6gNQiqYqvXSTLVLQeuwjHPcW3aeRzLxXUwK4obySr0cQUBXQQxn7oMimGyLIZ9KQonwnmLIJU_ZXcAYD86CC1svdrezM1_d_4Zu3NFSFy_vZjTNRyye12y7Fb6_UOKzY-f2k6f-tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtHvyMZM-_LeSHbZolVuy1T7tfL-HToxXCni9LKIyl-I0p3lXJmA8iDKZ72nqcgvLV8sMUrlcGMBgJ8iOKW0yw7JHktaTDwJnZQ7D72Qkf5fJidZZTdYGH2v1Jdz6knir4yOZyJFQQHAvThzHvZFqrv822JeBhUf5dIA713mSqDlfwcdv8pZqrRd3Pjmg0VQGQDOXqAyHUv9jnySFLmlsOL3tOFFNIN3ZWyyux_KehwgAUFaZcxsxJBa4G_oE1O2gUjDqbbrFVoSJLdx49MxkLzYWNGZFlhcfmThjgZTND4B_MfYcmNA6BPu_tiO9JrB1sWhJQryRYtxbozWPNn30Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaQ8TCr2Q966nKTGaabpIqz0v6K0DMqMXYwChFHAxg9UTeK9RYS5ddFeSWW5-T7lrmT2bID-TKiD9CfA6bEejyTvlz4CddFFToD0Vs3ajKab02lEMhjgRTOYwSB5StOlcuIr5kze6CB0aw4cE0RyoYkGv3_qpVmf8mQc1GF18S9wF96Uky12xQw40jy_NDfFQLQULQRT7aTXWLncNmYSMRJ6cmUdDtNCVl-_E5iK-_QtVVEeu3EMx1YE-MA9RRbY23reJH6Twp0aotsG-HL4Fbq1f98hsfx0Ik2T1U6PRj_7EyjZfMGDmVRoZ8fdT36f9aoE-8fh-ognfwof0v6rLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa2L--enSI_Hdm4GQNMdqse5eoap3abzeFBXFneC3-kE2qjyhBhhnf22rwlKwpFqUJK243HFHYDjWhv6GCkyKQOhiq9biBQMYxYkhLRtIYRIkpXV7EjERWuCEypazJH4qIP7bIK34t1OEj7KdETUGPdeSek1EIi3837HW7n3EZo4QhAyaAdBjzBcqQgBB1gOmqkOT68LWcZXmLHcjDnTQJRRopzpmhvq44xcJKOYVZSsnihaX8OHWbXTYNDxc_BZO72UWF_1ebJQkVvFiHoQaMoG_YVgu07dQIh_lyI8BTaLRjJbkDAFM4Ckiu-xx8gZ-OCdTnleyexy_lSsSJidQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlTWAbmx81KXJ5NNjw4vRsIUiy3lrUG0eeG5Rk_GtPoc8Q01nT21F87nmBCYJB4LabZGdY28RZ9WQL_I1Xc-O00SyvMwY--80flSfL10BKeBe71Us8ObFeuAuap38mFgvzsK20fPkHCwgGY28n44_6MKAZEM4OIBbJeVTBEUwzj-T8SjobcX294b7YhJ4CMetCAXxs2OxzJKKT45y7c8y7ot1_zfqPXgJwDmyDGd9EfhEfDPoMKLl3sv63vxgWLWa4vff5VK1GTxD41cNmyyMW9VglS_kVbro9_BChLkxz76RYdMnyAEambRIc5ekvKy9n88Yly6NT0jQZMRFqDtQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw33yHsoeJSLW1f7LrwgFB_fSHXxDBt3SAs1ZDu86Io-90R9ZYK2SrwavZu_Yce4HSBP_NhNH8S6BBOdg4mmIJQDxBzBEW3C6woK5R6EB0eWIRIXhv_Icv7K-ms7gFg1LXXoJVJIrsiJrxRYa2kprlVlrsceOIBEQvDL79mFprwyweGEXnygAkFn_uKjXrjooFrueoI8uPH8JeX9lWcOpfskaaKH2ZAaaA6QG_qBnrifstIvZ1JnYpVLOpZ-kqH3r7PCEq_56LkU2Cwuv32TZyiYBd875kDKDZRk1_InqMnZNjj3N8oAjvTv4gOciXpjH9Pj_KjQ9OM20jSjBgT9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNYTI-l0aIUuyvGJP9E8SMYvN8ZOY6nQ9-TtMGPhnEqIeKA7n4x_l2Z3nSe0ZZDZqKco_ouexYV1BxXb4MkGLjURZJvraQ6G_TSNWvYMSKgzv86CauopVJg6YJ2l8Y05CVFm31Oha1_o-ogiat-tlymkva5UQ8YZJu_VOBIL-svg36Cu7j_2qCC0AY3Dxq5_B6mUuGJYkgbUk5YCQxITkFku897eFQGfz801WdA7mTTxUZpZnG1MEC8xRoeYXym3Eh6UDgVzrREQqB43K2B21pOJhtS4xfyaQPfyiplDWBcWkLogBnsMCTt4UjX6kmJw30f2iI3Q5s_Q98hRMP6HYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TboFJwEeEB41zNBaj2FCUcKh66NoNarFK9Z913btAU7VRdqzblkF5p0kkjYcrZ2qCdj1wdY-zSU1zveynsAwAC2yylZfWSBbQL4WY5OJVqhlH-ToHKJR8IAz_Qkd6seo3AZribVvIxYjR-KH37mC910jISYm-Mmj0iYqGhDwPNbSBhoMT-cGEfOn0-WzwbfsLYndvIr0U7uygPmnyprhHI45SApKUVdoxCV1NF5VBlnbBCYKEo_6hLYmVntNEYg8PA4IilzH_WRFuJVSxoCg0k-8fMLYZz6RRIdoC_QyRxolk0jhavP0-FYklNSdD-LRApEb-IzwlVSvQGojWPdZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
