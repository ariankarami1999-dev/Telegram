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
<img src="https://cdn4.telesco.pe/file/gWifMOeti4AiOPQU_FI4zCHOaAdgxrqeXbzynWSQUzlWwRcfBCYJjWQLBiTFbhnTA0dLHo39_FkghtME6cOEjBmunTvvIsTTFdmshRgxwbYIShUBuv43MKGn45qxcmb9-sexRQAzyp7FGXVU_YPlnglqMQoJvF7RSvCvsy0bgJdu0E89DghmXRVX-gHahk-9-9TeinoVcwtDJA-RzYD9w9pqDo5091w87TLKGzn1Isef0sko3QxWZnq944Z61xBKrB8WgGwRPrxpyAYY_P4kVCIbsFgjUjcK0LZI0iVcTTDRNr4OTtCJxm_MWkEQAZH_SSnjvlL_dkUgiFv1-C7rzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.01M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 11:10:37</div>
<hr>

<div class="tg-post" id="msg-679355">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f1224bf2.mp4?token=tG8sqbXFkUf6MMr2muvj5S6ZXoHX3zoBsYHzPOtUgKUgU7H5Bp2td76oew3ues_ABrVvIjrZmo_tGDw5nagRNxfOKoy6y4LFsBKpvlrPlFCnpA0luNsLut1rte8Wv4MgVdpiY93XDP9sMO_J_BcNM8l49o7B-Zd_MuLdvQmfuRn5DVjsoqUnJ5ROeG64MNUE1dIwOSJAG719VXFAyoKdVQEQNJlIU8gUZ8MEjnexxwbELM_QjpEOaTW7VIbH2WteuelUDCGreLktPzZNwVpNI3nb9A0XBauBVeXMls_JIFBJwFZGKcWDvHCare8xo15FkrfNhRRTRJyzBLldEGXZFk48Hyb4MDxCv4xMHP3nDb3fTe43QVL3HCLPxX2rOzFRGHakVA3Rk9UVpx0-dlz_8MQQeabHILkeeiFFG0LcoKydrFBz7r5iWkhJVieckwQ8Dk38iOct7vRjUO9kjY5Ntxv1ZOcyuIjryfejTU06k0siRW0VdVLinfzsV3RrIesViT5wMEFq6SdrGM0MXqtHNBQiDUyMOE25HMa5r1qXE7iOE1B450AW_PXSvqvoGDcp8zEweCmRZfGgOr_Pt_QeL8Ow95sOuL1UGxv8DAFNQnfPUGgWebgdWf08kJc3NCDr-hJSI9Zn-F4GiHVn9seQd2MmHl6gSY1YLOY0ADGWg_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f1224bf2.mp4?token=tG8sqbXFkUf6MMr2muvj5S6ZXoHX3zoBsYHzPOtUgKUgU7H5Bp2td76oew3ues_ABrVvIjrZmo_tGDw5nagRNxfOKoy6y4LFsBKpvlrPlFCnpA0luNsLut1rte8Wv4MgVdpiY93XDP9sMO_J_BcNM8l49o7B-Zd_MuLdvQmfuRn5DVjsoqUnJ5ROeG64MNUE1dIwOSJAG719VXFAyoKdVQEQNJlIU8gUZ8MEjnexxwbELM_QjpEOaTW7VIbH2WteuelUDCGreLktPzZNwVpNI3nb9A0XBauBVeXMls_JIFBJwFZGKcWDvHCare8xo15FkrfNhRRTRJyzBLldEGXZFk48Hyb4MDxCv4xMHP3nDb3fTe43QVL3HCLPxX2rOzFRGHakVA3Rk9UVpx0-dlz_8MQQeabHILkeeiFFG0LcoKydrFBz7r5iWkhJVieckwQ8Dk38iOct7vRjUO9kjY5Ntxv1ZOcyuIjryfejTU06k0siRW0VdVLinfzsV3RrIesViT5wMEFq6SdrGM0MXqtHNBQiDUyMOE25HMa5r1qXE7iOE1B450AW_PXSvqvoGDcp8zEweCmRZfGgOr_Pt_QeL8Ow95sOuL1UGxv8DAFNQnfPUGgWebgdWf08kJc3NCDr-hJSI9Zn-F4GiHVn9seQd2MmHl6gSY1YLOY0ADGWg_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوه‌قضاییه: ساعدی‌نیا اجازه کافه‌داری ندارد
🔹
بر اساس حکم بدوی، صادق ساعدی‌نیا از فعالیت در حوزه کافه‌داری محروم شده و دستور پلمپ تمامی شعب کافه‌های او همچنان برقرار است. بر اساس اعلام مرجع مربوط، در صورت فعالیت مجدد واحدهای متخلف پلمپ و جریمه خواهند شد.…</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/akhbarefori/679355" target="_blank">📅 11:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679354">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای ای‌بی‌سی به نقل از مقامات آمریکایی: توافق ایران و عمان ۶۰ روزه خواهد بود و در این مدت برای توافق بلندمدت، گشایش کامل تنگه هرمز و ادامه مذاکرات هسته‌ای تلاش می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/679354" target="_blank">📅 11:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679353">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyxJXOrN7NTMy3aCKSe640nBat-pE5UZhsWPuYouMREKhCFTUSOLGkiBWoXjesRsC7yKGeG5ANOVJ4GCHyHX3OF33ecLASa1EYLuRzVO87GDYCxT54X9flOt-gIiAp04YEkrAQTXSGdVrDKPKTOekVHVoqEms8lj-8TRCUvqvg7pvJ2J0or2__u6asnb9IVSFvBqBjO83XMwgiosoCaJCZGgclnWd_emRqwOVdYY1du_0B0zmMC100XKXnvJnfmXkt9Zw9r_UPTNwCqemWOYjXtSjhlv3ugc7Cp4BN9MVEDrbF2zPMG_tu-ffZvyPvEQLBiBfL5ErjMEGIiyAkNU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأیید یک مورد ربایش و قتل؛ تحقیقات برای شناسایی عاملان آغاز شد
یک منبع آگاه با تأیید ربایش و قتل حمیدرضا رجب‌زاده:
🔹
او چند روز پیش ناپدید شده و پس از آن ویدئویی از لحظه قتل برای خانواده‌اش ارسال شده است.
🔹
تحقیقات پلیسی و قضایی برای شناسایی و دستگیری عاملان ادامه دارد./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/679353" target="_blank">📅 10:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679352">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
آتش‌سوزی یک کشتی دیگر در تنگه هرمز
🔹
پایش‌های ماهواره‌ای از آتش‌سوزی احتمالی یک نفتکش در مسیر جنوبی تنگه هرمز خبر می‌دهد؛ شناور اطفای حریق «ادنوک ای‌آر۰۱» به محل حادثه اعزام شده است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/679352" target="_blank">📅 10:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679351">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
دریاچهٔ ارومیه جان گرفت
شرکت آب منطقه‌ای آذربایجان‌شرقی:
🔹
حجم آب ورودی به دریاچهٔ ارومیه از ۴.۵ میلیارد مترمکعب در سال آبی جاری عبور کرد؛ این میزان، بالاتر از حقابهٔ تعیین‌شده برای دریاچه بوده و بیانگر بهبود شرایط آبی این پهنه نسبت به سال‌های گذشته است.
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679351" target="_blank">📅 10:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDPuWJQ70JSlCafaRofke-aTATsG5jYI1ivaQcLZv7DGvn1GTYsxoifH4kImXgtLQ6z2lvrdRlzkhIwg7xpZ_F1WGH-_h_qlb8ro8cDNSxHO6nGeyCQwEe2wuGCtqdrjMerqsBMRaSr-cNEPKeWCXAFk65vzGQ2n2z1Qc1DdCeDzqeF3cLyfpcatz6V_remiYzGz3VEHOeqxMXdJdWZ1mCfGhGtya2TMJNXZ3PR0S-eTDB-_OMKi3gi4NXJ9tY6TuQTKQQ87kpoeqvrYxZXo2jCLzaBJkVSx7lsgNsroS-wa-PKd64HwxJwDaKzbAygfN9jkHF4ZCqFKx-R6xEXtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPJhCx1UK-Qn5IchVolLfxZEkVmSBQup8tl7Ko0gG_LlrAs0x3LYBdDbokvtMxiZCjSRT1KzKHhJbjPcPvbwyH9KWdONIsyBul_LTcYwMzrzpRVSQO6W6pF3IV5YYlAOmzeMCrrQC7xFtYbXdZO7sdfd6c_XeMp86yyZXADfl1vhF48Mb6-gbzRnQXSOPFHpKXnkirVvvTtRpig0DjvqkAq4JSA1uU0q6h67eLgKxSUolzvE_H9TIBeXRyeRU6Tgk5yi0IrtlHmKmHwGJKep8nvBcmrPGS3oMjh_mQY20zrCq2xD8y4uvM0PuzRj4xs68nz-XukcM0DgegDoOo4ZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0bPOdDkSBy9IcBa2jEvw6XXSOyJkeUXBdC9Vwfxet0v_ZZYGEMoScEo7R6B0NK8G-jav3RNaNoePx32hYTMa_2KavwDRRUVlyWAoJUC823LiqCHzAkqgnkCRNgYHloPMk_Q4X9zFRKMGlDqnfAJ1l3ujrC8gNWD9ih1EEif9uuPjEZNzYhTZ0Pn04C4q6GKBOp2Ko__TIfM8--zkB3vu14wTPw1hJ8JUniwHkzPK422ejXk_5QZtGgUqaSL0PpTs429emeG0zg-BT2Vq-9ZCrbI6O0VKCkmqAYtaYpJkT1N65n-aim-y5ZPZdKNDFsyLUF8Ch6krzksKty6edoGoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دفترچه‌ای برای گوشه‌ لپ‌تاپ!
🔹
یک طراحی ساده اما هوشمندانه؛ دفترچه‌ای با برش زاویه‌دار که دقیقاً کنار لپ‌تاپ قرار می‌گیرد، بدون اینکه مزاحم کیبورد و موس شود.
🔹
گاهی یک تغییر کوچک در طراحی، می‌تواند یک وسیله معمولی را بسیار کاربردی‌تر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/679348" target="_blank">📅 10:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679347">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سپاه از احتمال شنیده‌شدن صدای انفجار کنترل‌شده در جنوب اصفهان امروز ۱۷ مرداد خبر داد.
🔹
شرکت ویندوارد: عملیات‌های یمن در حال نزدیک شدن به آب‌های عربستان است.
🔹
معاریو: حزب‌الله در حال تغییر قواعد و به چالش کشیدن اسرائیل است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679347" target="_blank">📅 10:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679346">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
رویترز: قیمت نفت روز جمعه به شدت افزایش یافت، زیرا معامله‌گران همچنان در حال واکنش به ابهامات پیرامون تنگه هرمز و مذاکرات ایران و عمان بودند
🔹
نفت در پایان معاملات در این روز، ۸۳.۵۵ دلار شد، یعنی حدود ۵.۷ درصد صعود کرد/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/679346" target="_blank">📅 10:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q99UrFn63IZlP6U4FhTrwV8BquodefjJgZYOnFbBIv0N3MMKsrC1NThUl8za5CU2KQY3aqxngFk3MlKnHRURVXOd-Oo1XAx540sdvcXtCLwxlq1F7WB-P4dIFw4tIaeY3SVBxp6MStpYKXO3cUE1EOZX_G8NJSNtvz56AQx7rzVzJab6s2mGTDE1rEvtW7Vc0bPsF9n639l7jc16Ni5B9uUX2aYdMlL7L4ZY1DEM1v4yV8SfMsf6TCgo_01pBDkwiugBR2IFIuZQqvkrJiaEJN0K8P64uZHFFnXswIbfZ2zYOJLVrqMmvwRXqIRw4iPDKivwFL91fQqOTM_R8hPKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دلایل پارگی رگ خونی در چشم؛ چه موقع باید به پزشک مراجعه کنیم؟
🔹
فشار خون بالا
🔹
التهاب ملتحمه
🔹
استفاده نادرست از لنز
🔹
دیابت
🔹
سفت شدن رگ‌ها (آترواسکلروز)
🔹
تومورهای ملتحمه
🔹
اختلالات انعقاد خون
🔹
فشار شدید مانند سرفه شدید، عطسه، استفراغ یا حتی یبوست
🔹
برخی داروها مانند داروهای رقیق‌کننده خون و آسپرین
🔹
زایمان
🔹
اگر رگ خونی آسیب‌دیده در این مدت زمان بهبود نیافت یا متوجه هرگونه کاهش بینایی شُدید و یا احساس درد کردید، باید فوراً برای بررسی وضعیت خود به پزشک مراجعه کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/679345" target="_blank">📅 10:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
الجزیره: تردد کشتی‌ها در تنگه هرمز طی این هفته باز هم کاهش یافت
🔹
بر اساس داده‌های تردد دریایی، روز پنجشنبه تنها ۸ کشتی تجاری از تنگه هرمز و ۲۶ کشتی از باب‌المندب عبور کردند./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/679343" target="_blank">📅 10:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679342">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
رئیس فیفا دست به دامن سگ زرد شد  بن جیکوبز، خبرنگار انگلیسی:
🔹
جیانی اینفانتینو قرار است با مقامات ارشد دولت ترامپ دیدار کند.
🔹
او به دنبال جلب حمایت برای ادامه فعالیت خود در فیفا است.
🔹
اینفانتینو در حالی که فشارهای فزاینده برای استعفای او شدت گرفته، با فدراسیون‌ها…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/679342" target="_blank">📅 10:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679340">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obeFvs7ozIcS2wFBXQyjMTjfUmVRUGiIwDfAEsteP9xu7J04Ab4WQkqKN3BXfeCltoidgY8QBhhnsRsQpPGGt9SdBdFOttoL2UifZmCBAInWfrR1ERY7oGKeHJ_Hlo9CJSxh0oZ2-lxjPqDVyoElBFc9PMLIVEcoN12NmnLGURYb6EmTKshNAhihkXn-KVK3EkWnbwD2n0fheQhcjQS8rr8ktUdg-gcHGkQr0AxwLZaFETyjsPPQIq1h8SX6gy5vId7-lrZff3KUVMdVFcq5V3WoJ2yqWdlPCcFjf4TZP4919l1G56GX7-TbfqETHdGrOoNxQ6R1Sb-yQvn8l9iFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ سناتور آمریکایی برای توقف جنگ علیه ایران قطعنامه ارائه کردند
🔹
۱۱ سناتور دموکرات آمریکایی با ارائه قطعنامه‌ای در کنگره، خواستار خروج نیروهای مسلح این کشور از هرگونه عملیات نظامی علیه ایران شدند.
🔹
«جان آمریکایی‌ها از دست رفته است. قیمت بنزین و کودهای شیمیایی به‌شدت افزایش یافته و ذخایر تسلیحاتی ارتش ما تحلیل رفته است» این اظهارات سناتور آمریکایی جان هیکنلوپر در پیامی در ایکس است. او در ادامه نوشت «به این جنگ پایان دهید. همین حالا».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/679340" target="_blank">📅 10:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679339">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea6ad6f88.mp4?token=QmGFOchddXOV6kYNw1N2QDYNpPAsGGnirePmBrAPC6lFN_eFrci1zjZr-KcKnqbzIYTKPxW0y1bQ2KOQofTLrztCUldAgsgwwTaBokSQjLivi3_38WL-xU5qrItMCqBBDmte5Oqy73RuSAFN86eZJasvGo_1G3W-iiHyd5P0LBl3hHvYHqC3-Mh6sibSba0YVJvb_T13pIDisJM5aEBQ4YFY1vm72YJIeJyA-v6kRVdO6PCLc8imcn3IE9DSmLJXpH3onQPc6ZuirLe0twvO34iPQVbxq1VCIHECfNqJ5eU_d1EAkXYlXh4DZ36QocHaav_nZn9CWfstZvRHFcApIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea6ad6f88.mp4?token=QmGFOchddXOV6kYNw1N2QDYNpPAsGGnirePmBrAPC6lFN_eFrci1zjZr-KcKnqbzIYTKPxW0y1bQ2KOQofTLrztCUldAgsgwwTaBokSQjLivi3_38WL-xU5qrItMCqBBDmte5Oqy73RuSAFN86eZJasvGo_1G3W-iiHyd5P0LBl3hHvYHqC3-Mh6sibSba0YVJvb_T13pIDisJM5aEBQ4YFY1vm72YJIeJyA-v6kRVdO6PCLc8imcn3IE9DSmLJXpH3onQPc6ZuirLe0twvO34iPQVbxq1VCIHECfNqJ5eU_d1EAkXYlXh4DZ36QocHaav_nZn9CWfstZvRHFcApIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موجودات عجیب و غریب خلیج فارس
🔹
لیسه دریایی
🔹
عروس دریایی دکمه‌ای یا چشم زخمی
🔹
عروس دریایی مهتابی
🔹
حلزون تی
🔹
شقایق دریایی
🔹
خرگوش دریایی
🔹
طوطیای دریایی یا خارپشت دریایی
🔹
پاتریک
🔹
خرگوش دریایی سیاه سم بنفش
🔹
ماهی گلخورک یا اشلمبو که از قدیمترین موجودات دنیاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/679339" target="_blank">📅 10:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679338">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn6N4qlCvDnIOEOWzcedXohXJ2m5OeYU86c4RJO3fUbjH1aenfqSAnf18hHZgDEN_S2zxXCpQfdulqaXDYZkXgeqyZIzzvaQat7GjcbYe9Q_TNk1Rt9s9QsN8_WMdk_p5ohhHZkhqWAQAaIJmJxMQvcDjHRvU1ssKw9VGCQmwjB7_x3Gf1vSFVf0BvkDBBoNy8_TS8DXss6mlFd8vFoXO8BVFVI0balNzV5Y6p7TpJOlB_bhyMKTRm9sb2cWZ7pDQ65wg3Cd0tfrtttLzd4ZMGuZqvd-MxMkznTUaWsO27QkNReJWMgUfLSqy06r6GE9kphjvoi6TbA_29midEOC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
فروش ویژه فرش سجاده آریا | طرح ویژه دهه پایانی صفر
⏳
این شرایط ویژه فقط تا سالروز شهادت امام رضا (ع) برقرار است.
🔥
فرش ۷۰۰ شانه بخرید، با قیمت ۴۴۰ شانه پرداخت کنید.
✅
۲۰ تا ۶۰٪ تخفیف
✅
خرید مستقیم از کارخانه
✅
فروش اقساطی
✅
ضمانت ۱۵ ساله
اگر به دنبال فرش سجاده‌ای با کیفیت واقعی و قیمت اقتصادی هستید، همین الان تماس بگیرید
📣
درخواست قیمت و کاتالوگ فرش سجاده تماس یا ارسال عدد  1 از طریق
👇
شماره: 09128044740
آی دی:
@Farshsajadeharia
💫
💫
فرش سجاده آریا
💫
💫
https://t.me/aryiacarpet</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/679338" target="_blank">📅 10:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679337">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075cad6e21.mp4?token=Iadx66-l9wG-RaLoOC0QBdduYEhgWLwmmd46-TEZp7wXT7qT91tJ_YF0gu7G5cVakacGjm61sXZUP8RzWttOK7N6CATkxNet7jHPh1Iugz4piyFIJWdpZ_U9CkwSga4YjxGVHD0RRTaAnTwU2Bd5SOv4jFOutTKSX4q__NaUZ_Q0SqP406QR7heexLPW9ncU3lddDJrUcnb-WLHU1mmXCbOKtXX8I1b0jliMh7XfoCVeZ1CJGsAYpweuoyzA7MTbuRi3Y10dJ0eWrDbdAAenmWSF03IxSHwRG8eEtvVtBPanuVw4udWcfGGZShu0xaQOEv5o1coE28H3o4UTxXTrUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075cad6e21.mp4?token=Iadx66-l9wG-RaLoOC0QBdduYEhgWLwmmd46-TEZp7wXT7qT91tJ_YF0gu7G5cVakacGjm61sXZUP8RzWttOK7N6CATkxNet7jHPh1Iugz4piyFIJWdpZ_U9CkwSga4YjxGVHD0RRTaAnTwU2Bd5SOv4jFOutTKSX4q__NaUZ_Q0SqP406QR7heexLPW9ncU3lddDJrUcnb-WLHU1mmXCbOKtXX8I1b0jliMh7XfoCVeZ1CJGsAYpweuoyzA7MTbuRi3Y10dJ0eWrDbdAAenmWSF03IxSHwRG8eEtvVtBPanuVw4udWcfGGZShu0xaQOEv5o1coE28H3o4UTxXTrUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجاوز جنگنده‌های صهیونیستی به حریم هوایی لبنان
🔹
جنگنده‌های رژیم صهیونیستی صبح امروز با نقض حریم هوایی لبنان بر فراز جنوب این کشور به پرواز در آمدند و بالن‌های حرارتی در این مناطق پرتاب کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/679337" target="_blank">📅 09:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679336">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
صدها نفر مثل علی خامنه‌ای در این راه جان و آبرو خواهند داد
رهبر شهید در ۱۳۷۹/۰۴/۱۹:
🔹
مسئولیت رهبری حفظ نظام و انقلاب است... رهبری یک عنوان و یک شخصیت و یک حقیقت برگرفته از ایمان و محبت و عشق و عاطفه مردم و یک آبروست.
🔹
صدها نفر مثل علی خامنه‌ای در راه این حقیقت جان و آبرویشان را می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/679336" target="_blank">📅 09:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679334">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddzTFu3UCgZxjDpNvwiYA7cQ_HUWtsrsKyecGRA_pv98aAwue_e1Ko95zlAkLiaJKFGOVUKvAYhC2Nl81BBgvyn6apirwIjhBePpIYQUM26gyzYnXcW68EqpWlEz3wWFi9JwtQNs1kb3Wxj3ssIQSkWhZBVsNTzAy6jNYFXscm054mOYJSgKegSHvzfvKbKzGPlLGT5pquHaFeT2npLo09Mt8d0lsPHo8tq5gIyvsHGGNFgLck_tICsZ6rp8OVpNdIStDEUNmRM-w7hrsZCM9Dkk1-kpomRSfDm4QxahTKTdUNMepBwXooo5fOi-M8LX7aS5Lumewp_4ZPc5VSA15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگاری شغل سختی است چون باید طوری از مشکل بگویی که امید زنده‌تر شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/679334" target="_blank">📅 09:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679333">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2094e644c0.mp4?token=sTUFbyT-raVSp5s24JDdy935vQTSYui6VncsV6QahASInfsxHgpFBPbD4_f4cmxvO2HSiNE2Bw3sYYsTBoLyIGNEunz0vLZHE2gonS2wuI2hIqT3GEq_VF8WDIfGUZIZV6eimzj_E1hRF7fyVBdUCg8LaJ1jWwBxcoppwygUfXf4ptC_MbNsaVBXZyQ18RktuNrFqR9lzU0ClZPtL50_swK2sDiNL48qzrGMKQWqIDRuX532Y9gviH3PJN24tSMIC2VyOxtIZ-0r7nxuGlML8PA8rYPyIsQ-EHTAQkIlQYwweRDS5NxBNgnaatDXT6cq4A7bZE7w2KBae9cyCXsGkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2094e644c0.mp4?token=sTUFbyT-raVSp5s24JDdy935vQTSYui6VncsV6QahASInfsxHgpFBPbD4_f4cmxvO2HSiNE2Bw3sYYsTBoLyIGNEunz0vLZHE2gonS2wuI2hIqT3GEq_VF8WDIfGUZIZV6eimzj_E1hRF7fyVBdUCg8LaJ1jWwBxcoppwygUfXf4ptC_MbNsaVBXZyQ18RktuNrFqR9lzU0ClZPtL50_swK2sDiNL48qzrGMKQWqIDRuX532Y9gviH3PJN24tSMIC2VyOxtIZ-0r7nxuGlML8PA8rYPyIsQ-EHTAQkIlQYwweRDS5NxBNgnaatDXT6cq4A7bZE7w2KBae9cyCXsGkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب کتیبه‌های ایام عزاداری دههٔ آخر ماه صفر در حرم امام رضا(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/679333" target="_blank">📅 09:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679332">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس اطلاعات عربستان از نخست‌وزیر عراق برای سفر به ریاض دعوت کرد.
🔹
ارتش پاکستان از کشته شدن ۷ عضو تحریک طالبان پاکستان در درگیری با نیروهای امنیتی خبر داد.
🔹
نماینده جنبش جهاد اسلامی فلسطین در تهران: حماس با خلع سلاح موافقت نکرده است.
🔹
زلزله ۵.۶ ریشتری آلاسکا را لرزاند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/679332" target="_blank">📅 09:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679331">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
روزنامه ایندیپندنت
:
روحیه خدمه ناو هواپیمابر آبراهام لینکلن به دلیل کمبود برخی مواد غذایی و لوازم اولیه رو به کاهش است
🔹
کمبود مواد غذایی و اقلام ضروری در  ناو آبراهام لینکلن، روحیه خدمه را کاهش داده است.
🔹
برخی ملوانان از جیره غذایی محدود، کمبود صابون و خمیردندان، خرابی توالت‌ها، نبود آب گرم و از کار افتادن رختشویخانه خبر داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/679331" target="_blank">📅 09:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679328">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-MxoMYb_s6K4fRE8MRd3k8Fva3qO20jp3OvCEF_8csIX9-Ja6H40v5lBQ2887S0BTVkPuX7n8ofz3CF5I12aEdmdzRSBn_sKYoB85yeQdfIsR3rX9ghUUMqFrrvo_LvjlBBnvBAtx6LRpBFTHjkWj70paJTQ9TKfFWo7pRQU2wIgPhiQ3L6X3fX_b4zyz0BE1ZZbSV6BickhwW8Z4MuZYiVIYONkUYaYimnmT_k-le2r4P5b2Dn5FYOXwzMNqza-6D4BQ1jN8heHw1suCNbAZTRRFu25awxI68bmEGZlIFfUaqUaUH1myZuQrXDdy-1PrTCRQjB29hxFeMgE6k_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس برای نخستین بار وارد کانال ۵.۵ میلیون واحد شد
🔹
شاخص کل بورس تهران بار دیگر رکوردشکنی کرد و در نخستین دقایق فعالیت بازار سهام ۱۲۳ هزار واحد رشد کرد و به تراز ۵ میلیون و ۵۳۱ هزار واحد دست یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/679328" target="_blank">📅 09:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679327">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peHYY5ioPMPUl0t-WbnRqtUn4DBvYhH0-aG0gJ8nXawQcJbfcaCucSqkxTnFcAxFy187839c_n6ktBz8WQe1eFovd6iVnfzKgrAbJ6GhATI-pmJTf9Og6QJijssYLqf7lN1_eQRPtlePp9kjbAiUzt3JRry1BWNcGZUmSps-AiqXt15whzTEgKWbevsXnhKAL1xftTY5-rz2LKWQdCdBhvcNiPerPr8HFnXG8OmJTAtf0JxEWtbum6ImhtUthcPBAo0bqzxS_wA2jpZt7Y9fBndCk_trpW8g-ZYCZfCY-4bSyjBuSaBOAAFiq13ZlSAYUDEwrX7CbZQCrmsACKdQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کامیون با راننده ۸ ساله در محور شاهین شهر کاشان توقیف شد./مهر
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/679327" target="_blank">📅 09:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679325">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
لری جانسون، تحلیلگر سابق سیا: ایالات متحده به دنبال تضمین این است که کشورهای منطقه هیچ اتحادی با ایران ایجاد نکنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/679325" target="_blank">📅 08:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679324">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
غرق‌شدگی؛ شبح مرگ در دل تابستان
پزشکی قانونی کشور:
🔹
سال گذشته ۸۸۸ نفر شامل ۷۸۴ مرد و ۱۴۰ زن بر اثر غرق شدگی جان خود را از دست دادند.
🔹
بر اساس این آمار ۱۲۳ نفر در استان خوزستان، ۸۳ نفر در استان فارس و ۷۴ نفر نیز در مازندران غرق شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/679324" target="_blank">📅 08:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679323">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrYUOX-PdOsGEvYXZsXvA-WyosXsOXiBnF3f_0lrdXhfv857wH5o9wjMi6Wuyj7GXXhoVJ9ZQ2zLvYuEuRYQXR6Qk8MHf8wlt5LoX8F16_DWddcS8FH_bnWDDlNh22GMfgdBVk9bCYqwgrqHSG3yYz5cCNn_PT2TTJnJdIe2LNEcgPTz3oFq9q7BhEK0TsKTsB-AMY7-E-43Fx6vnYhPxNV6fq07b9lTb0we9VDAMrsrgl1unLb6UMU7OuJ42nEkkvPPR0KXEbHj2r1R2fExjbg9fkrChMgZvliYO6_jb9UTlvlLEBiQ_Ai4SpSR4MKg2waaaHtmDTKJjCXPcjeoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضائیه: خبرنگار متعهد، هم‌سنگر رزمندگان پشت لانچر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/679323" target="_blank">📅 08:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679322">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رویترز: فروش بیش از پنج هزار موشک پاتریوت به چند کشور عربی
🔹
وزارت خارجه آمریکا با تایید فروش پنج هزار و ۲۵۰ فروند موشک رهگیر سامانه‌های پاتریوت به چند کشور عربی اعلام کرد قرار است این موشک‌ها به بحرین، کویت، قطر و امارات متحده عربی فروخته شود تا دوباره ذخایر موشکی خود را تکمیل کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/679322" target="_blank">📅 08:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679321">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
پیش‌فروش ساختمان فقط با سند رسمی معتبر امکان‌پذیر است
دادگستری اصفهان:
🔹
مهم‌ترین نکته این است که مردم بدانند قرارداد پیش‌فروش ساختمان باید حتماً به‌صورت رسمی تنظیم شود و خریداران نباید به قراردادهای عادی اکتفا کنند.
🔹
پیش از معامله، حتماً مدارک و صلاحیت قانونی پیش‌فروشنده بررسی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/679321" target="_blank">📅 08:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679320">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c7c72b59.mp4?token=h89ImvuTn6Y0kqZJ4Dj-1mBKGxI0K5-siTA2iURopuixqyAY0D8_ZmY4FqqVoOMUclP_cLHdLob2x4eu8dHJegeVxH8HTUFxR3O0Pwrpd5xb8ZncbwPkJ5W0yHWjYugnJhkWOVleVPgRLPYdS2hWpGLPIN5WO9hf6sIEgOv0ZCSiaEXJn3rXrh0LbQJcJ578RtlDbyTNgECHMt3FnZuPbvR6YAYszYks3YZ3qrnNmaDOFvyXYFU7lQptxMY2FtIhHNeOkAHBdG_pLzUblq00njuuAEtHVaCCKaaQMfM00u7BR3rq8zjFr4Keiv1ESJiq60I_cXNrm5SL6lMXX1phbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c7c72b59.mp4?token=h89ImvuTn6Y0kqZJ4Dj-1mBKGxI0K5-siTA2iURopuixqyAY0D8_ZmY4FqqVoOMUclP_cLHdLob2x4eu8dHJegeVxH8HTUFxR3O0Pwrpd5xb8ZncbwPkJ5W0yHWjYugnJhkWOVleVPgRLPYdS2hWpGLPIN5WO9hf6sIEgOv0ZCSiaEXJn3rXrh0LbQJcJ578RtlDbyTNgECHMt3FnZuPbvR6YAYszYks3YZ3qrnNmaDOFvyXYFU7lQptxMY2FtIhHNeOkAHBdG_pLzUblq00njuuAEtHVaCCKaaQMfM00u7BR3rq8zjFr4Keiv1ESJiq60I_cXNrm5SL6lMXX1phbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سانسورچی‌ها ناتوان از پنهان‌کردن ضربات کوبندهٔ ایران بر ارتش آمریکا
🔹
وقتی قدرت نظامی ایران و ضربات کوبندهٔ رزمندگان جان‌برکف ارتش و سپاه بر پیکرهٔ ارتش آمریکا آنقدر خسارت‌بار است که با وجود سانسورهای گسترده هم نمی‌شود پنهانش کرد. ‌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679320" target="_blank">📅 08:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679319">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54ace74ac9.mp4?token=ZfYGih6-ZR3kHpcTbohNRL5vZUpyqdy2yMxctq4lGMWHdsPdNxUOy1EYRQ1KmHgGEFTT6JmeyJ9gAwY5nyqdA5FbGAt8QayIR7S1J7QDbv2L97B6zk3LLhCD5Le35d-TMoGBze4j1yle-gaekyGYLtDRP9NRP7_rAYtU9ZfEvuV-uuTQILL6UsjYfmsw-LqGa_Z3YA7bwD08u0sD2vVzgMyQi1G5IgQKjF40_du9LbYp1u9iZoKh8h1ApAP6WMnl2lVRR29jk8_TUuKjdlYAvul7oQXtPpL8MQvL2qRTjcwKUXqm-QgvNW89F3Vf76k_dkoeMBsc0K0kAeM7FMt_syOb60562_BY_ifTH_MeHHlM0_A35q4Fc7Qltk8hb9JEfj5pDE6tW1AryA598nvkNKimXfn6UbeBOjUtxnJrZ3nZtyOiVq90YrNnXctsHByWMDy1dI1IOXYhbDTV3nHN7WguCIrYx7w_qD4oMeijdxtlkaq3LCAtprGK7G73xBbgaXz2fJTuTw-Bm1YrG8zAzRjQlp0PuidIvZAU6Z0dxTpqkTuqfkRgf7SLxusYCi-TN3_gEvUUK9lnPFJ8l3RPNZzUPHB_2D2Y52BvHwU9GBr_zc5LhXVkiASPm7SbU2-dv_p6_uXlYysBp_kvh0IovPat0uCSLa0IkdMI1j06_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54ace74ac9.mp4?token=ZfYGih6-ZR3kHpcTbohNRL5vZUpyqdy2yMxctq4lGMWHdsPdNxUOy1EYRQ1KmHgGEFTT6JmeyJ9gAwY5nyqdA5FbGAt8QayIR7S1J7QDbv2L97B6zk3LLhCD5Le35d-TMoGBze4j1yle-gaekyGYLtDRP9NRP7_rAYtU9ZfEvuV-uuTQILL6UsjYfmsw-LqGa_Z3YA7bwD08u0sD2vVzgMyQi1G5IgQKjF40_du9LbYp1u9iZoKh8h1ApAP6WMnl2lVRR29jk8_TUuKjdlYAvul7oQXtPpL8MQvL2qRTjcwKUXqm-QgvNW89F3Vf76k_dkoeMBsc0K0kAeM7FMt_syOb60562_BY_ifTH_MeHHlM0_A35q4Fc7Qltk8hb9JEfj5pDE6tW1AryA598nvkNKimXfn6UbeBOjUtxnJrZ3nZtyOiVq90YrNnXctsHByWMDy1dI1IOXYhbDTV3nHN7WguCIrYx7w_qD4oMeijdxtlkaq3LCAtprGK7G73xBbgaXz2fJTuTw-Bm1YrG8zAzRjQlp0PuidIvZAU6Z0dxTpqkTuqfkRgf7SLxusYCi-TN3_gEvUUK9lnPFJ8l3RPNZzUPHB_2D2Y52BvHwU9GBr_zc5LhXVkiASPm7SbU2-dv_p6_uXlYysBp_kvh0IovPat0uCSLa0IkdMI1j06_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام رزمندگان نیروی زمینی سپاه مستقر در جزایر خلیج‌فارس به مردم همیشه در صحنه ایران اسلامی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/679319" target="_blank">📅 08:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679318">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSKAcR5WVc0_z4DQSpY3YmpbT36h3lcR0KlANR_C_tBVNkhRZCNUyFhSA4e5KyHejWN_YLn7-_I35AhLAbI-JQox4grHmsTPfQ4SsN0RT_OJeN-HAA7MkQbywmlkN0KDDzHhsBk-UmY7fqzXzcJedDSHNCFoidrDD-Ootdfp5bUE9wWb_pMij3uNES3YfgagU9z9o6LXii5cA6UbRQIhFHYZ1YSxZWaQc4n4mMRI-mosM7VPx4nqrtcjMeEhA7_C6ELIU1Si96XrUa4CKgsJO0NvLDjsqaR75rpFprpaP4_In4ekUmbZwCGYVzICPSXmUrnDfnSOPZXwrYkErEzLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پانتا: جنگ با ایران، آمریکا را در برابر چین آسیب‌پذیر کرد
رئیس اسبق سیا هشدار داد:
🔹
تمرکز واشنگتن بر جنگ با ایران، موقعیت آمریکا در برابر چین، روسیه و کره شمالی را تضعیف کرده و باعث ایجاد تصور «ضعف آمریکا» در میان رقبا شده است.
🔹
چین، اکنون تصمیمات خود را بر اساس تصویری که از عملکرد آمریکا در جنگ ایران دارد، تنظیم می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/679318" target="_blank">📅 08:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679317">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای ای‌بی‌سی به نقل از مقامات آمریکایی: توافق ایران و عمان ۶۰ روزه خواهد بود و در این مدت برای توافق بلندمدت، گشایش کامل تنگه هرمز و ادامه مذاکرات هسته‌ای تلاش می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/679317" target="_blank">📅 08:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679316">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وزارت دفاع: ایران در میدان دفاع مقتدر خواهد ماند
وزارت دفاع و پشتیبانی نیروهای مسلح به مناسبت روز خبرنگار:
🔹
در شرایط جنگ ترکیبی و عملیات روانی دشمن، روایت صادقانه حقیقت، مطالبه‌گری مسئولانه و صیانت از افکار عمومی، بخشی از قدرت ملی و بازدارندگی جمهوری اسلامی ایران است.
🔹
خبرنگاران، یاوران و همراهان راهبردی در شکل‌گیری گفتمان دفاع همه‌جانبه و انقلاب صنعتی دفاعی جمهوری اسلامی ایران هستند.
🔹
جمهوری اسلامی ایران، در میدان دفاع، در میدان روایت و در میدان اراده، همچنان مقتدر، هوشمند و آماده خواهد ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/679316" target="_blank">📅 08:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679315">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hae-XBiSn7v9jv3-8914AvBcYCNVi5S5M8qhOoQDLSZWwd7QX94CQ_cFXCq9M3LRpMU8F8l7Fx0UVfus8074IFKxmJRT9S7PPt_ksG_cVeBBULNnbkwktrD4rYY_a0wR8ygHfoEt4SIBeKBN7kz13sulYLzP3t0o4oBhK4JM6YoyM7Y6UvSL8_NOwhtGRi1znJ0ZixWRXLnh2gTk4e4ehmdXkrbRCVH3diK57JlrdkDb27umPv8CDBTS8Jzor2r5vm3Y8ahCpTo9kfyz-SIW7SAmBjmAba8D7iKo5I4zlnf-lqVStQmZnsL9Y2uBGinj14xCIXsCpJKegpjqS-Y21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیلاری کلینتون: دکوراسیون پرزرق‌ و برق ترامپ تداعی‌کننده کاخ‌های صدام است
وزیر امور خارجه اسبق آمریکا:
🔹
این برای من غم‌انگیز است، غم‌انگیز است که (ترامپ) اینقدر مبتذل و پرزرق‌وبرق شده است و این بازتابی است از شخصیت خودشیفته و نیاز او به احساس مهم بودن، از جمله چسباندن تزیینات طلایی به تمام دیوارهای دفتر بیضی‌شکل است.
🔹
کلینتون خطاب به مردم آمریکا گفت: اینجا خانه او نیست. این خانه شماست و او دارد آن را نابود می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/679315" target="_blank">📅 08:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679314">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KL7lHNEaH0BnjbPjlU34xWOV6Pq-8ULzvxGMB1cC9TJRuTyn8X5Cw5ftHRBDiKCGP2U5UeNfVwX22vAAHTkdMc1fFQ5ZQ4rhDnqGrlmNJ10zEL395Yl22XXSZsvfUD3p-d-RgQ_0TrBf5Ih19l9H258ZY5ZeA9-KyZM0wIRwpseitJGZ4hYW4O425lGb0raC6bOhOVK2CIlzP19hPzgWZfI7p_WiTcdgYKIchq1WHkTnaecogkhWnG5bBLTo-A9a-ghYwX-CfFRP8AbJH528LyZJ373y0AQhfv_Zi5wq4WGxaviVmhobnZJvNeal5iezCCyiFE5MdFJ6hkBSgnhdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های عبری: مهاجرت ثروتمندان صهیونیست طی سال‌های ۲۰۱۹ تا ۲۰۲۴ دو برابر شده و سالانه ۷۰۰ میلیون شِکِل از درآمدهای خزانه رژیم صهیونیستی می‌کاهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/679314" target="_blank">📅 08:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679313">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سیلاب‌ سنگین در خیابان‌های گورگائون در شهر بمبئی در هند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/679313" target="_blank">📅 08:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679312">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syWCMNj5kRuPycTDyjtWb6kXVQgFpEYYUoA1-Fsyvu-9BYMxPNM-pfhNdRA6YLOgmf3jkoJq06moAfCof1GcZRvDO2bi5G0Hm_yv8nAY1n_lgECMfM9XLTnsUQUA6-ysvkazCJshzIp6v3ZUerbcMLCEsMQ0t6N6izCFnih6YCzA_X3g1XhVCm5fu26FfsxYI0JHNzylKTQP7NOT-YNclT6AibZm024m1oL_buyxUIeTyew5sVEmzEgCjn4ghlc2V2ZzOAdHd4m8eagGBa-Wl9d6bAujmW0jRdBbFg38nWQ2X-mu0TNr98rdO6pITWvcU5-okPL2y9zkt9SnPahj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقتصاددان آمریکایی: ترامپ هیچ نقشی در مذاکرات جاری میان ایران و عمان درباره تنگه هرمز ندارد
🔹
استیو هانکه، استاد برجسته اقتصاد کاربردی دانشگاه جانز هاپکینز، با زیر سوال بردن اظهارات اخیر دونالد ترامپ پیرامون بازگشایی تنگه هرمز، این وعده‌ها را فاقد هرگونه واقعیت میدانی دانست.
🔹
ترامپ مدعی شده بود توافق بازگشایی تنگه هرمز طی روزهای چهارشنبه یا پنجشنبه محقق می‌شود؛ اظهاراتی که هیچ‌گونه مبنای دیپلماتیک یا واقعیت اجرایی ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/679312" target="_blank">📅 08:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679311">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac9b82c54.mp4?token=bAZa0s1bttd_UgF9O0xKhpTfaml8BOhwW0GzBVH3nKkkT9P-8xmndw2RoETnc63TuWsLd1ezCKZDB0YdcWDVb6YrDFcM7VLmzFaGgZglGDx1_pSh-h89uVE0e3jYibaLhg4eAG2BVEloxcPv-7K-l5TxzTdmltKwVZ0uDsJ2VWakTiMkzmQ4xCjnoTXcimDOWCOLsHa7OF-ahuygi4MoCrtk41KwW43hJWQdo9Qu5nfPlUANErMxBYU6iAlySnQzkHYM5ghFjPcrVFf8jftPWfeWtEskWR93GrZza8w3KemdjeLmT5skhDhUMyxzuZvztsdqkTEHo5be3DI-v_jiOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac9b82c54.mp4?token=bAZa0s1bttd_UgF9O0xKhpTfaml8BOhwW0GzBVH3nKkkT9P-8xmndw2RoETnc63TuWsLd1ezCKZDB0YdcWDVb6YrDFcM7VLmzFaGgZglGDx1_pSh-h89uVE0e3jYibaLhg4eAG2BVEloxcPv-7K-l5TxzTdmltKwVZ0uDsJ2VWakTiMkzmQ4xCjnoTXcimDOWCOLsHa7OF-ahuygi4MoCrtk41KwW43hJWQdo9Qu5nfPlUANErMxBYU6iAlySnQzkHYM5ghFjPcrVFf8jftPWfeWtEskWR93GrZza8w3KemdjeLmT5skhDhUMyxzuZvztsdqkTEHo5be3DI-v_jiOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تمرین فیزیوتراپی مفید که به رفع و اصلاح قوز پشتی کمر شما کمک میکنه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/679311" target="_blank">📅 08:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679309">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
یمن نفت عربستان را زمین زد
کپلر:
🔹
پس از اعلام محاصره باب‌المندب، صادرات نفت عربستان از بیش از ۴ میلیون بشکه در روز به کمتر از یک میلیون بشکه کاهش یافته است.
🔹
بارگیری نفت از ینبع نیز متوقف شده و صادرات به آمریکا برای نخستین‌بار در ۴۰ سال گذشته به صفر رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/679309" target="_blank">📅 07:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679307">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaV98-ZOofz-WJtKUMaIkmAzN4NrSE6DMjLqgDQf1P86piDFk-c1ZyltFvfOjHF-uQuSTRqRW9cRuYv-p4jpMP5ava-MxZlCPFnyNImG6J2-4F8Me4r2TYp5A_JAjIPQVcTSnKxOPIaEuEbYgACB_M-NTE_4kStSrqwdVvx7iTeYV22Txhp0PCWvmP9XsFrIJWnodkoz_ROXwJVm_hiSIQ9QY3eMF2UyPcypOo-thcSHPSkFpHImIxywIC9aVNYArc5BLmYdN0t4LII5TixL_sul4kpKtJw6DOXL2SRLCaD9a6zAKqtK_wJobRBmlLMfeKDRXVcFOZI9bdJJAL7tVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ایرج» دوباره در بیمارستان بستری شد
🔹
«ایرج»، خواننده پیشکسوت موسیقی ایران، که چندی پیش پس از بستری شدن در بیمارستان، تحت مراقبت‌های ویژه در منزل قرار گرفته بود، بار دیگر در بیمارستان بستری شد./ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/679307" target="_blank">📅 07:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZZbk6kjnZJn8SvTxpceIMH_PIW9LWgcG-TZDTalojZj6sqQa1Qdq2PBhz5KcV0RQjyl6YXacvoMy8RyJJzZuwLR-jt5Lo3C-cxXaYzjbvI29-byF8S7C2YB1AHC3MwBl6JLwSQeOBmDGlEJxVI4kLHmIs7IhY50SfuwU65pWQnbwQOkbYfAJNZ0N4bQv4UnT6J3uQNZsCTvxXtWO6m1vFB8M4yx3vc_m2nlqrRdBFNyIlJ9dAz9FGk9nOkSrKxUHygNHhBXTzYAYhRRYb-UgCy2ejX1AG9MpUW8zL9SR9O_N9CunCbOdltydLmbZZ88chQdrG8M2cmJyuGk43DA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۷ مرداد ماه
۲۴ صفر ‌۱۴۴۸
۸ آگوست ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/679300" target="_blank">📅 07:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679299">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromربات هوشمند اطلس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbMJ3d0IrpmIh8_6EE59HQOSw1shAQVHAZJWWnLZ9i35OPysPdbOxPyqTnI8-U5R6r-ETocndkrwRqJCEg_9zDuf4sI7YaJq2gNBD-6u2pnV_3NNM5vVyCygxYZG2Egt7kw8knE9_1Fw84R_yJmK7EzqnT24aCN0tp9sIrIzLAnh0LyDfCijar_SDqJlyC-buJLTtxwKGUwtNLTrGIPVkNs6NgUvlDARrcuhvysLa0piGqGCbW6bcRtW_4b9V_Vxz4CfNndZTECvU-iVSV150Kbf5FyKO0LTk2c7qQGpwW53r8Gh2Fhx5JnHhtpmloYX9-ilDVv-RmqUB6iZsfFN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/679299" target="_blank">📅 01:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679298">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ژنرال‌های ترامپ به دنبال «راه خروج» از جنگ
🔹
شبکه سی‌ان‌ان در گزارشی فاش کرد که یکی از فرماندهان ارشد نظامی در حلقه نزدیکان ترامپ، به‌شدت در حال بررسی گزینه‌ها برای پایان دادن به جنگ علیه ایران است.
🔹
طبق این گزارش، گزینه‌های نظامی آمریکا برای پیشبرد جنگ عملاً محدود شده و مقامات پنتاگون را با چالشی استراتژیک مواجه کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/679298" target="_blank">📅 01:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679297">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
برکناری شوکه‌کننده فرمانده لشکر پنجم ارتش آمریکا در اروپا
🔹
شبکه خبری ای‌بی‌سی از برکناری ناگهانی و غیرمنتظره ژنرال «چارلز کوستانزا»، فرمانده لشکر پنجم پیاده‌نظام ارتش آمریکا در اروپا، پیش از موعد مقرر خبر داد.
🔹
این ژنرال ارشد در حالی از سمت خود کنار گذاشته شده که حدود دو ماه تا پایان رسمی دوره مسئولیتش باقی مانده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/679297" target="_blank">📅 00:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای حکومت جولانی: یک عملیات تروریستی را در منطقه «سیده زینب(س)» خنثی کردیم
🔹
طبق اعلام وزارت کشور حکومت جولانی، نیروهای امنیتی با دو تن از اعضای گروه تروریستی داعش که قصد کارگذاری بمب داشتند، درگیر شده و هر دو نفر را به هلاکت رساندند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/akhbarefori/679296" target="_blank">📅 00:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjJafNuoBjePNwrYMsaSK66tvj59nKuRfeB2WEFufWN1ZOIAYNIQnBcda09PY0KcYqUIXuQekfN65VoGLYna_estqlZLURwc3tFY8AK5OU5htoXj-FGIWFf3yuiNp7bQn1qiC1YQjWhRPD2_gBB1xDsou_mMKYEJNnyGb6hWPbSPo-bNqAHcQjLxwmbMhYz1gDckIfLsmWK3yT2ES4VNwk3nXFe95OnjoCFY8KptfWWh6pxJLMxwfFb7s6_o_6gXdZlykl06e9g8pTzOV9yh3_IDS1hCj2TSSf_sv-icAHQfGGM6sqNMTgq8F5JF0Wx-STEedwoU7Dy7zPqtdkjH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک زن هندی پس از سال‌ها کوتاه نکردن موهایش، با موهایی به طول ۲.۷۱ متر نام خود را در رکوردهای گینس ثبت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/679295" target="_blank">📅 00:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679293">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA1JWeZ1RXuH3qgN_m71hOE-EuCOm9m5aOocKqtg9qnSuEgAQq05YRZoEi-PiPBEDROb0EALuTLedzY7AOqfMKuW7YaRX_cnxpilS_J9dxVTByGpV0LU8rr1jlDaP3HBZe_luxj4loy8pNMtUBxtqrPvrwNATwn4uxzbB7V35PJVqj0vyqltmtofpNxPUYwSWso70mhE0H3ja5lJGKE2sklgFdGe78ydfZv7-U_qkF6FtnSTLwKgvRBZoHeiGQlUQdIlf4lz6-ZQSjL9lvj5Ri67KK1Sk5VRyJylng5g_KnA0eKQ9w0tIzkOKx15r6Q910SlcJyOhzpwnS7_0ph6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/679293" target="_blank">📅 00:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bb8067c5.mp4?token=X3mh7xduqLXAm0mbG5hn7PGg2Ys1FUUURZvNtzfMyyEjs46X5jXY3o6Pf3qjLuFM5ZC6WPT_Fxc9ZxfWocxeiHepHLJ8Q7eolwhzBzIDVWZekYGfhE2c_IE9pwLPCIldh55c58q8zTl_6LIhEmyEbm9Sd_jaXAwDRAMPPaTuNzfQTDzuKM2PnNjzR9OEexBL8G4rZ-Ww95oI9dv1mjozS0S4Ld23S98Z9zchr3W0vOXxf7C4pfd5M9r0TGThGo8fgX7vLTVHWL5QYohDghE8qcbPzTCX8dw_dJf1cXEng3T3tCu0ghQouLtE4mKP_rp2sGxwl5XHcze7izjnYysiRr4atY9ddICHv0wwEZrTV8eGwP8p2Qww2smVenodffaMEf_ZCCtCn8L02jasmHOPuxxtTu8i_zGMIW2PnGZ1BVHGOfFaCQE-9mpjYaZ7hai8AbcFZn06sBn4M98BzA76_NJ8qyanLt0q5cWsA4aRLMc1Dg-HGWH_dgg20DJ2J3s42CcOqFa2PruoQGd2RlhfXk-s-irrnA4TdQGOxcLpZJVwmqB7F083AMnYrlynQJyM4vBAoz1bKPxtnxLUOwpptVa9EP5-rCm3Olo40ss669Wa4wf0-4hOi06efEwNdxkXy4EbS7FWkMg8H9BJJXjggpiNP5YnHE8xhEBmzhTnW4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bb8067c5.mp4?token=X3mh7xduqLXAm0mbG5hn7PGg2Ys1FUUURZvNtzfMyyEjs46X5jXY3o6Pf3qjLuFM5ZC6WPT_Fxc9ZxfWocxeiHepHLJ8Q7eolwhzBzIDVWZekYGfhE2c_IE9pwLPCIldh55c58q8zTl_6LIhEmyEbm9Sd_jaXAwDRAMPPaTuNzfQTDzuKM2PnNjzR9OEexBL8G4rZ-Ww95oI9dv1mjozS0S4Ld23S98Z9zchr3W0vOXxf7C4pfd5M9r0TGThGo8fgX7vLTVHWL5QYohDghE8qcbPzTCX8dw_dJf1cXEng3T3tCu0ghQouLtE4mKP_rp2sGxwl5XHcze7izjnYysiRr4atY9ddICHv0wwEZrTV8eGwP8p2Qww2smVenodffaMEf_ZCCtCn8L02jasmHOPuxxtTu8i_zGMIW2PnGZ1BVHGOfFaCQE-9mpjYaZ7hai8AbcFZn06sBn4M98BzA76_NJ8qyanLt0q5cWsA4aRLMc1Dg-HGWH_dgg20DJ2J3s42CcOqFa2PruoQGd2RlhfXk-s-irrnA4TdQGOxcLpZJVwmqB7F083AMnYrlynQJyM4vBAoz1bKPxtnxLUOwpptVa9EP5-rCm3Olo40ss669Wa4wf0-4hOi06efEwNdxkXy4EbS7FWkMg8H9BJJXjggpiNP5YnHE8xhEBmzhTnW4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آذربایجان غربی؛ سرزمین تاریخ، فرهنگ و تنوع
🔹
از موقعیت جغرافیایی و مرزها تا زبان‌ها، اقوام، شهرها و طبیعت منحصربه‌فردش؛ در این ویدیو چند نکته جالب درباره این استان رو با هم مرور می‌کنیم.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/679292" target="_blank">📅 23:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVhvCRer1Pv2vts4KZKy1chiXcRM98nojMnzNgQK3RPB88Qwy_caKBUN9aIz5RAWQw_PFfTpU6dK6WIvW0bFgubdwx29Cqa_CA0GKU7mRNH4ZPSLc13SRjnEYDLYUniqxGOsR26mAanhz4GKZtkkJl5gsZjuyZDrAUFOMTHAgCV9hrrRPap2UUUBGSsnw6AlOSLMkkW_E_fJITyQmR-r1YfLH48LpSyzROAJ6pCgBJDgUF82AdK1AKP9YgSn_VdlbneJKIu6JAbJQj8IDnMYM8tKyA3HQiG8lS-EB42AXtMQkVan1pI7JLXTFYjmruXujrURLv3qlpOYdUm8LEmYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخورد ۴ تن آهن آمریکایی به ماه
🔹
یک قطعه ۴ تنی از موشک اسپیس ایکس به طور غیر عمد به ماه برخورد کرد. به ادعای کارشناسان این اتفاق هیچ خطری برای زمین نداشته اما انتظار می‌رود یک دهانه آتشفشانی در ماه به جا بگذارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/679290" target="_blank">📅 23:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای سی‌ان‌ان: پهپاد که در فرودگاه آلمان کشف شد، متعلق به سرویس‌های اطلاعاتی روسیه است
🔹
مدیر سابق مرکز مبارزه با تروریسم: ادعای ساختن سلاح هسته‌ای توسط ایران بهانه‌ای تبلیغاتی بود
🔹
ارتش رژیم تروریستی صهیونیستی بار دیگر به خاک سوریه حمله کرد
🔹
زیردریایی اتمی «یواس‌اس سن‌خوان» آمریکا  پس از ۳۸ سال خدمت فعال بازنشسته شد
🔹
سازمان ملل: منتظر نتایج مذاکرات درباره تنگه هرمز هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/679289" target="_blank">📅 23:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVnW9FtOf6qUE-lp9Qp3Yjyfs3jEAncA3-Tqw3o_2B7lAQ8izwbs2Nx9LxJ8Y8wBcf9kdTD29zimkcztBbAyMV59KCPSc9mOcp0oKqMyOp1TZ3Is7ZPnnCdKmXrR0SJV0s23dACsn5d6PhofnJXxBtTjMNpoqCfBHa6HNite1UF-54zrvQb0hGZPKZDgrzZley0K6KobwqUdGqTSEYk9p7_0ZQ96DwZD7WJNUbjsFRwBdLtkCTn7JFebl5D2wv455SFIIfwxKBKrwpUFvJXJMsw6ttw6R1p32kguWGVc5kcEcz5E6uhe2-8p9bSn9KJqktM3BrHpH5e-56QN7i8lZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای فوری لکه‌بری؛ هر لکه با یک روش ساده پاک میشه
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/679288" target="_blank">📅 23:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d3a7d45a.mp4?token=XvE7ZQ3KN1L3VnZgmTmHcP4qshALiHocUcZGTVl56uYPDjMssst4zZC9BUDsFuUt9tc-Y3AGVeZ-Ybe18zxgyYJ-1sNjob8zUHB3iWjeMcLzI-euIvue5LszXl2AlDY4bRDnCLQestQr1f2tS5zDovq8DRlB-qscpS651-nybwHdD0CM_Nb30lIkQyhViqdQVsx0ApZ7jt4mAL5TA3s8GLRFQTWGLpgjd05yMp1j-cRwyK0_XZd170CMns4X8KBFzZaT0sRsTe0_AzCcIXc1eci437imY_Su7pJqAkqmtsZZnqlYkcPvCL-IySthSeA8oxJxQ6XPLRy4_0546mUn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d3a7d45a.mp4?token=XvE7ZQ3KN1L3VnZgmTmHcP4qshALiHocUcZGTVl56uYPDjMssst4zZC9BUDsFuUt9tc-Y3AGVeZ-Ybe18zxgyYJ-1sNjob8zUHB3iWjeMcLzI-euIvue5LszXl2AlDY4bRDnCLQestQr1f2tS5zDovq8DRlB-qscpS651-nybwHdD0CM_Nb30lIkQyhViqdQVsx0ApZ7jt4mAL5TA3s8GLRFQTWGLpgjd05yMp1j-cRwyK0_XZd170CMns4X8KBFzZaT0sRsTe0_AzCcIXc1eci437imY_Su7pJqAkqmtsZZnqlYkcPvCL-IySthSeA8oxJxQ6XPLRy4_0546mUn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به حاشیه درخت‌کاری‌اش در پاکستان/ من بلد نیستم فیلم بازی کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/679286" target="_blank">📅 23:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679285">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7910a5b25a.mp4?token=BZjaJTTjZPGfIaeMqgCTGEo0dygRkZ1kLM5VihNgus-CSxyZJ_wqA0ib1HpDV6aFft-00XyMUI_h0Pjcw7QTQI8PUPVJyNBLcMe3HutcakzO2rUiHWiUhjIIiyMnZHWzi89TqOldlohRj5A1WblZtY30Y1aHcpkYexlFecLjB5xv2QSUgoweEBIdtcNbB0gBi7o8r7HEvdkZxRgKAIoRgiMQFGZzXV0EejQRH1a4ZxG2ica4ueYQs3GSM9PWpPLNPRETIul6boBlfTCc4T3wmlF6lyipVZLV_8yAUNuzm5VuJcei0qWshU6gDvbQzVcGuQyRJ4FgZyi0sJgTfU_eHLIeWipcDUqk3aOXTUl6bMH_gqboRn-cTamSXTFElEsFMqQySv_VsRo0Xl7-1seP9i1DsBiBMOnXsuSg02jNXiqWZc1jL9sqiSvquEHm3_vxuAIam1wHEkPdzTBfTkmHbrADWoW29wsKkR8i7siY4Y-aT5piafkbwrDd7vyb1Yexyfy01ossjjKvqPE1ufQR59ju7Z_IdUV1cj0Ygujz4pW0gU1E1juOiO0RpmRodLTCie6m1j1E5svfq1jlMFft0OzEBMuYyX1zKL21I9EvsrLfuKnIFs_E7bSjJD12qNhKwQxYrCKYnAAWZu6P42oeHbqh9mPv0bPV0wYzFUnWSPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7910a5b25a.mp4?token=BZjaJTTjZPGfIaeMqgCTGEo0dygRkZ1kLM5VihNgus-CSxyZJ_wqA0ib1HpDV6aFft-00XyMUI_h0Pjcw7QTQI8PUPVJyNBLcMe3HutcakzO2rUiHWiUhjIIiyMnZHWzi89TqOldlohRj5A1WblZtY30Y1aHcpkYexlFecLjB5xv2QSUgoweEBIdtcNbB0gBi7o8r7HEvdkZxRgKAIoRgiMQFGZzXV0EejQRH1a4ZxG2ica4ueYQs3GSM9PWpPLNPRETIul6boBlfTCc4T3wmlF6lyipVZLV_8yAUNuzm5VuJcei0qWshU6gDvbQzVcGuQyRJ4FgZyi0sJgTfU_eHLIeWipcDUqk3aOXTUl6bMH_gqboRn-cTamSXTFElEsFMqQySv_VsRo0Xl7-1seP9i1DsBiBMOnXsuSg02jNXiqWZc1jL9sqiSvquEHm3_vxuAIam1wHEkPdzTBfTkmHbrADWoW29wsKkR8i7siY4Y-aT5piafkbwrDd7vyb1Yexyfy01ossjjKvqPE1ufQR59ju7Z_IdUV1cj0Ygujz4pW0gU1E1juOiO0RpmRodLTCie6m1j1E5svfq1jlMFft0OzEBMuYyX1zKL21I9EvsrLfuKnIFs_E7bSjJD12qNhKwQxYrCKYnAAWZu6P42oeHbqh9mPv0bPV0wYzFUnWSPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای بازگشت یک زائر گم‌ شده در سفر اربعین به ایران در برنامه پرچمدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/679285" target="_blank">📅 23:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyNiTMuJMIXGtV-8-OkuaNMbA-79ENh0jEa3pQPaXFv2EnVhSbav8yI98kx0TCC01jNNxJ13VtzT_S6ao3Xq0UXXCIcbaaSG8Um1017opFNzY6A-3W0e4JccG63DkR7G8nFPnegufwsXcAS53Nq2IvK20un--GL_kMSMuwFdsRlKSQrtT_Jf2lTYtsHYCSJB-1XBUnjiFL8ZGgeY_TFgEuJtIv9J9sMyp0Ybi6AJ4oJSArNXanIG569N5EUFSJvKQvBRkZfU-bMaYP1uVhwRpxHPHDiVQwUaqLhMTVbZhb2BJya5zlGMON19L9xC0kDdO1wSQAqRP6c5V_y36Hlh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCwsDn-E8N3DXh6bfTTwpr5rXMNaIP-eCBEYGbfWA6bqymCstUsGfsQQ_KyABsMxuj5wkZhS5RlpZD7VQbEfTSl0G5I1NNEysXDjfqGrwLUW74ca_6zEjpxJhOKucm4pBEPe3bs-Ouk-hw87YNUTwCUmtaYvCTZDCME36guGdjlqtGNVJDDKW9jSNfc5cODpGLpUNgQt-wrJJeDXgrBOj2xiggirKa_wnCqR9fbR19wAHhLfDm2h4HrToWWpR3XafwylIHKaFSAoqwpv_S3OY39965FPbkwsZ8BIIiy9NnzVlkSNWdpDxIkwcokVeY08No21Obc1KYCqYAIhoJ5qig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۵ ساعت شنا در دریای بالتیک؛ بدون توقف
🔹
یک شناگر با ۵۵ ساعت شنا در مسیر دریای بالتیک، رکوردی قابل‌توجه از استقامت انسانی به نمایش گذاشت. وی از ساعت چهلم بیداری، دچار توهم‌های دیداری شده، اما همچنان به شنا ادامه داده و مسیر را به پایان رسانده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/679283" target="_blank">📅 23:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
ذوالقدر همچنان دبیر شورای ‌عالی امنیت ملی است؟
👇
khabarfoori.com/fa/tiny/news-3236165
🔹
ائتلاف نظامی عربستان - ترکیه - پاکستان/ یک مثلث شوم برای محاصره ایران؟
👇
khabarfoori.com/fa/tiny/news-3236126
🔹
نتایج آزمون مدارس سمپاد اعلام شد/ ثبت‌نام پذیرفته‌شدگان از ۱۹ مرداد
👇
khabarfoori.com/fa/tiny/news-3236142
🔹
آیت الله محمدباقر خرازی فتوای کشتن بی‌حجاب‌ها را صادر کرد!
👇
khabarfoori.com/fa/tiny/news-3236163
🔹
رقابت زنان برای ازدواج با سربازان خط مقدم جنگ | ظهور عجیب «بیوه‌های سیاه»
👇
khabarfoori.com/fa/tiny/news-3236085
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/679282" target="_blank">📅 23:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db145f35f7.mp4?token=n5sgZfC5KO5BBXJlk0gGe48IN_uqXjnzXfHN9rdLktm4LXNolgvrwsLbEmWKNwpIf0hib4sgNvxzg08ViAAZFWm5FKbl_lDhOvtlsPR0aSlzGXKL0Mg-Do-vYYjQcOUz3k33ADO0B1j8NLjIGVpByke_XHLm0F0j-r-ozcv4NXrw6TRRAk-S8arpUbax6KTvelz5-T6Q3uiUXgKNSVw5Pe1FHykqZlt5Kk5jbmezLoNY3OGOsp6WYfZFErM0viaqqw1QwEgdJy8Gm-uSMeDZm0SbPALQDlXe5H3wc3zRLk9HI7PKe55v4NC7PeHCTtrmSQf8m3MVv8JutxpYc45JUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db145f35f7.mp4?token=n5sgZfC5KO5BBXJlk0gGe48IN_uqXjnzXfHN9rdLktm4LXNolgvrwsLbEmWKNwpIf0hib4sgNvxzg08ViAAZFWm5FKbl_lDhOvtlsPR0aSlzGXKL0Mg-Do-vYYjQcOUz3k33ADO0B1j8NLjIGVpByke_XHLm0F0j-r-ozcv4NXrw6TRRAk-S8arpUbax6KTvelz5-T6Q3uiUXgKNSVw5Pe1FHykqZlt5Kk5jbmezLoNY3OGOsp6WYfZFErM0viaqqw1QwEgdJy8Gm-uSMeDZm0SbPALQDlXe5H3wc3zRLk9HI7PKe55v4NC7PeHCTtrmSQf8m3MVv8JutxpYc45JUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اگر بتوانید صحبت‌ها را کوتاه کنید ممنون می‌شوم، چون ما یک جنگ برای پیش بردن داریم
🔹
ترامپ برای فرار از پاسخگویی به خبرنگاران، جنگ را بهانه کرد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/679281" target="_blank">📅 23:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3c86a56e.mp4?token=TZCNC40oslAz4stwdXugwylsJTeBYnFrz_DqFD5--X_ncqQGf3mSkqo4Az8l8n8Wp8YhwyrFJs-bWeg44PJCSq_vqlCWJUVYzK2sa3UrEWxvCBQh4TdXEcjSmPgv40fPVXzmeR9Up6PTpXklv7Kzt7YNdnevvKuMKi2ueINbxd9xNJkKjrW2-W7Maj27UZY9t9HypJFksD9RZiqoVldYd9JLqZtZvJu69XEB1-4IspbEHO2BkpAizYAfRPpOMyE-g5WgKKmU1CS7ijpFcgLsczo0uO8F7nBbWx3Gu5jUQngbfPBcQRv3NsV45yDMFe6osLTD5-v09DPaTaMl6hmPHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3c86a56e.mp4?token=TZCNC40oslAz4stwdXugwylsJTeBYnFrz_DqFD5--X_ncqQGf3mSkqo4Az8l8n8Wp8YhwyrFJs-bWeg44PJCSq_vqlCWJUVYzK2sa3UrEWxvCBQh4TdXEcjSmPgv40fPVXzmeR9Up6PTpXklv7Kzt7YNdnevvKuMKi2ueINbxd9xNJkKjrW2-W7Maj27UZY9t9HypJFksD9RZiqoVldYd9JLqZtZvJu69XEB1-4IspbEHO2BkpAizYAfRPpOMyE-g5WgKKmU1CS7ijpFcgLsczo0uO8F7nBbWx3Gu5jUQngbfPBcQRv3NsV45yDMFe6osLTD5-v09DPaTaMl6hmPHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی‌ها با اطلاعات ناقص درباره همه چیز نظر می‌دهند/ این افراد جامعه را به انحراف می‌کشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/679280" target="_blank">📅 23:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubX59O-aRbRZ_FxngK975Vh4QatJ1jNn1v6yO5hzfwC1CUnTh0qaX3JpzKwt5NLQKMbS5Ewv1pWQ0u3JsGSvBOha9G8Mp88WhObsbTgVibpui1SCDHiI2s04MpPKz3jP8QS6hM5wq20XOEKhYO6ZUnyRzPi93VD4ySCFxbtht62QJzce30KJo2wDq9oYFPbUQNW5GD3qldpfYJG2OXoPvztN6T1McGXL5g0MvZJt8CpYZ3PsHj_GceXyJqz56jDmMkOkqrzMDGJ1ghtLE3K6yedR0L4zPpgHg2R4w3ckrMWA9DjldfLsSRvvv8OzX9pUTKz9EgvPK6VwRiqQNvQH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فروش بلیت رفت و برگشت زائران دهه پایانی صفر از ۱۷ مرداد آغاز می‌شود
🔹
معاون حمل‌ونقل سازمان راهداری و حمل‌و‌نقل جاده‌ای از آغاز فروش بلیت رفت و برگشت زائران دهه پایانی ماه صفر از ۱۷ مرداد ماه خبر داد.
🔹
مهدی خضری گفت: با توجه به پیش‌بینی اوج بازگشت زائران از ۲۳ تا ۲۵ مردادماه، توصیه می‌کنیم مسافران ناوگان حمل‌ونقل عمومی جاده‌ای، بلیت برگشت خود را از همان مبدأ سفر و همزمان با بلیت رفت تهیه کنند.
🔹
وی افزود: زائران می‌توانند بلیت برگشت خود را از درگاه‌های فروش بلیت و [*سامانه سپاس *](
https://sepas.rmto.ir/landing
) سازمان راهداری و حمل و نقل جاده‌ای به آدرس
https://sepas.rmto.ir
تهیه نمایند.
‌
🔗
لینک خبر:
https://rmto.ir/s/mfan7J9
⬆️
با پیشنهاد به مجله از کانال راهبران ایران حمایت کنید
#اربعین_حسینی
#چشم_به_راهیم
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot
🌐
@cheshm_be_rahim</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/679279" target="_blank">📅 22:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b40ffe4d.mp4?token=WIuDlL2ijH6RSCNVm-bis-I93z-Fl0WiilmXxHwKSNHtRbcn9XbK-DnLv9bqpIGapKqFyckjoIIEyLAlSj1QOAnSjyCaRYNjYFtelT6zjDgFFCPG6B0_7LC2y9nHf3lwBSQEMJSZx-RTW22olw9-qv8Y7MTgHsVz7iGBEayqeFyz39cdc76Z3WeCnRxsgHVKGOXv3HUmcQg6rAczHUsTE0g0VD8XRafTBW9sdBGjvlL9ajk7pxi-Km-fHBHBiScAwRAFn-dSQryMNxWVMJPnFgcG6bP_lPYmtlbqFVH_Cw1IzU9Y8oABRrM7lJHt4FPPgZqixbj1kI6b-QEEucn1ayU0fK4Z-9fTQR9al_O5CijH6tp4ZkgeUW_bXnjn5RB3N7kK7bX7qpUjSrOcFSLCR4gxaiJnRgMlpDSakGUT10lILG34_pfCsNeYzalnQrWivbQ34p59KNo0cBBqw5_FNFup1mOiLlgaHY4F68_tMzA6DagnEccFtao_xf3R5Kv-MnVpSsfkuMqO0iuz9yYatuTCQ9U3Bm871ysKOd89uWkCjrtuaZ5Z7NaNQBwecg-28JCl-YjJ2dZ45IDQafUbmgxrSzEE9W1ahvZnJlKGDd44-GCj0Eg7_m1Kpq-AqBc73-hdpn4w9yYIJPAOP9o0jIHXZE39NNzs5UMhTND365w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b40ffe4d.mp4?token=WIuDlL2ijH6RSCNVm-bis-I93z-Fl0WiilmXxHwKSNHtRbcn9XbK-DnLv9bqpIGapKqFyckjoIIEyLAlSj1QOAnSjyCaRYNjYFtelT6zjDgFFCPG6B0_7LC2y9nHf3lwBSQEMJSZx-RTW22olw9-qv8Y7MTgHsVz7iGBEayqeFyz39cdc76Z3WeCnRxsgHVKGOXv3HUmcQg6rAczHUsTE0g0VD8XRafTBW9sdBGjvlL9ajk7pxi-Km-fHBHBiScAwRAFn-dSQryMNxWVMJPnFgcG6bP_lPYmtlbqFVH_Cw1IzU9Y8oABRrM7lJHt4FPPgZqixbj1kI6b-QEEucn1ayU0fK4Z-9fTQR9al_O5CijH6tp4ZkgeUW_bXnjn5RB3N7kK7bX7qpUjSrOcFSLCR4gxaiJnRgMlpDSakGUT10lILG34_pfCsNeYzalnQrWivbQ34p59KNo0cBBqw5_FNFup1mOiLlgaHY4F68_tMzA6DagnEccFtao_xf3R5Kv-MnVpSsfkuMqO0iuz9yYatuTCQ9U3Bm871ysKOd89uWkCjrtuaZ5Z7NaNQBwecg-28JCl-YjJ2dZ45IDQafUbmgxrSzEE9W1ahvZnJlKGDd44-GCj0Eg7_m1Kpq-AqBc73-hdpn4w9yYIJPAOP9o0jIHXZE39NNzs5UMhTND365w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره پزشکیان از ساخت خانه‌های بهداشت با همکاری بسیج زمانی که رئیس دانشگاه علوم پزشکی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/679277" target="_blank">📅 22:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d1f13f40.mp4?token=e8p8MoIt8U1_n4gEGPnGrzCRMohFupQdSTBpTTwUTtM-gjDDgRljgSKF7d8vsaAifoimJ4Nb8eMh7DA8VSfORWqOeVqTYi0-vGmNcHOXBjaXGBgP3hSFBDsHyLIq4r_3zQT7KPxpneVOJ-hHIfKPhXwihwlk4KGBCLIvj-KSe_CdJ2aJCsYtNfy2wUyhlQ7eUVcOI4_jyWaCe-_ilA1oOGY5Y1h4gS-EIJ0xyrR7oW2bgJz4mWhOGYpX0HjZwXEiwltWJjTDmY03ZvN-mkfUzkExNdI7ESRXwuGrKmfOf0VSdK8g1au3b0nZAH803Uka8SK0HoRRSq5IBLxNLeRjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d1f13f40.mp4?token=e8p8MoIt8U1_n4gEGPnGrzCRMohFupQdSTBpTTwUTtM-gjDDgRljgSKF7d8vsaAifoimJ4Nb8eMh7DA8VSfORWqOeVqTYi0-vGmNcHOXBjaXGBgP3hSFBDsHyLIq4r_3zQT7KPxpneVOJ-hHIfKPhXwihwlk4KGBCLIvj-KSe_CdJ2aJCsYtNfy2wUyhlQ7eUVcOI4_jyWaCe-_ilA1oOGY5Y1h4gS-EIJ0xyrR7oW2bgJz4mWhOGYpX0HjZwXEiwltWJjTDmY03ZvN-mkfUzkExNdI7ESRXwuGrKmfOf0VSdK8g1au3b0nZAH803Uka8SK0HoRRSq5IBLxNLeRjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: وقتی می‌توانیم حق‌مان را با گفت‌وگو بگیریم، چرا باید بجنگیم؟
🔹
با گفت‌وگو توانستیم جنگ لبنان را متوقف کنیم، محاصره را برداریم و برخی تحریم‌ها را کاهش دهیم. عده‌ای می‌خواهند بجنگیم؛ همان چیزی که اسرائیل می‌خواهد تا ما را وادار به تسلیم کند. ما کوتاه نخواهیم آمد، اما وقتی حق‌مان را می‌توانیم از گفتگو بگیریم، چرا باید همان مسیر اسرائیل را ادامه دهیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/679276" target="_blank">📅 22:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679275">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
پزشکیان: کسی که نمی‌داند همین‌جوری می‌گوید بزن، تبعاتش را هم باید بداند؛ در شورای‌ عالی امنیت ملی ۱۲ نفر از موضع ما دفاع کردند
🔹
در شورای امنیت ۱۲ یا ۱۳ نفر حق رأی داشتند و ۱۲ نفر صحبت و از موضع ما دفاع کردند. کسانی که در میدان ایستادند، آدم‌های ترسویی نبودند؛ همان کسانی بودند که این افتخار را خلق کردند و ما به آن‌ها افتخار می‌کنیم. همین افراد بودند که کشور را تا امروز با قدرت اداره و از آن دفاع کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/679275" target="_blank">📅 22:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679273">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2bd08c43.mp4?token=vXfxsXWbgwiw8LZ-rHXO-CUgCyPJRSOytjnGIi3IVNXjxfLWJmExbGqVRyHlRIO86z7u-Z6jCb76jKU-TDXbgSnlILja2BQmIAg-o411tVxvZbGBIJaJq5HEj79u_uxJLPktiK-bmZ71pOCXYQA6LvZ3shcat3-6-Hw185xYiYnW83Chq8KrIljhI0H4jQ6mlC4chci5xK6sAtjZEtIYABZu6wdgeX9Rj_1F0hSoYPVNHvVbMe6sqoYQEqRqsoyIeyjM_OEiy6nhp2_mVj5TnPgufrfEwcXp8DsjMy30vqys6Y8MMJMXM902wMWCDnIHj48Kt0aMys37rUTVu2ZzUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2bd08c43.mp4?token=vXfxsXWbgwiw8LZ-rHXO-CUgCyPJRSOytjnGIi3IVNXjxfLWJmExbGqVRyHlRIO86z7u-Z6jCb76jKU-TDXbgSnlILja2BQmIAg-o411tVxvZbGBIJaJq5HEj79u_uxJLPktiK-bmZ71pOCXYQA6LvZ3shcat3-6-Hw185xYiYnW83Chq8KrIljhI0H4jQ6mlC4chci5xK6sAtjZEtIYABZu6wdgeX9Rj_1F0hSoYPVNHvVbMe6sqoYQEqRqsoyIeyjM_OEiy6nhp2_mVj5TnPgufrfEwcXp8DsjMy30vqys6Y8MMJMXM902wMWCDnIHj48Kt0aMys37rUTVu2ZzUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا پزشکیان به جای قالیباف تفاهم‌نامه آتش‌بس را امضا کرد
؟
رئیس‌جمهور:
🔹
کلیات توافق نهایی شده بود و برای افزایش اعتبار آن، قرار بود امضای نهایی از سوی ترامپ انجام شود تا امکان عقب‌نشینی از توافق وجود نداشته باشد.
🔹
اما کمتر از ۲۴ ساعت بعد، روند مذاکرات به‌طور کامل تغییر کرد و توافق به سرانجام نرسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/679273" target="_blank">📅 22:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679272">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb3e9b49de.mp4?token=YGOIxQc_KL9YGFXDGIZB0BnqQT3NY7GCoXroNWtOJgrzGw2g-gPzPraXztmjAtGq05WSgt0JnkcPpvDVIiCr7DRxlcPby3ygMaTZ9p02Eze7I3v6sEgcPWoYqhPrC402jlo_DnI6ElvQ5OPDR4wDyC680Oma-0g3PguwOrZMxytFLohXuCzR26_BxFadKS4KJNpezjECvzLCVl1QD-CYcvCyGgHdiTy5Ka9dExSmylPLzVfiGR5g7sqyQ4ZNR3qL_pVZPXvzXDQfWws_N47wGkahLkimTZMtynjcHmP_evV1ZXDD_VTEZgvaAsrOc98gQTXJjnqkr1yiT8FTitUYPxxyZcjB_2VVBtoTQ3FtLaeWKjSxcfZCN-EXyd4QpO5ZMEMk4kFiK62p_pHRIL7f5kwE49dAjw-JbSpZ-R9G-7JHRfjg0PXhJFVqf86xR_0_4eP5Yos6UaMg3ahRhwreRcl1SCgpYXYPyixiDMgzrHYtEoVRseZVQgRUofMfZqp-_k5lwu4ETXczpqjMet5rnasAvPJhL2ol0m3FvsBIT5Jva0K3baZ2073b-puu1zvvFw3x86EshepzIpnB2Bnl5CZU7Jws_iAQtPkkQTZRbgn0NtXHALiR44rv8oH0HSl8hh99v4PsO2T32o-j9YvAtghT7tf6w_wu4X_R4ppv5jk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb3e9b49de.mp4?token=YGOIxQc_KL9YGFXDGIZB0BnqQT3NY7GCoXroNWtOJgrzGw2g-gPzPraXztmjAtGq05WSgt0JnkcPpvDVIiCr7DRxlcPby3ygMaTZ9p02Eze7I3v6sEgcPWoYqhPrC402jlo_DnI6ElvQ5OPDR4wDyC680Oma-0g3PguwOrZMxytFLohXuCzR26_BxFadKS4KJNpezjECvzLCVl1QD-CYcvCyGgHdiTy5Ka9dExSmylPLzVfiGR5g7sqyQ4ZNR3qL_pVZPXvzXDQfWws_N47wGkahLkimTZMtynjcHmP_evV1ZXDD_VTEZgvaAsrOc98gQTXJjnqkr1yiT8FTitUYPxxyZcjB_2VVBtoTQ3FtLaeWKjSxcfZCN-EXyd4QpO5ZMEMk4kFiK62p_pHRIL7f5kwE49dAjw-JbSpZ-R9G-7JHRfjg0PXhJFVqf86xR_0_4eP5Yos6UaMg3ahRhwreRcl1SCgpYXYPyixiDMgzrHYtEoVRseZVQgRUofMfZqp-_k5lwu4ETXczpqjMet5rnasAvPJhL2ol0m3FvsBIT5Jva0K3baZ2073b-puu1zvvFw3x86EshepzIpnB2Bnl5CZU7Jws_iAQtPkkQTZRbgn0NtXHALiR44rv8oH0HSl8hh99v4PsO2T32o-j9YvAtghT7tf6w_wu4X_R4ppv5jk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاهم‌نامه آتش‌بس با هماهنگی، تفاهم و همدلی در شورای امنیت ملی شکل گرفته است
🔹
ما با نیروهای نظامی کاملاً هماهنگ هستیم و پشتیبانی از آنان را وظیفه خود می‌دانیم. کسانی که جانشان را کف دست گرفته‌اند و از این کشور دفاع می‌کنند، مگر ممکن است میان ما و آنها اختلافی باشد؟ شکی نیست که این تفاهم‌نامه با هماهنگی، همدلی و تعامل کامل شکل گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/679272" target="_blank">📅 22:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679271">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/229a1d9bf0.mp4?token=uP-lItLMN8S_HmvhjOcLLYN6ZfpF0LVvqKweFD_LY7WgqsHMQjZsCXNJ8p8hx1yMwU_ymTZJ5an8bCCjqz9C_THR5-M84q8wMkoNeYSX95dJAuSWC2dSSbg7D3iqauTODQna2DzUpxHq7ZGyGVamiLwq88fji58GzJMg_vLH23PluMl-0hnxAdKu6L7i0b1fxsmSKz2f6Mgcooku4aoGbJhFG1nXZvdA8L1cqkyem8SGMRD-F1VXBjiKmX2r20vnLtLyo-VAkJey4_vqUPoMpoLrmRwQUviT5de0b2swq67ZOArem69Gyjy3ALwdOnywSBjY7rq9Qir-UKPY487G9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/229a1d9bf0.mp4?token=uP-lItLMN8S_HmvhjOcLLYN6ZfpF0LVvqKweFD_LY7WgqsHMQjZsCXNJ8p8hx1yMwU_ymTZJ5an8bCCjqz9C_THR5-M84q8wMkoNeYSX95dJAuSWC2dSSbg7D3iqauTODQna2DzUpxHq7ZGyGVamiLwq88fji58GzJMg_vLH23PluMl-0hnxAdKu6L7i0b1fxsmSKz2f6Mgcooku4aoGbJhFG1nXZvdA8L1cqkyem8SGMRD-F1VXBjiKmX2r20vnLtLyo-VAkJey4_vqUPoMpoLrmRwQUviT5de0b2swq67ZOArem69Gyjy3ALwdOnywSBjY7rq9Qir-UKPY487G9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: استعفا نخواهم داد، خواهم ایستاد ما نوکر مردمیم، در خدمت مردمیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/679271" target="_blank">📅 22:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679270">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7398bed0ec.mp4?token=GTyivKl6drWm1u7-Uk6GbTFnCNOjZbZX6BSa4fwJ3pMNMot-73YG-T_4fpI8twTJx4NY54kCNPDpIf3a0BH36zNjOnR6LPSIAbJNVfWeu3Y58yRKpShP5K8OKRptkFwxZwpY8EDiidqhgHIE49rhUswA5_dz2bBuXaHe_VheDvf2azaRfuIdqYTp0sI9a3BJ7CC3q7ciNf1_YrFI2paKqqCMIsf2uonZzAFU5k8HXLV341CYTS6V6Ou_Wunt-eXEsKg5zvQbsUHfyawHXpIC8Fzv04u_zFhTL5xkpnvtzFVk0XHmjOLFV6Yl_PyVC_6biSYX5KsAHUdvlTShtN4PPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7398bed0ec.mp4?token=GTyivKl6drWm1u7-Uk6GbTFnCNOjZbZX6BSa4fwJ3pMNMot-73YG-T_4fpI8twTJx4NY54kCNPDpIf3a0BH36zNjOnR6LPSIAbJNVfWeu3Y58yRKpShP5K8OKRptkFwxZwpY8EDiidqhgHIE49rhUswA5_dz2bBuXaHe_VheDvf2azaRfuIdqYTp0sI9a3BJ7CC3q7ciNf1_YrFI2paKqqCMIsf2uonZzAFU5k8HXLV341CYTS6V6Ou_Wunt-eXEsKg5zvQbsUHfyawHXpIC8Fzv04u_zFhTL5xkpnvtzFVk0XHmjOLFV6Yl_PyVC_6biSYX5KsAHUdvlTShtN4PPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ دولتی به اندازه ما در جهت سیاست‌های رهبری قدم برنداشت
🔹
اینکه عده‌ای اختلاف‌سازی کنند و القا کنند رهبری چیزی می‌گویند و دولت چیز دیگری، هم در حق رهبری جفاست و هم در حق دولت. با قاطعیت می‌گویم هیچ دولتی به اندازه "دولت چهاردهم" در مسیر سیاست‌های رهبری گام برنداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/679270" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679269">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce7d20fd3.mp4?token=PTqTTL3mkJ3D-HZCmliAIlFKweSFaxUPo_VwTK5sh2NYDBEU8-d1AyqFSXaXC4-o58YN5UZ5vjFyyaqkRruXwDnNrrK3k5HXQDzSGJ3iACXSOHzur-ITmHzPo8vciYnb7Ts9s1t_03-8ica_fcGEQZKtz5n23eJDFdv9nMeBmH7JBMwprM4rMigHkl1nHJPMbuIlnVOJL__Kxw6v23EWSHzheBVEUPyxNPEbBD9tORRU8JMvnhoAzc57sjDIRQYOoWItdjYIa7QwpM6CHPxzwYO4_fH5WA5uydM1njlCHaBdK9cupKOyyLXgqSzHcr6Tq0Y9-4XbO2Bm91m5JLoqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce7d20fd3.mp4?token=PTqTTL3mkJ3D-HZCmliAIlFKweSFaxUPo_VwTK5sh2NYDBEU8-d1AyqFSXaXC4-o58YN5UZ5vjFyyaqkRruXwDnNrrK3k5HXQDzSGJ3iACXSOHzur-ITmHzPo8vciYnb7Ts9s1t_03-8ica_fcGEQZKtz5n23eJDFdv9nMeBmH7JBMwprM4rMigHkl1nHJPMbuIlnVOJL__Kxw6v23EWSHzheBVEUPyxNPEbBD9tORRU8JMvnhoAzc57sjDIRQYOoWItdjYIa7QwpM6CHPxzwYO4_fH5WA5uydM1njlCHaBdK9cupKOyyLXgqSzHcr6Tq0Y9-4XbO2Bm91m5JLoqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: استعفا نخواهم داد، خواهم ایستاد ما نوکر مردمیم، در خدمت مردمیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/679269" target="_blank">📅 22:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679268">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb3e9b49de.mp4?token=CIZTepZnFDAnNjkLD8_ICCGiCaPjEQkGp-3ek6aYUvk63v39xhgqR7uoaYZbdlgJM0dn30wK0lV6M7uJ3LPhvEMG9I6OC0Nwjgt-xSnNZNo3hwwpUYLh5nUJnyeVwBgPiar9BVtfzWf4o6O3xAffQZFVsp9SYpjzol7kZg1pF-xWn450Pn1jBnRfpcgZBLD6WFQdbk54nLAJEDHur88F21DmhyXv72d2HY87Loe_FB2aNyl7Xkf8buFkTB_BKl0yrjVWufvNRiNvT_g_O22-VPD4wD-jpYANfWxajevRHhOrZWH6Yh0YZchH9D6VIr4RqKamn4e7cCUU0GybbU_-xpGCBpMLVTZGT9xtj8MDB-WQdgHL8bg9hOkJIaMY6yvOVnqwLsjo4mKlqrPxLEffOQbj-pclELrNWkUTdSRdE3D54ddEPMhpqGzU-ROXXc38hm-6BwgmV9cgejgRL1yIdHSI0IYtAfX0ZfpSiwbzT_QXm528kGvBy9egive8oeZ_Ee9u7ZFgz2p65rpP_oevqTW8W8ZeoC865p3DV3XyEq812T99YBrbsXmYvL9JyXJfM_4gW2L3OTzLUpsQ0YhTq-0O1r9L8wIA6wPVdYJ9moDfnaQCKH-TGXi-Q_d2xYAy18-Gy4jW10GPSnVjdMa_pfJrnSzYyGXPS4npSO2LjwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb3e9b49de.mp4?token=CIZTepZnFDAnNjkLD8_ICCGiCaPjEQkGp-3ek6aYUvk63v39xhgqR7uoaYZbdlgJM0dn30wK0lV6M7uJ3LPhvEMG9I6OC0Nwjgt-xSnNZNo3hwwpUYLh5nUJnyeVwBgPiar9BVtfzWf4o6O3xAffQZFVsp9SYpjzol7kZg1pF-xWn450Pn1jBnRfpcgZBLD6WFQdbk54nLAJEDHur88F21DmhyXv72d2HY87Loe_FB2aNyl7Xkf8buFkTB_BKl0yrjVWufvNRiNvT_g_O22-VPD4wD-jpYANfWxajevRHhOrZWH6Yh0YZchH9D6VIr4RqKamn4e7cCUU0GybbU_-xpGCBpMLVTZGT9xtj8MDB-WQdgHL8bg9hOkJIaMY6yvOVnqwLsjo4mKlqrPxLEffOQbj-pclELrNWkUTdSRdE3D54ddEPMhpqGzU-ROXXc38hm-6BwgmV9cgejgRL1yIdHSI0IYtAfX0ZfpSiwbzT_QXm528kGvBy9egive8oeZ_Ee9u7ZFgz2p65rpP_oevqTW8W8ZeoC865p3DV3XyEq812T99YBrbsXmYvL9JyXJfM_4gW2L3OTzLUpsQ0YhTq-0O1r9L8wIA6wPVdYJ9moDfnaQCKH-TGXi-Q_d2xYAy18-Gy4jW10GPSnVjdMa_pfJrnSzYyGXPS4npSO2LjwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به شایعه تهدید رهبری توسط رئیس‌جمهور
رئیس‌جمهور:
🔹
ما با نیروهای نظامی کاملاً هماهنگ هستیم و پشتیبانی از آنان را وظیفه خود می‌دانیم. کسانی که جانشان را کف دست گرفته‌اند و از این کشور دفاع می‌کنند، مگر ممکن است میان ما و آنها اختلافی باشد؟ شکی نیست که این تفاهم‌نامه با هماهنگی، همدلی و تعامل کامل شکل گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/679268" target="_blank">📅 22:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679267">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30eb98c40c.mp4?token=Lp4pcVduyjXRn4iLX7YAbCb9Gzi3SeDZpounntXR3L525Vp848E0ZeAGoo7GDa5jl7OvqCfT6_CBjGy3yhc17f1Qg0_PReJkbR95cbuK0PZRpAf1i1CsDlE76nfQ_GEUjgPaXTdOs5DB0s7NG5FhvzU2r_CRR4igQ0U0GJdtlbWOrfFrUD3X1dyR3C0wa8iX9xHZj7pNVlx1XUoDWMAY-llIrAvwTRjrFlq5cEu6zkcsNvGrUL-JQAuy_15cukeja3tYj-B9yd9hX_45i6Yr_m0WOT0rHdNmkpsOiF6GUxpZAQ1xRym049segutI7AalJnH8rERKX9ITC-gdrdAGDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30eb98c40c.mp4?token=Lp4pcVduyjXRn4iLX7YAbCb9Gzi3SeDZpounntXR3L525Vp848E0ZeAGoo7GDa5jl7OvqCfT6_CBjGy3yhc17f1Qg0_PReJkbR95cbuK0PZRpAf1i1CsDlE76nfQ_GEUjgPaXTdOs5DB0s7NG5FhvzU2r_CRR4igQ0U0GJdtlbWOrfFrUD3X1dyR3C0wa8iX9xHZj7pNVlx1XUoDWMAY-llIrAvwTRjrFlq5cEu6zkcsNvGrUL-JQAuy_15cukeja3tYj-B9yd9hX_45i6Yr_m0WOT0rHdNmkpsOiF6GUxpZAQ1xRym049segutI7AalJnH8rERKX9ITC-gdrdAGDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ امتیازی در تفاهم‌نامه ندادیم/  نیروهای مسلح موافق آتش‌بس بودند؟
🔹
تا جایی که آنها عمل کنند، ما نیز عمل می‌کنیم. آنچه به دست آوردیم امتیاز بود؛ اینکه آمریکا از محاصره کنار کشید، به معنای امتیاز دادن ما نبود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/679267" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679266">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
پزشکیان: از شهادت نه تنها نمی‌ترسم بلکه برایم فوز عظیم است. اما اینکه نتوانم مشکل جامعه را حل کنم برایم قابل قبول نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/679266" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0001a40725.mp4?token=u15MBG_1fhzCnxf8RUxdjrO9qzCcnZOQHuUXdsi9vyz5accjIy9uxTvzR0F-YNWGCRR6tdh4ouCuMMDnVhzQvTA9yIXRuJ37WMxoKn5rDtajSngOOgb-RiEWqZdDvtdkNxtM1xU8yzWNStpi6KTBdeMye2h6wgrcgFAwBBot_Ucy6aPA081qzxWZKIwhsQ9bhgZI9V_QLHsX4Hote_tker8Kggikv731FWxDBOCsc6Qr6emr6URAhG2FgkSCOSgId3oy36mgc8j4WTBvkdcMPpjjXZScnoBKPnZ9zt9WtAvptw-MbC7BFV09XA4ooU6w0j8unQQfAsofYtpV6Nj3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0001a40725.mp4?token=u15MBG_1fhzCnxf8RUxdjrO9qzCcnZOQHuUXdsi9vyz5accjIy9uxTvzR0F-YNWGCRR6tdh4ouCuMMDnVhzQvTA9yIXRuJ37WMxoKn5rDtajSngOOgb-RiEWqZdDvtdkNxtM1xU8yzWNStpi6KTBdeMye2h6wgrcgFAwBBot_Ucy6aPA081qzxWZKIwhsQ9bhgZI9V_QLHsX4Hote_tker8Kggikv731FWxDBOCsc6Qr6emr6URAhG2FgkSCOSgId3oy36mgc8j4WTBvkdcMPpjjXZScnoBKPnZ9zt9WtAvptw-MbC7BFV09XA4ooU6w0j8unQQfAsofYtpV6Nj3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: با امر و نهی نمی‌شود جامعه را اداره کرد
🔹
مطابق آنچه امیرمومنین(ع) در نامه خود به مالک اشتر فرمودند امر کردن یعنی فرار از دین و باور.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/679260" target="_blank">📅 22:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b87f6a3558.mp4?token=ajFBiCQhn3hkpEWAZr3uGauBeSmZZwOwBqCbUM-a2MrPRxkJgvAgqCUr_K-50DCK4WQMgBY40_G7Js_aw-tHsW_qSXBkFyhxBsh02NPY5pY_OV3nRMehermi9vqgUUZcjgFCR9VnCjVqI3KDvqMummyWDnQ24z-0OT7HwcB_JXr9720BMTvoTaLzxA3DR_zzIi9o1lJcFYVRx4F4KZj-6S4nlDiLpta5SNjstJruI0yZurvNgaR9bZQFMavazBDK_Ra7iDLVtdjGPlivHxba0FNBKzygcudUILFQ_f6oDTK3fGaiahIzUpksKmp5uz3Okoqr0UHQvmC6DbEfyoFu1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b87f6a3558.mp4?token=ajFBiCQhn3hkpEWAZr3uGauBeSmZZwOwBqCbUM-a2MrPRxkJgvAgqCUr_K-50DCK4WQMgBY40_G7Js_aw-tHsW_qSXBkFyhxBsh02NPY5pY_OV3nRMehermi9vqgUUZcjgFCR9VnCjVqI3KDvqMummyWDnQ24z-0OT7HwcB_JXr9720BMTvoTaLzxA3DR_zzIi9o1lJcFYVRx4F4KZj-6S4nlDiLpta5SNjstJruI0yZurvNgaR9bZQFMavazBDK_Ra7iDLVtdjGPlivHxba0FNBKzygcudUILFQ_f6oDTK3fGaiahIzUpksKmp5uz3Okoqr0UHQvmC6DbEfyoFu1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آمریکا تلاش می‌کند همسایگان را علیه ما بسیج کند
🔹
خیلی از مشکلاتمان با کشورهای همسایه را برطرف کردیم اگرچه آمریکا و رژیم صهیونیستی با توطئه و جنگ اخیر به دنبال ایجاد اختلاف بین ایران و کشورهای حاشیه خلیج فارس هستند.
🔹
طبق فرموده پیامبر گرامی اسلام همه مسلمان باهم برادر هستند چه شیعه باشند و چه سنی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/679259" target="_blank">📅 22:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc165756bb.mp4?token=VOTE05qEIsM0zhE9FjSCqqQE4WtFnHMvzr5Wlyxr_7kDPp2w3OkeVK-iytpW7VEXslbPta1jyl_UDxRGGkdxNJhB3QVQSMAjLr8zo0JT2CzpBBYSCEq-YSMmHPK5ICK9EFoML8s2fAmJLYuJEr6OvxomzIxu-eHEPZxTdi7xM7Z-YxB6nzMV7j8S7tMs0cDuqS-UH-5f90o2_-yIQDSHMD9kx0AqG3-ge7ODYlpd3Jdt6LgFoEsm43kcwUlGZsLoC8_MNaHj-85fdejla5XJkaWenJt7X5WkJERbLbpP4Ad1CoD4mJp4Fnphgjal78GByZc4oaaaeiUW7jqaKdiLmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc165756bb.mp4?token=VOTE05qEIsM0zhE9FjSCqqQE4WtFnHMvzr5Wlyxr_7kDPp2w3OkeVK-iytpW7VEXslbPta1jyl_UDxRGGkdxNJhB3QVQSMAjLr8zo0JT2CzpBBYSCEq-YSMmHPK5ICK9EFoML8s2fAmJLYuJEr6OvxomzIxu-eHEPZxTdi7xM7Z-YxB6nzMV7j8S7tMs0cDuqS-UH-5f90o2_-yIQDSHMD9kx0AqG3-ge7ODYlpd3Jdt6LgFoEsm43kcwUlGZsLoC8_MNaHj-85fdejla5XJkaWenJt7X5WkJERbLbpP4Ad1CoD4mJp4Fnphgjal78GByZc4oaaaeiUW7jqaKdiLmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور : مسجد فقط برای مذهبی‌ها نیست، برای همه مردم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/679257" target="_blank">📅 22:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679253">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7gNfyL7KymWPg6Rd5GJlX8SUceWDKuTTZSczdTMLi-tnoozjnhCSU1rKvh0B_X-FWrT4RD95H7W_zUGJ9saP3hYWM6yxjnaOAvTtUx6W-UN624Kw0i9woMtYZ0Ar2jVEIXfhzL2KSRmU7kHOiCfMJMdk4gFfOLN-bMXh4ZAg9xBUTsPd73FW5yUmtZjVN-i5f8Uwwzqg1B0wu_W_DojGfMHgE_fIJI7WQgIqxU2RVR3DQUfkv9-huLZRwnsoIN1KFK6q2iLrU729F19SmnbgeqFj7x7uNQ8u90L4Sa8T1cI3HFGI7p-PUNGehw2irELUAVq3_6q9yfdW5-HGQGDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از کارتر تا ترامپ؛ چرا واشنگتن مدام در مورد ایران اشتباه می‌کند؟
🔹
از زمان بحران اشغال گروگان‌گیری سفارت آمریکا در تهران تا دوران ریاست‌جمهوری دونالد ترامپ، تقریبا همه دولت‌های آمریکا در برخورد با ایران با یک مشکل مشترک روبه‌رو بوده‌اند؛ این تصور که می‌توان با فشار، تحریم یا حتی تهدید نظامی، ساختار سیاسی آن را تغییر داد. اما تجربه نزدیک به پنج دهه گذشته نشان می‌دهد واشنگتن بارها در شناخت ایران و نحوه واکنش این کشور دچار اشتباه محاسباتی شده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3236097</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/679253" target="_blank">📅 21:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlU7hcr1Mrpmgmhja47uVW1DkBjnBBu7_sswYD3UKntX6xwiq0ViO1LNpBbsKFgrjbgS41CrablLSgGiBISpmdvYUetAaXYvG7skwauRrs41BMLga9df8ZgXUFs7pdN6RwO5o79Cg3sWhG3Y1uuamBWF36MeD9ragJ-uKQV6jDrDCsR4NACDhmC6MI6TOgavgnkjRS0Q8dxWawvUMCeRU1kncgz4YImlBSXIOp4PJqO37rfnXxE-PYe86oRPKbFKomkTmy-hf_5bJP2SWlvD88yCTOJe0lK7glc3eX_OSiUmQGMYvvIvNCtfTJnR2aT3-TqJm-MIJMVqM37n3VVeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤎
تسبیح سنگی ۱۰۰تایی
ذکری از جنس ارادت...
این تسبیح از سنگ سِرپانتین، معروف به سنگ امام‌رضا(ع) تهیه شده و روایتی درباره این سنگ در کتاب عیون‌الاخبارالرضا، باب ۳۹ نقل شده است.
✨
💸
قیمت اصلی: ۱,۱۴۷,۰۰۰ تومان
🔥
قیمت ویژه: ۹۴۰,۰۰۰ تومان
⚠️
تعداد محدود | تا پایان موجودی
🛍
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/679252" target="_blank">📅 21:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679249">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q89tBiqfCAS4BAZ6SLpHSHvJcaJaRYuzrYyv7flddiWYcTcnCtAV_-DKIqt3osC4J1p4rTWyPOaVuqbgI2B-20gFz13-kEtBxmIK03q1J-cKcDcu6qpjI3Jie4Sk8JIeKE3xntunQ2WjsnMUH6624TkNEx8316UUjfnnBfwc8YXPCAgyiortIVWpcg9_pSo-Psg57AW4zT6VnS9x6IW8aVuP2XrQfhivaiJmqEpiMpZE5TEzy2uVbSQ5ZaSuoRroIsk0wotTD1hClELMJOBGPusJGGiuwUe_MLJfdTwSy2towXuNWUWxnWdsME3zuj-CE-GCvYOHaRRAlRWvU80uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استرس و اضطراب؛ دو حس شبیه با دو ریشه متفاوت
🔹
استرس معمولاً واکنشی به یک عامل یا موقعیت مشخص و بیرونی است و با برطرف شدن آن عامل، کاهش پیدا می‌کند.
🔹
اضطراب ممکن است حتی بدون وجود یک دلیل یا تهدید مشخص ایجاد شود و برای مدت طولانی‌تری ادامه پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/679249" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6OXN_rTPGSSDfSqMnHa1GbZ6_a8naXBid3ggz4T4ncBaf7d00cPklqC5TD3H9HYxFJUi8VKjn2f_kQEVdEEnHDQadsPrkM17KcGQJlrGC3OaW7L2YDvia6eG9IGnyvHO41bGXFD2MLZQhE1HkXYQ6pb8s4RsqXCvtO1lFe0ECy3y-lKL39SzbygQ3BTXEvCQgTW2HskAOgh7yLDhVOgkE7a_5VlSzoqkSzOKMCMDCO7yynVPAYW5nah0v-aHzcPARL70Ks96_T6MrVTG2oQsdbJ7_5oKOH1GgHjIzEaY4Xrybnf2TT91vRsDr7ofvQ9M9lLj0VWv9sUXTvgPPKZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفریقا، موتور اصلی رشد جمعیت جهان
آفریقا با افزودن ۳۶.۲ میلیون نفر در سال، موتور پیشران رشد جمعیت زمین است و آسیا نیز با ۲۹.۵ میلیون نفر افزایش سالانه در رتبه بعدی قرار دارد.
در سوی دیگر، اروپا تنها قاره‌ای است که روند منفی را تجربه می‌کند و سالانه حدود ۹۹۲ هزار نفر از جمعیت خود را از دست می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/679248" target="_blank">📅 21:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679247">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McGIDagYCLWNpcDpzXaPyvnj9jOJ61Yr4I9SgJBX1o78c7zw4_7G2Kp4bP-mdDYOG9YQL6QHS_LQhDh0xFHhh--rsZGTP9AY8XD8izEjVJbuHGWfg3he89lhcnojw6nY7hM4Tlvt3Ti6qX0UQEtCiAX2Cy2sk2vrTwQF-bwcDSWDN8Av6RfKbGNnMd0eAlc93R5ELrv_b0KLSEbkaru73-ZxdT-_c4cHVNvwln9d8aBLtgiXvyyCen1fXQTd1LxwU-jS9aa4nFGMTofQ73wRN30mUfBhIHSf9PAmq5j79DWalE6ZL_dd6OyyB_tSHjJXfDAXOX1YwiJLqXhbSxOM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آکسیوس: مذاکره‌کنندگان ایرانی منتظر تایید نهایی شعام در مورد توافق با عمان و آمریکا هستند
باراک راوید، خبرنگار آکسیوس، به نقل از یک دیپلمات از کشور میانجی:
🔹
انتظار داریم این تایید به زودی انجام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/679247" target="_blank">📅 21:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679245">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ2GfW4UUHgjK7kjn0fzju6BIXHH1ZTKouidIWUCnIZJ7TNkiTB_dcRR4g5a9wjG149-xRWHcK5iuDxEUF-wMtI2qHxTSKq8j3OXUNCLdY07wMCZNPkSzB4KnG4asjzJorSeQKRfCiLz31Z0DTEV_xng-SwG8YX4wAslnSKKRjGDbMcUETt90Lim4lm7em1GcKC4imBz8zJB4PKLRLuZP9a5KBqO_OLRYm__MYrD7lBJorcehnMq2oTsxbIPHLOxjkXXjBBHi-nw96wDtQDRo53blWaAn1dVBEw-ls4xh0jMMLiztkymlYdc5JlzedGeoh3WJCUfc1mOtBxCNZf7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در حمله‌ به رسانه‌ها، ناخواسته یک افشای محرمانه را تأیید کرد |‌ پایانِ ماه عسلِ اطلاعاتی!
🔹
در دنیای پرتلاطم سیاست واشینگتن، گاهی یک پیام کوتاه در شبکه‌های اجتماعی می‌تواند به اندازه یک گزارش تحقیقی بلند، ضربه سنگینی به اعتبار و امنیت یک دولت وارد کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3236110</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/679245" target="_blank">📅 20:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679243">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLnMQWg6kfspbrDWITL7e5ccgUhBVJ23czP5G0-LiGLQC_rlpIKRRQFN92fjzoIapey7m3JhDHmVFDheVQFu0Zs6lFh2j463icTeOgBwoKG8n6-cgBK6yyPDx3CS7Vyb8dPbx16jE2TkL1K_YAVI0ojDl5wYOaifSn2fdV69FvF9j4R49VgqX5iIBKO0Kc8iaNYP5Wc23x8GTPm8TRJhDwnhaGcGErewObd-VoRwh_lD7xnWYP1aTtzZv6KDSwoM6KEetS_f7q6w0YApuCym2bFEIJ0DJkNxfVSjErifwL6ksau-PkQAneYU3zUYyg5_Bdjr5vEnAvUERkRi5i0pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان طلایی مصرف مکمل‌ها؛ بیشترین جذب، بهترین نتیجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/679243" target="_blank">📅 20:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
طلب مرگ، ایست قلبی و بازگشت از برزخ؛ ماجرایی که زندگی یک مرد را دگرگون کرد
🔹
00:08:15 طلب مرگ از خداوند در روزمرگی‌های زندگی
🔹
00:18:30 حضور در ۳ مکان مختلف به صورت هم زمان
🔹
00:24:10 رؤیت وضعیت ناراحت‌کننده کودکم به خاطر بداخلاقی‌های دنیوی من
🔹
00:39:00 تغییر رنگ و موزیک در گل‌ها برای شادمانی من
🔹
00:41:10 مراقبت اهل بیت حتی از افرادی که منکر وجودی آنها هستند
🔹
00:46:19 تغییرات رفتاری تجربه‌گر بعد از تجربه
🔹
00:51:50 متولد شدن دوباره و تأکید بسیار به رعایت حقوق دیگران
🔹
01:02:00 چگونگی جایگاه برزخی خودکشی‌کنندگان
🔹
قسمت بیست‌وچهارم (پرنده‌ طلایی)، فصل پنجم
🔹
#تجربه‌گر
: رضا معظمی گودرزی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/679241" target="_blank">📅 20:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679238">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkNO7yczzgPKQMBZBleecwed1XWYLuru5fG60sVflK7lBp5ZZsa1REc8lUFeY_AbGnUEjPkj2fPNz710jgjZvmwxZ9oz9crRszCqABSbW3zT_VTv7J9oEhlZrzl8nrJXS3uHEVDHubX092YPdempk65xDqCVn3z_vpRSfL9QhvUx8rfg99PGuRDS5Ocnh9bYBvJKFz3J9bJaFn15pTqg0QVE_3DUAangUoTobCbPWQJ1bu6xkeUBuM1psUdH7s7a72fm8YrFsopmXv4mBLp9NCi-PenVMlRl3uJh6jBSOe_r4WkkWwvxqK7qN-eZdgYS9cnUGAyvsmfMMjzEfo9oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز تازه ماندن میوه‌ها؛ مدت نگهداری هر کدام در یخچال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/679238" target="_blank">📅 20:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679237">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb0UzQhH2n3-7pQBztpa-oJuik7IQs4m_p48UWvGFJiN7SKsIPQkDQKlsGgnoov1s0svV1FU-8e4lba644TPJ42yCmKLfnii1HSU6imyX-c7K6E-CoVUqOOF90Brx0KltqObxRgYa5Yv5YT_hc3mAjAa6SkcRfVQKvlTQDLUkGkn84RFc5TU3ypZEvcRUvpSWodcZaAE1zUFo0mBw3Ko3asD0tF6dq36J5mJWcX7udfCi231JCDUb96PF90wFT_gZ7BtBIkS1LVVtdAOJzNMJGk23-9GXbQxPVVGokRJAD1Uraw6zwpMZb8YK3tHXg1MypmWXHn21xba2Mkc2zihag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/679237" target="_blank">📅 20:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679232">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
واکنش امام جمعه اردبیل به سخنان باقر خرازی  آیت‌الله سید حسن عاملی:
🔹
از دستگاه قضایی سوالی داریم شخصی خبر دروغ به رهبری بسته و دفتر رهبری با صراحت آن را انکار کرده است آیا این جرم است یا خیر؟ قطعاً جرم بسیار بزرگی است چون علاوه بر ضربه به جایگاه رهبری هزینه…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/679232" target="_blank">📅 19:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=vMIOrY3hf4Ru31-j7cKgSRom40co-7cRGShtPxpbt_Z6igCD5vW_iGpLSRTuc5KCSYjz2sqH0OHShK8IdQJcUIT2kBNUQ55LDPJuHie5fhvkDIxUrLgK900HBlNzO6h5hH4fyXAhB0RymTjXHNot1jULT7Z6EVToD3AOMWRJQ5tw673CgRprVEuGws2D_sSc2Comj49rpbIJ5_0IBkGzVavtvVMLTlZYmNngymSlxoPAJk_7gGz5L3Jlm02jP4cBOkwyoGMz8tnbrTRdkd_lMYh_J2d5etAK9-uQ28s-Ux-gCNRF2vm455RPMUHiCQ8Fb6CkJVgZCNJYRTGEFHvXRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=vMIOrY3hf4Ru31-j7cKgSRom40co-7cRGShtPxpbt_Z6igCD5vW_iGpLSRTuc5KCSYjz2sqH0OHShK8IdQJcUIT2kBNUQ55LDPJuHie5fhvkDIxUrLgK900HBlNzO6h5hH4fyXAhB0RymTjXHNot1jULT7Z6EVToD3AOMWRJQ5tw673CgRprVEuGws2D_sSc2Comj49rpbIJ5_0IBkGzVavtvVMLTlZYmNngymSlxoPAJk_7gGz5L3Jlm02jP4cBOkwyoGMz8tnbrTRdkd_lMYh_J2d5etAK9-uQ28s-Ux-gCNRF2vm455RPMUHiCQ8Fb6CkJVgZCNJYRTGEFHvXRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عطریانفر:
پوست قالیباف به اندازه‌ای کلفت است که خیلی نگران اهانت تندروها به او بابت مذاکره و توافق نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/679230" target="_blank">📅 19:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679229">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61965f8b55.mp4?token=k3T5ud3BpA_8CHS9hoPiHAWPSEoQocCJvjf0jSvC2JgWrLodwqy6gp0dQbFggI7xuSL6v7TnDcXVin62NVS0hn8BJRmbi1zWDmgpB4utWVnPa0z37ruHXBvFgA3VqMAkoIVG5utokWjHzuX_qwFUleMhwaw2awbodSVxencXoD_akDy_yXic1-MLCl6fLD_UMbsGwR2wiJN8muIox9ahMHn2jrHBz0ALPw6W94P3FgZkWa7YzSKIvWj0ug62iUELk1jPS12gt-SIuy0GejdRifa17WDcHpxCxH-XriQXGxPGsnt4tIsvJ_av2HN_xzLzG3AbOdcsPWk3LIRxqY_1A2kzTu7TdEUOB9HNZJPU6G_87xofJeZIs0iLoQ-ScH2biW_aDVC7azllgLfmMe19CvNk70wy0azEmCxCc-FrnrofVPVDOsZ62-0SIwOE8b60kiit1lkBkGlsswd3Q4O9SSYUSoUkKnNJ8UuYLKbawSQTrPKvLQY1nolj5h-bu4mg-xkKzaCjuESR6Qe0JXXibfUl5ovE3aPZNxP-CZKCh5yez_DNVjq2v-iTioBBREYAocl_lWgNGwLyfhWxt-SEyDa1QpiTHxEwlhniuA4IkPRkdoj36wiPm5_PxieuNHnmuveA5U6vB1aslUq_czJG6TX5Iepp5su16dQzY8Nreow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61965f8b55.mp4?token=k3T5ud3BpA_8CHS9hoPiHAWPSEoQocCJvjf0jSvC2JgWrLodwqy6gp0dQbFggI7xuSL6v7TnDcXVin62NVS0hn8BJRmbi1zWDmgpB4utWVnPa0z37ruHXBvFgA3VqMAkoIVG5utokWjHzuX_qwFUleMhwaw2awbodSVxencXoD_akDy_yXic1-MLCl6fLD_UMbsGwR2wiJN8muIox9ahMHn2jrHBz0ALPw6W94P3FgZkWa7YzSKIvWj0ug62iUELk1jPS12gt-SIuy0GejdRifa17WDcHpxCxH-XriQXGxPGsnt4tIsvJ_av2HN_xzLzG3AbOdcsPWk3LIRxqY_1A2kzTu7TdEUOB9HNZJPU6G_87xofJeZIs0iLoQ-ScH2biW_aDVC7azllgLfmMe19CvNk70wy0azEmCxCc-FrnrofVPVDOsZ62-0SIwOE8b60kiit1lkBkGlsswd3Q4O9SSYUSoUkKnNJ8UuYLKbawSQTrPKvLQY1nolj5h-bu4mg-xkKzaCjuESR6Qe0JXXibfUl5ovE3aPZNxP-CZKCh5yez_DNVjq2v-iTioBBREYAocl_lWgNGwLyfhWxt-SEyDa1QpiTHxEwlhniuA4IkPRkdoj36wiPm5_PxieuNHnmuveA5U6vB1aslUq_czJG6TX5Iepp5su16dQzY8Nreow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: تنگه هرمز هرگز مثل قبل نخواهد شد
اسکات بسنت:
🔹
ما از نظر اقتصادی ایران را خفه می‌کنیم؛ آنها تورم ۱۵۰ تا ۱۸۰ درصدی دارند و نمی‌توانند حقوق ارتش خود را پرداخت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/679229" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679228">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKj7McahBnKF_53uBU_8DkZbHLEJvrHqtgU4JKVtkABTkYyNnlpCgdixNKTN39EPd2LVhRgbRLFTe6bRjx9ewsjwZKKYO3vHs9tNXqZ1W_xY9ns6nuHUgqcdWCCFxeEsuPzVtDpykMdJzRESoYDCaZCLMmlW7NfB3RPNMvlusBj7qbugYpVkcZJL97BORd2PeRocS8RPCyHNwF1FzSbYXHCzfgvAgD_JhIcdJi0fe2BYIoiMN5bWSP0ZPDh-RLUVyH8uh0jMzqOQfZyJHkNGQeVk-a2v5I_a_MFs7QygTKNPa-GiZwqYoPTl86u7m6D5UZUqb0EWTfR3X3sBKHRoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین زمان تعویض لوازم مصرفی خودرو
🔸
بهترین زمان برای تعویض روغن موتور و فیلترها، هر ۵ هزار کیلومتر و برای فیلتر بنزین، هر ۱۰ هزار کیلومتر است.
🔸
لاستیک و لنت کاسه‌ای نیز بهتر است هر ۸۰ هزار کیلومتر تعویض شوند.
@amarfact</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/679228" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679227">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e930289fa5.mp4?token=oaGG89CvfE5Kx59u3o2vPHvmNBXpPAaIK10KrF70JG0BTdl4R2ujdev8rOMsx-yRfg-96tsXOrQWR73VIZQFAlOchyNd8fhp4FGWBFN6PDLC2vjz9PMCDi9ttt-mtocd6Lv0056-_dpxSypbqU8XeYRvqZJZKV4iRZfjreXxzuqGrajeTFnqAcY7mWMnyOjt92pVQHFnToDpzJgqxyEHgFY2mCy3LV-xs4Rpo9CMnEBjC6PnlHDdZTexF6WRetw6Ofw-Jg0s4tSIYpoPQlMdM-F0MCWEWBhzPQKFp-tRR906FNCSQ8QqnszS0jpQAYgMjAYrUPYSIePeCzRbZxMIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e930289fa5.mp4?token=oaGG89CvfE5Kx59u3o2vPHvmNBXpPAaIK10KrF70JG0BTdl4R2ujdev8rOMsx-yRfg-96tsXOrQWR73VIZQFAlOchyNd8fhp4FGWBFN6PDLC2vjz9PMCDi9ttt-mtocd6Lv0056-_dpxSypbqU8XeYRvqZJZKV4iRZfjreXxzuqGrajeTFnqAcY7mWMnyOjt92pVQHFnToDpzJgqxyEHgFY2mCy3LV-xs4Rpo9CMnEBjC6PnlHDdZTexF6WRetw6Ofw-Jg0s4tSIYpoPQlMdM-F0MCWEWBhzPQKFp-tRR906FNCSQ8QqnszS0jpQAYgMjAYrUPYSIePeCzRbZxMIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخت بائوباب؛ غول آفریقا با توانایی ذخیره حجم عظیمی از آب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/679227" target="_blank">📅 19:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679225">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJCULMDbM9HOjG-Ah98jYlzMTB4numXzSwAdD5mvLbssimGcfAQDdvyNqqwEHKtJd0cTcCrfolJCdiC5iXgq3OnbkUWZzFuE-1Zlie845tn4qdBW77l7BKxH7TBrFalF6sRIXQZajKsnShfEqUgFKp_dSbLJdwqqvWTKK2aE95sAU0snToUDvPbVi3i1P7YA0_AuIg1HdIKff3MHkwyXDSgTlx5nMVQ7Xl0FOd-U4EEdgB-VLcSurRrpICuZjXBuhiuBk1W3cBkXapYUTbC_7vAM2w-2ih4nkTxfrU56t4IkA-FTK5hgkAV4xNbJjLsX8t1HZAD5jIo4Yse77ZySUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/679225" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679220">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1zc-fDI_nz3XK-TF9DpQLgzkEMRBt5_lBndxjRJy98r32pZNhpoN27I3F6jOuZuAiFllLqbxvzU9uN0KHLZtJrgRCbIlM4agtXNQ-3QUeBZUMwZID_ss7k5S5_4mc84rXQKdo9dXQORrb5oO-cRLxl_aMHqTLtpzAa6EsZSBxKcDAEf7ChXBOFxFvmrPgCKeb6Fp84b0zvGnfY4WMMF41iBhW-bhbLF2zqlsWofy4wLiFiaEzxDotdQ48OHB-lj-CTNNschl9c9nb6q53makQEincXUcus76aFQXN-gPloJs4lfZq_UNyKr0ct_MCRzNWokRtNtbNwF_R9LyF6pBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ائتلاف نظامی عربستان - ترکیه - پاکستان/ یک مثلث شوم برای محاصره ایران؟
🔹
برداشت ها در رابطه با سند مکه متفاوت است. برخی معتقدند این ائتلاف، آن هم در زمان جنگ و درگیری ایران و آمریکا، به ضرر ایران تمام می شود. برخی دیگر آن را معلول و پیامد جنگ ۳۹ روزه می دانند و معتقدند این سند واکنشی است که اتفاقات جاری و وضعیت سوق الجیشی منطقه را وارد مرحله جدیدی می کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3236126</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/679220" target="_blank">📅 19:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آقایان مدعی! زخم تازه نسازید.../وحدت، سنگر این ملت است
🔹
کشور زخمی است؛ زخمی از سال‌هایی که بر شانه‌های این مردم، تحریم ناجونمردانه، گرانی، جنگ و هزار رنج دیگر سنگینی کرده است.
🔹
مردمی که هنوز ایستاده‌اند، نه از سر آسایش، بلکه از سر عشق به سرزمینی که خانه‌شان است. این مردم دیگر تاب زخم تازه ندارند.
🔹
اما گویا عده‌ای، رنج ملت را نه می‌بینند و نه می‌خواهند ببینند. آنان که هر صبح با کلماتشان بذر اختلاف می‌کارند و هر شب با شعله‌های تفرقه به خواب می‌روند، انگار از ویرانی وحدت این سرزمین ارتزاق می‌کنند.
برای آنان، آرامش مردم هیچ ارزشی ندارد، مهم آن است که آتش اختلاف خاموش نشود.
🔹
تریبون، امانت است، اما در دست اینان به سلاحی برای شکستن دل‌های یک ملت تبدیل شده است.
🔹
هر جمله‌ای که می‌گویند، خشت دیگری بر دیوار بی‌اعتمادی می‌گذارد و هر فریادی که می‌کشند، زخمی تازه بر پیکر جامعه می‌نشاند.
🔹
کسانی که خود را منتسب معرفی می‌کنند، اما حاصل حضورشان چیزی جز آلودن فضای عمومی به تعفن تفرقه نیست.
🔹
تریبون‌هایی که باید مأمن عقلانیت و همدلی باشند، به دست آنان به کارخانه تولید نفرت، بدبینی و شکاف تبدیل شده است.
🔹
آنان با افتخار از رفاقت‌های دیرینه سخن می‌گویند، اما در عمل، هر جمله و هر رفتارشان خلاف منش رفیق است و خنجری است بر پیکر وحدت ملی.
🔹
آنهایی که فتوا می‌دهند و دعوت به لشگر کشی می‌کنند گویی تمام همّ و غمشان آن است که مردم را در برابر یکدیگر قرار دهند و از دل التهاب و اختلاف، برای خود اعتباری دست‌وپا کنند.
🔹
اگر این افراد احمق نباشند، قطعا یا جاسوسند و یا خائن که در هر سه صورت باید نهادهای امنیتی و قضایی کشور به مقابله با آنان بپردازند.
#سرمقاله
@TV_Fori</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/679215" target="_blank">📅 18:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5c7b282f.mp4?token=IKVKDSWtz3TgjRfBvy92TfkSekpozCNN_TzQmF4U9lTrOEjQonaEwS17YTYYyJibAwHvA2Ab4iOxslbQdmLZ9865pG0SYfQQ8-DqLR7ipPDgTbPmm5lpHdg2AOIKk6cwlCxdF7sMSSKRvnKuNZjzornY1BZq_Il-7bzIIG7QftqQqCnkNRvOYZ1zDHxWJIMNad0J2B1gIX1fXa4FRwFNDr-i2e3WymefB2eGbgBlA5MeNUTIWGkVes6dmHChWiMLQdlMjf9oZDNJi72gUJpnSHe2_miC8JcQizgEqEQ7syeXW1WLjDDJbOPhVhQUQkT1dxHmNNoeQtm3ZB5HGlXUZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5c7b282f.mp4?token=IKVKDSWtz3TgjRfBvy92TfkSekpozCNN_TzQmF4U9lTrOEjQonaEwS17YTYYyJibAwHvA2Ab4iOxslbQdmLZ9865pG0SYfQQ8-DqLR7ipPDgTbPmm5lpHdg2AOIKk6cwlCxdF7sMSSKRvnKuNZjzornY1BZq_Il-7bzIIG7QftqQqCnkNRvOYZ1zDHxWJIMNad0J2B1gIX1fXa4FRwFNDr-i2e3WymefB2eGbgBlA5MeNUTIWGkVes6dmHChWiMLQdlMjf9oZDNJi72gUJpnSHe2_miC8JcQizgEqEQ7syeXW1WLjDDJbOPhVhQUQkT1dxHmNNoeQtm3ZB5HGlXUZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دستور انتشار اسناد موجودات فضایی را صادر کرد
🔹
در پی اظهارات جنجالی اخیر باراک اوباما درباره وجود موجودات فضایی، دونالد ترامپ به نهادهای فدرال دستور داده روند شناسایی و انتشار اسناد دولتی مرتبط با یوفوها و حیات فرازمینی را آغاز کنند.
🔹
ترامپ در این…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/679214" target="_blank">📅 18:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb3d1485e.mp4?token=teu-kxp9CJNkzwJrSpgdIaxH6KYS4yptzB8dhsVAGMnj9GY6kAKKojnbAfFhPZGo6w5lsZWU4w1y_IKq91XJvQmE8a4Zn0MJK4VLfISkO9YSUG85Ic0ctdCrY-bZZMytmjU4xvA8LLyma3V3tkc-U20RCU39YJ2XXX1_m5fNbFoYj1o2qEgGQLTln43gn3WvQpNGkk1B4SDTClhDegVuZJs8TZ_HLIm3klQObI21WYRxxKOrGzyfDuZllTN7iFvN-mDIyxtABH3Cij8CC1KcozWP5fjmu9rej-n_xULitGWQb70QEuM-SOpaiMJmJBLShxm9BZ-ln-7n8YiSONmu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb3d1485e.mp4?token=teu-kxp9CJNkzwJrSpgdIaxH6KYS4yptzB8dhsVAGMnj9GY6kAKKojnbAfFhPZGo6w5lsZWU4w1y_IKq91XJvQmE8a4Zn0MJK4VLfISkO9YSUG85Ic0ctdCrY-bZZMytmjU4xvA8LLyma3V3tkc-U20RCU39YJ2XXX1_m5fNbFoYj1o2qEgGQLTln43gn3WvQpNGkk1B4SDTClhDegVuZJs8TZ_HLIm3klQObI21WYRxxKOrGzyfDuZllTN7iFvN-mDIyxtABH3Cij8CC1KcozWP5fjmu9rej-n_xULitGWQb70QEuM-SOpaiMJmJBLShxm9BZ-ln-7n8YiSONmu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قنات نبادان؛ منبع حیات سرو کهنسال ابرکوه
🔹
قنات نبادان در شهرستان ابرکوه یزد، منبع اصلی تأمین آب سرو کهنسال ابرکوه است.
#ایران_زیبا
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/679213" target="_blank">📅 18:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daff06e5cf.mp4?token=FnZQpc01PNGt1msfptBFeJRdmiCZcKiNFj-nxRuby0C4z-3V5IV6_-tSn7iPlCEa1bM9i8-PJjdppMwyk06ZgffKd0NDx7DH6XTklXDEz4psWKy1ryT7JK4KLBdZwEVkwB3xvFzXoFRYuFi9wlP24c2PIIUxmFPoBgo6XueSXILYyVuOldka1Y2gpRXNoIheu9M94Mpm6s39HSKJQvvsViBAbb-KcyBLUFgJCai5W3885Ej3jcnirNCjWOyWpM4JOUZESjhRf-kKsMHY3rgvt-i1_vYnHlPVOy9tt2AgeW9MELPvKJ9pHqkLM5Hu1ZwuaXe2XIAJ31iRPczcpnOFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daff06e5cf.mp4?token=FnZQpc01PNGt1msfptBFeJRdmiCZcKiNFj-nxRuby0C4z-3V5IV6_-tSn7iPlCEa1bM9i8-PJjdppMwyk06ZgffKd0NDx7DH6XTklXDEz4psWKy1ryT7JK4KLBdZwEVkwB3xvFzXoFRYuFi9wlP24c2PIIUxmFPoBgo6XueSXILYyVuOldka1Y2gpRXNoIheu9M94Mpm6s39HSKJQvvsViBAbb-KcyBLUFgJCai5W3885Ej3jcnirNCjWOyWpM4JOUZESjhRf-kKsMHY3rgvt-i1_vYnHlPVOy9tt2AgeW9MELPvKJ9pHqkLM5Hu1ZwuaXe2XIAJ31iRPczcpnOFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚿
✨
سردوش ماساژور و تقویت‌کننده فشار آب
رفع افت فشار
💧
⬆️
+ پخش متوازن آب با چند حالت
🔄
بدون نیاز به برق/باتری
🔋
❌
🧼
دارای فیلتر تصفیه + کارتریج جذب رسوبات
🎚
کلید تغییر حالت سریع + اهرم تنظیم آب
💆‍♂️
ماساژور مکانیکی و بازوهای ژله‌ای
🔧
قابل نصب روی دوش/شیر/وان
🚿
🚰
🛁
🧱
بدنه ABS |
📏
۲۵×۶×۳.۸
🔴
قیمت 1,098,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/58323/180124/</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/679212" target="_blank">📅 18:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آمریکا ۴۳ روز تا مرگ نفتی فاصله دارد
🔹
بر اساس داده‌های بانک سرمایه‌گذاری آمریکا، ذخیره راهبردی نفت این کشور به کمترین میزان از سال ۱۹۸۳ رسیده و اکنون تنها معادل ۴۳ روز مصرف نفت خام آمریکا است؛ در صورت نرسیدن نفت جدید، این کشور با کمبود مواجه خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/679211" target="_blank">📅 18:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی: با ناقضان وحدت مبارزه کنید
🔹
حضرت امیر یک بیان نورانی دارد که بالاخره ما جامعه را متحد کردیم، و تمام کوشش دشمن این است که این جامعه را ارباً اربا بکند. شما مواظب باشید این جامعه متحد، مختلف نشود، پراکنده نشود.
🔹
اگر کسی خدای ناکرده عالماً…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/679210" target="_blank">📅 18:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15425cb351.mp4?token=NE9-IbPLWu6YHa0viG3hXuGetgIxGQAQJ-vHDstvXlrXtRFYBs-En_mC_t0V91-LH9CTgJjWFgyFNE0WQ2uHvR_B4wWSdrkDHGaOCeYfkTaKSTXbYR0_zZW9Fc02i5n3kFMPNcRFRe6StZS54p-wo_33Iq1C98LBBTb8aa7oe5L3sKEGxGUV4Vo6drFWzsTSr1HTvEE7pW4HhFPFTjjZR_gniMC5ECoRJ7sy2tVP2LAJonfcL8MFTp13htsOf_BNv3Ha_sLC0VINhOSukRqcvpjV8WAlrTM3QnAcmvJVfWvBn9VGfMrbspMwWI0gn_DVnTN-qrzjqBGRqP2VaOoIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15425cb351.mp4?token=NE9-IbPLWu6YHa0viG3hXuGetgIxGQAQJ-vHDstvXlrXtRFYBs-En_mC_t0V91-LH9CTgJjWFgyFNE0WQ2uHvR_B4wWSdrkDHGaOCeYfkTaKSTXbYR0_zZW9Fc02i5n3kFMPNcRFRe6StZS54p-wo_33Iq1C98LBBTb8aa7oe5L3sKEGxGUV4Vo6drFWzsTSr1HTvEE7pW4HhFPFTjjZR_gniMC5ECoRJ7sy2tVP2LAJonfcL8MFTp13htsOf_BNv3Ha_sLC0VINhOSukRqcvpjV8WAlrTM3QnAcmvJVfWvBn9VGfMrbspMwWI0gn_DVnTN-qrzjqBGRqP2VaOoIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار، سوئیس را تهدید کرد
🔹
ترامپ تهدید کرد با محدودکردن واردات کالاهای سوئیسی، می‌تواند اقتصاد این کشور را با مشکل جدی مواجه کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/679209" target="_blank">📅 18:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679206">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/679206" target="_blank">📅 17:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679205">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عضو کمیسیون صنایع و معادن مجلس: در وزارت نفت «رهاشدگی» و فقدان پاسخگویی احساس می‌شود/ فروشنده نفت وزیر است و تراستی‌هایی که پول به حساب آنها می‌رود، باید توسط فروشنده رصد شوند
🔹
علی‌اکبر رنجبرزاده، عضو کمیسیون صنایع و معادن مجلس، با انتقاد از ابهامات موجود درباره بازگشت پول حاصل از فروش نفت توسط تراستی‌ها می‌گوید اگر در وزارت نفت «رهاشدگی» و فقدان پاسخگویی احساس شود، استیضاح وزیر نیز در دستور کار نمایندگان قرار خواهد گرفت.
🔹
علی‌اکبر رنجبرزاده در ارزیابی عملکرد وزیر نفت درباره فروش نفت و بازگشت منابع حاصل از آن گفت: «موضوع فروش نفت و بازگشت منابع حاصل از فروش آن به داخل کشور، همچنین مسئله خالی‌فروشی که گاهی از قبل انجام شده بود و عدم بازگشت پول تراستی‌ها به داخل، از جمله موضوعاتی است که مورد توجه نمایندگان مجلس قرار گرفته است. وزیر نفت خودشان را مبرا می‌دانستند و تقصیری را متوجه خود و مجموعه‌شان نمی‌دانستند؛ در حالی که فروشنده نفت آقای وزیر است و تراستی‌هایی که پول به حساب آنها می‌رود، باید توسط فروشنده رصد شوند تا زمانی که منابع به خزانه بازگردد.»
🔹
رنجبرزاده در پاسخ به سؤال رویداد۲۴ درباره احتمال استیضاح وزیر نفت گفت: «هر زمان احساس کنیم در دستگاهی رهاشدگی وجود دارد و پاسخگویی به حداقل یا حتی به صفر رسیده است، استیضاح جزو وظایف نمایندگان است و انجام خواهد شد.»/ رویداد ۲۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/679205" target="_blank">📅 17:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679204">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق، شامل آتش‌بس ۳۰ تا ۶۰ روزه، خواهیم بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/679204" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679203">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571d5e5bb9.mp4?token=DLcH2tBL-rECQfF5GJ_b1OEnb4UbcYNlWTA-X-9Vk5K-Oh9gzyKbX02K0FHzdTJPRsVkotmhy0Y0n2H1GkuBVJYspd_GrkTb5__S7ChKrbX-AMQUQ51pUjyzN_PyvjoE7vA-tZCCDva9FG1sWADE_u62JEVEsvKQj858JmoYn3QnTZOAPPcvoWBuhDwfvuKv4Y-jxP7TBGSNl7IjolS7HyN0gyPMRVLPAhdoUdja2snzMwIFTtKYp_ChGd34tyWqq7LGhO6aiLaxnX77pM10a4L_fkk9UVeIXDGa-TA7fNuxx-KgUokdniJ16vPC0b4-jgq5YlpNgokOwz0erNi9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571d5e5bb9.mp4?token=DLcH2tBL-rECQfF5GJ_b1OEnb4UbcYNlWTA-X-9Vk5K-Oh9gzyKbX02K0FHzdTJPRsVkotmhy0Y0n2H1GkuBVJYspd_GrkTb5__S7ChKrbX-AMQUQ51pUjyzN_PyvjoE7vA-tZCCDva9FG1sWADE_u62JEVEsvKQj858JmoYn3QnTZOAPPcvoWBuhDwfvuKv4Y-jxP7TBGSNl7IjolS7HyN0gyPMRVLPAhdoUdja2snzMwIFTtKYp_ChGd34tyWqq7LGhO6aiLaxnX77pM10a4L_fkk9UVeIXDGa-TA7fNuxx-KgUokdniJ16vPC0b4-jgq5YlpNgokOwz0erNi9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش ساده مساحت مثلث
🔹
توضیح محاسبه مساحت مثلث با کمک مساحت مستطیل؛ روشی ساده برای درک بهتر این مفهوم توسط دانش‌آموزان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/679203" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/679200" target="_blank">📅 17:10 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
