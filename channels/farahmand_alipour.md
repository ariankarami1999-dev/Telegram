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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKpL8XcNjuSGgDo9_lu6V_4QskFWeO2xeOjdfxmlZ7AvsUIYfYrgIZn5EgiQSrnX-61crc0DH1W_2EpWnADkqjPatHdfTd0ilv6y7g0V4oLVrbZL5sGG5mQoLEqemhHTDOZtv5M8wvMcfFcLQdpBiY0DV0rxADtujt21oWItnQ21XV_53G1GoIfX_bKnzgNccChoj9-hriznKywmzdD2egGMoBAVAoyKV9jcI4um6iiBPjtp6C2Cxl6wK-smoeRQkEUANIUnTFKTcqPYqZirQK4ABXyAttHrhfJBO22h3z162Bg3yYaFOzqYaIDUYT7vhXl24TR1MX6mnLrv1ivvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmFcd86Chy_8xZWRI5DRyh1zFweCHRGeOVbAUrSflhmcVyZY86Gm8wtHam4CtEB6wjn40qPM6kzBrAngRlSFpgre1NfdFT90_UgAlAagNfQWxJ8IaQixcg3pCpxO5mCDyPKS79IXoPbaJVr_D0jJmUvayGC2FsHeKOoZy9a6XvoWYz_2PGh3MYbLcbQCKDKEXJiAo3PUOhE5jctFpgPqjDN46WgaaM5CQtzHCREGFjWP20SlO4lvy-bPSW6URFW4hIE4H5OL-OUEzghes6_nxfux1NHxfZvx8vXNnguMPwJe8N1oFKeDAnvtjjp5fzGL2Yuf_SCWtVz3WcQ7q-qqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M714M__idmOrh_9nZEqGJAciep9lVpqMRQzvBcmPqKirNQ16egO-sTpSKjpOV0T-8Jf35x6qmix0IKmnjNSUo2MtZ06SHLyXh4pqkFUanPs4zNKMacLlRUYrc86GIDe_jKpLdcfYRV1gAiObCHMWIoNVU2L9THTBpLipP8rKh-9g-haKTROJbsrQ0Y7Cv3qFlkRwUVXJyjuqmTln1P0GA8fC3NbHahi28d4WZE72FBfRLRIwlAOQfVhhietGAlrFMHv18kL3DOMRo2eydN_Yj0wT2rEAwJtmTJ9CcVLBhHtphDOELRDwQwDeoIAzE1NG18JsHIpngIs5fgcJ7dNNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o_CCrVqo6cR61bj7M73zL46GySBdFMgvAtKEFSEkEe57BgR53iZHP0shi1f6gc488vpJuBcEuNo_9M8bu-ft6TEfI7csGtnHpVdKZ-IslxXoolzf7aKiGJrgafDPE080Bu0M_X16u7AY0GoHxlUcjyspbE9mVqMqLka1bw2yacI4Xufq4V1TVgLh5_Zx03zxqUSFIF2gCBSXNJP0tHB2SP5tQbMrDE76gNpKzSr0qmbkRDmBZVaTXA4iAf4PzxWSmQrjT6PBPdBqNk-wgExaCivpUgzheVle6ghlkrctWc9KmSUzjWb7YUkQv5L-BFQsql1V5tpx31KzztnVX8YMgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o_CCrVqo6cR61bj7M73zL46GySBdFMgvAtKEFSEkEe57BgR53iZHP0shi1f6gc488vpJuBcEuNo_9M8bu-ft6TEfI7csGtnHpVdKZ-IslxXoolzf7aKiGJrgafDPE080Bu0M_X16u7AY0GoHxlUcjyspbE9mVqMqLka1bw2yacI4Xufq4V1TVgLh5_Zx03zxqUSFIF2gCBSXNJP0tHB2SP5tQbMrDE76gNpKzSr0qmbkRDmBZVaTXA4iAf4PzxWSmQrjT6PBPdBqNk-wgExaCivpUgzheVle6ghlkrctWc9KmSUzjWb7YUkQv5L-BFQsql1V5tpx31KzztnVX8YMgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJWuY01drZNVG8GPoMrii_P1eCcskbHS8d12ELYOFoG42S6CSBkoFtdx_K1bZFJwkfOx6EWloQU5LbztAkkaTA4eggBx-kiezZYuyhg4jCOpnptmYBXpEFt6dsQeBFqOzjRc4rUGMrSNrlI6v6SZM21lFrboMvkpqMcRL00IOdAMGWnsOuCFgMNxLu5Y1W8IKkD1LWpeTg_IZ6fPopOmq_4GiYh_RShRZqHIABRzkEqYwAaxhuThlsgFndWYYt5u-BH2uuPdu0pezAyBJnGbxi1DSWZwPA2tpSsgl2MznNYQ4ylwot9ZrCCpZ8R7LpEZmBaI83HSEd3qC5mIWIqg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmDjRaWue63TouEG_h3VRkHeRToos_ao4DABkBaHU9JON3q8lT3ozcHWijzjJJ3l4Z5NtpAMFL0dwSJiEZvuZfbmd1KHHhiHQ-8Vb7KaOk--XbalXM09Mq7JMtb8TiC23kNoIyXodbqNmr2U-kd4L_NVlzQ3tOM4Y_yzfZgzSJtLpWk4e2xB2YapC4BXHwiV_pgEa7ns0jDWfXiWaf4SR_0ksO9r5O6bJJ-aOGv4mjBwjgVYQfWR4e_bpnJuFAGhtfzrDGsDQTTpc6J5cxArb4D0-C7oZT0UMeEWPgTCpzZNGlJqCTcDSHJz3Y-34lFMuGsAf9U8ffip5tthHPWPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QLn6_Ht8IVjvvydoi7XDItHkATyjvXOsAZsDlebgN2qB3OD7r3oma9nEHwvIMYV3EEtDETfNSVaP-xMNI4SAOxIoDccoEZdaQiSVbv8VWVFKb8LQ3PX2pHetKhV6GIWOQSQM7y-tAnLz7ovchFLVxkdZslr_PFCjRaKECtAP0Ubt-OOD6N9fFevI2biGEne1hpA15Uhq7dW71QKyTyAHWWl2w3UzrR1RnYrOAtZPiHGQTlvdfC5u2e0q7PZPYh-WmJ18N4sQVW6csDIfTT9QBAq8pwMa6fQ5bqwDzyGPMOwY9V9-7k9g72UlKhoG9CVNK6LTg9pOLzl45UDoGIk6UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QLn6_Ht8IVjvvydoi7XDItHkATyjvXOsAZsDlebgN2qB3OD7r3oma9nEHwvIMYV3EEtDETfNSVaP-xMNI4SAOxIoDccoEZdaQiSVbv8VWVFKb8LQ3PX2pHetKhV6GIWOQSQM7y-tAnLz7ovchFLVxkdZslr_PFCjRaKECtAP0Ubt-OOD6N9fFevI2biGEne1hpA15Uhq7dW71QKyTyAHWWl2w3UzrR1RnYrOAtZPiHGQTlvdfC5u2e0q7PZPYh-WmJ18N4sQVW6csDIfTT9QBAq8pwMa6fQ5bqwDzyGPMOwY9V9-7k9g72UlKhoG9CVNK6LTg9pOLzl45UDoGIk6UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=LMKrlARAGTi_mj-kTPb4DHmPCcQ0EsKNMa52xC2viARDOefit3ECKIaruRHn-WpzHuDrhM5ZmrMdLMU7m3GvYkT6uNPuOwTbTPU11wT3MN9WgezOoJ1icVflGoETwPxG8GOKdru2AoKAin9HTBmJBYxxQ7j9B_M73Gml5r3mKAfJdPL2ZyBDrHVvoPxaXt0BWQRiQFVC60LnaOHX6ZbhMQko3Q3AYEjzKm3VlN9T2dslXYcL--aU6jlV8IeUPrlvKsIyQr5cY0MsA-aWpEXNLWYwqquxIijVgQI6erb_iOAQOVco1HtJ-8rqzv2qJa2oY-qJhZMeJvS7bP59yB4rLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=LMKrlARAGTi_mj-kTPb4DHmPCcQ0EsKNMa52xC2viARDOefit3ECKIaruRHn-WpzHuDrhM5ZmrMdLMU7m3GvYkT6uNPuOwTbTPU11wT3MN9WgezOoJ1icVflGoETwPxG8GOKdru2AoKAin9HTBmJBYxxQ7j9B_M73Gml5r3mKAfJdPL2ZyBDrHVvoPxaXt0BWQRiQFVC60LnaOHX6ZbhMQko3Q3AYEjzKm3VlN9T2dslXYcL--aU6jlV8IeUPrlvKsIyQr5cY0MsA-aWpEXNLWYwqquxIijVgQI6erb_iOAQOVco1HtJ-8rqzv2qJa2oY-qJhZMeJvS7bP59yB4rLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBIJd1hqBh_qa5hq8QOmu9EiwkTc0oFILCr14uh2aOXB7s1tMbYXL7PKlMiJffuC6tJm8VUmU7v-1ofxFiRgIAg3cyUkSsQzE6btC5j1WlswR8WsPUhDZvmTAJvBhpWUwxNwrSWLPe3-CPnjyymdX62KqZ8P5PMbNxvUWL7M1LvMBdYZdKBq7q_ENurw6FDo_BFFARpuR4A4q4pq6hVy8T1dKOZxW5l3KkGIlGyCRuaBN52WoL4mEVKIz3Y1cVAkY0bhNIUQbfYy2-xmJVcvZSISoh1ykqRkXQzlfOixEwuMxOJKs7e50OguvUT47xwbo1oXcZAHWYjdSbxHS7ee1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azk7kjbX-yT8hksaPKomzhWQ63EH0VF8uyn_MvZjBIXt8aT7Rt_5pSpoP89uJrfVdH7XiZQIwV9Qqej6QLsmkTVIlmiw16NDTEFX0ZWvo-fROv50A4X73BYYZbii3Yl0aruQty5wpRwpDL5hyacHAtjp4D1-_t4-fLLaDxi3aBCJxxWMvG6HMLqxi7kfweiXr8-iwyLA3Tmlc9XYcgQF-MN-TSNmHou9swlt_fkXtcLWj0uoAkya2Tzbskxr_F2WDGG8Kr5-PUr3PKVKS8XRH5vCJOQt8e9s2ZWIM5GlO818ls1MUL5GSkkkS4UUjoMurDz0DGtN3jWH21M_9TYR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn_reThGVDJylybP7nQtU4VSakKT0PDplBRGHa16JpX15b8strEwLgGZfXoa93PLZkIkEIb_8-PcMbUuXp_VvuK9wWHRXlVKCu7AYYprUr3j0P6TQkjDoqRzKmUZWW9H4g63Uxmqjd3Q9xJtayf-jYVgAknmAT6cgnD44PgHyhQdV3swXDiUb-XChuwi8wf-kvdkvVndNc-fUaAePCzrBzrpPu1OHrP3M74E2vnXPSl0reesJY3PWDrooe3qAmddpcmFMFtB8hpFlWiPKUVJ6iXD9nRoX9R-bfy4R3hq33pKRy64qWEPcbi0QM3O5tmWwFhIlK1kIAIGBEnzyzbT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCOIPmV3GyUQg5s8yhOznoStaRpKgGm8jwkm5kbr-AqUle7qLWCTu1SyX9DFnCLHGurnthdOqZyFF-nP5-9ZDXKUxNrTAmzFUN9QW4M-9n7vwsGCzGG66u-AMsNwF8qTh94K1_cxXXs1ZgZkCcyewHxdyzy9XVyfh3hmm_V1svxHXZGanq6-LSb-rey72JCf-2_I-vnwbJq-YWUS9HzXOmEZslk4q73cCld8CRGGHB9FYGraAi7ZvmuOhTALDcbXIs0e5JpjwbCS-yRO4S8rzBYWtGSCEHm4IBtBwnNiO8wN5qlxEvoDIAcsvqK7rJqLUZfBq9eDiOiar0H38OKMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2FfzCIA8w7RjWnKYDLuhPTTTx96kiow16aBbn-YfebNueg45Z6MUJJyZFQEg1WzzaKtQ7uw6vy9onE6LGEPONKHzh6mixd85H8Q2drSirFWcS7iSG7xacrWQHBAxXMCmNW8sK6CCMWMs6auN04MhD3BWT2AFDPwrTfZLQgmK_gl8VBViF6uarzHGrmeCdCs92F7rTnHOGQAFx7_aYUItmipqq8JT1fQIDgkSp159Z-mIffMR49vpHTy9I8HYyCbzpuWEgniJKhcN9riM_pEYNoXYgEgwvNATMcCmnRujPNdAUHihVcPgVhOuUUZmPntPbga8S6SkocXKzFzRvIEEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvqUhgZC26Kjgr8OgiVlb-U6sgqZy6A3cDS8whBucziBKKjx435QOOp19MuaJ8ji9blGIoZEEIvu--enjFYx4opsD01dZpLCctnS79t761K2HRu5nmUhc0oNHPS60T6OZfKSLCvFx21zGPASvGi6nlAA4pCXg7DJx_mkdZYQ3UeGJh2WhvVP-iOsnC1mRCnNXh8ygk8Y3qCOLpS79We3m-yO-BS-8rbGoI-4taRx8FVKXOab9CqUmy-1f0qxgrQXJ5nz_x9EPkAqff0HbAfzcR6nXZC77vLIhO-kqb5-VlQakQJHdofcKQCQqneCP9azWP1qGke1qto3_gmOuoxkzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYErmoTNfJB0Mc0mhR1YQNXy59gTNO85KqeOoO3peEhKVCJoHHz7TF10TIbtSdXTdJeOFsyawlsA61_Va4qsFLVYHHvqCdH8-KAa9_BcM98-s1wD2lSe9dIaa8vlr_sbo3V5qNB15FzjqMzuUp43Mh8VWFGFMDPG3vv6FUYXBaEsRP3nCTtTaOENVwCA0lwMtdDrR-qaRACxXJIrCwY9yO3HwV0cxbpmJP7LhrFTb-hdUa6l4JvPFfIQAwGoxaSGev5Qn5BHDpt3kEJraY1lAxwJv3QX_AHImXUJyvuTPgKFgpOhEayUiuXUHHdDKc9HWUH-QSU8PUXlXYvLRLhyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGYKeLSzbiXKZpcb9PzuNJVZxRhQE0UkWAZ28HhILngCCQvaMI-h8KeJGN66m101fq88RHbvTc6k13ADcdetbVKIM1sjiPprauI61DuEV8BgRudPEf7bPlxuXUlTyibetfQqyyoXTDpwDs66ArP8vyIfWkEOpQx1-wtXcb96JNNWddlTvvWaVkIQKvWJX9jWBMKPU2wQFzCuu6MiRawHqs6ebCISHmS8bf4zRkLvbaDyr7Q1K7WybGvHIiEoBLcoyvQMKA4S8XJwzCRs2FALvd6bjRNFjcv2OUZGfL7uItw7pkt7bYGC5Zeh0mLtyUTDlxM2UkttocQogbyJGkedZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=LBsSe3UY13l_e2MGWKCQ2DHR3KZON0v2-ZL25aM0OZOc16KIUOPFJPinn7bRIk5HMz_JLScLiAaktR2wc49qaqwGv6f_D0CDMf1Jrw9vUoR7S9DBsUVVNYBMIMNiXEX-rkPCtTUiAmjxjAQQ8nSMS-sqD5GQ0eJhqgkZ0ZxccH9kgieXBRgkAko_hO1BBHhIuPNxrhvmIoeH0QUbA59HF3utvYD2Wvk13N2zFnR1Jkm8PXt9FY95Lba8rgR2kdfO7XafycbRhotaIXoVjIdQU-vc7KXVKj2vzIrOw8JRmvuP-yNgMIRlAwAH3zTdAGUFfXeKWlms_owIftIc9LLTxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=LBsSe3UY13l_e2MGWKCQ2DHR3KZON0v2-ZL25aM0OZOc16KIUOPFJPinn7bRIk5HMz_JLScLiAaktR2wc49qaqwGv6f_D0CDMf1Jrw9vUoR7S9DBsUVVNYBMIMNiXEX-rkPCtTUiAmjxjAQQ8nSMS-sqD5GQ0eJhqgkZ0ZxccH9kgieXBRgkAko_hO1BBHhIuPNxrhvmIoeH0QUbA59HF3utvYD2Wvk13N2zFnR1Jkm8PXt9FY95Lba8rgR2kdfO7XafycbRhotaIXoVjIdQU-vc7KXVKj2vzIrOw8JRmvuP-yNgMIRlAwAH3zTdAGUFfXeKWlms_owIftIc9LLTxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBaole98jKYCf4PWW-PE-z1kxAtPUEkgmrGjS6q_5j_4n1s3IiraMsDUtuUgAoGAw2aULfVhrOU3Vm21xToTmLSeg-nA91mlw6oTheloRx17oi4YYPEczi8XCUlAf1m0e0Lv1zS9Q68TrjFCOOet-yfECjN7nhgYSOe0mDUXz9qwBH90dzlQkIJGptzFrmx3AGgTIEWkM7aEDonMgxUKSC2KN09WtZ-sJxX3aRMMvMi80qecfQCKCBpeu8c9EMMIA2EoyRYYNl-gyjNBufFlIt4fMCvzNLylqHebLFEKtmm1gPt9eyoCWmoovAdRMfMyhTUZmKgTzvUbiKF2SlEdHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=XiUmL3kyv16GDP0EA3YNh3urRbyFflNY_ENsxpY5CRKfrjilE8KHmaE58kW1ay0WVr8XzJ0jRCNEwOdNiRRAj50Lcr1SABx6Es2T89zX8xJPeIg722s1ZghRhThurmJxgcLpm8jijEp2KxosR2T00cMnQRj3AkZF9CKIkXq7sOO96hBc9-T4T3tZFg94MJAZh7KEWnDHNoDLRwTQNpEGjobdW02cReKzlJSxwQIDOEdCtw8luVensQHQHvkBtmZQYIcviurkZq6bRz9vyxDJsGuhHmRcI6WZxvVbtvSBn34Hx67gqU0zoXs04yJs8-fR0ZeSZXBgVgWNj5FdtTBfpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=XiUmL3kyv16GDP0EA3YNh3urRbyFflNY_ENsxpY5CRKfrjilE8KHmaE58kW1ay0WVr8XzJ0jRCNEwOdNiRRAj50Lcr1SABx6Es2T89zX8xJPeIg722s1ZghRhThurmJxgcLpm8jijEp2KxosR2T00cMnQRj3AkZF9CKIkXq7sOO96hBc9-T4T3tZFg94MJAZh7KEWnDHNoDLRwTQNpEGjobdW02cReKzlJSxwQIDOEdCtw8luVensQHQHvkBtmZQYIcviurkZq6bRz9vyxDJsGuhHmRcI6WZxvVbtvSBn34Hx67gqU0zoXs04yJs8-fR0ZeSZXBgVgWNj5FdtTBfpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=FESdgQNGJzfNz_cvPxK1chWU-qrgRe0a59lVZYhefTnIRWCxMdZQJZAh2x4ImsW4thtaGBrweSUjxlJMzQx_WrWMS-gPMlIKMZUhadgzZwYZCGr4vOyUf7ZAw2L_knf1sHXqKwOto9jqOmgDofZfBV6SjpMUIDKaQCmCSDjdLuRmlaW3Y4rfKbsqzJJaJwwqyD_0PA6jPKyDbDHPFrOe03EaYrGZZrPhItqDmyNTrDxDA_NIqWL5gyVYhfXuNjBICrWGQd70oKHqPCogeE42sB4CseiM8Jx4AwLhyX-KiJSOXhF-vc27vlTNgdG5YHUjTP7rI1PA6k4WexwMcBrZwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=FESdgQNGJzfNz_cvPxK1chWU-qrgRe0a59lVZYhefTnIRWCxMdZQJZAh2x4ImsW4thtaGBrweSUjxlJMzQx_WrWMS-gPMlIKMZUhadgzZwYZCGr4vOyUf7ZAw2L_knf1sHXqKwOto9jqOmgDofZfBV6SjpMUIDKaQCmCSDjdLuRmlaW3Y4rfKbsqzJJaJwwqyD_0PA6jPKyDbDHPFrOe03EaYrGZZrPhItqDmyNTrDxDA_NIqWL5gyVYhfXuNjBICrWGQd70oKHqPCogeE42sB4CseiM8Jx4AwLhyX-KiJSOXhF-vc27vlTNgdG5YHUjTP7rI1PA6k4WexwMcBrZwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSxIOD2cnprzLVFrB46VqEqnPoygMxLQJys0S6KxUKlexbcithA9DK-ftIbQllcTJmIl2edMVE_DxORzqjxFmimGHpTi8n20IekDZo93nlbDRLTVcwxrFLwewjQGzXfJiIeJhTLy2BMky-jkUGwvxfa467NrVqRCjls9uazEuLsHB_8VfNDPHLwwizCOyEqQJec3J9xIvuDjG3_43Fmoupa-NnFOoepROvZnWl1WGFmHSo1MBEi1uP6NBf-LftyTolLXzfk6kgQuKsnCAk7A9nIcUu8Qmbbylgu3P7vG2YJq0tyrxxVh2tWlqClfSg9Eh9b4v8h3w_dOIYFghfzOdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5CPOPF6U6p7aMJJIkn9TvlaXF_tQz0HWs6j_C91BaqO2RffxNVRbJRCSVDs62jW-BeKhoSevWbqjY7q0hDeOGl4qzzpe57x0MyEYab-rmmrlzEwZfFnU6eqjgicifyAb1J7GJCBbUPJk_fYFIsQpJ4-or3oY7PK1h7i7xWnOJEIlL6yOQlUTPwMaonND2tidHsAqB6u1JxT5KDfWeej2p1iO5fPDjinbfcnTmuOBwiDbwnTKkCqPyEiWndkXk6472aT5NHzn2_szspbFD4slEsRSWysaCEdQz7bgQIIq6RHJbnF9UVdKTk9Xw3MTFAdKCrFnMQEZIq3ZBxJ6tmFJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Zxt7uFAZvyV8MR4XDxeu3hTVEQkRcIM671fZSiD8BAt1K6DiXZ4fXosS3ZPsluKxDSMU3IKCbEgKVK65jU-XtV9urIwE3O1CfOkOdVX9ZvN8tA2koAUiOskiS-eD6_y9TZyEvq_VuHJ6zhWWM1cudnw_N1ewd-SPLsylEK_9kc646toTaMkAimAA_XOoibz20PkJw8gaCg8WRcb1ye4jpCz1oUOjlRZdbU9K1F3QYB3X2X8CBCJdR-YzaaHeQeOXlbFRcQb-Xhm9JO2z3hvU_MwbraU2Gs5xyTownsgBZEtvjWLpxG5cwZRsk2nnNG4DQouIm1xcXIM7KqdF0Vm7F36uPJv8IwHc8usYNSFl3M-mdHvybkUz_1GNsW2SU2btZwPu0uJKPCQu_LSvx3v67e3tzCA3typoxUjfLdaGnvgri9RLM1mZd4d97_oS1-9egCI0sQxROXXHcLpt3nonmxkDrbMB1cTm6Pwgx49_3pxPosvSfnPr9FL0AlwZLdP5kzBbpxOj3wTKr2Hxn3Zvit1BojF8sKg3qyImunI8r5TRVvMGhYRSxeQpazr2i09TyxmzjSBfPpy9cpkm5KXkcJ79FrEN_tvM2-79DZs9s_P28W4MkJWHv1Lkl1EZ0KrzBIsM7I2poWND3Eyl_edY8JNRp5hHqXvRSU3Y95_BUzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=Zxt7uFAZvyV8MR4XDxeu3hTVEQkRcIM671fZSiD8BAt1K6DiXZ4fXosS3ZPsluKxDSMU3IKCbEgKVK65jU-XtV9urIwE3O1CfOkOdVX9ZvN8tA2koAUiOskiS-eD6_y9TZyEvq_VuHJ6zhWWM1cudnw_N1ewd-SPLsylEK_9kc646toTaMkAimAA_XOoibz20PkJw8gaCg8WRcb1ye4jpCz1oUOjlRZdbU9K1F3QYB3X2X8CBCJdR-YzaaHeQeOXlbFRcQb-Xhm9JO2z3hvU_MwbraU2Gs5xyTownsgBZEtvjWLpxG5cwZRsk2nnNG4DQouIm1xcXIM7KqdF0Vm7F36uPJv8IwHc8usYNSFl3M-mdHvybkUz_1GNsW2SU2btZwPu0uJKPCQu_LSvx3v67e3tzCA3typoxUjfLdaGnvgri9RLM1mZd4d97_oS1-9egCI0sQxROXXHcLpt3nonmxkDrbMB1cTm6Pwgx49_3pxPosvSfnPr9FL0AlwZLdP5kzBbpxOj3wTKr2Hxn3Zvit1BojF8sKg3qyImunI8r5TRVvMGhYRSxeQpazr2i09TyxmzjSBfPpy9cpkm5KXkcJ79FrEN_tvM2-79DZs9s_P28W4MkJWHv1Lkl1EZ0KrzBIsM7I2poWND3Eyl_edY8JNRp5hHqXvRSU3Y95_BUzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGCMD0LOeUWRjALosY4vAhkOrm6oVO0mBnrpgUVJnOxHA9TqM1UnVDG22oWDkTUWnPPOfwfXaTTRVCPAoGZTM_WdYmUDB5CKUJ_IfD0BE5l14qWNqvMQLGE0HE6JRqCHpWEPGLsvPLhe9zTzlT0aHc-e87Mg7CNTMG4Jgk4rmRAi-JuVMEza2zYbDun-9mNTxltRcyWXaFzHi12Km-QkHwXXuUdMQis2g_E1YVZUi3J9r8fMr9VLDMH28S7Bk45iLbz1qxik_gJclvb9BA3oO78iiP7MMwm9pybRM6Yo73lhGqb_G0aoGFkJvtDI4smKgiFuNVttWPZ1ylni0To-kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=qMT2Rkfb-lvbUXFwBNNLt1FskI86-K980N16aaR1jB1GfuTH4OB9FlVzLlN9srn7pBjrJaZttajU0lbSWC9J-JfIPVxWW3OJgctJiSei68UaOmVLDdkssEbCm015DpPvLRVhIALdaKCB3MIILRWTVOY0tMynqAKbZ-ZeeqLMMHRNrbh_ozptwD4JlvFoTdQ5rSD-2qtRiwkbpJpHMe9VtDa83tF3sD-lsX8IU5seBQBJSstTazy442smsNPLMUNthqhZCTPx7A3L5XecFJvSf9GYIgf6gZ2CIbNPeqNBh0aVgxJ-5kK6i4Y5uBmL5-sNY3_qydFNGhe5Ck8I0l_uGU83BnTRo6yjg997HPAHW2xjDOw8EEWeK2solQb0ik9fhebNAixGrcoTA4TG2frUHVEdf5kRsFRC0zDjziZ00BFtGRAQf7VRwlniQn1NlcEs_p5g3WDrKp9YYZeFGUV21_rywwmKm45wI64KQwj07pFSpojlXIXZ4n3kIebfys701Trgi_S6KDSXNaHOkFsvP0CBykhIaFLhS6QXSufpkI_XZHLAfs7WZFszVxDLMmj7CAXQ80DTLs1aak9ZKILX5_PnZ2D6dXKg0KxcO4NMqGmQRsMf2YSP1Vok1uFZB2tf8robSmMRPevrpVi5_9jH1zVMbGomnBc5KB-J3SWbohQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=qMT2Rkfb-lvbUXFwBNNLt1FskI86-K980N16aaR1jB1GfuTH4OB9FlVzLlN9srn7pBjrJaZttajU0lbSWC9J-JfIPVxWW3OJgctJiSei68UaOmVLDdkssEbCm015DpPvLRVhIALdaKCB3MIILRWTVOY0tMynqAKbZ-ZeeqLMMHRNrbh_ozptwD4JlvFoTdQ5rSD-2qtRiwkbpJpHMe9VtDa83tF3sD-lsX8IU5seBQBJSstTazy442smsNPLMUNthqhZCTPx7A3L5XecFJvSf9GYIgf6gZ2CIbNPeqNBh0aVgxJ-5kK6i4Y5uBmL5-sNY3_qydFNGhe5Ck8I0l_uGU83BnTRo6yjg997HPAHW2xjDOw8EEWeK2solQb0ik9fhebNAixGrcoTA4TG2frUHVEdf5kRsFRC0zDjziZ00BFtGRAQf7VRwlniQn1NlcEs_p5g3WDrKp9YYZeFGUV21_rywwmKm45wI64KQwj07pFSpojlXIXZ4n3kIebfys701Trgi_S6KDSXNaHOkFsvP0CBykhIaFLhS6QXSufpkI_XZHLAfs7WZFszVxDLMmj7CAXQ80DTLs1aak9ZKILX5_PnZ2D6dXKg0KxcO4NMqGmQRsMf2YSP1Vok1uFZB2tf8robSmMRPevrpVi5_9jH1zVMbGomnBc5KB-J3SWbohQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoWJqlYv7TjTgz75inUoq0BHvwm4Fk9YEs7lKTL2ntjdSNV43d1pZtwDFYk41qUGKWzWVTmK2JFOMnIUgp6y5Y3mTkB1_CkVqlQ56x5EFbgKTrgJPBX9NH8WFJYMbitpfwZ7F6UJX1moRRjTOvs5Im8Vkd1uX-xJzu8eXz85dEchA43zah1dUL4uH0WqEOwfYWb0r7QSG7l0ZN2GjzDfTP8Ha-h7PYsIHZ5mI_ZIr5yWkTpG1AiebDykXfydQQjfTWnNnDeQMlE7wvcVpmQVjgJnzyyNHe5eHBNZdz8khmNdP4R38dESOBf4AvPEN6cXXes78AVBQtMR9eGRGDymMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YscgI1Qzicf-rgBg2jkM0TejObHw76TftabDcyp14fUPHcP0hsi-8ZX1ZtpG3TqYvgIlmMbS85F7QDBQWetcYGv6XbKOp7QAwmnoy8YKbpzoodHLjF55JeJmnDKY8WBtjNBwBpNkiJdWu2AlSuO3C_UEkXBvFhzquGeGqB-2QwANMOAN2whVSC4p1IgLHr3KFP4u0Hsa3W3Uq3J_hHtnsnXbsjHS0p3IbECM4FjKVQb__A1iQYmxCDLLBP78OfGbDJ1MOJMfp5rZX3YycETX7E_JRTl40gB8GBwzJQ6ZiLcq4nsUWCWBVNLY5Nd5ZP5sLJbZlitDQAIos_-OQay1og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzlrH2O3rG0O0CKmAvKqwDkRhHF5P1ZUFLq-CnTb1AbSF2q5bArib5z7q4XcR3r-PXpnCctyxghtDIjASNcOS2BDee0J2Ds3Q2gTQYTpjlFaUmto9P_lgRNBF0Ugnh3uwV2AdGE9ogLP8NZvUgo9Hxq-l0nxERtvpO3WgNBJs_lmtTKGn7zACtYLodC-9b7VlTupjT9bxxGoHQu1eLukgrV0cv0kFciSK5ptdM2jBrj2JNrOkDdBpQUbZ4iZudrNjGFZSN-YrE2YjkMDSzOt248kUiHVqWznO5LOpI9_Hd5GMiauNx6VBGqmsQdsuZktwEpY1jAxPWLJibfxEfRxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffY0fukBNglvFKPlVvJ-zqQfTkxAl8B7P8mB8MLKjaLFdKxiV_EHFergozugPC8sFyyy8ta54O6lVyegBLS5DCpplwrL8QqZNxBip4ZkSfd9xefw2fCkDzfbQia9Ia_fpO39scFYaAz60EAKISaJrUtfCtIS3kR3Nf2yRxMJV2HwcHJEKABetsyAU8MyobGXIgHTBQIDg6RCVzet6wjToB2TTgCh4XnmbTJ11WcY3m_IF-8f-1xxFJCoT_U5s16QPMqcUZjbjAhuPUGQW22EC7_yybtXZtoKynShM5LFDSGZBYTOdav14R0N398sMsFmZwGeLw2q0Kcd08sp29cT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8Erv4vQkFJA6E-bNxmHcADZpqceUUF_6Mpu1BSh5umxCS2k7vjiYZDjgGUBAPFB8t1YMm4mUeBguINoGRcMnoJQFsMzn9r1vwO2ljY8MtVIHDHSNAXHaUn5fDt4fDcMURS8XWcDB28W1IMxlt7bdg8eYFwjOVA3jDnKn-yEdba2jHb3rB9yxUqVO9_spGLF9qlY63l-BeYz5GgNIBv9h_DfNGrWq4UJvnSCWxtQRkjqLlT2_NHXWxV8FQjEB-OsuJwTV4gHjnu0eVU7LGrD7HLDJ9LGDf9VCt768qotPFc8NDI2NampV3mOD-obmYGe78qiU_oNFRUFjJDg3rixPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJFlKUt9t7ZXtLbT445Mqmp6QVezhLqEMgFHih-HGts--lQcCCIT0qZZycRsTiOpj15SlbSblHGK9lOdG_MeJ2z0T9tscen2RzNFmhU1CvtHJNph9YMLGJNH5bUgpWhnMz6ozdXkYX3OxEgF8W3xaNznAHMn5XXXCNl7w2Mt9JKRa2YJYBhrNti-etPdNnhWe0Js2V09sGxcEdTykFBkv0hdSpv2qqdvgPzhab7wIInPjuqKqFk7qCiPa7SdKrX2_9SYgxDQT_GQJIZyMgsWr-39dSMhsJP4DFw2ZMXJRSGyuRUABxPgLHG45SAhZUWYFGMmDyrJ5xtTMhawYrKzGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut46BfTF6q1fVsBxyYVmcK1OvhlJEd8I51mdvbrUZ_Ei0zdPa9HDP3_neHf99k7qhSA5yRVOg-YqjvLmKcsEIM9JAv1q7ykij4zb9nNrX7YRkZ-IxJQPoXILXbSi3BpJzIAILcwykOvb5-z8I5X-2LN2OhWAKumN60ScssSQK10gJLw7NlVEPfpwWSVE9oYc94Caninw1VKUJBBrr2mBlLcNZ1JZIt49ReZr6vNB4H-FI7aNHvtp7_vBeC5zB5ppTcWM9sxfDvEF0RhRQtTbc3dhqqpI9IXFt5EgQa8LPyXwSvYm_mPvLG0X4i5MrA8FdzMaA5uvh1wDtUmti0E-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWfUob4aXq1UeHBHbxLvUWVXobGLCxzO6EPNBhL7x8k9hEQul5dKniePeefyLj8znzTYQ42BVIP2mLaR9X4UPnuXmTvJjgk5dpPbXxICwffjvbl4EJhg3pGNwW2Iy-9PkHOJaIl7ni0OtNzKed2tv7hCZOFrNJGKtcay-FVKyaJio7HibPwGmcSMIj8DiUzVMCw-62SyTCefvsiO1NsvnirsfjRuuTjwZXOQMP_blP--2MfHMN5bgncyoAgHY7sl1RmdHKvNO7_iuPHH80EfiH1NlqrnMtksKjMn815ykLLtxv2kp6PvFIKmY912g_1cET17bUwokIuQrcVOBlttHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi5svtpQ3-d1DB5xh_sd0R1TuFO-n6OcsgBVu4CyDWMz-7UonhRIn_BwQMzQKJU3idx6qey_i3A9L6Tn_05TijBzfrEQHFxs1mM6lAE5_3OBliejaC_3r6-xI1m2DCJhZqfkvDKnrPCxj3ikDAc-Z40UlU4PAKX_p-NgS6IrmkYaUFGw0INVZOrKgb-HOuqS3Q_hpUV4CUh8EYhB_cD52jb2oBkL8-8RrOG0QmojLCYsYXB-8rgomK6Tz363UFVv9hwS_aFzTa0V6g0tJwDxruR7Ym1O1ZDCqeZPxyOmZgAdiKNdhbFJAcJnSAsb-VhomlWnJqYU-6CAd7ZnQ5UaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYpzYS6AAq6ZM8hypKeok0WCQqRfxzmr6XElIvBXzcuBaJQq9V7Ig7qtkp2QU92I5H2QZrJnaM1rQWQcemc9pXt05fsa-FkwiISpS_v3sQwL3M7jvSbXLCdYW5tgMlr18eHnD5rEbEdxp4vLqsFCMSPmPi02gTE0Q_Hkt3QxuC_PdgEz_d0WOyrPM5wNKgS3BCgQ2Omx_KbH952knHSbco9xZ9kev33hsuGS9GBXBNT1INeziGWSUccVj2z3S0KZp0WnU2m4z2OkbcC4vp1XJaFDJis9UefbfLFPky8tX9FqkGIxzmx-AayqG4gCo8xF9I5cAwtbmIkNl6Qk3Zr0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuYstg-_PheYmKZqs2VDHotA_ZTF1xyugAnD4A-P_EQMFVtcDyCytga5h0LmgiIxmcLnD_fMZfeIRlc0oufz4JgK2c166ierWiIuguTQoMllANkJHuP_rD6h3ZQuhteXsEkIDvyXAeve0uNkhFdFtaEA8gI4qfovpB0abYnURx3qrEebdzgZIckQR5stA0okGB1aCCOUwTUBdkItcfpYhBxC01MNHiX00MFAOOAjBJz_NuT4ed-k-MgC5iQ4XWaaIrMQ7D65Zrmv6V3F08sdI9vuwgmaE-5aioFRWPnvlsU9ln5IyovOmS5F35XY4eAZB9L9KlaH2ILWvlLc8Z9bfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnwyCLkq01jtWNjvbG9VZypGjbLdTomTSkePR32xZWkj0izRIVnVTVbCSC0OYTMx8AwoxH1AOO6aV30zCoUC38CLGz6PskncK6oJar7NBeEYtfEyM_aJ_ApjbsLl5aKfOoiDtne4k-UqlSvGai52vK53QyIMgTa0FfjA_cjmb-H8OlTSGVUqABQ8NuXs9RhoPHEbOnxApZLiKgC5Af09CZ2IMGFhauttCWx2XCAmc1g53bkI5s6CHi30lLRu09NBpO_7kLHj2S5sZU9D9woxRV6KUHA3dlXS0oSD7YVDojfCVz40QiMQFoTvNx7nHzI7GZb6KF_yjgTdyBEgnIMePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESaHLjSOHNXT-HLBd_z20mRlNv9Ok-An167get49I1sHoWk08jq7gBrpS8MisGLKJostpREBymjxmG7ikcExWXll96IlsK65T8VlHSpcF3st5c4XVesDv0dVflr5zKr7NTZKGMHovuP9cJq7ezL8jOezS3U-EdxCUbGyhfvwjshXTZXHYXe7i9-l9mzUQ7iRhnoE2vsE2q0sKtRHkEYvTzEo75r-RblWzmUNMBocu54l_iPRLiEP6GAtq6E5vbHSRjt4NquMbkiWr4KfcozFuX8jw_u6Bj-uoIO_zTIW1O-vsErZK5MRdhFl-h1v_e6-vile7kbZFaRa_WgovZSCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZFbKYAg9Vyo_2y6p_EgJh7soGiKWR_DgP5exMgLNV0yp_FykRsorKvXVoGex43tPuoJ5E3I0iPHR5T9KKe8kPHgSgor91T0wtATg9BTswdZX491zQ4PV0i5aDuhZDwxK7HM6OkLfI_Z8h_cy2Xh3Ek8Iu73uXBqNWopjP_VMPij-qgWn1axMOOWeGRd5NS4keRzdFJcOUm2cu7r4Q58z_4kmze9nn9XtAeitI0vFbvkzxNZRKryq0AzgBDx9mahD9iXGT3Chr4WB6PsjbV0zkNwsZux4wrzG1Nqco3_KAI0GmiPWlcc3YfC4KaGChhUOLhio4rapaW2hQ-mqknEDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDEX6L0S6ktgE9CvF5jZEFc8Aql7hIr39tJ0P4-nRfnUzGyP170ZvwXz0jkCs05dK13tO-XbWPIJOrs16vMVsrU-C3SK0-XwMAxG1DXxcK7dZJ5_pixywTNI42YRxm1Z1GFDncfe0nr6QQz6q4wwigLPdr5obdiFRXaanavObeQ7IWhR5k0whxaGFc2cqrhtsqBXAIrOfgfsVQLvDsvBHKKjZuUvfV3h7T7kS7UHYKF2gpW9XgZ-m4eM1dZvDI3Ald2YyWWMGnDWeRihtJqsiH5e2zszwhKXnzaBBu7bs09aaBbvbaNsolHCBKOs2Mrbvx-LpG5-A2FqGMorB6D_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE0RIJSKg3tWbl77yaeH_6FIqKPhoFt04MzxwsYJ7QZ7HBJlTZnkXCL5oq7hIYBlX2u9-ABw-30hmT5GPyYdOZpgSN8JVFbz9vWJ7t5sLRlGSPnOFBenC2nl-dAEUNBAJzhzPv81XLP1p0WN5aEhM5MamEr7KZz8r8iRot8gHdLJubtisQ2ufNhWng6-rYsR-YXGvlB_D9j9gDu4YD3kxAZ2Tr4SI-Iia0FmUVFTiAYat915s-4yBeWbU-_qIzVwcMibt_suIyPfZYN2iBhX-NWf_6AlDcErpPew8y_m9vumV-ZqDCQG5Nc5BhAk93bmcId-ReILv1Jg5vqUT2ZkzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4wBukY2A7YKqV6pCqCAyROdfO3-gC2r-yxYaasnvB59df5eA7jEPUxZElKdWij4-SIlGScdmb997TWQi9z_ETWDJIuGkvHLA0U3KNpTuTi-LpbB7n-xzjL-j_fvyDXqgQjRGLKRlBfxuTnBoPddtqeM8oO75LViPCVUqZ9-MK9ZIlKu3wFcdzxTS_9EPcVbfpsGI-hkts5lUeKJ4n5L2e8tVyVhL6QaXorkvPz8vOQVPSRfM0Zql6IF37Qr2v2F2_KBzPqxVEHGMohP3ZxD2NCnlEtdECT4TOkED-PAaIHA-Nq-yYk_-WRK2lF82q75J6Y_SkkiSJoiBv_XnllKvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ddn4dfw5DTGJAAlTe4_NZlZwJUNrghCFUXHWj-YLDs0hdzmn6wlzuI1eLMtrxCFEnls8ssp-miW7SygbdN249vCAnLgnbQO73ae-t90znu8LGvFgE59HpJ6JXpEadgHo2BjWPUqDbyOZ8TS4IsLRUfYeQqsJe2unBWLTflQ7eBj9Ww1aiolXDj9bp5vpTD71BVeOK6h62Zd8oRTNUHmQrBH_TNwIsZTrnahCBUTxlh5_2SuCN-gJWF1VGDx2iQbZXlzdgMz89lEvsxrhgWeR-JEVVPG6nSpgpp_sjM65hry2XPrJZcEFXx59mTTg_T9ifvmHz5ldThN55OV6GlL97g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGJMP3UlamlC7MjrQx6UHEYAQSu8quQCOAtPatKKUgsv37klF7ri7_9FrLJtFlqjSW91YnMSVeLP5GOp1AfvZFIiMtAmaXYss9mzavoy01Mckq9PB53x5MyIzIBfZ6kpgMrxM09i9ons_l-yGHy_UUWdjZk96KrUnlyrnS1S7pwmAvN2TvtUPdSxn_LpibKVyWP7BBn8gjeYAGCVa7JjjoarxmsFAoGvl1gM_h3kAwd3Lseb1HWgTMFRgk_G66P-D82w9ce7NcXtB6dV3ir0UFy-ISV1x_hRppkrjc95sMWtT1KlNK4CkktCjTdzKPbd3G14QOdgiKvAn8FrWUColw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4tq2zdcMv7WCiU398aMrBR_0T-nxAmi0fzn_e_eGiEzU0OP8Z2MQ_eRV9F7NUoD5zncGaesZ_7KKp02uf34uRhICXjhiWxrBSNHFOBHTh-8SbMkrNEqtoLEgsZOiWrqVtIu1dI7v-l2gQUuvZd_lHdXlaryqSV85f05tK9EUO8l4lvDn8TMUHBkojrQaNBzAP8fpNCez3HlRFk0DBa8Zte27Ny0tioTWAQcAjut6qHvxaAFRYyMMLfFze0orXn13eQjKk-rSGr3zNu65xZarsZuvwbXXbGrp1m2jPPd37sUoTuOrsGR0QzZGn6NpWuhuOvjzJq7Zud8vEA-3zZY1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fii89KkdahrqTKSoV4aoLOCHDx9IHriPEYSnQtdTISdmK4lO2m0dWfWx14b6gntwC0WNbUZk-mK9SSDh013NLdZtwZlz34ZnSR0UEfpeE81IsFJYYozfllpvuwgQWmwufXx1W-7cqccXtNU6p4S4weSmc46GaT8bA-Mlin264XWcsP6TSyh5LrZVgbOhSUmILANFQtvyVrdViVPCCljAhy7vQjLPqM1t43u8aKdnvm4hfnYy7tHIMKUnHjWzjwNfBn7YTXQTDLxjN20X59bcekNTYXn2BRnX4IdZl13sMLWMQsxbTBUgZ0KM03BHFK_LJ0ed8sBjic-dJasEq_AxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJiUxMQ2rg5koZ8PZjkrgY7n3gpb2sP3P8ZJk9zvMxhSJ3SNMxbnT7N3Gackl4RacnEVyIOe6PRrU5jDFHkjUZDwN04fF6Rh2dQZKOy4KR7gX5ApO2yddlpwLiGIfzbIpR_7SnCDz3uylP4wKNKAJmc60kioRl-ZhtX3AwELseAgnvCHpFB__kxLPaIbmeuPz_gFHR-3akbULgGqEp0GzR4PH_wlyXIFEMMp50Mz83Wk5vBbTjQB1a1F5JfUpby_BAf323Cf8gzg-pUoxdWgNTr-r6toGqYdW90MSIeHigVrcv7t_vNA-z39NUm_yg9yyLSI0LBFCBrKJ1BPA_J09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cry9YQXkKhkS-7T1Zu-iwN101vbv4IyL5L96y_aTUjBO6o0zAT4x30uKVGCAAvDHOYiimRhnp5SLwpp4UgaAX6mjIplHOCNsSKOdhGMQ2SY1rN9_BvwLVXiremtgmXOorfWDTQwAVvRzJv0UxiehKQ9TAvDKMqi9iDal1dkNQozKNinqSohNY0qYyfSwmtt9xru8csvtp6yxrF2tIUWxzmlXi40lBA6-LZNm4kjdXaNO6RLyuSobrYIaQad2yLVvfAPMkPWKYsEL24EqMb6mapaHfS8TIoMa0YyTkq56zOUzbRahxiha_Ae_mGyeJBjOLxl5qLm6R8vDQl6yZZCGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA5l-uE7ySAgTveFpMaX_Cagrz45dm_vgMP1AVEelijHIWs9E7FRJ_X8SS7JeCIhPeAjThWGHFC5QeREWP6v3_Z81GiqhbPQ8JruyszmpX6ja1B_SG9C7t6B7fmj5-6gjoPZVdrhPejLtGSb909PkBmDHja03OY7hzydtRHmCHX7DJs0cpSJBs0vArEiLvBHIjlHd7xZCFELqi2VcWIKmthqolot-SA3J9UP65he-QFAlvpov3jJEHSc-ttZXGaWannbLNQedKARtL801bWNJYBIZt7wQry2rG7KntUL8uLFJqY8KeMLNDklYsdzJWz1tHhpDJzsNWfc5uwKYqkxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOGij5fqo9IJPrrvZOdQOlEWz3lZL7wCEuBZZEmmnNpvlDDi-51mduCtDlzIazqe7RhZi3C9cS4nA94Wi7g8J6wyI7EZL1tFy-jcjsuetWreOK_uf7QuwW1xZfcmK1glFrnMx71okFSEkMEXiLe85NGgRRhL63uE598H3oEMTBuv-M_RasFFRoZ2FJQ3Aa__PSm_1Kf5l3TvEJZsUPBJ-uZSlqqlCnrbKdmjVxZ4os_yVQMITcm34z40ay5rXUfPzE2c--xCCJHNcW1PfPmJYAIcXTRGnutIlTvZkH21cJmMPdvMapFZZwb8kC-gLhArdTahwsA5QVoufnXKPC78Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buMSTR8IZeqHyZuJz3j9JkOz4ziD6mAuisNpkGjHteMp1Ns48uMJgRUi0zriqH1r0rCzKPUf05DF0GTkGWkqrYAfi1MxvEwGIKnbikBfu3rgUJ0k80YGUeyOEGChXIv-G_sVmu232gZVUXQVxhPJwb7IJAXNi-u_1Y9X8EhoVPpnRtRDSBOZZhGXktWo4PUALwsLF3R0NOn7eL4g_PuUbJ35kaJya-skkKwDJx5WkX0lcD6KU_OHp7umRuem09BEPDPqH8h-ZjrLI6supmATS1H6y3_mXlEvoahLIzbDMuCl_4jmpOI-MBwSI_UU-pMK1kDI_RZUetjsyg8jM0LoBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs44P5gwlz1gHKBBGnp_IqYQR5XVaOJethY8Fr4Wu72WJ7k99y_Xsqipb2txm99NA-USDhwvAAp0uKlDb5u3cpJnQCdtEuKEkeRe7UIjufqwJ2GZGAONs63EU0dF0Tq-Zvnnlx_i96XcZs8a8tc7hwIIRTA1TPFKR4ajUPtvrF9dAuNyrU0YbM513K6iZJ6nKYL2N8h_nbKNj9CdAzcYgEVP-Nchn2ft5Vzel5WWzR3lR1blldAk-23ZEaIAmX-9Y64PiIaE6TnFPw1_bZg8fIXAU-Q2SD9RHgTBl2o89kSqcwhLvAVOs65GynZRW-NwLBaXfrwn0rSPz73ghOSAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZsnJ7QsL5JysJ4gXXrZJipmbLv9MJ4Phmv3ntfsfH3B4NTOY3NEWdLdf2HqR88EGhLrlMu1u8qw3kF2JHuztNPRcHmp_YZD4lZZtYiNeTKqM-7l7De6I_XJJ3ErGjUGh5AXoeqWK9tYPosSnzZwIo_L-qW002XxuBV9XnC3kCnPnlgG3p33yGpNDhK_V2eELdAkVRJDpnfR_zb4Ed7PNE9BDti_Yq29uFmrUIY_TVw4dS5pT-naE6nS-aa5TjNc42rR70h6ij3UAbD0P8yBEiufP_8Qo7ULAE0-OTGwP_KGkbpfxCgbPgaYNeiJ-PgteMkcGNWErpOgik6D-L6zuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCTqVWJKd8335ZUuwyYjtwV35cE0lq7vLse84Dhp8g49YKU_-JdzktUUJjiWLWEHyUWJYMeNoAgr6TroTTwuASUaj_zlQDdAX5rQnUZW3qwIblTuGzpjg6dJSlG4YikERnLfxpT3ZRMrK6gIKgRQYxWyCCDvcmtLCz4I-I9Ka6ovWAIZwi8eQ7DClqHW35PjXDRT88j0jxrvVelkIdh3kndHSb6wUC2DTDX2HuwhmPp03eL4-u-KtBin84sUybqTCJX5drQUpmmiBGynOuFKsNHdV50AnpGoh2gwAP_Cpd17adkEQm-DqlwRpGb3EF-lNYgxOzZ1UChyd19sCO-Lyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0PcQSkWf9uiBojIFgxRLpfx0Eugvvnwf62WFb2pkVevTvCxSiS7nNZ_th6VoaBTc_7M9p3o-VUQweNenhtLLH2rhQiT0KShqyd55MENoV9A9D43hSrfwyc88YIMreZBk3KgD__YhpN3e17zn2PxD77REI_l27fT737Kfj9bcl_q1cdSUyN1PnNiGeq3DfnLSfoU8DkfXOzMSgWkxuiM9N1seylhmSNFNsiVfQsmk5AE9FAjMB-e4oJlXvPwcgQZ76dMLJyJ89R4C5g6b35x7IgoNLd-qXyiEpDnLW3eopxUF8JvfpW1ZIkPRVBQbMXVNIuhaTpaTakbv8tU2HgzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9tYTJsJx9vBBzfQQVXuyEEiiJwQBqlCcihnTah9PdnaoCQRIZk_oclqUFzt75JGoEeMMuR4AJtHz5EDTYrzGiuQLKj-9pilyQwye1ryYNvoQZgVqmOusDXuhe4HusQ4Gre4LNeostp-CFGzmyGlY2Gvmj-93SyNXZgY2Q4esZhbhCWB6Atf1VsujbpdX8Mao61EqTXh5MPd5rUzJ3tctOTZCzUbpssbhvy1ScWb0pvaoGGFiUaJRTaZSIFXkqlzSygg8cY7uzsBFaafa4VCMLMi_Z-49-siaBrlY3GcezCeAfxyckj23GcUsQ6kKx1Nk7KG7GN19N9QMypwwud2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoFAxn8ZIo5UN2iqhDExZlFVfC7tMg_MS9D30-acIxfg6jwYnGQyn25v4t1ttcJitWzV1Wv1vPV51zWuoS8Ykrc6v1InOggBME3fJQm9thyOAkBejEtVCYdTnBV03cnM4cMV2PHgc1xXMHbzRJLyZIsyqXnq8Chv8w8bd-W3bf6zOT8PYqvlvY1OsnP9zEQKvEtdgvGEtKs5wa5KI61Cp82yEB2N1a3HxEt3PTAlsrg2J7C3TJ3fa7DxxH-wSOvGXAKdjZc-RIwkvfKvArHKdCD6tzUuWhbwgnpDVpFmDeZTVDG_WLVa6jkaSQlttCbbO3MDb5WS9x6b9tX51AoVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwqFxRKVSmqLx8_0a4vc-jdPZHQwLJIh_eLpzPj7cWbLPsf5y-ub1TfyK9TrQ8BsSNP47Kib0u1O0LykjgXYiE8FzezhB9jTjREX0N0y5vRjnqZw5EF3iW6GYB6FxEExEF64xpNpXEdfodid9IWHKPvx1L1sXD9lNKziGPBlG31LhgpDy3OYc7yT2GVr1gf-VDjRygSRwZhYuwISvovmGFHrGYrwiZsl_UzpSH2WwDZi7abYR3iaFstbFonEUrQ1uqf-zQxFlrim3QxuU9FJWRiH0speBvlV-lF-IYNFLiLbpKv6WnriwiSOkwaCJ_yAeWjcHcxrPoBGSJEk3HGPtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re9k2upT5UJ7E-J9oSIV05gHrDk_BkI78gbVUGPXn93dON-YCPGx6TyZk4aj5inn_AgASTeWyniJGpe7WQqkYDGoRwS70QoMH7B8uaxdVxYVBpmOQsBGiGkMRdzsaK-o6WPH8iGlFiPGcmrg2Qh1ftTb1xuwI9DJjxcJvMIv6SYUYsu8WMdz7gKfMMjjkzZix20cNv5NIdYUpXwEWbTNuFkcAyCNXLnahF9YD6EYQBXT2e_jngqKzlSro7BA5Z7Ubw9GktqKw9A9LuX4ez5KI1ozQdz12-8UXlQgqB5XQod2oIJT-xSRCr1KY5b0VdcI1fVrlfBKB6igUL3CIJEfIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=BpKqjklDZbhM1yulXE3yJd0ip6SYMMJFj3YVSIM-irCuDUP72MNkOMIrf80JdLZcN-LtMYBiuGrK5n7xiughVFsnSTbWwtnwP-Lv4G6N-KyQEwYKvFSz-AnNZ5AFnnthOOYQTiAMybaaWBmKxfmO1BsJaLfX8G3tW4zzOdhwvMkQVCkPHp8yjpKO0BiI4uZ4_Ey2d-IzbHZvgOguzu0-BL2vPzO7pUnhfSwFhLPhAbYEiafuyCLWcayf99349Cb_Maghjx1gI0DdrPXLR-ee8HrXdwPiXGCPD8wKljZ4K5ecOTd2iZ9qRuJTIT0Bq7MobYMU3FMLZxpYhtPK11BAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=BpKqjklDZbhM1yulXE3yJd0ip6SYMMJFj3YVSIM-irCuDUP72MNkOMIrf80JdLZcN-LtMYBiuGrK5n7xiughVFsnSTbWwtnwP-Lv4G6N-KyQEwYKvFSz-AnNZ5AFnnthOOYQTiAMybaaWBmKxfmO1BsJaLfX8G3tW4zzOdhwvMkQVCkPHp8yjpKO0BiI4uZ4_Ey2d-IzbHZvgOguzu0-BL2vPzO7pUnhfSwFhLPhAbYEiafuyCLWcayf99349Cb_Maghjx1gI0DdrPXLR-ee8HrXdwPiXGCPD8wKljZ4K5ecOTd2iZ9qRuJTIT0Bq7MobYMU3FMLZxpYhtPK11BAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIPIbiKFWd--4IBI_gYmcLAGCRJBAl7EzSi_wraBEb_KTpFOKEWPw6w2Dh-8dFYrJtN7KVA_w5ZDrLk0ta83-VDRwfg_3XDB-n9afgt25KD4INC-LxOpNaC84-BiRYwYUlZQM3e_LSBrAdTaInObxm7MYtUI1QfcfH_bI3BSkub3fB0IB7ZGXaXDEDv4yUzRZCHYy-G04jNjwYEclmr9t_8Rm2ChEJudVIsA0GsVZTpGDXDAaGBEKq9-BAWEaOPxHa1YaEiGGP8R5uSTiez2FQKMoFdG9J_HVARpvf3cVax9OqeWAsE6tDthv5voShimSUgOAL34J2dLxYzsG8kOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=v4qTx56F0PikYY6Vz7K3Whn3w50rly_kEofsQvQI0JD2PNPJw6buutojsVxIGe4Ihi70UuhMFnx2ZDqLU11Bn2FmjvTgMamXMrO5L7YdGdfN-HzjFAABQwD1WF7NWqJxfXscxS4-_eA0iZcB9gbYxbtzaUKMreO5bK0a5fzuF5St6-hgMTUc2ft8w5EwEir6JvRuRSS-HlT8yaSOOsJpU_0hM7dPn-9J7vdNZsFkXe2I1eXim5Sn6oMfpL0H5qNLOSKq0Y2mIs94w5u_anIo-_dnctTTsm384MnD5PTaGdNE9TfKKKRzcBySNUvWbklOPWppdJfhF43vjhwlw-5TiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=v4qTx56F0PikYY6Vz7K3Whn3w50rly_kEofsQvQI0JD2PNPJw6buutojsVxIGe4Ihi70UuhMFnx2ZDqLU11Bn2FmjvTgMamXMrO5L7YdGdfN-HzjFAABQwD1WF7NWqJxfXscxS4-_eA0iZcB9gbYxbtzaUKMreO5bK0a5fzuF5St6-hgMTUc2ft8w5EwEir6JvRuRSS-HlT8yaSOOsJpU_0hM7dPn-9J7vdNZsFkXe2I1eXim5Sn6oMfpL0H5qNLOSKq0Y2mIs94w5u_anIo-_dnctTTsm384MnD5PTaGdNE9TfKKKRzcBySNUvWbklOPWppdJfhF43vjhwlw-5TiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR_JPLglStynFC8a1BoKT6tS368oYthG_Q3INo5S2TtOV6MNWAswECS9kC-7PJuzNvmDJT13ho8zI6ZmseFlCnAx1BFTvUVCf73iYQzE_N1SuDvi7Fa408Eyjqk17N_YQMHR19xqMTKHwd3c4gaY_yqzlLNcHwMycXFBNb9enO_BQ-iSpOfY1-m-W3D2kF_T5WcXQcL69YxeXfaofFP90ooCJYoNRXi50mNaydPXb-zqSKWBszOAyqLXIVfkJ6zaXXsPP__9RwyEFu4lugnVfR_JYfEHNNiw6FOXqUh2rcEM_108A0HbXIX7XWTuhwp9UKVedgZcLJsIVUoTk3OoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK7Txida5Ih1iHTmR6xfDy445qQV3eZNbEchVwVkT3E3uNwYrcMbnPqW7SAXLGD4lh5kWP6nV8A5qkAzz8fmGPm8u_6KqOc-nrahHDFozuKy408EcTsPx6iyu3GJRLnxT-ShwQhO3b5CJhuDB03ZJ7q0sfxEan_BWaAgZ_qwSRFcLsqmudPhPJ72Ga-4UbVsHKmrUaFd22F0eQshUHPiVX8-wIkJ9drLFDMPaIni0krYns6mIVe0EFmTssL71PTpUW-BndRoDvj0EB1mcptuys8u7we_DnsNECFVgVkloLHEcUHNJcAkFmgKPgyGJLGIzAYamLNddV7O7-bhg8xmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=p6Xu9Z-8Z0RpY5hrGjQInK8BWZVy65i6PHkbnam4gq9jhOXogyV8SL1-BDeIgVBjrfMVxSVD12wk9mqkdyC9lIQTtIGNx1X6dsNQpM8j4MPF3ZicZme33YsHavx_Hdd3h0ujuBYH7rWLLillXy7ojQ8F1B1Qr_KhYI7mZk5aBHHNA87K9HW--i7N8V1KJkUGx6zGPP6mK4AVvN5plYa3uNO4frNW1Pr53238q4T8Mj72vTwMjAP-H1VL8rdtRtCI5uq28-YZefaVajhQNba9uCXoLpMXpcmwXGahXORwOA2PDg5w4RqjnSDWmhWRHioMyTfNw_NkWhZ8ZcQmk_4-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=p6Xu9Z-8Z0RpY5hrGjQInK8BWZVy65i6PHkbnam4gq9jhOXogyV8SL1-BDeIgVBjrfMVxSVD12wk9mqkdyC9lIQTtIGNx1X6dsNQpM8j4MPF3ZicZme33YsHavx_Hdd3h0ujuBYH7rWLLillXy7ojQ8F1B1Qr_KhYI7mZk5aBHHNA87K9HW--i7N8V1KJkUGx6zGPP6mK4AVvN5plYa3uNO4frNW1Pr53238q4T8Mj72vTwMjAP-H1VL8rdtRtCI5uq28-YZefaVajhQNba9uCXoLpMXpcmwXGahXORwOA2PDg5w4RqjnSDWmhWRHioMyTfNw_NkWhZ8ZcQmk_4-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNeM5JZ6IdoWrL52yh7xgbw5AnaS3fjqwY0dBIkm64IJtqI5Qqr89qVOP99qrR4KMQZ5EOVthUVnU0Md_JctRrqI9dGYNww2wDKAM--Rnv3Kx_FPEFGy0mjBIFjYa6qr0Owcq6DmJ_vpAn25hKOvrN8hszPz74FRTne0AxlPeHDMzxBOzyUskYcCv4RW53iLJ_Y-ZpU07yudqD6CgjbiRGe30oPBuXHPN0N_t7XSwf9kDl6NraERsLHwqGgaZuds8kFI1PhkF-UzIsZcGls5urHJw2Qf-wZYimtJC6dnVYHHyPkQ_CN6KxTJbk4zpnlPYLMl6wZAxjwYtE-XUOTq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4TnvqsOrfJv8Jt34qESl9fiajZ9yx17MfzSEXucsMDeP-qDPwbihaOn17_Z6cCNzAxE2t11YonJw3v2p0352eg_PnAbzXoCeJJJb8rEeP3GcAagKXRg7W-YF0IIq8-85IwzeXIplT1apzT4MRd7El5szz2n1FiLp6F9e557LVAJJrvYJ4w_B9CKJX9ihJsebs-vJrtb5NzIiHq7DXJMTdQg9IbSOkx0nMg2ngp5goRBXKYHsmASymUIHXSDUHYUuwDt37Hf8wGfzJAmA9TmtNz8scGAYJe1AGT-d2z9d1OzOnvbaPxAcjgCVLympxyIJUS-_aTjrHb0wLsVlx0DNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7N-6CaxbAvHhHXik43tNAQE3i_iHIvol1ki1vUBbMx7-j2mqV0Zm6jj5w_UvK2iEkj46YknugFJ6Tb5u0kQ1-EeAnQLB53-_cLYU6fZp72kYLzbn5318upACQOja67Ki7LNifw77jj1h_se_shr4y4tz3FDuhbMgiNbchj5jrD1rwLJl2MCobuzFP1NDPXCt2m2eSar0YyqpQyDdtcWKAYvXC6EGQmWbQon-KiiMXxZsy1GDyWU_LEDIO7WjdxqrB9HsWyROIWZudyfVrAWodVb-g2T-sb2LfQAb5pdiQ6GAF_UjHs8oxLqvW8OQ_6XciOj-gxM_msRvc_lihU-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=fPBT5T1-2Tj7zkiIzy6WpQpU0rqSyubXzbtla7KEmbc7PwRbUkD1ews9IHDqOZhOW0rk6Cw-EjhIgU9xKm2VwIK1pMrzBmtCnljA6LaVurGhBt9Hzl2iFYa5xY7tFWubNMLtQoRMjmqq9NgPs7Yf6g6ZF7o4vtclpdwXQBnW5PtZd9W5hcwcr97IkwIGyKG3zTzot4esKyUBnm75p-FCAqBudFbt5PdlYL116YkDhVMAb38Dzqu9LzqWTGFDhLhVHq2a9Bbn4if_eQP1B6RDlI1oYybXp_RpL0NE5D4dB3ua4akU7V9Cr9MuQisjJObGiybYzpvrMqS6WII8OyyYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=fPBT5T1-2Tj7zkiIzy6WpQpU0rqSyubXzbtla7KEmbc7PwRbUkD1ews9IHDqOZhOW0rk6Cw-EjhIgU9xKm2VwIK1pMrzBmtCnljA6LaVurGhBt9Hzl2iFYa5xY7tFWubNMLtQoRMjmqq9NgPs7Yf6g6ZF7o4vtclpdwXQBnW5PtZd9W5hcwcr97IkwIGyKG3zTzot4esKyUBnm75p-FCAqBudFbt5PdlYL116YkDhVMAb38Dzqu9LzqWTGFDhLhVHq2a9Bbn4if_eQP1B6RDlI1oYybXp_RpL0NE5D4dB3ua4akU7V9Cr9MuQisjJObGiybYzpvrMqS6WII8OyyYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=hHk9tlWeGmm1dSobDFroabEUEXQ1JKpoDMBXiRNKruvI54uWCgpPqZsWk-ca7mSpi2quuRcFBiIKwKbkLAP1t6kCUEW3_jPBZe_6j91HAfwsWSJdyWb76GbdXopX8TurZmD7cSDoDqpSMCLLPmLo6Z_b-V7ozJMSBwvDcaT2w63DbBYjNZUXvtHgpfMkE3sTcyZ46qDNDquXOF6myPZZN-Er3oTmYm8k9fXG-VngVOO6D4nAriSm5qzgd4UBI22E8zwmRAbAZhixNuPE3DLZ2mtMX_TH1KXSeClVyWQZHcZgeszgr2wP9z_aFuMN1toVyrQvmiq7BFpbE8aqojafug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=hHk9tlWeGmm1dSobDFroabEUEXQ1JKpoDMBXiRNKruvI54uWCgpPqZsWk-ca7mSpi2quuRcFBiIKwKbkLAP1t6kCUEW3_jPBZe_6j91HAfwsWSJdyWb76GbdXopX8TurZmD7cSDoDqpSMCLLPmLo6Z_b-V7ozJMSBwvDcaT2w63DbBYjNZUXvtHgpfMkE3sTcyZ46qDNDquXOF6myPZZN-Er3oTmYm8k9fXG-VngVOO6D4nAriSm5qzgd4UBI22E8zwmRAbAZhixNuPE3DLZ2mtMX_TH1KXSeClVyWQZHcZgeszgr2wP9z_aFuMN1toVyrQvmiq7BFpbE8aqojafug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuRP76iLyxEcVdBQqHWoOnmoop_f7abg_37yCzAVUJMoQfG_cQdevPcSXI5r9kCqViE0nMaT8SxoQDde18yxNCKQko2ITHTNle13PfvJrjw2VhimMTo3N3FSbAexWUvw0wVut5cxDelb3-dRf1k3yYeI7LdmFGqvNQjz-_tuMMMYo2A9P7WeuG_tiX-fvMnZBwVrLBDj_iqYRbzgmrLbN7r7V4J6Iu6PsscVrFJCH78q7WrLwUpYz51GFAlCfi_CEGfPgqqgY8iiQKJoyjCzLZIdZ5vsYBmcCG8cOGyFMwH7zMK1QAjEki2CanmIXajPoodgSqauSUrAsC0X5gCMjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzyPBpfH32hVfdFsaJvI_ma5iNmVpw2TYNjyAhDJShtSvHOe3N9sRSVsT3ARpizYKu1a6IFoWsPdVfOqrI88CkxXevLrw_Tzt1esacvBMO1jwSQSP2XokyOk9ENXbGAeEyoN0AtU60XQ_J9mdZeh8xdERhSuzWcv5Ga_5HPVU7MmK0YWJ3KEQ7ltGlVh99CNgUUtH5f5MODUCE953D9EtCec5h1_Evo5B0iyNJSsBNhy1aacxpEFpeFF1ExCwdZGS9lGMmpPEzJocfaAkM8yI5B8B-98bknZRSPtV8QoEyus899W1cXXO2dOItK2EQDqvq_ys2_hjXVpyEKkreDjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFXdpyvwD4qMJ5xpopKyBkxxlWe_Qrm8C8VT_tY_gyvgVGdp9jg9o8N4qs6Mb39yd2ljg5VRwt2B0ENikUzSeQ64C65ey-kCoVlwmB3nGmNXGg9R62_3LS0I2wuanBguCfE8YSJu80H1HJO8xpIUNlEmY2kk858xU3dZ6A0kInUSYA6zEdDAc9Yk_KPha23KJH-rpdetWDctTS7c9GadUmYKyTGjaF64AF3KYxoNmT8evOgdoT2aeiMIK5MSXgmf3sM_0yX0rdbKimZhB59b7iQJdf3ZRhJjCzisWBiQIqBa60m0S3bqa-M9mtTYRG-11n4H-AVwBONFoLgQYpzCBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
