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
<img src="https://cdn4.telesco.pe/file/hiiOJWVB9SfqKw1Ai0mSrK72D6XdCrmzjqUiE8Jj38KcSspaOFw1SWDLFL34tjoHkvkZ_otPIk7XusYoWU2Sted22OxuMQzCP8fYbEc7GH9h7kZ498dOh0QTXtBU3k4ROTlVoSZ6pDQ59NCGJjqwKCbfv6wiWsK1--NO56USlDd0YGVGY4Lgl0roxdyp-oxJ-0U0zfMjkiT45cGakc5cEfXkhsSje0yOBacCl2F21FuxeG32ufIQ5SOlYia3O7HnYeJ9XAsHsqCFyLDtHjnsT6pN3xDmmooCOyCrFnKwfrejOOgCoQneKv049lPW6qccO_4jQ8jItIhstRw9Q_T2rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-6810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVfzz3zVZAyCdzisESdoUtYb3Bf6vbVUgyDIGiJ5EEa9aVsArvEDiZjOt5TIdPgfZDcy6h37ANe99rULm01rELc17GBw2v-VH7RLnqou7Ungob-ZDwdnOwK6H9EJqRrVqbkg-sLUc9za8nOVtKyA_RdZ4wwZWcFcCd1J47sSYTYGEcBr5FGRyx0Y5ZHPSG5sX2StxZucxDqV2Lrt2MOolGpjV7x3yff0_irJyscDd8416DaZ1Rl2F4STgikPEFJnGJvQW3xmNJWO0hUEiFqg1mlaX_XQxdyz_5EKPoiz9kKBi2JI1hUFMS0OB-USYmuqr2U7UqNoWdGwox244OS-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام آگهی استخدامی «خلبانی » ارتش جمهوری اسلامی گذاشته.
یه نفر زیرش کامنت داده « جنگنده باید بیاریم یا خودتون میدید »
🤣</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6810" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=FHaz3IRzOE3hEYfoPdp2xVcaD7vntsHzOvj7n4rj1DyG3WUwLY9U_OQfgNGXXOaJD89EejOWc-anKpT1bHtsmyaUgEdtzdTr5M5hGBideHgFBrIGo39RLthQUk_Uo2C400urxj_wRJSwSWviQ-aa1KDE8WBC4l43qlTFoGuW8ScK5Nwc7KDKMZjKbsDzp8o8oa1YxasbsE90EMVX-gP-fib4clOubig-UkZ1ou1EtB0eF3hE0CAbB60-G-TMWllJefrNrc7NCroD-gHYGgPycvvhUA_7CPDLvp9zxXgkJtthNaf-5zYj__mf312SQB8tiELiLgov6j92XLVpmsopxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=FHaz3IRzOE3hEYfoPdp2xVcaD7vntsHzOvj7n4rj1DyG3WUwLY9U_OQfgNGXXOaJD89EejOWc-anKpT1bHtsmyaUgEdtzdTr5M5hGBideHgFBrIGo39RLthQUk_Uo2C400urxj_wRJSwSWviQ-aa1KDE8WBC4l43qlTFoGuW8ScK5Nwc7KDKMZjKbsDzp8o8oa1YxasbsE90EMVX-gP-fib4clOubig-UkZ1ou1EtB0eF3hE0CAbB60-G-TMWllJefrNrc7NCroD-gHYGgPycvvhUA_7CPDLvp9zxXgkJtthNaf-5zYj__mf312SQB8tiELiLgov6j92XLVpmsopxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKxJ2u_F8vvLtdz73hSn8Bkx4wOw1Yfz1g3M9eIVBNSTqXNgLR0vrDDjqhFU2D9PNVdXXJgy1Hv2Du4K-1lmeZKuGEWf-Ujq41aChD-2GA4_zSUPgbftj63LuEgcHdOFQ7gxlyl4Qehusf7iE0zOoxmNpiRzAYHqd_V9hvGRk36DikZY7yX984YlzWmfLEFGWfctzxfLuiXb4jV_QlDEX29bCeyxVtqkYKvz6OXWFQQyENg6pS4MGszrb4rZMtxGYhpAEGWuvHvpzn9im-Rs273h8XMVlc6t-Fu4gS-X-KEX3sqImHbbN1h7x3Mklh95lpmw9T6oCPSGRK_33vxMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bB61r_car39sjP5Vi2QY1koQWemOUKVXjs25pVySVR9H3m_m4CCBw72dj8RCwHNtbLqW2kE5Q7y1K7fhgij8PNvLEY9X6V4oSIPY7zP_FXqTGd2OKtfSAxEOZXU3dRWVYs0ftI6pYD33_x53186lLy38VUB-usYauRWn-_Ivlmwd7MzdAlwtD_Nx3L2oxDpd2Us743arT0LAiKUc06tM7JSeFYGuxsz2qAnKtCMgJpT93OyTXNeArKQgYYHkyJQods9XaPydW1QW2dNZXCd0LvF7UdbxWGh5Y-FGhuoqeNpGuQYutR12wEP5XItN8te71lzTkk4dodCA-NkNqYOedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pv1u2uUleHFzW9Xw14Dme3Fkbt6DuYNptbaqbvmHQon6ZQ3Qr2QqrqO7QU2LliFgEowY45EDbxksA-XZcxDBC3oCVYmLkcbk4bUYuOLV_6yMNOJEMIRSVdNKm64p0jkLR6NiNwPoiKcRppT9t6h0FP2Y_ZdYDz7q8nesVhYOYna3_QVPm1dpniCpSMeR0yElpSnxg78TvP19kl3hvYdWcXQjuJNSse_HRmi6XrphSO56INHShOoN47JMNFfGN8BRLyXjpDnQONB5j8az9kcEuwbJIwyFxwO4wgdcaGfr3ruEuPg6THJMDGUn6WTEA2kEY3H1Sc-SPThiQW43SktUlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=djR8uCNR-UwLFwfklD7tKP9FAhR7M9FLyu0wV4nnOicWQ2CUguXiG6EpQhkwA0zVGwT5QoAqdkpqBIiiraaDlJ7ZNaLcKHXqbrbhxERFS9jv7ktR9M7SgaSYGesAcZSda-ZXCEwbtdBLtyx3_mDlEzP3aqgYtppgPpkU0j98Axyx-IqMI5NRGiC-fnkapTpqsEiIhzcM6nwhkPNEkuJT23LIcd7einZHlqtRZHeMive_TEPJM9D5aj9z8HbPAXcPyF0iJ-yBtoeshelmDWMZmBP4lwPyfsS-SXCfF7-N89YbfteQKzPAJ-26oPEm1r2oyKzcSPzwLKPdQDi71yf3FIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=djR8uCNR-UwLFwfklD7tKP9FAhR7M9FLyu0wV4nnOicWQ2CUguXiG6EpQhkwA0zVGwT5QoAqdkpqBIiiraaDlJ7ZNaLcKHXqbrbhxERFS9jv7ktR9M7SgaSYGesAcZSda-ZXCEwbtdBLtyx3_mDlEzP3aqgYtppgPpkU0j98Axyx-IqMI5NRGiC-fnkapTpqsEiIhzcM6nwhkPNEkuJT23LIcd7einZHlqtRZHeMive_TEPJM9D5aj9z8HbPAXcPyF0iJ-yBtoeshelmDWMZmBP4lwPyfsS-SXCfF7-N89YbfteQKzPAJ-26oPEm1r2oyKzcSPzwLKPdQDi71yf3FIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=fowpGnpof8-e1e86HyeTgFWLeLjjHL6DtZ9OECz5S5blUGTENbUj5YQuOL_LhDyRK-MSMpPQ9xRMVUwrm6WAYGvJ7RBAjaG8jbTfuHftrb4WfN39-upawezHaadVBZBWp87Rpqgj51g5_45S09dNcQmKCrMmVY-k3O3Qlhu2yYAOWv52OzwcNeOhYJ4gTY0H9FXRRQOd-xqKQrQZG4Cv8sXhAdUCs7FyyRNh6_9nIvAuk4bSippPaQheU_87e5nBZqyipKtHTkOTkvc_pafyNqrzKBuwjxdfMQpUn1sR_wHcQn7ESWwbgXY2DG9Orz6F0hL8w013Tt-E5EkfIdL_JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=fowpGnpof8-e1e86HyeTgFWLeLjjHL6DtZ9OECz5S5blUGTENbUj5YQuOL_LhDyRK-MSMpPQ9xRMVUwrm6WAYGvJ7RBAjaG8jbTfuHftrb4WfN39-upawezHaadVBZBWp87Rpqgj51g5_45S09dNcQmKCrMmVY-k3O3Qlhu2yYAOWv52OzwcNeOhYJ4gTY0H9FXRRQOd-xqKQrQZG4Cv8sXhAdUCs7FyyRNh6_9nIvAuk4bSippPaQheU_87e5nBZqyipKtHTkOTkvc_pafyNqrzKBuwjxdfMQpUn1sR_wHcQn7ESWwbgXY2DG9Orz6F0hL8w013Tt-E5EkfIdL_JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1HToD-m4hufu_X1IIc5b51DafvkDO2_GMeD_Se75Ntfz24NT-5ya5nM1pTV0L7VKsxi8CraTcEoh1rGzr-CO6_kEadqXYAKv16QmQbLU8I30llX0eFL45XEKKnmx8Z1qzxgQUJKamAm81xV-gQg2dhMNmSdat1zaZxKnEwrnlkPqlLXTgbRxuvwje5xjksBgjJ4329NEl1NeIVVDr1_RDhTEwCHlw9JQaYVQIf8rieG2W9sd2fWyZ5r-9yp50iDNgLyVd9886tZ_GihOqFzICMDB42Vxvqz65JRFZl5O_8t_Mas9BE6J-jwLGYJRd4tQs1IfSDo8NzXlD40WeWIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1ykXoZwX45pNc1-7eEf92IhhgVvrUQeAdENiHWRYRAF1huRh8L3gVreWBW8yDJo9Sj6FBxA-Z5kKXtH1LXFchoOeaBiyObb8AuGEc8Aif3K0lldAdFuiYWNGLFU2M-CBsjIkx3spSTvJ40jjpGV1BWp5CR5M8zBXYL7I_K6R8tudy3BEVlQdBvPTvCJUiTEmPu59mGmQGArRtOfn9hgLCIQcm2g2DdlvO3HS7_gm8wPYuL36KtdOzSMOWl3WDCuSRS-EOx5wKXor50KZ5G9F_ikNTSgWVpUg6Ve99I1nzEEbDpMVYaJmRPWEnoWeYjcU-BU_ROj50hp_qFx81ha3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=SHAkWnx0tUT6kClMIHqF9fCMvAz1u88M03iHjm33tYuUZBzu0it_zFVWHHTDOa9gYKROYmoo2fR83sU-YFe8KjItfcfVKsxIiQGVajQ1VCJAYaAlTQ_G417fNfPxK9mqyeOM4W1vK9nplwyAdlCnGWA5G0WAvdNoyEZkBxAwl-ZmW_isnF1so5N_hGWjnpYTdbsXfLQ_Dsp00q2ZKyrykW566iBsJo5wocd0_X22CKPyDzLOgx7xafmEfzHkMQLzKLsp13B4U6S3Nbh60uRYDNa6C5wh_YP4M5YnW6RMncAj486dGYSp1mJgbpvoyON8J8Q_FyKEafrYvqgN_9owurG47myEzJGLl5mPOsSwXz0hwXZfBRmXy4rNYcI-z5ELweCKE-gh5AafVTAQyc4sJvW3ERF7WbENTI2aYZa41mvgBruB_zKvSSLq6WUZ9_xwJUjH-4qHKDdd_Js29Z1r-Hr94wANzcWlE8tC8Bq9pb-ZCrH1xAId0X7XQOQ8ykTA-8oshb3jfzK1oSbHyM-TXpjz1IB0c6hyaxbrCtPCoyegpMuc-9fJSZQNeLpxK_QNL15s_5Q7ehU-5rTHaUrDtfMk6OJWenCh9yI2yJZeHQsYu6QtynWRcdLmdPSzii6wkvPqbh-g1a1I3TH4dy2CytL6InFqTmAKCCpNDy9qAB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=SHAkWnx0tUT6kClMIHqF9fCMvAz1u88M03iHjm33tYuUZBzu0it_zFVWHHTDOa9gYKROYmoo2fR83sU-YFe8KjItfcfVKsxIiQGVajQ1VCJAYaAlTQ_G417fNfPxK9mqyeOM4W1vK9nplwyAdlCnGWA5G0WAvdNoyEZkBxAwl-ZmW_isnF1so5N_hGWjnpYTdbsXfLQ_Dsp00q2ZKyrykW566iBsJo5wocd0_X22CKPyDzLOgx7xafmEfzHkMQLzKLsp13B4U6S3Nbh60uRYDNa6C5wh_YP4M5YnW6RMncAj486dGYSp1mJgbpvoyON8J8Q_FyKEafrYvqgN_9owurG47myEzJGLl5mPOsSwXz0hwXZfBRmXy4rNYcI-z5ELweCKE-gh5AafVTAQyc4sJvW3ERF7WbENTI2aYZa41mvgBruB_zKvSSLq6WUZ9_xwJUjH-4qHKDdd_Js29Z1r-Hr94wANzcWlE8tC8Bq9pb-ZCrH1xAId0X7XQOQ8ykTA-8oshb3jfzK1oSbHyM-TXpjz1IB0c6hyaxbrCtPCoyegpMuc-9fJSZQNeLpxK_QNL15s_5Q7ehU-5rTHaUrDtfMk6OJWenCh9yI2yJZeHQsYu6QtynWRcdLmdPSzii6wkvPqbh-g1a1I3TH4dy2CytL6InFqTmAKCCpNDy9qAB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKUA-GRoYMIBI9TymAgSvJBc7czbAjaXPo_t0tcwYndrQjfLj_ZGVvLTs5221VHszc6Ri2NY2tIywF4Sy6rEXWLE2r2bkJdbcqQR2QPaf-ZkLCZqhbzeL4D5v53Q2VYKZ5L9A122plctIFjfP35WSeaclWnhpE6faUhHX1xWISwYJqfhr4SABJOPqHCQLRUtTne8WtD9Ogq3wGlrcx-pOLm0rHCIKxOgUb4RBaMvhV2LAGw4MdrTKnoICJTprg9lm5TPJUnR1RDQoHQ0ZPLAShlo71qX4rfoSqy7G2ONrFulGxqJ54vOCURdv2lJ2FUklywh8Ex_tgjdEm7R9nMthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2qYD6WTNndkTfF4NpcWV0t3EfoOu9M0mwqzACQbp8eBapFo3XsHxIOJkBevlsKmLUqy5WZazvM11GlaCbUJ8ndCLrgJ7jERFaZojg6EVi4QItjjBJao3YSgkBWv6H-gFV2KW5_UgALyX-_Py1kGHnzeh0N3K-t_Hm6W9iOBOZAtF1IMOUpDEWgDjwFhjD319TG5q4dx4zYUJ80xXQIj-V9Er-CKeXwepPGTybIUReOr--hhgICSkb3DglZDBPrQ3p0BpB_WkMAtjsgDxjzHRlHKBLzdk4xL-ZaAJqmd_lQHPUQeigCTlVyfGm9heikVygbkE9ChymL7RRW2CP0HSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hd3RkBWqcri4HCg_UQwpcEpgDkJptlaCvhmgLVu2V45EGmkQDf8A_2ktxkX0lrtmYyW9nb6P1BoWaZrbxpfrAmRzOqgM0abo_H1zGF39hzNm5-6HDjOSY-McbxxWZ625PKBC_-HsRjC51_gfx8ZrzpINUFWXhYpzFJv6mjhkhOUrMYQHz7nGobrgCMiVpWiPf3YdZHq8aDbropgqyX0d6eb68tS83nrUnMwuOFf8ZrREtmBoIpuwZBuDyA4RvtMJieVIQ4d1zQFQ4Ber1vOePq75jFYzPZxFJRiwbGJZ088XrpSLw8qtU4XK-zf6_cDS8ledPYfi0xKo66mHPL2zrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqFNm66d2Mt_pGxCd2hIpzrhGtG9bdFCg_LrC-QWXKJFm9qctffkhagSbExaA1csKpxzHA3SzsYacUsrMjr9ajwJbSRoVOGt7VwjfkzfQRB4KVerpzu7YZvDrZ0Z3qq8u-3dyeB3psRaDwj-Nwwmiv_nxB4sr7s4eMsVwfUIFqXc06lWUSG8TXgjgXh1QVWnx2PkL_7OPy8-FOFCMajKs-WioLFDz6_vrN3y8-paiTuYLqi6vPnRHH6srE_tVOtmQ4izvUTkF_aZBKt21j2jdXBnfzAb8wnEZvQGswzj6lW3Ot9m6tkbzrqFjTSNNHR4_SPfc_e7c7BDiU1jLm5P-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjFi9jPbpoDDTsRQglDcSb7F1SCNFvjnvaZ9uJ0KsoIdT9KWBGBydP9NsrKFfHqqP4XNg2RifhEhhxIULlb6VaeyvvyXsyDFwpQMrQw1UT01j3Rx75_hawyk4r78wtE7aZWTe3jj12tbe8f5GqCnO98BkZ_qNNewPEGDdeOQXnCz1P9boXOG2Qp0VzshR-sNAIExsRi-DT1L9IwGnhmIcB_ocZ9AA1Xewz_N3zlW9MbrW_IG2rF1tnI_nJ9vbspw_lXrB0FKFUBn5Dj9TQRPk_UCnvulv5UfxqpRe2r6_v5CfokGkKR7tjcx0G0iWVeQduvOzbMyEvt8KFSAfS4KOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI9UIs1O0OmUOQCO5iSkEGHz9MJpVst0_jW_NjmSP9WMQ6koxuXhCItMiVzXCkJnAa8jjeh9cjrZJcOKgFVksLEw7oS0EB_-TW32_JXVqhx6ZzVVXEKAG4xTYflqatyH8qGft-0V1W_uvecKMdA1dbUnOJOm6jBp8XLHnxRUlykjbxMUbyscf8tyW_w3VPf-vrk4WbtdkEBRV_byq3vYalmFP8ahM6ypQQTc9epUugdWC690ooWfqA9lMffhQx7T-xzY1KSJkIwguLzC0bFDvDcLZjL7814mnCo07EgDhGKOnrORKrfJz24vL3X-ALk4eH9ZVmgBM55eKk5fvH_O9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Cu5jeDPThOZtmlc6TfAdmHT9FG10dHPMlB8O4_3nAvbahEMmGHuRQ_FN_sjTV3rm5jmN74j5qUmMND2eZ1iGIXYdfmJjLE7dowNNHYwzaptTwGuYpm4Hz_FG8eFfHygEFBfspC0xFY3bZKShWiwQRytG40bHGpUzfT5Xg6z1e5XotnOdI1iVgLrUZIkeCRi5pxCx_jtmdN8vZG93KpR1wUC3-mzWjEtSqDz8XyAjfoqf0vwv--bXp5owWHLhdIddVXdh7MO2PjknGFEUXfpp9edPfkoSJN-XQLdhTca42MSy8ZH7xakNT04Lq26mX1b6X997tn94KIAZH9xljD8c0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Cu5jeDPThOZtmlc6TfAdmHT9FG10dHPMlB8O4_3nAvbahEMmGHuRQ_FN_sjTV3rm5jmN74j5qUmMND2eZ1iGIXYdfmJjLE7dowNNHYwzaptTwGuYpm4Hz_FG8eFfHygEFBfspC0xFY3bZKShWiwQRytG40bHGpUzfT5Xg6z1e5XotnOdI1iVgLrUZIkeCRi5pxCx_jtmdN8vZG93KpR1wUC3-mzWjEtSqDz8XyAjfoqf0vwv--bXp5owWHLhdIddVXdh7MO2PjknGFEUXfpp9edPfkoSJN-XQLdhTca42MSy8ZH7xakNT04Lq26mX1b6X997tn94KIAZH9xljD8c0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=I91qYa0jyOmRv0b6sHtQZRHuwEHvIgFMS6Reqk9KAp3GDmsD1477rUWXz-Q8Sp9f9CLF6QQKWX_qL8FLW1QkNeryDPtRIpDRb9Mlvc-HUTLjgcwvVIniOHysUa77Bo2NNuKhAPREYcp3LQ9-OJOt5FCNZ_-7pGgPfU8PUzRzWVmjd7W9NSm7OsOfhzDSWkKLC0AW8EbH3Cd3XdJFsrZK3uTGZyxmLbULQuvO2Z-BYETuzdkRTU9i7-iazu7f7XlnEzto00LdYlxkCQxbgz0iCEztcxl_FhvBesqay4-im7OjfKfcXDxojfE55W2lYUe6uUMZh6sTdjE0o-VvfdTrPDlvnkmZxQsi1o9RvOJ3fOlIy2a5VmiesXbzCLv5tRuysA-lonhkaWrXGIMwdIZHCYRXkFcuPDB2LLMLG4zcDnRdPN6mB29DFmO6DGA8heGhOWPC8anoXmOAJx7cUNk5g7QM-ECq5KLg8WdLEr6zYvlIq5UyCgb_EIo36ZzGIa9U1YpbiUslw0j8ZzQ8TL0Lz9uqZ_P5sIFgGkOZNiqtDOAjUQlBaIS2cDNiFRo1xnBm045PaOTm5yz_IghswjANnR4pg2-BwdhFNp4ImraaNe6vyOKCn7APTD25pSXesU7SC0g1ziXgG7EO88frhdCvCiykjFSoDJvRpsSW-PN4R6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=I91qYa0jyOmRv0b6sHtQZRHuwEHvIgFMS6Reqk9KAp3GDmsD1477rUWXz-Q8Sp9f9CLF6QQKWX_qL8FLW1QkNeryDPtRIpDRb9Mlvc-HUTLjgcwvVIniOHysUa77Bo2NNuKhAPREYcp3LQ9-OJOt5FCNZ_-7pGgPfU8PUzRzWVmjd7W9NSm7OsOfhzDSWkKLC0AW8EbH3Cd3XdJFsrZK3uTGZyxmLbULQuvO2Z-BYETuzdkRTU9i7-iazu7f7XlnEzto00LdYlxkCQxbgz0iCEztcxl_FhvBesqay4-im7OjfKfcXDxojfE55W2lYUe6uUMZh6sTdjE0o-VvfdTrPDlvnkmZxQsi1o9RvOJ3fOlIy2a5VmiesXbzCLv5tRuysA-lonhkaWrXGIMwdIZHCYRXkFcuPDB2LLMLG4zcDnRdPN6mB29DFmO6DGA8heGhOWPC8anoXmOAJx7cUNk5g7QM-ECq5KLg8WdLEr6zYvlIq5UyCgb_EIo36ZzGIa9U1YpbiUslw0j8ZzQ8TL0Lz9uqZ_P5sIFgGkOZNiqtDOAjUQlBaIS2cDNiFRo1xnBm045PaOTm5yz_IghswjANnR4pg2-BwdhFNp4ImraaNe6vyOKCn7APTD25pSXesU7SC0g1ziXgG7EO88frhdCvCiykjFSoDJvRpsSW-PN4R6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_g8BXSyM74xymcnCVs-ghB1DBzO9AqtFfnNkRUAmfCYWThjqAMB855exu3S7-dplrxif-UItgbDr_tI_XysrasZfrUm139hPtOcVpgL4w5gKmnU2hscCZFUSJvplRB5uzvGGdIXNHSy8dCelp1luM7Z0E1Ii1ycxQ90h2s9MPutGQo7zdCCvgwk0ZcqPU0Rsl4GmhW-9H41ciSvYZ7nS0dK1Dqod-TdYAtkoiD0Owv4WFqjQxGrUlWz6cQfThHK1vivDPUH9HOsFdWrxwyYN0FWEiTPA3X3Hr9MbzuSERKWLcdQlqr48BuJgcX6IKF0yWGR1BqBOMtz3hyHb8Li6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTi5Qbn8N7abMhwtdzW6dfOBHfTXguCjMP5rtCn0Ex1d-YI9sckpdp8Y0OEYpwOXWpDJ0BDu0lDikVH-xvSbWd_B1aw8aFCaxqedRwbx9Hvmgk06RVdn79sGlrQ77rJFfXeXwTFq4IBBDCWbF0Lg7H3Nkcfe5pgYg5IA7U5kph7mJO1_hIGUGgQjSYpY8rbljrXNoD6NtzTHF9DY9gltNT0fwz6u2cnxZadZucw6BDcUlsNooPbmm-yAGOrNRv5RGkdATEYshq162ec7yPQ8lpGhHgX38gID6R7XjPzbb1xqm-uMxLsJb_McrCPvV0TYpQUzuv7ur49Cu5uIIR2glw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad3tp9avU5kq6ZhPOwtGIKOPd7qTZj0Bt5ydCGjIxntiNoJMANZW2p5RX_kqj6aFQYtn0Ra9TFVJlY6Ex-LOWFQ71LA69tLTQ_6zMesqu2Jb70umR3CJKgXlPeCxg2Vty1fJCuxCF4s08AE8HjwSx1j5sjx3vA9-Mj1AZJjcNtAsrv3p70ZXiiEehGjE_vgL0Gp3OMH6bPBSOUS1s3yKRnk015H3y6bycGkiHljhv7BP8CSYh-iHYPRWe2P4yeqv497tJ2zfamVsWTTOWCsJK2xDLeTQNP4CbieYSClDdfdts-iUBhQuJzbJszf1veLGLp5X7QynKtlhZmB6tfkqHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=gzRk7pa60P3DnRYLonydpOOX6f1HnXBemrHOumv1e5iy3kbMfN--yt1M9qS5tSILKgQA80DfzBW-ON56_NH3Dts_vrNkr8b6Z8ySEx_HhlpB8xe5srSWNKqhPKSlzRcF_zcsVbE7PRkvgNuytmWOI7pgUFSioj4oNn4ZOnCmpQwt3PSqj_qaEwJaImeO9OLvw5YBw1TVwGZpPbhRImQxwpXmQHsYSiEOUMAWg_70OOi9k_k2JCF1t_DT3xmQkY3NqfkxRN_2ODslocFl7WDvUxJ0SiiLmMF53GkMNiMXLYlhjcGeGaejkc8Ckl7IEwfPDOWoqpZx6hfkPqrA0Jf72Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=gzRk7pa60P3DnRYLonydpOOX6f1HnXBemrHOumv1e5iy3kbMfN--yt1M9qS5tSILKgQA80DfzBW-ON56_NH3Dts_vrNkr8b6Z8ySEx_HhlpB8xe5srSWNKqhPKSlzRcF_zcsVbE7PRkvgNuytmWOI7pgUFSioj4oNn4ZOnCmpQwt3PSqj_qaEwJaImeO9OLvw5YBw1TVwGZpPbhRImQxwpXmQHsYSiEOUMAWg_70OOi9k_k2JCF1t_DT3xmQkY3NqfkxRN_2ODslocFl7WDvUxJ0SiiLmMF53GkMNiMXLYlhjcGeGaejkc8Ckl7IEwfPDOWoqpZx6hfkPqrA0Jf72Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=I4FNi6jg79Qo2vuFWlYqu4eY14nDxQsmo8rfYfYHlHVdmXkT9xdxjiVfGoQXSyG_C_No0jJI6ZMgypCJJvfeVTqmjB4B-x4UQTnsadurpm6TRRZ7zFhzF7iQ9hXC2yM85Qg8FHCLTy-OZAw4HcqkRaUhM_vTYbUr17X_IrqCfBYGLL2Ar1w1AdaCzCd7uE3LVVy7q5EgcKB9BPxm7xce2TnoqXVEH_XVIqrefmjFxPVt2l2gggqr1tSa595oWQkxYctjzUbSYWti8ICPF0UqaJ_53lZoZ-9YCJOHwnv3YdDsq_2meF3hl1_4jzifj6kPVo8eW8MvFQ9AHFqwwxwHYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=I4FNi6jg79Qo2vuFWlYqu4eY14nDxQsmo8rfYfYHlHVdmXkT9xdxjiVfGoQXSyG_C_No0jJI6ZMgypCJJvfeVTqmjB4B-x4UQTnsadurpm6TRRZ7zFhzF7iQ9hXC2yM85Qg8FHCLTy-OZAw4HcqkRaUhM_vTYbUr17X_IrqCfBYGLL2Ar1w1AdaCzCd7uE3LVVy7q5EgcKB9BPxm7xce2TnoqXVEH_XVIqrefmjFxPVt2l2gggqr1tSa595oWQkxYctjzUbSYWti8ICPF0UqaJ_53lZoZ-9YCJOHwnv3YdDsq_2meF3hl1_4jzifj6kPVo8eW8MvFQ9AHFqwwxwHYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1LxyniED0a2Y6hXr013c_AACbLhZbU-gJUrN_vh2RhxATxPVZiPyoWb5JBp_0NNLjquzbSZGJlO3YL4L9SvH4DO_Q4aStWRR8738fpyxnruUvO9G8JVk8jDGAjQSBZJ6aEz2wF97PE2ZcHWG2CugB236SlWIjRqdqf8iEvdAKgmWONgVIRlmUNbkYjX-bMUk1GMif_xdkIh2YaIGeeTia4jYjTbJ7ogH0tlzqo6wS03ZKqbRY1gyuASs7aiXuK_tAFtQ16_Egos5hmBlxjNf81noq-A-NWJoP30cefibyA-i8PzOx6qtj9dh4zwa5Q_rdlpUCsFSIJgZuDBgX5Xew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=bwhdoO874qykd9CyEn8ziTnWDZ5rnRmgPn5UeMHxK53lCkIB7Fzbv7rVJNPxSVGxgzVpewWhI9hOozgQiP8ykE761xK9aTpT15MScR-Y8-DNv-VU5w2HqrB4hMe-ylIvtrhoJgo7PJWELSS0EOPuoaQ3AgK3NBpDA_Wncfll3De9cWJKbM3aYWazw2-R2q0J0qyedNlk1BTSscQATP9wxeW2SMwDjoLyI8Bjfm_OHd1--P6r7Dx3QRTVhCVd99Q0oAWnw5M1RxU-5RtwaPCCBC_sjqGl5WzgluLdRjI7ilsUJfN4PaKk22qVSvvKjYflbXnyCuxkZc1NddW6Cr9aAqUoR_UFpiT5OFLT7BtF3zKOnFKDKpgoUjC-kp53k9XPRCSra4Wi8yjbpPB7hCF8RGsf3cfygD6Prft2cpUwSOqHr1B0CuwTxjAA4Uco67Ea2JqeDZh_hWD2mO3Sc7TlmeWt-49CYXQ1kV7o0G8fdwd41u3G_NXNLXBBOm0bhCfPm6qF-mu4F194mSlbOcfaOraiWQ7aTTif0qDysNeMRHVNtfMxFtGJDKG32O_U8WHV5L5gCQ0wRFkur62U1sRHU27HozJWfDQ_o1lnF01f32_r2MDvySHNyf-kfgRwUgiIEJp9HL9_M6xsmN4G3Sn5nDbJJncQ5dC8BbndFgiUJMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=bwhdoO874qykd9CyEn8ziTnWDZ5rnRmgPn5UeMHxK53lCkIB7Fzbv7rVJNPxSVGxgzVpewWhI9hOozgQiP8ykE761xK9aTpT15MScR-Y8-DNv-VU5w2HqrB4hMe-ylIvtrhoJgo7PJWELSS0EOPuoaQ3AgK3NBpDA_Wncfll3De9cWJKbM3aYWazw2-R2q0J0qyedNlk1BTSscQATP9wxeW2SMwDjoLyI8Bjfm_OHd1--P6r7Dx3QRTVhCVd99Q0oAWnw5M1RxU-5RtwaPCCBC_sjqGl5WzgluLdRjI7ilsUJfN4PaKk22qVSvvKjYflbXnyCuxkZc1NddW6Cr9aAqUoR_UFpiT5OFLT7BtF3zKOnFKDKpgoUjC-kp53k9XPRCSra4Wi8yjbpPB7hCF8RGsf3cfygD6Prft2cpUwSOqHr1B0CuwTxjAA4Uco67Ea2JqeDZh_hWD2mO3Sc7TlmeWt-49CYXQ1kV7o0G8fdwd41u3G_NXNLXBBOm0bhCfPm6qF-mu4F194mSlbOcfaOraiWQ7aTTif0qDysNeMRHVNtfMxFtGJDKG32O_U8WHV5L5gCQ0wRFkur62U1sRHU27HozJWfDQ_o1lnF01f32_r2MDvySHNyf-kfgRwUgiIEJp9HL9_M6xsmN4G3Sn5nDbJJncQ5dC8BbndFgiUJMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=IUxfGgjC8-rNMrGPX7u4_iMK0mC7SBBPs_kJv16noRTPjLiucuKwB1tfw4I-GweCZCjrTeijACZO_zwiAqk0uP7Yxv6t3UTrvVEiWPAUvJiVyIa5YXiRVsfpzVcIM6Q6HzlUch-dkHrl8TXyP0hmdlrBlg6pKGy5as0JeRnzTN7M-okmr5H6tx1RluiWShAr2MamnEhs4dIMf8gSv6T-P65GnjFJthZ89-wNNt-UOLSmz7lhw2uZZJ3IbtJmM9AkhDpx-avr_F87MYGymLcfRuWyWqNfGubMZeH-TRa730_OLNJPYfiZFpvmlA6hmUoaeCRYUuGeFOQ1J9-qgb8FMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=IUxfGgjC8-rNMrGPX7u4_iMK0mC7SBBPs_kJv16noRTPjLiucuKwB1tfw4I-GweCZCjrTeijACZO_zwiAqk0uP7Yxv6t3UTrvVEiWPAUvJiVyIa5YXiRVsfpzVcIM6Q6HzlUch-dkHrl8TXyP0hmdlrBlg6pKGy5as0JeRnzTN7M-okmr5H6tx1RluiWShAr2MamnEhs4dIMf8gSv6T-P65GnjFJthZ89-wNNt-UOLSmz7lhw2uZZJ3IbtJmM9AkhDpx-avr_F87MYGymLcfRuWyWqNfGubMZeH-TRa730_OLNJPYfiZFpvmlA6hmUoaeCRYUuGeFOQ1J9-qgb8FMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEHIeK_loVzOLlHIedXY-zoq9h5T2KGvZ_3xnviV5hRCBaoTGbmU3kQy97bhoKCjG839nsitAO5gFrvI6R9ZmZ0oQ8XRIKi1u2HnagNCxwGl2ayQ-hDhJOn4Kh3wwvfqqzeR9SY7AfMHL6HPKPk6y6GImI4tNh34-UqiVVVgNRtj5aLDl6KurZMPLN-EgalIOatKyu8mIXJnJeYQk6eQ3KJdRqpDBhm-WLUoA3DK993GIEDSQJIThHUz5zsZ4igef964mAshDAyPQgvP1JAm-ZVtS06tDDjICJYMj6v-hRPCT6nDPMBsX28N1-UXMfCVddwCC0tWGesFsOMnz84rDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=ITxDNbggD_tzqaRXHdnElpuFp4ETfVbW5qpc_1_4r8V3cU2w82obNpTJk8Rg76p_OpiWII9Q9CLt94hUnmfDqBiI7d5lZXHverdGmBk4EN7pNsrDliGbIoNXpzi3h_4975jflRtLyXFnMq2IaZ5Muc2YqkI1N8Xs_AfK599ulh1MpnLHu1R80Bn77wY4Bz-FsNU_AwjbJAKJfFPDj2_ZsqxlCq0AqIR0n9icuOFBED0fEhpmnuHOXBIp3I4xjK6kZVer08ojf_VcIvd79UujQe338AxyKYBiQmsml73j8yQEHbs45GmHxp_SYDqHvmccm0feMvWaWI4ovNawwNgPlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=ITxDNbggD_tzqaRXHdnElpuFp4ETfVbW5qpc_1_4r8V3cU2w82obNpTJk8Rg76p_OpiWII9Q9CLt94hUnmfDqBiI7d5lZXHverdGmBk4EN7pNsrDliGbIoNXpzi3h_4975jflRtLyXFnMq2IaZ5Muc2YqkI1N8Xs_AfK599ulh1MpnLHu1R80Bn77wY4Bz-FsNU_AwjbJAKJfFPDj2_ZsqxlCq0AqIR0n9icuOFBED0fEhpmnuHOXBIp3I4xjK6kZVer08ojf_VcIvd79UujQe338AxyKYBiQmsml73j8yQEHbs45GmHxp_SYDqHvmccm0feMvWaWI4ovNawwNgPlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGwPcLAu_CfGkce5CM0bedAhvQF90XD3x2A4sjStExYMyZre9kRbZLgFsBSDiLhFy9N4iCgO68FTVe9Xo2IOEGSkRLpjlxXTe_kTSW9WL_RDECqWTvAuDK3ZhdU6A70T9cPovLDIOzUGhrs60mlEYTgHndAI5AOVsOrpaWcplr5Gr7QMe9Xcl2a238a_YM1zLflHHMguzAQr-MGXxPTmI8tv35gfu0nK21jEbOwZyCElzSKyhU71ljOVDOsrdrc7xQlwEgFD_ippMNk-74zEuwhM6x-8v5yYYBFHX_ohXDFaZCagHkxHyZcilyxDXhVXHZgPeZu_F8i4xMxzZVtrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCvN6Dpdot5E7IhvA73B2ygyT5IZCcQDIdV5sijig9fudSdu7mYvZebZH7fZAzwDcF1icC_Wuw_Y4HilzWJgSjL1ZoR6f9-VX_9D8feC8-_ea14LWngPuxhnMAuqB6z2ctLi9xQK8KZpVsltZNKAI6yj6ekm59PfHnBQOxg5qyPHconLUXSUulNpripH5bokUUcS7ATIKyqgS1O7sOjGEotd1WGz8nEvXNlfuqlTUtLkgr43yqpGoh1R15W9hc_Fbjy3nBLddhk_ASK98AZSr5DmMD_JtCUhDmo0_UA0ueWnwvU4IiEBHkRFPn8l33ytZvvvaSxsw8NeuZfPOupnrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=EnlWsJFiXnkZLtkquhu2fKc71GE5aSS4qJjkOdcF83sjmxfIKcpaOw0icWMuytFkfoXsxA0SS1BhNbjVNRr0bins9dYGEdd8m8NvSkAibvKDxg2sKpYCw9CcYiunTjKuuEv6A1DQMILhyzgrOjJL45gXs8MdEZpdh9aevY98jYMPa8rLNYPdigGeb0sw1StfjRVosfTGiPENXTRKkoZpSlINKjUYR-v2dvgL9wBHFoNZ77-g1lD1fPyHSB_9cR6dLReI4RDibQDNJukx7d8-KxmAftGegX8Lw4QpNmOPjvEij41g7mzLOn4_S-r-l_O_9vY0AsG-PpWjHkoeN8euVDuo98UAkh9QlP7MHo7nCONUPJO6nVPTHTEZjpcUhfZge74LhxpCuKeL7T8DbeJWq2_KP7TIebLBYnHLsRN6GkaeDAypBgVlzeZRemUpf4m5glrC3Kam_nxHSX7BpfWjrpU90oUkQtxGEAGI3XKRLOQ1EudhE7_jaamYeyovRD132SfbzrTmodPzVq5r0rqxI_SOKv15XMGubUh9LMNfMvtkbPglNIgFm-v9ihR22JP5Sq836dCzR7I6CRaeXNLI2wlv28FJm7GfcRf5KsAD0zBBb6z59Q2Waw7QJfjD9f9wHw39EA_07B_LpY3oZFOUjpkTvpCAGpAL_oiTl8HW62w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=EnlWsJFiXnkZLtkquhu2fKc71GE5aSS4qJjkOdcF83sjmxfIKcpaOw0icWMuytFkfoXsxA0SS1BhNbjVNRr0bins9dYGEdd8m8NvSkAibvKDxg2sKpYCw9CcYiunTjKuuEv6A1DQMILhyzgrOjJL45gXs8MdEZpdh9aevY98jYMPa8rLNYPdigGeb0sw1StfjRVosfTGiPENXTRKkoZpSlINKjUYR-v2dvgL9wBHFoNZ77-g1lD1fPyHSB_9cR6dLReI4RDibQDNJukx7d8-KxmAftGegX8Lw4QpNmOPjvEij41g7mzLOn4_S-r-l_O_9vY0AsG-PpWjHkoeN8euVDuo98UAkh9QlP7MHo7nCONUPJO6nVPTHTEZjpcUhfZge74LhxpCuKeL7T8DbeJWq2_KP7TIebLBYnHLsRN6GkaeDAypBgVlzeZRemUpf4m5glrC3Kam_nxHSX7BpfWjrpU90oUkQtxGEAGI3XKRLOQ1EudhE7_jaamYeyovRD132SfbzrTmodPzVq5r0rqxI_SOKv15XMGubUh9LMNfMvtkbPglNIgFm-v9ihR22JP5Sq836dCzR7I6CRaeXNLI2wlv28FJm7GfcRf5KsAD0zBBb6z59Q2Waw7QJfjD9f9wHw39EA_07B_LpY3oZFOUjpkTvpCAGpAL_oiTl8HW62w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHwY_kxcpKKrTqfTrrG1xMPfkJ-G3j53bs_u6A7g4Gv4PrkHkLzpDzuHPCT2R7HV6eBibFS_3R-lEUBoQ3iVtPDXAv2i7WH0FFvAGI6R5dSGUe60O4NtsMlTXfdu1MAu4Hi8VJieu-gi1wRlCH-L7AUSZsXmFiImqgl1s53CmjQVnqkMiG97uX0SkmAWCfrV5hZAKvomzqLGJjC5hbL4RltZd6McRQIgrHa039rWnFelpjBr1b7brDnfhi7NOd6Fkxv4jKjcgetCAElUqDbitLjYOk_a8ZoGTLhysbN_FLO-xWj2Zuxxdgy9BxR60t_RItO9x8A6WRPJGa5REf-t-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0_f8JpbM6Dcd2aIO55F3ydJ053SfZClFpZe3ahPACRB_WYAH6LaLWdBxnxMPv-6uuKD3mh7HLN8_KZ7S5HnabUgj8C6yHRugMLUTHSNxnRZADvOgrU6DfbHjIBUhbsVOsAhO8qpCKXynGx_QIYWZcqKKb375dQgbMXeBMJDaOaZin9ifGglvL66oF17jfjd0NDIEG1QiQIY7wiSQgfmUcCUtDCodxW-auyDnu1yjCZy8L908reI2xJ6o1oB4XYXAP3RxjR-ZiD1W8di3iydYf3p5TngVRFklK45TaGc74PFEUPXl5y4LBcr9-69XRxsZk5LF7ZRbatjj2aN6SDv8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=eFr0ZStJU_b3ekaLedMAqWkzljYdmmYFHC0YzvzuRdfRTTHcdFqP8wGnAaDT4ha0qLnE0IeO7cCOwY7LIWgFrAVeGfT6nrCFFSaubS7mR5XPc-PBmI71oNm7BjcgZjgyLDkm70CRaCBNRW_YZEnqzup_qgN7iyt0CbynZT4YlaFZFzZzNqZVPOpqdPKT8_EYj3fr2xLH8juQv-9m0YXURN8iS3CdIjm6-rHh37t1TN8NQvALERHAj1E4anKyXljEmVYn4EsyrIIVI0DSqi1sA971zVeSIz6Itrbkgac2qubwH96VJ5xjWHMxochwrEejjpuz3rdOHFaexRu_Uj0zhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=eFr0ZStJU_b3ekaLedMAqWkzljYdmmYFHC0YzvzuRdfRTTHcdFqP8wGnAaDT4ha0qLnE0IeO7cCOwY7LIWgFrAVeGfT6nrCFFSaubS7mR5XPc-PBmI71oNm7BjcgZjgyLDkm70CRaCBNRW_YZEnqzup_qgN7iyt0CbynZT4YlaFZFzZzNqZVPOpqdPKT8_EYj3fr2xLH8juQv-9m0YXURN8iS3CdIjm6-rHh37t1TN8NQvALERHAj1E4anKyXljEmVYn4EsyrIIVI0DSqi1sA971zVeSIz6Itrbkgac2qubwH96VJ5xjWHMxochwrEejjpuz3rdOHFaexRu_Uj0zhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=MvmtwHbS-S0njreTp8BAdiqNy_NwQ0M1QpLlfDZ0_Mfo8UtUKYwO4BltBBZ_IAGGHnaV-kxqsSNsrbIrK0mXHyoCG8XmelnyeybPCHmaL40bU-pwjo764zNxeiMF7kaFaZoyULTrXOXNIQpyQcm5w1ZScLw6_unWojazTtpQk1_2ffV231Q0LRYZJnf_lT9F8tNS5kz1SbfbnmfF1WGzBYn6qlZc9mgA3s3J-W0BEXcEjrkVwmzKrm9fmLSE9_r4DPDjAhgq9kgjebRuep41T_-FnIsBslPpPo2kPVwFjlVIrJrKRtwIy6I2RT8-6_PL2ya8i7RBmDQKm0KyeOMnnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=MvmtwHbS-S0njreTp8BAdiqNy_NwQ0M1QpLlfDZ0_Mfo8UtUKYwO4BltBBZ_IAGGHnaV-kxqsSNsrbIrK0mXHyoCG8XmelnyeybPCHmaL40bU-pwjo764zNxeiMF7kaFaZoyULTrXOXNIQpyQcm5w1ZScLw6_unWojazTtpQk1_2ffV231Q0LRYZJnf_lT9F8tNS5kz1SbfbnmfF1WGzBYn6qlZc9mgA3s3J-W0BEXcEjrkVwmzKrm9fmLSE9_r4DPDjAhgq9kgjebRuep41T_-FnIsBslPpPo2kPVwFjlVIrJrKRtwIy6I2RT8-6_PL2ya8i7RBmDQKm0KyeOMnnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=ma2TZ1LDAT4v7URQtCQpiMxuomL1-75EV2l1PUh8XfpAwkwg2P-zMT54jHwDyo6-AgR9o-faRfNk1BVdZRoc7h019JU6orgcqKEBzu8yOXdNejxBfOZYRZdNKGrbOWVGG2df2r3e6tMvvXWQclID0IB6zfUa8TOjWtQvQHQezdPZL0hYBkFoUvbRMvqYzh3enQ5etzoMcQGXGefPmiRzN4VhXWT_03YDiO2u6W_YK65X05asPmp5xeBrV4amewRIdK2lc6OYskT-GYFQ5dSr2s8KknkAnygDQxu5HZLeeWvbOwQKzy-BwIyGQg51AmKm868hXYKx5iiPUv3ZjsWmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=ma2TZ1LDAT4v7URQtCQpiMxuomL1-75EV2l1PUh8XfpAwkwg2P-zMT54jHwDyo6-AgR9o-faRfNk1BVdZRoc7h019JU6orgcqKEBzu8yOXdNejxBfOZYRZdNKGrbOWVGG2df2r3e6tMvvXWQclID0IB6zfUa8TOjWtQvQHQezdPZL0hYBkFoUvbRMvqYzh3enQ5etzoMcQGXGefPmiRzN4VhXWT_03YDiO2u6W_YK65X05asPmp5xeBrV4amewRIdK2lc6OYskT-GYFQ5dSr2s8KknkAnygDQxu5HZLeeWvbOwQKzy-BwIyGQg51AmKm868hXYKx5iiPUv3ZjsWmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxggQqRDW8vzW9I_6pQyvEKB6mK0jbOslkunZHVO-AQqLO7kAkRXqbySiAVjKapjHcgbF7Xqvh9ilRXy_wzZ0WU0MjLmt7GANyNAp8JkD8a4a16aeEbkbTQOwmkoDR2WXZxq_QU2tM7l9F3U-7RKENuJo3ldFA1kPG4X1YnD1E9Uo_7hnijSdcuOjkXJfP0mTvDEc5sxbzdcUZ9ZfoEhc8JtlGeCYEPZ3RpeqeIt8v0y_tHimHtjEeEgR7BIxUfiSlIjP03G2N_rmHaa_EzsGKwCzZBc3mlkafsbdtSvDoyR7nouPwDQasJm5Li-XuzAZp8Gtasx6QbXBRhdPKPVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KQt2SjLGY-2eU3oucYb-AbbgwdpPw_Nvu60LWFBzgVn77RCSy7upvGyVorV_7WU5aWcI-8U8v8gOy1GkmxtV5OoYTus7hNSYwGJgkiAwNMDNpimZb_HRZ8IubnSChWO1p1eo3H9oZWrAGe5XbB_2IsbUBDkIRtr9qcmPHq4QjQEoUO21ddOaZ8_iLVor2e75-320l7sdcrJ5DOZYarDMaIY_MXgioyTUtZGqCEOEH8gCgnVFSpF4BSEj0qcULegI9oMxp6ivhkyRZOimihs5j5gjHVyDaAF8Q_6KhOESJFH_tlESbGHT0Ws1xfCltjUxH74odmmNwKXHa1jK44IcNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KQt2SjLGY-2eU3oucYb-AbbgwdpPw_Nvu60LWFBzgVn77RCSy7upvGyVorV_7WU5aWcI-8U8v8gOy1GkmxtV5OoYTus7hNSYwGJgkiAwNMDNpimZb_HRZ8IubnSChWO1p1eo3H9oZWrAGe5XbB_2IsbUBDkIRtr9qcmPHq4QjQEoUO21ddOaZ8_iLVor2e75-320l7sdcrJ5DOZYarDMaIY_MXgioyTUtZGqCEOEH8gCgnVFSpF4BSEj0qcULegI9oMxp6ivhkyRZOimihs5j5gjHVyDaAF8Q_6KhOESJFH_tlESbGHT0Ws1xfCltjUxH74odmmNwKXHa1jK44IcNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=Obfhk3nIvXYv6zlFFIeJNIJfbTA6rbCTHOzRE4K7VI-8ur_WeKxGmKBEW2U75UAR6tlSsj4lIB0jxP_QrvDD1_8uiUFHRV14teQ29-LOcKU8Oo5LdIPAESCyZzKkW3rc7iAuBaGcNIkbAeTojSNyLREoPE6lQ_VZlcHzka7-w-5-pvsjS_Wj45GHDExmULy1tAjpELqYI-4i6HkwT3Zm2JmYfJl42WhYpyuppGcjnHTTjoRXBsnj7UhgdjwB7hlrOoZimvE6USesuaCKVQIv-PZ5WB0he0aoxt03Q_2O7kKd8o_mt17FLDIj_LyBC4xvV-QRfM9w7BTdpQvMpdpU0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=Obfhk3nIvXYv6zlFFIeJNIJfbTA6rbCTHOzRE4K7VI-8ur_WeKxGmKBEW2U75UAR6tlSsj4lIB0jxP_QrvDD1_8uiUFHRV14teQ29-LOcKU8Oo5LdIPAESCyZzKkW3rc7iAuBaGcNIkbAeTojSNyLREoPE6lQ_VZlcHzka7-w-5-pvsjS_Wj45GHDExmULy1tAjpELqYI-4i6HkwT3Zm2JmYfJl42WhYpyuppGcjnHTTjoRXBsnj7UhgdjwB7hlrOoZimvE6USesuaCKVQIv-PZ5WB0he0aoxt03Q_2O7kKd8o_mt17FLDIj_LyBC4xvV-QRfM9w7BTdpQvMpdpU0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiyB_LTAmErkqjeE1Eeh3aCI4zCBdVJ4GcCsiC_i8kHpYvixQSN5yfKJ2yaJtgkoFdz8RJfKQtQm4eNEuZ14cJhiQbj3o66ep_dL5bcSBHCAkZ_ypTDRNn0qMqmil8rH8dX-VgJ5mygz70NZ_1l7DHz57hKtWTY6djnBfzWd0-JCZxpMfqQ80Jk8ApIQraBxADG9PayxL82V0Axz2R40vqmn9vhvErbD5Wn6pi2g1ZQ4_Q9K-g8vIVwLbd4C92Jd4CQzWrwdcLUhB_AA964C7fwwSzNHIzkwlWsBnj2QzGhJmtU-7Uv4JuM0qTGdxz1XDCH3Ug1Y2poKdnY0dPxvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=KpMMfmfPRwnzzOMi-wgoqaRrz0hdc14zqLN5vGWwFp7m9rFfE7Gk0RXSq7qkb3a_1Is_UPqMuDF4vDbGIyyo178GDeL22xCzaWlSWgSFkwEm3EWR7sROuukxm6etYGotsAU88sfbbdKSpfOxCfzCK7SAua6bNOgNV4bfHgXHmntTJ6GPpMv5mzxJbYiAwV3SLntLkarZJegwhgsPpp9aS8Ikn8enGfdie12zszCLkuxgEOqJr3b_6Lv9CxbYObV0eTVswPu4UiyiWZNXzcOlrannCyJ0bf47swGpiGoVQq-HjaAG1krNFwgVShCwvP4aSwQYhH5WHfN_OSLkxyLbQVAVj-y5teP_Fe12flmY0wWR_Zz9rxorGcCsQ3hsoEXJCbI-EbCL3C-yeuPYl3o2wSy76aXi7MdCjPnE-MKZ3yWY3AM99vXfSYVRHt6IJ0tPVpUezpzJtu8u5wIXjrcMX_E6_xaKvr0mSzq_o6aGtBEzFzNOyeAA3dL5K9E_0xcVVPn3bmQODgKg0n8KdCOAB53rl0uK0Y6n2rDn5PrAdy-5rEuEcd9qwYokvTOuNgBffJtxHujfNAW81ZourWhXFG9GPptRjQmsI1Y4s5f_XhPMOc7RFD8wTGLxHLsLtClAVPZl7AXq3UMxIQVTvQ47-5VDtQXFbUdVOgq_JQYZw3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=KpMMfmfPRwnzzOMi-wgoqaRrz0hdc14zqLN5vGWwFp7m9rFfE7Gk0RXSq7qkb3a_1Is_UPqMuDF4vDbGIyyo178GDeL22xCzaWlSWgSFkwEm3EWR7sROuukxm6etYGotsAU88sfbbdKSpfOxCfzCK7SAua6bNOgNV4bfHgXHmntTJ6GPpMv5mzxJbYiAwV3SLntLkarZJegwhgsPpp9aS8Ikn8enGfdie12zszCLkuxgEOqJr3b_6Lv9CxbYObV0eTVswPu4UiyiWZNXzcOlrannCyJ0bf47swGpiGoVQq-HjaAG1krNFwgVShCwvP4aSwQYhH5WHfN_OSLkxyLbQVAVj-y5teP_Fe12flmY0wWR_Zz9rxorGcCsQ3hsoEXJCbI-EbCL3C-yeuPYl3o2wSy76aXi7MdCjPnE-MKZ3yWY3AM99vXfSYVRHt6IJ0tPVpUezpzJtu8u5wIXjrcMX_E6_xaKvr0mSzq_o6aGtBEzFzNOyeAA3dL5K9E_0xcVVPn3bmQODgKg0n8KdCOAB53rl0uK0Y6n2rDn5PrAdy-5rEuEcd9qwYokvTOuNgBffJtxHujfNAW81ZourWhXFG9GPptRjQmsI1Y4s5f_XhPMOc7RFD8wTGLxHLsLtClAVPZl7AXq3UMxIQVTvQ47-5VDtQXFbUdVOgq_JQYZw3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXE--uW2IGJrK7WsiH4oCJ_hBwAr_KRvFx6e2Y0qpMU7TyBrliOfTVFKE9tn_B46FMa5nD0bBp6h-EayGfcxQ6nfEB7rcHSmWJQOsrqskEdNLzXKC2Z8GeA_RErMX8m3jKb9-PWUu6bWX3zQF8JhTVU_yq7bpmarblQn4D1tl__y14e_-6JqAsM48QZKl6Pj7jAYZZaG_5macsbWF7tJCuXuAq0eYWkWmqVOSfa17q5A-dmYMwKrEdUfOju8rvdWV1tMHaFkSMJrXgSmUAmXWgqobFFzYJXelgFJadrRwpNDpY8kiJKELPe-nc9mPNilUbnNLpQ6nc8UQuFBslskag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=iboWeVq9hg7jME7M2dZHmygdjSW9HaV53GF7AOATrR9iZsxfV7-PU9gA1P9lYDS130aS_rgmN5zXkMXhyRkPDULPLye_lcCbbwdZ4jqP30WZB0_yrAfFk00xKy6o0EOW0MjeLLGN0mtw35W1V3GAnuuvuvTPGvkTujFbs1vi4oJ5qTsmyoc4wzFSC66Mgc6qN8xpbRD3zQAeFy9uqHuOXL_3oVZyt27ZZZMO8SDoGaSt1VWB2ghQZ9lPi4Vhs9WPdvFlOokGySxlm6_FRCI7sppnln8I1K-Oskna1B15nIJt5Kb4P_4ATkSiNgaxcQkVMX1osP4_k3yOGbP2t3TzMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=iboWeVq9hg7jME7M2dZHmygdjSW9HaV53GF7AOATrR9iZsxfV7-PU9gA1P9lYDS130aS_rgmN5zXkMXhyRkPDULPLye_lcCbbwdZ4jqP30WZB0_yrAfFk00xKy6o0EOW0MjeLLGN0mtw35W1V3GAnuuvuvTPGvkTujFbs1vi4oJ5qTsmyoc4wzFSC66Mgc6qN8xpbRD3zQAeFy9uqHuOXL_3oVZyt27ZZZMO8SDoGaSt1VWB2ghQZ9lPi4Vhs9WPdvFlOokGySxlm6_FRCI7sppnln8I1K-Oskna1B15nIJt5Kb4P_4ATkSiNgaxcQkVMX1osP4_k3yOGbP2t3TzMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1TlDVPEk_0_VcbbeQVHKo2W30m5xmB4EyHzyKBuaDQgFPV27evA19rexT2fGEmwf1Hv1RwCNiY734kxmy56dgbZVqNnw2rj7aDaVauPMDu2aY_0hDKo2EyR4Zz0uTsehX-1zPrpLg76ZgN89B5-ONItSgkBF7_6cmqkiwvkv1tr39NdVWiqlzjUZczBqJomLcU1SIMM3CjuSBIgTgqALpIlTPuDvQuLjv1oRGbnYC90cHRzp_LKQwDhNBP_JNu9JwZfTz4D5GceJoDLyDGfxxqQIWIsWVV9-1hj9hV9-goHVXcgawP07lSFLt8YzDs-VGc68BsEZhof6iiU0xTbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/untVBjXaEHfIiTrzuY3MuFp7Nh41bM0sMy4E8f6qRTlK_K6njdIfnVZy_TfPhSW3kaXRF7jEpj3f9GgWew7okDft-8L7CTLhGrYO-R1aJode65nBaTkoDoFgjjt7g6zh0XQcNqLhGsnQ4B1Q39u7U6dl62bVkM4aCJ66qXrxm4uP7qVwwbuBsBsj9nrDeFxS12nfU1Ml5mH9e4e6fmJwZV1HMDfQgYFv2BSLqXVz14GO5bQTu2PJdF8lYjTmBErRqdGhHj7E7b-CYjxdXfP_XmLfRZCvCVAKi-WIV9V3Fx5fQ5Fg_0Qe7Y6uQQD1RTm_OUBZql2_Y4tM0aHlkUVXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfOAhFaSMsAYqc1vPPCKi5kXNKjh_toCTt3Zgj6MZBvVGAivu3i2kE1lpLeobpVdn7Lz7fn2fhOS3LaS4hd5gUn6VELlqj02Hzh8X5LjE_ltD7mR4xwLhgztf1EDhWyDGhnBfqqqTNVYUf_ZnEAZsbo9HtVA--7g2JCKQDKQkfgi1iHEC3JrWfuF-5XypaGtSjkD99CpXZwypdT9kRl9rFSlmqOk4SVPU3Sp4BJzOlXjwYVlzLwI_cinStI_r1wiJxejxrYmMreVvZxMDVcAK9TJxpUfPosijFVLh_zJLKG3G17sEA4PCYJmRxHvYw6M-TDDy9Tquj--tRfCdAIOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=S29bjHWke-4-JtLdpTo9mMvuw4lUCW55E_T2uf0OnBom6Fj9k6i0zabuz_FVpHMH3qRbGJQnI4jjdoZzbeu3xrMjpylTwuY69q2PUrCUophzYXJUZU-plk6fL2EJd5C3cOeYoKTr6htIe-w9BdtGJdz6-HGKXECHDJKg3qhXL6XpXJX0xzFNqMz1qpDvi9Y6ns4ktH-9PWu-MBI406jBDej8TmWyTEPMZS9_IHTiOBILMvJrAwEHrkIxeIWg2vJASZiot89VjXEXjKfbGhfjs1kaNzZi8ZVsbl5wuaQWE2rKCCkJ-p8-Vs7wJrzYCzt6LmiJSCJmzir5C1awE_TDIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=S29bjHWke-4-JtLdpTo9mMvuw4lUCW55E_T2uf0OnBom6Fj9k6i0zabuz_FVpHMH3qRbGJQnI4jjdoZzbeu3xrMjpylTwuY69q2PUrCUophzYXJUZU-plk6fL2EJd5C3cOeYoKTr6htIe-w9BdtGJdz6-HGKXECHDJKg3qhXL6XpXJX0xzFNqMz1qpDvi9Y6ns4ktH-9PWu-MBI406jBDej8TmWyTEPMZS9_IHTiOBILMvJrAwEHrkIxeIWg2vJASZiot89VjXEXjKfbGhfjs1kaNzZi8ZVsbl5wuaQWE2rKCCkJ-p8-Vs7wJrzYCzt6LmiJSCJmzir5C1awE_TDIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW3i63nOkAkzIDHU793LH98D0IPgozXFe6rO7CWn3rKqlMXmC1ZdmHo2LwNsb0umbRBmsiVDaXCpIEirv58UppBcElVRSXBzwicseirMZW7YOsIvHyOzf6GtsRd9oypAKhtoju-6Y4kP2qgOpwwVqaDbI3gwgrVN6_D6h4EPq4hxQMiBFl656PjbVlDmtTcidOa4FOWZe1iqXp2si-Eri3PapZ2AIXFnVj9MaeAzdg_KxzQ1NJOLkjHsUS9QRfLY3OEelFuBrz3HANK8s1PLn46yUnP_PueXw4Rr79_X8J7Snxiy3wHfr7ylqvCB5PpAKURoGltxSkRMvRJQJZISKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6H1posbbgMhv6A8XArsIfEeM5RgdYA8gjFY48aQK_z_ijIWTn8pH_NR2SDxOVaSdDdek2oQA3nuxrih6iOVwAUCctAY0Tcxt-ldBlUtVogVBJ8Hy8qtDc_qAzqkzZWv_hzW_ktHe93d_T4ibPjaHMmk02DdPdj9xP95qvgWfcgRVU4sBz2GFBtVPIg1QuAXl6w2Hm5IOSbLCJyEB82rRtvL2eZQPkeMLx7ZvMgqTgzmiNNk4cVkAVJCzpk-BHyttONI1NOm6yKeuSSHCxSpM1QodcmvhXkpmHnVp7SSdZJz_ALRfjVgUexQC8zhh_91NJYUk55WvPovzzyd6Lur8eY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6H1posbbgMhv6A8XArsIfEeM5RgdYA8gjFY48aQK_z_ijIWTn8pH_NR2SDxOVaSdDdek2oQA3nuxrih6iOVwAUCctAY0Tcxt-ldBlUtVogVBJ8Hy8qtDc_qAzqkzZWv_hzW_ktHe93d_T4ibPjaHMmk02DdPdj9xP95qvgWfcgRVU4sBz2GFBtVPIg1QuAXl6w2Hm5IOSbLCJyEB82rRtvL2eZQPkeMLx7ZvMgqTgzmiNNk4cVkAVJCzpk-BHyttONI1NOm6yKeuSSHCxSpM1QodcmvhXkpmHnVp7SSdZJz_ALRfjVgUexQC8zhh_91NJYUk55WvPovzzyd6Lur8eY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=jNxubt8AmV33Mkf9kruHLK649LUD-r2NOp1TnkHbO2VyvRBm-Q_uojw7VyF8JbgOFI4z7Cdi-aCGgwoWyt6gAmFib419TLmGoHiLAESc4syyyiJ-YNyofh_rhMjs_kCwQEkVuDAYCA3AE3kSEp6fiyNo-ubOdf4ioqbqyEqhrgmbgsEH36LWZmsSpZtX7vX7pqVxJ09ZOidT0QQtSV-Za-cII3Eej-hw1VfwYyue6DWvvzvNIeW1FTrFpBWtZOjA8pr9R3e_E8WA5GOfkvt9_WS6-p0rgVZYAPdmXsqM0hNiVeCm8QW4V42Gercyxg1uS-3PFd3usDqE0B6YypH7ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=jNxubt8AmV33Mkf9kruHLK649LUD-r2NOp1TnkHbO2VyvRBm-Q_uojw7VyF8JbgOFI4z7Cdi-aCGgwoWyt6gAmFib419TLmGoHiLAESc4syyyiJ-YNyofh_rhMjs_kCwQEkVuDAYCA3AE3kSEp6fiyNo-ubOdf4ioqbqyEqhrgmbgsEH36LWZmsSpZtX7vX7pqVxJ09ZOidT0QQtSV-Za-cII3Eej-hw1VfwYyue6DWvvzvNIeW1FTrFpBWtZOjA8pr9R3e_E8WA5GOfkvt9_WS6-p0rgVZYAPdmXsqM0hNiVeCm8QW4V42Gercyxg1uS-3PFd3usDqE0B6YypH7ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=d7JiK98pLnz7IeOEWkQnawJKNJWHy6RTt7_DqQK99hap2uX1tbEjXi8sr2zjkQ7gCvPzqalFD3g455DPiOFwqflxk2wVUDeJ_cJr0G6upqhUfzeJNTQ8rPJ9UY0CQr0pC3N1F3T9P_5wrA4OtcIA5Tpl8AuVDylxOKH2M3RUJXydngEor0Yu9BwN2lrTK4iC4QCysXC-j-01Snqgr2I_PfVGBYsMhKEqClu8yIjdjQdPHytwFclXWxBQKOxzuJDrjqbfespNqXojbm3Ch85U4HpES8NWjb-HTXFVorTHfqK36meuElIJDn1TRQccYfQIWAnhgkuGAMbI_bP3cdOVDi06t3ynX1Mk8RcrotBDjRzPCOUXsk1ivOu35AgCUo69kxXYnwTsfrF1475MTZCGZoOBUX6QGt4as5jbPXZMaBBE9WqMHpHzFEMohBTlxyUNZmBHFN8U6bHgb3PKUzBdhWxNGdXvRvA0a1HwLYs3iMaZMzhZ1PmbBeZcp84-hi8H23SO__5yBeS7Vuoe-nH8xu4ykGs_DqiEN0oELrJQyCmFSQCOJgVufU7Evn78pPxC54RTaGpeDDwK0dIpV6po5QNfi5RFH0fPQ8ImtY5p9xVjgKBMDYKt2vsF1X1Sy9yM0d0nnw__odOZTjVptZGdI_aepIMuS-zljCwZXU_aIwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=d7JiK98pLnz7IeOEWkQnawJKNJWHy6RTt7_DqQK99hap2uX1tbEjXi8sr2zjkQ7gCvPzqalFD3g455DPiOFwqflxk2wVUDeJ_cJr0G6upqhUfzeJNTQ8rPJ9UY0CQr0pC3N1F3T9P_5wrA4OtcIA5Tpl8AuVDylxOKH2M3RUJXydngEor0Yu9BwN2lrTK4iC4QCysXC-j-01Snqgr2I_PfVGBYsMhKEqClu8yIjdjQdPHytwFclXWxBQKOxzuJDrjqbfespNqXojbm3Ch85U4HpES8NWjb-HTXFVorTHfqK36meuElIJDn1TRQccYfQIWAnhgkuGAMbI_bP3cdOVDi06t3ynX1Mk8RcrotBDjRzPCOUXsk1ivOu35AgCUo69kxXYnwTsfrF1475MTZCGZoOBUX6QGt4as5jbPXZMaBBE9WqMHpHzFEMohBTlxyUNZmBHFN8U6bHgb3PKUzBdhWxNGdXvRvA0a1HwLYs3iMaZMzhZ1PmbBeZcp84-hi8H23SO__5yBeS7Vuoe-nH8xu4ykGs_DqiEN0oELrJQyCmFSQCOJgVufU7Evn78pPxC54RTaGpeDDwK0dIpV6po5QNfi5RFH0fPQ8ImtY5p9xVjgKBMDYKt2vsF1X1Sy9yM0d0nnw__odOZTjVptZGdI_aepIMuS-zljCwZXU_aIwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Kol925l7T_FnaDZk-Dz_lwx8fqO1GQwdJ-UDk5pgdlVP31haf-_t1ln-kM0L7nhjkxe5287UnP6YAKPrddJi474vxy-5EVQ8OkkR9gXz-4e9IclEbqNPfJqO14Bzk65CYhY1gs8VvM-1E0w6fDNiuxGuChHhp51wV6kCv6ZI5dv8mf1cjer4Fq4MUx9LQY2t4ix2-sDUb9qXleQEttkL-sxEUzOg4zWMRc5Ka3ideihcDKkhJKXaMsuu5YNHvgD_WMbVodmMRUUXpIXL1aqD7VlWiHvG3Hw0ZfRmCXPuLuD2H-owjB2Ll5KhB-dJlYr_ByAL9P742bdtT59gfFXA8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Kol925l7T_FnaDZk-Dz_lwx8fqO1GQwdJ-UDk5pgdlVP31haf-_t1ln-kM0L7nhjkxe5287UnP6YAKPrddJi474vxy-5EVQ8OkkR9gXz-4e9IclEbqNPfJqO14Bzk65CYhY1gs8VvM-1E0w6fDNiuxGuChHhp51wV6kCv6ZI5dv8mf1cjer4Fq4MUx9LQY2t4ix2-sDUb9qXleQEttkL-sxEUzOg4zWMRc5Ka3ideihcDKkhJKXaMsuu5YNHvgD_WMbVodmMRUUXpIXL1aqD7VlWiHvG3Hw0ZfRmCXPuLuD2H-owjB2Ll5KhB-dJlYr_ByAL9P742bdtT59gfFXA8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQltrLUmNs0ubo6VE3p93j_1x0BwZxgSnO8BT0hzKkwc73aI_RZ0g-1w6gt5BM3YdefiQMLDIVJiY31_R27O9HVHhJf8by4EvDhpkskwJai_sCGCKs5lvNFWb21jVo7QdMQZRnPfAPocD2ExN5ox_xXJm9GOsLMuGnBZEf1ToKmk2wD9L5c-aXZCvUMe_OgIRERxG8iUjmPS9NIUFEzsi7SAXhioIaWlAvRVSkdPiU0fl1N3r2j_f5fn0FgIUp6i0WE5wgolHRJeteqIrFR3M013eOevz8ecDaZ1dlRPnV9Luez5Y76S4u3OJZF6y8dJJ5gg39IGYDhhT8GDLd-i8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=MLMgYuE4X4gbM_9eKXVZ9doLF-SQyI2es__UqDA76U27tJXXx9hfJSP_dSPGHhnihF9irovb46wYAwJK4Xk_Kmf4VKo2n-iErzEzcBkXrUEezlvXTkaEx_Ld8s9zFr6WjS-JpxsAF3NQ-hfMgvexjEOAg6IMUWlRB73qRQNFyFlxqsEhgrGmqLPNYyjoZMfHq1YKQz6jWZ2vPIKe8tMhZYeO0SLaaBDbE1OKD2h4gYE137lauPHf0mZio_c1PjvfqbVjR29g5sXwdzFU_6h9RkzCw0xyP2UwW0bQSSH68kK8WZUxE9Rmi0VfgFN-BDfagNWu8CX1etZNN-_8pfLlsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=MLMgYuE4X4gbM_9eKXVZ9doLF-SQyI2es__UqDA76U27tJXXx9hfJSP_dSPGHhnihF9irovb46wYAwJK4Xk_Kmf4VKo2n-iErzEzcBkXrUEezlvXTkaEx_Ld8s9zFr6WjS-JpxsAF3NQ-hfMgvexjEOAg6IMUWlRB73qRQNFyFlxqsEhgrGmqLPNYyjoZMfHq1YKQz6jWZ2vPIKe8tMhZYeO0SLaaBDbE1OKD2h4gYE137lauPHf0mZio_c1PjvfqbVjR29g5sXwdzFU_6h9RkzCw0xyP2UwW0bQSSH68kK8WZUxE9Rmi0VfgFN-BDfagNWu8CX1etZNN-_8pfLlsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=K7Oo0O_y1eNjWKCix0wImxzFP_Nku2yFa7VzWMOy1SiYxC50L_xtALnZOfHBAoxEzB5gk_G-Fq6dmenDUYyhUvCxHJjlSkCO9u1qAh2YouY4G9SI62ihEU2ro4l8LWLEzrJ0SVHSf2fOK1dpdgKq36vA86URIAAEQ_l3Mw4RgYG4lizyhtyfTHjHPlNuArBsBlTIAzpWmmzxnaConTpETxds9yl0hMt_raNIxT8GFZgrDbEnCpg-W2KjD3i77ayM_myc1DX_asVnHji89CYFc-Ser71TMRS45RMcyK0FcWtI6cVrrfjRgdWPIpvblKqDUgTJKQjYyvvBdeI7_40-p6rC4Zou240Jh6qTm76x_Nj98qzScgRbPnOwvYbODMjP5zUuqk7QhMv-A9HqQAqD4p-NJUuDMSaNcIRnIGPiVnXubejxA0W11ssB-7z9JY8O_gpxl3RR1LeIOxkKbOO4wegX_H_GqWx7Hki_8pGj_60AtJXCt2NBC1U3QyzRsbYwFRFsoW-uEsEwHcr63ViEv0FnkP2RnkzfsHR0SFgu6euoZWZMqh1T9FeAg0KU7vb-ezbda359Y36gWZ8PRgM39VwM5yFb-75IksoSJPcgaE_I_27iAgNZ15E9aYnuPdmwzxnioQZVeTat1cULIpSWiay7YAMuROAAwNiqTivri_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=K7Oo0O_y1eNjWKCix0wImxzFP_Nku2yFa7VzWMOy1SiYxC50L_xtALnZOfHBAoxEzB5gk_G-Fq6dmenDUYyhUvCxHJjlSkCO9u1qAh2YouY4G9SI62ihEU2ro4l8LWLEzrJ0SVHSf2fOK1dpdgKq36vA86URIAAEQ_l3Mw4RgYG4lizyhtyfTHjHPlNuArBsBlTIAzpWmmzxnaConTpETxds9yl0hMt_raNIxT8GFZgrDbEnCpg-W2KjD3i77ayM_myc1DX_asVnHji89CYFc-Ser71TMRS45RMcyK0FcWtI6cVrrfjRgdWPIpvblKqDUgTJKQjYyvvBdeI7_40-p6rC4Zou240Jh6qTm76x_Nj98qzScgRbPnOwvYbODMjP5zUuqk7QhMv-A9HqQAqD4p-NJUuDMSaNcIRnIGPiVnXubejxA0W11ssB-7z9JY8O_gpxl3RR1LeIOxkKbOO4wegX_H_GqWx7Hki_8pGj_60AtJXCt2NBC1U3QyzRsbYwFRFsoW-uEsEwHcr63ViEv0FnkP2RnkzfsHR0SFgu6euoZWZMqh1T9FeAg0KU7vb-ezbda359Y36gWZ8PRgM39VwM5yFb-75IksoSJPcgaE_I_27iAgNZ15E9aYnuPdmwzxnioQZVeTat1cULIpSWiay7YAMuROAAwNiqTivri_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPfoUrZ1yZDqfoyfByMaqYrZTa3fyEqwSTjGaqQV8WUeUAkVihykYKAIkM-1lLp52R_yAdPUMT5gMnU4Ii1vrsWOhl2r9fCmMhyGeALvdoItoWdsEm_CQAD2MzNQG6iCEDUifFRLwn37YtQIchw4LOeTPWALl8cJJo5M3HROZOj1Mj-t0-Uvm-IyT9AzgLGSmOkEPy_hxf4uluBPcnffG81WKM2zc7QpwDL6Ey-bNj4f_pYSYoQU3caTi1EFTeqEUB7dzc5xFwPNXyt42SHYe_kFaw1y1YGkIvAow6pZ618wavZSZcS_pnr9BcHFk9e5g4e65E8KFlg1IvaM_KeWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=uZcYX_wFM7tMeS4moL42FHX4_f2J5i9RmGi_zxs0yAfTmJ_9bE75Ew9YZ1zGdApvmo6yVIZSAtY61c_fQ-RCXX21OcOxz8SRIBn26RdVvn-eqT5G1AI4TN9aZqApWt72bpOWkm3mfT7H62TmPJsZHqWJnq04WqCKYKtqku-2y0-848DLeUqj4d4_s71L6-DHXBrmJGV6hYJ_8p3S_0F5iG6DbgUotOlsZay6-rA9Cx0kTmdmXXfA_GSSz13B9MhgLJ7Ix2Jl8nozxWeQqJmbDeX1AY0NujboW49MyuKFBmd7EqraN24x4_DCU6Me03wg7rjjIkI5O7S94kUNu1k5WF4aZyePirTBna6Hx9riUgm1fTEMB10gxQ4FDyNk_vk1qF66dOJcUz7UHQZ4kZ9aU5L9bdEHEoHP4llC_iPdAY0ctMdX2vo2hvmCXb0wP8L_qA6ZlQnGych3UZ_R3flo5LMJ0XxRc6OZ7L0w1483tt3oVAR1KPnHOS4hcUevL3_h97tR--P_Da2XcIXVsAIw7EnQAXoZt-puAkOhDLKvFeJ_25aWW49FYeU_-pHjHxm14ADvis3wZhIpDag0sKb1MZ4xQkzZaVe1JNBzSsUIvxRzcOzTNACx3WLtAHi3K-OtbqWqByApFyRSdCib2mOCAmgQ-KOzFMs8IwdTt4qdReE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=uZcYX_wFM7tMeS4moL42FHX4_f2J5i9RmGi_zxs0yAfTmJ_9bE75Ew9YZ1zGdApvmo6yVIZSAtY61c_fQ-RCXX21OcOxz8SRIBn26RdVvn-eqT5G1AI4TN9aZqApWt72bpOWkm3mfT7H62TmPJsZHqWJnq04WqCKYKtqku-2y0-848DLeUqj4d4_s71L6-DHXBrmJGV6hYJ_8p3S_0F5iG6DbgUotOlsZay6-rA9Cx0kTmdmXXfA_GSSz13B9MhgLJ7Ix2Jl8nozxWeQqJmbDeX1AY0NujboW49MyuKFBmd7EqraN24x4_DCU6Me03wg7rjjIkI5O7S94kUNu1k5WF4aZyePirTBna6Hx9riUgm1fTEMB10gxQ4FDyNk_vk1qF66dOJcUz7UHQZ4kZ9aU5L9bdEHEoHP4llC_iPdAY0ctMdX2vo2hvmCXb0wP8L_qA6ZlQnGych3UZ_R3flo5LMJ0XxRc6OZ7L0w1483tt3oVAR1KPnHOS4hcUevL3_h97tR--P_Da2XcIXVsAIw7EnQAXoZt-puAkOhDLKvFeJ_25aWW49FYeU_-pHjHxm14ADvis3wZhIpDag0sKb1MZ4xQkzZaVe1JNBzSsUIvxRzcOzTNACx3WLtAHi3K-OtbqWqByApFyRSdCib2mOCAmgQ-KOzFMs8IwdTt4qdReE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=VcthWiPTzv_UIobviTsHlVrKgRTapx1DzS54BY1qTVAdiK1G1QOQReAWbdCr3DYLKTuQTsFDXXx5_kIKUF5D5K3j1Z9Go66IhrzLpTeurKRghnlQzjqteTrCiNkMdUuvq0JotAJGoAX8p6NDKTJeZUeQtkeCOuqRyXuekSTdYo9t2JW9mr4t6UOiclC8-gMhIqRqqPk8lA1Wd1ZJWgyA3oT1_2qH_rtKb4fzIHuncxP7qawnlVp7yxD4ku0B-wxNsz3ss9LHfcjEfDij0R4EUr7Lz2m7dnYEtn69zEqs1y4nA80P4sXiQBykafcxR83omvdGk4_86cEFXkQTanG0dgbsI2ScuHxfVrhjCNMaksZ9NU_upQaMA1gVSxZyH9wnNSJmkxLwoL6Q_u7UEKGyczFSj8wHkvhwlHO_F0JVMyBvypo2RFJTYSOx_WtRGiTsbAJs9TqXqd8ZAXyohsghq-1zyY8POLPZNgis9el34UEEZrMMhAx9VON1cLQYrQXCq1OJpERt_m1buSDiHNo7pT-ex3jFgrQgx6w06u5EagYjeYaIxw399pjBqGjSVSTGD-QMqKTf7t9DeNKJyZ_IHfPohOd8Z3FGgHt4i3mmAreEzuZ7ayJVD30EhkvinBNB2x13H9_cO2PHtzUcWQqaPV33cYbASY_nHJ6wnkJGv3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=VcthWiPTzv_UIobviTsHlVrKgRTapx1DzS54BY1qTVAdiK1G1QOQReAWbdCr3DYLKTuQTsFDXXx5_kIKUF5D5K3j1Z9Go66IhrzLpTeurKRghnlQzjqteTrCiNkMdUuvq0JotAJGoAX8p6NDKTJeZUeQtkeCOuqRyXuekSTdYo9t2JW9mr4t6UOiclC8-gMhIqRqqPk8lA1Wd1ZJWgyA3oT1_2qH_rtKb4fzIHuncxP7qawnlVp7yxD4ku0B-wxNsz3ss9LHfcjEfDij0R4EUr7Lz2m7dnYEtn69zEqs1y4nA80P4sXiQBykafcxR83omvdGk4_86cEFXkQTanG0dgbsI2ScuHxfVrhjCNMaksZ9NU_upQaMA1gVSxZyH9wnNSJmkxLwoL6Q_u7UEKGyczFSj8wHkvhwlHO_F0JVMyBvypo2RFJTYSOx_WtRGiTsbAJs9TqXqd8ZAXyohsghq-1zyY8POLPZNgis9el34UEEZrMMhAx9VON1cLQYrQXCq1OJpERt_m1buSDiHNo7pT-ex3jFgrQgx6w06u5EagYjeYaIxw399pjBqGjSVSTGD-QMqKTf7t9DeNKJyZ_IHfPohOd8Z3FGgHt4i3mmAreEzuZ7ayJVD30EhkvinBNB2x13H9_cO2PHtzUcWQqaPV33cYbASY_nHJ6wnkJGv3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=dxm7UVLOoyESkXUwObwwgMHAdNSCg9_-X_a0WJV4glEaCopf_Ehc_LwjPKSo8xKbODAom-2b9Gv2j71d6DmK5lluA7xbQwCWVxxpBpPnInDd-NnJzuQwCQgsi9GN9z_FGwX37VEg8TJlhCx2L38a2341ZrkBbfwtjOFwzdIQ6VXFRT4Sp21r0MMlaIHuFt7Fob6WI340DZIZpGh0qDib6eX_9Qk4FeEzgT0JVio2uRm4WsH0UqrQo_S_2O3APAz4KHS36KS7h8q1N9zFuT0zkcXFF2vdOB2uqr11qDFaOwKoT1NqTuRFPtbuubKknhKL9OGJ-ghFjPYQCkkJmPDqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=dxm7UVLOoyESkXUwObwwgMHAdNSCg9_-X_a0WJV4glEaCopf_Ehc_LwjPKSo8xKbODAom-2b9Gv2j71d6DmK5lluA7xbQwCWVxxpBpPnInDd-NnJzuQwCQgsi9GN9z_FGwX37VEg8TJlhCx2L38a2341ZrkBbfwtjOFwzdIQ6VXFRT4Sp21r0MMlaIHuFt7Fob6WI340DZIZpGh0qDib6eX_9Qk4FeEzgT0JVio2uRm4WsH0UqrQo_S_2O3APAz4KHS36KS7h8q1N9zFuT0zkcXFF2vdOB2uqr11qDFaOwKoT1NqTuRFPtbuubKknhKL9OGJ-ghFjPYQCkkJmPDqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ORVBIX-OMC9lzGdrFVFiMZqcKENzwvPKGzK2tyt_SJ5eSCdCtlf_Ni0ueJtrqZ7veaqBynbt9rztQYFZXMICNfAJTBAi4ryXMWAgwZ6DZu_kJ7Z9xfx7OW5X0IzVOCqN1Pl0X9wB2a4cXqY_SsHVXTFO5u1tlA_T3yeg2BVvAV0V-h-CEu_AbXtaNcKXuNpPXZoiiVNg_ndOaXUp3j0SqFt0TGKxAtkkURtgxVoL9kCpujCe6OL_VOnPMxNIkP5IC5vH-nZsKnVSda_PXgo3FqMDFxkRnijRw7mC0wrc9-XhOvgOB_uGpSkslIn6nz4Fc9YPzEJpvnCXe5tU6ss0Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ORVBIX-OMC9lzGdrFVFiMZqcKENzwvPKGzK2tyt_SJ5eSCdCtlf_Ni0ueJtrqZ7veaqBynbt9rztQYFZXMICNfAJTBAi4ryXMWAgwZ6DZu_kJ7Z9xfx7OW5X0IzVOCqN1Pl0X9wB2a4cXqY_SsHVXTFO5u1tlA_T3yeg2BVvAV0V-h-CEu_AbXtaNcKXuNpPXZoiiVNg_ndOaXUp3j0SqFt0TGKxAtkkURtgxVoL9kCpujCe6OL_VOnPMxNIkP5IC5vH-nZsKnVSda_PXgo3FqMDFxkRnijRw7mC0wrc9-XhOvgOB_uGpSkslIn6nz4Fc9YPzEJpvnCXe5tU6ss0Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=vWn3my7T7ZLgs2Q15oXZrAmiPkIB5ie8qCfyOWaySQE7xvJfvb9vdTgswCNcC2N9VyQVeD25IfPE7uhJEjr0qBywo2gWGkanf5T7jGUn5Mio91Hf9vlnfFmglsNMWspPmUg3kUv3Q7KT3Qqzl98NhPgUbNxsgUZbJIHDqnPVWkcgEb9cJATdIitsjWs4oZLtNT8PTZb0bu0Ul2o2MfhU6hIiW9227YP47mFifg7JzRbHp3Fh_A70G1UMso5cTAlYc-tCkY06Tg1IK3Q8zPgliiOrOA5G0XY-fpEWtjPEuydiyPegYO_2vUqHtrA6yWaZop_E3gq2PGGjmjqaOzL2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=vWn3my7T7ZLgs2Q15oXZrAmiPkIB5ie8qCfyOWaySQE7xvJfvb9vdTgswCNcC2N9VyQVeD25IfPE7uhJEjr0qBywo2gWGkanf5T7jGUn5Mio91Hf9vlnfFmglsNMWspPmUg3kUv3Q7KT3Qqzl98NhPgUbNxsgUZbJIHDqnPVWkcgEb9cJATdIitsjWs4oZLtNT8PTZb0bu0Ul2o2MfhU6hIiW9227YP47mFifg7JzRbHp3Fh_A70G1UMso5cTAlYc-tCkY06Tg1IK3Q8zPgliiOrOA5G0XY-fpEWtjPEuydiyPegYO_2vUqHtrA6yWaZop_E3gq2PGGjmjqaOzL2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=YV_gcXhp88Vn3yOJf-5gdMRFMtJmWjV9rn-uMQ1YUCA0BqaLaaJweiNM5hXIw-n6Do3CkC4dCjnsNelM4ds2zP88UJVn7TlhBJwWtIgWbpDdFOejnowdzTkiVMEpkSddJtxn9sapx4ETgyN5nPRGaoe_kgmMI7lbaMAMbUH60g2zUJkOqPUIWhZ5jwLp-h6fmpuTdzLap1yJsChJDKIwOz_fA5qummuwS9GyrjrgM44mm1yFbteC3gTxqmVUbvewM1ZkhLyaxBxG9RasVl6gIxsOzd4NKL3SWKjFGuBw50iXW_Bn3mXIU1mTfr_OcuKXSzTvtDGXgEvOJvau2EjHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=YV_gcXhp88Vn3yOJf-5gdMRFMtJmWjV9rn-uMQ1YUCA0BqaLaaJweiNM5hXIw-n6Do3CkC4dCjnsNelM4ds2zP88UJVn7TlhBJwWtIgWbpDdFOejnowdzTkiVMEpkSddJtxn9sapx4ETgyN5nPRGaoe_kgmMI7lbaMAMbUH60g2zUJkOqPUIWhZ5jwLp-h6fmpuTdzLap1yJsChJDKIwOz_fA5qummuwS9GyrjrgM44mm1yFbteC3gTxqmVUbvewM1ZkhLyaxBxG9RasVl6gIxsOzd4NKL3SWKjFGuBw50iXW_Bn3mXIU1mTfr_OcuKXSzTvtDGXgEvOJvau2EjHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=n0xcWw_15GK-L5G1FcsUNDDQ6urB4RfOv8dghldQcPrqcrSz8VQOZUadS7d27IzFmQ2SfAERYMx-nDnjNjjPF6UD3qXi1oXLNjGDupj8noZ7Fr6vTNE-Kqp0uGsLeiqAz4SkroI7-XFbnUohZfudFc6JNPfR8TQKZV94r5Ag8Lzs_hT7CJ03oKEcEIJ8jU5FfaQRF2b9rpuKh2zgFgVHmMV76AVsklq7iKBrBSFeLo1giVFUG_R3Tz6vC1SWvU6cDXhTy03aiugmbav0OmvqGerLCgEBYobrituX5p_ATOv4IeeJDc6Ck5q75huQXObbVym8h1c0xqeQTs-4yb039w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=n0xcWw_15GK-L5G1FcsUNDDQ6urB4RfOv8dghldQcPrqcrSz8VQOZUadS7d27IzFmQ2SfAERYMx-nDnjNjjPF6UD3qXi1oXLNjGDupj8noZ7Fr6vTNE-Kqp0uGsLeiqAz4SkroI7-XFbnUohZfudFc6JNPfR8TQKZV94r5Ag8Lzs_hT7CJ03oKEcEIJ8jU5FfaQRF2b9rpuKh2zgFgVHmMV76AVsklq7iKBrBSFeLo1giVFUG_R3Tz6vC1SWvU6cDXhTy03aiugmbav0OmvqGerLCgEBYobrituX5p_ATOv4IeeJDc6Ck5q75huQXObbVym8h1c0xqeQTs-4yb039w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=t3j76rMQGAv0fzB-9yicw2ujsPSoMAIETF3nS0a5E2ZLCvN_ZfCPncsDxfzHT1Ix_1rVRe0mo8JK-vjaS7kiwAqta4ufjmUYOy7tL5L0BkYh8pXtKvPc6LaV9rrOCo6RVygqxqAzsuZSZoeCFrhtCsP1s2T9j6ZROLhm1ah55Pgn10h1ZZ-1dVPmHYtp5on70KMIa6kZ8OjMZlIN70eYrWbHKLivL65li0FQUbFHl9tl5XyNbG4nqFvgGIOmLOYr8X_yTWWq8pgGa9LpHQ7F_NwdcfxmfUq6hoExVSebEpn7i62LGO-3O6KzqAJnGFzMtSmcQOo_VBSq_agMlGP12w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=t3j76rMQGAv0fzB-9yicw2ujsPSoMAIETF3nS0a5E2ZLCvN_ZfCPncsDxfzHT1Ix_1rVRe0mo8JK-vjaS7kiwAqta4ufjmUYOy7tL5L0BkYh8pXtKvPc6LaV9rrOCo6RVygqxqAzsuZSZoeCFrhtCsP1s2T9j6ZROLhm1ah55Pgn10h1ZZ-1dVPmHYtp5on70KMIa6kZ8OjMZlIN70eYrWbHKLivL65li0FQUbFHl9tl5XyNbG4nqFvgGIOmLOYr8X_yTWWq8pgGa9LpHQ7F_NwdcfxmfUq6hoExVSebEpn7i62LGO-3O6KzqAJnGFzMtSmcQOo_VBSq_agMlGP12w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=gu_h_-ySYW8Uibl6F41Q3aHH435k3ATZDN-NZkJRiOgkfLuVd3pilzT8rF3_18q0pbT4BA_vzvg0NOi5lYYx8rXGgV-rrXYZiWjo-duWBFAKLYBKddREo2IaIv9qhmfwde-w0zLu8TuaAQKYcr6rJz0sznZTiziVtw6QeefQvdMXNkqZdajx4e7Ym5RT1XA4lqGAAcO-juEZ7NbvXQxTdg2XL9QLNZcigmPblEZKsDKFSqse1GTAiOqTyHWZbayAvxGuJUAh4iQLTu1reyYnfC1ROrolrLyDmDb9VlOWZ6KagMVo9cUAz6yX1HmthaEIvUkt3biYhpvupeZH0TUNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=gu_h_-ySYW8Uibl6F41Q3aHH435k3ATZDN-NZkJRiOgkfLuVd3pilzT8rF3_18q0pbT4BA_vzvg0NOi5lYYx8rXGgV-rrXYZiWjo-duWBFAKLYBKddREo2IaIv9qhmfwde-w0zLu8TuaAQKYcr6rJz0sznZTiziVtw6QeefQvdMXNkqZdajx4e7Ym5RT1XA4lqGAAcO-juEZ7NbvXQxTdg2XL9QLNZcigmPblEZKsDKFSqse1GTAiOqTyHWZbayAvxGuJUAh4iQLTu1reyYnfC1ROrolrLyDmDb9VlOWZ6KagMVo9cUAz6yX1HmthaEIvUkt3biYhpvupeZH0TUNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ3n_q8GyRDcxsCaF9toXCgo61tE07gX2DnvugIzMD5h5nUBN5nH9Pvz_LB4oHtmE_JTcJtQkqzsx1cMkKqaomcfB36bGEfkUJU2zazT4vM02DKmrZbVyy5M3AFb-RmQfFZ0MJ9imR_0EXOZp2SpU0SeHH0cj6SiXeUqh6Uj0YXo-J-Ht7sHPNfdmPjdKsRx8_nrQcPMvq938ijqcJamWpmp4AQQ3pKtRy512Vxkg8psUw-oGtHqrW-vlPyLZqHqMmICZIUvm_Q05KdY2XF9BG_jYOqf0y_gGmWfUJsfqyJuVwrtEWKt3dTSGK7JHjwU_3S8Z-xwChkvb01_ppA60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=jjoKVHxtQenNW20FvMxR2bx7p8qYEAaPGbm1d7T-xUH06oDFG63F4bC8llOhRKjJbDtOrglg3IDMzrxcb515KBGhHuKXV40g02IpHmIlBIFzhCqx7cv8oBs_4JzIBymFzT9utXQ56IMdMxT3y1FbCkJ8w9UDlkrUWpXoJatuA6C1Nl_q1SrGCG0XmrFkBNJ5qe030X_7-v2nHX4WMji-ww3-OoLzDMlPFToVxPhTqrCKtTWX0RJG6gGsgdkTidVvBv3jg_IACpltcxmNRoelsFfwZhTHBXAryZobTl1x5HOmSBOdpcozrJ-utXqaA_WU3zyM6TG9yH2ssTC4q2RSQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=jjoKVHxtQenNW20FvMxR2bx7p8qYEAaPGbm1d7T-xUH06oDFG63F4bC8llOhRKjJbDtOrglg3IDMzrxcb515KBGhHuKXV40g02IpHmIlBIFzhCqx7cv8oBs_4JzIBymFzT9utXQ56IMdMxT3y1FbCkJ8w9UDlkrUWpXoJatuA6C1Nl_q1SrGCG0XmrFkBNJ5qe030X_7-v2nHX4WMji-ww3-OoLzDMlPFToVxPhTqrCKtTWX0RJG6gGsgdkTidVvBv3jg_IACpltcxmNRoelsFfwZhTHBXAryZobTl1x5HOmSBOdpcozrJ-utXqaA_WU3zyM6TG9yH2ssTC4q2RSQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=QwyN6LacGa0mDsbZpRUIb8M8A4Q921Ou8A0Ew_uvVGb-bBZOc8Blxxe-D_jcMomiipXmBhC8Cx5VAS3YfZLhU7cDv1zMsbvM6jMC1qYCfCaR_7WvdGKnJxLDkX1FvVYDz8gtu4OQGLHH_ghfGW9hhUyz2l7fZPiKizvFP0HyAIvjAfyOv00rRXO9aGTaIxN8qfHNanl6Ci-Baane-MO7ZK4ozlB5uECkodJgUAmX6VaCtdUJrRRnsnFiMRxEEFtLRKmmuOgRmwQLKsLJJizd3u-15fZ1dBsYkpfckn8LHcEC0JKWXUQfvbKEwsx7HcA8V_AqpBN3YlDpZcBHkLT0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=QwyN6LacGa0mDsbZpRUIb8M8A4Q921Ou8A0Ew_uvVGb-bBZOc8Blxxe-D_jcMomiipXmBhC8Cx5VAS3YfZLhU7cDv1zMsbvM6jMC1qYCfCaR_7WvdGKnJxLDkX1FvVYDz8gtu4OQGLHH_ghfGW9hhUyz2l7fZPiKizvFP0HyAIvjAfyOv00rRXO9aGTaIxN8qfHNanl6Ci-Baane-MO7ZK4ozlB5uECkodJgUAmX6VaCtdUJrRRnsnFiMRxEEFtLRKmmuOgRmwQLKsLJJizd3u-15fZ1dBsYkpfckn8LHcEC0JKWXUQfvbKEwsx7HcA8V_AqpBN3YlDpZcBHkLT0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=DHRJnf2UAeajgVCKGt9Qxbq1S5XLZFU0rLPV7GnGXKWgfiLxKCPCg4gEBKlkLEmhcouPu-4e7uGyDbF8bVMMLY6znxnsHgL8OSMG39cfkuPaEAyh_Nx0XWip6ZGf_WFXKk9tFW79VNCNCMUFbR5NwuiZDzRgLKnnrSDyqo4vOnGkeOZHeWax3zRy9teNax1gQS2O3m9zwSVA_rqApm3lKgMFgo-Tdt4_ZUeCx0zYFtoz-_0ChBk__3qnNP-oOG5iZwvE3nqqnlD-jX6_7CBxEWw_pjQjag1dDsQLWrj4EjaUWCOIWjTwu9np_eNV9bchP2FoUaH8NuJxW_bYfqlVew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=DHRJnf2UAeajgVCKGt9Qxbq1S5XLZFU0rLPV7GnGXKWgfiLxKCPCg4gEBKlkLEmhcouPu-4e7uGyDbF8bVMMLY6znxnsHgL8OSMG39cfkuPaEAyh_Nx0XWip6ZGf_WFXKk9tFW79VNCNCMUFbR5NwuiZDzRgLKnnrSDyqo4vOnGkeOZHeWax3zRy9teNax1gQS2O3m9zwSVA_rqApm3lKgMFgo-Tdt4_ZUeCx0zYFtoz-_0ChBk__3qnNP-oOG5iZwvE3nqqnlD-jX6_7CBxEWw_pjQjag1dDsQLWrj4EjaUWCOIWjTwu9np_eNV9bchP2FoUaH8NuJxW_bYfqlVew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ff5hT0uqcFhXnDrlZ-4_Vrpuajzaq9LGIg-7_rZN9QaxkoISJ08-UxTgXNY8Sy8nv2B6glWRLXqdIzWv-___YTJiIBSps4CkwsoaqnZ6nhZmf2XWyWsEcRG8r6pj86A2utI5-sE5BaBgRl7pfMmUbZFspcXz0lSJjjbpgI2qpxNO0vF-mQe9ok4Zr9cj_ZIOJhLdNJpFGsQwlAaFZm1MDhmpBE7sqsbgFTYSy4e_tmf2XhqlmifVVUbR49gcY58gKNi845BZdNtNpBea_NcesM7WVuy7lg4jCEQXEk5b_ccST6Y_isV6Fa8m5I5_8bAo9FBejJy0KnXWyu0qDJ1aXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ff5hT0uqcFhXnDrlZ-4_Vrpuajzaq9LGIg-7_rZN9QaxkoISJ08-UxTgXNY8Sy8nv2B6glWRLXqdIzWv-___YTJiIBSps4CkwsoaqnZ6nhZmf2XWyWsEcRG8r6pj86A2utI5-sE5BaBgRl7pfMmUbZFspcXz0lSJjjbpgI2qpxNO0vF-mQe9ok4Zr9cj_ZIOJhLdNJpFGsQwlAaFZm1MDhmpBE7sqsbgFTYSy4e_tmf2XhqlmifVVUbR49gcY58gKNi845BZdNtNpBea_NcesM7WVuy7lg4jCEQXEk5b_ccST6Y_isV6Fa8m5I5_8bAo9FBejJy0KnXWyu0qDJ1aXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ3EP9S9bKsane4gQOZigZwhYGJ3nJOLUahswXvx3cGqNSEfYVtD63zk_VLkUVTHFP5xpnWN6Mrd7v5-xA4ASdrITumib-AvVBLa5UgWS8ZyaxxzKru6RBlVH0o93RX7qs7p1zpnIRnY-WA71hsTAWrVhe9p3LSkahZfIRVsK5XuM8Xf5VDEZVObUJYE5l51adM3uyA7c-VLMMBfXabYiWbV0qG314xhBf6_BSHgabEM_wsTGa9AT1jELitOUJ0MrauF2UdGZ-t_GAmu9JFk0QMvpkYLBFNO6Px4G_bzxKdLXDGy4GEdyU-Jz-5nhr3cvSovomLxuM7XU7cmMTK2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=phz2pW0PbWU1xCOapBLhvO9TOz5EcUw66nnF3NLOdos9RT9Uxlpl1-Q2pKeMmBgyXgjVxfLmaXkaEbaja0ka0JCaJeayXlVgll4G4lczst47o3eRB5gRLT9gVyiIsvC_4D0mNExsXNatIruzhbNs8LmdbIAP02CGpKOAQfAoEmo16GeMWOzmt1gSSCYCVMTCDXboXNmtJVvhmZMiOo1fWhFc4PVnzL37eN9U9XS4P4Ch_-eOV_LxXN5S9CGQrDLFlG2KXtNt8De9K59T5Fbuj2evDMmAQQpFIRHP1snJbHqr2XY0dAT9X-xT0yh3hrwUvYKZZaGZl-CvJjYvyqAFaTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=phz2pW0PbWU1xCOapBLhvO9TOz5EcUw66nnF3NLOdos9RT9Uxlpl1-Q2pKeMmBgyXgjVxfLmaXkaEbaja0ka0JCaJeayXlVgll4G4lczst47o3eRB5gRLT9gVyiIsvC_4D0mNExsXNatIruzhbNs8LmdbIAP02CGpKOAQfAoEmo16GeMWOzmt1gSSCYCVMTCDXboXNmtJVvhmZMiOo1fWhFc4PVnzL37eN9U9XS4P4Ch_-eOV_LxXN5S9CGQrDLFlG2KXtNt8De9K59T5Fbuj2evDMmAQQpFIRHP1snJbHqr2XY0dAT9X-xT0yh3hrwUvYKZZaGZl-CvJjYvyqAFaTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=EVaYNbNdNnTObw1szR0Tt_n3v02S_v-oDddVItQm78hVNPWIj500nkotqc72y8o8gRw5jh1ADMMs1ngQpxhxTtTV1FXwDCF_p6-VUf7DF1DMtxSCpMxzBOXcGfvzrWafpTVvq_Kh8LPdHWdJ4VYjKBuz4FPfHsPnJTL-N8DJS9lztg2Zx1JrbgH0ObuuOmUW53w7L5R8Sq9MXrvV_AQfLk2nE7KAMvWcIsa97eNGNdh42UVr27g3nU-xbR5VZNdmp3dk5lzqm2GGoTd6yToYY_b8hyRzov6qzzUrYoKr7PuUHjKpX0kNn3DqHGXOZ-SrtVSnxt5ZYJbTiP_ATDSq8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=EVaYNbNdNnTObw1szR0Tt_n3v02S_v-oDddVItQm78hVNPWIj500nkotqc72y8o8gRw5jh1ADMMs1ngQpxhxTtTV1FXwDCF_p6-VUf7DF1DMtxSCpMxzBOXcGfvzrWafpTVvq_Kh8LPdHWdJ4VYjKBuz4FPfHsPnJTL-N8DJS9lztg2Zx1JrbgH0ObuuOmUW53w7L5R8Sq9MXrvV_AQfLk2nE7KAMvWcIsa97eNGNdh42UVr27g3nU-xbR5VZNdmp3dk5lzqm2GGoTd6yToYY_b8hyRzov6qzzUrYoKr7PuUHjKpX0kNn3DqHGXOZ-SrtVSnxt5ZYJbTiP_ATDSq8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SeTf0YMpLZQzpXraQjcg-m0Jwxq2ufnnGBEZfPARzZprlC6RiopI-j957V9av_YNCzJ_zBoOwrTPfUPcrGP2V5mzo9Cm0hSEBr9GZcusG_qZtx4PgXIul1OK0q1m7AkHPTBJK3Xg97ZnCkCTW7sDftSWvkPbVSSeDRialL3WmwY5ywgXAVtK12XIXFUhHrURDYa3tu-yO3RQTJeOOsLVYk11ubg1UPS3DZD_63EeoQ7ZBUkK8Xm1217OVK0Ge71u6xiSMk0T50H526-1YtPMnRxr98urj0XuQb-kPPgR3yuF5DI4TwcT835N-eG38fTyfkh-pBfasGopie3W5Q9WfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5yPjBQY0rGTCKP4QSpYubX0DN0gsdtsedCJm5AJEkY16xsa75JpvtOB9a33BuOmn00-WGfu88W0nHH1FiZ6CEM07V-YDb-xVVodiwuR1xdKLtb12MGhI5tRo6L4X5uAuHnpItLRggIJBq7khu1Q4kjkHgSNzzfe559diGH-kayWw_kpYEDJke9CkAwSBioAJN82QfGF5GZVUPBu5Iu6chNaoMAxXC1Qn79BKHnfYR5bawyTcHkSw3UpiafmVxtlDMdIeuWThAm74IUdZSUtWwx4xhyrSBkZ3Kly6QNXmZc8q7-7i-q7QLRfJDrtFfGHG1Q-UTwCXAS_sqQI1Lgh6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
