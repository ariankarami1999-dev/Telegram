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
<img src="https://cdn4.telesco.pe/file/LzdhB48oBpMjxN6B4EdYKP32pXm30BffwhVGyWPTkUrddRkDOdP8fJhRnNy6ewifG5UIBn-g4A-V5R9PdewiBbGXxSx1sZLxlLjnhCewKOu_ovA67BvpR3nyzkdPyfYlnS5f9MNVJPA12Nx0TbxKDyCVpMSCtSiqhSGmKiJh7J24Ffj3-sAqgWlSMGdjLtCZI2eb9y7z5Cw-vLbKlwebex5KXt0jTvZvMkf_5aNO8x2mHOjX-X6s6_W4S_Rz2dasWhGd4UyQ1c4TcLuUst-5EpY2sFmI42bzYcw-jdEmGA4D0s_pb85nBo1E4ST4Pgzh_Bg5bliJ-vpe9WHrIFhSww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 08:49:22</div>
<hr>

<div class="tg-post" id="msg-82488">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54687295a.mp4?token=FPvczQpC9jA3pUYms3c2r9wcAzfEJJ-ANcZxfXtMETTW-UQIm_8AMOOpo2wuR78EWp2FYLKGiyWr4DgbRRad2O5JX-zoYdeBeqfv7HXmiI2Io35zNu-1UfIngz4TjEgZ9P49q4KPk3lryUIWxtEGY9EYIm7MAZRnAsKi9qyd37C862-pZtiikyBOa3AziigER7KCMJO3PG79BmlmZklxwk9nHIBjlhvquS1OyJE4Obtop2a89j0w7z0adwSHsMVY4PkhtXIGxo4S7XK8OnT-ZKk9J5otOSpC8vDOSN71_oaeTAu7Hx8HQRyBYlj34lzMtY5ktq8-hquB6O-ajtH8_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54687295a.mp4?token=FPvczQpC9jA3pUYms3c2r9wcAzfEJJ-ANcZxfXtMETTW-UQIm_8AMOOpo2wuR78EWp2FYLKGiyWr4DgbRRad2O5JX-zoYdeBeqfv7HXmiI2Io35zNu-1UfIngz4TjEgZ9P49q4KPk3lryUIWxtEGY9EYIm7MAZRnAsKi9qyd37C862-pZtiikyBOa3AziigER7KCMJO3PG79BmlmZklxwk9nHIBjlhvquS1OyJE4Obtop2a89j0w7z0adwSHsMVY4PkhtXIGxo4S7XK8OnT-ZKk9J5otOSpC8vDOSN71_oaeTAu7Hx8HQRyBYlj34lzMtY5ktq8-hquB6O-ajtH8_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاعدة الأسطول الخامس تحترق في البحرين</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/82488" target="_blank">📅 08:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏الديوان القطري يعلن وفاة الأمير السابق الشيخ حمد بن خليفة آل ثاني</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/naya_foriraq/82487" target="_blank">📅 08:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82486">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">المساعد الأمني لمحافظ لرستان الإيرانية: تعرض مدينة ويسيان لقصف من جانب العدو مرتين دون وقوع خسائر بشرية</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/naya_foriraq/82486" target="_blank">📅 08:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رشقة صاروخية  باتجاه قاعدة الجفير في المنامة</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/naya_foriraq/82485" target="_blank">📅 08:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82484">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات تهز البحرين الآن</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/naya_foriraq/82484" target="_blank">📅 08:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82483">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات تهز على السالم ومنطقة الميناء</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/naya_foriraq/82483" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82482">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/naya_foriraq/82482" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82481">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الكويت: نتعرض لهجوم جوي</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/naya_foriraq/82481" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82480">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الخارجية القطرية ندين الاعتداء الإيراني على الاردن  #مبلاش افتكر انا قلتلك مبلاش</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/naya_foriraq/82480" target="_blank">📅 08:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82479">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219677a09b.mp4?token=dNrqhrDpkyjcfUg_sdXJvfVwnlYusNzJZiKUOPGMnN6ayhc1Rwb-ovhjOzGgqY8JUmUVFBSIRnZ7UHsRot8KMTdBpwTZvGqNRY7cO_6u-b5DSSY62P9AEl9foTJUCnmNKC4s-AURBTSLdUEIvbFSDWpuWRd9M_1IqAK3ctflHnBM25ODDVihasicsxZb7-pr9Zv2kTgF_0X3BbgZAs_cYmobGCmHFb5aqIMwla36UIp3ocBhXBNVL6LZnR-aMzW8prDZzUcqbVa26ape0Yq6AWHjqec9excjn464gLPkiu9eFU3_GnoC5RhrJMS9n0c-PZMsTgfKIY9G1VX4Bjfeag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219677a09b.mp4?token=dNrqhrDpkyjcfUg_sdXJvfVwnlYusNzJZiKUOPGMnN6ayhc1Rwb-ovhjOzGgqY8JUmUVFBSIRnZ7UHsRot8KMTdBpwTZvGqNRY7cO_6u-b5DSSY62P9AEl9foTJUCnmNKC4s-AURBTSLdUEIvbFSDWpuWRd9M_1IqAK3ctflHnBM25ODDVihasicsxZb7-pr9Zv2kTgF_0X3BbgZAs_cYmobGCmHFb5aqIMwla36UIp3ocBhXBNVL6LZnR-aMzW8prDZzUcqbVa26ape0Yq6AWHjqec9excjn464gLPkiu9eFU3_GnoC5RhrJMS9n0c-PZMsTgfKIY9G1VX4Bjfeag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم جديد يدك البحرين</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/naya_foriraq/82479" target="_blank">📅 08:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82478">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a5922aca.mp4?token=T1qDRqkmdZJ-hmUELaSzu4ZzaEKuSBLCSPK2buAiQZVQ6ErO2dDQVgsg1T6OHj6x2JnHio8yZJ7fRQql47p6qbO8w1b84bUFadMKJoDHHo-AE1pqyzTgtGZLwfu7boZqSMuGUcyApFvSNgJtedriuMPVfCU_52__kL1O37fos2cIOwoHaLcQKhZIulntj02jRPhj8vRIvMBnlOPQ0fMmh4bTEpF6mZGt92AVj0D91P8OKRh2AnYwjqdNqJf_YdFWds2MvEu9AA2D4cGN7MGIvbEze-CbsccKVKOojQNOQy5wXKapR_lCY4k9-NI9Admccb3hoal9P0ZJ2Iq3_0LMVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a5922aca.mp4?token=T1qDRqkmdZJ-hmUELaSzu4ZzaEKuSBLCSPK2buAiQZVQ6ErO2dDQVgsg1T6OHj6x2JnHio8yZJ7fRQql47p6qbO8w1b84bUFadMKJoDHHo-AE1pqyzTgtGZLwfu7boZqSMuGUcyApFvSNgJtedriuMPVfCU_52__kL1O37fos2cIOwoHaLcQKhZIulntj02jRPhj8vRIvMBnlOPQ0fMmh4bTEpF6mZGt92AVj0D91P8OKRh2AnYwjqdNqJf_YdFWds2MvEu9AA2D4cGN7MGIvbEze-CbsccKVKOojQNOQy5wXKapR_lCY4k9-NI9Admccb3hoal9P0ZJ2Iq3_0LMVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم جديد يدك البحرين</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/naya_foriraq/82478" target="_blank">📅 08:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82477">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">هجوم جديد يدك البحرين</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/naya_foriraq/82477" target="_blank">📅 08:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82476">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
التدخلات الأمريكية لفتح ممر غير قانوني في مضيق هرمز تسببت في انعدام الأمن.</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/naya_foriraq/82476" target="_blank">📅 08:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvbKOb711V9JbVyaQKPl48r7O0bxmEwJJPWABMGP8QjCKmEfwo2pknUpjxxWx5NE39Ru2WUHJ40sBHpEvM64mkQnGFgW5HMl9sELhcrN7cGdH59CBKRGoKScVVlgiCEZsENfkMz4OjKC_zS9Nzl6Tk2J0KkJ4cs8ZIX71CT6CE8P4QPRWrtnLpYa8x477tKxMLOeyo9oBxWvaa7yhWEj8gWdbC_3WPjlYH33gPnoEc70smw3ir7IFcXNt3Klavpef6fjzMk8a3J7IKcOiG1jIi1mzydYwukd5Stlbru88rNQo0V5NToedPDbY7tzm3WBVL8JgR4ZwOGZL4eE8G--uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقر قيادة الاسطول الخامس الأمريكي في البحرين يحترق بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/naya_foriraq/82475" target="_blank">📅 08:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw6Jx_8mJ1ubd7qQBu2GAslyrmUqETqeMKWGNpNxbLvinhsCzIpFZhdp6jKkanmdLLwelRIxbGug8pIQPGwlyMSGhRdQjXEe_0MoMhu1ODE46AMlkyQO8XOHh0xP33DKVABcQLnr-aw8HJwydPr-2p1W0EZFnnAPBMSqJL-CRT14M8R-KDWLYrB6tS56FmwtUfnqXX-LH1olTPKDdiOIqMTK8lbgsbD81S1w6i1wZE3p4G9JubJ6LWi7n60Z93HOrpDuJB0ejA5ADxZg_agRofiTcFUzYytZleDfQ_meJmNBjPlimWZqopIYEssM7WLGe_EDgAFYuOO8e-5rzC1zNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
انتهى عهد الصفقات أحادية الجانب. لقد قلنا لكم: التزموا بكلمتكم أو ادفعوا الثمن. الواقع يطرق الأبواب.</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/82474" target="_blank">📅 07:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هجمات مستمرة على الدوحة القطرية وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/82473" target="_blank">📅 07:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=I3zNk6GR6MvxeU7X3YMinJLPl7rvMr4KZP-hduiAmwRnOCgyBVCQswWCzcZPSJ4AA5-qQd1nf_IA3y14P2nnla_xEom-vjY7FSzasHOK5tEgmYd_0dUOI-P_j5eSYYP6wHIh83WG0CVyAINgWBTnk2bwnXJlLBSIsRcBe9GjL66kGJYWCfJ-xgPLiPUWSmxAydRm4ukNZsCwMMwOBqE00g2yRIVNxoRp5R5nxOe2eKp-1TNCsejM4G2WkO-y9ykC2_tGjmQdAq8IuN69a5aUghBhuIz4I8ha_blVmrzYrF0frp8PNCu6UeOeid-QVBBhMQ-v-XPu_FNXQKML818_eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=I3zNk6GR6MvxeU7X3YMinJLPl7rvMr4KZP-hduiAmwRnOCgyBVCQswWCzcZPSJ4AA5-qQd1nf_IA3y14P2nnla_xEom-vjY7FSzasHOK5tEgmYd_0dUOI-P_j5eSYYP6wHIh83WG0CVyAINgWBTnk2bwnXJlLBSIsRcBe9GjL66kGJYWCfJ-xgPLiPUWSmxAydRm4ukNZsCwMMwOBqE00g2yRIVNxoRp5R5nxOe2eKp-1TNCsejM4G2WkO-y9ykC2_tGjmQdAq8IuN69a5aUghBhuIz4I8ha_blVmrzYrF0frp8PNCu6UeOeid-QVBBhMQ-v-XPu_FNXQKML818_eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الدوحة</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/82472" target="_blank">📅 07:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">امشب پایگاه‌های دشمن در منطقه شخم زده خواهند شد</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/82471" target="_blank">📅 07:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هجمات جديدة تدك الدوحة القطرية</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/82470" target="_blank">📅 07:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82469">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هجمات جديدة تدك الدوحة القطرية</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/naya_foriraq/82469" target="_blank">📅 07:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82468">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/82468" target="_blank">📅 07:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82467">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
تم تدمير المراكز اللوجستية التي تدعم السفن ومنصات تزويد السفن بالوقود التابعة للولايات المتحدة في ميناء الدقم في سلطنة عمان، وذلك في هجوم عنيف ومفاجئ.</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/naya_foriraq/82467" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82465">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=esQ6lXwVUVw6osQz8B2Gnr1APTkWq9Glv5vTW-T30ZUX_9Y3zGv_NOPdNZWk3S5aHVTgKh5jun7pWtPtCmfXGqi6GOB2OoQ0cITyuxSbtMghhULpaSVApig74eWSrA1ZK7W1PK7lO12QGOeek-5IKjGJO_yiZHsr06pHWvq2ZpANoS1pWOJKPIXQq-BOlkO3i7YXzC5otd1-5H2EcVku18T9d1f-J-L8TuLbdG0AictMizyC9YqwZjFkB6a7h4NgF0zokzv3QshcLCDsIMFTQc8cbBYu5C9Z_QzcIYYgVbrnuWHewN2zdy_2Q69oR8wyFtB4kYk5cZxNBkfgD87r3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=esQ6lXwVUVw6osQz8B2Gnr1APTkWq9Glv5vTW-T30ZUX_9Y3zGv_NOPdNZWk3S5aHVTgKh5jun7pWtPtCmfXGqi6GOB2OoQ0cITyuxSbtMghhULpaSVApig74eWSrA1ZK7W1PK7lO12QGOeek-5IKjGJO_yiZHsr06pHWvq2ZpANoS1pWOJKPIXQq-BOlkO3i7YXzC5otd1-5H2EcVku18T9d1f-J-L8TuLbdG0AictMizyC9YqwZjFkB6a7h4NgF0zokzv3QshcLCDsIMFTQc8cbBYu5C9Z_QzcIYYgVbrnuWHewN2zdy_2Q69oR8wyFtB4kYk5cZxNBkfgD87r3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الدوحة القطرية وسط إطلاق منظومة الباتريوت الامريكية صواريخها لصد واعتراض الهجوم الإيراني</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/82465" target="_blank">📅 07:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82464">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوي انفجارات وصافرات الانذار في قطر</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/naya_foriraq/82464" target="_blank">📅 07:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82463">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مسؤولين إسرائيليين: استعدادات عسكرية إذا شملت المواجهة إسرائيل</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/82463" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82462">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrEQsJy3f5B-URFueKdym3BUAdNK1PS_Kp9G3_QV02n63lYHQKWwYxJ0gv0ojJKF1c3asHlz1WS8qHXgLY8weFCCjFVerfXHmUTjZmwj19q8noim15mkx_feNFhWSFaE1WKY4mMMcZX0g3BwIbeRecR0v7XuM4t_h6JaMoIKa-nqNlSATdRZ-3hgSfmugoEyHCopF1qmTUtkWg1DH7TCklnJzfGUBe-BGj-oP9PWdY1udpt_hzjd5yxVDzOWnDbego0z8ebff2a3XOt7w7kvlxrHR1m8hC-1AOGgEWUVBSGrG2PeCbDmLJwVrtn1sVDSHObBHPFSInbSBrx0Ydbr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صواريخ نحو البوارج الامريكية في الخليج الفارسي وبحر عمان.</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/82462" target="_blank">📅 07:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82461">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اطلاق صواريخ نحو البوارج الامريكية في الخليج الفارسي وبحر عمان.</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/82461" target="_blank">📅 07:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82460">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني: أنباء عن إطلاق نيران تحذيرية تجاه سفينة ثانية حاولت العبور من مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/82460" target="_blank">📅 07:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82459">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265d875f3a.mp4?token=paYnrj6zAC0_l9dFvzsOHNw1yotY-KS5lbJjvWAA0jp86fqIMNKcIVoSB2Uqu6TD57p_I8Hf1IekcTXgzfgCTtxqLATY3u6dHkHWyc2U0KBNQ-BpXkkfIDDMj0jajFbl40nU6sfnyxPBF1opWu3hRbmFVIKqx1Na58B8B7dca7OKT6VsbchMeaB5CRvOE6nJudLktdlvHl-EiKF4PRvKyMZBZnH8WY8kPrd3yQTzhiDQrOlvXdDZ2C00ybK8MsiQDGi5EI2BxRwIK5ht40pEYO14zcFFN94mwSJgGTRNiKWWlQl_pYl2_Zrzgz6TvUGLr9MdZoqs7ClAsYqlR4A482h1h_xyDMTDEUpWnR0nIzztd_Kmpze9wtI3NfLi92qOMFerYSjbVwA6k28tqVyUfsl31_SK8TFixLsfdmEmwYp2jXyh8iMmWUbMl92sGW5wjIhf42RikrA-hnPALk8PP3kNbU0YYwIFae77jNEOLGIGfMzUsHpzA6TeZbpAY-FG8ZStdwyeqCJs6ubbg97Ev8RPMKrvoz3zo-W9f4uB6GsuGebrpHH9HVGNQ7mogf8S37PiwcA6RyEdci2nGqL1tmDpwMyd_QkcXkfDMbFoU_SnRjSMXUgfDgbYKYe5oiH9V9gNfBB6m4nU7nMPA3mJs-0YQQFRphAdLxmdC1Cso1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265d875f3a.mp4?token=paYnrj6zAC0_l9dFvzsOHNw1yotY-KS5lbJjvWAA0jp86fqIMNKcIVoSB2Uqu6TD57p_I8Hf1IekcTXgzfgCTtxqLATY3u6dHkHWyc2U0KBNQ-BpXkkfIDDMj0jajFbl40nU6sfnyxPBF1opWu3hRbmFVIKqx1Na58B8B7dca7OKT6VsbchMeaB5CRvOE6nJudLktdlvHl-EiKF4PRvKyMZBZnH8WY8kPrd3yQTzhiDQrOlvXdDZ2C00ybK8MsiQDGi5EI2BxRwIK5ht40pEYO14zcFFN94mwSJgGTRNiKWWlQl_pYl2_Zrzgz6TvUGLr9MdZoqs7ClAsYqlR4A482h1h_xyDMTDEUpWnR0nIzztd_Kmpze9wtI3NfLi92qOMFerYSjbVwA6k28tqVyUfsl31_SK8TFixLsfdmEmwYp2jXyh8iMmWUbMl92sGW5wjIhf42RikrA-hnPALk8PP3kNbU0YYwIFae77jNEOLGIGfMzUsHpzA6TeZbpAY-FG8ZStdwyeqCJs6ubbg97Ev8RPMKrvoz3zo-W9f4uB6GsuGebrpHH9HVGNQ7mogf8S37PiwcA6RyEdci2nGqL1tmDpwMyd_QkcXkfDMbFoU_SnRjSMXUgfDgbYKYe5oiH9V9gNfBB6m4nU7nMPA3mJs-0YQQFRphAdLxmdC1Cso1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجيش الأمريكي:
أكملت القيادة المركزية الأمريكية (CENTCOM) هذا الأسبوع جولة ثالثة من الضربات ضد إيران (في 11 يوليو)، محملةً القوات الإيرانية المسؤولية عن مهاجمة سفينة تجارية أخرى في مضيق هرمز. استهدفت القوات الأمريكية ما يقرب من 140 هدفاً عسكرياً إيرانياً باستخدام ذخائر دقيقة أطلقتها طائرات مقاتلة (تُشغَّل من البر والبحر) وطائرات مسيّرة وسفن بحرية. وشملت الأهداف مواقع للصواريخ والطائرات المسيّرة الإيرانية، وقدرات بحرية، ومنشآت لتخزين الذخيرة، وشبكات اتصالات، ومواقع للمراقبة الساحلية. وعلى مدار ثلاث ليالٍ من الضربات هذا الأسبوع، استهدفت القيادة المركزية الأمريكية أكثر من 300 هدف - بتوجيه من القائد العام - وذلك بهدف تقويض قدرة إيران على مهاجمة البحارة المدنيين والسفن التجارية التي تعبر المضيق بحرية؛ علماً بأن حركة عبور السفن التجارية عبر هذا الممر البحري الدولي الحيوي لا تزال مستمرة. ومنذ أوائل شهر مايو، ساعدت القوات الأمريكية في تأمين العبور الناجح لأكثر من 800 سفينة تجارية و400 مليون برميل من النفط الخام عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/82459" target="_blank">📅 07:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82458">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecd065d0a.mp4?token=TqgbAXSWTfd8pGB9PVRbScopAa1rS6ts38reJ57K_PILwmNB11_GDVJavysaxP90ET_Wx8smPZ1tfP6zef-o341OH0gKV9Mu8ExCZ4--9FRROaZ1aPgNAZpJkqRgvjAmmXPSw1jVtBCguXizqGqi3iicYDRqqPiGpSuHklZOe3-gZxyZY9vJ24B0gBJGk3M29dY-XxwtVTYkp1sso17RXqbkU6-z3nI9HK4eYQ4U1QqaPPp2wzxkUZLRw_neLXgPVWqwWsrWevNy43xXa0mg6uj2MhtTw06NGTVB9Kgl5V1YKOUfiH6cO0oOeIZjXnuyKqpOJ_HNcsb-ChtNDlfBh5293Dw0U4JGIaLotJ6qEQ09tPoZ5ACGz7aPCN2IaSd0PcPz3usMg7yyhorBKZLWfOgNT2reNYxVLujdfAQw9p4OIcvGatYQoazyl0YhYmqCLYrsCv4iUYfFuM9KR7sOyHKWgZRd0gvP1LG58AH7ELMrAQBHm_YqxpxOB1GNqgMuRwFEh-jzFLxFglU-hhsYPQvGKLWK63eZSThAY5M9HeLP38aiGHTD8YxJ4f3_zuXOmPKeTr65qiUAZlC5uHDAvw0eat_FOevbcMYcJlPxuTWJoJbZ2Dl3AEBx46dedw5moGztGAyGfNkHlWcsNq8NyJKLCkBDexJr_VQNoHXP8Ys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecd065d0a.mp4?token=TqgbAXSWTfd8pGB9PVRbScopAa1rS6ts38reJ57K_PILwmNB11_GDVJavysaxP90ET_Wx8smPZ1tfP6zef-o341OH0gKV9Mu8ExCZ4--9FRROaZ1aPgNAZpJkqRgvjAmmXPSw1jVtBCguXizqGqi3iicYDRqqPiGpSuHklZOe3-gZxyZY9vJ24B0gBJGk3M29dY-XxwtVTYkp1sso17RXqbkU6-z3nI9HK4eYQ4U1QqaPPp2wzxkUZLRw_neLXgPVWqwWsrWevNy43xXa0mg6uj2MhtTw06NGTVB9Kgl5V1YKOUfiH6cO0oOeIZjXnuyKqpOJ_HNcsb-ChtNDlfBh5293Dw0U4JGIaLotJ6qEQ09tPoZ5ACGz7aPCN2IaSd0PcPz3usMg7yyhorBKZLWfOgNT2reNYxVLujdfAQw9p4OIcvGatYQoazyl0YhYmqCLYrsCv4iUYfFuM9KR7sOyHKWgZRd0gvP1LG58AH7ELMrAQBHm_YqxpxOB1GNqgMuRwFEh-jzFLxFglU-hhsYPQvGKLWK63eZSThAY5M9HeLP38aiGHTD8YxJ4f3_zuXOmPKeTr65qiUAZlC5uHDAvw0eat_FOevbcMYcJlPxuTWJoJbZ2Dl3AEBx46dedw5moGztGAyGfNkHlWcsNq8NyJKLCkBDexJr_VQNoHXP8Ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
ردًا على استمرار انتهاكات أمريكا الإجرامية لمناطق في جنوب البلاد، بدأ الجيش الإيراني منذ ساعات، بهجمات بطائرات بدون طيار، استهداف أنظمة "باتريوت"، ومخازن الذخيرة، وموقع الرادار التابع للجيش الأمريكي الإرهابي في الكويت.
وفي موجة أخرى من الهجمات بالطائرات بدون طيار التي نفذها الجيش الإيراني، استهدف نظام الاتصالات وموقع الرادار التابع للجيش الأمريكي "الذي يقتل الأطفال" في البحرين.
حذر الجيش الإيراني: إن عواقب هذه الأعمال وعدم الاستقرار في المنطقة ستكون على عاتق العدو الأمريكي والصهيوني، وفي حال تكرار هذه الهجمات، فسوف نقدم ردودًا أكثر حدة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82458" target="_blank">📅 06:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82457">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8b2e00b8.mp4?token=E6rkDWNTLfaS2yu1AnX0wupXVoMZFhXc0hDIgT4YQ7nKC9AA_SeQzxUnc1u7Qm04YuV-HcnHzOLIst4_ZjKIoznw4t1PoS96O7aIJXrxwkFmaHfTNCurz_DaeUqxnxhU6wGE87ZGLiV8WcqnRrHKi32oRVgyWkrFxtzdZzyONoQkDxWkugJnvXBVbU1h1B0yLhb7eOJDUVIHiBxd2vvIj_polY-pP0nWrTRYcOZzRPppbo9skMcSsJCzaWydqNvCTOmqQKEj-bld360pr3iPUYFtHKoKVxJ9HCXPl0EvIETdEq9KD5R8PM9UjVxbsDKHYSV8FvsYNiJxhyVaUY40xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8b2e00b8.mp4?token=E6rkDWNTLfaS2yu1AnX0wupXVoMZFhXc0hDIgT4YQ7nKC9AA_SeQzxUnc1u7Qm04YuV-HcnHzOLIst4_ZjKIoznw4t1PoS96O7aIJXrxwkFmaHfTNCurz_DaeUqxnxhU6wGE87ZGLiV8WcqnRrHKi32oRVgyWkrFxtzdZzyONoQkDxWkugJnvXBVbU1h1B0yLhb7eOJDUVIHiBxd2vvIj_polY-pP0nWrTRYcOZzRPppbo9skMcSsJCzaWydqNvCTOmqQKEj-bld360pr3iPUYFtHKoKVxJ9HCXPl0EvIETdEq9KD5R8PM9UjVxbsDKHYSV8FvsYNiJxhyVaUY40xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقر قيادة الاسطول الخامس الأمريكي في البحرين يحترق بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/82457" target="_blank">📅 06:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82455">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=eyz8coDND0tg54cCEDMtghUVqw-HyeTWKwvF6NmWFa5k_EuTJY2e_NlonXIj7kplOIy6l8JW83J5AuDUdpivJJgqflsRNadsIlHjwjZ9puhXZ_hbObJ-_1c2gXVbP4K9RsWSYjYhM7jbWsmKxrzkW49c7dCvdVlVulGnyCHCNoosVA3KUru99x3nmLt3KQqqDUqTenAWNUrpNoVQl_Z-c9mtuCWEhz8x7bSbHUnPylAkJFj8zFh92W2-qdkvNo8xNLhamhTMM47swgr65o2E9yaE1TMpXJw1OOFE65JiGLfPEmANCRAgehwOQdq0dIECrlQF7SoKg1jrQhnIhW7F5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=eyz8coDND0tg54cCEDMtghUVqw-HyeTWKwvF6NmWFa5k_EuTJY2e_NlonXIj7kplOIy6l8JW83J5AuDUdpivJJgqflsRNadsIlHjwjZ9puhXZ_hbObJ-_1c2gXVbP4K9RsWSYjYhM7jbWsmKxrzkW49c7dCvdVlVulGnyCHCNoosVA3KUru99x3nmLt3KQqqDUqTenAWNUrpNoVQl_Z-c9mtuCWEhz8x7bSbHUnPylAkJFj8zFh92W2-qdkvNo8xNLhamhTMM47swgr65o2E9yaE1TMpXJw1OOFE65JiGLfPEmANCRAgehwOQdq0dIECrlQF7SoKg1jrQhnIhW7F5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  اصابة مباشرة للاسطول الخامس الأمريكي في البحرين والنيران تشتعل واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/82455" target="_blank">📅 06:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82454">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات عنيفة جدا تهز البحرين</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/82454" target="_blank">📅 06:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82453">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84fbe0232.mp4?token=bHrvItK86_JNIodPKPQ_LJ9G1E2TD-fYM43RDRC3x9vBEUrmDSZ2lcnp_khPGjJcgOMs_zIPZ2Jdff779AiPNf2G5-4BLRMcoQ1MkMdjyQ5nApV7Wek-OIkQmtbuMUwnFxHtbNBQPRuponjntP2PXWkPwPvXM-Hxq9Dh05w8X_8TA667mEt_rJLk8VaOWe4kPr2uM0b6zs_tVn7oV1urvtcj41q8bLxMZWSoV2JgGrg98KDFPE1ftkoD0q_s32a8eHubifSwg_ylW60k4lw-cxZKVU6Sz2gJusJagUDZZVYQHwg-dco3lOGsFfsUr3LnMvsBEDKYVX0fbt5AFNa4Jxg8tDQCQ5wh1utNynyrlEHrI-oFmgCDyCP4l8yJjHBp7FoyyM2BTbN3gY6GYlNdeysh8j6O1R4-OEChhBAYT_VsIf1fHFWQjmfuqfvVKDOCskpw_qhhbEqpgZ_qK6ui3JvWYfbx7ZiT089MOCFM_ZVv6XT_zN3toAJFjp8e8O_FbzyqfuMEpd2MIDVLAynHkZDtdw5EppoHLquIX4wFw4pgJKds1UNA_iP55sCSLJwI_z8Xe3y1OaonZbirsW4Bj_1Y8KTnULY9eh0qhIL-YH1NdoD1_0lWyViV2HBwqe_N3uLbHsbSjT2m_-NoIJ-tA38ASXS2Kj3vGayYDSNnXBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84fbe0232.mp4?token=bHrvItK86_JNIodPKPQ_LJ9G1E2TD-fYM43RDRC3x9vBEUrmDSZ2lcnp_khPGjJcgOMs_zIPZ2Jdff779AiPNf2G5-4BLRMcoQ1MkMdjyQ5nApV7Wek-OIkQmtbuMUwnFxHtbNBQPRuponjntP2PXWkPwPvXM-Hxq9Dh05w8X_8TA667mEt_rJLk8VaOWe4kPr2uM0b6zs_tVn7oV1urvtcj41q8bLxMZWSoV2JgGrg98KDFPE1ftkoD0q_s32a8eHubifSwg_ylW60k4lw-cxZKVU6Sz2gJusJagUDZZVYQHwg-dco3lOGsFfsUr3LnMvsBEDKYVX0fbt5AFNa4Jxg8tDQCQ5wh1utNynyrlEHrI-oFmgCDyCP4l8yJjHBp7FoyyM2BTbN3gY6GYlNdeysh8j6O1R4-OEChhBAYT_VsIf1fHFWQjmfuqfvVKDOCskpw_qhhbEqpgZ_qK6ui3JvWYfbx7ZiT089MOCFM_ZVv6XT_zN3toAJFjp8e8O_FbzyqfuMEpd2MIDVLAynHkZDtdw5EppoHLquIX4wFw4pgJKds1UNA_iP55sCSLJwI_z8Xe3y1OaonZbirsW4Bj_1Y8KTnULY9eh0qhIL-YH1NdoD1_0lWyViV2HBwqe_N3uLbHsbSjT2m_-NoIJ-tA38ASXS2Kj3vGayYDSNnXBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية جديدة تستهدف البحرين</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/82453" target="_blank">📅 06:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82452">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الحرس الثوري: مركز القيادة والتحكم ومواقع طائرات الاستطلاع من طراز MQ9 في القاعدة الأمريكية "الأمير حسن" في الأردن دُمرت</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/82452" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82451">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏فرانس برس: سماع دوي انفجارات في الدوحة</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/82451" target="_blank">📅 06:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82450">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8023d66f.mp4?token=S2dkpKLk5V5o0MMH4-AODjsVa7-TjTfaoX2vHZSAS0L4UcbGjA1ccN_L4Te9CTVffVs_P0EW2uZUSYFsm6cYk_m4i83WjZupwGxteAelPTm7MYyxJQJLXxheg9n3iQ6biHfynqpQrpKzidxlDp2ZMlTyHdJIqo5Bv380PHrGDertVrOX-9wO7baSJlP0-6QuP7WllEvCzU838yAPp9aGjogdKKGFuHjmwtL_EVe2lTq3d63ZfgnUzF1wj_yoMHwsl67gNECYKOrRrvs04HvAJ3FIeiWImKgwx5lsERPSwZuBpakRrqzlTCFJjVfaNPErDv72tlUCCnubsP2HA1Zu7pI794nJe4e_XLKnjdswxYy6a5olxdIFqKiKo9VhP8-nVvG38wR5IU4woTMiGAWTxhu3ZQudX2a39tAk7v834OHlFNgbBnWQVQI2obM3zHzVJogmoozi38DEfQzUpSQzoDXgx57fK8DN683BX7RHv8u0S2F_qkGcfSE6-KOHrYYiEcpV1s_lYqY3gkgvyAGDAekjRDp2WQc8Zb95DHc0CmnbyFkGxH2AB1Y-CTalcf_vplcgj_w2N8VOKTyYC24vt2xE1QUFAz-cKZWG31Jq2FWPa71vY6m6GeARSmMQ31wkpYVwT8YoUG-faISOQZnpbCyjYXzLC3N2C6RWcs22eiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8023d66f.mp4?token=S2dkpKLk5V5o0MMH4-AODjsVa7-TjTfaoX2vHZSAS0L4UcbGjA1ccN_L4Te9CTVffVs_P0EW2uZUSYFsm6cYk_m4i83WjZupwGxteAelPTm7MYyxJQJLXxheg9n3iQ6biHfynqpQrpKzidxlDp2ZMlTyHdJIqo5Bv380PHrGDertVrOX-9wO7baSJlP0-6QuP7WllEvCzU838yAPp9aGjogdKKGFuHjmwtL_EVe2lTq3d63ZfgnUzF1wj_yoMHwsl67gNECYKOrRrvs04HvAJ3FIeiWImKgwx5lsERPSwZuBpakRrqzlTCFJjVfaNPErDv72tlUCCnubsP2HA1Zu7pI794nJe4e_XLKnjdswxYy6a5olxdIFqKiKo9VhP8-nVvG38wR5IU4woTMiGAWTxhu3ZQudX2a39tAk7v834OHlFNgbBnWQVQI2obM3zHzVJogmoozi38DEfQzUpSQzoDXgx57fK8DN683BX7RHv8u0S2F_qkGcfSE6-KOHrYYiEcpV1s_lYqY3gkgvyAGDAekjRDp2WQc8Zb95DHc0CmnbyFkGxH2AB1Y-CTalcf_vplcgj_w2N8VOKTyYC24vt2xE1QUFAz-cKZWG31Jq2FWPa71vY6m6GeARSmMQ31wkpYVwT8YoUG-faISOQZnpbCyjYXzLC3N2C6RWcs22eiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية جديدة تستهدف البحرين</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/82450" target="_blank">📅 06:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82449">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf914DP5jpAiUHsgTI7ONWYpJQiecCIjCgU1G8friIOwsbZgcwixX-nwWRKpKMiIht4uOGjVSWUNItrW8TlaCp28f_6lbvY3V2bVwvdoq49YQ4DuxUdC9aOlsIZGIb1BxHCLOuuTtS94SYQJCPDTFBwQx4prIWkzZhJp3uS33KToYhumPtqiSyGZslJutQegJe1pPzekElJppBFr2Yv1iTt-NG9sToldydUwoQ_UcR3tWAg-9AqlXWHp-jGxT151gwrhMbpeXSyhNADescCsjQqhUN0flUCG8mM5uEC60zLSCjKH-wKp9BqtJbbNfnf4zPaNhvgTfjh-zNUth-SMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم صاروخي يدك قاعدة العديد الأمريكية في قطر</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/82449" target="_blank">📅 06:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82448">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">موجة صاروخية جديدة تدك الامارات</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/82448" target="_blank">📅 06:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82447">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">موجة صاروخية جديدة تدك الامارات</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82447" target="_blank">📅 06:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82446">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82446" target="_blank">📅 06:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82445">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سربازان "آقا سید مجتبی" آمریکایی‌ها را ادب خواهند کرد.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/82445" target="_blank">📅 06:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82444">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هجوم صاروخي يدك قاعدة العديد الأمريكية في قطر</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/82444" target="_blank">📅 06:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82443">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صواريخ تدك ابوظبي ودبي</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/82443" target="_blank">📅 06:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82442">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات تهز امارات</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/82442" target="_blank">📅 06:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82441">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات تهز امارات</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82441" target="_blank">📅 06:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82440">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTaLEXO9HcejHls4PX9zTXAWMQf7dINXcLZG42ufDbUnuLHm1Qhn7n4wlOv6iJC71xzlnJqbsMDok3lFhShxvTz0dSmM-UeAEmEOBkO1ulCFjekpyVQ7vw33HvKvidu-nVDNbp-s_U5rBwc2TA16aBncpqXX6RpAXJTvwTElvUfZC7Fywvx1jzlkBa8_AeDiTFtiTB3OSqSGIL4SU-98VFIkv1_uVLF1qVLJtzrQhvvH9lV99RS3ezPYe1s_8lU0aOtWO-Vb2_i1Lnn9-8hqnFZq6PYW1MaL1HmhT1AA6KRmSYFjX4vyAFhyQ2sFDXwpTMImvIN2f586YSDnW_4FEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/82440" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82439">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/82439" target="_blank">📅 06:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82438">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/82438" target="_blank">📅 06:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82437">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b3e9700b.mp4?token=KpWm8bdy5938tTWvu6felXkGZdJXLqLJBLrzOAvBtGJtflKKg_aZi40b3dljVOEY_VG7KDcKS_X27Zqgohc1bDQFQjrlyUGl0X8aGh1W7eMr7HJPhbbykyFQduoRWQxjKWKQBAWKeSAz9W05OT61qWyFCClcqpTWDuI95TdLf5NHy0093ZwtPY9fO532t2c_94I5sqnR-d_laTLFi_Pnnm-yoPgWqcYxLGzRAvuVVCTlsGdpia7gmJCwCsbgeNhk0qPj3PSSND0OdrNr6oasP6SUudo6segzOtbhmkX9v5fiJy9QEC3ODF5n8QxnlK0SU3n_KFk5w6MTdn5-Ixrngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b3e9700b.mp4?token=KpWm8bdy5938tTWvu6felXkGZdJXLqLJBLrzOAvBtGJtflKKg_aZi40b3dljVOEY_VG7KDcKS_X27Zqgohc1bDQFQjrlyUGl0X8aGh1W7eMr7HJPhbbykyFQduoRWQxjKWKQBAWKeSAz9W05OT61qWyFCClcqpTWDuI95TdLf5NHy0093ZwtPY9fO532t2c_94I5sqnR-d_laTLFi_Pnnm-yoPgWqcYxLGzRAvuVVCTlsGdpia7gmJCwCsbgeNhk0qPj3PSSND0OdrNr6oasP6SUudo6segzOtbhmkX9v5fiJy9QEC3ODF5n8QxnlK0SU3n_KFk5w6MTdn5-Ixrngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق يظهر لحظة إطلاق الصواريخ الإيرانية نحو القواعد الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/82437" target="_blank">📅 05:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82436">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338f41fc7a.mp4?token=WyUqd9kSnBmQRPJ-oT8hLNe3340FdtbhEYVnn1yZW9naRph-jZnIo4sHzNqm-LU5FDXhvn-JtNKVqkSoci9ttxcnuZZhmHpOmtfBpjohyQ0rj7v-4-AckjOl030y8-55jHs0WpfnJ9CIOdYbdu1HneuKe0SJmLcqTcV8MPSItSCfvhFRPyhtixFvSiuACtZtGJQMi2pJ_JZ-u2gh3sfvybxo8j_pFjdm59vimA6D8xL-A4VcM6wBq8IVH49KVydGuYIBmDlvoNh3ShjmvYXL0vxvlq1lFBfCy2qZWG1LXeZ-u6iS5i2ALmcKa_Mxrh7SxFkYM7BtGf1J_ZSMEFFxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338f41fc7a.mp4?token=WyUqd9kSnBmQRPJ-oT8hLNe3340FdtbhEYVnn1yZW9naRph-jZnIo4sHzNqm-LU5FDXhvn-JtNKVqkSoci9ttxcnuZZhmHpOmtfBpjohyQ0rj7v-4-AckjOl030y8-55jHs0WpfnJ9CIOdYbdu1HneuKe0SJmLcqTcV8MPSItSCfvhFRPyhtixFvSiuACtZtGJQMi2pJ_JZ-u2gh3sfvybxo8j_pFjdm59vimA6D8xL-A4VcM6wBq8IVH49KVydGuYIBmDlvoNh3ShjmvYXL0vxvlq1lFBfCy2qZWG1LXeZ-u6iS5i2ALmcKa_Mxrh7SxFkYM7BtGf1J_ZSMEFFxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تتجه نحو الاهداف المعادية</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/82436" target="_blank">📅 05:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82435">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d967790d6a.mp4?token=pZfAxN8f74zDepnMccT_cxfIG2MLVhFZp4FjTI8Ac7PcY5G_hYcg0a01Cy2ASz5K93XVX3nX6TE4bhzY80a6uByGA03X0t5R1lhI3duq_fZ8PQ4MoCKsLAgy55L_s4EyOI-GbzUjV3Gcnf7bi2jggl24TUfj6Wh8jQBJ017R8KftpZqkv0uEZCsU0d41G4plFtAAB7lwmEaL3GaNjg5qSX7nPZ62dmrY9fEIdli7T7Es84S6slhiROXvkO0CMGXn4ft4NQvwcOXfIjMqfvk30yeW3XFJbGowqKMiUnAothKwsZVdxDO_gofm8tXM113JR04rEh84S3244JZr1wUMaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d967790d6a.mp4?token=pZfAxN8f74zDepnMccT_cxfIG2MLVhFZp4FjTI8Ac7PcY5G_hYcg0a01Cy2ASz5K93XVX3nX6TE4bhzY80a6uByGA03X0t5R1lhI3duq_fZ8PQ4MoCKsLAgy55L_s4EyOI-GbzUjV3Gcnf7bi2jggl24TUfj6Wh8jQBJ017R8KftpZqkv0uEZCsU0d41G4plFtAAB7lwmEaL3GaNjg5qSX7nPZ62dmrY9fEIdli7T7Es84S6slhiROXvkO0CMGXn4ft4NQvwcOXfIjMqfvk30yeW3XFJbGowqKMiUnAothKwsZVdxDO_gofm8tXM113JR04rEh84S3244JZr1wUMaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق موجة صاروخية جديدة من إيران نحو أهداف في المنطقة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82435" target="_blank">📅 05:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82434">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اطلاق صواريخ من إيران</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/82434" target="_blank">📅 05:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82433">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اطلاق صواريخ من إيران</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/82433" target="_blank">📅 05:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82432">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الهيئة البحرية البريطانية: حادث على بعد 9 أميال بحرية شرق سلطنة عمان.   السلطات العسكرية تُفيد بتضرر مؤخرة سفينة حاويات واشتعال حريق على متنها.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/82432" target="_blank">📅 05:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82431">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
مساعد الأمن في محافظة خوزستان الإيرانية:
إن مقاطعات هندیجان وماهشهر و آبادان تعرضت لقصف من قبل العدو.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/82431" target="_blank">📅 05:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82430">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوي انفجارات في ميناء جاسك ضمن محافظة هرمزغان الإيرانية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/82430" target="_blank">📅 04:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82429">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/962ba7b5d9.mp4?token=AI0ugIhetutRYKW3X3lkQGl_J457mt3IMh6bJYc3sQzQ6auywffRTFziaLbLgGDo9ldrNvX_txzJucbSElxw0UicX-ObUwtc9AXwsuOXoh3noKvBB-zMmoDbl403B87l5BCYYCLG7AYf0c-SHJueI5G1pj_cQGcIKXLLuXzlPGC9DWLChvwzmDRC4sR_Ci8xgCtOdoJjYQ99xIC9N5gknJldTPA5XZNok04sCyjH1gSyPU9ljFm37RYRsh9ZA2tD411KruHVPVjXjsbY0tjRK4LMSSHLSVLkibH07nqelxWteeHycnDK3xOxa4jhwMjEQvAeCeNz0CY0UpypCJ0R6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/962ba7b5d9.mp4?token=AI0ugIhetutRYKW3X3lkQGl_J457mt3IMh6bJYc3sQzQ6auywffRTFziaLbLgGDo9ldrNvX_txzJucbSElxw0UicX-ObUwtc9AXwsuOXoh3noKvBB-zMmoDbl403B87l5BCYYCLG7AYf0c-SHJueI5G1pj_cQGcIKXLLuXzlPGC9DWLChvwzmDRC4sR_Ci8xgCtOdoJjYQ99xIC9N5gknJldTPA5XZNok04sCyjH1gSyPU9ljFm37RYRsh9ZA2tD411KruHVPVjXjsbY0tjRK4LMSSHLSVLkibH07nqelxWteeHycnDK3xOxa4jhwMjEQvAeCeNz0CY0UpypCJ0R6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مقتل 2 واصابة 5 خلال حادث إطلاق نار في مدينة تورنتو الكندية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/82429" target="_blank">📅 04:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82428">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
مصدر إيراني: نفي وقوع انفجار في ميناء ديلم بمحافظة بوشهر الإيرانية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/82428" target="_blank">📅 04:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82427">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
الأوضاع هادئة في مدن بندر عباس وسيريك وجاسك بمحافظة هرمزغان جنوبي البلاد.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/82427" target="_blank">📅 04:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
نفي وقوع انفجار في ميناء ديلم بمحافظة بوشهر الإيرانية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/82426" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82425">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔻
الحرس الثوري : اغلاق مضيق هرمز حتى اشعار اخر. بسم الله الرحمن الرحيم، قاسم الجبرين  في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.  قبل…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82425" target="_blank">📅 03:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82424">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امشب پایگاه‌های دشمن در منطقه شخم زده خواهند شد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82424" target="_blank">📅 03:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82423">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4e56b905c.mp4?token=bGICZef91eYZNq_QF4mQmqUmmSXP0-CzlqVNKNxd0yUAw7llLNPri-xPz77sLHt8Tn69ccq5_m04YxYVKZ7F33d-aVftmSLZkt5jViVdfJa32NgGqjpw1dRvUAyCSun1RZK8PB-XgTiL1dhlcugE5hwnIVZk7SqPilOw4HONES38OqjU_o6RN9Ac_Ia6EEJ_vIZfNmkCvda5G0oVJcBnLinynjX3ua9RiFToBJo8a10WzZScXH0pqTqymSrvcuPftP97mZ_VmzOSuEHh3_ddAETAjNc-2HWvISCeKtRPZ2hChtc71MotoWQVkkx-2r1AMe-EMdHMI-tXzhMGKHHfLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4e56b905c.mp4?token=bGICZef91eYZNq_QF4mQmqUmmSXP0-CzlqVNKNxd0yUAw7llLNPri-xPz77sLHt8Tn69ccq5_m04YxYVKZ7F33d-aVftmSLZkt5jViVdfJa32NgGqjpw1dRvUAyCSun1RZK8PB-XgTiL1dhlcugE5hwnIVZk7SqPilOw4HONES38OqjU_o6RN9Ac_Ia6EEJ_vIZfNmkCvda5G0oVJcBnLinynjX3ua9RiFToBJo8a10WzZScXH0pqTqymSrvcuPftP97mZ_VmzOSuEHh3_ddAETAjNc-2HWvISCeKtRPZ2hChtc71MotoWQVkkx-2r1AMe-EMdHMI-tXzhMGKHHfLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان في بوشهر عقب العدوان الأمريكي</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/82423" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82422">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سيريك مجددا دوي انفجارات</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/82422" target="_blank">📅 03:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82421">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات في بوشهر وجغادك وعسلوية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82421" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82420">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f26690d832.mp4?token=dlKlX6sGOR7k5HoWeBdDVOAFniCyaQbv1odQVC9-GxyeT7H3kWif_Q0lR8cfMWcxSj23hKuhdzgqCfyz0Kfxy5SWKizZ_UjAftXScqQKqrztc9K9JxX9VJtun43bzonCfzXCHo38jMtu95XyJdwzYYCeJ_ZWB99wAJNSP7Gf8Tmkf_v41vimqnvYPVzNssi2FARPg_jrcXXo80qFVWLIHAG3JKOo3XjuJOshtyL2zg8a-nFWtZn0r5iLKYlFMkJDPnLdAd7h8A5om6BAc6ucQvepz__Z7tzOerl6u8NkY8HnggxEGvCXPK1ra-RtY29sapiYs601VKwM0GHanf6jgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f26690d832.mp4?token=dlKlX6sGOR7k5HoWeBdDVOAFniCyaQbv1odQVC9-GxyeT7H3kWif_Q0lR8cfMWcxSj23hKuhdzgqCfyz0Kfxy5SWKizZ_UjAftXScqQKqrztc9K9JxX9VJtun43bzonCfzXCHo38jMtu95XyJdwzYYCeJ_ZWB99wAJNSP7Gf8Tmkf_v41vimqnvYPVzNssi2FARPg_jrcXXo80qFVWLIHAG3JKOo3XjuJOshtyL2zg8a-nFWtZn0r5iLKYlFMkJDPnLdAd7h8A5om6BAc6ucQvepz__Z7tzOerl6u8NkY8HnggxEGvCXPK1ra-RtY29sapiYs601VKwM0GHanf6jgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تنشط في جنوب البلاد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82420" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82419">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوي انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82419" target="_blank">📅 03:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82418">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مصدر مطلع: حتى هذه اللحظة، لم يُسمع أي صوت انفجار في مقاطعة ميناب جنوبي إيران.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/82418" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82417">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🌟
إعلام العدو:
حدث أمني تحت الرقابة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82417" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82416">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مصدر إيراني مطلع: نفي شائعة الهجوم على الأهواز وآبادان.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82416" target="_blank">📅 03:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82415">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e160b066cb.mp4?token=p_aVq7T-lJ0fmhclELhWW1GHriaGHj9utCkG02LQ3voPqz6UVxnWMN8_JJsHt1527UW6OsjZG-d3U5CEfy986K3KnM-fgIdXShfC_JvxOBaxSWRrhIxsn_DP4jBx7zPAB3o7Q027snPug4fDUnVcp7_aYkQOtkBQsiLt4NKKBg5VnabK80q-9cgmp0xTcVPkIkQAlzFEP88iToioAu3wyF7e_hfnwQreX4K4g6mZzybmznYjQ_fSfZ4jEqeBspV-tfb_btbV-UDc0uc17l7lEbxKbyBrf2xTZMkILkulXjKF2BoOTPOphnUNqzDDMkx6eyYQEzM2c5VkT6Sn3sjqTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e160b066cb.mp4?token=p_aVq7T-lJ0fmhclELhWW1GHriaGHj9utCkG02LQ3voPqz6UVxnWMN8_JJsHt1527UW6OsjZG-d3U5CEfy986K3KnM-fgIdXShfC_JvxOBaxSWRrhIxsn_DP4jBx7zPAB3o7Q027snPug4fDUnVcp7_aYkQOtkBQsiLt4NKKBg5VnabK80q-9cgmp0xTcVPkIkQAlzFEP88iToioAu3wyF7e_hfnwQreX4K4g6mZzybmznYjQ_fSfZ4jEqeBspV-tfb_btbV-UDc0uc17l7lEbxKbyBrf2xTZMkILkulXjKF2BoOTPOphnUNqzDDMkx6eyYQEzM2c5VkT6Sn3sjqTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الإيرانية البطلة تشتبك مع اهداف معادية في سماء مدينة ماهشهر ضمن محافظة خوزستان جنوبي إيران</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82415" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82414">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوي الانفجارات التي سمعت في قشم كانت نتيجة اشتباكات في مياه الخليج الفارسي</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/82414" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82413">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امشب پایگاه‌های دشمن در منطقه شخم زده خواهند شد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82413" target="_blank">📅 03:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82412">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سماع دوي انفجار في قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82412" target="_blank">📅 03:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82411">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5Up6mFGhsuDEMZS-pTwnBSBTFh_IFVnCNvQVIvxohmZCx6OaZv36XmpIHUxNOn2CLsgS_t0XrW6Dgqh2ZkvboFz-jrj0a_NwO-xF3OkKoI576N5ENsG-j8-7kGonyr23J0DA-QwjkUfEHea6dnUNF4cJvj4WF10ddjoRpb0qbaDqss20L3ILJgP1_F67kExG0VuBh7btSVYVRjZSSS3whZQeJw_2MZyK6WWsOdvXp9h6AH749UErZniMI-AlnTgx0h0QFijZEPlibKA-X4is66dT9fPTREUQVx83_ahkEW5qe1JKJWI-WUWz7DIz0nh0lXWCx1vlDdkca2LwYybFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماع دوي انفجار في قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82411" target="_blank">📅 03:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارات في ميناء سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/82410" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
وزير الحرب الأمريكي: لقد اتخذت إيران خياراً خاطئاً. والآن تدفع الثمن.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82409" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4npElzHKSIRRI-PLURm-PTGUkXCz9-zqsk_bjDjbzbYIKOaeTjKG_6t9viZFr_SQ6PjbyRvz0VH39NVykgerCT8FclIasDXrO-vA2K5uezOXrG4GqGOTjN0KC_T9QRxDEFiJ02gUkklaOSrIEax1MZPYx4DZfsvcs_gVr7IkKcE7TiE02lJ-KzLf50l8FBppxbnKbFFcjops-EW4enwzPqILb2z7HZUBcu6owth5oez3rOaD6brKLWcTm5vEOdhKMMJ6avRczON8Ge2vZ-IYQv8E_CnsUUqgkXEeVD4EzsZR_EUTfZQg1K-cNswHFG_ARDjlVfNg99WE1b7T6-DRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الحرس الثوري : اغلاق مضيق هرمز حتى اشعار اخر. بسم الله الرحمن الرحيم، قاسم الجبرين  في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.  قبل…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82408" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82407">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
الجيش الأمريكي: ‏ في تمام الساعة 7:15 مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت قوات القيادة المركزية الأمريكية الجولة الثالثة من الضربات الجوية هذا الأسبوع ضد إيران، وذلك بعد أن هاجمت قوات الحرس الثوري الإسلامي بشكل سافر سفينة الحاويات "إم/في جي إف إس…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/82407" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82406">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مسؤول أمريكي: إن القوات المسلحة الأمريكية تشن ضربات على أهداف إيرانية في منطقة مضيق هرمز ردًا على إطلاق الحرس الثوري الإيراني النار على سفينة تجارية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82406" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82405">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات جديدة جنوبي إيران</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82405" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82404">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوي إنفجارات في مدينتي بوشهر وكنغان جنوبي إيران</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/82404" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82403">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوي إنفجارات في مدينتي بوشهر وكنغان جنوبي إيران</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82403" target="_blank">📅 03:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82402">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوي إنفجارات في مدينتي بوشهر وكنغان جنوبي إيران</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82402" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82401">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
اعتقال النائب السابق طلال الزوبعي عقب اقتحام منزله الكائن في منطقة الحارثية شارع الزيتون من قبل قوة عسكرية.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/82401" target="_blank">📅 02:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82400">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
الحرس الثوري : اغلاق مضيق هرمز حتى اشعار اخر. بسم الله الرحمن الرحيم، قاسم الجبرين  في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.  قبل…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/82400" target="_blank">📅 02:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82399">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
انباء متداولة عن اعتقال النائب السابق طلال الزوبعي في العاصمة بغداد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/82399" target="_blank">📅 01:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82398">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b28dfe9bce.mp4?token=SB4oITiYVZ_1DRs1w54SSfeilUeNibevT5_fJ7IvwEVVeJ_kgibCORIth3GuEw9D9wCRVkpnYeQ3FIF6SkfWZFqiPjTQe0ysFCzROaH6IX0tCRsim77tm3fzMImE0o1hCHfLgtuEvxoDkh6DGasIjr0uSV7MR6ABK03FmrfDLynrq46NU39en4i0UnXu7bc_jwIcFdUV6r8w_1rKHhUvgOe8r7JfAfm4MnDK7KdDDYOsoJlnlRAM8yf09eEvosPScN6sv4dgMQMe-Vm_ihiZ_SaC_tDZ-Q0L0cGaAHkZV6Zqy3AdK_Lx0-Nd15S9Yx4Ek5pVyNd-seKs6i2WR5OwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b28dfe9bce.mp4?token=SB4oITiYVZ_1DRs1w54SSfeilUeNibevT5_fJ7IvwEVVeJ_kgibCORIth3GuEw9D9wCRVkpnYeQ3FIF6SkfWZFqiPjTQe0ysFCzROaH6IX0tCRsim77tm3fzMImE0o1hCHfLgtuEvxoDkh6DGasIjr0uSV7MR6ABK03FmrfDLynrq46NU39en4i0UnXu7bc_jwIcFdUV6r8w_1rKHhUvgOe8r7JfAfm4MnDK7KdDDYOsoJlnlRAM8yf09eEvosPScN6sv4dgMQMe-Vm_ihiZ_SaC_tDZ-Q0L0cGaAHkZV6Zqy3AdK_Lx0-Nd15S9Yx4Ek5pVyNd-seKs6i2WR5OwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر
🇮🇷
ايران تغلق مضيق هرمز مجددا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/82398" target="_blank">📅 01:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82397">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
الحرس الثوري : اغلاق مضيق هرمز حتى اشعار اخر. بسم الله الرحمن الرحيم، قاسم الجبرين  في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.  قبل…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/82397" target="_blank">📅 01:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82396">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
الحرس الثوري :
اغلاق مضيق هرمز حتى اشعار اخر.
بسم الله الرحمن الرحيم، قاسم الجبرين
في بياننا السابق، أوضحنا أن التدخل الأجنبي وتحديد مسار السفن في مضيق هرمز بشكل غير قانوني سيؤدي إلى اتخاذنا إجراءً حاسماً، وسيعرقل عملية زيادة حركة الملاحة في المضيق.
قبل ساعات قليلة، تم تجاهل هذه التحذيرات، وبتحريض من جهات أجنبية، حاولت عدة سفن الإبحار في المسار غير المصرح به، متجاهلةً تحذيراتنا وتذكيراتنا بضرورة تصحيح المسار والالتزام بالمسار المصرح به.
وبالتالي، تعرضت إحدى السفن، التي عرّضت الأمن البحري للخطر بتعطيل أنظمتها، لإطلاق نار تحذيري، ما أدى إلى إيقافها.
ونتيجةً لهذا الحادث، ونظراً لظهور هذا الوضع الأمني ​​غير المستقر بسبب التدخل الأجنبي غير القانوني، سيتم إغلاق مضيق هرمز حتى إشعار آخر، وحتى انتهاء التدخلات الأمريكية في هذه المنطقة، ولن يُسمح لأي سفينة بالمرور عبره. ثانيًا، إذا أخطأ العدو المعتدي وشنّ عدوانًا جديدًا علينا متذرعًا بهذا الحادث الذي تسبب فيه بنفسه، فسوف نرد بقوة، وسنستهدف قواعد العدو الجديدة في المنطقة.
وتتحمل الدول التي سمحت بدخول العدو الأمريكي الصهيوني إلى أراضيها مسؤولية عواقب هذا التدخل.
والنصر من عند الله وحده، العلي القدير الحكيم.
الحرس الثوري الإسلامي - البحرية</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82396" target="_blank">📅 01:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82395">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
انباء متداولة عن اعتقال النائب السابق طلال الزوبعي في العاصمة بغداد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/82395" target="_blank">📅 01:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82394">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a05d62e2.mp4?token=sdZ7BGDqWuYZ5EDrIodu-bOEk4RntA9O6a1oFFIqNIisgMCpTQOx5rebPbNwrDtR2dm5ilNaqF8fZaL9K0tvwKuTnoJ4rri_VRVI_ogkPPqldGYU5JH6QFEVayT1ONWhsHWy0diavYAAZ9eTN7W5VMe3YKlWpr8MnefEuhpM_mjpYKTMIC0EHr4qOFhbzDK6FaVdKVvW4Dloh7hGJAHI78BQNMjXaX_FDO9fiLlz1i6kwexWsr1K69s_Uq88XA48nZDi8ekG3t1XZKRSnqDhd_Nlyw5ua2vA6hHbq_LuB12guLkQEaPdsoBS15y2fBky0RsdJDq3Dk8VLUVR3zR2BDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a05d62e2.mp4?token=sdZ7BGDqWuYZ5EDrIodu-bOEk4RntA9O6a1oFFIqNIisgMCpTQOx5rebPbNwrDtR2dm5ilNaqF8fZaL9K0tvwKuTnoJ4rri_VRVI_ogkPPqldGYU5JH6QFEVayT1ONWhsHWy0diavYAAZ9eTN7W5VMe3YKlWpr8MnefEuhpM_mjpYKTMIC0EHr4qOFhbzDK6FaVdKVvW4Dloh7hGJAHI78BQNMjXaX_FDO9fiLlz1i6kwexWsr1K69s_Uq88XA48nZDi8ekG3t1XZKRSnqDhd_Nlyw5ua2vA6hHbq_LuB12guLkQEaPdsoBS15y2fBky0RsdJDq3Dk8VLUVR3zR2BDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
لمحة عن الذين يُراد لهم أن يحلوا مكان حزب الله ويتولوا الجنوب اللبناني بينما يفرطون بأوطانهم مقابل لا شيء.. إبراهيم الصقر أحد مسؤولي حزب القوات اللبنانية في تصريح له: إذا دخل الجولاني في حرب ضد حزب الله سأكون بجانبه وسأؤيده (
صدر البيت اله والعتبة النا
).</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/82394" target="_blank">📅 00:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82393">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
تقليص الدوام الرسمي في محافظة ميسان لمدة ساعة واحدة خلال شهري تموز وآب، ليكون من الساعة السابعة صباحاً وحتى الواحدة ظهراً، بسبب ارتفاع درجات الحرارة.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82393" target="_blank">📅 00:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82392">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo2wEOHvVO3MMrJdrrJZuizefjIW5Ok4BSUpjXEQsVKGyR0RX3lPSsLQvxbAeTYsd53RdQ8oVAYwHgIyZSg9aV3VXDMwYx3ex_K_o5kkuhugP34fBHveWxZsd4zhOil43AJvYnPLQ3wrzxBTCkLYhYmyy9GxzME0YlnrQqeTDTwyxY8yLpxW0wWEkWMUJVx4n5gvLcu26z_XN3VchPz3mNkMVmUzmw5kEspb6Nn3e_V9Z3CRnHHX-wWNaYu1PxNf7J5h-Pd4Ybtnj1YVGv1loq9lWIhxlbL8lz7NIlyB3g5AQ4BUfQEfTj1EPTGU3JYwAInmHRcvr5iKi8MM_UmVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
العثور على كدس قنابل في منطقة حي العامل بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/82392" target="_blank">📅 00:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82391">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انباء عن نشاط دفاع الجوي في محافظة اصفهان الايرانية</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/82391" target="_blank">📅 23:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82389">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏
الاعلام الاميركي:
المقترح العماني يتضمن إدارة المرور عبر مضيق هرمز عبر ممرين منفصلين</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/82389" target="_blank">📅 22:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82388">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTUBm-kKnBNh9j7EkjHQKmdj1ME0g-LIjo8Xay-S1RxI4mkSKdWOKOuKymCucLvdpnZku-jaF6arxo5-0IlKM-WgPo6Oq95aY5SMC2eY2fCn15bSoQvd_gbyt-4CNhh_i_-jN3Ll5zVJV7KxEOiqb64llmpfmno3voUqxXVr99Blw094PSHIxai-c8iTWjQ26zFx4eOFdfpnAoOCdf39LV3TdCV1_XBc8kRLWJmCkcOESzbIg7W0nUFCEYFs9rcQWR0XlDY25kdPkaY46zJqLcZgIF1ICLvCWcvTVsxVv2E0sqyMN41OEeqONa9qdrJS_ywWz_1RYSF9ECk39M6uUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
عقب إقلاعها بدقائق..
طائرة إماراتية تطلق نداء الطوارئ فوق خليج عمان وتعود نحو مطار دبي.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/82388" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82387">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🌟
🇮🇷
‏
السفير الأميركي في إسرائيل:
لا نرى أدلة حقيقية على وجود جناح معتدل في إيران.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82387" target="_blank">📅 21:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82384">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
🔳
وزارة الخارجية العراقية:
تابعنا حادث إطلاق النار على زورق الصيد ووفاة الصياد منذ اللحظة الأولى لورود المعلومات بشأنه.
سنواصل متابعة نتائج التحقيقات مع الجهات الكويتية المختصة واتخاذ ما يلزم من إجراءات دبلوماسية وقنصلية بالتنسيق مع السلطات العراقية المعنية بما يكفل حفظ حقوق المواطنين العراقيين.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/82384" target="_blank">📅 20:09 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
