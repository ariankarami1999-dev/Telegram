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
<img src="https://cdn4.telesco.pe/file/oQEi69z3ULo_fds4nRrRbpvuByIXQ9rDRbpu3m2Oe4BKb5g_7rPCjDN6aaql_y2uuOcF_8dJvI-HxezUzicOda-sPsU-C8Il3XbwWDyQ5GszK99uWSSYg_TKr_N5exytDJ85NwISRTNqAqcRIz2CWRcR_GFNSDAfmezR3JP3CHVWUHRtXWyUl5z3uKxFSQ4-LuDcHk0ZG-MfmV5ghglWRyxbFCXgrBrIIiWUCKMZcUkniYYn8-_JyM7qncouf-qj9WVfdi0vhA3blkGu16wgpfXleqi9gNUIm4gycOGL3HCX2N6FtplN0aEtu6HTPxRRDwLOpKWDJy_tip8tycqoaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 207K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 02:58:56</div>
<hr>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DkXKubrHFJaReOe9Kh1khvnPHZkhuZ6czj7YQ2DyEhdNxh0_GHmNhyEQxZxWkqaPKPoXqXqLmG9cMN7Q7liycma7w1nTsj5nK0IV60pzSE7lvhvSI8oglP1farUeV0vN2rIEgmFNGFZE5RSZWg3FG_J58989gTf3RS6hNpvTojT-_FnaZ-r8OelQmXgNsvMUsyvoehjN9Ua-9UUWLgvyWn_OLprjBzQklpFoJFHWALvPMXf1m5pdupSAjjPq5ZdiqXDTpTWEVC57_vnealmB_onS_ZY2NBFmrKofKM1D7GWZZSbdX4oUi2LTN95dmm946JokUrFj_um9uyjdaU17cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cye3988uUL2dfVzqRza6D6X0oHn478y3vtwdpo-sVpEqnKcOjhSWUS5e02yjLZ8ve9He-hfOrWe9gct_Tk-aX7_Z-hTUD9zVDJOJnviPA8Mw30cTIkUEGA8wxOQTZdhuKtHUxgDOuKwsq_VkeSPVi1daK_LT1-29nz_DKL34go3O8pgg0MAcMXPYz4QWFx0XsBuCsrNUGBKJJ3-fUc3nA7ef2HiwZSWJ-OQrHsxnyk08BlPff2UXMdrvOXC4ngzE74_179hY8e0ZJxTtyDTONxJw-4VBQzqKR3HnnTimlQGJhQY5RMLQ4NE9bZQgZpFUIQVwJ9cdE4QEAJ797aI47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=OqE4wxyC_nI-_a_PxU6GULNmA8wiRz3NAaAj31iylIW7WYnmeKZmva7UuO9CHxvmTSe5TiVmmLhXCQ9h00FtSdGf5CmnXuwdMqFjXr38qsukHTCK2HfpXaAj8pG1X6tuRHwqIyaJWAI7Qc7MVUto_NJOFxya4QFZC6Dj3SRQD4YKkAZlYuHioJ3Ns5VJesX2gnIEY_Q_aV5s-sE2rlxeTfG10I5s4C5mlrO8h9X61BePuLMCq54BG7n8ZNpaOBORSMJ9wqLsdvoBIC_o4Ep2BS7HmwNjoPlK_DNLIxYuHHTSsK4VqSwWKM5LEUHGOVVvyLX98XwWqQ6vnR07xYnkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=OqE4wxyC_nI-_a_PxU6GULNmA8wiRz3NAaAj31iylIW7WYnmeKZmva7UuO9CHxvmTSe5TiVmmLhXCQ9h00FtSdGf5CmnXuwdMqFjXr38qsukHTCK2HfpXaAj8pG1X6tuRHwqIyaJWAI7Qc7MVUto_NJOFxya4QFZC6Dj3SRQD4YKkAZlYuHioJ3Ns5VJesX2gnIEY_Q_aV5s-sE2rlxeTfG10I5s4C5mlrO8h9X61BePuLMCq54BG7n8ZNpaOBORSMJ9wqLsdvoBIC_o4Ep2BS7HmwNjoPlK_DNLIxYuHHTSsK4VqSwWKM5LEUHGOVVvyLX98XwWqQ6vnR07xYnkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSCRo-pWVyW-vF2zHNSD-pZ5LLY0SfPRkPGIdDoHzd_XLHAWCzcrD56iTxEXrmS6qLucDs5mAv6-1mljJFI-0lc_9dO3ieZKwcYdLjjFqcgyLgbTAR_VymOfBH17tvTLwuGCfAvapbqLwYOhtzwVoBRNg7SfjFQqTMPlX0UFZvF3FHMymBrrQgpQA1JSRO4vSj2clGL2tcol0gabywKlphZV8bLZkxOrvm1f8mUMeEPmTPU93lIrH70pf8V06rFCKT8okPSSDipoH3aenCANn1PmpISV3lVLAQvJKuV7lh5D9-UY69RCaC70MC90qt2PhaQChJrjyyzoaUZQlcn_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=bZvjCMaFjaIVPgv2yw-AfE25sDwRLuB3Qi89heHHV-mQqw4VmFg5PUAoMfbHgsPmON4qldfniZ20bIwCbD-MpNX2nY3KGvx67-UulUB2ZrpF-W62A0OVFr9fCbuL2aTpFHoHl-M6I-okjzb9HEs-hrQ70H2jgLX6nPkPbVqWTEy4zSGXBZ0OcBFp-p6GMuUeiaWawz1fBkV3Kkv0-dUJjYay_itlBalYWTQzeNx7bXchbYM_tvWLh4x6-VQUbXxH5FdZN-Be0Qf9eUFbtk_ASkKrvK943nFesd0MsI8_AQ6XObkSbl55ay0I9F4AZgaKUpL2wtp-ktLpbsrgWhqixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=bZvjCMaFjaIVPgv2yw-AfE25sDwRLuB3Qi89heHHV-mQqw4VmFg5PUAoMfbHgsPmON4qldfniZ20bIwCbD-MpNX2nY3KGvx67-UulUB2ZrpF-W62A0OVFr9fCbuL2aTpFHoHl-M6I-okjzb9HEs-hrQ70H2jgLX6nPkPbVqWTEy4zSGXBZ0OcBFp-p6GMuUeiaWawz1fBkV3Kkv0-dUJjYay_itlBalYWTQzeNx7bXchbYM_tvWLh4x6-VQUbXxH5FdZN-Be0Qf9eUFbtk_ASkKrvK943nFesd0MsI8_AQ6XObkSbl55ay0I9F4AZgaKUpL2wtp-ktLpbsrgWhqixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRdZ3C2LMcZykC5HWaHNP7aDcCXkyaWK0lcPz24UDW_xuhTRbwwIs6J9XzfQGYvfA328Vnpg1Iv6ZlICWYH9jiMaMhc6MeBP_vzjulLcl9RLTQLkToHEW8BvOM5fWlRZb-akWNn9U7t9FQr7nupK09XchGHrKtUFprJPKB8dj4cuGaO5RvEd07I6hFWJ2FP2Ost35lbUBTzdz1nVzOv6KQ1Ru-BQTk_UKIHQGnjr855yg2Jm1Zj1lk-tP1_qKWnpcCvwfqW0kXCo3FvHCVcuyBNwk8wjuXKCy0lTS43W0Du1u5MEd5a2AZznZkWoIYqj43_boJZmRTQ3f1ktErBNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=OVciMYBgRxDV4ZRMbgPJjUaLS-NewrrXbHjoKl34U_qk7dZjLOSRwQnVpHy_3Pqwk2E8V3tQdvteGtTXIF3qXDPlEKh9sEhjWPhlfGtP1hoyZopiYimW4SQX6nOr9md_mMW8nmPibYny0DZ6qq1hE0jySg7RYW8VSVYpDNUAhv29f_8CPfPfFHiqPQ-mIIMjc3lKfzbMiafsw5Gxq0ugCa5sYK0AGFWXGgxP85NKEQbbw3sX4e6BTzF6eTa1LkzL7C6A1yUFArABgNg6ecqet8pw0hMACGX75NLScjR8Kv9AmZrZepeuleUxuyHbVT7qxTe0CPWs9Wuoa0PzjumgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=OVciMYBgRxDV4ZRMbgPJjUaLS-NewrrXbHjoKl34U_qk7dZjLOSRwQnVpHy_3Pqwk2E8V3tQdvteGtTXIF3qXDPlEKh9sEhjWPhlfGtP1hoyZopiYimW4SQX6nOr9md_mMW8nmPibYny0DZ6qq1hE0jySg7RYW8VSVYpDNUAhv29f_8CPfPfFHiqPQ-mIIMjc3lKfzbMiafsw5Gxq0ugCa5sYK0AGFWXGgxP85NKEQbbw3sX4e6BTzF6eTa1LkzL7C6A1yUFArABgNg6ecqet8pw0hMACGX75NLScjR8Kv9AmZrZepeuleUxuyHbVT7qxTe0CPWs9Wuoa0PzjumgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUgp3gUXf-7xI5PTHhARzhLiTKZX5FNvRh4SKM8mLsW_6g4cTgFhdu15KX9cDaj7j0Rx8_aTgbZ6Lbych-TMBOmCwusy8jtx4MZnm8JOEho1ysUh6ntewxR7XRi1n-ZZW8QPGxpCIHI7qMUUV1UGJFpEWM_WQYm462GLNcFZid4ww9xNBwEmjF3gdnOQaQ6222w32sQvl2AUpaYac6lbdOw-vd-SzxL8sgTnCBfcecMVZvwa8QNHEmUGnPA0qX11g4kM2vNnHLVyYZIIptys4vLSZ4oKotYogsiK8pBv6UWe8WXwCkiMwPXzrPfjM_RLhjF4rKTfhTNcoRh2RQ4Syw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=NH_m0iuoBroQiYX9G1HJ1tC24zwK7U11M4wb0J6-6hLSD1ODEH2OAdC2_dCvbiT9wZn0byB7hY8WRCpjzvZ3cIdQeazV-Se7wGE0Z-F3hlz3i5TU6h64UYIc-SAh1bERfrPBWIaPTX08ueibW6LRaax8-cM1UUb3idrNQ2akuwTeJ2cB_QxAKVWoI-OF70x82lDcUjRw2UeXo9Upcv2RBg6VyQirQAtSnq7XRJ1a6zo3FU7Pm_5tzZlg-DXcGd1t4EzXNtMWSB6AGSO41Fc7Krq5ukOLenUtIuYL67dl7sRPm8mfZrTdFqIY1pImDvJfzpmBJr6PPdIXVWNFJftEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=NH_m0iuoBroQiYX9G1HJ1tC24zwK7U11M4wb0J6-6hLSD1ODEH2OAdC2_dCvbiT9wZn0byB7hY8WRCpjzvZ3cIdQeazV-Se7wGE0Z-F3hlz3i5TU6h64UYIc-SAh1bERfrPBWIaPTX08ueibW6LRaax8-cM1UUb3idrNQ2akuwTeJ2cB_QxAKVWoI-OF70x82lDcUjRw2UeXo9Upcv2RBg6VyQirQAtSnq7XRJ1a6zo3FU7Pm_5tzZlg-DXcGd1t4EzXNtMWSB6AGSO41Fc7Krq5ukOLenUtIuYL67dl7sRPm8mfZrTdFqIY1pImDvJfzpmBJr6PPdIXVWNFJftEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=WQFf7RYG1UZEj-LlfxKA7qahWXULju7ed34A4pF8Nh7Bzj7ouOdtLS0BpfK7bQJ7t5w_Q38YDPzy6UFKaGbuR--peyE-BNvMLVRm-FUH64byqox-8ZM3M1Mb8A3xz9VWaNozJNdwE7C-KOUgefYHK6zpw0oBNSXNEkoPMJbulIBAaOtre_uejOAwNjkPM-_eseRh4UchJQxc79cieFAjV8d57w_lcQ29NJsGnD66m9uB-spumn3a8-iY1DRJ-9IY023SGczR2q9ytFym7umobl-ACrcaGlM6uMd613Qm1IK5ZrsHtQ3XWTt3Gfa2pQezJtzRtqvU9QAa7UCFiKz1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=WQFf7RYG1UZEj-LlfxKA7qahWXULju7ed34A4pF8Nh7Bzj7ouOdtLS0BpfK7bQJ7t5w_Q38YDPzy6UFKaGbuR--peyE-BNvMLVRm-FUH64byqox-8ZM3M1Mb8A3xz9VWaNozJNdwE7C-KOUgefYHK6zpw0oBNSXNEkoPMJbulIBAaOtre_uejOAwNjkPM-_eseRh4UchJQxc79cieFAjV8d57w_lcQ29NJsGnD66m9uB-spumn3a8-iY1DRJ-9IY023SGczR2q9ytFym7umobl-ACrcaGlM6uMd613Qm1IK5ZrsHtQ3XWTt3Gfa2pQezJtzRtqvU9QAa7UCFiKz1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDWy4pzi4Ip5XV7vgElrgnwJbFAvfcRovbKXFsMQfktjsbJuyxWNIM0YGwif7vrTGD8XeZ0Lgs1XNBVnzhWoPCqYNe4bhEkCMaSXBCG2egIIuV9Qdu-zzyQtI34Dj0uB7ysJNMUh2WG9F3GqGuKBpUeN4zkhnzeEah0001WFsCCEmhzRB3o4Bl2f4IJP53cIUfdbDWplPPLBh7lFI5Hx78kG_ZmL74E4sYJLgdPkNUlSdj9b9ipL6bP-tqdxQsXmFkIbNThqJMk9qX0B1u0y6OQ6_E7vjFvPgp4ZgeaL5xCinMANTVihO4gWYID1uGY40Pvox5mpHlKyaeHiWZa2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm6tcfojvOdGL_83bYjDUh7y0BWt3V52alrsqGSuAkPjNP9PRg55kdIqlJerYybGLl5NlTwljMKzF4EOQqdVPImA_MkBeLJf_XuegOHnA_VUrfn5wHFCqkGpv9_RwY7QflTfGJNQemMhqwMVdcFcilBOfa_m-P3fQ2pQtD9ipD-YU0y5UHpjthTMXGjPNRel19UHSU10RLHiJC9hAXAy1azkF4j3Lp5dUFsi8t46n9iSzKcpqrUQBAI5ctWP1JZTxipjpLKyIn1qdR2e4Lwf4dAD_bDfZHoHdoUwZJ7rg5FZ3FfVdxlSzjUbiC9KKHhneqdI-1eCR0YiHlwKLDsAkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-x9-aOaeoV_adeiI6vJbRO5RJJ23JGEbe2axdaJK8uqYooCOtcZfu_YI3nTjT_HCpf8cOn7xYGzfZjLrAiERUYERtJZnhFZgabzbnZm0NWPtIfFiqI9BAWmOaonuOfrc4_p6IpnCrEEGsnlQ2oetS7oRLdEFOPWOltgIlLS8y5u8ZmfTUtqaPo4O5hOZlpf43VeqspUjE8OwLIoUDlM5qy50px87s86x5Gdpbj161rxrXKk-Re0Q76Mq7OMu1h2xno3M4QWo7p-3EQKQhvz_YVC70MlI14_8fI5Jb9-_Iz6Vnr0-b7VvBcZtaBvrx-b7yz5zcgH5oZvO2e3j1B-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=GxHoaPVxkwVCFTpbW6WbZY_jyyEebY4SZX7F4ea_CjjFKuk0FRy0Of6noOy8ms9w0KTXOSzzHFV4k9vzcY5I1AFrD3nF_A5mQN9Brnxna5665Tt3ZX4AYuo-b5unTBxyeCLNvFiduFgGSVYDMkM9z5ahwF3s5KEa0AXQa3fzQeZ8p3w9Mx81ikerernX4BS83i4RsEtKyj4TPEcuyTgo12AOIa05uwhrb2nDblebB-ucFTW9-trUhyUhpEMwmGwDfDCsZA5NiHQl1fQh5jLr-cwCJQKHEHxHTY9B3JAhlWoR_wQ_dGXHv9Fu7kzTtG3qwoOKj100Df1PXhmkO50CiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=GxHoaPVxkwVCFTpbW6WbZY_jyyEebY4SZX7F4ea_CjjFKuk0FRy0Of6noOy8ms9w0KTXOSzzHFV4k9vzcY5I1AFrD3nF_A5mQN9Brnxna5665Tt3ZX4AYuo-b5unTBxyeCLNvFiduFgGSVYDMkM9z5ahwF3s5KEa0AXQa3fzQeZ8p3w9Mx81ikerernX4BS83i4RsEtKyj4TPEcuyTgo12AOIa05uwhrb2nDblebB-ucFTW9-trUhyUhpEMwmGwDfDCsZA5NiHQl1fQh5jLr-cwCJQKHEHxHTY9B3JAhlWoR_wQ_dGXHv9Fu7kzTtG3qwoOKj100Df1PXhmkO50CiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=vBNJseh73LA_AoupbqKPBCW44o65Xge_mxcIuLOH_ZtWpnsx3zE7MusDdNnKmAISHRyqtYeKgeaWnuvy5DbFaBTw0KSd1tanYZihjlK-DfkT0TfMaLdYKBR411fzV0Qlf7KKM5yNi8Frf-GeeC_p2LNYBFl7vEsLojQcDaZNO7lCn5NGLb6SbEhJBK2bsZLEH6CEn-gROCOyTUEwKJhQycp3jVrPoR0PsjLTFuqXDzAEpoD1txA8HTWHbcOnG_z08r90gVVxW-GLB1RTr-PRxbutaa1Mg2tiJMHPIXIjt_nRzR5GoMxd1TJb6VfGUm89Mda_US8dJHt70rUNUxmgwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=vBNJseh73LA_AoupbqKPBCW44o65Xge_mxcIuLOH_ZtWpnsx3zE7MusDdNnKmAISHRyqtYeKgeaWnuvy5DbFaBTw0KSd1tanYZihjlK-DfkT0TfMaLdYKBR411fzV0Qlf7KKM5yNi8Frf-GeeC_p2LNYBFl7vEsLojQcDaZNO7lCn5NGLb6SbEhJBK2bsZLEH6CEn-gROCOyTUEwKJhQycp3jVrPoR0PsjLTFuqXDzAEpoD1txA8HTWHbcOnG_z08r90gVVxW-GLB1RTr-PRxbutaa1Mg2tiJMHPIXIjt_nRzR5GoMxd1TJb6VfGUm89Mda_US8dJHt70rUNUxmgwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGyidfyl8IRbkqaAq1M9__Vaze3zlalljbwjKSwbppvPFGqddS6JjaZ1TY_wT7PNKBgb-Q4e7w2K66b1oXFfSLgQbrr6QfS43jg2zI4VQ9HCAxg8DgfHJF2o_Up9o145RpH1ma2lTF1OJs4GvBz7X_yLQf6PgoCiAHk1LEoHeK6zKfyJf67VLRZqDsYgWECdydR24lV3LZP2gUpU7ICU5h0fdl4xxGNUKAcZHLfSsxVdMRG5PILfWKDS0lSINB1sJp5mxiR8LuCClVDpp2IyEHwv15ssQO5srQ9BPvUPfloUicDo5_jWQDd6h2xmJVts5HMw1JbAaiCcUb7gE4GKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBe-n5-XJ7eEpm0cKUvwMvRDINe0BD0DiaVO7qXAVtU5JQPnjMF55kSoTeCVG9B40ZK4LngQK48YBQWpnLEsAUKkGYuyHye48OSgGANvIw9lgpROv11qeyhRGsPgTJLyOxcHl2sTkiPvFYEN3-cUoOrnoCq5TGnirMcRL5R0Aj-gy_w6HZpP3YHQGCJrNduyUIJja5tERIkAQMOZEXEm19z92boLeb01KtYkkMn7FU9lwfLD0vylaWHc0Ej6Y9OvQk9d8-4XXlu5rSZd2VYiMzPcdau-3CkPRVpNSz3rKESct80om2jiL3JoHznzBH6CXrRlkynmMyHkL5rFGoCUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtatJ_urYgV3jA8hrmHntL4B3BGxS4j3kxrrRZP2pcikItiOkE7JHvsLJUhoSq7miSz7FB-_4lmxJPz7GwTajk8sICAm0LX8NW0yqXD2vN0H0O22LwHolNw8xT8wb8lDyw1DVOmhgp5cXD-mTXYWGKC1F5gmDR9y7AQAK6KoUv_LV8sy5-2YJmvXlpouQJmWQXV9xxhIpFpVutdSo9C8W7hJ6ZBJtQ35lcp6tHDwttMqsPo6IN8F9MjeeXBumo6JEopmStVMPHGZmhXeKqyl7YSr57x7w-oeEPIEJ2AKKbVpfREM7LH17c38A0KtBu0JE8_NTGqWPHe9CRMJXU8iAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=hEKJOVbL21PwDFs6d7tUNqjn_M9DJnPfKXeWsP5kxFuuYGwVK1cBKDv7edeAnPNzqEKDaWkvWYbyHc8wKr1cdtZVrLi9VHZH1IJaz5z9mkDorPMkwGOIQnUjMr6X6SlYN83kCAzIASfMXS9YpNahTgqYx5Cn1Dxs-Fz4-FTalayvxDJ1Afx518iZi1nDRVM2KxpnZV74qFaEj0g8_-C1GCmlU5cxPbV1dNt-Gwq8v69sxLDiSCkmDfc4t6vJ7ox2_C47dXXCAKdWwsSja7ddDIBGRjUGI9A8KiATVHGpb-nokmoj-Pg1B_YYzdo-okBTLwr8pfuYgvahFt9q0Zb2IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=hEKJOVbL21PwDFs6d7tUNqjn_M9DJnPfKXeWsP5kxFuuYGwVK1cBKDv7edeAnPNzqEKDaWkvWYbyHc8wKr1cdtZVrLi9VHZH1IJaz5z9mkDorPMkwGOIQnUjMr6X6SlYN83kCAzIASfMXS9YpNahTgqYx5Cn1Dxs-Fz4-FTalayvxDJ1Afx518iZi1nDRVM2KxpnZV74qFaEj0g8_-C1GCmlU5cxPbV1dNt-Gwq8v69sxLDiSCkmDfc4t6vJ7ox2_C47dXXCAKdWwsSja7ddDIBGRjUGI9A8KiATVHGpb-nokmoj-Pg1B_YYzdo-okBTLwr8pfuYgvahFt9q0Zb2IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=skOSn-tWWmHXJ0sO8P_8N9rixAMhHCaYwtI904RAQmp-2YpZJsIbEWKSLY2eNdgQn7XiiJIuG8MOUJVl5FGvZT2CYg8-7YcHAMvPvYuDMLE6qMsH6uACmVflSa50fBMXQwnXoKxN2xwjyz_0a_dO392K-sSrOhp6Pgyl4yyqfA3Gbevfrd5-_GRef0IdcUWyPY3QpYemUNXcb4icjmvzMDUrjIqiP5dS7PzVLTXX_yXFpsHXNbyQ1KT4KK4t8Hk7p7ubnImyVVCCd4XeR-LrfbtB4wZFtYKC-NK5RH88pY7npy6j2DjIQOaxXi9OYfkP8d79VGF5Ywc-JvomQpVQXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=skOSn-tWWmHXJ0sO8P_8N9rixAMhHCaYwtI904RAQmp-2YpZJsIbEWKSLY2eNdgQn7XiiJIuG8MOUJVl5FGvZT2CYg8-7YcHAMvPvYuDMLE6qMsH6uACmVflSa50fBMXQwnXoKxN2xwjyz_0a_dO392K-sSrOhp6Pgyl4yyqfA3Gbevfrd5-_GRef0IdcUWyPY3QpYemUNXcb4icjmvzMDUrjIqiP5dS7PzVLTXX_yXFpsHXNbyQ1KT4KK4t8Hk7p7ubnImyVVCCd4XeR-LrfbtB4wZFtYKC-NK5RH88pY7npy6j2DjIQOaxXi9OYfkP8d79VGF5Ywc-JvomQpVQXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsPdrGEjmyOKWd96Aplg8sjHrVbRbtZrvSPyZWGDHUgjSu6jyaZxlify11U1FpRHUP2fWpNTKP3ZntjAqbPg6GbffBuxbjZYlns36bvIIFYCfhzYCpM0rHiI2M1vJrW8x5m7dUCcaM3mKObw5tqYJGEyhZKzGgu5TOjM3BfywMWm21A4G_-merJwjPo-qLfsxmBXwgvfG8Gv6c0BnLZ7FiOoBwyBDqe-tghPjlxt2W7Dy9hU_n6je23pr6WsaCvsDGqIxmOc1OWqwxuQNevNsgA6ZnG9HbgqrEuPmJw5d5ion6FcrhmCE2SXBFwJBc7zQ9S59bfssceuoijH5y2pFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=vLr8niEG6qpUOjhBAqnDXizCP635RyOOjohI8CoRj2Smlk_MLeNpRNTgrn20uHIDawj6XZ1S16AZt9PtW3spIKs6XJpqOjWGA9D23Py7n2Cqw9sQKEdBpExT_PhiG6totKKfuzas3s-HrwRjgF6qVkhAB8Tim4heg67SCf4KzzVC01Y0FQQhK05pzlG-AXZKGw1xEzFn94ww3yDzA1g5oewjWstX62Cdz3mrMuKTPD6DGUt7Orh5bwcUaiVcsGESE71sb4UOcb9zEL2mOBYuZYlBrO1CPIeNfiG2U-MeLhc8K3YuQURYds6yWh-Z3DqX17ncBinBbkf-auHbt1Z2_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=vLr8niEG6qpUOjhBAqnDXizCP635RyOOjohI8CoRj2Smlk_MLeNpRNTgrn20uHIDawj6XZ1S16AZt9PtW3spIKs6XJpqOjWGA9D23Py7n2Cqw9sQKEdBpExT_PhiG6totKKfuzas3s-HrwRjgF6qVkhAB8Tim4heg67SCf4KzzVC01Y0FQQhK05pzlG-AXZKGw1xEzFn94ww3yDzA1g5oewjWstX62Cdz3mrMuKTPD6DGUt7Orh5bwcUaiVcsGESE71sb4UOcb9zEL2mOBYuZYlBrO1CPIeNfiG2U-MeLhc8K3YuQURYds6yWh-Z3DqX17ncBinBbkf-auHbt1Z2_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=XVItqT-jl6BCteat_w1XiSTD09r0hRwfp2sNOiiS0aZRmMZIkjVDKEslS-TBPp5ZNFOlwGm63a7ts-hcEFBmbGTY89Rqz6DnDWUnRrLOmVXrobpVAhzTdF2ghAkNNxIDYm92rIBS_MFTd0s66nu5XTiPAcTBiJUWvoIKBCbHQ_uyOf5i6NVs2qqAhLJQBA-9wDVyZEkctOBlAgLCmXDX7_F0ooTNea0vO8jtCZGWHXD_jvqGxMxtJ2YWdooM_BpZtGTmyWX8jWpplzrHT8ltbdsFCnw4DbNhOCR36tUwKt7HZzat0kT07GQE8B27VWG_z2_Bc0YYCvGOI3zUUviP1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=XVItqT-jl6BCteat_w1XiSTD09r0hRwfp2sNOiiS0aZRmMZIkjVDKEslS-TBPp5ZNFOlwGm63a7ts-hcEFBmbGTY89Rqz6DnDWUnRrLOmVXrobpVAhzTdF2ghAkNNxIDYm92rIBS_MFTd0s66nu5XTiPAcTBiJUWvoIKBCbHQ_uyOf5i6NVs2qqAhLJQBA-9wDVyZEkctOBlAgLCmXDX7_F0ooTNea0vO8jtCZGWHXD_jvqGxMxtJ2YWdooM_BpZtGTmyWX8jWpplzrHT8ltbdsFCnw4DbNhOCR36tUwKt7HZzat0kT07GQE8B27VWG_z2_Bc0YYCvGOI3zUUviP1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWRB3OtzT9AM5Q3eBAbRIiG7lMdXb52gf3L4MbK5g882juM_l8LQANeF0sSiL92UBqVb6kexC0ew7lCQtqEpNmy-N_COnH9dloJOtcGJcJeY1e9-bd9_NVEikRo6OtZcDiym5Un1kJ9t4-v4Ytfp1HoDYPTCBXsAl5vFJ53IAM2nKODbe1ctGYi3PjDiV2ywT4nOehp6I1yVJwNYz2a_ztaHBeVdqNuhQYxsZmXyttxB9Ob65D8fwKtfRVK3IpteNTmB64lOwd3vhM0j7UUtbRc3haRwumhGTNTJECfb-j1GeARhpQatk2Sw_vlhdAkKB9irS6Ywp5o94LrZN6vhng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw8RB9iCsXTdD-lRCyTu2YOosoccgmv-DRBQPi4xYrDAf13z0LMxba6o-J-fUDO7-oebKFuwY8u2un8QeG1XGUGujkd7PCDhxmKbHFuvPGNbxvhoIhIbmNPc3e1bCzlvaDWWKUIpsERAlk3OwvTYgBe24YGgqfZTdyJ3vi3R_q9tmJh7cuUDW__C_FIsYty3jqGpVkBAqDLmLV-j3jhvwjVw-rySIb3h4l4-D5xK6TpQPEBmzDIhyBKpiUtiYWpQwuIwHkWMuewbueoIMjKfUeYyEuGD6eswAjEus5e8YFwIOjjZkZUTTJohxEfc0jKg-3yx5dskhwfYv0_zIpcA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FolDcmo31l4qbBPGMGvJc35-Pl3b1pqIn5n62It4dZgrTjMZdiZinPkoVMQNnoEpssPL5fyGrr2AdMILFYsdI_m4Nj_ilSAq9aO-cdpdf910DM3PV42OchYQhZp4udQOWFJJoTrd3A-w9M3IprODtQ_X2Pdq0dFDU_ds6cIhzWSmou4Sc-_4y0pT_6HWV-38_zwJ8cB6QCOfjTZVqhMtwu2W3RAJSpMqf_ZGnbVls1A31InOUdIqpcF2SgakCxbVJMjbEM6jT0pJemkc2zvv62GvdEVwkuqS4W9A5GGj8Vq4jo_555hRj3maFkEVaqbxt8nSW4yQmq822INrBuf_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyIGoPC9gJveeBTm7AXnrlF7IDbTvdyIZYv8ZrsVUb58HURMiMAX8uBBhN2ZSpAj2hGUXNn9lOP6rRNwddfBqLIut4Cx5NQLUeaH7EfkFDaOqNg1uESeyQf8I4vHH1yP4TO5-URFKqe5JzwgYZVaEV0diCpYW7rIK-RAzQP3A6TJlBahyUOdS6D0h04pJ8Gxdbz0-aDdc-7-3r-aN9-IP_JdCiHYUR6xieKTZT7liqOXXc5Zzj0ivRvV_gu-zuwicAXc4x6kcqb7ePMiNVyfgXAx9CXTLu42ciLzijM9BGPFXkkMvKDZkVnnE-u4SXdfFWyDcIjfKDa4g8EAOsMSDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=KmocJ68soMHmyMbeucOr2yuq3_M-9NVD7rxD6ttJNnVnRebqgtMrs9__tot9eaiZEoVbVRoZFKO17E7JzrNHIh83FzT5jVXk4t0MR4ZBYf5o85raoxkBVLI-zdn55krG97YsYVR30XtI2ummUK6-9e_cJQZ0hRllsdtquPhXN5LB6caCq3x9-NOs7UpjRvwZgkZR_WDnoili-77eI5ezxYAi3cpdO9QyOk8mzFV-iXfPSflwcByCT0YZN99aaiaB_Ba1ILAxYiOG5MrPKa_5T5ahTjzcRHwwDqrFPPO-i6vbdpAWmd2vfd092w6Gbem6QVumPQyyPzjHDQQSlW_QIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=KmocJ68soMHmyMbeucOr2yuq3_M-9NVD7rxD6ttJNnVnRebqgtMrs9__tot9eaiZEoVbVRoZFKO17E7JzrNHIh83FzT5jVXk4t0MR4ZBYf5o85raoxkBVLI-zdn55krG97YsYVR30XtI2ummUK6-9e_cJQZ0hRllsdtquPhXN5LB6caCq3x9-NOs7UpjRvwZgkZR_WDnoili-77eI5ezxYAi3cpdO9QyOk8mzFV-iXfPSflwcByCT0YZN99aaiaB_Ba1ILAxYiOG5MrPKa_5T5ahTjzcRHwwDqrFPPO-i6vbdpAWmd2vfd092w6Gbem6QVumPQyyPzjHDQQSlW_QIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahJzFfwkXm3Z4zawoyPRoOXOf14k_NrbMi2V9Y4jV-lEihETmjZeGvQUmrgb-bC7fkrrZ0efDSr16OgKWMcfaL6JH1Hzb7Q5H9_1mstDnZP_Nu7eiRC0IJ5hCRpZdm2bqw6XQn0PXE5OEyB_sM72MiEgKcCRKcJ7U5z4-yvmFZioL_4r8IHyO1J1vu-EoTzZDN6h63xcZuCy_t0vUTPE3mfpdB7jh-9MUStr9rE_XoitSR2isFhiK49i8B8RRXpD2i39U-sVz1V2dfM-wAW9A8ZaR4IdmnnEPFfo4szSor929IFsgmKPxvCcuKTXk0arXt78QoqZ2GCFHJINl_-4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq2SBNjVnUXVtCA1jpvGEf1IBpcJyUIYXr-AKM1nPoLQF8XOasZV-n_wz0qrLDBB8QzqgmyBXuKml8V7DItUUq2iZe3Af-68QhYkf8CBzb8X8xEPuumO1Qlrf5KdmNBRyf5ukVVcQz7qFdZxMiMMyRuiyAWbuteV2fqF2hrq2olDdHwdtnieOCdeNpk_a21ftpVmLb1Ek1_SJ6BYFpHDF-QiC_PqPzFWRiTDYoiyMyGf7LaHEqtumegR6c0zToU1N4S9QqRjnV5zbEYYGJglu43e-1FZyS-J7gGNM4m3LyEiuNfDxyt2FqgZKIh8OakAq8LH_V7zesDPWeLVJTVH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM9l4waTqq4YDHLby1QDUxmAnLqgmlKDoNaUDOhFuJBbzHv1dDNNFo4u7uaosMpR5J4l7pplVqt_hjfUDWuM5Rqnw_KcnAXo-GrOocP4VO2dAXUm9wns2-xLS3nxS9GfIngUj9he-uyT3QYiECQNoa0EXEWGZilOFfQe-IyVzkoI6yFXoSbXdjv0RmfVQoGewDhiU16MuAi8WFQIqfbe4SLHZg1Xn87AqBBI7qwv9WUvXWeu9PLkIc8qOPPklj4nfCoimDKz90BUZvYZYLZH_soOtwnDLjK2Aw15peO5vidE5CATDI8TiIw3EgiJc08tIBc8ztcEGCgqzAPGjTnnAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=PMOAb682ewFTMgclSJ8NUN4FstVVgVWZDNvBuU8qtXlIk44GJhHYy_oMo7pqeZTRR12CbV6_p92gSR681bLWkHme5zNaeNLfSC26-6V4R-u6IhABHQDKuPSCIdNVdjBf8_haQiXgNHexNq4WJsOPd6OBFgv7fYm6m52UQaiV_NCTSCGnP47VCkfSu5H1a2rboUIXOip-M6YT36BQPcyrk3_9df-WD8V0_nchpC3uKjTqT6mxjRWv40GGJcE5-4KshsvtGrMljSC7IThNnxTA6azMHajxxuiqhqoI4PtcVz-bon8lL-leuSOiji3xyOpoQkZBRGOywAO_9pgI63xThg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=PMOAb682ewFTMgclSJ8NUN4FstVVgVWZDNvBuU8qtXlIk44GJhHYy_oMo7pqeZTRR12CbV6_p92gSR681bLWkHme5zNaeNLfSC26-6V4R-u6IhABHQDKuPSCIdNVdjBf8_haQiXgNHexNq4WJsOPd6OBFgv7fYm6m52UQaiV_NCTSCGnP47VCkfSu5H1a2rboUIXOip-M6YT36BQPcyrk3_9df-WD8V0_nchpC3uKjTqT6mxjRWv40GGJcE5-4KshsvtGrMljSC7IThNnxTA6azMHajxxuiqhqoI4PtcVz-bon8lL-leuSOiji3xyOpoQkZBRGOywAO_9pgI63xThg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2TZweqjwq3VoPPU77fisd7o1V0R89E-dhdPwTVBIjrVQMHheae1Wqu0Dm3VkHcqoCI3vXSbxGLmJRzVD3sjaO-BNS9_B2duCO0eA684hLV7dlfMrMUZywiavw5KsZXsVgrBXsVySahk_P2rTRUcOMQ5cqhaBe50QSuhAvKuQT1ULvj67v83P4BfsKDBkk-QQvXCRjc3g9JfDHpBE8ckLf3z0dd1xomDC1vLkXcsSJzvk28vkGEqXMXNemg0hagKoYwI7SJP6tk0KMgGYvPeVTjQYcYBud1D3XUxGGea2H614egCMGPNG1NB2DmXMvqx-Xjc1Y220G6ZVakAIMXeoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=OSZHbtEc0plPkG10iTzvUHd9BF-7hO2eDeTwv2JnwfAH9rPaSbFFn664WTMjAWiAvY_YG4fV3GNDuzqdhzZtdWIhgrs9wNXX-fPBL7OyFrfq3FGr_k6LKYDNsgRCKD5D7CeiX2_89GHr2OsJOmxyGau-IEqSogWv3fKe8uRypb8AKs9qG0tz_dCxvlZ695GYqvB3gizRfVL9HWLz9dIHGP3PdsEo5OtlomNRVB-SJw-deYALO41kKpyVEI8PzmssNQwF8V_cfR-hBdX26BAxW21gka4NKh0j9iGLzJqledZD8kS9EhpZgtYw4KJB408L7TBIH6H2lwK6fBQGKSqR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=OSZHbtEc0plPkG10iTzvUHd9BF-7hO2eDeTwv2JnwfAH9rPaSbFFn664WTMjAWiAvY_YG4fV3GNDuzqdhzZtdWIhgrs9wNXX-fPBL7OyFrfq3FGr_k6LKYDNsgRCKD5D7CeiX2_89GHr2OsJOmxyGau-IEqSogWv3fKe8uRypb8AKs9qG0tz_dCxvlZ695GYqvB3gizRfVL9HWLz9dIHGP3PdsEo5OtlomNRVB-SJw-deYALO41kKpyVEI8PzmssNQwF8V_cfR-hBdX26BAxW21gka4NKh0j9iGLzJqledZD8kS9EhpZgtYw4KJB408L7TBIH6H2lwK6fBQGKSqR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=E2nuGh5pjT3DTh6vkFgr2IfhZJLKpgtE70qXPB-040liuK-ANHRFwZrPwR9Fs_OdgNFkw5biyIxsmI_qQsmnZH60oLNVNaIdBdEA5ASszvzi-wYPWjPg6jeHAB0gru_nTR8EM1lb8afjWC1jYL2xupV1bhvehA396Kpv6Pjar-hX45kQndJOjATgeyAI-h9PxB0g6MpMRrTE7LV3wlGDkuMaIidBTadXzEFJl5s5N08ehnz8rZRzYlADIhw9LDVnWqCtQTpQ2Fz5UKUHeIOCueZpRWG2T_JBcn50BkwOkJVEPzQNkV-G0G5UcXzlb3SKt49T9PBvksKuvGT16UeGEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=E2nuGh5pjT3DTh6vkFgr2IfhZJLKpgtE70qXPB-040liuK-ANHRFwZrPwR9Fs_OdgNFkw5biyIxsmI_qQsmnZH60oLNVNaIdBdEA5ASszvzi-wYPWjPg6jeHAB0gru_nTR8EM1lb8afjWC1jYL2xupV1bhvehA396Kpv6Pjar-hX45kQndJOjATgeyAI-h9PxB0g6MpMRrTE7LV3wlGDkuMaIidBTadXzEFJl5s5N08ehnz8rZRzYlADIhw9LDVnWqCtQTpQ2Fz5UKUHeIOCueZpRWG2T_JBcn50BkwOkJVEPzQNkV-G0G5UcXzlb3SKt49T9PBvksKuvGT16UeGEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=S5YJmKl8dyuBQoBzGaHbil0tEg_PGWa5PJSf5vdSPB7i0vQSX78qgIKRg-4JVw5ZLqtH4ObngaR6opTggMcONMeiF63qir4xZOHOlBLO18koPIcxwZqETABGtcIIDkjRGlVKyJZcC8h2EUCCsKrZPp8zAh8-mWiGHM78arhGmH2ZIfDlhq-dl6p_3fi1NFSGZuGJbxLKmz8ftNofr83sLMZhVJsccJsNs26dEFWfrR5RgqsASG-QjCFsHj1nOv2bgsqZXC6qB6FW1H5KLCi0NWB5Bg1c8pvuhnBm2pBFC8qQS9ktwCY0xX-gfrUY4S68GoiWGSpk-SqWKpWheiQi9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=S5YJmKl8dyuBQoBzGaHbil0tEg_PGWa5PJSf5vdSPB7i0vQSX78qgIKRg-4JVw5ZLqtH4ObngaR6opTggMcONMeiF63qir4xZOHOlBLO18koPIcxwZqETABGtcIIDkjRGlVKyJZcC8h2EUCCsKrZPp8zAh8-mWiGHM78arhGmH2ZIfDlhq-dl6p_3fi1NFSGZuGJbxLKmz8ftNofr83sLMZhVJsccJsNs26dEFWfrR5RgqsASG-QjCFsHj1nOv2bgsqZXC6qB6FW1H5KLCi0NWB5Bg1c8pvuhnBm2pBFC8qQS9ktwCY0xX-gfrUY4S68GoiWGSpk-SqWKpWheiQi9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=A6zGyVwLGZqc6iyqWEVqts7qURVoox5diVMObMNJdnzOlWItRyfMiFG0b_rmAqK95VS3cuxebZYnX93oRDAxG1qLKO9al5He48OxfdX4grt2EHz7Nrs6DnfvLOjUM7qn6fIyAARWdzVYe4tNxknkYMFWc48up11CYM0kJ3K94t0ZlsXJ26qe52FgZd4fSHScj_4tuM3no-jnap4vGY15vxq9T8i5bLvzmVoKFbJYRwZFmkcHbxaQMJ14587EDmX3TXyYxnhV6SzRvRrZl_b7ptmGWNXns0EbWXr-qdAq9uUWfuKIWt9hF3biBdhDBjj54CODC5USM-3QUclOadmZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=A6zGyVwLGZqc6iyqWEVqts7qURVoox5diVMObMNJdnzOlWItRyfMiFG0b_rmAqK95VS3cuxebZYnX93oRDAxG1qLKO9al5He48OxfdX4grt2EHz7Nrs6DnfvLOjUM7qn6fIyAARWdzVYe4tNxknkYMFWc48up11CYM0kJ3K94t0ZlsXJ26qe52FgZd4fSHScj_4tuM3no-jnap4vGY15vxq9T8i5bLvzmVoKFbJYRwZFmkcHbxaQMJ14587EDmX3TXyYxnhV6SzRvRrZl_b7ptmGWNXns0EbWXr-qdAq9uUWfuKIWt9hF3biBdhDBjj54CODC5USM-3QUclOadmZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sD9YVzmY-1R6S9sv_2Zsv_nNhzipIsKvdjlecpWKHelhS5QKRx5RSq8xcm7UA9CGa3NI5O3ZAbkdSzLsbqX37daJmIBJL_sNbb6dptGFWEatQjyN5KWhJ6bta1tWGXh1w1pOg_zK5sjOHuDNlWUjtL8ANsNpXXvSyMDAlwRqcQH3Ybt-brAm7YowYCBlCntlgRsu6KHN_S-h2VICA1MJ_4q4SWE3SUt1l8q1wl3vRTlfmdnwVxYVTXGY7w1FjmxzDgKe7lL2lwEFwrhQJdBt8R6uABJpRAhD-35_xW_Xjka9VIX8Nz_kR4cBYwlEumq2JwkpPh4Vy7pgPwWPNl2RjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sD9YVzmY-1R6S9sv_2Zsv_nNhzipIsKvdjlecpWKHelhS5QKRx5RSq8xcm7UA9CGa3NI5O3ZAbkdSzLsbqX37daJmIBJL_sNbb6dptGFWEatQjyN5KWhJ6bta1tWGXh1w1pOg_zK5sjOHuDNlWUjtL8ANsNpXXvSyMDAlwRqcQH3Ybt-brAm7YowYCBlCntlgRsu6KHN_S-h2VICA1MJ_4q4SWE3SUt1l8q1wl3vRTlfmdnwVxYVTXGY7w1FjmxzDgKe7lL2lwEFwrhQJdBt8R6uABJpRAhD-35_xW_Xjka9VIX8Nz_kR4cBYwlEumq2JwkpPh4Vy7pgPwWPNl2RjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=f6ibeABQRpleP58lGd3bcg_Yljx05ULbKLp8eYNbgB66eKwO_GNa8LUE4oRmY0WfhyxGYRKTWLD-OYLa6K5tNg_P0-rww2b-5aJXbAbphZwLagBoQutTGh3gOvByQynZm99WJelf8vYicBdqBNxPimSgdSWqHqloIVIwpxlFEo1h5PbSgzapR6mLzJojIV3ja9ZPrk2_Z4pU58kmcWufoADi_-KGBduSsOGcJBNaW5G0esk_brgqt2kz-zKd-V8UkHTTl_oa5QZOQdO3BWGSdDctUzmiK5UzhS7sxHeARKgWlZn2DAfzu7VwcML_JQPRtXJjx9JbkiTjrR87wIXDJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=f6ibeABQRpleP58lGd3bcg_Yljx05ULbKLp8eYNbgB66eKwO_GNa8LUE4oRmY0WfhyxGYRKTWLD-OYLa6K5tNg_P0-rww2b-5aJXbAbphZwLagBoQutTGh3gOvByQynZm99WJelf8vYicBdqBNxPimSgdSWqHqloIVIwpxlFEo1h5PbSgzapR6mLzJojIV3ja9ZPrk2_Z4pU58kmcWufoADi_-KGBduSsOGcJBNaW5G0esk_brgqt2kz-zKd-V8UkHTTl_oa5QZOQdO3BWGSdDctUzmiK5UzhS7sxHeARKgWlZn2DAfzu7VwcML_JQPRtXJjx9JbkiTjrR87wIXDJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=swWbOXWZEq9rbirgwjO3VxBCO2towFS85qdBTWaWVtOLhepdF02TnnoLnc6r6_wsumkttU1lif66n32rY3DaPb4l2S4iyvep1o0A4Ws9yyYA3Wtb513SELZTe4rTaTX8K8uswV6__cCfooEiK4YG_COPbDTGTo6jN5iCmXc6NXUMlAXhf29KcbJ4NYz1WbtjVv-zhRTdKCRQO_lT8mPHLV0RdDp6el2QyMRv8_DUcz16m2YpsJeRYpQBoz_9JQp3eOMvmGyGCgywjseQPME_dJVwUPu2qIY2q83sT-_pU7agB-bTUQPsOzRl5gmTvkzcm6vzrE64s9-Lzzk16fNmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=swWbOXWZEq9rbirgwjO3VxBCO2towFS85qdBTWaWVtOLhepdF02TnnoLnc6r6_wsumkttU1lif66n32rY3DaPb4l2S4iyvep1o0A4Ws9yyYA3Wtb513SELZTe4rTaTX8K8uswV6__cCfooEiK4YG_COPbDTGTo6jN5iCmXc6NXUMlAXhf29KcbJ4NYz1WbtjVv-zhRTdKCRQO_lT8mPHLV0RdDp6el2QyMRv8_DUcz16m2YpsJeRYpQBoz_9JQp3eOMvmGyGCgywjseQPME_dJVwUPu2qIY2q83sT-_pU7agB-bTUQPsOzRl5gmTvkzcm6vzrE64s9-Lzzk16fNmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YhZiNDeJvPnO1cyhwlSahomXTlz5toPWNaVGbwOMDHxELt--wE-JWtGwec_vYPCAPvtzgnthx4uxU5HHY5i-GoWPhxfHtuRFH_BjAATe68RAfpZFcOXHEqc6HQnssy_rsGW4WW-kwk0hEpvFx95qTxeVGo4XelqtS0G_rSeUcbWqKW3h5ba092W9JEsxFPtP7UNOOUJYwueQvYZyIQw8hXU7DvZAt5e0AaZe97JhftIc3rv-ND7YDZLs861ReLmxprkmoBNdGRhsfUHcX3ZNmKVjzCT_YEwehwO3iyrq0QJyrCSy_SDKMXjdfGzHQpNjkkQxmM9ckMDlSUbhFjuDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gZerJy1p_WD70EUoOYxAI1cNd6P0D94k_VsRTLNdSnX0zg1Spsrkys7-axSR1xBInGBZrnuB86H8buaXi5RJEyT8fF9XIzMBC5r8SmZLDlYuREDlyDlP4kK4nDVW4wiyivbOz5VpW1uvIQiuVNJDOkEM5nm_VX4gkH5ofLJ6V9hR1rsNBi2NiaZgXGLodAwn1fLaVD1EoKTRtfFywWQYOZmvmteNCEpA_dpEpyPWfK_X5eMIa0F1yTw4lMK_ny0EjiIQ_Wt1jyZ3Fs04HIQNHc5bLi1aAK_ZMVbomFDnqYNhlM8OPgUTfqG0_qbzFe-Wg5ZjGKmz3rW6Vf1w1poAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=hEZEXNHV-gYEjHv-0NUvBk9eQW9jZSzz59guAjxjF6jgOJComZksKS3T5fc84bjEdrkIETjsoMWA20UgmdV0e1Cs3ciwfj2-bc67VIDBBmKyV7Y9oZZJYYym_hKRqvEBhwte87y8y8zIHC1OSBmjms_0dzgowbb--QKLOZYlVwVH9QwWYXJ1E7e_2djhiuFhNi39z0GKx5SbxahDFtkCiqHEds_jdDRyOeZ2JNIU-pZpAqBUln53_aDaGdAoQL8G7SwxnUTM9li6LobbUZzaleqrI3lKEuxgnhXnbtGdaBAdk39vNKmI4vJdFF8bgDF0KqcOiNNfT5DP7S4lD4RKERUoUl8Sf0ixVgG-cz7HkFB75X4GcIl-v5OmIolcVBCsNKethdbglN_T6XSSFn1EnBgRCWPnK_u1lsMyeJjRdlxRQahzDQa4Hn9-mX6gg7o2b_ajplWNHxXczRlfxAvfWOZD1lsv6bJfz750S5kkBR9UrzZvg3588l18uY-Wvqwn6HHn_OTq6BTiiwS7Uvoxv9ulWjLOz05r99Kc71DUO5EBtdS9dA4SLd2qVhBKcxkz8giidWd3PYbrb9S_M1U9DHJ9Qjaw6JQF6SjVqi_WR-W8TbY0Z50XzNlDA8DSq_LE2ZNa9kVKXnzkAB1VLC5wiz028d488EJwI_5wO4Rrsyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=hEZEXNHV-gYEjHv-0NUvBk9eQW9jZSzz59guAjxjF6jgOJComZksKS3T5fc84bjEdrkIETjsoMWA20UgmdV0e1Cs3ciwfj2-bc67VIDBBmKyV7Y9oZZJYYym_hKRqvEBhwte87y8y8zIHC1OSBmjms_0dzgowbb--QKLOZYlVwVH9QwWYXJ1E7e_2djhiuFhNi39z0GKx5SbxahDFtkCiqHEds_jdDRyOeZ2JNIU-pZpAqBUln53_aDaGdAoQL8G7SwxnUTM9li6LobbUZzaleqrI3lKEuxgnhXnbtGdaBAdk39vNKmI4vJdFF8bgDF0KqcOiNNfT5DP7S4lD4RKERUoUl8Sf0ixVgG-cz7HkFB75X4GcIl-v5OmIolcVBCsNKethdbglN_T6XSSFn1EnBgRCWPnK_u1lsMyeJjRdlxRQahzDQa4Hn9-mX6gg7o2b_ajplWNHxXczRlfxAvfWOZD1lsv6bJfz750S5kkBR9UrzZvg3588l18uY-Wvqwn6HHn_OTq6BTiiwS7Uvoxv9ulWjLOz05r99Kc71DUO5EBtdS9dA4SLd2qVhBKcxkz8giidWd3PYbrb9S_M1U9DHJ9Qjaw6JQF6SjVqi_WR-W8TbY0Z50XzNlDA8DSq_LE2ZNa9kVKXnzkAB1VLC5wiz028d488EJwI_5wO4Rrsyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=sHDvhBs-KjpoBCaoC4feRUgCrSUHqnVSpwViV9QE4Eb7CfbqUncqQPH1ZANNPrLS28rtw49YpFnPDX6Q-_KUfoq4UZ7t23fOlVw0klc1Nfg7Zs_fJgKGXvLdLkB_ZFpiZXTn7_ZOmadSdgXdOEcyN-bWUV3fzp03KVYwF6HHCv9xFekoar8MnszD5bhXJf4GYj5Ks7YuqB9aWkOiSEjnGjNhtthh1SzubCV-ggWzayChnJCw_xdikp7boi7wwTTkMaTe5jzcN58iQkNCZ-AIh_LUWlllq0aKCn1BO0B24zPl2gte-ZoJ1gYMMB5DGBAsJ8nWwwfzy-JA1K1jeuJdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=sHDvhBs-KjpoBCaoC4feRUgCrSUHqnVSpwViV9QE4Eb7CfbqUncqQPH1ZANNPrLS28rtw49YpFnPDX6Q-_KUfoq4UZ7t23fOlVw0klc1Nfg7Zs_fJgKGXvLdLkB_ZFpiZXTn7_ZOmadSdgXdOEcyN-bWUV3fzp03KVYwF6HHCv9xFekoar8MnszD5bhXJf4GYj5Ks7YuqB9aWkOiSEjnGjNhtthh1SzubCV-ggWzayChnJCw_xdikp7boi7wwTTkMaTe5jzcN58iQkNCZ-AIh_LUWlllq0aKCn1BO0B24zPl2gte-ZoJ1gYMMB5DGBAsJ8nWwwfzy-JA1K1jeuJdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=IhWwESrn5YvswT3y-phnmCHHqtD2cqVq0fypJArVk134uNsIiSwFXvdWO1TGtoMSKfWfzIqIx171GA6zM3T_Pd9JW74GPufxu1InrAqObw_cl4yoAE0wcEOElYsIJl01i7oPJe1aM2LS4LiBxloW6q5lZOrUYZuVB1-aTERvr4ZZpHkkdTlEg3hN-V9iwoJ0cS5-6R4E3tMoTJCyf94iC4lcFNSn_AYT5NAbR3tpiPKGXs-kOwSenNayXSxRtIi6RkvyWekXw8UFgm2NbZUW0u687alw61_N4CFtfilj9LWYsuzd4ughDSLn0TgPCqMn_qDmSn0dREMtZCJls4UFIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=IhWwESrn5YvswT3y-phnmCHHqtD2cqVq0fypJArVk134uNsIiSwFXvdWO1TGtoMSKfWfzIqIx171GA6zM3T_Pd9JW74GPufxu1InrAqObw_cl4yoAE0wcEOElYsIJl01i7oPJe1aM2LS4LiBxloW6q5lZOrUYZuVB1-aTERvr4ZZpHkkdTlEg3hN-V9iwoJ0cS5-6R4E3tMoTJCyf94iC4lcFNSn_AYT5NAbR3tpiPKGXs-kOwSenNayXSxRtIi6RkvyWekXw8UFgm2NbZUW0u687alw61_N4CFtfilj9LWYsuzd4ughDSLn0TgPCqMn_qDmSn0dREMtZCJls4UFIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=uF4l6_Oxl8gYa_q63VZb7VSCUrnBsevTJJqGgQTmrloM3uelng7gZ9fAC8MO6bln48Crkf83hB5gbmxsFHafkPtZtxLv14Pxv0LfxHy8cPh9lU77X3ShJ3va2yORDt0XM4NfFvENNSq_SQBo2MgOVDTBM-kkynqbUOr88n0mXksvML5FJrDj0823NhtVhI8AWZRn-KMTvI84ILceSxPTzp-wfpYkqWx8LY4lQcF9ErimDsHorn3ElMRynVHORqqzaqo_KPkVhwkPjkJF6gogpAHIu_Iqg_nXiuQSO6HkfJhfMc4axGyydRp-T1-vkq_76runCAZjUc8VwxyN__ZJUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=uF4l6_Oxl8gYa_q63VZb7VSCUrnBsevTJJqGgQTmrloM3uelng7gZ9fAC8MO6bln48Crkf83hB5gbmxsFHafkPtZtxLv14Pxv0LfxHy8cPh9lU77X3ShJ3va2yORDt0XM4NfFvENNSq_SQBo2MgOVDTBM-kkynqbUOr88n0mXksvML5FJrDj0823NhtVhI8AWZRn-KMTvI84ILceSxPTzp-wfpYkqWx8LY4lQcF9ErimDsHorn3ElMRynVHORqqzaqo_KPkVhwkPjkJF6gogpAHIu_Iqg_nXiuQSO6HkfJhfMc4axGyydRp-T1-vkq_76runCAZjUc8VwxyN__ZJUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=L7jdPFSypcIJd7VY-2kFGRL3N-7PIfsqpd4ByFkH7pemGgqP-9DHuO21La8wAPTu9n2To_JQx0I_G8W4wi-OEwcsweIaVDd_o8RDEsXp421Yiv11YKH3ssTI1E6A0rjKyHmCV1ks1j4KU-zYyICg63CUdPmOYOWHtiVqdkJNmPF7PQbR8kJNVTJTQ7qFV1KQHtih0w_xojAQT_TrNYwfzP-OMShbUarsKBnaU4xs4exwGx1de8mREJ5Eg16-08IFi_FTdahQ9B9CFscVgvxy4eHSVDceoRD2eB8ZvQpGz4_qxwc5iyZEfc_KsRx7b4AfTzbTVot8TQqt6nPHUnuxqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=L7jdPFSypcIJd7VY-2kFGRL3N-7PIfsqpd4ByFkH7pemGgqP-9DHuO21La8wAPTu9n2To_JQx0I_G8W4wi-OEwcsweIaVDd_o8RDEsXp421Yiv11YKH3ssTI1E6A0rjKyHmCV1ks1j4KU-zYyICg63CUdPmOYOWHtiVqdkJNmPF7PQbR8kJNVTJTQ7qFV1KQHtih0w_xojAQT_TrNYwfzP-OMShbUarsKBnaU4xs4exwGx1de8mREJ5Eg16-08IFi_FTdahQ9B9CFscVgvxy4eHSVDceoRD2eB8ZvQpGz4_qxwc5iyZEfc_KsRx7b4AfTzbTVot8TQqt6nPHUnuxqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUjOAKvf07e6Qm3m7MYTX-bSoLPEpU85FIj-2-EPY6n5Z3O5KF-AhiopvhSZmuQKEn7JAF1EHujflmhg6n-CcmUORNvMDVfcPMcr9yeMMmv5-_pec-r7vsdzeEqmpMBf2zn-c6hkp7-pahEisTau-ly3GRHNA3gXwKJTcMiM04e-cdT56sFp5hj5es0QGQEhSYuQjVv7b6Je4L5_cYPWZWfolC7WXn6f8pfO8S5barRwuFQNVZY_1QamYyzvejoLVafoq_NqYr4IVLZDvBvUxWyjKEQ92XVifGE4-N7luhWd5NVZlT1qpQn_rR6FPed0N8KFNcQXpisX_H4ZptKjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSwZ4rBTuibetVxBs1IlvDSamaQaFGK80kUXNB5JOymw6ee2kg9utq8f2asebOsyoLgaXUDziLx2pBImtFRaibxmeI5oyfgrIR_ZDDPSCq2khpEpzQZHvWrFkc_gwgTIlE2_72cjsog2GYYn8acXWQsR0We2dYXwZ7btulju6rosPXIaA0bb1vFaHXcm-ORWtyu9oMQPBgvR8tRdFiirGbZWmQp1rmH8Th-SMnQMdKLY_V-lRBGsxBZ-1rRt35cQEbJbpvjuwz8GhlEE0Vai2hMOLg6ef7n-1J4ZhI-FrucD9LrDPLWkL3GN267O_CzNmlqBlOxE1AXyODfYoRuf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF_1XbxBeArTb3iQYNTXi_IEztpiLPzdLVIH2mcNREROHEVq-ajH0e6lv_dPBiV_AlDhYbcFX1IObK_AsivHpHbvqZhsd6wL4bfViVQlMqzUkN_Ni9ZLs6ovIOkAkIj_8J9dkuJN3yQwi1tKp7lJ5MZFNZe5SB4u7PQxvZ-YYlx8OFYIm-9ofMPl6HfA66r3WT4BQxFnKnLFf1YjNwv4LBvyMRg97MlBEOi2Oy_fph0MQllOANR1tvG16ZFodrbTkkZVCjuPFZvzUpZa_8t2PkrjvYb7rXXvWftdPYjoQEbo6f2pghMPlwvQqv6jFYCa8Gg6vxmHF9-qYOH4GaMj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG0hx3SkOlrXJKcuCh7d7l_qMX2xmZCGWKDQibDQ7chzxf4n6UA2zP-mFK0s8NDUHJaysT4nzt2BBGxsIHTSB0DTGq6x2tHgd6ddxjXU2aYrOIlP5EPqqFLC8UJjYRsMKE7HMRl4aARQWfAyKZ-kbyW3lB-98IymzXXuLuRD7V5oQGt1Wuz5pxImcjOYbcKXx9nbfdIhPrmoKgt1YW7fropOa7H43Tqy40hxi-WJjepuoXgL_q8_BIWujWW2REJdKROxYzCgFdT6WEw0_MO9yhQweE_s0xTuzftSeTfpqyD47MIM0ndYsD1W-wn845yF-ZjADAinA73w9LK-dREc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF5_Y9DTKqmRZry1mamu5aa5h0lczav-F5n_VxF_42_0SDcWFBkNi9q1OTLuoo6_tnt_j_8OtDunN0O43PTFiPPmECwz0Gp7CIRID1FHa6bymPoYu3kEVRVF5G3PC0Fb1I6hc5H0G-9KOgo0XJURmn4yrbvb5yp0Hhw1JfzQ1N71H82iqxY9rcdU8THsSNgu_VdHXq8NkBDAkPDmHVeW1DBDE3xXIDBXcKNoToUSQMN163o1kLI1fYhxgRxmZ486aor5KjgLLTXrTIj1dQflzzV23dvddnHz0nsfey2TrBiyFwe3_dm2WhZT2CCFQFdYa_M6s4MHBnRYub5Inj4tjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_uSsfCmCQWbANqkaCiv2iY5cwVS6SND9FRzdly9xJ8RqLiIV5esmJuAh-qnTSvtY_Iw2hQN5Pgo3Af0DR4cTzF-dsOYKM2YZQOtlTBMJCcpRMHLd8HHqBlnZ6E6BqpCTPhhXJkO0AqU5e0qVjHwKTKZb9OvkXQmtuVOaGFrjfV2r4k75GPFZpIkjq6P8biq4129hDWyMT34cayUccfoM6potNGuF_5A7GAuuFXKqcgvG9rNMc2Y8o3e4pDTs7T9DSvUaffLG7PkkpAcZK6vjL-1JlnJaKILkWf58-rus_P32pAu4NiUws1ysBZ6jRzJiWiLVJLGvtGNbAit17Qnvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=uStGlw8yQ8eVOZqN03BgoJRWK7vmzVH_bvcd1RQki-zpFUTMPYs__knaA-wiQKDKMc2jckttDlIhLu5XRJ9vDFoiPunIWoue9qBN8SUc0OyY3iS_tqK-AB2k_cCdbSnhp04LcKVhLTI4J_ZsinCC3DwZyl6oq5B4wYCsUsS8zQP4EyTPAdRGGaj9ZutJdB9lkQEgofATw1LP-OWS8PwRq3pRNi6ZkTZXLtByJcKvi_VVZN4YdMcppZFV5sdb2YLOxb81BAPpJb2nLahck2L_6_qm3mZmtUNPb4E6DtMyeInmiECrwVPMU3s8b1tR8mJOP1rMGj3rwH_5AsNb2kCFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=uStGlw8yQ8eVOZqN03BgoJRWK7vmzVH_bvcd1RQki-zpFUTMPYs__knaA-wiQKDKMc2jckttDlIhLu5XRJ9vDFoiPunIWoue9qBN8SUc0OyY3iS_tqK-AB2k_cCdbSnhp04LcKVhLTI4J_ZsinCC3DwZyl6oq5B4wYCsUsS8zQP4EyTPAdRGGaj9ZutJdB9lkQEgofATw1LP-OWS8PwRq3pRNi6ZkTZXLtByJcKvi_VVZN4YdMcppZFV5sdb2YLOxb81BAPpJb2nLahck2L_6_qm3mZmtUNPb4E6DtMyeInmiECrwVPMU3s8b1tR8mJOP1rMGj3rwH_5AsNb2kCFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/i2gfux0YuYxKU4pbBiZhx2_O4ys3ipkk42PAenNVKJov_Ho7Mjh_3M3uAkSPvzk63SDdyRnt1hNw_AJSea2i8wRXpQ9f4_F8vARmHlSVSrJexG-fq7TdufYrp-onK0KXLoESjRjgBisDwjkfatO6Yvao_FPaBQ2_h1UZMsEmpPD1hxjxQIehSvuGvktf6QHXlCoaIt7aC_6OXWD9Pi4Cxc5FGZMvWtCnvY5uUs4w-uuXLYr9BjTMsQw0dznjscFlLgHJb_WFAD9Ko6FtViBAk42puHEGy0MDH4WMEysc2ABriSj9seHiGKFbT3A-P17oHREw7Gio64aKXWKWwDKYDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=Z962B_96_y_6oVo98H_LlrVRfNpfRgdBHeUpW0XIUwtNyGwsirI6oZFZoIhdqVy941kUWZv5hp-0yhpTfgyYDUoTZoT5Yrzs8t69gUw5tW_-Oihv_-LSz-iy52Rm04wO9ALFDd8_AHU5uymbzBeHh4Xet3dTvGnIH9ZsdqyRQKcqvuGXNPG2EV-Gy186hAl3NxxOugbrf9z3dcvmgeNHLs8BWhGdmSn621YwXnNm5Es0gYxC1YMWTnVlSiTjXxVwlPOQECRFr5nOcwNKPv7wCtqp5y-ScmIvGahGXaPmjYtcljLooer1GfocgEJZANJuUYYOvsHqDNAuNgGepxwYgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=Z962B_96_y_6oVo98H_LlrVRfNpfRgdBHeUpW0XIUwtNyGwsirI6oZFZoIhdqVy941kUWZv5hp-0yhpTfgyYDUoTZoT5Yrzs8t69gUw5tW_-Oihv_-LSz-iy52Rm04wO9ALFDd8_AHU5uymbzBeHh4Xet3dTvGnIH9ZsdqyRQKcqvuGXNPG2EV-Gy186hAl3NxxOugbrf9z3dcvmgeNHLs8BWhGdmSn621YwXnNm5Es0gYxC1YMWTnVlSiTjXxVwlPOQECRFr5nOcwNKPv7wCtqp5y-ScmIvGahGXaPmjYtcljLooer1GfocgEJZANJuUYYOvsHqDNAuNgGepxwYgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=h-ATR0DwrAB1P0x2kMVjfwJE7iA-9nb9fnUI7aqLYso0gNOxUbxWv1VIPJyBCdBy9l3an7IOLSeFrlNMGcxtWfEfirC61MbjY5HUm6yEJ3E9VXVVqwAzo40_vtZSQstdIhf4dSvDNTwDS935h3XYOMDd0ZoUwnJa1H3BLTyO3aFvrfNehGiR9XA-rR-jqjNWn2fzTmwg2KOJCgGarRUJjTfKsO_BtnviCwhUhauW89liEUS7j-LvlkkCD3uvlxKdu3wFv7ROA8CWpDT7O1J5-v03jgO4DRu0583nnqAkAOR7LYqPgcq0G7H8JXADoKgzaw07FNSdg82sOWH4QxXp6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=h-ATR0DwrAB1P0x2kMVjfwJE7iA-9nb9fnUI7aqLYso0gNOxUbxWv1VIPJyBCdBy9l3an7IOLSeFrlNMGcxtWfEfirC61MbjY5HUm6yEJ3E9VXVVqwAzo40_vtZSQstdIhf4dSvDNTwDS935h3XYOMDd0ZoUwnJa1H3BLTyO3aFvrfNehGiR9XA-rR-jqjNWn2fzTmwg2KOJCgGarRUJjTfKsO_BtnviCwhUhauW89liEUS7j-LvlkkCD3uvlxKdu3wFv7ROA8CWpDT7O1J5-v03jgO4DRu0583nnqAkAOR7LYqPgcq0G7H8JXADoKgzaw07FNSdg82sOWH4QxXp6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=UMZcNRhAnxpKU-ANmUtfvIfyKlS2uOBz-K2SxwpyBhxwQ4xxaMYgPFeAX5hUE2R4yrq6W90NslOkDwKFoJHWZ-VybMWw9ptfVqNFIdWhVwqAGexs51kmETlOrSeTXZMRGsl0JL0EvH8cqhZkT7x-qgJx2LIk00ibPIgqMOsHDrVkAvLZoPIZF-RsL5-VvMr0j5DPwO4rZjlY0k0Z9FVtuIzu1eXjtJjLoGiO0gT8LymyegzBN8O38bMsaerw3buVYnkMQ8WkvJ0-dy3O3hkzTL72OPslOjgwLj6Ocl4-jD8d86_ASHrxAccr8ER0QB0vq7keImg9RdZTK915KdLqQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=UMZcNRhAnxpKU-ANmUtfvIfyKlS2uOBz-K2SxwpyBhxwQ4xxaMYgPFeAX5hUE2R4yrq6W90NslOkDwKFoJHWZ-VybMWw9ptfVqNFIdWhVwqAGexs51kmETlOrSeTXZMRGsl0JL0EvH8cqhZkT7x-qgJx2LIk00ibPIgqMOsHDrVkAvLZoPIZF-RsL5-VvMr0j5DPwO4rZjlY0k0Z9FVtuIzu1eXjtJjLoGiO0gT8LymyegzBN8O38bMsaerw3buVYnkMQ8WkvJ0-dy3O3hkzTL72OPslOjgwLj6Ocl4-jD8d86_ASHrxAccr8ER0QB0vq7keImg9RdZTK915KdLqQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT6t5unkweQBAa0xNEMsv2a-8BbZHQI23HXPc1wcmEAvTOAB4peuTWGNzZvayxI0h3LZUeCmmJQykmzETHc09sJLMvnPmwpcqFPwLZ50We7XB8jKS3K19wBmJwsYCNKBZvU4nMZ9fZE8evsr3P0eqorHeEdszUVdbN4RA1dCV2K7lnapRPrwmnk7KZaEfulKjdrLs5hRm9CeF7rlmdpO7vda3Ud43TH7XQVSNHYJSy2H91yZE12JpylcZ7Gy0iDONyZvmTDqL_-N10ihlfL4MfAJh4mL8nhy-YH3vaeUF5ZZ7qnKwlp_7y6p0Nobc1Q4qBtq2_CZWttJZZQPoAgrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=CPJFNCRuv9dVt6_hP-WoKTfDwEtN-3gQpptUuS8oCnK87J4tZywTO5FupswjBvjYxOHiU-NVupU2ZxCDBZKxXKi8QzfcsR2HYoyb1fkYjP7oSgNa5on6GfNvWdOBhlp4RBuXaR5HWxgl4Ib5QlJ6nNIrmScXTJbQtwbGFh-ixgUHf8pBNm0gd7GvTvdoDU13v4DBy5FcT5UPRmIx92KOOe6zNLAiOY1Xg1dUYSZWiEIeMByl9unCKZ4LSI9E4rrBLtX9SBdCRfdIUPrOtB4J2kK56VBPh5viWcEAcwA5HxImm_kLPGz6ZOSRs_OJxL96MvnYgrq1llwIY_4LGdBS9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=CPJFNCRuv9dVt6_hP-WoKTfDwEtN-3gQpptUuS8oCnK87J4tZywTO5FupswjBvjYxOHiU-NVupU2ZxCDBZKxXKi8QzfcsR2HYoyb1fkYjP7oSgNa5on6GfNvWdOBhlp4RBuXaR5HWxgl4Ib5QlJ6nNIrmScXTJbQtwbGFh-ixgUHf8pBNm0gd7GvTvdoDU13v4DBy5FcT5UPRmIx92KOOe6zNLAiOY1Xg1dUYSZWiEIeMByl9unCKZ4LSI9E4rrBLtX9SBdCRfdIUPrOtB4J2kK56VBPh5viWcEAcwA5HxImm_kLPGz6ZOSRs_OJxL96MvnYgrq1llwIY_4LGdBS9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=qv5VE0DgP8OSgeZR3LK9csvjcKDx2KtUdEBI8f1Ru8qQVYk7z2qAgazVEeSd6hLtrtUTX4zqGK5gMYNIW6SH_cR7AbL7VMza-Wj28jTiLzdiiqPd1XIAT_ZJ9S-WPd8VGH-xJ4AK-WWPeOiPfZpqIsP7vvrRzdBoVThFWgMl-IY1SEFQvdigzjjr9FbnU0RPGajqEPoCHdEVEGvmIulPn8H6vPOmMTnEPehTcjBKPsI9iLneBZrbJ2zYm2VMW3MJE5rMDa2osCn7NYJI6J3a67xVkcV099pXmPoiRPL5rDS6v_-xu2Kp3i-dzFzdhxZHf6jAuSK8ZT4PS2e7EyKKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=qv5VE0DgP8OSgeZR3LK9csvjcKDx2KtUdEBI8f1Ru8qQVYk7z2qAgazVEeSd6hLtrtUTX4zqGK5gMYNIW6SH_cR7AbL7VMza-Wj28jTiLzdiiqPd1XIAT_ZJ9S-WPd8VGH-xJ4AK-WWPeOiPfZpqIsP7vvrRzdBoVThFWgMl-IY1SEFQvdigzjjr9FbnU0RPGajqEPoCHdEVEGvmIulPn8H6vPOmMTnEPehTcjBKPsI9iLneBZrbJ2zYm2VMW3MJE5rMDa2osCn7NYJI6J3a67xVkcV099pXmPoiRPL5rDS6v_-xu2Kp3i-dzFzdhxZHf6jAuSK8ZT4PS2e7EyKKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=lYuIsNkkdJN_L3OTTXMg0rFNv-Ct7f1uO6hgC9w5gmqnWvqhOsqVNcrR6jpHtD0xOKI0z3yZ3TPKGXPKA-xHYkU0_cBd-RkVMN_im2sBi-F-Slk84jK_nPlmdLrzsrwj_laRDtCD1yFRrLstwwLn3mvIJhVmGRuvLLad9PGjKT9CdPViZ3lG3t7TzWgNi0w4f-LqaInVNYuUe0relqt7EoJ3V1i11Kcx-G4kPNBtXWhAZ15Bmw5iI_uQXkHQCYg-8x2WbFcshu6B5PdSc2ill_6aS0sYK0xhT10sWH1ijM7O1g52G2ZlITD_M06g6HbSnu9CKtalqnchA0wE7NPF1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=lYuIsNkkdJN_L3OTTXMg0rFNv-Ct7f1uO6hgC9w5gmqnWvqhOsqVNcrR6jpHtD0xOKI0z3yZ3TPKGXPKA-xHYkU0_cBd-RkVMN_im2sBi-F-Slk84jK_nPlmdLrzsrwj_laRDtCD1yFRrLstwwLn3mvIJhVmGRuvLLad9PGjKT9CdPViZ3lG3t7TzWgNi0w4f-LqaInVNYuUe0relqt7EoJ3V1i11Kcx-G4kPNBtXWhAZ15Bmw5iI_uQXkHQCYg-8x2WbFcshu6B5PdSc2ill_6aS0sYK0xhT10sWH1ijM7O1g52G2ZlITD_M06g6HbSnu9CKtalqnchA0wE7NPF1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE_hOvLv6ZLB240Fok-DU02st0-6a428tYV388sA0xT4u70Qa6KejpRJpD59G-H8VoqgyQsvRjOqy5FRk-9-0zF8ULVy_x9RKQkkZ-MeawRYTGxJMYgXoMk8pmXEnFjRfWzCzEnf8REX6R0SuEzuDYWMpXfUYnzDQZeVRrJLmGAsUSMqSVp84XavuhMpEYLv3NDZw2iPgt33AO80cp38NVlkYsP-5g5WdgbYYaWGpQvk3lEvGpAg9bfP4c-HDFmAdX1ncnpzGb9BZZ1qYvBOZwTzOGzlK_RlxYRh00xux_uhJ7NAgyqOJseNiZ1YTkggOQVwfwmQI6qMwg4WBsSLCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uylsuiAvL3cgIaBMVCQCXBcpIZB70trUlrCq5BozYYj7yywfbD09qw22Z9jdwioB2d9IcwKOh4N25MfONcAgbl-vYe64w0cRzC2yLlrXva1ke7q8o6lL8N7EsNqkyCJPCHVbxjc4UZ2sLbA46qEc-QVOkvWChXsa5vRhnTVdMJlUrKoiirku7w-5l0MlgjXd9lDWqKGwakYJG8u0rXIt70BsxgAKNznn84kJdt1HWoSlL9PbJYpCh5-f9K2sZgq18Z3gB-U3PYoueiwgLk5tbpgFEflMBZX0zQfir87iJPyWBmmugfmZcsAiehMZ0IXmxHnuz6ElfDbOYIOWEliU9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=CvSLvRPq3LV-1RlgOz793nCAAEH1hWORuTDYXalJq7XlY-KuIn5qBavHEtHoErSWrEaWQCTVQbRVtqfBC1WpmBMTecpadzqUPqViMEdj-uiN8vL2cwf_riDSbYj328_Acx4rUfTQzphcO8-eKSOyd4r1c5BCwmuepSL7hPzFTkkbRF201XHXxZzN91bjMCDUbT1xo4ySjwhpgPcDuiswEOrqmR07yKgnIwWlE_Fabe4vEIBUgXCi5QSlEBdMiBcCLu-AWql21j541R421lLWEke_yKaFDytOum-Q-yhrMUi4dF_B-9fylgYLI8RF-40Mr3O8CPTkOlOqs0n5I4NYHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=CvSLvRPq3LV-1RlgOz793nCAAEH1hWORuTDYXalJq7XlY-KuIn5qBavHEtHoErSWrEaWQCTVQbRVtqfBC1WpmBMTecpadzqUPqViMEdj-uiN8vL2cwf_riDSbYj328_Acx4rUfTQzphcO8-eKSOyd4r1c5BCwmuepSL7hPzFTkkbRF201XHXxZzN91bjMCDUbT1xo4ySjwhpgPcDuiswEOrqmR07yKgnIwWlE_Fabe4vEIBUgXCi5QSlEBdMiBcCLu-AWql21j541R421lLWEke_yKaFDytOum-Q-yhrMUi4dF_B-9fylgYLI8RF-40Mr3O8CPTkOlOqs0n5I4NYHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZDHAvwzEg2jAtvKFeyb-HAkxLrCgmI9yFyNim7_bDXe9nqcJuBzMfEmirCPku_1RDJEUq0zku46BE4VOZRXpZRhNdu-n5QVl2_JfrJ4LrwsTgbkvfp3E_v2zX0A6O10XBqReGfg2QiORQ2rQpac0X-M1vpTp_juRNrXqFiMZ1Su-uVomtEwiUicYJtxp31vi_fairVND0pKa3Ip4VwwP9k9PQK3tEXg6JZEE2a4XsHDTLCjoZeJQ7dEEtcdXAueG2xQq0WaxyfvuPjY7CToBHWbwXdmxtvU0STnE5JXV0yWdLX2Hy5NKdpiskC3pGAHxmohbSh0SANcaCpTOm88Fsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=ICmNMheGMEfCuD4aOVTCuNamVTGEMpDKBjKifa6-k6OhFXb7rvCdj-jNfTdb_hzAMX_7mtbTw2NHnp00vP_IVbiM7qKdsvJd_F32679YSqYIA4Qrpv_bWzOAMWRoT6vN6SOwc_QwEAsGFb3JHnBZb42XsKaI8tBAa2KpvskshX6kfZ3Lnu333raN8U5a70w4h_zR5NPU0BzeyJfAe-h0TpHCBwi_JcxnZuglrt2e-YDVS5i-z77uX-ccYNgFIASIVQOS76ihjDngUTZqwZrQtiefuCoZbF2TrLkuHhDVWD673TVYwkqnzkJFJvz766j8cukT2g1lV9-6dMft-po9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=ICmNMheGMEfCuD4aOVTCuNamVTGEMpDKBjKifa6-k6OhFXb7rvCdj-jNfTdb_hzAMX_7mtbTw2NHnp00vP_IVbiM7qKdsvJd_F32679YSqYIA4Qrpv_bWzOAMWRoT6vN6SOwc_QwEAsGFb3JHnBZb42XsKaI8tBAa2KpvskshX6kfZ3Lnu333raN8U5a70w4h_zR5NPU0BzeyJfAe-h0TpHCBwi_JcxnZuglrt2e-YDVS5i-z77uX-ccYNgFIASIVQOS76ihjDngUTZqwZrQtiefuCoZbF2TrLkuHhDVWD673TVYwkqnzkJFJvz766j8cukT2g1lV9-6dMft-po9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peBoGmhgwGcctlwn4zKle4rEyR0DfqFQj2IxzzQVlY6KWB_wfKYpONkl_kGR708wlGKQSkCmzkui3LcPPot3ax1Ke2igVsiDuf05slxe3ngrsEhJxf-PbYA6VxQnXo5Y6xPxbne4enIBie6NESI2-oMKKjehDO0GU5AXhS5NHIVYOWI4_1anx6d-HPqfb9esfuEmfcU3oBLa9xIFdOwsNUYbRH4yNf3Yw2vql6EfP5DoomVD_oC6sV0Ioz6_mnoBRnkToJM6S61Lld22RpHYx8BemfhrrwaO4uMcO82TUWL63FyNiQny8l44NCqQU5z8D-i4k-BcteFqUkdQhV7nMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=m_5QthzYgh36obiFpwhl7xYvKJTAvuRu9pNzg7huG1fRkVHQ9epJKZ0mZgt55Pq1aq_ITY1-D99EhgH1iF-tGF05w8V8gwBgTUQMTkCOAFZ2NWSFotQkwUlq1SRJO-RF4Zv3ja4yNv-NlvA0yDWCkfXinM_f4LILauo_VVX1LYgY0NnTe6G9o7Uarp2jcA2TqUQJyB1mYdXCOXEQPkCHIPm4Em8nVDuWMgrrC0wET3y7p3eqhEHh2-d0vVOCucw-6iDKU-ZDfJC_n4gAXeAGExGPYISv4e0JkqWrUZZA9gtHjmxVGuLwSm_9aVeDXrRm35Vhn2r_DNbRPdAgksiXew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=m_5QthzYgh36obiFpwhl7xYvKJTAvuRu9pNzg7huG1fRkVHQ9epJKZ0mZgt55Pq1aq_ITY1-D99EhgH1iF-tGF05w8V8gwBgTUQMTkCOAFZ2NWSFotQkwUlq1SRJO-RF4Zv3ja4yNv-NlvA0yDWCkfXinM_f4LILauo_VVX1LYgY0NnTe6G9o7Uarp2jcA2TqUQJyB1mYdXCOXEQPkCHIPm4Em8nVDuWMgrrC0wET3y7p3eqhEHh2-d0vVOCucw-6iDKU-ZDfJC_n4gAXeAGExGPYISv4e0JkqWrUZZA9gtHjmxVGuLwSm_9aVeDXrRm35Vhn2r_DNbRPdAgksiXew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=BTBb6NlJifQ9JXLCpykCJDQkJKh1HJtbqGC7wcxG4YXa6c4qZwhAK73jwtE2YBGLfyc1FBVbgMkS5-tiS_NnjEdBg2MG0aGdz_qLjbJ2_-DwJ2qV8WUyiY9KvyGyWPVbxzaq1t4Mz6yqDZKBWU4aQYcRA-q6Nbq2G60rAG58Iy-RyAPFs5g_WK4dKemSmRVTFF6Ms9tdlcUR65Dzyqse8QF2Tryy5_5O2GIBxCRqUOb0wi7CwsQVWTfk9GtWSg566zSdrvLLCtnHGu37Gq5s0lx4YCym0Wu2axaKR5x-WhNDKKEV-kNgFZVLsRGD3HtAiz38A9CjarZvXIYJpCd-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=BTBb6NlJifQ9JXLCpykCJDQkJKh1HJtbqGC7wcxG4YXa6c4qZwhAK73jwtE2YBGLfyc1FBVbgMkS5-tiS_NnjEdBg2MG0aGdz_qLjbJ2_-DwJ2qV8WUyiY9KvyGyWPVbxzaq1t4Mz6yqDZKBWU4aQYcRA-q6Nbq2G60rAG58Iy-RyAPFs5g_WK4dKemSmRVTFF6Ms9tdlcUR65Dzyqse8QF2Tryy5_5O2GIBxCRqUOb0wi7CwsQVWTfk9GtWSg566zSdrvLLCtnHGu37Gq5s0lx4YCym0Wu2axaKR5x-WhNDKKEV-kNgFZVLsRGD3HtAiz38A9CjarZvXIYJpCd-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WI8_jGOxkRxZiEqrdTDVhkT6Nbmz8OTG_libX82WGW-A7hR5H-irmnPQZCV-auulPgaF7MRWwvjbKjVKdvVJWaoFVY53n6TcavkMWBWEMROvw2r1wltY_rGN8j16tnySiB7OuhFtpeZy5tYhkOm5O4daKkrPVN4RyceohG_khO6nW8Zu7Z6pPhB43MXwkBf3hShtuLtaZXzRUzBmfryHjTCJHC_AtRLiaKuMmPJB-S7sj-xJ0_8UH9Z3gFZalpFf4OvDlUOoR01kBAHQRudow9ZgHbjjar8ydtrfbGpW7dGVPUfZpe5SbNo8dVOtfDxR5L9nuipzGvGCvrKm5LvTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN6-M0e7whS-fdQJuszNYTse8x3rEOjeJloeWzlqdPhKzv7ILAnPJPwJ_VUoepZhKpNzuN8-rT6LQvdJmxYLhPzAz3Sgsyj0qBDlmgCttK61YPefpYqp8Pj56FyqF9-jPGq-P9PWViGS5fJs2jTEKI3oW4sfL3Gm6itIBIg9vRVlxK-SwyI578155QihR-IBWgUsWs4MvFCZeS5H0W2UvFwmZM-hCWpH_reir5HMOr8czu9qVAZIwDOpDggtbbNtWVbH0bKdzKswAjpCmvslXGzaTkH2_V1fsTc6Ipd7ZYC1BcO94V1ngfvwpy8UJcjah98QsNpprHdu-QICsjkt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-m9W5V9sAtXUegoHwyW9XnsfZLSjZpXHmy7wZtXF1EFbHd4gKPYONDsfvT0qRVA9Gh4Oi2LMa7K5GSnGDkY8TtWiQsRg5ur837e_sFQOTZXOligXeedHf8PeM7KiWcZW1OJ-5IAImC6AFYoYOcXLg3fnaZFYYzIs3ElxBQmQH65RH6ZbdllyehPK7BH7XYKXlkyH8lc1LybjvjZqTBGhrCwiVH82zHW1bPSnzxDbjSFUpTp-PzxzQnPvQdZzPKrRl_i6jDi1TRepnBsPov6HftmFoBwbWZOLjikH14JcF_TpI5ztD4vu_TtUiT0PIMk9llxmWwtRx90C3lnLMV97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=te8yvmgl5gzUa3_WdIBU7MBekmkeqAbpdJvMzH2GwSUWA_AlDrMCkP7cs_Ouv7V7WisKG_E3WLvoxraky8W-dUlZ-FcpqubHvTbRIp1qdLI6EoogZjDI4tU7iQ2sGcOlgxk7_CLH2OWW2EsJoJLgFD5ifPJaWU98euZZPzU-Oxaq993nwGXekiyQ5mf_4XmLJqyMRJt9r0F9xf9GKB8YFJsxlI_BGipBn6MUl2OfYYLhYVOsqmcFHcMU94TxxV2Unm2_queQJU_03iLu4svGRsqsLyUc_obQpWskno74EawBWB7vvs8L691JAgIo9LKAMEqACE0tI5WlQwfVS2Ch1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=te8yvmgl5gzUa3_WdIBU7MBekmkeqAbpdJvMzH2GwSUWA_AlDrMCkP7cs_Ouv7V7WisKG_E3WLvoxraky8W-dUlZ-FcpqubHvTbRIp1qdLI6EoogZjDI4tU7iQ2sGcOlgxk7_CLH2OWW2EsJoJLgFD5ifPJaWU98euZZPzU-Oxaq993nwGXekiyQ5mf_4XmLJqyMRJt9r0F9xf9GKB8YFJsxlI_BGipBn6MUl2OfYYLhYVOsqmcFHcMU94TxxV2Unm2_queQJU_03iLu4svGRsqsLyUc_obQpWskno74EawBWB7vvs8L691JAgIo9LKAMEqACE0tI5WlQwfVS2Ch1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=YAiU097h87d-ebTagbSlYXGgdXl8fd7c5EtrliG-OOK2v0XL53dmnuAmucT6wSHyk9RZQAMRjJjuZxcxfzOlOg9wf5sNACeVoZmAul4Cv4d_crFcp6yKGi7yTC62w_in4T3M92O6smWvXR9OkYvRnUryRVui7eVPL_Zjo4UN1yfO7V9m4H74VSxwNiX6MDQgxyZxOpvkiz3EzcdztoxEij463L1lldc9q15OYsS9SzyEGrpK1IZvQOVdBbmR2-T0anBhL8vIgV3qggFRMALRFuqfYaQhcv4qqGb7tnbP27cYTTfN9pMHmvEMHIxZcBjyOOT53mFd6_-Dj8PgfUgmpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=YAiU097h87d-ebTagbSlYXGgdXl8fd7c5EtrliG-OOK2v0XL53dmnuAmucT6wSHyk9RZQAMRjJjuZxcxfzOlOg9wf5sNACeVoZmAul4Cv4d_crFcp6yKGi7yTC62w_in4T3M92O6smWvXR9OkYvRnUryRVui7eVPL_Zjo4UN1yfO7V9m4H74VSxwNiX6MDQgxyZxOpvkiz3EzcdztoxEij463L1lldc9q15OYsS9SzyEGrpK1IZvQOVdBbmR2-T0anBhL8vIgV3qggFRMALRFuqfYaQhcv4qqGb7tnbP27cYTTfN9pMHmvEMHIxZcBjyOOT53mFd6_-Dj8PgfUgmpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTQRXhvqNfLvioIWF3PjhFP8UVINgg2tSEQpR5sVpbd78aFDNCTsRuhQwm1u8vtkEnV9-54DZRvOcb180jZwo2pBNxj1TCC55Doiy4Q7fGXu80Jn1IhdSe9CppQkYsxm-tkmSjPRS-0_a_GyyV3tblLBsL7VjyeJUIOjswj0ZhSzzjVuqg9mnvJzIWdiyAzjcmrqnfJvPE8PfZ-pM5ODkOFPj_Qy6v6gd626hSCyghR4C-HrLA4PaBR6BAu2NqbNzdTwo6wYhPAKD54q0GsJeWweMOAZWYxOLNM6GJex4y3x4E2ivh7OJ3JUmTkKz2uUHArkbR5TQlynDvxuAf395Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=KhB_leca3QfdcNbWT8h9J6NKwUiJ9eHsNFirmW-vsrY-lzCJh4bXIPiihIbwndaWdA3A9bIsxS4H6nCzMjaAHQ98FZbJIJdrFmNZdCvyMiALhZKybeFuRqHRLwvfhFYcIH1-d8WS4dSBMY9c0aJv7jCm1T8cxGyCwbAprp3Y11nAr4MfCdFKdVt107RRXjxkEuQujPF_z9YtYZfyWWzZcw80-ggbWbMByBA6ZUq33eESsV0MBSHYwIdjqt5qjAH8TNycovRfUpIrEAdQpZSxMOzf9ylXX_ZDwup1-YugudsmaOPqJehJh9U-rBjNAwRUhjHXdOEIC3i2U4wG7q1rsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=KhB_leca3QfdcNbWT8h9J6NKwUiJ9eHsNFirmW-vsrY-lzCJh4bXIPiihIbwndaWdA3A9bIsxS4H6nCzMjaAHQ98FZbJIJdrFmNZdCvyMiALhZKybeFuRqHRLwvfhFYcIH1-d8WS4dSBMY9c0aJv7jCm1T8cxGyCwbAprp3Y11nAr4MfCdFKdVt107RRXjxkEuQujPF_z9YtYZfyWWzZcw80-ggbWbMByBA6ZUq33eESsV0MBSHYwIdjqt5qjAH8TNycovRfUpIrEAdQpZSxMOzf9ylXX_ZDwup1-YugudsmaOPqJehJh9U-rBjNAwRUhjHXdOEIC3i2U4wG7q1rsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByYiTd6EwSPKhRODVFJBOWAlg2KY-FtwBOxX6oqyQWp01ShXNdnkYKAWPs9gYayStwQbWsKpfcREocsi3oVqNDuuPmCVeUkArJOVNYAcoLSiT7KRJ1D6QaHeagS67_gb_uFKb6cm_GOtMMzWDTap6d0odeeAOAN6DiWJolbRINbBU2KsNKMZ1t6t_9Hr61NH-6Gcb-GyURWYX88O9-mrTImaiTKxL2lftocjtke2Hbw6r68KGcnvc3jAB6X--EdScU1tr2XmMaRN0mdJn0K6Hy8AbfXW9n5oRIymztF8N5lRYcCKuQjPkFVptQeeyntyRNhUDyx9CUGp3vVLLXQXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=epxx4mpa2ipCLizp3CtTyPbLoA6cqcoWr7lIcTpD5-IVU4qk_KBv_FQaTt9myqSis0TPAmHL3XnX6qDHBVsjO8bVQKcIr4YGhPO_SJjRRdoXzhyUBYflAemzjFwKK4udmn-prJYOnovjpvh8ilnP3gyG1VH70UVXn3ckKsekqzjlghy_u8a2093uK8K8IKETmByh7uIuG141XTRyebXZ85BhRQ3-sB2QqiC9jPec3YWlva40b385MFoNSc8IBnFsPyXHvjtttHFeboO7yHeLwydaHm7f_YFr-h2im5wLSw_RvE2YxnQpQ6LBrng8nqWnnCTr4P6dssqkRu67jbebmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=epxx4mpa2ipCLizp3CtTyPbLoA6cqcoWr7lIcTpD5-IVU4qk_KBv_FQaTt9myqSis0TPAmHL3XnX6qDHBVsjO8bVQKcIr4YGhPO_SJjRRdoXzhyUBYflAemzjFwKK4udmn-prJYOnovjpvh8ilnP3gyG1VH70UVXn3ckKsekqzjlghy_u8a2093uK8K8IKETmByh7uIuG141XTRyebXZ85BhRQ3-sB2QqiC9jPec3YWlva40b385MFoNSc8IBnFsPyXHvjtttHFeboO7yHeLwydaHm7f_YFr-h2im5wLSw_RvE2YxnQpQ6LBrng8nqWnnCTr4P6dssqkRu67jbebmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0SyKLjKbHTYivhULfckzU-dzY3UpkV3JVVKg0Hwy0pCedf72Cua7aNROw1dfDZIu6HCp9mBS9i-X2B8RK-_VEZHRWbQ5YWO0VvJP4o3eembUGQnimLz8-5SCvx2ViBIfCPZoiB7Nflny0mOwpqB79PN8l24FufuOeJoQdGvJ8ZDLov6pXBGOYTz6tUHO1I3mEyslml-6Q-MLwi5vMEXPO_C-NWMOJ1e_JEADRPQgyc44sd03ulStSKg4v9T8KTnVVsWfDPSlJPBRZubLZlrv1bpcDrCGdUMp66VGncZ1jrLJ92a7KbLDEgfmEK5XSn_Rydik9_4GS5xkEgkVTdJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=RXnOs0o136CYoP1R5vAoIbUnIgtEbjcqpf7_a8npv_IuA5t9-rhnrs41lzn450ty_LnFY93rBi3cgZMaZrqwKXciI8nhYzNOf1YNK6nzF4YMBa57i5leJXwmOa0uuEuNZb6cKJHd6MJt6GnZa9qJPWZEE_XWdcUIJ3UpGQ8aEmM9vHg-_66C8QYfzI7IF-22ETD9iaXy_TRdd_tbDGAt7S8Y6w3qV8z7rrTICzdnO7lQBnxK5gSJcUL7AcMvzN2SM7LnzeRlwK15rUdTwtmrBZZSEcXkJBf84vRyRX4JP5OIpXRxGo_bDorh7wEPC1YEr_7EknnVMVKPVbqTWe7caw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=RXnOs0o136CYoP1R5vAoIbUnIgtEbjcqpf7_a8npv_IuA5t9-rhnrs41lzn450ty_LnFY93rBi3cgZMaZrqwKXciI8nhYzNOf1YNK6nzF4YMBa57i5leJXwmOa0uuEuNZb6cKJHd6MJt6GnZa9qJPWZEE_XWdcUIJ3UpGQ8aEmM9vHg-_66C8QYfzI7IF-22ETD9iaXy_TRdd_tbDGAt7S8Y6w3qV8z7rrTICzdnO7lQBnxK5gSJcUL7AcMvzN2SM7LnzeRlwK15rUdTwtmrBZZSEcXkJBf84vRyRX4JP5OIpXRxGo_bDorh7wEPC1YEr_7EknnVMVKPVbqTWe7caw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=fbRimHbZALGWDbxCX2Rm54wJUExm-HR8uBTVlQrfTi6MJ3WTuXI4JOreaKprgiMNjHLT7TO2qa99qUVLUo0i1laSMfg_YiPjdBrHTeRsAUB8MxXFi-McxgkdQIPhPKD-3UCOax7dkyECPVVXbQOxhwZUW6a9RUrnXtpt2MpeDuVF1THITnX3swqyKKufZ76w51lO7sre-3J6VGI1vva_KmETMkYroJnQXn_rvLACL_ksflCRnQeDjSyNeJgWw0rYZnxbvKRgZX5P_IrpSd9fJ4xpCewJu2I4-WeCX44ml-zaOlhTwabVjk1B-MNoozLTArmXjBYOQ-207M_gyVA6sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=fbRimHbZALGWDbxCX2Rm54wJUExm-HR8uBTVlQrfTi6MJ3WTuXI4JOreaKprgiMNjHLT7TO2qa99qUVLUo0i1laSMfg_YiPjdBrHTeRsAUB8MxXFi-McxgkdQIPhPKD-3UCOax7dkyECPVVXbQOxhwZUW6a9RUrnXtpt2MpeDuVF1THITnX3swqyKKufZ76w51lO7sre-3J6VGI1vva_KmETMkYroJnQXn_rvLACL_ksflCRnQeDjSyNeJgWw0rYZnxbvKRgZX5P_IrpSd9fJ4xpCewJu2I4-WeCX44ml-zaOlhTwabVjk1B-MNoozLTArmXjBYOQ-207M_gyVA6sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=jrXZq6IsgPsgqE3xE2j9G9GmD-ewLNJRnnp2SL-k4zMUUERcvWuFQMrxodEEzVUGqk-xgYnnV7RXK6zAb3nyuGzAMmfxUJk49n8clF3CiZXt09OlCgorAqQK9g4gFK4_1SjNyDhrAlbEMQS2UCPVojeI9jlZmiwJM9SVAdyURVMZA8VhwnWAflUMRUbNx3j4AMtsT8lbFWT0cs5Pg-SZRK7KJ1vrY7AM7Fjpeqmn2UoyqgHpoZCksnenuEIzoIVW3clS-ZUvW7me8WGR1LJgM-jvc1tHOzlZXv6GdgY5M6CASr2MRBsIEAhy3X6OLNnSG-2b1o_jwwzniGNnVoPjEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=jrXZq6IsgPsgqE3xE2j9G9GmD-ewLNJRnnp2SL-k4zMUUERcvWuFQMrxodEEzVUGqk-xgYnnV7RXK6zAb3nyuGzAMmfxUJk49n8clF3CiZXt09OlCgorAqQK9g4gFK4_1SjNyDhrAlbEMQS2UCPVojeI9jlZmiwJM9SVAdyURVMZA8VhwnWAflUMRUbNx3j4AMtsT8lbFWT0cs5Pg-SZRK7KJ1vrY7AM7Fjpeqmn2UoyqgHpoZCksnenuEIzoIVW3clS-ZUvW7me8WGR1LJgM-jvc1tHOzlZXv6GdgY5M6CASr2MRBsIEAhy3X6OLNnSG-2b1o_jwwzniGNnVoPjEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll2Ezcx9CEblubGfUta4kWj8x08bz78Ki4rO0RFxfzXQmHbee3DzoPFGaHTzS5U-FNu1gecsVnEq9_60G0LNz2OMVERpC23gWwl_W0Zox1kJ953FX3AKKTXNdKJGqcihVjcyeMpKMzH8mX61CL9lQHlHGOdFwoRz0hyypYhTQ5IeSit4eaKwcuF3Ix7QVYfNStEbHTSmELs6TNEf5lNXyhzNpAhElSwsRldDnN5zpcrkBNSlsjy2yFhAs3mjuMWASXNvjWB2lxcjB59bpRYyZPVhlMQLAm8Wscg9Cb__0tPOiuhxpSlXYoOrfeMoUBxbePPMZOYyvb3J5I_VxIryEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trKb0xxP4OkKs0VtIh13vO-7yeszOyRNRXtyyxrYD6WApK_HdXZPhjxayILvH1ubWkNRu-YMO_wYrSHXaEak6YHFQ1aPsExjGPmM7NGqVTqy6hBPlmWR8RfwPcdD6NEPtMREF1Gv1fQd3T4g4FKDHr4UFVHHdf8I88KLHltP0yZ7X_nUcvLlTOBnFj6ggBxXh8il3q2UVZQjv8Pyn7TIjGB1tsudQWMdbLHkw-10ssgcQL_wikhusb6k7iTZbet61_R-R2Trj87qOPYJsDa3P2EanFAuAvKfTrai8uXJoolKg1-3Us61yQ6w0_kp0UEYU_Y6rYtJfyedq562QJdMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFetWFILtikEnQYtE8ipEbGgxj5mFzHIlub-9e4W7Ee77zzukSXXMWOE-ZyARoBkI23ZdZxXysN9FFmgejimODFA6xwuV1pO3DDnQi26fjy1FMJNH63Ic-WkGAlEYSFWoY1HcZbYtcZEzqevIjrRILPTVoz1BdctOQbT-OygpyW6zRTsfqiMHMioO18vv9fjxCiXOb_8LIXBjL_2TGzIYes0s1EGyK58RNlUJN_9y9vZ73NcGclK0dhJELiUCcBvITSlDpgGk3mBxt3l8xjVE74qY52jU7SYilvvHyOff0MiRwhGxf8fD6xPzbP_yy7fqhOkbC0Ks4xeYBVonx13aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=NoVaa4VsHxrCH77FcYXiV6_CPKyzpEb96xQ97zPLbn6lqXll8czYA39UdfVNvNo4dhFNZU_qnVIMoXK6I_jgRZiXRuXbKf0UafG7rtH9WgSXChUaFiKTivE8-INWcZBgHKi5kQ_eC8KSZtxrXlgP_9j4epxI_8l00DaNItBzicn5NFFHtu1zHp59dLa1sp6T2hdBVLM7T3r5VN7f9o4yui5ldSbk7wN9kWpLF4x1tBmWOQRmPrwEFbtTiRW1DquD4jM6IQ_9C7Jb6b5EAF34qhDBWu0SMQ36BmFDgKHVqzr8_nV_3qfF9H_59F2EwNHJv7uJh9CEcs6ZZ9mlcJK-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=NoVaa4VsHxrCH77FcYXiV6_CPKyzpEb96xQ97zPLbn6lqXll8czYA39UdfVNvNo4dhFNZU_qnVIMoXK6I_jgRZiXRuXbKf0UafG7rtH9WgSXChUaFiKTivE8-INWcZBgHKi5kQ_eC8KSZtxrXlgP_9j4epxI_8l00DaNItBzicn5NFFHtu1zHp59dLa1sp6T2hdBVLM7T3r5VN7f9o4yui5ldSbk7wN9kWpLF4x1tBmWOQRmPrwEFbtTiRW1DquD4jM6IQ_9C7Jb6b5EAF34qhDBWu0SMQ36BmFDgKHVqzr8_nV_3qfF9H_59F2EwNHJv7uJh9CEcs6ZZ9mlcJK-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3bwmQDJNawvn0zt3-H7xzaMbZkDMJ27UaWJiVMHmtyOjvhFRd30xVbC_qq8S-cN55LMd8gba9xflQKKO5uH9Bd9dNvXTMs5m8QiaUOemZGfPBYChn84fh5C-MGkqynGY-YsJJ2-uBXK-aGygTJKX-NFZg2J3mJda8Zl98SZvSXdZWG-5kmDqnWdvXLIi7I0guyaoydDYvF1cjGTF_ThTwQ9NXC-NjKLFgE4sdZkYmPbOaJ4qCNflPe6JHL4ndvQqQkBSagvDg-MWym9AgP1bo1lJmv5kYLQE_0gwe2m0ck2mm6TCI5d0aXZFbqMqhCJjHO5Jbz5jWguBO2jbLPyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=YePoiJ1EQlpvSk6YQjYXiGQJpY55rqZEVQGpZkS2Ryl-TAyf3ihPXFlppmm5YeNVEsjUQ4mrP2p_0knI4Lzp8SWpfinUa5m8ZNeBhys5tMxrvOOnjOzLs2vKXBwkzPT0t7wBzXWXdinzVJ3O8uBFoc1FSdGINS-Y8vSrQEMTRvUgyO2BQrasS0i6R_GRp0BXBPVgOFo6B0GEfMwSPq3kTjtyZjtuTXNpMN6OjdpAv3iySdnYuRPnrellWjKmqYjp-ZZpwhnKKWt3BV9ibrvguduUEP6NH9bzuKV5Bm5PALshn0ThDmbZFoWty109PTaFiVhvzCwp2cjxZKlibOYX_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=YePoiJ1EQlpvSk6YQjYXiGQJpY55rqZEVQGpZkS2Ryl-TAyf3ihPXFlppmm5YeNVEsjUQ4mrP2p_0knI4Lzp8SWpfinUa5m8ZNeBhys5tMxrvOOnjOzLs2vKXBwkzPT0t7wBzXWXdinzVJ3O8uBFoc1FSdGINS-Y8vSrQEMTRvUgyO2BQrasS0i6R_GRp0BXBPVgOFo6B0GEfMwSPq3kTjtyZjtuTXNpMN6OjdpAv3iySdnYuRPnrellWjKmqYjp-ZZpwhnKKWt3BV9ibrvguduUEP6NH9bzuKV5Bm5PALshn0ThDmbZFoWty109PTaFiVhvzCwp2cjxZKlibOYX_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9ROjH3bJ9HvP_5BwjqtFYF9eczaAcNQIY7tPcj35Ayn4r3RSaz0Lj0hW0J3s1DcdCmLSdPkeZE3i71snTVfJHvsSLE3U75rzxc4ahlR4BpDa9FMdNCzh6r2Dm6rDgopbACItk5cdlcKBrShBgELBA98kPsuuAKlXrBZamqPsAl0V2XgBxSp7GWKL2AyXSbG0Vu3lFVeWuXRmKAEO4G6MzbLKGHqTE5VMEEIkN4EYotw2gYynUtIuaJBIcAbzVsasRcej01txld7ltUvhiV_7H72It47rE9no3ffQ37vQUHiKZL8K2gKts0BodBRG3jUYpVZQBx_uIRL2iGBgIvqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
