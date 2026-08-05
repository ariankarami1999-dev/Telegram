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
<img src="https://cdn4.telesco.pe/file/PSwJLHpxesUkD5ih6mphrrBGB6aQkIzBiSYi8-xxfG0aSiwRDubvV7WnnLyzM6HpOudFGNYwIvNgsCTQ1vU4qBYBqz4DU6picqbjMRVFy15dYXR0hI1sfMCagDmQj1LiTlgVBvpfLbaJtc4TnR6JoyDoAmhtpI2FsmRBQhQ3yi-RjQzb4bH3JgUrUKvLQRV2Bky9E_0ZfrL2V259TukEu6wvRTBiqEYtTWLHD-M5-dc0Z9Hvjr5X4LGKT0pStvxPJ1OIMV_skH56flQiFJi5YSLg3giMgGCzyRVNCFWkG6io7U07YvV1USGb8GF3wao3X6kpg63b-oAb163aqCUoog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 13:56:31</div>
<hr>

<div class="tg-post" id="msg-678631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c47d2a81d.mp4?token=swzrtlY_Dko0AhwD9j8MTU8QT2CvfxxOXB3h9n0hcFpSXWXFI1T6P30Owp12unZGdZhXbwc_gMtlrgv2-jymrKg4wd3pp9IbgNLqmfeGQS47nfZ0nl7EqRHDUw4A3FpOGejdmZWvZzRK0Fg7zh6wvIaDlDPt1k0lNi2behWXq9-7TKiqREVuDX71rnPIQVCQ1ejBYMoGpEGfMn0XXj2wyIu8Bi3vlZumTy_JAiPXt5feUyqc2nV_dDXagmicpnW1XPlNcZbQuBUiC65LUaRDf19lYKdLodlsvAxRcC3429usQ9Dw3SnyUWcKQmLF1NebTmdRie488YYM-ost7-cjyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c47d2a81d.mp4?token=swzrtlY_Dko0AhwD9j8MTU8QT2CvfxxOXB3h9n0hcFpSXWXFI1T6P30Owp12unZGdZhXbwc_gMtlrgv2-jymrKg4wd3pp9IbgNLqmfeGQS47nfZ0nl7EqRHDUw4A3FpOGejdmZWvZzRK0Fg7zh6wvIaDlDPt1k0lNi2behWXq9-7TKiqREVuDX71rnPIQVCQ1ejBYMoGpEGfMn0XXj2wyIu8Bi3vlZumTy_JAiPXt5feUyqc2nV_dDXagmicpnW1XPlNcZbQuBUiC65LUaRDf19lYKdLodlsvAxRcC3429usQ9Dw3SnyUWcKQmLF1NebTmdRie488YYM-ost7-cjyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: با هزینه جنگ علیه ایران، می‌شد میلیون‌ها آمریکایی را از گرسنگی نجات داد!
🔹
هزینه واقعی جنگ با ایران بسیار فراتر از آمار رسمی ۳۷.۵ میلیارد دلاری دولت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/678631" target="_blank">📅 13:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa54ce8da1.mp4?token=LVlrRIp5cTFDCChkzJxultIVCmEKIrC_t3GqXidSMCVErLSMsX6J_MsiLURIdu7JksMgTDm-T3TzYgB3ZRfsaYBcw_ekpSMM-gHWvjkloQ7soqDnG_6LWAizvvhbB6_U2RrMgQL5BIVxBN_oOC_ff7gKIVtIf_v6NBtGFwnvYQU0lLxIZuuuk1uLPI9oStH5CO3DIZqCD3cjieTcANX-mQn6z7ak2g1j-syW7zg6BppqIbVxA-bBSg6E_zZiR6Ii2k8LCmIZpp8c2XD_Zwf7PC9mk-1NDSzL-cbLLh58h_cUfht12_B34UjM2CFtUQhTRfiIvl05TYrgOIKyQhfyxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa54ce8da1.mp4?token=LVlrRIp5cTFDCChkzJxultIVCmEKIrC_t3GqXidSMCVErLSMsX6J_MsiLURIdu7JksMgTDm-T3TzYgB3ZRfsaYBcw_ekpSMM-gHWvjkloQ7soqDnG_6LWAizvvhbB6_U2RrMgQL5BIVxBN_oOC_ff7gKIVtIf_v6NBtGFwnvYQU0lLxIZuuuk1uLPI9oStH5CO3DIZqCD3cjieTcANX-mQn6z7ak2g1j-syW7zg6BppqIbVxA-bBSg6E_zZiR6Ii2k8LCmIZpp8c2XD_Zwf7PC9mk-1NDSzL-cbLLh58h_cUfht12_B34UjM2CFtUQhTRfiIvl05TYrgOIKyQhfyxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران من دور از تو چشم بد عشق تو تا ابد با من می‌ماند
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/678630" target="_blank">📅 13:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678629">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f827818fc9.mp4?token=L0ZsvQnbBoORE97qLOGan_Chg4pzJOpDc0MzW97K-i0P0QQj8ey5ZTIr_z_z7-U1vOBcNuDBxN5solVTSpQKf5ep7QRUDrytchmdXtKigYuDT74I2L4lrEr45VJiZ5tos4B43bm730QsTlQxEbKHtaaUzGz6v8pTpQLzxlOubPV_UOdzrvnsYQbCzXKU8jn0y6-le030kzPyd3p5jZ4GvzwsO62_iwp3tl_bNdtkwEJNfnosmf9iT78FLPWHrxovy4jkFc8HT24mkl5d1jhp1ObkNxnwRsngUqu8ghsJfJ5iP2ut8fkFbuieVMWrtutCRXOPHn8nLFimVxihim1ub2AJxFuo2Hl_SiXpK67vjry7SjnH32BC901yG6cgv2VL4Zp3NuQ5mfTNpZNqEUuPNZQ3jBtJPF5PJG4ZW2T-q1Wuj9lTtuWOxpFK2NMZ_JCFix2Gqrlx6zJ4SdO4mDfUzae2cSVVXlDPtcB-JxzKacpp_cbx1tNz9re6YZ78Ei3gRz33fDZGfCvwPf6D4LiqOPGHtBKhSpwkD7WpI5EIQLuPW5GvxSLTBL5hDeGzqFYMvHieFbS88LTghQ9zfp0YISmEcE3PsGvLr2DbCnPZswbQ128sPzA44yV10h1oGHDrv6bt2GXsqDrrnQ5sMQ0ywpH_YweHbHYibZhl29aA4rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f827818fc9.mp4?token=L0ZsvQnbBoORE97qLOGan_Chg4pzJOpDc0MzW97K-i0P0QQj8ey5ZTIr_z_z7-U1vOBcNuDBxN5solVTSpQKf5ep7QRUDrytchmdXtKigYuDT74I2L4lrEr45VJiZ5tos4B43bm730QsTlQxEbKHtaaUzGz6v8pTpQLzxlOubPV_UOdzrvnsYQbCzXKU8jn0y6-le030kzPyd3p5jZ4GvzwsO62_iwp3tl_bNdtkwEJNfnosmf9iT78FLPWHrxovy4jkFc8HT24mkl5d1jhp1ObkNxnwRsngUqu8ghsJfJ5iP2ut8fkFbuieVMWrtutCRXOPHn8nLFimVxihim1ub2AJxFuo2Hl_SiXpK67vjry7SjnH32BC901yG6cgv2VL4Zp3NuQ5mfTNpZNqEUuPNZQ3jBtJPF5PJG4ZW2T-q1Wuj9lTtuWOxpFK2NMZ_JCFix2Gqrlx6zJ4SdO4mDfUzae2cSVVXlDPtcB-JxzKacpp_cbx1tNz9re6YZ78Ei3gRz33fDZGfCvwPf6D4LiqOPGHtBKhSpwkD7WpI5EIQLuPW5GvxSLTBL5hDeGzqFYMvHieFbS88LTghQ9zfp0YISmEcE3PsGvLr2DbCnPZswbQ128sPzA44yV10h1oGHDrv6bt2GXsqDrrnQ5sMQ0ywpH_YweHbHYibZhl29aA4rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرشایمر: ایران سخت‌گیرانه‌تر از همیشه مذاکره خواهد کرد
استاد علوم سیاسی دانشگاه شیکاگو:
🔹
ایران اکنون بیش از هر زمان دیگری از برتری موقعیت خود آگاه است.
🔹
ترامپ هیچ گزینه دیگری ندارد. او هیچ راهبرد نظامی در اختیار ندارد که بتواند با استفاده از آن وضعیت بحرانی کنونی را تغییر دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/678629" target="_blank">📅 13:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678628">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H69NYRMCMpTAJKQxFPG8s6DcJJAzTnQNH25K1yZ1RtAW0fKA25LwihjLQa-YKJkNe38ZySvxp-2slT1TA1PtBL7GOU9alSIwQuvdaecoiPfE8Pxa48y5Tw2KIWrLMLdjBSKEQmT1TRCl2ubTK7q9LxDEZPjHETzCRA1iYDGgiXDP0X8SQf-s866kC4xJXo65dE-V0T4gA3jnLvfCLcYt1hoDTWf4LZJNResjshDdJeKofdpcq9ZyhWy312Ptjq1nRqgXaVCUfbpATxRwkNpWIA-jZilyGwoUji0TJu0If4N-wIspVJLYNYLahA9W3gk2duys7KPV8UifgCz9_2HvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به ۷۶ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/678628" target="_blank">📅 13:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678627">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL9JVluWFOpT9DBIBHE3PubBeKdLSeTT9hIIgZuQ6kWs4UAo2wzTrcFEBLBimhRH-uYNOGrQ-qejx2rWu_or6lTO8WzW3y53Q2NhdcLBXXSndgGgDnHwvDFRjMwoZH_i_dlxbTB1nQESvwml7tZDCXoA0LBDMoUElXN-GxswlvBwIQM4yYEA5Nb-9xU4eJSlrG0amhu_xf642mySm0pX9QhrR_0EC4SDfQ0SL-DE9BQlt8O7im-dZqcqvFHD4RIbUWTDnKVVIh7lKEppKG0YpS7GwwFPDhE1In-POIR0uLvNGoNy_pKCQBAzfi3IolseF_IxUdqZqeRtxBuN9LMHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به شهرک «المنصوری» در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/678627" target="_blank">📅 13:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678626">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
مسعود پزشکیان: از هر تصمیم رهبران فلسطینی در روند مذاکرات حمایت می‌کنیم
رئیس‌جمهور در گفت‌وگوی تلفنی با رئیس دفتر سیاسی جنبش حماس:
🔹
فلسطین هرگز از اولویت سیاست خارجی ایران خارج نخواهد شد و همچنان مسئله نخست جهان اسلام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/678626" target="_blank">📅 13:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678625">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGTUXc2M7lf6Y4EbBKnjYP2Q6-2U65uDV4uP3b2V6oykgwnpR60IZXq1tEhHMdhtMuuKG183hkxa4j-ZfS6xOksDP0ib5hxo-4SiBNq-hlir17_vhl1ALShkSPrylCtbZBxtT0uj49-sQmjB-sekHfEusVH8XVbw2_3bcSPCfu4wBAKzg3HyGFJL_I1rMID9rq83slFRa48fjP8cSF-xzMSzB7B6cySJhELtBt7Z4T2MPg5AcGN6qkdA7ay-3wYP4-C5WN9L1ZdYlcn7UJ_jjk3WHRFbkdcAuFhKpcAFrjBTnZnl_-e9CIYOc1pc29ZAs3E_vyGLdJ_Z2T57eZpJLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی محیط‌زیست هم از ترامپ در امان نیست!
🔹
ترامپ با انتقاد از فعالان محیط‌زیست، مدعی شد محدودیت‌های زیست‌محیطی تولید نفت، گاز، چوب و ساخت‌وساز را مختل کرده است.
🔹
کسی که حتی به حیوانات هم رحم نمی‌کند، چطور بعضی‌ها معتقدند که قرار است ایران را آباد کند؟
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678625" target="_blank">📅 13:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678624">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ان‌بی‌سی: آمریکا شیوه استفاده از بمب‌های اتمی تاکتیکی را تسهیل می‌کند
🔹
آمریکا قصد دارد با تغییر راهبردهای دکترین هسته‌ای خود، شیوه استفاده از بمب‌های اتمی تاکتیکی را آسان‌تر و مشروع‌تر کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/678624" target="_blank">📅 13:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678623">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه نیک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIyhmY530a6vYJ1W4B7AacKui4DR4c3Ke5Aj4EAIcx5LnwGdwLkISQUUfRHIJZ0wRdtle_oaXR8qXLEU7aCYL7ASdkCMwVVK7XpU4n47lSbDp_K3PQ9klGHzVkkNM9WEJJpx2hsoEuSnqD_havLF1FIHKAqOEUiQAdZcNw2VLzv3AS1buCnO7Nvve316fAuuWWy0kCMq3LHXmCA9kYlSu727hZ07fLbthnkx5L-YRBQOjmd2vTcpN8aH4JWJWX0Il1amwKPgWMsSh-75C1o_Prxg_Dm0GbVRTAk07A8_6Iz5VfG7fY8s7LGucE05KTKQa-Yobp6M6sijeU7gQvk7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فقط ۲ سال دارد اما روزهای کودکی‌اش میان آزمایش، دارو و درمان می‌گذرد
😭
💔
او پس از پیوند مغز استخوان، برای ادامه مسیر درمان به  داروهای حیاتی نیاز دارد؛ اما خانواده‌اش با درآمد اندک کارگری، توان پرداخت هزینه‌های درمان، اقامت در تهران و معیشت را ندارند
🥺
بیایید دست‌های مهربانمان را از ارغوان دریغ نکنیم؛ شاید کمک امروز ما، سلامتی را به ارغوان بازگرداند
😭
🙏🏼
🌹
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
6037691990491185
6280237094218423
IR
110190000000216777746001
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@Pr_nikcharity
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/678623" target="_blank">📅 13:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678622">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690251c8f1.mp4?token=XJd8ChcIRGdZHzYs7TDGpgA-egudjLD4_0lbJ803nIF1F367m-Pws-FMZA6yXqG_Onmw2Wvf_WciNaL0ldw1gf5t1DDeO_kZHRc7fEE9iNPdNT3C6e2r4mEwwPpRGrSwqgNua59umx1Gb4ioWs-QDLZy5eaV1yZz_ALWEaKDAHF4aZKVmzD0JX8B4CO5EO3yqiEjKB9T4im8L4YMotU1zthTeCFk0y_1cld26lc7ZuufZvpW8EA5ZcyMXte5AjQJVocl_giqOvmmZQ13Cmd9RWqGCtWlpdoI8mp2ON1hqDJlRig01LXhehMClhik9lAnU5OYTCdv7tEf3rIZ7oWa1JPclnKs8tgX5YKMSMpWykCbYQk_5imriLvrjSkvSgLPRZ7jbqhZSAqfH2d8xWAWjzxsRlsI0vMGv-iwfA1eBeWpQVV152wGE4pTrCjOnPW868iSn-xEZkBJgXeDLKTJGmZaqbBKTmaSTHeXpgOKjal9i0vj5bkoJPGIYXC-K7OhvrdVY0VBNWx9R3n966OMybMvDZf-fUBxeAenYJtngZSsx-mluDTeJ6-MzNdsBO73UqimBEXVHJ4FT9bufgiEqL7y1ojFrMUjKteKerc6XtoZS87xWbIPCCc1V9qQGXn43v_ezIKzpapHKMTjgaCo3FVj2okg7CsR4F-BrmIV2U4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690251c8f1.mp4?token=XJd8ChcIRGdZHzYs7TDGpgA-egudjLD4_0lbJ803nIF1F367m-Pws-FMZA6yXqG_Onmw2Wvf_WciNaL0ldw1gf5t1DDeO_kZHRc7fEE9iNPdNT3C6e2r4mEwwPpRGrSwqgNua59umx1Gb4ioWs-QDLZy5eaV1yZz_ALWEaKDAHF4aZKVmzD0JX8B4CO5EO3yqiEjKB9T4im8L4YMotU1zthTeCFk0y_1cld26lc7ZuufZvpW8EA5ZcyMXte5AjQJVocl_giqOvmmZQ13Cmd9RWqGCtWlpdoI8mp2ON1hqDJlRig01LXhehMClhik9lAnU5OYTCdv7tEf3rIZ7oWa1JPclnKs8tgX5YKMSMpWykCbYQk_5imriLvrjSkvSgLPRZ7jbqhZSAqfH2d8xWAWjzxsRlsI0vMGv-iwfA1eBeWpQVV152wGE4pTrCjOnPW868iSn-xEZkBJgXeDLKTJGmZaqbBKTmaSTHeXpgOKjal9i0vj5bkoJPGIYXC-K7OhvrdVY0VBNWx9R3n966OMybMvDZf-fUBxeAenYJtngZSsx-mluDTeJ6-MzNdsBO73UqimBEXVHJ4FT9bufgiEqL7y1ojFrMUjKteKerc6XtoZS87xWbIPCCc1V9qQGXn43v_ezIKzpapHKMTjgaCo3FVj2okg7CsR4F-BrmIV2U4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
چگونه مجوز واردات و صادرات بگیریم؟
🔺
کارت بازرگانی برای انجام واردات و صادرات ضروری است. برای طی کردن راحت‌تر مسیر دریافت کارت بازرگانی، ابتدا این ویدیو را ببینید. در صورت نیاز به راهنمایی، با مرکز تماس اتاق تهران به شماره
۱۸۶۶
تماس بگیرید.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
service.tccim.ir/membership</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/678622" target="_blank">📅 13:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678621">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUrdv-fkvKW-SNdp9FkGh0uEVQCKZtZj5DSeb5-TCOkQ4-SJdcJ7uuYCJkAm9KeevGtvQEzdjUSAZCDxEJPGtsCfQmwj-Ucd_pFlSMNyPX-5hJsPSc6vn7DF3I4p4B8KvQZIoKgw4ANB6wzLCdoPFDtUAeEZEpqezr99LjEp2j3OzbkwFGAR9bk6Cu0HS27W6WkrxWD06hSy5OKKr2brWvssFwoi63wnlcmc9Q7-Z5pd5khw8KP2dbNbXdHN4YoGV28VsLVawrDpZmYA_zG7TSQHHuufdQsjxAbrKB17M4LAIv4-T9_mk10a5aZhmOzcAC7U3_bvWBSDGZnvEFaRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با عبور از ۵ میلیون و ۴۰۰ هزار واحد به قلهٔ تاریخی جدیدی رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۰ هزار واحدی به ۵ میلیون و ۴۰۸ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/678621" target="_blank">📅 12:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678620">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvo4hbk_TPuo07e4bwZBL8eKLBpfZYiDueb4IwIi6AgaAcifC1yc4TUJQDgrzMBQlKXsLJw0kSJoGvbolb9jpzbtoTYbvqcmbSmkuiOeqs1R2Du1v_wzctzi2jWcV_y2RYrArYEnuzApDYwA9F8YuGDsudSBu-35u8dw4v9QEP-n1I9lQnB4REqmL_DclhEYKesTPJTgc3qC8boS0-S8RRk7OZHQ5yhsDfOUCJ8carabf1giR9qQ9g3ZE7tRIbbWyOugHbTNm4499MVdt1IddIS6L_KK8HC5YUOePNjIUbxOLJ94Vfgc2SUILY-L-twFPccHGra3SY6kEh86jnQoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقرار موشک‌های کره شمالی در روسیه
رویترز به نقل از اطلاعات نظامی اوکراین:
🔹
کره شمالی در حال استقرار یک واحد موشکی در غرب روسیه است و قصد دارد ۱۲۰ موشک بالستیک و ۶ پرتابگر در اختیار روسیه قرار دهد؛ ادعایی که در صورت تأیید، نشانه گسترش همکاری نظامی دو کشور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/678620" target="_blank">📅 12:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678619">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHWkR9jIcS2EhD19DFIYtXhPFVZmvUQH81Kh6T9Uxn7rSG0x7KeOEPjwFi_dOL7RVfslpn8PDxU5UCsITI0QNmxeOdlGPDa_OBcsmR_6Xbd9Gg9MLBonVs6DoeJtAKwoRhKdoaKWTE6ES73DgRAkV3UUqYAscBYSvIofeda_obyGMNQlv3g1o7zYeFvbGDIaYIGQibqnzdlBr6N1s8VPXH6JvGBTK0qfDEJjNFM_0OCsp22D558wcfX_vDjAoQ8wWOfmNGccvC98OIi40c3LzXuljuBIna_10pzWJVVHFGjFxLfAriERX7QD0PIYXv2SiQxTFqrqoS-apEHkkFICXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آدیداس از کالکشن مخصوص حیوانات خانگی رونمایی کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/678619" target="_blank">📅 12:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678618">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
کالابرگ سه گروه فردا شارژ می‌شود
🔹
کالابرگ سرپرستان خانوارهایی که رقم انتهایی کد ملی آنها صفر تا دو است، فردا ۱۵ مردادماه شارژ می‌شود.
🔹
کالابرگ سرپرستان خانوارهایی که رقم پایانی کد ملی آنها سه تا شش است در ۲۰ مرداد شارژ می‌شود.
🔹
کدهای ملی هفت تا ۹ نیز در…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/678618" target="_blank">📅 12:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678617">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/832b1431db.mp4?token=ZkVbO6_EA6C4HSbTrOmaaE9m2RkFqWhwPf2wBH9Wn4_FNxesEmyaITf2TWPj2835CXuMJanaMCPorRBp6x3FwsRp2uPJOsfjA4MjSKMk36SquzruVE_Jrvf-qhi_kPWlQkoOFKkWsRn4WXTBUoQhUcsxPS8aw1r6yvYMnScZrk7ubtdOeol8sEmwta_NrfVl6V0uecnLTvDhLNyZKz74ca3-077HbOH3ED5KbbfynY-PXUrp961KIJxflhyWbSK4Fkqio6DgtjRfjuQsl9V-lzTqunDGP1BUgWLvFFYt8x58S56gtQzsuj74S58etCBdd3Kxwwdk6asqMRDDzzQ7Dpl1YzyidlD1tCdk-e8xozJ1AwA7Eg3c4xDBGGRhfFPKR_IFTlI-RgiNdnTy8HNIbxKzDQIDUynVHFts4KnxDGb2IDTPTwu6s8jfcdFhjuv66xq7pP7SjDC6zzDpJb2z2IiRCvQByXnTJ1vUZKeT2hG0nbmqCxH3CTEAgI4IfUFTeUWzoDQT6XOi-aoM2EpbiWaxDByw5OQqyBRcGT9g3eE1KvnQiL1N8Nl44MmJ0qpxIZMlOiC15W-sxaN8C1B9ZYQgEcIOHnd4pbxZdAjd-5suNvxtda1I055vZTdb5FM4Wg9yusVk5sbkIrUWATMTVrlxvwsdOEtepOSfMkQjEUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/832b1431db.mp4?token=ZkVbO6_EA6C4HSbTrOmaaE9m2RkFqWhwPf2wBH9Wn4_FNxesEmyaITf2TWPj2835CXuMJanaMCPorRBp6x3FwsRp2uPJOsfjA4MjSKMk36SquzruVE_Jrvf-qhi_kPWlQkoOFKkWsRn4WXTBUoQhUcsxPS8aw1r6yvYMnScZrk7ubtdOeol8sEmwta_NrfVl6V0uecnLTvDhLNyZKz74ca3-077HbOH3ED5KbbfynY-PXUrp961KIJxflhyWbSK4Fkqio6DgtjRfjuQsl9V-lzTqunDGP1BUgWLvFFYt8x58S56gtQzsuj74S58etCBdd3Kxwwdk6asqMRDDzzQ7Dpl1YzyidlD1tCdk-e8xozJ1AwA7Eg3c4xDBGGRhfFPKR_IFTlI-RgiNdnTy8HNIbxKzDQIDUynVHFts4KnxDGb2IDTPTwu6s8jfcdFhjuv66xq7pP7SjDC6zzDpJb2z2IiRCvQByXnTJ1vUZKeT2hG0nbmqCxH3CTEAgI4IfUFTeUWzoDQT6XOi-aoM2EpbiWaxDByw5OQqyBRcGT9g3eE1KvnQiL1N8Nl44MmJ0qpxIZMlOiC15W-sxaN8C1B9ZYQgEcIOHnd4pbxZdAjd-5suNvxtda1I055vZTdb5FM4Wg9yusVk5sbkIrUWATMTVrlxvwsdOEtepOSfMkQjEUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران را تست نکنید! جاده‌ی خشم ایران!
IRAN: FURY ROAD!!
🔹
اثری جذاب با حضور بازیگرانی مثل جولانی، حکام عرب، مکرون، زلنسکی، نتانیاهو و ترامپ!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/678617" target="_blank">📅 12:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678616">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f90ed60dd.mp4?token=jJqWqj38LF3SXPBk8mWufV5G1jfdQguiBsrocx-6y1MBbGT6u_U8nTBwB11ggiYlIuG0QkkHOZCNLuOuFXN02-mq9AmLXs_0AAc0YJ2WwJk0qO7MIs44jTOnbf8mUZ2j-mH67lpF93WaEHEfZWtiJyYm1yfukytbH7vgrr2dhbVfYYBhASfMAz9FNktvB9JSncuT5HO7FtN2iTHfCYSTVddofY18Wbft_GSllCWWHZrtj0CEyPEzxSIqg4ruIxJJ6wtZ1GLRlCHhacxxbBmxkKmmc_WGwonD7SwlYid4J2uvsI0ALuEzpLACFKWAG131VDCW7ylD6DLZ8FzzP-MpTCek9aKUyRONFgzzR1NpfqBijU5VM5kwL8sxLpEQS0umcfZBAk6t8ehsg6pHIfDp4ifop7FLl0whPNzgZ1us-i_6wkr6v36imY2kiyNf9JohBgDre7J7n74sTl0dpQ-Z65lGNCOMqLhmPVRPnkfV943yNghubUASsK-9K0SYimqwbwGtnqHrKXgRWnghBsOzGPufJ_03tRWzhbvrgqKw5WTfdQB98aL9IfRRo0UzHDbKyaeuhS-qN3Ai9brbG_CymUttj9QZzwGFLDuRKASInL2UfcKXPVOPn9HRhQ177h9s6gyyqwe2VOks-wglzHzu7S_36GiEa4IU2VxUXTsjX3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f90ed60dd.mp4?token=jJqWqj38LF3SXPBk8mWufV5G1jfdQguiBsrocx-6y1MBbGT6u_U8nTBwB11ggiYlIuG0QkkHOZCNLuOuFXN02-mq9AmLXs_0AAc0YJ2WwJk0qO7MIs44jTOnbf8mUZ2j-mH67lpF93WaEHEfZWtiJyYm1yfukytbH7vgrr2dhbVfYYBhASfMAz9FNktvB9JSncuT5HO7FtN2iTHfCYSTVddofY18Wbft_GSllCWWHZrtj0CEyPEzxSIqg4ruIxJJ6wtZ1GLRlCHhacxxbBmxkKmmc_WGwonD7SwlYid4J2uvsI0ALuEzpLACFKWAG131VDCW7ylD6DLZ8FzzP-MpTCek9aKUyRONFgzzR1NpfqBijU5VM5kwL8sxLpEQS0umcfZBAk6t8ehsg6pHIfDp4ifop7FLl0whPNzgZ1us-i_6wkr6v36imY2kiyNf9JohBgDre7J7n74sTl0dpQ-Z65lGNCOMqLhmPVRPnkfV943yNghubUASsK-9K0SYimqwbwGtnqHrKXgRWnghBsOzGPufJ_03tRWzhbvrgqKw5WTfdQB98aL9IfRRo0UzHDbKyaeuhS-qN3Ai9brbG_CymUttj9QZzwGFLDuRKASInL2UfcKXPVOPn9HRhQ177h9s6gyyqwe2VOks-wglzHzu7S_36GiEa4IU2VxUXTsjX3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استخوان‌گیری ماهی واقعاً خودش یه هنر توی آشپزیه
🐟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/678616" target="_blank">📅 12:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678615">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بگومگوی مجری صداوسیما با ناصر هادیان بر سر مدیریت تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/678615" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678614">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705eaa8f9e.mp4?token=E22qm8Vwids8tNgZdu3qoAvulFQEh7CYGVJyKkc4bnSEaLY-AS3TUX0EBWn9Y6d7OccZWgFUocQT3aqIgsfGiR91E9k02enmOTNJA1qT_hhrHxq4gMfA0K1eDxStpw1bX9S7E0pLxOojod4FdIOjEdooPNeWRv3Cdsjw-y9PIcd635lOzjiCWMP1y4Ly9owodNeIXRgERzMewXzS3inm6ratTUV743tsMJpA407HmYa7tGN2JjJquzv3PTXE-eOkuUIV0DIfGMeuEI8CTDA6SiykG-li_kez98Oc9KJEnOIWPBieScH8p1yi3U0aWi9xKJeRw3fDbyQX8j0DhLJLOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705eaa8f9e.mp4?token=E22qm8Vwids8tNgZdu3qoAvulFQEh7CYGVJyKkc4bnSEaLY-AS3TUX0EBWn9Y6d7OccZWgFUocQT3aqIgsfGiR91E9k02enmOTNJA1qT_hhrHxq4gMfA0K1eDxStpw1bX9S7E0pLxOojod4FdIOjEdooPNeWRv3Cdsjw-y9PIcd635lOzjiCWMP1y4Ly9owodNeIXRgERzMewXzS3inm6ratTUV743tsMJpA407HmYa7tGN2JjJquzv3PTXE-eOkuUIV0DIfGMeuEI8CTDA6SiykG-li_kez98Oc9KJEnOIWPBieScH8p1yi3U0aWi9xKJeRw3fDbyQX8j0DhLJLOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۶ سالگی و تیغ جراحی
🔹
دخترهای زیر ۱۶ سال هنوز در سن رشدند؛ چرا باید از همین حالا دنبال عمل زیبایی باشند؟
🔹
فضای مجازی به آنها می‌گوید زیبا نیستند در نتیجه از سن ۱۶ سالگی سر از اتاق عمل در می‌آورند تا بینی گوشتی را تبدیل به بینی خوش فرم کنند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/678614" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678612">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4mCr_9QjtJogMpW9iZiuEqORMToAxIwbH56tYyeBkFz7FOsBuflr8lReJoYFJb_0fnCRXU--doQoYsJ8v61CRb9bOPRbyU6FQZdntuiU_KlGsTqBWiGVtZbzBGDC7o9XhRPM6yQoF9T1xSCmA36X1nwckjsx3NMryP02vSKh2VeE-MeIq-j-GuR3AMkOYl2hEPdG2a8viArtXclWOb_pkuXzTwIO5R-10DQ0rYFWiU9rU2chkqKXwBAxeAUbhOM1ZnNy49WWC0chB8FLy7XZhL3c9R9nuQjObYlUG92rrhIdM2FW21KQxlX6IGqbK0A40KzV2f0Zs9U5PTfC5ZD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام باشگاه استقلال، رامین رضاییان از این تیم جدا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/678612" target="_blank">📅 12:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678610">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنمابان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11fc209778.mp4?token=et8ICuzhnR3Vyf2wxATAaYh_UfC9aYBv1_RBk9MDooV5JpzY3bj4aJbol5hItYdZGqYDvdk5xwn7ZYmG43TDMy-35cz_ZdK_db2Rw854Esc0MeIFZvgl7HhjCVpQ1XU2NKDfGF19aItX2-fYW9w1r59y8ly0f4zVXRCEjg3N4PZS0hSK9861uTKUMCL9XX8s9lEVfXUtMh7oJ-ngDC6mTqGIUSUMMWz-ZdNwYjsKz0dKSCINFERqyir5a99raRKh-qyBmYAlvzKW6iTANN9wb5zfQh7a-LS-YYzS7WqxDW8HhO42gsJ8yp59UDCDv-zXzHszkmpHiRuoeGVc0j32eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11fc209778.mp4?token=et8ICuzhnR3Vyf2wxATAaYh_UfC9aYBv1_RBk9MDooV5JpzY3bj4aJbol5hItYdZGqYDvdk5xwn7ZYmG43TDMy-35cz_ZdK_db2Rw854Esc0MeIFZvgl7HhjCVpQ1XU2NKDfGF19aItX2-fYW9w1r59y8ly0f4zVXRCEjg3N4PZS0hSK9861uTKUMCL9XX8s9lEVfXUtMh7oJ-ngDC6mTqGIUSUMMWz-ZdNwYjsKz0dKSCINFERqyir5a99raRKh-qyBmYAlvzKW6iTANN9wb5zfQh7a-LS-YYzS7WqxDW8HhO42gsJ8yp59UDCDv-zXzHszkmpHiRuoeGVc0j32eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
بالاخره اینترنت داخلی و خارجی چطور حساب می‌شه؟
اخیرا درباره کم‌شدن حجم بسته‌های اینترنت کلی سؤال و ابهام مطرح شده اما اصل ماجرا اینه که «حجم مصرف» با «نحوه حساب‌شدن تعرفه» فرق داره.
طبق مصوبات رگولاتوری، اینترنت سایت‌ها و سرویس‌های داخلی با تعرفه ارزون‌تری حساب می‌شه. برای همین، با یه بسته عادی یک‌گیگی همراه اول می‌تونی حدود ۲.۷ گیگ محتوای داخلی مصرف کنی. این عدد برای پیام‌رسان‌های داخلی حتی به حدود ۴ گیگ هم می‌رسه.
پس نه بسته‌ات آب می‌ره و نه حجمش جادویی زیاد می‌شه، فقط اینترنت داخلی و بین‌المللی با تعرفه‌های متفاوت حساب می‌شن. / نمابان
🔹
@namabantv</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/678610" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678609">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vwtbs6YWq1FN32MmeiNw2nXvGZFb_RjPyo7EHlJO_gYEmL5PMroujPoemrVhvmiMljVUU68U4mH-OOybdk8v8o2uEwo5FCq--DLN_5mV3DLk13siJY2mJ3tJ6gAAVGCqZlumP3oJ_P5lDcLWyTYQP2nIlliFn4aI9e_nAno4kmj231GShZtiMeCcoVUh6ZQ8FM2JwHQ1NCKatySN0YFZ0ewhAwN3l9_6A4Rb29bE-_cf2Ur3s466o0_FCzWz1zdjn5oTCajV563zy_hPNQCDpH7_DKWwte8PF8tGWmNyZYWIF_NhoUJysVUpuFoP5I6Kv7ynwnsoeR8AdKhlaV-knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
جعبه هدیه صحن نو
ترکیبی از یادگارهای متبرک حرم مطهر امام رضا (ع) که عطر ارادت را به لحظه‌های هدیه‌دادن می‌آورد.
✨
مشخصات محصول:
▫️
نگین؛ از سنگ‌های روضه منوره حرم مطهر امام رضا (ع)
▫️
مُهر؛ ساخته‌شده از سنگ‌ صحن‌های حرم رضوی
▫️
تسبیح سنگ هرکاره؛ یادگاری از سنگ مشهور مشهد
▫️
عطر حرم رضوی؛ با رایحه مورد استفاده در روضه منوره
▫️
جعبه چوبی نفیس؛ مزین به نقش ایوان طلای صحن نو
💰
قیمت اصلی: ۲٬۲۵۰٬۰۰۰ تومان
💰
قیمت ویژه: ۱٬۹۵۰٬۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/678609" target="_blank">📅 12:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678608">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8JIQe_6UvCGQuZ3LAgKwjJKvdjaTFTph8UYRktNLKbSKSG651QPp2yj21JnmgA6awVny7L-YKAU8QtMStxNalAsQsi37j1B17g9767Pi0Gpavt0PujZ0emLNRhEAQ8DNDXlrHyxzihrzK-DM02INtoiuWy5-_zUiMkxuffi5Wiq7gu-KATOvn7LJ1GPqzcGQok6GpZcAiVyBX_5YDAm5PTTG8JXVnOjp1GCcWjF9MVpHn25p3B48y_kWjW_HcbR_VFck0sszZO97J1dfWcflxq4XXsHt6hiDa542QXs1GRfjMG_Zz09zh4ujGiz1ZGPDa9qIWGbrdVGmE7zsd_xpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار جمهوری‌خواه آمریکایی: جنگ ایران یک فاجعه راهبردی برای آمریکاست
🔹
اسکات مورفیلد، روزنامه‌نگار آمریکایی، جنگ ایران را یکی از بزرگ‌ترین خطاهای راهبردی تاریخ مدرن آمریکا دانست و تأکید کرد ادامه جنگ تنها شرایط را بدتر می‌کند و هیچ شانسی برای پیروزی وجود ندارد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/678608" target="_blank">📅 12:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678607">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD8Uxyy9MijWKOcB7o_py4Fvukcj2A1Yi000ydpHl9VNe3c7MTwFb-7EDpdP8hhqXyeAYFFVvjMsYphfg-SYeSmJzADXgu2KjoKG8jDc5LYrlQHQv38g38KnnagWPjRgEZSlAooT7K4lqtv0fFkfC49pq9dKAGythRM21FnmUq1aw_wbfCDlks2J5cDJTXt5cZhZFyvvT1_rJ4mW1VJUXAYC0zh9PJ3o8cNGoz1PE82qLvXvbFHYBO7Br7glVS04Ce9yqJlPCpcEvnDfgPs1vfnP1sPR8qO7soIhifGowUVzVjYQW4fu5gw2sOKqDUZssCbWJ_y7ZUm0FjpJktHtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینجا ایران؛ مازندران؛ میانکاله
🇮🇷
🔹
ایراندخت غضنفری
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/678607" target="_blank">📅 11:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678606">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: تنگه هرمز ممکن است امروز یا فردا (پنجشنبه) باز شود #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/678606" target="_blank">📅 11:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678605">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WidR0T4UGCA5YnDWP6R2snWGlI02JqnWndPMaxNYHUyRDK75gOMBIoe7ZK4TlCsBZPlnUMEc0dIHk_j7zV8zFeGNahl4PmOeF2k_a-cTMbA0sxCbkuvWRk_W_uU-8OpiLvQZ8MvWY6lBL5ZrvY6el9OeqOghAZ1LshnWyJ3-hwv7pB0KU_MNZEhUxgpvAN4W_3CnA87s-R-SwXaWZfgdbTss-_q470KZ3P8ujuNWJK6Dtxi1DocwYQ3ZPPmBlC9vrzHJEe2RFNMRlDsv2HB1oAU63guqeA7ytXR4dGsr7T9qoolJT1_4OsVu6qVoCXRJjaZg-oxGKfVtq8ArBknb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار رئیس کمیسیون امنیت ملی به آمریکا: به زودی از منطقه اخراج می‌شوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/678605" target="_blank">📅 11:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
عبور از تنگه هرمز بدون تأیید ایران ممکن نیست
دنی سیترینوویچ، مقام پیشین اطلاعات ارتش اسرائیل:
🔹
ایران کنترل امنیتی تنگه هرمز را در دست دارد و از آن به‌عنوان اهرم سیاسی و اقتصادی استفاده می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/678603" target="_blank">📅 11:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33cacc9554.mp4?token=PvxfRl3q51J8UowRAmg8rm77VOyRtzZeaKk6AWjwN0gsjPylHQvXnmRJS20PpR6pe770cLQn1vhpDwmPn2b5sJHBC-gSJEtAkgrBkaiNPKVipSjasZzBzg5sZijB2KJNIg9Jb_ep63Ouy-xpnH9u6-xxYYF646Kne2aib3fh7MPD8_vp8R6zxabuhxm4ChXwGNTIMNtzwW60zh7o1R2Hp9Go6XX82wueV1el3Xomkk5yfDoxgNIF2roKEZlBq5xqpv7T0QotPzJIUkriCZrWRnTVmICRNCW02-VUIEIHdGb4W4zq6lA85VKoAOAnS39GyR0sX4Am-u7YDgZk2LG2TiCTWPPuZ-7aE9beENgYciOHnmvxMpf6EC1ndIf_T3NQBSudgwzyvXHSUb2SI0vCHsGuNCsxE4fq7q5JaXQSLnqVAf_Y1c4FcpS0uvACWn_lCTCrDh-xMo8trRhcheymJfNDia8QBB6PqWb6Qk4RvbwEcdGJdEv0OwSLIjuff0l1fbrKZaJiPJjycSWS5_B5HGMJZnxBpY6xYm8dQZlKiXdmkdcXXKgQUUZgYIaXSWSCgG5wlH9Yfa4Idx0Lxush2RAc_ycPHNfvW5_yGX3YttD0dceQS1a3uIx-cE6DUnNY9ZWJL2BLWbhAyViPEITu_PYr1FfiQBS56t8LUHDa3nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33cacc9554.mp4?token=PvxfRl3q51J8UowRAmg8rm77VOyRtzZeaKk6AWjwN0gsjPylHQvXnmRJS20PpR6pe770cLQn1vhpDwmPn2b5sJHBC-gSJEtAkgrBkaiNPKVipSjasZzBzg5sZijB2KJNIg9Jb_ep63Ouy-xpnH9u6-xxYYF646Kne2aib3fh7MPD8_vp8R6zxabuhxm4ChXwGNTIMNtzwW60zh7o1R2Hp9Go6XX82wueV1el3Xomkk5yfDoxgNIF2roKEZlBq5xqpv7T0QotPzJIUkriCZrWRnTVmICRNCW02-VUIEIHdGb4W4zq6lA85VKoAOAnS39GyR0sX4Am-u7YDgZk2LG2TiCTWPPuZ-7aE9beENgYciOHnmvxMpf6EC1ndIf_T3NQBSudgwzyvXHSUb2SI0vCHsGuNCsxE4fq7q5JaXQSLnqVAf_Y1c4FcpS0uvACWn_lCTCrDh-xMo8trRhcheymJfNDia8QBB6PqWb6Qk4RvbwEcdGJdEv0OwSLIjuff0l1fbrKZaJiPJjycSWS5_B5HGMJZnxBpY6xYm8dQZlKiXdmkdcXXKgQUUZgYIaXSWSCgG5wlH9Yfa4Idx0Lxush2RAc_ycPHNfvW5_yGX3YttD0dceQS1a3uIx-cE6DUnNY9ZWJL2BLWbhAyViPEITu_PYr1FfiQBS56t8LUHDa3nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات کاشی‌کار؛ آینده ساخت‌وساز
هوشمند
🤖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/678602" target="_blank">📅 11:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حساب شرکت ملی نفت ایران بسته شد
🔹
بانک صنعت و معدن به‌دلیل بدهی، حساب‌های شرکت ملی نفت را مسدود کرده؛ این در حالی است که مهلت بازپرداخت بدهی‌ها تا پایان سال ۱۴۰۵ تمدید شده است.
🔹
پیش از این وزارت خزانه‌داری آمریکا در قالب تحریم اقدام به محدودیت مالی برای شرکت ملی نفت کرده بود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/678601" target="_blank">📅 11:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سازمان وظیفه عمومی فراجا: معافیت‌های ۳ فرزندی و ۴ فرزندی تا ۲ سال دیگر تمدید شد
🔹
مشمولان غایب هم می توانند از این طرح استفاده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/678600" target="_blank">📅 11:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPD8VC165T8kC3K0yR7LOlfEHadkjrzGeIch67f5_ffCr08QPzBh8kHnWTPiOpQXC2eO6ogiagI1HDysBz1ftVYBj_lQtOh1dyB3jFDCoiWAnYA4oFMxBrzERSI3S_MPmsepLKdDf2nz8zLAL20RliA6TZbkIlFeqLd0JmtF6dVw5ldUqV6dDoH7dXnhIuXCluL2odckCcl9VwgKyMxNipEo0ggFYEGaxyauXrrvSqnSNjAGXKfnSPBO7ycVL5GQkXkccVH_PefEwn1-8XyFpgBDp5LN6-eOiS29YyQ3mCGX-YvkIRCevA6AC-l3YqfxB9ATXQEzPs5_5OJYwle9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی پاییز پربارش برای ایران
🔹
مدل‌های پیش‌بینی هواشناسی، پاییزی پربارش برای ایران پیش‌بینی کرده‌اند؛ اوج بارش‌ها نیز در اکتبر (۱۰ مهر تا ۱۰ آبان) خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/678599" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
ترامپ ترور شد!
👇
khabarfoori.com/fa/tiny/news-3235561
🔹
اخبار لحظه‌ای از مذاکرات تنگه هرمز | توافق امروز اعلام می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3235587
🔹
قبض آب و برق ۴ برابر شد!
👇
khabarfoori.com/fa/tiny/news-3235621
🔹
پدیده ازدواج بدون رابطه جنسی چیست؟
👇
khabarfoori.com/fa/tiny/news-3235475
🔹
فرزندان خواننده مشهور برای وداع به بیمارستان رفتند
👇
khabarfoori.com/fa/tiny/news-3235480
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/678598" target="_blank">📅 11:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guf16yP1Y-QZgJz2Xbjz3BTMMv57EJDjYURuRGXD6lD8nwvmqdUcqucSo-ede4PknXDZgRCs_QsCsrkJ591AyXrudvqcSeCH8-NKac7JEswdLJkWpaNOhKqHMQlB6OrXAoyjWjuqaOgwbgnShEFdPiJO0LSA6Hewl7NGPiimjLpiym-QpqlrZXSdyWT0DZ_aokL6FWQNR_6NhSL0f-59Xu8-re6-mx8xgIaQjI6vrkF_ALYQ7tpaRnuVFCgGM3BMmI7WaBsgSSe3FulNP8jHW4nMZ1ypw8YT-HwyQW4YyV-agm8Hp8ZK67U0IUAbQKGTvl-pMA2uuZ4tt1TSPbqIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت عجیب انگشت دیدا، دروازه‌بان سابق میلان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678597" target="_blank">📅 11:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
شهباز شریف برای دیدار با بن‌سلمان به عربستان می‌رود
🔹
به گزارش رسانه‌های پاکستانی، نخست‌وزیر این کشور شهباز شریف برای انجام گفت‌وگوهای سطح‌بالا با مقام‌های ارشد سعودی، این هفته در سفری دو روزه، راهی عربستان می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678596" target="_blank">📅 11:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6c6b9445.mp4?token=hBT8qRGNX10y0nhqPBKgm2n0uJqeFtCzcnw8AY9QRA9HjY9SdhAeTrEHERVfq3sVDuvWshzR7-Ya4CMhjqCp1wY711PQ-h0hO87h5qfww_g3mXvFS8ETkuYUNoI7NAjerxG0loh3HXPGIfDA_HPKT7r4cq66yhScdwItsutIym3u3KMt3jG8zNv-_Nbksnx8rOCSIdw4uysoQRQA2DmxleVaLV2JlMwaevUuFTc2je_9_Z7DJXVxEn3Xwp0_4fxkZleHQO9aGkbuDunpu-QK1UKjNp4ZF7Y9-yP8UNW0crwdb23Q_umy9m7wxBal6CheIiFVBlBmrJIR2LRQmyYO0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6c6b9445.mp4?token=hBT8qRGNX10y0nhqPBKgm2n0uJqeFtCzcnw8AY9QRA9HjY9SdhAeTrEHERVfq3sVDuvWshzR7-Ya4CMhjqCp1wY711PQ-h0hO87h5qfww_g3mXvFS8ETkuYUNoI7NAjerxG0loh3HXPGIfDA_HPKT7r4cq66yhScdwItsutIym3u3KMt3jG8zNv-_Nbksnx8rOCSIdw4uysoQRQA2DmxleVaLV2JlMwaevUuFTc2je_9_Z7DJXVxEn3Xwp0_4fxkZleHQO9aGkbuDunpu-QK1UKjNp4ZF7Y9-yP8UNW0crwdb23Q_umy9m7wxBal6CheIiFVBlBmrJIR2LRQmyYO0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار اروپایی: آنچه در کربلا می‌بینیم، میلیون‌ها نفرند که خواهان انتقام هستند؛ انتقام برای رهبر عالی‌مقامشان و کودکان میناب با کشتن ترامپ
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/678595" target="_blank">📅 11:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: تنگه هرمز ممکن است امروز یا فردا (پنجشنبه) باز شود
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678594" target="_blank">📅 11:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678592">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM71rfUbHDPB9HpgOXX34VPgYIdif2AThU9ZJjWvN7TUfQzCv5W3mPvypopSLCTckGYCGcwEqTd9lPEeN3mRD3Ewq8RfqvJjTQKW0We1gVs9xLRV0UyPTyQG3khPC33ZgzurDjLxy6I41e1QRL_eCC3A8Uo_CmZzouON3NiCIgvH6FKRywYomzDG0Cp836nsKyunTpNT1GEraKZEJxKktVU2NgVOmklh3feo0fXLUh8ntl_BQbjJivZykfb2DLfQfzyN7WrohxksOgzQPrpDA-uoMaNMEf5sO7CdeCFqGJVQLXfoPFhHWn8EtRHLsflfSX9jJnGoEWxbSs2QgeJNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر ارشاد: مسئولین سرچشمه ترویج اکاذیب را خشک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/678592" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678591">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eicbRGwhmZhi9Cu7Gu3dAHQuhrGK16asYyTuOUl2zL6nMP93VuE-kUqs-b4NMJHvrXg3xqGF5wVq_1-I2jTYVvY2uC83FDVlQWUpawqfAhCzPHv73Aribg5FLQ-sAhzoPZ1bxvvWjuUJ7auOyfIvhjRWlXZV4KIWX5QO1QNOvQetER3RJ14HN7pqe6x5PKNtesFOSv00C_ADwIo_6ZqQPst49r64UFVZoPKQ1xj3w8pbHaHFSVJ_ho1O4rzYdksxLNFGMqvDKzcdDMhmcPb_os-Zknsl9ksBdSyOp8zNdVHxRheNOQBvj0zr4FvvZul_Ae3hcxegrYtwseSRHjIP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يك كليک تا خرید اسپورتیج
طرح فروش فوری کیا اسپورتیج 2025 کوشا خودرو
✅
قیمت قطعی
⚡
تحویل حداکثر 20 روزه
ثبت‌نام و پرداخت وجه به‌صورت آنلاین از طریق سامانه فروش کوشا خودرو انجام می‌شود:
🔗
سامانه فروش:
sale.kooshakhodro.com
📄
دانلود بخشنامه فروش
⏳
ظرفیت محدود</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/678591" target="_blank">📅 11:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678590">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpd5QmGyDyvM-lXY1MW9jAZX-SZFklzl_bo_KBaFLF_trmH0OpHWMU3onzphHLyF9l47UTGUO4ubHo5GKhQro3g7lGRPDLZuKuWBdYY8kHKm3uazh0AM4QNFx8-LlyjoIw8-TjjjmIhA-ZnPgf7HnXNxn8V39u3mVLMkPi6o1bE6E4Dy-0HXA-Y2bJeGW6nNX_6qfppzqPbXN8V0d0n6b-IMuCE9aDeQdBuiE1U21cbUhv_zu7EHBQLmBdpvVUoH5ZmifgSdsMNMXQbdmmByVyhJ331IcYnRGuZP7z7s41VFgfQn9pz8XxTGl1CxPEfzz70dQNiubDLdoaJr7Ks6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار رسمی زائران اربعین اعلام شد
🔹
آستان مقدس حضرت عباس(ع) شمار زائران اربعین امسال را بر اساس شمارش الکترونیکی، ۱۹ میلیون و ۹۹۹ هزار و ۸۷۰ نفر اعلام کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/678590" target="_blank">📅 11:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678589">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای
کانال ۱۲ اسرائیل: تل‌آویو اطلاعات مستقیمی از مذاکرات ایران و آمریکا ندارد
🔹
تل‌آویو اطلاعات مذاکرات را بیشتر غیرمستقیم دریافت می‌کند و معتقد است ترامپ و مشاورانش به‌دنبال توافق با ایران هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/678589" target="_blank">📅 11:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678588">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای العربیه: هیچ مذاکره‌ای در هیچ سطحی بین عربستان و انصار الله یمن انجام نشده است.
🔹
آتش‌سوزی پارک ملی بمو استان فارس پس از ساعت‌ها عملیات مهار شد.
🔹
انهدام مهمات عمل‌نکرده در پاکدشت تا ساعت ۱۶ امروز انجام می‌شود و جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/678588" target="_blank">📅 10:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678587">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تکذیب دستگیری تروریست‌ها در مرز مهران
🔹
معاون امنیتی استاندار ایلام خبر دستگیری تروریست‌های بمب‌گذار در مرز مهران را کذب اعلام کرد و گفت امنیت در تمام مرزها و مسیرهای استان برقرار است.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/678587" target="_blank">📅 10:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678586">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82cdb975d.mp4?token=LBjNbzKa0ux8JyIXqRPR_owtTVBYvSkEc3TB9M0b2PRZdYWplLm1vkCbTp_CCKg7Dgk89phHacalVfb_EwCmEK2lrXppaL3YT6Zh94Tle5t5cx0-qEUJHr3RUSXdVOJasiX3cROhM3LuQS7MnIgA8oLRKFTRaRi2dg8XsU4bzRgDLGTXbDeJ7WVj2HZ9076_XKLwc9k8IXgSOcK0bFh8wC7so2ZhLgs4UrcIkoTFttydpsIU8KWx6XGa4RabmtM5ZIaQJwwe5mFcUJQoFm8Htfe20G7FzlWH-8oWt9P1hDbgGs956euKVDkPOIRGRf9b6ofX_Xqm06n5jTgyVMhXe4RGTwAZWQ-9wRdToGrgYjFILckMHaF3x-S-PpMIE5mSE5Apy2O9q_AshNz96eOLoN_l9NlPr2AbfYnxuuGp26Xt2sGndjUYVh2ypqpn1zsg5jZRNlU9nPURSnkzhlVhtiwBfP8OHDu_IKjLrcx85l7m8sUVqcbNBMrFypzL15G6eItzNG06IjThBddF1ZddHqC-2qGvKozommv1PkUT8Y6AjZ-uMU_Gip_PVkVFiEZoXDz1yERx3ogpdjdJ6T5ock9nk6GrRLNcIMI4ZYzVXPiSXnai5OHIpHghYFsCR89zaBEzALpMiFMi83weXx9VZp0b0jp5gwWoO_eeco2qx8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82cdb975d.mp4?token=LBjNbzKa0ux8JyIXqRPR_owtTVBYvSkEc3TB9M0b2PRZdYWplLm1vkCbTp_CCKg7Dgk89phHacalVfb_EwCmEK2lrXppaL3YT6Zh94Tle5t5cx0-qEUJHr3RUSXdVOJasiX3cROhM3LuQS7MnIgA8oLRKFTRaRi2dg8XsU4bzRgDLGTXbDeJ7WVj2HZ9076_XKLwc9k8IXgSOcK0bFh8wC7so2ZhLgs4UrcIkoTFttydpsIU8KWx6XGa4RabmtM5ZIaQJwwe5mFcUJQoFm8Htfe20G7FzlWH-8oWt9P1hDbgGs956euKVDkPOIRGRf9b6ofX_Xqm06n5jTgyVMhXe4RGTwAZWQ-9wRdToGrgYjFILckMHaF3x-S-PpMIE5mSE5Apy2O9q_AshNz96eOLoN_l9NlPr2AbfYnxuuGp26Xt2sGndjUYVh2ypqpn1zsg5jZRNlU9nPURSnkzhlVhtiwBfP8OHDu_IKjLrcx85l7m8sUVqcbNBMrFypzL15G6eItzNG06IjThBddF1ZddHqC-2qGvKozommv1PkUT8Y6AjZ-uMU_Gip_PVkVFiEZoXDz1yERx3ogpdjdJ6T5ock9nk6GrRLNcIMI4ZYzVXPiSXnai5OHIpHghYFsCR89zaBEzALpMiFMi83weXx9VZp0b0jp5gwWoO_eeco2qx8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا اتصال سبزوار به شبکه راه‌آهن سراسری محور سبزوار خوشاب از اهمیت ویژه برخوردار است؟
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/678586" target="_blank">📅 10:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678585">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
یمن: یک نفتکش سعودی در دریای سرخ هدف قرار گرفت
سخنگوی نیروهای مسلح یمن:
🔹
نفتکش سعودی «وفا» در نزدیکی ینبع با موشک‌های بالستیک هدف قرار دادیم؛ تاکنون ۸ نفتکش هدف قرار گرفته و تردد ۲۹ نفتکش سعودی متوقف شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/678585" target="_blank">📅 10:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678584">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e6f734c9.mp4?token=NEaxZty7DrquUQRFsA1sXHfaEORF5Y-SdifXELejnpQQYjyYmediM0LRUoHPEyYv_c5C8Qj0gPqmGLlEVa8sHs03bzGvRRq4Mv2POVZd5U9dVzyjwibc1VhyB1MRl9B5B7WvXijPA7L0saKxpuCEkKcUT2HS_NNPv-8zZsM2Q7sAc0Bj_KpObSfzDY_fjHT4p2Y8Vhqeu-ZheNYSlykMaM-7un494iQVYEAiGadoqPvyHj6f1J4iXz1wlzD3kO11T44U_Hr9Ugk0HB-v-igUZik8nobzwJb7UZEDtP3UyE5EwoU-vnoH70A-V-GxmL-MCuS4dj4bK9Yoqadfe5Z8vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e6f734c9.mp4?token=NEaxZty7DrquUQRFsA1sXHfaEORF5Y-SdifXELejnpQQYjyYmediM0LRUoHPEyYv_c5C8Qj0gPqmGLlEVa8sHs03bzGvRRq4Mv2POVZd5U9dVzyjwibc1VhyB1MRl9B5B7WvXijPA7L0saKxpuCEkKcUT2HS_NNPv-8zZsM2Q7sAc0Bj_KpObSfzDY_fjHT4p2Y8Vhqeu-ZheNYSlykMaM-7un494iQVYEAiGadoqPvyHj6f1J4iXz1wlzD3kO11T44U_Hr9Ugk0HB-v-igUZik8nobzwJb7UZEDtP3UyE5EwoU-vnoH70A-V-GxmL-MCuS4dj4bK9Yoqadfe5Z8vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهارت عجیب و شگفت‌انگیز این آقا در استفاده از چاقو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/678584" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678583">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4511285b47.mp4?token=De4gRkSxJHKM3b_5EenkAZm6h8j5ffTDD7tJtGVRatCzSyhFK0dq45jf-mxrisltZ3DXxGwqaShrfr2E-Hlj53z1r4z2ugCZoKy5roZCW91Av9DTOGXRYhVZJWZo8ctcnWZHHdiDAlcUf5zqVo0jaVMjzrH_0yaYPZxcZB6o_LTtTO0PdVqjiARBy-pcB0ja7jM4bKZ-y0n-pMgppgPaKrc8BWc0xVGXjUH_EFfFdFBD4mtQJkh8-7aC7O_qMYiuvmBknwfDYtncR3UYUQ__WnwOdpsIwIuKDVn81Nh_FEZGys2cIGiUuPVEt55GM-IousBrUK59BpUswxDLqb8mlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4511285b47.mp4?token=De4gRkSxJHKM3b_5EenkAZm6h8j5ffTDD7tJtGVRatCzSyhFK0dq45jf-mxrisltZ3DXxGwqaShrfr2E-Hlj53z1r4z2ugCZoKy5roZCW91Av9DTOGXRYhVZJWZo8ctcnWZHHdiDAlcUf5zqVo0jaVMjzrH_0yaYPZxcZB6o_LTtTO0PdVqjiARBy-pcB0ja7jM4bKZ-y0n-pMgppgPaKrc8BWc0xVGXjUH_EFfFdFBD4mtQJkh8-7aC7O_qMYiuvmBknwfDYtncR3UYUQ__WnwOdpsIwIuKDVn81Nh_FEZGys2cIGiUuPVEt55GM-IousBrUK59BpUswxDLqb8mlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر سابق ایران در ونزوئلا: بعد از ورود آمریکایی‌ها به ونزوئلا، تورم از ۱۰۵ به ۱۳۰ درصد رسید/ از وقتی آمریکایی‌ها به ونزوئلا آمدند، با وجود حدود ۸ میلیارد دلار ارزپاشی، ارزش پول ملی این کشور ۱۰۰ درصد کاهش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/678583" target="_blank">📅 10:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678582">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcSOV3omLOPDibj34azhMktOUgFh2N-u2wPioo6ItZZCCz17ukXT_NxyhfHde3fPNqM2g6XkPfiRJtVmcHKUWRvEbkeCRkISW4htNFkUJJ6SsisSO36p4IEt4J9wHcZzOaW0RBlh8Rj3XJCX2M6JE7D1ramUS8ergbLHPNW3TU2QhbGOzGLRo-nA-Qn1TTZS_QR6g-TTb9j2EqTV3f_1H3wYXlNhO9UMSexLupXl4t5DVdgqakrCWtjgysQbjGNymuEasjXNveCJ9-nsN2YhE0PQ13n51rlJnlejOUau-mwdRpdtHEfyuZRa9VjFXraM_0LWwLBuSotNH6yXGIAyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردم ایران مبعوث بودند، مردم جهان اسلام هم مبعوث شدند...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/678582" target="_blank">📅 10:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFz9X9QUlSMDq_1E9eSQxQfeMvsKCCE88cgIF_B5Smesqj4CiSVLTz3elvsreXv2lkMqNXJaM-ssrzrqnFaiRYOcbE2w5OhvQYe0RF1wK5eK1-27ms38O-lPxniLfMTVN0OrpjG7vstB4ur_-r2l1U0FY4qP_yQZYibzu_cHEya4k1JJ2xIIrK8Xv77-wCezD0Q06FwyUR8atY9sFviwD6eoy4dD4-fwhAMPCFBlS1zYCOX6f4rjW_qTTClQXw4-ewMwlwoiSMz3bMpYgXTKWfJeZ05AFuS93cB2734CfCPm-ZHFGgz6iztMgAttmOPKpjjQwgvRXDo5txxtDmThOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این پنینی انگار از خود رستوران‌های ایتالیا اومده
🇮🇹
مواد لازم:
🔹
گوشت گریل‌ شده
🔹
نان سیاباتا یا باگت
🔹
پنیر موتزارلا و چدار
🔹
گوجه و فلفل دلمه
🔹
مایونز یا کچاپ
🔹
قارچ و خردل
🔹
ژامبون  #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/678580" target="_blank">📅 10:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سازمان امور مالیاتی کشور: بلاگرهای پردرآمد مشمول مالیات هستند
🔹
بلاگرها و فعالان فضای مجازی نیز در صورت عبور درآمدشان از سقف‌های تعیین‌شده، باید مالیات پرداخت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/678579" target="_blank">📅 10:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678577">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klzL5j7zy75qlVR49YN71RPs3B--hKfTgK3xc5-zqXMnykDIH3t61tT-Ygnh0L5Ysf4VZbZDmDEV7EPTTYqS2XNQTVfaoFLyWcAo-xN2JD9vM-YpU-68YGdom4U_MIX6lI2twguUC6HVcyN2iJK4Wwe3sbcV2JZIbmzZuPRdHKH-kK-KrkMmoMY31rauiIHRijqNc6kK4BTUzpnES1LkYvaUeDr6TcNNmV7jUr9RLcbI76I-RJ0a3I4OBMvqMURfK48Pww0yfdCfUVmjDldOVvL7vy3OavM6XnV1oxCZ-WG63q4hKzIfusUyLGbMLJ4n-h6PDz7NytkIQSC5kNRpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت پلیس مدافع امنیت "نورالله نارویی" در سیستان
مرکز اطلاع رسانی پلیس:
‌
🔹
شهید مدافع امنیت "نورالله نارویی" عضو یگان فرماندهی انتظامی ویژه جنوب استان سیستان و بلوچستان که مدتی قبل توسط افراد مسلح ناشناس مورد هدف تیراندازی با سلاح گرم قرار گرفته بود، پس از چندی به علت شدت جراحات وارده در مرکز درمانی به درجه رفیع شهادت نائل ‌‌شد.
#اخبار_سیستان‌و‌بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/678577" target="_blank">📅 09:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
دو نفتکش‌ با پرچم پاکستان با وجود محاصره حوثی‌ها از باب‌المندب عبور کردند
🔹
شرکت اطلاعات دریایی Windward اعلام کرد که دو نفتکش با پرچم پاکستان که نفت خام عربستان را حمل می‌کردند، بدون هیچ حادثه‌ای از دریای سرخ و تنگه باب‌المندب عبور کردند؛ با وجود آنکه انصارالله یمن علیه عربستان محاصره دریایی اعلام کرده‌اند.
🔹
این نفتکش‌ها، نفت خود را از بندر ینبع عربستان بارگیری کرده و با سیستم‌های ردیابی روشن به پاکستان بازگشتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/678576" target="_blank">📅 09:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سفیر پاکستان: کانال‌های ارتباطی برای توافق بین ایران و آمریکا داریم
سفیر پاکستان در روسیه:
🔹
ما نقش کانال ارتباطی بین واشنگتن و تهران را ایفا می‌کنیم.
🔹
ما کانال‌های ارتباطی علنی و غیر علنی برای رسیدن به یک حل و فصل بین ایران و آمریکا داریم.
🔹
تعداد زیادی از طرف‌های منطقه‌ای در تلاش‌ها برای رسیدن به یک حل و فصل بین واشنگتن و تهران نقش دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/678575" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678574">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM-x8Gr91UT4NOAUUzkYnQ0RgAVasCWbYFq-kwcKHkmNKYlH2fKHYhIIut0q4b8FlTo8zFLRq_HnsfaacG5S4wed0iBrFX-kk-VTMh5FjXJK3J-mF-Ib0NX-rFLTjNskY_Vu809wRtxNpuOM0tVuq9jm6EF2vvfJU0j41rSOftgMIXnoy6NCb6i_jI_3E-6nXWQv2dA75cPHG4WGrYFUf5C5h-N6zF5mirW-27LqdJDWN88C0FWOtnnsTc4tCEhevCSdpXGC4X2OFN_saWLEEj53q337cyM6tShAQT3yCC7skBC11f-Hmept2Zow2T04c2E9eaGrRko3n5Lg2BJpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: استعفا نخواهم داد و خواهم ایستاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/678574" target="_blank">📅 09:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678573">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbi4GXaqQfEDGyvTAmqRlNKys_HJzxGHTYoi06D6j3tHwxBeBfp4NjEiNdSj44shIYzBshl7O60W8UJC5riB_Ay--sybA4FSOGcPUp87w1U1zRI56eTeXO0TDBG_W370h-vbEzQ5D8F_3mT53UnIjuoe0Mn0sHxm1A1rP1Uz9lZdw8m3BB9w18VCX6AebgqsUez9RdPLp8XEBXTdLCpe__37uO2XCgudRFnAY51zfYHFGtXsaTBb0A0u6dt86er9hGEn74wUR96_hwZ40-A9D-m0UOjqY9yiDC_qaPSqcb5WzR1Yw92px-6zcWGirExCMX1jVntLTdl2EGOasPaDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور شاخص کل بورس از محدوده ۵.۴ میلیون واحد
🔹
شاخص کل بورس تهران در معاملات امروز چهارشنبه ۱۴ مرداد ۱۴۰۵، با افزایش ۱۲۲ هزار واحدی، معادل ۲.۳ درصد رشد کرد و به محدوده ۵ میلیون و ۳۹۹ هزار و ۹۱۹ واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/678573" target="_blank">📅 09:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5pEGXWzvsflbDFVLPlF_6BtTcBWtVodH6IAm2mtNpP5SrPi6jHfD8PWtYkJ1yJZgvvVnlAKBhZcHjcrldHyP_YnN1FJEN7AwBXUB58g_AlL6nMX1pSu6f8aBskYZGnKuqRuNmm8Oa0Suda8Mz5UeDNY5G6F1TJu7kbccj0uER7MWD78WZ5zMF-XvDzxDMNyPkE9Vx099Q1nFYPWV9E6guRI1lziv7xYgca08-bjHCFhavtD_NykK2wrTbmPh3Cc0Pay2HpwQVgXjhJciuw29DE-2AE-t0GNnE2Endrjhu0H_T5EtCURK1s5-JBXZdBB1KRW1CPdBLWh8bf60JVcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اربعین، جلوه‌ای از برادری ملت‌های ایران و عراق است؛ از مردم عزیز عراق، برای این میزبانی باشکوه، این سفره‌ی کریمانه و این دریای بی‌پایان محبت، از صمیم قلب سپاسگزاریم
♦️
الأربعين هو أبهى صورةٍ لأخوّة الشعبين العراقي والإيراني.
شكراً للشعب العراقي العزيز على كرم الضيافة، وسعة العطاء، وبحر المحبة الذي أغرق قلوب الزائرين. من القلب… جزاكم الله خير الجزاء.
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/678572" target="_blank">📅 09:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678570">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
الجزیره: شرکت‌های موسوم به «غول‌های نفتی»، سود‌های کم سابقه‌ای از پیامد‌های بسته شدن تنگه هرمز کسب کرده‌اند
🔹
«اکسون موبیل»، بزرگ‌ترین شرکت نفتی آمریکا، سود تعدیل شده خود را ۱۴.۷ دلار اعلام کرد؛ بالاترین رقم در چهار سال گذشته
🔹
شرکت آرامکوی عربستان هم از افزایش ۴۴ درصدی سود سه ماهه خود نسبت به سال گذشته خبر داد.
🔹
«شل»، بزرگ‌ترین شرکت نفتی اروپا سود خود را به نزدیک ۱۰ میلیارد دلار رساند که بیش از دو برابر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/678570" target="_blank">📅 09:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678569">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMvbOQUFooWB0u7RxJ56eOYnfoav9qZdRLxMHBnFm0ffyHfZl2MKuT5bfAx4JC10-BamwD3QrI3MBsVkoNk8yTOuhbUv5leyHP8y2zGcdCq70g629B0kvtsNxwrcz2TB74LYpyB4hqi7ne0vqe89A3fiZZUxx03NQQTgmXJVlBmTt7QKwA_f3Hpalea5kF_CLGe4mFDZO4NEM5RwTF1tnFhvCTcZBgZN8-Xlu253v_IOGHplY517uPC5sQMA8rd-Wa5-hUFiQyES2gH7HHWoL_WamRPIPDTTh1jyy11jf8nqBsme5jWNznu0BRlzjwnstkRcHTdWrxEnEcCpzaNPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درمان۷ بیماری فقط با ۷ میوه
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/678569" target="_blank">📅 09:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678568">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
چرا قبض آب و برق خرداد و تیر ۳ تا ۴ برابر شده؟
اطلاعات:
🔹
هزینه مصرف آب و برق مردم تا ۳۰۰ درصد افزایش یافته؛ مثلاً فیش ۳۰۰ هزارتومانی خرداد در تیر به ۸۰۰ هزار تا یک میلیون تومان رسیده است.
🔹
دولت باید ساده توضیح دهد که آیا الگوی مصرف کاهش یافته و مردم را از محدوده خوش‌مصرفی خارج کرده است؟ آیا الگوی مصرف برای یک منزل ۸۰ متری واقعی است؟
🔹
دولت باید درصد افزایش و نحوه محاسبه را شفاف کند و شرکت‌ها درباره سودآوری و هزینه‌کرد وجوه پاسخگو باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/678568" target="_blank">📅 08:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678567">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35c5d533e.mp4?token=bmR4k4SMt3XvolMpzsIhk5FXEZDO0CVOoyJ0dfvt8y-UYFJ3PuW6-T1LwSyZW0BalMLXZ3WQQIyqoTIhiX2hDxznvVKesQAaIMSE0dtwajNdxrU413T37j9xeGxliq5Pe10t9a1zP9O0eV6znX-cLrQMOoZUY7-Lm0rX2hUvjrEEa6D8LNxU9wWFVlMbLnHpTT3DyBXQfh9hQm2_sh-4jHQYIcSP57pmaCa4UXjP6K7h09Lg1XKK3GNY2E7S-GTK42ACXroAUrBucmJ3EePQTyQacQ558L9WLov7_ckkYihUArXziMdVmfX5vUjtkaYy0tA_59acitrwub09zFE7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35c5d533e.mp4?token=bmR4k4SMt3XvolMpzsIhk5FXEZDO0CVOoyJ0dfvt8y-UYFJ3PuW6-T1LwSyZW0BalMLXZ3WQQIyqoTIhiX2hDxznvVKesQAaIMSE0dtwajNdxrU413T37j9xeGxliq5Pe10t9a1zP9O0eV6znX-cLrQMOoZUY7-Lm0rX2hUvjrEEa6D8LNxU9wWFVlMbLnHpTT3DyBXQfh9hQm2_sh-4jHQYIcSP57pmaCa4UXjP6K7h09Lg1XKK3GNY2E7S-GTK42ACXroAUrBucmJ3EePQTyQacQ558L9WLov7_ckkYihUArXziMdVmfX5vUjtkaYy0tA_59acitrwub09zFE7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نظامیان صهیونیست به قدس اشغالی
🔹
نظامیان ویژه رژیم صهیونیستی بامداد امروز با خودروهای نظامی به اردوگاه قلندیا در شمال قدس اشغالی یورش برده و منزل خانواده الخطیب را محاصره کردند.
🔹
به گزارش منابع محلی، نظامیان با تخریب بخشی از درب ورودی، غسان الخطیب (۲۵ ساله) را بدون ارائه هرگونه اتهام رسمی بازداشت و به یکی از مراکز تحقیق منتقل کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/678567" target="_blank">📅 08:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678566">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d714c9892.mp4?token=g7EWms0lRoob005t39oESfG_b4wR5f3AWcezZB3Zi3RJC6cQH2EG9CNVlKJVNQIoXfScfN3m6SsDc71F6BuELvA-msxotHmDxyslyhvM-Ji3EIhwkGvrnMlTIP-Of1aD_Z9i1ZY3PkdOzc_VE6Wtu7TCmEcluFchmQKuEs_FWAdMXGv8avfQj-Nw2mSneYKsPr2Z1cOOl2LQGW_JgowvH54hbnEz3m7XAppsfNB_rQcIu5IDlnlbAzwD9-L7yj1Db51ex5Az5XSZX--niJPHuquR-UcF6CumM7wAWwzCr0GIPzUs4scvjT128bnWqGYPHfMMJ-FZJ5R6HSwEp1WgsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d714c9892.mp4?token=g7EWms0lRoob005t39oESfG_b4wR5f3AWcezZB3Zi3RJC6cQH2EG9CNVlKJVNQIoXfScfN3m6SsDc71F6BuELvA-msxotHmDxyslyhvM-Ji3EIhwkGvrnMlTIP-Of1aD_Z9i1ZY3PkdOzc_VE6Wtu7TCmEcluFchmQKuEs_FWAdMXGv8avfQj-Nw2mSneYKsPr2Z1cOOl2LQGW_JgowvH54hbnEz3m7XAppsfNB_rQcIu5IDlnlbAzwD9-L7yj1Db51ex5Az5XSZX--niJPHuquR-UcF6CumM7wAWwzCr0GIPzUs4scvjT128bnWqGYPHfMMJ-FZJ5R6HSwEp1WgsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار شدید در مجتمع شیمیایی برزیل
🔹
رسانه‌ها از وقوع انفجاری شدید در یک کارخانه شیمیایی در سائوپولو برزیل خبر دادند که به دنبال آن آتش‌سوزی گسترده‌ای رخ داد.
🔹
تصاویر منتشرشده از محل حادثه، ستونی عظیم از آتش و دود را نشان می‌دهد که از فاصله دور نیز قابل مشاهده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/678566" target="_blank">📅 08:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678563">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjfIosO1dHZLrC0khqYk55PSnQWBBAPVPwWcum1lcCixIw_7zqY9rw_yRIfhKEeFA8MNdz8bP86lJoN8e6V0yTQT79DeaaK-EySkGBpeCpwQ9QBOFxKdy9swl7O73qBz7OrSUg6xXZvblH2gqlDjLO2ZMqIMdqwDu7plKN6IkIa9kTH0eHgHcDqEAz1YIzsknfHFgNdmDrQJN0G2uyy7FHuwp16YLHluKTFgT6itxPtJlTlvojCm6FxJ492TE3yodMfujEoNNzrQyPx9581dvEfihTB61S2qsNW7_ebkMFdC_X9pDITpPQHoz1x9Ex-sJoHauocfDuzP5f1shTayGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8y1RsNqViegEk7pZXkvki6YRJJomib6ZodFdky6uxqGXMLclgu4UQc52nr7t71ptHZSKoHtx24mKddT9jbgE2dzp4akEoqwnrn3GL5mns8g3yNnOEv5i6IvVrYudUwuvGjnf53LKsMGKN3-O1kB2zUostjzZseXKVeZiYg4Y0i--kG_tEjbcLezAATgEonZEU8ib-UmkLp7iBi-NaI-hj4F42GwvtwT_rdJjkQRmd1vqQ8v-GIvTVK_HYRZ5FHc_nQt9cjMfxja686sNji1AnkjDpshki2VH3kQAB-gszayZ4Wq0_MM8lZnLoXiQ8-RgLKcXtkq7_3lTRJuNRUVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqnJuTVfoyEfBId_Oed3-AA5kOfj80hEiZfbbCHwa1ah8uv3iWcuOLeYJKIzvE-DP6iBkagijNccROdfSSiqqquJwEqt3mvVkookLra7vGN0ZWDB_t4RnMe4pTxVZ8lM39huIYczSgPLdX-JfGLok7iegL12OzVyrzjRGLSCBl3zX9xB2MD-WIvxXwtBbCQtJGi4e7iUcePlGtFyxyUATXLHgTYtQabnRFiRxkYXBeUoNpGxQPqBbFeEe9T2YM1SJx3gkYSMkxQThnlBdd-ed5y2XliGtBQJxueZ4RuMEIc9mPracwTh1FggasVnld1_IN2jHKks7KJLGh1aG0spZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انواع میوه‌ها با قند بالا،متوسط و پایین زیر ۱ دقیقه بشناسید
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/678563" target="_blank">📅 08:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678562">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb6e658c1.mp4?token=SBpQn9EaKhqur40c-jwxYhH6k_QlxQmeorhJ8zq7MM9Vr5XMx0XOZQJiq7_Gu5aPe5D8IBRZY7IUHlQr9Nk5pnhpJnR44wYPx9BMynFd-1Ey3S_UgRqqeCcR-_dXGuaF1r5ao4_nxh_RwPope4SxbEAJdFqOLTEXQSEKG0FK_Dr5fjZxed_jVMecex5JbhEBhi8xYrlneZxES4SACai_nXr6wmYVmlRqi26-zc5Blz2I0xKEmbT1QexHtyKpKdTUNWILUcGS1gbT8AxB3W_Gohw1HjDAJuS6BkITL3dKWPPrP9rYdqeMM5g7zjNNF2JEev9x0H9rRO7oQfJaZsGKpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb6e658c1.mp4?token=SBpQn9EaKhqur40c-jwxYhH6k_QlxQmeorhJ8zq7MM9Vr5XMx0XOZQJiq7_Gu5aPe5D8IBRZY7IUHlQr9Nk5pnhpJnR44wYPx9BMynFd-1Ey3S_UgRqqeCcR-_dXGuaF1r5ao4_nxh_RwPope4SxbEAJdFqOLTEXQSEKG0FK_Dr5fjZxed_jVMecex5JbhEBhi8xYrlneZxES4SACai_nXr6wmYVmlRqi26-zc5Blz2I0xKEmbT1QexHtyKpKdTUNWILUcGS1gbT8AxB3W_Gohw1HjDAJuS6BkITL3dKWPPrP9rYdqeMM5g7zjNNF2JEev9x0H9rRO7oQfJaZsGKpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تمرین خانگی برای کاهش درد عضلات و مفاصل #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/678562" target="_blank">📅 08:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678560">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
مقام آگاه: دخالت‌های آمریکا و تهدیدات ترامپ دلیل اصلی تأخیر در توافق با عمان درباره تنگه هرمز است؛ ایران زیر سایه تهدید توافق نمی‌کند.
/ سپاه نیوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/678560" target="_blank">📅 07:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678559">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROUjg95XZOwDVOROdcZWvlxhFbyKNLJp2Xo1FxGpIdzPDBZzxSuDK73wlNoSiQ64I4DzthPo0c721sBI-dAhRmKWZ63RWRh28jknhlmf0256hv7CiVDnnyra1toE25-tFF4mYsL7xOeDl_-vBfBfzmKtiIC2nB5qx3uHBv-PO6iBH3mU35StKOiwwAT_YLepe_nIJZ6kJ9n2KzqZ8X6jn5McxKQiIozyo1_W4mHNXiIOEr4qzTGPCOL0IdYwa_cRw4E-aNQkO3MLh9IYO6KUq_xXOgjssycDF3WgcCdNrXrDu8hEvnZeqLGTav7gYCJlhinJ1fQZpM2ZAHn_oGvH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردی مسلح در نزدیکی زمین گلف ترامپ در کالیفرنیا، با شائبه تلاش برای ترور ترامپ بازداشت شد
سی‌ان‌ان:
🔹
مأموران فدرال حضور فردی مشکوک را که در محوطه این مکان راه می‌رفت، گزارش داده بودند.
🔹
یک منبع در نهادهای اجرای قانون فدرال به سی‌ان‌ان گفته است که در حال حاضر هیچ نشانه‌ای از برنامه‌ریزی این فرد برای حمله به رئیس‌جمهور دونالد ترامپ وجود ندارد و تحقیقات همچنان ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/678559" target="_blank">📅 07:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678558">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU_qoVAWzvcYIVygnNl4axqG0Dtm1TRFr7yyEy3YKyqV5_tDrqhYY2HWq2uRGvfWdvh_AounebpiqoJ3SYTMFOTRIOih3fke7AJ4BaHiq_veB1RB40LuSVEztMS_UANr4kS9kbmSBJIA9a76lxr76yMhlub2vV_TQQfjdWF3X6XTicGsrJ4caOGtqKpDwH1VLq1DE7QZ0rRslhdYI1faZuyn_2PR_PE91XdDHuOccTR84EaYr0_6Plhi8e3kbtTj-xZA2fkPWh_rDudyW70O9n3TNXLT8776E4ghA4F2aim5ALYnqt52S3bttVNUmGS9bo1GS7PQzYTvD7ZR7c_VKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
وزیر جنگ آمریکا، پس از انتشار خبر کمبود ذخایر موشکی آمریکا: خجالت بکشید و شرم بر شما باد‌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/678558" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678556">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
کالابرگ سه گروه فردا شارژ می‌شود
🔹
کالابرگ سرپرستان خانوارهایی که رقم انتهایی کد ملی آنها صفر تا دو است، فردا ۱۵ مردادماه شارژ می‌شود.
🔹
کالابرگ سرپرستان خانوارهایی که رقم پایانی کد ملی آنها سه تا شش است در ۲۰ مرداد شارژ می‌شود.
🔹
کدهای ملی هفت تا ۹ نیز در تاریخ ۲۵ مرداد فعال می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/678556" target="_blank">📅 07:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست‌ کافئین | فصل‌دو،قسمت‌یازدهم</div>
  <div class="tg-doc-extra">شهاب الدین سهروردی</div>
</div>
<a href="https://t.me/akhbarefori/678554" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
شیخ اشراق سهروردی
🗓
در این قسمت، بزرگترین کلاس درس تاریخ را برای «استراتژیِ اقیانوس آبی در بیزینس»، «مدیریتِ ریسکِ حامیانِ ارشد (Sponsor Risk)» و پرداختِ «هزینه‌یِ ساختارشکنی در محیط‌های سمی» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/678554" target="_blank">📅 07:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a969d0ce3.mp4?token=RJazzG7BT2Pj_2GzCykInOxPrN1ggu6u1syFkcMTvmS_jUp2sgAl5Vwp_W86jCoPTwd4vi6kjjLGsK1zLqhtqOsfY5uDcROglBn_IgXNhUvPZekV05K2J1p0kjGKSWrTCgUWqWjiz9MNGbjg4nBknK0NIiJClzvTMl5W4F9MysU2HeGia18h064uTVOohXU9YawGxSyAzW1LGDPEuFfzNhqAMJCKVxzRO1IMg4HAeH0BFGbDK253qrY8-21X1ncYrf3Ir8nBwhEK7EsZUIBkau9EXKmH0fSGHYZ-Jod7-njslQSZLiQ-6qPoB_wcA6PmzJ_ipPIaOcz6RaRfh9YvLpUn0PBC2yceBQU4jAhCjmH1eR1AUMUwpi8HeqBM3itkcBLya5B4MhtziIzGurnQLmo1Z1X-0CAja4S5-4FWSrX4ilMVBvUjzApCS6LSkp3RgOH5YQizKdd4SpOUKNZ00jvtUgya8eTWRZDQQ_IYddHIiq2gyL4VGhpYuIzwNM6Z7k6cIcL2DboBP5cTYrOuuW-o0J4qQMpI_GaUI_mUDHE17P4ZbWUmKu2becYj7zi-vR1AQjU9m_iq4137Scrq_7vFNdvuUFhr_KwGOieAUP59G6GNeDS9PGa1sEL-5yiWkUrj8bBNHh8dTQUBwgeZOZE-1LP9CIm1yws9YScq398" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a969d0ce3.mp4?token=RJazzG7BT2Pj_2GzCykInOxPrN1ggu6u1syFkcMTvmS_jUp2sgAl5Vwp_W86jCoPTwd4vi6kjjLGsK1zLqhtqOsfY5uDcROglBn_IgXNhUvPZekV05K2J1p0kjGKSWrTCgUWqWjiz9MNGbjg4nBknK0NIiJClzvTMl5W4F9MysU2HeGia18h064uTVOohXU9YawGxSyAzW1LGDPEuFfzNhqAMJCKVxzRO1IMg4HAeH0BFGbDK253qrY8-21X1ncYrf3Ir8nBwhEK7EsZUIBkau9EXKmH0fSGHYZ-Jod7-njslQSZLiQ-6qPoB_wcA6PmzJ_ipPIaOcz6RaRfh9YvLpUn0PBC2yceBQU4jAhCjmH1eR1AUMUwpi8HeqBM3itkcBLya5B4MhtziIzGurnQLmo1Z1X-0CAja4S5-4FWSrX4ilMVBvUjzApCS6LSkp3RgOH5YQizKdd4SpOUKNZ00jvtUgya8eTWRZDQQ_IYddHIiq2gyL4VGhpYuIzwNM6Z7k6cIcL2DboBP5cTYrOuuW-o0J4qQMpI_GaUI_mUDHE17P4ZbWUmKu2becYj7zi-vR1AQjU9m_iq4137Scrq_7vFNdvuUFhr_KwGOieAUP59G6GNeDS9PGa1sEL-5yiWkUrj8bBNHh8dTQUBwgeZOZE-1LP9CIm1yws9YScq398" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیخ اشراق و دکترینِ شجاعتِ فکری
​
#پادکست_کافئین
| فصل‌دو،قسمت‌یازده
☕️
🔹
​ابرنابغه‌ای که نشان داد چطور یک متخصصِ تراز اول، می‌تواند با فرار از اقیانوس‌های سرخِ تکرار، یک «نوآوریِ رادیکال و مکتبِ مستقل» خلق کند؛ حتی اگر بهایِ آن، رویارویی با فتوایِ خونینِ انحصارهایِ قدیمیِ بازار باشد.
🔹
​هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
​از اینجا ببینید و بشنوید
👇
https://youtu.be/1r5Ic2zOt5Q?si=4BsA2eVTJROtKpW9
​
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/678552" target="_blank">📅 07:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7DBbaUAmQ9rRrcYz-8n8N3mSlxYVogqm7aB7rcWkIrjmIuGSv6HGMgCPhdMQinEQAKNbBAzXsfl3UIMLdhcLQO1qRAW6itVYMJLYYqEI5qsvERn3lWOvkRP1VwfXabLCbOcYlOKsdraRJRselLpZpfwzOFKpmXruGit-rtW-9J8ozgDBRBN0DgXScyBquqVUVXT3sSB6vGQKA2VY7JqfksOBUXEuYdsjTVV3Z49golzWEudC9NkCcBVpttAwTKZ8TvLTGmmQXpSulVoQYacqdrSn0sCHWtiJKwpoq0mJ4TOfBO0EeDWR0RcrDlVhURHLpW_Mi66vOzY50M1ImDz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۴ مرداد ماه
۲۱ صفر ۱۴۴۸
۵ آگوست ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/678551" target="_blank">📅 07:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای خوک نجس: ما مذاکرات بسیار خوبی با ایران داریم / تنگه هرمز خیلی زود باز خواهد شد یا ایران متحمل یک حمله «بسیار قدرتمند» خواهد شد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/678550" target="_blank">📅 06:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678549">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای
آکسیوس: ایران، آمریکا و عمان به توافق موقت درباره تنگه هرمز نزدیک شده‌اند
🔹
ایران، آمریکا و عمان در آستانه توافقی ۶۰ روزه برای مدیریت تردد در تنگه هرمز هستند و احتمال اعلام آن امروز وجود دارد. این گزارش همچنین ادعا می‌کند شورای عالی امنیت ملی ایران هنوز این توافق را تأیید نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/678549" target="_blank">📅 06:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57c6b95cc.mp4?token=sxVTcwrPdREZlqdG66s6LWmFohKbN2Cf2TF8v9xkaw-eYwJDKNxPmjIumCH0hI7G_rwJ7X1fQcK1OBk4Kb6v6VDOFiHTUzo9WPEOAemXXWwIGWt86HTxP4BnY6a9liKEO8YFSmq0n9AiCgZBkONlVb1sQXFsXfJ7UejbZFZF8U7XClGojhWuBbBHsuk5quhgPTfAuYIDChgRxAotJOhiZE5gyuInRvEm5f1ZCuHaaTgKSKiNN79Q6_R_zl_O8np4rZryO2Fq9Kiq2vbzQJ3IUlkulQ3xtIDQEhwLRkXzwVb-WrmsjQCAtCwCT9EbNZqbhQOWwFTAvdB1hE_xxfZgsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57c6b95cc.mp4?token=sxVTcwrPdREZlqdG66s6LWmFohKbN2Cf2TF8v9xkaw-eYwJDKNxPmjIumCH0hI7G_rwJ7X1fQcK1OBk4Kb6v6VDOFiHTUzo9WPEOAemXXWwIGWt86HTxP4BnY6a9liKEO8YFSmq0n9AiCgZBkONlVb1sQXFsXfJ7UejbZFZF8U7XClGojhWuBbBHsuk5quhgPTfAuYIDChgRxAotJOhiZE5gyuInRvEm5f1ZCuHaaTgKSKiNN79Q6_R_zl_O8np4rZryO2Fq9Kiq2vbzQJ3IUlkulQ3xtIDQEhwLRkXzwVb-WrmsjQCAtCwCT9EbNZqbhQOWwFTAvdB1hE_xxfZgsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخاستن ستون‌های عظیم دود از بندر جبل‌علی دبی
🔹
رسانه‌های اماراتی با اشاره به شنیده‌شدن صدای حداقل ۷ انفجار در مدت ۲۰ دقیقه، ادعا کردند این حادثه شاید به‌دلیل مشکلات فنی باشد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/678547" target="_blank">📅 03:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678546">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXQqEavAPlsKMe9tyiJL6zB0KknWT1nmuaPCNQcfnoDJgQCM0YYbx2OMKiGzN2bv_dlMXbzYzoNsTAB8QwlS2miQlM_3Me1Gw9SLnGlkwDIW1DRD-P07sQiLrQavZ5CKhScs8PH1xjIgP5gZSwM_44UEsk0WAIb8vnhEPFtxW0BEU-kOyksTK8BecHJ9gfzQ_C_FLXN9yHYE7pLSAjIEvT9GGvfKBUPGIyC0ECuwnEfPmB1ZC8_8CrAYP__SICcDEgJt5-gHTYXNCYm0hg-QKTCujkL6l-32J4SXtXCjgJe-fTdAxdQ4SrRL68W4kzuF0rLmpYaUHi5u4-x9biBGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخاستن ستون‌های عظیم دود از بندر جبل‌علی دبی
🔹
رسانه‌های اماراتی با اشاره به شنیده‌شدن صدای حداقل ۷ انفجار در مدت ۲۰ دقیقه، ادعا کردند این حادثه شاید به‌دلیل مشکلات فنی باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/678546" target="_blank">📅 03:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678544">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emlOla60jvJIpylfVIzgpLE6aILAR2Xn7WpMYAGGl3sDlPewWedZSzZfVnJYNQMfQ0UppGKeRDMso7nOe2D8n5F0eeFFgppSmmF8L6Br6KEWWYWOyF8u_I0w8pPX3kGkIfHe6MgYx1cWQDikMmkv7N5s7M581gsVN94U8cpGG2uwvU3Zw_HXuWSD0D9KEJZCfgzqEhyiIB8GgzUfMAzvYXva17V6AYW_bFP8FMOQ_U5tz_tb_tvFSJy4V-r9qtyV_LTVvJjK5hJaxjNNFlyo1b2fRt43EIvOvdMgCAEj4EwCERTqQ-pfdDMD-vtRD81vBFZKTiqPqhHMhoK-uPNJUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8Mk9xj0ELRb5aKk6h9JVeqYK0O5Xs-MhC8mRLwzGBaYBiZ_gd9jYNTmig0H9GQQ8ugDkwzTIcceiN8DwTUQ0xc0htaQdLtqL6A70ldmdoZEdYc6mCwwbOcblv25Z7SEPr8mIsSnBBn88E9DXrgQqZYbnhsprdEqjoaaqKiJX5bHVO6Ti3GsIOMwV3Zu_g4fpKiuhFHnRtQxoRRM-sFUnw31EMvFLQsR5S7to_4PFgDw3MDgasSunlor39DPuAhQcSvo0KstGPuZ2AgK3Ga6y6oip0d-bRl8zgSS4-XCZsXFtlaDYrUClbZlaa7LntnVgSYRQjSa55KhOKdRENyoNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع خبری از حملۀ عربستان و وقوع چندین انفجار در صنعا، پایتخت یمن گزارش می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/678544" target="_blank">📅 03:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678542">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
منابع خبری از حملۀ عربستان و وقوع چندین انفجار در صنعا، پایتخت یمن گزارش می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/akhbarefori/678542" target="_blank">📅 02:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678541">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه نیک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5Rgv0tnED-tZvR_IzNzLcOjwqaY2nYkzXdD7q2CBczrWrd1PiLn2-fe_JvNbe-RJVXYUQC0Uo-wMiheMkyo1R5aEz__MJLSylRJx7urcjEO7YhSjRmA7rZtEraK8WIfC0tPcfyf8QvTsU9aB0YGdPlVGldQcdZ0Et7F8Xxcgf10DEna5GqzbgKwgeINEhIQJUHqPNL4YskAQwsIPkF9qy01iZ6AKTzoDT8vE2UMM9hB4U6mClLP5zDpGnSeS_K2eWBalieKfGOfpax-cmh7IZx6G3H5z8ba1T4Wva6C1IgjHEis3KAEqgmt6djryYFW8Fg0CzKDYKCISxMAzR6szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فقط ۲ سال دارد اما روزهای کودکی‌اش میان آزمایش، دارو و درمان می‌گذرد
😭
💔
او پس از پیوند مغز استخوان، برای ادامه مسیر درمان به  داروهای حیاتی نیاز دارد؛ اما خانواده‌اش با درآمد اندک کارگری، توان پرداخت هزینه‌های درمان، اقامت در تهران و معیشت را ندارند
🥺
بیایید دست‌های مهربانمان را از ارغوان دریغ نکنیم؛ شاید کمک امروز ما، سلامتی را به ارغوان بازگرداند
😭
🙏🏼
🌹
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
6037691990491185
6280237094218423
IR
110190000000216777746001
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@Pr_nikcharity
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/678541" target="_blank">📅 02:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678538">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6Z7fT1DNxbBz4fqGMCzVDMe2GqJKeHCdJ9VSJROMo-KMvWv9wyQ2_YSFPU5WTgzr0S93CSvS9Pfz05gPCLeIlex9_-uVvR7Xz3VmzcKzoEdAlXXps8hr3_Tbj_MDUA-y2M_9-FhUaHI7DmGBqyPi149nmzBNdhZ13atL65LcA_q1PxlS4eqq7MPoO1pQrO6dkmDpihX3LPOBxzNIlAcHz4JDCPbZkSC_ebtPiCHppoiqqNjSKJpgBYAaL7WIuO4rTywcc1D8AnGwnAaI_qmvkOIfFDzokRDAIN5ym-UKVXMgKAr-uJa6cLthf58wp1ka7KgR46DGir0Rh2R9myASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObiJfyQ2cq1n7Or3Vi-KUGWoNwaDLJuzhJuGsyMhFtsYriZV51yU_Gelp0mCQgi5hp6HtbM8wFQVSJAmAVL7BgZVbKFrFf3xxGEG2CnTYWRLv5AQHdm2pm_hWAMnFWhXFAS9tG6Zyzklmn5wz1jDlQvh_0f4IccKQGPyoW9uNrPo3wTHCH2Qy-vkh4XDhlZRQPJF7vHiXYkbHD_dy7evbhCo6G9BbmirtxlcvPI_jYbLxWx7sq2AwbEcsk7MC6uy2x-wcEFEGcso10HfhVjtYZQcW_kSAip59VpOjYPBeLy05ovCd3z3qfQR9qFmQGps356jTdeq7eVhUxUKETxAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxXaHBRyQL3_YtmlnhOyXcvauiCBOtuiyhCtKmbnDQ_A3CkWI7Z5n3nJR4NAs2P_TOTxprowNB6EwVCDLM-FRSLZEWK0MaGPhUdbvgnyPSGg7NiYRGZ-8sTV_JKk8_PnzUIZwTIVNc8fQFOidZzkE3sPeDmegW15LIzup4Q1Wncbqn-oIXOC0ZzfWI1kgV76-Md2Xl-e74_K6tkIx8SsejH0L6q3_WzNNg9liT6hLazSp96ZLdE48iKsVQOwL2dIHfcVJ0QlgWC5ypFqvqHRaO1jBWbNejKO0Nnr_Xoi1gO1-ugN1BaZUoHWtAgpoghWEAH69AUx4MSF7PQOAfWV_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آسمان کی‌یف دوباره سرخ شد؛ تصاویر تازه از انفجارها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/678538" target="_blank">📅 01:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678536">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
المیادین: بیش از ۱۴ عملیات زمینی اطلاعاتی توسط ایران در اقلیم کردستان عراق علیه گروه‌های جدایی‌طلب انجام شده است
📲
‎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/678536" target="_blank">📅 01:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678533">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hn_-iUjhTfVHI81PPPai0AICDM10kRSYOhBJlvfj7qNEsgRReDmOXbrcMt2Mhqy9JCCXkhl4MKb6lRQdc82d84DgUtpEqonIcDKKFCCLCIiFteaG7uW60dc8hxe8pyx08X_p9oVxeULmWa0M_WVJ5Ewxdq7mnJNFDfNh-EzqqvVY_QQ1j3woyp5TbfQDYx_NL2-slzhJQQn5D_MtXvoonGKK7RW3nz45m224mSSTe9vmJ8x74CLZIxjPwMCFWeZZPtRWFdpgUmYQqjOQjPR74Me4WIW3o8PH3hnrDZJ3bu8RFAJ9-kKQAZ5rqXdqp-Lx_LYate37QL5AD82JEYzDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDLKM5NV3yLfYMRx3PpcZpfFOTcW1IJ_y-LHgn4rTlVpmGVu3cAmx4d6YxzL0qMTBhNq70R3qHN2fE304lKCQtSI0dZVgvkIbKAGH7On1FzzXVQsvXXjpXHgYdWnEi5Cfgi7SBPzGayR974hj6vq0cuvWqMjStepWd9_voor04AR5ClnOtEMTKjd71cbz_qMWZEBg_X-VB2lTjNzKdLneWDDO6kQE6L5slAZ0fVUeO7CsxFzsixIBF1nXBT2o-0MnanpwBGm5SaJWqR0zQUG4AqVk4N8ef1Sbld88m7tT7MfG-P1m76BCX7xdjYlOgSNk4cIRf0pA50Oi8KCZZjX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Whbf4vEG3IG5riYG_y8VyJUftJg6MHUbF56o64V-3dOgkQjkyptMivWNdPHUK7yZW0sDtg7nqrCCHm2a8H51Lico2DvYyHDnmzI19tRxtvdmHfrB3I4UEb0I09w7cO_lEz4ePPCSHtMHdAU_ar-ttorIl4NhEVEKMd_a5wMMWgvK3w8v54pxJnEPaluf5kX3zQjyEsd3Zj3iMleelQrauphGCrvA7Xxw6vK3S-42ywCZMZ9k-xRynOMOx4pSYtiUxTXl99LhWmqqeJGU0YAyz7_QAgn0fh96jezvAk6qn2BIPDdnV8ozXdZ8r6W1Mn5jqcQu5L4bDcztu_gXIXz_Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اسباب‌بازی‌های من
پست جدید رونالدو در اینستاگرام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/akhbarefori/678533" target="_blank">📅 00:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678532">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای روزنامه انگلیسی درباره طرح ایران برای تنگه هرمز   روزنامه تلگراف:
🔹
ایران طرحی برای بازگشایی تنگه هرمز ارائه داده که به‌جای عوارض اجباری، صندوق داوطلبانه با بودجه کشورهای حاشیه خلیج فارس و اروپا ایجاد می‌شود تا هزینه‌های دریایی را پوشش دهد؛ الگویی مشابه…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/678532" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678531">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/decb6d0f68.mp4?token=qSB5AtUHD91sk6ot9y8N_kOJptW-RLOpZG5nDimg4gPs-vMKMblx-IyCznlRjunrHRblYAFqK0OjoMs8yZebu7Ch1kpjt5FO_d7pLq0ZPrIJ7Ba8nxhApqX3jJwhtghuDyR4VtScPIcXkWEm6A2YoigbvUksKCXWsRRRf-tI5sP_5Ts6eo1rPxr70sR4F2uI1LnNl5yaR1vYCIdjYbZhsZ4F-2RQGMkUMrpCyQM0D1H59sx5aSAuT7l5wd-ZaZwqTzlfD7QcZYVKuXkpJ8PDjG3Ncq2j-VoTIQqrYkFo0P8Rg2Z1zBi6z1vv19rLqiaFZ9yMuOPhOslIJXmIPWTPmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/decb6d0f68.mp4?token=qSB5AtUHD91sk6ot9y8N_kOJptW-RLOpZG5nDimg4gPs-vMKMblx-IyCznlRjunrHRblYAFqK0OjoMs8yZebu7Ch1kpjt5FO_d7pLq0ZPrIJ7Ba8nxhApqX3jJwhtghuDyR4VtScPIcXkWEm6A2YoigbvUksKCXWsRRRf-tI5sP_5Ts6eo1rPxr70sR4F2uI1LnNl5yaR1vYCIdjYbZhsZ4F-2RQGMkUMrpCyQM0D1H59sx5aSAuT7l5wd-ZaZwqTzlfD7QcZYVKuXkpJ8PDjG3Ncq2j-VoTIQqrYkFo0P8Rg2Z1zBi6z1vv19rLqiaFZ9yMuOPhOslIJXmIPWTPmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای پرچم من
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/678531" target="_blank">📅 00:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678529">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سی‌ان‌ان: ارتش ایالات متحده تقریباً ۸۰ درصد از موشک‌های رهگیر تاد و تقریباً ۵۰ درصد از موشک‌های سامانه پاتریوت را استفاده کرده است
🔹
کشورهای حاشیه خلیج فارس نسبت به کمبود سیستم های دفاع هوایی ابراز نگرانی می کنند که بر توانایی آنها برای دفاع در برابر پاسخ های ایران تأثیر می گذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/678529" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678526">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNA_nd4Xsm5zrUwUuTdiDK910_NnD9Xh1pdezI0_lCwd1iRfQyZA-ZgFJhvdeArnlijVfNP1fcFcjIy96LZfGkDBO6x3hYCskuF2f107s_PxufI2bTStWdYVtDeNHp7jFGbaB-MzpsSZjDisxUqo7DrPUIFOUu4v-KZ6SBnoHLY3c9LFbdkkXaOI2UvLzCTDEzCF-q3LAWlEhgXC0MleHwzI4YIC2KDBG23C7xShEm5OHYWb7EtchhtLQMwkekgiJ5x6Y5zHBsFIBGMEF19cuzTiCpqUEdFtLdEMTtKbaD5TZVo3UqkOkwfXtSPOSFc0B6y8ny77W9sdcSZw3gatww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رادار اصلی فرودگاه نجران عربستان در حمله تلافی جویانه امروز انصارالله یمن منهدم شد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/akhbarefori/678526" target="_blank">📅 00:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678525">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
قائم مقام سازمان تبلیغات: تجمعات مردمی تا پایان ماه صفر برقرار است
🔹
در خصوص بعد از ماه صفر هم جلساتی در حال برگزاری است که تصمیم گیری می‌شود و در نتیجه با دستور رهبر انقلاب اعلام ابلاغ خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/678525" target="_blank">📅 00:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678524">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای روزنامه انگلیسی درباره طرح ایران برای تنگه هرمز
روزنامه تلگراف:
🔹
ایران طرحی برای بازگشایی تنگه هرمز ارائه داده که به‌جای عوارض اجباری، صندوق داوطلبانه با بودجه کشورهای حاشیه خلیج فارس و اروپا ایجاد می‌شود تا هزینه‌های دریایی را پوشش دهد؛ الگویی مشابه تنگه مالاکا که عمان هم از آن حمایت می‌کند.
جزئیات بیشتر
👇
👇
👇
khabarfoori.com/fa/tiny/news-3235497</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/678524" target="_blank">📅 00:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkUuLcfmUuwAuABtHkc4yt2wpimio8FvgBQkduXX4FAyPBGBtB9UBZcfYkEjgtdXpknZT_JoUuyDXI6mMTthsCYx1CSo50YXjS7tsn7cV0acwqYORHCmJ27g9uG3QiRR45OSY3crJERsvbqGYjbcAGpRfQHChJvQ9-muBnXwDL5BlTL8LnakRTVqxDl1TppnDKa6tUK95WTMiC6VbFYJvirBHhCn4JWwz_3o8cbp_aquoeFgUNnM3skO6CaL9Z6T5j-Dgric_qy_xdyR6TubMy2ShpGMekawJwwMMqizGdu6lT2s0KDOQpTMQvuFogvOhKdNaVTDWixiDkcceQcIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/678522" target="_blank">📅 00:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678520">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab59d1739.mp4?token=B_Y27YUlKWHmkBc7jkNuufzC0WvknDl3jpwSUM9tHYMQEjFaM3NWxhOFLBz53dJ01jpFdDHse3P8ihmQXcykwPUheudDLXr75XQIgzq68-cV0nyidt518mJqG8hK0vU1LfiLvUEzxu_RKoDmWeW9vnf5ZuUMRb0t6_Z6NxrOFcOxcK-Nrik_KJyRV5nLuCrPB5RLGOGtHh0AF0-FNLExW1vO09eBcZEA5BVB8DbF2X3u-6ycuyOVBHJkMa7EWEhh9WCjLCmEeN3nwSNCrAWp3ccUiLsIgO1gadvY-w3YFTp6gZnmtnNwALL5RrC6QKRE7DmHWzUPxqWmdXKO42Mmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab59d1739.mp4?token=B_Y27YUlKWHmkBc7jkNuufzC0WvknDl3jpwSUM9tHYMQEjFaM3NWxhOFLBz53dJ01jpFdDHse3P8ihmQXcykwPUheudDLXr75XQIgzq68-cV0nyidt518mJqG8hK0vU1LfiLvUEzxu_RKoDmWeW9vnf5ZuUMRb0t6_Z6NxrOFcOxcK-Nrik_KJyRV5nLuCrPB5RLGOGtHh0AF0-FNLExW1vO09eBcZEA5BVB8DbF2X3u-6ycuyOVBHJkMa7EWEhh9WCjLCmEeN3nwSNCrAWp3ccUiLsIgO1gadvY-w3YFTp6gZnmtnNwALL5RrC6QKRE7DmHWzUPxqWmdXKO42Mmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم جدیدی از حمله ایران به پایگاه آمریکایی در اردن| ۵ روز پیش
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/678520" target="_blank">📅 23:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7duq5_VPWgIO4zTic_7FWGoO6O3v8xdKnY4uX931HI7A5QOqYGCM37asXLI_0CcE7uTJfcuE5_0N_d3Lou-jtbdLvcxcyGRjlkTpyRGSwu3ia-ZeSFqLO1RC6qJ7shijfngc_3FGS2_q1oy8wHNZwoZPZfJ_FNNB6HAK5ibAbnqSvUlW2dQ9VoLl5w9Ackvv8_zwTfW2AAVj5nWvBjO87Czo8U--malCwMGrlTzM7fDMR0iBF3B5E0i-bD8fROk44aOT17OZ8GEDwUNFzFIaRJaOKCDg0c2DUj2d6wmulODWj2t6rrfdhm_nzk8DcDUAyXYKcMSfEkzs1nYf3-MMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McCb7dCiTBosp_6zNFmctOXM64CKnuJHsfY7nzdnJveZl3tnEdFFQBRPuSQKzM_xKE1-Nv_9S8EWtwER65Exq-bmR4aGP6dSXbNlAvTwqg7YXg5oDzGL1HLOZ6KZG_NRbPJaW2_j7UierczrvjSMhKe1QBeV1PSGUowgYPcjNFuKcdQkPqrmtlWjaCbPiqXLNHI2nsM37rLgIU-SxpHJ15i8lmx2Y36C2_52coK54tZmL5BXoa6DP8lSHNDNC2cnr0--gj0FglztcKpJ74DX20wbGKM7K0Fbedv6F5sLrAKKsuIMYJZ1el9lRvcTx1xsVvNq5MLyNVtFYNQLv_-m-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FiSoD6g_UvQSBtcHQuVQXNTc7gDXbe7kK7sJAfaIR0cgxojrCqDHM25tT-m63-js1Gehmrz2MXt2bzChvlsAgNMcVUKneCKUaZOAaa1HF1JXi7fFVbxjWtcRbNeiOtoBLNDnUZWCdwbShQ-KFj4jJmi7ShpwImdk4Msi9i7knZHyRMHtIvUtASX4FzowqkCnAofB7bqO7yNFF6YDUEOdNJ-PYroNgcS5n2k-rjmsCxGFyMfeVB4sJVxSmuqWQIzWI8t4mT6eWm5DeMKOQqixd2YtEeUBBpCGb4WXY_fG_4ou_6xjXTAUBWE29Hem4XAMWEtCCxUPDLm9YAIvyddwDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدل جدید ناسا نشان می‌دهد زمین مانند سیب‌زمینی است
🔹
مدل جدید ناسا نشان می‌دهد زمین کاملاً کروی نیست و به دلیل توزیع نابرابر جرم، شبیه سیب‌زمینی با برآمدگی و گودی است (تفاوت واقعی فقط ۱۹۰ متر).
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/akhbarefori/678516" target="_blank">📅 23:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hunqc9GlmMeGIzK4G1XWK9r_l16YbPn5q2CIBRmUD_0xlR7_sM8o1QqDokiXrCRBWIsdtzFKDQ231e9LCRNbspw-vLIxvgpu_us7Aq5oKazF2Fq7TsMaNbsWeUpJuKB1CuRTSP3eL_K4GbPpy_s7pmUigIekX8vVPGPoMdMkGWGEAM0qQ3BdHjCnKf99I1tAL_ogWGM7yFcG8lFT0UYzQil24gesBwY0DggVo2zd0V_LU-KmwD9G9D91BfxH7waN4TbZi1tYEnb6T5_GtZ6B_VVa-4jobS8sJTmbUB0SdhydD3IjYDM-8522aj8_cL9j7IIcabiL5COVfbQSG4mP0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWKEqPIPb9K_1HGXiveje-3Qme09AQ72OT2Dkm6wjeYsIZNqMnwsVx09mL3EQm-JgCHBKfBs3emW-JSxu3Z390FqvzUkJOWlKro5FdDu0_dlR1cBtJSVwM5YkjhDoaW64jF9DZrOg02r4Gkzpo1zrmEQBqozYAWl8I9BBi0yb5b78A0zAojQrgFEluxQGoIuY8QUxlDOwubu8h-06AvImZ00zujzT02PjRfsPRlIj4Arn4uNl33sYZSr5fzyoO_7NQuiN0o2MFFyqf2HvarwdbvI_l54nU2pR0jBIuKOQr4t6Tm9hckU-lhL2svy6csg16fnweXXxifajPacOIcFtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
♦️
حزب آزادی کردستان (پاک) اعلام کرد که در عملیات چند هفته پیش نیروهای ایرانی فرزند حسین یزدان پناه رئیس این حزب کشته شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/678514" target="_blank">📅 23:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678513">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ec74cdad.mp4?token=Jx-av-XhnoUeBT5Y3HpcCO-HE4WgsLIpkiQ3lwVjUcsrtZJRbRXc7-pBiU2nQK0mUXcal3JIefquYgtM0U6RTKvShp_t-25GoyylG2ZWOzdRAK0AV7fqLrmG434v9kevD-JqUk1A4Ae-bC7bf6dbfFVOpymfJ8JwmKPcneN_cVDbNY_apj5r6ItgxqCJwjjVfN3QmVSCsJnDpo8alKzXjxztW-GAx76cJaB4-nzVOsMTVFp9WlN67REgwWkV76q_oV508nkk-ArXNe_D-OVndWd0H5iE1_X6FiLWDHIXTjtb9p-XOOja7BAg9X5N6UPjecz6BHgjZw5b0x_kijoQwp4-Xe_edTYdEJYNg0lE5BHmtA2Azi559BA717Y0g0_81OhAdPlMRnmnZGM3zharDn9tLfppNp4eDic9Fjvjb4j7lIs5U3h7vRJo7J6JBPepqhG3zMseQgWVib9uf8sMbndUnuslqa-u8LzfATXPFFPlEIhUA8ZZVZVcCJ0a_M7W7Obm3LmJfHGME6K54h_SeJODEumPHD7W0-lA5dzg5_aG2Io8_REUqGpePXEkUU_XZIko18mFtr2eQMBXSiCJw65CatpA-otDc3wrCIDB6tON-S43Lz8PbphshDX8cwyz8aamm2xll-k3eqSN1-gV5s7x2KV1FivLDJmN36OScrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ec74cdad.mp4?token=Jx-av-XhnoUeBT5Y3HpcCO-HE4WgsLIpkiQ3lwVjUcsrtZJRbRXc7-pBiU2nQK0mUXcal3JIefquYgtM0U6RTKvShp_t-25GoyylG2ZWOzdRAK0AV7fqLrmG434v9kevD-JqUk1A4Ae-bC7bf6dbfFVOpymfJ8JwmKPcneN_cVDbNY_apj5r6ItgxqCJwjjVfN3QmVSCsJnDpo8alKzXjxztW-GAx76cJaB4-nzVOsMTVFp9WlN67REgwWkV76q_oV508nkk-ArXNe_D-OVndWd0H5iE1_X6FiLWDHIXTjtb9p-XOOja7BAg9X5N6UPjecz6BHgjZw5b0x_kijoQwp4-Xe_edTYdEJYNg0lE5BHmtA2Azi559BA717Y0g0_81OhAdPlMRnmnZGM3zharDn9tLfppNp4eDic9Fjvjb4j7lIs5U3h7vRJo7J6JBPepqhG3zMseQgWVib9uf8sMbndUnuslqa-u8LzfATXPFFPlEIhUA8ZZVZVcCJ0a_M7W7Obm3LmJfHGME6K54h_SeJODEumPHD7W0-lA5dzg5_aG2Io8_REUqGpePXEkUU_XZIko18mFtr2eQMBXSiCJw65CatpA-otDc3wrCIDB6tON-S43Lz8PbphshDX8cwyz8aamm2xll-k3eqSN1-gV5s7x2KV1FivLDJmN36OScrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو خبرگان رهبری: صلح و جنگ، مسائل راهبردی نظام، براساس قانون اساسی برعهده رهبری است
سعدی، عضو خبرگان رهبری:
🔹
اگر بخواهیم از امنیت ملی صیانت کنیم، باید بازدارندگی ایجاد شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/678513" target="_blank">📅 23:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678511">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_mABFZtTqrsWv7mQ4jukctZgDjLGadpG19NeehBVNNdrpz-HVf1Gq_82AdM_8lhOzKPkfjVjMlkGQOZo4-4WViHDb_hkHh4jjjZtdF5VrxXXn_R4n9Vti_Dbj4-J4i3_HHHO72K9kyYmS724wOI78geLspLqEd1Lf-RK0zd79A32Erv53zjcCWUSNIxmNVL3bIaFZpdfhdNyVfW1jBBd0p6VZwShO1jppfcFuEAWcfX5v4bktCXVYGzSA47u032V6yFO4jp-v5ni9riV65WXUMhe8nAzvFUE1du625PRj1NaKxFz32cHAOy924FX97USj0NcHy0AsaKybO8B8Gxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ زمینی ایران و آمریکا چگونه خواهد بود؟
🔹
واشنگتن سناریوی حمله زمینی به ایران را همچنان روی میز دارد، اما چرا تاکنون آن را اجرا نکرده است؟ در این گزارش به بررسی مهم‌ترین موانعی می‌پردازیم که آمریکا با حملهٔ زمینی تمام‌عیار به ایران با آنها مواجه خواهد شد.
بیشتر بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3235498</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/678511" target="_blank">📅 23:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678510">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
سخنگوی دولت: شرط تداوم یارانه نقدی و کالابرگ اقامت در ایران است
🔹
مشمولانی که پیامک دریافت کرده‌اند، تا پایان شهریور با مراجعه به دفاتر پیشخوان، اقامت خود را احراز کنند.
🔹
اعتبار مرداد این افراد واریز نمی‌شود، اما بعد از احراز، معوقات پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/678510" target="_blank">📅 23:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678508">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/678508" target="_blank">📅 23:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678507">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
الجزیره: ساعات حساسی در پیش است
👇
khabarfoori.com/fa/tiny/news-3235497
🔹
واکنش دفتر رهبری به ادعای مطرح‌شده درباره قبول استعفای احتنالی پزشکیان
👇
khabarfoori.com/fa/tiny/news-3235491
🔹
«نوستراداموس چین»؛ پیش‌بینی جنجالی درباره جنگ علیه ایران | دو پیشگویی قبلی او که محقق شد چه بود؟
👇
khabarfoori.com/fa/tiny/news-3235477
🔹
انفجار در شهرک صنعتی شهر ری
👇
khabarfoori.com/fa/tiny/news-3235460
🔹
توئیت کنایه‌آمیز ضرغامی درباره جنتی و دبیری شورای نگهبان در ۱۰۰ سالگی
👇
khabarfoori.com/fa/tiny/news-3235499
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/678507" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678506">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
آغاز عقب‌نشینی یا تاکتیک جدید آمریکا در منطقه؟
🔹
گزارش‌هایی از خروج نیروهای آمریکا از اربیل و احتمال کاهش حضور در کویت، بحث‌ها را داغ کرده است.
🔹
به نوشتهٔ الخنادق، این تحولات بیشتر به بازآرایی نیروها شباهت دارد تا عقب‌نشینی راهبردی، زیرا رویارویی اخیر با ایران، آسیب‌پذیری پایگاه‌های ثابت آمریکا را در برابر حملات موشکی و پهپادی آشکار کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/678506" target="_blank">📅 23:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678505">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8RM7zJPohiDh2a6AAZ_7Pfx_BIAxMgqoVuBSTEGpZTxLiCi9yJ50B0lRlg6ByDvCkhFbIBOcACiM-8KE27qKXnRXteGR5UU79kZArMmUcgGVYR9YDw79L9OqE6EglLfAUxDEPbGaEcNAiqf_zkVtt8QxZ8GN4NGsO8W59g1ztERQHx-98fHSzgSzUgkpzPBWldSR-qcnjfqxSwfjcCEzxOljTeGkzgevl210kH2426akY6ANnY6iwmto1f78AeOpmUL2dHWgHnpu5_CT-vCMSnxwgXt4fu8KcnZsS4SyiTFOjzxnIiovl6aYqwJVtn9Ov2OHn5_ZAeGEUbxQbTccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواب با کولر روشن؛ دشمن خاموش بدن؟
سه نکته طلایی خواب با کولر:
🔹
دما را روی
۲۴ تا ۲۶ درجه
تنظیم کنید.
🔹
حالت
Sleep یا تایمر
را فعال کنید.
🔹
رطوبت هوا را حفظ کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/678505" target="_blank">📅 22:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678503">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U98c0B6YDd8QW-z3B5y0hAVcfFtlZ7MkVwlBBj42poNz3i5F-hzFn3lVhyo52c20jFL4bPA27Qedc4VW3QQ06YPzd_yKakyTkLjy7vO8ySIsMnaV4098Mw_d1w62HPA0qdLcObAMdtosz5UE5bZqaGFvR9etFHDqB1ZJKDHqml9PetMmQpQIGip5hUwYaVAKOLTEkrk0aRb1Iy17AfiIfmztzAZ7ZngS8S-mZZ9WXzbSuPaQMM8uWmqJ54RJ_qAc_4gq3YSmEPniD1E0DBkhRMC_Y6Ui8kg53IDkGwq1VTdmI0jCxl7kTfQ9PrgAcDIn_dX77Ej9x4kkQP8_spr2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادآوری به جا اکانت سفارت ایران در آفریقای جنوبی، از توییت گذشته خودش در مورد نحوه کنترل ایران و ترامپ بر تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/678503" target="_blank">📅 22:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678501">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuPCmgewSdGCf6ocOjFeXAyya-xaQU4DF8UsgWFTi1jslW0Ahl_VvRO3gAKagIKzNL0g1HYRX5bD3S3cBKnFIqBjcKOe_N41JRVYQmcDD8xUFXYY2KsL03aj9PLo4hKWnX8LMBSWmBkiBnJAZrN7qZf-6zRYAOTtl1NCRD5fEg5XGu2_jHP0Nua-SykRjAi7OxvT3ooenSOU5Ky9zjcSR2pkEdcVlfxzH5K3knUqmnXcZ-EgZsk1i1aHuoOKqAEzYrwaXwDkMA4ipLKji7g-ECTWgqyAb2x2RVpOJynzyZGlYXOhLgFUCligCNtQG6xga-erYX34MYOcR4ByOhDcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9eec3cf4.mp4?token=j3BQqQBH27StBILuX-03oWb-rZe0LQ2a2js4nNh58uBTcfSruBaN9FZHvIA9HDv5EKpRy31qdRU8IFQ3F-wXbILkkW-0IWkgxMgYRjWxbbgilA0kWQ9Fq6-rbrmJTeY4xh2FH8LNOFNVM-1Pr9ULIWIfX5C4nf85umvq1lvt94He4aqdZLLcvIf79-XKoPIiOKXnorO04WRddKNFbmjwPu3OuuClKDqwop-744F-ddepiBsw0aFrj2r4xYlWXRS_nqLrq74zSMqXk_OdhpyVRLquGoz12jvzXE2mVpN8fhRRLlUhgl854wVTgjvMqaPCZl9URGNzsl-LMOs-Lvk6ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9eec3cf4.mp4?token=j3BQqQBH27StBILuX-03oWb-rZe0LQ2a2js4nNh58uBTcfSruBaN9FZHvIA9HDv5EKpRy31qdRU8IFQ3F-wXbILkkW-0IWkgxMgYRjWxbbgilA0kWQ9Fq6-rbrmJTeY4xh2FH8LNOFNVM-1Pr9ULIWIfX5C4nf85umvq1lvt94He4aqdZLLcvIf79-XKoPIiOKXnorO04WRddKNFbmjwPu3OuuClKDqwop-744F-ddepiBsw0aFrj2r4xYlWXRS_nqLrq74zSMqXk_OdhpyVRLquGoz12jvzXE2mVpN8fhRRLlUhgl854wVTgjvMqaPCZl9URGNzsl-LMOs-Lvk6ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا چین دست به تهدید اتمی آمریکا زده؟
🔹
چین برای نخستین بار تصاویر هوایی از بمب‌افکن H-6N منتشر کرده که موشک بالستیک هوابه‌زمین JL-1 با قابلیت کلاهک هسته‌ای (برد ۸۰۰۰ کیلومتر، بازورود فراصوت) را حمل می‌کند و دو جنگندهٔ رادارگریز J-20 آن را اسکورت می‌کنند.
🔹
این موشک هم برای اهداف ضدهوایی (کشتی‌ها) و هم حمله به اهداف زمینی قابل استفاده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/678501" target="_blank">📅 22:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678500">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2db0ae20c.mp4?token=bySAXCOPqUU-pynlCilvyeD58DBEu4NX9Oh1rMPn7qJqqbc3p4NDpJuclA8Z0Jpc1Wopgk1kl_0gJ8zllVFBcQOAjKr5fYuaB1F1kcpG3bEnlCR4kfRso6SZrPC963dayg55FK4fC0fdY0OreVIxyDKXcW3qRMfDjHxqAbKtHoCXnAl9rGjHInDhmLYplK5FpiU0XFKIpb1zl2fpF0wFbV1auCoufiSXS4ToOhVh-R5N9rYkZuhDH0FBgpEHqx2CO6EupyrAzkeUwVx77Z-EgF8hzKWG1ofLUaE3XOqE4I-1SpAXrkvOwBG_Ma9b1PcyXabfqrqc61eLFyzbUG8k2A9hjMa37aeZFaG2D3m_YUN8sTwnmctxnnetB3YeEwJ8ARiwny0dB7yJtePAUimYDP61Y4sQ_cTjjvzQqYdq6oCB7D-kdYuftg_Wux4JgnQCJ9yfbCVMgzutKZK5hFu24XgURbiYx4So0lAQA8ynFOyq1tRVOwF3vGnrQ41Rfr3K80Umrr-V_DyzVgDsHakKbpIF19ippNxD8e5IPK-icYcMn4jIvIIhIfw1ut9RQ2_aB9t4YAnAjA8BtrwgtJe6IvfQlWglO-djFFh9s8tOdXEhALoGTGecV5PeETQUKccJGQuj63shB-DU3lEwjlXv6lsVK_4RyX0-vIcfZyQfcOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2db0ae20c.mp4?token=bySAXCOPqUU-pynlCilvyeD58DBEu4NX9Oh1rMPn7qJqqbc3p4NDpJuclA8Z0Jpc1Wopgk1kl_0gJ8zllVFBcQOAjKr5fYuaB1F1kcpG3bEnlCR4kfRso6SZrPC963dayg55FK4fC0fdY0OreVIxyDKXcW3qRMfDjHxqAbKtHoCXnAl9rGjHInDhmLYplK5FpiU0XFKIpb1zl2fpF0wFbV1auCoufiSXS4ToOhVh-R5N9rYkZuhDH0FBgpEHqx2CO6EupyrAzkeUwVx77Z-EgF8hzKWG1ofLUaE3XOqE4I-1SpAXrkvOwBG_Ma9b1PcyXabfqrqc61eLFyzbUG8k2A9hjMa37aeZFaG2D3m_YUN8sTwnmctxnnetB3YeEwJ8ARiwny0dB7yJtePAUimYDP61Y4sQ_cTjjvzQqYdq6oCB7D-kdYuftg_Wux4JgnQCJ9yfbCVMgzutKZK5hFu24XgURbiYx4So0lAQA8ynFOyq1tRVOwF3vGnrQ41Rfr3K80Umrr-V_DyzVgDsHakKbpIF19ippNxD8e5IPK-icYcMn4jIvIIhIfw1ut9RQ2_aB9t4YAnAjA8BtrwgtJe6IvfQlWglO-djFFh9s8tOdXEhALoGTGecV5PeETQUKccJGQuj63shB-DU3lEwjlXv6lsVK_4RyX0-vIcfZyQfcOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعجب گزارشگر آمریکایی از پرچم‌‌های قرمز در دست زائران ایرانی اربعین امسال و فریاد خونخواهی
🔹
ایرانی‌ها میگویند خون در برابر خون و انتقام باید گرفته شود
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/678500" target="_blank">📅 22:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678499">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHumcFAURfjLZS5vHuglkE_yJ4QtzJcFLXld03ubgBu2w_XGqJWDw5wIun6fu72rsZi2cZKiCPuItgaKQXcjayoK7tE3G6oFZJ2UeKNPtTnem9PgkfG_ghif1couMZoo8XQ3XIVwf6pQGrF0njyZhtBShTe4JFv7pjmOQMAyt-vVZYELyd0yqFQKoVqklldp9tJBAEVW7mcUmU3pPmkQRvQo_vX4txCCpd68AB3x7BWezNdASjY1HCIZV4KfIhk4slB9mmtfum_FjIVxLwfSe5OwUhob5qlsGOz7uHglnYrPiKR0e1CKbkpYKvn3w0nvH27443Ye3zCc-Rw7rG_5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست اینستاگرام ایرج طهماسب: غمگینم بسیار زیاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/678499" target="_blank">📅 22:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678498">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09fcd91286.mp4?token=JRg1UPn_xGcfDXTavFwO4OfRFA8eSy6EdrtCY--eAfPva6Gmsxi-Cp_pCYj9fBVMUtp5B3DYsA0-NJK1Gom7fPCdmnJrnrirSl0KQ_VS50kycQH0_IR5ng7m2cYRkObCem2LPhUL8pR1fT9Tx0v0R52hyXDqw0kGjM7A-C2oyh105a-g8KBqFb7Yo6EoyeaMNSnShr6sWXmHZVvfPv9lphLSZaSOSRQSb41_-R6ELDoYjSP00SNuxFqNaVRCtqMmtk83h99KU1xC-jJDE2x19k1cQzmODr3tuQYmdEaXGi6bV3DoeKGTAlJDAsLxYp3_YGOHJvBDYpkxTInJqkNCDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09fcd91286.mp4?token=JRg1UPn_xGcfDXTavFwO4OfRFA8eSy6EdrtCY--eAfPva6Gmsxi-Cp_pCYj9fBVMUtp5B3DYsA0-NJK1Gom7fPCdmnJrnrirSl0KQ_VS50kycQH0_IR5ng7m2cYRkObCem2LPhUL8pR1fT9Tx0v0R52hyXDqw0kGjM7A-C2oyh105a-g8KBqFb7Yo6EoyeaMNSnShr6sWXmHZVvfPv9lphLSZaSOSRQSb41_-R6ELDoYjSP00SNuxFqNaVRCtqMmtk83h99KU1xC-jJDE2x19k1cQzmODr3tuQYmdEaXGi6bV3DoeKGTAlJDAsLxYp3_YGOHJvBDYpkxTInJqkNCDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی عشق از نیاز فراتر می‌رود؛ نگاه متفاوت به ازدواج
گری زوکاو نویسنده و استاد معنوی آمریکایی:
🔹
ازدواج در گذشته بیشتر بر پایه نیازهای زندگی، تقسیم نقش‌ها و بقا شکل می‌گرفت؛ اما امروز می‌تواند فراتر از این باشد؛ یک همراهی آگاهانه که در آن دو نفر علاوه بر ساختن یک زندگی مشترک، به رشد، شناخت و بهتر شدن یکدیگر کمک می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/678498" target="_blank">📅 22:29 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
