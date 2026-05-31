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
<img src="https://cdn4.telesco.pe/file/Y-xPyG9rqL-hC0ltMCK3SbjmOcov35wdwwLIGE56FNxTCMFRxit_kNmZQ9-u5Ht2NEIys3Sk1mSUf-vDwkJJjxky031IVgP-h2lI2kcgvdbuYRAmWrCa1JohOOlyhaRBRo6iZtoMkwCuKhzItLGA0qVho-mbSgbUNnfJrlw9_rCIx70YVBAl-JJGIrOIdvDEVdLi-COfKHMxYCaFsRAtCzKscN3RG5LL8p_0OgsCIkU5LUQOrMQ0JcX5ECnbu5bLzrjV7tuieXqg5vY84JkXGGpGcfKLWq5aGKYIsu6ZwftNiXjEmU9NpzjsKS2MBuq3nMJJHPpIRhKGeYqXmtSNrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 178K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 01:00:29</div>
<hr>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0u8p8nB0ASwGJdnD2_OSV0qIA3DHC4d6wqcqaWWkIuiE11CGVi4kPubFVpP2OuQx0oU3SMtsCZSDq9Ks1G1NlMzbbawCzVlnh1aWM3XxD4sgmOapjMXCxxOopJA-aaF-cWIluXruytNAQM9O-2y-llRhY5Rnyu_wqKLc4-pe7gwA2OeksmkRZZssEzOW8688x2b0IE782LqYZGU8I0lqELBbbXcYD3qN27mxR2rbwGuAbVp-enUv__I_nUEjJvfS2fr6B7-CrplT84c9AOCMtQFgiCSpXW4pjSWQs3i_BNUartFG_g6owPqFsj1LrD7oJln44Gx2O0wpR6aClOywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3EzfDPluca4AOX5zqi_tFcK2OFqBmdDtyOeBBXuaFciLwxOpgA5aOijvP2Aa8CyvE3CGdz0lyTLS5GekFPUrObvaZqNmIaLuHxMVRkAgvDPRxhB8lV_wEtg_Jceb0-On_lT3XjXNDTXolMsbWc9IMRI4UWWyZsyFupdjzQKECAyKRpNSVQwM8lAQOtzP3hhRPIEsoQhsjLV0uQRJsb2wRgYj1InFyTnsllzV631CJfwW0BSWBDRV30emZMS8iuqsBDKqPQbMOGkkrbapzb10xY-6dRxoGgajsMS3n0YdjZdK168Y0scBTQp6GWEm72a0bO8LDmeL3q9GHvUeAl1sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9kH829V85T7pt2n1r8H8fPW3JQ04IfWP3pztu-yMgHjOm2f4UU7SgVYJPeeQOyVCdX74b9-9kInFeRDFeFdBBJf0U2_FHHXP02xUHPwBwm9puokT-lwmxreLavtBa6rB7hwQJPVw6AF-7mNsmsxb4kuPW0tadT8f9NcbvHzCqbZYdDlBs4pBTBUiGZaq-N_-pH-7vsLad8wGzZK7Y4qSGD-O-uK9pP3eRuRYkxXMVyU3iYLRo21TvlQpvfIOBY9TbGnQrEHtAI1ZDmRLoxp7i83i6gDuj_OLMObGoltayztrIsSY0zG3pIoMC7FQ3ZsCUKBYK8gPmVBJ8pxUtc3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درحالیکه اخیرا رسانه‌ها خبر از مذاکرات باشگاه استقلال با محمدخلیفه گلرآلومینیوم دادند اما اعلام کردیم خلیفه‌ازتراکتور آفر دریافت کرده نه استقلال؛ حالا امشب‌هم علی تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال نیز اعلام کرده که هیییچ گونه صحبتی با او و باشگاه آلومینیوم…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/22578" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=XRRq9wJMFi44EkkBeNoAK4IaHaqBoOWzlcd-f38jiKo-F-g6RGpvHSzCzaYT3PUrWCJUofovoucI7aEYAOQho0IXX3hkv3g9Lu5cGHixnVGSX4VplOsk9bY9oxQ_tLjXYPVWmoVVjH7xjljUwi_ckd74GfxQ9H1nBMJhE_rVbM1sZrys_S7d3LCNHtYriWzP1xchjk6Xhl1vyLxaeg3dVv2M8WogAluGWBXfvNEyKeGa8H3YzXEW8Pc8fKqwg-JKeNNpFPbc6FePEAZNBuxwIyuUUdBloVvmJDSbyy8sHA9TwoIzkVZXAcxR5n5spalu_0eh7ZK9nXSeWT-YmYhmIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909763a6a9.mp4?token=XRRq9wJMFi44EkkBeNoAK4IaHaqBoOWzlcd-f38jiKo-F-g6RGpvHSzCzaYT3PUrWCJUofovoucI7aEYAOQho0IXX3hkv3g9Lu5cGHixnVGSX4VplOsk9bY9oxQ_tLjXYPVWmoVVjH7xjljUwi_ckd74GfxQ9H1nBMJhE_rVbM1sZrys_S7d3LCNHtYriWzP1xchjk6Xhl1vyLxaeg3dVv2M8WogAluGWBXfvNEyKeGa8H3YzXEW8Pc8fKqwg-JKeNNpFPbc6FePEAZNBuxwIyuUUdBloVvmJDSbyy8sHA9TwoIzkVZXAcxR5n5spalu_0eh7ZK9nXSeWT-YmYhmIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاری سن ژرمن انریکه کاری کرده که دیگه تیم ها برای قرار گرفتن در بین 8 تیم برتر اونقدر تقلا نکنن؛ جالبه که از این 8 تیم 6 تیم رو امسال برده، مقابل سیتی بازی نکرده و فقط مقابل اسپورتینگ باخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/22577" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22576">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFcAJ2FJBydCQP-51rh1HWyF_TzA8z6pKcy258CvQZNnxaGQu_IFE5h0p2EOjQi7gp50Rddx_f3x9CfwEeMsytfJp6_NDeHPLEP2dyB-KRhJ3PxPvDMk-JNCbM72j4H6aTiuOBy0k3H_WKZfXvF8eMDWLp98tmYCJyX8-BBSJuo3Tx39ZvuKv3_Sfx9GVqZv4cwDlRuL8xX5MOPJ4H3TLSkii8Tb7TXhpPaMsGLbB0S0t2g-BG1eGe1rHS_WXffgjowTQI57XvM02DYuZkv_ldURiyWtvFlRSmN7fbluz2Ab1j3eteJ-CMboiFXPD7YpHL7hQnOtpA9uhPPBAlr2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت‌مستقیم وسریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a10
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/22576" target="_blank">📅 00:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYpcNptPHWbLUajd2z0hIuMaAsxwh6eQ0B8h8EIS4TmEjEQENxqVIqRNYghIbhIiEFKX_6U-1cAUHRrvTL-G3Tygi_fxw4Ox_x6hJHMtRF0jlfVySCJgOHOebYo3CuljCC622HmYTvly0-J0okhrfXVcIKkh6VQxY8ne2hzXOlZdn10bBfphywawg4zu09oJz9KXGk-2OsYlEbmQvFmEWi4K0gbLNNfhRx10qw29jmKywVCpBmnFnklGfkYAOBlUtWEPm13G9DJeyBm4dX-st8FxBA8mmNeH--aaNS9O6VvTOoE9xseDy9WYCUqxsg1TYYa-y0on3Yl1YYN9CMeR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22575" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfN16u-jI8ikx4fmYEpGA_sBC10JBP36dNQZGmsCCcM3DmYQC48dvGlScrZTVfrS32LP7_V_uf0Ix8L1ThqgXNyNhIlZoaCqpf30s-YADra9Sm6JmoCjAw07rQcJv75JXJF3Nda-ZXvP8rfAa8hdsgd8JUtXf-4unc8U-TiEp8zya9cwHzqVrYgpumxYKXJkihmTohpi6_VHpNgD2HghSIsN-n3Jz7DgcD9AsAol94LJlNJvtzzolthh1F0Hf-_wl7qKPZqwSswRFWPzqnJyq1Pg8aa2CSyxI4gSn_fz-6XOog-J_rp80jxP8sBc_LXINTQ4rbFkXoEndCPLcL-CRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22574" target="_blank">📅 23:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpwaV265nzEhpibO5EbkbrP8ifELAlGIEW7vwF5kEsje0ZPmuYNfVPeta55-5knlMGV432my9h1v132o89I9_7Eq10kglowlQ0teCj6-XLy4gro7J_J2hiRtNF5RtAcdkldRgFJSNYFkZ-ktsZY_-W7txXcYXLqnPm85LETeFzT_ufDH2om3gLKJgc0icVuKNltFsrydhuJL_e-4Miz8DmJRNbT54B3gYz7wNDaS7kvp772FkXp6zRXCMMA4WGoGnCXGOOD46cygdM3k3E4UbxSEmLPA3DfNjbF0qEp-7osw4aREXULS8f2IvmZwe0jGDrJsEPqPdQGnBhamuHxM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22573" target="_blank">📅 23:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=cmi0NFfJGkEbUHje0Yg5f6cTOSILQFXRPnMqh1KHkekUPchrpXZMq6nCqugi6JTW8oasElZ9caY3x_prR_WwGwpM752PyfeciLJqTy49_hv2hGr7Zfzzp2kjhEXTnQ0KAD_s3f157QMBf-McnNkGDH5OS3EBPtEy_emMCUoqKKN28-NpS-s7RYHR0mxIdSxOAHAj3ZYmCiGG6vb9XD9KljwCuk95367Ir7NhGOtPIrL-DWNn9_w58hZP8jUY_CdgMBh8z7-6g7MCtqctGtQFmfc-eb8JrUKeJGk1UE2UOXlHe59ZETCOFw2XjHnc7nLDkfjtus6DgDys0u5nncLLGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f2e6ecbb.mp4?token=cmi0NFfJGkEbUHje0Yg5f6cTOSILQFXRPnMqh1KHkekUPchrpXZMq6nCqugi6JTW8oasElZ9caY3x_prR_WwGwpM752PyfeciLJqTy49_hv2hGr7Zfzzp2kjhEXTnQ0KAD_s3f157QMBf-McnNkGDH5OS3EBPtEy_emMCUoqKKN28-NpS-s7RYHR0mxIdSxOAHAj3ZYmCiGG6vb9XD9KljwCuk95367Ir7NhGOtPIrL-DWNn9_w58hZP8jUY_CdgMBh8z7-6g7MCtqctGtQFmfc-eb8JrUKeJGk1UE2UOXlHe59ZETCOFw2XjHnc7nLDkfjtus6DgDys0u5nncLLGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
یه فلش بک بزنیم به زمانی که لالیگا اسپانیا برای رئال‌ مادرید و بارسلونا درواقع یه فارمرلیگ بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22572" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNpPXuLUbfZlLy7X3al3zMl6tddPAbqBJkmlAlT-2SBl-cRkcW3FlkHutIdRmZi5onslfYsw2cq7blGgrj9IP09AVRBkVRQaPJ6jQeIH6A9Tm6zvFM4n6X-P2MlUt3qAcOKTdr0Po_yO4PWRnDXIy4AJFG4oB2JX-gIVW74v0ygWRnN_0nFnD3ITSnnVLBDVONBTJ4cvfOgdRoQwogh4C4waQiJ_1a4bimWcQjih2Pfz26CBUF-PKrko2ls-iUTh6lJq3Q2Nfq5EzDIr3QaonFYKLjnm3T0RseHp3YjRwnNshHvb4u3mNy3koE36zp6VPIfgQqcHaUD_QOcNwYiwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابراهیم کوناته‌مدافع‌فرانسوی‌لیورپول قراردادش رو با این باشگاه تمدید نکرد و رسما از جمع لک لک‌ها جدا شد. کوناته هم اکنون بازیکن آزاد بشمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/22571" target="_blank">📅 23:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7N4yts73V3RMAzNufduT82myXUF8klB7HdzYvLY1W_eefLJBFXTcD2api5IgbDed4RVH1FybV20pUDtoQVhKfGu-sXsLwNsJdl7J6FJjjQDH50gLjzK7__KoXrlTsnu0pTYJVL3ZPGGWaa3BzKlDs_49Zid3YSX-oG-o3Y_deqU5-ROzXKCCHPnoBjGMgplaVuGFGd7RQOLRqO1iZ6KQwmNC_y-CDgHQlY3gmAcf8_YTen_CYJhoqNToxt1odOI4-K2xVVy5XnDk7tmKmEtdyCEaXfHu0ab32PlE3sErZkoRUByQIoOxon3eR0AI9qgK_jJioyBUibgIP52PfcBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ایجنت نونو مندس مدافع‌چپ پرتعالی PSG در تلاشه که درتابستان پیش رو این بازیکن رو راهی رئال مادرید کنه. مندس اعلام کرده درصورت جدایی ازPSGتنهاحاضره راهی رئال مادرید بشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22570" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3xToXfdCK5KFJLhFAbE09DMSuncsjdwghR5FupsOTqE4zlTZQgHEpgoMaRkCGZ1vH_1Zz76Qbl7ajBNU_E_5ixFa6l5Cf8-DS3YvoLr2V2SMbv0pTrNmaOGF3QZDmD0UqZGh9YroNsr3vEFOlBt7Icopv30QmJYTJiWyV2locnw3bjEwNpswlELCQspcxLiyoltUDgaCs-p6SPn8GF7CO1dsBy09s8ePykr94lpXChjpm0yjcyG1ZaESc33wE7qVPSLB0Zlbv6U4eAdPGm49XMS9ny1D5b9LJB_HVDSOpwVClH7c1jCoQ9jTkJ_3pRAK4W2aXoRhXy6NT49RyTGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTQD5MEuhdlZ8bOsEq32ANEJMglUVq1-X2cEm8-qni_ulAXi11L7ZlD5lAczsp0YrxghbLIF2yJyt1CPzDe1-QPLQ9Ztiz0-Mm1EB25e5nB2Af6FsB-YCFJLi3M5DlVmDFtVnIO-jDxSACPIC4HJgtJ1INPRHdUGzxT3iiZ4hvsfxVbk2DDvxf8AMIfN6GnkkRex9_-K4_X05dULaMxn7ldrjtcJcyz90B97PLXVnP6pLRPG_ufsHho8PurXeE9MgGcYn6l0W9n5m_oAf0nEeD2RUUibFUw9QQ-9Kf3Vk2rsSan3ncsyd3XHuoVbex-RHxj3m1soP9xvxTY-jQVsBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛ گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22568" target="_blank">📅 22:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba2bczBVFBkC-TZvYVz4hCCG1SWL11hetmmj4gzUNukVOO-Qd2B6TtJwf6Elm43F_VzCEZe_QnBMJmZF3a-9juDaoCn1dA9AMrILMancfne3jwJPkWdlFnxeBuo6Kb_EcUNXKFN1f8aP0nR9TRVvy7rU98asdLgw3TrSb0gRVA5H7eUHk212awkdPIFSUty7CS90ymubhytrEhoAPwFRNgQmJQv0-21jc0WqOvdH8PyHBmRZ6LPuvD_S7CPWYpnLbtvG_z_L0OMlApXaoS2SIzOnIFwn6QZD3jstiVoXXO0fr5Oh7h0i65xbIgOK9s1_u0Pnb8J1RDXaD0j5XRrbrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|فرناندو پولو خبرنگار موندو: خولیان آلوارز بزودی‌قراردادش رو با باشگاه بارسلونا امضا خواهدکرد. ایجنت آلوارز به باشگاه‌های آرسنال و چلسی اعلام‌کرده‌است که ستاره آرژانتینی اتلتیکو مادرید با آبی اناری به توافق کامل رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22567" target="_blank">📅 22:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3mrONUUofdlMCyp365TEzLjcuEHel4UBAhsKINZYphE8hIJ2csjCoy4jyCzsT_wtT9Rua6xBdDOjInFyl9cE7hyF63w_BCtpsRAhLAUJpDX32OB9YQuI5V7LyMWJIz6FJ8EfgM6IAzUuTC02l8CIIhodS6D6u6M5gzbnSaGuDNzHOo0NMVGJDy0LBX_UiIbGO2GDCrg4knyusp17t2uXgpLmcZe2spu0saeLau0njcRNbrFJ9ybwb3-bSrcC_6_XihfPFQvfHMdtuFhZCirHrfbfQIfsm05oBoBSRfJKQ6O5ZmLQqyu39ucEfkhEFHeFsp4KVqQi_uQnMiLjrcp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 20 روز پیش پرشیانا
🎙
رئیس‌سازمان‌لیگ: به این نتیجه‌رسیدیم که امکان برگزاری ادامه رقابت های این فصل لیگ برتر مقدور نمیباشد و براساس جدول فعلی سه تیم اول رو به رقابت‌های آسیایی فصل اینده معرفی کردیم.
‼️
همچنین درصورتی که سنگ اندازی نشود بعد…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22566" target="_blank">📅 22:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkzRfdNYcxB58oqGamzCH-1IQ5tVzP2l9gClvGyoRYNp4yVeGABUseYCrDRPG5-Ptwb9xttWVnlhdM8j-YpoA6qmtJI53aQ30YBhf-QlbydJ6Vd4Ie-Uo3wYriXT76q4NzTZ_xfvI_9bqNuPtqESZM_IfKFXmZY1EQYHsoxJV_kOIQ7VMYkeXP2Ymtt9-YvZJTvIcMcRWnyyl766zx4Vfgqa_MtsF98YmJtia7dvD7Xji0JcpQ5gTOfCQL26f9nwKibkGkTMcEZMRNi8ZHx7-dNg0JBMrhaLRHhaZKnhhokxgxKHxC2itkFyLiS2s-09bO13Tc5tJp7Fbiyo5nSxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxpjTHT3O_tL26xv0s5UMhH11s6WshrW7xYoDgtQm9yndkTkZjkxc_p3UeFsALjQaCCV7rJtXDy9PGfvl0iKdLzsXj2Iexuh8AIIg5AveltGkd-FHfDpppUTspp7zgm2U2Do5DUnO3E213JcWkHg6csYBEp1-hH5jv8bww1pVZAbiGHluvzCTCqexZdmTgP3gFMTlU1w2D_u9C6FR0wKG7UqNRNZci-vT8ktMAJP6wcap_ei6xMYfxzGZsmqhXeNN5iAszvRq-g7L8sCi6NryegyOFGrGLfhbKkY4picLPa_WD8fkwKt3eId7P0lmN07Ea7Nzbu7MK3nnUClfqqxfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خبرنگار معروف ترکیه‌ای:
رویایم قهرمانی پرتعال با کریس رونالدو در جام جهانی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/22564" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=HNi029BPcVND0Cx9H5bC0iyICut0Ut32JOB9A_GTccGXhwaZfCs9nkdytvfM8kM9ZJSilKH5J8I_8FoWDmasfXL7nEUlfDU7JA9t2NmjX4GlFtfu-O-7M8CPMgbLyQU7I0umS0_pfu_uxCygRsCV4xm0CJXr3l0CJcHeCdDDhtBsYUa4vICeEtRJB4Rq5vA7OfpfWN-X88cugor8LplbBpp6u6jdsu3Gz25TOGFUjcqXbMm-_dD-qldqd1fkI1-5drCZV5ra0YrAQwD4qpc9SuFjSS2V5AXgBMZ2QkHFudN2M_2WY3bGyzueP4AVWHsucWsI31AWab6soHEHp6asZGuO_-iK2lysfyvnLZZUsG8wkhATAfml_sZDdHoeEJAimUWitZyEaBTOFPL6jhu4ZSZSaNb_Q5d3nWE4AxrcLSXhag-xzZwEzJaLorS54wMLt1FkMg2ESXZT74RXO4H8YXY7k0FbjlzDEGPX-qOHoCnc63IIdt7UU2IzA21rh54gPd-hFPYVhtVBvqJ8-jNQfo7DL_BQdeAgTV1gk7ywX_BVvmZNiQGwcWvMcgiTgYPM6Olf7UilpgyRHQrmApLhHQ8Ka39tOYvaCRqzqSbPZADb7fgUfZg_S3nkjSXPQuVI3qVYgWO5QNSIPcGURziW6SzJChWJr967AMygMRVulnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=HNi029BPcVND0Cx9H5bC0iyICut0Ut32JOB9A_GTccGXhwaZfCs9nkdytvfM8kM9ZJSilKH5J8I_8FoWDmasfXL7nEUlfDU7JA9t2NmjX4GlFtfu-O-7M8CPMgbLyQU7I0umS0_pfu_uxCygRsCV4xm0CJXr3l0CJcHeCdDDhtBsYUa4vICeEtRJB4Rq5vA7OfpfWN-X88cugor8LplbBpp6u6jdsu3Gz25TOGFUjcqXbMm-_dD-qldqd1fkI1-5drCZV5ra0YrAQwD4qpc9SuFjSS2V5AXgBMZ2QkHFudN2M_2WY3bGyzueP4AVWHsucWsI31AWab6soHEHp6asZGuO_-iK2lysfyvnLZZUsG8wkhATAfml_sZDdHoeEJAimUWitZyEaBTOFPL6jhu4ZSZSaNb_Q5d3nWE4AxrcLSXhag-xzZwEzJaLorS54wMLt1FkMg2ESXZT74RXO4H8YXY7k0FbjlzDEGPX-qOHoCnc63IIdt7UU2IzA21rh54gPd-hFPYVhtVBvqJ8-jNQfo7DL_BQdeAgTV1gk7ywX_BVvmZNiQGwcWvMcgiTgYPM6Olf7UilpgyRHQrmApLhHQ8Ka39tOYvaCRqzqSbPZADb7fgUfZg_S3nkjSXPQuVI3qVYgWO5QNSIPcGURziW6SzJChWJr967AMygMRVulnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفت قیچی‌ برگردون‌های برتر تاریخ رقابت های لیگ برتر انگلیس؛ عالی بودند از دست ندید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22563" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDp7NZiOicn283rqB4OFmtiTyr6yTlk3_Goa185JTXuNknZmBlxYDopxNL2sf3iNKB7sQewAzisddGLZyJv9FroCU-c6OUkiXx38285sJHmWTpHaAVjeaIaw0TID4EgSH609ql3aEAuimJMD_4Sefnwfs5OGXXg4fD89HYZctvODxsuWnBEbkW7-6IRuOzwpOyXzBXFdsUGtdv4pPe3bmObbwBleYYOl0xeJOGXd5qY6tsvDC7NXXer2rSnQZ5UsJGLZ6aqAdyjrATWpvREIEEXpi1OHf58oO49eseTJkgEu8klRjwS0hJ9EFhhkaf_W_bu2Z5PN3FLTDw4cIeQvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22562" target="_blank">📅 21:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktdc_AN2Qs5Ihu1CsZAmoEajPU4K7TQzwuEypLX9acMXTbF5_C9n9_3LJI6r6hRAH9gW-3lQ66aJIKQCDbKkEQXAWQp1vOquQjMtTvfw5xcvr-fCjKbGE4CBg0znAr92aEugQwkAOZUnHlXBplR8XlCB9RhYH7kKM_Toy4YSAdc0v-7Mft3MwvO-2AjfO-djDUlftqhZiharBKJ5-NjQ7y7y21GyLPE_Q10CRGP0QaU3nik4QpxuT_JfeKs7kTILBa8K_mg03cjUeNKlolwGkJH5ueyaU36qryRXgB8duToC_7GZw4WcEkndqFRYsddpvrNyjzbASg0tzvSvYIBy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ مدیران باشگاه پرسپولیس بامدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22561" target="_blank">📅 21:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tToZxiDvGwGEMtFGM3hrthWl6mD9piXWfQmeDZxHoDl23YS1V0nQY1smXINr5KwaHkcQLleAFi8Uqj94eag6zczRvRHJJBm3cLTmaVpf8-F3KsT-jWHvECLeL8EStz7bcpmPorMeG9TKwqc-CF15UtlU3vBg_6ItLxZn8tzOrzIEpgwRTfFxWcdVa9gYg9DkiWroEeDHEi6z_4tdLCyT6aL8WdtwrVAVVSgUxXrR0_q9tdOlztm4ws4THlMLZU2_vOxjIlreC0beU47IzYBVBiJ1FikunaPRln2ziIioUYzxkDnqWmB2uGX3JVt476xpTjQJjg_ktDsZtQSfpGoFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22560" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSlvyvnRd-DN_rhyV9Zs0EWUu-o59EUDEFxPwZFv-4__SOJki3ZQsGupitOIlDSLfvi32Qgv9xP81ukXFWQFrMbhEZKsgo_ww5rKPqsMPa5URAfjX0TYrxJOjLAhO8CT-iqrKLlpiSbeMsUSdC-mzxO7dr4WgsgV27U4YXyk5YlclArRnxttHg32qXzAiOaA4RXpALm6e1Vnn-tAk9tldHKNGFlQjQMYjH5EVzH1SIa7NACxbkWlxAH-K81TEQgnk4v18YwQ7x628WKckAWrzlkl_oNLTd9Vi6XXuRotMW5yJA8DH-mdcpP2-mC_wyFW5UM3VTEfLjH7s3URQ2h5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22559" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=d34cmd1hk-O-BOEjOTjXxYPhI6mLN29sCVT5vqbC6d750isSVHbtkfNUB_x2lmvvERgcUl7i3D0kXGR4y670Y0UC6aDFtsyl1V8Ietz6wwBwSD3WrtRBZuZYFy72_8mrpzXzdeVhYuFDHAqVMU0-SN6odCMIN-O0gWf9woAQ0SJ9TKI_piVMayYDCehDaVbMod0GPKjgEwsaaEcyu2d_uF5mELUQbAIdmFxmc1fYPIAAYUPKL6M7Zb4kVO3syU3FAQlvEAjem7VuVNrA0bhRNmqqusuGUBVcX2EGObWA-6Zg05RLpEdsoAmW_1EsyFVXf5jnaBCyXk5_HB5b51EQ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=d34cmd1hk-O-BOEjOTjXxYPhI6mLN29sCVT5vqbC6d750isSVHbtkfNUB_x2lmvvERgcUl7i3D0kXGR4y670Y0UC6aDFtsyl1V8Ietz6wwBwSD3WrtRBZuZYFy72_8mrpzXzdeVhYuFDHAqVMU0-SN6odCMIN-O0gWf9woAQ0SJ9TKI_piVMayYDCehDaVbMod0GPKjgEwsaaEcyu2d_uF5mELUQbAIdmFxmc1fYPIAAYUPKL6M7Zb4kVO3syU3FAQlvEAjem7VuVNrA0bhRNmqqusuGUBVcX2EGObWA-6Zg05RLpEdsoAmW_1EsyFVXf5jnaBCyXk5_HB5b51EQ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازهواداران‌بانو تیم‌های حاضر در رقابت های جام جهانی 2026؛ شما طرفدار کدوم تیمید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvwsuaLh08N7N6TR8SS4-ziCpQyS1LYS3ggjHH1kA0lVtbZjoJlphFDLH26yeOR-j-o7Pqr3Pkj9TXFRM5uyrdXr2G3L7QD4QpKvfuiS80ugtYRH4utjOqQP3VjUVTomT2_WErhhewQEoN0_yPNdcQvsJmUezIzAQfWdOMWGzmxK8XeJ8wasS8vISmNIQZlBcLtdX85LfOAU3MoVV3OxXnz2_W5j-RF90JZaJrARVXpvi_dfwo_2UN9B9xWzsCUaTOETRQd9XrtsccSocuCVo8eVIZ8plkUqOHlkGyiHu1LVw7IVfN21a7xz_GYrREhtuYAfZYV3gZzWD6o1oH8Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF6DP41XbeLiNYMtzQ6PacKfsYZ5PFiwUwpIddW136Dwz5jiOYmhpyBnFeyGV_aTPzatL8bCw9Zg5gx_ENs_Sj_Nt0PG3bnrffzPpphahF_g5yUcTDq8dkRozUstSxaOhENk0QKuG6amYKLyi29xldXsyCdBQatuqpuK9VEQNM26XKypEwncvYVFqWJkLnserbkoam1Pp8syBEZ2lUezY1dVhgtu6WpiK_yfXaXhBlHxTx60MZbTM08-xCFMxi6vgHnRAkh_1Z4F_T1BK52ajae2FPZq9RRm6qKRNswmnhx2LP_bybZpz51K2YSQY2P5FwKqUGzB-qwntcxjt5H4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjHuHFy82UmObqOkyjKT_dcRfJRZJYdq8dMqJ_DsyYWC64hkgwK-tVt_4wvBTlIEmmKT4V_jRZsNjuSCRpnMzP5_Lpc8L56317gDPYnkZugYKysUFTtrMsmIUXHY7oVQFhfCYukwN2WpmqbDsqBbdXPCPJn1vu1L3PQNsfNN8tRAW4wPWJVzkT8kKd-9R7dIc0pdEUodd9FDPYKxqcfgKbidgiTksI61AiNrU-YpdUkeeT-oNUs-wIHVyTJy6SlMdqfQkjS56-zpStfRSf_9Ezs3VvoTdJwzKDJe5CesR0D6OXmVgZJr8rRK3ISramNiR0DC3qommzYgFTgV7ReGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_5VZ6qkaMgd1s2E7kv8kFbLG_KUUp23sN59dmDwwPSWQCVNmBq_XhR562VWCmV12GxNCMwSsCJf8S4ktkflIC6jp65t5-oL4E9X2MlPdhNfJ3e5P3ylyQngasJqDsM12fWp01UpjJp69IgUgyzIbwAUR40dnaLfHIC7VdCSJJLnqvNWSFAY2vjlojDKJgadM1rbtv0EL9cpbUm11zWEB58rDQ8Day79r34m1ciEytC_koBO36f0uHcgC8odti-rhqOJAcTw3CjEOPioBy48A9cboAGtZr_mjJDIVKUy_eUMEw9Zgz2X3E4a6cKS-7VmoZXAX2B6Tr1DCF5JdkR1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCtwGVF6iZk_e0FI1LxFTJvKIgkmssBnuDSI6GQnNiVWXS-DayzQAepsG1kC50LEPl3yhUpBkIvc00yMURyyl8rELHsUGNMI94WCe5nE-8Riqq6FLbQ3xh9OPVv_2bErEu0fIt8JreGbySkThNZojZq59um0n096-T5GWMgHGbIANDJ6SEf1oQiokB3fWmc1t7foahiavgdEiRJeN_QJmTiB_O8eoT-1QW1EIRw4iOEiLEMrV4P3nuXZno9C1wcPO3VmhUNH9pOlKtJPLn5n7E1_lixCJQa6U7LfsgvdrEu2eYI3GrfI_kZlzvCuMwDcAbZN5n-m3110e-I7Tzj_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/av17zHrAdgxtnYsUQhTuIp_6V1zhmwoIxqQJXUHSep5S20BNo11fNcUNevGWHmFCAaFLK8YBU-f4rc6ZnpsWIOJColw6Ur3JNloMj7ml_uXYu-XMqfsolGjgyE3Ijo64w6NTp17xH3JH4D9Mv0hqLhptOcqI_R3u-2142CC90ljH7pYZuEu7sORWkRCJ7bOhe0PAzAfk_6KJ1ECXoPbkoSDpw5yLBveVsYkyGOuzQrOIvyiAKpV1e-hrrzUCE21cB_lyzOfhLcSUJqHv1YIHxJo9XlaSHqqRmfNB0S8kP-Sz14-MFGao29U7SIM_lusk0f2hZ5NHTqWNhYuCYVYklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aASV4Er8gMiudfXMGhfNvCHb5fibyB2lnCia5RK3lrxUL_JgJeFTon4-0m-qMOfYYc6EYGBwx9Q3r-fuI0MgVjR85cix-4DVj-OF2LjojqP1nVsbGUVsA2FS5h_74GQQi_Qp58VGlNxqMqw8bzcqGtAOd98ja0Xf--4fjQ5dMkIQc12jz8qSOoiFohraVUVWeI386tgBiD5rXMCdydvBFQ52tpM7ODOfLjIt6W4bIFA_dl-CvXz9hKeNI9MCEfXYSW0rSJpAqH32HFzcYPIqXfZuTNjAt9Tp_7_ge0XOkDJEKh8b-zrHAbN7_IlwFCzUQE5QeU0vz7i_KHRNm1adag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdSsmIeSqMVM9-5L217aEULWxs3MgOPz8Swsvrf-VbydfJnHCx-oHA5vRyu82AqhWOG7T9Zi9ljLb9yrFYHFlSZQwqCrtRaBhKkqNTWZCi-v1t4XPGKbAyaf5KMCCoQvvtOjWzWNkzd_iJddqKgWhT-j1Uip47C1xqDRpFMFFdKNEIQBb-WPiShO3Ub4r5SnOwkAVUBwZIo2dpB4AuUr88Sf1yWsWtWwMkqZ5MIHK06hOoRL3n9SmgureJe7_wrW8oK-rEQqYaUq-a--_f3yfa2JVHgJvsqDw96m1UW3WXxwwjkSvDnGw8I2bfkJj9EYCRDxIDg4zKoNUoAIYZ2_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=df9ar1NOkmtz_Bxxpd5cleNS336Wy-xHlnDPREr_cNkTbFhcFtoltj078ZSBMBZOS1ckjP8eX6yfbi4ymRNf03DSF_zKs5tcy3719GwzLwODt3-Vlg_0P4dQbAjHxpv3brdPeITkD3VWbjjI5JuhKI4ybYd3os1kmrw4iw9vibpl82pA9MtrAwFJ5Lg-h3PF7oAnqF08Ii8DG4Ild-dvv78Lx9V_NjDvwA_xSEROv83d_5FN8fDfaOwLweNjLkAXCHHfI6Edvm0ONrbHlJAbzccjDYFtWPK8h2OZ50z4Gr_NMvp6w7umjrR4IQ8I-g-fboXe5iHPJ8PaUGZR95OtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=df9ar1NOkmtz_Bxxpd5cleNS336Wy-xHlnDPREr_cNkTbFhcFtoltj078ZSBMBZOS1ckjP8eX6yfbi4ymRNf03DSF_zKs5tcy3719GwzLwODt3-Vlg_0P4dQbAjHxpv3brdPeITkD3VWbjjI5JuhKI4ybYd3os1kmrw4iw9vibpl82pA9MtrAwFJ5Lg-h3PF7oAnqF08Ii8DG4Ild-dvv78Lx9V_NjDvwA_xSEROv83d_5FN8fDfaOwLweNjLkAXCHHfI6Edvm0ONrbHlJAbzccjDYFtWPK8h2OZ50z4Gr_NMvp6w7umjrR4IQ8I-g-fboXe5iHPJ8PaUGZR95OtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt8RxDaWbZM85ruxIzXeO-0n2CNT4EdFJdTwLsL2T4FWxVKGYikixGoQiXOVLKuLeUVenhTVmcOoayEVw5J_59Qqd-useBIti6t1Kk8VRkpPmo1qXoMpFuVH9qXfQ8bA3Ika9btqG7bDrtWrw4HueLix7mTCuvrYdjxNsT019POzcTQRiXM6uy3vCakhis97656xFjdtu9yRwPSEWBv5Q0J8BJLfWUe6LViL8izYWOhgVmr4VCuex8FFpzfLchcPyG0aGIxiXhNH1P2sqCbv4-71iAkrjQ4Ww-qpb8hS6R9xX59jmmSwiWtXC-XG26ZOdMKKpKt5iQ22lNgGZyqeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYSs65hm-hwRxImADxJMdjfddOnsAn70FK9YNDyHJrJTBpzczsxGgVrOgGsoKWFRfp3snWRXtvr1E-hBR4zthtzNLoKAwlfJ5aMbVz2FQnk5dF_XVbHjqfjkg3FZr7IriAvKBcwTUtNPKV7MixiG_J9sJhLCKLD3pyHButsevD9723UpXrYb9-zMhoR2AasGCjHo-GgzHlp4nsMaaMmrSL83mlv1PmVe0DZ_CFNPTNfEvyonH5N9Y8zDd80ZY4LNdTT4KEevpwbBQlUn4FW1Wfg9Iew9iWRMyWCXxV1y8lv6C58ULj2SKkU_-ijD1PF6PS2Bzfp0KgviOVJa2CaxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfLYbIhvXJce8vMT7Acs4jT83uiDCN0CzCc94O2gksd2usKL_VEeL62Df0jjp0ROYvO9hp66uC2Y_kJwd1Zs5XTBdJSlEHZNxRn82XKGhIdt5AC7QgNNReT2mr2t66neD90gZNEnawn6DQgAdodq77AHvpxSkIvJ4PShi0SPfDAD5_UXhL-6H_HgctDlNWFVXNxIyLeRfTQSOTXWqhV0CCSmsGtZG3XswDm0salxvvQ009R_vLmeGazfgqIrnQ6gxYz_64c8FWN_p9Xfl-mBwRh6BYwR22Y41FTKbziEuyUqIZlT5pjSK3IFWgSNhn6t96vvLX8DNj2_CQd5mYtj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💩
⚠️
دیگه
#فریب
بونوس‌های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت 500 هزار تومان‌اعتباربی‌قیدو شرط بگیر
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g10
📱
@winro_io</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22543" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcAKbDnJ-lMRqn8bcHu6-37i2vRpctPI6C3YX9EKBMwQzTvJLAg901kfCQGiUepeiBPgClootmdvkrgrQRcZjmua9np2hHKtn4Wd5MA_S4J4sK2qQOqaNUQgqCXeY4avC6rGTZQMWy7Q_A58A5UpC7SlwD7Yoi5aw7-0w9Y3DFs8UU-emumtQca6FPji65Nh_rCi0RH-xYeBrhAo6tSK4-AjTLp01WemlInyCKJluXNEgIiDnAl8m3IuYfN807sBumRGLEdXhVIihxzafad_vFhp-ZeLnt6knHS9OdJ1qpINGYFflKrWR5_9sCx3aIlOL3ajH6w89P4DZflZ_EHQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XbCkn3yEbFD83VgxuAckuUjVgj6JdNdaww9JGnfE-U6Rs-bX5O1LngWyokgZ7r_48Lk71FxrSMXs0vogNO19HTa_fZRXnI3gY_GaRl-ntZGEl9j01n0ytx3cSe1Lac4R1Y6rbQsCp86cHISAqYHybptst2ULwe8u0afpmIPN7GfWpeiGAYpdwBtANRm2VRJn9AodwezW6CQNKUV6j5glFpCcecXV4VCHw-oHYlb2WBXm_ivzelmelBAPfSogQojypbe0Z4nZZ551gaSC2z54mz25y8r36_r24FEyI1RzcG_piqxaFHHEEpMVHyjuOJ0tANRUoKNmv--4uH2VtDbZMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XbCkn3yEbFD83VgxuAckuUjVgj6JdNdaww9JGnfE-U6Rs-bX5O1LngWyokgZ7r_48Lk71FxrSMXs0vogNO19HTa_fZRXnI3gY_GaRl-ntZGEl9j01n0ytx3cSe1Lac4R1Y6rbQsCp86cHISAqYHybptst2ULwe8u0afpmIPN7GfWpeiGAYpdwBtANRm2VRJn9AodwezW6CQNKUV6j5glFpCcecXV4VCHw-oHYlb2WBXm_ivzelmelBAPfSogQojypbe0Z4nZZ551gaSC2z54mz25y8r36_r24FEyI1RzcG_piqxaFHHEEpMVHyjuOJ0tANRUoKNmv--4uH2VtDbZMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=hRX8qmB-R8bvBnocsjvW2usOhVdS0tCIYK7O5u-5rDvwKEEM3CmGoiqnuqhvucILO1ZDwWPFLWtYc710-NPbhUGHXw2LCSWcnagxf-zamRscfj9mfLxZg7R6tBvBHGlsTy4xtmGfcaHZKjyoZYh8ouI0DZF_pa340bprW26rOQmnknNip5ZigWuZ96Bwe2tLxk8HvubJTj5nqP_fuMdN9u-PXe943aeC3FcrJSMB5_VdNn-oXyCmUzBHYxfoGACcEVfcIjp6DI8fHsyhkMmCGtd-NuxmIrEuLu49Pzu0YWaQsUNx0k3z7cp7mI9NUjwIEiDXPm1AUjiqBFjSeexAqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=hRX8qmB-R8bvBnocsjvW2usOhVdS0tCIYK7O5u-5rDvwKEEM3CmGoiqnuqhvucILO1ZDwWPFLWtYc710-NPbhUGHXw2LCSWcnagxf-zamRscfj9mfLxZg7R6tBvBHGlsTy4xtmGfcaHZKjyoZYh8ouI0DZF_pa340bprW26rOQmnknNip5ZigWuZ96Bwe2tLxk8HvubJTj5nqP_fuMdN9u-PXe943aeC3FcrJSMB5_VdNn-oXyCmUzBHYxfoGACcEVfcIjp6DI8fHsyhkMmCGtd-NuxmIrEuLu49Pzu0YWaQsUNx0k3z7cp7mI9NUjwIEiDXPm1AUjiqBFjSeexAqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOuOzLee1NBfy67A1oMawMQRh3iW8Dx7uuUU8LqkB_IA8QOHx9woJuhkKp6wz8-bROaYgPzt9pNEtLlRxSCD3tEzv5sFEJ_t66MMAHDEobMI_x9OspQNOLd29TIkkVzDhudH6GfYmuMx-zZAmDt-oskDlAkiH4_ctBk-zb7tF2K0NUpjDHm_8hu-CPOPsbwX45q-dKuq1_Jrm30RZqYhRlVeFXtjDt9oFwB4tRFYYH46xNOIN9XP1391RHbZrCMPf0inu5wyCQoi_7mRCxHesvIYKf_FAh1IkUDWh8y_UqZ1dO91MxwvcY91RVApK3aTS6ogCgN0se8nk-_XMVquKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObWD0I5mcTanFCJ-jaYDX6gD5ig7mv9GKZFzpZa8IIBeDhPV9_VYG9zTLXTzXG4SqP9BCACrk_6ZOCFdkFqYW9pey4TULioW92Zt52_4IgnJAMGACLiZamNE_BeORgJARHmtC6VlJTAxqvAxSvWCz2gT_ORnaMn_GcK46YDaZhOMifIqSykJ_mW-sSgybFl9U6_yR1iBBfJ3HtWiZqKLhAVqbi_Ok9T3JpM9LuXY703DfMXCgalWH2NuXugy6N8oZVRUUqx5t6Jh2jY3k3yewj2FrbMof10ddqONIjMFufRyeohRN8hJzcSvKBrpFaM8hz4QyXTDKncWn2Whr6o2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYcdx_kxaEKeDpaH7q_Zcp1csFxWNq48Rqq1cZfOUSjeUyp_7blrD0GP387ORH5KUTRYicbvN4rnJEDX27MXxBLxdv2337b5x__U06vEYqpHAZeJdzpm_avycgkIDaj5gAqwP8MiBk7RmtHLOHwB0K30k1I6aB10qodnn-fNKEdpIJYZAgzMH__JxPeMr4NRnV085U7nJqQ-IgnMvFjZnPYuXZ3BTLF_YvdEVlUM5FvgqxrNst3HFxjI4drlsneNtClvFcmq5MX7ZSk44zxoA7n4dJ5OPmvRMDXx6GYpLOysuUOeCDIoIeHc2UAjFeotqxh_kIxlLS-Td_64JjdHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDi2flK1XL1MM7KsI9U3xss0RLuqgv-eJU5ARfUCmQcKE6nfA-hpjjxXy0B17lZXBIedkUSVtvt2nQDX1m9WBhir9CFaizKfadcm9CrlVZE4FPCDirbowMEDs9vm3AzBRzdho8kLYMAwgdFUHbOsIza8ZrNxIDxoiw4tn-ou3Czir4g7zmIDRsIfQnmVrFkloGrekrbLrQSgov8Q-7-3w89A1GWnd_msBFnZTOyf7NmjCz0bbi9D6IfRGjPusjP-gAqHklrw33x904-F2Nl_9qxUL-_fszZsuJeuxkqHbR-ZHa2yNM1eGVGkYa5Y9StjF71e9Yx3iDctl1bixjTQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpaAFIjeWZ9C4_sepgoHdkChTBrCrvpY1sqtv42eIRRKlrPQQwEfZYzEn6TkHpOI_xfjzBq-Ewbyv9fXdBNEWeqR1ZV-uqPRBp6DQzbwMDer3JWW8HUrop5GJoXamsnQXGW0UWEBJL9MvtArH8AkCHr0gu4ZksiUxyERZQjPVNv4Sauw1yocWBstkXNf7wyx-OHFSUrvvs6E1CsmgJfnZ8A4JfvB4MjqxfTV0zyRNUGn-5gDOemQegc3sdCnkRXbT-La3Gxwte7AwPwQIc9AQRJAMttP9JZGh2ne6vjPTo21qxcgHrHAycSm0bqqoOvqGpHCpiY4k9yFtAtia4-l-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIXX6qMO7XTik32eesU06cyHdmp4bvTVW5mpXhG6P2wxPnYO0YKggZ6UtF_fH75qD5awoFWAwsQIO4ghrn5DAvfXqGQb3Y1ERVEZKMMSyPugDLejOO95pG9_B4xEkV-DSgp0b-UgyDEOEjOmVPaoXaPBKrs-iP-Hb25r75Pw8ESu-rbJDreD7vAhIXyk163zfpiMwjHwGt5enTAmH8ZtQ_wfrUQ9rEiPkojAR2ipRvrMmvlwZG5a0lm60xJ983H3-oZKamwC99cxO8Do40BNhWyKexP43NuZJW7eWgcEuVOEpQkWc2E2hI5wesMUduuroJpcjS6Pwf5yLhG0nvlt4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt4fS0aNTu4n9t1FaBcZnhHDzUi9t6wt1mXIxQzbjZIqukN0jN7tGyXE8ZzFfVNdc3DMkRekdQaZz4RQ44Du2K6Vqm2xeY6QcI5xh9-oUNY6EBLgJ699IZY44QS5Okk6sZnVd3qUL44TNE43r2aIkqlzugXYtd9ZysI3Rc-DCvKxjK7JN9kezxoxOKFg3AaKqtn-e5tQwbKUbiu936nnBLKQ9zG_V9A0nW_CNuiX0HAk_QdftA31JA4px_L-hSLB96gP3xAeqL_exC6lCbjBm0Zcg3Fv-tBZdtd6RegPR6S8xIlQDOaQ8x_kmwXnni-OlQFyH3xWCTlvaDfuG3TeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaXKoPz53ZbF4WlmVF9O9Fnt23b6JBA-q5BUAm9Rdw0B2DY0MUrapH2UWbBqFJaCZmODwXWNbt8pLHagnBbXr8F9iQzshIEbyxX3bFlq2xt51URNyKETeFbjLOVqbp4arys1WLOrHzBvijVEOgwH1fRky-SFAkVVe7p9QzcxRUgVYG5QIwrZz_e3ifmWVR5HQ7MTj4fQKBy_vBXzuOEFNaWwidQ74fsjeXZ_bmYns8HH0SfCvRQPvPDhK6Ei511FchIE81QHZ2uq9lY8tYeWNOHX17Pcc9-1o8Z4XgQwP0JcR40SCfUpw4UKz57bpTPKfNlKY-H9lKnxbxWzU_J1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twXSBUkLwHEerxnqFilwM3ItsZEEu1PE5GgrOl-4FAU8SeAaxbfL2so2RdHHUYGsGy5zMeSlra9vQOGOoVx-g8UpqoRcaSQ1LQMIY2MVb-b3SmHs0Ysbxrsrh9-MMc6aJf-iYf2Y7wa_ihlq05osTi9c5ry3iurjf_a1jLqFBF6l08lB72J_GBXIGmSq-WoBh3TQBWaF-wzyZng7bXmNjmxmmkcRxIwZXwLXtr9TyWK0r-iszb9P2Dhd6w9o5OGazpGup-EhKsrnU16pbXSAeud7O-mD8XTL13hwKEdVv--rzUoNADcliRSO0MVlgyJ0OzG5niq63M44ddalU76a7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=rTgO24QAZzNQu13J2_IDd0idW0PDC46aVjn2IXJ97QS2uIVbyxDHdUaTS-fT254xLwyOE16RkbhZzUCSruGSorJ54hJBqSzk0oLDR_xWsHAr9HJGacFmxI-AGKtHsHAbNAtfxUe9BrpSD14IYw5B4X3eAArce-Hf9L9K0CH4eyUB6JlpfOX9tkvtPHD7k33WD0_wJfbWKzzVPWlyXGmKAhkE9x-0JMtlAiYCZrlM1g677eMR22AcZ_tgepNhiLRNAuAr8v7hixBwi5KuccxubGIBjleleiUEZUopGsbv06WVXocom5TC2Zrbl4POxlEoiGfE7404bfi8ZZQkyrrnHRU_0ZzB2aybT2qVhMGQdggWLSmNXh30du6FjReIGWVJc9dqE4HmlqnAyVJqTaUDumxYhNDnewTXtG3FA2Dn9FrXsODpCHl8gpTU_kpHLTBH0fhtQl-G59_OMjb4u05TpD9kmljnEyQSBj7fi-TM9OVoHs_YxpjINk-3vw6tEghkWo2iVp-2Tdu2b7Cf7OK6_pv6T1N77dsflrSLlrmUgt3Gv5CVeg55efVLvA4BNToIGLglpO6oCtVPXvtCQmdGKgg_OBCTnc4iWeETp0M7Og2GCoyikR_vXgH6PvcyCqKa-eWQF7TqhRN5pCoWmOyndzQd91nDOya8QG73Ok6dF-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=rTgO24QAZzNQu13J2_IDd0idW0PDC46aVjn2IXJ97QS2uIVbyxDHdUaTS-fT254xLwyOE16RkbhZzUCSruGSorJ54hJBqSzk0oLDR_xWsHAr9HJGacFmxI-AGKtHsHAbNAtfxUe9BrpSD14IYw5B4X3eAArce-Hf9L9K0CH4eyUB6JlpfOX9tkvtPHD7k33WD0_wJfbWKzzVPWlyXGmKAhkE9x-0JMtlAiYCZrlM1g677eMR22AcZ_tgepNhiLRNAuAr8v7hixBwi5KuccxubGIBjleleiUEZUopGsbv06WVXocom5TC2Zrbl4POxlEoiGfE7404bfi8ZZQkyrrnHRU_0ZzB2aybT2qVhMGQdggWLSmNXh30du6FjReIGWVJc9dqE4HmlqnAyVJqTaUDumxYhNDnewTXtG3FA2Dn9FrXsODpCHl8gpTU_kpHLTBH0fhtQl-G59_OMjb4u05TpD9kmljnEyQSBj7fi-TM9OVoHs_YxpjINk-3vw6tEghkWo2iVp-2Tdu2b7Cf7OK6_pv6T1N77dsflrSLlrmUgt3Gv5CVeg55efVLvA4BNToIGLglpO6oCtVPXvtCQmdGKgg_OBCTnc4iWeETp0M7Og2GCoyikR_vXgH6PvcyCqKa-eWQF7TqhRN5pCoWmOyndzQd91nDOya8QG73Ok6dF-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنش عجیب ایوان تونی بازیکن تیم الاهلی به قیچی برگردون کریس رونالدو ستاره النصر
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El_LjG3doqVEZZ_08Jb2DP8YHYO6ae2pXcHDdaW-wUFL-zUGZZF2mCoOR4nr6vQ5c9GGTCaGuza75Zb9kKTfQYu1y2sLvTMTvOjzNn6xM6z_VZx8uY6EeDCJ_56SoVfvZRLGefo3xLSCY5_vNS_UE7dwPpxd1nQ3-tdATBzM9GIKrzbCIRzHhXz5g083HBv5X6rSRg_t7q7-qIXYL13M_uz3LKBlz-sweNvaC4CeBE6V1iQmIp8nrCLc8Ki2E1263qgFyqwcgljm5lXG4sqTfNI5S4C1qHwfVLo8RDFjLescSDXnDUmyBGX_Elz16jUYkXFm3BmkiSObiqPZt7ghEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fCgnY-uoVsxg2tAKTHM4CDXEBaRifl8ecY1yznQuIO4Ng3CA9xTxeldhsEqM2CWLBJ9vPXnNw8nud7AASSll9TrJ1UL-LsNL731lT3OOo0-eRBS570yAg-bHXJtGoUofXqzmNiLvM0724VJi4Xwalx2udQnzyux4k8MkksVn-RCvI0g_exXTlKOVIbjz0xgU9MBGgfRHP3Xi3tUXupLVF-2K-27Rle9am2sWtk6B2TzWlQ6NsTSeyNYJFa3RzM8zCjFkZInkeZpJfnLtyCsx1o8rTspITQm8YjpGj8BZtneySLn8iJPndf42wrFANIUnfnz3e1uMlshQKQb4wUhd1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fCgnY-uoVsxg2tAKTHM4CDXEBaRifl8ecY1yznQuIO4Ng3CA9xTxeldhsEqM2CWLBJ9vPXnNw8nud7AASSll9TrJ1UL-LsNL731lT3OOo0-eRBS570yAg-bHXJtGoUofXqzmNiLvM0724VJi4Xwalx2udQnzyux4k8MkksVn-RCvI0g_exXTlKOVIbjz0xgU9MBGgfRHP3Xi3tUXupLVF-2K-27Rle9am2sWtk6B2TzWlQ6NsTSeyNYJFa3RzM8zCjFkZInkeZpJfnLtyCsx1o8rTspITQm8YjpGj8BZtneySLn8iJPndf42wrFANIUnfnz3e1uMlshQKQb4wUhd1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژوزه مورینیو سرمربی‌ سابق چلسی:
ابراموویچ مالک چلسی به من‌گفت‌که برای مهاجم کی رو در نظر داری؟ منم بهش گفتم دیدیه دروگبا؛ گفت اون کیه؟ کجاست؟ گفتم شما فقط پول بده و حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یجوری هم متعجب شد از اخراج شدنش که فکر کردم یه خطای ساده انجام داده!!! دِ اخه مرد حسابی زمین فوتبال رو با رینگ بوکس اشتباه گرفتی
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=Ixi1fA_0i1_f4b6DmmYnU7SnkAReHefDVDQRPhSYx9Q_TfE002XfwmVFzEagX70pHF0R4rdI21b2H27sJrtUcI--fGxWi95eHc6_eoMk1X0yYLUK-J-zulDkFX1JN8OMxVzC02rt3-YAdiwdXd_Fp4GER1vgrfdUT78aY1MrLDs9fSDFSB0i0F3PvLk9VmL0fmeNCDfPN_MbVYIcLIdp0uuJr5jk898NDG5LTK2YHrOyyg_rguguSgLLhUcEbvoj_XOj4-JlnANuPyst2gm8eWTw5BDGPOrMK7LZ_HCAZpx9kIjiq0OOr9MVNoYIhS_9fiEPnBYUP0VStSdBTM6yvwo6p50DidMS5W96msqS6CdhRaRWMImfssJYPVm9Q8IS3DlPp-DZHD23vxwbesKim_yaak99uBZHsr7p51P5SsuOnO0ZcaLo6rC-eldaeav-vF3MD_AVlKBfzqes_vKwYKcKfE3caeWB2CELBtH2_uPA58QJoen-nh6rP6HUCjdDFI8HTltyiPqt3vbfgjcuqojkH4xYXewMY5yCYRaCGAcN-ouJ6frCU8P9u5sWezuXZciDToE-uAXEZcpjOoS7_yMp_rXuLncxjmH7EvtLwJp47P4H_Hrp6UBLm57-FXbqfdZXmKptZpv1bFvkVkK3uYOZUwwwdhAEmcuf4oIh5yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=Ixi1fA_0i1_f4b6DmmYnU7SnkAReHefDVDQRPhSYx9Q_TfE002XfwmVFzEagX70pHF0R4rdI21b2H27sJrtUcI--fGxWi95eHc6_eoMk1X0yYLUK-J-zulDkFX1JN8OMxVzC02rt3-YAdiwdXd_Fp4GER1vgrfdUT78aY1MrLDs9fSDFSB0i0F3PvLk9VmL0fmeNCDfPN_MbVYIcLIdp0uuJr5jk898NDG5LTK2YHrOyyg_rguguSgLLhUcEbvoj_XOj4-JlnANuPyst2gm8eWTw5BDGPOrMK7LZ_HCAZpx9kIjiq0OOr9MVNoYIhS_9fiEPnBYUP0VStSdBTM6yvwo6p50DidMS5W96msqS6CdhRaRWMImfssJYPVm9Q8IS3DlPp-DZHD23vxwbesKim_yaak99uBZHsr7p51P5SsuOnO0ZcaLo6rC-eldaeav-vF3MD_AVlKBfzqes_vKwYKcKfE3caeWB2CELBtH2_uPA58QJoen-nh6rP6HUCjdDFI8HTltyiPqt3vbfgjcuqojkH4xYXewMY5yCYRaCGAcN-ouJ6frCU8P9u5sWezuXZciDToE-uAXEZcpjOoS7_yMp_rXuLncxjmH7EvtLwJp47P4H_Hrp6UBLm57-FXbqfdZXmKptZpv1bFvkVkK3uYOZUwwwdhAEmcuf4oIh5yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=jocPW5zM2B-nuTKABXcKIahxdGqcWTZWdtjRnAoex5Ptw8WNqxTzcZWaUk4IMMoXnSvx0_z1kWOl4NA1w2GBGjCYbLuxHywGSTRoKfo-T3AVgtCaLpIT6hQH0rNwhMKXS-Dqh-s3ffsVNnH7bvbkeq_Xn00i6l7Pz3HbWO_D26MAOjnZItbJ2ke2NyHuw0g5ypDblh9SSzRv9dJD9A8mqP5TzwP5a6n_j2pIJ_HV-hbRhVNsabteqSInluYp1YolIoAp_O03i9hUnZvU-S19F8he7UVUqsMvSTLgdDFdkgcBrybBaQ8C4efbABTyNxySdpnQImGUQoM1UoPh0dnWXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=jocPW5zM2B-nuTKABXcKIahxdGqcWTZWdtjRnAoex5Ptw8WNqxTzcZWaUk4IMMoXnSvx0_z1kWOl4NA1w2GBGjCYbLuxHywGSTRoKfo-T3AVgtCaLpIT6hQH0rNwhMKXS-Dqh-s3ffsVNnH7bvbkeq_Xn00i6l7Pz3HbWO_D26MAOjnZItbJ2ke2NyHuw0g5ypDblh9SSzRv9dJD9A8mqP5TzwP5a6n_j2pIJ_HV-hbRhVNsabteqSInluYp1YolIoAp_O03i9hUnZvU-S19F8he7UVUqsMvSTLgdDFdkgcBrybBaQ8C4efbABTyNxySdpnQImGUQoM1UoPh0dnWXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویتینیا: اونا تا میتونستن وقت تلفی کردن، اما در همچین بازی‌هایی بایدصبورباشی؛
ویتینیا علاوه برکسب‌جایزه بهترین بازیکن فینال یه‌آمار فوق‌العاده هم ثبت کرد؛ هافبک پرتغالی، در فینال لیگ قهرمانان اروپا مقابل آرسنال باثبت ۱۴۱ پاس صحیح، با رکورد تاریخی ژاوی درسال ۲۰۱۱ مقابل‌منچستریونایتد برای بیشترین تعداد پاس‌صحیح دریک‌بازی فینال از زمان شروع ثبت‌دقیق‌داده‌ها درفصل ۲۰۰۳/۰۴ برابری کرد؛ او همچنین باثبت مجموع ۱,۵۸۹ پاس صحیح در این فصل‌از رقابت‌ها و تعداد پاس‌های‌بالای ۱۰۰ در ۹ بازی مختلف، به‌تنها بازیکنی در کنار ژاوی تبدیل شد که به چنین دستاورد بی‌نظیری دست یافته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOJv9pBZD9sn5KPGjoB8XxocNU6fhGHDePicUkeWhCy5-BAmTpc2l3vmVeP9gl3gDVOCK1nNgZfrbX43bp5pDzjswMfcdZAEf6U3HONdVQSQHhNNvRoPMqNjKQyhIQGsGUg4TWw8kDbfuTKopLY3axyAcE6Q6PMD5cSMrkxOqiluhZYPNXG2PBnKMr9aa3OndnvOXxPF3wOgh6M6U5JF5GFVeaZHU3wT7qu_0sQ_M4nXv19aUGN5MA8TJfp_j3V9orRTXbNJHcvlA2xXwYmND0bj_iJF5uMRJyRPnWejq5urwPxoCsXPkHvBsMHBmsmSbGLLSPA66DpsTyqR5TuO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
🎉
کافی‌فقط‌عضوبشی‌تا
#وینروبهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22518" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL-5lKyZCXQ3CT4VtZATqgCG_kPoh68QITjwqPbnE-k6qGk58t-6eS0S5T2TBYCOoZVgOb0LixxJoGKdmwCv-pL6mZSldUjshpsPPU4zCaHOjGgdZHch9Tkyb0m7z5jLjhyI6rx_cajSBwtZ0ZtsXw8SbkpxxTzl1E88R0_kd85F_0lREYM5Eh5Jzf-E3dj8Ls2Gu5rxhoq8tlKbmy9I308uyeDGmpeHdmpWEDhNmzdrYuUzV4lRFlbUpMVP7BSHb44bn2AVIRqRuARunGoh3KYhHtF6ZeOrCTrCsS1YuzkR8-PXcphcli-177PYCpu-fcMKzEdZSrrb8ueIayzUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22517" target="_blank">📅 09:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_pNmRVL_uWLHfyRyJgYHkaBEtXj_Ygi3dlfC1LqiiiV7G7j3bEuMgFP3ojqS-4m-4qhDdTs8P1cf6qJuMjctTrDkbSPTJ1GoEPgoE3w2KtMy2oDLudvTQI7JWdAKW5_Aa4dGMdTMZnaRILC9VUuN3R2__xiRFR3kGVGHhgfSxSO2Rgxl42ZgN4Ekj5zPK4fDqyHFwY0ln04wwKmEe1XmtCIaZkAlHa9c6fVTwYTVycZ_AhrkVkgmG2vwbSaSLDeZGWZC6YfgeWBfaDw3ETHxhXKtG7tkKZxiWnx5kfB8JWOlyfUqP2Qfd8R4O8a_9q1VO-4gjs7t_dkbR2WmZPazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22516" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq5isfehZRyCV4b7GY-rfm9cSkJrNFwxJgNpZvQOee5mfZL6Fe0BnjXwckAvgpZQxesCL5uzcV3_fg8r1-12wlDN6atCW1MbEoomVf6mVmY6RvIwqRDQy6D3mMnAlLbAOn6nK1lS1pvUCBR9jltqVUe6aDdEU3ON-sBL9YuvpVlB1hpb-dr4tzQDQlogUHDl_hHDBhhzTij24ibIXG2vZb8Z49XsiatuajJHox23CLScL0CeFHWaE0QCZOU-3SoRcT0X7WBl1CRGPqIFtFOyVjDwUmB5PUIzbdGZq7Ie3-YPq7xCz_FLDC5TBMfkqrYFR6rt0_5hfwM5a4V_3DtPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا ستاره سابق باشگاه منچسترسیتی؛علاوه‌بر بارسا از اتلتیکومادرید نیز آفر دریافت کرده که اعلام کرده اولویتش عقد قرارداد و پیوستن به‌باشگاه بارسلونا است. این انتقال بزودی و به شکل رسمی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22515" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSRvhs8V0Ig1XQ0ZSC4Tt14fRgawEXl_lV0tuVaE5AbJhKr0Br5oohnv9AtnwjsshhKMz0Zgfqqzwb_gsZWXxtPfGGBKOrOU4ndNqLZ2yDSH5Ulo1e2DejPv0zEpMXQqIiaAysiIcP2bglExdX9j7_S3i8E2vuKZcshwVxYTa60Jsda9__ZLioRH2Y7qPE24fB0yyYEKkIiG3MoR_hnxsnVWzoiTG0z3W9zk4uAX8cIJRp5NBM9del3r-98rTUsQd5joHR21ldezfAvqEZIoTptRbSOPTp0XAHv4duiVVHJl6oDMhIXDubz3cv1PyKLWkK_BjzBnZ2Vl469_pvjCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptQMXYi2J5-aqme7FgSjaCmieMUSJQSEZMgH-wFnP9N8nNVoDZB6f3SW_W5XlvK5KMvLJF0HaqG26ce8wj9swu4w6Lb3mlwJcyN1Ox8awpBoNXfzwdPwVA6i_WpZHbPOLdx4B0_aJtu-RR-UlDb5h_OeFx8Gnnii38PXxKbiMxqV22aglKdg3cdNe7xXuLmfuPsFBvnybvZ3j3_GYVyMy6XyfrxFmqVGRFJErLCNlsGJzmgEszmOjt5IjqtqZDemluweY0hz7M626tisvGsVfDWsA4JdmIzAUJZHrJieUAimtkoR-VcCofiaPtG_aVa25IJJvrA0KEv913z4WhY5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXjcD6bZRTo0KatSJrLD6F3t6oZ9Hv065CH0JtU6O_660pmcJUhLBMCCEGUye-aldBESsz20RtlHYLDQ4m99MZlcclhzbshgAXFBsNWsKNZEWGvcBoWyOSXfGjrohi6KfKeQvtdFPbhR8hzGMKQqADYDlWkSFiLgR5nSB88mO66-t0DQWF8vtGoQezeC8WCgYb02b90_m1b2mbESj1AQTtyunxh_8inGZ2kdAOWRqC3-YCpIc_anHO1B5ZJXx89mpsRY1DYJUCMAv3CUHizXJ9vJcjn7bGI4W_bL5ahD_4CsCnm85ssoXa8yo47-xcvdKv5zk2W4M47mCHQZa3OcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2cwougoPUDwtiHrxmYrJqniz5kLu55rpiKcz_qWCTWKtvcj606LCLutPMU4WGKAeu07XAZiWdUr4TIJS__HSEDEqpRvdCo3ApANw_o_O8y7cvWqwoJsOVX-5d5LFPT1GZo_ISA4RErMECidlfZ2oWnq4PHP5vQaCm2xLEzIcBMblofHsNIJWDd1Ezur8fn-cVBmvX71E-hpE4v_MuPWLUOD9e79PQfPFwBBBIswXUKqZ80M0rCwSUxfuhNrKFnqUK_AK3_N0qYJ4xoBaqtA3a4zJZbjVqkoWmuVoy2VVWXKxdOmvixahIrOpo-yL4-6Hrl0B2kG5ubGSNqL__RSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVKw-DfxLtawQTOmxGRZldTr9DQjF_-wPGzS8PmdyxBa3ee2VZrApcGEFlMzCHhC2nyOnGKOdaSgspxH68XYzS4UUxQhGxeVNa65cMdGzLD7OBdPEyWL41FCYG5YRyS-cQrL48WdiVQoZ-uFeDCMtT9RprFFYgcMYnk4ApqiBKOELIGpKc8ozprwZVqYxG1e2lYHtV6twhjGZOjuvCpnXr-AJ0NAvqZIToIqrMwLXO-iXamc_QrNKL10wS14tdJpwEwG1gS5M1S5T1wwtnuix01DNm264G4ltnLpSHBRMKmoFY5HMNy3YrHSAtWxkGOHlhyfSWgyepFZQFD3AJrO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPKW_E9YYvShQmxVlv42mCuuTT4XI0paIlfyfp4YVKnfwGmL5f1MibhhztV0UhoLn8EVrxEc0pdWwC-GrZyWDeblFQK3lOHnmXkRUGKLNiD5MrxABnZUBi8Wbq8-6rwM-wFGN0XtrOkv_wy2uf-IMWtyLpicjX9o6mBCoppc0hldWXwr5vKF8m_xtSrtWsTmeIpFhLZDArenAQYiwZrWWXxgmRDhTt_S7rKzS3Of8dYHPsxsQsHOh4oFHq0bjLCtqR79T26VCICp0dhpjkxyRujqG4hdkPge2l5l0tAWHzm9EiBm10omQ-_v4g3DQ1tPtAMciwUXGHdkzJxnl2dS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlRk2pqAm3AH5UBZYaAGO83k71X7YZpW-fBv3O4r3opw_LlwasNr7AQecU4weX_tM-EnYaKaKe67jp0alDIlHng13abBxwKuRK2s78Vnv1AkCqW8dDVVuws4YkX5PoHZBJZnmx6cRB5RmLmzAGaUdohWN0DHfmoi5NrHv6CawTbEMid4wJK9IOT1nRDHxOZeOs5heq4WsBtvTo4eSFG1YP3xclj43nkkYG5uV6KVYxS-mMeth-y4I0_CAKF9DaAgK_nZJjizals789dH8q3ozuYAzSQUKqCkr7uHxf5uwdCQeyAg2588r7IB5Q81krPIva5fqsdlk7iXTA5-6uk3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=o_hR16aP4uWzQQ09y8HZ1TN5XraGHn_1y9VvshBLIh7qIFhyKQ46fB6AMbB7jZ3xfqcFTEDdFaqMkCjsdmVCybLt_0Y7qq1oydBpJNfAKWe9PQa3tXZmz90JeYnS5PaX6OrvOsI-umL9DPDDgzOsOAMXIYmwh_7NhQNfjSPAflXw0hcAyc3AOp0Q1yGPWomtzTkNFq2eIc_G4dkiS_9IfBsHMcL0JfzxxwuhD6_0oq8X7slgyUualjcKMNJH0wsT8BP42tf9Mwc4x55gjp2o4Vd3qrY1Ue2nq9JE4ymdlLC3A33jxazpYPVhPrqiILQUP47FBS-C2xFppAteWvzL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=o_hR16aP4uWzQQ09y8HZ1TN5XraGHn_1y9VvshBLIh7qIFhyKQ46fB6AMbB7jZ3xfqcFTEDdFaqMkCjsdmVCybLt_0Y7qq1oydBpJNfAKWe9PQa3tXZmz90JeYnS5PaX6OrvOsI-umL9DPDDgzOsOAMXIYmwh_7NhQNfjSPAflXw0hcAyc3AOp0Q1yGPWomtzTkNFq2eIc_G4dkiS_9IfBsHMcL0JfzxxwuhD6_0oq8X7slgyUualjcKMNJH0wsT8BP42tf9Mwc4x55gjp2o4Vd3qrY1Ue2nq9JE4ymdlLC3A33jxazpYPVhPrqiILQUP47FBS-C2xFppAteWvzL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=XyHCI1tn0wtpuA0BHjHDD_-S6xIPFvgAcGpH0Ucnn7agYGY5OpPhzBjbgvUgtM7sXtK8L8h6CB9cZgtIuawSFRJHVkJuTcMvIzrTxLxPXuawwMX78bkGPgmutb1Fe6-Cz6_ZmetNL6NJqXXagM4qAE7e-WIBUEpE5OpVxjpMCDWkMBnP8VuRiVvg3VVJyat8tSwItZxjtj-2HPkLtVKS2reDJV6Kx7GJCF3tadklVhOebF0GsZ_R0X3FKUNBEsIpn2ErVeatB4U9eZFvnCFzM56p-GTHlNQyG6dJVzV0lG23h3fAeZMaR00Ob77E9CV_0fv7nKCwjGu6uHCtZRvIzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=XyHCI1tn0wtpuA0BHjHDD_-S6xIPFvgAcGpH0Ucnn7agYGY5OpPhzBjbgvUgtM7sXtK8L8h6CB9cZgtIuawSFRJHVkJuTcMvIzrTxLxPXuawwMX78bkGPgmutb1Fe6-Cz6_ZmetNL6NJqXXagM4qAE7e-WIBUEpE5OpVxjpMCDWkMBnP8VuRiVvg3VVJyat8tSwItZxjtj-2HPkLtVKS2reDJV6Kx7GJCF3tadklVhOebF0GsZ_R0X3FKUNBEsIpn2ErVeatB4U9eZFvnCFzM56p-GTHlNQyG6dJVzV0lG23h3fAeZMaR00Ob77E9CV_0fv7nKCwjGu6uHCtZRvIzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIXc4YgWSL9rZMpbeilCL_WvltDNnIiP1mwwycVMNI_L_0tm98ILFee-w086o4GDZSixsGcOPCpq0aRagNVoAmKjzC3IgbvgWT9nsRC88Mp14-fUgGKmeqJhi6QK-taaj7VOCoLFRMKAHLiZwJcRcCHKCXUDZdAB099S8DbPu5cZJkXVQ0heoeXI91pTRwGrPlJ9EsTYKR3caH_m3rMhypLcoXHmP98koYiiXSugnydFPlU-PGHpU4RnxiSfxIpqyxOLzMTAHlLwISs3W2fBiGrCR4nutjAiAl-yqMq9fWl2BPy46mrLoWyUoOaw3PoIvdvxSttWh58RFNethISjnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=ESLcHYZQ-uiDD91GIMbK45I7whq8e0LqeyhKWcbAxf_XlWyjABsXP15lvg_5_KrRaMw0g0j52ccQJjwp4atPtG5bJZ4Blo7G42R8HM9qhyN5SgLPtpARtFIIsFK0uoSRtez6kO_En21it-8_al096JdR8C887-Qiw_19i0dJiix1cHXSjbj1nWHU7VD_2PeDj036XTHvq7QypuN3oivefADMKSFB_APKGPW4ssuteDvpRJfUGKx5MyfWOg7jaey5vRewe0cSbQJkiQ1dSq2FiU5ml6HiA8rKSbREukEPjsowwGG74HVqEPdVFNJSOzbygde7_DxV_Z2H6PR1tVxssVmzpFYPu5Z4HNBEZKpETziZBl081HION_CVyqMXzIecOkjLh9hDiG2nG3Y-HeWuhp3TP54gYSpy1se-iq3zEedG_epLN_-UShfseNGA-nrO1zBwVUdl9cN_YWCVtakv-pRcHPrs3aZDSG6LLXR9Cu4uSfHl2AuqoP4rNWA0zHP_ILyt4NH6TWpnnmUKJaRmcwrmfkzGUeSt1Vcz-6RDHSU4_d0Cd0hb4HLCT3_P-2f2rNUNs-tCFfW7XczfH4wP6wv2G3b77s0PIGPe1P2NkiE_Ob0nHvfAZzLI3OmRLq-mnuEnQ0u-pkziq09aFvLB-YSYjS-_Q3MUwcMEuZluUgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=ESLcHYZQ-uiDD91GIMbK45I7whq8e0LqeyhKWcbAxf_XlWyjABsXP15lvg_5_KrRaMw0g0j52ccQJjwp4atPtG5bJZ4Blo7G42R8HM9qhyN5SgLPtpARtFIIsFK0uoSRtez6kO_En21it-8_al096JdR8C887-Qiw_19i0dJiix1cHXSjbj1nWHU7VD_2PeDj036XTHvq7QypuN3oivefADMKSFB_APKGPW4ssuteDvpRJfUGKx5MyfWOg7jaey5vRewe0cSbQJkiQ1dSq2FiU5ml6HiA8rKSbREukEPjsowwGG74HVqEPdVFNJSOzbygde7_DxV_Z2H6PR1tVxssVmzpFYPu5Z4HNBEZKpETziZBl081HION_CVyqMXzIecOkjLh9hDiG2nG3Y-HeWuhp3TP54gYSpy1se-iq3zEedG_epLN_-UShfseNGA-nrO1zBwVUdl9cN_YWCVtakv-pRcHPrs3aZDSG6LLXR9Cu4uSfHl2AuqoP4rNWA0zHP_ILyt4NH6TWpnnmUKJaRmcwrmfkzGUeSt1Vcz-6RDHSU4_d0Cd0hb4HLCT3_P-2f2rNUNs-tCFfW7XczfH4wP6wv2G3b77s0PIGPe1P2NkiE_Ob0nHvfAZzLI3OmRLq-mnuEnQ0u-pkziq09aFvLB-YSYjS-_Q3MUwcMEuZluUgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=F-qGmgF5UuS2cN2rPOLwikRirzDn3YM6NsOqUf8wVQTl9fXfTrH6-n0of2LSI8wOa3vWHBmxBXSqW3YRkAT7qOecI584_le7dWcqRcht82qIfIb-KKZogtYObPZbg_FLzsJDmYRooXC267LAKLQ_umpD-Sze9imXhY0MKJGUiljtgWF55H6N7jAMe3tbD96AXXzQLz5soxI-7EE5-NqvaoCXqNngOJ3LNUnblOob4YYIfWWvEQPrW9NXvPCo1stBDiOQo5I1AQCxutc1MleRtrvCNnnjhDE2p2Cc6pKNzEHvzG2hKTGsnQpPwR7Ilrg6UMHFvIPv9O_kH-e3tkxTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=F-qGmgF5UuS2cN2rPOLwikRirzDn3YM6NsOqUf8wVQTl9fXfTrH6-n0of2LSI8wOa3vWHBmxBXSqW3YRkAT7qOecI584_le7dWcqRcht82qIfIb-KKZogtYObPZbg_FLzsJDmYRooXC267LAKLQ_umpD-Sze9imXhY0MKJGUiljtgWF55H6N7jAMe3tbD96AXXzQLz5soxI-7EE5-NqvaoCXqNngOJ3LNUnblOob4YYIfWWvEQPrW9NXvPCo1stBDiOQo5I1AQCxutc1MleRtrvCNnnjhDE2p2Cc6pKNzEHvzG2hKTGsnQpPwR7Ilrg6UMHFvIPv9O_kH-e3tkxTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS4zbgluHafTqU0CjEI2fz3xWcV37sCZEp9b_e1TKCd2Xgv7oZwPX4fnuFJJo5_AOvKuqICMqqgt6i54OodXikE7pTiMyxwHUvTfe8MA4utCu01JzCNmZwTpIrI8DYBcM2RgkomxfvbZo-bmwbtRyxRnFSrZSX9V6W8krJMfP49egp-MUs0UPWBbddcxpSZcjgD08ixtd8kvEfXSelf2bfsXfqCzKci63siBSJvHdhWjn0n2GvP74YLFldmeIR1sWNHboYLfWoCSmzSf_CHoFVLRl6MJXzi0eAU8YRd8qUgCfZ77lmrcd31CIoFKXHkyNFw33pXF-9M-eZZGAqFbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToiAddkCBUo5GsIZMQwfc-FSRTE2CHn_qF6_5d9AVWZZOp9OD8lPnPt32fmjKhZBmDWjGSrtKAERS0U8dqVZgEF28X1Q3K3iQ-E9epqJPH52t6Pj76N4s9tZ8it-eATj212O9kbvGPQtZ-7Z3S4nI6stjE-80yUMFIKvNhd-OItgpgfTs1nQKt1kO8R_5dQ2BYd5s8moImKmn4WDOFrEl9j-N92dfd00d-zym66NNcJFik6qyFNTkP_XWXa6aDC9_capP7b7hE9eegF1KRea7ogeGYqAPRyZdtAdxVP46-O7tYVWMVh9736eqD50jiD7pfWGYe6vJ3tTGvv96-gmtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازی مهیج و دیدنی امشب دوتیم ارسنال
🆚
پاری سن ژرمن بوقت‌های اضافی کشیده شد. آمارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22498" target="_blank">📅 22:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJYDIIo9VvzhC1AurPvM9-RCBsNE7b8UOpoKZ3v0JVReGgvQWqUBhv5r7G175pnOM5QDRdUZPPWzI_N0X_n_zyk8rPlGjCHPR8POqqc1lGaIv7HZ4u6VoKF0L2FB2PQB2d__HeFjFfEKsCc6N_rVykyBQ-GmZlJ5aCuU7acE3MofyBPRY9j0a3rlLQysqPNwFhQjye0N6-Z3SJSK-CMraH7a720wZU8RJGdI4h5gkXupP6GsIEhWZBET-nCYkx638RyFtsM371_DbNAOyVwSHrV3IiI3UfDuJI1H2ylagE42IG6wLICjQrS29cNskIG3fRkSHG42qCyL9tnfDlumJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3Ds60_g1-ACruepyogFcZhgexuuKfMDGkHylI0c7HYY__dUeKWRLKbfu3IrTsM8CGel8e7Cvn2XSEuG48C0kVZDVWgJ58xF5TI05ZkZD-9SizTmxaJnxqxZcE0K83cET7V9F8itoiS66uDbGZtIIq-W-tHXUsAfge1PuoXqTms1mSUzouumcEZVhWuHdaK0YOffWY31I1CLYgsqF8xM39TgZky-lKI8l-cxH4CyWx7FCTAPdJL10HFDME3btPIkz5etsbJZpLcQ1Ahx_q3bXqHfBwV4GCK7LkYpe8mpuyWqYHqT3pjqkOK2kivum-Dd30_Cf9szACugTX1e8-CgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA8qECpJvDVCFJo1Tk1GUkfyQ5tpCBgWg3wOl3sKaG58yBPED9kXVNYulgn29vTtxIzWh3WBNrTLja4vaBHk9dpjmS8pC7TbtaZPAhcXiWLSydyCmV4anewackmSdE4hGtbQUUebiySj_X6YhXcrKvVqd9uPncA2gocnE7DnfK6I0HkdG5gaXof_5zPLih-9YLNpzJm2H3PYeqgcLOx980zgznaAERBDTGkt4mWsc_CQSN_xzoXrLXvr6s7Az06DRi9jS3jh_nryKIfwcj79iaCApBD5QXgucH0YLz_V9s1Gl2RqOB8n8HTE4x-2ntUZW40rMShSWtyw2V7nkYZpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLdbfMi_SKihn5MV-cabr5Pio-V_b2fGwEL516hcJLIGO-XKZSHzVk09tp5WWiYI7Bn8fJ5KLeG3S50YoQAfz00-pyshItNcE1bUoMPPnPGSGycdTplxsnSO-FbLiLeb6K9ScU3SDHeyken-I_OFxgbBp2DGcRiB1tTtODD33RaC33fQqcNB7L7b5bpk6VfqqXYe_Q5AxVX-5VPesfuFUR0zyukeArb1TF-FgjpYxUGELkIX3BHx4wNv4atZyfduDa_aiuLBx-VhT7S7KljNspLwLF8YF-9oM2l7HkfLRAK9VEkpjLHOj1TQRM9nP64cH4WcqmzfWLH032KA-hYccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng8VWiMN1KLbP6jHjOLGThSZTkVtJtqNB5xCEZFxVFq3d9x8ksJeFNCblJ9rzenzFO8sj5SD2nVem2TuUFg9SvkxZU28FMdm9gBWzInEwSVCy0NOe-xqfoD2azTYI7w2eXKdaSbyMy25JLAb5od1nR9vp3x42k7nAiwN3vm0E0OMNk-dUKcvpetr5lOwFZ_xWO4HQs2ytH6twUhGnTRu2IDfKOuytgAOSZAs-lyMvCqTi3WrpHdQM2Floko6Us6hjSpu0E9N9A8U6bxGjfkmilwioZS3VbN1UTYmY8hgXv7x0OyDf519qgrPU3hEupoH70Wf_fZQ0pAwTO_wQpSDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=nT0r-UeI0uqDVw3GHoJc0y0CpBqwutsmOLoURrH0lquttm6s_Kp1c51-Ga0fKQc8NL1tZIaOwFwzHfkLX-kBUtJVpZ8sGrrV85UQ1KA8xfuON8sq1Q3JuI1viMeT0c8LAZzdJXUCcP94YJJyx_B03JmDpEYjBWruoylgZKUxAVB1PQM-VmBen_joG96NgqVJoU2kzIo2YhEaJmy_JjybUZt_mjQa0wgSoyHyT3NnSyb_7tfLj6G5SfaLXMMJEKK9GjnZAS8IoLRpHnRYJfNCmXxUK_HIODRe-8a9RxUr9OxU_HJnasVLLJHyu2Kb8DDYltBhS5xvN7ZzZqueEd8U3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=nT0r-UeI0uqDVw3GHoJc0y0CpBqwutsmOLoURrH0lquttm6s_Kp1c51-Ga0fKQc8NL1tZIaOwFwzHfkLX-kBUtJVpZ8sGrrV85UQ1KA8xfuON8sq1Q3JuI1viMeT0c8LAZzdJXUCcP94YJJyx_B03JmDpEYjBWruoylgZKUxAVB1PQM-VmBen_joG96NgqVJoU2kzIo2YhEaJmy_JjybUZt_mjQa0wgSoyHyT3NnSyb_7tfLj6G5SfaLXMMJEKK9GjnZAS8IoLRpHnRYJfNCmXxUK_HIODRe-8a9RxUr9OxU_HJnasVLLJHyu2Kb8DDYltBhS5xvN7ZzZqueEd8U3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb3mEi8k4mAdccX41CrdcbBUzh6lb92t6AIhjL3RYICZH0eLYXP1-YgNDfgmA2Z9_VY9_Ngt1wOg1_PNCRgAO0dQb5Fb2U8zgFKOWPs_4Wlj35NqN3CQS-mYxFV0rVgxxq5Gy8yUuljTp7hheYellZ-RLIsO-pWofMX5Wrpzjg12pHcjOYMVP5oifsGy-Hs1bUWsQqrkraSd-hgdIVleCj-VlbX5cI0x9LythmAooBY1M6hUB_PC_q6k9Ud5DQCFnYw5l1RNawTPbdxkBAqOjft_WIpqo1Ye2D3IiAp1qSLYgoojRUeYnz5podp6kSFxtxofbMETDhnoBV_BT6nbbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRlLZTYECG1B25ql-Ogp7UUNYD_RkzYIpfeGedY3KNo1vGmDjvfZxZeAJDOcvI-GCllJKT_UFtQFhASW0fH0zvu4FdisZyQaknzL2XV2JfjWIuyE4NHGsut2sM_GT5CHXgNKZDnR8gSVT2isoqfrAkpDsdIwiLk9nv9ljG3bINarE-1_sywFlH3NDdYqt1eDRFh0QRUY1X6SLkrcBWjZnyA5f9nopIO6YM6IUhWznyiHckDbljK2UmuVURMi6Hbtx8HgEMUcMeQnpvKi3JD5W8Z4l1Fd5Hcl92uc0suBe72y8M3U9y6YnN0jNuGQ9CA44rgrUZlsTOGKj4gEByBTpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AP5kFcsAqMkSTGAffyKXPBwNVALGPgA_HQ5HVOClm7XayUEnHcrQQpdDXHf7TmFbTv5lPlqy6wZY_OkaTwMnuKcyggXv2TDKucF7kgkEzCgmAxmqS-VAzsTtSWt8fsl0Jf8GTpLZyOYT67_Thj78g1qeN-6WWUCGj0wicnXv0KmOVdPqH5kMehkTftESoCu15oy9FH25xsiVVVWOQsK_gNXv7EPaLPdM1IFTaNvj0QBUBXiZLm56U-QodG9duxBh2KUWGRFBR5ef2N9p0S7MMSNl7gV3vgv1lIB9XsGEL6tS4GfYBAc6TuLyhWVtiRhji6KvCI_BL7FrnJHQvkI4zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fat4wmEl6OjeoI6Gav2R2dV7ihAWXXi7Gn_7LDgMzm62nJO6FQnRe4emBCo8UWybydIbFQZ9ZnyYV4CS4aiutWkRpy8IOODbn5EP0TPfgbYk3bFsVRLnKxuZsvOCrvY2nDcZMwgvR6amkVVAge9UweqmodjYmmPsjSR1zEuH8nZRArzXj_fiQrHN6pV6I2WVHYVaY33JwRV_WKSlLm4SiUwS19k8-zmwQ3dBboFZIlbf8l6NWBd2sMS8WcL8gdKFZL_5B7u3i4wopwUr3-J0lj3KV40CRhmu9UGCtiT4js_xGgVgOEZFTwwxjYjpT9jmJDl2r0GciyfJImdmt67_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVHhuCLbZYJMPLtQfJBdp2y0b3cawfarSJIZJur33QG5laEJ9mySRBv9cEFAIdCJEaxm7E98GJTs088Cd6Gg1IAAvgxKJX4ETgVsJGrGFbvq6gCf0QM1kkAy63yNp1--7flhLH83ec-Ie7yblgI_iLCqI3lEgrYloLiMYsngVmFLHyzT-yDUxlx4ySb0mA0uLviHewdyl6f0DcTBwm1kpc0EjxwPVCq28h5s80VLIAhSr7axUrCveFXR3Zbun77qeaBvMpGWN4oXFdcuX_RE8tgqdYyucdciYrUe0gn2QdYUEiMcXJ0B1wDmk3m3Ii-fk1K-z2orQrNpnVdAlYhL_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ8SKgeDCOcanbof-I4-RrqQXgMEGwN_A6vVwGCo0oRuEchO7vlFuy7JDsRc4uyc9OCObaCXo-7MDBj9_9zwNA7Jz1k--Vo3eVWTDc764BUntqAlA_dyBHx-JOaXpzJ-4YTjQcdTqjdK1HjsEeqfmKyrEDJlPeQSXBUtzQ-mOHVy47Rl23M0BEiadnoyyRHks8SUkE8cYiQwib6qjMP_RgS-jTa4M3HYX5VKp6SeRzVICahpqsZJSf9yXA916RvX5hwJGLYCGcJt-mjDb2LxpDgvRxNIKCWt9mQht9x71L-UeplF7NfgmwDFkDSwt8Nfj6V-zdv4ntJJC9szxrLjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhuMaOczvE1BNrla6-G7mF2Ug7nU4zCkNv7WlfoQeBq0V6A0LWxlyycIxATorCaNnjZi-4lWhfudk6yf_qV2Eav0bvcU8-QuZtAO7N-hgjGuYQyvGppL6GEmict9igpY1tirHLcpqihAWdJ2Zf9wXpgSo4IWM79G3FO6GP_oLzAPcRzcnJRlSMz4sxkYkpm64QEaRd9snWvDFKxromIyUd6vSjxbVyPqo97d2Fjq_njAsn1omEXhKzJDbSktCkzRChxI9AilNDP0wUwoeYS98naW2WP47BqK2yHPU0T_69LDGfqvEyecgerO_p5BORSzsVzgK7ZZlH921H3U9LJUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbEu-eSChe6TTvYtgu38oEH0fPH5grtsFfv5HSdJgTcarCceyLRCZGx5BYV9JTxYP9lmoqCas42Bb8Y-2oeY36WFN4d0obSkCZEK6P_oCpJRcW1aO0yRDl3wPP5m-WG8IIXa77SY4X_dRtt8agTW7rgOJzxalbfrK-Sk95E3H4Db5Hwi57luaYfvee_d993AO7QwuKZDzhYHZYGUd1ZFceZUn9oBksT0Ej4qSQqRg198c0dPk6u746xB2Njytul6IBnuqqpoD9jwKCD0fShMwRxUGm0iCFkH8iz8sgMudLB28u3-VTlnoCDyZ6Ck38x8KeDwUtl5EOK-oqbbkEKE0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gke5809875nxfNhk5L4ii1fZq9HmzKJppHlez9KsrW1tOXJG5DP-_xiuCDTxJzS5T9HR1lH_EmiowgoyKEJeNnQd0ESe_OvizlhnDOVxLhhmb33uEtD3Ive6Pbo1dpTgL6u7N4EKN9SU3XCxc6Uoz-EkyX-vT_T9oTCF7oJwku1OMgl9mr9FActvOPSaOi-bAF8fIWNHyMZorGdhpDOk8BYY2gRCIeIzEIdtTEPMMp2XUJhTLM7lTnne6g5tj_V50jr7maftu_LkApa-3pz3KrRWlgjQuU5mKCEAf7uoEa4sShaDHu47Q_oZ5sxwu-e6SNVDRflqFqgI6zq8NMA98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=jejtCn4x0yYax8RrXlFGHz0RtEEtbInzYtv646-88JBKqp23wxDm_xhPb-0OB3lJu0IwAZrYG3fLyxiJZT1LGCcfVi6qMVocvZ-csC2xTOvVrJx6SgECgGwrGsiueP0e5wffJ1Diz53i-pZq14N-kFYvU7YMjO-edJFOotfMPhAwhIKFkn4BDI83ymmPgs4V3963e-kvVCtf9HNNMoMmIEoZ-Au6mhA1GP5sBN6RNNJaourKy1XIqZc8SlK6EdhB87DNCF-v4RdcBCRavzrkvHriONZ-xYPG4CP1_grEtIvqlCE_Y5I6cs2h0W3-H7wMaqMXTqXq8eZXQdWKzshPxHAPTQeQOoo0c5sknJ1YNLVvFIBR02gYaWtcmmkJAjyJ4NOZLCETJYMsy36vLGlf49trytWBaRQn6uIK06Mz59RVkvfE-awa3U1AmdxS_0-6rl0oFiyfYh3YsK_0Jbivx9cQu3dZHQltyS_EDat4Hmcw5rUfDXWAXS5VoMi427mC2HHWSUKnpJubD7delbKbERtFtUhb-qOq3kxH2bEqPM0kR_dWcQeN_YwIlo0lIfbAog8Z_ws5MtBIsvghUefGZ4JdIhRo1hPRZjHzUzG__suDI2t440EzZqnxBWbu6LnKDgaxp027W4itmsoI3uIYZ5FY8nqkKxVaj3GGuFh9BV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=jejtCn4x0yYax8RrXlFGHz0RtEEtbInzYtv646-88JBKqp23wxDm_xhPb-0OB3lJu0IwAZrYG3fLyxiJZT1LGCcfVi6qMVocvZ-csC2xTOvVrJx6SgECgGwrGsiueP0e5wffJ1Diz53i-pZq14N-kFYvU7YMjO-edJFOotfMPhAwhIKFkn4BDI83ymmPgs4V3963e-kvVCtf9HNNMoMmIEoZ-Au6mhA1GP5sBN6RNNJaourKy1XIqZc8SlK6EdhB87DNCF-v4RdcBCRavzrkvHriONZ-xYPG4CP1_grEtIvqlCE_Y5I6cs2h0W3-H7wMaqMXTqXq8eZXQdWKzshPxHAPTQeQOoo0c5sknJ1YNLVvFIBR02gYaWtcmmkJAjyJ4NOZLCETJYMsy36vLGlf49trytWBaRQn6uIK06Mz59RVkvfE-awa3U1AmdxS_0-6rl0oFiyfYh3YsK_0Jbivx9cQu3dZHQltyS_EDat4Hmcw5rUfDXWAXS5VoMi427mC2HHWSUKnpJubD7delbKbERtFtUhb-qOq3kxH2bEqPM0kR_dWcQeN_YwIlo0lIfbAog8Z_ws5MtBIsvghUefGZ4JdIhRo1hPRZjHzUzG__suDI2t440EzZqnxBWbu6LnKDgaxp027W4itmsoI3uIYZ5FY8nqkKxVaj3GGuFh9BV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMf5l-iuYw6QmTUubhE8yBllyb98vLy-PGuoJqm6CzRck9yNlNfrITmpY4UyrhcPm5XRoHaq3cqGSOQimXeGwgIngMyci_ju2btR1BKD2tr1yybhJQPEJ40dWCQgSE0tC_nneO8-IvWqvh6XVXTWNs30cQRberTKbl_kXGrsfGgfq_jJ3uJWwBHjm4mIafXbycoZEaDpD5JriA0ZGP4ZKeotw3Pp1kesyGZC-mdp341bd0s5_C-Wja8934AHCU57-texEPvSjS4FXesEUHPk1ClKfasYfd4S67lK7yIqmXy3KCqd_RBsfG1_QvGq85yvXQkQ6W9rzVAO1m7rKvmp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6Vq1kWxqATu_wY7gS3cqZdML5RmS-ULm8-wTOHfSFrToCgSibZLsYu7d7vPHcm0fINeCSrhT_ft2iVhDDao9Oy-eY99ljAmFGZ7BqLbsstHocWD4Ldt7Et4j4V-29yNF0fmyucKyv3Ess0hKKUYywCK4pOAeko1psVpLNmbR_7b7F_YUxIhLHPA8iuWJsOghPgM6Uw0h3iCn5vS3ay6BtAhsFvIo1RwXrQAYlR-q2AZYdlO2yfhbMRQoFKJnbfi2yVC_x2Mu9WLFzAU4NGY0ouN8b8bfVdU1SB6utOe9ew9Cu7o3phpS28aPzlAM7Rf1LajNtM6bS5Rxk5yVodPEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0ggiudxYpyPIOfff-4DI9rwz_Y7DI1BV8ZmJJagbZ3n-68ZmM478BjFwOkaHoiula6NZ-1UgipgpmepkaP4_cOMXnWVOd_fnrRo48pVlFPJwGPHGMuwYm088ZHTHfjUwFQSsEbpxz23R9cdpO1CPXS9sL0ubRL8Jqq3rEhub51K6owlggGBlH09AGc9JErwQcfwV_CDwlXdJ1MHDBGkueTDFLnvZ9LS7q2C0DlDeFUOccmeEBHnvczOXdfsnG3iaCe2I648ON8K9TyyEGYkKoLaUzcIAkIa9cu3RsorMCZh0UySh6b9KeO5RJCq3XAOhlhyK3rezixvbxqYHGI6Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=AnCyO0EwXwlLT4KpMOsV6gq6WBhvGz3obmoq4O4PZNraUP9UNHPZn4p33xIXn-gcBgSO3JV2LBKwlSFE8cn2TI6ymuU9pdDjsINXcuM8CZzpRiNmmF006XSConkoLpa9EuyxZTpN4Fe43_BhC4-yFHAbjlGYKY71I2h-tfNr62gjJ4ISBYEOc6uT_Xv1UNu4Lku5m6Tf5xX9x4mldMPJ8FHBxkyyYHqcslFNCR3scA3EDNgCCnfvZXgRJg7QZumJC5JzSHPchLk2xRK6H3q69kO__PguSO01gG2lIjqeB6-Nw1R5PdWpEQYQKyf3Aun6OBahxYWfRydnD7NHP8MqMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=AnCyO0EwXwlLT4KpMOsV6gq6WBhvGz3obmoq4O4PZNraUP9UNHPZn4p33xIXn-gcBgSO3JV2LBKwlSFE8cn2TI6ymuU9pdDjsINXcuM8CZzpRiNmmF006XSConkoLpa9EuyxZTpN4Fe43_BhC4-yFHAbjlGYKY71I2h-tfNr62gjJ4ISBYEOc6uT_Xv1UNu4Lku5m6Tf5xX9x4mldMPJ8FHBxkyyYHqcslFNCR3scA3EDNgCCnfvZXgRJg7QZumJC5JzSHPchLk2xRK6H3q69kO__PguSO01gG2lIjqeB6-Nw1R5PdWpEQYQKyf3Aun6OBahxYWfRydnD7NHP8MqMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjI0alOKeBJru0AJk3pwqNm2_CFJmb-8CUkjc1OG576yRcSa0T1j6SED49Vm7gSRf9EyW7wDkR9TPhEzSfq9w9aIIwOyn4_bL3DNzMrh6aXWGDcs9RS95NcnOm6CmIcNFeuqRGsdasyiZQpbjTy7X9MZ76tRUA40YFgKzKk0qoaMGm7r7vkEPg0H7JzicoxhvuLnzLC95yQJnI5hHwztOCPHvtGWceXc9Lx1Q_b2P6IfD68ETGfYdSdr5dH1twOYG_s3rJvLaJ-GJ1luHP3g_3xX8UVhXu7JYTaf0Zg8rCF561kO-2_F8MeiuzHHLHzJW0X1BURQIrWOMERWHG54HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIpEGrut_1OAANAn98PxCcY6QoUg3AUK9blHsT7AtHIK-s7oc6bkJWQ6IdHI_SlDyIMgloS_VMyUghH0dxByMZhP9p8XU5oLnP-_0EnoXr2xTgxvJVa6sUsq9Eabc3kXBAYxzL6deRowVq5nmLBLR2cjshD2ZG88I-egVNonu3Xw4bFFREIeKa7ZEc3EvTqYQ4JZcXvNGzj-4ywXvIdu3oSTsTdh9qvI12HHx9lr1BqhYcU86sld9qrnD9GEYs0EC-8E8T8RsFu2imwq9_vcIfs64yTIdKZHdmOmm0CaMR5yKCKUYGaq6RK_lQZfJYGBNkO7mhDSVY0rppAiSva8hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlbRzFAWp5oQQ3soKC_ciOlUrCHxQQ7j0-nP5gvB-URylAaDV_bLAnND68UBRFR7X_SE6VM77cjV9CTRN93eu85VMqtU9R0tNbUrusdUqW1CgnLtyZWJYNnDdeXmSC1o0qtH8kCLo19QKaoK2fWf_otz6t7INr9INlE7ekEHXKkx-1TJDj4VRnb__t5q3Dj6ONLjq2P6uHNiAq_9C9MNQJwSz5Jgn_dcOD6f-D7CMUFajchiNAQJmPr0cSYG5hkn4O568AubY0z88NnCRgzvtT_rpNu970Yd7E4NRrC8x0vnFtfuF0NiPhKYnFxXHhANXJ7QUsCGTkL3FxCw1xU2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQ9vQ6qs_Br9qcHiEyEoQWKmMlGCv3guou6AYz9sOf65rlmEyZGsEbw70RPzQHExsreycT9VYyG_KDgYA03GJumWFvrKpPeSia608kSZMavNnx5uigBaqN5u_o5XE3Z7XK9RrJgfo4VqwY16yt_N9x4dmOSiR3OkbtRkQcja8lbo7TMww45HTV07032atC3GOSCJuvnr8uzj3vyT-GRhFX_oIOnTFvKOLGcV2f9WPVzihqzPznWU-nPe8V5cacF55galIIiJ1N0d1arYbIroNqN8MoeeYxt5FdzHZmys2FE5pRSdc-bLMGGeH6vMKCEKDeMeVIsSZLfDNLK_m6Zf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SprXqiLikI3SqdGJO_d61e4vr7bZuEkM6Njqo8Oq27xw6j4ZGNF95NmIcNGJoatdLTeKtJhbaTfdUcg_tA4oayl9v4EI8kQCKxoL91H8qKYuObKEziGWIfHw8iFzWcp04vV2-pqxFSXrCWTztRHxn0Jn9m73Lg39q9Wft0KcoJ49FpAcn5t4hMSWdcxdZZpXiKbHcVVaNFIY5Sk40d3p6Ldm_hLZmH4vL7uxPFZSZwhFr3RfSLci6bRZLszB1bhlvWtUAGYRQSJWWvBW_jp8aUH9cqVxwvWCWlnZPHpqRp0UFWDqZAoNdWVznqdrLpJom2GmfejYH4n84bWcOgYkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPJcYrvXx4zYsKSZKl3LkMNqJ1T486wu0fRrQafJaJTodfeRCNJ-MM2WW9copAKWViwuznMLKnLzvcEYS3dqoWeRXZ8YmGbZkxae1y2if5wtTiZ7GTUBaf6eiVoTtGx0TYJjxsXzDcMp5HOxoNCtkqF_Lc5EU1gaD96RcEuNDIev_tMpUrQtum7SO26K8ibJxafCeu3mjmeDtGHZq0ftL5Wv0FQlhGnrGffNK2wQN9X6idNqzn9k6BxwwPl_QoOvDffeEU0zOmr1PwlXmyJP032nIFrxiiaE1dfj0RgwMP-P5yTuB-6tf8zLrUq6OaCDPFYTNgwh4QhOZIBdHAp_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY6pwQqrEnCrPQ-tFl1bF2gsV_gdamvcSQiqL9w0DnyS43D78gUQ1kgKbg0zvQZarC0yMRHmDpoMmyecCBW-ZxjFlxepOCKv96t11gfh3dy-X6M9P3Oqibwt9H4Ya98vWDQv_MxTYMaJiiZ3rejd4fBY6HSrn0BcJ3F-tjkpNu_DE3EOeerraghzlTOaEn9u3BP_V01j0InyXxLrO20ff1FlyyJUPSxAa2uNpQG7oFtaMWfghVFBEl9b5rrdZ93SZdjqMp2z0i7nzgntiCEp9fCGV4Wkys0zGG2k3Eg58bCyz5hxQ356XyLBqbq0eFSCTn8YaXy1SmbNQisMrzkIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABiv87vygVofHPz6SAYVrcZynpV2Xceh1EpG0vEuIMC7xggUTmrkrnPJfKY4GewLxzIfKF65SpI97vjXLOSbpveuQfNUjIBwwwzfWGJ7i_Z_D8fPidVHsX5eyLQh4m3FkNxO7S6rUjF1PeJhsD5qSLo5AKNu6Dg8mjUcJKpaIt2GRu8adHtYSPEen9oTABa18rG7VHtsRYjLuNQLAqGJmzY9x7OPfj7oOAF3aLB4oRxuU_s63nW8nIaPkJFAIZl5mzf8MRHqb-kVNnPWBfnGNKuSVmzJ7rTTHhpdEbHnEchPwiapnFz3ZjJfk6N9hC5VkvZueTYrrTpsq43Jp075dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
