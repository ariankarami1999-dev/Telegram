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
<img src="https://cdn4.telesco.pe/file/PYvkd-GTfp9RNpmKWmsuepLgvDaLAPwRDvz7YXofKsG_C-LMOf7PppC9eW_AR1JjDu1K_zN3hSYYsV9ZmGs0Yvd9t9vJtqDQ2kyyeehLKb3SxEHnC2DC1ZTBOhWV31OlZ2_VOJObeSwD7RND4WcFRmHN-6gImuHzvbII2IVMA4DCYaneKJmq-OCEsQ8rB9lZ77kIVRFKR3aBTMjCWrpe6RkuDQ9_D03xAY7anW1INRYqyVoWhQt-8sjCmR_XioTG0M8xRlyi6QyQhaxWppCN4PquuF7D9L3iiRnocQRSCwcc72X2cDpSFRp02KffArMwGsL_Si4hIyiD1LZatzbH-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 147K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 00:54:15</div>
<hr>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUOvCvOioHaohVvdQUwqFVFlrf9mDr8052V9KwPk7siJ1p6Yu42xkKfaBWY2u2yr1mXYqnxTTZN8bDEaWtxpA2UmX__c_AnWVHhS68vJRvl-7oIa8YXIm9A98w6o63JsE4dYknj1zAf-KQAjqO7CG7iM7GNxkSCXFerdG6oiNR0Vk04qWUu8J9uz5_St0aE6PRvfmzHiyWxjJlBUMIkxcAVvT2VlxKI3U-2u-BU5nSoBV2rpJc8VgbCQO7K4r78UG0lxlbJDha9JqQz1QjcE3CgXffTXvO7kPX7iJhZGU0HVz7wX2G0i9AWboE2SJINersqSNqEJmHgDBQiyz5g-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6gYhEugDIX-Tww12P0DzcSg94evEWu6syKjA5r6h_DGl7pC3esHrPn01nDfQOypTn7Wtg5OdZWVt_pF6PIrzA3yGiBA6ED7jEFrxdDYzNaAcOcn_E-kCVvDIZkbwKSCZlObWuwKAhED2R7o4RWFv1kmGd-2ctWHbf8FX04S0o0NdNWQP0Ou0KFWxPvQWLPhTO8OTC5WXQH8U6Cnk_Cu9npGzCCug5qGWsagpr9RVmoq1JyYhh8ktHMJecmCkEI2kNatrNuSyaRPdorr6cRlbCQYOrPPGSkRqwIhhECA2Ddow99s-Wkx1eW8kVIuE0EZlaJALm-XXMcVTwQn5q0mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDvMdlkfzDheHcMPeLoYmRVALTMV78kx_rSxpNdhCUapv95RMTJG1dwtRk0nyvQmhMsRJfQuZHLTw_XyuFYGv_U9A9bmZKabtCAH-h3DcyQtYP65gAJK_JHE_SYfoMTMP3RsTHWWHPS570yIGE4MK6BcvueLia5vznIY4qbA8ms1vw8G19DxGEOZL6HZ5uQstHrx3i3OgKp1XrPZHTAz81IC_5qcu-FDgYZ55FFQR_Bp50cVmfLx1UC7q40qYrVkaoqTBjBNGl8M4apyqWgSiOXyHTkVgFPurM3PJD6tWnAjzoHcEkgd5tOwXz72j06k6C-3yoylnFkEPcahxTyu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qk_mK4qzor8fxJLEaisia8lHgXZlkfDvVRcerwiWCwfwj82mpMbzI1mJu5QNHhHuO34kLm0rxguEgHikSTOy1kbcveATi3RYHjnUR7uTs1sF81iQ0Mp6hSotvwyZwLytPSHfRIH4Y9CdPLIw7RcejIxsBu-Ct5bJRCoWAHr8ExMVVCwQ3H8uPKnDJzpMwQCyA-xVdOM8WGNhtoA34wESsVkO8856SW0FbWRaUq1OVWxBTPJiYfHEvrwgWOeS0rwSZSfdzQMQ4SwXPq8Y6UXPFlDuBDYKXDq8GWmETHgV7aCdswTGJAyOWLDPDP7t0_R8011Vfz7mhA6MEIAPkaXbWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWMWlgvAbtND3FeNR56bbRbzSw5qysmjogV-enKZriOe1uyxoWoUcHrdFyZFLyngwDR3yovq5D8er9ch_VU9AIY9-q1ji88-XZYg7M2ClwxbA6i5FhzMf_5x2UyaMFzD2ZEzSGqB67o8TAeRFBG74NkbaLTA5kYScLvK4g7MTkTlEMsjG7qnNZQLXK5xImCDaio1wvB70yovr_cpQc6Cun0onQuJVMgipDkEk38pzZXdHSndg-JePoUSHsKkGay6y6H1J0nDVZbpFB5qZPNAkavtcQz-rTHVPxrVTnlArILoKPawyW9FWgHCUQRLDpAnQWMvsfeYhhFOMjGtZwsQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhVbztuVaHrDiarLc4Vd-K7ti_7k1F73q_83EUNC6AGcRVf1Al3D_Sf8ctRFQrxPwttI4w_r0yJ9q1DyVtxzc1pFf6fcevzkMDpUP_uKReA6jzsDTwXUwsvMUbL2OPwGjPrA7s_Db9MO0cGTKaymyp3meEtHYXQytfFvOX8NvbYHSiB_2fF_LRHt2rCJqMI812knkMGgYt-SGMc0t4lH51rIEVImfxkuG5M1yuY7dXOkhimNmvevE9LbbAGi6YGbdDmv9gb9VdmIBXElqx6lBUT04j9juaf3yBpJISt0O8W4AJc5KUPbHcJcRMoaLBvvjT0ltlS2OzSKkaUZDmGazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnnNTLe-3_Zft_tZDYhNITNsIDju1KGfRCEO_EyxQb0M6jbwMeuICcSiy1eoPBjNquBTajaD7A7lhgHuRfElje7Uy8SXctriJMpiTIOHrRUu9eCfydG7xbPtXmkocrgCTyf003kHddRM3iumBQImdEgVe68Oo1_hKWwz-BcOavlg5481qBHqq3Uk3iFGcGvHeAx_Eg6cvSKJYss6jK9-p0XaaCZk7SPLD79ppKZE0UZ5A9X_giO5ufI5zB3TRjf59rh2WBxwoHl8JfsBCyQkb0DwhU4ulaPk_gj-TssmwbI9LnS389f7PaGoWYPd-RXgkjzNwORvnOg69V-QCw4yOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tx0eGbOvUPPuAVj80ZZDq0TEGp6scsBVBZvjqDK5uK5P4UtpzKHU0zp5cgoFyYnccDBr2sMXCnboV6NnurNjPuZP4J3O9YELemuc70jhVyFEdZiulnt22XfsKm-FvL51Nq6CEklaXEOvbjM51cNmjXtlgunQKU9JzQSAFQWFr0ZWkPUdofYUzfFqsE79yx74UAiU0AUutZ2iPLQOlq12zhhsPAwZTAvWKBKt56I_lRby5_1moQaQfkc4CjROUmvcqYP1pPiz_NQRX0L8q2VloK0dDqjddY6RlNmCuAM78IdsH6_q7kfwWj5EyYQJ9Y2KvzF8tAUlwec5sm-31UncXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7oNV3rCVQ4u0STnILGPCM7c6NmzDhFfdMXoIFQBY3ep9x1psQdDEOwnHDHmmMD0pukBPzGI0SYiCEYu3BCHq_CUDqw2_qwDnPLuzD8aX8IfyVMs7SBU6168xp6bwtf4PQz6jghzzXayTMyCnwgEKrRPzbwBKxQXpt3MmfEp3YPCuGc1PoDaZd8ZvnX7hHqXwLheMUzbuaswtdiidWU8FPD8khD8AUpqwkbcA92ikogf4RjtWn2FQoROZ-zpF-Z5Z6buQqO8PDJXOn9Wu_1wmyHcFpYl3Heu1duGEnc9bBmv7tkcZPf0WQiAfDEsxEIqI52EewjTfvc7wsBYFR0Yew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrNRm1kIEwuZqmenYVIr8_HjJDOkg5RvyCW8kkLwVU960TT2hHLdyelx4Gw8a3MrUSaQtFyVhpUAMvhDQMYcKnIedO-uAQM4RBI7HNgkqxeUuJSNH9joIvO8YaiQ0PMOQBa6xVF3Ov6gZ5AobU-dRLokAm3nA4wdN0J2ho0a20JmOZD-Kq1gaVOI6E7W6E3SW-h-zoO2bGgavNJLdPLhW-vxS5TR3ebuoRALb4wWauZDYWc-TgU-KY1kgMaCMoyuCeYV_cgKmNOPpbFO66Bsh0Yb8hveiVDMAVDnaucFXTQOweR93IHABxa3ijKejClLKOnCy_BGU5HlLQnjf2Q5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFAHgaCBLOtnj_4Mf4EEzIWRYJ_RIDfyYj8LA96j7JfbtvWkT1JsdBO9NywRpixZS5ZbAHjHmD4njphW2mvX0C6u5b2Dnh4lIR7xyEfAa6rkh1xOPObDlflG6po_EF0FSIb_gcV5RLZO0etLbS6ol9AuFqrFgxw5B6sz1rTEW8DRBh3tUdwX2-QsogvL_W_3eQ06s14bAzJEivA5YllCXIaFtkJxjY_FY6siJKzx6JHK6--JnNs2B65pA0-wn1_4lItOiurriEfbV3PA6vPJMKlsLr3lV0bL1c0fd8OIThsWHAMHRdzCM38_R1m1ZClxReSD5Fk3J60-GLFls8shHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onpOWQkQ0XwlHH0k93a4FtttvtJriK_E0bzxTS0g7SxP_ZeKszT9kCtDOSXnnRdD5UUmVClUAlwSjoXf35VA0JQH97PTtEiIbk-gTL3-URpX8kdqddYw3iPjzqYm9GOfFFyUE3bW1LCAPq5SSNstw-bW9_2BHyfQ6HpTIpj57yng2LSI5-fgvE1W24epEfB5-IVOZ_xpDclZEQMqnr8vU2b4OsPL8S5jidGNf2B22MJ-hBRfQVU_EbLx6HDoUo-cZQ2t9N0JlLEszZFUA4tWc6tEMRPvDzTkm6iWIZS6oGMEnuzFfbsI5n7_77lbnIvU_y5zpzDcC1MC3Yyuyd16rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIk7SBkkg9hdb2P8J5t64xU5pLvUo8ZWjUaNOwM1hdnvMKoaI4R9tkGu4wIMCYDGMKq_hLOGnKfY9W3AM9-VClSnpou6veLT8y2T-4Z1IDqqkcxkY1KIaooxneDkTD2PUGfKeL5luRnBYVewxJoAosXaMtJb51puzxJaVU8oC62fX91ES4ML5E5rvNHW3A5OFS6sXXfPspLGD86uWYc2x2Y6gkPz7MmB67ltWSPJ8wxntdROGzEbxtNXlqQlie_FSKMUkkm79cJBc7oUp5vUc18uV448WxTpvFYHbkQ8YixhkrTGo4DScrF2CcxazoIR4w13JgSeCfhSg3bKaw3Yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=WvI1iuhKV7ThIxt4McMRn45tNyKPHnATYZ2qXfE_zFOXvIEBNI7Tou4B-rKcN3tDaCSc5sAL3xUqs7EOFy3Y9xUUv2D7FMh-QnPecWsd6EMipRSzn8qH6esMn-CFsItK0_uLOFpMawhXmheHrbpl88kQW0HfKrwbJWqKGAlDcGlgLjYtrmH8RY5TpgzJXQK9hoqxDQ-wikf-tdhbaichRwV8bdK4lPAab9kWzBQkTkW99epNXjzq5LqoEh4-JvawY5ZVJ0Ldy4GQUapkqgiIHn_lihPNwY9_tpRgVi1vSbfvsmiuAzXJJWkm48vwsOZL0Y761AhYe2ZgSZjCwsaL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=WvI1iuhKV7ThIxt4McMRn45tNyKPHnATYZ2qXfE_zFOXvIEBNI7Tou4B-rKcN3tDaCSc5sAL3xUqs7EOFy3Y9xUUv2D7FMh-QnPecWsd6EMipRSzn8qH6esMn-CFsItK0_uLOFpMawhXmheHrbpl88kQW0HfKrwbJWqKGAlDcGlgLjYtrmH8RY5TpgzJXQK9hoqxDQ-wikf-tdhbaichRwV8bdK4lPAab9kWzBQkTkW99epNXjzq5LqoEh4-JvawY5ZVJ0Ldy4GQUapkqgiIHn_lihPNwY9_tpRgVi1vSbfvsmiuAzXJJWkm48vwsOZL0Y761AhYe2ZgSZjCwsaL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVx0G89pxfoUR4kPsYzjXUt5FGR1EOAJfeUnNESwHvK02-fQ6of4KKyUJ_60ZwAsVQFapTRZXFHecuREI_4PNUHtpMZeIhlJ-bS5z_cjzDAAHRaSG58hOHCslSJAcH2-g6WAjIA6cEL5-EAWW7KjDqOytKwf-5kxvb81pe1JVYoNtIwc5aVrIaO-vB8ZZxWgiEEeLCRmy7UgAdJ6QBZR7C6JzPuo4FKJOnRy-E8E011MKb6yDiX3FpBWm1d7OTtY1uDo1zL6yYzJniGKf6eun4763JieoGkbp8qLPX_1GjOrNJjeS-hdheP6VFnmV5c30Ypmtj7kQRZ25uxXuLSxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlBXjLGChHNXHVWE2n6vSVTLkRWlQfWEwSf3v9eOM4ecuA-aojg0M7RZGBuwB1SiEeXJUbQ8pRO_99VOd8GOWrg38-NkBsmSP56gI7O4aQZfCuUMIdTKBO3HQVfcQcfNR25wfAUXeNsRdVpP4FbXaWxTV3_xZvvg7EEqEGRqMW8f9lxuNYZHGg1C94tvKVYKRxxK2LQCqxjuaLQ6n2WiIS4yDZ4DRTndMYJWsuI3KuiYm08dMMErhmBZVkauEwqWbA9uSb4T7OGO9FXMq6xrk6tanxst_YYD8yab9Y8VDdQ3LTSN92f3Y6QcX5ZDqX_nKIt1hyqFGbpdozDmDjeqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbeqHRoYFDIkOOY0akZ1BOqNs3G-GChr9bx1bbevs725x3ZIEUc1LIqzoa5HTih4UuHWgWNd_er-MAsGqfbsSnUr31N3PvKL4bHY3jOyV8pGo7ph5P5A5fy4W_MWfsPARa1Wcevivu1DHSgn_5hiLVXTn9hv9ZrTGNAwnu07tnIdo9KremnOGfQAPviVtDM2y0SLhdsYIyNVejjlvFXcSfOD_WNejeVVoT6xAIfDVH8Uq0vJQ2tI0gHa9t9p68uUVVBNdPpJE0nFEIbsPBj1NjU37XY7neHolLEoerR5oMfowm8jLGuigVnUtUSY2jzkJ5WQHFGXrgvqbKMdU8OIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO3x_yOkZ1Nh1aSNC9PNZdGBreW8lSjBsW6FlZA9E6CW8eUqwtuLBYUXHo4YKTarMvWlzvHw6aIT1Y3oVQyAAIHcX8oYfyexB72eh-vDRT41W1uSiXoW6X5KFgtrPecRG0r5rMb2WfhMofPUVENB0KqYtl9_EW1NdH3N4qmFgNHsGRiKD3zBvs78F86zhvJUd5E_CUU56UmQl0cATD-R-MEwiyKJX0m1IWhdgyZIVK4Ny4jr9A3uYvV35anvr6PtA62olYimTxmEd8XMN0IsGGyba_q8aZrswn0I8seYOl7vXsFHhvWEbfIlk4fK3ElPox8ExWOijxs1qwjqa1SMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=foNhdtwJQKho_gCIKy1OBgW0XkpieEAw9tk09DAPSxd8-Cja6JSZ0A4oF9JISCy6tuzEAvS7QZtDfb18_KtJbqwHTUNfnXQRqz0PkDhs5AolRz-9-tqOnEfl5EKH7uINRpFSNkRR7CBFiUgf13qZ1ZPdUxcKn5mESOPMwDh1rs5FUPRLw_LRHiePCvCRcHos2Z1YVAgkPdFqup1aPspdz08PTd2U5NCYlBQSjbCk2YGXTXmx_L-_bbJuClNqPcTvn2QVXbQc3fTHYBfwKE2b9Oom49lEQ-Gy2JlJNQSh8YNmHce0YI34t2burs453EiVqokBPFRIQbGFgwUp2g_K0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=foNhdtwJQKho_gCIKy1OBgW0XkpieEAw9tk09DAPSxd8-Cja6JSZ0A4oF9JISCy6tuzEAvS7QZtDfb18_KtJbqwHTUNfnXQRqz0PkDhs5AolRz-9-tqOnEfl5EKH7uINRpFSNkRR7CBFiUgf13qZ1ZPdUxcKn5mESOPMwDh1rs5FUPRLw_LRHiePCvCRcHos2Z1YVAgkPdFqup1aPspdz08PTd2U5NCYlBQSjbCk2YGXTXmx_L-_bbJuClNqPcTvn2QVXbQc3fTHYBfwKE2b9Oom49lEQ-Gy2JlJNQSh8YNmHce0YI34t2burs453EiVqokBPFRIQbGFgwUp2g_K0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=RTbYuxlLCDmMEleV--o4CYoWhHtAJTMpxA8zR2b5U0Q8CZxmA9vLL2mhJQFE-SrJrMQ8aed_DmZpDxFeiVzV4FrtqAoKyv74n2NwJtx4Owg2yxHMXTwj_JmxqngP0X5l9eeVlGQl2ipywCAOWRS6rGOjmOWcL7Xpi0OoJRNqDNQaGe9c8J01QB-QGl42Mj8XKiUkJlU1D0Sk7zDaBZJfRdfCL1PjX-aq6IWLOMb5OEGvR8iIBU9DAZNVsL5KL_Hk9UQm8qeedY6OuqSci7M2WbQQj_MD3D-70bKY_CO7UKVxSVArmqRPGLv_KJa2Nc9xNXtszCkvnJMWubkluf4xRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=RTbYuxlLCDmMEleV--o4CYoWhHtAJTMpxA8zR2b5U0Q8CZxmA9vLL2mhJQFE-SrJrMQ8aed_DmZpDxFeiVzV4FrtqAoKyv74n2NwJtx4Owg2yxHMXTwj_JmxqngP0X5l9eeVlGQl2ipywCAOWRS6rGOjmOWcL7Xpi0OoJRNqDNQaGe9c8J01QB-QGl42Mj8XKiUkJlU1D0Sk7zDaBZJfRdfCL1PjX-aq6IWLOMb5OEGvR8iIBU9DAZNVsL5KL_Hk9UQm8qeedY6OuqSci7M2WbQQj_MD3D-70bKY_CO7UKVxSVArmqRPGLv_KJa2Nc9xNXtszCkvnJMWubkluf4xRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm0Jj9lN-z4W_ajLriiR0duhnv-GVsedoKabU3HUh_xVWPaaEiNHZP2pnE0E7Z5Wn1v3DBraNagsuc98T9koSw-IXT5uFD_DRDxkQUhUy_vj9eHNFLrxLfB6jd3yqeGTY8-fqSMdd17ra4PdyySddpgaC_FXXm2Yg71_58kdB6fhJJ4qEFwr0WYHs_NglLvAqRb1KM8jPhVlA4kE6kLQxlUKT328V5FsUBEoOZzLTNY_Wf0IjhoJ-pgVZkY2inqQu3K_0Q8wWFxOPx_RmaZWXEGW6s3BRk2mAtDZXJjbWd8yzrYyfmNd_Q22YXXnOUcQn0mv-j11SpdFBMAmhlkGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g75wtzPZw2SblXu6oXv5BZ6InUgOfJGiJNDS6VdHetuZLJ77wDSsl7o_Q20Kk2v4W4U6ri0uz2DrjIBinIkSc3s3Ik-Vd9TqKtwMcYNL3Epxj6dhCKz2Ugmjot4AA_9G9360td4-p1TFkLN27Bj0JLgmTxb-gzuahMSos42sSYWuL7NeFwp7CxexRid0KLmW0QrSxXka4tfSMmxkregjXJssT1N2CwPw-gWjm6dlUHqfG8DA4vrtEpOETP5upkUbokYxGH4f88BjeK2Mb8ekMwYkaz_mhl68CfeJChCOtIeytOtriJAaR-ZuY76eRTu2aNIzk3FoOnkWr7X1Vxg3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-NTtkv-Up4LkjTEf8KPckOUWDbxnriyLA65RRPt518bla9DVh14li0S9MDzsQER3PcDHiPudoI6M4KoZM2dVGSesa3Z8ETS24l_waza2LiJR2m9jBeENORsPlnQAbCSk2jvygpAbbH8cG0R5m9NYdJ8m4G2jOr6I3Jna1M-s2eGNhXr4Ewz2sl8k3-CWn3gR792ZZk6IjakKo4j_uNu3t4Si0IPQyIDxw1_IsnCoCGrNgbO3Z1BqftXM48FenACPR7_p5QcwBnNno2FCtHncE98frk6EkT2mdOKgV4u-V0Xf_YC7V20_Cr4s7f0GzrpSYQWkn_obU2JpqxbS8PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=Dwl-9-MQsiVu9QspTxERJQKoOlgyPbptjlG4e_Rm4Ytx79sWkNzx-ESV0j9voG6HrqUq4Yd3Q05NrGDMPtW6ojDCqazXsWhSJleanq2jyYB90ROrMmpx0RwjKDtQ88umzQ8Svc6HCTZ3oHudJ9THbiEJhACe7FAq4mIZkGblyCHyfa-G4170CiBRBXoSTqe3Pwy29uK5nyRQuZyM3lFptTR42wQDjGBuIurSDWCM66aFhc6Cdh3ntLm7cnmMAJiy6X_3Nw4YP3aXWIUSY8b10r9onJUfph3nGfGhkigNe_M03JTHz1fpezkqFuGdE8LU2p2A6Ldfj-hrclbKZuQxZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=Dwl-9-MQsiVu9QspTxERJQKoOlgyPbptjlG4e_Rm4Ytx79sWkNzx-ESV0j9voG6HrqUq4Yd3Q05NrGDMPtW6ojDCqazXsWhSJleanq2jyYB90ROrMmpx0RwjKDtQ88umzQ8Svc6HCTZ3oHudJ9THbiEJhACe7FAq4mIZkGblyCHyfa-G4170CiBRBXoSTqe3Pwy29uK5nyRQuZyM3lFptTR42wQDjGBuIurSDWCM66aFhc6Cdh3ntLm7cnmMAJiy6X_3Nw4YP3aXWIUSY8b10r9onJUfph3nGfGhkigNe_M03JTHz1fpezkqFuGdE8LU2p2A6Ldfj-hrclbKZuQxZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vzGHToUO2PcpVH8rrUeqwADr7mQ8Obwu1NGuYL8-0wMx0y3iDNBxGnm7yGRlX-710Qpp_TvZXO0u7YesCC0bNWTYLQfbDvuASrAqHKjJlHNEYkrUdhfzvOMT2mPAVO4NWfqeTjRP2S0uBqxHqXIwuacGqWNtSwuUo5dnLQ6O7zVooxMva1WAuaorlksqz6jnGNP_XQM9FL2haitwBJPlFejXjTsVNZeao-x6rhK5meD93CJLpF5sNIN6f8ensXYyisHsd429lPQwPlv8qzeAHvWGr-UWeTEwNO2Izk44V1aCzzdu0lDDa0cghQFoRwq0dBIISyjjHx8Ae5hOC8lQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ihmAOY2ujhTNUbYe9Vd5PGTpBPHf93FLET_aTehSTK-xuQ_iX6IEx8v3nRLl1nxSoZUQKBTkXQk0TZcXWvf4HJY8DFu11lqZ_W91CBnqdoho37CpPx4zypPS2I6eLdICkhBgP1QOmOsh9jwwIPuANFYLolVs5KpB6opGrWIOkB6W4R0zXueaz2ZcBGbuzeIwCSDCAXYYbVV5gBGDXabWpwaIhiA0ymYv9fA8A1fq8u8UbjTy8zAJTB2VK4plC9RVLrLdkZ5CZ1Q5XLHGtbXLUeQSIoGm4RHejIp8w3iX4xM2BMQf76Buz9PpFuoHdhDimdV-gpXf2NiLT0Qsr_8R-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nxy0x6_UQxaqwVEeyvU6XzNUQy1cKtPvzbkP7N_9sVjICpfMwhgRmarCjdOTJ4lEWD4gA4jU8aDSze_rBorA-lUY-mCMTtN7ACkI2GC4FFB6E-PCVeL1KotHyEPYT4b-tZGZ3Lo-Z-_W1PJ-WOUWRRcklDkA56LKxxS_L5iXoTNgdC7P7pjXteRlAEHa_o7xG9U45mJPbXtu_YUl3G85sDKzl002MJ4lYsYCmVVpKruNREcoIxYdQUAarpEXNBXzm3DzOKO5w8UWdpDUjFta4ydo_EhvxZlUGD0mdEz8WGS0wAvnvmDL4UHBN18WY4keYsiiGfAsXunEklrMQNxMgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nxy0x6_UQxaqwVEeyvU6XzNUQy1cKtPvzbkP7N_9sVjICpfMwhgRmarCjdOTJ4lEWD4gA4jU8aDSze_rBorA-lUY-mCMTtN7ACkI2GC4FFB6E-PCVeL1KotHyEPYT4b-tZGZ3Lo-Z-_W1PJ-WOUWRRcklDkA56LKxxS_L5iXoTNgdC7P7pjXteRlAEHa_o7xG9U45mJPbXtu_YUl3G85sDKzl002MJ4lYsYCmVVpKruNREcoIxYdQUAarpEXNBXzm3DzOKO5w8UWdpDUjFta4ydo_EhvxZlUGD0mdEz8WGS0wAvnvmDL4UHBN18WY4keYsiiGfAsXunEklrMQNxMgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLkpHjk8tyAhx76LYk2E5sCQ0lc8cdrdOgJC_ZyBNXCiS3IW3OsqYZm9gVl9RaQo3OUfiVIcFTyZRj8a0MYYvfwufDH0joWTb9b3Lu3UQ9MatN8KzavPnSLNJD51rFrpjs8ahbJwtLsTEV9AxKsXmOnhaTSZUUGPLdiXqu72GE4zt4mn0_6cyd6FcZ1TXERP9ZVnLsIELKpEBmWqmzoW2Bo4vjtmyeWvmOF1dMVJsiwMiUr7IUGZ4VAqQjyt0vBvz8N0ReOelyHfiofXaMHHDvHPW_9zSfR91Q6Hgenb_ImpJC3uW45tO8st_iY3-BTXvGOpZo8T4xYTsIr4MOyquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvDfcstQGCD7xZW-2cR0xsHXd8eX4tsDbR2uIwfrb1jpOPXZtaYzeDjUmTfiFwQmaUEbFhmFKtHStBMjLS7D3zBVEwCGCRI6HQGswptpAMdlAr99zGQYAdViCTIyOzuTxFhFHxprDMbSmIrh0ZxPNVu9JycwmSoCFXOqxlPjONATvlAU3hXsUwyXlk-oXgjYqhbQ73D1z2lT4vta5uPmZcnv9V7nBP2eKhcyI42xzCawM8I2vdoCt55AjFN6Uv1VwnoFBPxNfMGO2OdEda2RSmvjBtfn-FuqPel4-JINsuNwfY7z0uy3XxcOWhjQtJC-C-ihPfrVs6FdRJxaQo8IhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=bU1JhC_ohpGKxUDe2H-05rAT-3GxnpOFhIz_Zy9A-H87bOqg08LXnAgSQUTgdTJVVuITM3Mudq_8dDDoC3uPZUTRQi_9k85NAqes5Q9dWMfLD2M_4x_qZyTL-4ulLjPey4Lo_hTyWfpL_dPR6n92sBLmWvGbqa5g9Zgp3ZCGjWSBbR0wEF8hyxlqzGsNSxsNUo_TcKGd1N1OHmEza0ou2-n5G8Vxhl0_kwAQysSMCOBBnpyG-d-4gGjRItr-Ba6QpK62QWqhri1IDh-XR-xAMDPCGmPvcyDdHgRE-Aq4zHzj0zX_cbXTLzoYRTIvO7wZNtCsZVhnrnSqPqL54a7ZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=bU1JhC_ohpGKxUDe2H-05rAT-3GxnpOFhIz_Zy9A-H87bOqg08LXnAgSQUTgdTJVVuITM3Mudq_8dDDoC3uPZUTRQi_9k85NAqes5Q9dWMfLD2M_4x_qZyTL-4ulLjPey4Lo_hTyWfpL_dPR6n92sBLmWvGbqa5g9Zgp3ZCGjWSBbR0wEF8hyxlqzGsNSxsNUo_TcKGd1N1OHmEza0ou2-n5G8Vxhl0_kwAQysSMCOBBnpyG-d-4gGjRItr-Ba6QpK62QWqhri1IDh-XR-xAMDPCGmPvcyDdHgRE-Aq4zHzj0zX_cbXTLzoYRTIvO7wZNtCsZVhnrnSqPqL54a7ZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=gngqexoZs_vpDGwNWD6oZpDmJUMHVireDhsNceV9dsBbJ8JCzXklKg7tB0IE52ffOX5eroj9MlzkPwlU37WKseqAsXo_lyGA8ZpghdgzIFCNmbgihSdYqIHVtWJgydqul0LED86RNh9EePRsDRhyjWtku_Rlay-2x_cwEXaZrAhjo6Xb1Km2e0Czi7T8KMqvNJBWOUm8nrSQVeN0vVnr8HTv72uuELwUdu9hoUJuAoRSgIpTtAAIt6oMFySzFMms8VA7bF0-vYwfiR0z3OtnwYvF3qxsPchG5GdDj3mNUga3Vd2G9DZMT7SKhKJFq8jNnyIiMGfMYC2Bh7glWxq-sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=gngqexoZs_vpDGwNWD6oZpDmJUMHVireDhsNceV9dsBbJ8JCzXklKg7tB0IE52ffOX5eroj9MlzkPwlU37WKseqAsXo_lyGA8ZpghdgzIFCNmbgihSdYqIHVtWJgydqul0LED86RNh9EePRsDRhyjWtku_Rlay-2x_cwEXaZrAhjo6Xb1Km2e0Czi7T8KMqvNJBWOUm8nrSQVeN0vVnr8HTv72uuELwUdu9hoUJuAoRSgIpTtAAIt6oMFySzFMms8VA7bF0-vYwfiR0z3OtnwYvF3qxsPchG5GdDj3mNUga3Vd2G9DZMT7SKhKJFq8jNnyIiMGfMYC2Bh7glWxq-sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blr3IX4DB4HVyokMvvVmbvDVKpBccMI7HfsiOV7DNA6fxnZiV8-Sj-UwELR9BraSubSqbVkqmbbMqMJG0OH9KmxlaWrhSpBNTRc1OC0GAlE9Fy1-xyrSz0zSDMGGNhny-ElNlI_sP1HUoK8zAiILjqZ4ZaFaaYnyqgoZILCxX_mOtyK6PucsMqU9-RkZS9DkDjOi6TvEq4oQEacru580pAijoyXkqvw_5wH1AkGemfDQNc6dTLvsjpBMj3jTSUn7OrYOX81JE2tP-oxP2TmayksQepTbsS7gVs1blvJHS29W6v1h3S53qiRIHPv9eh3W6_6mZfW0BToTT-B9KpbBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=nVoiVUm1VzHzchR-zV-x3foNT1G7s2Lw2Mqpz-euYIOi8cIUUkWkoycgxg2JKMUwOuEzdju5EoGDXiM3BZNgE_fzoa8Lmvg5teK7RS_PeQ39n-8ADigGvuMIkE9kWQ_KSriPAlw-lAACGwIjkuLBlZ-iaI6lopH2kBAHsKNYHGSxTunBOmZDbQjKx49OCZo2dMySU-o0EdknFEjVNpA1LvE_zM53uWPjK_JwW94KzcGfxiHoLYFR86vnZLAGRmozXkqfNSxJAdOTWR73iKV_CqFtk1tMiRvxhvsYb6XYHpaHD1ijZmjn9G_7feVWBvFKT5ZjngHdRL3synoqcMMsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=nVoiVUm1VzHzchR-zV-x3foNT1G7s2Lw2Mqpz-euYIOi8cIUUkWkoycgxg2JKMUwOuEzdju5EoGDXiM3BZNgE_fzoa8Lmvg5teK7RS_PeQ39n-8ADigGvuMIkE9kWQ_KSriPAlw-lAACGwIjkuLBlZ-iaI6lopH2kBAHsKNYHGSxTunBOmZDbQjKx49OCZo2dMySU-o0EdknFEjVNpA1LvE_zM53uWPjK_JwW94KzcGfxiHoLYFR86vnZLAGRmozXkqfNSxJAdOTWR73iKV_CqFtk1tMiRvxhvsYb6XYHpaHD1ijZmjn9G_7feVWBvFKT5ZjngHdRL3synoqcMMsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPuSlFEvPKAf6UnEcTXiXBk40-lzEv7iUcNQ9n_wIS3PVbYnP34p3LhHjckNuIMmH-Bkzf8CLAGBWNzGVrrlGzIwB5lM74yIpEHTevr8H5cAHjEXLd9YmhrafRXOOGLsm6mnKNIC_BAQFX54CPRFdf4kb9e1Ywod11DtAVB1Za1Jw9Za3fuWWHX-0vyGndLNLkTB8KULUs_OQ7tmvyeYut0uf0D5tqbbeCYYsh4-cNDnntdqkshsxvDiPzE6DlkjFSE1wbqr_kaaraUwpAiaTgVMr7Vac6ELMQIV080o4-NAfq7-oIpStC4iDZXLr32YvPVmrNvoIot2jIffwg0-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJA-5wUYFhQ0ErrHe1NevRq7vQZdJweh7cLtIpI4AyKoEXPohUvWR5Qhs2jCfo4lwQB4BUr64E1c1sCrnFiOWDcN0h6v1YA0oCLrdYKmqwkdf0Qt2_IA_UrHBgxmQ0nt5bWsj0BVAm8PTEe8NwKM3m10i7jdf0qDmG7ss5DoJuZAyxHDXEQuRKVnQ5lYwfhoopiUQpG1NeXmctggJqfkgtL3_GyzpGfjj1WQuJ_42LKnRT8Tb6D5F-sv3g8TfIkxPyEMuO8xTBnmeKqZeapZYmGnxLl_F1gI6voNaeJMW92CSb-yKWS7nhVKTqEy9l3fVJqmZ75U2GlHZ2xkxR1ERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py-2qELTevtOqsnrnDbqe56Qjl_uIirEunFADVRathtyh8PeRE6UHrcdKLUaPlTk2q67m-Y5f6FQOwHuUhkSptdkfamAIJ075RY9bH6EeVJte9zqXCe7oSK1Thbex0ox5wlC5opjwnqDLoXzZ-xphbOAT3dyPfBLvl9fVjk_YNQ4uL5Nz_c2mLEvMCZ3hePolsPD9pgwCOMx1Aa3VWmVxcYOKHbMSagtVNVte-kq45aCgg3luq42IEOTDAg0KLpii_5WkyPEP6CS3Cm_pGxBdZZrvHsoxBCBh3Jitj342xDGbOuh7aOvaYVHi1X5bWYwvwxuvwEkwJXESI5u72gioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7Zniex-oixc8OvqX7EUAA2mZIdMttesWLdjraEXKvNBWonH-hazAXV62Kj9YCrMLZLX2tae7nnqip0lzCFQLJxq3_IKSbQYywMus5aezxsGjnAOi6RdipvC26bBfW3VXHkxqT7utwpyMMwwnStlGsK-h0EqIUrxLRQoDPt3eaVg-xXMjjmJP-uNmt0WSsce4Kt4NLhumt1U5qV15_SvxTEDI4cEFthpb1Eh_R53_cyh6U8fU7w3-2cMFrSaICtf4Qhp1YMPWPZvOAVlmgbdVB_dPdtL0vkE3yeKA_mfbJdUoZcjpxIpIUDgStYLTL8MrtG3bwl6hMOdmfJL0emOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=NBre767BMgwp4ncQPsOD4G6avR0ODqINFvIRK-MjA_CnwTrV42TzbAndzX4FcNL3fXVcWLowvEXkf32NKy0crC9lXIeHnPn5odwvVg9V_78Ez-qLezBjRq0FNZt9fSH9ELkYkRhQRQ4XuQ99XnQXduZVxP1IOdiAvOMsQ58MCfKd5wRiU8fSm93HjL8ziojicSeAQboT2fniPXUCsjHI1UID8bjJNjeZnOX-ad9GYCk8Ym9A65lfA3yrjqJwAR1KnK1yHApYebvw0lqEICU4LgYW0trHjCYKP8tnTYE1S9hHLifLG2_0C1mm0mZXOVChoRzbK6Nr-y5Tv6sfvnzcag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=NBre767BMgwp4ncQPsOD4G6avR0ODqINFvIRK-MjA_CnwTrV42TzbAndzX4FcNL3fXVcWLowvEXkf32NKy0crC9lXIeHnPn5odwvVg9V_78Ez-qLezBjRq0FNZt9fSH9ELkYkRhQRQ4XuQ99XnQXduZVxP1IOdiAvOMsQ58MCfKd5wRiU8fSm93HjL8ziojicSeAQboT2fniPXUCsjHI1UID8bjJNjeZnOX-ad9GYCk8Ym9A65lfA3yrjqJwAR1KnK1yHApYebvw0lqEICU4LgYW0trHjCYKP8tnTYE1S9hHLifLG2_0C1mm0mZXOVChoRzbK6Nr-y5Tv6sfvnzcag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=BL13ciqt954s9635N9bkRX9qclCKH3a61y0T1wIWdjZNdlTvsbPdSYOK12HUQx_45pcAds5e_e7O0LirsK3D9UH5zk5r602H35B8flx_YDr-kX_rVfcdjDDCQ96ce9Q0tPg_aGPvwEr52fPhKsPYWV0MugGLadrTEBouAwzyWFqHth9HNp-LXGS2WMb-VzIOBabDUS-GwLlZhCyCwAGR1ec0Ad6bpCvDkLNVsGdXFuk8AG_HfXugqFTIQ99jv6Ks3FkaO1Oyw6gbWI9YjAzNCU4OUAl9DulTff8fxY58L56Sn6-50TqeANMMtu_v4ferVMbFniEX5YiYQkhb46378Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=BL13ciqt954s9635N9bkRX9qclCKH3a61y0T1wIWdjZNdlTvsbPdSYOK12HUQx_45pcAds5e_e7O0LirsK3D9UH5zk5r602H35B8flx_YDr-kX_rVfcdjDDCQ96ce9Q0tPg_aGPvwEr52fPhKsPYWV0MugGLadrTEBouAwzyWFqHth9HNp-LXGS2WMb-VzIOBabDUS-GwLlZhCyCwAGR1ec0Ad6bpCvDkLNVsGdXFuk8AG_HfXugqFTIQ99jv6Ks3FkaO1Oyw6gbWI9YjAzNCU4OUAl9DulTff8fxY58L56Sn6-50TqeANMMtu_v4ferVMbFniEX5YiYQkhb46378Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsU8rv9SXfdaDEcjre0cUEBarg1fg2SEPKsqSiZn7R7-l7pHE_RJBW00Ea_ubtIs3fNPYF9_MxjXxoaidEJAH6oa0Kxjq_p0qj7ov_DXHypUW_Wz1UMqy3feVe125EaczqDhGhfvYOUyQ33nvV80yuM-N9qRDmtYWynlB5s6MglEDi-WGr1mdwuB6JTcujROSf4AGChIlyPxfG1mEGUdcNUafSwGWBqXsiyRsnBLZ_U6UjE4AbkX9zuIYzcOGW60tUrOtKjdn0535xKNudNk6-LAd6CTXcg1r8jPfs5yEurhQ2HM0bff5_9rnrTCgbU8yyC2duUeNXaX0GIPpy78yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=oICfMnXFEVRdf-DwLRSXf8vXpn7NUEkYWzMm-q_jTBLm8F8ZySrykvnLlE3bMMk4mAFq0lE-LpOB10QOQGoZGKbuIj_I5uUGhW7fWMttF0u1BUTZELy7Xc6rT00_DMLia77kGnI_OrQUa8TwB5q1VULO1Y79M7pGlpHD816-xv8sLO_yQWySSSsWcOtzPZqQjkjeI9aDKaYfnp0NPdPFqIhEnLT35LnqNZ8lQ2BEupwTN3_fzRg87MkeNFvpCOIlkxmpAMJX_eyIC1pZfb6PBqSCJ__jKevMqg-15p3ymuEa_sOfUgUjYCHbJHPfbM48qZAhNidcY7v76qKic8MxNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=oICfMnXFEVRdf-DwLRSXf8vXpn7NUEkYWzMm-q_jTBLm8F8ZySrykvnLlE3bMMk4mAFq0lE-LpOB10QOQGoZGKbuIj_I5uUGhW7fWMttF0u1BUTZELy7Xc6rT00_DMLia77kGnI_OrQUa8TwB5q1VULO1Y79M7pGlpHD816-xv8sLO_yQWySSSsWcOtzPZqQjkjeI9aDKaYfnp0NPdPFqIhEnLT35LnqNZ8lQ2BEupwTN3_fzRg87MkeNFvpCOIlkxmpAMJX_eyIC1pZfb6PBqSCJ__jKevMqg-15p3ymuEa_sOfUgUjYCHbJHPfbM48qZAhNidcY7v76qKic8MxNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=CDgC_-AVqrzq4UDz-j50YE5dyqMusnY0ArDfsYu5l6DSeMVChMSyoTPyYQFT3S4lZHrM3OyCt6M86mHvXA2AX7Yhf-3gr_HNtp17xrvbwJL7KkQh2u6zreyGjrDj6ViVzwPsuIPa9ezaRec4asswtNwN7Qr0V2yn7OlFGaU1RCXghGICE8IJC3dGoq573_RWUTyrt6MmwSXQk2sfOgPj48XE5aVV3lUft8qSG4OeuJHvie6HQHHUbqPlGSoxzZ9oluGufFn-5b1z40yTVgZvOAhaPn8t7b3fhjK09x6-i0TpjJbYh5Cl-P9sDOZoJgT9I-n4ka-AXc58AWk35blByQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=CDgC_-AVqrzq4UDz-j50YE5dyqMusnY0ArDfsYu5l6DSeMVChMSyoTPyYQFT3S4lZHrM3OyCt6M86mHvXA2AX7Yhf-3gr_HNtp17xrvbwJL7KkQh2u6zreyGjrDj6ViVzwPsuIPa9ezaRec4asswtNwN7Qr0V2yn7OlFGaU1RCXghGICE8IJC3dGoq573_RWUTyrt6MmwSXQk2sfOgPj48XE5aVV3lUft8qSG4OeuJHvie6HQHHUbqPlGSoxzZ9oluGufFn-5b1z40yTVgZvOAhaPn8t7b3fhjK09x6-i0TpjJbYh5Cl-P9sDOZoJgT9I-n4ka-AXc58AWk35blByQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=GEaFrJShCHfdn6o_sGtbRhx6xXvWuJipk0GUPVL_2XgWSmx1yy4kqfTOXGBPcp9aYkc3MEVQMvMGoirABPM3fa0VrnJqfgoQjk--62njYqvY3t9rgXmHEbksr4OBurFTTPpeBUxjiPQHmES9Naxkgh-umGyEHMxaxTgoHntn6XdaVXKF0DWV7tiLv7Vq0tdw996DMDONQ-d-1UgRErN2lweOjtvY2OXt6dtVnCGcQbX5Bo6Pzxs40VMV58yn6Ukiz9kGrgWUiEmDEOKvC3TWKLfy6aralimaZZQun2_XmpKv8mwa_yHVJUgX2C9m0wzchCIj82WRkYyt2BmvTHBk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=GEaFrJShCHfdn6o_sGtbRhx6xXvWuJipk0GUPVL_2XgWSmx1yy4kqfTOXGBPcp9aYkc3MEVQMvMGoirABPM3fa0VrnJqfgoQjk--62njYqvY3t9rgXmHEbksr4OBurFTTPpeBUxjiPQHmES9Naxkgh-umGyEHMxaxTgoHntn6XdaVXKF0DWV7tiLv7Vq0tdw996DMDONQ-d-1UgRErN2lweOjtvY2OXt6dtVnCGcQbX5Bo6Pzxs40VMV58yn6Ukiz9kGrgWUiEmDEOKvC3TWKLfy6aralimaZZQun2_XmpKv8mwa_yHVJUgX2C9m0wzchCIj82WRkYyt2BmvTHBk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=qyYuwAjG1E3APmgpKkvSrRTBTEVZag7s624DrLktKUqr6aV0OBZQNOw56IZepA-4Ze-yFmiDjHN_oU-oUFVA6DxMCDYFKWVsyRusXUQK6iB7G_qlO0MA8NH9fl7FjlBkzrAkDIvoJF_c764jioc1dTM9q_trVIcmbsiXZobBJXBVU3yrbE_VuFQc_II1Xh_Wvv4cwWqSk7WCwO2xfRkx8M3GKakq9hh7VkpVOf8DaIAu0LQ1JQtWvY7ePj5pWEwrI3pzxwNQg9QwJGzitnLh34hOXkdzHF0yrZFmF-b2qfEgkVn3VTB2LU-XNokiqqGH9dJojks4bVLmObcrpVA5lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=qyYuwAjG1E3APmgpKkvSrRTBTEVZag7s624DrLktKUqr6aV0OBZQNOw56IZepA-4Ze-yFmiDjHN_oU-oUFVA6DxMCDYFKWVsyRusXUQK6iB7G_qlO0MA8NH9fl7FjlBkzrAkDIvoJF_c764jioc1dTM9q_trVIcmbsiXZobBJXBVU3yrbE_VuFQc_II1Xh_Wvv4cwWqSk7WCwO2xfRkx8M3GKakq9hh7VkpVOf8DaIAu0LQ1JQtWvY7ePj5pWEwrI3pzxwNQg9QwJGzitnLh34hOXkdzHF0yrZFmF-b2qfEgkVn3VTB2LU-XNokiqqGH9dJojks4bVLmObcrpVA5lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suJ6Z1Jc9QXqHRxB47MBmLvs0ixZoqVaJMT80BB2zv2dN0MsKUd8w-4yfbDrWT7C_IRr9kZh4K0oJbYooirRvdAuP7MuOKyhXKteA_pLqxeyIWzxW5earzWFJeXxrVgkN10qjComTso6VrMzO2w5x3i3NlPqE82ErexVNHKDmD46xXBSt4bMFvdk1KzkWHTdCoF1R-EVALEU1D6M7gI9hZttiKc9157BGrblzCPPpIRfmBJey0MaiqC3GPBtnkCwjBz17TnWa9xArDG_5DqTKNiFjRC2YeIG80aL6DO5gfwmqCdSEtlmhr1JYz22NNPmmeJKGvniQmaM9Zy6ZWxZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=PEeyVRENBGyEgQ7Hv64ehDqJSJijuuqah95rHznHpf4sfCQl2VEASn7xA2QOqa6vDDYK-9yh6wHTehEoQJnF9ni8SH3fPhmSIY-c0hfk9hTGu6FqrNpmdF_zA_syhYx8Z6DUrOrBlZQvi1ysVTdJ9zuKupVsV4xl-C1ZmVWhs7F46MzU4weBsOjZ5r8pf37m2xbaFojN_-eyPFT916Au5heBZTYvOSO62GRGL-JQ9szRkjrI9W93913bSeOD7pthSNCJLna8pk0hVd7Pf82rk5si90dU9p9m-lm7r6ps2bpA_vt7GAQ58ZEOJtQVdAHJMhtTqvji8TcHiikXQG5OPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=PEeyVRENBGyEgQ7Hv64ehDqJSJijuuqah95rHznHpf4sfCQl2VEASn7xA2QOqa6vDDYK-9yh6wHTehEoQJnF9ni8SH3fPhmSIY-c0hfk9hTGu6FqrNpmdF_zA_syhYx8Z6DUrOrBlZQvi1ysVTdJ9zuKupVsV4xl-C1ZmVWhs7F46MzU4weBsOjZ5r8pf37m2xbaFojN_-eyPFT916Au5heBZTYvOSO62GRGL-JQ9szRkjrI9W93913bSeOD7pthSNCJLna8pk0hVd7Pf82rk5si90dU9p9m-lm7r6ps2bpA_vt7GAQ58ZEOJtQVdAHJMhtTqvji8TcHiikXQG5OPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA6vpg2RlobTBxmtezTEzMV4tBDKys8qZdxBYv3a2omkcj35McPk5UDLOHjTKnzBz314prdkjnLm4I0QOWqMziadHAiYrwzYemMbyacfEh9ozZU13j9u2yc2dpIRQE-Krt1NYi0YEW5RIwnXa9Z04700VlpRsFvNcJFJStQ23yeVfziTOPz1zBnO-_uPYd1DEwOtrOKqPSoDl9_3eulyGr9fPF6PWtLBYitTZtbNqWCmHiHk0TY_HuX62QJNOywRcHcmJgSPqIfLv6ScZJBuoCB4sz1JnZxMTgFNBWrqyELGOp30yPARpYBFfSQjtaoN9VDqr5nd3kNOkh_31eC74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=kFRV1jcevPW_e-0W4wKf1Lf-MxgsxO7XjT2_OQnF0Ut1wXOVxqkXN22Ko65wdQ01RRvXH-sOx0FpF-4wUrAccx04PiqDbeqdVvsfLxVM4t1ojxqE-qQ-d-HiwSVE8VDYK4kNgC3sLhPeht4y_1XA3zXilhPQ0xLvCs8xO0bxX1UDotVdVnvmOB_QAb_LsFYFHNdrNSRplKp5cT-F2ZyK3XKjpss0mMCQuXphzgcQ-ZOUIY9-uTJFFNYBezNLPU3-iR3jAD-EFZxMtZs6MVIOCmb-5ygNf_fv5jdkZod9VSEMvlM6u_ucH74auAR4vjqtKNhPrppmZx3aYRrjNbM9AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=kFRV1jcevPW_e-0W4wKf1Lf-MxgsxO7XjT2_OQnF0Ut1wXOVxqkXN22Ko65wdQ01RRvXH-sOx0FpF-4wUrAccx04PiqDbeqdVvsfLxVM4t1ojxqE-qQ-d-HiwSVE8VDYK4kNgC3sLhPeht4y_1XA3zXilhPQ0xLvCs8xO0bxX1UDotVdVnvmOB_QAb_LsFYFHNdrNSRplKp5cT-F2ZyK3XKjpss0mMCQuXphzgcQ-ZOUIY9-uTJFFNYBezNLPU3-iR3jAD-EFZxMtZs6MVIOCmb-5ygNf_fv5jdkZod9VSEMvlM6u_ucH74auAR4vjqtKNhPrppmZx3aYRrjNbM9AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=nZK1HknVAlc349OlBw234xKHDTBL23_EPWwpDwMCX0gtrExXe1fw620WFZsNBD_MIkOLAaqtYVJrXF5aWCg6ZiUtVhzbnZRHUjN_noscdco8FPOrf11zWoEThnbKUbsGR0V9QdI-bRqKohNjNHgb2QdN0wCNwrikwhbTVhhdvMOSr1uAq8y8lPb13XxzmRDCK5eqUq0pCPoci6I0nsHVcwmzMZ58PbZqAOggtXGYnBhP0khrR109hVrK170FFsZIMYMKkaExsR0t19GxEM9OdfMt_8AHRgrD50utihE-4jNBZrs57nInLlAcENiyNDyni9Qw87v7M8_dZBgTt2SZhzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=nZK1HknVAlc349OlBw234xKHDTBL23_EPWwpDwMCX0gtrExXe1fw620WFZsNBD_MIkOLAaqtYVJrXF5aWCg6ZiUtVhzbnZRHUjN_noscdco8FPOrf11zWoEThnbKUbsGR0V9QdI-bRqKohNjNHgb2QdN0wCNwrikwhbTVhhdvMOSr1uAq8y8lPb13XxzmRDCK5eqUq0pCPoci6I0nsHVcwmzMZ58PbZqAOggtXGYnBhP0khrR109hVrK170FFsZIMYMKkaExsR0t19GxEM9OdfMt_8AHRgrD50utihE-4jNBZrs57nInLlAcENiyNDyni9Qw87v7M8_dZBgTt2SZhzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=bjVmcWYLhD75rhxA7ZYAPfZ3yIG0KRBGeg6gxrKUnIdjoZ5XC58a4OSk0j0E7KV5ttnekbQg0f_R6r0b-gMIxeZYOU_EYAdUw_XReita-ljVqq5BIzlAtmm6m7hD7-3Fr6AfXqDBpuSOcSOHptiHE5jk0wm9TP0GDg_Zsw0UMInNfum1dtS36Ty4mcbeffTnAIw7Nu91DepVXEwqv3JPytfF8xzRD4ptvDeuiixcBPc528M8ID8JbB8Jsq2OLqLi8q_QTuF06qT9Zo6b41rM4ltD6yJ2lL-wJ91y6S-at8p6PdOkehcUstlYWBPYQ41nh55aWFNNPZb7n9V9BCluvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=bjVmcWYLhD75rhxA7ZYAPfZ3yIG0KRBGeg6gxrKUnIdjoZ5XC58a4OSk0j0E7KV5ttnekbQg0f_R6r0b-gMIxeZYOU_EYAdUw_XReita-ljVqq5BIzlAtmm6m7hD7-3Fr6AfXqDBpuSOcSOHptiHE5jk0wm9TP0GDg_Zsw0UMInNfum1dtS36Ty4mcbeffTnAIw7Nu91DepVXEwqv3JPytfF8xzRD4ptvDeuiixcBPc528M8ID8JbB8Jsq2OLqLi8q_QTuF06qT9Zo6b41rM4ltD6yJ2lL-wJ91y6S-at8p6PdOkehcUstlYWBPYQ41nh55aWFNNPZb7n9V9BCluvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=tq-dxHVto0ucTrxI9vsdOKuewffP_LD8-BGVoVJod1ChzEPcaFSkU-1Y7zNzwnxAD3bYJSk1YbyFHZQBisTXvDAuoCsVa8u2eholsKVPJlqjmE1AFx9zZoKo6XiWTlKkJI5c__SSbMm7UIEe_lRJgCXPlT662UOQmdeSD9jKiXkvrO63YIyQokhEYuGAeVtSuDT95q3Y9saILDWinteZv5UKdHRhRymKThqyMMJas158w0LhCHN9YQhx4xMLjeIsPJLAdK-enfH7q0HvaIePdgmTi3LKnIxVcRxFv9MW0HoqEoZhrs079gHRhKXE61jwK03QIetgjAJu-Q65wS1-GWugpbktXftA9ZOM9YGFcv1lDwbSPUCtlVbPm8fEDFBXVVGazpckpCPRym4ty2glws6FEFKJOLhaJCmfKKJvtycT9fc1wBxpBj61MLtJJ77uKhMqXQOxJD3-CK0SFOZD_xwIiU3PFnclq5N80dQxTagUKJlDc4qA4BTur37YCtEVSFVM3tlA9UKgtPRdNHwn2qxL0VgMGqusLMv7PBfpqqiH5StQHXbJXOy1j6N6VRWAAB58IH_rVj1l63NH5UG9dRDNuVnMXL41LN4x5ETaIYTGHeNlYZqYQRvUkfUIhOD1kS86IelzzZyPAClF-vXpDGKxPhfXLH6ZUChMKjwwWps" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=tq-dxHVto0ucTrxI9vsdOKuewffP_LD8-BGVoVJod1ChzEPcaFSkU-1Y7zNzwnxAD3bYJSk1YbyFHZQBisTXvDAuoCsVa8u2eholsKVPJlqjmE1AFx9zZoKo6XiWTlKkJI5c__SSbMm7UIEe_lRJgCXPlT662UOQmdeSD9jKiXkvrO63YIyQokhEYuGAeVtSuDT95q3Y9saILDWinteZv5UKdHRhRymKThqyMMJas158w0LhCHN9YQhx4xMLjeIsPJLAdK-enfH7q0HvaIePdgmTi3LKnIxVcRxFv9MW0HoqEoZhrs079gHRhKXE61jwK03QIetgjAJu-Q65wS1-GWugpbktXftA9ZOM9YGFcv1lDwbSPUCtlVbPm8fEDFBXVVGazpckpCPRym4ty2glws6FEFKJOLhaJCmfKKJvtycT9fc1wBxpBj61MLtJJ77uKhMqXQOxJD3-CK0SFOZD_xwIiU3PFnclq5N80dQxTagUKJlDc4qA4BTur37YCtEVSFVM3tlA9UKgtPRdNHwn2qxL0VgMGqusLMv7PBfpqqiH5StQHXbJXOy1j6N6VRWAAB58IH_rVj1l63NH5UG9dRDNuVnMXL41LN4x5ETaIYTGHeNlYZqYQRvUkfUIhOD1kS86IelzzZyPAClF-vXpDGKxPhfXLH6ZUChMKjwwWps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCSeCaol8IifRqxlKkKVd7nagft-laMNEYIVLfKgI5taLNXR7r43Hsu_ewx7545RGDL_eg-WFZDDkjXbX04YBK6T-B815_RAH17hHwm2FHij6QJxBoNwPSEw3S166SzaXSMsxx4wVMIRj52RyoQvu-LHESkhxA2EtTaGzO3dClrROKL3JNPbo9yY5p-EoXDZH4vJC4GZV_sIf-LK2YILjALqpGWHws2Bed0x3SDLVlIUSc5yt3w6n6ghq60sZC1EH1acL5IMmmiVJOJTRo9ZOq0nJyp7db_EpKg-nsdKCxBOGIcge5-prpo3_RsqDVhaZ08gZXxpVRdBxlxeVq30zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=bftYJogokKgwag_zD7k9pZzyjE2guV-EOgcE3KtkdIMub42rrF9vTQS49wx3VN4MS7UFGg1psHUUbkgrp9WmoSDJR_4Wffxvvf3t0Wfj1A-Q-Sdojp9zwqN79Uhz0trxGG8N8qs8KSAnMU8T4bcPa879wvJ5z3N8vKk7aaJqFt9J9i_oa68uFdnRFa5RiVIEdyv810FC-gWCw4-aDUxqd4ZpnGsiOE1i3MtsJAtQ4yIP6UJ3kW_LLwAzvPbREl5mm9zolK8Ru7oP0l90noStJ9q6e9oU-oeEbC0lIcyo6h7b4r7QolSHIn-mNC0VOoYskJJ6Z_zTX8GRXkKxTsMyxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=bftYJogokKgwag_zD7k9pZzyjE2guV-EOgcE3KtkdIMub42rrF9vTQS49wx3VN4MS7UFGg1psHUUbkgrp9WmoSDJR_4Wffxvvf3t0Wfj1A-Q-Sdojp9zwqN79Uhz0trxGG8N8qs8KSAnMU8T4bcPa879wvJ5z3N8vKk7aaJqFt9J9i_oa68uFdnRFa5RiVIEdyv810FC-gWCw4-aDUxqd4ZpnGsiOE1i3MtsJAtQ4yIP6UJ3kW_LLwAzvPbREl5mm9zolK8Ru7oP0l90noStJ9q6e9oU-oeEbC0lIcyo6h7b4r7QolSHIn-mNC0VOoYskJJ6Z_zTX8GRXkKxTsMyxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcBFYkJqss2PRaorDZtAO228J2sKgpol6qPgUyMakkE-xkwNVn4H1LmAryjHZ1ceuCpcNCy4o1tL0VsxT-LSEbCNxIP5Oz94pcRTtUzg13NqOvaxWMVRKxsmDCXS1EAOt6xAEW0E-oBbVoClSIJegb8ERUfRHpXgk2B3lwlti96pgaPRjhUXzzDDqN_YKC21KDDtdUeE_qZ8SmoWOf5qWS0hs9D3hOWNeUwNE9dq-XvjYraQltRSm6kuwSo7fW4xy_hNE7iCUY63h_VrbSsvh0oIOFAK-yZr9VqqrX5cFhqsbk2deIReY-dnYoc6FkRUImqJPKxu0rgOu0CZYj1DlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGKAF7n96J_N1Kyg-OL9n-6L2mT9vS3ZbQTpi6p-8FD2HzyfSqU1oWYp8jXP9i2vXgb7D-a-QmH_3w5AmZZmzn7Qo-n_mEPOOQ_NxZVwSCgpkIfWBtg7ONTDJGAvnNlUPysOUas-w4z6vGdv2N5DtUcgRrkobMCk9H9wbtm2iWlSbI4gYEQEezQDjEMHeHxzYdgwXJqi_vhofDPf7xOa9dCcQb3JGgEVmugRhNBHYnJYDdc5FCyM6yysGzNfnLFleu_VJmfYbazHJlNPZHMdJqDxGWgglYpaRwzayliXVrzEhqA8Pb_DsE3O4yQr6yEy2RGnsMlyp9ehs8t0FXyl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXdEXh2eiPIRkPFoEBaTs3kc1BbdFKaynB9jQUJ2zw1bQePO3Y1o--U-Sd1mKjdJvWIORKttciMayR6VCHVQtXAZlEMotf8MhsjXUlTkSZO-L9J9kIKwBCwCPtPMiHoNXqmiC2KZ7v_4T9I1frDWww4ZbPpvWsljr0isVNTGkDaZIfnvvJ3hqNOL3LwN5IJTYCu8fSZiKdrs0mxZbxcxqPSb3luwyYhce0t5rYTGZ4RVHXk4YKvTivw6A-8h_s2LQtndoChcIH0YPeIOcnOQ7Dsk8kN665uvIY1vkDsO029LTqdCCar2ltd_Rgq04N4jxOJIOV5Cv-iyVVgPwftP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDT7aJYh6Ho_VAJf_NtA3ItzaZhyKM9RFa1oWBeNbKNvHa3e_8HaWKr2wq-ooce4nvl8MYtDh89lqUtcEhSAeXqXmGAU5Kg1Qr7gMxdWjup5-LGfQCa3yZtBhYj7efkIr8CDvO-7jVItfpC4d1-c1V2FuZY3I0F6ob2uf2twocDvtia7xTt5ffMtbNC2yZeoHvYFQck5HjEJDAcErvCglHRFHLGDB0rSS5L_nsf2Zpimbb2KmH0nsalKMQ_UW-nJmJOVOfx8cTenSiGff254wEtSPe7eYqUmPdHAMqrI3RI2Jncs6aaMzHAO00147k0ca85Lp_dxuuExrD18Ymwmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aT27M5Y2EK_8C4WYxQPy0Tr-nRHfz37oEFJhMfhj9VM4_Vqk3Ey8-pvJIc8w2_mlkYkdUHSVAbOVgs3f6gv9gYUr0Ue_K162tbPTdsV7391V62WIuiRcijZuy5UQmtABrFsD-E0LPpHbsYgVSL-QfAnI_7lqBO2ZbKNJxnP6ftGJjohuezPmqy-nX5QTOplC3JFW8cPA_vGFH2M8ofNxLLE8661Ge5V9XWez_VmcwLHmUVrPf1Jy7bmg0Te-_xz5bre9kJcaIbM4viXj2BCZklWisfJujLXoxoDz_rPVZFqta088VvlGPCVVDWj22s_854jfCdr1-szQBxtYm3nF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiJG4htpg8adWV-2XajDhe0cUo6-I9s8e63n4sPvUk5_6x52njtPF9BSQwKrl8LrD2DmmISmpCB8OlSBxvwkl9H8rg5_mJ69wMaEmxRXSsmrFqAhLnIn4OiOxhuN6ccf1pvjFW3PnKbsMl1-zCwYVNebmIGdPwNmjiX4obeIRuKnqMK6o66hmjWpPShkSJCyVrjdugIBSJfngMgUXeC86bhMZzKhKSi3m0nTBeOgtM8Ozlbwhu-8b58aBCODE2bZwvtH3pcvefvOh6SGkDHY0uIlIv7tp3qlA4kkwADTuWu2dPXSzH6kMdfzW2Ta3erd61PbHWZLIxfSQAYd-0_AnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=DIpHxddBj2iBo0YX2plechY4UL_6yU4AUi3QLig4AtMxdGmJC96MJcM9AmHGKD4lLuo9spmGvCTg3nF4jlZzmQYJA46zFfcfJ7JpXnT0PtIVzy5RWTCioWlJ2syIMydYARiX77ka4id4OOdrzijkzwecyLPBlil_PSaOvBepgna694beZnBTrGmWfFNpcGxy61sPjcAnztd5D97xnzCD-Mx5fGXTrXD8mkqRjOqdQW7dLvMDYM4_64lDEb7zOkTmSeryNEyXgEDu-q1F-Wq6FNTVsKbQp41s5M5u6Tko5DQloOkI5W7EyqoxZDVV0Im-4KszeKGPeWplt7fdGIBOKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=DIpHxddBj2iBo0YX2plechY4UL_6yU4AUi3QLig4AtMxdGmJC96MJcM9AmHGKD4lLuo9spmGvCTg3nF4jlZzmQYJA46zFfcfJ7JpXnT0PtIVzy5RWTCioWlJ2syIMydYARiX77ka4id4OOdrzijkzwecyLPBlil_PSaOvBepgna694beZnBTrGmWfFNpcGxy61sPjcAnztd5D97xnzCD-Mx5fGXTrXD8mkqRjOqdQW7dLvMDYM4_64lDEb7zOkTmSeryNEyXgEDu-q1F-Wq6FNTVsKbQp41s5M5u6Tko5DQloOkI5W7EyqoxZDVV0Im-4KszeKGPeWplt7fdGIBOKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=eU6Bsj-TDNfyFGQwl82dGO7rHNC-ZfFOZt3hQ88Jj7CyO063oJqPQMIoj3nB79BiRgLCAFzb6-0XXo7VSV7W6caF02DVgZJQ8w9U2RFTSXL0_D2rl_YKZYd_GSymlTPGpIYXlEH_MXcJGVFjIh80AOZNJ2nghXcbdkfYhhBW3BG-jmFcVtO5p76HayEIw_CIXM9h8i9QMIP9PkQABSgwleBdxvMmrT4Z7UBLQBdBmhYQzgj2KbhFBevcF1IPzKEOzWxt4g2uMtvXfm2lnRgb4FTC6dJmPtBCCV3JN1XJ1UkTDlx4YR92a6tRPOtFj5tuzEPu85RclMbGY_MjzudSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=eU6Bsj-TDNfyFGQwl82dGO7rHNC-ZfFOZt3hQ88Jj7CyO063oJqPQMIoj3nB79BiRgLCAFzb6-0XXo7VSV7W6caF02DVgZJQ8w9U2RFTSXL0_D2rl_YKZYd_GSymlTPGpIYXlEH_MXcJGVFjIh80AOZNJ2nghXcbdkfYhhBW3BG-jmFcVtO5p76HayEIw_CIXM9h8i9QMIP9PkQABSgwleBdxvMmrT4Z7UBLQBdBmhYQzgj2KbhFBevcF1IPzKEOzWxt4g2uMtvXfm2lnRgb4FTC6dJmPtBCCV3JN1XJ1UkTDlx4YR92a6tRPOtFj5tuzEPu85RclMbGY_MjzudSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=Yk8-t3TBwTuyISPJ4DdHWjxfv1_teq2tfVxFUx8wTO-_NVqZJ0NTPqUfv4wAKCsdY2HictwUCsE8DwYWCt52gNhLw4UelBEXFFIRPx633UjcvtrGbGyHXdamLRZzQbW5peaXtkWj8Vb0Ijdf0z1JtNXV2B8ZccfSPLqrmr6pnrxo3qXPAGd0EpSZW0uvsznUbljJoLXxbmB1Z4q9_AVEB1jgs7eO2Ns0thZJV0LdqHm3Vi3YQY3uoN43L-KmIWHllMs4NLb9UuTESCbsX706quqpGb7QhIQGoCMeD5A6eC7yOROf1bAvdI3ymzrPbE3AVSyKwrFzJyJ1XuJAH8hzJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=Yk8-t3TBwTuyISPJ4DdHWjxfv1_teq2tfVxFUx8wTO-_NVqZJ0NTPqUfv4wAKCsdY2HictwUCsE8DwYWCt52gNhLw4UelBEXFFIRPx633UjcvtrGbGyHXdamLRZzQbW5peaXtkWj8Vb0Ijdf0z1JtNXV2B8ZccfSPLqrmr6pnrxo3qXPAGd0EpSZW0uvsznUbljJoLXxbmB1Z4q9_AVEB1jgs7eO2Ns0thZJV0LdqHm3Vi3YQY3uoN43L-KmIWHllMs4NLb9UuTESCbsX706quqpGb7QhIQGoCMeD5A6eC7yOROf1bAvdI3ymzrPbE3AVSyKwrFzJyJ1XuJAH8hzJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=vinWmQJsydQ5VOaNforg__UwOPobip7I7OAGi2GgGd8h3iSKpEc5_x6Cgon7UrakmL_73Kwee9i5AQPeORghxc3SYq_7NF7cNmJI6dH6a0PLkCEirYyRQnaG5jfwETHf4vtZFX_PsDGrKaGJQgOqTyJW2Pj6s2rLzh305SK_5-gzMV7LebSDLHpNOXiL1ULn2uWZQS0k6jCbGoVeRZtjcaR21Ro-itoBHRBJOTHC-VyzKbRGyr-HXbrqH1dJ4xfJxfN-ES_pug2B8YsNdMPu9vYCwhSVxcwlYNo9v-MIY-8jo2SDr2Qm_YNihK9dDHHWDLe2k1pl55ZOHeJIe3AwYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=vinWmQJsydQ5VOaNforg__UwOPobip7I7OAGi2GgGd8h3iSKpEc5_x6Cgon7UrakmL_73Kwee9i5AQPeORghxc3SYq_7NF7cNmJI6dH6a0PLkCEirYyRQnaG5jfwETHf4vtZFX_PsDGrKaGJQgOqTyJW2Pj6s2rLzh305SK_5-gzMV7LebSDLHpNOXiL1ULn2uWZQS0k6jCbGoVeRZtjcaR21Ro-itoBHRBJOTHC-VyzKbRGyr-HXbrqH1dJ4xfJxfN-ES_pug2B8YsNdMPu9vYCwhSVxcwlYNo9v-MIY-8jo2SDr2Qm_YNihK9dDHHWDLe2k1pl55ZOHeJIe3AwYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=M9FtfN2yNOQOCYe-PNZz0s5Fu5h8wGQaTMVu1Ed_4Sh85NyptM51z9ea3E_CYiV6LJ8J3xszr8Au3y6dmadoBLEtzw5t8R_lfouE_MgEZTsmdWBu3qbGDF1fDkkQV4mUqOQr0qBP6uWxVfGZoUtOfhvapkI6ztS0M3Of195wu__Mi2I_eqnwEfmHNg0W3Jv0CBqmXXbRnRQAW72ylk16XZEpfAFltbIuf6xy6gslghc3-kpv-PHfhlaHHXx_Ddrs7V2N7BWTVxviQf-7iA6liUd91yOtQBx-fdruonULXC8mZJL_ZmSXFdM7Oxy_tm9Lu7xkHBPur3sSF0rPj9kJ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=M9FtfN2yNOQOCYe-PNZz0s5Fu5h8wGQaTMVu1Ed_4Sh85NyptM51z9ea3E_CYiV6LJ8J3xszr8Au3y6dmadoBLEtzw5t8R_lfouE_MgEZTsmdWBu3qbGDF1fDkkQV4mUqOQr0qBP6uWxVfGZoUtOfhvapkI6ztS0M3Of195wu__Mi2I_eqnwEfmHNg0W3Jv0CBqmXXbRnRQAW72ylk16XZEpfAFltbIuf6xy6gslghc3-kpv-PHfhlaHHXx_Ddrs7V2N7BWTVxviQf-7iA6liUd91yOtQBx-fdruonULXC8mZJL_ZmSXFdM7Oxy_tm9Lu7xkHBPur3sSF0rPj9kJ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=Zz7cHZw-deCoE8LU1OQG2rpIcvh8G1A9K024bvBoJUJLzE_cKNnOsWIzA7ZUhlr-EhofepwRUGzvJGO-NImXQpcG-wIOd-VTnN6tSXV1owOzHlCrPVT_7Jpdfgrp4ATRtqLhENvngBhieg2VbliPLhZiUSrx7M9COk8Cj5BIigmeOMpo9-bK1p5uMHCzZ8f48Y24fb9VTb3m59kSfhrphQfqwrHPcjRtrD4veE9GlgF_rmwM5HtOWt1SmRxn1WSdSL_T4m1x5W6fmU0Ld7gqhOEVM_FFF1Wh_crm0TDH6nGKmoupvIGN3SVz1o1MI3tSwseUf2TO-j9eoDlKrl9tTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=Zz7cHZw-deCoE8LU1OQG2rpIcvh8G1A9K024bvBoJUJLzE_cKNnOsWIzA7ZUhlr-EhofepwRUGzvJGO-NImXQpcG-wIOd-VTnN6tSXV1owOzHlCrPVT_7Jpdfgrp4ATRtqLhENvngBhieg2VbliPLhZiUSrx7M9COk8Cj5BIigmeOMpo9-bK1p5uMHCzZ8f48Y24fb9VTb3m59kSfhrphQfqwrHPcjRtrD4veE9GlgF_rmwM5HtOWt1SmRxn1WSdSL_T4m1x5W6fmU0Ld7gqhOEVM_FFF1Wh_crm0TDH6nGKmoupvIGN3SVz1o1MI3tSwseUf2TO-j9eoDlKrl9tTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quTpeL8e12Ww3cdf_kRPdDraqwZ-2mgWkAKzoT1akPq1yfTuhGLVNsyWFXaRYQT7GncYNWFVVveHPs-yedUi3LqNoa8GuDc9-N6ptoaqSUyaTPqXgVClpP1khj0qL8E3uFlLiSl8MKwDz9XvsXkvC-CS4YOHOTN-_jqLwHRefbZiRdGNaENQnvYiAIqJzJngWwVpyiCKVBqZxKZ-kXHi2-SCKzIfDw5T6J1FUiyEaFMuYuJsn26VsJVF36D4xLkpF6I4VUb-T8piZ8k4_pmM7Eh09RujMBosdphh_Px_50gTL2lfXOmN2eq6AmxmmFtOs9x5yaZkiSWEQKh1q7eAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esN6MHA4f7REhgm5nDSImND3o0pJQW10z8V965uNT0rauu8BmfjCsXOgOA96HlXdhSuWpynL6jg2s-5wxEYshvEcTKF2xIps3Wq_hpXB67JKsWTyrGoJdrLD23aPWPf9hniwk_p3fG5cVAHvzFsN56f_tdGRwEx0VZyRQjs9qTGWizCPy_u_-qejjLpx5M7a1yvqth-RzvjoMDwUe1K56X950t8E_XOWGllNqjOtWl0Bd8icwCRRDbJQ-mbk5ugX-g-9ntlybe4hCpSVrlYMqqaF4KMC8O95meqBH7M9YArz9snujpdDx-Mzyszjf5sUy2MfN_kifMjsRRBf-TL_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4kpM4YX81ge-GNuwQkdnfwBfDwRPUWtDTNTS9VZwNu5zWa8NpAytOGsEsIZ2FWf30OFh99EWtJQCCITahuLU0SUgzvU9vmMfkMOgrVIzbIRbql_RNSyQhjEa8n7_3rANdLuzbd-bRa0gvjDmK2L7mM08F9kYqA1syIA8wk3NsRMt2gkw1PX4a1jg0EeLF2UJoHTPJqtfbqzyERREsPosml7qyARvMKVRB9aITCstMBlit_ArqAD9HI2huuPTGAQxa5qy5gcjbtA3I6Poegb1JKzFPn8hDnKryPBQ1XkXpI-0GgOMEHWooHKQ2LTbE4CzHyy3Xzl6XCWxwxfLTGhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=D5EU7hU3A-ccFMD414T7gfH040WzYbRp2-6xVWXC_lktO95Maem6cV2GAfFcXn9iOwFQtLqUZHoPPssH_lrZD1xKw9e8tr-ZvUO3RGxsmmuex_bCQq5nFUwo99uNiZTxLFJHqbivz30bv9YtW_xQ7r5XtjgH4-Nc49urykTaohzVAfz2olR7LKtqaaELMikOo-WUbZLUtFNpjDL291dhp-HBeONiHNNiKjbcyTvn0QHwkEbKSiVo24SoGkJvXauh9U00JsT0Ney5JWMPZ95anujFtYMEepOUMukmC5Oi5U5LJ7H3FM8D_YH5E6eaZ-_bZX44xVrAWCipGTk0_qLbcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=D5EU7hU3A-ccFMD414T7gfH040WzYbRp2-6xVWXC_lktO95Maem6cV2GAfFcXn9iOwFQtLqUZHoPPssH_lrZD1xKw9e8tr-ZvUO3RGxsmmuex_bCQq5nFUwo99uNiZTxLFJHqbivz30bv9YtW_xQ7r5XtjgH4-Nc49urykTaohzVAfz2olR7LKtqaaELMikOo-WUbZLUtFNpjDL291dhp-HBeONiHNNiKjbcyTvn0QHwkEbKSiVo24SoGkJvXauh9U00JsT0Ney5JWMPZ95anujFtYMEepOUMukmC5Oi5U5LJ7H3FM8D_YH5E6eaZ-_bZX44xVrAWCipGTk0_qLbcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaRdABb6WqWY0-7DyY8dRrjztCBEkNe_eK9vayYoZaXLlzqKk664qNdgmRfeqPUt3dAlL09IfhQnzEB_-Wt5NEnq_LHNekgEd_ghhdiLXPvXftBSBFdG2McpUOK26KBtQGe-G35JfiT-OaamHDTPDTtChJhPWAGxdOGWqZ-Ds_RNRv5ywv_xf4ir6YnXUGJy9DuDxLNrPTx2mhJyRjFu3Zojz6zoUpQSOXHuAQCnwJ3EqW8Nkw3mAZITLM-8h22GPm7Qb0g0752vnM2oS1RsGCLoW5eZaH5MuT3nUzagOfNEeras1mH4IFNcn3Ic5v_NUfFuQQg07RFaFqSPCVTOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHjfFS5Nq4fmU4giyWISnKb5FYydz93YiAciObJisnSNzd3jeQ-aRpptQ9KqrozAJdtHAPSRp2jX7p8XXPw1xpCXCde7KOYXRmcLOFaF-u00JJ1-yiZJM08Hh_oH4U_KddzrqIbgqrwSdGcjsIC42dpk_mLTZyGfuVFNAqjSUNbHkJ1F7TKBYPgVJxdIqdfuh8nfKjhZZI6Ur9fKUCTUXprZ7vMp2W6Z4U1x9-Sw4EwTR19YmX4gfbOl7Rrp_6l8rhq_gFZrce-XEzit0dfyY_tLomFmAz8F5dOAiAWLOmkCR2-WcK0Xt9P519neF1AaZySgzignS_TqVakHOYN-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=S5nN507AHP1KjOv3GUKn-I3PrsqcYZ8hJKFZnqZC-v7VZ7mC7k-aQJCj8Yieb_1QDVHVk5X0LgQ0oxNGgF8tIr54Ag5-AVcS7nFAW9ESq5CRlVnKu5pqWYptl9C0cZXxP2a9MoO1NIYWLqFHK6MwYdayIHEJzAIIBq996UmjAnOdIFlvQPH3RJREupTDg3lPewDXymYA176jE4fvTjJn41WzEnYSPxIvYowRYaEMBoxCwN1d9MhCtheLQaZYkKjEGN99lAtuKJSDbRA5UMbbPGOuk6UbbWAeL3DzoiFX5qbfta2t-A8Y50CHdAL9KwR7Y-_LpE-W6dawtOirIKZuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=S5nN507AHP1KjOv3GUKn-I3PrsqcYZ8hJKFZnqZC-v7VZ7mC7k-aQJCj8Yieb_1QDVHVk5X0LgQ0oxNGgF8tIr54Ag5-AVcS7nFAW9ESq5CRlVnKu5pqWYptl9C0cZXxP2a9MoO1NIYWLqFHK6MwYdayIHEJzAIIBq996UmjAnOdIFlvQPH3RJREupTDg3lPewDXymYA176jE4fvTjJn41WzEnYSPxIvYowRYaEMBoxCwN1d9MhCtheLQaZYkKjEGN99lAtuKJSDbRA5UMbbPGOuk6UbbWAeL3DzoiFX5qbfta2t-A8Y50CHdAL9KwR7Y-_LpE-W6dawtOirIKZuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPbNem9eUpqyq_FlbSM7bLssApIOyxD4yXV0P7WHGlboPJqwy2C_pm6bB8wNDg0hFibarCmHVggCgPy-vDviR5AaL8r2OPaHDun8GLwzBZ9cyCCmWQKHVDIBn6ccEGyLLgrfO_NIbQPJoQv2u2vLP0ZEYNmmBlx4XInob8_8dWUKQ3dQ23NFvNoU8dIXJG5K3LMY4_Xz1XCUzRrQkfgNjipx4K_ZqGwgE2u9wwJ_0At851sWGXIB3f3v8cSP7yDPeTfAdX1gm7nLl18YcLTNI9IPoloV_3eFczuMp9G5emKGazqE4BocJswt9uAFVUAbv0z9po9WrpY5sgZqDxXoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbUinOGimDHtxsT_XhxihmdRz9bYrWBAx9VP_LGTs1MB-ndtdop7vFyyVjbRhDKKJtE7NkExBBZ48msXvZ8l6OwABVOezU-jUNCo7hDnKIayo5fXRCg25nOZLHWAHd4VNheBsRW1-WmZD1QIMGpaWHOo_ZOe6EnYYmuttgkjAoK10LKwm7u9ii0OfDXqCBgP3LLQqTn4tfbkgbRoKD7f8l8Zo74pOkQbUZ2aVvpdYCsgEA5QJh939wt5Y68ZfG9e3f-2a6ecS78WmLPmgWFXTwjdzMN-r576F9rGmSL57sAJn35ILXwOdDThm3yqC81EN4xPopTNOdMjtHukrIJkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kig8YLO3fsljQvnt8XDRueZdJiAXOQUBQmw_qDXzCSBda23T3hNKd_hRPPd2vrcIyLBpawG5mWqVSoJzd-x4nEM6nWz0Ist1VewQzqhwoUjh3mlxd6Xb3B-Kf7MxZ6z0LlTPvxqoODOdRt2jKa18xa-AXBbOVofc5zeq8pWBt-4ErXQBcyshslxflkCI5jjis80gHXU0SNAiZ7ovZ4H7LnrPBrAIqPq9iDkH0DOVcArwNUJv2C9EZQC7ZxCoQAktRp3s4T_c1g05g9weVxDOZIHA1_I2qOcss94ImWBBpEWSGcq2vpvMotFJkzWbYishsVsRd7d19cZ16imItd0PMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUtE2ylgIBGyttv43Aa_c6xIiLgNBV0eFJeTmSmBn4w7IncTKfbTzhv4gdTezaOglAFVUHB2hCSOe-BBoMx-rMpWS8Foc6vo3M4-XeBNCfirh6bffJ2wOmYxBnjnlUX0Tual0VWUVLl91R96km6tFlG0FTq0NpJh5RTzpo_MB9tBnDrmvP_KuteRngxwfWmtsvMPLvYEiB6MOPqzee2JPpRCmuqQjQA3Ch1Y6ydpJTzHD4MpkobCwHkBqPajiybsbvVRUUC_H9SoSebE6cE9h_XeYZfj3EPE-RRDyQpi5_-fS0JqyiJxFG0AvXm3FgPda9ZRw8KBqR9-ncJcyQLsUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=WBmZ15DDdmOHaWwU2HzdNR0XDu7yemaRAS8SU2WsJrI56mAvSFxhB3kEmY6ZiwW2anvO0Nb3iS0sZ1NP25rmsLtY7-hmS-LO_DKD4UbzUvvQItF50R9SrNnsxY-8ZU9ES1hZ6bDVYh4ELjegY1VJl_asAOJNIWPerQ8-eTDvZjuTwEpEdwVT_DZcdYdyHC-vC2t_5B3fflvhTcCYPme1cWAbJgh1uFPc6340gQTa-aT-M9flstWimq7KRyd_HlTzwi68gIoTqI9OlI0px2J_eyIKBiRLmSCEC3zl642ooh4uEmEvpHvsfk24eRW-Jhf2Ge8MiCrlXcq35s0hmy2aGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=WBmZ15DDdmOHaWwU2HzdNR0XDu7yemaRAS8SU2WsJrI56mAvSFxhB3kEmY6ZiwW2anvO0Nb3iS0sZ1NP25rmsLtY7-hmS-LO_DKD4UbzUvvQItF50R9SrNnsxY-8ZU9ES1hZ6bDVYh4ELjegY1VJl_asAOJNIWPerQ8-eTDvZjuTwEpEdwVT_DZcdYdyHC-vC2t_5B3fflvhTcCYPme1cWAbJgh1uFPc6340gQTa-aT-M9flstWimq7KRyd_HlTzwi68gIoTqI9OlI0px2J_eyIKBiRLmSCEC3zl642ooh4uEmEvpHvsfk24eRW-Jhf2Ge8MiCrlXcq35s0hmy2aGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=CTo_jtNZctJnBvSxleFA6L7u_wczKNVFduJp4EThCCgEgN6PXThIA6Yc3eIIfM-C5HmMwGrppHjzApvpbkumKdOlcaKmRAoOWBeSdDiCbcoFMXRX99DiS5aQaxucBGd3qLf0FKdVGyM98aTTB8rlgCwo34pPnN8nuouIldUKMiorVnEQNx9hNUFivvTDgT2bHUm1Cdg7uzShbFbNLFoG2MaNIPb8L1XNapPwkuusaHvjaOGJk7YzxhHkGKDvP0j1I9-ywDwj3ABRYJuE350Tmi2Xh7FxFeaztJ2KmzVfNbX5DWU6289sJsyPTUQxT1fhXbGd_uxY1b6wW03GOIgLvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=CTo_jtNZctJnBvSxleFA6L7u_wczKNVFduJp4EThCCgEgN6PXThIA6Yc3eIIfM-C5HmMwGrppHjzApvpbkumKdOlcaKmRAoOWBeSdDiCbcoFMXRX99DiS5aQaxucBGd3qLf0FKdVGyM98aTTB8rlgCwo34pPnN8nuouIldUKMiorVnEQNx9hNUFivvTDgT2bHUm1Cdg7uzShbFbNLFoG2MaNIPb8L1XNapPwkuusaHvjaOGJk7YzxhHkGKDvP0j1I9-ywDwj3ABRYJuE350Tmi2Xh7FxFeaztJ2KmzVfNbX5DWU6289sJsyPTUQxT1fhXbGd_uxY1b6wW03GOIgLvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUVba9koLLWvzN3eIG_zDyYEAGWMTY1Ii-pMQZLA3zvvo6YxIC5oUUXAZnfKN_WK7wsvT9ZadonMv2GQlAkdZ9Io8qm81U7SQT7d4q0MGsecghDADmHCVRNB1UCBe6SkxQMBLh4BuvZ05TxgO4JFJD7-ouUC7N_UmsY_EiRkYt5-rtC2Cj4c7PjzYBBGWZK6mLxEJgt0Ob-HSZh_hBZOmuYBqHaFnsDvsfrysPnjfbL6PLNrYIfsg-jVgIO2cttP6lXPY9PO_-VN09Dy177onwn-MP236F76L_rZ-Tfz-cczUkiGwkvWt7NcC7IKCWRaExoL_sKSF_kxmG1StXubOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=Qt2R0EnHvJbX_zUaY3wGm0fZzwa7Ov9IbAhWutGYZ-NQzO2GUiGjca2OL4gRbqqMjoPb8l4-AlLGLICcu4rHE1vE-7V1ZPQfe0T8uyVYl5QQmPCiL2DEB53_rOqUe_iLO4D5_kbtsf2ERpo7PWXWkSM3eviPR29vpQ9qnG-x7LdzOCCW4EPdE4qEe-CEd7wS68BBm9Q43lm5GURVLx4WtjMvTDfYBJyWN2IP3rCKYrpjRMZFCurwAY3L6JeL5WkgfBgVqT1HmkHRYwkmSdI04g4BolSIUYVsL_obYVSbj1xchP7vpr8SBXJfo9PJw0Agqdlbjv2myjo2PXPAk61bJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=Qt2R0EnHvJbX_zUaY3wGm0fZzwa7Ov9IbAhWutGYZ-NQzO2GUiGjca2OL4gRbqqMjoPb8l4-AlLGLICcu4rHE1vE-7V1ZPQfe0T8uyVYl5QQmPCiL2DEB53_rOqUe_iLO4D5_kbtsf2ERpo7PWXWkSM3eviPR29vpQ9qnG-x7LdzOCCW4EPdE4qEe-CEd7wS68BBm9Q43lm5GURVLx4WtjMvTDfYBJyWN2IP3rCKYrpjRMZFCurwAY3L6JeL5WkgfBgVqT1HmkHRYwkmSdI04g4BolSIUYVsL_obYVSbj1xchP7vpr8SBXJfo9PJw0Agqdlbjv2myjo2PXPAk61bJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=OuFbuqsIPxS4VXmv0vQ37o7IWl4XGeyYMNItfXyI2b_M91BHrbF73LcUDhHLk1rkZgddaSo49_eXDmuh1RLtpurkEIsVDy1Ie8Kj51g2ZwSePzqOsZnTx7EngVpuvrB5YDNCnmdpFzjbQjTVSTqjGV3F_uTRbF2VtSetgRmjQOYfnnN0vhFwA5Mc5lDzSQYIi0rO7Y9CwP7784Z8ylDgr1KQrysG-L6K7aJyba-Hh41Dh5KLmw-O22ullUzn8_MhbVejEHaaZf3DoG54tQqf4E_V8Mj69zaNCaOh8hrpBm1jCsmvqR0Fb1OV7MlfWDNYGMCN3stK3wS3sLsy1QX9KgmbO75SMtVhCIgEYWVFiyOUU4CGKU4v_JgZ6jkL9Df2k2ubv9L0Xk-ndKvAHIExcibK0sJWZWfaGR6KXxuPmhmrMXxGWCtP1ZeT1ApJVFLzo_PBzJXTc_9Gs3tb8byhiShXzHQs80jVoii6QMcvT9cInVmD7eFgTv8s4oRjKMIwZcMtFU5TxmH0m_r5PaZvV21hZuBhv92RgLVwkRYRToNFn9yAROWY0Ack238vQ096AKYars_osmHfve4Vw1tEJ-TvDXPopCUSdPQaGedgQjOyvmN7zfknul2cTKc6f8kOieSWUHZX3_3Baawzgk9d6D1l46Xjsvrd6-2FXroe0PY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=OuFbuqsIPxS4VXmv0vQ37o7IWl4XGeyYMNItfXyI2b_M91BHrbF73LcUDhHLk1rkZgddaSo49_eXDmuh1RLtpurkEIsVDy1Ie8Kj51g2ZwSePzqOsZnTx7EngVpuvrB5YDNCnmdpFzjbQjTVSTqjGV3F_uTRbF2VtSetgRmjQOYfnnN0vhFwA5Mc5lDzSQYIi0rO7Y9CwP7784Z8ylDgr1KQrysG-L6K7aJyba-Hh41Dh5KLmw-O22ullUzn8_MhbVejEHaaZf3DoG54tQqf4E_V8Mj69zaNCaOh8hrpBm1jCsmvqR0Fb1OV7MlfWDNYGMCN3stK3wS3sLsy1QX9KgmbO75SMtVhCIgEYWVFiyOUU4CGKU4v_JgZ6jkL9Df2k2ubv9L0Xk-ndKvAHIExcibK0sJWZWfaGR6KXxuPmhmrMXxGWCtP1ZeT1ApJVFLzo_PBzJXTc_9Gs3tb8byhiShXzHQs80jVoii6QMcvT9cInVmD7eFgTv8s4oRjKMIwZcMtFU5TxmH0m_r5PaZvV21hZuBhv92RgLVwkRYRToNFn9yAROWY0Ack238vQ096AKYars_osmHfve4Vw1tEJ-TvDXPopCUSdPQaGedgQjOyvmN7zfknul2cTKc6f8kOieSWUHZX3_3Baawzgk9d6D1l46Xjsvrd6-2FXroe0PY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0Bc2OkIfQ-C3HvLTUE9Oc5lBEcKAfctPJiiPqEBGz-FWpFgEjmCvLRDeCdvEPe6icUK_x5c4V_5V2X0gz-ZcMGcYPA-M0k97H5pvWaJQ2fsr-7yIh4ryafEukdHxP2CjhE-VorjnDMT4Cu5D-nhcgUdPnpLPBeMHtn6SKAj0iVyNVEWmBc_93DJ837bZqhkJkLvu16QzKtzVk0sx_ixi7u56bvKvon59cLBvF5nxB18zEnVJT8f4Jn-r7gXU9VJ1gCt35UG2wrHFSMdJh5l5XQY45aRr6AYYntvMKdr8shXiDmvOdMCxtauuNomkiI4TeZxpyn2qXDnW9zO8LQPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2yhIKaMpSr97KT2HcUCfbDp33IDgV9KOK7SVz1WKowf7sMJvHFhogvCthEpKX8ak5tt8OgO24m71wzCxjYS4oOPtanpVuVk2E3u5rCZwH6wks76EXonP9oevzlLtpUCROQX-y_BiyJUC1QuZt4eUKXthb5GIfucOkmU-LCGdf_jFeBGlttOswoa81WBNkjN_YKo9BFViAITraPX_yY182Gwe0dRVHVX1Z8MO5IE4q1OvkWJ7PJzNnqVHnXcR_oxAaabixyKqEj6zigKGwUq48hCxXwNvyaWwvFp6uSIYHRcge8nFP2IbqHnqaoN1nHT4N8y6ebNJ-8kMIRm3XddkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMWSP6AmVmVsCr2EoJ2H56LG5RmrnAfh0omJNMAx8EUyMPitUKHqimhoGYw2KBYVqnvZ6FBclI3Z9C7eWL4xqBs-OoUqh6AH72MdllU_Q9N-1ZwRmCkxBBrGO8h5he45S6BWVuTeMtog_cQXlQcRoT2FTGju1TC5ALKPTsWh7q6EnB-fiuLhB0hijGLP3rVdGGa1lirMu4D-Nqcd4HV43wnhyVz7hOlf18WgCqJx6vgnXxZ6MUD7FEwlQm7w533oBQsSYhzJiVUKnXXPd5eBf0qRCbyr0DE_jZAPyTFXsZx6pAwGnl9Bs8Dnc70E30xFQUCjNGPjSsvrqoOxiofCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHPfsZjpJlg63Rq4aTQHddQ8lm8s7kmGjGqnJ9ouko4YqFBJw8aIyEIVpCcLWIm8Yq1ErH-ZFliDyaPlg-bTjdLsQ_vgWdbhsLQoVd3Q4lNR0fb24t8WVnayyauzMW2Ep9c-qOS0pNmuQQcEuk9l9X6N1JXGstwWXXK_oTCa3YdfR9fxzTE03s4VtL6_mq2Rnr2dp_wpfqT-aI6CjXBO_0wch79JmCyUyEaC9Qe-ycUItktRtw5m_OTKzwaDhjT7LSzBOAlmiUoKzPmJq4iivQI4HtkyetcRPhStg8he9nqQwPknThWzaKzgWyKdW4vvfwtxGUv7CMeJ3Yf84_UMiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=OYzYO8g0HqJ-kk0i0Tk7laXbTe08o2HhromfYwE8tCR-a-tVTeSfEWN4doeQNY7fUDFCLbb-m4QyYWnz0a4oc7xrw_lU2bbCLCTodvwNcSzOQO_jPyadFJ-WqZie4CKvkI8ORDwqp4_IRciPSnWc4e0b02Z4-oFOXceDxnuGn4p-dgEV3Y0JKl-Yyony9iCjkATcxzmZikMeWrl3vZc8m7pJ91SHMPILaZ19LKy8LKY64dxtGIj2kzUsEa5dwCci0k03XMMykMcDdkJmKRAfafgI8gbeuUDf4qX0JDdJlNv5tnBny_xpPmLXAxx3R51Kvv18JIZ5ug_JhuumfUuUYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=OYzYO8g0HqJ-kk0i0Tk7laXbTe08o2HhromfYwE8tCR-a-tVTeSfEWN4doeQNY7fUDFCLbb-m4QyYWnz0a4oc7xrw_lU2bbCLCTodvwNcSzOQO_jPyadFJ-WqZie4CKvkI8ORDwqp4_IRciPSnWc4e0b02Z4-oFOXceDxnuGn4p-dgEV3Y0JKl-Yyony9iCjkATcxzmZikMeWrl3vZc8m7pJ91SHMPILaZ19LKy8LKY64dxtGIj2kzUsEa5dwCci0k03XMMykMcDdkJmKRAfafgI8gbeuUDf4qX0JDdJlNv5tnBny_xpPmLXAxx3R51Kvv18JIZ5ug_JhuumfUuUYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQRDt2otJvojHDdXumU15acbBw59qQFzv99uq1XwveOjwHTgrIKUuk2aK6jFsAVIwDRxcVH6lztYR3tTMR-JelVEeIvFUFIauoirNxEHZms029cPJW4tkKJ-FhzO3cUAyTMyWxAVUsJpT5ttx-LIapaBFphbVamfWX_Yttg5UsSqBXTYdzj4Q3Dxf9-XepXBLc52ArbOM0a54yZKaHxPXYjX6Z7QReM2A34AzjUX8EDbJpkaFG0dC0CHtrZFZI4WaymF3MriCDQ_l3tS-dMlD5Xr5EMBOclG2DxCpc_g6ljPEo_tWoskEZ7zmbtzRhVTeBVPUWmqIv2DMISzCqM5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7UEigKNzqlPL0QEFgZEmhaRTYvW4jBqfICWmk3dvdoKps4DY_iH2HIGSeIeNcq8S46avwpHeivMpfo8vy3rOe1eBCmwSHhmGJAp9B_81hwhBYAdCyK62gs90xG01Mo0vlg2HzEeYPdMyBJyVOmucalgot7_o1PZf_JlLIrIpHhwQW_xQoF-vIn1bDwvvziw0YSqNT7HhpGeND2LMxU93_7u17agrDvx0-eybmRJwH34vMm6UCpa-ufjQl9tkhbuiy9jNx_VVVV43E1ffvSH-zj_N5wQybQBjJuExq4BRNJAtOTICLHchvOezXHb85NMsgKAw3r4HA7iM4ZYtscSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=Uecwij_ZYYsXZb91WCKgBWbSQPq5-MWqcncEV0nLCJwgMo1kAYY8NAGV7GALzV_davsFI3E4QlwsJZdY63xujJsR1iwCbUXGuaKS1I1Gz06cGfVlduCuTFu8AB260cvsCmnLN1e8HgkdRRrSb9PLZ0jDe2bDkqldTe6s_66zfZ1plHaOUZ2k1AxONNT3AfC_DLQOVEDu1eyzK0YsnkUpZLnUXZpsvdJCMkctN6yJAuKQVwCyPnKPkNX5AE6fqVHpoXfRJTaN6kveDoREhSd9os7qhd4bJH1HNDUx6saG1f99XL2tMl-tIH8AKS7CDxBzGOUEYCrj3GUD78cj89Duuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=Uecwij_ZYYsXZb91WCKgBWbSQPq5-MWqcncEV0nLCJwgMo1kAYY8NAGV7GALzV_davsFI3E4QlwsJZdY63xujJsR1iwCbUXGuaKS1I1Gz06cGfVlduCuTFu8AB260cvsCmnLN1e8HgkdRRrSb9PLZ0jDe2bDkqldTe6s_66zfZ1plHaOUZ2k1AxONNT3AfC_DLQOVEDu1eyzK0YsnkUpZLnUXZpsvdJCMkctN6yJAuKQVwCyPnKPkNX5AE6fqVHpoXfRJTaN6kveDoREhSd9os7qhd4bJH1HNDUx6saG1f99XL2tMl-tIH8AKS7CDxBzGOUEYCrj3GUD78cj89Duuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=Yr5nn3BtH6063FLuesv4QZz66O_SR3ZNP9aMi2uy93xUlm6Kx1aHGxpgdOK5Nk_CRm52wjze1v5Vnal614eRWncmT3tHgF7FxKCL35GAujEwxCe44yjjc0sI60OlcY3cVFDajqgkWjLXdoPJ9ltWqpzt6gOGmgn5pRgnFDi4cL-emsRGk46bWbDG53aUwUb-avHGnpExt4uJWHVPlJAZuC8fHrFD4m2XDJ2xl1xwWhpwev26IbaxyWtfFMjb_PnzPgPodLuGe2y0JX6mg8MDxeHfjdpdpwzOuHPUbTFVmjZkLDCXCenjXARfqf28aGX4bMjSzDJG9X4eR-5Vg52DPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=Yr5nn3BtH6063FLuesv4QZz66O_SR3ZNP9aMi2uy93xUlm6Kx1aHGxpgdOK5Nk_CRm52wjze1v5Vnal614eRWncmT3tHgF7FxKCL35GAujEwxCe44yjjc0sI60OlcY3cVFDajqgkWjLXdoPJ9ltWqpzt6gOGmgn5pRgnFDi4cL-emsRGk46bWbDG53aUwUb-avHGnpExt4uJWHVPlJAZuC8fHrFD4m2XDJ2xl1xwWhpwev26IbaxyWtfFMjb_PnzPgPodLuGe2y0JX6mg8MDxeHfjdpdpwzOuHPUbTFVmjZkLDCXCenjXARfqf28aGX4bMjSzDJG9X4eR-5Vg52DPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=XrbZFT3XXwmup7ldJoQFKwuDZ2JvoQxdOEnNpfNB3UBIoKxA-KHIYGAWkjU5LgtDFJ7rXHH13camFbuH40miKHV5Ie_ny9yUzmYT0Yo3moBG4MUOioIX0Pmzxw1iIew9WkJY6rNJDD1FTtpfhGOgnAlgcR1zjUyexiAPu1abBlJdb18UM98DsGLtaplduU84R9FmDLlQqAUXt9BsZEnJdYZPKnwsUdQWt2QCBjPT-7cMbJI_XdoWwKpgauyEhX0C_p1psG0VY9AOgCFO3fSnJDl_YVozoaMIGoHgoEbYZkgMPygVHumxhSWVHSA6Tx0B6AC3Q-b-yl13Z-vGMTmGzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=XrbZFT3XXwmup7ldJoQFKwuDZ2JvoQxdOEnNpfNB3UBIoKxA-KHIYGAWkjU5LgtDFJ7rXHH13camFbuH40miKHV5Ie_ny9yUzmYT0Yo3moBG4MUOioIX0Pmzxw1iIew9WkJY6rNJDD1FTtpfhGOgnAlgcR1zjUyexiAPu1abBlJdb18UM98DsGLtaplduU84R9FmDLlQqAUXt9BsZEnJdYZPKnwsUdQWt2QCBjPT-7cMbJI_XdoWwKpgauyEhX0C_p1psG0VY9AOgCFO3fSnJDl_YVozoaMIGoHgoEbYZkgMPygVHumxhSWVHSA6Tx0B6AC3Q-b-yl13Z-vGMTmGzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=r5DRGO0enYfDrUYc572Ua0erov2tkhyIy4oIzOHAC_O7FckO0WNSrKW6kA-3TCt3AdI0n_xJnH9fTClwk286glCyIObKGC7OPKmEfIkBIdBuCdZVCxHamL3ABV6jExgMiLTTmLb6VFX0-xpp1LIk8suNpJkp79aF4fwF-Dk9YVlBvHLX5SrXKjZF2UkxhUMRBjwbiEE9-BVpPsMJzA65KVh4oAirLhQp3vNLxtxCCbwvuWtoinRhU5f5vUsZTq3pRxR8Vw1PR-hodQz4g7LLSEJc4Vv6dHrYv3NFYM-aq2AUjaHkHNdeBLjyHHW8vFFnQzEXDOWN6q5WzsVZU5-7vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=r5DRGO0enYfDrUYc572Ua0erov2tkhyIy4oIzOHAC_O7FckO0WNSrKW6kA-3TCt3AdI0n_xJnH9fTClwk286glCyIObKGC7OPKmEfIkBIdBuCdZVCxHamL3ABV6jExgMiLTTmLb6VFX0-xpp1LIk8suNpJkp79aF4fwF-Dk9YVlBvHLX5SrXKjZF2UkxhUMRBjwbiEE9-BVpPsMJzA65KVh4oAirLhQp3vNLxtxCCbwvuWtoinRhU5f5vUsZTq3pRxR8Vw1PR-hodQz4g7LLSEJc4Vv6dHrYv3NFYM-aq2AUjaHkHNdeBLjyHHW8vFFnQzEXDOWN6q5WzsVZU5-7vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=qcrPgN5oCJ_6FmSuvuk14i7UUc0qLCe1uzPBM8s8kotWVSXh2a2_rKSRuLcX-1WqLg98-ZHpfn4NPwA8SylpmoB8EhKknQ4D-tG-SAZ-DWFCFYnvvEDeFmynv_leeslpBeaF36oodxP-0GtmeLaRQoCt6oXmEeS2WdGzRuOdAY0gyh1mHSeQ6m2jgOYfjQjL5jsMuleNSlKFvgruivaX2RyR86TStdmZVa1b-PS4Y2_Uyru2dfc7EPYLFNcc0Lr6EW6OowQ4ATkIgYocaqW6o2l_wGYQBe1nit-fr7-p7zgCqvw_AmTz0tseNacgA7juWq4nWz_nJe30ecIyIbbDNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=qcrPgN5oCJ_6FmSuvuk14i7UUc0qLCe1uzPBM8s8kotWVSXh2a2_rKSRuLcX-1WqLg98-ZHpfn4NPwA8SylpmoB8EhKknQ4D-tG-SAZ-DWFCFYnvvEDeFmynv_leeslpBeaF36oodxP-0GtmeLaRQoCt6oXmEeS2WdGzRuOdAY0gyh1mHSeQ6m2jgOYfjQjL5jsMuleNSlKFvgruivaX2RyR86TStdmZVa1b-PS4Y2_Uyru2dfc7EPYLFNcc0Lr6EW6OowQ4ATkIgYocaqW6o2l_wGYQBe1nit-fr7-p7zgCqvw_AmTz0tseNacgA7juWq4nWz_nJe30ecIyIbbDNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
