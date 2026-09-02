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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 20:13:26</div>
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
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKpL8XcNjuSGgDo9_lu6V_4QskFWeO2xeOjdfxmlZ7AvsUIYfYrgIZn5EgiQSrnX-61crc0DH1W_2EpWnADkqjPatHdfTd0ilv6y7g0V4oLVrbZL5sGG5mQoLEqemhHTDOZtv5M8wvMcfFcLQdpBiY0DV0rxADtujt21oWItnQ21XV_53G1GoIfX_bKnzgNccChoj9-hriznKywmzdD2egGMoBAVAoyKV9jcI4um6iiBPjtp6C2Cxl6wK-smoeRQkEUANIUnTFKTcqPYqZirQK4ABXyAttHrhfJBO22h3z162Bg3yYaFOzqYaIDUYT7vhXl24TR1MX6mnLrv1ivvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmFcd86Chy_8xZWRI5DRyh1zFweCHRGeOVbAUrSflhmcVyZY86Gm8wtHam4CtEB6wjn40qPM6kzBrAngRlSFpgre1NfdFT90_UgAlAagNfQWxJ8IaQixcg3pCpxO5mCDyPKS79IXoPbaJVr_D0jJmUvayGC2FsHeKOoZy9a6XvoWYz_2PGh3MYbLcbQCKDKEXJiAo3PUOhE5jctFpgPqjDN46WgaaM5CQtzHCREGFjWP20SlO4lvy-bPSW6URFW4hIE4H5OL-OUEzghes6_nxfux1NHxfZvx8vXNnguMPwJe8N1oFKeDAnvtjjp5fzGL2Yuf_SCWtVz3WcQ7q-qqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M714M__idmOrh_9nZEqGJAciep9lVpqMRQzvBcmPqKirNQ16egO-sTpSKjpOV0T-8Jf35x6qmix0IKmnjNSUo2MtZ06SHLyXh4pqkFUanPs4zNKMacLlRUYrc86GIDe_jKpLdcfYRV1gAiObCHMWIoNVU2L9THTBpLipP8rKh-9g-haKTROJbsrQ0Y7Cv3qFlkRwUVXJyjuqmTln1P0GA8fC3NbHahi28d4WZE72FBfRLRIwlAOQfVhhietGAlrFMHv18kL3DOMRo2eydN_Yj0wT2rEAwJtmTJ9CcVLBhHtphDOELRDwQwDeoIAzE1NG18JsHIpngIs5fgcJ7dNNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMbTrJ1cxkKVtaWF1vAleUk00ZtLvk0Z9lLdesjnDJNCaO8OEkLzA2ZWybbgjgwQk02CFHooTqVVWsNewvci4b6GP0GfnFI8hYU6j_R9auI8oORe7-RZHcgGdaQcUhnEk-jHoH7w71CVjkCNOFQEWUmek5mnqykoiqD96Sl-JQ4UglR1p8CbX9CvhqY2_uOWrSiPCiV6g31M_-iOCwnWghCVFIbYDBYC9y3DIxDDwiXZE5oh1C1pDUspLmZCQiEFSSmiDRDOAWT-po5fcuqFGJn3sTqhZq7f-TZethkPVi7BoRS_zmpFeSetnHN5kla9o3OGQaWtTy0JqHuKUue6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmDjRaWue63TouEG_h3VRkHeRToos_ao4DABkBaHU9JON3q8lT3ozcHWijzjJJ3l4Z5NtpAMFL0dwSJiEZvuZfbmd1KHHhiHQ-8Vb7KaOk--XbalXM09Mq7JMtb8TiC23kNoIyXodbqNmr2U-kd4L_NVlzQ3tOM4Y_yzfZgzSJtLpWk4e2xB2YapC4BXHwiV_pgEa7ns0jDWfXiWaf4SR_0ksO9r5O6bJJ-aOGv4mjBwjgVYQfWR4e_bpnJuFAGhtfzrDGsDQTTpc6J5cxArb4D0-C7oZT0UMeEWPgTCpzZNGlJqCTcDSHJz3Y-34lFMuGsAf9U8ffip5tthHPWPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=LMKrlARAGTi_mj-kTPb4DHmPCcQ0EsKNMa52xC2viARDOefit3ECKIaruRHn-WpzHuDrhM5ZmrMdLMU7m3GvYkT6uNPuOwTbTPU11wT3MN9WgezOoJ1icVflGoETwPxG8GOKdru2AoKAin9HTBmJBYxxQ7j9B_M73Gml5r3mKAfJdPL2ZyBDrHVvoPxaXt0BWQRiQFVC60LnaOHX6ZbhMQko3Q3AYEjzKm3VlN9T2dslXYcL--aU6jlV8IeUPrlvKsIyQr5cY0MsA-aWpEXNLWYwqquxIijVgQI6erb_iOAQOVco1HtJ-8rqzv2qJa2oY-qJhZMeJvS7bP59yB4rLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=LMKrlARAGTi_mj-kTPb4DHmPCcQ0EsKNMa52xC2viARDOefit3ECKIaruRHn-WpzHuDrhM5ZmrMdLMU7m3GvYkT6uNPuOwTbTPU11wT3MN9WgezOoJ1icVflGoETwPxG8GOKdru2AoKAin9HTBmJBYxxQ7j9B_M73Gml5r3mKAfJdPL2ZyBDrHVvoPxaXt0BWQRiQFVC60LnaOHX6ZbhMQko3Q3AYEjzKm3VlN9T2dslXYcL--aU6jlV8IeUPrlvKsIyQr5cY0MsA-aWpEXNLWYwqquxIijVgQI6erb_iOAQOVco1HtJ-8rqzv2qJa2oY-qJhZMeJvS7bP59yB4rLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVBSuNgFh6XpCxl5dpaXapw3B5Bx15sOgl17BCTXwC3Wm7E5eHfHIvy8c9Bzhr0YkED7mXVhezxUaiWTPVGFaV0aqy7aAv1cXrGAUmJKvk_OyZdqbrcJRWLFaARKnSUvfukx19rkcag10RRbQN90fBL42-y0U7NRCvLfF2xA8RPsIhOSUMX0btIvAv1ZtzXBbUUwwQvZwhl4kjjBIM42wa5oOfxbOtKAXiV7sBzffAgunjMdjZde7zEY3L0Ct1W6Wc1ScpDRzUrYi1EMidzZwQiCYXyf47Iu3Tq9XGsNyysSI6LfsmCVKWe3HVewzGRGyxi2IHoc2-AYdgwFuZKrkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azk7kjbX-yT8hksaPKomzhWQ63EH0VF8uyn_MvZjBIXt8aT7Rt_5pSpoP89uJrfVdH7XiZQIwV9Qqej6QLsmkTVIlmiw16NDTEFX0ZWvo-fROv50A4X73BYYZbii3Yl0aruQty5wpRwpDL5hyacHAtjp4D1-_t4-fLLaDxi3aBCJxxWMvG6HMLqxi7kfweiXr8-iwyLA3Tmlc9XYcgQF-MN-TSNmHou9swlt_fkXtcLWj0uoAkya2Tzbskxr_F2WDGG8Kr5-PUr3PKVKS8XRH5vCJOQt8e9s2ZWIM5GlO818ls1MUL5GSkkkS4UUjoMurDz0DGtN3jWH21M_9TYR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbG0cRn6WbWTTpqHrfUBpcpkDTIrRpBp86c86YxmyMJHBRuTdu9aEfKTvNsPaD9VKyChLuZHgbWicpao1cKPpT-5pQLN9oYZWGMnib0fqqLD5TAAapP3xwN0OzZgDTUl9ls4EYZuzsOm0uPiWYtTcJWxQI9U2VEmbPyS3uYzmajwww4eJ8rVR_AmNzBkzTdBH5KXIWXaSVre7cuZI_kPpSxUCwasY8GnepMP2LL7rfDr8nfPlztlvm0JOlPSgDrA1u-TXqBfT4j7it_oYmOcP3cZHrncaC5TmFjbhF-CUSddXlkocsEZR-qMOv6znTXkevCzmPyVplTvIGnBqrp64w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSaV9jS5ar3h-U2I0PSkWUvmSG4Wb0KK1sZ2MG1mFZUG0PSWRHc0fi8cMkV5S4BnHaTugxCQFd9CsURvbMVcAVFDGmwZKZxNARqpbUv9_NCJKmTR6oE1TiCjgHWtX5wxG1jRQ-EsMmA0PG2Xp5HA6mJLZYK5jAINE4wytZvpRKcHssZ2ogfW5tfbWm82LU2U_Fpdx4lF3K6vtTDnOIMKNj2NE4CN2KmG5CMmMf3mpI-CZC0XciA7nc18w5AnTAEH4g4J441UYEBO4V4DVHDDB_8OKcHjuBQirS3Mj4fwIEN_0KuWnWXdkDKTGdZ136qXcrwVmQYcpIUppDuF0tyJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyKvIK70O92mcIGEXzZmsEExOa9YzIMINqTVCj8h_UNLsX37GnmKUiwE8txxPnEHVnXLlHPuRC4e2qiW9CIkj7NogTqJJRbYzIuxCFw13BVcRa9bGmDUABNi0DrRaxZzUJYdeGKfRoN0FO2JCbmmIAPmNIMwnlspPA8-WWz7SO3XhSbKqM6Be6DHgXdxuka8NcsifhhAUaOd5_sBFLupCFdmrZmMnyxTfhTm24698qk8scF-vxJSE-H5vqJbiMCc3Ru31KUDXK1mqCxrYDKOYbIax8JqOHIsG1Z1BtaPgp4SnCO5xq7qX4q_Ylbd4WL-EQKkBrPfac9j4gOuVKegZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvjkinlMV9kcKRuhbJQd_gftKOnMeYKSJHp6fLKd_w2ivjY5NeleBL1dP9f_MDcPf-NDsKJheWbcf8BSMUS4_RIqdm8Fwd_LEXMtGn_prvqcTWbqItlu7elsyMvd6wlJFWb9UlexYc97FqFgHD-RFcQKoLEK1dfZtbnP4g6-X17KTV2TaU8hUFHF5X-KQQlapiyoInLwJwtR0_rJFCE2DOChOJztcOqL3P7aLiqXLDwzdWtDzfpteNt2E5v92ExlLbsJKCtZf-YZbm-ezQT2ls3iTQgOkgMyPUO8cPTHE8di0Nwu2LL-wo5NVAc9MXfVh97ZhEMl5WFmBczIupqldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXZKtHdQvJlvS01kprYm99IeZe8j8-Zh1Bbc5-E2wtCyl3j_ERmEd26IZXA4rMh9dZEqBz0iY-EePTcGdu8qy0HzUlYqbxVY2nnUC4VQ8EYAwZSuxmhE5jj4M_XFxoDurphbONmcM-ire5dCmmqtfEO6266TpDARVPzE_o8PukcRfEBBBzjOHsXnOhcHp46ZnECCvDCFVA2c96KE_fGlW9kxf6iCgIQcbwSQYSYvRVAxNsfLO-mEi9D8gFHOHwnSjmXs5Oc7Ldlq_yfwoUkVZKkTSGF3nKui5_UbaQQXQj6YJYwWrztp2cy978T4dFDdo5GlPopliUfioPkRygTWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktsJCqFd6rUxE_JWQvPKY8n5fV98LdPgF60BLmz-K5WF8Vbpiz8FZpTUrTg1wX4YJ5Vo5VVFHDktqGGjUHKMU01pkzZ1sQH-NOs_1SDJcFharSk2TebMJNYdLk459hy4gnSs4pzY4cIZg40plElZgfcXIb3dQuRDR8pdBl5qoD75Sjz-1yOkDGcyhPyB6Idf3sxcPdZWSOwiNLQxDWlgNBzLJFMGD3oCcPbmsZhqMnxRP_mEbwuNVwnTkj4Hm5buisryhbKmIdCRFToZaHZwwtBhnvg5HK49Z4v1NAFHDXniqxlueBMdU0JM-5IIcgxqpVhQsFuqkZoVusrQxQ4Bmw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=faX8go2m5uNrhAq7FJVSK8M70mpApPPt-ODjV2_Uz6D6BgFb0uy62jLvefp3F1eSx1qD8pW-aDMZAKeYPSZRUKJtyyQa779iCGl7LTRQILAlzP6m-FMCAMp2uM8kfuKiIbMAm6gSnpZjBIkj91l9X_sjDRqp6mDYukpakAotQRnJobEvW6nUm_t0sV5WwWjv_zjrosKM_uh09BF4FVHgxdl8LQnal5WJoK0c6JA5z-snaSzTA79AqwOWRQF0AuIdub2O9jly0nWN3XvT-EM67BVpfGv0xY58cZ7dChYe73u24kZASZ2DYU5PPcELkuqEQmp1vBGxsFHNJV1cWr2tiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=faX8go2m5uNrhAq7FJVSK8M70mpApPPt-ODjV2_Uz6D6BgFb0uy62jLvefp3F1eSx1qD8pW-aDMZAKeYPSZRUKJtyyQa779iCGl7LTRQILAlzP6m-FMCAMp2uM8kfuKiIbMAm6gSnpZjBIkj91l9X_sjDRqp6mDYukpakAotQRnJobEvW6nUm_t0sV5WwWjv_zjrosKM_uh09BF4FVHgxdl8LQnal5WJoK0c6JA5z-snaSzTA79AqwOWRQF0AuIdub2O9jly0nWN3XvT-EM67BVpfGv0xY58cZ7dChYe73u24kZASZ2DYU5PPcELkuqEQmp1vBGxsFHNJV1cWr2tiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgLYTq6RD0IZl4hCSveAAHFvnUsA8EhBbfgiYnmskyUdYDIM9cZ0UqFN0fHpKCexj5BS5lVmplSmX2OHNRl1nU1tO2dp75W028dIaEeFNBpKtkTj-m8TGPrpCB-nTK1vbO_mIkHE32XoBW4BmpGUzp-Hab1CAVsjOrpwMgVVw-lLd0xOiUcx72oY51MbYsgseqmM5lvW_b9VP2UZwyfcl5RAzii4CrHhrsg7I0EgjOkd4IYaE2Sb9G9Mzg8diCTS01Hm8Iz4sFwgRq0oiJIKYtukM0lIqy7MyVxUwlyKgMNcnaWe8YGw_K_ahdR8byqq5X2JS3uWxjJmxnrKPl6cqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=FzLtfMdx9td3kHZwiphUMHTsVat7MxeBwpnwHXt6YhlSIZiU71FUTTRHv8d0iKLmYmjq2fuUXwZdGHUq0gECJ8jjJ7TvIOtC_T-run-uBpiDqkLpPqpRcbKvqqJgUHFBczy_64InOdacYoYebmTQvSMIvElYQCzQXGoxfhIlSiA3ubcOgGtTwHnwj8v95eQJfTHF9K_zE2DhBT2ZqFZLYgCU7gOemcZVCTE_YOrP66ScneFfimwmZ1N0ZAfSIDkFDk67B6Wo67oUn5Ln7n59Idu1oJ36OhzwCCkrrbtrhlYtiOudfIHfHUHRZurh_uXZ0FiuMsg2pSH2UUs8dsHVOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=FzLtfMdx9td3kHZwiphUMHTsVat7MxeBwpnwHXt6YhlSIZiU71FUTTRHv8d0iKLmYmjq2fuUXwZdGHUq0gECJ8jjJ7TvIOtC_T-run-uBpiDqkLpPqpRcbKvqqJgUHFBczy_64InOdacYoYebmTQvSMIvElYQCzQXGoxfhIlSiA3ubcOgGtTwHnwj8v95eQJfTHF9K_zE2DhBT2ZqFZLYgCU7gOemcZVCTE_YOrP66ScneFfimwmZ1N0ZAfSIDkFDk67B6Wo67oUn5Ln7n59Idu1oJ36OhzwCCkrrbtrhlYtiOudfIHfHUHRZurh_uXZ0FiuMsg2pSH2UUs8dsHVOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=gZEd8hHFntNfJovULeitXEPkF2ASFHlOqYlBxMzRxN2VbqQKS1VAtVF-85lfTd9AQKyqtmSDMjCbNtreNdxwoGbznmIEng6ZQk3XALkQbblfxA1NhP3f_c8nmhn9wILrkTPr7LfQUivA3qUHMr5lYUn1qupWIlRcw1nUrmzNuKooUxzaEnyOr2OyvBwPq5rDMMZPyDSH-7cCLaJckplqqY-BZQVBdKPfcTi8nOFFOaE9smn5g8-2uOD0r51chizrN_LW01WZhd2g24ZC26atcWVZCnp43ZUtwQxVee-OpJlUH6kbUg_SHfOi1wQUe2eGGJwS6jRduwRLh9tYTqi_-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=gZEd8hHFntNfJovULeitXEPkF2ASFHlOqYlBxMzRxN2VbqQKS1VAtVF-85lfTd9AQKyqtmSDMjCbNtreNdxwoGbznmIEng6ZQk3XALkQbblfxA1NhP3f_c8nmhn9wILrkTPr7LfQUivA3qUHMr5lYUn1qupWIlRcw1nUrmzNuKooUxzaEnyOr2OyvBwPq5rDMMZPyDSH-7cCLaJckplqqY-BZQVBdKPfcTi8nOFFOaE9smn5g8-2uOD0r51chizrN_LW01WZhd2g24ZC26atcWVZCnp43ZUtwQxVee-OpJlUH6kbUg_SHfOi1wQUe2eGGJwS6jRduwRLh9tYTqi_-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI9hOY0ECAO8XqTQRPVa5PG4jcGTuofRPoLytzCUf7VWEMlZJfzzKrxFR3fTMgsiNR70DoB8bFk4zkP7RGnrKK4cA3j7Il2iwaQHzI8wE9zG9rf6wgHBHUvKbfc80X3Vmq5Uu0e9tRbEFWziKJpzzCRSKjKfETLzfeGl9h4etQMtz3Z9Q1zr7HEdzAVClag2qxkJokwx2OhGHeT2HrkmamssKsfVEY5K6VvGN1xoPmn2M-1Wt7zeW33UXhSX-rkK23CiWGF-oI_aSFDcv2dPRH0O6sUIeFMcHvuvSluj0XqT-TdxvECkfBRjofmeWMEumVbZjqhB0MmUI9C9uE1a9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ca4Hry2dnEOCtanjE7RSd0T8HYM48uKPOqvn0tiNLtnuI88VhWPskldHh_rmMnZKjxi5QZiehaIEBt8RqaRzgwA25zJD1Pp1Ut3yESrj6tO-X7mDnacxw2-GSxa-juPrvUYBrrDcKK8DnFTFuR6UX_v-G7nrAKbhWxYSfxCsmW5Ln6-W68MKHHoO8us0s4dSN4wFfMUPMa36yRysdLWrNsi-aWdhcoQPNu02KavmAyF1ZAQAArusWKjGAJtmBSg1iJv31UlFjp_N2l4LJ-FLjaCuWvVJjsbGbgztvM7yW4sD-Rl6Xx7EUW8MdKsC4vRtRnUjpLzn6-zJ4Xxh_8gTAw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=RIeDKJKaQJOjihC2iB1yX8y05xBImwDvuDJ6ykUJo1JLbAPAML7_gM49Nrs2zVh2mSESxmyyZ0G9TUeOkK8R9SD_uE45tn9q7Y_tY7-rFEEPKSlvpSbbdlCG3Yup5V94EeT_p28WrP61TTj11q7HwzkVPPlGBskeSQCutqYIk2KB7ZVOL2AUEEsZcKYnkKL6bNSc9R6ZwnG5xsflej_vPpPQoYQavys8qwg_yRtQKip3V-nOLprxv6cLuVpu0sz-N7bG0tpq11qNEXiJ0QTdCqz_fNeiGIGh5tRrxGlk_OVdrY4F-X68M_qP90ntq0REJuzL_Zz1M48D6LDCgjokdbgOe5NvTcYDTkX7T8017pvzbJ8R-RaDblA7-_7SOfsk-_eJmeV3vuWGA-DM7rLQmo8uhJB4KexOnipuiCACiPYMiAMOpy9Sl-DOR8blqeH1YkazuFG2JtRUXXr-22oSiHmW7p_lEHSBXIugr5oqCzLpHbu4Z87wy_6LT3VE49Nn7553EFrlhZWXPUchI_NT5H-WB4WQ25RxWUlqizXWWUlweEIyU9NJgoEnRMks6oDYWttdLJD6b1vmPyXdLNYBCTKKopGb2JsNFFViW81Ds1JcUiOQ_fw_o5d9IXAaChxz9vre9S5vC3bmvhVLH_JsJXzZvcdMrTtnA_b0-1spjMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=RIeDKJKaQJOjihC2iB1yX8y05xBImwDvuDJ6ykUJo1JLbAPAML7_gM49Nrs2zVh2mSESxmyyZ0G9TUeOkK8R9SD_uE45tn9q7Y_tY7-rFEEPKSlvpSbbdlCG3Yup5V94EeT_p28WrP61TTj11q7HwzkVPPlGBskeSQCutqYIk2KB7ZVOL2AUEEsZcKYnkKL6bNSc9R6ZwnG5xsflej_vPpPQoYQavys8qwg_yRtQKip3V-nOLprxv6cLuVpu0sz-N7bG0tpq11qNEXiJ0QTdCqz_fNeiGIGh5tRrxGlk_OVdrY4F-X68M_qP90ntq0REJuzL_Zz1M48D6LDCgjokdbgOe5NvTcYDTkX7T8017pvzbJ8R-RaDblA7-_7SOfsk-_eJmeV3vuWGA-DM7rLQmo8uhJB4KexOnipuiCACiPYMiAMOpy9Sl-DOR8blqeH1YkazuFG2JtRUXXr-22oSiHmW7p_lEHSBXIugr5oqCzLpHbu4Z87wy_6LT3VE49Nn7553EFrlhZWXPUchI_NT5H-WB4WQ25RxWUlqizXWWUlweEIyU9NJgoEnRMks6oDYWttdLJD6b1vmPyXdLNYBCTKKopGb2JsNFFViW81Ds1JcUiOQ_fw_o5d9IXAaChxz9vre9S5vC3bmvhVLH_JsJXzZvcdMrTtnA_b0-1spjMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2I2BIziofWRIJXv1nu2IC5ii_4HQpX75cwP4xAI_Wi3YSxmPSh322ixF881H4Lr-c-yvvaoeIem6xZIHtYYhuc6Rr-LREKgKWeClUlHTycj7hyCqRFm0jT-eKPG9uQM5rh9J-RsVHaFgs4NGKzDdYUdV1YHIQdv78PLx1Ck4_TPQzsVv3fFZAwQHkb4OEvdhLTlg1qO5HSBXBm52Y01NzL6GN0HZZKTeb7TLGSFzvLMf6Pq--eFttUzsE7K-VboBkRKCBa4JHoa75KAp42ETKVMFkKj8UhWZirIvi75Sv3zPkRLNfVkh2FJadI6DMxj9e-OiDTJ27J94zIaWyjD2Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=rbLIDLVELBo_oQYUdfq0XPnu0B23zFigFX6lJ3Y8JkHKahfH2E1ExSQhm23P9pgLFDmz1uLjwlzoOs-z-5ygOlM7UNiwDCzgPApA5XmjqYPoK3_fn6QkK6RyBOT4j0T9HsKsdKlYSSSFdM1k09dMWB2xWJABSZV_DJGto40eT5UCXSXhj9zGnZB16KUq5hBprfwK_E55OC33c_diS6YxwPQj5suF88Otb6YDanr7XdZUqmhxcD5FD9JA8uIaCM-8S0V3dm96NGKmxfLfoqqxEA6rUZQNGcpeVymdlKW8tYDg9fx8qDrPh_Rvw51ScgPxqLaRE5Omn8hbnBu1zKSccEoEkFRmbBiLacC7ap3bdViaExZ6RhLot8_hYYLcWWMVbr-fHZapcD0U8IHX2xoGwYggGryhUFJT0PT31ckXl-sZE1SEISpML2y_2H6l6la-fzTsvwuTNjfmAFL6Xcpx7TnoiopK7tvBLuwHn6sh1AWTeNpgJnJJKyW319fwwmfQywaTekA6--QPr4hHSxtqJir8QJVKxhw4bwXZXt_8KmGFWBY0fOOiaK5tE9rCa3QFiSsBUlQ-x8Er5brifDSZ50RhIFQ_7aVmipyT9MAyuGPvNhILdfnja-dyUMe8PF52BsOGNXVvFmX_70nBTeMg2eM_4Ka6eaFVS7Rq1ZxK0p0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=rbLIDLVELBo_oQYUdfq0XPnu0B23zFigFX6lJ3Y8JkHKahfH2E1ExSQhm23P9pgLFDmz1uLjwlzoOs-z-5ygOlM7UNiwDCzgPApA5XmjqYPoK3_fn6QkK6RyBOT4j0T9HsKsdKlYSSSFdM1k09dMWB2xWJABSZV_DJGto40eT5UCXSXhj9zGnZB16KUq5hBprfwK_E55OC33c_diS6YxwPQj5suF88Otb6YDanr7XdZUqmhxcD5FD9JA8uIaCM-8S0V3dm96NGKmxfLfoqqxEA6rUZQNGcpeVymdlKW8tYDg9fx8qDrPh_Rvw51ScgPxqLaRE5Omn8hbnBu1zKSccEoEkFRmbBiLacC7ap3bdViaExZ6RhLot8_hYYLcWWMVbr-fHZapcD0U8IHX2xoGwYggGryhUFJT0PT31ckXl-sZE1SEISpML2y_2H6l6la-fzTsvwuTNjfmAFL6Xcpx7TnoiopK7tvBLuwHn6sh1AWTeNpgJnJJKyW319fwwmfQywaTekA6--QPr4hHSxtqJir8QJVKxhw4bwXZXt_8KmGFWBY0fOOiaK5tE9rCa3QFiSsBUlQ-x8Er5brifDSZ50RhIFQ_7aVmipyT9MAyuGPvNhILdfnja-dyUMe8PF52BsOGNXVvFmX_70nBTeMg2eM_4Ka6eaFVS7Rq1ZxK0p0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD9uC7zALBo1J8BBYyVSg-pEVjsNUeRo5IThEdpFsFj-mcW-3hG8fpzAS7EgEm-ucKL0bZ6jtuiuVux6tNgaHwz58pzU2DD_rE6p0CHf12XZpQwmr1fNO0EwBgRTWjaBAH_NREtnBB8VrgDWo-CmPTamfajAdeDD6R0jZW9Udp8AfVB-ixPWPlEos4q9qw_CmMXJ22z2J0rhLW_93pFPomDJBNKPTdxMI6XsZ3seqmwRLT7BZePOePKDlbmmwTX80uZhOrWOOsD2nbGKWtoKMcr3Dae3_M_zq-zNd1ISXWGyqXWiEHiJaZu0yYwK2JwLeJhqjATl0EAoVDCMTyid9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2ZP3Tyb98uDyAqQXEU6cKjg_26xCw46vQe0HCafVAZPXEr4A97scgdXMsfmzsR4yCZzgdVXsgS5cSY7qTPlDbCFb9MKGS3pJqB9WIgqFez3VpVmNwOxft23ToDX9fCKaEghYdvJ_ROeEsF-RyVkRAHMwigWOVIdSo9QerYZMqZRDnb82MWoUQ5P5nloavOjDDXjiSpPshI_8UMIfQMJ9LfLYsYSc5W58CP6i23oyMWEX-hDoVy3sWyinAg0hzDphcIsiUnBfGZfgn6bfdXxnq3SbPY5bAO-QxqfLw0HKilVB4XSKe6BhegcaQbp2p9Gh6sp2C9Qib_1CkPm9UbhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g66FvbJ1V3mFv1HPQeMSBV_7Bdqwm2iheAtiWS5VXvMYsQKRrwjkTnTL4Oqx1xlOD2nxOxwhKWHwTA2yBVcTvqCOYz24E10UW4UBTuAAsSfN1rKru8zfNQ2HDeMOB5wlnxy_UaanMDWcGs819lHjn8E4v_VJYvcBtW5tMnhG5RA62EGlkaI5kr5rWuGvu--Ng2e_FH_fmxprWQrq3CWbkArS8xjtdSpJ0RIm7NjAyhmf2lcPZE0XbEcX-loXtZdT7_lI_yzAzDnnjhjq67PgY6S8LgyxuT-g9cWhm4P76Hhlb82xEH3wU-juXHs6X78cNhNNZjoawzRn2guJ1yItEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHKpyibgnekfcRVCvWsQqVzp4fdpJYN9tmIt9CgN6YAccOsgpKn5S5W3BkvILOeOwqlYOUZ0AAgiOOxKqVmv_AROEnb7AyAwoKcufD2SFAEi7oUWH_gwYrlMEjW4e-oH0l2O2zv_EH2NnHYm2Yv8ryh7cGU35uqN6xV7Io-N2ePRdJBg1_wyzmthrB46QpBRIY4hzAR0kn2Mbd7u3IaemhQ8lT_5-HlSeJhvxy3ujKw8U5eIssyP0LqBMKW4QPEiBuDRvB3m7g5DOAht9YSi9OYLHATXayssjeKDI0IK6aFuwtA6--0GCrx-cO07d5cYJunduhyRX74Ta9E_K-lYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edyZkhaWBLQJCkKpMfs01khPZcZNxacZJykyfVHfPOEJJa2w84GApAe8TtIkJ8pqPauI8Dbwc1Yl549gOQtjbCzle_x7truINPXC64lKL_-oESRSZp7nU1pke5SUWwlC-3sUPo7eXyCqB0fqPP209iFFIXABGNg0RGZY-0F1Z1RD_kRzSwC0JQqWRAgOsxNcO1oF9V_ebAzooB1sqkHUpBqQTNRCApRa2mV-eb-UXWmtyea5aD65L0dIi2bpRf1fuIQCOx_XJTECU0pDAlOwDy57HDdyCoVORYGmsFYRibj8Y57pcWcM433pCyGDBrGw4jXNnpVOv5rz4Q_irI2eqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg5dgan8iI-7hzTPFQYEfcfhouY4TlqyaKhZRILyrXzZ1Aa3Qdk8VDraqapjTvzJtbH6rM6rs22Ayusnwxk_LPkEbD3Wqgk3H3Yo52p5vN0VBP6z8-6Ao3rR2wLsxfsthoWCe3XFJjB93ac9i13EfqEQQ0COK-4v6cPC4fPSRMD5cFYQ4Aay4kKA01Fs3QSBniAAEhgJIRRiKyYYotRrwK7fyBbh_im04mrhhQD4K5A1fShr0M00OqRpYuaGDLydFhu_kwqxteNrZ-Rp6ZUPeWnsXmT64Ng1E4GCKWTs-atpx1eIiBRs42wjUAycJtXxB7cjvfxRj2vUevI8bvlrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9uxfK-_Nf_4Db9rwAjBG1TTjsy8-ipIXBKA76m9hi2tKwliJRj3gIkqClkikUD2dFaukS5f5UByMBx3bpXArUfKb_-UqfZLwrVTuDs0u34Ub3xYHie5nREpCvn_14meLhqrY3TSEDcogTV00jxMh4P5wR8i3SCkw_MvxAOpFc2zMKgLD86fI2rr_5gJnjlCUIleQaZoMes460rdLdOuvElUqutFw3N5yn-c_dv7ZsYHFs80VMT83jJoXQc4k1bhnkqLq4xHTYP6C7dc2mwnSNFQHi3ZxzluyFp_y0lNKYV5eOnLb5yhuQCJgsqpdLXWNTv5YUsknnVLxJZP6fbijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ6NUB1Y8lbnOU56bmavhpHQApiAXTXg8lIao7nS9Syk_uBzSVLcIXGa4TjQJM-GEUgpVSoT0f5vVk1J2aZX6Nsfb8lMdDJzRpLiZkqsD4pEFbyxvgwrueTGBFCeCrYxpa1BoWl-wju5wish37HkJz6xfmaxf_vkeO6_qM1uvxqkDifV89YUmAirNGzi5CDqlmpcNip3BrgdbngE1YNGXN0SKaBB62J9T9HincFwKuaS_mWaj3rhdvrDwEBJdWML7dYa8k5agyrIsK-yry3nyKYGTd0pwEP1PML1tpydEbr_d9duxbqbLkH-zgBF8k7oli3w8F6uOQU_4-KbJpMW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0WrK58Kc19ed00t4bVoJ-zghu_U4MI6R_KYmaasezVdy2bGzkYZP2Dycd_JlGBWBLRQc2Tq26iR0GGE0BHqZZgrOHY7w2MLE6Cvut60aGGykyhfJQsiyvr7JV2boReKewzkZwoxHjicTS6q6lb83UhwK2GyKERxI-_B1shGN627tkbtmHPx4ElA3dGQmXly61dMDvKQO7StRSb1-g1G5XwC8IOnSDmLKZ2XCl_Z9voKL_g7LnQ5VRpdWcmbXKO9clWGfXuC8FBLrL1-btykijCJ1jQ1EBdLtXRhqS_3IJCZ5XIK1kEaD-kL8hiOVIfUWXHNeIkY-tkGz4-vnyyubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL9hFZGJIqKh2xDT4-HI38SEe30qLoVTFuUd7P54osipUP0tn-chYrDKwAAoBayy0JsYIUIvU5VAjDATVxMHUpc5ns7dsTUd0rMjcoY8CD_GgIusWZQiDlUaTZE1RHxNbWedAHqnEmI60Ld4SiVm0sQmGQFzULI9maPQO-lRQQ8EZ0XrBHxXz2BahBtIEgxUtmMM0Sc5RbI_R9znze8PefkOy0D1clUQ2ykfUOfFWkono3TJKhHwpX3TsHExYMEjjuIApCFQj5QLx3132Se21myG1Pkk6JJU2L6MeVfumT8gpa9LElCo-1qw3I3sflwC0ZN1kCAPa2ShV0HHR1UCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nx1upS7JiG_PySbCxtwpe_nAHCjNxxQ44hV20Gepui-Hgci8QUQmzaU1k70vbrD1Hu63iXdHAHA-BgQspQsON7HLIRq2MvcFtqIhZnezFuKK5-GsDJOVFqguOhzcKIBPH3Ow2XISkbultqNiUhnnvCfmnwOtFMkPKqCtSbwhJhugvFajohWaugDCc3OaQAsPdH-WwT700UBbOKdFq3FTsxr5wdy7-tnX8B0TCxPWR4yUjBVpWgFVLg4BARYoxDl4JAc8ud7_Lku6H3AxUYx4iMLp0NEen-AGRWIM8JD64YBvGdUjKCfL-BOsOaVXEPrBSr-reHZElk9BRd9r6EK6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV2-wMr1s_yaJig7OdifjcwLfQKqbEDj-nlSfbXZ6MEGd2RCEtrKl511wQ0a2o-aivQ88rRxwGwOk2K-a-CmzjwHzmqloyRepDgGShLvA26QfoUJc2dLgQiBllWf2k60gb40HNhbl2NQLqJmLG2b9JdryYUMEWVFQ37UH9R4tYgp59sflmetuaFF3JEV3m641OetnvXtoh0iEe3lUy6kaWTD3gOTWXy3DAYpnUkbWRtWK3KSZTavc1QNNPQAp_RNH7M8v5OtPk8cq9m55N00FidOwlNIb8jzHqzghQmy-6Pvg4Cz6Lrm5WOEA8N0JPizgpMoywkwvFnFBFPW23l6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7xmkVNF0xf_9w5eqF4rd_0FOEYptSclzGEHCu1ROvP2k9IYQyRz39x9xC5JGsB5-aY_dNqVphGcIgKTisBmz9LQ9JcSs0x_bGpsav2eiZ2tyCwrQh4W3CuWGmSL5B2ukPVxJowt6iCUGJs4dGF0HOL5H-IMfbFC2ccQOVpkaGT09n0Ffgdyv5y9EQjJbH70_4UUT29wgOsYbC0uIt5MOrk7VcOXktmWqxoZMOhrVk4Fvb03DG70yZHqFJCI7hq--Ctx4syyyYrj5ocuZ4k2tAey3JI1PKE494_538bUGFxnqAqDT4SdYoh3lToQsPcdOv8RsIZkKYnIlW2wzcPmHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlwFL1dIeSQlHthsSlOOMwlMrme_11EnUeHGMRmwF7hAXK3jlMZalj8ZBvzCKTC-B6DV8BTfLpSdyw5i0PA-h2QFKWYMebgXZAks6pI_gB34X1XsSZ_BH0VYHhG3QifGtKILkPmLBBKnsor6R9xtt-kayP8N_a3E7JnRuhBt5UqI0-Vw0NilpqwFMs4VMpO3jr5GlY8D9zl5RGYCNE5uvK3nHu_sGhb4XlTeYly0zg_U9ZqVwIKkaPRxZxXw0f38msrFU-PVu56E69_r_Jaxwbfus_iFv7OTWtLoFl5ZAf3nkgiY14-YdCVUtHX8gaxHxiU475U0vtj7z12c7JpLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4OciBwhyM6YGyvwZmGb08pXhGSSCRL7QPyaUCR-ci-dAlRI-hHlfn0reGfJOl_8OT21BHq2QYJ_W45sDzHPkjAckXhC81XUwIAh0J6Aap0k5rRvJB9aucJM128nV16DawA89MnJsUW0JyHVJXjmxYwk5Tu7ylxzDpxawyHFwYhEDVii91BTVwDI5zZHRWzt-RmqM_cb6fRM6cYJqba5iQMF5QYRbOGw3-Qu9uhiOyehcucu3S00SgERP1bvtf9lZYC9QSkNWjxfXZKb2Z26LKfk9jnlZvviuP3vVX9vA0Y5zvmUTwFIffgkDyc9LAIMWfUhDGh05nIiFKgMemG_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXxcaX9a2DH8qZjuSU7v2tX-Mi86aUNo65_DfFbVppbFWaR10zL1Z-nBpRCRzxFgMiGn9jv9GZ3vOqhUDR2fkrsvGuvJU7xZ0oxhO-N1xlY4XUVZtuUB1qvdZdEutvGDLLtzx27FhuIMjgGElVv0ARLHX5FpaN41RL_nYP0pRb92UaEG1eRZyUnKtj1OL05HmPd25sbLp_QCb2_AC0C94ZrFUjBlXl0DCkMGPhihGF8vQnjMuc1kB08G9t5oZIt5QMMaKsbSMDMG67lXTE8iBrdIqxFSjyhyfhuK14GQlWIDhkS3ttI8CgtuqmjF_BKVG5rcyde-SlY2t_skUkKESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwsybgjqPbTWjH9q6XNUHBxxEyq_Rp8i8HzQkRygXMsaB78mJr5h9wllBagBZISAGV3Uzug0BpX5njM8TA-HXbtW_huybvn50yRh6HAsj1ByKFwhA5Q-1tRm__F-SlYvPUD1kCetwl35Bwuzi0jMRYwrrxjo6XIEgSYIetwDCws6EZxPfPmStyAQpI7kyJjxkVoLg4bxnce8H1gYqxEc-AcpKOFfPiONh6Y-7VctzuHufmabfQg5jJoVl-mt9pHbaMXn8PRgFi4VijXAtZPSJEugYlQZaI2t9NrA5f0CPSEzCmT6YRtNGXLdh8bkRUV89k9myUWAgxecWnr1C94xMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsB1dUbcUZR1Fax-geMRkasbCxXc4H0Kclp1UClflQZxRPo9XUDAO092R4zarPHFlL9Buw2h00pX1Y4Se-tXHy_154JJQ0rsq0FYo6uamI2NH_xZ8WX8vpa8kIgXciwSnhgAIwqRSETPo7VyRHsgMrF7Je0yb0oD6ywJqfTudIfCV5r5ihIZ0fI-q9KcdVShQMT-7azyObRMhyH4Miwe5LljBINK09coKUxnkubG48RzXVKM6Kwcjf1bCeIAXob0_Z2IC2lyze50hKLMZl-IqQdi9IV4efCUe0KsKdWieoKOk-6A04fXgoI-iuwVsK6T5dAE_jSd15z4T_dSwT1JuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnce7y-ZdJ7Dv39aM6JIMgbypEOZ2xO2R5YUAB2iFLNI0wrq8yEy_AVqr6KeUkB0KSqYIDYeq80rH4haJEvhcffJ4cg-YkB3TnCMcB8qmRbFp8w6PmqG0xyinBgLjnH6SL8AE6EOcc8LI-hEeBDo23Pzwc7LUJ9L5Or3pl0XIHw24YSUfR53vvxEE0O_8Er_mPaA5FxmvxuX9Btx1EvVXlv3BsTUKIPOM74YEz7FuxpMtZijKDxKicQY6yE84NGQ9ZbFDkpYHQSj-dK6okpTcRkby5DwhZTTPXCRYKn495usUA9X_tm3sKl9Zo3X0cUadAJzuVNS0H0mLZT6LKCXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiki4OtDebDZK0y-Xl0zfON-LBI9Ix9GEj0eNxb8FLQj6q5PFZiktUebz05KliLauCBvBLaRB1wP-bzkdsSCDIGZs6XomrX11Ht5Eox3b6JzzzHdrv-_tOuQVAm6wlx-rOOog3oXEsfuxivlrkcTETvnqYeB5mfPq794Me6LdJ-ReVGbKajQXztxyPomwKfya7uj83OJ7tAJV8l-KTa8NWjFk7fzl3TARI9Pq-YZxkWxzGqXuuD_qARCoJGUZPHNppA1QazgIgQcvWIys-UYVSriN0vljKn1SuV_DLEVU5zi-o7NhzSfRFh5zOuAohdSC35P3V0h3MHM3qviL6d89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkiGR0ko0ARU0JkaJ_x7AoAF2taTeG5wZKsA9tyi_IObII_787s-G5KsBtcFQYLCv7UDxRIqeWuAdcRkxaRk99v3ePlfZb4Sisji-W_iMYTeHPyo6kmpGZdhFhBQt9HYaBsAs5eUCWpUMwgMbpA7mrmfzjLEyVw8rcxFVtEqT7257GQpAH4h0Y-ZByukn9N7V2bSZPE7e1hWGU2t-z7-Cy1Rf1TnZRKmKqhf4tpcNlamTdsa0jXjLiQYLW1UVw2UKhsAGGhXd8GLwRO_Bec_Zmo8a8XP8ln_qsyHV6jxx873AOkY26mPmr1DzVyyOVWPg8u42Mm7fBxKurJePActPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rACYcPSWluqpuU86SY5DkYA-JEYHlfSiVgNC39pI3nUUkLnPOIWDEjVaZSGmisGD8pTlmT7yH5_Wfm8D1_kq_uRaazoTcFP7P1KqvrXUd4v3-PhwoURixmTK2XZ5Jwi9WjKzhlfd__rkRseFyOCz2nc9F0ShcjxKRCHU8lIsqSnhDFf92IiuhPFkeQanLGgJ8oqWE_IVPUDxym9U8F5kzXz8lD4EbHpok0vgcXgiP0f9Z49Tiq0dQEd0yXOm2v6Xty-XMD5_421zGL7fazmXnAELR5K20P7hJVNsKyHMFlPEZ4TtKEe3QBKjbE4ad-KxLogdA7VQWiQL577Jd7KD8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wvgi5GEEOTiBF8qhyYKF1ejjmB8dfNRVYx4DeImvq_FnfbTAH6uhpKC76y7YygVRpUB7FjXl7SS_NBQR0sPo0y7DhFDBsi_LSU_-r4qp2cRRE7ihdBigQrosF05OIk5loRN_q7ZWltM1B-WVBSoremhkzE1X9rXExW0l12mlvCVAEkABbCLH8-WT0o1ysSCkNMoxbjF0BUKPKyLCsHpLSC_RtUxPGKtHR1Td0epFqTDPK7m9RwUn5qDSvVJy3Xc_GuvlgKMl9Eobw680M75A6u07-faJTnb37AYcFuHL64NFQMPxth4fMJsihhd8Uzcleb5fEg7uSafYGVdbEnz5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPB1SRXycY0iQ036D6wxr5WgTyUOY3GQ3MgxFFk9ZZSDNoEnUnJIy48TnLn1B_QAP58byfAI9Y5KDMkbyDHqtcXeoUUkuN8dmIgEDptdP0ZeTulyp-iDwphNm_75N3IQYot5Yc3_CXV0h1vrbULoTbQ0LQUccR_fDbMLYbW-SA61PsqXQZd7jkjQSn_uqUgSRFKTqD_RWfq3K-jCrbbeSMOhzL8DAvV_EfJdZUuyE3FOFnJaGF8Gsw6d0JCLvoWMQaesPWq8HBKGk7n2JFlxtAQtOyKGFyPYZzK8zvk_xuWTsslgfvs0nTjEcFU0i8_4zhdFSyYyR-zexQHYvNb51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8NAIjrpvgx4y5eavZ9I9AF8RybBdO8Mn7pPT8w-OMbRlaiC0B0s5zqZaQBczT72MU2QKvMFArPjI98Axu4OXQYTo0zlCJTVnAuuqcW_0GCnXvEC9g03Zm882jJ76N8S9aTMnF-GCTL4k3Y5G_GXXcYF_SDgxf84dqbj4TcN60cc_PuDB4c1LBf_LZXxHZpguCRhvzXCsRnOx_tKG3KJ2dZ5HD2w7unYYahYFlaLAcfap1JG6Wbp1qExeWpluGadOW6a3DVserK1yOUPPaCiBPHXE4U7tfDET7B3bgTAk63uHttEScXg8N7U7-WWFlsVXZ0cblN-FHNWR8M3DQNeFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCzqszOp93HeyqqnrGNRqE6pyECjaUuBOJALxMCb3A6xoy3mQzfrtEoi7frINoQFkvp4inmf11y7GnQJ5eEcb7BZJg8cCvPAVAPlKQF8S6RLzwPObMuzULXCABRAQYcctacoWnQ5XX2blpjDN2QfRes8DzetGx5ExSidnfxoMHfMjACAjrkhKcK6Mq2FKp8rX_WkELaisCdm966sl6dk0EsyoTdWhrxNvCHBGTvkCeFUyG3_skRGX5TNxrD3tf-6K7dsaoEBefTua1pgWuo0ElCPSgcbNTWaGdL6_ngP5gwAvbb1EScSlTTYYjneDJojhVqJOpvjaWKg0PVqXOHA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9RD6MOC3h9nL7GwQZLbRh36dll3Nn9Vy-xuKR4rq2h_5MCcxv-Em6LHNQu8Up5PpOVc1gIogkyGLwG7r0TgNICX04VdboLFvHCIulupsg4-xQc1h1V-Hf2UzFv51in2x-FeOh5RET2qE_XFCBIKf5tky1LF2ficcEGreotsq2jGF3G8emLGHm-TXVWOJqouKkHmepUaqDhIT1ICQBx1tOv4Jqio3kEyMqM7iff7gXp1_I9l2RXpcQpVe3B49A02G13AWVnua8SyTw7TcFvnSJQ-EAISAr_hkhYEUQTIjIyowfd88yTZsL8po98IxHJboIMNZK2Co96KKKeP-l9vMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0C-cM43jbxyd6l1-VCq_JYglZb503JM6JdG3sn4BBSfuPqGDMsJBSlD9snjdwxsraJzdUt3UOCbF4-3fIRKGl-14DMHpCaVvnZoKhyNWh-eJGw-NECmvTZ6_4OrQvMO44fPigebo3EmRpv1SQYz0jOm3A-SjHhrknkdJdN9jKdTMgD4-MP4Ai_LFeogkMZlYeqNXk0UvMmBd0IjKgVTJ75WFHzD3oNgaS0S-zXENg0FMmkNsOWPiYBJx9Yd0TYDJ0PrTmPh6DsgVBwG-R63AbVqNfP5mnELKQnb1jObXxiga2OGgwzovadiY6TfbtXL9eGdn5LsKlCpwjbtMEhcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh07L9xGsRIu2e0-2qZQXX0Im_nWaV_hSfZb-5QtllvB6RzghdQcTnuKot_OzkfGnZ5jJSaNdwemX7n4sOt9lxyVngrpmJtOoLI-qBbVSNjb1rENTjs0E33B_47hNKEvZdhr8HfhVWZHdoNuUnuZT5xohEZn7sqju85cv6gXkV3FjxWDhJYnL5QkiZ_M7YTp1qRdrt1Vie7QjI6ZlRDE63iqJ53u8PReGoKLqIY702mwiVpC06hw_N7aBwDwDkv-JDGWEGvYH1D_NDFyNw8zR0LoLVJu9PqlZuOub8oD1_LaGTbGX-QWUymDsnctS1sfI34BjiJVjtkvjRlFIt4-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW_Pc6uKvDQdXbdRperFHoKIURIP8Xo1--EGnAwGCSZAkG7fj9xGxaCwM6E0tlVLXuGvikjrc806HJ7lYHCf6b_MkHm56iP8Zk17E3q7LqN_4fkThbVG9Im154rdZO7f5cHZXws0cl4Yj6myrlmzcXnP6mQTHpjAPJf0l2xK26zhjm3A_YJN569Q5cgVWmg79H52F49JJQ_ysRUwS1uNyVWTjrDio2n46Y52xBZ_lmCc17WF0HWT005_d-fiLJweoyKxciGd0udIT7CvrsJeY36HUOM7jwjGWhcBNkeyi9Y9OaJyMiRQ4wHlTg_i3AyVpeK0ow9keX3E0gV3XQFFRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_Kn73k2uRsCXCob4D2KoiB0cnOZM_tv_Ld_nMdAu3FYExJvsYPs-gNMuMND1a_Ao8pDTN05eLQ9QItprFCZLCrycOJFuecRfYXwqmlG8jv33pV7hXxPA3a1AjcFrZEuhCdEBhEJrv1uz6aIwb4Cq50EUHDNKu3nJ_CrDVqiKSEyCnBlxdHaYF_wNFTbVfk4GTCI7Zp_uXJ_cHDBHSMa7kLgFN9sp1FSNmmdAgTpElTJ5R67cCIt3fITXZFVzy3iV3DZm_oGCa0NGUS6filGhrtN2AHPbTjnJxgLJWU94Lq_x0sWsAFuykGV-KaLA6bDJYML_HDg7k-fy92MwlOy9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggGAO4GTD82Mdcizs8_4fSr66XED1gQsJ1HNIdpHhysSlWj4Sc3lmPc1wTGJx0kw-Ak7OkiXoUTJiSQszx59U9OVIN3h0Z6PEC_1BruHBaRvuPJLOpzn04xkua5qZCZaOslJayyhV52mdmk58J5IELOOeBXBQ0vRkrtd1zvRqp7Tdm0LUON-UKXpUkG8iCEcJSkEguhzfQBtEgeHU77TMAvOjIp4ZmiLENY0Y3GGubKxYKqL31rO9fCK5yNm1A_gm3gPZHhFVFeUjF1gth7JXF8Xk9VS9n9WBc6Kh3t4-15uaUjz23_m6PsEQsxd-p8HXBEJy0kKZ5oYljYfih3XvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sr22eMsp2GzAvfjgcvXj5Zqoob61zAfzyH2r8r0dALmM0WWHarBgWE-EQNj8P8PALvaxVZdNNzKyCM1PUKAMSTCBdCxeoqNELAHJP6gvZFPn_QVv_PRd83wNwXIOgVsqAgqc9bnfU7HX4He7Ml8_uu9_KaxtMAtDQN6yNBjB4SsRGnMzTTPGq6YX9yX-KRp8gEtKtC2iitiSDmQ7vsgsFvEsNBbRONQ9xf4MWKKdWrSPTJTg2duOQ5HJPQJqwCUMHr0m1vxWvTVbNbywlJUMj1DRHmiHuz3Ud3wAaj9t-CNILDX1iuekC511-009-LiidS9Sz6yL7hUzoIRtK83gsA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=Y_r45ssUMVKAksp-bIRvv4pTZrZYshGkk0wnlfZW-LqvSeTaeWGYMna0_lyWrJycSltUyfcNJkcLZbF2j65V8n5xvZZBpV2dLfKCfK74k5mE9AIUGUZopxQUpVUDIAJnUV8y-09emKb4CCix4z8Vu7tkvL4gf83bgID6e-QK5jISdB4MG9MehEOc3PrH-5Qm1AkxZOwm0IrV_EYu_PlVWcId6ZQ1SZQblmAtU9cyGYZKh-g0xP2SPqlooSRSbw0Z2dwBwh20N8RMV9_f-VoZLXvu4p_oNor5ZASu2FoZqYPxgpjyW68IAhkg-H1fYtyjjh9ZKNCufrAAd4gUlbbIvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=Y_r45ssUMVKAksp-bIRvv4pTZrZYshGkk0wnlfZW-LqvSeTaeWGYMna0_lyWrJycSltUyfcNJkcLZbF2j65V8n5xvZZBpV2dLfKCfK74k5mE9AIUGUZopxQUpVUDIAJnUV8y-09emKb4CCix4z8Vu7tkvL4gf83bgID6e-QK5jISdB4MG9MehEOc3PrH-5Qm1AkxZOwm0IrV_EYu_PlVWcId6ZQ1SZQblmAtU9cyGYZKh-g0xP2SPqlooSRSbw0Z2dwBwh20N8RMV9_f-VoZLXvu4p_oNor5ZASu2FoZqYPxgpjyW68IAhkg-H1fYtyjjh9ZKNCufrAAd4gUlbbIvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ-GtbqI_GQeFk6c5SYyDixKX5iQofUqeEPFhtsr_ysJiIIV-po_6aiFZqkklOml5A3XIBH2qV3mvYME9wy6cfd-OCcQDcbkaw__UHL2-AG5jjt4b5QTjxHPCtVXExqlT4GkynkH1kZiHs8a4C8P07pBe4rXxY76PzaV8vp82Cq3B33MutrIK791-Y2cF2SNYMq8Rg-MWSn9DHV8CKMPPv1qV9lVUfi4vkl6sriByliuDVkRYnylD8sU_OYFDeDQVht0NbLMUoonxFyUNVdTLEa3XzB6b2VuGDLQ53DtND3_jF2N_-T_PSSV9bfkmamLkkI6rAK0b0m1cuzgiwSjeg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=S0BD0N6jGgJOYqbaGQaL7PUB7nd1X6j483fZdGWyBIt1IZTZuQnIG1G_xFh8sBOhEqGI3yEMMW1J2tY0T3ruq3kf1ryDOS5zEC6te7zI9Q01xqryiuC-PYWXThHMxSjUUWiIu9fJyEPF61ugB_L7VwOSY6RctH4kE-LpE7ZHdttZC63tawz3gqLiSmYZq7GVDqvbBBphGb1wuI0dGbuovVjMMTHQ6rgq68j3NsGrHGNYQRrJdbJRtQZ6W2wk_2pi06PLOoBOyJ52DU1IA9EWft0dX6wa4kiw1MvwgTjz0H5AJwhm1u5qy2J_vFC44DZ-7rjQxPc52xE1IBsUpSksww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=S0BD0N6jGgJOYqbaGQaL7PUB7nd1X6j483fZdGWyBIt1IZTZuQnIG1G_xFh8sBOhEqGI3yEMMW1J2tY0T3ruq3kf1ryDOS5zEC6te7zI9Q01xqryiuC-PYWXThHMxSjUUWiIu9fJyEPF61ugB_L7VwOSY6RctH4kE-LpE7ZHdttZC63tawz3gqLiSmYZq7GVDqvbBBphGb1wuI0dGbuovVjMMTHQ6rgq68j3NsGrHGNYQRrJdbJRtQZ6W2wk_2pi06PLOoBOyJ52DU1IA9EWft0dX6wa4kiw1MvwgTjz0H5AJwhm1u5qy2J_vFC44DZ-7rjQxPc52xE1IBsUpSksww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIBdRqi4-dDodsr6721PI5RrH_PGM2ZfueOX6LFg_ewGqrX6DjNCKSE6N3n2TmwOQ-Lfz4UXDp07T_vxn2d-LwH7OZJR45MPl9pV0VjkQbzIXFjeGOHmuMl3g59fzGv_dw_XI_6obSKZKYQY46W7artE4vBZFli2NN9dkSamJasmpkXEUt5Sw8MlKXGdFvH1L-2lAEAmJuUZIcn79rfJrAGaHYNnc9uf_qEES8FVfmjAEYzZT1qsnKSewsVBRAYMOeimrS4F_W7EbUp19i_vr0ZDhATYsOdoaQm-mW44_8gqBXJmBEyOIYP24uQGE3o2vlM-oMa6NLIzj4Ik4W8PpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBjrP8kaLUcq_ko7508bdt5BTELMTZ2cUtSPtJFxKvn8DNAH1M6gtF_oZovWP0byioDWZxz9wJmBihvD3FY6ycRFQWfAh7ZrjjpWQwwTyMG60NZPtE9RnUG58mFHIK9ZgA2I21JONt7Q3uTbprW_0_J1fJLdJ80utAyJ7xP9w2YC-4pL6EzZM7SYOCZCrxrzVj1PkInj9sqGdzMKKd1rfiEfE-r0Uml-jXEk7cQembSKaa5IHEqDTGAGee4qnDbTfBJ4KUvz8x7-zLEyN8ZOfNeYHhFsuYArcXubUv3YFocNF5JDEMeyvGnN3__Yfb2Lu_7a_Ki1-K-OmeIU-ceNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=We3Pmql4uQIUy1xyOqJ--MjAnUl38SXXm614Cp9-0uNcUmbdikCI8BQKIJx2iM1zhnGV34OJbE43WpPjpxbhJg_Jtuab7lVup22j699VXIV-ISRh9LwDTqgLKbdpqOfhi9yNZXeL2y89EGX0CHlsk8swnQp5RmDYMbEglKWvu7saOr5o2gJass2zWq6z7mLzBvHYGQZttTQrMw3U7yYy00EROOY5If2lGk-AgiBf6RTJAFCQ8n-GJsibEJ2JaY9V7cdwlzfjgJte8IdLyoIVeTP2ZdddHWjfcS4NK-axSr7q7NaoO7ECcPaPkDVf8AhwzS3ADlHJcOBXd8EmqknwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=We3Pmql4uQIUy1xyOqJ--MjAnUl38SXXm614Cp9-0uNcUmbdikCI8BQKIJx2iM1zhnGV34OJbE43WpPjpxbhJg_Jtuab7lVup22j699VXIV-ISRh9LwDTqgLKbdpqOfhi9yNZXeL2y89EGX0CHlsk8swnQp5RmDYMbEglKWvu7saOr5o2gJass2zWq6z7mLzBvHYGQZttTQrMw3U7yYy00EROOY5If2lGk-AgiBf6RTJAFCQ8n-GJsibEJ2JaY9V7cdwlzfjgJte8IdLyoIVeTP2ZdddHWjfcS4NK-axSr7q7NaoO7ECcPaPkDVf8AhwzS3ADlHJcOBXd8EmqknwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofO-soa1Dj_4aFSgYKG_jYYHuLOUC3e-mTwo9f31w9fK2fVlNtItDLivq22ZfZL0wL3MrbAWmdO2tPiwPkwqBv8f4FJEBCY6DGCbbfCv-hzmoTL9PVi75GHZUk0-eVysQaBRIaLGeaYpaD_tQ8B7WyyYle6RdD9iFC4XevLGWiHqIkSDjSr7KoHwJnt_maVmussRCdgUp-qA_fWmwH5Bp1mFWUna2gXGX0xAHNOHvH0I0NPX8PR4VtzOpB83JKyq6mRYQnVMbpQj7T3xIToul0lVnpnP6ZXmxWMscADW_mYN7ah6NKauoTA7cSCch5P-zlFHJfdK4yRo43DMmtEL1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_CurhENKJe3taHtguUjwQqi42PGja5LGrwxsUv1k9izax9S6DxJB80SkJJBijKtGyJaheaAm3Gh85b8_jQ3wamWYIFTK93F-w2lL-oOKEhHsKUJLb-uS_IMJk7FiNNftfJ9aafHou1HCe48uTIzPN0Z-P1YmA3nFdp8XvyV_ZjXhoO6y4UGLRpiX2L8cyqv6MCN6CNxvWMUKB3hp0vbGneqIOB7mVaYrjvUblE5hiLUIMSuIs2etVqw7oGB0jPn2ZN2p9uU0Mfrq2K6A23706cv6obF_477v1RQopmOjdhZ6hEVnQ1trD5g7-xo_XL4mdM4J-SuvvRTxRMxsrwN4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhd6FgtQ8Gs0dh6jAUEYaXw2YoDUDiXTSaqflOWiPUi9pktuedOxdf7dAYn_nJG5Y_Gj90rNnlzH2rzaGjPki63IhWM6GrELaqB3SKU_Wp8ac4G-F1HkjfZeN4zPY83qVG1irvD1zliAKVrX-qOBxvUaBC7MkQZ1ZriJgM6G45E3Wl5fM37-85bcz-TeJMM2LHFkE9C-6pOBiFlziTfmMy4PudmD6B43wV4NrRqKOyv1n-EoehoX_WVdSV7K2p3sqEjaUwEgyqfYf7I-agWV9EEhfLU7U5lXzFCDPdhWzd7SbRtB-yV0FuIb5rUpnrgk_Z5kZgkXR-akAEqxXpoAcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=cnbTUGibM27BR4txF5o6aNdTtlnR0MduwLIM4LnxTj-JL7djAvMHVod4AUHd6hSgyNLT5tvC26AtvOa2Ux7_OufXIkkDVG1dABb8uzwDklFCHpUwngRY1dSo_X9svzv-q8C1ek2xJMiYLSf5vWBRt6SvA7fyTRklge8OLKT6rLP4SDE770Fn7EtVf8-ggCi87YAKGowHgtAxe28npYo7gehx3lKgO0vQ1x43I6HXDnQWWhIw1-Lg9Wh8l0v_TbNo2aUMlN_V3h0KkeMFi1MBc_QmML-rgbyRkuGldP6sDvJNo3sNSoZ5gzb13-vfPBwSvGpnR83tr6hASrGO4SiFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=cnbTUGibM27BR4txF5o6aNdTtlnR0MduwLIM4LnxTj-JL7djAvMHVod4AUHd6hSgyNLT5tvC26AtvOa2Ux7_OufXIkkDVG1dABb8uzwDklFCHpUwngRY1dSo_X9svzv-q8C1ek2xJMiYLSf5vWBRt6SvA7fyTRklge8OLKT6rLP4SDE770Fn7EtVf8-ggCi87YAKGowHgtAxe28npYo7gehx3lKgO0vQ1x43I6HXDnQWWhIw1-Lg9Wh8l0v_TbNo2aUMlN_V3h0KkeMFi1MBc_QmML-rgbyRkuGldP6sDvJNo3sNSoZ5gzb13-vfPBwSvGpnR83tr6hASrGO4SiFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=q0EXIfmunQlHvFrpzB8kUvOZyI6AT6Jq1cXUFggMNdgIVzpt0YFxIxFpy0MKzQq_HaqkTfzZS6YJpw7GCDn3L4LjBqMB-1ztKfpp2mfjxhG2hRSEHly5jijQJk_b75zDn1gODTlaIOjS_q71c9oOVXhO8LT5rF0hYCxecVJ5WFtaqkmWL3fR0hgiSxfgmXqgu7pzM6V7jU_LcyYit-GN9ZeFbHrAP-uscBfaCN7GKrRArhQwCrHrM_Whej5gF8donqnXLZiLdY2QCwJ4x6dwSSbgcqCBqztykyeuJmQe7PInL_K43GrPrhtcSaJ3Ru-KyRB5ySgGPyUipGhWnojGdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=q0EXIfmunQlHvFrpzB8kUvOZyI6AT6Jq1cXUFggMNdgIVzpt0YFxIxFpy0MKzQq_HaqkTfzZS6YJpw7GCDn3L4LjBqMB-1ztKfpp2mfjxhG2hRSEHly5jijQJk_b75zDn1gODTlaIOjS_q71c9oOVXhO8LT5rF0hYCxecVJ5WFtaqkmWL3fR0hgiSxfgmXqgu7pzM6V7jU_LcyYit-GN9ZeFbHrAP-uscBfaCN7GKrRArhQwCrHrM_Whej5gF8donqnXLZiLdY2QCwJ4x6dwSSbgcqCBqztykyeuJmQe7PInL_K43GrPrhtcSaJ3Ru-KyRB5ySgGPyUipGhWnojGdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ6BY4GLQ4yKnBT6E3mQDNCjHoC2ULXXnIBRXpxy-ZlQ3dbP0v9OFJQfSOXNqmIxVlbJcUHfqQILFST98BnEgQTqyacatm2u5K4u_hyUUikOeaEYrFy6BjeRlokBQRhJMXMB_SwUYivzx1PSwxVSN5kcKclFxwpOYqhf6_LfMfpxgZVnIrHO-u_ZkkeF2B2QfTPsLSevs2aY2vTBin7gBQwKmQ1PPpx7xlxQVMh9QaUkABpTq42aWXgROMGWDiLOqMn_Y_wC-zmzqfGQH94mi3XtXZDML1F5h-6sdLawDXTd4LHdSXK537_ync1oYn3JoOQ3FoNQJIhH6yA_12iBKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_ISeZs6b8GhbHl78qnuxad1h7ikydxCadZd6cIjThT4GVccEfMHBU45KU0sdw_uGq90gMv_XQgif5BwlfheuTU7Y2K4KFm33y1d1EJsnIl9nC1Dj_oBf0Jzx3fGYqva0N2rotK69dsv15NhTpJtieIuOWhLwVEx1NnRJKUTsVUuGntJ0BS9VSg6AgIrToK5dmKnJ9kzVoOCSiDMnnQAJ0-a_9IY1ebXv06-BX4sr1Rs3e9SWDCrxBsBz3geieNCu4fYTMIfwV2NR6NEwdB743LPSnPpzzkoOl47eB_nLDwyo9YczmOxwlFy0S6c7l8J4zJgUlrHQHTCYEjmi5Vipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
