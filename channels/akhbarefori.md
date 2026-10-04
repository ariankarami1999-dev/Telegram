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
<img src="https://cdn4.telesco.pe/file/O9LKj1Nmkh2fkDLMfdNxOlU_C0KkNVDgd85j-_4C_s2nLcreJANANuxd_vx-_kEb9vSA0_j4KocvTmmZJnHEB7SCxpycY_CfEFy6dtpgvcXpegT5HdnMSapQDvXVxKxa3jvqVaN0yQsrjOvalTilxbYCBMeHY7vuZLSl6iHlo9Nuo8c9-3mxTZEKetnU2I59psxegz4931VMLAHmMx-MfRy77CUNhmzy_rhmw-RNP_aW19tSVXxd9xMn57uak-uyIcr270EgNFElnIvKZ4UsP7QRdWHFdSjnSUuIX6lNIf77EySW1gJkChw6BxlM9j2_0u7u_hOwK49hIx2jWsoGaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-695600">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu9PDfj20hAojRLOqgt97kqXUzdo7LnFjToSEbRIM-ZqS4Jnkd-UtwjVsfIHd3yCo-slqbMVymtCFSM7txBd8FbzqdEeBl5PHCOusnTSbANWqGycUlAVmBzY6EhR42GVxMU9coL8by_bjApsLpQtZlmCda4cS217OwgJjGuEjO3KCQtNTcC3u1H9xS8KdiK0dMHdZjOuvBmz8O9vH25u_6aJAUufSeWewmG5zjI3EylrW-oQBPB68SzCt418FxXEKKQ-8UggtCidJ0Wgl8JMS28rfl9nhV68BZqBgZ6xV3Kr2LPrahU9tM4AqCTFgniEVdNG8bQvWt2i4CKiUwd71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری از خط لوله شرق به غرب عربستان که بار دیگر مورد اصابت یمن قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/695600" target="_blank">📅 20:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695599">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
وزیر نفت استعفا داد
معاون دفتر پزشکیان:
🔹
با پذیرش استعفای محسن پاک نژاد طی حکمی از سوی دکتر پزشکیان رئیس جمهور، حمید بورد به عنوان سرپرست وزارت نفت منصوب شد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/695599" target="_blank">📅 20:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695598">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b07137eca.mp4?token=BgpA4hDoxUok7L2uNRV25Z1_rBTt46btI6iz2PLTaOUESgYian0cIn6qRSgrMAiwdt5rm1HBZADiy5NX_KCTUqOh2Sdq4QbYUqakNUyBfzdKlFaEewFJU1Nrwc40wv7yxiTxvVk6kMznjZ2g6CQ7IqPmklWaqo9ilvj_o2UHAhLiikZVDwH2jDrbqtPPpw-YPzz9NLbcM9ILlKNY83STkf-Zoa08Opjv9FLCRRrVNp5jg_0EyXCoqAGx1j2URcovPmdn8hFdlDnMpDAXSI2vbVcoquQ8mYaEU2tH8jU-6QVTJOVass_Db0t8Q_xkvG23MToCQacULbj7yNbDNnYWkIlJQIP9wxLnK5KAXjvL3SqgeSn-HiMU_67_EXSFFETa46RHGoC6oWIMkb11Lwj5V84HlZvO4gHPs-y651anFJce8Ki8529lmEUVP4FNBGLIXoxJz-hHdwNKEE2X-8vJIhEQNw65NYPgEBJzMN3qYfWd0Dwhx9mTDc_HfAlFNtqI5KKWSw-8KRbR_ySsL7Gt8aYctUuQj5Yp8S9NvHl8h57nx_Gx3bth83iO19jYtmoRLbkhV7YbbmDCTUxg3srHKtW0p808Rd1p2ozZNePFT2vudLqtbsO5QfKSrcFhWZyayzV4P5tE10UMcWeqhxftk_93LppLhZcKMSNAxsXgSmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b07137eca.mp4?token=BgpA4hDoxUok7L2uNRV25Z1_rBTt46btI6iz2PLTaOUESgYian0cIn6qRSgrMAiwdt5rm1HBZADiy5NX_KCTUqOh2Sdq4QbYUqakNUyBfzdKlFaEewFJU1Nrwc40wv7yxiTxvVk6kMznjZ2g6CQ7IqPmklWaqo9ilvj_o2UHAhLiikZVDwH2jDrbqtPPpw-YPzz9NLbcM9ILlKNY83STkf-Zoa08Opjv9FLCRRrVNp5jg_0EyXCoqAGx1j2URcovPmdn8hFdlDnMpDAXSI2vbVcoquQ8mYaEU2tH8jU-6QVTJOVass_Db0t8Q_xkvG23MToCQacULbj7yNbDNnYWkIlJQIP9wxLnK5KAXjvL3SqgeSn-HiMU_67_EXSFFETa46RHGoC6oWIMkb11Lwj5V84HlZvO4gHPs-y651anFJce8Ki8529lmEUVP4FNBGLIXoxJz-hHdwNKEE2X-8vJIhEQNw65NYPgEBJzMN3qYfWd0Dwhx9mTDc_HfAlFNtqI5KKWSw-8KRbR_ySsL7Gt8aYctUuQj5Yp8S9NvHl8h57nx_Gx3bth83iO19jYtmoRLbkhV7YbbmDCTUxg3srHKtW0p808Rd1p2ozZNePFT2vudLqtbsO5QfKSrcFhWZyayzV4P5tE10UMcWeqhxftk_93LppLhZcKMSNAxsXgSmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس صداوسیما: در صورت حمله اتمی به تهران، سه‌میلیون نفر کشته خواهند شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/695598" target="_blank">📅 20:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695595">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEva7vPAaB2DUPxoi4-5TnxMUikjdy958z64w51AbQG8RX-zQ1tNaAEUsUrQ9osHqkrJ1KDwvILmHdYdlPwizSRJ7iwRKz0VawV03fjZC1aJUb3egdPN6UALcJYjtnUogwDVOu4VZ6MM8E1CMfejDy76siZxSbOFBEln0vlFCdoIXfeAsi5VcEQd_xmDkcKqe4WYJ8u1RsDBe_pVw66JA_neJxdz6q-NEbjAf8S2mCT-zmzGArKZyq0Cq45vgpOLAJ0qBxb3hhzBRtT64TtYDmwPr8GmdV3ookKoJsFgCzbCqT-WSNe6-FJjYurum5JqNYAvx99uytLFbRaixa0LzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d738f2c41.mp4?token=L8SSQOyXWPT1ZtQRX5ZY85UBD_JwFE_FrRLajw91YG3MUU1-DJmGIVQ59WEizlVDO5198c5dqAoaWpA0LVUsDC4J1dBduWPdKvf_po4oUANTzf-7epbRJBhIZ5i9UEYKMI9Ns1D_YvMFBoDaeWXnVtO5vtir7O29ge9ACkSr5LKfLFMxgwutbYfArj8mC9umT5hH9HMEkG4LndmvJoNCoVtsEM0xq3xFVJgxpm9OGlX9jseJULvQ4vxk8KSOPo2Zv6EaWwNwee1tRFalkMzva4U7YJ4TIUgdUNeOQOcseZ9Hx489LxMsadz9L8x0fQefpCSeo48iBxNMxuNJQF3tOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d738f2c41.mp4?token=L8SSQOyXWPT1ZtQRX5ZY85UBD_JwFE_FrRLajw91YG3MUU1-DJmGIVQ59WEizlVDO5198c5dqAoaWpA0LVUsDC4J1dBduWPdKvf_po4oUANTzf-7epbRJBhIZ5i9UEYKMI9Ns1D_YvMFBoDaeWXnVtO5vtir7O29ge9ACkSr5LKfLFMxgwutbYfArj8mC9umT5hH9HMEkG4LndmvJoNCoVtsEM0xq3xFVJgxpm9OGlX9jseJULvQ4vxk8KSOPo2Zv6EaWwNwee1tRFalkMzva4U7YJ4TIUgdUNeOQOcseZ9Hx489LxMsadz9L8x0fQefpCSeo48iBxNMxuNJQF3tOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاق عجیب در کنسرت میثم ابراهیمی؛ پلمب سالن پلمب شد!
🔹
سالن برگزاری کنسرت میثم ابراهیمی در شهر پردیس در ۱۰ مهر، پس از برگزاری برنامه در ۹ مهر به دلیل نداشتن حجاب مخاطبان و ورود بطری های آب  معدنی پلمب شد!
🔹
این خواننده با حضور در جمع مخاطبانش از آنها عذرخواهی کرد؛ ساعاتی پس از برخی پیگیری ها، کنسرت با ساعاتی تاخیر بالاخره برگزار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/695595" target="_blank">📅 20:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695594">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-LNekFeaCvYGtHwKG1aqipBVfmwjBna3B5t1ZyKlWzCYZ-BFymteatXMa0Pm6akuVdgyBrUoYBYHvOgY1zRKgnK1brcAv9ke_t9bpvEXBssXs7qbHoK1sqeDCtuT0U0qnrn_xiEiaraklhL6iU-zEL6SFeL4RZ82H_W1IERKP04b_Gciq2f0X1-SZe69UVlbrvVnf03Oq7vjIEoHtih08NrcqPM9_2ZJScdE5hlC8TIqcPltcMNPKllnL0gVoiLoLTQfPxKRtj83AZFlMoToddSdjbyjj6PL9gGR16_P27Pp_TU-t7x_eHrNUBp7vLCt8N3NEgGf95sv6j07jx_FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳۸ابزار هوش‌مصنوعی با کاربرد‌های متفاوت
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/695594" target="_blank">📅 20:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695593">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592495b982.mp4?token=TZIOO9QHL7-y7_q7VlhDvh-yU1tAPeCJeMGDg2DfuyotWrHrMhwj9RWssEObLgHzIXdaQ42ShODVEqSXf25kJMgcwX_eGi1Gq4D84EbIc6Y-5DJaG6wh2oS6srHHDCsoHWhfT3rz4ABZuM3yaJXw4R8bKexvDZimygVwPE3jZC-fk2VMwVjGM75Im0iG2X0E9bG2HL-a_leWJ-HHuv6RUx8QMgqY9LavIvPM3vUYxNxpwbWV-72YhzHgOTxbJ5kmqSmuopkj3iLpQgjeGyQfqDnQQRllOERVGfN2YH2fCQKgAkE5yjtjj5DSKSWnn4Z1as6zD1L0omwkelqyKklNhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592495b982.mp4?token=TZIOO9QHL7-y7_q7VlhDvh-yU1tAPeCJeMGDg2DfuyotWrHrMhwj9RWssEObLgHzIXdaQ42ShODVEqSXf25kJMgcwX_eGi1Gq4D84EbIc6Y-5DJaG6wh2oS6srHHDCsoHWhfT3rz4ABZuM3yaJXw4R8bKexvDZimygVwPE3jZC-fk2VMwVjGM75Im0iG2X0E9bG2HL-a_leWJ-HHuv6RUx8QMgqY9LavIvPM3vUYxNxpwbWV-72YhzHgOTxbJ5kmqSmuopkj3iLpQgjeGyQfqDnQQRllOERVGfN2YH2fCQKgAkE5yjtjj5DSKSWnn4Z1as6zD1L0omwkelqyKklNhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بالاخره کی پاسخگوئه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/695593" target="_blank">📅 20:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695591">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16e95bbad.mp4?token=awl84j6n90QAi89g6pRx_wg9le6O_EvcY2fb_BtFU3ER2j5Vca4VvG_d1asPGySf8fX3OPd6G9fDyMHCElLyaUAuhYB0OFIUli9aiTcIIL1WGUglqtcnHOBhIj8MPmwThgFMrqMvAm9XM14bL5JSR5pbUeEVHIekSPH-NKK0rA5Fg1NhHv-a0O9ROdH6WpreRGDOfN3dp9L7X_lBBDVl76gn4XLgDTEOtFfaw9XAgSThDGyWvhSVc_7S4JsINEuHJj1_KlDL_8JvBQEka8Aogqp-PivH4Pmo9qA85KDMg4m9EE7b3rM1ohMNuHsx9bx_pML7q0WHbUcvpeeALj8YgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16e95bbad.mp4?token=awl84j6n90QAi89g6pRx_wg9le6O_EvcY2fb_BtFU3ER2j5Vca4VvG_d1asPGySf8fX3OPd6G9fDyMHCElLyaUAuhYB0OFIUli9aiTcIIL1WGUglqtcnHOBhIj8MPmwThgFMrqMvAm9XM14bL5JSR5pbUeEVHIekSPH-NKK0rA5Fg1NhHv-a0O9ROdH6WpreRGDOfN3dp9L7X_lBBDVl76gn4XLgDTEOtFfaw9XAgSThDGyWvhSVc_7S4JsINEuHJj1_KlDL_8JvBQEka8Aogqp-PivH4Pmo9qA85KDMg4m9EE7b3rM1ohMNuHsx9bx_pML7q0WHbUcvpeeALj8YgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه عبری: ایران، گورستان پهپادهای آمریکایی شده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/695591" target="_blank">📅 20:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695590">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">22-1 Ane Manaee (1404-02-09)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/695590" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌ودوم؛ بخش اول
🔹
"فی قلوبهم مرض"، یعنی ایمان واقعی در گرو “توحید” و “ولایت” است [01:09]
🔹
تفکیک امر خدا از امر پیامبر و عدم تبعیت از پیامبر به اسم عقلانیت و مصلحت‌گرایی یعنی نفاق! [09:56]
🔹
اشتباهاتی چون فراموشی، نشان‌دهنده سیره عقلایی و انسانی انبیاست، نه نقص در مقام نبوت [14:53]
🔹
پیراستگی جایگاه پیامبران از هرگونه خطا حتی در امور عرفی! [28:32]
🔹
مصلحت‌سنجی" یا "انحراف از حق"؟.. نقد به رفتارهای رسانه‌ای در ذبح اصول اعتقادی به بهانه دلجویی از برخی! [31:58]
🔹
"سکوت در شرایط فتنه"، رفتارهای تاکتیکی رهبران الهی برای مصالح بلندمدت بدون خدشه به اصول [38:27]
🔹
اهمیت حفظ محکمات فکری - عقیدتی در شرایط ابهام‌آلود سیاسی - اجتماعی [43:04]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/695590" target="_blank">📅 20:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695589">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما کدام عامل بیشترین نقش را در حفظ فرهنگ ایرانی در میان مردم دارد؟</h4>
<ul>
<li>✓ خانواده</li>
<li>✓ نظام آموزشی</li>
<li>✓ شبکه‌های اجتماعی</li>
<li>✓ نهادهای فرهنگی و هنری</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/695589" target="_blank">📅 20:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695588">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/026bb1441e.mp4?token=RPxATQJbz_WIbjT82jQjgP1u0gVn1cBJyaBRoRYHkjDPRxfc4WWnyd2wfilVGq2Uoc1-7yner7Pdd8K1iBeBhNJqOW1RQ8yyUWkF6TzBJfcGYSS8UiH-Ss-yU-7kfaSUNRAqMACaqax6IG7uoRj9QLcRD8WYbwGOQHEjHG0Y-TP5H1s6uj6lLqd1DD-LQBKu9x5X-GKuMBrsiDwEBcPWMPSUd5WRkZ3R6Gc5dIabs7XFSrD-ZD_uHX6FvvjLaOGWT6mtp1tfQ7jbLR4Or2r0FoV--hZMwxQGS9pdMI6mgZoXNk_xvoA_kgEvUXoZH1WkDUdcNv95-TwHB-egb7AYkyM3EKjDfk4VLsCtLyV_EkkKODORPGoaXt5bp6N506vkG82XaDsiGanmvvvbi-f_gCOlps0vqV29cygOP8R3UhtD-9L47d30Qi4M41kJhLzr2hJtIjKa6tvidzO9ys9GWECESsfeWSh9g7XFFDaA9EkA_WMInFxeWgGCdOUFZpjD-JP-dZoGbAdSSmHqav_pQLBeJHTsSUxI4rHAd_tiU_bt76fTIPMzR58_93IKfbRX3R2XPsXRj3bOEOmhNNey_XQqlEWqgJnm87KHKNVO8wix01BmGTWODqcbw3pbKXbJiXc5P7NSHbQYerzsMcXdi8Rq6oZykmpkHNhDRb6XgQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/026bb1441e.mp4?token=RPxATQJbz_WIbjT82jQjgP1u0gVn1cBJyaBRoRYHkjDPRxfc4WWnyd2wfilVGq2Uoc1-7yner7Pdd8K1iBeBhNJqOW1RQ8yyUWkF6TzBJfcGYSS8UiH-Ss-yU-7kfaSUNRAqMACaqax6IG7uoRj9QLcRD8WYbwGOQHEjHG0Y-TP5H1s6uj6lLqd1DD-LQBKu9x5X-GKuMBrsiDwEBcPWMPSUd5WRkZ3R6Gc5dIabs7XFSrD-ZD_uHX6FvvjLaOGWT6mtp1tfQ7jbLR4Or2r0FoV--hZMwxQGS9pdMI6mgZoXNk_xvoA_kgEvUXoZH1WkDUdcNv95-TwHB-egb7AYkyM3EKjDfk4VLsCtLyV_EkkKODORPGoaXt5bp6N506vkG82XaDsiGanmvvvbi-f_gCOlps0vqV29cygOP8R3UhtD-9L47d30Qi4M41kJhLzr2hJtIjKa6tvidzO9ys9GWECESsfeWSh9g7XFFDaA9EkA_WMInFxeWgGCdOUFZpjD-JP-dZoGbAdSSmHqav_pQLBeJHTsSUxI4rHAd_tiU_bt76fTIPMzR58_93IKfbRX3R2XPsXRj3bOEOmhNNey_XQqlEWqgJnm87KHKNVO8wix01BmGTWODqcbw3pbKXbJiXc5P7NSHbQYerzsMcXdi8Rq6oZykmpkHNhDRb6XgQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمارهای عجیب و غریب از میزان تقاضای استارلینک در ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/695588" target="_blank">📅 19:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695587">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db760fe162.mp4?token=AJWPuBFctHu7mG9B3A0YHVuVTKu423XQkYcs0x9LiDYKXaqhFMVwgtMgCrwqt-gJ03ogGru4AOmya_-2ENvYCMxbAAcL1ma2cL6xsCB2ziugEKjyCxqg29Ngg8iOrS6qAmgJKPTK3ClvrhnUh9cpDaWTrH_sSsmLRcgJInu84n_u_c7TSJ7mTu32BBREo-rf21FzMdzGFhoUbub2201r7fwJ8ox-oa-onN2c1ae7gUewy3EDi42SDVI3o1fJeDMWtcot6WT4y4f_5Ppws7lSlDlEZvDQK1b61lMvlXvNZ619alTTgpvm4Ac8ZdASITBX5zzBFIGUS-3Qm5gdI4Afrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db760fe162.mp4?token=AJWPuBFctHu7mG9B3A0YHVuVTKu423XQkYcs0x9LiDYKXaqhFMVwgtMgCrwqt-gJ03ogGru4AOmya_-2ENvYCMxbAAcL1ma2cL6xsCB2ziugEKjyCxqg29Ngg8iOrS6qAmgJKPTK3ClvrhnUh9cpDaWTrH_sSsmLRcgJInu84n_u_c7TSJ7mTu32BBREo-rf21FzMdzGFhoUbub2201r7fwJ8ox-oa-onN2c1ae7gUewy3EDi42SDVI3o1fJeDMWtcot6WT4y4f_5Ppws7lSlDlEZvDQK1b61lMvlXvNZ619alTTgpvm4Ac8ZdASITBX5zzBFIGUS-3Qm5gdI4Afrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سه‌ترفند کاربردی در آشپزی
🍳
🔹
سیو کن یادت نره.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/695587" target="_blank">📅 19:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695586">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال اطلاع‌رسانی سازمان توسعه تجارت ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31788f03a.mp4?token=jTIL_S6qV0iEee532eqhlfvD6vm81qNjPdBi9w-qcmvt6_I00r2cf_aGUrp3aLD16gTqzYKTLLX7wIzI8_I9oeAPg_zlQv504x8Giw3J_URru0FjoemUhnU6QqQt-4hDSp7r4KvVaJsr8HnXvGZD19A4PMeCjm7o5oTuUCsPTvxspN7QA4siCTQadBu-mE_s90ivh-xVB5GjdKfWIHGcSdF0eg2VvTLE3sih8VaUjAqWl3qrLvSIQwpPKSHkcww05coJSODLygDvPNZGUClPTjE9R3GeW8QQ7mwt62EoYHhzx_-IL0neabiOlE4vi87Yebwj3OGpTvys7Sm9hZ22DAbrzcnNRSIESghz_aEkiUgx3HtKrBAe_xY67NwQwtdKZkt4YvXn4Uk05Tbi-i88tNSb7bGDKeYv4BN9ful1Cuuys8hXCQuKCfydAkHzIPPvz0A90v82_PneC5ji8rrE2swPOeK3BeOPbnhTbfpNyPZFrjfwRNe99w7AqS_dXZr_RtCizTx5VzC0_yvFh1ePXaCxwtT1gLNadvqZAVTmoDChCYQn5uxR1t1id69hDKesPv_692FzDmHKUAV9hK2IBY-dZkIeI8z4-alC_lIwL69G2FxjaBjA_vpGNpHZrwA-mObGY-a9cwFMGbuJmnJnU3XwxgLTzUYMF1NcE2vsCPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31788f03a.mp4?token=jTIL_S6qV0iEee532eqhlfvD6vm81qNjPdBi9w-qcmvt6_I00r2cf_aGUrp3aLD16gTqzYKTLLX7wIzI8_I9oeAPg_zlQv504x8Giw3J_URru0FjoemUhnU6QqQt-4hDSp7r4KvVaJsr8HnXvGZD19A4PMeCjm7o5oTuUCsPTvxspN7QA4siCTQadBu-mE_s90ivh-xVB5GjdKfWIHGcSdF0eg2VvTLE3sih8VaUjAqWl3qrLvSIQwpPKSHkcww05coJSODLygDvPNZGUClPTjE9R3GeW8QQ7mwt62EoYHhzx_-IL0neabiOlE4vi87Yebwj3OGpTvys7Sm9hZ22DAbrzcnNRSIESghz_aEkiUgx3HtKrBAe_xY67NwQwtdKZkt4YvXn4Uk05Tbi-i88tNSb7bGDKeYv4BN9ful1Cuuys8hXCQuKCfydAkHzIPPvz0A90v82_PneC5ji8rrE2swPOeK3BeOPbnhTbfpNyPZFrjfwRNe99w7AqS_dXZr_RtCizTx5VzC0_yvFh1ePXaCxwtT1gLNadvqZAVTmoDChCYQn5uxR1t1id69hDKesPv_692FzDmHKUAV9hK2IBY-dZkIeI8z4-alC_lIwL69G2FxjaBjA_vpGNpHZrwA-mObGY-a9cwFMGbuJmnJnU3XwxgLTzUYMF1NcE2vsCPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🔻
سه دهه تجلیل از قهرمانان صادرات
🔻
🔻
29 مهر؛ نماد تجارت ایران
🔹
روابط عمومی سازمان توسعه تجارت ایران
پایگاه خبری
|
تلگرام
|
بله
|
واتساپ
| ‌
آپارات</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/695586" target="_blank">📅 19:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695585">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: در کنکور امسال یک سؤال برای چند دقیقه درز کرد که به‌سرعت شناسایی شد و به‌گونه‌ای نبود که بر نتایج کلی کنکور تأثیر بگذارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/695585" target="_blank">📅 19:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695584">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افشاگری نماینده مجلس از گروکشی کارتل‌های بزرگ برای دریافت ارز تا همکاری دوباره دولت با آن‌ها
پیمان فلسفی، نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
برخی کارتل‌های بزرگ وقتی دیدند کشور با کمبود ارز مواجه است، تهدید کردند که تا زمانی که ارز ما تامین نشود کالا را تحویل نمی‌دهیم؛ به نوعی گروکشی کردند.
🔹
این‌ها در مقطعی بحران درست کردند و به بازار نهاده‌های دامی و کالاهای اساسی واقعا شوک وارد کردند.
🔹
برخی از این شرکت‌ها که تعداد آنها به سه تا چهار مورد بیشتر نمی‌رسید با عملکرد نامناسبی فضا را تحت تاثیر قرار دادند که باید با اینها برخورد شود.
🔹
فکر میکنم دوباره همکاری با این شرکت‌ها شروع شده است ؛ وزارت جهاد کشاورزی و بانک مرکزی با این شرکت‌ها کار می‌کنند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/695584" target="_blank">📅 19:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695579">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">honar_v1.pdf</div>
  <div class="tg-doc-extra">18.2 MB</div>
</div>
<a href="https://t.me/akhbarefori/695579" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دفترچه انتخاب رشته کنکور ۱۴۰۵ منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/695579" target="_blank">📅 19:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695578">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تمدید ۲ ماهه مهلت خودروهای گذر موقت
🔹
گمرک به مدیران مرزی و استانی اجازه داد بدون مکاتبه با تهران، مهلت پلاک گذر موقت خودروها را ۲ ماه تمدید کنند؛ این تصمیم شامل مسافران و سرمایه‌گذاران خارجی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/695578" target="_blank">📅 19:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695576">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KD-b3nV9NUuiHgEbqw-A-0TAb6rzoPDDKxuwjeAUB6QhBHvsYercy7Mo79alwewfnQp54XAQtAa27zXKVY4j1armAUczJef0yBVceDg2NGG1cvzHgyROb_vPzI0-X6VvoAO4viWISyzhJNTADUTddjofSRvaA7ZHf65XGcZ2bCOnDfxH4qgWcsmZoc90paOZkBdlEXBZGark2e2WY1NSyaW7MxCJKLE_xDVSJp6MxwCkyF98cJ6nNL7IPKluBp9aMD7ULI_LxEuKW8FUXD7LxH-X38YYIKL-MzLI7Uu2aYrTXARy4zQjwNHnuotBI06fTdZaE84y95LXS8AGgyLA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqNXn3wHePMjvfvggvtB7RJiNh9GOWQPhd2jVbFYZnHsqk1afOd2ffQx9_jCfGe4XZ0LdYjJOg7P0Ytwhry4-LmGyLD1Fj9e7lhuxmeM6CwUSQVlXL5alMUgbHUDSGDZ9mZmbCqymNiyyos2hKpbZIM2-65NJCMzbrV-0UrQUUNl-WeJ-sZEeVkoEQfOZTUTxlIxFKVbTgxZ7UAo8g-q45CYBKFz8OD63A9JylHeL1IwDHcTHmonX8VWD-qAGzvk9eQ-cxTdyzXfOJ9PNGRuKsyE5s0yhzZquT10F9Yfx2_6pp6e_f8qp03-TGlwky7GggIqt-qr4E8W3_WVKA6f6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عکس اتاقتون رو به ai بدید و منتظر باشید تا با شناختی که ازتون داره اتاقتون رو دیزاین کنه
:)))
Use the uploaded photo of my room as the base image and redesign/fill the room based on what you already know about me from our previous conversations.
Your goal is to make the room feel like a realistic physical reflection of my personality, interests, habits, hobbies, taste, lifestyle, and the things I care about.
Before making any changes, silently consider what you already know about me, such as my interests, favorite activities, aesthetic preferences, technology or gaming interests, creative work, entertainment tastes, routines, and other relevant preferences. Use only information you genuinely know from our conversations; do not invent personal facts just to fill the space.
Preserve the original room itself as much as possible:
Keep the same architecture, walls, windows, doors, floor, ceiling, room dimensions, camera angle, perspective, and overall layout.
Do not turn it into a completely different room or location.
Keep existing furniture when it makes sense, but you may reorganize it slightly if needed.
Add, replace, or decorate objects only where they could realistically exist in the photographed space.
Fill and personalize the room with items that make sense specifically for me. These may include furniture, decorations, technology, desk accessories, lighting, posters, books, collectibles, gaming equipment, creative tools, personal objects, or other details that naturally match what you know about me.
Do not add random generic decorations. Every noticeable object should either serve a practical purpose, reflect something you know about me, or improve the overall coherence of the room.
Make the result feel lived-in and believable rather than like a furniture showroom. Include subtle everyday details such as naturally placed cables, objects on the desk, small personal items, realistic storage, and signs that someone actually uses the room, while keeping it visually organized.
Match the lighting, shadows, reflections, scale, material textures, and perspective of all new objects to the original photograph so everything looks physically present in the real room.
Do not add people.
The final image should look like the same real room after it has been thoughtfully personalized for me—not a generic “dream room.”
Prioritize:
1. Personal relevance
2. Realism
3. Preservation of the original room
4. Functional and believable object placement
5. Visual coherence
Output only the final transformed room image.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/695576" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695575">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6J65YQ5pVDc-IGpxN5Fpy-Pc6McwNo2bN1mqaxdWdizGfnrxy0UuV6J7-sZUefkN185STfmh36Ou4LRM-Gyoz4fQFJ4uMGFWzm4UhDn9aVPqhQgHD5eqggeX4tCB_BglVav9NhtbLoEIizr4onVBF77pcfUOhwknduFiMuNbKerfigDWMJMUYl8Zl-7irybJF3qHV5uHAG8htsVC01rem7ug8-0nWbyvWzeDC3NxbXgFFVGau5dOZKrnsEEeThoIihGG6QyXGk7ykTUsCT-v7-A-XKWbL3b-r-NHfkJVSSPh-tjzr1UPfDHgtYmNw5JXjyhWtryHDZ-47PXzfYpdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو دفتر سیاسی جنبش انصارالله یمن: با یاری و لطف خداوند، تعز آزاد شد و آرامکو ریاض و خریص در آتش می‌سوزند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/695575" target="_blank">📅 19:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695574">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
حال و هوای هالووینی خیابان‌های آمریکا
🇺🇸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/695574" target="_blank">📅 19:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695573">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8sjn4Mabu-F-L5lRWnMYQmSEShj1KrEiMGK0pvHI0dM0i_lnVrj_8qw8EFZYmeT2hHgR_UaKLAqtiQNpMm2v82Zfs92cfM7QVgmWgrmuFVOWartMbjTPmsYF513TZfBtYEXxq4xzyu_HdSAlIQqWReIMJMjP6ZlACtVOXBVCWyZ1_WKeqAW5k9r1IxmAAbpVp4ECqSBM-aWigsqMDJlj577jUq8_Y71rPuOfE3Cy11n64054sCB6vYueEWpwIqbmsuNZZvLJI2n6FrCmBE6seaEmxKHgyXD-0NP9qcEdwbfs0Oi1z8gJzxSw7iqf6JTX1d0PEc9i3z21TzdgzMZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی در کدام صنایع بیشتر نفوذ کرده است؟
🔸
بر اساس پیمایش جهانی McKinsey، فناوری بیشترین میزان استفاده از هوش مصنوعی را در بخش فناوری با ۴۱ درصد دارد. پس از آن، ارائه‌دهندگان خدمات سلامت (۳۹٪)، خدمات حرفه‌ای و انرژی و مواد (۳۸٪) در رتبه‌های بعدی قرار گرفته‌اند.
🔸
گسترش هوش مصنوعی در صنایع مختلف نشان می‌دهد شرکت‌ها بیش از گذشته از این فناوری برای تحلیل داده، اتوماسیون فرآیندها، بهبود خدمات و افزایش بهره‌وری استفاده می‌کنند.
📊
آمارفکت | مرجع تخصصی آمار در ایران
@amarfact</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/695573" target="_blank">📅 19:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695572">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وزارت ورزش و جوانان: ۱۴ میلیون جوان در سن ازدواج در کشور، مجرد هستند و هرگز ازدواج نکرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/695572" target="_blank">📅 19:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695571">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سرقت ساعت ۵ میلیاردی سفیر فیلیپین در تهران
🔹
ساعت طلای سفیر فیلیپین در تهران از خانه او در شهرک غرب سرقت شد؛ پلیس یکی از پرستارانی را که برای نگهداری از فرزند سفیر استخدام شده بود، بازداشت کرد.
🔹
متهم به سرقت ساعت طلا و برلیان اعتراف کرده و تحقیقات درباره پرونده ادامه دارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/695571" target="_blank">📅 19:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695570">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842665b733.mp4?token=ZeBeguSu1ZT6nrqmHVFccEHvOy4jgmSPWtge0xO9KexTqDMXlH5B5SRBR9RcNm9eRZTanyog2bzD1MWsvwGjZc1MsXsdjiWVjwshv-tUnF3DqO_y8Kapu8zBeq8YabISNJ6WHmE7a9qQjm743ax0yZRNDrYF9JglazRBsyTsSxg6rCPEscaMuFXI7DyDHbNFJE9wZi0mB0siaw8zX1f6vt9AAolzYud9lnbhKVZzWqMCPbLRyVompNPkIiHkBjkVez3ey7uoDBhfyDI78unBcn2HLMawfYNoFxvKzRVfoaQzjfkENHfzaWHZFNtFjnJ6rRDdzsm-aJ5m7ubZvJCLMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842665b733.mp4?token=ZeBeguSu1ZT6nrqmHVFccEHvOy4jgmSPWtge0xO9KexTqDMXlH5B5SRBR9RcNm9eRZTanyog2bzD1MWsvwGjZc1MsXsdjiWVjwshv-tUnF3DqO_y8Kapu8zBeq8YabISNJ6WHmE7a9qQjm743ax0yZRNDrYF9JglazRBsyTsSxg6rCPEscaMuFXI7DyDHbNFJE9wZi0mB0siaw8zX1f6vt9AAolzYud9lnbhKVZzWqMCPbLRyVompNPkIiHkBjkVez3ey7uoDBhfyDI78unBcn2HLMawfYNoFxvKzRVfoaQzjfkENHfzaWHZFNtFjnJ6rRDdzsm-aJ5m7ubZvJCLMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی وایرال شده از کیفیت تجهیزات خودروهای داخلی: شیشه شور کوئیک داخل اتاق!!
🔹
آب‌پاش شیشه پشت کوییک به‌جای اینکه بیرون ماشین نصب شده باشه داخل اتاقه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/695570" target="_blank">📅 19:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695569">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d58981eab.mp4?token=g5jX3wnTD7uzagbPLTES1wwjR4MBP4xGk_E7gsn-KSOFZF6GKfQR_cD8I4X4jKyE0GZ2gpHTv98ScSFtXWQKxI6f7elO2BcK9zZecKYbGqbYdUTsIV8ijvgiGtVoI5_3O5c46AOGfAuQM9-N7aMYjIZ5fhp4SXAfpHLrLLhGnMs_c773qOkt0EbN5UPe7Ievd2GrqEv5AdX4bXRcbTItYx1kK9mA2q44jYbCOsujn33tVsI7yg-3bEi-aLLpfLnytFt6L3JOKPZEmgP_nGw5ZDLe0ySnp18cxc8klB8zm8pjfMS86r8R9ki9QDnLfpr1E6lrLCOjJE4yr-cimw9oXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d58981eab.mp4?token=g5jX3wnTD7uzagbPLTES1wwjR4MBP4xGk_E7gsn-KSOFZF6GKfQR_cD8I4X4jKyE0GZ2gpHTv98ScSFtXWQKxI6f7elO2BcK9zZecKYbGqbYdUTsIV8ijvgiGtVoI5_3O5c46AOGfAuQM9-N7aMYjIZ5fhp4SXAfpHLrLLhGnMs_c773qOkt0EbN5UPe7Ievd2GrqEv5AdX4bXRcbTItYx1kK9mA2q44jYbCOsujn33tVsI7yg-3bEi-aLLpfLnytFt6L3JOKPZEmgP_nGw5ZDLe0ySnp18cxc8klB8zm8pjfMS86r8R9ki9QDnLfpr1E6lrLCOjJE4yr-cimw9oXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیاوش جمشیدی، از اوباش مسلح شهرکرد اعدام شد
🔹
کلاهبرداری، تهدید، سرقت، حمل و نگهداری سلاح جنگی، مشارکت در آدم‌ربایی، قدرت‌نمایی، واردکردن صدمه بدنی عمدی، تهدید با سلاح گرم و شلیک با سلاح کمری مقابل حوزه علمیه شهرکرد، از جمله سوابق متعدد سیاوش جمشیدی بود.…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/695569" target="_blank">📅 19:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695568">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وزیر نیرو: افزایش قیمت برق در دستور کار نیست/ برای پرمصرف‌ها جریمه خواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/695568" target="_blank">📅 19:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695567">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromصبانت | Sabanet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOR7RyvZmk9xxDuV0dwBLKi_bSjPq1az1y_jyEwQv7JM5FUUkRP_Eytz5gY9vIOuLiXqa22CfD9HHQ6gG9_JJVrsCOIEHeMBVi6EAJzadWlTVNRTEztsdE5mqtwtUTqovD7HsSg9WfLo1QUd2fjO4wt43NybFXoDO4h2-N-QDgD0R6eBoKyK0Aco83q69907wiBanLKyqRSOXDfhSId_6D1DQedbbitjMIMkdKMZwS_Ao56gCsGAPG9i0aE4pHYJERCKYTLX8KRVKDSbfEUG8ETk7jLh_6aL6P8TFQDAFwdNKRfjD4K8w1jBGZf8GhB0GO5tVOU6f0G5pbzSbQU1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت قطع شده؟
😶
🔴
نه برای همه!
وقتی بقیه دنبال وصل شدنن،
تو
با صبانت
، بدون توقف به کارهات برس.
🌐
اینترنت پایدار، پرسرعت و بدون مکث
⚡
سرویس‌های ویژه برای اتصالی مطمئن‌تر
🎮
پینگ پایین برای بازی آنلاین
📥
دانلود سریع فایل‌های حجیم
📡
اتصال همزمان چند دستگاه بدون افت سرعت
🔴
صبانت یعنی؛ وقتی بقیه متوقف میشن، تو ادامه میدی.
☎️
1524
🔗
sabanet.ir/UR
#اینترنت
#فیبرنوری
#صبانت
#اینترنت_پرسرعت</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/695567" target="_blank">📅 19:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695566">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: احتمال افزایش حقوق‌ها در بودجه آذرماه بررسی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/695566" target="_blank">📅 18:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695561">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
معاون وزارت رفاه: حساب بیش از ۴۰۰ هزار نفر از مادران، تا چند ساعت آینده شارژ می شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/695561" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695560">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leX2J2wgqya0opg_Tu9YS9b5stuaWWY-x_pXCFuNiWTcXcI31JAoS_-6WNELwcUrjMytNHbiwPPQLxRMqd_FFX45vJ8Y56xduBW_Gmt6mJdJO4TKZo5IxPKH4Y3P-Lj5y-J6iefZ28Iwu3eA5dbl1mpngWkNm0wSVTME-Z1H7PYo3perMpAOtuoVl49Nri4K3EQNXwAgm77D9dQ0VefOHjLJEZb-aD0ZWiLv6R8IgG6lFapguVdn74b7L4YcG8YlRmjYpOmb4BYH0bwMvSr-sKW--zeuZjJMIBeVw3HsjQYSPYocLbvdXdd6BziiT9w7D39t3UqrifWOnh7d3f_eYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آسیب شدید به یک فروند هواپیمای شناسایی RE-3A عربستان در جریان حملات ایران به پایگاه هوایی شاهزاده سلطان در مارس ۲۰۲۶ حکایت دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695560" target="_blank">📅 18:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695559">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873583313c.mp4?token=QEbKn08UG66kYECnzEmR9HmRyCX9Ino5OSn97lJh7Eou-nKeVA7XV8pr21xMO7SNhCW9S4oEs_gWOQgOwYHAroM-R4G2gAQSZ7OhUsKH3zZ4HHFs_6m647TZJiE7R2IlaWFfZhkaiV51W1ASLC5HI8HnAAseViqyv3KtdXflO2ebwvUY1cxcyTiBxhA35yHZtf8Ih9O-KZ49Uj4-YrUw6TikAf1o34V8Xhuw2gx1RsEyJxenY8dJdNz6AruTkBR4NowR7Rlc8TlxNEII4r31AC6dg1i2ASLAx02MonSPjSzZAg0dNjyRfEOI36px81qdBUhq5sEP0IfQ89484bjb3FnfeR6tu3wNMhLY2y99ws1h79ZPP2EiY_fRexIDqBBR-KguxeDVpJFT8c4K2cF3yNBGIJINs9_VYpnbdIQ9xM_FW-VGoHYuRcMR5lJ5cwiAa-E7fsqlpaiwh4jIpJTSkxoGcI_lUbIv_F8l4qjGm7O7M0GNX2tD6GqWABe1gOyp-SqvbHnxc57cmws27PxBJzUqZSxJ2KFZ7HfeXZyxsMyY1UyM0I0rAgZGKDspghLq6do6fKFvpUmEvNRP-qSunOZCE0q2YvGbtihG7_yoIWtdT6YdD-OHftTaNbYr0sFyjSLXyNoFTerzTvkSsW8LQM_UykpNeX0qTq8oGhxLHJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873583313c.mp4?token=QEbKn08UG66kYECnzEmR9HmRyCX9Ino5OSn97lJh7Eou-nKeVA7XV8pr21xMO7SNhCW9S4oEs_gWOQgOwYHAroM-R4G2gAQSZ7OhUsKH3zZ4HHFs_6m647TZJiE7R2IlaWFfZhkaiV51W1ASLC5HI8HnAAseViqyv3KtdXflO2ebwvUY1cxcyTiBxhA35yHZtf8Ih9O-KZ49Uj4-YrUw6TikAf1o34V8Xhuw2gx1RsEyJxenY8dJdNz6AruTkBR4NowR7Rlc8TlxNEII4r31AC6dg1i2ASLAx02MonSPjSzZAg0dNjyRfEOI36px81qdBUhq5sEP0IfQ89484bjb3FnfeR6tu3wNMhLY2y99ws1h79ZPP2EiY_fRexIDqBBR-KguxeDVpJFT8c4K2cF3yNBGIJINs9_VYpnbdIQ9xM_FW-VGoHYuRcMR5lJ5cwiAa-E7fsqlpaiwh4jIpJTSkxoGcI_lUbIv_F8l4qjGm7O7M0GNX2tD6GqWABe1gOyp-SqvbHnxc57cmws27PxBJzUqZSxJ2KFZ7HfeXZyxsMyY1UyM0I0rAgZGKDspghLq6do6fKFvpUmEvNRP-qSunOZCE0q2YvGbtihG7_yoIWtdT6YdD-OHftTaNbYr0sFyjSLXyNoFTerzTvkSsW8LQM_UykpNeX0qTq8oGhxLHJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک‌
لحظه غفلت یک عمر بی آبرویی
🔹
در چین در صورت عبور از چراغ قرمز عکس فرد خاطی در تقاطع‌ها گذاشته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695559" target="_blank">📅 18:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695558">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fbfc5fb89.mp4?token=Oq-kCvuzwETrNlDyf1mCrFdvjb__dJEZtwrYK-QkiFyX4ZxUzWKGNaRkKLxzSB8iSJ_3GYX_QNGVL-pdsXUxapj48F0pS9O_Z9CPbwd7DphWRnpZ8HxgiqB1_8DMXvIurCv35siqWBf350pXmhI8jKmdxDpub1PlwzFid_9OjZypx-Sc9ZyE-uasd19L7x2aG2giN9cyLozw7HSPwEVZgIXONbeGz-mAE8yOr76R4RCdaUThX_PHTZqjzWqD4kEZH86w_UcSD_ZlotrDgwc8tiGRJVLWOpZZJZy2YT2o1YZtQH0kRYFsmsBz0ZlLo5DeYVE2weG3NRMh9b0wTt9g-jY0rR3g8jhD_VhKdiSvL4cqpiVIBsaT7opNU-nZ0dejLnXokthEQhkBmLZD3i8PqcyJrJGPiGRIYEJbwT9AjKscwl-9MYKAh1iv7obuGT04nzNVKtbudUGqFlGCkCuTfC4eJxsz_MDialiyUDaIO0eyV0JLoVDuXwxqJE0fbROkpYR9bK7yvtf6aWt69bnTuEoqCWlDRqE3ZPLzKRsDe_MX1VHQfHXHp0RMD9-qm5tY9ZlpimTbgjR5IWgKUV3iYajZWGCly5wzp6UyX2ABzb0_TJo7IgzonR6i-6RAqN5oLXreQapXXsnDAb5dvJChorxaJ-fakfyXpLub_IRMwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fbfc5fb89.mp4?token=Oq-kCvuzwETrNlDyf1mCrFdvjb__dJEZtwrYK-QkiFyX4ZxUzWKGNaRkKLxzSB8iSJ_3GYX_QNGVL-pdsXUxapj48F0pS9O_Z9CPbwd7DphWRnpZ8HxgiqB1_8DMXvIurCv35siqWBf350pXmhI8jKmdxDpub1PlwzFid_9OjZypx-Sc9ZyE-uasd19L7x2aG2giN9cyLozw7HSPwEVZgIXONbeGz-mAE8yOr76R4RCdaUThX_PHTZqjzWqD4kEZH86w_UcSD_ZlotrDgwc8tiGRJVLWOpZZJZy2YT2o1YZtQH0kRYFsmsBz0ZlLo5DeYVE2weG3NRMh9b0wTt9g-jY0rR3g8jhD_VhKdiSvL4cqpiVIBsaT7opNU-nZ0dejLnXokthEQhkBmLZD3i8PqcyJrJGPiGRIYEJbwT9AjKscwl-9MYKAh1iv7obuGT04nzNVKtbudUGqFlGCkCuTfC4eJxsz_MDialiyUDaIO0eyV0JLoVDuXwxqJE0fbROkpYR9bK7yvtf6aWt69bnTuEoqCWlDRqE3ZPLzKRsDe_MX1VHQfHXHp0RMD9-qm5tY9ZlpimTbgjR5IWgKUV3iYajZWGCly5wzp6UyX2ABzb0_TJo7IgzonR6i-6RAqN5oLXreQapXXsnDAb5dvJChorxaJ-fakfyXpLub_IRMwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باید تراستی‌ها و داستان تراستی‌ها را جمع کنیم
پیمان فلسفی، نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
باید با سوء تدبیرها و مدیرانی که عامل این مشکلات بودند باید برخورد صورت بگیرد و نباید مماشات کنیم.
🔹
وظیفه قوه قضاییه این است که قاطعانه برخورد کند؛ البته قوه قضاییه هم در بازگرداندن ارزی که از کشور خارج شده است، ورود کرده است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695558" target="_blank">📅 18:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695557">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وزیر نفت: وصولی‌های نفت فروخته‌ شده همچنان محقق می‌شود و این روند ادامه خواهد داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/695557" target="_blank">📅 18:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695555">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxwVV6vNW0OoVNZXt7YY02cvHRF5XV8qkVw9bbxMPoWiiyVyjX7YH7xcJs6ct_YQTlsuHGanoSD9r0tgr_BMO6N39OtZedEQGpexU8rUhZTaEXSYkWUBhjCzhkl4XP53z8GY9jbKQyGcxLAvyaZJtPyWSMSdQwDciPRsp5giAWd5xytuqLBAk3gIuU37rAzQE8uGbGOxvbfhv3MD73P1WVguYdHIdkE7u2zV2dlDXo3cUMlJJIeHFw4HzCSt3rtj4ks8HmbtdJ1znvWx_rzSKB4L1Anqh2aoAba1P8R42_HlKllKXCWBw1WcxSykoJWkVe8XarsEkOLrDyga5a--eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از رعد و
برق دیشب ساری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/695555" target="_blank">📅 18:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695554">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca56ffa255.mp4?token=J0WUwk3XBC27NCl4a99WCSZuCyubJiSAyjX_YuXFUSVk3HvaP6iPniOOOktRTYuy3h3HfYtfbWo4rV7lyA-Mv1Xzyv11fg2HBtC98ldpYm_UqBlEBJ_GZVakO66MIyItp53h5m7J-hPNxMGop73o3eMJ4CwErXbjDmm1OEN_zMDLGHh5dNIJfjDCPsGlPnmbyboF5u8rgjdLLYH_aNQa40Qycq8H52qGWjy6RBLHgmE5NvtRnFPNGO9YIHHAuLtn7OJ5JYlE6JAE8oHWVadU6kHrfxAvVXbzDBZTApd7AqzGy2G0zkXhZjiDk6BnGYM9uv7W2ijYrMsjch5cFf_5w4GBAFuANNKaY5-o4ZvMGC6LWWb8UhcrJ7IWQ4GKshWQTi8yYsD-Vt-dnBgaVicmGOKKNOKmQqEfP9as6-u9q9KBbKvUKN8GH9PouSO1p89CfPkcSjwwi8tCyUzr-m2btATvZvXVBVhHAh7eeGlxXcFJnDZk0nj5goxrLEg1AvY3gFUSKhvnyoM9I3n2bNv3RT-jjNcACoOmdJX76kfJiUfloPRl7VxGbdIMwAk5eUKUk-5yYxsrakiebaUqbA2jjrns2POzSa0UsiulelbttW-fmSpvBaz1f8xaZ9nCfNvRKafGBnxpb8nKj9fE7ni9l5TVMscNlPz3-avzli6ukg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca56ffa255.mp4?token=J0WUwk3XBC27NCl4a99WCSZuCyubJiSAyjX_YuXFUSVk3HvaP6iPniOOOktRTYuy3h3HfYtfbWo4rV7lyA-Mv1Xzyv11fg2HBtC98ldpYm_UqBlEBJ_GZVakO66MIyItp53h5m7J-hPNxMGop73o3eMJ4CwErXbjDmm1OEN_zMDLGHh5dNIJfjDCPsGlPnmbyboF5u8rgjdLLYH_aNQa40Qycq8H52qGWjy6RBLHgmE5NvtRnFPNGO9YIHHAuLtn7OJ5JYlE6JAE8oHWVadU6kHrfxAvVXbzDBZTApd7AqzGy2G0zkXhZjiDk6BnGYM9uv7W2ijYrMsjch5cFf_5w4GBAFuANNKaY5-o4ZvMGC6LWWb8UhcrJ7IWQ4GKshWQTi8yYsD-Vt-dnBgaVicmGOKKNOKmQqEfP9as6-u9q9KBbKvUKN8GH9PouSO1p89CfPkcSjwwi8tCyUzr-m2btATvZvXVBVhHAh7eeGlxXcFJnDZk0nj5goxrLEg1AvY3gFUSKhvnyoM9I3n2bNv3RT-jjNcACoOmdJX76kfJiUfloPRl7VxGbdIMwAk5eUKUk-5yYxsrakiebaUqbA2jjrns2POzSa0UsiulelbttW-fmSpvBaz1f8xaZ9nCfNvRKafGBnxpb8nKj9fE7ni9l5TVMscNlPz3-avzli6ukg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
بازسازی جنگ بدر و نبرد تن به تن حضرت علی (ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/695554" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: نتایج نهایی آزمون سراسری و تربیت‌معلم، در نیمه دوم آبان اعلام می‌شود
🔹
نتایج چندبرابر ظرفیت رشته‌های نیازمند مصاحبه را تا پایان مهر اعلام می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/695552" target="_blank">📅 18:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سازمان مدیریت بحران: بارش‌های اخیر ۱۸ خودرو را دچار خسارت کرد
امید محترمی، معاون سازمان مدیریت بحران در
#گفتگو
با خبرفوری:
🔹
در پی بارش‌های اخیر
۱۸ خودرو
در استان‌های کرج، البرز و خوزستان دچار خسارت شدند که همه خسارت‌ها سطحی بوده و حادثه سنگین یا خسارت جدی به خودروها گزارش نشده است.
🔹
۱۰ واحد تجاری و مسکونی نیز دچار آب‌گرفتگی جزئی شدند و حدود ۵۴ مورد سقوط اشیا، تابلو و درخت در نقاط مختلف ثبت شده است.
🔹
یک جریان آب با ارتفاع حدود ۲۰ سانتی‌متر می‌تواند به‌ راحتی خودروی سواری را واژگون کند، بنابراین هنگام جریان داشتن آب روی جاده یا خیابان نباید با خودرو وارد مسیر شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/695551" target="_blank">📅 18:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac482bfcef.mp4?token=u_BTd4mj5EQwcxpY6vGo6AIIGGfs_90nIpek36KVqXHZ5F4XHJECgulfGzKUFQI_i_0tJzO2qG1cVc5XstuO8KDxfsa6iq1JjtF1zlTO2VorIKMCyiQn9FMxGtoanjCMvtNmrhFshhQKmecz_YiNp9ItMaWMgMZ5tl3s6mD4_88wa_jfz5aveC8EDjk6-CBCzwQPdL26mCy2RNnKyClXOGAxLPOWxZkhr20QgfzdEr4SpPZto8Syy5ngHpEP_sGUNgQYBCEPOrfP7uLu7M8Jm2RhyDHtV80ewX3sOAFcDi58Y4VN3v7zy-vt0ZTvZi0xpAPF9URRpBC8FL3jNSy00w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac482bfcef.mp4?token=u_BTd4mj5EQwcxpY6vGo6AIIGGfs_90nIpek36KVqXHZ5F4XHJECgulfGzKUFQI_i_0tJzO2qG1cVc5XstuO8KDxfsa6iq1JjtF1zlTO2VorIKMCyiQn9FMxGtoanjCMvtNmrhFshhQKmecz_YiNp9ItMaWMgMZ5tl3s6mD4_88wa_jfz5aveC8EDjk6-CBCzwQPdL26mCy2RNnKyClXOGAxLPOWxZkhr20QgfzdEr4SpPZto8Syy5ngHpEP_sGUNgQYBCEPOrfP7uLu7M8Jm2RhyDHtV80ewX3sOAFcDi58Y4VN3v7zy-vt0ZTvZi0xpAPF9URRpBC8FL3jNSy00w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/695550" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFaraDars_Course</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JORSQP5GNv82_lp29Gi1FjZ1DG-IHILq3smgHoYckZrhMuYkt4KdwGilcwyfrdtcAF35HoP5Fau-_jGgAgE_dgQHr-ZdM-0Wv2oeVmvfHW7TJJCEJH-wXlWS29EY5McFfM_RpSGgq_1wbFZdUrvYv1nmWFADJU-j8Md1ySJxMf_rpQTZ-4wXz6DHldIQx3Qa1FMtFwr6LAUdX775Y_qZ0V7_Vi1CRbKk2byn_80yF-OqnUb6KWB-zodNT3bVw93OjMWSrFADRmki2bs8AgNILMiBXhEgvS56VXBCuoR3fwCscgfC9Cj3OAwBXJvyLSyePbI-tEaQVNBEdcGd6NErNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
خبر فوری — انتخاب رشته کاملاً رایگان و هوشمند با «مسیر»
🔥
نرم‌افزار «مسیر» توسط فرادرس و برای داوطلبان ورود به دانشگاه ارائه شده که ابزاری رایگان برای انتخاب رشته است.
✅
بررسی بیش از ۳۴ هزار رشته‌محل
✅
معرفی بیش از ۷۰۰ رشته تحصیلی
✅
جمع آوری اطلاعات بیش از ۸۰۰ دانشگاه
✅
مقایسه گزینه‌ها و ساخت فهرست انتخاب‌ها
🔗
شروع رایگان انتخاب رشته با مسیر [+]
🔥
رشته‌های دانشگاهی را بر اساس گروه‌های اصلی کنکور بررسی کنید و با مسیر و محتوای آموزشی هر رشته آشنا شوید.
@MasirGuide
— کانال تلگرام مسیر
FaraDars — کانال تلگرام فرادرس</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/695549" target="_blank">📅 18:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2f834fa.mp4?token=ekKW8G7h7EPfZrRHCacWx30cF5WOrYDb9knABGLZMSTnP3_bzwqcBR3tG6cjr91g8mI8GVJqE-qXv2mwH1s2-rGwYopuVJcv1NAcY6J8IxlZxqI6vF_oHsDYsPfyBFVpOKLF71AUnZKjxqGJ1yq4pro42wzU4rhaBy83xsjrU2Njz4b7Vra9F5xIY0EWUl4yFMKxf62bWE_yD8LcR7Ef_F2-NP5ICR08-2mqGfwtaH4n-_CkDeniInIvKIJoeeIcXIHJFybu1P5UKVFllz1-IP9BrtF2DOh5V2qAE5lSlIe4h6tsT1Rm6eBLSSeXCnlv4kgmrFygPwtHrM5vx4rbYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2f834fa.mp4?token=ekKW8G7h7EPfZrRHCacWx30cF5WOrYDb9knABGLZMSTnP3_bzwqcBR3tG6cjr91g8mI8GVJqE-qXv2mwH1s2-rGwYopuVJcv1NAcY6J8IxlZxqI6vF_oHsDYsPfyBFVpOKLF71AUnZKjxqGJ1yq4pro42wzU4rhaBy83xsjrU2Njz4b7Vra9F5xIY0EWUl4yFMKxf62bWE_yD8LcR7Ef_F2-NP5ICR08-2mqGfwtaH4n-_CkDeniInIvKIJoeeIcXIHJFybu1P5UKVFllz1-IP9BrtF2DOh5V2qAE5lSlIe4h6tsT1Rm6eBLSSeXCnlv4kgmrFygPwtHrM5vx4rbYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فشارسنج خون درجه 1 برند Arm Style
قیمت ویژه و فوق اقتصادی
📌
استفاده راحت فقط با یک دکمه
📌
کیفیت عالی
📌
دقیق و بدون خطا
قیمت نقدی:1,698,000 تومن
🌟
امکان پرداخت قسطی هم داری
✅
4 قسط 480 تومنی
🔥
تخفیف تا 15 شهریور
🔥
🏠
پرداخت درب منزل + ضمانت بازگشت وجه در صورت خرابی
خرید سریعو کسب اطلاعات بیشتر :
👇
https://memarket24.ir/product/fast/37863/180124</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/695548" target="_blank">📅 18:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695547">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
صدای انفجار از داخل پایگاه ارتش اسرائیل در نقب به گوش رسید و دود غلیظی از آن به هوا برخواست که از مسافت‌های دور قابل مشاهده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/695547" target="_blank">📅 17:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695546">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7e577ef3.mp4?token=jebEJL1occFjgmfabSQ3PK6hhvMyT3SfSW9doVYSwlzZZCXqOyP1IEEUAVJtSUdmArL73Cjzy3ktpoE7Pl_O7v_08MOpCYkTpU-IcSp-U9MPbxVfGWQ63f6QHC5xrBcTiLBa3hnE_F1o7UCV_zQzOrSrPK6PNNaiZzJtFBRWZbr3JMoUpc3uqIahGfpr388AHQIn1czug0i20vFwBdN_lwWmhR0SZTzmXMo7UijPUR65wI2P-C0IsvzrinR9p3lAVnVJ3xHd2fhWCCYNrZ26abUsEy09nb3KKAjGq5o_tuCdHLmF-5CUJtz_Dq_kvSx_BpKCHgHRCNdqUohe5plNzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7e577ef3.mp4?token=jebEJL1occFjgmfabSQ3PK6hhvMyT3SfSW9doVYSwlzZZCXqOyP1IEEUAVJtSUdmArL73Cjzy3ktpoE7Pl_O7v_08MOpCYkTpU-IcSp-U9MPbxVfGWQ63f6QHC5xrBcTiLBa3hnE_F1o7UCV_zQzOrSrPK6PNNaiZzJtFBRWZbr3JMoUpc3uqIahGfpr388AHQIn1czug0i20vFwBdN_lwWmhR0SZTzmXMo7UijPUR65wI2P-C0IsvzrinR9p3lAVnVJ3xHd2fhWCCYNrZ26abUsEy09nb3KKAjGq5o_tuCdHLmF-5CUJtz_Dq_kvSx_BpKCHgHRCNdqUohe5plNzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: سوال درباره قیمت دلار را از آقای همتی بپرسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/695546" target="_blank">📅 17:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695545">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
بانک‌های مرکزی هنوز طلا می‌خرند
🔹
بانک‌های مرکزی در جدیدترین خریدهای خود ۲۳ تن طلای خالص خریدند. چین با ۲۰ تن و لهستان با ۸ تن در صدر این خریدها بودند. از ابتدای سال نیز لهستان با ۹۰ تن و چین با ۶۰ تن بزرگ‌ترین خریداران طلا بوده‌اند.
🔹
این خریدها صرفاً برای سود کوتاه‌مدت نیست؛ بانک‌های مرکزی با افزایش ذخایر طلا به دنبال کاهش وابستگی به دلار، تنوع‌بخشی به ذخایر و مقابله با ریسک‌های ژئوپلیتیک هستند. کارشناسان می‌گویند این خریدها می‌تواند سوخت جهش قیمت باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/695545" target="_blank">📅 17:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695541">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDKqMdaJ1QngIhQkyewTZ-kVqdFa1SnRc8J4SgsNH3JASqYjbgGIL2AwVq3Nhb6gOEWMTs70Mc7-yeTK1EaHmKvZUPOtC_RyKv0RqTLD3TFKOxngA4gkSPo3wv3YLLmeufmBNtpZBllR9ZEPG4oaptVTIuw4-p8hfu_F4PwLsxOGAaLq2qsVZTgEMYM2kJANQL1VmFqaDyuMHf2_5nRhGvW44RXrGYtUq6WcqdHjcnLpYKbANQOLBpm-QZ819sHr3EZxox2UwX2UkgKSJ81Km95F4T8AyRmipLGIgEYgdfRxYtzXxe0fnkW9xyShhP4mVMCPUJ3t1aMC-LTmgmm0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دمپایی جدیدی که در مدت کوتاهی مورد توجه بازار قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/695541" target="_blank">📅 17:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695540">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وزیر نیرو: افزایش قیمت برق در دستور کار نیست/ برای پرمصرف‌ها جریمه خواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/695540" target="_blank">📅 17:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه درباره افزایش احتمالی حقوق کارمندان: افزایش حقوق‌ها فقط در بودجه اعمال می‌شود؛ بودجه آذر ماه به مجلس تقدیم می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/695539" target="_blank">📅 17:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c847298983.mp4?token=O5JL49CuipboPLn5YiC4j9qgFTDn7IA3OOwBR-uB1gfU-jpq3JBZu0sj9_ZA_0Lnv0fTFonPDXj0GpmORFx-5iVauiL9f-0k0IKSnArxU-NOBVWWLw-PYWG1-LwvZR6gb_0CreT8e-dOKl62MyRTl65td0Txyx6r4htxSa7TXbi9sVt5aNSnIeGwd-yPS-YXloXiXbpt0iCVMdXgSBtCAgN5s0SwMsdmvi2oCizkiqM4DPH-To6A8Lu7hVE5LJAQbetIJsurShxPs1WrjhYTbpeBX8ySD5EI1XKgqd0zygzF5azHp3v2kET3yL0Dq1_wyFtQepD2pyj6bvVmr2RXtWFYwnHwYWrRsA4OvoDX2KgaTWzmgxLym9H_qbJzoiK783aJypnDY0S4eTy_nQcDCi59-mnzzgnhfadd5S5bEYAUXBfpY347Nnz0jthjBkoy02JFHEfFVus3uVa6yToDWqtRHYYyvX6E3G1BVNjhi1uqGoL3ViKDNnAW8ioGfdcL9oWhLS243OnkIu1MZJer-SGDsKWMBtxKtK7ttdzRJIsmfMslHnJegR8EMzSitbDIaAWQWyGdgyNMQ9gExC7MRdnc8-E8NDcmR-VhekdPASP_NikP1fAXnRO3pDAvbTQFNLdwnx4z1wTvJyP3IFm8vCyybidG6LPLej5ekr4Q9tM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c847298983.mp4?token=O5JL49CuipboPLn5YiC4j9qgFTDn7IA3OOwBR-uB1gfU-jpq3JBZu0sj9_ZA_0Lnv0fTFonPDXj0GpmORFx-5iVauiL9f-0k0IKSnArxU-NOBVWWLw-PYWG1-LwvZR6gb_0CreT8e-dOKl62MyRTl65td0Txyx6r4htxSa7TXbi9sVt5aNSnIeGwd-yPS-YXloXiXbpt0iCVMdXgSBtCAgN5s0SwMsdmvi2oCizkiqM4DPH-To6A8Lu7hVE5LJAQbetIJsurShxPs1WrjhYTbpeBX8ySD5EI1XKgqd0zygzF5azHp3v2kET3yL0Dq1_wyFtQepD2pyj6bvVmr2RXtWFYwnHwYWrRsA4OvoDX2KgaTWzmgxLym9H_qbJzoiK783aJypnDY0S4eTy_nQcDCi59-mnzzgnhfadd5S5bEYAUXBfpY347Nnz0jthjBkoy02JFHEfFVus3uVa6yToDWqtRHYYyvX6E3G1BVNjhi1uqGoL3ViKDNnAW8ioGfdcL9oWhLS243OnkIu1MZJer-SGDsKWMBtxKtK7ttdzRJIsmfMslHnJegR8EMzSitbDIaAWQWyGdgyNMQ9gExC7MRdnc8-E8NDcmR-VhekdPASP_NikP1fAXnRO3pDAvbTQFNLdwnx4z1wTvJyP3IFm8vCyybidG6LPLej5ekr4Q9tM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بانک مرکزی مدیریتی بر ذخایر ارزی ندارد؛ فقط به دنبال ورود منابع نفتی هستیم
پیمان فلسفی نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
نظام و بانک مرکزی باید بتواند مدیریت خود را بر ارز و ذخایر ارزی اعمال کند، اما الان اعمال نمی‌کند و فقط نشستیم و شاهد افزایش قیمت ارز هستیم.
🔹
می‌دانم رانت‌خوارها، فرصت‌طلبان و کسانی که تا گذشته منافعی داشتند، قطعا صدایشان در خواهدآمد؛ باید دست اینها را کوتاه کرد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/695538" target="_blank">📅 17:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695537">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83703e962b.mp4?token=icV3fjeGy2Fj__Q-A8QFGkaHlhwaRvAMURK9Uz73OGk-0o9nrdwoX34jcWUJ96Ah8-9swXFkE7_UHNfEQhS753r-zACGGHhZl2Oe_JFXp7ZKUwHsKTj-eZ42Xyu7-SmFBxNVMoUkzgYtGoxnTl6mOZTHap04rz21rt9wLyYHg5hzSKsO6TLbdJrn1hcaC3vhuulwsDsxaocjD2j3W8LYf40Rw5r33FGgFbw4jWEk-ucn5vySkl0H6K9faxIbvQ1b8RPrMdVeRB-O_McGpJA21bDHNKovJVAe1YTBZyzm0UDQo847V1KLvgfimBlAFWN47Sjed1TEndsoSmbHCxqo7pa6S-pJyOFXfX5tcJUAB6vGx-p09un8lKQYfI1dKEcnAITuK40UKA6Pf-6GVdy8z0nzeyqjDb2X-i9sMdLa71AabFobbd5aSr5klSiRJA5UbGQh46XoX4bC50FyGnOipCB2OGdIPZK4Ivr_4M40eOMEq596HBYWwAmbwSsd4Flnw7w2bv7iervwSr_t6AQ9vbx-4qkhTGsxX3iqEUx0-4GZpmAIuin5OQ3tN4kWIiHDNTRq_gAm_mF1kaUHT39f7MH-fy9EaCY-Ys7z5OTbrypVz7meHs-z1pED9n2KoqrQOfGNv6kLhYLyubvA9BvRewhP8y5i75xE3Q9JJQOgynU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83703e962b.mp4?token=icV3fjeGy2Fj__Q-A8QFGkaHlhwaRvAMURK9Uz73OGk-0o9nrdwoX34jcWUJ96Ah8-9swXFkE7_UHNfEQhS753r-zACGGHhZl2Oe_JFXp7ZKUwHsKTj-eZ42Xyu7-SmFBxNVMoUkzgYtGoxnTl6mOZTHap04rz21rt9wLyYHg5hzSKsO6TLbdJrn1hcaC3vhuulwsDsxaocjD2j3W8LYf40Rw5r33FGgFbw4jWEk-ucn5vySkl0H6K9faxIbvQ1b8RPrMdVeRB-O_McGpJA21bDHNKovJVAe1YTBZyzm0UDQo847V1KLvgfimBlAFWN47Sjed1TEndsoSmbHCxqo7pa6S-pJyOFXfX5tcJUAB6vGx-p09un8lKQYfI1dKEcnAITuK40UKA6Pf-6GVdy8z0nzeyqjDb2X-i9sMdLa71AabFobbd5aSr5klSiRJA5UbGQh46XoX4bC50FyGnOipCB2OGdIPZK4Ivr_4M40eOMEq596HBYWwAmbwSsd4Flnw7w2bv7iervwSr_t6AQ9vbx-4qkhTGsxX3iqEUx0-4GZpmAIuin5OQ3tN4kWIiHDNTRq_gAm_mF1kaUHT39f7MH-fy9EaCY-Ys7z5OTbrypVz7meHs-z1pED9n2KoqrQOfGNv6kLhYLyubvA9BvRewhP8y5i75xE3Q9JJQOgynU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید سرکه سیب رو از زبون خودش بشنوین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/695537" target="_blank">📅 17:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695536">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
وزیر تعاون، کار و رفاه اجتماعی: تلاش می‌کنیم افزایش کالابرگ اقشار هدف از ۱۵ مهر آغاز شود
🔹
میزان افزایش اعتبار کالابرگ احتمالا ۵۰ درصد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/695536" target="_blank">📅 17:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695535">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/661232901a.mp4?token=PcstZgX30eIb72hRnY7XyMKpsSMHNDe-OHuO-0xZ9C0jzF9x8VMA9UFG2JJuzoekx4ROqAomUpcv3IHIHyTo74rbXrugqrvDvh-ecH4oU5AttPg5RngK2q2v9jF4gDZicdQppP6rKKI9n5AyFG5HHFOh2Elx3x1XVIT6D3_0jsZNYW37Q78Z1auC2Tu86t-ctcPn8y_9KILFq9P5H4UEnLX1zmClX4i8RZxXycYKwwQH36uOZtRaZptptWgUWM4gUR8OmlwpR0Kzf2ZqhcTg_ExJsF0u97d4dZ8x5Dvan1mkYlqEo2vyzt0c3Che3vbYZMd_sLClTWr9WvZB9FWfyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/661232901a.mp4?token=PcstZgX30eIb72hRnY7XyMKpsSMHNDe-OHuO-0xZ9C0jzF9x8VMA9UFG2JJuzoekx4ROqAomUpcv3IHIHyTo74rbXrugqrvDvh-ecH4oU5AttPg5RngK2q2v9jF4gDZicdQppP6rKKI9n5AyFG5HHFOh2Elx3x1XVIT6D3_0jsZNYW37Q78Z1auC2Tu86t-ctcPn8y_9KILFq9P5H4UEnLX1zmClX4i8RZxXycYKwwQH36uOZtRaZptptWgUWM4gUR8OmlwpR0Kzf2ZqhcTg_ExJsF0u97d4dZ8x5Dvan1mkYlqEo2vyzt0c3Che3vbYZMd_sLClTWr9WvZB9FWfyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات‌ها در کره‌جنوبی جای نیروی انسانی را گرفتند؛ این‌بار یک ربات به‌عنوان کارمند در دانشگاه مشغول به کار شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/695535" target="_blank">📅 17:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695534">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
زاکانی: برای ساخت پارکینگ پناهگاه‌ها در حال اقدام هستیم/ لکه‌گذاری و ساخت را در برخی نقاط آغاز کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/695534" target="_blank">📅 17:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ورود تراستی‌ها به واردات کالاهای اساسی؛ ارز به کشور بازنگشت
پیمان فلسفی، نماینده مجلس و عضو کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
برخی از تراستی‌ها وارد فضای واردات کالاهای اساسی شده‌اند.
🔹
قاعدتاً باید در تامین ارز ورود کنند چون ارز در اختیار آنها است.
🔹
تراستی‌ها جواب اعتماد ما را درست ندادند وگرنه این همه ارزی که قرار بود به کشور باز می‌گشت.
🔹
دولت، حاکمیت خود را اعمال نکرد و این شرکت‌ها را ایجاد و اعتماد کرد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/695533" target="_blank">📅 17:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398958a62f.mp4?token=Se4LrTZaTfyt_2cgOIuGCCAQyNq4ceG8CtIl7Gs4S7GDu8EBxlio3PZ8Dt7IMA1YnkTfcnSKoI4iv5bbtr1F0T-enDbtKRHJV34VdXJgO21O-VZ4rz8Z-iBwEILm4yq8_yuE_2sgSTs80O_xnVxVb1_oaswAbnV59jRDSgXdWo2zkaGjwoWHxQGMs21QqjiZF436jwsamdyKTS0H1qSzlnWk8QDilJ1ixgTBqB-3wgnKLPEoPtTZe4hgcco-OZoop8LkHyMYRhe6Gz1T_BWaQPGmh8t4BXe0OUOv8NSN3Ul3LwpsitVipT_BH3eva4tLJ_D-R27NxG3ooGdtBPncQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398958a62f.mp4?token=Se4LrTZaTfyt_2cgOIuGCCAQyNq4ceG8CtIl7Gs4S7GDu8EBxlio3PZ8Dt7IMA1YnkTfcnSKoI4iv5bbtr1F0T-enDbtKRHJV34VdXJgO21O-VZ4rz8Z-iBwEILm4yq8_yuE_2sgSTs80O_xnVxVb1_oaswAbnV59jRDSgXdWo2zkaGjwoWHxQGMs21QqjiZF436jwsamdyKTS0H1qSzlnWk8QDilJ1ixgTBqB-3wgnKLPEoPtTZe4hgcco-OZoop8LkHyMYRhe6Gz1T_BWaQPGmh8t4BXe0OUOv8NSN3Ul3LwpsitVipT_BH3eva4tLJ_D-R27NxG3ooGdtBPncQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این موجودات عجیب نه گیاهن، نه اژدهای افسانه‌ای؛ بلکه از خانواده اسب‌های دریایی‌ان!
🐉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/695532" target="_blank">📅 17:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695531">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: تنگه هرمز؛ «استالینگراد» جنگ ایران و آمریکا است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/695531" target="_blank">📅 17:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695530">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tft6EfA2hSFG6M14NCvhc-HeIogrO1BWejXsv1u4Jhn-Quw5gyAQbCuCqFpzAyXZwhR9JyTUG9wlbUULemo5MhYapMhjUOVqDF8Lcdg10vArQiODf3TaNK0b1f77zOlrqzm3OZE-D9q8-kf8bZg5H08U6UYJUUQJrLw7vvMfWDG5t_k9GGC6bcZjDcfombAsUoyXSO34WCu5cu-wRSyq48YpS7mKtgmZl81SEnTFhKzxGq4K_j24sCfn_KZxz579GV5LTYFwjiii6no-V0lojHSSTj8GXJGfy3a5ITXFAiLzhpdXC8oV4DJbcF8fnCLYE-MW4ty6vx--9D3Kmqqf1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/695530" target="_blank">📅 17:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
حداد عادل: الحمدالله حال رهبر انقلاب خوب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/695529" target="_blank">📅 17:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
داروسازی تسلیم هوش مصنوعی شد
🔹
شرکت‌های بزرگ داروسازی دنیا برای کشف و طراحی دارو حالا دست به دامان هوش مصنوعی شده‌اند.
🔹
ارزش بالقوه قراردادهای شرکت‌های داروسازی از ۱۱.۸ میلیارد دلار در سال ۲۰۲۴ به ۴۳.۴ میلیارد دلار در ۲۰۲۵ رسید. در نیمه نخست ۲۰۲۶ هم این رقم تفاهم شرکت‌ها با ۷۰ قرارداد، به ۴۵.۹ میلیارد دلار جهش کرد.
🔹
به نظر می‌رسد آینده کشف دارو دیگر فقط در آزمایشگاه‌ها ساخته نمی‌شود، بخش مهمی از آن حالا در دنیای هوش مصنوعی رقم می‌خورد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/695528" target="_blank">📅 17:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7e8fef23.mp4?token=o9OPeLBr4J8naM0SJZCXAe0C8jpx3ppW5nMrAx_uXoxz9VF4lr5XWf-N18aMH4RdGYjjHBzLuI2rJh6K2z0kR1cuVeWnnmxgTrDnb0OF5pCYjJFojn6dY2MGqdRQYRk1X2kgtnYl76zCbkZ8WNTHplzr8EkI9jwG-PD-4rSQhRDNcqb3vbcuH2NF1rW19e4kBLjUYr8xUlwEMIEMpILuMlTvvgafkkA9kr7PfjLQgNd8iBKIlAr90PYDjCPVvMwkibwotWtvuMj-m4IbPnUASHc1BdD_E6aaRQIK57iCg2-UiJp7MUbLn0mSaoEwTnwzpwAWKHMzoeaqHOcV9mnHYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7e8fef23.mp4?token=o9OPeLBr4J8naM0SJZCXAe0C8jpx3ppW5nMrAx_uXoxz9VF4lr5XWf-N18aMH4RdGYjjHBzLuI2rJh6K2z0kR1cuVeWnnmxgTrDnb0OF5pCYjJFojn6dY2MGqdRQYRk1X2kgtnYl76zCbkZ8WNTHplzr8EkI9jwG-PD-4rSQhRDNcqb3vbcuH2NF1rW19e4kBLjUYr8xUlwEMIEMpILuMlTvvgafkkA9kr7PfjLQgNd8iBKIlAr90PYDjCPVvMwkibwotWtvuMj-m4IbPnUASHc1BdD_E6aaRQIK57iCg2-UiJp7MUbLn0mSaoEwTnwzpwAWKHMzoeaqHOcV9mnHYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ آمیزی روی BMW؛ جدیدترین مِتُد آموزشی مدارس غیرانتفاعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695527" target="_blank">📅 17:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نایب رییس مجلس: عده‌ای دنبال خرابکاری و به زانو درآوردن مردم در موقعیت تورمی هستند
علیرضا حاجی بابایی، نایب رییس مجلس:
🔹
آمریکا بعد از ناامید شدن از جنگ نظامی با ما به جنگ اقتصادی همراه با فضای مجازی و از طریق رسانه روی آوردند و به همین دلیل ما نیز در تنگه هرمز و دیگر جاها باید بجنگیم و روبه رو شویم.
🔹
عده‌ای با ایده خرابکاری و به زانو درآوردن مردم در داخل کشور به دنبال موقعیت تورمی هستند و قوه قضاییه باید برخورد کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695526" target="_blank">📅 16:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
معاون عراقچی: آمریکا پاسخ طرح ۷ روزه ایران را ارسال کرد و ما در حال بررسی هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/695525" target="_blank">📅 16:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695522">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0801b72dc.mp4?token=fhVxAormmdqZ0YBEcBn0PCVSwtUOy508Wu1V69F4D4-_v26pV4lV6Y9lHZIRzp_Ng6MLW6xTcij7T5OBg8kmoOYUUSqV749bf4_bCaQNWUWeq4_Wzl1_kmEn5i5EtFdNjhtTb4JGbqVkO0Y9M2w4WX1ymHFf6dnre6z7bmdxfqo6o-5SHqwKhIfC-zq2sTi_YbKznzWOX_8ajImNsIOq9G84cYXoJ_gN1yjdxlcs6q0nn3O8z7tCrIq-6o51st3qUrb-8CaXyVMMNrMT2_DPR6bjlRqHg4I-sR7fE7bsi6Jj4Xli0JYYU_HL70DqT0kVla7SOWTCb0YFMQUTPezd0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0801b72dc.mp4?token=fhVxAormmdqZ0YBEcBn0PCVSwtUOy508Wu1V69F4D4-_v26pV4lV6Y9lHZIRzp_Ng6MLW6xTcij7T5OBg8kmoOYUUSqV749bf4_bCaQNWUWeq4_Wzl1_kmEn5i5EtFdNjhtTb4JGbqVkO0Y9M2w4WX1ymHFf6dnre6z7bmdxfqo6o-5SHqwKhIfC-zq2sTi_YbKznzWOX_8ajImNsIOq9G84cYXoJ_gN1yjdxlcs6q0nn3O8z7tCrIq-6o51st3qUrb-8CaXyVMMNrMT2_DPR6bjlRqHg4I-sR7fE7bsi6Jj4Xli0JYYU_HL70DqT0kVla7SOWTCb0YFMQUTPezd0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در گوشه رینگ گیر افتاده؛ جنگ هزینه سنگینی برای آمریکا دارد، راهی جز فشار و مذاکره ندارد
آلن گرش، روزنامه‌نگار فرانسوی و تحلیلگر مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
ترامپ در برابر ایران میان دو گزینه گرفتار شده؛ ادامه فشار یا رفتن به سمت توافق. جنگ هزینه‌های اقتصادی سنگینی برای آمریکا داشته و فشارهای اسرائیل و برخی کشورهای عربی خلیج فارس نیز تصمیم‌گیری را برای او دشوارتر کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/695522" target="_blank">📅 16:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695521">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c207a1682b.mp4?token=blZS9mlc9FrmKXYaxKbYAEnLiJUspQxPuWeETuXEr2OTRhXg-mYkvaCCmNSk79JZGS7HF4r4Z-1MYp3hhypoyyPtgkwhF3tKtTF7hY0lITYP89_Y7-KB4DICqpKvmtl5eJkLXl1hOqnYwvDAsEPdfX7IANG0OAjlBKxN6L4zFtkeOMje_IUixqRUG_pBIJMCYKwonxmgQDPAodxNdvDI-mmRVQ2fgDo19iee6Lmym5Hlst0s3N_2KHzj6hmU1-My51ztjgvOvjApfAIGdyHWaZUKcx_vgki7tg8OMeN-RMSol-GiRMcfCLorVltE92vIzPojkFSbENtcpVlh_rajgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c207a1682b.mp4?token=blZS9mlc9FrmKXYaxKbYAEnLiJUspQxPuWeETuXEr2OTRhXg-mYkvaCCmNSk79JZGS7HF4r4Z-1MYp3hhypoyyPtgkwhF3tKtTF7hY0lITYP89_Y7-KB4DICqpKvmtl5eJkLXl1hOqnYwvDAsEPdfX7IANG0OAjlBKxN6L4zFtkeOMje_IUixqRUG_pBIJMCYKwonxmgQDPAodxNdvDI-mmRVQ2fgDo19iee6Lmym5Hlst0s3N_2KHzj6hmU1-My51ztjgvOvjApfAIGdyHWaZUKcx_vgki7tg8OMeN-RMSol-GiRMcfCLorVltE92vIzPojkFSbENtcpVlh_rajgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی کاربران فضای مجازی با ساخت یک کلیپ هوش مصنوعی از مناظره ثباتی و شهریاری نماینده مجلس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/695521" target="_blank">📅 16:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695520">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
بروجردی، عضو کمیسیون امنیت ملی مجلس: آمریکا از طریق قطر پیشنهاداتی برای ایران فرستاده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/695520" target="_blank">📅 16:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695519">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اولین هواپیمای ایرانی در فرودگاه نجف به زمین نشست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/695519" target="_blank">📅 16:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695517">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08010a728.mp4?token=sb3Fh3meAAmTo598egjuwC97VXHkf_lPUQUegLu0NTPc6LbLJZaH5te3qIsqgAApshbSSOCfbHQ2ufsLlrDtW5GiqY5q6VLIW4a1VZwHuhNoBWHD6KjiV-mTkXpFxilrTl7UIUofptiRzvZW3BDHeTA9qPj_HR1_IiRh24Tx3yiTW-3bwguvpU5RkUAiEm6620FtWvj4LrMZhbef80NvejpWf9CPW6Frey70poycgouPwrIBpEw-3pj8yCqgGNSQlqeboASlB7uwi0-ZB4B7_oewbPquNM-0aNeVlEVHV6j_5m4jNglwdZSIydUxInd1Szs0BNaL-_VT4uABu4WIGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08010a728.mp4?token=sb3Fh3meAAmTo598egjuwC97VXHkf_lPUQUegLu0NTPc6LbLJZaH5te3qIsqgAApshbSSOCfbHQ2ufsLlrDtW5GiqY5q6VLIW4a1VZwHuhNoBWHD6KjiV-mTkXpFxilrTl7UIUofptiRzvZW3BDHeTA9qPj_HR1_IiRh24Tx3yiTW-3bwguvpU5RkUAiEm6620FtWvj4LrMZhbef80NvejpWf9CPW6Frey70poycgouPwrIBpEw-3pj8yCqgGNSQlqeboASlB7uwi0-ZB4B7_oewbPquNM-0aNeVlEVHV6j_5m4jNglwdZSIydUxInd1Szs0BNaL-_VT4uABu4WIGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پیشین ستاد ارتش اسرائیل:
ایرانی‌ها بسیار قدرتمندتر از آن چیزی هستند که تصور می‌کنیم
/
اگر کسی تصور می‌کرد قدرت هوایی می‌تواند باعث تغییر رژیم در ایران شود، اشتباه می‌کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/695517" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695516">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UToXgNeCnHQTYOvlV0HcBsHpKUM_HAqQVcGbwyV11pTCoYPruOfIP5OeIyChPOsPx4YRB-U9lDwtWZLQd754Wjj3QQo-TXdbwIJSjOm5vaZ4YnH69e0JOLyJ7HcSkyGcgobu1xwGGoyI4obvenz6T3VHHI5z-QKnFkMCsSB9qOLXQu6KYO-tPn_LSZ_zMHmqxC8icKtwUyO5wbBAt5TpAGwy365X2CJrSS4AyGEFSVeflXwuY6-DoZp0R8MhwpyCFy_IqiVMdBCnDZOT55qY7TgdSKZu_UcKku4uhRPRbSmxNflv5SLUYOSOzwhKhAIzADK_SnN63nCFfr7PXFP8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بالن هوانوردی هواشناسی برای بررسی شرایط جوی به منطقه اعزام شده بود، اما نگهبانان یک معدن آن را به‌اشتباه پهپاد آمریکایی تصور کردند و با سلاح برنو به سمت آن شلیک کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/695516" target="_blank">📅 16:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695514">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTAgfHopwzbmnG8mC9W2e_ju2u-ZcWpgU8LgrQvDsnzB46lQ3ZZ7SrOHaj_nej7l_NlBbzXzoFxTbwMfeunmOeFEoIZtKMSTq1EfCEtpdeTm5PEPNZDpZMUy9s8Trj77xzbZvaxrwDdHyNM2DkwxhVQdIVLz13V1Vo_aJDHeYUogBWrEtYsbAGo1nVtzfIN7QvwNdWO-2J7FQfe7y22xB6mnPuTQjFz9e7EDLMPgE_HxqH7Jlf4iJmEPhbwKPU1XE3hex5RA4QZe-daBFkIGGAInXSQSpoOqqD4fWVfyRHG2CTmqjCA_cP5JbU9AY8AC3C_l41rKbucigtoO6DvqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرانی‌ها بیشتر چه کتاب‌هایی می‌خوانند؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695514" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695513">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57ccb33f1.mp4?token=GaSMH9ynAmM1uT50Hm--96z_iEEePUP-X_4a8h_hygEGPlcnMhp33n8Zfbt9hGBNNVZGH2GIUy7v27-Pdg2XHA4-BzzJsGP6_4z5EGd594ObAAA6QYfyRhrtWu9FwpNKj6un9Gx7OKn90GDxb10mJr1GSCZywIx_USGzXUQoygRn0X7vcF4N_uqEyrlAMipkAQHap19k6lXbxgd3bi_A421xd8GKJXlKhFlEniJhm3w6GPlUzhsVH-aryjoJnDyPmSQpuA3Rromzrk-h1TcGgvBUgUQJCQOHIIfe8oNIOMKzY2ladInwKN3OuqO9wr1sXsnvFQq4He_CqwpGG7uDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57ccb33f1.mp4?token=GaSMH9ynAmM1uT50Hm--96z_iEEePUP-X_4a8h_hygEGPlcnMhp33n8Zfbt9hGBNNVZGH2GIUy7v27-Pdg2XHA4-BzzJsGP6_4z5EGd594ObAAA6QYfyRhrtWu9FwpNKj6un9Gx7OKn90GDxb10mJr1GSCZywIx_USGzXUQoygRn0X7vcF4N_uqEyrlAMipkAQHap19k6lXbxgd3bi_A421xd8GKJXlKhFlEniJhm3w6GPlUzhsVH-aryjoJnDyPmSQpuA3Rromzrk-h1TcGgvBUgUQJCQOHIIfe8oNIOMKzY2ladInwKN3OuqO9wr1sXsnvFQq4He_CqwpGG7uDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر برگی برای پتوس نمونده اینکارو بکن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/695513" target="_blank">📅 16:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695512">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: الان زمان مذاکره نیست و باید تصمیم گرفت
حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس:
🔹
من نشنیدم و فکر نکنم که عراقچی با ویتکاف، گفت‌وگویی داشته‌باشد آنچه که در سازمان ملل اتفاق افتاد، رد و بدل شدن پیام‌هایی از میانجی قطری بود؛ یعنی همان پیشنهاد ۷ روزه که داده‌ایم.
🔹
در حال حاضر، زمان مذاکره نیست و بلکه زمان تصمیم است و آمریکا باید اعلام کند که برای آن ۱۴ ماده‌ای که روسای جمهور دو کشور امضا کردند اراده عمل دارد یا نه./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/695512" target="_blank">📅 16:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695511">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148e4ff4cb.mp4?token=GUipMB5gQ-qBMwIHLmIXB07PSF0ksVqnAe_vVZIqILEYITPFMfDLiCjGZJ6fNCMKThVRerGSkvkGp5YPD29isjzvb8U3QxJnQ-Akif8jKy0FqAmSDQL-8ghpvCbGvoLuQZTjca4dtR91FvLCfK9VJssA0QWAF6wErDaZ6YQZM2ThzC9pdHhFYVg2KrCKtvJ0w6gzNZNwM9B59eEC55SsxEML0F_ykfPW3hIq7coxFdWreMloQCS9JFczQKubEEzwS5Rl20XxFE69vZbCR0cXLRWI92ppaJF_KFZE3Cljx979lJi9DLiSp82l-P-9Qx7rbw-VZoh9TgVTXf1Wn5qSxC96i5gQdKvNLjjFHvAjC4Sr87hoh5I31bKwOmS4DWR6yetepIMVn91rL7r4bRCz9hCDDFp6uIoskXzKqIld3gpULectacg8owZHWExsly1d9USGuKSt_8OfdCNTOIn-K6sfPoJWqVmvCEH5b9JifuwKmQLK6S_hxS3jQP9-ed8HSL8lxWddaFw0W1LD9MRTmcMs_9OTnk7jTK7PPLo6IiwscuhzxQv1IgbpMCj5BjVWgoUWz5B_cPDoo4P7u0nN_3bBHIvAuaad5BE_2Q6M7afASmUx7vH5D7xk1Ru5w3TmVQxo3mLJB0GtzOa9urxYyvpB8ptHfMTdyuT060BKECk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148e4ff4cb.mp4?token=GUipMB5gQ-qBMwIHLmIXB07PSF0ksVqnAe_vVZIqILEYITPFMfDLiCjGZJ6fNCMKThVRerGSkvkGp5YPD29isjzvb8U3QxJnQ-Akif8jKy0FqAmSDQL-8ghpvCbGvoLuQZTjca4dtR91FvLCfK9VJssA0QWAF6wErDaZ6YQZM2ThzC9pdHhFYVg2KrCKtvJ0w6gzNZNwM9B59eEC55SsxEML0F_ykfPW3hIq7coxFdWreMloQCS9JFczQKubEEzwS5Rl20XxFE69vZbCR0cXLRWI92ppaJF_KFZE3Cljx979lJi9DLiSp82l-P-9Qx7rbw-VZoh9TgVTXf1Wn5qSxC96i5gQdKvNLjjFHvAjC4Sr87hoh5I31bKwOmS4DWR6yetepIMVn91rL7r4bRCz9hCDDFp6uIoskXzKqIld3gpULectacg8owZHWExsly1d9USGuKSt_8OfdCNTOIn-K6sfPoJWqVmvCEH5b9JifuwKmQLK6S_hxS3jQP9-ed8HSL8lxWddaFw0W1LD9MRTmcMs_9OTnk7jTK7PPLo6IiwscuhzxQv1IgbpMCj5BjVWgoUWz5B_cPDoo4P7u0nN_3bBHIvAuaad5BE_2Q6M7afASmUx7vH5D7xk1Ru5w3TmVQxo3mLJB0GtzOa9urxYyvpB8ptHfMTdyuT060BKECk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی کوچک‌زاده: به خدا اگر از جهنم نمی‌ترسیدم خودم را جلوی بانک مرکزی آتش میزدم، اینها دارند کشور را به آمریکا می‌فروشند
نماینده تهران در جلسه امروز مجلس:
🔹
چرا مملکت اینطوری شده که راننده رفسنجانی هر کاری می‌خواهد در این کشور می‌کند؟
🔹
برای چه در اوج کمبود ارز بانک مرکزی گفته به هر بالای ۱۸ سال ۱۰ هزار دلار می‌دهد؟ اینها پول بیماران پروانه‌ای و مردم گرفتار است که در جیب سرمایه‌دارها می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/695511" target="_blank">📅 16:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695510">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COq4BEzvAxZ4meqLlXNzAljqUPsMEYN3q5u1epexV-YdrxtsgHPfNimU0Vdypd8YteP9y_OLa54ixkikpmPcA1_tKN1JZcNkD3La19UjhEDYVBwOC12HtufJ8zcn-mhU-kFPrb4PivIEC-OinHk4DxT4K6DKQdRVJL9yn8_B5_uTIapim4KfrEOMYqktNTDsQKIXnhI81UOHKS3h66wzKi1JOdN-9_8mZvqcAhmpsCsL9rn2mP-PjnfY496HNg5qYBd6B-WDlMTsB1Vhfh1Jtj5suty1QHmoQW-GJQ157mvZ1dxUGFOQC7nmyU2x4zP1LkqEZMT1-P3bk8Xf3mRWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع بسته های حمایتی لوازم مصرفی خودرو در سامانه جامع
شروع طرح از ساعت ۱۰ صبح روز یکشنبه ۱۲ مهر ماه تا اتمام موجودی
امکان دریافت نقدی و اقساطی
هموطنان گرامی می‌توانند با مراجعه به سامانه رسمی ایرانکو اقلام مصرفی حمایتی خود را به نرخ مصوب با محدودیت کد‌ملی دریافت نمایند.
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/695510" target="_blank">📅 16:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695509">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=upeK5X4miYkc5-1PEOfiuC1cMhOJZUh8lCjY4wyqVEq5EllMiDhTc9Q-m00pcaNn4V3eishMIRmAy9_iBDAP8036A2KBjxqvjw7lsOwj09bPcvCYl9tgvsQB_de_pXOvo56WzT1wp38iChNTSWyOleMvuRZ68jPah8XjJ6jMIKBhD4rIW9NmsElvdumoJaduVLOjeiLLV2vcYsd6Ey6b6fjUTQzBbQMZ08qOASVAm__oawXDM_wyDHTtY4a83aS9e5EXvppxfZVrlYJ35tOryMwGOabdMnJ_tb45-Pq4qOHqQOWzEmgOaWvIkB0nn5t8gd6xPTY44xp0sCRjL2tlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=upeK5X4miYkc5-1PEOfiuC1cMhOJZUh8lCjY4wyqVEq5EllMiDhTc9Q-m00pcaNn4V3eishMIRmAy9_iBDAP8036A2KBjxqvjw7lsOwj09bPcvCYl9tgvsQB_de_pXOvo56WzT1wp38iChNTSWyOleMvuRZ68jPah8XjJ6jMIKBhD4rIW9NmsElvdumoJaduVLOjeiLLV2vcYsd6Ey6b6fjUTQzBbQMZ08qOASVAm__oawXDM_wyDHTtY4a83aS9e5EXvppxfZVrlYJ35tOryMwGOabdMnJ_tb45-Pq4qOHqQOWzEmgOaWvIkB0nn5t8gd6xPTY44xp0sCRjL2tlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
شهروند عراقی: حاضرم تمام فرزندانم را فدای جمهوری اسلامی ایران کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/695509" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695508">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
اولین پرواز در مسیر مشهد - نجف پس از اعمال محدودیت‌های دولت عراق، امروز ساعت ۱۸:۴۰ انجام می‌شود
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/695508" target="_blank">📅 15:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695507">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQOgp7_Ruq-voT7tZG2m9cQADMZIhxi3q4_U2hQzhwAsEj26suQTNJlSH7cmexUSJGSCkAz37TFhRz4NSpACEtt5RHBJpXmUy2SW5bvGAB0U5bJSWlseUafl1Z2nn0eO4ISpfsA2Neld8Psszav_mPj2f4EAofwRuU3E5t82z1gQ3rR4l7JgxGWgldYmFyNl-cx6YK9p6iA_qob0Fw94rNsitmDqwJte1P1vXDphq_dFtxygw2lNf7YKNDsEmN9-4SZVoQJvkTHuEfem08kiZIKRt9DyDKjVW51JjZ0cCDORgFHZdPyhQYH3zKTkzJUsA4IhY-uToXCbDprUj4i8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: هزینه اجاره یک سوپر نفتکش برای حمل نفت از خلیج فارس به خاور دور به حدود ۱.۳ میلیون دلار در روز رسیده است
🔹
پیش از آغاز جنگ، این رقم کمتر از ۵۰ هزار دلار در روز بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/695507" target="_blank">📅 15:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695506">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c24488e9f1.mp4?token=l_e-SOVTyH15QpYnkpXVJ0WpuBgdwXDJrtDs4yukm1U8mu3xgKi0Ra8WNkffqsgqNUIJdZ6ur1Sy7VcPXRcyrSbbHFLoA2uwyH2zYOCbVmUgF8CbnTYJ45aDWKhS6m95apklrmqCXrXjXTN7Z7Pu9ciccWOUGfcGvDzM3l3A2lT80O6yv_r48GJFUD-74b-JrT3cv5WZhaKhriQtBQ6N9oXAawi-qN6v7jp0NCvCfNaf9DLHIZF_R5rjcXw54fgc4OuWF8YKVwb0MjbmozoYzW5ei5yp4Om5L2xMB2Pc1csaa595YjW0kktwoF1-oj1h4446rePzezczshu7Koz9-VV0CA4X-uviKdSnrhTkxehJQ-abcbAjs53GM5yiXMIb60F_poWVal7PuMZZJCg3A5PuSNERAeux4afBRbRmOhaHCcSWuDuWq1sjELCBstaC_3JYVJZ_hodJSSdqGJkLjLhLEBEotGE7lCDu6ivmRQWkM8AcCEAh6vKg0fyAQ4Hmayo6YaP8r8IpPCthf_otqc6t9SP4QPMgks6H0E_IUYZwLQkjXMsi9VZmqa4R-DC8ZVsnwjcNdjVhl6BLUEk9OZ3GfaK1ME5GQTZBKPpDV6re_BBq8DsxOn4I34AGA_xVo9nYemmuRIxk05JLBFHTAkLDVGkAMX3cIVrWvHyy2rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c24488e9f1.mp4?token=l_e-SOVTyH15QpYnkpXVJ0WpuBgdwXDJrtDs4yukm1U8mu3xgKi0Ra8WNkffqsgqNUIJdZ6ur1Sy7VcPXRcyrSbbHFLoA2uwyH2zYOCbVmUgF8CbnTYJ45aDWKhS6m95apklrmqCXrXjXTN7Z7Pu9ciccWOUGfcGvDzM3l3A2lT80O6yv_r48GJFUD-74b-JrT3cv5WZhaKhriQtBQ6N9oXAawi-qN6v7jp0NCvCfNaf9DLHIZF_R5rjcXw54fgc4OuWF8YKVwb0MjbmozoYzW5ei5yp4Om5L2xMB2Pc1csaa595YjW0kktwoF1-oj1h4446rePzezczshu7Koz9-VV0CA4X-uviKdSnrhTkxehJQ-abcbAjs53GM5yiXMIb60F_poWVal7PuMZZJCg3A5PuSNERAeux4afBRbRmOhaHCcSWuDuWq1sjELCBstaC_3JYVJZ_hodJSSdqGJkLjLhLEBEotGE7lCDu6ivmRQWkM8AcCEAh6vKg0fyAQ4Hmayo6YaP8r8IpPCthf_otqc6t9SP4QPMgks6H0E_IUYZwLQkjXMsi9VZmqa4R-DC8ZVsnwjcNdjVhl6BLUEk9OZ3GfaK1ME5GQTZBKPpDV6re_BBq8DsxOn4I34AGA_xVo9nYemmuRIxk05JLBFHTAkLDVGkAMX3cIVrWvHyy2rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حواسمان به دریای خزر باشد!
🔹
دریای خزر فقط آب و نفت و گاز نیست، بلکه پای پول، مرز، انرژی و منافع ۵ کشور وسطه و نکته اینجاست که منابع خزر بین ۵ کشور، به طور یک اندازه، پخش نشده. حالا یک سوال، چه کسی همین الان از خزر پول در میاره؟
🔹
جزئیات را  در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/695506" target="_blank">📅 15:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695505">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b53b1e6c.mp4?token=ETZc9tg86rH2IY9tWxRkVOrhUJ1VjiCb6kvFiHkNrvSKTytk2mDpwrGNA6PK7hsA0D7QsxPfH-bBZ6tfQ4eKe4W4atzeKFs66kRzrjCGp3jtrM7mXL0sOzgfsI2qrzfeGmTB0g1u_5vduI9U5fG4GdoNI4cuVk_SZNWtQy3oqpupNbbab1c_L06YvvkFXjJvr70nn5jBgsMhoxNdAQMuPeipZ_2mf0Lne46JFuJ2oXVN36J8jLHkLjPtio8Bzj1XpnMU6UzlXk9-sgQHIvRL_54jYQTLchhXR1YA1b8GhW-Jrbn0y_Z5wpo9mmn9iaVpCdG1hKhZsXwFyJMmk2WvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b53b1e6c.mp4?token=ETZc9tg86rH2IY9tWxRkVOrhUJ1VjiCb6kvFiHkNrvSKTytk2mDpwrGNA6PK7hsA0D7QsxPfH-bBZ6tfQ4eKe4W4atzeKFs66kRzrjCGp3jtrM7mXL0sOzgfsI2qrzfeGmTB0g1u_5vduI9U5fG4GdoNI4cuVk_SZNWtQy3oqpupNbbab1c_L06YvvkFXjJvr70nn5jBgsMhoxNdAQMuPeipZ_2mf0Lne46JFuJ2oXVN36J8jLHkLjPtio8Bzj1XpnMU6UzlXk9-sgQHIvRL_54jYQTLchhXR1YA1b8GhW-Jrbn0y_Z5wpo9mmn9iaVpCdG1hKhZsXwFyJMmk2WvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهین تسلیمی: شوهرم خوشگل و شیطون بود، دخترا ولش نمیکردن
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/695505" target="_blank">📅 15:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695504">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZjYwDDF9jLuDFu4cmSvDUZHOTzwO51dnQDDIxvuXCy5iLLQPNOeboyaSRL6NfeUu6qjq3N_j7BvgVXPYb8sRYqZPRnPmaoqau39tzcrPkxo63_5eoSILH2tgThoRjUS6cgoX3XcL_VK1r8-pm6PdPFRlPGtvpNURG60eFKdvVtUvhCD5i0YVnlstv4e33PfeMR8jwWUWikliJqSiZGeigAeyPZccuywCmUBdNJtmihxNMwx_2Id8XbiXCQP8BvyRmbh74voa7zGrM0w6gANoY8LJUF2rRukvIr5msiAtP9UsZgiss6I2RRYD3Mj5VcEhE46xplozRblrqETAzSVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«کاوان» در راه بورس تهران
🔹
شرکت مس کاوان نماد با نماد «کاوان»، از ۷ مهرماه ۱۴۰۵ به‌عنوان ششصد و چهل‌ودومین شرکت پذیرفته‌شده در بورس تهران، در فهرست نرخ‌های تابلو اصلی بازار دوم درج شد.
🔹
ورود «کاوان» به بورس، مسیر تازه‌ای برای تأمین مالی، توسعه پروژه‌های معدنی و صنعتی، افزایش شفافیت و تقویت حضور این مجموعه خصوصی در صنعت مس کشور ایجاد می‌کند.
🔹
سید حجت زینلی، مدیرعامل مس کاوان نماد:
مس یکی از فلزات راهبردی اقتصاد آینده جهان است و توسعه انرژی‌های تجدیدپذیر، خودروهای برقی، شبکه‌های برق و زیرساخت‌های دیجیتال، تقاضا برای این فلز را افزایش می‌دهد. ایران نیز ظرفیت بالایی در صنعت مس دارد و با توسعه اکتشاف، سرمایه‌گذاری، فناوری و فرآوری می‌تواند سهم بیشتری در اقتصاد و صادرات غیرنفتی داشته باشد.
▫️
مشروح خبر
titrtejarat.com/fa/tiny/news-11141
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/695504" target="_blank">📅 15:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695503">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سید ستار هاشمی، وزیر ارتباطات: اینترنت ماهواره‌ای جایگزین اینترنت زمینی نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/695503" target="_blank">📅 15:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695502">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=IBKo6xfRBnEBpD3fV9PZHdzVB-Qu4kf5eTTOSmubSUL72kjbS13BtfYYMnNuREDvkU5eD_l3GctFVpvbqIr4zCka5ok2bTEJ8ae-S10n-RTBIMWBizsER9W_Xb0N2cKs0jYX7L37SALLNuZ4SVQQ1mfS-wkY33YIDXa-zhuZLFDkaK8f14FAqZTHr-iS5pJ-cCLkhZMgRcXIaeqeJ3Pp9-0xxgED8O6T_KhKw0vgMrdHOxnapzXQQdk5NErTrqmGC-A35CHZno6x0-3cgkoLPcvvcfADQYPXx12h67-eTS_TTUF3YUWKlO9qTnGx0cZD1ASzaj7EQHxsKocJch7gAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=IBKo6xfRBnEBpD3fV9PZHdzVB-Qu4kf5eTTOSmubSUL72kjbS13BtfYYMnNuREDvkU5eD_l3GctFVpvbqIr4zCka5ok2bTEJ8ae-S10n-RTBIMWBizsER9W_Xb0N2cKs0jYX7L37SALLNuZ4SVQQ1mfS-wkY33YIDXa-zhuZLFDkaK8f14FAqZTHr-iS5pJ-cCLkhZMgRcXIaeqeJ3Pp9-0xxgED8O6T_KhKw0vgMrdHOxnapzXQQdk5NErTrqmGC-A35CHZno6x0-3cgkoLPcvvcfADQYPXx12h67-eTS_TTUF3YUWKlO9qTnGx0cZD1ASzaj7EQHxsKocJch7gAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه بخاطر رتبه ۳۰۰ تجربی؛ وقتی یک کنکوری رتبه دو رقمی میخواست اما رتبه ۳۰۰ کنکور شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/695502" target="_blank">📅 15:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695500">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت مرغ به ثبات رسید
افضل ملکی، رئیس اتحادیه فروشندگان گوشت و مرغ در
#گفتگو
با خبرفوری:
🔹
کاهش قیمت مرغ به دلیل افزایش عرضه و رسیدن نهاده‌های مورد نیاز تولیدکنندگان است.
🔹
جوجه‌ریزی و تأمین نهاده به میزان کافی انجام شده و عرضه مرغ در بازار افزایش یافته است.
🔹
قیمت مرغ به ثبات رسیده و پیش‌بینی می‌شود برای آینده مشکلی در بازار وجود نداشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/695500" target="_blank">📅 15:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695499">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e758b833ff.mp4?token=rLYyDIpBQ549NTJxbdeWhWbaGojNsIzXS6GImDYyBnzyV4E74x-M1vgq4OABuks7E_fnGkDTVocYSyqdxScertgArf-vR835DSM_8tjGeocVPq1brCuRBueS2FZSHLxzLLYTu7PoGHhzKJyJGCP-rIKnX71QXCvTJzO8h7cLRZxs4A29ZKN0YKvAICbpHjT-qrtxx_AhaphOxhnBgPTZn_FJi0amMv6BIigCer78steIDsTfc2OJreJatB0lbV4vtmjtEBJ5bCM9AjtEIxJJJ7mg_v5dSZ4LPdi-_8aME9IxVQw2ksEWV0v8IjLG5XnNrlW3etOxGIzYsWSubh9-7i_9B1JpQdj7we31BtLqEIqe5jDb1s-j6CvLvIOMXDgohd9rbcajOakI2v5VXDZbiSQwulwu4qZGj-R7c4AMNXdk4t-4xh_NK4J6jYiwoMX6_pLXkMYrldrS4hEVUhSWFhxsl1pbte25bEFFgoJQjbPjlrijyq4XsJM7Enlua2bwiK1PawndHonhqGFmn4mK15CeY_9lW7CyuGM8fzR31uH00YXoQxzNAh3cBgchUvyduEYEo88ClwHUa8REuu8j4OQDnW6b_lyO-IlyKXl8lFcUx-7bi__tHniQK8ccscI5dnlMNhQo0DAsYjeNYPvHxPVp-aPb9wKVZbymctzg9Vk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e758b833ff.mp4?token=rLYyDIpBQ549NTJxbdeWhWbaGojNsIzXS6GImDYyBnzyV4E74x-M1vgq4OABuks7E_fnGkDTVocYSyqdxScertgArf-vR835DSM_8tjGeocVPq1brCuRBueS2FZSHLxzLLYTu7PoGHhzKJyJGCP-rIKnX71QXCvTJzO8h7cLRZxs4A29ZKN0YKvAICbpHjT-qrtxx_AhaphOxhnBgPTZn_FJi0amMv6BIigCer78steIDsTfc2OJreJatB0lbV4vtmjtEBJ5bCM9AjtEIxJJJ7mg_v5dSZ4LPdi-_8aME9IxVQw2ksEWV0v8IjLG5XnNrlW3etOxGIzYsWSubh9-7i_9B1JpQdj7we31BtLqEIqe5jDb1s-j6CvLvIOMXDgohd9rbcajOakI2v5VXDZbiSQwulwu4qZGj-R7c4AMNXdk4t-4xh_NK4J6jYiwoMX6_pLXkMYrldrS4hEVUhSWFhxsl1pbte25bEFFgoJQjbPjlrijyq4XsJM7Enlua2bwiK1PawndHonhqGFmn4mK15CeY_9lW7CyuGM8fzR31uH00YXoQxzNAh3cBgchUvyduEYEo88ClwHUa8REuu8j4OQDnW6b_lyO-IlyKXl8lFcUx-7bi__tHniQK8ccscI5dnlMNhQo0DAsYjeNYPvHxPVp-aPb9wKVZbymctzg9Vk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">​​
♦️
چطور وسط دریا یه سکوی نفتی میسازن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/695499" target="_blank">📅 15:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695498">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
جزئیات قتل عام خانوادگی در اصفهان به خاطر سگ‌های خانگی
🔹
دو خواهرزاده که پیش‌تر بر سر نگهداری سگ‌های خانگی با دایی خود درگیر شده و او را با چاقو مجروح کرده بودند، این بار با ادعای گرفتن رضایت وارد خانه او شدند و دایی، همسر و دو کودک ۶ و ۱۲ ساله‌اش را به قتل رساندند.
🔹
پس از ناپدید شدن خانواده، بستگان با مشاهده گم‌شدن یکی از فرش‌های مقابل خانه مشکوک شدند و اجساد چهار نفر را زیر زباله و آهک در پشت‌بام پیدا کردند. دو متهم ۲۹ و ۳۵ ساله بازداشت و به قتل اعتراف کردند؛ مادر آنها نیز به‌عنوان مظنون بازداشت شده است./رکنا
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/695498" target="_blank">📅 15:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695496">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیام الیاس کردی | Payam Elyaskordi</strong></div>
<div class="tg-text">امروز یه اتفاق زیر پوستی تو بازار طلا داره میوفته
.
طلا گرمی 26,606,700 معامله میشه اما هنوز 1.8% حباب منفی داره
یعنی 468 هزارتومن زیر قیمته
یه نکته فنی بهتون بگم
، سکه‌ها حباب مثبت گرفتن تو این چند روز اما طلا 18 عیار حباب مثبت نگرفته هر وقت سکه حباب مثبت میگیره ولی طلای 18 عیار حباب نمیگیره یعنی نوسان گیرا تو بازار هستن نه سرمایه گذارها (احتمال نوسانات زیاد هست)، حواستون به بازار باشه برای دوستاتون هم که این روزها میخوان معامله کنن این پست بفرستین حواسشون باشه.
@payamelyaskordi
✅</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/695496" target="_blank">📅 15:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695494">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4eb0b1e68.mp4?token=BQNuPO3af87Mpql-PMCa1aZtNAKmO0bUIU-ts5-O6fahauPmn9VGD8K-QkXLrNH89W8ti_faiCxSJBDQBPAQvCRxh8scqBx7AkpiHF3GXhsO2HECPQKdpsWcfzbjXwT1lcrTiP989CxKpID1K7oP9JCmrGEx0M8aCevKsk0Vw7OEbxwmfV30YcBXRnJCK8MwonQWFWUiqfAHxVXzk-x3pJHUrZmXQREsn_zCRa76_L3sqCX3FTFqzwdpE2koY-mJ8GjpQB_eN_g2tTQ_p_BpMnyPa5MAr89vrQ-cX6RaBnK76Q6GB3_MEHDYDOMbUGTDhU_a1mnnLNTrQnQfclLbkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4eb0b1e68.mp4?token=BQNuPO3af87Mpql-PMCa1aZtNAKmO0bUIU-ts5-O6fahauPmn9VGD8K-QkXLrNH89W8ti_faiCxSJBDQBPAQvCRxh8scqBx7AkpiHF3GXhsO2HECPQKdpsWcfzbjXwT1lcrTiP989CxKpID1K7oP9JCmrGEx0M8aCevKsk0Vw7OEbxwmfV30YcBXRnJCK8MwonQWFWUiqfAHxVXzk-x3pJHUrZmXQREsn_zCRa76_L3sqCX3FTFqzwdpE2koY-mJ8GjpQB_eN_g2tTQ_p_BpMnyPa5MAr89vrQ-cX6RaBnK76Q6GB3_MEHDYDOMbUGTDhU_a1mnnLNTrQnQfclLbkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا شیشه‌های امروزی با شیشه‌های نوستالژی قدیمی فرق دارند؟ #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/695494" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695493">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbae2c93ef.mp4?token=K8gUonmLm0UqIU1Be3aQbPQD1CxDqcRn8HrcZILZVmMHwTnZZ7Id12YfPKJz8NSsIE-kZGv2pR8XxrkBmZPj20icUN4_LuRqWK4cImbLUNzGZfT7tho8l8SVfmqRHqPDsWsOOJ-T3v6yTeULW9uge6FsALfT0OYlZ62SvoWbdQzHwSBcE7VRvOVDdPrROQx1SrgNrKNXqO81DXarbfkDtnFkM_jSQhxmCYB9jaDlxSpOCdI8wr1rvkxgwqUwepePLY4QDL024aNOKq0ixQJ6COgTq4rcDXmtZJJBIZm7uY5E367rmOAM0aVxY5jIao8wIHgO2Iw6FVjtKVXcDCUcJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbae2c93ef.mp4?token=K8gUonmLm0UqIU1Be3aQbPQD1CxDqcRn8HrcZILZVmMHwTnZZ7Id12YfPKJz8NSsIE-kZGv2pR8XxrkBmZPj20icUN4_LuRqWK4cImbLUNzGZfT7tho8l8SVfmqRHqPDsWsOOJ-T3v6yTeULW9uge6FsALfT0OYlZ62SvoWbdQzHwSBcE7VRvOVDdPrROQx1SrgNrKNXqO81DXarbfkDtnFkM_jSQhxmCYB9jaDlxSpOCdI8wr1rvkxgwqUwepePLY4QDL024aNOKq0ixQJ6COgTq4rcDXmtZJJBIZm7uY5E367rmOAM0aVxY5jIao8wIHgO2Iw6FVjtKVXcDCUcJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواشناسی: استان‌های شمالی و برخی استان‌های شمال‌غرب، غرب و جنوب امروز هم شاهد بارش خواهند بود
🔹
همچنین فردا در بخش‌هایی از استان‌های گیلان، مازندران، کرمانشاه، ایلام، اصفهان، استان مرکزی و لرستان باران می‌بارد؛ موج جدید از بارش‌ها پس‌فردا وارد کشور می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/695493" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695491">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88dcc5c70.mp4?token=kk7O94o1oPbK1rATJiUOUHeWLe6Q1XC735MY6_uQ--3Ewo7AT6J_vFutXukfYDdRjxr5H33w0I_xZRO7BlHNFk7_k_qh0aQuDiahvgq3aZo-JSFu6YfqmCoty0P_By8EjHk2fXSL7IGQOcrvsmX7B8RUk2bhfdbgyFn0ZzaISnpn_n1IS4e-duRA50bPYYToVlZXPrUNOrNBcwrB6K2GFGxhNYzElbB2eljhkx6anNEQ_Zv62jyPQ3MkR2GkSEASJxLe_DjGnfSHliXOVquDBzoOQC84L8Y4QRaid9V7D0TjfzuOg_dgp-gi6SEBtYMJfgGBDkFyzWlVNqi5nICawA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88dcc5c70.mp4?token=kk7O94o1oPbK1rATJiUOUHeWLe6Q1XC735MY6_uQ--3Ewo7AT6J_vFutXukfYDdRjxr5H33w0I_xZRO7BlHNFk7_k_qh0aQuDiahvgq3aZo-JSFu6YfqmCoty0P_By8EjHk2fXSL7IGQOcrvsmX7B8RUk2bhfdbgyFn0ZzaISnpn_n1IS4e-duRA50bPYYToVlZXPrUNOrNBcwrB6K2GFGxhNYzElbB2eljhkx6anNEQ_Zv62jyPQ3MkR2GkSEASJxLe_DjGnfSHliXOVquDBzoOQC84L8Y4QRaid9V7D0TjfzuOg_dgp-gi6SEBtYMJfgGBDkFyzWlVNqi5nICawA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاهش اعتماد به آمریکا؛ چرا کشورهای خلیج فارس به سمت چین می‌روند؟
آلن گرش، روزنامه‌نگار فرانسوی و تحلیلگر مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
کاهش اعتماد به تضمین‌های امنیتی آمریکا، کشورهای منطقه را به سمت ایجاد روابط گسترده‌تر با چین و دیگر قدرت‌ها سوق داده است؛ اما خروج کامل از مدار واشینگتن همچنان دشوار است. جهان در میانه یک دوره گذار ژئوپلیتیکی قرار دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/695491" target="_blank">📅 15:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695490">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUVwj7eW9k7q0_i-Y2_JZyexcQKsgbCm1b04dvnyQPJlXoMzCt1oUNUMlAk94J06UeGBmTSFeaIvui_Vmbsfj7egiW8c6prcsJyVaD3NdD8MuXzDRrbo6uYe6xIsOjpuTP4xeadCgu2g1Cwh4H9GGQPzATzfJ3MD4M0ALj5c8SD4Xz56Bm5GsezhnKiWuc9h6R70Nl9T11ehHwcpGxW7ngMiUyF9s8EoL_viYaqppKDXLVR-8J0ANY3maJL9UokLVEJRocsUUM4feUlqMX3JgetqxgLfsGcu_3LgPir0lon_DuhSkValsGIBfrZFJ1GKtRAga9dxpCAanYcjiEyoyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/695490" target="_blank">📅 15:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695489">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49db8350d3.mp4?token=rf3r4_o-Sbki_ke4zQfNIaThIwsO0yNyK82e11-7jxPjnceahi1u7Vhf1RRs188Ny63ORPYARqJ6ivXjcY48_yGgMFxWQ8vv-xRmFQhJGzUdDHUHbFzyvSnH6hiNX04-asiiMwiv_Or_qcrgCLQxXydpcRsWc30I5KJHLJziSyoB1QqnaqiZ8LcHNFA8imZEuptHe6VoYiISnMKiGSON0JL3ukPt8WWZPIPsFUn-olm7ovTpgpsZdHraa5ZMO02tQ2N6pE52xGJugAZGk9XnN5TWi_SJdjBTXy-fLIPvSmS6r_t0B37eh_ogUyQr6UhVhhh_PAL9kvYCW1J2_XO0WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49db8350d3.mp4?token=rf3r4_o-Sbki_ke4zQfNIaThIwsO0yNyK82e11-7jxPjnceahi1u7Vhf1RRs188Ny63ORPYARqJ6ivXjcY48_yGgMFxWQ8vv-xRmFQhJGzUdDHUHbFzyvSnH6hiNX04-asiiMwiv_Or_qcrgCLQxXydpcRsWc30I5KJHLJziSyoB1QqnaqiZ8LcHNFA8imZEuptHe6VoYiISnMKiGSON0JL3ukPt8WWZPIPsFUn-olm7ovTpgpsZdHraa5ZMO02tQ2N6pE52xGJugAZGk9XnN5TWi_SJdjBTXy-fLIPvSmS6r_t0B37eh_ogUyQr6UhVhhh_PAL9kvYCW1J2_XO0WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیین اختتامیه یازدهمین جشنواره رسانه ای ابوذر ( برترین رسانه های ایران)/ انتخاب خبرفوری به عنوان برترین رسانه در زمینه روایت اول
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/695489" target="_blank">📅 14:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695488">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd93505e25.mp4?token=WREekaGl5F7AZibv2UtweNWj9m_Mt_S7rHjkuwbHpD0m9JmUEqNtCjxBu8En0VLe09gSjjFJ3xGkxTumGKb1JXMtxsFQBdqjyefK02yDfY2B7_bBEnIVeQ3F0kNuYaZFIzVxBjW65X1Lcwe1fT0eOH37fiYVLPjjpmiBboXsVN14fEHKsqNctqWdeYnj44O7Qd9Gdp3GzJGZaaWIDm41liRK7qLTEdhFA7JIsRICSwdqcpO_A6eJAd_SRwPPaRptfYy-2yq5b8HyMZCQNLbCf5GY5wdlimiiRabCPUr9NGH8tfYjLtnNhLnR17a40sF5H20dmjbBgiBKBfpzeIv-ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd93505e25.mp4?token=WREekaGl5F7AZibv2UtweNWj9m_Mt_S7rHjkuwbHpD0m9JmUEqNtCjxBu8En0VLe09gSjjFJ3xGkxTumGKb1JXMtxsFQBdqjyefK02yDfY2B7_bBEnIVeQ3F0kNuYaZFIzVxBjW65X1Lcwe1fT0eOH37fiYVLPjjpmiBboXsVN14fEHKsqNctqWdeYnj44O7Qd9Gdp3GzJGZaaWIDm41liRK7qLTEdhFA7JIsRICSwdqcpO_A6eJAd_SRwPPaRptfYy-2yq5b8HyMZCQNLbCf5GY5wdlimiiRabCPUr9NGH8tfYjLtnNhLnR17a40sF5H20dmjbBgiBKBfpzeIv-ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین زمان آبیاری گلها و گیاهان را بدانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/695488" target="_blank">📅 14:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695487">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9ORT01id1rZHVQkIPSpH72URim9r06aV0GrKdxeKNaZV2CwaDiwJc_dAvDRjvM2N_6ZEu0P4XQkrski0WNbCVb0m-Dh6aQV1NQlTbHSc7c58gItkOH8PYjKcM4sVscElzSZr5RKE4i4hdnfMaE59Df6j3TdleF4Oqze21bEmwhwMmCyY8tnuO99jLiHffTFD5iKQJUfxEp3Tk0QGHg5Ur2aWLuIYzRuXYvrLYvE2kg1QlX53MsOLqqcHhYeNuwHz62d1spR76YRLXblmh_1a5xqeETIsPJu6eACelRyVBhDGq4Uu0C5De4UGE37GhRAsUEzRhj4hmUd027uT00j6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وبینار "
راهکارهای حفظ سرمایه در برابر تورم؛ مقایسه فرصت‌های سرمایه‌گذاری
"
در
شرایط تورمی
امروز، یکی از مهم‌ترین پرسش‌ها این است که برای
حفظ ارزش سرمایه
کدام گزینه مناسب‌تر است؛
طلا، دلار، بورس یا مسکن؟
در این وبینار با حضور
پوریا بختیاری، پژوهشگر اقتصادی، بنیان‌گذار و روایتگر پادکست اکوتوپیا
، وضعیت اقتصاد ایران و جهان و مهم‌ترین متغیرهای اثرگذار بر بازارهای سرمایه‌گذاری را بررسی می‌کنیم تا تصویر روشن‌تری از
فرصت‌ها و ریسک‌های پیش‌رو
داشته باشیم.
🗓
۱۴ مهر ۱۴۰۵
🕖
ساعت ۲۰ تا ۲۲
مدرس: پوریا بختیاری
✅
شرکت در این وبینار رایگان است
👈
ثبت‌نام رایگان در وبینار
👉
❤️
@talasea_mag</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/695487" target="_blank">📅 14:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695486">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWGTxZbQKQxLv96BzdE-IYKLUBcraOjDnopLkNRIXlBz7WFyj20hpCjo1A9LN8WS0nC6y70T4OgmxZWLsW1dQT-S7utQ27ad-Fn6IX17TypradGovUv07Ze6UrzgjpPuCLclr92xJUU4w0tiFKA8uQpWRFU54k1EELzWJ0xIRpnpydMlkf4UuzQkkhoot-xv430t_FpruS-vWa0bqmjhklpCz-28gADF8y17ehTJTaH1-qDtduxGL4HK7JFD-A6HbYoUnhWfxInYnaNmsn6ycf7OsqvRCa71k8cmVyFBz3gUTnO1cHB_O-kyshVFbvgTkTLOExhTnNRFiqi_LVCOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین برف پاییزی بر دماوند نشست
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/695486" target="_blank">📅 14:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695485">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
بیشترین گلایه مردم از پلیس به‌خاطر چیست؟
سردار عباسعلی محمدیان، فرمانده انتظامی تهران بزرگ:
🔹
غفلت، حواس پرتی و دقت نکردن به محیط اطراف و رعایت نکردن توصیه‌های پلیسی عامل اصلی بسیاری از جرایم است.
🔹
حتی همکاران ما با شهروندی که غفلت کرد و با گوشی در خیابان صحبت می‌کرد همراه شدند و گوشی را گرفتند و آخر سر به شهروند گفتند مامور هستم نگران نباشید، ولی غافل از محیط اطراف نباشید.
🔹
بیشترین گله‌مندی مردم از پلیس به‌خاطر نوع پاسخگویی و شاید همکاران ما نتوانند نظر همه را جلب کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/695485" target="_blank">📅 14:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c27a68aef.mp4?token=OBXrWcPpTVar_aNu4vhd2JzdMFyaI0t4MJMyD2__Ghia7JTpkC5oeQEVohqrpwQmAuFfdnllgLgK-Oj_MFrX8sFFQ4pUunowXjo4-TxuXSCIHR4qwcG7DWTx89DtomQUz1j8P6xcHPbQEZA--uJ7-96lSl0VrmPhka_MrDTsdfWH8wq_TiK0TglblZIIukVJscLzHDu5z9TKoaxKAxOPjDFksxyCDA3aVApsX2MKHUG0-lq-PcCpFq3hYHZpcZ2c9uSC0lh-IYyE6A5Uh5EKZIWgTSo1vGFbZloOYToTb6V23mPQQgZG7AeG7zfUy6mF-dRbS7zvMwDJEQDehljHmBJ80G7voNxhvaCKY2HSZonYzAmg9sOfTCyvullu9AVOm89PzVc0q-2Q_9AgxLF7M9WrcRVt4YmX0fT3LMntEJZRonUkP0mAtOvNBAlVoSKAO3Btw8FJ1IotrRFkgAdqx7mZ9clnpvI-jUbbqWQ41GqmiGQ0oeIsde_LA2K_E0TnvMFSKjZOJ9YGq0WsS6T5YitGTlwMVx_qnGgLQ6t4hpngFrBRnPrN9SL1NWH9ssRriyIzWdP5SKUvtyeiJhbkERyGSCm73jfj0cICK6xp3oK_YlAnb5gxvZ_TXSnm0_pHScAhbwxikZxehEuvtb0sk_7ApkOngXnJpcYP-_SJ9fY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c27a68aef.mp4?token=OBXrWcPpTVar_aNu4vhd2JzdMFyaI0t4MJMyD2__Ghia7JTpkC5oeQEVohqrpwQmAuFfdnllgLgK-Oj_MFrX8sFFQ4pUunowXjo4-TxuXSCIHR4qwcG7DWTx89DtomQUz1j8P6xcHPbQEZA--uJ7-96lSl0VrmPhka_MrDTsdfWH8wq_TiK0TglblZIIukVJscLzHDu5z9TKoaxKAxOPjDFksxyCDA3aVApsX2MKHUG0-lq-PcCpFq3hYHZpcZ2c9uSC0lh-IYyE6A5Uh5EKZIWgTSo1vGFbZloOYToTb6V23mPQQgZG7AeG7zfUy6mF-dRbS7zvMwDJEQDehljHmBJ80G7voNxhvaCKY2HSZonYzAmg9sOfTCyvullu9AVOm89PzVc0q-2Q_9AgxLF7M9WrcRVt4YmX0fT3LMntEJZRonUkP0mAtOvNBAlVoSKAO3Btw8FJ1IotrRFkgAdqx7mZ9clnpvI-jUbbqWQ41GqmiGQ0oeIsde_LA2K_E0TnvMFSKjZOJ9YGq0WsS6T5YitGTlwMVx_qnGgLQ6t4hpngFrBRnPrN9SL1NWH9ssRriyIzWdP5SKUvtyeiJhbkERyGSCm73jfj0cICK6xp3oK_YlAnb5gxvZ_TXSnm0_pHScAhbwxikZxehEuvtb0sk_7ApkOngXnJpcYP-_SJ9fY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مچ آستین لباس‌های بافتنی گشاد می‌شود، این روش به رفع آن کمک می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/695482" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0IaBAFYyIJ7c1Ub5uNhCXTj0DUGJ60xkf_s0j0QZTZWDP16Nk11QmvL7JrC6bG7PJSGNhOSPSCJn83F1CYj1IpMB9KGH_QpuUABoirFKdBCCXVORROoNuq0As2QLzTLoK1I3oufBU3BIVMi9NrTULNT1_H1pvI7En5U4sK6YiubA1F_z6uUJBPRMxtFdQEx4lvNihPVuo8VUu-nDsoj5T_ngDAFoeVSG844cHAIcJi558slMQ11SDelAOu1yFKuhQiB6YwtpqDH6D95L7hLwEXAlgS1EaPtvqFRfe-CUTHPItxpKIWAZlazj3cVV04ivc89c1AiwpAxNK2-ZH_BWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عرضه اسکناس دلار با کارت ملی در شعب منتخب بانک ملی ایران آغاز شد
🔹
عرضه اسکناس دلار با کارت ملی در چارچوب دستورالعمل بانک مرکزی از دیروز در شعب منتخب بانک ملی ایران آغاز شده و افراد بالای ۱۸ سال می‌توانند تا سقف
۱۰ هزار دلار
برای خرید ارز اقدام کنند.
🔹
متقاضیان علاوه بر مراجعه حضوری، می‌توانند درخواست خرید ارز را از طریق پیام‌رسان
«بله»
و بخش «خدمات» و «بازوی مدیریت بازار ارز» ثبت کنند.
🔹
ارز خریداری‌شده با نرخ فروش اسکناس در سامانه ارزی ملی (سام) محاسبه و پس از طی فرآیندهای تعیین‌شده، از شعب منتخب تحویل داده می‌شود؛ دریافت ارز در روش غیرحضوری نیز منوط به ثبت اطلاعات در سامانه «سنا» و ارائه شناسه فروش است. /
متن کامل خبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/695481" target="_blank">📅 14:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcfuCGIT4mf4kfe-Jc6uwYIZs1e14XEmGjNGtWzeeXeisClFHCII-b-XGZIOgAhcQlZBlR_-ELQUotr_HjNgmX9B1xnmqn1OyLynYOLcccgGuJZTS7sGrr7DHimejjyDUyuX1_ZBhME7RAm98TON9MsxTR9hkGAMa7p761VG702Q-23ax_X9jijopb0mSO--K9kGoFeDM7qBu74W3DJ1b7IiTiv29DbaVQ5demyCdFNe2o2Msp9gnOF2aG2SrJCFA26iwmh0n1kVqXAboj7Y8kDbCTursL3XTmWh49zgismkTtUpV-cP4VWAi-6VJEV4cCPgYjGqqGikMLTJgbktag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAB27p6CEq760wJvkGKFZTWpAl6PhgmMxYCQm_U8VzPqavUAHg3ZAktl-b4MceoqBjEBVpYYJ-bS5uICK2oSf86RYbeuNnbAUKFmXHUjMHiaBC1hUK7H0woZCe_ySdFxbSMbNjKHSSyAWoh-5AkyCzfDmf04wOeSpmnzeC1qubp51jEOsP9w4EYnJNpm3WB0TZsH917ZlYIJ-jI7zqpsrEV46c0G8QwuXtVdmDM_4wRqFZr4Gvl8HpWgSm1q1wI-Xtaailh_64jUi5vyfAE6tYybLaWgGY5eDNuq-V3CqENjwgSbZJQmHriWy17E9_3LlOnPgyyuleYvZZY_DEC6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RD3HquXZYkHPzVEIQDzz03LRixtw2M0obTN3dEQbrsKYiXKw_oOry_LOOXR8xNlYbUV2iPIRjow3VdSWNVqXZ4E-P9oVYqI9ipuc7qTOXd7kDSV6EGHjq0SsP_zISFLcofkNa3mcKYnBRLxLATsoHJmAc-98HhfuIwZOIb-UexzoI9kTDuK_WeIDmg71S8ujULRf5TunHEWN7HAKEFJOBdWcsPywyWoX6zHREJ2qf4geubuxJ2TDqwn6e98xZhZQywn7PbsOWPWGqkPcpaF7sX1YeeEDX86FyDm4vqRELj4RGYoNnSAxvLCWFui77gb7ROSeaneLs3QdQsNIQOKUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAzKanCR93yl8i5lY3IK3Mk3AsDgWGwkc_XTxuqCl67FIukbzORNsTT6a-BaiMphLwcl9i6EH9-W10ApW8P1DUkjMpAPXbp_AsswC6ghn1X5qF4XwWvx0d4KlUMObc5gWuv7wm0LbwtmAvRgiVZ13WgCxrb-1lMI7dTMOkRby-qFXefWjDuU33YFTBHF8dk63zfFGwTWuwZ62CWdmCFJ1VR0jV2GSw1rwFayODbbeOk9LUe-41-jmtZh4YhPdmjitJf5mn1P864_bNuGc5cht7kZHKkp7zLj-iZ-oPbyE8tx9bOBJDHdMfwscw8cbzTpsIoDeIwXuN9OFVVHlEIdxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از اینکه سال تحصیلی جدید شروع بشه، این اپلیکیشن‌ها رو بشناس
📖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/695477" target="_blank">📅 14:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۹۵ درصد کالاهای آرایشی تقلبی هستند
مسعود تهرانی، نایب‌رئیس اتحادیه لوازم آرایشی و عطریات در
#گفتگو
با خبرفوری:
🔹
فروش لوازم‌آرایشی نسبت به سال گذشته حداقل ۷۰ درصد کاهش پیدا کرده و مصرف‌کنندگان به دلیل گرانی خرید خود را به حداقل رسانده‌اند.
🔹
یک محصول که در سال ۱۴۰۴ حدود یک میلیون تومان فروخته می‌شد، اکنون به حدود ۲ میلیون و ۸۰۰ هزار تومان رسیده است.
🔹
بر اساس اعلام مسئولان غذا و دارو و سازمان صمت، ۸۰ تا ۸۵ درصد خریدها کاهش یافته و همچنین حدود ۹۵ درصد کالاهای آرایشی موجود در کشور تقلبی هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/695476" target="_blank">📅 14:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695475">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
صدای انفجار در بندرخمیر مربوط به عملیات شرکت گچ خمیر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/695475" target="_blank">📅 14:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb41196e9.mp4?token=PVHbDOcpe-DBUeca1lLE1NbdNL61F43M3Y6i0n_zMY3u8Vm8XONbftWkO6QV3dNwJnSYyHRRUCWU7efNN1JPBWUcS5sOFrnM_ZoUabLISaE1umL_seq93rh7p9AXs_R9bv2rdX80EihWWm8jjWS399usoiH9e8aVeMZsyjuueGcMTWJ3i9buA39lev5PXk6FTPZrgbl_HQUh0ZjqmoxnCQidwChPhkoCcNPGmdMFLEVzpFvTca1dNfhCTSum1h2mhJ190lrciaGkyNG8j_VlX-uQxM1u1fkbnrC0gd0aNoHxUcaylqdCQyI28m9xZ_dpRsfavDRjvUTSSkfxrmRtSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb41196e9.mp4?token=PVHbDOcpe-DBUeca1lLE1NbdNL61F43M3Y6i0n_zMY3u8Vm8XONbftWkO6QV3dNwJnSYyHRRUCWU7efNN1JPBWUcS5sOFrnM_ZoUabLISaE1umL_seq93rh7p9AXs_R9bv2rdX80EihWWm8jjWS399usoiH9e8aVeMZsyjuueGcMTWJ3i9buA39lev5PXk6FTPZrgbl_HQUh0ZjqmoxnCQidwChPhkoCcNPGmdMFLEVzpFvTca1dNfhCTSum1h2mhJ190lrciaGkyNG8j_VlX-uQxM1u1fkbnrC0gd0aNoHxUcaylqdCQyI28m9xZ_dpRsfavDRjvUTSSkfxrmRtSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با هر رنگ شلوار جین، یه استایل متفاوت پاییزی داشته باش
🍂
🤎
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/695474" target="_blank">📅 14:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695473">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-GqayUn1G8MzXfAyzhClDDs6Uhxyp4z1zuUA5zL1oFcn3HRT9sDpbVIp4DbSr52pdCgs3OMvKgnG98qzrVl1YEZ0NR4X1aK_tjv4_u5WNV_MIFaTWvzxy1UutKbfQJR1QBQyrz4Kkri4ejaR_jSJ-8ClEBteqTXuErJowuVZNbO2ev1XCpuryg_QLTN2qFCwnlvvPBSQOsxsXIH5lfiMXdT4S9ygUSM2AbXaHKl5xCWLqHFNqidmxNwhqvhU-HvUEZVtsw8n2-dy-qKGVWkjEMVuWMphfW6QCpwoxaLLwuL7lnKL0jA9pChRIm_XiBMltcel1OsRohA_3MYX5ZXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس اتحادیه طلا یا سخنگوی بازار اجرت‌بگیرها؟
🔹
شفائی، رئیس اتحادیه تولیدکنندگان و صادرکنندگان طلا می‌گوید ورود افراد غیرمتخصص، «شأن آب‌شده‌فروشی» را زیر سؤال برده است. اما شاید مسئله چیز دیگری باشد: مردم دیگر حاضر نیستند برای خرید طلا، هزینه‌هایی بدهند که در سرمایه‌گذاری‌شان نقشی ندارد.
🔹
طلای آب‌شده، بدون اجرت ساخت، سال‌هاست انتخاب بخشی از مردم برای حفظ ارزش پول است و پلتفرم‌های آنلاین این انتخاب را ساده‌تر کرده‌اند. پس سؤال اصلی اینجاست: نکند آنچه «آسیب به شأن بازار» نامیده می‌شود، در واقع آسیب به یک مدل قدیمی درآمدی باشد؟
🔹
شفائی به‌جای اینکه توضیح دهد چرا مردم باید هزینه‌های اضافی بپردازند، از «شأن بازار» می‌گوید. سؤال ساده است: رئیس اتحادیه قرار است مدافع منافع مردم باشد یا مدافع مدلی از طلافروشی که با اجرت گرفتن معنا پیدا می‌کند؟
🔹
حالا باید پرسید: پشت این همه حمله به پلتفرم‌های آنلاین طلا، واقعاً دغدغه مردم و اعتبار بازار است یا دفاع از بازاری که مشتری‌اش را به‌تدریج از دست می‌دهد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/695473" target="_blank">📅 14:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا آمریکا ول‌کن تنگه هرمز نیست؟
🔹
فکر می‌کنید اگه تنگه هرمز دچار اختلال بشه، فقط قیمت نفت بالا میره؟ نه! اهمیت هرمز فقط به حجم بالای جریان انرژی محدود نمی‌‏شه، بلکه مشکل اصلی، اینه که مسیر جایگزین برای جبران کامل اختلال در تنگه هرمز وجود نداره.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/695472" target="_blank">📅 13:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-695470">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35225b91.mp4?token=drnja5I4kersWeWXWzJD93-xLzgni4eEJVdT5vE_a9WfU-GF2KCEqN_EPJDoYwUTKAzedr47A1nNXtl71AwoUX5qqkdTsCNf8JxYgQ3aNIKM7niKffdHhdxblhf0jfRTP1xlUgAFbeMKGpefQxxLCDfbD4wxmeKb5DnThA-3qwSaGNIVBjeMnHKvAOp9wlfRV_tq0tTz6vD0-AF2TsIIf4XDihtSdQWCbZJM6cOPAI3bLvxLvC-YjEKIYE92CuRcq9HEulyppnp1hD8UNvwiBGQmkG2UdlQg4XPGKyMU5OG2ESQRVOU4_N7STw-n8RpsBRJGKCQ7yt25FfR9aXnHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35225b91.mp4?token=drnja5I4kersWeWXWzJD93-xLzgni4eEJVdT5vE_a9WfU-GF2KCEqN_EPJDoYwUTKAzedr47A1nNXtl71AwoUX5qqkdTsCNf8JxYgQ3aNIKM7niKffdHhdxblhf0jfRTP1xlUgAFbeMKGpefQxxLCDfbD4wxmeKb5DnThA-3qwSaGNIVBjeMnHKvAOp9wlfRV_tq0tTz6vD0-AF2TsIIf4XDihtSdQWCbZJM6cOPAI3bLvxLvC-YjEKIYE92CuRcq9HEulyppnp1hD8UNvwiBGQmkG2UdlQg4XPGKyMU5OG2ESQRVOU4_N7STw-n8RpsBRJGKCQ7yt25FfR9aXnHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهین تسلیمی: تمام اتفاقاتی که داره میوفته بخاطر آخر الزمانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/695470" target="_blank">📅 13:48 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
