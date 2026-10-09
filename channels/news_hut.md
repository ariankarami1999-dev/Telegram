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
<img src="https://cdn4.telesco.pe/file/akACXgWgq8TrOfKTGn-Ja7LZj12HrceEVcomPGCNpytXJ1UUN-32DA2txMwU87sakSXA6yWue0CsxfDcGzj5m_vt0JIhsSn-lwqS92Wu2zZSakZFvZ-PqS_YNkwZxsGh0iVKtwqzbny_tBIWzCyd5L8_oYKwq6v-CfgJHl4Rpllmk1aOmNO57FB3q-zfELqO6-KSIBhOXO8TtwvKCjsJ6UZGlG0CvJeFfQarrcZj-76QD-Iht5oBVifR4t603YnbVuAII7uDBt2EG_K-S5rQ_6raxM1XFmksCwfBVuejsEQzK_0nPPFXmBC_zi2R4eOezqbt6DEJvDTbfcja3SOPjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 11:42:18</div>
<hr>

<div class="tg-post" id="msg-72991">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=o0b_JB9K69n2VVRBJ1unOKhXw3dAUOJK8usGkfHZ1BBNQhJjVgfkAP37qPGDfSjYiHNIGk2uDeXmg89xiwOFbw29fgXPM8iaAWYhdXuDEx7dHpTSOT8Vb3wwC4M1KRmCEaXh2gdiw70eySw1PWxPPWFNZaupDdVnSjNvZe77kfM_OQxVFiuEJAYkpUTzsr0dIuO75TzPne6f49_IyxCXQlq1DKtYi9-JFq61vVsdTGNYjKe9mEDU5I_MbrZTSBk6Ice47O98mAXcKDagrUpPmVDnlL5ZRh0v5Cs_xfjFnpHwaiGcWF9nBMZb-vh3gtdIcrj8nS2Dabf3uTGqos8qXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=o0b_JB9K69n2VVRBJ1unOKhXw3dAUOJK8usGkfHZ1BBNQhJjVgfkAP37qPGDfSjYiHNIGk2uDeXmg89xiwOFbw29fgXPM8iaAWYhdXuDEx7dHpTSOT8Vb3wwC4M1KRmCEaXh2gdiw70eySw1PWxPPWFNZaupDdVnSjNvZe77kfM_OQxVFiuEJAYkpUTzsr0dIuO75TzPne6f49_IyxCXQlq1DKtYi9-JFq61vVsdTGNYjKe9mEDU5I_MbrZTSBk6Ice47O98mAXcKDagrUpPmVDnlL5ZRh0v5Cs_xfjFnpHwaiGcWF9nBMZb-vh3gtdIcrj8nS2Dabf3uTGqos8qXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی وایرال شده از سروش هیچکس، رضا‌ پیشرو و حسین تهی از قدیمی های رپ‌فارس در لندن:
@News_Hut</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/news_hut/72991" target="_blank">📅 11:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72987">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMvFEvmXfrLnHSHSi03bWYaZq47GIokiuftX47CEoGYOc5jIlJYIsFhof6W2OeGsy1DmPbfV-gbahVQH2mZY1g0xwoLlTD4Ukkma4XdFvkqEFCukSLWfZsT1TUBkeMayQbjL_IZAFwZ5MKzWUPn1S_83vCJnzHBcALQdp7IA8cvw1nAY1MoTmVmrUmKIc93YYCw6SjqbkDQ4T-7MR4G-x9Xqnldc-jIyKKCPn8PteyCW9cAk9vCU9NtOdmWLsvopMMyCvnvzYStMox2vr9LytosP4PelmS8Ve-8XTL0G1bGmk82yRv20vMyYdrUghDfvhH5cOen62-zegVBcMInr8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4xzfB0n6Vw0U1yt3qipwvpO56vew4LoX481imqN4AhwxkpPz-0oGyDYtAsc6m0Wc8ijVhQFmvG74Tv_WQ-OQ-Bu0LUdm0qkDGexoJgGHQsvUhXHRL4KAjbeKOq6SX88ZmXeRO0agd3CwaNIfzOli35ulVchW-BYXYKBAOshPv96wxFLpUtab-hBDhSdDcapWQSKmt4XIoog7BZiPI-bDn6ltGUkaRxXeDNuqjo862mKuaZ8vD10xZHMwvc-4zEs1yB4zBNIn53VaJRZV9JBWP2lgqpBeWO8gynYlwemQOHBp82tD5lltfGDJyADTjRIc6EJZFHpNg1BuRjcOXLSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PimxJFDkkX3vWKGUDpgFiE5pkgWRzdFPqhNKRA7TTpHaB3Lt0njIFWvGS1PoZMcMAl-vjdyZYx4g8jYTkrMQAu-3ROrLT4v2YIc8Z-Y7Oukcvv5a-aDzNSgLxMxmi57fROC1mkSEWccPUwCtHZtwO6EknXTERvsqJ07UsWMjZERaNA9ZNkdaIoy3meDr9pnKNGMOti3HfBg9VWzSBnPVIGGd4-OGLiC8QX7vLuDPIAGs6Hn7jw2J9yl4PZ6pjcWuJD0JIfcFfPOIU0mF6dpiXsZUQtlRUpOhQsM0fembRhozBypmmITs4NDepAtzoSa0sD4Y-jAheOoA_IvWIAp2tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78275c1097.mp4?token=UkBOfzS_S6ORmOpxRKyWc6BXm95Wmim6mpQUJE2FGk8Cnzu79DUGSKXHNCjAlX60jA9uzfcFok-1Vzs44izITdGdzO6lqJdpfelNNl18Vbhm5Us4zOyXu2w8Hb9aA1AKfwLmeHh_ttj_SWQyDFnCYAxz0z8nQTKUUhW-Zkunfb-0ooVeseUH9_VCrbGwKxihY-0Eaq8sE3ZPh6e2pEDl-NBwaP4niYz4DN228MEyPwj9UOX5skU6g_sYt4WtSvZSlxCTuGgsrOFXK8GHpukLLHCY1Fxq_E5JugUP1axq9CRPzDReaf7Ey9ZPYqqpGWAHFqQmSZuYmX_-e-2L_0xIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78275c1097.mp4?token=UkBOfzS_S6ORmOpxRKyWc6BXm95Wmim6mpQUJE2FGk8Cnzu79DUGSKXHNCjAlX60jA9uzfcFok-1Vzs44izITdGdzO6lqJdpfelNNl18Vbhm5Us4zOyXu2w8Hb9aA1AKfwLmeHh_ttj_SWQyDFnCYAxz0z8nQTKUUhW-Zkunfb-0ooVeseUH9_VCrbGwKxihY-0Eaq8sE3ZPh6e2pEDl-NBwaP4niYz4DN228MEyPwj9UOX5skU6g_sYt4WtSvZSlxCTuGgsrOFXK8GHpukLLHCY1Fxq_E5JugUP1axq9CRPzDReaf7Ey9ZPYqqpGWAHFqQmSZuYmX_-e-2L_0xIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اعتراضات فرانسه از یه نیروی پلیس که خیلی شبیه امباپه‌ست فیلم گرفتن که خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/news_hut/72987" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72986">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/news_hut/72986" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72985">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCJ90WGigNrT5uMBYM5ck4WOYSTYKAdJRkhI3dDT6c0EpBDWLulGscX_qiSw9t-V9Wgu4fWbKLb6dvs1rjReXSVO8jO8ZzKRJy-QgjrFkR5LNT3Q2Nm98W2_icNZXWH5VlZf7ixdJwMffuG8cZXruP2qfwZDeHIkZ3hhdD2wqrDDs4jccpaRjyiG2xiiDiSMybnDQzRK8Z3QXpecloycj6aJzvBP-NF2GalX3-tYY9cgspIbjSqcm4fK6ucKNnJFYgeTYVCxoF53Z2JbMzRPrUZJcQllOWeJliP-ebPWW2ZkTr3q0CuhkrWHfay9lMOa1UEUsMaGGflsc4qd-s2zWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/news_hut/72985" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72984">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=bT26vWaSwtxuDpWFb55jMUWqzND_ATh_KJuXRjcUQMsMJvC07KG4kPuvuiuO3u-eEz8IvzQBsUdnLa5O1XJ3h1szKC25CIvJnso5-m5ZyWV9ziL9IILXn_hj2NV-bwGYdkxrv90SUjlfcuHIht9J7CVLBwTX14yPBpAZJbEF_so5AbTgAnMf_o2TaPcZHuCO6XL7ZD4LhaRSXHwG9_RcBf1WGEhUj7VEIrBsWiqU9OUDXP8XgYqjQfj8RvbtJT0gWcMQ8pqxaub7hJ6QyDNifSjRqwMzsQDAGJ5BdZdXPfIvhNSlrkzvOab8t-exgh1FnuStfpy1kPi98-FyxmdftA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=bT26vWaSwtxuDpWFb55jMUWqzND_ATh_KJuXRjcUQMsMJvC07KG4kPuvuiuO3u-eEz8IvzQBsUdnLa5O1XJ3h1szKC25CIvJnso5-m5ZyWV9ziL9IILXn_hj2NV-bwGYdkxrv90SUjlfcuHIht9J7CVLBwTX14yPBpAZJbEF_so5AbTgAnMf_o2TaPcZHuCO6XL7ZD4LhaRSXHwG9_RcBf1WGEhUj7VEIrBsWiqU9OUDXP8XgYqjQfj8RvbtJT0gWcMQ8pqxaub7hJ6QyDNifSjRqwMzsQDAGJ5BdZdXPfIvhNSlrkzvOab8t-exgh1FnuStfpy1kPi98-FyxmdftA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
:
زنوزی پول‌هاش رو از کجا آورده؟ رانت؟
نادر قاضی‌پور ، نمایند سابق مجلس
:
بشین سرجات مصطفی، حق نداری به شیرمرد آذربایجان توهین کنی.
شما مردم آذربایجان رو نمی‌تونی مسخره کنی، حواست جمع باشه ما ستارخان باقرخان داریم.
الغدیر مال کیه؟ به ترک‌ها توهین کنی من بلند می‌شم میرم.
سپاه، تراکتور رو هدیه داد به زنوزی! من واسطه‌ی این کار شدم.
شما تو روز روشن داری حق ما رو میخوری.
تراکتور پرطرفدارترین تیم جهانه.
@News_Hut</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/news_hut/72984" target="_blank">📅 11:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72983">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=NA-26Oc9BJY-c76MUwAQm7cyegziW2CtQHfVNLeL1m9KlndQg-JybDa2oBEpyfb4EXQZBQPHwvJ4I4TuIIQx6FPV8bnyeqzpufwf2NKgJa56vBVhRbO8iHlGgbBWsGBfxE2jARyfLfGhhR62V6Htbvw6Zxhlbf86n5-QrtJdK8ByxIcm_35YFMGNqOM3Nb-Q2cnnzPGV07eIjusb63Ltd8riuMNfQrRPfOxlL0e6sXvXrVVDMP0pV0kxLN8vmItiXnsXD1B4jj_pTfto5om7Wi_unRaSG80FFgvfCB-6-LP22NFcjd8IEdGrBT4fIaoG1E7mj45x_82SXQD_FR3dHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=NA-26Oc9BJY-c76MUwAQm7cyegziW2CtQHfVNLeL1m9KlndQg-JybDa2oBEpyfb4EXQZBQPHwvJ4I4TuIIQx6FPV8bnyeqzpufwf2NKgJa56vBVhRbO8iHlGgbBWsGBfxE2jARyfLfGhhR62V6Htbvw6Zxhlbf86n5-QrtJdK8ByxIcm_35YFMGNqOM3Nb-Q2cnnzPGV07eIjusb63Ltd8riuMNfQrRPfOxlL0e6sXvXrVVDMP0pV0kxLN8vmItiXnsXD1B4jj_pTfto5om7Wi_unRaSG80FFgvfCB-6-LP22NFcjd8IEdGrBT4fIaoG1E7mj45x_82SXQD_FR3dHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: گاو که دلار نمی‌خورد، چرا شیر گران می‌شود؟
مدیرعامل اتحادیه لبنی: اتفاقاً دلار می‌خورد!
@News_Hut</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/news_hut/72983" target="_blank">📅 10:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72982">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=bqQYwjSW7UVTXdmc0KjMzD_9J8Afw4FbZgW7M6XAUpO0o1HWaxXd5pr8W6VOTsZA5ccnsvp6P3Z8FexQBGcIroi4kABaeSUWLKi5u19JZFNyF-XnV24uBNNRlvmHbndDSmgX1MGYbcJtDfS9Jh9EPeuYYRtSmYZGdE6FZQslc0rqTEvRg-9_zyeojXouv3rYtIh6RF1f94TZw7LHHody4Tcp0GRupJ8_rJ0ESxwIcZpoKLdcQjlV1laaMQ-83aimQDIHToGeup0IGXxoGkvgKmBbJbRQNs9GAWbVjFeTmsGF7KIHPd2ff2fvx5-6lsGW0-ktYnawdOv2rwtqsjg4ErSeZAhXDpdZUzo1yC9d4GEGRI58WwE88QzT_KqKqPTOMyodm7BQQW7E5Y2PRi4HHGjm43l4e7ADJlihZCU9X-mmqrikWGRiFkpN06owZ3HlOuK2P48sKiDYO4_vFqeRlC65mTcQQTMTJ82fIcRWtJC9B1i7_7Fg7h7JZTlTUdNIKG_K54Uvbdwk-gsf5NBM-IG8IJtPU_zEOtjnrX4hGqzDCDms2G9q6bgEBgleQZbqI00PHnYBTZ_a3VQizBuXf2qUbwXMSLQTpvkzepW1QkqZm0clBlZhnEoEXNsO73B0gu2H2pEPl7y9PtbBowjZKDUSWdwQINyEt9d9-eUfC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=bqQYwjSW7UVTXdmc0KjMzD_9J8Afw4FbZgW7M6XAUpO0o1HWaxXd5pr8W6VOTsZA5ccnsvp6P3Z8FexQBGcIroi4kABaeSUWLKi5u19JZFNyF-XnV24uBNNRlvmHbndDSmgX1MGYbcJtDfS9Jh9EPeuYYRtSmYZGdE6FZQslc0rqTEvRg-9_zyeojXouv3rYtIh6RF1f94TZw7LHHody4Tcp0GRupJ8_rJ0ESxwIcZpoKLdcQjlV1laaMQ-83aimQDIHToGeup0IGXxoGkvgKmBbJbRQNs9GAWbVjFeTmsGF7KIHPd2ff2fvx5-6lsGW0-ktYnawdOv2rwtqsjg4ErSeZAhXDpdZUzo1yC9d4GEGRI58WwE88QzT_KqKqPTOMyodm7BQQW7E5Y2PRi4HHGjm43l4e7ADJlihZCU9X-mmqrikWGRiFkpN06owZ3HlOuK2P48sKiDYO4_vFqeRlC65mTcQQTMTJ82fIcRWtJC9B1i7_7Fg7h7JZTlTUdNIKG_K54Uvbdwk-gsf5NBM-IG8IJtPU_zEOtjnrX4hGqzDCDms2G9q6bgEBgleQZbqI00PHnYBTZ_a3VQizBuXf2qUbwXMSLQTpvkzepW1QkqZm0clBlZhnEoEXNsO73B0gu2H2pEPl7y9PtbBowjZKDUSWdwQINyEt9d9-eUfC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه میخوای بدونی رضاشاه و محمدرضا شاه پهلوی چه کشوری تحویل گرفتن و چه خدمت بزرگی برای این مملکت انجام دادن،
حتما وقت بذار و این کلیپ رو ببین.
@News_Hut</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/news_hut/72982" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72981">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=kWOtbxPw9aY__2Cz37ZmJgSBm3FpKZkaMrbn-8Jur8D-LRCJVk9n5vS7mkcWNi4WN1_aPseBj6VrpkQ54TQgqIijKJQtD1h95kxtcGX7BPn0JB7C4rteFutItERWzuLPQIxTow0-aMuYoP7zmr1id3UPFovOBz81f2p61otMK7HDXHjXqTRMi5FwMjVSwHkbe1j3VUl1RX8yK0PMRahHoFmue160IMmPt3jTKpqRIhbwS6l9nh4tLL8SLFHGEaWFs1v8-rB_H2g5A07pzoII-Dh2GoiH8rfuxjdzvaIhrjcB4uHPJr82SsAdyt8TQzvXA1NINb06qaWysmzRgl5U5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=kWOtbxPw9aY__2Cz37ZmJgSBm3FpKZkaMrbn-8Jur8D-LRCJVk9n5vS7mkcWNi4WN1_aPseBj6VrpkQ54TQgqIijKJQtD1h95kxtcGX7BPn0JB7C4rteFutItERWzuLPQIxTow0-aMuYoP7zmr1id3UPFovOBz81f2p61otMK7HDXHjXqTRMi5FwMjVSwHkbe1j3VUl1RX8yK0PMRahHoFmue160IMmPt3jTKpqRIhbwS6l9nh4tLL8SLFHGEaWFs1v8-rB_H2g5A07pzoII-Dh2GoiH8rfuxjdzvaIhrjcB4uHPJr82SsAdyt8TQzvXA1NINb06qaWysmzRgl5U5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو گیلان، یه نیسان گاوی و موتوری باهم درگیری لفظی پیدا میکنن و بعد اینجوری موتوره چپ و نیسانه راست میکنن :
@News_Hut</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/news_hut/72981" target="_blank">📅 09:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72980">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7QC7-ovNDyk_mFtruaACdLWm9IJ2Qm4FSWfjI4IDxszGHI5hQixIwsGZOtJzQ-DJ0EAbjwtX-F8KiAPf-Tp8Spw6VBjTzXmrjglPjjpgBFoKQPq8VKiLK-iMOtLI6e8_JRj2aLJV3K5VxspNIAF3MySH7cneWm_9CRtH-StDZt10gb3ZpsJ9H3bXmoVTUl2AcISRtvN4nqGD_5yC0uExhhDTnbV-3BxmqG0Te-XrbashMvOm5bnOHc0_4lEJxG2zCiGhs0zBx5FSKTUtM6LFAg5xWUJJo_rLMWNmoTAykMcuA18GbeKS0hibiiTTpakY2jCrVSk9fymztr7R0Xd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقام‌های آمریکایی: پنتاگون طرح‌هایی برای احتمال اجرای یک عملیات سه‌روزه با حملات شدید علیه ایران آماده کرده که شامل هدف قرار دادن زرادخانه بازسازی‌شده موشکی و پهپادی ایران، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تأسیسات نظامی می‌شه.
انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات نظامی گسترده آماده می‌کنه.
با این حال، ترامپ هنوز تمایلی به ازسرگیری جنگ نداره و در ماه‌های اخیر پنج پیشنهاد برای عملیات گسترده علیه ایران یا حوثی‌ها رو رد کرده. او گفته پیش از انتخابات میان‌دوره‌ای آمریکا، مجوز حمله رو صادر نخواهد کرد.
مشاوران ترامپ درباره حملات احتمالی اختلاف‌نظر دارن؛ برخی تردید دارن که حملات بیشتر بتونه موضع تهران رو تغییر بده، اما برخی دیگه معتقدن یک عملیات محدود می‌تونه فشار بر اقتصاد بحران‌زده ایران رو افزایش بده.
@News_Hut</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/news_hut/72980" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72979">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6nDFnLeN4VLLVAQvjtW5GwzE2EJTRfpchTKARq-elcc4xcdQQMznJZAd0CCfSNWEggANif4DnqUrr1jIlRsq2EzrLlZg1v4D8azhWUQMrTkidKgOOuFy_vuZSw3Ipwaet9XukbINWgw-XGR0l_pdLljSu7mZRVFEHUWAQJAeHD7G0lVQZvNAq_EV8c3xNl9--18FEbvpiO6PdLJjPmzpmotcISG9aAeSCcVeITmrwdc1igiwGx8zoPen017QrYgumJ5WFbzZucWK3xoYXarY8bzLM71HW-KFEmAErLXZM12TcPo6SgNP0mZnKC-IP2prbFmAs6p6wramCa7zgYJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«وزارت خزانه‌داری با قطع منابع مالی، رژیم استبدادی تهران رو از پولی که برای جنگ‌افروزی در منطقه استفاده می‌کنه، محروم می‌کنه و به افشای افرادی که به فروش نفت این رژیم کمک می‌کنن، ادامه می‌دیم.
هیچ‌کس که به ایران برای دور زدن تحریم‌ها کمک کنه، از تمام قدرت و اختیارات وزارت خزانه‌داری آمریکا در امان نخواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/news_hut/72979" target="_blank">📅 07:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72978">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBNjUNFgzNOm267nYcACQZ9JKJucxbAnmfUrs-zy7SLNOCbV860do4fQrGKvHxBVOAuU6v8s8mUC2hd7oAkoixUkBm69s1K5nPxLkylgOInxntpZat3ZdtMiqXleyWL1kIkOTe3zBo6oezK8FD6-FwiJPPJRkZyb8IeN0znS6THubcaAP40Uml6QGoEN5_U0SR8z-Epfnv1dsNzSsxBf1XaLIYJgzngL8Mn1PtLCUur8e8IUBhNT80KPJvOj8W2K0kJ3sDu9Xed2jPdgzOEbYp7CHNn-92EUmJz_2_FNIJXKW8yXgw5O-5Ph9UEesHLBvp06nRhT4_cSOAmOnuXX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه شبکه ناوگان سایه ایران
وزارت خزانه‌داری آمریکا از دور جدید تحریم‌ها علیه شبکه باقی‌مانده ناوگان سایه ایران خبر داد؛ این تحریم‌ها در چارچوب کارزار «عملیات مطرود اقتصادی» (Operation Economic Outcast) اعمال شدن.
در این دور از تحریم‌ها، ۲۲ کشتی، ۲۶ شرکت و ۶ فرد مرتبط با شبکه حمل‌ونقل نفت و محصولات پتروشیمی ایران هدف قرار گرفتن.
این تحریم‌ها اپراتورها و شرکت‌هایی در هند، ترکیه، چین، هنگ‌کنگ، امارات متحده عربی و بریتانیا رو هم شامل می‌شن.
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/72978" target="_blank">📅 07:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72977">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72977" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72976">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbabiQXapfgFEZZEH-8sJk4x_hO-LaxISzXeG6eKIOqhPtBpa8p_a_npbzSWclc_LTj6RSqVaOHcrHBynOPy9dwyXLlKhFSf9xXs4fUyZPwVcD4Rq0cVFb6vzn3NA-v61r2s_Z96hhxFtUSlk4ToPeU8tzWQaPcnz9G_wjFBlYYrBaxDQAXhag6-WJOfrz5OeChfXv-0tfV3A4ZJUS7RyLxnnhfTEJb4ipQqMqdgruQkrHB-Awturv8cYlOZM-i7nGdDZfGz0paYBM1UoXPlk5wFyDkQll1-NGfnRn10ZutnoZS7oTyDI-0_AIeWWfmlbogBmaBBaHASyKwiUDAKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/72976" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72975">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPrBiQbkGKrtnGYmv6dlfg5B0iUPpcleSONt6-MNh62M5A_MVrMR-n_5NRAWn5Pe1ENdKussvg52XXTLSPXklzi739kNmd2lxbEHEGbFZIM2KjDqV3cwKdEBw8GoE6hcljbowHlHv1LGQXTmXPa5bD8HjN00WZGU9okx-slyFRgiF4aC-lKH-Dh4G9B0rOIKPyCE_QqnpHyA7k3Y5YSsHxWGeO4wRhMcTjFz538Z_mWXkofA-SNUCAxzfb9xQbe665ozWAWZu0Aec5YD2b1WF0MPrBAl48Ofioch4pinzUGa1w6RcN9UJ1qTaaKqKAchGZ16Zv-aIeRtlwyWrwhK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی لشکر ۸۸ زرهی نیروی زمینی ارتش:
روز پنجشنبه ۱۶ مهر، مینی‌بوس حامل کارکنان این لشکر در محدوده نیکشهر، سیستان‌ و بلوچستان، هدف حمله مسلحانه قرار گرفت.
بر اساس اطلاعیه رسمی، در این حمله محمدرضا اوکاتی کشته و سه نفر دیگر مجروح شدند.
حال‌وش از تفلات بیشتر خبر داده اما هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72975" target="_blank">📅 01:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72974">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV6NfxfpxVKuIm_ldeWusSXqcArVxYhCxnWKaEEZMA3UR1QMflfejobaHtnM6l0vSKPsXTErzCVbB_IYhvKu6QYuIrMDKn87lqd8tJH3EfetiOREekgvwPCu7ssAVnfynt3xC1LM1t95BZlJCpd8wU8DRuiJgnrCO5PfJwMiZ_PCvlGY26Ux0JB7PTUBMPULMBz5PAwbEXkWYlqIkJrzCmZSvt_YtlaEkapHMq2OK98xU_yjbiEm1iYRPiNj7rGisZb5sbGgnIMG0M3Jn05TkTJigY1gKxouEOOt_9yXdR67RhXpI8rYR31k3gYocBajCPGMKO5xwkyHE7_mthKROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72974" target="_blank">📅 01:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72972">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=R7VX_Y5zx1_Kw-_ai42CEZSS107fdn4EBtrSbDK4ivgH96zW6Ka3WSUI9ODW1PJvZi0Pa0vvOBcmnJz5dsyNT_LNZxsaT5HVpabWJDQqHXlT83-5bY-ZP2xxUp2gL4tsfmzkhUgfvEaiy2vPbrRTz1OXHyOMIrFd8UL3h9DBMImcj6hmF08cpRdATYkYKkj-t9eaQHwgv24ftPO2Ve-_hd4N7pvILtxYq35iinN7zE3wL9T1i1lB0_k07qx_t1pGmLf_8uTxIpjVbxwsjbQ7TFdNvlhiwxK1ILQmaPtI_wdOa7cWMV9SB6BZMrdnDgamOnQfn_0YZ9JjWT3GOWc6ID6smJ2jqT_tu6Wr-Em4P4NbYG2elSv3nT9e-4ca4w1ixnRYgjopjuXWGUdyegiq5tXyND35ddEaeIW8Wa5zw7d5qQwDLv49oVT4SVD07P_-tcnr4lypaTxzjPNRyXwqtbccZEH7wQ2C5NhXnxT5xse8-CDoy2RkA0X-67A0u9jELPe-MB-sM6U_ol1HEB2xr4uR3w-UhpW9veSPXCqp-w8PYICHKsdGQJFTeWDIeXIxWitKdMjUQvCpFZpjshgFFwrQ2VCMMYHRtQY-crO2xXuyfXcdmW6yZG2PdOWfP-OciX_3ggCb4u5OPkh3fZNLWIU83tBuGQ8Lmv6vrUrQYjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=R7VX_Y5zx1_Kw-_ai42CEZSS107fdn4EBtrSbDK4ivgH96zW6Ka3WSUI9ODW1PJvZi0Pa0vvOBcmnJz5dsyNT_LNZxsaT5HVpabWJDQqHXlT83-5bY-ZP2xxUp2gL4tsfmzkhUgfvEaiy2vPbrRTz1OXHyOMIrFd8UL3h9DBMImcj6hmF08cpRdATYkYKkj-t9eaQHwgv24ftPO2Ve-_hd4N7pvILtxYq35iinN7zE3wL9T1i1lB0_k07qx_t1pGmLf_8uTxIpjVbxwsjbQ7TFdNvlhiwxK1ILQmaPtI_wdOa7cWMV9SB6BZMrdnDgamOnQfn_0YZ9JjWT3GOWc6ID6smJ2jqT_tu6Wr-Em4P4NbYG2elSv3nT9e-4ca4w1ixnRYgjopjuXWGUdyegiq5tXyND35ddEaeIW8Wa5zw7d5qQwDLv49oVT4SVD07P_-tcnr4lypaTxzjPNRyXwqtbccZEH7wQ2C5NhXnxT5xse8-CDoy2RkA0X-67A0u9jELPe-MB-sM6U_ol1HEB2xr4uR3w-UhpW9veSPXCqp-w8PYICHKsdGQJFTeWDIeXIxWitKdMjUQvCpFZpjshgFFwrQ2VCMMYHRtQY-crO2xXuyfXcdmW6yZG2PdOWfP-OciX_3ggCb4u5OPkh3fZNLWIU83tBuGQ8Lmv6vrUrQYjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه به مواضع گروه‌های کرد در اقلیم کردستان عراق حملات پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72972" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72971">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیویورک تایمز: انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات‌های نظامی گسترده آماده می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72971" target="_blank">📅 00:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72970">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6_xHKagLvFPOKEGDz12oOssnPDZjs7pPpqk5K5ecDx0KaJnSkmyP7HgL73TgtSpadIHvrgsbHmkoiMC_YSpvNknxcyVhRtp16XlebWZm9sD7QBoKSQSnFzCcwqLxG46D4u-naobjrZUmcMPI1JWGOtguW2mXfitdFBC5n5Xv_5SlxzgFBCVeKSPaMT4bAGdErnTPNV4y2HrFeXrXKTJ8wqfOHXhRiV1H-fQrZSyddTqNWwb5wDeagIqX-tflvSWbCmtUDsvN8qL-oPXL6v6WnC5MMbrvWjF528Oq0FglnA3aoyY0dRRZrAXDuicao7_B3sf2BwETfCqcrkertpWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
«رسانه‌های جعلی و دروغ‌پرداز دارن این‌طور القا می‌کنن که من از دشمن دعوت کردم به سن‌دیگو و لس‌آنجلس حمله کنه؛ در حالی که منظور من این بود که افزایش موقت قیمت بنزین، بهای کمیه که باید برای نداشتن سلاح هسته‌ای توسط ایران پرداخت کنیم.
حالا اگه می‌خواید بدونید بهای واقعی و سنگین چیه، تصور کنید اگه ایران به سن‌دیگو و/یا لس‌آنجلس حمله می‌کرد، چه اتفاقی می‌افتاد؟
تمام حرف من فقط مقایسه بین کمی بیشتر پول دادن برای بنزین، آن هم برای مدت کوتاه، با حمله به شهرهای بزرگمون بود.
همه اینو می‌دونستن؛ رسانه‌های جعلی هم می‌دونستن، اما بازم ادامه می‌دن و می‌گن من از دشمن خواستم به دو شهری که دوستشون دارم حمله کنه.
حرف من کاملاً روشنه، اما این آدم‌ها منحرف و فاسدن و فکر می‌کنن می‌تونن مدام به انتشار اخبار جعلی ادامه بدن و از زیرش در برن!»
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72970" target="_blank">📅 00:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72969">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2l2xuEpPSxHk8uAvuKWLgj8GaZB_yTnQJ5t3baifRjnO1yi5clCek0-48281aXzFaFhRd9Vj9ecpcZmODnqDUzAXKbvv1Z9hp0dOKIBFUsp5nLyvT7qD6mb-o-_FY272v8Heg7MWRL1-NZgvGYkPaBPYfacYdmunVi--5BB6K-KVtSO0Z_CIt4tzohQwv4ZfYWEuEEgSlpHdMi1pHTgLnW3-kks3pvGI1go2RL_m85xoRpBvelZY0uiGWmQPYTEmOXheZkcLC_aOOaVrO-9oyJdaeQ_V2VW7XAlDkXMtlI-CIw0ItrJpPPN517DfU83Vv9d_va_NxCGZY2GVhzdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز 8 October روز جهانی لزبین‌ها بود که به اساتید اهل فن تبریک میگیم
🐸
🐸
🐸
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72969" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72968">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=TrzSydINJpz7j6crsQhrRootGAv_NUo6yIiJri84_6KwTvviyvZhN6nw1xM2AzXZmFHsA7XZhK1Sgyk8yqnkjBG7qngWV5D3-SI-ZNiGu67Bp3bRV1Fr-xmg3rDBvVJc6oE-VQGSLuDESLPw4-nEMKOJ2T2QdOS7rZmC0hblC_ZjxTT5hZZHsWoKh_Ofd9pWpnz5RxG-RTKmRMNfGlJRBJougcDlhL84a4IsjgsqicfLiDW65joqYu5SphXBkoGR48sytShaLjQ9AvsPPRrQp7fOV2k0B-1IcXApdMRbOaRn-4bF6oHkSspkW5Na2wJSSwJtetZoV-IeQXbQOhysqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=TrzSydINJpz7j6crsQhrRootGAv_NUo6yIiJri84_6KwTvviyvZhN6nw1xM2AzXZmFHsA7XZhK1Sgyk8yqnkjBG7qngWV5D3-SI-ZNiGu67Bp3bRV1Fr-xmg3rDBvVJc6oE-VQGSLuDESLPw4-nEMKOJ2T2QdOS7rZmC0hblC_ZjxTT5hZZHsWoKh_Ofd9pWpnz5RxG-RTKmRMNfGlJRBJougcDlhL84a4IsjgsqicfLiDW65joqYu5SphXBkoGR48sytShaLjQ9AvsPPRrQp7fOV2k0B-1IcXApdMRbOaRn-4bF6oHkSspkW5Na2wJSSwJtetZoV-IeQXbQOhysqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی دخترا برای پسر خوشگله زندگیشون این حرکتارو میزنن تا دلشو بدست بیارن:
بخاطرت همه پسرا رو آنفالو میکنم.
ساعت کاریتو هم درک میکنم.
حتی عکس دو نفریمون رو میذارم بک گراندم، کی دلش میاد اذیتت کنه خوشگله؟
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72968" target="_blank">📅 23:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72967">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9487485a01.mp4?token=BoVdQpuhTaiD9f-ftbjJHenCzCnUKhEt_jHcgz33ujugbz8HCTOtX5dnlaXzMzJ0k2na6NVEo_ft81HD-0T61Zp3dLmOOAO1Tc7Hh3X6XI-kT52jW_h7YyhLmjVpP8fzTrWK7nJPE0NR8JMjXZA_C2bow1PMJoQL5lUhNndjh5zOoVcKQndQ27IKWNXdGmlXFxPWm1dTwcHhnajFsbt7o48sO8ZDRxOTjeOx25FyjHnP2-Y-F0KupO4AjB3AlP8QLM3dOECH5mn2lkpS0rkDk8JXCU_yGzat2mRFv1IFRjilnjqXriwHftqi3J23d3LA7G7KJILyvhl3iT1bpZJY3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9487485a01.mp4?token=BoVdQpuhTaiD9f-ftbjJHenCzCnUKhEt_jHcgz33ujugbz8HCTOtX5dnlaXzMzJ0k2na6NVEo_ft81HD-0T61Zp3dLmOOAO1Tc7Hh3X6XI-kT52jW_h7YyhLmjVpP8fzTrWK7nJPE0NR8JMjXZA_C2bow1PMJoQL5lUhNndjh5zOoVcKQndQ27IKWNXdGmlXFxPWm1dTwcHhnajFsbt7o48sO8ZDRxOTjeOx25FyjHnP2-Y-F0KupO4AjB3AlP8QLM3dOECH5mn2lkpS0rkDk8JXCU_yGzat2mRFv1IFRjilnjqXriwHftqi3J23d3LA7G7KJILyvhl3iT1bpZJY3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72967" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72966">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=HxAJQVrEx92Y79clk5ZEGhB3ZzheuJrrannedoJhUlfm538opALbd7lHbi8Z8JPZqYiRNi4VVq-V1vLgQPdnPiumBjhx9m9jVHawg0v7FXjpvuA3oKoYEpPLfBySEKqUc1kY2y50anb2wjrjDskvCmbX1OSMXNozBkhvsAuSyvwWXfvkoP2nJz9hSBoL3HtaJPak2An0ttv1JMuhAEUxUGCaE3hiFgU38AbbYND9NDiKWtxznpYraFRWO_y8nKxUGq4740pzz4covEV2n-BBtkKCJXKbpIaUg8LGbO2-MAPm8_xmTd9e5TAYEHKBwbE-iwMs-KnYyb782CRMhXzZDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=HxAJQVrEx92Y79clk5ZEGhB3ZzheuJrrannedoJhUlfm538opALbd7lHbi8Z8JPZqYiRNi4VVq-V1vLgQPdnPiumBjhx9m9jVHawg0v7FXjpvuA3oKoYEpPLfBySEKqUc1kY2y50anb2wjrjDskvCmbX1OSMXNozBkhvsAuSyvwWXfvkoP2nJz9hSBoL3HtaJPak2An0ttv1JMuhAEUxUGCaE3hiFgU38AbbYND9NDiKWtxznpYraFRWO_y8nKxUGq4740pzz4covEV2n-BBtkKCJXKbpIaUg8LGbO2-MAPm8_xmTd9e5TAYEHKBwbE-iwMs-KnYyb782CRMhXzZDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ترامپ رئیس‌جمهوری نیست که بازی دربیاره. رئیس‌جمهوری نیست که زمان زیادی رو تلف کنه.
ترامپ دنبال صلحه، اما حاضره برای رسیدن به صلح، به شکل واقعی و تاریخی، هر کاری که لازم باشه انجام بده.
ایران با داشتن بمب هسته‌ای، اتفاق بدیه؛ نه فقط برای ما، بلکه برای کل جهان.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72966" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72965">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=O-u9Nw-eKxb6baGktA0KzuUKkKFRyrH0nFTeZpECVb5f8_XO0TsBp2ZT6vr9nIlMS7yJ1V1PuZo264YcWeKgr6XkgWj7kKwXrQJvc2PeMu8RWzmNvj4OE1gKRyP1rGPNYSD2RC3pZMiv5HohorVYqKv2RMUbtmPHaIVnY3TQ5pgfAKOieI1jBQ4nZ7DhSeUzjRKjfrhpN0DjlPA_W3xHrvw3kFDwc_hXR5dnZIWlNUQttR9x1urBPlyw5cxjASJfLYu1_xB7PP8cSDJagY66UUoa1ehnz24aka8jTzbJJtSkHDCbVTlcgwvltgyb23SwwbzQX0tEuJcRB0A6Iuf6-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=O-u9Nw-eKxb6baGktA0KzuUKkKFRyrH0nFTeZpECVb5f8_XO0TsBp2ZT6vr9nIlMS7yJ1V1PuZo264YcWeKgr6XkgWj7kKwXrQJvc2PeMu8RWzmNvj4OE1gKRyP1rGPNYSD2RC3pZMiv5HohorVYqKv2RMUbtmPHaIVnY3TQ5pgfAKOieI1jBQ4nZ7DhSeUzjRKjfrhpN0DjlPA_W3xHrvw3kFDwc_hXR5dnZIWlNUQttR9x1urBPlyw5cxjASJfLYu1_xB7PP8cSDJagY66UUoa1ehnz24aka8jTzbJJtSkHDCbVTlcgwvltgyb23SwwbzQX0tEuJcRB0A6Iuf6-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ما دنبال ملت‌سازی در ایران نیستیم. نمی‌خوایم تعداد زیادی نیروی زمینی وارد ایران کنیم و کنترل مناطق رو به دست بگیریم.
ما فقط می‌خوایم به اون
رژیم، رژیم اسلام‌گرای دیوانه،
بگیم که شما هیچ‌وقت سلاح هسته‌ای نخواهید داشت.
حالا اینکه این اتفاق از راه آسون بیفته یا راه سخت، انتخاب با ایرانه؛ اما در نهایت این
رئیس‌جمهور ترامپه که تصمیم می‌گیره.
و می‌تونم بهتون تضمین بدم که اگر اون لحظه فرا برسه،
اقدام آمریکا سریع و قاطع خواهد بود.
»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72965" target="_blank">📅 22:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72964">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=OL9ewmibu8NUNi8sQJR5giBYR2nOCkQs5JE8gva5G-32IQEzATJK0kU-je493G4anTUIf0d1XgOfIdwLKNEdO3pBT9p9fr3LC5uF1lNsjIqqYbuRq8BEYP3spYrf3mbiKsb7XeovAwugNWqeIFI8ZT7iTpqvhLCFfCSFfiRMMBtmdcMhlKEOBMEfFOt_E325MrrkJqOOFEEdk23BWbYanm7ArlW5Y5kmb8nLq93SmN4IPu50j0SCROww6psXN7j-UIGVDFazit97FawAUQ4DuUu3gtsBzFRzjZ_3cHPGMN1b-2DdX6cpb97PSEkFRB3Ewe-4X14k_dwa-W3oGBJ85w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=OL9ewmibu8NUNi8sQJR5giBYR2nOCkQs5JE8gva5G-32IQEzATJK0kU-je493G4anTUIf0d1XgOfIdwLKNEdO3pBT9p9fr3LC5uF1lNsjIqqYbuRq8BEYP3spYrf3mbiKsb7XeovAwugNWqeIFI8ZT7iTpqvhLCFfCSFfiRMMBtmdcMhlKEOBMEfFOt_E325MrrkJqOOFEEdk23BWbYanm7ArlW5Y5kmb8nLq93SmN4IPu50j0SCROww6psXN7j-UIGVDFazit97FawAUQ4DuUu3gtsBzFRzjZ_3cHPGMN1b-2DdX6cpb97PSEkFRB3Ewe-4X14k_dwa-W3oGBJ85w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران:
«ایرانی‌ها فکر می‌کردن توی تنگه هرمز اهرم فشار دارن؛ ما این اهرم رو ازشون گرفتیم. دیگه چنین اهرمی ندارن.
ما کنترل تنگه هرمز رو در اختیار داریم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72964" target="_blank">📅 22:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72963">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=WdCKC5NcuZWLZ6N-8y003ZxYwVnl2x2QSms5qnkA-WIqmLTi-ttOqgghkA-odzVikLaIs8SmNr-dgsn3FgBBaRxMaREC5Fq1zGbhKbXz_eX0pJjN_7BC-LO1WpSqNjOR4B7Q_6RnSbUYxL4WkRAxHQ8H0rGBvyIWn4n14ziR_qLkgFqh1S6wBvfKnwA4P72kgxIlcj3q5EhnoUelcoIhsHLxuqZkN3UL_VJqzaxO1_RnsA6DSeQ7An72egUT73Xt-7rXJuV3gYWYPSWxYgUCAcnvyWNr_-QNSM1rJfeLE6C0-sU4bCxAAboAnh5PNwZzGlR_DlxlDXzej-q5fZzWXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=WdCKC5NcuZWLZ6N-8y003ZxYwVnl2x2QSms5qnkA-WIqmLTi-ttOqgghkA-odzVikLaIs8SmNr-dgsn3FgBBaRxMaREC5Fq1zGbhKbXz_eX0pJjN_7BC-LO1WpSqNjOR4B7Q_6RnSbUYxL4WkRAxHQ8H0rGBvyIWn4n14ziR_qLkgFqh1S6wBvfKnwA4P72kgxIlcj3q5EhnoUelcoIhsHLxuqZkN3UL_VJqzaxO1_RnsA6DSeQ7An72egUT73Xt-7rXJuV3gYWYPSWxYgUCAcnvyWNr_-QNSM1rJfeLE6C0-sU4bCxAAboAnh5PNwZzGlR_DlxlDXzej-q5fZzWXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایلان ماسک:
«ایلان،
توماس ادیسونِ دوران ماست.
»
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72963" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72962">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVcAyzgbFI9HTWSxmJf3Y1MntbWW4q4OV6sqLgowf-4wTBUsspRuQ31sc-EaM51jWsGD9k2iLJV8MXZkZoXvYKYbeB9o8i1krcBO37_MVWk2CxLKcX9ehH6PHtrbkLcrkHk-fY2-VPp5p-uq63q1VzCbyjeLCIl8RFP_WS8joWbOT5oEU-zeGTo_S_t1zx2cXmUIp_fcvh-UOgnrRhQtD_KuQkVJhkbYJL2QdCEbNl_1_y9tkyEbb1ZLlSt8N2dvA9dcWHv_QrE3wssrhFPLfjScoc2iN09xy3GGppfRelZbGijmjC0ezoD4yTYaSyGom4-MF_04GfkquAVTDQPUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، ژنرال ایال زمیر، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که ازسرگیری جنگ با ایران طی سه هفته آینده ممکنه اسرائیل رو مجبور کنه انتخابات ۲۷ اکتبر رو به تعویق بندازه.
«زمیر نگران بود که ایران در واکنش، اسرائیل رو با حملات موشکی هدف قرار بده. این هشدار بعد از اون مطرح شد که مقام‌های آمریکایی او رو در جریان آماده‌سازی‌ها برای ازسرگیری عملیات نظامی علیه ایران قرار دادن.»
«ترامپ از اون زمان اعلام کرده که آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.»
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72962" target="_blank">📅 21:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72961">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=Tx-KVLjJJocPJwxdQvskaLABsYanwe1T5-po1mI8ujxiYP4NZhmJgtN7DPiDE2fjDBOberqZ3kztEXqPsMBT-Q6BmIiX6GNeoJ61kqJau2wwjf_b4z0k0WoMnBHvl4t3ciZ4YR7xT-aJX_INK99Xn1eaEgxjviUeriJDlwGODksrqlSbL-68ihxgYkDVO_2bNXDT4RXzEfIjXRNaQ6uTLKaOg6bwt7sGyxAjFkhsRjx0tZNNu042c19wBefvlkCd0HPwHmQrhlhpM7JRd6cRqRn8vQtTIHpmNQpY27QvO7q-fpCBICJehLOXCTrRE2HFVogBeesUl60X9VzmqwXMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=Tx-KVLjJJocPJwxdQvskaLABsYanwe1T5-po1mI8ujxiYP4NZhmJgtN7DPiDE2fjDBOberqZ3kztEXqPsMBT-Q6BmIiX6GNeoJ61kqJau2wwjf_b4z0k0WoMnBHvl4t3ciZ4YR7xT-aJX_INK99Xn1eaEgxjviUeriJDlwGODksrqlSbL-68ihxgYkDVO_2bNXDT4RXzEfIjXRNaQ6uTLKaOg6bwt7sGyxAjFkhsRjx0tZNNu042c19wBefvlkCd0HPwHmQrhlhpM7JRd6cRqRn8vQtTIHpmNQpY27QvO7q-fpCBICJehLOXCTrRE2HFVogBeesUl60X9VzmqwXMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی معلم به دانش‌آموز در هنرستان؛ سقوط اخلاق در نظام آموزشی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72961" target="_blank">📅 21:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72960">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72960" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72959">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i04yPwixFGYkYl4RhPKBWKLX_jmo1_CnktoAnqh0yEfFGhsSVC88NiO0k7D03Jygal5dnl2zkuaB8IdGWe_l3-50aDLVmexNxC6W9ox6yf8aOtd1tRiln08xkCfC00Ru2WBu6Soc4ah-WxqjBwGae1o841UVQsqZd3zsdpCehNOsYZVOwYrJdWv_-3UUIcQ0hyoGf5aSoGHaepwPb0_EmTBBRFLEMbPvBzzrMmmrpngwGKBS_SKbCmqwbylfA7JRtdOZ238WiROcY06Ai5i0fA7vc96SBPIpiEjDBrYRtyqQjV723X0HTygzAhxqn2Xhta-1r4dorp0ROpC986TE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
ترامپ درباره ایران:
«ما در حال انجام مذاکرات سازنده‌ای با جمهوری اسلامی ایران هستیم.
می‌خوام برای همه روشن کنم که با وجود اینکه ایران هم از نظر اقتصادی و هم نظامی در وضعیت بسیار بدی قرار داره، و با اینکه محاصره همچنان با قدرت ادامه خواهد داشت، نفت با رکورد بی‌سابقه‌ای از تنگه هرمز عبور می‌کنه؛ فقط دیشب ۲۲ میلیون بشکه نفت از هرمز عبور کرد، بدون اینکه حتی یک بشکه از ایران وارد یا به ایران ارسال بشه!
ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72959" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72957">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB1xxNrUN5VsrM968vwb9TVKAazN82jkEdXG2bZptj3dbzWSeksX4e6A9Ou_j-KNNPE85ehEWf60F5XGDLFmPJnxGDj04putwF3PQrJUL1aw2nl-Tn1TlcSNB3t9-mZHKLam93zsZjNVeYQVo_4pUfN895_zKf6Cgy9U26sRWZs1yaVV01ApdieW1E_vkXB9laNf7foIuRxoH-BaS1fZyrKMETmaBo4ZUKi6n3DwXjkkJClRIK3lEj-pK32CJTN-2D8EwrFGJmw3ctD5mvfX05iqxBInHQ5f6N9gmXy0Pa7ZMSdEtfuuXDGYO6XfeAvhRqzMeTXV1vl4ultNciigNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=bQdyH8X0cxIW5Ho1PLFxT9SCg6ZKZidCGBak0GyPPjOVhhXCdxfpRnu6gowOc41-mj2r3VBc3TlbXeAMLQtEaM91_BpzSbwibMh0ipH1aLzb9sm6VnLMVkU5qC9tLyfHUnb9bkGLOz76R-GNpiUqORgxHafL56kRvqZbRUy907aO_6j7b7conVkSUbXc9AMRjENncYVaWcwMxGzv-YAwCEjrxE4679eU5y2HACnjg5ToSNc_FF7BypS-GcWPYtrkKCdyxUcdgOHG1pyxjSwHU3z5DcXJ0qwJgLEH3n_JiTi0mZN0IlwbzGHsTVGuXoSJ8W-DzyW5Mjrd8yPNyL9Z8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=bQdyH8X0cxIW5Ho1PLFxT9SCg6ZKZidCGBak0GyPPjOVhhXCdxfpRnu6gowOc41-mj2r3VBc3TlbXeAMLQtEaM91_BpzSbwibMh0ipH1aLzb9sm6VnLMVkU5qC9tLyfHUnb9bkGLOz76R-GNpiUqORgxHafL56kRvqZbRUy907aO_6j7b7conVkSUbXc9AMRjENncYVaWcwMxGzv-YAwCEjrxE4679eU5y2HACnjg5ToSNc_FF7BypS-GcWPYtrkKCdyxUcdgOHG1pyxjSwHU3z5DcXJ0qwJgLEH3n_JiTi0mZN0IlwbzGHsTVGuXoSJ8W-DzyW5Mjrd8yPNyL9Z8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر تأیید می‌کنن که یک هواپیمای شرکت هواپیمایی سعودی (Saudia) که در فرودگاه بین‌المللی ملک خالد ریاض متوقف بوده، در حمله موشکی اخیر حوثی‌ها (انصارالله) هدف قرار گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72957" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72956">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=DX3TLaI1y0VWdUWV2naWEcKS3Dtguf3yjUk6sYyd4V6Y90ulnroYQTBHt7NlS07Q9xyK_Aw6hz6eYGKgx76vTEqUXfgFtVukOEtOp3UH7YPPhjJ0RPef_mpgKN5E5NaSOY3Z2hm45G2El_2npAtTTcP5fuUbdR9YK9cQg9wUa_IX41D-Vwr0eBGT7-xwA0TQ-ZvnJcghU-OTY6-G9_5zQO_kJGMdNuLc6Z-neexW4is8DbuWo5fSxiODS9ikqPKZ4YgO_RehFj2WfUT_V9Hp5Ufd8GnagVkTRsLCXqcfawJvjbv_8BdIIslDVqs0KL4GnLw2E34OvNz7xf9t8YCUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=DX3TLaI1y0VWdUWV2naWEcKS3Dtguf3yjUk6sYyd4V6Y90ulnroYQTBHt7NlS07Q9xyK_Aw6hz6eYGKgx76vTEqUXfgFtVukOEtOp3UH7YPPhjJ0RPef_mpgKN5E5NaSOY3Z2hm45G2El_2npAtTTcP5fuUbdR9YK9cQg9wUa_IX41D-Vwr0eBGT7-xwA0TQ-ZvnJcghU-OTY6-G9_5zQO_kJGMdNuLc6Z-neexW4is8DbuWo5fSxiODS9ikqPKZ4YgO_RehFj2WfUT_V9Hp5Ufd8GnagVkTRsLCXqcfawJvjbv_8BdIIslDVqs0KL4GnLw2E34OvNz7xf9t8YCUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:اقای همتی قرار بود وضعیت دلار بهتر بشه پس چیشد؟
همتی کله کیری: فقط به اقای بسنت بگید 3 روز بیشتر وقت نداری
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72956" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72955">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=RnibOGcfo8ekQim19LiMA-qUxipnE13XbcMZtDGjT9BgDEMtGhArwquH3CCacTBG5Vp7mqm-OdV4l5U16PqKuHGZxLB1IsO7UJOOTmU2IwYFoC9isC0aaySMi4IKLurPM3nrVxCHJY93YQi2K23RwA-0L2ALFc6yV6Mhyspk9mkEjxp2n1wXuNw1faNh8Jw9MavDLA1pAwG28xNW0CqpjiVeP__d5igQxqp3M80_c2Le4V7L332Yua4IuFbD57N6TGkdRvV61hUmHTi3e2ZT63sHS5EUpHKUOca7nOXcKUR-byvicROKS8tDsbUOqt5gAnHANqTkZtczOkLb2qY2zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=RnibOGcfo8ekQim19LiMA-qUxipnE13XbcMZtDGjT9BgDEMtGhArwquH3CCacTBG5Vp7mqm-OdV4l5U16PqKuHGZxLB1IsO7UJOOTmU2IwYFoC9isC0aaySMi4IKLurPM3nrVxCHJY93YQi2K23RwA-0L2ALFc6yV6Mhyspk9mkEjxp2n1wXuNw1faNh8Jw9MavDLA1pAwG28xNW0CqpjiVeP__d5igQxqp3M80_c2Le4V7L332Yua4IuFbD57N6TGkdRvV61hUmHTi3e2ZT63sHS5EUpHKUOca7nOXcKUR-byvicROKS8tDsbUOqt5gAnHANqTkZtczOkLb2qY2zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن زنگنه نماینده کاکولد‌زاده مجلس:
قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
البته قرار بود سهم بیشتری بهشون بدین اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
@News_Hut
😐</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72955" target="_blank">📅 18:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72954">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=hKxK8TfugHak31d_Y25jZpamExEJqRM0tbdx0GaD9NS3OitrdOmWXZDYfwluJwM-ORLvw1T-Yv_mjxXeMZAatuwJda2pUEtp2zX6pg8_LB6O6cF3xwH6ozPmM_wMW-sP9lABaTyunwIkHwj_AZNHkXBZznoRA35gZVw4lbpoTCn1SpEwzYifQI-LXgLT1GeXa8I6P6sv-W4sQXEU46XnpMDHJC9EbTcM3t9t7FKDCCKR-vN0yXhjr2frWpPGF5ZfHd0JPP0uMjrAXhoE3WuJSxNWt2iP-1Cur7gklqURABHMge1JKvaqPHVAC3YKo93qyGpmJk0a4dwtEV752phe-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d8b68a96.mp4?token=hKxK8TfugHak31d_Y25jZpamExEJqRM0tbdx0GaD9NS3OitrdOmWXZDYfwluJwM-ORLvw1T-Yv_mjxXeMZAatuwJda2pUEtp2zX6pg8_LB6O6cF3xwH6ozPmM_wMW-sP9lABaTyunwIkHwj_AZNHkXBZznoRA35gZVw4lbpoTCn1SpEwzYifQI-LXgLT1GeXa8I6P6sv-W4sQXEU46XnpMDHJC9EbTcM3t9t7FKDCCKR-vN0yXhjr2frWpPGF5ZfHd0JPP0uMjrAXhoE3WuJSxNWt2iP-1Cur7gklqURABHMge1JKvaqPHVAC3YKo93qyGpmJk0a4dwtEV752phe-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌خواید ببینید مشکل واقعی یعنی چی؟ بذارید به لس‌آنجلس حمله کنن، یا به جایی مثل سن‌دیگو حمله کنن. بذارید به یکی از شهرهای بزرگ ما حمله کنن.
اون‌وقت می‌شه گفت
یه مشکل واقعی به وجود اومده.
»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72954" target="_blank">📅 18:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72953">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=EZRBh6v9kSOCsNod083HnVIz3dhsulIVirNvkEREQr6FAQgUXOtVuSQwC73QkBs6d6iPwZKUR8JUVwsHpQjUM4EMnEzf0mN9HMyBC-X4lA_owl55Erlkh3GT5X0-n4lD0jZwpfhtkzvjhR3p2NzfZVQ3-TV6s0hry3u_Z3exLKo6FTobtiEQtsY9lv4IqF2U3T8KKs1gNlNLXjTkghwL6uBa5JMh9ZfeyKF7spYM-2azj9aPEDailg8GGhU5plfR0HlXGNgb13ODeKQvxeWCt5XYz3bFGG_wCfGQWNZuZTmAuNnIL89S-E3nL0-XJQ6tnCrrTiWWk8zgN6W5bsivbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=EZRBh6v9kSOCsNod083HnVIz3dhsulIVirNvkEREQr6FAQgUXOtVuSQwC73QkBs6d6iPwZKUR8JUVwsHpQjUM4EMnEzf0mN9HMyBC-X4lA_owl55Erlkh3GT5X0-n4lD0jZwpfhtkzvjhR3p2NzfZVQ3-TV6s0hry3u_Z3exLKo6FTobtiEQtsY9lv4IqF2U3T8KKs1gNlNLXjTkghwL6uBa5JMh9ZfeyKF7spYM-2azj9aPEDailg8GGhU5plfR0HlXGNgb13ODeKQvxeWCt5XYz3bFGG_wCfGQWNZuZTmAuNnIL89S-E3nL0-XJQ6tnCrrTiWWk8zgN6W5bsivbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما داریم ایران رو خیلی شدید شکست می‌دیم. دیگه تهدیدی از بابت سلاح هسته‌ای وجود نداره.
الان اوضاعشون خیلی به‌هم‌ریخته‌ست.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72953" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72952">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=FNI0-EscIdffMfF34OHfMO3NSfFnnyZljoGzJIC4B6Zlt81K07NKDxjGZJU1X5rR1XoX8o_oW22EdZvszesFTUlP0SbED7s4-K_9HFeJx5bYENe72tY1P2iq2czKqaKSStuB2JtkBVNjcscN0yVkVlVwSPJv9yRpL_gA7kOTq08URjO8x9_2GMHlwjKAr8tc3LTWDRcuVU-6CcWOt1jL_GmeABnBhMGQ1XP-aUfBqT0gOMUWHb3jIMllN4jNq4WOWhc9W65Ms3LvEZ_qNF5LydahvcEUeoJBuTI5M12wfWc4T7efBj4tRWTAI-tU9Ap0LzIwGSeEZfgzNLPlZWmh6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4e1705e.mp4?token=FNI0-EscIdffMfF34OHfMO3NSfFnnyZljoGzJIC4B6Zlt81K07NKDxjGZJU1X5rR1XoX8o_oW22EdZvszesFTUlP0SbED7s4-K_9HFeJx5bYENe72tY1P2iq2czKqaKSStuB2JtkBVNjcscN0yVkVlVwSPJv9yRpL_gA7kOTq08URjO8x9_2GMHlwjKAr8tc3LTWDRcuVU-6CcWOt1jL_GmeABnBhMGQ1XP-aUfBqT0gOMUWHb3jIMllN4jNq4WOWhc9W65Ms3LvEZ_qNF5LydahvcEUeoJBuTI5M12wfWc4T7efBj4tRWTAI-tU9Ap0LzIwGSeEZfgzNLPlZWmh6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه پسر ایرانی :
سرمون درد گرفت شماها ولکن نیستید هنوز تو خیابون
خامنه ای رو خاک کردن عمو کردنش زیر خاک ولش کنید
خامنه ای رو خاک کردن شاه رو مومیایی ؛ ایران یعنی شاه
شاه که اومده بود دانشگاه و مدرسه ساخت
جاده خاکی هارو شاه اسفالت کرد و ایرانو شاه درست کرد
اگه شاه اومده بود تخم مرغ نمیخریدیم 50 تومن ماست نمیخریدم 680 تومن
خداوکیلی من تو این مملکت چطوری باید زندگی کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72952" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72951">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72951" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72951" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72950">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxdc773lpC7wg_z4heSJt30WTbi0ah8I0khPTuTBEGVfhvh5NfDAU0fCgc79DQovo3BZiKz4hev5cWd-I1kEbIIQY0kAZ0eyEHL9pJv35KCWiuRoQd7h138i_KgJdjBtwCXwBnmgubh3X9wzf2p5xTtOaBwn9zd2DN_-lg4bdTQdX7g1RpVmS7kUv8XThyPP6ybE-lGbUW49k_htTW-JL_wdY_yWcc7MDv6GXqcMeUy-5IvihSHSb10yP49IMIbfokfckFzaxOLG3rD08sxXeWaIncS666B40Tk5dBiqDBWN5QpRv1Ri7JLwgcaJqkqo1aq2d_t3RMWajeGivsN0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72950" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72949">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=bPJX6hZ3PtQ36z0UOB5OfhQPicdaa1U83WskIcmyy8KCjwWHadsUAFvUpjibcFg0e5wS7Mt5BMXh1SQS1-7bLySFZRfD6vIbVIKEdzPXcoAZcjlVJfFlq1KVz6Bi_EDMZAkYjvGtUTDUF0wo7gEEAWrnC3FdVYfqgLJLfkh-CicGY-mOqkJHbKCCr0Jc9Nn_GkBj6C-MDLEyxSnpt6rZNZYFamxJeZ8Jj_lkmVtaXTHRF_wMyKq9t7g2c6tsY6tt9eRzCBuPHla1oapGkB589dLJ588MT59f_6ziVGfRUnzwJ7CamhfVxI_b8d2ruvpjJyvPItYT6ea0BkJPNC0Ee5HMcbfyZgEyu9_dfJ8CSB8FknqtiJHvL868pNiAw6xZaetCqX8pl5-pUYd3rrSaE-OREKzAqmL6tDkxZ0XYqHuHXAXZXVovZiysfNt_SqXddJ0iFDKArB8Zi-rdtE_LJcaW2LqfjcO_-JM5yke8--uZPfh6fnctGV1BuwhFM8pCDB0Hqc4HwBjM3U2uf5aeiz6mtz-yJLsgkSnWoGz8cBJa3d3_5YDdLRhDtHaEjUg9bTISMLLAtOkOXMJ2TlXEbyq8aqF601zmxCxzsveYnsSmQIwvuSd-Xc4GYhBViZv50uGWvGJ1Rl6F_RE75b-VdHj4YDiEUBHg0mSgc8O0ZCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9c7d6e9b.mp4?token=bPJX6hZ3PtQ36z0UOB5OfhQPicdaa1U83WskIcmyy8KCjwWHadsUAFvUpjibcFg0e5wS7Mt5BMXh1SQS1-7bLySFZRfD6vIbVIKEdzPXcoAZcjlVJfFlq1KVz6Bi_EDMZAkYjvGtUTDUF0wo7gEEAWrnC3FdVYfqgLJLfkh-CicGY-mOqkJHbKCCr0Jc9Nn_GkBj6C-MDLEyxSnpt6rZNZYFamxJeZ8Jj_lkmVtaXTHRF_wMyKq9t7g2c6tsY6tt9eRzCBuPHla1oapGkB589dLJ588MT59f_6ziVGfRUnzwJ7CamhfVxI_b8d2ruvpjJyvPItYT6ea0BkJPNC0Ee5HMcbfyZgEyu9_dfJ8CSB8FknqtiJHvL868pNiAw6xZaetCqX8pl5-pUYd3rrSaE-OREKzAqmL6tDkxZ0XYqHuHXAXZXVovZiysfNt_SqXddJ0iFDKArB8Zi-rdtE_LJcaW2LqfjcO_-JM5yke8--uZPfh6fnctGV1BuwhFM8pCDB0Hqc4HwBjM3U2uf5aeiz6mtz-yJLsgkSnWoGz8cBJa3d3_5YDdLRhDtHaEjUg9bTISMLLAtOkOXMJ2TlXEbyq8aqF601zmxCxzsveYnsSmQIwvuSd-Xc4GYhBViZv50uGWvGJ1Rl6F_RE75b-VdHj4YDiEUBHg0mSgc8O0ZCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
« سازمان عفو بین‌الملل یه کلاهبرداریه.
می‌دونید به نظر من عفو بین‌الملل باید روی چی تمرکز کنه؟ روی حکومت ایران که ده‌ها هزار نفر رو در خیابون‌های تهران و جاهای دیگه کشور، خونسردانه به قتل رسونده.
عفو بین‌الملل باید روی این تمرکز کنه که حکومت ایران وقتی معترضان زخمی می‌شن، می‌ره سراغ بیمارستان‌ها و اون‌ها رو روی تخت بیمارستان می‌کشه؛ تازه گاهی پزشک‌ها یا پرستارهایی رو هم که اون‌ها رو درمان کردن، می‌کشه.
این‌ها جنایت جنگی هستن، جنایت علیه بشریتن و جنایت‌هایی هستن که این حکومت علیه مردم خودش مرتکب می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72949" target="_blank">📅 17:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72948">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Xi900sIROCts0wQ6bTXmc9bFIRfYBadZdz-1QzFwr2VRH9ffaW13-6iHhPKeA14_NS9roOQZPuqQ1kU9dppzChnrQ_OLEtnNZw9-1LsPpWGp7zbG9EM99_KDrN8cc9CuyOMGz4Yz2m-98pG2RMvEhApoDwLK4TDCDcbxd7SiZdJeooB_HWAnaVB_SYvx2ic8a_trgy6TIsq9hBUqj16bB90Cxdp5abRc4flioKZ2XtlKo3dTHn4fl9aJTZ3822vUVtE9ToUXsCa68lRf0uT2OzJoJ96q6mCQto5L6YTNcVQgoXv5W4dZMFHA9EBQtSaicBAwjVDeKM0TvpRFaiZB_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2503fbcfb1.mp4?token=Xi900sIROCts0wQ6bTXmc9bFIRfYBadZdz-1QzFwr2VRH9ffaW13-6iHhPKeA14_NS9roOQZPuqQ1kU9dppzChnrQ_OLEtnNZw9-1LsPpWGp7zbG9EM99_KDrN8cc9CuyOMGz4Yz2m-98pG2RMvEhApoDwLK4TDCDcbxd7SiZdJeooB_HWAnaVB_SYvx2ic8a_trgy6TIsq9hBUqj16bB90Cxdp5abRc4flioKZ2XtlKo3dTHn4fl9aJTZ3822vUVtE9ToUXsCa68lRf0uT2OzJoJ96q6mCQto5L6YTNcVQgoXv5W4dZMFHA9EBQtSaicBAwjVDeKM0TvpRFaiZB_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنج اصل عدالت اجتماعی شاهنشاه آریامهر برای ایران:
1- غذا برای همه
2- سقف بالای سر همه
3- آموزش رایگان برای همه
4- درمان رایگان برای همه
5- اشتغال برای همه
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72948" target="_blank">📅 17:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72947">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=u4Xug5hvYeZDgbUz5l2MWa8qkaKsCObjvlzw3Q05nwT5kjG3Hu4P9RK5dcKpc0GAPtNl9pD8fb-jM7Xt_NHnATvonJFDWVCXbrXcZISMitDj25Ycj_bK4P6w4V2sYUcRsAV9eiY3RBDl7YD6tmWIsTHbt3BIGd72ZTQvx0klSeedBsgorpGbl_Lg0sbAeiPTeHN2W9lb8K4NOpTDq1gRqUZobCB4O0eXn5GB1tCSRUn0XOhHwJ4fse7g8Cbu6qggkejOyCPs_kNK9hd_GBF5VLZ0YtFww581liFUy3Yf7QEzIie6lCdP83n3dyo7iPSu30oExN5yWWIlZCqpM7xZ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb418c058.mp4?token=u4Xug5hvYeZDgbUz5l2MWa8qkaKsCObjvlzw3Q05nwT5kjG3Hu4P9RK5dcKpc0GAPtNl9pD8fb-jM7Xt_NHnATvonJFDWVCXbrXcZISMitDj25Ycj_bK4P6w4V2sYUcRsAV9eiY3RBDl7YD6tmWIsTHbt3BIGd72ZTQvx0klSeedBsgorpGbl_Lg0sbAeiPTeHN2W9lb8K4NOpTDq1gRqUZobCB4O0eXn5GB1tCSRUn0XOhHwJ4fse7g8Cbu6qggkejOyCPs_kNK9hd_GBF5VLZ0YtFww581liFUy3Yf7QEzIie6lCdP83n3dyo7iPSu30oExN5yWWIlZCqpM7xZ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر جوگیر شد و می‌خواست جلوی چند تا دختر خودی نشون بده که این شکلی بگا رفت:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72947" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72946">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=kE8wZTq0Q3Tf6DbjsEur9cQJgszd_XfStTl4-zTqTW8isL44Y4tY8_K2DpRGQLQAUJ1UEafyD2MJEEHJ5kskckGcAWIGMwA1vuYkdoNy-zOYfeYVcMDrXHZw9c2ZQ5oI712yDmJVaxpQsJtVOKPnCBpBkXzIGF5wJb9zSQ4jFXgRZlLrnQg14mRkgEF8IVGsw8K2kWIJvZrxa9pBrxiZFoSS4ZaoYbUsxjXj0matAtkWdm5mD3A-BELH_XMy9_fnd3gfTKXrVG4KuYsuOSyWsz87UQUYPF_S7HJE2Ip8y6EAiu8LvfRE_4mtbke42TMpL4rXHLbSqE1vx2rgSUvbMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadae5258f.mp4?token=kE8wZTq0Q3Tf6DbjsEur9cQJgszd_XfStTl4-zTqTW8isL44Y4tY8_K2DpRGQLQAUJ1UEafyD2MJEEHJ5kskckGcAWIGMwA1vuYkdoNy-zOYfeYVcMDrXHZw9c2ZQ5oI712yDmJVaxpQsJtVOKPnCBpBkXzIGF5wJb9zSQ4jFXgRZlLrnQg14mRkgEF8IVGsw8K2kWIJvZrxa9pBrxiZFoSS4ZaoYbUsxjXj0matAtkWdm5mD3A-BELH_XMy9_fnd3gfTKXrVG4KuYsuOSyWsz87UQUYPF_S7HJE2Ip8y6EAiu8LvfRE_4mtbke42TMpL4rXHLbSqE1vx2rgSUvbMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو گرگان یه دختر 19 ساله میخواسته خودکشی کنه که اینطوری نجاتش میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72946" target="_blank">📅 15:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72945">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=H3Jo9OXE1HKkQ0W54JSqE557_qhAgXgj8rV-_Ww-xICtqLsaFk5c9pkJ_95cZFvzEDr9c_gjktMyyj25TyTAD1VDE3Ab1Wqo3R2fcpAHrUJ17cZ2r6jyv4qCOBgNmI5WmPp2PKOk2fJBFDoODoRdJcRtMA5_yXQ9URXELbXMVRsy52yApMw4JMLbWKFfiYBSuYcetaxjkkyezzNCg_YzT_AHM4L6UAr6RiB0TbgkQWaPR7ROw2V05XXKxB4xy8W-a5Yf7qavazCUEQVnQlMqsy8JaSPioXyGAo1aNEpgJBhKl7Y-RMopB8_a5jXGU_2FlcrdTj2gwo-cmbhfm6WGig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583782fcd3.mp4?token=H3Jo9OXE1HKkQ0W54JSqE557_qhAgXgj8rV-_Ww-xICtqLsaFk5c9pkJ_95cZFvzEDr9c_gjktMyyj25TyTAD1VDE3Ab1Wqo3R2fcpAHrUJ17cZ2r6jyv4qCOBgNmI5WmPp2PKOk2fJBFDoODoRdJcRtMA5_yXQ9URXELbXMVRsy52yApMw4JMLbWKFfiYBSuYcetaxjkkyezzNCg_YzT_AHM4L6UAr6RiB0TbgkQWaPR7ROw2V05XXKxB4xy8W-a5Yf7qavazCUEQVnQlMqsy8JaSPioXyGAo1aNEpgJBhKl7Y-RMopB8_a5jXGU_2FlcrdTj2gwo-cmbhfm6WGig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هیچ کاری نیست که بخوایم یا لازم باشه در قبال ایران انجام بدیم و
هنوز نتونیم انجامش بدیم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72945" target="_blank">📅 15:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72944">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=GnQxJMUvzDPzldeCxliodX_tDNEgFvDxAnudIfWsRVW8ab8DKYjMJpyAsTgmlOgfS3O7ODjRmjo8aOm2kZeGgLCT5NVzegdZjd41SWgyp6Gm3fXWr2FJq3tWLEbn9hBikJewi_vBqopC1UwAp6yj3YIuI-U_7niE1YnHVWXUqtOkH5g2jQM_WI5cvJc87gG8fz5VW3NSxGCVPtm3RS7GnLYEUPCGPC_lzcEgikpVLN1jpdb_TAVQp1Fz66GrXakRPtOyrz_72--pUdkxY0htOfJpOlriV95CGQm-fOkqi_zXTYpK3OKxAC2pbn6Pq_Edt2bDXrIyXC1ZySs9Wv1Dyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85939dfb7b.mp4?token=GnQxJMUvzDPzldeCxliodX_tDNEgFvDxAnudIfWsRVW8ab8DKYjMJpyAsTgmlOgfS3O7ODjRmjo8aOm2kZeGgLCT5NVzegdZjd41SWgyp6Gm3fXWr2FJq3tWLEbn9hBikJewi_vBqopC1UwAp6yj3YIuI-U_7niE1YnHVWXUqtOkH5g2jQM_WI5cvJc87gG8fz5VW3NSxGCVPtm3RS7GnLYEUPCGPC_lzcEgikpVLN1jpdb_TAVQp1Fz66GrXakRPtOyrz_72--pUdkxY0htOfJpOlriV95CGQm-fOkqi_zXTYpK3OKxAC2pbn6Pq_Edt2bDXrIyXC1ZySs9Wv1Dyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
«روند مذاکرات همچنان ادامه داره و پیام‌ها از طریق میانجی‌ها رد و بدل می‌شن.
ما پیشنهاد خودمون رو که اسمش رو «طرح هفت‌روزه» گذاشتیم ارائه دادیم و دیدگاه طرف آمریکایی درباره این پیشنهاد رو هم شنیدیم.
الان داریم نظرات آمریکایی‌ها رو بررسی می‌کنیم و فکر می‌کنم طی چند روز آینده پاسخ خودمون رو ارائه بدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72944" target="_blank">📅 15:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72943">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c679392.mp4?token=p7sBWluIFQfT96cGehuekcpxuGwzj3Rwd50o2cNgYCL8cylV-mEXlZXppaw1B2spBxBxLBNe2m0f7yuLI2FfOobcUwYEl-iVK-4ze8jaJeaaGw7WDZUvimkvUcMx4lnZ8nHoY8483FQjLGXPgJ3z5vJIzmEbIh1hs2ic-XN4Mq1tk1_TtFwQUK9vCSmzreX1Knj15Hjxcdmihmepb-GtoS7IliEzgH75b8pt_N_Y128vIm1whn7fPXUEXFtkzTGgjkB_UGdbLV14CT_cGYzI20SU3pb92XGdJKOSigKVPw0JIl6EvbrWeUIj20VhgUZR6AsIztl8ajFrWvqAa0-QZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c679392.mp4?token=p7sBWluIFQfT96cGehuekcpxuGwzj3Rwd50o2cNgYCL8cylV-mEXlZXppaw1B2spBxBxLBNe2m0f7yuLI2FfOobcUwYEl-iVK-4ze8jaJeaaGw7WDZUvimkvUcMx4lnZ8nHoY8483FQjLGXPgJ3z5vJIzmEbIh1hs2ic-XN4Mq1tk1_TtFwQUK9vCSmzreX1Knj15Hjxcdmihmepb-GtoS7IliEzgH75b8pt_N_Y128vIm1whn7fPXUEXFtkzTGgjkB_UGdbLV14CT_cGYzI20SU3pb92XGdJKOSigKVPw0JIl6EvbrWeUIj20VhgUZR6AsIztl8ajFrWvqAa0-QZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک جت جنگنده F-16 نیروی هوایی ایالات متحده که در حال سوخت‌گیری توسط یک هواپیمای تانکر سوخترسان KC-135 در جریان انجام ماموریتی در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72943" target="_blank">📅 15:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72942">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=neXfrLw_EMiaKNBqBes1BywG-Ivh1Cd1MmxR68QRwptHo5Bz_6gWTU0aYO5f5AfXesXeQWtWnFTbVVZISNEdUNv9_sXN97UgowSTVl-LhW2NVRir6JSpQScMkdxyBuSGOKcCbflqut0nDveBX0bx9SXPlqWroUSladEv8uafnTCEfCSVbtYybd_s8FrxefcddQb1OiE3dscRRUYcczJZGRFmiqOFdjLW1UXpFbm7_C7IQT_duH5_lsv2U1Nkto9SJ5tIP4g6tMK9EZjOlKglmKZADLjVZ785CO2fvMoB-16KZ0-uKSlsS03i97NoUOyYOVjfV3QQeqiUjJ392wfEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5ddfc1fa3.mp4?token=neXfrLw_EMiaKNBqBes1BywG-Ivh1Cd1MmxR68QRwptHo5Bz_6gWTU0aYO5f5AfXesXeQWtWnFTbVVZISNEdUNv9_sXN97UgowSTVl-LhW2NVRir6JSpQScMkdxyBuSGOKcCbflqut0nDveBX0bx9SXPlqWroUSladEv8uafnTCEfCSVbtYybd_s8FrxefcddQb1OiE3dscRRUYcczJZGRFmiqOFdjLW1UXpFbm7_C7IQT_duH5_lsv2U1Nkto9SJ5tIP4g6tMK9EZjOlKglmKZADLjVZ785CO2fvMoB-16KZ0-uKSlsS03i97NoUOyYOVjfV3QQeqiUjJ392wfEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا پسر رفته بودن بیرون که دیدن رفیقشون اونارو پیچونده و با یه دختر اومده بیرون،
این لاشیام رحم نکردن و اینطوری شرف رفیقشون رو بردن:
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72942" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72941">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=iAFB0KOV3mbfs1jsGV4HnEjgQS3WTaVHg6gV-s4UMO2yiq_v5nIaAQKMBZNrgf6Fz8Luo4-KlL3uQciQ7oecRPLxzYVrT5h9ojHYoBQURqzyo5bkwOKmXd8OcY_g9tAiA6lX3hbJq5L5qqS1MQw4L7zxqQHEmUsch4e-nhOd9mh6GJu-547pI4-Pi4lCXyrkgcxdygdkyThEGOcWlJLNNDdbo1T1-UYgR3lmNJsFO_afQIO-fL8Hlsv71_lO2Cj8v190iECVE7zo27hP6NN-GTNi939YAMHLHBHKBfZtFOxkkPb1mMs4QdXnQp2ADpbl5gPZDOYWsCSixwDJuR479Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6867894c.mp4?token=iAFB0KOV3mbfs1jsGV4HnEjgQS3WTaVHg6gV-s4UMO2yiq_v5nIaAQKMBZNrgf6Fz8Luo4-KlL3uQciQ7oecRPLxzYVrT5h9ojHYoBQURqzyo5bkwOKmXd8OcY_g9tAiA6lX3hbJq5L5qqS1MQw4L7zxqQHEmUsch4e-nhOd9mh6GJu-547pI4-Pi4lCXyrkgcxdygdkyThEGOcWlJLNNDdbo1T1-UYgR3lmNJsFO_afQIO-fL8Hlsv71_lO2Cj8v190iECVE7zo27hP6NN-GTNi939YAMHLHBHKBfZtFOxkkPb1mMs4QdXnQp2ADpbl5gPZDOYWsCSixwDJuR479Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت مارکو روبیو درباره حمله و تصرف آتن در جریان لشکرکشی خشایارشا به یونان در سال ۴۸۰ پیش از میلاد:
۴۸۰ سال پیش از میلاد، در جریان لشکرکشی خشایارشا، پادشاه هخامنشی، به یونان، ارتش ایران به آتن رسید و بخش‌هایی از شهر و بناهای مقدس آن را ویران کرد.
بیشتر مردم آتن پیش از رسیدن سپاه ایران، شهر را تخلیه کرده و با کشتی به جزیره سالامیس و مناطق اطراف پناه برده بودند؛ اما گروهی از مدافعان حاضر نشدند خانه‌شان را ترک کنند.
آن‌ها در دژ سنگی آکروپولیس سنگر گرفتند تا در برابر سپاه ایران آخرین مقاومت خود را انجام دهند. مدافعان با پرتاب سنگ از فراز صخره‌ها تلاش کردند نیروهای ایرانی را عقب نگه دارند و برای چند روز در برابر بزرگ‌ترین امپراتوری‌ آن دوران مقاومت کردند.
اما سرانجام سپاه خشایارشا موفق شد آکروپولیس را تصرف کند. ایرانیان معابد و بناهای موجود در آکروپولیس را غارت و به آتش کشیدند و بخش زیادی از آن را ویران کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72941" target="_blank">📅 14:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72940">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=I6pdDuHhSu6mh2KFKouThqoiPO6UdLZSw3f5GTj4z-Kf6pD5wKn_qbIu4wngabTkxsxH96ngUNQSYGsF50cQaf7U0_8uaTUyr6WEXjYFYEzoIWYC-bSspuW_-zDJNBcwqDE-GE1_r1coCpZKj3zflaqqeOFmgzpc19ry3Dgv730ffDx5V34sIlPeMEQnwgr24xdZhLpoOM8A2ta6CmVtjNl4g8kI2Z8z_7ZNl9uc-BwB-8ebwbzReehccsZENx_RsoniUKn4aAE2PL66ZN4CkHv-woUg6PFJ6JayFVtxpqGdoTr0iAWNOqu0f4w5B9fafR6ZihceuHuciCagKux1cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e1f63945.mp4?token=I6pdDuHhSu6mh2KFKouThqoiPO6UdLZSw3f5GTj4z-Kf6pD5wKn_qbIu4wngabTkxsxH96ngUNQSYGsF50cQaf7U0_8uaTUyr6WEXjYFYEzoIWYC-bSspuW_-zDJNBcwqDE-GE1_r1coCpZKj3zflaqqeOFmgzpc19ry3Dgv730ffDx5V34sIlPeMEQnwgr24xdZhLpoOM8A2ta6CmVtjNl4g8kI2Z8z_7ZNl9uc-BwB-8ebwbzReehccsZENx_RsoniUKn4aAE2PL66ZN4CkHv-woUg6PFJ6JayFVtxpqGdoTr0iAWNOqu0f4w5B9fafR6ZihceuHuciCagKux1cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جهانگیری: از سال ۹۷ تاکنون چین حاضر نشده یک بشکه نفت به صورت رسمی از ایران بخرد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72940" target="_blank">📅 13:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72939">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حمله ایران به پایگاه آمریکا در کویت؛
طبق تصاویر جدیدی که CBS منتشر کرده، ایران در روزهای ابتدایی جنگ، پایگاه آمریکا در «کمپ بوهرینگ» کویت را با موشک‌های بالستیک، پهپاد و جنگنده‌های F-5 هدف قرار داده است.
در این حملات، انفجار و آسیب به ساختمان‌ها و تجهیزات نظامی دیده می‌شود. یکی از شاهدان گفته جنگنده‌های F-5 آن‌قدر نزدیک پرواز کردند که حتی کلاه خلبان‌ها را می‌دیده.
@News_Hut
| CBS</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72939" target="_blank">📅 13:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72938">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beJQSl6F0femEvrDlXtJaohoRVWnb6URBeMn999A02yRbdEB8NfPg9rXaFZcCqVbXidTIsKAjT8Zfx-BW-dC1nBDmWnLErpJQBHZmn4rhJpAB-nWo8jd7ruzIT_UrfhyXi5NhSXzzupT3XLVzSL4SxxK81z7PDmk14VxjY14JZQUGBv4gn7EbQdzJWuPaMlI1gWlpte4wrgyysNBoVQYlP4GTaR4CT7XKsb11Q96W5oI__7-AeJRXNvsl1fWhWo5xFZZDpNAF4fUPwYROebzKABYNjZUSqFy-ufwl9f61rhIzXvxefjbbAPgcsoDxinA6w2zLXfSFL-21Ek_MZC9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی:
لئو، سال‌ها برای کشورت جنگیدی و یه تاریخ موندگار ساختی. بابت همه چیزایی که با آرژانتین به دست آوردی، دمت گرم و کلی احترام برات قائلم. بغلت می‌کنم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72938" target="_blank">📅 12:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72936">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnp1Y-85G9RgRyUM6UahvgS4yUtkri1C5uIhjonJ-m4Mkhtrex7zhBNlT2cefcRB10qzTAJwPCPGXnDWUJo0W_NKYm-ThMjgtb8OEk5qYskElac2DFise5VRS99cl8WXMN2tT6s1W4OBJWhuBO85tYAsr7ptnANBkQDpm0mHNZtHH6cRZht3CpdCwOmk4L_uzEK3Dcw1wEYWbugUEplQtW434OrSdnwzZggbpMzn62zUW9KLSC8JGZC3W1z8h_xhCri-dPEqTiE5s_an1i-D9SWURyxZDpjKIPxZVzCZ-V3xylQVbDyc8af1544fxbh2qeNdEgKZYCEL7hn4fzJ8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=B3rQjD5r2awTgZe2dHFe0G1KzOtK0gJItg4WRduNJi38-Y45osuMycNaiRpVhtsfWZaOV-tcdyDwBaJabCQYEWMMCMQfNAFdYU4ldriGhtXLJ362CvK3CwH4Mwoq0ahiqKvs0uM63FKontaARY1WLfjVNhjHfigOy4nh8vDFJIF3_4QtWMufQxJr24PlOR7Q_wsshvoVpS3QIp0CF7LagS-vk6xKul_2smkxiUIytiCukJXrzAHgsuMtg6fDis3VaUCyglWSQTM10G79589bSDYTSRJSIjc9rId2_a4KWvLQsSBaaVkyqG7J75DH_FLx5b2CtwmF8Kzh6hHTONcMlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5f1c5b88.mp4?token=B3rQjD5r2awTgZe2dHFe0G1KzOtK0gJItg4WRduNJi38-Y45osuMycNaiRpVhtsfWZaOV-tcdyDwBaJabCQYEWMMCMQfNAFdYU4ldriGhtXLJ362CvK3CwH4Mwoq0ahiqKvs0uM63FKontaARY1WLfjVNhjHfigOy4nh8vDFJIF3_4QtWMufQxJr24PlOR7Q_wsshvoVpS3QIp0CF7LagS-vk6xKul_2smkxiUIytiCukJXrzAHgsuMtg6fDis3VaUCyglWSQTM10G79589bSDYTSRJSIjc9rId2_a4KWvLQsSBaaVkyqG7J75DH_FLx5b2CtwmF8Kzh6hHTONcMlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داریوش بزرگ؛ نامی که پس از بیش از ۲۵ قرن هنوز در تاریخ ایران می‌درخشد.
پادشاهی که ایران را به یکی از قدرتمندترین و سازمان‌یافته‌ترین امپراتوری‌های جهان تبدیل کرد؛ از ساخت تخت‌جمشید و گسترش راه‌ها تا سامان‌دهی نظام اداری و اقتصادی کشور.
داریوش تنها یک پادشاه نبود؛ بخشی از تاریخ و شکوه ایران بود؛ نامی که قرن‌ها گذشت، اما از یاد تاریخ پاک نشد.
امروز، به احترام مردی که نامش با شکوه ایران گره خورده است؛
یاد داریوش بزرگ گرامی باد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72936" target="_blank">📅 11:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72933">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duIp-Hypr9lSLHS8Nj_uk7UxckHAllc1mN9G399UlQU1jJYcul0Fk5ze5csWyS1KtjiS0o0ToCoA2STYBG0lowf-NtRiI2LdvW1UmpeXOisflOeykGMhsg82k8fZyVRI9Jh1eoPlsFIzgz4eNnm0byubxjQBAeaFNVVIjh928pQc8kce9WnF4kW0mZmv-ENbU98jFAE4DGYB5EhFkwem3cYHAVMKR0ADw63_GnA8X5EjXJVfEDJDRti4M90OB9gdZbTfogCV-hAFHPw92ZPFDxWojcHqGnEA0Y99NZmy8uwYX1xIeotj9PxgMUUjkVB7BlGc2qcgYCwfuJudTOthOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۲۴ ساعت گذشته، ۱۱۰ فروند هواپیمای نظامی در منطقه شناسایی شدند که شامل موارد زیر بود:
۱۶ فروند هواپیمای ترابری ورودی از خارج از منطقه (متشکل از ۱۱ فروند آمریکایی
۲ فروند بریتانیایی
یک فروند ایتالیایی
یک فروند آلمانی
یک فروند با مبدأ نامشخص
۱۰ فروند هواپیمای ترابری نظامی منطقه‌ای
۳۳ فروند تانکر سوخت‌رسان هوایی
۲۱ فروند هواپیمای شناسایی
۲۶ فروند هواپیمای ترابری نظامی فعال در داخل منطقه
۴ فروند بالگرد نظامی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72933" target="_blank">📅 11:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72932">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlJG3Km_6GHbHJ7eVSfn2NJTbrb5iJBmEmwmXmjajqLgbi9xR-7ZRYEPECWnEWitE_dV0Edi8NE-D0TorNOTxqILkGsrnvjwybAQI5TbMlT7tChVH_d6xjmxn9r_IwIZBYhMT5NfWj3quA2sNvzMv2FCb_hI2f36Iic0-62sf8uDmBJXxUTZ9Wh92vKroaTwYbvfZzaGIRR_xfIqdESmlvNDIMN3GXK8_u30l8A3ftyN8cCbLJtza9Kk3nZj4ptYDR_IFprgTjO8teh4uzy_WpDk0CYz8pZ0efg787LMhJhhb4t6Gx6AA620_Tx05CfNqoggQj1MYg-tE4MkrX3Ygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
پنتاگون به ارتش آمریکا گفته خودش رو برای حملات احتمالی دوباره به ایران آماده کنه:
طبق این گزارش، هنوز دستور نهایی حمله صادر نشده و ترامپ همچنان درباره زمان و اصل حمله تصمیم‌گیری می‌کنه.
اگه حمله انجام بشه، احتمالاً اهدافی مثل تأسیسات هسته‌ای، زیرساخت‌های انرژی و دیگر اهداف راهبردی ایران مورد حمله قرار می‌گیرن.
منابع آمریکایی و اسرائیلی می‌گن احتمال انجام عملیات قبل از انتخابات آمریکا و اسرائیل مطرحه.
همزمان، تیم امنیت ملی ترامپ درباره جنگ جلسه داشته و ترامپ هم طی چند روز اخیر دو بار با نتانیاهو تلفنی صحبت کرده.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72932" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72931">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72931" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72931" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72930">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc-J_eahDvELSVHzYwmT1MY4_ZZUtwV_hHPN4F3E323RyD4x3BToW7zYgqpxUMYB8WJHtb3Ti5wA-1z42nAzQUwThTl9TwyyQoy9MTOl1D4oVCHAUphGusFVfWq4Y8_2IjXC4NegabyJ6g2-bBILt7_7bUBjwsYoppV7Wtl4HLj6tzktl4UJamqdE3btW3JXPMjVslztA1ViXnwdWh9Jwdw1PWY3JywUFGLuz1e8sYk7WFmZq7GYkqnbbNswG6CfxpoNiYR_kQi3sd8ieokDDzGaEXN7xX6lb60sdcAUQ8AbrLSYJPF_7sBrpcD_qQlW8v2-adYFPVrViRRStCFM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تراکتور
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
⚽️
تراکتور: ۳ برد، ۱ تساوی، ۱ شکست و ۶ گل زده
⚽️
استقلال: ۱ برد، ۳ تساوی، ۱ شکست و ۳ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72930" target="_blank">📅 10:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72929">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=ekwWdV20EKIgKBdtSqE03WfItYz_AIe581LlKfxoVADtcwyR3zksVmU0lJVmHgrXmBs41gUdcq1ZvrHKPGbFPS6YIIxR-K66O0GrNpSYm8gr4XM-Ry132u3VO_KOmxgjMPACMqHkeHYqiPYtyZVV-tXPc-uLR-W-lQebkOY7C4uqxlRq1U1lI-H95BlVGsQM_rGm_sbAR-eqWc_zJbj9tLlXkVuFSQP6UNWE9JgCvCWbw4SizV-qNZKgZ7ER2hUPkGSC-wekkY6QAJqa7LHWO7A92zDguPc2qBWfZes6fH5_poLD_avvFwa83Stq-T2r04vFHvwqP8CHoMmwXfslqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96ef1b8d29.mp4?token=ekwWdV20EKIgKBdtSqE03WfItYz_AIe581LlKfxoVADtcwyR3zksVmU0lJVmHgrXmBs41gUdcq1ZvrHKPGbFPS6YIIxR-K66O0GrNpSYm8gr4XM-Ry132u3VO_KOmxgjMPACMqHkeHYqiPYtyZVV-tXPc-uLR-W-lQebkOY7C4uqxlRq1U1lI-H95BlVGsQM_rGm_sbAR-eqWc_zJbj9tLlXkVuFSQP6UNWE9JgCvCWbw4SizV-qNZKgZ7ER2hUPkGSC-wekkY6QAJqa7LHWO7A92zDguPc2qBWfZes6fH5_poLD_avvFwa83Stq-T2r04vFHvwqP8CHoMmwXfslqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یه هموطن گفتن که این خونه جن داره، اونم خیلی پرقدرت و باشکوه وارد شد،
اما خروج جالبی نداشت:
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72929" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72928">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=KHuWB7Np5bXaH8kX88emw0T4ohXIAELiTuL6FbuMVJWD3rdf2h8Cmfu544M8hd7EByaT8WRSDR2vkvE39_9j0pYhMI0etGS8RtRw6whdsaqAOBxxmBzMZXZStLpQ-BK7Msi7vx5sRmLgodd366kCFGMhRV7kOUTkRff4qfaX0IMzoXdO7N3fuzRfl3ACN1tvOFioXEt1cIsXHexGfoJRx38E7-PHnHn4IEriNxNhGwO3NspZ0MiAR5ZlbhzOQyLJ8UQyBW-PtXGmKqlg4woQvsqKCYMGA1gXbV7OvyBLpYm9gtY7Skx7Q9JJkNwYeId9OVVOoBnvaDsjrY238NC0FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e69732ec1.mp4?token=KHuWB7Np5bXaH8kX88emw0T4ohXIAELiTuL6FbuMVJWD3rdf2h8Cmfu544M8hd7EByaT8WRSDR2vkvE39_9j0pYhMI0etGS8RtRw6whdsaqAOBxxmBzMZXZStLpQ-BK7Msi7vx5sRmLgodd366kCFGMhRV7kOUTkRff4qfaX0IMzoXdO7N3fuzRfl3ACN1tvOFioXEt1cIsXHexGfoJRx38E7-PHnHn4IEriNxNhGwO3NspZ0MiAR5ZlbhzOQyLJ8UQyBW-PtXGmKqlg4woQvsqKCYMGA1gXbV7OvyBLpYm9gtY7Skx7Q9JJkNwYeId9OVVOoBnvaDsjrY238NC0FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«استیو ویتکاف داره روی توافق با ایران کار می‌کنه و خیلی هم خوب پیش می‌ره.
فکر می‌کنم این توافق واقعاً چیزی نیست که بخوام انجامش بدم، اما ایرانی‌ها حاضرن برای اینکه این وضعیت متوقف بشه،
هر چیزی که ازشون بخوایم پیشنهاد بدن.
»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72928" target="_blank">📅 10:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72927">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ درباره ایران:
«همون‌طور که قول داده بودم، دارم مطمئن می‌شم که ایران هیچ‌وقت به سلاح هسته‌ای دست پیدا نکنه. خودشون هم اینو می‌دونن.
به‌زودی از اونجا خارج می‌شیم و می‌بینید که قیمت نفت مثل سنگ سقوط می‌کنه و قیمت همه‌چیز هم پایین میاد.
این عملیات بزرگی بود که رئیس‌جمهورهای قبلی باید سال‌ها پیش انجامش می‌دادن. باید انجام می‌شد، ولی هیچ‌کس حاضر نبود زیر بارش بره. ما چاره‌ای نداشتیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72927" target="_blank">📅 10:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72925">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=AanLWQAERL9Wmd-uN5X2l2jlGfk_A_xJw915acy34kACkJpwa23rpdjBl9CfJyEjR0Pwre5HU7pQhO3IGUi532TeQ4O0Wco3ieLyNYb1gP9zG6v7as0n1zrhCkc7q1As66k57q8aUEuaqUL0OoU4pldOQU6UQCPHVotlE6aV9ah9K095ecNvtbdr2_7yfIgoQe4vuwc5rg7srjbiQZ2DTkFBYEC-3szlmnOd6Thvx8_0I0EsN0fwSK-xWs2yoti8CUVkDRilwcOQSPV1eFCQxOzsCNBFgSHKEyokIoxuaEuWqVGecXJn4FYtSfpAqupgs7nVr9wv2PT7VItNKbiQ6E9BSuUG6XLul2Nrg6CiKFOZMl1uwNLPwdxUDUS3T9oljNeSjCIPvjKmfodLtZhOMqflGTMYdn7Ey25Zj8vCmJlJuLTJLiSFkW51vfjC2oWtxKydpgz6C_wG7ZIZ5wJXjKv0n1yd6oWWFSm09gOuxi6jD2BeRo2bHLB0cJkX-ND_k_kJ_OMvl7FhAgm-UN1637SYbzJ32Vk9g8aAAmAvd5usAS1ZUj_067w3JP31R_3641JS1Ndx6gBulAEHM-rBzlsa34GajGeR3LxJU9CDZKeVUe7tMfCs5N18sQ1kSfA3gkP9TMCjduKfJPxqkJBWulCGbCpMxQ5mPwG1JNfFB0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2348ec3a.mp4?token=AanLWQAERL9Wmd-uN5X2l2jlGfk_A_xJw915acy34kACkJpwa23rpdjBl9CfJyEjR0Pwre5HU7pQhO3IGUi532TeQ4O0Wco3ieLyNYb1gP9zG6v7as0n1zrhCkc7q1As66k57q8aUEuaqUL0OoU4pldOQU6UQCPHVotlE6aV9ah9K095ecNvtbdr2_7yfIgoQe4vuwc5rg7srjbiQZ2DTkFBYEC-3szlmnOd6Thvx8_0I0EsN0fwSK-xWs2yoti8CUVkDRilwcOQSPV1eFCQxOzsCNBFgSHKEyokIoxuaEuWqVGecXJn4FYtSfpAqupgs7nVr9wv2PT7VItNKbiQ6E9BSuUG6XLul2Nrg6CiKFOZMl1uwNLPwdxUDUS3T9oljNeSjCIPvjKmfodLtZhOMqflGTMYdn7Ey25Zj8vCmJlJuLTJLiSFkW51vfjC2oWtxKydpgz6C_wG7ZIZ5wJXjKv0n1yd6oWWFSm09gOuxi6jD2BeRo2bHLB0cJkX-ND_k_kJ_OMvl7FhAgm-UN1637SYbzJ32Vk9g8aAAmAvd5usAS1ZUj_067w3JP31R_3641JS1Ndx6gBulAEHM-rBzlsa34GajGeR3LxJU9CDZKeVUe7tMfCs5N18sQ1kSfA3gkP9TMCjduKfJPxqkJBWulCGbCpMxQ5mPwG1JNfFB0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از مدرسه دخترونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72925" target="_blank">📅 09:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72924">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMgvoXrtLN9T9_1oHHP3zzbwVsS8oHEu-T1aXpY4ugMBDPr2UxD-m2Geq95tHeN84mP8ZvxYdPZNGtzWkZa-UA7Ew1frvndK876aeY8XlhVF0O6qK0d-c5_S7le5f8_xle7NYbuG5DVy49T9JUdAOmEpQry5oY-0_jbPpAkz3I7JElBL4dTlQkyI-YZ8CAmcC3GQEExLSrvWJGj3P-idC3FR5NFDFklCvSDqZqC14i6fqhncDThp2cMAuts5_amVabCyJGlPASvpYkt-IRfkPe2lHNp7Nr7ynmD2SdF5yVdkXgsUHawS6VuIKCPBlFgHDtgDBNfQSuEFof0Kf5XTwe1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMgvoXrtLN9T9_1oHHP3zzbwVsS8oHEu-T1aXpY4ugMBDPr2UxD-m2Geq95tHeN84mP8ZvxYdPZNGtzWkZa-UA7Ew1frvndK876aeY8XlhVF0O6qK0d-c5_S7le5f8_xle7NYbuG5DVy49T9JUdAOmEpQry5oY-0_jbPpAkz3I7JElBL4dTlQkyI-YZ8CAmcC3GQEExLSrvWJGj3P-idC3FR5NFDFklCvSDqZqC14i6fqhncDThp2cMAuts5_amVabCyJGlPASvpYkt-IRfkPe2lHNp7Nr7ynmD2SdF5yVdkXgsUHawS6VuIKCPBlFgHDtgDBNfQSuEFof0Kf5XTwe1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو تهران، عده‌ای ساعت 9 صبح از خونه زدن بیرون، کفن پوشیدن، به سمت قوه‌قضائیه رفتن و به پسر پزشکیان لعنت فرستادن :
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72924" target="_blank">📅 09:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72923">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72923" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72922">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72922" target="_blank">📅 01:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72919">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sIOH9XK9yWa0Lwh-xk2P1EqpTWVetX5Odkzm_KEMnI97rpAOO0YpLD4SYkh6WqimrWzp2IOxEsqufOebDDHO0hfdjTP2YTiH-yEqpcBbD7smHeIGmppyKar_ykNys8Ww5veb5WHzqqdFVTNBC8dhQbMQALCTJby6g0TCZzcI6Pq7sMiz8Oz-oRyCUuN1Lt-W4Eo8jaCmKBCT3EhjsuBynjSyjqmhNpH_j3J06o2ZgRfJXhn4rAXMvR_QqyxDX7_SKuAYggKvh9raUCQ_lcGbVnc0Buhx-xlrE7FeM9QhpTyvLJJFmnpJ84U4_r5xb3zcbIYHwLEn5JOUYJS14nHn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-Ryh82qAZ6Rz6e6olpvsmrmwrc4fro8mctfb1kkW3PwUznA71rxPbZ38ny_fIY7xJ7bDoumsah2YuviobARGFB7gvfz7Q-dYsD-PbFcSkQDsPNGqQlKzJcyvyVW14juGN_5oZCmedavxw9YcLkDPmUkTlKni13iuNlLB0a1euI7RzSyVtCPh6UwOwppRH3VPl9u1fpVuMOle66l4-wZBG8Iil3tmpQNKNhqktYolAZD3JGr-T6yOX-_sZ8-zHxozQAPfENnPsqxjXQ0tdwR-ZZwAjpMwohmtn85RxoXpmaBEVEnM4oYeO9Pew8MObo4ynZB5Mhyrs2xQf6bGmJY5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=mlh1e929flykAqb5IPQ3MqiB6bDOBGXyqvOh02A7Ozqtm4748ZFqNGnrP0yXAcHatZC6rphqwUoVB_1_G-yaX-Ehyg5RyP1ZM-qFjL30CukZJSITgoWF6OWSQBmEz7I4iiNHh-1rQEZmOyw1MwHuzPq2Fy7wKhyU5VpF105EhFaKVS9NP07lEuVd8E14o4dPw1uJFjUzf4ubX-7yEjORyz1AIr1alEuryTobZ5BXshQ6w8qtUasygcQAliI34xihtHI01gA0eUZYfQY9FNic5miUaPmIGBWCDd6UdAq8-YU6-8bkj3kMc83HLnc-ZhC9O9BVTZaWuCdhges2iu7jUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea54d8bc.mp4?token=mlh1e929flykAqb5IPQ3MqiB6bDOBGXyqvOh02A7Ozqtm4748ZFqNGnrP0yXAcHatZC6rphqwUoVB_1_G-yaX-Ehyg5RyP1ZM-qFjL30CukZJSITgoWF6OWSQBmEz7I4iiNHh-1rQEZmOyw1MwHuzPq2Fy7wKhyU5VpF105EhFaKVS9NP07lEuVd8E14o4dPw1uJFjUzf4ubX-7yEjORyz1AIr1alEuryTobZ5BXshQ6w8qtUasygcQAliI34xihtHI01gA0eUZYfQY9FNic5miUaPmIGBWCDd6UdAq8-YU6-8bkj3kMc83HLnc-ZhC9O9BVTZaWuCdhges2iu7jUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۷اکتبر ۲۰۲۶؛ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس رونالد ریگان» (CVN 76) در حال ترک سن‌دیگو:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72919" target="_blank">📅 01:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72918">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=iFuiEe4Pgqp85bQXmSOU589Z3Nbq-oHGEA_2P8_bqSVc0iyj1gc6Ha19hm4mgSD07gB_wAqXBC_SZ_KbMAStLQHD0f8cN1e7Dpcut0k90EQg14rq8Z7jMKybyCth_FWeoqNgUCY5Vyhu-q7dh5J5t6mpMx4Y9jnM2B2CmanGG7a4X8IllcVUOhSwSI4Gzj_ODDVN32Njm8-L7YEf7tTyiILFJjWH8Qo_XSZTpP4_132no3HPLjgEHO8cJ8buspJV6p4rRdPJsQ2nF-GF7dRd_htzlrZxeurBNON57vRwtEzjS393P0y2WcZ5xNr-kuARrykR74jfvGFsXhUJ42MKzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b185c0bc3.mp4?token=iFuiEe4Pgqp85bQXmSOU589Z3Nbq-oHGEA_2P8_bqSVc0iyj1gc6Ha19hm4mgSD07gB_wAqXBC_SZ_KbMAStLQHD0f8cN1e7Dpcut0k90EQg14rq8Z7jMKybyCth_FWeoqNgUCY5Vyhu-q7dh5J5t6mpMx4Y9jnM2B2CmanGG7a4X8IllcVUOhSwSI4Gzj_ODDVN32Njm8-L7YEf7tTyiILFJjWH8Qo_XSZTpP4_132no3HPLjgEHO8cJ8buspJV6p4rRdPJsQ2nF-GF7dRd_htzlrZxeurBNON57vRwtEzjS393P0y2WcZ5xNr-kuARrykR74jfvGFsXhUJ42MKzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72918" target="_blank">📅 00:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72917">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMuEWWUM8leSds5C8oSawtkIqVnUZlMwXiDzZhK8ZhmnMP-FdDyazLJhS3c4vj5c8G7CP-Kf_cUGg03RdTD2IKKE8gVyWiZ5vis6Gx9T0Cdy9WgHVtdfD_aNlyTYLNDy6g1BEfZOhx_sZiacr9lv9UIoJRYxIzIe5bNNy1N4KfNRbNTEaN1h8WPOO1_kj0UzPY2wRDOhXbKXOAn0E2zclvVv48EcAI76qyn_nffs4ETKXccz0w8Rq6PiQcuoKAAvoP3L1BDyG5sAytvBpO7NAVwnCpNmVNffebToVAago_J-iUScfOM9ukJfYoo_429BAV4Y0Z9Eg2b6FRvkxXUwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: کاخ سفید از پنتاگون خواسته گزینه‌های حملات جدید آمریکا به ایران رو پیش از انتخابات میان‌دوره‌ای ۳ نوامبر آماده کنه؛ البته هنوز هیچ تصمیم نهایی‌ای گرفته نشده.
به گفته مقام‌های آمریکایی، ترامپ می‌خواد قبل از انتخابات نشون بده که در جنگ پیشرفت حاصل شده و هم‌زمان به کاهش قیمت بنزین کمک کنه.
همچنین گزینه‌های اقدامات نظامی گسترده‌تر برای بعد از انتخابات میان‌دوره‌ای هم در حال بررسیه.
@News_Hut
| The Atlantic</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72917" target="_blank">📅 00:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72916">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=gQ1W2OLJD2OlandB-ANoOdLsuTR975C63W805X6GzumOREmVjSeMNCyhIl1LgLrJMhclQBZs8Gg5_FD5uMkAo2x_rmjYDep5uxh7oXKlhRKnO_nywMq2x5qMILrn-SRZj5oZeB4Gl5CfvRJ1Va_0Oldj4vbpb91rQ_aHVwIM4BS0RwfK7zGObET8dBo0ctpZudKpru334JcmsEwJqsUrC4B7mEcwXRhHxc_gDsj71NlaKFyHLEZ05F8EBs2ieItN1lzKuUZWVKV0oyYIMeDE247p5CTEcLKWPMscAgvlDHE21oQZ9P6_QEQ1KhEI3zM5_7_A3ys8g_RZeQmYJhZnPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce779c5dfa.mp4?token=gQ1W2OLJD2OlandB-ANoOdLsuTR975C63W805X6GzumOREmVjSeMNCyhIl1LgLrJMhclQBZs8Gg5_FD5uMkAo2x_rmjYDep5uxh7oXKlhRKnO_nywMq2x5qMILrn-SRZj5oZeB4Gl5CfvRJ1Va_0Oldj4vbpb91rQ_aHVwIM4BS0RwfK7zGObET8dBo0ctpZudKpru334JcmsEwJqsUrC4B7mEcwXRhHxc_gDsj71NlaKFyHLEZ05F8EBs2ieItN1lzKuUZWVKV0oyYIMeDE247p5CTEcLKWPMscAgvlDHE21oQZ9P6_QEQ1KhEI3zM5_7_A3ys8g_RZeQmYJhZnPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست وزیر جنگ آمریکا:
«ما با نیروی دریایی ایران به یه توافق رسیدیم؛ تصمیم گرفتیم اقیانوس رو باهاشون شریک بشیم.
نیمه پایینی اقیانوس مال اوناست.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72916" target="_blank">📅 00:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72915">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=Z5jzM6hxN6zDVqeJ3kuE8zHAwoT153GdcJIAQt5YT8d0wNYtfDIHs2_8dz-IxDWfx2oCM1tI4O3zSWmJFKq0pQaWW81ptsMvl1JaAomt1XYSFY0hauvEoD9aKKrC4gdwQPlGGa_hWIgxDn2f4GAtJu6QgNN4DY8EitRDrgo2ATn7apGycLzmYm8w-Ep09XcblPxvjr0HSCfEtU_Tv12jY-AeakMLVrZ_9VCCufyLVQQHGefQzObM4d3ekmp5l7aWEMssL1upjtXZMRpD9TbAwEhZvH1XdghdKb6CbETpg-y5D28TyP7nWc9KexfsDteV4CxD0YhLDunegNGMuPWsUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4015ec5f18.mp4?token=Z5jzM6hxN6zDVqeJ3kuE8zHAwoT153GdcJIAQt5YT8d0wNYtfDIHs2_8dz-IxDWfx2oCM1tI4O3zSWmJFKq0pQaWW81ptsMvl1JaAomt1XYSFY0hauvEoD9aKKrC4gdwQPlGGa_hWIgxDn2f4GAtJu6QgNN4DY8EitRDrgo2ATn7apGycLzmYm8w-Ep09XcblPxvjr0HSCfEtU_Tv12jY-AeakMLVrZ_9VCCufyLVQQHGefQzObM4d3ekmp5l7aWEMssL1upjtXZMRpD9TbAwEhZvH1XdghdKb6CbETpg-y5D28TyP7nWc9KexfsDteV4CxD0YhLDunegNGMuPWsUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله سرحدی، مقام طالبان:
زنان بی‌عقل هستند. آن‌ها از نظر عقلی ناقص‌اند.
آن‌ها هیچ‌چیز نمی‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72915" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72914">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=OoP_vIfF2kZRxGMSAgy7I3lBTE3S4YImOnM1szGZ2MHnhnGJ7KiX1vmVDYCOcVI4WahVMear3gAN0ndQL7xcvx_llMfK0-OEf916Cp2kAqYnXneEtU0THSTYRRU6yo7ZaxvGYXzXiAqIKfy7q2Ka-5xnnTRGnEBpKzMG6TQpB28JXYTbQlU7nRHiQyF2q7sPc6xjZsf0fXqXydk5AHq8goW21szeSoFqUgXi7wWNuc-EiR96OKVWHlYF10btjLNVzSZBIvythCLMgeDfdqIupW223kHCCiiwKJNdovbhx-Ujakp_YvkuXkab3jT9tQdJEnoqrjpuBrqINo5mz8qOmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/982682c0ce.mp4?token=OoP_vIfF2kZRxGMSAgy7I3lBTE3S4YImOnM1szGZ2MHnhnGJ7KiX1vmVDYCOcVI4WahVMear3gAN0ndQL7xcvx_llMfK0-OEf916Cp2kAqYnXneEtU0THSTYRRU6yo7ZaxvGYXzXiAqIKfy7q2Ka-5xnnTRGnEBpKzMG6TQpB28JXYTbQlU7nRHiQyF2q7sPc6xjZsf0fXqXydk5AHq8goW21szeSoFqUgXi7wWNuc-EiR96OKVWHlYF10btjLNVzSZBIvythCLMgeDfdqIupW223kHCCiiwKJNdovbhx-Ujakp_YvkuXkab3jT9tQdJEnoqrjpuBrqINo5mz8qOmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگاری پرنده‌ها با این هموطن مشکل شخصی داشتن و اینطوری باهاش تسویه حساب کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72914" target="_blank">📅 23:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72913">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=QV-Xe6AdCwHU3CPhD5BqYgo636CpnfSL--MhQWv-Rhd_Jf5y9ZqvQNBP54ctmBHS9gITAQPArXprLRmPz1EeWa15aGZh4l7G3jBfW-BJMaG0BjRsMVzL4lfuA9NO_C124D8f8wPek3YPddV3D_1lQuVjYs_jzuX1gEC5tC_RvOVbgb7fZnxPfPXa1D9WK0D5Q4vTd-2-4APIL2b6Xqe4FR-SaZlujBkY0Iu-_TAqEL4FGl5fFt6u6IvCNJZO7J9mXBcyWj8xW0AavNOzLhOpf6f-qJJFY7y-LO0PR-Zs3TAhlkjWIcZ5KvJpibqXofJSvHEipUBFbw8nwfK3azM3lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f06b3f32e4.mp4?token=QV-Xe6AdCwHU3CPhD5BqYgo636CpnfSL--MhQWv-Rhd_Jf5y9ZqvQNBP54ctmBHS9gITAQPArXprLRmPz1EeWa15aGZh4l7G3jBfW-BJMaG0BjRsMVzL4lfuA9NO_C124D8f8wPek3YPddV3D_1lQuVjYs_jzuX1gEC5tC_RvOVbgb7fZnxPfPXa1D9WK0D5Q4vTd-2-4APIL2b6Xqe4FR-SaZlujBkY0Iu-_TAqEL4FGl5fFt6u6IvCNJZO7J9mXBcyWj8xW0AavNOzLhOpf6f-qJJFY7y-LO0PR-Zs3TAhlkjWIcZ5KvJpibqXofJSvHEipUBFbw8nwfK3azM3lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره 300 تجربی شده و زنگ زده به مشاوره‌اش داره گریه می‌کنه که چرا نتونسته زیر 100 بشه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72913" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=X2P1fUSZYpoUT2yS84udlOeiKMTXAzxLYBCWqtZgnzgstnyiiCFGmSWujRI6BENxIttUvxmVTx1K9FsZ4Oo0j6RyhKg2YPD0R-JgvVoJvfv_1tD0c5BFoc2zxuwwmpT2E02lwSUJ1tlp_anJdcJ84HwmJRi2Y9LrcsCyVx_Z_tNmwSAVX98F5SK1et8lJtYtWfxaDE3XJVX6TDGg9wXK663eHT8Td7QQHPedSCEY539AGjd7joaHXCvFoTxjp05J4HMdZbCO6-8ERilRWJrqdLzTvKcyLNMk1q3wMp1sTENhVylXumCmqyYaVkZANhHFW3-3uSzmEEWOOEk1xEbajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaff4cab2.mp4?token=X2P1fUSZYpoUT2yS84udlOeiKMTXAzxLYBCWqtZgnzgstnyiiCFGmSWujRI6BENxIttUvxmVTx1K9FsZ4Oo0j6RyhKg2YPD0R-JgvVoJvfv_1tD0c5BFoc2zxuwwmpT2E02lwSUJ1tlp_anJdcJ84HwmJRi2Y9LrcsCyVx_Z_tNmwSAVX98F5SK1et8lJtYtWfxaDE3XJVX6TDGg9wXK663eHT8Td7QQHPedSCEY539AGjd7joaHXCvFoTxjp05J4HMdZbCO6-8ERilRWJrqdLzTvKcyLNMk1q3wMp1sTENhVylXumCmqyYaVkZANhHFW3-3uSzmEEWOOEk1xEbajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیوپ برای استخر یک میلیارد تومان!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72912" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72911">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=J3nrrBPrF2pJ_vms6hDTVbdmHdy1JrPHtwSbvlURmT4ztm0EqIixL-unBj05MCS2mpkcMG8K-0t2jm0M-2YKOjctx_EEU9JJi8szGSwlkL9l1kKLZI-3j4HlSZ60P-ky4HlDwIo7Ld36Y3KXMN5pkmv0Vz_OBVw0FEJBNkiTwABlrdIzb8TaJiYwcfeapxIrZHSm89a35SuO2sIen6Vow36k-v8NWHyf7_fIFyBfXtumvHNNPdUlwT3dDzr9F1qDHLNaPYTdYOOvwi-gn3CQRwpmnl6OFp8Llo2_cxQU8Z0FJ7ivE92z5N9buNTceVpiWM-hreLS6jHi2xstx0YIZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=J3nrrBPrF2pJ_vms6hDTVbdmHdy1JrPHtwSbvlURmT4ztm0EqIixL-unBj05MCS2mpkcMG8K-0t2jm0M-2YKOjctx_EEU9JJi8szGSwlkL9l1kKLZI-3j4HlSZ60P-ky4HlDwIo7Ld36Y3KXMN5pkmv0Vz_OBVw0FEJBNkiTwABlrdIzb8TaJiYwcfeapxIrZHSm89a35SuO2sIen6Vow36k-v8NWHyf7_fIFyBfXtumvHNNPdUlwT3dDzr9F1qDHLNaPYTdYOOvwi-gn3CQRwpmnl6OFp8Llo2_cxQU8Z0FJ7ivE92z5N9buNTceVpiWM-hreLS6jHi2xstx0YIZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«شاید من جلوی نابودی کامل جهان رو گرفتم، چون ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت. و این اتفاق خیلی مثبتیه.
رئیس‌جمهورهای قبلی باید این کار رو زودتر انجام می‌دادن، یا اصلاً یکی باید این کار رو انجام می‌داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72911" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=nlMdLRVHg40mUKexPpQ87q4d6m9Q787qTKm89nSI7P_KsULoFhXPLGw6N_yFim0KJzXnxDOsg5dkU4GAvF8Ivvi2zuqAacXmJWSRjDMMn4W5h2wqAmHsT2CZTe0jK4vzsBIEJ0uHux216NuhDq5h4y6zSqRR8Yn-b9StYNsYJtLRS_IoS6t7vLbw8mIdPvdwavt4rv5l0Uk31QNcO0-3as_eB5yZ3szkbIfi3C_lcfOKVZfVGaMYyWPTP2KVYXGaU3ElGClDdz3tk-ltoBv-p2VPdjbQ7ztSDrd_TX3SIkCjCe9PBQHRkplxnhnxJKc_um4CvLO6dzqrwXR9_KbKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb506785.mp4?token=nlMdLRVHg40mUKexPpQ87q4d6m9Q787qTKm89nSI7P_KsULoFhXPLGw6N_yFim0KJzXnxDOsg5dkU4GAvF8Ivvi2zuqAacXmJWSRjDMMn4W5h2wqAmHsT2CZTe0jK4vzsBIEJ0uHux216NuhDq5h4y6zSqRR8Yn-b9StYNsYJtLRS_IoS6t7vLbw8mIdPvdwavt4rv5l0Uk31QNcO0-3as_eB5yZ3szkbIfi3C_lcfOKVZfVGaMYyWPTP2KVYXGaU3ElGClDdz3tk-ltoBv-p2VPdjbQ7ztSDrd_TX3SIkCjCe9PBQHRkplxnhnxJKc_um4CvLO6dzqrwXR9_KbKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: الان از روسیه همون حسی رو می‌گیرید که اوایل کرونا از چین داشتید؟
ترامپ: «چین اون موقع خیلی چیزی نمی‌گفت و روسیه هم الان خیلی چیزی نمی‌گه. ولی روس‌ها می‌گن که اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72910" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=PDdXM9qFGLABAfNaih_CIcu2h7-Gg7KUS78BB2Y699yHYkzH147L5bI8sp25hx7N-fcxWvkX-xYes7-cd-nxQEl1_ImpmHmJ-_K6QD_6l1QmLSCtz98ZUAsuiH1ejjpDzr9zI9Xn7vqazY_fhyI2dC5kFgDhmYFKFvWmnT86nFcTjb9pG5gWYfbd994F1GlFOI2ErMgKTPxPlniS77azCifsP0jAAr55hIbQnjvIIOnObqcx872gtzOSNGWkKMjUmsLAfTxicUMctnnI1NGEeiJFp3q_Q0R05Su9375FMsSISr6PmZzCdYwPYDNhyh7hsNjKpaZoVK12e0Wq89OuMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded261ded0.mp4?token=PDdXM9qFGLABAfNaih_CIcu2h7-Gg7KUS78BB2Y699yHYkzH147L5bI8sp25hx7N-fcxWvkX-xYes7-cd-nxQEl1_ImpmHmJ-_K6QD_6l1QmLSCtz98ZUAsuiH1ejjpDzr9zI9Xn7vqazY_fhyI2dC5kFgDhmYFKFvWmnT86nFcTjb9pG5gWYfbd994F1GlFOI2ErMgKTPxPlniS77azCifsP0jAAr55hIbQnjvIIOnObqcx872gtzOSNGWkKMjUmsLAfTxicUMctnnI1NGEeiJFp3q_Q0R05Su9375FMsSISr6PmZzCdYwPYDNhyh7hsNjKpaZoVK12e0Wq89OuMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
ترامپ: «فکر نمی‌کنیم این‌طور باشه. خیلی زود متوجه می‌شیم، اما فعلاً فکر نمی‌کنیم سلاح بیولوژیکی باشه.
روس‌ها هم می‌گن اوضاع کاملاً تحت کنترله.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72909" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72908">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا، در سن‌دیگو همراه با تفنگداران دریاییِ بال هوایی سوم تفنگداران دریایی در تمرینات بدنی صبحگاهی شرکت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72908" target="_blank">📅 20:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72907">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=OSge3SWKyLH5X9nhksesDkWoC0qZkfiQSXZ08CY4ozvbYWwjYNpsnPlFVopzC2B7bnnnnK8Q5rSowxY_yjtAq4mLN63iQPAZ84ABqWiAbiPGXrpEfa9NFnsyOhc_MrIvy3KqluVDJaZhKw3Mym14qVMcbQMBpr8QoXzJ-DFYauj3NcorB-xJPA6eOlck0RsJ01WhoHVKD2kPrU08UgZX3KjdgkOf1g_p7Y1uvPfJ3pD9yFKgyl5u0HqDdBmKhAGCLdIm0XlTg5N_gQFc3j1Vuf3BIJf3bzMxXkNnOviuUANNpGo5Orqq6JZ0F3V0DNXOuTFVsmONZ17SFTcN37EdfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c97edc55.mp4?token=OSge3SWKyLH5X9nhksesDkWoC0qZkfiQSXZ08CY4ozvbYWwjYNpsnPlFVopzC2B7bnnnnK8Q5rSowxY_yjtAq4mLN63iQPAZ84ABqWiAbiPGXrpEfa9NFnsyOhc_MrIvy3KqluVDJaZhKw3Mym14qVMcbQMBpr8QoXzJ-DFYauj3NcorB-xJPA6eOlck0RsJ01WhoHVKD2kPrU08UgZX3KjdgkOf1g_p7Y1uvPfJ3pD9yFKgyl5u0HqDdBmKhAGCLdIm0XlTg5N_gQFc3j1Vuf3BIJf3bzMxXkNnOviuUANNpGo5Orqq6JZ0F3V0DNXOuTFVsmONZ17SFTcN37EdfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجایی که مشاهده میکنید تگزاس نیست، کوهدشت لرستانه که یه چند نفر با همدیگه به مشکل خورده بودن و تصمیم گرفتن با کلاشینکف حلش کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72907" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72906">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB3-H31srVFAk57jzOJB3JmRpu2MNqcr8ZFQyU2AVfq11ZJIesN7TjQ8Bwi-SfVuwxJngw6ZQKVCjEHGab_nDxWfGPNea8zzD-NIju42moHOjxoCxZJBZQ5vU_z60uppCNWxNRA8hHsFd0EIk_CqBRYavG6ZLyIWDKypA8PdR5nznmBq0DQv7AbcEBU3kWqWy_4TyMtblGBFZxyuLSWKaqxc7h9GiBC0kqdDayFdEPJ1z4VLtYRjPNhad6oKp_0NTy4dpZPIy9-hk9BFX9IJ05yIH2o4f7Z2vodVcpQTGPdYJoyk4OqG7rwW6d695OOaxDrzIFADqIUNM2kxg1kFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه
!!!
طبق گفته منابع رویترز، قرار شده به هر خانواده ۳ هزار دلار پرداخت بشه.
حدود ۵۰ هزار خانواده که خونه‌هاشون تخریب شده یا از روستاهاشون امکان رفت‌وآمد وجود نداره، در اولویت قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72906" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72905">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=EsXfN9z1w4zW9m99sL8S8Yf3Wjg61mFrsgBYhp3YX92u6bhsiJRdvSuRk4rhSvywh1hyD0l8fMjMULq8bYrEdj6ibDRgQPkJDglxuRKQDxFtAYdYO7DcDh9fFbFh5SkzuwAA60whrLb1pxo9Sf_FhdVES72GlDC8k9O_YqQ6eVax-1_szcvfo-R1YB3IutrPJbgg-2I7P4tynjVulWz8LIihmGsvFhd6MyqSAJA83wNfLU14bPkWWhZBZnk68gyGJk0AjYCZPZ6qOs2MlNaulqMvEzjs0BIClNlS1wh_SCbSYsQl6PYWTebpa1jW7dxQXKwvK9XSC4nbThaEx4FsAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb95b8f0e3.mp4?token=EsXfN9z1w4zW9m99sL8S8Yf3Wjg61mFrsgBYhp3YX92u6bhsiJRdvSuRk4rhSvywh1hyD0l8fMjMULq8bYrEdj6ibDRgQPkJDglxuRKQDxFtAYdYO7DcDh9fFbFh5SkzuwAA60whrLb1pxo9Sf_FhdVES72GlDC8k9O_YqQ6eVax-1_szcvfo-R1YB3IutrPJbgg-2I7P4tynjVulWz8LIihmGsvFhd6MyqSAJA83wNfLU14bPkWWhZBZnk68gyGJk0AjYCZPZ6qOs2MlNaulqMvEzjs0BIClNlS1wh_SCbSYsQl6PYWTebpa1jW7dxQXKwvK9XSC4nbThaEx4FsAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی: علت این‌که ۲ میلیارد دلار ارز برای بازار تامین کردیم این بود که به ترامپ و وزیر خزانه‌داری‌اش بفهمانیم مشکل تامین ارز نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72905" target="_blank">📅 18:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72904">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=fJxQWxfpbLAe1mt1V_e5mvtoaCaeNNAdVBAaqoxDCWbBkFi0h449_QrB3zA82vWN5DzhyQa1SVaDqaN2eaZNtkcARK75BKZx2iybfhFtaxG-iXiBAs5Qc6buoopcDWrBwQw-kESTmmlTXr4PqspUUbCjUY_U8PmWW8cx6iH5ow--Ekb0gtC-qyOdZOFfOXhJqDyGgetKzFTJ9gXR__hk7opvh595kbEGRm4Cgw6RRlbAexSMCxdX5ilOrfoPd3CLSJGPQXpKiysYRjhJ3v9s2454KPxNkeFa6DBsiKNWpSeDAHzgH7LjfFV0vsuEsJ6N4qfwcDjQz02V959M7Y8_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a9610ab5.mp4?token=fJxQWxfpbLAe1mt1V_e5mvtoaCaeNNAdVBAaqoxDCWbBkFi0h449_QrB3zA82vWN5DzhyQa1SVaDqaN2eaZNtkcARK75BKZx2iybfhFtaxG-iXiBAs5Qc6buoopcDWrBwQw-kESTmmlTXr4PqspUUbCjUY_U8PmWW8cx6iH5ow--Ekb0gtC-qyOdZOFfOXhJqDyGgetKzFTJ9gXR__hk7opvh595kbEGRm4Cgw6RRlbAexSMCxdX5ilOrfoPd3CLSJGPQXpKiysYRjhJ3v9s2454KPxNkeFa6DBsiKNWpSeDAHzgH7LjfFV0vsuEsJ6N4qfwcDjQz02V959M7Y8_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
مجری: «شما در سازمان ملل گفتید: «یک روز، که شاید این روز چندان هم دور نباشه، مردم ایران آزاد خواهند شد.» منظورتون از این حرف چی بود؟
نتانیاهو: «مردم ایران خودشون می‌دونن چه زمانی و در چه شرایطی باید کاری انجام بدن. وقتی زمان و شرایط مناسب فرا برسه، اون‌ها به پا خواهند خاست و این حکومت سقوط خواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72904" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72903" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a41Oci9k0WsI_zTUXA6TBCvpIZWerI23Te6vnIQK4sMEfjC9je59B2beJMWeU0chXHKFj1CJzqg4A_hnbBSdMkepqlc1-7scGIyg3UdeSBS-m_e2kkWvmem_R92ZYwRAihQfgn8xURMHu4Fxrw8zJoPrIILyEZG1BPQU5X9jRVLZ5YPoK-0p-FB9pbvX4T1mOETXkUIwG8EkTriwRCE0eBKUuKFQO5adW2YwcFjgrHwv38C2atuL-waWyawVaPqg1vnxLS7Vv9fuMIe6OarKp2gMeSh5x7z17VG3VNegQUVPDWf8QBi2xWnxwLaegH37MXPV9H4NEXB5YVj8y4syrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72902" target="_blank">📅 18:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=LqExaS-wH6IsLK4DKAbEgcVR1kSIX7A1Hhk1B1inLozA1PCu1ShakY8_Rn55Jdwk6bOiE11L2eMBfzbtakk-bdL9ZIEZnjoX9UmD1JbDDthU6fD7ZVNBW8lByi375cCMJGI1jsnv4koTkzmhQxtkxhcLxkK2BpXV9M6PPTBFp9J8bX5BrCHqM4fIkTkgKrme9Il-QE2XmTPKAR8sY-Jom0J9qFtbURHlNJlCiZSrujf7pQBgYWKAwCDg82J7yM8tVmsx7DgL-iecz1RMGYyXiuIsOw6NWdW0k-PfhpZckPTOzzTouDHkkIs4y9wcMr5ZaD1x09f66dYHm94iBJ65FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0613e028.mp4?token=LqExaS-wH6IsLK4DKAbEgcVR1kSIX7A1Hhk1B1inLozA1PCu1ShakY8_Rn55Jdwk6bOiE11L2eMBfzbtakk-bdL9ZIEZnjoX9UmD1JbDDthU6fD7ZVNBW8lByi375cCMJGI1jsnv4koTkzmhQxtkxhcLxkK2BpXV9M6PPTBFp9J8bX5BrCHqM4fIkTkgKrme9Il-QE2XmTPKAR8sY-Jom0J9qFtbURHlNJlCiZSrujf7pQBgYWKAwCDg82J7yM8tVmsx7DgL-iecz1RMGYyXiuIsOw6NWdW0k-PfhpZckPTOzzTouDHkkIs4y9wcMr5ZaD1x09f66dYHm94iBJ65FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تریلر Gta نیست، ایران خودمونه!
چند روز پیش توی بازار آهن تهران، یه نفر با ماشین میزنه به یه موتوری و فراری میشه، پلیس هم میفته دنبالش.
چند تا تیر میزنن به چرخاش و در نهایت گیر میفته و حسابی کتک میزننش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72901" target="_blank">📅 17:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72900">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=RaRiCvS5MtDdcJbMQ9rbw0mKz-bLvyHPTdY6JgYZatKN6zLH6MG-brPxIurNR5ugLv79E44JmqnfE_EkcUoR3BTW7ZtZPYW0v3jcLOGpxxf2BloczEt8htRWDZCwmrUVQP0YkzVzx1Y_qxLVz9Ye74RiQJorFWXIV9W8Om7Sdj0wX8n7o29mk1_g76pbH2Br6x8pip7ftqgCaDV0SmrEjQkdxqeueeFkLvov3UDAlH2dGB_9Y2q7iE3bRvoaR2rolR88hYjlHIqtIWhYrTUBSg3hIQMB9a4gNrF5fQIMr3EUgQ_es6V0CNI7NgwD7Yi9amm_jDF0f50TCtjF_C0OKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aced9e8ba.mp4?token=RaRiCvS5MtDdcJbMQ9rbw0mKz-bLvyHPTdY6JgYZatKN6zLH6MG-brPxIurNR5ugLv79E44JmqnfE_EkcUoR3BTW7ZtZPYW0v3jcLOGpxxf2BloczEt8htRWDZCwmrUVQP0YkzVzx1Y_qxLVz9Ye74RiQJorFWXIV9W8Om7Sdj0wX8n7o29mk1_g76pbH2Br6x8pip7ftqgCaDV0SmrEjQkdxqeueeFkLvov3UDAlH2dGB_9Y2q7iE3bRvoaR2rolR88hYjlHIqtIWhYrTUBSg3hIQMB9a4gNrF5fQIMr3EUgQ_es6V0CNI7NgwD7Yi9amm_jDF0f50TCtjF_C0OKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم در جستجوی کار:
بعد دیدن یه آگهی منشی مطب با حقوق ۱۵ میلیون تومن رفتم مطب اقای دکتر
خیلی همه چی هم شیک و با کلاس بود؛
وقتی گفتم برای کار اومدم اقای دکتر(آلت متحرک) بهم گفت اون ۱۵ میلیون حقوقی که نوشتیم فقط ۶ تومنش برای کار تو مطبه و اگه ۹ تومن بقیشو میخوای باید به خودم خدمات جنسی بدی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72900" target="_blank">📅 17:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72899">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=d0gnQSe7x8fnDNfemLnG6NW71ByvLT8eScKnWQ6K-5cY_KaGnflnZruPxiP4x0Z84SNC2SghUgFqXfDQhHLbC-s5VSi_zwKFU3wNdJBKEF4HG3rVYOYhHeaTQKskr2EPQyPWINO2soM26MIaeXzoTpSe15ImgjWu1V0z4elaaxaTsN55iukTXjBdmgONH5a5TdY7CtZKlGFDRrbxUFkeHAW8C0PHjmUbi8PTVm6lySS4jidIK6hW3Csf9CYxKjHynhCXOfUgVxG4rC9QlO6CD-vPKgwrrAS2ce3HBJ6NoeDF-0hD5XyLRIBptHiZ7PpLg-QjNvsGZ7HdYJF0LFPv9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cb601ba6.mp4?token=d0gnQSe7x8fnDNfemLnG6NW71ByvLT8eScKnWQ6K-5cY_KaGnflnZruPxiP4x0Z84SNC2SghUgFqXfDQhHLbC-s5VSi_zwKFU3wNdJBKEF4HG3rVYOYhHeaTQKskr2EPQyPWINO2soM26MIaeXzoTpSe15ImgjWu1V0z4elaaxaTsN55iukTXjBdmgONH5a5TdY7CtZKlGFDRrbxUFkeHAW8C0PHjmUbi8PTVm6lySS4jidIK6hW3Csf9CYxKjHynhCXOfUgVxG4rC9QlO6CD-vPKgwrrAS2ce3HBJ6NoeDF-0hD5XyLRIBptHiZ7PpLg-QjNvsGZ7HdYJF0LFPv9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی از اینستاگرام پکیج پولدار شدن خریدی و خیال میکنی دیگه کار تمومه...:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72899" target="_blank">📅 16:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72898">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=Aa_q-ypINEYOL0b2AD7B2gYuEmdgD2GFNCFrGPgMWXGt_zJh7itZg4Og0c6yqb4qnhZHDtQHDOtC87xKM3VvlhBD9rG0T7sUTY3eSr9HAWhvfy0dCKXnjAHW6cCM9dLifHLyziFj1npBEvfQrf1TfDmjSbv9UGyoJqrVhWjbs4D7YQ-0OlebmYnUhXWVI_1xknzHRoUBqyQHVVhxu6od6YmkNcUuCIOM6ha8opzHw90O7voJJDbtIpsCZvA9q-4vxMRoC_aOfQG6KzjvwEzcJUHd2wkmy08c9_lWkkHDKgqm3Jj_gNOs1xxOdQV7t69QEVtIjm9QvjmPEDqmeh59rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7100f309a7.mp4?token=Aa_q-ypINEYOL0b2AD7B2gYuEmdgD2GFNCFrGPgMWXGt_zJh7itZg4Og0c6yqb4qnhZHDtQHDOtC87xKM3VvlhBD9rG0T7sUTY3eSr9HAWhvfy0dCKXnjAHW6cCM9dLifHLyziFj1npBEvfQrf1TfDmjSbv9UGyoJqrVhWjbs4D7YQ-0OlebmYnUhXWVI_1xknzHRoUBqyQHVVhxu6od6YmkNcUuCIOM6ha8opzHw90O7voJJDbtIpsCZvA9q-4vxMRoC_aOfQG6KzjvwEzcJUHd2wkmy08c9_lWkkHDKgqm3Jj_gNOs1xxOdQV7t69QEVtIjm9QvjmPEDqmeh59rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از سورپرایز تولد علیرضا توسط مامانش. دخترا اگه نصف عشوه علیرضا رو داشتن سر خونه بخت بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72898" target="_blank">📅 16:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72893">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTeccP18c8dO4aK2N-Nmce14akf0VfIV_kTHYxjczlVtCAlItvlcTwK4FWt21QAyDcKe45Zz38AbrVwbt6p8EbhUYPaP75uQ_Of_asdiROAcFCm6YHnUTYN086Rr9di9rBJ7W-4tdVd7l4wZC4_rydsm0FedQ63CBcd2GZo2-56u9fBbeEDq8_imdZSQs_0H2FhRHBG_yV0ZybvSD1VP3RuvQIFiS-mFfTG0FRtuP8VTLj4PbpBixO6TBTu05P2XdKfdSbyUwYxAui7kDwXxK5pN2o1pWGhqnJHNMU0Be5edq3oAZZ-AcRlu1Gzr9y68zeKQ_brdZz5wC7ZrEFW58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1zGf9Xt7xS8ZBqWYPNE1Zn_e2ZuztDcwgodAwsZU9uxx2zxPjzELSiWL29pAAy_muN8RQqZkm-NOUGa-jhwP1whb1VtFdkQB7RejhIzOc7uJNTTfTiVirzm13ieVHdYNs9ed3djRUxad4Ods21dcckXAkY7eNd4gauclTFHZeys8z_gNE7q4_ki2IPppnhYilpKy1QV4VQoNAWT8FO0xwZ2BnC4SspE9VTKDWd7Qm2YaX3Zxul5K4cS6aJKxHoWmnuuR0q1YQgNdLjuHm81y2YUrhqkQiK9VDp1DlSljfyowggUIvWLkM-3NGGUhL-8-MP-WNBwvw0eueeULNv9vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=js-chXTa0eBAntZmvGdwCcUxC7lzGe2yCCEI-cCkF9wZH48P6Q4BT8eKqEm3WT29dtVQPrI2wpODEufnWR_iuOk3TkyfnOFSio8PCbHNSZkdO4JrIeAEmvfafgMgj2xJkPcuJakOo8zRsev5ENUD8kRneAnJCOgslNLmlUpiSGw4tVh9S5N1U-3vDKX-Qqo_q4h10w7M3t12zWh_z7umojbfclwaFrYjN-3XKcfIIXq6tg8w9OGEFzunJmB4RUy8YzTpeDnvHm6KshueJw6_apqCz0uq6ahhzJA7zdSotzcuXysRcQXgOYuGC5jECHHkuwDAl8ojCB0yZdKHezMCgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d935bdc93d.mp4?token=js-chXTa0eBAntZmvGdwCcUxC7lzGe2yCCEI-cCkF9wZH48P6Q4BT8eKqEm3WT29dtVQPrI2wpODEufnWR_iuOk3TkyfnOFSio8PCbHNSZkdO4JrIeAEmvfafgMgj2xJkPcuJakOo8zRsev5ENUD8kRneAnJCOgslNLmlUpiSGw4tVh9S5N1U-3vDKX-Qqo_q4h10w7M3t12zWh_z7umojbfclwaFrYjN-3XKcfIIXq6tg8w9OGEFzunJmB4RUy8YzTpeDnvHm6KshueJw6_apqCz0uq6ahhzJA7zdSotzcuXysRcQXgOYuGC5jECHHkuwDAl8ojCB0yZdKHezMCgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۷ اکتبر، سومین سالگرد «طوفان‌الاقصی»؛ حمله‌ای غافلگیرکننده که سال ۲۰۲۳ توسط حماس و گروه‌های مسلح فلسطینی انجام شد و حدود ۱۲۰۰ نفر در اسرائیل کشته و ۲۵۱ نفر هم به گروگان گرفته شدند.
بعدش اما ورق برگشت؛ جنگی شروع شد که نتیجه‌اش ویرانی بخش بزرگی از غزه و کشته‌شدن ده‌ها هزار فلسطینی بود. اسرائیل هم از همون اول گفت قرار نیست ماجرا رو همین‌جا تموم کنه و دنبال کسانی می‌ره که در حمله ۷ اکتبر نقش داشتن.
و این وسط، فهرست ترورهای اسرائیل هم کم‌کم بلندتر شد؛ از فرماندهان حماس و حزب‌الله گرفته تا چهره‌های ارشد نظامی و امنیتی جمهوری اسلامی؛ یعنی جنگی که قرار بود با «یک حمله» شروع و تمام شود، سه سال بعد هنوز کلی حساب باز و بسته‌نشده پشت سر خودش گذاشته.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72893" target="_blank">📅 15:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72892">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-wKT159MQ_6-sQyu_CFDkkqkgvmgutrYuI58IeYWAt7cnsXyQlzPTM0K1U9VSzJBhoR_CvTfa8iLjCFzn-WVBhEp1EjNdRPsV0EYkmU8X7WdEZeLc8H0Wv6dofC_625P4eBH-U6wdcd-EhxCTEk8NZWPuT0HAdFORhbPGYIFu01ZraU1mPeaHzDQFB0Y9S3ZBrHyirVuvIQwhBJCsjNhnrd7nwFnrm5GmSXOhUFYfuvGvyS6A8hwJ0QFvGsfsZFHnKDIUDi9QxpOPQYV0PcwUaLTLYlWiBcfVC1qZiliMbolPs31cl2v59W00XNZCz8jWNhah_jZRoJCgPj2mKXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه‌های برتری که مدرسه فرهنگ (وابسته به حدادعادل) تو کنکور امسال داده :
زرین، پسرِ بادیگاردِ علی خامنه‌ای : 16 انسانی
محمدباقر، پسرِ مجتبی خامنه‌ای : 106 انسانی
محمد‌امین، پسرِ بذرپاش (وزیر راه سابق) : 173 انسانی
محمد، نوه حداد عادل : 910 انسانی
محمد، نوه محسن رضایی : 1700 انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72892" target="_blank">📅 14:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72891">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=onXs4AyI2TdM_a6c3YY7FohYWih9XB97mvlRkH8pYJLVR2Aj6XfVIya95eWjFm9N1tQPgSNcLgwK-nGwFNMIn15Td5lwgVWbWJ9abEbUIcVOd1fXK91bL0Ga_Q2OWCW8k4123seFqKvzy8Mvd5g6FWz2BOeL2bC5qDT3n4J79p4gRBcy0aTr6kz06O1YeDrlbHBQ6VnDN_tGog_nkx223OSlp6UZUoxv1ByVSkNlsP16ZHTl--kLYf0nTiGlCBkZzWtSV-Xk37HTziwKt32Il48NujElU3FHGuQ5EuvhR1_Dl9Ga4LGexJe3Wm1yQf1-thge2f0QACNNBty8CnrRbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1e3a6f34.mp4?token=onXs4AyI2TdM_a6c3YY7FohYWih9XB97mvlRkH8pYJLVR2Aj6XfVIya95eWjFm9N1tQPgSNcLgwK-nGwFNMIn15Td5lwgVWbWJ9abEbUIcVOd1fXK91bL0Ga_Q2OWCW8k4123seFqKvzy8Mvd5g6FWz2BOeL2bC5qDT3n4J79p4gRBcy0aTr6kz06O1YeDrlbHBQ6VnDN_tGog_nkx223OSlp6UZUoxv1ByVSkNlsP16ZHTl--kLYf0nTiGlCBkZzWtSV-Xk37HTziwKt32Il48NujElU3FHGuQ5EuvhR1_Dl9Ga4LGexJe3Wm1yQf1-thge2f0QACNNBty8CnrRbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوچک زاده نماینده مجلس:
به یوسف پزشکیان بگید یه بچه دبستانی از پدر تو بیشتر میفهمه!
حرفایی که تو میزنی باید امریکا بزنه نه پسر رئیس جمهور ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72891" target="_blank">📅 14:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72890">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=ZP24tNOTLfuQKWsq_4oFzqDL2ZXVPjBrWAkLqITT65fdbqfUDaZIbGEZdk6tSPd5r36JEaY16OhKJ9WDDbJks2tny4UovIYhRa9uUG2a1Mp23d1_Uirpn3TqwSWVpqMDe36AzUmxD2fxncNQdUsNXPu3muVQb6wccsPJcXKfplTg1PGRDj4eEVjyPFWCwb0_b5Awdp9yoWySv0TlZBYXggHeikOjSbgvemo7sne-xtUMC-ZEqoNROVQGSsJQ5ELv0Oro8kc4ox0Xl_AFxXc4Gk-R-AxU0EB1Gf7TjuOupA3TlAildHBFYzvTPcEMQCgKuuxmvz4Z47-jg3ZGcGW2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab42cc577.mp4?token=ZP24tNOTLfuQKWsq_4oFzqDL2ZXVPjBrWAkLqITT65fdbqfUDaZIbGEZdk6tSPd5r36JEaY16OhKJ9WDDbJks2tny4UovIYhRa9uUG2a1Mp23d1_Uirpn3TqwSWVpqMDe36AzUmxD2fxncNQdUsNXPu3muVQb6wccsPJcXKfplTg1PGRDj4eEVjyPFWCwb0_b5Awdp9yoWySv0TlZBYXggHeikOjSbgvemo7sne-xtUMC-ZEqoNROVQGSsJQ5ELv0Oro8kc4ox0Xl_AFxXc4Gk-R-AxU0EB1Gf7TjuOupA3TlAildHBFYzvTPcEMQCgKuuxmvz4Z47-jg3ZGcGW2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر نتانیاهو درباره ایران:
«کشورهایی که حتی به ما حمله می‌کنن، یواشکی و در خفا می‌گن: اینا باید سقوط کنن؛ دارن همه‌مون رو خفه می‌کنن.
ما مطمئن می‌شیم که سقوط کنن. سقوط می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72890" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72889">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=IROhrEHSZIAW7zvcRtH7s-0aM8hQcfP7uNvpumXqtV_Am64m0KV80SnWcDJNPvRl6yiYhtNvmfkIxRIaUz45zopbQUwSgjfnpb449bOLphoIc7y_f6Lr8AefAGIZP6mz2wE63YzExnEp1PXcxTXqFWZqDTglWm9jT48E11SZWsmfJ_WfB4NOXUJcyMn8ClPsa11kY9yyKbuuZBCi0XXlcRRAAI6X96HmjQS-yHhsjYbz_Of_yPOM5aEowHNJYmaLCNaBeBSzySuLj8f6zy_rGL7wN4wDa88x0SoGHYOPA6O6RIcPr-anOnzDOG1nN8OlPqqtPwFE1OnVLbq2JlmRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec68a44315.mp4?token=IROhrEHSZIAW7zvcRtH7s-0aM8hQcfP7uNvpumXqtV_Am64m0KV80SnWcDJNPvRl6yiYhtNvmfkIxRIaUz45zopbQUwSgjfnpb449bOLphoIc7y_f6Lr8AefAGIZP6mz2wE63YzExnEp1PXcxTXqFWZqDTglWm9jT48E11SZWsmfJ_WfB4NOXUJcyMn8ClPsa11kY9yyKbuuZBCi0XXlcRRAAI6X96HmjQS-yHhsjYbz_Of_yPOM5aEowHNJYmaLCNaBeBSzySuLj8f6zy_rGL7wN4wDa88x0SoGHYOPA6O6RIcPr-anOnzDOG1nN8OlPqqtPwFE1OnVLbq2JlmRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«هر دلار و هر سنتی که این حکومت به دست میاره، خرج جاده و پل یا بهتر کردن زندگی مردم ایران نمی‌کنه.
این پول رو خرج حزب‌الله و حماس و شبه‌نظامی‌هایی می‌کنن که از داخل عراق موشک شلیک می‌کنن، و همین‌طور حوثی‌ها.
باید پولشون رو برای مردم خودشون خرج می‌کردن، اما به‌جاش پول رو صرف تروریسم و تسلیحات می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72889" target="_blank">📅 13:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72888">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=CuOa9r8ylXaqZYsGDsgTcmyFitGDmpZn5TdvUFJN59VLpZZLH2q3ozu_gpjQZiaNAe0LrLLVwg5uVPPiaPTMpsFORNshAbbl4YNU7pR5Xs7OCLKUR__bYnzsX_mpPuU2jItPlmp9nXcMOfOPJcRaHTcIbzONvv6kOEbO48JFg3gJ7i5QZOcDpo8b2VTJ8uJOo-cx3UWmQRetLi26FCkxUhn-zMUE8RfCEe4I6IrxwXipvwwmiua8WD5IuafiTV5ZVteM8B9lrLHmi5tEgRTy_xrckTrB5w_VwagEszGTmf3U2dZclJMwRrEBQ25zbynLBuhqAQc6lzBkdzLJyZmspqq3lRg_A584L0sBI6n-kQ32q2ray9jO5saIl5NUUH33BenTH_2PoIlY10lwIAaxkN603foIuBZ9fH0BtlkiAjgM5xSAVWcpDqo14s3MPkJMeRK6QuWN2-ezl0bkUqw6H-WRQIvZLrjFmwhEct_yAWyJ_O-8sSahsxg3wrbXNa-nuzX5qwI3fU5yeFnoVol7TvoneVElGIAduMFt0jtfiAFPI1hWVSfKLLtvol75wblLmiC29mO__1wIUleRlUirOJsT-PcAk8kwUjXa0EJjug9V4z5Im1Gk5Xyafblm-l0PQUmHydHoq8mVQbuN8vmKFuFgo9ndgSKVgVAnlg03_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aba6a5b62.mp4?token=CuOa9r8ylXaqZYsGDsgTcmyFitGDmpZn5TdvUFJN59VLpZZLH2q3ozu_gpjQZiaNAe0LrLLVwg5uVPPiaPTMpsFORNshAbbl4YNU7pR5Xs7OCLKUR__bYnzsX_mpPuU2jItPlmp9nXcMOfOPJcRaHTcIbzONvv6kOEbO48JFg3gJ7i5QZOcDpo8b2VTJ8uJOo-cx3UWmQRetLi26FCkxUhn-zMUE8RfCEe4I6IrxwXipvwwmiua8WD5IuafiTV5ZVteM8B9lrLHmi5tEgRTy_xrckTrB5w_VwagEszGTmf3U2dZclJMwRrEBQ25zbynLBuhqAQc6lzBkdzLJyZmspqq3lRg_A584L0sBI6n-kQ32q2ray9jO5saIl5NUUH33BenTH_2PoIlY10lwIAaxkN603foIuBZ9fH0BtlkiAjgM5xSAVWcpDqo14s3MPkJMeRK6QuWN2-ezl0bkUqw6H-WRQIvZLrjFmwhEct_yAWyJ_O-8sSahsxg3wrbXNa-nuzX5qwI3fU5yeFnoVol7TvoneVElGIAduMFt0jtfiAFPI1hWVSfKLLtvol75wblLmiC29mO__1wIUleRlUirOJsT-PcAk8kwUjXa0EJjug9V4z5Im1Gk5Xyafblm-l0PQUmHydHoq8mVQbuN8vmKFuFgo9ndgSKVgVAnlg03_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
«اقتصاد ایران داره به نقطه‌ای می‌رسه که از نظر شدت وخامت، فقط تعداد کمی از کشورهای دنیا چنین وضعیتی رو تجربه کردن.
و تمام این وضعیت تقصیر روحانیون شیعه افراطی‌ایه که توی اون کشور تصمیم‌گیری می‌کنن.
همین‌ها هستن که مردم بیچاره ایران رو به این شرایطی که الان توش قرار دارن، رسوندن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72888" target="_blank">📅 12:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ3UPSl0BIYozINJpDq4OOIz9UrzdHf5ADrxfFR5za3wkNcrdE_Uhh9XTJF96Aeb8lcRLfeCKZNaSD8Wtq7JDN7dki-bitWBpANeg0r00ZCuW7sEHMT2J2dixL-Rs1DzPr_uarX3DJhpAAqJp3CcwBMPkoyY8GOJXruepqhhMG0Kz7n6sJzya5nKlo4NoZNRLVfpRNIer7AZccIABi8e-3rBy4bM4t58lYRQzA8ccdx2tjd6kasdRJcu2njXIntpPPM33lNTq8rPUjDHRUgIUH5CDf2k-dlf_AE1XJfBA498cy6871nX7qBdW7sBkwH8loHiwZ87nSDdmC0lMuAMPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، به رویترز گفته آمریکا هنوز دقیقاً نمی‌دونه بعد از کشته‌شدن علی خامنه‌ای، چه کسی در نهایت تصمیم‌های اصلی ایران رو می‌گیره.
ونس گفته آمریکا در حال مذاکره با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه است، اما مشخص نیست این دو نفر در ساختار فعلی قدرت ایران چقدر اختیار و قدرت تصمیم‌گیری دارند.
او گفته یکی از چیزهایی که آمریکا متوجه شده اینه که «کاملاً مشخص نیست ایران چطور تصمیم‌گیری می‌کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72887" target="_blank">📅 12:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvhBI2TACXrNUHCH8VER95XOhooFyUcmyPEI39C0h7obndu4L61jqa9_P3Wn1qEkmkXNqcvuXURQMhyRkyICILhgkeNtuFi2IF-kCkRuPV4pB49bI-mIQmsmLQVO-1-5zpaISVCKuOvc5T7GF8pG3I-VWjuXuw5FWNUTe49ZxlXm4WXHfItESndirx9xdl78QQoaJLBlQYKN4DdLUsUK7rEOqvTUWUteQLlLXFtUORGFR0FbvuJZVv1mjw0Pl9zgMcyNG2vSRXbJW8hpBSVoP2bzklAjdUcUQV--H-cmUmBitg_2r9pRfNgI4J8pmZfRBZbLvtL9aAk7LigM26Gl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله ونس، معاون ترامپ، به رویترز گفته اگه ایران بخواد به توافق برسه و جنگ ۷ ماهه با آمریکا تموم بشه، باید ظرفیت غنی‌سازی اورانیومش رو به‌طور قابل‌توجهی کاهش بده.
ونس گفته آمریکا دیگه به وعده و قول برای محدودیت‌های آینده اکتفا نمی‌کنه و باید اقدام واقعی و قابل لمس از طرف ایران ببینه.
اون همچنین پرسیده: اگه ایران واقعاً دنبال ساخت سلاح هسته‌ای نیست، پس چرا باید اورانیوم ۶۰ درصد غنی‌شده داشته باشه؟
با این حال، ونس گفته آمریکا همچنان برای توافق آمادگی داره، اما امتیاز هسته‌ای واقعی از ایران می‌خواد و تأکید کرده: «قرار نیست حرف رو با عمل عوض کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72886" target="_blank">📅 11:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=lNNeV3aRXdf6z8pyAAhVwIh1NHN3GwntlpnF295f2zgMwrKaQ0Vi-1EzjfckPGJYzBD5BEhMUJYQdv4Y-uqA0B7x4XsK3RSQcRiIaX6Fn-6Mp38fZGAcuAxHYA93kYXPRmW_n8WKrQRmhCJzdTEYVt8T2ZLEhIYROx6Ool3OkYizHBcdilJ4OBvNai-Qc6zGNsX0fJ89K8JNyiamt7TJDJoRgvv1Y1PL5LHo_SEtQmTproM2VC6bhl-KLGP1BNImWlitIHfO0UZexy68c_TKuLqTKSWU6dSXDjzvf99nlBaMBjtJQ_tDWhU14y-xgWqOorkMW_GBnlbU-dzUsr39jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bff0381d0.mp4?token=lNNeV3aRXdf6z8pyAAhVwIh1NHN3GwntlpnF295f2zgMwrKaQ0Vi-1EzjfckPGJYzBD5BEhMUJYQdv4Y-uqA0B7x4XsK3RSQcRiIaX6Fn-6Mp38fZGAcuAxHYA93kYXPRmW_n8WKrQRmhCJzdTEYVt8T2ZLEhIYROx6Ool3OkYizHBcdilJ4OBvNai-Qc6zGNsX0fJ89K8JNyiamt7TJDJoRgvv1Y1PL5LHo_SEtQmTproM2VC6bhl-KLGP1BNImWlitIHfO0UZexy68c_TKuLqTKSWU6dSXDjzvf99nlBaMBjtJQ_tDWhU14y-xgWqOorkMW_GBnlbU-dzUsr39jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند نبویان: نماز و روزه و گناه و... مهم نیست همه کار باید کرد تا نظام حفظ بشه!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72885" target="_blank">📅 11:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94194705f4.mp4?token=oWjGiXAaP6_fbiJh8fT6sy44EQF6s1JdSZ3xPspHmcQswoZZsA-IKMN2I64Nm0Op93w_Zf_WMeYFwsb77JJTuBKJQZSvpJac1urOJPskJ8KWK_OUdek4QuPiDyIA-tD2Q6S3PprRRINYCzQHr7-QDcb9dDFDyIQEsEf8voS6ch_wvoQRZ1ihB-LjZc-2wwrrT1pe5d2q5P_d6Swlqie7fQqStI-eeDs-nCU_0rRFtMRF1-vYdpX9w0uFnWMBH5eSAwVGq-d1j0ejLbFhh8Q66oL9q4vSoxmhWtCytY8Uzx7yfRIFqJc0eAGLThouF2VcS6sZZMKn0_SINfXPtV5wmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94194705f4.mp4?token=oWjGiXAaP6_fbiJh8fT6sy44EQF6s1JdSZ3xPspHmcQswoZZsA-IKMN2I64Nm0Op93w_Zf_WMeYFwsb77JJTuBKJQZSvpJac1urOJPskJ8KWK_OUdek4QuPiDyIA-tD2Q6S3PprRRINYCzQHr7-QDcb9dDFDyIQEsEf8voS6ch_wvoQRZ1ihB-LjZc-2wwrrT1pe5d2q5P_d6Swlqie7fQqStI-eeDs-nCU_0rRFtMRF1-vYdpX9w0uFnWMBH5eSAwVGq-d1j0ejLbFhh8Q66oL9q4vSoxmhWtCytY8Uzx7yfRIFqJc0eAGLThouF2VcS6sZZMKn0_SINfXPtV5wmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم زیبای و ویژه برای وداع با مسی با نمایش پهبادی در آسمان!
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72884" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72883" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCzEkWXIgHJDhLtqf5pBJZti0TPjTBF9oiseh2vwDG1WeiVttjIiajiZrjlw88nqTIJD4oNWfwSbYHRqesoKemdxEkaGEo9YmpFb_OUBk6TdbET6btln9t4t07o7Yufbmp88zC9_W-6Nlx7XKk5L3Z5RchlSp75gB3devM7Ba5Ub9aufr15aX8Y9B7v3VW2uBOmORGD8t5ulexeu5VmF0pQkwivgQpQTu98vmSL01IN6IipSFYEQLNvY8lRdWgOXfkRbTUk--5q_IjTGWgqWCYqedjSrUN1x1f_NdAMDpUvfO89XO37GuXFYXdPW6ly7Pdq5U2Dwh-dAmNy9NGGsRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72882" target="_blank">📅 11:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72878">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=E43j-3cBUGkp3PI1DeKfgtq3gDBoXN4BXKC_RHoU2KAnc9Amja9sMG3NgohZajYOgtASoYqGLm82L4FYUl7Iue9Gq0DbrQA3N2r_CXHX43WI_xfuweOMTFTgUt5ilAC-zAyi8laJXt5Y96latOE8TBec9NjM3BJJRMcEDaVdG3NeLpONazTTzgeW4hYzdQ_c67ys8BnqIeIUgJmSsXQyqZrYU9zPkL9tSgv1X4tNN65r3-CccUTddnHGcjn16G-EKLtUeyR5VgUh8EW-mKnLmA3uCHnrbVPHerioAHHXPCB9HePI7a9DaY3fPnI2OzfWdrCfFnvDc8gbTkSMcMn7Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39cf67708.mp4?token=E43j-3cBUGkp3PI1DeKfgtq3gDBoXN4BXKC_RHoU2KAnc9Amja9sMG3NgohZajYOgtASoYqGLm82L4FYUl7Iue9Gq0DbrQA3N2r_CXHX43WI_xfuweOMTFTgUt5ilAC-zAyi8laJXt5Y96latOE8TBec9NjM3BJJRMcEDaVdG3NeLpONazTTzgeW4hYzdQ_c67ys8BnqIeIUgJmSsXQyqZrYU9zPkL9tSgv1X4tNN65r3-CccUTddnHGcjn16G-EKLtUeyR5VgUh8EW-mKnLmA3uCHnrbVPHerioAHHXPCB9HePI7a9DaY3fPnI2OzfWdrCfFnvDc8gbTkSMcMn7Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسیدیم به اون لحظه‌ای که عاشقان فوتبال تحمل دیدنشو ندارن...
لیونل مسی، اسطوره ۳۹ ساله فوتبال، سه‌شنبه ۶ اکتبر ۲۰۲۶ برای آخرین بار پیراهن آرژانتین رو پوشید؛ این بار در ورزشگاه مومنتال بوئنوس‌آیرس و مقابل بنین.
مسی بعد از سال‌ها افتخار، جام‌ها، اشک‌ها و لحظه‌هایی که برای آرژانتین ساخت، جلوی چشم هوادارانی که برای خداحافظی باهاش ورزشگاه رو پر کرده بودن، رسماً از تیم ملی خداحافظی کرد.
از این به بعد دیگه مسی رو با پیراهن آرژانتین نمی‌بینیم؛ پرونده یکی از باشکوه‌ترین دوران‌های ملی تاریخ فوتبال هم اینجا بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72878" target="_blank">📅 10:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72875">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=u-hePc20WZoE5D2qesM7gDBnAev-SLflUFJ2egQt-c9j22CJWgZAFJYtG6ZkC6bfXuJ9tLj7DIM0yclzdX3oT4hOUwEW3Ur0v7aAOZb7PDUrmU1xJ_TjQUopSLvpZK5cUv-Q8h2ybqZ3z2RIMUbS_t7o6zzZlN1af1EsUMhhg4XE88nzyE2czvHOdg6OkdjV7HIXMUQytrJhkH2qdDec5jAPH_lTY14hAfFxOXOQN38e0LPB7THrEtczsPcy1NmBC1tNQlPQ8fVmHqaKkBsKwk5YSaL7GjR9M72DT_m235AQ5QijTxSx0XupE6y-fWgk-X0_0TS7XJoTbsonQLiBGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca1a543a9.mp4?token=u-hePc20WZoE5D2qesM7gDBnAev-SLflUFJ2egQt-c9j22CJWgZAFJYtG6ZkC6bfXuJ9tLj7DIM0yclzdX3oT4hOUwEW3Ur0v7aAOZb7PDUrmU1xJ_TjQUopSLvpZK5cUv-Q8h2ybqZ3z2RIMUbS_t7o6zzZlN1af1EsUMhhg4XE88nzyE2czvHOdg6OkdjV7HIXMUQytrJhkH2qdDec5jAPH_lTY14hAfFxOXOQN38e0LPB7THrEtczsPcy1NmBC1tNQlPQ8fVmHqaKkBsKwk5YSaL7GjR9M72DT_m235AQ5QijTxSx0XupE6y-fWgk-X0_0TS7XJoTbsonQLiBGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ایتا و روبیکا تصاویری از یه سلاح ایرانی تو مرز ایران و عراق منتشر کردن که حتی خودشونم نمیدونن دقیقاً چیه :
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72875" target="_blank">📅 10:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72874">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=XXrbyHbZw4qeY5QbyfW6mYW4OvW1e7MmhW0LWVCX_Tkp5-gI1zVjvVApXORVqu001Oq9S9ICOmitUC8TRQtw9gHLoBZSe0VNkvaQqROeoeGKOjdiDaZQzQgK3YV0NkjD79_qWcmZlyetAb0cNS7WyaSIHHUo5Ifmh_GCNuTLiYGhaAGx2LD6wW6hd0KcLV6NhyIhlwGBRzhJIGxq3NR3luQjSoAdn9rW1rv069rTP2ZmfaxZysrVy38pmTOX-MSHOyey9NnfYY4--tHyy8x0ACAsFUdBd--hKy3YlfKlxqZ8ep_jWTB11ftuJm3238aNAsXnkZ2zjqran_3x4H1Sfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78e235c72.mp4?token=XXrbyHbZw4qeY5QbyfW6mYW4OvW1e7MmhW0LWVCX_Tkp5-gI1zVjvVApXORVqu001Oq9S9ICOmitUC8TRQtw9gHLoBZSe0VNkvaQqROeoeGKOjdiDaZQzQgK3YV0NkjD79_qWcmZlyetAb0cNS7WyaSIHHUo5Ifmh_GCNuTLiYGhaAGx2LD6wW6hd0KcLV6NhyIhlwGBRzhJIGxq3NR3luQjSoAdn9rW1rv069rTP2ZmfaxZysrVy38pmTOX-MSHOyey9NnfYY4--tHyy8x0ACAsFUdBd--hKy3YlfKlxqZ8ep_jWTB11ftuJm3238aNAsXnkZ2zjqran_3x4H1Sfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72874" target="_blank">📅 10:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72873">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=uPXp3C2uf45ljtWhCJDh5fr9nHqq3U5acy--kcwQLOdSOLY5GXIAzemvkahHlkXRQzP8LlJ4gzSWKQfnEhSzIRIjsnKuzEkfTSTquMqqEev5JQBtM18YbvZ55Ftv7h83qN0rA4u-pnZiz0zMbDP27eFHh323g8AFbVHfCFlfLBPd8ONyZwxR-hUZZGTnvC-d8WVpMag-rIRNktYoIjx0a4mUTDdBa12Q-8v7ZMjdJfpUxAb3W3e5jo7Wwg32wm17qhjbw9dgIs3GNjI9L9LMSZty3m61UTNxNgfGTb8zw9BZR3p4emSiycUlpj433a3NCPYbVUT5nTeVFDw82FNL9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=uPXp3C2uf45ljtWhCJDh5fr9nHqq3U5acy--kcwQLOdSOLY5GXIAzemvkahHlkXRQzP8LlJ4gzSWKQfnEhSzIRIjsnKuzEkfTSTquMqqEev5JQBtM18YbvZ55Ftv7h83qN0rA4u-pnZiz0zMbDP27eFHh323g8AFbVHfCFlfLBPd8ONyZwxR-hUZZGTnvC-d8WVpMag-rIRNktYoIjx0a4mUTDdBa12Q-8v7ZMjdJfpUxAb3W3e5jo7Wwg32wm17qhjbw9dgIs3GNjI9L9LMSZty3m61UTNxNgfGTb8zw9BZR3p4emSiycUlpj433a3NCPYbVUT5nTeVFDw82FNL9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شک این یکی از عجیب‌ترین پرونده های فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72873" target="_blank">📅 09:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72872">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=cSFjHY0Fo0SlxdadVBWfJcGtKgOgOZRoTuABSgqh086-F9dqzx0NaeV2xmhOSecyDy3-EBSTjbSriX8Nj6em-Ga1_h92Fu5VVlyHKYJH2LNdEH1AuNWWVTvm5VhUECe26p6BdZVD3-AdrGDlHn4cTEMRgNSEyS2cZCnJgu-exLbvWMhecPJu6muSP8DvNcaJPIex3fj_FmqB-DRBQXoQTvWWo4LsVyIiRt2WIe-LZ-i6cn-L89J-mkzvlMN8md7zQaPDvt1OueevxNBydFuvzpOaA4rnRYA3xhrVE7iz_7a3SZ1qwJKkDGJu6flhfSgQpErEmtFOe_thhWdR9XIIrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da58b38a06.mp4?token=cSFjHY0Fo0SlxdadVBWfJcGtKgOgOZRoTuABSgqh086-F9dqzx0NaeV2xmhOSecyDy3-EBSTjbSriX8Nj6em-Ga1_h92Fu5VVlyHKYJH2LNdEH1AuNWWVTvm5VhUECe26p6BdZVD3-AdrGDlHn4cTEMRgNSEyS2cZCnJgu-exLbvWMhecPJu6muSP8DvNcaJPIex3fj_FmqB-DRBQXoQTvWWo4LsVyIiRt2WIe-LZ-i6cn-L89J-mkzvlMN8md7zQaPDvt1OueevxNBydFuvzpOaA4rnRYA3xhrVE7iz_7a3SZ1qwJKkDGJu6flhfSgQpErEmtFOe_thhWdR9XIIrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
حداقل شش ماه اول امسال، عمده کارهایی که کردیم این بود که دو تا موضوع مهم رو به نتیجه برسونیم؛
یکی کنترل تورم، چون به‌خاطر رشد نقدینگی و فشارهای ناشی از دو جنگ پشت سر هم، نقدینگی شتاب بیشتری گرفته بود.
دوم هم اینکه توی این شرایط بتونیم کالاهای اساسی، دارو، معیشت مردم و مواد اولیه کارخونه‌ها رو تأمین کنیم.
این دوتا استراتژی اصلی بانک مرکزی بوده و خوشبختانه بخشی از اقداماتمون هم به نتیجه رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72872" target="_blank">📅 09:01 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
