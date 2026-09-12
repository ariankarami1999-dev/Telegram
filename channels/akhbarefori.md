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
<img src="https://cdn4.telesco.pe/file/ceNHDQbfAK16gq_FGVVgh5iLUnT-tFU0ZzLRVHeyPA1DCRJi8n-G6ZzDz0WoO4Vtm-ohqK14AYDL3HEtW4MyPkZQUrx0wXOKoWS3AZ2bjMyJcTPehJ-lGdmizZeSdFear0oQDvtX7-VMG7NZKSEGuZ9YVP7iAxUNjHm-Sb-KrxpedW463hi_-ckPyDu-XDLU1HpMfkAODuRiMolHmR9kqQwhtfCN8JrNXoGIe03P4NUdSGcEIfr3YIQPz1LAiEHYDZwR9TRAuNnmHmlxpdxRpYdQD2DM2bW1_nt3G2M9ubH5jSPek7UsHH5Ct5avkE0c19mGsnnOQZwc7ScD0FSuwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 14:30:57</div>
<hr>

<div class="tg-post" id="msg-689230">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/689230" target="_blank">📅 14:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689229">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0NRQR_wVV_6-RS_Ky4rFvC5aIhOyQk7JBFpIOkcqXPShvCcl2uD97wE8Py9zpJdRHDTKXq_B-BpVEssHCGHVSHySw7PbjgiqmihZIkueLn1_0TcRgSfLOi9fODejIlNFliUql78cVDZj1CrFV5_oEQpxQU5TLbUO7FO9pB5HOxtI4ZYORC1OeX3aMxk3mwp1EesXzyq0UICLmfX_ueqagcdBWO2HoGaVSGinPtNpxixf7X1eMwKJEtPfigiTHFBa4rIO3Xz0td-CCK-j26WRNdcGofo6i0-B7SMFvildfKE8H4ZXXZNcveI-KO4q4yPrxDWDDBeEYJUBXX6k0PsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمایت و همراهی مدیران وزارت نفت با شریعتمداری مدیرعامل هلدینگ خلیج فارس
🔹
اطلاعات رسیده به میز نفت از همراهی پنهانی تعدادی محدود از مدیران شرکت ملی نفت و زیرمجموعه‌های وزارت نفت با جبهه محمد شریعتمداری حکایت دارد؛ مدیرانی که در ظاهر کنار محسن پاک‌نژاد ایستاده‌اند، اما در پشت صحنه روی شکست وزیر نفت شرط بسته‌اند. انگیزه اصلی این همراهی، نه اختلاف کارشناسی، بلکه نگرانی از موج برکناری‌ها پس از تعیین تکلیف مناقشه هلدینگ خلیج فارس است.
🔹
همه این افراد به‌ دلیل حواشی، تصمیم‌های پرهزینه و عملکرد سؤال‌برانگیز، صندلی خود را در خطر می‌بینند و بقای شریعتمداری را سپری برای حفظ موقعیتشان تلقی می‌کنند. گزارش‌ها از تماس‌ها، انتقال اطلاعات و هماهنگی‌هایی حکایت دارد که جزئیات آن پس از تکمیل مستندات منتشر خواهد شد. میزنفت تأکید می‌کند سکوت فعلی به معنای بی‌اطلاعی نیست. مناقشه خلیج فارس سرانجام تمام می‌شود؛ اما پرونده مدیرانی باقی می‌ماند که برای نجات صندلی خود، وارد یک قمار پنهانی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/689229" target="_blank">📅 14:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689228">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI1tKCWsb31U2DMU8Z2dJI8p9QKAm9gTetogsE_esP6xgJ1zpkefsBk6QPARc8_u4czG-RSXhrapcil75cJIbrktAS0OfjX7HFlZrWMR4uei4YrFMSbZIcO9QI9dkDJVvsUMnGGX3JlPXldld7KLi0UZaH-yNXWoxQVVNvGKzMrzydHKH8lvMyW3yiYeIc4BHPNe5ltAfc4vfIRhfi7AM3dOJHOBU_mFJWhkE0zDlcl3PsXbXPBNZLvC-Dud2gTVGs6U5p2VdQXBF-Q8089Wsl_8IntfbrsQOTcPQrPgGh5eOdT1MTEj6tkW7bqotRCrDH7czTCxVOv8owPRCF83hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارین افیرز: جبهه دوم ایران پیشروی جسورانه حوثی‌ها، جنگ‌های غرب آسیا را دگرگون کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/689228" target="_blank">📅 14:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689227">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olx8dGSKx7rfFEN7hint_0rZpSLgtCOnI_CQX3vXfIXe6HfmVpEm0Ob9oQNTvRa0sDvb9gGbzn7EHQCyAYcteRS4rQFGYAiHJkuLLqLwj2OvjWmjQgEex6l_YKUClw3SB5UZ_KjX_Lp3Ix3JWBi8X51bWNCE_5fRxRZf99BOwR_KF0usi_R5P6qBJ_W9EwYTeDYYdO0Ho3FXLq4GZgI14-fExIbNfrAThWVX7dOgtMCSlf4RyM2ASSo-4JPPoGl4EaEcWGPulp8RNC3COy_i6bUmVyS2T9GFlYQpoiS7qFGvH4ohZuPy94AXju4ibCwQY_KpSsvd4HDdeqfwRxdKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت ترامپ درباره امید مردم ایران
🔹
ترامپ توییتی زده‌بود که در آن ناخواسته به ترس آمریکا و رژیم صهیونیستی از امید مردم اشاره کرده‌بود. امیدی که با انکار هرگونه امکان بهبود، با بزرگ‌نمایی قدرت خود و کوچک‌نمایی طرف مقابل و با اختلاف‌افکنی و القای فروپاشی داخلی دنبال کشتن آن در جامعه ایران هستند. واقعیت این است که آن‌ها از امید، بیشتر از بمب می‌ترسند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/689227" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689226">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
مقاومت عراق اتهام حمله به تاسیسات انرژی عربستان را رد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/689226" target="_blank">📅 14:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689225">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHaMxrp1VMlQZQVW_klMi2xwzYkMa4KloSEBbc8XkQlXmWohq_6D_zUbXyu57Sb-31eFnKzfvv2gHPeaO_TBv5akYOjQo80TPCBg3vdz_3iyuwHn2KQB76zUsYKrj5d4TGlom1MoF0t2-VeFqnESlTb8O9fXb54mAo63qCFkUByNXpv1auUVQyzQV-ZUkyrauwSvdjxWXFvgIPhhvy8uHslfWhUJ4ESuvW-WQR_26AyWAetQI9xUvk2gNhAG13IYv6JkffDB0gZlwoLH9pPP6eq4oTYlBADtgJon0-MUp3q0Q7_vPGkqiiWsvtWApYyZ4Ga5y6FHVKix21pCdRJB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با گلدوزی می‌تونی خیلی راحت لباس‌های لکه‌دارت رو کاور کنی
🪷
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/689225" target="_blank">📅 14:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689224">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای ترامپ در مورد حمله به خط لوله نفت عربستان: به احتمال زیاد ایران مسئول این حمله است    ترامپ:
🔹
جنگ ایران خیلی زود پایان خواهد یافت. جنگ ایران احتمالا پس از انتخابات میان‌دوره‌ای پایان خواهد یافت./ حوثی‌ها نمی‌خواهند با ما بجنگند‌‌. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/689224" target="_blank">📅 13:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c005ed5d.mp4?token=ZZ7Sb2gAy5Us1jJXonOvhswOTIxpIGS95GskyScvkq2x1HUEEdI2jBZ3r08ihwiey2SI7nxzds6Srs9ckU-2-zxx_gp8ZVSyGA1mhv2W4K9gjLqYHv51-w5aV6TGOOcJDjsmot8nzsl85LVKDtN_g9hO6Tdp0V21152M23Sn-wfgAnk8qo-evp-Hn88k0NK7oleuG80uw07_nXszbg4rJN4JFJnaP20s7UFlKoMttsiyuEVuwrUZBuCLuIqCZOAjDSP33XKBu1siYvnRcqHNwZMpHr41tj2zc4orgYu2KAC1aaiZfYWO_cssrNfSibuh6CUb61eC19IG53RskZl91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c005ed5d.mp4?token=ZZ7Sb2gAy5Us1jJXonOvhswOTIxpIGS95GskyScvkq2x1HUEEdI2jBZ3r08ihwiey2SI7nxzds6Srs9ckU-2-zxx_gp8ZVSyGA1mhv2W4K9gjLqYHv51-w5aV6TGOOcJDjsmot8nzsl85LVKDtN_g9hO6Tdp0V21152M23Sn-wfgAnk8qo-evp-Hn88k0NK7oleuG80uw07_nXszbg4rJN4JFJnaP20s7UFlKoMttsiyuEVuwrUZBuCLuIqCZOAjDSP33XKBu1siYvnRcqHNwZMpHr41tj2zc4orgYu2KAC1aaiZfYWO_cssrNfSibuh6CUb61eC19IG53RskZl91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاربرد هررنگ چسب برق رو از زبان خودشون یاد بگیر
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/689222" target="_blank">📅 13:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
از ساعاتی پیش یک تیم تروریستی در بخشان سراوان توسط نیروهای قرارگاه قدس سپاه محاصره شده و رزمندگان در حال انهدام تیم می‌باشند
🔹
گزارش تکمیلی در بیانیه قرارگاه تا ساعاتی دیگر به اطلاع مردم شریف ایران خواهد رسید./ صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/689221" target="_blank">📅 13:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
عربستان حمله به خط لوله نفتی خود را تأیید کرد  وزارت انرژی عربستان:
🔹
خط لوله نفتی شرق به غرب این کشور در ریاض و مدینه منوره، روز پنجشنبه، هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/689220" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ff2d89ba.mp4?token=c5sJdPTWkrPzE_lGzsnGhDEXaDs8ugRm91Y2ndpakFgTRwIsiomUzh3jLEoBcezM9zNIDtQJaKmp6SOS3cib4OTGkSNN75l-AlA9251ZH8TI5mxLsr28yFxFXj1zcJyPN8DsfTmCwAaSyaMPaW7jcgf5cNXCcqhBfybzvJ6CosQakHpCejZkiLmDn2mta4rNoPJpitCPigL6_W3ethkE3fzIoxcI53u4l-IVL7aLIwsqESYf4-Ar3yUosfsn88MdfDMiVkgXLtfxCz3mhRXlCnK63P_ofQ-g6Y_ea9wutRwqmWeMftNbIWsUiNuzDBMr89gHRrKEblAUfZvD5WxtQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ff2d89ba.mp4?token=c5sJdPTWkrPzE_lGzsnGhDEXaDs8ugRm91Y2ndpakFgTRwIsiomUzh3jLEoBcezM9zNIDtQJaKmp6SOS3cib4OTGkSNN75l-AlA9251ZH8TI5mxLsr28yFxFXj1zcJyPN8DsfTmCwAaSyaMPaW7jcgf5cNXCcqhBfybzvJ6CosQakHpCejZkiLmDn2mta4rNoPJpitCPigL6_W3ethkE3fzIoxcI53u4l-IVL7aLIwsqESYf4-Ar3yUosfsn88MdfDMiVkgXLtfxCz3mhRXlCnK63P_ofQ-g6Y_ea9wutRwqmWeMftNbIWsUiNuzDBMr89gHRrKEblAUfZvD5WxtQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در واکنش به تحولات مربوط به ایران مدعی شد: همه‌چیز خوب پیش خواهد رفت #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/689219" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crjI-UXVowTDn6eVA4e6gXixAOVXGtIe9L9j1lZ7Tvo7RyqOwX-AjFrW8Zb2z4yDWv68MbO9TxihB_mCdZb3YSqYbGr9GcvP1zJL8S47FzDjA4A27noFLYK1Sd1JNnHXCriObUXEO8zmMdeeUUrY8r7wYihbk6nt96iRSa74rWEkn3E0H_61kHMqyQNpPRkp_fFmw-69IRFe3Xgher-cbVI7ve9VdbyQXOQL-77xnzupHRyzI91ZN0EGk8tnUvfw9H1JE6Mg5QKYTiVQAg0UufxpM63xHNubKkJs5Or8wzqxTv-ej_xJR4iX5pm9l5gV4I6LAdlBz5uNHGyTddFTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشست مشترک فرماندهان ارتش و سپاه پاسداران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/689218" target="_blank">📅 13:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689216">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl8IQ5pUandFw4xsFrn8VEURuZmicFMdZAN0jRlxke_fLGkMfWM1UYEGnGUWwp04mH4c-75zT87rdw3fkLl7wQ4vPwMkwmB1TESO_mw0j044TnUim-O3y_o-Pa3khYzSFnnduvknoLy8jL5Ggp7D08l_7CXcMS7Ngu8cfDBnAsa76XQm22rMnug2utOpFUHE5uqA5Sx9MlXwK70IUslxaHBED-joFGhjzM1R-9rN3dyYK3I17sQ7niAwAXUgNhF7thBOZh3cJ7Cl_gRp3xUKM2dIpOWp7uGa3dU5AH6gn0dfpSsUbnS9bMAsmVk3BVPUdML0_2WiXFEY8qzm9KGs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e10581af.mp4?token=XFgnvmrt6-x6zakvMTcx-FKAKPIeQMCuWYhxLAcBROyshAzza92fEP53yvJEgpiH7HWMXVyEePsWkxgu7HqEoyDsknYGteWaqtuIfNYL6kzz2IeZ9Zkbzg0MTOcDxX9nXKfD901yif1UQUiXZLLjdRXYf0F4OTFxN9rNqoOZkiH8_v3m_an4D_pW7KlNXjeuMycFkO27KoHBz8Y6UGiH8AeiaKXHF35ctoMfd27_d6Q8QJ0qW6Dk_DQT1VxBMdwdmhg5TGgj7UGWiRMz6ALX3UAUVCX-7bdjFrOAQbQo9DmK1mAhVMW1n6RKjZZCWONuTgC3LSQMKsNKVoiuHxSHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e10581af.mp4?token=XFgnvmrt6-x6zakvMTcx-FKAKPIeQMCuWYhxLAcBROyshAzza92fEP53yvJEgpiH7HWMXVyEePsWkxgu7HqEoyDsknYGteWaqtuIfNYL6kzz2IeZ9Zkbzg0MTOcDxX9nXKfD901yif1UQUiXZLLjdRXYf0F4OTFxN9rNqoOZkiH8_v3m_an4D_pW7KlNXjeuMycFkO27KoHBz8Y6UGiH8AeiaKXHF35ctoMfd27_d6Q8QJ0qW6Dk_DQT1VxBMdwdmhg5TGgj7UGWiRMz6ALX3UAUVCX-7bdjFrOAQbQo9DmK1mAhVMW1n6RKjZZCWONuTgC3LSQMKsNKVoiuHxSHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه سفارت ایران به سنتکام درباره تنگه هرمز
🔹
صفحه رسمی سفارت ایران در زیمبابوه با انتشار این ویدئو نوشت: «وضعیت سنتکام وقتی اتفاقات تنگه هرمز رو رصد می‌کنه!»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/689216" target="_blank">📅 13:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689214">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مدیرعامل شرکت شهر فرودگاهی امام خمینی: تمامی پروازهای نجف و بغداد از سوی فرودگاه امام خمینی در حال انجام است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/689214" target="_blank">📅 13:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689212">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2dheZCxPWAE55bXgD4adi5MJ_2ykiqM9GoR8AlPxh4hhtEz2FRzeZWGCkDXAgrV2KGd60eX4VVHiiq8apip70zLaQhQY17lWggwFBmRB4h8DCDwnQ9nylEsd0J22_3t4O-t28vroRukH34aHHwb2jj9KW5N_DiYXIO6fCpwlthl9AsEx1D80OWmA_7fst3ivnwfNXh1FN0EcurVARg0Y3e05TnJASwBcpU3a7eDXf9O5EanyRjZeCKwWAoQ0il3nTrNfeS2oaal9R9gq7CYqJlPEQgTVkQcf5GyWAckOL3cV4MFmz-XmZc2WrRznJQfml6e_-kqZvpEvLlfo8I54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_خودرو
| قیمت روز خودرو های بازار کشور؛ امروز ۲۱ شهریور ۱۴۰۵
🔹
بازار خودرو امروز در امتداد موج صعودی هفته‌های گذشته بازگشایی شد و بخش عمده‌ای از مدل‌ها همچنان با افزایش قیمت همراه شدند.
🔹
بررسی روند معاملات گویای آن است که بازار خودرو طی یک ماه اخیر، سنگین‌ترین دوره جهش قیمتی خود در سال جاری را ثبت کرده و شکاف قیمت‌ها با نرخ‌های پیشین به شکل چشمگیری عمیق‌تر شده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/689212" target="_blank">📅 12:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689211">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85b001aeb.mp4?token=X5PCRBrCaQH4cZk35bkqfDZfT0Da7xQQGmkyu339ifu7ZlufQylW6BnU6_n3IbAXmW-0F442XJ6oCx0q3oYQxyIySANLygR2MdX3x9gkuHA9zKb_3xMU_k9Dtj-0eDS-u5SSorMgPHT8x1ZhCNgw_TZKtLC-stY0d0tOJXx4TSWNfNwpB0alQtbmECIXixjiz4wiqyw0wvRaFwyz2GOSjPed2wJd64j00XbjWFCLFFdYZEkNa1dOdjGF4_a4k1jVvEQ8PIanW07ZOFg75gQltP4C1s6G_ZyJrhOrMhgGVirpDlU9CpQjN3hnt_lUeToXK5Or27O-yPXKJucQ8VvfMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85b001aeb.mp4?token=X5PCRBrCaQH4cZk35bkqfDZfT0Da7xQQGmkyu339ifu7ZlufQylW6BnU6_n3IbAXmW-0F442XJ6oCx0q3oYQxyIySANLygR2MdX3x9gkuHA9zKb_3xMU_k9Dtj-0eDS-u5SSorMgPHT8x1ZhCNgw_TZKtLC-stY0d0tOJXx4TSWNfNwpB0alQtbmECIXixjiz4wiqyw0wvRaFwyz2GOSjPed2wJd64j00XbjWFCLFFdYZEkNa1dOdjGF4_a4k1jVvEQ8PIanW07ZOFg75gQltP4C1s6G_ZyJrhOrMhgGVirpDlU9CpQjN3hnt_lUeToXK5Or27O-yPXKJucQ8VvfMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در واکنش به تحولات مربوط به ایران مدعی شد: همه‌چیز خوب پیش خواهد رفت
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/689211" target="_blank">📅 12:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689210">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729f8f860a.mp4?token=HgF3C4PdTYRQZ6VdTmILccsSadsMbkNPDERoee9UtI7_a6zaPvfj0iscu2MSgsyxLcI95keszv9lnLvezXRbth05GHSRHSkHGdGHKqYlkAHoAcN29J_HtQDSj_GT5r5bQwQ1GCSSBZZXpx9kN-Z6tHx3W5VVHJ7-7586HIS2DyuchFgNs0izwqAFdiCdRLFF64LuhNoDKNg4v4Xp6QuRRAFfRlhYclxYJWAIn1ybNzs2LWiCabbILLM4xiGXAeqnyB3qcS_kdFgXjnvEnEdo03hkIt12kj39Po4nn9y8NqieHDjyImpEpEHUXk1T0sGp6AujTAvvYdJwRCT4oxvWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729f8f860a.mp4?token=HgF3C4PdTYRQZ6VdTmILccsSadsMbkNPDERoee9UtI7_a6zaPvfj0iscu2MSgsyxLcI95keszv9lnLvezXRbth05GHSRHSkHGdGHKqYlkAHoAcN29J_HtQDSj_GT5r5bQwQ1GCSSBZZXpx9kN-Z6tHx3W5VVHJ7-7586HIS2DyuchFgNs0izwqAFdiCdRLFF64LuhNoDKNg4v4Xp6QuRRAFfRlhYclxYJWAIn1ybNzs2LWiCabbILLM4xiGXAeqnyB3qcS_kdFgXjnvEnEdo03hkIt12kj39Po4nn9y8NqieHDjyImpEpEHUXk1T0sGp6AujTAvvYdJwRCT4oxvWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/689210" target="_blank">📅 12:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689208">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1985c52952.mp4?token=RyFQx_dcziI07EXs43mCydzX0DDsLEXLWK6j4MU04Tnihvi1AVL9ayUNh5bUAIFB5vrYyO1GwrOoqzxE41Yf1oZyPUgNLSjEbWg5WyQbTNqFytVGyF6ZyhBllud9_bWg9ml7j_-kkgBw9Pr2ufXF1XuSvhCsKETTqCtFB37oX-rYiXw78tRTttJnhUNu_uC25cN3ujQ7Wt4CuNG7dCtEHXRODGfONHo68UOiksd_xMDDanlXiPSDNZJg2FE0gNz6LMBKl0jXQ_ZqUgWnZrteVgl2QxGGIbD4YIluC1o8lQcHJg09_mBza4-A4h3XxiyO1X0AsNQLqu7BuSYUu736Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1985c52952.mp4?token=RyFQx_dcziI07EXs43mCydzX0DDsLEXLWK6j4MU04Tnihvi1AVL9ayUNh5bUAIFB5vrYyO1GwrOoqzxE41Yf1oZyPUgNLSjEbWg5WyQbTNqFytVGyF6ZyhBllud9_bWg9ml7j_-kkgBw9Pr2ufXF1XuSvhCsKETTqCtFB37oX-rYiXw78tRTttJnhUNu_uC25cN3ujQ7Wt4CuNG7dCtEHXRODGfONHo68UOiksd_xMDDanlXiPSDNZJg2FE0gNz6LMBKl0jXQ_ZqUgWnZrteVgl2QxGGIbD4YIluC1o8lQcHJg09_mBza4-A4h3XxiyO1X0AsNQLqu7BuSYUu736Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند جالب برای رفع بوی بد و عرق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/689208" target="_blank">📅 12:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689207">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekl9WI08H2kq2Sgq7gs90o5oZjxs5a3r5EyOL15uzddts4_s66mRwN9kEcyXukmwzqUzn49RBNZaj-Gqf3UvjeH---qmlpg-v-Dmngqd0DVs3iGBZejkCrKGMs_qArswujzaPbA7wy301BdfXywbP5FMDhAZnBxLqvJ3x-zkEX1APGVjhdbW_WBgfChgDOPwNwM8dZKR6-ER5Q1Az8sG5AVM979L_GU-MbiWHSeOoX-UcWhfB0RbARt_1mmDwWlIzbgK_qynQuP2MohoLDyU2RTrVQQzsAJt3_oj-m5U4qpq7xourlG6gozvUbYBb_NITKZSkpdjNGf8fp1jNypLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرسنگی به‌ عنوان سلاح در محاصره پاریس/ چرا ترامپ نمی‌تواند تاریخ را تکرار کند؟
🔹
امروز ترامپ سعی می‌کند از طریق روش محاصره، مردم ایران را به جان هم بیندازد اما این روش توسط او ایجاد نشده بلکه محصول یک روند تاریخی است که ریشه در حوادث مختلف دارد. یکی از محاصرات تاریخی که احتمالا ترامپ را به سمت این اقدام خبیثانه هدایت کرده، محاصره پاریس در سالهای ۱۸۷۰ و ۱۸۷۱ است.
گزارش تاریخی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244515</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/689207" target="_blank">📅 12:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689206">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تکذیب تعطیلی مرز مهران  ‌فرماندار مهران:
🔹
مرز مهران باز است و فعالیت‌های مسافری و گمرکی در این مرز برقرار است و هیچ‌گونه تعطیلی یا توقفی در روند فعالیت مرز با کشور عراق وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/689206" target="_blank">📅 12:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689205">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6bd17689d.mp4?token=q5SQTtl6GNCzOToIb7SEMn3DbFhpJylVeG-slvJ9P2Xk3pl2kzGuAKhFbXRN0q1cAW62Ju3NPuyagpT20x_RMV-rK7te12PZzA9nCIxc-BJoexYZTFyzrmOI6OZaEdla9jSM_KWAvURvxgiJjg11k6SgBPcz1XsU5-8Tphod2Sj2vT3fR22C5674pjNuKUfWcRrKWuXw2PVqrHcncxXQ9d0xT55rIu68NigNU2AWHkHQ61ltQ5M_PJHg6Eyz3QGKhTNYR59Yd_pdFwZOtyt8NAvNQ20N8dUmoQ1A6ZKdlBiDYKYNDX54wSr5RvoyWXsMDLMUpJpzkRSB7PLMjhtEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6bd17689d.mp4?token=q5SQTtl6GNCzOToIb7SEMn3DbFhpJylVeG-slvJ9P2Xk3pl2kzGuAKhFbXRN0q1cAW62Ju3NPuyagpT20x_RMV-rK7te12PZzA9nCIxc-BJoexYZTFyzrmOI6OZaEdla9jSM_KWAvURvxgiJjg11k6SgBPcz1XsU5-8Tphod2Sj2vT3fR22C5674pjNuKUfWcRrKWuXw2PVqrHcncxXQ9d0xT55rIu68NigNU2AWHkHQ61ltQ5M_PJHg6Eyz3QGKhTNYR59Yd_pdFwZOtyt8NAvNQ20N8dUmoQ1A6ZKdlBiDYKYNDX54wSr5RvoyWXsMDLMUpJpzkRSB7PLMjhtEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: موشک از خاک یک کشور حاشیه جنوبی خلیج‌فارس به لامرد شلیک شده/ ایرانیان برای همیشه این مسئله را مطالبه خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/689205" target="_blank">📅 12:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689204">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/689204" target="_blank">📅 12:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689203">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ee7cc5f4.mp4?token=QvmDBCm8pKT2dYIcigfTdB9DYrtoF-9b1QnoLPNy_Qnw8AtWJqw2PAakPDI4vtqMiAXyemeHNv4CCWUcyrcvLP8pfBJVlG1ip2J1GlSN5rr9ztW4DI3nFABU1jOdaxBsLLiL0-9zK-IRTO351zWWBiUnCWZN4dSoUQOV71Vez8LbZNgPEaxRripVFf9H-HiC_DaNEeQxZ5kP4KpaKtX0Xp3w4t4oVbHGtAj1uJHq92AGxoWOmGWCC8X24a6ANn83jdWYhtXOMHJyBJ7PZaVdqwbLmEoJZ1TygSL3Mg9HsvpjhOZ-gWSeXOt7udZVJgfoaYEhG8SH5NuQlzh4YH5xiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ee7cc5f4.mp4?token=QvmDBCm8pKT2dYIcigfTdB9DYrtoF-9b1QnoLPNy_Qnw8AtWJqw2PAakPDI4vtqMiAXyemeHNv4CCWUcyrcvLP8pfBJVlG1ip2J1GlSN5rr9ztW4DI3nFABU1jOdaxBsLLiL0-9zK-IRTO351zWWBiUnCWZN4dSoUQOV71Vez8LbZNgPEaxRripVFf9H-HiC_DaNEeQxZ5kP4KpaKtX0Xp3w4t4oVbHGtAj1uJHq92AGxoWOmGWCC8X24a6ANn83jdWYhtXOMHJyBJ7PZaVdqwbLmEoJZ1TygSL3Mg9HsvpjhOZ-gWSeXOt7udZVJgfoaYEhG8SH5NuQlzh4YH5xiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد حاجی‌پور، ملی‌پوش والیبال ایران با تماشاگران برای نجات توپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/689203" target="_blank">📅 12:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689202">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6242363ef5.mp4?token=of103OhIAT7nc1LRVEhbjTALxtWPZV6fp65Iw_AN7vt8G1L3xvJ9Xcpt0TDt8ml62AJVvbAsE-TqgG2okITnsMYmlg6-_WiDf_vZFIMbYi11HYgQc8ifO6Skdm9NQgBW7sfdS1TxXMuau1AlUapMk48dHM9y4CBZHwfNaP-HBk8yiocLIbrnUs9WVgI6aZODJ3P-0eh6_CzhPsJ0cSSmKfUeTybcs7-ipekKckCYK5IO4PwfxmJfpZTUx-H6LhSaP_1Ueftjr6AfZD3czPvIsff1k4c511QeQaywoPnhIQs4WNGnj_yafZWltuij2-9bTdC3-73wfvULencLDx3m7W10p6T-Iv4eO0h-tC3J4MLU7_-m5JTMQgJF-zKJyEPZQFfdPlC-KovEmsIJWXlXRqe5ntgyPP9u2mkFUCM7NIX_6o3EEmwbVY41VwG-chDs4pUwCUV597riwJ6oYKrMgrylOc_CgREfqMLYrsJqpSP-FKYUIQuDZvcWnR7Rnr_MnXEgkg29Fbu96XExRSTGI8T8wIsREsZdlYygRqILSxewX2f2j5ApNhJZyWnDIOjqkezak1E65lXUj9RuemL215VWDlTBEMPbOMS30PgjI8_snVaWhrewvxI7xJdr6S-MSZVcsj7D2Vk1lqXo9dLvSypPohygcW9_tLGpVV_kOzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6242363ef5.mp4?token=of103OhIAT7nc1LRVEhbjTALxtWPZV6fp65Iw_AN7vt8G1L3xvJ9Xcpt0TDt8ml62AJVvbAsE-TqgG2okITnsMYmlg6-_WiDf_vZFIMbYi11HYgQc8ifO6Skdm9NQgBW7sfdS1TxXMuau1AlUapMk48dHM9y4CBZHwfNaP-HBk8yiocLIbrnUs9WVgI6aZODJ3P-0eh6_CzhPsJ0cSSmKfUeTybcs7-ipekKckCYK5IO4PwfxmJfpZTUx-H6LhSaP_1Ueftjr6AfZD3czPvIsff1k4c511QeQaywoPnhIQs4WNGnj_yafZWltuij2-9bTdC3-73wfvULencLDx3m7W10p6T-Iv4eO0h-tC3J4MLU7_-m5JTMQgJF-zKJyEPZQFfdPlC-KovEmsIJWXlXRqe5ntgyPP9u2mkFUCM7NIX_6o3EEmwbVY41VwG-chDs4pUwCUV597riwJ6oYKrMgrylOc_CgREfqMLYrsJqpSP-FKYUIQuDZvcWnR7Rnr_MnXEgkg29Fbu96XExRSTGI8T8wIsREsZdlYygRqILSxewX2f2j5ApNhJZyWnDIOjqkezak1E65lXUj9RuemL215VWDlTBEMPbOMS30PgjI8_snVaWhrewvxI7xJdr6S-MSZVcsj7D2Vk1lqXo9dLvSypPohygcW9_tLGpVV_kOzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور میشه که مردها با یک سرماخوردگی ساده احساس می‌کنند به آخر خط رسیدن #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/689202" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689201">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسبدگردان آسمان(سبدگردان آسمان)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fC0CzgPV_hETBJAZ6EqIP-B8zNknlKhVAeWN1JGQ3dK7zbTrnEeHSze3wh8r5sUkSD_Owa8twRjaIGlrh2NmFrble_DiOSnDHxs6pUfRa1Eo_x4ckDA0YU5C6ETwzk02LyvurHNTerMs2PSAvySUsQdVL6oTqBYwMB5uCf0251STOkr4wXdORR9GeXJzoUdctMJ9xbHUULipmKasmRNE9a-b4tapia_zKJPQA7Ndv5Je4KKdqmi3pQIR_87tql1NMvgCh29AKt7xPsBxJfX1NIzBa_iiBRgPd3C4rRatKt8ej_RmqcAbI9b_pkBb2O2bUr9CZrx1b4x9YeuFrG75rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💯
۲،۷۷۰،۰۰۰ تومان سود ماهانه به ازای هر ۱۰۰ میلیون تومان
با صندوق درآمد ثابت
آسمان سهند
🎁
%۳۸ سود روزشمار، اول هر ماه!
✅
سود بیشتر از بانک
✅
واریز خودکار ماهانه
✅
بدون مالیات و جریمه برداشت
✅
محاسبه سود روزشمار بدون وقفه (حتی در تعطیلات)
✅
بیش از ۱۵ سال سابقه فعالیت
🔗
مشاوره رایگان
صندوق درآمد ثابت سهند
.....
سبدگردان آسمان
.....
☎️
مرکز تماس: ۰۲۱۴۱۷۹۳۰۰۰
🌐
وبسایت آسمان
📩
سبدگردان آسمان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/689201" target="_blank">📅 12:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689200">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMyAlfSexQZpJhgT_YFB-gZD5wFE0ShajcCj08-WNdwZHiqM12D1If5-Njp3A_mzXDaiChjMxk0k4ImBS4l2PzgwiztrDQlwXBYRX32xvslNuXn-T01UI6spurpst6ZlnY2h8ndRxAy2OU8Ed6Dl-g2_iYD9UAamTQAoashdnfnmjOp1Z48RcB7jAYZLAjdzZzC28Zbo65_BX3-0wFGDqPqDzgwbD-G-YN6KbP4btygjJarY991eefWrsn1_5dsTvGeRv7s-hETp9v5myazo_mABSoi4KQINMR3Rdui7pjBGvcWeTdGYImb9-jsaIT0EOjATbgaZ_AhmLjIED4PiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ ایران به فینال آسیا راه یافت
،
شاگردان پیاتزا کانگوروها را هم شکست دادند
🔹
ایران ۳ - ۱ استرالیا
🇮🇷
۲۵ | ۱۷ | ۲۵ | ۲۵
🇳🇿
۲۱ | ۲۵ | ۱۷ | ۲۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/689200" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689198">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEv-Y2aRdfFybaabZ6RKb0EB3Vua7FEmyT5SUwRiGpqXPnK6h0PAnTiZzVe6KRW707m6R1LHkXVE_S4FrstzL0ntGnkj3Xb4Fc_WXq0z3A0R2kiwEMF9USqxKbMWbXGALRmej_hQ_rvFLiGVbGtIL2bEvOMzjIWjJmgk_NAf-WTrgg0MhTFd31HfF0KZV3IXQM-ph1MfpabVmTKM5Bq1akpnWOEZJRJmMxSr6fptfyx1cFA1lY1pWuRm4o1ZWxRsSFs-a9ibWtXeMBct7l1AXzKGLc4nBdeeNcBBLDTrrZlag24rYPD05xoMTWOBQeJQ17sM8Gdn8atJJgwbP8lPHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/689198" target="_blank">📅 11:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689197">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f56cd818.mp4?token=hqyoT7cPWVI5ow5y15NeNA-B2yDSe12V3VCDAIO9VHiQ6NkqTq5zSIEAYdAr6MJYcd98QxA5RYXM0gEk0yKU7DJy6MzfwM734K7lcUw8-NQdhkyVTVItLejfCxjdOgVp2yX3YPruZEqswIvwCRrxvOqLPOmbSnSLG1i6_s8EYEfXRdLQdNzpLxvud3bybr6dKp-HA-s-6cI3BtXoMt2aEourxr4xg6KQ7S-a0jwkHNGYx5QaTVWCtkNfcmqb9Vx3DHNWAcsPVNoq-gzO2SoLM1lQOOBN4zFaCCfR4lgMVOJYcrJcXM5BDHh9wGh5n_H3BTJysmp3nxlOQ7lkWSi_PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f56cd818.mp4?token=hqyoT7cPWVI5ow5y15NeNA-B2yDSe12V3VCDAIO9VHiQ6NkqTq5zSIEAYdAr6MJYcd98QxA5RYXM0gEk0yKU7DJy6MzfwM734K7lcUw8-NQdhkyVTVItLejfCxjdOgVp2yX3YPruZEqswIvwCRrxvOqLPOmbSnSLG1i6_s8EYEfXRdLQdNzpLxvud3bybr6dKp-HA-s-6cI3BtXoMt2aEourxr4xg6KQ7S-a0jwkHNGYx5QaTVWCtkNfcmqb9Vx3DHNWAcsPVNoq-gzO2SoLM1lQOOBN4zFaCCfR4lgMVOJYcrJcXM5BDHh9wGh5n_H3BTJysmp3nxlOQ7lkWSi_PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این
تصویر را خوب ببینید؛ نوجوانِ سیستان‌وبلوچستانی، ماکت پدافندی که خودش ساخته را به محفل ستاره‌ها آورده و از آرزوی بزرگش می‌گوید
🔹
«سربازان در گهواره‌ خمینی» بزرگ شدند؛ جنگیدند، درخشیدند، جان دادند، اما میدان را خالی نکردند.
🔹
«سربازان در گهواره‌ خامنه‌ای» تازه دارند بزرگ می‌شوند؛ با این نسل چه خواهید کرد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/689197" target="_blank">📅 11:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689196">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY_DZYle8Jwqbob1GTenh4KurJr1psxJRufuXHsGAvHCIC1w_gOaAO-OElbiWdwduhKALHGZEWNbsBSp7tL-Yc8J880cCy3rat6KwKI5hFQccv18r3tFWXHhREckfg4pTLnvhRe4xzCp7SSujpRWi5Lgu3QvYu_z0tw1I44tj4iitCTphuc5dk7F__5mvostVnA8Jz7rC3WsMZoFjk2c5Q7s_sPeO21N9JtU264HJ2Rdcx28_bUeA3gAwDZnZ_64lcZQBR7kxGjwMWHdv3HbMMKWrmGN-P7qRqGPS0k4-cH7wJszl1pWyT2jWAxlmMtSa2NKLG9JwR--q_t-lZb0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕰
ساعت نگارگری پنج تن
ترکیبی از هنر ایرانی، هویت مذهبی و یک دکور متفاوت برای خانه یا محل کار.
✨
مشخصات:
▫️
قطر: ۳۶ سانتی‌متر
▫️
جنس: پلی‌وود
▫️
طراحی: نگارگری با مضمون پنج تن
💰
قیمت اصلی: ۲٬۱۹۸٬۰۰۰ تومان
🔥
قیمت ویژه: ۱٬۹۴۴٬۰۰۰ تومان
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/689196" target="_blank">📅 11:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689195">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb48de1ee6.mp4?token=Xfqe3ZyTtTYWK_GPrLRqDZvKFg7SDQ8k3p4H3dNmsoj7nFeDfsUA8MW9m7FnIQH2acQEybpIC7BJIwd3V75NRRlsFNzJJcAUdSpwYbp_3xani6nR5aR3sbLlXII58_AtmTeIMLBclDf7WuFWf2Hz0YIeENGg4uLey0uyr71uAvKFhIpb7k7yOlci54Z91N3pNtrWqgWuowDm9Fp3Xhhh4kz5kAn5AdoL5RD0n4w5Cz4HAxxPKv0AJj-tfc_ob7qVPVbpkInuU1x9Hj67DmJotJsjla_EzOppKAUjnsMLm5otBwcY_xFkf4Bjyx6Akr5H7Dv3gkGXNkiG-ATkrf8MSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb48de1ee6.mp4?token=Xfqe3ZyTtTYWK_GPrLRqDZvKFg7SDQ8k3p4H3dNmsoj7nFeDfsUA8MW9m7FnIQH2acQEybpIC7BJIwd3V75NRRlsFNzJJcAUdSpwYbp_3xani6nR5aR3sbLlXII58_AtmTeIMLBclDf7WuFWf2Hz0YIeENGg4uLey0uyr71uAvKFhIpb7k7yOlci54Z91N3pNtrWqgWuowDm9Fp3Xhhh4kz5kAn5AdoL5RD0n4w5Cz4HAxxPKv0AJj-tfc_ob7qVPVbpkInuU1x9Hj67DmJotJsjla_EzOppKAUjnsMLm5otBwcY_xFkf4Bjyx6Akr5H7Dv3gkGXNkiG-ATkrf8MSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«بنیاد شهید آیت‌الله رئیسی» از این بلاگر اقتصادی به‌ دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/689195" target="_blank">📅 11:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689194">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME8UTtPH3lyjta3_cAZfm0OUn8FHEfJvZ8_0pihTEQuxHMhLjmEH6FHFO7RPbujn8t7Cm7yjsJCtVHvRddWec7ypqBnm3LodcfC9vSOu7EkFKfBsNcs0bEi2E2zGG47yM6VMe_deVAoux5qkZcBT79g__uPdrklqnaJ90SbE86-rSCZVKHItDTYj4eIBumpNRl0bxOh5B9M8yMn3c5zhUqgMGU_2si_zuUdYVZp4_omxYsAbnyfMNg-b6Rz73NV_9K2Njz6miKJeXY20KzzVOXtbI7GVqMw8269Cq1mUKzHxvgTM2WfXyoDNdUQU7tO2cXG5S2zf-iS9dDD_JnYZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت کاربر یمنی: عربستان و امریکا دارن پیروزی‌های یمن رو نگاه میکنن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/689194" target="_blank">📅 11:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689193">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/X6tGck3fG8twv_7S6Y_t1RsCSqbizCv_-gdsPwl0DK3qr5m4mFJKYJD2coQoH7KSFD1AYyr7u6Rp0uTobQvdrRyS_eIFMtXOzL7BqdMjcdBgIp0TQc0206wm5DBb0r2UhQyCkGJVskDZiC__IfURVnb-VKJvyXn5xQNol-PMUb7U69K0FWCSM-EnUE91JhAIc54WKZRwVjPdOgqLJWCkDNXE4OM-QMGpYbd4tfrWjMcCrzvU3Dk4Iy-XuSXWR6nd5zfD9vG3KimdqsJchBnGqaMY-wOhDW2MAyR-gPSkNO4anKGgSs41bXI84RkVgcXEJzvXK3I7OpRKZqBXNHaFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس هیأت عامل ایمیدرو: نتایج بسیار خوب اکتشاف در معادن جدید چادرملو، سودآوری آینده را تضمین می‌کند
محمدمسعود سمیعی‌نژاد معاون وزیر صمت و رئیس هیأت عامل ایمیدرو:
🔹
در چارچوب سیاست‌های ایمیدرو، چندین معدن جدید در اختیار چادرملو قرار گرفته تا این شرکت بتواند عملیات اکتشاف آنها را تکمیل کند و خوشبختانه به نتایج بسیار خوبی هم رسیده‌اند که آینده شرکت را می‌توانند برای سهامدارانشان تضمین کنند.
🔹
چادرملو یکی از شرکت‌های بزرگ و مهم زنجیره فولاد کشور است و مدیریت جدید این شرکت اقدامات خوبی در فعال‌سازی معادن کوچک و تأمین مواد اولیه از این معادن شروع کرده است.
🔹
چادرملو با توسعه معادن جدید و برداشت سنگ آهن از چالش اتمام ذخایر عبور می‌کند.
🔹
چادرملو، معادن کوچک را وارد مدار تولید کرده و در کنار آن، موضوع اشتغال را در این بخش مدیریت کرده و می‌بینیم که سال گذشته رشد تولید و سودآوری داشته‎ است./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/689193" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
وزیر نیرو: ممکن است بارش‌های سهمگین داشته باشیم/ همه آماده باشند؛ نباید غافلگیر شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/689191" target="_blank">📅 11:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689189">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/689189" target="_blank">📅 11:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689187">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمدیریت دارایی گندم</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgNVLIQHu5HoSsxNhdzw3GAs6AL_oVI1TxjeQfD0EWYoSBAadj6hib_APMGC2unU2F-Ww-ly3yBRfGE--2NvWi7XcSGsinemjLKjz_9AW6s_FgPuHGz0fyh_1vK2b1Wzaq_1riazFOcSzlo_tFbpp0pYrdzh5XKpP7HZfw0-q26V2JuuIXLm2nCtbmViJN1bnJKsGC9SGJE5FEWGSelw1smWO9ok32Xj3QHAZo8wEDXXDHtR_C4IASuFKOxdFLxhmC-zVtN7NvKeSHfNv_2kT7oyKOcp1OMH0IbmMESnPsvkapROsv9TrYAxsAGtVf6IJGEhAXuDimPUNBXWCo3RvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبد سرمایه‌گذاری خوب، لزوماً سبدی با ترکیب ثابت نیست
😇
در سبد ثروت، وزن سهام، طلا و صندوق‌های درآمد ثابت متناسب با شرایط بازار تغییر می‌کند و ترکیب سبد به‌صورت اختصاصی مدیریت می‌شود.
🔵
۳۰۵٪ بازدهی از ابتدای دوره
🔵
حدود ۱۷۰٪ تورم در همین بازه
✅
سبدگردانی اختصاصی
✅
مناسب سرمایه‌های بالای ۵ میلیارد تومان
✅
قرارداد یک ‌ساله
✅
امکان دریافت اعتبار از کارگزاری
✅
مشاهده روزانه وضعیت سبد
✅
ارتباط مستقیم با مدیر سبد
🔗
هماهنگی جلسه مشاوره اختصاصی
🔤
پشتیبانی:
@gandom_mediaa
☎️
شماره تماس: 02192003330
🌾
نقشه راه سودآوری با گندم:
@GandomFinance</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/689187" target="_blank">📅 11:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689186">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_0sBBmzzernaqWOYI1vRpK6P4h5V3vAZHxFJRjTavMEKsrOVNmsixXkEZbe_iZk8tERj-2YLbyDRd-YF2UWfpN6vSkAMw23Y01fyz5ImqLesO5TWdo2dxeUmTX42Oe-1prrGGQJ3VQj-h8_yY9kwAQtrsW_HaxT5Z5jf4brgzMjMozSGM9De7GYYMQUImt75EEhAAyLO07YTjOP2AcAR0Tguhv2nWqT9SwNHIBA_v55ijnAqdwfSJiqo3jxZ2rBzB4TGcX9Iui4lEMTFKuQ18WSBVRQPnmpt8Drj4d96Nd-KlgygwzAFCYUShq_CbSOhpagXK81PrspBQ72imnnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر پاکستانی: من پاکستانی‌ام و در کنار یمن می‌ایستم/ لعنت به سعودی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/689186" target="_blank">📅 10:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689185">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سایت عبری والا: افسران ذخیره اسرائیلی خواستار گسترش عملیات در داخل سوریه شده‌اند و برخی از آن‌ها ایده اشغال دمشق را مطرح می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/689185" target="_blank">📅 10:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689183">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e1db5944.mp4?token=AU6sYkai7dMuZmEZI_6JnAIX8I363hia8frfygj65v3eqvjhQmKqX4Y0SGQce8kEg0O8MX4zTSWiM982cGZ5uYh310faKdwxcbvmyTGRcd9HhN7Y4jhrqABh3uyepb3Ia3Zqy24Vo2KAw9ixbjDWHTwGFXr4otpQsfvwQv8-VexWV6S9ySNgSyImIoxzaIF3OwqXQjRW1rdAazXQulQy1bK6lp1xQbKp41JSVxpN3A8J9sEw5lObUKLh6dN3tGkJxxiN6HU5FZejZUZBRrgluULYkTpSPEIR6sKMHGIOFj4GPO0iiRUBS_LZXewx2YlLprkhOS55Zg6JY654tszyLIfeB77ZKOxBSp1_jjDPT9VXAZTpVmDXuviy4tin4fr02MPBBRcjRl9lp_lsNsezqYSiOrb2Qfydi5G7IBSkKD_lad-4ksJc4D8MCRzA0wsDRKXNAPw4FeY78DX8LC7MIE4jnZS2PYVbBj_JSNVclKnDxueXyZ-LDmjazj9llD9T3qDKtA5ZH_gRtHwtXFjJze8b6XKDRbJ6sSOCfdcQakgf5z4C3jLNziRwuoBk6B4sK01Zv1ELJ-T3Cnepnxu-D_-B0mzpU6p-Y3L1nGDLlNF4lY12FqBn22kEdNf2FMzkJBb9xsaCKtnrEemCTsHyTar1iNl3W63h5GuLrRK4znw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e1db5944.mp4?token=AU6sYkai7dMuZmEZI_6JnAIX8I363hia8frfygj65v3eqvjhQmKqX4Y0SGQce8kEg0O8MX4zTSWiM982cGZ5uYh310faKdwxcbvmyTGRcd9HhN7Y4jhrqABh3uyepb3Ia3Zqy24Vo2KAw9ixbjDWHTwGFXr4otpQsfvwQv8-VexWV6S9ySNgSyImIoxzaIF3OwqXQjRW1rdAazXQulQy1bK6lp1xQbKp41JSVxpN3A8J9sEw5lObUKLh6dN3tGkJxxiN6HU5FZejZUZBRrgluULYkTpSPEIR6sKMHGIOFj4GPO0iiRUBS_LZXewx2YlLprkhOS55Zg6JY654tszyLIfeB77ZKOxBSp1_jjDPT9VXAZTpVmDXuviy4tin4fr02MPBBRcjRl9lp_lsNsezqYSiOrb2Qfydi5G7IBSkKD_lad-4ksJc4D8MCRzA0wsDRKXNAPw4FeY78DX8LC7MIE4jnZS2PYVbBj_JSNVclKnDxueXyZ-LDmjazj9llD9T3qDKtA5ZH_gRtHwtXFjJze8b6XKDRbJ6sSOCfdcQakgf5z4C3jLNziRwuoBk6B4sK01Zv1ELJ-T3Cnepnxu-D_-B0mzpU6p-Y3L1nGDLlNF4lY12FqBn22kEdNf2FMzkJBb9xsaCKtnrEemCTsHyTar1iNl3W63h5GuLrRK4znw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از یک رستوران و پرزنت غذاهای لاکچری این رستوران به یکی از مسئولین شرکت نفت که در فضای مجازی پربازدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/689183" target="_blank">📅 10:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689181">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
دستمزد ۱۹۰۲ درصد بالاتر رفت؛ تورم خوراکی ها ۳۷۴۵ درصد بود
/
دولت به افزایش حقوق کارگران در نیمه دوم سال تن می‌دهد؟
🔹
افزایش ۶۰ درصدی حداقل مزد در ابتدای سال‌جاری، قدمی برای جبران هزینه‌های تحمیل شده به معیشت خانوارهای کارگری بود؛ اما حالا آمارهای رسمی، فشار تورمی بر معیشت کارگران را تأیید می‌کند و طبق قرار قبلی، باید تمهیداتی برای افزایش دوباره دستمزد اندیشیده شود.
گزارشی در این‌باره را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3244607</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/689181" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689180">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای وزارت خارجه عربستان: خط لوله «شرق ـ غرب» در چندین حمله پهپادی که از عراق انجام شده، هدف قرار گرفت و این حملات به مصدومیت و جراحات انسانی منجر شد
🔹
عربستان تأکید می‌کند که حق خود برای اتخاذ تمامی اقدامات لازم و تضمین‌کننده حفاظت از حاکمیت، امنیت و…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/689180" target="_blank">📅 10:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689179">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
یک سال فعالیت در مسیر استاندارد و ارتقا کیفیت
🔹
استاندارد، فقط یک مهر روی محصول نیست؛ از تدوین و اجرای استانداردها تا ارزیابی انطباق، تأیید صلاحیت و نظارت بر بازار، بخش مهمی از کیفیت و اعتماد عمومی را رقم می‌زند.
🔹
اداره ‌کل استاندارد خراسان رضوی در یک سال گذشته، در مسیر ارتقای کیفیت و حمایت از حقوق مصرف‌کنندگان، اقداماتی از جمله صدور و تمدید پروانه‌های استاندارد، تدوین استانداردهای ملی و بین‌المللی، برخورد با تخلفات و آموزش‌های تخصصی را دنبال کرده است.
🔹
این ویدئو روایتی است از اقدامات اداره استاندارد در راستای کیفیت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/689179" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689177">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کارت‌های ملی فعلی تا پایان ۱۴۰۵ اعتبار دارند/ رئیس سازمان ثبت احوال: نسل جدید کارت‌های ملی جدید از ابتدای سال آینده صادر می‌شود
/ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/689177" target="_blank">📅 10:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689176">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/689176" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689175">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
فدراسیون فوتبال ایران جریمه شد
🔹
فدراسیون فوتبال ایران، به دلیل ارائه دیرهنگام درخواست برای صدور مجوز بازی دوستانه تیم فوتبال امید کشورمان مقابل تیم کایسری اسپور ترکیه، مطابق مقررات AFC برای صدور مجوز رقابت‌های بین‌المللی به میزان هزار دلار جریمه شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/689175" target="_blank">📅 10:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689174">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
فرمانده ‌هوافضا: آمریکایی‌ها پهپاد لوکاس را ‌از روی شاهد ۱۳۶ ساختند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/689174" target="_blank">📅 10:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689173">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/894a3db316.mp4?token=cH5e_06BVUTa9gwCeSw9PfvLmpBUZmn8hA7m9lrtosLWIZQ4_6PD0n7gHvbQio-It6ZqwbG1hZwAd6HeppS-1XBN5EEVjabI1mCPz_7dHGbrggy0srOONlC8GrY4widpvAHddD2Be9O3PHbBTGN0vwgsHyZpAZ8KTjk7VE0HHOC0r71VLyN9SOv-hTSFIvxiMW6LpYEdET9PCP_oHfIRJ6EC0rdeW-P2xjRqzn5QhRAMOZKLp0my7L9OOFqDOUtp3wL0Zrl5KacF0zNNQciGiV5lj2hDtlXyJV_V4TuNVlArSZL2VZH38tnG83Rzq1X0h78zqbwKoB6NFNCdO8zF_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/894a3db316.mp4?token=cH5e_06BVUTa9gwCeSw9PfvLmpBUZmn8hA7m9lrtosLWIZQ4_6PD0n7gHvbQio-It6ZqwbG1hZwAd6HeppS-1XBN5EEVjabI1mCPz_7dHGbrggy0srOONlC8GrY4widpvAHddD2Be9O3PHbBTGN0vwgsHyZpAZ8KTjk7VE0HHOC0r71VLyN9SOv-hTSFIvxiMW6LpYEdET9PCP_oHfIRJ6EC0rdeW-P2xjRqzn5QhRAMOZKLp0my7L9OOFqDOUtp3wL0Zrl5KacF0zNNQciGiV5lj2hDtlXyJV_V4TuNVlArSZL2VZH38tnG83Rzq1X0h78zqbwKoB6NFNCdO8zF_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند همیشه کباب‌تابه‌ای تازه، اقتصادی و فوری داشته باش  مواد لازم:
🔹
سویا خشک: ۲۰۰ گرم
🔹
گوشت چرخ‌کرده: ۳۰۰ گرم
🔹
آرد سوخاری: ¼ پیمانه
🔹
روغن مایع: ۲ تا ۳ قاشق غذاخوری
🔹
جعفری خشک یا تازه: ۲ قاشق غذاخوری
🔹
نمک: ۱ قاشق غذاخوری
🔹
پاپریکا، پودر پیاز، پودر…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/689173" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689172">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f4a86dc5.mp4?token=bDoQ4pbTWNXbFlTfTPDxDds3DKFzTgomyNvEKe6O4lmiNLDPpVWup6a7RJSp9_Bl8g6KfvPCKaDKymfL5Uuv7cVYR9oLDbKVIOxAFbK7QOcYu7etcTM2VRboYbVaH7ZWC12LE2VsfrYufFJBi-cIgU-d9YG3uKGD-1Ap4gdJKQVOvdFZcMgyn5uH0Qdgb8l5PBUOTpg3mt6CKB-wyYFetcq8-FL5lZ59i248Li0Au_H-B1hRRGv9yTk512c_r1KsAxeO_yNOQfCf-c0lDn8sud--e597w65F-aYFIGgxzk4R5DgW6-W2WZ7KLCUZ5lVfZkxYgDTaud3VH8j7cqeBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f4a86dc5.mp4?token=bDoQ4pbTWNXbFlTfTPDxDds3DKFzTgomyNvEKe6O4lmiNLDPpVWup6a7RJSp9_Bl8g6KfvPCKaDKymfL5Uuv7cVYR9oLDbKVIOxAFbK7QOcYu7etcTM2VRboYbVaH7ZWC12LE2VsfrYufFJBi-cIgU-d9YG3uKGD-1Ap4gdJKQVOvdFZcMgyn5uH0Qdgb8l5PBUOTpg3mt6CKB-wyYFetcq8-FL5lZ59i248Li0Au_H-B1hRRGv9yTk512c_r1KsAxeO_yNOQfCf-c0lDn8sud--e597w65F-aYFIGgxzk4R5DgW6-W2WZ7KLCUZ5lVfZkxYgDTaud3VH8j7cqeBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از ساعاتی پیش یک تیم تروریستی در بخشان سراوان توسط نیروهای قرارگاه قدس سپاه محاصره شده و رزمندگان در حال انهدام تیم می‌باشند
🔹
گزارش تکمیلی در بیانیه قرارگاه تا ساعاتی دیگر به اطلاع مردم شریف ایران خواهد رسید./ صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/689172" target="_blank">📅 09:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689171">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سپاه اصفهان: احتمال شنیده‌ شدن صدای انفجار کنترل‌شده در جنوب اصفهان تا ساعت ۱۴ امروز
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/689171" target="_blank">📅 09:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689169">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fdf27086.mp4?token=jAaH4-v0fcu3Xs18rjGZPLheCrISBOoyc6Ys_I6DOh0DDsSWyiI-ATdDt6Klag2oyPEaoQg91nVgY_VklqL9-9KWv16r3zB2HWzrxKSaJJGK12Jf0_qMZJeWyKzirbUl2pO8m1Q3yUhCu07PyZoxGM2l-KSS8GmzzMCTdZz9Uj87U7o0nzA0fXCvBCtJNY77uY_6N5E2YEwUdc-JMNa9J39sRwnR56GTg9qUYb6ckV_ETha71lN36PZSclGLEt_11ZTB2ut-Ew8VClLEVr1Z3XAlWieYv1e91S6SMUXRx0S_ed1-ZNSUJ3KKAcs88c97x2L2T_F-xn8Cn9ORdpxEuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fdf27086.mp4?token=jAaH4-v0fcu3Xs18rjGZPLheCrISBOoyc6Ys_I6DOh0DDsSWyiI-ATdDt6Klag2oyPEaoQg91nVgY_VklqL9-9KWv16r3zB2HWzrxKSaJJGK12Jf0_qMZJeWyKzirbUl2pO8m1Q3yUhCu07PyZoxGM2l-KSS8GmzzMCTdZz9Uj87U7o0nzA0fXCvBCtJNY77uY_6N5E2YEwUdc-JMNa9J39sRwnR56GTg9qUYb6ckV_ETha71lN36PZSclGLEt_11ZTB2ut-Ew8VClLEVr1Z3XAlWieYv1e91S6SMUXRx0S_ed1-ZNSUJ3KKAcs88c97x2L2T_F-xn8Cn9ORdpxEuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرت زدن ترامپ جنایتکار در مراسم ۱۱ سپتامبر
🔹
وبگاه آمریکایی «دیلی بیست» درباره چرت زدن او در این مراسم نوشت: «ترامپِ ۸۰ ساله نتوانست برای ادای احترام به قربانیان ۱۱ سپتامبر بیدار بماند.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/689169" target="_blank">📅 09:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689168">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی بصره تمام پروازهای خروجی به ایران و ورودی از ایران را تا اطلاع ثانوی تعلیق کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/689168" target="_blank">📅 09:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689159">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای فایننشال‌تایمز به نقل از منابع مطلع: وزرای خارجه کشورهای خلیج فارس برای پیشبرد توافق هرمز با عراقچی دیدار می‌کنند
🔹
این نشست قرار است روز دوشنبه در شهر ساحلی صلاله در عمان برگزار شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/689159" target="_blank">📅 09:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689157">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تکذیب تعطیلی مرز مهران
‌فرماندار مهران:
🔹
مرز مهران باز است و فعالیت‌های مسافری و گمرکی در این مرز برقرار است و هیچ‌گونه تعطیلی یا توقفی در روند فعالیت مرز با کشور عراق وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/689157" target="_blank">📅 09:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689156">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/689156" target="_blank">📅 08:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689153">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e9030f43.mp4?token=hue29NJdVL7z6AuppJOIzx9OrQtyFP4D6-6x72aButaAZVm-DHmQYhPoZpj9aUWg0_I416S_UgUH53GJEPQuzDrn1sc7jVn42E4xH-2mWppGoqL1_fUKQQsIoKx4FIRT4mK8SplbaVcZxKoM8-pr6MBZET58qDQzJX6la0EjjF0mwBuCW_q13mXryqufG64P5xLzZnuV2OQEg7gm3k8L8_klT5F5qegon9iJlHUzRn7u7TZPWn4mSM6VVU2QsRP-nyESVapk1VJplc-4tMq3OuPLVC_ZhttuIC7KF8AJ3XhMcXDNotQlgU8rXOyuBGvG6ZVwfn1v1zQXCAGHdvAk5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e9030f43.mp4?token=hue29NJdVL7z6AuppJOIzx9OrQtyFP4D6-6x72aButaAZVm-DHmQYhPoZpj9aUWg0_I416S_UgUH53GJEPQuzDrn1sc7jVn42E4xH-2mWppGoqL1_fUKQQsIoKx4FIRT4mK8SplbaVcZxKoM8-pr6MBZET58qDQzJX6la0EjjF0mwBuCW_q13mXryqufG64P5xLzZnuV2OQEg7gm3k8L8_klT5F5qegon9iJlHUzRn7u7TZPWn4mSM6VVU2QsRP-nyESVapk1VJplc-4tMq3OuPLVC_ZhttuIC7KF8AJ3XhMcXDNotQlgU8rXOyuBGvG6ZVwfn1v1zQXCAGHdvAk5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری نیروهای امنیتی با افراد مسلح در بخشان سراوان  معاون امنیتی استاندار سیستان‌ و بلوچستان:
🔹
نیروهای امنیتی با شناسایی محل تجمع یکی از گروهک‌های مسلح و معاند در سراوان، آنها را غافلگیر کرده و ضربه سختی به این گروه وارد کردند.
🔹
این گروه قصد انجام یک عملیات…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/689153" target="_blank">📅 08:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb40c5dc75.mp4?token=VUlJcmHi6UNi3UDld8BHsO4H04McztrnzBeG37Ls0sRkaubLC82dSeyV66u2-ftDiRHDLlV88Qp_mieqx0H4noEWhZZA7QGuEOTq_lSJx3OhYx7-TP4puil-LSvRTSqShjSQsk7HunceqhQ8iKJTbyqPJzOANnRRgWtfFbF4MOxZroWXnSyA8H99F5qHcvmbmStfFyZUSSUVV-YCXp4N3WY4oPWujYkB4329dBCCHbLbzVXnm-CRAKQbrUSzM3w47iwilVxa0bXFaCZGDd75CwaLUMuIHQN4hR2n9M-IdD-Cqka7XtA6K0cgUZmjhaX6VAf_7P9XYEgKsBj02LJgbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb40c5dc75.mp4?token=VUlJcmHi6UNi3UDld8BHsO4H04McztrnzBeG37Ls0sRkaubLC82dSeyV66u2-ftDiRHDLlV88Qp_mieqx0H4noEWhZZA7QGuEOTq_lSJx3OhYx7-TP4puil-LSvRTSqShjSQsk7HunceqhQ8iKJTbyqPJzOANnRRgWtfFbF4MOxZroWXnSyA8H99F5qHcvmbmStfFyZUSSUVV-YCXp4N3WY4oPWujYkB4329dBCCHbLbzVXnm-CRAKQbrUSzM3w47iwilVxa0bXFaCZGDd75CwaLUMuIHQN4hR2n9M-IdD-Cqka7XtA6K0cgUZmjhaX6VAf_7P9XYEgKsBj02LJgbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: خیلی‌ها فکر می‌کنند اگر در انتخابات ببازیم، من عصبانی‌تر می‌شوم و کار را یکسره می‌کنم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/689152" target="_blank">📅 08:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689151">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10a23745f.mp4?token=PckKmuUTeHNVxuu6hEzUtsMQFCa6jNN9GyPosfCdaGMyC1AMrMw92pF78xeH6bUYg3x_VOwxDkzEqdYmFSLkDZTiHYHKm4EC2-dlDb-ii5LwEzz2Myqazhkws6IdNgTPq-3wv-d6AaiwqK_fZ7zF4XsJSCp0X-ZVampde5AsvcXUoMOC_UQibHqwR_y398U8DPFqhCQWpn2frEkWfmfpxRt_9qHNH_6RTYTQ0pO4snjEJQewPCU22yna53MRGgN48oBJ22E7SVVUkauDQvZu5YUfGk-a3fDVzlKwWptZZE9VRecqGiBcdFf0F-ScRTfFZrByOUiIGy7SJVON1XLNKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10a23745f.mp4?token=PckKmuUTeHNVxuu6hEzUtsMQFCa6jNN9GyPosfCdaGMyC1AMrMw92pF78xeH6bUYg3x_VOwxDkzEqdYmFSLkDZTiHYHKm4EC2-dlDb-ii5LwEzz2Myqazhkws6IdNgTPq-3wv-d6AaiwqK_fZ7zF4XsJSCp0X-ZVampde5AsvcXUoMOC_UQibHqwR_y398U8DPFqhCQWpn2frEkWfmfpxRt_9qHNH_6RTYTQ0pO4snjEJQewPCU22yna53MRGgN48oBJ22E7SVVUkauDQvZu5YUfGk-a3fDVzlKwWptZZE9VRecqGiBcdFf0F-ScRTfFZrByOUiIGy7SJVON1XLNKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صمصامی، نماینده مجلس: بیش از ۸۶ میلیون بشکه نفت کشور به‌ صورت اعتباری به یک شخص واگذار شده و صرفا ۳۰ میلیون به خریدار نهایی منتقل شده، اما سرنوشت ۵۶ میلیون بشکه نامعلوم است! شخص وزیر باید پاسخگو باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/689151" target="_blank">📅 08:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689150">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سازمان رسانه‌ای رژیم صهیونیستی از برگزاری دور جدید مذاکرات اسرائیل با لبنان در روزهای سه‌شنبه و چهارشنبه در شهر «رم» خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/689150" target="_blank">📅 08:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689149">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLCdg7bTYBrGz2jTSucQFtCOrAbgAUXHsu72eQp6IvWxOnaj2a-WBhzVS5OOyhLVbWA3mzlim3IBRC9K5GMepG42KkQ89eMtLlp265xgrMVRzr6xz4RILNrtwtKoUFm12fnEiC6tjYMWpqNasFqigEuoAPB996AugGbpQxO8V_LSuPYw2f0VTk5LCp4XbE0jJN_91Fq0uXrlKy_gqxmtt0dABk1CVt3fvzdelZ1Ihftt7Fsxms3PzbkvUqsliYHyN7fsXkfEqcGDiKqYI6B4OUr4un1H_v1I1MJkACIcx9WRXbFQdP5zLSotHafznYH2MUBTtbToG5RYHZvfqxvoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون: اگر مقاومت عراق می‌تواند جواهر تاج زیرساختی عربستان را هدف قرار دهند، پس هیچ شکی وجود ندارد که ایران هم می‌تواند هر زیرساختی را، در هر لحظه هدف قرار دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/689149" target="_blank">📅 08:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689148">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7UpbvzQxxxts2fh08YEil1icLLk-BAnhFWRCyPyQFyci3WkCVhGtesaV7lGNbu1ZEw1dsl4ExJ7zM4e47e_50_SX0jeRcvYUe3jfDY_iX5mxS9B4m6I-MusGX95u_1FyTEGFJw7x4BonHpO9XbJsoFfWJ6saP7lbotisf8Mv1YuoJhcWDXn-uSBiDAeCJ6F4NKJWViApMqJlfSabnT4uoK-5dvgKi6W1mtK7tDwZqfN3iMI_XqHd91ag_zh85HDfpUoRDwc2-9Mat53v1OaJuVgaiEArfwNoQMytqVCdQzrQ2u5Yh17CKeIPvGWwkO-SswBJwLOyw2tPNH6UK_5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد دانشگاه میامی: سقوط سعودی بزرگ‌تر از سقوط دیوار برلین خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/689148" target="_blank">📅 08:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689143">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEJWbNalofkoHO2q7ZTlfc6aXNpr37K5mYMLzSWruPBPKMEmhChj_4jcW7BobyN-GHeivytsfjD8t1Bd6LFDzTdlxYn3LGkC9Lh1AqL7wF9cWpKQzEo273ZV6g6kyYB3j8b25IFpOb0gM_QpdujnnezBVVqPm6DORBePiN4p32XZpvpCJJMolyE2znUJebBkosgBdsAgB-T_7UiiDc1EVD4FqCAU9Zz1XRWJr8Y3PbS3fG3xA-vYXkLevEdXzC_gDLSpRXP_HIij1N6LeSKT0sRfVYRRBMBhdjgL_07biYpjYRoc8sXlSOhOM_fBJOyxGLvjqEL8Y_C8ZAZseQZbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guiC1YLdnQMdmOvAsGkuCFXWuj3_zSKmxjdY5PRg2h1_T6ChaYgMycSDl1y-RJut_SDWPvN4f03o-DlWhO0vlAMNfQf9GoRkAZ5JVnoxJLgZv0Exck6Jf_sTI9GNdFq7iffUQlUqh55KQs4PS90d1o4hj9TE8tV--OLJA16rSQDYxoVxA_g-G0xSk3hBO5LtxwEMda4EkSq-MoqWO-w20bGy-tWzmRjLtlB-rFookWXOqTGaQtXwyLN90wiWSfwpWIbU8vAqtk1-asnGHwZqC_2-zNLXIuNkv3NeKLCGxC0W_xmhkAKs3VDVWJ3nGRjJKYxCrZm5PYT6XoqKZVGjxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEiff47DypD0fsLGuiVulXnKE3blA4ZI-SXxj4hAb-ZP6oEWGr27pH11ltKH4v3oxTi8F1_U0zKU5cBPsw2uSRXKCatlk1hO4G8yFQ5yWpCGHtSxNa-t79oNHb9Ef6psjsZWnu5ncq7smf7A4i8kHrg7BFFZ8E4TeOVoOYX2ZbXP9k2zB7AxOz0rohSA5rGAII1TN7dLh3uqzUjZr65F4Y6A9ZQQpNKC3jalZyqbruXzJEJBCLt7ebQ6YJRFZSxXz6P64_-qeBQAdgkg5K5Pf65DSduYTW6OonqqIGbKUuJiBmc6IpsZ2UqePe0m6U1GHLHSX6K2JL-qY2oKnKIboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dv79ekGQ4boeajAjQ1OLLdxXWVZY-oMrQ1LSdM-xUNmlgQIFohJY1hykjaBAgWQaXIikotw7ZgipqQqSWYqKc5zRMf3Yj4MgGVZA2lIZyOuVT-Y3pjpMOxUMW68dseDan5QGc8CmKIrLfnSHx04H8DoVRRXyzgechhU_hNIJGa2M4ThQ05CXb5BImVoXN6q5TzA-GEeCh145MbAn_eEs78yIAnXqcJnHqXlrCxzIaFDXgI5eFMRNRNNVa1TL9KtrZsxo133gyFubLCvTXgOZBuSxTgKhBLaQLrOw0aDTVx1La5Nq5zLUiJ3EAUdc9MwQt0hii1PKX1dvvA9YfWMlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yr-WGT-zCBvOW3Lg4Btb8lh37IIQW7dH18o-VGNgBDJWFMREaaefDRTeShSVN_muET4sEamXUHObNPpAuhzRr6c6BjZHMq5xiFuR9rBf0UfyHQlfeFVtlPOKqRp9oOBDZPgpDvuXHes2jjs0QnjttZm7aIj2N4_ciW5XjWnneVztJEj1D4NntTHRE4SaBaAfhzMlbVaP9wsgjC3cnPAo-YWZ-eY-EwOPFy4cSfrt29M0tOnSu0Ih0me56IvfK-QIVKXPxc_Xi5fyxjmeY_0i7P-4xWGrJprSaCG69Mc9IIP2Nn5h1mLJQ6toH3H1AdiA6Nvw7A7XNXIMsCYksc8Y9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قیمت عرفی مشروبات الكلی، جهت تعيين جریمه در سال ۱۴۰۵ اعلام شد
🔹
ارزان‌ترین نوع مشروبات الکلی، آبجو قوطی با قیمت عرفی ۴۲۰ هزار تومان و گران‌ترین آنها ویسکی جانی واکر بلو با قیمت ۳۱ میلیون تومان معرفی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/689143" target="_blank">📅 08:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6723a95a5.mp4?token=i76VNm6lq0nTJ-12Vog50JUWGBN3Yuac1v09a-fG3OrOuzzWUfyTNFCClyizB9qb53b-nnx9vR9dY_LLx8XEnE0MUodgfmJgnxvHOpALriCshaOJgkWzSyi9ASNFdkLxdYqnTCcOD-McKjOOXD1QowMSxU6eIoSevYIc2K5cF5X9SNQj054MGtz3743LOi6BX3fMJIiGmGl52txSIwY0OnuIeA26akZsadsaOBxOfavXKdPexkzDOFnfJDXI3rss9lzzlkqs_XkwwcgwOawTFWh4lpCSxGFJvpS17yCstKLVM_zP1vg76MolPFjQqGKWVAyJueZBZtXCo-W8vxdAlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6723a95a5.mp4?token=i76VNm6lq0nTJ-12Vog50JUWGBN3Yuac1v09a-fG3OrOuzzWUfyTNFCClyizB9qb53b-nnx9vR9dY_LLx8XEnE0MUodgfmJgnxvHOpALriCshaOJgkWzSyi9ASNFdkLxdYqnTCcOD-McKjOOXD1QowMSxU6eIoSevYIc2K5cF5X9SNQj054MGtz3743LOi6BX3fMJIiGmGl52txSIwY0OnuIeA26akZsadsaOBxOfavXKdPexkzDOFnfJDXI3rss9lzzlkqs_XkwwcgwOawTFWh4lpCSxGFJvpS17yCstKLVM_zP1vg76MolPFjQqGKWVAyJueZBZtXCo-W8vxdAlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری تلویزیون الجزایر از فعالیت‌های پشت پرده مزدوران امارات در این کشور
🔹
تلویزیون الجزایر با انتشار اسناد و مکالمات ضبط‌ شده، از دستورات مستقیم مقامات اماراتی به مزدوران داخلی برای تبلیغ و تمجید از بن‌زاید خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/689142" target="_blank">📅 08:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689141">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
وب‌سایت «اینترسپت»: یک شرکت هواپیمایی آمریکایی ارسال تجهیزات نظامی به اسرائیل را از طریق پروازهای مسافری از سر گرفته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/689141" target="_blank">📅 08:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689138">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e545e3479.mp4?token=ShuyWaH1cMz5YN3kcDAGXiHmtKoD69VewD2_XKVHRBoJgWIvA3IIPBa-zWqXShZMNiA1PPG1-toF3kmLMRoztnGAoEow33unFuh-MpvS6dWtuXhxtE3cGHkOxEWkU4niVMp892gqfUKhpiPSuUkggLHTY1f5-wSLmZgKwVZUDWVkTRupt42rmR7Ze9ZqEc8og3MlnGhR8OQgOLDn6e4eswJQldfAvgqWS_xFi7h-rcnie1JIS2A3yUxs9JJqfajzgfpQ-TQOyEFz6MEbRhe-9eiATXQ2ZcaZtdLtKvh15YkqfqVcJxhH4AvcNPibF4-KU6Scp8UMIWQ_p9-117SB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e545e3479.mp4?token=ShuyWaH1cMz5YN3kcDAGXiHmtKoD69VewD2_XKVHRBoJgWIvA3IIPBa-zWqXShZMNiA1PPG1-toF3kmLMRoztnGAoEow33unFuh-MpvS6dWtuXhxtE3cGHkOxEWkU4niVMp892gqfUKhpiPSuUkggLHTY1f5-wSLmZgKwVZUDWVkTRupt42rmR7Ze9ZqEc8og3MlnGhR8OQgOLDn6e4eswJQldfAvgqWS_xFi7h-rcnie1JIS2A3yUxs9JJqfajzgfpQ-TQOyEFz6MEbRhe-9eiATXQ2ZcaZtdLtKvh15YkqfqVcJxhH4AvcNPibF4-KU6Scp8UMIWQ_p9-117SB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری نیروهای امنیتی با افراد مسلح در بخشان سراوان
معاون امنیتی استاندار سیستان‌ و بلوچستان:
🔹
نیروهای امنیتی با شناسایی محل تجمع یکی از گروهک‌های مسلح و معاند در سراوان، آنها را غافلگیر کرده و ضربه سختی به این گروه وارد کردند.
🔹
این گروه قصد انجام یک عملیات نسبتاً بزرگ در شهر سراوان را داشت که با اقدام نیروهای امنیتی، تعداد زیادی از اعضای آن به هلاکت رسیدند و عملیات مقابله با آنها همچنان ادامه دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/689138" target="_blank">📅 08:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689137">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
معاون استاندار خوزستان: بسته‌شدن موقت مرزهای شلمچه و چذابه توسط کشور عراق و توقف تردد مسافر و انتقال کالا
🔹
ادعای رویترز به نقل از دو منبع امنیتی بغداد: عراق پس از حمله پهپادی به خط لوله نفت عربستان، در اقدامی احتیاطی گذرگاه مرزی شلمچه با ایران را بست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/689137" target="_blank">📅 08:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689136">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2lMl30R0qPT-H1b7fFDuIPDLRQB_eXHoQ6xRD6rf4_7ZxPhCjmxFD-l5nljbfcybKRIUgc26nKJO_tq66y28VFq5da2Tis5JZ2rGGwPzh-_kYKPHowxkl3xVkTRze009MJUcxIgCaSWE3exTK8wZTBX_bZaHucVSjyxVVYKz9EXx_J_HFwRIaPO7jbKbIvoakhEcj1okBfuCbzKnpU-BiLty3JmbwRNR9Q_7WBN8UHz1or9qh5tYC3Fiq4QpBdtoosF6C_DZNDl6m7niPxzMz-GPGPI6uzZYlvNTCsuM7_ojHeI7qSDvFFbRgM4j86FNcahTr2YRUcn9TqcRKiY2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲۱ شهریور ماه
۳۰ ربیع‌الأول ‌۱۴۴۸
۱۲ سپتامبر ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/689136" target="_blank">📅 08:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689135">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFO2nSPj0EpJ9PYs6R5HAaFneZLTHEryCBokoDOWhxY7YKQs96Q7S8iu7OtgyBknKuPlyGcCtLk4qdwtwryEGLC7ho-Cy8kZsAYl7dfOVqk8ENZ1kmdE_TcVTvQ3d9Fk3Z6HKADMGv4QtxgsrxLkGQifRWRb6IkCJ3gUvdo52U2txrp4aoJe4FHd1SZPaQgSYC68UJelgo9BxE7qzeWSwqMyy0HOAvFV-ox9oDoJGVm19WxH6OOiIYIhnVw7z8bNNjZVfMb0BYN8DoRRlb1GkQF_tPGJ_a3dmn8bctWppUQEGHWgGlH9XacXYCTOGT4Wic20MdWDfL-nbpqYPCxgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
کلینیک دندانپزشکی کاخ مشهد
🦷
با مدیریت خانم دکتر آذرفر
✅
دندانپزشکان عمومی و متخصص درجه یک
✅
طیف کاملی از خدمات دندانپزشکی برای کودکان و بزرگسالان
✅
اتاق عمل مجهز برای انجام اعمال دندانپزشکی تحت بیهوشی و آرامبخشی
✅
انجام ارتودنسی و ایمپلنت بصورت اقساط
🔺
ارتودنسی
🔸
ایمپلنت
🔺
بلیچینگ
🔸
لامینیت
🔺
کامپوزیت
🔸
ترمیم و معالجه ریشه
🔺
روکش و بریج
🔸
جراحی انواع دندان عقل و نهفته
🔺
جراحی های دهان، فک و صورت و ...
☎️
05136028800-4
📞
09155671518
📌
مشهد، روبروی پارک ملت، امامت 22، پلاک 8، طبقه 2
🆔
@kakhclinic</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/689135" target="_blank">📅 00:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689134">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHRhTomn0Xlu4I_W_45Gra7tDcQ4DiI9bPiD03o0arww6p5iCj60WU__DRVd5SMc-R-6CuQkcMBNl61vEeUUXphHDcNws8-d4ZmtyER0osjZ1g4TJDRBuaFXo0bGP3ViCtJN7gN22QZC9Gt2CiZuLYsYrn19cbWCJ0IUGBV-ogwAMHngV4QU_ObXKKLsPRLNJObpkHF4b160kt9vBQRLsWi9_AKRqCKeekkbeZ8md3tZ3eMNs6H0bNvNf2UcVcjqqHP6JB3XHo-J1yG_VV1k-suIWoDRgLR4BhtUMIcXra0a4i3SUmARTVAm1w7sgbZ4s0sn_wZp4-p0EFdnsIA87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
اگه بین ۱۸ تا ۲۷ سالته
؛
این تخفیف ویژه توعه
دانشجویی و برای ترم جدید کلی وسیله نیاز داری؟
دیجی‌کالا
مشکلت رو حل میکنه:)
7️⃣
نگران هزینه‌ و زمان ارسال‌اش هم نباش
، اگر بین ۱۸ تا ۲۷ سالته میتونی با وارد کردن کدملی‌ات
اشتراک پلاس رو با ۷۰٪
تخفیف بخری!
پلاس رو با تخفیف بگیر و به صرفه‌تر خرید کن!
🛍
🪄</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/akhbarefori/689134" target="_blank">📅 00:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689133">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqkHGHd-9nsCsdRyYiJNSQSxJH9oojm_LcKo2ROsfUdc_vU3Uvr9cPjADF0qO-czxnGzBdtJdzc-3zfaYyQARFwM8sIDml5fvyM-nhF50mgfhugACiI7TBG2sIiSopkug7HN4DtO_9AAhm5yMaGQV3T7JzHPWJgplpBOl3bz_mrFAXYO5CB5VyF7si_J12s1HOuqT8VU9Pi2IKoHauAWWIn8ii7wgD7YgdJxBiW3TUN3WjqzlquPm8uv8d4xy3Okvy-TQzno4axhKdq5P7XparLZQhUmXv5-5U_mdBWNqg6tt7sCG1O9yKDvgnrioJi6JaxgiU1rLnpCmsOMoVw2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج دستگاه تست قند خون دیاباتان SMM 1000 +دستگاه فشارسنج بازویی دیجیتال
یک ترکیب کاربردی برای کنترل راحت‌تر قند خون و فشار خون در خانه. مناسب برای استفاده روزمره‌ی سالمندان، افراد دیابتی و همه‌ی کسانی که می‌خوان وضعیت سلامت  رو با خیال راحت‌تر پیگیری کنن
🔴
قیمت: 2580 هزار تومان
پرداخت درب منزل
خرید
👇
https://memarket24.ir/product/brief/63615/180124</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/689133" target="_blank">📅 00:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689132">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPyrHbxem96KATvkfLge78Y5ER6k0dCJ4_qgNdmWiEYoCCfaMevA37SR7-ddxQ6_Q2AVxI2I-SnvPz2zEqVUzAdYQxvchPBByimZDG7GAkk_SPB_apMVeoTjROOe2leKqaxQokradyz2szjjmYvLUORRraILNYLHTU7hVdZcaHwFvbERBmrlmaNMK0_NfPMH4nEDMZ59GLp1fUVmPjH3FMy5PjB2k2EvwnTxl1y7SiegWlCPwWKHhCu3IeXscYy-TAiY5H3-uNW8L6f_JlOEpcqNwwNMMYlx6qwspl7RROKQSzj7sRNdr1jb81MSQSHJh3k_96JCzIqXWNc_xTkkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیروز، ۱۱ سپتامبر، با غروب آفتاب روش هَشانا (Rosh Hashanah)، سال ۵۷۸۷ نو یهودی آغاز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/689132" target="_blank">📅 00:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689131">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb8vVVYQbXpCJmVLSlF2phcPAT9SmQGOAUQew0FnS2FmPa1GmiUfD6CWdYjd45mR0XARQbcAK1nw2aqyUy_OVXWbgOk7Ola6ylkeQC53ohZdgf9PM-02_U52QlsOdXMP-TOqld7cHNhsmu8QAlVTsJqObUU9IHmjx_h0k4WUuYC_uLqhJVvaGYjWN-ZxL0ZzYuJK7Ux7-aifxjn2KuKAHMoQ_7DrVBq7Big4kedxO-8pvL1eI8KaGdPTZEdHX6PKPpcjo7b9jH70t365CjV7O-gSh-__JSDxxrxBPe7mFBjoHxQcv6FNpDc3tsVbSFz9T41v_h8NV5gZcMi0zMOWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع محلی: انصارالله حمله‌ای نسبتاً گسترده در جبهه مأرب و کوهستان بلق غربی آغاز کرده و شهر مأرب زیر آتش سنگین توپخانه قرار دارد
🔹
همزمان، نیروی هوایی عربستان در حال بمباران المخا است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/689131" target="_blank">📅 00:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689130">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای وزارت خارجه عربستان: خط لوله «شرق ـ غرب» در چندین حمله پهپادی که از عراق انجام شده، هدف قرار گرفت و این حملات به مصدومیت و جراحات انسانی منجر شد
🔹
عربستان تأکید می‌کند که حق خود برای اتخاذ تمامی اقدامات لازم و تضمین‌کننده حفاظت از حاکمیت، امنیت و…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/689130" target="_blank">📅 00:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689129">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UG5fJHOjcZ0tQZoTFrCy54gigd1Z-f2xyB8rZTpkWPEYMxya8a0-zNP27CgibN4srQcg_xSA-I0ehDKrmrsGf1COvSi6akLeX9XJCi80zlg9cXKsVot6_V0r8BUqRP2ngjbNBb5LmYvCkz7Rwj1flBAAKZCoV0zUyDgd8O69qXtVdGrG-hpdPzEWRUCPmb7SSmoqLtJBGDeZC1zj0ykVRv9sU5xX0drccCEc1zHQRvYIyQ1xnynnIa7IwFEDU49sP9Al5oiPAPSXuCkY2TKO3cN45PuohM4lmQHaqAkbRi6SNgLh_39SdVb_f-T-OtfL1YeHRBh6jGrpwZLx2zWXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیبی و پروژه آبیاری عظیم «رود بزرگ مصنوعی»
🔹
لیبی حدود ۲۵ میلیارد دلار برای ساخت بزرگ‌ترین سامانه آبیاری جهان و انتقال آب به مناطق بیابانی هزینه کرد.
🔹
در سال ۲۰۱۱، تأسیسات مرتبط با این پروژه در جریان حملات ناتو هدف قرار گرفت و کارخانه تولید لوله نیز ویران شد.
🔹
لیبی پیش از این، در چارچوب مذاکرات بین‌المللی، برنامه تسلیحاتی خود را کنار گذاشته بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/689129" target="_blank">📅 00:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689128">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByltJgVlapghv5WIW1Qew0vVg1QwOOddpmhsnBNC5QDTHoBnpC1HtAcv1xWJgd57jIXprWI50NeyKwCb_EGCiWcpEJLafhPwxHDlnxY2glaViD4beazW7jB7hsxoD_OJwhCm-kHGzg0vau_WGwDFLHEFkCzM9YeJDAnj6omuteI02zBdsCd-dSc63oBbmPZacjI29UB4kXbGAtm8z7XIdc1p-4qfI6hXdYFILTHp4vz3ilbbuWzr6oMItoswwSS0Ksqw5EhjC19WsRGEvHORtLFQ_CGQGlKFUAJXknqmY3XR32KdyDl_Mq_0biJauA61cwSHM42ZC6ZSb7tMtmLCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فایننشال‌تایمز به نقل از منابع مطلع: وزرای خارجه کشورهای خلیج فارس برای پیشبرد توافق هرمز با عراقچی دیدار می‌کنند
🔹
این نشست قرار است روز دوشنبه در شهر ساحلی صلاله در عمان برگزار شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/689128" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689127">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449e1510e9.mp4?token=OzWi0aVOFCug8IKty0RAiOEKItSA8bxmyWsMpV0Wr7NAcIX7LZqs50S_We8xAIi_absUfhSegpyxLhnhxbEcbAoHb-yV6MQ85Nop7TGTXS2WnXBEH_JkH_WMYoq7Y8ZgajPAIB1jBCm0t6A87MI8viT3S4pfPNhc4RP2dWGfWK0WAIChcEH1Xz6e8Cs9g7hFeeXkvGe3XUogfJHi_b7HxSLIKR2LlK2XFaJMC2TKZfVbtAHuA3JChcOKK5RsHCuwxMMoL3QpkKg-K5GdoDdXF1XL-YaHTedpjtPBXX950NkwnjckBUNUE7lH5KSXo8DX6g88rOiWpxGVfif4-nyzUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449e1510e9.mp4?token=OzWi0aVOFCug8IKty0RAiOEKItSA8bxmyWsMpV0Wr7NAcIX7LZqs50S_We8xAIi_absUfhSegpyxLhnhxbEcbAoHb-yV6MQ85Nop7TGTXS2WnXBEH_JkH_WMYoq7Y8ZgajPAIB1jBCm0t6A87MI8viT3S4pfPNhc4RP2dWGfWK0WAIChcEH1Xz6e8Cs9g7hFeeXkvGe3XUogfJHi_b7HxSLIKR2LlK2XFaJMC2TKZfVbtAHuA3JChcOKK5RsHCuwxMMoL3QpkKg-K5GdoDdXF1XL-YaHTedpjtPBXX950NkwnjckBUNUE7lH5KSXo8DX6g88rOiWpxGVfif4-nyzUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از نبرد تن به تن رزمندگان انصارالله یمن ضد مزدوران سعودی و استفاده خیره‌کننده از RPG
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/689127" target="_blank">📅 00:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689126">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ3j7LcKkdEvNjMQ-ccpmAUD9bV5DRr9c4fNaRc1V3df2Sx8zJzE0l1JbgKgudlaxKdyYqeOrXOO74Wlk7d2n1DTUQ5O0-vV_D2U2vzfV_4ZeZJG3FupuOznXey2LIwRiDUOPlgQFDUAhTv8OlnfMhHiAzedyFdr-IjDbOHCBrU1ZBEqASoZtwmQ3ZbQYRbOyjyf7M4PFnL4ymXmBYtyBWLgtssyisfOnCmr-09XJG16s-EgepiBoy2zi01uvOUMJivUuRvIZBQqeMQbNIdYVEyijPj7p4NkskeJVjZyvvcOj1iw7dBG35lQXMrEgrgKHFEVKUFSHgUXcmJrlUPfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/689126" target="_blank">📅 00:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c03af870.mp4?token=Us4lgfFmQxnHyK8LIvNHYGdkMOA2r-wFKo1YVrM7XnUT5evEnPiyzV83xrFX1Lp_yFGynQodmBazYS8hC0FJRyKVn91YQwgobE7PTVJ0tcMZLnvUG-2g4gOKYu-x9OCQICOql8Hx419WurAEbvvCGBlU8-xu3xb9u8jEQybMsLh0SeTPnT_riSDrpb1sc5gJ6IOeWI8rTQTTuI9CthQ-R8nn8ONQyQkDQrIm14eRU2tRFXA1U1loaUYkEh5NrYgo0eEGMDRJknxRoZOpHgE0BTkPebwhk50ByAgHHitl3ePoUYqoP3yJALYUvhckM3oUwf20_GHfsEXo9ZqAG7QD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c03af870.mp4?token=Us4lgfFmQxnHyK8LIvNHYGdkMOA2r-wFKo1YVrM7XnUT5evEnPiyzV83xrFX1Lp_yFGynQodmBazYS8hC0FJRyKVn91YQwgobE7PTVJ0tcMZLnvUG-2g4gOKYu-x9OCQICOql8Hx419WurAEbvvCGBlU8-xu3xb9u8jEQybMsLh0SeTPnT_riSDrpb1sc5gJ6IOeWI8rTQTTuI9CthQ-R8nn8ONQyQkDQrIm14eRU2tRFXA1U1loaUYkEh5NrYgo0eEGMDRJknxRoZOpHgE0BTkPebwhk50ByAgHHitl3ePoUYqoP3yJALYUvhckM3oUwf20_GHfsEXo9ZqAG7QD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزارت خارجه عربستان: خط لوله «شرق ـ غرب» در چندین حمله پهپادی که از عراق انجام شده، هدف قرار گرفت و این حملات به مصدومیت و جراحات انسانی منجر شد
🔹
عربستان تأکید می‌کند که حق خود برای اتخاذ تمامی اقدامات لازم و تضمین‌کننده حفاظت از حاکمیت، امنیت و تأسیسات خود را محفوظ می‌دارد.
🔹
ویدئو مربوط به یکی از ایستگاه‌های پمپاژ این خط انتقال نفت که مورد اصابت قرار گرفته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/689125" target="_blank">📅 23:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689124">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLf4xnjpgAIIgzuFFCFiwJPB4hW0NPj_SLXa9KOn0pErXgw2e09EaRFXi0Tg0M2bFy3XIJZUOlZj32RGI37_n0MIr8LSYz91X4dM7M7TILv2is6-7yHGR21NBps7ub3MHlqrvNq8mvbZVqI5YJWn0nDLoWsZHA-bVfvgz9gv7TxczSF9UEq-n36BnSZ8-idYH_u8QxoodNW5flEFFqD03lbjraThPddcMnAaoBsqXkJ1FqR_AElM2gyTI_9JPPuSsFvW8DhH7hLS01BtP4w3ciYNZpO3Sqf_rYzfF52YkqaXrxGHXn1v408fXer3W_f_LMxKGpKlaWL90QUn4pmnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الکساندر دوگین، فیلسوف روسی: حوثی‌ها و ایرانی‌ها همه ماجرا نیستند. غافلگیری‌های جدیدی در راه خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/689124" target="_blank">📅 23:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689123">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
المیادین به نقل از یک منبع ارشد ایرانی: مذاکره تا زمان پذیرش شروط ایران امکان‌پذیر نیست
یک منبع ارشد ایرانی:
🔹
ترامپ شکست خورده تلاش می‌کند خط مذاکره را بالا ببرد تا کمی قیمت نفت را کنترل کند. ما بار‌ها اعلام کرده‌ایم مذاکره تا زمان پذیرش شروط ایران امکان‌پذیر نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/689123" target="_blank">📅 23:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689122">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا به نشریه اپک تایمز: ایران پایگاه ما در بحرین را کاملاً ویران و نابود کرد
🔹
منظور او پایگاه پشتیبانی نیروی دریایی در بحرین بود که مقر فرماندهی مرکزی نیروهای دریایی آمریکا و ناوگان پنجم ایالات متحده به شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/689122" target="_blank">📅 23:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689121">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ماجرای شهر | سرِ درِ تومانیان
🔹
یک بنای تاریخی تخریب شد؛ اما سؤال اینجاست: چه چیزی قرار بود تخریب شود و چه چیزی واقعاً تخریب شد؟
🔹
پشت تصاویر منتشرشده از تخریب «سرای تومانیان»، ماجرایی وجود دارد که برای فهمیدن آن باید به آبان‌ماه ۱۴۰۳، یک استعلام رسمی و اخطار شهرداری برگردیم.
🔹
در این روایت، سراغ همان اسناد و اتفاقاتی رفتیم که شاید در هیاهوی تخریب دیده نشدند؛ و چند سؤال را بی‌پاسخ باقی گذاشتیم:
🔹
چه کسی مسئول حفاظت از یک بنای تاریخی است؟
🔹
وقتی ارزش یک بنا رسماً اعلام شده، حفاظت از آن دقیقاً بر عهده چه کسی است؟
🔹
و مهم‌تر از همه؛ چرا باید میراث تاریخی یک شهر، بعد از نابودی‌اش شناخته شود؟
🔹
این فقط ماجرای سرِ درِ تومانیان نیست؛
ماجرای نگاه ما به میراثی‌ست که اگر امروز نشناسیم، فردا فقط باید عکسش را ببینیم.
🗞
اینجا ماجرای شهر شهر را ورق می‌زنیم:
https://eitaa.com/Majaraye_shahr
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/689121" target="_blank">📅 23:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689119">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VM4KuKY-CFcZwHb1jps7ca-AdyQpr4u1YUKkSYgfseh-0DzPrZ-cpDwKZRkj8czjgS2lhbpmqAYYiddhFXN_3mNoSCSjs8O5Rrix2uwJ5TsWr0aVsqbwynjnneA6gbLJd1JudZVcAJBAg-iD6OIlZ2ZL2xWf3XwMuELQQcwt0OGDx4kfmqghYc8T_O-QUDIgx3bijKLPy5B-J9DhtSAgN-VPYKzypZqkVidKI2HMqKG5naSV3nSPHqY-H0Sth7rYKT8F2uVB7m52TLRs6BELdootlBK_2UNRUIcIlvllG6snvjctgZchDI4mmpe7hyG-ZLqIVRMOzWLxH9k4yJE8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ck5H19o4FDt-6Vxr9jDoz-DOdDtxAMs6vCLyn-3hORkpoPRAjAxymXSjAPgkB015yV9GJ0nlfGNGJ2GVmsYNWfbokKgY-Mtk0Z014X2bY8D_lgdzDYSQGkyF_8LMyVLtRy8qVndEEgs9tqPAw6uI1WjCuNMzrAYUPGR5ywxejRBQj1SttGkltn69nNOTEJbx2lrZSfLEfxPJu8zZAisuAmMbjD8DUpR88ci1tbFewAxrEttvVpFh9Wyf-cSbTpsei6wEc_m33hMTILzydgNGRQQM1AjEy-zWI_fG-QJj8tpeHXc-pqe9m_FcmqENJp99c0E045v_sIiPRIuFVknopA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از تسلط نیروهای مسلح یمن بر برج کنترل تردد کشتی‌ها در تنگه باب‌المندب در شهر مخا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/689119" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54f1063ecf.mp4?token=fW_YBGITCnSgnoighV0ZDZUZ3J_Zs2elREBcrnw3G6lOWvN8USmFiYrS5fxe-VL6Bd-jCc6ky_CJjfAxtBFw-0KfDtAbrVmPibRseyTKyvDODLsNZ5fLGJohKqcJd0L1xmhOCymzxzx9b20N2L2nbsrXCH44dU0Trv_4toCXkL7BJ-yWYDUR2cNTBl1GCgXzfTRmRJQhqWaIPNdqybjt0OW_U3FWGgC1DAlKCW8OwejqlspU2gY8Vz10ohMjy7EZZcZB2XFtDXKDWyCJpolbxmR--dXRMY-1xRzJy9lRoWCT1bp36XvJUBsXHZiAxe3nn0bW62XdE1VK541wcM79qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54f1063ecf.mp4?token=fW_YBGITCnSgnoighV0ZDZUZ3J_Zs2elREBcrnw3G6lOWvN8USmFiYrS5fxe-VL6Bd-jCc6ky_CJjfAxtBFw-0KfDtAbrVmPibRseyTKyvDODLsNZ5fLGJohKqcJd0L1xmhOCymzxzx9b20N2L2nbsrXCH44dU0Trv_4toCXkL7BJ-yWYDUR2cNTBl1GCgXzfTRmRJQhqWaIPNdqybjt0OW_U3FWGgC1DAlKCW8OwejqlspU2gY8Vz10ohMjy7EZZcZB2XFtDXKDWyCJpolbxmR--dXRMY-1xRzJy9lRoWCT1bp36XvJUBsXHZiAxe3nn0bW62XdE1VK541wcM79qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: تحولات یمن ربطی به ایران ندارد؛ آمریکا عامل اصلی اختلال در صلح است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/689118" target="_blank">📅 23:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔹
خبرهای متنوع هر روز را در خبرفوری کلیک کنید
🔹
🔹
چرایی ترور علی لاریجانی از زبان رئیس سابق MI6
👇
khabarfoori.com/fa/tiny/news-3244385
🔹
نتانیاهو به‌زودی می‌میرد؟
👇
khabarfoori.com/fa/tiny/news-3244472
🔹
لقب تازه برای روحانی در تجمعات شبانه
👇
khabarfoori.com/fa/tiny/news-3244435
🔹
پشت‌پرده پروژه جدید جاسوسی سیا | ترامپ به‌دنبال چیست؟
👇
khabarfoori.com/fa/tiny/news-3244449
🔹
مرد پشت پرده حملات به تاسیسات هسته‌ای ایران | شلومی بایندر کیست و چه نقشه‌‌ای دارد؟
👇
khabarfoori.com/fa/tiny/news-3244415
🔹
خبرهای جذاب را هر لحظه اینجا دنبال کنید
🔹
http://khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/689117" target="_blank">📅 23:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/689116" target="_blank">📅 23:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2J0Ilk3fxjJIK25qvw3-1N--kDoFdmlGgvIsoRl-Xjwi_aQmbgUwcRa9lx7KxvSF4AqcV82D8m7j1xE-Km6f7uiVdd4ZhnE4X-ajrnSb3VWcLVsXdQ2-5DVgyHimT-mWHfZK5ZV7u-LEGE6su4hO77iaQh8tK69lJ52QEvhD0MEo5LPLvmGjU_GZB7VXxwJWq6Ig39w8xwunAv_nmkUh2Yx3FU2zCymHOdLNRyLDNCd02hqrxM5lreekJpfrIdJNPUJcH3dKMbEuflaWdUbU4kHutx6gr4Mpjy3DajzurR2yiQxQczXDwiX8CVx8dePHVgJWzoFe36fzeMSVZmaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو به زودی می‌میرد؟
🔹
نتانیاهو در جریان یک جلسه دادگاه در می ۲۰۲۶ ادعا کرد که در اواخر ۲۰۲۵، در جریان آزمایش‌ های دوره‌ ای PSA، «لکه کوچکی» در پروستات او شناسایی شد که معلوم شد آدنوکارسینوم پروستات در مرحله بسیار ابتدایی است. اما ماجرای بیماری او چقدر جدی است؟
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244472</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/689115" target="_blank">📅 23:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms2o0SkuiArtThBOYldC3ZW3Ah7jRJPxUX_E576MD8rDD6QHiFRMUbH4VEYpqZnlSmC5mbYXhv1s97DN45dSdJZdF13bnce5ypl60ZbJ_CYZ8NaQQ6O7O9DjSw3gs5hkdTbN-dDYSJDE52A-lb7GQlZWaXjmyLOJPqqW9gNItlCKU_SUGHDvWxd4NFcLepRzPTldvhE84SUpoT9pqYl18XccJfGA1u4C96HUw1LmIZMGJqiZ5UOKh_P3n8ln4frhMnp1Dxgv456JSD6KX52eDLoIKIT9lfsUbUNliFG8rmE7ylJm_zLqdefTw-Q7epMYPfKJsIigt9CZHYZQeAwK8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب فرش اشک حرم حضرت عباس (ع)
یادگاری نفیس از حریمِ وفا و ادب.
این قاب، جلوه‌ای معنوی و چشم‌نواز از حال‌وهوای حرم حضرت عباس (ع) را به فضای شما می‌آورد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۴.۵ × ۲۰ سانتی‌متر
▫️
جنس قاب: PVC
▫️
طراحی شکیل و مناسب دکور
▫️
انتخابی ارزشمند برای هدیه و یادمان معنوی
💰
قیمت:
۱.۳۹۰.۰۰۰ هزار تومان
✅
قیمت با تخفیف ویژه
۱,۲۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/689114" target="_blank">📅 23:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اجرای ویدئو مپینگ بر دیوار ساختمان بانک ملی ایران، شعبه بازار تهران
🔹
به مناسبت
نود و هشتمین
سال تأسیس بانک ملی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/689113" target="_blank">📅 23:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689112">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febe288c78.mp4?token=ao_kPw3HtQmpxWsw9zRcEO1ISCihjUM5B2X7vhC_Y08ydrL5mpvOzuaS04Kh2VC3YwyZE17kxUVeK8AXYWolZInHbq1dxi37ji1e57v7Al8Y8yFwuuXN3lLpjP9rPpl3ql2DfU8yxEGhe90-I1KYi9ROxR1tsBAifbqZ1MLR7-SIO8Do2QuTcv2o_oNHZG9Zx610_nGWUxHjwk0adSm_2GnqAX3xD0xEqn4_stsBqxe92tRBcjH1RVt02zYTAhGZlnt_rKmkyW5fCZMeJDpQdFEUOE2ojgYwiFPotTX5-XsD9c8fqCGi6p3iHhp1HIwwZDqAJCLG1FFiLWiyWWck4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febe288c78.mp4?token=ao_kPw3HtQmpxWsw9zRcEO1ISCihjUM5B2X7vhC_Y08ydrL5mpvOzuaS04Kh2VC3YwyZE17kxUVeK8AXYWolZInHbq1dxi37ji1e57v7Al8Y8yFwuuXN3lLpjP9rPpl3ql2DfU8yxEGhe90-I1KYi9ROxR1tsBAifbqZ1MLR7-SIO8Do2QuTcv2o_oNHZG9Zx610_nGWUxHjwk0adSm_2GnqAX3xD0xEqn4_stsBqxe92tRBcjH1RVt02zYTAhGZlnt_rKmkyW5fCZMeJDpQdFEUOE2ojgYwiFPotTX5-XsD9c8fqCGi6p3iHhp1HIwwZDqAJCLG1FFiLWiyWWck4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: تحولات یمن ربطی به ایران ندارد؛ آمریکا عامل اصلی اختلال در صلح است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/689112" target="_blank">📅 23:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689111">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCIYPjtLUz0jGU9uqfq99eud7TbELb1jNBW2IwWAXVu_P1DIHn8syNt3wkqasTm1c6eMu8vHa7PNlyMnft_oVhNToUzAy4NbuUpS_0aPLIYTPY9ZYZjrSx9zTCWypo-Xh_baeUbFbbBU_uCTPI7itrCQeUCe4GRQ2ITX86gMIf6LJYdtQsWY_KBtkdLfyDLZbpU8SKsBOpzaLGWPFstg0vMt8k3F5oUHhh1eLb1cXDzRMftmKBVIdbxNcFktuBp25Cg5wWAvVIs1ntxSntY4HkCg6qzRmCt9ltIjN1guCgMOEO20aY7mcc_E4onVs8xo7Q80TSR3W4CRaILnUEofwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کره بادوم‌زمینی رو با چی بخورم
⁉️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/689111" target="_blank">📅 22:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689110">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
🔹
۱۱ تایید
🔹
۲ مخالف (روسیه و چین)
🔹
۲ ممتنع
🔹
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/689110" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تد کروز: احتمال اینکه ترامپ ایران را به آرمان‌شهر دموکراتیک تبدیل کند صفر است
نماینده مجلس سنای آمریکا:
🔹
احتمال اینکه ترامپ مانند کاری که در عراق کردیم صدها هزار نیروی نظامی پیاده وارد کند و دست به اشغال بزند تا سعی کند ایران را به یک آرمان‌شهر دموکراتیک تبدیل کند — احتمال این کار صفر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/689109" target="_blank">📅 22:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689108">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
حاج رضا برکتی: مادر هر روز با عشق، انگار برای یک سلبریتی غذا می‌پزد/ تا هست، دستش را ببوس؛ یک «دستت درد نکنه» کمترین جواب این همه محبت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/689108" target="_blank">📅 22:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689107">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما در وضعیت نه‌ جنگ، نه‌ صلح نیستیم؛ ما در وضعیت جنگ هستیم
🔹
تحریم و محاصرهٔ دریایی به منزلهٔ جنگ است و هر آن‌چه که ما در این وضعیت انجام می‌دهیم نامش دفاع است.
🔹
منشا حمله جنایتکارانه آمریکا به لامرد، خاک یکی از کشورهای جنوبی حاشیه خلیج فارس بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/689107" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689106">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان غربی(Admin)</strong></div>
<div class="tg-text">♦️
نهمین جشنواره انگور در چی چست ارومیه
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/689106" target="_blank">📅 22:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689105">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: نتایج اولیه کنکور اوایل مهر اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/689105" target="_blank">📅 22:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689104">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
عربستان حمله به خط لوله نفتی خود را تأیید کرد
وزارت انرژی عربستان:
🔹
خط لوله نفتی شرق به غرب این کشور در ریاض و مدینه منوره، روز پنجشنبه، هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/689104" target="_blank">📅 22:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689103">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: شهریه دانشگاه آزاد بین ۸ تا ۳۶ درصد افزایش یافته است
ابوالحسن مصطفوی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
شهریه ۳۰۰ میلیون تومانی مربوط به پردیس‌های بین‌المللی دانشگاه آزاد مانند کیش و واحدهای خودگردان است که برای جذب دانشجویان خارجی طراحی شده‌اند و ربطی به دانشجویان داخلی ندارد، در واقع این شهریه برای دانشجویان خارجی بسیار پایین است و باید حداقل ۵ هزار دلار یعنی حدود یک میلیارد و دویست میلیون تومان باشد تا با نرخ دانشگاه‌های ترکیه که ۱۱ هزار دلار است رقابت کند.
🔹
شهریه دانشگاه آزاد در سال تحصیلی جدید بین ۸ تا ۳۶ درصد افزایش یافته و این رقم بسته به رشته و شهرستان متفاوت است، اما خبر افزایش ۷۰ تا ۱۰۰ درصدی که در فضای مجازی منتشر شده صحت ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/689103" target="_blank">📅 22:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689102">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d409fe30f3.mp4?token=GS7fNFv1Vl2OA4InuAVoOp0uzY33bUIgti15-ARECIpuOgSYBCZr7XZXk2W943boo-Wu4Z4NEfgBnJYYXY48QMgmwo-x8IdJXRiDrySLReCwAHAh-Y7RkT0gSuB87aIbiVqtf2Vvvfk6x3EpWx6VDb0izT3tF9GjmweN1rodfmwoZEeAnWY1Ru0oEZdYFvvtkkbxluFLAILEE0lDOBELo5tXzu4E__atfh_FHMwmw_m9VwYA0RYr7HHgv3UBMfv-7fxJ4EmSXTJs_5IWsDao27dmAE04QNCXZG-pJnGC4q1FuSo7ZXLVngPPnhy3HLChxlbkpiX2NSbvgYI3k51gXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d409fe30f3.mp4?token=GS7fNFv1Vl2OA4InuAVoOp0uzY33bUIgti15-ARECIpuOgSYBCZr7XZXk2W943boo-Wu4Z4NEfgBnJYYXY48QMgmwo-x8IdJXRiDrySLReCwAHAh-Y7RkT0gSuB87aIbiVqtf2Vvvfk6x3EpWx6VDb0izT3tF9GjmweN1rodfmwoZEeAnWY1Ru0oEZdYFvvtkkbxluFLAILEE0lDOBELo5tXzu4E__atfh_FHMwmw_m9VwYA0RYr7HHgv3UBMfv-7fxJ4EmSXTJs_5IWsDao27dmAE04QNCXZG-pJnGC4q1FuSo7ZXLVngPPnhy3HLChxlbkpiX2NSbvgYI3k51gXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازخوانی هشدار ۹۰ روزه در خصوص علی‌الطاهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/689102" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689101">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIbz9iOly0Vb0RlhtHkyujEZKt3wlhEnZmoRTsMdkZBPgbx8O2TLkbAFys1MQ446iOawnIJEKp1AXMptF-R0aTfxJgtGTrCaGmdroB47lg0gZWUQ8sCNlBZKeMSg_i0ZJZGDOSolEOT8aTpgaif8I1ScVvDgpBU4XwGunmHxAorCHc4rbpVdiu9B4ufGkT13ynNo3XDtkXsJiXYdIgETeQ9ZcmbIeB9RI9TgNJhH7-Hd_fj8crw7NdiT1jIVW_K6mhIl76X3rLdk8GGir6B_u5pnad4NDST-Tn5j3rWSLYNq5_c_xubZ6VHLYKOZ29KWbwSKCyWJkz0pq7UpeWge2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصرف گوشت فرآوری‌شده؛ زنگ خطری برای سلامت معده و مری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/689101" target="_blank">📅 22:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689100">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
طائب، رئیس سازمان بسیج: نباید از روی سستی و ترس با دشمن مذاکره کنیم، ولی اگر دشمن درخواست تسلیم شدن یا مذاکره کرد، باید با قدرت و به قصد گرفتن حق خود با او وارد گفت‌وگو شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/689100" target="_blank">📅 21:54 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
