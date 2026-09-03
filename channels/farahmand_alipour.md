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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 03:54:12</div>
<hr>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsto6SnBp_pi60gd21bENs2IPfIOgAbWrPCJxtlRTSApICc1zggjF2Y7MByxAXnkx-u3Ys4YWQDZJEii0f_W4GiD1gIShvgzQqrWwBi_ppkRxeXGbGQQP-jXFv5gWZHppGrmiYpimg2XruhykZrDYNvPAzZVBxd2W0z3nvJ0a-8jnGD8QabSlnP-HtHnCAO_pT6EvWbCFCvh-3NqcoPUSOa7jIXbGe1oKXInunZLwy8XLj4giZKn8hlNaYB19MARHMygRn0Dwwxf8xXBucL7kyGhFuNHgRvp4ATh-7zPqXJJAuRhPhWIT3UiKMHVTkzY3h6ZSh-4AO2LFZl74ZP4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKpL8XcNjuSGgDo9_lu6V_4QskFWeO2xeOjdfxmlZ7AvsUIYfYrgIZn5EgiQSrnX-61crc0DH1W_2EpWnADkqjPatHdfTd0ilv6y7g0V4oLVrbZL5sGG5mQoLEqemhHTDOZtv5M8wvMcfFcLQdpBiY0DV0rxADtujt21oWItnQ21XV_53G1GoIfX_bKnzgNccChoj9-hriznKywmzdD2egGMoBAVAoyKV9jcI4um6iiBPjtp6C2Cxl6wK-smoeRQkEUANIUnTFKTcqPYqZirQK4ABXyAttHrhfJBO22h3z162Bg3yYaFOzqYaIDUYT7vhXl24TR1MX6mnLrv1ivvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmFcd86Chy_8xZWRI5DRyh1zFweCHRGeOVbAUrSflhmcVyZY86Gm8wtHam4CtEB6wjn40qPM6kzBrAngRlSFpgre1NfdFT90_UgAlAagNfQWxJ8IaQixcg3pCpxO5mCDyPKS79IXoPbaJVr_D0jJmUvayGC2FsHeKOoZy9a6XvoWYz_2PGh3MYbLcbQCKDKEXJiAo3PUOhE5jctFpgPqjDN46WgaaM5CQtzHCREGFjWP20SlO4lvy-bPSW6URFW4hIE4H5OL-OUEzghes6_nxfux1NHxfZvx8vXNnguMPwJe8N1oFKeDAnvtjjp5fzGL2Yuf_SCWtVz3WcQ7q-qqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M714M__idmOrh_9nZEqGJAciep9lVpqMRQzvBcmPqKirNQ16egO-sTpSKjpOV0T-8Jf35x6qmix0IKmnjNSUo2MtZ06SHLyXh4pqkFUanPs4zNKMacLlRUYrc86GIDe_jKpLdcfYRV1gAiObCHMWIoNVU2L9THTBpLipP8rKh-9g-haKTROJbsrQ0Y7Cv3qFlkRwUVXJyjuqmTln1P0GA8fC3NbHahi28d4WZE72FBfRLRIwlAOQfVhhietGAlrFMHv18kL3DOMRo2eydN_Yj0wT2rEAwJtmTJ9CcVLBhHtphDOELRDwQwDeoIAzE1NG18JsHIpngIs5fgcJ7dNNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=mGdwr7f3S_uxClEQQFEjIA_yViTWbcJeoTcajssyIBzKPX35kREVf9anxtoKaBKkL2eT6O8kwSeOCBOjiUWEk9B6y9cPGZ6_1N6tS9VwvK8K8oTZif1QCtmVYaf0ouy0l0WPkNNbprMHt7mBJmD1CY9u87nb4Y6poxh0mC1bfR99WdHZdSdZCi9LFmwdqoQEQc5JAINbMNh_QeM_cftQr0esVO4I31MkDz19IJaOtw9Qq6_ME0NLD1EXyemY_mLCcfIuDrjrK2FIIB5UYUzInOYGw0gcZQb0-Wh_7KiT9ZdAl_Z1eb7onzr-vi31HLwMVnIdWT3wz5DmaDQYZ3Nwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=mGdwr7f3S_uxClEQQFEjIA_yViTWbcJeoTcajssyIBzKPX35kREVf9anxtoKaBKkL2eT6O8kwSeOCBOjiUWEk9B6y9cPGZ6_1N6tS9VwvK8K8oTZif1QCtmVYaf0ouy0l0WPkNNbprMHt7mBJmD1CY9u87nb4Y6poxh0mC1bfR99WdHZdSdZCi9LFmwdqoQEQc5JAINbMNh_QeM_cftQr0esVO4I31MkDz19IJaOtw9Qq6_ME0NLD1EXyemY_mLCcfIuDrjrK2FIIB5UYUzInOYGw0gcZQb0-Wh_7KiT9ZdAl_Z1eb7onzr-vi31HLwMVnIdWT3wz5DmaDQYZ3Nwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMbTrJ1cxkKVtaWF1vAleUk00ZtLvk0Z9lLdesjnDJNCaO8OEkLzA2ZWybbgjgwQk02CFHooTqVVWsNewvci4b6GP0GfnFI8hYU6j_R9auI8oORe7-RZHcgGdaQcUhnEk-jHoH7w71CVjkCNOFQEWUmek5mnqykoiqD96Sl-JQ4UglR1p8CbX9CvhqY2_uOWrSiPCiV6g31M_-iOCwnWghCVFIbYDBYC9y3DIxDDwiXZE5oh1C1pDUspLmZCQiEFSSmiDRDOAWT-po5fcuqFGJn3sTqhZq7f-TZethkPVi7BoRS_zmpFeSetnHN5kla9o3OGQaWtTy0JqHuKUue6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmDjRaWue63TouEG_h3VRkHeRToos_ao4DABkBaHU9JON3q8lT3ozcHWijzjJJ3l4Z5NtpAMFL0dwSJiEZvuZfbmd1KHHhiHQ-8Vb7KaOk--XbalXM09Mq7JMtb8TiC23kNoIyXodbqNmr2U-kd4L_NVlzQ3tOM4Y_yzfZgzSJtLpWk4e2xB2YapC4BXHwiV_pgEa7ns0jDWfXiWaf4SR_0ksO9r5O6bJJ-aOGv4mjBwjgVYQfWR4e_bpnJuFAGhtfzrDGsDQTTpc6J5cxArb4D0-C7oZT0UMeEWPgTCpzZNGlJqCTcDSHJz3Y-34lFMuGsAf9U8ffip5tthHPWPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QLn6_Ht8IVjvvydoi7XDItHkATyjvXOsAZsDlebgN2qB3OD7r3oma9nEHwvIMYV3EEtDETfNSVaP-xMNI4SAOxIoDccoEZdaQiSVbv8VWVFKb8LQ3PX2pHetKhV6GIWOQSQM7y-tAnLz7ovchFLVxkdZslr_PFCjRaKECtAP0Ubt-OOD6N9fFevI2biGEne1hpA15Uhq7dW71QKyTyAHWWl2w3UzrR1RnYrOAtZPiHGQTlvdfC5u2e0q7PZPYh-WmJ18N4sQVW6csDIfTT9QBAq8pwMa6fQ5bqwDzyGPMOwY9V9-7k9g72UlKhoG9CVNK6LTg9pOLzl45UDoGIk6UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=QLn6_Ht8IVjvvydoi7XDItHkATyjvXOsAZsDlebgN2qB3OD7r3oma9nEHwvIMYV3EEtDETfNSVaP-xMNI4SAOxIoDccoEZdaQiSVbv8VWVFKb8LQ3PX2pHetKhV6GIWOQSQM7y-tAnLz7ovchFLVxkdZslr_PFCjRaKECtAP0Ubt-OOD6N9fFevI2biGEne1hpA15Uhq7dW71QKyTyAHWWl2w3UzrR1RnYrOAtZPiHGQTlvdfC5u2e0q7PZPYh-WmJ18N4sQVW6csDIfTT9QBAq8pwMa6fQ5bqwDzyGPMOwY9V9-7k9g72UlKhoG9CVNK6LTg9pOLzl45UDoGIk6UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=M7dq1IOIkB9-r6EWn_Nxbt9_pn0r6D0qZ9_S0IiQQDfDZicwk7osQ1esCVk5oQFGtWHO5NmW62u8UHMM5QdjF4znUpXIvWS5hML_IAwgU71dfV3G_j4Zi9h7NyAyxyRzSwiq0K_53nU7vnDAYYIu40LQVTRiNkjcXufUD0gcrn9Z-R3Cf7h5yd3vES4yneYvA6wLz2GMUxyzX1V7TQEkebdr62B4gxcq7YKNuPazXlAkVp19-9eiW7Pqrzl35ZbUP0_YjS6jfohklm8i0lKjLJzZRZS9PoKNcfS-Wa_jWZeLlCrZAMCRpFYU0gsPXFaQPHYh_BNdmKQcAF6D-BN8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=M7dq1IOIkB9-r6EWn_Nxbt9_pn0r6D0qZ9_S0IiQQDfDZicwk7osQ1esCVk5oQFGtWHO5NmW62u8UHMM5QdjF4znUpXIvWS5hML_IAwgU71dfV3G_j4Zi9h7NyAyxyRzSwiq0K_53nU7vnDAYYIu40LQVTRiNkjcXufUD0gcrn9Z-R3Cf7h5yd3vES4yneYvA6wLz2GMUxyzX1V7TQEkebdr62B4gxcq7YKNuPazXlAkVp19-9eiW7Pqrzl35ZbUP0_YjS6jfohklm8i0lKjLJzZRZS9PoKNcfS-Wa_jWZeLlCrZAMCRpFYU0gsPXFaQPHYh_BNdmKQcAF6D-BN8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVm5EcuMcpvEQwSFXzlqlapTNi0_RekW-YU-bp6B5M-7nHYLvV2Hr5qRkVAGhQPi-yleg8omu88Q6cCORmGBckGOygLofqUthmaKa8R0ckX3SuYEt8S6Z0U0TrbtRev4WN0Bw-TVQJvCwXcMgYayHqDSATH6UNOR-7pw4J5hOpNA2k3up5eRc2WL219B5GIJpnPmhMjjgaSVjUXlYwUw3V3Gz_Hr3spQzIGGkr-srn8l77CUf9C8z747cgf-aTSc2J6_Kgx8K04kyjYtJM-glYMSVznfYU7mT1aKuyo-Wn1FkpcfU3Qn8wvl906caoi-mVjZmZ80SgYjZaOsJT19Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azk7kjbX-yT8hksaPKomzhWQ63EH0VF8uyn_MvZjBIXt8aT7Rt_5pSpoP89uJrfVdH7XiZQIwV9Qqej6QLsmkTVIlmiw16NDTEFX0ZWvo-fROv50A4X73BYYZbii3Yl0aruQty5wpRwpDL5hyacHAtjp4D1-_t4-fLLaDxi3aBCJxxWMvG6HMLqxi7kfweiXr8-iwyLA3Tmlc9XYcgQF-MN-TSNmHou9swlt_fkXtcLWj0uoAkya2Tzbskxr_F2WDGG8Kr5-PUr3PKVKS8XRH5vCJOQt8e9s2ZWIM5GlO818ls1MUL5GSkkkS4UUjoMurDz0DGtN3jWH21M_9TYR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yeci91ppnF4TPmQhO3vyNs5gD1qnRmtVTBF7i1oxgYgtyQkzndS3DyWPN76NLyvBB9r2kxsazuNIGfapYosNPrlPeGTTzyFY8r7HsCI4rsM2dISXm__sDBOvf0pRNWyYbg65Bunhengq6gW5txsxF7_CjQqiKwjLROzSnOBSjzPtemXbHt55nbXFadMxNbB8GZZkMGlLRdE5ii5r85lo80GhkftL_CvyMTu3llrNDwlkMFBfeWGdsgYnghtR8HebwhH4-r9bUlXNi0HlniDhhkI8JLTiTR9iSVc5lLPxi5VGkOJ1ejid6s7qpd8qGZG14ncPSKEm5WATP_cUCv22jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOWk0E5DaJd0RqEV0V90INSAKVsbhVn5X3whKXgHG1sL271XOOcTaw4B6lT96R2ppbT6cdStkfczsY-9vr25RF4OTvN_g8vXqhS90UhEluZorWRVJeMuWQ_e6BKjP_mCMgsrhyqmKoAd2ndQut3F_OjXEXE9Oe033uImPhmalR2Y_PbJytOZZ2rjYOpSNI_c538HlrVtb2WuDfWj1Pvebhid_v8cVLacguht40GJy3HkYnx4_sidGHcV_4Lk5Fq9gyh8C2YWv1gW6c3II0W_DYw1wr_F7AmV8oc9bowytKQXS-foROkxBt_smuK_znt-s9rNnN46vrOCISXs8Yr-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilPzZLPc9gjP01BN8mqq8gFZX45UkY95ysDhp_ZK6I8xxplkOnP6oQ1p_xqtaZ7lUMPEKiWHsn5w3cP7FrPEyuXMyz-HsdCjdyR-hu9zeLI40ECKlI1btmTV_ikpwqtPXDKNjCqqOvZux8jpkr978FqSCAxUCkEXOxW_rIW2d16s1yBIoDmU83xrqVgIxarIpylWdNpEGX7OZ8tvYOu0zwBmpD-pZz9oHmAilxSlKS0LbJr6y7mLi727X5uCx9QIIGLRjNRIdERHSvX4bXyEMa2POVXT-7MUK_dipHqgYht8_gsSwoq7RuG-_TJL7zV1m7J4WryVUO_tvHOPjU7N8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKaOqxznTBN5VoHULiXsDe5Qc9obdZ2YkSsJpBZuEzGTod4uHW8gw110ILXXzqOlzRdtZe3BXgD6CI-9S6mysiSlZKRt_aeWDaErEJ1htwJoS4XgiSDeS7tb-SHLUtlgwQPOg7wOtvCyJPUIeln2N39bO9sPACdKU4w7hAnIbTnSulWxUZ6RsW2GUDLyQ4xXuTkCcx29tzbk3UUM2yadGImb6rgP-TgHPVPMwI_IFFUvmJPd-PFPyRJvV2tMuq5xFd6LHzgTXVvstH2W6U-_Cb9hvaiQgK0GBHihDByyjU7bilIkzwhLewXyjILwTTOMndenTbm3PbUfhWCPa8StSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAmp586iUuJbK3VXyBeHshc9HPt85o8_oJW-dQvj2ymcb4IpkjTJItzvTBue5M6U8Chup7s7x9OUbgAPkRybDWvoJuTgq5carxrCYMZkOlSSCrKTawuzZJJjYelotxkVLSe44n32UnrW-2y0Svw77LKBMKsQHXyT6Etk-g1BQ8iMNkiF1icdHrDQCkdp3sedTBiOZ1LZ8zYnNBOYaTbFwhflX3RTMQk04NiWo6n0Z3CjEXtvsdFkN_2flIwK676VJnkmvjUO1rWlnFzFDuoHw5J2AoR-mhr1FniwTYfuc-6K9gOastjFnA5TlhntlRL5Sz9I4hf5Q-sgAkzUi9X7FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfEp9sfFtBNOcJVADTPfMQOkjms7AZ0qH5Zy3X2hX74w_AU0k_mNoOJ74vAmmajuCDJkTH-90ayVSET-c65PDPkX0qt4ocH7m_G2i93VDax3YK4DqG_td-80wz3e1f3iU6HdnZ9R_QtZekRpPrFVAqMKWuvVQDml7I9Wx5MNSxuqUyiD991JrQjtg0WZAzEnJLidqcfegqqS82d32V66odFqpYxXFUz_-Julyi2n4grcqprrtQBVVFKXTXxtviHlxT4l6f6uK9VnR5BGVrf-JlfqilnMd3sPmBo6FzktlymWaRJ-Cr_zgjYtbXs1lSYQc3jmuxV7L8P4Nr6juB7-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=GlN4WUvV0d-2X-nfRFLhtw5hSVi7r0m5V2ptX54Rh_kLkd_T8vS9IG83cqkiFTAcNx1ZZQPIqtwAiysX8OWqO9HPYKq_HxQlNV5hg-uYzxzcYX_PJQvYhEvfxUTM9hYD0RBULqWjANOw0ED-zUhLNkqP8kXNSONVtVuhgx87CL7B4IaQlz7FwzQxLadxajWOz8yjG4msrrfdWJzoZAyxgjkTPedZeAA2g0CSRcTMhU1MAoSL28UaS6HPW9Rk6gcT2hiEet7sgCF9j2TxIz0YC-AtwoEA-D_uR3bxNFO9LUmeep2S15UEq6Y28k3E-3MA04Rk7tmnjSECzYHH2tUN8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=GlN4WUvV0d-2X-nfRFLhtw5hSVi7r0m5V2ptX54Rh_kLkd_T8vS9IG83cqkiFTAcNx1ZZQPIqtwAiysX8OWqO9HPYKq_HxQlNV5hg-uYzxzcYX_PJQvYhEvfxUTM9hYD0RBULqWjANOw0ED-zUhLNkqP8kXNSONVtVuhgx87CL7B4IaQlz7FwzQxLadxajWOz8yjG4msrrfdWJzoZAyxgjkTPedZeAA2g0CSRcTMhU1MAoSL28UaS6HPW9Rk6gcT2hiEet7sgCF9j2TxIz0YC-AtwoEA-D_uR3bxNFO9LUmeep2S15UEq6Y28k3E-3MA04Rk7tmnjSECzYHH2tUN8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwORZlFXvpZssn_PYXp1-CXpMX8p68RZ6zBYsPNdVi7nVBkiCnp4Uv7UqesV1ciwCzAIph0F5rkwTHKdsDsQxpOI9YhX_KmCEdGpnB1aLaYjxyCcItE9JL7j6Mnec_flnC8IlQAfKLqNvImmQOCLhT1rYTyhR1QZshz0VFsY9dWvGZex7a1QTnOjS0cGoZpGttd9dRsNKnnmob1l6ujjNNLPd0ZlTDXzbIBX-R7FIDm2pd2vRJ9C5UIddlODLkOP-bvxHOWSn4MHb2eJ5y0ZuUR5gah0Of88k8uhjA9ir3EGH_sEgDNH7V2Y2-SP92F5356HSmsj1k_SbD6sfXrpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=gqR7DkjoNMuuvfQhNMDRW3hT8Q2U_88-5Tf8UayL8w57Cdy3JLDqA0fbw4DdfohE3AlYarzRJ5VFcm745-LAxJzxAoPJJEUo8FyswkVvHb3BpRrVV32YChzKCClAF6PKRR4x0nup0M4oIBowTD8laH_e0yBPdPx6P1fIPnCpGF47DSVTAS33hzA4mQwgaxrklq1E4722LPjTIUM1e91MUIvcdWWmhZj-NJ0iITNmZLKeFs9pkQcvNY6EeJ3DmBD2KctsCUQtLe3Ih5B5fyl1k1-EBqBdcWQy7mCyWxXn_j6Y3k8OmguWF976vJdkaz1tEEieuKUV8-ht7iFOWq3UTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=gqR7DkjoNMuuvfQhNMDRW3hT8Q2U_88-5Tf8UayL8w57Cdy3JLDqA0fbw4DdfohE3AlYarzRJ5VFcm745-LAxJzxAoPJJEUo8FyswkVvHb3BpRrVV32YChzKCClAF6PKRR4x0nup0M4oIBowTD8laH_e0yBPdPx6P1fIPnCpGF47DSVTAS33hzA4mQwgaxrklq1E4722LPjTIUM1e91MUIvcdWWmhZj-NJ0iITNmZLKeFs9pkQcvNY6EeJ3DmBD2KctsCUQtLe3Ih5B5fyl1k1-EBqBdcWQy7mCyWxXn_j6Y3k8OmguWF976vJdkaz1tEEieuKUV8-ht7iFOWq3UTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=ESyYJCT9qii-_ssu9pzpDHc7-w9f1v0yT_kYErrbzOcEOjfpWm9GJKpxBu88wzh0D4T52nF6-xSy2N-bgkFbrGk8DaJbdqsdeXKBNyGV8e298UfPEZpGkquwTKSeyCPqgSWtxJKiVlxrVgRb6EatbclBpAa96LyQAWWWlsO9taiJn_ZS1qAbA02XUMJSFQXdUN02ZoEXds2H_0IkqIoT8xaQSFY8DwBFAz0s8FaZ2tbr3yZEhvodIVnRSDNdJv9Y5trVlwyzxfZ0Jbyfg7KQVi2AfH0jc3gqFz_A7oNsSbPfUOVEdGgtO1CQcw5DWK745Ao2KSrzclgAPmno4k6PVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=ESyYJCT9qii-_ssu9pzpDHc7-w9f1v0yT_kYErrbzOcEOjfpWm9GJKpxBu88wzh0D4T52nF6-xSy2N-bgkFbrGk8DaJbdqsdeXKBNyGV8e298UfPEZpGkquwTKSeyCPqgSWtxJKiVlxrVgRb6EatbclBpAa96LyQAWWWlsO9taiJn_ZS1qAbA02XUMJSFQXdUN02ZoEXds2H_0IkqIoT8xaQSFY8DwBFAz0s8FaZ2tbr3yZEhvodIVnRSDNdJv9Y5trVlwyzxfZ0Jbyfg7KQVi2AfH0jc3gqFz_A7oNsSbPfUOVEdGgtO1CQcw5DWK745Ao2KSrzclgAPmno4k6PVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ny1_FFttN2VMxCxFw4oj3QtYvc2MXh7tNSTAHZZOh80mOVdcs6mJ7LEnphAfOxoa7B-4DGDUmJo4jE3B_aiN3uEkDF5bsbKRhs8-gk4NknB6V8YbmC_uj7GlzHioczqR6235qNwJ7oplv4s--Zl5-qu-ghCKgUHKU6lv7Qx_qELb4S2QA6UbV2J0oi7UBT4s1gqMgp8bhXMopjT1u1BRVryhpI08jsznlmB8a42riU-8Dy4EbU-jXTjER25jwq43uTtwyXm4Z2sD1Ib8ICcYJCyLk8FHZAvHQ5xgmQOM4HMUbLInvwjnWwTfRLyeLuX_a5ZiN3PiYw5axW5eYFFVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXzFmZT8rljQEYuZaSKv44S4CUOThDBFEOwWz0bIuvz0QnQ6GTii3v7D4ULX-UbErSMOqzM9DCWx_rgWelPhJWOp8rGEY4Q_5kSamyqSJdEvXcTmK5Xx0KB8xQLmmN431GYxq_VSggnFZvttdef4_r9ne2TjFr70WCEVSjKYIVo4nZNE9IO8k3W0QZsAyT1hOMc_NRp3SsvKdptvgb8YNQMS0a_N-zM9pus8A0cxN3jasBTHKHjC8FLpJp4rkwG7ZgmYfa8_E4RExPBgtBB5dLw6alD41o1Fm9jHnorLOLNXz6jjXGqwCxSFHUd6ThNVGdmjkGTP179-AjwvXEcfeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=UJQrQSHwo19YmLb7_1nxhKPLhVvSjNkVz6ae4ecxNaqhovhsYIv6JbTWBqu9Fh87ccecVlAnLTfkrLvCg3WdlZJywbFoGiDTtWWKQSS48uwCp6VjoqsxPqapsrAxn9Jco7TXBoaNQCYbXHuIJyht7hdJqhY06c1DZhszloTeBv11Tm7ZIpOxKlT6m_0JJECAhtyKdA8BG0Q7mRJGup_j5yvWHCW_UdorT7wnS3bdNubMHI29u02oAX00UIvTDxmFLrDGBfIH86Bzd8lUUDO204Z-NMwKtZq-ckGt30WFw4DrXPAQY34bCw6Z7aFvQ1kxbYCNH46cJ23ad4oxqXYeChAY6bAuHkPKXwqBjx4Po-4wOGR7KBa0gwOSNPbw_PPQdMscC4MzRsWyo3p5xiQm6R16u_DjmyNtIfn7dIW5hHA0GajXJsxIs221ixyECCTDGSnmMQPb0s-kt6UsyOzLlOD2saOqdTPckJslQLl9N9okMZoR5O8ok4SVf6gbYRdW90GdViBOTYZ9aC819DH1oPgTeQhjlAJKp7CLk4BWaFD14d_piVlBGNn0GIZo0KcbUNkqFQXVlNPWkLmW4oLv54ABSXDomcf-y_3VXH4RFO4Zy8ON6ZrGULKXJuBLfV_CxJ1ubz2V04HwbncAPYtwPqOU2mnKAwsF5gbNurNt_18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=UJQrQSHwo19YmLb7_1nxhKPLhVvSjNkVz6ae4ecxNaqhovhsYIv6JbTWBqu9Fh87ccecVlAnLTfkrLvCg3WdlZJywbFoGiDTtWWKQSS48uwCp6VjoqsxPqapsrAxn9Jco7TXBoaNQCYbXHuIJyht7hdJqhY06c1DZhszloTeBv11Tm7ZIpOxKlT6m_0JJECAhtyKdA8BG0Q7mRJGup_j5yvWHCW_UdorT7wnS3bdNubMHI29u02oAX00UIvTDxmFLrDGBfIH86Bzd8lUUDO204Z-NMwKtZq-ckGt30WFw4DrXPAQY34bCw6Z7aFvQ1kxbYCNH46cJ23ad4oxqXYeChAY6bAuHkPKXwqBjx4Po-4wOGR7KBa0gwOSNPbw_PPQdMscC4MzRsWyo3p5xiQm6R16u_DjmyNtIfn7dIW5hHA0GajXJsxIs221ixyECCTDGSnmMQPb0s-kt6UsyOzLlOD2saOqdTPckJslQLl9N9okMZoR5O8ok4SVf6gbYRdW90GdViBOTYZ9aC819DH1oPgTeQhjlAJKp7CLk4BWaFD14d_piVlBGNn0GIZo0KcbUNkqFQXVlNPWkLmW4oLv54ABSXDomcf-y_3VXH4RFO4Zy8ON6ZrGULKXJuBLfV_CxJ1ubz2V04HwbncAPYtwPqOU2mnKAwsF5gbNurNt_18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVDqGX6jYxvM0aqbfmAf8wyWWgH5BapjMTSGajFPjpepUJGzB53ua9fJkaQMzqY_hN8TaVK8xTZBl5NyVU67TZqmF4iumHnjUyry6Ve-ZXpvlW2egg1yqS2dD4R9HAU_6sdVAh3GBLlha2A7GkosqEMYY1QkkQTAPdBMgY-tCKkv-0nSCi9wtnUMzYSr2Drygo2IPekk64gLTQopeiB283Ee7aYk0oqus6Iz-tvpLDT-LHzXMCVgpaFAIDDeZ0eu66MXbgnFS2qsgNX6mxidJyFCo_TUM5qJukYxr3xwf8H0wAApuFpSwEPF9KyzC3r2DlMyRzVKvmuEUfEN0xI6sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=VKaqKElihbw5G47QTT4CVhU6gnfZNIYzYeA-ao6BEVqNcydprccx9Uv46LQ0lo6G8JlDyLljVbbp6zAEiXA1AT4HgUsROLavFN3ACMzW_M51nrtXMLz4fP80CumOM_Zk_5BWF2wXT4J6Vjibe4fLNaEpfzbwSr5VG0ip7CvdmRHFX0voVgoacurqGRNphnvNLYzp8OFqoYHm0M2N0giV17EDJSr_nw6sq9EoNa03SFwUWVhXbcY13w3n2sqDVuaQggneS0HNJrzHkXx-5AGUmLoWZrcoDIlJgabeHBnvtQPioNt3kllIlaj-mCSTgQkmYKTpKSbjB6lfR2yW_OKZyY75bXYl4X7XPiZkRZIdwQSASjjrt0HZwQ6xgkDzuP8t_aSIZ2-nt4PbK6sGmc77MOCb0JpotU4LfgYkZzyPBcQBu8CNsOVO2swLKGFDUfBIkp8OFQVAFnTfnGe-Du0PwVWJDCzyXZcKrBmhUMrh7dFs_ENM9KQHyihN_evwvkd15P4bCBdh5QMhJGed90NQGC6xB7cH8ixEKWMbd8cfMcMFY5W_ti2PDWXZF55H3OqWokX6vDpg0EALofYYcXnRddaDDAReAi-OA-faYu92HCkZ1RG1QVS61yQkgC7ZFk_DCirNuFVbL30U9OMenXmgAjnuJty4s8N1PPAyFb0-sLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=VKaqKElihbw5G47QTT4CVhU6gnfZNIYzYeA-ao6BEVqNcydprccx9Uv46LQ0lo6G8JlDyLljVbbp6zAEiXA1AT4HgUsROLavFN3ACMzW_M51nrtXMLz4fP80CumOM_Zk_5BWF2wXT4J6Vjibe4fLNaEpfzbwSr5VG0ip7CvdmRHFX0voVgoacurqGRNphnvNLYzp8OFqoYHm0M2N0giV17EDJSr_nw6sq9EoNa03SFwUWVhXbcY13w3n2sqDVuaQggneS0HNJrzHkXx-5AGUmLoWZrcoDIlJgabeHBnvtQPioNt3kllIlaj-mCSTgQkmYKTpKSbjB6lfR2yW_OKZyY75bXYl4X7XPiZkRZIdwQSASjjrt0HZwQ6xgkDzuP8t_aSIZ2-nt4PbK6sGmc77MOCb0JpotU4LfgYkZzyPBcQBu8CNsOVO2swLKGFDUfBIkp8OFQVAFnTfnGe-Du0PwVWJDCzyXZcKrBmhUMrh7dFs_ENM9KQHyihN_evwvkd15P4bCBdh5QMhJGed90NQGC6xB7cH8ixEKWMbd8cfMcMFY5W_ti2PDWXZF55H3OqWokX6vDpg0EALofYYcXnRddaDDAReAi-OA-faYu92HCkZ1RG1QVS61yQkgC7ZFk_DCirNuFVbL30U9OMenXmgAjnuJty4s8N1PPAyFb0-sLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfDQeoOtGm2DPcqicY89VDG-LUDZcNQmHR95sQCi_2PChWA9ypPWOVgSzAIQGlpzhXL0EXmFSVKHYVxPL6B1JioCxdGfZlIaEsAfGvzuIW2qrIyzqbCPDqRD1LIXmLvDRqtl7rMMnavXvmbJBw3_OruA1DNlMeR-Op8Yh1GajEBzA2SEXgE82VZamiCNmphs2_6ro9fXs5KzXjpBaUF_ag6A3VHtLiIzsnT45Bc4cLAE9YWZX0ZFMPEFDKebgh_FHcJGLdedfzoeUfww4o7YT344WgqeIeM5Cvi0fA4CAKvgjHe1N1eujLG3QZ18-XyOByzB85obvB_m3UFo9RP-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4DM8hDkaeeFL85Babh4HdngkXRa0-Yw29mrsuyZYh6mSJOfV0dAWViOXVa1YX09caYehXfPMVaDG-FYNQOErxSu33c5j3oyGZZlJwZGzI7rBykp2mROzKoxIalVTDsF86yTrCR4YHo9wiZIAng6PjcgjxYrK-9c85qc_n5IxXEM1iUC8feipeaAIC-mR2uAEFA497ntCtLU3bFbd_XnpAzZt_HfEpuAVFllLBRIjjZW5q3EiwWRX_AYeKLNVEBvTOXxisakC7GZeZped93dtxuBmzqZWNI3c0YHEzksVL57b3ffjlByW9wozNibeAJeL-FNnTkItmFX-A8mcUqzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Txat2x_2BGsDvfH94Sd-EXajIj0TJgXbhvDOy8Xr5yeFUgl9L597Y6JRtNmfkc-FkFN26aT8x9h5PYVIg9YFtJsz3KVzpgnKTXDjxexHgYB6xG0I96X1cldgVuPPv3xhwV9W2_oo-f2-d11fZ4mQ9OrBFtukw6YO07g5mINF1J3qES4jX489TyV1J1sKTJuyjQmxDMwAPVd8D2olLTuQnxqOjgtP3MU3ac6K5zahyzlLUactkkAmN68rgExQ3S882T1EquMpQJTzGekNv85zSwEjHfHDfPTJCEGbJ5FTxHZ-DcVEdOBNPMINUFdnaqvskS202R6C_pmF463UMRidMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUUTrjUbrdItTfSGzOYy9BaR9JX5Kw7DMdhbLMU4tUVVJmOfnSCVYPw0iKuw0Hben44PB6jgd0zjw8kAcggVRrWwitM7uozg7ZDpZYzmifaLWE4xiZVGNEM_wYE3VQgLUWsb3V785VhYXbVL72ct4cDYR_WXwd5VM1jaWEw8pa5pklcYaBfBu-zBNhYXAxV5t4x8X1Oyb8wJmjH685vysfvgWEaLbg-KwpcEz7bljggUzQFPl0yKIuLianQV2Qsz0o9h25rKYUx3Y_ZcfHyNNqmyZZUjcBR7bf_XC_vJRK2437VWSaMzeJuAbighT17PdWqOS83dT4sqdq1FR27QCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgqbFrPwf7-qr3blTVpVrYFQpJ29SiHQny-k8VHh1dA0JvOdf4xW-jSHVDpM9oxzuuAi1INvY2fpyFSxdAokjF9ZrYwGpikj7dHdTyCFT9d0Vk4ncizhAWoDLlNX0FUX3jsVtHJApzSrFw5mu_OUNWFzE7ydC2vKbW0ImHxVbGG3ISL8lEZ6AGpAZ_WfP9NKr6THK1syKRgj83cV7nI_u7YblFofIZyJUAd-ZE3j2grDt_qq2qS-J8ehglSLDcubkxmydrGd5UlL8TuBNZaIzWz31LHtk42DWN4kD8qF6dbHSgxVVp_3N9HNA6XcF3yXqzbdmuodpv_cRwz9xAJG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx7cD6AkjnidbJ1XolAilMnSeLr98m8dVUXPqJPpC5ZdVXama9jc_x_Tyd6yKFUEczSSONlRzZvhGDMuE02Ie9MFkhJIADb32TUc0Q0yFVwIa9yx_SCkrZSr3Jzc3-lJWTfdFO8LE9u4tGZaXOeM9C0GsV3Sod2ErVwcGQ43DfrO0CtfkThsnDMUBgEbRienSpSmnTM8EOAm1bP6hcrIZpqGxjUf8Hwjx0q-Di5hJLv0BIkwXiUmSamNhhkC77mJuFf6121grbsAKA6e6WvyKU6xU7Xv1Myv5VVpgCtujW76tx9_c81UwNrq2P0zVaEQr2wLtFqCfqRubwkJbelA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXavhKqa73HFFX-KAN8cLw4ItrWWcZY9NFI8Po_RRh3YTxxnZtYVajQMXnclVJ_ULcrRgVTWLs--pXV5ShSlK_kXFiJPpQF7uLUX8eN3RoXrBv_I8VznbGiJPYV7_ib71tAwmpkQD4MnxDTHkct14XxNjSH25bE5T35ID51pMYMpER7K7y6aWTGEJyXsUG3fDBaV-Nsqb57jQ1LUzTcgC7Bk12g-tBK2peQIMN7ODEwXS4TFmgBJq9AgHQq2UxNr4ZD4WZCw9G3NHDYl_VB-GDyieqAla9aZAHoGaQ8QaDFqwXqPaoYV_eHaSXAKP6uC7EKHC5XrxqY0U8wxSpDVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbOZMlCG0grf0uazdTi1gCZva6GiVZ4T0x2xThad8c2NPyrTYuTzbaL_t6mkzccGfDIxZPiAv6PBB98XzyQ9KiMNVc06WNdaQVwfjazJP_N78sKUv_hfbp21tBPFFUY9zjiG3xaR4XvHloFDHR5f97RqsbnyEcS5i5C3hIRC_2G1W0JSrU_ZrY0VWuff32i6BjxM4BRLIohKBX-ZQXOFVUdN5ZFsGRjCaQxvA-QF4-khoiRosNIk2Yzc3ZA9RsQ0hpMLVMAmYF6XdJ-wlcVYN-doKM_aJNdTfV8tV__CCR1_7z-PdScW0zIwyNFeTNkmSFMhurLvx1qlNTHb44mU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7IikIK3EFVH-oAnnZ2mSS3KGYD5-X3ZXgY5_AGrF0OenrCjt9J1DZDyTDT8TTUWoqXtawwKjZHMH345oYku_kPC4sgs4owRNBoSM7wQ5DLwsZBcQnx55dYD--Rw1hYb_DXLa1Pa6veFnTCuHTyNiIsxsFl-bhaASkyYMBpvea3hmpqusbm0YC15_1T1Osmw898ez3fplJrCuYN7NMNJrdJoMC6fJXGKeoHQ0_tKul6-HLyMUy0Aui3oOcKq3U_h2XtGU9ZrSXTiVD6o9k0TpG_hlhJ8GlqHyJ_U9CkzljURAKESQezoE69fXsMuc4ME7UmMaxRtGSLL_LUSNOigyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcSGCBXg4IfFte9RSJ7mgSgiJZXjRolhcImarbsmV-mfP631M2oM9NpRTdr3EHwgoQUqBiZABUwnrtkeSAjBeQRGmJdOzr8IhjeJS4xRx7Oa08mDFh7FSKO1_6pUWgTuwy8TJ78RKDpB01FdMMV5g8X5SAkoWx3mNMF1AjkQxZT3CW-n5tfC0tLzNDbTqVvjIlPx6KaZ80beEg_9DgEo5Z8MvMnu8SWCUnH7PaLujrG7FY7LlTAzgvBtEnbtNL3TrnMYeFJAbmju1zyk4y7uhZgEyKAix3XmUI7VquXZHX6s8ZD3w2OcP1qEbrZc1-HDsPwXG7d0E8dh4JlToa7QrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCYOgZfXEuT44T6wyKyy-ygD4cWnFJ5SJ0vrsK_06UcxfHUcQXsUAPPoH8hSm6SGpqibgWRJGrP1Ns7N7U9ml0GDw3VBl0jZu9o-Uxp7PsEcOdWKUZAM_tg8jF5mZoP9QbPkkieFq_9ZPwy8N3HWHHGLa0aLigfwNpRgb8dWTOAnt6Tpw4LY390BDyy_bpvlJn8E7RMNJXqeL-m-EYuAWC1Czd1tYmuzITi32SlqOp6_TdgqkcYYut1a2Tb-Ffs6fIiyg9xWjDTAOAM7uhCiurm2MYPFXFlTkjkifAYsyuZgSxylywpi4KgfAgPFhABMjR3ivaInjo0MVrZpY5_6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzOv1hR5lxcMZh0yP-7Y9bPWwhMnhD0PbL2pzpu6lHQS877X-gnYAAlbmd4qNML-iehPgDN3JXT7yu2aD9SvSltqv2hY--4PZhMbnIlCVTTZmr2yiYHSfVzQ0Wgz00LWff3mxAlvsqxffV-PErsbGTATH2bUXAhYS8J_yjIMUzUFWLguGTmleG57yYNy8AVXgvp2Yd5NoS7F-0SAgeisVGMAw916vWoIcp8_C1Ki6pgeH5rLQE06BTRaGHEyIK3FEQvTp1cieDk74YDt2-cOAl5wkX08q6eSoC-xRQXmyYGaib4Sdo_qbnBmgS15hlH3P4TA3EGkr2FVtjP8qxjnXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZWNbjM9wKY2LUlQ2cLaPqpS5gzwe0YrggAtcQnRhHU4q_4opBIH2xOQmGKJXqRJPctXaAMjUuu2HPl4kjoKChpRbp4h9mYDvSW9qTzY19NlXVLtSgMwZ109GPDVXWnCsZ_Du30DZODwZ6k2CueE4J0DHpFu22LmtHPJal64_iyNSwWgKzfyDtE6J_ea2tMECk3Zdkfwtr_i71xXuEudWWdsZS43zmvpEAl03OzCXhJ8xOcNArz83qjUGGD80tzO7njtkf64J8XCiYXxlGx8ziZqya6sGDgLJB58YswuP1mprNOE8Y8c3aKFb5fyFbQb1YiJKOsUxa4oUgX7isi1wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te1d8aGy9xABcyAqrgOUtKnmzWBwIB_ajh26oc2MueY3DrK6lE9TP11B-S89Mo5xF393QjaduBT0Q9fwZh8fqi9GRKfXyOCINYMmW5Px4F1eO1YsLkjb0AJNsBzuCBS1F8FgOSmZYYP0Onp1o5hSmkqxl1dl1G7V0xPZF7KH9P1ahU10A1IYdHe7hTndc0ZjdkyaBNAExE7hy_mGAV-fW-NcWKzp629DNdfd2op8OS5sKteJdRoXUpc6KSMmxuMIrnqHwpnOkTskESCWxOmHHOHwggIvkgen5oD6E5fLt4Qe4RklNf2KOsni_JBmkoi4k0vZzRg1lKFuTmb-aawlxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFeRPt9D3TdagMmtk-PB0IAjJ7o2MMYjWCOqB1NpZR-4yY53FQNt1B6veU4DiCWAwYMt6REbXdzZU32Q7aIylSkejX0k-oZe4YdFDO-UJnE9jSY3QcqemkyBkV_2u_4sahNnREciqXS1epbmBBPUqiTa_pT-4TKhhWFQr7OblHb5akZx8Ebd9TF8hvDixO6Iikrpm-Xej_kj3mNg2IB_pWqjxJGgcA30uY1rm8uupnArT6KiKyTsxOplBpXeDDmulAdln7irkMbAshkpejGMMDIvHIWFhiE8jJqCJdtUbLCkZgDEC-GGiH520SEp9FrRn2u2z1dl8XddsE6K1dXKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djjyfUsEL8licwW2v9uM0Ohg8uQi5nzeDqcw_L4bELbwB7jeNMclqcbwvB5fCAPCygaO3FtJ_YHArYGrRbXy7QjtxYNUDSeOFApz62pBDI9fosZvYkWE1FHefzWBk1ZY5Ul2Xe4Q1PJVW0NZfSF7-lsUJrXPuedgJ42l-v5KImn4CxDnw6gTwjG_oQdrTMyxuz2Zsye4CVGzSE1ZGAcaobZp14uFGVZe7-XnVEFI9s3abWpQeyPkxKASyfFObIGRzbz_TF6EHSCbCqdbAgWVgHBWnY0bjLuOSa0lTfe2XGsoXtu9NLltrYxhX78WNqJJjMm6JTk6bP73vkMStqL5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsmzNXEV7EMVs0YqlT_zfTD3OPhz4mJcy6JScHPPej8OE9t1chMaMYO2ku10BDnxNabupCz_dlYszBkQdC_XaRyzbTctg9_LeqtyPUbfkGc-1NKGGjexfRXBf7dxpYQcVm7SKsQFtp3RkjEqdOtR_qNT2HzZeqJ1H6xfxWvjI5P9TCcI4_GEZH9TFTcYxhuoAwmM2NiZAd0-IfXcr4o_0ncbtASEzfmMEFgOKC__PYJ3gL_-V2l15WziEdkHUreO-GhVJWcFiVsSfvM93bMuK5VXYkkF9hf5LZmoAFEO1M1HNLguZihRoo9ErJO7OLr5hTK6YFrkQV7VpCtkk5gw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNwi6sh9B_Ps-La1WkCsNIz0kOIg4muGn9PQSARhbocpBmWRbkBSXexoy74do1qXfExQSLBPO6SyqRd_e9oKQwr5w2hLdJuzLKlaGvgmx1CTHla9WeYsXIURyrU5NCFg1uDX4LuW37uTPD9iS3NvrDlSIBquPP1ZalGAgLvHW2I1_l-PZFR9W-hEHJtSpUMwYBOv4q3tP3JgDiilB1srwfB5IiG6psCD1cOcCE0M4crtuvPWGOsaxQrTH1d9n85NPhfmP9KsHfv7Cf8jX8iSC1pFdgimYWJ5TpjTWDb7fRg-fXTTm_zC2pj4m13nsDvyXV7-TB3GwYw503WeIDHh5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kifYywUjBMpOHh_EVZkQ44kbNC6s5k2UpkrEs5svFUJz2WV4QovXOEkvEsujtYK24NbHEGTadvnGafUuI20siw3ROl15Y4vUm8DHaTugQ0-OrAYwzLQ9CrDRf2XAUBvB93KRN8aWfjXMCF8A9JOtoieN5eHp9br4n76RTjNGk9N0UtPcleNfuAsQUZdNS4vjPuSAbry2UCj3KqW3BcJMHSozfNTLY8Dfl22O9uVsS9JyNjDTlDpQwd0Sazb0iaTrc36BohuAL43PAt8kJhW0e01-7ag7WAclB9E9GWwqsJvVV1o-bPvLdkL_G1e_tTUUogpARhU-A9nKaglRoCXG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cj_B9BiCnt3TZ_LF6FiwOU47JHbv9Zrlz52agHn-yRLRy-Nt8YJ1nIMU0MkrqU5xHA-cTGV-HvO4aqkcBMJeJ5A8ykB667jcISgKQqqj9et8TaqSRDIDNy_Rhl8RtGHCAAxDT3hTOBpiWOpibl63NXJCuf_nt5lk4MPozlpbtnjPev4t3J0G_K42C2YAB6ESSgKzMJnpG1Sfqotf6fiQKhNaw9plwzRznceT-oqh5leSrDLq1UjDmblQjaPrRQY8Y0uKe2Oa3NvqpaafVa-y0MJQRkriK8z_32yeLkiOo6xsdwR7jZ8b4qKbrHi7m0PMVYDKMV4NkUZrJlJ4OlnDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqLkDMduP2WK66dXNJjsobzohERQNaUt2oy-ASdPArm51v5qyRpj5W8zFHj-cphf4rClIgkXfZ5H8RKqkWGml0p2M-YIHJp5ySCvzO4PP84LgcoW2jzey9vdCxEChKrH787IWKumm4F2R53ZlPea3KovrmR2eWybP4j0PNolGUxwVWShH-RaAzrBWMBshFwnxDfJu3_WzR542FkcnEle7rin8N6Kzj3WKQpOGjnotX7UZMV1KOz6kv0cH-d1wY6iOZRsUTNEwHPbAY6aX7sBMLxeAPy4HXkuLuSUSijxO6A-_po1hn3SPcer8peC1HjlYA2R0NBmGoJx0r-GCl6taA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEizSpRU7zFfTGE2usiVqqopiKyD_NPXIJ_OmaXKVSf5QO2oZ0Xm2BhAyjSz6YncAmUgX7cAg4daAsty2ZeoFBMGzNxQkUq-jj2PR-AaH8sURsEAYFHiomkSIzOjYrzmnZuAmBsf_yKq9ccgaG9SqZZzXPHU8w6D9RxqFVXObDF-CUaDM0tl90UkWogQfOB3EVTWmyaDGKrhfBgJaLzbra5C-KMetaSLSQK9V7UJ8vftI7y99s0XbDb8C4tDKrBZt-3zxOriMSw778T_A8ml2LhKrm5naGfkJTaXf8qEwF_fbCu8pXAUB50_GZdgu1hSBwsec36PJvKXw02L1SXdlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaE5yfcj3wsjHQvFB9lH5h5XCaQhrfw5rdxTcMtjs1YmVTnsEh_I4Jc1s3nPbFFIon_CLp7OBMCXWL2Xri71YaSEto_waMxCnSJp3jEv4UhZZkUmCo-4CVK4-v0GrduuSyrtieG4U32yFnRUVFA5SygXfEzOdkd0ynDlj_FpuXQGembY0YnC6fghdtuCQk8mlfsiw3pYBp0NmN2YrzHMDWDqgIAZMJav_TYYVQOZiqy99K-PGVLim55n9H7ThIQjsQxJ1uGdw6sW-S_PpYk35UKPsgyYMOq611vJM4MRBATQapH6Ln7kAFSPGyrIbcyjQDoziAMaQ91tsOCJh0BDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7C_yjkhP-qazcT1_RRX5bZLURYuTArCQezykLkmRaQhilf3RM656-qVAMGyxkYvJ35fYfK1M9GW76aRAnpW0IOG2f7sRqgo6QAEVzKMiF_mOQg5Oa5wLS5py_RXdMmK5sDtebDKENcRxnCW5DM5NbAZARSUXH-vG_kisZXHv3wKIRzZMHpTwFH4ups6xHbjVeuDAu4QxPsYMpqM39Gkk0NUB281zEDg6qe6lT7YKTCx_0vccJrihUN6jib0QTvqq4NTe24xx_LMh3X8py5FSkwiETRvh0AkEBJl-suVMOa_A2RsdEdAiLkrswYwva8RYRNr-VPlZohrgD5D6GP5fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gREWTnug3yO4b-yM8KAL5eQ37eifRkVO1mlLbPKpS_by8sO_3CuuMrINB-xY4CPjAzpEjqlcn_soTOWcCp40GiEyfnCoyhNd6V2KkBNh9zewDtHag0XZ7n64hGkWhly-WwcTQP0AoHuYb9glYQRl3j_743DJ8H7gFGb7uQqwMIEGIsIgqw7rlLBekYjkjUPyQCLNuA3qu5Pwe0lRzO1CSVcluTv8Wmt69518sD9KwMSXFIfIVIFKMTJ7smh5cPTlM-Wsi424_4dxmItv5DgodLdxR7sZn0M00fcS4bsXjn8_mwGMyiTeaggcjcNndKvfNUhQ8Ae4NgdcUDaU-ZMUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlkLESdplG0ZUazx6q5LUyaw3meawcIintcBgIzSBsIEpyal9og3NFIu-Qfw7n_tgvdS9h1dVLK7B9APl5cy5VywB86mDuLcGmRILlfeTIuWUBtAR0TUDxSy9ygtzBxzsGqlptW9a5sSSjbCD2IMeRSGiu87K8OQbehN8QXLWhsoVX0mlMvXCXEi_bmYMqNp1oel7PusisxG2MCsmoKX1DRcWjMl8l4IQkM7UPM01e_H9c9uY3jwPugawLppyR8lXVPK8ELMC_Bmq4HKxSNDSQI8aN3cc3pz-_73x7J-CZvNKzgTRaM9Jc2bf9_1HKA7Frq5gYEippb_o8Ww5XKgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7TfvQSSEmjzq8qy8ouZZofKf5UAFc98HwW_X2evKRMipu2Df8GUUeQfi4HV3Od_h7Ejq3KtWFzKImyQmM-LWJg6MpJjAVgV72KtxtJ8YIJn2R97v3HvQj9liaVO1X5Jr1MG8kq76UWB6MUs2mfdEndoH68Bzc81_t2tzjtE3lsTUCwQbwIUSFeo5utXx82m3AZxYbzQf7af9JIZzKrD7tzCV08lldai79xF-YzvWCiFCNJn7eMzSWpJHLrJ7HQ073uy0pK03h2uMkLVHkuz0igrZpCZPxcepC9CdYr9ut0jhLD5GXndT8JSSwVNX-Pl5sAlupvTdDpEgX1F6FjRFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqlO-MTpRh1bkbviTBBbgc2q22VjmmGe6z4aA9PJLZ7A9USbXai5jWco1laZp0vt7CgoKbvCaev3597mGm_Cj7UeAnArat05EMDZdT4qMDI3wCwStMjCsNEqxeLozV2Ib2WTWtDCTwLm9yQxe1Jndso58Q5OZZ2z7avv-s4POOImWootMCQNVV61eHsIfhX9T-gsga_VIv8EANDTEciJkWxp4czcvd3fr1BH9qbPnXxeN2jeYPjXQ8QLw7CCC_gsNuf51lXi7HXgSsKhD64zI6HPeY_n2hmmXjYvko3ggd0y50WOCsJXlsQBwVzgECgeU7lJsJzzhSQD2Fj0p2W1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcQbi9c5P_nF_JblBwwKLuC6GgxaCM2Nk99i8E8nFwP2dIz7mteU85pM1iGJAs4Hn9mc5Op0AK9MsVe34sZK1HHNnlu43Q1rvtIJXjWW9592F1s_SNe0IywIuMCO0nZPkh_EesvjSFFCin0_2iVs-9IZdE3cjkvWHqKoJsC2u-hfLepQPiU9Kv7-m79t-ail8LkqQtn586DX1nUDCgfI4CUva19qorON05YoaH3ujWl_mBrMMC1jGyvUIund8eQaUfjVwbUHto-AdpRSSls9hYKqeImYN_alOHyvEVFARK-KAdZIpNNUMKhus4uLM2UFip8c3UcTBjLOXS7VJhqxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llOV61w4B9RQdnd862CC1aVkH4aCT2C6cr3UJggrtntmf33V4wShwG6zsY7YHBv--x_MYsBToX27F7q_doNFfvEoKf_gz2DAxcu3WYdkIjvH0TdULxQ9_kur9mXFPIjlsRU9iGM8jl2FXZNPx9lAanTEBx0NZTVK7JWnwW5Oe_cYlw4OYiWAtNl3IEZD6Jm-WO-xKBWG3LjdurVGpzHb3qPq6iOaZVXyAJ0MK5DN_QTF5QP5BOYxonN6m-d3KmKh2TBPmVJ5HKUCohGR2yYi_Ez050lFVZvj6Xjt7RSNWpB54RmPo7gyDvfCy8k1h3Ptao2qYkBj6npq5cD04Sq4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5HYKHyIVw9q3dzzWmDEjok2GptAR9e1VXZ4I3yfCYwYoCEJ3Hpw4OxpEFo6JaArdL1LjRpA4Vq-BVCTov_cWlPGHZawUhMYAGEQVeBYRJp1pqeqgjHJ4P863jAw6wTrguHLLgQG_TzkE-6R0AZbJIXdbvDRbhe-dr_s59jCkkQjeIMWoApfkuVFCRY66d9oenzOk-1i6lJLiP-0Sw5kB_q9f5ufb3U4nsEhQwEjbYjcUG-wE2f1JXYZjdXuZv6w00_0oPqZk-CAvvUba_S1HQODb4Y1lA0emFi15CPklOIJzdSiYFJhIyWMbEBTuY5PfmRXsa5MqCbcE_zbn3NTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1M3wmiumAcKIFO0H5cUvTgYyIK0g2oKMBDGrIXNaYnA0H_XnSScWjREIxkHT2XWBTJAben5QfyLlP8lBeUIbBaDbLua4kQxobfn73PYpz_kf5yDB1MjzEurfBQq8VdDF6-C3nMFxS-WVntDYXS8nRnM1KY9lt50lcDkRaHD5zZtsDVVfmKLtcF7xqc5sqliioUz4iEpRUNokBf9kZ39wzEPaqaA1hDXw-qbnPWgn5e3j76Th3A1QcyWCu5aM_g2ZUnin6NEY1frKS95NyZFUmTdbn795v0psdTwbEUfya9YeiJg0ryXMH99jnSj6_w1opyPkeN_ePmyP438IMlrWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOuTAV3qFA8IszqlvaLnnjSApv9oxcM0o3jpQtFWZ1c6vbUU_YegMqPJEEgdmmDRHxa3Bb15nkZG2tymOI-lazklHa_IeRGWv2BzwiZSO0cInwX4XS0dF-0H0EKsMZY757htyI1zLjg2mOP4eG99BD2lp6EGLdzc3AVischlRqyGG-igz3h3DeKWs2zYd-KGwZ96mi-l0V3JOxa09YgKcj18dKVMXUC96Iu6HsFYO6XUsoSY2xbfJpM9ZlXrIp7Io7dGPaOzutZMXsRsTZrSrrxDS8C5iMElbnEUvhpU-7B-E3SqVK02UC_py8KQ8PsmskyHQAF5RErUymo_mTDF1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAl0TThoLFqNWbh2vepX3wmXg8ajkEk0qGJBNDbcJRvdXUGrS60rdopeSxQEBJ1MiZvfrKU0i2fReziz2jsX2szQJ84ffL7AMlO16URlUDEBoZ0PqbEmqHKp77iwbsBcc0TMbpYyO3T_eR7fYnWBbGTKNHdVKs_MfdS9Z19aCp9Wfy5RDlj3I88ak-Yo6MfXy7MTpH6Q9TBj1fzSls8u9m02h4VCJjT7zBjGeHPIDGPO9LFPLuvb6oIf8FZqpPlNh3QkYkThVLgNCqL_VCaMf2pI1APpS_8u0ogWEuMs19aQeIQNFIW8vQTPLJUsvf86BFWN2GUf0gQdTBslkiI9Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=lGM_RyptnByV7AoVci291_Vb7E_TUZpzHGawK0NiUMyfaJ14LSgOho7vXw02OPIM3W6Y86jxmW25YgSu-vxNnzyHpm7MEyW6ab57-ZJS2FG6TQXE6lQIuZ8DDuDZ1dASt9etGtJWbrvrw66Mxl_oc9VltADHtQHeOzPpqGv4yecg5aNXnA9GpVreigtMOutnxUpaVmmtfCix9Uo-HCk3X8SRwhearPVLRQeu6RTDDbnxviocJOxrDX10L8TQC_ILDTa-z_8UV8Fc5gEp9efbgDaTb2xIcV7TrYHiRFzFNPoJbYI-0Sph2hgCdDDz2zIQVSpC3Kk1u_nnitm4mqPx4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=lGM_RyptnByV7AoVci291_Vb7E_TUZpzHGawK0NiUMyfaJ14LSgOho7vXw02OPIM3W6Y86jxmW25YgSu-vxNnzyHpm7MEyW6ab57-ZJS2FG6TQXE6lQIuZ8DDuDZ1dASt9etGtJWbrvrw66Mxl_oc9VltADHtQHeOzPpqGv4yecg5aNXnA9GpVreigtMOutnxUpaVmmtfCix9Uo-HCk3X8SRwhearPVLRQeu6RTDDbnxviocJOxrDX10L8TQC_ILDTa-z_8UV8Fc5gEp9efbgDaTb2xIcV7TrYHiRFzFNPoJbYI-0Sph2hgCdDDz2zIQVSpC3Kk1u_nnitm4mqPx4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-l9o_tH-6LeBcd4tLvGr8Mz7d6Wu0QHEbo9m8a9U3xX3zzw9BK2LC0Quk-NN-XnVmJxiVdVxYJ-FUmblZfnvM0QHUQcRL4xzffdKH3n876jlIKL_cRf-IF_A6GIEZxsiltomWMSs5lltx0DzXPHyocgm9dsiEEEIfOG7sdNnOR9UOjoHkMHbKaZ99dfPsCKl1Ag6fgg-d4ZQxVA-ymrgd6wPOCK3QThVe2Dd-IbeApMY_8uFNOOb0O4ouwlIN0pFteQbW6mPpSeOwIfamddB4vkPx-3vpIRVkUU6LZaAiuYDW9k-V48GNwG38ZiW4RSkf2ehvJy3LSo5P-eRY06CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=nNhAlt846eClylEfvbavslUjqZTPQ_5IuknWVWz92KUmyzQitHhlavPYE00ttPOfjw308yZ1TdLz76JZUD7aIutQFkMqK0at3OdhjPTZwBVWlxN4UvwF1G8hKbwg4MH-Cq4FS-xjcXqdu5SS5TmJcKn4EnKaQrdWTQfWEVPRPUoiiiAu75VN-S7XXQi3STfF91c9GmkhZH9N59mSzOQSI2FBmRMVuVu9iTNY7-4fvTqp3neZa98kvuovPyabuOpAsBRcqCdKVQd_A4jaHa-zbtpc8eSct7NOCwMLBkZsihO8BiIcv2or5-XDpuz_Qt1z97QUutWiKctBMH6G0dY2og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=nNhAlt846eClylEfvbavslUjqZTPQ_5IuknWVWz92KUmyzQitHhlavPYE00ttPOfjw308yZ1TdLz76JZUD7aIutQFkMqK0at3OdhjPTZwBVWlxN4UvwF1G8hKbwg4MH-Cq4FS-xjcXqdu5SS5TmJcKn4EnKaQrdWTQfWEVPRPUoiiiAu75VN-S7XXQi3STfF91c9GmkhZH9N59mSzOQSI2FBmRMVuVu9iTNY7-4fvTqp3neZa98kvuovPyabuOpAsBRcqCdKVQd_A4jaHa-zbtpc8eSct7NOCwMLBkZsihO8BiIcv2or5-XDpuz_Qt1z97QUutWiKctBMH6G0dY2og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEFcMdiXpybydxTTxpd7172CDINDbM8PJvkuFpC0y5WA3TFzeNRCGQsP8dChyXiENv2DxH196I88CiZauYs680GDKmIe6TcdY0Jev7F7MVa98jvC_SsyiNp93u-nykqIkIaAk_pp59pOhzEINmI-zp26p4Im1_UExedlgCIdeurJEcmVjpYaVAWgYelUEQtHtgjngenUv3OjljYP-FUT6rnTIwcS9ozp1zvwHwJT9fJ4CiwENwqThpBU8wpxYz_8Du94J8noBCDRHCL0--fxDUkqKuo2mH0haBTQfjc9YCaX-wAoUpf-4TJ52T0U6BElv8kMx8zh0wxVKBeHRRSZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwDez0PUv0L0XQFeblVzVLJ8FBGN5zhpM2yqewrTvpRPOwtiFICC0WKjAvogPmgRJTbWHe6M_aSBUAEm3QBzF8RMgvDnzmha2cZ8HcREnDsGNlleDq-8mNuuy9WhlBXvvAVntwOftbZ6rLxGsmRTnIoTXWySNYVQyb22ys3-cKrlQ7SLwF4PUZl2NHkyOztYH5Q4iQngHvzODGlcJYoA2BNQS5NWBrrD67aWX0UlXmPeMzaajlt83hk1IX6Kr6sl3YAdGmYzADQKG62TiwzI1zS9Ndqq4Mil9qU5PvKbE7Bt1UVL0pxcozBUc6LCRN2zeSZURkeRaRfyO2lfUc4geQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=To8NX82NFv6K6lMF9Tf4nIMyay1YwB5Britds5rGEj_W3mcWSE976QwVA0t9fhbIKzbKndfyZR0Fl1W1cikVPaWnwuIfCg2sNKTW4EtIhlJt37hhNEHyS4s_yVuRsoNnEg16fv8vrJM8OdzJRCU6ftx14EeFVLtF0C7l4iVSEaEbfIR0rSGcdQlKpdsRhuuZj_W99viO8-P_BebbEW2QzLDq7vzC00Dzf3jYFUpN6VYbG8-80_nDtWEwjOn7uuir5O1g7vfk9iPngaSHaSLtvJqVslqeGJ-mdhxfzLPv-R_mDzGoapB66MSrjnUWZRCZ7b2PyA81WZREcnxFdV4SaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=To8NX82NFv6K6lMF9Tf4nIMyay1YwB5Britds5rGEj_W3mcWSE976QwVA0t9fhbIKzbKndfyZR0Fl1W1cikVPaWnwuIfCg2sNKTW4EtIhlJt37hhNEHyS4s_yVuRsoNnEg16fv8vrJM8OdzJRCU6ftx14EeFVLtF0C7l4iVSEaEbfIR0rSGcdQlKpdsRhuuZj_W99viO8-P_BebbEW2QzLDq7vzC00Dzf3jYFUpN6VYbG8-80_nDtWEwjOn7uuir5O1g7vfk9iPngaSHaSLtvJqVslqeGJ-mdhxfzLPv-R_mDzGoapB66MSrjnUWZRCZ7b2PyA81WZREcnxFdV4SaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkQEoUvzoFuMYSptWHMPjMXldkEFTpXglTiQx5jPLW-T7C_HDFlkM30GHFq9f5EUKZkDA_tHQDwNyCuRpH0UBC4aHQfhP94Bv04JFPJxSKsMGnTHV3xp0ejLFScWTBlyVUDlYMQGvEIoYx6GSY0ZiYeoGYxlTAzZx5OMFWz4woW2VBDRqTYZcQduMctXONypozteyhkJTHBcEUw6Wa7i88CTqY9IoiqRnkYdKus79l_WjLL5Q_EYlZDSUgxtVwEISEMqtqiX6e6OpUvrIvjhhmmuZDXPNJH9lQwOqvj0qS9l_UqxxdQ1V2NKtR5oA9uMhfs-fGNX89gr8vNq3x9zgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsrDx5LKMtFqw41cxV0LWGAMsiWjyd4Ksq3h3W7wLewxAq1p-q73pDUTS0Pspn1zJVNyEvphRKaeJZNEqzeN6f6r21Ydf7glPW3tdA5c1YM8qN8cpyBSbKkQAY5p6rumbwx2-X9qyl5ZrwvEa8EIujQ3KIL7Q9qgSoQxYZQUxeAjKiW1WfX5fM40OaoviLfQi3JoV3oAqaRwBe6jGBB6J00d42BAmI-3lpDM7b6JGHMlkE-9_07MU9w2YuiOetibPrv1TGX-De5OutTZSSqhjW-eRfJq32vNTWddMR47eC9RXq9klDBwb6W7Sm9RU_wdrSwCK1ZGr2H4_Tjrv0Gifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aez5TXlzGr-_X4mmNkp4YyN5Jl-l8aPU5IH-a8LCML6CExt7oHFu5pPdqTJ2Whqd4j7O-vxW79UhLBaROVTpKBiGzE-063G5-wGHInqdygpCIsOKHA5xSMfvA4UXPvp1EoKwYvsARyXDcpqdJljJrTp47jXIpW0sYUzJ3OFS4IlSYe0yi7JRT3qD2mDfcBGIep0g7Is82lfnqxzkeL8_eZEUmWo-wFuHqM9blclSdVWE5KqEqQ4a9WJpHlOEHQN2vmGqWArou-yicIzpEHdt6ALL4TZCac0i824gw0H6r4Ys0YB5eNURKiog3pY898UpjnaXV6sDdj0tYFCcBt1iWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=BHIB8W3qJH8y90AXlZ-RTydoumphfEemYCVhJJz3yahD8IXZbJ3jtAFHJry2zPhlzydtTxD68dMXvuCExuRuqrJapn8-EUBREuH4oQWNkvBEXKaCiIO1or21v_P7D9Shmu1dToE1pmrl4hhZQMdhdqIJNXrFBLia7cX_wpw18ICksr0A1m13S2TJJsx7b9HuEIP9sRBY7S4jU-8h6h3KyaNHeJcNaiBbkI4-3zfknCzvu2sZGIYU5F5E6Gh_snuBudrmP6sDGDO0KIt7xluN5pvDw3fgcBWBcJOZZK9dhAfQxmSU-huLkeeVuArNvrSvI0D8A8fWGcP-svMJU5C-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=BHIB8W3qJH8y90AXlZ-RTydoumphfEemYCVhJJz3yahD8IXZbJ3jtAFHJry2zPhlzydtTxD68dMXvuCExuRuqrJapn8-EUBREuH4oQWNkvBEXKaCiIO1or21v_P7D9Shmu1dToE1pmrl4hhZQMdhdqIJNXrFBLia7cX_wpw18ICksr0A1m13S2TJJsx7b9HuEIP9sRBY7S4jU-8h6h3KyaNHeJcNaiBbkI4-3zfknCzvu2sZGIYU5F5E6Gh_snuBudrmP6sDGDO0KIt7xluN5pvDw3fgcBWBcJOZZK9dhAfQxmSU-huLkeeVuArNvrSvI0D8A8fWGcP-svMJU5C-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=XOWj_kIuE0d_OYsY8FrE3X_pvZ5i4eUgdEFkHflcsPCtpm-y8Uhk6m0FCMDGbuNHaNODPmAQTCE4EITA5GHvLdHWOcTV_mEHMcfFbNaal6GwGH261mgUjUCqva00M3tfP3JAzzvEd198q_jwSiTqTCmqVqZ-kc-02aqLjBGfR-6hJtWX3VvetWg2ukmlrwZGF9bmo5f_xJVTl8PiojTA1sAJDRxrESBJg4B8hAEu0yuO6nGsezsD7t1O9S2sraGn7_hpMNmbZeZS969olsVuA83sblF5Qe-h4FQ5w3sjcBTf0sr0n-cKKb_6tZSSvYSPyURDD6HVFM7x2L-9Kx_l7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=XOWj_kIuE0d_OYsY8FrE3X_pvZ5i4eUgdEFkHflcsPCtpm-y8Uhk6m0FCMDGbuNHaNODPmAQTCE4EITA5GHvLdHWOcTV_mEHMcfFbNaal6GwGH261mgUjUCqva00M3tfP3JAzzvEd198q_jwSiTqTCmqVqZ-kc-02aqLjBGfR-6hJtWX3VvetWg2ukmlrwZGF9bmo5f_xJVTl8PiojTA1sAJDRxrESBJg4B8hAEu0yuO6nGsezsD7t1O9S2sraGn7_hpMNmbZeZS969olsVuA83sblF5Qe-h4FQ5w3sjcBTf0sr0n-cKKb_6tZSSvYSPyURDD6HVFM7x2L-9Kx_l7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwJ2em1MjzD-Yp_5Ye73fOh7PciEeJuiq7BxFlN37kTZRbQtBobWvipfJakKbxiaw7btsJv0646JO2XUVxQCBbEp-ibF-bAbkTropzjzaxY-hV7k6Myu2Or_Wnh6gXRmFA7qwblvO8edkCDbtSVp0lEdVD5tz6X5DcKejOJEXnXx6I2tSAQ1sq7kVv29aD9hcCY70EpHS41DQq8ATwpOUhEZYjKXlH7KROX_WZLiqbSoH8u6GaXDsYzfJtC-Qb1JDbjajWWs5-MOcpsy1Ql2BYo2IbUcbBXFmvec6sO4EKyE9yFWQcKxiaX1gZO_9VckkmuIGL_1GIGkz8B2bUMQCA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
