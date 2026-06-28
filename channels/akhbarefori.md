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
<img src="https://cdn4.telesco.pe/file/t_r6O36fvFxyDz1cSWQQxM_R963RZymQu0Y3nFYBC1MGGWfwTroQzz9pkWk54W8-us6MEe7uNk_jdvNKj9sbMlswZYFQk6McxvosjumEPRuXpL2y7_awoYQGVfzkGxolqzCqHwPcLFMhsZGtH8Erh8jW0Ji3wx2bCFlk8_BhEnaondz4Aqfa3tsZlkhwslWzCq-HUX0RjTjV0wOidraFWH1DvfzsInd9KBvxK9P9DUJFG908oSlXjTL7phDeJ4uJT0TjRDnIn12qWX-ZG09JA95LwQRjC9gtlxfcNxp_6Shm2RyLh3zCIA_JIV-k_RNk3B9C3s6zHY7pfFe0l3clnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 11:31:22</div>
<hr>

<div class="tg-post" id="msg-664192">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df43f4a96.mp4?token=GmMIqKVsqrbEGi660yHPcP_-b85exfBOVYS25VQQV6g4GAcv0n9pTGAk-1nRO9kw62SlAn24U87o81p-ptWzK05ZhoMa-_2Avi38aCpdOfxl1OeLzTh6dsJcF3IUkrAo8N3IusF0FSZvs5uR66hVNyTWoxOg3H_9HtWUisaf8vUWAKV3kaWgsDABXyHN0UjqqSRxuwqjrNT-3-H9Dzj_JfLXjuWm6tZJhWHxkcHUyZamD33uwweElRFomBovh89bvfGytW1hQmqlLccTGczyWueB7bkr56KtNXcKjacU941TwSSv4nYWr0TVBH8cEh05WhmRDK5_uH1DCJ4UxB03R2cIfnBACW0rnCmlNoYrklvdxH6OId-eP2rD6SdKbtG8cvOHr5jtcjygLWXuNi3AZtbhaF_t5rvnvPBxRyotLRGcOu-7K8pdE88H7OouvI1M550DcEJ8I_-1os-DxQOU6Ec4Bh8qVtDv4i2jbryuFPMDbrrtJmRKeMibOFgWJRm-UcV6hx22q8L8CX0ILERvuyjuNJTo4ddWPgpbdVymARlrM3PFsXXB4mLZ4pFSxVGgHUYAgqsfp-b6WMXTUDi-U8xxV-BhljPT_jGH1UhLdXfKLi7TfnYvd_iFXXIYJZlTXDfYhpZM5Fx3kT5NVgEjw4yfr5tidA9pm2lAqc7Jg2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df43f4a96.mp4?token=GmMIqKVsqrbEGi660yHPcP_-b85exfBOVYS25VQQV6g4GAcv0n9pTGAk-1nRO9kw62SlAn24U87o81p-ptWzK05ZhoMa-_2Avi38aCpdOfxl1OeLzTh6dsJcF3IUkrAo8N3IusF0FSZvs5uR66hVNyTWoxOg3H_9HtWUisaf8vUWAKV3kaWgsDABXyHN0UjqqSRxuwqjrNT-3-H9Dzj_JfLXjuWm6tZJhWHxkcHUyZamD33uwweElRFomBovh89bvfGytW1hQmqlLccTGczyWueB7bkr56KtNXcKjacU941TwSSv4nYWr0TVBH8cEh05WhmRDK5_uH1DCJ4UxB03R2cIfnBACW0rnCmlNoYrklvdxH6OId-eP2rD6SdKbtG8cvOHr5jtcjygLWXuNi3AZtbhaF_t5rvnvPBxRyotLRGcOu-7K8pdE88H7OouvI1M550DcEJ8I_-1os-DxQOU6Ec4Bh8qVtDv4i2jbryuFPMDbrrtJmRKeMibOFgWJRm-UcV6hx22q8L8CX0ILERvuyjuNJTo4ddWPgpbdVymARlrM3PFsXXB4mLZ4pFSxVGgHUYAgqsfp-b6WMXTUDi-U8xxV-BhljPT_jGH1UhLdXfKLi7TfnYvd_iFXXIYJZlTXDfYhpZM5Fx3kT5NVgEjw4yfr5tidA9pm2lAqc7Jg2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیو را نمی‌توانید تا آخر ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/664192" target="_blank">📅 11:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664191">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb6ba14bc.mp4?token=PTWmtBuTfY3nkD3OEHlBUUQYqrhmzKjixWeXFf0DqvMYRs6wE-Q8CJtyceVePOgzmtc8hLK4_mLAnFCCyjWyR2-edKkcitYuhrQCQ9K6al4gJb2C0qdPkIOSivq_ljwYQkA-xrk4sYjGzo9RXQzJyoK04MbXqHTLz6OYyi7CWUje23w_y9Jo7F7SiGExb0j0bfKsxLPTdqAcAWuFiOk9AN3iDjHz6umCrGIk5DM5zrRFby7m_SNlVew-uBi2UdgAgrA1qmmeQCV3Yk3ipAHhEPb9lRNi8z2dGaj91HPZ0VU-Lllxgm3uPyAH9ZdYFiN89-TivnAtBa2VWo07uAD6D0wx1rSKGS2kx-oZUB6Lw_k5ERWmZT6MkXziuGTWDsasF_ImCelTHgpWw4RYEKnN4wJf-JKLOam7PsfePauHvAo37vi7mwDZS2xVFfdQ3QYWBLJoYru_SWhHHDtc_nYJvS0YeOLuvpgje3eatGa2nV-8jiYs9YqYzFfyLulccHsBX6aeW9mCVANryA61Nh4VufUVEuTWGPPlLFWthdWNAzgeRTAILtYofm0RKUKOTW5Y1BvDgEnBxOAzvJAGbdfIWqKtIWehpzOJtTj9vl2UEprW4cCnZ5SHTcs80g8IgPQyAJFTClmYz7d7w_PxW81vno6xQZ7UinJ6GyfecM_29a0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb6ba14bc.mp4?token=PTWmtBuTfY3nkD3OEHlBUUQYqrhmzKjixWeXFf0DqvMYRs6wE-Q8CJtyceVePOgzmtc8hLK4_mLAnFCCyjWyR2-edKkcitYuhrQCQ9K6al4gJb2C0qdPkIOSivq_ljwYQkA-xrk4sYjGzo9RXQzJyoK04MbXqHTLz6OYyi7CWUje23w_y9Jo7F7SiGExb0j0bfKsxLPTdqAcAWuFiOk9AN3iDjHz6umCrGIk5DM5zrRFby7m_SNlVew-uBi2UdgAgrA1qmmeQCV3Yk3ipAHhEPb9lRNi8z2dGaj91HPZ0VU-Lllxgm3uPyAH9ZdYFiN89-TivnAtBa2VWo07uAD6D0wx1rSKGS2kx-oZUB6Lw_k5ERWmZT6MkXziuGTWDsasF_ImCelTHgpWw4RYEKnN4wJf-JKLOam7PsfePauHvAo37vi7mwDZS2xVFfdQ3QYWBLJoYru_SWhHHDtc_nYJvS0YeOLuvpgje3eatGa2nV-8jiYs9YqYzFfyLulccHsBX6aeW9mCVANryA61Nh4VufUVEuTWGPPlLFWthdWNAzgeRTAILtYofm0RKUKOTW5Y1BvDgEnBxOAzvJAGbdfIWqKtIWehpzOJtTj9vl2UEprW4cCnZ5SHTcs80g8IgPQyAJFTClmYz7d7w_PxW81vno6xQZ7UinJ6GyfecM_29a0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاشته دیدنی؛ گل سوم آرژانتین توسط مسی
🇯🇴
1️⃣
🏆
3️⃣
🇦🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/664191" target="_blank">📅 11:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664190">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8aff6ae05.mp4?token=FcwXs5D0MpOl-mYlE5vpMmwBUq_9jK_5vPWEXofZqPS1nafNrvF8xajkiO6R61q1rptlWtRftOI8phoxe3wRRebP1RhsbnksdR45C3EcjmFzqbYRCOvGaMGCCpuD02nfZfl7DbLoB3sPoL7JbWrHeIeVMCrBFj48t6by0Vsxn25sApuQrVRjNh3PZ53vcv1cKl19eWaLCAuy-UI5rJ8iWA0Pnrs3e3wMlnS_ozRz8E57J3oOdZJn0HHqgrRxFGM_3zjz6Hz5_hnjF1t8gMaLa4Jzo08qJQXeWT-xbpFohdmRSrd8vE3dI7Y1-zaBfgVm7c4EdpaegCWZK78oJsaduj1HcaP2ivgvYMr1byrzz-XU2k2xJbGpP4n5zDLpoZxagAq5xJS5Q_qx9mIMcdKATHUkkEGbO7hxQyH99UHeFD45iStHew1J5KmX_2UdC0_s7vZ-WyBAUpEQEoUoVfNywedlicaRT3GaddSoDuZrG5-acINv12eP8s-uDhY10sX1fVizm8Nd2MAQVxsZv9UijCMqNO9DeuFNv9IFJv4yAAsHMZmGSlkGvRKSuuVm4oCHGuILSVR5wO59yHYeriUNTic7n589_8JAKvNG1LKZxTwTo-dbCeWsi9chZtNuDxdIDF7mv511YwpJVo_Cdz3hyR3ZZ83vFWFLbaiNIJkksCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8aff6ae05.mp4?token=FcwXs5D0MpOl-mYlE5vpMmwBUq_9jK_5vPWEXofZqPS1nafNrvF8xajkiO6R61q1rptlWtRftOI8phoxe3wRRebP1RhsbnksdR45C3EcjmFzqbYRCOvGaMGCCpuD02nfZfl7DbLoB3sPoL7JbWrHeIeVMCrBFj48t6by0Vsxn25sApuQrVRjNh3PZ53vcv1cKl19eWaLCAuy-UI5rJ8iWA0Pnrs3e3wMlnS_ozRz8E57J3oOdZJn0HHqgrRxFGM_3zjz6Hz5_hnjF1t8gMaLa4Jzo08qJQXeWT-xbpFohdmRSrd8vE3dI7Y1-zaBfgVm7c4EdpaegCWZK78oJsaduj1HcaP2ivgvYMr1byrzz-XU2k2xJbGpP4n5zDLpoZxagAq5xJS5Q_qx9mIMcdKATHUkkEGbO7hxQyH99UHeFD45iStHew1J5KmX_2UdC0_s7vZ-WyBAUpEQEoUoVfNywedlicaRT3GaddSoDuZrG5-acINv12eP8s-uDhY10sX1fVizm8Nd2MAQVxsZv9UijCMqNO9DeuFNv9IFJv4yAAsHMZmGSlkGvRKSuuVm4oCHGuILSVR5wO59yHYeriUNTic7n589_8JAKvNG1LKZxTwTo-dbCeWsi9chZtNuDxdIDF7mv511YwpJVo_Cdz3hyR3ZZ83vFWFLbaiNIJkksCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرمای شدید در فرانسه باعث بیهوشی راننده اتوبوس و تصادف شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/664190" target="_blank">📅 11:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664189">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678ead5773.mp4?token=S1E833sq3MsagKZFgMEEb7Lh4W-2VBDPMucxF4UPLfoSP7W25XYzxM_rwQEWJtAT9M7QxOU-PMkFXmBTaqV30tvWw6S-kCEE2TpF4BCedPQfMJ9HjbXr0iqI2YB-aVQGJ8Mx-4NYVpQIO0L5Znnoi_4s4Z2p3bxGhIEkPfIAjuO24GTevRGiP3JuBrK9hE3S5oh39K1wl7CvQhWkCLxoCoDzQ37DfzArvYAp5Qm3SvmX3diThlOhyY6G7hP5Z8tFFI7A1k68kmxE2PblYML8ielfQtWxASC8dPAnl9E2SoFjRFSoSNV5TVFxazzdWgJ6XBtDMsFuiurhjOSmmOXVJAwUkjALn5nW-VW-xJDCGbhdrPlr5v-sAPd8VPXROtZrSCbm2kM9WlSuptoBWrSuIFJne3Wm-CwyrLPgoVC7OSGNc3c5uazOPkwUworBuzj_hmCU-rRVx6j603pKwVIjGFKNwRFUrnOIyr6e9UDXe1hdsy4tLmPNZ6LIMbr967PhUOyUeuprNb5U2DF9JCf1p0hIhCauPlq4L1JdCpPsz2VSUfOSuch0KdUPrhKytJzS0lilwQ1M8MQvizEMA2eoD62_XNUPQreplBMJ-6M9QUojchU0sggOCtpOqCvaCrUb-FrTHiuKK4FYrMi87psL2GXaIWRNo_iitml03tGYVM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678ead5773.mp4?token=S1E833sq3MsagKZFgMEEb7Lh4W-2VBDPMucxF4UPLfoSP7W25XYzxM_rwQEWJtAT9M7QxOU-PMkFXmBTaqV30tvWw6S-kCEE2TpF4BCedPQfMJ9HjbXr0iqI2YB-aVQGJ8Mx-4NYVpQIO0L5Znnoi_4s4Z2p3bxGhIEkPfIAjuO24GTevRGiP3JuBrK9hE3S5oh39K1wl7CvQhWkCLxoCoDzQ37DfzArvYAp5Qm3SvmX3diThlOhyY6G7hP5Z8tFFI7A1k68kmxE2PblYML8ielfQtWxASC8dPAnl9E2SoFjRFSoSNV5TVFxazzdWgJ6XBtDMsFuiurhjOSmmOXVJAwUkjALn5nW-VW-xJDCGbhdrPlr5v-sAPd8VPXROtZrSCbm2kM9WlSuptoBWrSuIFJne3Wm-CwyrLPgoVC7OSGNc3c5uazOPkwUworBuzj_hmCU-rRVx6j603pKwVIjGFKNwRFUrnOIyr6e9UDXe1hdsy4tLmPNZ6LIMbr967PhUOyUeuprNb5U2DF9JCf1p0hIhCauPlq4L1JdCpPsz2VSUfOSuch0KdUPrhKytJzS0lilwQ1M8MQvizEMA2eoD62_XNUPQreplBMJ-6M9QUojchU0sggOCtpOqCvaCrUb-FrTHiuKK4FYrMi87psL2GXaIWRNo_iitml03tGYVM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول اردن به آرژانتین توسط التعمری
🇯🇴
1️⃣
🏆
2️⃣
🇦🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/664189" target="_blank">📅 11:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664188">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06088a319d.mp4?token=qcE0xJG3gCUiJmfUqMzwdy8wOvxdqDl2W7p1mzLGGGAkJEy3yj9A7UVd2N70EXq2D8qL2pP-qzIxs-SNvFrTVXMY0oKhC39JuLeUPyGIM2-EpZExVU7aEJ084KEJPyDD90qhov3rymmkmpjH2zrnedu5it9HNGq7dS64H6WnNknw9_cdCsvzkZ2u5SJQHG3tE269BJS_PVSWJThgkSb8-Rr5yksn4g1uNNa7SEV__5fmOZ40f16wV0z0_7hifPWuTquM9PfiRPhXUADpDemBgGcRW15bKGns_3wMIOQscConwvTfVQFrvrZd5ODAvuzuYqyeyuu95BMGto9f1HDO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06088a319d.mp4?token=qcE0xJG3gCUiJmfUqMzwdy8wOvxdqDl2W7p1mzLGGGAkJEy3yj9A7UVd2N70EXq2D8qL2pP-qzIxs-SNvFrTVXMY0oKhC39JuLeUPyGIM2-EpZExVU7aEJ084KEJPyDD90qhov3rymmkmpjH2zrnedu5it9HNGq7dS64H6WnNknw9_cdCsvzkZ2u5SJQHG3tE269BJS_PVSWJThgkSb8-Rr5yksn4g1uNNa7SEV__5fmOZ40f16wV0z0_7hifPWuTquM9PfiRPhXUADpDemBgGcRW15bKGns_3wMIOQscConwvTfVQFrvrZd5ODAvuzuYqyeyuu95BMGto9f1HDO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از لابی هتل تیم ملی در تیخوانا؛ واکنش هواداران به همراه بازیکنان ایران به گل دقیقه ۹۵ الجزایر
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/664188" target="_blank">📅 11:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664187">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اصناف تهران: همزمان با افزایش قیمت نان، نظارت بر نرخ‌نامه و رعایت وزن نان از امروز تشدید می‌شود.
🔹
روابط عمومی فرودگاه امام: پروازهای
فرودگاه امام طبق برنامه در حال انجام است.
🔹
ثبت ۱۰۹ مورد مرگ بر اثر گرمای در فرانسه طی یک روز/آتش سوزی گسترده در جنوب اروپا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/664187" target="_blank">📅 11:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664186">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip6fP7OJnFah-JpjWplqga6mkXobN6zkX3UR7d_o6kCrBuf7eAa4_NzZFNc0-q2xNUg5ZEgPqo-BHTGWGunTh3sq4v_Z8ZMm63zEjSzqYDs-c6xkIQ3jf97J2Hfi_LD3L_vOHzF_Q61-7FMydVGmHauM_aO6PL6CkqLaOdsqr04jbdPnIHWG5ThlHGV5rVMVQ0vqG_S1NpuZ-uGox0_ntT9qZcUEiJWw3YIaGXCKL8P9KvCx4fnH8XWUT-WTx5zMSuQQRgHciZ_CSZEVjV49BJXnFwBUzxsZsRgzsjJWQRi2r_XoCdbD3Zz2Cb8xGO8qnlbDJ7ynHix2QSHxzvjztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ ترفند کمتر شنیده‌شده برای داشتن موهای سالم
🔹
اگه این موارد رو رعایت کنید دیرتر کچل میشید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/664186" target="_blank">📅 11:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664184">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4Jxzt6zMFO68OgjbzfQMw0NnWMQ8RuJKRCIhAT2vxfeVQxHGxl0hvy1ftFw8xMlvtHEtM5Ol7RT1xARumZz1WY1mWiSv7wKhYsF1l9uteOzCLC5ZS44WapmsU0m6EpYQDmzM9Tj8tYcuAtJXv1USqNsgtSq1trzIZe0fe5QIHqF7H1anAXEsac5Rk3l3Mw3XfEzW-8bz6VJZcL3LV7N45PfVM0_xazbaMBwT3vtFrMbhsUC-ZGC8glTty4JXLTE1mtyYwvFjx_fgbh3XK2AW1038fID6a-q90xxDsu05sgRIZtosfTLw1zFE0WSxGokw3taMeDIPxw0N_Ir3Y4jwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJZWy1_O9m13diam-qmFM6M8rc89EtxJ_iCc68QNJGkiHPumSAlnwNQWgS-Jk_eSl7nWyL983UYJdxxAnaZKp1to4ImTnWwV1bTJm53WKBW0q8iI6fnWvIVQtwXKNXITScepFAV5ILmPnHSJs2KnMZqkFsl7JkzYutIvMC0XLfr_Z8_kd4lzg4xLT2AVsXEpgHYGF1emA6IeCcXr72sPTxsF54IHqa4wiochWXYbWwGprOt3SZir6iz92afcVvBzj66OGo_nqIpG9OpbGw2Uvcp5q8XXljXUBcXdtDfjdwBeTMpZu4CLQ85fe-vQ5PSfVI2kBU8unI2k156a7GbaGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور عراقچی در محل شهادت سردار شهید سلیمانی و ابومهدی المهندس در نزدیکی فرودگاه بغداد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/664184" target="_blank">📅 11:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664183">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaAuqDapOmWsQrajbLEW5lR_koe_LvumnT8fhRSp6Pfi5EcoKW3khpKIwLontBmsFQyNzueIVoc30H8nzQeUM1fqJah-CnZEcGaSajiGiCFQRQNZSVWWgYY1cWPFfXwI51X8JDo0zmrx7z04KmeRy0jMYMrB3RnqO_NC4WWJUqJFUmCcYoIVHJL6qZa5VBtdFeNhTL6--B4O_Z7BlVips5oRgLuToGxx9AaHUBl1AV5k_k60Wr56YP9LI9a8nHWB0sbOPj0xqsy8VZcCaoaP8tWMBx7IYLv7Q1xa-PXr9MpFRKl0JsvDnfe2wM3IkVDjFb2z1SL2dgARbHGusTJUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت‌های جدید اینستاگرام برای شخصی‌سازی بیشتر الگوریتم در راه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/664183" target="_blank">📅 11:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664182">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73bba0667.mp4?token=hH1dMiywhGABgdMiRtwbUAcu1PXbnPjpn_ReaYSfBRglYI967WnpYfypwDi6oOhwfkVLJruI-3Lpysl4cUqTLxyZ68WzNVpmV_aagJxZJPxuoYXUkr9gkM_-_w4JWWtiu7oIvBDiIywHg479QDw81GX01KJKOlYfHNZby2ewVQghgfUYs9_xqrk6E5V5UdCdk4-i11FfOGoLe9Jh6v70YVpFKWwV-k2clGTeDcaoTrYN9cihEV8_Q9TsLXJC5E-gLunhMnmRQPIMVxe8b7-HuHNXkLpHLBsvOaYcTOvINP0MG_uQGfYM2Cxq54mFRX1LiheEkxdM7w0L6g6fdH8uSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73bba0667.mp4?token=hH1dMiywhGABgdMiRtwbUAcu1PXbnPjpn_ReaYSfBRglYI967WnpYfypwDi6oOhwfkVLJruI-3Lpysl4cUqTLxyZ68WzNVpmV_aagJxZJPxuoYXUkr9gkM_-_w4JWWtiu7oIvBDiIywHg479QDw81GX01KJKOlYfHNZby2ewVQghgfUYs9_xqrk6E5V5UdCdk4-i11FfOGoLe9Jh6v70YVpFKWwV-k2clGTeDcaoTrYN9cihEV8_Q9TsLXJC5E-gLunhMnmRQPIMVxe8b7-HuHNXkLpHLBsvOaYcTOvINP0MG_uQGfYM2Cxq54mFRX1LiheEkxdM7w0L6g6fdH8uSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به اردن توسط لائوتارو
🇯🇴
0️⃣
🏆
2️⃣
🇦🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/664182" target="_blank">📅 11:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664181">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdGEJzNBuonVJgywBjWEu1AG7w014Ewv9_2Q-8wpMzB_Ei4DoCRANZ5SXOjRyMhh0aWl9XJX-Lfo5_3baCKOEYkXHwg2nakGacCUwn-DEVrk18il5JB9KaOu1DDOVQM7IRMpobDRvFoHAsTv7WniDWzLfcWHi2MTrHYocaw8mDja4a1jGm2Gj8llFNnbJcMyo0HviqEh36aCc51HTWUFOIJ4CVYXFZtGDSuP-AGKUqWhvflqJxLqZEJ2F8sDOGOe05BUUbAxUtJE58TjQT9up9mN_7iJeNj64_gOtooKi21mVhzf0wNyVARdPLz7KeISKJcwNWmriQc2cSEyo6PBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
این روزها اگر سری به آگهی‌های خودرو بزنید، احتمالاً افزایش خودروهای پلاک مناطق آزاد را هم دیده‌اید
🔹
تمدید مجوز تردد این خودروها که قرار بود یک تصمیم موقت باشد، حالا باعث شده بازار خرید و فروششان هم جان بگیرد. فروشنده‌ها از «سند به نام»، «تمدید مجوز» و «قانونی بودن معامله» می‌گویند، اما در مقابل پلیس همچنان تأکید دارد که تردد و نقل‌وانتقال این خودروها فقط در چارچوب ضوابط قانونی اعتبار دارد.
🔹
به نظر می‌رسد آرام‌آرام یک بازار جدید در حال شکل‌گیری است؛ بازاری که نه می‌توان آن را واردات رسمی دانست و نه کاملاً خارج از قوانین.
🔹
به نظر شما این اتفاق فقط یک گذر موقت است یا می‌تواند مقدمه‌ای برای تغییر سیاست واردات خودرو و افزایش عرضه خودروهای خارجی در کشور باشد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/664181" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664180">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322e5f683d.mp4?token=WsQU4JoE-An-ll9KZgN5WnuyqbERHcZSEHf308aHujK9gf4s28qWqSAOvfh2LC9AGdOch8vX3RfEht6JP7j6kIFBhYbi3O_pUVrYon8j01hi_Io7CjV3YY5uxluDhQ2QbTaWnsyVncz8ARORIUWD-rbQdDDmJZyAw7IV_2n44NgohhxEuAW1rezaCu4OWNPoncOyi6z49PNkhSjjTmX3EA0DQVM7RYaGh8oe_p0H2zXiYM4VZA6ttXb1TsaQprELEis4ipsKSLBaKck6Nzl3mp8nhN6doKRuRsDD5ERlCv1_omJxGcE3OzxlsH-LW1pbzJTdFWk006C4Et3wmwtTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322e5f683d.mp4?token=WsQU4JoE-An-ll9KZgN5WnuyqbERHcZSEHf308aHujK9gf4s28qWqSAOvfh2LC9AGdOch8vX3RfEht6JP7j6kIFBhYbi3O_pUVrYon8j01hi_Io7CjV3YY5uxluDhQ2QbTaWnsyVncz8ARORIUWD-rbQdDDmJZyAw7IV_2n44NgohhxEuAW1rezaCu4OWNPoncOyi6z49PNkhSjjTmX3EA0DQVM7RYaGh8oe_p0H2zXiYM4VZA6ttXb1TsaQprELEis4ipsKSLBaKck6Nzl3mp8nhN6doKRuRsDD5ERlCv1_omJxGcE3OzxlsH-LW1pbzJTdFWk006C4Et3wmwtTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیشتر رفتارهای ما در بزرگسالی، از طرحواره‌های شکل‌گرفته در کودکی میاد، الگوهایی که اگر درمان نشن، بارها در روابط، شغل و عزت‌نفس تکرار می‌شن. #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/664180" target="_blank">📅 10:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664179">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf7ddf7fe.mp4?token=CaS31_MvPWsYS6HP1Q_yjxgXHiP76qiNW10_UryBeWpl03iLnxifW3GG6ws_pSGdeUhfdocJ5Ark5GeywV0oePIZKMyjrY_K-YgM4kbgriAg601Tjvw2-5mpS_Mw6Tk7o7Maku9xR9wx611r83if1CAU0IaCp2pd8DHl8lrnlRUiDVJ9lxF91yG_bgUq6LchC8Yqy_RZPTvFfLTvbSxyXWsoxoYf-tqjaPJXvWpyJe5lAmgUAsU58y4WLMDFlP0CJbKhg7wJ6WHgKjzNSeIOrbOQEddIIWa0AmLAyD_X-oesW1kLL8_Wr9qcwWoo5ho_x6EPz81yEyApYVFUhuAz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf7ddf7fe.mp4?token=CaS31_MvPWsYS6HP1Q_yjxgXHiP76qiNW10_UryBeWpl03iLnxifW3GG6ws_pSGdeUhfdocJ5Ark5GeywV0oePIZKMyjrY_K-YgM4kbgriAg601Tjvw2-5mpS_Mw6Tk7o7Maku9xR9wx611r83if1CAU0IaCp2pd8DHl8lrnlRUiDVJ9lxF91yG_bgUq6LchC8Yqy_RZPTvFfLTvbSxyXWsoxoYf-tqjaPJXvWpyJe5lAmgUAsU58y4WLMDFlP0CJbKhg7wJ6WHgKjzNSeIOrbOQEddIIWa0AmLAyD_X-oesW1kLL8_Wr9qcwWoo5ho_x6EPz81yEyApYVFUhuAz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به اردن توسط لو سلسو
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/664179" target="_blank">📅 10:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664178">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538600ab0d.mp4?token=muZY8nNjELvFN3rHuuISLqNx7elB_cyLyUEbtFuhL2sosk3g2VJQaEUEvKjeYARWR6fVU4XayOJ5d1dt7AOMZtKlHdBVoKam7pAOUIm5eeBFze66zZ-f7aey5L-agbexMWMcg5STl1mcZADwsmHxi0LXo-YoVkSutXUgqKg_bH7Wq4WXtUzqFuq14c-_nh9Cv5tPVc7hwVEkJx_jSEdgDNLnw5sy5UlC0Lt1g92gLU2Y5qGXPE_E2YTz8jvpBayDmrhaBCiInPh8gtu19cD3y60SyMyQazSXFqK2KMlQTYGr2jHxxGAS5VVP0d0h71RQquHsFkqza3uK0gcOU-Gq-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538600ab0d.mp4?token=muZY8nNjELvFN3rHuuISLqNx7elB_cyLyUEbtFuhL2sosk3g2VJQaEUEvKjeYARWR6fVU4XayOJ5d1dt7AOMZtKlHdBVoKam7pAOUIm5eeBFze66zZ-f7aey5L-agbexMWMcg5STl1mcZADwsmHxi0LXo-YoVkSutXUgqKg_bH7Wq4WXtUzqFuq14c-_nh9Cv5tPVc7hwVEkJx_jSEdgDNLnw5sy5UlC0Lt1g92gLU2Y5qGXPE_E2YTz8jvpBayDmrhaBCiInPh8gtu19cD3y60SyMyQazSXFqK2KMlQTYGr2jHxxGAS5VVP0d0h71RQquHsFkqza3uK0gcOU-Gq-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از رهبر شهید در ارتش که برای اولین‌بار می‌بینید
/ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/664178" target="_blank">📅 10:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664177">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9rNPn6GbOxPFK5QLGwLnkLDFfTsIrfSqOZgoWJ3AXd4bKHhpW431O4HrwmLNjO6GVTcdJaiMhjxtGrGKKyd8lPWuLLfODb9jfJN7CxhJr43NVbyH-o9Gz9ufAYmutLKIjtl02Vho9fJXwahk40Yry2kXg8aNgVk3sa3wnguaSdstacv-Bcou7C43hsTeA95RpEV6nPcBuDKiWqNu5jMDc8MlZXWfM4Pbu-ZRIeHkKy5I6O51XDvKW5JHjkK_ji6eyXnRbCNiOyjjtwvopq6rxyJ4YsvRRv04dVwJpq_dcgUZrlttjdta7m1Dewd2JPdu0eqxXPvqG8e_5KvVWCR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آثار حمله امروز صبح ایران به بحرین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/664177" target="_blank">📅 10:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664176">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7ccb3cb9.mp4?token=F1xYFwVKF2_DbOMgZtu5TyaMJr8HVmVel08Tu7a57Qa3BUBiQkFTo8hTiS4b7ssOcy0Z9cWEFz9RSkpA-Rs-aKyYS-Dhq8PR_1ntkIWL5yIx7U6ABIWRwu1zwq4WLkLsNZRLDmvPOy1mq-AjYWvJnhJj5PoNz1aVOlOTXu7VvD_wE5skUZmGXesfEvcKMDLjKc76zpPCaWL987dVYyKPfOgKrdk9haMmLpeoUxbWAhbj4AurjuAqA2lElByc8sfobA1hFER-luGr3TzMheCWmAIoAfSnNZ5UVWxWIj7QbxCLxmB-KHX-K82rr6FSdPV3NH_gm-3wrhsAVsdl1mb7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7ccb3cb9.mp4?token=F1xYFwVKF2_DbOMgZtu5TyaMJr8HVmVel08Tu7a57Qa3BUBiQkFTo8hTiS4b7ssOcy0Z9cWEFz9RSkpA-Rs-aKyYS-Dhq8PR_1ntkIWL5yIx7U6ABIWRwu1zwq4WLkLsNZRLDmvPOy1mq-AjYWvJnhJj5PoNz1aVOlOTXu7VvD_wE5skUZmGXesfEvcKMDLjKc76zpPCaWL987dVYyKPfOgKrdk9haMmLpeoUxbWAhbj4AurjuAqA2lElByc8sfobA1hFER-luGr3TzMheCWmAIoAfSnNZ5UVWxWIj7QbxCLxmB-KHX-K82rr6FSdPV3NH_gm-3wrhsAVsdl1mb7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه زلاتان به دیدار اتریش و الجزایر
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/664176" target="_blank">📅 10:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664175">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
کاظمی: امسال استخدامی نداریم  وزیر آموزش و پرورش:
🔹
امسال استخدام جدیدی برای مهرماه انجام نخواهد شد.
🔹
تنها فارغ‌التحصیلان دانشگاه فرهنگیان وارد مدارس می‌شوند و دانشجویان سال آخر این دانشگاه باید تا آغاز سال تحصیلی فارغ‌التحصیل شوند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/664175" target="_blank">📅 10:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اژه‌ای: اگر به اموال آمریکایی‌ها دسترسی پیدا کنیم، آنها را توقیف و ضبط می‌کنیم
رئیس قوه قضائیه:
🔹
دادگاه‌های ذی‌صلاح داخلی، علیه برخی از مقامات آمریکایی که علیه مردم ما مرتکب جنایت شده‌اند، احکامی را صادر کرده‌اند؛ ما از این به بعد چنانچه به اموال آمریکایی‌های جنایتکار دسترسی پیدا کنیم، به موجب حکم قانونی دادگاه‌ها، آنها را توقیف و ضبط می‌کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/664174" target="_blank">📅 10:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c567377850.mp4?token=aGHokjEKv1xA5Fde7wXwpoPPlDjJzrgQ_MG6G5VP_t20o4Kj4zurOHqjekgEhAL6seUbhebQezdV4BXaAzL6ZWJ20_kEQx1GyYZxo8XejaZIUeDDAyYLgefqYrhkGjYj7VFBJqGiSPtjWimnkqwVJgUHiVs6PbQPLpii8YIThA0BQUeZG3Yx7FVfz5T3HT-Pj5MXzGjNAeu9H-QQhAYsO4kW9CmVVdoSFDOJ4WP7DbCVGOBtD7D1YeE7XvlIspQcwCdsE9KJDtg-aqi0-OnJkPLky38cHV37uyLNQLoN-S5msdA1ElGGqUK_KJFPoKHVi1PdGWTVGD76633PTLPE-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c567377850.mp4?token=aGHokjEKv1xA5Fde7wXwpoPPlDjJzrgQ_MG6G5VP_t20o4Kj4zurOHqjekgEhAL6seUbhebQezdV4BXaAzL6ZWJ20_kEQx1GyYZxo8XejaZIUeDDAyYLgefqYrhkGjYj7VFBJqGiSPtjWimnkqwVJgUHiVs6PbQPLpii8YIThA0BQUeZG3Yx7FVfz5T3HT-Pj5MXzGjNAeu9H-QQhAYsO4kW9CmVVdoSFDOJ4WP7DbCVGOBtD7D1YeE7XvlIspQcwCdsE9KJDtg-aqi0-OnJkPLky38cHV37uyLNQLoN-S5msdA1ElGGqUK_KJFPoKHVi1PdGWTVGD76633PTLPE-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظهٔ هدف‌ قرارگرفتن نیروهای ارتش صهیونیستی در حملات حزب‌الله در «مارون‌الرأس»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/664173" target="_blank">📅 10:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f59f6c5fa.mp4?token=mE6buOUmGzro83JFa9KI7hnChKiqp0UJ1Fd1tIrO1tm20O96Fr-DTP_uNIPiq_LfFgEZkKDHBUBTypyAZcrKKaXwLj5_aMbSdRRMPjWj3AGhL5OqpSd5Dz9RIlZuLXl6R8CPKY608ID8SSZ9V42tsmXGjzXbsSMV00I9LaOBUHCVwkhrpyzHfjslJW08rFLzkfgi1HmEaQe6LSD4LoCJAcqDdEm7zQ3sWc0Wm_BsTb029NKwrZ4KWY4KOKQRh5RM8n11LNvtpcz_Zz7BLTYRiAtYN0-7gfYyq68R1A1llgPgvLO7dN9-aQlMdtkmYORnL-a7napkqbn4mcaUhn7FXwRsdMGzOvFoSqX7MoJbI-wFQht-eEuc8TZWSoRMAUKRuTEd8UFaw6HUz09ezjqb0lCm_nLZaYjbytQ5_PXEiBQRk3u8aYzdrd0He0sftKF2-50_qWI8aEvMW0cqOHFNML9UGK0cxK4lggNXmKnJvbHDdd9DDnXF2SLl9PrabzK16gdVtakZssGAiOvh_ruZCUaO0qk_Vq4ePlM1JiuABFpOLrf8VWS3n1kGLgrCySFVwixcCggtL5jmG3XVikbjYGN035CKyiStqaeovhLYJF34-5wTUHIi1-26yewmu15zRBur-TrW1JFjAg2OZ3B5WtwZxAVlW_i4uW1B--lxqVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f59f6c5fa.mp4?token=mE6buOUmGzro83JFa9KI7hnChKiqp0UJ1Fd1tIrO1tm20O96Fr-DTP_uNIPiq_LfFgEZkKDHBUBTypyAZcrKKaXwLj5_aMbSdRRMPjWj3AGhL5OqpSd5Dz9RIlZuLXl6R8CPKY608ID8SSZ9V42tsmXGjzXbsSMV00I9LaOBUHCVwkhrpyzHfjslJW08rFLzkfgi1HmEaQe6LSD4LoCJAcqDdEm7zQ3sWc0Wm_BsTb029NKwrZ4KWY4KOKQRh5RM8n11LNvtpcz_Zz7BLTYRiAtYN0-7gfYyq68R1A1llgPgvLO7dN9-aQlMdtkmYORnL-a7napkqbn4mcaUhn7FXwRsdMGzOvFoSqX7MoJbI-wFQht-eEuc8TZWSoRMAUKRuTEd8UFaw6HUz09ezjqb0lCm_nLZaYjbytQ5_PXEiBQRk3u8aYzdrd0He0sftKF2-50_qWI8aEvMW0cqOHFNML9UGK0cxK4lggNXmKnJvbHDdd9DDnXF2SLl9PrabzK16gdVtakZssGAiOvh_ruZCUaO0qk_Vq4ePlM1JiuABFpOLrf8VWS3n1kGLgrCySFVwixcCggtL5jmG3XVikbjYGN035CKyiStqaeovhLYJF34-5wTUHIi1-26yewmu15zRBur-TrW1JFjAg2OZ3B5WtwZxAVlW_i4uW1B--lxqVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور عراقچی در محل شهادت سردار شهید سلیمانی و ابومهدی المهندس در نزدیکی فرودگاه بغداد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/664172" target="_blank">📅 10:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ggs37NWUkJ7leQWk6oHa9DUbPIB4uHFskMd-CHEa7TsUr6Z-mt28BWEe8jFEyajmbZOTPNyolM6TWmldu6qqvWmVeq8mDay4BAZ4VyOHaLR78AcCENYox8PowV-ZTjQ_fUU-VgYOg3y7e05Ob0g1JA2wo16Dpw0JDIPBi4tnp-ZOy9Uz8Yv5yQFpo_JI-Ln_JbHz2ULvupRrKjV-2XnhbBoRpEWQJRNZowG4kX1cppLIuathVz99JGswDTMtuw1ZzU4IUAQzaq98D9rozMBwgKwqdhCiGCECZbmFbQe_RX6FnlMd0HfRCefsqoBpTLHUjQee0Id-8aNnziNKmb2sew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر کلیه‌ها در فصل گرما
🔹
گرما، تعریق و کم آبی در تابستان باعث غلیظ شدن ادرار و افزایش احتمال تشکیل با حرکت سنگ‌های کلیه می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/664171" target="_blank">📅 10:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664170">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb833a1f17.mp4?token=BH-jBx0OoJOpD_339-WBL0GQQSDaODDptPEdgsNDH0QwB07BbjqrzJv5vAbrgvGerBGr9DqoAJUwZPZVhOvZXWGdDNXH_B8k0ymxVeRGTsN-COmDZ02ZxxqDIL5ze5RKnHh7NKOEUo7x-F3WSitG6eY5c4RDGLJvzOWaEufza2GNPqUe-yx1T50rjYc9W8yll8ORx6QU4qTxXjzPgybAzBCL9C-kzCBp4MYC4s2S5wWdEdX84tejVoQfCXrUocSQnUxtnKQvXqbY_v6LoOUKTVPvWLi9GaLfOUzh0fSzmaP-QUTobitSfGfKyzlS0dI16-GfAJJ_TXCWDy937vMu2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb833a1f17.mp4?token=BH-jBx0OoJOpD_339-WBL0GQQSDaODDptPEdgsNDH0QwB07BbjqrzJv5vAbrgvGerBGr9DqoAJUwZPZVhOvZXWGdDNXH_B8k0ymxVeRGTsN-COmDZ02ZxxqDIL5ze5RKnHh7NKOEUo7x-F3WSitG6eY5c4RDGLJvzOWaEufza2GNPqUe-yx1T50rjYc9W8yll8ORx6QU4qTxXjzPgybAzBCL9C-kzCBp4MYC4s2S5wWdEdX84tejVoQfCXrUocSQnUxtnKQvXqbY_v6LoOUKTVPvWLi9GaLfOUzh0fSzmaP-QUTobitSfGfKyzlS0dI16-GfAJJ_TXCWDy937vMu2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش الجزایری‌ها به گل خوردن تیمشون از اتریش و خوشحالی‌شون از بابت نخوردن به اسپانیا تو مرحله حذفی
😂
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/664170" target="_blank">📅 10:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664169">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c813788b.mp4?token=bzql-QGMDzrSyVUyu7L387-6aSpR1rB1dK0oJYz3veKE_AyU41isJrGDK54qlCzFbZlygy4xntdDoj2KOL-pto9E3fdkwITCVA9l0W-hKRIWZxngEMOQLhPMz5WNc4n13_JfCRX96JhTc1EI4dY-nNXBDRiZN0rVEWmzGD0iAyM1UNzJnXLlW8i9N9TtWd0HhL6kG8eBb4iw30h53IY9eqaL-OUPl-vlVZMz-6zL_wDJKEMkEPFPN671P0y3zMhWF_AGmGd8wxFPIIrYIc__krcZUjffUWNxaJ3eejc-Ma--K9eJo2pLErFTyKmqrSURSjkyllt2ey1de00SuxSQcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c813788b.mp4?token=bzql-QGMDzrSyVUyu7L387-6aSpR1rB1dK0oJYz3veKE_AyU41isJrGDK54qlCzFbZlygy4xntdDoj2KOL-pto9E3fdkwITCVA9l0W-hKRIWZxngEMOQLhPMz5WNc4n13_JfCRX96JhTc1EI4dY-nNXBDRiZN0rVEWmzGD0iAyM1UNzJnXLlW8i9N9TtWd0HhL6kG8eBb4iw30h53IY9eqaL-OUPl-vlVZMz-6zL_wDJKEMkEPFPN671P0y3zMhWF_AGmGd8wxFPIIrYIc__krcZUjffUWNxaJ3eejc-Ma--K9eJo2pLErFTyKmqrSURSjkyllt2ey1de00SuxSQcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان استراسون، استاد حقوق لندن: مشروط‌ کردن تحویل مناطق جنوب لبنان به خلع سلاح حزب‌الله، شرطی غیرممکن است و حزب‌الله زیر بار آن نمی‌رود؛ درحال حاضر نتانیاهو [برای انتخابات] دچار یک کابوس در لبنان شده و در مقابله‌ی با حزب‌الله به تناقض‌گویی افتاده است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/664169" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664168">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEpnldx-Us-ZfYRe9nC4RCSF_5DHOwX9YwRBqf5LwWbcbW-ISunpVHKBeMLWgRj9YZdBiQ2Roep0UDkEDt65-rF-ep_-AbTenhuh4bUHpZwa5k6h_wSYdMB_zbCq9-sCQV1-7oQIAALMT8fq_rQ9re1O-PfVrXtYfmBbV4g4HvT65ZJ3GXdll5f-XKdwBVwSqwL528gy1sppQtaRx572kNqmypV7h5HhK8I91LVBN2r877ZYzRilp1OCrR0NxoioNlYl4fO2o4K6A3LxZVL1y8TJ7G3OrLnz6yuZy2bojk7xdQFpwDDQ5IDyg9BVd80pLrMe9hFo9JD2QJlUayn-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا گروهی از لکه‌های خورشیدی سطح آن را به نمایش گذاشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/664168" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664167">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mh7E63YAaTH9gsUgNve-L14ED26NPXhZJOpSdXrQd47uvK9atMs4Zbiuf2I0oSn2bL_dgjOS2u-kmLKOzNW791Q6i6t1fErtcc64bnZuegLlJ5yoiBU761GRN2fh3uGvhZNmDM-RyP6EK5BgN1tCiWT63SLRkbR-5usiM-ACn1CycYSdPcbKr7wZ0AwhieXnYThSM8ILd0RtxptAOLUnmUkWVCRMgCNGO-CBE8Ho3eu9aPsz8hZbw6UelLvyuVxzo1hOUARPJc4deTpEzIapz44r6RjsWWm-1xzOd85VKQAURNbRoGf0th9XzCQkpS0e7kkysmoLZ7PK-JFtKhZYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شاهکار نمایندگان آفریقا در جام جهانی ۲۰۲۶؛ از ۱۰ تیم ۹ تیم به دور حذفی رسیدند #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/664167" target="_blank">📅 09:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664166">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: زمان امتحانات نهایی تغییر نمی‌کند  کاظمی:
🔹
تغییر زمان امتحانات نهایی به‌دلیل ارتباط مستقیم با کنکور امکان‌پذیر نیست و امتحانات پیش از اربعین به پایان می‌رسد تا نتایج به‌موقع به سازمان سنجش ارسال شود.
🔹
اگر تخلفی در چند حوزه رخ داده باشد،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/664166" target="_blank">📅 09:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664165">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143ff9fd34.mp4?token=BbBudkpzDRi8GitGtLmap9YN_5A9Iv8qyJbp2UOQuhS6PRmCt6x0w0TXT6GgSdFbsgQNgbbg8_l_sv9dnsEXe61mMoCT2iUNtJ2k04yf_cCIHdyYsKmYROUGiFnpEQGVh42wqDhRkHcYN5XmsEdszcY5ZTfxG1cbDEAQE8pv4bOyuWKjgui-Xwi5GmcAC0-3w_XXsOku8nDZxlDM3_ntiGwGuG1ha6FZSpnfLO_bPE33Dk8qGvzCaLnE1b5k9aO6dzuAgq2AT0QriAJYk7mFjQDYQPAbdFRNs2Wi5viSzW_NUrNWv1-8cn_km18I0K1gQRi1xYvi6Tsb8J83UzVr2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143ff9fd34.mp4?token=BbBudkpzDRi8GitGtLmap9YN_5A9Iv8qyJbp2UOQuhS6PRmCt6x0w0TXT6GgSdFbsgQNgbbg8_l_sv9dnsEXe61mMoCT2iUNtJ2k04yf_cCIHdyYsKmYROUGiFnpEQGVh42wqDhRkHcYN5XmsEdszcY5ZTfxG1cbDEAQE8pv4bOyuWKjgui-Xwi5GmcAC0-3w_XXsOku8nDZxlDM3_ntiGwGuG1ha6FZSpnfLO_bPE33Dk8qGvzCaLnE1b5k9aO6dzuAgq2AT0QriAJYk7mFjQDYQPAbdFRNs2Wi5viSzW_NUrNWv1-8cn_km18I0K1gQRi1xYvi6Tsb8J83UzVr2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جو بایدن درباره ترامپ: ترامپ از زمان بازگشت به کاخ سفید میلیاردها دلار درآمد داشته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/664165" target="_blank">📅 09:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664164">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9d73ca2d.mp4?token=pfVkTewDgiR3yeGXdbPk7jXVHldr01VWY0ruhkjqsHGl3byO5fxsUHT_4C2J0bZekgdiphQo-N4nWr9z9LQ8-FGBrYcxPhOb1cEZMNKv-N2VXuJpOtP6yEyfumeeyTbRFdK1X7jE1ozZoE02_xVaOAIXh6-baJUVnS75_hFobqmr_gMp_ZaWReWXaqi17B4fl2jHiyIi6sDGbzvvDbo2FdfKQajzUwiQrC3DZtr4YYKiYsXb5ehg0tlvwaJNyqRvfG08WocJ4Ag0_1hRqHyKcywdF9ibN5ZVfsa07A-UmcIOrWOAX6p2UFDsUIOxGZp73KwGqC3hCgSEdCIq28YxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9d73ca2d.mp4?token=pfVkTewDgiR3yeGXdbPk7jXVHldr01VWY0ruhkjqsHGl3byO5fxsUHT_4C2J0bZekgdiphQo-N4nWr9z9LQ8-FGBrYcxPhOb1cEZMNKv-N2VXuJpOtP6yEyfumeeyTbRFdK1X7jE1ozZoE02_xVaOAIXh6-baJUVnS75_hFobqmr_gMp_ZaWReWXaqi17B4fl2jHiyIi6sDGbzvvDbo2FdfKQajzUwiQrC3DZtr4YYKiYsXb5ehg0tlvwaJNyqRvfG08WocJ4Ag0_1hRqHyKcywdF9ibN5ZVfsa07A-UmcIOrWOAX6p2UFDsUIOxGZp73KwGqC3hCgSEdCIq28YxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپی جذاب و دیدنی از یه ترفند آشپزی خلاقانه
😍
🔹
سوسیس‌هایی که با برش‌های خاص، وقتی توی روغن داغ فرو می‌رن، مثل اختاپوس باز می‌شن و شکل می‌گیرن
🔥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/664164" target="_blank">📅 09:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664163">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCOcjl4YziQKTnb4y2pqCCKuW1aiIx6e7EmmanGAkpWh9kEZc5SPoPCuGfGrIlraOCg6WjTQ9TlZRk1nSu7gBfd8Y7v6Evmv3trUIGtXe3i_SF0QQhingFZbMtMVfRwI2mhzsAtRx5q4q9uNE883C0t3sjUW5pALdRibyt4n_ob_Tee5OBM74N7354X50EnA1C_DC6aTYr3goAJNjZES_IkSChFHUSlHUaJTID2yCFAj2NHzI3qobI_XrBZ4_Ibn2EQQSZZvQp6X-gq7flsBZom9LWYPQZbhtyOE63GCLyNCCDz1ZkY_cElZ7MAtTS-NQcUFJLsFgCsRH7eKdAmxvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس ۹۷ هزار واحد ریخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/664163" target="_blank">📅 09:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664162">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSBlbupvUWX1C0Jyn94P8TNHzmFGOG4oIKfbsEmBAUe76LidXXv0ai_c2I6DFftyCUBcQ4gXgi0UizMgwsre_-VvMcj5tRr9mR1g078vd8Zee_yt2qlH1_nvSlaEmldFHvriqAQq-cM-7WGf8dlj-164hqLJZTCII9VDCPcFaTXICcIU8VwCo9PWkf60ipMY0tYk3Y0Mc7jCU24bjTNqRCfh7c7O-XsgTsWFZHQAK-uTGI-go3rHwJO2zY9mpALuvzDqCk-mAU5-Mn51tSUHNVqaj5_HhcWFZ87fGzKVRnM5G3m-uV5HOUFD_6egpGdM95NDvmCIQ9FkVmkO4icqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب گروه G جام‌جهانی از نگاه هواسکورد با حضور شجاع خلیل‌زاده و سعید عزت‌اللهی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/664162" target="_blank">📅 09:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664161">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه: مسکو به بازسازی زیرساخت‌های آسیب دیده ایران کمک خواهد کرد.
🔹
مقام آمریکایی: در حملات ایران هیچ تلفات آمریکایی گزارش نشده است.
🔹
رهگیری و انهدام ۲۱۳ پهپاد اوکراینی توسط روسیه طی شب گذشته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/664161" target="_blank">📅 09:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664160">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
شیرخشک گران می‌شود
سازمان غذا و دارو:
🔹
شیرخشک هنوز افزایش قیمتی نداشته است اما قیمت‌های جدید پس از طی مراحل نهایی کارشناسی و اعمال مالیات بر ارزش افزوده اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/664160" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664159">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVukbRWSCsezt59HFy1xFFiNUQUk1G7KkP2iRPjtq-z5bgoBghtfU96aWDXXyGGNw3_GfeHwhYVc4BzaTdlbZYH3bxW_urzFjFaedGiJ2Fmwp3KWMG5p06SA5wwMnaXVgEhjizN4SCEU319tfD3LYC8vPSCvWuwvHb2qfJVUAA5_wiWcVxE_G77O6iCSJZDBlAEgo4zLd34EdfPgukkqVN3NN-ALSMNHKYnhkOsJ-4B3ZJ3RIY2x8AEmIkzM857b0XfPCeoO9i1EQx94mbMnb7BHl4RgpPYv4FFQvHl2QkINJJ5oYanPtIUo6jj2x_y4raNotEmfk_Wc3fSuFY1RmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول برترین گلزنان جام جهانی در پایان دور گروهی؛ مسی با اقتدار در صدر
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/664159" target="_blank">📅 09:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664158">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e53834165.mp4?token=gUbi-0ZfKAynA5KQ9NKuDa1jbAsQVep2hpOTuLWASscegoqb0c_Xijvuv_IeppO84Lfyx5UUwsGkVGA6eYBElqH-KGmeCdP18RQLM_X7zGjSmRPXRhS_tAZhKaIaTA2PKQoaDicqj8fNIH_6Er6F6mZx1b5cmhsbregzmtxs-zScPS3imNHNaTMXjA95hpFYa9L8S1-osYvyBhhw4OLozWFiV0W0HiNzi_T1q7iIWhY35E3XBUpmLqu8D0xBfxfpUWDs8WaYfuzZFIZXNc6KXV-o8CXBtAkGYua89Md9NWnSc_eVWtFPhBJVG6tON2R6pyHO3_mfA3EOH8KKEeTHzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e53834165.mp4?token=gUbi-0ZfKAynA5KQ9NKuDa1jbAsQVep2hpOTuLWASscegoqb0c_Xijvuv_IeppO84Lfyx5UUwsGkVGA6eYBElqH-KGmeCdP18RQLM_X7zGjSmRPXRhS_tAZhKaIaTA2PKQoaDicqj8fNIH_6Er6F6mZx1b5cmhsbregzmtxs-zScPS3imNHNaTMXjA95hpFYa9L8S1-osYvyBhhw4OLozWFiV0W0HiNzi_T1q7iIWhY35E3XBUpmLqu8D0xBfxfpUWDs8WaYfuzZFIZXNc6KXV-o8CXBtAkGYua89Md9NWnSc_eVWtFPhBJVG6tON2R6pyHO3_mfA3EOH8KKEeTHzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به پاناما توسط کین
🇵🇦
0️⃣
🏆
2️⃣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/664158" target="_blank">📅 09:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664157">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9133254b32.mp4?token=RKBRK5ERQpX5uirPbcdK0WvS9oeRYaRG9cQGooBR6M1gsP3X0okvodLrqb4OfrV_bmgbpcuKwd2cf8y41Qsnn73z8Jj-T1wQslB0bgiv2JAN0gvPMPA4G2kn-PUWTpo6maeA0STvOyyJBWaznWCREJvmybldR_pIx5sNaU-XC8K_amZqq8txdAqOuRTaBGSsalhxfujOaXDzsBN0fYv0s3o_Q0EU67AXXOAZMpKZFRbgd-rK-HtykPqHJ9OAhPIm_yoPu6CVviEsPk_ChfWFiVqmH40OJPF2HwK8Ni5FCIyrcugYSRmt2t-WI7z4xveqoTI4evNMwzbVsYsMeGC0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9133254b32.mp4?token=RKBRK5ERQpX5uirPbcdK0WvS9oeRYaRG9cQGooBR6M1gsP3X0okvodLrqb4OfrV_bmgbpcuKwd2cf8y41Qsnn73z8Jj-T1wQslB0bgiv2JAN0gvPMPA4G2kn-PUWTpo6maeA0STvOyyJBWaznWCREJvmybldR_pIx5sNaU-XC8K_amZqq8txdAqOuRTaBGSsalhxfujOaXDzsBN0fYv0s3o_Q0EU67AXXOAZMpKZFRbgd-rK-HtykPqHJ9OAhPIm_yoPu6CVviEsPk_ChfWFiVqmH40OJPF2HwK8Ni5FCIyrcugYSRmt2t-WI7z4xveqoTI4evNMwzbVsYsMeGC0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی سپاه پاسداران: از اینکه دولت به سپاه نفت داده باشد اطلاعی ندارم و بعید می‌دانم چنین موضوعی صحت داشته باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/664157" target="_blank">📅 09:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664156">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoK7fhjytD1Gv8QKgCsUs1hZ23Rd_qmDbyLsiGnHLH1Ee4MZ16vTqCi4mafQ6K-j9fm0FqE3Z4T9sDt4yYmWQELpTL4mPmRGVzOBykcVV9rxhLtwRMOR2JPdsmdJzjTStVKNrHxNuAqQqmtdOp5LhRcUXoR1ia_wSFipxVI0bn9N0fmqqDGSH2kN-9cV5tApUCA82zncqOvn33kCsR6XVmywLW9wOFvqSlIBZF9oMiotVPtU86cwVjB4jiVrWTn05AS-s4YIyXu1bXPrHwNFrmtt5V7Fi40SxqwyfnS5oSRK8AzBntBUclTYadDsu2Mrf6HV6zO1_nxO_V6sUYrs8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای کامل زبان گل‌ها؛ از رز تا آفتابگردان!
🌸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/664156" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664155">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe377c1d0.mp4?token=QVUD7tLyWnIx8m3k27m28b5npx7cg4R1OqzsMxa1qXSdW-75KS6YagCGo2KAko9zyIgXLZNIkcDPGgvbHNckekiZXiQdNNUzg4VRqfBPFz_di5l0-yvAaCrrBqRmuOJqjR8-jXAcsd7k_bGzfJdImV2sFo5Zzkis6yQKJIz2CT9pdq1XG6-uP2MqSmgHWGk379bjG1FJ1J97IJ1iKAPSIpDy6CId05CtcT6pN1AQJ9aerJZPKy2IeHKvxDO0YKqOHWrmrgrh1LM3c6e0hxrb1JDzKE-gH26Fqo7Aeljr-eRObAsNqTy4eaWyBXU2PEril9o_YepVNMGmbKbSG40_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe377c1d0.mp4?token=QVUD7tLyWnIx8m3k27m28b5npx7cg4R1OqzsMxa1qXSdW-75KS6YagCGo2KAko9zyIgXLZNIkcDPGgvbHNckekiZXiQdNNUzg4VRqfBPFz_di5l0-yvAaCrrBqRmuOJqjR8-jXAcsd7k_bGzfJdImV2sFo5Zzkis6yQKJIz2CT9pdq1XG6-uP2MqSmgHWGk379bjG1FJ1J97IJ1iKAPSIpDy6CId05CtcT6pN1AQJ9aerJZPKy2IeHKvxDO0YKqOHWrmrgrh1LM3c6e0hxrb1JDzKE-gH26Fqo7Aeljr-eRObAsNqTy4eaWyBXU2PEril9o_YepVNMGmbKbSG40_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول انگلیس به پاناما توسط بلینگام
🇵🇦
0️⃣
🏆
1️⃣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/664155" target="_blank">📅 08:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664154">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
استاندار خراسان‌رضوی: محل خاکسپاری رهبر شهید در حرم رضوی هنوز نهایی نشده است ‌
🔹
به تأکید رهبر شهید انقلاب محل تدفین باید به‌گونه‌ای انتخاب شود که زیارت حرم امام رضا(ع) تحت تأثیر قرار نگیرد. محل تدفین هنوز به‌طور قطعی تعیین نشده و چند گزینه در دست بررسی است./فارس…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/664154" target="_blank">📅 08:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664153">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1520938873.mp4?token=u2ceuAssfF3l-58cmmP66kOpd_Qa3FVFbjJPTepRwn9ZkS_rwMBvsZDGueokD2Pljw3rY3e0yh0GkDjSYowoJPCSIxW57Qpz3CH5uJX6BqjJNPAPqAicuYh6XxU3aHz0NAY4y9k6VVJvsiiLiVQIGro1Jo3pfTicloe0AQut6lAWF4KyGntIQIwrG_R2-zYciC8aB1qTToJ4Z6jOd8sT75WwKHw9Dlg0JN3a2Hb-d9n6tLccIN-13-L34czm0eKnJS44PwCRjW6JC_kjfX6v5BsYhk3UcDjvY2FPm4ENQ_xSsSRAL5jYrrSh7qgN9OnMsVCafU_bzSpvVMFPYokBhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1520938873.mp4?token=u2ceuAssfF3l-58cmmP66kOpd_Qa3FVFbjJPTepRwn9ZkS_rwMBvsZDGueokD2Pljw3rY3e0yh0GkDjSYowoJPCSIxW57Qpz3CH5uJX6BqjJNPAPqAicuYh6XxU3aHz0NAY4y9k6VVJvsiiLiVQIGro1Jo3pfTicloe0AQut6lAWF4KyGntIQIwrG_R2-zYciC8aB1qTToJ4Z6jOd8sT75WwKHw9Dlg0JN3a2Hb-d9n6tLccIN-13-L34czm0eKnJS44PwCRjW6JC_kjfX6v5BsYhk3UcDjvY2FPm4ENQ_xSsSRAL5jYrrSh7qgN9OnMsVCafU_bzSpvVMFPYokBhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع اعتراضی مردم ترکیه؛ «ناتو باید منحل شود»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/664153" target="_blank">📅 08:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664152">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D91Xhq52rollp5wp3NfqT1uVeBr-ThBADhkiihwAgOoYhDaVUVj5r1aHNpt4yVvPQuZrMx4FP6MrzNr7grqIhJesAG-Fy9EiKT2XtkW-9LBFWOSfKhL1r0BHiERq-RibbwfLcGeAfRAG3LU98k9OI0I9p2yzEQU2BekYYnbzzl-43JB7KhmgNdRxO_-qWwOF82kKOrk5KRUY3ZlwLWHLQANINFYzTk5KG5Uz7KpWmhbOU529qsAwygOQ9l6QWLTArWMgjZ1KUe3L_Ng5QhOs-zr5bSCvzm4ByHF3YTw8pdOE84Sd5RTf2goP0ZYk8FaoNijucXaEik26hNkCdMLUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شاهکار نمایندگان آفریقا در جام جهانی ۲۰۲۶؛ از ۱۰ تیم ۹ تیم به دور حذفی رسیدند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/664152" target="_blank">📅 08:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664151">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
واکنش صفحه معروف «ترول فوتبال» به بازی اتریش–الجزایر: اتریش ایران را حذف کرد/ترامپ و نتانیاهو از همه خوشحال‌ترند
🔹
ترجمه عکس: وقت اضافه تا وقتی که ایران حذف بشه #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/664151" target="_blank">📅 08:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664150">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaab0cc766.mp4?token=g3CLhttBwtN1ElpZekXfZKsgrkMba_q7inyBfe1oCLWqHX5Ku1N7iEHhb_QwJv1Ci9F6HkJoiK2BEyMqp4MF10WICJBYnjILQrIOfwCMJhyGNic2h3kl-nlj19fCCklzJy0tr91GoZt8mktXnvIp4lxhA3z9K47WTp8avlB-gLAWbpG_VMQCXwaFdJE9taGn1gl2sXSoZk8VKx6mhua-7XU17sB_WnEVb6bR-Qmy89N8kuP8gq33LFLa9fXQTpmlKaj6BqNS_AHCMN6LZL_i0iv8sd-aLlvzBmjxfDm44pXr8JPuTGT3rMXGZt2wnCkUZM3fepw2zniT1lSQdxV22wuyyogArbWSnBk7Ja06a-yVaA2H_t3ATzXlCL-jzqF-da48PTZK1n9S9wtnfkjW5Ue8wzlyj8CCDKSwktdwjU5vyyhE1paznrw3ZotJC5gtS0WiegG-t_d5zwm8VhKT18VliGlyL5bKbts6DFSX8QoJnwZuh9OyOftonVaDdvxAjFpeLEWnf5XAkud7W7LTySdGBgDchzsNvqlrgMhCP-cHtynOS7zH2rHzl3723fWDUq8RVB__CKwQvIfdlPyorscxtZq6UacgsAEVOPxTG3x_Yhw9LX7xeSnOKADkHyzlT3gtheBYwJ9hhyYhwQHmQmw2NHohhbXyYvOdnMRG_c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaab0cc766.mp4?token=g3CLhttBwtN1ElpZekXfZKsgrkMba_q7inyBfe1oCLWqHX5Ku1N7iEHhb_QwJv1Ci9F6HkJoiK2BEyMqp4MF10WICJBYnjILQrIOfwCMJhyGNic2h3kl-nlj19fCCklzJy0tr91GoZt8mktXnvIp4lxhA3z9K47WTp8avlB-gLAWbpG_VMQCXwaFdJE9taGn1gl2sXSoZk8VKx6mhua-7XU17sB_WnEVb6bR-Qmy89N8kuP8gq33LFLa9fXQTpmlKaj6BqNS_AHCMN6LZL_i0iv8sd-aLlvzBmjxfDm44pXr8JPuTGT3rMXGZt2wnCkUZM3fepw2zniT1lSQdxV22wuyyogArbWSnBk7Ja06a-yVaA2H_t3ATzXlCL-jzqF-da48PTZK1n9S9wtnfkjW5Ue8wzlyj8CCDKSwktdwjU5vyyhE1paznrw3ZotJC5gtS0WiegG-t_d5zwm8VhKT18VliGlyL5bKbts6DFSX8QoJnwZuh9OyOftonVaDdvxAjFpeLEWnf5XAkud7W7LTySdGBgDchzsNvqlrgMhCP-cHtynOS7zH2rHzl3723fWDUq8RVB__CKwQvIfdlPyorscxtZq6UacgsAEVOPxTG3x_Yhw9LX7xeSnOKADkHyzlT3gtheBYwJ9hhyYhwQHmQmw2NHohhbXyYvOdnMRG_c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبر این سبک از رهبری در جهان پخش شد و امپراتوری‌های دیگر دچار وحشت شدند
اما چه بر سر کوروش کبیر آمد؟
👇
https://youtu.be/koNYR3vumHk?si=VqAO_YcToXpH7tpD
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664150" target="_blank">📅 08:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664147">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14dd014a5.mp4?token=txWSjGpM1RhvgaYApxWiIsYV-yhUndNTuy9xnyHyAlcbUKIciJUqv_LrWTX37BNuZARFFw6eEJLmzv0qp5MXpw-O0IgkkQZ5AG77RZwA0YZ8S9vKOfD-cuVeQhQUw5zyBlURGqT3VLxc_51Z-IW7TGIet7VO_xRnAwG8ycmutL13bhESBxvVUt1-fhqKbL_bSBBWR9s5A1EDqWSnvQSzA_tyzToMNiVOx0J89vIDpUNrA2CpKrMm0B6U_3V_zkk4wF7NQdAWJ2Pf5yp5TPR5fDY9bKYsshw-rAdLsVEmX-nM6E9MG5K9ptNTsugInwMbDphsUoep-iKpBCDTuLRV3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14dd014a5.mp4?token=txWSjGpM1RhvgaYApxWiIsYV-yhUndNTuy9xnyHyAlcbUKIciJUqv_LrWTX37BNuZARFFw6eEJLmzv0qp5MXpw-O0IgkkQZ5AG77RZwA0YZ8S9vKOfD-cuVeQhQUw5zyBlURGqT3VLxc_51Z-IW7TGIet7VO_xRnAwG8ycmutL13bhESBxvVUt1-fhqKbL_bSBBWR9s5A1EDqWSnvQSzA_tyzToMNiVOx0J89vIDpUNrA2CpKrMm0B6U_3V_zkk4wF7NQdAWJ2Pf5yp5TPR5fDY9bKYsshw-rAdLsVEmX-nM6E9MG5K9ptNTsugInwMbDphsUoep-iKpBCDTuLRV3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در ایالت‌های یوتا و کلرادو
🔹
آتش‌سوزی‌های گسترده در ایالت‌های یوتا و کلرادو آمریکا موجب تخلیه ساکنان و خسارت وسیع به اراضی جنگلی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/664147" target="_blank">📅 08:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664146">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdNMwae1MUrs1uE8JOicfvAnFyByf5ELgMYlLvavYaxFJ-sRj_VKWTlKburUAeOzrMxdYoT5P2GA8XC3D4I3Bn8CfqWAlwp-_XdWbHfY2mUxTlrIimbdXmDIo4JVyR8OeGgkAdqsTVfx3sWwEKBgp-q4t0NYZPSQGhX5kgbFq00yAaZE1lF4YOxi_OErXQkYObEbZMhFH7q0IfIHWR_ZM0FFA-sleWJXosgfMdsArpU5b-rSB3Ep4y6KmF0PT0yxiHo88xf9S3pdyCy4JPCRwB7ReWJdBuUssGOE9ogppqCjm76MWDzYoRHCdpLLlVlXBt61VAfyTVOMfm1KKzynUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر انتخاب تو، نتیجه را تغییر می‌دهد
🔹
هر بار که یک چراغ اضافه را خاموش می‌کنی، شارژری را از پریز می‌کشی یا وسایل غیرضروری را از مدار خارج می‌کنی، در سمت درست این مسابقه می‌ایستی.
#مدیریت_مصرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664146" target="_blank">📅 08:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664145">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPWWuYDJK8lj0Ra4wNmIGali6lga8iU6yfaH-yMs_hcslRfZe2an-BYcCLYSz9M1DpnWwF79DI5d3mjIoA6F9XCVHPD5GbAy2ew7v6Qbz9ssBpNVqBdtylVnHQGNZ3yPLKSOp_7nFui3RCVFVeyQU-h5q1A5uFdCQutzVSoKbFxgOkcoI1cc1qcPF8vN6s-KC9YBMF2ESwLxIbBIJTYui3-3kC48hcKpnamururtNPkP1MADnrycU4QGu3buZolzghIHWlDtRJH9Kqd5wR3h4L51Vnc__ic5a04U_clGMMIOC7bVz3WLWnpDQ1uVIW3_P0sLdKia8PmvQes6L_nFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش کویت صدای انفجارها را تأیید کرد
🔹
ارتش کویت در بیانیه‌ای اعلام کرده که صدای انفجارها در این کشور به دلیل رهگیری اهداف خصمانه توسط پدافند این کشور است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664145" target="_blank">📅 08:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664144">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7--OHewzzrCQhFUhs4i-SgdJi-RqqRdxUWHyRgLdzanYzdiykp-3Fsxq_wbom3ah1GGHm77QlHliiVjLNhSOELmIBg9AvivZ19SV7loOXsT0oHBzIL5kWzeKtiheiAJa6PZa6PeFPRy91LCWVe--K4LNXbg6nwmyCnv7ILlviQTSjnWewSf-dXNLKd_qEXE0g7y-7Cnj1iENGG8ssvG4Em3gGhFfQupTlshS6NHNEnZE8-dmT8oxCcrH3MhPZNovz4KsF2j4UB9kbImiE4AyMIdwdSEuRAwUZSI2KTAOcm_WVwltV7pdX3wkaeQiwQ2XjiQU3zikuiCnk8w96i-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش اکانت ردیت به مسابقه تعیین کننده الجزایر–اتریش: سرگرم‌کننده‌ترین «تبانی» تمام دوران!
🔹
گل الجزایر در دقیقه آخر بازی!! باورنکردنیه.
🔹
اتریش بازی را ۳-۳ مساوی می‌کند در حالی که واقعاً زمانی باقی نمانده!!!
🔹
الجزایر و اتریش می‌آیند و می‌گویند: "هی، ما مساوی…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/664144" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664143">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk2_-xYMMneYYY4Kl9tpzOsZtxzfVsdzrGGbGN6HvF7hN1pJEJBNZjWg50JqDiLUKDadisAuCtSw54WBh5FALW-IeioDvv_4cmL7KvuCKleo_OTC0Qay2YUkmFt3mFrQOcjqrsDCa0sIw0iR_zP5-wvszVwcP-EQx3WJxs28IjXGDw9zowFPBiUIQS41iu8AElCiIbNsS8P3B8Df6Jt0cs8CrYPolbuNMn3tCTHVmUH1fbTKIG6b_Y7HPOA-kt7Zn1aFHOkVnB7Ku-V57Xw2iFVtM6o_1MSppTUViFIEus3zU5eiZFu8hMM3CjwVBW7_mNKIJ366eQ7EEbcEVun6wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخی گزارش‌های غیر رسمی از شنیده شدن صدای مجدد انفجار در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/664143" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664141">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453496b501.mp4?token=Kekt7D5RU2JdlbaSjMZh-R1g0tGhJLosFyLx60UgMwehezr_DZWzN5PvZM-rvklzlM6TwDRWitkT8qMziooTenFq1BDxRR9_fvCi_jAvTcsbbMEP8JF4PbnKftC9UUyKVhFrCXL0VJC1i7eEX9NZEw2IsFPRALzXVo68osWaHHUwamV2ZvcI59xfSVb8ifrQjWi9ywl03xgLoCnQDhvVfZTJry0Ba2o3QodL2E7-KxjMBEBeo4VB_UicdDKteXJsCTBk9NbgJ4jZ4VDD81XDiniQaCj6qwZUl2t6HOrHhRzANqCpf-CudEBAyFrRYoc-oByKngEHWDlbguU-PSIk8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453496b501.mp4?token=Kekt7D5RU2JdlbaSjMZh-R1g0tGhJLosFyLx60UgMwehezr_DZWzN5PvZM-rvklzlM6TwDRWitkT8qMziooTenFq1BDxRR9_fvCi_jAvTcsbbMEP8JF4PbnKftC9UUyKVhFrCXL0VJC1i7eEX9NZEw2IsFPRALzXVo68osWaHHUwamV2ZvcI59xfSVb8ifrQjWi9ywl03xgLoCnQDhvVfZTJry0Ba2o3QodL2E7-KxjMBEBeo4VB_UicdDKteXJsCTBk9NbgJ4jZ4VDD81XDiniQaCj6qwZUl2t6HOrHhRzANqCpf-CudEBAyFrRYoc-oByKngEHWDlbguU-PSIk8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیر تکامل بازی‌های کنسول (۱۹۸۲ تا ۲۰۲۵)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/664141" target="_blank">📅 08:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664140">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5W3AA46KYZcHHgrJXCItLByQDo9gY9Lxk-5fHR4CtXGFwhfuptQig4b5k6l-RGGUx5CNiJQ4Cz4IKrScKIMXAzKvNHXCbJ0BaDHklhgvbp-YsgMGS0_vvy6_q_Nx5bLR28BxpR4JSMztW2L5e4X2kxP7oXAWgxLGPBLaSq9zy5mqmPzIiiZaJGjZIU-F0Cqi1EKElMCLEubvIgzb0u5qsU9KPQeu04g8P3p1C8Bclvx10Iu789I0D5sQaZg5fVEsEQZwp3DdztYxqysI3ppDnVD89cG55gaqIPZCLdYgdGZ21qGDdTs-WNAzd43D6Q6p8Xzl2FZdhz3mUWiXCdTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز تحول بزرگ در کریدور حیاتی تهران - بازرگان؛ بهسازی آزادراه‌ تبریز - زنجان پس از ۵ سال انتظار شروع شد
🔹
رئیس سازمان راهداری و حمل‌ونقل جاده‌ای از اجرای برنامه‌ بهسازی و ارتقاء ایمنی و کیفیت خدمات در آزادراه تبریز - زنجان با پیگیری‌های مردم از ریاست محترم جمهور، استاندار آذربایجان شرقی و به‌ویژه نمایندگان مردم تبریز در مجلس شورای اسلامی خبر داد.
🔹
رضا اکبری با اشاره به اختصاص اعتبارات لازم برای بهسازی این آزادراه، افزود: هم‌اکنون عملیات بهسازی این محور با فعالیت ۶ اکیپ عملیاتی به‌صورت مستمر در حال انجام بوده و دو اکیپ جدید نیز ظرف یک هفته به مجموعه اضافه خواهد شد تا توان عملیاتی و سرعت خدمات‌رسانی افزایش یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664140" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664139">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان وارد قم شد.
🔹
عراقچی صبح امروز یکشنبه برای انجام یک دیدار رسمی از عراق، عازم بغداد شد.
🔹
نخست وزیر آرژانتین در پی اتهامات فساد مطرح شده علیه وی از سمت خود استعفا کرد.
🔹
اسکان و فعالیت‌های تفریحی در حاشیۀ رودخانه‌ها و ارتفاعات مازندران ممنوع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/664139" target="_blank">📅 08:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664138">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUU7wX8UImfLrqdSMUif3q-8SrplP_9XECLYIdYj8OPjmPYeIB6RzFBtKY4sRXwJaW-2a4QfkldrZLbHMcQba0w9zAXFWjeISe5iaeG1o_NvfFDOZSmxZhTe-j88P66xGiEotACAdsUO2lurCFm-vgyhZHJW4zfi4pDFt1rmtgVq11BDgf3LbRlHAWrTXN1vHt1LJiDWvEZLLJFflgvqwHaoSSfsYhaiyDFJHaCpWvj3bIXiIQYfrAJub9eaSO0BvdsyRakYEuhRBCBTqWVR94FwO7xmiZGZBRl60Ecja63f7Y_4fa53YKyp4kwhWXLn7200V2HoWdO4i3uRbF6FTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرز تهیه میلک شیک توت فرنگی تو این روزای گرم
😋
🍓
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/664138" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664137">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFz7FiIfulKMJkP68vfSGG_suefogrjsye3MES2o43O4Sy7SUp7w_lHqKrz0ViDaMuZqU1nUYRy77H-ydmROR3potY6lkR2DnIfHOHqPV--yUN3m_XS6CIIfjTRu1H5YZp0Jon7YP3LwoKU3ueMEqFd1Y-VaQvrRsWCzczRQ26blA87Ij2AOxsceMYLp5HNSiNzYlUR3ojVsUSE91emETOn5g1QdtSt21KELuk-o6y9ZY7_ecw15fAicUwlyp0hsQDe6KSD7bWZgV5GWoRoPBcCtQ40cASTwNibLGxCtcfzf9gGXBmu6LCeDpxx5t3P5bVyeATtbxOPrAoiVMQlZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت خارجه درباره نقض مجدد تفاهم خاتمه جنگ توسط آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/664137" target="_blank">📅 08:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664136">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97dfd0c359.mp4?token=YDzHmLAmZJZ3GkcLqu67AWLpO0PI7uDXn07tqj_oHCbIkCXAjcT--Kf0g6GWUSFmdVfHdqFbTZUrTnnNccLm0gj6DscQUhdkEgEIAxEJEJbdZwj56V4EpmdZcRRId-4fuOSkJa2fRcdv2UOePGSwhHRVW03snUas9B0LQBgRaBuERbgDp5ohcwDSMxkaR1SLgtMuc0ZcVZrElFb9Ka5q9-S8jrcRtzPBEl49ay3DPScTVzvzCrLnltYAKM-sXO2O2p64itLDPfHNd9uzO4Yp1rkpJElnrGhvJr6AXmtBQ58JNgTeVeqx_DRlRb6BscZDYZJxl48_Cl_Jyv7N0wKDqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97dfd0c359.mp4?token=YDzHmLAmZJZ3GkcLqu67AWLpO0PI7uDXn07tqj_oHCbIkCXAjcT--Kf0g6GWUSFmdVfHdqFbTZUrTnnNccLm0gj6DscQUhdkEgEIAxEJEJbdZwj56V4EpmdZcRRId-4fuOSkJa2fRcdv2UOePGSwhHRVW03snUas9B0LQBgRaBuERbgDp5ohcwDSMxkaR1SLgtMuc0ZcVZrElFb9Ka5q9-S8jrcRtzPBEl49ay3DPScTVzvzCrLnltYAKM-sXO2O2p64itLDPfHNd9uzO4Yp1rkpJElnrGhvJr6AXmtBQ58JNgTeVeqx_DRlRb6BscZDYZJxl48_Cl_Jyv7N0wKDqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه فول بادی بدون تجهیزات #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/664136" target="_blank">📅 08:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664135">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUrSAjOYuNBz4DPnh10L6X0rh5jJVlDcalAz2CsHH0J5Vob4jLwZGlQpkJn9GDEeBH2hmJLXZbD5WxHKM7y4T7jTeRy9fSuqMCqUEwT6nRkhq2QZAg6rKJrXeqjkNy1yj9EBmBtAJ4l-a_bJIdy3_XiRMp_i1HGF9FdloaA3EX9dYopmyEkmxvsO6oAqo26jIH7uqIVaBOTBk9g3C2Pj1d34ptINfEeIfrk6aTe2HsS2W6c4F6oX-dtyXY-P4TNsjUCWyghCWVHKON5liuazcQzj1pJLrt0DaANiYDhuOH_jQEU2vTp8L0UEdnoyvy4O9bahyX5XxkBCYkHH6YencA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ایران و تجربه عجیب‌ترین لحظه جام جهانی ۲٠۲۶
🔹
این یکی از باورنکردنی‌ترین و دیوانه‌وارترین لحظات تاریخ ادوار جام جهانی بود؛ واقعا فوتبال است دیگر!
🔹
هواداران فوتبال ایران در سه دقیقه پایانی دیدار اتریش و الجزایر عجیب‌ترین شرایط ممکن را سپری کردند و در نهایت همه چیز به ضرر فوتبال ایران تمام شد.
❌
دقیقه ۹٠+۳ حذف ایران
✅
دقیقه ۹٠+۴ - صعود ایران
❌
دقیقه ۹٠+۵ - حذف ایران
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/664135" target="_blank">📅 07:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664134">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQLX5biCQoZ6965xipdgivdVvwoQN1c9HXTpEOlG_CbmapfVoluoKoE6IMSlDCv--0MRphrs31auprMLhkzyWArMBnHDUYDZsGzh706GrFX_PxQFXvfBIeeHnlI1K1zGRx9KigHP3Elakj-YVjh_4Wwz0m1Z6oCz_vIQc3cMZNPtdQZiiqpgpP5b35CKlletZfM7Am-AulZOZEcY6MrtXDcOVkHVmJOoUtNAywxPQ-NBjipYlcmJu5RfdnfctQssMlvbPyWXyiSccWfpMtB3hklidqQ0YSSz-IDoIgcKdywTxhOmf-kWyqrUjMXYoPPvnpFOBu6cTHK5m2JlU4z53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ساشا کالایجیچ کیست؟
🔹
بازیکنی که قبل از ۲۵ سالگی دو بار دچار مصدومیت رباط صلیبی شد ولی به جام جهانی رسید و با زدن گل سوم اتریش مقابل الجزایر، شاگردان قلعه‌نویی را از جام جهانی حذف کرد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/664134" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664133">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3XVGbnXjiXSwR-s3XmPE2QN7y6aQMI27oa60OzP22rSqjS48jV9NluxeklqrDBskjM065M6VGJQncjcGsxE7UTalTmF3rJw9vJ5sGyTAEi1c2I2EwfLn6-TIXOrTB4WYJB8H4ByRsS85iLOWugfDXLe9U9bd83lADXQ25JT4uiLnbgKH7FYlPDUs_lUK5cJDzqLO-j-_4OK6nurqpnQQycH909jW2eLFf9PDszWaH5IFnaw5X4Z28B6U52rH9iD2pVTdDczPVTToIfB5AmlBmwmJDUHqXq3pAdrHbRfpENbDOWlMV1rzwm0io3xXdHkha9YcjB2NbZZVcHQAn_9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقسیم سهمیه صعود بین الجزایر و اتریش به عجیب‌ترین شکل ممکن/ آخرین برگ شانس قلعه‌نویی هم پوچ بود تا ایران با جام وداع کند
🔹
غنا مقابل کرواسی به پیروزی نرسید
🔹
ازبکستان مقابل کنگو موفق به کسب برد یا مساوی نشد
🔹
بازی الجزایر - اتریش نتیجه مساوی داشت
🔹
تا تیم ملی…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/664133" target="_blank">📅 07:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664132">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: زمان امتحانات نهایی تغییر نمی‌کند
کاظمی:
🔹
تغییر زمان امتحانات نهایی به‌دلیل ارتباط مستقیم با کنکور امکان‌پذیر نیست و امتحانات پیش از اربعین به پایان می‌رسد تا نتایج به‌موقع به سازمان سنجش ارسال شود.
🔹
اگر تخلفی در چند حوزه رخ داده باشد، قابل تعمیم به کل فرآیند برگزاری آزمون نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/664132" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664130">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeZyrBYf2xPoVUczXp5pP_6hUk7rqDfPquPTGCP-RAg_Ndfbg34CYORzsjWF7HQh5DC66TqJ0a3Dh7fk725AuIwWwe4pzqzCPrvuYHdPcDFybeGMTu-sCNUd3uvI7AGVVVTkAFbFz7RCCx2HP9uQzOgczgwFR2xYBeJpve_9G9TOVwIBQKOxuJW5BkbH-_dkgmS1ifMfRWKEQfycCnVPEnelT5W0AqXKdcPyMEpJoOn-W2T1fbQdtfgHx8NSsMn9oI0y7BBgOUsbumprb5WmWE4I2C2vgXIqNgkn5rYO4bVrWzwUdB7tXciv1Cjt2novtzPzgbsW8bCuGWo11gE8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشه «آئدس» در شمال و جنوب کشور؛ هشدار وزارت بهداشت درباره خطر گسترش تب دنگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/664130" target="_blank">📅 07:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664129">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeKyZ2lOcAOI5ljdnEZ45UQBApJNFBJwRa3yYbdnQvP8AMK7Gg5dkF1TfLHt7kM3gjq4sShNmmTI36YB4o6tzzcn1bpnHkdVUDH_Sn9OJxxLfj7uqDEaCmArX5oCtw8aS09GytZLYsSzseZ9mDo6jm_Mv9a2pwPc7qzpXluysDFIylU2jNsgCXoMKXCjultNO9cY7h2PsTBUfCX1pKu_wKhJthjO6NjtnIPW6rLmmbTvkQoSbVhZ7sqdJCjHNvto_TUV8xqlSoDEj_dYugz1cUw8am3PXToq52uh1QsrJfvmnmp3eyq9D9uANq2csEdPZpp2QZoA-18OsHjEKX7BdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی ۲۰۲۶ پس از پایان مرحله گروهی و مسابقات یک‌شانزدهم
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/664129" target="_blank">📅 07:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664128">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏆
خداحافظ جام جهانی، خداحافظ آقای قلعه‌نویی... @AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/664128" target="_blank">📅 07:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664127">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXeSVXVscUnQJAhmNU2pAIKoay5EtTYhRq4Fjv2efYePMnpSbubpCXKcWRkNCS9DSHGHEteuUz5PI3AIBBH8mbzdRdOfkpVJ9KBizXnvfGM8kcVEapqIL4PHhra3SwREA1CBkuVz04_I1KLwy6RSpqCPScIcmkagA5_W97ePxZWuMb7s587JtkBVuaEs21iBR8d2xmsfSfxDdjVUv7K252PuOqjCrEQjQVBwic3ZfrAX2xDehZrt0NQ5by7jI8x3cwwYceVqsD2DkhIFaElpPNcnTwjqALZ096cprQ7GAM2d7S9pDwg1EVpQ9NaVKj4KVi0yFSoTpV_4vYEVPwqmMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خداحافظ جام جهانی، خداحافظ آقای قلعه‌نویی...
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/664127" target="_blank">📅 07:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664126">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2dVjuL_ulndgoTpu5F5FNvizqWj242qc5Kh-oufI6lMMT4sHRwyWiU9822eYPusjAv4_1uuHYF-wlwemood5Brr397T8HxRmKm959Gp1X-Fk1qhTZz-_VgLnXRIVtzSidN3-kYD6l5cCJjyh8gtHCpLER3Y_cRd41uneEdIV9n1Gk-_CuEO-cojdsEUw8-8V4_BA0SStkSrITihkbD1C1UzQQMhojSxN0ksXkltOG3YAAPkFcLrlRke3KNQ4sWuvAad5gUB9Rsc2mAG_cbdrG5KG5Fa2jqUWZyrFUV2H_p0VJI3EhyCHyrCZXN5ptYrOD2lPd8onx5EzmEk4X-1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۷ تیر ماه
۱۳ محرم ۱۴۴۸
۲۸ ژوئن ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/664126" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664125">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ایران در عین بدشانسی حذف شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/664125" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664124">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">در دقیقه ۹۰+۴ الجزایر گل سوم خود را زد و ایران تیم سی و دوم بود که در دقیقه ۹۰+۶ اتریش گل‌ تساوی را زد و مجددا ایران از دور مسابقات حذف شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/664124" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664123">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گل سوم اتریش در دقیقه ۵+۹۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/664123" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664122">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اتریش گل زد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/664122" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664121">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">داور سوت رو بزن</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/664121" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664118">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الجزایر گل زد
گل سوم الجزایر در دقیقه ۳+۹۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/664118" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664117">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گل گل</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/664117" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ثبت‌نام کتاب‌های پایه‌های ورودی اول، هفتم و دهم آغاز شد و تا ۱۰ شهریور ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/664116" target="_blank">📅 07:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجارهای جدید در بحرین و فعال شدن صدای آژير در این کشور خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/664115" target="_blank">📅 07:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664114">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجارهای جدید در بحرین و فعال شدن صدای آژير در این کشور خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/664114" target="_blank">📅 07:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجارهای جدید در بحرین و فعال شدن صدای آژير در این کشور خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/664113" target="_blank">📅 07:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
گل دوم اتریش توسط سابیتزر در دقیقه ۵۵
🔹
الجزایر ۱ - اتریش ۲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/664112" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
گل اول الجزایر؛ دقیقه ۴۴
🔹
اتریش ۱ - ۱ الجزایر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/664111" target="_blank">📅 06:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664110">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
اتریش ۱  الجزایر ۰  تا دقیقه ۲۹ نیمه اول @AkhbareFori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/664110" target="_blank">📅 06:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ترامپ: هواپیماهای آمریکایی انبارهای موشک و پهپاد و ایستگاه های رادار ساحلی ایران را بمباران کردند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/664109" target="_blank">📅 06:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664108">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اتریش ۱  الجزایر ۰
تا دقیقه ۲۹ نیمه اول
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/664108" target="_blank">📅 06:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گل برای اتریش @AkhbareFori</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/664107" target="_blank">📅 06:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گل برای اتریش
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/664106" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سردار حسن‌زاده، رئیس ستاد وداع و تشییع رهبر شهید: روزهای ۱۳، ۱۴ و ۱۵ تیرماه تهران تعطیل است، روز ۱۵ تیر کل کشور تعطیل است و در قم ۱۵ تیر و روز ۱۶ تیرماه تعطیل است و ۱۷ تیر برنامه تشییع در عتبات است و ۱۸ تیر ماه نیز در مشهد مقدس مراسم تشییع برگزار می‌شود…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/664105" target="_blank">📅 05:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPqeHkng956hDymDXWfRERztLvB3YO5n9Usxd8-9mhs9ufcWtCxBSZ9jugQg46IEcwIJfuFsezUGFNAQS-UNy-B2yUo5XDwYosFLDS-5CNiE33WIWvssOpDjtX5YzxHE8ov0zzHGLTQ5gEqxn8_F1Xnr7hzNsNXTlPYINPAIKK2UhnN6i8SoF2nFMhMqR16TyBd4Uuag8XR2BmrX2LaXQw1ZEC8TseKRn8WsAVLa6Qi4AQHoUYJitpigAq0ceI-soewmH1uIJRpa_hFLu2uAqGhSFTYOAZQ_eJsxWZz2rlvNEHvsPuEl9awSktLfRrhR3fmzA_mn1YJMahG0e8VGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کی‌روش برای صعود ایران کاری نکرد؛ پیروزی کرواسی برابر غنا #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/akhbarefori/664104" target="_blank">📅 05:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
منطقۀ سبز بغداد بسته شد
🔹
برخی گزارش‌های تأییدنشده حاکی است منطقۀ سبز بغداد که میزبان مراکز دولتی و ادارات مهم عراق مانند کاخ ریاست‌جمهوری و کاخ نخست‌وزیری، و سفارتخانه‌های آمریکا و انگلیس است کاملاً بسته شده است.
🔹
میدل‌ایست اسپکتیتور با گمانه‌زنی‌هایی…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/664103" target="_blank">📅 04:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664102">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBZkUorKNrnix7ET6gVzb8ePq14LdVLoTKy8MBta-sWTmmJQUGx0RvDLI2BmW3VPg-iWfJmVjbaPq9NOvCIy9YI79pkJ_zaLHeEovMfrMSErS2iuXTkyXz6BnPpO5lN_Lj6vtHE1Ui62exBC1aH_PxlHiAVyf6WiygIutODBk34DMPZDli3THW4L2Tk4faH2wSnKzyf99ekrNvv4nsLUfkI2I2MEdncAksljWCDDbcs_vLFe1fGA1rFabFjJw6DDcMI5P3KvkaxfcgXl7QkCoksaKXY33HCAiDqx00nk8xw7OapvcZOZiXc5iH6hGP6liXkpxGzxHYKFX8-9hh1mUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی سپاه: آمریکایی‌ها جهنم را در این روزها تجربه خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/664102" target="_blank">📅 04:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664101">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c935e2c032.mp4?token=oCUCmEc2gvqqPT7AaZJuxnOGBCk21CH2YJ97qZ7gOESuMpjPdUI6kuwZTBqfMNzRbGO3H2F4WFP7Yxq_S5NEP1hkzn7u3Y4ydaRq1TKLv3RINUBL8dG5TeSOlflXdw7sMntveUhiSkDjT1qQX7eKldrPjjDU6a-jWq1b4rFLaGBt6gQB8o27ZJo8gwwZfdcy9muo3HvZwxcKu4DXSJzyL3l9l_DMvSU7C6oxAZ4aEyYYAC3NW6fAwKTcbCVLftou8GQNdEJ2nTIstkeCD7HEzCvKEeAr7wOTUVKmLtlOppR1Slpgz0aza9ZFmmjhgGD0k2J_lmLxyF34MVr_VxFflQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c935e2c032.mp4?token=oCUCmEc2gvqqPT7AaZJuxnOGBCk21CH2YJ97qZ7gOESuMpjPdUI6kuwZTBqfMNzRbGO3H2F4WFP7Yxq_S5NEP1hkzn7u3Y4ydaRq1TKLv3RINUBL8dG5TeSOlflXdw7sMntveUhiSkDjT1qQX7eKldrPjjDU6a-jWq1b4rFLaGBt6gQB8o27ZJo8gwwZfdcy9muo3HvZwxcKu4DXSJzyL3l9l_DMvSU7C6oxAZ4aEyYYAC3NW6fAwKTcbCVLftou8GQNdEJ2nTIstkeCD7HEzCvKEeAr7wOTUVKmLtlOppR1Slpgz0aza9ZFmmjhgGD0k2J_lmLxyF34MVr_VxFflQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منطقۀ سبز بغداد بسته شد
🔹
برخی گزارش‌های تأییدنشده حاکی است منطقۀ سبز بغداد که میزبان مراکز دولتی و ادارات مهم عراق مانند کاخ ریاست‌جمهوری و کاخ نخست‌وزیری، و سفارتخانه‌های آمریکا و انگلیس است کاملاً بسته شده است.
🔹
میدل‌ایست اسپکتیتور با گمانه‌زنی‌هایی دربارۀ دلیل بسته شدن منطقۀ سبز بغداد نوشته مقامات عراقی، مثنی السامرائی، رهبر ائتلاف سیاسی «عزم» را به اتهام فساد مالی بازداشت کرده‌اند.
🔹
او یکی از برجسته‌ترین سیاستمداران اهل‌سنت در عراق به شمار می‌رود و در پی این بازداشت منطقۀ سبز بغداد (الخضراء) بسته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/664101" target="_blank">📅 04:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664100">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا
سپاه پاسداران:
🔹
مردم عزیز و شرافتمند ایران اسلامی؛ فرزندان غیرتمند شما در نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیرماه، با پرتاب موشک‌های بالستیک و پهپاد به‌سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی‌السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آن‌ها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانۀ مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
🔹
براساس تفاهم‌نامۀ اسلام آباد ترتیبات کنترل عبورومرور در تنگۀ هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
🔹
دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم‌نامۀ اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/664100" target="_blank">📅 04:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ7cHD3sa0S7DnvorEgTzj4K_b-15x2W2aaJj66iymQi-6iD081uCWfkwKd_DzgF-TIWSkC57yHoJdRSm_5SRcBZqGW_4y-ZcTLraFxjpUIdzXDSbu1bB4L-HMeIP8Bmzd7miv5mOvU2B0WMH0-k8AT_dmxUdtfiSwOHPSXFQnzbyWR32-lepLrslVEDSQUF5rpyKSky93WlCYdOROHcrO3UaAI8jDIkNyvf2Q4XvUpCMyf6Hc1ceF2vTZ_jqwfjCcGLUCeVfzJMglHPWU1QSWM9_Vp2GPCEX-ccCQ4p_FRHRKkReLkhIZAsaqNS9D5B3KijtZJDgYmKJxnJeZEiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کویت
🔹
گزارش‌های تأییدنشده می‌گویند صدای انفجار در کویت نیز شنیده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/664099" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664098">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین گزارش می دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/664098" target="_blank">📅 03:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664097">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqHD0OIKcSDEEs0Vb9pu8YxaL7J8-b06NVXMFA3R1pI8cnl_v34y8I7uyO224USoD8VUNmDRIMbPz2TIXmzA4YGWgo3bgzMe2Z7ahpB4DyFoQfrzCuQeqyhl3rVzn6EsYNrZGmj2ILA3qwga7tYmdGxzmtw0RIl2nEzd7u0nax3ozyRn-WpRkrxAZnpGTCN80JRl2C3rIUG7YOI7OmGma-I6EsMb_L1JgkT50BH_VzkGWnOS5822GUdGkb3uR8RvDH1St-ozNyrNRvwBd-tfVczuzkFYl25rY2T7KXqnLyD4x6-hW-MElHIR-LbuSYIEsTs9DqrQDhXkd_utKrKlhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: هواپیماهای آمریکایی انبارهای موشک و پهپاد و ایستگاه های رادار ساحلی ایران را بمباران کردند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/664097" target="_blank">📅 03:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664096">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ترامپ: هواپیماهای آمریکایی انبارهای موشک و پهپاد و ایستگاه های رادار ساحلی ایران را بمباران کردند
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/664096" target="_blank">📅 02:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maLg3KfRN2mxvoNoWDfx809XPHb1EA0S0UR1U3R2FTAV2uWmI3LIbKp7QLFm9xftz2nRaeSf-o_YnCGNdTgKR88o3Y07MRGXgJ_CLS6EPmzalbOWZjeEcuTTrz3cFe7Z-ontoooMCbPmigu0oib1ibtXd115Gs0TOchU-26Apxl4_k9NvDVnli6FV8ZrRuOnM1p_Xu3XezW1I1kT30Cc19RAE7YbIZlvQOMSDVQZOJ2Ay23Iu0NwpRME2dRuoe_YQAuZySh3lb4JHtNwTkAjh1zRLWwpLvdlnVdJEnGTgAUaYM4BKZyV77tK-MAVTveAnYSn6HghLbvONcRGa3A4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای قطعی شدن صعود تیم ایران باید ١ اتفاق از ٣ اتفاق زیر رخ بدهد:
1️⃣
. غنا موفق شود کرواسی را شکست دهد
2️⃣
. ازبکستان موفق شود از کنگو امتیاز بگیرد
3️⃣
. دیدار الجزایر - اتریش مساوی نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/akhbarefori/664095" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرلنگه و بندر کنگ
🔹
گزارشات مردمی از شهرستان بندرلنگه حاکی از آن است که صدای چندین انفجار در شهرهای بندرلنگه و بندرکنگ شنیده شده است/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/akhbarefori/664094" target="_blank">📅 02:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664093">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe4ff472e.mp4?token=c4MvCl3lt7bCS4juBVE1rWriQappZ9tWH6RvhLE5k7xQRJDXHyhYD-cOieFLqVAlxLdJyY4NdHRglhZtSyeRo0VpazxXQD14lSWr5id-01oh7ExnBI1FjyJwB_PpUdcRoIk6apPeoRno4snyjEWq3R94lu1M-zpWbSi_ro9LhGjDQu543yNZQksPQA9qPGt09Rb0UNrYMXqQ_fsLXy5Nuxlla_3kaR7zo4lY-3UJb_rpJuGWUXtxOZSl98xQgQHBOvvXXZm7CthQTR0aB0MlCpYpCOfZ5NxfY54te-s5-2433pQ01mTFKv-D0Vzo9JD4AkwXC5Yplh3hcEkrGmlexafAtijSJxOF-kcVwoOLJcyHSoyrhhOQ3eYhOE9_iSDNmV6fg7evz-OFmh1-9CF1p7SXuSW-W9nOwrUb73RlV5qKkEFj1cePy_E6ggylhtlUC3QQEmGWa15Lem9Kt-9hhcbVH-HSD34wYHEWy3wZA-sGFkL_Wl9idUd2KcPDbn1y9c88P0jbj-I-BbD_CrtNOwAzvJ8VeNDETWS3tfALRR23_EG1CC0xa6Fx6N45pb8lcilfQP7ysy2ZF9Gprrafmtr2aAqkDvPDlctW3ilWrMMsX1RTRBFAUUZbcTYZ39lJr35GWtAj5IsSrr1wltVJWuGU4m2Svy0ns_u5SyEjac4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe4ff472e.mp4?token=c4MvCl3lt7bCS4juBVE1rWriQappZ9tWH6RvhLE5k7xQRJDXHyhYD-cOieFLqVAlxLdJyY4NdHRglhZtSyeRo0VpazxXQD14lSWr5id-01oh7ExnBI1FjyJwB_PpUdcRoIk6apPeoRno4snyjEWq3R94lu1M-zpWbSi_ro9LhGjDQu543yNZQksPQA9qPGt09Rb0UNrYMXqQ_fsLXy5Nuxlla_3kaR7zo4lY-3UJb_rpJuGWUXtxOZSl98xQgQHBOvvXXZm7CthQTR0aB0MlCpYpCOfZ5NxfY54te-s5-2433pQ01mTFKv-D0Vzo9JD4AkwXC5Yplh3hcEkrGmlexafAtijSJxOF-kcVwoOLJcyHSoyrhhOQ3eYhOE9_iSDNmV6fg7evz-OFmh1-9CF1p7SXuSW-W9nOwrUb73RlV5qKkEFj1cePy_E6ggylhtlUC3QQEmGWa15Lem9Kt-9hhcbVH-HSD34wYHEWy3wZA-sGFkL_Wl9idUd2KcPDbn1y9c88P0jbj-I-BbD_CrtNOwAzvJ8VeNDETWS3tfALRR23_EG1CC0xa6Fx6N45pb8lcilfQP7ysy2ZF9Gprrafmtr2aAqkDvPDlctW3ilWrMMsX1RTRBFAUUZbcTYZ39lJr35GWtAj5IsSrr1wltVJWuGU4m2Svy0ns_u5SyEjac4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: جزئیات عملیات امشب رزمندگان نیروی دریایی سپاه علیه متجاوزان آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
🔹
شناورهایی قصد داشتن از مسیرهای غیرقانونی و ناایمن جنوب تنگه هرمز عبور کنند که نیروی دریایی سپاه پاسداران با آنها برخورد کرده بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/664093" target="_blank">📅 01:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664092">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
فاکس نیوز به نقل از یک مقام آمریکایی مدعی شد: حملات امشب آمریکا به اهداف ایرانی تکمیل شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/664092" target="_blank">📅 01:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664091">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
صداوسیما: شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/664091" target="_blank">📅 01:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664090">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk0MuynZa4kfDYc0xd0gAnXD1jE82JW9BBfaVdUXPtJ2-p9AyODjeLnkwzEssFy1TUc_yJG5qmkGnBE5MxIGOhP8KlE7hF3MgjFzbdYb23MTUlSRGPHsSwIk_Gcld5r9hYqUK6dMGskeKQUAd1FkHKUZNzp2rvJJGeAFTYN_ebM-PAOIxKW6TiWIkHCDTNELiCb2Dxv1rqH2xiVFbxHXFIXokMDD1EfeUZ0I37oVFyyex96I-Yad0X3uMHUWLYmOte_ezY0cppTd7U9ZD9afhlDmkiSRKT9pPwVdYwT8jub5BTLgCHkNXvD4zMo9guTooK_Encr8Uo-dSejhIIcAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام حمله تجاوزکارانه به اهدافی در ایران را تائید کرد
🔹
سازمان تروریستی سنتکام رسما حمله تجاوزکارانه جدید به اهدافی در خاک ایران را تائید کرد.
🔹
طبق ادعای این سازمان تروریستی این اقدام در پاسخ به هدف قرار گرفتن یک نفت‌کش تجاری صورت گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/akhbarefori/664090" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664089">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
صداوسیما نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/664089" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664088">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای خبرنگار آکسیوس به نقل از یک مقام آمریکایی: ارتش آمریکا در پاسخ به حمله شنبه ایران به یک نفتکش تجاری، حملاتی را علیه اهداف ایرانی انجام می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/664088" target="_blank">📅 01:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664087">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oujzmHV_obSAcGg0sxK2Vran_-dUJMwGKzeGV5_5w_qpHNgTGhq4sz1F-UE3Fc4wcYyUEn9fsgqdj_UtLtozZdbeYJs6zOWQ3g_kU6oe8K-XfDWWcos_EWXJK8x_S24r72Oc-IPLZzpNKQSwxW_B8zT2ZTorFf30_y-09s2MuViJpVrVwabQaASsfIlRtrHZkg_TUvXwUw857PhIOC6jyiXIXT6QA_obzi_wqmphk3HyDePj9u4grTiHpY27s2K1NVQVIEuEHKJzPdohGXlxQ4YRKPR3UkNdQYB2JtomoIeL8KAL9KNC36lUDZWS6aLCnqGO4ixCeD3YlK-aYCWVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صداوسیما به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/664087" target="_blank">📅 01:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664086">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در سیریک
🔹
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در  سیریک شنیده شده است.
🔹
تا این لحظه هیچ مقام رسمی یا نهادهای نظامی و انتظامی منطقه ماهیت این صداها را تأیید یا تکذیب نکرده است.
🔹
برخی منابع مدعی شده‌اند که صدای انفجار در بندر…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/664086" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
