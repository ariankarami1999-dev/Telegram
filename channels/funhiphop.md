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
<img src="https://cdn4.telesco.pe/file/cHYioJ4MuHuf53wwF6Ws21Myu5oOan9mcTQQKDfvf3XhowgGWEnQumb7w587LqmbJEBUa9WL69l70h2-haXKKgqYA1CRtr8Akoj80zWuxk2V_5IO8SAnABPhBMLuaVrKz5yItu7V0SNmKcuOXYxgVWlEYt4LJmhIiO0YmEwYbW27AOOkERMI7tfAT4RiP40pMIw91ZWQbgOxa4F4WHr7wT8A-PpDzHGXD5bpoMLFYYA9s7N3H6ZLmrWNZdqyTSC40DHehGQd7wOT6ksu9Pw3ZdGJHBre8vCQZYKnMaDJIPuYB5QWTWf0VMbX6ZjL6wuvO7xdIeyx0epImy8XJAJGHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 208K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 08:33:32</div>
<hr>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کن این قیمتای بازیکنا که تازه داره تو مارکت معامله میشه رو بارتمئو ۹ سال پیش میداد برا بازیکن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/81336" target="_blank">📅 01:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فیتای‌ کنسلی بیگ شگی با پوتک و خلسه از آلبوم اکتیویتی لیک شد:
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/81335" target="_blank">📅 01:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojJn11NE6alK4-y_ofQ3BP1tFimyihxKebXagmJGvTpKWOt3sm_AViQ9njtC-zTCAb_L7lgrRzDybs9I_S7k6rveXK4LtgG-DBp4QT4YGME8YFgNwSp-a5riyYlJ3oM79TvQQqPGEXK1NWhY2ohLWVHi8J_hBqrvDuEtuMG6JL-_6bojeA7gMfXihsRpLsRu6909wqOdeNFfZqp7Cd52lzj5p0yk8HzDJIQZ044XrhfBjQ_UqXcvFOdcx4hzQ11PfsG8U-iWxS43geofpwhpKlXePPDHEzJ42S90n318qr1J6BA_VhmHKnKdohiTfcH7Rzpnez2RPj_EpK7v380wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ue3p9jEJl15pbG4nxHurkMqeQgS52SlZ80_BRVCinyodCJ0y1bYY6EHhkSHZiR7J9gMAOQjxFcSultq1G6j6-yjj7EekH9728HMIQTUjSktOckNKlytfWXB8r9VapmKCdWahJ_sl0pU33x6cdooZ9TvzYgq9EWttkytN7UWThwt5d_HiCM8uUWcJ1WyPSep9qN3TEGxovHbmBGXHO1N5YLuuvtCiFe9PPqmZ1x_b7UyjKuPDbRPwFBd4cN8cdSQeixKcDBP0TLAzNDJ4NZr-A9Kmqh1YW9zj76WPSiC6QPKSGdOoDBpmnMEyEaqTCRq3EjAvBa0ITa7xdKLWs1SXjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vscp28LI2jlAJctpoDZ5GqtncGo0vEIYdcgH1Oe4FwZcpP6PayiyxpQFF0XBsa-KdNumPWUyL8R6pCCQf6fvDmhYF3Yt2Qon9diR1vzJ-DAdWloiLTOYb8laRNQW6wCLmBs8IrIvSZIzbEchkeAzdO8DSj5IqjnW4ZjHrrOOA-5GmRXcraqktIDaDxPJQySkx0DFl1mksBlbNAteiVJzohFcPxEEyjt7i3DFd_YSpMvKigyclSCmW_EU4mIla1m0DU9s-ktfymVQj_ElpeBwOK9crf0hPye4f9rItjFwGcBvWrMs0OnfQcoejzmi5E6nlYhmLLt9ULVk-imKV54Uvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODxP0qRp3y7TQpNMgPJzD8AplddJ7dLA-Z1nNNT5pl01SrgqUfhYjTmVRZ0qOzGbRZm3VA26XBe7qnqI7oqKf-cHX8qK1wP96kTCo8T9qhuRgUV_3GtftWqYCitNVCwcaZ6FuR2Fb6SKEqvqgBIsghbnk1hV1-sD2J1UN0HmTGLpU5x_maexe3BJO9AYpqPhjD6dsQGGnwc-YZFoeCTZ5iMlXRSldJ75mlQmvISQNalLKgicyjpAJlLzfD5eJr2EDvDGEqycD0ACT3jJsq_-pW81yIgaPovPvw7S24Fw_TIjQ3-zDobz7qApwq0Cyt9rdYZgiovGhM6c_Ozx-VETOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ob1fCVD8r7p3NhgB9EIN1l8uquMD-c06rVy-OWxfQfDfAr5y1EGRcQs_8G6jw8U90qeZ-y-VS-jEl2yWsw5E89DKDGl6RR3tKJ9zSCfZBe9SVhELnL7ZSIrBrnhTdIUdQa3sDpzukKDCC7GcJWv_SamJPbivpgpxBY10dHN3k5_Gyn0mc25DDHJtC8GwB2rmtUXvGdNOJrTVlkhzKNceQxsWb8cJtz6TT-ouKhTPPh3e3ou2nWQ9oY1g3iAgyxCSEsrvP0fucFUzpmPtIQKiHVxtUnIUDv6jDMCyshs-1Zv7EDXYOp16EtFL9tVHIuR_oQRCQGfXXTQkbKTG5smtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJbQuLCWVHB7OsDyVt-ITWxLQixuwi-dr3gXesaW6o7V-cuJqRH7XcwOvGDOBTxhbM4e4-7JxM3mas6ITzmZChATIGxuSzFYjEclSx6Pi-XuCon8MZ-NJyRGKxPF10SbuY6RB_8Wgdg3UAgzUtCxCoKaXys5SPhTir7_J7QNsfuYQzsF_V91dFkzdhuTwWPE_ttm1K-jMPEBTMjC20eRWxeSQjUGVJA0AMdv9IxqYcHYTernRJ6JRdd7vR6OF4qPGG1YAvn7drAmmK-cBjcq_74FuF1_z26dFjA4qjwxDBbln0_H7PpNV5Y7EQwwM8zJ3CwHHhUrk3RZS2n53sMTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iiq9bpYwROXDBjNvtnTvElkAbiquLW99OKrdQLqyVOAF6QRrv-OAAm1aGkJY1J3UvDI4huDp5bjwpGaEHb-K4os-lUDsNQQLJpxqXACGCgIrCTn9CPmOHXOVk3FwBm3nQPikDKuGkJRiCizFyIhzmHdIGjbENmokBvaJzAn5pPQotaIrVa4Lcek9Rit8WhZjc955BIq6QL0P_KWEWf6sBZoWvL9W6iq9c-OYvuBqfMtX9pCwwfHkUn0Iyi7HYZgnlVvZGD0DNfmHCvwQSFRNbXkt9LpaMEp1tDLcBlAKLIHJouVovKeJZHFqnmJJIjb0AUQ8uvPDsD1uML8Dk61rXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsIfWrybWGecjnJzkyFnLjtcqCZyyVBAZHsbN_KMBhD6hUDpeu4iF8PIanOx7Clk3MsYl7_VhSPXbNVrQ1IQKI4DE7Xaalm_RFZxAlH_iknHfXRi_mgq4LWPXlsy6b18eJRhRhMh1-ySLGDyjq5tzOMberFOVvk19_XxWhRRvb2v2v78eGu-lcNXZtm86iRWkdMNfJWDi0UmTTMld84sPJUSav0eFcJQVNzM3PItpB_oIEJSK5-PIgk34F0cjLpsUe_zvbsJsTYVasrWXgetFKTczBi-nce-CMzkI-y-yW38JCZaI0hDOpE7rlRzUPOJq4GmYBcSLE3xIQ02iFMF0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید بازم براتون جالب باشه بدونید که انگار بعد از مدت‌ها پول داده اشتراک آن‌لیمیتد خریده و برا همین بعد از اون ۱۵ تا نه تنها متوقف نشده بلکه تا یک دقیقه پیش ۲۶ تای دیگه هم پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/81327" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB53_16xmlCpuKz-sljh38PM3yhxKS3u1fGGokp54rlNOnwmtPWce8_2g4us1sQbOwHI7qvfgM-_0afHfdYqGbyyU9krc-3vAOssnuYFGYRMq5_WUonwYKuvc77WLNK5eQfbGedI3SImlGShj0w3ImpZ2QUm2cgDwk7VLYrQ-7lRR-tSxtn9Bns-tWtTSUWZ9H8_NxQvEMA2g_SsS9_L203n8IwtiPQ6n9nTh8m9aRmWTCfNlfSxIyXA2hdpMSiO4YE9aDo9ZZJVXuKU3-T_B9PrZk1AUlMGF0LrQSq4FCfJ0NrKd5Jgrb0J748npsLQdKz2bEN-AMbRgav405FWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگه گفتی وقت چیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/funhiphop/81325" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/81324" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/81322" target="_blank">📅 00:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">جدی جدی قضیه پژمان جمشیدی رو فقط برای پرت کردن حواس ها از عروسی دختر شمخانی راه انداخته بودند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/81321" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8KhC0TRkm7UxYJT9FTEsjngRhO3asdUJ5otdjQZ9OvwF0fWEyXlX341krYPSjjI7EVfNRR_G3yzWP1QEscprf6xsnNl-iaIf8JTEInQhkL_K35XIhlTy_wpJbpfhGMQdyBjgTt5fLN5VTrX9ULglDdCFxUXm3TV8dHu6w5zw1jj6LwXQ5r7S3597ccOEo7Z8uJuSDqkWCOa_SaS1kqPrs3KEOYAe7gi8XVkOF_0J_u_AexgwES3flcuQXTh5clWWexenBkrZQFc8iIMu76u4VCkIh54All6_forBWOBrZQ6spjGdNUaieau8la9Z5pwBYurba4-lUyPRqTFIK5c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MD4Yi1yvoDOiHr1kkDEKl0n3YSD8lMCEtGagDPQ2hmx0a7EF2xAu_YiMDJZfvrzEFl--5WkzTzz9e9S-F6ZhInypgpkf82msaauNcLbMXxAuz1K7EIdPBSUR73Rz43_QXwSv6wq7za6VZ-FMBDFtBjSpoNWMjOX7aU0bG9GEuQJ_WOdxXub8gYSn5ddwast5CVgdGU4H2JLIT7XFSk1t8qMY_EJqUbKrB6_Mybqjwq_cBtFfg9BgYHqowsfOYuPnjNwR1NelVypzbQgSHz6IvghuAm9LApKjNiHuc1FMf8AyDDPNvBe9p7V_czKzk339-N7d5expgW68_18X7R7w8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9_xJvKoYsaZf0K5npfvdNNl2DqIDfaa2n13t_YCADCT6PS4f-F-XqhZjL7JiRHghAWmzJK23lVXquifPejwvGbrI2Pr6YkBagIsVPRy5GfknSMIyhbrPnm41Uzk1MmaSGmLjssbujD5uoav902ulVzVfcnekM-lzIQBN8mmj5_XfsY0KfuBcvEepAmDsy92LBTj7fseawCXEWwQ_oaTh2y5sitnSj11xj_php7vpkZHXxGhJ99Yp4L1aMWtRsnBeQ4H8Kr9eFUNAilCqkRCByaws5MP-tlyCbDu1e-XQnO_17WRY7YO-9Lb3tRCJBZS790JTa_CdWXO4oMW9KxZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgefSYaP3fyhHuLKcWvo6rBdCcT8Pap9erqdf0U1sDAMaylvdo1edTZVSQst3qdW2GeVYiGhdSJqr0MWDCJnOwhsLPnioliv0dvq5nnF0yq3pDK-1T7ovaTfgbyvn_h6eaPdgWALOsosNo23BRt2SjaWH0vb4A_RPR19sgOH5JI6-7MqAELyzYbcLyOeLBQZ1bQ_8_CkdgK480M94_LUrazKfyES1eD3K9ya6bePnRb_YqU8bn_nFZtApfshEVuwH92VAUOPZWblAJeqkXg0aUCOu-u5HPEDXjtev-b3KvsQmW-w4yQXeeaODklJp7_snFMka0INEo9d8MiBEv1D1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QaI2Ofl-Fnr4u6xcs4XdND7tun6zv4l8OSj0MujA1Dflq36fW7g2GTacKv12hEvacfHyR5ZaFrTQg8kBU8n1WYIdZaloBN9a0hq-k9qxpVIinEUPU82zBgrrD6fOUlfOHACNDHSyWVc5WQyXVDyJAj_S18L4wAfQQJW2hAskTKcrJmF1QIpcjYYlM14-o37L8O9mmTtxTQ-d4ZXnHZTFOsmZt7x-LzS3ZgYTv9E6JYVJ7rYX-p8uwTigzq8OXLpbbtu31Yz4hq7fvH8WAM9DdQf_a2SYDN4U6pFDjnfxTy-4GX0UWWsNo_pBFYpi2f_nBs2FpJCP5HNHlv7GJ54VAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRVlVuR1GUNU21gVljOj8iJCLdSpbln3UFi22dIh0j8Mht2Rm9Hm9A1hbg6nWZhfNtv66pFU2LSqJNMl-BhvNfZYs_sUeziABJZ0B2Wr1NNnllynqkvtOZdQG5oe53KFs3KFA4VrMqxfrNArcqsZdhQ5080dVsosuZDoou9naQ7luhlC4BCWCRQ-kOs6MYp6YlltEFa2zncReARDGSPULArdhwpui2BY8qQ-5C1eHNqLgsbDLzc51r-JDQSpcS23SGHPvW8aNjv-diQjsWuiQezFzc03uVSro9RKSdmuU85NHGacVCatJOZibWTBYQx-2gBiVrmXBZJFDKaX7D-ihQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید براتون جالب باشه بدونید این اسطوره از ۴۰ دقیقه پیش شروع کرده و داره رگباری کصشعرترین عکس‌های ساخته شده توسط هوش مصنوعی تو تاریخ رو بدون هیچ توضیحی پست می‌کنه و تا الان که ۱۵ تا عکس پست کرده انگار هیچکس دور و برش نیست که بتونه متوقفش کنه یا حداقل ادیتشون کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/81315" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7k9QkxLLdvQtycUnQKGvHd8lFZvzJJDnoOue5u9DVvCNgmeZcb_DImgTfEXHZvxIni8oU0bQ0enxQl50y3V8ikK6Q5mJzBUSE3qwUncwFnSs__bec9i9pFXVTVZuZzk_Bs-a8DWOlTcKlpBj0ngk7xPwPa0gFf_02QEUC4yeCtT31S-yZ10Ej9mhA8xtTVq1vRiFqYKh-gDI7Aso6S9LkMpkFRKwVyLCmyP17xdy6QB3PnYS5unTlRe55Ai1mojWQCT_wZfZA_yCSyDSfEDBrgQN7cvk99kXSjgYvRcVb_F6EoQ7gIdXeNBml4aD1ebI_f3luAu4jr0nvOulGADyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏پسر بیژن مرتضوی اوتیسم داره و استفاده از ویولن سفید تنها راهیه که میتونه پدرش رو در میان نوازنده ها تشخیص بده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81314" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در طول روز حوصلت سر میره ؟ میخوای بری سیرک ولی فلجی ؟ یه چنل میخوای همه کصشریو پوشش بده ؟ افسردگی داریو پول تراپیست نداری ؟ پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/81313" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuRsApYo1o_v6Cgw2yCQaP5Mn34q-k8SD2zoNa1qKltuGE8WJ2pKT-PZSjbh_pRVZfF9Xa6WXBXeJUTQ3WHkpJSkkET6Brq0gUVgQLN-yn4csi2W_vN-v-bqeagC5duU75-0X7rducUiYWaJFSEWeamffmTGdshjNyw8CVVWpSjDEzctfcmxyLZgkwrd7wppJ04lmQhZRhec1D3E1YMpMoEAv-de6F2o5gJFbz9BqQzPHMnTDB1fk_cD6_2Si-s1PkFOzMHNpaXO5pHkUedBNQ1gAWZmYty35Eo3RTmmJCgrChY6DjEGtMpWl4QktXmbCNe8_QevpZL_y8ICUOrCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول روز حوصلت سر میره ؟
میخوای بری سیرک ولی فلجی ؟
یه چنل میخوای همه کصشریو پوشش بده ؟
افسردگی داریو پول تراپیست نداری ؟
پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/81312" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtYUoL7cwZmlnke0gs7XPkiLwPHL_DiPvok6hmzaEhkY_t4ikSgMbOd7aMD5ydYzkeR5s0crkAqa0HQrtUNFwnK034qBzMp-g-HvSNZvHlusBWP__CDfpP2U4nk0zYvKqN8PoG_1MpNzmx5Jq5MTtVcVYVeWlX1kWNIUYoD4vIX_QP1FUD-Bst3hR6vl-KgkktBxQFJkPed79xZuaiJzr18i9t0chXmukcm_Jr270is4PiVOQHgPGNRDyKnmW2etu2VwpaceD4v14QQT0an04Oa_EkEdaOIGsFDtRjESaM2APfo196mUQFZKRAsWKi-6TtAgibqSYiKzsZKVjJPfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتای بیناموس یکم از این پرز یاد بگیر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/81311" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raf1YMLVHzMBMYe6yiKpPHm3Moo_a1b0M5JlFBX4f1wiJK8LKJL8IV2EIXs2OmrnZKX_kqLuEmOUu89RueAtKsZABAp_7waOJiTXOAwsgRMf3WtEK55_IcMno1VPRUS-Prxwz6kVe5QxV8SmCbAbK1JCB3HXZtjYpltMyi8zJik_cxaAnazvzgCQtbNASWmSm_DAqoLKxKPoNld3994dh1HbBoJqfHaBuJv70bKuGjan50lc3ASfuTUJwhUyavfKUcf3xK2DZRIfJ3K0YmKDh3LDuORtYFWaKnswy39v1hOanfvWGaNf1Ib-OsFwVA6GjMJGUlePja0FI0Y9YAQqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم حصین به زنش خیانت کرده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81310" target="_blank">📅 22:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6LV4_y2e-6vt6cMyJpom8KVmyMpV4euy4IFziERAQGbP1So2SeKbFzB8MFby8CCf8laSBheExex9RXFOJbI8vkWRCKrAS1wTNT9BAkKSD6nvXP6sBW9P7KhLb5-IlgKrbScKHzeHx4UEWdRsn0NRIlNMephwPslKJL2pjOo67V7pQ-vSj3voqqj6x1a_HwCC22Zbo8iWhy86lilP0Mi7T8Q8_vNk_mUDhoJspPMAmZ7in7e2dFqdz181k5sJKH182hIRBm2L5ujK0B3hLA6jU4_RR3y4QsmgdRJiICcYmlXNefioBGyhNFxyCxXq43bsqxwOTFKwvRKTIWo7fTzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیامونده رفت رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81308" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivk0eSPJKBaMv_y1Z6vg0DxkMPFOWglVsbJdKIoBsaHFyXkjdyJCNjQp1uZjbv9qWf3NzcdyPW9NicGftNAUpiHpdqfpYwg_5BaEcjYmu15hlRnff7Uw-h9MYcfGNm_UvB8ojJjJL9-xPaYXWSskzQvijpUZ3DBtKiKJMR-Temnh6ytsN2jaOqkgvcfsayQ-n8CBWRavF1SYabmPMxlPnVhhIXFj8-Wq9LwKtlZZZEGEf0s9hk4ar-kDhOASkUjZ9VYRvh2D1OX-9neIaG17-Jr8INv4UFPf74ycyKkvGAfuZLCB6z1sx0WMSGiyDhCRZ_XJfBKCqJSxZ1cphq5-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط کیر، توییت مالک شریعتی (عضو کمیسیون انرژی مجلس) :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/81307" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گیفت شجاع خلیل زاده به تلگرام اضافه شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81306" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81305" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">درسته پژمان جمشیدی از اتهام تجاوز تبرعه شده، ولی هنوزم باید برا رابطه نامشروع ۸۰ ضربه شلاق بخوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81304" target="_blank">📅 21:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUAMSjsK8n-t8wvneL76E8RYWQ8LyN2hGXy0H_sAqPNIbs7sPCRB64ixHb_kqlAt-43lqVP2PLR_UQSGyYxSQDrWTUJ6BYKlOWSBUCA5PDHZ7itg8TlP6Nn2z7bbGhjuq8c5LFVu4VLzYR1SZv8qFWc2uBbxifPLvjkDWvPaeWUi-moGMO4o0aKaUxIA5aNYLsWxvN4dezXoJaoiUaEPsPDx5O4ebuKMMntgtzvT5uuejUqk0Cy4lJ445kg5TCVJLPAxgoX1JAIQxLY7_HjMYMr6yaIFtvLCjymiWTEoXoP4lOdTJOQCQO3b0KSCVVRigqCfqzrTBw0iqmNRD9GxkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وی‌پی‌ان پرسرعت و پایدار با قیمت اقتصادی!
فقط با گیگی 4/800 با بهترین کیفیت ممکن به اینترنت بین الملل متصل شو
😍
🔹
تست رایگان 12 ساعته
🆓
🔹
ویندوز، مک، اندروید، IOS، لینوکس
👁
🔹
دانلود و آپلود نامحدود
⚡️
🔹
مناسب وب‌گردی، گیم و استریم
🎮
🔱
20%
تخفیف ویژه
برای مخاطب های عزیز کانال فان هیپ هاپ
🎁
کد تخفیف
: funhiphop
🤖
برای دریافت اکانت تست یا خرید، از طریق ربات زیر اقدام کنید:
https://t.me/ToPoLvpnbot?start=start</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81303" target="_blank">📅 21:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l25N5gY842ZmKrrfmROzhY4V4jGWhLdcC7S6-te_1AtAs2OOkgo0999jA5eNoklY_YgnBKMcTMGp2mSg_7ASE29MYgXv0WLdZQh3qwZitJId_wSXNoUO5Ofk3xBedgBS73y0Zd6e1VLF8FZ8C4jeIgaF_-ABnGRXF7T9U4eAAZZN7A4k4EXot-5CzG5HY5qLvhe3Fy9jx0CJjPQT3xSwQRZFBp5LLkGBcDQyKRyvTmTi3Qkco-rC_rrgp1tFRTPBBtdJLMO_lQUxqDOHWPCEP9znIYtbSZ8j-F7YeLEiF_qFlYkUyBb3l5_t2R2NG6ZtxePJUgoF09-5IbmbGF--Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید دیامونده بازیکن آکادمی بارساعه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81302" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پژمان اپستین تبرئه شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81301" target="_blank">📅 20:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v6vowwmJFXDNpGFJLSuQWaeOB2dioHljQuQlxlFohVcQcBXNlO6xu1x9hWt0ldfVCivqmmR4SAD4Au4vfQ4E8QKMUPV4Of2xPB8ND--hdk3tJdxuBA5acH_dlw4pM-ALiDQmvU9My4qL2nGVzWVoRyE08WM3mO8MLzYke0Fv9nRiGNc4SwX3wzNY_8QSOhgb0OjVNz-eG8R_ycuE7kHeGSdCKNy_WpZ6CXC2LsjMWggnvpmgICs6CHdDDnXogZGNSd9IBZ9PqYWMPe79gJOknojsOHt17yiGgxiHdOt-8Q4CwX-E1IxYnDW_QJSarOwrmvLHKXw0CR4EvA1pwis0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3hcSvNqee84E6qclFKi7_n59aUFCtIJRAPC0LKY1kMV9GYsOJrxipfMNXF3yKcf4TPQDYiwE1LzdLIUdD3_t5zISl6APxlXy8eH-NYiC7CstBSGL90JyFl0JQHAC8alMarQA8qK4S-hCA5mFDkn_L2Pk3rQswsVSIO9N9Qju-q88H2w9Po_U_maGM5t__jkKIzWuKNW9BpFvly6tA8X64zy6C4HOCAxMccCt-0-HOhIWmpdpMqZ6O4rTGe9LcaXMLiIQKA2ixGnynCv1JBRwXLjup0yc4qk33iJoN7uLzE0BToal6H7jle1AMt2yyLY8N2NjgdWLVBgJXg9RJ6_mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شتوت جدیپ بانو
سیدنی سوئینی
:
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81299" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxARK85BWikOpcYi0Y7s_cge-tCwL74d_qCiIK0W1kaWbVXQ4wFuu_1tHdbb_NKWu_vZ9QRk88aymb-M3vDVQyv5mUwBizsfQb4oAw-B2md-23y6ZHGk3JQ_wOXnzpvKVB_vdyDE7QF9qjhR2o9RWabgpVRaFLiWcOsrILhVcJ3GxoNOTCMX8AdFarehDvPSR5-tx1VMUWE98cj-_rmyWjkMmJFy5vIWxF_ZP0gR_R1E9on8SkB5n_GEqjGrrt4mMIhSwdIhjTqNIQuCzBjT4roKis0jq9G_QR7mJ39QQKAaXLFK8Dysla5Xo_g85XbOWRQyn5QixZtVz9U_yLHDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا ولی کورتوا رو روی مبل تصور کردم
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81298" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7XHENmF-Wt68xt_jnMPgX2dCVmpp3I2T_IYrOlk8KXPMbLOT6aKutl7LD8Vbu_4FhLIg2Fi0k6bep-FZ90o-w2VHybhWTdnoy8p2m9Uh1kZ1FXqPVAV4Ej-6aatyF8JHVbr9fGxjti-YDqKIC2fJb0_nB4t0UrodaJoQnPV2gbKtipuBpablHhiyP9rsBvNPv3dhXvMBYoXApEubESOQfvJ1hvlzZIvcF_kgRXoTvXTEwcZgTfxHwvGfh3INdWm1LzN0ove8bvvr5walN4kAOfmmI142FNW2EBewIYUsinSaPb5bNv6XV62udtfYz6XuZ-lhk3DFXoefGk9R7rfcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81297" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امروز 4 مرداد، سالگرد درگذشت رضا شاهه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81296" target="_blank">📅 17:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=VDgJkWUqCl1-maHvURK8JFiYkX0DHuvstAeyDCvrSG8kV3j-fvHk_9VKIL3_yA4PM6LAPcJVfr0nyyWK7ko2QbLYIeBmL-mlNadDxZXiQztorSzePb_soNb-rpyvMekXzr8-Yn8-7StVJM1voJtDrT6_kfKOzcKsImmOC-gBtQXnlMWAlzfjOF6NLXfzGPrIc7jO2LtUxuwgLfRBvGj29mAdpDX2_VtqSuHuh4LOYRXrXb-hzaYcFvvw7XgqT4zmpGeY3PquB2FVbxuOy1lmLicObe_BM6GdZlYQy9ogOwtr_mloQkL-_Ae5nb5aqv2foU-sB4EwXtlXZOgc6WjjbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=VDgJkWUqCl1-maHvURK8JFiYkX0DHuvstAeyDCvrSG8kV3j-fvHk_9VKIL3_yA4PM6LAPcJVfr0nyyWK7ko2QbLYIeBmL-mlNadDxZXiQztorSzePb_soNb-rpyvMekXzr8-Yn8-7StVJM1voJtDrT6_kfKOzcKsImmOC-gBtQXnlMWAlzfjOF6NLXfzGPrIc7jO2LtUxuwgLfRBvGj29mAdpDX2_VtqSuHuh4LOYRXrXb-hzaYcFvvw7XgqT4zmpGeY3PquB2FVbxuOy1lmLicObe_BM6GdZlYQy9ogOwtr_mloQkL-_Ae5nb5aqv2foU-sB4EwXtlXZOgc6WjjbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنگ (هیدن یاس)
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81295" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=FCz7tP6ZK9FwJkuQFLaj5dZXUonmmobNBh-iPYYsq12wthrOtaFAuMBwKjnNvQNj5yAz9iTyLdAPOn5M6-2q7XCAeBnUVXjGp-ozAOI9qRHWKNyMm9drJoOOna_o6VXdDZVQH4xy6Xhd_PRpJH8ZDtKkzfTYnLKFF6Q9Fj_K5dVNJPAuF4wgd_5eW_ImBu9Kd3UA4jFgzg0gI8sMf3IVf4KSFVQj6peLpzJjd0hrU4o9l1R7UHn5isKcy586zpKFrZA8DDI4xfat_jHavqhl6NEK9fSoH2Z9L1hUhr0FodjIDq0mY8oD3120Jvkom0hxauqvUoXJ9STEmmj_wxzCfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=FCz7tP6ZK9FwJkuQFLaj5dZXUonmmobNBh-iPYYsq12wthrOtaFAuMBwKjnNvQNj5yAz9iTyLdAPOn5M6-2q7XCAeBnUVXjGp-ozAOI9qRHWKNyMm9drJoOOna_o6VXdDZVQH4xy6Xhd_PRpJH8ZDtKkzfTYnLKFF6Q9Fj_K5dVNJPAuF4wgd_5eW_ImBu9Kd3UA4jFgzg0gI8sMf3IVf4KSFVQj6peLpzJjd0hrU4o9l1R7UHn5isKcy586zpKFrZA8DDI4xfat_jHavqhl6NEK9fSoH2Z9L1hUhr0FodjIDq0mY8oD3120Jvkom0hxauqvUoXJ9STEmmj_wxzCfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آگاهی_سازی
دوستان این ویدیو با صداگذاری ساخته شده و واقعیت نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81294" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Letu8RiAMQKe5QCV7TkwmnkSB8RXOYDItY_jPii4OUzUpNlMJnOMg5nRLTG4aNpSzE0JIpOJrqSrYwl_m0PtVPGJ0I38hlyr6Dryl5rhrBA3Md20Rz0F8qwOT5BDSVH81afKwUrI0Hul8jbpBo5glL9D8NlpuDKfdydQUfqhBqekI51B3PXmweDF62c2QRUezh9mSm4l5QV5x8CQXugHrXejqRZSrEPqEnRQkfyWcPJKJ1Tlo8giyKcu223oflPMsOPbLoOduUAvmTP3Suv458nHAo_awabcprIQJY0jyFwPYH2I2u_CJ9Sx7qvNEq7q_YDsf1iiFqjKfHxaDEKQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسام سهرابی هم بعد این که لختش کردن و موهاشو زدن دیگه کلا از رپفارسی خداحافظی کرده و بلاگر شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81293" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81292" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=JXdyjmwwD1AWja4NJ3OaZRcaHlE3xVEFhaAA-OemsutknFfcnLByytwqYJeJtYICHs4QokIyH6wg8gZcIRwpNx7Q7d4umcaMoC4lpjXgwkBKirPSYqOUoYBQZugpfpFKYvYJ5MxNo28nn0o6VxSgxYxm9K8ar5LhOmACoVtjsl47PKyGhCfBInZ8pw5TRf04trKavjnPXYfwhhJ4OZNc-oWvl5k6RYI9pA50abeupAvDtLk0ik5oYjvq0uK_1d_Van1xJILYSdhaZCI4zCr8KVIcT6BiX9OCUm7oI9dLg8Uxu1zAl7qJE4jD88L09LFfjR-i9oBStCvntHpz8xbzIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=JXdyjmwwD1AWja4NJ3OaZRcaHlE3xVEFhaAA-OemsutknFfcnLByytwqYJeJtYICHs4QokIyH6wg8gZcIRwpNx7Q7d4umcaMoC4lpjXgwkBKirPSYqOUoYBQZugpfpFKYvYJ5MxNo28nn0o6VxSgxYxm9K8ar5LhOmACoVtjsl47PKyGhCfBInZ8pw5TRf04trKavjnPXYfwhhJ4OZNc-oWvl5k6RYI9pA50abeupAvDtLk0ik5oYjvq0uK_1d_Van1xJILYSdhaZCI4zCr8KVIcT6BiX9OCUm7oI9dLg8Uxu1zAl7qJE4jD88L09LFfjR-i9oBStCvntHpz8xbzIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب آنتونی جاشوا موزیک سیاوش قمیشی رو به عنوان تم ورودی خودش به رینگ انتخاب کرد و وارد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81291" target="_blank">📅 14:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">امروز ۴ مرداد، سالروز درگذشت رضاشاه پهلوی، بنیان‌گذار سلسله پهلوی است. او در ۴ مرداد ۱۳۲۳ در سن ۶۶ سالگی، در زمان تبعید در ژوهانسبورگ آفریقای جنوبی درگذشت.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81290" target="_blank">📅 13:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNtPIHf7Y-mhTFNbvxWYM9fCA9gOF5cT4dhrX3FB2Xgw5K2KhSHjfmlxFRXQSsMBUSID8l74VrwfH_yonSlfsmplkOjrc7Kop5amGKBNeKbctBxZ5Qf5lQ4Myapvbdwl3f7v61bz7rDkfEr31B8wmMa6XVSJ8wBiz9CgP0kB4HHwC13wcQHxETwpPKcs1Qw9Jjo-SiRDabaepe4UWloZ3JYHXi6dJbGiKhOxVUa04ruilEMHufmLWoDHUnNfsosve-1uURUkxVQLWQJ02KNmFlbJJLdAYRcxjRQIpUnln2m2zA_79KQFxknMc7yMoXPQQROX7TbTGYInaXG3n1iwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی دیروز در پاریس، با فعالان، هنرمندان و نمایندگان سازمان‌های مربوط به جامعه LGBTQ+ ایران دیدار کرد.
شرکت‌کنندگان در این نشست از جمله شش خواسته اولیه جامعه رنگین‌کمانی برای «یک زندگی معمولی» در ایران را تشریح کردند که عبارتند از: ۱. حق زندگی، تحصیل و کار در محیط امن ۲. جرم‌انگاری کوییرستیزی ۳. حق تشکیل خانواده ۴. صدور مدارک شناسایی متناسب برای افراد ترنس ۵. دسترسی به خدمات درمانی متناسب ۶. آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81289" target="_blank">📅 13:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81288">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جفری اپستین تنها شانسی که تو زندگیش آورد این بود که زمانی خودکشی کرد که ادمین اکانت حافظه تاریخی حوزه پوشش زیاد گسترده نبود و اونقدرا هم حوصله‌ش سر نرفته بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81288" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81286">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1QVydnzEvXq3IvQnxIGmPF4TQCzTCEGGrTllgnKRpyFA1If5GzTxS67y-3yty6iSM1_y8QN2a13GXc48bPOCOPf0NESq37eYL8uz83z0kM3xs8Z1ZKrH8FHKTJFCZYKFDIEZ6qMtjvtq4w-Fd5KtwaXP6YF3aM4Cc_xE-my0a_-5Sq6GTkEBCkh8bEDHDqi1A4bfCdbE71_5A104Y43eEAPXgaYeOqHl9XbBlShRoC_NAqOo8fu-92hbOWffsfyeFwz6LzOBkKlUOcGBtrUHX_5vl-dsoCKdVuEnNtlOB8bQ6s48ZTyipeg3vyFSU6Ht2r90CWjmZTz7PH7mjKYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو دیدید؟ رئال مادرید دو سال دیگه برا همین 250 میلیون یورو پول میده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81286" target="_blank">📅 12:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81285">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1KL4Rq17Fc0Vc5y3p8qeJ6XuzOwujm1MkUheffs4Oi7I0js_MM-nIZgwFL1dXoh_AebFvEbGUsBrISXBnasGmbkNxP3X_NX2PY0XiNADaAla7UeNqBVv_b8Y7hAwcpCd5BYiPtcgaEEChu0xwhw1gu3JwPFyx7MlRdDP4a8goq78xjq5rcwT0GlcchpAvJT37kNyjv3tIhlo_lPm6dVNCBH5DliUszXVgqDn9j2nb6COHossYw2RAyP_o64e_MCEF485VHd1fBkdGVkwKzpCaqy9LbxeaLYGIdYgBxxo0Gd_pMMa3necax3LBEzy5zj23edZDHu9e9N7AJJapCHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید صدف زن هیپهاپولوژیست :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81285" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81284">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq4PBnJCHC5sCTxyhgecM30-bgIVgyLaiGP1voAnqjcG14kFVIbu6o6NtNUJXRUqMmHwSKy_x2oiZOTOdcRps7ja6MheZZs9NopSepfTjiDv_CNcLGeh6dqanzDKp-fH8CQBl3xRKGS7P_cfnp_Gvs18IChOEo6ma920CMWIhG9eHPdvCBU4dIDpJWLCPNIJ-bWqGGG6poX294dg7iwvKhKY6F8iAzX6ytWgSm7I_pc0eBLN3N0xrj4BD56eaKVh_oxhTM7Q4zSCLuGZ-a2ly9GE-cztrxqfoW888hPXlZmzBFh8n0yIok5SQ4Etj3iddwajqkfhfjHFDU3SAgBBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81284" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81283">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clNPWzEbOc82UxDN97CC63dnWKyjyK8Qb0YBnsTwe9DUKYmx1EkxTYCGcm0o3tNAmOQbob7BI3ZE1eI6Mfaun4vOvYfVoUAGu_AQyqoyPfRs170t1w0E2n2zxahopZrdodjcvvUWUW4ptJMZNc6truXytLPkKRUYKi7RahKDT736Ct84T30koaQa0hp0MIkv_P1bvNBCvjp-Byj6BqCRvtS__0qLRU2mWh_EBn1b4BIzZnYGbeXfG09SIHdFis1hjP6D-nrvYwSEzoHBJrNloazBSf0D_CWeCUrz_PZNC1GgHAjLcWTBhAbWtg5FDLO8C4u2PkvCSXuy-ZaH_wfR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تجهیزات آمریکا که تو دو هفته‌ی اخیر زدیم نابود کردیم ۲۰۶ تا ۱۰۰ میلیون دلار قیمتشه.
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81283" target="_blank">📅 11:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81282">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خداوندگاران هفت آسمان را سپاس که امروز من را لایق زنده ماندن و توانا در شنیدن این معجزه‌ی جدید تمدن بشری دانستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81282" target="_blank">📅 10:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81281">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یادش بخیر امتحان نهایی فیزیکو فرمولاشو نوشتم تو کاغذ بردم سر جلسه، بعد نمیدونستم کدوم فرمول برا کدوم سواله، افتادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81281" target="_blank">📅 10:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81280">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvw_Ox9_s9PITz81PSqT4Sz-Cggx3t5nXGfqVYeflY-vylEUIyx41Ze9nLfL1uMlXR1tlziqayn2EqkujgXvmcn0PaqcN5Mnf_pjQ9WHK9tQkdcNFOwoB3D3jYOYpyr3nyPJTg0LV_hp1pJjp52kGYMXKPjniubXe9IEqkpL3EgNV_hPjrD7LUDOES4LAiFk5K7_sfxa5LNx494GzmiU-vuAKMrbkP4lAPync7WsFXiQXijlg91yU8QSqAbHc_iiHL2njek4RAdDj3hxuN7cNEuaOZAcFFkIocoyYMWl7c3XVmZXzbSl-jQ3ETs5BNRUvZokZD2DzGpCuqCj-dUSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاسی بسه، بریم دعوا جنسیتی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81280" target="_blank">📅 10:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81279">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آلوارز کلا سه تا مشتری داره پاریس، آرسنال و بارسا، آرسنال چون داره وینی رو میخره کنار کشیده، پاریسم چون فران رو داره میخره کشیده کنار، فقط بارسا مونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81279" target="_blank">📅 09:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81278">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امیدوارم زودتر بمیری مهدی اونوقت حافظه تاریخی داستان پسرعمو و F35 زدن رو به همه میگه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81278" target="_blank">📅 09:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81277">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81277" target="_blank">📅 09:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81276">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81276" target="_blank">📅 09:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81275">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یارو پیرمرد افتاده مرده ملت ریختن سر جنازش میگن ۳۰ سال پیش خایمالی میکرده، خب کیر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81275" target="_blank">📅 09:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81274">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سلبریتی تو ایران همین که خایمالی نکنه کارشو انجام داده بیشتر از اون بکنه یا فراریش میدن یا یه بلایی سرش میارن دیگه اون آدم سابق نشه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81274" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81273">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgdYzdUwq7bE4bpr8U2fxoJ7DkGyWCz96oX5_zSBNHmO2dSloON_1_X_w2BFQf7ccHzB9jE-odeZ__Mc_NwaaqavS_3Q63Xc982a0iPMhYDkYtYdmOVFGMJjEoWXLbsKRzRw2Yaiol_OgHFYoAmUnGXMYAWSxNVonTP8PWF3dzbRWOVAJH5-G0Qce8eZjujAnU9XDQdxBhZNTHA3iMsOGaDGzCROMXCW3uVqD2s_6OIEUhCt2z5v_mEYypOLyAcKFasnpGuZvOB5yZwQ8QNe1fqianjnnyJMDwz7clHnOGTDqVfU--Led7ClXLPd_iuV8u6rwwp6YOnKEO1WGZPE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشید مظاهری اومد مستقیم گفت، چیکار براش کردید که از بقیه هم انتظار دارید بگن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81273" target="_blank">📅 09:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81272">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEZgsQO4zsaqsauPN4QtsFMBjZ_g3dk1qkUuT8qcFUk-d-49GWqtC10JSDyfYud8r8Zby0ZhYHDbPxnzbvo0gu4b6qulzWWjW-nF_TiCXoYq8wcnblHsWt2Efp7bJ4j3b7AUdfFzpzSPhOKksR0ULNiKzM-FjQZcpRpkCoXPYXZ27TTq8bhT6oqf2PZJ4JQr_sP-se1EmgQsybv_hyR2HQK-ym4rmnV0WtfWR4Y-KKjX9uYO41DdQOZSZC3qys9YnH9USIz3vP70nYxzKtB8XyLI5eQp9JzIBuvfzCWx-8MfJODpUv5PaLi_bv9q-mVswBi_pzCmQAh5S0XXmzphdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81272" target="_blank">📅 09:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81271">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فیتای ویناک و هیپهاپولوژیست از سپاتیفای پاک شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81271" target="_blank">📅 07:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81270">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZRyF5-qkGDtr8MNlfCYrfpNEbbd0nE2dRs6wth5pA5vFcO5FbxPoIuXhT8xbjKksOwsCt8qkzSibePBsUFenWGIU3M7akQFVy8m5eljzS8GCcdzbq_0c3mOEVIHCb0mXaPbm4H-1vwXdM6ppjxvFA28BnzWgsOQttZiyCzfYWDmp7NMK8gQ1Dm02vkftmk_riTt_w3xbdhisrhkrN0STXMkEf2WK21FnaWV84QKU0EqD6e5aTnLfF9HXaok5feivXwkuMq9lxQNhIkeUTp5T-xjn7SQSHqx35mZ-14IJLrfZ-h6JLHjuTzYtKKQng0lmnCq_afcc-1THpVJIecNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود هم پاخور بوده پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81270" target="_blank">📅 02:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81268">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایمان کیرم دهنت چرا کسی جز تو صدا نشنیده</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81268" target="_blank">📅 01:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81267">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زدنننننن</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81267" target="_blank">📅 01:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81266">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1-mbSKu9_kH0Z_Iprk7P1_75umFvX-kPF1KaOiFWcn5HGj__kSqPqy3kGsxL9v3r0Rzfd6En04jsvpvq3m-BS8l-NirfZm-IJ6hZW7BR7-vHqlaRyda5fHrM4Zg9tyClRJAux95ViVBACkTDHx-xXZ-LZKHHb0RDht9amFxZsdXljGTltFSjmg_66ZRyJ4tpdR_4BKxEcH-e7Hkd1NidO5ghsSFGFO-O0wl60vrVLLIbIUUREEidUOXjf1LS-rU2jXVd--OuY-_8-p2c0NjqxQanAdgkBfy-gWWJj5Z1C8bBIGvCmurNTDuWFc8p3eEM3f1YDBW83Mhp1hUz3yCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی رپفارسی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81266" target="_blank">📅 01:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81265">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81265" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81264">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH6qhBOY2O9OYRRb75nByfYtDKNm_B0YDORFOTeQTLDyCVDZ0Qg_4AouIvHSXJQq-8oGLQ3AxbidwTF50H21I9OaeTvrF5Rt7kvG50VzvasxUv8Pl1ygL-LSajtFG6aYHoPN0Stfjj_sMvTTIJBLiHkIdLtzVKhWvLTWlyzlqrSWaOoqA6IqPcARTyku4Z7KbWldQQ4cM53v9U4-YJXwi15wVUkPqI-sJCbgdt5ihPkj0w9q16X5tShKgOSQrvIvWsr_VPGRjxr-TvPQOc9GoVE5V-ZQoZIGCGJvga3i2kJ8R0QWdICG3eKJbhRY-TXxpU8z_D3lOhuiLDHCW40m1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81264" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">طبق جنگ ۴۰ روزه امشب شدید میزنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81263" target="_blank">📅 23:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تموم شد، دیگه هیچوقت، هیچوقت نمیزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81262" target="_blank">📅 23:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ در گفتگو با شبکه LCI فرانسه، درباره ایران:
به مامان توماج صالحی قسم این دفعه
این‌دفعه به شرافتم قسم بار آخره که به دیپلماسی فرصت می‌دم و اگه برا بار ۸۲۸۲۸۳۹۸ام، ۱۰۰ درصد از ۱۲ درصدِ نصف خواسته‌هام برآورده نشه یه جوری حمله می‌کنم که اصلا خیلی شدید و دروازه های جهنم و این داستانا قول می‌دم قول
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81261" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هوف
کانال ۱۴ اسرائیل: ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81260" target="_blank">📅 22:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81259">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b585792e34.mp4?token=vjt4_BzN6v8F9_3pRf7oSatorHRNBTDfbpJEMPF9ZDeUkBQc6tFHH5C62LouWfFhjmI62ucI5WRWhJoZxwWrSeZHQrOkxG_2oM32YoNSPr0to8VJ9LoelWno4FPrNVIOmz-TxAfR_GrGhpbGkyWefzfVDOtViUc3OxKYB9cuOSb5NpYj_KnlPzZm33iRwBqpA3Z4oRzML72VbBNzAQT9MXXziesSeaipJSyh8vnapUyXqO1QrAKFF16z92GLlwfcKCnbLYl1oR8uwjZr14wtqaYQ7QClNs1NCZ9EAoa4cBTAyPUQbpO_hP2ZwyJHJbCeZ3kR_6NFusm26V8OjGZiFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b585792e34.mp4?token=vjt4_BzN6v8F9_3pRf7oSatorHRNBTDfbpJEMPF9ZDeUkBQc6tFHH5C62LouWfFhjmI62ucI5WRWhJoZxwWrSeZHQrOkxG_2oM32YoNSPr0to8VJ9LoelWno4FPrNVIOmz-TxAfR_GrGhpbGkyWefzfVDOtViUc3OxKYB9cuOSb5NpYj_KnlPzZm33iRwBqpA3Z4oRzML72VbBNzAQT9MXXziesSeaipJSyh8vnapUyXqO1QrAKFF16z92GLlwfcKCnbLYl1oR8uwjZr14wtqaYQ7QClNs1NCZ9EAoa4cBTAyPUQbpO_hP2ZwyJHJbCeZ3kR_6NFusm26V8OjGZiFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از مادر رپفارسی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81259" target="_blank">📅 22:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81258">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=cedOob3Ndg1iMFR2GrU36QDbY6aUu_FfzdUuFkdMrHYsfRGfhOcjVlNf4D3UmesVKL2SBcvqqYQdTTJutZhPFA0PmMMpVuEtWDIUCmfpqhnXpO9WuUuSXwUSIfIYLcj9t-0k_Yv9ogZBB_6OWyVR5yOkj5kzuQrnD3PlKTksI_Q0yAkhw_nOw1x07wHEKyRr1nh8pA2dt5syZp56h6OmQ6J2NHvacrwMp1X3MZwkTsAQfecUDqaMpOENJnQ_WMYHrABKlREwV1BXtK2uYrD1Eq_i1TUDBl6CfC8CqF6ULpgUSF0R-ZHniOIUkiYmClAuNnPWraMBg6PVEuyuXaq5Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=cedOob3Ndg1iMFR2GrU36QDbY6aUu_FfzdUuFkdMrHYsfRGfhOcjVlNf4D3UmesVKL2SBcvqqYQdTTJutZhPFA0PmMMpVuEtWDIUCmfpqhnXpO9WuUuSXwUSIfIYLcj9t-0k_Yv9ogZBB_6OWyVR5yOkj5kzuQrnD3PlKTksI_Q0yAkhw_nOw1x07wHEKyRr1nh8pA2dt5syZp56h6OmQ6J2NHvacrwMp1X3MZwkTsAQfecUDqaMpOENJnQ_WMYHrABKlREwV1BXtK2uYrD1Eq_i1TUDBl6CfC8CqF6ULpgUSF0R-ZHniOIUkiYmClAuNnPWraMBg6PVEuyuXaq5Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس داوینچی درحال لذت بردن از مذاکره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81258" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81257">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0O0qghal86zqYxUNtqtQunBYv2E_lc7HXXM0pAnW0dH1ZCQ0LMQcXI1zVs28GiPU-aPyXeU0zEUeX4woHlgBNf3pMIUVFH6ygpi3RIrYFiZ3kzJ6XK5Ud9eAPVgaxV0NU7oXQ5UySR7iF5ZRTZgKLG8x3WR4FVhutqEFBC721AmajXJHSwECDhNRC0H8wApmxjyonXlEcB0Ym373humPfp5OxyHdeKEdG8NF1cQkmourd7_SDKrvfK4xRjk5qKaL4FmLGEBjwdOCr4z6XfS4PDL4xQTf6U0HIHgjA9VbFfZO6E3hzrqMBXmUHa7x6kLjB7slWcb_XB1pIx8muM2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81257" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81256">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzMbyRon6wmOQe9SAauOtmlcSHY63FDBVlSlYqC__I-6YBAPgqlTImPITNqc2lfYriXj6vv01xX2WvzR3BDE3xm5TRmCVbfokyJjpag-wZtbVzmOon26qcrHGXK3dJf43_X7QOgExoWPlMgVVALHnAQxtjQyoqelz-DXP6EHZW1uJIGPskEnnds1hms5zRan3UZChkZhe6XRvmXxDU4ij1IST1BPbHkqe7Wo5WMBx-wIcWxc8CZGQoDn_RlI0gwAag3a4suhKalb3R6Py4VMgEzySbc7RI1btmMIgOzmVisEJlTXzzSFyxq2zf5Au5VSr1BMVPBikcb30ThAGUivLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید: این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81256" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81255">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید:
این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته که بگذره خواهیم دید چه خواهد شد.
#تاحدودی_بماند_به_یادگار
#تحلیل
#اکسپلور
#مراد_الله_ویسی
#خدابخشیان
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81255" target="_blank">📅 20:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81254">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K375AuzEZgmiS-df0b5rdIDH6stjIG09pdlmlC99HA96ugiMooHQpzm08M79C20Cm3-QdZjsXtz9vtL4CA_6I6o3XfDTFa4lcv480m6WmilItzAj4jfxKwc6l_srq6JGfJe2puy0CZ4ZOxTo42BwkWnG0zXDCh0e9Fc3NbECYIthI2stnEVWdIvwSNcTt3A1OfTfJeLrNqjdcCZSXMWU9VJOmRU4GXKo_XjucWn6ojcnBLJWO7JhVH8NDvHP6i9Fe513xmQC0mKFmbOeD3md4NREM4f7PY0I8a57ojaSxQAqAN_BaDVkXIYIFQcXqynHPtzcXlAFMOXRJ-GEYUGA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید باشگاه فرهنگی ورزشی لیورپول :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81254" target="_blank">📅 19:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81253">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قوه قضاییه اعلام کرد که ساعدی‌نیا حق باز کردن کافه نداره.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81253" target="_blank">📅 18:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81252">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kErL8nMWzeQ4IW-ER6vYzxUVreJ2VKXx9jG_WU3gH7R1IOonInNS0_4vy4UTFcIoXmDe7z5XOGE8OX5DUyXMJmgL21GFz8Ll7I-VqVGQ4jyMuN6U6Goxy8okcCwFen2lUTOqg-F44QmfSUDeZWzQETsTycs9Nrt63mPjfU60go6hWMl5lCxUqZiQV9yC1zSC7y_Efg7YcVy2XD9cQO2vd9upRyTCMs6eoTuJDdIGdGVSaT2gKYIjd03PVnAypFyarGxysj1RBxDWvE2o8Y6RSovYZQSffGwFIeDPJ3uGdpUXPgu69TczXNL0GKT_PvlqqoHhr-KC9DDLu40WsEwmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستم اینو قبلا یه جایی دیدم.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81252" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81251">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ame4yNIuSTfBj66CiCs6aPCZyqs2wL5RHn_n8JTN_yj209dTkpVE1TxWyjt4lUAM6V6ryzbyA4nUms_M3R8oo86MFkLBkwX8vLkvYcRG3d_t14OsfLl7Ux5DO7srnruXnVehiESyTMRhJS27JlfjezvUCXQ80JrDA7rfBe2asAZkZu0FR-Sj0O_jKaKD8ISyAjnJejwR_xibJPC_OyRYZdubY9v4sg1JfsP-3DlGoJoh-dmGG3ZwkjXXdgzwDReFWM42Q5udAW3B3H6rkekLqbIgaXi4OZCxHT9w53zoKjbOCVsbM8tPcr4E_BsPlBu7JnvKmCQqGrX6oNRqFTQzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پورتو
🇵🇹
-
🏴
استون ویلا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۲۲:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پورتو در ۵ بازی اخیر خود مساوی نکرده است.
✅
استون ویلا ۴ بازی اخیر خود را برده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۳.۷ گل در هر بازی بوده است.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r3
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81251" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81250">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری وای‌نت اسرائیل درمورد اینکه چرا دیشب نزدن و چه خواهد شد:
ترامپج می‌خواست خیلی عظیم و گسترده بزنه ها، ولی گفت یه فرصت دیگه به ایران میدم شاید دکتر عراقچی یه کاری کرد، پاکستان و قطر هم دارن تمام تلاششون رو می‌کنن.
ولی برای اسرائیل، این یک فرصت موقت برای ایران است که تغییری در ارزیابی کلی ایجاد نمی‌کند: توافق‌نامه آمریکا و ایران از بین رفته است و
احتمال دستیابی به یک توافق نهایی که در آن ایران تسلیم شود، صفر است
.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81250" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81246">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLz0AewPlq-pXsD9P_-GtgVFmJ3i-Nr8t-2IkWvFQY4fNY6uC413Gf1qeeS2dFOWsmBbd6jxWj_hrjkPGNNfenCdQeJM6-c87a7tAN4cNfW1GwYJA_KJ6ByTX3JTsgD_CI5qVEflnJDU-z3MuZpbWqNuBhKAZGpujygB96yh13RlMRoz5E-0JFwCSTTuRVSbGGbhR_b4F7u5yq1aXn7dZZxAJyu1JEuy5yEhn59lSsfNEQ7zuFGJZlx36GDc604OMFYXsyvXwj_RZF9IBfKKn4XLogUnJcIGso-SP6SKQdUgQu6uj4jMOp4Qemqlj2_a84LOliKqKNaPehLnSIkr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدبخت مهدی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81246" target="_blank">📅 16:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیویورک پست:
آمریکا در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایرانه؛ «پیچیده‌ترین عملیات نظامی تاریخ»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81244" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عباسدرمن: اگه وزیر نبودم میرفتم پشت لانچر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81243" target="_blank">📅 15:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81241">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5IilYAfN0CaVSfDH4eKivhkUQkCI06XYP_o2TZRDsjXKHsOuejvg6BnX-hASYX82t2ewe_GY5FFYOw4JIeUHKiFKLTAUVKGgf98HVDInhBvDu5zGqAtaBPw9A8pp9SX1RqbbgkyjJsssezp98SdZ64s2CLzk-mV0aWyjYILdqyVFNDT4mwaCebtf9R30upWpY8LwDgyLc8AhXzQi1PCpRadfv4eNWXztpENYU-D5CmXGAed8f8TFBt1GAPtoFpVB0QdJlUUJPw7i2s_dOoYtjtMuGRjUDB9DGb_mIrmrjPOUjWf89LhBTeH-XctZNqdqQTGDiSdmLJtE_BPZKaZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ما بزرگ شدیم علاقه به کودک ترند شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81241" target="_blank">📅 14:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81240">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCeta2u-gdSfoT5DTZg9z2ru2YSEKPcLEOZwTqhe8ya2TJkaCtfd0L1aryJgGrdH8fcr-q-CPFOsjGA6lZYFXgHETmj_0LlaFgCRVsPzwLDe5Xw3zqgD_JYVVCEhajaXn263OZlv6t_f17-RcuwVHl_i1EV76tYs05PbjO1qIZ4E83M7Zt8-nL0fF0PiCng0j-arg9WHbi99Y65c-TyDQs9-SKfg_YI2O9mFaMT8vtzNnGU2v8Cg73uXbS_3hSEGx0qDvAawm_QyLvoVS2ccFWILwVHGNVYIr3j4zu4O1M2M2ZnSZkny6i3YUaG-3GJ7TpZRQgK3vbdv6rs5Z0xM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81240" target="_blank">📅 14:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81239">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اوکراین چنتا کشتی روسی که محموله های نظامی ایران رو حمل میکردن تو دریای خزر زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81239" target="_blank">📅 13:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81238">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شهریاری، گوینده جمله مگه تنگه ارث مامانته:
متوهم ها باید قبول کنن‌ که آمریکا ابرقدرته و حریفش نمیشیم.
پ.ن: نه مشتی صبر کن رستاخیز بزنیم آمریکا این سری دیگه از خاورمیانه میره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81238" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81236">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsvEYagQp-s4Tqo47BAckoa6OSHKhcTvl6i0vEpjkNPdciHm-K0DH_MJUq_aeTNyJxW70uXXN_KSZ_DUm9Ld2x79tupE12VaZb4f-y4hbSASK8BxsEWwXWR468iL-ec-H_N-N660SQuxta3pvKSIFiPQbdKshhiUBer_0wk6-RAZCbz8jUNKq3ys5DbLqtEMSgtDr5-3AIPd1CHynU-I4GHZC9BUIF3q1vnFFY9ePrX4WtzMN53wGh6rJ1P0zWfRGFzrdvB2gEP6pHdUC7LlhkkcJwlR6Ozm2MRX5SkUCmd1fBHMu0Vbk_JSA8ZjHUXSwfVSZ-XQ4F4GHeXh3L2C3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXDMCvGo5VvAqyTpjhZ_wNy_bAag1tez9aME-fvS_utvV0Zr3Er07qdEjPouv9F1cUAfR78CzkLosaJI1D2qVbWRuwcypiZ6v1Z66rMaQrJmDuV_RrcABN7FHC3P8DrCppFrfzZSPI5WqP0z6d7yHKvovl2MZ_HOwnNLZ5CYqXZEeZMYC6szWmektoLbh8lqBpQBzOARYMD5ozOiEIDaG1QiZXxCXnl-ywiBAK6QGRR0kt4xCiafZxQlW-pMcezV_G2gtdBxdJN9Dm7bRqlkzb_Dk-34dy_0FHyAfuI9i5UYtrlAE9RhXgKcNaLvKHsThWpb2kX0iFPr4CzJ0p333Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اسب که فقط ۵۶ سانت قدشه رکورد کوچیک ترین اسب دنیارو زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81236" target="_blank">📅 13:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81235">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هوا گرمه کصشر نگید</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81235" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81234">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
ترامپ: رسانه ها به دستاوردهای فوق العاده من توجه نمیکنن. من رهبر ایران که یه آدم قدرتمند بود و همه ازش میترسیدن رو کشتم و الان یه دیکتاتور همـجنسگرا شده رهبرشون. اینکه یه قوی رو کشتم و جاش یه همجـنسگرا گذاشتم دستاورد نیست؟!  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81234" target="_blank">📅 11:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1e370de3.mp4?token=UFGiKEBVS86x_2X1C0uVAHM_lw0fKorl42o-dLro74T06X0811QBxS-BgOIxangYLAD52rWb0-KkXtxNKM_vDzMJdT9o3HGIa8nz6753JxqtmHpvq4DgqXZgAmKYzQewVE93bnYnWlzYAb7p0_t39ZAAOpMrmixy82EP9syOnMrSwEVpNUNNKTndIq5u3HjXg8ESRejnanN9pEka-yKi7diIA7TiFDmF88zcu5Bn0IXt5vqUFQSHx17nulqt9fz6ptloLKo4_bymMHjKZSZyuoWix9DspthPEPdpgxHX3OCNrc92fOFZ4CybR7R17uifcLvfKrZg_BkR-F563YH02Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1e370de3.mp4?token=UFGiKEBVS86x_2X1C0uVAHM_lw0fKorl42o-dLro74T06X0811QBxS-BgOIxangYLAD52rWb0-KkXtxNKM_vDzMJdT9o3HGIa8nz6753JxqtmHpvq4DgqXZgAmKYzQewVE93bnYnWlzYAb7p0_t39ZAAOpMrmixy82EP9syOnMrSwEVpNUNNKTndIq5u3HjXg8ESRejnanN9pEka-yKi7diIA7TiFDmF88zcu5Bn0IXt5vqUFQSHx17nulqt9fz6ptloLKo4_bymMHjKZSZyuoWix9DspthPEPdpgxHX3OCNrc92fOFZ4CybR7R17uifcLvfKrZg_BkR-F563YH02Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ:
رسانه ها به دستاوردهای فوق العاده من توجه نمیکنن. من رهبر ایران که یه آدم قدرتمند بود و همه ازش میترسیدن رو کشتم و الان یه دیکتاتور همـجنسگرا شده رهبرشون. اینکه یه قوی رو کشتم و جاش یه همجـنسگرا گذاشتم دستاورد نیست؟!
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81231" target="_blank">📅 11:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uE6oB-sCt_t1Io_XMuwJdSTlF78yFEHteRf9r8vrZP2m-DY6PuRmq977MehSAIM4_fOzarnyRUmQ3WNNdDwmscHt7wSZTLdPAiIIcIjXeW7LAPRJS4JVcckpKvd0PPv3W4qnsD33GrfOOjLc_RAy1uftA-yLEWsHhLH5xQZomW2RrkVw3GdcpbhCyurdYuvLuU4JKrbVlSIuGusVVQuJNzBVqSq8n3AdOR1l-aegp05HM45YIMuj7TaDjP0g_uEanr32KzWYAvwmF2sy0-VZ90VfJJHPGb4AJug6PM-i3lvMIrmwvqjs_kmYZxhKBsfl8pUrWVMU1Rj1NLaBQm-09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پورتو
🇵🇹
-
🏴
استون ویلا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۲۲:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پورتو در ۵ بازی اخیر خود مساوی نکرده است.
✅
استون ویلا ۴ بازی اخیر خود را برده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۳.۷ گل در هر بازی بوده است.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r3
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81230" target="_blank">📅 11:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">کانیه وست
😂
@FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81229" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7_N7YMhBonzToXhIQ3oPpSB3Ylkxe8Jp_PsL2hZJx2Nc-SC9dNGnd16e39mgcCY7Ct7-P6CFL12b0rHdaQ68BkC2DdKS68W4SLeRVSn9puK_48-2GNRbu0aUnuF_o2VDs8pG-85QSB4HKUr-SzHUtU2tAuyKDF-PEGSY4ojXQxFqYLyanglOORH_pDXG6-YUCIWrnm0SozXO93W1ON92vex8lWkdUCYvA02xRQ_MysWQ-BPD0MVWAUbN4pD4ncA0IXGCQRD1bY1ILw-Wt93nSjfH96AiJdbMiyyodEg-ifkwCb7tmBG9Pexm5tYIsLCOXUC_Jh0zAi4VwKdRRkUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانیه وست
😂
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81228" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قدرت اول منطقه برق ما دو ساعتش تموم شده ۲۰ دقیقه تاخیر دادین چرا نمیاد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81227" target="_blank">📅 11:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چین حجم تسلیحاتی که آمریکا تو خاورمیانه مستقر کرده رو دید و رید، حالا خودش دست به کار شده و قراره کنار پاکستان میانجی‌گری کنه تا قبل از اینکه آمریکا حملاتش به ایران رو دوباره شروع کنه توافق رو نهایی کنن
علت چصه دامپ تتر و نفت در روز گذشته هم همین خبره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81226" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یمن همینجوری حملاتش به عربستانو ادامه بده واقعا برمیگردن دوران ملخ خوری</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81225" target="_blank">📅 10:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یمن همینجوری حملاتش به عربستانو ادامه بده واقعا برمیگردن دوران ملخ خوری</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81224" target="_blank">📅 10:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz1Jm0lt8RX98Qnlcuq4zQxsLkpmI1GrTlOXir9-8cnHquxacLgL4hngfijBHpnPDSZV7PN_f03KbcVtImuMHJ4TBNcAKVNzqQuMdQxCvbUPm8Jk0UUXOtzAUG68yAXQv62BnRR9NRBmKpnvsRFByRM1ZEgmT7rufYvBiUMeCHJ42ZBoLpuNms49hC5zY6lZe5U0vV3fuzObrHY1BGYlul9Pg_s-NTvQ_9bGm4YzGZZ7ibKZQhAebBVY2MaKG0iOu2-OPME0NlHumLVFhW73enID_mbsqT_Z7s_aPwQgV2SjuSUKuM2JKMIw24oaNoBy1WgbXqD_riNpjwB1rpDKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#بالاخره_یه_پست_رپی
پست جدید ایلاکه که احتمال منظورش اینه که "پوری خارت گاییدس فقط صبر کن" ولی روش نمیشه مستقیم بنویسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81223" target="_blank">📅 09:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLZDkXMLPjh_EDxDKoPuW3lLxBT3uj4zrxvlFd8wDo1evPJYbSL5-yiTVeLF-5ijbUzJ8QcjCxt-Mo64w4du3QizVo3DixvWBxYI1exnJ4GCmDwywKNH2h-flMKAZ0PkHw5c9vSTrvCmLTLoJtGprvezFMb6DEx_rXZbQnT7aFT9DA0IspJHyfBfOlXlJc0i4naf6BOUJuJDsjk1a3eJH6dmZCeBAcAjFSWKZkJ1nmoebwfgmPD2X9rrer3ygjZc7tEvHoMZPxT0L4ttub1lRy8RQZEezGiyD9yMxtecTSdfbeezzzZgV1AQHJpiay-4yv9N1QGWDc5vHCRe2jgFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باور کنید اینا با آمریکا تبانی کردن خار عربارو بگان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81222" target="_blank">📅 09:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81221">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این وینگری که رئال داره میخره از قیافش معلومه فقط برا کار تو مزرعه ساخته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81221" target="_blank">📅 09:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81218">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لبران جیمز بعد از ۸سال از ال‌ای لیکرز جدا شده و رفته فیلادلفیا سیکسرز
تینیجرای ایرانیِ همیشه در صحنه، آماده شید جرزی این تیمو بخرید و مدعی بشید که از ۵ سالگی طرفدار این تیم بودید و بخاطر لبران نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81218" target="_blank">📅 08:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81217">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">علل حساب اگه جلسه سرانی چیزی صبح هست لغو کنید که اوضاع مشکوکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81217" target="_blank">📅 04:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81215">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رفتم قسمت آخر برنامه ابوطالبو دیدم، بلافاصله رفتم هایلایت لوکاکو جلو سیتی تو فینال سی ال رو نگا کردم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81215" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81214">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شرکت هواپیمایی اتریش، تمام پروازهای خود به تل‌آویو را تا اطلاع ثانوی لغو کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81214" target="_blank">📅 02:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81213">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امشب آمریکا نزد، من زدم  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81213" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81212">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">امشب آمریکا نزد، من زدم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81212" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81211">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عربستان و یمن همچنان دارن کون هم میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81211" target="_blank">📅 00:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81210">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIvw2-mxnWVG-S0Eb8il8A568seTDg0tiyV8ntWnwV5U-YiXZvTFQBFjk_ZWSEugI-3FUsCOwtZQNdDbSDRdPVbx8ZTnURo_cbyjL0mx2b9CxRWwI4_VlGCJDkVFKd1AiWYRV_ApVT4EdwVtViupVAgoD0t04UhiZv7rqrhro4I2GxwzifDhuj9odCNRDkF2ZF54LLhb6dv8ncWDCUF0JKMxX-aC6tHMRaEgJpRNRQF608hUSptaKa74Glk6sHxHfi7vyOkPAtj4fmLvpNpVn5U6aX-EWcKWn2YzLLipaU46Rif03TOc1Mop5LiiLljiB4fT_qYfu2EP7VIxE1X4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81210" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81208">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کوسه و زیدی درحال لذت بردن بعد از قهرمانی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81208" target="_blank">📅 23:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81207">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESvCWIOkuEUyh2_VWbjifozbAez5KfxpA9s3bRZsjbMcHQt4cUxxzXZhw9ywUVfVcFJU-LVed-5gHvDmwesn0TKjQ7dZ9kErfleYwAyo5CwxYeT8AkQI3OAXHRzFXZhbDybY4HtDm2xU2JuC3QfH9XXciNux_k3uQfdTXQH1VYNosf2M9-XpNfq7-Bqq5-xPTjsVZMZ2kagtSGm2TRsOncMeJUTLeKGPJFSfn3fIiXSSh0tTYSKPSRzmG2WBg-WyQtO1VqEcny-2hnZdz56NEtjJ51bawwyrfWAcn-akihRcoGGoXsgmlQ9L_l711Aue8_becf8GdPXqWUwKpbdVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه و زیدی درحال لذت بردن بعد از قهرمانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81207" target="_blank">📅 23:26 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
