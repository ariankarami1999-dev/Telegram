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
<img src="https://cdn4.telesco.pe/file/IKvTy8_gV2jvj-MFsmrDB6mECCFRgRIE9HzaI0pRgMjrbH2CV2OnCXQ__nLY9_ta02gKzK45DaTXIUCJMdV69eNORqkAeVG79idMQNN0wka40G81JJ6sGRSnhaDlSkp_zCkDP8OkYRsHs6osXiQ_DHqFQ6mN4HQ_ZlPwA2gN9_ujzcw1z0-MShmXnVjUs6cRbTW6mRxUVJNnilHzLU51XLmu17YCjtiX0b_hR9EE_KxkD0c-CTENUtGaVuz4WQ_FouXMTtzUe6EE5fdsHT2R0yimXC9fI3W5JIyh2V52ONwk9v3YNNKaEca50k9SplocstD2CP5vgYSezPJmv87Fmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
<hr>

<div class="tg-post" id="msg-150190">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سنتکام: نیروهای آمریکایی روند خروج نیروها و تجهیزات از پایگاه هوایی اربیل را به پایان رساندند
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/150190" target="_blank">📅 13:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150189">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
جمع‌بندی حادثه عجیب پرواز فلای‌دبی به مقصد تل‌آویو
✈️
یک فروند بوئینگ ۷۳۷ فلای‌دبی که از دبی به مقصد تل‌آویو در حرکت بود، ابتدا کد اضطراری 7700 و سپس کد 7500، مرتبط با وضعیت احتمالی مداخله غیرقانونی/هواپیماربایی، را مخابره کرد.
🔴
هم‌زمان گزارش شد برخی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/150189" target="_blank">📅 13:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150188">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6cb9V5ghqvrxiCGLiqj_5kUgy6xWagEQmMkaV_7Np4TH7spblLAPElc3ZcCfCyQoA8QUR09JbeG06viX1NNV5rZmO23SUbOB-wcIdpMvaMjvfueCtmeAYgvkytYgIl7iABchK1vVB2VFi2d8pL2mCwuH6SzGU1pkYBn-UpWjQXo60_ha_EWKWbOSxztl6mdE-5OybC52SAfVFJfk2LUM7qetBgo58ZB2o9OXguhAR9lSghHLnqX8G9Rw7KJw6TLMsOw8rvTTlveufDHzpbkqmjvOQGDKpfu5yHysTMibrJk0WdCLftar-KN_63PVl2P3ugaF3fJWU4p9wRILk5Eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نفتکش در تنگه هرمز مورد اصابت پرتابه قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/150188" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150187">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
چین: آمریکا و ایران به تفاهم‌نامه اسلام‌آباد برگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/150187" target="_blank">📅 12:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150186">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سخنگوی سپاه : توی هر ۲۴ ساعت در تنگه هرمز درگیری نظامی وجود داره اما مدتیه که آمریکا پاسخ نمیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/150186" target="_blank">📅 12:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150185">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
یدیعوت آحارانوت: تخمین‌ها حاکی از آن است که حادثه رخ داده در هواپیمای فلای دبی یک اقدام تروریستی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/150185" target="_blank">📅 12:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150184">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
یدیعوت آحارانوت: تخمین‌ها حاکی از آن است که حادثه رخ داده در هواپیمای فلای دبی یک اقدام تروریستی بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/150184" target="_blank">📅 12:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150183">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c905f1bc3f.mp4?token=Q5dd0snE3qTnt81vEcXDb8LuBPh9n6lcuzOeIVKhqlLlaktbV14mt81ecXDDhbF2QlUJDRsAmHEFfYbanRH4nY-bVAdU0aqU8UB3EMhKwtDzDy7cqW-5fDpNNsA65TiTK_JeeGujnpnRGDAQQskhOwBarOGaQ075igss5rNVl_041QxehDnSIoLnkaw2l1xlOwSg0zQDpyP_chW_L5RpijtDav9g1XJ8A568qqELzrHjNrNv1NrYQQd77QE0J-Yec2T3cdjkr56fR4qcRSlH7L3KZn8lgBeD_q0I3gT-U9AzvxCquk5vc2wMaay8VT_2efxn3TBPlXJP9DCVXVXmHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c905f1bc3f.mp4?token=Q5dd0snE3qTnt81vEcXDb8LuBPh9n6lcuzOeIVKhqlLlaktbV14mt81ecXDDhbF2QlUJDRsAmHEFfYbanRH4nY-bVAdU0aqU8UB3EMhKwtDzDy7cqW-5fDpNNsA65TiTK_JeeGujnpnRGDAQQskhOwBarOGaQ075igss5rNVl_041QxehDnSIoLnkaw2l1xlOwSg0zQDpyP_chW_L5RpijtDav9g1XJ8A568qqELzrHjNrNv1NrYQQd77QE0J-Yec2T3cdjkr56fR4qcRSlH7L3KZn8lgBeD_q0I3gT-U9AzvxCquk5vc2wMaay8VT_2efxn3TBPlXJP9DCVXVXmHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار تجمعات شبانه: قالیباف رسایی رو رها کن؛ در مجلس رو وا کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/150183" target="_blank">📅 12:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150182">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737da06d5f.mp4?token=m-GLnOG0KYKDDKKggIGwhTGoBooh7kfkr_TgslRtWxeEHjpVX3gD399zxybuL3IQrm3tO7I8-Pcgao0FL_e9E1IYXDDz33LbzD7x20qfkh26a5eCjxd19kXivnx8kbOCRZU1weoZsmfRkT15hYzxFW-vh3R0i2T-00Y1f89Ki4wCVc5PRJMMEDE5-2fulhFvo5mWEkkZnCCzDgnBaBLUIHi59nA0ZLIqX5CH8rQiFVa4QJSsL1MsGkt1o_62MHjkeOoJGNozIoyK2UNnAuSoxEaNJWsaL5aflv52TUen9tZARW7iPhwHOHImAg-UH70iSO_vccOSgSSJE2IKwiE36A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737da06d5f.mp4?token=m-GLnOG0KYKDDKKggIGwhTGoBooh7kfkr_TgslRtWxeEHjpVX3gD399zxybuL3IQrm3tO7I8-Pcgao0FL_e9E1IYXDDz33LbzD7x20qfkh26a5eCjxd19kXivnx8kbOCRZU1weoZsmfRkT15hYzxFW-vh3R0i2T-00Y1f89Ki4wCVc5PRJMMEDE5-2fulhFvo5mWEkkZnCCzDgnBaBLUIHi59nA0ZLIqX5CH8rQiFVa4QJSsL1MsGkt1o_62MHjkeOoJGNozIoyK2UNnAuSoxEaNJWsaL5aflv52TUen9tZARW7iPhwHOHImAg-UH70iSO_vccOSgSSJE2IKwiE36A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر ویدئویی از لحظه فرود اضطراری هواپیمای فلای دبی پس از درگیری در کابین
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/150182" target="_blank">📅 12:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150181">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مهاجرانی سخنگوی دولت: در جلسه امروز پیشنهاد طرف آمریکایی توسط عراقچی وزیر امور خارجه کشورمان به رئیس‌جمهور ارائه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/150181" target="_blank">📅 12:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150180">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پزشکیان: به آقای قالیباف گفتم اگر ما مشکلی داریم کمک بکنید؛ با حذف کردن مشکل حل نمی‌شود  ‏
🔴
واقعیت این است که ما همه عیب داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/150180" target="_blank">📅 12:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150179">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6b8d09462.mp4?token=abxrixAV-eCfkw-_LP8bL8kcs7ZZGetF8JGEsHEZjMlFJ5s2CVTZAhvqbf57iPwKl64z8YxI36mFvCdajZuIeNdI9nCjQt5Jz6b0fDDMp32hPTIrGOeou2moLh4Ca4URnaDHGTthiUxyO1xf-gcpLa7eTS3c7Z9-7Ewuw6cRbAVDOC-wuCg6n6ezeCdmjFHV72vH0Z2RX7dM4Cmwu3ObhrUwjEH9WYHzv7nyUD43llHiFQIIiN-cMIP6KWREe1FyFPEbuJD9HEXdWrhhsdfMF_w7ejl6m7YSDtUVujB0FYDbqNgEr15HzIgQ7pc91d8tXGD5yIrVYLpfdbZiu21o0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6b8d09462.mp4?token=abxrixAV-eCfkw-_LP8bL8kcs7ZZGetF8JGEsHEZjMlFJ5s2CVTZAhvqbf57iPwKl64z8YxI36mFvCdajZuIeNdI9nCjQt5Jz6b0fDDMp32hPTIrGOeou2moLh4Ca4URnaDHGTthiUxyO1xf-gcpLa7eTS3c7Z9-7Ewuw6cRbAVDOC-wuCg6n6ezeCdmjFHV72vH0Z2RX7dM4Cmwu3ObhrUwjEH9WYHzv7nyUD43llHiFQIIiN-cMIP6KWREe1FyFPEbuJD9HEXdWrhhsdfMF_w7ejl6m7YSDtUVujB0FYDbqNgEr15HzIgQ7pc91d8tXGD5yIrVYLpfdbZiu21o0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: به آقای قالیباف گفتم اگر ما مشکلی داریم کمک بکنید؛ با حذف کردن مشکل حل نمی‌شود
‏
🔴
واقعیت این است که ما همه عیب داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/150179" target="_blank">📅 12:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150178">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رسانهٔ اسرائیلی:مقامات اسرائیلی در حال بررسی این احتمال هستند که یکی از خلبان‌ها تلاش کرده باشد هواپیما را به دلایل سیاسی ربوده و خلبان دوم تلاش کرده است تا او را کنترل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/150178" target="_blank">📅 12:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150177">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
فواد ایزدی تحلیلگر صداوسیما:
دفعه قبل ترامپ اجازه داد تیم ایرانی از پاکستان برگرده بعدش محاصره دریایی رو شروع کرد، اما ایندفعه قبل از اینکه تیم ایرانی از نیویورک برگرده محاصره هوایی رو شروع کرده و اصلا ترامپ دنبال توافق نیست بلکه میخواد حکومت رو سرنگون کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/150177" target="_blank">📅 11:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150176">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c78f9d54.mp4?token=SVO_tuejzH7Uw_RcAnBXRQTq3S5c7ec8h3qVolj8BkUui-dXcLVausvq8pmyFyTTOx7WZ77aa3mP_9YlE8xmNJo7kGy_tlxZFxl6IW04mPL563q9LyzAGICb5Isuyw5sX2ncT1v1HdUkZaHM5zj-8s7iusao0dDFpVobbAgnv9qeU3UPR-7P9TqPxImedzizep0DS7ag4oAb_p47HoVREB_I8ZUs0MZaFEM0yOuAvl7jFvWzuaRSJgh_940j-dFAUcdjc9fEF0-6y9XvwfhfMtYEjyG3Ja-Nl0ygnw_u236s4Rjb_taSUOxoHcQR-_cVCVxtengogDP7v1w6PIBHhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c78f9d54.mp4?token=SVO_tuejzH7Uw_RcAnBXRQTq3S5c7ec8h3qVolj8BkUui-dXcLVausvq8pmyFyTTOx7WZ77aa3mP_9YlE8xmNJo7kGy_tlxZFxl6IW04mPL563q9LyzAGICb5Isuyw5sX2ncT1v1HdUkZaHM5zj-8s7iusao0dDFpVobbAgnv9qeU3UPR-7P9TqPxImedzizep0DS7ag4oAb_p47HoVREB_I8ZUs0MZaFEM0yOuAvl7jFvWzuaRSJgh_940j-dFAUcdjc9fEF0-6y9XvwfhfMtYEjyG3Ja-Nl0ygnw_u236s4Rjb_taSUOxoHcQR-_cVCVxtengogDP7v1w6PIBHhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ربات‌های چینی با لباس‌های سنتی عربستان، برای شهردار ریاض و سفیر چین رقص محلی اجرا می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/150176" target="_blank">📅 11:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150175">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1bE1ziDmhDBMTfvZnS9kyT_gRRkTeQZa-8TVIlMUvCQhQ1UrD88zzUjAOfW7ZiCXrEnmGWhB7I9ue1jaCkDWwA3jOMJ5nZqjLE6JY9RHrdSXroHtjO2-dzCUsi9jtMOsEKTXpFgM1wdp_RS3SD5nV3cUdnflNJbY1N7fJLZWmSRCy0aDb2Obm5WBUEGOwdMKGMx0DeTYdvAOYlPu4Aw1CqHwzsuFPlHYGohEGZfDI5IO2ZvUCojAV0PnZY_SkHGTezYqXqyMy14JQi5zah8HvWOasdI56Mr33G85h33olC0eBoKKlkWZQzp9oJ_8H4myWx3zQJcBmKMpaw-vcWZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین:کاخ سفید به طور مخفیانه از امارات متحده عربی و عربستان سعودی خواسته است تا اختلافات خود را کنار بگذارند و اجازه دهند یک فرماندهی نظامی واحد برای مقابله با حوثی‌ها تشکیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150175" target="_blank">📅 11:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150173">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6pDLdRs8U_qCy-wppnabNewoj6iQ65dqA8NJlZ1Jrj7tDZIUD90HvtUJ_6Mg2y3gB8cCs8kc79wYqDV-O4ewWTQnO4LEpvqKIsQdBX_dbS6UB29WS9jkJayWjdpV_JxKmfibKagv-r8ARe72b32a7uxH3vQT8luseQCKWtD8Ll64VpdPRdq15iGyMAEWSX5H16dxO5WmlMt2Iy4iTePlUAYE_LFO9mBqznJNXtHXFFc-saVCvhllNeackx-UQoZnZKxjHgM0ZJR2KN3biQ1V588Glbn18FyMVCsYrSZUm6TRp0SODBEUbSwIxZxNEFIrdfw76sp5Ih4e6d2SaEpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nR_Oi17S1t_8Fwaj_xKBTg4iLWvueIn9ycjH7x0u-0YzM9RxXzxwnusoO8rgYQQAvp2gHJ6_bvsLeoFnzi0QVti3BCT3ikEtePdQ2bgn32T_-4WNhh4E7Dvl18Czkz618WTFmdxuezxanzvsD5MfY6jt4936ZAFROd_4bwbW08j5W7jR2wlk5tOYN1_c9TfFeVoSBz6kTtqxVI3ETjGh0LvKrzSYS0_uvjhnICQXEB05mulew0z1qeIg1vP9EZOTSSV7XZo2wFMbP23-UHjJlh-CYbtCKhsF67EFTmKudSvNkRV9GMNHUuTic7BpUZbcKsBwwSL9CgreDiKlF5ZLeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مسافران هواپیمای اماراتی در خاک عربستان سعودی منتظر هواپیمای جایگزینی هستند تا آن‌ها را به مقصدشان ببرد؛ برخی از آن‌ها پیراهن‌هایی با لکه‌های خون به تن دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150173" target="_blank">📅 11:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150172">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نتانیاهو به رئیس دولت امارات:
اسرائیل اطلاعات جدیدی از احیای برنامه هسته‌ای ایران دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150172" target="_blank">📅 11:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150171">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sraYVM029vfP0vHcQpV1yXGG-vUQz4sNF5moKSAAnRsuyz-uC-z6eUuElEg5EFXNtSkWbyCspT6A1rgkSI8_qeC3XncsjjwQ44jsLHVdGarCg4SoKjTolkxP81iOCeRUYRW2PfiFAHV0ZMuZ7-Ibscb8X3ta6OJMzjQaR1-uASy1YU-ecAYprAlOIKabpp29AlKKk73zVzhAjDDpEM7gmSZwZEPZtdi_kSfheqXcfYr7y1bBNhHY4E38QLl0zNwXYznzgGqRGb2FNdxmU9AwwmSaT46_nR4zB0Btxqz-9bNtacR-PTlC7pLONkeWOD2SFVp2YyjPyzKuqYVO4lo16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود ناشی از اصابت موشک‌های بالستیک تاکتیکی ایسکندر-ام در شهر دنیپرو، اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/150171" target="_blank">📅 11:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150170">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رسانه‌های آمریکایی: نیرو‌های نظامی آمریکا امروز، پس از دو دهه حضور و مداخله نظامی در عراق، پایگاه‌های خود در این کشور را ترک می‌کنند
🔴
نیرو‌های باقی مانده ایالات متحده، به اردن منتقل خواهند شد
🔴
شماری از تفنگداران دریایی آمریکا برای حفاظت از نمایندگی‌های دیپلماتیک این کشور در عراق باقی خواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/150170" target="_blank">📅 11:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150169">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل گزارش داد که خدمه پرواز شامل یک خلبان روسی و یک کمک خلبان اوکراینی بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/150169" target="_blank">📅 11:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d66c2f72.mp4?token=pBN5eHpGpUNI8jUWSF87BR9NEAgqwHsCvF6yNTetHB7TPtah_wNAUjKMpq_wpc09iu3M9LhoKkBQFP51XD85LFblDWYAx0K5NQk_ebfOdTXySNL9aWYJxtJlNFa3z6rXBaJNVbFb9Bh80jPzU2UT2--zm_J5YsX2tdyu8yJJeqscqXIW-koe3SEO1yWiWuMSCxQU6169pLyctj5wYov4iPkjIrWXfuYyJcHVYAGJL6YBtoBwViZGQORhU2GhYZLC_ZAkNYl77IGhGu2HUPUTj0vXu7DfNTM2rMLL4w5XZv08bLA-SFiO945FGlWU-ztHGXtWStysuMrmOIeERvy9-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d66c2f72.mp4?token=pBN5eHpGpUNI8jUWSF87BR9NEAgqwHsCvF6yNTetHB7TPtah_wNAUjKMpq_wpc09iu3M9LhoKkBQFP51XD85LFblDWYAx0K5NQk_ebfOdTXySNL9aWYJxtJlNFa3z6rXBaJNVbFb9Bh80jPzU2UT2--zm_J5YsX2tdyu8yJJeqscqXIW-koe3SEO1yWiWuMSCxQU6169pLyctj5wYov4iPkjIrWXfuYyJcHVYAGJL6YBtoBwViZGQORhU2GhYZLC_ZAkNYl77IGhGu2HUPUTj0vXu7DfNTM2rMLL4w5XZv08bLA-SFiO945FGlWU-ztHGXtWStysuMrmOIeERvy9-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروازهای جنگی متعددی در آسمان شهر طائف در عربستان سعودی در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/150167" target="_blank">📅 11:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iodPbvyX0A-GYQf74iDUb1Hh182gPQX8sM19olgqy8i1hHf8pMlwP4DlnexCFruvTbpOspMzUNNh1QuLlV-qV5xyNtVI5686Jy8p_PgT57P7VWgAmwmMItST1SSnuRmxz-tXW0lLFztSaSl-RcLeLQtdC94wn93vOr98-FSKRndVVFfnhKJz5A2oniOZ2E37aUmG617H0b5QW8hM2ZLw_9kXao4FKKaUn5-_VOZ8h3B9qT8GpO8YH5Q7TxH2LLOtmK5Id4Tvb38-HnTzg_IAE74IjuPORLGVTp7eJg5AbkPwtEySY3mFYIkJDh-LVC45FLa47WWOiHz9T-1dE3NjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کتب کمک درسی ۷۰۰ درصد گران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/150166" target="_blank">📅 11:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی :  دلیل درخواست کمک از سوی هواپیما، وقوع درگیری و نزاع میان مسافران در داخل آن بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/150165" target="_blank">📅 10:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): «در پی گزارش‌های اخیر، رئیس ستاد کل ارتش اسرائیل در دقایق گذشته یک ارزیابی وضعیت با حضور فرمانده نیروی هوایی اسرائیل، رئیس اداره عملیات، رئیس اطلاعات نظامی و شماری دیگر از فرماندهان انجام داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/150164" target="_blank">📅 10:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
مورگان اورتگاس، سخنگوی پیشین وزارت خارجه آمریکا : اگه مقامات جمهوری اسلامی منتظر انتخابات میان دوره‌ای آمریکا هستن تا قدرت تصمیم گیری ترامپ درباره ایران محدود بشه، دچار محاسبه‌ای کاملا اشتباه شدن
🔴
کارزار فشار حداکثری علیه جمهوری‌اسلامی و کشته شدن قاسم سلیمانی هردو زمانی رخ داد که دموکرات‌ها کنترل کنگره رو در دست داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/150163" target="_blank">📅 10:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سخنگوی نخست‌وزیر اسرائیل: حادثه‌ای که برای هواپیمای فلای‌دبی رخ داد، اقدام به هواپیماربایی نبوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/150162" target="_blank">📅 10:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/150161" target="_blank">📅 10:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150160" target="_blank">📅 10:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
پروازهای فرودگاه بن گورین به حالت تعلیق درآمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150159" target="_blank">📅 10:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تتر به ۲۵۹ هزار تومن رسید  برای اولین  بار در طول تاریخ فقط در عرض یک روز ۱۰ هزارتومان دلار بالا رفت.   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150158" target="_blank">📅 10:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150157" target="_blank">📅 10:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
منابع عبری: انتظار می رود این هواپیما 10 دقیقه دیگر در عربستان سعودی فرود بیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/150156" target="_blank">📅 10:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/150155" target="_blank">📅 10:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150153">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b51a72c.mp4?token=ue69fZBl9w_6CW58KPdmqPESJl5cPMNC5UdkktdFn62cgQmKkAY3zOghOhgNadZb-oV0FI1B4U7VHvSHaa7ONsKNYFtVlufnmPjuUGEawD_BsMf93UwaHM-jsOSZH2V9n2M3j29EemhNnLd1H2ZRsbfVlGfnliXuocrtbVDYXm55pyFJp-Z90bWSVk2LdzKz1wqeN-MzoEMeHzrraN4x3mDGvTCOTWn27xBTYGYULcfuU7v8JmgOxmJEruDDwN9U1SCxNDXSOaxl5lon7hcepDT7PdRTU9KSHWZbDhnW5lHa0m2nVilg5tBwyGht_fSRZGCMX82YwdB4n27lfuRW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b51a72c.mp4?token=ue69fZBl9w_6CW58KPdmqPESJl5cPMNC5UdkktdFn62cgQmKkAY3zOghOhgNadZb-oV0FI1B4U7VHvSHaa7ONsKNYFtVlufnmPjuUGEawD_BsMf93UwaHM-jsOSZH2V9n2M3j29EemhNnLd1H2ZRsbfVlGfnliXuocrtbVDYXm55pyFJp-Z90bWSVk2LdzKz1wqeN-MzoEMeHzrraN4x3mDGvTCOTWn27xBTYGYULcfuU7v8JmgOxmJEruDDwN9U1SCxNDXSOaxl5lon7hcepDT7PdRTU9KSHWZbDhnW5lHa0m2nVilg5tBwyGht_fSRZGCMX82YwdB4n27lfuRW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع ایتایی: کار ماست، الله اکبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150153" target="_blank">📅 10:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150152">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل در مورد هواپیمای بوئینگ ۷۳۷ فلای دبی: خلبان کد مربوط به ربوده شدن هواپیما را ارسال کرده است، شماری از اسرائیلی‌ها در این پرواز حضور دارند.
🔴
این هواپیما دیگر در اپلیکیشن رهگیری پرواز Flightradar نیز نمایش داده نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/150152" target="_blank">📅 10:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150151">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: مقام‌های اسرائیلی ارتباط خود را با یک فروند بوئینگ ۷۳۷ فلای‌دبی از دست داده‌اند و اسرائیل در حال بررسی احتمال هواپیماربایی این هواپیماست.
🔴
جنگنده‌های نیروی هوایی اسرائیل برای رهگیری این هواپیما به پرواز درآمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150151" target="_blank">📅 10:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است …</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150150" target="_blank">📅 10:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIrUAtWoH-u37EMz7He1iZw7YsgZAn6iTE_PFe2p6Nt3_bKeuNvaZ091SFLpUr3Ih4J6b6-zl92CnDIZCZsvFN9Dk9Q1PDsv53Dn6BY3Ydc1OpGQi9XgBB7Rwu6qw807wWWdJ3WA7Kc-IzCLoWJWCXCNJtuNByPV4zEbyU8_OE30-mb9ySMRjE_CSYbuNhfUvBZF4s_fxwraEEg_FOgBgVtSUXPMdWT4V5PU92CsnzGv3h_KhWOfxnas4L2R58YnTg_mqCFHbwUqAKUrEPlq8YDlVk0se-UCzfmZUkf0OXuL5pAykeKgeRxVbv6hsu8nz4h0GB4DoV1Ck4yVTcMSrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فلایت رادار: یک فروند هواپیمای مسافربری بوئینگ ۷۳۷ شرکت فلای‌دبی که از دبی به مقصد تل‌آویو در پرواز بود، پس از آنکه برای مدت کوتاهی کد اضطراری ۷۷۰۰ و سپس کد ۷۵۰۰ مربوط به احتمال هواپیماربایی را مخابره کرد، اکنون در حال بازگشت و تغییر مسیر به سمت دبی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/150149" target="_blank">📅 10:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گاردین: مذاکرات ایران و آمریکا نتیجه‌ی چندانی نداشته و احتمال از سرگیری درگیری‌ها افزایش پیدا کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/150148" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150146">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLfdmLBRD41zU7oryhtctM1kBziYbXDLa8G-qvMhuHWQsPeX0ohviEnG2VQ2uFq9D0n2MrFx88IBjtVV9NZt4QSHPuXbH0JkvdePvhjS0094VBlbqE2ZURYXDnsOvyIHrqKVJXwZOuAtguSpan6gTibpm8R7yJJURNQ26-uUhYR3rW0XRPsic6rvKy0syZ1rF2M2LHOt0bS2VsoERkjc16TvpwnQh2_-i8SPLsMnTLrhhYWaR5YIE9-n93Jr7ZuSu2s7FCKYMjyWz--VMbgVmP4gaPCTeb0CUDbCjj3bi8_WtVzzK-XPxheGyiAaV_HxmBYvfl7AK5tZkoIVbLFpSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFIsSV33Cy2jWH3P0rsFmpnfyCYidQRa60Z32C2oW1B8A6hrcUQVquMxBJ1ClL7-oUS0WOB1BZGYz-tNY5neKoOVostSCKLQ241Dzo7ynTFq6Wu66xyAO-lEye7vC1wf-gpH5t7RKhyjAOA4jPx8lhxjZBvbxZfquyuuQSNnEoBERo6fbEOAYsEVouQKm5nHrE_-FnXW1IdhclLtr3p9dPG4YNalIOG_Xd6cGKJPOi-RFDbi36Ks0Fyu6DyiN8lXw6RdKuU7aOBuIhXFtIOLARzBUwq2oH-1SBnKNox1Hpk9vSBP07uuORBgyupudX4mnhwha83yp9Me22NYLYkcgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ با فرمان اجرایی، «هوش مصنوعی» را به «ابرهوش» تغییر نام داد
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا، فرمانی اجرایی امضا کرده که بر اساس آن، نهادهای فدرال موظف‌اند در مکاتبات رسمی خود عبارت‌های «هوش مصنوعی (AI) را با ابرهوش (SI) جایگزین کنند.
🔴
بر پایه‌ی این فرمان، تمامی ارتباطات رسمی دولت آمریکا از این پس باید از واژگان جدید استفاده کنند و اصطلاحات پیشین در اسناد دولتی کنار گذاشته می‌شوند.
🔴
جالب‌تر اینکه برخی از مدیرعامل‌های کمپانی‌های مطرح دنیا از جمله AMD، گوگل، تسلا، اسپیس‌ایکس، متا، انتروپیک هم این تغییر نام را پذیرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150146" target="_blank">📅 09:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150145">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام آگاه:
سندی که ایران و آمریکا در حال مذاکره درباره آن هستند، طرحی هفت‌روزه برای ایجاد اعتماد و بازگشت به نسخه‌ای تقویت‌شده از توافق تفاهم‌نامه را تشریح می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150145" target="_blank">📅 09:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150144">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رویترز: عباس عراقچی و تیم مذاکره‌کننده او شامگاه گذشته در دوحه با میانجی‌های قطری دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150144" target="_blank">📅 09:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150143">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رویترز: اختلاف اصلی میان آمریکا و ایران بر سر ترتیب اجرای گام‌ها است، نه بر سر مفاد و عناصر طرح هفت‌روزه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150143" target="_blank">📅 09:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150142">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / رویترز: عباس عراقچی پاسخ آمریکا به پیشنهاد «طرح هفت‌روزه» را دریافت کرده است
🔴
عراقچی امروز در تهران درباره پاسخ آمریکا به این پیشنهاد گفت‌وگو خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150142" target="_blank">📅 09:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150141">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فرماندار ایالت کالیفرنیا با امضای قانونی، اعیاد فطر و قربان را به تقویم رسمی کالیفرنیا اضافه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150141" target="_blank">📅 09:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150140">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وال استریت جورنال در مورد یک مسئول در پنتاگون: ایالات متحده در حال پایان دادن به عملیات‌های نظامی رسمی خود در عراق است.
🔴
واشنگتن، توانایی‌های اطلاعاتی و شناسایی را حفظ خواهد کرد که می‌توان از آن‌ها در داخل عراق استفاده کرد.
🔴
باقی‌مانده سامانه‌های دفاع هوایی در عراق، بر حفاظت از ماموریت‌های دیپلماتیک ما متمرکز خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/150140" target="_blank">📅 09:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150139">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e4e9e398.mp4?token=PbcJuRZqR5aOPxlJP6fd6EzHiUwqV9GkxtZ693-mf9rKQgnnf4zpjj3e_HYq9HLFAiV0PWIWWOTSxaBcy6lfZo8Swrbx-IyavHDbGbckM7Lsp-Q1BszDkWgAHKeMl-wZCkuMgYOj9yGQmMMhTdwTx8FPPGgCBdxRA0Ze1TsibwbyftspgdQiOoqL7oEt2dr-TKgpaHzA8Dpmal7c4vBDJRdX6SOfDnfXZiCaTzODsW_OaMn3Ti4llD6TLFIfMwfN92ZGrJu6PbNa2BvIgsp2zjQN4rijo72zwjqzSQmLhvprapY2qhzqydJkmX1zD3ly1h10hhEUlVoPIBUfPCjghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e4e9e398.mp4?token=PbcJuRZqR5aOPxlJP6fd6EzHiUwqV9GkxtZ693-mf9rKQgnnf4zpjj3e_HYq9HLFAiV0PWIWWOTSxaBcy6lfZo8Swrbx-IyavHDbGbckM7Lsp-Q1BszDkWgAHKeMl-wZCkuMgYOj9yGQmMMhTdwTx8FPPGgCBdxRA0Ze1TsibwbyftspgdQiOoqL7oEt2dr-TKgpaHzA8Dpmal7c4vBDJRdX6SOfDnfXZiCaTzODsW_OaMn3Ti4llD6TLFIfMwfN92ZGrJu6PbNa2BvIgsp2zjQN4rijo72zwjqzSQmLhvprapY2qhzqydJkmX1zD3ly1h10hhEUlVoPIBUfPCjghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایران باید به آنچه آمریکا صلاح می‌داند، عمل کند
🔴
مجری: "آیا واقعاً می‌توانیم باور کنیم که ایران آماده دیپلماسی است؟ می‌توانیم حرفشان را باور کنیم؟"
🔴
کیث کلاگ، نماینده سابق ترامپ در امور اوکراین: "اگر کوتاه پاسخ بدهم، خیر ... عراقچی، وزیر خارجه ایران، کتابی درباره مذاکره برای ایرانی‌ها نوشته است. من خودم این کتاب را خوانده‌ام و اگر آن را بخوانید، متوجه می‌شوید که این تقریباً همان نقشه‌ای است که آنها دنبال می‌کنند.
🔴
زیاد درباره مذاکره و دیپلماسی صحبت می‌کنند، اما در عمل چندان به آن پایبند نمی‌مانند ... باید به عراقچی بگوییم برود یک گوشه بنشیند، ساکت بماند و فقط کاری را انجام دهد که ما فکر می‌کنیم برای جهان، منطقه و شهروندان آمریکایی لازم است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150139" target="_blank">📅 09:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150138">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVFmQR-6mw8gHNb71smvAOp1ohvCKGCeyPoDp41mUzFlzvAkFFyXSvWm_Lc_EJexTgXpWNtIB9jk3yotDzoo6qUNju2ixz9DZw3KuS-5oBsoa_Ulhsy8ugLSo6OQ5Sq6QUOL0gYs0wdukeeiJpegZrrgmF15YjU-1GS2-3z8R5V0-mzMDbHKgMILRi_uIyxUZhn6ZXHkuIdTN83ssthHs79_DSrl0XzYzHdQvk5SmQ6M3QIoim-q2Ned3dsIFxdvRYRojjrRSDMEmbGHy1dYtgSn1EkiZelQMLaeA_8BznzjvfTJn8QNSYmB-9EUsF3PPj7gPKzJ5ae_H2Mb2nH63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به ۹۶ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/150138" target="_blank">📅 09:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150137">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گروگانگیری ساختگی زن ۲۵ ساله برای گرفتن ۷۲ هزار یورو از همسرش
🔴
مردی طلافروش در تهران با مراجعه به پلیس از ناپدید شدن همسر ۲۵ ساله‌اش، مارال، خبر داد. یک روز بعد پیام‌هایی دریافت کرد که در آنها ادعا شده بود همسرش گروگان گرفته شده و برای آزادی او باید ظرف ۷۲ ساعت، ۷۲ هزار یورو در پارکی در شمال‌شرق تهران تحویل دهد.
🔴
پس از ورود پلیس به پرونده، پیام دیگری برای مرد ارسال شد که مدعی بود مارال به قتل رسیده و جسدش سوزانده شده است.
🔴
حدود یک ماه بعد، روشن شدن تلفن همراه مارال در یک شهر مرزی سرنخ تازه‌ای به پلیس داد. مأموران هنگام بررسی یک خانه با خود مارال روبه‌رو شدند که زنده و سالم بود.
🔴
به نوشته همشهری، زن جوان اعتراف کرد قصد مهاجرت به لندن را داشته اما همسرش مخالف بوده است؛ بنابراین سناریوی آدم‌ربایی و سپس قتل ساختگی را طراحی کرده تا پول بگیرد و از کشور خارج شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/150137" target="_blank">📅 08:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150136">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نیروهای آمریکا در حال ترک عراق هستند
🔴
انتظار می‌رود خروج این نیروها تا فردا تکمیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150136" target="_blank">📅 08:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150135">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8p5qqeVwtZ7QbUSeNiV_a_MBgt0Aq4Z0fICB1_blc-BY4_lpenSfTcYNZl1DaFmGMHMG2lpzJqOsAYvOibvGsJ3MpXpUCSj6qip5BrGGP2KfQX1K8KfKkj5NhU1ueC_xZQGGyWVkYaGDZT_WiCg8C4cCWLoO8S2tWy1952TixDkxRyzukqq4eldD-36sSCvlJf9NK32PoNJeVBrdfMss5SvBri-sPKPUd-jIQZAVcJsN5dB9ena2OyWuy9LZkJq1hKRvbtEBBI8E6r3evVHWwoU0vKGj0lnwlYxRBJgc6W7n4GfUPmEQpLQXMjiA1-inrRnrJI9gcPbH9Voe0viwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع پاکستان: هر چه داریم، برای ریاض است
🔴
با امضای پیمان دفاعی سه‌جانبه میان پاکستان، عربستان و ترکیه، عملاً مرزهای امنیتی منطقه جابه‌جا شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150135" target="_blank">📅 08:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150134">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام ارشد سعودی:
نتانیاهو در جریان سفر اخیر خود به امارات متحده عربی، با هیچ مقام سعودی دیدار نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150134" target="_blank">📅 08:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150133">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsrPDGTE4L9PeBKDHKp4vOPIOC1SYUuPNoALMmpJJn7Tb1xUAW225q14m8M6E0iUUblIRFvAZjehq22hnl6ZYdNZ1huPOwN5iRAau3PiKf2AUSKIYHb869GeCJQSTofw9VliQt3P8QsfBaXUu6btDF1f-vpezjgC_0H4xl912vc30RDb4f5aTkrds5WEtIfouTQfCbE0N61d_at0rMztPnRE4XCFtQL1yAhd_JD6Y9e9K4Ft7z6rTdhmUMrLs9nJde4FwgEwWJOjvekYna5LDzdxQuw0m2s7rXqwy8F5ekvZZTRSIPhfX6sBoNSs2MUpQeNshdfJzwa1MfDmIEJByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس عراقچی به ایران بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/150133" target="_blank">📅 08:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150132">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سی‌ان‌ان: نتانیاهو به محمد بن زائد اطلاع داد که ایران توسعه برنامه هسته‌ای خود را ادامه می‌دهد و پروژه‌های ساختمانی جدیدی در جنوب تهران در حال اجراست.
🔴
اسرائیل احتمال حمله ایران را در «چند هفته آینده» مطرح کرد. یک مقام امنیتی ارشد سعودی نیز در این نشست حضور داشت و موضوعات حوثی‌ها، تنگه باب‌المندب و تنگه هرمز بررسی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/150132" target="_blank">📅 08:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150131">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی: ممکن است ترامپ پس از انتخابات دستور بازگشت به عملیات رزمی گسترده علیه ایران را بدهد.‌‌
🔴
ایرانی ها اعلام کردند تا زمانی که واشنگتن با بازگشت به یادداشت تفاهم موافقت نکند، امتیازی نخواهند داد.‌‌
🔴
هیچ پیشرفت محسوسی در مذاکرات…</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/150131" target="_blank">📅 02:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150130">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی: ممکن است ترامپ پس از انتخابات دستور بازگشت به عملیات رزمی گسترده علیه ایران را بدهد.‌‌
🔴
ایرانی ها اعلام کردند تا زمانی که واشنگتن با بازگشت به یادداشت تفاهم موافقت نکند، امتیازی نخواهند داد.‌‌
🔴
هیچ پیشرفت محسوسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها چیزهایی را طلب می‌کنند که واشنگتن نمی‌تواند آنها را بپذیرد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/150130" target="_blank">📅 02:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150129">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO0wZv0WzeDadT2xy5fKRrog3k4tT-pzGUEs-7q050pjGlclN7WQY47aoxGWYXA_jv6JmOkHki3oENCJpbWYyfRTB_F3bNQ2dCV-YP31AEpbU9oHDSElTI9fhwvrF4H9k3bH5VWqeGVdkwvbdHN0OlnvsxEOXXUT33uaxlrCgAUlX3WrzBzxPfPTvxhHeEys2WhwfVYI5hJS_8cfmgTF2QmAF27gNjDZwngqXTr51ukVRprB_aJ5qbhYdUjb6E8-WGAd-CFRg5BfQx40B7gJgkQDVk7FNquJaliSC0lF4oaNxySLs94evNn5T7VakcB0TjGAKeTM8kKTAClKWqpeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
پاییز برگ ریزانی خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/150129" target="_blank">📅 02:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150128">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ایلان ماسک:
هوش مصنوعی در آینده خیلی به نفع مردم قراره باشه، بخصوص باعث میشه درآمد مردم بدون کار کردن هم افزایش پیدا کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/150128" target="_blank">📅 01:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150127">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b51a72c.mp4?token=SeVhtJsohqpA-3Zg4gf1LPwmNkyy21mTdAOMqhUsYieZ2uUaboLmTSaWIsybmiXU3agVvnO-uYoWCEQfDTrwkSTqopPZdOKk00jEFV2D8o41PlioO6DM8z2_0bz2Ye1PQRCr0J5LtMlfw9Q-EKSRDHxHLHrOqIlIPyNDBvCFcETVOM8Tl7XvxQZIf1JoHGlCAuBwZyGB2MHGW5I1QUYOVNUsUZSRR1i1LBDVaYBkfyiZXarhqRRSlBKiVLOW5VFTk1q6vGqZzeKCh0ELgOq4FCutjVpTD6S1NO-9xezLSyRS1MUkMdpApE6wBSRqtFlKqPdAtHkKnEryDlenT1_uXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b51a72c.mp4?token=SeVhtJsohqpA-3Zg4gf1LPwmNkyy21mTdAOMqhUsYieZ2uUaboLmTSaWIsybmiXU3agVvnO-uYoWCEQfDTrwkSTqopPZdOKk00jEFV2D8o41PlioO6DM8z2_0bz2Ye1PQRCr0J5LtMlfw9Q-EKSRDHxHLHrOqIlIPyNDBvCFcETVOM8Tl7XvxQZIf1JoHGlCAuBwZyGB2MHGW5I1QUYOVNUsUZSRR1i1LBDVaYBkfyiZXarhqRRSlBKiVLOW5VFTk1q6vGqZzeKCh0ELgOq4FCutjVpTD6S1NO-9xezLSyRS1MUkMdpApE6wBSRqtFlKqPdAtHkKnEryDlenT1_uXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تتر 259 هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/150127" target="_blank">📅 01:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150126">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏
👈
وال استریت ژورنال:
به احتمال زیاد به زودی سپاه برای بازپسگیری کنترل تنگه هرمز حملات پیش‌دستانه علیه آمریکا را آغاز کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/150126" target="_blank">📅 00:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150125">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVs3v_KDOuzjBCT2lgO_GtnLYWKnmG1J-xRWB73tR1kFHFEkU7yM02yvQcyUu8AMbQ71ExAq39yRYD3xk0TTXtO7QI63Cz9PsBehO34NMtAKDjzjYvZbmGRkIR-_VphNkXYs7vSz2rnffwo8h_FjA5QPfJwU9Fx6CkB10xGeqWA2tY95vus5gPlO0RwrV5ewtkG2Mc8kdSH2gEdTYX6JTjetLBOIxehysp1S9-O82oODFrUimlFLfFRhhKcalI9R7tKaYTp4ZK-_Ffq4M5ErSh4HJDrAgt2c7ZzffPHa9AvRscnAM-Zr_BfZ8WzJwu4CMCtDUXOUgMo6098pbix1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرباقری: فرمان ظهور امام زمان صادر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/150125" target="_blank">📅 00:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150124">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb12dc46c5.mp4?token=aTNhDFTB7Uz9160A2LrJPtzfKGW9bkVGmDvxbpSVN-cwUcm8wne3-eIiuTUkdL5vS60mjiK6BE81tZ5AnKQeadkj1peW2KiVDZ1JFCNaItjqiDKskh9cREr4um2IEIUwku6rmZWpzNJNDgGiO3Ka-Nu5TJNB2twLRA9by3L4Am-zljQDc4xkNnOX8M3eqZNEBW8MJA53Bj8ZSHGWMmN8BHjYaOZzipz9lNu1Zw1iAEV876cWe95icKmnjafzDiLcbVrrC8rm9bGQcEN8lLvTO3n1lzp_vEGYP4xuzFu0b8zxL5wafuYYVo9rPG2eD9X-yA38sn-pgD2LTxUokOtD1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb12dc46c5.mp4?token=aTNhDFTB7Uz9160A2LrJPtzfKGW9bkVGmDvxbpSVN-cwUcm8wne3-eIiuTUkdL5vS60mjiK6BE81tZ5AnKQeadkj1peW2KiVDZ1JFCNaItjqiDKskh9cREr4um2IEIUwku6rmZWpzNJNDgGiO3Ka-Nu5TJNB2twLRA9by3L4Am-zljQDc4xkNnOX8M3eqZNEBW8MJA53Bj8ZSHGWMmN8BHjYaOZzipz9lNu1Zw1iAEV876cWe95icKmnjafzDiLcbVrrC8rm9bGQcEN8lLvTO3n1lzp_vEGYP4xuzFu0b8zxL5wafuYYVo9rPG2eD9X-yA38sn-pgD2LTxUokOtD1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آموزش زنان جانفدا برای مبارزه نظامی با ارتش آمریکا و اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/150124" target="_blank">📅 00:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150123">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0jXziD_Zyzlw18KlCxu_IDxo_-IrT2vx1-ynDHGHLa0N9k0OOKOKc0ADDJqMyG8HeNMaasosD_93hFXOzNF89T0NQ6fQAH4GAROIJKcSRrGYREnlsSsT7AYm-p1wNmkHaGIiLTNEWYprkZeYbc04pQxJvb2nntrboTO_Podg-5Ttoz_Vg8Y3xyyxY4L-SLCFU91yatuXPo8cec6Bn2DrM2nbR4Da45Gpn9MfKDfd7SGC_YHS-4FOf9BHciNqollfabFCZ8LSvOrR8WPVxpJI3GmwvbTSiDvkSGiGk_bCLRlcB8AHFjH9euygxyTJmwoHgOlLCK4XahEQ2xqnUB73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه میلی‌گلد: بعد از پیگیری‌های میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد
🔴
خدمت تسویه و تحویل که به علت مسدودی دارایی‌های میلی در بانک کارگشایی مختل شده بود، فردا عصر پس از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت.
همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/150123" target="_blank">📅 00:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150122">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دختری که پاشو میداد پسرها بخورن و فیلمش رو منتشر میکرد، بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/150122" target="_blank">📅 00:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEhqHpXlK8rO2LxOhFpAjKRZ1LlnTF0EcY--m8CA4tTUG5S_UZ7NMheZr8innY29-BYZHkx9mV4CbDbM_MTtWAx6b2YmPivOluGDK2ezj-iP01CbDL27b3fIYyktKu9dQgk4IRZ1pAKdKBzdx0TtGaWCiuTmjL9GMjhDUcwVc6DWqgpVU4rflYlFRB_dRet29BWB3Le4h06Hs96AhgjsVEtqgvbahwHvC2r08YLjiG8V-rOIO0WpzplODeCpUMucisqvQF-bXVQbHKCd97JzAXIhWpOpy9vxypMunDcPJi-0Q1PPXTTS5YNkCMNn5Wpfmph15LGmnN2P5BtY3ki3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دختری که پاشو میداد پسرها بخورن و فیلمش رو منتشر میکرد، بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/150121" target="_blank">📅 00:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150120">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/مارک لوین:
آماده باشید، سوپرایز در راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/150120" target="_blank">📅 00:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150119">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elypAIm_xcVmFy7ZLbG0LbfJu6uMzC7_YzmthWm2R9EYrmXZBjnV_Ewsegdxz6MEDV6ZUtiVIWcycF_9ItVd4D5joH48GP0lYYj2NWLzpAipQrEptw25KTbUUec3dkeA1zTbB3s8PrCEXCNiZIFYweWp5wsO1xOwJDibcnW2dVar9cheEbM23IyCB8D5Bq7bhgBGWBqW6go0uN5qhB5B1QnJ_GN0KLKsV_0J9tAvHZq5RWUOAtZMswit7IFmBVNqIGe1kw6RAebmnfJA75G7mYS4PcC4cOoTEqh_JK82wd5tvpoxGEsleoNyN6j00E7j84cuymrVHR0Rz03dfs-okQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی خبرنگار نزدیک به حکومت: آیا غیرتِ «لابیِ امارات» در ایران، این‌بار به جوش می‌آید و می‌گذارند «اسرائیلِ کوچک» را در جنوب کشور، کمی تنبیه کنیم؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/150119" target="_blank">📅 23:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150118">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: ایرانی ها خیلی فقیر شده اند / ما ایران را از داشتن سلاح هسته ای منع کردیم / تنگه هرمز کاملا باز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/150118" target="_blank">📅 23:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150117">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e6dab3e8.mp4?token=oUuRkT2OKmRq8YkYe8eNI2apYO-B-aaf0QykpZa_5gIzP-aSekoEVVXq6vPTN8yZeBJnrzyYAmjZivNsxdAy98I9G0FYNzYjM6BDBI56_PAkZczGlei91m0TuWtDH75wgEB2dqvcpvq-P0dwaexEQD_93GSktBDHfdGsuTtgtARM-H7lJHtfyZ5TdJlJz-ckYYzqKeN05d9SERZ-RxSrooVXGwomUjBUm6_IZugrCEBSR5sW5S4SUF9pUajXDyQwmonBlzeUggCOjwnL2DViQnXz3KnZJNvHMAmn7I3rEsIhd9OoX7Iz4y_-czq-M6L0LLVV07GXTXmfIvFzYLml8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e6dab3e8.mp4?token=oUuRkT2OKmRq8YkYe8eNI2apYO-B-aaf0QykpZa_5gIzP-aSekoEVVXq6vPTN8yZeBJnrzyYAmjZivNsxdAy98I9G0FYNzYjM6BDBI56_PAkZczGlei91m0TuWtDH75wgEB2dqvcpvq-P0dwaexEQD_93GSktBDHfdGsuTtgtARM-H7lJHtfyZ5TdJlJz-ckYYzqKeN05d9SERZ-RxSrooVXGwomUjBUm6_IZugrCEBSR5sW5S4SUF9pUajXDyQwmonBlzeUggCOjwnL2DViQnXz3KnZJNvHMAmn7I3rEsIhd9OoX7Iz4y_-czq-M6L0LLVV07GXTXmfIvFzYLml8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد هوش مصنوعی
:
این باور وجود دارد که باید میزان قابل توجهی از خودکنترایی در این زمینه وجود داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/alonews/150117" target="_blank">📅 23:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150116">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae5795165.mp4?token=lJqmFih0wAnNPonyfQRvrlXXiIIBv7NjZpIZBkHpf5xDvznuD9XrJZNVzYqn-2HiGzxpTTJw0HF2pIu2GKKvlFxe6XEyB-oxJGSawj-FhEq2lrxMml1rfahCHLff1ZTEqMgD3FBahX4RycDx63U2hUjDzXuuL7gfEE-ZLfNqVa5_JoYl0543Kub74x8Oxrnl--rgKZ4gU-gPsMhIBpQdEyDmr-7oL7lZt0TR3ecxc7nEwKMmUGVj_bHIfRge91XeefoPW02zcGWtrfJ3dEufxjPSoUgtEE0MshCAMWGXRqfiJZ0sIIYzIYWaQMJYjGEdt1cNoWaizmGHlH-hwDEaOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae5795165.mp4?token=lJqmFih0wAnNPonyfQRvrlXXiIIBv7NjZpIZBkHpf5xDvznuD9XrJZNVzYqn-2HiGzxpTTJw0HF2pIu2GKKvlFxe6XEyB-oxJGSawj-FhEq2lrxMml1rfahCHLff1ZTEqMgD3FBahX4RycDx63U2hUjDzXuuL7gfEE-ZLfNqVa5_JoYl0543Kub74x8Oxrnl--rgKZ4gU-gPsMhIBpQdEyDmr-7oL7lZt0TR3ecxc7nEwKMmUGVj_bHIfRge91XeefoPW02zcGWtrfJ3dEufxjPSoUgtEE0MshCAMWGXRqfiJZ0sIIYzIYWaQMJYjGEdt1cNoWaizmGHlH-hwDEaOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوال خبرنگار: شما گفتید ایران نمی‌تواند سلاح هسته‌ای داشته باشد. چرا کره شمالی می‌تواند سلاح هسته‌ای داشته باشد.
🔴
ترامپ: چون تو یک رئیس‌جمهور متفاوت داری. کیم جونگ اون. او دوست من است. او ترامپ را دوست دارد. من او را دوست دارم. تا زمانی که من هستم، او خوب خواهد بود. می‌دانی چرا؟ چون به من احترام می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/150116" target="_blank">📅 23:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150115">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: طی دو روز گذشته مقادیری نفت از تنگه هرمز خارج کردیم که از میزان پیش از جنگ بیشتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/150115" target="_blank">📅 23:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150114">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28b81ca12.mp4?token=lkYQVMVZL9jyqcyf6hvKUYJvwFYqZC-OgIpDFk3WnnxLiF4rCNoepFOJnHMjmK-XwR7qS-YSZ1VcEXd1-Myn4gkFcuxKMBKLJ3fxzswKBgL_tZw9yOnzgtzD-c-On53UAb0tpGM4cVkb4w7RRAVJA4uUlFMQMgy07W4e2dhSSfvP4h9fWOelxqSJm0imsUStU5jbfXPEPv5TbyWEI3GU8C6BlHiDnG9LyDbDkGEV-RXnMujFhPG41xFgKaaIa0rUkTtz34gxYu5mfT30NugaEZAofd8En3wzCAhdhJn4cX5F9xF2TeZIbPRGmzftGkEnqrzMPrheTXwd0phPfHbMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28b81ca12.mp4?token=lkYQVMVZL9jyqcyf6hvKUYJvwFYqZC-OgIpDFk3WnnxLiF4rCNoepFOJnHMjmK-XwR7qS-YSZ1VcEXd1-Myn4gkFcuxKMBKLJ3fxzswKBgL_tZw9yOnzgtzD-c-On53UAb0tpGM4cVkb4w7RRAVJA4uUlFMQMgy07W4e2dhSSfvP4h9fWOelxqSJm0imsUStU5jbfXPEPv5TbyWEI3GU8C6BlHiDnG9LyDbDkGEV-RXnMujFhPG41xFgKaaIa0rUkTtz34gxYu5mfT30NugaEZAofd8En3wzCAhdhJn4cX5F9xF2TeZIbPRGmzftGkEnqrzMPrheTXwd0phPfHbMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: بیل گیتس می‌گوید هوش مصنوعی می‌تواند یک میلیارد انسان را بکشد؟
🔴
ترامپ: الان دیگر چنین چیزی نمی‌گوید.
🔴
خبرنگار: او یکشنبه این را گفت
🔴
ترامپ: خوب، برای من مهم نیست یکشنبه چه گفت. دیروز اصلاً چنین چیزی نگفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/150114" target="_blank">📅 23:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150113">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba82f7739.mp4?token=WQ1IxREERN1IKNUMZvGI2GytbDM7qEbJSk0v8YtLbX2aEi9QWuRxemYBShp_bG8de3p51YywGNFYQZlGi8XNOHqgC0dcMtz08e_2aydjbK-W6t_KqqH-o7ZnnggHRrsRdXH7OD2AjzN2k2DqOzqIH0g8k-ZX-4q9-8EJzb_4CupdI5oIQMK3A66Gcy_0b6eVXBHguJRt3EaxkQmzOf5RkrHuV4nEuix3snz1dx-wnNkMS-v_49CbG80MQGJyNWIE99av_K4D5VsY2TjUFJlvldljbz5j9KeTEHE-Brx3wqdIuQSjF2SmYNztE4RyH-p9nvUQIlsk1cYZc_uUCFTB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba82f7739.mp4?token=WQ1IxREERN1IKNUMZvGI2GytbDM7qEbJSk0v8YtLbX2aEi9QWuRxemYBShp_bG8de3p51YywGNFYQZlGi8XNOHqgC0dcMtz08e_2aydjbK-W6t_KqqH-o7ZnnggHRrsRdXH7OD2AjzN2k2DqOzqIH0g8k-ZX-4q9-8EJzb_4CupdI5oIQMK3A66Gcy_0b6eVXBHguJRt3EaxkQmzOf5RkrHuV4nEuix3snz1dx-wnNkMS-v_49CbG80MQGJyNWIE99av_K4D5VsY2TjUFJlvldljbz5j9KeTEHE-Brx3wqdIuQSjF2SmYNztE4RyH-p9nvUQIlsk1cYZc_uUCFTB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: وقتی عامل‌های هوش مصنوعی مرتکب جرم می‌شوند، چه کسی باید مسئول شناخته شود؟
🔴
ترامپ: اسمش AI نیست، SI است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/150113" target="_blank">📅 23:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150112">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: ایران وضعیت بسیار نامناسبی دارد، نمی‌دانم که آیا آن‌ها هنوز قصد تسلیم شدن را دارند یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/150112" target="_blank">📅 23:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150111">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPP3cWl5eO7eEbX_DGS9BJIAPKIJuOE_4hNnt6Xq8u2umWWuIYe0owFZaeMjOl-X4Pyi9_kVFMgOUaNEjXdipUxjwJRXHC5YOvS-SEs4jrHg9WecLZA5_jZOeqYYkMGzZsWDnVVpwkgQ4u6azKnIA2zsghqDXbFa34xnewPo3OJBPDmkXJLOcEikmHxZZpF2Q9QoAxP-7GbfSsgdWbJzyXxhhZD-6NPWGwIxHV-m1jeLAYKnJpYzmXdfAzo2ndtV2KEo6XkhP72kZXdRrq7mweMjqlmNZHQAiUYbIJZvLi7kiQVOTPZ-k_UnPFfS3A1yQgvPPAMRH5kJszECnVXLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارما یعنی این
‼️
🔴
طبق معمول چند سال قبل بسیجی‌ها گنده گوزی و ک... نمک بازی میکردن که زمستان سخت اروپا نزدیکه و بیایید چوب کمک کنید
🔴
حالا قراره گاز کشور تو زمستان قطع بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/150111" target="_blank">📅 23:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150110">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/150110" target="_blank">📅 23:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150109">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b186b209ea.mp4?token=nxDTT-eLcgvFKlplmKxBpAf1kMZ4ZbGuM1IRjIYCBl1--vgGeQXK9B9t4SPONn4yoEIiGwBfXJfd7-ovu7HFQKsaLZKMOlHPcQ7ruHbODiEAK2DtkxDerPF_dOP10EuZkErtHrMSKPLXUtlfOOLJh0hL7zk0rgSNQDUUIPoImjjkDusHU1IsrohKHh7cL4K6DlUq5L7JAGkvsCGAybPnK-0v0LjWFpB8sKTOSXeYe0G-hts1jDpKsRUPOXU-4-jFJpdJOElNU2aE4JlvsuJ1r4Kk-AbSOcht4c3OoRxT88v2XGK8A3yKexsrjYufc6p5njHdFQLJgfwW1a9syEMDNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b186b209ea.mp4?token=nxDTT-eLcgvFKlplmKxBpAf1kMZ4ZbGuM1IRjIYCBl1--vgGeQXK9B9t4SPONn4yoEIiGwBfXJfd7-ovu7HFQKsaLZKMOlHPcQ7ruHbODiEAK2DtkxDerPF_dOP10EuZkErtHrMSKPLXUtlfOOLJh0hL7zk0rgSNQDUUIPoImjjkDusHU1IsrohKHh7cL4K6DlUq5L7JAGkvsCGAybPnK-0v0LjWFpB8sKTOSXeYe0G-hts1jDpKsRUPOXU-4-jFJpdJOElNU2aE4JlvsuJ1r4Kk-AbSOcht4c3OoRxT88v2XGK8A3yKexsrjYufc6p5njHdFQLJgfwW1a9syEMDNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه ای 24 نیوز: «آمریکایی ها با ارزیابی نتانیاهو مبنی بر وجود نشانه‌هایی از یک حمله احتمالی علیه اسرائیل پیش از انتخابات پیش رو، هم‌نظر هستند، این ارزیابی به تهدیدات احتمالی از سوی ایران و نیابتی هایش در منطقه‌ اشاره دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/150109" target="_blank">📅 23:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150108">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IG-jWdclv4HLXvME-Fn5P7GOrvhiEwaBkoIVxhHSXGlZo6TyeObOVycTxj8B6ZRqINBUkI4Wz7XCSMqoqGiFnLhN06YailoC4zvhJ3hE6dPGyninMAriKM3RiYp3aR5-iHpntszQa_stOrzHIBvfJPRQkHZOSOJrjM2Xh0lTQSald33O7CCixXlgR42b_a25EEqFBjLUSa2G1_4x4En6BaAW2JgvPjb4fZOM5lS2VMXlSsMWfpZrUn83GWAtbMfohkB9mX4tcLB2a1EJYvlN4qSqS83wt-iIq3cVa6Zjm5S3Mc3qk0M_aPDMYm98K8AADYEj05QsM3FHMDmpY5bdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر دینار کویت از ۸۲۰ هزارتومن رد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/150108" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150107">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رسانه‌های اسرائیلی گفتن تو سفر دو روز پیش نتانیاهو به امارات نماینده‌های ۱۰کشور عربی هم حاضر بودن و در مورد ایران حرف‌های مفصلی زده شده   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/150107" target="_blank">📅 22:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150106">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
بلومبرگ: آمریکا عرضه حداکثر ۴۰ میلیون بشکه نفت خام از ذخایر راهبردی نفت خود را اعلام کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/150106" target="_blank">📅 22:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150105">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
امیرحسین ثابتی: حق اقای رسایی که واقعیات رو گفته زندان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/150105" target="_blank">📅 22:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150104">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhFN6GHgvlFZoENSX3Q1uPLDPNSKPLiY1iMtT2yGGbDnwN0pf4mI084KzCS0uSEO1sf8KKaFqPy5tmFbE-ZmezM3tgjceP712M48BikePiubznGncbhrUS4xyg_jdumTgAC-3A99rYajfGRssEP8oxq0hCZHx1_R5cv8s8NMxh123WpHTrGNrlGTnabLHY1rhcccpxWSfMfD6r4cUR2lerzPBNuW390uRxJE0XuiqZ2QrrpVz0T4VMlMWoYTTWY1ZJvOQgvnsvZkCgpPzrPXzA95krbxhkGAixQk6lryTU5xIj1p05qZITPBwXkC-SDsEqyFOpKB0Fnxk8I3UVkEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت تگزاس به ۸۹ و نفت برنت به ۱۰۲ دلار رسیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/150104" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150103">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فایننشال تایمز: میانجی‌ها به‌دنبال توافق موقت میان ایران و آمریکا
هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/150103" target="_blank">📅 22:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150102">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09ba0150e.mp4?token=WUFrHKYw3pSYCVtoulV-Hl05mfWdZkbIbS-5etRJDD9sbQnu071BWrm6rsS5L_u1zzcuPG5baTQwgNKaToUATDt8znnguAhNU_E1bnnZl9lUwYasNrRZ_-SZ7CWkBgEXkxeCUjkW8zK4CHlMZe90MORJ9k_G_b666ORJYeRudiL2KSUVI0fSHBhYnCps8VKF3lozIwsJvkjDchKjVgkR61emIbZqu6DacHzEzyIkJU5jnlgA_0c2DO-AtiCCP3DuwQ6YVyv4348KTVJZK6jB7Rxi3EF9mJJBZsf-omBdUqbsfzw_04sGiZlVavHmKSSZVT1npwiuW1Joxye8JvOozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09ba0150e.mp4?token=WUFrHKYw3pSYCVtoulV-Hl05mfWdZkbIbS-5etRJDD9sbQnu071BWrm6rsS5L_u1zzcuPG5baTQwgNKaToUATDt8znnguAhNU_E1bnnZl9lUwYasNrRZ_-SZ7CWkBgEXkxeCUjkW8zK4CHlMZe90MORJ9k_G_b666ORJYeRudiL2KSUVI0fSHBhYnCps8VKF3lozIwsJvkjDchKjVgkR61emIbZqu6DacHzEzyIkJU5jnlgA_0c2DO-AtiCCP3DuwQ6YVyv4348KTVJZK6jB7Rxi3EF9mJJBZsf-omBdUqbsfzw_04sGiZlVavHmKSSZVT1npwiuW1Joxye8JvOozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره هوش مصنوعی:
اعتقادی وجود دارد که باید میزان قابل توجهی از خودکنترایی در این زمینه وجود داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/alonews/150102" target="_blank">📅 22:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150101">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf413cd42.mp4?token=ZwRLNmHyiFUPMF6S_4NP6zBkSnji0jVPP9sqWfuwymUM5c0K7fF9KvWZvnPrZFAFdq7ITxduIc_N8W-_dx6HA0lGa7QPEp41He2Tu4jGUbAuo9CHcpg4s7x9P5GjofT-82YJboBOKDh4VvcqFCaxIAV4_s7oiuT4dlKZijNmRbC-UgFK0diMxUIjWirv3AawIDGblbvLndFa8lUhUTR6fekprtJKt1D7ohU7UDCAz47pfUROHCGkS-pI7AE-48MSJqCxXboNNSQIZcpFMNPheY1PQs2HQhKOQ3n37QfYbmSnwyEOobyZnoWbg6q0x5hpzWBbfNUpDLvPKYACkehVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf413cd42.mp4?token=ZwRLNmHyiFUPMF6S_4NP6zBkSnji0jVPP9sqWfuwymUM5c0K7fF9KvWZvnPrZFAFdq7ITxduIc_N8W-_dx6HA0lGa7QPEp41He2Tu4jGUbAuo9CHcpg4s7x9P5GjofT-82YJboBOKDh4VvcqFCaxIAV4_s7oiuT4dlKZijNmRbC-UgFK0diMxUIjWirv3AawIDGblbvLndFa8lUhUTR6fekprtJKt1D7ohU7UDCAz47pfUROHCGkS-pI7AE-48MSJqCxXboNNSQIZcpFMNPheY1PQs2HQhKOQ3n37QfYbmSnwyEOobyZnoWbg6q0x5hpzWBbfNUpDLvPKYACkehVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : شما خواهید دید که مراکز داده (data centers) بسیار محبوب خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/150101" target="_blank">📅 22:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150100">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b122f6a38c.mp4?token=HNxg2RMf66CJor4iOdJQ0EE6bY3hmZb9VYHj6uGD1bgyMgqu0JEY_KE0hIwZyaip6YBX6TBd5bkXMiwoJlopzIGlRqTjOSrD3WT2Gi-23mixfe2yw2sCcQhCcPZbAjZ6so-LMDHgHdp_5dcd7QbkVlN0a7izGwbCeYrpTAk4YOVm18jnYN3yGQbwhh7jP-Xk1NeYFEAxcKdfoWPh9Uv-82mAeFCKuM2JPKW-PUFa4_5U0YosI3lMPFoSvQU2tjMwWvsRcrCWOWvE2KHyyur8rjlOK06hEfjE-qolIN38MGOuEXxtp30rjFzPauZLzNHVg4pxyYv-GyLd2VSY_T8c-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b122f6a38c.mp4?token=HNxg2RMf66CJor4iOdJQ0EE6bY3hmZb9VYHj6uGD1bgyMgqu0JEY_KE0hIwZyaip6YBX6TBd5bkXMiwoJlopzIGlRqTjOSrD3WT2Gi-23mixfe2yw2sCcQhCcPZbAjZ6so-LMDHgHdp_5dcd7QbkVlN0a7izGwbCeYrpTAk4YOVm18jnYN3yGQbwhh7jP-Xk1NeYFEAxcKdfoWPh9Uv-82mAeFCKuM2JPKW-PUFa4_5U0YosI3lMPFoSvQU2tjMwWvsRcrCWOWvE2KHyyur8rjlOK06hEfjE-qolIN38MGOuEXxtp30rjFzPauZLzNHVg4pxyYv-GyLd2VSY_T8c-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره هوش مصنوعی:
امروز، ما یک سند را به طور رسمی امضا خواهیم کرد که طی آن، نام "هوش مصنوعی" را به "هوش فوق‌العاده" تغییر خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/150100" target="_blank">📅 22:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150099">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086c0eef0d.mp4?token=N0N9Y2vfdf6mpZ_GZfLc6VuYHHkAhCRsg54mX7XjeThRnmWmhqhTJ6yP7nHXaWcGktwA9P31-nHKOXy3rAV76PWZnfFK47MBdBldN-b3PUKsreisXAwL5mb_RloRI4goAV8nvYxT-0m1Vqav2ONiSl_YAadMaS4yydUvU8jAx_EaA-Rn2oMXHbh_8y-OIohGbUz253_3y5pyRg4Zag0vhyZryV59jQ8mIu-8QCPz-EYw9EVz2jcDwdeU847829Ua7InKk2ynw47cvFzh6P8N6GWUxatuZzgZK2Q7Txy4unyCqs3VS4l1veZ_p1cJbHtcSfSr6ixxA3XAHFEazUDWzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086c0eef0d.mp4?token=N0N9Y2vfdf6mpZ_GZfLc6VuYHHkAhCRsg54mX7XjeThRnmWmhqhTJ6yP7nHXaWcGktwA9P31-nHKOXy3rAV76PWZnfFK47MBdBldN-b3PUKsreisXAwL5mb_RloRI4goAV8nvYxT-0m1Vqav2ONiSl_YAadMaS4yydUvU8jAx_EaA-Rn2oMXHbh_8y-OIohGbUz253_3y5pyRg4Zag0vhyZryV59jQ8mIu-8QCPz-EYw9EVz2jcDwdeU847829Ua7InKk2ynw47cvFzh6P8N6GWUxatuZzgZK2Q7Txy4unyCqs3VS4l1veZ_p1cJbHtcSfSr6ixxA3XAHFEazUDWzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره هوش مصنوعی:
ما در این زمینه پیشرفت بسیار زیادی داشته‌ایم و قصد داریم این برتری را حفظ کنیم، و این یک موضوع بسیار مثبت است. این یک صنعت فوق‌العاده است.
🔴
برخی معتقدند که این صنعت از انقلاب صنعتی بزرگتر است. من نمی‌دانم که این درست است یا نه، اما به نظر می‌رسد که همه اینطور فکر می‌کنند، و ممکن است حتی بسیار بزرگتر باشد.
🔴
ما در حال حاضر پیشرو هستیم و قصد داریم این وضعیت را حفظ کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/150099" target="_blank">📅 22:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150098">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
دقایقی پیش وزارت خارجه دانمارک از تمام شهروندانش خواست از سفر به ایران خودداری کنند و از دانمارکی‌های حاضر در ایران خواست فوراً ایران را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/150098" target="_blank">📅 22:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150097">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r69TMdu6Fig14La2UVbnBsj6pQoWbWTodEwGu1t60lZsM19Iz3ELIt4m-Mi9eo2qrm4NcuIGN5CZi87EsAz7FkHHdn2Bp-V6ifYMwM0qIBHcjqZKJmQH7LyVd4CXRUBmRH4sOC6vaQ3v2v43kZ9U_zph9m5K-fmbQRwcB_VhmGHy8HbpXrXNrv8qITL3ZiviAGMdbO67lKZmDx09N_k8XtwUiwPA04fnkgQcbUMfH2B81wdj3THOPZUoCLw5-vZTo1iGCnfuqnxb--0PuOp6cDNqAotCUhNi7md2uYXgbh3GP3-xws2-hZGaAhdPD4Vou_IWBsObJQQg90aEImn0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی بعد باخت به روسیه:حاضرم تمام افتخاراتم رو بدم اما ۱دقیقه جای ملت مبعوث شده تو خیابون باشم
🔴
بازی به بازی ایشالا بهتر میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/150097" target="_blank">📅 22:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150096">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAIWUtsdRy1qZVnRFTZuJXd_9yKtKrf2L_6yTp2uPyZhHn_8seFefLdrt2WMcCP0yB9cBuRdkKReRx8n633X11UQ6gWs-gMrOVMaI4nBsYt48zKAd2GP3eTJGG7mQ5B8ZAO0xmK3N16dVv0qzxBo8ujtNuIN12n8XK3pUIqjmL-0mJXzVMqmLOE9svy-oRMl25u_R8bR4fALkP1pl6mOnDf6J6j-9OrBeIZrzhyR0n1yeiS9xYwH4tufBYmHvVu8olBnrYSqu17Pasy4OtiDMTrBEhHcfv3JpUhg0iiqbC9sp-QNJ-aXKpSmP-WCV2DWb0Bhdy9TfLNsbnH0-_dxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نجمه جمشیدی ؛ روزنامه نگار: امسال سخت ترین زمستان رو تجربه میکنیم.
🔴
گاز بسیاری از شهرا قطع میشه. به دلیل مازوت سوزی کل کشور شبیه اتاق گاز میشه و ریه ها رو داغون میکنه. خدا به داد مردم برسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/150096" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150095">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b253481a4.mp4?token=dwe4SeBDyZ0buJXRPyHYfxc0po0JaUHq1C4zWGhhnzQiIdnsij1Yn-q8ouP3xCjMWUXL9MiGB8IHm0h7KSWPzykVa5JgcwxJH1HAx1EWa8GS8Cnoe5P985QmiW9ifGIGwp-pWLz13U3L6vBeeuYe0KqpE62BinZFrhrjkTdCwO1DYBP4R7N01d3eWuO8hKNAhKCHUJrgUxaP76_3rDSdCftjjFDTf9ztYMCBaac--_PUjCzvvz8ORUjUY75-Sm1FLvzB3F2nMGr-a-21Ar3UNnNMphFipb3iY-YRdMb8WPdmUVsVSNvQglAIkZEHyf791J16hPeBI3W5XnDsKlLm3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b253481a4.mp4?token=dwe4SeBDyZ0buJXRPyHYfxc0po0JaUHq1C4zWGhhnzQiIdnsij1Yn-q8ouP3xCjMWUXL9MiGB8IHm0h7KSWPzykVa5JgcwxJH1HAx1EWa8GS8Cnoe5P985QmiW9ifGIGwp-pWLz13U3L6vBeeuYe0KqpE62BinZFrhrjkTdCwO1DYBP4R7N01d3eWuO8hKNAhKCHUJrgUxaP76_3rDSdCftjjFDTf9ztYMCBaac--_PUjCzvvz8ORUjUY75-Sm1FLvzB3F2nMGr-a-21Ar3UNnNMphFipb3iY-YRdMb8WPdmUVsVSNvQglAIkZEHyf791J16hPeBI3W5XnDsKlLm3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پی‌رز مورگان: آیا برای شما و همه افرادی که در تلاش برای رسیدن به توافقی بین ایالات متحده و ایران هستند، آسان‌تر خواهد بود اگر رئیس‌جمهور ترامپ در شبکه‌های اجتماعی کمتر فعال باشد؟
🔴
نخست‌وزیر قطر: برای ما بسیار آسان‌تر خواهد بود اگر تا زمانی که به یک راه حل برسیم، هیچ خبری در رسانه‌ها درباره این موضوع منتشر نشود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/150095" target="_blank">📅 21:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150094">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43a5034505.mp4?token=fYg9xvQODRz3GlMNj9qkXoRWsGy7wUvOOAsc6d7VRfIAcaShlnQKh8_0eHp8r8z1zwVToJIwcNVFW78NiHqSwNiyoFmAITGp03zqeD_OcJrX6xfqLJl-PSX0etaInV90Nmb14szJWZk68Fz7hhhXIwSKHmgOr4lQrDf1HiMY2TO9-jIycV1kqXxa2rZ0HkyUmOWGdWuUcO4ndVxpMCpD63M33J8ne_jAWpnTRUq5XlaPmk8RFzA_6bOvYUtAGrC3B2OSD1QoAlCBMEqiM6aAbPMIx_8Z05YuahgMBqvO5yNrkF1i8GnWTAMgzYj9wZahHyeoTME55Xc7eKJF98BSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43a5034505.mp4?token=fYg9xvQODRz3GlMNj9qkXoRWsGy7wUvOOAsc6d7VRfIAcaShlnQKh8_0eHp8r8z1zwVToJIwcNVFW78NiHqSwNiyoFmAITGp03zqeD_OcJrX6xfqLJl-PSX0etaInV90Nmb14szJWZk68Fz7hhhXIwSKHmgOr4lQrDf1HiMY2TO9-jIycV1kqXxa2rZ0HkyUmOWGdWuUcO4ndVxpMCpD63M33J8ne_jAWpnTRUq5XlaPmk8RFzA_6bOvYUtAGrC3B2OSD1QoAlCBMEqiM6aAbPMIx_8Z05YuahgMBqvO5yNrkF1i8GnWTAMgzYj9wZahHyeoTME55Xc7eKJF98BSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر قطر: اکنون، صحبت در مورد این که [ما] از اخوان‌المسلمین یا جنبش‌های داخلی آمریکا حمایت مالی می‌کنیم، کاملاً نادرست است.
🔴
چرا باید بیاییم و از گروه‌های داخل ایالات متحده حمایت مالی کنیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/150094" target="_blank">📅 21:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150093">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پزشکیان: اگر گروهی فکر کنند که تنها آنها عقل کل و تصمیم گیرنده هستند، ناخواسته باعث تضعیف کشور خواهند شد
🔴
[در خصوص لغو پروازها] ترامپ از آن سوی دنیا تهدید می‌کند و دستور می‌دهد و برخی از کشورها هم به دستور او گوش می‌دهند؛ همه کشورها به فکر منافع خود هستند
🔴
عراق، افغانستان، پاکستان، آذربایجان و دیگر کشورهای دوست و همسایه با ما کمک می‌کنند اما محاسبات خود را هم دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/150093" target="_blank">📅 21:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150092">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4148e692.mp4?token=voQYa-EQfu75IXwP-FnxTDM3xRkvAMcPnCJR_N4YhPdQ7x68t9dCb1A22slgd2KtmnrDb8s_VdCkfU50P45NYhNVku7LAl4DFPrwc5pmRggqC3IBvIGVLunH1E1Sk53xCHAqQMkso5vGi_ZOddflimrSmR4HCg0fK7eAWYaY0tMGJsjbeLj4fsv7HP2ujTlQrtnwYzxoJV6HeAHs6J12ScbPYQWtvTSErmeBWTA53F5lrees8pEWRZ4MGPeq4m0aelomPD6GKSn4YecLUE633MjRieIB8hO5xzOQyME0DBr6ChCgeqiRR2EfvXTKehp_kuxikpZKhgD2EXdZpxzDtgrNO3aDRnSGifIgUIn4ZiYPYKlytzsstmU_HYfQSUvt85AXSsuuTiDUU_WtGiSa4O808YV3UFWRjCjcUmYDWHc1ndUOnF-jXh-qm_nZYHxmd5pCYlVXU13Xp1UkYcgSG5bCJxo8cSFB_Qow4s9iQH1MzV8n1hTT0By7cxQ8ppGGDGKoYFzVLeKlEtZb7Ee38Mon9aLa-1tkImv_xXzjXGrBgZwniyo3MhZnMAwxbvx8rvu9Rx34lrmvDtb9Im5A1AygT_kmWlRwXr4lU_NrREmiXWlHrxw4AfRApIWlj7MQ12ejCZlfwnat5_It_9MpkcILDRCnRi8_0zcH4ry1BVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4148e692.mp4?token=voQYa-EQfu75IXwP-FnxTDM3xRkvAMcPnCJR_N4YhPdQ7x68t9dCb1A22slgd2KtmnrDb8s_VdCkfU50P45NYhNVku7LAl4DFPrwc5pmRggqC3IBvIGVLunH1E1Sk53xCHAqQMkso5vGi_ZOddflimrSmR4HCg0fK7eAWYaY0tMGJsjbeLj4fsv7HP2ujTlQrtnwYzxoJV6HeAHs6J12ScbPYQWtvTSErmeBWTA53F5lrees8pEWRZ4MGPeq4m0aelomPD6GKSn4YecLUE633MjRieIB8hO5xzOQyME0DBr6ChCgeqiRR2EfvXTKehp_kuxikpZKhgD2EXdZpxzDtgrNO3aDRnSGifIgUIn4ZiYPYKlytzsstmU_HYfQSUvt85AXSsuuTiDUU_WtGiSa4O808YV3UFWRjCjcUmYDWHc1ndUOnF-jXh-qm_nZYHxmd5pCYlVXU13Xp1UkYcgSG5bCJxo8cSFB_Qow4s9iQH1MzV8n1hTT0By7cxQ8ppGGDGKoYFzVLeKlEtZb7Ee38Mon9aLa-1tkImv_xXzjXGrBgZwniyo3MhZnMAwxbvx8rvu9Rx34lrmvDtb9Im5A1AygT_kmWlRwXr4lU_NrREmiXWlHrxw4AfRApIWlj7MQ12ejCZlfwnat5_It_9MpkcILDRCnRi8_0zcH4ry1BVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست وزیر قطر : ایران همسایه ما بوده و برای همیشه همسایه ما خواهد ماند. ما جایی نمی‌رویم. آن‌ها هم جایی نمی‌روند.
🔴
ما دهه‌ها رابطه بر پایه احترام متقابل با آن‌ها داشته‌ایم. همکاری‌ها به دلیل تحریم‌ها محدود بوده است، اما ما تمام تلاش خود را برای حفظ این رابطه همسایگی خوب به کار بستیم، هرچند در طول این دهه‌ها و در بسیاری از سیاست‌ها اختلافات زیادی داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/150092" target="_blank">📅 21:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150091">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
#فوری | تحریم‌های جدید آمریکا علیه ایران  وزارت خزانه‌داری آمریکا روز سه‌شنبه از اعمال تحریم‌های جدید علیه ایران خبر داد.  طبق بیانیه وزارت خزانه‌داری، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (اوفک)، ۱۰ فرد و نهاد جدید را به فهرست تحریم‌های آمریکا علیه…</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/150091" target="_blank">📅 21:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150090">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
دقایقی پیش وزارت خارجه دانمارک از تمام شهروندانش خواست از سفر به ایران خودداری کنند و از دانمارکی‌های حاضر در ایران خواست فوراً ایران را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/150090" target="_blank">📅 21:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150088">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ونس: ایرانی ها با شلیک به کشتی ها مرتکب اشتباه بزرگی شدند و توافق را نقص کردند
🔴
وقتی رویدادها را می‌بینید، با شواهد روشن و مشخصی روبه‌رو می‌شوید که فکر می‌کنم ایرانی‌ها متوجه شدند اشتباه بزرگی مرتکب شدند.
🔴
ما با آن‌ها توافق امضا کردیم و آتش‌بس داشتیم؛ قیمت انرژی نیز کاهش یافته بود و همیشه این امکان وجود داشت که اگر ایرانی‌ها رفتار مناسبی از خود نشان می‌دادند، از رابطه بهتر با ایالات متحده بهره زیادی ببرند.
🔴
اما آن‌ها رفتار مناسبی نداشتند و شروع به تیراندازی به سمت کشتی‌های تجاری کردند.
🔴
اکنون می‌دانیم که افراد زیادی در ساختار حکومت ایران وجود دارند که نمی‌خواستند چنین اتفاقی رخ دهد.
🔴
آن‌ها معتقد بودند بازگشت تندروها و آغاز دوباره حملات به کشتی‌ها اقدامی احمقانه است، اما این اتفاق افتاد و نتوانستند جلوی آن را بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/150088" target="_blank">📅 21:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150087">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f617699456.mp4?token=SzGwlsq66LhPpn0zE2hgdLvypkgSTMhaG5LH3JmhAz7cfKJ_-a4GqVuaiSAyFiGCVt6cKefAAlzzRFOAj-TjwCddlyNlIiEwF0HNMGS6v_OrE7NjpgWJL_WUYuCXeGnULkREmyXztXOYdnHWRYScm_c2vT-vESXMe2vEwrhGmn5dckpQnJ5tsI3lglT1hVc5UOWDZ0dN9MMqOc4lzWA_delY-J4fHBsxMw2CcgY5K9jh0XlVM6zuv00oHZs_vhAG_RpRga778NYREk3NV9ziXtbF519LyDY9Frgae70zxgB5cL9NcCVkdDx4yDHnJw1BXt6-fT209A0rUM-IhZiKKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f617699456.mp4?token=SzGwlsq66LhPpn0zE2hgdLvypkgSTMhaG5LH3JmhAz7cfKJ_-a4GqVuaiSAyFiGCVt6cKefAAlzzRFOAj-TjwCddlyNlIiEwF0HNMGS6v_OrE7NjpgWJL_WUYuCXeGnULkREmyXztXOYdnHWRYScm_c2vT-vESXMe2vEwrhGmn5dckpQnJ5tsI3lglT1hVc5UOWDZ0dN9MMqOc4lzWA_delY-J4fHBsxMw2CcgY5K9jh0XlVM6zuv00oHZs_vhAG_RpRga778NYREk3NV9ziXtbF519LyDY9Frgae70zxgB5cL9NcCVkdDx4yDHnJw1BXt6-fT209A0rUM-IhZiKKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از حجم مورد نیاز زیاد پول نقد برای خرید آیفون ۱۷
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/150087" target="_blank">📅 21:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150086">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizz Vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYe9LfbNj4l1gRZ5BcsWrIXVwbDxGiTbLjXK8nw2YKOB20QQqTbJ4AePo_VaqHxpGsglGlQoMTWiAxUucrezNgJImv_DTak-xgslEO2yYDmBPbVmdyMTs185Qr0P46b6_8lGYaP3wCJuegBuJqH416HB_9PUy_9AeK3-gD6gNUNRBAFCtZyNLy1QQ7fhTCGzCny9buCbR8kvgZIxlHqaIYYjXdx20e8M1q-rbAuZjMM712bJF_QQ_Dsy6J-En_2My7R6nj1HrGtp_YlgBc8auHX5oeB7WOPbnpDmw5MCRIeaH_R6a0no0sLtTaHh9wZVkxH0ypL7NmxvYthpAvcb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
دارای IP ثابت
💥
سرعت بالا و اتصال پایدار
💥
اتصال پایدار حتی در جنگ
💬
تعرفه ها
🔸
سرویس نیمه عزیز
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود نیمه عزیز
▫️
تک کاربر — 180,000 تومان
▫️
دو کاربر — 230,000 تومان
🔸
سرویس عزیز
▫️
10 گیگ — 30,000 تومان
▫️
20 گیگ — 60,000 تومان
▫️
30 گیگ — 90,000 تومان
▫️
50 گیگ — 125,000 تومان
▫️
100 گیگ — 250,000 تومان
🔹
نامحدود عزیز
هفتگی:
▫️
تک کاربر — 129,000 تومان
▫️
دو کاربر — 149,000 تومان
▫️
سه کاربر — 169,000 تومان
ماهانه:
▫️
تک کاربر — 240,000 تومان
▫️
دو کاربر — 360,000 تومان
▫️
سه کاربر — 450,000 تومان
🔸
سرویس اختصاصی
▫️
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 275,000 تومان
▫️
100 گیگ — 500,000 تومان
▫️
200 گیگ — 800,000 تومان</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/150086" target="_blank">📅 21:02 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
