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
<img src="https://cdn4.telesco.pe/file/AJCefhYXToWNNMcUTX4-BZFWYG05D-yhWIvFaNvKEjMXKqM9u6ZCnfsA6OaRiXbAQ2ehSJGT8Ebo8G2wy4zHvxufNF8OPcASXW-xSh3MJ3Qtx854btHJhMRPePueI9TXdQVjG7-EC__1lSHsZllmrwxd-QpFxAQ1zD2C1PDknKKePxhcTJtyyB1OZ5d9YLjHfYtUQac0595w6IEN5XM8f8NsXeK7MgfUdtUYzWM7vu30iENRuMgOhSAY12v3tGfzulhUVd9A2FTzWMv7ctVSHFNVR-gLWYklFRioEndxWf17WBx1XQaj7mUIxtq-519XOp2IFRoS9AWrPFvE-Q15Yg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.58M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 11:49:06</div>
<hr>

<div class="tg-post" id="msg-658935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خشخاش به کمبود خورد؛ شقایق الیفرا بکارید!
حسین عبدلی، عضو کمیسیون بهداشت در
#گفتگو
با خبرفوری:
🔹
تولید قرص کدئین به دلیل مصرف بی‌رویه، قاچاق مواد کدئین‌دار و کاهش ساخت داروهای آلکالوئید دار در ایران، به علت کاهش کشفیات کمتر شده است.
🔹
میزان کشفیات خشخاش یک‌پنجم شده و میزان کشت در افغانستان بسیار کم شده و به‌جای کشت خشخاش می‌توان به شقایق الیفرا اشاره کرد که قابلیت جداسازی مواد مورفینی و سوء‌استفاده را ندارد و در کارگاه‌ها قابل جداسازی است.
🔹
تمام داروهای ایران، قابلیت قاچاق به همه کشورهای اطراف مثل عراق و افغانستان را دارند و داروهای ایرانی در آن‌جا ارزان هستند و آمپول‌های تزریقی که در بیمارستان‌ها استفاده می‌شود نیز کم شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/658935" target="_blank">📅 11:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658934">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40415b230d.mp4?token=DfyON8kgXOYmHVqybtrJF-p6zDd7UpF_iRCfi2nO0zIZXUj52CUJi7wQUTeyLGQGI5EPxworR8Ov9yCc9Hm4tGsDn6HLsr1BtGhShENP1ELkm7dUAr5p_yNtz_FMq6te-s0jr3n0Gd5QLrSoCx3Bzt5dAWsWeH1TO7jLf4M8AX-IfhBUDn43eRIJw8Ch5AMrfB2ht--4J53ot6FGXphk5KxWLWbv6pCUfgy3Lf6SIV8abbk3_ytpUdKBLzO_daS5ipw1XoUX-LYhQMGeSe52bRN56MuqX6gOllwiqreVj4Z8W37sgBhdwBQTlJW3R0r7EcBdexPyylIw7BdmnLVQQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40415b230d.mp4?token=DfyON8kgXOYmHVqybtrJF-p6zDd7UpF_iRCfi2nO0zIZXUj52CUJi7wQUTeyLGQGI5EPxworR8Ov9yCc9Hm4tGsDn6HLsr1BtGhShENP1ELkm7dUAr5p_yNtz_FMq6te-s0jr3n0Gd5QLrSoCx3Bzt5dAWsWeH1TO7jLf4M8AX-IfhBUDn43eRIJw8Ch5AMrfB2ht--4J53ot6FGXphk5KxWLWbv6pCUfgy3Lf6SIV8abbk3_ytpUdKBLzO_daS5ipw1XoUX-LYhQMGeSe52bRN56MuqX6gOllwiqreVj4Z8W37sgBhdwBQTlJW3R0r7EcBdexPyylIw7BdmnLVQQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وسط اتوبان حکیم تهران، پیاده موبایل یه نفرو دزدیدن
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/658934" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f507d88efd.mp4?token=bz6GcR89fnlcv0JxPZdu0ziCzvh8XYKbzh9yMbVgqHlklsWmApnWRiISNygyOWXJ5uII61KAMKqz9KHVQ_rVjlxew9A1bsMlM3EJ6bWsqP-0lNq_pz7w-Pwf5y2eQ5Fcj_pNd_SaE8WpmLLhTPk5tjatFhJHEky2zzM_AjK6fF5I9wIcA6ZMDgsahhGb6btsrymdnKcZ8U4tjiAppqYZBGr6ASxseH9gMR3xMpPEvnuO77hbTWn-64OkwHT7uHH8Aq0c37Njpl510QhihMRV222KJOSoinl2xJOxM3DyWatPIE-DvcgvrGJ8I9WH-rzB4Jb355ELhxMh2NRa8JR4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f507d88efd.mp4?token=bz6GcR89fnlcv0JxPZdu0ziCzvh8XYKbzh9yMbVgqHlklsWmApnWRiISNygyOWXJ5uII61KAMKqz9KHVQ_rVjlxew9A1bsMlM3EJ6bWsqP-0lNq_pz7w-Pwf5y2eQ5Fcj_pNd_SaE8WpmLLhTPk5tjatFhJHEky2zzM_AjK6fF5I9wIcA6ZMDgsahhGb6btsrymdnKcZ8U4tjiAppqYZBGr6ASxseH9gMR3xMpPEvnuO77hbTWn-64OkwHT7uHH8Aq0c37Njpl510QhihMRV222KJOSoinl2xJOxM3DyWatPIE-DvcgvrGJ8I9WH-rzB4Jb355ELhxMh2NRa8JR4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهرمانان جام جهانی فوتبال ۲۰۲۶ دانش آموزان مدرسه میناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/658933" target="_blank">📅 11:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b84ce7570.mp4?token=Lc8yfC6-X0BpZ61aVrMEbKeea-Cy7rSOfwvwLHiioxYZxM3RsCgOOJihZReFH7dT-iNKiH30mFCsA-nnRHzzfFvxBA_9foNGxPP8Gw1ZL1eFPR3Fng0O3C8u_wYJSVVZb4kE7iwMDzB_bkkzQvytHY84VcjM7ttCCeYCxsJnt3m9Xs8EpPEVbL37JdAu_ax4VQCZ6wtGqAGxqN51I69YWVXERI0Gxryf4WNbpagc51EgOrctmVDEM3kW7u0HlTC7vahscgCZQClpiteOxjN9NzUe0FITxmcCjIEv59iBOY8Hw4MYjv2uFJm2I0Yp7Em7gGX6cU3MY1CJf5_dJdlY3E7YfPSsVuA1htH5MtgmL_WZ-blvUrEuTdEd2HIuYvhBAOTgL_4pJbzQjowOVtBpqOIFR3HPDItX3NGBHA_WclaIpUBEkCBh_K7CjYdXs5YzKsOCrO_Vq2wTCY1sDaedX_n1YWJathko81XPE2H6p6Ty5PlWVBru5pcb1QDo32u4gHqO4N-ZqMvJQ-33OKtNUgIuDBJTLdkj7yuf_SNqN3J2GbU71aDTCJkYZn8zKyfGXIBv1Hu8GH99spJqxEUU1q2nSQPvJB2885dCvY9MIM92j-iQBz9aujKJ6PpXJCtvZmNX69lby_Z6DMLL1dDp5wzOw3W-niCeVeLHdCPMSaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b84ce7570.mp4?token=Lc8yfC6-X0BpZ61aVrMEbKeea-Cy7rSOfwvwLHiioxYZxM3RsCgOOJihZReFH7dT-iNKiH30mFCsA-nnRHzzfFvxBA_9foNGxPP8Gw1ZL1eFPR3Fng0O3C8u_wYJSVVZb4kE7iwMDzB_bkkzQvytHY84VcjM7ttCCeYCxsJnt3m9Xs8EpPEVbL37JdAu_ax4VQCZ6wtGqAGxqN51I69YWVXERI0Gxryf4WNbpagc51EgOrctmVDEM3kW7u0HlTC7vahscgCZQClpiteOxjN9NzUe0FITxmcCjIEv59iBOY8Hw4MYjv2uFJm2I0Yp7Em7gGX6cU3MY1CJf5_dJdlY3E7YfPSsVuA1htH5MtgmL_WZ-blvUrEuTdEd2HIuYvhBAOTgL_4pJbzQjowOVtBpqOIFR3HPDItX3NGBHA_WclaIpUBEkCBh_K7CjYdXs5YzKsOCrO_Vq2wTCY1sDaedX_n1YWJathko81XPE2H6p6Ty5PlWVBru5pcb1QDo32u4gHqO4N-ZqMvJQ-33OKtNUgIuDBJTLdkj7yuf_SNqN3J2GbU71aDTCJkYZn8zKyfGXIBv1Hu8GH99spJqxEUU1q2nSQPvJB2885dCvY9MIM92j-iQBz9aujKJ6PpXJCtvZmNX69lby_Z6DMLL1dDp5wzOw3W-niCeVeLHdCPMSaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تب فوتبال با جام جهانی/ از برد قاطع آمریکا تا اولین امتیاز تاریخ کانادا!
🔹
طرح
طلای
بیمه زندگی
پارسیان
▪️
آینده‌ای طلایی با سود طلایی
▪️
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/658932" target="_blank">📅 11:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCq_yzyd81eVR57ayjgk-kgJCcDsYw-TvoJPzRuqShhdEXkK3_ih78sj81YgT_fba-3Mqy7WWS5LcnYnPUc35JEKCXx6OMDpy6DFG8VaHOWIc_KD43e8-YOBKkawu9weu_aDKEXzbRqyH6HuGwmlYUlDy4bRN9lw1dFkSgzV0nfhhOnAZKtG2Y7LRw8QOtjoKXKymthBKk7j-HDbwJGM8sSuPJHPaZslq-ICCwsEzEZtQciOwQf-GelalOxgYHqIoPT1lxxAVCFVf65PWZb4s4Btj_2fCReieNG6dwrnjqozwPAYMnKn4m3tLPDTEzrnwNq2nTRpcpr29C5sAkp7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اژه‌ای: به آمریکایی‌ها مطلقاً اعتماد نداریم
رئیس قوه قضاییه:
🔹
همگان بدانند؛ ما به آمریکایی‌ها، مطلقاً اعتمادی نداریم و این بی‌اعتمادی از حقایق و وقایع تاریخی سرچشمه می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/658931" target="_blank">📅 11:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed82a8cdb.mp4?token=FKje7jrOkuv7QVbiJOY2MF7L9tKf9LKK5nZEpaCDSpzOfNWXrFLTirw6Y-2Jo6LEqk-ZhDb1lfpZKK8xoZnZpX4s7qD4WaU5RDc-fwNrT1GJDVyTZ65aWGnrR7zNdRFJIFoWMxvwlLiD_9GU_hwfNMlH9TLcbIKD_UoCBJQFzIho-YPf9_iGIJqvU1H_MeSDcllQJEvwadn4aZR5nz5C9GowsdhdTMrZJlarOCVnFHLy36eT-LorM_i5zzTo9Tnh4j5gij2tJOr-92-SLO4OB4-reIOhUg4SgmhmLlxZaWDXCp-UQpioQwaRC5xX6nFZpEBTQBlPCqv1D80u1XSQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed82a8cdb.mp4?token=FKje7jrOkuv7QVbiJOY2MF7L9tKf9LKK5nZEpaCDSpzOfNWXrFLTirw6Y-2Jo6LEqk-ZhDb1lfpZKK8xoZnZpX4s7qD4WaU5RDc-fwNrT1GJDVyTZ65aWGnrR7zNdRFJIFoWMxvwlLiD_9GU_hwfNMlH9TLcbIKD_UoCBJQFzIho-YPf9_iGIJqvU1H_MeSDcllQJEvwadn4aZR5nz5C9GowsdhdTMrZJlarOCVnFHLy36eT-LorM_i5zzTo9Tnh4j5gij2tJOr-92-SLO4OB4-reIOhUg4SgmhmLlxZaWDXCp-UQpioQwaRC5xX6nFZpEBTQBlPCqv1D80u1XSQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس رونالدو و یارانش در آمریکا
🔹
تیم ملی پرتغال وارد خاک آمریکا شد. #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/658930" target="_blank">📅 11:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWFppUqSQlNDtIXuPomFT05BX6X4TEoXT1qLTm7qN_O1mcqnSoOc9nI9XKGgb6gA0GO3ZdQe-sD9L7LxOLjXszFpf_1tZAQ5fOUL0CLz2guXRYXTud-4wW7ZY9fo5EJMywuPMsg9NoPHx5ZwNJc9Jf_3vkU3sKgJgisN2uVqvR51kkkBJgvguLkIG_G67aAI5IZu_Fbkqz-USuCieOfVMlaTSx7eTm8feYjPh4nw2vKd5vEYIfutddd47KfqOn60zTh42U4vAdPf2xD6D8isqBpcU8AZJl6efzgYC8rwT7Ogsif4Q6m3eTK7CzPVUMTZmVct1Bjp5MwHgPtPC11UzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از کارت بازی داور برزیلی در افتتاحیه جام جهانی، این تصویر عجیب هم ثبت شد!
🔹
البته جدا از خشونت جام ۲۳ تا الان، کیفیت لباس‌ها زیر سوال رفت و ضربه اقتصادی عجیبی هم به کمپانی «پوما» وارد خواهد شد! #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/akhbarefori/658929" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odHtLbIbN0uAH83TOFe7mOsYJy89aa6MLZ7jjlYtiM8fyinGh8VgAwygmdgwaH_6pC0PjPjEKI6eHDpcjMm_5QVXmoRUJIiM-1qo815jGDx5eEZD8Gs9fw7Yhq0kZj_7efMBGdBxvMUhU7RrsNs3BnUtKd1t61YM9Ppa9kDkxXUCShdY1KjX890Amm7BNIUsuv2Rpl-cq7-JJuRx5gFRZyshe7lfbV2GWruyHdWe8tXP6JhqDyzJRnA0PtnoqhDToUaMTfaVml1zvg2jAAIJDepfdxPY_WcIjRZTpb7yElylCk68o_pNJ2aRZHSrhr-ibHXYpz0VSMGEDZslcJ6bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات ادعایی فاکس‌نیوز از توافق مدنظر ترامپ با ایران
ادعای فاکس‌نیوز:
🔹
طرح پیشنهادی دونالد ترامپ، شامل پنج بند کلیدی است:
۱. نابودی و حذف کامل مواد هسته‌ای ایران
۲. برچیده شدن برنامه هسته‌ای
۳. عدم آزادسازی هیچ دارایی ایران پیش از اجرای کامل تعهدات
۴. بازگشایی تنگه هرمز
۵. توقف تأمین مالی گروه‌های نیابتی از سوی ایران
🔹
این ادعا در حالی منتشر می‌شود که هنوز واکنش رسمی از سوی مقامات ایرانی به این مفاد اعلام نشده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/akhbarefori/658928" target="_blank">📅 11:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658927">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Deo9W7AUg8Q3ws-6AmK_kxlcup08m2JQihmDmnAfqWouiN6vVJp_KFX8nu5n_LJbTOOcvpSYBH_dOkOuRnSKbzWyP7A40_I_MX6G_E0HGlePICQxSOK3bMCfanZTXXY6MW18-sRt6x7SQT_uYQjgakF_JP0oSoOvVgkaw8oIaxmhygpn9GxQ1FKh1TMrXXsqSQhg48EfwDVobXOqbb41PlUIP6fCG6Wqa8Dwmg65wfSvhey--dkyIqOfkz1JqW5EF76R0Piwf2iME4SlEHPvrip_-u9a-W6XtaEkiYtkXB-UVYXCt7U-cdDfRSKVSps2uXihFkddDGRCvNtXaIw00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از بلندکردن شتر ۲۰۰ کیلویی در ترکستان قزاقستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/658927" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658926">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شرکت توانیر:
برق مشترکان اداری، تجاری و خانگی پرمصرف بدون تشریفات قطع می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/658926" target="_blank">📅 11:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658925">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHBCzcKIoH-GKmZ2HySEhP-NQstwb7IKDY9Af9ZnWLJdmK6hdjd8iOv_JgmnQ1ax-6F7QszoqyRqJNlgZAaB0bmqUdgm9F6cxcIUeMw_exq6hyEMeAYIlllZn8Hjf5JJvCaNy9mTb0YFTC8KLHBj74PRtxCDs9Uj8eq5LEGOhk-ZVQTvi-bTu0jFllr40Jt0NoEjWXL74n0Hhr43Pq1YEwbHS_37NDdbnFW6mgLUpoidoI5aghq9lyH3F56UP1iyAUnuUnhaohWwvgW0jYnTiyebbw4i6TyBKqjq__qie-_AJEQ7zARSVeINSpzLH4UVpNaz2PMQ_qamoaus1MMJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سبز ۱۰۰ درصدی؛ طوفان بی‌سابقه در بورس تهران!
🔹
آخرین هفته خرداد در بورس، با یک انفجار خرید آغاز شد.
🔹
پیش‌گشایش بورس تهران با صفوف خرید بیش از ۵۰ همتی رکورد زد. نیمه اول معاملات تمام شد و بازار کاملا سبزپوش است.
🔹
خریداران در ۸۱۴ نماد، صفوفی ۴۸ همتی به جای گذاشته‌اند.
🔹
شاخص کل ۲.۶٪ رشد کرد و به ارتفاع تاریخی ۴ میلیون و ۷۱۲ هزار واحد رسید.
🔹
ورود ۳.۶ همت نقدینگی حقیقی‌ها، ارزش معاملات خرد ۶.۳ همتی و خروج ۳.۷ همت از صندوقهای درآمد ثابت همه در نیمه اول امروز بورس رقم خورد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/658925" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658924">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWQeOnFGODsfa9oirw-qlrk8OYdExl1PXgaAqkzVAHLZfESDOrXIjN97ANb4_lT_dR9mrNHROA9qRZ3_3mU54GRnzfp1KTr-R3reUZCaqtvioJvm1FDILeri_aiLBEcs9k1q_IR7zxWjXXrgI60Y2UzMZQVx_j-PG4RUn_hEhzdk1F0LZW7BS5Di2LsHMn-7VxWjBti7wV_6jmId_hyqh99rQyJWo-1YFZDWFNYv-IDbNxkz-B4F-lS2RjTEGLNOT4zhRhj7Ug6m3QzZyCyKF1qOzVn4nSuJeUsS92ZnXhXg9aQ4gLIuVXLGs8ftY9ByVleYnXBt4GkTbrllWX5itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا ترامپ امضای توافق با ایران را به معاونش ونس واگذار کرده و خودش پای مسابقه یو اف سی می‌نشیند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/658924" target="_blank">📅 11:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658923">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یک منبع لبنانی: دور پنجم مذاکرات لبنان و رژیم صهیونیستی با حضور مقامات نظامی در واشنگتن از اول تیرماه آغاز می‌شود
🔹
سخنگوی قوه قضائیه از عفو ۱۳۹ محکوم به اعدام با موافقت رهبر انقلاب خبر داد.
🔹
فرمانداری دزفول: صدای انفجارات ظهر مربوط به امحای کنترل‌شده مهمات است، جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/658923" target="_blank">📅 11:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658922">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nad_qrnx1nK82VZSTa12SYsSi5SBxT8qcFBX6Fm0jBgGTkrALyXFsPIrPx4i8E_NfqO2uGtSJUb117QSjsjeX897107Tve7fT44zM7q3O1Cr9q1tId2NpMW87wKtlylveu3MXc4aH3GspyVCW_R5Xwt8QkrTOdYt-t0k3vfLAV58kJLXRudhfyLnpv2G0bghFy7ueq7SD0sI49Qk4FmEkh1Gh7ugM4hYq4dl-cbcCNWXaYP_UoRRorkQinjloCkukgwNi4x67adyM8doPLUyQE96jNIkb2mOHaLIfq2fq8YJD1qwFrXxZv-sY9-_yKJl_qO4YhJKzjrwx8NVOYq_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/658922" target="_blank">📅 11:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658921">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoLKCehOJ0thYfaEE-dUBHBWwH0NcMRhZl9ivjqESTqSDqLi21d7mIMpSoIM_kEh1gp4-K4l8tDtvovD_eBhZysIISxe3ta8wE1tIMb-qD4fdNt_dvBwCQ7kaoukkkKlwR1eOWZTMQ2FmfV6HDws36n3_vYDg2fpO5zwiOjeULMOogaC0Wyw5QwuwVsVHOeTrzfoD2niSyM4yGIUt3iAWQx8oqMFxdT7L456qm1GnBzbv3tOkbOt8wFjzukExw3OVKyiMVWEMJH8ZybDohIHemSYJh9p2LE60ILj78_ehwZ89GPieW_9dgOZ67MWN7TIH0qIPGfpWZtNieFjVhBguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر عبداللهی: دنیا به زودی طنین پیروزی ایران را خواهد شنید
فرمانده قرارگاه مرکزی خاتم الانبیا(ص):
🔹
به فضل الهی جهانیان به زودی طنین پیروزی ایران و ایرانی و غلبه مقاومت بر دشمن متجاوز و تروریست در دنیا را خواهد شنید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/658921" target="_blank">📅 10:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90c9c606d.mp4?token=RcdJxydBCJi6AHP0XCurnxZd_6ajvggnVHupW_XVw9f6RCCKjFG51V49MvBq0AcjEIRLSpitZwHRCZYuFeZGAoGwaPFxLJetYWuzshwwii-Iqzaq5h_mU-FD1b_ZJd4y_V-bS0uwYzXle6ASAnZ6c409-3eHF6juKCKzcYd1noDpaa6NTAHbXhCkvKdlw9khGJdcx3YH18WweyJHNtuiJs30NsprRY56CEiPCfEHABClY6w3Sx1XE6RDDafXOb1lhT4HgKskr70An2IHrpMcouU0XHYTe7WZmydBrFL8iY1sr5hs7mU-zHaCUFLNiVHzWIoCSSDveW4U2qGD3fJmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90c9c606d.mp4?token=RcdJxydBCJi6AHP0XCurnxZd_6ajvggnVHupW_XVw9f6RCCKjFG51V49MvBq0AcjEIRLSpitZwHRCZYuFeZGAoGwaPFxLJetYWuzshwwii-Iqzaq5h_mU-FD1b_ZJd4y_V-bS0uwYzXle6ASAnZ6c409-3eHF6juKCKzcYd1noDpaa6NTAHbXhCkvKdlw9khGJdcx3YH18WweyJHNtuiJs30NsprRY56CEiPCfEHABClY6w3Sx1XE6RDDafXOb1lhT4HgKskr70An2IHrpMcouU0XHYTe7WZmydBrFL8iY1sr5hs7mU-zHaCUFLNiVHzWIoCSSDveW4U2qGD3fJmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط هواپیمای نظامی هند در آسام
🔹
یک فروند هواپیمای ترابری AN-۳۲ نیروی هوایی هند هنگام فرود در پایگاه هوایی جورهات در ایالت آسام دچار سانحه شد و بلافاصله پس از برخورد با زمین آتش گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/658920" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21a7ca6c94.mp4?token=ATIcLYakITgpXZjr7qaGr_0300dge-vT_XFXlOsRqp1hBRuBfwMluGHlgmmYTl7zkhhKU5uJwfFGdsA6iLTMliC0E1FK7R51cF5b58ssscgUxEy8pD8tZUr5tnY8ovDNND13E9-q4WWM2qcX8E_DuX6dcpUGKVu9qO_hEW6X2ibM1lARjsBmGQw7zQNYeYPh7yZ1L35Kj93eN04jEpjVSnEPi6i6e_mO-qmV9lXOtJsAuk3MRtaTSBiE3xYs9e3T5V3nv607FExYoPGC7qgzCHNLTyRBq4uXeuyJaw_8X94RQfwsVfXAM5iua3gDnaFtlqa98-yZpwK9S21mAXiMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21a7ca6c94.mp4?token=ATIcLYakITgpXZjr7qaGr_0300dge-vT_XFXlOsRqp1hBRuBfwMluGHlgmmYTl7zkhhKU5uJwfFGdsA6iLTMliC0E1FK7R51cF5b58ssscgUxEy8pD8tZUr5tnY8ovDNND13E9-q4WWM2qcX8E_DuX6dcpUGKVu9qO_hEW6X2ibM1lARjsBmGQw7zQNYeYPh7yZ1L35Kj93eN04jEpjVSnEPi6i6e_mO-qmV9lXOtJsAuk3MRtaTSBiE3xYs9e3T5V3nv607FExYoPGC7qgzCHNLTyRBq4uXeuyJaw_8X94RQfwsVfXAM5iua3gDnaFtlqa98-yZpwK9S21mAXiMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متفاوت‌ترین هوادار روز اول رقابت‌های جام ۲۰۲۶
🔹
پس از پیروزی مکزیک مقابل آفریقای جنوبی، یک اردک با پیراهن این تیم در حال راه رفتن بین هواداران دیده شد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/658919" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
قوه قضائیه: به‌دنبال جلوگیری از فشار بر مستأجران هستیم
سخنگوی قوه قضائیه:
🔹
مالکان از افزایش اجاره‌بهای فراتر از توان مستأجران خودداری کنند.
🔹
برای قراردادهای بلندمدت، مشوق‌ها و معافیت‌های مالیاتی در نظر گرفته شده و دولت ممکن است برای کنترل بازار اجاره، سقف افزایش اجاره‌بها تعیین کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/658918" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQOVi2jgUmfKNHw7GkeQUucI7Lx9oDCWXS41ND2D-9Hs-S2Rhy850V5IU7IHcXetWiMx9dgGYvrxSLziY3u5_BtO1aA0H00zhEqMOaIjHhztk1YJpNpWgcpmDO-WIZswlArkKSi_zoB4s6T_fho6Y8ZYlgr3xo3RsNAtsyfa7XjuFURtO40bWgzpM5kGylPO1jZKAn-0TR5e7ge5lHpuJCxgzCszYZlglwQxMb5JHQTvzNDEHwVFVTXrcv707Okup7d-QnSZBWnepbR60PJ3vScflohW1AjZKYhcVxOxY4i7und-X-qWchBMPNcUY2jy733UglIMXC1MjBItvHWyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ مدل سالاد خوشمزه که وزنت رو هم متعادل می‌کنه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/658917" target="_blank">📅 10:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
فروش اینترنتی دارو غیرقانونی است/ با متخلفان برخورد قاطع می‌شود
سرپرست دفتر بازرسی سازمان غذا و دارو:
🔹
تاکنون به هیچ پلتفرم یا وب‌سایت عمومی مجوز فروش آنلاین دارو داده نشده است.
🔹
هرگونه عرضه دارو و مکمل در فضای مجازی خارج از زنجیره رسمی داروخانه‌ها، قاچاق محسوب می‌شود./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/658916" target="_blank">📅 10:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7746c19bf5.mp4?token=ple3yIOFJ8D3cMbXecwVa_-ktiX7DUBFY3yWEfGwYfoIe8i7Nx85FHDZfXnC9rbHWHhKLsSIWF_A5RHM9HygJ0rsNKgndTdgR03dXfo5xyMf5tHGUtD7idQsjuiNKkNbLSMSru0Gq34bD4cx1qpp8pa2baA9LOdkTmSNzOEFz9RnV06sCNDyI0iaUywlIOjycV8Z2EowwW8H6H8m5lOLFNpNXqfBfn-WChWDl01XcQiB_bzbjq9uZbZP8JVJuGH3HYe-x4rn2w6dskqDvgV6H8XjdovU-aX9Yh3Y2hLx18gLVX8qq7xtLltYhh-P4C8ndDols_bM5Di-4eZEOBWTgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7746c19bf5.mp4?token=ple3yIOFJ8D3cMbXecwVa_-ktiX7DUBFY3yWEfGwYfoIe8i7Nx85FHDZfXnC9rbHWHhKLsSIWF_A5RHM9HygJ0rsNKgndTdgR03dXfo5xyMf5tHGUtD7idQsjuiNKkNbLSMSru0Gq34bD4cx1qpp8pa2baA9LOdkTmSNzOEFz9RnV06sCNDyI0iaUywlIOjycV8Z2EowwW8H6H8m5lOLFNpNXqfBfn-WChWDl01XcQiB_bzbjq9uZbZP8JVJuGH3HYe-x4rn2w6dskqDvgV6H8XjdovU-aX9Yh3Y2hLx18gLVX8qq7xtLltYhh-P4C8ndDols_bM5Di-4eZEOBWTgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم ایران در قلب لس‌آنجلس
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/658915" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658914">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره تله‌‌گذاری ایران برای حفاظت از ذخایر اورانیوم
سی‌ان‌ان:
🔹
ایران در هفته‌های اخیر به شکل چشمگیری تلاش‌هایش برای مسدود کردن دسترسی به ذخایر اورانیوم غنای بالای خود را افزایش داده، از جمله با فروریختن عمدی تونل‌ها و تله‌گذاری ورودی‌ها با مین‌های انفجاری.
🔹
دسترسی به حدود نیم تن اورانیوم با غنای بالای ایران اکنون بسیار دشوارتر، خطرناک‌تر و زمان‌برتر از یک ماه پیش شده است؛ زمانی که ترامپ علناً احتمال عملیات برای تصرف این مواد را مطرح می‌کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/658914" target="_blank">📅 10:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658910">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZgG-EutC0Wd_9r43V1X522HrUrvPD6Dn6ciD0xEaCeuPyAFuuxamXQgx5SZ6IP5jGhEo8xyRVXVE4gkbMDJt3l8qvof7an0Xj_CywSlWBBk2MlK52_FGw2voZ3vcCeMP4RkRfokzmaq8zsO8B-7aiqgWjbFNoY44bgqYTF3T5Es6vVj9AvBuEobCGSSUPz4_P9LC3UTnbA5nSm28CRYasgSkl4C5A4cRH-504HNlITag5lmIgzc22EszKq-amSYX1RQ8j9gprhLQ8JETClCZokwJpX_zBFcWa8P0T2_hCIAERFdhktuuUc_x1kg9ROmwRMQ8K97xH61jQN8sJm-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L0qcnLs75kP4M018zhr3elxbXIl4K2A7HdcuejLKzOZMjpE4KAU6nZc2hkAgGB7gwal-6K5P8BkSN005ytjAzrnoOtV2DINekgXMYYY1Nryjee3xfwZtqr9ZU1-P48XqlKbXNU-nci2n5Yk0yynKm_QbYXMuCcbWAGpQdbOGvSrmdkFm4znt8o3LAdhXR0Lfr2hD6a3eWFTzzqi9PAOc2Pe5I-W8y7roZokaG8pD4psWVmYqmw7Fw0DACr5U3R62UBrt42geF6oG8Qq4NeiJoZl5lXqI1EkOMIunuOVU2rPtIa0obL3Eq6pttFYg2vHe7l-MyRE_G2qbvtffK-XJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sieg7m12HIxaAPLYlc3csqY6romn5LHxmyvTpCxYf7ikio-bbQORhJAU5R5z2uYqYg04ROeQWgR-A2iYZCgByGhIaI0OKI4mLRbyQLN0GcNLxBuRCT2PrVYCdScCET2kfdTEsKp3nLCdiKTd0SiuHOaUE01v6HOg2WQ-WSsBzuFdUG7FZi0x7ZqmKg406k4HEYrhNEyxc4mw0PPo1pzPLGDOO0DrYmTzA9Iwx2goeihuXOJjmNW-FgIBBWn22cGJjYykZmx5MSh56janMIoK-My5mMNxmS4yniiFBVqJYrZRvgTBb5v5VFBO3jRbNimj4aBE9b3-GTutzFUWMwVv7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrIHhAKdS-I9f3bNfeRcQDjDGahUyL9ceWLPglUGQW-IXrxNakrwLc1oZhEnWGMbhBCOekFmqadyobiC-0cqA679qwFse4wCTQ0uAkU7SLG2hETdn3R42b5Atcw1FWB9wPDHsG9QPEXigaGB0UimRaMMyF_kco4hUzMFm5lQcSv7vpcdUtS_LoYNKDcHCSh31QuvVSFbPKDa0JihSMxqNdugRH4-LcMPY13hyCZ-UeogodglzZtczeUr-x_rI-61FJP4E-ope-OUibyj7B_LwuBW56ICLKbywyXNXEJPFxzzBIxv09LRPWf9RZMGGcyX8lqKHL1BNToSN5CVQuQA1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری دیدنی از لحظه وقوع صاعقه در اسفراین
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/658910" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658909">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
رژیم صهیونیستی برای ۲۰ شهر و روستا در جنوب لبنان هشدار تخلیه فوری صادر کرد
🔹
سخنگوی عربی ارتش صهیونیستی از ساکنان ۲۰ منطقه جنوب لبنان خواست فوراً محل سکونت خود را ترک و به شمال رودخانه الزهرانی نقل مکان کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/658909" target="_blank">📅 10:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658908">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b667de7ddc.mp4?token=VTG6voryPCegh6GCQ5zzCdRt-pCddBKCcK1x8b0iVMXQR_mKKrO6qVqg9dUhvcNx6mLpsgINri4sejV8wWETQa9OI74WV-wr19R9MM40um1VeUrKuPIUyke04Ox1jh-Ki2oFGC9m8-krsHsYNC_Bkl4YS56WOJqWWwJ5z_7fl748WI68Obo8_li9BmIuZveXvgYviIgZ4wV8MPO5tc1kvsV-AK_NFXVOUNHTlfnrQb8xuDJ87j7OTclMyYe0P-F2Ly84DhsWaasCVYweiBA8iCEtJCwVsmGEs1TxN3RHQYF-xMRhEgNcStO55-F1EsN-dU5h8gv4adBwCDB7wpZhGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b667de7ddc.mp4?token=VTG6voryPCegh6GCQ5zzCdRt-pCddBKCcK1x8b0iVMXQR_mKKrO6qVqg9dUhvcNx6mLpsgINri4sejV8wWETQa9OI74WV-wr19R9MM40um1VeUrKuPIUyke04Ox1jh-Ki2oFGC9m8-krsHsYNC_Bkl4YS56WOJqWWwJ5z_7fl748WI68Obo8_li9BmIuZveXvgYviIgZ4wV8MPO5tc1kvsV-AK_NFXVOUNHTlfnrQb8xuDJ87j7OTclMyYe0P-F2Ly84DhsWaasCVYweiBA8iCEtJCwVsmGEs1TxN3RHQYF-xMRhEgNcStO55-F1EsN-dU5h8gv4adBwCDB7wpZhGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر میخوای واقعا خودت رو شفا بدی، باید اول چهار نفر رو ببخشی
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/658908" target="_blank">📅 10:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658907">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ptk0iEVjs3Gcy4hf-UVIkopDqZ5buylE3bE0VVWD83GzLiIJapOTH30vnJYPgy2IveBUiRdwF3FTzeeGEvQDnPdvz3bhcPn8GE6hXxRtgwYArXsDN8YrLGiTaZYJhrwKvDB4_0rvh8Sp_dJZ6VvmU4eSgpkXavCv01opruiDHnsNnZX709Vr_ymjkhD9J79bdpLvaiKwaCFde4dMBFKJzUREpFauxRbxH1cr_lErAI7A8fvKGEFe2DKFshxkFxxBZVgpkR5aUJHHRIZjIq2esaOldowIsWI5zT4o-ZmOGqG6eYJ-zdyzIGP2IkPGXmcQY5auZ2T1KgQhzkv_EE71EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نویسنده و تحلیلگر ژئوپلیتیک پرتغالی: این جنگ با ویتنام، افغانستان یا عراق فرق دارد. آن‌ها برای آمریکا شکست‌ سیاسی بودند، نه شکست‌ نظامی. اما ایران یک شکست نظامی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/658907" target="_blank">📅 09:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658906">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
مقام امنیتی عراقی از تحرکات مخفیانه حزب بعث در استان بصره خبر داد
المعلومه:
🔹
یک مقام امنیتی عراقی از تحرکات گسترده و مخفیانه حزب بعث منحل شده در جنوب عراق پرده برداشت؛ تحرکاتی برای سازماندهی مجدد فعالیت این حزب از طریق جلسات منظم در مناطق مختلف استان بصره در جریان است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/658906" target="_blank">📅 09:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658905">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a75dcaad.mp4?token=q9ZQjEYjhKSshSQ4fSukLCixUHjzuvIGxmtshbSyUt5oOZOm_M15sjuMgb6JWihBPB1DiIS5E-0pBDGE3WX-rpxbp2FFgJUKkdw8xa2LU6nk_n_3QobhxKP4IIlrqMhNuJDuKVsf6Y-xC6qgizVR_Ph8u9bmb2gcThRlKEcp-Hj_DTsR_45X9U7TsW5M34LJLy2w9vd-HcHopqy8OVkp-JUjavI6yLbnrkzpw13JBRwDD7_6DMNlB34ZofNsDMycCO1twHTozSbvRoR47pTOq6ARgzVMnudb9T-thgUByc4HTFaTpF1RdCJlbrns6ia7kDYkRijRtkPSWfvwr5PebTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a75dcaad.mp4?token=q9ZQjEYjhKSshSQ4fSukLCixUHjzuvIGxmtshbSyUt5oOZOm_M15sjuMgb6JWihBPB1DiIS5E-0pBDGE3WX-rpxbp2FFgJUKkdw8xa2LU6nk_n_3QobhxKP4IIlrqMhNuJDuKVsf6Y-xC6qgizVR_Ph8u9bmb2gcThRlKEcp-Hj_DTsR_45X9U7TsW5M34LJLy2w9vd-HcHopqy8OVkp-JUjavI6yLbnrkzpw13JBRwDD7_6DMNlB34ZofNsDMycCO1twHTozSbvRoR47pTOq6ARgzVMnudb9T-thgUByc4HTFaTpF1RdCJlbrns6ia7kDYkRijRtkPSWfvwr5PebTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حضور یک فیل، نماد حزب جمهوری‌خواه آمریکا، در کنوانسیون این حزب در ایالت تگزاس جنجالی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/658905" target="_blank">📅 09:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658904">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0GY4c1uqrjPKDOyJxGtoltSAVeXVJEUl8Qluhj6zPGUQw0V2JCcUSXxCOjhTVAPjGaPaXo-vYN_kNuqjf_4RePU2zOSbtwOWHicHoUeDY-zmXfDajF96D_yGrh_5L1nVkKpKJc5XY7YJr3112E7c3epIWIO-SYQsoB-9f6z2gv-QbQQ86fR5Ef_OV0Cb70qDNrGOVLyONENZByCUaif2h60kfuESxBnInoVPnraXz97msILEwOpM-kd2Y3ih660a9PykCWv3LAZuuJ4NUacgUoDz6TDmm2dfER0rAWs5IbbeSPoJUU_NQbTjvS6t9yLnx42hyMY8TkXIFCan5dCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۹۶ هزار واحدی شاخص بورس در چند دقیقه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/658904" target="_blank">📅 09:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658903">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
روزنامه
رژیم صهیونسیتی: احتمالا توافق تهران-واشنگتن شامل آتش‌بس در لبنان هم باشد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/658903" target="_blank">📅 09:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658902">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c311e352e.mp4?token=BIVjKhjXzpt4riP62nKSA15CgVKohMjIvlia9Xt452lvVa6cDEKHQQ1kN86tgfyy4gIshqHbjfyN4YKTq7hNjYhpKORVmI8T168oSSy91m8IP2GO9t-eAwwJANxUfZtpQVBXJoRtcXcQmcXyNNc576TbtyJCmBEZmDJ5oPX-XD76RrvBkLaRGeJGcXLRSKuQV0SxsQEMlFw3ywJZt68ZdfrWgsfnid7ASLm6g2BoPX1j8-kh2-u4PIaNFMFGwFkhtqi15vw5edYcKIWYigz_OpAu1zBgo1PCMi8bJ93-B6hGOngSQSojVL-pQ1OF3xm8JGxPz8Nm8JqEd6zE86fq6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c311e352e.mp4?token=BIVjKhjXzpt4riP62nKSA15CgVKohMjIvlia9Xt452lvVa6cDEKHQQ1kN86tgfyy4gIshqHbjfyN4YKTq7hNjYhpKORVmI8T168oSSy91m8IP2GO9t-eAwwJANxUfZtpQVBXJoRtcXcQmcXyNNc576TbtyJCmBEZmDJ5oPX-XD76RrvBkLaRGeJGcXLRSKuQV0SxsQEMlFw3ywJZt68ZdfrWgsfnid7ASLm6g2BoPX1j8-kh2-u4PIaNFMFGwFkhtqi15vw5edYcKIWYigz_OpAu1zBgo1PCMi8bJ93-B6hGOngSQSojVL-pQ1OF3xm8JGxPz8Nm8JqEd6zE86fq6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی صحن‌های حرم حضرت عباس (ع) در آستانه محرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/658902" target="_blank">📅 09:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658901">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
روزنامه کیهان: مخالف مذاکره نیستیم اما می‌گوییم اگر تنگه را باز کنید دشمن دوباره حمله می‌کند
🔹
کنترل تنگه هرمز یعنی نگه داشتن پای ایران روی گلوی دشمن، تا دوباره دست از پا خطا نکند
🔹
ما مخالف مذاکره نیستیم؛ می‌گوئیم تنگه هرمز، همان نقطه‌ای است که باعث توقف دشمن و تن دادن ترامپ به آتش‌بس شد. ذره‌ای تردید نداریم، به محض بازگشایی این تنگه، دشمن تجاوز و ترور و کشتار مردم را وحشیانه‌تر از قبل از سر خواهد گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/658901" target="_blank">📅 09:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658900">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
بازگشایی دانشگاه شریف از امروز
🔹
دانشگاه شریف از امروز به روی ۴۵۰۰ دانشجوی مقاطع تحصیلات تکمیلی باز شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/658900" target="_blank">📅 09:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
خبرنگار المیادین در جنوب لبنان از حمله رژیم صهیونیستی به شهر النبطیه خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/658899" target="_blank">📅 09:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb8rQV2v6_z91te-NbaOGAwbETL7RFSxtJ07joxmOMwr7hISNqf8CdUjcDtuxuqP0ErtjMtKAWRs3PqQdmfbvTEfzWDBLUFZA3iDnine4t1tjFXR9tDBCZFe1va9x1UGqLKCS_SJlD0CuQCP7CZUG7HhdvnAUM8oICz_tQOdpvGGzISEQWJabxt4GZxekdN1z8oW7YI56GDLaXo1JrWXHo6hGVHTIoQrm-OisxQh71_vU43KkcFaWPRNyzVmj3BrpQr2io3O2aYIcF1Na0_poBxulmKJBHkalKNGbHKVTgFzqHQYB6D7Rt1GqFGb7AdYjRIne82j1jiog4Uqn3f-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای جلسات محرمانه تیم ترامپ برای مهار بحران اپستین
🔹
روزنامه نیویورک تایمز در گزارشی اختصاصی فاش کرد که مقام‌های ارشد دولت ترامپ در ژوئیه سال گذشته چندین نشست محرمانه در اتاق وضعیت کاخ سفید برگزار کردند تا راهی برای کنترل بحران ناشی از پرونده جفری اپستین و تأثیر آن بر ریاست‌جمهوری ترامپ پیدا کنند.
🔹
این بحران پس از آن شدت گرفت که وزارت دادگستری و اف‌بی‌آی در یادداشتی مشترک اعلام کردند بررسی‌های آن‌ها هیچ فهرستی از مشتریان قدرتمند اپستین را پیدا نکرده است. این اقدام که قرار بود به سال‌ها گمانه‌زنی پایان دهد، با واکنش منفی بخش قابل توجهی از حامیان جنبش «ماگا» مواجه شد.
#جاسوس_موساد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/658898" target="_blank">📅 09:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658894">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUl-H9u3GBRSGv5BgGMVqPuq8LYLHixxehIuvjNdFta5cnKDqbaGIG2vNXTHnOpJbgB7LTweCmfJvMVTGqWukGm3cguDqfovPonr49LBjOn10ixOaU9iXH2rv5dJ75GDotuAAu7PTEgNunb9j7IGdF3nZLbm-_PZJKGLLp35xJKn7unlSSo-giLwZSbSr6dMJdimQhOYq5cxkBDwO-atS-ciR5rb8c8XL3cCvlwahnHM_2qPhyImDKJpttb8Ows6_tyF-MWF9kBkINcyluJT1w36jZsI9AURFTyEKW9rCIQxKtgUDx2_n8FyI24mXLSBe7girFl0we0BQmmdUcPvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgEcWR6NmsGe9J8Mi9-MSOOvNvsfSIArKbf6kuLt7BMv8NBjrXMZCTuqkAa9_lgH8DiPTKhX1XcBz5ReB1s2Vl2V7R575eCJ0Dtn36UElT4vGa1X87_rb30tC_5rnVWwyUPBxCZAbVo7WIBTVqOgAv4NEak3esBV2MzVFNMP89kYLO-wA6cqfx1Ng7f_yjaCwjAEuoU6Guos7DFB6qKz_hPpZgveyNuDF4bO376JxVq0PJHQzMfYZinCDFikI1OCig8DZZppW4NOg2hHkay6Tqa0X97DANDmslCgpJTzCn05NyFg-w-mhu_kYqw2dyCXoTWoSZrWTbFvmkqWG9nDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Al6pUKSpbCZsOuhY1uop36eIBO2oLwQr4jThuLcwfYNlpmeSTV5ehMtnR9rZC61VmS6HXThwSjz2Lmov7Ko8HVfWdireVOE4umhOPO65a9FiWMuTX8ln0YpsbFCqPCGAgUNYtStheFZXSo687WbblB3JpNjAycBKxXhB8DxJJVXOjkNchbYnBVWl1e5wrztU1U60DpFCs8rHOVCkBKxmxkanhwBPMmQVeVeWWg5osZE51QiUrG6OTZgf3dHRUlJHecKMrNc9PwX2WIHWXJWKT5YW3Yd81Tb597ASppoj4YNeV7INQCah5a4fnX1WlJd5lh_ZzF6AMDtTpf1SzNiotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggOV4_omgIPn5KxqKx214_ieCHeiVQVDW6V0vApxI3pF2BQyKrmWRNVRj7oRjx517_W5lJYVeTyPk10RoIzdKCVYL3TLC8hGkFKy7Fq-6xYnw8_kZYj8sW9J18gx00n46--Tu7dQD3YQ8Y5UuEPB1Ank_5OnMwReuv6OQfo0oO5oVOwP-NamNY17lk3GC0ZEOe8O3mUSqBvTJI0-Sj0zmARgxeOoXYapvkJn3KU5jk5HjmairLZUhQOd18KTtlIE09dlmVqqtQNpYUV-VFyYhjKsF5URciPm6oR8E9-whNnfeHoClQx9rahJjivYQVu7QuR-ESdlILE9s-ipsytfcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کریس رونالدو و یارانش در آمریکا
🔹
تیم ملی پرتغال وارد خاک آمریکا شد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/658894" target="_blank">📅 09:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658893">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122a593ce7.mp4?token=WurC7TZUvIBKa16FxWkWG6seacwQTsW1LgRJmJw32HV3IVqVoecBpvPbl8TFEdp2o2zIxKEGhmK4tU9awDvUoAG-K0jHwCG-x-A3vDH9ovLrZVVXf9QMEVOYImzJK3vPZjXoN0W3B_WQMXLHDiOuiHD3toYOHdWAH4wix7H63Szo2X1ukSR3JuwZ5Tv-SHPH4kSXMhW6I-Ba2t5fdFWf9nzGele6EawthU506U3wE5Fy3oRyCFEun8T_0mNW7t5r1POWIiQtoD2PAJvyBJggb6_OyFCTDGrq9fxMrLwiLYxUmfMYLb6sDm7vsQeeu5QpMFz_uUyDemYedI4fydeLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122a593ce7.mp4?token=WurC7TZUvIBKa16FxWkWG6seacwQTsW1LgRJmJw32HV3IVqVoecBpvPbl8TFEdp2o2zIxKEGhmK4tU9awDvUoAG-K0jHwCG-x-A3vDH9ovLrZVVXf9QMEVOYImzJK3vPZjXoN0W3B_WQMXLHDiOuiHD3toYOHdWAH4wix7H63Szo2X1ukSR3JuwZ5Tv-SHPH4kSXMhW6I-Ba2t5fdFWf9nzGele6EawthU506U3wE5Fy3oRyCFEun8T_0mNW7t5r1POWIiQtoD2PAJvyBJggb6_OyFCTDGrq9fxMrLwiLYxUmfMYLb6sDm7vsQeeu5QpMFz_uUyDemYedI4fydeLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
*اتفاق عجیب روی آنتن زنده*
🚫
😮
توی شبکه سلامت مجری از یک کرم استفاده میکنه که مهمون برنامه گفته چین و چروک رو توی 2 دقیقه از بین میبره. منم تا نتیجه اش رو ندیدم باورم نشد ولی واقعا توی 2 دقیقه 10 سال جوون‌ترش کرد.
😳
☘
این محصول گیاهی توی ایران خودمون تولید میشه
🇮🇷
و متخصصاش دارن به مردم مشاوره 100 درصد رایگان میدن.این فرصت محدود رو از دست نده.
👇
👇
bam30.com/ads/landings/22748-2e958
bam30.com/ads/landings/22748-2e958
bam30.com/ads/landings/22748-2e958</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/658893" target="_blank">📅 09:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658892">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای رویترز: ونس معاون ترامپ، توافق‌نامه صلح با ایران را امضا خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/658892" target="_blank">📅 09:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658891">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
فعال شدن آژیرهای خطر در شمال فلسطین اشغالی
🔹
جبهه داخلی اسرائیل از فعال شدن آژیرهای خطر در شهرک متولا در شمال اراضی اشغالی در پی حمله پهپادی حزب‌الله خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/658891" target="_blank">📅 09:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658890">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیرعامل منطقه آزاد قصرشیرین: پیش فروش خودروهای وارداتی ممنوع و جرم است
🔹
رئیس دادگستری اصفهان: صدور دستور شناسایی و توقیف اموال ۱۰۰ نفر از خائنین وطن
🔹
وزارت بهداشت اسرائیل: زخمی‌های ارتش رژیم‌ صهیونیستی به ۹۱۶۰ نفر رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/658890" target="_blank">📅 08:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658889">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fdb23d2.mp4?token=PmreqbAPgiL7Iz3L9cjj664POwwOz5ttgzBA0usAdgKOdGYqxcktkBgVRpg6eStTKjaX48v78kToWhjJhrioleai-IyaoxGF5cdADTCX-L-RqefnFiHZpoamYpfTidiwrouKBwZmXQSFFSTlxQsKVDIcWqRjW0XughgGctxxDDJV0lWf1R5rzgrEgVqHHHRdlxnaU2Xj6BHVW862Feh4T4nw14oXrUdKCFmiaS07svRQe130HmhwV4N1xqvn1_jFujn9dpJGD0vJWk3Hpb3tXi5zIDRdq20hhjrqlMM5C2g_UFTvgNkIVBHVERrGXJEJm3lUNS-DEFC9BxX6SnQuaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fdb23d2.mp4?token=PmreqbAPgiL7Iz3L9cjj664POwwOz5ttgzBA0usAdgKOdGYqxcktkBgVRpg6eStTKjaX48v78kToWhjJhrioleai-IyaoxGF5cdADTCX-L-RqefnFiHZpoamYpfTidiwrouKBwZmXQSFFSTlxQsKVDIcWqRjW0XughgGctxxDDJV0lWf1R5rzgrEgVqHHHRdlxnaU2Xj6BHVW862Feh4T4nw14oXrUdKCFmiaS07svRQe130HmhwV4N1xqvn1_jFujn9dpJGD0vJWk3Hpb3tXi5zIDRdq20hhjrqlMM5C2g_UFTvgNkIVBHVERrGXJEJm3lUNS-DEFC9BxX6SnQuaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیونل مسی، آماده برای حضور در ششمین جام جهانی زندگی‌اش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/658889" target="_blank">📅 08:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658888">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
الحدث به نقل از یک منبع بلندپایه: امضای «اعلامیه اسلام‌آباد» به‌ صورت غیرحضوری (از راه دور) انجام خواهد شد و دیدارهای ژنو نیز به‌طور موقت به تعویق افتاده است/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/658888" target="_blank">📅 08:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
الحدث به نقل از یک منبع بلندپایه: امضای «اعلامیه اسلام‌آباد» به‌ صورت غیرحضوری (از راه دور) انجام خواهد شد و دیدارهای ژنو نیز به‌طور موقت به تعویق افتاده است
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/658887" target="_blank">📅 08:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
آمریکا مدعی سرنگونی «چندین پهپاد ایران»
ادعای سنتکام:
🔹
چندین پهپاد تهاجمی ایران را که می‌خواستند به کشتی‌های تجاری در تنگه هرمز حمله کنند، هدف قرار داد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند.
🔹
ادعای سنتکام در حالی مطرح شده که ایران اعلام کرده که عبور و مرور از تنگه هرمز تنها با مجوز نیروهای مسلح جمهوری اسلامی ایران میسر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/658886" target="_blank">📅 08:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658885">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16b06d3d4.mp4?token=k-ALCnHdVvl4f35EIVYVb1EdlaK_Ucc3tESz6uykY6jPmbEFk0ucgr1eo_2o8foN7ZLY4AqpUnmTc8teQHU3IzbshsQ1G7mirxYCnrPtRQLTXz5LYfeCcGNl6w3dOOXCNZQ-3_mcDYBuQ4gBkmJthaTlYryhE9nPJ1-X7aq4tcJoTcb-o5dPA6GpKlsXWZWx7Jg4w8MnjcOX6tc5u6gSTdN8-Slz_iTvjopCoCxDGbvXdTA9CvTICWBtIKIk2WyLf_jQgOE0WZl3LKCxnklSOO_IVjZmaNqYWXSKOHXztngJ2-9FZG63qSWsUUvOeDVMXR6jRnVfSLfBQKA61O8mIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16b06d3d4.mp4?token=k-ALCnHdVvl4f35EIVYVb1EdlaK_Ucc3tESz6uykY6jPmbEFk0ucgr1eo_2o8foN7ZLY4AqpUnmTc8teQHU3IzbshsQ1G7mirxYCnrPtRQLTXz5LYfeCcGNl6w3dOOXCNZQ-3_mcDYBuQ4gBkmJthaTlYryhE9nPJ1-X7aq4tcJoTcb-o5dPA6GpKlsXWZWx7Jg4w8MnjcOX6tc5u6gSTdN8-Slz_iTvjopCoCxDGbvXdTA9CvTICWBtIKIk2WyLf_jQgOE0WZl3LKCxnklSOO_IVjZmaNqYWXSKOHXztngJ2-9FZG63qSWsUUvOeDVMXR6jRnVfSLfBQKA61O8mIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تمرین زانو که برات معجزه میکنه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658885" target="_blank">📅 08:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658884">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qm9jZrrLHpxng23h4P-TkuvrtCZdIGQ6DC9B6WQZZljYzfAXNc7sTovgu4vhJnuTDgwbD6WOiv6wpraV-zOEZ4YEsNYaA89-4xP7cepYFfa7D296eKZ9RjaPVjLxP9BkwhP5yzKoIOhklrt8ODaEqHETo92EL4SJUelwuLSCyk9H_jxQA9kpMkeyQmHukTqMAgeNV7SOCAKOOo_EnVOgSVPfVVpYkMI9fsq0-sajRnXk36Ir4OkMXEHv3-8V2Ba5wgnFrWlzvL0wN0xGH7-leKTc-Ptr_U22ucZRo96z346bx1wP2zCUgS2OCUVOMUmWgmIkBEINjjb7wJwlNPWzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: توافق با ایران تا اوایل هفته آینده نهایی می‌شود
وزیر خزانه‌داری آمریکا:
🔹
با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران احتمالا تا پایان همین هفته (میلادی) یا اوایل هفته آینده نهایی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/658884" target="_blank">📅 08:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3edcbbf56.mp4?token=qDF552N8E-Xj8apSvDm_tK7xDNTGKpxVJEErdFbPwTgyz-4t0NVDGx_ZRU55SBI6-zjWTwhvj02msXsgoU9Kej1Yeoq6ViL_o2PnoPsYkZ9c1ZdrNnZ0jqAB-Yu8J5q2xUym-UhjDhpva1GjgO_1tC99ZsuCvDBWfjjw3CdvEu4wAyFfzbGR7dD3AQowWV9HExXU8sgqFjfcqYRxnjpLiVUifhVaVPKkLIdim3Bm0b66yKg_sNichfTr1GC6h55W-hLukymD1oVFR2VfrePEM70YoF-KtQNhl4xUvpCo_YQ4Rkf2z7wbpGuLwQ1B5owMIx82881Qn3PGNokV7eZ5SWzwMIs4BP8rosiE3gUNoaZ-g20tSPfcqyr4QkeEDfw1gxAOnfMePJ0YntaAiskKyUUURPEy6S9ls9x0ReHRcI7QMFNslEDs_YOg3k9ccDo5MaFfK7OIp_4x5DF-p_9LP3L_DgpEotJ8HQqC2zvF2nEEndhgXIGmn-EGI8ZHUAGavw-k38AjvpE-OKYwJh2mZ8mKSI0Xi4ZZyd9ex36b-Vw5tnLatty-3jPSA1QgeE3JdCnN_vbEFAwdeM2LoYxLgCQHkVB6pplBV1pLpxtwGme8rg0--ycb8uImD2Zq6Qlm_szxSIASAjspO7RBW7tuarHI_VGp1Zo0JjbpgHg5cyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3edcbbf56.mp4?token=qDF552N8E-Xj8apSvDm_tK7xDNTGKpxVJEErdFbPwTgyz-4t0NVDGx_ZRU55SBI6-zjWTwhvj02msXsgoU9Kej1Yeoq6ViL_o2PnoPsYkZ9c1ZdrNnZ0jqAB-Yu8J5q2xUym-UhjDhpva1GjgO_1tC99ZsuCvDBWfjjw3CdvEu4wAyFfzbGR7dD3AQowWV9HExXU8sgqFjfcqYRxnjpLiVUifhVaVPKkLIdim3Bm0b66yKg_sNichfTr1GC6h55W-hLukymD1oVFR2VfrePEM70YoF-KtQNhl4xUvpCo_YQ4Rkf2z7wbpGuLwQ1B5owMIx82881Qn3PGNokV7eZ5SWzwMIs4BP8rosiE3gUNoaZ-g20tSPfcqyr4QkeEDfw1gxAOnfMePJ0YntaAiskKyUUURPEy6S9ls9x0ReHRcI7QMFNslEDs_YOg3k9ccDo5MaFfK7OIp_4x5DF-p_9LP3L_DgpEotJ8HQqC2zvF2nEEndhgXIGmn-EGI8ZHUAGavw-k38AjvpE-OKYwJh2mZ8mKSI0Xi4ZZyd9ex36b-Vw5tnLatty-3jPSA1QgeE3JdCnN_vbEFAwdeM2LoYxLgCQHkVB6pplBV1pLpxtwGme8rg0--ycb8uImD2Zq6Qlm_szxSIASAjspO7RBW7tuarHI_VGp1Zo0JjbpgHg5cyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری معروف روس از خجالت اروپایی‌ها درآمد
🔹
۱۶۸ کودک ایرانی کشته شدند، صدایی از شما درنیامد، هیچ تحریمی علیه کسی وضع نکردید....
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/658881" target="_blank">📅 08:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: رفع تحریم در ازای اقدامات ایران در خصوص برنامه هسته‌ای صورت خواهد گرفت
وال‌استریت‌ژورنال به نقل از منابع آگاه:
🔹
واشنگتن تأکید کرده است که هیچ گونه لغو تحریم یا آزادسازی دارایی‌های ایران پیش از اقدام مشخص این کشور درباره برنامه هسته‌ای‌اش انجام نخواهد شد. هرگونه منافع اقتصادی برای ایران منوط به «راستی‌آزمایی کامل» پایبندی تهران به تعهداتش خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658879" target="_blank">📅 07:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1c9a800e.mp4?token=h11K4ywxcJbTD2VPTjuffP1x0W73C3cOFlUC5aoCyn3hMHM_drjhkACLKvz5wLGCwlvjkrQO8zrfSa-u2TY8l5Zfilly7Y1WF34Tyv9eCvho7Gt54fwldbdqzo31jJmat68DVU1eWyegL5hWV_jRUdOIv3Ych3LGiFwz9NKF-2mlMVDlP_tR54UN16NMCHVVBRkfDpYwn0NCBs4joWvBSS9TTunqGcJrOu_4OXnmQpgRwr0kj2iJ3hP3Kv7H_wAFQYq1fptVAAgLQ_jmQ0j7oKdVVHFBFzyDmn5i0pOfUD8oUa6bxQ3XErJmIaWj5sR9PYA3Ymox-bGM0mMzmY47iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1c9a800e.mp4?token=h11K4ywxcJbTD2VPTjuffP1x0W73C3cOFlUC5aoCyn3hMHM_drjhkACLKvz5wLGCwlvjkrQO8zrfSa-u2TY8l5Zfilly7Y1WF34Tyv9eCvho7Gt54fwldbdqzo31jJmat68DVU1eWyegL5hWV_jRUdOIv3Ych3LGiFwz9NKF-2mlMVDlP_tR54UN16NMCHVVBRkfDpYwn0NCBs4joWvBSS9TTunqGcJrOu_4OXnmQpgRwr0kj2iJ3hP3Kv7H_wAFQYq1fptVAAgLQ_jmQ0j7oKdVVHFBFzyDmn5i0pOfUD8oUa6bxQ3XErJmIaWj5sR9PYA3Ymox-bGM0mMzmY47iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از قانون جدید VAR در جام جهانی ۲۰۲۶
🔹
دخالت در کارت زردی که در بازی آمریکا -  پاراگوئه به اشتباه داده شده بود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/658877" target="_blank">📅 07:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658875">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vu-e-OKfy_XzK3e51Up4VokZwTdD8h1NRaXChQsWMC57X301bKx7q6gYYSOtwtgwexIrJ7jHa3iOa5YbpxuNgLvZHUXh2eGemgs1jU3CzVEhbVn3AoLyFSoIqk3VEn2y-r2jyCvucpa3avfm9yxq0uo2ld4umQslfB_pi7V8GWfoCebFvQrLbBvfkqmh4E0RFHUslIj7bJTPmXFOiZHMAvmTqD8U6dYOgTLOytpohnShtjJ9C11d1JOcYTQMqpOWl-eJN3KPaZKkqaoUd87MqniSw-QUWj49OPmuvX_cOaigr6SrLcAb7i7WdQFHoY8FCmZN-BLCoxnxODLNIZMYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPKCz4nEQLo7d3jKWMBDTcnsq8q23R70RaD5X6Ql5alC-d8xmaRF40eV9JMtnVaXuiHZ-71PN5NvJKn4MxPekYhclSdOoffFriVZXqdJvk2rLop8hSBJuI_YVU4qg2yHCr6ieuskD4SmcDft0FY1nNLl7-qewtLl1xEC3zbLJPE_BXuksN-oTEmJkIRNkcDNal4e6t247-4OJtzLzjxUFuqHQf-ba2hKRS7jlogAvSGFQIEpQs-9rPrpXA06NDwf_4YWFtUdEilZSj6DeAqRYdOad3dLG72GObnBCNOKJHvp6kgBUpNGpeodjWtjnJXFVf-6q5KAAAIQyQP2LrTpmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کشف یک جسد در نزدیکی ورزشگاه تمرین تیم ملی فوتبال ایران
🔹
خبرگزاری فرانسه (AFP) گزارش داد که جسدی در حال پوسیدگی درون صندوق عقب یک خودروی پارک شده در نزدیکی استادیوم کالینته (ورزشگاه محل تمرین تیم ملی ایران) کشف شد که در حال متلاشی شدن بود! این خودرو در پارکینگ فروشگاهی نزدیک ورزشگاه «کالینته» قرار داشت.
🔹
دفتر دادستانی کل تیخوانا با انتشار اطلاعیه‌ای اعلام کرد که این جسد در جریان یک گشت نظارتی کشف شده است. در گزارش اولیه آمده بود: « مأموران گشت هنگام بازرسی خودرو، متوجه حضور فردی در صندوق عقب شدند که درون یک کیسه سیاه پیچیده شده بود و آثار ضرب و شتم روی آن دیده می‌شد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/658875" target="_blank">📅 07:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658874">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ثبت‌نام سرویس مدارس آغاز شد
🔹
والدین یک‌ماه فرصت دارند تا درخواست ثبت‌نام سرویس را در سامانۀ سپند به نشانی
irtusepand.ir
ثبت نمایند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/658874" target="_blank">📅 07:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658873">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXRH45rq1IGJlaZhcUWn8Vuctkb-ufltE-E81Qfq8tiiAo18VcIxXvDyJCjwMndAUXSF2dEtJCbnU4Arcf0srcPfaV2NgsuMa-XzZdRN9oRV41g--jPr6I4tk-7K6JeJWD_qh-imio1dFNHDgRj8HE9YEVCns9gckLbbBksFGDT8PgoAxFruEgrzmQF5GLDGl5pojGkfamSpNSvXwcKTOKBEAcycsJmdtcsb_PKL7b60agYc32pCLs1ESCjz6rL1jh6V8rK3DBXwBSonIEAIqfvPk6IkxWt5E7nRI4-By39Kk7cR6y8B5jHLO_AHFRNTH_XBudq90GpR_vTGEow6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین پیروزی سروقامتان ایران در لیگ ملت‌های والیبال
🔹
ایران ۳ - ۰ آرژانتین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/658873" target="_blank">📅 07:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658872">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG-aPnhV6vGOdsUjesCmSQNO9kJiGo1TAla0uJJmf14T6rVXNYCNWxWFSumzF7CRe6WbAj3Dfq5JD2S02kAtstW_l4isCon2Zm4HFir43eLUdb7qzaMu2N3ftcQfFej_SRPkxoJjI2sRsJb-sGmDbiSgUUb_erxBcerGQEB_OiOvsToGm2qJvr6zaZgZ072JWma-o9CZeu-2c2IKu3QNF2PEiPjNbPB_OHIsmWSs0bkj1mSK0DsVNVMqmV3eheeHD1xUXvEL0u3dshx-GZYZjNwTeCYOC_5-m6L93x4rETdkNBdbQXm7FdQ0OmgNgUkUchahOXZJO2DL-0g2gFMqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امارات ادعای رسانه‌ای در مورد انتقال وجه به ایران را قاطعانه رد کرد
🔹
امارات متحده عربی گزارش‌های برخی رسانه‌های بین‌المللی در مورد انتقال یا تحویل هرگونه وجهی از امارات به ایران از جمله ادعاهای مربوط به سه میلیارد دلار را قاطعانه رد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/658872" target="_blank">📅 07:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658871">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beyFjF6eGqNotxYlDjai-WEWGlvLWxRRLfAoTtGcaG5Gh2e3szQb2UehZQRk4kyzDXl_lca2ACeh0GS6DYJ897uW53carDQuAsKiXOCuOlWgxoQcVbnaW_WZyUMEIhSyv2pFdlNyhwRDC84Qdj_50gQq1-RDzMoJdIM8gbSUY_B0miuEJfEfMA9N9Eeb22UHzegXI2Vu6T4uNCBXSmaW7hAb4-eic_vtLMXaMG8QzLRAt3Ldqz5ugcRBQFQ8YbT9hhx9CfteLThZXhGnOx9DKVV43Z59XprP3mjgzqGvm98RtP-iIIMZEaj9AKAHQeZ8NhMYx2nvACCNGp_3OHgt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲۳ خرداد ماه
۲۷ ذی‌الحجه ‌۱۴۴۷
۱۳ ژوئن ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658871" target="_blank">📅 07:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658870">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در حوالی جزیره قشم و سیریک؛ گمانه‌زنی از درگیری دریایی
🔹
دقایقی پیش ساکنان مناطق ساحلی و بخش‌هایی از جزیره قشم و برخی نقاط ساحلی شهرستان سیریک صدای انفجاری را شنیده‌اند.
🔹
تا این لحظه هیچ مقام رسمی یا نهادهای نظامی و انتظامی منطقه ماهیت…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/658870" target="_blank">📅 00:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658869">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در حوالی جزیره قشم و سیریک؛ گمانه‌زنی از درگیری دریایی
🔹
دقایقی پیش ساکنان مناطق ساحلی و بخش‌هایی از جزیره قشم و برخی نقاط ساحلی شهرستان سیریک صدای انفجاری را شنیده‌اند.
🔹
تا این لحظه هیچ مقام رسمی یا نهادهای نظامی و انتظامی منطقه ماهیت این صداها را تأیید یا تکذیب نکرده است. /مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/658869" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658868">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqpUJ2FeZfukwZpYk6LIgbGYnUFu58nItateLQKykukkveOAGzkWdk8oCLOY-5vF7yQ-5ZRAP6jQDs8RvkX9s5xIRMxdjLQniGvqBRlKBEbhLkVcJ2vWF948oeYUCTcy2VTS-ACQuS9ao9JK_8Aa3P0AUhwwzWwRDWMtV0O_34STmi8jhPR-2HJos_x27x4HWITejSQd8gDqTzJepRWmbgZEpDaHM33iTflSmKEv331ucLc9WO4PU2cAJvMw3hsDHukr6dK14i-S89vuPxfg2uHRWLsohEAsbK8fzoWkqZaxIeExswLDEt7exTaGi1k15qkfGksYlyAV94ozXksOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/658868" target="_blank">📅 00:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658867">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzgh_1sGcjOuOFYmJ37iYYf-fA7MGp7j9Tod-bpkNbWmJB8NA1wq17XAfcSIbC1aaXavy0qgii-8KisEV7mlp3MjLDMrDFg8LJgdlmPkO_uwGrQ1PzHUpujMNjTFs-wpTBHQq1VkIvlFiB716rxtAupYkD-k8bBuswVr4FpGvz2q2d9MAqpj0nLFTYi7GBKtNc--A1HPR7KW4tv-5U6jBqluh0AmnSZRdL7SyxBg-Lm3dhmu7uk9bGSBsmfqxuaPigUDyOiYcK8eISqNLDWi98Y___Yq2FJ3ibD_WIa2Icn5VE_cmlNWgZk9f9bdz6AYQTB6zfgHtiZUzCwfwsK1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز به صورت همزمان گروه های سرود جان فدای ایران ، سپر انسانی به دور زیرساخت ها تشکیل دادند
🔹
در بیش از ۱۲۰ نقطه از ۳۱ استان سراسر کشور
🔹
تصاویری از حضور مردم و گروه های سرود در اطراف زیرساخت های ایران به منظور ایجاد سپر انسانی نمادین دربرابر تهدیدهای دشمن آمریکایی را مشاهده می کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/658867" target="_blank">📅 00:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZM7m03_jrjG9z5AAQ-9g_dbVJZkYMhwbyHhI_Hxl9YyY4-ybb_u3DZgK9bLD_tg4nr9ViYwuZmQOxsQT9vMKJQXZ5-sdr1dclUnwHMePvlOTeN6Czn3hrUWAVmOJhd3rbLkBbhPnUmhtakGoeIsMQf1ast7ebpKDNuaM2PFVeBOtRYXcaLA_zixxxS-5dNi3yLcc8YlA2mcWqOdOX99GorChy_WTgJkbmRnXpSSNSJ6ew9AH7pEHGhPsSfXKU3XURDQ-PfZBAUGrCx7Ivil26DmHPqdijqpzZ6kUo5IRQFYQaLHjEdmOEI_v64_cimmtuWlY2VIXugSgMe-_WkZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجیب‌ترین رکوردها در تاریخ جام جهانی فوتبال
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/658863" target="_blank">📅 23:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csd2lvoQpV6MnQ2MvEEufsb6i-eZOzQ8MUlx1ee6paLPpxAa0JumYtA_JAd2CLILynsL_wAgMkWoyfra3aCdsII1orbCRY0VxmjmJhAwcQayzT-KwPadBWL5A5FC2miDMl2-IiY-40PI0pZ6Vr6AH-S0N57Hq24R3bJT1EyY3B6gK7oif6X6sjV6niYpQJWpJ1ro0fARzL6c3TxinS8DSL5GvPUkPqVLwE_1We2JE_ixQ0ZyyQmCtk55YwRUBES8NARNsyQRVtlxA1eU-HP-HUPhLejyIGN8o0dxWgLSbRZx0ObMm0Y7XnopwfcMUKJVzY8M5t3ltOYN986J478DYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تتر بعد از اخبار جدید درباره احتمال امضای یادداشت تفاهم
🔹
۱۷۳ هزار تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/658860" target="_blank">📅 23:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
عراقچی اعلام کرد: احتمال امضای تفاهم در چند روز آینده به صورت دیجیتالی
وزیر امور خارجه ایران:
🔹
به محض اینکه آخرین مراحل مذاکرات انجام شود، توافق امضا و اعلام می‌شود. امضا در مرحله اول به صورت دیجیتالی از راه دور انجام می‌شود.
🔹
ممکن است این موضوع در چند روز آینده اتفاق بیفتد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/658859" target="_blank">📅 23:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عراقچی: موضع ما درباره مواد غنی‌سازی شده این است که اگر بخواهد تعیین تکلیف شود، تنها شیوه رقیق سازی در داخل ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/658858" target="_blank">📅 23:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
عراقچی: شورای عالی امنیت ملی تصمیم می‌گیرد که چگونه با مذاکرات برخورد شود
🔹
پیشرفت هایی که برای آتش بس بود در زمان خودش محقق شد. شورای عالی امنیت ملی اشراف کامل در مذاکرات دارد. یک‌ کمیته‌را در شورا مشخص کردند و بر روند مذاکرات نظارت می‌کنند. اشراف کامل…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/658857" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658856">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPat2k2eWfCRvSnTxgP4UfGm_zTMaKhgfIfmfixlAu9VMst1fAJyG9Eqp0vtO-nSPpJHfX03ymeolmZ4_5OG4keialtHarEmgiq_YAcBHSP_vZk8TFzdGZlEDcwG3-YpWSlga_RLJu7LtOf82kLHtPMVgUA91A4cpiaVoK1qPU1UZ2iBxLKB1Y2eFtvKP560jZXhlo4BZMYTEhZ0wcZmWG7e5avaH7jrv34lhc39k3X_OvXADxjRcjMDbvj54lgHxQ3w8YfBkbsjHFzfBiSYaz5nxnb54qBDSkhtcBdkmpGXBG3cjMEDGkAyLiFIZRaL26mWlkJF_qc5uYYsyblX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرص لاغری اوزمپیک| ozempic
💊
جایگزین آمپول های لاغری رسید
...
💚
😍
‌رسیدن به وزن ایده آل و تناسب اندام آرزو نیست
😉
👇🏻
🔻
۸ تا ۱۰ کیلو کاهش وزن اصولی در ۳۰ روز
🔻
بدون عوارض ' پشتیبانی ۲۴ ساعت
🔻
دارای کارت شناسه وارانتی
« عودت وجه و استعلام اصالت کالا »
زیر نظر متخصص تغذیه و کارشناس لاغری
👩🏽‍💻
‌
برای مشاوره رایگان و ثبت سفارش عدد « 2 » رو به آیدی زیر بفرستید
👇🏽
📩
🆔
@
Parisa_norazar
🆔
@
Parisa_norazar
💎
09963990775
آدرس کانال رضایت و نمایندگی اوزمپیک
👇🏽
📩
🆔
https://t.me/ozempic_noorazar
🆔
https://t.me/ozempic_noorazar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/658856" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658855">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c90df03cd.mp4?token=uUZVMFHHvn_fSynqE2-cAX_BQaohCHrxR6xMuq5gTMEd-GELSeJ71QUbSZ6SWDgfPpMByWAsmnhcp4PeUPNKkE9T3lRPJhBJRnZBbn2qFc1PwcrAtvhCK81trM8S2yq3-zNF-vsgBlBxXk_bummKk3R-2Dlmoper6Y6UUqjhdh_NO9ZKc7Fe7kEllVKQX_WP0nai0AL4jToEt2ghqZxEFsmYMhldIaBh5LFnzx6AxukpX-rH1DrG1No43MqSzf-bFz08NDPKz3bYkF7OJYCF1Izq9fMoK0QfvlKXZkHGhMtapJQPYSnLNuK7olclfet_tZWzR5lUPRGJpGokaoGW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c90df03cd.mp4?token=uUZVMFHHvn_fSynqE2-cAX_BQaohCHrxR6xMuq5gTMEd-GELSeJ71QUbSZ6SWDgfPpMByWAsmnhcp4PeUPNKkE9T3lRPJhBJRnZBbn2qFc1PwcrAtvhCK81trM8S2yq3-zNF-vsgBlBxXk_bummKk3R-2Dlmoper6Y6UUqjhdh_NO9ZKc7Fe7kEllVKQX_WP0nai0AL4jToEt2ghqZxEFsmYMhldIaBh5LFnzx6AxukpX-rH1DrG1No43MqSzf-bFz08NDPKz3bYkF7OJYCF1Izq9fMoK0QfvlKXZkHGhMtapJQPYSnLNuK7olclfet_tZWzR5lUPRGJpGokaoGW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/658855" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658854">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
واکنش عراقچی به ادعای معاون ترامپ در مورد آزادنشدن پول‌های بلوکه‌شدهٔ ایران: بعد از نهایی‌شدن تفاهم، در عمل همه خواهند دید [چه خواهد شد]
🔹
به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/658854" target="_blank">📅 23:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658853">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d496fad7.mp4?token=IXAdqDdGxy7NWKzChK2kE2il4cBdW3GUxD5iVscaW3nEH7z8esPwCHz7gqRl3d2DWCwXr93YuAsXJlRO1qgrDmkk2pwDQ4nwVw_YNHNAvSBwN9PTsu-g4pflNgivxCOEXAEahyLNRUkYTCx63g6XQ6F9fNFZoML1G5ktF9d4Yw0RvI5c6Wwfsf3XnvdjG6i-rpBlDb542QnjfdGCknoteDcZ-cDfTN29D0b_LutAZ3s8FM2xZOiZNR_yMJwdZs2ZkRTFpXeflNkBrA4BYy_DmmAh5YEhinaUge-izRo0pzAJVl9dtUqPf1e3SFGg-Lumkq1qTwiwAirE8bRisfs6Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d496fad7.mp4?token=IXAdqDdGxy7NWKzChK2kE2il4cBdW3GUxD5iVscaW3nEH7z8esPwCHz7gqRl3d2DWCwXr93YuAsXJlRO1qgrDmkk2pwDQ4nwVw_YNHNAvSBwN9PTsu-g4pflNgivxCOEXAEahyLNRUkYTCx63g6XQ6F9fNFZoML1G5ktF9d4Yw0RvI5c6Wwfsf3XnvdjG6i-rpBlDb542QnjfdGCknoteDcZ-cDfTN29D0b_LutAZ3s8FM2xZOiZNR_yMJwdZs2ZkRTFpXeflNkBrA4BYy_DmmAh5YEhinaUge-izRo0pzAJVl9dtUqPf1e3SFGg-Lumkq1qTwiwAirE8bRisfs6Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول بوسنی توسط لوکیچ در دقیقه ۲۱
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/658853" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658852">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
عراقچی: تنگه هرمز الان یکی از ابزارهای مهم بازدارندگی ماست
🔹
این آبراه سال‌ها به روی کشتی‌ها باز و رایگان بوده اما تصمیم جدی ایران است که آینده تنگه هرمز مثل گذشته نخواهد بود.
🔹
اگر آنچه در یادداشت تفاهم آمده عملی نشود، مذاکرات برای توافق نهایی انجام نخواهد…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/658852" target="_blank">📅 23:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330b6d5794.mp4?token=UZo-Bk23gkxyRZJJ_McpjRb6fOJHu58-f_QJGkSa-dUanzjgCDTcRY-2iqPuOYKDfC9Agf6CYG6E7wXVNfiH6twVO46brNqIuTsV83Hg9HCtWNwLhFW8pBF_47ZkVgQqJe8UYcMFrDOXoO26xVRisrK7e9qt84t86i-YSWeDlu8n9_r13BvccwjFPAQdBmDKC90cRZE3WDO9OkGLTAM2tpKQyqjM5sjh3n6OIJhUBRz9-X30iRevuodnzmLQGgEiI5VduLhaYi0P0eDHJeF0lyYSiFMFvKOLxvFyxTE4CmHy0yhL8qo6X7X35hj6DtWL8BMbnE1aTgWlYD4MVIJjDoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330b6d5794.mp4?token=UZo-Bk23gkxyRZJJ_McpjRb6fOJHu58-f_QJGkSa-dUanzjgCDTcRY-2iqPuOYKDfC9Agf6CYG6E7wXVNfiH6twVO46brNqIuTsV83Hg9HCtWNwLhFW8pBF_47ZkVgQqJe8UYcMFrDOXoO26xVRisrK7e9qt84t86i-YSWeDlu8n9_r13BvccwjFPAQdBmDKC90cRZE3WDO9OkGLTAM2tpKQyqjM5sjh3n6OIJhUBRz9-X30iRevuodnzmLQGgEiI5VduLhaYi0P0eDHJeF0lyYSiFMFvKOLxvFyxTE4CmHy0yhL8qo6X7X35hj6DtWL8BMbnE1aTgWlYD4MVIJjDoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احیا و حقیقت | قسمت سوم: سرمایه مردم
🔹
روایت محمد جامعی از حمله ناجوانمردانه دشمنان آمریکایی‌صهیونیستی به زیرساخت‌های غیرنظامی ایران اسلامی در شرکت فولاد خوزستان
🔹
در آن یک دقیقه، فقط آهن و فولاد نسوخت. رؤیاهای هزاران نفر زیر آوار دود و آتش ماند. پشت هر…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/658851" target="_blank">📅 23:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
عراقچی: اگر دشمن بخواهد سمت جنگ برود ما آماده‌ایم
🔹
هیچ شبی نبوده که دشمن تعرضی بکند و از نیروهای مسلح ایران پاسخ نگیرد.
🔹
به‌هیچ‌وجه از منافع ملی ایران نخواهیم گذشت و تسلیم فشار و زورگویی نخواهیم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/658850" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
عراقچی: بحث دربارۀ رفع محاصرۀ دریایی و تنگه هرمز در این تفاهم‌نامه مطرح می‌شود ‌
🔹
ترامپ هرچیز دلش می‌خواهد را از زبان دیگران توییت می‌کند
🔹
اگر قرار بود چیزهایی که آن‌ها می‌گویند را بپذیریم در گذشته می‌پذیرفتیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/658849" target="_blank">📅 22:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
عراقچی: بحث دربارۀ رفع محاصرۀ دریایی و تنگه هرمز در این تفاهم‌نامه مطرح می‌شود
‌
🔹
ترامپ هرچیز دلش می‌خواهد را از زبان دیگران توییت می‌کند
🔹
اگر قرار بود چیزهایی که آن‌ها می‌گویند را بپذیریم در گذشته می‌پذیرفتیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/658848" target="_blank">📅 22:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658846">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
عراقچی: دشمن تعهد خواهد داد که دیگر آغازگر جنگ نباشد و از تهدید و زور استفاده نکند و دوطرف به حاکمیت یکدیگر احترام بگذارند و در امور داخلی یک‌دیگر دخالت نکنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/658846" target="_blank">📅 22:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658845">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
عراقچی: توافق شامل دو مرحله است و موضوع هسته‌ای را به مرحله دوم انتقال دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/658845" target="_blank">📅 22:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658844">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmpoTMsRDZCRs-OoV78_6orDEptRz4L-ZO5kqXZk8sRKv9jyKrQvkprlK2wYWi5jdj_7EaPiVWXTnoiba6XobRiHvDEE_f10K9WSzAVd1kJMHoCvEfn-ct9W0po_WCZJTaCn5z56xq0r49vca5krRn3HAMPdzW8RX_QCaMG_BHjImyKf0V4I3rY-LgmeE_WnmRvDAmVjDyVWA3cA4HxY6ZcAoT8eJ5LM6dd8i_YkQYJoyH29Nl60crRFNuGaghg8n-3_BxDVoGU_2ZkDxRTIVe_a9mRhGljCAW4t1sc5hEa1W2fYTF8y7wyZaVYhWCk6cPDmca8MANV6_KmO4IdChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: باید به تعهداتی که داده شده عمل شود، بدون هیچ اما و اگر و بهانه‌ای. برای توافق نزدیک پیش‌رو راه دیگری نیست. هر کسی درنهایت چیزی را درو می‌کند که کاشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/658844" target="_blank">📅 22:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658843">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
عراقچی: ترجیح میدهم جزییات تفاهم احتمالی را بعد از قطعی شدن بگویم
🔹
هنوز تفاهمی امضا نشده و ممکن است برخی موضوعات بالا و‌ پایین شود
🔹
متن تفاهم تا الان در نوبتهای زیادی تغییر یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/658843" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658842">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وزیر خارجه: نمی‌خواهم شعار دهم به عنوان وزیر خارجه عرض می‌کنم در این جنگ پیروز شدیم  عراقچی:
🔹
کسی ایران را اینگونه نشناخته بودو تصور ایران ضعیف در هم شکست شما شگفتی آفریدید. اینها شعار نیست من اینها را مسئولان کشورهای خارجه شنیده‌ام.
🔹
ما پیروز راهبردی…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/658842" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658841">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
وزیر خارجه: نمی‌خواهم شعار دهم به عنوان وزیر خارجه عرض می‌کنم در این جنگ پیروز شدیم
عراقچی:
🔹
کسی ایران را اینگونه نشناخته بودو تصور ایران ضعیف در هم شکست شما شگفتی آفریدید. اینها شعار نیست من اینها را مسئولان کشورهای خارجه شنیده‌ام.
🔹
ما پیروز راهبردی به دست آوردیم؛ باید طی یک تفاهم این پیروزی را تثبیت کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/658841" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
عراقچی: دشمنان ایران فکر می‌کردند با به‌ راه انداختن جنگ ۴۰ روزه می‌توانند به خیال واهی خودشان کار را تمام کنند اما مقاومت تاریخی مردم و نیروهای مسلح ایران آن‌ها را ناکام گذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/658839" target="_blank">📅 22:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9QiEbkrTYIjWFoU-xhoUXc-NQ_K-7L2KvS3vIA-jkXBp4S2T9fi4IjOcQXtQoV-OLLI_LJAQFmhU7bJLml9dIaQ5Bp_rfMSP7-MiYUmdYkiHySDfKM_837gwh85FRXTkOKP5uORNf9A7NTcK1FZ8eFVs2wTVI4MyEB9rwrm28deT78JT1u2o-s4fXT2n9rb85pRfE1n_3jx6jCu51mcwDpUmMvT3tgNOd-How3Yi4RLtmvg0LnrpXpuau9dStZuSop8iXNGQ2E17rUBfWHtPp112Q8gFY0mMNizr71X0TeJQArhFurnBmSn9mSBE-96jKSMLjlxTaf71Jc7GMOvaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: دشمنان ایران فکر می‌کردند با به‌ راه انداختن جنگ ۴۰ روزه می‌توانند به خیال واهی خودشان کار را تمام کنند اما مقاومت تاریخی مردم و نیروهای مسلح ایران آن‌ها را ناکام گذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/658838" target="_blank">📅 22:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnepvhDn2H7J6MoyjpnhwiExqksKVTf_KIAFPxsEqCMbkwjpQUQCi4VwUGtxO1Y_0mON0fMjBF1aJQCn5EvWh7ap0F_A_S2MvHAKNLdru0TMfhHju1pRVc2XTbEM3RHa16DZ43bZhzn83o_EFPcOgpLx-peTX9EtJyVrtSO9XOttqQS_YyZsgbSuHXQkTG0vHtj3jb9sEvZIAsL8qvIhAuEMi0vCo6H7z_w5NQd7mg8yrLAe4PI5tQn9NkWPF4d6QJPLlgwC2iQ2EO0YRvkFQHF9rul09r2S6e-DJZ-5uUqaCisidc2eR5_eaE86iEZkYXe59_g5nrZxDeG0BNF3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پرچم ایران بعد از مکزیک، در کانادا هم بالا رفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/658837" target="_blank">📅 22:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0WI7Z2o4f6BLnxXHZfPGGMvp55Exx5kxjfUlcVqf6C0BaZeVDGHEUujMeu9Cdkl6A0KVUFxDV0g2ujF2JZpo1mu_uoapq0KWCOG4Fc5LElTKdjoPce8WQkOHZ_u3T8h7EOdi_QEvDFxv_HxZ4nnNN0y-CPNLZl6_hLevKErG3SzS58Qo7yjqYY7udUN9MZ4hKhIiUrF1nUr3_mF1PrBlDbiVT7JKHg5xVtxEf5BU1fRaZT39gWcKsfP3pBCTKcYJFMBNgi4V2TTsMk1fmbYY7Gbbq9ubLkNBe7SGoKM_JdqhJ1SNIpRSAt7FS6HOQURg45pzmVDbxr4qFYne_b5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک پس از عرضه اولیه سهام اسپیس ایکس، به اولین تریلیونر جهان تبدیل شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/658836" target="_blank">📅 22:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نیویورک تایمز: تخلیه ذخایر نفت جهان به ترامپ برای رسیدن به توافق فشار مضاعف وارد کرده است.
🔹
حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است.
🔹
مقام آمریکایی: مشکلی با نیروگاه هسته‌ای در ایران وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/658835" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658833">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اهدای تجهیزات تنفسی به بیماران سی اف، زیر سايه امام رئوف
🔹
به دستور تولیت آستان قدس رضوی ،۹۰ دستگاه نبولایزر به بیماران سی اف، در بیمارستان اکبر مشهد اهدا شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/658833" target="_blank">📅 22:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658828">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای رویترز: امارات قرار است مجموعاً ۱۰ میلیارد دلار از پول‌های ایران را آزاد کند که بیش از ۳ میلیارد دلار آن قبلاً تحویل داده شده است/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/658828" target="_blank">📅 22:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658827">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای رویترز: امارات قرار است مجموعاً ۱۰ میلیارد دلار از پول‌های ایران را آزاد کند که بیش از ۳ میلیارد دلار آن قبلاً تحویل داده شده است
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/658827" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658826">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a055303acf.mp4?token=XM2ZpA8jkqXAvFJM8YPhy6rUzxv3IsN4w6TGULjiZb6i8bATI1eSAnBSN07m_QhZxSNc6AF6SXmmwwJv96vlz9ILk--CdUS21b5lJQzr21-2sJJH56ne2jHebxgahlBQ8yaVlhTlKy9IkOBRHGWZuJuHBbuxDQVFcbKrx1qDV904WbJBVX3SYHCmEES3clab5mIHbqAsIrEOeWzvehPeCgNic3bPCge-Z7E68l8HgOJcNA3x0m0N8h5Zub9ibB9OhZahDGCs9v-vGpkU0Nd6_navd3XuayQlnj-61RNNG1SZCREf00fjtssv7_eUz-P2lCtQLpbN7SlJh3R3qwQmIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a055303acf.mp4?token=XM2ZpA8jkqXAvFJM8YPhy6rUzxv3IsN4w6TGULjiZb6i8bATI1eSAnBSN07m_QhZxSNc6AF6SXmmwwJv96vlz9ILk--CdUS21b5lJQzr21-2sJJH56ne2jHebxgahlBQ8yaVlhTlKy9IkOBRHGWZuJuHBbuxDQVFcbKrx1qDV904WbJBVX3SYHCmEES3clab5mIHbqAsIrEOeWzvehPeCgNic3bPCge-Z7E68l8HgOJcNA3x0m0N8h5Zub9ibB9OhZahDGCs9v-vGpkU0Nd6_navd3XuayQlnj-61RNNG1SZCREf00fjtssv7_eUz-P2lCtQLpbN7SlJh3R3qwQmIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرایند زیبا از آیین پوش‌کشی خانه امام حسینی در شهر یزد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/658826" target="_blank">📅 21:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658825">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2887501b6e.mp4?token=kQ-i-ew3FN-GoTFhmB4GGp8-eBvRyGmGy7c41i0A5ZuMN3t0VFx4bgDKs9DRegxeqFFVukWcY1jqLUao_rA8K7qN5ep25eeUfqu0-XBik6-7CRMGSLUGNaawETIYYe2OC-z7p-pk3WugZQe7owG6EjIwK3_qUxgsW_UJRh4Tee01hVXWVMe7OZRko3h90sR8liNteyHIN0CQf0Qw7cZ6VFBdRvZ0EONndhyd9Qy0Zue7tqYum5hUpYb5nnA6GzGUf4MNS24yB3BBP4v-DGiQkY6ZmCG0X2KlhDnTDvbbQnYnzCrBJp4RJhL_N7T5WB0o3hVbWFwOBLHnwemjkHsYl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2887501b6e.mp4?token=kQ-i-ew3FN-GoTFhmB4GGp8-eBvRyGmGy7c41i0A5ZuMN3t0VFx4bgDKs9DRegxeqFFVukWcY1jqLUao_rA8K7qN5ep25eeUfqu0-XBik6-7CRMGSLUGNaawETIYYe2OC-z7p-pk3WugZQe7owG6EjIwK3_qUxgsW_UJRh4Tee01hVXWVMe7OZRko3h90sR8liNteyHIN0CQf0Qw7cZ6VFBdRvZ0EONndhyd9Qy0Zue7tqYum5hUpYb5nnA6GzGUf4MNS24yB3BBP4v-DGiQkY6ZmCG0X2KlhDnTDvbbQnYnzCrBJp4RJhL_N7T5WB0o3hVbWFwOBLHnwemjkHsYl4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ عجیب بقایی به سوال مجری: من فکر می‌کنم شما حساسیت بی‌جا نشان می‌دهید به ادبیات!/ آیا می‌خواهیم به نتیجه برسیم یا نه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/658825" target="_blank">📅 21:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658824">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای شبکه ۱۲ رژیم صهیونیستی: ترامپ، در آخرین تماس خود به نتانیاهو، گفته است زمان پایان دادن به جنگ فرا رسیده است
🔹
نتانیاهو در طول تماس تلفنی با ترامپ زیاد صحبت نکرده و دریافته است که توانایی تأثیرگذاری بر این توافق را ندارد/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/658824" target="_blank">📅 21:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658823">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سخنگوی هیأت مذاکره: هیچ‌کدام از گمانه‌زنی‌ها دربارۀ متن تفاهمات را نمی‌توانم تایید کنم  بقایی، سخنگوی هیأت مذاکره:
🔹
در مورد زمان و مکان امضای تفاهم نمی‌توان نظر داد و باید اول منتظر بمانیم تصمیم نهایی در داخل گرفته شود.
🔹
هیچ‌کدام از گمانه‌زنی‌ها درباره متن…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/658823" target="_blank">📅 21:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658822">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4339de380.mp4?token=sGH6C_IhyhzYt1JerjBK4yU9Pdub0snYZqmNC_FrEeZPw3yWUeEfoy7Kz7rCHbOAiYwR20BOeJI3INWNU9Fas5svSeeMYnDy4ogpqy06z4b2Hq9XrmhcklEvU1dMwSwa32Wz6kKicgINqAPdQUU6SWNuRHj4l4lvwvKvRKn61z4sjY6RhxxA9iiOKU3UH0Ds7yEaqQMYBA7sOcCBMU_Fow2FnONbpa4mDYTn9mLwlXkXGZQvWM63nMhRn7s2HbM5slyncw9eAH7YPudYwBn1YZhdhqY3NYBpSRf97VwHyPrRxdvrHD-rLvk63lCjjqIYVjqacpEWPaqh-U39NL2PpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4339de380.mp4?token=sGH6C_IhyhzYt1JerjBK4yU9Pdub0snYZqmNC_FrEeZPw3yWUeEfoy7Kz7rCHbOAiYwR20BOeJI3INWNU9Fas5svSeeMYnDy4ogpqy06z4b2Hq9XrmhcklEvU1dMwSwa32Wz6kKicgINqAPdQUU6SWNuRHj4l4lvwvKvRKn61z4sjY6RhxxA9iiOKU3UH0Ds7yEaqQMYBA7sOcCBMU_Fow2FnONbpa4mDYTn9mLwlXkXGZQvWM63nMhRn7s2HbM5slyncw9eAH7YPudYwBn1YZhdhqY3NYBpSRf97VwHyPrRxdvrHD-rLvk63lCjjqIYVjqacpEWPaqh-U39NL2PpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواداران بوسنی بیرون ورزشگاه در حمایت از فلسطین، یک صدا شعار سر دادند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/658822" target="_blank">📅 21:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658819">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSXnez9JkLxhv4WPQnSttAGjWC0ntHbSGVtFuEQPq30iZg8bTx4QXXRlxBBaJ7GCVYkrGf1j78JX38ri4N62x-K7k1gL4UMsKcGTORisSpdG8KXzRQ1YBZp_UGOFjGH2vQA3u6_84Z2Is9p-MVJc2bxzr1XB2nuc2mqXyZUUHSkZnpLGwphDXEoGutog98FbVJ9xztLdYeqruZcodVyUJIuZbGctmJA_4Rt4LiQ16Z2GSosCfTmTNZFANzJQ3O-mqCpUL_v_Vp69d7mH1NaOeqRK4rKWzrC1YKGUcejegQmVvoigkw9lPeLOw0MHrw1VWbhMt5TWBnqZk5kfqOArjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQdpyTOtkCku0F6FAr_Fr_BLKcGgTycLjNHdK_1KwXtiTh_5IgTm5dWEtEcA2wgsYtyXuJ6WWeN-LapAO10aMRwpTpb_-6Ey1P73ayTi3smQ4OmW_KM2szbPYmUUz0smG7tVUcZU2Fm5rrWRfi8pRCZj06jdvF7K6H47O9GHfzQf5aU3GOkk7XvKZUCkh3ZhoCn6HPBhmJ_k4qlNmqDWHDqUT3z37zRy_0xb97FAwP4f0QIsGu-U7JXaMYs6ZOifjTmUAMTx-62qV5PAA4O1OWJliB4dwQ4P2BaE0sQmHtvEaCkZs5_MOFk5_r5t96jFrT3mSTqn5MGjBJlimURq7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9299515ba6.mp4?token=AjA9_eieXXizSlqYTMc4p4nwI8Ipz9rqEPC2XZ_ft6eyXTdW2F4fY6I2Bh7iUNx0UuYvVm6SPaoGgMj5Ns-LZpKLIeDdF73hz0x2xaVgBLXyg4a9lC8m-oqqqUkyBOdaDZy0qJ-FMyNTqVfavCB_w-54n-mLMCO40IKVXM_aAALFmxLVlXrGIZL5Zh2xUWQX4uI8A2kw19me02OU_bqQif9NTDdSg3NLRHGkpKT2txKcgtBNrapK7zwHf8b_-FK--DuUj59lZiidzUKuc27q2mZH5nYW9bcOtptW9JUAF8wn8fOwmBkDJp8ynoh8YPzkrYSEd8GO_MUV9T17PDG4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9299515ba6.mp4?token=AjA9_eieXXizSlqYTMc4p4nwI8Ipz9rqEPC2XZ_ft6eyXTdW2F4fY6I2Bh7iUNx0UuYvVm6SPaoGgMj5Ns-LZpKLIeDdF73hz0x2xaVgBLXyg4a9lC8m-oqqqUkyBOdaDZy0qJ-FMyNTqVfavCB_w-54n-mLMCO40IKVXM_aAALFmxLVlXrGIZL5Zh2xUWQX4uI8A2kw19me02OU_bqQif9NTDdSg3NLRHGkpKT2txKcgtBNrapK7zwHf8b_-FK--DuUj59lZiidzUKuc27q2mZH5nYW9bcOtptW9JUAF8wn8fOwmBkDJp8ynoh8YPzkrYSEd8GO_MUV9T17PDG4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از مراسم افتتاحیه در ورزشگاه تورنتو پیش از شروع دیدار کانادا و بوسنی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/658819" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658818">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: سوئیس پیشنهاد میزبانی مذاکرات ایران و آمریکا را داده است
خبرگزاری فرانسه:
🔹
وزارت خارجه سوئیس پیشنهاد کرده است میزبان توافق احتمالی میان ایران وآمریکا باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/658818" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658817">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
خبرگزاری رسمی اسرائیل: رهبری سیاسی از ارتش خواسته است عملیات خود را در جنوب لبنان کاهش دهد تا به توافق احتمالی آمریکا با ایران آسیبی نرسد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/658817" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658814">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhKGZvsibYbUgulwfyczuR5Oq6pb7f1FSS4As3FYvLg1LmTH8IUXlBFa0q7-iwD-_gPUnHR4dp-uzT1PNcTqZnxWMGPjeBWAY5M9fNEZLIbdT3z7_QzAE0Z2LlKQjUTGNb-FprBeuZYoAAKUBkGdBpvRJIonmQdOVErgGmXniI_YWnDiCCBC-vLqtYUC1Q_0_0QITKo_XlE2l-153cQTa_QjktbUZyR-46EY-G1WCMA35WxnBc3kI_RZB6PHf-BHQswPXGLbnWDyIfceA_NRHW7NGWcftrcGD_3ZYEq5_zJIm0DeGo4L4s3qXoBTRhkEYlIN-o4jlijFJuBkH4vYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: ترس ایران از جنگ ریخته است
مجله اکونومیست:
🔹
درگیری مستقیم ایران با آمریکا و اسرائیل به «واقعیت جدید» منطقه تبدیل شده است.
🔹
جمهوری اسلامی پس از مقاومت در برابر دو رقیب قدرتمندتر، جسورتر و در استفاده از قدرت نظامی بااعتمادبه‌نفس‌تر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/658814" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658809">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K74H6gCdx7tTSvyN4WxGXurtdndwxi1xZZexOjc7EIa7g_bJs5ZyM6ywzN2-Jy-hk1e3bySZxG0K3HmfmJSHFuJrKhli7MapLk1AtI-i5EDMFKRcin_pMLsxdKH0NA40p0YTKBisKeksFR3tqXn0ocOFAArPc-FYaYs732U3OMhXYCMMFZAjR2gAM6wRWphFtTPEy4Kuw0G0bj2eJ2o9PJxWmPOyyD4I2TE3e9HpjOW3RnNnh4VfcnP3iz1cZhCbANgRXkhjI5f7-vsQuyiiqjybCSXkOxamPabuzuGh_4YSTxoqD0ylKAzpAYgXTDSpX40tBCPKtwpLy13nyWhWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8F4IbZKYudSXg1haEbynZWDIQLJbLKUM_p01jL942qsDOkQNCsa0hMBrb9TP4x8BCKlOa6N1DLh6hI82L3X9HbgCQJLTCV6lmPv_IsTqKaZOj4XVpNAW8yHL6zSdGZ-1oveBeePF2lRVeBLk54tziOR6Ky7IdBa5H9WZL5xwlcbsZ6t4idYwBkM89OL4Ifk2Va1w4Cmf06KyFtA8WRhlP4x2pT8IIlsxpc8cXTuEzRn7E9mUqPsP5SNE4n1k8wLpucSZTAK9MJfvIUWNupdtGSwOVM7JBnQlmU3b91Ms84T3XRbeAahE_F1E1dUv4U-U37OoNQypGwAahAHTXP6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNLAWmlDtz48lLESEqKlvZfgGHOr-idB1-PjfwwKUgTSoNUIiGD36JjSTiuT5JHj3b2cQbgl7_P3tpx9KS1LftQr1lxQroVkKiuJjDrN-pQiqkTWapErJNg_Mh2g9bNF61tTqGnuUkUA6H-98G1VKuMksppmsmUej5O8-w2pHYCXAIfFi9nIqldEtv9TU6A5OWtuT5a5oghbTBYCWpxog3A46tZDSJBZKGOeKufnm1A4qDAbenyzfDACBkuWxU4Pmg5I_gMqtZBCc7jrDPyDXM3kofOAFjvX23PmrH1-TNu25PNgl0mKGcSbVtGvoEFye6wwB-GrPH7c2ZK-_88mAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEaTAourWvlGQUMZgFsE37NOR6JYjDDIzONcZ-virqmite-j4CeTV88WURNOGQL9Xg1SIad_hqE7k6d65o6YNTgjk3ivZQPg1pPPaPMfWb09hKAR5QKOAo9QhDFSxcNoy-ncQdC_2miQU8Dszjj2IJBhxj8inUB7rlSkwxS02W32KW8Hbsz-wpHWTyaf39jCu9gSfYcqIqIo-A8d5AHSq__WmNK60EXshK8uIOC0j5JKlZGqNoKN0kbcXoNJVJ8vuF9zhOXLyenZW5EZhkqdSTCQxgXI_0ofD5-Zz5zaI-6HqYCrC4tc1TbUCC5xdiT8VzGQLCf0uzy_eYZnIJe5-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3KwkKyMttFzgsLtMBDfsNkwKeojZrqBvEdiEDvTJUBz_HUoO_y6KpzBs0FvL2CHwHXQCkRV9q1egY3RgphsQC5CJ4AH-vhzVGv9nOrbBPD9sD9-a__E6yHKFLD_EYX7w_mg0lmcUjvnEb0u1qYZXNXsXK-9C5pv6n5B4283OrIXNC4auUn4QsVEUBXtl0BE0xrt8l3DFIRyd9Sym2iI5rMqvd1ZVHaZSsyAPp53azHW14H-WNPLW_fbr45Y0w0579oPC1xBZ6GiXj0p5wIoh_wMnGjdyfs_LSLdRvKTygc9rVjLokSRF6eyaQ3kPIZ06hA5ruN2Z03BzDP60TxbwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زنگ خطر بحران پلاستیک در ایران و جهان
🔹
بیش از ۸۵٪ زباله‌های پلاستیکی در ایران سالانه به دل طبیعت و خیابان‌ها سرازیر می‌شوند.
🔹
همچنین، میزان مصرف سالانه پلاستیک در کشور به مرز ۲.۶ میلیون تن و سرانه‌ مصرف پلاستیک به نفری ۲۹‌ کیلوگرم در سال رسیده که زنگ خطر بزرگی را به صدا درآورده است.
🔹
این چالش در ابعاد بین‌المللی نیز دیده می‌شود، چرا که نیمی از کشورهای دنیا در بدترین وضعیت مدیریت پسماند قرار دارند.
@amarfact</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/658809" target="_blank">📅 21:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658806">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سخنگوی هیأت مذاکره: هیچ‌کدام از گمانه‌زنی‌ها دربارۀ متن تفاهمات را نمی‌توانم تایید کنم
بقایی، سخنگوی هیأت مذاکره:
🔹
در مورد زمان و مکان امضای تفاهم نمی‌توان نظر داد و باید اول منتظر بمانیم تصمیم نهایی در داخل گرفته شود.
🔹
هیچ‌کدام از گمانه‌زنی‌ها درباره متن تفاهمات را نمی‌توانم تایید کنم.
🔹
اینکه درباره جزئیات روند دیپلماتیک نمی‌توان صحبت کرد به معنای نامحرم‌بودن مردم نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/658806" target="_blank">📅 20:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658804">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ترامپ دیوانه گستاخ‌تر از همیشه  ادعای ترامپ:
🔹
ایران به طور خصوصی به خاطر ارائه اطلاعات نادرست درباره توافق عذرخواهی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/658804" target="_blank">📅 20:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658803">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a93427fa.mp4?token=R6HwDQr4mlFVMWTX296K9HMSEsZIDMPcV7UpldPEvMVAYryge0mGWjYRjzH_s7r6BcXUHVYRO-L9AxTHcdEYU9MViJssl_tiUFurZTfpUxNIWM-wBWZORHw-RnSlcCAxIUdqy3HFf_ozCsehFEJAYozjv84Y8EhA2XKwt_0u19PHSaUMDBnhhbnUUwX7AnV_-1eCvJwcWLLjr9uPht-UYc9nz3CsrQMCWgyNEmHN5OgqOXhAyDet-NnRb23ocxFTPYeWZozKwjvOkaRhnotDHdIk1tz-730_XEyzMSczAZz6Owuj4gnfnlLzEsdpOp2mANqwNVe7FCUVUlfkdalMAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a93427fa.mp4?token=R6HwDQr4mlFVMWTX296K9HMSEsZIDMPcV7UpldPEvMVAYryge0mGWjYRjzH_s7r6BcXUHVYRO-L9AxTHcdEYU9MViJssl_tiUFurZTfpUxNIWM-wBWZORHw-RnSlcCAxIUdqy3HFf_ozCsehFEJAYozjv84Y8EhA2XKwt_0u19PHSaUMDBnhhbnUUwX7AnV_-1eCvJwcWLLjr9uPht-UYc9nz3CsrQMCWgyNEmHN5OgqOXhAyDet-NnRb23ocxFTPYeWZozKwjvOkaRhnotDHdIk1tz-730_XEyzMSczAZz6Owuj4gnfnlLzEsdpOp2mANqwNVe7FCUVUlfkdalMAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار شبکه CNN: احتمالا ترامپ باز هم از ایران فریب خورده است
🔹
این که تنگه هرمز بلافاصله باز شود و حجم تردد به سطح قبل از جنگ ظرف ۳۰ روز بازگردد، اینکه محاصره دریایی آمریکا و برخی تحریم‌های ایران به عنوان بخشی از این توافق لغو شود، و اینکه تمام خواسته‌های آمریکا در موضوع هسته‌ای تأمین شود. این همان چیزی بود که ما گزارش می‌کردیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/658803" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای ترامپ: من هنوز فکر می‌کنم که توافق با ایران ممکن است آخر هفته یا دوشنبه امضا شود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/658802" target="_blank">📅 20:39 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
