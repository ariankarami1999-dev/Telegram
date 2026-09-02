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
<img src="https://cdn4.telesco.pe/file/tgU8LwFP6EpBCUdXp9ZTAftuqxZIutNBl4AvGuIIvg-ZTNL6hF0FpHtN7M4ZU__ZIIJiscDibUvLe1riOyMg39eS7XyAvN628uT1DYMfiKsCNQ_-1g4OEvJhfnRjwYPiSlHFC1DN8FV1CgK5u_BQKr9e4ts9As62algpIGRWNPoyphaZewNJR5b_oY0mtjvENjRTP66CjtYy631UbDbO32hW2UFz1XvWFeRaqAHHCm6Ruz6Wur4I1_B-Dmx5Wt1UrevpSTymFWpjbUJZWMjdU-A_zAAi1LDq2ZOYuh67d3MMG45F-zSG_Tg00LgD4ENItTNGi6LFOEfIiSqyKsQDxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M714M__idmOrh_9nZEqGJAciep9lVpqMRQzvBcmPqKirNQ16egO-sTpSKjpOV0T-8Jf35x6qmix0IKmnjNSUo2MtZ06SHLyXh4pqkFUanPs4zNKMacLlRUYrc86GIDe_jKpLdcfYRV1gAiObCHMWIoNVU2L9THTBpLipP8rKh-9g-haKTROJbsrQ0Y7Cv3qFlkRwUVXJyjuqmTln1P0GA8fC3NbHahi28d4WZE72FBfRLRIwlAOQfVhhietGAlrFMHv18kL3DOMRo2eydN_Yj0wT2rEAwJtmTJ9CcVLBhHtphDOELRDwQwDeoIAzE1NG18JsHIpngIs5fgcJ7dNNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHVqIEElGhXUJMSvojAMBjW4mU7WbfbTnxWCpcNAhdKnuECQMbiWbLNak_ZitJ8_IP3TZVFXdqJ_Aa3B8bJWmYgtrfyXF8y2c2BN7CGMiUbZ6k0F37X6a3jHSqxoUQwluMBIuL8QRHJPL-o3Vyltugq1x7hS9AoP4NGh645mwStDpskostSQsjSQsdlHgc4-37yb9fadkbavcIF-s0ZghZMSkmkHjQGnANgyNFpXuBA7x1YU4SJKmyQtCqliVLxFm8yFGo_yPg2xWoqsysQNuLO9UBC10c2bubsPQBcfSwzRRs5_GY2e43XyHY_i23WRjQsbZOXOfI280NkxuJahHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IV_8tOwOqK_UbPj1F40WrUVaFEGNeNSMZYO7SGzOX7Bll0-K_dwwXMWHvWJoTwjCT1udy5lvFnl0xx1aKKqGBlf6WWNAl6uyDqQxXmKwFb07p01gN9E7NLuQT_XAkFqxSMR9t_RdoepMiNPvzmSM2Xw4QabgopAAjYDa6KSdkkXbEha5bKcrfAfJ1RilLLzmUy4G_GJWr3DyxWMnZjOkbVOVK1qtXwVlynjj4jRIdSLM6fkH5g3aWqn4IL5tWDkXibWnVfLVHnSFpj4Jmpt_TBIelZxfdT9zErDsjXq_cJ8ox3Bxrw1Swun4oManFtZNfbPLcOLPU7dw-368yxFICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKGqOepbnH7NY-VLlwItp3EQhBrE4ksceVGVmJOsVPUKspEKSyBn54POI4zd5VTfYTKju1bA1F9lm8EBSQCfvNiGRvrBmG4JonbiprrFR-SiXgJDRGMsqT53DRmMaDWuAbKq5xSf4DYaIzWIZPSYew84JckPKmtCFhDDa08ZzminwIJaKJvEn0v45JqTUSzi7JjjHWgxeX6_z8cCb6WLpoJCkV9y5cPN1qrk0jnBQ5xIDIrd4F2LNjWOypHEszu3xjybh9OdvKWozvUWn7pNN7B5NKwJ61DvgsgHPWgFOjovKqZWvb7yaTepK05zg3GtoDAzS8yIu1s_L_jSvjusbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o_CCrVqo6cR61bj7M73zL46GySBdFMgvAtKEFSEkEe57BgR53iZHP0shi1f6gc488vpJuBcEuNo_9M8bu-ft6TEfI7csGtnHpVdKZ-IslxXoolzf7aKiGJrgafDPE080Bu0M_X16u7AY0GoHxlUcjyspbE9mVqMqLka1bw2yacI4Xufq4V1TVgLh5_Zx03zxqUSFIF2gCBSXNJP0tHB2SP5tQbMrDE76gNpKzSr0qmbkRDmBZVaTXA4iAf4PzxWSmQrjT6PBPdBqNk-wgExaCivpUgzheVle6ghlkrctWc9KmSUzjWb7YUkQv5L-BFQsql1V5tpx31KzztnVX8YMgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o_CCrVqo6cR61bj7M73zL46GySBdFMgvAtKEFSEkEe57BgR53iZHP0shi1f6gc488vpJuBcEuNo_9M8bu-ft6TEfI7csGtnHpVdKZ-IslxXoolzf7aKiGJrgafDPE080Bu0M_X16u7AY0GoHxlUcjyspbE9mVqMqLka1bw2yacI4Xufq4V1TVgLh5_Zx03zxqUSFIF2gCBSXNJP0tHB2SP5tQbMrDE76gNpKzSr0qmbkRDmBZVaTXA4iAf4PzxWSmQrjT6PBPdBqNk-wgExaCivpUgzheVle6ghlkrctWc9KmSUzjWb7YUkQv5L-BFQsql1V5tpx31KzztnVX8YMgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJWuY01drZNVG8GPoMrii_P1eCcskbHS8d12ELYOFoG42S6CSBkoFtdx_K1bZFJwkfOx6EWloQU5LbztAkkaTA4eggBx-kiezZYuyhg4jCOpnptmYBXpEFt6dsQeBFqOzjRc4rUGMrSNrlI6v6SZM21lFrboMvkpqMcRL00IOdAMGWnsOuCFgMNxLu5Y1W8IKkD1LWpeTg_IZ6fPopOmq_4GiYh_RShRZqHIABRzkEqYwAaxhuThlsgFndWYYt5u-BH2uuPdu0pezAyBJnGbxi1DSWZwPA2tpSsgl2MznNYQ4ylwot9ZrCCpZ8R7LpEZmBaI83HSEd3qC5mIWIqg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP1ardfHXK_oA3UfPU5e43RYvcdW2SyappBciTUhcoBc47unluEIuLP2TzCkrSy-NBym8Gm9888b1akkgEwqEwJKMc8sCWgDsqmUzJ6yDxykiy7tv1OI2J5nnou-2sY3Ocjf5DkMuMhoQkq-r2rMg_mjiP2_B_D4HxqkJddDSv7JjvCJuWv8tB-95dVYKOSCqTla3mTrFkZbhZ6yRy9Em7W6gOM8FTnWCCa3jKJFzuO6SrBD25cw2CULYQ9rdnzTytgtr4r9vUVXBK5m_DCZQ-X7IxTR8YYXIqWWZaiouu9UvK_5i67auYbPBGevQXf9SSty3BTg_ckm2q0mZo0F6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=e1GnF_NBOrd9h4_1ohL5vGK3utWNRukG3tT8Yb9S7olexIR67vy7kJOtKBGNq3FJ0raQa6wAUew59JXZlOZ2BRCpxFgweRtjXqwcH4qqsSXeU9EKoVCL_Zd-a_xcFBh2JoAB9F0NbjcTzvzGf0_1hOtr5Y1yO6XEYsU7U175IVK1eLLt3bq76Xs6kdw7f7BJCyH1MeXtEPdLHu-ZKq9vuPFE4xVR2_E8mBAppMe2ayxEGzLnRjp5qhbtx9uSHlzG84UPVtY7BjfJcBkFw5nhzJShq5bm2wMpISVWr7iB2mXlJaFKWQ_SpU9e-tp8QX8HdExdd5EW_pcv6vToFfxpBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=e1GnF_NBOrd9h4_1ohL5vGK3utWNRukG3tT8Yb9S7olexIR67vy7kJOtKBGNq3FJ0raQa6wAUew59JXZlOZ2BRCpxFgweRtjXqwcH4qqsSXeU9EKoVCL_Zd-a_xcFBh2JoAB9F0NbjcTzvzGf0_1hOtr5Y1yO6XEYsU7U175IVK1eLLt3bq76Xs6kdw7f7BJCyH1MeXtEPdLHu-ZKq9vuPFE4xVR2_E8mBAppMe2ayxEGzLnRjp5qhbtx9uSHlzG84UPVtY7BjfJcBkFw5nhzJShq5bm2wMpISVWr7iB2mXlJaFKWQ_SpU9e-tp8QX8HdExdd5EW_pcv6vToFfxpBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=CXqMRIpIVFNgDfGf1NwIw1FGnXT9c5fSGk-GRS2VyV04dMVRUaBC7FZOw8T6m388glOIARc3ZtuLOWRy78ydwr3Ai8Tly5dG7oITICPoxZQLvOxkCNAcgkhKd6HY0lW0nWNjxvKPVeTOs42-gXb66vMQqwVfS67SSfh8oA1Ad6pbKOMqBbEM2DMACmlrcuKNIEStmv_jChPiUtQtIvNVyGVegSyaGgurqNNRVLO2CDbP7quJ5HF4ND-NhxfKZL8V1Cl8YSVFiAkZx-XjHT8_JLEeVkQhT8QZCkeHtMesUB-AHGswJYE5dlN72WdNalu9kw4zwkdfBr-wR9oSa0-mgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=CXqMRIpIVFNgDfGf1NwIw1FGnXT9c5fSGk-GRS2VyV04dMVRUaBC7FZOw8T6m388glOIARc3ZtuLOWRy78ydwr3Ai8Tly5dG7oITICPoxZQLvOxkCNAcgkhKd6HY0lW0nWNjxvKPVeTOs42-gXb66vMQqwVfS67SSfh8oA1Ad6pbKOMqBbEM2DMACmlrcuKNIEStmv_jChPiUtQtIvNVyGVegSyaGgurqNNRVLO2CDbP7quJ5HF4ND-NhxfKZL8V1Cl8YSVFiAkZx-XjHT8_JLEeVkQhT8QZCkeHtMesUB-AHGswJYE5dlN72WdNalu9kw4zwkdfBr-wR9oSa0-mgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2TIF47akLexrcJ1Zoxo6b2mGdkHf5k5C5Z3J7Altx4nK6OA7j4hYKjVoeeDXaz-qXpSpaZNCvuEDZiz0d_FA-TPIchyhmdW28FP9FdklxhGRLYqbOVXMJjb0fQQSc8MFl1wWGMtV5NGR_oeXlB5Dh8aUGB-o1jCHnPG4fzMrJwBeteXAwNoSTWoijZEguaw34N709mKmvh4ScbNupFV5NKM1mP9Ge87VWOt6suytVSdXhC500RwcDDVxyq0q-3Y1taTGmAyEOvAQzu7ptS2GzMxItj3sjo1wnOAncf-ZvZOtp0ITps9afQeKxAtmd4Y5TpaX3HsqWZkmRAUZL3cBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azk7kjbX-yT8hksaPKomzhWQ63EH0VF8uyn_MvZjBIXt8aT7Rt_5pSpoP89uJrfVdH7XiZQIwV9Qqej6QLsmkTVIlmiw16NDTEFX0ZWvo-fROv50A4X73BYYZbii3Yl0aruQty5wpRwpDL5hyacHAtjp4D1-_t4-fLLaDxi3aBCJxxWMvG6HMLqxi7kfweiXr8-iwyLA3Tmlc9XYcgQF-MN-TSNmHou9swlt_fkXtcLWj0uoAkya2Tzbskxr_F2WDGG8Kr5-PUr3PKVKS8XRH5vCJOQt8e9s2ZWIM5GlO818ls1MUL5GSkkkS4UUjoMurDz0DGtN3jWH21M_9TYR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEPavcw8PueoZtosKxvoO9-PjpYyVEfP-2Oksy_Svx1YtV9DokbMRcKwKfqYDAFWR-AvVof65gUEF4ALo_X7rpjm1tETiL6dIHCmqW7F5MmzN9Fct-7EB-UxyOlzK5l1i73ym_9yCzNSI2tO4k4Anca7oqYeIvuJ6HVcQ5AIuhKUFcmp6yPGMPQgjImTlRA7tapNMaYFZfFMWxszmgr2BRWsQfAqCNhpsx-O23c6RUTuB1JDMPSR5GeCea4Dot5dnZt3_2FCjQ9YAaJlMHDixUZ5hLMVdxnQL14DCI1Hj51MqaDrb-ZwP9bFYxnegMPSpi3AI3CzofuY1qwNvrsykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjlKA8ORiwMUSyddX664AaUR94H-hEvcpNnVmtViEGnZNq5DGn2uycXkGwq7V4PdVnKyh-TznRGgKx-L4UJtEVbXX_w2gSddk_sedchFKc6g0G2lhhyrbfK0z-Ai5rIlhdixnBOlxaKamq5LwqDaqBZEvlKPBUSix4O0JYW69xcrGvc3brXjDn-zkqvrZpL4Xmf4Uet8ycat_gVo7YHtFy77w0eG-3CeypqE_--i7uWVsNS3HMH3xPKILndnW89eXYGav0ZCiwIVze_d0VFJuXtSWitZ9BD2Ar2hYjBCcrmhv1Bvnv-FAEI-LIvV53wQb4wTK0Mvc_fjQMmjhlZttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQJAu7lLL5imk4yaNFFpXNXCcNPNl0jT5rxuOTAph5j0ZygXzdaTKZq-XDzz1NunHKK4dTSmfh1ZAChziYKM4sstxQL1rRvCzp9g5_TgYmTLbi6Jjvp25wyp7GpoGKA8StKIoVqrxcgo-9ZJ5KIlFcRy-mv9jSPY8Yq063WirTwQ6J1FbmyQH7kLgBb2RqFFxc_JXOf5iutxF7Xg3yl8k6d7pfw-imCMDeX6ebEBnFgN9ngKynhOhYVswIHMCWt543-uCA3Q8Yv8T6X3_NEGp02Ts61t8eXun_FtdZTuCD6gT4UCVlgrbaXxYNNDvxmgR1NflE5kl5BN_sS85AAcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHTgMju5GVllQMAkRQ3hLmjoeNaaBP7IptJ6UKX_3yqdJvzikAnFMSm_siDkANoBHVvFusNU6zjCy37jma2M5A5mOCw_XnN3hOSv2YZYwK_n0UbNgMiZLcpQ0wWf3gSNDJeiT7p9cLIzfoiXWqXCIVYLfxkvZGf6xCRcjaXNTsG_EOPCT2JZndtgJmNLQWmoQp4PYeC9MEAvd4ZFY1QLY-O17BQv7A8zuKqd8ituUjmAKlYRCIvopXVPPlq9dWXVYtYvpPFLFWt3hpt-11zhk99vF5IbFUIQX5zSle4bSBed5b5n7rz8ebMCPi4H2GBzC3t6fMm3CvmgInRnG1lvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRPWdmj0S9yDYirUkzq2xoYF4TK6i1-2_P8_gzVxlNnAulOPu2NTJSRHwnO0RUZ5VqXIbzHTnIVSKCMzIoqepdOagppcnTfBoYS0D12Hx0GAuieu53IvCv02zgpRUsZkKNG8DVKqO0xPcEOGZvWruCGGMWiIy4xF1wBoHNKS4HFcKL7XVtklkUxsmgOCvvY0Pzxq3DFZSUwJ9Clnz5marhn4QsL5Uqro6Ur-rp7fbac6Wf9nXbF2ggWgKRg2oDn1eJeB979zd3hWqZgR855DaOcvfbLKQLAqfq06gm0leAxPY401NUMSdxqMmtKdfod5tOceBb9Pi0BqqAlbGoi2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzbKhhUyykCBuKGyjSkYjZhz4NZT7iU9wquxgjPtd7nPIJPe-GI0ufOgnhT647kzJJzLqnTN9lnRzalq7sL6ZTf-bQessZ-4zB4XCrmAI-b2BbTGvaTl1OGG6SafGnkw4JOBu5x76Z54_919PCgdJvSKqkHNoKWRZnYJr_e_1tRc6-ceIn_GXjYTMilDl7LxK05IZP3_Ut4Qw_GGep3oqtLas3k2Eg_fE6j6NRQL3DLyWPKY2_22oxvfjAig-4383RX2arPHodv7ygGTbkhQNA3zX4Ix1ZHsQE28-VAjMrnpJR3e5XatB-uUGGW0qs3U9phvrfiy5KGE-o3Gg_7KnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Kl-BpG5EpS3he8Bd_2a7ocyNE2MGDiIk9dj-LHPkbeUOv5aV9XgyQxGzurh5-j6M__1mAYzj9KFqbRwesScCCmceqSzAzWgMB-OCR7Qrwj7SusV7G10Dl6aOMQjN-Myjnc5P3rqHcNfQBh5wUG7HQG9VYEkBqL0BQ7EQU6BKXjfb2WiMg57fSY1KZwAdCI6h3pRY38TEtKB3M4U1b9WrPhXEV9zBPXJg9rClUpg_LteWiEhfTXzFyO6dQQesTNik03QPRmzf2HAf0B3pHKb5yZyjOKd1b7H8RFffSVEvdG-orqDgdnisY7B6uyZCNqHCCXtVcPfUR1OQHBsQhBjTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=Kl-BpG5EpS3he8Bd_2a7ocyNE2MGDiIk9dj-LHPkbeUOv5aV9XgyQxGzurh5-j6M__1mAYzj9KFqbRwesScCCmceqSzAzWgMB-OCR7Qrwj7SusV7G10Dl6aOMQjN-Myjnc5P3rqHcNfQBh5wUG7HQG9VYEkBqL0BQ7EQU6BKXjfb2WiMg57fSY1KZwAdCI6h3pRY38TEtKB3M4U1b9WrPhXEV9zBPXJg9rClUpg_LteWiEhfTXzFyO6dQQesTNik03QPRmzf2HAf0B3pHKb5yZyjOKd1b7H8RFffSVEvdG-orqDgdnisY7B6uyZCNqHCCXtVcPfUR1OQHBsQhBjTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUTjEqR2Ls95AwNOkPrdtZOUnqLUcLJiX7p8KmDzO5U9cUCzakO_2ApcP8zWyYW2YkG8tDi0CuIaKHhKmejnqTWLuFE-PNzCL76fsyZMq2MxMWUD-bJe4DxsZ4HBscTsJwajh1wijsLCjAlAjsGCA2lE39WXeiS5v_R4poj1OOf56jG_MebFBXgEQUqfExpnnZ4gyP2yqkstilaTcUSldQX0jno9WK4pg8kGTJWMxwDjdnLNEtGLF-GIQU9nMQS8yl91EdIL8uJGboT5xBLn83BYo0jXpHlsQVSsJ_FhvsVrNeSWjgOHb7aEtRVkp9joIYKs02tubhqAuwvDJ7L-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=BBskIGpMNbTJzpucA2G72upeAkn39EIcP3hPHXrbGyN0yJ1UmJ_Inu2R2tKkp4wYaOxD7BhB24tBWzaRjnJNzHdFYWANrFXnTpPqTVtbNEEX05bKv1pTuUFdFj0DjuSeKinNUkfs42VYqFun4OlRQ7IC2h1A5NtjUhMtmAHDMolURqyAG_IQ1L7mJTN1udwEnli2H1z7eVl_c9qW_p5PFZarD3MwdjFGUByAGPYOFKc_gC1IhnSc0fiYv6OxqkdYISnz_I8ifh9N38cQ3vvT2UNrFiJg6IWgjmQMvdf1OBnBwz0k24IlNc3936EUHEXflhkxqGuJG6rlbL1d3NODww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=BBskIGpMNbTJzpucA2G72upeAkn39EIcP3hPHXrbGyN0yJ1UmJ_Inu2R2tKkp4wYaOxD7BhB24tBWzaRjnJNzHdFYWANrFXnTpPqTVtbNEEX05bKv1pTuUFdFj0DjuSeKinNUkfs42VYqFun4OlRQ7IC2h1A5NtjUhMtmAHDMolURqyAG_IQ1L7mJTN1udwEnli2H1z7eVl_c9qW_p5PFZarD3MwdjFGUByAGPYOFKc_gC1IhnSc0fiYv6OxqkdYISnz_I8ifh9N38cQ3vvT2UNrFiJg6IWgjmQMvdf1OBnBwz0k24IlNc3936EUHEXflhkxqGuJG6rlbL1d3NODww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=gLLsLlDxf0OQh_MDpADuIXsx1Cusls75OxnnkpzoZQu_2xQrIDTOJiRak6HPNHZWhN8_5QI_SvAPRjTBj-5mHmg2cRJ_Q8h0xyPtLOqk2uXyteTe4hocGx5vce3HkVkljrBWyg2P6jw_HfKo4Ooht2_FMBUD9FHZbIO2T7ez4GS5kYA9pqLlmxnUY5hokmXCW9gZ_9RualTLF67ZLz-nPingAbAUfBw_nlhXa6xSmHi3T19lzGuhvwiSGFVT6DHOoQJh8py6f7Qzj_i_gcwhJ-zsYKcZokI0y6x7t2IJ_WLs0dM-C22Ln8N5gbv60baGRmMf_o441j4-E5fsCupwKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=gLLsLlDxf0OQh_MDpADuIXsx1Cusls75OxnnkpzoZQu_2xQrIDTOJiRak6HPNHZWhN8_5QI_SvAPRjTBj-5mHmg2cRJ_Q8h0xyPtLOqk2uXyteTe4hocGx5vce3HkVkljrBWyg2P6jw_HfKo4Ooht2_FMBUD9FHZbIO2T7ez4GS5kYA9pqLlmxnUY5hokmXCW9gZ_9RualTLF67ZLz-nPingAbAUfBw_nlhXa6xSmHi3T19lzGuhvwiSGFVT6DHOoQJh8py6f7Qzj_i_gcwhJ-zsYKcZokI0y6x7t2IJ_WLs0dM-C22Ln8N5gbv60baGRmMf_o441j4-E5fsCupwKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P87EUKhTixSh9xcJxFpUPLmbikc443YdMkaLMDjL9j5RU3-Q1J3NdHLQ5NK-CKECOmMMu0MZ6UvBwEQtsmTrJKUhH6tnyPpo5GTZy1gvfTieMYKg80drNcFfDeMzwtRVeFKccLXEiscIewdVyE3nFBSJ3A_Uu7S51Go_yzv9FiZ6gMKsFv09jSeXWqYe--cHeJ-grWGr9X-sxWBT8AxmZLLHaqOdypN2H1hx0HKWWfE64hlle_yB2OC7k7fmipFk_7oemi2iSNKQJxbzZm_yLTmRAn88jCCccUQBa-2WcIvxmnqknWHy_FSTmLSFwqS1MU-su9r1VE8H2cJCXe6iqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNfW7vbJr0r5hkXL9PQGHGNjIpvKMxR3ONEY3n-DFt6U1_KJ9CumJlX1OMKEu-GIqv0Um_xMbdI1AGOac6-MNxkAb-DCJfaGiXags1A7HKFz94Sx3okMtE1pb5Q9rZa9h4Wdc2QOQYVdEUALIfW_j4c23VtI43wMvit8cSpCOiQ_IE_-nYHkvKElgmJ49egglSN9wyzNllW2kc5RlVpscfLHOrFFGFvM0HlN9J8KyaxxF80KtlPStSFnXZf0HvYEKBam1fgM3XpkyxNigyZBBj6lvegzPwiLNLPt0tG8tS5xkNCOEtKgWr1IcZ2l1MqM9mdDm4Tgi2FYJrwOQ0_DmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=FYUO9Cov66_Dg3Xu1SLSM683okBiMfOTrUS6aZxNbZvl0qwf7YAKtc5qjuZYd5bggqfgPXlShYaoIel4rB98leik8FKUBPYxfUV1bB73nEk7VN9W8Nk0mPZt5c8E103jJ9uHkh7hMKyvGfXJQU9Se1BOlHbhx_6nVbqbmMBjPlV_eDJ2iDYKSmYBO4PbHHyNxsUrjO1_GLHe7UMOzJeNM4XG_JWn8ClAF6mQsCklpon4A35k2n0WSBujQz0bdWtxm2M60d_y9bVFqgziVntjmZWg3vUXCKtn6njWqgVq6ZYc8cr-RlXGRzwhtv2qrvTD0RdXz30HOOUaY9CPeL-vcF8JFMFDhicG18amYEt29WwieQVUqIxMx74DlDQCFvItlnbqKijbqDGVpp9SsEWohu3qGYw8FgQDNQxg5r98YGjxJtqSDmw9Kxh5bHIaorrhoMQO0dbTYxTKT-CrJHrH-LVj5LQ311K9_2wdwIFY6-2FDt39ncPZBlOlIWtDmIwH7sEbd8uT1n-WqUDLF4oSix7TuDaFZSgIQ11BkXksHnHAMIiFJ2HX5d7Y8iElQpQhLr9szHQBE-a4Awk0pvkaZhS8oBCJTnLN7JEU8hSfL3tGnbIoFuPPVx4m4W_XtBcxmwIhW0DkycmLo-VRKAQfzcFPAktTmq0chyciLnpITqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=FYUO9Cov66_Dg3Xu1SLSM683okBiMfOTrUS6aZxNbZvl0qwf7YAKtc5qjuZYd5bggqfgPXlShYaoIel4rB98leik8FKUBPYxfUV1bB73nEk7VN9W8Nk0mPZt5c8E103jJ9uHkh7hMKyvGfXJQU9Se1BOlHbhx_6nVbqbmMBjPlV_eDJ2iDYKSmYBO4PbHHyNxsUrjO1_GLHe7UMOzJeNM4XG_JWn8ClAF6mQsCklpon4A35k2n0WSBujQz0bdWtxm2M60d_y9bVFqgziVntjmZWg3vUXCKtn6njWqgVq6ZYc8cr-RlXGRzwhtv2qrvTD0RdXz30HOOUaY9CPeL-vcF8JFMFDhicG18amYEt29WwieQVUqIxMx74DlDQCFvItlnbqKijbqDGVpp9SsEWohu3qGYw8FgQDNQxg5r98YGjxJtqSDmw9Kxh5bHIaorrhoMQO0dbTYxTKT-CrJHrH-LVj5LQ311K9_2wdwIFY6-2FDt39ncPZBlOlIWtDmIwH7sEbd8uT1n-WqUDLF4oSix7TuDaFZSgIQ11BkXksHnHAMIiFJ2HX5d7Y8iElQpQhLr9szHQBE-a4Awk0pvkaZhS8oBCJTnLN7JEU8hSfL3tGnbIoFuPPVx4m4W_XtBcxmwIhW0DkycmLo-VRKAQfzcFPAktTmq0chyciLnpITqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBsYLuD2qkWJQPFV3VsCI9Z0mPYW9eNJtrAIEOJJzgTT1e0xz5wvvyN2JPOShDV4ow3l51QIM9oxuW8xLbof0naKaX9N5fXFnCTY6H8yvMFWKQ1B6J4yXQJ2HxwvrXmy1JYIQM4CufaV0qu04WOMfqs9suq_Eyh9QUYztHy7kdTmblCmv7CQbNYGlr91bMU0hAOtLPif0wcj5xtS1sEt2K6MFJnORt7w1CzTdlPIaVtxrxPd4frodILP6Hlc1rzQDfzoK08-Zn5BZAgV7uGpHw2YbMpmmxsn2UCR4NEoQTLESr_hswbcyZc_8g_cwp4RgVukLs-cJ7E1EYbOt7ok7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=NtZSIw-8lC4ZSqtfFh0so4bGRpWJf8HaFvrAWOeBXOeTsAGexV7pr8jDgk6BGpcDuihwmfB1DgjpJraKrTjhJcJxvDnpQeMcLvqP6b1GPcH4dt1Q7MER1VVdzpfoX8khulP1ezNi5QbiuUIAnZYupEtbrmMAMT-08c9QzaExjhJdupuSR842Tc9r4ZxDGu2yE9OCrt9QMfWhW-gyYcVeIi2KDy4g-RoGQTalns56Q5XWyyYP39Z1k2pmPl7x0FF5EsAvdNV5wumuA1LPGmxEgPCTXtajonwknnZ6SEF_lP7w2_XFwrYt7i0pUQvaQitUut2ZELRQGrmED_-DhRFtVAKOnJ9ooxWdn9C_999_C9ud0dbrQERLUe2w_1U-7ybJ7-n2lOG7Mh2hZ7HyaQeaYFg0fgOCrAl7fk0BC66vMH4dTWEURT-G9VCt8l17XhZPFTZns-VRINoNlVmoa_3xFThXlENqGS3aAZRyh0Kj-y8ed9pHO1goI4AlQ_kgmjciqd5-vpbSMd8RxxLb4bg3ulIlxTTsTH2XVe_WkEioKyGNrEJ8Pc13sH4l28VWpp65T86ZZ9wl3Kmz5GTzUyyAlrmJvWZse5tc9ymUjMd2plsB6b8_vgblEAfUMKmXkNnlULR-bzflwnS4ORdZuIGhJqvk2si2uIWEW6jv_n9efBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=NtZSIw-8lC4ZSqtfFh0so4bGRpWJf8HaFvrAWOeBXOeTsAGexV7pr8jDgk6BGpcDuihwmfB1DgjpJraKrTjhJcJxvDnpQeMcLvqP6b1GPcH4dt1Q7MER1VVdzpfoX8khulP1ezNi5QbiuUIAnZYupEtbrmMAMT-08c9QzaExjhJdupuSR842Tc9r4ZxDGu2yE9OCrt9QMfWhW-gyYcVeIi2KDy4g-RoGQTalns56Q5XWyyYP39Z1k2pmPl7x0FF5EsAvdNV5wumuA1LPGmxEgPCTXtajonwknnZ6SEF_lP7w2_XFwrYt7i0pUQvaQitUut2ZELRQGrmED_-DhRFtVAKOnJ9ooxWdn9C_999_C9ud0dbrQERLUe2w_1U-7ybJ7-n2lOG7Mh2hZ7HyaQeaYFg0fgOCrAl7fk0BC66vMH4dTWEURT-G9VCt8l17XhZPFTZns-VRINoNlVmoa_3xFThXlENqGS3aAZRyh0Kj-y8ed9pHO1goI4AlQ_kgmjciqd5-vpbSMd8RxxLb4bg3ulIlxTTsTH2XVe_WkEioKyGNrEJ8Pc13sH4l28VWpp65T86ZZ9wl3Kmz5GTzUyyAlrmJvWZse5tc9ymUjMd2plsB6b8_vgblEAfUMKmXkNnlULR-bzflwnS4ORdZuIGhJqvk2si2uIWEW6jv_n9efBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru1wzfOUGSaCV5Q-eABBXm7V23HqzFiPALXMLwbuEOpquCmCZ67G7wN5Ay6S_NVfofhx8Jl4xuO9oj37VxfuxVP69Cz_HNeCbl7cDxh8gp2a8gZa__nN0-GD-6lGeGdwT6Fd7ZKV8GzlSbpBnhcJkqyFIB95n_JZvbGM1tAG0__jEOk_05AyR4GeHA-WwmAC-GrUYPl-M8TogxSOh-yCn7wZKd9tY7Fjp-XUedRyAp0YiiZE__1MzBffN6e4O7S6nTcSNvHHrnKwK7WCqmw8LkC7VObiHGKv4kqOvBScqcaZ2Vmi3iioqgOg54LHHS7qDK5QfFWl1_8cNtVB1jv7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWwtNaDJl-x8SY5boRjIldJHxwIEdcSB-BrmJ0CBA5XsXu9_omhQffZlLxGxJsLkZ6sgeoyjV0LKtpXDd1Xwrsu3JlC3eJn5RO0NFglCy3MH5WqDHWhZNp-dHcvAxVydX3Vau9KonA3jf0rNGI2uqA4loMZAeHTK_O5ra619s6kWS5J6fKuPmtmrJ6-dosD-0YJgJoNjqqHl4zUNAlQYBiZXtgtpMf74Awj1qJPYQvCzAvhtbZuaTL4UsDFJTD6dfX2B1SjSL3pxlEepgQf1uxKSI5u4sdYmW8EPcDpzs7Xf19EvY1ksTlFhH3NX3_b_x4eWGPEXMVl9uq5OOpchjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv1UuAaBRKnBXOPDr5gwB4L1AUduGkyWYOIa89-fr5NoSvoBFNHeCqSG8PDEOr02-gZYPlLLh875bGvxcL-4RoHAfIO8J1rO6BdyTqu55E380sGbCZpmzE91AqYyI43oIoRDgrTGMuYEBEdes_Sw7oRsA1cOzpmIGul49staHGZMGNG8BR7vlbGb-KIgce6pfYCHx3_oMiPY0Q4eUO_J7VUZ2BOqdAQvDslk-XoMpQOeN0-OXEAkrt-nTDMy4QothDITWAHMe22kOovyYUyEcQGziSXdes5PMhYgBOy1ZTkNjey_jhUJoH12WHHfgq9s8t44jD_WvN4__4ylfTjwQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz41SultiSCpkCC40v7LUjGBH3UJOoi2bmudfhfKiK_hkG8U6xZLdUaJ_xJ32bboNTMq8LT7cnMF5Jiqqs71xsARn9TG7XcbPR-X3CDhqf7nOMosxI0luHBHUql9D_4g27DVT0C0TIGmwu2WjxrKCKImbpYq8QRtj1yi6htrVDLlM9RwhcxgKxTOJxUTpNv06RHl8H7rEdsfBDrbP9wzensn7RkPEGZUZ6EyuMR2n7iqQo-SFRsFoBFVNnGno0yfN10q5-kC8RxoFWmnXuL_LusbxLQ2YyXGb8tdtOPftGALmbv7O5KLwa1FIyWPP0JvwzrN66Z8Xo-3_T2dF1SJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1F1MSLnFXoNSM1J0egojFE1N7tKUCHUdJ4uQwlD_XzpRAHyY4d_YcCNXgqTx3r-rfAAOy-fTEamTNxTqKk_w2lHVaSuMN0PUwC-zAEDqZllC0DG5pjqPL3vF01Mo8X27rNYPQbY56KkvBY6pH8SChd8lhnR49I_YUeY-5gVWtSZoWDxy28R1WZ6_y4wriplVPS7cE-O50CoLob5o3Iy2qgC-KRi-Mgfixil1HC2UQdsfJUB5UAPOk25FtYXYeHZbIJh8IkA2dLyM2MoNeRjN3YdStEBTK0KIPMbqgaZCQS3579S4zrKtfsngAxhitdf7VoXHPQFlWtxdpFOmqa6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcCeTis9YlwNCaeHYUnSB5LOD4Rv971qS2D_-FZmmuxTH4znwFbjVpx3xxJFMZKPZckvbXMkMniGo7VNybTq0Wbs2jdiiIUZFycY6saPZRVFG6eVkRQp9gDpR5-jSuNaFZJQywCtTyw6FJpSidqt-E8zjXmQWhnrHsO9LnaJr__Ar7ECfgnuaFugtjYp42pPeO6OMGmD8UsDf7Anu-4lBg7c8mMBYPmFVKNH7QwxNuHCWQ7DpSpWiYdLSU3lfd3tQTihhMbnzsVZ2VOmDxmPAHpEQ3rCuLieJXzNMdr42u1woA50H-9RxzFeCOGlqLThVwZhw8gWKcu5Yg0_sj_Vjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUdCoGUxzHhTe5ACrbb2U-BaiCWK9xsaZXMlCs7GLkX6aLnL6-Lh7QHkf5KweNVMuJKHhtjXsNmHY-AKEmPGq2rG8z0AbEH9GBtaJ_7R8g7WxWTLnGbb6VN2Nmx75oYJuX3-8xZDEcooUyu85wtoHOMthBzk0qdulvDuFtGnEHBOP7WGu1VhhaBdzb1_ku2z32Rdt3jykKn_oyHQk6rzW9ElJ7bF6CAmp5Lhiwxd2KLLySRdJGXg2q91U-kUz3Kd3EAs4DUXeBs2zKyWhqcvuCA8w7dGxYE4Ts_7LJwQnJQJkp71oj7znIeMNmlj83tgZbJK3g3n9Dqs5zWPMnXgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG7iGosLyrLLVSUPEJDxv7nFwcdLFZ1zX429yDGkKM1H8KTIgMHpHF3GWloezVtW7BJCjseMMsAGHFslRaB73jTYNAOlWPtObHDWsUExXrnC5tMFOOV-qduNlfyWLkMQK0ELY3zOQBm_gbTxzGLy33bf_jwb4zCOZw_Kv9FV-gTph5hIvvIexvik_ZrK8Hegipo04xsLUxWZwi1vW3EnfZF5eWbiCADtXWEw2TOohYe7gS0GARH_OyDugPTBUU8KEYcw9osmG67uz6mDYjg9XXauM5JFPUZpw5vQmt0N7U_YWoL9HyQlDeGjWuQl1JWXa4qR2SfDLdtPDRObOab0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzRWEwXYfwBw_FSuXVmDDLxE38tz1DeXaUMefVg_4mAQDGbTaM5NrxbuBjsF3XzXbLDYkfamyqG7VFmfyWydXlx4nX5ffcVNcXp1Riqzdf5FIEOV7pffucjdxtYEEjuVTAk1Je2T1TC9tJMFAqItkFyPoEIX-08gvUYMfvJqpdG5kQBP9UAjbY6QTXL0g1C0RO2RoNMsnwonjaTgE5OqHETjw97rjoeHAn6VtSD2UZznva6YQpDo50xOXkvH9C8trUP5Vydp9AFHXq_1xv8lxK_tYslpoUJUzIyIfkkoPN5HEEvHxnYDovMQpZdPXwKwDIlLE9bicuMPxU0RcohXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjSd1DzcmO7TQsncOIMBwVMZlhOstpY7ApfIicVb0HaNjTqdyctge8dEVDWsZ0JMtg0qgdjz1ICFzGLdcSHMPfHZQwAQoAodEt1OQRNmBnsIuqah4IFkuX7euDFc16pmA37dss6oZzFgs4iHbr95tNBOHjmuk5z6orcQAyqPMXGT9bD3cMDifk67J-DSngdw9ioHj-icTTjBXzjIa2LjfSACiGxZw67J6WOudb2IzwqmAp4zdFwwuKRxbB-WzG-4C8A4GtEY-XSZLOX7JoU2R4JD5dHmXIC0WxQ2jurwlVVTezJ4RFe3P0e4BwS4UG_cI9d9qvRoXB5k9lMKzKggGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWUGg7yzHLkgAkJFoAhQ7unDwhBNnkdFpAyTUmw1PaSXkyoV1OkwRo9V6hlVmp-Q07Z56C659046L_kb0kKmbIRAcD03n1OI5wYnYGhUNlqSc46XkJvcyyVSpeKZSB-jEAXElOpDmmHibAbAlmcyOFlI-WirhXgv9uItlxvnif3rAO94LP9mcmfLREUvcepSMGwatW4AC_XEbvxeSPWcSQFvORjSUpcso6ib7kcPwjbw1I-PaYekTnyCHS-n6O6Btit2m45tq1BXiCT7yZXqBOORxZ8kOwLGiFd7c7_0XyVJxU8jQDDuWjD0hor0p6UnJ39HpkAmJhhWT0VAsSGuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV1PrNANRB6SX3JKcUcjyB41yFCQvpQDgOFE_NmWOhMgvS6GOweAqktMGm9K6GcBkFIr8dL4RybGA-H5CgwcPCMhEdXDknSxz2KfRzb7dZ5Uq9O9VJCimLAobrD_8JN6mCyhmW6CByTgwK8Wnx_ZnCLJ4sTW578duSuGJ6HcyI_FiQfPBRF75INHpCzt8adz8YdIjHjO0QzMOgrvTkeRgRMLkHp1dWnK1FwbI-5aJRddBHSaOVthJmClrlsTbia9qwXaI_MypUBxusR2lqdJ_6bHhHUaalsptJXQnKIEQDXm1ifI8M5HEJF3bAlI_os6MFcvtaunzrqXIvq4MgzRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_apil6uYSdbbun_6GMV8BUm9UCu9eGC2v5NmMpJsJirs0YZzpJJyrzOaAnPpRxa8_mm3tV-iEL0bJYKVoW8pFPaf-YmSp-XhriYLBn29yrEJsNtIVYXYkD0wtjYv9Zs7e-RCEu6cRcFqF3adLqfo6LowYPhYf8vY--3EKTSbBAFUuwRmY_vjKRY-GMK5zhQAf3lFLO47rDKRLrJpRyshCdKRbmI0E2QAmYPmULCIWNeI1udsda052gfFMAkPiR5OY8mRH12DIZGSIdCKla4uruG-b0UFzUOqpyN1tRi3-S_SBgpsWgPfVmM5kFPYLFxvh2r8C23aOIEy5f324foWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5N2Q7gJuDzb4-Iy4nihV_mwMCHEHEtOk58Bb-rOSBiZqpeMxRibA4VQAhf1OIL-pa5e8QzxYRe4LImKiQjAT6GxswzmoHDHSCz-736nzh_Rn5QQuCyDLhRS7Jf9qfurJ-TBmAy3Lgjo_rxr0NksYiZ9dxiusmoFyeMhV44B4nk-DX2r0ttBbRYOOSnCaKNBIj7ck-WIHpj-XbT9XPHFrbnS-pHrmIGgy916P4wyrRp4rnuDOiQWwCskW91Xkuzs4vy7EGk7cyDS8DOJSUUABnCSJhDWgfWqFTp-m6XdtXSjdythvvaQJLJ9Y9T3c5exFJymKCL4lzR4bo9OcTKkag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L70XebJ3E207aGcGGDd5qhLW5Yn_g7etK2GpkG8ePP2ZZ-NqqqrwnOUZUAOQq-hYn2gfdd7LcTpwZ_o3MyllZQGE1uO1-NYLMwFi5VbPy5ROCRImePBa5lKnkueiBKyank7pU9ETQNHj__3zzSr99ze_hkwDx6ukEy4kHUcDmMn4w7iV-1hEDIORXne1Y3UiYAtgV0-Zijw671QUra2G7Q67XjUqmNhN_x7GNYN1pC9Mt7jvpEDpLY0Ijz-0CttbShW65ca7DKa7fmpYKVulDTN7SUKR0W1XuvAp-ui2Foqn2ExTFoQzVyZ0TXWWR7UGpMiNFCyKSy5Vbd7-y_KWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeAGJW389vZAl0gLUJM0n_i7vYq7l9wChxBTQP8QAgDco0ChxExNojllRBTRGHbx66OVzvw_1ovEWe1dS0IndX86jLMorni_wWDx0RehyXJzW8N1PVBOP9FSTO-Q7OkY6IfaNZTHHjdXTwUJbtAEYVXufiXV-NVrpZOhhM3L9kaifsiywQKx-3ZuC62ObrDRcVF2oD8vHCG763ybXFcLcGmTwv3Fr1wIYC-PeHTDD8Z_UbPx3fZBYmxQIXVE6kKM703YeH5ucvklkcWbab1b3ekmgwhPiyuoO2xR7rmN4do2jX9DJbOwxfPObS_WlG_SjCEoSAEieQ8NbZFfK9RXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWLJCEgYxDnlAkMW2EgvY3S25R7-zndSjB8_VHE_X4w3yvtwjmm89zKSNGNfavJWncTM4Zw-EBn9i5EBdRybrGEGLQvNkcU2v3vJi3ajaOz_D24apISIbc02VW-KviX0WSnGbnR86ANQQj4aEXPJkeF0rRcwMxAbD_Qe98UVKISA_2AjOGrpT7ZrwyWEGPKNqOu68YYX4qlJ68roQgtctESA7Sn3HQ4mBXwd9YjHU9Gnq0X_8rt5r7F8YWeosv-UWMZ7Ryo9xqGrYBb25ngWWf7e6VZ7Ditzt0P0GdDpI97iRbXwlgY0r_6LN29LiKsLhzVN5eC2EhM7vJRWP8VB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u14dZWWY1wgor8wMjrzsOMgfpTGsWYmRQHDoykmkB_bfva7NlrKX55dDD_DdzZfCLY0zWw03QsXD7UzBbQbtpaRjra3Ps_Sv_9M19UM1XZ5P6znP4LYyJBEv2ZB2zW2mlEEoqvvm40-SPZO9XchoT4vEOQm6agUgZZNsWMGwAJU7qMmeUK9-WWiZMg8EuvG7ebUkqCu3NsMIiDNfR73KH4vuLGtQZXiHEI7cKwOBvGIpPcWvnI8lFUVTt6zmCEp0-UxW7AGE67dJI3NMwKFNx25R2rdJ_fqi_T9VX5n9WvkNGpQtTv-3Ox23VGMMM6J6rHuVWoQEc9hypWRp7faP6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBhU38p1KnCKIX3VaVo1MtnWxp-yRUvDgP30lslucqS7scsYyg9T8mA8DbO6TPl4FauoS2eFaRZ7-B35G-35imR2rohIVSuxKD8QxtIEj1Sn3XndR3ZW7e2_tC8vaBGewRpaI0Gu5l1r1NPsjgkZzP7jCxAEB3RMQz0_wbnSCznR0OtPaLjp7QW4JWVKxPDzVC8EVzYf9EuNCHzyQfpjPK9_MLWTWJuO4EFzthSXmHuCW1THHtXzBYUF7elhdLRdFusZTt-Z7fThuHFywOcHY3lTwvQDtwk26AzImHW6_dITlthJXGxwFgYpKFKK_EeVCyWbUAffhYzQYxx9-ld1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqHnp_K5a5X-oU2t3MH-ZehdTYPrRamwBFNFcvIj18htlcszg8ZjRQ_MLMKgrz6JAoxxjUjooaMVivx8ezaQ73are_HY9A--miIv1dBTo8f_VDckSTdlgJgeVauic1wuT9Q0iI_-7qQg7QnnA_vUjsHbg7dRJeTvTnVMoZjefVRoK8uikB4GzzvB-LdXfOl1n_MD4r64HxkB6md_0ruQV6wOBF54j8hVp1bW-sleNenGyTCqrvXmWFGDSMBPE_PRoa2Q6edpnqNOHCDzpIDfCT11516HwvXlKMvDBtJILiUuYSy-VLoBHVeCWmiMPl2AZwt7YkBNG1lk_wWajYfPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw-t47Gaiuuu5SKLaV9gOdn7W1E31fhVOR_T4zAEZTCQOwz9HAQUlEtfZ5wL876CEr_OmHg60hgUBTSgAUfILmu6grgGPT0OgJ3wxNUQSEPWANTwQ5eQRjKI1KfswltO_kAXC5uxv34k19bSUCWaqbOBNewSlg1hmdRFqySyzYvpZYbSNQs10Tm7osqUnxWpU-mjwJmqh5yd8JIs3nu5l-qyhsmjGNlu5Fos0P1gZCMo5srP5CJCuLUx0sT1fBi5Frf0Qd2QES_g1CYQQ3kR3NRxoBwGeDiITa6vjtegqkRW0tmmcMso78oRWLMVnzRRiKzc9pjY0fg3MdRL_AeN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3PvUBBv-OIM60zgzVAc-5QZeQf_9V0NAsXmdepIWtTstNZDQEtejVp8a1jDXK_TfIw5op_8ZuLzzDQQjPjBceO1Imon172B8A1pNUfrdCHsKCLp4KFWklppO-jeKQcfkCpytSHTJlOcgRZUn64tkOuxR5p_uSpHj3Dx16ESZ_U_l_L3JP5dGGY6-oWuy6YOjgz83UmjI_ynz5G1NCA3avh8D7AhZRSyN1qCZ4lnsoKwAqnL221Q5x93bREcqULRmDg2g2b3M2Ixe1LMvBYSEQo1bpo5e_dUoUCAtR_LkfmozOQVZFgRk3DmmXpESWf99D_toQZ-p-W44DU3o0lz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmVeKHRsr6d-8x70Dvix-aEkX18DMY1VSb2gIuOgmeb_--Mc2bDLUiGKOjM0kphsV-KQkrSvGSv1_i8QlnSp9JewHbiWtkfwaObCUqCo1f1on4e-C7efWEX3z8y0xC0ZMxSYhzsjs4ZmiuzioSG3TnGkaDaN-ANaB-6DoMMRdQ3-6raDB91FJYPbrisHcGuqxQgllldOQGUCIdC_RPWaXdf1YPldYf0c_7EJcsv0U9dhA_Xd5JXoEu-a0g002gbU6JaZLUAE4Jo4r62pQiUiRJBm-xwe-KJdfM-rk2wpIksIhWCXu1Unxx-KN3SSy4feeheEp4kg1qGfIiyAeh9MhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVXHRO05QsY4Iw41SQfehRt36fq1IgbqvK3kqXhnzmgzNBG_zI2b3RUr3pcTq2G-ZFyuPFVVHxLBbsG03L6B-gQu-afzTH-zbklj6poBPEhfzNVciYCX58IdPwBcCO4vmWayYgbZQ6DoL_YHenxglQ0Kf1d1dlP5U6OuyW7IXf-7seTHUtrk90mJxNCQVy_v_wNKw5Ak1qgvE-vTka5uyD2j9nO4ZGe6CBkvDxYW_YewdaXIIrGn-In-M7zJsyxFlV02LktzX1mNmuZC_e9zyprK5i90NEwSs_S93ccXUXzCUZE3Gn716Oss9OkCQnDGK0Q3ChQ2fXh8gyZWjvhxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VopFyurdSQjmMFJ-3nQeu2UteNdGX1-uuXI5P70_JmpLFuZDCkiN5pMvgPP4y_hlzu3PbMsuUf1SDBd_hiN485mXQchgS37F2pbTFIkJ2wiciMh-1SGf_b-nd0AxrNzufqAwSsmQxlOtqCAyyBHIUM76IkHwoZ9ctaGzJvfUzRKq3_po9jJ1guhviudmMfcgtUfcU8gPPBIqTJCq3ERJqZuvm1MkjFo0B0jUOW6O7Db5u6t0mB-cUqWMboR3yGBo7kDz3Ygez7Xnvu1eSw3qBmvwuA_mjmyXTQd-4DXGr6eBP4VI52rSYBJ3BnOfpFI9WG9ZyLtsbp4LqUIqvM_C7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr2e9blLnNn--ZJBVyNSnFtO0U1B-6kT5Ll8iAsS6sMbF4W3zKfQb7dqf1p6rwsEZ8yFQiVdp0UtCMw6wsgX5OCvyCWkr3pX0nDuiG7qLipwde_qE0ljOK6Oc4eEWC-5KOhC3bPh0EDvJy2h6M4XJ8-SP01b6vxPhkyEsVdVqFyiHYT2KvEl8Tphuwrjr6j1DfC3-gjE9X1cHloHT8XBOkwvQcAnJMzHb-CMBRK5mjheFpehVcs5Gs8Q_S3gvmcMsyJ8Lp4h-P74aOFVwk4YN5sLEr-5JkZJ4ASWTM6xTQ4kR87LaJIO4OZ2bwCp35Y7sQjhWpo4AYtQuTf0yCGH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdQ3F_yNULG5_6qQGAk18udy-T9GGEk9rwAIthWqKltnaX9mqJS-SXIH20TnZinSoj4jZLDpKOB84Jld1ZLuQs08c81ZGJf7kuNQxrCuak7ygmsF_G-FXgS7W4VUXQ36MO2MwOE-lzL3rFXqk1hxsV1yL-EN-OivKMjVgTBsZMMB1ancX5h-aHpnSBLJAq3bjqDWtvwaU3D4bf_1AdE5Rg4VtzxTen9xOreg-iZplNHy-vp5pPQMRMN3-HFItgZxYnDBYsl2QG5wYmV7gSeIr3VnRhwEmm_Ip9JVte9Q2RiCSZjDDKyPWqLtru-98x0_xCQqOvcHqpmYbKJ1HB3wqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwT3eEF9STQM4W0aBzWw782nDICOjHFmbc3PmIlm48ab8nK0thLeWbeGLoG3NElFIXE9LiW6kntGN7JyeM29I6GJtYsip_zoYg3ZYy3gPvTm3tmtJ66wSn0bISWGUchhbsIIhdNWbDliFvLDAK26HMdlFL0n-_FtSkQShuCeEAKzDX8IBSS_reNiK8k41aEPW27BICxJwUa9655wgBaHyhSHtI49hdlXzNtQww0CyTP4L7Ru8c8nbrn7O7xo2lMI9_p2ayuzCBZn9S8Usfn6l9Uw_muzzIXH1LK1XKr1a5uDJsu17TzCQ6_alFlXZelnFglIcZZ1EnoVn-AaRePZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qtio7QZEVGMddlDVWpf3K8-_WHd4St67rnVM7dbGVK4nYvWrz-i0oWmDQl4S4kOqncFXPvv1dhWSS7lXu-OMpdsLWyqJmMeM1gNiMvVuDdNsGj6qmoeorA51dqlqDPVCZ-iBiKEbzopjTIPUjaeyiU_KJbLlWGI45aY8zAYe-Id6AH4tA-QczGM7IgwFAdeB2c64tsOpxPa8SP63uFsD9nmWyvWGuVv9eOkXpysxilX_zQGBzxNBpx00RbAUWv3zCs1LmT6p8-Fn1VCDAvtaJNjDLaXLVbEbuN4ExxczcI2eK8VwnBGFgMQiLuFgaWLPQcLf5-9sfU0IGvZ5RAzbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyMeprdX8ecH3Ccbld8BKZY8RnWklI9sOJuxymhn96wMVWJqxJpJgAkWnL3vP1xQcqOx6aMA7tGOGejak2_eOgXTy70q8wtKApCBycCFQfEMxIK3mW3sev1u2btZPBGUtBja5PKBDnMrDlOTqVVM-CaULYiLmeSC1xy52O0GPmFsbs0e8hUukR6eGzVtDc2tmKqp6ea5mahp29epnkebLr61TxiUKsQ1X3pYQd5i0cb_88T6hbuQCveOmAo_Zjz2xJOeETP5rGlse4niq0M9ne1pm8nOTtoByNo3ARYleY71A0gW8WGjsu24GYkGq1rKkLxHiSAW_XaEkOIaU3iMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qdavp8xDCQtR8MofAD0RFsretdkoI838Ww9l8q0QOGKHLHrlfNAHXgVan8Cyp0o3aTCThwDuxrUFm-x2GuawP44wedL-3rR6Pv0IyWKlN7Haq6VqSC5GOuRYBad2k054Hc_5oUHdzV7yONOMr4MCUSdrWAmavZHXVBbEaX2VuvYpKxOePYWRg6hKwi2SQkhBNLmydMfhPtXHYKi025O7fZfruFsb8wCp-XyB7zeblTChv00w9eg8qacXjk1v8gSQJZ3Kfjji94UoxkgkStWqpnO1Pz-0uJwBUoIJcuPjP4H533Q13ZtkGUSZS83BMjIYss_lQEkXKvwhoIopcwgvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGUsA1OBjPJMwtXNDKqvbEFxx70t4mFHqq0tvJkaVAIx2gnVk2Nei6t_baSq3yC-n0A6w1BKDaUNUBEtI5Xxessg5eFiSEDOSif54UNe-usOPVt7qRXKIbhI41eIO8C6_zeyrmZGdeZ228gyKE3Z9xDklEwMozqBQ62T1jaGpvJy2dBO5UpngE-szTVLv0d2skX1uTneiWvMTEa7ynAE5iW9yT4kxy63FjeiUUnZc2hQTF9UDZ9BJwjP9zSMq3qfYhDAM7-FpEF4R10q4wRKwE9HkU3OOp_LKgMLlJOAf5glLHHg4Qzb3WjIAgkAgk0HGr1hwJys4pB-zynpD74WuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OguA4WCeSsr-OgU9uUTTXh464Ak8EvcGFzqBVkHjvTQifH1Jz5u08TFrjh0PNXMgaynAAGKH2Llqj8gchmfgGcjpuNJJ5Rg7O-BKwefqY2pncvp-1fwGvWfgU9nR1bjuW-71gTti66jk4DtnyUh6PDtur9eYThwwKzmLRuyX5UiGpzApkxHe_rqSG-kS_z8dKiojk8KWbnqgpSYRtZzBhWhFvTk9cfuyfs58BIKqeelS4MohnKTX1qsJLtf3i6GjSrdmvGWKhjB11Hy9TQijTPLIrGfKAWB9cYM6ff0dgfzQ4BlYoXLEoGIibKlcoOspBqq83Tiy5wWbgx_FrCE_RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLbSofCIc7jDY8ywKDZYe3T8k_5m7yrI288kD2rCOOb4wlm7rWfP8U7z8KkWkN02Bygjm1McJEdA_fiDFC_w_-AWLCXmSBQj6MyZOZvkhMsHw_666X9JJNnM8ob43zfaRCctxnHDWLHQKmuve9QynorXsdyXACW7mRgK-xn4LUkCeOO2RrNAWC7PExpM02vfEn1I_fXNYDkfABAFFloPvmUIYvQl9J-Vj6vt00wo09MouUyCz_L2V8B30RlvqsEQBet14sVCkvOHelwF0IndOYvQY8gb1zwhA7gE4cz0PvFRQ_WkB-oQN-eVvg0GcSL1d8v0jQQdUxVnAGmc1zzWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=LWXbYjMYhnmVddNEX2EW8ljCG25Z6znIq0jDf4539so8VyC3AS9Yleitng2N9k-zDErM_3_b7tfDcwt_DSIvDwClEpOjbK5Q5XRsw3bugcWqD1MbCtxyniRQWNdIWJc-40PPS8SISh7F_M5pvvkCgldKFYou53l6ioDWm74FaAv9vFJHBokEe5iR-ZOL1jnGjxVxyGyK8QPpoAuV-MeSq3VF46-BfMXm6PB744zoS9yfY8-G5EHSHrR0G4gbWnUD2Bt4U7EHj24qbth-KLb6LmLwevV9mRyWarsP67bTbfqT-zh_0T-20zY8vPWkHRwh5XbW_D3Gl4bu_728R0wT2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=LWXbYjMYhnmVddNEX2EW8ljCG25Z6znIq0jDf4539so8VyC3AS9Yleitng2N9k-zDErM_3_b7tfDcwt_DSIvDwClEpOjbK5Q5XRsw3bugcWqD1MbCtxyniRQWNdIWJc-40PPS8SISh7F_M5pvvkCgldKFYou53l6ioDWm74FaAv9vFJHBokEe5iR-ZOL1jnGjxVxyGyK8QPpoAuV-MeSq3VF46-BfMXm6PB744zoS9yfY8-G5EHSHrR0G4gbWnUD2Bt4U7EHj24qbth-KLb6LmLwevV9mRyWarsP67bTbfqT-zh_0T-20zY8vPWkHRwh5XbW_D3Gl4bu_728R0wT2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiIlA9gSTihKSGZKEJCYCoGEwTwp6g8rx2sS8u8PLGu8GF31CYNYMbuyq2b3cFpy6wZvE-xVoFXu8blXGLqge5CNDnCibkDY0vcF-FMCM4Jmag0Kgn_tfuf6etoMt7MHFzgyOd8t-qTFeVw4mwjYxsQAcW0aGgSzIcCLMH_gX7dEw-Lv5hAPGiQ0_PVwIKkuRUBjSXahJKmUY8gSR07DlIlOF5M2u1Gnvf2JMo2SWDkfSvZM4SCi7AYgNW8Z9A-hyMHrT22UxKjCrr7NgB9aWHsEEnZTJLU8qB08SpJp7FElOT8PtpcLpDDxAbL8fYglQqQxDRra82WNd4rbCSzHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=jxc6_AqejjndcTF-X0ZnCOLH42M0xo1DIeKx4jA55lbdha3mYorDNhlK6VitUQIIiZHyiPxPfjlf69KmlfTdMCkWqYPVWQKpMLxeDo88PE0Rfsqak4LijQvHyOKJ1HUWQdYvwIbXwfSfIGCSAOGFOspbUkYqeSSdOVivP5odynFR75pgarjetry6GYm7RFlb4DRdRItUFMpj2bqyMD5G9f9pJj9Qp1PzINfi3uM6RZ66JeNYVYPrOVlLH0ZoQb-xXBDxUAfigCEVgraf-EBiIQvbmrZNPg9dFc1_nJ2r4X1zmxN_EODm8cfXaEt-a95BYuhYrjnBZAyOMTd9aEdjtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=jxc6_AqejjndcTF-X0ZnCOLH42M0xo1DIeKx4jA55lbdha3mYorDNhlK6VitUQIIiZHyiPxPfjlf69KmlfTdMCkWqYPVWQKpMLxeDo88PE0Rfsqak4LijQvHyOKJ1HUWQdYvwIbXwfSfIGCSAOGFOspbUkYqeSSdOVivP5odynFR75pgarjetry6GYm7RFlb4DRdRItUFMpj2bqyMD5G9f9pJj9Qp1PzINfi3uM6RZ66JeNYVYPrOVlLH0ZoQb-xXBDxUAfigCEVgraf-EBiIQvbmrZNPg9dFc1_nJ2r4X1zmxN_EODm8cfXaEt-a95BYuhYrjnBZAyOMTd9aEdjtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au5cVPGIOJlmF0KVLrKOaErfChGKZ3OLk3tQaNn9d7vfjUQIkiFto5hg1ldduHUNVdi2hZL04l5v2HqGb4ufOeDPKf5Rh1KtaM-PXlt_TzvR9KpWkxgnJiV6XxpjgoE3vvuhrAlT1jwH24rShopXFkXcXIywKZhZaUpYAV4K4m22vPxPyY3b44u_L6eXRKiUTb7_lNXGQaCTEz1Bliw4V0H8OB7S_v0spqFmEeK44aKQEm4DT5KfKvLYufrFB546qf6qhRV8lFs2JxvG0byaHZUnlVnPkMZLGvz2QSc5jqhmKLEpniQ4-LZgu-w9MLVr1X8tdPNuAYBOybNVc0wY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCb1b0ulMzmLJwsclGRNvb_B-XfUZg20cSN9MbjzTJQzqLNiMb0brRyH5iU6bCDvIdb4fsyZuHQwjEDXEhJRy62M2HgL9seAEDI4h9_5-t6_QjWvMPjCWM3ZY09y4zNEcjM-HKDrRwTmc6FtsAITF4g8Y4v8wMmXJsDTB5vaouJR7JeQe85nMjgQOB5bn6nIm5N7_Ait7NotZLgPG5n7-wlUDLRYpAowNpM9OrHtyRC6saorZeqR14I-q_RBs8QjgPTMkP71F4hbsuRjrQKrxlnOMImIFzNSFXN3Et37-63Zk9f52_BilZOk3BsFrz7PAArDtMilhO_fOjllTeI_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=L_8OWdZhNdHE2Akcjj0N21NaC0RWdIuoVY9lcR62gousiKTEhkVh9eVtzcVQg5YqMx2ezPYRt3UOdNwSA60TpaEIFCBbNWXkcVaFNjCphR_w6jB33aH-dNzBBgUKVMZ2uhjrgsqTWg91UR8dLB8VbpB46tVJMtdxadzko4HNPnQ79s9s0mnavdFPBNd7QvLp-65d9WVWNEJRGkEu7TTb9vqJsPaZiIl_UYhXleGk8RH3N2hvvgTIM2tpy5FZzzUWClbXBdYMpT-ByxdzaNyuIHVhw9ZNBGlKlQOOU3yLkoS-BRh46kzQGe9a5fiCJR2Prd5mUtGYt_QLEpOMYt8ZqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=L_8OWdZhNdHE2Akcjj0N21NaC0RWdIuoVY9lcR62gousiKTEhkVh9eVtzcVQg5YqMx2ezPYRt3UOdNwSA60TpaEIFCBbNWXkcVaFNjCphR_w6jB33aH-dNzBBgUKVMZ2uhjrgsqTWg91UR8dLB8VbpB46tVJMtdxadzko4HNPnQ79s9s0mnavdFPBNd7QvLp-65d9WVWNEJRGkEu7TTb9vqJsPaZiIl_UYhXleGk8RH3N2hvvgTIM2tpy5FZzzUWClbXBdYMpT-ByxdzaNyuIHVhw9ZNBGlKlQOOU3yLkoS-BRh46kzQGe9a5fiCJR2Prd5mUtGYt_QLEpOMYt8ZqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSJorq37KHXHQoo5H-M5VvtHbouhP_r8xj-s_0vsferzHdGSfpoPYisFGG1YP5C2vu3A_E0G2fdjJCGAqtBYBup7DVyoTykhjFBWPWwqU30_Kwl1DrQT19kcag-qOJrYDOI4jCXImkoejzJ1hljfjnhAF_SBJet4crKhlNuglRKC-wijMI2S6L_pBAS9HNMY2l2uVd43jifTYRRgAn5134f7kqcib0a8DyDuKghePNc0IJrykQPIyq8LsHSEgQw_W8j6QHjLGqGA0RJFphLHjpNna_TsNfA-Vuf1pIwRANgPMAV_6HGG57jKpgc5JPnd6fxXrG70Y7Dv6WNObiX-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6uGfyxgArQS2bIneQioMmA9uK0HhgYWcxWM2OTqWApUkC1iBJmaCp4t8WDmoWzz7pXuibzs2-EDDWARpqu9iFsfFDEo6zShra367MkqECGmWqtJ0f_7dhcJTAN9-lvCWzJdYfl-AAe7Oa_7_lMJUdz5tf4vRrx32tfRp4W3A8-9_ITzlGPSILd2Us7G360kQ8n_ANSM8zzbFitWRtA71kHfKW8x0CStn62xEUrJ-hHP4BfgbNZp1sgURU_C0cGtqlwUxptmAPeFEDuHwXJGYBGilS55cWZYISeD_qFusaK_Aq-yBSD0lQlHsO2oIfpbCNz4aqr7uL8qm5LC4jsvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDN3BNkTGoEyPXb3L38iIdMJUcA8GIepTsm3eZxlHtTlHb6dHqYCk9r4CZeIL7Icrv-IF0BIkivMVAtDDdhv1785w32T81Rb9IKMMi5AQlqDzXoX9ukUJZ4TnpkW7UzADHxyjBjBFmfk4bnrtDcP9qqkPhzAeZfY6FFkrp1lEaIo9MboEM6tGpdNWAlTp8LJRsa0AkiOk1jqMDqzf7cuVewyvvWn9PQf-g1bsRxK9ru4kpelsFB990LG8jRK9P0Gk_gSXOXDga0miyImb0FfekmNN7tt-ay-wIqhlYx77_HpM0mejDsD3d-dkX_udVuXZPdm5WLyLwci_wn8OchBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=o8pKIvjqLh4p0MLIWq3tcxygWuZCf0GeA9uJFFccuU0l3FdOvzWUkWC1CjNHxRDnv7_eGIkDvanyPJKZ9NXyNdYIjJK99kCHWkejgSwjQ7Voo3YtDLbdJlhkXl4lQA7gwc0hFs5WT8rvPG2lW1sgvouSHuXeRtsjqp0PxTAM7sGhDuknApGZcdwJ-CPVkQip7D22KAn4qGzwdvFY9Mg612zJigrpeTxeCuyvV0mzJFsXHIE1WsB-sW7hCMBMqA524QMYmoBVQ2jPfn5nouOjTMYjT_PbouHo7XzYgmm1SKju3-bxS0Jrq49_mzt-jBsDJd_FGJaIG8TFomPGv-NSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=o8pKIvjqLh4p0MLIWq3tcxygWuZCf0GeA9uJFFccuU0l3FdOvzWUkWC1CjNHxRDnv7_eGIkDvanyPJKZ9NXyNdYIjJK99kCHWkejgSwjQ7Voo3YtDLbdJlhkXl4lQA7gwc0hFs5WT8rvPG2lW1sgvouSHuXeRtsjqp0PxTAM7sGhDuknApGZcdwJ-CPVkQip7D22KAn4qGzwdvFY9Mg612zJigrpeTxeCuyvV0mzJFsXHIE1WsB-sW7hCMBMqA524QMYmoBVQ2jPfn5nouOjTMYjT_PbouHo7XzYgmm1SKju3-bxS0Jrq49_mzt-jBsDJd_FGJaIG8TFomPGv-NSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=ncTSS1gk8dhhfrGphzG94qLp_UBB8BFBJ9Do4wlXtD6NcmPSpZdSp9xMQImQix0VuecqcROJkJJoSqENTpaSDDwZb5HESd8XfRMVyQkrUsfvnRuhr43BXCS5FfriDQKUIMliZGXSEHW7Mvbz21oba69NoPCVmrc0JwZ3BtlRxTg8Qg_EfMgHqCjzhE58IBuYQh9zvj2JZFy6nFMzKebkEcMwQJg7BFG6_b0cBNWHzJO4pHSvzhCjWpGHf01ECTrqpy3WBbUH0KAcmgVONpUno7rZ6o-qpI97855YihEwafg2I8efGnQsgTnS5wmoRQVZVH4e7Cpv0dxd69La2Q9tUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=ncTSS1gk8dhhfrGphzG94qLp_UBB8BFBJ9Do4wlXtD6NcmPSpZdSp9xMQImQix0VuecqcROJkJJoSqENTpaSDDwZb5HESd8XfRMVyQkrUsfvnRuhr43BXCS5FfriDQKUIMliZGXSEHW7Mvbz21oba69NoPCVmrc0JwZ3BtlRxTg8Qg_EfMgHqCjzhE58IBuYQh9zvj2JZFy6nFMzKebkEcMwQJg7BFG6_b0cBNWHzJO4pHSvzhCjWpGHf01ECTrqpy3WBbUH0KAcmgVONpUno7rZ6o-qpI97855YihEwafg2I8efGnQsgTnS5wmoRQVZVH4e7Cpv0dxd69La2Q9tUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-OSN3OLw7MVYg5tvqOVpB05PM0Nex-dI3VioLZHbVDWgWvOJ9pawWja5erlHnkiBBEhXoUliPnLFIq80E7Yw80O_gBykbLZFc2ycWmKXqTTVyH1y0oqq6iIWQsGpjOHDU8WXz2FUaOfQlgACwTSyIo1GFAcqV7dPnC5xwcwCQZBH7HVuQYvxrdLJHxDm3eo9p786B5swHFemE3LzQ0HW_co66MXJSLWFsufo5qOU86l7eOTwj5RIcHKF8D4bMNjRdG8N4EQpMjZ0C-0GuzNv8pGZFyLrUcU7bkbTSg8Bb29J9XSYq19_vPfcti6MNK4dY4Q-YCx_kkM6GiZubKmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGcG2SseeeB9u_DucwA_3TAkCegs-dETWE7v7b1s6JJfvha24O0AEIc4hO1lozZDWFqyeuWtUfObf1vQCs_b5PrPWXh6R5VPpl3dm0ve7TsciiYFwjymMr2dofsLY3DthM9oG85VCEPKJjahM5D4tYTX__67IO2O5JY2hE5Ek0_8Upn77rVztcAyPDpWkJKpDYOo6gvfqThM3uDWohoculMAGLafzcLdqBTTjXgvQJu5JHdwEsDLVfsWQTYnSbXCqUqfVAUz0AQ1DBLq17vJmdt2IVjSSbz3ERt1IsuSN9K8NSNeSe6raKud27632-UUaf-qli_u-Xbd7wKsLm-zDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWaQ98QLZSZBZpzP8Y2au6F8Vx88cu6mDl8gwsha8Ssrxu4QMrnFU3bde5ESAH0bklZCQxnyNnZ7MW3R8CGaqtiKoqwTq29sdkXMl9PZqpxpXxQuMFlFqPa68xCivpffcEy2a5SFcp4FzMbb_RQxmCaTyzp7lpMuMk4lRpkgUjzH8Nhapls4xmjnWbndiwt3IYqye-wnE5cVjcar_UoGGwv37gHW_ZAOWiJoiL9Wubgc5IwOzm-Jqro_HJkY_GzU9ezVLYg8-UlYaIUdLGg_zvxBlzZQ65iu_V23L47YmRY1U3laT9tkk_-SYfPIlhD_H8REj_Jiu6oy4ADkfKwfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B12S3lFfUNvR0y123J8RClJsO1v5_ZjZQVrfV13ZllghNizLRRYa_tithCBX6xrYnxdFx0OUaymZRIjr7JeQzop6PEOfBFYwtplCNaiQ5zb-pz7_QFtNlKaaK7gu7jANTvDBPMagYPHJKrP_5uJlC3Z9pZMkZsTIAYQRXXkVIC67tFdYYSCSELa3l7MUbYy10nOGZjPn48_-BnWiZ44Lbs5XlPG8LjwAlBNiT9pxC3AsZHDTjhrmX-VFCmIZSUlGxE9g4RRyQrLG_3DWYn6ey83TzjV6O28_Uni_p79GhVBOXK7w_4lyFG9WYkE5jqbd0ejHJfkEFFGbM4A8CSJIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR4goSEn3O17djmmJOJ36_Tt_tMgfOXNGDfRp81_F5tX8j0ajgzA5elUFgEuoFvvqqo7RzNdH3Sj8r9Fwpv4WAo9hRCE0cMm2hVSd3Fwdi4PawF8xnrnOZm1F6FgHMBGkpStisB2A8oFtUw3bpt5cj-k64yOdDDHYSv6ZaHxpFkE8KJB3KjVV5h6Gj428UdVgJRVqSiZ0N-2z_vh1BI_jXwcAamgNZiBXqDP-Rq0SG98JwVS5wJ7SB4S4xyZCO3u0AIoICmTRQaA-TUlcwu6xnR2AebSyQPJEG7IQg073r_PqrHJdyNGOKl2YRLMlzzAutikE4VRLONOwxwbRehQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtHDw97AkGX8kn7FA5cJpQ5e_X3UY9v86fAl88WWOr5qrOnZRlCAEV4_50BPCAQqesjEDsbVjed2_m_yfHqKski_8MsF0Yq6WpLOyQOKBgKm1uIdmLJW4xnbq5xVPnFeMCHn0HHjZPYoxUtpz3GyCJk0Z7sWLQjoGUyn2REHZRiJdIXfXTqRjmLIbgFx5fDl_ISkoAMApjV6L9D4DjM1lEo2X-WFeWrCxTfXwz0EWFOrXoO0r0eF1IGGy7rHic04PO1UHUoSFT2e8hNuBD1luAjY1iyqbhtMA_kJeQ6s1C_ig0TbaycTMgzkume4bj0XwjqkwZ1PkuaRSMzy_ZCfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
