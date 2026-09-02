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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 23:03:40</div>
<hr>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsto6SnBp_pi60gd21bENs2IPfIOgAbWrPCJxtlRTSApICc1zggjF2Y7MByxAXnkx-u3Ys4YWQDZJEii0f_W4GiD1gIShvgzQqrWwBi_ppkRxeXGbGQQP-jXFv5gWZHppGrmiYpimg2XruhykZrDYNvPAzZVBxd2W0z3nvJ0a-8jnGD8QabSlnP-HtHnCAO_pT6EvWbCFCvh-3NqcoPUSOa7jIXbGe1oKXInunZLwy8XLj4giZKn8hlNaYB19MARHMygRn0Dwwxf8xXBucL7kyGhFuNHgRvp4ATh-7zPqXJJAuRhPhWIT3UiKMHVTkzY3h6ZSh-4AO2LFZl74ZP4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKpL8XcNjuSGgDo9_lu6V_4QskFWeO2xeOjdfxmlZ7AvsUIYfYrgIZn5EgiQSrnX-61crc0DH1W_2EpWnADkqjPatHdfTd0ilv6y7g0V4oLVrbZL5sGG5mQoLEqemhHTDOZtv5M8wvMcfFcLQdpBiY0DV0rxADtujt21oWItnQ21XV_53G1GoIfX_bKnzgNccChoj9-hriznKywmzdD2egGMoBAVAoyKV9jcI4um6iiBPjtp6C2Cxl6wK-smoeRQkEUANIUnTFKTcqPYqZirQK4ABXyAttHrhfJBO22h3z162Bg3yYaFOzqYaIDUYT7vhXl24TR1MX6mnLrv1ivvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmFcd86Chy_8xZWRI5DRyh1zFweCHRGeOVbAUrSflhmcVyZY86Gm8wtHam4CtEB6wjn40qPM6kzBrAngRlSFpgre1NfdFT90_UgAlAagNfQWxJ8IaQixcg3pCpxO5mCDyPKS79IXoPbaJVr_D0jJmUvayGC2FsHeKOoZy9a6XvoWYz_2PGh3MYbLcbQCKDKEXJiAo3PUOhE5jctFpgPqjDN46WgaaM5CQtzHCREGFjWP20SlO4lvy-bPSW6URFW4hIE4H5OL-OUEzghes6_nxfux1NHxfZvx8vXNnguMPwJe8N1oFKeDAnvtjjp5fzGL2Yuf_SCWtVz3WcQ7q-qqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M714M__idmOrh_9nZEqGJAciep9lVpqMRQzvBcmPqKirNQ16egO-sTpSKjpOV0T-8Jf35x6qmix0IKmnjNSUo2MtZ06SHLyXh4pqkFUanPs4zNKMacLlRUYrc86GIDe_jKpLdcfYRV1gAiObCHMWIoNVU2L9THTBpLipP8rKh-9g-haKTROJbsrQ0Y7Cv3qFlkRwUVXJyjuqmTln1P0GA8fC3NbHahi28d4WZE72FBfRLRIwlAOQfVhhietGAlrFMHv18kL3DOMRo2eydN_Yj0wT2rEAwJtmTJ9CcVLBhHtphDOELRDwQwDeoIAzE1NG18JsHIpngIs5fgcJ7dNNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o_CCrVqo6cR61bj7M73zL46GySBdFMgvAtKEFSEkEe57BgR53iZHP0shi1f6gc488vpJuBcEuNo_9M8bu-ft6TEfI7csGtnHpVdKZ-IslxXoolzf7aKiGJrgafDPE080Bu0M_X16u7AY0GoHxlUcjyspbE9mVqMqLka1bw2yacI4Xufq4V1TVgLh5_Zx03zxqUSFIF2gCBSXNJP0tHB2SP5tQbMrDE76gNpKzSr0qmbkRDmBZVaTXA4iAf4PzxWSmQrjT6PBPdBqNk-wgExaCivpUgzheVle6ghlkrctWc9KmSUzjWb7YUkQv5L-BFQsql1V5tpx31KzztnVX8YMgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=o_CCrVqo6cR61bj7M73zL46GySBdFMgvAtKEFSEkEe57BgR53iZHP0shi1f6gc488vpJuBcEuNo_9M8bu-ft6TEfI7csGtnHpVdKZ-IslxXoolzf7aKiGJrgafDPE080Bu0M_X16u7AY0GoHxlUcjyspbE9mVqMqLka1bw2yacI4Xufq4V1TVgLh5_Zx03zxqUSFIF2gCBSXNJP0tHB2SP5tQbMrDE76gNpKzSr0qmbkRDmBZVaTXA4iAf4PzxWSmQrjT6PBPdBqNk-wgExaCivpUgzheVle6ghlkrctWc9KmSUzjWb7YUkQv5L-BFQsql1V5tpx31KzztnVX8YMgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMbTrJ1cxkKVtaWF1vAleUk00ZtLvk0Z9lLdesjnDJNCaO8OEkLzA2ZWybbgjgwQk02CFHooTqVVWsNewvci4b6GP0GfnFI8hYU6j_R9auI8oORe7-RZHcgGdaQcUhnEk-jHoH7w71CVjkCNOFQEWUmek5mnqykoiqD96Sl-JQ4UglR1p8CbX9CvhqY2_uOWrSiPCiV6g31M_-iOCwnWghCVFIbYDBYC9y3DIxDDwiXZE5oh1C1pDUspLmZCQiEFSSmiDRDOAWT-po5fcuqFGJn3sTqhZq7f-TZethkPVi7BoRS_zmpFeSetnHN5kla9o3OGQaWtTy0JqHuKUue6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmDjRaWue63TouEG_h3VRkHeRToos_ao4DABkBaHU9JON3q8lT3ozcHWijzjJJ3l4Z5NtpAMFL0dwSJiEZvuZfbmd1KHHhiHQ-8Vb7KaOk--XbalXM09Mq7JMtb8TiC23kNoIyXodbqNmr2U-kd4L_NVlzQ3tOM4Y_yzfZgzSJtLpWk4e2xB2YapC4BXHwiV_pgEa7ns0jDWfXiWaf4SR_0ksO9r5O6bJJ-aOGv4mjBwjgVYQfWR4e_bpnJuFAGhtfzrDGsDQTTpc6J5cxArb4D0-C7oZT0UMeEWPgTCpzZNGlJqCTcDSHJz3Y-34lFMuGsAf9U8ffip5tthHPWPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QLn6_Ht8IVjvvydoi7XDItHkATyjvXOsAZsDlebgN2qB3OD7r3oma9nEHwvIMYV3EEtDETfNSVaP-xMNI4SAOxIoDccoEZdaQiSVbv8VWVFKb8LQ3PX2pHetKhV6GIWOQSQM7y-tAnLz7ovchFLVxkdZslr_PFCjRaKECtAP0Ubt-OOD6N9fFevI2biGEne1hpA15Uhq7dW71QKyTyAHWWl2w3UzrR1RnYrOAtZPiHGQTlvdfC5u2e0q7PZPYh-WmJ18N4sQVW6csDIfTT9QBAq8pwMa6fQ5bqwDzyGPMOwY9V9-7k9g72UlKhoG9CVNK6LTg9pOLzl45UDoGIk6UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QLn6_Ht8IVjvvydoi7XDItHkATyjvXOsAZsDlebgN2qB3OD7r3oma9nEHwvIMYV3EEtDETfNSVaP-xMNI4SAOxIoDccoEZdaQiSVbv8VWVFKb8LQ3PX2pHetKhV6GIWOQSQM7y-tAnLz7ovchFLVxkdZslr_PFCjRaKECtAP0Ubt-OOD6N9fFevI2biGEne1hpA15Uhq7dW71QKyTyAHWWl2w3UzrR1RnYrOAtZPiHGQTlvdfC5u2e0q7PZPYh-WmJ18N4sQVW6csDIfTT9QBAq8pwMa6fQ5bqwDzyGPMOwY9V9-7k9g72UlKhoG9CVNK6LTg9pOLzl45UDoGIk6UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=R5o6oE1I6fjfKY9IJkRCFRM3gmLnmJ7zvwRaqmXAOGCldt-P-9AE4EZ6W59p56UFzoBaGEux3P3mDyK2uCv7O2tMJtIRvZJE0iEX-v6lf_O7GhJNLa1Mq8bZtVRVa8siYWkYz4EncZatpPn6YOeNk7ot3y2ss0qmSh-xPo09tZGs2sBYloMa2QuMHfMjUv3BmrVkHnMO1mU0X9a41ub3WqJ6-9zOG9RgbQ5y-1mT3xTigHfnAIH7ueA8LZjYUsSu4uL96TW-1q1UHzBN7JCp353UUuvvysMslCjfK_MYCA6fzD943C8l2mGhUgO00fK465uTzdDRLobIDsaIoK_VnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=R5o6oE1I6fjfKY9IJkRCFRM3gmLnmJ7zvwRaqmXAOGCldt-P-9AE4EZ6W59p56UFzoBaGEux3P3mDyK2uCv7O2tMJtIRvZJE0iEX-v6lf_O7GhJNLa1Mq8bZtVRVa8siYWkYz4EncZatpPn6YOeNk7ot3y2ss0qmSh-xPo09tZGs2sBYloMa2QuMHfMjUv3BmrVkHnMO1mU0X9a41ub3WqJ6-9zOG9RgbQ5y-1mT3xTigHfnAIH7ueA8LZjYUsSu4uL96TW-1q1UHzBN7JCp353UUuvvysMslCjfK_MYCA6fzD943C8l2mGhUgO00fK465uTzdDRLobIDsaIoK_VnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gkk9svfU8VhvMprsYfNHUu3eNjuZ784aRnEOIns7i6Yt0B2gQzShUtO--PwO9iUZGlytoCwsKZvI1WTGzvUwPABMFqY4RUTrXGJDnxNGMs7gOf9ASu75cvWTQJ9OYITbaPKi99O4WA25myZPKQSjJF-yfSoD01tnCHs6iZ9m9PPR92x_70Jic86aY1gIpjOfUBWT_I-gLMkpBbbkC3ibximRceORgyjziSZMiwatJFAhe2GMZ4J9Y5IMAr8Rix5Rd7AKBmEEsR1_Ehm_XZJAtF8StcIwaBjAvhWhxKzI6RoXCLn93mFVKz7tzK8F-qGZ5tGy3i4Sjqsory5lVCaTow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azk7kjbX-yT8hksaPKomzhWQ63EH0VF8uyn_MvZjBIXt8aT7Rt_5pSpoP89uJrfVdH7XiZQIwV9Qqej6QLsmkTVIlmiw16NDTEFX0ZWvo-fROv50A4X73BYYZbii3Yl0aruQty5wpRwpDL5hyacHAtjp4D1-_t4-fLLaDxi3aBCJxxWMvG6HMLqxi7kfweiXr8-iwyLA3Tmlc9XYcgQF-MN-TSNmHou9swlt_fkXtcLWj0uoAkya2Tzbskxr_F2WDGG8Kr5-PUr3PKVKS8XRH5vCJOQt8e9s2ZWIM5GlO818ls1MUL5GSkkkS4UUjoMurDz0DGtN3jWH21M_9TYR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgL0HbbGupAFE8tA69wd5HwNSbicBXI_q2MHnfoC9UJXykzxoIwAgLrP1-6pZC3Xiw3fg8a-4_jeoAIQ4WL77sELiBv2iiBMDbWqoEdAeZBnbf4p3lknhIxI2bPxQOOqP9A8YvYU28McDj62wWXFkFFIv-Tj-v7N53x7rmLqiwi01e2U4Jz8mDO4gWnYxjgUCfX2IGsVDacthR8nBRJs7hduTuSjguAtUacyAfzmIndvz2kkN_9n8a89KiCwRWzVSlrtETy8V452x5lfkkhVZWwcKDlY1YU_-0QONU8Rm7lL_rUrNx-jzyT_ONWCEjGiMrB2cQittPWcEHhbgdMhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7Faovmqt76G1J3IRduB062FcxCWNIEa65GluznYndjPNuK-oe3TdENgffzM6HhLX3g1jUMBpy-DEtW3mBwZp2vbTyd9m4_hqRV2_bYrha55GqfUYcpxwGdhU5uoxb9xTDpyA2pz60aRPTEwrYgopRm8jsQ4rnbZ_ZUK4nVr4v38S3aH74ccmk4HG50S7X2uasf4GFUhbcGpeav-A__b_gDIQ8kCa4s6-uLpBvgpsniX1AanQoKu5aLqnARTdhuJoCeY1fY01BAHtyA5rlLhh9KW_qJYsbBjJraS8sc5yDO2eSHmpi_yu5q_2m_z5YgFzg7xCdjzgka9VejVgi9KXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilPzZLPc9gjP01BN8mqq8gFZX45UkY95ysDhp_ZK6I8xxplkOnP6oQ1p_xqtaZ7lUMPEKiWHsn5w3cP7FrPEyuXMyz-HsdCjdyR-hu9zeLI40ECKlI1btmTV_ikpwqtPXDKNjCqqOvZux8jpkr978FqSCAxUCkEXOxW_rIW2d16s1yBIoDmU83xrqVgIxarIpylWdNpEGX7OZ8tvYOu0zwBmpD-pZz9oHmAilxSlKS0LbJr6y7mLi727X5uCx9QIIGLRjNRIdERHSvX4bXyEMa2POVXT-7MUK_dipHqgYht8_gsSwoq7RuG-_TJL7zV1m7J4WryVUO_tvHOPjU7N8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApQTh_EHrgKLyZk0a6Mqchq5ZD1SthHQugUmrQgwqQC9ysVb54mbiWFRMwmyMMVP8wBrY35WEVJi2Fd0Qa-2AR1MdoQcyisXdlpNZuk9iqpCwTzZPFd85TgFsMFef0ED35t30bF0LiPluiIFRxETck65U0fVH6GAdCRoFt0uYG211-Z_DorZ1lHDi3MpOrEiKsxCTLFeheZHyVhzMVdV9x51dwHVFKjBI1UQdGDcT8DXjtnVD5SM357tu_mmg1Uj_jJIx_inYpAnwA_3zAd9u3J3hPIx2d3WS3Nf_WqfXhqUzMOvpAf5U6W9HNeGdYzyOS7Zau3Xtp51v3r7SloKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpzu4skttb2oL0lwdTDd5D3h0PCpBLOPLLOA45W6enjWvOxnfQENP5i-8M8tZcmiHFMaWMfupcXwOH7XcWpD5YKsLyN50w0foV3xGWAYb1chaOX2brrXjhNXWuLjFsTnR6NbTY-GmH_cO0v0leVfYVCUXVNcAf_d27khZ1sM7Xmtvoj1s3eJAyhhJ_pXpYVOGnTRPLeJZM_XUpKYOc9rv0mRx0g3AlEu7NqyO8t7iGepWFJVcPSQNt4pHSKS-oLfokARLMr-nor51hPJSfoH-eVdvRe1g06tBmw4hEQm5l1OzfP3t1rHKZCkSiSkFEBkhLu5ywFbPk7QctW7wuTmXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfEp9sfFtBNOcJVADTPfMQOkjms7AZ0qH5Zy3X2hX74w_AU0k_mNoOJ74vAmmajuCDJkTH-90ayVSET-c65PDPkX0qt4ocH7m_G2i93VDax3YK4DqG_td-80wz3e1f3iU6HdnZ9R_QtZekRpPrFVAqMKWuvVQDml7I9Wx5MNSxuqUyiD991JrQjtg0WZAzEnJLidqcfegqqS82d32V66odFqpYxXFUz_-Julyi2n4grcqprrtQBVVFKXTXxtviHlxT4l6f6uK9VnR5BGVrf-JlfqilnMd3sPmBo6FzktlymWaRJ-Cr_zgjYtbXs1lSYQc3jmuxV7L8P4Nr6juB7-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=aL8ivfELFVSwGtMKpMurkErCwjRQX-JK1w_dpPDQvhgw8IX7rDSYCml_Qa-6lfbwLkZheP10czlic8_XJ0qtj4Ng0y4dVN3m9C3yYwc9-RFkiGmGhllr49VXcGWLgvIfuHsrQhL6C5wT4FjNK7kZ1lCcnrLVFjVWG8aQqRrOCYTtJ7uUuVZmflvLrwqRpYGTQfIe4C_naby9j0E1IS7U_IjmTkkDo98Vg4AP4OeI2ib0EeWFOsId6N0x42i6ZSRIMoxW0MyEizEX9-hYvaSvALr5vm8LJOHwqP_uNUyjPWYWhrQKd7VPsoZebSoc149etyHgv_t0ObW1Fen8wllDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=aL8ivfELFVSwGtMKpMurkErCwjRQX-JK1w_dpPDQvhgw8IX7rDSYCml_Qa-6lfbwLkZheP10czlic8_XJ0qtj4Ng0y4dVN3m9C3yYwc9-RFkiGmGhllr49VXcGWLgvIfuHsrQhL6C5wT4FjNK7kZ1lCcnrLVFjVWG8aQqRrOCYTtJ7uUuVZmflvLrwqRpYGTQfIe4C_naby9j0E1IS7U_IjmTkkDo98Vg4AP4OeI2ib0EeWFOsId6N0x42i6ZSRIMoxW0MyEizEX9-hYvaSvALr5vm8LJOHwqP_uNUyjPWYWhrQKd7VPsoZebSoc149etyHgv_t0ObW1Fen8wllDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIsqu9BQDv4MH_B0xDnySaHC3kOzopNACARKdrSaKECvtpoB4nSvRXvKB0liV9x-gWBtEi9I5pObiKcT_FNzuSlgqmlUsBB1UqBW97rRwKKX-hvgvutIvX1_wnipz9UWq41D7oZrGcAWCDvZz3nvL02f8MIuQsZTekGdFAZX1xx4R8VhMBTbaX05_xeBwjRECBrqtQb80c3-aZiUud4oV4Qol2ObO7cEGIqC1gkU7W_A9QNlWctZ6axDlcTYqsDKBWaLZE1UlfAueCvrULdCMqZWj5z1KZXTi8Wt1omaQgI6t7qnUjocCJuUahdKKq2hUdiLza-fz4FkeYkQZVQ_mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=mQais-mjqWnaqzpFxzV02kIOTdq-eFXxmGOLmLzRMGmC-li-Us8P3q19cPOYOc1wK7GyWMM5xci1p1lGT7jpYq6VapuQLSuQrou0CIanhG6gnLZfX4Aq__sZLLRjkHuXDV95seYILZCxR60_GIBUD-vWXXzfy4olfCybLch8trlcDpONka46QfyLLz9-HhY8oXELSy80SYXqzP9Pg6nJYBhxCzIZ1qrelGc1C4jXYpQQV7aO6FtqJjdUuw9LibhEBNdSSRIK8y69PpYyHGSBFtx8_lbKR4S_gWd8lYWsbQk9-8gYX8IkptrjqQuThbdc7j-2-_5wZJN_Ef002-QF8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=mQais-mjqWnaqzpFxzV02kIOTdq-eFXxmGOLmLzRMGmC-li-Us8P3q19cPOYOc1wK7GyWMM5xci1p1lGT7jpYq6VapuQLSuQrou0CIanhG6gnLZfX4Aq__sZLLRjkHuXDV95seYILZCxR60_GIBUD-vWXXzfy4olfCybLch8trlcDpONka46QfyLLz9-HhY8oXELSy80SYXqzP9Pg6nJYBhxCzIZ1qrelGc1C4jXYpQQV7aO6FtqJjdUuw9LibhEBNdSSRIK8y69PpYyHGSBFtx8_lbKR4S_gWd8lYWsbQk9-8gYX8IkptrjqQuThbdc7j-2-_5wZJN_Ef002-QF8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=ESyYJCT9qii-_ssu9pzpDHc7-w9f1v0yT_kYErrbzOcEOjfpWm9GJKpxBu88wzh0D4T52nF6-xSy2N-bgkFbrGk8DaJbdqsdeXKBNyGV8e298UfPEZpGkquwTKSeyCPqgSWtxJKiVlxrVgRb6EatbclBpAa96LyQAWWWlsO9taiJn_ZS1qAbA02XUMJSFQXdUN02ZoEXds2H_0IkqIoT8xaQSFY8DwBFAz0s8FaZ2tbr3yZEhvodIVnRSDNdJv9Y5trVlwyzxfZ0Jbyfg7KQVi2AfH0jc3gqFz_A7oNsSbPfUOVEdGgtO1CQcw5DWK745Ao2KSrzclgAPmno4k6PVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=ESyYJCT9qii-_ssu9pzpDHc7-w9f1v0yT_kYErrbzOcEOjfpWm9GJKpxBu88wzh0D4T52nF6-xSy2N-bgkFbrGk8DaJbdqsdeXKBNyGV8e298UfPEZpGkquwTKSeyCPqgSWtxJKiVlxrVgRb6EatbclBpAa96LyQAWWWlsO9taiJn_ZS1qAbA02XUMJSFQXdUN02ZoEXds2H_0IkqIoT8xaQSFY8DwBFAz0s8FaZ2tbr3yZEhvodIVnRSDNdJv9Y5trVlwyzxfZ0Jbyfg7KQVi2AfH0jc3gqFz_A7oNsSbPfUOVEdGgtO1CQcw5DWK745Ao2KSrzclgAPmno4k6PVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vf_N4fZudSaa7BYhh5XA8KZfrey0NGBplB7TIXBGrHpbZYPCs47Mec3xuWOsIUovwDDdQIBrKFYW8OCZl7EUmrR0Ryj9XfsemOg5MCjTlXrPzZyavL0UL_E2PnCDoXv5LnhsjlxagABLZhFExn7g1bBCK441AURRWurl7RKxO63epRw3VAf1KL0rfURkze3gAjTCOJjc1Xm6R-ouLFL4mss72iibznp6cNnkTVakS6Z4QcxLSZwlMFWHTezMdm4gZ6vbFp-XzGX2Qwbt4340uqh-McbJGa7Hfia6GSMwIXrKeaazqx9b9plbl4B9r27Y_2TO5tQNNk_Os0cUIS9-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MavCqt9riCVY16CIi9jaNVpdbHKqvIPllsL5BiNT29-cnUF24WX4yxH5UXcl6uEeaUFeyfK-1YLKooRXkeSiaf55xzqlqBio1cKblhadbEZWMOEo1mpVN91ncFOmywBMPbq1b9VNHMIkAwhaK9uR5mYqXl95k3qBeKeio2i28BhswbMx4GsdshgzoIzYrZWncUw5PVrMkG4qHYLQNWwlOTt3HThKCsKJvzLnkZohEB0c3RPOYpTf8h-fMTPbVVKmmJsZtuu66K31yFmqi9WRq7rOvU38G6bR6y9Mpsx6U6PtOGzT6WADwaxAQF2vD763woojLPfkgz79wWBIijfP8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=tAyATVRWgcXqhBLcwCOjNk_x3C_RFgIVhMlV2A7Yk0hXXt3LX2yLMkWiNjaqgV4strLtWWBPxADBx2N88Vvl1R0yuHsWxLt1M0hn8m0ekbJsunL7tqB6jAzbrocAJHqYG73TTl3Mfte-Y6zvPTl95vBwOsH1AiEEwyKsLuXYITHQBCpUNwlVmp6VmTT-5yImpL1jJ_aBP_ST4FCBuSEnw_ZZzgDmXrmKYQD9_EgucH_XWs3noIugP3gj-jBUZ3GAfYUzTLYmLrqB9bTqN39DSwLFWb7bu0njZohVJJ6VDknZy1BIfYbWFM6fXLxX1a4Bo9IX8uTxMbFyCzvIUMBJI6eVXyzUkIUn7rS1hLJc10RuZQ4dlOgG0fToD9q61vGF_uA15NK0GMfiSzSjcaUzKCPwE6IOQLeDmKdVzYdg6dMtwW-ftwfY2eqKCWVLBDjloms3tPm1J70ImvfpvAnuWJ9ArVwaBQE1fG_Q3dnKpYxG2ay5X4PeM5Xhd76cW78roeytgAN0Q40SxZ3U9vuFMm_6AgKwJyy6jW7vWaDwr00oh0BBGIgKuom8WnxkbP25qZLRDJpJ4JSP19vkHhYEWQWPuw7u56FyS8sCcIH-1oYimjk5t8ZrWTf0039hIbfM6col8rXd2C39ILEMeW_n9SKLAnjceXYHhCLu8cfqAQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=tAyATVRWgcXqhBLcwCOjNk_x3C_RFgIVhMlV2A7Yk0hXXt3LX2yLMkWiNjaqgV4strLtWWBPxADBx2N88Vvl1R0yuHsWxLt1M0hn8m0ekbJsunL7tqB6jAzbrocAJHqYG73TTl3Mfte-Y6zvPTl95vBwOsH1AiEEwyKsLuXYITHQBCpUNwlVmp6VmTT-5yImpL1jJ_aBP_ST4FCBuSEnw_ZZzgDmXrmKYQD9_EgucH_XWs3noIugP3gj-jBUZ3GAfYUzTLYmLrqB9bTqN39DSwLFWb7bu0njZohVJJ6VDknZy1BIfYbWFM6fXLxX1a4Bo9IX8uTxMbFyCzvIUMBJI6eVXyzUkIUn7rS1hLJc10RuZQ4dlOgG0fToD9q61vGF_uA15NK0GMfiSzSjcaUzKCPwE6IOQLeDmKdVzYdg6dMtwW-ftwfY2eqKCWVLBDjloms3tPm1J70ImvfpvAnuWJ9ArVwaBQE1fG_Q3dnKpYxG2ay5X4PeM5Xhd76cW78roeytgAN0Q40SxZ3U9vuFMm_6AgKwJyy6jW7vWaDwr00oh0BBGIgKuom8WnxkbP25qZLRDJpJ4JSP19vkHhYEWQWPuw7u56FyS8sCcIH-1oYimjk5t8ZrWTf0039hIbfM6col8rXd2C39ILEMeW_n9SKLAnjceXYHhCLu8cfqAQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuPmUGOJ59Zl-vJZ7RecYI8-wNV0qYYqCVxSa2oqvG7xAz0mGGBAT2oUupugSoC7H1GL_fdP303otyCVgRHLW0xKGEwuaXOXJRUIGwYO3yTSRLOJVWdLJbkzGYIrD2BnQHK_c-0YTLtYV-sOUfVpJHVGdChT2DCnJnqbJGAdpZHMfBI8Ri4SlDInWuIy8D05BwoLIvH9gKkGyBjlyDRiYsJ_D51cno2NI60vJR95Keg8QfACtRLqH8YllLoznD8uE2W11HyJBaGTrEyWffqkrBbJVqACt9iZCgghP_5YeB0hSI4RrUvpFQ1P658jCLSnBnNUU8kubJ-ysPpAGwhM1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=KYYOoliltJusfeeKWODgpHLwurQ_PB9l6fVSKOiVyqbOyAWX8NTf1MC8e2S9ZAdaq8oDLkGSh0JmlUGtCqqHce_RzzFPQM4Sa28s5ZU6A0j2Tfb_WvoBVErH7J0HXFzHixT3k_WSe4ZOEpLq_wu86plEQaicNeAYzKFAlGXMTSszBx3TmI0YeHHancx_YeexsRYK56TGgRs1v5GShLWEeBVbqu-YzDow1fYxTbe6rFCQcROK5DOxU8EzErq3ZP3dDmwFCE3xjzLlQ7uGMqP-MJIsIPV-rWMVrg-aJABz0kQSFvKwqayzFLUbsRqiDm3O_XU3K8Bx_X9uK-u-ZKWvAmlVKT24OS_8IiSckBgWCVmKL0eXy5_o64qPeHZM0sARE4CmzeWd2KOxipyWQ7KucmUpIPFJaaH24BW_GYfYOnbAP8tB9d3TAMYP7e27oHhKR2nzhAKWljbx0TLUe5Blr4nB3xvoOTRLUowwntP7tlZ24CACLeQSxIMPFL9DRcrMM7Za1O2fOV6va0XMQqtxF5lELBSR-zpuoRVhU6MbRiWyOzZlcgHni_HONraVxCp1DQWUF1VLFjKzA-beKETbvwJH2DXs6TYjhFV69fR-OmiiBvHaR9N-8D9WLD8Qb_v22XA3nPgRnnYd-0TpEk3KYCZ6WkIVLxSkR_9PXxxj_Bk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=KYYOoliltJusfeeKWODgpHLwurQ_PB9l6fVSKOiVyqbOyAWX8NTf1MC8e2S9ZAdaq8oDLkGSh0JmlUGtCqqHce_RzzFPQM4Sa28s5ZU6A0j2Tfb_WvoBVErH7J0HXFzHixT3k_WSe4ZOEpLq_wu86plEQaicNeAYzKFAlGXMTSszBx3TmI0YeHHancx_YeexsRYK56TGgRs1v5GShLWEeBVbqu-YzDow1fYxTbe6rFCQcROK5DOxU8EzErq3ZP3dDmwFCE3xjzLlQ7uGMqP-MJIsIPV-rWMVrg-aJABz0kQSFvKwqayzFLUbsRqiDm3O_XU3K8Bx_X9uK-u-ZKWvAmlVKT24OS_8IiSckBgWCVmKL0eXy5_o64qPeHZM0sARE4CmzeWd2KOxipyWQ7KucmUpIPFJaaH24BW_GYfYOnbAP8tB9d3TAMYP7e27oHhKR2nzhAKWljbx0TLUe5Blr4nB3xvoOTRLUowwntP7tlZ24CACLeQSxIMPFL9DRcrMM7Za1O2fOV6va0XMQqtxF5lELBSR-zpuoRVhU6MbRiWyOzZlcgHni_HONraVxCp1DQWUF1VLFjKzA-beKETbvwJH2DXs6TYjhFV69fR-OmiiBvHaR9N-8D9WLD8Qb_v22XA3nPgRnnYd-0TpEk3KYCZ6WkIVLxSkR_9PXxxj_Bk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea-Dt1lPQaxLGBILzB8V1VXDqgr9GTa9f34BGBtKIDiLdesHnv1S11Ji44LRRRVM6nLRPH8Lsmfd7mY2rPlICkkjXNsCVaDfe7lHuYyEKSRjbxnZmiODHXQJW5gUmCm1Qr-U9Y8XuRfdgbWskPpDZsxnfr-MGYeWInNJvXdITeMEZXYYjGMZDxMcL7MmF5_Vc0LHuAzyvmMK-eSg6Y_pss2vzS-n9Q8SsMVTaVjTIJSpwtQ1XH9gCdEUZ7JppjMkT1TfsERuuUlS5M7jJgKFECNm4Tcj4nJobNQKZ-Dibs8dyyV-iGLXvIYtvUFOSJYm3T26UQS_ueEpTURFtuxPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERsKJKUK1Fu9PJkr53QayKK76ACS177RVPbeoMQahcL2-GeDSj5oNRm9Bx8nF-6NG7pCxY5pi6YVi-uDCabOf2TxObETIWLqI8JYg4EYKxwd5G0-fpBsFjjolVqdelvEfkCpvR1uisCH7FU7h9xQF2OF4c0LgBh_z4h3HPSf0w6SwO7_Gw2BPQAO5Xch4yEIrO7AxwWAEVqxlh3kc7ifVmEFzUXp9Fc9e7dwdTBFclYwRkcOEKpOsEpWqqEwDJUsjILvdFTCr1lGccyh2MuC74YMYtYM_J5fSdRHXMp7CGlrnD0Er6AFl90GWCb7mFw3js1ZyBkdaXfPlRksmqZfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpWaO-yDBHTbcLMQpTlSxi4tlyB_Zjfxp6-Arn27TNDxdSFu0iTm6Wids0IVbT0b8XO6jf2I4EsNoJBP9SOil4xGxiPVcHtud1zVC5yqNeoAnOAO6bcVbM-vj0IjnfMwZdRtGp2kAK3fK1rEvI3Xgg8ZLcwEVxeNl5HcjtQ98GoV5vpJLafDSCklEgpVj3zGzTT2RPddzI4k-cS9f2lUw9h0prBkbnm1bqUdfGJYrlms4EDGky3NZppR81r_qchOKiXwxps78PL1WECchHiHWIGJP2tm4Us2MBKOj-WqRQLP9kC4rZ0IPFpc0MLFcLWYfdGtZvt80lNdttKhQ8Y3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dph9MUqkdr8gwxTm-rrZa2tjSTKDBmEqgEFE001-w6YItYpNCT5h8BhX9S5FuN_mEX1bynkqUNuLFJkpNRk68BOauUFyT244w0kRBnilaR_yFGRH0gn-TRQDIb6jIpkujr8z_JpQYKXLaZd5sLUBpLY8_pCY43gTxbYjb2BH0NyllvuSoJc1w9ZSr6rueHC5N-ryKDuIAdmCJJMRynvJMIf8PJEodIkjeyTM3fT0PhzSQzkV-ia8jZJCLdsHbz3LFTG4vzfmIbNuiKXQybalFeT3kZ76sGeqZERqsM-k0Ybvcey5n3IkbL61DnTdl4ptADXgn4JfU0Anq_NgwtJ2nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXT9PyrnkpSXB2hHsUYT7shqizWMIqDpr-qVckGQ9whN4DY7AgJxjTL787NDcUdpXWs_PSj1k2vTY-KfF_cOMAVOdBWetdYv0auwdMGz8yB0fmkWZzTvHJtASgyhaia4KFk0E2DxajMvnCzDgJdvxE0wiQs8ha-Ij16xyDVw-9jt_Swu4-MYgmhB4hpCKG_nbTdDtjROwldupAyeTsDVfdH8g9IAqXX2eb3ebaDlkxbMH0Q8L_a-G_OV1W2UqVA9D_583buZ7Gjv-n4oMjC8-N7K1HbFroRVF6BDRiszMgAkxUrgOGYtcB76VeknFC9L0Q8qWIJ7a94uvXtLs1CpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbmJE5p6zpzuz06qCdqVqEDoV_ghfgliXUUzddz0GW6xak6II6Sn6uYbS_Gt7s7neSTV1OSZ-H0GYYOhEYOQeDrS4Ao2yKjnFOCRagU_ZFLwpuQq6dp2f3hWhw0ZtY1o87bFy7oPqNdNj0Z4gf8b3wvuzGnOEy5WLJvNwvCmLOUTITCkz5o2kbxYVFDoV_e_uXIcJyLV0jXQMe_wobBE1JZPxSa_VO_2tPhlgkgUdjpGQEPRdV4rg9xWaDONZvZSa0Br8OHYjFJnDVbBcR-Kf3Ertcm_MsX24BeiTVl2ShEqkP3cW9B50eulp7ZU75sLyoTHAxmwDl38zJEAOJ2xKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLbJPDtsB7pUIVuVkXyA_vTcswOsn_pReMGxnQRNe6rE3Yu47pBsi6iv7SPPCpGhQNoZPxKhJ8R0ls9s0SIusMSM0v9NvecuQGJzszzHBBjvDIJtg3DjqwwnivQZ0y6N0F7rctnCyMGH_QyzaJpCV_OVtW_j1A1HxfdNYup1WuuHwmh1etSXakWGGAdUvwAxmNO8tl84y4cJn8r9BJ4XsK_8MzhTqnSjDFg4IlCNpBPKKR624IkCKsgvfrtraQtNiu5svJ68hB7riR4luak4Gvzoo9QuwdiwDwzcgqpNz-ji2_vVxd2ahaxjk9d-LrFA5KhWvQiTEoxnBR9ogKZD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huaNgS82CAHCosEQoF9n0AwSN8p1i7emwCFmVqb2vnGurNoYh-PDYn_3ATGDCu0tGbkOt06Tld1YpCDLyG7HaZCg1zuHHVb6EsXOuwK_3FdHv2oALI8dZP_wO4zb__n0-nvFHxeiqMEhLj9cLci0gv7ruk15K3UclIloUUJ-U7gGsMnhtD8K8knuonBrKD3xJ9PzxNsxNvuGkz15jvkHt7MJMkIiZbjgoocYTEdJyDNuKP11aUqz6ndzjeVkoeaiQF26NLB1cNKwgBzwGU1BZWbmR64ALJrCz3sv_fzSHoFINroOMAatUhFVhnxyOxKNHt1l4wHpoL5T--ii4YH3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FluBiAV_JdxRebdI7FNvHDYXU5v3lLMIS-fcNIMp9_4j7NbQSea0jHp5Tjc7zIyv70SGibXlw_EQiB69JqqfDFR-d6laYDI5XUC3_fGNbcIn9vC0laxzZn_A5wSowg0G-eXPV-u5uE_LpXDUFXobfyD3VifYW9PJ_DZnrnf5kHoTxqM1lGW0FJH2-paj_o1zbrBsqn1Ra8e5oRhJ6E_99x2WADydkeW3aBlIEoDQ2yQks9BP6oP18IfOWHuZzMxUVfOP3Z8tmVw2fbw5AZittFgBA7eKFWkS0VVHU9QXA4E2OQsIjzCAV7HboCPuUvWQ_kx0tyVp2UcvwHYv-GeHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3nILc6faXcBNcaLFC18i1AiuNK8A7ffZcRk0G6DZaq5WTIeSRqB8KrQp5_7_WEVGXW8XxyNoDXqF-9t9u90hDboYP_OJg3-E5DWBi59RBdo2WT7mn5h1aQA1mxacT1HhmPKfDZDbLSSTRibQE7t1zixpupd73jET-xBo5FKKTMRc2HHgMv4bOj4Xnv8GY4KpAIXCxtE_8KV64CwmlcNed8Y84X_GAH5aInYW2xQz3xr-vK4ZCYf4sZ3wFyo66lPRs6AhCkcZmH2IIholS3m2qpscJAJ7YXU2LBOdqWPF9E07bZfQEr3PJnSwIxQi0r0uiWAk_4GO-A2zxhV4K6wGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmTAJVSyO2nwqWtQm-goxM1NHSFV2ij57uO8NbhdHddqZnUWrQwG42Tv7dnuU76ODL2G9zGm9x9Qiwj3k613BoCHsebFTiqUEJSslw3T0t_fp_X55tyMi_X1UtbGfdtDt4E24T6I5xDSxmdDYzuLiFmCWmgf9M3OC5i-telYgM7hls_JC5W4l29qUGILH5UAH705qtMaEYbd29IlKuWqcuzqfAAvXDEfzCVvtvG2g9sw6VYM1N6kzaZEGQYDqf9jS4Fdx_iimPcBHHMFnEBF0voHgTt-pvuH6xTLRT9tlCgg4AHlWNK3Zlnqe0O0wKrSDL-OSfalN1rCpzckInRXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2NueKBRo4XvZTxZ0nPAgsnz3dKQqR-9OwEPvNBTwkDgdXeXirPQy4I7_etytuVN5isXxGc5PcTGqh1oYvy9mqz9aX-X1NB1Mj02FVvs_CO0Hc0SCTsxWRW4ugb5KPV7qTbdHGC1ler_hIOyRhTLENMEi6lyhuCnnA56MpVtOjdjiYQaKVn3LVlIzTaJdHbweIc5ApxfE48mSJ_olFtbS6xrkgsvPtUrdVYmsA0p80DqSvRp7Hen77Jb8Fx4MomLihHF4GsLwIxDT2wvSKgX7pxOipr6VCJdvASkLzkFKgEeDM025xHGReyhdAlQUtRy2ENs3aVuDfOF52SWq1q9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJtLKut5pyDdH7pEbeSeW0hkZ-sMvBTMHxdm_7Rh8qTJQVs8N6YOjgRSANsUlMapTG672lg_s7j5zSXvqpM6VY73WgMjSZohBQ_6GLcDnMX9x991u2oq0yopVVvF4yfVW-AHVQu514X31YNY_SrRdWYPzajsND8YMUTSXCrdd3J5D8tMjODjEJm2OxZgy1f3uihLFMWUrbqACxfIeLUezz2SnaEwCrxPNCpsaVFryfSSCf6xwDSAqpUsJn1ub2HRJGZabCKxc1DUFmBT5YQ9PnrH0AkXUbELo0diLxqrLCkXyCfqvuNh_gxzjeXm57MpWjFXBDa1RSoXPxj7w6t5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2fbpeBPN16mVaI_VPduun8uNYytk0bGfnMNvK8Tcoy8j9Z5wfNdtKSiDTPlFqdsUftzOAyd_xVtEjRT-P8cVqBAH7hUbb4iKFOnwaqE1YoZ8qrpGHmIxVVZZpDWO6aAOI2mRuqU1BdwImgZfCoKkNhiKDG30TKRMDqreVdwS_fz_Aa25ZZqbGkXgXhrS6JffP4mdyWLTHLpOyC45tU04BR0mYSSH1jtQhmqfVTcfIU8Jl_yB9bevwGIt4HAkjL9h7ilwU5JSgK62_mi9B8R3_s12iMiPKwuS5_J3tVLaRB0DCffH1T_AebkIHPPlWg_rIhj8RBPF10tccUDRd5HjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObXkttrjYi6ocxLbhKLej_kRE06WKNhhUO1uNJil8_vv4EPrgL6QOpOxQ_12WzPCBrjfL0kT3QWzIZls8FHi9afC1KPLMjmGD-vrd2G_aMtSbTYSSkZ0_jSZu7Qt5nAP3h2j1I-p4QcWX6ITIuv7rbSTRE7dF7TSk9j7w6CWDOgC04y4PRMODP_ph-UjSoE0TeAubKntf472JpCBRvLJ2O4oKN5kqjTosMMI-5NBSZeEB-7wXiZOFJr4c_ZQlpncBSA1zFv9KRt9C3qkZlA99T5BSeWyA8qbVY0Mpln0q3PAd_RKbLtpZnSl6OW0QEA3zgwZHaS6F4jQmYwXlHEFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwurQw5hF8c94EHD-rI20zun6qxEf1a55qeN_v2pUO_U-85M_HYyUao2_4wyDXipsMcGZvt0iYka6ytu5K8D5bIFfU2kV7T0ZXWI3B2goXWiCYWY3xJ7KUefZutdTTIM8L3LQ-BDXJef3IfLow1eMMYUQAhiA1UJ24_DYdzZYpz8ZtiohoVDbmmkgMBCuUAMU8pgLg_H5rpXINuo6dxMyz1gn3E8FYxrRocnfGc0M-XIu5QY--tM6Eh5RQu--7c5RzADPRN5P193UOxDJ4EaUt3Uo7_gBs1LOmcEGpCmz2UOGVllLkJOoiAXKK5OGV2bPmHCnM9VsNlwyjsSaOyJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_nj1n5stuWPmdTSO9pBV4JmPw9utTFdtDahbm8kxWrhLB8LYdHYNCtvmlm26yXUWeVCALwBTT9_1Y5ZPYg7tYz7d_kYauioKyojLWpgYq-oTbEKlniUaueR2IfpBhgPQ527zmep3MwR6ZiCOq4-8CFhwTlsrJ0TiZxOty-cqh26JMW1OSGD5x1hiFLDIhcrTwF1fzQ02WeXuwEGukHx1vNCGAiGZ-VzB_IDY8dfT3HTqx2qxluCHuqMA-U4CMhI03f_bbNmPlh4Q6N7mJ6lousZ78nKIAGWQeK5fQZgXmPbGrcGEbgg5Mf9yPs48kT97F0WgX5GNLv6vuqeBsGoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRWHtB99Ugk1cljlzCDYPGdOJmNsIBC1gpryqLrdtmqTJq4zP__B4mlN7gaqHC17KQo2v5P-N4qbdOZAvIGILa4ZAaEoLJXznVXhsKjz7ucjWg5MIVfwq7jz7wFw5bC-TzO_LYCCtxDhJN71B9c8lkkKUaloWh00cKvn0neFXiGJ5ZYJK6nEQhh6l0XWDPyMo-hqeLCEL0NVA6BGTLNwTXvTYWTYRbWhqarCA4iL8XxhM6mMLZhfiXqRkczvUvqAY83M9yq16FSyyTWoO4w0iuDkNQynrB4hZmYNELeFCF5fz8xG5AEVGsle9OTwELlrhhu1XrKDt0qP9j5oP_-IIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr1LTHT1SwQKBBnLEcAzK0Qe6UBMKUa_LFFhdkexIxlBealBq_L83-Zg9utYiTWLsV6FgDdNq2VIJRKr0uUTt3y6Id3AWjAqWFS69qsRyFFQlhrpdd_zSn9cIrQc8rFc_IjY9iHvcwPoOG1f-WgqGtrhbMb1vLUY9ANHNZZPfcw52hmSyfntn1d22gZgjXHDf3Ujvp47jYRyE1l62Rrh4ek7TcbNlsixexjmlBM4v7r5UotgJtAZyeg5sawsMe8KuI_xE9AQE5P4b_g2ZVgxPWG1y8pcEr6jAKEevUppc0h2PtaOkTQOcTQCPfdS_3f8AUE8SV_NLHssWzI46zCiAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_G-HKyc0Ky2gJRIXf2mp0Qt8ERORQ4yoDliYszRzJSj2WmA97Gcgl4RNuw4D1fLNXTDKb9o_uE9OTuZar1SYbavcLcP8z7FYu2eJbQNBGF3LHRvvY59TGNd1ZZ_SkXnwrwumARHDqLmtpkmDoxjyN6gT1TZzuDpRD8w7VThlSTrSeaLWofzca8-XLywvBEfP8i3vTrIm8mxqFsdXHgx_iqBc0seafVZxPmVhZOKLADZqupJ4d8gfKWzgX06v2hFkKNKTFEWIfdVGMYsHK0IiE87wb4H_0xELaGIyvbC8Y-9Cs1ft5ojuyZEzyBsSFWpv5RMldb83H4sj7r-ECs3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5VgMGY5vkniW5GjcYIDFBda-SXmMpONKKkatMXNvvuCdTE4U6lPpaKLtjM8SJY70AIoNBj6daTVr34cWi-e3KazYXzbZxD4jC_e9Nq1qakeOOv9-zxRE1bdARyqFfeO0GSOgmd_VXAxQt-E97FONBq6qgcpbIo5s5837icUD1GJPtTk86EFMBv8sURq1TjlGDKzp7qieSKxQR7OUZbdRkeztGPoh4lclBHsw8dXI1Hw7tNLcyzIBqITk6FqTvun2jKxaPCmaGWZN4hlR2Sw7FMmYF0ZfQt-KwsbVjLk6SJPR-CEhsd5ztHrhFyfUHVRvxzVjisGnP_Pi0Abz0jUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HewmWIPiN7-8DqOoJjz_MrUzbHFJp2se31kAdaHI_UxkvQj41jby9YqfaZQkxhfBAegk_QcEX54nlCt8pkjQrAdm9iPwxGqCtEKgFxDQSxjR5VxM7iHMsSQ3c9PuHR-7NnDduMiOK6AOXmgpMMvz78XduqdveHGdGugmWAk-jo1TzhSNWl6GwDtY5ymicdYtHvoe4ZTBChkchuEmYerokDkRgWrTMMrQ_NWpf6qVhXFT5KP6CjgqOhVx-kpmH2_GH0px5S202VlaaWh6fdRRjSfVKWNDoJ02DewZy7HSwG-oHZRuAbkrxNwylUcy1yl3udDtdshXEH6HqKFkJV-GLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZzmujS2Vd9eoYXMyge-kOQCXoAU4LsUh9sY2Valumt2bZY_RZRdB49Ne6BCmb__29sjrwBQHeOXg6YEnGQcR0tfVlhxfNgkOEBUUjcYOryxsvskzeApBcLfy30rEpm11LAEo0aK29zi5WIpvfijrWmh3EEerc0H_Dz_dDD37QVce9wu5gppupyAZw9LeLNmwmTViTiMofXtBVDgO8TOG3noDI3W6vdg504Io4qo-UORjSVrow2EyHaxiY8HMsCq7IM9V75AgYjSXifutq_AtSGPSJdrourZfViDZFVBrLrwcdW5MaHsv4vEK8v1CcAYpc_23IuaIjFblvBfVfcYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw-Zr2jui0CDlJoCWrlKmaM7uN-pwIyRkNdlaYkpE_zuzTWjl_iTkoFQsZRY2bmo5CISH_bkdynDRJ-0sJXajrQA5n2LE0EK65qMO6QzOuo0cmOgnpEThydt4oMcTsAoz7FgueSKMcPi7vZU--wnJi-YL6xHgJUfszxSjlQpB-dgvJp38xIYHUKMc-ViUkGzNDdK9YkkGmxAOajK9T-nTh6M6-w3aQCzwrQpOhI5hFqyet40Vh4drX4RA-VXb4ofgGqCC0D7x4NBsy-CtwKX6YqJews1p9KZIb7wzkVHFVrattQ6PJoFWPgVs5hzpLi3lI9yLmLsxnuJspNZ7edwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYTBiq-O4wKfHjGdQQnOG5usoDO-coIaEp2quqLluzvG6H-fV5BW48qepFoUaLukWUV4JCwbr9udyfu3AcPP8RgUTr6MpQGm9pjgBzrLsa71YIWjFqPAGVkytTIsCv3DRB_vQEwho8xyS_YRerBLCJS1UEc9DhqczAWf0Gxi12g0oc-WVwIdAvWk9HELYY9LEABHTRmbhqYZCd7onQ7sCIat1mp1plu5vI8SIZYRZretrQu8yMDsZ6mioedBPiXx8RpNyahg06ZIO2gUJCrTMPhl0fDnwd8xkFUm0PP2s9caioMj0-GiV7-zwfvd-naY39ppSKrReOknHRMvdjPhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikB3jEjJ38-1FscG9bsdVgbEAXXqwSW6TuMzOP0hBmt-JwR-Tk95BFAH5dkG64HEGRj3dXieufHq_QQCLW26BLBOAI2VWpPPlpBS4rMQhp9Mbl-M0e_rmk8U3ZfDdiPW9vXoOI1OePEO13zSElUCQYXxiZjDsEKqsnBFLoyr-FAGvQWwHaHAWLdnQ0mLmSqrbajLWpse_iCsMA3GcOuaUZ6iaJP8YiDVHSh8I_QQ_2CamrF912MGKGgLDlsfSoFTHrhWqOmDrxeCx5bfmi1xPEcRvubFMlbBjeO68RTbiQIBL-ejzvcLgRrLQ8Fo8LHF6e2q3mCguvEidyMC96ctxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XViANU63q7timvLJf0BJoDfVgLiWSeFQsXlWSqJtGLAtTsKZveQwGjRCuNv41wjVriMdQRMHyfNr8JfId2sBk4ZqjlojsgL00s5x3GNn1aagupu7CBBsIZ-ZG4WBlKHewNSwilArF37kvno5O1Unl1xEp1WtpiLcrRSzt8OBW5aFfEettiSCMh3XPzPwljhs9jmrafLODI1B-jjfgjU9rDftmgIuS26PIE1lRrSg9W2hEMgnSKBGFLeMs3s6dlYiercUa2Exb9Iwk4kVkYX0DDyrtyYBYc-WImdpJS6AApCW8cfkSrA5kpKufjqfRGf86AToamBWINJj5okeIdPpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6DEv-STuVGUoYv-Dwcib8XYeme4mrpJMP1wBrZz_xuM2BO5NTHsWdykk8d2C6p-g7jsdXyqBbrVKsB3lp0QXor7iOu1x8rM8WQKeVRvhL9fCKc_y0nKE6Iq5HcK3VTlMpi8rXO7DiNsK_Ya80vQXtDiw-riqsLDGJcMnxFis_ut6F6Mo6Fj4ZgOR_BH7WyPbpYjCBaXINpSL91U7SNhctRttSKAp2GDlH0Xiv_wDyxiYDyoxVoc8h2Dhk8jhgZREEJ7ov9n6XN5i-HmEC5fRnz3dRPatoUGmBYaqQt6t1uMERZiqjsLJKaQu1lE71JP1L2R6Bz5McZyLxKZZVGb5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itK507ZqQ-uFPlhEO8Zv1F_4eVcKyC-vPDi6pxyXt78Eq2heejn_oqwdG5XGzTYgF57G1ViEm-tI66FKvam1HWC4X5pqDpvUAFaDac68ep8Gc30kieIQGuVkuIYAEnfWfkWDEDwplb56k75Z9Csbwlc66jeWBqkarDln4ZmYnRykoRCqq-VxDaasZDxucFsTGKp5Zu5kVZxXsM08BiuwfJdZCaebCjYQrl_ZBprnsxHZZ6CS_HXvGt0Bm9axUVhOY6qcNBQa20lfZmzEHS-ucQ7SZw8CxDxnsUo6Cw4v5pnlLaAtu3BE0gF8nZwHHRBgOmt1jeBNGQvO7wcs0Nx3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIu8fIlQu0Qo62Sq95H176JXgF0qa4Dj3QjUxAFJOie16loHAoAecACr60lncu16Qmg_Nk0AZTg_tTRnmgmI8FwaNXG-Fn1IX8LiH4ctrnlr_X0UvPq9v1fgQvfEgOlk9kx--A7k5theqEOEX3EHKb1LZefM782ZMUDQ5Y9NjOFsDABDaPDOd-ptaTwbavzMNTwWfaKTIPoZUWO7hJ1J4m84VngSsp-WqFT_aX9B_giD9TNKSR59zbIIo-p0G2bEPplCLBGUSTLG2AvigixgxRXvXDr--KghX7Q7i82zw7ga-QLv94r5FhcpVbqqhhlPJ-nj114mhAXWojy1zjjGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0-tmG3tqdWQAOwQDe8BfTykgyK2dC6e27GAeS6DWFRfpj7OBr1nxKl6Tk5cVv-in9vDvYKsBX7Tq_TrIbqeslLcH9av4gtTYdp3XLIZrZ9pLyp91lE0lfJnzZJjvqvBfSCGjcmO1m40mpCusj3OxlUsq5fyJbFwvruGqwxSjkR1R_fEPlNxbvJ-934zz2rtWGGiDIacci_J7vttFAMGz7sbbg5cWhzGEz8PBAggaMXrXPDYakNjbJ5N2TPCfRBKADtUqSyEcHx1qY2wRIfTuVntryHkH85ZRvTiu_JYSKxpGdJE8Jx-_ejUb00p0LjQSFMMsnstZMjHZYrn2G4V9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXxc5BtlDfj06CEFzvRtJUgpKvx9-SQIyW-VXO4VOOwV9qP6hi1Td823FlESGgbeo3qss-UQbxOqBlQZC3l15NoAZE22FEHwh-lBG4GNunWMbweu1Ci1mLoLvW9jmIEtcSD5V4gxafMrG0v15qzwj030BL_fqhvmU-bjM1IG_srruN_HOkUhkv7DQKRNTI24FsjmkX4_KH5nKJc6OKepV1Zy3scGqoSp8UDbODcyxQjrxctG6zTiBpj97uxP42yN9B-jjN76Vrgu3ZFjAXiPlXTmGK0zkY8cpTALCbtwRbd_lnhuMoNUmTT3s1xXSmzLzLz7Yw3GQ05BJ7ZEVaMM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf-ct3iU5i7LCc-XrVCyuMMFu0Oj5xdbVETVmpruJlw4up2sKnMC9UKDC3T0yoIO_sHE7I5KyDRERINvLKl9ksPXt6JDzlPwKtOzH7MT3s7HiiWQPG2IfVFE77Fsuv9ZIIKUZG0rZjMbpC-XGiSb0uD24nZ4l-CVP4PwdQ0JPUaKYNhZUsWPB-uFa7U2ep2FTPCCpRBZ0eAKiI5EN7EnRskK8AcgHCguB2KBz0M8YdQ3IGjIjsRIHec7ORS3ZxWWP_Qf35nzqsJlQooba3Rf8Y5e4tArSI30jXSsCzm8N-4M-PvkK4vcuPpyFDtgWA1i-xGsxJQdbtN33iOpmM2cZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRHN3oZNZ5wzzyUJPfWhLDXXRk_h4VeuLnC6W0ttM_XBVCDmxPI9tftlrPkG-NYeST-z5u4fKaK2dIxv2PY78A7cLuvZ2gK_DfPydN7GVx0ZcX-H4-cxSUqaAEsImpsp-WcMm92Afa2Gym8DMVZ9w93zwxYQ9Gja_CBd3nC_nfThFZ46E3kHuVW_CqRSHR8cJx4ixH44noA_ux51wzr5iOHfojRk9dRK42UsY6uEWd--WnjuBR4HJuV2mXnbvurYALpgrYWotp2PQNsL3JTDtZx7R0vuXTaJK2MXti-5iCwGnmgizXoFlQvG7krfalC4952SrY2cN0z6VHV0-LxRtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=V-ucLnbxkW-4zKSoIuEBGSs9qVBOm0kmSgJcYrCxmJErX1tJj0mMgtJDzJv8B_rMkbOicVg5BNGII5B6MfZsfdL-HD8qHtyKsdTrJ_zBhxgSM_ZGWS0BPFy4QJayQLsrq6PvcLmDi-j5JMfFK-dKtA31Qqychu1zn4YczZRokqU9N-fMwXybHoJ_K40VZ0IOFjgl1DFFhAFqWXDy-NEmyRDD7RCYQq-p-h5fhCUQ_wdq_Lwtvt_cnb5dFjTtDiaT_qp9gvhv86zOrVMbgcXlROCdezPIuSCC__WNOK3kcPRSrf6t_n8HsBaaF-CEttSII_FLF5MYHoxxBdDYU-YQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=V-ucLnbxkW-4zKSoIuEBGSs9qVBOm0kmSgJcYrCxmJErX1tJj0mMgtJDzJv8B_rMkbOicVg5BNGII5B6MfZsfdL-HD8qHtyKsdTrJ_zBhxgSM_ZGWS0BPFy4QJayQLsrq6PvcLmDi-j5JMfFK-dKtA31Qqychu1zn4YczZRokqU9N-fMwXybHoJ_K40VZ0IOFjgl1DFFhAFqWXDy-NEmyRDD7RCYQq-p-h5fhCUQ_wdq_Lwtvt_cnb5dFjTtDiaT_qp9gvhv86zOrVMbgcXlROCdezPIuSCC__WNOK3kcPRSrf6t_n8HsBaaF-CEttSII_FLF5MYHoxxBdDYU-YQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgryyY1rLWrKUM15b23vZPMmCBIZ3hjLBRvN9_U3YgU2qdwOt3X7vcYQ04FOkCvHEJWmF5A9breT84ZwYGNtn5pS2FCXar5ew5VuKPjOa7hUTtlCqgHq6n8mrCIETW7HHpU1eF21XgN8muJWqCbGjorT33BsSPeQGruL7hiyMp5mo-Lx9Pi_1e40aL-9L-w8SRLKenFRHOgOyvgvQEGh5TDmXqvVP1Bx9N7XF-qx-v1Exa4rEjizuJhCB5eZmcXAHOFz7hX6ayGKpke9by-y97_n-6tTDwut6FbA5h5brGIvtuMTzxSS-7U1nSS1xPNGwF9eyWhoduZdctA9tG0Lag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=Vz2KqH2krhP0nxYRdoUxbujQOPQUglOlwBbqUuEzMroUVx9_fYEmKDlQvXKdSVSy0zum5Igcu8iyEszE2u5WQyqJDZ3-zICQ01LFZXsiPuxM1TiAkplJrp4-w60E-P_BdV5maPQR-rt2hgAgOZFOy9AKOWEF24qRyuHJx7jXld_Dd-l4OfVw6j4XPgnl2PRy2GnBRBGwo9pQ78N6X0L4xbUwB47b9e2uYFyGBKG_69kFNvkahn4nIjlv7v7D4ULAWcku26ogW9fCLWM-f4XivDn5jU6u0VPL9_P6R4dj-QV4R2bTAZeYimzfpGEfB-bqSE3S6Dul96Z8ZDENgK4EXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=Vz2KqH2krhP0nxYRdoUxbujQOPQUglOlwBbqUuEzMroUVx9_fYEmKDlQvXKdSVSy0zum5Igcu8iyEszE2u5WQyqJDZ3-zICQ01LFZXsiPuxM1TiAkplJrp4-w60E-P_BdV5maPQR-rt2hgAgOZFOy9AKOWEF24qRyuHJx7jXld_Dd-l4OfVw6j4XPgnl2PRy2GnBRBGwo9pQ78N6X0L4xbUwB47b9e2uYFyGBKG_69kFNvkahn4nIjlv7v7D4ULAWcku26ogW9fCLWM-f4XivDn5jU6u0VPL9_P6R4dj-QV4R2bTAZeYimzfpGEfB-bqSE3S6Dul96Z8ZDENgK4EXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8XI2Cn6N4_pRjFSNpMQzQNYRl9qYyaCJtny-4vJ6iG2Rw7WSFE8_-tpG95zy_muOBoE48LUo9E8NTooV3zRjoyzZ958RAFO8D3bQJ5Lrdty8zXvRniwlRIfFFZupmaacR_-C7j5nBzfujjHYVHbtHRpy6berwUP_rN5X5wEP3lBKCZznxtI0Knq7ilcdrOCGP3Ve8wnFS_RwPw6zRzmzmV3f9t03oGiQOdQqEJs0RkejNZ3zNET68rUSQho08i-9WB2rRY4VJAgBNAqLmbT7HT5tSv2v1012w8K154rHXammeXHV8q5inCv--U66B4iYWsAxbk_bRYXuR6hP2kRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2y1D-xdORODvGesE1kEQzHRs1u_AkomszKgPvLZUtwD0aO_Pzzd32Jl8wnYWcd2fYoP9sKPFqpwF4WL0yPbu8E1H8rvESKDMcK2ZOj_2965OL9T0LdrqYiY2hUAgaMotLVDydpn0AwIkQTYOfhCuxUta5R5TS43gxqlb1UjQK70qhQAKAWSf-spnYY2rNtVXiZCu97lD1Gny5Ptm_yIUUO8pf9abtzMriSNPQp9HA-jI-1tfGSAhK2KjknfSFxn4zHN5iv-r160vl8tA8PHunm3U5ETy4ugZBqF2da3qNC5S0ajV4Wj8hD2CDLjTXSg77etiyUD3GJsqVdTkSsDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=qg_wG3JxwBZfQio3w1gkURMhvENYPlbVhrSlG5hegkqraZOhZ4dkGgPeNGWnAbzlWrrUpqp1ZgIabiSgYl80s8E_Mop-8nMqpsBGTmQ9lCdRhOdqvdD91oW99xbNH3Tg8SxgDO4Camxl3b47kZXLSaiOODH9bGkuhztJtiZgwo9IMFk-TEMHttYNWIkndjIN59j4ib-UTPlNAQlXaN03dzS7BH4UXJTzS-MdnLnUNlYsn0H0QrqHjsk6V19m1G1rpyg3FDLILWXi5ROjVYOTXMyKMcOj-UBo7qWe_lY9c4EjI_BMGkDunxsmwA9yqiiEF6jHg40cdMQV2Yv9IeAgtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=qg_wG3JxwBZfQio3w1gkURMhvENYPlbVhrSlG5hegkqraZOhZ4dkGgPeNGWnAbzlWrrUpqp1ZgIabiSgYl80s8E_Mop-8nMqpsBGTmQ9lCdRhOdqvdD91oW99xbNH3Tg8SxgDO4Camxl3b47kZXLSaiOODH9bGkuhztJtiZgwo9IMFk-TEMHttYNWIkndjIN59j4ib-UTPlNAQlXaN03dzS7BH4UXJTzS-MdnLnUNlYsn0H0QrqHjsk6V19m1G1rpyg3FDLILWXi5ROjVYOTXMyKMcOj-UBo7qWe_lY9c4EjI_BMGkDunxsmwA9yqiiEF6jHg40cdMQV2Yv9IeAgtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT2Vq9l_pi6rAREmY63cKahrAtYY78b3-_sjmEdTZ8if34E0TZRLSdr_h2Ef6UD8UGy8HZgjEP6LJIaIh9hArmtkZWQRwdMUZoLq577KVjT0RiA4lNEnVqsWFCGnBtZz7cmfpVj3fJcJjTmFK8TIgBiIG1xFM6jdQfWZeDHN91we-rDEQ7cmRwATlqforBcbvaroJF5aWC107aT-ZwFTKZFds77Ax8foJdkgUBY7KQFSm0dXWWkiZR3gnKPX5jcedGD4rhCTcjLTsXXQxVQlRswn2XSbYSw4ITARPQ0sU9c47mHK-XgvLJMBFV2Q6gNuck-6JNQjUXukzuJgu_K7eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq2yYQz8hL_UHBQgmmNhYSVV_Gv8C2Qeb52pEhcD8mCeTAvRJc07C0gNmE2rtnQE5V2L-kVFZ1YCXdIaSDTgJArESyrmdrlc6c_3A67-cW2HGvbQUQHhJsgmtOw-m3URKeiWIJDuTO3VIVyLQIiv2UITYxXD6VVepXVLxoO4Nm3jgVp-KG1wB9OlgN9IXofgrI9QMl5nlgKlSfH4TUt4_UQvg3BGERPyXZbbhvvBL7alTHZFln7AH_PCgOwSsQtzrczXuqoQPP4rrSCYJhV1H4GprqHKrstNtd7VUWfzb79kUSRjggv8ePG52J6CYTOcBVMtsWN2nXnIxxJMOWYxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYskFamFLpcu8UB1JVyoTGmU0SuCfX-uLR931LhHZT4x47T4Ld1nzhgNI15FWSTQAqTmiqzmIAYyJLyEzCGGxK5ENwjTV72yCEXLXZl6uQGrAygRLH2g5Btqk8nP7rhaInBzz0aezYOnnDNdiu6yy0GQUYJP1jec_LCxdm5Ulhl5h8jJvo5lwnxGk_yOxCR5b5qxnG-vvEePE-L0uOAF93syv4sTbyY68cq5mYXO19xKIr4dKEMn5xdaNlWrAODZjYXrkjvWxpJBxZ42jyI3udYzTtopfvAWpCuNcF2G3p-23g9AyPn0dcy7Orvb48h0sd6yguSFQvDr7qFWjYB4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=UsSrWDbv4V4Hv7fHQrsn0JXzNrAlx11HHLk8VEktsDFGONI-2a-E2dTu1_MA9NVeFTNw4-FeAHT7wVnzTHqREBBfXfEU2g1s80-KXtowOBgOgZ8inFQErEW4MyXBD7yXo8MX0UD4UrYBl4JKI6xMWD9vUGN4VP34sbU5qBchDIwHOs3P7JHU1Whx_5XyHmgzJALUfW9XbCJPfD1O95gRul4kGfTCq1MhScsM0YXH0GOXBqNoQ-VxO8ULZSWQNcKLmMmeME72W4WDgGZ7dlwY49ezmRG0kbGj83ftE3-NDdkzwL_7rlMzp6s8_uchdQxV2yixx2jJnqbILO9HEtY9lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=UsSrWDbv4V4Hv7fHQrsn0JXzNrAlx11HHLk8VEktsDFGONI-2a-E2dTu1_MA9NVeFTNw4-FeAHT7wVnzTHqREBBfXfEU2g1s80-KXtowOBgOgZ8inFQErEW4MyXBD7yXo8MX0UD4UrYBl4JKI6xMWD9vUGN4VP34sbU5qBchDIwHOs3P7JHU1Whx_5XyHmgzJALUfW9XbCJPfD1O95gRul4kGfTCq1MhScsM0YXH0GOXBqNoQ-VxO8ULZSWQNcKLmMmeME72W4WDgGZ7dlwY49ezmRG0kbGj83ftE3-NDdkzwL_7rlMzp6s8_uchdQxV2yixx2jJnqbILO9HEtY9lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=T2y4Fu1pXDFvvVDFgLsp9tLfUAhWGmd-0tYY_QaN1nDA9_k2HzcGuIMdNkD3prD7gfnov7znHF6pHqfYeWGM2eV8jCi3euHru9AgnMkzgyrjZiJRSgBeek8evOu7WJTu8S6Q-8BP449LOMfknMrBDfqYN7gcBmImVs6XSb4hMdrolXh47A_u5wtaaIB8vYpVqcZohig_ZtYkWr7xj-0t2RV9-2inD1QgxdCrLtYMDKt6zFze6BBgSGiiPNJ--pJNmWlIxjISuA6US96srHORir1PoHPKKz52BG9bUOpyxgBBTD9rKqgHE4b8T1sQsfcfukIpdWVHeF-M-5J6Malcow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=T2y4Fu1pXDFvvVDFgLsp9tLfUAhWGmd-0tYY_QaN1nDA9_k2HzcGuIMdNkD3prD7gfnov7znHF6pHqfYeWGM2eV8jCi3euHru9AgnMkzgyrjZiJRSgBeek8evOu7WJTu8S6Q-8BP449LOMfknMrBDfqYN7gcBmImVs6XSb4hMdrolXh47A_u5wtaaIB8vYpVqcZohig_ZtYkWr7xj-0t2RV9-2inD1QgxdCrLtYMDKt6zFze6BBgSGiiPNJ--pJNmWlIxjISuA6US96srHORir1PoHPKKz52BG9bUOpyxgBBTD9rKqgHE4b8T1sQsfcfukIpdWVHeF-M-5J6Malcow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbgrLz0vUBSaaVz0rdltha6joASj9PpGsN45BJdatw76s9xlxUDg9dB7JkzsRuPG6RDVFxZVb-tUqsrU06w-hDbUmQDO2wPds2pOPRvsUi-U3vSh-zeiqcxwZNYXcrjELvMQDSs5bLZ8ZuJZWyeN8ex3TC67-qxF1JZ7OT0LkFbZtZlnzMsxOmtDUO7LilBbgPw8hBf7Rl8S2L2D_V2fR1otR8REDNhG1mLxLNCP4uNpC9JeWbTjp2ODC6fBjRRL6C02ZUcQULw7gPtTzNNs-fUdPE2gVGbJz2wLiREhFm07NKeNiHGCTSlc_u4I2s6HnWtdNet1H9OQx9WSGtIBEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl4wq3JtouYMAIiVbgaCjhIsxbOSENqE9o8lP608eiAGpxpttTFvAqymBxNBAHlsfGa7lSQ4xexOOKSiMsZ_yE-b3hrDYMmQHqCsUXD-BrpC90w51R-uJKROc8jScaKJeddt035rPKByWHQizLjI9nYHPfOfAQuPR019WS5aB6k9wTtnLmkKvDSMwkR_qgRg5nNU-Llhl-wcvDOo8Wm66bli0-_WOKQwMCFCaEhNupgDNIfqpR7a20jMcI4JD-sPHkYVYrKYLTdA-oEZ0Hzro1tYxqjYInx1k_pF7rpZistR0dAZ_I0453WtOfcbnVoY5NoLJEYZ291K0jU4x0nCuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
