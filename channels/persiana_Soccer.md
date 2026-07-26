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
<img src="https://cdn4.telesco.pe/file/ndtSLrz1COmALWAWEzqQRhSu4IPiVLMHp8zBgunBsh2FfAhH4YdIx5Fw2wUZr4JWQdw_zFXm_Ypvv-VbTmoczi-9PwEQoJ-2j43sk-tdvKdzdA6ysEkDDt8QJR7G9GGJt8DnjpyGHXrDbeWrV5eDEx0SeChFqg6_a9b55KyndRg3TyLYbubHfINyIlrkpzmvKu680ssIWZnumsCbasDiYBw2C2PVhGAz6tQ4mEUZd-dVATMe2WKoaTNEENsNwmojsCSgg9ixByxOBDKzNXZJOvCQEf3078KsjCfF2wEoe_qj9uRMQSLFzVfJd2GoBZX2M6BX-tl7K2WDZf7FENsFkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 589K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 20:19:44</div>
<hr>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TV3Uyn81n5NHSkuLu8bNggPjn4xfoTO6dBzPHSHqnZj9xb9ZMxK_SX1qCn5GcoZKHB3-f-9hsAdTXPDt1cmzMumxEh5mm0128eHwQEGcMbcSKlXvFs_oWfyEn03_5hZnyTNjezJ-194sra1m_FcWUwFDGBygUkJw_LgTTrxQ9xMd9Fr-oJ5wmuBfvdcBpFzXCPPACuVS6lEIf6PSpeehCMC0krf96uyfv5f8fi8dTQCh28wNKStEdbqgbxqNMewe3M9EVpMDfF4YoklDBoOd5sOuAdvM1eA-K69VUYqSYYu503RVaLkejkDElYgyP_1MhTBWYKyj6JADJScXrCQ29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=hucH-4UszKCQDzeNK6sl85PN3ijoVwh53UvAbHpaUW8Vh-JPfBvtY0cdrpOACNXbpGEcXhSi5aOwKbqarEQdQ6cAWsJAU8sStOcDFSNiJ07mdp1oU0a2xRH-1IbSdy6j5OSaa7_Nr6ACPs4Nl8WwSkZDSWpPTIz26htFrCjpKj2z3pZeSwI-t3pydhfT3R9-45NPlXZ9mbRVomxSeHQMRm2F8JVM2_iEpUMEqRKVIryUVhUS_tcWFGRvDxn_2Aa0sWJTi0o7kOPCdTYXKOiypV0WIloOyoZ83wSiL-Wvlu95Ti4h2f5QnA8-JccbU0FKVY6lmvN7v9rFFary8EBtZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=hucH-4UszKCQDzeNK6sl85PN3ijoVwh53UvAbHpaUW8Vh-JPfBvtY0cdrpOACNXbpGEcXhSi5aOwKbqarEQdQ6cAWsJAU8sStOcDFSNiJ07mdp1oU0a2xRH-1IbSdy6j5OSaa7_Nr6ACPs4Nl8WwSkZDSWpPTIz26htFrCjpKj2z3pZeSwI-t3pydhfT3R9-45NPlXZ9mbRVomxSeHQMRm2F8JVM2_iEpUMEqRKVIryUVhUS_tcWFGRvDxn_2Aa0sWJTi0o7kOPCdTYXKOiypV0WIloOyoZ83wSiL-Wvlu95Ti4h2f5QnA8-JccbU0FKVY6lmvN7v9rFFary8EBtZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooS8sSfd_3a_gFTvVI33Z9OVKF9tXlDrnwSYVoeRSceCkFBfHoyT44KhGS6r3HDnViWfkGHxPVXofz-VorJ98jab1t5BsEctVzHzbPiHquqgAvjhp8wJE-lplrrjVli8yV_p1nM8zWoT4dXCiyVwq2kZYrCyop4GDSu0IGcAARNW6yMK6V6tD3NfVwHpT5qMq39XYSzPvZD32q7V0R8wUZY4tbHjLBypIPjhedkWf-r82HC_KVW0G5V1neLY0bYY8PbFF_7quh2OmB-XmBFXR0XMluZNt__Q4pyF7YSWCtDgx2aEw8vYxCewhnRajPoQN3mqKdD9z9-z_9XG2Cznlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=Prr34NRaDEQlZsXpAVf6w4QQMe7N05hshoHKZSKuy2EbLyfDjusFEOioANxjDo-g2jy4M6Yixje1UrpH9p5Vms3c5TxhR_9etmHDaeqh56tCntmSI0qnvu8MZ40w_UgxcjkccLRACYr3SryeowJ3V9bBIbfMxBhnPZ-fzEpp2yLu-q9nRlQbGmGQQqedCILNqtA_PfXZrwRD835vAo54mHjCYo62y8kDP-hi4CmfYPp2GfJGQNQW7HdCcBPi350dFRaxD1Fu2K7bPgd1IBQNWriCjL9RqLQIrYvtJSqzaMxQe5qHpZv4FDycq0mpqhZR8knoNiBNgNEZvmbffgpchw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=Prr34NRaDEQlZsXpAVf6w4QQMe7N05hshoHKZSKuy2EbLyfDjusFEOioANxjDo-g2jy4M6Yixje1UrpH9p5Vms3c5TxhR_9etmHDaeqh56tCntmSI0qnvu8MZ40w_UgxcjkccLRACYr3SryeowJ3V9bBIbfMxBhnPZ-fzEpp2yLu-q9nRlQbGmGQQqedCILNqtA_PfXZrwRD835vAo54mHjCYo62y8kDP-hi4CmfYPp2GfJGQNQW7HdCcBPi350dFRaxD1Fu2K7bPgd1IBQNWriCjL9RqLQIrYvtJSqzaMxQe5qHpZv4FDycq0mpqhZR8knoNiBNgNEZvmbffgpchw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiJCH_9-o_I-KfU8hMwx8RminURe5qgAq6RNNdCIaTyY-m4g-PitIBtZmR6hLRJvfycAV4Osf3If2QusbKfZRbvq3e99koFFdArUxf7euPGkP1jdEy64j-KFqkpVR-0xq3KDBKzlzRJmh45-F8awq5x97kehKtn6UP0CzVnQVwAAp9A2nmq8KgHIBWJWseQxi5mtGmkmeTiz0C2WvB8x3j0AD0td4hNWtXhWbaY2fkQv8Svjn5K8ItxBO_eTZhKxoFw3p9EqB8hQhEE6PnXgv8AYlqw3Lu9gwMmWx5HgSP2fDHGlk0fIv2pUVlxt4WMTdgXKLyqkTs_JV8ldxd7T8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzrnZc3PF2ZjbenaLwEfwRr0ifU95f-LXQUwROkdIGfgcy7x1tGhKqZE-qYJjQpNM_ZLNnjas-vP89S4Fdnp0Euw9Laf1VtGcBHshDSBq4__4Ij3RrK5kJvGypp640Bl-6VG1B4cTdw8G-G7l0IA8wzvZ42POH1exwv0tOJEDh7D4zoYgtk01iOrsEm0Rr5XRuaNdRSWgfbRTUclTfO5_4CbGkipFhUYw3QcchpC_7t7S4qEdgp9JvGlREQ8mmTHFjgkOBv4zaVYmVJEIk6Lja5vPBxvOvBCElkrg80AiMMxst5-diX3HfeiA0_h-MLjk8TDv2Pso1599KHsKnFVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKq4T1vZSP1je--aJiVhKfRaQfQR7DEhhrRZPmchhLHIs8VRwCuJIpeSbAntHFaEt1tk0ruB6GXh-h10gXetHvmA0ovMzo96dRhPpUthpssIqfm7i8d57d5Oz-INpKiokqUBHVop_sgDt15GUTjj_dPZ2o7v5kZ1cu6gcxKQvtWVgOFEEFYjDgqNQ9YfZhcp4B7lf6tOuX0yPuKO64DNqImDm4yhSlqF2GEmCRgkAOxQDJNDzAU5QYzbGQ4LL72qiDYkn1O3Ke0QRklaNG6ISLZAWn_uc5uQ7P1ursGPGRVdCUop1dnoVZMGqfbOa97QKajG6kTkLT9-N1QHdRwN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrIlwwzjYCy-iEpbXe1UdW51TGrbHy8uLuod6Xo9JhYlmBRPuZFNKReO8kl4uXt1ELceVv7vsrJ_sEQS4CfPpOyq0gFSqMmD5Ps0ia2XimAogI34cVEVylrou9Nfp5_-Uyxt1woCK9KOuWK53uhNGEipy1yLr0tPW2CFeNCtGfjP0ArEOk6q5WUsLzU2qIV5R_jx1tQtPPRR05uQfMkmALwB0fbkN2yl1-RqCIJ4ouGRW5TOZLrvUQ15EobCmqAt02E-nFhoKJi4NVwQNH6ET1syUsCm8F8h4-pJWWWgyWXgL07oC1A5xRFVy-nABLabASH5NFmsspUBT4pShCnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2VW5LJvz0BUEUutl19NASI6Boupbja26bx5avyWVUEeXIRrVN6G8tVQCaX9aanxLeJ9_YOu6hFTlyofvG_gOM3gW3jWd3dZR0me7wx2f_lwp-LOEsA6DgCxqCfgmzrMh4V1wo-8tyMmXx5QWADxgJn6Vf0axmt11OJF8tPReH1D1nmWOu-9FuW-pBOHRCJPjeolWqlPWTKAmyvATvwFQ3EQVK28Ycnwq3DOjYZQbw6VI6JP0UcNM_7MWlRmXJp2TWiQiY9aIV-QBhfjWiNTjJXTD3yMQfsMN7LRxTs5A_YwlOwnvR0uvf3MyCA0Th-uaRh1nGVDvMD6xR6rujldPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_sbgI_3m5iiuF1qwdZCCWHQJDzRZydvEcz3-rQ_U37iX5Wqs88AaDA7ApNZbGxsZiWe_8iitLuQq0y_d2GCbTyiVMO66kG-mY2sZ1hCbyWpTB6pIoS_si6rMCBlPeElp1K_INKPjKLX6BQAW8SQBS7hyUSQgKtYZsCtqz7lwpNmzMXOL_WqpSsttvHBkzFBX8HN1OUIqB8XNjI2weCRQ0Ml8P9kXf3hPlR3czJ2AimEIyMKtvH3Jcaq4BxXwo1wqEJeQMpIyy06kpvmFUKVKZzvSST-QEFmrQyDr771N-KqkaNTI40WqNPVfL9BfsPIxjBYTWZVZZaGKHjSTzxceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26553">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spAe5Zw4JmryIT7TSxJ4faMuko2ehzuzV_gHzfI1eVeXEZgEkHAv5jRZ5lYH472lDzfXvMbe9YlBFV1vMeDC2g_0BpCiqgitkAYM6cP_CzG7zF-NX8CQ5tGW4MmuK8sHP2pX4GhV9Nvm485w8XxSFPUt1zNhjiQZlNO4oHFQvnIsKJbVPU8u8befCldC45RLnzfyVKqtnBZi4AYZFVGd8R86_duQOFbAs7LpdHcN5gpOlbwIMKlkFagQUa4QFB_3uCBfES4c6alZvj1DQu6tNswQp0IqFzTK5ZXHUx4BFA4qhUqqpWvcqP8kSzH1v_dNYxqSy63pKLMhmEYK2MwqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛همراه‌شب‌های‌فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/26553" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFyIg9yz0mLAbJarvskX-v6b0-vGO8fs74pidC0m9FfjRMcbS3PGev05929daig8YJUsFFMnKPmbboHp4TvHGhphGbNNP7DIuPoasoSak-LfpYu07GjCAWAmwn2ug1Vmjxebm6enRy55SEsCitBaMnXbglLqic6nsNwMnd8IPlZyTvpPtfI8ehEpMY5xwmUtBTd_lKBEwsb-hKHnirNhZOwPfTnBrtwSDMm5C4WsjsEVAbsJhkFPY8GgkvDgjFV7f8i0l0vG7FycBLYoZ2_lFYbXPxlhakwNaJnX2ZUHYUyhfZ8xQj4EFrZQ-Bge94iRKfHIo3Jxf3FJpKp6LTG15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjkJkh0qjA_6d4vkFa8nhklDpj6-vu5CknE__AK4VkZxn4et3YjOnLEwgNLDNecKj3CwHaHl4cinPKgFPQy_8ivDcZ9xA-60YNiwFLck6ZaMMgwmuVU5BPwzpbwpxI8QphSP3PEdm6yOcPtLJTjdHsZMeXQDOBpHik5N0FML-KOUUBTuFW_ctJLKmXTI3a0jKtbhjaxXGIgNquQNuh-qqoUCT3oAKx28rTMu-ZHrH9fxBm7UbCudMVbSt0sefxk3FvBJiRgM35Td48CBWNAL1vsAyUE7cZRPNGNyZ1DPb_eS4Zmqfoo0Z2VY1XMFFG9jvLyn9jWCFWKFWYQaZPlx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWoPgrCrjqds4K2MQoABNBGV6ivdfKIznpVvNneZnNmdqve7YVYIt71shdCVRadwIa1VFsnQjGuxyK-7svyOHsn5YoRt_WYfLZcqdydZK6YwtPJglGwuitJWXN-iMBfXwMOHboDHtItBp6RecWPpZZpPrSDMLDUuBB2ODyU50_YjP39qVuF7VLKEt5BQ8TajfHXe28FyqaYxzWpu0diL55d2ljO8Czusx4QG6LQBHvix9sGM-qk0i42siYM6ezBqjSGJjodQzTYZqovw0jdOx2alVGYgRuIE-0Uno3MaIttj3PEGoYRx9C8IM9bL2Mf0vvwKKHL-qBth_mAM0DrKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LElJA7r2XpTHYq6qzGDo4YfuKN_aUJTuyBSAmC-XqXYOIZxL6dx7inq2qQ0Y8Y6ubt-jwUNEgzPEmm2fFLPYKROYVAlxOlNgSwL3i3K5ruxrJysN25oznwcUBzrK-gWOVzVfSTPEB-Yh96YUEVMOuhlLjxBAFKzEXd9Tlu-ZPFKOoo3yfgwnnPSVQzLDI35ZGU6XWD8ecy-gGix0E2_lQcK65AvEiwig5eDE8KT2mPB96ehN7fHhnxlTQnqrQpgYyVkIS7MQljcOfwZSmgk5_j2GadpUTiaJl1kKeglxRXX3jUXbR-0PhoEt_nuwGOY0ctxW9lOs-PYFTA9PmM1Jfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOVkt5oWbC11Gtq8YwTWAUq3XmCP1D8_VxYhNGsSIAEXYnuta6Dswv0QojwOqGqdw2gOoLkZCOLY6YSNGTKHOaDripBMiAGw87QfaMelVNghDWeZqqAZOFYwqGG3aHaQDUjiUDCCNalLdA6xeNPZtdHyCGlEU9yPfW-6imxMjjWHwmrtfIs3nbitxc45SGFUJ6kGLhdqovFW7fkkO0aPE4ST7plrAJkHO1Z9JMamDX1GuhxRt1Jh6r1mCqJpx_c6SRa5wEJUDahw1O2mpKLFLNthGyLESSAe0clTVtGjuGnAd9VW8jL3oSvG5z4J_HrqjP9i81NfYh1Wf7mnlMg6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FASUWGNvYl_oCB02AJoVO2SqKjSkASIQiWOlXel2FcfeMAhViXL7YfZ3VYazBgE8LdpkWKXz5xIha7_JvY9BzEymRDv_3AOKrvzLs0eOuiijUtsdbnrdeyTdRUHC2bsmpDjaXVTCTiLu2fCqUUZQOiiJtd2acd_YZpFQgJRdOP1tsdML56OlctGe5gRilYKx5AfMtEb6JZMkwgLGT5Efr8kkok3SO_uYi8qCiz_yGnwJXR1CjwsdjCy_4Wxl8Q_OLMAXMFhkCzW69CHgETFE7u0YNmrkadUQDFO68DkkmIwXF0P7LZDba2Xom23RWpXD9HFk3pXhGSonbw8CKziF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpXz2VhYRwVLswKz5WCKkVjGJ9wthITakWLRs-dZ6qBZE3ZH1omwizDT2yCkWMgsew_EHE1s_WMFS7ge3qvhtVa3WQqPsFGvJrTqamZgIN9Y2OfNmmbbX7JS80iBpoeRdoDYbSgnJcX4WEjwmtir7HPjICFCDag1gFmBuLKs5uSrO5_hxdzgpa_LSYqgzmm-zZgI_XQw5Fd0w-NugxkFIqwD1RevQ02q_8eFdbDhKt2n-L19cwW4DCh-AzggziInRk0I6GTlaD0Zy8Al3Mkz_RiLSp6wzZ4JrWTjPdJIAet7RnbXd-kbrc-LcaUdjZTKzy9_jmW_GMRe6OFSSrvpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxgo050yNTgmG1S6slg__7ty9lhixPzR8lPW-Lpfsvs8PtwUv44tVPzzvFAvEy7Tpx1t8K5CWZK9jRqnyzBVboNZvqO-muQT2GwWvrZV-TvXJQ_SBRb07igaTXVhjLoNxUgu6sV62VMlc7A5gHiP4mDpi91ObObhwA7yje9k5-an-HaJKo0qCHiMG_dDiFTNYauxMvUva47sInY_UbgWsBjjya_gvEw3PflUX_yFCl8DrvLeMVYGqijazECWuM6OE4WzacjoLqdM65zdy-WOBf7vDWEuN2sj-i3TEq6VWCNg3JcE4WJCKGPGGJhaY6vIvor1Arp22F1N83OZ0G00bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=XgQh1WQ1IKn-a1Ule-LdqK6NfHwofH0ZtLktaA-GusKRHNdfYSRyroYWoANI_USQ6SvDvxHexhTJ5IoA1kESTbeyDmvlZxkAbpMD9M8S_WsMLGxt5jJNyzgYlhnX6BIVojcao6z-2E2ZSe66inJi4zd5vTAu9CBUrwpW2cn5BZQN9TRZJQsJtrU0h2Nc9ufMCGsIj8EopIUHLbiC_NyaSqa1h-uvmIZtfQTZhnnDUsoYhqwaaRyKxCOlwgBTIzrg8FvTTfSEwAG3n4ZURyKzOmiUj6gs_h_xjLjsxxrHgJZEhbQS5lA9jUZDJDHMnfeXU3jhGvN47I06zfOp650TiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=XgQh1WQ1IKn-a1Ule-LdqK6NfHwofH0ZtLktaA-GusKRHNdfYSRyroYWoANI_USQ6SvDvxHexhTJ5IoA1kESTbeyDmvlZxkAbpMD9M8S_WsMLGxt5jJNyzgYlhnX6BIVojcao6z-2E2ZSe66inJi4zd5vTAu9CBUrwpW2cn5BZQN9TRZJQsJtrU0h2Nc9ufMCGsIj8EopIUHLbiC_NyaSqa1h-uvmIZtfQTZhnnDUsoYhqwaaRyKxCOlwgBTIzrg8FvTTfSEwAG3n4ZURyKzOmiUj6gs_h_xjLjsxxrHgJZEhbQS5lA9jUZDJDHMnfeXU3jhGvN47I06zfOp650TiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFmu5_aDKvq--XJSDu4WM0dxgqQoP7GUCNcLSurhd1T34O-3xCuOnH_3jMYv7rFQAK0exxnL16qjAIRRgFX84VEmALkjEerbe9TR5mp3ynl2-_sIlyuvPyv70HcfmvOfm1O-fJIRrg5hhkV-uvYw5-0pyw-EhjAPkWaoEU5q6FYStnRgZkyg-hn3UU8aMFnEnQATVC66-sSlECM1OAqC4-mNKJP1Ah-6WMWn6-6BjV7c4Qzs2prexBUz-0esoEbqfB2gjzy24UPYoqZwcwFXCxP1PmzPrYmyrCFNt2MDNZpwek2Cl7WV4XrJ-XU-yFJ7B_db0qKYIOqXR8m_cJV4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kvm7qMvBh54STpGrTFfPTJF0XUh75PqfxHzScoBQaks-17aQpEkXWcJxXD5CaVVcAjkF0PY6LqQaeMOM3A6zD_FP5y-t1Wf57h6dq5PEIErlIV4h1T8NckLujP7Mr5XIB5au4_kBWlcznBwP1dqCKmBHLIxw4VDxMOTLaX2ZgQWOSfg73QuBM2dSpa8-DlRjSpGEVYmiOGVBrcqSY0etXlh-XIo4slVVTAA5KDIclBOZUpAHZzmEwoUt2ahO4gJPEfwZNm_bMt3PZzBAL-S9poFrY1Er9RNJ8U692VYmPC-Vtu9bubgRPhv7mLnPxeUtWUjCLr7EzrzurD6j0CoF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGrBv0qw5EBvmsPZAHHiEaABL_I2s48PPk9qOfWerO8JL6scoGeJYAHG2IpzLqqlZdyQpkjGWDqjrbbYvKU77ickuz1tbZzQzHtWVZlzdjIkRJIIZayqFEfBGOEBZkTKn2Rrg9ZPTnPaWCx33O_3phPc2feERZ_Iu6BibJFdaOBVMFICXk6ARV1znu3SqJWCjQbFsmLL6ZSl6YL6OrkcHVGNoy2EWvz9Ta6O0IiK3vxw8h9CEB3l_tpzykuXXOraHrJnGCY2XIR_ASqPghJndFgidCHTtqkX0YwxU5Jl2v6hs8Y3WOpARgaX1CjPQbqfx7Xu6amHDeQcR3wpstEPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHhZ7GOGk4lYXHOv0ocxxgLOs6WZIEmBfkxzl-3GCTmmJ9YOvsX_n8CKFNaL1_hFAdFVLM_xQmSn495nXgMfkACs6lJvMl7apRQzlp7QrQO8Q70D_Zzxrz6VLKA3udnLGqFvfVsz5ePB3JHIhC8quR4rYlx_YHE7ROc4k7R38u4KhqSidVI8Oitl37YFMeTVm25J451Qg6f8t3dWGGfHVuMzVy91QbAG2qyswXiUU7j9u_aIj1aZMdo-c9V3crZJHdzWE7codyezOdowkkbtZ7z-1cJi5FWwG054qOZ1v40zuWZh-YnlfpMywGg8xPcXIl0P0gprBvwRt5z6CCR2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0MivnYc5fAW7cSURrI_dym3YZ1zClx78uaAOn4YRgO1qrwd5PDNTUP_Kff048VFRzn3GY_WrakKELpJCqmvDRUrsaNjCO6MgZCUUY-ryvZYkcK53h2reNcbboRnUoqXkqFxW-zvwvNQt3M1uWtyWtRswa1Wq6kSyzWKz4XR9AYx9JdnclmBgdDE1F2LRNu89KLLroRmN4-zbV7yzCeXWOJBFKj9UvbuDf_CvuQGXkEpL7QSY-Z4X9ZAofVuc317nv-Z0Vm5DWXxcXX-QwYFNrJHaOb2h7TH2KJC2Z1aD0DiELKDzBkil2A_aGB4mRPWk5_yCifajWRxUGvfNeQLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=jXv_ko_MxGJiCt85CHDAJlJJUhQ_BSUwsMEw4plM1UGOPTk252raEJA1EItEkc4pJ8FL2ccCybfogj_GarschHuvPZc8qhT_28irXOPeM2QcZwG0SgYtLOwbwAJPq7KjYCZd68TBtsMXL4kyorjRtcAGo-yJn-52wO8Q_UBk_Ee7Iq0KXG9c26MpEog-FBn3D_Frce3c2WgXrsK1hpwGrwkyBYkf2NR3FKj3dGIzLiw68o67-seB6E3f9S3JK_-R3zCemM1eQbk3uGGdH1Sc-z52qIxXwpqAKU34wfWL0HU7-bQ12ct2S41cokCvpfNwnV4AOEqPDV3RvtHLBVIKaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=jXv_ko_MxGJiCt85CHDAJlJJUhQ_BSUwsMEw4plM1UGOPTk252raEJA1EItEkc4pJ8FL2ccCybfogj_GarschHuvPZc8qhT_28irXOPeM2QcZwG0SgYtLOwbwAJPq7KjYCZd68TBtsMXL4kyorjRtcAGo-yJn-52wO8Q_UBk_Ee7Iq0KXG9c26MpEog-FBn3D_Frce3c2WgXrsK1hpwGrwkyBYkf2NR3FKj3dGIzLiw68o67-seB6E3f9S3JK_-R3zCemM1eQbk3uGGdH1Sc-z52qIxXwpqAKU34wfWL0HU7-bQ12ct2S41cokCvpfNwnV4AOEqPDV3RvtHLBVIKaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLH5r_5UwR-I3CpMpZUUzNe6TYlRbdvnnMLjHEHvNCWoX5iYR7ASx0DgdVgtUZRui3yPEibEtvhiUpBadT2ROnCpjWFguvrlvn0x3897J_JZcFlQqbGtf4MRmpuiWN7ICe5Z-2pR8bHA4NXPk9mSV_2zQYGP0I7Xya38YrKAV7kIlrU7efGA6gbYFREWKIYBCw01JehZ7uJlGxSIenzIDlZHMdmtsr7mZauPnQ9zhsGPz_X103E8HmKgl579_8bNDJbYFj-BxuA_O8pVR7HMRpCTRC4tz-WlwGk628rIILKzhCoNvBnMOExRxNFH8C3FnOZg1T8QxnCPPbDHjhosjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlEJUULg96XRfllX_t1u1NqxgdgS92Zw-TyAiGUTC68rziGg7iOJVzqRwYVmT09SwoM2_ZMT82Fk1GnTg6cVzLRIB9XE6VnYvrIeDCCoUv9vu4kodPjbjyFBGKTfpSkdxUDssemjTMPkXKppIaV-rDyDzejvDaIiwe2JWYS8ynxsvhD685QFGblTQQrNIct4EGK5JgZ9jcVn8fgUDEiR4Mw0I23rIvJN8eZxUJ4m-K0VE2rqZfBzhvFGxgauVrM-yFwdYqO_Gk6C067NIzmKSTN8BLoMDWLZQTH_tLSY4MB_E6rLkMt2oD7Z9LW5PfXsXAjGy1xMD62Ab_tOyfCayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKwbJg56lV7ImXE-m0rUzCQmEgs90EZMNSYQm8k5Lm1W5BDHFe3RpNK3JdESeLsuqYE5e8OuEyhvYKbc1MVHgIppIcuSBTSqS2i4WwxBI3ULeyfAnGmarV_mwPnsGP4LlhahWYDPusm0-x-ZsiYHHeIr7gvhG4uwbWmAodNu1fMky_GetYQQLbfzlHOl30Z5KKlhbp9E485I6ehihhBw_aU8pJe12esdmknzDPGwIrvBbUbOcq-nnkgifgEzrKSdW3_BhL2GedfdEjXOELoVeFbUc79qlwVBwfVtJgXzbINUR8hGTdrD9AoRzv8Nz_yuIUedYYvGGY6bE9xMCLGUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtaOhdKZjS1qvVYdD3Zop-Maf_n16mzdnyi7co_NfUz_DVxOyfumHyaPxYFjC1PE2ReqMiIWZNFMBfRM4eACwhikJOoRg5IrxjwjEKVSiJ6ggcnJleTr22ZIsdU16R3eotEok7WAAqQQbvmOGiacDlkogzKVFEoxZ-WP_KzeK5pUh2L9D3iMChwDHPy4ezZ9vVp9qVrqYN-NsKb4Ha4kenoHWxFpqNkdE7xGiE7iZV_pd7r69HQvZfiSPjNr0E5QeVRFd2nr3RrxVAdGF5DDnFw0RkbraPsYvs09jKRw012DDLYbAmfmmBa-_EZUNnZ6ARyyvp6Qw5cUyxGOZcEPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvGhYJlW2rsTl80k_IfzbsWVnr0jTv7NdJ4DiAzqNBg8PhrIXjLhpkm7X_rCzF_PAFDSWs8wa3iXkPPoZdtGzo-1R7x9bbM8Kpneh70xAhM-iFSi39iFf4hV-y3z-UtWtUP6bHKd2HiyhifJvDGD2Dsqwr1QUgBbhWWT6DW61x6kMLt_BLi5ygnrG1Z7epmnIMNOITr_B7YGfKd2i6KqNFhxtJIwtTa5pdaIOaTL4ZuoM3LFObChCS_7N-aQw8FoIIOHeRyTqo5-8WIA7mrlLSQp2nsV3EOdB2NsrqWwlzq6g8jPcSU29k5kRvnjN_j11CgY0-FwZoastS46D8FNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKqs8Ux712pLiTfeJDPUuxqCFSyS4TjO2y_2IqTvTK0xsAzNeLGPKkFhiuG09B6DeZzO5Ir8EJpxRaSaW-7AyEYXeNkHwmF1iQ0ZeWBxA9BjksSnKkb5h3LvOL_wFoTn0e2DIMew9HvAuuKP6mFHXz73xHcDTat7GsZLChF9-iC3wZfXNyWJInu_SXLiHl4nM07chZgJs3D0R1mY_tjHcSRmLo_YDeawfTk6vJO-B2Ke2t315QMvdhP5WwIJvDVxlgcNfBhnBvj77WV2burwF-9Ybe2CcJ4D7O5Pfhqyn_PS5bCc9OGceFZO4WLtgmvFKTh2kORrxkAEVW4Agk2e3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=KzzuT_4bpQc6dOqHFKr-yinkH7ZFHcqmI0Fwu9lqiaOFQsHCpN_mKHm-8p19N12PWhHpUIrNKVsTk8pUhEyFpNEhN90Whfe_zGr9Y_4uoCkoxNLm44j-vBV5rAg0rSoJKnud4EevCRZYXRc0x6i2Hqgchsmi_FHfSD_8XV63dD3_mnoY1URiLdhNlZ-3f0H9yJ51fBMJSNpdPXRU3GOXBv33QizvqmmKFRymuv74ADU2L0OQKgqesdgL4b-8UKHmJVCD_kWu9I-eoxZJDHvYR8SFxIgkPv3YsDSnSGlzvs5Cq8tcL1gRcIk5GxJLe_dpqcyyfv3fnXigKbFzbJ_p9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=KzzuT_4bpQc6dOqHFKr-yinkH7ZFHcqmI0Fwu9lqiaOFQsHCpN_mKHm-8p19N12PWhHpUIrNKVsTk8pUhEyFpNEhN90Whfe_zGr9Y_4uoCkoxNLm44j-vBV5rAg0rSoJKnud4EevCRZYXRc0x6i2Hqgchsmi_FHfSD_8XV63dD3_mnoY1URiLdhNlZ-3f0H9yJ51fBMJSNpdPXRU3GOXBv33QizvqmmKFRymuv74ADU2L0OQKgqesdgL4b-8UKHmJVCD_kWu9I-eoxZJDHvYR8SFxIgkPv3YsDSnSGlzvs5Cq8tcL1gRcIk5GxJLe_dpqcyyfv3fnXigKbFzbJ_p9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGsO1uNSSBTXXLxb-GTe6b3id6TmipEU7Ad6WM6HO7HIKhlzeUQNCnkGUgF3IXtC_0pzloxQbD9VcTnvHWyN6JVVI8vlcLqFNoy68t8ACkksE-m414JUw3tPjebH8ncKni9EZVjUzozMTaABd8myis3RYFnYaZxKe9wNt1wPYt0ACLQZlt8MmA8bq4s2dI7MxSg1qQfgTp9JqJ2szuNkATxO0o3vzNjXdkbiyXPbVSHQI0qZeRRnqMQc0IzQW66JX1o44AGZuks31sp-dYThanka9BjtiE5U7z46ZmUkST3s7YOGenSivAVc80n0B-sEGqEdHJKXusdBj9DXoMFaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTTiQO0PEJXhltSrkFvN3snlP_rGFaFgK3h1vyvQRNqznn_fsCfDp5sKMVrBz-XaZMJwczs3oZoD6Ytb_4qQlRzLdK81of3MBJgydeAwfq8hG_3TdD3iuiRVpcfrBJ3CH3-3VVOaubDXp-H90kPti2s39hL2qAifwMCL8C3hg_QItNyDCYyEHqYg85lGDTo4OjmUAkf4FXhta8fzux5GmKKGv0N0fmUnZgiXnGtZl_v0YH7EnV4lIPDFt2xuWuohhxZjiwnBMXYPaa216uR3dgV6x_oudw-qMwLLjVVWxnW2fz_LJaF2Ghj2VWwVjiogd0lmzTxb5YJusC-VNq4lMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3aE0i51AKcEKPyPQkSJRpKqjSpQV8pwBmI8U59eCooPgGrmHu-B6pNKWqw48_ungP8kqkwEY61SP62f8eqo1Re7LhMf-0wGIWHbVZNBcYwOzHev52k_9p4_82RM5pfityegYJiEyxJOLQzAGDjXacNB5SviIYD5n9ChjPjzFBOOsv7ylZ3j-1lCK5cx5HS7uKCcbq0GuTvpWAANBImWjcun7Mxd74OPbLOUXK6GALFcnVQQMl9HfzF3x3MwhHCjXuHa2LYCqKrn7ex7bSgKxCETm6QSuexCTO9Qe3XFQMMJ9jVJ3J6XOGNmnwuBq2xfLaeQS2n8uc-y6gRsUwaDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8R-uRM5bki5uEvY446CAesHN4utKx-PYdNYxIiwCPdl0gSR_gJrRRPb7k_WKiED9MPt6-jwd_Ho9vwohEt9Yaernflkc7dOEOkQOCatDg7PDpuUorfddnj3-e6P4LRm8OyAzLUovczjokFhZPld8gl42QTGAenSRmihJACl1yxd8fCZKFl5DVN24W2qe_jOg1XEnKDE1stm7rjbk-hRbYoW0Ib40H9YomG4AJG-OeZYabiMrjOgNCgKDqDS5cFamiCU-7euuI6LoQRIEyTK8EJz2SLYcOOjuIPSjV6lZfH3ow7AxEN3gqRWmV3cixrs6S4tLZTRcnjMR66b2RKwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBo7B1MPgZaVyw3YRXPFHLLFHWuU3Y-E4xLKemyxKSdSQMKzTYwM7EmD4doNLXgrIUppEOrjFkdIJVnpAn906v3IckZvwq8bfE9L1-mEzBwgyRkLLpf12m2kqsAZ925LkOf0xpL558lNrNWdhk9kSwAPLT0C780YkcRWVFS3UtCpLtkI6mIqdHVqHnxo40w6_cYCIEGMBXQ2jvMhNo9T0GLeiU5P0hQYqCGisLOwOWgTtM8O6XppxdD69QeMYRIdwSC360NtaQncv3oZkqsUd5bnKU4azDXHcdoRXiG1oiPA8L_0K-EX0p10jluGTmYkQxV7f6wVw_RQpQyRTWzdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlhS05l5eYl9UpUain480ypE7xlK3101znDCktclnKYWkPeoCBuCqqn1yEP1hO1pwt7MnxuGIM6UCRhFmgJo2bUFiTU4gDKAX5JhrHs0m-FpYSrT60sasfK4yjiyzB57pAkOXDB1eVC9Clr_D_0DAIKIvt2b5G6QQUODKUYM_YuXoxCW-dfU2CQeXKXfZVGHfU3-n8CIBNbNCIndWDnXnBGzmx07DLBiyTB_ctiA_wxPygdN3A_Ij1aJ_4T2cpsHwIT1W3aP69RBFf1FgH7-LlFctOwgZdMBm6wa5qCsnS9KIYSjSj9cru-edEPa0KELAFW68eGmtf40T745ZSvVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbv4NcFJ5FXY6QhsIKZ61GW6l7PysIIZjz3n-UX7S228V6Az3AKGYkhTSj6nqKcwlzoM58REMt5zFXBmiHvml7dr0cluD4UP8ujgF0lb2xiNGvJM0tSDXamI-ohOKWz450jWM3PrxSaE4dpSpak4IcsmQgxyAacIvVwi00bR0EuYZ7CdEQyUcRH46aTCvkSbr-ZXEidWGKQAPjHNHRN6YAAPuFrp_MhgHl0W4SFa9vwkxscm6RsZ6RNP27ZkIJlaOCB8Ki33Y2crAavsfC1Obhb30K5VhwPBQIUvXjSvA2bVQdn-H2LSzvhisBWam8zeY2ELSuHjepA4KO2wAqZAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjTvbPVt6mWgGNjpfATbLhEgDuSEhQjytTY_X9aC1HKAlJtkQ5VQm5JNRb115HUhMXUaNLawxMeQBuTZfa_F9U_bbXDdEg8zw7MTKCVFgtjDEBpz6NJ8lv2-zpl9XnlQqFW1CaPANTw98EKshPzAnUrCwBjzdDxCTv5bmZ-iz39OoSIyAIxK3RF4Fu6B6cwy_cO14AqoEpKlLTS8-n39qxd_6EkZT9vxbFlM_xI4Mlkz4HyZRF_AXvoGe7azUs47pjDtmOVaY8c5YXcn-Gqgd5OQEDFrT_w0bGKOTgK63pIaxXngoANbB71NwLc2Syi1YQWQPxAH4amUcIKd1janFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS1hJQQigYoU7rQW4Tzn54p_OOL-VnUgwvRABxNo5kZ0PUAT4uqFja4PE39vuYDt1IMKZCTXTJ84HZksMiclnOTK0ZwYJChSul5eanUsQA0MezK0hRg-TYBV2nX9nNiCvKEdDZ2r6i2RoKNI-H2jkq560HyzBbPTiMKnA3M-WTmhdxBXf4PF95W_yq3qTTpK-tCbGfK7_lmQIw-cywhuUTnx2bZmeMMaY4bk-ReX_oTAoNHTgKrP16dYWuKKWascixC4NW5Efi4NhqWefvayQPm-p-wpIjS9p8ZdzKcnClx_LM6dXgoZ8sES3WnhdmpKeMGf0_Z28fGcOzioQuSmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srIvFKddqQBfWVfxIw1nKBPrXqdCN6PDn4Aw5gfykFLTDM8ytNWl5a9h3mBqIM3hfIhrp2ImIqPvp9lVmsv_aHOWKOv1kQFnRNxk7i890rtWPvhv9oAPYGfU_cEPPtX727UEsIaBK0QhCBGj0e3Ig0z8Egm24wsovBjj5Ex4rYOFFatLklSAQs-PZt2A38hdmCnU3PaLOHytVC-EUDe0XwlCF3wM5COdGTFWFu04i26eKme9A5DgilvLy8oWF0YQs76UkO6qX0lUFssC7y_LREpiAAnGivcSYV4e991GFNvhRNKcPKMw3uZcXWJ2MFF6QdhFVK5ecev0rCyLkMrkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHvfQBmRH7L_UCm0ZRyLwpdRmAVD-rHQ1MFIci65pMo3cTrfTGgpgAS4vCZRZXKkiC_SxrsH9mw7oiKjFkc7GZxDEBEEWKarNhVtyLoG4TVHliApE7LyDQ8jsYR4G40002lJPn1t2sttEow1Qg9d2ez6ET6eRxhVhqCwFac-xKRc07CCzz47HnPm33Nig7ZrZE8zOpyHn6yyui3I7Au7VUd-YKwvZUej8uk3OlROM34hRz9Ij53q727KzViNWv3dYkbyMrXq9QIVzlwELFTQCXpgYgbWzOpAy-cIBOnvd-JoEflCkvOE4rWozdOAOfLlQ9b694UOSEwyvzTDJvdFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1u3txHJ-3ES27kq1RDZzuZ1nUdvRYd2hvq9C659bw1STH8vp35Q-dQnG2IY26D_hZ4B2FvNmBv_BNt3jLnvTFvNF_D1UWRZVaKJo95e33cxIfTVRmIrO8yplYAiVYj4h5Y7HQ0ryHb978H9l0IwNOp81MJvX4bx61LIRNsXgnWcm3eL4yaQtf2r7gL5vmSrbBv-zz1PWHUa9mkK2mS5tRSS5FvqOINISU_CfU3bqKj7iZwe6zB9jsSSHFSETkqxWUESkhjx31900mwWZmxAC2N92c1Xn1Gqgnh_rLW-35FvJFECsdarPV0F36AHX0jFUuow4bIj62mGW4OHBDyOaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea5ENbDvw_QGdxX244fecvJqA616oPG2fINdbnysJqsBplKHblqSOZqqnmIA8nGRGgatnkjUC43UKpAVKs1Xb58ihIQwEd75HeIWIpAiutysWW7AZ9TVZIDCAVAmiCEj4UVJ9gjw7mPhHZUXzS12EZ3PJicDqbSbYGI-P0tBKjOxJzBYyJS8jt_ExZ9eyf9IsM4qhVJPaCdDmKWlpYz2Bqe3f39dMzvo5tkLfunCdZBhUFFq-DmajFtvHQnATTy-E3uHTYQZUamNys72BA-8WtK5xlaN7Ve33DsJo_HvTMMHpOx8JnEkbaakMLZ-jjWfIQk5UwGPe4xwSbktHE7uBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG3OS7ZtVXMLEg4FJ3dzqcfhicmkFUMSfrbXaWzqDJhpBbOi0_6NrDvEzPtaBaAVkfbSg_RD4DkTmGn7hV7jdFoXb7xgyM7P6Rqj7TofOR8xdwCxgr7f9MX6Cddf-OLA0hj8ekgcxRlp8yY-HpOccfE6BmhuCgcWRCGTNYee55VUda_LdRky8SjCHl5FEnVz1VVtioeTMIi8L31riU2H3lm4XkP_iTrXveJR-WVbqwu_YEYiA4gcxtKTTS-mTxClx7fhcyxI-gVfaIRzVi2K-qHbcZSbc98UaIxNWB572HHbVOseARMYTh-d-UdIWTEOMQ81VKqvyL2cyJRB1IpCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTwMvp_5eMD-5vHuBLa1FEuwF1ogDYlH3E1JV5Wtr972J3oaILjl666KZqOB-v2yOFShylistM-EdJi2RjqLF2FBD9kmn1L59MrY02CYT9bLyUfuIvGFSTDVu3yXbxzHmYwzuP14uL_rPZms1aO1G7sHfCJ9ILV_j96ivtBR0Sdkw7VFIXHxeS1VrpFRhyT-zu_ejhDognf7rVAyXsYP9y0keD7flj8dOrNSQRzOAP6iVpSNReuZEhbZtK01WJNbYbQ5cU0Wl9AHXuc4YF66H7u5Zxpfbftobe9HATG_QUOit_s_Up2MK1RUjMITbOXtfXXFYOKZ_tpR7pA4gdQ_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ5PefN3kdiYZ4Li70Zc2pWtf53yeqrKIOyZJLItRqZ_YwXrsGPcP-XcoSyISHUo8QP3OrtrlQId4wQpfEJaXrm2pW48AFemu4SSH667j0c5u1h_lvNwWg6_NYyQVO8VCO95lPMEs-SixfQrnn0wRSDVhyIBaR-_XpQvrGbSG9JvVeO5-soM8UG8Oh1gAhJXDbQu8GOUrTSEmHLGDwjiMygnf7qBbxXuYQ6tl3WCGRNaIWZTa_sSqPHeSd3Kxjp_hsMovAhkAEdrhkr-_9UqVAgueqI-zz2qUqAOTdg6DCbikGdMOlgmDomweE5XCN27brYNQdNlSpw8FEqejbQvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFWzSU8Y7gFQ5eNgwj5oGaV7Rrzf0Mhm5zhGw8wyCGjghRjMk9wDupp2M3lV_bn_cEMNdP0NExvcZRf1o7hxWfDOMSOFiXqlotVfBfbFciMN0bBWYf8alb04ehAS2imas1NCTamAAqbeeB_EIeadqJesMtlYK36LDoUDQmhlSfh1_HDo075mBwCzQafkjc7_FrtvK4f6ZwRSUy3YRMmmSC6KsseFGo5rkIhHfV_W3gS9rv3pp82bzwMnKxjQilDC_bE-k9a2wcIuuwbag9ZskoF2YKc6WAeqxGCBT0ZAHfZevf1bQczLoFe-JjjvUgb4-zbBJHKWoZPKrohbkHVUXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=JUMJ43JO4jtvqezn8axnOc_tA92kXSrhhCK6LoJrFDgRoot2rXIpe1UrOh9AdpzIzzvaWk7PVK3eakNggteKEr-HGdHHQdwxGGjMoZ80t2nZb6JEVOjpkTS1vSk3DwozblCV_SaezWL51Ro1b4VmseROHqVHpcHMGZzi0XkMeNY3lQ_SrPW6-G7AW-OR6bjRAkM2Aij-9tEV1LFSdtcQHR3vJDOSIru5hB4j9Mzahf5I8rRZbT_LXJP6aSUSV1OPngO0KmsyLItxI9HKtCN4Bv1sZECMlKhPDbr4EzrCWhrBtYDyRR3enmp_zoeGqcHEtEm2giWA9_Q3vXoSI6Q5xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=JUMJ43JO4jtvqezn8axnOc_tA92kXSrhhCK6LoJrFDgRoot2rXIpe1UrOh9AdpzIzzvaWk7PVK3eakNggteKEr-HGdHHQdwxGGjMoZ80t2nZb6JEVOjpkTS1vSk3DwozblCV_SaezWL51Ro1b4VmseROHqVHpcHMGZzi0XkMeNY3lQ_SrPW6-G7AW-OR6bjRAkM2Aij-9tEV1LFSdtcQHR3vJDOSIru5hB4j9Mzahf5I8rRZbT_LXJP6aSUSV1OPngO0KmsyLItxI9HKtCN4Bv1sZECMlKhPDbr4EzrCWhrBtYDyRR3enmp_zoeGqcHEtEm2giWA9_Q3vXoSI6Q5xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxvU7pBtneehbob32Bi_KHZnhTmOjD-nZvgAma0pVtt15W79OWTObhMvwT6k6srfsz59l5iXTCsiAm_4ZszgxgKVF8zJ3UhFkZbFB11V2F3M3oaJAqL0GXi2C6j-mXnDUl1CcU-hLHix_2UBAELnh21AS8amrkjCPrnJxeYEG6FOLJFNdvgaeheC7uzWHggxYqU15zKhV8KVYhAqsXV7GYTP_NIRUO1DQPB8hzAo1ShL8PuxdIWL3c033tSEHVfwMhAroE0yT827GhL7c04khZScdtvhACMHk6PzXlnX1fmc_aL-OMrY3fkSJkNDHH9H2QiesyRYLWBZnGMM66w3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHWvgEZk6iV-DfXzOXogxGjF8hiQH4_DabZluHWw8Q4ENpj9sm_m25Cjiqb8-Skpe110j4L26BtXQF5Lml9H-qww7EPDuEl16AzWCuqb7oY_PaJrwFfBDacJEXYg4c6V_jpQo2WxTGqwWqAjsQ3O4c0whdmZ314O-TVYHViUpBY-_SKpxfGyewIFlrdf5MQsqDEUizgaBSaY7FnqMfcQLrLk2WnwcXT6oXc3pIhpr9bzHppzAzUksTQvaP7IV6HbBpTrAK8VgdTvF5kx53vTTY2R7Z4oqFJrSrEUXi6jgLwIdQ87XKdY7eBdMd5SfhtOLjQmx4DkQ1_oG_TCVAHvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G56nSL7K4xXW6xlNDKKAIuPbKmqAlJsaIo1AfvG7m4Mp6y9lTxvSCAfEp68oRp6ae5VlLB3fNA-dwI3UNn_CsCaIrmZPcxHBmij1Y61WhY_GtnuedGFyVcMHJXyAA6FoPAYXR-dkIOT653oyZDwVN07CiPEcZ1cyNlZK_hp7-dVqg2hHtvctb7Yl6XjuHy8Ecy5hSgF1jL5GQrBRCnqENeA0Mw_02oDBbVui-GBrtOmHJMdeNky1BnRenx9jvzb_XOf9Wp3V6Qv3AQeCGWWx0XuvoFursY74HbNn1iCfLHllEzHR6TowzDzfCXJ1gZ2Ht8rMmCSwvvbaZzcFyEKqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=JN61H9aLIZ5OBJFiGXWD4FD4z1d2Ew-5tPWwyoygJNHn-_yTwW2bhW_llai9_1lv6-Hz5vbygU7w-flZR8Lx-ZRkS04bu28jvSQzcc3pB4o-tvSrPzxvDD1rtySfcTiyawpWKNB3NpyrQOUh7Q_tRGhkhc45jGh-HBZgqTu41rjj5sqbtdx_DIiYVyi1UWJldsV8vjD83Hf7-TmI3sRl0ikk5EbAUH2p2pusP_0GAjkmcWl3wudS73CdDbo3T6ePvStNG3L-VSxOdAhYT6mZGXEENqia0eA6VacSLvy2z-e6BG_H6LPdHkCm78rT5rGPab5PLXthbxOYnIvscC3M5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=JN61H9aLIZ5OBJFiGXWD4FD4z1d2Ew-5tPWwyoygJNHn-_yTwW2bhW_llai9_1lv6-Hz5vbygU7w-flZR8Lx-ZRkS04bu28jvSQzcc3pB4o-tvSrPzxvDD1rtySfcTiyawpWKNB3NpyrQOUh7Q_tRGhkhc45jGh-HBZgqTu41rjj5sqbtdx_DIiYVyi1UWJldsV8vjD83Hf7-TmI3sRl0ikk5EbAUH2p2pusP_0GAjkmcWl3wudS73CdDbo3T6ePvStNG3L-VSxOdAhYT6mZGXEENqia0eA6VacSLvy2z-e6BG_H6LPdHkCm78rT5rGPab5PLXthbxOYnIvscC3M5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrVyL-x-G052F6EExYaNuLRLmTvMN8hzDCYE_ZRPZeogJ1XJ4pPLWgr5xppa95J_nQi4kmbtwdEN06wocm6SGs1LGTq65XKivCr7JJ9HLN7tFVoKmp6Hdg4MeqIGmT6lvOfv-AFsEwTCLWcm2fEMM02dCYnB_aF3vMvZfHuiRaGg1rYutB8kG1NeVW_Y4tIPiQ7RS-fIA57Vi6XBZURlHpuGa2IhldoJ2e9beFPK5VaCBcrCydHHG8845o56jMx3HkLK0Hnw-GYtvjpgTKFdPuOyV91qrUDJtM8FWDPhXqwZzV0BUl1mEQ8ezyii9pV_1ifP6iU7m7qPnWBGLbs_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=qbgcztl3JGc9-avb8gNGYjm8RiylIQceTrHZV8u0hTf5rYyrFUMfg7C3V523TApE774PwX12GQl5YvUPs32Xe2IBlcAFicWVImZa8cA7p3D8-L3yhHWwQVBK_n7vssncxYFrZiaHz5EZnpaXlgy-KaKhxPY0BuoDJjyIO3HoqePOCEGlJReBXuGwVhFOkcB0WiBrByV3sVUaLNQEL6laeTfv3HkhxAE9XvpL0DeDRkc-ALJuYqqLjdabiKaueT_sMHMUq9y9Cpbzjy5ltafD_aNE_G9vbnRLPhVks638ZWk4ld2E5Cf4uhM9eeuaLRSf2ImVAPJh8lMXvCABDSIEMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=qbgcztl3JGc9-avb8gNGYjm8RiylIQceTrHZV8u0hTf5rYyrFUMfg7C3V523TApE774PwX12GQl5YvUPs32Xe2IBlcAFicWVImZa8cA7p3D8-L3yhHWwQVBK_n7vssncxYFrZiaHz5EZnpaXlgy-KaKhxPY0BuoDJjyIO3HoqePOCEGlJReBXuGwVhFOkcB0WiBrByV3sVUaLNQEL6laeTfv3HkhxAE9XvpL0DeDRkc-ALJuYqqLjdabiKaueT_sMHMUq9y9Cpbzjy5ltafD_aNE_G9vbnRLPhVks638ZWk4ld2E5Cf4uhM9eeuaLRSf2ImVAPJh8lMXvCABDSIEMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PNIhmByD0XDoUaCeL4vITznssQXsG99pnDjFRd785qMlPxfUc0AAKr1GyN6ICXFoe5b9eu-9SKIsC6KeXSGPHrV6aFekLllteregjbRVL7JqIseiPPBPQ_1MLJPgzdWfXXRWGSxTxQ3EKi7OdX5NtF-5hIEBnYkvK4_yu7El6YEPeBERPJ-tAQnwX5Yz3ZEPXQsN9Tozq0vgjMb6SkHJJTBZIAGDM_1z1vGQDaitmu87H-KyVwlpRSzTixCnA0j_rTAu7HLGAATSQq14a6Ch51ILS8RI9_v8P_9UAHf72vAkAZxQ48zc5ijbQtXbLrJEc2_nFVftflSjqK1WGKwZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0q_yxbqnVPOSamsULMXp2V8B-5Sic962N-xZrVmdFGuLaIcp3iathpRVbc5MBVUK7yz1fCpvFGgnPtbch0BFNdD--Rnw9kBjc1mmJsuIOtbdIe6TM0R5cbmHfWLMpV7dzi9rFOZkdSPIgO91dPzpMaBTv-3V2AleO3tkKyuJACArG8BF-HawAB3KYzcdgIOFgiB_ty2kP8Ps6TDTT5Wz2ZBVKELpu5qBst3Ud1GmkOXGvBCP0x74pYH5JW0wc1JrUVBMxmuuHXVaksS8Ui6PwMkWQMgPAa_OUriO4YnQ8TZGjaHYhpuxq_J_8ckyn42_SH9XvoYC432St3FFo60rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngqv8oxod4WQGKvq_X5nA1FsypW76phU7bYkS0t1HfD5yKm7zElMT_OhU3tNL94NciAkSoXuUxFfh3nN2tAXwgQryyLuKYLLbu1lAHuQ-qAFGGX4wQJsfoRTWOBG0hcbmZ0QRPynNF1iuk64_P5vCFcyR8ZTLvEYCSvxgzNIbavraHY5g-ubabu8oHtb33WtQicnr4SY2pFWTCXCP6qFVXWzzDuCgbycbbebnP2bPCJcYUPflhliMJT-FFOwBdKnDtwKo4WMCegrotvaF9mgdBkvaaaDULZiKUb2pCv-yIz5KUr0OH1ceO9Q1228byQ8gpEwb4h7K_HCPqlVYKaD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGeYysQhjp6EWYglxh3e-67tazv74dLOpfP8wqZSURRvsW4Tom0ktuG3pePj8to0piJ9WxrZpnpX8xVc5bHAIlb0IeVoqKONS-IDFLQsx2OMYPakqqkZ5R7wBzlV8HeReYKYS8bidWvdhGVrDtdw6HHwVJo2ZJ2e4xjfKpKfhl7foBIIGdhe0bBHevcGyBYAiI6_td6jzFsyW8h6beJl3WrftB71333vZzr_zctpvZc5yV35dCURmKgT2vrr0sIcDT9KQ18oeSUcEbIvWMdLtA6uDb-5k4uL7Bz8EOLBTdExlklGCSOLb5LwtiKbrLJIlh14DOLgcxrDe3lG0wczCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNUHQP4TTmpjRR9kUWc3Yn8CqYOiFI7gGDGuTKXyQ_V89S7hw84Ra-tVNHQXD0SNjL5Q-iS3Oe4noG5wLj4lJwgNI47BjJBGh8mcQmB6y7SM06rhURSUMAGx2XlSenOR-XSqovSG57j3QbqdeFf6lXH3S2A_4SPgoeHMQJfMWCCK0yRsDAMzo5efgvwfYTpFgojdB3_26M4FZppRMAdA99bkS0Am_Ew5CCVI4wyfmq_vgkIh55BJoNMQHdCvzzfiW9_61g6lvpHvhTTIdNq6szwIFucDGl_Hfhdc9bu_gVIiJ3Mc-ZN8TccZYYZ4CdY90ol43tzJ_1zwx6I8q0T7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_mV5nBFjEsZyw0_Np8bbrsZu6xp9hqkdxgO0Wpf862DdtEU0PqvHrh0u0zJsvNZwHGKoXjLZ9BHYYCK__zrN3UifvzzlZqrZAJlvS5BkaAMyjchcR1MkQ8ysFyTi9wFMQOrYfrzaRrFYEF89E82uwWeC6UhwDFKbCwhIacmlpgUWLEdoqtFuEeTYD8IMsvJdWdLF9vY5Ew-UlOJuat97ZRwCvByGtQZUIWk_qY65LXjwdQNgQqyRdnaG1LUsRXGC9CeW1zTqXL-0jhfyT4o7ZlXcsCPmDiL3hjC_JNkjtuNosrpT9NGmvpOj2Wr3lB12xMUNwH7pFpsGtWN-1C-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp3p_MvdIFfT6nRsbQvhb2D_nyI5rhJyxQtEUOE2f-X7p53s-9tqn5xxcZurI2Xdj9zsbYbZYz5hEz_YeKQM0OBkMGJsOlYcFK6RblJFNzxPwA68M-pwaaoeLZwVBb8-hQ7UqcwCb_pT8QSbrAJ_g69FsU9srYT4qt1lhpRmTDel6V1JreiQURNUV1jTlMOl9sDQHexvMnwE-5yp8aGQLBd9y6c91YvpUhToBi6vLtx-5FAtxoUDgQSEtaBBiODP2f6tIUUJV2pc4Fb1opRnVVaWDXLT2CB2cUEi_WXsigy0voLteWay7v3M_9CA4jOXKn3c0TIJiJf0At76v8bXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeA3n9yu7JaVOKK_waIAmslBT5OkTU-zmiVXRYKkB-0xW-4N5algwDUDhdstV660vS_GI3v4BS1mYOMXKEfWuRK_f552pLr7H2rPmK-f2b8R2Zt4jnGcaEWxC7mprpGOiJKTZnacm1GqHR8t50Xo5Qs_07V5DORvI69aOiwKDIH08HSbFsQrjrHDHMbSqwovlmBtVIJxMK5CNv_jqQ3M4A__CLkQwQcdJN26oZhNGeTXxFaez3TsnCevC26Geqw-nnriQtg3tKkGql121mBji_-ebW6HZVPve66vZ6Q0l4YGwFpjsAAaeMMCJ3GCIM9g3hO6CIfNJV-F278ghYrM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=AIOpRnDvcOypyf1YCSv3rLcfUdBpno2ioFyur3nL-3thjFldCGzArZFDtSG6Sc5orN_khhsXIoDQIKBJ7GT1YR0Fa0jPIGECtYA5V-wWx5kaPIoBn1BfTjrRlWC99uoSy27wsRAyo0G6zXHy-1u4vbZhU_Fq1NFBGLew_xaoPCTevPnL_js3SF7_5Kdesa1zxXFUcn4sESzMMF7Z0nWUuVPWVHq-11WSgTh1IEH696rxF--0JLPl4PHbu9_DOs_oXUdmJM9Ic50ZhFWy0JuVGOhlaKqIes5Gm2atvbhOZ8jTxRV0WcCvbqmbk8WhRjROb79M3-Zzub6JbPUjai-fjD_LjuHT3kRHve2wejfzeCFAnA9c_eX0D-mTT5Mk6wISeqxi8aCwgtalsfVe_evW0sFhj_2F7LtPXCt5BwJtcmlkMLfxiStkMMzo8wkthh9AC9oFUksrxMQQKXmyvZ3xCaPlA8oKnt7GT8VFdg76odJPTMkoG7Ahiyvxp3vytW5Qw8Kxw3_L4d8L-G-T1yEstR9v_V8-PZd765LxBTiJew_eHmCvHfql0Iz5QN3gIxBGnS1Di9lv0HlhnBxO4cryKvl7bzbtUmETxy0qgmrQKvTVb3jXqb6zp5sWeCvhSltu89RSr2ajx-z3e_U-Kz1WXd7-qs3uC40dnIZQ_GAzMPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=AIOpRnDvcOypyf1YCSv3rLcfUdBpno2ioFyur3nL-3thjFldCGzArZFDtSG6Sc5orN_khhsXIoDQIKBJ7GT1YR0Fa0jPIGECtYA5V-wWx5kaPIoBn1BfTjrRlWC99uoSy27wsRAyo0G6zXHy-1u4vbZhU_Fq1NFBGLew_xaoPCTevPnL_js3SF7_5Kdesa1zxXFUcn4sESzMMF7Z0nWUuVPWVHq-11WSgTh1IEH696rxF--0JLPl4PHbu9_DOs_oXUdmJM9Ic50ZhFWy0JuVGOhlaKqIes5Gm2atvbhOZ8jTxRV0WcCvbqmbk8WhRjROb79M3-Zzub6JbPUjai-fjD_LjuHT3kRHve2wejfzeCFAnA9c_eX0D-mTT5Mk6wISeqxi8aCwgtalsfVe_evW0sFhj_2F7LtPXCt5BwJtcmlkMLfxiStkMMzo8wkthh9AC9oFUksrxMQQKXmyvZ3xCaPlA8oKnt7GT8VFdg76odJPTMkoG7Ahiyvxp3vytW5Qw8Kxw3_L4d8L-G-T1yEstR9v_V8-PZd765LxBTiJew_eHmCvHfql0Iz5QN3gIxBGnS1Di9lv0HlhnBxO4cryKvl7bzbtUmETxy0qgmrQKvTVb3jXqb6zp5sWeCvhSltu89RSr2ajx-z3e_U-Kz1WXd7-qs3uC40dnIZQ_GAzMPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upVpxnhyesKIuYX94zBJo575BPC2DsPGKPm86SmL4h2jmvFCyO7LKZwrY_RqA6bWKkvJyDq3-l1Vmn2q0ttOI4Oz7Uba1XDv-_NMpW65kWVWe1qAv2sYsXBKFBm5ZsXzF4AJLk6jx0L1dd0SH69s0m2-oF4NntYiho_3QNiKX1yKYD78g4dnBcKcw7atub621PFfG6KyomsOzhFBFeW5CLI7XMoDARlclQjGmP9K320NRUZwiG0kyYxU4bmDKwV8DSmrnrFRiGO_OIdi9LYsbwR5h4VDwGANcuj6bKY8G9Xw_GxpgWd5PTXsex5yPIQBv5IOoxbdLUOIpqmVnRFb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAOaD0LfKUg5f7n2HSKQylUivxqUMr0DdzqclxeigQ0sJiIUFJdmNnZTvsIpf9f82WH7Fh-aKQ8yuFZmeA3jO5O7ZJpRs2FWFltJjJCSDYoxQF-YuAiO2qYIsbh00n6kIDTi79nIVXS-hS8um5nhyxXRl1RsMfTBLlGpGiI1_c5lGaoMxJFVIbTuMbbZ3sDcuZ2w1qTDrBKUExRwOPoMcnELDQafdaxEpKKnv8-w3b9J6zKh-ISWsYU4QUd-ZFhJGd1Cwjb8Kb-Ch1_1sH8RAibEmdcNLg_Dx2vidKT2GoT-yvfIhgauKb6EBibecUtFD8WcvS3qV8L6hocO0Rjyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElBhs9VlnspqehpPDPYf14CjLZI5Etqed62_WObxnyPWE1l_zSSYBteCs9JFVU3VHpiIkZYw4hwq_nZIF93pvfpwG6Pl2YjWE222jF_Y05OATBtT6ENAkRpMFlNqmiw0K_b8WXCuxReUX23RG8gxVGTbCLtUG8O50vxu5iygU9nshdypm_oA72Q_yNtd68zXTIq_C4GoD4MsxwXxufvtxB0XuCX3y1AHLPoEC_J1d7fmZflPH6ReY8harrCq_ZFgNiURGJfpsZv0tbWbAc45hkjjzO30p8vYQB-uF23K2wqRI1D0ifYOdFOgQNX642G8ZMoPVJKpqXZYNKjrKtUxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOayGwgibnEKLA1xzPaL9g-K1RCFmxXmUVWg16a52_GOel8Iw1Me09HQKnoSwyZCaMJo1LaTGU8CaL0rOSOtq3ZzWnZVi1PkTNCINewk0sEf8BU7pxtbHb-PrDbjtCuLjPR9X9q9aO8bYS-uHAos4tGkwNj5lPdlO9Trtsql7xUnJkz_7VbkRGw1PxHvv3vpM3pbjKdjoJwA0mGFvblG7HjI42lS9I4ji1hU2xLwODK_jsQNnjdrCi9NgdUTObhwL8jsbQ8_grU7sARlQqPiR-n8vlXKPB72Z3ChCl8aDkxNfelodpx3KiSmE4c4YAQ7mRiIRJ728fHMlxyL2lWYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaevX0QVE2SqfSnYv4N-5r-yGlp5woXisDFD2z6R_WEa2q3KZYJVfr6paC3XMDtDczeyz2B4SMlYMT9wo8wmoxC8NILVioVPcDH8aPYolXPMD9LapHmI9jKWBVGVoRBRxW-jhwnWArifEzKHFrMMFZoxSYOTNgKMF5tdz-S4bnLW148wnmmXgLfEd4m5tMESEEMiTUJrXw7iZhTga5iSBKgwM7Kz9rncDghL1SM_97nIMguCyASHSqNejT_S51BX-E2Otx2F1RTl4dzSn3DAemrYaKyNVKILI7FrfDB0XtnZIlwlovzKDc9eg7Ezc5v3orrCWMLzjMLMjd4GQADNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2RPNUP8ZhlTZXUlyglHGRIwTl2cXhEtyNlBpgnlIFJ-DwZdbRG8RXiU-1wz9NNZJQsDSUY-4IkrFtLkEa8r-JaGTieixDd9YNnyxMfyzRTrSH4s6wGh1FUpHGNBwsAePJvWzUdVPV_gODAdQ3yjppt0t1AsWYyCmbXMbagQiC1YTV27ggRaR8aCCZa8R4qQAbeNoNCu0yyZn1SoFBqct5nsYf-gTwa_E8jHKTx1pzAND6L55L6yooT45_8Lz-2ft2xxmuoHUwlnqaDgk4vFMH-5yF6-aFlUrvUmEHNXkqfW4Fs5b3dB-yc1hMazNKexN_8SXC50FMASIVviOc2Oww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=STZDyEBW-7ZBMdLkzXr3nz4cl4YgNEBYZ-xDElDLDkVX16HVR3IUNyeXFMMFSEOHLLZsXtTiebM5C_gX-2v-jPr93w63MUMDws5IH2TH71HVgG8fEdYGcFvVO97u-8an7yowbjtUNAKgklJwHh0Cz7GF9nP3mgSMCYUE6h7Bbasvqz86zPsijcCOBwJU5_f4fLUDK8k82okdkV_jlFcXuJ-9Q2jFjUZtN0PjX_Srx2HsuHpv2dKynFthzAMcFlvFWG4nnGw_ibTnMoNCMxL-mNa_4XMcRUwIyXXQIcUO_FE2p5b64Yly4vavVgnvZnEPVI8frZFJgTzoH4Q2lVCNHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=STZDyEBW-7ZBMdLkzXr3nz4cl4YgNEBYZ-xDElDLDkVX16HVR3IUNyeXFMMFSEOHLLZsXtTiebM5C_gX-2v-jPr93w63MUMDws5IH2TH71HVgG8fEdYGcFvVO97u-8an7yowbjtUNAKgklJwHh0Cz7GF9nP3mgSMCYUE6h7Bbasvqz86zPsijcCOBwJU5_f4fLUDK8k82okdkV_jlFcXuJ-9Q2jFjUZtN0PjX_Srx2HsuHpv2dKynFthzAMcFlvFWG4nnGw_ibTnMoNCMxL-mNa_4XMcRUwIyXXQIcUO_FE2p5b64Yly4vavVgnvZnEPVI8frZFJgTzoH4Q2lVCNHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-BpfWtS_pnEcDRlbfni5MeuJvUJSQ_DGHbIvwV8mwAxQvq_gYImTEM8jZSxS5vlk98A8L_IFPnTGiygAvoYrYYA7CFHUHUDIa_-uBWq8qKReZxNO7mAo0y_Ts8qogtBiM1W--uHptvj0ntt8gDBGC2sHJGTLKQ8uHh4oHO6VnCvN-K18rfVEpNkHgsfUQrVpa8VrVDBYBIqfUc6RhyfXEh8Pj6uNAy0TE6_JLVVGrPn0nGYZEtYv8Hv4HGQcB9Es606xI8EG6xK98CaHXE2GzOgQdGKF3kgREfiGAr8xvXwWE2sDB2A33_YtIyFXipN1XZBNVG66rIL7n0hZ7FlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8YoS39jFlUImuPevPlHkgzfV1jUODr94He4lsWKA80m6GV9yZsxtiBwtslJ70h4v7pteszMruUrxuCcwD1DysVgXJfiwTtTo8BZ_oCJ0KOsW7iLn7j5j9sVCyKgS934rqgFA9Om4foxry5Ify9XRXrMtsZhFibeQZbsGcXZBZNQdELqQDVJB79ek4cau8wqbXUMpyvE-V7NqU_EkYzSPm4wr1WdnWOKpnh6fGvGJVvA_uv21RNjibGDofonJwcOuKh1enJW0wkFF0LcjZI7YCroX5puYKQtnmsA7FFlWHlc05uuOaKWYLw_ifPzeskxVl6ZbZuBSbvLPMzF051-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_o3SP1OPO1rrJFB83wWhjdL7bzHCuepktoLe5dj-AOrLlAs2SlNM16EkFs32Zf-Qat3YVkbNajnZsptOX_oM44o9ODNDzJ8S57MyuRKbxSjQyEL9V4Z3nu3XT-L1YwK-dekEXqKEeIlJMa6CN_Lc_DRQle8h8NJETi4oMoy0OhvWVwWx7L10-LSUjkzgsQj5cwKKA78IC0JdEmO6E7KDPp2ZiE6CLutmA-nSzHaBNe-fxA1Xo-0XtNjf2xlrKQVp-awGAfxvgf-Xw1FD-JEJq6juOxAStImV-zn7crEdVP6O1kQeZ3MBXnVOeTZ2Tw8X1-O8GTzw7d2pJAb7VM2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3oByyK2rcGkdUM6rGp4FeZOGZ_AddRjMoDIp3MkqthzW21bm1UPRn3V-eZrHGOtb3lKZBcy2TUNe4qQno0bpP9H-4Zcr9piIIXy36gpwFB4e6fd_mWcCaRhd0fgw60DAHJa2vpZkcqzkXuLIY-lBHjuS0QK59If4_tjO-bYzvlTrLW7JylWXcsUzFX2JZDvltywmAiKaOJ_7U2DLYgdlqLP2TIljVnORSIhfumLsfDnmFFVx3MX0dleE_Wgc8E7aJkzPtWX4AiAve-rX7SVeadhlg-RTYXNiKicIQht3p0P-zXAFrUYouFL6gDFMrVOHNEGmOOZyeJZBdMWlFhggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGz5NmLV085UqdA9On1gPs78h3BXuncuFfDtLm70o23b6-6TPKtccCzE_qmgcmQ4v5zRkKVsNkVjNzV-m2wTRaIks-zqOkFfaCk4GMWlOmFkY4JN1VG9xmKJVPb0E8yAUdtRuE-c8t-UGS1fQzWRbfa2qvANa8HTtbDO_4zDQAgP596atnQTFsk1DWlML5sA9Q_xzAM-87Jw0FWhIghsTLm0bTZ1SCDsSYycRu4vfSTqQTHx4I_kqb-01Furo2MH6QCg51oPDH2ozFj3sWCqM8gs7-9XcwqosURAlxH2ec3sGH3S52qcm5UvjmOB23imka9o1Nh1xABVhtBJpTntLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFGWVshF8ZYMGogyy1QGcG3A8LIE86qWKa6A3rNgxH_LWBUFF5svgFh44tL-RhfZRYWfUC3vRQY4vBBKKrv4YhekGn0yg0BknQfIdwL85uYGBFH6CEd1KNm_OElEF7x_f79YjQovuO_70WaBJMzchoGVg1in-r7vLTviBgbguvUUQfSbsvyI3o85_vlHDuMFIkPDzPsTWiP652qwDRhVrtuY4C86zaBkfjw2BcEpYozlyEDKida9AhA68OYDxWDD8ZDj-uKgXvRVdXuijlBjZ0XO1Fd7Pn_ziXUC_R0kOLcOsznctSFPgsaHq-ucguXrMSRj0i1jkWwqu8KVLoQA3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op04PFABL8E4sWox4hXGdxau_2cPNEWwq9ZW-9sjIHE_wD9whR5yaK3Kt7RRE-oObk7FjVcvTuWdd9BtXAZFGoZBStRavfGz5kVLd4dopD-_dLESJvkykcbSVewuILiI9e5xJr6zHEcEyxNM5tm7u6oO5YMST1SSUcxtumbdaH-jnpdbTxozM_v2TqdUDlE_fVSAvfurIuAtBz-3RRFvlDtZfd-Lv5UGxd2wwm7aP51TsSvHbqgHsqGwfS8J_RqZN_VWHEnxng8ezDkNDgdytBn12q-QyYQIcYCYnr5dSQFoLsWx156rYtWfmgYfscz73tDTHFjOuPn_SLoHnhC6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTHxBGlmP_KOv_kMEnN2c7txjqCN6_bm-Xt-TxKGONdE_a-UlPwOIHPrJY1CP7nxcOiFlGmI83ljeIrmodYUkkLlrtc6oG5UVhljLVKMFZh1pBcEtE7X6ExmG__6O1ff1QR5sdcfpyp1k-5q3WTFeYlV1iQPzE4UMW489LSgVtgGvwEzBdZa2oduhH_7J8lmKUiY5-bx_sO8CTRimweqRmlfcz-BLYin85_7l64LPM38H04EN1HmG9HFvGtot4xY4OuQSj0s2Srd1z1xDOokb-Rw0I4G1WojlJGsWe7do2Pdg1_C8B1xiyvt9aQSGTeWfcVXLn6jZ1cOwI0rps_s4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbaRCCigCYnA43XzmCkH1azv_vH_iEWqE_mPlHZDmGZy2QF3BNIW5ddn6uqlELrPq7eFGl6J3IGfOQitA68OSqY_D6YwvaSkdpEXcdzRbdEALQpC5Ak0GSDgzMDKidNcRwb0_d3Yu0IkGV8ikrLiWAqDD7CmFCKNHxy3Hic9IvW26bJFmn_DEuh-pntF2EdQ0TZEfM0HNhb7IBD9HK2aZLljmGkQmHGjsQgGug13RyuA0Qk6daeSY5aYi29llGq4Ez6Zzw9Sd9yryBJG_GQmtk6Cf0if0yg78twmIq7XxXKhYEwEzvbtRGc_TMgTsf-J2ffj1kVtxDp_Jcfs4NsZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDsOLIq1tTnWSVoA7nscmjLfdr7CUH4LISN5VQ7zhQ5hKKxcBkwpBVv-pXnpEJD5Gz2E2-ntJonZxuLi4xFVGLNAX-eqpm_ST72MslfHo0iUNUb_ZGdUlt_UXFGPkPgFTCzj-ZiKZl8ShJc0HLApLojjRMOjsBUQfEkJZpAg_wLVnCfyM5mN3fnHsSFHjkByXSAMJsH61m9AIjZm4DrlV-K04f016kYcgDkRSowl7a0r68Y_4utkN6tW8RVm4swfhv8FAgKfi1FL8Bx-bR0MHf_X8PDpaaTa29HKxJ28Bnm_0tgAeRKRDVo_nUcVGj5XsYbrUoK0efuZuJj2Umk8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=RNffq_JTIkq17euGOAP6-FbS-7CU4GlapaZqv7KGkIVQ2tNW0Mj1BdQw_Qbmg0eXqV9Byc57awQpCjryJNemEPi3LEjGXz5gZgJ2LFbsz92DktysgrhqiFJQwWpv10Sfg1Jc8u5V2tF76NZISEmGczw5LHYHHwNmYAR9XeiQz6GTsq6Yy6IiouMsXZ-JFZD67n_avUJtuER2OACVdIMNyXZDfScl4YkqPhIZchnU5_TQ1a-ueKRq7gxYpqUVCnlYjZBSjpcXTFjgVlTAmXgGwW0moauIrkdemzw4YxGq0KYjtA7N-1b6vSxq1dYYbelm7uwyZaJj18RlrVTQJYwE8iD1JPxF5qpGIpii_geMjQ_04nKeJYzDa-eljxbR4ACz7lyB42agfVar_98l-TlFi67MLhqreCJASDjOM-6_RacMS2kna7c8XKFK2MrvZRwNgzIaweTBCESx9M5i7mvjM51a06g6QtWCkLwqqIoR36oWAze35-iw7oSF20c9zfudcd93-N-toNd6GNj867yM-sg3HUX2jqNj0OjhZjLjpog05yFJKg4V_KHJgN5TKY5kaca-Anh1sDM7tV8UwMBltC1rBp3gQnCC4MWwsCE4rzK7mAm54dUQ9UhMYYty_7lWSalkJttqwzyjo5xpiiQZ5f_iOwvXH-f3SSu2ACD70Ok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=RNffq_JTIkq17euGOAP6-FbS-7CU4GlapaZqv7KGkIVQ2tNW0Mj1BdQw_Qbmg0eXqV9Byc57awQpCjryJNemEPi3LEjGXz5gZgJ2LFbsz92DktysgrhqiFJQwWpv10Sfg1Jc8u5V2tF76NZISEmGczw5LHYHHwNmYAR9XeiQz6GTsq6Yy6IiouMsXZ-JFZD67n_avUJtuER2OACVdIMNyXZDfScl4YkqPhIZchnU5_TQ1a-ueKRq7gxYpqUVCnlYjZBSjpcXTFjgVlTAmXgGwW0moauIrkdemzw4YxGq0KYjtA7N-1b6vSxq1dYYbelm7uwyZaJj18RlrVTQJYwE8iD1JPxF5qpGIpii_geMjQ_04nKeJYzDa-eljxbR4ACz7lyB42agfVar_98l-TlFi67MLhqreCJASDjOM-6_RacMS2kna7c8XKFK2MrvZRwNgzIaweTBCESx9M5i7mvjM51a06g6QtWCkLwqqIoR36oWAze35-iw7oSF20c9zfudcd93-N-toNd6GNj867yM-sg3HUX2jqNj0OjhZjLjpog05yFJKg4V_KHJgN5TKY5kaca-Anh1sDM7tV8UwMBltC1rBp3gQnCC4MWwsCE4rzK7mAm54dUQ9UhMYYty_7lWSalkJttqwzyjo5xpiiQZ5f_iOwvXH-f3SSu2ACD70Ok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26463">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0IEQTTaFDxXc7SNF2gQcwvBy13PND8NeB90G65Kx9ug6Fp-9me8ZftYApsV4T3fI10nLky6KhKLQeOqjbGCNYR96y7NDVyjGSP-YSfrn1cRFwy7r6kMHi2vaFjm0vzUML28UijHZH6NEec8W-ftfEVozHXOUOYdpaDrojkSiacj06occpVZz2muItBw40lLPhKRGJolAlBThrxFYra1StsKwqqWTefLFcphX2MYJ7w6cN_EzWpCcO_v8UIRUdszfD60be-00D5tNtwSogtnawa9q57GABy04kvfu-tXta5J36Z80jjEmwu-OkTJWxbIsScNkvu_AWab-52y5gvTCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26463" target="_blank">📅 11:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26462">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rg0tCetdWV3ejhpaa7Nsp6c_ibPhGZgEKqntwP3bBcO54ngQQIPMGqAJrkVbSXgXsPTKpSNs6xwwcrMoGZzdhr_3EvqpwGNH8xyiV_lk8QjnuJMsiSnzF5ZwwBTt6eIhZxv9UubZBmTTxKPlOum5q6jAb4LEMXyM8RBEvR3maEL1LcxXxJwSILuMhJK4223Ohe8f7iuHHHW1rGa9LR07ae_yJkl0PWXZ4LOQmfG94ag3GTN5XbrQSlS3e2bk_vhu4EKj9M03y3AzACuV--9pyBKrLnrK5Em1Gqsqp7W1NusYxsTgqv2n9oa5cFMRWNa1p_5aiqTud6d8CyT1QHeONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26462" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26461">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv76BgAIsODTr9i2QXEFwk1aDIUXWelXwE1PjYrR2Km05K5tvZTPcItIYXIFP6DNXTb5t0QECXZ4ah89oJfFkyPw0CRnoRe_m_5gkPng_sWBg4PjBlnCKvHUisa_j2dXPboP6E0rO7vCVT2x-lAaI_EksMYGdWQa01iAztjDPk4HeV6v29iWC_jXWjblcLR35Bq09rQOXd1w1l6UAuM5YizHAWl5osoYNgzhcT7QYPsOl0fSbuWFTZ-eaxHvg1dryBoWp_I_mbhxlxzW9_h1n8FYjYyTfjXGn1WfFvGXcwGlZC5Zn1qCHTrt8mtDEcgRZU7g1M1L5UBUGdGvfKiQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های‌دیدار بامداد امروز اینترمیامی
🆚
شیکاکو فایر؛ تقابل دو ستاره سابق بارسا در یک قاب. سوارز دبل‌کرد، لواندوفسکی هم اولیت بازیشو انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26461" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26460">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPH8P8BQARRabrh8bECRZUE_1j8P-U5cVLGomfwMZ4_pG6HwciY2Im5lcX5pOO7GaHpaaFpQJ0-rYDPNux17AHyzzhYi4v30WsBqphBvBz3sFBfkhnPGEE_-OwZOP6-oTYAkl67AECBC27VmAN_CEfPSB-wCiJhUGHh9sg_ZLkFxu7KIEmL4dZkM7Uk2LITK8XccKh1Ep7a0zLO5OTTmZBX88kPBeq2lrPZ6sjHum_KVSajoqc8Wx1Q4p4Ql17eKVVX3KiMdgzVI7EI9TIwsz1EuCgU3oLTgZrwxQVKnZ2vNjHtNrrnODjgQ5ZyHOhKnnSa78rI9nOv3TohnJFzZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری‌بت‌مخصوص بازی سلتیک و میلان
🎁
🎰
با ثبت حداقل 10 میلیون ریال پیش بینی در بازی سلتیک و میلان ، در صورت پیشبینی اشتباه 5,000,000 ریال فری بت هدیه بگیرید .
⚽️
سلتیک
🟢
✖️
🔴
میلان
⏰
فردا ساعت 17:30
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr3
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26460" target="_blank">📅 11:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26459">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJHDtJuVkBZPRWFcKwtBxZjvv9rqdUfBTHpf_lYX5h9uVGSsDD567B0GKxiUlJ4-TOODaMqu85IixyDWNUMRStHHVc1HzGnsLJWOlobbjVJNjIDhd3SuB5tBAr73OWBt7czzZq9J9MYFMrhGMZdK2VfBvChJ4r6qXdgb5OE2qDarj1GJ5oPrH1EJoEeVO31fC7lJi-8UWbHSQedVmlJnSPg-OUEnD779FpLH8rBrY50PfzvIYJ4Jue9WcEpX4F-XyZiqS34hDosoVGzbvHukW4ywAbwcWj8jfxsoKaKy0iXFpitZWBc-wgWRjvs1TK04BXYpScEhanM-4PeXVRhoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26459" target="_blank">📅 11:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26458">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIEEYSgUEZDaXUrYo2r6KlmzfXibvwf8gnE2yVFqi6wqLY8VlHcxizvt1rE13m_F3hWKXT5zQFk27wLNrjq6zF-N5l3BGzGJmtDi1NblvgzEQQv5A9Tri_ftPDqpquiZL65iIgdxQhuv4x1CODMbKIWfrzFiyxUX6Y-4b62NWZsB-L1C1n_Q__6MszU2iUYswkJJpg8NQUH-lAf9Ay6NEhYjF-LZNSl1tGfc3nzkeJemkaUZAtfGbPEwkOifiBcL1424JaLmnjWh7XHdsA_pwMvppMa1BZ671WK9SFnt79-s0qJg8iXJ2hOYjEkLalFKOz7vDhw499zCIrN8vsqjGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
عشق‌وحال‌کریس‌رونالدو فوق ستاره پرتغالی فوتبال‌جهان تو‌قصرجدیدش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26458" target="_blank">📅 10:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26457">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXHyVhz1RD_-4tYVFFbZo7wFL6ZuDc3TlMjsUYsaX2rK6f64juEfRvxk3jY8BWMqr2nusO-0PNMd0BsIRJkUgrncwM8vhKmys-JtmCGh8gUT_1DqUMJV9fgmgaFjLGXI7CNEmTKRh3FQnCo-F6NYnmcLLbZKFbrtzHD5gSzZ_Ow7SQ9BXIkIrHKPyhWi_tPhTEpsfOoNtm30K_O7wmsBtit4XlODip9htaTRG7fsTdWLLjnbR5yzHJtdNRcyk-XFTGyUb4jdWODjDO7OdmUOwFVp9qEVQ7zedjpR5de6dOayIhpBTRzZXtBVo1cq27CDJn-VsBEx6dsRKsEqqbXOZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
هایلایتی‌ازعملکرد خیره کننده یان دیومانده ستاره ساحل عاجی لایپزیگ در فصل گذشته رقابت ها که در آستانه پیوستن به رئال مادرید قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26457" target="_blank">📅 09:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26456">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=tcXuxrXPDVRHy0GrWB8v0nR8Khz-k5od1k-vmjF30pxEFQEPSFij10d6dZLVPP0FIrcO6QPvzNj5TwkgZf2xbsqBSXLawINEO7t3w0IcCcJcDUFZXMzGJsFRXrVsssxr9m5KCjD7exgb4eClvf9vEiekKSqmd_1MzzXsi4ljxWwQ2uyJDgsySjFEIPntzeZJssvcnYOGioze5_ZTWzLAJnZo3ZRTqGBepxxVPrl_iBigc8A05hqE5Pm0BibTAcdt5UBYjt4o5ZMnrd15Y-bZobatQ3COCLBX4pgpcMZfMhp27c3YAusrpKqU97oHJwhZc5F7Np6uGKDlb37izY9UPXGXPiPb-qqwLyeWLfjqUv52B5FhzCdGkBsQ08xZENWv7_jFSpwVYTLqA8KDQKeCekq6w7z41HM5sGOEJy-ilgY0Crlak9uHK4q1DdD9F3Pm4YeYFxILSYVdoDsn53Rw8YRTjmYq5l8gLMI0OV4uj87DKuMcrpDrpnZ1xoPJBeoBDPsnJdyb-3fvSfoPxs-YuwEvSw0LZqiTuqUj53J73uP_7Si-ZJqN_VNL5OeDMUxPphEXNFZpK3Avmj14sSlUuRHLooB-2yeHgkA5SEFFFAM9hzHyL8_i9qycNMmQ8zmD0_tehQvjHhDOYOCnSoryRNenjleBWHkuVGqI1BrPSEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f585c525c.mp4?token=tcXuxrXPDVRHy0GrWB8v0nR8Khz-k5od1k-vmjF30pxEFQEPSFij10d6dZLVPP0FIrcO6QPvzNj5TwkgZf2xbsqBSXLawINEO7t3w0IcCcJcDUFZXMzGJsFRXrVsssxr9m5KCjD7exgb4eClvf9vEiekKSqmd_1MzzXsi4ljxWwQ2uyJDgsySjFEIPntzeZJssvcnYOGioze5_ZTWzLAJnZo3ZRTqGBepxxVPrl_iBigc8A05hqE5Pm0BibTAcdt5UBYjt4o5ZMnrd15Y-bZobatQ3COCLBX4pgpcMZfMhp27c3YAusrpKqU97oHJwhZc5F7Np6uGKDlb37izY9UPXGXPiPb-qqwLyeWLfjqUv52B5FhzCdGkBsQ08xZENWv7_jFSpwVYTLqA8KDQKeCekq6w7z41HM5sGOEJy-ilgY0Crlak9uHK4q1DdD9F3Pm4YeYFxILSYVdoDsn53Rw8YRTjmYq5l8gLMI0OV4uj87DKuMcrpDrpnZ1xoPJBeoBDPsnJdyb-3fvSfoPxs-YuwEvSw0LZqiTuqUj53J73uP_7Si-ZJqN_VNL5OeDMUxPphEXNFZpK3Avmj14sSlUuRHLooB-2yeHgkA5SEFFFAM9hzHyL8_i9qycNMmQ8zmD0_tehQvjHhDOYOCnSoryRNenjleBWHkuVGqI1BrPSEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛باشگاه‌لایپزیگ رسما اعلام کرده که برای‌ فروش یان دیومانده 130 میلیون یورو میخواد. خبرنگاران نزدیک به او نیز میگن یک بازیکن بزرگ از رئال جدا میشه تا شرایط جذب دیومانده فراهم شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26456" target="_blank">📅 08:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26455">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇦🇷
با‌اعلام‌رسانه‌های آرژانتینی؛ لئو مسی اسطوره آرژانتین و کاپیتان اینترمیامی در روزهای اخیر پای چپ‌‌خودش‌‌رو به‌مبلغ 880 میلیون دلار بیمه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26455" target="_blank">📅 08:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26454">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0tY8jyAHhTpMBeO3a6PJf3Vwwffvi9V8CObuVhYP82M_6yhtonDTzSWV9_IhvXOdPNTOkEVPTivUwgRp_FYMNUM3eSPOklmLIal-av80SR4Sj7tSVxbaofuX4o3Qy5_BSBhLNanJVctnFGAl3Tg9F8pm8ZKAy9eKyuXgsc2XqLThY5c7eAX0oGKqbVZZDmWteXNBQ4szrT8SqFppNb0wnAtBgzC020Jq4I_bTPGtC6pelWOBhIv843cjgsKEkZR_OBAjGn-1UI0VOItEhLq1TBWCgrTKla36zqAJyPjLUn7kf9Dr65bCnPpqQCZEqTjxeHDaO1onY5myKDgN1veTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
مسابقات دوستانه باشگاهی و آغاز فصل جدید برای محمدجواد حسین‌نژاد و اللهیار صیادمنش در روسیه و لهستان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26454" target="_blank">📅 08:02 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
