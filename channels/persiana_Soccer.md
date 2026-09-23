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
<img src="https://cdn4.telesco.pe/file/FZiO55tkzNDD_2W2N9PRMP4a3ovaw9p9oXugPRwvLkw2HgwNS0VJOr9Tp3P87fRStl7HSn8cYGm4XKwwfs4NvqVriHMJjNWC881AAfyiAgh_nXgRP0Fs0McOLW-P-vi8iVf5zEQ5xmTRwbZT9SCr6yjmYpygGO8K7-EzEIyE_KV0eT22N7xwlgFhn6Pj1UEmCO7_WCt1_QJem9NxKxJ049a0F9me4x6x8V5YmW66BM8sC8zNOttEDhZsBcCVjVtS1mHFSPACJgaeL3vs9BZ6fcq1O7mtBVV48SsGtLOzyvvgSMSh8y6YL75En27R89UHjH2yBMIFxu9JDyKqOnO-kQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 456K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-30284">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454042688.mp4?token=XlSRuonoHIW1K2SpNjqBWi9Tu7Lpyoebea2PHg3Z76RfkuvgBLV3THlUICi3NLKg798j_tcRv8E9XVp79fHaM9DyWMdbxjfyv-xE5ZQMvqXT5N3vRmRMeR4R84ib73q4wqadCha57eZLDJXETfn8Di_QBd77q22_-X-8WpmIldHJWI2D6hyO5S2nPAyTwVTVZgJPUKdVkJJ7NU7lY_8Se7kEncv1Se3LC5gZBO_jmQTJQsaK1VasaHPgomcfy_UBzuI56FB86GbiRZVUD2gKUJl_9DtzDfP3Ru27-PT1L4ZAAu_4eYN4PPu9zlObgjUHvFXLojhogoob9PzUuH-lfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454042688.mp4?token=XlSRuonoHIW1K2SpNjqBWi9Tu7Lpyoebea2PHg3Z76RfkuvgBLV3THlUICi3NLKg798j_tcRv8E9XVp79fHaM9DyWMdbxjfyv-xE5ZQMvqXT5N3vRmRMeR4R84ib73q4wqadCha57eZLDJXETfn8Di_QBd77q22_-X-8WpmIldHJWI2D6hyO5S2nPAyTwVTVZgJPUKdVkJJ7NU7lY_8Se7kEncv1Se3LC5gZBO_jmQTJQsaK1VasaHPgomcfy_UBzuI56FB86GbiRZVUD2gKUJl_9DtzDfP3Ru27-PT1L4ZAAu_4eYN4PPu9zlObgjUHvFXLojhogoob9PzUuH-lfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌گزارشگر به قلعه‌نویی و حسین عبدی بعد از شکست مفتضحانه مقابل کره شمالی در بازی امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/persiana_Soccer/30284" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30283">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/30283" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30282">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=OY0_rVcMyf3kXqtUZf33-b7V7ODo-vdTeXgyOGuiVnqPNYjsLl1nwEtoLeolUUwhdSeZqD4d4nJeTTjlDWQOvMotCVtBa3q8vGe2U6Yi9gspBjx2JlU85aFl4tn9hNQFhPEoVpQADRTHfza0H1qhmshMBegX6VuWijn1RrtZuRw9hZgr8AYI0dj_F9FOa5_RtVGa-41KF3t-PcrP6cM_wSZlRQJG9EjG-CUNS9U_7FvwJ36UlVHGPuRj3WYAUcOWJZ-VRLVhR0EMe7jqJ14T9Ty1klcUqN9lsWLoBNBRS4iuXOWyoV1yCFiLw7YXLf3_42oyEdzAdDSjeePvZ8_VPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=OY0_rVcMyf3kXqtUZf33-b7V7ODo-vdTeXgyOGuiVnqPNYjsLl1nwEtoLeolUUwhdSeZqD4d4nJeTTjlDWQOvMotCVtBa3q8vGe2U6Yi9gspBjx2JlU85aFl4tn9hNQFhPEoVpQADRTHfza0H1qhmshMBegX6VuWijn1RrtZuRw9hZgr8AYI0dj_F9FOa5_RtVGa-41KF3t-PcrP6cM_wSZlRQJG9EjG-CUNS9U_7FvwJ36UlVHGPuRj3WYAUcOWJZ-VRLVhR0EMe7jqJ14T9Ty1klcUqN9lsWLoBNBRS4iuXOWyoV1yCFiLw7YXLf3_42oyEdzAdDSjeePvZ8_VPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانی بیخیال هوش مصنوعی نیست؛
این چه سمیه که از مریم‌امیرجلالی و حمیدلولایی ساختین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/30282" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30281">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D78ojxFj5Qsh-kxf3WfK8H_U-MdL-XXbR_YZnALLpFHTDmP5uIq8KCVZ5RaKtPkoVTH7lVUsLHPo9CWGT1DI3Grrvd7w796CIWMc2E5gaMMz6Y0YaLw8YiruUiLSa46BUZg2j7mnqRUi3XR9qS6bnyeAkKL0xtvo-ZtR0yniQhj3tzimUhf-0LmeJdVjuQWIV7h908c5O1e2Ur6m3y2CAhJRNvZNjs5-syN9F2VOvUjQZ5zpDU5MkwxyVcBMI54czA-dofhu7VjichprtyhcuXuWvjbrq0eRB2oBPzVWPQt63mRfRukaqFm3smYiZByEcVQMkuoNPFfql5Jb7lcLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب بوکاجونیورز برای دیدار خدافظی کارلوس توز فوق ستاره آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/30281" target="_blank">📅 12:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30280">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTt0SY8d0KPDQpKcQJXf5p2i4IMOu4HeC5ZlT5UumAo8-o8Ij2_WRiPDkGbELh9l7wMKFqBs8hPw9cWm9bMgc0xo0BhVt6h__hKrFZgw1i2fCpYPX-S_BBsTXEAffh_PIudJqZWBxX_UVRPMWCCyNhp__ao0nUJeht11vQriQzM0KJKR4eCSBXe37D8c7dQGTgiWXEEYHroPm2GPQVon2d8PikK_gWR9kuuBdkBhMsq0omrPGM06MESJB2x-RM0LmI04CdQN74wwPg-GBeEn5sQ1ri6d9TJI59GfS8dtiE-HxiyniRFehzSNtJhdTMBpCgn3D4N-2L0rSz0WZPDFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناس شبکه CBS ترکیه:
«رافائل لیائو فکر می‌کنه برای‌تعطیلات‌اومده ترکیه. اون به دید حقارت به‌فوتبال ما نگا میکنه انگار ۵ بار توپ طلا رو برده.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/30280" target="_blank">📅 12:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30279">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUkYjfBIlUCslZJqur6TC62Ug8p7QIJD3knl3nAZiSqUQrYPkQtnXOqFfsA3brbiQPFimEo7LBU1KsbMuGKd7ieWDdVNvX4AIrJhfJkdv-TxkkDpDq93aqIDGnu0uAV3Z2S0-iyL_nhbCAm5MJZJ8Zp1RHkA9J480N88gIAIWGL0oYKa7Du4NeJNRk47ru0qNrADH7oYhAFDB89QZd45rHaCX7NypYEQnR7Zb8uZGkuHjFOCUdzPQ2KRw_EFNL9JnIfHVjKT-gVRckT6t92iYnK7bdrEf1w7wYpWPA9YoeqOIvWgz0hjOF-Y2mmRLDXcpcKvKB5FtgngaT66XM2bgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/30279" target="_blank">📅 11:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30278">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At-tv92HnblOsziQzOTfV_PLP-bKCr9sRpEtgcVoZEyxx02B4E_HPd_OZLzAh_cotC8t8S_DzLOYH6qSzp2mOtOM2FrR1tzc5BTVhmhKj9oroY_78-BRFdx3H5-uUeUJlhYbJU50gJYT45KeUY6lfr-df8hBcCC82H444VojHiv1EN8DOdIxmUiJXSMtWhS6caAXtbyppimU_WbSmcr1Yn_c-4S_sV5CVZmVELo16n2j9SpNzGIs__1baN6xH25veCtXL30BQpcTvupsKg4f73WglmetOI3f4gaG2BBOjEJoQxaKSH0iS-f8J4hUidw0031PqqrSwb09BR_H5Ha21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/30278" target="_blank">📅 11:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30277">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf_jKTRmYLc3l7HC1dmrM9ZbZzZf5A_l4t46gWe_UU8IWL4fokBXMKUVwaQiLA_UzJdjeJp1aznAu2UvLl24CfRqt_M9IO2EQ4Os9k4JPflxR3tfDBfh7QjEvXvnEfjJ23P7FlVmkm19Op_xM4ebAj5g8-CeN4LerN4SrlM8SVGRxkDXHDMBFGln-Vz6PrLHPQ1aRtTi3ojb3gkAE3ekdoCjGRm8JJiVvdVSSrwwAOKPlVn-417LrKfSwqiLrk7ho8Z7icyFG3chmJSubNFLIUVVCmG4TPhnOpqzDj5jPLt1XQiZuUWy9kAVMulEPak7BD8b_UESJiJkBP3eKLvIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/30277" target="_blank">📅 10:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30275">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVgSgiitINGxTwFmc05IVZ_3EshXV9Ta0jK3CUgD0IMKOShMe5uUkMqxE7W4H308kUQWZInDWT3Yv0mBMGvDdh9Vf5Yg_uT_MC2VlRXe7-QSoeWN4jvurKB-4JiRgOyXWsWYFLXBWTb8yX0p2JYtvkRAzDbYL5sYkyVgAQobFtgK6KAQ00gWzeDz2gKY5rzvpnp_8gKvQKyJBzh8OR9mO9Mc8K1co5-6_mlyc9MQChxGoGm1MSjMWc0KHDZ1UIoz_hSxPmPKDpkt1dAjdssFpZNeBSC6ULTi3x9q7Pw84lcBV0_y_WJewE-Z9MDLHafzcqy7gwl7Bl_Pw4OUesIbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6HvTN37ZGL87s_OoFNpEd-r3xCECNQWzuJIAP0iaaequkGO5kGhVkfIEkun13z1U2tfQrS7bQadxWmxnenpvblVfnbQO3ZRDoolqO30pvya7GsAXI9p53iDzSoo6sGdOETnwIVagGG8ZUktVySJDOWdxbYSVC4G6uvCOMeBpaV3nBWtYay6S7sGR0HCQ0wGZi0h7b6llAsXNTsqvPaMmPeJKKw1uBuA_ZzHjYzYnE_rPD8-FE-GrpJHVfEWHaEUbgKNYVyyias4jUmAbkwiqWB5_ftZXuLoFqG2RsAyFe_ryhmgF5rKNYQ6TOUX1FFp91qYkbW74WszXMS3R1e7fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/30275" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30274">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWUCg5QmaHkvsoTVoa7-_c8Qeo10w1auaQSq9rrgv1QVufYpJCKlVIZsFg9KVsqf4hNBKXycPHgb9Edgs02v7DZEft50Dc6ymyiEk1p55cs4tpZ0KEtBEsYmAhnemU3jGh8qVdxb4BL96DAKj9AGXakYORe1ZHZhOk-fWt72s7-NhpMfs0iiRV50peJo6cCbt0gvbh175zGNyglmQToUtLwo0-LgA1bzobJeJ3eb-sHDiBoyNH2FRzbwK9bbs4ZXl0ApRgNr1jTVCDV73V1xlrEFTYynGYzV-CI00DxCR0p59F_VzFGi51cLEG9IQ8v8T0q6Ux7W1pGF_FI2FuwJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30274" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30273">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thXebj5d3r-P-0bjJWGrB0rVW8N1_okxt41Fpgf2ecFtzjYeCupDxL8kEgMgQ7LlufIx-oVGQvxYqmsFijBZcmYWQsG5HlIpQg0VTxKeBK8Zmmakxp4G4sb907oDakosGFffw67bPq0poZY8cqrZaZAHHuXyazNEqcXwKbQrGaxOIV3iMkFR39tUtSYvLS6VyBPGGPnO4Ieqr4Gg-PANjJNT1fz-7wBc0Fuv7zIIJi4gS5xN0xebjkYb0Ux3L8Y7o8djnrhD_ECaKD6UnlMMuE36tVq64HDFE2wblEhCBi8XyLgi1z00NYtmjgsWuIyVs1hjz6jRCG_-RCtewR_UdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤬
گردونه شانس یک فلک
👑
هم برنده باش هم لذت گردونه رو تجربه کن
🤩
واریز کن
🤩
ازپشتیبانی کد رو بگیر
🤩
گردونه رو بچرخون
🤩
بدون پوچ همیشه برنده باش
🌟
جوایز بی نظیر سایت بزرگ یکبت
👇
⭐️
آیفون 17
⭐️
ایرپاد پرو
⭐️
پلی استیشن 5
⭐️
300
💵
جایزه نقدی
⭐️
و هزاران جوایز ارزنده
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r1
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/30273" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30272">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpngXIDCHJz0sjujAjXNfzj-L5ZfyqhprTqKYwWLYiRTbIXEXuaV2szv18pazySdBRUqfj6CAhQXl1V6N1bT9HiOARz-M_5HahuwwZFUJZEh4cLykiHr8wZzQPTTW_Upul1rWr3iEE7jFgoZtnkBI6ye2Y4LMezZg2sTowJdoaycdNXRgTLQBzLVnWd_uFwt2Ig_EkleXGTNI4sr3_ldxDZ9V4p4uPS03rAS5Cw2DZzBTdHeoFl3ddSUzAF_IY3rBWMoYT0Pr69Ns-qiRbcX3SCADyDH7E5zqgQNpcaX4G2zEiIARj7WoUjVumJzps-Oq1mLBZ-j7e0ggostoEKtrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مثلث خط حمله بوکاجونیورز در بازی دوستانه خداحافظی کارلوس توز آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/30272" target="_blank">📅 10:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30271">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=cb6JD6IKooLO5Ja5ElbIbsUTpmiRH6V8GFiDvjVTRSn96WDZVIB3en9i05_RlrkowmoBwP2lodJesS2A3IXZjw8mSHMCpDqKhpXWXswYkvNLWtPGxCpxbe5wpxAf0LVcuzAScpGUtKVL5RP-WCRPNdM-ABQnPJcPK66-MTAEJ3GYnXRlesToBLPG9nHQMEc5dKFWg9Sv0A6Kq9ShI3RlCA49BYJU0ub4rOQmAtMe1WH8ZleUz_m7TibxXvX7pC2p5xiNkxm61qN4MH16WhS9g3IdUxfCe0c901EQJbrsutAtxvTIXcOyP8aiRfY2-s_r85070xyJZm9sGAlaUsE6CEk-BJnY6mYcvcyBiw-bHzxE4zaYWLyUcc3CecWm8iMh7jzrbD5-OCJO9fKbJprtdX6SWYM8iOXux1uCaoj7e5Kv96SqBM6MALzRoff2FmQ1OSgyEERcJRXBPIeEmEvB64bMRpzsQGJmgRbD2Tci8r_jSfmlEklgJ5NF-oXDwjTTL27v-xXrn5JQkMCgREpLXgShxkia1lVYavNRZGMh6FX81bk0moptPL-FxOJqZ8H7nKUBgr6VFX1hOZqyj9l80r8XyCrSantngrIj2mDswTFamRyGv1y4vjLAsZYEBW3a7JH5HGXW0eqffTgp32faM8Rsm4oXQr9H0zRGzX2tDQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=cb6JD6IKooLO5Ja5ElbIbsUTpmiRH6V8GFiDvjVTRSn96WDZVIB3en9i05_RlrkowmoBwP2lodJesS2A3IXZjw8mSHMCpDqKhpXWXswYkvNLWtPGxCpxbe5wpxAf0LVcuzAScpGUtKVL5RP-WCRPNdM-ABQnPJcPK66-MTAEJ3GYnXRlesToBLPG9nHQMEc5dKFWg9Sv0A6Kq9ShI3RlCA49BYJU0ub4rOQmAtMe1WH8ZleUz_m7TibxXvX7pC2p5xiNkxm61qN4MH16WhS9g3IdUxfCe0c901EQJbrsutAtxvTIXcOyP8aiRfY2-s_r85070xyJZm9sGAlaUsE6CEk-BJnY6mYcvcyBiw-bHzxE4zaYWLyUcc3CecWm8iMh7jzrbD5-OCJO9fKbJprtdX6SWYM8iOXux1uCaoj7e5Kv96SqBM6MALzRoff2FmQ1OSgyEERcJRXBPIeEmEvB64bMRpzsQGJmgRbD2Tci8r_jSfmlEklgJ5NF-oXDwjTTL27v-xXrn5JQkMCgREpLXgShxkia1lVYavNRZGMh6FX81bk0moptPL-FxOJqZ8H7nKUBgr6VFX1hOZqyj9l80r8XyCrSantngrIj2mDswTFamRyGv1y4vjLAsZYEBW3a7JH5HGXW0eqffTgp32faM8Rsm4oXQr9H0zRGzX2tDQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛ مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/30271" target="_blank">📅 10:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30270">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=ofd8Q2H6xp6wEn3A7YVMWrFxzUk0icXFiAKOAPVAPa9toFV9pqtVKHblIdWvtRS44HYcnExgGCkJNylUUufxBSllFRjTFWp0l2UTKhsjWjT3B_kKi3WnRAwBt16tfxZxDCBpv337pzL9FM_KnuoxExyO_IYTETSRzuDCcVWnrZ3pJ4XWtT6D2jfbIHoLxIdzHkt8hE6aUfcqvlWefAAwLr3Mfjgux6Z2Fi8k674Bpw0vzKu5QUYu1NVqUsQ7dubu10_qbU7VRHTKP4tmuAwTm4hr6rXDrKUZW70gZNMH9_2_uJrSRfZlplRoQ4Tt_oDGgZNnPn4zD-tz1q1dPVQgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=ofd8Q2H6xp6wEn3A7YVMWrFxzUk0icXFiAKOAPVAPa9toFV9pqtVKHblIdWvtRS44HYcnExgGCkJNylUUufxBSllFRjTFWp0l2UTKhsjWjT3B_kKi3WnRAwBt16tfxZxDCBpv337pzL9FM_KnuoxExyO_IYTETSRzuDCcVWnrZ3pJ4XWtT6D2jfbIHoLxIdzHkt8hE6aUfcqvlWefAAwLr3Mfjgux6Z2Fi8k674Bpw0vzKu5QUYu1NVqUsQ7dubu10_qbU7VRHTKP4tmuAwTm4hr6rXDrKUZW70gZNMH9_2_uJrSRfZlplRoQ4Tt_oDGgZNnPn4zD-tz1q1dPVQgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛
مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/30270" target="_blank">📅 09:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30269">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Z7dqT-9j3v7q-7E-m6ROEIjV-bHUEtkjx2d5oMMTNQoq8M2uqerHhalOB2tsOGCi3tZLSlk7XLE7D244K7ffh7H9uDALOQ9zLsfY-RdrTOWrkXsp4_nyrIEXvCpfPOo7omWDMr8-_HxihTDzqm-XiVINmIm0GflZ2EMRScCdKhoT5h-dMPLCtqW3TS4ucAYluio4C1cFIbpeE3h6BUs9K-ly7UMuKjmcEPO5eiQXnpJ3oh205UFTc9zi9-2N4lTLSc-xrN_JP2qz9DqWN9TjkQJTNbCeT66EEzpDn0oF7N6f-GNsR-x5f27IG5kdQPAZm2A8_V7LtOo6u8iM5SAsHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Z7dqT-9j3v7q-7E-m6ROEIjV-bHUEtkjx2d5oMMTNQoq8M2uqerHhalOB2tsOGCi3tZLSlk7XLE7D244K7ffh7H9uDALOQ9zLsfY-RdrTOWrkXsp4_nyrIEXvCpfPOo7omWDMr8-_HxihTDzqm-XiVINmIm0GflZ2EMRScCdKhoT5h-dMPLCtqW3TS4ucAYluio4C1cFIbpeE3h6BUs9K-ly7UMuKjmcEPO5eiQXnpJ3oh205UFTc9zi9-2N4lTLSc-xrN_JP2qz9DqWN9TjkQJTNbCeT66EEzpDn0oF7N6f-GNsR-x5f27IG5kdQPAZm2A8_V7LtOo6u8iM5SAsHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌‌های ابوطالب حسینی در قسمت اول برنامه جدیدش که هر هفته سه شنبه ها قراره پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30269" target="_blank">📅 01:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-ojI5rTqTEJl1-6O8uT_eDMO_393YAl4-qUgRax277zc12_OUWvGt0YXpnKg2E2uLttoEAu7uEAd_kOgvszTax7fLFYTCUb-0Tqeh8OGIBJjvSvILM0-XLjkpiwsu_kUpn_-8M6UJps6BQOFzu1Wx8VGeC-1Afd9eZI-U_-Y49DLbRMxNNOlSp4UbNt3e4b24EnVGq9ER0ZqUWw-JiuuqFwLZ0DUrr02wyEjwvg8hdNIS_vz537P7wWtqyPBEKaejVz3DJdBPu_mdMg8nT-CnU2ev8qTzMig2tLrAVvEenp2g3sxabOOuThD6f8ujK_bxKz09KRN7XWOPrA3GHXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ بازی تیم‌های امید ایران و کره‌شمالی برای صعود به ‌عنوان صدرنشین در ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/30267" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=SuIs2X8c0F3M4dym_WOrh6FPclEM4yyYSab_Wq9eYwSh3MoV5iDtm1BwUrQittpPhZpPiWxrkuM67xoPtzGxDxQP7ANa8zEyWhaYesqGp-T0m0CvGw7dw6F4cqQoZ7e8ExpopaE7qaRSF25ozR5oq3gApm-K_Y07g9GxM25axKho2BfPYFT3bWZSf4-mR3KFStKIs3Pbhf-ai57dKnqRAfCP-WlEsdhflGk8rmhLtxuO6Xz14NxsEaev2nCKGpBIjDMmXEZx__fSDGvPGdDvtNCI9ymJj-1KQBBxNYK48XOn2xzAvvzi3ByrIHV39HKbyBns7rKTov8ko6UpFYC3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=SuIs2X8c0F3M4dym_WOrh6FPclEM4yyYSab_Wq9eYwSh3MoV5iDtm1BwUrQittpPhZpPiWxrkuM67xoPtzGxDxQP7ANa8zEyWhaYesqGp-T0m0CvGw7dw6F4cqQoZ7e8ExpopaE7qaRSF25ozR5oq3gApm-K_Y07g9GxM25axKho2BfPYFT3bWZSf4-mR3KFStKIs3Pbhf-ai57dKnqRAfCP-WlEsdhflGk8rmhLtxuO6Xz14NxsEaev2nCKGpBIjDMmXEZx__fSDGvPGdDvtNCI9ymJj-1KQBBxNYK48XOn2xzAvvzi3ByrIHV39HKbyBns7rKTov8ko6UpFYC3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
توصیف‌های عباس قانع گزارشگر مسابقات فوتبال از لیونل مسی فوق ستاره آرژانتینی تاریخ مستطیل سبز که تنها یک بازی باقی موندهه که از دنیای مسابقات ملی برای همیشه خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30266" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30264">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxrTEK5bjsdlOw-kegsmh4KunPpm7C7x1Ov0p1nlQ817ZC6-ygHpWU1bmw3AUSfzSQBqtXBEUnvArSgovxL8jgtR6BuybYsCjO5eYJ9tfNCCouAWTpN0a9V2GNQLlMl_KZNb1VBXh5W-NhtbATxEMFybeSsWMvv3j0SyVrGUmUUm4HG9ymfxEMK6VgxGX_9pJqQaovTYrezF4-EtbUCOxKcvew709UJl1hfefj3pB-UJd9XuhC8NQd_xnVXgZW9R6y9xK-QiWeWWxNjvR6rINlFbJ7fsnwaSXDHrcsvrrgoC3gzEMlyHbAoOvOSopk_QOcIscnLI7a3Eq4_y_zGr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30264" target="_blank">📅 00:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30263">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=PEu1dmKUkQEB7VjcCG2G7GQHG1jY2h9vl2kL3O46dAbz826Zauxl_GzxEU9Gl-smdceh8oDQ6J-Qll0GzcXjUEYJQUFVKnDj2he3vrqHDBVab4pN4GLsMNCsfpMMv2CYLp05JuoJEvMQmTMxF3w0taUZRj5Nt0-EI1BGiVGTnYNjpUEizIKE1yhvr0_MmqsqVmZLTBPwAJmQM6ymzt6EllygjRiiLaL3KDlje-dcMW0K_IQUZBYFXYCQZRJn_-RMGlhm3NMr-PlLSEPzeP8gp_VDODdynYAfmup7_x7M5xL3VNirhn66a73qDannC9-vbSecbpk5aiTtZj54xCRuEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=PEu1dmKUkQEB7VjcCG2G7GQHG1jY2h9vl2kL3O46dAbz826Zauxl_GzxEU9Gl-smdceh8oDQ6J-Qll0GzcXjUEYJQUFVKnDj2he3vrqHDBVab4pN4GLsMNCsfpMMv2CYLp05JuoJEvMQmTMxF3w0taUZRj5Nt0-EI1BGiVGTnYNjpUEizIKE1yhvr0_MmqsqVmZLTBPwAJmQM6ymzt6EllygjRiiLaL3KDlje-dcMW0K_IQUZBYFXYCQZRJn_-RMGlhm3NMr-PlLSEPzeP8gp_VDODdynYAfmup7_x7M5xL3VNirhn66a73qDannC9-vbSecbpk5aiTtZj54xCRuEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بالاخره‌تابستون‌لعنتی با گرما مزخرفش و قطعی برق پیاپی اش تموم شد و وارد فصل دلنشین پاییز شدیم. باشد که روزگار هم روزی به کام ما بچرخد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30263" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30262">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9fyzlFBoxThjZPJcKq4D1qJQUSfjtlVWn_kuQBRdnsvcjdT66zWUBjpbhJcpH2188BED9dbnf1MzqnN0hI75dR8VP8lW4GM33HB3xJYYnAwAxOAiZzFafs-I6MSxmjSd0J7ToZcOq4hiOfdlCayQMmnTue2i3isErjU13QswUfJak9G6AUds7dZQC9k5BflG19_AEZYb2bejJT6BaJgLWgVTjiGC8R-WNxjtR8rUXOSIqgYSARLaehaUIgJp79LJNWcB2XAOAvCNOkbJZbBOfq_Y5XrKV3NijoBZvwG33sklg0X7OLkJk9NkiUJGgj7ipQLEfP64TjQvRlacRTUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شب گذشته تیم زیر 17 سال النصر در لیگ برتر عربستان با نتیجه 2 بر 1 از سد الاهلی گذشت. هر گل النصر رو پسر کریس رونالدو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30262" target="_blank">📅 00:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30261">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP_57tllRopNbf_eXcOf9UvcHmbPW1ZTicNK0rD4MSYAM05mjwQoWP3I0P57HNioWIJdxNHMqLWLMzO8z0Le7z6NiOU4NOADcntpmgdjFeUK6tFI4aOwJG3pe60SRzj4Du7Dm4n9C12R2SBwqdOZTcJ2NAuaPPp25IyF0_DpXsUACOUWmg6qIBX9TCaFtH0DbmtDFR99EBszN8NmCqPJTjmBV1EUXlZ3s0PjrRYIy8KppNGhtNuJ8eW55XEsDOe3lBkJdc5JhzVAw_Tz7HLfLpfVbJAdAberJQ55450vvnjS2tbsFqnGo_LHw8krSJOCvr71PpeAd9WHcRMZKIN5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام کمیته داوران لالیگا؛ لی کانگ این ستاره کره‌ای اتلتیکو روی این صحنه خطا روی فده والورده کاپیتان تیم رئال‌مادرید بایستی اخراج میشد که داور جرات‌این‌کار رو در ورزشگاه متروپولیتانو نداشت. به احتمال فراوان مسابقه این بازی محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30261" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30260">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJIYSPKzNq5pfaZn8oN4kTSULncEx6k0Du-8xRHvR50f-lAZWw_6bjeURdop5N3QxBSpbjuFxvv-Fj8vMEEQKDOTdVotFF-RAuDA_DBGXu8HpjwKCP9o6JEAwPY3SiRnGiRKIP2MKpMZY5VKouQ3fG2yT2YuLGqYFDzOdplKbrgs108u8fgeoQ1QwbFsIJ3S9elHWx3eY-bzRWYFP_ajM_JAsJCFC1r3jPdn80w7TDeoqXRKSqDKh-rLRLnGCVT0bamws4OulIKqvnEUFpIWVaIEbiA72CmKAPti611n-8DKW3T-1FZlHQUE1tt-XkMAGirkXzZUPaULgUYvb97Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30260" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30259">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
چالش فوتبال دستی بین تیوی بیفوما ستاره تیم پرسپولیس با زهرا خواجوی گلر بانوان پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30259" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30258">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siKMJrE3UMsUPWgfI-C7a8uorMQojRi1kCtEDbEIFT93z0oWB6Tn1w1LF2wfynJNNcyggo5bCyzis7QRmGH3DH5P5oper8lcm6fROc0OvNQRGT1iTkB4FbBMqGxGDe_xT3gg-zAzdZcSuItFJ5PAETJcU91Tz8aWif5ScBY6c97g_6R7bbE0WfifkgjzfAnLDnuh4mfRjDlT6J9_41S4z-_HvykPrfJKZbd3lve6QGrRE8F82_ztFgW4PCtJGCyWazlFaHIBId_X2YAOV6-Wa3SDpbrxsL1P3uLHKFmeOe8GvtYLf3sQHzEjWuHz5NXbtlFY-qo6s2k0cuBVJ21iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛ تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30258" target="_blank">📅 22:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30257">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h53c7m7GgZmBbXWpaQOLlI0H_kDoE-8uW9KqO9APisiJEXl_8-flPxG8HzAVpA9yUjRjRaSOhZ816KMOrOx3TH20kGAptOItIND2W8k7vtlxAAebv5oQa5c6IthxbzacJ9PsBliYBffku3P570rW8XgZDwIopLe3fc1d_y9CyYVliafFWSmeNQXfgzszNsLaniWm5ekR0vifnJZp-xhqoNTfQwmInVluBnksOtJCvlh_Z3Jf6cQENh2lUfIrgmi3PQu6udRnxOpUiq6LYdW_8lfv6aKggADXav3R9Q38V890cUVuzNaFW1CqOsHJf9qRQbnYgtmFDhCtlBO7eDfvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30257" target="_blank">📅 22:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=MDWYKdSv856HleChpn2PRgYOUACV6Ty4w1jckgPNXOFUa8epqD0b62se90aqNOpuYCNpWEbdSYYLMkgfzjwFP2trD6rjYvpi2IapTtTXc82uMh8M218dnlf3KAnS1b1meTjtuTFZQl0MC00VQScukEC9-c_FwDhZa5AYIA8jVN9Azow6HkVZO9yNsFcYZMLXWKnRGc0MDPmEVnXYYh016F7-X_IB671JsiUng2tB4QlzXRlD-mUJBu3APetv-PaeRyFqfqURb_cpEYRdEx9kvOSWohHAzvLf0e8vPLpkA7MlOiwCSfErRvxmJ-RrngxppxKOgscQgIOLlEluzyPhB7lkrEfL5pKYTkqD1FbVwG-6dQDF_eqc9FDNDowAmyKmoGJwy6BuL5Df_sUCxPhqZo3x85MRigWkhwQD34DGNZhaNlQJhlV2wtWlDrgnW30KVlDfIHBaZQUEgXkvyk4WkP93j95sohOTM-UOJKkjoqokzrZR9taAe8ebuhIdg4XoVuoOBAdipZaFJ4QxLrlXK-c1SzJLguyzYWziwVpdYttH0OmEZBKphyAoi91YLanAwWwTgp9eIiV59E7hH5CD0OGXrR0NU3F02CCKvesRfdDyCR5rrM8Htk6dcGy90IW-up8cApHj_VrVymj6DPuu0CKeARrmmhB1mX-vHe_duUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=MDWYKdSv856HleChpn2PRgYOUACV6Ty4w1jckgPNXOFUa8epqD0b62se90aqNOpuYCNpWEbdSYYLMkgfzjwFP2trD6rjYvpi2IapTtTXc82uMh8M218dnlf3KAnS1b1meTjtuTFZQl0MC00VQScukEC9-c_FwDhZa5AYIA8jVN9Azow6HkVZO9yNsFcYZMLXWKnRGc0MDPmEVnXYYh016F7-X_IB671JsiUng2tB4QlzXRlD-mUJBu3APetv-PaeRyFqfqURb_cpEYRdEx9kvOSWohHAzvLf0e8vPLpkA7MlOiwCSfErRvxmJ-RrngxppxKOgscQgIOLlEluzyPhB7lkrEfL5pKYTkqD1FbVwG-6dQDF_eqc9FDNDowAmyKmoGJwy6BuL5Df_sUCxPhqZo3x85MRigWkhwQD34DGNZhaNlQJhlV2wtWlDrgnW30KVlDfIHBaZQUEgXkvyk4WkP93j95sohOTM-UOJKkjoqokzrZR9taAe8ebuhIdg4XoVuoOBAdipZaFJ4QxLrlXK-c1SzJLguyzYWziwVpdYttH0OmEZBKphyAoi91YLanAwWwTgp9eIiV59E7hH5CD0OGXrR0NU3F02CCKvesRfdDyCR5rrM8Htk6dcGy90IW-up8cApHj_VrVymj6DPuu0CKeARrmmhB1mX-vHe_duUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2011 در چنین روزی؛
وین رونی فوق‌ستاره‌انگلیسی تیم‌ منچستریونایتد این سوپر گل دیدنی و به‌ یاد موندنی رو وارد دروازه سیتی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30256" target="_blank">📅 22:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM8iVPTsqZA98Fi79nn-01QokNnzJruzx7da6YgvCOP-QuBBhW68toOmt5wchIjG229cO061zK9x6nZfzWj9u15oypokbzc6fXRZP2uALtNcs4l4jz1KLQaG4CgxePWECM8LzTvFuEvw6pVNPe4VcGihyv16BEYzg9KoRRYg3nJMZqng3-UGIWHBvJOcMDN-WtxQH1oi1V8ojtHYy1xJNLo_0_ZhexA9_pu7mcYP1Hz4QJttRGuIqi2bd5pPVYvQACrn-0TKU08TxHcss259lwwrc8T5j60P0x8qQdSq1k7lNfaxaBj1hjNhgQ0nHbbAZC0Ozcuukv97KJvCkcF2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30255" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHIj1Nkhvp5MnOLtmuILXjECSJTr23bU10YWqBcIRJGFOkAFfKTi2Qyv2QzIPAFA9IS1S_CPTp0slCLTWlVFl5Z7mIMtvGPUzd3Sf3InLXzx9dv9fAEGXdhwD85fpqjvBRJl1DQXCRkw-qyu7TrC75eoOV1uvsmmApoo5PzsHHv-anqTWEBX-gVFA-4PtXh0GyX2IUmJ7ZB3eB76SSXQNltCNuphBMTVKf9W4OU35uE84rdMJCiZMalKU6V5fsRtHQVbSnWv8BhyhLLXCpeugOHV5lCMS96ywg2PlyFJZm1EHgtelnX1cQw1LPvzwiFVWVSuJGa8HLm2_zzivJCR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛
لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30254" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS41kz7ioSBK0291U9p1E8YgukCTOnQeajopz4CPRg1ak5PuPY00fFMkzIiV5-6XWKZQ9sDG3FBivBxMCoAev5tiQ7IkmDl95z9fjl-WoPGKt0ZSPvX4X9Pe5XrnyVwS3enzx6TWo_jAplHbswfw8CI2BXts6nQfXUQyD40LLZRq0cB2o9zUhfq_0GsTM0-PLqP_pPOUnczMI0xii8IwT3b5PFtYSRj0Izkme2aMeMiPh9CuiMe7H1j4lx6RQ2ABfBV0aWvxRjbvdWo0ECFNto9fbL5IwkyJx3ORQWhG_TOJfOAdy2O3ji6q8D2QZ8hJpsaUrVFGzrTn7LijdNMmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30253" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjW1Ox9FJRHNC-MCzHIwTcHwKKNl2cEnCK9lrPJHrneko-kY1NJ5MQy3Zl8ptU8O5x2JSvsJU9O5pyHcBjF-PK1XDuM5r1afvT6ptCaY3Gnli5AqNfb3I0W2ReHOt2eXhWEGPbPs2pgguZfnTjpFLVcFEhnRjXfNFMep5z0Kfbi5K2nQeidGKAlD6LYgIIYczdgsT0GV3U9qi_1yEK9orNP9P9BQFB_4HiCWS7KBX187JB_1VccE-MLyAOCZ1-eALUEWXo7xFIya3JLWBG2fM5b_16qD87pIf_s_Dqlf3gCO4mALmVIE0tlI695pp9F889PMp3JFzuzSromjp_83fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ خدمت سربازی فرهان جعفری 28 آذرماه به پایان میرسه و با شروع نقل و انتقالات نیم فصل از ملوان انزلی جدا خواهد شد و راهی یکی از دو باشگاه پرسپولیس یا استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30252" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H01-inSsUJxPg1eFsKYFbSGJ8tkWX2OTcpOzXNNBlBLX48yp3X_CJT09wbrDCu9UX4T8jpzMGQc3wuwieEelAvrkwWg6MSDRoo9l3A6fygV4SR8nQjedOBtHwUUxMb24nLCyLSy8UL8A5HbR5aPrTypXrSijvsruINxpdLIjQbNYGU1mI-HoJgGNWajDJd-5HM0EiJegjIOxk3Bcdp66l2OCSHS8Uhe0kcAgfX-51JGbk_RLZDqNiQs8JCN5a6SvEN-DFAS-xAhIkxmul8rzwii-1zZUWRpbP9McuojDV9DOkiG0QglWtxYiwEA2ovp8kG5tgfg5zqrQSVqjdxSVIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H01-inSsUJxPg1eFsKYFbSGJ8tkWX2OTcpOzXNNBlBLX48yp3X_CJT09wbrDCu9UX4T8jpzMGQc3wuwieEelAvrkwWg6MSDRoo9l3A6fygV4SR8nQjedOBtHwUUxMb24nLCyLSy8UL8A5HbR5aPrTypXrSijvsruINxpdLIjQbNYGU1mI-HoJgGNWajDJd-5HM0EiJegjIOxk3Bcdp66l2OCSHS8Uhe0kcAgfX-51JGbk_RLZDqNiQs8JCN5a6SvEN-DFAS-xAhIkxmul8rzwii-1zZUWRpbP9McuojDV9DOkiG0QglWtxYiwEA2ovp8kG5tgfg5zqrQSVqjdxSVIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
هایلایتی‌از عملکردخاطره‌انگیز و فوق العاده لیونل مسی درتقابل‌خود با منچستریونایتد و کریس رونالدو در فصل 2007/08 لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30251" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=WpQN-GPbfWgguyOl9RRy7l-te_iOlt1LmxTbH8SDmuGj4LbTs__xX80idVHglhjjQgWtiKEIiLxgmJpZ3oMynDkAS4lnDq5pus-HLodwYISoKEiNEDGFxkV7n9IWh-pI0jxhXLXP4R_pzF7H-vU0EjPHazFSr_FjmSCq4OkepJFy0hde7Cdi53i6zu7Rabsvd9FwnbQr95nQXBShxBnYEXVJ8vv0yCKCutE_GMAH2Tgqbrm20NFcasBh3ZZ1b46c0QEPhgzefSEhC1f2XcYn91EfRfNTiwadsA1KVKCrIUuJlolH-QdL3UeSe8IgYY1Hi6kyvT9Zbl5uorRfYX1CwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=WpQN-GPbfWgguyOl9RRy7l-te_iOlt1LmxTbH8SDmuGj4LbTs__xX80idVHglhjjQgWtiKEIiLxgmJpZ3oMynDkAS4lnDq5pus-HLodwYISoKEiNEDGFxkV7n9IWh-pI0jxhXLXP4R_pzF7H-vU0EjPHazFSr_FjmSCq4OkepJFy0hde7Cdi53i6zu7Rabsvd9FwnbQr95nQXBShxBnYEXVJ8vv0yCKCutE_GMAH2Tgqbrm20NFcasBh3ZZ1b46c0QEPhgzefSEhC1f2XcYn91EfRfNTiwadsA1KVKCrIUuJlolH-QdL3UeSe8IgYY1Hi6kyvT9Zbl5uorRfYX1CwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از اولین‌مصاحبه‌کریس‌رونالدو 18 ساله با زبان انگلیسی بعد از پیوستن به منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30250" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib28Ar0idDyVXn-aLjzj3NNEVDEZbChNnBRYFm8vBiaTFPHW3FDPtJne0XzCZIP3-gCYxJg08v-nMdqmw3w9I_mjS-XJs1k3lw1aEQuFlI_BUqeximq4iRGSMwjXaL0iLmJu6s5SFW5M7544wVCdKkK3opunAREnbhPr2LZTTdVhrgD2IMQ9UtUR1nES2mHFMJA5dyBcR9lPFeZEJ_nXOiKJjYMDhUi0K83mizJjs4fiq1ASGfMh6hMptHlWQ1i1NnCQiQHCAoX4-rblVlDMtQ-pVHNhmLwmPx4sRfOCOReh1mFCvh8QorgrCX7EHMug5HTsmIkr-BApZBT5pVlBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شیخ دیاباته آقای گل سابق لیگ برتر:
استقلال باشگاهیه که حتی آدم مرده رو به بهترین فوتبالیست تبدیل میکنه. حقیقتا من‌قبل اینکه به باشگاه استقلال بروم هیچ تیمی بدلیل مصدومیتایی که داشتم باهام قرارداد نمیبستند اما اومدم استقلال پیشرفت کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30249" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=he82DyMKikySUZz3wtuooAoFYmM67hCOFy-bIYZr_xtmWaqtnQsTCaHM1TqZJX_ejMA-KZ1JIT37NqmeKBtTeM9WZiYk3hxHDcN-nS47g9Uf04Nh2KExz84-rUFmJB2K8l7VmsyEQBMJ498PEjkYunYiV26xOAnEe1fbVxGPVDA2mezhLb3PoCvXoyGWp9j5WEAZGbt12rDa7qvC92BLV6gfPr1iuYQFLgh-Mv8SoRQC_JTlsz6iM75BeDNoUaXgYJduf8zNarYKXWsLyrHg9T4ISfDKMAj8jV6EBXP3l6vKyHkavzmPSJIwzy2Ov2n2-06LRMh4Tk1dMzF1zgnutA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=he82DyMKikySUZz3wtuooAoFYmM67hCOFy-bIYZr_xtmWaqtnQsTCaHM1TqZJX_ejMA-KZ1JIT37NqmeKBtTeM9WZiYk3hxHDcN-nS47g9Uf04Nh2KExz84-rUFmJB2K8l7VmsyEQBMJ498PEjkYunYiV26xOAnEe1fbVxGPVDA2mezhLb3PoCvXoyGWp9j5WEAZGbt12rDa7qvC92BLV6gfPr1iuYQFLgh-Mv8SoRQC_JTlsz6iM75BeDNoUaXgYJduf8zNarYKXWsLyrHg9T4ISfDKMAj8jV6EBXP3l6vKyHkavzmPSJIwzy2Ov2n2-06LRMh4Tk1dMzF1zgnutA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30248" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDMAMWxspcSyEjz6ckOOw-9XzKfFKu-t2ap0XWHAD2T25FbxX6F6hOM7oqF47dbhNo9jM9qOgWJAgPEzgnvT1GXQo4DVCb8iQf-zVvjwTqqmsKScSKIzH-xUSIpCTrpNxzEpFheiH40TDbjHfZZ51JD-10A0ZuAYLhtmtMnHj3DY0U9aWv43oQQvMvwwyt8fICIEJRIGYwBu8JFh-HXUljhiRz1C3nHDpZ6rqDCCZRxYummI5nK5Uy0grl6Cvq6_s6Xcq6ZqXD4vjz_doEqrUGfe02vaB6RPHQFmNEsD08k6ReSuHidREFHyFhIeDldkjsrA655qJROikIqR3nhh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30247" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA2LIj926JayhKk0G7JmtupN733f6K1drSCiOdv3fwIMQgFlvawwqWUwaPtW96a7nYqsmgJbEC7cLN4HDRPKu-8doRnXjvHJ0i1Zd68oa46Z_P7mgKTu5TZUEbrbgAIHIwtO1hQV1BYdFRCRc07S6lAF7YkU-o7Azyi6K9ajrz4T7PpYeTdvUjStp_nEZMQQxlK_vSGoEZUGvRHQk4RMRvsUeQ83tVthBnJ1O9SIMhkS0hW_QnuXKvYUv5C8SnJgsk7arqu6v6dW0-zNy1hlsszLC85V1nPelBCG-qu5Q4g8O-cO09i0-Lm5hwvzyKhacB_QoQFerl1fl2lnCtvcXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g31
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30246" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30244">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fcduz4YIwh0vSVNtbfz4FyfckC5Avqi4sWdzonCXR5Pycu0zhTM6CzSgFZIp2fm_xMe4ZJN3wvedd7GXgzwoO-unGDFlZE4nYsbT3OrMxLHYswo1dj7C3T22iQIEWlBsRtbP-nQTkXSg7Uglke4BLJLlIxLSejzrGWNpHmOgCpDBuG1TCKzKdZSS8nhoK2--HvG4aFr4Zv8KXurD3o47y4OzE-0sjmG0dCV0Xmqd3lzKi38ELyMz4N3_nQb29u6zSOPBvITpLfc8pM128isq8UzNv1rdEX8vT1wlWuyIvm3qjqQlcTxr5azjaMrhePF3C39kjE48-GbuDp-YVbUYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peMdUzxsSRgtI35luBy3UR0yzWP_AMCzvHSdmf8IY2XWZpIm16hTKpyT6dtQRjc28h8vJgdxp4aGkQK5kvrEpDha368g9OG-Ypki7oC0pLHTEhAAKWQUJKHW0BrvC2j2ASk4LkL9ZEtPG59v_0yKgxiTwgbwS_4RdZtwD-qyO25hX0KvvHKsXbS9MIbo82blcRXc2OrYXvTylWk5WVsF-QZQVUQH-iIcovNqDZLn3Q1rUQZe97ZisHULQF8dilHdwQT1PAlfXu_Gkkk0FAtmKiCGF4YMdR4PgYTk0nZ0wf0BnjXeJFiVviK3mQWhPipgbJJ42olysXr-J4_ANd_e0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
برسی عملکرد خیره کننده خط دفاعی استقلال و خط حمله پرسپولیس در این فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30244" target="_blank">📅 18:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30243">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaPiOKHtAqgyxBKJGaHpeuDQgI25WQXIMsJFP5RK63Pl5ozxe0njWNipN8SjAMkWy2z2VXvbyjUSiYm3FzHfe8DoPE1CL803fCNwhEUb_Im7pbcGNR2bbmYqHarpmrFzoahXQbnRRr-e6cBSIgb_HvH35Si_TL-1mlKAfYTLBJflrgK35gbSLTnKeJzL_3mJnTtBv0XWxSTu8KyVcxGhTz3oKWwuOahkB17BuVD7HM-DtDR7egNkCksp_vFZX7T33LS-sa2l3VU_i0STfWpcuz2gV0KAM56j15Qxo28RgFldYy5M6LEoj5kr0cVq_ztj0yflJwvzBAjyuq-zJDuzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30243" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30242">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq8J5Gil3iLMbZfPM3_Gty0q1naQERyECOHVeb8Au-TWNPANgAf1N7BS69f1lKloiwUuYg3287Bsrh_jz7ZikT159dJ2YjMgYj_ax6HnH-b4zRkccGOqLFlLw6OrpqW4fheSMWFZNaqTMP6qMbTH4iOhRKKovEH29JszF6HZOdg4XSRnvH7ynYYOmJB0v_cr-dvvKQyWxQPQcjBimwcNUsAxmq9Oo08SwGYRiaWWQARHD8ZoZEud1CfPlTCuRAO9TEU6zmL4mhHMGNLEK7ZxIj7pTwvWhNWNSl59Bbz5TsulVgyTI-GCM5jwrU7Dbq_pP92G79C49qleVpyHKiuevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه ستاره فرانسوی رئال مادرید رسما داره از تمام تکنیک‌های نامزدهای ریاست جمهوری مملکتمون استفاده می‌کنه برای کسب توپ طلا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30242" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30241">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVWWxWn7QdInZtxmjkAD_fvVI0ojQB5jcJwgAo-t80LKNpMIRCMI7Bshlm814BTIHTGZv5tAt9qKPXz_o1cXUHaX50uM8hiaahL31_mGVzGKqkpTGYyF3WwzR5eA-WtFCD2dpyd-NxW6-Vye3lzjtu0RFU9Z7eJNjjHM2QqIZYdclmOu_dbCtQGQJqZ6vmCpMbFzDvk60rOpiM_o5fydJpTaVlUJTy7rVr5LZfAmDQXq2VVjnKwptcYMrino1XVQ4Y7zjaaLSNyW30q0y7DIZWFuKvuRturqOdhyi7xEc9EQuNK1RdNtAITN0OcKvLhCZneUlj18YvC3L79xXStjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30241" target="_blank">📅 17:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30240">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIG_MHGnIPkOFPokxzeYdPuhy5RWqjYNlzSKS5oR6uPNOD0mjcVWdUwW3b43vr_JUVdOiZhFf76X75ZynQ0t-JabuPwrxk7dQhwFBGBAMvj_XsytDGEYkH3yFlP0_l6mHRDnguO0jX0kiMDidWF5O6lFadlZGm13liIk6sqKQaNX0x2Hr0b24JsK_tCjIF0UpCWWFauVRY7SVgYCLv0nnqLxgVpvTHjXh9h2PbQDTglPWj2Dk-IfN09edAOg0yG4zx3zBlG5fy9l1S7G6XgEaBHsCo12pMkQQRlacNAGma2V-mMPM4-BkAK5I9P1iqx06ZOFjlgM7x3M-7K-Kt9ESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌حضور دریک باشگاه در پنج لیگ معتبر اروپایی: رایان گیگز ستاره سابق منچستر در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30240" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30239">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=S0s2effkQ5DgSPdDBJ78FPL1JdDDFMoVFG9ZnvgJf3ETBlfrVJ1_Aww_AdQh1ntfY640QnwPXMiCK-P8Un6Ag9duqRL2-HlofrBA6PiMQt101XrUt76Sa7WRawAgm8Ddm0hAreykD9MDzYNE1mJh64x17xrDG-f85v8tLdwSX6BvICZ6snwxZ8HdjiGhV7qFpWRmmT_wY1AuOpn4MEBgijRlazs9m4kDbKogV2uibV6AyOLXGi1aHe8UHgJY8KAbgkaSNSVfXLTZtSvHvgXx5bwFpfHuV093UugfQTYXPJLqDa-b70kS2tmHqT526UYOaCxtbAv0kXBEAgW1081C4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=S0s2effkQ5DgSPdDBJ78FPL1JdDDFMoVFG9ZnvgJf3ETBlfrVJ1_Aww_AdQh1ntfY640QnwPXMiCK-P8Un6Ag9duqRL2-HlofrBA6PiMQt101XrUt76Sa7WRawAgm8Ddm0hAreykD9MDzYNE1mJh64x17xrDG-f85v8tLdwSX6BvICZ6snwxZ8HdjiGhV7qFpWRmmT_wY1AuOpn4MEBgijRlazs9m4kDbKogV2uibV6AyOLXGi1aHe8UHgJY8KAbgkaSNSVfXLTZtSvHvgXx5bwFpfHuV093UugfQTYXPJLqDa-b70kS2tmHqT526UYOaCxtbAv0kXBEAgW1081C4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30239" target="_blank">📅 16:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30238">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNdq1j52xafLS8v_Ueo6cwHl_53dWavv4GbbnaaKijwVsj38Cbu-lHolFaoCWsKqZUjRKWxNZUDbhoXNMRxm6ze9v0qjV2PUw6tXm7UPES2EjI1VkFPjrOw6e-Nrr2iTcmFQgE5ykMrOm06M2a-prKVqSLmDr7LFR7yJvBZlSPA1JDxNUu5QowMJLpAz7yJG1dgoTlbu31MmY7WIiJW42EpV52HvCM7_Ge-HAOUOekZSdrj9dI98HNvMQGFfCp9vfVpHnoVBGWhxBRviXw12ULS3ptMgk_tyLAhm75yaAQCSgg6CfANvfXYPgUrCxXU4f55dMq0-dmzTtfJZKyZKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌مارکا: جانشین‌ خوزه‌مورینیو سرمربی فعلی باشگاه رئال‌‌مادرید درآینده یکی‌از دو نفر میکل آرتتا و سسک‌فابرگاس دواسطوره اسپانیا خواهدبود. این فصل خوزه مورینیو برای رئالی ها جام نیاره در پایان فصل قراردادش با کهکشانی‌ها فسخ میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30238" target="_blank">📅 16:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30237">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=lkrgUzQqIzUlyxBjH8VKnEKFR4s16xDrK9JvZ212rfFcTI8NM-xVHkadLn07xtd4YbbL5raIXZozlMH1Be353y_CxVPtFnVwda60ocx3jjNW_DwehK9858khgEZgB48gcXIAqHg2ddJTtDyb1LMQ4FWQFmgdoQ7TYX5D_D3cccqAFQYq1187TIcx567ejWtUafu1MPKloE1BbhvJDKBdZSHqLWwq3fBGqFb5n6vgJMWfVubUOCtZBIOT24pujxLVo3MmsneA3A9vC9iv0xVEHpjybWyosBWsxX9bsg0ikKsMAU7Kf6TvW7dqwQlnmgAce4agIpibeYr3JsVsP_EJSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=lkrgUzQqIzUlyxBjH8VKnEKFR4s16xDrK9JvZ212rfFcTI8NM-xVHkadLn07xtd4YbbL5raIXZozlMH1Be353y_CxVPtFnVwda60ocx3jjNW_DwehK9858khgEZgB48gcXIAqHg2ddJTtDyb1LMQ4FWQFmgdoQ7TYX5D_D3cccqAFQYq1187TIcx567ejWtUafu1MPKloE1BbhvJDKBdZSHqLWwq3fBGqFb5n6vgJMWfVubUOCtZBIOT24pujxLVo3MmsneA3A9vC9iv0xVEHpjybWyosBWsxX9bsg0ikKsMAU7Kf6TvW7dqwQlnmgAce4agIpibeYr3JsVsP_EJSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعریف و تجمید عجیب و غریب علی رضا علیزاده از نوید عاشوری بازیکن تیم گل گهر: اگه زن نمیگرفتم میاوردمش پیش خودم باهم زندگی میکردیم. عادل میگه چرا تموم مهمون های ما اینجوریهه.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30237" target="_blank">📅 15:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30236">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMM9X5svIBxEro4wDmnVZRHtfgfV5i57fw0nwjBpLsnVuboJ9xZSlAxBieBOzrkiZ6Uwn6Qwf-hpNY1fHgzemk5XMqR0Jc4e_vpLM2ShWlbYl8Arodtg7saJ2hwYVi_5f4If045naP0AAE6o35Tmhg9in45VWxA2C5-svul45jsruVih9uA1FVAMah3OM5ukjM4YOlrElvk-IVEQgPNNKqFuOMsU4pTTPgtWsCAPiJ_PmGZuyG3hYjOAAM-3oUa_eLz95PN5ZnMwRB__2HaXYPPMNqns_DwZFtowaNIMrcovmg7hfpnINsPcEF3HqlaL2X5vtdXEcB-W6pHzQIATrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
درشب‌پیروزی پرگل و چهار بر صفر ترابزون اسپور مقابل گالاتاسرای؛ محمد صلاح ستاره مصری ترابزون با ثبت 3 گل و 1 پاس گل یه تنه سه امتیاز ارزشمند این دیدار رو برای تیمش به ارمغان آورد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30236" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30235">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djahWkUhizYEs0ikwsKBxFI_oVK6xlQuMYzBYz5QAg8jxG1EJ6dGG87bxOl6wP7HnELmNGyVdqeifWBAdGjc5eg7NLg_yJnjHwty2RuseOO5mq-NwZ50ROkBZ566YICUSnQrgnD066KfQi2vD-PZ3OPFOXPsKnsLmwGKJY-PZusoaaEAwmr8oGHZ48DGaAbz3E7oG1tg9MDgV41uZ897jZuQ8XkgdDLAaf4ThGQpQnfIFO94PXordikBlUhJb64hbisjmYD-7I0xqydEfwOuzjpSevkRwU2ZurVzcN9rjhU5NPMIDhOYz5RQOYumieduoHrykkaBTymtE2TlPWdihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30235" target="_blank">📅 14:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30234">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=XCiAEkipE1ubX028OKXBfnIa8wtztc0c3qzDXkVhtQhVAHKBfZJ_HG8DHwg4gkhT5Eexa2Wr7Y6kwssSUwW0V5eKQNsWLz8NW-yDQ9Zv5LPTSM4toi8lLN3bqihnKFkSlalPoF4C-x-46fU0bfhZEnzmjyp4f-RtnH2gjRSrgzEjAhKi5T55d2E-fmwxntiIFpJ-YCGa4yiNUI2WZD738jc4CBDYaM8dhWjpulH-m12U3ZoJCRbTQAg1zSRDjziYwa8km4zjxSnQRdR1m5dwknVOioV-xVGp_78EwqJOPrZv3YNe8sGTrgp6r4kofWiE6_-_RPIailgUZ83g8t0Bhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=XCiAEkipE1ubX028OKXBfnIa8wtztc0c3qzDXkVhtQhVAHKBfZJ_HG8DHwg4gkhT5Eexa2Wr7Y6kwssSUwW0V5eKQNsWLz8NW-yDQ9Zv5LPTSM4toi8lLN3bqihnKFkSlalPoF4C-x-46fU0bfhZEnzmjyp4f-RtnH2gjRSrgzEjAhKi5T55d2E-fmwxntiIFpJ-YCGa4yiNUI2WZD738jc4CBDYaM8dhWjpulH-m12U3ZoJCRbTQAg1zSRDjziYwa8km4zjxSnQRdR1m5dwknVOioV-xVGp_78EwqJOPrZv3YNe8sGTrgp6r4kofWiE6_-_RPIailgUZ83g8t0Bhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30234" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30233">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvozabrmc7k2v2vObiQ9O8jJXgcPWOCJi05GWXpT9wVrRChdvO4-NHM64g-Y-VtLXzj6GbAdKVzFb2KAYnRNq5taS9zm6RfUsuR3VFNNnwSlngeIbwpSzivx9IV7qFCTPKFagF0YQW8eL8wKpjFARe4xKA1XqANLITs_x3RlNXKmF2ia_PG4h0xrFLaxRkwfHZtsXkCmwaaKEIgEcIRRQS4LT49m1B-hnbQmeTH-Vkcd5C6cM0vbAoBAYK58j53vQL1j_5LEPOIqkFHI4YsTaz9Qx9EctaIdTK_MVMILJAywU_yJ-VW_ZvqrWeo9P9EGfhiya1Z7oyY61tWSMRoLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
#فکت
؛ آخرین بازیکنی‌که تونست تو یه فصل باپیراهن‌باشگاه‌یوونتوس 20 گل یا بیشتر بزنه کریس رونالدو بود اون این‌کار روتوی‌همه فصل‌هایی که برای یووه بازی کرد انجام داد. از وقتی هم که رفته هییچ بازیکنی دراینمدت نتونسته‌ازمرز 20 گل‌هم رد بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30233" target="_blank">📅 13:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30232">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=JbXsuTskuS2MiTAkfdjpRgOkO0CqXlR72_SmsruloLyjiiT-OCTnagHmUlVaKkcPF1r_JLBcUuuO7TvJdiI866eieg75UK9ttkpWfDKVj5F149X7ONtXfMN62ZYkOelbinJK8IHfpSJfulJE2bPCZQ6I4Ldqn05SIrV4hWIEgr1mio0IgX-s3It6mHqB_Jc7yNR7NJAfpxa-iSa7_Dkk7ZsIwSZ4gB6szk7OzENET_jS8_kfqkFBOQBFrCS3f_woCUSF59Icolb7kfoFrglKzTma-sKgfVdIapvrQSgwHynAqkBr5aWXoIETp-Vr03d7tXNFfrKe724VakqqyByn6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=JbXsuTskuS2MiTAkfdjpRgOkO0CqXlR72_SmsruloLyjiiT-OCTnagHmUlVaKkcPF1r_JLBcUuuO7TvJdiI866eieg75UK9ttkpWfDKVj5F149X7ONtXfMN62ZYkOelbinJK8IHfpSJfulJE2bPCZQ6I4Ldqn05SIrV4hWIEgr1mio0IgX-s3It6mHqB_Jc7yNR7NJAfpxa-iSa7_Dkk7ZsIwSZ4gB6szk7OzENET_jS8_kfqkFBOQBFrCS3f_woCUSF59Icolb7kfoFrglKzTma-sKgfVdIapvrQSgwHynAqkBr5aWXoIETp-Vr03d7tXNFfrKe724VakqqyByn6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30232" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30231">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCstj6LQXj8XYOc4ZFFdqMAWhhQOUz-bcGVxuT6NatPwJQg2m4fKB16TadowK7ZRN8-dnZBovoTlJKt6R8turC-Xze_qEjGQyHqOr5G_ZHsRHc5FCBdXyoqEZuk_31egyENcfzjDp9m8w5kQnRO9kgvdspAOROmTUTff6dsC3sjugci2pdmUQezzIuSSwUSerd6lv4vpHQrPsccEwbjtIvBkYRVnPHvYywyFhdQGff54gm_sYJ0vscjF53bgYxf0UEfp1og50_zRM4-NrhRsrBimyg1UhgfjqAMmXA30hA-JooKsae8VHwLDeJAIrzzfKPYer_QuvfTgEM5QzIHU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منصور عظیمی معاون ورزشی باشگاه تراکتور که ارتباط خوبی باستاره‌های‌ایرانی و خارجی داره بعد از اختلاف بامالک‌تراکتور از این باشگاه جداشد. در طول سه سال‌اخیر عظیمی‌مسئول‌مذاکره با بازیکنان بود و مذاکرات حرفه‌ای او باعث شد که تراکتور ستاره های زیادی در طی این چند فصل جذب کنه. هر باشگاهی عظیمی رواستخدام‌کنه از همین حالا نقل و انتقالات نیم فصل اول رقابت‌های لیگ برتر رو برده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30231" target="_blank">📅 12:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30230">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npHZdyoQ8_P_Ai6ZRAmjiO6o3BG_O03ClWuFyByihBccGENNeoZ9jHPtTHydxaNArXE4Y0bENpIGS6M_s2ehmQ_zQfsXjzFdd3tLpjQfsrOm3z2rtot7XZN4ZQWOVCV4jIPBAO1Sed1XrMJRFi3MI0uOHmJpkeGVsTwo_iabZKu9gn-b2nvQX1NqsGyTD3zBwoWOv2mwsNKQq1XCMKJrp-5GuB26f5KPJWB6EnhnFdc1flwqnvgW1OcaJYoFXlzjf6nOSx0x9eyEzekMlEqjQ15mN8nq1dO5BJbc0P6TQMAtR-YL6fdwPfJwM2cGIpodgiakL6_BE_WSUmgBZ0g6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30230" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30229">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول‌برنامه‌جدید و فان ابوطالب حسینی برای‌حواشی‌فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30229" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30228">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: توپ‌طلافوتبال به بهترین بازیکن دنیا داده میشه نه‌اینکه‌بدن به بازیکنی که فقط 80 گل‌ زده چون که برای‌گلزنی جایزه آقای گلی رو میدن. اینا خیلی‌ متفاوته! بهترین بازیکن جهان کسی هستش که وقتی به عنوان گزارشگر یا تماشاگر بازی رو بخاطرش میبینی لذت‌میبری…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30228" target="_blank">📅 11:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30227">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9EqBMB9Hg-SmElbi7n3R0Ceqhucwz1Mw4rIGSGCdZq1F3lE0bnUtS8J8AOZc58GB7aPqtdl_7HnRwrPgzoRw-HxWp2QIja5geGHiBEDs4IaozYT7QBhg_pUqXvvRjU1_8XMmhkumQ-zPAUjq_SNm5wiL2XRoJ1sOyt2yKWB0-pExkpxNNqTj0z9akwCNA_e1xE93KffMi2jlqSxu7PZqzQAfx66rENKlr3ZZKXYZXoEJ3cscG_Vzjw5qX6MtSrLtK-eu3pfguY1ZR9zSlyztrrUOK9Und-59HP11VPtm7cmvXn-yCd8DnHNpFRGRGGJ1SRL1-OEBa4Vcm9m5bxY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
مسی درتعقیب‌رکوردی تاریخی؛ لیونل مسی حالا تعدادگل‌هایش‌از روی‌ضربات ایستگاهی را به ۷۵ گل رسانده و تنها ۳ گل با مارسلینیو کاریوکا، برترین گلزن تاریخ فوتبال از روی ضربه آزاد، فاصله دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30227" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30226">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇫🇷
ویدیویی از اولین تمرین تیم ملی فرانسه بعد از جام جهانی 2026 تحت هدایت زین الدیت زیدان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30226" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30225">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=uD0Le2vWVLOONgX5ED-2tbjWJxkyFQz6O5K8QDJjtAcNNjjKbMgyZ8LmHCx7NQMTFonRseBLAB6ZVaKS2jEOReKAWL27FbzO2ySssLXz9ANgdSRV02K3mSVl_AtpEcVHLkumYRL4mxrZ5MNfe3Y5wS9XckD37xfmMAMfoHtp6YI8XPWlQq8LvCZxPOcwwUGjFzl2F1MSpmkddwyj6ChZrjibSWUat7fO9m4jJEiS3d0QiQZee6ajcxTgNGcqa9pQ8DuiVOCKEmqRhPWQXnN5LI5kzKHvgzPLisd3_PP66mVcKAHg9vHnh2mHg-01bb6CPOS-fqQqwxfnaV5vng0oPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=uD0Le2vWVLOONgX5ED-2tbjWJxkyFQz6O5K8QDJjtAcNNjjKbMgyZ8LmHCx7NQMTFonRseBLAB6ZVaKS2jEOReKAWL27FbzO2ySssLXz9ANgdSRV02K3mSVl_AtpEcVHLkumYRL4mxrZ5MNfe3Y5wS9XckD37xfmMAMfoHtp6YI8XPWlQq8LvCZxPOcwwUGjFzl2F1MSpmkddwyj6ChZrjibSWUat7fO9m4jJEiS3d0QiQZee6ajcxTgNGcqa9pQ8DuiVOCKEmqRhPWQXnN5LI5kzKHvgzPLisd3_PP66mVcKAHg9vHnh2mHg-01bb6CPOS-fqQqwxfnaV5vng0oPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده:
من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30225" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30223">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619db5893c.mp4?token=WvkUF6iWnHj3Lq3SJIK0nbZyRCmugEBQq4ftgLXTUT8RqWZHln-sB5ol_NJa78IqZf9OU2CB6QwLyisCsXEKSrMYBSDOHksgk2oYfVWYXdX5YFLxW1EGO55rKuIGzZyXrIozp8uaVoSBBbwODStprCwl9pmJWku8z5A2J2ltMswUnh-2Fx25Iqandyx_mfHchjC3gNvmgX0RNl6UEjpmOzksZp_QPHI_7OfCbw4W6HO1fuPW9_nNrpsvw554R3im1xwpXySB-d8D5J95sx0MfPtqzwePQLUf8htbEZXzL-VAKptD4NqI-wvkfBEVLws5UqTXBRFLinvnjcvyixH1Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619db5893c.mp4?token=WvkUF6iWnHj3Lq3SJIK0nbZyRCmugEBQq4ftgLXTUT8RqWZHln-sB5ol_NJa78IqZf9OU2CB6QwLyisCsXEKSrMYBSDOHksgk2oYfVWYXdX5YFLxW1EGO55rKuIGzZyXrIozp8uaVoSBBbwODStprCwl9pmJWku8z5A2J2ltMswUnh-2Fx25Iqandyx_mfHchjC3gNvmgX0RNl6UEjpmOzksZp_QPHI_7OfCbw4W6HO1fuPW9_nNrpsvw554R3im1xwpXySB-d8D5J95sx0MfPtqzwePQLUf8htbEZXzL-VAKptD4NqI-wvkfBEVLws5UqTXBRFLinvnjcvyixH1Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد ضیا مجری‌سابق‌صداوسیما که بعدِ اتفاقات 1401 از این سازمان اومد بیرون درباره خداداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30223" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30222">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=fne_Am14G5EFkK_9eqK7ama5rwqsPyfXQfTrWwkHcPukqruWuaMF8iJdnvQ_UV9rIo1BSlvnLCmy18VvLpkyFq33d_lvFmlYQwO3YHRwOBK0oOJxjV22lqy1X3IF5sOEiXSS3pT4LMM1HbuoHJaUxv926mRt9uNONJd5Mo6AHKcn7fObOSHBKppMVUUrJ7JCqnIOvroKZafIali5QZgh8connL_k717Aonn7XKQqpJ6bozmbY2ViFeox6ALiVR7Lmj4ZYV9FgkSLtCiG5CceDqK6FAJ4U1iSf_LLaMBtpqfRz4P6xcupEBGuSxg4RoLk6nh_wG3CoOEAEsJMo0MHdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=fne_Am14G5EFkK_9eqK7ama5rwqsPyfXQfTrWwkHcPukqruWuaMF8iJdnvQ_UV9rIo1BSlvnLCmy18VvLpkyFq33d_lvFmlYQwO3YHRwOBK0oOJxjV22lqy1X3IF5sOEiXSS3pT4LMM1HbuoHJaUxv926mRt9uNONJd5Mo6AHKcn7fObOSHBKppMVUUrJ7JCqnIOvroKZafIali5QZgh8connL_k717Aonn7XKQqpJ6bozmbY2ViFeox6ALiVR7Lmj4ZYV9FgkSLtCiG5CceDqK6FAJ4U1iSf_LLaMBtpqfRz4P6xcupEBGuSxg4RoLk6nh_wG3CoOEAEsJMo0MHdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس‌سنگین‌ابوطالب به خدادادعزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30222" target="_blank">📅 10:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30221">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6pjw86vtBqaGTndz1hNZc-zr5MBieCQun2KqnVp67gJWEKC5zT7pUWWdi4zFcMIXHymSjfZB4VisAQ9UDi-eRaaGIugEHZLmG4iEhAtlIzB3Gsj1D_grQLK-UyhRmud0g9846hbdCx9buCRr9lo-djxrEbYkZNxwlfpSNqLrWXwZbmlQCPHTLmecxvjHkCSOgXFdyGlRT9FFJedsK-LPe9FHh7pd4-znpy5DWjVZtPEU0nO7RgCxZK9lgiogkJvRiJyVIBDLUQpQET6cTUNOyY8kM8lFJ1sVRyvIeQWF2Dm4arqWMzAhd_yXoygPSgoQeDYf43lBRxEGKQTURhLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از علیرضا بیرانوند در روزهای آینده در سالن تتو کارها. این‌بشر شده کل بدنش رو تتو میکنه مثل بدن امیر تتلو تا بالاخره معافیت رو بگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30221" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30220">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkknj9CShvcClwni_SDi8cWwHzIJ3lJLlr_qrPNs5zwNnaOrsmiVoziq0oWEQdXBR_PYQUYiije3yjlbS42f0sfNqyj8Ei2waC6CDOIbhYpqOISXIdI2lD1ID8Xsv3Qq7IyriPAvVL0sqxGufwVM1THRGQm5rmvDS3UVsuR08KQfqyiFfyK02NElpTIIr4qlKtqKS20A2FBarEIX1Yn04rTOKbW06yB5RCAW1OO7QYZzAI7A8TnVRIu4iK_8OrH8BUaxeN2WOVi8y0uGeogFlzg2KZQC2TcYEoqDMBov9ftd_0JjIkgIozzN-HXvAtiPMJi1-o3_GgBJ0BL1XhXgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری مدیربرنامه‌های یاسر آسانی در تایید خبر ظهرامروزپرشیانا: همیشه به‌آبی وفادار خواهیم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30220" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30219">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=o7pCO2u3YLhdSaBrSvNL7G-1RGZ6TabXPuvZAG4ODJO4sZuNBDd3RI7BqR5WLwgdT3T-ufMAuim6mhsABrhF-RcPlfYBXyfWTVMtdCOt4wdqgZFjquSeYTP5ZaKAyKdl3k9H4dX8aGO39p5RHKFvR3Jy2KNq3esFe415SHwyTqwkJNhS4GGOS6LucxbagCamz6hY-YTkpTrLQ4Ep09oh3M6_EjcU9hZ05VFvwopUGQlK5tnCDRftZVOICTPGJCDmVnruvNZSTowlkwEjp_AM5WxMQjc_qgakjk4jx7ZrM5dbfk-jooKzkGzbea-56KzWFjjWpCzDYItWFliFxXObmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=o7pCO2u3YLhdSaBrSvNL7G-1RGZ6TabXPuvZAG4ODJO4sZuNBDd3RI7BqR5WLwgdT3T-ufMAuim6mhsABrhF-RcPlfYBXyfWTVMtdCOt4wdqgZFjquSeYTP5ZaKAyKdl3k9H4dX8aGO39p5RHKFvR3Jy2KNq3esFe415SHwyTqwkJNhS4GGOS6LucxbagCamz6hY-YTkpTrLQ4Ep09oh3M6_EjcU9hZ05VFvwopUGQlK5tnCDRftZVOICTPGJCDmVnruvNZSTowlkwEjp_AM5WxMQjc_qgakjk4jx7ZrM5dbfk-jooKzkGzbea-56KzWFjjWpCzDYItWFliFxXObmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی‌هوش‌مصنوعی‌از قهرمان فصل گذشته لیگ برتر؛ رقابت بین دو تیم تراکتور
🆚
استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/30219" target="_blank">📅 01:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30218">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwGeqn-wv78a2L9mlPSrbHu5oS6t0EwdYyge2bW-TzZ_BHH9gGT1iOOviy2PUt7g-BBaTBE76uQsnvtXjRMyopGgppy6Mqomf7tiompJ0AJ5zeFLbOWyzLSwuR57XOOvypI41X5ewwheDMJERJO1pv0UO0OvN81X2dE7Jkl-qgsMm5-1lYbg4imve2GgauU1CrNz5uom3r1JM65t5oN3zxhPu_L5BfgJpx2kFGCAg3M8sD1I1jv3I7LvVGKdz-12WcbYuOCfswrkJq34BHE6DOjGLQJD1B2AYrrY3fxo5UywdTZg7_ym3tLmxxSSZd9oyvPtmWuCMfkOOJ18vn6LfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/30218" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30217">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPVYWF5o8fBBKKOA5h6R55ahH1MSIuCbWPBKDp6-1ZftDNzcNhoMGgOK79vfRYuzOUiOlqqGaJXYXP4p5hrBdTiHWD3-wG9qX0wYuTM3_04BVSQK74tm84TrGYrXJxAt0RGJEy3gwPrd0q3SFjQLJwi4f5xumxYHYRNQT3eKgw6EKC23cVkVVyAWDuHLnG4aGaT4sMb9VhQfG1pA9V1p2y82rtaU5iRdj3ukb5rvblBMQQhshkkkJNX0q8lVE8t-TqYxaFPBi_l757ldoYa43bLukPMNyg3LYolzkC6qiU6zSrtr3SIYmH17oXxACSYNLoVsTxKzd-UW57jefqUI0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها: رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30217" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30215">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30215" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30214">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=sY0nb_giUcX3tzuaFkGMM2MavKX7BIK4iTG5lzdqPU0Ms5sJ5e82N2xhCb6MYBW0dlPbSp8g0reIBiowrNmKRrXeZBW2-_1zM9xYzPsH4EA8UuxjsM9-o584Nm37Vc82JJT0SwhtcTFThmWdsc0CQ31BEd9sJoiRyNdQpavWVIZlz2ZfhA9quFPwx4QEhkcVAgA3TQ1P-TBoCbpPzXN3tKdSp_m6t16ROEI2OH7nVfq2ZNmnBayII5jJKHts0nNJ1p-jIRSsNL_CMKHItPNy2w0NSplTvZDFfVxQ9w9ssyzxIIHzoRtJvnWSkUWsxh2q2Kdx8898QUqxLbaL5-DEXxC60XpR3RYVPLpk6k8Z6NZ2Cc9IoYmDrJu-Q0QJmsDEwBpcCI7HtZzi8PdQyHjsh0ik3APoO4PRtHJFRdkA6pytniNiXnQ-77yHYdcYJDIqoT5W-8452fMIUkOWWnLDFYXFYjSFD2G1XEMx7MeRqMJcZJzhF2BQcG2QbGC97LYgECGkWh14phnRzS_HBWEKQJQgE8gVwAMSU6AR3np1EevcCLwE-rPEGxv24Z696iQBGFoKh2J7tRIX3PRpm33Ld88DGqxudeHB2LfGnHU8-Xy_ysijBMN1THJV8_cgLA-GiEY24pNwFRV56cZCH0Dl_-8gjDvtiwwFBOTX5c_NNuE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=sY0nb_giUcX3tzuaFkGMM2MavKX7BIK4iTG5lzdqPU0Ms5sJ5e82N2xhCb6MYBW0dlPbSp8g0reIBiowrNmKRrXeZBW2-_1zM9xYzPsH4EA8UuxjsM9-o584Nm37Vc82JJT0SwhtcTFThmWdsc0CQ31BEd9sJoiRyNdQpavWVIZlz2ZfhA9quFPwx4QEhkcVAgA3TQ1P-TBoCbpPzXN3tKdSp_m6t16ROEI2OH7nVfq2ZNmnBayII5jJKHts0nNJ1p-jIRSsNL_CMKHItPNy2w0NSplTvZDFfVxQ9w9ssyzxIIHzoRtJvnWSkUWsxh2q2Kdx8898QUqxLbaL5-DEXxC60XpR3RYVPLpk6k8Z6NZ2Cc9IoYmDrJu-Q0QJmsDEwBpcCI7HtZzi8PdQyHjsh0ik3APoO4PRtHJFRdkA6pytniNiXnQ-77yHYdcYJDIqoT5W-8452fMIUkOWWnLDFYXFYjSFD2G1XEMx7MeRqMJcZJzhF2BQcG2QbGC97LYgECGkWh14phnRzS_HBWEKQJQgE8gVwAMSU6AR3np1EevcCLwE-rPEGxv24Z696iQBGFoKh2J7tRIX3PRpm33Ld88DGqxudeHB2LfGnHU8-Xy_ysijBMN1THJV8_cgLA-GiEY24pNwFRV56cZCH0Dl_-8gjDvtiwwFBOTX5c_NNuE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منفجرشدن عادل از حرف پوریا پورعلی؛ عادل پرسید مهدی زارع تو حموم چرا اونجوری شد پوریا گفت من و مهدی باهم بودیم که اونجوری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30214" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30213">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERd6XHwCIwxUk1eIF8Ubwo0-9Oopui7YgdnvaPN9lUb9P2i3P2yThlEKGO-9GauKudG0ZV0fjV8c0AEuJ-B-VtOpzvtSF2HOuBjL88cTI6YZ9U-b9SpK6q4DmAcAcdObWl-eer4qqn66eVeFbzg7UauDoHuNdKYoNPa-z9hMZKLVjvvmy3sTOzIDpFwsPxEKQz5Us2gWwRRZKSz3UCPykFrh7zZOQ3-dXNw7yCc9WJDuV2WhtB-_8ZxPH3FXLW0_8XaHUlcg98iafIH0ERXBzb2Scm9-nYwafGZoelvmZWXHF6AeBMD3dPWtzbad5TmCyDW_spJALZE1_pwthYQMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30213" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30212">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM6dx6RLObiWdXzcwyrnNzfFeo9ZQNoGkHGnNcrx4Gwogt9LzMeTwzDdvKmktGCEDok1Zsie1cNjJRyzU4e1P6M8hwNo1QlgWI-pZQs9ARbcwUTCOEggJ6tIyAUHvL_tfmpj8LFXIaKo_RvWRyTog6pudHL5619slrnG2DJWReXKvKkbVMmX0xSD1cx9HGlxzYIGWl6JBedbD478DLA4BAivYNuOydIKV9D4gdz-4ZfoyEs_7qlI0AvdEAWysNG2W-PuHsgJZ3tc9Z04vJjkk0yzc5CUvzAmrpHDkXFABn5eNj4_mkmP1MkOcK23QXeNJHM9cfkggUfCCHv6qI0CBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/30212" target="_blank">📅 23:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30211">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TItMOjYvkkXwmtn8gG2ZgACwsj0QRZC3dZ6Yz6kppvfehCadX4IRak26voFqpuABdNJjPtWM0o2uGCaSpywoZhOBPAgTccbXxECadzD29ihMoFR_SVq99fC_JwlfvTRD8aCIJFGTRsnA0eBkzixqy78-YfqP1QKcDfgSA9wPD8yJ90MWAQswaWNMuIk_-I0BWhw5p1oEyrL9Km4jHxJuUacVAsgxaUGJI_b3WVZSxMg7Efsyeis0wCNVSZpcYF4O0j0h2GR5f-5kNNT8RZRPkajk7kIgDFQ3isM5hXerm-yhsl9PQocCG6yhjLYAOqtMZTxvEeKBLOk-RvhGe90tNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/30211" target="_blank">📅 23:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30210">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=q77Ih1VHBImSC9Tq9JXb38G-M4zBt_itzB9V3O7hREh7OdT4k0IWm5fj64G8n1kwM0htMyhxUKWe9-7AkT-InEixYrqeJFO67oDpuiIGInFNzzKDJcXxhTg4e3Zwxew1_IIfnBWD1Bw5RzjTcBV0pnc93KRlzl3Ka_vDINnwfQ_F9Vjs3dRNl6hzOXqmNFvbok4mIJdd6s8_HvbyYyx68qKykVRaLHurfngDZmwKTDvF4x1om3OsKFDQVNgVcVbcdpZST2T-GfLLi6Z8TQjNUznZyOe5H00acYYO8I4bCmgdwB3ZC3BhmLytAUj8EHYUIh2ACjWOEFwVBvrXS5rPcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=q77Ih1VHBImSC9Tq9JXb38G-M4zBt_itzB9V3O7hREh7OdT4k0IWm5fj64G8n1kwM0htMyhxUKWe9-7AkT-InEixYrqeJFO67oDpuiIGInFNzzKDJcXxhTg4e3Zwxew1_IIfnBWD1Bw5RzjTcBV0pnc93KRlzl3Ka_vDINnwfQ_F9Vjs3dRNl6hzOXqmNFvbok4mIJdd6s8_HvbyYyx68qKykVRaLHurfngDZmwKTDvF4x1om3OsKFDQVNgVcVbcdpZST2T-GfLLi6Z8TQjNUznZyOe5H00acYYO8I4bCmgdwB3ZC3BhmLytAUj8EHYUIh2ACjWOEFwVBvrXS5rPcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/30210" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30209">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=UVMcrytr_O-wtoeN79jsY1pVdLa_vIqt2_lbaNFTZaSSCcZPnhbhMELaSVRMw5mnxbHt1yrgy1qLjAaOAzKzwD55EMllMgXYqKv00MwnJOk00vcLAVmpTdiK_eoCcLzBgAaflCpPEYlwXIaDrZYYf4eERf1f8SefXDIL4lRqgJ4yeRW3JC8EDui-1Ru28mSFDmk5RGuFA9bsfuidGWit70caYArKVyTU1qNURriaz5OypPUUhr32MuHHehRDmxTUik5C265McrvvaTrJHOsE9OXiZvzXqiblTwCaiMRDwDxQf-fmiP6y1hhc0Hzjj5zO9233Bbmi14z1KeA_fRgn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=UVMcrytr_O-wtoeN79jsY1pVdLa_vIqt2_lbaNFTZaSSCcZPnhbhMELaSVRMw5mnxbHt1yrgy1qLjAaOAzKzwD55EMllMgXYqKv00MwnJOk00vcLAVmpTdiK_eoCcLzBgAaflCpPEYlwXIaDrZYYf4eERf1f8SefXDIL4lRqgJ4yeRW3JC8EDui-1Ru28mSFDmk5RGuFA9bsfuidGWit70caYArKVyTU1qNURriaz5OypPUUhr32MuHHehRDmxTUik5C265McrvvaTrJHOsE9OXiZvzXqiblTwCaiMRDwDxQf-fmiP6y1hhc0Hzjj5zO9233Bbmi14z1KeA_fRgn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌جالب‌عادل‌فردوسی‌پور به برگزاری دیدار دوستانه شاگردان امیر قلعه نویی مقابل ازبکستان: دیگه پدرمون درومد ازبس با این تیم بازی کردیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/30209" target="_blank">📅 22:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30208">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb7BX1sVGBuvXMTmTgmtjO8c3oyHdxvWwOAOfT12n-5WalGCKS6Wki7MzgOIWfqPNt2PCdy7ZlrF6NKu-3IRUs4SXreuxDigGSGBwEqH8ZTiFmn-Rc5e9WTT-DmbqDeSft0ITpZQswJU0nlbWHDys10_tCZDI29MFUbYsMsOrWuVnONlXBDQP3kXaRhjHw-qkzBQX8L7MIyf0FxTVKNfQGSMsxfQwrN1oeI8BddjNbmhI7x2160FvZ89blDJPFmhYM_nhB_L-WcC4_fxKV3vngG5uwxzJKRcpdvmrXJaDc8-Rz3hgX481pdqPhQ1cU8NU8Y0WkstUp1X3xkrOIGH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال2022دورتموند هالند رو داد منچسترسیتی سال‌بعد منچسترسیتی‌قهرمان UCL شد. سال 2023 دورتموند جودبلینگهام روداد رئال‌مادرید سال بعدش قهرمان UCL شدند. سال 2026 دورتموند آدیمی رو داد به بارسا، یاران فلیک قهرمان UCL میشن؟
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30208" target="_blank">📅 21:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30207">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfLi-lSmQM7mAfINgNyPzfcNSPmSJsLkES6xXL7eiN5x1spzlZ3xpjTCZKlRM6BGTaVwSlsbbzAb2dcssUbsseQPKGPaiCJuBAMM7tk2rER-xyU3cqKJJVpZN3ixIRb-98hkROYwyVE9bNUhlUADQfyYeuOJHy5ve3ps80ZHdZATLqqRz-QdrlA_ZGZtdIMgDtMCLEdMQMCnT6h5f1ecf5k8pCbXNqldeoFI2W2EvfvVbLOIVwFIb7--SOau9wyy0LKIlMFjc43CdDNrEU60La0cCB1ieTxnU2Y1rHCeHevJhwCwHV_k2uRS9Gk9K-ghY3KlHwGfSGaAnJN5q9co7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/30207" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30205">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KF7goVgrq-3jtazONGv6D-t5CPxwnpHiYkzYR5wN3JP3WD58Xdg9jeSlxWAx_LY_J9ySpHJrAp-PBUmwjG_0FNN25Epi3NychRuIOKw8bYN4wAr7dJK3q3WEUntkakGPcOmyHqCLfXSR69YWCC4FKiKj6vdIwF_0Y0M4HO6iP78APfGJ3FjQleEuATwrgYSegTud1KhtKYTsuznHwl9g6Htm3rQ155-I4yVjc28BVQxj4r6Wv3U4U34jtHZVRN616tBeq_rc3WoVzWRgRMYm8pK9S23ntIpqF7ukNjsVqqu-1wel8IH7BKH1ghjCKOYSfU3j5Bu4Ty1fQ4x2kIXXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gN-UxVMaN_o0HdjYyQnRd6sSi_CTiqIEHP-w1t0EWIPeVtxHJypLGWKCmbroJdEDB9fSdKRl2wzKn2Mo_zSiY44BAO0xeP3b4IAAcJfRJkgGFEIUieeeSN9Ev9Cpm7bSY_98_FOXHEg-JLvStqinNr9zDyG35lQNKD53eXAMV043BfHadYyAzKNFq-ILIrQmPO_NzNXYqxZo4HKuHEsz1GczwJ4LmKXbdGohXUzzi-A7CCWdJXVgqKked-2wZKHirIw-jhWjSVc8T9pcpAWDEiS_-PIKFeFNfekIQl9sdNK0XZOjMxuLrHMei2L-N-wp_cbnRXpW5WJfz1FJdIFmGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج بازیکن برتر لالیگا و لیگ جزیره در فصل جدید تا پایان این‌ هفته از نگاه سوفا اسکور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30205" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30204">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVTQ059LgzDic_HrJfkufKZUgVovx0b7Xm0c979lERl5BxZ-YUnlnULhKVIeAmMiayZu5tM7pSrR8bXXE0uZAfZPfqLgxUs9WaORVpGIGjU4hRbL9rHjq16EGOfGdnVMdEVb7sZonAelr7A9WQ3D4nyZ1y4ysyW1gY_mpeqRbH-nWkgbv7rSdqxDnpaI9S3i1W6tOF_gwxWju3e4KxTiEIrtT7Wkt4x4ezvcEUMP3B4Uh00pP6v2Du9OGznFXkbHduu3aj6m8wPgx6aLRqiTXW197KXW2hsNBJ3dO-NVjm3RzhQhnCTMi1BWAQMHzUJq896nL4Lfhr_34puo5sXEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشود عربستان‌ سعودی و چند کشور خاور میانه‌ در آستانه‌ شروع رقابت‌های جام ملت های آسیا بافشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30204" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30203">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=O6Z6Gswqb9cm85Sym4azlaa4tP5ipJD3IR1Fh7fr75GkIjbyRb30nXml4DOykQqjk-xYnfcRXAccQDDjvO5ECjw61jceB16LD9NjrPiJfPlan-ts2QGXNS8bQiEsGAdd1e9LnJlQFK1ZcPNMvVj3D5_EffJwnddDBajSqsyo9gWXq4YnSZocOFHGxjq6-55JH6tvElySm5Ki29M4d42NMe-lkwdpY7aRmX-TsjONyJ6yTrotHMlh4qfBKYkEynD2KlBGPX3hBVlhNCfCGySXYEhlXFwuRZTEspW_XxEW8-UECbhsR_y4gedN8czyPqo032LcG6JCZP7tnJMRsrW6XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=O6Z6Gswqb9cm85Sym4azlaa4tP5ipJD3IR1Fh7fr75GkIjbyRb30nXml4DOykQqjk-xYnfcRXAccQDDjvO5ECjw61jceB16LD9NjrPiJfPlan-ts2QGXNS8bQiEsGAdd1e9LnJlQFK1ZcPNMvVj3D5_EffJwnddDBajSqsyo9gWXq4YnSZocOFHGxjq6-55JH6tvElySm5Ki29M4d42NMe-lkwdpY7aRmX-TsjONyJ6yTrotHMlh4qfBKYkEynD2KlBGPX3hBVlhNCfCGySXYEhlXFwuRZTEspW_XxEW8-UECbhsR_y4gedN8czyPqo032LcG6JCZP7tnJMRsrW6XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30203" target="_blank">📅 20:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30202">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=Nvb6ek5wDXZi3egS0oIFO6TDgp9_Z33fQOtMSCdsdcvbcCcWYeZrGlfbgVmamWiGiZR-8mRdaQ3CoXzbDvE85fZpUh94mcJtLww9TIpDGYZ9VmRyJ1g6OQvAT1WUuIMNC64r3-QxOtTtCZwjKX766gaKHJufO-lrNIn1OzeFPl3CDY-yFDTVb4--ky7NsWfxHsOpRu3EtY1xCNSC3qsSaVztcnX7-ngpgBKvWvZ4HCuxLNdmH1ibiD8pOgxn2ipoVjUqB2YCg5OKTtz4utPtvvE3SS8igGcoL8GXXtrzjJQGCeDpymMCE0FCHg2xq6wZUSwc_UfJS1Di2w7Z1H6_jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=Nvb6ek5wDXZi3egS0oIFO6TDgp9_Z33fQOtMSCdsdcvbcCcWYeZrGlfbgVmamWiGiZR-8mRdaQ3CoXzbDvE85fZpUh94mcJtLww9TIpDGYZ9VmRyJ1g6OQvAT1WUuIMNC64r3-QxOtTtCZwjKX766gaKHJufO-lrNIn1OzeFPl3CDY-yFDTVb4--ky7NsWfxHsOpRu3EtY1xCNSC3qsSaVztcnX7-ngpgBKvWvZ4HCuxLNdmH1ibiD8pOgxn2ipoVjUqB2YCg5OKTtz4utPtvvE3SS8igGcoL8GXXtrzjJQGCeDpymMCE0FCHg2xq6wZUSwc_UfJS1Di2w7Z1H6_jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30202" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30200">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1ObW9rcs3LQyd1IhLFVUVzcNDN6ycB73Tsm4UVFFPyPFHVzui4DBzeh2tL3gahTicJKkFnU3BIjuNpYfjQTB6TUj_9Rxx6-uGDvY4NBHj8pd8FimPZluEBRWDmpHhp5prmVI70JFB8OSQaW-KsZjs9IB8wh52XV2KJQerWVBYkM2Pi-Iii6BD6-qRktHmjIkgikttmF-bCGJ6BUDwsaVyA6rDYM4gLPQ50dbTSlkWhRIpTUuEHj2GAKdHSNCN_q0JS_wT-ZqhWv9cf5KLCZpqW10h0hz834pVAzoY4LC1VdUVp5ko6u8rhzcfkBQrEZaqP_R00Jx157sRdwfKHxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Inv8BY0HmCDwjSPvOMEHPJvC_uocMwlHddFesxuJ4IjtjVovu82IrTzBUJyNJulYQO7FzVTdux7lv9pXMqHcjs-0io6fMZ7JFQmrLJbILew993LgChpNolP_SHNubiduJez5iRc-4DFi2UEAUD0TlxbW0GnTDFJQLUPjjUwr2UhZfB5JmDzah71OhGWP1f31xsNtjO8mhh-OdHUCNXarQYhRI6ZVCv9zb8ukep_tTDX5LPPcrIkSPmP_nTIcm52LGZmv79gblLTqqadaU-RqORdTuvVL491_ejonvKf7XdPd6fuu3_H1ZnLf3dlkKOtg43cSn8QRO_GdFcS0ZKh9HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
تعداد خیلی‌زیادی‌از هواداران منچستریونایتد از مدیریت و کادر فنی شیاطین سرخ خواسته اند که در نیم فصل کریس رونالدو رو به این تیم برگردونند. قرارداد 2.5 ساله با CR7 و خدافظی از دنیای فوتبال باپیراهن‌ منچستر یونایتد رویای هواداران این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30200" target="_blank">📅 19:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30199">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAgV3MIE-_Eacrk7MGyyFurkiVuFUlYsxe32DPf5bVbxXFimIGyG6-m2ADpoZkND2olNyVsGv4HTr2vivYCCOzQJATruoFp5GyikTUqYkHdNYtLc0aBynWUIRaTJePRkcrl3cYuDhu65-ibop7uysWA76DErO44cAQlYGUUvgIcEiRxhtZBo_4wY4QXlgDBRNRkdcCyxa97tJW0YyS1rs5aOWmFMbWt_DMH0UMRyiKG3WAu9IpAZ3h0zUMN-D0qV2pJEo2fn29YjVXHyf2x8xhV43tOzlOelicn4vXhByYD3N9E0_-iUdW4D90ky5X3WvIfNYwZ2pa_FjYK4pisoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قهرمانان10سال‌اخیر تمام لیگ معتبر اروپا؛ پاری سن ژرمن و بایرن رکورد قهرمانی در لیگ‌هاشون‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30199" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30198">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEeBNx7uNM2oGLdoIRkASqSZq1SBa8OMiQjjNczHvl-NTagZsvLcOYh4ENHy5xg7KQvW-7QYGDSHxLLDyQ6wZuQLidUwsXGT3aDDAeR_467S3eJSpp_zEuPqIg2KF1SmIb8oBybxsH0gXS_GWR7ROfeRcqYKsYELR7e2JlBO0L-PnV_JxZMNxrsSiMZSW4SKvJfMToF4DYx6arpSeRri4u6QRk6DzwIPBDPxOUD69chP8lSnTDz8KnTp-J9A9J_DLv9UVaN_JBWOo_Sw7pwW8AaHPl7c8rIfio7v2xs_7vbiQWW9HoTT4CUKKeqj_1iMXTQT5o1lyuU06Qh0xPI-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30198" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30196">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IXkzwEx5ni6QuU29k116kYR2O6h8m3b0el09VoZ0MVOCRFhpK9MF8eXypOIkIQRluq77pU-sK87s-zz22qVTPbuFRbZ_D6DXu-XeUZlD_M6MTIAR1aqJCNzWwJ9jwYsBAFiXAIJoAGXp7jC9V0ao0_Wn23UA1Qs-LVVOiDSMGZ_2jVQRDSFlE3REcQy-cyOGGEAtIH8-0TfHNDs7nZeKFJsp475J2LiW-abrRrMMLUB1uAPLW488-HR4Z5PZmNjAWi0isFn7iVLcNp5xOJsnpufl3UmmdraIpVRMW6rrnIY4tQ-QaC2X6kL2WtepMsE6_teUZ3yMjed5LbGSDq_sNFIKHJVDaX5Z-daGAXlxfX8yUlVBQfFuY_AEATdgQVMRROIabTOYjPP-fFkU_UQJJkQ3gfRmCaSghLcDK3HbLy89I2yHg23UMZyjUNcytSRxdErgdr3A88_hmFBR4s13kJVIbh1rGn9MQLECHInpyReU24JBAMRSUsrvODrbYDLvEEdJUT8ilwwr4ozppQpzUieeV0tdd4zSL2qpI6cwJ-UloiLIoJjr3oWVD2ErU-E6R_frUPgGx5envdaU4NENCJxEZWmyRQGQkOdL2rY-u0eKKBz3hXdibtWjHEYuQ27K7T4Z5YRggwF47lAmPY5pfDJYpc0gu9e5HIFltzXyTZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IXkzwEx5ni6QuU29k116kYR2O6h8m3b0el09VoZ0MVOCRFhpK9MF8eXypOIkIQRluq77pU-sK87s-zz22qVTPbuFRbZ_D6DXu-XeUZlD_M6MTIAR1aqJCNzWwJ9jwYsBAFiXAIJoAGXp7jC9V0ao0_Wn23UA1Qs-LVVOiDSMGZ_2jVQRDSFlE3REcQy-cyOGGEAtIH8-0TfHNDs7nZeKFJsp475J2LiW-abrRrMMLUB1uAPLW488-HR4Z5PZmNjAWi0isFn7iVLcNp5xOJsnpufl3UmmdraIpVRMW6rrnIY4tQ-QaC2X6kL2WtepMsE6_teUZ3yMjed5LbGSDq_sNFIKHJVDaX5Z-daGAXlxfX8yUlVBQfFuY_AEATdgQVMRROIabTOYjPP-fFkU_UQJJkQ3gfRmCaSghLcDK3HbLy89I2yHg23UMZyjUNcytSRxdErgdr3A88_hmFBR4s13kJVIbh1rGn9MQLECHInpyReU24JBAMRSUsrvODrbYDLvEEdJUT8ilwwr4ozppQpzUieeV0tdd4zSL2qpI6cwJ-UloiLIoJjr3oWVD2ErU-E6R_frUPgGx5envdaU4NENCJxEZWmyRQGQkOdL2rY-u0eKKBz3hXdibtWjHEYuQ27K7T4Z5YRggwF47lAmPY5pfDJYpc0gu9e5HIFltzXyTZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی از انالیز دقیق عملکرد خیره کننده بارسا هانسی فلیک در این فصل از رقابت های لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30196" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30194">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3-TLHRW7ok97fiN8hTcihhnXPKsoFfBpriaj0sqYoxR2IzWlqY6y65y7meYpzWEfi0o6fsky_9y-rA6lDHFz9VbBeTvku66gvdhLC4rifiSqtF0ZBfS1NnC6bRQlWU140t8vS4ooy5SN0qHOdUHNGb-be-Yr3OpSSPzBxEShm4Zftkt7mBC4KXjS1WFh3dDiEA2PWLoy5orMC94b6j9fMlTUyReu-b3-IaEPhlPnJw18jJKXP0fD82oyuqwEWFZarl1KHP1rAKoGJc9JSOdmmzV-cNC8b_1A8WbQz717I7V2BBVuM8LEmy9nRlQ3F_2NhjfKVyyh2AqJTpzI-VXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTogKWpWF6CFncMGoXtENCe-xzElzZKIFDeJFl1D1PQEEab3qGini2TnbWuY5bjSQnSeIzqAvp5WmD989_VZa9Jofbtsu6rxKkW7eNHMb1oXkfIjC0j8acwSs9HUlCfFZD0FWfPmSOHqsJUjCOlTzhBkLedbJDJuOJnrAkfJ-qjOxYkAiuhEC6xsEKkKTAJCcbRyc3J7WGSds9Q1jYFvJkbdQkMEN6s1RJQggWtpqXahhWLomM5zZxvJA6j_iFd8R4HoNTVh7gJ7FOwNgph4eDfm-FMfaIZgq2GFIObZsecbJXbh0XhdgldRRJTgLjpi5nNE7bh42lgXlvcWj2ks4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30194" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30193">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnG_UpTubZbJ8UV9iKxFmBl5OFMRvCIZYw_HN8fLsvkmwd_46nWkoXzV0hDHMsqKMtl47XHgKgMr6AygC5UwyjkGGPQ_oBVOV2mrK9ww509R68oBh-mP2zoAqJEcyLHga9XswaKu-j7RU9UdtJ_d9nRafLWoHJ95JIvbsDGwq7QVwEdrDHAwtXKh6mSfI5HRh4cmGMTswgT3vhKrb2x6x8752owA8Hu59fvqzawQC4cyLU7YYJgPyesQtrbJZqxBjW02RNd-RB1MS5gJhTvDfBPIYs-UdVo_EDdwpdmQNolhPEx5conrygzlJ-C5iJVWUuMPpuB1KC8ez4G12K-yHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30193" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30192">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwGwkyvheLguY7Xr2Cy0vee1EovlK7XzdrnLLVSov1Dt0SAFELOS3VCterqHep-63gC_MVIFKRsYhtBzUVQHqoACp9NWT4TR97vwCtu4NPDbSdeaGCzN1ToYktfvu350w528p1cDC9buNoug6XjMOR-zsCVk0Ey-b7q9D3bNDLOSb4nTprL2k25uFHAZmdKzLHbRX4Q22oCTO1CxbI46qeNPOPXBNoRtqCRd3LwG-dN6dDU8CupcFdYW-lWwU0FbDj9dmuBIVsC59mR0mGO780Ms-KODZE-fKq_MsPjYB0F04ciU9bhQmJfoWvFC6uPAYGLUZVPZow471p6qyjb1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خبرنگار:
بارسلونا این‌فصل خیلی خوب بازی میکنه‌نگران‌نیستین؟! ژوزه مورینیو: از نظر تاریخی و فرهنگی رئال مادرید با هیچ تیمی قابل قیاس نیست از مقایسه های مزخرفتون دست بردارید. بعد مسابقه الکلاسیکو از زدن این حرفتون پیشمون خواهید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30192" target="_blank">📅 17:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30191">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=WySvABXqMoqn37wRJp6WdjmZuR_v-WMzktW6Mm0jKeII9CY0uYUt1-XQz0vBgITlMDLbu2txLV1f8WTVyaRtM4aEGuUS0Ai1KeZDJNCjfJXkOTcJbV36s-hOexB5I5XuS52C584uUzQa8X_snuxZtbh-e9UIn8pdS8Iv8J87IaMnis3O8GkBEHv1UAhfV62EBuN7zO_qXi890Nx5z3---j1cEIh5DNMiSdOXjVNaaLUj8c05XfPZNllSwK5osGs_xkkfZgjgMMGVQUx82VPDJrWHYGW_z9bBRdupKEnhvNW8luUv8Gae3ma2ug6OjapV_WaB-pwUr9qE_JnutB02Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=WySvABXqMoqn37wRJp6WdjmZuR_v-WMzktW6Mm0jKeII9CY0uYUt1-XQz0vBgITlMDLbu2txLV1f8WTVyaRtM4aEGuUS0Ai1KeZDJNCjfJXkOTcJbV36s-hOexB5I5XuS52C584uUzQa8X_snuxZtbh-e9UIn8pdS8Iv8J87IaMnis3O8GkBEHv1UAhfV62EBuN7zO_qXi890Nx5z3---j1cEIh5DNMiSdOXjVNaaLUj8c05XfPZNllSwK5osGs_xkkfZgjgMMGVQUx82VPDJrWHYGW_z9bBRdupKEnhvNW8luUv8Gae3ma2ug6OjapV_WaB-pwUr9qE_JnutB02Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدرنشینان لیگ برتر تا پایان هفته ششم رقابت های لیگ برتر؛ هر هفته کدوم تیم صدر نشین بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30191" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30190">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVANM72Dp4S-BIZUA1_WMp4lN81WoABWU8CP2ppDbpmHwK_HjFq-v9iAEb_EiLMH_TTEyxBCpuSCdqKpTzvaSkk2REeuStTNiZnKD9UmR8wRpjHSIz6a7zAUHOEnPM0ET75zAOpHHs7PmRenGXBlMl5HaulLxzBfuPQj1Xm_Ra8fisqyATVZejeqvqlMscOQedajcqeAeKcikiGtzGbScdsZ5BEX3oul3OZBOzi6UcgJt2VE9flsWHkLZxhnqYA6s_KHLzT1f6Zrajp4SYfF0VdA40ImgQOIcULSJxf-ABoEheK0r5g-guP-stfCtXxqcM_L28hiX4fOBhXg-7zAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30190" target="_blank">📅 16:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=m74VjUBdCXnDDg48C_q5xv9NeXQVsvEuVBoM1FhTa3lO6NI2HtqXnTSW2y0v-Ijye8RQ_oGikyrmCLKHEFsybVGVAHxk2_rfgNJbu7SZJZ96LpkuYt1son5PVURd6zYaZsxKFHRHPitwjeXwoialuXqIhAHrE09dU3gBSrAOMX9Q_GFcgqBMFv2EPFTptFxyuDU-NEsj6hLZIZdAHtqPA8Oth9Go0agZdJXkU5JKcp1ksgxkgWdzUURGxRQdkqUNi9XxbAVi2biNpPb77_VNKAj6izJI_B8975qofqWcK-cJbkQR0T7N-n13baE2XcK1XXXEQQu46n38MIjRdmOnzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=m74VjUBdCXnDDg48C_q5xv9NeXQVsvEuVBoM1FhTa3lO6NI2HtqXnTSW2y0v-Ijye8RQ_oGikyrmCLKHEFsybVGVAHxk2_rfgNJbu7SZJZ96LpkuYt1son5PVURd6zYaZsxKFHRHPitwjeXwoialuXqIhAHrE09dU3gBSrAOMX9Q_GFcgqBMFv2EPFTptFxyuDU-NEsj6hLZIZdAHtqPA8Oth9Go0agZdJXkU5JKcp1ksgxkgWdzUURGxRQdkqUNi9XxbAVi2biNpPb77_VNKAj6izJI_B8975qofqWcK-cJbkQR0T7N-n13baE2XcK1XXXEQQu46n38MIjRdmOnzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برسی‌لیست‌بازیکنان‌دعوت‌شده به اردوی تیم ملی برای دیدار دوستانه با ازبکستان و روسیه.
‼️
اللهیار صیادمنش،مهدی‌قایدی، سامان قدوس و علیرضا جهانبخش در این فیفادی غایب اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/30188" target="_blank">📅 16:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY3ORRBOLIII0JdrFP08yA_FNOtGTJV97HvJ_Q_jZVtrfnUygTGHWXpSEYzzJLAbukWOR2PjkKV_sYd7kIcE2isnRgXBQKjfgF9n2J07H8Rlm8eUrJ3m_vaTExA_5TtqX75N9IzVy3DOtU6nHn4arTbVRMmSg-KL1Cw8yVh2uSmHQNfwovHXIIPKYQqhk_BgaHCFiexuYQAki3mcatBhGKzcxd247wW0OgwXeVCYyIU6saS8NbKmcYb2x1mN-K6arjHF9lAx5Dxo8yoaQLr-gUP33JJbZYUtT476g2npsggi8heDeWal2sK3R32IoCzxaopf070xvz3gS9ZXoXSRjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانیت‌ژاکا ستاره‌ساندرلند تحت‌یک‌پیگرد قانونی قرار گرفته زیرا گفته میشود کارت واکسن کرونای او جعلی‌بوده و بازیکن‌حاضر به زدن‌واکسن نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30187" target="_blank">📅 15:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30185">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ih-MQ40tSCxSsQc0nMXdt3nw_QiEp23rkuB7VIMKWLLDf3GUadzkCHeNcidB6Khve6PYFq17rkdEeMBs1tRANRakvKwVMk98TVYrLrrBmRfbx4wclesNkwUEVz_PdMUGkOm2A4PzeCIGzswQEh9qpfFQM55VAlb7cxn_nWZ6E_5pHlHI-TSF7BHJgNtS7Zpta6kmXzFQbVJr0il4hwlx2VMgX-ga_U0jbNLMKijmbB0l0_zPFtv_a9nFUMYh3VzhlZhpZxwn0YLESbY8t9ODBlr-RH-ptXluFP80PTqQzf7SPhsL25D0LFbmDqbGl4uG3xMhx0XkmOo9uxuPrnjfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBFWZqqsgRT3lEpxCrOJ8SVX8JXszkQiIvuEm3b15T9a4Jpr3ukiMwyEpO5mB9h7-5g-vWE9MKizkHniMuVBEv0fBik4YTZfy9mXt8FS0gWBMmzcq1tQuUrJJy9fQCXfgWFdy4spm68aBDh5Y1--ysUe18qcn9WuZ_MPrOwju0MBZ_7jpSIroHYwyHoeQcduXK3D30zTk5Ny1Yf1htNItauTqHvE6ZQNJ8_xzjVJm_zy0Gp0s6BdDPS77j72GxicGPotTc1YIN_Krq1VbtW27KHNn8l27z693wOJvhOBz4mhDWZh7L9v1mtQDquJEPVQHa4vBXhhWMo9spvks0sDrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30185" target="_blank">📅 15:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30184">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi-UTOraSDNqgt5vPEwLUfxiz2IsrSCGGTC3eZFSn4qJEkbkXx8oxdUW37ha5CP5QMbv0zBY5s0YzChzrmnbGG_BuXjYEIbDj4n-C0XLPik0TzMYr14jhQX9a1jkMrWhbMLZnR_9Mrky_RAlctIvQIvt-CCOJJO35krmZTxH0ChQymT20_3YN70KHmFPwNUP9Pz3yT_CalOVHh2tIbszA9su3hb6_Lu88hte474MBve3avREbajPDD3YGLT0CNJxZ0z6WYLZ4b_xoo2rkeqj0wcsyLvBEMxgflom4crQnUuylS71wkEjYEXX2PUMxs3X072DIbfxZhHXGJ3ONGU2lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30184" target="_blank">📅 14:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30183">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0shOOLaKa8i4_OxGBzcpuODuUrEMp2WEVlE7Hd7GsbtuogaLpMg2Y7k-M4jxdu8yGDrA0iOtt4Rwhiu7lwAxTvyCUEiA151zllNVbGp2wFMCDD6-zt9H1xHsvUPvWASJICykC3P1Bsy26TXxHkHJDqzpzWQzDh7e8a9d1rzkKuEvgbKCp7fIsui7OjF0Hk0juC3JRZ-OoA-Xw5aHR1His9xW0W9_c57MYNQMDl9atYBfc5hq54__Nr5EnTrRJMtr2hyO3KMM3lRNd88YACmiu6yRF4CkD6bNDrRggrjkqgOh3zu6X5B8OinTMpj-8wwFf4LAbQMwd9UGK1Enp8lLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30183" target="_blank">📅 14:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30182">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcXSclCBjezng_HJJibpgJBETRMCyxPy17yqt5g_RAN-DDgW51OJwNP9bgiDRarPckjM4k3-OfqRc6TjLmgUHY-uYMF7et3W-U4RfV3-p8MNMpmeXDqk7wzmesedBHvUPkYuUpWxmrfGqk72GE7zEGeRbEb85aDWtE95GuF3y8U91m9fB76BCvm5xDhCQCEW65yOdlE3SY-ShvgYpzDtz_38zJHRhnEfNUCY1nTkaZLItq8im5ApDuFgonU_j-E97-H3E0AfF0tx5wHKooanURYq_nvSX0RIaptBHpeQruqsxWSKRlsDH278gvqX7AEzYvpNu0qO-iSYGAW3ZlQaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30182" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30181">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
آرزویی‌که محقق خواهد شد؟ درحالیکه خبرنگار فنرباغچه چندروزپیش‌ گفته‌بود آرزویش اینه رونالدو به این تیم بیاد حالا رسانه‌های عربستانی مدعی شده اند؛ رونالدو در نقل و انتقالات زمستانه به فنرباغچه خواهد پیوست و شاگرد کارتال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30181" target="_blank">📅 13:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30180">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T93XBA_ncy_FR3AJ0nK4bSR8y2d9IiFDiGk1skqR-qVU_0rs125lEtkVy_3WtfGIPK0buLpjQRt3s_I1RUOPbx9bzZM0Hn2g_Ly3pgeURsxaABvzAhk2DXL4-_jGOYr7GA6i1_A4udim_ejVaPuWnZiKZ8XHEoOU3cc_0DK5atDZP0arNNjJIGVs6iRq7EpiOnzTrg76BlddBZ35bjqIyooZu9gME9dPwUlpiRn6iVF9VH_R7D7OhszuO5jVBm4fch7NqLAhIsmO80gx5XNh8oklzoQCbgxPhn6C4SQmNcGOSd85pbZyicbQhUDR27gCS-fkgiJa1cuOc6z2zQ684w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30180" target="_blank">📅 13:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30179">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjxCHXoPPEJ093B2Pb60pzbebVhtwU_dMw6fZKap6Yx_yqzj3tZ6LIHo5C9RbE9hr6VIN0RHoIzDjUfYbmzQc1s_WSjLnlJSOV3t3erdM2SqQi_quVDQ8nb77S1rjnKd1mcvUZzSjxMxcXv0-h0Rl4A7lER5V-foyuOMMrpiMznr2g21YZdYifoYBK5ohrvmaAvfDdTGo2aa2fpLCeKwwMlMk30OvR8qF4gskpo-ngrCH_TeT6KKnsG9jTbQajTfhI8OQRI5zzttyi2IqfP6Ma0Bbm9H4U-UKMECzNQyWvKpjBrrNyW0PsjjzAGTYUkQZSlUofgMK33TTfDgF0IvFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30179" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30178">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd_s7Iz0Q6Q78DrfNYj8PtiDRIMzDDsGcoWjVB_vVqmcz07Q2NL58IzfRkJ5Ono8l_4aSxsmq9vRvTGT_RK1g95-gsXGrVoKj1HTe1CNI0h6H_eY4aB6FBjDyn0b6AdDPtjPWEMjowW_IGgclct6bbUpJv8aFJiCd8uvwoeAb06ibwjS58x1vbV4mVPI_OSYcpKH4K1Rve9O35UR-xSJwvNNUcsOF6vu-dXRXCOkNEApfCFQAR0JzYx6EYuGtj6TlO1WBM1HSe6NzQa6GQ6AMYO5SZZTT65D5PdHZlnJpMIWybV7cdTq5sBE0XD5r2PfJkyJexGTIFtX4bJX8w8h7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه بان تراکتور در جدیدترین درخواست خود از سازمان نظام وظیفه خواسته کهه یک ماه سربازی‌اش به تعویق بندازند چون مریضه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30178" target="_blank">📅 12:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30177">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCUA0-hi0wGUAe44kPYLAA1ji-9bpKQUPg9y9_U2AHazag9hXxyCi04ep9rmyH6AI-S8btFGai1hq7c5koI3yQcOoz-C872x2N-OffV4ESAawzXUVNX51CMggUjBgWVPyhcfZiFHH9qpUmo8nrqdEvoxwL33cu2gMj0gXECaad_v-XDWCnjLWYeB9rlMKAia3WH5jsHh9vv_Xrhk187G7JMy_h9VlT75qsBDtnBW8BpeH47vyzf47PJRZymERsBdyL7EgiaqqmvbbU6pppiUXffy6b28YNptvnCHRsRSIkKsj2ec9VeZtYZmv6NJq6jm-DVHZpVH-Ml5VxUJf9DwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30177" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30176">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b904658a51.mp4?token=akL8AI85Adhai-5zQ_kgnUZekd6O-PcWHXgdtCNFeSdsXrMoB4wKfa_fxcRtALpsCxVT0oRtVc9nWQ0zk1Z6-74zqkayFO1KIPGAyMG3IoUUgW6g2Qaw95uyxxv937Uf5l5xAhJwWV3n1n8YMuJQK4nX2sGZWkD0MiWm7AM3j_rusWfnw909IWPu-HGH8Ga7wphP6I2R59bvtfIfBJYD7WWnTJM_8RuS-52kpQd16YYvfm4Jy-EAkLlp2lTFfvmBKVENerdr1jBa_kbvgLy2EDkIyl0OhSWD0NDpJDKbGCmuE62xJBAROhgA-E2zq7NeiK9FB_Ss5BPUma-EWx7wow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b904658a51.mp4?token=akL8AI85Adhai-5zQ_kgnUZekd6O-PcWHXgdtCNFeSdsXrMoB4wKfa_fxcRtALpsCxVT0oRtVc9nWQ0zk1Z6-74zqkayFO1KIPGAyMG3IoUUgW6g2Qaw95uyxxv937Uf5l5xAhJwWV3n1n8YMuJQK4nX2sGZWkD0MiWm7AM3j_rusWfnw909IWPu-HGH8Ga7wphP6I2R59bvtfIfBJYD7WWnTJM_8RuS-52kpQd16YYvfm4Jy-EAkLlp2lTFfvmBKVENerdr1jBa_kbvgLy2EDkIyl0OhSWD0NDpJDKbGCmuE62xJBAROhgA-E2zq7NeiK9FB_Ss5BPUma-EWx7wow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه‌های‌محمدسیانکی‌گزارشگر بازیای فوتبال به شاگردان در مستطیل سبز که منجر به گلزنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30176" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30174">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=gLumB0XRvyk56jack_MblpleOqE57ukzmdlUNCH7uUclH4_eTNpqVwQMXsz_zEonnkJ6Q9CTAlD91bdaDJKNsrA_Xfhr0BpdZ245-bPtbK3Qf_IRizfjlduGnP0HXqAq_qL4ys1eXdqnX6A8mqLIyvmil6QY9HkpURDujc47WeApTkuJBxY3aSkaR7ifMezLr7NYst9Cf-CRQej8mS9LD1abKGzYM-_AY4ubcW5s6N36PkiKbtR1BBMpHmNhWJiUn4kGXdPnjzZq7TwYLWcJGQe5OtZSXE8SVcVZ7a2mMWRFUiTkbhWlGR2t5Y6RhhirT2RUCecojgRKvMcDnAVOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=gLumB0XRvyk56jack_MblpleOqE57ukzmdlUNCH7uUclH4_eTNpqVwQMXsz_zEonnkJ6Q9CTAlD91bdaDJKNsrA_Xfhr0BpdZ245-bPtbK3Qf_IRizfjlduGnP0HXqAq_qL4ys1eXdqnX6A8mqLIyvmil6QY9HkpURDujc47WeApTkuJBxY3aSkaR7ifMezLr7NYst9Cf-CRQej8mS9LD1abKGzYM-_AY4ubcW5s6N36PkiKbtR1BBMpHmNhWJiUn4kGXdPnjzZq7TwYLWcJGQe5OtZSXE8SVcVZ7a2mMWRFUiTkbhWlGR2t5Y6RhhirT2RUCecojgRKvMcDnAVOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کل‌کل‌کردن دوستاره‌انگلیسی و آرژانتینی در بازی امشب رئال مادرید
🆚
اتلتیکو مادرید: جود بیلینگهام: تو لیگ قهرمانان اروپا داری رو من تکل میزنی؟ کوتی رومرو: تو جام جهانی داری با من حرف میزنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30174" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30172">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLTI5oGyGk5Gorqhm9d-IWO_lzyULrWbK7NZsNDVD-CDUbRC3oFbVrLxmD-_fCYbs9P1m1ouI5wJH_CLasy-ZCqhXLJSwD7i0M2d5b2E6JDr0RoTA4DOOypnV-7TS_GjW8P0nv2ygkFN4mParWfiKhaO74c14RQmGx5aCBjsN2YtGM0B7hx6flgMr72mcjtr4e0zDtFg-MZF4R1-BeC6VZgzf7JF5EHcqArIYr2i4u-7aUhOTRSHgyvhDgAhBCdcisOnKICY4VbM6i30i2rmJBRLqxSzMZrfUaYDpV0bBuTM87cwrwvOULdwkZrs5MGXm8YzsmRSxeXXw7S060DCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
دو مسابقه استقلال-شمس‌آذر و تراکتور - فجر سپاسی شیراز در هفته یازدهم رقابت های لیگ برتر به دلیل بازی های آسیایی این دو تیم لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30172" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30171">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMNjzuZPQ7oCkhqgFITXHLumtqutns0c2uNaVkmTSm6y5yDMd1Fuv4vtip8CwA_3fuX4Co5wDW1hmdUEODVQ3w7ECNHkRv9bC9ee5MxLeFuqiJieqAmGhwz271Folex6uzOb1ESZ5fKJH3lIm7K6IWvnAt04L-WMLxG_km34Okxu8yyJ-UIi4h66SROMY7jN9M8BO8jjd4fgjUqShGsKpD5yQp5oc28VuZT3TXbry41syyYVVNZd1feYWiRmlHPQbPKSGTqRwCs8TNaaq9mJQrsCVMeXHO0HZtaNrDYsibsnsbw4i40-bZKKh5dbxqlf6COrGi44RZekmnMjjOC7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت نهایی سه نوع آیفون 18 پرو، پرومکس و دائو اعلام شد؛ آیفون تاشو یک میلیاردتومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30171" target="_blank">📅 10:46 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
