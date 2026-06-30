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
<img src="https://cdn4.telesco.pe/file/FkoP_aIeIL4_-_inYPZro2KkX3opEAg21gfjMIaaHHMqWBonI0wH0NP7B1zMp9_tXARGNQLpQBLhpn8-vBOAwLZ1aGwwmFjStYdT7Ojt1pJias0tSQmw3qUZHuM6ax2iPaGj01C9cAX-3EdnCWYbkSH3AAoyKdgWRKdxJca61ijaFJtRyCvS83xET_e0hk0Jt_s4HmLIW99JH6RzpIrlJoF5KQM6TdfnzHjoUX5u7GqxpP8_E_ifu9k_w-Zv66zlX49xblAQJnVD_BxIABhHXMaUAvSxqSs77j0CHIjzii52kUIcOBZvE002_HJgdbEh8RIlT-NkM6M5WcmYOWfjEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 216K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 00:42:18</div>
<hr>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=VD8ZFjzLIQJ1S_ZpgZOBZv6LypkIZjZ3o0l0tcb127_0EizW1ymmdpdYxHeMCDSiamuWg3IOz9UDq4FmECFSzN7BtH0w52L42JYUXhpXQ7F7BrNVMD2FWYHjzzWQ2nAd9WpWycMSQJmwtBQc1zLEEMHqiTZl47-3Vw2tz3NywHC75ZHp_Hx94qqkMO_ewM8sfE2zVX4rkx5JlL0NzYlQplNG7F0_yhltsCtGDvEXTaOTLkmXjjeIns13Ip5SI6TrRLZaj2aMOolXJJuBRk0ROnJFbaR4FXjg_0uipN4JsRTDESIOuYDWv_nQxSgJ5fOIzZIVTS2WYCckiukwpjNt6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=VD8ZFjzLIQJ1S_ZpgZOBZv6LypkIZjZ3o0l0tcb127_0EizW1ymmdpdYxHeMCDSiamuWg3IOz9UDq4FmECFSzN7BtH0w52L42JYUXhpXQ7F7BrNVMD2FWYHjzzWQ2nAd9WpWycMSQJmwtBQc1zLEEMHqiTZl47-3Vw2tz3NywHC75ZHp_Hx94qqkMO_ewM8sfE2zVX4rkx5JlL0NzYlQplNG7F0_yhltsCtGDvEXTaOTLkmXjjeIns13Ip5SI6TrRLZaj2aMOolXJJuBRk0ROnJFbaR4FXjg_0uipN4JsRTDESIOuYDWv_nQxSgJ5fOIzZIVTS2WYCckiukwpjNt6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=mxOvuqvvf8KnMeZ25tJuqRFq3SKLsofQX1ArogW3QTRvZ5dv4--hyLjHXFVe_uKjAOY1vlqkIhYncRlXlWW4UCn_MGj5vCnYufM4LFstqD6xu84jN4i994r_EmQWWHaWngWFBcJhJtcxlkVRydPp_mXP_rLVSxEiDdN1rRRuKGxUeIvFskv5vLZfxHU9Q1RPRa30T3Fn3uys65pfxuSQDfwHfpWnud70RmVN6nEkXPxC8kPBZsIbnbK5E6lxPlBqocwqWc-HR38cyGQY3l6bCQqgAo7zCdvyHSxiVkvJ79sHeRIbfkpMw_KfIcsYox0e-3Q3z8mWl4N4EElq3LN_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=mxOvuqvvf8KnMeZ25tJuqRFq3SKLsofQX1ArogW3QTRvZ5dv4--hyLjHXFVe_uKjAOY1vlqkIhYncRlXlWW4UCn_MGj5vCnYufM4LFstqD6xu84jN4i994r_EmQWWHaWngWFBcJhJtcxlkVRydPp_mXP_rLVSxEiDdN1rRRuKGxUeIvFskv5vLZfxHU9Q1RPRa30T3Fn3uys65pfxuSQDfwHfpWnud70RmVN6nEkXPxC8kPBZsIbnbK5E6lxPlBqocwqWc-HR38cyGQY3l6bCQqgAo7zCdvyHSxiVkvJ79sHeRIbfkpMw_KfIcsYox0e-3Q3z8mWl4N4EElq3LN_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDwv2KQSR3uhiq-Vw_62tKvPSeCjZVsof6DyT8chB0Zq_rIMCZ6FbJ7hiGe9xow5yCMA0joDka3b8RzNb8nv51fxAZkwnM7leFkEiMk1N1QmAkDARWDNCLBIPiQtk4cfJZsrnRjqtQUC05r-chQexczEPv0pGLBdBJ69TSqaI5my18XLMuQIVJ0dTDj-JFewB-6ZVi88PpidHDfAlLf6pvjgBMpEMXIqzJz8WMW9T5t1HvTZ-CkFS8yHoe_hMcwN-a1EljzWnJLf3pCklm4DdEhGt5l7TsZTQC05UR_wnqfuX5ICSLbHProdZmTp_qstSRsm9oreZpA9_8wMEWvFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7hxqacCNitGEG3Yy-8R8Pe3o0aEkJgPCGLfuqn2hE6XPhtZhR4Zbphn2TBWe3O_1mS9MCiJ1zzE44dcJ8a2kUlNAkKikUUjzBTT2n924O0TcoYtIusMsLbGdOte2N389PZd1iCTk9tGZ9YE-8EoR2NSMoCY9sjBa_TH22SKq5qlHpgK-D4aojndzxWLmvn9WvCC8wEwNQq-SCryCkLXTDKz5VzMZ1oIK4RUeBCdw2TjGQXsc48gtuL5rwp1FVFiHHZcfxq74BCfsSnMnTw2DgczTgMN9bfpodCYN-ZMCNi-7R9D4q12Lpv0Pp_G7eUpID424iOXuQELLhO_egq5Yxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7hxqacCNitGEG3Yy-8R8Pe3o0aEkJgPCGLfuqn2hE6XPhtZhR4Zbphn2TBWe3O_1mS9MCiJ1zzE44dcJ8a2kUlNAkKikUUjzBTT2n924O0TcoYtIusMsLbGdOte2N389PZd1iCTk9tGZ9YE-8EoR2NSMoCY9sjBa_TH22SKq5qlHpgK-D4aojndzxWLmvn9WvCC8wEwNQq-SCryCkLXTDKz5VzMZ1oIK4RUeBCdw2TjGQXsc48gtuL5rwp1FVFiHHZcfxq74BCfsSnMnTw2DgczTgMN9bfpodCYN-ZMCNi-7R9D4q12Lpv0Pp_G7eUpID424iOXuQELLhO_egq5Yxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=gNtp01Fj5iZE8lHjmaFEHPdExbD0vLLY07j8HGUllyZSRrEdd3byCgPZAx_3HMgbUdrg0xXhciFaoIucxlBpDkoO3N5vOHuhnJMCWGbTMctUfaDYn1MRgE4MIbzddA8HU1amMAI9eqTVdDqjzy5i8gaLxOx-Z16hNk7WNSatEA6WiWCoFOAb5eWL4U6nY_TRcwN3TJnEzfkqzoeu2l-aNcjLId_iJ7gNz6wgDwi346yJcuVT7fm-1WLzBUnzBwkajks5nOqtyD9tlySqs9g_PP6xOnuzhPaMifKINcoPY4NOVyiSjHiuWkyzL2HhVTR2G2gGo6fRXc_rfw6IFlI8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=gNtp01Fj5iZE8lHjmaFEHPdExbD0vLLY07j8HGUllyZSRrEdd3byCgPZAx_3HMgbUdrg0xXhciFaoIucxlBpDkoO3N5vOHuhnJMCWGbTMctUfaDYn1MRgE4MIbzddA8HU1amMAI9eqTVdDqjzy5i8gaLxOx-Z16hNk7WNSatEA6WiWCoFOAb5eWL4U6nY_TRcwN3TJnEzfkqzoeu2l-aNcjLId_iJ7gNz6wgDwi346yJcuVT7fm-1WLzBUnzBwkajks5nOqtyD9tlySqs9g_PP6xOnuzhPaMifKINcoPY4NOVyiSjHiuWkyzL2HhVTR2G2gGo6fRXc_rfw6IFlI8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=nr0KPM5n_1384L_7R6NunEg767wDRtL_pnKmjEwOCuTRcZbmBh_S_S5GEspYeCDZRluAeP9Bfcuc9H6klWxLedNamKkfE8jiffyEjTENkjOLXgQ0_gdi1EkekEuF0UKsE9k6VkzvPwa-Ayo0NF8WmUlCVJ-yC6Sf8Y0FVnkv2gcG60vDwzvkjxlxOx-kfKFcy52Frydr7jqK17BDvMbOANg7byQCxwEl4LUVUvs6c97i4IsJY-OpIQk2YRZwG535fzCyJvqzKMnw7fn4WdjteuIEbw72hvd-mSlR_S9xVcS1tFCqsP0Qex6PpPjp7zfdySPsXD561liZQQLIjnKhmY_bDois8e3FSFS9bHMe-6cEJhcWCUPOCqoMVf_dXXCzS0NygQizVhGOh53g9zCrma25qh0bIK6p9qMScI3z6koBqAxbxOwx4GE9_krimxtHgY5DS1N85eUgpsv3k1bahV11YT_8SknCj9vNT3KUPQ0dhVdgzm82gtrY6G9btRBpm5CVyrs6bG25kxxSbCsONI8yXNzvuSi3Juv0DhN6gkblD4wtemkBSZx9panEmxtY_1XJ65fWvJ_5QXnGXzQ0Hn46VPhsxW4Swj0QoeNugL-si43Wth9H-wTNloLyrcSbXbyhyygxit-4WRJ1NuipzdNwQM9OwGGS69RAA3fm_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=nr0KPM5n_1384L_7R6NunEg767wDRtL_pnKmjEwOCuTRcZbmBh_S_S5GEspYeCDZRluAeP9Bfcuc9H6klWxLedNamKkfE8jiffyEjTENkjOLXgQ0_gdi1EkekEuF0UKsE9k6VkzvPwa-Ayo0NF8WmUlCVJ-yC6Sf8Y0FVnkv2gcG60vDwzvkjxlxOx-kfKFcy52Frydr7jqK17BDvMbOANg7byQCxwEl4LUVUvs6c97i4IsJY-OpIQk2YRZwG535fzCyJvqzKMnw7fn4WdjteuIEbw72hvd-mSlR_S9xVcS1tFCqsP0Qex6PpPjp7zfdySPsXD561liZQQLIjnKhmY_bDois8e3FSFS9bHMe-6cEJhcWCUPOCqoMVf_dXXCzS0NygQizVhGOh53g9zCrma25qh0bIK6p9qMScI3z6koBqAxbxOwx4GE9_krimxtHgY5DS1N85eUgpsv3k1bahV11YT_8SknCj9vNT3KUPQ0dhVdgzm82gtrY6G9btRBpm5CVyrs6bG25kxxSbCsONI8yXNzvuSi3Juv0DhN6gkblD4wtemkBSZx9panEmxtY_1XJ65fWvJ_5QXnGXzQ0Hn46VPhsxW4Swj0QoeNugL-si43Wth9H-wTNloLyrcSbXbyhyygxit-4WRJ1NuipzdNwQM9OwGGS69RAA3fm_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=EDGiCdzsTTxZnC_cDWJLIazQDoAhewA8PSzrFze0vSrJxoUgh_p9a-6f8j5tz5o1EQXdtyP61G7GqHxEksMXSr6E0jKbI0OcJyqvBy0gKIYkW_i6HA0V3t8t_7b3-9A1KTiOn4sfEaDuMEGWUupmp42D_V33sWqlZKLouSKad_Fn83sruQURpHjfTVNX9BvuIbrvq-07oBpgcLx8Pay6pUn-6aYdv9o5Cb_k5YOStDxmzsDvwC0dWtbVsW-pHtNElCv-d42q-CknzekB_RDwavlideFdW9dAgk6HXUsW-vagMZQltBMh3xCOkCqGQ8E6iPxDDJMrfUldHnl5dM_lPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=EDGiCdzsTTxZnC_cDWJLIazQDoAhewA8PSzrFze0vSrJxoUgh_p9a-6f8j5tz5o1EQXdtyP61G7GqHxEksMXSr6E0jKbI0OcJyqvBy0gKIYkW_i6HA0V3t8t_7b3-9A1KTiOn4sfEaDuMEGWUupmp42D_V33sWqlZKLouSKad_Fn83sruQURpHjfTVNX9BvuIbrvq-07oBpgcLx8Pay6pUn-6aYdv9o5Cb_k5YOStDxmzsDvwC0dWtbVsW-pHtNElCv-d42q-CknzekB_RDwavlideFdW9dAgk6HXUsW-vagMZQltBMh3xCOkCqGQ8E6iPxDDJMrfUldHnl5dM_lPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=POOQ-JMitB0WQORcxnHRvJIoevGIC58A9lwpzjwBMkck2wfaHOdaJJKblThRT95XbzBnT3lOpGMmKyxVfW8aiVQrPsU-C3shkNrEtQENkGWS1q3VTKy9eEmh1H7tu9TLXtgdvpzvMrf7feE9JskuCSO8cuVczizkZ6xzH9gQ-OuJHQzHUJN0OJft2yqOWQPr17Ji-1CNfIaeJKbgMKTE-ZLHUg9huVSnhHxVV5Shg9SVaggVHVR4bsZ1-6mVUrcN3JDejhM4ownEITFTFDwJ4jn3Q-2AcImMAebonpNlk3wCFrqcVNcs5dWWi_r_j9bZPJxIBW_GL79HyGrOW43o1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=POOQ-JMitB0WQORcxnHRvJIoevGIC58A9lwpzjwBMkck2wfaHOdaJJKblThRT95XbzBnT3lOpGMmKyxVfW8aiVQrPsU-C3shkNrEtQENkGWS1q3VTKy9eEmh1H7tu9TLXtgdvpzvMrf7feE9JskuCSO8cuVczizkZ6xzH9gQ-OuJHQzHUJN0OJft2yqOWQPr17Ji-1CNfIaeJKbgMKTE-ZLHUg9huVSnhHxVV5Shg9SVaggVHVR4bsZ1-6mVUrcN3JDejhM4ownEITFTFDwJ4jn3Q-2AcImMAebonpNlk3wCFrqcVNcs5dWWi_r_j9bZPJxIBW_GL79HyGrOW43o1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=I2lrf2HwvEO3LL3tH-nqYcVFkWA7maaw5dVxP_6vLeWeXz2rhtrY9IOQ9hYtQ7zGpfjf-7jH7gBL3abENelJrQAxDa3JbzN1axXtxKb2u0tLSigI2crmcQor5uMs4Jm8fQZoKWybUKdq3_CT9HgFmZUxA5N04pJOWkBkWBx1dI4ySt4wDNpeI2NmZ-70Aek7zCDos04lkT9UsgMJxsrvPVN4NjaFNfEsy9y9tu07cw59ghbKnupoJBezZKrPsaKYG_NeMWOFW36BQ_iQucqC7Kpn-kocBc4Ng1ld4xVD3-t2VbkNfPlg1wDZdbni8DlraAmY8frH2yWeM_fVU2HJNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=I2lrf2HwvEO3LL3tH-nqYcVFkWA7maaw5dVxP_6vLeWeXz2rhtrY9IOQ9hYtQ7zGpfjf-7jH7gBL3abENelJrQAxDa3JbzN1axXtxKb2u0tLSigI2crmcQor5uMs4Jm8fQZoKWybUKdq3_CT9HgFmZUxA5N04pJOWkBkWBx1dI4ySt4wDNpeI2NmZ-70Aek7zCDos04lkT9UsgMJxsrvPVN4NjaFNfEsy9y9tu07cw59ghbKnupoJBezZKrPsaKYG_NeMWOFW36BQ_iQucqC7Kpn-kocBc4Ng1ld4xVD3-t2VbkNfPlg1wDZdbni8DlraAmY8frH2yWeM_fVU2HJNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gw8No68lp9wWVHExlGYMWIzRJ7U-Pmp38-lKUJagida2Ot8jJwTKr8IuxewJ38ehjCASkJfo1-q0gyKAxZPyXxidUpi-NYUAl1WdT7481L5KW-TYNbEi38kYeSnfgIFu3Bmfa5z29njpCXFRuOMCowInGA5kciSmfZjjfXcGW_LTUIAMGxLy9DweQWwZi6G24eMIX1qPsdCtGTzi2vb6wb2GYCjSvQhmvFqAmMXl-oSJNMDDz1C5XTh6ZNS5-05fdgDsugi1LX843keu64Okc504aMMC7ezFjmkJjhZON0R8zEYmPB_GRzV-o08FzlzuPA0Wkl-XYRk35ZAtKesKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4_JVxkOlUfZEp32xhM3-wRs-fAtZ-cUabDYhytdUWY1zIlxzUQadG1CFrt5IzWOfiy9kRkiystB_tAp8mHvUDpP0wQt-DTDypXB7dc3Tc0X1Xl-kUb62Z8pYJHNgfJ6m8mQXT1UA5v-AtZJrqoGfxvhZvWPeEuGqs6BxrxdFv0oWlo5Z7zsQQbVf2X0_267dAKjdy8IicDGqKK4paclgxuT5YAoPhuVKYjNxbcWJ11zsFQYHvuvZhlYcAqtnLUzEf6kW-mjTB2U76ZGWMCd5Bo1H31h-SCDcUBBsyEqSkJNsjjFsF9r6eTdQpNazkjhOxDQXzn-OdgGD6DUTQt3Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDQsQxCBpCK6B-b4dFVzg2sEdHj7sffq4PtiYSy3y4kNASK_m7_9XPsmQe7whKL5HYbORklMjHJ4u-fHFtysX1SZ7lbLt1a06o5o8cgdAuLtUIrgygNMNSPoV2mSk_Im71_Ymc4UxuPbQiQJ7s_KLrmNpNdCPi70cOcmhETtj_179Ddw2f_4Efh-AbnqYcHNHf1hWEDpHzq7d4gvNypYCUuzjSh-Wsej2sYeyGs6zMqE9_aexDAjGkHRDmnlSdsAroM9EjlCSoQ3VFoCldzqp3dK_QwMw34CJNPd9byekNLsOSrNW2QsyYthq7CPg8PvuTfYaYRVgG04LrhD1s6ylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hn0HRuSnra2IoQNIKzDtnSh3pvSc-yK427wN5uHy9QSzriHWe4tyY-RgIw2RsA2VysVdawrxwvmIbRNN6fLtqGYTs2zP_45jaWD9U0TQodHSlPpiSNPDQBlqAikw0DtLN1Jt5RdWkanYhsVwgY6ZIn98K7D1MiThRxNtsKewO6iljnDr89SlEEuMU42ePkPha8rUYMI18Bj5bJx0Dcu7JHD5XeEPtcj7KTRRPjtzbF2dr2mQ9R18FICTDb0X6iv2y4cBFwxV3W5cIYaPqdttdgqKl4PfmW8OZfFf1tXLff4F81qwY7x-G2frI271NpXCLLD2F3xhwSK_NOiwaQxJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE_Q6vbfr0ZwC8vOptYr03-M0qz9SCjp20l7BVespeY5sYbyxOYDKCZG9TRV075kPxl-2Urhmy8bhBJR3PR5kieT2KWj0R7Bf-LD0lrFwm2CjS9cGlFvV-0fJvFax3ED7368UknwXIF_LDvP5Yc-OFTW12uAWTBfko-i6RBBpr_rEYAAPqa1CGmobg2b-5ZY0zYsf26Ii4VMfbUYcV7o3RWZU-6ZNbI5i645GdUcBJmtNfSC2mSUGWnxBYmphhq4PEZcNSlTBiFlV7GpJcTkjx-caT-SUCmSYm9f6J3lk6GknqTyA9xWseayPkwQ5SgpoanxoR8paAECABhQ6qu9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzvNKrYOm9f3NbUw7shrZtFR34D5dkYKHM3Mg8gn2k-a2K0lNZLcrjZOx2yNiZXEZWytAsLCSMjZDSn3csK-03mGgvXvTznZyq_HqqC6N7U9FABKxM7slUif0BOJFjtULg73Ns5ODo84tuHOkOa9FZjuJcBYfWrK6jN6xTRxE9c2dnBSbmb_yClG7D-ep-zceVdAAnWx8pP_xKa38kDp61Po_303WLAN9iIiz9-OiUD_3uhqBl_zaasmbJULSOTaL6AKBW-yrn1JbM6n2UovnAKCLbRvhTrQLBSqXLB6bd2K7ukn57RJVAVhalGM-Sr-kymKiF48BmyRF4blLNryeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OHDGa1HQv6JcSYxWgOuLpI9xGy0FvC4kEOj_xf-lpa2V-IIjbHK1OoEFoV7HSY09IAWYD0rZg3Xk9zdY89RY5b-EiOfEA7nFquSu11DsHcFvF4RWqYUd2MaB4-RAkbGGREjnsizbtysMiA-ntecEQ8Sgd-51TJqgVlCpyCt15W9gO49U0Wj3XLsdameYLsHDvjq3uuqkFZi8Dlza4XXdJjXmCZuZZW7osvRMIxJVM3UTgrbkZ1HZJlpuJJ_JA6Q7hXgJXBoC560Rc6PA1r74UY409ZJXp2k6Mcm11dwXMi22pK5miMYpLq0Y2iCS_KdHWziHG6HzpmqP6rMKQO6uSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OHDGa1HQv6JcSYxWgOuLpI9xGy0FvC4kEOj_xf-lpa2V-IIjbHK1OoEFoV7HSY09IAWYD0rZg3Xk9zdY89RY5b-EiOfEA7nFquSu11DsHcFvF4RWqYUd2MaB4-RAkbGGREjnsizbtysMiA-ntecEQ8Sgd-51TJqgVlCpyCt15W9gO49U0Wj3XLsdameYLsHDvjq3uuqkFZi8Dlza4XXdJjXmCZuZZW7osvRMIxJVM3UTgrbkZ1HZJlpuJJ_JA6Q7hXgJXBoC560Rc6PA1r74UY409ZJXp2k6Mcm11dwXMi22pK5miMYpLq0Y2iCS_KdHWziHG6HzpmqP6rMKQO6uSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaoHAWLGnm-SsJHyNFl1K0_Jqc1hb3oHqoJvYY8wF7SmxWVca1Oy9Rayl43kp8q90pJJ0vhJ5C0Uzub6b7-Vy-LlrSONLHf7qWjCWvDkkfwjNlrKdtofdVT9P7Cv2bDaC1F8qJbtt1-RQsk8kiLEYAO6s3C9CNN8AGbhVqA9koxnOFU0MpSAPnTLeMUm07v3kpq3VHTTVhw7se-AEDpc0QK8AqTR8Q1boD6TPbqlhIOzYOEaFB-iFWxrd-I4i-WRoWxt6k_i7CGnsxzisVppDYKcp-7b5klSKGqIfkOcvGPAoC5NJYeaHau3hQWumEpHT4t4zXTWV4dvNuz7i1XPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfG9YDIHFfvl-S_btL325FsNuwgg-TWsCjRt1pjTPW8BqZ_wkhMHgvq6Ga8MkchVsjZGJOM86UK3V5S37ts5wrt5ToRdvuDIyqiwe22MH9R4NhRJ9PekzC10Yg83YO4bv5w2uKb7RhUvggFB2X4xoaDPDx2prqSqhcVAo6AWn0plkxDGnUK6vz2AGP-oLWoT4aRKo4t625QgIUcEkohLjp0FwkhZIYPkrqkx9nNfFfgzts0hOrfEu9-Jj3ZcnbbwRv2gpWiCLiwrN_zthAPCUAKVrX0MTmmozx1NZk070MwMTfgW_tKiliqc16rY7Vzf1i-UmqYeEspgxbb6GYlf-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=vBrrYymBn_qFyVm2h-DvytUrN2Gyj_SjESTAbb1eIkXap8bsgcS5zoF4WV2UeLhrELmQW1C2aGoOHVw9M2DQNuBnjXHh_-M4ZU5WgZOK_fCxKih-QE1mbd_I9MApMeG9mK1XGJ4xR-BqBADwaJqMzVmjISLrofsqgHJV9XB8ScB3UPnWq_8hCqH79wav4oVMNk_kgs86NhqBqfVjZBRAIMJ9rAJ99k2pqHBY8uytLrAFtOt-qmuNgCuqEyDHvdbPG8ISvYcrgtVEU6WAHpmvT-hcSiWFI5OOgoAge_hhf5DzDvgIbHoFMeoksdjchH1Qmaf4-IgHM4tqNTR1438GNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=vBrrYymBn_qFyVm2h-DvytUrN2Gyj_SjESTAbb1eIkXap8bsgcS5zoF4WV2UeLhrELmQW1C2aGoOHVw9M2DQNuBnjXHh_-M4ZU5WgZOK_fCxKih-QE1mbd_I9MApMeG9mK1XGJ4xR-BqBADwaJqMzVmjISLrofsqgHJV9XB8ScB3UPnWq_8hCqH79wav4oVMNk_kgs86NhqBqfVjZBRAIMJ9rAJ99k2pqHBY8uytLrAFtOt-qmuNgCuqEyDHvdbPG8ISvYcrgtVEU6WAHpmvT-hcSiWFI5OOgoAge_hhf5DzDvgIbHoFMeoksdjchH1Qmaf4-IgHM4tqNTR1438GNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=D8a5GLdpUfOkdMG_3FRp7W92p_JRPV7vE23uGUnXcRBazmJzVvEInpitTIm5GFENIRiwBc8FHWEf6-SZnpU7KdqPypscIdqDcQLVudSQzeVrUA5slanDv4rTVyKS_6UVne60cXz_1xMS6iCglUTTGMze_SHeh-fTgGfOAqThpsijvglCh8UPXcwqRi3l5RtADQSrT7watIon-pD9CY39_L7-ClrK4l_RVBpsKTOsBivLy9dnkzL-rwSLHXQ5iDhOzq72hQBPbv0GBs_FcPsZL_AFH7serlPKMkTyWuDws8L5-p2Fa8CMeSQQHw7X6dK5ziWKDNYEPpr5KRRGdg0vOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=lL9TP8EvNLmDBsDmATvfD7eALDHe6JV6tLWtE5NL--qBQQnJFyQQvw8-snroeup-DPmvihCx0DQuCcktQAA4F1Q1BaLq3KFzFUZgjQ60q8oDLCSGtApI_OTHzNwMyqWJyzOfOTZNDOTLlNeGywuHaTgMrZ-AIn4SDlbW4kNZHu-ply-cFUA5KuXqt712hjxOKyHx0vPkpvJ3jIKvmAqsKyxGDXFpABu33ezVCstakAsjs5WzkK-HN14tOHB_eVd9QCOBXSLcLwjdISwXSbu1racwDajWcBPu8DmAlYiJUjYQGo5xn5AMKRo_ZxMHz9GWR4rsoKbY_1Dy3et6ZmvdVzjxdSLhaFZfqgRgeNPJsEBL-Hmq80I_efTVoLWkzvKUqlM2n2jpPAfKma6pNMperVxr0MwWFbnsjtkIyz__pZTW3yDexP-_DHGBdJVYR_FNVqxpSqM85emy5f-PTxLeuqW4tzYlxUx2-ka3F-5sSJ57iYsDghgfNlVlXFpU8MpBNhvHjX0yAuaRpA-zDmkEXM_O_yleH0QS4DeL5L-zCQbmxWZAPNJCZLdVN6S6gLsJCdyvSw1N9LcCI2xU8MSXUvmr7PmzTaOmMvjiquPY3a6T3w36CG2OawLgYJX-dZcO4q1CUJKy5UKT4H6KLl-GcOouEXC9a4ZJwYZ4Eknsbdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=lL9TP8EvNLmDBsDmATvfD7eALDHe6JV6tLWtE5NL--qBQQnJFyQQvw8-snroeup-DPmvihCx0DQuCcktQAA4F1Q1BaLq3KFzFUZgjQ60q8oDLCSGtApI_OTHzNwMyqWJyzOfOTZNDOTLlNeGywuHaTgMrZ-AIn4SDlbW4kNZHu-ply-cFUA5KuXqt712hjxOKyHx0vPkpvJ3jIKvmAqsKyxGDXFpABu33ezVCstakAsjs5WzkK-HN14tOHB_eVd9QCOBXSLcLwjdISwXSbu1racwDajWcBPu8DmAlYiJUjYQGo5xn5AMKRo_ZxMHz9GWR4rsoKbY_1Dy3et6ZmvdVzjxdSLhaFZfqgRgeNPJsEBL-Hmq80I_efTVoLWkzvKUqlM2n2jpPAfKma6pNMperVxr0MwWFbnsjtkIyz__pZTW3yDexP-_DHGBdJVYR_FNVqxpSqM85emy5f-PTxLeuqW4tzYlxUx2-ka3F-5sSJ57iYsDghgfNlVlXFpU8MpBNhvHjX0yAuaRpA-zDmkEXM_O_yleH0QS4DeL5L-zCQbmxWZAPNJCZLdVN6S6gLsJCdyvSw1N9LcCI2xU8MSXUvmr7PmzTaOmMvjiquPY3a6T3w36CG2OawLgYJX-dZcO4q1CUJKy5UKT4H6KLl-GcOouEXC9a4ZJwYZ4Eknsbdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=sAjHB-Zx4EOXg8TUI1irCWqv_bX8YYWoZfdncx4m3ceEosD51_uKhyQ77K4t58dotjQCpXtjoTLO0xMhUT3WekfRe-W8S4BhHTHIl2N7p4kUMjiAwpGtmjwzZIIFNkzfvFqgJMUoQk2YUH3kSypazWicV9bkgxls8G3j4MOm6CjJVXuH9OzRkdnKAHTjEQZ5KJ18Y2m-PPgOWL3ihVsgXWIuVLccsjB34e53hXyQ5ijItZX78823iuGS6gt8dcmw5cOzppoHfQmdyJEyUN3cQoNrKr_HNmCgDB9KCCT8Htr2e9LDD6008l_btcg24GEQmQMGyq39fh_dHiFFwzy1mHtNmklPUyzy6SKqIJj44bo26AZgfb4wr7zKMrnissJ3DhNz2Zr46FfGwXwYwPKNFK-pX1Bt4NLKUuXC8D49M2k32A7LUWhOKWS1l-8D4ZGhOsv87SQEZux24oC0zjKJ0ExLW3meh9PL3kECZhbE3goi9acpScQwFZZacYrbSyjmQyuFbSf_BSE1Xke-ZunyuGtChQkLLM8g_CLrdfKtHRMQI6OzDmMAck9LVL820I5abLqh4xvIw5eYmF8Z5Sb1e5tSmhAAXaTOHMyHgH9XHw7fnTYc-81wVHhioMWWaMDq9jNG6Hnpb9GTcBh7Xhe6427MPStLkgdtZ6bpuPxqKuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=sAjHB-Zx4EOXg8TUI1irCWqv_bX8YYWoZfdncx4m3ceEosD51_uKhyQ77K4t58dotjQCpXtjoTLO0xMhUT3WekfRe-W8S4BhHTHIl2N7p4kUMjiAwpGtmjwzZIIFNkzfvFqgJMUoQk2YUH3kSypazWicV9bkgxls8G3j4MOm6CjJVXuH9OzRkdnKAHTjEQZ5KJ18Y2m-PPgOWL3ihVsgXWIuVLccsjB34e53hXyQ5ijItZX78823iuGS6gt8dcmw5cOzppoHfQmdyJEyUN3cQoNrKr_HNmCgDB9KCCT8Htr2e9LDD6008l_btcg24GEQmQMGyq39fh_dHiFFwzy1mHtNmklPUyzy6SKqIJj44bo26AZgfb4wr7zKMrnissJ3DhNz2Zr46FfGwXwYwPKNFK-pX1Bt4NLKUuXC8D49M2k32A7LUWhOKWS1l-8D4ZGhOsv87SQEZux24oC0zjKJ0ExLW3meh9PL3kECZhbE3goi9acpScQwFZZacYrbSyjmQyuFbSf_BSE1Xke-ZunyuGtChQkLLM8g_CLrdfKtHRMQI6OzDmMAck9LVL820I5abLqh4xvIw5eYmF8Z5Sb1e5tSmhAAXaTOHMyHgH9XHw7fnTYc-81wVHhioMWWaMDq9jNG6Hnpb9GTcBh7Xhe6427MPStLkgdtZ6bpuPxqKuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=TLqD1UKL1uRj3YWssU38DXMrRJNTZg_l-9yi82Ehprv7E2xSt63NNHfjTL80ur3banErNAr4FFbsgd3bTolwCdDJ_TLIb6PZ7_Ta3yFzXS-Sgopxx7X75Y4TnyFh9vf_u0Me5a73oF6-k8g4J-QNEHca4s8i5uqmT7TJ-Yk_PHvbtAxZZ4kc_e3wp1KG2CObprMFyIMm363FispuJBMTyDk6jnsCUV_Yk5jPHiqDTbc0eW0ZZPXJUpjD7cM1z03ndtvYQcoOkkvyM8o3eNz5ZCV8ryHrRXItl1TRNCrZOmpo6RqqJWwN3Na5wjBKUcdIU3WAhda_5lbBw8JXt8dWBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=TLqD1UKL1uRj3YWssU38DXMrRJNTZg_l-9yi82Ehprv7E2xSt63NNHfjTL80ur3banErNAr4FFbsgd3bTolwCdDJ_TLIb6PZ7_Ta3yFzXS-Sgopxx7X75Y4TnyFh9vf_u0Me5a73oF6-k8g4J-QNEHca4s8i5uqmT7TJ-Yk_PHvbtAxZZ4kc_e3wp1KG2CObprMFyIMm363FispuJBMTyDk6jnsCUV_Yk5jPHiqDTbc0eW0ZZPXJUpjD7cM1z03ndtvYQcoOkkvyM8o3eNz5ZCV8ryHrRXItl1TRNCrZOmpo6RqqJWwN3Na5wjBKUcdIU3WAhda_5lbBw8JXt8dWBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzHg7nZgAStd3i1qzaDQ2iPoHRhxKl4pDicOUHsIfUkh8p-9G2jeJMAm0Kf_1IZYi1GaRizrqcqMLBu2kOJbQ2XDuDrqxgpwLmTGuaOrn-jJkZ_xVUWyAWWZCFQAdGL_zvflYS-DOg5amRZNRR7Crp2O40GU9WN8zineStI3jn2B79Ji7K6mvhX8s9yKSMz7R1a52BCqA770l5C0F6hm78CYTv0bvXpiVv37YvLQCxjYQrR6O6pPFHqM0E1fdU6-sEkWZrxfqlX4xajF5btiF4g-PN3y0YMeeCINoxnZfviFrNYGxiwbjB5CS1CksnNScZuDQiUaEG8jAq0dgBmSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcooBHFheC8WEJKzTMvrtqaMMqgonozgYBUUjnypFRCp3p4XuUdHTxO9dg8l7FT-z3V1Uyx1_sHiMqH5bs5cIbZJZxK5HuvWvpeigKdqsMRYRIMVzx34-moGSc6GlS4fxs7-1-VdS53JLK-62xoVzrn6s4mZI0n02OpIrPLlhhff6sYJ_BRo0YcGxeY0f15J7TPuuSbi0JqKKH7lLRN3JagK1KykNh4piGKQSv2Pcha27gzoMhQX7qK9nhgVT_kDDZDUw95HtjqWSyTDAQkICCY1Er_E8DMBSUwfreJPOZbIc_gvV9XpshST02nU2M8Db0LQvMiHXo7LhzPaduBFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=vRFBr5UyYm9W4kyRJWZP4rVQO_YgrJ0qMUyVhRLAqTT7kOuAq6h4qhA6WwajsTbgx0GYCFM6SCUg6s5ie4mXgTzDaze4zu7hJl0Uo3eix7VDkPceujr9hdeNR8pKVaD0DRZgnOv7trr55WK8bDeT82MXF0vbxfvz4hzUTYQFQ7B0OvTf4VVcJaMJD8Tp0WIyXGjs_QUZ7vp0sLjjKbm8ciUaFt_mbRQl_kStjbllbrLTimEPG_xQZhVUwnCvSDI8cNP9LoC_ooYDq32wKwgDWqIpNcjahdqjyNZyGyW0FcP62Wrdd9Q0HvWOFMGea9mJXVxXLdwVkiqnKfRsB0QXcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=vRFBr5UyYm9W4kyRJWZP4rVQO_YgrJ0qMUyVhRLAqTT7kOuAq6h4qhA6WwajsTbgx0GYCFM6SCUg6s5ie4mXgTzDaze4zu7hJl0Uo3eix7VDkPceujr9hdeNR8pKVaD0DRZgnOv7trr55WK8bDeT82MXF0vbxfvz4hzUTYQFQ7B0OvTf4VVcJaMJD8Tp0WIyXGjs_QUZ7vp0sLjjKbm8ciUaFt_mbRQl_kStjbllbrLTimEPG_xQZhVUwnCvSDI8cNP9LoC_ooYDq32wKwgDWqIpNcjahdqjyNZyGyW0FcP62Wrdd9Q0HvWOFMGea9mJXVxXLdwVkiqnKfRsB0QXcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_qKH_xiHrdrHRlfBrkTI3objswcpNS1kkCOZF1jUUArYCY5iVVZTJZBxvP3RU1Rp6LcbwyFAUHBmS-bt0BaaXxHi4EXI6hPHl081--muZviuRPlCx_917O2g8iZiT6M9iBFb2lSH7fTlSBMqxq4kgE0c4Hbey5qG7r8E3qNvdAKnwAkvi27l4w8bldYl__NmBdaYAvW26L-o6VAPRt9kuVOW4_mLNjSQAeoAHBMS9FwfZZqwEWmtyDJBImF_kjy7k1nKd4_lBu6x3w_lB3q-sf_85E9HvKxtRYkOFpXnW7PGCWsE2rQ_-nM_U_r1NSTZStMSg2iyPbcYj6pkHFY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJMj3mAJE3Ir4G33bV6XA0GEyXH5EbnFMwAFXmw1hiPI8kLbfdOR_B4sMdzhoUrX2sOSBZkkUqBDJybXrKvsapuVc_nLgrTyI8rOTa_yqndUXxLhMfTXXFtCtq41KcCmKZLf8KGuF7AOeKPSkejvfkVHGChhPx8FvNf3G5lmQB-BLNFqQkSxI7PQ60QBYfRm4yCPyaELqw9W1ST_8FEh-PC6NRQTwgDu9wtFrYXr-WEtGRqBLEFGVTXZhuYRniLt2OM5lM7G2lLF_u7ca89VCVQHNewxMIwzQgdCqzMYLjpJSr9GXNR8XDHy87eOT3O39LCP6EHJohA7nU421xmp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8W7BnxqGbOLiZtnek5aICelEauX08rsAYtRpY0Pd9zTBe5wBVHUxRiNKjPUmnr-3_1eUr05I3a5YcUtvVgyPWrId7BpewexYiEqncfw4XVK2I5ChsdWx87TNljnsJigV4-yHlnh-3uY_AxM52-8PwUDgTTdqUQ2phueXoVTmz5jimmIyrMxHNK550xH085iIN89tGWcJ-d1Re8-BHHKl4v8PHK5vv2A4NKSj-KSrRD78EsPwxsVMrhSq4T6dgXcDp7CF_c8EMEMKuxVxKCqqbczxDSNQCdrDrd5OnPznJIQ1zM2quGXD1zlIzrEdlxnb4dbZUFArvCcgvaLtBOiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bReYRhxD9r-YQjR73jTJmspXLdhCrB0fufTtRlNacdbSURNoPh_3P-Tz8QFmdA-I2nX1bsJQlq4peig8FqHLmQZpnW7kh3OUT-TCHbPm_H6eHbVMDU8gHB8mYceqUUlb9aVwKAQI2X_efBP5in6i03ISLJyD8CyAgMoXp2bOyuxCYpgtCJvBWiA5m1OjSXCkMjj8DORyaMUHpJKY1TGE0ZL9vtNld8npdVItsOKcyh2iIPylYiwAxV8UE0dEtfiVPoYo5uy2Y_NB7hBDpLZLNn1pAmfs5ndtUHyskXbYeUKovIx6uZ-yinJ_anQWtnyld8kG1kD2D3dFDi3eQpG6aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rvpg4y1M7SsRdQ98M5Y1f4-tiFUI4iinfYqyPnU9mMogD_UiIlUg0lscpC34pIShrAGrSskc9Vi8ebO1bBk6WmrkN2qc8kdCcHLf6kRxDLMCytZ9Hb_G2xOetejNzrgloH71X1B7ijEOaf1PFbVbrea1Qe5BwbZdw8Fv0zupwX3HO-YtAUtZwkkKUmnZbXN9xXovo2Z5-Ya4TOrgysTwzMUK7mG77vpL7_FPIgPebG2XQkOoV3DJMXb3dzPITwCVvXnhc7WShSJnyVIvXyjARJ8ejL7oohmrH1vu4wsQ0zkpgV7X0nzVHT9EiltUmJ51oLXwEv4Sc3P841C2T00Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeZEIRwJxWoR4nfR-4ioZYYyQxJ-2DvDceHCwR0bGeCrT0Zbc97pfeUXvgKQkSNoO3r0Yx1h0rJVoeHI27flJ3TtfKqecBq-I7puD33xxw7FX35OEnl_FI_42n8JEDzyzH7GUvoNJt4eUNUM1QXCTMGkcQLFADCwE5zb1TtXv8IO2Lv8oduzLH314F_uWsIaGxf_7dNzR-5X4tyUkjmZ0D8r-57p6anEZlKIIF5hjvxV41z1p5rbsqV14oP4Yku1YyORJK6d19QyOZXXdRDrhCNhJCZKBVjdZKW7e0kFEYez6BZapVGTseE34GOT83BTPkjqey7ipiGRosFpzALgsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk38KDy6znmqYVGv-nwJDpHoBmqOgvMwfc5_XbALGzBdRtJ9oJDH1219hbA6_54hQ7OQDITkEpGqO8N9a84Sa0XnJAkIujeMPB0kcIRMXBdjdcEP5z-OSVshQ6WHcHqm4RQ7XCgBYsLR1k9SGrGGwN4qdMzTRDWm91vTgC-z98vdjVcQwBdOqpBruu7kVlzxkusSlk8YVVZ23DQbm9LX3_kskdCUaU2LVyiKCNCoBztgUR0iFULKtYGUSnPdSDUbym-WWHf5cynTlMYB2wtMyQ7j7NCHMhz4VdCIlbQTJTWHEX_yBkbGwuZEO4JxUhTaMIKOBiIgx4g-dckV57qlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYJLBVu1bKcJ-LWcFdUHdA4-2vitY4YlJGOsMYxutWmnDl59wNXIQ_bwm8MH4De5r8-T9_JwjaGl7gdW6N19mEdSB468aGOi6S7GPFWs2e7_wLch7Q501tOHdw05cK9BEECZjU3mlcYsYMep8cpb9SSDxNjNpbCxMj4pYfoLAXvdvKSr5XTg4csN3zLGhh4PzdZWYzRl17rJ_038Q7aJhDuhd_V794r4SaCbxI9o2oyUu3SWlj9kPT-LPFLMyVSjWUSPENetqN0VdxUIA5G6y7cRALP2u_4P11TgeiYb5LBAGMtj5NNi5xZxR03m0XGhpTeGYd6IHIci80CNCImOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AY6p-x5Un1lCPIhuh62PNKNOkx3hjm-SDDE0on5fe_8x8RHZwsDUB_C3ZJiqct1cI85spMl2-4aSE0v2YmOWPKGZdrDHvea1djhsHITTmFz3TloR0NHnfeNkLbHFS0irpT2ChZ6I3UViIJctR89vnkRUEK2s7TEc0_d060F4i43aVf8VRjhWDOiP9W0cOZFdvzvTV5wiqsz0zBGsrCqY412pnYx89EE2Y3AC3RTH9KTwIyv5LNj3kTcBlxghXDFITEF1yZuwMrZXWkPYI2ByMCVw_scpHpmZCbrmZVgpEKN6e6WhGXbDPsy0ZJdBkAcM6BOLAXFT9UJxNQKghsj1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFp6d1x3SOzUjZ20n1emGY7UHxYxf4XdA8HOJ0swG5qMELnsPxc8sZAQgbIyVYaz5YWDVI7mpuYUxKHqtHt8ASw7DtLHTLMoHG6weVepTbCPTr207ZD-otA5p35Rby3ZUiUbGfd5r0kNDBBXXFNdUFPoWPEW0cbC3f4_haCD9V1cnsYIPlnRbzkXSJ5-MR3E6xltreZOXB4EQ5mjNHZLSloNGgITTCihdIoHmUdUOaXiKsTfx5-HmjeSGpLoreWqp4ACa4IGxKRWBBibTBcqeDFmjQKxVGtXtPjzPKwpvL5uSYZJT1pAL6H_aN8Ugx2V-e_DAoX4ajiOm8UE75FRaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVLproieiYIWXoonAb01ErmIyPuxEdVZw9ny0Qm71q_UlaJ8HZ3ZqPNBDW1_QjOGsMdX0iK9o0teFe6m46XQiLJuF9ILGR80qQe33l4q91WBRUlyrwI7tP9rkGsCE3YCB-Kj8jVsr68kwQeBieVMSNfugQowykQOC7mo0GLjslKTcLRyivFGXLJeraYfJVR_PIqS_NvQzA53PeEIhC_I1brphh70TCah5L5AB-rQdvZpZmfxKTd-vKJ6JdmXPJzi4U5XxUsFondgjiMin-TlS63ryG9ZycYQkIq24GJIxR0mEkBtTc34GFIg2ki-vbOMmIyH2CeO93OBCC6xV0fhBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=FLWwzayK1Z76jUDtYJqt4cOtF3R-lI-isdyltrb8EaAT8fpxdXf-E8cY6tjhdVIS_evu7o7MUB7RQdWShbvCHZGrpra0oXDOytvEaaNKmeShSCrESfTJuc2Lyo7PqSYn9nL5yALKGzmIUzvGlFfKRCn4F0zxvwvCboG95WDOzpzVB2Hp3tGbrwLkEgeR8XVnnjcVf4h1R-YPpArCEeHqMKU2tq8zAZdgMf2RVL-tP6-NBu1DVffIduFUa1eiefZTPWJfEQbTbVgysFEX-slARwCvqsOChkSNG0Ii6eu4Kr5SxdZevymcCbmD8WcCrmOb6xiMUrak5hdXhrwSFsLhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=FLWwzayK1Z76jUDtYJqt4cOtF3R-lI-isdyltrb8EaAT8fpxdXf-E8cY6tjhdVIS_evu7o7MUB7RQdWShbvCHZGrpra0oXDOytvEaaNKmeShSCrESfTJuc2Lyo7PqSYn9nL5yALKGzmIUzvGlFfKRCn4F0zxvwvCboG95WDOzpzVB2Hp3tGbrwLkEgeR8XVnnjcVf4h1R-YPpArCEeHqMKU2tq8zAZdgMf2RVL-tP6-NBu1DVffIduFUa1eiefZTPWJfEQbTbVgysFEX-slARwCvqsOChkSNG0Ii6eu4Kr5SxdZevymcCbmD8WcCrmOb6xiMUrak5hdXhrwSFsLhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=BUhfER4sagDV9oB5ZBkGGDCBKBzsXjtWEc635DIIBmTSWg18xTG4mMIgNBGcz6hykn_3lTLX3jl50dKArdywEXU_PvPO02JpBZZ_GlodkbDJ0MsXr3N3hVc9M_7CLKt2GhkF3JTfL8EU-SuqwDv1TZhZmmmMkSAFePclln5QRri3yDLfU2b-X9J5oTVv6GBmWlrcVx5bTf5xaLUrqAcf5YBmrDB8VxraohBl4DjqdZH7Eq125LsmiF_A_ENtuAfUK6vTDw30oZV8kGF2g65p_Dfu9I0EVwbY3WvGmkhSV6R7iin3BDffolb6DhXnNP0Zl4vXOUYHbBqg6o_j1NWOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=BUhfER4sagDV9oB5ZBkGGDCBKBzsXjtWEc635DIIBmTSWg18xTG4mMIgNBGcz6hykn_3lTLX3jl50dKArdywEXU_PvPO02JpBZZ_GlodkbDJ0MsXr3N3hVc9M_7CLKt2GhkF3JTfL8EU-SuqwDv1TZhZmmmMkSAFePclln5QRri3yDLfU2b-X9J5oTVv6GBmWlrcVx5bTf5xaLUrqAcf5YBmrDB8VxraohBl4DjqdZH7Eq125LsmiF_A_ENtuAfUK6vTDw30oZV8kGF2g65p_Dfu9I0EVwbY3WvGmkhSV6R7iin3BDffolb6DhXnNP0Zl4vXOUYHbBqg6o_j1NWOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mP9GvAF9TZZzf5KZEY-xbprJYI4vL5faZygF2HrmmtQS42BhamslpJlwMTodApcmv1BWRBobJIQYite-CiNGKnsfBXpoAgjg1ZmQ_IXPFa-F4xhBec5tRPFwQecEFZZtHKgIS3UlS07uXDSQq53d49ibz-FdhmMYs8hX8c4snEre1Vey5QKOI98p3PXBEr-MGHEBuZbW_AFXK-wLOeKTeBI2-lvXhpKxl35rxdeziBtWUQNjj1OEOcWzLKjDsnCEOOKh_-SsnjAEJke69EqgtgUP9Dm2SGhjRKV9WznxJ7p233Bnsm48tVP7MlX6LCcW2RrurUE3xdFUzFpvB1zpKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mP9GvAF9TZZzf5KZEY-xbprJYI4vL5faZygF2HrmmtQS42BhamslpJlwMTodApcmv1BWRBobJIQYite-CiNGKnsfBXpoAgjg1ZmQ_IXPFa-F4xhBec5tRPFwQecEFZZtHKgIS3UlS07uXDSQq53d49ibz-FdhmMYs8hX8c4snEre1Vey5QKOI98p3PXBEr-MGHEBuZbW_AFXK-wLOeKTeBI2-lvXhpKxl35rxdeziBtWUQNjj1OEOcWzLKjDsnCEOOKh_-SsnjAEJke69EqgtgUP9Dm2SGhjRKV9WznxJ7p233Bnsm48tVP7MlX6LCcW2RrurUE3xdFUzFpvB1zpKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=BsZxtU1Oz305mGsOhvZmWGmvWj9fE_tSWwDffmKmNyyQqGEEd4s0rafehoTgkhV3vOV6mv-EeGc2e3bHqAXX55D1z0FGhaE1xEll1CrIs6rSNKV1DV4hfU17Pyzx21kPNDijfxv_J71rBVGV-9mYwIQsIDaZzUfPeYZuKPI8OhqrAiursue746-r37E8WjQ-Z3qNp2ZvA6Sk6FYcg-T2eout4HAFBZAY65AgTGeO3tYHRf5RJ2pkmUwE_xwhLSyk1f50MRb91eEHaa3S7Eum1B9jaO4ieKpWTpzJuEtl94_uorAzijUkZlwrSAqNbgiA738Hz0hC7IXFqlTID9jLlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=BsZxtU1Oz305mGsOhvZmWGmvWj9fE_tSWwDffmKmNyyQqGEEd4s0rafehoTgkhV3vOV6mv-EeGc2e3bHqAXX55D1z0FGhaE1xEll1CrIs6rSNKV1DV4hfU17Pyzx21kPNDijfxv_J71rBVGV-9mYwIQsIDaZzUfPeYZuKPI8OhqrAiursue746-r37E8WjQ-Z3qNp2ZvA6Sk6FYcg-T2eout4HAFBZAY65AgTGeO3tYHRf5RJ2pkmUwE_xwhLSyk1f50MRb91eEHaa3S7Eum1B9jaO4ieKpWTpzJuEtl94_uorAzijUkZlwrSAqNbgiA738Hz0hC7IXFqlTID9jLlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8NwRTXNe4NGP5vMZegg3it8aVW67aH_8dVGIJEkuX-X33YEvtfABPQ--FNyn6eS2efdHunp1I50ZQgXIzEWcHqTvNHZONgh9hzXjFkEcDDycDI8P11QSZpHRVKXIhKnAD25qCUvUJX4BlnMMqRRMtaAbwWAuJ4IfnezrPwybO2cMCCh5OhLu_ZxDvWuMLyLtJ20kGa7qE3SXKqkQYSSpqjcZvo0VVNNvCkgLH_D_pKaf08ZxcrGWHiDH5PTny1v6pdbGDdlGvHJ34NjHQJNSx7FXmB8L4ejNB69D4oGaMUbbOMHsk7XkSOHCBwkiRDgV4xecYLhwHfrvg3hR-lNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxqgZMzsEJ6aIcxHe6T8o8cW8tjMNv9Jk_43aQif6xTIqNin1Vbpwf_3O1ov-Eao7A4GL6o7_Ty82QVj3k_nzkh0-e6ZNUwPlcqlpbZgpItCNox87-a4aVbqSLJuZP9OzuP6TKfYKj1d2myZ4VGk6w2msDokXeePYOY4Gz5A6I_vzrIwlgp04Tdas9SAgQphffqkYmzn1S0vBWajkszLtmACyeSQ1sFn1q80ZFKf4xi2Hut_dNWLWgaeZ3OGL5pPxpO6qShtyT9qvyBgx-x77qw8EM45ZqqPdWVStiTVg8kIO65ttFC_2oz7dpqd6i6jNxY2limN_gbZplYCVqAEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWPktgO7of-OHjdjqw-bNdhOJ_x8wM84U_YIRpQb59UDDRnCH1M-AN9wVWLloR1P0LcfFAEzyTSwdvq2NeGaNRqnulILLBP153HzVdVWMX7prCY_ccRdRhwXqZHEJHgxGU5S1c6tbQD-6FPMVJSqfdfAfM1o5dQBAlwS68nWnzYMZ6INZPmxPIISFMCnpIvdigkoeBhHAUbr_M8_c9jkKwI5LjhKM1TNTMdShGOrSY0UQPSZE-jUiJy9HvP0YkPdJSWK45i9wMGtjiynwxFYqSvcCdNm72vGbvXzZznG7xFvpGNFJSRc2zenueJua5evypGnoCuoPriQwT3tuU9Fag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=dC6AWLUty9hjvQYx6W0FH48rg1UsT5XqrbT3_iG_oqMzvrolkIk1OBmNCppRbjLQrT9MPZtxOzVoUucdbWHrT_M-Bg6SnrYqNxNsAX8-GGeZFOtuv54YwsUCJEyNrT3fRTw7X_QUtCbHpxsNzqfbkOlh7t_oEyvaHsEYZHjdoTETr3Ik7P6pwnzzYiyorXVJmRRn4I0RyQImgRrYmmEYypQsl-a0gwvo2oZneLopnk_A7lx1N2v25ICZHWasM2PJHN2BTiseMBRdpnOY-2P_QQxkI6bjckKOG9-nxAdhVETqZ2zYf05YukPkc3OujjXbf3E-rX9OjVsA0j_dqrKg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=dC6AWLUty9hjvQYx6W0FH48rg1UsT5XqrbT3_iG_oqMzvrolkIk1OBmNCppRbjLQrT9MPZtxOzVoUucdbWHrT_M-Bg6SnrYqNxNsAX8-GGeZFOtuv54YwsUCJEyNrT3fRTw7X_QUtCbHpxsNzqfbkOlh7t_oEyvaHsEYZHjdoTETr3Ik7P6pwnzzYiyorXVJmRRn4I0RyQImgRrYmmEYypQsl-a0gwvo2oZneLopnk_A7lx1N2v25ICZHWasM2PJHN2BTiseMBRdpnOY-2P_QQxkI6bjckKOG9-nxAdhVETqZ2zYf05YukPkc3OujjXbf3E-rX9OjVsA0j_dqrKg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHI4ZcArym9p58KXPpa4smtgLky48ZgOBc5OiPnIfePKbYmblsXecvkSBN-R6K2owc85FxW_Z3bze7fQeX3C8gTQxvUQ8FPORw1F1h-TULCAJKIOtelCOXcu9PyLoCUk8Zt80AHbUBE7AvYS4SlGaStWvwYt5jen51lS-lM9qFg4kL1Hc0BzM-l67UbQZKpMwVA-azPf2k5QB6AOq6mFMddynU-r8iQ7ifuTaTGsI5VU2Hvmzz1-RDIn_7Zrf1yAsRRe4_xkGAjjcueOa1iRVrCFbPNEGprWaHKIr8skVfBnVdyg3815pW3bxKTES_kuY1E5zo6sZvN5brC6OvckXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=PwM2m-FcT-8vubKSGQlwAbNdPLgEEt2paFE2D7eyYMsFbYr0vDV5eWypfHkMT4SGpyuxrGgpTgjT9HEXhds7T-byrVsrn-2WQCVYmARdYcdSePM_w7tN60sD4ylZ51VO33VG5PCWch8kARu8pT_eLA8ZuXPEhlWegBwDlQ4g_XlravvsaRCJiFLe-ZTC2yAvbd6b_d0HUkcZR3WinDqUzkAPuQvQ6mFiRf6O9yEBIrWV7hS8RxKo9Rxp2XyYz7F6yHUNF29fxE91agNvT5tMo4gxUYRhRJzkV3GqELkux-4hfzgH1M0wK7e8bBKev4wi0fcCfTMSszWEjjkaAKlXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=PwM2m-FcT-8vubKSGQlwAbNdPLgEEt2paFE2D7eyYMsFbYr0vDV5eWypfHkMT4SGpyuxrGgpTgjT9HEXhds7T-byrVsrn-2WQCVYmARdYcdSePM_w7tN60sD4ylZ51VO33VG5PCWch8kARu8pT_eLA8ZuXPEhlWegBwDlQ4g_XlravvsaRCJiFLe-ZTC2yAvbd6b_d0HUkcZR3WinDqUzkAPuQvQ6mFiRf6O9yEBIrWV7hS8RxKo9Rxp2XyYz7F6yHUNF29fxE91agNvT5tMo4gxUYRhRJzkV3GqELkux-4hfzgH1M0wK7e8bBKev4wi0fcCfTMSszWEjjkaAKlXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=duKlOJfq4uEOGuBy_CxtOEprUJ75pcCCqR6n3rXav5k1tr09S1tPWV2i5qHQX6a1RFwKZz6zLmAQ8DmMS5jypNYUooup_lvQKTkceW0NQl5XjcpN2SlxG9IQqM6TP1JbawFONASKefFgYx0rnAvZQkB2sqkN0lAzZA0P_QtX4NkbAUPfBPF1M7XHTklxAoqlIvq0Qq0DcQIWb0FZfshQG2L3ySbdpRUPHBITqXsl6X1cxEpbvP_2sDRS9Ivmvr6DN0wxvBTIV7qfJpI5esKJ5aELZPedzLTeEAwZynMvJdDS5ieq1RHbsWScWAvzrdz9OqFLrUe6JENO88pV3t0v7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=duKlOJfq4uEOGuBy_CxtOEprUJ75pcCCqR6n3rXav5k1tr09S1tPWV2i5qHQX6a1RFwKZz6zLmAQ8DmMS5jypNYUooup_lvQKTkceW0NQl5XjcpN2SlxG9IQqM6TP1JbawFONASKefFgYx0rnAvZQkB2sqkN0lAzZA0P_QtX4NkbAUPfBPF1M7XHTklxAoqlIvq0Qq0DcQIWb0FZfshQG2L3ySbdpRUPHBITqXsl6X1cxEpbvP_2sDRS9Ivmvr6DN0wxvBTIV7qfJpI5esKJ5aELZPedzLTeEAwZynMvJdDS5ieq1RHbsWScWAvzrdz9OqFLrUe6JENO88pV3t0v7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=uRZXm9GL_9CKVoyxEvfNfj0bwjap8VcK4ioCWx2Ox1j-R8DxURcgPWbLRZ6pN3wTx_PKPdEHQYPxe1ZAwEJRVMcTVoeYTp5RdLEZxmgxVVws4qZRW4jXbv0I1zoC4TzUBUy_CTPPhVysDQswy-5srBUW08u-n-Xbb-9pTn740dUZDpfNlSbvV-uFsk2ynrTNqV9UoVRF4wrtgpe7edv2ekz5o40Czuw9hUKhjiyyz-tDlDJuwtkYy6lQwTV2sVExwFz_SKPoKHG1qymBf7UcWPGwrj6yA9mQ81wObHT1A3162grJ3uRyugRdG23ejCYlzkTEQAGiSnmjmsappVhVFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=uRZXm9GL_9CKVoyxEvfNfj0bwjap8VcK4ioCWx2Ox1j-R8DxURcgPWbLRZ6pN3wTx_PKPdEHQYPxe1ZAwEJRVMcTVoeYTp5RdLEZxmgxVVws4qZRW4jXbv0I1zoC4TzUBUy_CTPPhVysDQswy-5srBUW08u-n-Xbb-9pTn740dUZDpfNlSbvV-uFsk2ynrTNqV9UoVRF4wrtgpe7edv2ekz5o40Czuw9hUKhjiyyz-tDlDJuwtkYy6lQwTV2sVExwFz_SKPoKHG1qymBf7UcWPGwrj6yA9mQ81wObHT1A3162grJ3uRyugRdG23ejCYlzkTEQAGiSnmjmsappVhVFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMbciYQfVGXc1QfnH5PoMd68q2LUJADYyp7tKjGF5QTtym5qMYnl10Z1bwQt-jJ7EQJlxwPKj6iTNKglWbhuJUlSubkwLp4esqC7pD9ZWWYE5oMVuy0JyQ7qqBexsDwL-hz12iJt7-DcJKo-qmLXPXp8oFPfkqIKJvSsRctEI0UTtxKT454vh4KsMm7E1ujs81uP4zLOj4DzRuF8ixSgnZavxDDDotA9wUehlv0ib7m_wd3qbwBy9HbNhLeXraflJBHhbyBfpXsQycISUnFJ99Ara0Mm36rgdcpyHed94F3aKS2mqBTHVB9-CK7rHQZRM27UwEJTyoxP5-3pbttmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=hn10dg-drR2TLavN1y7cet-mBmEcqq95Bl565FqkBfWKtBFe-8_4Qbkpg5wkGYY4UcvXfANr9Eq56D00HxeWRUqv7xmfG-xLvC-ow_ypWIbl2gjQkfUwdZN6oZLA_O1ePB0ML-SV9_vKGBv3662iA9iHxJLqphAK0yiA-jKwuLRgXTuvZPzF8OJuAvr4gmnwfnF6c169KNYDtORIRZkYNkzQdvgcQKMwh3L5lMNpS3qgWrisiPCZWpuySfDb8C0x1RzTuE2wFe4BIPgtcaaEToIpN9TNVUnpjG_JnOyKvXQ5bfgRUbBs7zEGbvoFSPWmB6ffgQFAuCAQlYxy2XE_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=hn10dg-drR2TLavN1y7cet-mBmEcqq95Bl565FqkBfWKtBFe-8_4Qbkpg5wkGYY4UcvXfANr9Eq56D00HxeWRUqv7xmfG-xLvC-ow_ypWIbl2gjQkfUwdZN6oZLA_O1ePB0ML-SV9_vKGBv3662iA9iHxJLqphAK0yiA-jKwuLRgXTuvZPzF8OJuAvr4gmnwfnF6c169KNYDtORIRZkYNkzQdvgcQKMwh3L5lMNpS3qgWrisiPCZWpuySfDb8C0x1RzTuE2wFe4BIPgtcaaEToIpN9TNVUnpjG_JnOyKvXQ5bfgRUbBs7zEGbvoFSPWmB6ffgQFAuCAQlYxy2XE_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNST64dLMTSfhagjHYJ_2A6gJwPmPtQSiSIA9Q9iMNXitvU8mKeYahxrHaDOu4nxkjgitiYE8FXp64JuAIZaq1LUNpO1J4UG8FnSY5IIMDtdASWN6MC7HFRxWvGE_RSmqDBzqApmQdd3O1qbeYEDllaBo3TWZ5pWrhSHxMW37WsXDHA99ROX3Ze9RmWmW9UHqJjUStAJhxZmeql_S8rAPKznxYa2GtCQ2WdPP9z5cHrIEk6mTK43uEw-5YzqFzv7NBreO8cnbAb11jkbxMDrT9MQvwx3oEM3hZYswtvJRQ78K911JSEr5JxN5keN3QnbVIht6kGqx_0JqO9vUY9bfgwsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNST64dLMTSfhagjHYJ_2A6gJwPmPtQSiSIA9Q9iMNXitvU8mKeYahxrHaDOu4nxkjgitiYE8FXp64JuAIZaq1LUNpO1J4UG8FnSY5IIMDtdASWN6MC7HFRxWvGE_RSmqDBzqApmQdd3O1qbeYEDllaBo3TWZ5pWrhSHxMW37WsXDHA99ROX3Ze9RmWmW9UHqJjUStAJhxZmeql_S8rAPKznxYa2GtCQ2WdPP9z5cHrIEk6mTK43uEw-5YzqFzv7NBreO8cnbAb11jkbxMDrT9MQvwx3oEM3hZYswtvJRQ78K911JSEr5JxN5keN3QnbVIht6kGqx_0JqO9vUY9bfgwsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg2yatvJBF2jt_W5TSfs3G5HH0V0P0erCQgn4lJ_3KuOP0cqMg6V2bNZu8UPLxAndiGNs3ysV68JQmzBZVnLjAwZjqZB5CgaqV4BkU2MKD2aOqH-HaxxKJhq0I5BjdDFs98zRQWh06G7InZ3BI_o5HJCcfp-O4YJd820Ad1MOx5h46cGQLHgTIxjvDv17l7phUi-bXv_HP4KL-quKqetc-_SQ5FwzUAj4JXYybaqUScfP7AJEgYT7Wdz7mZY5QYhNOpN13U-kcGf9ylR-4kL8knwpN1DTZmF30UaU45Q7l-H8YYdrgBk9dqc-dO2LShDpX2muw8n60Tedetf_cxRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=cdubEbA2euc9Pmm3cISIZtdoveZ01PnZoCzrhvOVE3fHhEuEVoahOu0bjBs88pK91GpSZelaA7Wk2duE_ZYBXHHrRBdBh4bsTfQdaCxEehinv0vJMbUXs-JFTmLKR0mPyHwbOBDgNOel0RjmtG-UXxqZNX7cZv0pQ9Bvo5_SI_DYDOeHuUhrZ1tQ9tBl5Ob6EcAyWjKHapSBvhR64tZ4OO3sAXcufuLd_52aV76pD5MWisbSUcSGKAYmszG9Ed3dAJlbnRk2eAUTvIpd33Ff-eW-ACadAv1f7E2P6244H2dX1lpX4CLo_HI2e8oDrhcrBBc3ofzyho-4OxJRXUB6UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=cdubEbA2euc9Pmm3cISIZtdoveZ01PnZoCzrhvOVE3fHhEuEVoahOu0bjBs88pK91GpSZelaA7Wk2duE_ZYBXHHrRBdBh4bsTfQdaCxEehinv0vJMbUXs-JFTmLKR0mPyHwbOBDgNOel0RjmtG-UXxqZNX7cZv0pQ9Bvo5_SI_DYDOeHuUhrZ1tQ9tBl5Ob6EcAyWjKHapSBvhR64tZ4OO3sAXcufuLd_52aV76pD5MWisbSUcSGKAYmszG9Ed3dAJlbnRk2eAUTvIpd33Ff-eW-ACadAv1f7E2P6244H2dX1lpX4CLo_HI2e8oDrhcrBBc3ofzyho-4OxJRXUB6UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdFysowrgnnDwdikE58Q31xRS2z2KdTbHSKWQ3DOxHmXJJCS-Po2ft59C2kmR4s4AFXmr9jY6Y2A-HnvtFJ0plB95Abj6feLpuXuqp5OW0lBxnZ8l_EkO1Z7Bvgf5UpQoxS8J5m17YjZBksTg5BrVD0x23d8-k4RbYoa27-Sq_6OkLplP_7X8zJJYf5Upo7HV_chHVHLs4sDaebNatOPogVy9BgZwgj3lB46uYhPM8LqDwOXYEF9rAxvfQN-ibtWjcYXsOHXcaU9_8j_ZsxlSO47rfS2wJCKEj4sb7X5nNvD3a-ZkCJsPsdJb-h43wxXmdQolqWMMfhBqOSte8UCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=tVQ79vEMZd6hcJIM5l6H3j-CPfYgk5u8X3-zoLZ25tLwJ_HNP5tElvSEYZ20S9kAE-vTzGbjNUGI0NHi9_Gp6Yi76t_OeqL8rBw4vynd3Mw4ByyiAbOJCGMlBV80TY9c_hwHBBva2JLS7Tl_zaVIBY9MAMVvuCsJBXf2t1j3cOZ529hsQRWry4XfFVoPOf1XvugWIsCQp6yO50ml-5AdUuWDAP8L9IyvgLOKuidvRjwSod7aKcw9H35QG1NkrGrX68lc0Tfo3hr42AnmJEDhD6SLt1Mu4KQF5vtK66phlAlWqn8rVT6WEz4A1maSmpURvnqaMkEULIgZs-tSOE6XIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=tVQ79vEMZd6hcJIM5l6H3j-CPfYgk5u8X3-zoLZ25tLwJ_HNP5tElvSEYZ20S9kAE-vTzGbjNUGI0NHi9_Gp6Yi76t_OeqL8rBw4vynd3Mw4ByyiAbOJCGMlBV80TY9c_hwHBBva2JLS7Tl_zaVIBY9MAMVvuCsJBXf2t1j3cOZ529hsQRWry4XfFVoPOf1XvugWIsCQp6yO50ml-5AdUuWDAP8L9IyvgLOKuidvRjwSod7aKcw9H35QG1NkrGrX68lc0Tfo3hr42AnmJEDhD6SLt1Mu4KQF5vtK66phlAlWqn8rVT6WEz4A1maSmpURvnqaMkEULIgZs-tSOE6XIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=cFfC0kF8HluuuBESSTHEX-wlj8V1ghMkYt85e9iVc4YGhRUnAjMpM4w2bZlRZnMMmFG9t3bugnbKtQuHHO9yeDvOL7zUW9NuqSQLMQxPJWZqMC7zmFPBwzErd3MLFK-6kARFqeNkLPZWIgBsGoRg5AdGtbmAt4_5zawM3581-7lEuj9i8aZlLIK6Q3UmpSPciy-iOYDxqy7lBVqGhhdcPwjzUHS2qGT0bs6B0cTbzM-5H_5jc5xRO19mpaW0bUB1UBCehbJDxrLm6dz4ie6Y7HeGLP4xn0uKYEghqko1k12gZ2XfbcJBDtKkc_EoLhhkzhc746WuBVxGD1NxBDZ2EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=cFfC0kF8HluuuBESSTHEX-wlj8V1ghMkYt85e9iVc4YGhRUnAjMpM4w2bZlRZnMMmFG9t3bugnbKtQuHHO9yeDvOL7zUW9NuqSQLMQxPJWZqMC7zmFPBwzErd3MLFK-6kARFqeNkLPZWIgBsGoRg5AdGtbmAt4_5zawM3581-7lEuj9i8aZlLIK6Q3UmpSPciy-iOYDxqy7lBVqGhhdcPwjzUHS2qGT0bs6B0cTbzM-5H_5jc5xRO19mpaW0bUB1UBCehbJDxrLm6dz4ie6Y7HeGLP4xn0uKYEghqko1k12gZ2XfbcJBDtKkc_EoLhhkzhc746WuBVxGD1NxBDZ2EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=qDMK90a4gKHa11myuSgOTqj3HMcoYej4I6l1iiZIPv-aCNkAy8Uv0aksuEDlo-HxKZTF1tO4s9S8U7maMGRLi-_RqXZb1gkigf9eqR8CBwBAkO9N8HS-5Wyqfm9P4DQzGRIftTRybR5nuklTdgrznq3HzFe2rlpH2AgniQzDpwaSECR0aVo3my7wtRbd6BclcWQKEmm0FFFl_ucdzcV1u7YuvrOTWSj_xjKPcgL59QtPaQZ3TVpiJp5I_EdAyPlrdhXHroZswCaIxe6LfC4qMIv7xCH-jfbFBTRfvOeIE8CeDEs5aS1JLp9rU-M5hDwOLSYPupfODRrbxEoMriXY2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=qDMK90a4gKHa11myuSgOTqj3HMcoYej4I6l1iiZIPv-aCNkAy8Uv0aksuEDlo-HxKZTF1tO4s9S8U7maMGRLi-_RqXZb1gkigf9eqR8CBwBAkO9N8HS-5Wyqfm9P4DQzGRIftTRybR5nuklTdgrznq3HzFe2rlpH2AgniQzDpwaSECR0aVo3my7wtRbd6BclcWQKEmm0FFFl_ucdzcV1u7YuvrOTWSj_xjKPcgL59QtPaQZ3TVpiJp5I_EdAyPlrdhXHroZswCaIxe6LfC4qMIv7xCH-jfbFBTRfvOeIE8CeDEs5aS1JLp9rU-M5hDwOLSYPupfODRrbxEoMriXY2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=GaPpYYkr4__RXW-Z64-yke_CP5RFiShi6liXbMgi79gFhXHFXpl8I41LtJ9hd9QzUnu01dXTJC_AzDefP5z8R_LCaawG9wK4MiM1cluW42Vevgt7MKRitRWknsq2jbAq8eTOZEQN8j0aHCMSMHk_OetcduF105sQeZ0N3e6Dar1OgUxcDRX6opD0qiixMM-C_yuWbNnzKdmPANNqf9mM0AgLE7e_J_BQS__S_f2TC2HPTfmaYS73Ngo9oRNQEPwr3k5Irmjtzd2_FUfv6_WQQWm4ZtCKSiK7V4IftywAvYcXdqaxoIP6-s9QHH7ORkJLzR50sV_UQc8jb5ikmPDYXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=GaPpYYkr4__RXW-Z64-yke_CP5RFiShi6liXbMgi79gFhXHFXpl8I41LtJ9hd9QzUnu01dXTJC_AzDefP5z8R_LCaawG9wK4MiM1cluW42Vevgt7MKRitRWknsq2jbAq8eTOZEQN8j0aHCMSMHk_OetcduF105sQeZ0N3e6Dar1OgUxcDRX6opD0qiixMM-C_yuWbNnzKdmPANNqf9mM0AgLE7e_J_BQS__S_f2TC2HPTfmaYS73Ngo9oRNQEPwr3k5Irmjtzd2_FUfv6_WQQWm4ZtCKSiK7V4IftywAvYcXdqaxoIP6-s9QHH7ORkJLzR50sV_UQc8jb5ikmPDYXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=v9Ctg2hR9Ma80JDjIYON7hirp2o7-Y9gidn35yANsfyE1NbWeNwk7BgEFIM0nHUpNb4tytVNGjPtZeKvhFZeh6r3qhsL66h8tIeq8WhsQsZWpfZNxbokdOdVmgtY-dkwNLBndVShVxhHKTCSl7K7c66x_G0hR4H56bepV6mQK-5gvtgUSa4HyEe0mwk660SxKtcFDyWqgUA8wzZSnvu1G-Ycr8KAFWaMODxnZOrMb7qZR8bfpUpxCIvlvV4xhXt6TCx3NvHaHmqz2lZ5xR5ZvNdnM6GyuyHzRhLiV3ouYf0XVHOoaAEXKkjiQ17RhDhYyZ3FHvvdjkWB7QT9I6mkeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=v9Ctg2hR9Ma80JDjIYON7hirp2o7-Y9gidn35yANsfyE1NbWeNwk7BgEFIM0nHUpNb4tytVNGjPtZeKvhFZeh6r3qhsL66h8tIeq8WhsQsZWpfZNxbokdOdVmgtY-dkwNLBndVShVxhHKTCSl7K7c66x_G0hR4H56bepV6mQK-5gvtgUSa4HyEe0mwk660SxKtcFDyWqgUA8wzZSnvu1G-Ycr8KAFWaMODxnZOrMb7qZR8bfpUpxCIvlvV4xhXt6TCx3NvHaHmqz2lZ5xR5ZvNdnM6GyuyHzRhLiV3ouYf0XVHOoaAEXKkjiQ17RhDhYyZ3FHvvdjkWB7QT9I6mkeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=XqHcEnzZg84mECykvCiqgGSNIIj0wszmcIkUBGLcDDn9L-0KOYIKiQmbrc7ECBycju9fCq_SjmvmniXSA6Tn6hKFmNRBRWxwpL1Ql9eDbFk1SACji2J7mx5dgRliCPYrWsoU-GiH1lFTzy4kyfUsIz6qjenBdkZLdXwTX8FU0hMN-nk_RzpxVfsyo50DkuH7siWyYke2IbX6Xjqw51wdmoFczNHfhgCbsTNkIe9k6eu64AOCNhsOXLlikpU3lvxc-1PXUu4iL2gaPv4tVB3y5CV1iI4FJbTdYdiRnanE9zQayPra1jBuGWXzkfUKMISQEZ1d_YfcAdVoCe9nIrfJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=XqHcEnzZg84mECykvCiqgGSNIIj0wszmcIkUBGLcDDn9L-0KOYIKiQmbrc7ECBycju9fCq_SjmvmniXSA6Tn6hKFmNRBRWxwpL1Ql9eDbFk1SACji2J7mx5dgRliCPYrWsoU-GiH1lFTzy4kyfUsIz6qjenBdkZLdXwTX8FU0hMN-nk_RzpxVfsyo50DkuH7siWyYke2IbX6Xjqw51wdmoFczNHfhgCbsTNkIe9k6eu64AOCNhsOXLlikpU3lvxc-1PXUu4iL2gaPv4tVB3y5CV1iI4FJbTdYdiRnanE9zQayPra1jBuGWXzkfUKMISQEZ1d_YfcAdVoCe9nIrfJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=hny49PHZj8HtSxRu7rXD7XVdibZ6sIW38p-HlE9uObPWFgKaBtvsoa5OTyeInNFEtE26Y99Rm3kR8NcY8oYiaKLw5pg4bHbzyCEdgdtf63jyz_euBYV6HFu4AB48GMEz_p1gO1dqz_b1VGzpVLNiAE8-NhHmKQiub_a11k-A4j4R6dHuRsFKST6D7Jveq-ur6EDlyv_YEFgR08Hkcmx-yglVnRSXoFambXinHyrgEYVHo3VS1eIoMLNOjUSE2hcTV_h-1hehGdtj5untijUF3nnW-YgzWMwc61QM6nVH6tGEWWlzpBhNmPtq3GL7L1TwY-Ze8ezhALaCK6fc0oJ-Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=hny49PHZj8HtSxRu7rXD7XVdibZ6sIW38p-HlE9uObPWFgKaBtvsoa5OTyeInNFEtE26Y99Rm3kR8NcY8oYiaKLw5pg4bHbzyCEdgdtf63jyz_euBYV6HFu4AB48GMEz_p1gO1dqz_b1VGzpVLNiAE8-NhHmKQiub_a11k-A4j4R6dHuRsFKST6D7Jveq-ur6EDlyv_YEFgR08Hkcmx-yglVnRSXoFambXinHyrgEYVHo3VS1eIoMLNOjUSE2hcTV_h-1hehGdtj5untijUF3nnW-YgzWMwc61QM6nVH6tGEWWlzpBhNmPtq3GL7L1TwY-Ze8ezhALaCK6fc0oJ-Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHcQjoFf9ZHfELB3YvDH6EER0STLfA_QrCKFvuOHdJdJEikrZZYwXA8I4jD9z-PbsL0ID82JUos-TXqSdlm0vpgeXAzYIzIEcjQTZd5YTFV-f7HXn5dP9RmsGSm0x1WeWs0Nr27_AlSqTBem-DPw3KpLLI9wGCceZTP2Xt0hPN8wrvqKDQFtW8dcB77jLHaxmDjDjY_NmJJYaV7Z6tAsEjiamYwhXAAx_lublF2GPGnfzzL8y-jUScGYJpCpUzz_wqORW0JEZe2FqlRZMiED_PjmKUj2JkAX6e1GUD7pqq__dKInkCgYMUuDw9ngFGhWiaF525wAuOaFY8CBxNvrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDswzC-D1fP-uMdmGSISnNo1WEwNKgY323M14C0EpEdCL1Aiccynm5r3bb5lpiwQeUT07gE8wl8uI9FjMgmaRbTi6e1oUYPId2vH99-E6soWz8iY9iPldvZf0_ST4H-8nB8FT8GOUMfH-_TNarrm9lIUHxdjywkRbySTVbSfwLCebHv9ijglADwcCoVB-2oVQP8MC8bpV4ikBZO-pUZOmFVux-3JHwgBSPkgeCkrPjblHPLQTzGfey8CavDFvMw_PPnnKGVh1Fl2AQihquS7XrsGKBYCkDz547_LMEQDdDN90Vk6dUMH95UQQe5lULkYd6W1q1hiPvElYbJnWLB7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbE2WLHPrCBsx9OCFkTV7bH34c3dbR5bskU61cus3OrRWojlePFonVEaiZCu7O0eiWSLJimoxs11OCqWYSRP0P0xV3LJ8-sVM9zIxOlkhYSxSQ1TufC8HrC4NPrG3G4r_qhnkrq1T9DiK0HzQgoEm9OSSH7bl5mXkwMGMLKLIvnYvjinDjZHGVwfN69TVxqiZ48I3AAJDRgfOck_FW7ApAJHEGPXCLVqRon3pfWpGjpE7uGcj41QOedkqAp3Dz-XCvJDEpDsDKtYI8cruJkpk5rGbTEY4LfqJlsg59upHNI0TreUI7vBF5F8l8In3SixDecdz0L3kqjHfVpn_CosOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=rZbXQ0nowo66JFrVtap510KH2xDIypPiW2vPjozh6PGkZdo5bO3-dNH3Mcv_P8mq719yUjaYxDWRNMuRxyeb-bKm_UBCLCW144reLMBV2Zs75VFt_SkPGQQxSTDTQgrPmB-rfPbIDOaEW08VnanA8Si2UP3REXLbG67TMAHPIkbh87D2hfljWn_Ix69PzKNNwM972SudmyvHgtbOf8QWFvFUPrc8KIet9rPUxMwvV3tvrlnj79jb0iodPmlDvFQjgCOzcb190qI8_KYCSSBm_jxM-bm8EmapCbVl09ZLeq4xO32z-qk3XJhyo16xqNI2c312o0G9Df1ljZ-Y803XjVEr_WKb_HWA-0mhZiZo8T2n6aclu9GqYmqMu5u4gM0bR67ryuHm2PNjaFofMc0zIr8Khwx2zpChKacJo6pOyns7rYPlgVJW-Ssv4TLwFillYqZXHmsXcZFwF0WI1b7zBgyLGrMJoUf2hGrUpzrgvn2R68nqXr81nM0MpG1nUdE-ITW9nZzuHrCEoEAusRc6GXwKoibnhm2EB-CWCjCfIxC3wWfvOvYNWq06wqZyR7ePZ7ifmYg7kH02CRo7fvFhFWuebM8T711wABU_GAuYeDhuAvQBjIrEORcayipc9CGC6mY6lkFjRvpUM4GfQpwZZL3bu1NDfqYNWM_z6xLoLyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=rZbXQ0nowo66JFrVtap510KH2xDIypPiW2vPjozh6PGkZdo5bO3-dNH3Mcv_P8mq719yUjaYxDWRNMuRxyeb-bKm_UBCLCW144reLMBV2Zs75VFt_SkPGQQxSTDTQgrPmB-rfPbIDOaEW08VnanA8Si2UP3REXLbG67TMAHPIkbh87D2hfljWn_Ix69PzKNNwM972SudmyvHgtbOf8QWFvFUPrc8KIet9rPUxMwvV3tvrlnj79jb0iodPmlDvFQjgCOzcb190qI8_KYCSSBm_jxM-bm8EmapCbVl09ZLeq4xO32z-qk3XJhyo16xqNI2c312o0G9Df1ljZ-Y803XjVEr_WKb_HWA-0mhZiZo8T2n6aclu9GqYmqMu5u4gM0bR67ryuHm2PNjaFofMc0zIr8Khwx2zpChKacJo6pOyns7rYPlgVJW-Ssv4TLwFillYqZXHmsXcZFwF0WI1b7zBgyLGrMJoUf2hGrUpzrgvn2R68nqXr81nM0MpG1nUdE-ITW9nZzuHrCEoEAusRc6GXwKoibnhm2EB-CWCjCfIxC3wWfvOvYNWq06wqZyR7ePZ7ifmYg7kH02CRo7fvFhFWuebM8T711wABU_GAuYeDhuAvQBjIrEORcayipc9CGC6mY6lkFjRvpUM4GfQpwZZL3bu1NDfqYNWM_z6xLoLyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkUFlLvlIFY4tGHdkaeRoON3w6ZvLUKnbulE9h8gr73vutnp_UwofU6_ASFhj-oKvMThhWdmeSccqipa2PYM7egBOucYHzNENP1B-z-uB8Z3Sh6qIUrhhdubV8unMHeapp8wk4uQUHgHFp_KzdEOB-fkruShg6f2NvaC68t6vDGuDNq7oAhECInJd_dl5UACYHhnPIABWgIzYoXQdAaPElA4-TnQH4OdNzRKZtbjDLlJ39j0Aq5ayCHhqFzycehiDBSF94fhKz2W38BTAncc8DbDi2jOTZrc7_o0rmETy5ZyRQvECFuPUItmwv-Xe4tV8cxmaOUhlI-E718SZV7CUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=B5y7cMj2dLZP-CFls8oJKYy9brlX7Ye7q5q3LIA--VJBmHehM6UBXbkITWy7EH95TwoHHyIk607-k02AQMpYTQOzS_6dWMLc8DxR8cvm0RerKjlxd2FW3HyUiTPEN9BC6_pkjNSD5wBUO7wbfm_-R-Z9PHYUy5QPm8b48PlQGic0CNlXbK14-kw1W-ZndCBYbj2IOOcJq3i_BUX-stSK3vkTAT5xm4c4xazfX8I_mPpPLnt8qcfixupypyH2arMktHaLjLPSaKo3IJNIo_oJq7CMFVOJriGgqM2rFZKVV-azqbshSKiEGP4P9Wx44tZKxAywdD9OLnkOpqrU9UgMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=B5y7cMj2dLZP-CFls8oJKYy9brlX7Ye7q5q3LIA--VJBmHehM6UBXbkITWy7EH95TwoHHyIk607-k02AQMpYTQOzS_6dWMLc8DxR8cvm0RerKjlxd2FW3HyUiTPEN9BC6_pkjNSD5wBUO7wbfm_-R-Z9PHYUy5QPm8b48PlQGic0CNlXbK14-kw1W-ZndCBYbj2IOOcJq3i_BUX-stSK3vkTAT5xm4c4xazfX8I_mPpPLnt8qcfixupypyH2arMktHaLjLPSaKo3IJNIo_oJq7CMFVOJriGgqM2rFZKVV-azqbshSKiEGP4P9Wx44tZKxAywdD9OLnkOpqrU9UgMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=cUOnhmwjA8e7SiLxHw2ez42-Cc-ezpF4s3Iz1GYVhcuOsJ5-3sHMNO_9x0JLhbVDCBcQY8bY28xHaFi-scT3KG6HdDTioIQJcPXT5SupE7ja3kiqEguSBhh7JDTzlvX4fL6d_ycECouCrjcb56TGIDPfLwY_1No7I3ouXAEtKrj2FOFaEiYu1mogqzWmpR9CpoXuv_2LZK56fza78CDoAabuH4B7xSOF6vbZD6pJf6JaqmwMDhEZBlGSv4cUPtfyIgJ_0McKpRWhNo4etarcOZlsPWrlf4wYMpr6ZNhbeQgMEsxY-cfeEKotAcvx0_270X4PPIFeXfPcGcffRJuvQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=cUOnhmwjA8e7SiLxHw2ez42-Cc-ezpF4s3Iz1GYVhcuOsJ5-3sHMNO_9x0JLhbVDCBcQY8bY28xHaFi-scT3KG6HdDTioIQJcPXT5SupE7ja3kiqEguSBhh7JDTzlvX4fL6d_ycECouCrjcb56TGIDPfLwY_1No7I3ouXAEtKrj2FOFaEiYu1mogqzWmpR9CpoXuv_2LZK56fza78CDoAabuH4B7xSOF6vbZD6pJf6JaqmwMDhEZBlGSv4cUPtfyIgJ_0McKpRWhNo4etarcOZlsPWrlf4wYMpr6ZNhbeQgMEsxY-cfeEKotAcvx0_270X4PPIFeXfPcGcffRJuvQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=tKOPIW30_Djlr8iAoV-Effx60-oyXLjxoeFFnQKMCZkJjGDDAcl9y31NkLaJh5tY2XbONZfJbFeRaDtSqMvDhZ-UNj7Bwu4eIi2mYP2xKckxX8JGhVG9IizQ1a-yrbf3WWZ5ScvGIFBHkMYXmxIjCb4GxzgzdRue0dnIIfX95cqomEIKOnVnftBKzpo840VA1wyyJ8xfa1FWkxMyAYUnf7EMFjooBz9PhLTp2PyV_zSF6h_v35qFui3O5qtQZRWhKVXBkbD7R5lgWR_zluX81MOeyd4hPaJtSuEbS_kmOLJ5FNta4j1wBMACVJnH7JgS4Ot2mA1XluD0qQ8ciIfhig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=tKOPIW30_Djlr8iAoV-Effx60-oyXLjxoeFFnQKMCZkJjGDDAcl9y31NkLaJh5tY2XbONZfJbFeRaDtSqMvDhZ-UNj7Bwu4eIi2mYP2xKckxX8JGhVG9IizQ1a-yrbf3WWZ5ScvGIFBHkMYXmxIjCb4GxzgzdRue0dnIIfX95cqomEIKOnVnftBKzpo840VA1wyyJ8xfa1FWkxMyAYUnf7EMFjooBz9PhLTp2PyV_zSF6h_v35qFui3O5qtQZRWhKVXBkbD7R5lgWR_zluX81MOeyd4hPaJtSuEbS_kmOLJ5FNta4j1wBMACVJnH7JgS4Ot2mA1XluD0qQ8ciIfhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=Rf27jNu-AFC0rNB8fvmMzoU3SxJsYalSaA0_2iQogZftsg8p_xV_4Il8SllL4rti9bu4ZiRgfsuddYPUUUG0c8emhyJ0zxR147VmPGQFOkh4P3EGP79M1U1G_UDsDMW5pbICE4u_-q8QVWoyFOvB3n8l0_RAK_kMOlnlvjVlxB5ES61lV_Dt5DAd4sVY3FirHib_ThWOleSeBWxDfiYeDded5c1E9FTumhqJjYx6kUd3WyTzOy97j61LGFqdAoWJkUOpjQqOS7imc678bzfWirEUxJH3OvBsqttbGsFX4plfM78z7WgFD0_AeEHmFqJP9vWkzIir-Mm9YJPraU_P44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=Rf27jNu-AFC0rNB8fvmMzoU3SxJsYalSaA0_2iQogZftsg8p_xV_4Il8SllL4rti9bu4ZiRgfsuddYPUUUG0c8emhyJ0zxR147VmPGQFOkh4P3EGP79M1U1G_UDsDMW5pbICE4u_-q8QVWoyFOvB3n8l0_RAK_kMOlnlvjVlxB5ES61lV_Dt5DAd4sVY3FirHib_ThWOleSeBWxDfiYeDded5c1E9FTumhqJjYx6kUd3WyTzOy97j61LGFqdAoWJkUOpjQqOS7imc678bzfWirEUxJH3OvBsqttbGsFX4plfM78z7WgFD0_AeEHmFqJP9vWkzIir-Mm9YJPraU_P44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdOjw0mQtO_A7f1U2EW0N6fZojKKIddq5k5Q_ift1V7VHHXVYa3jcc7lUDokKottMA81x88FRq7-TjdJnLfbf610g6m1Un77D_DJsbSOIgAZiQlmHrvw7N5nd0o7iB8mNA-LgTwiMbVDYPE_2EMIdPXjALyWYvP1ci0868AMVAljjGT8yYHaqYp41PgU4UNtkCyq4pEM7d1OwrqMuc3RB6Kgqc9tDafgl3LpAwMKqafozyL4eeT-xo31R6DHiIKlNf3k-xHi0z3-NmFLgdiv3CF3X3FTSevlwuE5fYz0mbC7QQgdGd4lqOpY142IMq-XB7EOKoMjGxUTjcbWt3I_HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cnNfvyIYct3amd8EagTRYMuXL8SpH5yfqeXqCv6hcbWZjkIAyxzuoUXsb19tmTJEDsYP7c0nFLm2SX1bAF4R5D0a2ukAD7_9uReVXXZGztIYRSekl6NND4BXxHZKDh11va-1SYu30D9ek16dAGejT7muxaPXcHg2Q3zXgM-HY3o3MJRqbOP7cGnmZ2TiXAc3DukqwEL3L2xzzfFym1KDY0LvgZwlFOfON51quWYouvfFHmRkNxeJFeqh1zOlU_sbNLmcgEqq_flAgYWeBaEqoV_FYq1xM2QG0-sSzwDKtzvK9K6zfM_jNMsPRarLc6Zxlh6JFP-TL9lda1W7NE_J0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=ALM-wijS_CDPGNLVTnGSfH-tbhnJXICwmcc4kVyB8n26rn4Jd8wYMEEyvS7N_wtVjE61BAZDS4UoLQGg23k6qdQJ-Wowmoz4lRUhJOywDL9VtgfI2WICs99M-FwFRIyRmLK4yLvJnDq1ZCBVfhLgOU-RdJL67Z7358pL9oCEyEV6iyPsxbJ9-SUIukofEX8wy5DQRNm9TOigGotd9DmK2oi-Dz86NE6TTT2Bz8qgt1LKLYen40J2f5P5pIs7V1oYajYNUw82PT7em8Qt5aBp7aJ0G2urwS_PnvmuUvpF3sx2B4Qgzcy1JM0eFhtVh58LqAnQswlDAFsdvfPZeSY8Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=ALM-wijS_CDPGNLVTnGSfH-tbhnJXICwmcc4kVyB8n26rn4Jd8wYMEEyvS7N_wtVjE61BAZDS4UoLQGg23k6qdQJ-Wowmoz4lRUhJOywDL9VtgfI2WICs99M-FwFRIyRmLK4yLvJnDq1ZCBVfhLgOU-RdJL67Z7358pL9oCEyEV6iyPsxbJ9-SUIukofEX8wy5DQRNm9TOigGotd9DmK2oi-Dz86NE6TTT2Bz8qgt1LKLYen40J2f5P5pIs7V1oYajYNUw82PT7em8Qt5aBp7aJ0G2urwS_PnvmuUvpF3sx2B4Qgzcy1JM0eFhtVh58LqAnQswlDAFsdvfPZeSY8Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=JSyOGFiXFVf0HtnSSSKzhUtVX3KK2qC9efVyGtOfnYGQG61pYFSA0G-_LViFSinZt0W662ORLqjIvNb8D37P1akGBn4uSlverjAH_RiT1aaBXUBaVxlxLE_i0YufesMvN10uIemnHYc1_f-iTFDQDNkUCi-zRRNa_taNruAZ7xvSrF5cRgDQLQaoGIqZdSQ11EbbjVIbkBmExWThDmemsrxva9DDUnuLhBCKA0Rgyz4t6R_lf9FVZA3UEZMCKsGpLcNLTlAOOIzmdu9nXvPf2FNi1j7Wn_Vdh10ZUx1vuDBwtI8wGDlQUXPTvul2LV8dysKfHtD_DW-DLLpbttY80g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=JSyOGFiXFVf0HtnSSSKzhUtVX3KK2qC9efVyGtOfnYGQG61pYFSA0G-_LViFSinZt0W662ORLqjIvNb8D37P1akGBn4uSlverjAH_RiT1aaBXUBaVxlxLE_i0YufesMvN10uIemnHYc1_f-iTFDQDNkUCi-zRRNa_taNruAZ7xvSrF5cRgDQLQaoGIqZdSQ11EbbjVIbkBmExWThDmemsrxva9DDUnuLhBCKA0Rgyz4t6R_lf9FVZA3UEZMCKsGpLcNLTlAOOIzmdu9nXvPf2FNi1j7Wn_Vdh10ZUx1vuDBwtI8wGDlQUXPTvul2LV8dysKfHtD_DW-DLLpbttY80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcXdjIgn0voSk8vLcnQCDHK2XJxXyBh3U5yUkrLEDu-QuO80xpfckrzknZ91-a-IfQMKrY-Y8aASb3i4-sW1hGLbCiZT1f9Gy7d4O7b1nYAcInrncTdJ8UGDTzdBZ6dqZZ37-GmfCrvrMH0A9vfTdKYqAaR4U-7QVsy6gdvLQxAq4htslH6IChC5dUA3zUYSn5X8G8fJHT00yGmwBDvykI7LxDO2O6IvlBTzlHRoelGn6L7ZPoKZrTgsysT9DDbeWF2wdT-9UGQtDbYq7CwGL5GPLceXDI2a0p_J483YgYaQnVjl86xUT3mMS5K7eNu0y8p7URg_YAg_gSDAjwHs4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=iO3kORyCbEAtdRjW-BaGJhkuZ9ZHHZMch5LFNNHvV_flzAvzBKUuTDhd5FQvUyn68HftP1aioNcdXh4YSKm6Zi_4XDZNLAQrLozFyXqMhiKmgI_7HcYaWJaQ7mqSW2qKz_60wCP8-KdflktuuV4vsg3renR_z8oosJLBAURjktTrIjGS2qov0fiiTaeC7AYnvf5_Z_8TEtdzW_zmPWZ9Y0XI232lAwJXPFlcRCLeaKxWZJ_YyylRZ5Jxbc4qxq49V_GQ877TTPcYFoVmVPQ3sWywBn2fUwalie2ntgkV1HBKIfjTGroAaPfHkbzvuA5QQLRf4zCasR7OuI3E5IOzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=iO3kORyCbEAtdRjW-BaGJhkuZ9ZHHZMch5LFNNHvV_flzAvzBKUuTDhd5FQvUyn68HftP1aioNcdXh4YSKm6Zi_4XDZNLAQrLozFyXqMhiKmgI_7HcYaWJaQ7mqSW2qKz_60wCP8-KdflktuuV4vsg3renR_z8oosJLBAURjktTrIjGS2qov0fiiTaeC7AYnvf5_Z_8TEtdzW_zmPWZ9Y0XI232lAwJXPFlcRCLeaKxWZJ_YyylRZ5Jxbc4qxq49V_GQ877TTPcYFoVmVPQ3sWywBn2fUwalie2ntgkV1HBKIfjTGroAaPfHkbzvuA5QQLRf4zCasR7OuI3E5IOzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=UaZ9TENqLdaJqPUBkms0hI5tLyo7IeV2ZkL_j2uyTX5oF_gtiINqU0Xd2FEIjArqb1eVTJEZwdf-v2wGZnwcSYNWHpou3aE8pr-zuzpTfDX9_MQ4OQVkykq-LuRvGVpbcy1eDy0nGZrrwz7L97US982kYkUGfLT2WGehvi1mNa_IX0sp3opcBbUJTfnlY-sEFarHSFvlcsD3Y821fmLjDNsgph92fnpAj73uuxCGtpXMDY-zIcyRs4rE3U85JJq5vYHiH_Psm-CsnTuvPcGTB5q9W35-6Mx1YrsdWTURiQJ14wgbHmNg6F3mJXITwwv9l3fDRrI-Rrt9aTxDtE3SJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=UaZ9TENqLdaJqPUBkms0hI5tLyo7IeV2ZkL_j2uyTX5oF_gtiINqU0Xd2FEIjArqb1eVTJEZwdf-v2wGZnwcSYNWHpou3aE8pr-zuzpTfDX9_MQ4OQVkykq-LuRvGVpbcy1eDy0nGZrrwz7L97US982kYkUGfLT2WGehvi1mNa_IX0sp3opcBbUJTfnlY-sEFarHSFvlcsD3Y821fmLjDNsgph92fnpAj73uuxCGtpXMDY-zIcyRs4rE3U85JJq5vYHiH_Psm-CsnTuvPcGTB5q9W35-6Mx1YrsdWTURiQJ14wgbHmNg6F3mJXITwwv9l3fDRrI-Rrt9aTxDtE3SJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjKdDWGqvNzd8qrwJi-_Pix1JRpbeifz7cnHVEB1UmW926TfuWlFjcVx2xz1_0l_K5GBwFEVM2TVawfxKW1IjpTRvuIivpF-S1nmV3ixI9jp8bgrYjMPJPSxPWwMSdfQtOvO0xFatQYDOPTFQh1uLo4R9zqi9oRQ6ufSLGGEWG_zNJhcVKFlqqfut0FQiPHPNE22_Gm1VQYT5-sz39PGuCM-INyU6xTZmgstvKOX3izykrms3eOoNJJPVMLcJyzHQvG-HbTwI-bbAi1SmdzCRANelZDlNZ0nJ5JzdKtFvQOmbStXsL-fGW19F1LvCZXQYNqdhwpzY8rbptM4MwxLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3rrSuRY49tF17OgBoE_NulRO0OR1Ytd7Xiv4x-RyabuwzlsNzv0PAKE2BvNryhcT6NfU5q7N5qx6x45dUIF0Z5VJgvGe-rY4TUQfn1EUpS9GBrqzd2Vx7awt3dA0bZdH2XUGctOA9OYt5cg1Cu0MspZxUgipQJsqhl8hjM8Ai1MXXaSF8njKCuwVRBR30LfDBp0M9Wo3MiD1_DS8d8GXYRY37asxyFeWgz4TUFL4PVw4geegNOihUXPQgZeReDcbP5H-3QBxBv5-2j-oz16JrPIo9xaqilTMvRF_5__Lq1yYlcaSln06VhceoInPEuvHqJo7_lFXCZpfTG-HlV5zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rtnlC_QvkYREuKmwP71C6ykgd18ODVNTI3dB-TiXwJ6URMntgwL1S-UsOHIPSIL2THaks8SAta-IDCOeIaBgE11BpqTLc1_3B-TcGJVDRz-JOtpEpqwtIe-6xBF-WvKf-xG1H6zt1LZnx8hTTdBhRubv232bmzDNxN5Fbybi8rU38bBTdugRkEol8z9sk_nqkgqri5lgZjv59i14_7l6FkRRq-tBWfQOVoPveaUY3z5cKhALnum7iH2FDpONYyhVso0p4vOcGBHrBOc2E44_zv4ta-l05eT-p0BfBoRZTJu3_UVoX8ObDFmpLMNZahKRiTIb_-n2Av3-tje4J1zfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=NO7FtAAh2W6BUQxk3Ovmc87YlrxmxSUO7diRkNCZ9SwzYFal7LyLNEZ-eaMFkrBXzF0pHfm_ITPCeGLcWji1SjOQBdxq9O-yAuIPEyKN8zRiWSamz647FeOtGpQE85MPb9nqOsuZVyIfHwDOk0akjwlK02RMIHsNhjLa0z3jdHLwZh5U3Lvg62r6Si6wFphCeEVooH-ZmF7v5vzfnfa5PlO9u207q2vyMd5TAwrDtIbyZZ1ldW2jGvWnls8M6vADUFT1Q8SLFBUE7caEFYY1o-yptkSw2hajmf6afq3PyvbF3kh-CiXWwW18s4rRheUjyioKS7sEo5PagZTtVg8cuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=NO7FtAAh2W6BUQxk3Ovmc87YlrxmxSUO7diRkNCZ9SwzYFal7LyLNEZ-eaMFkrBXzF0pHfm_ITPCeGLcWji1SjOQBdxq9O-yAuIPEyKN8zRiWSamz647FeOtGpQE85MPb9nqOsuZVyIfHwDOk0akjwlK02RMIHsNhjLa0z3jdHLwZh5U3Lvg62r6Si6wFphCeEVooH-ZmF7v5vzfnfa5PlO9u207q2vyMd5TAwrDtIbyZZ1ldW2jGvWnls8M6vADUFT1Q8SLFBUE7caEFYY1o-yptkSw2hajmf6afq3PyvbF3kh-CiXWwW18s4rRheUjyioKS7sEo5PagZTtVg8cuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw_zdsJtRJFbXgusJ3Bkbxrue3uPFounnb5JAefz4zraOWDRW4s_Lv6S7uZFAjg0Fo5GIyEvFPvyXos7PmqabXHPG5OQi2qyptlJc517nJdtX-IszfR8wJUqx-IIeZrFDLYdLzCZtQBaKNnhC-wgDYoQCZaVVikPaR-mpU7gGpZPOehBSCM9h3HWgLIrbF3b3OfEtRmlzUZlJJJe4SMzhkrd9XIhjq6nceZ9eGfGisZS-1HjyBK617IlSC2Lp_929xv032EJleuqEvZf4PQh5IlIUSIJQVg-P4dsMYhqmW9xb2dHEnmazq6o036bSj42qKhvh6Dl7_jo3mljfzK3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bmhx-35A4O4OC2SqAX3K6SryVs9PFw76FQKu_4BwPLdny7Qq79AD1OzSlupZBAzPNjxzW6WhzmGdSPX-fWES7Qpjsq208GFqoVtqcq3dEwyzjv8ebDtLwDvGPBYyDjYqkBql9Qjn2aOBXgTzJvueoXvSV9VXUqmLMNagj5gU7EX5IYRMGC71t3iVuAdhktoq0ujdBPBCbE-23dRIu6NIzKewgGgFW3R6v1Kaiqycd_xTOo0sWrBU-PpVx_8XaToIRoe6d2xxagHUP6kRfRjDX1tex5uZBzN3gagiEkiD4FNvGM-hjZXp5YU548WPh87JQyHcuEUg-y9WWUQv1Q_zpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=RiCcr1eufffc69zphuV2TU_OZwaVUWZHyfp4lTRfAyeTRAyJN_wb5FfKj41I-pG-7ZFzbhTMsTx4UJwO6Y-gGRZ4IrPIPPnzWPzIuNg6v-tMQDNP_pNIevrvjrDvqEj1we9VOfVWS8oxvqnbgqhRGfawUAWPpBjbTAwyYzIyFoblZ3Fv0URSkiUZ218B7JB-FLXCi1-SHbJsQxNzbbufCuQsqrWptimRtaXSnHI-dHKLTBw4lWGg2NwwJSVaF6911aqI5UF8hYEOGkya_y-gdlT7-_KN2bgbT-Gs2SlY_nnWfTRH5Zuhexwmgds8pQSSf1an1z9oN6RiE_onngOsDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=RiCcr1eufffc69zphuV2TU_OZwaVUWZHyfp4lTRfAyeTRAyJN_wb5FfKj41I-pG-7ZFzbhTMsTx4UJwO6Y-gGRZ4IrPIPPnzWPzIuNg6v-tMQDNP_pNIevrvjrDvqEj1we9VOfVWS8oxvqnbgqhRGfawUAWPpBjbTAwyYzIyFoblZ3Fv0URSkiUZ218B7JB-FLXCi1-SHbJsQxNzbbufCuQsqrWptimRtaXSnHI-dHKLTBw4lWGg2NwwJSVaF6911aqI5UF8hYEOGkya_y-gdlT7-_KN2bgbT-Gs2SlY_nnWfTRH5Zuhexwmgds8pQSSf1an1z9oN6RiE_onngOsDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=eVA0GmAnBDmfFw5_Q_JWuqSw8Ji8yFgay1wlmdMUnG2lBKCCJougitacVdZpxfE53yKveMFuPdytQkw8FIz8pfBvLEviZAIq7ouc0p0yV_lcb0aaa70KfDY_CyBpNQBOJ4xeetCNO-LBVosc-oA5rPU3-oGIed4ggDvtX_XWZghL9Xi77NorPFXVy9ZQy4R1R38mSg-wz0ko_xmi_r11XrHNbIk19p-Sx68SKX4GpXNNnhR4oZdzA7KX5OPU1QrAwux672NuKhT0bI0JQZv1A1diQIpCJuHVSjNmttRTDiW0DXOZ8ypIGESG62nmMxSiDgSmACvchopvrp6RPl1a2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=eVA0GmAnBDmfFw5_Q_JWuqSw8Ji8yFgay1wlmdMUnG2lBKCCJougitacVdZpxfE53yKveMFuPdytQkw8FIz8pfBvLEviZAIq7ouc0p0yV_lcb0aaa70KfDY_CyBpNQBOJ4xeetCNO-LBVosc-oA5rPU3-oGIed4ggDvtX_XWZghL9Xi77NorPFXVy9ZQy4R1R38mSg-wz0ko_xmi_r11XrHNbIk19p-Sx68SKX4GpXNNnhR4oZdzA7KX5OPU1QrAwux672NuKhT0bI0JQZv1A1diQIpCJuHVSjNmttRTDiW0DXOZ8ypIGESG62nmMxSiDgSmACvchopvrp6RPl1a2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
