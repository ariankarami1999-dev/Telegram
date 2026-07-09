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
<img src="https://cdn4.telesco.pe/file/hPcx50AwDt5oNyv-C_yvlUfVjEgdqDRbv_QrwAAkl-mneZLe9IP0LG2O38v7EDn1w7TLvERJcewgzIAztRBXGIUEw0SkNN_zKHE9T6nLSD4UYEXRNJvk22yBrEIqzTdxaYKVt8GVghqnph7Na9fAyZ40luWZdggqdHtNXblQExWQdEe7k8zQlJQ-JCHCtByiDxwxcqOe65wWCMzs2-7rM5ce9AEtrkadXi7On-XvPzanoaoWX3mAZWZTxvY_FnWbSTTFtgOcoyzhuJhQ9XGWdiryG4HGnGPYX7MEqE_tcz1bFGwlag5Le3L01kxZ5urtmEnRTfg7NmTSdvQiF_EV0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 190K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 22:35:41</div>
<hr>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWxWawQ0Ovw-PxGSuTXEwf_9VMSjV9VgNi-rTZlayTGr_IbY0zedIMUGvW3rOHxPqCqC4Jsp62JH7D4MgMYl4WsAwagpydzUDNX-RsajCfecl1PZ272p1EqiYRIRfRijSL-xk_FCd2vfl6fY0lPWe98OHMUs3bYDEMq3L9PYzjNFGpfgSQm9dJFmJ0QMfrYRJ8tPDfeCCen-lbne90ekXlRH05IQo2u4plZj6edwbrk3mXx_Qqb_VVXi_gKVi6Cpgf6JHKfwez4eUYbpvn-4r7zIVyR11JtMqeqYLVaz1Up7bjmhUaIrvQPYVzOBAvwiff3EayZyU6Kw4UjlGJ6Beg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=QaW-g3NV4rfxIHm1Z53lTy6Bjaa20cz2Jo4688_pQaWKagGvxtUF-E40iHQjDVz8-sxOUMht7V4yKlXpK2couGWut1ARxBFBO05fNGOupcLHK4zak1X6MKl4OLQEF9Ji7lC2bOmSCaGMyfcSYAP1qplVLychcQrRK_beiFIngX_rI0CUV8Wdp-CnWhVRISKlYzfigB8soNIcbafcewZd9M3ue4rgINLI-qyZOW7f8jmBUuc8ag0RjQiwCNHJkORQtxFD4vhjjjtJov50eInw5dWfxsJf9b9vGRxHmB4X9T-upmmA06yyBm7kZuopUPXE1xWP0GeESt6hxctCK4cfqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=QaW-g3NV4rfxIHm1Z53lTy6Bjaa20cz2Jo4688_pQaWKagGvxtUF-E40iHQjDVz8-sxOUMht7V4yKlXpK2couGWut1ARxBFBO05fNGOupcLHK4zak1X6MKl4OLQEF9Ji7lC2bOmSCaGMyfcSYAP1qplVLychcQrRK_beiFIngX_rI0CUV8Wdp-CnWhVRISKlYzfigB8soNIcbafcewZd9M3ue4rgINLI-qyZOW7f8jmBUuc8ag0RjQiwCNHJkORQtxFD4vhjjjtJov50eInw5dWfxsJf9b9vGRxHmB4X9T-upmmA06yyBm7kZuopUPXE1xWP0GeESt6hxctCK4cfqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=WMLwk3xuAiKftyyox8gQELvCoIxdxd9bBQU_GZa4LP8ACcwi24waUoGiwQsg6pfyE9jMMRNlneFy26sO0Pem8iIMhgDoCKpByUf17bZgLHrO1g1YZZ1a1z59fSEZ1g9g9nT5LpkZmjrhntU-arebO5G0nSfHGo7YgbPQliO78Cmsn6Y-NbBCsXaFubs2fcpPqSFf2s1RNjH_TtngCmHGADOxsU-EyO9i1dSqSo9Cr62b6vwmbZnkY_xoIyO3DXivvuNCVJYyipytbaLA-7toLy0sSBJvR6EfzxbarnOIImtyxVwkCC4o1DCMCuRQMwukkk8bO_VPuG-CZ4uOzkjx5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=WMLwk3xuAiKftyyox8gQELvCoIxdxd9bBQU_GZa4LP8ACcwi24waUoGiwQsg6pfyE9jMMRNlneFy26sO0Pem8iIMhgDoCKpByUf17bZgLHrO1g1YZZ1a1z59fSEZ1g9g9nT5LpkZmjrhntU-arebO5G0nSfHGo7YgbPQliO78Cmsn6Y-NbBCsXaFubs2fcpPqSFf2s1RNjH_TtngCmHGADOxsU-EyO9i1dSqSo9Cr62b6vwmbZnkY_xoIyO3DXivvuNCVJYyipytbaLA-7toLy0sSBJvR6EfzxbarnOIImtyxVwkCC4o1DCMCuRQMwukkk8bO_VPuG-CZ4uOzkjx5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=elWau506QFEJAiT0SPJbEXFGNZsywnVeJAnptdFuUBPEW216XY4fHXAq6insvDwdlGhjs2breFjmhyNYqLEE9uvvWP12d63WLezsNgwfMjPvTltZ1pEDX-qnCvL2wJJ9iQrwrefaqagXxuxtZ-enAS2ixXH505F3ZMsxJMd2dfIt5KFs0QL32jM3mdVHSgD9yYnZ0ku8phFQfzZEgEt6wrenecKLR1QJmnK6elVCaIZvFraq9YS_Sm5lLJLr92ZLvcuZabKptyZBzbFQBbRW-yZXCbH8lj3IecCL-hbybw_6KweGwvT8_8XZzjcOFHwTdE8K2DCHqIvj5TdpOeHINg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=elWau506QFEJAiT0SPJbEXFGNZsywnVeJAnptdFuUBPEW216XY4fHXAq6insvDwdlGhjs2breFjmhyNYqLEE9uvvWP12d63WLezsNgwfMjPvTltZ1pEDX-qnCvL2wJJ9iQrwrefaqagXxuxtZ-enAS2ixXH505F3ZMsxJMd2dfIt5KFs0QL32jM3mdVHSgD9yYnZ0ku8phFQfzZEgEt6wrenecKLR1QJmnK6elVCaIZvFraq9YS_Sm5lLJLr92ZLvcuZabKptyZBzbFQBbRW-yZXCbH8lj3IecCL-hbybw_6KweGwvT8_8XZzjcOFHwTdE8K2DCHqIvj5TdpOeHINg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6wBP70QzIv4-hqBWP2UihMLtHDHPTa6s2n8xelomfrKH89OIFfP2YEpQ0dEBGw4eBdA4yoyevz8FZjzhrc5gmY997qQYmKobRqM99mm5dNY0OuC6UIZHgHgsI5-amg5Np-a0QsvCg_uAqDpH4JzUYi1WRFhVBDs47CD8qS_q3WL7cJAIr3ngO_spgtLF00C0R5Mjvf0NNNhGnPS6zuJ8tGmUlrVinbFso4XNmFwev_353bcpKOk8HXk0-ZYRBZgFIesVM77gkwbRDo-TIcv-LHMZPLuJxw0N9NyZKjMubSZfGkty8T24DG22boi9Mi3R6RQftxSFwGwfjIq2i6BWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnRlNF7r0qmvGefJ0jcj1MBTUoGeWIOst4p45g017v5dvorNe5ylcsJqJycJMxJp_Mu33f_3XPMNE5x4C7lr1Ug_6awXsg_CXcheYw3zd6BjlyOrtwjzyqmkKPwOMdxeNcUX68YTu1LDnW14iwi103rB-aB1FAO5GO451V7T7VoNbrKqVsC6iLN7ucdJtp9LDzLUVp0zN3Hfeugl9TomTBNOJ5kGZWkmkSxvivIR5-OUJdzGpl57TaDDM7B7gTjqlKn5Bk_PC1XbBbHAa3oW0fmqwopl8oCrWEp03zC5a98XksMi2wb2vIVBV3jgN2Iv8161i0jbX4879hov9YB0ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=uMRjdrB8tWYqCumsoWpo2UOk6LRWjKIK3agtU62AzI-5XFtOjgA-rig0SEF7BYJQlAutItrg1EZ68MyFOy64fE798Yh7NKaW4okKXEIzMGQkrqqJjHRhtC7G3Cnhi7irdRu17xk_4CHSL8MDpgn2fUDRDYUOHAsvRRr4XuDvbldr81dv8icUQtx0yzDMoyORWr5w3uWZ1r1FXMx0eL4Ud4OBfssyyrUcKvdnmYlMeLy8_ARDwcq_SF0l2gUFRY0gv3sMKZ7fPPg1ARCsNTt3h6kzQYCI19kp-FcfC7CLhh-JSY1isWVmZCMuugO-FSvcr7a2l0y0xbQS2BfKta1zLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=uMRjdrB8tWYqCumsoWpo2UOk6LRWjKIK3agtU62AzI-5XFtOjgA-rig0SEF7BYJQlAutItrg1EZ68MyFOy64fE798Yh7NKaW4okKXEIzMGQkrqqJjHRhtC7G3Cnhi7irdRu17xk_4CHSL8MDpgn2fUDRDYUOHAsvRRr4XuDvbldr81dv8icUQtx0yzDMoyORWr5w3uWZ1r1FXMx0eL4Ud4OBfssyyrUcKvdnmYlMeLy8_ARDwcq_SF0l2gUFRY0gv3sMKZ7fPPg1ARCsNTt3h6kzQYCI19kp-FcfC7CLhh-JSY1isWVmZCMuugO-FSvcr7a2l0y0xbQS2BfKta1zLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=S6t6xI7g7cI1-AjYfsUypYZ2ws2vc9YLZGLt7m23LhT3zWK7zxmpi4a5jLCoPuyrvU_Nb3ukFOidUDwrrmvN4f6jou2NJqyx8zJoxjTwy6LDESNa9JGf6A9phrrv-Q0EPASJ2R0_qWuM4_Ah3-0BMnI20gO0o4Dw6tkEtOrpPB162oOX_ihEFAu7PCwz35buE3HbXLwyBPmgLQScI18t5K0TzoAX_LDDdEqYO3l-YtYUylCr8bAeeOgzesQT9H0c6tmtf4HUAooR5tzVDnbw9dLGvsNzOhc1Re_5mpgIU204aWv52Lsqma0RZ9pNHzgfibl3jMoPaMUESxeQVNofrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=S6t6xI7g7cI1-AjYfsUypYZ2ws2vc9YLZGLt7m23LhT3zWK7zxmpi4a5jLCoPuyrvU_Nb3ukFOidUDwrrmvN4f6jou2NJqyx8zJoxjTwy6LDESNa9JGf6A9phrrv-Q0EPASJ2R0_qWuM4_Ah3-0BMnI20gO0o4Dw6tkEtOrpPB162oOX_ihEFAu7PCwz35buE3HbXLwyBPmgLQScI18t5K0TzoAX_LDDdEqYO3l-YtYUylCr8bAeeOgzesQT9H0c6tmtf4HUAooR5tzVDnbw9dLGvsNzOhc1Re_5mpgIU204aWv52Lsqma0RZ9pNHzgfibl3jMoPaMUESxeQVNofrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0FvGELUSCcSJpteQp36i9AOuDjVNmRyCsk-h5t1bGAJdqjsZH2uct_oWr5QuSPvwG8VUWXMloMpAbaGUChzW7ujZauxRDVJObKOqhF2fzd1gbsyYzhQuGw4Etu7zqP6p0XL8ZJKgNZv61fKsdZsdp9_3xvnkrNdBYafAFLbC05znSuPgK8sanJlvhuhC8lIdlfYV_ehssjG_VrCuc1f_OqkwhTkowW7KunxdbJFNzqW0LtosYVc_TN64l1Pm6m0EO8lgVrcxAn5BUlgE6D73UQd9AgUBeQHwmH-BeuHsuG7phG8AK7p5E9G0eIxq6K2tArKz59abPXUze0-oZ9NoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apScyXHgDXrS16eCcrMGyPbSIrVWRjwc5eKVpMUUR3JXcms9nvDebtKHAxRc39tIzm4TCTzrYeX758BGqxjXnFcJm6QiuYX08fePAPz24S5eq9j6DVgeRZQc-7BV46o0S8GJvPUDFq9zQqppgKYWsUSW3PFt6fN4JcxEviDwyo5d1Z89R4eyhTPRy5-BQ_CYVqQI0NVskDfSd1-Tsi6gcExg1CgwWjorMI_XhECtbVCitchf4Lov0iHQ-NZbEVxzJj7zFoaCmqPcwZKM4wjLudIrZ0gAf93mmVTRWoamWUx6OZZMejCI9u-yPUOzi74tOlWCnY3r_NYMcoJJ0O30qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZY4oboMFvjLVqVP0pKIsDILWHEbuDjgIJFB43kSFNyI7jGg3SeW-YgGKXJYIoRdPeXZsomwzYuAOeGe5482s45BfENdzayk3NSHX5xD462daeZuQEj-Ct8TtdbQZe8A89am4lCbq41RYhG8M54M8vTf9nirgltVr5alAXtORDjtM2jxnXNaqu69f_JWHoKWbhN5HdwDCz1xL3rp4V8enRmJc00YaucezQeX3PD-kWQYM0BZO9Zbqv7gDGMG5krzKx3cnDddT7uRjhrIG7NMeD8_8Zdjz3it8m8EcagiuIW2-0iRhfbnSnP1J5hKypMd2Qk5mJ5FXL1rF0c8jRqXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=hruGgHfNi21826GJqG_7lfAQX2bDWjjg3mijMbo_6M9Qtaph7Mo5iN1EzaPzFUgI6oLkJbXhogqhsRBMI_UI-thswvzUx14v6BQQ92pC65zs0z3Xpj-xtwu12tDdpCGgbW3lITMY2HrhvOY33GPoxwRMEKvnCYQDSOT6pJrLmmNk1qo_dc8md3d9u2VM6n8pV5h0NA5x3wPcJ4z9oj6LOz_QuengRfcyYKqQHv8AbBhvOSUc7bFbBXcOEtHLhSTVPuNj6mnpsAXrVHWKzeRzamRT2GN7dZ1h6kkMjBX7ZtM-JRrxtJV3STKyUGA8lHmxVm-wqn4kEdUAokf19rUXnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=hruGgHfNi21826GJqG_7lfAQX2bDWjjg3mijMbo_6M9Qtaph7Mo5iN1EzaPzFUgI6oLkJbXhogqhsRBMI_UI-thswvzUx14v6BQQ92pC65zs0z3Xpj-xtwu12tDdpCGgbW3lITMY2HrhvOY33GPoxwRMEKvnCYQDSOT6pJrLmmNk1qo_dc8md3d9u2VM6n8pV5h0NA5x3wPcJ4z9oj6LOz_QuengRfcyYKqQHv8AbBhvOSUc7bFbBXcOEtHLhSTVPuNj6mnpsAXrVHWKzeRzamRT2GN7dZ1h6kkMjBX7ZtM-JRrxtJV3STKyUGA8lHmxVm-wqn4kEdUAokf19rUXnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=FSC-fCBzdF5xLPb86Ic2hLt-Sr8P9kbpLecXY0zhNFcWG1oxV_0QeaFL7xmCiod2sirQhDIFvGHd7EyR4XrJWMgtdyeNExnVbOPbUBRgZllEV3yXTFDeKsqPavM1q68wOfLM3BwKSuR69IX9WoMOD6BNyoS1Vkrk6MD7lepDkr-ODcG2Y8cnma47SAmuas_5ctQoez0frwfo-uNdV_7YEDSAXw6HXFMyWKSoc_8DldKZsiTUNZ7SHPmNRrHe6MHCk88Qj9M71V6uBvVs3ehO-8YzLHAQ1ANbmPKH7U-wmOCT1HRMOfRZyaA4n-rV6n4zw-XrEqU4r5rkKppVRoZRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=FSC-fCBzdF5xLPb86Ic2hLt-Sr8P9kbpLecXY0zhNFcWG1oxV_0QeaFL7xmCiod2sirQhDIFvGHd7EyR4XrJWMgtdyeNExnVbOPbUBRgZllEV3yXTFDeKsqPavM1q68wOfLM3BwKSuR69IX9WoMOD6BNyoS1Vkrk6MD7lepDkr-ODcG2Y8cnma47SAmuas_5ctQoez0frwfo-uNdV_7YEDSAXw6HXFMyWKSoc_8DldKZsiTUNZ7SHPmNRrHe6MHCk88Qj9M71V6uBvVs3ehO-8YzLHAQ1ANbmPKH7U-wmOCT1HRMOfRZyaA4n-rV6n4zw-XrEqU4r5rkKppVRoZRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=SEAsSICsKnB9YEoOL8vK4kjcYBfbt5dXnh59je0Sp8T9i_Lbq9vFqXgUqP2cwqgA47WAVSYxUdqAADVDrVoUG42E0LwU5gAUqb1eGzyjkEx3WVAewSh3oiKQVB1qLE-lKr3bSsWrcAXT4XifviFVbOwPZShMBiPd5inJZuDyvl7TQtM3IAFaAQMLf8og4OjEeXnU4N5h2egtZBillqY9y1PYnk7y-mGGfHUwtLz034RNqFO35R2_VXoP8YQMz1nTAcr3OzfLELGsmIFUXv95UHgGp3KbkKP33rir89dCRmFQ3ZGJbvQTwc5YHYnf3WVthefgzmcC3sJDigK02FsRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=SEAsSICsKnB9YEoOL8vK4kjcYBfbt5dXnh59je0Sp8T9i_Lbq9vFqXgUqP2cwqgA47WAVSYxUdqAADVDrVoUG42E0LwU5gAUqb1eGzyjkEx3WVAewSh3oiKQVB1qLE-lKr3bSsWrcAXT4XifviFVbOwPZShMBiPd5inJZuDyvl7TQtM3IAFaAQMLf8og4OjEeXnU4N5h2egtZBillqY9y1PYnk7y-mGGfHUwtLz034RNqFO35R2_VXoP8YQMz1nTAcr3OzfLELGsmIFUXv95UHgGp3KbkKP33rir89dCRmFQ3ZGJbvQTwc5YHYnf3WVthefgzmcC3sJDigK02FsRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=IavZ4JrrdRjZF0XIgwClSuopoCXKVxhkxTi-_rp873lKd-V3vSJ7ERln7jXeAfNNJOT_a94BV5ooENRvmWkqB1NOHk7SLAvu51gn15E7yjIauzkINLYqzCBIh5i9mAGB-4xS0a_6YGbRM70k7fZiKjpBcfzPA72j_g4xOrmguDurTRBbOLJoIKcLSO0NPGMJrJCepYJAp9e42S32h0Hr0NwmUg1OJ4cKaNRhfvCfVqTC5DX0TvE0LwlqcCN9JxEQz72EwB_R9mMpIbc6GKlBUosC3eY-d9Nn99aKGTObxOaF2D63ZwiFcm1tHgpsJUUIth1WKMsKJ0Q1slat3MfykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=IavZ4JrrdRjZF0XIgwClSuopoCXKVxhkxTi-_rp873lKd-V3vSJ7ERln7jXeAfNNJOT_a94BV5ooENRvmWkqB1NOHk7SLAvu51gn15E7yjIauzkINLYqzCBIh5i9mAGB-4xS0a_6YGbRM70k7fZiKjpBcfzPA72j_g4xOrmguDurTRBbOLJoIKcLSO0NPGMJrJCepYJAp9e42S32h0Hr0NwmUg1OJ4cKaNRhfvCfVqTC5DX0TvE0LwlqcCN9JxEQz72EwB_R9mMpIbc6GKlBUosC3eY-d9Nn99aKGTObxOaF2D63ZwiFcm1tHgpsJUUIth1WKMsKJ0Q1slat3MfykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RupB3tBmfu-IFHaNW_mstZDYGIaXuy3J2xrXe-K7-Vsxkcn6ZS7lVqSYNayDU6rcJodHiXcQs4hjyH9EmYjxCqEXvYROOjVJZ6r-RNO91IuRlQxC3mf4lYaM27ImztrqJFmsalk_4Ez4ZQJjY0w30UAcBC78phGCpq_niFDCR0vGDj5MLpf-r7aBIBZmFHgF32G6-iuZEwSHqpI4qLlcSYQLwlLivVU6-5AF0r7R2OoE0LFqqEk2Zqov6-gF4fePNzm2Fn0LLZYyFin_Tyb5AluhbOQAv1jM5kWyBZbLD-gW8WBz0iA9B_D-yiqdcqwR_sFNUlswem3EUI0pda_S-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=C-MdvsEP3R8NRDGHNlrFvWaK7-IqPqHjBmYfaielEGdhTZKyiAfnwN3tHxP_CJmEbMWBG-dFVqiDUpfGZwGQmqK0BMwrxQNyu6hx7JUU1Sbb88bglQMCU__jFScdOdWNe_diRRnjJ19oeWaTNdm0drrGeNEf_W6g1QlK2amglLai-APtHyNmzy1z_vVxZtjW_rCxWGrwXgLBMB6ceM215gGElNuG3jH8109OxXWemC-R3OqaY6KOb4HkvAt4QCC1FSikR_2wGNR-ZLNzd2sgRUhZzXUq8vLYoAMf8lxZpXy_em1TSjdt_D5jiUDXk8iBgarjAN0H5XhRZu14cQKogDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=C-MdvsEP3R8NRDGHNlrFvWaK7-IqPqHjBmYfaielEGdhTZKyiAfnwN3tHxP_CJmEbMWBG-dFVqiDUpfGZwGQmqK0BMwrxQNyu6hx7JUU1Sbb88bglQMCU__jFScdOdWNe_diRRnjJ19oeWaTNdm0drrGeNEf_W6g1QlK2amglLai-APtHyNmzy1z_vVxZtjW_rCxWGrwXgLBMB6ceM215gGElNuG3jH8109OxXWemC-R3OqaY6KOb4HkvAt4QCC1FSikR_2wGNR-ZLNzd2sgRUhZzXUq8vLYoAMf8lxZpXy_em1TSjdt_D5jiUDXk8iBgarjAN0H5XhRZu14cQKogDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRz7vVKslJVLSYB6OfYBY2N-jzP0BN2gYFQD7PR4tMg3n3SsF7oh0B6Qkw9HJakytuIReoxPPr4Wzy-paMAaW8M7yP7F-ISqgcYw7avYF0STCF1HpzcGbZMr3x0o5SPK7NyCd1R6eXrwRsek2IqHmfBD2OnqODHy4_27qXwff517b6TJy7bB3kmMTWMXa7p2UwVR6s2jMOsTFr7-6w0tjMU8Fg0rT4N3AjAe0MkWfEl1zbbshivCSvbCHch9lP4q_4nn8RdyjfZlGnZGAyH32_pEPTJpVu_0okcobYwCqezziDg413Ga-MV_Jw9l_ycWwm7p75KUfKEd2OkTQEi8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8w9KJjUe30YVEfPHLbRoPb_h9B5ee3LJcVvuv6-GZBgoLUTMtPVcXRONF3T5NoGSisMpI4pg0md7qyr7clYceJgUWjgB0R2nPTIvHiJcnnhl-vOLrIiXkLGvmkig19c0k44OsLoaNnmeDHJGQr-HLaT5tW5ZwFEum_ZoPM4-gIPtqxOK3nVxww-KlBy3RnDcszpSGmHktGkZwo5lMHDSZefLNETEbTikM1h_wAUOv4JSY_wloZNYOq39QA2gkIr-HIn7D4joywmbpbqEwqwz42wuuFi9MBRGYaey9yiBYtL2tdNe8SAlcMdGhUwsTwU8fzPG_aRvKdqTW0galspPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB1zQEefpOsBcqMA5CvFu0XIcwdsyuxorU22IXQCuwcjFodsZg4MJ3wLB4L9mGQlW9ti8nAkWq6DvhiKvo4ZaFMf_p_dFwhTUhLy6wicuSRO9lwxOYgdVoNF2u81lN6fBEOvnFUuqmxWeyj92-pUgplHJYuunHW1MhUIXus1ZyTpU6c38zHLbVGie6mk5FWPY2TobR4n0TrdIq7NMA1vxSQqpfMFQbryxEUSFM5cAkYCvQmxpu63jvG5hcnoVYlAdzTMCgu4V7DCVKgFolylic5_zKs4n4aionJI69I3YrsMIQoFA6H4KoK4Vrdgm01RuEgZ4Hh359yxBsiukesx9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqIrv6xg11mmymbkGNYklRBLXp_lcK8p4RlfTPqEibIYVzm-zyylU-Ya_HydSkJ0tWLJ7Ju_jEXH8lZK_A5_iQBxMbIEITSu0KSg5ZRRorqJbppYDDDxXPEDUcRvyXcKjp3ccQKw8HqXOJMWuLdWk3xtMwNv0u6LaoRLIePetJZWcX2tXqK-zcSanbnv2H1Zw1gcTxQMuUDOnJy3x-ED9IarNNpitf-I5uI40ZAdJNNs8UQ7T14wWiiizqq7sUzQxm_BJeSSPmkmmTSvVJwFP0bKMPLqCFzaTIxkuMxg9Z3whl9e2WeZ2LTt5f9OgqWy0uNq6FyrltjATR2ymsoEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=FB9p2HzXDJAT_bHkXJjTrIZYKCzwj3078-T8NV5aySr30nqZ8n2eZnpVO6ts2wWtqtpc0h2L7Njm4jHDqSc8xC7CdMVAWkAZnqyK4U_kjGe5k2t7-0ypi-tjGLeUQSNXRanQ-zfkLQTDWwiUhMB0x35gNcsQMeTfhezCNUmDQZpJj2Kokz22Lw1ZPHWuhHRpTzPYZ13j4W_NoyKIBGemHaoz-ACkIkICcEKRSTGPyNk5b89WrQB1MX25CEB0glOAjO0Y1520hwI6-7K0wEhgrh-Gb7PI75D_UpdWWx3sZ2TEE3YfAUXFhxePae3shUGruQz5wyiAkyZUCn_TKxckOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=FB9p2HzXDJAT_bHkXJjTrIZYKCzwj3078-T8NV5aySr30nqZ8n2eZnpVO6ts2wWtqtpc0h2L7Njm4jHDqSc8xC7CdMVAWkAZnqyK4U_kjGe5k2t7-0ypi-tjGLeUQSNXRanQ-zfkLQTDWwiUhMB0x35gNcsQMeTfhezCNUmDQZpJj2Kokz22Lw1ZPHWuhHRpTzPYZ13j4W_NoyKIBGemHaoz-ACkIkICcEKRSTGPyNk5b89WrQB1MX25CEB0glOAjO0Y1520hwI6-7K0wEhgrh-Gb7PI75D_UpdWWx3sZ2TEE3YfAUXFhxePae3shUGruQz5wyiAkyZUCn_TKxckOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=ZcsnWb2X9asH2IS1YfzsTTsFpz1AXu1aD1kBIJBuQFncC_l4i45G-OBiriA4cOPAC6NRiPPxwTzvHszVp0ClWy4FCus6haf4M5ioETkKVxgfLy6XSAyYsfZSxR3jfDL_uv_3ZXzO4XNuOjEvM7sUgsngMLdMJ1NZKDYyrvLMgMRH8AUed-CENzWFJl5xjnHcaI5fgRuSgo_a58s-QxoTeYOoeWCwjdzBe-u5iJNSKsijQ8bXMgPPdiuP-Co8eI6zkqDFa82NBOxE21X-D488P2pbPP82NLaRIi8veoag16IlR1v2g3byj-isCSodCA6aFzNrHgpewSv9My5mmRlPB5G-lW09QfJ4UjWcY1CFdD-ITTzQAQCp9g5OrSESw2s2agkj_YTik0nONoau_BCCfVgNgrgdlnVTcNO6DSooxQ3CcseTf7zbz-x5eSSNG0zwkuvCeJeIyfsuLQWRk614d5hUqbY_m4KgMUOidZ5yAK7CD8mKZ8XtMqLTJPkgfsB7I8d00oiS5mCluMZX7-SJOo9ykSN-JPUAyZQn04it2WVEUduubh5bmx1PlMzktN6oBSfRrJ8V__byi-9H0V7KlkYBsYtq32tMnyFZiKGHwJWyslNXQHqYveekMPegTMNYHuOIVLGNDV4NDBE8CTYEi0QHsWBrAiBOV5mnJokYf88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=ZcsnWb2X9asH2IS1YfzsTTsFpz1AXu1aD1kBIJBuQFncC_l4i45G-OBiriA4cOPAC6NRiPPxwTzvHszVp0ClWy4FCus6haf4M5ioETkKVxgfLy6XSAyYsfZSxR3jfDL_uv_3ZXzO4XNuOjEvM7sUgsngMLdMJ1NZKDYyrvLMgMRH8AUed-CENzWFJl5xjnHcaI5fgRuSgo_a58s-QxoTeYOoeWCwjdzBe-u5iJNSKsijQ8bXMgPPdiuP-Co8eI6zkqDFa82NBOxE21X-D488P2pbPP82NLaRIi8veoag16IlR1v2g3byj-isCSodCA6aFzNrHgpewSv9My5mmRlPB5G-lW09QfJ4UjWcY1CFdD-ITTzQAQCp9g5OrSESw2s2agkj_YTik0nONoau_BCCfVgNgrgdlnVTcNO6DSooxQ3CcseTf7zbz-x5eSSNG0zwkuvCeJeIyfsuLQWRk614d5hUqbY_m4KgMUOidZ5yAK7CD8mKZ8XtMqLTJPkgfsB7I8d00oiS5mCluMZX7-SJOo9ykSN-JPUAyZQn04it2WVEUduubh5bmx1PlMzktN6oBSfRrJ8V__byi-9H0V7KlkYBsYtq32tMnyFZiKGHwJWyslNXQHqYveekMPegTMNYHuOIVLGNDV4NDBE8CTYEi0QHsWBrAiBOV5mnJokYf88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=by_qLuAoLy444ditUoIzDFVt1LNl8JJShN5x6nn-7RJlpn5lIyMpfBYOLSFW2ZTZBg4regShUAo-g60nJprqMLAtl1UoD0piwgMy0brK4jxwI2hO1eu9oiVw53tk3yarSSfQzy5_RNqZWAmifdRJAXAgImTv_ZvwsKvai2dqfEnlp-rWSt8pxJZVMcraZARU1tE70Nyl0N9i24bSCTcRsvCXtProFFwJOk9Lp9K2hGN0WU5H-fgU4xGR2ge5SNXPs9Z8KNnHJM9dwSchDdqgoNrsME1mUOECvqgbOnQH7B8sJx8pAiGYzS-WSwmDHw62aEtwKDHU2jiz-z-ZJctAyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=by_qLuAoLy444ditUoIzDFVt1LNl8JJShN5x6nn-7RJlpn5lIyMpfBYOLSFW2ZTZBg4regShUAo-g60nJprqMLAtl1UoD0piwgMy0brK4jxwI2hO1eu9oiVw53tk3yarSSfQzy5_RNqZWAmifdRJAXAgImTv_ZvwsKvai2dqfEnlp-rWSt8pxJZVMcraZARU1tE70Nyl0N9i24bSCTcRsvCXtProFFwJOk9Lp9K2hGN0WU5H-fgU4xGR2ge5SNXPs9Z8KNnHJM9dwSchDdqgoNrsME1mUOECvqgbOnQH7B8sJx8pAiGYzS-WSwmDHw62aEtwKDHU2jiz-z-ZJctAyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=iLWBzguLQqD-7Hapi30vsXhU3tNPqjiWUm0bvHhvqhrmUHXX8DM-vSMjUf73vrp7Yvyg9ZV28Er1Adp3h482O-wlzGVj34jFpueM_r2cHPRyFl3WSVs6YusisdUpIpXBKl3onhyETkigquqwF-kiuzfgvnGsp1_IfPHtXaUF4ama7wIK3p53UbKp5emAysWbjlf9chWfrTvYCoh4K8h2-wULTR9TBu8R5x2fVq6JXGP11FMV__0Z8wnEk-BC3r_YC98sr3xzPcE3ih1BpTdEa8myc_lhGWSArxHFAa_Z5KxNKB0fvFvHa8RQCLC-twnkhDScnk5EQ_Vu5_HOWfo6vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=iLWBzguLQqD-7Hapi30vsXhU3tNPqjiWUm0bvHhvqhrmUHXX8DM-vSMjUf73vrp7Yvyg9ZV28Er1Adp3h482O-wlzGVj34jFpueM_r2cHPRyFl3WSVs6YusisdUpIpXBKl3onhyETkigquqwF-kiuzfgvnGsp1_IfPHtXaUF4ama7wIK3p53UbKp5emAysWbjlf9chWfrTvYCoh4K8h2-wULTR9TBu8R5x2fVq6JXGP11FMV__0Z8wnEk-BC3r_YC98sr3xzPcE3ih1BpTdEa8myc_lhGWSArxHFAa_Z5KxNKB0fvFvHa8RQCLC-twnkhDScnk5EQ_Vu5_HOWfo6vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0Z4drlLg_tIqekvEUSvys_cZqRhm37k4P_GvLyc2Z93ukifiYbG5mZywiRt6DFoCmlC8DA1zc5i8vciRw6dRqRbYcioMAJslyW_IhGCdoEdby4kKOrhjtNm8r5CcAM5eczQzjFcQDhmE1UF7Aqqm519W7X-KcDgFEW9isNcPd65yV7O4m6XosuYf05kXJ5UD98xl7YsC-7ibu7uwtf74FMhpBIc1c7O_m40TVhfRuCLSTtoh-IieGTVvutTb7baocThDdGyegIlPerySmp39khyWBwCzhroEZCwmlwC6Vk1OGETAqrb-2OtEsdpyhVQwzmMyCdLg4k3GoJ-Sv22dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8_jvTRdudFpT8Ho85ri-8qDCQwcr0bOREFyb8ByjJ9dhcjtp9oyXY8a74YqRK-9dg_hDc9q-se8ZwOKLVoDIlU7q65MXYZ8l-VTlipCz2yLY8s-zKyFyFFCgU-EIeK8ZGgScw7ioSaDRYNfzvu6fCvuzrDYzmpKCuWksD1N3M27AZegrlyVHWC9IngEzMgB1PJZPteY9etrChs7DP84e3YQNBq4dvJJhCx1Kre-a73K5eh02u3qOjpcvsd-22zW7GlDuEDWsmDlRPklGoiIzlcTBOmQ0M2IxZ4fS_iRhEZdG04OlpK_OaLaH8C59JW_oSqmHLAxelazIuSnec0HvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra_TIkd3lUPyIjdvTE6j1a35oo3OK-AVhRTPGqk2BoOMTD9Gg8jooVsCjB6TbV-aiEDL7IOFiVPZi6SUOEA1QPgyoXeA9qarJUYRe82VAgFLkSgP2gDtyMq45G-e6lS6R_X0pbGvUkPuV59ZdLd0CRyL4uOwiU9APz-steRXntmaPAAwBy6d9YJf-Y17uzbDb00KjKfilJSQdWi7CoJKK5iU5fMOcNWCB428eYhllJmpz_zbckJn6F2K2ORDo9BoAJVagfKKjY4-BvoQx33mMwyOInIap5bWuLrQJlVB-8C38jntr7-WYXkr_JmWX2qVJsvjSGbtA_-Nr3UQiCGN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-hBpBHYLFbNyc9q5q_vIXObukteKUHBtKlF-RQBuO8efA8f-34-MnXdFHIx8RleYOVlXgOJJG6OcakkyzMGAdMcURLbXsAxFM1ZMvSBapsoWDG4yoPUvnGR1KnewhgwV7U0coZyS5hv63h8GTogIXWmvvuYZhEmIf_VU8sA7h4De7IQoZ8vJm-38IzCgGxD9wiw9prVdd5Vp42tw5YvnGUCn56_QvBZWrkHjuXm_lUI3HeSzWPKJIKiPeDvx-rR7vYOhtEeCzvjfoDsZZLcYa9nYN6J9O0yCJGyqEzvUH3VXjpvfyVV06e_D9oQcENjr5Apl_ELlKkkRjTZNvqm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdPw50F13GaRTzfYNL4KIHEHmAXqndT3wV70aNEUkXOXV5p0gJHVMfVBmEZjhH6rRxPwzGf6yBT2R__Zz0dnKOBavUznoVNB_gx84x_mlcTsnScJ82IORMTeH8yyIXJqKMejZF_xzrRRDUKTwEN8E4C23ygR85PEFrTVv1QurMuKgxSynAYsNxSKNlk7Gmiurxn5I-9LjVejXikNAq_cLDmSZKOvZNLSaAnS3LVlLYVRPVmVpbF52JLBK8mnxFrmf4nighIrzdw9SbrNyYBSP1zGP7X1J4VmNQEXonEbsUDlRTp3f-rDuylow9QimG6-GGu46yYcf-_wEGSoMFS9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IF-GriZmzbCEWt3nAYcB8-sWS-jfn1FNMjJUvVLBdtZPsimzlJdbyqb0iVQATrU8PvcYGK_Ge9er-eInIzBQ3kVpSRFfWRTEJFKGwT-rGRIagbMSVqcfXxqP5S-i2WfdqoLyQqhavVPb2KxU9IPwFFvqOyXvwhOBjiMHKZ-HymDt8DfDgj_DKCv72qPZCJSOTK0Ya_SiQIlPMPzSbqm7merYmXxdpy-TQu-LGBTDhqmL8ZApscTY3deERIbYkrbNx3vTR1stmgawIywPYfgtZ7dyYnlwJKLI1fTLesRfY1LLtYPHHYYYXyzcT2LABATUTVceSQosKv-ZVO5cID2_0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHnBN78FeIJArUJjFtA70TAUxPkqHubEemaSjffm0d6xbyY6ygi1msdxZfhB6oBCCrDkXlKw2TihnF89v6-h_Q7y9AtjWy81l_3HipkWO_8DrSm4fgd0bI7CW6jZWp_TlAFyumGrQGNCryeIyOaE2MCpd_64ca5kU0bxuGiS1K-3omWhQ6Z84YhQQtlEb_nWD3cDGqxGrxExwfmQ5E9GwEISr9EvfxH6ZABCRdyTBAASAnsP9KLohBgMESiNqWFEcrOj5P2QcXiYHLC2-bXzyI0sHTWZhsDovB5tflYBnE8puY2o4IPA25PMXjNQfYyiOyqvzz5ivKJuvlC2nKzwEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsIDxg_0Z3BTAlMNsHwFD2Mow8vuTBO2BCJKRh31WfSCQRh1qcvx-09bD0yHA6lnlscHLISLNW0EUOG58rT0BQdytH6bxio185TERJXNf8UYks1z6XuASlwOxaA9UFHMFENDebz4dC71j8m2n8jGdfEYpMMH1idz157kk-OUYHlFdx3_dvwkqzJp1I82Xzz55eP0eoN5rkfANROMKpRvmy1trOYeJG1VT6fTeGLgZ-HYaoeZBUTa7NkL5xHz0lReYTNoxQPa2zDBwiUfI-DurO5s_xsNcdYJN_rJEjjQFklPMPoi4VH1ixbLfzfAa8LIJb00Xo-jURRri-W46B1hWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=Sj2_9QSsSFpbsJGNjtFFLEx0sh6yfudyeaQ97p4pJipJE8TUe1OodJdq_d57YE7Dk4RwXtrjCopQHEf6bTubwhZJB9cyajNFOZ5ipi_y6RX67Uf2xdlA23KSanbT-vSIpqIhwlgmhRH5UWBFYOq3h4V7dEkAkEIkUHGe4oQ-17itfFMmq5nYOFjBuxRKXL3HXabrZ5wxDaM-mgEB8fJ_L9CmhPV0Jw5HXMYUnDJxVxTjrKjwkuXpfmpS7FAV6ghSdtY7ZwB9e4Wruq7wMhAMbFJtdIybVO_R7iqaDTVwty96cFf064oCXTqvEPZfqwp7luDtehhI-bSj3DzV5KcFpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=Sj2_9QSsSFpbsJGNjtFFLEx0sh6yfudyeaQ97p4pJipJE8TUe1OodJdq_d57YE7Dk4RwXtrjCopQHEf6bTubwhZJB9cyajNFOZ5ipi_y6RX67Uf2xdlA23KSanbT-vSIpqIhwlgmhRH5UWBFYOq3h4V7dEkAkEIkUHGe4oQ-17itfFMmq5nYOFjBuxRKXL3HXabrZ5wxDaM-mgEB8fJ_L9CmhPV0Jw5HXMYUnDJxVxTjrKjwkuXpfmpS7FAV6ghSdtY7ZwB9e4Wruq7wMhAMbFJtdIybVO_R7iqaDTVwty96cFf064oCXTqvEPZfqwp7luDtehhI-bSj3DzV5KcFpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=jm3tsEnjL9B2rTTuEWcp0ZB5iLKapKLEaWjNM6caVp7zgHe9DN5igvN5GXeZGjSn-nEWy-yccNSOlGq4uVXhjq4ad7M3nQejkgoNOy4wMFgFlFp_-L-mgIONsnxtL3-yUBTfy4_KJlmqJ1tdaCnaE116n0t5JCS9w34I8R-y51XJVMCJqyiUUa2NTQ6Bw1HvhwhlpCPyblXLB1mc7GLUXxX94oMDWvYex5tC1sbKKDwlHwkuljjypx_yUdmhQ7rsJLOfwpjp-qp3BkIO3jMRz27EfvyGnhKYGWvc-qY5ZPVUYT6BuVjvhXP0tfHPM-tq0i4Lx-SwBmAMCwzKjWrykA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=jm3tsEnjL9B2rTTuEWcp0ZB5iLKapKLEaWjNM6caVp7zgHe9DN5igvN5GXeZGjSn-nEWy-yccNSOlGq4uVXhjq4ad7M3nQejkgoNOy4wMFgFlFp_-L-mgIONsnxtL3-yUBTfy4_KJlmqJ1tdaCnaE116n0t5JCS9w34I8R-y51XJVMCJqyiUUa2NTQ6Bw1HvhwhlpCPyblXLB1mc7GLUXxX94oMDWvYex5tC1sbKKDwlHwkuljjypx_yUdmhQ7rsJLOfwpjp-qp3BkIO3jMRz27EfvyGnhKYGWvc-qY5ZPVUYT6BuVjvhXP0tfHPM-tq0i4Lx-SwBmAMCwzKjWrykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suEfewZ5GxiQCc4RhdcnQBiU4oZ4CnUxjvns0IFV-Ikl4h0dbtD_cXnuRW8OEd3JhaokrKR6MpziQiwCVtbb8S_k78nOzLJsIAzfCzL2Qna3a2KrcDbYFCFe8IQ9AgvyLVzI49GqqW3OPD6ozhrMzbD4rEgtotfyBW0dA-gftb0wK_m8GZZayl7fzlllZsrcg9JeIDhO9p-qgZP76kUMNgqFTlh64LZklJ-Yja7S_ipTUEx3Q0y8xyP7KRnxS-2xWo4CMk8BejyhUi_ZbzOrGm28k-YnpmPbIoJsdOw8wTphHSJmPvjco1wr58QzF49feEMVOvBjSrmebMf1QXyeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=jI-Pu3t8TaxJnwgtnWvf5vs8ce0lxWK_YQPx5LiLA-_E3PvHEeuqvp10KzaSGO3C0hZU7HzQtlvJlL_bX1NRM1wYRzh2BdhPAKPZVtXcRMbrIwz7o7JHG12SzNMQ_H-HP3JKH0KHbUE0VbaB9N5cK10PwoDXXt30Zi9eg6_uIhaf9ar7LdaQw5bgRSZiO-YAkeNTVq45cydOnUPOuuJh1cMtLX96xXJl-bvK9n9UQCe3jbDWOUQdg6BGoekM5rnu8hXhPJHIshai8qPsXzhpjyqs0bXdLNscPmqclIQ_qsZVfyLJaTyWbtzX_5cM6-vadisJp2Bgcb76Hwk8ZF70nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=jI-Pu3t8TaxJnwgtnWvf5vs8ce0lxWK_YQPx5LiLA-_E3PvHEeuqvp10KzaSGO3C0hZU7HzQtlvJlL_bX1NRM1wYRzh2BdhPAKPZVtXcRMbrIwz7o7JHG12SzNMQ_H-HP3JKH0KHbUE0VbaB9N5cK10PwoDXXt30Zi9eg6_uIhaf9ar7LdaQw5bgRSZiO-YAkeNTVq45cydOnUPOuuJh1cMtLX96xXJl-bvK9n9UQCe3jbDWOUQdg6BGoekM5rnu8hXhPJHIshai8qPsXzhpjyqs0bXdLNscPmqclIQ_qsZVfyLJaTyWbtzX_5cM6-vadisJp2Bgcb76Hwk8ZF70nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=MzUlP_QM7IOTUj2DKl5bCjHb0sE6paQlLFhXb6zKUpn2TPzeopzk9HcRlqEZ9ZjluW3IshK1LLgEBAJa6B33WdKlic8TBTeCTxCdMShwoHbcDXbB0UwCC99cOakOmP1sY_-_P1zEBNUJZbJgJ3aQrvUhK0FmM2RKLR0HRHcEJWRHF2h3CbepQTTuuwwPagb40aADSf5MZ5DusWE5_sgm6Ycn3-tZUicIZ2ofGA-FDmFWp9IYjmhAPDknqulrdFelD8Z_h0Ib8canIf7oqhHA1R8tIZq5kC_7bV1H3gOSWslVFRKTK8BhMYVGrZYIcS9N95AagEu5dOM5ghsgS20tNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=MzUlP_QM7IOTUj2DKl5bCjHb0sE6paQlLFhXb6zKUpn2TPzeopzk9HcRlqEZ9ZjluW3IshK1LLgEBAJa6B33WdKlic8TBTeCTxCdMShwoHbcDXbB0UwCC99cOakOmP1sY_-_P1zEBNUJZbJgJ3aQrvUhK0FmM2RKLR0HRHcEJWRHF2h3CbepQTTuuwwPagb40aADSf5MZ5DusWE5_sgm6Ycn3-tZUicIZ2ofGA-FDmFWp9IYjmhAPDknqulrdFelD8Z_h0Ib8canIf7oqhHA1R8tIZq5kC_7bV1H3gOSWslVFRKTK8BhMYVGrZYIcS9N95AagEu5dOM5ghsgS20tNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
🔴
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور دیگری از حملات را علیه ایران به انجام رساندند تا توانایی این کشور برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
🔴
نیروهای آمریکایی حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، انبارهای موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
🔴
این حملات جدید در پی اجرای موفقیت‌آمیز حملات تهاجمی در شب پیش از آن صورت گرفت.
🔴
نیروهای سنتکام در تاریخ ۷ ژوئیه حدود ۸۰ هدف نظامی ایران — از جمله بیش از ۶۰ فروند قایق تندرو متعلق به سپاه پاسداران انقلاب اسلامی — را هدف قرار دادند تا در واکنش به نقض آتش‌بس توسط ایران (از طریق حمله به سه کشتی تجاری در حال عبور از تنگه هرمز)، هزینه‌های سنگینی را بر این کشور تحمیل کنند.
🔴
نیروهای ایالات متحده همچنان هوشیار و آماده عملیات بوده و برای اجرای دستورات فرمانده کل قوا آمادگی کامل دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bsh2JuWu-Y1lFVflQR5eLVGK3w6BgQtsHPjshqyi0VCHCNZ2Q7z0CZLpHMazdPuimkSHPLWI0Bj-NtW0I397zfwTTNohGRkuNPrG1T77Pr-9GHyaT0WLsXlSdz1XvoeKMY8MmODRcOXHv8MDjDxSPCqfHwktlokcW5DyTGi7c7sHbiknFTEaMel86zoLGqqSOYDs9A7ZdIZOE0AFenZOfYTqRclBtlPUm-Y3W-6opMy-C5iXrIPvSN5pfP6WVRBLlsvwn71GPjV4MuddDh-LfTYYsZeIdyFTQWBLW9rKgh9DzNJ1ECX3ecSh2bZ6J0fSWeMm9cPlZx_bv41kfoW9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7WZrRViEvFMlrOn5sukk2PUSIK9Y9_5qkUjIl8MInSvRZOW7XkNJzgjAsyEh1UGSW-ZGe2OasFtJ8qherGI4UjO-HbEsN2idRByv0kWzXYfFp84IQKd4j46bnfpzGe4XnQ7PPe-31fMqg9clF6kTNm3W6IVSye8txSfKjh4-d00Utv28Kbo-zvQarIsF_Zgk_YhYux2sTuSo9mCp9X0prgjyUv-emcussNIkEVD5jZsSzjaYy4yf99YbqHogbDr5H3LG_nJOXdLIucOfrCm9Sr-sqK7Aw3dDHhqN7RPMxRkgW6OESvsL7_K0QYMp2CuI1Ab9s1NB6G2QPR-oS9RSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVQcdfuk93qsmPm4f2-Fb2b7JTxTJbQYz_EBXuBULcHWEQwH9PVDo9e1eZle6QUcN4X9gEpIAtJftjbjqLtTcrkgvQ3h6h22YW9gYml2PfkDQdUB0xu38mABsIXPbpaO9FNtSb5WdpbQscwo_RUWF3T_VwVkp04NOcei4GGoXmfQwGSI6S4EOyH0vpEgaZoDURxVoLpftv63Mm9mby_9dBprIhByENKoYdREBdG438ZCeUigW1VN2MBVZst7DP_XF50fkwXReaCV22bkfTMsTFwRBHtaYKHg2AyWtvFYKXaDq-psRrG7x9LT9vjHUJW2UtJqoE-KBYLgpv5R7x7cSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=DRIvoB-6sJrr5QlRTaVZNjghfYXhUSdo8VbA5gRalQMaEOCnOfXIh7SUjXMTIqZ1_lclXPW2lq-zfg5tg_KQIG6xRyzRC5Vzpy-nqY-p_D93cITTlA57Qr3Y1C72IHjV-srjE8jA2u8Ck74ETouJABAOij1wicIr0tSnz-Ve0ezJ0p2UyFdyIO-qxFU7JBgg9O-_Rw7Vy4Fz2WgjFApPJjVMpUcOZ889PFZdXgIsOvfPOuBuNdWg3ms-HRBG6L4yVl9Rtyyd6XfyOqbX0YyuO9mwPR74oJsAKqC197-iSjnKt5rA_MyZYVEWuTjbdJHnrxenXf1eiROaUZFx75ysfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=DRIvoB-6sJrr5QlRTaVZNjghfYXhUSdo8VbA5gRalQMaEOCnOfXIh7SUjXMTIqZ1_lclXPW2lq-zfg5tg_KQIG6xRyzRC5Vzpy-nqY-p_D93cITTlA57Qr3Y1C72IHjV-srjE8jA2u8Ck74ETouJABAOij1wicIr0tSnz-Ve0ezJ0p2UyFdyIO-qxFU7JBgg9O-_Rw7Vy4Fz2WgjFApPJjVMpUcOZ889PFZdXgIsOvfPOuBuNdWg3ms-HRBG6L4yVl9Rtyyd6XfyOqbX0YyuO9mwPR74oJsAKqC197-iSjnKt5rA_MyZYVEWuTjbdJHnrxenXf1eiROaUZFx75ysfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67628">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67628" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67627">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dPkjB5E3eZ9rmwW5GaEKWf5fH-LIFolWZAcWQLxuRDNhTHWGY7lWQXgZSm3hAB2AFt8PTH6xcZ0GO4boAD3jz5urv1UzuqrWp_ghpKyuWbRKbokeooHx8BcNyf8QQyIwW2m3yKt1oj7M84M1lsghSo7kFqQ16YOc0sFQ9o6J3ODCT3gcFuxaUBv32AD8qT-hvyXtXqUmFykA3KjRUPEpAlDYxbD8JttQzkJdOQpE7pHUQBQeCwvrWYoqb1oaGVgvG7vIOBZpp7L_fCUTeX_liA8ofcmKaEnBd6tYapcvM1kJRt-h2uvjIOePKE9sudYYZyAktRf8h91AZt_r2ZmSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67627" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ba_K1e7gjcedgkZJRMcD24kvuU9iYAlP3RA1uBvRrhdVlmArU75ltRmUS1wnsOeX3KRBiK6pcco_cQVGCc0kgcJSHsjLZfNEZV0yBmgD3vHPzJNTBF6EpRQnTG-JbTLO5GUg_7C_gI5uVyS4SYbqm9S72qDgLGglyd4Nr_f3MpzacR63Bca1ALJFMkYURCvNKBfBEiJhEFmfDyRSL75ooRTnglHsnOFePk_PCEzXYndokxPXLBqxZmtdpNuqBS5SpwcyshV-OqyqN0JlJctn7nPJuWyKnvhIO3NOiMpInTMwD0Y2Z-VUSmJusvVZQfVtRP2lNltP8naJuoVMaDDAiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJ3ESRTfehKpGeX-P3g14WK_aMKffFtuyifaycQMNM04P4_W5fmTTpspC_FoFpIrDDc7DcboUckCpwqCCrVYPVUTnJ_41pnliop8ncOibmv9Vj2-ZZkMlVxSZqLlq4WGopYAm31kdNkFo2mAwdCUIU5PgDlNNZwGOggkKCaLY--ma8N7ZykWoF5wxibv7wi6ZdVG0a32GdUh2C666RcbltEWoO9LC8d_yF3X95Qu1rPQaUWeF-oznqcrh95iuvZ6PQ8qgzXtU1G2lf1y_Lyc0smsdTswiNz75F8WEwtrA-ojbGejW00Ec1kl9EcjnhFOn8isjjjE1MB3fohXDfMR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIZO7UDeQgSF4yuIppX7YSb4ZYpQsSoLY5dUeo3eVGhk6qwvdSmjGaQzqHyB0EkdT23ZiksBpe-QK81BqlOk6utvMhviIORCCtov-DrH7hxYTEajdYfn8r4HwjxDfu5SERJOlJAzinaDztH_zF1bk_pSTVAuw7xAXKMki2YfHatLklqfR43rGqynuPyTCm9bv3ZAke2l71RF_s7QMD6UpQqkGrNXkShXgtGjKpWCJTYbgfNkK3xpa7-QwA6aLy-GmVdCjG2jiZRgMKkR_LicdjB-7l00334ugkNwONZ6MCQw_9Em0HUJUGzdKNQ51rlXNdwW226sQ8Cwff3tEYqaSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=Nlsuq90MCL-yrnx5CePTJxpWvcnuJBzKM2CfdgSV1Yp5iriOOVt9hLgxLqlHDuahHtxQM8WaBVowb56denYOhZH0S1-i5gNH2SFCDMrMIwk8K0lBp4mfjcG7cilYLw1wvJJUsjic5nZ7d96Ht1EQlPTdZNo4R41_M74mbxC7tOAc_EhKfGHPLfP5PdFKxxWo--lCRwPbK1gRd7eTJo_BiSOTIA3Hnchilpd-vsHYeePz0Kn40frwTjup5L3Kkwj1don96yNazFCL4lXniqZzq8g4rSvQURwp43s1CpLDsFNeFicuY76DbWaOIE_nGLKET6h36UDeK3BMt14OkN4O4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=Nlsuq90MCL-yrnx5CePTJxpWvcnuJBzKM2CfdgSV1Yp5iriOOVt9hLgxLqlHDuahHtxQM8WaBVowb56denYOhZH0S1-i5gNH2SFCDMrMIwk8K0lBp4mfjcG7cilYLw1wvJJUsjic5nZ7d96Ht1EQlPTdZNo4R41_M74mbxC7tOAc_EhKfGHPLfP5PdFKxxWo--lCRwPbK1gRd7eTJo_BiSOTIA3Hnchilpd-vsHYeePz0Kn40frwTjup5L3Kkwj1don96yNazFCL4lXniqZzq8g4rSvQURwp43s1CpLDsFNeFicuY76DbWaOIE_nGLKET6h36UDeK3BMt14OkN4O4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=GOjtlZmtVvBKzfFA0op-ta_8LYz3b5gN6kNPnuVCaKadtbgoCC_4DSf0F1O4Cnx4jlyBMg3y_4kAaQIQ3cHvsLa7W8iRpffCxA_5VL4sIeOQMgN6dyimIIJT2Ef5BKqIJtNm8h0d74u4zqtPF3vSz2W-5I8J_p53bIZ9Mt7aEvXA85RaAdMdVtWvDJBiIL-AHkHlnATPYu67dkj3DPiwI21q_fjQw_GmU8d1F5K6saJDrvSHJIYW-eOsUt_GM6szOLOLNKKLuZmNmLOBli0AmbmHj2MMilrwfVgbtTD8mQxSEIr8cb-gRNamT8U9ZpsxhXP4BIx-nHDUXFg7GLLbFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=GOjtlZmtVvBKzfFA0op-ta_8LYz3b5gN6kNPnuVCaKadtbgoCC_4DSf0F1O4Cnx4jlyBMg3y_4kAaQIQ3cHvsLa7W8iRpffCxA_5VL4sIeOQMgN6dyimIIJT2Ef5BKqIJtNm8h0d74u4zqtPF3vSz2W-5I8J_p53bIZ9Mt7aEvXA85RaAdMdVtWvDJBiIL-AHkHlnATPYu67dkj3DPiwI21q_fjQw_GmU8d1F5K6saJDrvSHJIYW-eOsUt_GM6szOLOLNKKLuZmNmLOBli0AmbmHj2MMilrwfVgbtTD8mQxSEIr8cb-gRNamT8U9ZpsxhXP4BIx-nHDUXFg7GLLbFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=jg8lSdwEwSt6YTyPPsCuT2G_wBA90uPKF_408L-ONurkjGrVqf_Be2OYdnOtqUYdC-Yoaij3GC0GhnqpXs4wm5FfLHr88xtH6o99coLsHbcaliXTXCDjfgRABiitQk2_v0LPlYZ63Q3jryLFnJUjwZhZa3-XEerywlfsb0cvRzzg4zzQxeq3q9aX89GE6tsHJLMtqQewPANg4Q9Sc_spF47Km-BFCu4lrPEAqOiUG2nHPbUYHS3TfZs-lFt1Qz7ORdkkfvAXqy_IeHjdiY-1-UqgxnSHFCII5d2UbSXkL4xYEF8wmvP2d3tXz9RNhVXKUSHqJIV4b1we98pd_ph95Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=jg8lSdwEwSt6YTyPPsCuT2G_wBA90uPKF_408L-ONurkjGrVqf_Be2OYdnOtqUYdC-Yoaij3GC0GhnqpXs4wm5FfLHr88xtH6o99coLsHbcaliXTXCDjfgRABiitQk2_v0LPlYZ63Q3jryLFnJUjwZhZa3-XEerywlfsb0cvRzzg4zzQxeq3q9aX89GE6tsHJLMtqQewPANg4Q9Sc_spF47Km-BFCu4lrPEAqOiUG2nHPbUYHS3TfZs-lFt1Qz7ORdkkfvAXqy_IeHjdiY-1-UqgxnSHFCII5d2UbSXkL4xYEF8wmvP2d3tXz9RNhVXKUSHqJIV4b1we98pd_ph95Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=iA0q1g2YfGt10nx9FyGUZOFccA0LG8jFKy76fNUD7D8FGHN6LvHusTX6HCQnzW9q9mJVxx9Tl_jOmfI2JDS-VeeyXhT2WGL2RVcptKEpfrEpQkgRH_mFQhgeNwEh1rPskuosl0ZVIW71bMAmFCR-2aV0s7WU5AY_krHQxDZ5gpjkrZInLlv8bauaNJn91PN6-tXlCRgbML_tMPoOohv0-I4QnGe7_puXayVjySKPm3qjSHRShG0H-ZI2TTYvIm6Usk1oAA4v4PjJEMTMUtgT1vBfBI41iMu2CJg23fHr9WThZNU1X1-el2ojKCVTB4zWVnlS7qfbHLZPh6P0KuCDGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=iA0q1g2YfGt10nx9FyGUZOFccA0LG8jFKy76fNUD7D8FGHN6LvHusTX6HCQnzW9q9mJVxx9Tl_jOmfI2JDS-VeeyXhT2WGL2RVcptKEpfrEpQkgRH_mFQhgeNwEh1rPskuosl0ZVIW71bMAmFCR-2aV0s7WU5AY_krHQxDZ5gpjkrZInLlv8bauaNJn91PN6-tXlCRgbML_tMPoOohv0-I4QnGe7_puXayVjySKPm3qjSHRShG0H-ZI2TTYvIm6Usk1oAA4v4PjJEMTMUtgT1vBfBI41iMu2CJg23fHr9WThZNU1X1-el2ojKCVTB4zWVnlS7qfbHLZPh6P0KuCDGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=rAUsieoxRD4r7bUNv_tIjsa6bqmqTNvD99tkSnchxOg4uE6rzJBomHVu3tm2B50irhSezHOlbxUGWgaBkVleD-FZ05X0r-7vMBCLUa95atEnThqQQl3uDjE_1XTF8xjcTP3AzpYaGY-9LqEBAua3da3vNLVq8g7syXHhevp1p9ab6iy2MTSHxUU8AqZp-EeEZiFDg3tSDMdmYuPF2EmQIUZKn2t-wfgewE1JnAcqqphyWrRzHj3xCfQKymp5ktdbJXUd2R0gH5jjLqIL3fynpjGxoGauSZfmDWQJI_ipRPs3TrRIX9SMRa2ySAFvq0v68rAi-h5U4hGg2fxQQtbCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=rAUsieoxRD4r7bUNv_tIjsa6bqmqTNvD99tkSnchxOg4uE6rzJBomHVu3tm2B50irhSezHOlbxUGWgaBkVleD-FZ05X0r-7vMBCLUa95atEnThqQQl3uDjE_1XTF8xjcTP3AzpYaGY-9LqEBAua3da3vNLVq8g7syXHhevp1p9ab6iy2MTSHxUU8AqZp-EeEZiFDg3tSDMdmYuPF2EmQIUZKn2t-wfgewE1JnAcqqphyWrRzHj3xCfQKymp5ktdbJXUd2R0gH5jjLqIL3fynpjGxoGauSZfmDWQJI_ipRPs3TrRIX9SMRa2ySAFvq0v68rAi-h5U4hGg2fxQQtbCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_1BgctUoe03xtj5aUoeE9fAisGE_DbiCopKacF6A2bN4A1MHSjoE1fwSdWQAcTSomEvo1NcximteqM0xRc34L-zFVmWDd-F1lJZ6wNWdgq-z-EIsHIZrZydJFqqosJz3bS67mSkuN5i3YosOHqD97059pH1WcwLgz63YKc1VxV5Vo8YHYnvySCP6QCn0fieKCrrH-4GcQqi3_VSXzBsUBrCFyiSxMNBA2fgUOOasI9MRU5_W8GFNXpj0AM2NLjMcHB7n9rEf7UkuToNu9HA8i8F8A-cofeUltkxM84CnqYmO5xnEFrL3SU0Cup2DpW9CQGuTBWlHT29TdiefiW0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGapYpHLfLAlbSwzs_Ngujbw_TxnUN6YA1C3x43DPxJw9qCd6oA3BWBcIeJQc04KOyfUbVW0glLJH2Yo6Si4J9DXFAEXG3T1TFcpHvH-u_nFNHF7E_g3UjDz5Zcyr6m9yYpczBLpHaFSe-17eQwyzrNI0aFLVDoYy2u6gkTERt1GthDf9tD0TdslJBWmHboEAJ1CwGX6mPQqIHsEVEIZtXuoZO9-BBg3ndbIxg-h7OuDAtRKM998vUROKc0pCT8WFXbTe9pLdrkzQ3Hu505H0TgMIRRP4D9V7JmEGULpNvUgHVK_RZw2cO5b-YitYC39_zgO5cAuYVPtgVjOsfSTBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=YdTX9_zavUonjTm2lX60NKyrEfhZ4RjKug7gO-x-oQrGIF8pfY4-P1GeDOx2h2nQsy5kIPUg-dZnoSIIoYFA-_8n2mag1iwX7_914OpMzncIRED375AU1P4K0Vp9aaWLNQRqYVTeUC4PF3i4fDm9KibkxMdwPhTgEz9V5jPwokDCnl5z1S26_D8HAgt03qFXPeIoZ1lN2MsvTA_U4N-ObukpCseOvDdx47cqLLbRGp8kVFTtFjezUa1ysv511CMPdUPxr5EZsHVT6kC68PS_9du8WiKMIIgKPY_w5GqzldAjWi7wsHb9X10JBgdthsUgayy4mnhlaQSgSWvijb3hUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=YdTX9_zavUonjTm2lX60NKyrEfhZ4RjKug7gO-x-oQrGIF8pfY4-P1GeDOx2h2nQsy5kIPUg-dZnoSIIoYFA-_8n2mag1iwX7_914OpMzncIRED375AU1P4K0Vp9aaWLNQRqYVTeUC4PF3i4fDm9KibkxMdwPhTgEz9V5jPwokDCnl5z1S26_D8HAgt03qFXPeIoZ1lN2MsvTA_U4N-ObukpCseOvDdx47cqLLbRGp8kVFTtFjezUa1ysv511CMPdUPxr5EZsHVT6kC68PS_9du8WiKMIIgKPY_w5GqzldAjWi7wsHb9X10JBgdthsUgayy4mnhlaQSgSWvijb3hUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDaD0d2dPdQOc8YXN95BvxzY5JbkQjUwfzykOHMzwrqtBN02yF-T0THLwcpGZUIGPemBx_dCeooztHECn65FucLzGMx3X-myArsexhNOmDV8Py6fQsOqSEqd_T6R5o9H2vyVTtqVd_W5BmJW0w21n1dSImISUl2B0EjKVF87n9WTlZvsKSsF9BeugfsBdxtcVTSELKLX5GJDb_DMP4PHUXiP-7xs-chkH4KjOkSdDnxDrpssJhTp9-iiGWdzOi_3QJy23s_VKi4hpCrE57WCAyrr1bF4Xx8w5XwjVViT1Mwb-cwpKp5B-F1V7B8PjsjG8g9-y2flRhSB-rdb6lsFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IA96h4qtzC_aqNpkkyoVI1SQPzE-6OwdG70NRzSwkwng36JdqegXMAJfAQZ1UOiQnW2SiAdSwoM1hbIgEi_XqsaKAUtnjQ8ZkqFPIJLF9NifNcKxG4TTHHYaNsMh1nkHnUSaPmXbPQ9AdHCwbOZf3c0Oya1XpNDdvB7eW0tB109vP3c2svdPLdyb1BmJMh3VrXvVaTgKOilHOGgF9uq5XDdRPZiSr7fWRW9ImaVfV1ta7btPCaR6Wb9AMxXPLkUi0-xueG4fGa-q40nNMGx0y0r58z5WaVv4IVU2AJ04k50oUA6rIK1PH0gvXPwI-mumeJB8zDoZTGZGcwHKQuEIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVroiYKSpSzix05u8ZceWz1j7yii830FCkt4BlLPpfEaB5AjAzFbrBB0vRjw-3ES1Hy-iCOcEOv3GXa_hG0PVdp8IRBQm_ezvJGwQTwqF6HxmCmOck_tlZbFsrJgT2yyqb3RsPDokZ9iDf4FLQQE_YiTmP1qvQeBZ4fOKqZj8zB4uWHpv3U9YZ16vXiNO6mT2PsFuX-V577vkoXgkj2bR6FjBBST7xNUvvI5T9-yMKEoSfcp9DccwdQiEMVGMg1Yd6pVmL8nomugeecwYvX33sO1cIB5HH7gITSDqP5bzT_CbVy3_vIZn0XJyaJf_P-T-iCJhD0n6DFGFnix8YZ02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFIJqwvVmXYVMyzzuNf18v2vCJpeOaZWBrxHUcNDZJsyT-YphE-NbO_XOVG8gMmPUQ0mIEaVssIL6uqqFrN0T6hk40tN5ZL63P1M62_Uaq7cG40capCGnT8EIDn2dbUcyc0v9otX7G0q0rHIWU7P1imfAXr9FIlaK60dp7CtX0naNFam6OOmz-hYrBfmVbB9YNOQi4JO41_htdYYGGdFbVbBk15pj1nHewXqZkaN817iJE6rWzlf0A9GRYBtPQgXtVj7ci-JaFCYsA0PfcWYJxjf71mcZpgnLThUUURT7KulJ_23B3GC5KorOV4CkLnbGvIw7aM4be0AeQQsaZBc1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=LeeMY94k40tKfp5ovl7oyWzaPE2i9y3Pc5TNrpWTTV4GNnr1usn2cHUlFa7O5mr-oYuhFSO4ndstHBTyng7Px_MCT4z7_qQzThyTrphfFacCKUsTvHINxxPxWgwQxtcw6Z0KSP2FLajXXhQNDIHRXi_0fmQwDFFGRgJg1rH4XBR4_ddesx6b63VXoKsGEqHQQVSnY10jHw7QFwUwMKgcqq7bjZughZJJGZFK3tSrz2vNntvsi3xSfu7E5aMNg_jyLy2c0edHlFU6or6Qk6g2Qa_8IyHhvLFwsyLbsIbROvGZiHVNjxFcdTH7V1BMvYdMUjGXvnsrZHIKJCsc7ttX3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=LeeMY94k40tKfp5ovl7oyWzaPE2i9y3Pc5TNrpWTTV4GNnr1usn2cHUlFa7O5mr-oYuhFSO4ndstHBTyng7Px_MCT4z7_qQzThyTrphfFacCKUsTvHINxxPxWgwQxtcw6Z0KSP2FLajXXhQNDIHRXi_0fmQwDFFGRgJg1rH4XBR4_ddesx6b63VXoKsGEqHQQVSnY10jHw7QFwUwMKgcqq7bjZughZJJGZFK3tSrz2vNntvsi3xSfu7E5aMNg_jyLy2c0edHlFU6or6Qk6g2Qa_8IyHhvLFwsyLbsIbROvGZiHVNjxFcdTH7V1BMvYdMUjGXvnsrZHIKJCsc7ttX3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4L4id7p0spEc-dvaIymhEFUmLr60_M3LOyMWt1bGAcfmUOXRULEKjF_9tzw9tqHDEsAUqH60FrlRefVB1vc23ygcykTbIwnfQX5zWysOJ_WQO779JxsLpwSIXiGax9ck0xC0ztp0OMEK_4wLaJKlASEEt1nF5MK4CBYd2kaHrEngJPx4Cv4rs0oHdaAjjE6zbRZ2wa5qPAxoCvCDozwuzupD-io_XGlpuSKF_whYjFL8ifV_y5pyuEIyYgeeg1PlHvFCXAdQBP0jwzRAG47vsQLq7nihS4Ebk84DAWjkCza8hp6bODvwGWYjU82EtcO6VTNz7SKg3BbQXvgRD3CRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgWd7tXhDRy2wFfHLU68xwyiX54CZi7JViUvwTnYW6R4k8Qk8VCKED-Q9UlLzJ7gYPMyrd31A_Lq_WkQPANM3_OkwqbQR5pXvHtG-6hXNqBFCEdady3PFi6JCIHfwiObufxi-TRVkH-dmMF6sL4i_d57gdD_f3F_yM0QJwx0gm3WIr6PkNBjf35hf95ePK68PdbBcZtxWMv7il0pd71jNJu5QyEuT93Ykf22D3zbflpuOs_QzapuXNNFaDn_X1fz68L1MfdpSccJ_poSj4T2ZsShdW34jBaFWUUSg4RC_cPQp-uo5nGOgPtWRx9MKWMu_YGmB7d-M_x7_PI_1NJM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
صداوسیما :
نیروی هوایی آمریکا در حملات به چابهار، اسکله‌های «شهید بهشتی» و «کلانتری» رو به همراه برج کنترل ترافیک دریایی این بندر هدف قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67599" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h208aD9TWGr_kNFFH_3mqlf2zxpSx3oaMfeFiXi95JtyPPQI2hXz8cfLrl7QxBJae3-g1C8UEnb74TrQVwu0TS_Ci4b-0IqulE857gly_F43Keli418Bla7kO4tnA1Xzh7u5vWJVVgAmB-CN3usbjfwwrWY23Lrh8EtFPRC4eQ_pS3NuZ4dhoCsy0HYugQBOS7aTLnDP8xf6bPcM_wKOBZeLviVlBkVhUJi53vQIxr1B4uXCmqbXxq3Slj2Lo0Vvk-S61WXDlR1ygixCECQwZ2oN8zkDb9bhx4vIvbNN8zo-ex3eLUch-Vg3hqUHJt7Bmae-9ssAPZ_AWCb-mPP1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hr4XtxLUu9yImmlljkaQhIcXYzIBLyfX54uvJO_BoreRmdoCRipLlvnM_ytKqvvzSog5IVY_MrLgsMStm1NlVK0niR_gvUPZrohwbriucWa7JwrJW_TVzilN3W_Ke2wLQOBSmayzN-rEiUmh-8kPKHvkI7iVRh-ZHiP4YtfW_DUTL9lrMyAlNCtdaYQNV0H4Fip1_Ns62OM_-yC1l5AP2bnFytGL4hYv4o4QAouc5KVX7M20TmKA9MRhtNGpvxgQIhk1fbYLFcgB2AL27a339XChqiQq71eiRF77_Kfrzl6Fq1Nosk64UX3uJt6AwI8XVgIHnVOxNnc-k2moMlphRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
برج دریایی اسکله شهید بهشتی چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67597" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67596">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی مشاور رهبر:
دشمن متجاوز و همدستانش به شدت تنبیه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67596" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67595">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67595" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67594">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
چندین انفجاردر بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67594" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
فعلا تمرکز حملات مربوط به خط ساحلی جنوب کشور بوده
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67593" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67592">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60497304.mp4?token=GyvVzOkxzv2q_yUstm9hGbaDpYXaBPLX7mNpn4CYBqy-rGR21Hc4VIRL61klmHAWJB5Q8RGg6qOhH-kniyJIPbNEeYJ94rOKaGBrEvm0cXU8ekg9c4oq9JuTTMZMRnBB1fpeD2gasfgIfXtcoKRd73WDRCe7FDKSL7OUYFpkz4TzYEArIj1-DPCwleh8rqhO6ZvoYClQbyOvGGk8csNBE8_mxBx5YeHJ2K1ZKluHFozog7uyaq-TjQBmc5Y06742LBexoBi6BfuEt3AConANp3nBekCgXkF1z_-mrhrBYsY0jEesfRgISe3wo-spnIguzZcDJZ2KQK8BXv_HrkQK4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60497304.mp4?token=GyvVzOkxzv2q_yUstm9hGbaDpYXaBPLX7mNpn4CYBqy-rGR21Hc4VIRL61klmHAWJB5Q8RGg6qOhH-kniyJIPbNEeYJ94rOKaGBrEvm0cXU8ekg9c4oq9JuTTMZMRnBB1fpeD2gasfgIfXtcoKRd73WDRCe7FDKSL7OUYFpkz4TzYEArIj1-DPCwleh8rqhO6ZvoYClQbyOvGGk8csNBE8_mxBx5YeHJ2K1ZKluHFozog7uyaq-TjQBmc5Y06742LBexoBi6BfuEt3AConANp3nBekCgXkF1z_-mrhrBYsY0jEesfRgISe3wo-spnIguzZcDJZ2KQK8BXv_HrkQK4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67592" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67591">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67591" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67588">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cylXk6xliCvwZBbrm_ciCVsxUWXD5RbYiAM-bgrbITjNWonrsrzzxVUMhjXzV_2CNAsUYvhfR6EK6Ue-2odafQq4q1CeiSIJPZYfgB2HTF9A_iyg-GCuYy4POcMzoXt4zWzCdWx7VOc6Ca6yAc1RkajvvSeq-fK6iqLJHeHQoDrMWNvLrsXz4UqOs0QjQXVZ_XAldpeXJ7gydDgpMv3sbpFHxcv85O1fGKq0kS9DAPSiB2l0lhwe_1kB6t5axAhpJM1W310ntyxecaOgVTryfeSTrevODG059Ir0cGRm5heJm41bEMNCYHVRUoJWvWTy1PpUN9KI3uG5Tm9p4MFvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=f9ouSs28T7uF5doM3uSK7YTgX0bAU4u3NfjjE2zsjFEH2NHct9tFAXrZ1bvpcTOvwXLeLAna79nP8YZLjDhfj9P8TDuFKqy29lHsIcAEPDUarx6Bj81DrRl72kTVg6JMpw3_LRweZuSDsYAKbojP4vTvf2uwjVQlt_zbOO5RHwClDGpi-6Ilz6zW0zPRhXim9kc_I1gEBRuEfqLHo4OPK2HL4pLW6mjeh_U-aE0DB8RqRmzN_FkLeDwxHkND55Yepu8dMQZW6-CZs0YR0GqOh0RhR0BYsNspYcCoGyieASWjcpg39b56W7bFFhnThWAbTJ2QYBG3t0O5HJ4IX6av-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=f9ouSs28T7uF5doM3uSK7YTgX0bAU4u3NfjjE2zsjFEH2NHct9tFAXrZ1bvpcTOvwXLeLAna79nP8YZLjDhfj9P8TDuFKqy29lHsIcAEPDUarx6Bj81DrRl72kTVg6JMpw3_LRweZuSDsYAKbojP4vTvf2uwjVQlt_zbOO5RHwClDGpi-6Ilz6zW0zPRhXim9kc_I1gEBRuEfqLHo4OPK2HL4pLW6mjeh_U-aE0DB8RqRmzN_FkLeDwxHkND55Yepu8dMQZW6-CZs0YR0GqOh0RhR0BYsNspYcCoGyieASWjcpg39b56W7bFFhnThWAbTJ2QYBG3t0O5HJ4IX6av-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67588" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67587">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=hxNyc6De8GgU0aNoGjSKyeAh4SgpPKyQF_7-0ASO_g-hhUpT-nZcFmEi0CI53PbXxeosaI9X-lXK5XReodUipCtrmH0x2b_n7VPD1FMdQ0qTdFWQFnZtt68MOzAtAKJFVSISNn4wqpS6q6KE5jng9h-5D6z_7AjGrwLWxeRP9QbwSMJmMtQk-JbA_toJ71ycFywezBRQwyd2530JAvFTPRxKpDFhbywjuE0F-8_ohUn8idnFrgPkIpM-VlO0W15GXsXoStXxkMe_he9qxZ0zfjvKdCdCYNZ4XpANS8wykRTYa1y_9UuC9_FnpSaA7vgyyc7_hDXDe-jwpXG_9pvPYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=hxNyc6De8GgU0aNoGjSKyeAh4SgpPKyQF_7-0ASO_g-hhUpT-nZcFmEi0CI53PbXxeosaI9X-lXK5XReodUipCtrmH0x2b_n7VPD1FMdQ0qTdFWQFnZtt68MOzAtAKJFVSISNn4wqpS6q6KE5jng9h-5D6z_7AjGrwLWxeRP9QbwSMJmMtQk-JbA_toJ71ycFywezBRQwyd2530JAvFTPRxKpDFhbywjuE0F-8_ohUn8idnFrgPkIpM-VlO0W15GXsXoStXxkMe_he9qxZ0zfjvKdCdCYNZ4XpANS8wykRTYa1y_9UuC9_FnpSaA7vgyyc7_hDXDe-jwpXG_9pvPYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67587" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67586">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره ابوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67586" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67585">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=UJoGXZEsNVNmmh9Mh552JUiG7Xx2EekTWAx_tlkAOYQ_cDC8ksl0HngwCb2UActI1w-zDb9ekva5ZzNK_QPAz4s-YYFeGNSb9NWz9hctJEDHgsXYPT5TOSch8IaHyA2JklNFZmDZaEso4r_UhbDQ2MsWB_jWt1qEPKOKb7GOIHC5cwqgvggUOWuliDpnOTNzjPfApaMfXg3xmZN_uUUCRoalKR8bQwZgZ7AKKrLyiLe9qt25PlkSRgoGRNO0YdOf3YAfRMN-h1BbRPPN9_u8XPvnZx6QJAPMitZk-ZsKgBYIdJUBe54eIbN7VbF8vJnEcOR_PTxpxbYVUPjEceB2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=UJoGXZEsNVNmmh9Mh552JUiG7Xx2EekTWAx_tlkAOYQ_cDC8ksl0HngwCb2UActI1w-zDb9ekva5ZzNK_QPAz4s-YYFeGNSb9NWz9hctJEDHgsXYPT5TOSch8IaHyA2JklNFZmDZaEso4r_UhbDQ2MsWB_jWt1qEPKOKb7GOIHC5cwqgvggUOWuliDpnOTNzjPfApaMfXg3xmZN_uUUCRoalKR8bQwZgZ7AKKrLyiLe9qt25PlkSRgoGRNO0YdOf3YAfRMN-h1BbRPPN9_u8XPvnZx6QJAPMitZk-ZsKgBYIdJUBe54eIbN7VbF8vJnEcOR_PTxpxbYVUPjEceB2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هم اکنون؛ آنتن زنده شبکه خبر
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67585" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67584">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=LTusAL4Yhmvqf35VObJ0JQdj-7NItTeyu2F3Mjb-miX1vmv89e2UKbLEGHJn1Z9qzX8ezCY5BWW4WOUSSBC_n5x8FfYO4f5-1pIdqB3cdunLycFF7jJuqOka5CXwcQl1eDaogyC52QbMnSDFQIN9OoUZnucsFjbuCy2BwQX12IIEe3PdcxURTd8_cW1-PK-s4644Kdnm5LSSE4yohs5nvKJHgKi29jn__Gxbr6O1mqAHTi0aX0CbkDTOew-xlvqPeRen5VisoW5AWrhUe8DHwDzl04RzXPDPvovH66_EYEfI3vqRqz2ey79yMLpxwl050uk4r_Hihp0zg1IHzvx_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=LTusAL4Yhmvqf35VObJ0JQdj-7NItTeyu2F3Mjb-miX1vmv89e2UKbLEGHJn1Z9qzX8ezCY5BWW4WOUSSBC_n5x8FfYO4f5-1pIdqB3cdunLycFF7jJuqOka5CXwcQl1eDaogyC52QbMnSDFQIN9OoUZnucsFjbuCy2BwQX12IIEe3PdcxURTd8_cW1-PK-s4644Kdnm5LSSE4yohs5nvKJHgKi29jn__Gxbr6O1mqAHTi0aX0CbkDTOew-xlvqPeRen5VisoW5AWrhUe8DHwDzl04RzXPDPvovH66_EYEfI3vqRqz2ey79yMLpxwl050uk4r_Hihp0zg1IHzvx_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67584" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67583">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02d221609.mp4?token=MavKQIUL5QDLqq99HtT1t4uXCF_3_GAEzhc-tFKS3tBINNwo5QesAtRtCS_W8H6YXGAoD9oS0Kbk_TIllca0YlerRg67NHz7zrstGvoAY4FAaBHYY_CVL24xwixoG3VYjg3Cu-7JSfHbCNnLKFuIWJY-lVybkPsTzX4PAkZ2IPNh_guTPYI9xd5L1A5rpfKZ2hMEYC7SuqHHplbMl7y00fX0ZsKdUTNXo1-2FNXErtT63gl7n4DHG7eDqs6ia2bb2nNwfaalPvNmBhbLMkC-dfn4mABqDdF8u680jPbUtM57GjIRXmzEEITNXXAjmodPMKBx2py274zzS1NQtuhUuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02d221609.mp4?token=MavKQIUL5QDLqq99HtT1t4uXCF_3_GAEzhc-tFKS3tBINNwo5QesAtRtCS_W8H6YXGAoD9oS0Kbk_TIllca0YlerRg67NHz7zrstGvoAY4FAaBHYY_CVL24xwixoG3VYjg3Cu-7JSfHbCNnLKFuIWJY-lVybkPsTzX4PAkZ2IPNh_guTPYI9xd5L1A5rpfKZ2hMEYC7SuqHHplbMl7y00fX0ZsKdUTNXo1-2FNXErtT63gl7n4DHG7eDqs6ia2bb2nNwfaalPvNmBhbLMkC-dfn4mABqDdF8u680jPbUtM57GjIRXmzEEITNXXAjmodPMKBx2py274zzS1NQtuhUuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67583" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67582">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
نور نیوز  :
به زودی حملات ایران شروع میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67582" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67581">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=ip5OpP6KiV5xno-z9k2Y97XUuTEpk1S2kfKmFLndJUFiLMvaK9C6dVmn30fgqYl8CKgnVzCAFg-OuzKtef8fS3npHM1lKPMG3BbZT2gEfooVW7E1Y7VmRNnd5PYah-YzNAro4WRodfP0zoPV8i7JWwIDMasdtQLL9h2mrf7_DdAWhLH-OKBPwAR6JRN6qli_eR2h1GhZXsUM-e4Y4Rlev8yPJhQCmKfT7az9Y66p26cz0TAHixuw0ubyxcFN9GLd6hbskgpwewWmopst26VEt28BJBo-uom4atcggBq20ZUcUB5tlECxU-8O8n8y8z49XBYnLjV3eBf_YkSXV9FXNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=ip5OpP6KiV5xno-z9k2Y97XUuTEpk1S2kfKmFLndJUFiLMvaK9C6dVmn30fgqYl8CKgnVzCAFg-OuzKtef8fS3npHM1lKPMG3BbZT2gEfooVW7E1Y7VmRNnd5PYah-YzNAro4WRodfP0zoPV8i7JWwIDMasdtQLL9h2mrf7_DdAWhLH-OKBPwAR6JRN6qli_eR2h1GhZXsUM-e4Y4Rlev8yPJhQCmKfT7az9Y66p26cz0TAHixuw0ubyxcFN9GLd6hbskgpwewWmopst26VEt28BJBo-uom4atcggBq20ZUcUB5tlECxU-8O8n8y8z49XBYnLjV3eBf_YkSXV9FXNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریشهر بوشهر دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67581" target="_blank">📅 00:11 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
