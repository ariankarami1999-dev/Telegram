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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 01:57:18</div>
<hr>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5y1a2KLuM15rJ58ws0N-_7TNYsk8hCVtYvu_WTpN4bvuVqVm1exC9lGsq0FVYID1hqr3pT_5kGWC6ZaHulBhKarW2ge-g1sIw8e0Gm3XtL0Hs-jBkCOT_PL2aYoEcHQMb1xdb6p5fJGKI728c4v_pc-dvWYU3fQc7fgMws_4nxP6SzcThO4xL_nymww-yjZoZXpnyGuVwT9sVICG_VmgzEr_Nq4vpRh5BtENJV8cRLnIkhWIc82zj6y2f274w27ovyTNJ8sO67jNjfIQtEr0kGEuH995rTwqI30S5qG92F9CRPF8QGVkLSl3SD-7iHCmXI4RJPxLRBQKyA-8eGyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUOvCvOioHaohVvdQUwqFVFlrf9mDr8052V9KwPk7siJ1p6Yu42xkKfaBWY2u2yr1mXYqnxTTZN8bDEaWtxpA2UmX__c_AnWVHhS68vJRvl-7oIa8YXIm9A98w6o63JsE4dYknj1zAf-KQAjqO7CG7iM7GNxkSCXFerdG6oiNR0Vk04qWUu8J9uz5_St0aE6PRvfmzHiyWxjJlBUMIkxcAVvT2VlxKI3U-2u-BU5nSoBV2rpJc8VgbCQO7K4r78UG0lxlbJDha9JqQz1QjcE3CgXffTXvO7kPX7iJhZGU0HVz7wX2G0i9AWboE2SJINersqSNqEJmHgDBQiyz5g-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWMWlgvAbtND3FeNR56bbRbzSw5qysmjogV-enKZriOe1uyxoWoUcHrdFyZFLyngwDR3yovq5D8er9ch_VU9AIY9-q1ji88-XZYg7M2ClwxbA6i5FhzMf_5x2UyaMFzD2ZEzSGqB67o8TAeRFBG74NkbaLTA5kYScLvK4g7MTkTlEMsjG7qnNZQLXK5xImCDaio1wvB70yovr_cpQc6Cun0onQuJVMgipDkEk38pzZXdHSndg-JePoUSHsKkGay6y6H1J0nDVZbpFB5qZPNAkavtcQz-rTHVPxrVTnlArILoKPawyW9FWgHCUQRLDpAnQWMvsfeYhhFOMjGtZwsQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhVbztuVaHrDiarLc4Vd-K7ti_7k1F73q_83EUNC6AGcRVf1Al3D_Sf8ctRFQrxPwttI4w_r0yJ9q1DyVtxzc1pFf6fcevzkMDpUP_uKReA6jzsDTwXUwsvMUbL2OPwGjPrA7s_Db9MO0cGTKaymyp3meEtHYXQytfFvOX8NvbYHSiB_2fF_LRHt2rCJqMI812knkMGgYt-SGMc0t4lH51rIEVImfxkuG5M1yuY7dXOkhimNmvevE9LbbAGi6YGbdDmv9gb9VdmIBXElqx6lBUT04j9juaf3yBpJISt0O8W4AJc5KUPbHcJcRMoaLBvvjT0ltlS2OzSKkaUZDmGazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnnNTLe-3_Zft_tZDYhNITNsIDju1KGfRCEO_EyxQb0M6jbwMeuICcSiy1eoPBjNquBTajaD7A7lhgHuRfElje7Uy8SXctriJMpiTIOHrRUu9eCfydG7xbPtXmkocrgCTyf003kHddRM3iumBQImdEgVe68Oo1_hKWwz-BcOavlg5481qBHqq3Uk3iFGcGvHeAx_Eg6cvSKJYss6jK9-p0XaaCZk7SPLD79ppKZE0UZ5A9X_giO5ufI5zB3TRjf59rh2WBxwoHl8JfsBCyQkb0DwhU4ulaPk_gj-TssmwbI9LnS389f7PaGoWYPd-RXgkjzNwORvnOg69V-QCw4yOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tx0eGbOvUPPuAVj80ZZDq0TEGp6scsBVBZvjqDK5uK5P4UtpzKHU0zp5cgoFyYnccDBr2sMXCnboV6NnurNjPuZP4J3O9YELemuc70jhVyFEdZiulnt22XfsKm-FvL51Nq6CEklaXEOvbjM51cNmjXtlgunQKU9JzQSAFQWFr0ZWkPUdofYUzfFqsE79yx74UAiU0AUutZ2iPLQOlq12zhhsPAwZTAvWKBKt56I_lRby5_1moQaQfkc4CjROUmvcqYP1pPiz_NQRX0L8q2VloK0dDqjddY6RlNmCuAM78IdsH6_q7kfwWj5EyYQJ9Y2KvzF8tAUlwec5sm-31UncXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7oNV3rCVQ4u0STnILGPCM7c6NmzDhFfdMXoIFQBY3ep9x1psQdDEOwnHDHmmMD0pukBPzGI0SYiCEYu3BCHq_CUDqw2_qwDnPLuzD8aX8IfyVMs7SBU6168xp6bwtf4PQz6jghzzXayTMyCnwgEKrRPzbwBKxQXpt3MmfEp3YPCuGc1PoDaZd8ZvnX7hHqXwLheMUzbuaswtdiidWU8FPD8khD8AUpqwkbcA92ikogf4RjtWn2FQoROZ-zpF-Z5Z6buQqO8PDJXOn9Wu_1wmyHcFpYl3Heu1duGEnc9bBmv7tkcZPf0WQiAfDEsxEIqI52EewjTfvc7wsBYFR0Yew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrNRm1kIEwuZqmenYVIr8_HjJDOkg5RvyCW8kkLwVU960TT2hHLdyelx4Gw8a3MrUSaQtFyVhpUAMvhDQMYcKnIedO-uAQM4RBI7HNgkqxeUuJSNH9joIvO8YaiQ0PMOQBa6xVF3Ov6gZ5AobU-dRLokAm3nA4wdN0J2ho0a20JmOZD-Kq1gaVOI6E7W6E3SW-h-zoO2bGgavNJLdPLhW-vxS5TR3ebuoRALb4wWauZDYWc-TgU-KY1kgMaCMoyuCeYV_cgKmNOPpbFO66Bsh0Yb8hveiVDMAVDnaucFXTQOweR93IHABxa3ijKejClLKOnCy_BGU5HlLQnjf2Q5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFAHgaCBLOtnj_4Mf4EEzIWRYJ_RIDfyYj8LA96j7JfbtvWkT1JsdBO9NywRpixZS5ZbAHjHmD4njphW2mvX0C6u5b2Dnh4lIR7xyEfAa6rkh1xOPObDlflG6po_EF0FSIb_gcV5RLZO0etLbS6ol9AuFqrFgxw5B6sz1rTEW8DRBh3tUdwX2-QsogvL_W_3eQ06s14bAzJEivA5YllCXIaFtkJxjY_FY6siJKzx6JHK6--JnNs2B65pA0-wn1_4lItOiurriEfbV3PA6vPJMKlsLr3lV0bL1c0fd8OIThsWHAMHRdzCM38_R1m1ZClxReSD5Fk3J60-GLFls8shHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onpOWQkQ0XwlHH0k93a4FtttvtJriK_E0bzxTS0g7SxP_ZeKszT9kCtDOSXnnRdD5UUmVClUAlwSjoXf35VA0JQH97PTtEiIbk-gTL3-URpX8kdqddYw3iPjzqYm9GOfFFyUE3bW1LCAPq5SSNstw-bW9_2BHyfQ6HpTIpj57yng2LSI5-fgvE1W24epEfB5-IVOZ_xpDclZEQMqnr8vU2b4OsPL8S5jidGNf2B22MJ-hBRfQVU_EbLx6HDoUo-cZQ2t9N0JlLEszZFUA4tWc6tEMRPvDzTkm6iWIZS6oGMEnuzFfbsI5n7_77lbnIvU_y5zpzDcC1MC3Yyuyd16rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIk7SBkkg9hdb2P8J5t64xU5pLvUo8ZWjUaNOwM1hdnvMKoaI4R9tkGu4wIMCYDGMKq_hLOGnKfY9W3AM9-VClSnpou6veLT8y2T-4Z1IDqqkcxkY1KIaooxneDkTD2PUGfKeL5luRnBYVewxJoAosXaMtJb51puzxJaVU8oC62fX91ES4ML5E5rvNHW3A5OFS6sXXfPspLGD86uWYc2x2Y6gkPz7MmB67ltWSPJ8wxntdROGzEbxtNXlqQlie_FSKMUkkm79cJBc7oUp5vUc18uV448WxTpvFYHbkQ8YixhkrTGo4DScrF2CcxazoIR4w13JgSeCfhSg3bKaw3Yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbeqHRoYFDIkOOY0akZ1BOqNs3G-GChr9bx1bbevs725x3ZIEUc1LIqzoa5HTih4UuHWgWNd_er-MAsGqfbsSnUr31N3PvKL4bHY3jOyV8pGo7ph5P5A5fy4W_MWfsPARa1Wcevivu1DHSgn_5hiLVXTn9hv9ZrTGNAwnu07tnIdo9KremnOGfQAPviVtDM2y0SLhdsYIyNVejjlvFXcSfOD_WNejeVVoT6xAIfDVH8Uq0vJQ2tI0gHa9t9p68uUVVBNdPpJE0nFEIbsPBj1NjU37XY7neHolLEoerR5oMfowm8jLGuigVnUtUSY2jzkJ5WQHFGXrgvqbKMdU8OIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO3x_yOkZ1Nh1aSNC9PNZdGBreW8lSjBsW6FlZA9E6CW8eUqwtuLBYUXHo4YKTarMvWlzvHw6aIT1Y3oVQyAAIHcX8oYfyexB72eh-vDRT41W1uSiXoW6X5KFgtrPecRG0r5rMb2WfhMofPUVENB0KqYtl9_EW1NdH3N4qmFgNHsGRiKD3zBvs78F86zhvJUd5E_CUU56UmQl0cATD-R-MEwiyKJX0m1IWhdgyZIVK4Ny4jr9A3uYvV35anvr6PtA62olYimTxmEd8XMN0IsGGyba_q8aZrswn0I8seYOl7vXsFHhvWEbfIlk4fK3ElPox8ExWOijxs1qwjqa1SMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=mRVxuyh752dw4OboL4aQUqvL9sV91FJfIJSGtBZ6XqSnj2JfvitLrex0DyxZN4wcvL7yMgTNSrT_e-BMD1N_E6LfygEZantXCW7C9jN4FUDrcVZElD8ob6_cbDmkwVBjleNZP4-3aWvjDx4CHqjMULZ_9dJejaRG0BnQsX2Pnkrj2QvPZ4TME7CY7yW_lzEFagP6RUJBlpaa4B2LtjonlIl7k2xJVZAGWZIZaeRwnSq4haJ9l85nkCAI9h8yE1dgLlC7N8TmqZp6yunz4g23VRW-X8OT3_5rcKfnrLkHCHkp-4-HebamLQW2PAAiuuZdeJxUfzuS4c2Q16Qie56mbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=mRVxuyh752dw4OboL4aQUqvL9sV91FJfIJSGtBZ6XqSnj2JfvitLrex0DyxZN4wcvL7yMgTNSrT_e-BMD1N_E6LfygEZantXCW7C9jN4FUDrcVZElD8ob6_cbDmkwVBjleNZP4-3aWvjDx4CHqjMULZ_9dJejaRG0BnQsX2Pnkrj2QvPZ4TME7CY7yW_lzEFagP6RUJBlpaa4B2LtjonlIl7k2xJVZAGWZIZaeRwnSq4haJ9l85nkCAI9h8yE1dgLlC7N8TmqZp6yunz4g23VRW-X8OT3_5rcKfnrLkHCHkp-4-HebamLQW2PAAiuuZdeJxUfzuS4c2Q16Qie56mbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=Sd5Zg_Xa1aeB0Gfn8evK6G-6bS83HpmcmTprYs8kpLJ2_uG4TvhDc1jeaztMVHm_lIWinxVpTXGjAsltNuhQV6NI1WFmJXxHh1QfH3ym5t56x8EY6OHwqgcJpcUkfEALWVYU0rI5m1MUjGhPQFVIkMrUUsR40ytodYRTcpJQxT_ueHEUmXsFWkTUFwI77LDDUGY26dAGGBj-eogxP9G1NMf9iNV54n2IdiW6SG3WURwe99vAU2wlDDQ6lSn94hvlluzk9aJsQPbJz72LuuWj5GHzj_rWT2BDfXRtnw5_4muZAVgJWrnw3md0QHd9-EhpScbEYSUElj0KhI4M7n34fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=Sd5Zg_Xa1aeB0Gfn8evK6G-6bS83HpmcmTprYs8kpLJ2_uG4TvhDc1jeaztMVHm_lIWinxVpTXGjAsltNuhQV6NI1WFmJXxHh1QfH3ym5t56x8EY6OHwqgcJpcUkfEALWVYU0rI5m1MUjGhPQFVIkMrUUsR40ytodYRTcpJQxT_ueHEUmXsFWkTUFwI77LDDUGY26dAGGBj-eogxP9G1NMf9iNV54n2IdiW6SG3WURwe99vAU2wlDDQ6lSn94hvlluzk9aJsQPbJz72LuuWj5GHzj_rWT2BDfXRtnw5_4muZAVgJWrnw3md0QHd9-EhpScbEYSUElj0KhI4M7n34fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH3vydFthf-6Pp-LzwxUnjO-lcoN_mowfyeqnLUU5L3QsAX_QZFt6Cmu99DGrI72cOXsypUeeEMa59a-h6iXbDi3n9uT0mFtTiSq8ZgpnPGwCLtO0Nkj46vaYDKdH3FYf2cOBdcXkl1mLbWDvLHZCVba6PpQpskYPvstEFpFqYIIK_B-ujtINGocuDuBAIksaLd5JYkZQB-TJ_-3QrCBx_LpN9Q8PDIY3KV7__bPQwWxa4fww0_yPSB0K9ks-XjIZW1sNY3LbAPIvqrKis4yIp1F5fEfT4UtXSyRP1l_nKKWaAKnMl_l9SBiWOObqzCj581RGLNSxRr4KYT9cZaEQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=umvyw23eA8LYZGaTlhRFQF0dzXVW8RTipkcM1unTmeyha3svFI2pUcaTh8ySZB1Qkd-F0TBbujcqttsJ2hxdP3QMP-q6CN6aR8ZmRRMSXkx26ySv_iDUj2rOaeLSWNHf60loGJ3BuQnb0W6v7-B6vBr8tmT2UmfUIJfo3m08jqfOWbpBdO7ok0JJC2dkkidS5YhqmvXXuP8MgM6_bxHlVOgnfTXeOi5eg1Qy7PYlSxQ4aYGQ7dpTmS6YMHF2nbDC_qFvyRPiOubKCVc-D4lnbNr0MZpwBzxSOu9Szc6L74jt9VnraGnbnjv0ylDTkL8acTZN-P2JlTlNWsvb-VFH1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=umvyw23eA8LYZGaTlhRFQF0dzXVW8RTipkcM1unTmeyha3svFI2pUcaTh8ySZB1Qkd-F0TBbujcqttsJ2hxdP3QMP-q6CN6aR8ZmRRMSXkx26ySv_iDUj2rOaeLSWNHf60loGJ3BuQnb0W6v7-B6vBr8tmT2UmfUIJfo3m08jqfOWbpBdO7ok0JJC2dkkidS5YhqmvXXuP8MgM6_bxHlVOgnfTXeOi5eg1Qy7PYlSxQ4aYGQ7dpTmS6YMHF2nbDC_qFvyRPiOubKCVc-D4lnbNr0MZpwBzxSOu9Szc6L74jt9VnraGnbnjv0ylDTkL8acTZN-P2JlTlNWsvb-VFH1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKbGacvhWJQdnI1U_iM90nT5QFAMNEc5esumY1tfWu2rcRCX5D37LR5-TWSgwfDs7rp6CP5EuukiSEeEEO05zdNHSQzkv_XdAa_g77SAh7UhjgXaXy_ZD3wH0FX_H6Y0tEv6XcR68kd8B36rkSegYY-XCQzceVvqJuEdEE3DVstRcpmxXdBIV2_RguHczMH1e1Rh-iHK4y_mSPp9A2yJbXDHqMjkKhcdC03gfnwS9UyLUTAXGgwvRtZ9GVEjs_d4Ijonnbo7Af9DyOXcCbmNxNSmulH55ZL9ot6XYnI-3yU5QZqaiz9MM2_3ylYj4Es_S5nmpcS0_PfxbPm4BY_o9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-NTtkv-Up4LkjTEf8KPckOUWDbxnriyLA65RRPt518bla9DVh14li0S9MDzsQER3PcDHiPudoI6M4KoZM2dVGSesa3Z8ETS24l_waza2LiJR2m9jBeENORsPlnQAbCSk2jvygpAbbH8cG0R5m9NYdJ8m4G2jOr6I3Jna1M-s2eGNhXr4Ewz2sl8k3-CWn3gR792ZZk6IjakKo4j_uNu3t4Si0IPQyIDxw1_IsnCoCGrNgbO3Z1BqftXM48FenACPR7_p5QcwBnNno2FCtHncE98frk6EkT2mdOKgV4u-V0Xf_YC7V20_Cr4s7f0GzrpSYQWkn_obU2JpqxbS8PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=Unvs5qTrr9e9PS0MrGIjykjYXTn6RtpbvqZagzeXtQIWD5V1A6EjM9WObe08vgpwSnRujHrctohoJxEEVLf6xlTONY_JuZiNxJ0hWS39wrWUhfX8E5nhBDZXAkEt-Ys_xdHbSNC1ShobdRiig-XPFCTHUmLHYsZ1uPgJBmdM823vHb5box5JOr3T_m41KXAaBIbsqF8-_kZ27u2qTw-KX6BSHybpRuL6cN08VyzxKZPixSivEKvE-SJ9nzbZ3DGzdMK6OwNb-t68d6oSTpOrPDF5Vbpo-4KViXe6Udlci7YlJxWWjdgtL3CUTkoEj_nj3xL7glqalYYhI0y8mtqqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=Unvs5qTrr9e9PS0MrGIjykjYXTn6RtpbvqZagzeXtQIWD5V1A6EjM9WObe08vgpwSnRujHrctohoJxEEVLf6xlTONY_JuZiNxJ0hWS39wrWUhfX8E5nhBDZXAkEt-Ys_xdHbSNC1ShobdRiig-XPFCTHUmLHYsZ1uPgJBmdM823vHb5box5JOr3T_m41KXAaBIbsqF8-_kZ27u2qTw-KX6BSHybpRuL6cN08VyzxKZPixSivEKvE-SJ9nzbZ3DGzdMK6OwNb-t68d6oSTpOrPDF5Vbpo-4KViXe6Udlci7YlJxWWjdgtL3CUTkoEj_nj3xL7glqalYYhI0y8mtqqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r-wZgsjjrCNOTWAizRxmEkM2AX_I_tQjXZonLHWJz80_G3FWzsikb4zPIbKVaBak3L5qH6osfAR1C-ONSBaC-TgArMb36b9G7ELyWGc07N9AEptCmoUwtzm5CM4bmo4q1FrcwI_1-BTkrVifsrJxuZsSiDoGb_Yqa2k5P8xYhmumwwEGMAW3Mto8xyc2Dg3JAWQ-59JCWoc7lwQmqp2_8hUDQGwVfduh7bb3eDfcH7nJ7pnF9jO679lmkdxqyxkXUnhUAVL2PV1IsJE9_6x4NYUQDDeTZ_FwmMDQe1kT_r6cfZUoZt2oGy00nE9to8xo_POOSOQZEt5Iwwq4eDHmxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Us5a8rY8fs_OssRdVpSJitCOVxak2QTASwj0zpWvVFCLLRj23YMXObgoduXRcOb5uRNk_cAaYsedXI1qhdCwggfzLWqq0aIINi9RzDQJhruVvhP0qyeBYap2CyutyjF8FAmuQhXTSyWMkloLmSEFOJE4SLvPfWSQv1yE1Rp766hLH7GzP-hB2elQRhavM9rUjz1NGW8bnCTJC_9Z-2accHTrSJ5oBr_nsW2kbPPKY-QFZFlvbcCzYtQjJ7XnIor8QMcnn5i1xzEfNiSt22xMM2cvqUNAB8dztBT6QFIrdV34LCYHr8iS2NB0ZkTJlq4I13SU9Td7aIK__OVYFBBeyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=bQ8pqNaHI1g3o96D1ZkLpEFNV3JDwc9Bvl9tU1io1zhtiJB5skQCuAMHjE0bajouYllU8o5eGRr8rIz_AWDMpgI3n4rTnskB2R_3hIg7ZVCpSyiT-62ov6g-euanmqFjJmUccdVTGSc_Ll1zknKq69qYOjeAMPZbQQNTRq5xTeSeaejGIT56jyf4dVw18Qzh2Cw1_Wny_-zMGJF-rNXwBqg9eL9rk9TdsM6JbSolfoPMCe08Y5GdfemhIYow1-LT4oS1OFoCjJS7tfUE79I4lqjbroAwxFRJWGXHrXSThFzgMDF34e8jmOlAuZGAK2MUjbfF2pNfHr6D1DAcQcpmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=bQ8pqNaHI1g3o96D1ZkLpEFNV3JDwc9Bvl9tU1io1zhtiJB5skQCuAMHjE0bajouYllU8o5eGRr8rIz_AWDMpgI3n4rTnskB2R_3hIg7ZVCpSyiT-62ov6g-euanmqFjJmUccdVTGSc_Ll1zknKq69qYOjeAMPZbQQNTRq5xTeSeaejGIT56jyf4dVw18Qzh2Cw1_Wny_-zMGJF-rNXwBqg9eL9rk9TdsM6JbSolfoPMCe08Y5GdfemhIYow1-LT4oS1OFoCjJS7tfUE79I4lqjbroAwxFRJWGXHrXSThFzgMDF34e8jmOlAuZGAK2MUjbfF2pNfHr6D1DAcQcpmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIRqQQfgHUs1_zkht0PD2cs0SrbqTZMJVrnaEIcyE2yxExO2KXX9xwwQuc7o_Q29h4UPQFgpwpRq5K211KuS9PYi35DrO6rVV-BrnLbgBU9Z6VDMY2G5aP3206TrG5XKfQQWzM0rjL6XmOXNGnzWP7ArWx9kSypa05Fm5n9vJ03Ays3hQ5ZGgas73Kq22XN6nyj9x3SfB5I3onJwe9RsHblm9EYYD-z1eyGokXIi0Rigv6JljfkV1mH86Aqg305qdzNEEyHFvT3z0AsaKOq9UCmsSynS__LMOxbUDIS_Ceki7Gz6a6kDSufO-BjzA0i6l8HszXQQ7GCjo_DVRiGB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD5pjNHdXsTQJ6kRyk8K0Ns8kizNQPcSBXi9kI1ZO4gkP-FbPkjY3-mKUpxk8Jx2UK94IxeeTwnhfx39nJCJFN348QwWBbgidmQJeUYTF8qEgokfLu_gV6h_ginAau7bcsKkl0M-glF9DNubAcJ2xE-VA0te0S6RwmIoLxhhMuNQn-8YcDsaaIngoW_ZTZngK3H2yqmp-5ZM5fLSbDOHxD_-YGqhT3QMO0D9AQbtvMumrStRSiAi6kRYv6dy2M60k8WZ03H_SP8YI6sXDB9KjU0T0TD-o0qtUsVWPKKdX8eJqeMapyBmafsIiI925In01Eds_8LZsY1Xmrbw80psLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=aWITLJNSe_Ag83Oy-sg8MmHQaXY-LXsHGU0IbsY7rkpIhudoHQlmJStEj3YuWzuUeJAXu8vHNc79fjgnJ0TPqKpAOumgQ-cYNEJicNaigxaHyCX0bEi-Hi3NRLi6eJMTKt08d-gYfxlX-dWGyxbRnd0rRiMDJ8KiFcRil_mhS7-FtoUHOgY5hwB1TommyTSdzpqDGuWVOlJTnVThfK1y3GlCbN42W9Qax5lsxpBBJyNUpioG_a2VxQpwmrGNy1n3G3kNr8Jo1tBLX0uESaN2AXGitXmEXkVHBDwuBihVnBczZBh5EOt8jUjO6hPTtZ7sqBlVQWkepZvjOaS5t4pSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=aWITLJNSe_Ag83Oy-sg8MmHQaXY-LXsHGU0IbsY7rkpIhudoHQlmJStEj3YuWzuUeJAXu8vHNc79fjgnJ0TPqKpAOumgQ-cYNEJicNaigxaHyCX0bEi-Hi3NRLi6eJMTKt08d-gYfxlX-dWGyxbRnd0rRiMDJ8KiFcRil_mhS7-FtoUHOgY5hwB1TommyTSdzpqDGuWVOlJTnVThfK1y3GlCbN42W9Qax5lsxpBBJyNUpioG_a2VxQpwmrGNy1n3G3kNr8Jo1tBLX0uESaN2AXGitXmEXkVHBDwuBihVnBczZBh5EOt8jUjO6hPTtZ7sqBlVQWkepZvjOaS5t4pSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVY-m7L0vOwZHxbkclFGyva6rBMJvNb6tJIOeMm_qzlvZri3slgxiUQIC4Rs7LaNpfom6Ao00tfhGkwFE62N_jVdE4SbEIMpvCda0BGzT7rST4yXjgC6usYR5EWjFhO1v5J1LGPlDwhnyun8m2mfN5A_Uv-Tmwbj7F1qIX6h34o2M1g09wrKiH6gCkSj2KFHaTj44e2o3eb9K9vT7D2puAGm9mfZs1Tqjl8p4HEpSOpoJsTCczQybqogFgSpkia2p2EZAiKtXN8-wMD0E2sX4GtbnS4DNbppG9EhQS704t8qyrQSn6lJymh126z6dVa4kOmucXdDXofGLPzVYe_D4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=cUJR0qadZtZAHrDnM14AQcah1YKOHazS3X0Zi5crs_FiofB7UzR7uGcNRaz4I6w3qEfDBhSv44qEPZg4SmJYcfMnirerFYpwJv5EB2kY3XcCREKrDWaWGPJO1Fyn6fzAbCgaZjKKxU87WPKorc7uv9zlV3HOAHYMEUB5POgtNGckNWL5xvqKz7aW2H19qXe3C_RX-uONwpnw0xxHKEsDqkXdxVMnsqt7CW_i-OtJaOwHSHqbRiKdUXlvqziAADN61xw9g8sm8cvLrBwWhxOk2DpKohfeuYF24Y6J4_OzVkM-p60EqtFRzW6__8UIMAH70G4lavKonMqMCXeLxPQitA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=cUJR0qadZtZAHrDnM14AQcah1YKOHazS3X0Zi5crs_FiofB7UzR7uGcNRaz4I6w3qEfDBhSv44qEPZg4SmJYcfMnirerFYpwJv5EB2kY3XcCREKrDWaWGPJO1Fyn6fzAbCgaZjKKxU87WPKorc7uv9zlV3HOAHYMEUB5POgtNGckNWL5xvqKz7aW2H19qXe3C_RX-uONwpnw0xxHKEsDqkXdxVMnsqt7CW_i-OtJaOwHSHqbRiKdUXlvqziAADN61xw9g8sm8cvLrBwWhxOk2DpKohfeuYF24Y6J4_OzVkM-p60EqtFRzW6__8UIMAH70G4lavKonMqMCXeLxPQitA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPuSlFEvPKAf6UnEcTXiXBk40-lzEv7iUcNQ9n_wIS3PVbYnP34p3LhHjckNuIMmH-Bkzf8CLAGBWNzGVrrlGzIwB5lM74yIpEHTevr8H5cAHjEXLd9YmhrafRXOOGLsm6mnKNIC_BAQFX54CPRFdf4kb9e1Ywod11DtAVB1Za1Jw9Za3fuWWHX-0vyGndLNLkTB8KULUs_OQ7tmvyeYut0uf0D5tqbbeCYYsh4-cNDnntdqkshsxvDiPzE6DlkjFSE1wbqr_kaaraUwpAiaTgVMr7Vac6ELMQIV080o4-NAfq7-oIpStC4iDZXLr32YvPVmrNvoIot2jIffwg0-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJA-5wUYFhQ0ErrHe1NevRq7vQZdJweh7cLtIpI4AyKoEXPohUvWR5Qhs2jCfo4lwQB4BUr64E1c1sCrnFiOWDcN0h6v1YA0oCLrdYKmqwkdf0Qt2_IA_UrHBgxmQ0nt5bWsj0BVAm8PTEe8NwKM3m10i7jdf0qDmG7ss5DoJuZAyxHDXEQuRKVnQ5lYwfhoopiUQpG1NeXmctggJqfkgtL3_GyzpGfjj1WQuJ_42LKnRT8Tb6D5F-sv3g8TfIkxPyEMuO8xTBnmeKqZeapZYmGnxLl_F1gI6voNaeJMW92CSb-yKWS7nhVKTqEy9l3fVJqmZ75U2GlHZ2xkxR1ERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgNyi1jhODrp1EHzBQKN5O61C4g_n-1kYwXhwk37K2dhAXuZqlMTdiClOqcdMng0J6jV_2aj1SZG7s3vKOnStxF-DmP0CCiQdO1vyi8bj2TD8w4_PLTkzgUxNapN8kad_5_pjuYEvilm1rTBUKTAUc4S0Uo8a3vE_f5fRKaMw7fBvVHkmukU47hufPToWjBf4oupR2H_6pkPdK3kOWEpX6zmoU5rGJBRu_IlzH2J2dunaY7MomSPWZXCQvOLGcJEIBB7QSxQYSs-4xw91eG4w2Yu5jIF1yFvpvSqxEojS-53QNJftdtsBmd7YQfyGLVSU_ysQK8K0jZw9I2fZxFGlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6dojmXDqzhYxb8AR5Gt-vPG8MTsKvFV55j14snHTzQv9BXZvRDD7Eu4eqaeZ-nhs5hIjRrJJO4wynKy94qXOU-uRNBLjuNV8AccBktYZqKyAId-tyEfIqqoRNELP8FS-OwW5Hc8Bg6JySvDiIsbfDqfg6zOCHSDHtpiyq_DlOlel0qnNlP1KCz3DdndczQlyJ0jczXxaOxNn4WZCgRF4Rdt-t-DJgAi1FWN-DlTFY7esDSMoghxXaN5wIW3hskx6OI25FRfR-plVie-xj1Ie5cQxHSIXRknTd4fN0Hfm19eI31egefD1oyibl_PxxHgREGKafAtLNCwAvNoT6ApyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=eYC2YSWYuDId94AhqNnhWR_CyYW1zPjn-9suz9aZid7mapR6LG9016Rc7HecVZqsZI0YXof3_xJpFgnl3encbC_BSrapSMjEtifVlIbyavCwtbxV-CV7_prDpR8am19JL0xQTfA5NlpvCPMY8CsYBzyTjJDbUJBLO3026lvbhedbFk9k087Sm1RyaCZPRlWQ8tgGT804HngmN8bh5vuiXe9IPo6XaSHRDh0NS1zyYukn_Qr_KmLR6rX86z8hJREtVgU0-b72IFdN9QRalnv2nij_ozjHhS709WM818J1lSoGH-3RXz1A_ssEM5alalRT4E2UEpuJehsNSYjbJESvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=eYC2YSWYuDId94AhqNnhWR_CyYW1zPjn-9suz9aZid7mapR6LG9016Rc7HecVZqsZI0YXof3_xJpFgnl3encbC_BSrapSMjEtifVlIbyavCwtbxV-CV7_prDpR8am19JL0xQTfA5NlpvCPMY8CsYBzyTjJDbUJBLO3026lvbhedbFk9k087Sm1RyaCZPRlWQ8tgGT804HngmN8bh5vuiXe9IPo6XaSHRDh0NS1zyYukn_Qr_KmLR6rX86z8hJREtVgU0-b72IFdN9QRalnv2nij_ozjHhS709WM818J1lSoGH-3RXz1A_ssEM5alalRT4E2UEpuJehsNSYjbJESvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=VbqAaDJC03sgHLa2EsE4vWTMbIjJjSkmoVKt1iIrppY8s3EWe1Dd2U1ipIlwnS9IYSMa0L9nP5G7UIPW7PqsSegny2rZrS_OQEfhT2ANyege09LU2_-DfQhuQaZxr3avNpzYf0nuDfdbVAmnedlvGAMY2x3miJMNrZRv2OerVzx6mrIDSfw5eCAWGhlrNiYq0Uc0xjI0H8C25HfI5BXq6RHvwPTQiN81KRFugcU8NLIoJ5Wbu9tzAAK8zNPUYqv1IykPjbtPCKGyMuY3K5_9S2Efi8268BYKHpIKmAZqgpCOIv_RiVPECTXZXhAASBbTx3DYtYnSYKtDFIPGrFEn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=VbqAaDJC03sgHLa2EsE4vWTMbIjJjSkmoVKt1iIrppY8s3EWe1Dd2U1ipIlwnS9IYSMa0L9nP5G7UIPW7PqsSegny2rZrS_OQEfhT2ANyege09LU2_-DfQhuQaZxr3avNpzYf0nuDfdbVAmnedlvGAMY2x3miJMNrZRv2OerVzx6mrIDSfw5eCAWGhlrNiYq0Uc0xjI0H8C25HfI5BXq6RHvwPTQiN81KRFugcU8NLIoJ5Wbu9tzAAK8zNPUYqv1IykPjbtPCKGyMuY3K5_9S2Efi8268BYKHpIKmAZqgpCOIv_RiVPECTXZXhAASBbTx3DYtYnSYKtDFIPGrFEn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9RTDx0ld22Gq2qH8zXUlCk_l3cYTYSrvj0XH3NJ5_6j4rrEjUGJ9E3E4xLODxPgULdBhUhldTvk66pNp0GuCXMxgUjlK82TEzaC-DPuorAyOLErzlGGh9_NYE88LMhPWSkq_g0s-i3Davf7xQNMDII3ys9Mx2liNv2qC3x5OVHGo7EcemdCpA3em7xNxH3vFC2EMXKfiE1hnQA0kuDZhGuEwZB5A3HbApPdm-J9Qkp5JAAi19ZDKX64XNsTtm8ZlCzaI8rQok6yV0yMgw2WqvSdsj31Xv6IVXtofjFoTX4hE7mNZFR4VFeBUy8WnRJU4hqSId2mV0v3zEQ9rwWLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=pQDLSg9RR7MB5ZoHJeuAWWwazThhzGYnqDTiUp782k-nyLOMPK5ikWJhCMACn__mhwz47YCb_IU2cE_8_PaSvbgiuv7r5FkOnKVx0J1-0USs9_Ich6TN6_pf1bFyxO2k49k2N1RISpiJtYZGM63MzqasD2_LgJDIvVxnRCXgxr_URAfsM2k87J2frzboKu60PKT72v46j9cqwTrfmHOy7vUp30PV0UBNO34L3XllyfbLi2_1de8-sMLWDLe-gUwS9YjDYQ350UKkJ-0529XFHB7swv2mcHabIG12E48lrbhfr9c7wWE-AueSJ0HH_06LJ1GseCbCSuplqcRYua4VqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=pQDLSg9RR7MB5ZoHJeuAWWwazThhzGYnqDTiUp782k-nyLOMPK5ikWJhCMACn__mhwz47YCb_IU2cE_8_PaSvbgiuv7r5FkOnKVx0J1-0USs9_Ich6TN6_pf1bFyxO2k49k2N1RISpiJtYZGM63MzqasD2_LgJDIvVxnRCXgxr_URAfsM2k87J2frzboKu60PKT72v46j9cqwTrfmHOy7vUp30PV0UBNO34L3XllyfbLi2_1de8-sMLWDLe-gUwS9YjDYQ350UKkJ-0529XFHB7swv2mcHabIG12E48lrbhfr9c7wWE-AueSJ0HH_06LJ1GseCbCSuplqcRYua4VqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=AJHmqf-5_9LePrNiTMCS5MlATR3_EbmNwYUXBMfxq7QAw9O7UGlwU4dQhFmtEdMT8PJmhqF0r8Jj3QxdPuibfl9CAUJ6MgHmiUpttaRxxthUAYpNYUIR1E1sjTzSnD0ZLywgIC0UfP5wvifHq20IIqbACTabQ2xSTgYwjItWqISucK-tj-DBHFKz9aB14XmNsb6Rf0zQVZvUhjtM5mm6UNp9ezs7UtasgPPrx9vuq2uA1NmuYQCXOjtKkCzo73Ri4OpCGlEoXdQa3P0BZ-k6xT4rTNKycNYJ1Hsd23Wr4A8RUCM0qpB6LSE0Qb_gk_dQBzKTglay5ZurZ0KwZM-qrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=AJHmqf-5_9LePrNiTMCS5MlATR3_EbmNwYUXBMfxq7QAw9O7UGlwU4dQhFmtEdMT8PJmhqF0r8Jj3QxdPuibfl9CAUJ6MgHmiUpttaRxxthUAYpNYUIR1E1sjTzSnD0ZLywgIC0UfP5wvifHq20IIqbACTabQ2xSTgYwjItWqISucK-tj-DBHFKz9aB14XmNsb6Rf0zQVZvUhjtM5mm6UNp9ezs7UtasgPPrx9vuq2uA1NmuYQCXOjtKkCzo73Ri4OpCGlEoXdQa3P0BZ-k6xT4rTNKycNYJ1Hsd23Wr4A8RUCM0qpB6LSE0Qb_gk_dQBzKTglay5ZurZ0KwZM-qrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=YeSGtLHUUsFEvGOyFgjZTR0PtK_iWJUcahLPXXRGueX3cxZNW65vzOnQgTUn-us2KlLbTS_sm2MGf50BESgQbOibPDLDO-EAPoihTqp_gdxBB9zuKP3O8Njb7o2zkcCxtonRzJMcAZifwZQ3eAa-E10e59k1JlxwJTywio6Fqea11jjN7G-9tkoZkAd5mNHAzCzkJJYbalPmC9TnBMyXTgakuVlPPdJWzu-9ucB_AIGMqYE8pKJ7KGX4d71SH-ei1quzI_07aFOoaufe6q94jU3K3Em5SV6R3vay9wB75auUF764gFuxMvyjMBweMwXNqFAJa_qEkZ9F0nzy1-JV1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=YeSGtLHUUsFEvGOyFgjZTR0PtK_iWJUcahLPXXRGueX3cxZNW65vzOnQgTUn-us2KlLbTS_sm2MGf50BESgQbOibPDLDO-EAPoihTqp_gdxBB9zuKP3O8Njb7o2zkcCxtonRzJMcAZifwZQ3eAa-E10e59k1JlxwJTywio6Fqea11jjN7G-9tkoZkAd5mNHAzCzkJJYbalPmC9TnBMyXTgakuVlPPdJWzu-9ucB_AIGMqYE8pKJ7KGX4d71SH-ei1quzI_07aFOoaufe6q94jU3K3Em5SV6R3vay9wB75auUF764gFuxMvyjMBweMwXNqFAJa_qEkZ9F0nzy1-JV1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anp2dlggEi9B5EtPKSxS6EN3SHstEbVuf-eeKava49HBXLepmfhYt9FYVIXidyFQi-i8j0tp18vHw9T5zTlUvONq1zzw8DopFa5e5EZW__kY2v5BUjmBLu1mPSxKf6Q-RFJLqtEGqQ725Ny-MFpkaLtYoezO0iFEw_mg-zul8sU6k3zkWkONBuwKhj1h09148Bd4rg36r6QkqP81fvpo7x5DdrxlPzmc9N1J3b7KZsNTojYm79xu4IZXEJWBJOl-Y77yKMLInfWf1_oyEoaLDpqi2f-Er9Mw1-azb7IYKsNW687tAJZosHKGqeC-lu8rvmipLuXtxnFRtM7TJ3SM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Usm5rLPTWM1Cc6MjXEyHMfZcpXPu5WxRSOy-Y3-a5jadTdaxgYGl6D8roQcImx2zaLS015tHSkRG3EsVqcNvoJgnR69bv3TzrCm7yI6MO6R8PO4BhwKEEVrYFkmjDk6qbZIGklN_negr1vsRan3lrLFzUlkfDIyTlj2oDgWE_LrdqcqwDmjuZKlIZR2JVkfxTVWNuRnl_XIpwrSof-vt1TAGt7-hAR2GZlNU7LL9Nwmjm8GhX1p-lo4uRzSqdtgEKqj69fKkh9tMXhoJmGgNlhrUJdnhqawh4kg629hIeSRLTTp432Dr4Rk6qZ3NVS42lOvofO9vmLDaqniCPC8bGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=mSi0XXHWZtmW-74_QO6f-Ozz4N6u0S2faBS5Xm_tdXh9p1kxVY4v-L1X1iH2Zq7kGerZnYiEzaReQbUSaBgPmnN32e1DMWRNZ0mepivSvbItJ3R8ECmJxPUSn5Kz-6GD7PpgC8omMjWz81fgVQLyo6yq1UvXPmZseXw2xfz6e_D6Jk25kcOKBJwqwhBi-K8MVVfeqidvtZCnbAlLTIVK-szb-3OGr7efLfeyvpVL_43qQOpB77aOULuL6oIk-QLvK4GFmC3MiMCxQZNVPnJWxOqE7RE-DOjwRLCELw_HerBN0DEVSnM09rHRwbIefMm7I-TD9Lnc1gDAiPJh08JCmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=mSi0XXHWZtmW-74_QO6f-Ozz4N6u0S2faBS5Xm_tdXh9p1kxVY4v-L1X1iH2Zq7kGerZnYiEzaReQbUSaBgPmnN32e1DMWRNZ0mepivSvbItJ3R8ECmJxPUSn5Kz-6GD7PpgC8omMjWz81fgVQLyo6yq1UvXPmZseXw2xfz6e_D6Jk25kcOKBJwqwhBi-K8MVVfeqidvtZCnbAlLTIVK-szb-3OGr7efLfeyvpVL_43qQOpB77aOULuL6oIk-QLvK4GFmC3MiMCxQZNVPnJWxOqE7RE-DOjwRLCELw_HerBN0DEVSnM09rHRwbIefMm7I-TD9Lnc1gDAiPJh08JCmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=sMAeWdBgLlJ9ooNDxL7kjigIwMj9LcKf9oD20-mIvstGpBEPC7wim7W6ZAtW46eUd1nZehRL_Urb9CEKoWi1AOc2qVF_rFS75n0bt-XvUQpIMI-1blM9FxxCE6AWrxT6ec9YEJ8Mo52yBEN44jsSNGafvHHeRougm9CQcMndWEKYEqpExEcW7p93p4IzXf71eYx2s5hw_7QrNlMKxSLl9lrCZE7oMRP9bfZk-VoVElhotBlqdV8hieEHVqo8yBQwG7fFPkLnV91ZkRULxoqLkAZyYv9GaAHnI65BgFOAqcxB7cS1WpMWQygNsKnhe3qprOIO7CGCKwwOiOfxCHu4jDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=sMAeWdBgLlJ9ooNDxL7kjigIwMj9LcKf9oD20-mIvstGpBEPC7wim7W6ZAtW46eUd1nZehRL_Urb9CEKoWi1AOc2qVF_rFS75n0bt-XvUQpIMI-1blM9FxxCE6AWrxT6ec9YEJ8Mo52yBEN44jsSNGafvHHeRougm9CQcMndWEKYEqpExEcW7p93p4IzXf71eYx2s5hw_7QrNlMKxSLl9lrCZE7oMRP9bfZk-VoVElhotBlqdV8hieEHVqo8yBQwG7fFPkLnV91ZkRULxoqLkAZyYv9GaAHnI65BgFOAqcxB7cS1WpMWQygNsKnhe3qprOIO7CGCKwwOiOfxCHu4jDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=OL4fTNf_bgrSNqh8pvPmUYtJWFYPQaa0YFYairuUzLMwhKZdHp_YduumW2zP6Xp7ZHSkVbNGNxdD_q-Gwa2MRtCl_CQ4jOc_rYPRd8jaDeDDSQFa9jPak-aSscwbDeUJWUPZCoJOCL06bOE_SWtqxSSPxGRR4Bv-nBQgL8e2Cwc5F3Cd0rfjq1eW9GQZ0pIng-Mro8PxY-086K5cPyRC-8KjrdJ5L7f4SZ6dz2cP4EeO4YUxC3zZa_fcmspSkoa3xOBnMPrFlJXJQDCnph1CDuX5z4pz-3k0eYHBKsq5S2e9i_5OivPUI2oCxqtRU9-P7c-iywHnrH5lsDMMuRv3lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=OL4fTNf_bgrSNqh8pvPmUYtJWFYPQaa0YFYairuUzLMwhKZdHp_YduumW2zP6Xp7ZHSkVbNGNxdD_q-Gwa2MRtCl_CQ4jOc_rYPRd8jaDeDDSQFa9jPak-aSscwbDeUJWUPZCoJOCL06bOE_SWtqxSSPxGRR4Bv-nBQgL8e2Cwc5F3Cd0rfjq1eW9GQZ0pIng-Mro8PxY-086K5cPyRC-8KjrdJ5L7f4SZ6dz2cP4EeO4YUxC3zZa_fcmspSkoa3xOBnMPrFlJXJQDCnph1CDuX5z4pz-3k0eYHBKsq5S2e9i_5OivPUI2oCxqtRU9-P7c-iywHnrH5lsDMMuRv3lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=VzKjjjoEBaFrE2cVv_12CE0WJA901T6Rj5gFM2ZB5Apr1dLHIBER161Y-CsVlAOOyGg2qy27QdGYy5L8iWFbx0NyO_i-cpwEZWLBMhbHXxO7gYOyS3a0n1NW5KpkaaI0b2jVAtfy0q0tjc12_zfM8dxIV0vPqTZVuYQTAfcUdqL6g8mIlguArNSGpjSQ9ogXrES-OoJAjWqzvzcAWiBibHMLQ6w_ulSNEUvnwaQDHAD0z7cqcWY41_KbqUEJijSl7C-EEXN20KLLrsWSkEc2TbrcetoZpRzaJTFf6fnwP5xW11guGRkXaRJV_z3N5zJH-Ee24XYlMuLwj2nJSvQCjV_boWG_ONExnW97TkmGdMdcUA4iIRUHWWXKO_M6a6AdAFAjHKgMqxc0tvzyvECjaWaWKGNjcx_-H-H0WdQWRZRKb-WN4m-yvD7qYqWhnPtBD8xfeWeRhk7Cs1CQy9PNmpEQbHGQ_B0YbKEDg1NG_gE8WtKMAUggL-v7g_U21t7oJYlwewnvsFuZXZR8Iz9sgN9_whVU9l8U__GMVx3KQWBx7qwsH_6mjh9AbUAi4aMW1vtwFbB-isb0ap9NNIaK-hcMmKnRJs_IN1xwDySNQ5KL4Zk7S2tuoeauh6_MLsu5wOhHnTkPgvnqsumnUNakzFUOIzJvxhMkcnwEFEh9qTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=VzKjjjoEBaFrE2cVv_12CE0WJA901T6Rj5gFM2ZB5Apr1dLHIBER161Y-CsVlAOOyGg2qy27QdGYy5L8iWFbx0NyO_i-cpwEZWLBMhbHXxO7gYOyS3a0n1NW5KpkaaI0b2jVAtfy0q0tjc12_zfM8dxIV0vPqTZVuYQTAfcUdqL6g8mIlguArNSGpjSQ9ogXrES-OoJAjWqzvzcAWiBibHMLQ6w_ulSNEUvnwaQDHAD0z7cqcWY41_KbqUEJijSl7C-EEXN20KLLrsWSkEc2TbrcetoZpRzaJTFf6fnwP5xW11guGRkXaRJV_z3N5zJH-Ee24XYlMuLwj2nJSvQCjV_boWG_ONExnW97TkmGdMdcUA4iIRUHWWXKO_M6a6AdAFAjHKgMqxc0tvzyvECjaWaWKGNjcx_-H-H0WdQWRZRKb-WN4m-yvD7qYqWhnPtBD8xfeWeRhk7Cs1CQy9PNmpEQbHGQ_B0YbKEDg1NG_gE8WtKMAUggL-v7g_U21t7oJYlwewnvsFuZXZR8Iz9sgN9_whVU9l8U__GMVx3KQWBx7qwsH_6mjh9AbUAi4aMW1vtwFbB-isb0ap9NNIaK-hcMmKnRJs_IN1xwDySNQ5KL4Zk7S2tuoeauh6_MLsu5wOhHnTkPgvnqsumnUNakzFUOIzJvxhMkcnwEFEh9qTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCSeCaol8IifRqxlKkKVd7nagft-laMNEYIVLfKgI5taLNXR7r43Hsu_ewx7545RGDL_eg-WFZDDkjXbX04YBK6T-B815_RAH17hHwm2FHij6QJxBoNwPSEw3S166SzaXSMsxx4wVMIRj52RyoQvu-LHESkhxA2EtTaGzO3dClrROKL3JNPbo9yY5p-EoXDZH4vJC4GZV_sIf-LK2YILjALqpGWHws2Bed0x3SDLVlIUSc5yt3w6n6ghq60sZC1EH1acL5IMmmiVJOJTRo9ZOq0nJyp7db_EpKg-nsdKCxBOGIcge5-prpo3_RsqDVhaZ08gZXxpVRdBxlxeVq30zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=W0eBbelTSaYkVZbPAzCLtbcHJo81LgCMAFHcCuDnrRF1U5iR3lwNUmjvOmPUt9MOkmMOTzGARi-M5TCX58dA4DmcjPqO-tqfNsQPYYrTQA6vX4s3iviC1PhgAXNSio78o8ngyI7pg2fSAlfndbrUl0tg0vK2q40LdcQqc2MxZVQX5Pr3xsqhmyM9q2g78Nzhja1UmXfktqh8CWMLs5cJLlmeBSch6hzBFqwB08dqb_TjmPytsMI16TQENGaMMz8xbS9es8tN7ci97PnCXggfeWskGeOSQhtEDnlgQfhkGoICGialqkQtVXfw87cnbvRY2eEZgZ8wcnwnPBc4CUr6yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=W0eBbelTSaYkVZbPAzCLtbcHJo81LgCMAFHcCuDnrRF1U5iR3lwNUmjvOmPUt9MOkmMOTzGARi-M5TCX58dA4DmcjPqO-tqfNsQPYYrTQA6vX4s3iviC1PhgAXNSio78o8ngyI7pg2fSAlfndbrUl0tg0vK2q40LdcQqc2MxZVQX5Pr3xsqhmyM9q2g78Nzhja1UmXfktqh8CWMLs5cJLlmeBSch6hzBFqwB08dqb_TjmPytsMI16TQENGaMMz8xbS9es8tN7ci97PnCXggfeWskGeOSQhtEDnlgQfhkGoICGialqkQtVXfw87cnbvRY2eEZgZ8wcnwnPBc4CUr6yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcBFYkJqss2PRaorDZtAO228J2sKgpol6qPgUyMakkE-xkwNVn4H1LmAryjHZ1ceuCpcNCy4o1tL0VsxT-LSEbCNxIP5Oz94pcRTtUzg13NqOvaxWMVRKxsmDCXS1EAOt6xAEW0E-oBbVoClSIJegb8ERUfRHpXgk2B3lwlti96pgaPRjhUXzzDDqN_YKC21KDDtdUeE_qZ8SmoWOf5qWS0hs9D3hOWNeUwNE9dq-XvjYraQltRSm6kuwSo7fW4xy_hNE7iCUY63h_VrbSsvh0oIOFAK-yZr9VqqrX5cFhqsbk2deIReY-dnYoc6FkRUImqJPKxu0rgOu0CZYj1DlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGKAF7n96J_N1Kyg-OL9n-6L2mT9vS3ZbQTpi6p-8FD2HzyfSqU1oWYp8jXP9i2vXgb7D-a-QmH_3w5AmZZmzn7Qo-n_mEPOOQ_NxZVwSCgpkIfWBtg7ONTDJGAvnNlUPysOUas-w4z6vGdv2N5DtUcgRrkobMCk9H9wbtm2iWlSbI4gYEQEezQDjEMHeHxzYdgwXJqi_vhofDPf7xOa9dCcQb3JGgEVmugRhNBHYnJYDdc5FCyM6yysGzNfnLFleu_VJmfYbazHJlNPZHMdJqDxGWgglYpaRwzayliXVrzEhqA8Pb_DsE3O4yQr6yEy2RGnsMlyp9ehs8t0FXyl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDT7aJYh6Ho_VAJf_NtA3ItzaZhyKM9RFa1oWBeNbKNvHa3e_8HaWKr2wq-ooce4nvl8MYtDh89lqUtcEhSAeXqXmGAU5Kg1Qr7gMxdWjup5-LGfQCa3yZtBhYj7efkIr8CDvO-7jVItfpC4d1-c1V2FuZY3I0F6ob2uf2twocDvtia7xTt5ffMtbNC2yZeoHvYFQck5HjEJDAcErvCglHRFHLGDB0rSS5L_nsf2Zpimbb2KmH0nsalKMQ_UW-nJmJOVOfx8cTenSiGff254wEtSPe7eYqUmPdHAMqrI3RI2Jncs6aaMzHAO00147k0ca85Lp_dxuuExrD18Ymwmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aT27M5Y2EK_8C4WYxQPy0Tr-nRHfz37oEFJhMfhj9VM4_Vqk3Ey8-pvJIc8w2_mlkYkdUHSVAbOVgs3f6gv9gYUr0Ue_K162tbPTdsV7391V62WIuiRcijZuy5UQmtABrFsD-E0LPpHbsYgVSL-QfAnI_7lqBO2ZbKNJxnP6ftGJjohuezPmqy-nX5QTOplC3JFW8cPA_vGFH2M8ofNxLLE8661Ge5V9XWez_VmcwLHmUVrPf1Jy7bmg0Te-_xz5bre9kJcaIbM4viXj2BCZklWisfJujLXoxoDz_rPVZFqta088VvlGPCVVDWj22s_854jfCdr1-szQBxtYm3nF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPxoJWlGOoqvKPudeXR0Kqf1YlHaWUjc48sC15MMUUNhsLuhBvBEhtzBjGotWV6FolJRwECaYy12ZhgbZYs5uiKjwr7X64EuvLtprQW0V1HBQRUx1UA7lN-a_ooSCTTbH5SViQDsF-scL61lYs_CO7jjWsA0PF2G0hHDB59_uD9ttU3TxeV1RCvFbgsmXf6v1l-eCLU9pzeRvWLHR2XuMFcENj3jtgiCK3xSeMRL40-wLUe3wC5O-keVbCD2RI4P9tKB6qRwsWrf2dFJfbT0KW1srzJK2Kcn-hRBkL0Q2HsVUTgnCMkWswq5i8HZJyfgm6tgllO-fj3L-aenHN6BYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=ZvJE8zkwe1Y3phsB6hL5wP-pS9Ek4TQQJvvLWfROaB5LBv2MazCS5Lt0ZCYJ6W52cXJxQELLrpCq3xmi13q2HNeUfrGoWGVBQ2OqMvyUPU3z4yKlfufzpnOOzmVI0jDTi57IS4afUx9kw5mVOGPURO1m0zlUEM3PSsLtkZI7PLcCIwlBOxHdFe01HN8q4q9YhDo5FchAOtbK77VnFmN8r6FKV0uNHidV_8tZbpf9VITVNbRZFSa5AUstAmu_gammJHIx_RJNfxsZY6no-oN0kXDpn_8XLs9g7j73OTbrWkORG8G2uchFaod0R4yN3nCdd73p6v5G84nuSQu1ajQAZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=ZvJE8zkwe1Y3phsB6hL5wP-pS9Ek4TQQJvvLWfROaB5LBv2MazCS5Lt0ZCYJ6W52cXJxQELLrpCq3xmi13q2HNeUfrGoWGVBQ2OqMvyUPU3z4yKlfufzpnOOzmVI0jDTi57IS4afUx9kw5mVOGPURO1m0zlUEM3PSsLtkZI7PLcCIwlBOxHdFe01HN8q4q9YhDo5FchAOtbK77VnFmN8r6FKV0uNHidV_8tZbpf9VITVNbRZFSa5AUstAmu_gammJHIx_RJNfxsZY6no-oN0kXDpn_8XLs9g7j73OTbrWkORG8G2uchFaod0R4yN3nCdd73p6v5G84nuSQu1ajQAZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=WsBg54dNRNCWYkKzETEdGaXJVkJX-4-7yXN3gutldIk2tLVaBw35YWyVEz461Yzp2PyOTg_KYiXGLZCeGFcLIZpcrYEEPHBlItEEPsEGru3-_fPf3pIdu0LcDIPP4aXDAHoKxqsbj7WqmUyTBdHVe9PD_S8hI11X5FVWQcGasAosqe-DqXL4vfyNWlkCzaw3_IVQ9qPa4ZtCBsooinuBEgq9sf0boA1l4273oflf9PJvapDBhZoR0-9TOeXA5g1gJ0APLBfRfAuxe58rVOay5hwyN7lTgYAit43knlrNY2sLyMOBgialUmN5jO9kitWlu2LppDcBEeS3bSDtejB-qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=WsBg54dNRNCWYkKzETEdGaXJVkJX-4-7yXN3gutldIk2tLVaBw35YWyVEz461Yzp2PyOTg_KYiXGLZCeGFcLIZpcrYEEPHBlItEEPsEGru3-_fPf3pIdu0LcDIPP4aXDAHoKxqsbj7WqmUyTBdHVe9PD_S8hI11X5FVWQcGasAosqe-DqXL4vfyNWlkCzaw3_IVQ9qPa4ZtCBsooinuBEgq9sf0boA1l4273oflf9PJvapDBhZoR0-9TOeXA5g1gJ0APLBfRfAuxe58rVOay5hwyN7lTgYAit43knlrNY2sLyMOBgialUmN5jO9kitWlu2LppDcBEeS3bSDtejB-qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=VMoiVeg0c1Uo4wFnNmPLkK_DtSZN58caicPIV8IJCjQhuJOvGGT7efinokrjyRH6EG2Lg9jKTTX8eIyIgTakWFK6onrvjdk1KhO2CdHvAVAcbWMSI7YXAiL4wl1XJ65AhgxfGJTZhCgOa6w1CQVKj17K0pKBM6q2MK2dTvu843J3xdB93B-pohEnQUw_sLcRme0XpgTmNnoN82LNzMf34GMPadRJP6g9G4ajQpqtxh2vU1NCWS5LjlPT9Xa_l3qP6GS53nYmfIIEkzUG2qkMSR8p5_iNcmobTI1HwzFWrIc9e5lQwDNuoY0oqScxddbUqgnaSLIR8Illq9sIEwDOWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=VMoiVeg0c1Uo4wFnNmPLkK_DtSZN58caicPIV8IJCjQhuJOvGGT7efinokrjyRH6EG2Lg9jKTTX8eIyIgTakWFK6onrvjdk1KhO2CdHvAVAcbWMSI7YXAiL4wl1XJ65AhgxfGJTZhCgOa6w1CQVKj17K0pKBM6q2MK2dTvu843J3xdB93B-pohEnQUw_sLcRme0XpgTmNnoN82LNzMf34GMPadRJP6g9G4ajQpqtxh2vU1NCWS5LjlPT9Xa_l3qP6GS53nYmfIIEkzUG2qkMSR8p5_iNcmobTI1HwzFWrIc9e5lQwDNuoY0oqScxddbUqgnaSLIR8Illq9sIEwDOWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=Y5pPqVTPQVpwmQAMeK7gEJgq45SMyICyPnLVzdoCUtsYVirsFGuDNXun8WGaknep3V9RdLWN4hZH3VwY_TB4ofEql5jIMfQkLFgLW59_7HcNm9fvWOMm4UiEKXJAYPSMWcAqbcXOeB_4fCoOVAe7n-ASK2ih36L4bLLT7iKrhsR8KTHFzfD-LQEUo21rw-NMsckNSZNZjNqOsRsygIFufTrZ7d-qroRvZ_MWRyshQrkijQstrmoXCExtnwgt5g4_9qE1Sh2ln4drUZEo-Edsy3pstJ8Q5FL-Xrt3SZtu5ywhDmFx8WrbIrmaSxL8753sAuMEdkW8FweE59_0zshHIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=Y5pPqVTPQVpwmQAMeK7gEJgq45SMyICyPnLVzdoCUtsYVirsFGuDNXun8WGaknep3V9RdLWN4hZH3VwY_TB4ofEql5jIMfQkLFgLW59_7HcNm9fvWOMm4UiEKXJAYPSMWcAqbcXOeB_4fCoOVAe7n-ASK2ih36L4bLLT7iKrhsR8KTHFzfD-LQEUo21rw-NMsckNSZNZjNqOsRsygIFufTrZ7d-qroRvZ_MWRyshQrkijQstrmoXCExtnwgt5g4_9qE1Sh2ln4drUZEo-Edsy3pstJ8Q5FL-Xrt3SZtu5ywhDmFx8WrbIrmaSxL8753sAuMEdkW8FweE59_0zshHIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=EY9MXjCYK7S5DOLKl4Ku61k-vRdcnBHoDpYOCxo_QXFQrwEx9W_wWXYD7RBDCdG0jq2glOqXX0ZJWRk4EFUWcFKjAUT0WYl8GMMznJ9UVWb4iE5J2hHNEq3VcxTxudmEI0ISyAMmwLd9M4YE1NCLjvimNp2aY-C63UykpycrO_7X0ATo94bk_Fm5Qt0DFqEEjgcsfWlEPzlp-mywhq0h0q1fqWNVl3LXMKlrasJvSwwZaS4uf-JeXY8NDhgY8zs97p2EVaoxNmDxUR51kedRVwxAPW4y16yjwlnGuvRu7MflABtt4R3wlUKccikD1NAq26UT6Wz0ln4mysJmDTp9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=EY9MXjCYK7S5DOLKl4Ku61k-vRdcnBHoDpYOCxo_QXFQrwEx9W_wWXYD7RBDCdG0jq2glOqXX0ZJWRk4EFUWcFKjAUT0WYl8GMMznJ9UVWb4iE5J2hHNEq3VcxTxudmEI0ISyAMmwLd9M4YE1NCLjvimNp2aY-C63UykpycrO_7X0ATo94bk_Fm5Qt0DFqEEjgcsfWlEPzlp-mywhq0h0q1fqWNVl3LXMKlrasJvSwwZaS4uf-JeXY8NDhgY8zs97p2EVaoxNmDxUR51kedRVwxAPW4y16yjwlnGuvRu7MflABtt4R3wlUKccikD1NAq26UT6Wz0ln4mysJmDTp9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc8DM0w5R6etZOqoNz4yAwepHOk-_l5iyng2eyqCR7YTh08mvUm3NzBxsNiiK5GAy-mS6cXji8kOB3EYYEMiphdsMxmAlebxxrBxVQyxTNu7RaN8xfepVgK3xbv9n0TIRGTF7EBGK0MQARE_ffEw_7pxSRvhZjLIJdJ1b5eMZB0jOLeL4bu_jC1ih22Ob-PUvbTFeinfeK5Mw8ymURa0_qxrnrzkjWG7K9BNXs5OqOTKMKrp-5RFj7rJQDPPlIk9ezd8BmGvkRdT8ZsutxqARuXyEGUF72oQA0euln0MXlsuzloVUCw8kQQTdbaAWSgdcBHDsD0n_oV0JEn_gRGXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esN6MHA4f7REhgm5nDSImND3o0pJQW10z8V965uNT0rauu8BmfjCsXOgOA96HlXdhSuWpynL6jg2s-5wxEYshvEcTKF2xIps3Wq_hpXB67JKsWTyrGoJdrLD23aPWPf9hniwk_p3fG5cVAHvzFsN56f_tdGRwEx0VZyRQjs9qTGWizCPy_u_-qejjLpx5M7a1yvqth-RzvjoMDwUe1K56X950t8E_XOWGllNqjOtWl0Bd8icwCRRDbJQ-mbk5ugX-g-9ntlybe4hCpSVrlYMqqaF4KMC8O95meqBH7M9YArz9snujpdDx-Mzyszjf5sUy2MfN_kifMjsRRBf-TL_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3hIbyJXNWjC60V6Omfpv_x9RmXE5D_thcHg0dx465mEP9C144j44s0tWK1MqcRZ6Q5-uINLFb9kn1CdQcmcmkVW_Gzo2dkjfcJ5WeXCQ4z_e76MDMrRVv0aA2_R4VcYTv4NGiWC9mp-cLBDY886fYrVLl2tMNcMIEVZXmPLxNv4RoXth83fReRwY8IpCc3_sJ8OYkDH9YgZe2aMTY06wFfhHhdPKlr0anybpIvwpQHNSqd9-6zMYmu3We-_wHqIiuyMViwRjftBg4OcTwlN5oqfXEddUP8l2gdkIPlH0OYatEWFG0Gpi6CLkTgxfEKvIs28y6jgIZH8LStgo7sqGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKN614qAEwthEUQ-xAoK37EBmNNHqezYP_Mclj3N-z8V9kmF6EeP4zSDMlWLXnO21HCwdKoWvJGExmzcRkuNCfHLvCashaSwzpU5SNSEWdSfE7gIyViK2OfuGDGeLjpcF0tJU6_haarudpMC-mGnzAYBwQ7PGKNakdnWzYKp3EzCAhaeppNl0H9ka9pczUrryCRSTw-UrP_LPBtj8m54Z_4bK37ADjCp7NcwsClthi9rBxZ7hyih4nKRux0lNimVaECD3KBDnTPn6Z0F1SdCQM9TPsYblDDpCCtiq1g-SLTKIdV7KiokqxUDhrODYRMmIvNrsNls3AIIgU7inG_Yvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HucXOHmOyAvNctJQj3-yWfeT6xKcEafqJ1MbLXR2y_8Su2mdQl3yCPhqqIKegFpn2VFqwUpAejQPcHGlfSanl7vA0MrE30ChgROIY2N1igQju3ZJCh3J-XwI_xbkgwTTYt_e2fqX-6_prU3L4bEzwS2yy3qK_19IrElGPnAHej0vsYF0h-uUZJEvN9EArBSMp8qr_cNXkcbH2eaqRwA6UUBLbmTumKA4seeWxXbQFZiXaG6vhSXLDZNKin7eJSOghAA4Xc-DXY4XJyBmjpwBcFanwvq_bv0hV27ABHnQeuzCvbOD7TDqUs7Th5zNWkUBX4mlJXwzAL27J2EXlrUsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=Aunx2GZSDJTGQSX9HsIPLYUizHqBWnuqv5WXIgEDSdZqgMIkTpzksH8B2ToKJPVs4KWmCT5eaQj5ySq8ABTLbWA2bDQZNTfBdmNhhqtuBn-W-gziVaMhBmreRgXz2vzfzWwO36znDwsjoJLDVn0-BEsbbF6bOJGlJaYhiuj1d6g8nGED812EnEmshZcA-239X--Uks9UpRXA1Ca68Hg61ZA7_cd9it-i30FKXmFdiCM3uVG8ttlashywWbCK2_FKJOND8sZbBdTOvPK5VhkCL1COaLS_h_8zIALAn0mGkeU0VKDBcTUWHxciyxs8qWLvbuiKtemRu7DtcN1YyM2Bxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=Aunx2GZSDJTGQSX9HsIPLYUizHqBWnuqv5WXIgEDSdZqgMIkTpzksH8B2ToKJPVs4KWmCT5eaQj5ySq8ABTLbWA2bDQZNTfBdmNhhqtuBn-W-gziVaMhBmreRgXz2vzfzWwO36znDwsjoJLDVn0-BEsbbF6bOJGlJaYhiuj1d6g8nGED812EnEmshZcA-239X--Uks9UpRXA1Ca68Hg61ZA7_cd9it-i30FKXmFdiCM3uVG8ttlashywWbCK2_FKJOND8sZbBdTOvPK5VhkCL1COaLS_h_8zIALAn0mGkeU0VKDBcTUWHxciyxs8qWLvbuiKtemRu7DtcN1YyM2Bxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLWdFRJ9DmMZTuD06ODHpYzUvtDF-qh7_ffmw1psqFQeks1MMRTC7TUvqT3MrxqYICE1PfW49muOgR2olzWdRpK_rEdikbvHV2eZimVyW9GAMvhBqv5xN9STWiUhx6uRL74jeW7pGHNC6ieoh6AUuSU_6GTwT7h_JBDkVgMkHr3CJ5nk-oVUb-9hqO7mPiNKasFDfVNRUvlmx7j69UD062E_f5HTk2WhM5IkiCkN9PLsIcmk0mptUUlG3E2wJZoAt260KVHmoKAoI4KNKGlQuTUoPbGtg3-uixAL5c1fJGr_UGCC265UFBj7STO8fyZIV3exE2zzpb7ZlEE-vOHgnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGJF58bnydbBB6GSHBlGWGvAIAUcJNEI3scgGMNyiM48OcdK3lYHOeUVfncqaauaixId0NhNnHoXALoVCqAibUctrRhJyXrFW9wxm9P_n7A5ID8OBDlj6CKGWr4SaleQHeH74S5WAxeMhIYVNuWfd5NtYPDq5nRqGSYFHxf3yxceLrehviZyGYOZ6orLZnIpTdUqMP0cdKPkhgF9R6dK5f7bWMRGA3o2Udf7egbMntrzAxp0pbs2ERA7Gs7YBu496uJZh8nkasAZMeEaZZQTcYudFNIN42ngYojOUYiGhXd23krZ0kXkom8jToTXhpkWC1z1BIwOIQ8r5nmplxdLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DM5t7bGbfX4P_BCLTx2pmHlqvJmy9Ey691H47FaO59Q7qNT_vT135SvYIECa3QiwU10kCpWFHcwiLug2Jg45GoWf9ERJVQJlQ2A_uMOlQKEvs9e_ExJQFXuch5FdBgg0pULR1I7U7aMAzrunmvQbWAkh0WMKzY5mRJw1XgocJGIL-bKdPNSpeJUe9URuFh-1zv0KSBRhcPfa-IGz9HrZrdGQGCfl1VmXhRLYLhQ3iqtYTQWYlIEY07uJXmpg3A9XD4byBAxOztS2kQT8QPPi-OzG_3SUSt2JmxtMBbK06KvxImuBOYpi6arwkfPxPSR8I-GLnQF9uTyFzSsCjzZOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gb3PW0zRAC4kSZhSYRpwb4934aunhvrIHs1aaOi2c3eNuKxk6CHkHiNJ4NyQ4vs4ijKTuttS7TJENSZibxQvA992ICqsX-FWnQbQGpq7J6V47Dg6hKltkhhSkzuroqxoJ9ObTyjlk6dBZGBUzD9o5R4BbRrorEASsQ-9MqumuFwK12ad5QOdtKzLmUBr0NXmkHzPAY16kjNI0n7IP_R39CyZIUKNSATY0n0YGz9ns3CeWImkiQvDM4QPMoUA7yKAlGe9KN_s_1NJ8o9hD7VIgnPP0IKFIDNLEHc-rwO95p-pGUeF9yUmJSDx11KLXNemdFkljdtRFRaR8U57TFq2sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=mq3DnS__kQndAW0I685YvTVDjG1_NTkHnDZ8VfR8DoyrElcc6vX098MHD1Gvj0Yd_yxQ_MLAjRijTbVxRqBQOPIrRXG1qqwg3BFvnVRpxi5s_O_SYbzJz5PfL0hnCN3IenZG0JVvKZBxnhyn-nSS8V1PTcXP9-LqWZarNepDheCp6Ck17-WQVbh0BWhY0125QMP65YQQwcNnJc2yQIcxNHaGsIQ3ugQIrQJPe2v-Cll9djXEzwLGE0c8kVUZOhfG_3BHAbagolcr9bxXuiIa6nkLxfWdV_obBEuHs2ldn0R2s_ONohTWwih1iMoXFCO7j5g6CDQ1IDgxLt3N_HdKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=mq3DnS__kQndAW0I685YvTVDjG1_NTkHnDZ8VfR8DoyrElcc6vX098MHD1Gvj0Yd_yxQ_MLAjRijTbVxRqBQOPIrRXG1qqwg3BFvnVRpxi5s_O_SYbzJz5PfL0hnCN3IenZG0JVvKZBxnhyn-nSS8V1PTcXP9-LqWZarNepDheCp6Ck17-WQVbh0BWhY0125QMP65YQQwcNnJc2yQIcxNHaGsIQ3ugQIrQJPe2v-Cll9djXEzwLGE0c8kVUZOhfG_3BHAbagolcr9bxXuiIa6nkLxfWdV_obBEuHs2ldn0R2s_ONohTWwih1iMoXFCO7j5g6CDQ1IDgxLt3N_HdKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFcwMOr0hcLxGE2T8QFSJ89xafTjxIFUt3Pge3-R6rBRpHEy_EKHR6O0QokJu5NfAdZOxhEP2q8P4JivNHxSB3IJ5uM_EiZRbz86_WE4pFd5dWVSIbmKPCzx2X4zwKXOIL69ulAHQDOiBxWlzo-bx4JfiBJmegESIWRzhaP56XD0eDSUC5MQDYsM7u2GasXavrD16MOCY3FOoLjx89TuBYfKF-Rqv8xSlu6utb6hJRxbzqsKAQ6zBi-tkQaC9rXXxPBmSWUwEoAMdg32w5EtDCnJ4jqVFAlJvimJQoYgE1JEQWg6eC3LkfiaGUSL2IkJn-Q_ZfRo7Fue5rQXbyEtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=NyH5_EhGhP7slFv3bzzxc6uPc_OsXVoWQH74HtnFJtyVEvXBq_GS7JNgiRWIFF7jWN-LZN11hV1392Ki-ySHL7YPZxLzjHXoo0ErwQ_Q8FbB1Zt4_EVEiaUrIiPXxsF00kRlEGn3D3x6QbiFgilwmEcg4aoepgcyinvebcLO5R9IPFZkTNp1Ejbs2wCH-Q7HIZ64lKzgaQmq3vRtUf6-cGkv3G59EIs7pcCY933OBtJ869o2cofYyxx-F7JHjiJQ7UvI73KE2rmXdyKeoEhzP5MAs4PUhJ-GyIEc4Wp5CJtgMcKXmJPDpK2sMbfc_HdEpck01fANcsm5ckk-tKu4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=NyH5_EhGhP7slFv3bzzxc6uPc_OsXVoWQH74HtnFJtyVEvXBq_GS7JNgiRWIFF7jWN-LZN11hV1392Ki-ySHL7YPZxLzjHXoo0ErwQ_Q8FbB1Zt4_EVEiaUrIiPXxsF00kRlEGn3D3x6QbiFgilwmEcg4aoepgcyinvebcLO5R9IPFZkTNp1Ejbs2wCH-Q7HIZ64lKzgaQmq3vRtUf6-cGkv3G59EIs7pcCY933OBtJ869o2cofYyxx-F7JHjiJQ7UvI73KE2rmXdyKeoEhzP5MAs4PUhJ-GyIEc4Wp5CJtgMcKXmJPDpK2sMbfc_HdEpck01fANcsm5ckk-tKu4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=qfZYEqPQo17DCc_sIS9B3CgWGaJXDYex_fAhTBaFI8XqrGjW6POupW9Brrtq5EUaRn_Mgcpf7dqf_P4YW9oyA-xy0RaIbQzLcPQRiEDeniJDSCuJXOpiJ3WaezdQ6g25ps6qGwFUczOduiBGmz45Vet4FEmg3tD1rQNBsOylnuPGr45i8AHKA4cwnEq_yL76FKej63qkKR3-4-sgiH5puEmbftWrQ19LhgINeZZrRrwKoU5QCnRe_huMc3Fp_tiK7S2IOQKmT-qVvfTvhCfr-TjuK_TfHf6qzQQ1ANEDBcIUjGGC8wYydE2yY_eQ5_sLT3i6700LmEs239y6u5-ill0MyCBK2ZQ-ghM8QWPcP-JQH6q71DEP00LkB2WfXCetCUD1sQTdedSwGQpD1oq5mxbr-yYCTP6oZTg0JlEfqZTuJRSCL24bd9zps7D45S724fEQ1QORZ_wicCqAwsdg4J5O-ktuirFQLrCgwsYDL8sBfPk95y6y1RIk2lciYLUcoI2HDnUXj1ezQ-d1-GEAhEOoN9qnW28v106A05vOTmcJC4ePS2Iqqas8ZRZgSNhYGDupy-WF2Avcs-E8JJCHSe6_w9aTmB5T_bd59v2Af_xro_a6-AKzsbQ7OBPfcH0NptqjLw1miZn0AhK45QNVRv5s_Nh6xJ-EU63Q5wVWGZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=qfZYEqPQo17DCc_sIS9B3CgWGaJXDYex_fAhTBaFI8XqrGjW6POupW9Brrtq5EUaRn_Mgcpf7dqf_P4YW9oyA-xy0RaIbQzLcPQRiEDeniJDSCuJXOpiJ3WaezdQ6g25ps6qGwFUczOduiBGmz45Vet4FEmg3tD1rQNBsOylnuPGr45i8AHKA4cwnEq_yL76FKej63qkKR3-4-sgiH5puEmbftWrQ19LhgINeZZrRrwKoU5QCnRe_huMc3Fp_tiK7S2IOQKmT-qVvfTvhCfr-TjuK_TfHf6qzQQ1ANEDBcIUjGGC8wYydE2yY_eQ5_sLT3i6700LmEs239y6u5-ill0MyCBK2ZQ-ghM8QWPcP-JQH6q71DEP00LkB2WfXCetCUD1sQTdedSwGQpD1oq5mxbr-yYCTP6oZTg0JlEfqZTuJRSCL24bd9zps7D45S724fEQ1QORZ_wicCqAwsdg4J5O-ktuirFQLrCgwsYDL8sBfPk95y6y1RIk2lciYLUcoI2HDnUXj1ezQ-d1-GEAhEOoN9qnW28v106A05vOTmcJC4ePS2Iqqas8ZRZgSNhYGDupy-WF2Avcs-E8JJCHSe6_w9aTmB5T_bd59v2Af_xro_a6-AKzsbQ7OBPfcH0NptqjLw1miZn0AhK45QNVRv5s_Nh6xJ-EU63Q5wVWGZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0Bc2OkIfQ-C3HvLTUE9Oc5lBEcKAfctPJiiPqEBGz-FWpFgEjmCvLRDeCdvEPe6icUK_x5c4V_5V2X0gz-ZcMGcYPA-M0k97H5pvWaJQ2fsr-7yIh4ryafEukdHxP2CjhE-VorjnDMT4Cu5D-nhcgUdPnpLPBeMHtn6SKAj0iVyNVEWmBc_93DJ837bZqhkJkLvu16QzKtzVk0sx_ixi7u56bvKvon59cLBvF5nxB18zEnVJT8f4Jn-r7gXU9VJ1gCt35UG2wrHFSMdJh5l5XQY45aRr6AYYntvMKdr8shXiDmvOdMCxtauuNomkiI4TeZxpyn2qXDnW9zO8LQPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5yfHtpedHms_pDSs4rY432ItscaKSlYrnb5wAJ-GaX7fnsAtbc93qka9kgZR-ZtEUXLQFl7g5DaLsBlgDL7yfAxVHl0WD-UHQdhts76bi98X0NSqVYEUtEjvtYuhCkpr5a5-Jbb_1GM161LXmNM_a_Od1yHXBTi2Qr3YRDA0lfS6b85lqpLTSJkWYcuVgWB3x_Gm8fu_u-P6yEFQLCdtH9sHOzq5ZsFFGUVTdkwZNuhkJmL3Up7OJXu0AzcytcY_-arYC5cBivOr0RwYbC7SVmyl_b_si3P3dHHGxUiq8anWZrvzNRNie-eXNLewVllgIigApHV4p0ZLhz5UiU8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMWSP6AmVmVsCr2EoJ2H56LG5RmrnAfh0omJNMAx8EUyMPitUKHqimhoGYw2KBYVqnvZ6FBclI3Z9C7eWL4xqBs-OoUqh6AH72MdllU_Q9N-1ZwRmCkxBBrGO8h5he45S6BWVuTeMtog_cQXlQcRoT2FTGju1TC5ALKPTsWh7q6EnB-fiuLhB0hijGLP3rVdGGa1lirMu4D-Nqcd4HV43wnhyVz7hOlf18WgCqJx6vgnXxZ6MUD7FEwlQm7w533oBQsSYhzJiVUKnXXPd5eBf0qRCbyr0DE_jZAPyTFXsZx6pAwGnl9Bs8Dnc70E30xFQUCjNGPjSsvrqoOxiofCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8qqMeMvrTFOoFqRR6wnx2MGEhwZWrPTEBLtIROOmBbqtMsfdKkDSxaf2JFwfLQahfvMGhTjKYkI2WBG46q7VJS8VHN0EydqH_jf9xEOUmmDW6WNnhn4VLNh8MgDqTIqruGY1L9763htTnWHEwHqe53mELA7TAMEMPb3RkVnzmiBoLVABP3rxU7KDFTRrHKjQXeVxR-YDvw01oj0Bw21IrkC3QsddecFj26rzuyD54a8nw7RFYoPHGZJ-BXQ1kciaoboZJCCmmwTdMQXiSph9cwroa-lICy-suIbStXAZU-g7Qp7eIi2X7vDmURkX8m6RP7iXlvyV0Rb3NfpgXt0EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=ckrFSzh6JQ9Csyx1BAfO6lONWEteyjrgmu7N9zKZ7QPqpaY84Dbewc6h5gnZ2O0Xf3d5CyFC2x-p-7tl1AscGOhPNFwkDKs7tyikTgwxOwSJdrNZzBKz27fl_kSDwEkKkILnuqlkN1lAO-EYeDH025BW4W7BFYEDYM7CnkPSwQvcVBE7SNfuPFBh97NptEjMNCOFwDIbRdINew6myrY96HcBLuIe0kohDYsxBT88VYTtygZXhgAvlacz64dhqUCG4uZOvsqh6q8MCX11QjnwQi0GA7Ky0yiItqVz2Llec8pjpi5Miy71SU9ldhSMCiW6h3AXMzR8PoiKpYDaouoJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=ckrFSzh6JQ9Csyx1BAfO6lONWEteyjrgmu7N9zKZ7QPqpaY84Dbewc6h5gnZ2O0Xf3d5CyFC2x-p-7tl1AscGOhPNFwkDKs7tyikTgwxOwSJdrNZzBKz27fl_kSDwEkKkILnuqlkN1lAO-EYeDH025BW4W7BFYEDYM7CnkPSwQvcVBE7SNfuPFBh97NptEjMNCOFwDIbRdINew6myrY96HcBLuIe0kohDYsxBT88VYTtygZXhgAvlacz64dhqUCG4uZOvsqh6q8MCX11QjnwQi0GA7Ky0yiItqVz2Llec8pjpi5Miy71SU9ldhSMCiW6h3AXMzR8PoiKpYDaouoJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2XWjmv_yso-5_DXaE2_4mo2fJiuSxik5iHo_3q4Lo8NxzCgmxQaP5ZVFNE3eereduqtaRYhL23nuY66-41WcRzPLoYUg6hYVfWu7fLMhcZDCf_2o-Iqrt0lBdVknR-HETbS7UPWFQMYSRpiITazsgzQIPN9scsntIevPaSc9PtIWiy-vZk0m6YykFqzGUH8YzbGF1F0apNR14k3drBE8Kcic9FwgZUuY8sdEfwacZaThTLfkQ5_exrslp_-aNBTLhl7bicvoH_OGM4Ku3wmSG7Bcb8LXP1koA-06ZlQiYpAd-qHhKzLj_0NWyBR-760J-R8ozaYWmDmPsGIRWRvlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=p8FIr8zVO5cEmlGwSZYt_76CpXFZRgBn4qIPsTdeiC6VC3CLT4ZSecwBppkBNgQV5FYInYBfTG-uriuT_Dg18xFh8k7sRXL6Mkb8t0hc_W0MYpfJsZAeyQFkJ4rEe6nfl6ww7eP73soUSB9lkUBYwlHArvhY3EK8zPIhTwb6aaml0nBq4kCFdOZnk6fzyPOhfw_1ecG7uP7jIMZmh_sZxDRqUgVavIVwatvwehw_EWRjTUjfPMhFhzy7vJkaEngDsNWsZ6-n4F32LT-5e0_X1Mi-l2W3CZoc_wp77wzkuf45bU61-7O2HGToiMj34D3pOsTHk3oel2PcvvYCSrlwnoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=p8FIr8zVO5cEmlGwSZYt_76CpXFZRgBn4qIPsTdeiC6VC3CLT4ZSecwBppkBNgQV5FYInYBfTG-uriuT_Dg18xFh8k7sRXL6Mkb8t0hc_W0MYpfJsZAeyQFkJ4rEe6nfl6ww7eP73soUSB9lkUBYwlHArvhY3EK8zPIhTwb6aaml0nBq4kCFdOZnk6fzyPOhfw_1ecG7uP7jIMZmh_sZxDRqUgVavIVwatvwehw_EWRjTUjfPMhFhzy7vJkaEngDsNWsZ6-n4F32LT-5e0_X1Mi-l2W3CZoc_wp77wzkuf45bU61-7O2HGToiMj34D3pOsTHk3oel2PcvvYCSrlwnoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=JR2yKtQNIkAl57oAVXYgEo_cOZsqiTphi7GpS2POKXRO8B6eO78sBgkRyobl9Z79vC0Rbw0sOaRU-JTs5ii3ncSA3KbSoTepXBauGUnK-gywlj4upPG0JUPFSWfbbMi0mqVdl7dF4kEP2giLUNdSi_6wxuO2ggsrJNoAtTcmi8VeXDW2euzDDrS2iaIxznTd7DJayPYJDUi7grsHV3VKOfULjbpB_CgdYdbmzr3-yRGS_j6I56EMQDva3DD5kpXjOlPnm8UV95tfTO7cAO7x7pDD2OXp7GIKKEOqNRc785T_rI4Q0MTQTuLKIw46Cso-tHBOS1Sf9ecP39ZoSMXXHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=JR2yKtQNIkAl57oAVXYgEo_cOZsqiTphi7GpS2POKXRO8B6eO78sBgkRyobl9Z79vC0Rbw0sOaRU-JTs5ii3ncSA3KbSoTepXBauGUnK-gywlj4upPG0JUPFSWfbbMi0mqVdl7dF4kEP2giLUNdSi_6wxuO2ggsrJNoAtTcmi8VeXDW2euzDDrS2iaIxznTd7DJayPYJDUi7grsHV3VKOfULjbpB_CgdYdbmzr3-yRGS_j6I56EMQDva3DD5kpXjOlPnm8UV95tfTO7cAO7x7pDD2OXp7GIKKEOqNRc785T_rI4Q0MTQTuLKIw46Cso-tHBOS1Sf9ecP39ZoSMXXHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XHhjCgiGZbXNu3Rq3_ZYpZ0-AMlBGeEkHGe9LRvggaGT0BYxG1r1yPx3Bpbph2SpocsRsr0cA0jRI4sIb7uR7swer-0U2Ih1dhQpuK_ZT8u667Sg-v3bQEoSEDGasjZETcLzynPR35C2JwGpJQnwk2UpoSCEdgb-mXVtV0bafqk313iaEk6iR46IUcdBo_F47QxV6y-XzmbP5zK--ilPLO5cPsM1v6cI-Ywxxt-knC-VFh3krITyCn5DhZlT_kqdI4xn17Bp1m2e-CtQ133iK4--v-JYBYo2Gh-af3DgRCe0ZvwFeIbw7wC6bcSt2mPefb67vFt5zwJkazuuGV9usA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XHhjCgiGZbXNu3Rq3_ZYpZ0-AMlBGeEkHGe9LRvggaGT0BYxG1r1yPx3Bpbph2SpocsRsr0cA0jRI4sIb7uR7swer-0U2Ih1dhQpuK_ZT8u667Sg-v3bQEoSEDGasjZETcLzynPR35C2JwGpJQnwk2UpoSCEdgb-mXVtV0bafqk313iaEk6iR46IUcdBo_F47QxV6y-XzmbP5zK--ilPLO5cPsM1v6cI-Ywxxt-knC-VFh3krITyCn5DhZlT_kqdI4xn17Bp1m2e-CtQ133iK4--v-JYBYo2Gh-af3DgRCe0ZvwFeIbw7wC6bcSt2mPefb67vFt5zwJkazuuGV9usA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
