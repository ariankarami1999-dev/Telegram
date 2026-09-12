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
<img src="https://cdn4.telesco.pe/file/hqN87zEFu03QJ5rnfrJdOOX7D-ZabTKlfLlAZb-SCgBCpGgejOUWrb5jYD0uUbcEm_VMfkyz6uCAFdSWq8kipZ8oWWXz4Faky4pJ-LeWKPDFkztigVbCjEU6krbVPPyjJgJ07nvzZdRLz3lVEyvQJAseVk1SH2h1sJSYuONlz4W8Z771hp5YpQP_XKpwHfMJOU_-cOXtHwnmx03CgrHAV602ZGbSF1jqSccbPbFimzRnri6qsa6WB9IXeb3LQV6JiY4YV_Ohw2BRaJIN82H_QaXPRar3Abvzp6PwRckIf_QuGOwk9dXMi-z2GJS30bW87thNnid76LdytIwGU76mGg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 03:06:01</div>
<hr>

<div class="tg-post" id="msg-83322">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینطور که معلومه بزودی داریوشم میاد وردل نامجو  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/83322" target="_blank">📅 01:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83321">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4ed0fa89.mp4?token=tJ8gRpSXFaqBEyzkv2zMosiQJn2ZSUd6APGiTPMOSBYEVIh_AceIS23rQYe0Nm_6_ys6eY63fCzyeHiGuFLCfsaIukkJk7c-0MX3gaSJIxglOBICJK7J5iTdkbYOH598HeXVI4zyEKQrXqaOD3U0Lt_pgFZV77gRvbnFpcgSeQahBM9MbhWgoA044yiKYwfs2grxxc5zn5qrU9j7QqywSYHBhHZooUckTmV4QmkqxaSsqUwUyyF4JcvnfvSWwkjFbBJLfkWAKSOcwg9DnFDJ7VHzBNz_NAReXaSmJwD_xADhfeTlYzh7-CN4_oOpSuwhkjnfSstcsoYfC4aL-jEaN38ZedCotzUnjhdE70H7DuQa9MrwSechKutVNSGXoShBEM9RberLKqP8Ei5tClZfb4bk_xbhQEEq3vz3NV3FbWHJDvB4qAplLjP3U4MkzrG12SzqhCUeMeIUhp-ytr1kgax_Xh6vD2bFaYRN80pQFqsIzEMRkmy0_LmwOMSdttsHYjrdbABZDB3v6EfEbxhYleF4aKcyZs9e1CoPztWE9dzmoC8wXEfnYajus156g7IJn_L5uIc0II0q6F6Plfijl5jjR3HI2QhNpRJTpLa1VlSvV96LfHT9x7H9AQcBpbq00F7FJ87ORyWP9XgdVk62Hc2U7CJzhVyZFWknDApoDGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4ed0fa89.mp4?token=tJ8gRpSXFaqBEyzkv2zMosiQJn2ZSUd6APGiTPMOSBYEVIh_AceIS23rQYe0Nm_6_ys6eY63fCzyeHiGuFLCfsaIukkJk7c-0MX3gaSJIxglOBICJK7J5iTdkbYOH598HeXVI4zyEKQrXqaOD3U0Lt_pgFZV77gRvbnFpcgSeQahBM9MbhWgoA044yiKYwfs2grxxc5zn5qrU9j7QqywSYHBhHZooUckTmV4QmkqxaSsqUwUyyF4JcvnfvSWwkjFbBJLfkWAKSOcwg9DnFDJ7VHzBNz_NAReXaSmJwD_xADhfeTlYzh7-CN4_oOpSuwhkjnfSstcsoYfC4aL-jEaN38ZedCotzUnjhdE70H7DuQa9MrwSechKutVNSGXoShBEM9RberLKqP8Ei5tClZfb4bk_xbhQEEq3vz3NV3FbWHJDvB4qAplLjP3U4MkzrG12SzqhCUeMeIUhp-ytr1kgax_Xh6vD2bFaYRN80pQFqsIzEMRkmy0_LmwOMSdttsHYjrdbABZDB3v6EfEbxhYleF4aKcyZs9e1CoPztWE9dzmoC8wXEfnYajus156g7IJn_L5uIc0II0q6F6Plfijl5jjR3HI2QhNpRJTpLa1VlSvV96LfHT9x7H9AQcBpbq00F7FJ87ORyWP9XgdVk62Hc2U7CJzhVyZFWknDApoDGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینطور که معلومه بزودی داریوشم میاد وردل نامجو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/83321" target="_blank">📅 01:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83320">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ناموسا این آرسنالو منحل کنید، کیر زده به فوتبال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/funhiphop/83320" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83318">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار امروز چنل:
🟢
1.32
🔴
1.26
🟢
1.5
🟢
1.3
🟢
1.34
🟢
1.53
🟢
5.1
🔴
2.4
🟢
1.41
🔄
1.86
🟢
1.54
🔄
2.52
🔴
1.52
🟢
1.58
🟢
1.41
🟢
1.83
🟢
1.4
🔄
1.8
🔴
2.8
🟢
2.32
🟢
1.5
🟢
1.5
🟢
1.925
🔴
2.4
🟢
1.4
🔴
1.4
🟢
2
🟢
2.8
🔴
1.8
۲۰ تا وین
۶ تا لوز
۳ تا ریفاند
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/funhiphop/83318" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83317">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یعنی تو دنیا کسی خیلی جدی علی گرامی گوش بده و باهاش حال کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/83317" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83316">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKqjn_DiPCuI_NZnTxk0pC_Jbg-xGifdNV_GffIafuAMolhKOMz8OHa5xg6vpsJg676hYSF9201wskUNfpHR2r_zOTRrBBb7QYB2nYiMtzuWuHf9sPhcbjt0TCFAEDvz6cwjz5zqe9vZ3MtCbdboGX4Q7AtZIRIXLOrSLtp1ff1CLrooJpMobzZL9rB3mq9OS2lFu9JUw4IegL_urUxbXyuAZ_BNMxxcXgemFc48penMXOIVwnUCk21-prYXjIjAPzn5LI1eeKP-hwMGTFvqpG-LrQawlzK1tmdEVneTv4DBECgKhaPeNzVGSWOgYqfRLrmO3WgsO-DaohgLeP7puA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این استوری هایی که از علی کریمی پخش میشه ۹۹ درصدش فیکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83316" target="_blank">📅 21:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83315">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBtOsowJO14JaN6Ww4O3OfR6Y6F3a5Q3oYW84NVom8k0w62dPwcVH6AmnAM1hOorPCyqPZNUpJVevhYzKiKwJNHlkYkbog7v5rcQn_Htn2NHn5sXxRMsqBnfykaHkkfxlBBdDH8q3KXAIhJhSLtLgjAmeJRjHiDqZaO2_KRWgdXnrSAODnm5XRRH95TOR1svou1qersU56ld4ry9ZqlfBlpaEJrdMP6SpC9tbW6IfnCNhXl9Oc4Hy9PD52rfD0x2Zh2xcqvtME3PbIzEhQzjn-dpa6Ln8Kwg95RWaOf6ietFD6BQOdSp2FFd201Z5oT2CW1TKstNgD4R5fq4eeZtbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پسر تو کون نرو هه با این دختر اسکیت سواره رل زده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83315" target="_blank">📅 20:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83314">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49da2cdeb6.mp4?token=fWgORZ4hCdJ6lzogcyPOfWfo8lppoDcMCpbfF2hdf5TFOg2_tQRJjqPr2FYQgfRHWdPNJ_gQIaZS1wiVPHgvcbAOWUie0idsbLOz4rLwL1z85fJ0VeoYx_z9aEuxv8kX2eaSYU3Nvibof1QVJ5C5qzP5AAxxGMDBuK0_jn_CNut2NfgxfpDVpNS5fr-KJHsCcK4DxzMjRUfCIdaoXJRjKSgF5Lv_M8zp-1IkeiKVm45v4jRXMWWKq0UHFZW3ndK7V4bu4FGpPU2b4RSJEeaJYZX2a-0CTt-gD4sSNZtgOpwpHSkYyjbvIdwY9YD7gn65HNcEJSDmoWQDHIX8oUPPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49da2cdeb6.mp4?token=fWgORZ4hCdJ6lzogcyPOfWfo8lppoDcMCpbfF2hdf5TFOg2_tQRJjqPr2FYQgfRHWdPNJ_gQIaZS1wiVPHgvcbAOWUie0idsbLOz4rLwL1z85fJ0VeoYx_z9aEuxv8kX2eaSYU3Nvibof1QVJ5C5qzP5AAxxGMDBuK0_jn_CNut2NfgxfpDVpNS5fr-KJHsCcK4DxzMjRUfCIdaoXJRjKSgF5Lv_M8zp-1IkeiKVm45v4jRXMWWKq0UHFZW3ndK7V4bu4FGpPU2b4RSJEeaJYZX2a-0CTt-gD4sSNZtgOpwpHSkYyjbvIdwY9YD7gn65HNcEJSDmoWQDHIX8oUPPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک:
حادثه ۱۱ سپتامبر واقعا وحشتناک بود چون عمه‌م بعد از اون حادثه دیگه نتونست با خیال راحت با حجابش از مترو استفاده کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83314" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83313">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRE1ynebVZdmyDX14K-SWlypUmvg-Z4Y8FFLep3M7ItPb9v-HC_kTuoCaL5kAsAVIXBOq0bWgTlz1lAM525SMtNWH4pWG7JG2YmfmO2XcXmMpwFi2JI5At_FkyDZ4S0gDhfK-5lAVgjEDXyCWGjptPloeuHyuMowS8a6s1KA4LChbO64dTmAUkygW3yrm1DLR4nCk-AvD0ul14I0AM2aFS8Bsma9TkyGvC3Ng_nfYlAhn5p40kprXGCWenkgI2RusDKPO8xXT-FaUnzII9R7Z_2Sr-OhxMsdU0tb_PCwX8RYoK28EOYTwuYbQnTHEJmfSb4pPfRQitUjCrRb84FH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرو و هیچکس کال کردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83313" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83312">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-5D3NdOnyBwOeWOC-opwPasOTYiLqsHa7xdwqXltlQORD_FNkLYIVP8tsHW23nyTYrQiyqWJTAXfBT71Nik9e4ZHJnazn2yL1heZJG5hUmHYJlwelmluMAQ-wOH_ItiwyF-5ttrpYO1T22V5HJn4p6AyTX8xE4IyRFJ1NBRJpwWK1atG5r-HoyLvTCyNZDIvr_FU50seBkuDrZ8REXcBSj_8QsYRAsLoFfd-EtAc4cVvqW5zFzjasRzDH5LBFNBVJIhxv9S2Mna8qpnpVPefQj10XjPH3TUi1Be2mK2FmBVW6EFkA3klaB6_XsjkZuKZjZX8208lixdx8Sr9hofCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تعویض طلایی بت‌فوروارد
🔥
🔥
با قابلیت «تعویض طلایی» بت‌فوروارد، پیش‌بینی خود را در مارکت‌های مربوط به زننده گل روی بازیکن مورد نظر ثبت کنید. در صورت موفقیت پیش‌بینی مارکت انتخابی، برنده خواهید شد. همچنین اگر بازیکن انتخابی شما پیش از پایان وقت قانونی مسابقه تعویض شود، پیش‌بینی شما همچنان ادامه خواهد داشت و به‌صورت خودکار به بازیکنی که به‌جای او وارد زمین شده منتقل خواهد شد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/SUBO
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g21
💻
@BetForward</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/83312" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83311">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e048011808.mp4?token=StmgDznRA5hXTUmCiNqXmGItWJHAvbz5I6n2PKfi4hZfGU807sYVzugesge4-dvlrmxsIrG54_G74VLk3hRquuD0ktn0rcomIErZ3i0gs7zh2W0LCv4nhNGRuaGbVAx2AWcVX_1qeZVzs15GfYNfGGFj-MwPvkMEpCSsDsmftttYTY0U-l3MVNiBhDaK5c7hg0Jyuun_kbclE6GxXiHy8CqN_yvj5uxnRqAHERCLEc7nN1Z0ofMCOVGX2Mr21V0Oza2arSYNW8Qms1GPnYLrPKwJAEagbETW7CAAkwI1QgdfIku6c3iRvGxkUBXtfMxW0laJ5XXpklNzQa1cyK3TVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e048011808.mp4?token=StmgDznRA5hXTUmCiNqXmGItWJHAvbz5I6n2PKfi4hZfGU807sYVzugesge4-dvlrmxsIrG54_G74VLk3hRquuD0ktn0rcomIErZ3i0gs7zh2W0LCv4nhNGRuaGbVAx2AWcVX_1qeZVzs15GfYNfGGFj-MwPvkMEpCSsDsmftttYTY0U-l3MVNiBhDaK5c7hg0Jyuun_kbclE6GxXiHy8CqN_yvj5uxnRqAHERCLEc7nN1Z0ofMCOVGX2Mr21V0Oza2arSYNW8Qms1GPnYLrPKwJAEagbETW7CAAkwI1QgdfIku6c3iRvGxkUBXtfMxW0laJ5XXpklNzQa1cyK3TVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چی بود
تو سراوان نیروهای سپاه و مسلحین درگیرن بعد اهالی کوچه دارن تماشا میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83311" target="_blank">📅 18:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83310">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGEaoxX8q6P-bsHuKn8GsLPOET9kP0EXCEnjs6zp5pJ3ymeIHPRKe3FrD7927yGXmCXF6WO1GBbBacqq5gbxXBLM7oCRsZ9o3r7NMQyB8_tO83NQX0YyuXwEdbx6-5BTc5_YeKhiOGQRkV5Xy3zFjERid5vU9cOhU12p4numrU4T3YCJPCjU6jGaZo5N0mQSaekrBawxoOBK2cp0nQL_7LCqjTP2zLxyuwb1B6Stvz5hj8N__7mpoGyXaFE5v5Y8VVOgw5VU_1P-6wHxkkTvmL8Hd-cNQaaOblwRjsFl8-7jjtGInecvyjLEOoYyktlDe-CgmAJhbGq6s263YyEvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیت مپ این فصل دیومانده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/83310" target="_blank">📅 18:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83309">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkOCr_gnPMY3Jl1wGidrxJSAMd_pcfhJl3-vgVisvNdtC_2OgZma3NfhvmnLMtCkicTpw0wotjw0XwFBz_IOcl7ZmmJWYsYt-PLm0841hIz3jMCml57mzE4AXLeRqAFNtf4qpiVE4x8yvjPVuvaS0K_97mTB50DS2QgPZ-xROruDhSnc0QqewIUJQZehWtSWxR31lR1YrilqGZmaKO99eNfW9yX-aLIMBCZgIp9kHLoxEXlZ6lIJIbx1D0ejIVtasizQd9o_HWt16cpiXZtgzNNQDzS0tQ_r_Tm8n-r_TU9H9L3aLRhLp9ZE6MDr_rcL4TAcEtXZQ7DVOgmjmLs5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تیمیه یاشاسین تورک میلتی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83309" target="_blank">📅 18:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6JLVl1KVjWWR3XcHHVC5Izy5YOH37OeKrkV4JRZuylTR4nEhlY7F0zonvQsOex0xB7BjD5yKJ0zMXPp4QFkwBgiC70ftxtnOiaVl2ySaINcLjVc_qIaEIwCU1Co-gAXSvwICS2OVexuNifz6TWKluQolEMyVLhzoy9ppeNNd-wwPemhCLbFqcQPKq1MF5VFnnG0W20M1ple4ka_FIzziyMatm_P0UU_W9kpGqiwksFvFi8x7l0qBknYD86qMVKDoQ5WIVbO17Lhrd6aNJoHpa4TDdNPDpx4iIoHHTYGc3Iw811fkRbxnBBzpqh_fB-UL4oKrL8BTwZuc1xTsZ1how.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تیمیه یاشاسین تورک میلتی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83308" target="_blank">📅 18:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370c15519a.mp4?token=Np9tQcKFrQ0kEmKd33UwpkMlz7OvMkjNC3Q455D4fvIS6dqg62PtZc6R9TqctUW6lmY0f8Ah0xPOULib_6KXfB7NDr-5aDyX8snA93O4x8f8EoZOVWWqDde6FrAUvRJn-0skHrLcUL1i7gZv5KDoNZIvKbfGk-9QpMgm0Ijios1EJNXmN8er1rG1LlX1nzsGWMaiBGr5WsLe0rh-zqhHsdqCZTpZ51e9S9uWsl9D6emqYPZ7xC0xQVkI4ehnTlm4aIXU-o0qAGw6UH_wpwkq98CaHFAgZ4pbC9L2woud8FbETNN0R2MzwzfkUsosXSUhk7EfqXhVt31sn2op-g-_fJsWYItQrc6u0KSXXTf8JdXUFHPbf3WMn2OoTLkawE7_7iVclr2Tl863nJ2DnGlhzKvptUgm-lhksdtDotKqqkA50vtKBFHMnb6dC_T51Gszy6M5Z5aAwGUf4JaGsQMuxGR3pxsW20cN1MUZ6XOAKvPDkaR537GeSscLpTerjA7aR749YmGWe84nOqSfOhKCRTvfLrRS0yYUGhHmMlKTdN6Hnz90zb8eHBuy0dU8o99jaKnMTIBcwnkUdnE6RpScbzgwyLtR2tN5Rk54c_UgyUDZsIes_GNZLLFyETwP1Ueum_H-B9A3FM4_eRrsoEqtelt0HuV2lDEna4n2I7GGTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370c15519a.mp4?token=Np9tQcKFrQ0kEmKd33UwpkMlz7OvMkjNC3Q455D4fvIS6dqg62PtZc6R9TqctUW6lmY0f8Ah0xPOULib_6KXfB7NDr-5aDyX8snA93O4x8f8EoZOVWWqDde6FrAUvRJn-0skHrLcUL1i7gZv5KDoNZIvKbfGk-9QpMgm0Ijios1EJNXmN8er1rG1LlX1nzsGWMaiBGr5WsLe0rh-zqhHsdqCZTpZ51e9S9uWsl9D6emqYPZ7xC0xQVkI4ehnTlm4aIXU-o0qAGw6UH_wpwkq98CaHFAgZ4pbC9L2woud8FbETNN0R2MzwzfkUsosXSUhk7EfqXhVt31sn2op-g-_fJsWYItQrc6u0KSXXTf8JdXUFHPbf3WMn2OoTLkawE7_7iVclr2Tl863nJ2DnGlhzKvptUgm-lhksdtDotKqqkA50vtKBFHMnb6dC_T51Gszy6M5Z5aAwGUf4JaGsQMuxGR3pxsW20cN1MUZ6XOAKvPDkaR537GeSscLpTerjA7aR749YmGWe84nOqSfOhKCRTvfLrRS0yYUGhHmMlKTdN6Hnz90zb8eHBuy0dU8o99jaKnMTIBcwnkUdnE6RpScbzgwyLtR2tN5Rk54c_UgyUDZsIes_GNZLLFyETwP1Ueum_H-B9A3FM4_eRrsoEqtelt0HuV2lDEna4n2I7GGTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحمدالله بلاخره یکی فهمید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83307" target="_blank">📅 17:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پسر یه بار نشد توییترو باز کنم چهارتا آدم تحصیل کرده و سیاست مدار در حال دعوا کردن سر مسائل سیاسی باهم دیگه باشن، هرچی آرتیستو ورزشکارو بلاگر تاریخ مصرف گذشته اس افتادن به جون هم دارن از طرف ملت باهم جرو بحث میکنن</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/83306" target="_blank">📅 16:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83305">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93f927888.mp4?token=nc5nVi-rGsxLoCbN-qQyHUYMIqqiHe9xMGbJuAOwi4Mchr70qH52-pbEMnCc71yqDhItkaVyrBOimWvxSDI-yGqny6cfe9sTQAl2EIGLjO9KDCve2uxG_x2aMWJgmPzjFkQzNA3MdQofdINbEZwoiIglJ49L4pS1nDjl5QUdpN5FrVguPA9PKlB_b2VcJ2IVbYTkGBpiBkmX5WME_oblnNccccHn5wN-IzxQP3z5eHXrWm_YXlL9Kj1u1ch9UVBv6R5c0Bj0xrNN0nNvrSRGoPE86RhQjHva5HD95-JUlpWaBdsOBeR6qW9fo3182kN55_KqniMwZ78SJcbm9ge1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93f927888.mp4?token=nc5nVi-rGsxLoCbN-qQyHUYMIqqiHe9xMGbJuAOwi4Mchr70qH52-pbEMnCc71yqDhItkaVyrBOimWvxSDI-yGqny6cfe9sTQAl2EIGLjO9KDCve2uxG_x2aMWJgmPzjFkQzNA3MdQofdINbEZwoiIglJ49L4pS1nDjl5QUdpN5FrVguPA9PKlB_b2VcJ2IVbYTkGBpiBkmX5WME_oblnNccccHn5wN-IzxQP3z5eHXrWm_YXlL9Kj1u1ch9UVBv6R5c0Bj0xrNN0nNvrSRGoPE86RhQjHva5HD95-JUlpWaBdsOBeR6qW9fo3182kN55_KqniMwZ78SJcbm9ge1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی اینارو حاجی
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83305" target="_blank">📅 15:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9e4acc8e.mp4?token=D8U4ANJsVVSm_OOih_Ij16zBtr2AsX0-lbIEGkqpJjjfrZu9NG5ZZmhmAWkXKJ39X1y6smqJU_lD5SvNUjwd-7WUze2Wz9vMPcaLN7Xvi46wnhu1GqIAo9YPcafdhg7chwSV-lHc4e0QiUBk5WplGb-ve88EeSi-P7zltfLAyMeQaU7jGQZ7XCDZqA5y7JrXz-Ij2IIzhVQNGJReBXz_FKsJGIgJTTUwwTb0X11nQMeCkAM5Y5_8IbNl-8rD86BEQBzk8GKu5iVLy3zhLDUA04D97t0Y1zTcRgus587ROFX-VBFaipwYLMR6EK8hUrdC7efrCVvbw5fNv4updETRDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9e4acc8e.mp4?token=D8U4ANJsVVSm_OOih_Ij16zBtr2AsX0-lbIEGkqpJjjfrZu9NG5ZZmhmAWkXKJ39X1y6smqJU_lD5SvNUjwd-7WUze2Wz9vMPcaLN7Xvi46wnhu1GqIAo9YPcafdhg7chwSV-lHc4e0QiUBk5WplGb-ve88EeSi-P7zltfLAyMeQaU7jGQZ7XCDZqA5y7JrXz-Ij2IIzhVQNGJReBXz_FKsJGIgJTTUwwTb0X11nQMeCkAM5Y5_8IbNl-8rD86BEQBzk8GKu5iVLy3zhLDUA04D97t0Y1zTcRgus587ROFX-VBFaipwYLMR6EK8hUrdC7efrCVvbw5fNv4updETRDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر پیر اومد دست این دختره رو بوس کنه نزاشت بی لیاقت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83304" target="_blank">📅 15:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ درباره حمله به خط لوله نفتی عربستان:
ایران به احتمال زیاد مسئول این حمله است!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83303" target="_blank">📅 13:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=DhDawXX9mew_YcwzWc2fK0zXkNsoU8hSdBl6KkTRBUIMxt5rbc64SfZ5V9QwTOcF3Lci-wxw98voH0CPz6MGaa6BXQR8u8OiXJHT2uhG1nzGwouCoitU4By3M4qo2MW3CHrP44GZN-Dax0i6rwxmzNWPqrO9mOSv0yBCvKJ_ZEaerSmxM25ytbb6LY3tLR1aOrxL4YGUq3PgdhNL8DrKl2c2TWvatORCSCp1DC0AkkpV8mDvPRsefN9SphN-EOKyxgtIBXjyx7THTL6GAxiyfEeePsLm547OYH6R38EfuoxIpH-A-7SKHis2L06mbL0mjvLo3q6tlEKIC5e3HYelQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=DhDawXX9mew_YcwzWc2fK0zXkNsoU8hSdBl6KkTRBUIMxt5rbc64SfZ5V9QwTOcF3Lci-wxw98voH0CPz6MGaa6BXQR8u8OiXJHT2uhG1nzGwouCoitU4By3M4qo2MW3CHrP44GZN-Dax0i6rwxmzNWPqrO9mOSv0yBCvKJ_ZEaerSmxM25ytbb6LY3tLR1aOrxL4YGUq3PgdhNL8DrKl2c2TWvatORCSCp1DC0AkkpV8mDvPRsefN9SphN-EOKyxgtIBXjyx7THTL6GAxiyfEeePsLm547OYH6R38EfuoxIpH-A-7SKHis2L06mbL0mjvLo3q6tlEKIC5e3HYelQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی این چه اکسپلوریه من دارم آخه
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83302" target="_blank">📅 12:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83300">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگه رپ آمریکا به کیرتون هست، باید بگم که Lil Durk تبرئه شده و قراره آزاد شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83300" target="_blank">📅 11:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83299">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه گزارشگر تو شهر وان ترکیه تو یه گزارش خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده جواب هاشون رو ببینید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83299" target="_blank">📅 11:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83298">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e472b3e6.mp4?token=RQg0tGUAakwH00rzjZhe-tPmqEomB0w31ZTwWxQO79xbRiCoudDU0Oj84LYd5xGOfbK9Tob6keVqvNCUVeaU1L_PuzSSBnR4kND2zMkp9stwm1y8GnHtg7fP7ljcIbP3Ul-jw-n3ehGHw8aU-kcIdBXVGrlk6XCkX1eazcoJ3AnXhRcqkG2cnQnxADl11FUk_K0uAVtluFqaAZTRZUzH_of6v-jugmy0tYI4Wzxq8QpIh6HvY0r9SN623An7jxuS9c4HxAQLYgMx2gJKvgULeNVEn-wB2GV6CwH2BbI7fruV4oFJ1MIcUwpve3PhZN_3VaS4bcKUpXVlAokX6ID9LFDu02eYw1dOJ-VNNOfP4qBk4546phzUNYqejHSwbdnbpv3Q0NswWDIjvWwZQvD-fq1Lp2sAiRVq2fE8Ly9inJkYymD3cg1t-jRNGVeA7ktlgHAtc6_Zo1S8DZTEC02QPTp5ZR921WtYbTf7JGHKc0T6k4Tl7cpp6MIH9wFEU6BRzLI61X1opmP4KDGfvL_61c-lXodpZcg7u0FpFqQqHelno6WIhu_-f0utwK5_ax0Iqk8eUqTwFlcJ6LWVnniBPWKGzXhKqc9-3VqqJH6DLx-cwV80v_nprqKZG-_Y4ngvecaOmRwXSLFD8ggZoMm1LiZmsRqjKmBaC2RodUxoY2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e472b3e6.mp4?token=RQg0tGUAakwH00rzjZhe-tPmqEomB0w31ZTwWxQO79xbRiCoudDU0Oj84LYd5xGOfbK9Tob6keVqvNCUVeaU1L_PuzSSBnR4kND2zMkp9stwm1y8GnHtg7fP7ljcIbP3Ul-jw-n3ehGHw8aU-kcIdBXVGrlk6XCkX1eazcoJ3AnXhRcqkG2cnQnxADl11FUk_K0uAVtluFqaAZTRZUzH_of6v-jugmy0tYI4Wzxq8QpIh6HvY0r9SN623An7jxuS9c4HxAQLYgMx2gJKvgULeNVEn-wB2GV6CwH2BbI7fruV4oFJ1MIcUwpve3PhZN_3VaS4bcKUpXVlAokX6ID9LFDu02eYw1dOJ-VNNOfP4qBk4546phzUNYqejHSwbdnbpv3Q0NswWDIjvWwZQvD-fq1Lp2sAiRVq2fE8Ly9inJkYymD3cg1t-jRNGVeA7ktlgHAtc6_Zo1S8DZTEC02QPTp5ZR921WtYbTf7JGHKc0T6k4Tl7cpp6MIH9wFEU6BRzLI61X1opmP4KDGfvL_61c-lXodpZcg7u0FpFqQqHelno6WIhu_-f0utwK5_ax0Iqk8eUqTwFlcJ6LWVnniBPWKGzXhKqc9-3VqqJH6DLx-cwV80v_nprqKZG-_Y4ngvecaOmRwXSLFD8ggZoMm1LiZmsRqjKmBaC2RodUxoY2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه گزارشگر تو شهر وان ترکیه تو یه گزارش خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده
جواب هاشون رو ببینید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83298" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6LarM4cb4PIYlvXM_QnIGvDG9jIH6bpw1SG49aLTM72nM009QSxGvJKWmhVpRBP_o2ChXILWHtE5W-KaMiBPYPmWe8fKMuOIIQ8tgE_DpG-BC4n7GQBCxftcTYCiaRGOiOPl6odGfLW9srbbEj2xz5px7yuwd8eXAyhoj735mPuZ2GEgd3ek1t5wjFzDRCvBgqU3dnaXZYGQDS6WqMQ3fiUQ1VDU_nf3JtpP84DU90JDl5eV0V2jd8CGcDiC4LsvFf1_n6pbG0MJjyEXboQq_IPUzn85cE190tBM3cmCadnye6TOJklArfowQ3zOyP6GnApnJRed0IjUkkalZTIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
شارژ کن، هدیه بگیر! بونوس فوق‌العاده ۴درصد
⭐️
💰
۴٪ بونوس نقدی روی تمام شارژهای حساب دلاری!
💰
🚀
می‌خواهی با سرمایه بیشتری وارد بازی شوی و شانس برد خود را چند برابر کنی؟
🚀
از همین حالا، با هر بار شارژ حساب کاربری‌ات، ۴ درصد بونوس نقدی هدیه بگیر! این یعنی پول بیشتر برای شرط‌بندی، هیجان بالاتر و شانس بیشتر برای پیروزی در بازی‌ها و پیش‌بینی‌ها.
🎯
💥
چرا این بونوس را نباید از دست بدهی؟
✅
اعمال خودکار روی تمامی واریزی‌ها و شارژها
✅
سرمایه بیشتر برای ثبت فرم‌ها و بازی‌های کازینو
✅
فرصتی بی‌نظیر برای چند برابر کردن سود
🃏
همین حالا حسابت را شارژ کن، بونوس‌ات را بگیر و شانس خود را امتحان کن!
🌹
کازینو رامسر جایی که هیجان بازی هیچ‌وقت متوقف نمی‌شود...
🅰
r21
🔗
ورود به سایت و شارژ حساب:
⚡️
لینک ورود بدون فیلتر شکن به کازینو رامسر
💻
@C_ramsar</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83297" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">همینجوری پیش بره ایران میشه نیرو نیابتی یمن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83296" target="_blank">📅 11:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83295">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صبح بخیر
مرز شلمچه بین ایران و عراق توسط عراق بسته شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83295" target="_blank">📅 10:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83294">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شلتون ست اولو که باخت اومدم ۶ بزنم رو بردش، اشتباهی زدم رو تیافو</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83294" target="_blank">📅 05:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83293">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7W2ic-CWxFE0ReToMPLYxkYg1VrR2sG33HffwcvQ5nf1Tbc066k8OIL46McPtqm1KJ9IG70A094KvUke5GrOrUp5tB8urEV5o8Jda9T4dU0nWSU8D8aIg-iIC4MAPlpX3ye9pxQSh8x-v3edz7fhRUDiXsIkvWYuK6r0wu0cNFBsxAiz0YEVuua9-zjLWesRI1Wa_MUZ4qPU1iFuyMx64yrCQV9ABmZfcPAbs8K7KRJoxPByZg0fe6nfjH3JfQx_myBP56jqR_6N0N2BO2HcYozWzsVc69vNZ-Wx0uoR13ntoT0kXV08Azyd0vvGczdleT3nhsGkndzuIymY7topQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلکسیون نمایش زوال عقل با هوش مصنوعی توسط جهان پهلوان کامل شد.
❤️‍🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83293" target="_blank">📅 02:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83292">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmndvYNJJPufH04m6qgcg5PQFWN6dbart-V8ZK6b7cRd1PCfdpr5bmBmeniz2WWBbC1CsgcW0AuPmNDtRXiH16Rl4R2hu_BmLXP3K9SdDUkrAnc22NgI_KRyiUV-aJfrf9_GgoGhusmLWKI_zaNBjdm9Ubdt5h298bzwaH045g3Ll2gK9fFBwJpRAGO-J2sW-EhspOCjUhhDKrC97iKs1u3EFnDvChQs-YnNIqCYkoH35T58mlGT1iC8t12chCrM8oU6MEfBlvC8uljrtuq3Llod0403XfPsRSq4UB_L8h1uPcgHNDeKabYZ13XDokiAzLQKUZfYRTYQ8UV9Wi-q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83292" target="_blank">📅 00:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83291">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njYuqXBMIlWtFHd47mCHmFRzwLHTHyWxUeQx6oEZym0Tu6pUFu8ojxIJoVbxCqlhR3SVjuGjYyHjW-op1M5WvRa2w2LBF3_8GPtGr0GUxTFFU-fks_Xp7pHC6FyKTPs4Fa-Sm3tmsuQYNxPXByIpl5SOhkDKfi8fMfvmLFpYrDBhWUsmevnL-OUcQHMr71XyAmBcoUxoQeObDfIZBNzBc1Lr-6IaapYt-jrtMq_SzV6CHWXL5YxG-U217wVi95XnpFPj5M9KaGwQ2mGg5L3ULDjUUHhUPuISwDGpyVvuYCR_ibstYrEF_zSe4AnQ1x2dR8BdTg5J_6gHoT2riENZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پسر تو کون نرو هه با این دختر اسکیت سواره رل زده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83291" target="_blank">📅 00:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83287">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شرکت آنتروپیک، سازنده‌ی کلاد اومده یه گزارش مفصل از عملکرد و تهدیدات و اقدامات هوش مصنوعی کلاد منتشر کرده که توش یه بخش راجع‌به حکومت حاکم بر ایران خیلی جالبه؛
این شرکت ادعا کرده که این حکومت با کمک مستقیم نهادهای چینی، به استفاده گسترده از این هوش مصنوعی برای رصد و شناسایی مخالفانش در فضای مجازی پرداخته و تعداد زیادی از مخالفانش در داخل و خارج از ایران رو دقیقا با همین روش طبقه‌بندی و شناسایی کرده.
همچنین این شرکت ادعا کرده که این حکومت، از طریق همین هوش مصنوعی، برای طراحی طرح‌ها، سایت‌ها و بدافزارهایی که تهدید یا استخراج اطلاعات و به دام انداختن مخالفانش رو در پی دارن، تلاش‌های زیادی کرده.
ادعای دیگر این شرکت این است که این حکومت، با استفاده از این هوش مصنوعی صفحات مجازی غیرواقعی زیادی ایجاد کرده و از این طریق پروپاگاندای عظیمی را برای خود رقم زده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83287" target="_blank">📅 23:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">زندگیتونو بزارید رو برد کارن خوسانوف</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83286" target="_blank">📅 22:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=M1bTRMKDKUtL3OCEqh0pMIWDgW61CkOAgT8RzR38hLv_mGToEaY1P6t3iAqENU0hc5POpd1sX8XjBGw7WAPxKG9JSr5OnPMi8iXiYwTlfZM_YHKXy6pejI2-VLbR3pSQPbm7sfcqYTtmz7EKM_1DJZckJEMReQeATr_jp8Rb_kI-aIRqTMlMW9XaRuciDQk0PiXFfHsY3650o2_5j3Qto16SqeNgjpWz-Sex-RDbQGgOhVv99HkWwNiudBukZe5OEYLWxf44KvfkMJ7TAFbB8FA4HonZ-uisYkm7CDIR2DW8UiSd7vuiXaq-_aQQMV_-H0ReQYwlx_06kwKcZDPv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=M1bTRMKDKUtL3OCEqh0pMIWDgW61CkOAgT8RzR38hLv_mGToEaY1P6t3iAqENU0hc5POpd1sX8XjBGw7WAPxKG9JSr5OnPMi8iXiYwTlfZM_YHKXy6pejI2-VLbR3pSQPbm7sfcqYTtmz7EKM_1DJZckJEMReQeATr_jp8Rb_kI-aIRqTMlMW9XaRuciDQk0PiXFfHsY3650o2_5j3Qto16SqeNgjpWz-Sex-RDbQGgOhVv99HkWwNiudBukZe5OEYLWxf44KvfkMJ7TAFbB8FA4HonZ-uisYkm7CDIR2DW8UiSd7vuiXaq-_aQQMV_-H0ReQYwlx_06kwKcZDPv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83285" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PixfEha0PBCbmW3gDNZGMT7x2Fcm86lEtUNjudiS_PR0eIJHVvivO_5pHpcDG5aL70-5aIPeZddmHzJyFjvgwWhql9CWjCtVtvGuGHqIlAeyaQ_A8zpKZ4Xyz9Lhpoh_VL9fpeXyww4OWSrPWgEhET2JVvU6Zl7aeq_g-7hEixKEiZJujP5j8z2I5mGH2UX8Mdju0qoVrHGri-2ddiwH0f_Xf_wJjHAlAFRX2pE3x28cfEXU10_l_Offa1HuT9f1DHbmP9a4Q3bJWFs_qipqafGygxcsxdfagh-jZWcm4sGmuyBSKyRwIllBbdOVRO51g0y59INiio0_GwS8zt0_pncfJckjE1lBMPI_ZwaKO3QrliaJX0cjZ7ywbPYDyDA9lSyuI0ZPFWhkiiZMtSaygquGtoMGfZ3PZc8RdpVNfx0UJL6o00nascS94Ux5gNQXl1_vxRLT7N2XEXQQi2palQKcsd_z-sFi5PXCz_ZgKu1NAUmSeZcho5G7E4FT8kYuCZZN2Bw7JFmeeXM5kPMRUe5m8nIEwkA5MBZYvnHrSEonm3qTAQKcqcPVpHC_gO0FSGLWLY_bN-mJDJ4hVKevchs4pIMcHe2RfzqR6e9s8CWK4mJ2N6OjKdwwZCPQQ0On1RItiLuew3LziKLDDLS8lcI7Kw_2KffzeatY7acjp4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PixfEha0PBCbmW3gDNZGMT7x2Fcm86lEtUNjudiS_PR0eIJHVvivO_5pHpcDG5aL70-5aIPeZddmHzJyFjvgwWhql9CWjCtVtvGuGHqIlAeyaQ_A8zpKZ4Xyz9Lhpoh_VL9fpeXyww4OWSrPWgEhET2JVvU6Zl7aeq_g-7hEixKEiZJujP5j8z2I5mGH2UX8Mdju0qoVrHGri-2ddiwH0f_Xf_wJjHAlAFRX2pE3x28cfEXU10_l_Offa1HuT9f1DHbmP9a4Q3bJWFs_qipqafGygxcsxdfagh-jZWcm4sGmuyBSKyRwIllBbdOVRO51g0y59INiio0_GwS8zt0_pncfJckjE1lBMPI_ZwaKO3QrliaJX0cjZ7ywbPYDyDA9lSyuI0ZPFWhkiiZMtSaygquGtoMGfZ3PZc8RdpVNfx0UJL6o00nascS94Ux5gNQXl1_vxRLT7N2XEXQQi2palQKcsd_z-sFi5PXCz_ZgKu1NAUmSeZcho5G7E4FT8kYuCZZN2Bw7JFmeeXM5kPMRUe5m8nIEwkA5MBZYvnHrSEonm3qTAQKcqcPVpHC_gO0FSGLWLY_bN-mJDJ4hVKevchs4pIMcHe2RfzqR6e9s8CWK4mJ2N6OjKdwwZCPQQ0On1RItiLuew3LziKLDDLS8lcI7Kw_2KffzeatY7acjp4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83284" target="_blank">📅 22:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=Yg3KZgjD1lv9EFBkPNZ_d74WjHRLrJCVYuQGe3MaEXAyTzSPd1nWN7bI7lfVgqWMsTumxmklFGQkBwaZGKTaTIINhE_Gp4FQBzpE1mXem7zyJyGwAKJIrHaCdq4R3OPzzO3SiPRD1mnGIPrECHFj74vCpG_MgwsGCx2ixxPjAPumTwtEwC6ds2jRgo-PfpOqKy1N7X1tCOVbO3rgGa9-BE6NHW4es-sH9sn_rh2-m-pnVGP-nAoPBGjk9V0eF-y6rD601uqaQyaWvMgk9TkmO3X6P-Ecjfwk7elzQlg0LXxZfvv2gh6JhkH_UyWzMvk5xrv2eI5D-tRSnVjF3ggKnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=Yg3KZgjD1lv9EFBkPNZ_d74WjHRLrJCVYuQGe3MaEXAyTzSPd1nWN7bI7lfVgqWMsTumxmklFGQkBwaZGKTaTIINhE_Gp4FQBzpE1mXem7zyJyGwAKJIrHaCdq4R3OPzzO3SiPRD1mnGIPrECHFj74vCpG_MgwsGCx2ixxPjAPumTwtEwC6ds2jRgo-PfpOqKy1N7X1tCOVbO3rgGa9-BE6NHW4es-sH9sn_rh2-m-pnVGP-nAoPBGjk9V0eF-y6rD601uqaQyaWvMgk9TkmO3X6P-Ecjfwk7elzQlg0LXxZfvv2gh6JhkH_UyWzMvk5xrv2eI5D-tRSnVjF3ggKnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: هانی رامبد رو من گنده کردم، قبل من هیچکس نمیشناختش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83283" target="_blank">📅 21:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83282" target="_blank">📅 21:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3D0OzzRoekvaqCAMoU7tNv0udmVey-1lOcUCsLEkgwPXv393DjAmoNSflcSCOPY4UZcG9nGz3CRIzIgbJ_6O5ONVeknhiyCTuVZ1h-uLBNw958Td_H5XEaN4OqtzdkPVLCUexaBMb9DJb2MFBkoWY4Oa7t-nMVIHyPBfzlWfHAJSqKRg2sseKeTQg2Ubzdm3tZDx95UJEm0t88sBOsULQOr2sKSqj-9-awLZztsG_twPtiO-LH43Hy7WDnIKEsAEkf7XjehEPUCDL4RxhRqBl_2wPKjdZ-E_zBWYjV2eXDt8d9UETRJU4Fw509lY3-iflwvuzjSBFjUwqGy8UZcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83281" target="_blank">📅 21:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جدی این وضعیت دیگه داره تکراری و حوصله سربر می‌شه، به نظرتون سیزن بعد از کی شروع میشه یکم پشت کامیونای سازمان ملل بدویم یه ذره هیجان زندگی بالا بره؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83280" target="_blank">📅 20:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83279">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سعی کنید تو این دوره زمونه درامد دلاری داشته باشید
من خودم درامدم دلاریه، دلاری بت میزنم و میبازم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83279" target="_blank">📅 19:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83278">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه سریالی هم هست Special Lioness یجوری توش ایرانو گنده کردن منم کم کم داره باورم میشه ایران ابرقدرته.
- مثلا ایرانیا رفتن افسر ارشد اطلاعاتی CIA رو تو خاک خود آمریکا دزدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83278" target="_blank">📅 19:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83277">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=mUqqLaWTfSdz622WAAHx_8MyEL5BivpSyKWi4d-RygQ01-FwxuU1Xn3j7eCx6WFanQLyLnuKcV3hJ-kcvZ0PswBOrAxWuYaiKMYT_DV2f6naXMRokoRaJUq4wIOFfXbgXcKVoGThaPK8g6V4v3EHfLjRw-MYNzgbvrLAI1OlnUxN33gCRS0OY2PTTeunYT6oZo_naPS94oqva7WOUTOTGqIQu_X-2ROgM1_-DnNsI83j2gQ61Z0AAFrJA2Ke660iowVdvSyosNQ68j2amJPxqIw4ANe5vCTUyI6z917UtKjlZxT0ffp5mPsse8l9QTwzE0oo1BhoaDB5tLdSIsZXyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=mUqqLaWTfSdz622WAAHx_8MyEL5BivpSyKWi4d-RygQ01-FwxuU1Xn3j7eCx6WFanQLyLnuKcV3hJ-kcvZ0PswBOrAxWuYaiKMYT_DV2f6naXMRokoRaJUq4wIOFfXbgXcKVoGThaPK8g6V4v3EHfLjRw-MYNzgbvrLAI1OlnUxN33gCRS0OY2PTTeunYT6oZo_naPS94oqva7WOUTOTGqIQu_X-2ROgM1_-DnNsI83j2gQ61Z0AAFrJA2Ke660iowVdvSyosNQ68j2amJPxqIw4ANe5vCTUyI6z917UtKjlZxT0ffp5mPsse8l9QTwzE0oo1BhoaDB5tLdSIsZXyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق تجربه شخصی ۹۰ درصد فیلم هایی که تو اینستاگرام معرفی میکنن کصشره و بعد دیدنشون پشیمون میشید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83277" target="_blank">📅 19:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83276">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLhQOOaaXn-j5xFnM4gkTk9exeovulin7MGWExyvAG9M3wuqtW4wR-JjxCMXTT_3huKJXI0t0xda0MP1-BQNKmnIY9DoIEs-EKIUtNpN02u4vTSRKER0S_t_RvCnemkJZMzT29W98t2Oe-FjeA4UmVdhkBcB8WZXPiHg849YFrfNsUi4pcCUy8QuSpKTKtShJDSHKA5_RtiTJ7rV99eWdoYheN48rWwkVyg2AjzIwk-9bp45r6jEs_WRudCXp9SjaEw6ZaAx6MxWqtBzSZ9TptZyGQSBTDAL2nu9FOmjlCWiQg-IG2YC-2Y8YZyHZ3mXbN0Mcuh1xWwqmuqwbm3N-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی هفته چهارم سری آ ایتالیا
🇮🇹
⚽️
تا دوشنبه بیست‌وسوم شهریور ماه، با ثبت حداقل ۶ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته چهارم سری آ ایتالیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بتفوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/SEA4
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g20
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83276" target="_blank">📅 19:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83275">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb5n7U-OQeLVnefTxntF2t7OlCBiawfYHkPY61wKWeSAMNtIjLEImBEc2m-9s4tpM7y27jO1Py1N-9ZpaMUnm6jqxU7VRqSlOvLbr-YfwMF-znDvFmwZUpvCwJD5wXHQoMUAQrkb1jIxDRFwu9gaDO3VUFh_5rB4CvMkBszofp-JAaHwxgJ6tcX9bm4qS3CC7MT6W5eOJg8eyqAAPR-EXQmycJ9j0y1eU8Rm0aJjxoutNM17o5l4ZrHyB6pil9DLE5TW53CQlCppW-1QDUl59KimCvNYfLxbAeePAIgN7LlGGfI29Mx241BRHVoSmmj-lE9Ro9gyO0EPX1FifP582A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیکس چند هفته از تمام دنیا جلوایم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83275" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83274">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=Z3VPKwndKz4p1GKGPvHePSMjp9qG72sD6Ax2sWpFps0osSh04vGSbwTrWT5RHP82KF0D5uA_b6kxONafyacRnltZAOZArhKSHY7OSooIz-74NLimfcWWr9psxHMh-hw1S64r0rM6dFDzydvxNq7sy-l4guuC8Tlmrelvm7h4nNodg8SwchOho0AJpETkWELBG6B4RXbHgJsKBLJGkLeVAjpvS_nf3j0nVQfp1Z4rotAxVNQERoCAg-c3-NxDjA2HrBs_VPL3iv3gVmTBloq21lDErj4qH5_ulyq-udH5IHkS1paWhYb1SgUuhjQ0rMvisc22e92XAlwAaDSTSByFig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=Z3VPKwndKz4p1GKGPvHePSMjp9qG72sD6Ax2sWpFps0osSh04vGSbwTrWT5RHP82KF0D5uA_b6kxONafyacRnltZAOZArhKSHY7OSooIz-74NLimfcWWr9psxHMh-hw1S64r0rM6dFDzydvxNq7sy-l4guuC8Tlmrelvm7h4nNodg8SwchOho0AJpETkWELBG6B4RXbHgJsKBLJGkLeVAjpvS_nf3j0nVQfp1Z4rotAxVNQERoCAg-c3-NxDjA2HrBs_VPL3iv3gVmTBloq21lDErj4qH5_ulyq-udH5IHkS1paWhYb1SgUuhjQ0rMvisc22e92XAlwAaDSTSByFig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی این بچه چه گناهی داشت که پوتک باباشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83274" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83273">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ و‌ آمریکاییا بفهمن با ۱۱ سپتامبر همچین شوخیایی میکنیم همین امشب با اتم ایرانو نابود میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83273" target="_blank">📅 17:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83272">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تصویری از فاجعه ۱۱ سپتامبر:
🛬
🏢
🏢
🏢
🏢
🏢
🏢
🛫
🏢
🏢
🏢
🏢
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83272" target="_blank">📅 17:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83271">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستان رئالی شما برا اولیسه بمالید مالک بایرن نمیگه اینا خوب مالیدن پس اولیسه رو بدیم بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83271" target="_blank">📅 16:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83270">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دلار ۲۳۵
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83270" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83269">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83269" target="_blank">📅 15:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fo1efToS-eMp23E6IFVc_a5zvhAvTRSdTzfdUMkRzB203oxCfLBGyeBMzocjaDdh90J3PjQa8Jm8iQZYV9BS70sazaM2DxJcbHkwD-dS_G3xB4seGCmM060cO_GS3D6QvuKTzX9oZR6WzydN1BKIb1t7yxH-im8PwSYUHmM3bZxQciaA5QuJAOWG1Fzwp8YJg-prsZyUniKlm8dDcLsdCicsns7daGvZihL3BaCJ7IA6owxOjw6mWeMZBsEncN5ifgPzJRrsJpaXcsCMCY6q4wO85HPaX5jHZkKelGm-KN7--m-fRH-bj0PkHndyqE-VrP30HDwDW8hKLQ7LLla1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlziI4aOoakl0mgjWo-iTHwTT1ysnHv1T2vpC_Z0ZKc73VwhMGU8_ivVdKb0kEQpoTNxLmoa4uE4GF2UQeYRyWEHyO3FlzbvmFiB4ARiQPlAjC9FRgeaWBguYicS7EY5ewuHK_AWRzYmronhGJ45-DM7UkxF_qXJ8qdm58fUdCBJsUxVtjg9gUotbYMWuntKqCPWtzG-su0SK5no9ySuN9rLLx0z3NUSzGyiH7BSxCrt5_JjtxuSan3na0hloHlUzKckO_dx1z2bGlAQNIGK1ut-VLJh0G1ddJG_TxY52myjQmZvNHMdNe5q-t7VVYS5eXUbWg-8vYq_8zEpHa9FkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همدردی مردم ایران با مردم آمریکا همزمان با حمله تروریستی القاعده به آمریکا 20 شهریور 1380
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83267" target="_blank">📅 14:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=BYEXM8zsK_BgVJ-XvnN1hxT6ZBHJQGrXPYlZ6bw50qqBgIwokmzjwQeZRw5V6KfZ2T6lF5C6FKELfFhnV-2qWofI6j2FuWE02yn-ehOhyWCv6Gqqpf5RSvVEV9vJZX3usYoNjJIJn5bkVbv2ZTGvAknE9OH9XfvUyxDgVAuaFKEPzqHdZjyFcFfJ55dhm2NxM9r2W8ObcE8069EKMzx7N0TXSplysoRDoq523ApFOmKF5_H82JvbTG01GLszxHcJnyyqjcX-ZgzG46zFsVbn_Tngs3MkFsuDqsz9syA6KMFYt1D5UG2b5z7tb_fYesQWORshRgllI9FzIGA7YDrijA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=BYEXM8zsK_BgVJ-XvnN1hxT6ZBHJQGrXPYlZ6bw50qqBgIwokmzjwQeZRw5V6KfZ2T6lF5C6FKELfFhnV-2qWofI6j2FuWE02yn-ehOhyWCv6Gqqpf5RSvVEV9vJZX3usYoNjJIJn5bkVbv2ZTGvAknE9OH9XfvUyxDgVAuaFKEPzqHdZjyFcFfJ55dhm2NxM9r2W8ObcE8069EKMzx7N0TXSplysoRDoq523ApFOmKF5_H82JvbTG01GLszxHcJnyyqjcX-ZgzG46zFsVbn_Tngs3MkFsuDqsz9syA6KMFYt1D5UG2b5z7tb_fYesQWORshRgllI9FzIGA7YDrijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت ۱۰۶دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83266" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83265">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دیشب نه در آمریکا، بلکه در یک کافه در قم از آیفون ۱۸ رونمایی شده، تو این ایونت همه حضور داشتن الا خود آیفون ۱۸</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83265" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83264">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8758825884.mp4?token=mEVXGjiFvR74O7wfgTp2ou5-KSduVW13fEKktYTaoF0vFKhPlEKRj8SHJV5Upst1kIMrAhJMiUOb42WzY_wGgQSbBQSws3JoKsoVfCunRbYGGFOvq-B5IBqU5vRhHilFUykj0QYvrdZNc9m7KcxDrFot8_y5zIzv7rFrh0aBSQHYzZTvR5ESu1iWSRoxR8AVwizkEuI5hZzDFY7NsM75FOqn1uCKadhmIUuxLERgQK1YgVWHzFyLL9MfdjZJdb7XXtfu1tyfPrqyAfj_6gqJRYIBSnvI68d04xw7rrSEtRKj5HoRgZyke_asuFk9dv0rQO3kFWOzIHphjwJvg-cK6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8758825884.mp4?token=mEVXGjiFvR74O7wfgTp2ou5-KSduVW13fEKktYTaoF0vFKhPlEKRj8SHJV5Upst1kIMrAhJMiUOb42WzY_wGgQSbBQSws3JoKsoVfCunRbYGGFOvq-B5IBqU5vRhHilFUykj0QYvrdZNc9m7KcxDrFot8_y5zIzv7rFrh0aBSQHYzZTvR5ESu1iWSRoxR8AVwizkEuI5hZzDFY7NsM75FOqn1uCKadhmIUuxLERgQK1YgVWHzFyLL9MfdjZJdb7XXtfu1tyfPrqyAfj_6gqJRYIBSnvI68d04xw7rrSEtRKj5HoRgZyke_asuFk9dv0rQO3kFWOzIHphjwJvg-cK6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو منهدم کردن تونل های در علی‌الطاهر که اسرائیل منتشر کرده
انفجار این تونل باعث شده یک زلزله ۴‌.۱ ریشتری بیاد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83264" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83263">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=JqxqFsctHCDxmm56FMDohxNHyR050mcaP74Udys-yXEbWF2I2LEljmBi1gcPmPLl03xRABr1Wa8-GknbzAWde0Z_yiRnJJN9glSSRl6Wd6wJjEW6r1RdBRWmpwwPyIBSBT6c4YQ5c68inKO2iSGuFY0xAUKmCMFbl-Wpmy0Re5eYd9ZrVY3S3w8YKasHquA_qNXMXB9dMb8Ecmu4jsrxNsyME0dxhzLwZw4gZfLJL_27FnHCRCbSBpdr_yLvxRYZFPUAskSnPCZlvOntOOH2g8BTbDb93CA5Rt3WJTeN7pd1AG73zNjihm1bYjQSQa21ojRNrhH5OKrlDo5iL1bi_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=JqxqFsctHCDxmm56FMDohxNHyR050mcaP74Udys-yXEbWF2I2LEljmBi1gcPmPLl03xRABr1Wa8-GknbzAWde0Z_yiRnJJN9glSSRl6Wd6wJjEW6r1RdBRWmpwwPyIBSBT6c4YQ5c68inKO2iSGuFY0xAUKmCMFbl-Wpmy0Re5eYd9ZrVY3S3w8YKasHquA_qNXMXB9dMb8Ecmu4jsrxNsyME0dxhzLwZw4gZfLJL_27FnHCRCbSBpdr_yLvxRYZFPUAskSnPCZlvOntOOH2g8BTbDb93CA5Rt3WJTeN7pd1AG73zNjihm1bYjQSQa21ojRNrhH5OKrlDo5iL1bi_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی پایدار کی منحل میشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83263" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83262">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83262" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83261">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t38zEsk3KZ3_HNzRgVIZawRJXHRZQJYzH_nloCCWwqj8cbzlxs_7-IBY7RVjMaIrNaLBi0FOG9HJ29RE25eMt2A6IuBmSryLvnhAYSBorwFXaiuz5dgR2-bSGexF41zZQ5x3QVG7T-CAqwHLuBDUYXHQba2kHER-0e-wmTehVs3xjpLUJmIQD-XNfjKey3wvnGtGJTd109uMEGlM4DG99gIVQ5tlODznaHZdZjFtTL-f-bClDPilcRDQ6U99cJToh8xcseI0GzZTNJBhpLyURMtbgaQeNlmh2ibFGKZIhcR4qFzlpPlvfH6FgLAI4rCxfgxIIj0UpHa4PsHfD4eJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r20
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83261" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83260">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امروز سالگرد حادثه ۱۱ سپتامبره، یه دژاوومون نشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83260" target="_blank">📅 09:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83259" target="_blank">📅 02:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83258">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV6SftnHryJsX7ZoZaXTe2Bfo_vvEWcD2iw3o0YFV4RaCvzlYvhGI09XX81nOjgT85-FA6l_-d9cGiHNxp8b3qSfKgiEoPnjc8_m2x2kOzlYuh3czFGP3BWl8hXjgKrlvqJfYW1PHULb1XQkltztGpfArlyA632yZ0ZB5ffizVfcKqpq3z2kldusCpItLhVsHEgFz-ZyGTyHDdfNLpQPOa_ul0_fZfO4alQHBN-hwkPHanCQSDgJfhjNId9-Y5kJ_JniIuT_X8QnBIvWSpuyZhoTGf_63BzRwE0lN3iEzFrQ2g6YiKMLdtWbVqnO07Yjn7bUSVCj3cdEg7ycsK-GuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا اعلام کرد به دو نفتکش در ۷ کیلومتری عمان حمله شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83258" target="_blank">📅 00:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83257">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شاهین نجفی الان برا زید جدیدش آهنگ عاشقانه هاشو میفرسته میگه لیلی بهونه بود اینارو برا تو خوندم، درحالی که اون موقع این اصلا بدنیا نیومده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83257" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83256">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8aC-amFYIDVQhiPChZrz31xyx6re_2KMNBOPK5h0OTyshohgsdiK619lfSrTd5yuDhbl5sk4IQd3E_uve95nZ1z6Q3_McWboiYQYzovFIKhNxaf80ORydXaL35la_BbfQuzcSY2XcDZUDJeCOP2hKS1x6AXJikazlnEYvzIXbf3iDwCchIqjz5LYE6y0GkTCNE71WdC9C-GLbTubIxf8cr9K6mYC-3I_nQBUEl30LiWHMLI9F1BW3mAEJmV-eP1bD0WuXks667YwJ8_Ms8Z37KyktFQU_zeiWYuaSeIJfKDyjh8cl25kNCz794wyqlltqCjiauGAQhL3okj6PHOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا یه باند میپیچه دور دستاش، با اون ۶۶ میلیون تهش اونو بدن بهتون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83256" target="_blank">📅 22:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83255">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=RSf1Qo1Y2Xp0SZJZGtC64wsjvyRcaFQThu1UTkpXK6tprVtDFuh1A69bJQM30mWrio3jONHOUxV4bbNgOSefADWc97848VMyOQmVNW-8q8l6DG6tZZf3m5_L7cX5TKTXABFo-jAo7FjZS-as27V5yBF756bazJCppPbnFV6vDLe1IcZuyhI7rxMaje9H2N7CeHe-FYk0NydpPp3rTriihL_Oio3z1eI-xUHX9URn8-x09i_QfQgu1g3LGNM5V-EitCG330gWMAlieumf53L6E3pAz7wsyyi0L9JZTmwGZkcH4eIhmnxZSczrqf4EDC3W8CHL3w6vLIRXrGj0InhKiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=RSf1Qo1Y2Xp0SZJZGtC64wsjvyRcaFQThu1UTkpXK6tprVtDFuh1A69bJQM30mWrio3jONHOUxV4bbNgOSefADWc97848VMyOQmVNW-8q8l6DG6tZZf3m5_L7cX5TKTXABFo-jAo7FjZS-as27V5yBF756bazJCppPbnFV6vDLe1IcZuyhI7rxMaje9H2N7CeHe-FYk0NydpPp3rTriihL_Oio3z1eI-xUHX9URn8-x09i_QfQgu1g3LGNM5V-EitCG330gWMAlieumf53L6E3pAz7wsyyi0L9JZTmwGZkcH4eIhmnxZSczrqf4EDC3W8CHL3w6vLIRXrGj0InhKiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو انهدام پایگاه عماد ۴ حزب الله در تپه علی الطاهر توسط ارتش اسرائیل
پایگاه عماد ۴ بزرگ ترین پایگاه گروه حزب الله بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83255" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83254">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83254" target="_blank">📅 22:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83253">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=D8ktcMDPy261-cXKRrUo3NVubdxRSOEdjqWwXf2QQWBhu5SR9iudiPVRBe3IChDAg-52bvmBf7uXxemGkovWnlCVUGr95_SLesym3YNg4cch6FwR_eTgAS7f5tki4gXHqnR94ZX9TUXyKi6MwJTElFW6GFOp8VkpwEj16pFyDvzsMuRVcXQdnthk3HGn2iglMdfWiiICjcdVzWvZGi9MCyzLu_luRKbu8Bo0VgJJH9zAVYBxI_WUcLao6WLF2jqixYCokYKhovvTbrXSgz_YfEUa2EJcRSFqBBmRTWyhU1OB388NdUPFtnXHTdvKckm_LT2Td7_1v6hxbSVBm_Fndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=D8ktcMDPy261-cXKRrUo3NVubdxRSOEdjqWwXf2QQWBhu5SR9iudiPVRBe3IChDAg-52bvmBf7uXxemGkovWnlCVUGr95_SLesym3YNg4cch6FwR_eTgAS7f5tki4gXHqnR94ZX9TUXyKi6MwJTElFW6GFOp8VkpwEj16pFyDvzsMuRVcXQdnthk3HGn2iglMdfWiiICjcdVzWvZGi9MCyzLu_luRKbu8Bo0VgJJH9zAVYBxI_WUcLao6WLF2jqixYCokYKhovvTbrXSgz_YfEUa2EJcRSFqBBmRTWyhU1OB388NdUPFtnXHTdvKckm_LT2Td7_1v6hxbSVBm_Fndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83253" target="_blank">📅 21:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83252">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW6IC2hFKuTyNBkF3cokS0cFCqPNqKA0K6ZOW93nYen7TwuCzKCrWGwVvFSuStbd3_hXQQ_n8I6m1Gvj1vyb3vFVrIC7PmlP8H1v9i0uqDAkoZL2MJ-xTr5RO4Jw5Yh0Fhq0R7hEArZ-8AGLMmYQAXRXE2Qo6S44FcUQlsMBeyx2H5_okp2YHrV-ooufkaayPlXAjCgjUBQwaB4gNZ4w7WMhIHFlfHgv2x86yXAvJD5veM20K7AVehJ_gxPOVY3zHF_1q5SC-EOJMvFhv3HWFowrCgbi_2EFC1mc8cJVEOXjNZGXE_biv2mtMAaGNl4b4nIb4-4rfmXVWC1-OwzRWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصخل که اشتباه جمع و تفریق کرده ولی جدای این ۲۶ تا میمونه، یه تورکم بوده گیشنیزارو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83252" target="_blank">📅 21:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83251">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXc_PvOX4JdexbhnBN_yTkQllbqQ6hO1jQLcBCHvp7EqKJQRTzU-oZqtFNttVVEfAG1WuLZILw-_W26icyJ4QpCEBl6UFj5TSHYzVzY0PoqXttVK-QNtHgUIID8sUoLBNH1BYa_pQKjMA7uGWq9DWmxfXv_1mITW1PsP_708ZD-f4A8ORyW6xpYzFLPuQG476Z1kg2ZPah62V1CK33BQ7mLmYsEOCkc2z3MDIsgoLU-Z2TjYqr8Eespp9sQUvtrKV4tpAU4DSzCqNj8rGxiVmAtKI9LuI3UyG_pMe7pFrBur9avAvRgv6BvhuIsOBF1HmY8b-TXLZTw8in65V8KWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا مهراد هیدن که با اعضای گروهش فرق داره و بحثش جداست اومده ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83251" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83249">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aco7UZ5SfMKJI0QD-ZUmtLtsidENsSqMQYrwu16GQxPLGaP6V6BeDGuoFyXd4UoPRcCBr9y2Py1xNaEVNrfgPecABJMcoZPJu7Q8c-fGotIujxtvKc4U1EOsWjE0NQL-UwFm743-VlyKksns-neNvOxIxjflv-cDA4DHXUTK0gqPZXsI1dH_Q8N8O1mRgAj98eXNuGad8yGm7N2wNS-ovEAFnXUVYIB-OuwONWjmcE3_W_1ryJCFxYCXYY1Ao0tMAYo4pjwJzItKUOuQeLMDQGoP57_wDX23O78GhtsXD0sH43uvi98O80HnHgqQ-9lFtihUSrBQ05TjcMxGlg63Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVCdXdVmSNBXSqWlSheSuOQWbMGQWFHVJkKuldDrvdKUFh9wDzS8Pnwo7Bi-B7yCGcSRK3D37btus5zhmNH_TiUFXX15ov53aP8gAIpgR9Im-xR5pXuc5HN-n3EHpv7k3iTHo2MO7BGJ-lZGAnZ9VrHx8XX3h9sUXgediYobVS4GBjpDRH1wmZWHd1EJ2gZCsV_oHsiLs1vUY5a_R0aKuzv1G3mCoeZJKJi5iQBZKuNvB-1j3HjBMDW_vnHYITV7ndOnsSsq34tb9-6MWyWTCyNDZelAxjZxtxmADVctgb8QxvPM5eqjNPtyNXeyG-9dAgkNQ3LmMy4zOJvZi4oX-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آدیداس با انیمیشن ماشین ها همکاری کرده و کفش با طرح مک کویین و ماتر داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83249" target="_blank">📅 19:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83248">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgihR6rguZj9hoh-rCUBPwVWCGgHvtU4s-5oJ1GIfZOqAsbhEvA-xwtr6CG4uTll6fO_ByGQ1YkGQ1sgvHpr6YiCzMAt2HFChT6FUfWxWge3WqZ0-9gY4c-Su1RZ7xwx8uK1O0YyYYgNc4ggDmL8qgSUc_tUQ-J9rNqL_q5c0YApmvQ3IGfabnnlT3fC_MB6Cq4ZWDNwb0sZ4TWmLAflnLb_089wtflqwcR4hikjusYxAX8ZqPv81edGzmftBaCL2dBSGAPTc8ID0XTzvL3_MDaLyJ-MLpVf_4jB0Sd9mE7iKfHHivEzHozyC_ZVg8pwvSmktHA0VxZoOQ4IpVooAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم دیگه بگذره عکس کیر مهدیارم لیک میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83248" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlkfkQFbjuquBWXvZuUa9HumF65PzkBWT4zYmuRpxaykXL2xF1z54q_p8SNPuDpLY6feHsyssWNc5aLZXh53KIwwQY3IhgJjwcSPfcEyixH7rNtwm49KfNj2jQq15VtPa8O0mkuxDoE9fT4joRY5exV2Xw9N6BGetrgsdap4dHc5rHnpwThRnbHfIR1ege_MvAp4tElV6OgZsOw2gtuYLIVZwbrkl_AAGHHbRhM2W20E54LECIXlCjvPVtDeB-geyXk5V1Sbq4J1IFM6u6kF8ERoql0bL6CbFXpjQa4Eso3ZF1KPkPUqwsHQ0PU4pI1tK5g2Kq368LrOqwhaPTlLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین مهاجم نوکای تاریخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83246" target="_blank">📅 17:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خلوت کنید آقای خمسه اومده</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83245" target="_blank">📅 17:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roohiS6jxqMBejNLfUBkOP6KfSNLMY_9YkMkSNebOkPbwyLpt7jlzrxhSu4NFyo6CFLtIXXsbwuCrvVPFD94zdKoVm2tO0xr06hRZj5U_pDoKla2V6pTmob2IdlJL0Hdfy9hRpt--h-YjX0ScgSJjURJUZCAaWU2Co5O8YA7LAYeub6oXWfrQuFhtn19RJtyMCLN1BdIxjDgkHA6PeNlJPFdmoU3TAD-VP43ipiu0lidUHCZfwMy2Bl2WeK8arEYRXA8MIU04GxixWCYPOaT983Pvd8XrtCyxW8hT84T1yXutF3XezsewbyZikoJDAcQfeMYtWuBTvqmKdeQHmuhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب رپفارسی اینه که کسی که به داداش حسین تی ام میشناسنش به سجاد شاهی میگه فید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83244" target="_blank">📅 16:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=j4A8bL1erkVZAQ_V75cA9tf68Hk5ImPs_0V_5Iv8UT1TNVYkSxbtsKLBa1YDAatR-tCn8sTNzRx1I4vlLEE0KuYSSxpXZW-iOS5KvD5RoP44i-dlst6DhcJBbzeO1tDI6b9GRFZ5Rc4Wu9NoMbsCE-5Ud7yObL3MGq8b9cQv32ZbDKajRN5YJPhiVjohXIkQNOtc5p3E3gs7RFO4mbUMv1t29YTFDayNf3sKreOwnaFvGoRYxomuGfmDo4VNzGED3AvGteACy1wjrvdfkKDqeXT-3JiNrZA6koxNkRvzPcLC8LxEP_jzqkoQAfCCZBy3SJIY90y6tsRZ4tLVidCkyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=j4A8bL1erkVZAQ_V75cA9tf68Hk5ImPs_0V_5Iv8UT1TNVYkSxbtsKLBa1YDAatR-tCn8sTNzRx1I4vlLEE0KuYSSxpXZW-iOS5KvD5RoP44i-dlst6DhcJBbzeO1tDI6b9GRFZ5Rc4Wu9NoMbsCE-5Ud7yObL3MGq8b9cQv32ZbDKajRN5YJPhiVjohXIkQNOtc5p3E3gs7RFO4mbUMv1t29YTFDayNf3sKreOwnaFvGoRYxomuGfmDo4VNzGED3AvGteACy1wjrvdfkKDqeXT-3JiNrZA6koxNkRvzPcLC8LxEP_jzqkoQAfCCZBy3SJIY90y6tsRZ4tLVidCkyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83240" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ولی خب طبیعتاً هیچوقت کسی که برا پول میجنگه نمیتونه حریف کسی برا اعتقاد میجنگه بشه، اسرائیلم سر همین جلو اینا دووم اورده و خیلیاشونو نابود کرده، چون اونام اعتقاد خودشونو دارن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83239" target="_blank">📅 14:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مگه نمیگقتید حوثی ها دارن بگا میرن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83238" target="_blank">📅 14:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انصار الله و حوثی های یمن به نیروهای تحت حمایت عربستان و امارات کیر زدن و درحال پیشروی ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83237" target="_blank">📅 14:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83236">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZt8Keq4X_60eo0jItMY8NTWGwAJd0jtXSPv3Rv30DsvUOx5KVwuiOsgu9hoCThrtd9zUGNUOrdWqiDu3XrOiB8K2__McMQ2Pdda7q4mQOrbgh3u9GdPg3E2rKQngjh0tlBlbK0bRyGPD2cNtdMxI9KKzhhmZIZyUT14f2ERLC5SaQHvud8cm4Sz0P-tx6ZQDaFk0k9lL_Fcaqd5V9FSiHzCsJquWW1JlvD_6xL6eTsLQXM2YkES4ceBCSndDjlhGhOcnkWLYSCAgGSVpk_9XdQ0uPk398etShP5hpquSHyHGI57aymIjmu4_JKmG0WIJrVp-ZHyI8d3t0kMad4uog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم نظرم عوض شد ولی همچنان لیلی بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83236" target="_blank">📅 14:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scB8nR93xXpDiMgIRkTO_XMBLUlv7NkEsQO731mhGY9fl6ed34F2uzdhoocxfVO3D38R3c-Khn-trKidRt2JZmlgE2mJhUAfekXgStnKfGS_EYN7tCPalBQx9Ro9g5hPficyQEjGADxtDpQk_M6KtgUuuLz5pRv9caF6PxM4c1ebQasG7bnurD18uuxdqGXz6iQKAcqCLV1LXM4RMcPvzmljCYLIl0lW93erh4fB_1ebEyp310RzJfB7-wMkotarU8ZRcAx38jQNbtB22Lcw8Zwo2QCh_f0_VHkxRk08Zl1QmnfPOEiFmrAFeIUCjy9T4zipEIhVqLf9Qjfbnh4_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-zcTagtiyxfUsIeTDC6dFK6xHsLLFHEGS0nTQGXs6B2t4hsHzcSzWtla1Y3tuCjeumCVpmZokmsPnFhKPPaJ83dUlFAiZpXjIlGYR2vuC-0044BaozoWdulNyyaxraLCAXOrSxS99Sl9szX7O-L4xjGvVhTnZckz7e2F-8ETEm9bWuQD6k2MzbsGm2PMTG6HhQMQ0Iy-h7WAwDTorK6-KMiQyY2BVdT6LrXi1_U9ue76fp5r7EPQFCzXszf2i5XC7KZhXkwk7Jc2j2vcIbXsfvkXyh56CgMphGH7FxoNNI8Wqeyao-C4whxO1JkBP_OKG1gabOC6kd_EqNT1PU86Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لیلی بازرگان بدون دست و پا اینو میزنه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83234" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الان لیلی بازرگان میاد توییت میزنه این کار شاهین نجفی رو به شاهزاده اطلاع دادم و منتظرم باهاش برخورد کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83233" target="_blank">📅 13:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83232" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83228">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkzQozmj6gYWPFTVarbCj5rX9asELJs54pw0eL04bbXJPFjHYKRCcxFpXLlUz75W5F2OIGo70qlP_oxcH2ozdSuz3Psarrc5i9Z6FslrAjTSQDFvb1g7CJKPKj0iyBblGytb7gq3T_lRIszJIbfJEwt2Pb_bvXdOARpAm3Te1w3BGLoMhtEhxbSMt1GDmDLz9JokFy6kyhXDIR1fCjrZ3Ovf7Jj0pfqE1-INIplPO92f91kA0mmiLKY-T-MDn-IY2Wb5Wrx-g-wVW4rF2TcYjhJDbDNaICzGD55WM-p6xbFY7tnvs6YWb6k9jOSn3SUkl97QbkTSasXAFjz8lkR-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dx-vrPX5CHsj_AFVvdyWNYqELI5bgWyRTrPKjORp2z0iQ7qS4v1sJkauPonLh8SpZ0NoO8YybQrk798JHl2izqyQTqgObKLAWnBq1VcKuNkb4QiTzfIG4_FAAZCM6ZvCufRioF2u2Lt5kOvblpsfdqGEoSIvBtje-jXrrWWypDC8SpQ2uhQkUrRQCowZcLizMJx6qK5JDbYt2-JAIA4JQgF0C-TivxMiyMTPrI54A6f6jgprg9giudlsDGjbn6mMKfOipgGl11o57HqLrCg7v6IQuUDiZBLnC2HRbz04SYEziP63nwRRrxItpCeipGTzOV3O3T2uTyJve8xfCirW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxaGxLera3LzKTiKdVPlBYW9XmlV39JWro_AmRXWQD3Hhop-UHiig5mrfX8VRmzXFUphB4nV5jdEuZ68eUCIhocTBB1vuKPrDjJRhErNKMjlXfholGj076TXdgEtpfTmlSeXxbnLJzsriKsKQ9E4B8ehAWCjgem0SJL8iZZvxh_Mw1_sd0MEgAmbeVqJ2DTHRTWOvaelBwTamhDpPwhDH0tMGi7aFB9gzGhyBDggrvRUWjrlIA1wBpwIIAEMfrWpPPlhWa8pXZxYOxj0er1j8Ngf5pthuk4FG7M9dJLqRwq2NOoSp8ZJevYCqYE0O5sbMuAnPLMjx8MsUm6NVhbuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2hdefW74_TQWE0VjsYhoGvDwjxWoASh17-7QR_E196ZcSEf4vRlNHwso33Cy5kYwQU-ACeNfPdKlGfStpTqLhe7LEMAtb2TENx6hkzE9Z5dD6REV3pkCkHipDeWe2buG4S2i_An-uJ3U11Sfh9E7k4sXfp7xPJs8jfmY05k_y1a4A2LEIJYThEvR43hGV3BBlnY4_EE3iB3o00DI1qI6YkaAX_FSYVW_urgQZGrRCCKZai-SH-Xld1FVoChD-RqlJ9KKAlPOARCdnSESJlGrt3SN5ui6PCJHJKKFCfkTP8PWrEXQjM_sD91CaSUvAsSxRYapER8hVL_eGaw9pKyxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83228" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83227">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83227" target="_blank">📅 13:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83226">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83226" target="_blank">📅 12:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83225">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الان دیگه هرکی عقل داره از قبل داشته</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83225" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83224">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzutBcyseVGM9VqNmCxnoam2DEoQlcS9n6yuGCUu6UaJ398biI6exWJUgmbKcjk5XmQY2TetF6d3F3eykumcfc6dxKR4Pstci7tNAR-thb5seV3j_z117yYltLvN6U5Uex2mNiufI-ybVu1PDgRQM3peYCo8S73arJpjq06y1d1pBJu6H-1yb0ENIXebDx1-AHXBY05OM5Fvy-Bp8NVPTwgUwlwMnxxlSUTueJA2IMuwmyC67n7sqtPPXA_2ywgoL6hOm_osLAi5arITI4kvi7014DfFeB8sqWjl1WVMGYNNvqJdQXvfrmVuPZbH_TfYCu3udFr2COq1PelaFBNjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید جوانمرد، افسر معترض ارتش، به ۸ سال حبس محکوم شد
جوانمرد، اهل الشتر در استان لرستان، پس از حضور در اعتراضات سراسری ۱۴۰۱ از ارتش اخراج شد و در پرونده‌ای مرتبط با فعالیت‌ها و مواضعش به سه سال زندان محکوم شد.
بر اساس این گزارش، جوانمرد که در مرخصی زندان به سر می‌برد، ۱۹ دی ۱۴۰۴ در منزلش بازداشت شد و در پرونده‌ای جدید با اتهام‌های «همکاری با دول متخاصم»، «اخلال در نظم» و «اقدام علیه امنیت ملی» به پنج سال  دیگر حبس محکوم شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83224" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83223">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7-_nhOupBxjCSoLk4zZSrffaaNrJLZil8vT-BrbNojAwu1ag9kypkcWeYnbyV4sjBtMcnBfVk9mlcdJv2kE34kmrg-bw10r8bCjGhLofMDMioSBRV2JHq4T4_nRwobhEzc_cwrG7n1vCyG15p4TBgwoSsAGjvZzunBmy7xOMrrfQIZ4COoaSC82ucKPcfniEL-k4y3n7Fe0eC08BcVB6AcAYur1vAxivCqXKqJIgzgDzZVbAYilnkgsKncPPknevXYYCpPklZVlhsbRfEOgSvoIXrHMFpa-jGpwhy2yf_-c0huNcJylSjFGV_BeXR1FohTW74mbDfwmsMTpXih_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا به خدا این کار همه جای دنیا رای خریدن حساب میشه، این آمریکا دیگه زیادی دموکراسی داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83223" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83221">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ:
ما شاهد فعالیت‌های مشکوک در کوه کلنگ هستیم، به آنها هشدار می‌دهم دست بردارند وگرنه مجبور به اقدام خواهیم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83221" target="_blank">📅 10:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83220">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFSv5u-SELviOfZkY1RKHLDa8t6szleR2apgT7cazT3G7UzLu1wNRN2zCG_GWDfhc6tHKE-ChuNuR8LfIYpwaGGNcXQkvzIQUwSn4n8Uc5xrJjB_iuP30jpzdj7581cPreaaQphOQ1Y1TjXN14QAr5iRpPIcKiDg90aXCK2Mvf-ynevYJN0j4GkN5W5I6byx9CzRhgEFB9B-MGRqQq-KZOMKkC6sTBn561XFfOp5YkyqEurzOkYLCGbTbmx2Q5cnE_aQQ71kGWUCo9jK2GrRaK20PQDMcndCNyAJ1ne7BOAp7bNthrjY_ho7ZexjZHGbBYlMAQ1XR8tZURVVtjb5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون متن ریز اون وسط رو من اضافه نکردم، خود عقب مونده‌ش فکر کرده خیلی خنده داره.
ولی به هرحال اینچیزا مهم نیست که، دوباره صبح زیباتون بخیر
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83220" target="_blank">📅 10:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83219">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=RzgC7uZ8Hm0ADbuzK4_Uq0BuIbXwYXgtNX9f03hY7Xl5qpOYZCie1UDYlH2z3HFdodTHKQJy_ER_JhD_a9SdTd0juJNRgwU1mkA8_ENPhK6s5Xd8p4xMIh-0l-9LCaggOA5lJPQPdK_OLobuhFpa0wNWAyxfk953LqF6IaXMHTLlBKv_rz8Q7szSR9Y8p0SnSzx22Wxk1pW1W-t2FLUKO268OCsn1zJgoYeEuAFHWwDouZjn_KhiaCP5H1kK4PDegX9IbHjhub5FBFmHEJf5Wkt0SIJCJcFbb91ou_4PTasC4GRxLBXlXKBcvvEgED-p7NA6_2n-Wkgv2Vulbe678A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=RzgC7uZ8Hm0ADbuzK4_Uq0BuIbXwYXgtNX9f03hY7Xl5qpOYZCie1UDYlH2z3HFdodTHKQJy_ER_JhD_a9SdTd0juJNRgwU1mkA8_ENPhK6s5Xd8p4xMIh-0l-9LCaggOA5lJPQPdK_OLobuhFpa0wNWAyxfk953LqF6IaXMHTLlBKv_rz8Q7szSR9Y8p0SnSzx22Wxk1pW1W-t2FLUKO268OCsn1zJgoYeEuAFHWwDouZjn_KhiaCP5H1kK4PDegX9IbHjhub5FBFmHEJf5Wkt0SIJCJcFbb91ou_4PTasC4GRxLBXlXKBcvvEgED-p7NA6_2n-Wkgv2Vulbe678A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا اعلام کرده فیلم سینمایی نجات خلبان آمریکایی در خاک ایران هم دستور ساختشو صادر کردن و بزودی وارد پرده سینما میشه.
بزودی مردم آمریکا تو سینما:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83219" target="_blank">📅 09:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83218">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=d35-JZIy26EyXZ1Rw7Q-__ox3G1igNBZLF675afZg5YVA2Z7POzoBsVKNFjzmrm0geSH9U3cjCGmvANf5dIp5pifCfTy-5Hv0Pwqf1COPeD28Hwr7HqUNbOY5vq48cZjgF4eAEUJ0ZZQJ_nBmgVXvyXtcFx08s7hYSYkAc6r55YbPAl2Ha1xKJaDNE0AobXIL-YfTMYwEbIVAIQCNEYFzpTe8hNTQN0NuywydylhEuE4ECP74N7H1teUqTBPsR6rOC_Z6R009vK7HIN5lIybScVWSJA0MbJiyIu3KsN-5BPVYr_JufhpQnLOfbPxyT1er7Tcmld7iBgHNs4wuuvG3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=d35-JZIy26EyXZ1Rw7Q-__ox3G1igNBZLF675afZg5YVA2Z7POzoBsVKNFjzmrm0geSH9U3cjCGmvANf5dIp5pifCfTy-5Hv0Pwqf1COPeD28Hwr7HqUNbOY5vq48cZjgF4eAEUJ0ZZQJ_nBmgVXvyXtcFx08s7hYSYkAc6r55YbPAl2Ha1xKJaDNE0AobXIL-YfTMYwEbIVAIQCNEYFzpTe8hNTQN0NuywydylhEuE4ECP74N7H1teUqTBPsR6rOC_Z6R009vK7HIN5lIybScVWSJA0MbJiyIu3KsN-5BPVYr_JufhpQnLOfbPxyT1er7Tcmld7iBgHNs4wuuvG3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون با تیک‌تاک فارسی بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83218" target="_blank">📅 08:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83217">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قرمه سبزی جا افتاده از نظر پسرا و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83217" target="_blank">📅 02:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83216">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۸ ماه گذشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83216" target="_blank">📅 00:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83214">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYrutHWV7B-p07Pcz1CXFG4VI-A1CI06YpMmIu6ocPch5VO9kQJ4hKM2gcB6szYm982S38oSYrLPAddtfmBA9v19ZLaS9OL9Zrz6DRGyUNfx1WS3xibgUTMlbBbNFIor_kDy69SkeVPYtjzXWNsNmKnys-FTKB6mnrmC77BRFw2bhTkHiSeNOJmyKrHzgTRruFC1b3AW5wlvfgmKmzCZJsOoK0p6g-mtEbeduvkrMq8x4IdXd9lxLf0MGfYIwQnXw3RdbFhsBPVvq4wsOP53QOQE3fyAxuWL7WM4DXeB74BvTF8F4C6FphFkAXExdvHS78MbyneqEibsSPWHmXCYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ln8vipwJs224OaeeN-DQPIM-OSC2UR2kkEi8bop4Yk4ffs6QFiBZ_vPbdgwOvxvhA7GlayWMNVjWt8GgFNgt4GievlR-FWI9iUiuKKVQb9IHVoDQ5MsX3cLwXG9ps35KZwP0xit3tLY7xqj89954kbPrNBNLXa7qRubABABD1CGsrK6fN5S1ys48pfftcdA8aNbfrNXJjkOuuwmS5Qbax1GqosxkFM3Hwh1p_VMM81xNqf7WVFq3SrWA88rRGoj2PiJpms2Uz5aX2gxMxbSdzngbY7QKZC6k5qVXwSygHMalkjZ30ypUuC9mhMAIffiDJff_NZqtAQuAp_x-F3qFqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت بت زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83214" target="_blank">📅 22:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83213">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhxvlvoZuSfarU10QhnqAtkaZA32uM6yptP2QFGcX3-HQpavoZ8kjHTExgkF__WeMC2mXgfOYy_i7l4o-VEsC1B_0aGiSOS8Q-sGUo3I--4C7Nt2a4Qah16ITHB2JB9wRsQ7KbdlmwxHFISgdscYpVPyplMuSBBAjrxlQxGs6H-WqoyZpomvgBE6Pej07QVWRpheyOOm9khYuhdOzqNM_92kLVWoyb-fDjcYoLyjdUs-49KZZbAO5f9Czhb7xMOV8T3ufsDT_5JBNR4LH8FmJ6g8KCoLTirClOSI36SkYpjJR0dL-K9cr3in4bRWVFDjBGs3mf6_tCbWxB_7-A6aGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احساس میکنم بارسا منظوری داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83213" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83212">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orfNP1IYm_G_2068yOnnIfaO02pX0WeoiSVjd3d6Yi2I_F4_eWmViJVP_HoQH59uL72dk_0w08ooA-Gm1Li0iyRNPnR5wRPvbx_o_DcSkcSjHt1OH81pth-PVuL22FNcasdPt9U6QUIwbqdhDHHFTSB_at5lWtqDV3WP-OwGDm5uPhs8kjSgDMJAuOtvpkW4uX9jWtd3vRjxQ0wL9wAZ-YZhYtFklV_2xORIo41BhtHIxHnQOzGdY0PHQgZ8UCub3D8XnX7bhafgOkLVqbWZ9ck6vVqgKnxW1-CiW747IGx41Dci4HhIWZtEfDnmEI3isAKgbPZw8rR4wNIXYNbN3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظ
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83212" target="_blank">📅 20:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83211">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کریم سوسکه چی موشکی ول داد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83211" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83210">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">میثاقی وقتی خداداد تو پخش زنده از کلمه های "کصخل و کصکش" استفاده میکرد میخندید، الان اومده میگه کار خداداد زشت بود نباید فحش میداد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83210" target="_blank">📅 19:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83209">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=qe4dcm848HxHZ2RtEyGet49Dr4V-uoeVoYiD9W-oy0g8HEqvZeQIZOfbsVnqU0fNmk4s-lHkaA-XgFv_-OQWQe5sXg-9WUxCzt30sBD865cEJLzQ_BlVFX2DNo1CwHl4jxR9CDFoi3liqrqxrCUycoD67SeAefj3Ig8s1pm_zLA5L_NElIbv9ZPYTGmuLLg_5djWlv-HPq_MMVEcO98_HNxrrR2IY4rYG6SYzOneat2XXuuuVRZ1XXpMMyfYneFxPxYquUupANte4wHJwR0n3pSSLToEpuW8QViczwqPP8pr39pl2mBGYDWsN9EamCWJQwwKiusv2BNVcwuBmGd6qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=qe4dcm848HxHZ2RtEyGet49Dr4V-uoeVoYiD9W-oy0g8HEqvZeQIZOfbsVnqU0fNmk4s-lHkaA-XgFv_-OQWQe5sXg-9WUxCzt30sBD865cEJLzQ_BlVFX2DNo1CwHl4jxR9CDFoi3liqrqxrCUycoD67SeAefj3Ig8s1pm_zLA5L_NElIbv9ZPYTGmuLLg_5djWlv-HPq_MMVEcO98_HNxrrR2IY4rYG6SYzOneat2XXuuuVRZ1XXpMMyfYneFxPxYquUupANte4wHJwR0n3pSSLToEpuW8QViczwqPP8pr39pl2mBGYDWsN9EamCWJQwwKiusv2BNVcwuBmGd6qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ سیدنی سوئینی برا یه سایت شرط‌بندی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83209" target="_blank">📅 19:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83208">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=KWtckhFhWvolqKx7Px9uchN2-HvAlIZ6xquylxF9vTzKblGh4VVkTN2pMYkutbxTTluW1PtwThGPPA885ZeDnLh53uuzBGwA4u8BCkKKO1rFqDgZVW47YlZkicgrUocep7LwlqKLCX_FAunqXK_CKYgwjwo7fnMmFP9dtRJtQQj0fRzq1XYMyRjy7GENcqECvsDThig0NCyp9cW6ikOnYBDJlQ20Pc_ZuOn8kQFNSZStcP1Pi863Vn4qr3256tJ5c_8riKNUyPqwp7-o1Q3rEzyJSHaW8I3yDvltEAIWMvKfhgF7-iEuUXp4kjjLCBeBBgE1GZsrWnbYwQQqF5CVpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=KWtckhFhWvolqKx7Px9uchN2-HvAlIZ6xquylxF9vTzKblGh4VVkTN2pMYkutbxTTluW1PtwThGPPA885ZeDnLh53uuzBGwA4u8BCkKKO1rFqDgZVW47YlZkicgrUocep7LwlqKLCX_FAunqXK_CKYgwjwo7fnMmFP9dtRJtQQj0fRzq1XYMyRjy7GENcqECvsDThig0NCyp9cW6ikOnYBDJlQ20Pc_ZuOn8kQFNSZStcP1Pi863Vn4qr3256tJ5c_8riKNUyPqwp7-o1Q3rEzyJSHaW8I3yDvltEAIWMvKfhgF7-iEuUXp4kjjLCBeBBgE1GZsrWnbYwQQqF5CVpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83208" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83206">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K29NeZ6Q1LWS8c66yajvjFl8THbu7BiXLVzTdtwWNXuNvdhRZiO0q4ewAXvIFUxhMRZSY6noOA37yy842zJdTZQj3bfkGIvFwd-X81jI50EDeevVGgAF07_-DRwbCCJxeaMEHfYvXJIn0j_k_1RTG_umSnk1i3cHZiqXC6BDGFlORFsY8SZdMLMuBjoaJMMhNfVmGgJyL_uweE-xmG7gjFJNLzM_nGZuSTIWj7y_yEDfzNEijVfJn1yTgdLO4447nWnamD0G_Z2KCvWf1Z79gQlhaY_6jj7Qe1cD0VZkLTxdinvqQmFmeJLSPFGDEX3vxl6P8zGLGBZCz5MioeXlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت هرگونه تحقیق، بنده‌ی حقیر به هیچ عنوان هیچگونه ارتباطی با عوامل این کانال و به خصوص این محتوا نداشته و ندارم و به صورت اجباری و تصادفی و به دلیل کمبود محتوا، در این کانال ادمین شده و دست به انتشار غیرعمدی و ناگهانی این توییت زده‌ام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83206" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83205">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مثکه پاکستان میخواد پیمان مکه رو فعال کنه و حوثیا رو بزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83205" target="_blank">📅 18:14 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
