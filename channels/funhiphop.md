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
<img src="https://cdn4.telesco.pe/file/cCXHbVNfqJ9VsxeFPYe-IvD4Qe3VOS4jXvdyWF0HzcR2jgzWTym9HQ06CetLUXse8qQAHM33icDfptHZtAC9B2SbctYcLMzpaK4qPIeN6Z0QOjN2akOSiaxb7ZaCOKu3gJYUq19rtIN8ZB_71QPAo0RAjJCjGwfAIwgkNc1fzDNUfg4TUremzU33yXenLCN-cSmJCmbmJ9kqdQgpjpqdzkknePMvQc5p7DK_2SRboRAiO_wZeGUxl2-R7Y0WC9AOZsmps_xUaLRi9SE6oXRc4bfx3Lf57-kEcBQu4LN05pLyFDSJGWlzHXMZ16by9KwTYMunyRfdzCqKrtHo7a3ADQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 204K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 05:20:15</div>
<hr>

<div class="tg-post" id="msg-81035">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سنتکام اعلام کرد عملیات امشبش تموم شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/funhiphop/81035" target="_blank">📅 04:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81029">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تسنیم: دشمن اومده رو آسمون تهران ولی جایی رو نزده و فقط صدای پدافند میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/81029" target="_blank">📅 03:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دانش آموزا بگیرید بخوابید فردا امتحانا برقراره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/funhiphop/81028" target="_blank">📅 03:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81027">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نصف این گزارش های انفجاری که میزنن فیکه، تا الان پنج تا انفجار برای شرق تهران زدن ولی هنوز خبری جز صدای پدافند نشده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/funhiphop/81027" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81026">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ginza</div>
  <div class="tg-doc-extra">J Balvin</div>
</div>
<a href="https://t.me/funhiphop/81026" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کوبارسی اینو بعد قهرمان جهان شدنش گوش میداد من وسط بمباران
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/funhiphop/81026" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81025">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/81025" target="_blank">📅 03:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81024">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZahra</strong></div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/funhiphop/81024" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81023">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پس خبری نیست، جنگنده اومده بود پدافند فعال نمیشد.
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/funhiphop/81023" target="_blank">📅 03:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81022">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صدا پدافند در شرق تهران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/81022" target="_blank">📅 03:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81021">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شبای خاورمیانه واقعا ی حال دیگه ای داره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/81021" target="_blank">📅 03:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81020">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شین: انفجارهای عظیم (حداقل ۵ انفجار) در مجتمع پارچین، شرق تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/81020" target="_blank">📅 03:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81019">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b1c9a3f5.mp4?token=tXGrbc2fscYFku5yW40rWBposkbcq76JTkApm3kgwNi0Om0GV7VM1Mzx2VkfGljLCZVaRsnX0AuQXJ8usEsc8BXIUEWlQHfXk3Y8Wkv16Q3KSFvD1iVQoZzr_b53mu4T0raj_16sw1PzUarAgyQjZ66iP1hOg1Ef-8kmbVcC7UMCk5ZNeysrtSzR-oVgxMpVSnDnlM7VnGH3WW5-PwV2ASw5apGuTZkNgli4iQbz9ITaLPUk4BWrSva5gqhUAjUljD2mLQ6o0ys6SJw8EqPTbtrKPaipcyRRpM3PJ-5-Fpk2utC4We6QxhtcK2bBp4dVl1oqu5533jHbARWItlMhooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b1c9a3f5.mp4?token=tXGrbc2fscYFku5yW40rWBposkbcq76JTkApm3kgwNi0Om0GV7VM1Mzx2VkfGljLCZVaRsnX0AuQXJ8usEsc8BXIUEWlQHfXk3Y8Wkv16Q3KSFvD1iVQoZzr_b53mu4T0raj_16sw1PzUarAgyQjZ66iP1hOg1Ef-8kmbVcC7UMCk5ZNeysrtSzR-oVgxMpVSnDnlM7VnGH3WW5-PwV2ASw5apGuTZkNgli4iQbz9ITaLPUk4BWrSva5gqhUAjUljD2mLQ6o0ys6SJw8EqPTbtrKPaipcyRRpM3PJ-5-Fpk2utC4We6QxhtcK2bBp4dVl1oqu5533jHbARWItlMhooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پالایشگاه بیدبلند،ماهشهر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/81019" target="_blank">📅 03:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81018">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سنتکام:
نیروهای سنتکام از ساعت ۷ عصر به وقت شرق آمریکا (۰۲:۳۰ بامداد به وقت تهران) برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند، با هدف تضعیف توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/funhiphop/81018" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81017">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60f68ed4a.mp4?token=NKzGIUe8IoZzQL2nMyneQgFmbGN3Lcou1B4xLjoGVhwyBroTqerIDQP9K1lB6XWuVOfbSM3jcSJMaitZNPJzfevCup8c--l0ExWL33Pa9dMxOganK_TgcbLyubapYpEJgclHrPucin-Oac1cXdTiorm0RHVx6mcneSrKVxcazePTBjE4ORmLTJu3EsHxhU-JiiCyIOm56950XYPx_WrYV6TPN-4KUULBxrTenM2jWoJJxqN2De9Se_JB5D7T_vSJHX5sEiWBopvDyue05TOgz5hUbEK-es1NGlRbnkJwWnYN4dP-BDUHHpBHdl62-2L6QVf5EsXYIVRez12okJWiSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60f68ed4a.mp4?token=NKzGIUe8IoZzQL2nMyneQgFmbGN3Lcou1B4xLjoGVhwyBroTqerIDQP9K1lB6XWuVOfbSM3jcSJMaitZNPJzfevCup8c--l0ExWL33Pa9dMxOganK_TgcbLyubapYpEJgclHrPucin-Oac1cXdTiorm0RHVx6mcneSrKVxcazePTBjE4ORmLTJu3EsHxhU-JiiCyIOm56950XYPx_WrYV6TPN-4KUULBxrTenM2jWoJJxqN2De9Se_JB5D7T_vSJHX5sEiWBopvDyue05TOgz5hUbEK-es1NGlRbnkJwWnYN4dP-BDUHHpBHdl62-2L6QVf5EsXYIVRez12okJWiSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریز
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/81017" target="_blank">📅 03:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81016">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجار مهیب در بانه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/81016" target="_blank">📅 03:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81015">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فعالیت پدافند هوایی در سوهانک
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/81015" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81014">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1366210ff4.mp4?token=IwjHdJYXkZwDSBk7a1FqeP5FIYWtPxKTEwE0LWRi6go3tyq5cOpex7rQzPkCXwlDVlKtaJNraSsF_S9e_uUCQxp0_zH14NDd4DFQuIiRl97fbhstzUwVWc8jtKY-qydf4SpBGC-hPG3c2X_V_rEwbu7GLZx6IGmVTVALpAvSuQIy8I34ndNWbp6Q2UGMBelSZTkF-DHExetPoJ0N5snoxrYmX4J80zWbBx_fUB1UeiGGv9fWZm9BdhxVzx6FWGwbufOT5l7G2VddV04q7Cf4_CpUWNdOBRzEsToVrnKtD-D30trouTm8vZzHp6pipRBpZpPOn6ozMcvPKleIvbTYDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1366210ff4.mp4?token=IwjHdJYXkZwDSBk7a1FqeP5FIYWtPxKTEwE0LWRi6go3tyq5cOpex7rQzPkCXwlDVlKtaJNraSsF_S9e_uUCQxp0_zH14NDd4DFQuIiRl97fbhstzUwVWc8jtKY-qydf4SpBGC-hPG3c2X_V_rEwbu7GLZx6IGmVTVALpAvSuQIy8I34ndNWbp6Q2UGMBelSZTkF-DHExetPoJ0N5snoxrYmX4J80zWbBx_fUB1UeiGGv9fWZm9BdhxVzx6FWGwbufOT5l7G2VddV04q7Cf4_CpUWNdOBRzEsToVrnKtD-D30trouTm8vZzHp6pipRBpZpPOn6ozMcvPKleIvbTYDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهبهان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/81014" target="_blank">📅 02:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81013">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تایید نشده انفجار تو نارمک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/81013" target="_blank">📅 02:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81012">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">۵ انفجار مهیب دیگر در بهبهان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/funhiphop/81012" target="_blank">📅 02:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81011">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شین: ۶ انفجار در بندر ماهشهر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/81011" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81010">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چندین انفجار تو تبریز
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/81010" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81009">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نت شمام کیری شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/funhiphop/81009" target="_blank">📅 02:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81008">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تایید نشده
انفجار تو نارمک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/funhiphop/81008" target="_blank">📅 02:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81007">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به گزارش نیویورک پست، دونالد ترامپ، رئیس‌جمهور آمریکا، خواسته است که جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، به عنوان دبیرکل بعدی سازمان ملل متحد منصوب شود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/81007" target="_blank">📅 01:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81006">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/81006" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81005">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چرا باید یه کوه اسمش کلنگ باشه</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/81005" target="_blank">📅 00:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81004">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اقا جدی انگار تو کلنگ خبریه
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): آمریکای جنایتکار مراکز هسته‌ای و حساس ایران اسلامی را تهدید به حمله نموده است
-اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله‌ای بشود، آن را به عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/81004" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81003">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به سیکتیر (۳۱ تیر) آخرین روز ماه تیر رسیدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81003" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81002">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">افتخاری دیگر برای ایران و ایرانی، بستنی سنتی زعفرونی ایرانی مناسب برای افرادی که ضعف رون دارن، بهترین دسر سرد جهان شد. در ادامه هم فالوده و آب هویج بستنی به ترتیب رنک نه و بیست و یک جهان رو گرفتن.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81002" target="_blank">📅 23:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fodNSm-uP4ssZEL5OdZSGo173R3qQkZUXP0Jmd6av-icxK4yuA40nAGGFSXBvWYnVJH3nXrQ4A5NClx2D5tmat5MWmbRZ6JG2EozGIcEtcEDhP81NLpQ-ueIbsuLAxKACpD79VI-CaF42PLmZUTV5bK0t1PjZ2wk-jumNU9vrbVEffewteHOOnULY36AxbJxNeOigoQ2ziBKlEwrpkl_trgnPYtQSr72MFMwfEJuzHlXNZC6ghaU3ED5fYidb3Ckp9IsXOI2CFJiQS2w97VRAZub3c5BWAG78rI4FLmmW3mqqUnQZLoB8ZQGHy1z-GswMMaR0Q3u6e02ePez_F0DLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۵  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81001" target="_blank">📅 23:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80999">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TldzvsRPkPnwTCRDXbOZoZCYyosJWS0VRTBTcqc2Bc_xsZX8B3VtlsXtTlgt8zGYXQOfzoGmCkU4hFw9635XGWG1Wt6IEj2QVwJmH8gWht60TvY-E4Te6Md3YIDC9W2XiTyouUts1h4KTWlFsZA4OLp3AWIOORSkRFglOo4CgY8Hq1JwnVOIM0ARx1M2KWVkYy3yAgEOD4a2TXae2pZ5Dne8UuUXJkBa2w5ZBSX8vSaDEoxRVaFzF1dopEOhk3OZobDVrmNIKBZkxqyhwCCL_tXnW4IknG7CwnV8-RrgADWfpPQV1r5lIvk-J3X3XCNsEXho-IwVYzbkpqd5WXz2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0Qg1bMp9X069LNSHGPQINL2R3g3skWynDQxuQJZOJk3A8Dk3L-b2KQyxY9WrPbspJKFFoTmdve15_g2FUqeadQBGR95uosDw9lUsa6Wr41Bg2Jc91ShCMApgb70xJcQvHloS-ealc9StmEeu2tBqC14HyBm7uflaaf06R3iU1887N79HcjldlMfvQ4YFWjKm9Pm5RsGLacWGUd5rUS_ZpzqqyGJPQWp9x6ndunWJWusfC05zjfLdevCrw2IGM59ILnLppE4gmm0o0ef-Yqabvw10ldTzA7-WS_82aeiNPtm_D7vMfUEgOb9hqwq6vaL0Rq1TYg3B3j_bthWo6QdMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افتخاری دیگر برای ایران و ایرانی، بستنی سنتی زعفرونی ایرانی مناسب برای افرادی که ضعف رون دارن، بهترین دسر سرد جهان شد.
در ادامه هم فالوده و آب هویج بستنی به ترتیب رنک نه و بیست و یک جهان رو گرفتن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80999" target="_blank">📅 22:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80998">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جدی این یکی بخدا عی ماخارنا ماخارنا بعضی رسانه ها میگن سپاه سفارت اسرائیلو تو بحرین زده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80998" target="_blank">📅 22:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80997">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هشتمین روز اعتصاب غذای گسترده زندانیان در قرلحصار در اعتراض به اعدامها هم سپری شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80997" target="_blank">📅 22:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80996">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این دفعه بخدا عی ماخارنا ماخارنا ماخارنا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80996" target="_blank">📅 21:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrmNbG2YG6dcw4u0Hf4tXLfM1UDp7fJEbqFt0PB0dqjX6wzb7UIb_pTSNbt96AG7p04cPI1fU6EEayomN84bGfYHjdzy3MS-H9-j-8UHfbjaTGrmzFUm10a8HSIDO_L5C_7fnTjPXgCkZSiwI4CuEr8LxUlcGNEc6bB6GhgZ-KGeO3Uj4OCTa9TvRzEzAMj8OjvxV_yE5HcOwedvMPs60QGFUUvpiApWJ6svem_OBYjAPi424uSUMQ31u6UrSSvK1SCj_9pzKPDal5YDoK0vwewdwNcMF3fTaEgyTIKR6Wxa9clzzn6PaMgF3rIyf9ZrLfvl8_EmwWdNuCa1aPuCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxEVjGVAVtj3yFxsTuG77cXulPT6sy_LQz_ni8BecNIG7X2L6YPutFDAT8fUSxx1uDQd7NxxB0Im2CrgZ1qvK81RKXI0bGJCXny4sLMTRSDnssprW_q1OFTZCOVRA4GC_2UWeFhyN0JFqh5hXPe2smnVGnq1zAPbhiL7G5PFJb6OPJZ7VU_oATfeGa3WBC3QfXhE6IFxfLKaTZzzbXINxO2SsG18VgMnqW33I81WiSrrk2oOrG5LMnZ331SS_AfME31QOXZ3AQsfZu9BvYCadc8nPxe7ezGC_yr_6pVEGV6u4jct2eyvOC74JlALGqjk0ZEk5B9zRbL_macmn9tViA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینی چرا این شکلی شده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80994" target="_blank">📅 21:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ گفته تاسیسات هسته ای ایران تو کوه کلنگ رو میخواد بمبارون کنه، برای بمبارون کردن این تاسیسات حداقل چیزی حدود ۱۲ تا بمب سنگرشکن لازمه، خارکصه میخواد چیکار کنه خدا میدونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80993" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بمب افکن های B1 آمریکا از بریتانیا بلند شدن به سمت مقصد نامعلوم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80992" target="_blank">📅 21:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80991">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W88BRXIu8tDQCD5N_80hC5ht82QxU_JeytO71Hgj1jNIT4Lf_ReWzx2ojurvkQTkIhsgvDceh4IztVms7GhV99_Dqj3V8d5BXGUQFdb-W21Tgs3n7hpjDnC8ZsSv7jM6VCbTqEEflxGIK-aA6MGBVmkiSVfZyeYKCvjlS-jCZVnIDCvtyQ32vbykFPsI4af0yaHc8THQgniUuCDdShlwm_r_BXb4Dt5ttDmfEFXnGdY_yvQkgaT0LdD1bU5uYQQiuVXm48QMADFoRTLk4WxcUvTA70wuZ3F2qv7XnXyN6n8flJzXN2udmFZYFuhHVOmo1Wn8nZiNdHiviCr4GGtIYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80991" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAu7FUWrflHUrXQ_lY2pxTfmv75dABP-hJqzU6nVsOlvhv6EzzaZJD5XalWhHNSvo3Wlsm7-CyNhDzSQcf4ecyub1JZY6nyFvuWw5H_r4P2Y3dpu9HglMkI0uDq49XvhJu02_W-NjpB_YXlWBUQapPMX9ztMOFlQJqyrZLDdPBLGelMVMEND4IrEJuXJntyunamKg43JmwbraxIPwyFSvXAhcfLxucnZw4QMkzcTAvz-HjFX7OWROsvmyWX_NA635BjdUXgx7FMUCItPJVTR359Ly7wzldRg_T1rMkjcuvqnn1Jkj5xNDH4a1zojLwzzvKiby5jhwP9AkKn4AgQbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUyYkyitZ-ezDJvfweN4ptRa7fFNdqchGGZ6Z3QVZPxk1zwfVY-mIsK8PRf1_O9tQ_0QD3gwfFkrqHTrWX6Us60to3JS_f-WGpaYlqEcPxrctdLH216UNmuNibeEsRDRf7egV9o6XFvTKO1DtGzR9n3gQJrMbAtJfk865hm16YhI9m7yUUisvxMDVvN4woqC387dyJgoKW8MG__X62GDl4bYvjvKbucJ3jnXbqaNo8dxURb3pmv3wlFOacJR72XCf62HFtJE97FpMuY55A7WV6Iusu5ixsfrkt-7zDtdnm2Ex6NYdtXSS--zJfTbcf_la4jVjcknSsVgz1YAuXwqQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری verse خانمی انگلیسی که با خودش ازدواج کرده بود، از خودش طلاق گرفت چون تو رابطه به توافق نرسید و احساس تنهایی میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80989" target="_blank">📅 20:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc36a1a784.mp4?token=Ttre1-xSt1X6tCIr90lhQT5U8WyBfRR1S-HZwDOfBkWYWUJKEHFxlZro1XHRGe7_DUOgov-X7N1PaaqNYdbmOhpqWqP62r5SdAwQhCNVLBhpuannBETF06DmLguTlEgVgHzGJ7qOGR9_HadWJEcNWFCtN43Bi09BcScnJ9azFgYLag99mkj7_OsFZ7D3Ue-Ocg5fClQUftWHHf6TyhLAt8r89XjRmMaMiAz5BOzKGGV94JrqJ9N_CJvRFMxSZ3MC5M2WFjXWQgAtTm4HxWwDekvGhMlIZlIywFXgFza1T1QUFPT8Fanu8xFOfbFncNUe8jd5C9o3DneGxD-CDZ_3cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc36a1a784.mp4?token=Ttre1-xSt1X6tCIr90lhQT5U8WyBfRR1S-HZwDOfBkWYWUJKEHFxlZro1XHRGe7_DUOgov-X7N1PaaqNYdbmOhpqWqP62r5SdAwQhCNVLBhpuannBETF06DmLguTlEgVgHzGJ7qOGR9_HadWJEcNWFCtN43Bi09BcScnJ9azFgYLag99mkj7_OsFZ7D3Ue-Ocg5fClQUftWHHf6TyhLAt8r89XjRmMaMiAz5BOzKGGV94JrqJ9N_CJvRFMxSZ3MC5M2WFjXWQgAtTm4HxWwDekvGhMlIZlIywFXgFza1T1QUFPT8Fanu8xFOfbFncNUe8jd5C9o3DneGxD-CDZ_3cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید دکی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80988" target="_blank">📅 19:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🗣️
تعرفه سرویس‌های Retro  پلن نامحدود
1️⃣
ماهه :
🌀
1 کاربره |  99  هزار تومان ‌
🌀
2 کاربره | 149 هزار تومان
🌀
3 کاربره | 199 هزار تومان  پلن حجمی
1️⃣
ماهه اقتصادی :
🌀
10 گیگ | 30 هزار تومان
🌀
20 گیگ | 50 هزار تومان
🌀
30 گیگ | 75 هزار تومان
🌀
50 گیگ | 110…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80987" target="_blank">📅 19:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRetro Channel</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krIwVCvXv8Oj5QgHmxQj6c1xHtw3aN7Rss8ytPgsHf9dP1RkQb2HBFTlJNiC4N6TS9zeFTyTqrOQC40RQaOKqiHZgeyvgFjua_lZb2D9lWCtd6qXYJIrTAbHM995f-qEIg2ojxxVftSguT04IFvtIkYFMnTf8aA4vBEBtp1P-_Jc8Qu2wAuaSXberOSW6tc_YiUrEPeyjj3HiZuncfTnHl-ldKo0WBe8HK6RVZyb-hoJiUXwn48AKEwmOB-yzJ17T4wJENtqyFoYv6yTBh8idFG_Mm5hHJC4Oy7dvvQDVEAr199OTBKvWw_j2-t_9IAXjP2q3PoDnFG_4y1JYb3k-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣️
تعرفه سرویس‌های Retro
پلن نامحدود
1️⃣
ماهه :
🌀
1 کاربره |  99  هزار تومان
‌
🌀
2 کاربره |
149 هزار تومان
🌀
3 کاربره |
199 هزار تومان
پلن حجمی
1️⃣
ماهه اقتصادی :
🌀
10 گیگ | 30 هزار تومان
🌀
20 گیگ | 50 هزار تومان
🌀
30 گیگ | 75 هزار تومان
🌀
50 گیگ | 110 هزار تومان
🌀
100 گیگ | 175 هزار تومان
پلن حجمی
1️⃣
ماهه VIP :
🌀
5 گیگ | 35 هزار تومان
🌀
10 گیگ | 60 هزار تومان
🌀
20 گیگ | 100 هزار تومان
🌀
50 گیگ | 200 هزار تومان
🌀
100 گیگ | 350 هزار تومان
تمامی پلن ها دارای تست رایگان میباشند.
⚡
پلن های حجمی بدون محدود کاربر هستند.
♾
مولتی لوکیشن
💸
پشتیبانی
7️⃣
/
4️⃣
2️⃣
🏪
⭐
با تهیه یک اشتراک Retro، به اینترنت آزاد و بدون محدودیت دسترسی خواهید داشت.
⭐
خرید
|
کانال
|
پشتیبانی</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80986" target="_blank">📅 19:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80983">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uboXJqMtiNAqbR6VbOuS_OPD3rD1Xy39Pq1MKaQzsnwJA6OqxNIt1YN0Pk83JDI9nDIKApg3djeFK_OVryMQrOT1W5ZjD_C_pJUOCL8z4TCqY9gEXE-c9ZOF0SvtXWnuXQgv0L835DXU8IhVbSjlSe8OzR6ZozbSQrERe_Jn-jyxn0WSRHBrMHYdKZHHAmXnwznS74Jv3iig5ublNV5cDOFIA1TU7yqtvu8wmw2dRM7xsuzwUXXym5SEwmNahRSjI7B_-jkgkfpoTWAANzqHGhYIV2408sNHyIeg0kbJKRaWTjEXzxGj72RoivE-WnNNLk0zWx71OdBh10vt5VB_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quKYZELNA1fxdSSmnFgXCePbAlQV2r_jHNG6KbGLmbyau6esorrbuvT9AOE2wnosbpCksFQr6yurJvbzxWVwJgKCjM1G06jFYfeOjXCq8oxRvZeq2vSAL-IMJbW_4acw9qDnn2gTOTmVoRPgmdDIUpElhpi9zjt599SMyG6-4iiuptx-n4fRYQEqzwaA5Moe5thyYSbDs9XO6r-RJVj1wKsEbhpRTFoZghk2gv51Xn967n46x0rx1BHccdbtCCrwOOMhlkz4jzdqTo2fBPN-NJsI_Rs_SCghUcdbqy2_RtbOg5eDlTpuHguR6xv9JBud0Rj_Isc_4Yr9iOmxcYBtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzF6EeKwgQbp7nh9LhTtVpeLC1JJeQ0IgEcxbY9mezwhRrM1k70I6NnWB4Tp3fCEuR20B4tym0HBFJuRQVfi-PAxbtGGVi92GB1AoB5eYaSzwF9WEI6ULXSqXBnFt85Thq46i1wKtyylmuocO5KnzZ4s1pVYJ2lJVHZE_-XR_Z_DzN3wvAxdfkP9m75ydWUWD0M9FeIQmBA_1oe1uHr_U6ZMrfPkaPp0zbr5hW3px8FoSccqQHYcLbMNymL9jyXuZfV0hEgpT_ABWcwA2AZS1mz1RVKIY_fckMtT924Yan_aQwXYO10oeKEI7YBkHs9we-ELoGUM9AP_sc3kXdNQEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فعلا عکسا ربکا رو ببیند تا من برم و برگردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80983" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80982">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221f89e3c.mp4?token=MGPUYKc_Wh7I3z-UODXlqfSTKnn7FMiVPqNQnU_PL1DAK1jKgR8359OdzT8FYQp-tMhqx9Bm1D1zRpSgS5LbWyEG6NzJVVp0vogCLA9u8IPLsd8EfP11KfAUjzYWbVZrx0yQ2NFrXOJsBJver9cQiqXZw-gA0fuf5_Y4AnP72BBmw8_HL_DQqrgxA5_Xs27FfrPhchXlrhmZqlpjeWiG7QhOMvuHPQOYWcV_mbqAWjEe9kldKBbFOwm9_c5ld0d2n4e-VOqiVxvhcLt45Qiid8wMBlbAKhTrbBUT4QQuJJNhzAg2mkEoCzWg73yjty_GKGssDa3oFFU57gWauvZ29mRss3uf4SiFJt47vJe5HeozuNwKqQzlYzU7PbL4J49ipRN5A-m2ZvJBMselsWpeXwpoMhVEDKSPp9GDTM9BeRh0dZe3Y8D8JBumrMiClEpCF1VgPV4BhhqCQN7PfTFXgGLcFMvbKreehwiYlbEFPzH7eTAXPlYFQSxyyIKee9z9zxTMRxUcidQgAvDk7qyGUph4WjgW14uvRcGKYTuqZ1Zg_YUngBg2AMwJAogBVEr93_8fvVlV8yQtMKroM-XgHQPPg28gIVMWTefpMHNIlcWrQtefWOIfgd_FM0AGZ0L6yMi57jh097J2qshGhmmyD1WqmYvVwgNmoilIn9OqroY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221f89e3c.mp4?token=MGPUYKc_Wh7I3z-UODXlqfSTKnn7FMiVPqNQnU_PL1DAK1jKgR8359OdzT8FYQp-tMhqx9Bm1D1zRpSgS5LbWyEG6NzJVVp0vogCLA9u8IPLsd8EfP11KfAUjzYWbVZrx0yQ2NFrXOJsBJver9cQiqXZw-gA0fuf5_Y4AnP72BBmw8_HL_DQqrgxA5_Xs27FfrPhchXlrhmZqlpjeWiG7QhOMvuHPQOYWcV_mbqAWjEe9kldKBbFOwm9_c5ld0d2n4e-VOqiVxvhcLt45Qiid8wMBlbAKhTrbBUT4QQuJJNhzAg2mkEoCzWg73yjty_GKGssDa3oFFU57gWauvZ29mRss3uf4SiFJt47vJe5HeozuNwKqQzlYzU7PbL4J49ipRN5A-m2ZvJBMselsWpeXwpoMhVEDKSPp9GDTM9BeRh0dZe3Y8D8JBumrMiClEpCF1VgPV4BhhqCQN7PfTFXgGLcFMvbKreehwiYlbEFPzH7eTAXPlYFQSxyyIKee9z9zxTMRxUcidQgAvDk7qyGUph4WjgW14uvRcGKYTuqZ1Zg_YUngBg2AMwJAogBVEr93_8fvVlV8yQtMKroM-XgHQPPg28gIVMWTefpMHNIlcWrQtefWOIfgd_FM0AGZ0L6yMi57jh097J2qshGhmmyD1WqmYvVwgNmoilIn9OqroY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80982" target="_blank">📅 19:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80981">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBTdZEstEFDWWVQeXE84Aq_hJFw6ZuZK42iWvTwyTt9pflCb6b3kEPEOJhT_HIDlBgX7h7J82Zsbp_Grr_rh8lKMmfsMUOVCoBVwlHCnNZp0vYE_nhIJZo_rdbdQEYDDqxOVKizOSvpC4eBgSk01hrmGg5SljT-OKpv1fc8l2pvg4xZBLjVYfn8ka4UWz0rMZt1nDhfXQ7JP5fcLWLBecgp77T4By2tBaiUCRFGS41Ti9wqVRg-_85I4me4LxyOtczWGRl6dU_MdZr5HL3TREo7hU6JGEimhelX9kJdyJ5rXcOOADOkPfqN7XjL_1crKOZvKmgSAwCrn9bkGlcROuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی جبهه مقاومت شعبه اروپا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80981" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80980">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTquFgeoSTjOONqCZnXx9ATMq385-bgJKMoPO-GamCOuvqO7-DIGl8Sscr8cWGA4V1zOOdC6vgsbUvMxmTZDKexPV-S-j9f74AwNDMyrjY3MPDWXjRoOJ1KC0opCdzEsl_0Ep-eY9dBbsr9jdX3j7aFinJcB-cPzZIlel7cCrEDIWwPF1Xeo1TFlH_vI2IXPH9cB1PXydWtLkJP0p63iTPffbfPPF_5ty8osyxIRXcgn_0jv3cH1YmunHoPMZx2wiQcPZRZ9FSosmxwgdhq2rXcwnVDWhmnKgGloVPPd0nsBK3fezwy5yHyxgZdh1l0S9MiHCO93MAsycCjbahHLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
مجموع جوایز پنج هزار دلاری بلک‌جک زنده
🃏
🔥
با ثبت پیش‌بینی حداقل ۵۰٫۰۰۰ ریالی در بازی بلک‌جک زنده جایگاهتان را در تورنمنت ارتقا دهید و سهم بیشتری را از مجموع جوایز ۵ هزار دلاری بت فوروارد دریافت کنید. در صورتی که جزو ۵۰ نفر برتر تورنمنت باشید بر اساس رتبه تا سقف ۲۰ میلیون ریال هدیه نقدی به شما تعلق خواهد گرفت.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BLN
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g30
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80980" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80978">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b79960724.mp4?token=mXk-MlA3_rX3JJP7VVBw-IhaYVDLGz4KWzgsH0bQcSyN3eHMGZo1JjmDjsZkrDS45W4-CWOYdJR9Pd8QPGKy7vC18wzMG_gnrwXtFvSDeWTgBgGFwG6D1A7nbL1ij5FImd7DAHeG-4VfhHrWXFpCw37RF9d2pRh-8RS7NoQvbYMwPAI7eu9NUsp-W6qBXCyG7AxPPm5RnWFF3nIm6PcoBkBO_cFBdrMRJ56GZmxDNKm0r5yo0lqFEuYic7guHoZ9wnM86PWTK92gstJS8IVITG24e_OEKJTfM0cq2bdvai5TbX_UAgI2i2oLNhIGQerpYM4Qv6taE2NSKNXRSKEu4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b79960724.mp4?token=mXk-MlA3_rX3JJP7VVBw-IhaYVDLGz4KWzgsH0bQcSyN3eHMGZo1JjmDjsZkrDS45W4-CWOYdJR9Pd8QPGKy7vC18wzMG_gnrwXtFvSDeWTgBgGFwG6D1A7nbL1ij5FImd7DAHeG-4VfhHrWXFpCw37RF9d2pRh-8RS7NoQvbYMwPAI7eu9NUsp-W6qBXCyG7AxPPm5RnWFF3nIm6PcoBkBO_cFBdrMRJ56GZmxDNKm0r5yo0lqFEuYic7guHoZ9wnM86PWTK92gstJS8IVITG24e_OEKJTfM0cq2bdvai5TbX_UAgI2i2oLNhIGQerpYM4Qv6taE2NSKNXRSKEu4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو جشن قهرمانی اسپانیا یرمی پینو رو اینطوری معرفی کردند:
قبلنا بهش میگفتند کریس رونالدو ولی فرقشون اینه که پینو جام جهانی برده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80978" target="_blank">📅 18:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80977">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](𝙼𝚎𝚑𝚍𝚒)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wc8QHIWThxEOLOzLtu5lwgl96Mu4WGsZNSMRpRdqIg94XMN3vYgkt_ErMrZA03MDEwwk6RbK6Hs3HKFh_MwAc6OxKxH4JL7fDkHbF03acnp2Ym3O60yZ-YJF_Ex-_xCr8jwCsP3dKBBOr45nR3oNjDU-6vjhh4YvH2npCosXqWH_L4FCpvnIQQN4u4J34-n4_jl4UpwHCIWqWimpBIQNGjXoihWJMNna_7BmaDEPApmSv30XgDRx2OCKSFcLFhrUppxgJiBkV9YPQnWN9f-v1Yu_6DUdYNFFGPzogb4bmSEM-gtsF_WFpNkWSJU3mSskGow3Z6MJF1zd4NMlGf0V2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریف نبود</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80977" target="_blank">📅 18:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80975">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بگردید کارنامه منو تو چنل پیدا کنید، قبل امتحانا یسر نگاش کنید امید به زندگی بگیرید</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80975" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80974">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امتحاناتون چطور میگذره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80974" target="_blank">📅 18:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خب دیگه چخبر</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80970" target="_blank">📅 17:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80965">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آمریکا یچیزی حدود ۱۰۰ تا سوخت رسان تو اسرائیل جا داده، این تعداد سوخت رسان میتونه ۲۰۰ تا ۶۰۰ تا جنگنده رو ساپورت کنه، معلوم نیست چه گوهی میخوان بخورن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80965" target="_blank">📅 17:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80964">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آمریکا یچیزی حدود ۱۰۰ تا سوخت رسان تو اسرائیل جا داده، این تعداد سوخت رسان میتونه ۲۰۰ تا ۶۰۰ تا جنگنده رو ساپورت کنه، معلوم نیست چه گوهی میخوان بخورن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80964" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80963">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عادل با شرف
❤️</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80963" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80962">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ما کی باشیم نظر بدیم اصلا، ولش کن</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80962" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80961">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دعوای عادل و صداسیما دعوا خانوادگیه، دخالت نکنیم بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80961" target="_blank">📅 17:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80960">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جنوبیا نگران جنگ نباشید احلام بجاتون موهیتو خورد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80960" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80959">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGw4YeJnEW6OvmlsbfFLkWlo2asYvKjjGqy2WjW6GZF_svk4zur381NcEEB-4TUUXlU33DTIwWubcQXoVL60d3Lv-Z5If5ndTW_WiFD8O4LBKO3Y4drLb703EiCsAXtHIoWxGkYW_Wf7Snc85sEL-CZNniJ1wRFaZV1m3AtKcZtMRKLj94MSmxwzouFlcwlthhjMFrWgxoO7t9BC0HlDjeLlpFtC4nYrBLnCu8UAMY721LRjDkYgddPI8-x3D4B85r1JGQp9fNXqpZtsakcA1HdZEKRdj4-D6pIv6j1zVnwbQdEOxsGvzMecusMuGcSKeiEs6Uj49PWCMdWHaeBywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوبیا نگران جنگ نباشید احلام بجاتون موهیتو خورد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80959" target="_blank">📅 16:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80958">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTfZR-Rcj3FWp2sTOWx9Q08sgd1c3bEvMbQFgLNYb_AWt0JUuJXZ5ETgr-ZIdU7h9u0eo3dPPfXJHxo3lB2PetDQPsGr6CukPiCQdDe8XQ7H2TdC37eFn_VXMVkOJZJ4ULN6L6ACh0t07rrRj3qHoEKgy2V1gcVdF-PcxnM9QtduTPxtBFbS1dph-OYhBp-V06pFDdrK2KmRlU7L9mX0rFNLr4kcKbgg2bX4qVGg3PeTvuSTfqzDzDbkN-_NrdG0kLZPSQOyKU8lA2Y0wl94BDtkOA45kMWIl8zrV-TnW9I8rBw1lApIpLVuyWHkfXMZqz8BcwT8ZdkrfXxF3V08JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم ناجی و تتویی که خیلی وقت پیش از چشماش زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80958" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80957">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انقدر هوا گرمه که هر روز از دیروز آدم پخته تری میشم.
پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80957" target="_blank">📅 16:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80955">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دعوای عادل و صداسیما دعوا خانوادگیه، دخالت نکنیم بهتره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80955" target="_blank">📅 15:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80954">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بارسا لاپورتو گرفت</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80954" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80953">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جرزوالم پست: ترامپ پیشنهاد قطر و پاکستان برای آتش بس ده روز با ایران را رد کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80953" target="_blank">📅 15:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80952">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سپاه عکس بسیجی جان بر کف فران تورس و همچین میمون فلسطینی رو چسبوند به پهپاد شاهد و بعد شلیک کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80952" target="_blank">📅 14:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80951">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dbc0a853b.mp4?token=A37-FfLFaE7O_VAuLFE9oOhyYpL0wU7V39hhJ2MOKauXjX9ZGcEslgFeymgf8v2IuJxrM9IysH5hsqwmqkvrcVNxabQGWVi3r4MsmENi22rfE5sXDjRX5hLaobSVbHlqhbQO2cLARARJi3AqJi-G6suJjCtoPypn22-Z2VuyUcNiV4S6Q2c6HIw1edP-WEVyJocN1pq25fL9JDiq88kfzVw6OwlSgO9fW6NIb41KwPX-__NOQN7y7T3SwjZEgDAVyH6UY9TtX9o3BFVQ_HgooQWyP9aJ4KYT2qRTr-2bK-DGPJAwjlD24_44xBiZunsdJQRveF5rzYSEx5RkbnftpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dbc0a853b.mp4?token=A37-FfLFaE7O_VAuLFE9oOhyYpL0wU7V39hhJ2MOKauXjX9ZGcEslgFeymgf8v2IuJxrM9IysH5hsqwmqkvrcVNxabQGWVi3r4MsmENi22rfE5sXDjRX5hLaobSVbHlqhbQO2cLARARJi3AqJi-G6suJjCtoPypn22-Z2VuyUcNiV4S6Q2c6HIw1edP-WEVyJocN1pq25fL9JDiq88kfzVw6OwlSgO9fW6NIb41KwPX-__NOQN7y7T3SwjZEgDAVyH6UY9TtX9o3BFVQ_HgooQWyP9aJ4KYT2qRTr-2bK-DGPJAwjlD24_44xBiZunsdJQRveF5rzYSEx5RkbnftpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه عکس بسیجی جان بر کف فران تورس و همچین میمون فلسطینی رو چسبوند به پهپاد شاهد و بعد شلیک کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80951" target="_blank">📅 14:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80950">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قاطی "همون همیشگی" امشب یه همون همیشگی دیگه هم هست و اون "اطرافِ نیروگاه هسته ای بوشهره" که دوباره زدنش  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80950" target="_blank">📅 14:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80949">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80949" target="_blank">📅 13:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80948">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80948" target="_blank">📅 13:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80947">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKxOdsZR-FaOrQ3ryRR6RWtsZFHR_Nb1BuUr-jWZ4mnz-bTOgzFhuHoTOWwTZsGe94-eSiWOL2ikpOWtvC4EYOxca2fFwVc64qRRPSXzrnWV59Hm2_XLFIWrXzPy-ojVuYDg_jH6m_IohqUSv_hfT1catjMTRlZ4L-35FUdKtHtjo8ApgjDmseKOGDno_brB8xyZFrtDUfWaWKuemaavPq6_4ulxEjO1dN21zKkWnrvbhuNeAGq_12Y34gyKYFql99uHIIL1h4GjfADcN_RjjYVxa4Men5s-8ZoA3ljMFRtAGnefrx1FFeebORsZ2KXSDe2QzwMUB_iy5wJbJ9DLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید چه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80947" target="_blank">📅 13:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80946">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شات جدید یاس.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80946" target="_blank">📅 13:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80945">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شات جدید یاس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80945" target="_blank">📅 12:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80944">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGloriø</strong></div>
<div class="tg-text">رنگ پوست رو میخوای چیکار کنی داداش؟</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80944" target="_blank">📅 11:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80943">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVBqEdEn7yjjHNLFcR8tupu7CL6En-bviqkLSm6imLhgZgKuEfnxDo_2se-EB7vJDRB2Fqn13MNTV4bMch63kePdbVQfIHocIojQmsrK_89EL6M4ofarXQUHYD1xZuemhpludRtDLmgPPsjFQsUmovleVJQu9qgjPvMJxbfbAtRlCttDiLqdZUk1uKvL1LB-uHMDcKssSnZRc1VAxF0gFSqd4bLpTCbKCjscOVIEFCDrIt6FicVUwoUZXNmDF1D3uLr-lm3yfGAY1pd9Yo_dUloLDNZ7QSRoBYGN4J01gB9dhBI9FH1cmdjKf2Am32Ooj8AFswJKoijLQbfj2-BCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی، فقط همینو بگم وینیسیوس رفته عمل زیبایی انجام داده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80943" target="_blank">📅 10:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80942">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eac4416dc.mp4?token=XpUxIBvA51aggdEeh4J4AK5UOBlZ0zVuS5_U8BeRtrz3CH74l8SfRO_N7bugTQq7JObBBkIKoxwIQfON6Lr6XfZpdqrsg0-poo1WYrkSdKHr3ny1ZkboUbqcxqL9SCUalXfUEKpQ6C0HNSOi0UC034cGYrFTgJ2ipdAKoVrPsqCSNOAz5WTRqV1F6ebNpoFunhdHGxZcb8PBTFBnOSOyDNgPs8WvX7BiuSjhjIfX9Gz0WmBi9iUicIxtXJlnz-XVU4c0EBrVhlq0YvOD0jy4Qfz136oMIeM_0Vubx4kE-HNQjXyKBjRz0E1UUwgXkupA_U_edp5ASxqeyoHUt7jinQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eac4416dc.mp4?token=XpUxIBvA51aggdEeh4J4AK5UOBlZ0zVuS5_U8BeRtrz3CH74l8SfRO_N7bugTQq7JObBBkIKoxwIQfON6Lr6XfZpdqrsg0-poo1WYrkSdKHr3ny1ZkboUbqcxqL9SCUalXfUEKpQ6C0HNSOi0UC034cGYrFTgJ2ipdAKoVrPsqCSNOAz5WTRqV1F6ebNpoFunhdHGxZcb8PBTFBnOSOyDNgPs8WvX7BiuSjhjIfX9Gz0WmBi9iUicIxtXJlnz-XVU4c0EBrVhlq0YvOD0jy4Qfz136oMIeM_0Vubx4kE-HNQjXyKBjRz0E1UUwgXkupA_U_edp5ASxqeyoHUt7jinQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی عذر می‌خوام بابت تاخیر ولی سلام صبح زیباتون بخیر. 7
اجرای جدید پروردگار و غول ادبیات فارسی.
❤️
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80942" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80941">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8g3Dk2UwNPNbCA-QXt1OgzETqv3dyare84ZYF5M7ZV_ZiHgHMuBoTSEtW4Qt8DXtkq79MvGQJJEqrqYvRKoS11VvYgFa4jvcNlfdkRf8btYM1QdKyQAfaHCIrVBv8psiWm08xvGT88iC83HBpcDw4wHQkM11J_nWl8dB3DgqAMl0Ur3QFBI7cfkTqW5LS26tApTGeNr_pKwoB2riW8WFkQ_IeiKZzyw7AgexKgVtq729CGUPbAafhn8ybzzeUUo2sdyzsZwj6c1UZ06keZnlB8J25A1ompGaRnaJT28nk7botvCyBQ6DpGFLVPInu9f3bdJVyW5dt8NkGovKt_SEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
مجموع جوایز پنج هزار دلاری بلک‌جک زنده
🃏
🔥
با ثبت پیش‌بینی حداقل ۵۰٫۰۰۰ ریالی در بازی بلک‌جک زنده جایگاهتان را در تورنمنت ارتقا دهید و سهم بیشتری را از مجموع جوایز ۵ هزار دلاری بت فوروارد دریافت کنید. در صورتی که جزو ۵۰ نفر برتر تورنمنت باشید بر اساس رتبه تا سقف ۲۰ میلیون ریال هدیه نقدی به شما تعلق خواهد گرفت.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BLN
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
29
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80941" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80939">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هووففف عجب امتحان عربی زبان قرآن سختی بود.
احساس می‌کنم تازه عمق جمله‌ی عرب هر چه باشد مرا دشمن است رو درک کردم.
@FunHipHop</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80939" target="_blank">📅 10:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80938">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpk5m-3YyzAUBeunkRjJ_IRYTvXa-nc0qJQpQGNl_WBnut5yLjLvwxdq_dJoXRTUwFSgEqYV_pRQc3UB5LnNByEsviObuiFOF3jfZxMT-008ZBwWotkQlOXw9LRFUpfuql93GSDl-Bpgk8BjCTtWZkwQURcHUCZzYTNO8_JcDVAcgt3kQLJHYSTUrB5lxo62-aNxdCTPv-1FEGbm4MUmB7gOu8UlgJcP2O-rOXF3nG5um43eAuXv-FV4I_9sWBie9-TpLdiEZo4GqCMG2LMe2h67r0Ynkv__9GAmw0hrMjTc8Dg6NSjYGU42fCbeThFQgMhuLt_J43x2Q-DyxJ3gRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند سوخت رسان به همراه چندین جنگنده و بمب‌افکن حامل میز و صندلی‌های بسیار بزرگ برای برگزاری مراسم تاجگذاری محمد سامتینگ شاه در حال حرکت به سمت خاورمیانه هستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80938" target="_blank">📅 10:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80937">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY1CbA5rCvXpxQFbRHILHGebkVubTb0kLPeI9GGZVFbaP6S0FqTPGTEgyaHsPNmYae3x9QmUCzUgcUKV_3GcncuLjoAoAoAIvnvn5xDvRfT2AjtEXQn011XmWnlliuc3Z08Kh7dD7cjOhjUcqZlqPDD_KxpBCu0u2AS2jIxQbIvPg_DyObAbRwnIeUIfOYGfxU4d7y9cRsP1DDgtZhxgAsiyKwLl5C_XqfBE9QzNJ143EXJls31mbys9nNawrcrjeNbApb40MDf111psM9nIBgPxT-IhL2RkHIdXq-NtKCAxe5lS1JwHoIiCB2Y7o_ya7gP45dC5NRtwkU734jyn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی چیکار کردی ایکس هم دیگ سالم نیست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80937" target="_blank">📅 08:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80935">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apX8w9ZUdNbiEv5ZmlMw7uw29oIlTy3uq7FgXDxU6R6U-D7CwSqa4txix8ngcXBKKqfYKJH7RBzPQjl9vOT8aliIXkoeAEO4wBlo-7s2gZoOy0ueMSnWNzy7VW29e08KdKBS0jCqOVBjIxFzrkeZUYX1o5qBjr9Ax2oiSm3sp1MKGqYW7_vwl9yAMXpyhM_GXogsj_LruxvquSZPDiapfoVaCiVhH7cp2Lz-kWUJhkoPC73ySMB_phYwzAGQQ-BdMKRe5Jbo-Sl2m8Yu6Cl-wDi3otoO2al4JPRx2h9z6lkdMOck3l1U4EaOyFouFKTybWgUe2y5Xw8dkX2hT1Uwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WuhXtd1oaGpLWhEiZXIjEtpHzORyBehQZIRcBcqABGh4rux43EWeK5GTxrawcDILpHws34ztBGFNq0Z6pcb7KJt1Te1_6r6OyIYgQHociEWF7qW6V6DoHY4-7RvZKU6IZVn4P-gmzARfOwKqbwPl2292CUXmwH5px28NYM1cbqYmpEsIj26xzzSE3_lPsx9O8h119Xh-8geo-sfpKC2hBCbJ9yVaaJD1gzVeK-Y9XWbF3GL5Nno0iHNQZcAhI38u9t8SgUg3HrMnzyfcG-1eZn-mkjZ-36jhBxzCOCW2efWBDLXcDeLjF-IYtYL0ERYCidVOGVjf9IZjU237guDnNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنده به عنوان ادمین یه رسانه شرقی در برابر رسانه های غربی می ایستم تا حق ملت بزرگ تورک خورده نشه
✊🏿
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80935" target="_blank">📅 07:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80934">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AntU_FYlclgifK_lW_ZW_PWwtJlcctKNRuXoVKznHbDWuT1RaOT9ZHKUZr83tYs7NCHaogzhgXXAxS-frxfervo8tIn2y0sPAcRb2LZBjOc_bVmGVvO7Z_V56aSMIM842moeIb8vYIboIJyhzEpxCAp2_mrrjep4dMA7c0cs0QHuqy452eeecVuOx4sniwtCAeLElo2gaE3F9mplgG7EQtPS7R-4F59g-IeL2MwNOcasTMuqdrAWVJXqsVSEhLsojDPA1d80NCKpHwB_Pp5zMMagrS0Axcs4TM6BkPPaqj0LUPwSglmpuvOf9KTDfQjc6Ahj2Uv8UxfYL43GIsX3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا دید دیگه کار از هشدار به آمریکایی‌های ساکن ایران یا خاورمیانه گذشته، یه هشدار امنیتی جهانی برا تمام آمریکایی تو سراسر جهان به دلیل «افزایش تنش در خاورمیانه» صادر کرد و بهشون گفت مراقب خودتون باشید خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80934" target="_blank">📅 05:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80933">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxU8NP5nM9ibi_iDOvqsaTF71iwY72-V6d-cjcLl_6QfJfKWOd8q4-PDcmMFbpFb5c9ljPoyKTl49c8feuJr0RKnd0gSzWiavbw8zAGToX0lKuEraeaJ-AIYyyYn5pJ4auhhESHqz7_uS_nC2nIWXjBrA8Sar7hHP7Lb_JuGz7LZR9aU2u6vEzlUh2JZLahvACaiAEUnFRLgUaVAMsVgiX6vduHiakW8jVuyjykzCpSx13fHKiJ3hNzB7kCBki0xM_KM1xzgudiKxSZ2ZfX8BaSrXt2q3XU_AK4lnpqWObvQYGKoMsjUyGbi23jL20kH4Acq8izNtgHauxcEZE4ttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری ترامپ از ایفانتینو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80933" target="_blank">📅 03:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80932">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چرا قبل مهاجرت کسی نگفت که خارجی ها چیزی به نام تعارف ندارن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80932" target="_blank">📅 02:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80931">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تا اینجارو هم نبستن هرچی گیف از ژنرال ساخته شده بفرستید
ما تو این جام 3 تا زدیم و 3 تا خوردیم و من تو کل گل‌ها آروم بودم؛ حالا سرمربی آرژانتین همین کار رو می‌کنه و واسش کلی کلیپ می‌سازن، پس چرا واسه من نمی‌سازید.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/80931" target="_blank">📅 02:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80929">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جنوب
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80929" target="_blank">📅 01:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80928">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">برنامه عادل فوتبال ۳۶۰ بخاطر انتقاد از تنها دو تیم شکست نخورده جام تیم ملی ایران بسته شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/80928" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80927">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شیراز و اصفهانو زدن
انفجار در شیراز خیلی شدید بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/80927" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80926">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرنگار فاکس: احتمال اینکه آمریکا دوباره وارد یه جنگ تمام‌عیار تو خاورمیانه بشه داره بیشتر می‌شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/80926" target="_blank">📅 00:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80925">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یادش بخیر پزشکیان میگفت پایتختو تغییر بدیم و ببریمش تو جنوب به یه استانی که نزدیک به دریا باشه
خواستم بگم سلام دکتر مسعود پزشکیان، برو دست اونی که باعث شد از این تصمیمت منصرف شی رو ببوس وگرنه الان بگا رفتن تمام امورات اداری مملکتم مینداختن گردن این تصمیم تو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/80925" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80924">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امشب خیلی بد داره میزنه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/80924" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80923">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آمریکا بدبخت فکر کرده مثل همیشه با آدمیزاد طرفه
سخنگوی ارتش: اگه آمریکا بخشی‌از خاک ما رو تصرف کنه، ما خاک خودمونو موشک باران میکنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/80923" target="_blank">📅 00:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80922">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سنتکام: همون همیشگی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80922" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80921">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قاطی "همون همیشگی" امشب
یه همون همیشگی دیگه هم هست
و اون "اطرافِ نیروگاه هسته ای بوشهره" که دوباره زدنش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80921" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80920">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه سری منابع نسبتا معتبر عربی خبری کار کردن مربوط به اینکه ایران میخواد یا خودش یا به پشتیبانی یکی از گروه های نیابتیش به کویت حمله زمینی بکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80920" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80919">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80919" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80918">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سنتکام: همون همیشگی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80918" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80917">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWN4A5_04ig0c3wGcLzhelkMcYQzOpaU3RVW5ZX6HYGUU9-f7FeadXB-gkSAN2V3U9oXUi5iieccbemysy71D8GL2QQGX0nZ7xMbWy2pPrMX7Jzpv1gQiaGeYpEthzYvZ7KeZK3AE9I6clFQri7hcx59RGv8wf4DtlauaFcx77Dv5bUlZfJTp4fDsKsDKsseog9L8lewe3gH-Nlgzv_6q4lP237h2cjgQ1Kc4KPiOIIgrfdaiJpYLi950q4HRq03KxfFsuWBzH_SulceDQ2ouUcFOla9tzg03_bVVIqhxr6siMGEblIqMhld6w_NpyDLDyfHRokzfleB6dbQyZgoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور آرات حسینی تو جام جهانی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80917" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80916">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvRXS9OpAK8km4wft-vIlSTx0J4DQnnrFXatrumU-8ESYL66mEA5xgS5aP0JYhnDwfJNXnjRYT5jBv3wc0yseA7MvkuxLWMawrCeROdwXiUtV8JTyebnTXXCntAR1QXfJXlHU545vw9HbJzozWK7TRLp39vWiWQYD2wH9aiVfA0_ilOoqXW1Q0Af3W8Yavd8Khw0BH4XXN4UrwUEY9U1EO6OJF4XxOFSxB4OrR6gtwAUjSX53MAL8d4zRS98zoaqSqchBkpaLMYCGRJ4mHEcHMz90PNP0sWBuwkLVhJHu2rJDAV-ag6tkPn8M7mOWdCjPBfIkrfFHharY5sCWfoN3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
با نایت موویز بدون نیاز به تهیه اشتراک، فیلم و سریال مورد علاقتو تماشا یا دانلود کن!
🎥
توی ربات نایت موویز هم میتونی جستجو کنی، هم تماشا و هم دانلود، تازه مینی‌اپ هم داره که اگه به فضای سایتی علاقه داری میتونی از اون هم استفاده کنی همشم رایگانه :)
🍿
@NightMoviezBot
🍿
@NightMoviezBot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80916" target="_blank">📅 23:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80915">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j22Sg1RjA6WmB8-mLvpYeJlqmflJmxbBM6A4cziehGOwxLjyCz6uW2a2txNGWmweCYz0IrsThWCUZlTpdatv0m6MB1O61qa0XthbF1pI0c_FpmhFl31z4tSmoPdsR92DbBcJBS31JQLEfaFwEzlJmzevAgDjgwUYlCLjNk--K3BH3EhxCm6iL8qzWMz9XE9E1-hB_I_WyOGse4HrFYDrS3bOz8WlAOdprZWd92RIia6_5sNxQWWJjKjsLM6M0GWnXir6586HFHKcLkfN1eb8-zOiTopmLZ3sXzH2QwfOfi8xSkMvbIAqUVS3HfdjZW8_b3v8U5nH9xKgDrH6yaKDQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنری که یامال گرفته دستش
شب هفتم سال :
پارادس
🆚️
گاوی
(این به یک رویداد خاص اشاره داره که در اسپانیا برگزار میشه و شامل مبارزات بوکس نمایشیه)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80915" target="_blank">📅 22:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80914">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfLWUOG-PAly2yuWTXs1CiPsZp8LVJ3KUUpq2oV5aAOX_eY8T5qUAUVI_yPB8n4Bvqmjmu5-XJvuMMeG4amVSoAZRSUuvUCucvATjoOZatl2N2uKnFkDsx_RIOISVW8JXQ4NU0EocDNz-i5Mpuj3zEecT2_ZOy3gamMFkb8tEvLrPbN1TE8x5a3qolxNUqorxAknxmRq4j_bgkOENjYcSzdaA8mJL25Uo8FeoyC8IgOEpWlBCqb6EQOIFe91RV0cutUsfaAWeZPqdLjKRwtKlbtnm2difIrliLQ_eg7GwAClJkP-Pr6QfiTT5gfqClCUbUhOjpYV-WbwoHE4HI4Cog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید پروردگار و برترین اسطوره تاریخ فوتبال:
شکست دردناک بود و زخم‌ها دیر خوب می‌شوند، اما با تمام وجودمان نتیجه را عوض کردیم. حمایت هموطنان و تلاش تیم باعث شد دوباره جزو بهترین‌های جهان باشیم. امروز قدر کارمان را بدانیم؛ این تیم دو بار پشت‌سرهم به فینال جام جهانی رسید. از ته دل از تک‌تک تبریک‌ها و پیام‌ها متشکرم. توانستیم مثل یک کشور متحد باشیم و افتخار آرژانتینی بودن را با هم تقسیم کنیم. همین‌طور به اسپانیا بابت قهرمانی در تورنمنت تبریک می‌گویم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80914" target="_blank">📅 21:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80913">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جام جهانی 2030 با 64 تیم برگزار خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80913" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
