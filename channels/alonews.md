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
<img src="https://cdn4.telesco.pe/file/e6jl1dYsBZ9azK4PTMlG0qUNCGQ0njZ7HlM0oKxDhUrMXUwMpt50G8-4V5QwQ2UFpHcd2Gvpgw9E1-gMcman9ooMshQQumGURn1educ4WY4HuCGOOXd8YDpDBs1mNcznSCAQUw7WyUrc8B-RM7zHtBZEaLYFKnAVOLymFU26MD-fSQXV22aFwzCsWRz1xeFK1DmSV-9uT3owYeHUfQwM5iIwKSyghDSFM56Iwxnu6AmgV5kfLR0jm95-WyOKR9OVW3QqRQlzCrEIC_Dqaej5HOCpgvwk-PneUKFDXPFl00_dFWq2lzaHYSPxBM7rdS7IyQ9ih48DqJApWvYy3XO_eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 21:22:53</div>
<hr>

<div class="tg-post" id="msg-126920">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcqiinN_MStmKeUnoepd1gs1aFvcjpqQanz5WpC4VV8tbQJm5I-DWCZd7PFzq-c22b_jcxyJ2vfIFinANTIWLYym5Mgm6d6AYvCsCncNS-n9JmO4j1fS83pfrsmwxmv-ZXYCGhazULaRCyWiQG5r2G9R46_Du9TTS75ycuCQBz4wVQ3-9SLH0SeRlVPqDg37pk7du2JjryX5a1URjXI_Rp78yS04OwMSIlpBd5B4MGLsSY9Dan4uZuVnDJfHHIv_OVRBHLXM4KMCn_m6ErbVUUlLCFJe3nOtn6tOS21JIKEFyvfqVkbKmh3r3Rc-K-L3h4b7v9M9OBVLDI4mK4C65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یدونه هواپیما ترابری C-5M Super Galaxy هم از اروپا حرکت کرده بود الان تو آسمان عربستانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/126920" target="_blank">📅 21:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126919">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYDgPwC8-URECFw4zXhFjuV-AwEwhSU1KfYnHUeWi13PkX8v7-Q1EW7IVFYTLeaxH9th4HjUNloXB051iiicM3iZUbquAbD349Nc1ZvRR4dITcRrR2ic1d6xXSh5I30Uz_r2Ogc3F8Q3if2Zcf1eGIO02cCy7dfNIpUq7Cp3Sc5aRhGJZuU2lHlALNBpDgsoo87o5tFdqdLLJA0fbwJp3YiIxzCCt6pKcoZkwFQ9Vm2rlYbKD8tGWcYLDNFfuT9pf64ob_8MH7v7rbisWNdlLEF6LLQmCOcyBL7BOW3bxMamnNJ-Mgn1wioaV3AzCa2WaCK6RtJbXXeksctCkUYsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون یک فروند بمب‌افکن B-52 در حال پرواز بر فراز عربستان و حرکت به سمت خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/126919" target="_blank">📅 21:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126918">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuEPI0SnjE37mnLmmozkXxPvNjtq56cgfo-ImlJzf6Y4q0ChvzD13x0I2Tg612pEHekiMNvwL5-rQmLJRkwgcg9xcG8MdZ55tSyANHr_YRnGWHrt0aYcYxbWcIFon7Smuw-8i9UQSGI2Ks45jRDlgGgEv-UfwHm-OqCmefkLeoce5-IZICTTsEINwifHpO4hvT1VxIzqh5XD5-s6OioExJdGKg_FTKuA1BK051mn3evHskUWrEZdJil7xhlA38kvn-u9IRdG4BLE9y5GGlYJGlsw0Gv8DiQIzsoTm3VpsJb5G1KJrZACWYRRbSyYPjQM4xmCPVYxVoywcUI6Njva4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: تبریک به نیکول پاشینیان برای پیروزی قاطع او در انتخابات ملی ارمنستان. من بسیار افتخار می‌کنم که از او برای انتخاب مجدد حمایت کرده‌ام و شک ندارم که با او به عنوان رهبر کشور زیبای ارمنستان، به سطوحی از بزرگی و موفقیت فراتر از هر انتظاری دست خواهد یافت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/126918" target="_blank">📅 21:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126917">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر انرژی آمریکا رایت، در پاسخ به سوال درباره اظهارات ترامپ، می‌گوید از خارج کردن نفت از ایران توسط آمریکا مطلع نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/126917" target="_blank">📅 21:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126916">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آکسیوس: ترامپ پس از سرنگونی یک هلیکوپتر آمریکایی، حمله به ایران را دستور داد، اما مقامات می‌گویند خشم او به دلیل عدم پاسخ تهران به آخرین پیشنهادش، تقریباً دو هفته بود که در حال افزایش بود.
🔴
این حملات طوری طراحی شده بودند که بدون ایجاد تلفات انسانی یا به هم ریختن دیپلماسی، اهرم فشار را بازگردانند.
🔴
حتی در حالی که نیروهای آمریکایی به سیستم‌های نظامی ایران حمله می‌کردند، میانجی‌گران قطری گفتگوهای خود را برای احیای مذاکرات ادامه دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/126916" target="_blank">📅 21:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126915">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OXf5ykOiy_NGJnpMc8ccSA_G0wBpWGDJqij-qbU7MFP99qTbuD99tOhz0ZdeJjAf1Zq79jo58Zz13bs307JWb8zwAWCDdfxJSFZXa6A7Epzk7LTZHr07Ni100KC-dl3Z5RdNWryJxn2E7SKt1gOi8-IrlS71oHEzJLFDb252tWhNwM8JqSJlSNcLRxlevWemi4rBAIy6I5mn0H7swdxAjBB4YiJwO-axWG7YzKmSV7CnG4oJr4H_HvaWjGB8p2hM2aQoP705MWq0YYfXPSE7M6lGpDzG2JtUVzAkNFWjDgm8FRSkI_xMbSC1so2ML7JXSpZwniehjX7KswIYrkh49hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62accbae38.mp4?token=hSHhhZDfzryubIIzidid18OGIMqyJ3ELEPBHHySjH50Ar3kYNDN2H_Nw4pQl3QigrKsA7n20I3_ZCcrhJRz52nCklomMF7DMysTvazKw11el25Uqt9OmKon5fGx-vHxCnIL_FBugoY1Mr-rZA6fvOFk5Kq8UZNlbi5iJRuObY9Z--Kx4_pFbYFcFMhCnHT3m66DvFaUfU6apWWuacOpEOhHnNmKEOfKyFNyuOtbbULelJSRkAGVM-7zzYvsSGPNYfIcdPyKhA4UxLVgLiQCGbwAxlDzniLJZK4NG7TS481qE2eFEUDu039LbciRa2XwSX8GhqZiLmRwm8-H5HX_3OXf5ykOiy_NGJnpMc8ccSA_G0wBpWGDJqij-qbU7MFP99qTbuD99tOhz0ZdeJjAf1Zq79jo58Zz13bs307JWb8zwAWCDdfxJSFZXa6A7Epzk7LTZHr07Ni100KC-dl3Z5RdNWryJxn2E7SKt1gOi8-IrlS71oHEzJLFDb252tWhNwM8JqSJlSNcLRxlevWemi4rBAIy6I5mn0H7swdxAjBB4YiJwO-axWG7YzKmSV7CnG4oJr4H_HvaWjGB8p2hM2aQoP705MWq0YYfXPSE7M6lGpDzG2JtUVzAkNFWjDgm8FRSkI_xMbSC1so2ML7JXSpZwniehjX7KswIYrkh49hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه i24News : انتظار می‌رود ایالات متحده در ساعات آینده حملاتی را علیه طیف گسترده‌ تری از اهداف ایرانی انجام دهد که دامنه آن از حملات شب گذشته فراتر خواهد رفت
🔴
هدف از این حملات ارسال پیامی به تهران برای ارائه پاسخ فوری در مورد توافق پیشنهادی روی میز است و به معنای بازگشت به یک جنگ تمام‌ عیار نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/126915" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126914">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKKGtmS0pYOtBh8GKhixKLX0ttjgDszBNVYR1IFrb2oVBgIBWLMLf1RpUAYk5w8KkJ_PbbDyn8xmDxgoYcQduAslridqshYKz3px9BSnpaJTsz-6PIVl7SRT8-aSjt59IqoUC9F3-sXT6lffzVpqvG-ZmDpkgYn8lt98kEGZ5iUhEtQ7XuER2T_Chyjn9yOBnIa0gjBDu2BubK8ONxt_Cq0rDyQGXAADUpKXEVZnE-LJrET_50dW_KrsuMfEe4Wpys8QZb4h7GzAMCpBTY_nmzibE575E7jJ7kBN2ZQsL_Mhl7H7EuLPMbxrcIn4exVhwteWPq2MEOjPw8DjQcY2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر آمریکا تو اسرائیل هاکبی :
احتمالاً اوضاع تو منطقه به‌زودی یه کم داغ و ملتهب می‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/126914" target="_blank">📅 20:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ خطاب به سازمان رادیو و تلویزیون اسرائیل: ما در حال پیشرفت عالی با ایران هستیم
🔴
بدون من، اسرائیل وجود نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/126913" target="_blank">📅 20:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا چند فرد و نهاد ایرانی و چینی را به فهرست تحریم‌های خود علیه ایران افزود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/126912" target="_blank">📅 20:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDwAs3Fsimj9vzEzEeeTAmQPfGHVIOH44qSfNGQb2syZdKXtjVj-4T1wdGNUEL48i89k_ZXlJvUefkEGWE0SmDALakk6pl9CO_-64LjbUmEui5wk_t6GUsHxrYmCjZ0ha19P_KI1ncchEmXvD66tReKEdsUBD81Khax40v-Vl4jsXOnTpMZA381CTNvk-Zn2WOFGap6TKisuFpUCnvsoLVgZDLAo8sn1XrBdlA0CLDc9qv1_g_kBBWEX4izXuowQ59hQQ8Cou0NKNzIRvMTe8DN1wCH9mi8ze0EfZvUyC7cNfo71w4dn7WaiiQvhF_VnIFnwm9Bq613OWZ3fe42wug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون / آتش‌سوزی در انبار کالا در میدان قیام
🔴
انبار فرش ، جنب پمپ بنزین پل ری!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126911" target="_blank">📅 20:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
حنظله تهدید کرد !
🔴
گروه هکری حنظله: به تفنگداران دریایی آمریکا توصیه می‌کنیم همین حالا با خانواده‌های خود تماس بگیرند و خداحافظی کنند
🔴
موشک‌ها آمادهٔ شلیک هستند و «حنظله» منتظر یک حماقت از سوی شماست. ضربهٔ ساعت‌های آینده تلخ خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/126910" target="_blank">📅 20:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آتش سوزی وسیع خیابان قیام تهران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126909" target="_blank">📅 20:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GARPYx6-t_uTUX6h8QM4ntTfjDT7uKb_bO8TmRE6cAiB6Jq5z2FRgnQMz95kq8IVVXJbbIRNLKhA1bmPGTQJiZ-xg58wZo4pPwDNMB4pO647uOJj7vhLJS9UNEDrY6oEGyXcIaFu3VkYxDVbffec8YN6KeJd8QNuKAX5sVzbu7NlTDVVBOnPxDQkLYfP6DgVv8i79MNzqvucFzYWq16KMF-pK7LzrYagkL_QjkQ_b8t70SvLDBGBePZqfn_iI2lXY_wy5BStQFBrv5LTZQvXxIzfSAqmTKjkARA-n5YIo3NOl0uw0YFK5zo0MBBJPvw5vqllQhERbV9EuBAzxdGB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش سوزی وسیع خیابان قیام تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126908" target="_blank">📅 20:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMIi1B3V0UdgUTKPzXv2tvCw7bWz7FwZyZZZmAM8bU-pdeFOx2Gu7UAIwUVUgIUviJdTUqZtbjNYBacBvyUngBKDSfRT1TyYvnZjXAUKxyxYi2YDG4LdxtZRfALEANJmMtGHy3mMbgJJpOFrA6QozSNt9VnpZufid0J2y5bjyspRrJCVnLuXLX4EKJnuuf9mIn8SAxHeN8QultDfW1gx6bNQeYU3yqpHiEkeRB96exn3BjjGCulKMPa11Qh3zYk8KWMgIc3GgfzRDxaIWKQ67QrskDfqqmJDXkEekzFjYDrugYjMUQ6qiOazLE_9Ult__ZLvDPFCBHMw1jgk9fzNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: زیرساخت‌های حیاتی شریان حیات مردم هستند. تهدید به هدف قرار دادن آن‌ها — از شبکه‌های حمل‌ونقل تا صنایع برق و آب — نشانه قدرت نیست، بلکه نشانه‌ای از ناامیدی در برابر اراده یک ملت است.
🔴
ایران، با تکیه بر دانش و توانایی متخصصان خود، وحدت ملی و همبستگی، در برابر هرگونه فشار یا تهدید استوار خواهد ایستاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126907" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پیت‌ هگستث در خلیج گوانتانامو:
ما به دنبال دشمنان نیستیم. ما به دنبال دشمنان نیستیم. ما یک دوست بزرگ هستیم.
🔴
و امیدواریم به زودی بتوانیم دوست رهبری دولت کوبا باشیم.
🔴
ایران باید بداند که به ما بیشتر چالش ایجاد کند، کار نادانی است
🔴
من همین الان وارد یک قایق مواد مخدر در کارائیب یا اقیانوس آرام شرقی می‌شوم.
چون ما شما را شکار می‌کنیم همان‌طور که القاعده و داعش را در خاورمیانه شکار کردیم
🔴
در حال حاضر، حملات دفاعی برای اطمینان از محافظت از مردم ما.
🔴
باز هم، برای ایران غیرعقلانی خواهد بود که ما را بیشتر به چالش بکشد.
🔴
رئیس‌جمهور ترامپ به دنبال یک توافق است، اما نه فقط یک توافق، بلکه یک توافق بزرگ به نمایندگی از مردم آمریکایی تا اینکه ایران هرگز به سلاح هسته‌ای دست نیابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126906" target="_blank">📅 20:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
تسنیم: ترامپ باز هم از ضربات کوبنده ایران عبرت نگرفته است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126905" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126902">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upWM9mbyFi4wHELWN-WqycOz4VgnSgvmQv2TmWDjxvEAhmudHvixXEeLmcM3p_RYB15HfXA-3R5RSQWsZGHK9QBfFkOHLH6LMKc0QNDeDQA3Is6upXFqJnspFItbtZCCO_9gpPSpcJdNsbV6xtMwQRkiBfPHv2QQW2OnOl13UgPercmu5_ZqBZwEe9bGCiT1m7EU-0BWzYGYyX9yPni1GL9FsYSVhZxqbom-m3RwwYd9PCrFQCyG0YkUk8F9cocoPEv9rKKME48tDx8oyE0j1jWDUsKBlfa_YyvTwvoOiRWWsamnYw2Gdl1en_3ERGz2r2-T83CWohCR691boBkW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19a799ca2.mp4?token=U9hXRLyK_pXh-6IB0YzwmFbj2nUymZK7cjljGo1wxMhs_XJvTPhX41vjJSCs3LWzA_AdkM8mkIEgwxhi9W5n7A_nvlT-zMLIB5FPlwWCd21k4LRXUggZQ6pf6qf9rVYXMgcuXX6zWXmUVlTyWFqm69FKEFUk1LlcREcjmfuABxAsapYAy_vJ7F6aLCXiKzKCwHKYBZLNBUtRkO7Selhyd4hu8bPw1VCXJ8deDL3jDBH6sDr73d2SHtk3rQq-x233b1AsRkvz193404kci7rBTFP373gtdxX2Jk-DhVpzOaE04q0OxD_9V_Qq6Tz96rpsxh-E561cVFbnR0xkgE-mYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19a799ca2.mp4?token=U9hXRLyK_pXh-6IB0YzwmFbj2nUymZK7cjljGo1wxMhs_XJvTPhX41vjJSCs3LWzA_AdkM8mkIEgwxhi9W5n7A_nvlT-zMLIB5FPlwWCd21k4LRXUggZQ6pf6qf9rVYXMgcuXX6zWXmUVlTyWFqm69FKEFUk1LlcREcjmfuABxAsapYAy_vJ7F6aLCXiKzKCwHKYBZLNBUtRkO7Selhyd4hu8bPw1VCXJ8deDL3jDBH6sDr73d2SHtk3rQq-x233b1AsRkvz193404kci7rBTFP373gtdxX2Jk-DhVpzOaE04q0OxD_9V_Qq6Tz96rpsxh-E561cVFbnR0xkgE-mYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126902" target="_blank">📅 20:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126901">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126901" target="_blank">📅 20:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126900">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: هند معاون رئیس هیئت دیپلماتیک آمریکا در دهلی نو را در پی حمله به یک نفتکش در نزدیکی سواحل عمان احضار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126900" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126899">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی ایالات متحده: از زمان آغاز محاصره تنگه هرمز، تاکنون مسیر ۸ کشتی را مختل و ۱۳۴ کشتی را تغییر مسیر داده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126899" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126898">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
قطعی آب سیریک پس از حمله آمریکا در ‌‌۱۲ ساعت وصل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126898" target="_blank">📅 20:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126897">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwW8OYzYFnWzmGZN_zYHlRCZsQrvvPeMuL7b4GCpw90RS1PAk1p88wbgMwTR09t-UzuNEOmc3leas-TY_j7McI9LhwVw9oQdp7zNDxKIwm8-p7YEbocywGatCWq7sdkd2U56gszR8IfaON00KT1CtfZkrwBpRPgYUFJla44rObugC7dnaDIxcFEPCBlt5tfWiE-CrFU3xrXQi24-uQ2dqPtltc3yxl5cEGG1HgA9PNTYlk4fht5HuuFi4dIlTKT2Bq7Y3Bxd_KTEwbGvVEds1YYdhoL9CSnHzngtsBPE88oOVRLvLMmzswvdsilcOLhCaL0VY2KRJQ27K_QRBdZZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/یدونه B52 داره میاد خاورمیانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126897" target="_blank">📅 20:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126896">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf0c94043.mp4?token=klSi4dvTO9QsnO3S-z6tfgAvFBtIOEQ4P5SF5eGe-Wb3Hm224uCdx4NH24ZJD28atdqVd2EJyGPvcbZNVY9Gu83XiYIePsIuesWIoSNByD7zkLoAXTA6Yzavawp3UJM1CBKi_QVSujfiys-mTWJphPFPYMAXjIY124WnTZMokVhn9K-5kqYuejvVmAl3OSiDnA24giWStgF8bK91sn5oSeEOzTMu0WLnQLsoex24tmtRQA6XCzOdhWOfUHPuCkWIW7QCz0yZN3sVZLj0K705sPOGNVLojv0PkbwMwP6CtmGyomTlw9ayuN7PUlA9DfUuZ8137G0ymNl7GJLtbRMUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf0c94043.mp4?token=klSi4dvTO9QsnO3S-z6tfgAvFBtIOEQ4P5SF5eGe-Wb3Hm224uCdx4NH24ZJD28atdqVd2EJyGPvcbZNVY9Gu83XiYIePsIuesWIoSNByD7zkLoAXTA6Yzavawp3UJM1CBKi_QVSujfiys-mTWJphPFPYMAXjIY124WnTZMokVhn9K-5kqYuejvVmAl3OSiDnA24giWStgF8bK91sn5oSeEOzTMu0WLnQLsoex24tmtRQA6XCzOdhWOfUHPuCkWIW7QCz0yZN3sVZLj0K705sPOGNVLojv0PkbwMwP6CtmGyomTlw9ayuN7PUlA9DfUuZ8137G0ymNl7GJLtbRMUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی خضریان، عضو کمیسیون امنیت ملی مجلس: براساس اطلاعات دقیق و میدانی، تعداد کشته‌های ارتش آمریکا تا به امروز ۵۰۰ نفر بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126896" target="_blank">📅 20:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126895">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ac1b45c2.mp4?token=RjBtPoPTn4QnimgLSEV4aEbAhHApR9VwTEeHMDwUiYawo9vhGgywM-Uwl6VTAafNVItUNkfOAGX_-M51XLnm-2LWdEDLEFBLuIMeI6UplTZEPHFDU4x4rq_tk8dHPcHoxbh6uINc8bUOdER13mDzl7c-ZVAG7Ykn2666YPQKQNqMeUgikzZiH4tSKeYxuDhwACBuIHxKyoarDeWHG48_wcEH8OF63prid3sLAauRus9Tt5oXclTuu5XwcGRj3-IVasXWkkaVmLh_veOXa7JU9dk9BCNP6LrHzpeJhuyPeDzSe48AXqETGj1Uks_gJkXbnSFgUDT8fpP9I3tLhiUaeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ac1b45c2.mp4?token=RjBtPoPTn4QnimgLSEV4aEbAhHApR9VwTEeHMDwUiYawo9vhGgywM-Uwl6VTAafNVItUNkfOAGX_-M51XLnm-2LWdEDLEFBLuIMeI6UplTZEPHFDU4x4rq_tk8dHPcHoxbh6uINc8bUOdER13mDzl7c-ZVAG7Ykn2666YPQKQNqMeUgikzZiH4tSKeYxuDhwACBuIHxKyoarDeWHG48_wcEH8OF63prid3sLAauRus9Tt5oXclTuu5XwcGRj3-IVasXWkkaVmLh_veOXa7JU9dk9BCNP6LrHzpeJhuyPeDzSe48AXqETGj1Uks_gJkXbnSFgUDT8fpP9I3tLhiUaeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: ساعت 11:14 شب در 9 ژوئن، پس از اینکه کشتی دیگری با تلاش برای انتقال نفت از ایران، محاصره جاری را نقض کرد، نیروهای آمریکایی برای دومین روز متوالی یک نفتکش را در خلیج عمان از کار انداختند.
🔴
فرماندهی مرکزی ایالات متحده (CENTCOM) M/T Settebello با پرچم پالائو را هنگام عبور از خلیج عمان غیرفعال کرد.
🔴
پس از اینکه خدمه بارها از دستورات نیروهای آمریکایی پیروی نکردند، یک هواپیمای آمریکایی مهمات دقیق را به سمت موتورخانه کشتی شلیک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126895" target="_blank">📅 20:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126894">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeafbbbb61.mp4?token=IgbJlcHxWncm8aWqc7rCkf2bKcVJ3-TdGoOfDMWWrqltJwCR_rcY9pFvdEmX3FWZxb4qnuU3Y8eC5YEJhNUuQBwjtjRSDar1W8Ydy3DVcZHYQKHNsJR3ty9ucM-ZBNKrMy7li0gc6T5RPn0mK4ozJfQThrtw7k576plVKISDH_whtmf60p9HbsJlfIM0XF5_zo_t3nvT56joeU6MdcClmmWyRZVQ0SqMdDpdwH35tsRaP5SuOPOuL61yeXSfEVDHn24Ex7T4kt3w8W_l7LdotMQWPQ_pQuPA2irc990yM8vCqHSLsO1AJhgQ3k2WcMgKg1JYI4NahEESK6R9cl9Mmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeafbbbb61.mp4?token=IgbJlcHxWncm8aWqc7rCkf2bKcVJ3-TdGoOfDMWWrqltJwCR_rcY9pFvdEmX3FWZxb4qnuU3Y8eC5YEJhNUuQBwjtjRSDar1W8Ydy3DVcZHYQKHNsJR3ty9ucM-ZBNKrMy7li0gc6T5RPn0mK4ozJfQThrtw7k576plVKISDH_whtmf60p9HbsJlfIM0XF5_zo_t3nvT56joeU6MdcClmmWyRZVQ0SqMdDpdwH35tsRaP5SuOPOuL61yeXSfEVDHn24Ex7T4kt3w8W_l7LdotMQWPQ_pQuPA2irc990yM8vCqHSLsO1AJhgQ3k2WcMgKg1JYI4NahEESK6R9cl9Mmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: برخی افراد نگرانند که دریافت ویزا برای جام جهانی روز به روز سخت‌تر خواهد شد.
🔴
پرزیدنت ترامپ: ما بسیار نزدیک با هم کار می‌کنیم تا مطمئن شویم افراد درست وارد کشور ما می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126894" target="_blank">📅 19:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126893">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=VseYi9n7kmalkpN1EuiqN9BcWbnAiDohEz8aG2UJFa7-iH2_dU4PkwRmahMB8p2VcmZa5r4hL1DXGVHLuLXWww-VjP5SDCPVI6qXib7r7WUWN6NcstG0iKXvKc5cXkAuokJTE8lFOEfs5SJqhhGGNUEGSnttH2Ols2dFTWkXesuF9RJo6A8iZWU3yZQvLQ0t51G6602QiR8OtB-WdfYYVucqEa9Q5BmToDNdK1Y1U1Qq06QJQ9BO7ByvLYLZLwAiaVUtJCiuwUMQaHRwmG3QV3RBaILx_9ODy8dTsL1YIy7wMSZ9mbSSnuRE4T1D8czE2jx-8AQ0TPXZS_joAi8_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c4b4da62.mp4?token=VseYi9n7kmalkpN1EuiqN9BcWbnAiDohEz8aG2UJFa7-iH2_dU4PkwRmahMB8p2VcmZa5r4hL1DXGVHLuLXWww-VjP5SDCPVI6qXib7r7WUWN6NcstG0iKXvKc5cXkAuokJTE8lFOEfs5SJqhhGGNUEGSnttH2Ols2dFTWkXesuF9RJo6A8iZWU3yZQvLQ0t51G6602QiR8OtB-WdfYYVucqEa9Q5BmToDNdK1Y1U1Qq06QJQ9BO7ByvLYLZLwAiaVUtJCiuwUMQaHRwmG3QV3RBaILx_9ODy8dTsL1YIy7wMSZ9mbSSnuRE4T1D8czE2jx-8AQ0TPXZS_joAi8_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي ایران و پاکستان
:
من به درخواست پاکستان به آن‌ها (تهران) فرصتی دادم. مارشال میدان و نخست‌وزیر پاکستان افراد بزرگی هستند.
🔴
ما مانع از جنگ آن‌ها با هند شدیم
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126893" target="_blank">📅 19:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126892">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: وقتی جنگ تمام شود، تورم مانند سنگ پایین خواهد آمد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126892" target="_blank">📅 19:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126891">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ: ما میلیون‌ها بشکه نفت را خارج کرده‌ایم، که امروز برای اولین بار اعلام می‌کنم، اما ما قبلاً میلیون‌ها بشکه نفت را خارج کرده بودیم. هر شب نفت را خارج می‌کردیم.
🔴
اما حالا می‌خواهم به شما بگویم چون ایران تازه متوجه شده است. حالا که فهمیده‌اند، می‌توانم به شما بگویم. برای من خیلی سخت بود. خیلی می‌خواستم بگویم، اما نمی‌خواستم خرابش کنم.
🔴
میلیون‌ها بشکه نفت خارج شده است و به همین دلیل است که قیمت نفت ۸۵ تا ۹۰ دلار به ازای هر بشکه است نه ۲۵۰ دلار.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126891" target="_blank">📅 19:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126890">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ : این یه مسیر برای رسیدن به سلاح هسته‌ای بود
🔴
اونا تو دوره اون در حال توسعه سلاح هسته‌ای بودن
🔴
اگه سلاح هسته‌ای داشتن دیگه اسرائیلی وجود نداشت خاورمیانه‌ای هم نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126890" target="_blank">📅 19:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126889">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdcf6ef687.mp4?token=OJs8H6dlqLbmfDjdSKnIwxAnoMpRyijFNsSfDr5UY0ARsyKFojuExxF2NojzYOGN7WDrrsHy9ToccTXkaszYWnrTQtokzZj1pnZm7Ic6Wt9Byg796Rw16XkjOD39S2u7fibznWRw2nyWLqo-Oi_uthUl7foBXoDYJTfJbiC4aKcsel3wGYiRZ-rriTx-W6cqrh8Dl6WgWyrRj9HFJY94EKCuKtAMOS6JdHNMQrz2tV94Z-Amt4s-j4kxG0wgVTfyNNduBW7LIWHbuliszIhhGSoF0ddNqPGyj0QU8qHMfwuo4h04mcdmYsMe0yduNznckzc8YoR32WJspcZahPOZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdcf6ef687.mp4?token=OJs8H6dlqLbmfDjdSKnIwxAnoMpRyijFNsSfDr5UY0ARsyKFojuExxF2NojzYOGN7WDrrsHy9ToccTXkaszYWnrTQtokzZj1pnZm7Ic6Wt9Byg796Rw16XkjOD39S2u7fibznWRw2nyWLqo-Oi_uthUl7foBXoDYJTfJbiC4aKcsel3wGYiRZ-rriTx-W6cqrh8Dl6WgWyrRj9HFJY94EKCuKtAMOS6JdHNMQrz2tV94Z-Amt4s-j4kxG0wgVTfyNNduBW7LIWHbuliszIhhGSoF0ddNqPGyj0QU8qHMfwuo4h04mcdmYsMe0yduNznckzc8YoR32WJspcZahPOZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : فکر میکنم اونها میخوان مذاکره کنند...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126889" target="_blank">📅 19:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126888">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ: ونزوئلا به یک کشور شاد تبدیل شده است، باور بکنید یا نکنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126888" target="_blank">📅 19:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126887">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: ما با بمب‌افکن‌های B-2 به ایران حمله می کنیم
🔴
میلیون‌ها بشکه نفت ایران را بر میداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126887" target="_blank">📅 19:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126886">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecrl0SHddJF1DR7aUUJAJBic0mjuv4cCV_p0tOz2RiB5VWQ2_4_RlxjPKYE3Do7prL4XpFw-zVRXDJzciJGR9A31As8tVho8vxEq9dSiI98GjPjSGmPkDxO0PDF2GW3d9cL4VqrdFY-0ztiQxKrPziVjFWtvwcErW2GTDOgdrIUQuufYZ5jDtl5jHhxgNf_I_D-7d5wCuetSumG2mHKBwjiU0_raaGOzmeI89dR92HQDAryp4i3hhmp79Pn9OepYxRUKDJ1tFdKqiJrVjM1wzbnp_0RvB_jFPOAk_YAtim_G1UhH4V-UREMdU10YcVh-uDrkHZg_OUhqyoSES-zbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
اینترنت رو قطع کنید تا دیر نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126886" target="_blank">📅 19:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126885">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: ایران وقت‌کشی می‌کند و من می‌گویم چند روز دیگر هم به آن‌ها فرصت بدهیم، اما آن‌ها همچنان به تعلل و وقت‌کشی ادامه می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126885" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126884">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: شب گذشته ۲۲ کشتی ایرانی را منهدم کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126884" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126883">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80f48c832.mp4?token=bLm22ARbJlvGhmEhcYgH01835zC6LSpagWlEp60idRW5pv-0PB0HiTWWQ1q4lOlCpbxsiRiaxVNvCehP2aD9I_W0IgY24P3MdKQ2K6ssO34ZjG_iBtmGS-3isDgXDl-0VnNf8fcabFOpLVg82hnLZl7ynpNwmsKDLzhSa7UDkA9NwyAlL2v8f3PutOHwxLa6GyrM0kAGwStSX-nPxDd67DN5AS_rJsgYQxkp6R0vP5wXOG6V-LS69OBX4XEMFc4G0QPp0e9zK2d4CCj6YGeapih_DckvXifGaR_fSkR54x38LeCRQgj9QRHRE7kOFOXoGmtsueyTXQva_DPz8iNtDCXI6rga6Q7ER-858OdvRPnjvCemiL3BFRVPck0M4neWzC9-6iPzP40QA-rVZvbZ1V6qkhcy5sL8llc-iTtqgkUIkL63JXUy1V7faUyaYqPoGZ5D2f2HEL4Wd5KM-xmMbKNiNvWlM20ruC_TQr_2XUeTlvyxSXrZ-4cvmnIzpyK8NoWt7bHsuxNtHCPmURjXVqp_meIzTdlOFw-VgK20cVNdAJKTdoD5PZyiy6NOLabk0g6Osz-Zvv3hO2BrRRficDT5TUCYP3Blcl6UA6n_lzfbqOXs8TaAth1BJdOqGqivC6hrQyGMrvW3UiqoqeSm_s4dWlujKKwRl2myjwZV_jU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80f48c832.mp4?token=bLm22ARbJlvGhmEhcYgH01835zC6LSpagWlEp60idRW5pv-0PB0HiTWWQ1q4lOlCpbxsiRiaxVNvCehP2aD9I_W0IgY24P3MdKQ2K6ssO34ZjG_iBtmGS-3isDgXDl-0VnNf8fcabFOpLVg82hnLZl7ynpNwmsKDLzhSa7UDkA9NwyAlL2v8f3PutOHwxLa6GyrM0kAGwStSX-nPxDd67DN5AS_rJsgYQxkp6R0vP5wXOG6V-LS69OBX4XEMFc4G0QPp0e9zK2d4CCj6YGeapih_DckvXifGaR_fSkR54x38LeCRQgj9QRHRE7kOFOXoGmtsueyTXQva_DPz8iNtDCXI6rga6Q7ER-858OdvRPnjvCemiL3BFRVPck0M4neWzC9-6iPzP40QA-rVZvbZ1V6qkhcy5sL8llc-iTtqgkUIkL63JXUy1V7faUyaYqPoGZ5D2f2HEL4Wd5KM-xmMbKNiNvWlM20ruC_TQr_2XUeTlvyxSXrZ-4cvmnIzpyK8NoWt7bHsuxNtHCPmURjXVqp_meIzTdlOFw-VgK20cVNdAJKTdoD5PZyiy6NOLabk0g6Osz-Zvv3hO2BrRRficDT5TUCYP3Blcl6UA6n_lzfbqOXs8TaAth1BJdOqGqivC6hrQyGMrvW3UiqoqeSm_s4dWlujKKwRl2myjwZV_jU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما به هیچ‌چیز که کانادا دارد نیاز نداریم. ما به هیچ‌چیز که مکزیک دارد نیاز نداریم. اما آن‌ها به همه چیزهایی که ما داریم نیاز دارند.
🔴
آن‌ها باید با ما بهتر رفتار کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126883" target="_blank">📅 19:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126882">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: ما دیشب و پیش از این هم برای هدف قرار دادن رادارهای ایران تلاش کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126882" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126881">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: خواهیم دید سر توافق چه پیش می‌آید. واقعاً به توافق نزدیک بودیم، اما آن‌ها مدام ما را به بازی می‌گیرند. مدام ما را گول می‌زنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126881" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126880">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX1bc9MbyKn3au7866ep9LjpKqLvXKxPKkAeGpHJvfV1H3E8ZfI8BxzcsxqHZK-cc_IUmRUiNMxDCkXVcu-2R_7mPoVTV6RLno7_zK_yapaj0Kxjfve31ObpIZTn6-hhIdXPx6TlvwmgsYBQMBKAHKEAMeoLLi1jSo7PzEeew3v2k1vv4KdoxrDIEfz0eKWO6nqCZUBaAFDbC2VMNMgN65k7vl2keEFCDCNUQrTUMye458sc14vP_zObHNbG9Rk9RS95TLbXQg6akGq7lFlriCInunTJXKwwlF86m0jV7UurRVNhl7Xe1YFy__5h2yHwnjygZMpl5ROHorkfeQMjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت بعد از تهدید جدید ترامپ بر علیه ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126880" target="_blank">📅 19:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126879">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/929ac5f5bd.mp4?token=St2P9LczyIs3KwT-r_EQgv149w4Tbqx8JfY54pdfiaPyV8T3k4CKehzSe7A49-ILnEwn_T9OlvhUxQXUaRjvYNlu-ptcbToiJhPq9OmPGqwzjkpp-TFDsy4Dt4niOElKKsEEk2cu-OJjWwEtiqn36iUDLzSI5Gs7oXLZr7W9d3l8bKR97mPMIIwA2Ig7QGpQDBarnVqBtPCf175931jVDlxJVqKCdvxPUmzYgA3-f3SI_29ws8y30CFCnloc8c1QWRmSMTVcx30SVcKM08eoX71fm_EjKvyTwWxjiMKRbkSLkQGHdlk6bYNfBRMdZwWe9pezGFE6MPqnr_49H5WXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/929ac5f5bd.mp4?token=St2P9LczyIs3KwT-r_EQgv149w4Tbqx8JfY54pdfiaPyV8T3k4CKehzSe7A49-ILnEwn_T9OlvhUxQXUaRjvYNlu-ptcbToiJhPq9OmPGqwzjkpp-TFDsy4Dt4niOElKKsEEk2cu-OJjWwEtiqn36iUDLzSI5Gs7oXLZr7W9d3l8bKR97mPMIIwA2Ig7QGpQDBarnVqBtPCf175931jVDlxJVqKCdvxPUmzYgA3-f3SI_29ws8y30CFCnloc8c1QWRmSMTVcx30SVcKM08eoX71fm_EjKvyTwWxjiMKRbkSLkQGHdlk6bYNfBRMdZwWe9pezGFE6MPqnr_49H5WXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : رئیس‌جمهور ترکیه اردوغان مدام اسرائیل رو تهدید می‌کنه؛ فکر می‌کنید ممکنه بین اسرائیل و ترکیه درگیری بشه؟
🔴
ترامپ : اون دوست خیلی خوب منه من خیلی دوستش دارم آدم قوی‌ایه
🔴
رهبر خیلی خوبیه فکر نمی‌کنم این اتفاق بیفته تا وقتی من رئیس‌جمهورم چون اون به من احترام می‌ذاره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126879" target="_blank">📅 19:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126878">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گزارشگر: برای تولدتان چه آرزویی دارید؟
🔴
ترامپ: صلح برای کل جهان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126878" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126877">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: به توافق نزدیک شده‌ایم، اما ایران همچنان طفره می‌رود
🔴
ما توافقی مانند توافق اوباما نمی‌خواهیم.
🔴
من برای خاورمیانه و کل جهان صلح می‌خواهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126877" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126876">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40bb596104.mp4?token=hoiQuEL5C5iy0eUOKONhVp_X3QvHxP3kJjbz6qcWbhiyB0TKvEhk-UWKAHJ_A26UQ6sM6HfMABB6vl6-tM0tsAtx93j7iNM-6oYckR7vU7f91tH2vzNkouG2i9ZikO1BBBVL2QurLrgM6oDelOf29xSwcuqC3rBQfsbLbBdYwyQb3Qx2EJ6LZDNNqMtbvn_5DPcwaKNPgbLZXXOk_kwZDF-CeNTrSmBrD1gEVRJq909GW0S0BLjvwKTDdaJ48fMPyDk_ypBEBcjeaSTjANo8hSYDH264pK5fB5patl02gT4RiXQZlUWBYUOLPqIp0pALo9ImxLwDKy__ohCrD-wJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40bb596104.mp4?token=hoiQuEL5C5iy0eUOKONhVp_X3QvHxP3kJjbz6qcWbhiyB0TKvEhk-UWKAHJ_A26UQ6sM6HfMABB6vl6-tM0tsAtx93j7iNM-6oYckR7vU7f91tH2vzNkouG2i9ZikO1BBBVL2QurLrgM6oDelOf29xSwcuqC3rBQfsbLbBdYwyQb3Qx2EJ6LZDNNqMtbvn_5DPcwaKNPgbLZXXOk_kwZDF-CeNTrSmBrD1gEVRJq909GW0S0BLjvwKTDdaJ48fMPyDk_ypBEBcjeaSTjANo8hSYDH264pK5fB5patl02gT4RiXQZlUWBYUOLPqIp0pALo9ImxLwDKy__ohCrD-wJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ایران داره ما رو مثل آدم‌های ساده‌لوح بازی می‌ده
🔴
چون قبلاً با یه سری رئیس‌جمهورهای خیلی احمق طرف بوده من خجالت می‌کشم اینو بگم ولی آدم‌های خیلی نادونی اینجا بودن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126876" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: فاش نمی‌کنم که آیا امروز پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126875" target="_blank">📅 19:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: ایران وقت کشی می کند و من نمی دانم رهبرانش چه کار می کنند. ما مصمم هستیم که از دستیابی آنها به سلاح هسته ای جلوگیری کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126874" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ:  ایران نمی‌تواند سلاح هسته‌ای داشته باشد و نخواهد داشت، و آن‌ها به این موضوع توافق کرده‌اند. تنها کاری که باید انجام دهند امضای کاغذ است. این موضوع کاملاً مذاکره شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126873" target="_blank">📅 19:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126872">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4265b3dd.mp4?token=N5VyDdJ2c9Ppz17HE_4Cm5NhXZAdJr3o0oyOFMac8pdo_F6UIeKelvQ6ix_bYquXTS02Vav5f__rGEalgV81RWV3wrufBVNmPRmppRxKMWiYrxPnvzXjoIca_RePvTCUfrC3la82eagADpL7PApxa2Qj7B-CkvqAGkxF9xrGzsb62EbEncm4d52L0qJDtImzEmTBek9QXiELFu9n1lrmZqHnLAsEAPyjmufKjYebWGRued2zeMTXO0SREJtnEdQ9WK_YuqwoA2LEuhzXrQMK6k431uxCrD4zB1upPfk-Wy_fB4SPvA3kG4Ce7b-X6xuPcRy4A65caNKs4m1u0bidNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4265b3dd.mp4?token=N5VyDdJ2c9Ppz17HE_4Cm5NhXZAdJr3o0oyOFMac8pdo_F6UIeKelvQ6ix_bYquXTS02Vav5f__rGEalgV81RWV3wrufBVNmPRmppRxKMWiYrxPnvzXjoIca_RePvTCUfrC3la82eagADpL7PApxa2Qj7B-CkvqAGkxF9xrGzsb62EbEncm4d52L0qJDtImzEmTBek9QXiELFu9n1lrmZqHnLAsEAPyjmufKjYebWGRued2zeMTXO0SREJtnEdQ9WK_YuqwoA2LEuhzXrQMK6k431uxCrD4zB1upPfk-Wy_fB4SPvA3kG4Ce7b-X6xuPcRy4A65caNKs4m1u0bidNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوووووووووری / ترامپ: امروز ایران را به شدت هدف قرار خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126872" target="_blank">📅 19:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4521420dfe.mp4?token=Vd1PNRPjVV9OsSoctR6lQkRZW_llp1amNLa4JIo9BqRRfST0LprBPbQTGIYkW664Uk2Kbi2PE4gXHmfnTfAhMT2G5DDepH47cNQ-F0nbTm1kHhvijtl_QU6sCkqwM8xbMoJ_l2fcaNUX7WJTKktnzPRuseGt6JYuJ2M1mpwIgz2hrJcpsEZsjvdrOkG_v5Xzr55TB3UxLR6KLlGpInqCu-l-bnnA0njqz3HQiVIWXRsf8aywNhXRLOOxRpG-AMIQ5GMkvYiGf-WAuhYcQBXvih27f3Ie5075PJNjhSlVKWOOQ3BCUnUnn5XuelpIjxZ6K7HTjD48xjF6ZZoT8DFTIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4521420dfe.mp4?token=Vd1PNRPjVV9OsSoctR6lQkRZW_llp1amNLa4JIo9BqRRfST0LprBPbQTGIYkW664Uk2Kbi2PE4gXHmfnTfAhMT2G5DDepH47cNQ-F0nbTm1kHhvijtl_QU6sCkqwM8xbMoJ_l2fcaNUX7WJTKktnzPRuseGt6JYuJ2M1mpwIgz2hrJcpsEZsjvdrOkG_v5Xzr55TB3UxLR6KLlGpInqCu-l-bnnA0njqz3HQiVIWXRsf8aywNhXRLOOxRpG-AMIQ5GMkvYiGf-WAuhYcQBXvih27f3Ie5075PJNjhSlVKWOOQ3BCUnUnn5XuelpIjxZ6K7HTjD48xjF6ZZoT8DFTIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
پاکستان هنوز در حال تلاش برای رسیدن به توافق با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/126870" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587a5ae9fa.mp4?token=gS2QqwsoD0ZyisgWRPWAeXt787BDcu0UnJk5IIBJISc_F_ceZLNl5wgQfs4YW9qpk_T5wZId0BTrmK5089OYg0nknDFUIBSIEph8wEuGNzSySWSPLXBY2GTMj5D30JX2vaemBlmzJm2vlre0wEFxzH3gYg7yesidaV6ydHI9uFktWGYqbYzGP6dkUnCmmyOF3cfPzM8wPN1LFpCo9-ProNNOzykE1LYMhAs5sbBDWRJvwYotCzo_Pp3aZW-B4ZuC0V621CPeWlaBOITsiOYr-BQjLmGMUmIKPVNZEjum1Nen_A34rqTTFkEcrbUug4x8HiPSvw3OnsaKkwKSs5CcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587a5ae9fa.mp4?token=gS2QqwsoD0ZyisgWRPWAeXt787BDcu0UnJk5IIBJISc_F_ceZLNl5wgQfs4YW9qpk_T5wZId0BTrmK5089OYg0nknDFUIBSIEph8wEuGNzSySWSPLXBY2GTMj5D30JX2vaemBlmzJm2vlre0wEFxzH3gYg7yesidaV6ydHI9uFktWGYqbYzGP6dkUnCmmyOF3cfPzM8wPN1LFpCo9-ProNNOzykE1LYMhAs5sbBDWRJvwYotCzo_Pp3aZW-B4ZuC0V621CPeWlaBOITsiOYr-BQjLmGMUmIKPVNZEjum1Nen_A34rqTTFkEcrbUug4x8HiPSvw3OnsaKkwKSs5CcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي ایران:
من چند ماه است که با ایران کار می کنم و آنها باید قرارداد را امضا کنند. معامله خوبی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/126869" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / ترامپ: به ایران که به یک هلیکوپتر آپاچی آمریکایی حمله کرد، حمله خواهیم کرد
🔴
ما با قدرت به ایران حمله خواهیم کرد، این کشور باید توافق را امضا می‌کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/126868" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / ترامپ: به ایران که به یک هلیکوپتر آپاچی آمریکایی حمله کرد، حمله خواهیم کرد
🔴
ما با قدرت به ایران حمله خواهیم کرد، این کشور باید توافق را امضا می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/126867" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e8a0de94.mp4?token=Kux0FZ_SVTjIXjhtjm9qgNM-5L0HSWBWdNQRP4TVxGMVnP3ejsGqqpwBdXjB68vLBVQA8SaiisL6pSbY6VMfLlpGTJTGXYHH3d3wU9vfPPrKkpkcRHI-PyTyfsN35QFuVh71wAZ2onnxgkQILjBOgeE1yASw4dtbZ4rqzYm0LJavhf4CXMfBTqfqgPyph3HOINZuXNvhMvcWd_K4smU0eem4P4hQq1yp30mniVGhFHZtZtvJdVN-HJRBUTLzamyO469cqf6xOfp6F96tf7x0EhvPbL5z0HIdWm7KNOJE2B8ZSL7obhj_tkGL_tPpojLkTbMe5Um0QPk-RjI4kradZT8khM7haX5V2YfYZQmte7cwybtpHFN682ZkeT-Y1DcdaenMJlJTU-8pR3aTnizGaICi7eLBcvtPNhrQqnMIfwb_V51Lan3CIXv14XoSL-6c3Ux2FwLwpdm2PlfCDThoHk3rr8ARjbrBviCCtCFBK4bQQ4o8YXT-sFaKxBfMTk6DtoIyFJJjtxgTkugafKxdN68QXwpBTVrYunaQ98P06OCKzTYAHYue0hd4I0iHELFK3rYV5gBexitdbu1pNiGeDvGsRq-ypOoQR1szz3kwLOd5WC0eLGMShJz808HboMIrb4I4ixsDPePrb4DklzoHndw4vuXm38kKXpIJIcGcTMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e8a0de94.mp4?token=Kux0FZ_SVTjIXjhtjm9qgNM-5L0HSWBWdNQRP4TVxGMVnP3ejsGqqpwBdXjB68vLBVQA8SaiisL6pSbY6VMfLlpGTJTGXYHH3d3wU9vfPPrKkpkcRHI-PyTyfsN35QFuVh71wAZ2onnxgkQILjBOgeE1yASw4dtbZ4rqzYm0LJavhf4CXMfBTqfqgPyph3HOINZuXNvhMvcWd_K4smU0eem4P4hQq1yp30mniVGhFHZtZtvJdVN-HJRBUTLzamyO469cqf6xOfp6F96tf7x0EhvPbL5z0HIdWm7KNOJE2B8ZSL7obhj_tkGL_tPpojLkTbMe5Um0QPk-RjI4kradZT8khM7haX5V2YfYZQmte7cwybtpHFN682ZkeT-Y1DcdaenMJlJTU-8pR3aTnizGaICi7eLBcvtPNhrQqnMIfwb_V51Lan3CIXv14XoSL-6c3Ux2FwLwpdm2PlfCDThoHk3rr8ARjbrBviCCtCFBK4bQQ4o8YXT-sFaKxBfMTk6DtoIyFJJjtxgTkugafKxdN68QXwpBTVrYunaQ98P06OCKzTYAHYue0hd4I0iHELFK3rYV5gBexitdbu1pNiGeDvGsRq-ypOoQR1szz3kwLOd5WC0eLGMShJz808HboMIrb4I4ixsDPePrb4DklzoHndw4vuXm38kKXpIJIcGcTMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دموکرات‌ها: منتظر روزی هستم که دیگر آن‌ها را «دموکرات‌های احمق» صدا نکنم. و این اتفاق نخواهد افتاد مگر اینکه آن‌ها وظیفه‌شان را انجام دهند.
🔴
اگر بخواهند جرم را متوقف کنند، اگر بخواهند مالیات‌ها را کاهش دهند، اگر بخواهند آموزش عمومی و کارهای خوب را انجام دهند. کارهای زیادی هست که می‌توانیم با هم انجام دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/126866" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55f3e4309.mp4?token=UWB_UsGIgc_IGJd8C6VZLTKO9I2iagRydNHalHZzgxlM13ykKe6MbIWsJq6XExUbo0tBuyog1BFuLT5e2FmbxOaV7vlBdohKnfJvDKetsuDFtsq0OPxuXc4eZUbPdyvU0vY2ImEWScFpexeIpqqaLBn6dN1hcB6b6gyRpGiDBzJug1w_8b9TLl30BIMLnfy2rHg6r4zo1tmHO3wm3x6uRmgp2J4nq3T-1zTW3xfBRTaJdolHnk1wV4jIrj6p7-mJHmWPs44eNA908KIpCDBE1BdLaCxisrzllATi2Hax7dX0xL3pToAEN2I57LigO5GioOPv4MZvq1OcIfPC3sev1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55f3e4309.mp4?token=UWB_UsGIgc_IGJd8C6VZLTKO9I2iagRydNHalHZzgxlM13ykKe6MbIWsJq6XExUbo0tBuyog1BFuLT5e2FmbxOaV7vlBdohKnfJvDKetsuDFtsq0OPxuXc4eZUbPdyvU0vY2ImEWScFpexeIpqqaLBn6dN1hcB6b6gyRpGiDBzJug1w_8b9TLl30BIMLnfy2rHg6r4zo1tmHO3wm3x6uRmgp2J4nq3T-1zTW3xfBRTaJdolHnk1wV4jIrj6p7-mJHmWPs44eNA908KIpCDBE1BdLaCxisrzllATi2Hax7dX0xL3pToAEN2I57LigO5GioOPv4MZvq1OcIfPC3sev1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: شومر به خاطر این و آن دیوانه می‌شود، یا اپستین، اپستین، اپستین!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/126865" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfc8df3d6.mp4?token=rqXVeo-WwV2era6INgtjE4OcAlwS0KP3Yg7up9WwBrPJqJa_1WjqqCl2JKcKoAtkbDeuhP9TxnPDny2LNGTgD29WJPSXpLBNud-waMr_B6qzetVYT3mVePflv6iIhqEuTzznFsx2cSY1HUl9yQyOuDpo_DEUd1ExukFJRSMiZ9UFwJOfLJ8RR9-X6eWIY2G5UYrnVEFDfIAMkwYAEknmTln9E880t7aILFThBJg7yauTkxQvk29aLOt50Gw3WYsm_jCiE9AsqKEuKugnfPIqunfaWf2lwY8ou5OT9ghzdq4YvNyMvjon1LwhSFroC-930CyAEv0NjFNyebHGp_nxoouktb3g1DwlObTXtGyoWq-4XnflRhv7w16r6DLqRqtrWK6YwwlUvwXKyatXZeX1U0tiiVTBQGF9QmKUMd4m5NNH7Qet5u9gDx_Jt3xoCMRzwG38U_igy2lmmq80V6-Xr3gHetlaGB9xkTRnAfwJtLIpmVNZxUww-cUuZcxUnQiAnCli3UW4gIoTAZYTW8tb3A9dVAIxsa7roCZf0N8pPMNSdDgPCkHfHBmfPLDV34ZhkjT7ACKjBFfquRDTbvppPmegCtKik5QluBTXaQJhzQo-t_PKVlTF9w5PfrBHF6aA3WmHwY9hL7dHN5U0qkBhLtzl8py0Ow_tXrGzHXk4aDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfc8df3d6.mp4?token=rqXVeo-WwV2era6INgtjE4OcAlwS0KP3Yg7up9WwBrPJqJa_1WjqqCl2JKcKoAtkbDeuhP9TxnPDny2LNGTgD29WJPSXpLBNud-waMr_B6qzetVYT3mVePflv6iIhqEuTzznFsx2cSY1HUl9yQyOuDpo_DEUd1ExukFJRSMiZ9UFwJOfLJ8RR9-X6eWIY2G5UYrnVEFDfIAMkwYAEknmTln9E880t7aILFThBJg7yauTkxQvk29aLOt50Gw3WYsm_jCiE9AsqKEuKugnfPIqunfaWf2lwY8ou5OT9ghzdq4YvNyMvjon1LwhSFroC-930CyAEv0NjFNyebHGp_nxoouktb3g1DwlObTXtGyoWq-4XnflRhv7w16r6DLqRqtrWK6YwwlUvwXKyatXZeX1U0tiiVTBQGF9QmKUMd4m5NNH7Qet5u9gDx_Jt3xoCMRzwG38U_igy2lmmq80V6-Xr3gHetlaGB9xkTRnAfwJtLIpmVNZxUww-cUuZcxUnQiAnCli3UW4gIoTAZYTW8tb3A9dVAIxsa7roCZf0N8pPMNSdDgPCkHfHBmfPLDV34ZhkjT7ACKjBFfquRDTbvppPmegCtKik5QluBTXaQJhzQo-t_PKVlTF9w5PfrBHF6aA3WmHwY9hL7dHN5U0qkBhLtzl8py0Ow_tXrGzHXk4aDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره گراهام پلاتنر: او یک اوباش است. احتمالاً بدتر از هر انسانی است که تاکنون برای مقام انتخاب شده است.
🔴
من او را نمی‌شناسم. نمی‌خواهم بد بگویم، اما هیچ‌کس سابقه‌ای مانند او نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/126864" target="_blank">📅 19:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ونس: توافق با ایران باید از نظر اقتصادی به نفع آمریکا باشد
🔴
جی دی ونس، معاون رئیس جمهور آمریکا: احساس می‌کنم در موقعیتی هستیم که بتوانیم به توافقی دست یابیم که از نظر اقتصادی به نفع آمریکا باشد و واقعاً موضوع برنامه هسته‌ای ایران را نه فقط در حال حاضر، نه فقط تا وقتی که دونالد ترامپ رئیس‌جمهور است، بلکه در بلندمدت حل کند.
🔴
عدم برخورداری ایران از سلاح اتمی، سیاست ماست و فکر می‌کنم بسیار به رسیدن به آن هدف نزدیک شده‌ایم، اما هنوز مقداری کار دشوار باقی مانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/126863" target="_blank">📅 19:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cef8fd5d.mp4?token=B7Bq6HRcRnGTwY_2saw_KZPrEIYBG_WruSyJqZzgNZokg6zyl71DN9YlxOAEKELF6HF4bjr9voKI3ir82xNUnyA13HbPb43T-SR5GZuekgIX6CR-eox_95o21hpSXJ4AaPjj4jq5KYvxmZnfd0w7TojCpXs7j9XxQka6yc8PCmcbpr51VoeBjCl7s2aw0TKDLNLRiUp6q4Cv_Ap4aK0rGfWr5pUOVtLboTnv8BhaDxKifVFXWlJZ70Vf1weZZWV9kWOTMJf_1pE0Q5aXM3kvZG-f5E55O7txQTMbHnaM1Vzrdx32SsgfuRzIJL2iqp6v_XhTJLnLc_8Ga61FarA8zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cef8fd5d.mp4?token=B7Bq6HRcRnGTwY_2saw_KZPrEIYBG_WruSyJqZzgNZokg6zyl71DN9YlxOAEKELF6HF4bjr9voKI3ir82xNUnyA13HbPb43T-SR5GZuekgIX6CR-eox_95o21hpSXJ4AaPjj4jq5KYvxmZnfd0w7TojCpXs7j9XxQka6yc8PCmcbpr51VoeBjCl7s2aw0TKDLNLRiUp6q4Cv_Ap4aK0rGfWr5pUOVtLboTnv8BhaDxKifVFXWlJZ70Vf1weZZWV9kWOTMJf_1pE0Q5aXM3kvZG-f5E55O7txQTMbHnaM1Vzrdx32SsgfuRzIJL2iqp6v_XhTJLnLc_8Ga61FarA8zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما جریان فنتانیل را از مرزهایمان تقریباً ۶۰ درصد کاهش دادیم.
🔴
از طریق دریا، ۹۷ درصد. ما به دنبال آن ۳ درصد باقی‌مانده هستیم، زیرا فکر می‌کنیم آن‌ها از شجاع‌ترین افراد هستند.
🔴
متاسفانه باید به مکزیک بگویم که اکنون تمرکز ما بر ورود از طریق خشکی است.
🔴
بخش زیادی از آن از طریق دریا وارد می‌شد، درصدی بسیار بزرگتر از آنچه کسی می‌دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/126862" target="_blank">📅 19:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de8ebd6c8.mp4?token=c4JVA2uy5FwPXk7LVmIu6CnkA_3SSWak2kqnr5BxGdKRT7XhDnhpt-iuzCK-bsbr1mBOJgwevW8tDE8FcJhDL5n7ltoh7Df7Y0AZK8DvpZ-EH1OoPMcxRr0ks1gXUcC--k6vZwiwnDoErB7e6iPfj-c5vV420vUtw8umpQ3WrI1GFeJu3gDYkwyKxC7W-bO9QRE4e-rmJdTMCPFnomN6pYl59jkza1udLYwCE59tu2n1y8W7ZPs1L27oGJ0E340MBUu6EF9j6eRIO8m9694t9OBqJm_u-lciFP0bl8ccJo7o32aV_gUsh89-o7INgqNEPhfgrPPxbalj5m2B-KlXwDJdUNAHzgl6kGRcM-dUxx5jc1cSUPZFyqhG69OYSUs2xCfIH6RFDWXBW-TgcmlGOhYBCv_vnYzDVedFjMlkJp24W1zWjRFBAU0b0aukV5BB2isOn6VD6pldT0UNdSZeNreX8Qbebc9bFOrCLBx70QTS3osffxjibWnR22TANSyzph12Ek8kXGb4_zoYrZi4ldkSLYDbRBk307d62JFohFWKOAWaqes9avp5_LBVoqTpcXqG2DqW2fiBzlqEvHwfoxoEhZzgdGYWCAwPAyfj0DXgOG2BFT3WJlfMqeZ2hnuxQbh4CBBsqLhij0-WyNlSgW_vogbjLdKT3VlveX1QTkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de8ebd6c8.mp4?token=c4JVA2uy5FwPXk7LVmIu6CnkA_3SSWak2kqnr5BxGdKRT7XhDnhpt-iuzCK-bsbr1mBOJgwevW8tDE8FcJhDL5n7ltoh7Df7Y0AZK8DvpZ-EH1OoPMcxRr0ks1gXUcC--k6vZwiwnDoErB7e6iPfj-c5vV420vUtw8umpQ3WrI1GFeJu3gDYkwyKxC7W-bO9QRE4e-rmJdTMCPFnomN6pYl59jkza1udLYwCE59tu2n1y8W7ZPs1L27oGJ0E340MBUu6EF9j6eRIO8m9694t9OBqJm_u-lciFP0bl8ccJo7o32aV_gUsh89-o7INgqNEPhfgrPPxbalj5m2B-KlXwDJdUNAHzgl6kGRcM-dUxx5jc1cSUPZFyqhG69OYSUs2xCfIH6RFDWXBW-TgcmlGOhYBCv_vnYzDVedFjMlkJp24W1zWjRFBAU0b0aukV5BB2isOn6VD6pldT0UNdSZeNreX8Qbebc9bFOrCLBx70QTS3osffxjibWnR22TANSyzph12Ek8kXGb4_zoYrZi4ldkSLYDbRBk307d62JFohFWKOAWaqes9avp5_LBVoqTpcXqG2DqW2fiBzlqEvHwfoxoEhZzgdGYWCAwPAyfj0DXgOG2BFT3WJlfMqeZ2hnuxQbh4CBBsqLhij0-WyNlSgW_vogbjLdKT3VlveX1QTkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور ارشد جمهوری‌خواه لیندزی گراهام:‌ می‌خواهم از شخص بزرگ، خدا تشکر کنم. بعدش از ترامپ. آقای رئیس‌جمهور، شما از خدا دور نیستید، اما ما با او شروع می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/126861" target="_blank">📅 19:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ درباره استخر بازتاب یادبود لینکلن: این طولانی‌ترین استخر جهان است، سه یا چهار برابر بیشتر.
🔴
جایی است که مارتین لوتر کینگ سخنرانی بزرگ خود را انجام داد و می‌گویند یک میلیون نفر حضور داشتند.
🔴
و من چند سال پیش در چهارم ژوئیه آنجا سخنرانی کردم و جمعیت زیادی بود.
🔴
و گفتند من ۲۵۰۰۰ نفر داشتم. گفتند او یک میلیون نفر داشت. اما وقتی به عکس نگاه می‌کنید، من گفتم، «صبر کنید، مردم در سخنرانی من حتی فشرده‌تر بودند. من بیشتر از او جمعیت داشتم.»
🔴
اما گفتند من ۲۵۰۰۰ نفر داشتم و او یک میلیون. اما من نمی‌خواهم با مارتین لوتر کینگ بحث کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/126860" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc565a1c0d.mp4?token=pJbve5F4sDIkdiz5x9uLlEzdsPASFyE7vGmoutLpYSXjUlZq60wzF_5T57ptxtRDLx_Oc_8THHT3g32NXAU49dhMo_yD6CxYswe63BEhdCDVgCzONquLG3jLl8qm9P2K5UMzKidl2uHV9brw7uBcsWMQM8HL6tSj0FpJfBLBZxCLhRhPzBDZCFcPNXvAFPOqDGOWQiBAG0zUo3Vq0lwUmBv-bEeoZlAFOMobUXliWQDeaPbpa-10BlV9WYW_a8dQ0O7maVO5xMaMRrHQOZLTXC3ez3KfQX_UY53pvwbQyDHJSmvPNgEkYaiQedYeF8Tyz0LwujG40RUvYIkOxrCTDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc565a1c0d.mp4?token=pJbve5F4sDIkdiz5x9uLlEzdsPASFyE7vGmoutLpYSXjUlZq60wzF_5T57ptxtRDLx_Oc_8THHT3g32NXAU49dhMo_yD6CxYswe63BEhdCDVgCzONquLG3jLl8qm9P2K5UMzKidl2uHV9brw7uBcsWMQM8HL6tSj0FpJfBLBZxCLhRhPzBDZCFcPNXvAFPOqDGOWQiBAG0zUo3Vq0lwUmBv-bEeoZlAFOMobUXliWQDeaPbpa-10BlV9WYW_a8dQ0O7maVO5xMaMRrHQOZLTXC3ez3KfQX_UY53pvwbQyDHJSmvPNgEkYaiQedYeF8Tyz0LwujG40RUvYIkOxrCTDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ پیت هگستث به همراه نیروهای آمریکایی در پایگاه گوانتانامو به تمرین می‌پردازد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/126859" target="_blank">📅 19:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJeMO-c-nsILIC24qeFpZ5hIPP7wPLmjeNhl66EFQZAFUlNUkvDXFQM5zRD8htVGC7L5zrMg5kWhw_34CGHSNZrn9_c4tk7xR-JUsOQFjA3Ja2MhMxfDw7ozndzkb2nn0wz04JNzhrKHiAsoX-BtwWhnlWmdluyAjQauls6NkAgIU0rzL9uFBg-gefYDqJXz3QohPsFt8nSbyHoPFZXOt18SXYTZUXJx_WrozwmhJtPhttsfpJvFWRUk6nArfL8o95hMh1lUiCWjo-7WLm5wcYX8_UqYla_1ZPQ6fO4htmFBRZ0kAHrXZx65N_oTRCnr1Pbn9hNTXfnlx4ihK8VMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏سید حمزه صفوی، تحلیل‌گر: وقتی رهبر انقلاب شهید شدند، صداوسیما اعلام کرد که مردم به ما اعتماد کنید. رهبری زنده هستند! و بعد دیدیم که رسانه اسراییلی خبر داد ایشان شهید شده است. این وضع صداوسیما است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126858" target="_blank">📅 19:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqN5_0LQmHYuIBbFFnE6SNndQHDk13P31SB5btopi_SQk-67iHtuzHoSr4-qX-jPU9ExH2bZuVFZEdBHob656R1eOxqIo1exY0t9FXKm_ldDsMeCUw9n1nohad7Io0Ix5nGFhXmN6i5MUTRLQodk3D6QjH3hTHrMX8tM3WIEr7fpD2uFkEjxZLo0JEeHtRW8zQrVBv3sU7h7oxqO_YVFX6gugTw9cWO2LWpinJkek-NgJ3eM9WGsDVsejHP5BWpfYYbR2fzjwU8SdwiM6dh2w_ycdqJCsVcC0fE6pJBWewbpLREDezXJrizN0OTcA7JwwFTdetqb1wKzBGjsEh81xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
هنوز نگران تموم شدن حجمت هستی
😱
یا استرس ضریب و تایمشو داری؟؟
🥸
کافیه اشتراک TVPN رو تهیه کنی
نامحدود واقعی با ساب
🔥
که دیگه نه نگران حجم باشی نه تایم
🎈
اشتراک نامحدود فقط 290t
🎁
😀
حجمی از گیگی 2t
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126857" target="_blank">📅 18:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مشکل ترامپ این است که تهدیدهایش دیگر نه تنها در نگاه غربی‌ها، بلکه در چشم ایرانی‌ها نیز اعتبار خود را از دست داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126856" target="_blank">📅 18:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نمایندگی‌های ایران، روسیه و چین در بیانیه‌ای مشترک در جلسه شورای حکام:
قطعنامه پیشنهادی آمریکا علیه ایران در شورای حکام ماهیتی سیاسی و غیرسازنده دارد که اوضاع شکننده کنونی را بدتر می‌کند.
🔴
با هرگونه تلاش برای گمراه کردن کشورهای عضو آژانس نسبت به وضعیت واقعی برنامه هسته‌ای ایران، از جمله از طریق گزارش‌های مدیرکل مخالفند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126855" target="_blank">📅 18:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/هم اکنون هواپیماهای سوخت رسان آمریکایی از آلمان به سمت خاورمیانه در حال حرکت می‌باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126854" target="_blank">📅 18:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126850">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJyAFzuX_pu2PajT5oTdR7CATsF0EFGJTifF_Ttvu1jE-Z9pGqJvHO6oYrYUQxcOKeI-wuZRRM61OdL5h-Vx9qvbXZCWfkfn6X5Sww_AxQgICQ74VBMTHpyN5q2qF3ITlf9w_hroVkwsWzpQo6Xli06OdvIXWtn75GMoNMR3ElcNDi-ug5Mme_OvKY9Us1lL92ZSp5UfmqGGHiFSTrYlLe84taOysHeu3b1XuJodmoc_VwnFexvZDHpQvRPSVGrpxBUPJTdrDFthOjjKijEU-cOoBaP3nTt5MxQZKfpv7xvM59FPemjjtkYMg_MdfKlUNxu_MzeYcbmtbkI32-YIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKfQkIQ14gtGCHep_HsQDOQbktR8R5MNaXHnDZdA2qcvzm48HfxXn4Uibtn1hXjYU7jbn1s6IA_YlkUpT3gvERPaIHqDvQZ94Ysx8DnCt1yktpOeu_LX8QOeb-gyiw-pvhm0VZ01-VAPcV31PcP2DXzFPX0ibFIcvr1TYnSG7ZdBD5eunWsZpxbFO8Nb8geSlYJ1QIhYHngWKxzZmFqTOa5xkWJrthUAN1jprKLj4IiuVyALO274wv-len24fxfaYJCPq9Xjg9xDfDvzj8zJV9CfjUrVHdwBtwRRLb8u11QtrQMsGsQG_p7FGOgD--p63TYEYmdQr7Ul4-eYn_lNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAfwf1Q1c7CzJDVnMojDcd_9Izi4KtCWT3SKQQYhAiHGik5SoFUkC8o0tWCgE3qZzfsBkuS6ONp93lZcrWncVfM1rebzPoWHK7rw1lsaMAYmvSh7MQ1K7A0I4OwlFmXv5d8n3gGZueXLy08Jdgq0cbsB6WyQOH7ekBItUt3sh5zmEaOaOk28I3w6kp5Cooogj_HW_T6V7NZzzD4sGDAuwGMLaPtn-yIzRKzZT198Jrs7mIHlIM3ZR1Qc4AH8b4t_OOlS66uOqFh8L_7LiHbZVSnwtiV3k7Edq3WHnjsdoY9AN6DpU4MIoivaW7G5eLNMB8XU3QXRLaFmVrwydizOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PK5UIwmmamDukB4sqmTrs1sUfsy7ZArwbyx_4832LP7FOkkI6Z5Qzyi8h8wAZOs49N06nAbVUTbZaWqZ5rwSYWX8m9UKItKaqoeiM9ODVbFPrHIMyLJgnexrA1ExZI0CUjEZsjU_L9r22SSpdhh-u_-2URHtfLRd2rRC2TT8shCpTygW5EaEP_7P1USpW4a1tCxAj9wqCnJSPhj-qP-vQgKulzI9CUix0W7eW7Gjci7YAnjHHJuXZ9xIRcsTOG1q8zsxUQleqgeSiyoInzAUQ4BNApfQ2icj_wUUozAwJE4eKQ-JvGEcHy7qOFqo31O2yb_Mvi9-kO_TPFBHU4GUww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی خود در جنوب لبنان ادامه می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126850" target="_blank">📅 18:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126849">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ابراز نگرانی گوترش از ادامه مسدود بودن تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/126849" target="_blank">📅 18:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126848">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بر اساس پایش هوش مصنوعی دریایی «ویندوارد»، پنج کشتی حامل ال‌پی‌جی که با ایران تجارت می‌کنند از محاصره دریایی آمریکا عبور کرده‌اند. در حالی که ترامپ مدعی شده بود «هیچ چیز» بدون اجازه آمریکا عبور نمی‌کند، داده‌های ماهواره‌ای کپلر نشان می‌دهد چهار کشتی محموله خود را در هند و یک کشتی در پاکستان تخلیه کرده‌اند و صادرات ال‌پی‌جی ایران ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126848" target="_blank">📅 18:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126847">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
به گفته برخی منابع آمریکا داره هواپیماهای باربریشو از قطر خارج میکنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126847" target="_blank">📅 18:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126846">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت خارجه هند: حمله به نفتکش «سیتیبیلو» در سواحل عمان را محکوم می‌کنیم.
🔴
۲۱ نفر از اعضای خدمه این نفتکش نجات یافته‌اند و همچنان ۳ ملوان مفقود هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126846" target="_blank">📅 18:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126845">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
تصویب قطعنامه آمریکا در شورای حکام سازمان انرژی اتمی علیه ایران
🔴
یک روز قبل از جنگ دوازده روزه هم اتفاق مشابهی در آژانس انرژی اتمی رخ داده بود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126845" target="_blank">📅 18:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126844">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
کانال ۱۲ تلویزیون اسرائیل: نیروی هوایی اسرائیل به تازگی حمله هوایی به دره بقاع در شرق لبنان انجام داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126844" target="_blank">📅 18:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126843">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر جنگ آمریکا پیت هگست در خلیج گوانتانامو: آینده کوبا در دستان رئیس‌جمهور ایالات متحده و رهبری کوبا است.
🔴
صرف‌نظر از هر چیزی، وزارت جنگ آماده و مهیا برای هر احتمالی خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126843" target="_blank">📅 18:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126842">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITsa98MdTC3ezS1kqUQuO7t4PA66PZ3TDU61d5r1JMHtCU0UBCxdeYI95ark2pIRF2pmkpBcm-GMNl9M5OS7cJnqvhc9QA1ziwIQPff6Ii1WFRGEJzMtepQVk7RPwLMtGfPEbWt0nt1x3cZm-ypkUFd0RKlYU75EL2fz2TgNhqbBBYamdjWkC8oYUTshfswjTQ-tzmrfJ_MBA_2DFlEKL2rX63wdX071mkwT4FJh3G693tGZFwFV3QP7tNQuL7IDL5fGVBaqj8FXW4L2zZofhrM3j4d_0Qtlvu4nPVcxnAzlBoYuWd2ZN74bDAfwSqDlXboe4j1AH0Mjybpc06vdag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی در حومه شهر سحمر در منطقه البقاع غربی، شرق لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126842" target="_blank">📅 18:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126841">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
تصویب قطعنامه آمریکا در شورای حکام سازمان انرژی اتمی علیه ایران
🔴
یک روز قبل از جنگ دوازده روزه هم اتفاق مشابهی در آژانس انرژی اتمی رخ داده بود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126841" target="_blank">📅 18:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126840">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3267c9f92.mp4?token=OmUtZg8-H1IQ6Q0_0-pQwCx_5RhjLs-U7GpD-dFUShGzRD8x7mWLiqKWAusCnUMmWhZLl-A-h17OlKC4qQN47d8Bl_v10Hxmp8OY-Il_IPEMwrZODAr9fDcGdudDCOao1PSAgJmEdfDDQBC9cddj6hlzayVL6BwtBItzxmiJEJy-6hXv5x51texkx2rlBubeMM9sJiHTsyhI-EcPmkR5qiYEFCgMhmdxeSnEW6DDuUieFax0xQPC3Ttj8KJOpXFsbs1xoXvVsYC2zD9fE3ack7FRSZzBDXOqCwWFo4B9yiyJkPb9mHA1eysxVwzRhb52-6ZnLhm_7TEO1knsYBbSAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3267c9f92.mp4?token=OmUtZg8-H1IQ6Q0_0-pQwCx_5RhjLs-U7GpD-dFUShGzRD8x7mWLiqKWAusCnUMmWhZLl-A-h17OlKC4qQN47d8Bl_v10Hxmp8OY-Il_IPEMwrZODAr9fDcGdudDCOao1PSAgJmEdfDDQBC9cddj6hlzayVL6BwtBItzxmiJEJy-6hXv5x51texkx2rlBubeMM9sJiHTsyhI-EcPmkR5qiYEFCgMhmdxeSnEW6DDuUieFax0xQPC3Ttj8KJOpXFsbs1xoXvVsYC2zD9fE3ack7FRSZzBDXOqCwWFo4B9yiyJkPb9mHA1eysxVwzRhb52-6ZnLhm_7TEO1knsYBbSAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار
شکارچی
: تو
دهنی
محکمی به
ترامپ
زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126840" target="_blank">📅 18:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126839">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
هم اکنون سازمان ملل متحد: درباره بازگشت جنگ فراگیر به خاورمیانه هشدار می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126839" target="_blank">📅 18:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126838">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
تصویب قطعنامه آمریکا در شورای حکام سازمان انرژی اتمی علیه ایران
🔴
یک روز قبل از جنگ دوازده روزه هم اتفاق مشابهی در آژانس انرژی اتمی رخ داده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126838" target="_blank">📅 18:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نمایندگی ایران در سازمان ملل و سایر سازمان‌های بین‌المللی در وین: ایران حقوق غیرقابل سلب خود را از جمله در پاسخ به این قطعنامه نادرست حفظ خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126837" target="_blank">📅 18:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فاکس بیزنس: نرخ تورم سالانه ۴.۲ درصدی بالاترین سطح از آوریل ۲۰۲۳ تاکنون است.
🔴
قیمت مواد غذایی در ماه گذشته افزایش یافت.
🔴
شاخص انرژی نیز بار دیگر رشد کرد.
🔴
بخش قابل توجهی از این افزایش را می‌توان به مشکلات مربوط به کودهای شیمیایی که از خاورمیانه تأمین می‌شوند نسبت داد؛ از جمله اختلال در محموله‌ها و افزایش قیمت این محصولات.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126836" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126835">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام ارشد کاخ سفید در واکنش به پست ترامپ اعلام کرد:
مذاکرات با ایران همچنان به صورت غیررسمی در جریان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126835" target="_blank">📅 18:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126834">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39fa6c3d78.mp4?token=pcukOUlPnaUdcqxKo3mHJNYJDy-XqP9ESfOq3nqnrLbn3odwoCijmnsV-gzyggak-TTdnqCyxJCkMVqilOOmQyNvkwhr6TcDUhWCEUaJ8SRi9hMmR3PsvoQDeW-f1v4uj9WPpjJ2vhMUIqewVO_jcdC3UpRgZtsZb-WWhXLFULIDcb2-JQQOaT1644lpv1Sac5VSATSeAEzssg5WwQILOn6kw2ekmQxn1Y6mJqCf7pXANc5Akn3q01WOPv0EgGW796Q76QO6T616Y5RjUe75q-jtA9FtZzb5dnuleC6sBCyehzaPAl7N33rJhiMmNP-LF831lr2oFbH5zdT9Xaxo2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39fa6c3d78.mp4?token=pcukOUlPnaUdcqxKo3mHJNYJDy-XqP9ESfOq3nqnrLbn3odwoCijmnsV-gzyggak-TTdnqCyxJCkMVqilOOmQyNvkwhr6TcDUhWCEUaJ8SRi9hMmR3PsvoQDeW-f1v4uj9WPpjJ2vhMUIqewVO_jcdC3UpRgZtsZb-WWhXLFULIDcb2-JQQOaT1644lpv1Sac5VSATSeAEzssg5WwQILOn6kw2ekmQxn1Y6mJqCf7pXANc5Akn3q01WOPv0EgGW796Q76QO6T616Y5RjUe75q-jtA9FtZzb5dnuleC6sBCyehzaPAl7N33rJhiMmNP-LF831lr2oFbH5zdT9Xaxo2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دی ونس: در حال حاضر، احساس می‌کنم که ما در موقعیتی هستیم که بتوانیم توافقی به نفع اقتصاد ایالات متحده به دست آوریم و واقعاً به مسئله هسته‌ای ایران بپردازیم — نه فقط اکنون، نه فقط در زمانی که دونالد ترامپ رئیس‌جمهور است، بلکه برای بلندمدت.
🔴
تا جایی که فرزندانم وقتی بزرگ شدند بتوانند بگویند ایران سلاح هسته‌ای نخواهد داشت.
🔴
این هدف سیاست است و فکر می‌کنم ما بسیار به رسیدن به این هدف نزدیکیم، اما هنوز کارهایی برای انجام دادن داریم و به انجام آن ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126834" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126833">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
هم اکنون حمله پهپادی حزب الله به شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126833" target="_blank">📅 17:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126832">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری /  ترامپ اعلام کرد امروز ساعت ۵:۳۰ عصر به وقت شرق آمریکا، در یک سخنرانی اضطراری با مردم و رسانه‌ها صحبت خواهد کرد.
🔴
جزئیات و محورهای این سخنرانی هنوز اعلام نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126832" target="_blank">📅 17:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126831">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: پایگاه‌های فرامنطقه‌ای آمریکا رو هدف قرار خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126831" target="_blank">📅 17:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7CdQAkWUqLYUAimleIQRptdKwvKrk93LoLnov6FYMkAOOVHvx2TjtMZV2uF_1TXdi5mVAG7MtE1w6dGLFuNJNTxCwywZyAvpxqSZstHx2HaNP_iTGzbcredxZXib8xR90cDHf0OAnaEJhCLYFMFk5DPnybizPmlWheSXov-LMuQrqPx3PZLs43f4Fjr20LHgWmAoumSVwRRltchJHftEGp-7B_GWyE5dF-U35vckjUfER8UZmffiMnU6yJAM4vcA0042e5t0ek2f-wZyqf1oMWmWWdyWbiJP5mci2rgAn2GXdGDY39P8iQQAKpbkB3ULkS7LYfjMaB7zlRRoXZcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی هر اونس طلا در معاملات امروز با ریزش ۱۲۳ دلاری حدود ۳ درصد کاهش پیدا کرد و به ۴۱۳۴ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126830" target="_blank">📅 17:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126829">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424a37ec4a.mp4?token=D0T7mHvn0LS6fg086y5IGLwQd0jBoblvL5bnkOvnKzS0LtjnzNA8XqjnTT8im3QyelZTu08haQKR0KOF1z_y_QwKrHjcvM1BDnBhufZQtV-0qttgWnxQPkbAT3a5D7YqHB2-Gm980PFhv993mr9_-tGgcxizHyLul5gQpm8Bcwk80IL-gr_6aWR-WKJCVVHz26dX2m5E3ukDIcxT6s7K_xQDFmEKMGd5ovhd5RNbTd9s8YKsail4z8Xe05es-0GnzF5tsYBmd7AHiPQSmY6mkizYhmKAHXcq3pttzyWSSBuTpQzj9-gjGju47gXe4pj3zFWD68eRUP92nazni8lnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424a37ec4a.mp4?token=D0T7mHvn0LS6fg086y5IGLwQd0jBoblvL5bnkOvnKzS0LtjnzNA8XqjnTT8im3QyelZTu08haQKR0KOF1z_y_QwKrHjcvM1BDnBhufZQtV-0qttgWnxQPkbAT3a5D7YqHB2-Gm980PFhv993mr9_-tGgcxizHyLul5gQpm8Bcwk80IL-gr_6aWR-WKJCVVHz26dX2m5E3ukDIcxT6s7K_xQDFmEKMGd5ovhd5RNbTd9s8YKsail4z8Xe05es-0GnzF5tsYBmd7AHiPQSmY6mkizYhmKAHXcq3pttzyWSSBuTpQzj9-gjGju47gXe4pj3zFWD68eRUP92nazni8lnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عصبانیت کارشناس تلویزیون از صحبت های زیباکلام:
🔴
یک لعنتی در مورد رهبر شهید ما گفته «او دیگر نیست» بابا ما هنوز پیکر این آدم رو دفن نکردیم، چقدر شما رذلید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126829" target="_blank">📅 17:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
معاون قوه قضاییه: خشخاش نکارید،ممنوعه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126828" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ve67OOUbZ0CWzW3emptPoTzX2D8wz6nF1swfOtNUiBSb5W6DQFL7f-1iOfvhWxqADD15HRpAxmws3gv1mQ7wE_UXVQkmX-2ZvrWGq0rCeCvjnhK24DlNhxJF2WeGg2wS1Pif-R9JChWX5OTF8v4_ugyJKDEpvOXhMzfpe-OXagufJ2itqQYK6c91fNHIx2bvwMaxaij4exyY6RzwSXdrMku4Ctv7JNGYW4uASkXq8I7akxUXCkBfEHcXUGBo76CzL6AQHeR2wj546JbrprWB0d3taKfLlO-M4c3nhMp4mhvYsSFKY2SUNBeCU-LQPigPTt6KV7ZQuovWXsRwJLnC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قشر تندرو دیگه رد دادن نوشته: غیرتی که ترامپ روی یدونه هلی کوپتر داشت کاش مسئولین روی رهبر شهیدمون داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/126827" target="_blank">📅 17:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
تامیر موراگ خبرنگار کانال ۱۴ اسرائیل:
ترامپ همین الان توییت کرده که ایران برای توافقی که می‌توانست برایش عالی باشد، خیلی دیر مذاکره کرد و حالا باید بهای آن را بپردازد.
🔴
مشکل ترامپ این است که تهدیدهایش دیگر نه تنها در نگاه غربی‌ها، بلکه در چشم ایرانی‌ها نیز اعتبار خود را از دست داده است
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126826" target="_blank">📅 17:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126825">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxT5GDdI9PZRB6NBSQh2dDBdu7VDoS_4XBW0dCv6kWcFBnoFjEuHeP7MZZuRartb2xPwJCBBn1JSbPdtKwSo-KoZQZDevYJXP3JkBBHOj85S-b6vTHvehIwmZF-NftVMmYSZwMon_shvcYmtH5xjccFNadj8iREbQXNWfMe7q2bHM7Uc4bI4aHh2LrPYyitK0HlPsj0d65mwRprG8PW7a7IA_0VI2osOf03i7MNtpLsyjG0Vd0jILSr5s06BKG0MzcHnR4_rCgX3ztwT7WA4rj4QBy8Co_9tnzkEesQFvYrPTWfjhul_oV94pcneF_C0OgHavgqW_hQoLds1ATk45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران تو ارمنستان اومده یه توییت زده که همزمان داره "باسن" ترامپ رو میدوزه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/126825" target="_blank">📅 17:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126824">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S5BHr6twUlF1kEx6Iyc6VdYhGnnp2vOu-QC0RYrPQO_B8Yt0j8DKFIVbsu2WxhcI53nhFfsQuuLkeuMjysmdcnXQ75plhEKVPEeHkw4lN_wCywCDwD47bPePJ535R6zXrBPeW-b-oQ4hctaj_GfRavnLXRCZmY4bMwU1YfU6vp0xrXoFeF5LVqDQ31quIdj_9ObN6AWJDcnYR8EJ2nNVeJwBezwUw1yQ2GAzZJ37j8t3qrxro1UmZq-NAui4itwGM4qBA6j_LIJ5Zh7L8aQ7LzOFIGLRoG8lKjb4d83O8KpAW_GjszvGZBshQhHfKLgfsjRK3a0sV4jdFg6H9JocSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن زنگنه، عضو کمیسیون برنامه و بودجه:
ما باید حقیقت رو به مردم بگیم، در شدیدترین حالت جنگ با آمریکا هستیم. ما با بستن تنگه هرمز روی اقتصادشون فشار آوردیم و اونا هم با محاصره، واردات و صادرات مارو محدود کردن.
محاصره باعث کاهش درآمدهای نفتی و ارزی ما شده و به شدت با کسری بودجه مواجه شدیم.
با پایان جنگ دوباره درآمد های نفتی ما برمیگرده ولی تا اون موقع،
۳ ماه خیلی سخت رو پیش رو داریم!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126824" target="_blank">📅 16:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126823">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
3 بمب افکن B52 آمریکایی در ساعات گذشته از آمریکا حرکت کرده و در بریتانیا فرود اومدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/126823" target="_blank">📅 16:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ایران فرصتی برای امضای توافق و زنده ماندن داشت‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/126822" target="_blank">📅 16:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز گفت: تهران مذاکرات صلح را به تعویق انداخت که در نهایت منجر به پیشرفت بسیار محدودی شد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/126821" target="_blank">📅 16:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126820">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک دیپلمات آگاه:
پس از رایزنی با ایالات متحده، مذاکره‌کنندگان قطری امروز صبح برای دیدار با ایرانی‌ها به تهران سفر کردن تا در تلاشی برای رفع اختلافات باقی‌مانده در فرآیند مذاکره باشن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/126820" target="_blank">📅 16:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6201d48750.mp4?token=U8q5vuE0F2lom53RvNA-FBWj6lOaChXLe7-GA30x-3QIeuM-UZT14Et8P5jeRip_UIOXJ79LjjudFjdrWZafbe-X81RQ0e6FycIpTetKZ906qWyEfFvepVJDG6INuJy66jYjdwkRDuGBABZKnPEeg7R_ZiiGiwTTi0c7MytK0k1WMYKRxW6HocQLkq060njmyRt0Gxlp9vVP9-MI3OMXRw2zccyD819vvV8m4ONdzCyqthN39BfCgraQp3zA8lNgmWSnhJgpJ0UXNrhxU8N2Pm5DKKdjic2dQNhXKpG84kwtqzpwDy3N9vs2nqbvfKJQpHdPf1oTifHMyAZPyofzcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6201d48750.mp4?token=U8q5vuE0F2lom53RvNA-FBWj6lOaChXLe7-GA30x-3QIeuM-UZT14Et8P5jeRip_UIOXJ79LjjudFjdrWZafbe-X81RQ0e6FycIpTetKZ906qWyEfFvepVJDG6INuJy66jYjdwkRDuGBABZKnPEeg7R_ZiiGiwTTi0c7MytK0k1WMYKRxW6HocQLkq060njmyRt0Gxlp9vVP9-MI3OMXRw2zccyD819vvV8m4ONdzCyqthN39BfCgraQp3zA8lNgmWSnhJgpJ0UXNrhxU8N2Pm5DKKdjic2dQNhXKpG84kwtqzpwDy3N9vs2nqbvfKJQpHdPf1oTifHMyAZPyofzcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صادق زیباکلام بخاطر این مصاحبه که گفته بود موشک‌ها فاجعه به بار میارن، بارداشت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/126819" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126818">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رضا دالمن دانشجوی کارشناسی ارشد رشته مهندسی کامپیوتر دانشگاه صنعتی شریف به خاطر اویزون کردن عروسک یک موش و بدون هیچ دلیل خاصی از دانشگاه اخراج شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/126818" target="_blank">📅 15:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126817">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ در گفتگو با فاکس نیوز: بالگرد آپاچی AH-64 ارتش ایالات متحده که اوایل این هفته سقوط کرد، توسط یک پهپاد که بین دو خلبان خورده بود، مورد اصابت قرار گرفت.
🔴
با وجود آتش گرفتن و ایجاد گرمای شدید، پهپاد منفجر نشد و به خلبانان اجازه داد تا در دریا فرود اضطراری داشته باشند.
🔴
خدمه حدود دو ساعت بعد توسط یک شناور سطحی بدون سرنشین نیروی دریایی ایالات متحده نجات یافتند.
🔴
ترامپ زنده ماندن خلبانان را یک "معجزه" توصیف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/126817" target="_blank">📅 15:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
معاون وزیر ارتباطات از بازگشت ۷۸ درصدی ترافیک اینترنت به شرایط پیش از محدودیت‌ها خبر داد و ابراز امیدواری کرد حداکثر طی دو هفته آینده وضعیت به طور کامل عادی شود. وی همچنین شایعه اعمال فیلترینگ جدید را تکذیب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/126816" target="_blank">📅 15:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGlBoa9zWRTuPMYMMUBHCVQhSVdfFZZgtMlqcarvWl6szyQ-Y0z1BNMsWCayRLn_4sUAK81y_MxCAIAj5WX4csuDS7QxTcjant6dzqkxw_0ZkyiwO_bCtgh0AmGh5MbetzNiEluLDw7ZPgc7ygsNeqWW1lfYTEPl6Rzn9X0UM7Cf5nxltXtIhqiS9gJ7f-fC4OZ3BAipm2yOnHnbo6doUiz6By6fFebWg_jNUTp05v-dPmj8XQISKzQIzn0blRyWYVlMugOje8rQNFXxn4pTq54c9lJtNtSXWctHdt3F1RbxaY_-SDqXcqUP-SDTjx_zTwcZzTvuWT5h_qwCQZ7CuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، عراق در حال تسریع روند بارگیری نفت در بندر اصلی خود و افزایش حجم صادرات از مبدأ خلیج فارس است. این تحرک تازه، جدیدترین نشانه از عزم تولیدکنندگان ارشد اوپک در این منطقه برای انتقال و عبور بشکه‌های بیشتر نفت از مسیر استراتژیک و حیاتی تنگه هرمز به شمار می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126815" target="_blank">📅 15:46 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
